# -*- coding: utf-8 -*-
"""Finds ffmpeg and a headless-capable browser on Linux, macOS or Windows."""
import os, shutil, sys, glob

def find_ffmpeg():
    p = os.environ.get("FFMPEG") or shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg not found. Install it (winget install Gyan.FFmpeg) "
                 "or run: pip install imageio-ffmpeg")

def find_browser():
    """Chrome, Chromium or Edge - any of them can screenshot headless."""
    cands = [os.environ.get("CHROME")]
    cands += [shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome", "chrome", "msedge")]
    cands += glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
    for base in (os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)"), os.environ.get("LOCALAPPDATA")):
        if base:
            cands += [os.path.join(base, "Google", "Chrome", "Application", "chrome.exe"),
                      os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe")]
    cands += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    for c in cands:
        if c and os.path.exists(c):
            return c
    sys.exit("no Chrome, Chromium or Edge found; set CHROME=<path to browser>")

def ffconcat_line(path):
    """ffmpeg concat lists want forward slashes and escaped single quotes."""
    p = os.path.abspath(path).replace("\\", "/").replace("'", "'\\''")
    return f"file '{p}'\n"
