# -*- coding: utf-8 -*-
"""
Builds the 30s teaser and 60s trailer as real cuts: shot IDs pulled from the
episode timeline, durations declared, an EDL emitted for each, and the total
asserted. Change a shot here and the cut sheet, the EDL and the duration all move.

    python3 tools/build_promos.py
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
FPS = 24
EP = {s["id"]: s for s in json.load(open(P("production", "04-previs", "animatic.json")))["shots"]}

def tc(sec, h=0):
    f = int(round(sec * FPS)); hh, r = divmod(f, 3600*FPS); mm, r = divmod(r, 60*FPS); ss, ff = divmod(r, FPS)
    return f"{hh+h:02d}:{mm:02d}:{ss:02d}:{ff:02d}"

# (source shot id | None, duration in the promo, treatment)
TEASER = [
    (None,     1.5, "BLACK. Room tone only: a refrigerator, and rain."),
    ("SH0003", 2.5, "The kitchen. Warm. She is cooking badly. He is sorting mail."),
    ("SH0008", 1.5, "She reaches past him for the salt. He moves without looking up."),
    ("SH0021", 2.0, "Four bare picture hooks in a hallway. No frames."),
    ("SH0046", 1.5, "The doorbell. Both of them stop."),
    ("SH0049", 3.0, "A small brown box on a wet mat, squared to the step."),
    (None,     1.0, "BLACK."),
    ("SH0074", 1.5, "A blade going through packing tape. Close. Too loud."),
    ("SH0096", 0.8, "AN EYE, filling a pane of glass. It blinks once."),
    (None,     1.2, "BLACK. Silence."),
    ("SH0126", 3.0, "A woman's face in darkness. It is her own face."),
    ("SH0214", 2.0, "DO NOT GO BACK."),
    ("SH0281", 1.5, "The deadbolt turns by itself."),
    (None,     0.8, "BLACK."),
    ("SH0308", 1.2, "Knock. Knock. Knock. Pause. Knock. Knock."),
    (None,     0.5, "BLACK. Nothing."),
    ("TITLE",  4.5, "TITLE CARD: WE'RE FROM THE FUTURE"),
]

TRAILER = [
    (None,     2.0, "BLACK. Rain. A refrigerator cycling on."),
    ("SH0003", 3.0, "The kitchen, warm, ordinary. LAUREN cooking. MILES with the mail."),
    ("SH0008", 2.0, "She reaches past him. He moves. Fifteen years of choreography."),
    ("SH0016", 2.0, "INSERT: a notepad. She writes a seven. She begins to cross it. She stops."),
    ("SH0021", 2.5, "Four bare picture hooks. Four pale rectangles where nothing faded."),
    ("SH0032", 2.5, "She lifts a phone to photograph him. He turns his face into her shoulder."),
    (None,     0.8, "BLACK."),
    ("SH0046", 1.5, "The doorbell."),
    ("SH0049", 3.0, "A box. Dead centre on the mat. Squared to the step. Bone dry."),
    ("SH0074", 2.0, "The blade through the tape."),
    ("SH0096", 1.0, "AN EYE."),
    (None,     1.0, "BLACK. Total silence."),
    ("SH0126", 5.5, "The face on the pane. Her face, her age, a scar she does not have."),
    ("SH0148", 1.5, "Three seconds of footage: the two of them, older, running, bleeding."),
    ("SH0157", 2.0, "A brass drawer pull. Cold."),
    ("SH0160", 2.0, "The house is dark. The pane is not."),
    ("SH0161", 2.5, "The street. Every house lit but theirs."),
    ("SH0237", 2.5, "A photograph on a phone: the two of them asleep. Nobody took it."),
    ("SH0250", 2.5, "A motel on a state highway. A sign with a dead letter."),
    ("SH0214", 3.0, "DO NOT GO BACK."),
    ("SH0220", 2.0, "A number begins to count down."),
    ("SH0281", 2.0, "The deadbolt turns. One full revolution."),
    (None,     1.0, "BLACK."),
    ("SH0308", 1.5, "Three knocks. Then two."),
    (None,     0.7, "BLACK. Nothing at all."),
    ("TITLE",  5.0, "TITLE CARD: WE'RE FROM THE FUTURE"),
    (None,     3.0, "CARD: SEASON ONE / EPISODE ONE / THE PACKAGE"),
]

VO = {
 "teaser": [
   (7.0,  "LAUREN", "Did you order something?"),
   (8.6,  "MILES",  "No."),
   (14.5, "DOUBLE", "You've been here too long."),
   (24.0, "VOICE",  "It's me."),
 ],
 "trailer": [
   (10.5, "LAUREN", "Did you order something?"),
   (12.0, "MILES",  "No."),
   (13.4, "MILES",  "Did you?"),
   (22.0, "DOUBLE", "You've been here too long."),
   (24.0, "DOUBLE", "It's started to hold."),
   (33.5, "LAUREN", "You didn't get a package."),
   (35.2, "LAUREN", "You got an answer."),
   (44.0, "MILES",  "Nothing comes through whole."),
   (52.5, "VOICE",  "It's me."),
 ],
}

def build(name, cut, target, out_md, out_edl):
    t, rows, ev = 0.0, [], []
    for sid, d, treat in cut:
        src = EP.get(sid)
        rows.append((tc(t), d, sid or "-", src["fr"] if src else "-",
                     f"{int(src['t'])//60:02d}:{int(src['t'])%60:02d}" if src else "-", treat))
        ev.append((sid or "BLACK", d, t))
        t += d
    lines = [f"# {name.upper()}", "", f"**Duration: {t:.1f}s** · {len(cut)} events · "
             f"2.00:1 master with 16:9 and 9:16 extractions", "",
             "Assembled from the episode timeline by `tools/build_promos.py`. Every source",
             "shot is a real shot with a real runtime; nothing here is a frame that does not",
             "exist in the cut.", "",
             "## Editorial rules", "",
             "- **No voice-over narration.** Only dialogue lifted from the episode.",
             "- **No music bed until the last third.** It opens on room tone.",
             "- **Nothing after the knock.** The promo ends where the episode ends.",
             "- **The double's face is shown; the double's scar is not resolvable.** "
             "Reserve it for the episode.",
             "- **No shot from Act Five beyond the knock.** The final image is never in a promo.",
             "", "## Cut", "",
             "| TC | Dur | Source | Framing | From | Treatment |", "|---|---|---|---|---|---|"]
    for a, d, sid, fr, at, tr in rows:
        lines.append(f"| {a} | {d:.1f}s | {sid} | {fr} | {at} | {tr} |")
    lines += ["", "## Audio", "", "| At | Speaker | Line |", "|---|---|---|"]
    for at, who, line in VO[name.split()[0].lower()]:
        lines.append(f"| {tc(at)} | {who} | \"{line}\" |")
    lines += ["", "## Music", "",
              "Room tone and rain only for the first two thirds. The score enters on the",
              "cut to the pane in the dark and consists of one low sustained tone. "
              "**It stops before the knock.**", "",
              f"## Delivery", "",
              "| Format | Note |", "|---|---|",
              "| 2.00:1 | master |",
              "| 16:9 | centre extract, safe |",
              "| 9:16 | **inserts and singles only.** The two-shots and the street wide "
              "have no valid vertical extraction and are replaced by held black with type. |"]
    open(P(out_md), "w").write("\n".join(lines) + "\n")

    with open(P(out_edl), "w") as f:
        f.write(f"TITLE: {name.upper().replace(' ','_')}\nFCM: NON-DROP FRAME\n\n")
        for i, (sid, d, at) in enumerate(ev, 1):
            f.write(f"{i:03d}  {sid[:8]:8s} V     C        {tc(0)} {tc(d)} {tc(at,1)} {tc(at+d,1)}\n")
            f.write(f"* FROM CLIP NAME: {sid}\n")
        f.write(f"\n* TOTAL RECORD DURATION {tc(t)}\n")
    return t

a = build("teaser 30", TEASER, 30, "production/09-marketing/teaser-30s.md",
          "production/09-marketing/teaser-30s.edl")
b = build("trailer 60", TRAILER, 60, "production/09-marketing/trailer-60s.md",
          "production/09-marketing/trailer-60s.edl")
assert 28 <= a <= 32, f"teaser is {a}s"
assert 57 <= b <= 63, f"trailer is {b}s"
print(f"teaser  {a:.1f}s  ({len(TEASER)} events)")
print(f"trailer {b:.1f}s  ({len(TRAILER)} events)")
missing = [s for s, _, _ in TEASER + TRAILER if s and s != "TITLE" and s not in EP]
assert not missing, f"promo references shots not in the cut: {missing}"
print("all promo sources verified against the episode timeline")
