#!/usr/bin/env python3
"""List every spoken line in the shot files for voice recording or TTS, and flag the shots that need lip-sync.

  python export_dialogue.py ../../shots/seq_*_shots.jsonl [--out dialogue]

Writes <out>/dialogue.csv (one row per line: shot, speaker, language, direction, text, clip length, framing,
lip-sync yes/no, target audio file) and <out>/voices.csv (one row per speaker: lines, languages, first shot),
for casting the ~12 voices. Lip-sync is flagged for on-screen speakers in medium or closer framings
(file 05 §9.2); V.O., O.S. and unit voices never need it.
"""
import csv, json, re, glob, argparse, pathlib

HERE = pathlib.Path(__file__).parent
LINE = re.compile(r'([A-Z][A-Z0-9 .\'-]*?)\s*(?:\(([^)]*)\))?\s*:\s*"(.+?)"')
CLOSE = ("MS", "MCU", "CU", "ECU", "OTS", "medium", "close")


def language(direction):
    d = direction.lower()
    if "egyptian arabic" in d or "arabic" in d:
        return "ar-EG"
    if "middle egyptian" in d or "ancient" in d or "old egyptian" in d:
        return "egy (subtitled)"
    return "en"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", nargs="+")
    ap.add_argument("--out", default=str(HERE / "dialogue"))
    a = ap.parse_args()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    paths = sorted({p for pat in a.jsonl for p in glob.glob(pat)})
    rows, voices = [], {}
    for path in paths:
        for l in open(path, encoding="utf-8"):
            if not l.strip():
                continue
            s = json.loads(l)
            for n, (who, direction, text) in enumerate(LINE.findall(s.get("dialogue", "") or ""), 1):
                who, direction = who.strip(), (direction or "").strip()
                offscreen = any(t in f"{who} {direction}" for t in ("V.O.", "O.S.", "O.C.")) or who in ("SESHAT", "AMUN")
                speaker = re.sub(r"\s*(V\.O\.|O\.S\.|O\.C\.|CONT'D)", "", who).strip()
                lip = not offscreen and any(c in s.get("shot", "") for c in CLOSE)
                lang = language(direction)
                rows.append({"shot": s["id"], "n": n, "speaker": speaker, "language": lang, "direction": direction,
                             "text": text, "clip_s": s["duration_s"], "framing": s.get("shot", ""),
                             "lipsync": "yes" if lip else "no",
                             "audio_file": f"audio/dialogue/{s['id']}_{n:02d}_{speaker.replace(' ', '_')}.wav"})
                v = voices.setdefault(speaker, {"speaker": speaker, "lines": 0, "languages": set(), "first_shot": s["id"]})
                v["lines"] += 1; v["languages"].add(lang)
    with open(out / "dialogue.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["shot"]); w.writeheader(); w.writerows(rows)
    with open(out / "voices.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["speaker", "lines", "languages", "first_shot"]); w.writeheader()
        for v in sorted(voices.values(), key=lambda v: -v["lines"]):
            w.writerow({**v, "languages": " ".join(sorted(v["languages"]))})
    print(f"{len(rows)} lines from {len(paths)} files, {sum(r['lipsync'] == 'yes' for r in rows)} need lip-sync, "
          f"{len(voices)} speakers -> {out / 'dialogue.csv'}, {out / 'voices.csv'}")


if __name__ == "__main__":
    main()
