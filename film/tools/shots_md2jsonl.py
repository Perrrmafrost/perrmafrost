#!/usr/bin/env python3
"""Parse a shot-list markdown file into paste-ready JSONL, expanding fixed-wording tokens.

Usage: shots_md2jsonl.py shots/seq_NN_shots.md [--out shots/seq_NN_shots.jsonl]

Tokens (expanded verbatim, so every prompt carries the production bible's exact wording):
  {SUFFIX}          global style suffix (05 §1.1)           -- PROMPT must end with it
  {NEG}             global negative prompt (05 §2.1)        -- NEGATIVE must start with it
  {NEG_XXX}         negative add-on (05 §2.2)
  {TOKEN.FIELD}     any entry of production_bible/locks.json, e.g. {CHAR_NOUR.SHORT}, {LOC_KARNAK_HYPOSTYLE.LONG}

Shot block format (one per shot):
  ### 07.03.012 — Scene label — Shot title   (6 s)
  - **Shot:** ... · **Move:** ...
  - **In frame:** ...
  - **Action:** ...
  - **Dialogue:** ...            (optional; "—" if none)
  - **Sound:** ...
  - **PROMPT:** ...
  - **NEGATIVE:** ...
  - **Refs:** A, B, C
  - **Flags:** COMP, VFX-EXTEND, EXTEND:07.03.011   (optional)
  - **Comp:** ...                (optional; overlay text/graphics for COMP shots)
  - **Continuity:** ...
Exit code 1 on any validation error (all errors are printed).
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).parent
PB = HERE / "production_bible"


def load_fixed():
    style = (PB / "05_style_and_prompt_grammar.md").read_text()
    def quote_after(heading):
        i = style.index(heading)
        m = re.search(r"^> (.+)$", style[i:], flags=re.M)
        return m.group(1).strip()
    fixed = {"SUFFIX": quote_after("### 1.1"), "NEG": quote_after("### 2.1")}
    for tok, text in re.findall(r"^\| `(NEG_[A-Z0-9_]+)` \| [^|]+ \| ([^|]+) \|", style, flags=re.M):
        fixed[tok] = text.strip()
    locks_path = PB / "locks.json"
    locks = json.loads(locks_path.read_text()) if locks_path.exists() else {}
    return fixed, locks


TOKEN = re.compile(r"\{([A-Z][A-Z0-9_]*)(?:\.([A-Za-z0-9_]+))?\}")


def expand(text, fixed, locks, errors, where):
    def rep(m):
        tok, field = m.group(1), m.group(2)
        if field is None:
            if tok in fixed:
                return fixed[tok]
            errors.append(f"{where}: unknown token {{{tok}}}")
            return m.group(0)
        entry = locks.get(tok)
        if entry is None or field not in entry:
            errors.append(f"{where}: unknown lock {{{tok}.{field}}}")
            return m.group(0)
        return entry[field]
    return TOKEN.sub(rep, text)


HEAD = re.compile(r"^### (\d{2}\.\d{2}\.\d{3}) — (.+?) — (.+?)\s+\((\d+(?:\.\d+)?)\s*s\)\s*$")
FIELD = re.compile(r"^- \*\*([A-Za-z ]+):\*\*\s?(.*)$")
KEYS = {"shot": "shot", "in frame": "in_frame", "action": "action", "dialogue": "dialogue", "sound": "sound",
        "prompt": "prompt", "negative": "negative", "refs": "refs", "flags": "flags", "comp": "comp",
        "continuity": "continuity"}
REQUIRED = ["shot", "in_frame", "action", "sound", "prompt", "negative", "refs", "continuity"]


def parse(md_text):
    shots, cur, field = [], None, None
    for line in md_text.splitlines():
        h = HEAD.match(line)
        if h:
            cur = {"id": h.group(1), "scene": h.group(2).strip(), "title": h.group(3).strip(),
                   "duration_s": float(h.group(4))}
            shots.append(cur); field = None
            continue
        if cur is None:
            continue
        if line.startswith("### ") or line.startswith("## "):
            cur, field = None, None
            continue
        f = FIELD.match(line)
        if f and f.group(1).strip().lower() in KEYS:
            field = KEYS[f.group(1).strip().lower()]
            cur[field] = f.group(2).strip()
        elif field and line.strip() and not line.startswith("- **"):
            cur[field] += " " + line.strip()
    return shots


def main():
    src = pathlib.Path(sys.argv[1])
    out = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else src.with_suffix(".jsonl")
    fixed, locks = load_fixed()
    shots = parse(src.read_text())
    errors, seen = [], set()
    rows = []
    for s in shots:
        w = s["id"]
        if w in seen: errors.append(f"{w}: duplicate id")
        seen.add(w)
        for k in REQUIRED:
            if not s.get(k): errors.append(f"{w}: missing {k}")
        if not (2 <= s["duration_s"] <= 10): errors.append(f"{w}: duration {s['duration_s']} outside 2-10 s")
        shot, move = (s.get("shot", "").split("· **Move:**") + [""])[:2]
        prompt = expand(s.get("prompt", ""), fixed, locks, errors, w)
        negative = expand(s.get("negative", ""), fixed, locks, errors, w)
        if not prompt.rstrip().endswith(fixed["SUFFIX"]): errors.append(f"{w}: PROMPT does not end with {{SUFFIX}}")
        if not negative.startswith(fixed["NEG"]): errors.append(f"{w}: NEGATIVE does not start with {{NEG}}")
        if TOKEN.search(prompt) or TOKEN.search(negative): pass  # already reported
        flags = [x.strip() for x in s.get("flags", "").split(",") if x.strip() and x.strip() not in ("—", "-", "none")]
        rows.append({
            "id": w, "scene": s["scene"], "title": s["title"], "duration_s": s["duration_s"],
            "shot": shot.strip().rstrip("·").strip(), "move": move.strip(), "in_frame": s.get("in_frame", ""),
            "action": s.get("action", ""), "dialogue": s.get("dialogue", "—"), "sound": s.get("sound", ""),
            "prompt": prompt, "negative": negative,
            "refs": [x.strip() for x in s.get("refs", "").split(",") if x.strip()],
            "flags": flags, "comp": s.get("comp", ""), "continuity": s.get("continuity", ""),
            "resolution": "1920x1080", "aspect": "16:9", "fps": 24,
        })
    with out.open("w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    total = sum(r["duration_s"] for r in rows)
    print(f"{src.name}: {len(rows)} shots, {total/60:.1f} min, {len(errors)} errors -> {out.name}")
    for e in errors[:200]:
        print("  ERR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
