#!/usr/bin/env python3
"""Build stills_manifest.jsonl: every reference still and location plate prompt in the production bible.

    python extract_stills.py              # write stills_manifest.jsonl next to this script, then validate
    python extract_stills.py --seed 7     # validate with a different random spot-check sample
    python extract_stills.py --out x.jsonl

Deterministic and stdlib-only: the same bible gives a byte-identical manifest on every run.

Sources (film/production_bible/):
  01_characters.md          numbered stills  `N. **<still id>** (...) · aspect ratio **4:5**` + a `> prompt` line;
                            plus two expression stills per entry that has a "Sheet expressions" line
                            (01 §0.7: rerun the front prompt with the expression in place of
                            "neutral relaxed expression").
  02_units_and_machines.md  `**REF A — ..., 2:3:**` / `**REF B — ...**` (ids <TOKEN>_REF_A / _REF_B) and the
                            single `**REF — 16:9:**` of the §14 machines (id <TOKEN>_REF).
  03_locations.md           one `**PLATE — establishing, 16:9:**` paragraph per entry, generated once per
                            lighting variant "changing only the lighting sentence" (03 §0.8); ids
                            LOC_<TOKEN>_<VARIANT>_plate. PLATE_RULES below names, per entry, the variant the
                            written plate already shows (emitted verbatim) and the exact lighting sentence that
                            the other variants' phrases replace.
  04_props.md               `**REF — 1:1:**` (id <TOKEN>_REF).

Record fields: id, kind (character|unit|prop|location|first_frame), token, aspect, width, height, prompt, negative,
method ("text" or "edit_from:<parent still id>"), priority (1 = LOCAL_SESSION_BRIEF step 5, else 2), source.

Only mechanical substitutions the bible prescribes are made (the expression swap and the lighting swap; the
variant phrase gets a capital first letter and a closing full stop so it reads as a sentence). Everything else
is copied byte for byte. The video style suffix (05 §1.1) is never appended (05 §1.3).
"""
import argparse
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FILM = HERE.parent.parent
BIBLE = FILM / "production_bible"
SCREENPLAY = FILM / "screenplay"

# Aspect ratio -> generation size: about one megapixel, both sides divisible by 16 (the usual SDXL/Flux buckets).
ASPECT_SIZES = {
    "1:1": (1024, 1024),
    "4:5": (896, 1120),
    "2:3": (832, 1248),
    "3:2": (1248, 832),
    "16:9": (1344, 768),
    "9:16": (768, 1344),
}

# LOCAL_SESSION_BRIEF.md step 5.
PRINCIPALS = ["CHAR_TUT", "CHAR_NOUR", "CHAR_ADAEZE", "CHAR_TOMAS", "CHAR_TAREK", "CHAR_FATHI",
              "CHAR_RAMI", "CHAR_HALE", "CHAR_LAYLA", "CHAR_AKHENATEN"]
PRIORITY_UNITS = ["UNIT_SHABTI", "UNIT_REIS", "UNIT_JACKAL", "UNIT_FLY", "UNIT_NURSE", "UNIT_INCHWORM"]
PRIORITY_SEQS = {1, 2, 3}

# Derived stills: the bible says these are made by image-editing an approved parent still (01 §0.7, CHAR_TUT_CHILD
# "Generate from the approved CHAR_TUT front still (age-regressed)", CHAR_AKHENATEN notes "image-editing the
# approved forecast stills", CHAR_TUT_CHILD_11_front "derive by image-editing CHAR_TUT_CHILD_9_front").
# Views other than the front are edited from the parent still of the same view.
EDIT_PARENTS = {
    "CHAR_TUT_CHILD_9_front": "CHAR_TUT_A0_front",
    "CHAR_TUT_CHILD_9_34": "CHAR_TUT_A0_34",
    "CHAR_TUT_CHILD_9_profile": "CHAR_TUT_A0_profile",
    "CHAR_TUT_CHILD_9_full": "CHAR_TUT_A0_full",
    "CHAR_TUT_CHILD_6_front": "CHAR_TUT_A0_front",
    "CHAR_TUT_CHILD_11_front": "CHAR_TUT_CHILD_9_front",
    "CHAR_AKHENATEN_1336_front": "CHAR_AKHENATEN_A_front",
    "CHAR_AKHENATEN_1336_34": "CHAR_AKHENATEN_A_34",
    "CHAR_AKHENATEN_1336_profile": "CHAR_AKHENATEN_A_profile",
    "CHAR_AKHENATEN_1336_full": "CHAR_AKHENATEN_A_full",
}
# Tokens whose faces are derived: their expression stills are edits of their own approved front still.
DERIVED_FACE_TOKENS = ("CHAR_TUT_CHILD", "CHAR_AKHENATEN_1336")

# 03 plates. token -> (variant the written plate shows, exact lighting sentence(s) to replace, {variant: reason
# it is not emitted}). lighting None = no single lighting sentence exists (the light is written into the set
# description), so only the written plate is emitted, under its own variant. Entries with one variant need no rule.
PLATE_RULES = {
    "LOC_EMBALMING_1323": ("NIGHT", "Deep amber lamplight, cool lapis-blue shadows, faint lamp smoke.", {}),
    "LOC_KV62_BURIAL_1323": ("NIGHT", "Clay oil lamps on the floor throw flickering amber light; deep blue-black "
                             "shadows fill the corners.", {}),
    "LOC_KV15_LAB_1925": ("DAY", "A hard shaft of daylight falls from the entrance at the upper right, dust glowing "
                          "in it.", {}),
    "LOC_AMARNA_TEMPLE_1336": ("NOON_1336", "Blinding white-gold light, hard short shadows, highlights blooming.", {}),
    "LOC_GEM_CC": ("NIGHT", "Clean cool-white LED light, precise spotlights on the cradle, polished reflections.", {}),
    "LOC_GEM_PLANT_ROOM": ("NIGHT", "Hard white overhead strip light, flat and industrial.", {}),
    "LOC_GEM_TUNNEL": ("NIGHT", "Cool white light at half brightness, long soft reflections on the floor.", {}),
    "LOC_GEM_TUT_GALLERIES": ("NIGHT", "Warm gold inside the glass, cool blue-black between.", {}),
    "LOC_GEM_ATRIUM": ("GALA", None, "the light (statue lit warmly from below, pyramids floodlit gold) is written "
                       "into the set sentences"),
    "LOC_GEM_BOAT_HALL": ("NIGHT", "Warm spotlights rake the wood; the hall is black around it.", {}),
    "LOC_GEM_LOADING_DOCK": ("NIGHT", "Tall lamp masts pool orange sodium light; beyond a perimeter fence, dark open "
                             "desert. Hard black shadows.", {}),
    "LOC_GEM_ROOF": ("DAWN", "The sun is just below the horizon at the left; the sky is cool blue warming to pale "
                     "gold, the pyramids' left faces catch faint rose light, and haze lies over the city.", {}),
    "LOC_NOUR_FLAT": ("NIGHT", None, "the light (desk lamp, laptop glow, city lights, night-light) is written into "
                      "the set sentences"),
    "LOC_CONTROL_ROOMS": ("LIVE", None, "the light shares a sentence with the room description and the glowing "
                          "video wall is set dressing"),
    "LOC_CAIRO_FLYOVER": ("BLACKOUT_ROLLING", "Some districts still glow sodium orange, others are completely black; "
                          "a wide dark river glints far below.", {}),
    "LOC_CORNICHE_DOCK": ("BLACKOUT", None, "the blackout (dark towers, fires on the far bank, stars in the water) "
                          "is written into the set sentences"),
    "LOC_NILE": ("DAWN", "Mist lies on the water; the sky is pale rose rising to cool blue, the palms in "
                 "silhouette.", {}),
    "LOC_KARNAK_RAM_AVENUE": ("NIGHT", "The gateway is lit hard white from below by a few floodlights; the rams cast "
                              "long black shadows across the paving; palm trees and a dark, unlit town lie beyond "
                              "under a starry sky.", {}),
    "LOC_KARNAK_HYPOSTYLE": ("NIGHT", "Hard white shafts of floodlight fall from far above between the columns; the "
                             "aisles between are deep black.", {}),
    "LOC_KARNAK_NINTH_PYLON": ("NIGHT_WORK", "Harsh white work floods on stands light the scene; a grid of small "
                               "drone lights hangs over the field against a black starry sky.", {}),
    "LOC_KARNAK_SACRED_LAKE": ("NIGHT", "The water mirrors the stars and a few white drone lights overhead.", {}),
    "LOC_WEST_BANK_FIELDS": ("NIGHT", None, "the pre-dawn light (deep blue sky, last stars) is written into the "
                             "set sentence"),
    "LOC_VOK": ("PREDAWN", None, "the pre-dawn light (sky paling in the east) is written into the set sentences"),
    "LOC_KV62_STAIR": ("PREDAWN", "Deep blue pre-dawn light, the doorway a black rectangle.", {}),
    "LOC_KV62_BURIAL_2033": ("BLACKOUT", "The only light is a hard white torch beam from the doorway sweeping the "
                             "painted wall; deep black beyond.", {}),
    "LOC_KV62_NORTH_CORRIDOR": ("TORCH", "A single white torch beam full of hanging dust.", {}),
    "LOC_KV62_HEART_CHAMBER": ("TORCH", "Lit only by one hard white torch beam from the doorway, with deep black "
                               "shadows.", {}),
    "LOC_LUXOR_RAIL_YARD": ("DAY", "Hard sun, a bleached sky, deep black shade under the shed, heat shimmer over the "
                            "rails.", {}),
    "LOC_NIGHT_TRAIN": ("NIGHT", "No other lights anywhere, a dense star field above.",
                        {"BLUE": "a powder effect over the headlamp beam, not a lighting setup"}),
    "LOC_AMARNA_PLAIN_2033": ("NIGHT", None, "the night Garden light (lamp-masts, floodlit stela, star field) is "
                              "written into the set sentences"),
    "LOC_QUARRY": ("SUNSET", "The sun touches the western rim, turning the walls deep orange, with long blue "
                   "shadows.", {}),
    "LOC_DESERT_ROAD": ("NIGHT", "Far ahead on the horizon, a white glow of floodlights. A dense star field over "
                        "total darkness.", {}),
    "LOC_SAQQARA": ("SUNSET", "The low sun turns the steps deep orange-gold, with long blue shadows; to the east the "
                    "green edge of the valley darkens.", {}),
    "LOC_SERAPEUM_GREATER": ("WORKLIGHTS", None, "the work lights are written into the set sentence"),
    "LOC_OSIRIS_SHAFT": ("TORCH", "A single white torch beam; reflections ripple across the ceiling.", {}),
    "LOC_GP_MAMUN_TUNNEL": ("TORCH", "One torch beam.", {}),
    "LOC_GP_GRAND_GALLERY": ("BLACKOUT_TORCH", "The electric lights are dead; a single torch beam slices up the "
                             "slope, the corbels catching light in stepped bands, the top lost in black.", {}),
    "LOC_HALL_TWO_TRUTHS": ("THREE_SOURCE", "Everything is pure black except for a cold silver-white plume of light "
                            "standing in the balance's right-hand pan, a warm amber-gold glow low at the left, and one "
                            "small vertical amber slit low on the left; the stone is read only by rim light.", {}),
    "LOC_GP_NORTH_FACE": ("DAWN_0614", "A low gold sun just clearing the horizon at frame left lights the pyramid's "
                          "east face and draws a thin gold line down the north-east corner, while the north face "
                          "itself lies in soft blue shadow; dust haze glows gold at the left.", {}),
    "LOC_FIRST_TIME": ("MORNING", "Soft green-gold morning light.", {}),
    "LOC_DEWAR_VAULT": ("LIT", "Cool white overhead light, soft reflections on the steel, quiet and clinical.", {}),
    "LOC_PORT_WAREHOUSE": ("DAWN_GARDEN", "Soft, shadowless white light.", {}),
    "LOC_STADIUM_GARDEN": ("DAY_GARDEN", "Soft overcast white light, shadowless and calm.", {}),
}
# Plates that show vehicles, boats or animals on purpose: NEG_PLATE ("people, figures, crowds, vehicles, animals")
# would fight them, so it is left off even though the plate says "no people".
NO_NEG_PLATE = {"LOC_GEM_LOADING_DOCK", "LOC_KARNAK_QUAY", "LOC_QUARRY", "LOC_FIRST_TIME", "LOC_CORNICHE_DOCK",
                "LOC_GEM_TUT_GALLERIES"}

TIME_WORDS = re.compile(r"\b(night|midnight|dawn|pre-dawn|sunrise|sunset|dusk|midday|noon|afternoon|morning|"
                        r"daylight|blackout|power cut)\b", re.I)


class BibleError(Exception):
    pass


def read(path):
    return path.read_text(encoding="utf-8")


def size(aspect, where):
    if aspect not in ASPECT_SIZES:
        raise BibleError(f"{where}: aspect {aspect} has no size mapping")
    return ASPECT_SIZES[aspect]


def one_line_after(lines, i, where):
    """The paragraph that starts after line i (skipping blanks); it must be a single line."""
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines):
        raise BibleError(f"{where}: no prompt paragraph")
    if j + 1 < len(lines) and lines[j + 1].strip() and not lines[j + 1].startswith(("**", "---", "#", "- ")):
        raise BibleError(f"{where}: prompt paragraph spans more than one line")
    return lines[j].strip(), j


def record(sid, kind, token, aspect, prompt, negative, method, priority, source):
    w, h = size(aspect, sid)
    return {"id": sid, "kind": kind, "token": token, "aspect": aspect, "width": w, "height": h,
            "prompt": prompt, "negative": negative, "method": method, "priority": priority, "source": source}


# ---------------------------------------------------------------- 00 and 05

def index_tokens():
    tokens = []
    for line in read(BIBLE / "00_INDEX.md").split("\n"):
        m = re.match(r"^\| ((?:CHAR|UNIT|LOC|PROP)_[A-Z0-9_]+) \|", line)
        if m:
            tokens.append(m.group(1))
    return tokens


def style_texts():
    text = read(BIBLE / "05_style_and_prompt_grammar.md")
    suffix = re.search(r"### 1\.1 .*?\n\n> (.+?)\n", text, re.S).group(1)
    neg = re.search(r"### 2\.1 .*?\n\n> (.+?)\n", text, re.S).group(1)
    neg_plate = re.search(r"^\| `NEG_PLATE` \| [^|]+ \| (.+?) \|$", text, re.M).group(1)
    return suffix, neg, neg_plate


def token_of(sid, tokens):
    hits = [t for t in tokens if sid == t or sid.startswith(t + "_")]
    if not hits:
        raise BibleError(f"{sid}: no 00_INDEX token is a prefix of this still id")
    return max(hits, key=len)


# ---------------------------------------------------------------- 01 characters

def parse_characters(tokens, notes):
    lines = read(BIBLE / "01_characters.md").split("\n")
    text = "\n".join(lines)
    common = re.search(r"\*\*Common still negative\*\* \(append to every still\): \*(.+?)\*, plus", text).group(1)
    blocks, cur, section = [], None, None
    for i, line in enumerate(lines):
        m = re.match(r"^## (\d+b?)\. ", line)
        if m:
            section = m.group(1)
        m = re.match(r"^### (CHAR_[A-Z0-9_]+) ", line)
        if m:
            cur = {"token": m.group(1), "section": section, "start": i, "lines": []}
            blocks.append(cur)
        elif line.startswith("## ") and cur is not None:
            cur = None
        if cur is not None:
            cur["lines"].append((i, line))

    out = []
    for b in blocks:
        char_neg, still_negs, desic_neg, expressions, stills = None, [], None, [], []
        intro, sub = "", ""
        for i, line in b["lines"]:
            if line.startswith("#### "):
                sub = line
            m = re.match(r"^\*\*Character negative(?:\*\* \([^)]*\):|:\*\*) (.+)$", line)
            if m:
                char_neg = m.group(1)
            m = re.match(r"^\*Still negative:\* (.+)$", line)
            if m:
                still_negs.append((i, m.group(1)))
            m = re.match(r"^\*Desiccation negative \([^)]*\):\* (.+)$", line)
            if m:
                desic_neg = m.group(1)
            m = re.match(r'^\*\*Sheet expressions\*\* \(use the front-still prompt, replacing "neutral relaxed '
                         r'expression"\): (.+)$', line)
            if m:
                parts = re.split(r" · (?=\(\d\) )", m.group(1))
                expressions = [re.sub(r"^\(\d\) ", "", p) for p in parts]
            if line.startswith("**") and "eference still" in line:
                intro = line
            m = re.match(r"^\s*\d+\. \*\*(CHAR_[A-Za-z0-9_]+)\*\*(.*?)· aspect ratio \*\*(\d+:\d+)\*\*\s*$", line)
            if m:
                sid, desc, aspect = m.group(1), m.group(2).strip(), m.group(3)
                j = i + 1
                while not lines[j].strip():
                    j += 1
                pm = re.match(r"^\s*> (.+)$", lines[j])
                if not pm:
                    raise BibleError(f"01 line {i + 1}: {sid} has no > prompt line")
                if re.match(r"^\s*>", lines[j + 1]):
                    raise BibleError(f"01 line {i + 1}: {sid} prompt spans more than one line")
                ff = "first frame" in desc.lower() or "first frame" in intro.lower()
                stills.append({"line": i, "id": sid, "aspect": aspect, "prompt": pm.group(1),
                               "kind": "first_frame" if ff else "character",
                               "desiccation": sub.startswith("#### DESICCATION")})
        if not stills:
            continue
        for s in stills:
            after = [n for (ln, n) in still_negs if ln > s["line"]]
            before = [n for (ln, n) in still_negs if ln < s["line"]]
            if after or before:
                neg = after[0] if after else before[-1]
            else:
                neg = common + (", " + char_neg if char_neg else "")
            if s["desiccation"]:
                if not desic_neg:
                    raise BibleError(f"{s['id']}: desiccation still with no desiccation negative")
                neg = neg + ", " + desic_neg
            s["negative"] = neg
        for ln, n in still_negs:
            if char_neg and n != common + ", " + char_neg:
                notes.append(f"01 {b['token']}: the *Still negative* line is not the common still negative + the "
                             f"character negative")

        source = f"01_characters.md §{b['section']} {b['token']}"
        front = next((s for s in stills if s["id"].endswith("_front")), None)
        for s in stills:
            sid = s["id"]
            token = token_of(sid, tokens)
            method = f"edit_from:{EDIT_PARENTS[sid]}" if sid in EDIT_PARENTS else "text"
            prio = 1 if (token in PRINCIPALS and re.fullmatch(re.escape(token) + r"_A0?_(front|34|profile|full)",
                                                               sid)) else 2
            out.append(record(sid, s["kind"], token, s["aspect"], s["prompt"], s["negative"], method, prio, source))
            if s is front and expressions:
                key = "neutral relaxed expression"
                if s["prompt"].count(key) != 1:
                    raise BibleError(f"{sid}: front prompt does not contain '{key}' exactly once")
                for k, expr in enumerate(expressions, 1):
                    eid = f"{sid}_expr{k}"
                    em = f"edit_from:{sid}" if token.startswith(DERIVED_FACE_TOKENS) else "text"
                    out.append(record(eid, "character", token, s["aspect"], s["prompt"].replace(key, expr),
                                      s["negative"], em, prio, source + f" (sheet expression {k})"))
        if expressions and front is None:
            notes.append(f"01 {b['token']}: sheet expressions but no front still to rerun")
    return out


# ---------------------------------------------------------------- 02 units and 04 props

def parse_refs(fname, prefix, kind, negative, tokens, priority_of):
    lines = read(BIBLE / fname).split("\n")
    out, token, section, main_section = [], None, None, None
    seen = {}
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,3}) (?:(\d+(?:\.\d+)?[a-z]?)\.? )?(%s_[A-Z0-9_]+)?" % prefix, line)
        if m and line.startswith("#"):
            level, num, tok = m.group(1), m.group(2), m.group(3)
            if level == "##":
                main_section = num
            if tok:
                token, section = tok, (num or main_section)
            elif level == "##":
                token = None
            continue
        m = re.match(r"^\*\*REF(?: ([AB]))? — (.*?):\*\*\s*(.*)$", line)
        if not m:
            continue
        if token is None:
            raise BibleError(f"{fname} line {i + 1}: REF outside a token section")
        letter, label, rest = m.groups()
        aspect = re.findall(r"\d+:\d+", label)
        if not aspect:
            raise BibleError(f"{fname} line {i + 1}: REF with no aspect ratio")
        aspect = aspect[0]
        if rest.strip():
            prompt = rest.strip()
        else:
            prompt, _ = one_line_after(lines, i, f"{fname} line {i + 1}")
        sid = f"{token}_REF_{letter}" if letter else f"{token}_REF"
        if sid in seen:
            raise BibleError(f"{fname}: duplicate still id {sid}")
        seen[sid] = 1
        tok = token_of(sid, tokens)
        out.append(record(sid, kind, tok, aspect, prompt, negative, "text", priority_of(tok),
                          f"{fname} §{section} {token}"))
    return out


# ---------------------------------------------------------------- 03 locations

def seq_1_3_locations(notes):
    """LOC tokens of every Seq 1-3 scene: the 03 §1.1 heading map rows for Seq 1-3, checked against the headings
    actually written in seq_01..03.fountain."""
    text = read(BIBLE / "03_locations.md")
    rows = []
    for line in text.split("\n"):
        m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
        if m and int(m.group(1)) in PRIORITY_SEQS:
            rows.append((int(m.group(1)), m.group(2), m.group(3)))
    locs = set()
    for _, heading, tok in rows:
        locs.update(re.findall(r"\bLOC_[A-Z0-9_]+\b", tok))
    for n in sorted(PRIORITY_SEQS):
        for line in read(SCREENPLAY / "sequences" / f"seq_{n:02d}.fountain").split("\n"):
            if re.match(r"^(INT\.|EXT\.|INT/EXT|I/E|\.[A-Z])", line):
                place = line.lstrip(".").split(" - ")[0].strip()
                if not any(place in h for s, h, _ in rows if s == n):
                    notes.append(f"seq_{n:02d}.fountain heading not in the 03 §1.1 map: {line}")
    return locs


def cap(phrase):
    phrase = phrase.strip()
    return phrase[0].upper() + phrase[1:] + ("" if phrase.endswith(".") else ".")


def parse_locations(neg_base, neg_plate, prio_locs, notes, skipped, conflicts):
    lines = read(BIBLE / "03_locations.md").split("\n")
    entries, cur, mode = [], None, None
    for i, line in enumerate(lines):
        m = re.match(r"^## (\d+)\. (LOC_[A-Z0-9_]+) ", line)
        if m:
            cur = {"n": m.group(1), "token": m.group(2), "variants": [], "plate": None}
            entries.append(cur)
            mode = None
            continue
        if cur is None:
            continue
        if line.startswith("**Lighting variants"):
            mode = "var"
            continue
        if mode == "var":
            if line.startswith(("**", "---", "#")):
                mode = None
            else:
                vm = re.match(r"^- `(LOC_[A-Z0-9_]+)`[^`]*`([^`]+)`", line)
                if vm:
                    cur["variants"].append((vm.group(1), vm.group(2)))
        pm = re.match(r"^\*\*PLATE — (.*?):\*\*\s*$", line)
        if pm:
            aspect = re.findall(r"\d+:\d+", pm.group(1))[0]
            prompt, _ = one_line_after(lines, i, f"03 line {i + 1}")
            cur["plate"] = (aspect, prompt)

    out = []
    for e in entries:
        tok, (aspect, plate) = e["token"], e["plate"]
        if not e["variants"]:
            raise BibleError(f"03 {tok}: no lighting variants")
        suffixes = [v[len(tok) + 1:] for v, _ in e["variants"]]
        for v, _ in e["variants"]:
            if not v.startswith(tok + "_"):
                raise BibleError(f"03 {tok}: variant {v} does not extend the token")
        neg = neg_base
        if tok not in NO_NEG_PLATE and re.search(r"\bno (people|boats|vehicles)\b", plate, re.I):
            neg = neg_base + ", " + neg_plate
        source = f"03_locations.md entry {e['n']} {tok}"
        prio = 1 if tok in prio_locs else 2
        if len(e["variants"]) == 1:
            base, span, skip = suffixes[0], None, {}
        else:
            if tok not in PLATE_RULES:
                raise BibleError(f"03 {tok}: {len(e['variants'])} variants but no PLATE_RULES entry")
            base, span, skip = PLATE_RULES[tok]
            if base not in suffixes:
                raise BibleError(f"03 {tok}: PLATE_RULES base {base} is not a variant")
            if span is None:
                skip = {s: "ambiguous: " + skip for s in suffixes if s != base}
            elif plate.count(span) != 1:
                raise BibleError(f"03 {tok}: lighting sentence not found exactly once in the plate")
        for (vtok, phrase), suf in zip(e["variants"], suffixes):
            if suf == base:
                out.append(record(f"{vtok}_plate", "location", tok, aspect, plate, neg, "text", prio,
                                  source + " PLATE"))
            elif suf in skip:
                skipped.append(f"{vtok}_plate ({skip[suf]})")
            else:
                new = cap(phrase)
                prompt = plate.replace(span, new, 1)
                rest = plate.replace(span, "", 1)
                clash = sorted({w.lower() for w in TIME_WORDS.findall(rest)} -
                               {w.lower() for w in TIME_WORDS.findall(phrase)})
                if clash:
                    conflicts.append(f"{vtok}_plate keeps: {', '.join(clash)}")
                out.append(record(f"{vtok}_plate", "location", tok, aspect, prompt, neg, "text", prio,
                                  source + f" PLATE, lighting sentence -> {vtok}"))
    return out, entries


# ---------------------------------------------------------------- build + validate

def build():
    notes, skipped, conflicts = [], [], []
    tokens = index_tokens()
    suffix, neg_base, neg_plate = style_texts()
    common = re.search(r"\*\*Common still negative\*\* \(append to every still\): \*(.+?)\*, plus",
                       read(BIBLE / "01_characters.md")).group(1)
    prio_locs = seq_1_3_locations(notes)
    manifest = []
    manifest += parse_characters(tokens, notes)
    manifest += parse_refs("02_units_and_machines.md", "UNIT", "unit", common, tokens,
                           lambda t: 1 if t in PRIORITY_UNITS else 2)
    locs, loc_entries = parse_locations(neg_base, neg_plate, prio_locs, notes, skipped, conflicts)
    manifest += locs
    manifest += parse_refs("04_props.md", "PROP", "prop", common, tokens, lambda t: 2)
    return manifest, dict(notes=notes, skipped=skipped, conflicts=conflicts, tokens=tokens, suffix=suffix,
                          prio_locs=prio_locs, loc_entries=loc_entries)


def spot_check(e, sources):
    """Byte-for-byte check of one entry against its source file. Returns an error string or None."""
    fname = e["source"].split(" ")[0]
    src = sources[fname]
    if e["prompt"] in src:
        return None
    m = re.search(r"_expr(\d)$", e["id"])
    if m:
        front = e["id"][: m.start()]
        exprs = re.findall(r'^\*\*Sheet expressions\*\* \(use the front-still prompt, replacing "neutral relaxed '
                           r'expression"\): (.+)$', src, re.M)
        for line in exprs:
            for p in re.split(r" · (?=\(\d\) )", line):
                p = re.sub(r"^\(\d\) ", "", p)
                if p in e["prompt"] and e["prompt"].replace(p, "neutral relaxed expression", 1) in src:
                    return None
        return f"{e['id']}: expression still does not map back to a front prompt ({front})"
    if e["kind"] == "location":
        # The prompt must be a written plate paragraph with one span replaced by a written variant phrase.
        paras = re.findall(r"^\*\*PLATE — .*?:\*\*\s*\n(.+)$", src, re.M)
        phrases = re.findall(r"^- `LOC_[A-Z0-9_]+`[^`]*`([^`]+)`", src, re.M)
        for ph in phrases:
            new = cap(ph)
            if e["prompt"].count(new) != 1:
                continue
            head, tail = e["prompt"].split(new)
            for para in paras:
                if para.startswith(head) and para.endswith(tail) and len(head) + len(tail) < len(para):
                    return None
        return f"{e['id']}: plate is not a written plate with one variant sentence swapped in"
    return f"{e['id']}: prompt not found verbatim in {fname}"


def validate(manifest, info, seed):
    errors, report = [], []
    ids = [e["id"] for e in manifest]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if dup:
        errors.append(f"duplicate ids: {dup}")
    for e in manifest:
        if not e["prompt"].strip():
            errors.append(f"{e['id']}: empty prompt")
        if not e["negative"].strip():
            errors.append(f"{e['id']}: empty negative")
        if info["suffix"] in e["prompt"] or "24 frames per second" in e["prompt"]:
            errors.append(f"{e['id']}: contains the video style suffix")
        if e["method"].startswith("edit_from:") and e["method"][10:] not in ids:
            errors.append(f"{e['id']}: parent {e['method'][10:]} is not in the manifest")
        if e["width"] % 16 or e["height"] % 16:
            errors.append(f"{e['id']}: size not divisible by 16")

    sources = {f: read(BIBLE / f) for f in ("01_characters.md", "02_units_and_machines.md", "03_locations.md",
                                              "04_props.md")}
    sample = random.Random(seed).sample(manifest, 10)
    for e in sample:
        err = spot_check(e, sources)
        report.append(f"  spot-check {'FAIL' if err else 'ok  '} {e['id']}")
        if err:
            errors.append(err)

    # What each file's text implies.
    t1 = sources["01_characters.md"]
    implied = {
        "01_characters.md": len(re.findall(r"· aspect ratio \*\*\d+:\d+\*\*", t1)) +
        2 * len(re.findall(r"^\*\*Sheet expressions\*\*", t1, re.M)),
        "02_units_and_machines.md": len(re.findall(r"^\*\*REF\b", sources["02_units_and_machines.md"], re.M)),
        "03_locations.md": len(re.findall(r"^- `LOC_[A-Z0-9_]+`", sources["03_locations.md"], re.M)),
        "04_props.md": len(re.findall(r"^\*\*REF\b", sources["04_props.md"], re.M)),
    }
    for f, n in implied.items():
        got = sum(1 for e in manifest if e["source"].startswith(f))
        extra = f" ({len(info['skipped'])} variant plates not emitted, listed below)" if f.startswith("03") else ""
        report.append(f"  {f}: implied {n}, emitted {got}{' OK' if n == got else ' MISMATCH'}{extra}")
        if f.startswith("03"):
            if n - len(info["skipped"]) != got:
                errors.append(f"{f}: implied {n} - skipped {len(info['skipped'])} != emitted {got}")
        elif n != got:
            errors.append(f"{f}: implied {n} stills, emitted {got}")
    plates = len(re.findall(r"^\*\*PLATE — ", sources["03_locations.md"], re.M))
    report.append(f"  03 plate paragraphs: {plates}; entries: {len(info['loc_entries'])}")

    # Index tokens with a look-lock but no still.
    have = {e["token"] for e in manifest}
    lockless = [t for t in info["tokens"] if t.endswith("_VOICE")]
    missing = [t for t in info["tokens"] if t not in have and t not in lockless]
    report.append(f"  00_INDEX tokens with no still or plate: {missing or 'none'}")

    # Still ids named anywhere in the bible (or the shot files) that have no prompt here.
    pat = re.compile(r"\b((?:CHAR|UNIT|LOC|PROP)_[A-Z0-9_]*?(?:_(?:A0|A|A1|B|B1|B2|B3|C|C3)_[a-z0-9]+|_REF(?:_[AB])?"
                     r"|_plate|_still|_MASTER|_expr\d))\b")
    idset = set(ids)
    named = {}
    for path in sorted(BIBLE.glob("*.md")) + sorted((FILM / "shots").glob("*.jsonl")):
        for m in pat.finditer(read(path)):
            sid = m.group(1)
            if sid not in idset:
                named.setdefault(sid, set()).add(path.name)
    report.append("  still ids named in the bible/shots with no prompt here: " +
                  ("; ".join(f"{k} ({', '.join(sorted(v))})" for k, v in sorted(named.items())) or "none"))
    return errors, report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(HERE / "stills_manifest.jsonl"))
    ap.add_argument("--seed", type=int, default=1323, help="seed for the 10-entry spot-check sample")
    a = ap.parse_args()
    try:
        manifest, info = build()
    except BibleError as exc:
        sys.exit(f"extract_stills: {exc}")
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        for e in manifest:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    errors, report = validate(manifest, info, a.seed)
    by_kind, by_prio = {}, {}
    for e in manifest:
        by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
        by_prio[e["priority"]] = by_prio.get(e["priority"], 0) + 1
    print(f"wrote {len(manifest)} entries to {a.out}")
    print("  by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(by_kind.items())))
    print("  by priority: " + ", ".join(f"{k}: {v}" for k, v in sorted(by_prio.items())))
    print("  edit_from: " + str(sum(1 for e in manifest if e["method"] != "text")))
    print("  Seq 1-3 locations (priority 1): " + ", ".join(sorted(info["prio_locs"])))
    print("\n".join(report))
    for title, items in (("notes", info["notes"]), ("variant plates not emitted", info["skipped"]),
                         ("variant plates whose kept text names another time of day", info["conflicts"])):
        if items:
            print(f"{title} ({len(items)}):\n    " + "\n    ".join(items))
    if errors:
        print("VALIDATION FAILED:\n    " + "\n    ".join(errors))
        sys.exit(1)
    print("validation passed")


if __name__ == "__main__":
    main()
