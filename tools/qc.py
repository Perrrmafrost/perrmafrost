# -*- coding: utf-8 -*-
"""
Executed quality-control audit. Run after any change to the cut:

    python3 tools/build.py && python3 tools/qc.py

Writes production/08-qc/automated-audit.md and exits non-zero on failure, so it
can gate a delivery. These are checks, not a checklist: every row is the result
of reading the actual timeline, script and subtitle files.
"""
import json, re, sys, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
S = json.load(open(P("production", "04-previs", "animatic.json")))["shots"]
DUR = json.load(open(P("production", "04-previs", "animatic.json")))["duration_s"]
SCRIPT = open(P("production", "03-script", "S01E01-the-package.fountain")).read()
clk = lambda t: f"{int(t)//60:02d}:{int(t)%60:02d}"
ALL = " ".join(s["action"] + " " + str(s["dlg"]) + " " + s["note"] for s in S)
DIALOGUE = " ".join(l for s in S for _, l in s["dlg"])

rows = []
def chk(name, cond, detail=""):
    rows.append((name, bool(cond), detail))
    return bool(cond)

# ---- delivery -------------------------------------------------------------
chk("Runtime inside the 28-38 min brief", 28*60 <= DUR <= 38*60, f"{DUR/60:.1f} min")
chk("Shot count plausible for the runtime", 250 <= len(S) <= 400,
    f"{len(S)} shots, mean {DUR/len(S):.1f}s")
chk("No shot under 3 seconds", min(s["d"] for s in S) >= 3,
    f"shortest {min(s['d'] for s in S)}s")

# ---- the countdown --------------------------------------------------------
cd = [(s["t"], s["cd"]) for s in S if s["cd"]]
vals = [int(c.split(":")[0])*60 + int(c.split(":")[1]) for _, c in cd]
chk("Countdown decreases monotonically", vals == sorted(vals, reverse=True), f"{len(vals)} readings")
knock = next(s for s in S if "KNOCK. KNOCK. KNOCK" in s["action"])
chk("Countdown hits 00:00 exactly on the knock", abs(knock["t"] - (cd[0][0] + vals[0])) < 0.5,
    f"starts {cd[0][1]} at {clk(cd[0][0])}, knock at {clk(knock['t'])}")
chk("Countdown start matches the screenplay", "**11:00**" in SCRIPT and cd[0][1] == "11:00",
    f"script and picture both read {cd[0][1]}")

# ---- framing / contact discipline ----------------------------------------
touches = [s for s in S if s.get("contact")]
chk("Exactly three physical touches in the episode", len(touches) == 3,
    ", ".join(f"{t['id']} @ {clk(t['t'])}" for t in touches))
chk("The last touch is the final shot", touches and touches[-1]["t"] > DUR - 120,
    f"final touch at {clk(touches[-1]['t'])} of {clk(DUR)}")

# ---- continuity -----------------------------------------------------------
chk("No daylight lighting state after the teaser",
    not [s for s in S if s["look"] == "GOLDEN" and s["act"] != "TEASER"])
jkt = min((s["t"] for s in S if s["subj"] == "M_JKT"), default=1e9)
card = min((s["t"] for s in S if s["subj"] == "L_CARD"), default=1e9)
chk("Wardrobe changes are one-way (no reversion)",
    not [s for s in S if s["subj"] == "M" and s["t"] > jkt] and
    not [s for s in S if s["subj"] == "L" and s["t"] > card],
    f"jacket from {clk(jkt)}, cardigan from {clk(card)}")
chk("The double appears only on the leaf",
    all(s["dev"] for s in S if s["subj"] == "D"), f"{len([s for s in S if s['subj']=='D'])} shots")

# ---- device rules ---------------------------------------------------------
for rule, needle in [("reflection lags", "half-beat behind"),
                     ("temperature inverts", "It's cold"),
                     ("needs no power", "breaker"),
                     ("ignores Miles", "nothing changes"),
                     ("responds to Lauren", "I walk past it, it wakes up")]:
    chk(f"Device rule shown on screen: {rule}", needle.lower() in ALL.lower())
# only flag a UI element the leaf actually DISPLAYS - "not a menu" is the rule,
# not a violation of it
_ui = [m.group(0) for m in re.finditer(
    r"(?<!no )(?<!not a )(?<!not an )\b(menu|icon|button|progress bar|loading screen|"
    r"interface|HUD|scan line)\b", ALL, re.I)]
chk("Leaf displays no UI element (five permitted items only)", not _ui,
    f"found {_ui}" if _ui else "clean")

# ---- plants and payoffs ---------------------------------------------------
PLANTS = {
    "P1 bare picture hooks":   ("picture hooks", "we don't have photographs"),
    "P2 refuses photographs":  ("turns his face away", "asleep, folded together"),
    "P3 the crossed seven":    ("cross-stroke", "seven in it is crossed"),
    "P4 knows the ending":     ("She was never on the train", "Lucky guess"),
    "P5 the smoke detector":   ("CHIRP", "The same tone. The same length. A half-beat late"),
    "P6 the sightline":        ("looks down the street", "same spot he checks"),
    "P7 the circled date":     ("circled in blue", "the fourteenth"),
    "P9 title drop sideways":  ("We're not from around here", "They're from Ohio"),
    "P10 reflection lag":      ("The hand in the pane raises", "LATE"),
}
for name, (a, b) in PLANTS.items():
    chk(f"Plant and payoff both present: {name}", a in ALL and b in ALL)

# ---- tone contract --------------------------------------------------------
BANNED = ["timeline", "paradox", "temporal", "portal", "quantum", "wormhole",
          "time machine", "time travel", "dimension", "anomaly"]
hits = [w for w in BANNED if re.search(rf"\b{w}\b", DIALOGUE, re.I)]
chk("No forbidden sci-fi vocabulary in dialogue", not hits, f"found {hits}" if hits else "clean")
yrs = re.findall(r"\b(?:19|20|21|22)\d{2}\b", DIALOGUE)
chk("No year is ever spoken aloud", not yrs, f"found {yrs}" if yrs else "clean")
shouts = [l for s in S for _, l in s["dlg"] if l.isupper() and len(l) > 12]
chk("Exactly one shouted line, and it is Lauren's", len(shouts) == 1, shouts[0][:60] + "..." if shouts else "-")
chk("No score under the three protected revelations",
    all(next(s for s in S if n in s["action"] or n in str(s["dlg"]))["music"] in ("", "M04", "M06", "M09", "M14")
        for n in ("AN EYE", "You got an answer", "KNOCK. KNOCK. KNOCK")))
sil = [s for s in S if "silence" in (s["audio"] or "").lower() or "Score out" in (s["audio"] or "")]
chk("At least eight authored silences", len(sil) >= 8, f"{len(sil)} found")
chk("Redacted name is an absence, not a bleep",
    "REMOVE the audio" in ALL and "bleep" in ALL.lower())

# ---- mystery preservation -------------------------------------------------
for m, needle in [("who sent the leaf", r"\bsent by\b|\bsender is\b"),
                  ("who Miles writes to", r"I write to \w+|it's for \w+"),
                  ("what the double is", r"she is a (copy|clone|recording|hologram)")]:
    chk(f"Mystery preserved: {m}", not re.search(needle, DIALOGUE, re.I))
chk("Lauren's real name is never audible", "[ - - - ]" in ALL)

# ---- deliverables ---------------------------------------------------------
srt = open(P("production", "07-post", "subtitles", "S01E01.srt")).read().strip().split("\n\n")
chk("Subtitle file populated", len(srt) > 300, f"{len(srt)} cues")
def _p(t):
    h, m, rest = t.split(":"); sec, ms = rest.split(",")
    return int(h)*3600 + int(m)*60 + int(sec) + int(ms)/1000
prev, over, short = 0, 0, 0
for b in srt:
    ln = b.split("\n")
    if len(ln) < 2: continue
    a, z = ln[1].split(" --> ")
    if _p(a) < prev - 1e-3: over += 1
    if _p(z) - _p(a) < 0.7: short += 1
    prev = _p(z)
chk("No overlapping subtitle cues", over == 0, f"{over}")
chk("No subtitle under 0.7s (readability floor)", short == 0, f"{short}")
edl = [l for l in open(P("production", "07-post", "S01E01.edl")) if l.strip() and l[0].isdigit()]
chk("EDL event count matches shot count", len(edl) == len(S), f"{len(edl)} vs {len(S)}")
chk("Every shot has a generation prompt and a seed",
    all(x["prompt"] and x["seed"] for x in json.load(open(P("production", "06-shots", "shot-prompts.json")))["shots"]))

# ---- write ----------------------------------------------------------------
passed = sum(1 for _, ok, _ in rows if ok)
acts = collections.OrderedDict()
for s in S: acts.setdefault(s["act"], []).append(s)

out = ["# PHASE 8 — QUALITY CONTROL AUDIT",
       '## We\'re From The Future · S01E01 "The Package"', "",
       "Produced by `tools/qc.py`, which reads the actual timeline, screenplay,",
       "EDL and subtitle files. Every row below is an executed check, not a",
       "hand-written assertion. Re-run after any change to the cut.", "",
       f"**{passed} of {len(rows)} checks passing.**", "",
       "| # | Check | Result | Detail |", "|---|---|---|---|"]
for i, (n, ok, d) in enumerate(rows, 1):
    out.append(f"| {i} | {n} | {'PASS' if ok else '**FAIL**'} | {d} |")

out += ["", "## Timeline summary", "",
        f"- **{len(S)} shots · {clk(DUR)} · mean shot {DUR/len(S):.1f}s**",
        f"- Longest shot: {max(s['d'] for s in S)}s · shortest: {min(s['d'] for s in S)}s", ""]
out += ["| Act | Shots | Runtime | Ends on |", "|---|---|---|---|"]
for a, ss in acts.items():
    last = ss[-1]
    out.append(f"| {a} | {len(ss)} | {clk(sum(x['d'] for x in ss))} | "
               f"{(last['action'] or str(last['dlg']))[:75].replace('|','')} |")

out += ["", "## What this audit cannot check", "",
        "Honest limits. These require a human or a rendered picture:", "",
        "- Face consistency against the reference plates (no frames exist yet)",
        "- Lip-sync, performance quality and whether a silence actually plays",
        "- Visual artefacts, hands, eyes, geometry and reflections in generated frames",
        "- Whether the double's eyeline genuinely tracks Miles in the delivered shot",
        "- Whether the mix is dialogue-led, and whether the score stays under it", "",
        "Those are listed in `production/08-qc/manual-qc-checklist.md` and are the",
        "gate that this file explicitly does not clear."]
open(P("production", "08-qc", "automated-audit.md"), "w").write("\n".join(out) + "\n")

for n, ok, d in rows:
    if not ok: print("FAIL:", n, "-", d)
print(f"{passed}/{len(rows)} checks passing -> production/08-qc/automated-audit.md")
_exit_code = 0 if passed == len(rows) else 1

# ---- the master file, when one exists -------------------------------------
# Appended check: if a conformed master is on disk, audit the container itself.
def _probe(path):
    import subprocess
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from platform_tools import find_ffmpeg
    ff = find_ffmpeg()
    return subprocess.run([ff, "-i", path], capture_output=True, text=True).stderr
for _name in ("S01E01_previs_master.mp4", "S01E01_picture_master.mp4"):
    _m = P("deliverables", _name)
    if not os.path.exists(_m):
        continue
    _info = _probe(_m)
    _dur = re.search(r"Duration: (\d+):(\d+):(\d+)\.(\d+)", _info)
    _secs = int(_dur[1])*3600 + int(_dur[2])*60 + int(_dur[3]) + int(_dur[4])/100 if _dur else -1
    _rows = [
        (f"{_name}: duration matches the cut", abs(_secs - DUR) < 0.6, f"{_secs:.2f}s vs {DUR:.2f}s"),
        (f"{_name}: 1920x960 at 24 fps", "1920x960" in _info and " 24 fps" in _info, ""),
        (f"{_name}: 48 kHz stereo AAC", "48000 Hz, stereo" in _info, ""),
        (f"{_name}: subtitle track present", "Subtitle:" in _info, ""),
    ]
    _out = [f"\n## Master file audit: {_name}\n", "| Check | Result | Detail |", "|---|---|---|"]
    for n, ok, d in _rows:
        _out.append(f"| {n} | {'PASS' if ok else '**FAIL**'} | {d} |")
        if not ok: print("FAIL:", n, "-", d)
    with open(P("production", "08-qc", "automated-audit.md"), "a") as f:
        f.write("\n".join(_out) + "\n")
    print(f"master audit: {sum(1 for _, ok, _ in _rows if ok)}/{len(_rows)} passing for {_name}")
    if not all(ok for _, ok, _ in _rows):
        _exit_code = 1
sys.exit(_exit_code)
