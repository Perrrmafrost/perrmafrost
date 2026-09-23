#!/usr/bin/env python3
"""Upscale approved takes to 1920x1080 @ 24 fps and join them in shot order with ffmpeg.

  python assemble_film.py ../../shots/seq_01_shots.jsonl [more .jsonl ...] --out HERE_AM_I_seq01.mp4

Approval: set  "approved": <take number>  for a shot in renders/status.json (default = the latest take).
Shots with no render get a black slate of the right length, so timing stays correct while you work.
Needs ffmpeg on PATH. Uses the take's 1080p version from upscale_takes.py when there is one; otherwise Lanczos.
"""
import json, sys, argparse, pathlib, subprocess, tempfile, shutil

HERE = pathlib.Path(__file__).parent
# Fill the 16:9 frame (crop a few pixels rather than add bars), conform to 24 fps
VF = "scale=1920:1080:flags=lanczos:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=24,format=yuv420p"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="+")
    ap.add_argument("--out", default="HERE_AM_I_cut.mp4")
    cfg_path = HERE / "config.json"
    cfg = json.loads(cfg_path.read_text()) if cfg_path.exists() else {}
    ap.add_argument("--renders", default=str(HERE / cfg.get("output_dir", "renders")))
    a = ap.parse_args()
    renders = pathlib.Path(a.renders)
    status = json.loads((renders / "status.json").read_text()) if (renders / "status.json").exists() else {}
    renders.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix="_assemble_", dir=renders))
    parts = []
    for path in a.jsonl:
        for line in open(path, encoding="utf-8"):
            if not line.strip():
                continue
            shot = json.loads(line); sid, dur = shot["id"], float(shot["duration_s"])
            takes = status.get(sid, {}).get("takes", [])
            pick = status.get(sid, {}).get("approved") or (takes[-1]["take"] if takes else None)
            files = next((t["files"] for t in takes if t["take"] == pick), [])
            src = status.get(sid, {}).get("upscaled", {}).get(str(pick)) or \
                next((f for f in files if f.lower().endswith((".mp4", ".webm", ".mov", ".webp", ".gif"))), None)
            dst = work / f"{sid}.mp4"
            if src:
                # a clip shorter than its shot (e.g. Wan's 5 s cap on a 7 s shot) holds its last frame, keeping the cut in sync
                cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-t", f"{dur}",
                       "-vf", f"tpad=stop_mode=clone:stop_duration={dur},{VF}", "-an",
                       "-c:v", "libx264", "-crf", "16", "-preset", "slow", str(dst)]
            else:
                cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=black:s=1920x1080:r=24:d={dur}",
                       "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", str(dst)]
            subprocess.run(cmd, check=True)
            parts.append(dst)
            print(("ok     " if src else "slate  ") + sid)
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", a.out], check=True)
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {a.out} ({len(parts)} shots)")

if __name__ == "__main__":
    main()
