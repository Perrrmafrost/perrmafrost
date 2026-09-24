#!/usr/bin/env python3
"""Scan this computer for the HERE AM I local-render pipeline and print a report to paste back.

Run:  python scan_setup.py            (optionally: python scan_setup.py "D:\\ComfyUI")
Reads only; changes nothing; sends nothing anywhere.
"""
import os, sys, shutil, platform, subprocess, json, pathlib, urllib.request

def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception as e:
        return f"(unavailable: {e.__class__.__name__})"

report = {"os": f"{platform.system()} {platform.release()} ({platform.machine()})",
          "python": sys.version.split()[0]}

# GPU / VRAM / driver
report["gpu"] = run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"])
# System RAM and free disk
try:
    import psutil  # optional
    report["ram_gb"] = round(psutil.virtual_memory().total / 2**30, 1)
except ImportError:
    report["ram_gb"] = "(install psutil for RAM)"
report["ffmpeg"] = shutil.which("ffmpeg") or "NOT FOUND"

# Find ComfyUI
candidates = [pathlib.Path(p) for p in sys.argv[1:]]
home = pathlib.Path.home()
for base in [home, home / "Documents", home / "Desktop", pathlib.Path("C:/"), pathlib.Path("D:/"), pathlib.Path("E:/")]:
    if base.exists():
        for name in ("ComfyUI", "ComfyUI_windows_portable/ComfyUI", "comfyui", "ComfyUI_windows_portable"):
            p = base / name
            if (p / "models").is_dir() or (p / "ComfyUI" / "models").is_dir():
                candidates.append(p / "ComfyUI" if (p / "ComfyUI" / "models").is_dir() else p)
seen, comfy = set(), []
for c in candidates:
    c = c.resolve() if c.exists() else c
    if c not in seen and (c / "models").is_dir():
        seen.add(c); comfy.append(c)
report["comfyui_dirs"] = [str(c) for c in comfy]

# Models and custom nodes
for c in comfy:
    models = {}
    for sub in sorted((c / "models").iterdir()):
        if sub.is_dir():
            files = [f"{f.name} ({f.stat().st_size/2**30:.1f} GB)" for f in sub.rglob("*")
                     if f.is_file() and f.suffix.lower() in (".safetensors", ".gguf", ".ckpt", ".pt", ".pth", ".bin", ".sft")]
            if files:
                models[sub.name] = files
    report[f"models @ {c}"] = models
    cn = c / "custom_nodes"
    report[f"custom_nodes @ {c}"] = sorted(p.name for p in cn.iterdir() if p.is_dir()) if cn.is_dir() else []
    report[f"disk_free_gb @ {c}"] = round(shutil.disk_usage(c).free / 2**30, 1)

# Is ComfyUI running?
try:
    with urllib.request.urlopen("http://127.0.0.1:8188/system_stats", timeout=3) as r:
        report["comfyui_running"] = json.loads(r.read())
except Exception:
    report["comfyui_running"] = "not reachable on 127.0.0.1:8188 (start ComfyUI to include this)"

print(json.dumps(report, indent=2))
