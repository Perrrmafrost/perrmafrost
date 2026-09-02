# -*- coding: utf-8 -*-
"""
Veo render pipeline for S01E01 "The Package".

This is the mechanism Perplexity's video feature uses - a prompt handed to Google's
Veo 3.1, a clip of up to eight seconds handed back - driven by the shot database
instead of a chat box. It locks the two leads to the reference plates on every
shot with people, splits long shots into an optimal cover of 4/6/8-second pieces
chained from the previous piece's last frame, assigns each line of dialogue to
the piece it falls in and to the person who is actually in frame, retries with
backoff, persists every paid operation the moment it is accepted so a crash or a
rate limit never pays twice, and resumes.

Written against google-genai 2.21.0 (the SDK source was read, not remembered),
then adversarially reviewed: 19 confirmed defects in the first version are fixed
here and listed in production/08-qc/pipeline-review.md.

    python3 tools/render.py plan                       # cost table, no key
    python3 tools/render.py dry-run                    # every request through the SDK's own
                                                       #   wire converter, no network
    python3 tools/render.py models                     # Veo models your key can see (free)
    python3 tools/render.py smoke                      # a deliberate trio: two-shot with dialogue,
                                                       #   the double, one chained shot
    python3 tools/render.py smoke --shot SH0004        # or one specific shot
    python3 tools/render.py render [--from A] [--to B] [--model M] [--parallel 4] [--yes]

Credentials (one of):
    GEMINI_API_KEY=...                                       Gemini Developer API
    GOOGLE_GENAI_USE_VERTEXAI=true GOOGLE_CLOUD_PROJECT=...  Vertex AI: adds seed + generate_audio
    GOOGLE_CLOUD_LOCATION=us-central1

Nothing here has touched a live key. `dry-run` proves the wire shapes; `smoke` is the
first paid call and it tells you exactly how many calls it will make before it does.
"""
import argparse, hashlib, json, os, sys, time, threading, functools, concurrent.futures as cf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
PROMPTS = P("production", "06-shots", "shot-prompts.json")
RENDERS = P("renders")
MANIFEST = P("renders", "manifest.json")

# ------------------------------------------------------------- Veo constraints
# SDK: aspect_ratio "16:9 (landscape) and 9:16 (portrait)", resolution "720p and
# 1080p", person_generation "dont_allow, allow_adult". Clips are 4, 6 or 8 s.
# The master is 2.00:1, so we generate 16:9 at 1080p and centre-crop to
# 1920x960 in conform. The prompt tells the model where the crop will fall.
DURATIONS = (4, 6, 8)
ASPECT, RESOLUTION = "16:9", "1080p"   # --resolution overrides
MAX_REFERENCE_IMAGES = 3       # SDK docstring: "up to 3 asset images or 1 style image"
FRAMING_NOTE = (" Framed for 16:9 but composed for a 2.00:1 centre extraction: keep all "
                "essential action inside the central 89% of the frame height, nothing "
                "important at the very top or bottom edge.")

# List prices per generated second, audio included. Sept 2026 figures; confirm at
# https://ai.google.dev/gemini-api/docs/pricing before a full run.
RATES = {"veo-3.1-generate-preview": {"720p": 0.40, "1080p": 0.40},
         "veo-3.1-fast-generate-preview": {"720p": 0.15, "1080p": 0.15},
         "veo-3.1-lite-generate-preview": {"720p": 0.05, "1080p": 0.08},
         "veo-3.0-generate-001": {"720p": 0.40, "1080p": 0.40},
         "veo-3.0-fast-generate-001": {"720p": 0.15, "1080p": 0.15}}
def rate_for(model, resolution): return RATES.get(model, {}).get(resolution, 0.40)
DEFAULT_MODEL = "veo-3.1-fast-generate-preview"
RETRYABLE = (408, 429, 500, 502, 503, 504)

# The locked reference plates: face-centred, >=1024 px on the short side.
# MB shots use all three slots (one of him, two of her); singles get two of her
# or one of him. These are the ONLY images the model ever sees of the leads.
_M = [P("reference", "miles_plate_frontal.png")]
_L = [P("reference", "lauren_plate_frontal.png"), P("reference", "lauren_plate_threequarter.png")]
PLATES = {"M": _M, "M_JKT": _M, "L": _L, "L_CARD": _L, "D": _L, "MB": _M + _L, "FIG": [], "NONE": []}
IN_FRAME = {"M": {"MILES"}, "M_JKT": {"MILES"}, "L": {"LAUREN"}, "L_CARD": {"LAUREN"},
            "MB": {"MILES", "LAUREN"}, "D": {"DOUBLE"}, "FIG": set(), "NONE": set()}

def load_shots():
    return json.load(open(PROMPTS))["shots"]

# ------------------------------------------------------------- pieces
@functools.lru_cache(None)
def pieces_for(duration):
    """Optimal cover of a shot by 4/6/8-second pieces: least generated seconds,
    then fewest pieces (fewer seams). 9s -> (4,6) not (8,4); 17s -> (6,6,6)."""
    need = float(duration)
    if need <= 8:
        return (next(x for x in DURATIONS if x >= need),)
    best = None
    def rec(rem, acc):
        nonlocal best
        if rem <= 0:
            cand = (sum(acc), len(acc), tuple(sorted(acc, reverse=True)))
            if best is None or cand < best: best = cand
            return
        if best and sum(acc) >= best[0]: return
        for x in DURATIONS: rec(rem - x, acc + [x])
    rec(need, []); return best[2]

# ------------------------------------------------------------- dialogue
def line_offsets(shot):
    """Where each line falls inside the shot, using the same reading-speed model
    the subtitles use, so picture and captions agree about who speaks when."""
    dl = shot["dialogue"]; d = shot["duration_s"]
    if not dl: return []
    w = [max(len(x["line"]), 12) for x in dl]; tot = sum(w); cur = d * 0.03; out = []
    for x, wi in zip(dl, w):
        out.append((cur, x)); cur += d * 0.94 * wi / tot
    return out

def lines_for_piece(shot, pieces, idx):
    lo = sum(pieces[:idx]); hi = lo + pieces[idx]
    return [x for t, x in line_offsets(shot) if lo <= t < hi or (idx == len(pieces) - 1 and t >= hi)]

def speech_block(shot, lines):
    if not lines:
        return (" No one speaks in this section; ambient sound only." if shot["dialogue"] else "")
    on = IN_FRAME.get(shot["subjects"], set()); parts = []
    for x in lines:
        c, l = x["character"], x["line"]
        shout = l.isupper() and len(l) > 12
        if c == "VOICE (O.S.)":
            parts.append(f'a voice from outside, through the front door, muffled, warm and unhurried, says: "{l}"')
        elif c == "SYSTEM VOICE":
            parts.append(f'an off-screen automated announcement voice, flat and pleasant, says: "{l}"')
        elif c == "DOUBLE":
            parts.append(f'the woman on the pane says, flat and unhurried, without taking a breath first: "{l}"')
        elif c in on:
            parts.append(f'{c.title()}, on camera, {"shouts" if shout else "says quietly"}: "{l}"')
        else:
            parts.append(f'{c.title()}, off-screen and out of frame, {"shouts" if shout else "says quietly"}: "{l}"')
    tail = " Only the people described are in frame." if len(on) == 1 else ""
    return (" Dialogue, spoken naturally and in sync: " + "; ".join(parts) +
            ". No subtitles, no captions, no on-screen text of any kind." + tail)

# ------------------------------------------------------------- prompts
def face_lock(shot, with_refs):
    if not with_refs: return ""
    if shot["subjects"] == "D":
        return (" Her face and age must match the supplied reference images exactly - it is the same "
                "woman - but here her hair is worn down and loose and there is a fine pale scar under "
                "her left eye. She holds perfectly still and does not look at the person she is "
                "speaking to; her eyes stay fixed slightly off to one side, on someone else in the room.")
    return (" The people in this shot must match the supplied reference images exactly: same face, "
            "same hair, same age, same build.")

def base_prompt(shot):
    return (shot["prompt"].replace("2.00:1 widescreen, anamorphic-adjacent spherical lensing",
                                   "spherical lensing") + FRAMING_NOTE)

def build_prompt(shot, pieces=None, idx=0, with_refs=True):
    pieces = pieces or pieces_for(shot["duration_s"])
    p = base_prompt(shot) + face_lock(shot, with_refs)
    if idx > 0:
        p += (" Continue this exact shot from the given frame: same people, same faces, same "
              "wardrobe, same lighting, same camera position and lens.")
    p += speech_block(shot, lines_for_piece(shot, pieces, idx))
    return p + " Continuous take, no cuts, no camera movement beyond what is described."

def pane_carries_text(shot):
    a = shot["prompt"]
    return shot["device_in_frame"] and ("DO NOT GO BACK" in a or bool(shot.get("countdown_reads")) or
                                        "number appears" in a or "11:00" in a or "00:0" in a)

def build_negative(shot):
    n = shot["negative_prompt"]
    if pane_carries_text(shot):
        return n + ", subtitles, captions, lower thirds, watermark, any text that is not on the pane itself"
    return n + ", subtitles, captions, on-screen text, lower thirds, watermark"

def needs_people(shot):
    if shot["framing"] == "TITLE": return False
    if shot["character_assets"] != "-" or shot["dialogue"]: return True
    a = shot["prompt"].lower()
    return any(k in a for k in ("hand", "thumb", "finger", "palm", "wrist", "figure", "her ", "his "))

def reference_images(shot, T):
    return [T.VideoGenerationReferenceImage(image=T.Image.from_file(location=pth),
                                            reference_type=T.VideoGenerationReferenceType.ASSET)
            for pth in PLATES.get(shot["subjects"], [])[:MAX_REFERENCE_IMAGES]]

def request_for(shot, pieces, idx, T, vertex, prior_frame=None):
    """(source, config) for one piece. First piece: text + plates. Later pieces:
    image-to-video from the previous piece's last frame - the SDK forbids mixing
    reference_images with an image source, so continuity is inherited from the
    frame and the prompt says so instead of asking for plates that aren't there."""
    cfg = dict(number_of_videos=1, duration_seconds=pieces[idx], aspect_ratio=ASPECT,
               resolution=RESOLUTION, negative_prompt=build_negative(shot), enhance_prompt=False,
               person_generation="allow_adult" if needs_people(shot) else "dont_allow")
    if vertex:
        cfg["seed"] = shot["seed"]; cfg["generate_audio"] = True
    if prior_frame is None:
        refs = reference_images(shot, T)
        if refs: cfg["reference_images"] = refs
        src = T.GenerateVideosSource(prompt=build_prompt(shot, pieces, 0, with_refs=bool(refs)))
    else:
        src = T.GenerateVideosSource(prompt=build_prompt(shot, pieces, idx, with_refs=False),
                                     image=T.Image(image_bytes=prior_frame, mime_type="image/png"))
    return src, T.GenerateVideosConfig(**cfg)

def req_hash(shot, model, vertex):
    plates = [hashlib.sha1(open(p, "rb").read()).hexdigest() for p in PLATES.get(shot["subjects"], [])]
    pcs = pieces_for(shot["duration_s"])
    body = [shot["shot_id"], model, ASPECT, RESOLUTION, list(pcs), plates,
            shot["seed"] if vertex else None,
            [build_prompt(shot, pcs, i, with_refs=(i == 0 and bool(plates))) for i in range(len(pcs))],
            build_negative(shot)]
    return hashlib.sha1(json.dumps(body).encode()).hexdigest()[:12]

# ------------------------------------------------------------- client
def client_and_types(need_key=True):
    from google import genai
    from google.genai import types as T
    vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "").lower() == "true"
    if not need_key:
        return None, T, vertex
    http = T.HttpOptions(retry_options=T.HttpRetryOptions(attempts=6, initial_delay=2, max_delay=60,
                                                          http_status_codes=list(RETRYABLE)))
    if vertex:
        c = genai.Client(vertexai=True, project=os.environ["GOOGLE_CLOUD_PROJECT"],
                         location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"), http_options=http)
    else:
        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key:
            sys.exit("no GEMINI_API_KEY in the environment. `plan` and `dry-run` need no key.")
        c = genai.Client(api_key=key, http_options=http)
    return c, T, vertex

def status_code(e):
    return getattr(e, "code", None) or getattr(e, "status_code", None)

def with_backoff(fn, what, attempts=6):
    """The SDK retries at the HTTP layer; this covers what surfaces as an exception
    anyway (its retries exhausted, or a transport error) without re-submitting a
    paid operation more than we must."""
    delay = 2.0
    for n in range(attempts):
        try:
            return fn()
        except Exception as e:
            code = status_code(e)
            if code not in RETRYABLE and not isinstance(e, (ConnectionError, TimeoutError)):
                raise
            if n == attempts - 1:
                raise
            time.sleep(delay); delay = min(60.0, delay * 2)

# ------------------------------------------------------------- manifest
_lock = threading.Lock()
def load_manifest():
    return json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {"shots": {}}
def save_manifest(m):
    with _lock:
        tmp = MANIFEST + ".tmp"
        with open(tmp, "w") as f: json.dump(m, f, indent=1)
        os.replace(tmp, MANIFEST)
def record(m, sid, **fields):
    with _lock:
        m["shots"].setdefault(sid, {}).update(fields)
    save_manifest(m)

# ------------------------------------------------------------- render
def last_frame_png(mp4):
    import subprocess
    out = mp4 + ".last.png"
    subprocess.run([os.environ.get("FFMPEG", "ffmpeg"), "-y", "-loglevel", "error", "-sseof", "-0.05",
                    "-i", mp4, "-frames:v", "1", out], check=True)
    return open(out, "rb").read()

def concat(files, out):
    import subprocess
    lst = out + ".txt"; open(lst, "w").write("".join(f"file '{p}'\n" for p in files))
    subprocess.run([os.environ.get("FFMPEG", "ffmpeg"), "-y", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", lst, "-c", "copy", out], check=True)

def wait_for(c, T, op, sid, i, timeout, log):
    """Poll a long-running operation. On timeout the op stays alive server-side and
    is recorded as in_flight by the caller, so the next run resumes it - a paid
    operation is never abandoned and never re-submitted."""
    t0 = time.time()
    while not op.done:
        if time.time() - t0 > timeout:
            raise TimeoutError(f"{sid} piece {i}: still running after {timeout}s (op {op.name})")
        time.sleep(10)
        op = with_backoff(lambda: c.operations.get(op), "poll")
    if op.error:
        raise RuntimeError(f"{sid} piece {i}: operation failed - {op.error}")
    resp = op.response or op.result
    if not resp or not resp.generated_videos:
        reason = (resp.rai_media_filtered_reasons if resp else None) or ["no video returned"]
        raise RuntimeError(f"{sid} piece {i}: filtered/empty - {reason}")
    return resp.generated_videos[0].video

def render_one(shot, c, T, vertex, model, man, timeout, log):
    sid = shot["shot_id"]; pcs = pieces_for(shot["duration_s"])
    rec = man["shots"].get(sid, {}); files = []; prior = None
    for f in rec.get("pieces_done", []):          # trust a piece only while it is on disk
        if os.path.exists(f): files.append(f)
        else: break
    if files:
        prior = last_frame_png(files[-1])
    for i in range(len(files), len(pcs)):
        path = os.path.join(RENDERS, f"{sid}_p{i}.mp4")
        t0 = time.time()
        if rec.get("status") == "in_flight" and rec.get("piece") == i and rec.get("op"):
            op = T.GenerateVideosOperation(name=rec["op"]); log(f"  {sid} resuming op for piece {i+1}")
        else:
            src, cfg = request_for(shot, pcs, i, T, vertex, prior_frame=prior)
            op = with_backoff(lambda: c.models.generate_videos(model=model, source=src, config=cfg), "submit")
            record(man, sid, status="in_flight", op=op.name, piece=i, pieces_done=files, model=model)
        vid = wait_for(c, T, op, sid, i, timeout, log)
        if vid.video_bytes:
            open(path, "wb").write(vid.video_bytes)
        else:
            c.files.download(file=vid, destination=path)
        files.append(path); record(man, sid, pieces_done=files, op=None)
        log(f"  {sid} piece {i+1}/{len(pcs)} ({pcs[i]}s) in {time.time()-t0:.0f}s")
        if i + 1 < len(pcs):
            prior = last_frame_png(path)
    final = os.path.join(RENDERS, f"{sid}.mp4")
    if len(files) == 1: os.replace(files[0], final)
    else: concat(files, final)
    record(man, sid, pieces_done=[])              # consumed into the final file
    return final, sum(pcs), [f"chained {len(files)} pieces"] if len(files) > 1 else []

def select(shots, frm, to):
    ids = [s["shot_id"] for s in shots]
    lo = ids.index(frm) if frm else 0; hi = ids.index(to) + 1 if to else len(shots)
    return shots[lo:hi]

def cmd_render(a, only=None):
    c, T, vertex = client_and_types(); os.makedirs(RENDERS, exist_ok=True)
    if getattr(a, "edl", None):                  # e.g. the 60s trailer: render only what it uses
        import re
        only = set(re.findall(r"SH\d{4}", open(a.edl).read()))
    shots = [s for s in load_shots() if s["shot_id"] in only] if only else select(load_shots(), a.frm, a.to)
    man = load_manifest(); rate = rate_for(a.model, RESOLUTION); todo = []
    for s in shots:
        h = req_hash(s, a.model, vertex); rec = man["shots"].get(s["shot_id"], {})
        if rec.get("status") == "rendered" and rec.get("hash") == h and os.path.exists(rec.get("path", "")) and not a.force:
            continue
        if a.force or rec.get("hash") not in (None, h):   # forced or inputs changed: start over
            with _lock: man["shots"][s["shot_id"]] = {}
        todo.append(s)
    calls = sum(len(pieces_for(s["duration_s"])) for s in todo)
    gen = sum(sum(pieces_for(s["duration_s"])) for s in todo)
    print(f"{len(todo)} shots to render ({len(shots)-len(todo)} already done): {calls} paid calls, "
          f"{gen}s of generation, ~${gen*rate:,.0f} at {a.model}")
    if not todo: return
    if not a.yes and input("proceed? [y/N] ").strip().lower() != "y":
        sys.exit("aborted")
    log = lambda m: print(m, flush=True); ids = {s["shot_id"] for s in todo}
    rl = {"consecutive": 0}
    def work(s):
        sid = s["shot_id"]
        if rl["consecutive"] >= 5:
            record(man, sid, status="skipped", error="rate limited: stopped after 5 consecutive 429s; re-run to resume")
            return
        try:
            record(man, sid, hash=req_hash(s, a.model, vertex))
            path, secs, notes = render_one(s, c, T, vertex, a.model, man, a.op_timeout, log)
            record(man, sid, status="rendered", path=path, generated_s=secs,
                   cost_usd=round(secs*rate, 2), notes=notes, error=None, op=None)
            rl["consecutive"] = 0
        except TimeoutError as e:
            record(man, sid, error=str(e)[:400]); log(f"  {sid} still in flight - re-run to resume")
        except Exception as e:
            if status_code(e) == 429: rl["consecutive"] += 1
            record(man, sid, status="failed", error=str(e)[:400]); log(f"  {sid} FAILED: {e}")
    with cf.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        list(ex.map(work, todo))
    mine = {k: v for k, v in man["shots"].items() if k in ids}
    done = [v for v in mine.values() if v.get("status") == "rendered"]
    print(f"\nthis run: rendered {len(done)}  failed {sum(1 for v in mine.values() if v.get('status')=='failed')}"
          f"  in flight {sum(1 for v in mine.values() if v.get('status')=='in_flight')}"
          f"  skipped {sum(1 for v in mine.values() if v.get('status')=='skipped')}"
          f"  spent ~${sum(v.get('cost_usd',0) for v in done):,.0f}")
    bad = [k for k, v in mine.items() if v.get("status") in ("failed", "in_flight", "skipped")]
    if bad: print("re-run to resume/retry:", ", ".join(bad))
    print("next: python3 tools/conform.py --source auto --audio clips")

# ------------------------------------------------------------- plan / dry-run / smoke
def cmd_plan(a):
    shots = load_shots(); rate = rate_for(a.model, RESOLUTION)
    if a.edl:
        import re; ids = set(re.findall(r"SH\d{4}", open(a.edl).read())); shots = [s for s in shots if s["shot_id"] in ids]
    pic = sum(s["duration_s"] for s in shots); gen = sum(sum(pieces_for(s["duration_s"])) for s in shots)
    greedy = 0
    for s in shots:
        d = s["duration_s"]; g = []
        while d > 8: g.append(8); d -= 8
        g.append(next(x for x in DURATIONS if x >= d)); greedy += sum(g)
    calls = sum(len(pieces_for(s["duration_s"])) for s in shots)
    chained = sum(1 for s in shots if len(pieces_for(s["duration_s"])) > 1)
    refs = sum(1 for s in shots if PLATES.get(s["subjects"]))
    print(f"model                 {a.model} @ {RESOLUTION}   (${rate:.2f}/s, audio included, list price)")
    print(f"shots                 {len(shots)}   ({calls} paid calls; {chained} shots chained)")
    print(f"picture seconds       {pic:.0f}s  ({pic/60:.1f} min in the cut)")
    print(f"generated seconds     {gen}s   (optimal 4/6/8 cover; greedy would be {greedy}s)")
    print(f"shots with face lock  {refs}   (reference plates attached)")
    print(f"estimated cost        ${gen*rate:,.0f}")
    print(f"wall clock            ~{calls*90/a.parallel/60:.0f} min at {a.parallel} parallel ops (~90s per call)")
    print("\nexpect to REGENERATE 20-40% of shots on a first pass (face drift, captions, motion).")
    print("a realistic first-cut budget is 1.3x the figure above.")

def cmd_dry_run(a):
    _, T, vertex = client_and_types(need_key=False)
    from google.genai import models as M
    conv_cfg = M._GenerateVideosConfig_to_vertex if vertex else M._GenerateVideosConfig_to_mldev
    conv_src = M._GenerateVideosSource_to_vertex if vertex else M._GenerateVideosSource_to_mldev
    shots = load_shots(); built = calls = with_refs = 0; example = None
    for s in shots:
        pcs = pieces_for(s["duration_s"]); prior = None
        for i in range(len(pcs)):
            src, cfg = request_for(s, pcs, i, T, vertex, prior_frame=prior)
            body = {}                       # the SDK's own converter: raises on anything mldev rejects
            conv_src(src, body, None); conv_cfg(cfg, body, None)
            calls += 1; with_refs += bool(cfg.reference_images)
            if s["subjects"] == "D" and example is None: example = (s, body)
            prior = b"\x89PNG"
        built += 1
    print(f"{built} shots -> {calls} requests passed through the SDK's "
          f"{'Vertex' if vertex else 'Gemini Developer API'} wire converter; {with_refs} carry reference plates")
    s, body = example
    body = json.loads(json.dumps(body, default=lambda o: f"<{len(o)} bytes>" if isinstance(o, (bytes, bytearray)) else str(o)))
    for r in body.get("instances", [{}])[0].get("referenceImages", []):
        r["image"]["bytesBase64Encoded"] = r["image"]["bytesBase64Encoded"][:24] + "..."
    print(f"\nexample wire body for {s['shot_id']} ({s['subjects']}):")
    print(json.dumps(body, indent=1)[:2600])

def cmd_models(a):
    c, _, _ = client_and_types()
    seen = [m.name for m in c.models.list() if "veo" in (m.name or "").lower()]
    print("\n".join(seen) if seen else "no Veo models visible to this key")

def cmd_smoke(a):
    shots = load_shots()
    if a.shot:
        pick = [a.shot]
    else:
        two = next(s for s in shots if s["subjects"] == "MB" and s["dialogue"] and len(pieces_for(s["duration_s"])) == 1)
        dbl = next(s for s in shots if s["subjects"] == "D" and len(pieces_for(s["duration_s"])) == 1)
        chn = next(s for s in shots if len(pieces_for(s["duration_s"])) > 1 and s["dialogue"])
        pick = [two["shot_id"], dbl["shot_id"], chn["shot_id"]]
    chosen = [s for s in shots if s["shot_id"] in pick]
    calls = sum(len(pieces_for(s["duration_s"])) for s in chosen)
    gen = sum(sum(pieces_for(s["duration_s"])) for s in chosen)
    print(f"smoke test: {', '.join(pick)} -> {calls} paid call(s), {gen}s generated, "
          f"~${gen*rate_for(a.model, RESOLUTION):.2f} at {a.model}")
    a.force = True; a.frm = a.to = None
    cmd_render(a, only=set(pick))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["plan", "dry-run", "models", "smoke", "render"])
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--shot", default=None)
    ap.add_argument("--from", dest="frm"); ap.add_argument("--to")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--op-timeout", type=int, default=1800, help="seconds to wait on one operation before leaving it in flight")
    ap.add_argument("--resolution", choices=["720p", "1080p"], default="1080p")
    ap.add_argument("--edl", default=None, help="render only the shots named in this EDL (e.g. the trailer)")
    ap.add_argument("--force", action="store_true"); ap.add_argument("--yes", action="store_true")
    a = ap.parse_args(); RESOLUTION = a.resolution
    {"plan": cmd_plan, "dry-run": cmd_dry_run, "models": cmd_models, "smoke": cmd_smoke, "render": cmd_render}[a.cmd](a)
