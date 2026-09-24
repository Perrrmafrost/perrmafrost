# Shot lists — HERE AM I

One shot list per screenplay sequence. The `.md` file is the human-readable master; the `.jsonl` file is generated from it by `../tools/shots_md2jsonl.py` (tokens expanded, one shot per line, 1920x1080 / 16:9 / 24 fps) and is what `../tools/local_render/render_queue.py` reads.

Edit the `.md`, then regenerate: `python3 film/tools/shots_md2jsonl.py film/shots/seq_NN_shots.md` (must report 0 errors).

| Seq | Title | Shots | Min | COMP | VFX | Files |
|---|---|---|---|---|---|---|
| 1 | THE HEART | 103 | 9.5 | 32 | 4 | [md](seq_01_shots.md) · [jsonl](seq_01_shots.jsonl) |
| 2 | THE READINGS | 163 | 14.3 | 43 | 1 | [md](seq_02_shots.md) · [jsonl](seq_02_shots.jsonl) |
| 3 | THE GLASS | 123 | 10.7 | 30 | 11 | [md](seq_03_shots.md) · [jsonl](seq_03_shots.jsonl) |
| 4 | GEM NIGHT | 123 | 10.6 | 41 | 19 | [md](seq_04_shots.md) · [jsonl](seq_04_shots.jsonl) |
| 5 | CAIRO DARK | 84 | 7.2 | 23 | 23 | [md](seq_05_shots.md) · [jsonl](seq_05_shots.jsonl) |
| 6 | THE RIVER | 132 | 12.8 | 24 | 30 | [md](seq_06_shots.md) · [jsonl](seq_06_shots.jsonl) |
| 7 | KARNAK | 164 | 15.0 | 35 | 32 | [md](seq_07_shots.md) · [jsonl](seq_07_shots.jsonl) |
| 8 | THE WALL | 166 | 13.9 | 34 | 14 | [md](seq_08_shots.md) · [jsonl](seq_08_shots.jsonl) |
| 9 | THE FATHER | 244 | 22.6 | 73 | 58 | [md](seq_09_shots.md) · [jsonl](seq_09_shots.jsonl) |
| 10 | THE LAND OF SOKAR | 136 | 11.9 | 40 | 20 | [md](seq_10_shots.md) · [jsonl](seq_10_shots.jsonl) |
| 11 | THE HORIZON | 163 | 14.7 | 82 | 39 | [md](seq_11_shots.md) · [jsonl](seq_11_shots.jsonl) |
| 12 | THE WEIGHING | 180 | 15.5 | 74 | 21 | [md](seq_12_shots.md) · [jsonl](seq_12_shots.jsonl) |
| **All** | | **1781** | **158.7** | | | |

Total cut before trims is about 2 h 39 min against a ~129-page script (~2 h 10 min). Some sequence headers list cut candidates; Seq 9 (the longest) is the best place to trim.

Flags: **COMP** = readable text, glyphs, subtitles, screens or glow added in compositing; **VFX-EXTEND** = crowd/set extension; **VFX-ASSIST** = water, fire, collapse; **EXTEND:<id>** = continue from the last frame of that shot.

Open questions for the lead are in [OPEN_ITEMS.md](OPEN_ITEMS.md).
