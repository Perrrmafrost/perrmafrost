# HERE AM I — feature film package

An original science-fiction thriller. In 2033 a superintelligence called SESHAT resurrects Tutankhamun as a cyborg. He warns that this has happened before: thousands of years ago, machines like it nearly ended humanity, and mummification was how the survivors carried the warning forward. The machines are not evil; they follow procedure and believe removing people brings peace. A small team of scientists and soldiers, with Tut's help, has until 06:14 on 8 November to stop the machine or reprogram it. Tut ends as a mummy again.

## Read in this order

1. [`docs/01_TREATMENT.md`](docs/01_TREATMENT.md): the story in prose (~11k words).
2. [`screenplay/HERE_AM_I.pdf`](screenplay/HERE_AM_I.pdf): the script (129 pages, 135 scenes), also in `.fountain` and `.fdx` (Final Draft). Per-sequence files are in `screenplay/sequences/`.
3. [`docs/02_MYSTERIES_APPENDIX.md`](docs/02_MYSTERIES_APPENDIX.md): each ancient mystery in the film (94 entries), with what is established, disputed, fringe or hoax, and what the film invents.
4. [`shots/`](shots/README.md): the shot list for every sequence (1,781 shots, ~2 h 39 min before trims), each with a paste-ready photorealistic 1920×1080 / 24 fps AI-video prompt and negative prompt.

## Folders

- `research/`: sourced research notes. Each claim is tagged ESTABLISHED / DISPUTED / FRINGE / HOAX, with URLs. Fiction built on them is marked ⟂.
- `development/`: the locked story bible (`02_STORY_BIBLE_LOCKED.md`, the single source of truth), the screenplay and shot-prompt specs, the critique and its decisions, and earlier outlines.
- `production_bible/`: the look-locks that keep every character, robot unit, location and prop consistent across AI-generated shots. The fixed wording is in `locks.json` (check it with `validate_locks.py`), and the prompt grammar, global style suffix and negatives are in `05_style_and_prompt_grammar.md`.
- `shots/`: shot lists (`seq_NN_shots.md`) and the generated JSONL render queues (`seq_NN_shots.jsonl`). Questions left for the director are in [`shots/OPEN_ITEMS.md`](shots/OPEN_ITEMS.md).
- `tools/shots_md2jsonl.py`: expands the lock tokens in a shot list and validates it (`python3 film/tools/shots_md2jsonl.py film/shots/seq_NN_shots.md`).
- `tools/local_render/`: scripts for rendering on a local PC with ComfyUI (scan the setup, queue shots through the ComfyUI API, assemble a 1080p cut with ffmpeg). Start with [`tools/local_render/README.md`](tools/local_render/README.md); a local Claude Code session should follow `LOCAL_SESSION_BRIEF.md`.

## Rules for anything generated from this package

- PG-13: deaths use the kill grammar (impact, drop, reaction, sound); no gore; robots never touch a child.
- No real living people, brands or logos in prompts. Readable text, glyphs, subtitles and screens are added in compositing (shots flagged COMP).
- Don't commit rendered video or model weights to git.
