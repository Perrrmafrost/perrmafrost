# -*- coding: utf-8 -*-
"""
Generates every previs and post document from tools/shots_data.py.

  python3 tools/build.py

Assembly durations live in shots_data.SHOTS. This script applies the documented
FINE CUT trim (see production/04-previs/trim-log.md) and emits the shot list,
storyboard, animatic, generation prompts, EDL, subtitles, continuity matrix and
workspace dataset from the trimmed timeline. Nothing downstream is hand-typed,
so the shot list, the EDL and the subtitles cannot drift apart.
"""
import csv, json, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shots_data as D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
FPS = D.FPS

# ------------------------------------------------------------------ fine cut

PROTECT_PHRASES = (
    "MOST IMPORTANT", "THE PAYLOAD", "CUT TO BLACK BEFORE", "Hold it",
    "COUNTDOWN", "Do not cut away", "PERFORMANCE HIGH POINT",
    "LIVES OR DIES", "KEY IMAGE", "THE REVEAL", "Do NOT bleep",
    "BEST PASSAGE", "THE PIVOT", "LOUDEST HUMAN SOUND", "Hold three seconds",
    "no longer", "ONLY SHARED FRAME", "single most important sound",
)
PROTECT_SCENES = {"TITLE", "ENDCARD", "SC-23"}
TRIM_RATE = 0.14      # fine-cut compression on unprotected shots
TRIM_FLOOR = 3        # no shot below three seconds

def protected(s):
    if s["sc"] in PROTECT_SCENES:
        return True
    n = s.get("note", "")
    return any(p.lower() in n.lower() for p in PROTECT_PHRASES)

def fine_cut(shots):
    out, log = [], []
    for i, s in enumerate(shots):
        s = dict(s)
        s["assembly"] = s["dur"]
        if protected(s):
            s["trim"] = "protected"
        else:
            new = max(TRIM_FLOOR, int(round(s["dur"] * (1 - TRIM_RATE))))
            if new != s["dur"]:
                log.append((i, s["sc"], s["dur"], new))
            s["dur"] = new
            s["trim"] = "trimmed" if new != s["assembly"] else "at floor"
        out.append(s)
    return out, log

# ------------------------------------------------------------------ helpers

def tc(sec, offset_h=0):
    """Seconds -> HH:MM:SS:FF (non-drop)."""
    f = int(round(sec * FPS))
    h, r = divmod(f, 3600 * FPS)
    m, r = divmod(r, 60 * FPS)
    s, fr = divmod(r, FPS)
    return f"{h+offset_h:02d}:{m:02d}:{s:02d}:{fr:02d}"

def clock(sec):
    return f"{int(sec)//60:02d}:{int(sec)%60:02d}"

def srt_t(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def vtt_t(sec):
    return srt_t(sec).replace(",", ".")

def build_prompt(s):
    """Compose a generation prompt from locked blocks plus shot-specific action."""
    framing = {
        "XWIDE": "extreme wide establishing shot", "WIDE": "wide shot",
        "WIDE-2S": "wide two-shot", "WIDE-POV": "wide point-of-view shot",
        "MED": "medium shot", "MED-2S": "medium two-shot",
        "MED-TRACK": "medium tracking shot", "MCU": "medium close-up",
        "CU": "close-up", "CU-2S": "close-up two-shot", "ECU-INSERT": "extreme close-up insert",
        "CU-INSERT": "close-up insert", "INSERT-TV": "insert of a television screen",
        "INSERT-FOOTAGE": "insert of degraded recovered footage",
        "INSERT-STILL": "insert of a held still photograph",
        "TITLE": "title card on black",
    }.get(s["fr"], s["fr"].lower())
    move = {
        "STATIC": "locked-off camera", "SLOW PUSH": "very slow dolly push-in",
        "HANDHELD": "handheld, restrained", "HANDHELD-SUBTLE": "barely-perceptible handheld",
        "TRACK": "smooth tracking move", "TRACK BEHIND": "tracking behind the subject",
    }.get(s["mv"], s["mv"].lower())
    parts = [framing]
    if s["lens"]:
        parts.append(f"{s['lens']}mm")
    parts.append(move)
    subj = D.SUBJECTS.get(s["subj"], "")
    if subj:
        parts.append(subj)
    parts.append(s["action"])
    if s.get("dev"):
        parts.append(D.DEVICE if s["sc"] not in ("SC-07", "SC-08") or "box" not in s["action"].lower() else D.BOX)
    parts.append(D.LOCATIONS[s["loc"]])
    parts.append(D.LOOKS[s["look"]])
    parts.append(D.STYLE)
    return ". ".join(x.strip().rstrip(".") for x in parts if x) + "."

def build_neg(s):
    return D.NEG_BASE + ", " + D.NEG_BY_KIND.get(s["kind"], D.NEG_BY_KIND["face"])

def seed_for(i, s):
    """Deterministic per-shot seed, stable across rebuilds."""
    base = {"SC-%02d" % n: 1000 + n * 100 for n in range(1, 24)}
    return base.get(s["sc"], 9000) + i

# ------------------------------------------------------------------ timeline

SHOTS, TRIMLOG = fine_cut(D.SHOTS)
for s in SHOTS:
    s["slug"] = D.SCENES[s["sc"]][0]
    s["act"] = D.SCENES[s["sc"]][1]

# ---------------------------------------------------------- countdown calibration
# The leaf's countdown runs in REAL TIME with the episode and must hit 00:00 on
# the first knock. That makes the gap between the two a hard editorial constraint,
# not a hope. We calibrate it automatically: measure the gap the cut produces,
# then push the difference onto the longest unprotected shots inside the window.
# If the script says 11:00, the picture says 11:00.
CD_START_VALUE = "11:00"
CD_TARGET = 11 * 60

def retime(shots):
    t = 0.0
    for s in shots:
        s["start"], s["end"] = t, t + s["dur"]
        t += s["dur"]
    return t

def calibrate(shots):
    ci = next(i for i, s in enumerate(shots) if "11:00" in s["action"] and "10:59" in s["action"])
    ki = next(i for i, s in enumerate(shots) if "KNOCK. KNOCK. KNOCK" in s["action"])
    for _ in range(400):
        gap = sum(s["dur"] for s in shots[ci:ki])
        delta = CD_TARGET - gap
        if delta == 0:
            return ci, ki, True
        step = 1 if delta > 0 else -1
        # always take from the longest shots in the window: adding or removing a
        # second of air hurts least where there is most of it
        window = [s for s in shots[ci:ki]
                  if s["trim"] != "protected" and (step > 0 or s["dur"] > TRIM_FLOOR)]
        if not window:
            return ci, ki, False
        window.sort(key=lambda s: -s["dur"])
        for s in window[:abs(delta)]:
            s["dur"] += step
            s["calibrated"] = s.get("calibrated", 0) + step
    return ci, ki, False

CD_I, KNOCK_I, CD_OK = calibrate(SHOTS)
TOTAL = retime(SHOTS)
for i, s in enumerate(SHOTS):
    s["id"] = f"SH{i+1:04d}"
    s["seed"] = seed_for(i, s)
for s in SHOTS:
    s["contact"] = any(m in s["action"] for m in D.CONTACT_MARKERS)
_c = [s["id"] for s in SHOTS if s["contact"]]
assert len(_c) == 3, f"contact discipline broken: expected 3 touches, found {len(_c)} ({_c})"
ZERO_AT = SHOTS[KNOCK_I]["start"]
CD_START = SHOTS[CD_I]
for s in SHOTS:
    s["cd"] = clock(max(0, ZERO_AT - s["start"])) if CD_START["start"] <= s["start"] <= ZERO_AT else ""
assert CD_OK and SHOTS[CD_I]["cd"] == CD_START_VALUE, (
    f"countdown calibration failed: reads {SHOTS[CD_I]['cd']}, script says {CD_START_VALUE}")

os.makedirs(P("production", "07-post", "subtitles"), exist_ok=True)

# ------------------------------------------------------------------ 1. shot list
with open(P("production", "04-previs", "shot-list.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["shot_id", "scene_id", "act", "slugline", "tc_in", "tc_out", "runtime_in",
                "dur_s", "assembly_s", "framing", "movement", "lens_mm", "subjects",
                "location", "lighting", "device_in_frame", "physical_contact", "countdown_reads",
                "music_cue", "sound_cue", "dialogue", "action", "qc_note", "seed"])
    for s in SHOTS:
        w.writerow([s["id"], s["sc"], s["act"], s["slug"], tc(s["start"], 1), tc(s["end"], 1),
                    clock(s["start"]), s["dur"], s["assembly"], s["fr"], s["mv"], s["lens"],
                    s["subj"], s["loc"], s["look"], "Y" if s.get("dev") else "", "CONTACT" if s["contact"] else "",
                    s["cd"], s["music"], s["audio"],
                    " | ".join(f"{c}: {l}" for c, l in s["dlg"]), s["action"], s["note"], s["seed"]])

# ------------------------------------------------------------------ 2. prompts
prompts = []
for s in SHOTS:
    prompts.append({
        "shot_id": s["id"], "scene_id": s["sc"], "act": s["act"], "slugline": s["slug"],
        "runtime_in": clock(s["start"]), "tc_in": tc(s["start"], 1), "tc_out": tc(s["end"], 1),
        "duration_s": s["dur"], "framing": s["fr"], "camera_move": s["mv"],
        "lens_mm": s["lens"], "aspect": D.ASPECT, "fps": FPS,
        "subjects": s["subj"], "character_assets": {
            "M": "CHR-MILES-01-L1", "M_JKT": "CHR-MILES-01-L2", "L": "CHR-LAUREN-01-L1",
            "L_CARD": "CHR-LAUREN-01-L2", "D": "CHR-LAUREN-02-L1", "MB": "CHR-MILES-01-L1 + CHR-LAUREN-01-L1",
            "FIG": "CHR-FIGURE-01", "NONE": "-"}.get(s["subj"], "-"),
        "location_asset": f"LOC-{s['loc']}", "lighting_state": s["look"],
        "device_in_frame": bool(s.get("dev")),
        "countdown_reads": s["cd"] or None,
        "facial_performance": s["note"] or "Naturalistic. Preserve asymmetry and skin texture.",
        "dialogue": [{"character": c, "line": l} for c, l in s["dlg"]],
        "sound_cue": s["audio"], "music_cue": s["music"],
        "music_cue_name": D.CUES.get(s["music"], ("", ""))[0],
        "prompt": build_prompt(s), "negative_prompt": build_neg(s),
        "seed": s["seed"], "version": "v1",
        "qc": ["face lock vs reference plate", "wardrobe ID matches continuity matrix",
               "no bezel/port/logo on the leaf" if s.get("dev") else "prop continuity",
               "eyeline: the double tracks MILES" if s["subj"] == "D" else "eyeline consistent with blocking",
               "shadow/practical direction matches adjacent shots"],
    })
with open(P("production", "06-shots", "shot-prompts.json"), "w") as f:
    json.dump({"episode": "S01E01", "title": "The Package", "fps": FPS, "aspect": D.ASPECT,
               "shot_count": len(prompts), "runtime_s": round(TOTAL, 2),
               "runtime": clock(TOTAL), "shots": prompts}, f, indent=1)

# ------------------------------------------------------------------ 3. subtitles
# Laid out the way a subtitle conform actually works: each cue is placed at its
# proportional position inside its shot, given a duration from a reading-speed
# model, then swept once to guarantee a readability floor and no overlaps.
# Cues are allowed to cross a cut - real subtitles do - but never to collide.
CPS = 15.0          # characters per second, broadcast-comfortable
MIN_CUE = 0.9       # readability floor
MAX_CUE = 6.0
GAP = 0.08          # minimum blank between cues

def label(char, line):
    if char == "VOICE (O.S.)":
        return f"[muffled, through the door] {line}"
    if char == "DOUBLE":
        return f"[her voice] {line}"
    if char == "SYSTEM VOICE":
        return f"[system voice] {line}"
    return line

raw = []
for s_ in SHOTS:
    if not s_["dlg"]:
        continue
    weights = [max(len(l), 12) for _, l in s_["dlg"]]
    tot = sum(weights)
    cur = s_["start"] + s_["dur"] * 0.03
    span = s_["dur"] * 0.94
    for (char, line), wgt in zip(s_["dlg"], weights):
        raw.append({"t": cur, "d": min(MAX_CUE, max(MIN_CUE, len(line) / CPS)),
                    "char": char, "text": label(char, line), "line": line})
        cur += span * wgt / tot

raw.sort(key=lambda c: c["t"])
prev_end = -1.0
for c in raw:                       # single forward sweep: floor, then de-overlap
    c["t"] = max(c["t"], prev_end + GAP)
    c["end"] = c["t"] + c["d"]
    prev_end = c["end"]
cues = [(c["t"], c["end"], c["char"], c["text"]) for c in raw]
assert all(b - a >= MIN_CUE - 1e-6 for a, b, _, _ in cues), "subtitle below readability floor"
assert all(cues[i][0] >= cues[i-1][1] for i in range(1, len(cues))), "subtitle overlap"

with open(P("production", "07-post", "subtitles", "S01E01.srt"), "w") as f:
    for i, (a, b, _, text) in enumerate(cues, 1):
        f.write(f"{i}\n{srt_t(a)} --> {srt_t(b)}\n{text}\n\n")
with open(P("production", "07-post", "subtitles", "S01E01.vtt"), "w") as f:
    f.write("WEBVTT\n\n")
    for i, (a, b, _, text) in enumerate(cues, 1):
        f.write(f"{i}\n{vtt_t(a)} --> {vtt_t(b)}\n{text}\n\n")

# SDH captions are viewer-facing, so non-speech events get authored caption text
# rather than the production sound note. Anything without an authored caption is
# omitted: a caption that describes the mix instead of the sound is worse than
# no caption at all.
def sdh_caption(shot):
    a = (shot["audio"] or "")
    u = a.upper()
    act = shot["action"]
    if "DING-DONG" in u:                       return "[doorbell]"
    if "knuckle knocks" in a:                  return "[knocking - three, then two]"
    if "CHIRP" in u and "coffee table" in a:    return "[the chirp again - from the device]"
    if "CHIRP" in u and "off-screen" in a:      return "[the same chirp, from the living room]"
    if "CHIRP" in u:                            return "[smoke alarm chirps]"
    if "Breaker" in a:                          return "[the power cuts out]"
    if "brass mechanism" in a:                  return "[the deadbolt turns by itself]"
    if "Deadbolt, second" in a:                 return "[he locks the door again]"
    if "Deadbolt" in a:                         return "[deadbolt]"
    if "TOTAL SILENCE" in u or "absolute silence" in a:  return "[silence]"
    if "the audio bed itself stops" in a:       return "[all sound stops]"
    if "compressor stutters" in a:              return "[the refrigerator stutters]"
    if "Tape parting" in a:                     return "[packing tape tearing]"
    if "sound bed cuts" in a:                   return "[everything goes quiet]"
    if "Phone buzz" in a:                       return "[phone buzzes]"
    if "Rain begins" in a:                      return "[rain begins]"
    if "shouting a name" in a:                  return "[someone shouting a name we don't catch]"
    return None

sdh_raw = []
for s_ in SHOTS:
    cap = sdh_caption(s_)
    if cap:
        sdh_raw.append({"t": s_["start"] + 0.15, "d": 1.5, "text": cap})

sdh_all = sorted(
    [{"t": a, "d": b - a, "text": (f"{c}: {t}" if c in ("MILES", "LAUREN") else t)}
     for a, b, c, t in cues] + sdh_raw, key=lambda c: c["t"])
prev_end = -1.0
for c in sdh_all:
    c["t"] = max(c["t"], prev_end + GAP)
    c["end"] = c["t"] + c["d"]
    prev_end = c["end"]
with open(P("production", "07-post", "subtitles", "S01E01.sdh.vtt"), "w") as f:
    f.write("WEBVTT\n\n")
    for i, c in enumerate(sdh_all, 1):
        f.write(f"{i}\n{vtt_t(c['t'])} --> {vtt_t(c['end'])}\n{c['text']}\n\n")

# ------------------------------------------------------------------ 4. EDL
with open(P("production", "07-post", "S01E01.edl"), "w") as f:
    f.write("TITLE: WERE_FROM_THE_FUTURE_S01E01_THE_PACKAGE\nFCM: NON-DROP FRAME\n\n")
    for i, s in enumerate(SHOTS, 1):
        src_in, src_out = tc(0), tc(s["dur"])
        f.write(f"{i:03d}  {s['id']} V     C        {src_in} {src_out} {tc(s['start'],1)} {tc(s['end'],1)}\n")
        f.write(f"* FROM CLIP NAME: {s['id']}_{s['sc']}_{s['fr']}\n")
        if s["music"]:
            f.write(f"* COMMENT: MUSIC {s['music']} {D.CUES.get(s['music'],('',''))[0]}\n")
        if s["cd"]:
            f.write(f"* COMMENT: COUNTDOWN READS {s['cd']}\n")
    f.write(f"\n* TOTAL RECORD DURATION {tc(TOTAL,1)}\n")

# ------------------------------------------------------------------ 5. storyboard
with open(P("production", "04-previs", "storyboard.md"), "w") as f:
    f.write("# STORYBOARD & SHOT PLAN\n## We're From The Future - S01E01 \"The Package\"\n\n")
    f.write(f"**{len(SHOTS)} shots · {clock(TOTAL)} · {D.ASPECT} · {FPS} fps**\n\n")
    f.write("Generated from `tools/shots_data.py`. Do not edit by hand - edit the source "
            "and re-run `python3 tools/build.py`.\n\n---\n\n")
    cur_sc = None
    for s in SHOTS:
        if s["sc"] != cur_sc:
            cur_sc = s["sc"]
            f.write(f"\n## {cur_sc} — {s['slug']}\n*{s['act']}*\n\n")
        f.write(f"### {s['id']} · {clock(s['start'])} · {s['dur']}s · {s['fr']} / {s['mv']} / {s['lens']}mm\n")
        f.write(f"> {s['action']}\n\n" if s["action"] else "")
        if s["dlg"]:
            for c, l in s["dlg"]:
                f.write(f"- **{c}:** {l}\n")
            f.write("\n")
        meta = [f"**Light:** {s['look']}"]
        if s["audio"]: meta.append(f"**Sound:** {s['audio']}")
        if s["music"]: meta.append(f"**Music:** {s['music']} ({D.CUES[s['music']][0]})")
        if s["cd"]: meta.append(f"**Countdown:** {s['cd']}")
        f.write(" · ".join(meta) + "\n")
        if s["note"]:
            f.write(f"\n> [!IMPORTANT]\n> {s['note']}\n")
        f.write("\n")

# ------------------------------------------------------------------ 6. animatic
with open(P("production", "04-previs", "animatic.json"), "w") as f:
    json.dump({"episode": "S01E01", "fps": FPS, "aspect": D.ASPECT,
               "duration_s": round(TOTAL, 2),
               "shots": [{"id": s["id"], "sc": s["sc"], "act": s["act"], "slug": s["slug"],
                          "t": round(s["start"], 2), "d": s["dur"], "fr": s["fr"],
                          "mv": s["mv"], "lens": s["lens"], "look": s["look"],
                          "subj": s["subj"], "loc": s["loc"], "dev": bool(s.get("dev")), "contact": s["contact"],
                          "cd": s["cd"], "action": s["action"], "dlg": s["dlg"],
                          "audio": s["audio"], "music": s["music"], "note": s["note"]}
                         for s in SHOTS]}, f, indent=1)

# ------------------------------------------------------------------ 7. continuity matrix
WRD = {"M": "WRD-M-A", "M_JKT": "WRD-M-B", "L": "WRD-L-A", "L_CARD": "WRD-L-B",
       "MB": "WRD-M-A + WRD-L-A", "D": "WRD-D-A", "FIG": "WRD-F-A", "NONE": "-"}
def wardrobe(s):
    if s["subj"] == "MB":
        m = "WRD-M-B" if s["start"] >= next(x["start"] for x in SHOTS if x["subj"] == "M_JKT") else "WRD-M-A"
        l = "WRD-L-B" if s["start"] >= next(x["start"] for x in SHOTS if x["subj"] == "L_CARD") else "WRD-L-A"
        return f"{m} + {l}"
    return WRD.get(s["subj"], "-")

with open(P("production", "05-assets", "continuity-matrix.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["shot_id", "runtime", "scene", "time_of_day", "characters", "wardrobe",
                "miles_state", "lauren_state", "leaf_location", "leaf_state",
                "house_power", "weather", "device_temp_rule", "photos_on_wall", "flags"])
    for s in SHOTS:
        tod = "late afternoon" if s["look"] == "GOLDEN" else "night"
        power = "OUT" if s["look"] == "BLACKOUT" or (s["sc"] in ("SC-20", "SC-21", "SC-22")) else "on"
        if s["sc"] == "SC-12" and "breaker" in s["action"].lower(): power = "OUT (breaker)"
        leaf = ("in the box" if s["sc"] in ("SC-06", "SC-07", "SC-08") else
                "kitchen table" if s["sc"] in ("SC-09", "SC-10") else
                "coffee table" if s["sc"] in ("SC-11", "SC-14", "SC-15", "SC-17", "SC-18", "SC-19", "SC-20") else
                "drawer/cooler (failing)" if s["sc"] == "SC-12" else
                "in Lauren's bag" if s["sc"] in ("SC-21", "SC-22") else "-")
        state = ("dormant" if s["sc"] in ("SC-06", "SC-07", "SC-08") else
                 "active" if s.get("dev") and s["look"] in ("COLD_PANE", "MIXED") else
                 "dormant/cold")
        flags = []
        if s["subj"] == "D": flags.append("DOUBLE EYELINE=MILES")
        if s["cd"]: flags.append(f"COUNTDOWN={s['cd']}")
        if s["look"] == "GOLDEN" and s["act"] != "TEASER": flags.append("!! DAYLIGHT AFTER TEASER")
        w.writerow([s["id"], clock(s["start"]), s["sc"], tod, s["subj"], wardrobe(s),
                    "guarded" if s["act"] in ("TEASER", "ACT ONE") else "exposed",
                    "at ease" if s["act"] == "TEASER" else "escalating",
                    leaf, state, power,
                    "dry/clear" if s["look"] == "GOLDEN" else "light rain",
                    "cold toward room / warm away" if s.get("dev") else "-",
                    "NONE - four bare hooks", "; ".join(flags)])

# ------------------------------------------------------------------ 8. trim log
with open(P("production", "04-previs", "trim-log.md"), "w") as f:
    f.write("# FINE CUT TRIM LOG\n\nAssembly cut ran **%s** across %d shots. Prestige "
            "assemblies always run long; the fine cut removes air, not content.\n\n"
            % (clock(sum(s['assembly'] for s in SHOTS)), len(SHOTS)))
    f.write("## Rules applied\n\n"
            "1. Every shot not on the protected list is compressed by **%d%%**, rounded to "
            "the nearest second, with a **%ds floor**.\n"
            "2. **Protected shots keep their assembly length.** A shot is protected if it "
            "carries a note flagged as structurally load-bearing (the reveal, the reflection "
            "lag, the three-second pause, the countdown reads, the performance high point, "
            "the final shot) or belongs to the title, end card or tag.\n"
            "3. No trim may take a shot below three seconds, because below three seconds a "
            "held shot reads as a cut rather than an observation.\n\n"
            % (int(TRIM_RATE * 100), TRIM_FLOOR))
    f.write("## Result\n\n| | |\n|---|---|\n")
    f.write("| Assembly | %s |\n| Fine cut | %s |\n| Removed | %s |\n| Protected shots | %d |\n| Trimmed shots | %d |\n\n"
            % (clock(sum(s['assembly'] for s in SHOTS)), clock(TOTAL),
               clock(sum(s['assembly'] for s in SHOTS) - TOTAL),
               sum(1 for s in SHOTS if s["trim"] == "protected"), len(TRIMLOG)))
    f.write("## Protected shots (untouched)\n\n| Shot | Runtime | Length | Why |\n|---|---|---|---|\n")
    for s in SHOTS:
        if s["trim"] == "protected" and s["note"]:
            f.write(f"| {s['id']} | {clock(s['start'])} | {s['dur']}s | {s['note'][:110]} |\n")

# ------------------------------------------------------------------ 8b. asset manifest
CHAR_ASSETS = [
 ("CHR-MILES-01","character","Miles - locked face/identity","reference/miles_reference_source.jpg","v1.0","APPROVED"),
 ("CHR-MILES-01-L1","look","Miles look 1 - WRD-M-A","CHR-MILES-01","v1.0","APPROVED"),
 ("CHR-MILES-01-L2","look","Miles look 2 - WRD-M-B (jacket, boots)","CHR-MILES-01","v1.0","APPROVED"),
 ("CHR-LAUREN-01","character","Lauren - locked face/identity","reference/lauren_reference_source.jpg","v1.0","APPROVED"),
 ("CHR-LAUREN-01-L1","look","Lauren look 1 - WRD-L-A","CHR-LAUREN-01","v1.0","APPROVED"),
 ("CHR-LAUREN-01-L2","look","Lauren look 2 - WRD-L-B (cardigan)","CHR-LAUREN-01","v1.0","APPROVED"),
 ("CHR-LAUREN-02","character","The double - CHR-LAUREN-01 + scar, stillness, hair down","CHR-LAUREN-01","v1.0","APPROVED"),
 ("CHR-LAUREN-02-L1","look","Double look 1 - WRD-D-A","CHR-LAUREN-02","v1.0","APPROVED"),
 ("CHR-FIGURE-01","character","The figure (tag + street) - never a face","-","v1.0","APPROVED"),
 ("VOX-MILES","voice","Miles voice profile","production/01-bible/character-bible.md","v1.0","APPROVED"),
 ("VOX-LAUREN","voice","Lauren voice profile","production/01-bible/character-bible.md","v1.0","APPROVED"),
 ("VOX-DOUBLE","voice","Double voice profile - unprocessed, no breath","production/01-bible/character-bible.md","v1.0","APPROVED"),
 ("VOX-DOOR","voice","The voice at the door - warm, muffled, gender unclear","-","v1.0","APPROVED"),
 ("VOX-SYSTEM","voice","Tag system voice - flat, pleasant","-","v1.0","APPROVED"),
]
PROP_ASSETS = [
 ("PRP-LEAF-01","prop","The leaf - hero prop","production/05-assets/locations-and-props.md","v1.0","APPROVED"),
 ("PRP-BOX-01","prop","The package","production/05-assets/locations-and-props.md","v1.0","APPROVED"),
 ("PRP-LABEL-01","prop","The shipping label - crossed seven, 14 Oct","production/05-assets/locations-and-props.md","v1.0","APPROVED"),
 ("PRP-CAL-01","prop","Wall calendar - one circled date","-","v1.0","APPROVED"),
 ("PRP-HOOKS-01","prop","Four bare picture hooks","-","v1.0","APPROVED"),
 ("PRP-DETECTOR-01","prop","Smoke detector - single chirp recording","-","v1.0","APPROVED"),
 ("PRP-BOLT-01","prop","Brass deadbolt","-","v1.0","APPROVED"),
 ("PRP-BAGS-01","prop","Two dusty canvas duffels","-","v1.0","APPROVED"),
 ("PRP-PHOTO-01","prop","The photograph - NEVER SEEN","-","v1.0","LOCKED-HIDDEN"),
 ("PRP-PENDANT-01","prop","Lauren's pendant","-","v1.0","APPROVED"),
 ("PRP-IRON-01","prop","Fire iron","-","v1.0","APPROVED"),
 ("PRP-PHONE-01","prop","Lauren's phone","-","v1.0","APPROVED"),
 ("PRP-SHEET-01","prop","The tag's sheet - same object as the leaf","PRP-LEAF-01","v1.0","APPROVED"),
]
with open(P("production","05-assets","asset-manifest.csv"),"w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["asset_id","type","description","source_or_parent","version","status","used_in_shots","tags"])
    for a in CHAR_ASSETS:
        used = [s["id"] for s in SHOTS if a[0].startswith("CHR") and
                {"CHR-MILES-01":("M","M_JKT","MB"),"CHR-MILES-01-L1":("M","MB"),
                 "CHR-MILES-01-L2":("M_JKT",),"CHR-LAUREN-01":("L","L_CARD","MB"),
                 "CHR-LAUREN-01-L1":("L","MB"),"CHR-LAUREN-01-L2":("L_CARD",),
                 "CHR-LAUREN-02":("D",),"CHR-LAUREN-02-L1":("D",),
                 "CHR-FIGURE-01":("FIG",)}.get(a[0],()) and s["subj"] in
                {"CHR-MILES-01":("M","M_JKT","MB"),"CHR-MILES-01-L1":("M","MB"),
                 "CHR-MILES-01-L2":("M_JKT",),"CHR-LAUREN-01":("L","L_CARD","MB"),
                 "CHR-LAUREN-01-L1":("L","MB"),"CHR-LAUREN-01-L2":("L_CARD",),
                 "CHR-LAUREN-02":("D",),"CHR-LAUREN-02-L1":("D",),
                 "CHR-FIGURE-01":("FIG",)}.get(a[0],())]
        w.writerow(list(a) + [f"{len(used)} shots" if used else "-",
                              "character;locked;face-lock" if a[1]!="voice" else "voice;locked"])
    for a in PROP_ASSETS:
        used = [s["id"] for s in SHOTS if s.get("dev")] if a[0]=="PRP-LEAF-01" else []
        w.writerow(list(a) + [f"{len(used)} shots" if used else "-", "prop;locked;continuity-tracked"])
    for k, v in D.LOCATIONS.items():
        used = [s["id"] for s in SHOTS if s["loc"]==k]
        w.writerow([f"LOC-{k}","location",v[:100],"production/05-assets/locations-and-props.md",
                    "v1.0","APPROVED",f"{len(used)} shots","location;locked"])
    for k, v in D.LOOKS.items():
        used = [s["id"] for s in SHOTS if s["look"]==k]
        w.writerow([f"LGT-{k}","lighting state",v[:100],"production/05-assets/lookbook.md",
                    "v1.0","APPROVED",f"{len(used)} shots","lighting;locked"])
    for k, v in D.CUES.items():
        if not k: continue
        used = [s["id"] for s in SHOTS if s["music"]==k]
        w.writerow([k,"music cue",f"{v[0]} - {v[1]}","production/07-post/music-cue-sheet.md",
                    "v1.0","APPROVED",f"{len(used)} shots","music;cue"])
    for s in SHOTS:
        w.writerow([s["id"],"shot",s["action"][:100],s["sc"],"v1","READY-TO-GENERATE",
                    s["id"],f"shot;{s['act'].lower().replace(' ','-')};{s['fr'].lower()}"])

# ------------------------------------------------------------------ 9. workspace data
with open(P("workspace", "data.js"), "w") as f:
    f.write("window.EPISODE = " + json.dumps({
        "title": "The Package", "series": "We're From The Future", "code": "S01E01",
        "runtime_s": round(TOTAL, 2), "runtime": clock(TOTAL), "fps": FPS, "aspect": D.ASPECT,
        "shot_count": len(SHOTS),
        "cues": {k: {"name": v[0], "desc": v[1]} for k, v in D.CUES.items() if k},
        "looks": D.LOOKS, "locations": D.LOCATIONS,
        "scenes": [{"id": k, "slug": v[0], "act": v[1]} for k, v in D.SCENES.items()],
        "shots": [{"id": s["id"], "sc": s["sc"], "act": s["act"], "slug": s["slug"],
                   "t": round(s["start"], 2), "d": s["dur"], "asm": s["assembly"],
                   "fr": s["fr"], "mv": s["mv"], "lens": s["lens"], "look": s["look"],
                   "subj": s["subj"], "loc": s["loc"], "dev": bool(s.get("dev")), "contact": s["contact"],
                   "cd": s["cd"], "action": s["action"], "dlg": s["dlg"],
                   "audio": s["audio"], "music": s["music"], "note": s["note"],
                   "seed": s["seed"], "prompt": build_prompt(s), "neg": build_neg(s),
                   "wrd": wardrobe(s)} for s in SHOTS],
    }, indent=1) + ";\n")

# ------------------------------------------------------------------ report
asm = sum(s["assembly"] for s in SHOTS)
print(f"shots          {len(SHOTS)}")
print(f"assembly       {clock(asm)}")
print(f"fine cut       {clock(TOTAL)}   ({len(TRIMLOG)} trimmed, "
      f"{sum(1 for s in SHOTS if s['trim']=='protected')} protected)")
print(f"subtitle cues  {len(cues)}")
print(f"contact        {len(_c)} touches in the episode: " +
      ", ".join(f"{i} at {clock(next(x for x in SHOTS if x['id']==i)['start'])}" for i in _c))
cal = sum(1 for s in SHOTS if s.get("calibrated"))
print(f"countdown      starts {clock(CD_START['start'])} reading {CD_START['cd']}, "
      f"hits 00:00 at {clock(ZERO_AT)} on the knock  [OK, {cal} shots calibrated]")
tagged = sum(s['dur'] for s in SHOTS if s['sc']=='SC-23')
print(f"story runtime  {clock(TOTAL - tagged)}  (excl. {int(tagged)}s post-credit tag)")
