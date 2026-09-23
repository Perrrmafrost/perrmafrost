#!/usr/bin/env python3
"""Render HERE AM I shots through a local ComfyUI, one clip per shot, resumable.

1. workflow_api.json (Wan 2.2 image-to-video) and config.json (its node IDs) ship with this kit. To use
   another workflow: in ComfyUI  Workflow > Export (API), save it here and set the node IDs in config.json.
2. Make the first frames: compose_first_frames.py (EXTEND children start from the parent's last frame).
3. Run:  python render_queue.py ../../shots/seq_01_shots.jsonl  [--takes 2] [--only 01.02.003,01.02.004]

Outputs go to renders/<shot id>/take_N.<ext>; progress is logged in renders/status.json so a crash
or reboot just resumes. Nothing leaves your machine: it talks only to ComfyUI on 127.0.0.1.
"""
import json, time, random, argparse, pathlib, subprocess, urllib.parse
from comfy_client import http, upload_image, set_input

HERE = pathlib.Path(__file__).parent

def start_frame(shot, stills, status, out_root):
    """The composed first frame (compose_first_frames.py), or for an EXTEND child the parent take's last frame."""
    own = stills / f"{shot['id']}.png"
    if own.exists():
        return own, None
    parent = next((f.split(":", 1)[1] for f in shot.get("flags", []) if f.startswith("EXTEND:")), None)
    if parent:
        takes = status.get(parent, {}).get("takes", [])
        pick = status.get(parent, {}).get("approved") or (takes[-1]["take"] if takes else None)
        files = next((t["files"] for t in takes if t["take"] == pick), [])
        src = next((f for f in files if f.lower().endswith((".mp4", ".webm", ".mov"))), None)
        if not src:
            return None, f"EXTEND of {parent}, which has no rendered take yet"
        dst = out_root / "_chain" / f"{shot['id']}_from_{parent}_t{pick}.png"
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-1", "-i", src, "-update", "1",
                            "-frames:v", "1", str(dst)], check=True)
        return dst, None
    return None, f"no first frame: run compose_first_frames.py for {shot['id']} and approve one"

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
            # image-to-video gets the derived motion prompt (05 §5.5); text-to-video gets the master prompt
            i2v = bool(n.get("start_image"))
            set_input(wf, n["positive"], shot.get("motion_prompt") if i2v and shot.get("motion_prompt") else shot["prompt"])
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
                img, why = start_frame(shot, stills, status, out_root)
                if img is None:
                    print(f"{sid}: {why} - skipping")
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
