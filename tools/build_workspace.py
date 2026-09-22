# -*- coding: utf-8 -*-
"""Assembles workspace/index.html from the template, the generated dataset and
the screenplay. Run after tools/build.py."""
import json, os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

tpl  = open(P("workspace", "_template.html")).read()
data = open(P("workspace", "data.js")).read()
fount = open(P("production", "03-script", "S01E01-the-package.fountain")).read()

# fountain -> display HTML: scene headings, character cues and act headers bold
body = fount.split("====", 1)[1]
out = []
for line in body.split("\n"):
    s = line.rstrip()
    e = html.escape(s)
    st = s.strip()
    if st.startswith("#"):
        out.append(f'<b style="display:block;margin:26px 0 6px;letter-spacing:.14em">{html.escape(st.lstrip("# "))}</b>')
    elif st == "====":
        out.append('<span style="color:var(--line)">— — —</span>')
    elif st and st == st.upper() and not st.startswith("**") and len(st) < 70 and re.search(r"[A-Z]", st):
        out.append(f"<b>{e}</b>")
    else:
        out.append(e)
script_html = "\n".join(out)

payload = data + "\nconst SCRIPT_HTML = " + json.dumps(script_html) + ";\n"
open(P("workspace", "index.html"), "w").write(tpl.replace("__DATA__", payload))

n = os.path.getsize(P("workspace", "index.html"))
print(f"workspace/index.html  {n/1024:.0f} KB  ({n/1048576:.2f} MB of the 16 MB cap)")
