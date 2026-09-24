#!/usr/bin/env python3
"""Upscale the chosen take of each shot to 1080p through ComfyUI's RTX Video Super Resolution node.

  python upscale_takes.py ../../shots/seq_01_shots.jsonl [--only 01.01.001,...] [--redo]

Only the approved take (status.json "approved", else the latest) is upscaled, so rejected takes cost
nothing. Output: renders/<id>/take_N_1080.mp4, recorded under "upscaled" in status.json;
assemble_film.py uses it when present and falls back to Lanczos scaling otherwise.
"""
import json, argparse, pathlib
import comfy_client as cc

HERE = pathlib.Path(__file__).parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="+")
    ap.add_argument("--config")
    ap.add_argument("--only", default="")
    ap.add_argument("--redo", action="store_true")
    a = ap.parse_args()
    cfg = cc.load_config(a.config)
    base = cfg.get("comfy_url", "http://127.0.0.1:8188")
    out_root = HERE / cfg.get("output_dir", "renders")
    status_path = out_root / "status.json"
    status = json.loads(status_path.read_text()) if status_path.exists() else {}
    template = json.loads((HERE / cfg.get("upscale_workflow", "workflow_upscale_api.json")).read_text())
    un = cfg["upscale_nodes"]
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    for path in a.jsonl:
        for line in open(path, encoding="utf-8"):
            if not line.strip():
                continue
            sid = json.loads(line)["id"]
            if only and sid not in only:
                continue
            rec = status.get(sid, {})
            takes = rec.get("takes", [])
            pick = rec.get("approved") or (takes[-1]["take"] if takes else None)
            src = next((f for t in takes if t["take"] == pick for f in t["files"] if f.lower().endswith(".mp4")), None)
            if not src:
                continue
            dst = pathlib.Path(src).with_name(f"take_{pick}_1080.mp4")
            if dst.exists() and not a.redo:
                continue
            wf = json.loads(json.dumps(template))
            cc.set_input(wf, un["video"], str(pathlib.Path(src).resolve()))
            cc.set_input(wf, un["filename_prefix"], f"HEREAMI_1080/{sid}_t{pick}")
            cc.download(base, next(f for f in cc.run(base, wf) if f["filename"].endswith(".mp4")), dst)
            rec.setdefault("upscaled", {})[str(pick)] = str(dst)
            status_path.write_text(json.dumps(status, indent=1))
            print(f"{sid} take {pick}: {dst.name}", flush=True)


if __name__ == "__main__":
    main()
