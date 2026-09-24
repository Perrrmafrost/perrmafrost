# HERE AM I — instructions for Claude Code sessions

This repo is the complete pre-production package for the feature film **HERE AM I** (see `film/README.md`).

## If the user says "make the movie" (or "render", "start rendering", "do everything")

You are expected to be running **locally on the user's PC** (RTX 3060, 32 GB RAM, ComfyUI installed), not in a cloud container.

1. Check where you are. If there is no NVIDIA GPU (`nvidia-smi` fails) you are in a cloud sandbox and cannot render: tell the user to open this folder in a **Local** Claude Code session (Claude Desktop app → Code → choose the Local environment and this folder) and stop.
2. Otherwise follow `film/tools/local_render/LOCAL_SESSION_BRIEF.md` step by step. It covers scanning the setup, choosing and downloading a model, a test clip, wiring the batch renderer, reference stills, rendering sequence by sequence, assembling the 1080p cut and sound.
3. The render queue is `film/shots/seq_01_shots.jsonl` … `seq_12_shots.jsonl` (1,781 shots, ~2 h 39 min). Start with Sequence 1.

## Rules

- Ask the user before any single download over ~5 GB and before anything that fills a lot of disk. Never delete the user's files.
- PG-13 staging per `film/production_bible/05_style_and_prompt_grammar.md`: no gore, robots never touch a child, no real people or brand logos.
- Don't hand-edit prompts in the JSONL; edit `film/shots/seq_NN_shots.md` and regenerate with `python film/tools/shots_md2jsonl.py film/shots/seq_NN_shots.md`.
- Never commit videos, stills or model weights to git (see `.gitignore`).
