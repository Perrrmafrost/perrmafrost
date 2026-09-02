# -*- coding: utf-8 -*-
"""
Veo render pipeline for S01E01 "The Package".

This is the same mechanism Perplexity's video feature uses: a prompt handed to
Google's Veo 3.1 and an 8-second clip handed back. The difference is that this
one is driven by the shot database, locks the two leads to the supplied
reference plates on every shot, chains clips for shots longer than eight
seconds, records cost, and resumes.

Written against google-genai 2.21.0 (the SDK source was read, not remembered).

    python3 tools/render.py plan                       # cost/duration table, no key needed
    python3 tools/render.py dry-run                    # build every request via SDK types, no network
    python3 tools/render.py models                     # list Veo models your key can see (free)
    python3 tools/render.py smoke --shot SH0126        # render ONE shot to validate the key
    python3 tools/render.py render [--from SH0001] [--to SH0320] [--model ...] [--parallel 4]

Credentials (one of):
    GEMINI_API_KEY=...                                       Gemini Developer API
    GOOGLE_GENAI_USE_VERTEXAI=true GOOGLE_CLOUD_PROJECT=...  Vertex AI (adds seed + generate_audio)
    GOOGLE_CLOUD_LOCATION=us-central1

Nothing in this file has been run against a live key. `dry-run` proves the
request shapes compile against the SDK; `smoke` is the first paid call and it
is one shot, on purpose.
"""
import argparse, base64, hashlib, json, os, sys, time, threading, concurrent.futures as cf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
PROMPTS = P("production", "06-shots", "shot-prompts.json")
RENDERS = P("renders")
MANIFEST = P("renders", "manifest.json")

# ------------------------------------------------------------- Veo constraints
# From the SDK: aspect_ratio "16:9 (landscape) and 9:16 (portrait) are supported",
# resolution "720p and 1080p", person_generation "dont_allow, allow_adult".
# Veo 3.x clips are 4, 6 or 8 seconds. The master is 2.00:1, so we generate 16:9
# at 1080p and centre-crop to 1920x960 in conform. Nothing is stretched.
DURATIONS = (4, 6, 8)
ASPECT = "16:9"
RESOLUTION = "1080p"
MAX_REFERENCE_IMAGES = 3         # SDK docstring: "up to 3 asset images or 1 style image"

# List prices per generated second, Gemini API / Vertex, audio included.
# Sept 2026 figures; confirm at https://ai.google.dev/gemini-api/docs/pricing
# before a full run - the plan command prints the total this table implies.
RATES = {
    "veo-3.1-generate-preview":      0.40,
    "veo-3.1-fast-generate-preview": 0.15,
    "veo-3.0-generate-001":          0.40,
    "veo-3.0-fast-generate-001":     0.15,
}
DEFAULT_MODEL = "veo-3.1-fast-generate-preview"

# The locked reference plates. These are the ONLY images the model ever sees of
# the leads; they are what "locked faces" means in practice.
PLATES = {
    "M":  [P("reference", "miles_reference_source.jpg")],
    "M_JKT": [P("reference", "miles_reference_source.jpg")],
    "L":  [P("reference", "lauren_reference_source.jpg")],
    "L_CARD": [P("reference", "lauren_reference_source.jpg")],
    "D":  [P("reference", "lauren_reference_source.jpg")],     # the double IS her face
    "MB": [P("reference", "miles_reference_source.jpg"), P("reference", "lauren_reference_source.jpg")],
    "FIG": [], "NONE": [],
}

def load_shots():
    return json.load(open(PROMPTS))["shots"]

def pieces_for(duration):
    """Split a shot into Veo-sized generation pieces. <=8s: one piece rounded up
    to 4/6/8. Longer: 8s pieces then a rounded remainder. Conform trims to the
    exact EDL length, so rounding up never shows on screen."""
    d = float(duration)
    if d <= 8:
        return [next(x for x in DURATIONS if x >= d)]
    out = []
    while d > 8:
        out.append(8); d -= 8
    out.append(next(x for x in DURATIONS if x >= d))
    return out

def speech_block(shot):
    """Veo 3.x renders speech written into the prompt. We hand it the lines and
    tell it - twice - not to draw captions, because it will otherwise."""
    if not shot["dialogue"]:
        return ""
    lines = "; ".join(f'{d["character"].title()} says, quietly: "{d["line"]}"' for d in shot["dialogue"]
                      if d["character"] in ("MILES", "LAUREN", "DOUBLE"))
    return (f" Dialogue, spoken naturally and in sync, not shouted: {lines}. "
            "No subtitles, no captions, no on-screen text of any kind.")

def build_prompt(shot):
    p = shot["prompt"]
    if shot["character_assets"] != "-":
        p += (" The people in this shot must match the supplied reference images exactly: "
              "same face, same hair, same age, same build.")
    p += speech_block(shot)
    p += " Continuous take, no cuts, no camera shake beyond what is described."
    return p

def build_negative(shot):
    n = shot["negative_prompt"]
    if shot["framing"] not in ("TITLE",):
        n += ", subtitles, captions, on-screen text, lower thirds, watermark"
    return n

def reference_images(shot, types_):
    plates = PLATES.get(shot["subjects"], [])[:MAX_REFERENCE_IMAGES]
    return [types_.VideoGenerationReferenceImage(
                image=types_.Image.from_file(location=pth),
                reference_type=types_.VideoGenerationReferenceType.ASSET)
            for pth in plates]

def request_for(shot, piece_len, types_, vertex, model, prior_frame=None):
    """Compose one generate_videos call. Returns (source, config).
    First piece: text + reference plates. Later pieces of a long shot: image-
    to-video from the previous piece's last frame - the SDK forbids combining
    reference_images with an image source, and the frame already carries the
    faces, so continuity is inherited rather than re-asserted."""
    cfg = dict(
        number_of_videos=1,
        duration_seconds=piece_len,
        aspect_ratio=ASPECT,
        resolution=RESOLUTION,
        person_generation="allow_adult" if shot["character_assets"] != "-" else "dont_allow",
        negative_prompt=build_negative(shot),
        enhance_prompt=False,
    )
    if vertex:
        cfg["seed"] = shot["seed"]          # honoured on Vertex only
        cfg["generate_audio"] = True
    if prior_frame is None:
        refs = reference_images(shot, types_)
        if refs:
            cfg["reference_images"] = refs
        source = types_.GenerateVideosSource(prompt=build_prompt(shot))
    else:
        source = types_.GenerateVideosSource(
            prompt=build_prompt(shot) + " Continue this exact shot from the given frame.",
            image=types_.Image(image_bytes=prior_frame, mime_type="image/png"))
    return source, types_.GenerateVideosConfig(**cfg)

def req_hash(shot, model):
    return hashlib.sha1(json.dumps([shot["shot_id"], model, build_prompt(shot),
                                    build_negative(shot), shot["duration_s"]]).encode()).hexdigest()[:12]

# --------------------------------------------------------------------- plan
def cmd_plan(a):
    shots = load_shots()
    rate = RATES.get(a.model, 0.40)
    total_gen = total_pic = 0; long_shots = 0; refs = 0
    for s in shots:
        pcs = pieces_for(s["duration_s"]); total_gen += sum(pcs); total_pic += s["duration_s"]
        long_shots += len(pcs) > 1; refs += bool(PLATES.get(s["subjects"]))
    print(f"model                 {a.model}   (${rate:.2f}/s, audio included, list price)")
    print(f"shots                 {len(shots)}")
    print(f"picture seconds       {total_pic:.0f}s  ({total_pic/60:.1f} min in the cut)")
    print(f"generated seconds     {total_gen}s  (rounded to 4/6/8s pieces; {long_shots} shots chained)")
    print(f"shots with face lock  {refs}  (reference plates attached)")
    print(f"estimated cost        ${total_gen*rate:,.0f}   ->  ${total_gen*0.40:,.0f} on Veo 3.1 standard")
    print(f"wall clock            ~{total_gen/8*90/a.parallel/60:.0f} min at {a.parallel} parallel ops "
          f"(~90s per 8s clip, sequential pieces for chained shots)")
    print()
    print("expect to REGENERATE 20-40% of shots on first pass (face drift, captions, motion).")
    print("budget for it: a realistic first-cut cost is 1.3x the figure above.")

# ------------------------------------------------------------------ dry-run
def client_and_types(need_key=True):
    from google import genai
    from google.genai import types as types_
    vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "").lower() == "true"
    if not need_key:
        return None, types_, vertex
    if vertex:
        c = genai.Client(vertexai=True, project=os.environ["GOOGLE_CLOUD_PROJECT"],
                         location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"))
    else:
        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key:
            sys.exit("no GEMINI_API_KEY in the environment - nothing to render with. "
                     "Run `plan` or `dry-run` instead; they need no key.")
        c = genai.Client(api_key=key)
    return c, types_, vertex

def cmd_dry_run(a):
    _, types_, vertex = client_and_types(need_key=False)
    shots = load_shots(); built = 0; with_refs = 0; chained = 0
    for s in shots:
        pcs = pieces_for(s["duration_s"])
        src, cfg = request_for(s, pcs[0], types_, vertex, a.model)
        built += 1; with_refs += bool(cfg.reference_images)
        if len(pcs) > 1:
            request_for(s, pcs[1], types_, vertex, a.model, prior_frame=b"\x89PNG"); chained += 1
    print(f"built {built} first-piece requests through google-genai types "
          f"({with_refs} with reference plates, {chained} chained) - no network used")
    print(f"mode: {'Vertex AI (seed + audio flags on)' if vertex else 'Gemini Developer API (seed unavailable; audio is default)'}")
    ex = next(s for s in shots if s["subjects"] == "D")
    src, cfg = request_for(ex, 8, types_, vertex, a.model)
    print(f"\nexample {ex['shot_id']} ({ex['subjects']}):")
    print(" prompt:", src.prompt[:400] + "...")
    print(" config:", {k: v for k, v in cfg.model_dump(exclude_none=True).items() if k != "reference_images"},
          f"+ {len(cfg.reference_images or [])} reference image(s)")

def cmd_models(a):
    c, _, _ = client_and_types()
    seen = [m.name for m in c.models.list() if "veo" in (m.name or "").lower()]
    print("\n".join(seen) if seen else "no Veo models visible to this key")

# ------------------------------------------------------------------- render
_lock = threading.Lock()
def load_manifest():
    return json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {"shots": {}}
def save_manifest(m):
    with _lock:
        json.dump(m, open(MANIFEST, "w"), indent=1)

def last_frame_png(mp4):
    import subprocess
    ff = os.environ.get("FFMPEG", "ffmpeg")
    out = mp4 + ".last.png"
    subprocess.run([ff, "-y", "-loglevel", "error", "-sseof", "-0.05", "-i", mp4,
                    "-frames:v", "1", out], check=True)
    return open(out, "rb").read()

def concat(pieces, out):
    import subprocess
    ff = os.environ.get("FFMPEG", "ffmpeg")
    lst = out + ".txt"
    open(lst, "w").write("".join(f"file '{p}'\n" for p in pieces))
    subprocess.run([ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", out], check=True)

def render_one(shot, c, types_, vertex, model, log):
    """Generate every piece of one shot, chain them, return (path, seconds, notes)."""
    pcs = pieces_for(shot["duration_s"]); files = []; prior = None; notes = []
    for i, plen in enumerate(pcs):
        src, cfg = request_for(shot, plen, types_, vertex, model, prior_frame=prior)
        op = c.models.generate_videos(model=model, source=src, config=cfg)
        t0 = time.time()
        while not op.done:
            time.sleep(10); op = c.operations.get(op)
            if time.time() - t0 > 900:
                raise TimeoutError(f"{shot['shot_id']} piece {i}: operation exceeded 15 min")
        resp = op.response or op.result
        if not resp or not resp.generated_videos:
            reason = (resp.rai_media_filtered_reasons if resp else None) or ["no video returned"]
            raise RuntimeError(f"{shot['shot_id']} piece {i}: filtered/empty - {reason}")
        vid = resp.generated_videos[0].video
        path = os.path.join(RENDERS, f"{shot['shot_id']}_p{i}.mp4")
        if vid.video_bytes:
            open(path, "wb").write(vid.video_bytes)
        else:
            c.files.download(file=vid, destination=path)
        files.append(path); log(f"  {shot['shot_id']} piece {i+1}/{len(pcs)} ({plen}s) in {time.time()-t0:.0f}s")
        if i + 1 < len(pcs):
            prior = last_frame_png(path)
    final = os.path.join(RENDERS, f"{shot['shot_id']}.mp4")
    if len(files) == 1:
        os.replace(files[0], final)
    else:
        concat(files, final); notes.append(f"chained {len(files)} pieces")
    return final, sum(pcs), notes

def cmd_render(a, only=None):
    c, types_, vertex = client_and_types()
    os.makedirs(RENDERS, exist_ok=True)
    shots = load_shots()
    if only:
        shots = [s for s in shots if s["shot_id"] == only]
    else:
        ids = [s["shot_id"] for s in shots]
        lo = ids.index(a.frm) if a.frm else 0; hi = ids.index(a.to) + 1 if a.to else len(shots)
        shots = shots[lo:hi]
    man = load_manifest(); rate = RATES.get(a.model, 0.40); todo = []
    for s in shots:
        h = req_hash(s, a.model); rec = man["shots"].get(s["shot_id"])
        if rec and rec.get("hash") == h and os.path.exists(rec.get("path", "")) and not a.force:
            continue
        todo.append(s)
    gen = sum(sum(pieces_for(s["duration_s"])) for s in todo)
    print(f"{len(todo)} shots to render ({len(shots)-len(todo)} already done), "
          f"{gen}s of generation, ~${gen*rate:,.0f} at {a.model}")
    if not todo:
        return
    if not a.yes:
        if input("proceed? [y/N] ").strip().lower() != "y":
            sys.exit("aborted")
    log = lambda m: print(m, flush=True)
    def work(s):
        try:
            path, secs, notes = render_one(s, c, types_, vertex, a.model, log)
            man["shots"][s["shot_id"]] = {"hash": req_hash(s, a.model), "path": path, "model": a.model,
                                          "generated_s": secs, "cost_usd": round(secs*rate, 2),
                                          "notes": notes, "status": "rendered"}
        except Exception as e:
            man["shots"][s["shot_id"]] = {"hash": req_hash(s, a.model), "model": a.model,
                                          "status": "failed", "error": str(e)[:400]}
            log(f"  {s['shot_id']} FAILED: {e}")
        save_manifest(man)
    with cf.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        list(ex.map(work, todo))
    done = [v for v in man["shots"].values() if v["status"] == "rendered"]
    failed = [k for k, v in man["shots"].items() if v["status"] == "failed"]
    print(f"\nrendered {len(done)}  failed {len(failed)}  spent ~${sum(v['cost_usd'] for v in done):,.0f}")
    if failed:
        print("failed:", ", ".join(failed))
    print("next: python3 tools/conform.py --source renders")

def cmd_smoke(a):
    a.yes = True; a.force = True; a.frm = a.to = None
    print(f"smoke test: rendering {a.shot} only (one paid call)")
    cmd_render(a, only=a.shot)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["plan", "dry-run", "models", "smoke", "render"])
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--shot", default="SH0126")
    ap.add_argument("--from", dest="frm"); ap.add_argument("--to")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--force", action="store_true"); ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    {"plan": cmd_plan, "dry-run": cmd_dry_run, "models": cmd_models,
     "smoke": cmd_smoke, "render": cmd_render}[a.cmd](a)
