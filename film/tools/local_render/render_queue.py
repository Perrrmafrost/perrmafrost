#!/usr/bin/env python3
"""Render HERE AM I shots through a local ComfyUI, one clip per shot, resumable.

1. In ComfyUI, build/load a text-to-video or image-to-video workflow that works on your GPU,
   then  Workflow > Export (API)  and save it as  workflow_api.json  next to this script.
2. Copy config.example.json to config.json and set the node IDs (open workflow_api.json to find them).
3. Run:  python render_queue.py ../../shots/seq_01_shots.jsonl  [--takes 2] [--only 01.02.003,01.02.004]

Outputs go to renders/<shot id>/take_N.<ext>; progress is logged in renders/status.json so a crash
or reboot just resumes. Nothing leaves your machine: it talks only to ComfyUI on 127.0.0.1.
"""
import json, sys, time, uuid, random, argparse, pathlib, urllib.request, urllib.parse, mimetypes

HERE = pathlib.Path(__file__).parent

def http(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def upload_image(base, path):
    boundary = uuid.uuid4().hex
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{path.name}\"\r\n"
            f"Content-Type: {mimetypes.guess_type(path.name)[0] or 'image/png'}\r\n\r\n").encode() + path.read_bytes() + \
           f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--{boundary}--\r\n".encode()
    res = json.loads(http(f"{base}/upload/image", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"}))
    return res["name"]

def set_input(wf, spec, value):
    node, key = spec.split(".", 1)
    wf[node]["inputs"][key] = value

def frames_for(seconds, cfg):
    n = max(1, round(seconds * cfg["model_fps"]))
    rule = cfg.get("frame_rule", "any")          # Wan-style models want 4n+1 frames
    if rule == "4n+1":
        n = 4 * max(1, round((n - 1) / 4)) + 1
    return min(n, cfg.get("max_frames", 10**6))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("shots_jsonl")
    ap.add_argument("--config", default=str(HERE / "config.json"))
    ap.add_argument("--takes", type=int, default=1)
    ap.add_argument("--only", default="")
    a = ap.parse_args()

    cfg = json.loads(pathlib.Path(a.config).read_text())
    base = cfg.get("comfy_url", "http://127.0.0.1:8188")
    template = json.loads((HERE / cfg["workflow_file"]).read_text())
    out_root = HERE / cfg.get("output_dir", "renders"); out_root.mkdir(parents=True, exist_ok=True)
    status_path = out_root / "status.json"
    status = json.loads(status_path.read_text()) if status_path.exists() else {}
    stills = HERE / cfg.get("stills_dir", "stills")
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    n = cfg["nodes"]

    shots = [json.loads(l) for l in open(a.shots_jsonl, encoding="utf-8") if l.strip()]
    for shot in shots:
        sid = shot["id"]
        if only and sid not in only:
            continue
        done = status.get(sid, {}).get("takes", [])
        for take in range(len(done) + 1, a.takes + 1):
            wf = json.loads(json.dumps(template))
            set_input(wf, n["positive"], shot["prompt"])
            if n.get("negative"):
                set_input(wf, n["negative"], shot["negative"])
            seed = random.randint(0, 2**31 - 1)
            for spec in n.get("seed", "").split(",") if n.get("seed") else []:
                set_input(wf, spec.strip(), seed)
            if n.get("width"):  set_input(wf, n["width"], cfg["render_width"])
            if n.get("height"): set_input(wf, n["height"], cfg["render_height"])
            if n.get("length"): set_input(wf, n["length"], frames_for(shot["duration_s"], cfg))
            if n.get("filename_prefix"): set_input(wf, n["filename_prefix"], f"HEREAMI/{sid}_t{take}")
            if n.get("start_image"):
                # image-to-video: first matching composed first frame or reference still, if you made one
                cands = [stills / f"{sid}.png"] + [stills / f"{r}.png" for r in shot.get("refs", [])]
                img = next((c for c in cands if c.exists()), None)
                if img is None:
                    print(f"{sid}: no start image found (looked for {cands[0].name} and refs) - skipping")
                    break
                set_input(wf, n["start_image"], upload_image(base, img))
            pid = json.loads(http(f"{base}/prompt", json.dumps({"prompt": wf, "client_id": "hereami"}).encode(),
                                  {"Content-Type": "application/json"}))["prompt_id"]
            print(f"{sid} take {take}: queued ({shot['duration_s']} s, {frames_for(shot['duration_s'], cfg)} frames)", flush=True)
            t0 = time.time()
            while True:
                time.sleep(5)
                hist = json.loads(http(f"{base}/history/{pid}"))
                if pid in hist and hist[pid].get("outputs"):
                    break
                if pid in hist and hist[pid].get("status", {}).get("status_str") == "error":
                    print(f"{sid}: ComfyUI error, see its console"); break
            saved = []
            for node_out in hist.get(pid, {}).get("outputs", {}).values():
                for items in node_out.values():
                    for it in items if isinstance(items, list) else []:
                        if isinstance(it, dict) and "filename" in it:
                            q = urllib.parse.urlencode({k: it.get(k, "") for k in ("filename", "subfolder", "type")})
                            dst = out_root / sid / f"take_{take}{pathlib.Path(it['filename']).suffix}"
                            dst.parent.mkdir(parents=True, exist_ok=True)
                            dst.write_bytes(http(f"{base}/view?{q}")); saved.append(str(dst))
            status.setdefault(sid, {"takes": [], "approved": None})["takes"].append(
                {"take": take, "seed": seed, "files": saved, "seconds": round(time.time() - t0)})
            status_path.write_text(json.dumps(status, indent=1))
            print(f"{sid} take {take}: done in {round(time.time()-t0)} s -> {saved}", flush=True)

if __name__ == "__main__":
    main()
