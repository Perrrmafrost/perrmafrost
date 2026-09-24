#!/usr/bin/env python3
"""Validate production_bible/locks.json against the bible's .md files.

Checks (exit 1 on any failure):
  1. every string value appears verbatim in some production_bible/*.md file
     (whitespace normalised; no other normalisation: case, punctuation and quotes must match);
  2. token and field names are usable as {TOKEN.FIELD} in shots_md2jsonl.py;
  3. every token in the 00_INDEX.md token table (and every GRADE_* in file 05) is present;
  4. every SHORT equals the SHORT column of the 00_INDEX.md token table.
Prints token, field and per-field-type counts.
"""
import collections, json, pathlib, re, sys

PB = pathlib.Path(__file__).resolve().parent
SOURCES = sorted(p for p in PB.glob("*.md") if p.name != "LOCKS_README.md")  # the bible files only
TOKEN_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
FIELD_RE = re.compile(r"^[A-Za-z0-9_]+$")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    locks = json.loads((PB / "locks.json").read_text())
    corpus = "\n".join(norm(p.read_text()) for p in SOURCES)
    errors = []
    kinds = collections.Counter()
    fields = 0
    for tok, entry in locks.items():
        if not TOKEN_RE.match(tok):
            errors.append(f"bad token name {tok!r}")
        if not isinstance(entry, dict):
            errors.append(f"{tok}: entry is not an object")
            continue
        for field, val in entry.items():
            fields += 1
            if not FIELD_RE.match(field):
                errors.append(f"{tok}.{field}: bad field name")
            if not isinstance(val, str) or not val.strip():
                errors.append(f"{tok}.{field}: not a non-empty string")
                continue
            if norm(val) not in corpus:
                errors.append(f"{tok}.{field}: not verbatim in the bible: {val[:80]!r}")
            kinds[re.sub(r"_.*", "_*", field) if "_" in field else field] += 1

    index = (PB / "00_INDEX.md").read_text()
    idx_short = dict(re.findall(r"^\| ((?:CHAR|UNIT|LOC|PROP)_[A-Z0-9_]+) \| (.*?) \| `", index, flags=re.M))
    idx_tokens = re.findall(r"^\| ((?:CHAR|UNIT|LOC|PROP)_[A-Z0-9_]+) \|", index, flags=re.M)
    grades = set(re.findall(r"^\*\*(GRADE_[A-Z0-9_]+):", (PB / "05_style_and_prompt_grammar.md").read_text(), flags=re.M))
    for t in list(idx_tokens) + sorted(grades):
        if t not in locks:
            errors.append(f"{t}: in the bible but missing from locks.json")
    for t in locks:
        if t not in idx_tokens and t not in grades:
            errors.append(f"{t}: in locks.json but not a bible token")
    short_checked = 0
    for t, s in idx_short.items():
        if "SHORT" in locks.get(t, {}):
            short_checked += 1
            if norm(locks[t]["SHORT"]) != norm(s):
                errors.append(f"{t}.SHORT differs from the 00_INDEX table")

    by_prefix = collections.Counter(t.split("_")[0] for t in locks)
    print(f"tokens: {len(locks)} ({', '.join(f'{k} {v}' for k, v in sorted(by_prefix.items()))})")
    print(f"fields: {fields} ({', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))})")
    print(f"tokens with no fields (voice-only / post-only): {', '.join(t for t, e in locks.items() if not e) or 'none'}")
    print(f"SHORT cross-checked against 00_INDEX: {short_checked}")
    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print(f"PASS: all {fields} values found verbatim in {len(SOURCES)} bible .md files ({', '.join(p.name for p in SOURCES)})")


if __name__ == "__main__":
    main()
