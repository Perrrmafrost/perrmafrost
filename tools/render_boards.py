# -*- coding: utf-8 -*-
"""
Renders every shot's previs board to a 1920x960 PNG using the same drawing code
the workspace player uses, via headless Chromium. Boards stand in for any shot
that has no Veo clip yet, so the conform can run end-to-end today.

    python3 tools/render_boards.py            # -> boards/SHxxxx.png
"""
import os, re, subprocess, json, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from platform_tools import find_ffmpeg, find_browser
import pathlib
CHROME, FF = find_browser(), find_ffmpeg()
W, H, PER = 1920, 960, 16
OUT = P("boards"); os.makedirs(OUT, exist_ok=True)

tpl = open(P("workspace", "index.html")).read()
style = re.search(r"<style>([\s\S]*?)</style>", tpl).group(1)
blocks = re.findall(r"<script>([\s\S]*?)</script>", tpl)
data_js, renderer_js = blocks[0], blocks[1]       # dataset+script text, then the frame renderer
shots = json.load(open(P("production", "04-previs", "animatic.json")))["shots"]

harness = f"""<!doctype html><meta charset="utf-8"><style>{style}
body{{margin:0;background:#000}} .stage{{width:{W}px;height:{H}px;border:0;border-radius:0;aspect-ratio:auto}}
.ovl .bot{{display:none}} .ovl .top{{font-size:18px}} .cdw{{font-size:30px;right:28px;bottom:24px}}
.slate .t1{{font-size:44px}} .slate .t2{{font-size:20px}}</style>
<div id="root"></div>
<script>{data_js}</script><script>{renderer_js}</script>
<script>
const q=new URLSearchParams(location.search); const b=+q.get('batch')||0;
const root=document.getElementById('root');
SH.slice(b*{PER},(b+1)*{PER}).forEach(s=>{{const d=document.createElement('div');d.className='stage';root.appendChild(d);paintStage(d,s,s.t);}});
</script>"""
hp = P("boards", "_harness.html"); open(hp, "w").write(harness)

n_batches = (len(shots) + PER - 1) // PER
for b in range(n_batches):
    chunk = shots[b*PER:(b+1)*PER]
    sheet = P("boards", f"_sheet{b:02d}.png")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={W},{H*len(chunk)}",
                    "--virtual-time-budget=2500", f"--screenshot={sheet}",
                    pathlib.Path(hp).as_uri() + f"?batch={b}"], check=True, capture_output=True)
    for i, s in enumerate(chunk):
        subprocess.run([FF, "-y", "-loglevel", "error", "-i", sheet,
                        "-vf", f"crop={W}:{H}:0:{i*H}", P("boards", f"{s['id']}.png")], check=True)
    os.remove(sheet)
    print(f"batch {b+1}/{n_batches}  {chunk[0]['id']}..{chunk[-1]['id']}", flush=True)
os.remove(hp)
print(f"{len(shots)} boards -> boards/")
