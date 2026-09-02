# -*- coding: utf-8 -*-
"""
Offline test suite for tools/render.py. No network, no key: the SDK is patched at
its HTTP layer so google-genai's real request converters and response parsers
run against canned Veo responses, and ffmpeg runs for real on tiny clips.

    python3 tools/test_render.py

Covers the failure modes found in adversarial review: operation errors, RAI
filtering, URI downloads, chained pieces with dialogue split by time, resume
after a crash, resume of an in-flight operation, parallel manifest safety,
and the request-shape rules (plates, person_generation, pane-text negatives).
"""
import os, sys, json, base64, subprocess, tempfile, shutil, time, copy, random, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
os.environ["FFMPEG"] = FF; os.environ["GEMINI_API_KEY"] = "test-key"; os.environ.pop("GOOGLE_GENAI_USE_VERTEXAI", None)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import render
from google.genai import _api_client as ac

TMP = tempfile.mkdtemp(prefix="render-test-"); render.RENDERS = TMP; render.MANIFEST = os.path.join(TMP, "manifest.json")
CLIP = os.path.join(TMP, "clip8.mp4")
subprocess.run([FF, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc=size=320x180:rate=24", "-f", "lavfi",
                "-i", "sine=frequency=440", "-t", "8", "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", CLIP], check=True)
B64 = base64.b64encode(open(CLIP, "rb").read()).decode()

LOG, MODE, N = [], {"kind": "bytes", "pending": False, "jitter": 0.0}, {"ops": 0}
def op(name, done, resp=None, error=None):
    d = {"name": name, "done": done}
    if resp is not None: d["response"] = {"generateVideoResponse": resp}
    if error is not None: d["error"] = error
    return d
def sample():
    k = MODE["kind"]
    if k == "bytes": return {"generatedSamples": [{"video": {"encodedVideo": B64, "encoding": "video/mp4"}}]}
    if k == "uri": return {"generatedSamples": [{"video": {"uri": "https://generativelanguage.googleapis.com/v1beta/files/x:download?alt=media"}}]}
    if k == "filtered": return {"raiMediaFilteredCount": 1, "raiMediaFilteredReasons": ["policy: likeness"]}
def fake_request(self, method, path, body, http_options=None):
    LOG.append((method, path, copy.deepcopy(body)))
    if MODE["jitter"]: time.sleep(random.random() * MODE["jitter"])
    if method == "post" and path.endswith(":predictLongRunning"):
        N["ops"] += 1; name = f"models/m/operations/op{N['ops']}"
        if MODE["kind"] == "error":
            return ac.SdkHttpResponse(headers={}, body=json.dumps(op(name, True, error={"code": 400, "message": "invalid argument", "status": "INVALID_ARGUMENT"})))
        return ac.SdkHttpResponse(headers={}, body=json.dumps(op(name, not MODE["pending"], None if MODE["pending"] else sample())))
    if method == "get" and "/operations/" in path:
        return ac.SdkHttpResponse(headers={}, body=json.dumps(op(path, not MODE["pending"], None if MODE["pending"] else sample())))
    raise AssertionError(f"unexpected {method} {path}")
def fake_download(self, path, *, http_options=None, destination=None, chunk_size=1 << 20):
    LOG.append(("download", path, None))
    if destination is None: return open(CLIP, "rb").read()
    shutil.copy(CLIP, destination)
ac.BaseApiClient.request = fake_request; ac.BaseApiClient.download_file = fake_download
_sleep = time.sleep; time.sleep = lambda s: None

SHOTS = render.load_shots(); BY = {s["shot_id"]: s for s in SHOTS}
def args(**kw):
    a = argparse.Namespace(model=render.DEFAULT_MODEL, shot=None, frm=None, to=None, parallel=4,
                           force=False, yes=True, op_timeout=1800); a.__dict__.update(kw); return a
def man(): return json.load(open(render.MANIFEST))
def posts(): return [b for m, p, b in LOG if m == "post"]
def reset(): LOG.clear(); N["ops"] = 0; MODE.update(kind="bytes", pending=False, jitter=0.0)
def clean(): shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP); shutil.copy(CLIP, CLIP) if False else None
def frames(p):
    r = subprocess.run([FF, "-i", p, "-map", "0:v", "-f", "null", "-"], capture_output=True, text=True).stderr
    import re; return int(re.findall(r"frame=\s*(\d+)", r)[-1])

passed = failed = 0
def check(name, cond, detail=""):
    global passed, failed
    cond = bool(cond); passed += cond; failed += (not cond); print(f"{'PASS' if cond else 'FAIL'}  {name}  {detail}")

# ---- pure functions --------------------------------------------------------------
for d in range(3, 19):
    pcs = render.pieces_for(d)
    brute = min(sum(c) for n in range(1, 4) for c in __import__("itertools").product(render.DURATIONS, repeat=n) if sum(c) >= d)
    check(f"pieces_for({d})={pcs}", sum(pcs) >= d and all(x in render.DURATIONS for x in pcs) and sum(pcs) == brute)
single = next(s for s in SHOTS if s["subjects"] == "M" and any(x["character"] == "LAUREN" for x in s["dialogue"]))
p0 = render.build_prompt(single)
check("off-screen speaker is labelled off-screen", "Lauren, off-screen" in p0, single["shot_id"])
dnb = next(s for s in SHOTS if "DO NOT GO BACK" in s["prompt"] and s["device_in_frame"])
check("pane-text shot keeps text allowed on the pane", "not on the pane" in render.build_negative(dnb), dnb["shot_id"])
hand = next(s for s in SHOTS if s["character_assets"] == "-" and "thumb" in s["prompt"].lower())
check("insert with a hand allows people", render.needs_people(hand), hand["shot_id"])
title = next(s for s in SHOTS if s["framing"] == "TITLE")
check("title card does not allow people", not render.needs_people(title))
shout = next(s for s in SHOTS if any(x["line"].isupper() and len(x["line"]) > 12 for x in s["dialogue"]))
check("the shout is directed as a shout", "shouts" in render.build_prompt(shout), shout["shot_id"])
chained = next(s for s in SHOTS if len(render.pieces_for(s["duration_s"])) > 1 and len(s["dialogue"]) >= 2)
pcs = render.pieces_for(chained["duration_s"]); pr = [render.build_prompt(chained, pcs, i, with_refs=(i == 0)) for i in range(len(pcs))]
first_line = chained["dialogue"][0]["line"]
check("chained shot: first line only in one piece", sum(first_line in p for p in pr) == 1, chained["shot_id"])
check("continuation piece never claims reference images", all("supplied reference images" not in p for p in pr[1:]))
h1 = render.req_hash(chained, "m", False); chained2 = dict(chained, prompt=chained["prompt"] + " x")
check("req_hash changes when the prompt changes", render.req_hash(chained2, "m", False) != h1)
check("req_hash is stable otherwise", render.req_hash(chained, "m", False) == h1)

# ---- executed scenarios ----------------------------------------------------------
two = next(s for s in SHOTS if s["subjects"] == "MB" and s["dialogue"] and len(render.pieces_for(s["duration_s"])) == 1)
reset(); render.cmd_render(args(), only={two["shot_id"]})
b = posts()[0]
check("two-shot: three plates on the wire", len(b["instances"][0].get("referenceImages", [])) == 3)
check("two-shot: person_generation allow_adult", b["parameters"]["personGeneration"] == "allow_adult")
check("two-shot: rendered + manifest", man()["shots"][two["shot_id"]]["status"] == "rendered" and os.path.exists(os.path.join(TMP, two["shot_id"] + ".mp4")))

reset(); render.cmd_render(args(), only={chained["shot_id"]})
out = os.path.join(TMP, chained["shot_id"] + ".mp4")
check("chained: one POST per piece", len(posts()) == len(pcs), f"{len(posts())} posts for {pcs}")
check("chained: second piece is image-to-video, no plates", "image" in posts()[1]["instances"][0] and "referenceImages" not in posts()[1]["instances"][0])
check("chained: concatenated output length", abs(frames(out) - 24 * 8 * len(pcs)) <= 2, f"{frames(out)} frames")
check("chained: manifest notes it", "chained" in " ".join(man()["shots"][chained["shot_id"]]["notes"]))

reset(); render.cmd_render(args(), only={two["shot_id"], chained["shot_id"]})
check("resume: already-rendered shots make no paid calls", len(posts()) == 0)

reset(); MODE["kind"] = "error"; render.cmd_render(args(force=True), only={two["shot_id"]})
e = man()["shots"][two["shot_id"]]
check("operation error is surfaced with the server's message", e["status"] == "failed" and "invalid argument" in e["error"], e["error"][:80])

reset(); MODE["kind"] = "filtered"; render.cmd_render(args(force=True), only={two["shot_id"]})
check("RAI filter reason is recorded", "likeness" in man()["shots"][two["shot_id"]]["error"])

reset(); MODE["kind"] = "uri"; render.cmd_render(args(force=True), only={two["shot_id"]})
check("URI response is downloaded", any(m == "download" for m, _, _ in LOG) and man()["shots"][two["shot_id"]]["status"] == "rendered")

reset(); MODE["pending"] = True; render.cmd_render(args(force=True, op_timeout=1), only={two["shot_id"]})
r = man()["shots"][two["shot_id"]]
check("timeout leaves the paid op in flight, not failed", r["status"] == "in_flight" and r["op"], r.get("op"))
n_posts = len(posts()); reset(); MODE["pending"] = False; render.cmd_render(args(), only={two["shot_id"]})
check("in-flight op is resumed, not re-submitted", len(posts()) == 0 and man()["shots"][two["shot_id"]]["status"] == "rendered")

reset(); MODE["jitter"] = 0.004; batch = {s["shot_id"] for s in SHOTS[10:58]}
try:
    render.cmd_render(args(parallel=8, force=True), only=batch); crashed = None
except Exception as ex:
    crashed = repr(ex)
m = man()
check("parallel run completes without a manifest race", crashed is None and sum(1 for k in batch if m["shots"][k]["status"] == "rendered") == len(batch), crashed or f"{len(batch)} rendered")
check("manifest is valid JSON after parallel writes", isinstance(m, dict))

time.sleep = _sleep; shutil.rmtree(TMP, ignore_errors=True)
print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
