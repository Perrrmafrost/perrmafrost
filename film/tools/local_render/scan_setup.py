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

RENDER_BUDGET_GB, MODEL_BUDGET_GB = 300, 80   # renders + ComfyUI output copies; video/image/upscale weights (~70 GB)

def list_drives():
    """Every mounted drive with its free space. Windows: all drive letters; Linux: real block devices."""
    drives = []
    if os.name == "nt":
        import ctypes, string
        kinds = {2: "removable", 3: "fixed", 4: "network", 5: "cd-rom", 6: "ramdisk"}
        mask = ctypes.windll.kernel32.GetLogicalDrives()
        roots = [(f"{L}:\\", kinds.get(ctypes.windll.kernel32.GetDriveTypeW(f"{L}:\\"), "other"))
                 for i, L in enumerate(string.ascii_uppercase) if mask >> i & 1]
    else:
        roots, seen = [], set()
        try:
            mounts = [l.split()[:2] for l in open("/proc/mounts")]
        except OSError:
            mounts = [["/dev/root", "/"]]
        for dev, mnt in mounts:
            mnt = mnt.replace("\\040", " ")
            if dev.startswith("/dev/") and not dev.startswith("/dev/loop"):
                try:
                    st = os.stat(mnt).st_dev
                except OSError:
                    continue
                if st not in seen:
                    seen.add(st); roots.append((mnt, "fixed"))
    for root, kind in roots:
        try:
            u = shutil.disk_usage(root)
        except OSError:
            continue  # empty card reader, disconnected network drive
        if u.total < 2**30:
            continue  # tiny system/virtual mounts
        drives.append({"root": root, "type": kind, "free_gb": round(u.free / 2**30, 1), "total_gb": round(u.total / 2**30, 1)})
    return drives

report = {"os": f"{platform.system()} {platform.release()} ({platform.machine()})",
          "python": sys.version.split()[0]}

# GPU / VRAM / driver
report["gpu"] = run(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"])
# System RAM
try:
    import psutil  # optional
    report["ram_gb"] = round(psutil.virtual_memory().total / 2**30, 1)
except ImportError:
    report["ram_gb"] = "(install psutil for RAM)"
report["ffmpeg"] = shutil.which("ffmpeg") or "NOT FOUND"

# Find ComfyUI
# Free space on every drive; renders and models go on the fixed drive with the most room
home = pathlib.Path.home()
drives = list_drives()
local = [d for d in drives if d["type"] == "fixed"] or drives
best = max(local, key=lambda d: d["free_gb"]) if local else None
need = RENDER_BUDGET_GB + MODEL_BUDGET_GB
report["drives"] = drives
report["storage_suggestion"] = {
    "drive": best["root"] if best else "(none found)",
    "free_gb": best["free_gb"] if best else 0,
    "suggested_root": str((home if os.name != "nt" and os.stat(home).st_dev == os.stat(best["root"]).st_dev
                           else pathlib.Path(best["root"])) / "HERE_AM_I") if best else "",
    "enough": bool(best and best["free_gb"] >= need),
    "note": f"budget ~{RENDER_BUDGET_GB} GB renders + ~{MODEL_BUDGET_GB} GB models = {need} GB",
}

candidates = [pathlib.Path(p) for p in sys.argv[1:]]
for base in [home, home / "Documents", home / "Desktop"] + [pathlib.Path(d["root"]) for d in local]:
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
