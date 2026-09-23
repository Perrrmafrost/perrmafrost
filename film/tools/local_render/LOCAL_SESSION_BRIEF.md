# Brief for the local Claude Code session — render HERE AM I on this PC

You are running on the user's own Windows/Linux PC (RTX 3060, 32 GB RAM, ComfyUI already installed somewhere).
The user wants you to do everything end to end. They approve installs and downloads when asked; otherwise work autonomously and keep them posted in short updates.

## What already exists (in this repo, branch `claude/ancient-ai-resurrection-film-p0oyqy`)
- `film/screenplay/HERE_AM_I.pdf` — the 129-page screenplay (12 sequences, 135 scenes).
- `film/production_bible/` — fixed-wording look-locks and **reference-still prompts** for every character, robot unit, location and prop (`01_characters.md`, `02_units_and_machines.md`, `03_locations.md`, `04_props.md`), the style guide and prompt grammar (`05_style_and_prompt_grammar.md`), and `locks.json`.
- `film/shots/seq_NN_shots.jsonl` — per-shot, paste-ready video prompts (id, duration, prompt, negative, refs, flags). These arrive sequence by sequence from a cloud session; run `git pull` (or re-download) to get new ones.
- `film/tools/local_render/` — `scan_setup.py`, `render_queue.py` (ComfyUI API batch renderer, resumable), `assemble_film.py` (upscale to 1920x1080 @ 24 fps and join in shot order), `README.md`.

## Do this, in order
1. **Scan.** Run `python film/tools/local_render/scan_setup.py`. Confirm VRAM (3060 = 12 GB or 8 GB), free space on every drive, ComfyUI path, installed models and custom nodes. Report a 5-line summary to the user.
   **Storage:** put the renders, ComfyUI's output folder and all new model downloads on the fixed drive with the most free space (`storage_suggestion` in the scan), even if the project and ComfyUI are on C:. Tell the user the drive and its free space before creating folders there, then set it up as in `README.md` §0b (`output_dir` in `config.json`, `--output-directory`, `extra_model_paths.yaml`).
2. **Pick the model.** Choose the best current open video model that fits this GPU with **image-to-video** support (quantized/GGUF or small variants are fine; research what is current and well supported in ComfyUI). Also pick an image model for stills and, if it fits, a video upscaler. State your choice and the download sizes; **ask before downloading anything over ~5 GB**. Install required ComfyUI custom nodes via ComfyUI-Manager or git. Check there is enough disk (budget 300+ GB for renders).
3. **Test clip.** Build a working image-to-video workflow, render one 5-second test at ~832x480 (raise to 720p only if it fits and is fast enough). Report seconds-per-clip and an honest estimate for ~1,200 shots x 2 takes.
4. **Wire the batch renderer.** Export the workflow in API format to `film/tools/local_render/workflow_api.json`, write `config.json` from `config.example.json` with the real node IDs and the model's fps/frame rule, and dry-run `render_queue.py --only <one id>`.
5. **Reference stills first (consistency).** From the production bible, generate the core stills for the principals (Tut, Nour, Adaeze, Tomas, Tarek, Fathi, Rami, Hale, Layla, the forecast Akhenaten), the robot units (shabti, the Reis, jackal, fly, nurse, inch-worm) and the Seq 1-3 locations. Save them in `film/tools/local_render/stills/` named exactly by token/still id (e.g. `CHAR_NOUR_A_front.png`). Show the user a contact sheet and let them approve or ask for regenerations before rendering shots.
6. **Render Sequence 1**, assemble it (`assemble_film.py ... --out seq01.mp4`), show the user, adjust settings if needed, then continue sequence by sequence (`git pull` for new shot files). Re-render bad takes (faces drifting, hands, text) with `--takes`, and record approvals in `renders/status.json`.
7. **Sound (after picture).** Offer local TTS for dialogue, lip-sync for speaking close-ups, and an editor pass for music/effects, per `05_style_and_prompt_grammar.md` §9.

## Rules
- Follow the production bible's safety staging: PG-13, no gore, remains shown with dignity, robots never touch a child, no real people or brand logos.
- Never type look descriptions by hand; the JSONL prompts already contain the fixed wording.
- Keep the user's machine healthy: don't delete their files, keep renders inside the `output_dir` set in `config.json` (the storage folder on the roomiest drive, or `film/tools/local_render/renders/` by default), and warn before anything that uses a lot of disk.
- Commit nothing large (videos, model weights) to git.
