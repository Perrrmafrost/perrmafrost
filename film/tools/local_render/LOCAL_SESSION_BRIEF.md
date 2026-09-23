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
3. **Test clip.** Build a working image-to-video workflow, render one 5-second test at 848x480 (raise to 720p only if it fits and is fast enough). Report seconds-per-clip and an honest estimate for ~1,200 shots x 2 takes.
4. **Wire the batch renderer.** Export the workflow in API format to `film/tools/local_render/workflow_api.json`, write `config.json` from `config.example.json` with the real node IDs and the model's fps/frame rule, and dry-run `render_queue.py --only <one id>`.
5. **Reference stills first (consistency).** From the production bible, generate the core stills for the principals (Tut, Nour, Adaeze, Tomas, Tarek, Fathi, Rami, Hale, Layla, the forecast Akhenaten), the robot units (shabti, the Reis, jackal, fly, nurse, inch-worm) and the Seq 1-3 locations. Save them in `film/tools/local_render/stills/` named exactly by token/still id (e.g. `CHAR_NOUR_A_front.png`). Show the user a contact sheet and let them approve or ask for regenerations before rendering shots.
6. **Render Sequence 1**, assemble it (`assemble_film.py ... --out seq01.mp4`), show the user, adjust settings if needed, then continue sequence by sequence (`git pull` for new shot files). Re-render bad takes (faces drifting, hands, text) with `--takes`, and record approvals in `renders/status.json`.
7. **Sound (after picture).** Offer local TTS for dialogue, lip-sync for speaking close-ups, and an editor pass for music/effects, per `05_style_and_prompt_grammar.md` §9.

## Starting point for step 2 (cloud research, 2026-09-23)
File sizes come from Hugging Face listings and render times from community reports; none were tested on this PC. Re-check each page before downloading, and still ask before anything over ~5 GB.
- **Video, 12 GB card: Wan 2.2 I2V-A14B GGUF + lightx2v 4-step LoRAs, about 27.6 GB, Apache-2.0.**
  - `QuantStack/Wan2.2-I2V-A14B-GGUF`: `HighNoise/…-HighNoise-Q4_K_M.gguf` and `LowNoise/…-LowNoise-Q4_K_M.gguf`, 9.65 GB each (Q4_K_S is 8.75 GB).
  - From `Comfy-Org/Wan_2.2_ComfyUI_Repackaged`: `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (6.74 GB) and `wan_2.1_vae.safetensors` (0.25 GB).
  - From `lightx2v/Wan2.2-Distill-Loras`: the I2V high- and low-noise 4-step LoRAs, about 0.64 GB each.
  - Custom nodes: ComfyUI-GGUF, plus VideoHelperSuite, KJNodes and Frame-Interpolation.
  - Output is 16 fps, frames 4n+1, max 81 (5 s); this is what `config.example.json` expects. Reported speed on a 3060 12 GB is about 5–8 min per 5 s clip.
  - With 32 GB RAM, set a large Windows pagefile (about 64 GB, on the storage drive) or drop to Q4_K_S.
- **Video, 8 GB card: Wan 2.2 TI2V-5B** (QuantStack Q8_0 GGUF, 5.4 GB, plus `wan2.2_vae`). Native 24 fps, lower quality.
- **Alternate video model: LTX-2.3 GGUF.** It is 5–14x faster but holds faces from the start image less well, and its license is free only under $10M revenue.
  - Skip LTX-2.5: it needs 16 GB of VRAM.
  - Skip HunyuanVideo 1.5: its license excludes the EU, UK and South Korea.
- **Stills: Z-Image Turbo, about 15 GB.**
  - `jayn7/Z-Image-Turbo-GGUF` `z_image_turbo-Q8_0.gguf` (6.7 GB), plus `qwen_3_4b.safetensors` (8.04 GB) and `ae.safetensors` from `Comfy-Org/z_image_turbo`.
- **Same face across stills (turnarounds, costume states): Qwen-Image-Edit-2511, about 22.4 GB.**
  - `unsloth/Qwen-Image-Edit-2511-GGUF` Q4_0 (11.9 GB), `qwen_2.5_vl_7b_fp8_scaled` (9.38 GB), `qwen_image_vae`, and the Lightning 4-step LoRA.
  - It takes up to 3 reference images. Both still models are Apache-2.0.
- **24 fps:** add RIFE (ComfyUI-Frame-Interpolation) in the workflow to take 16 fps to 48 fps. `assemble_film.py` then keeps every other frame.
  - Leave `model_fps` at 16, because it sets how many frames are generated.
  - For 6–8 s shots, the 81-frame cap gives a 5 s clip, and assembly holds its last frame so the cut stays in sync. For a better result, test 97–113 frames or extend from the last frame.
- **Upscaling:**
  - Bulk: the NVIDIA RTX Video Super Resolution node (`Comfy-Org/Nvidia_RTX_Nodes_ComfyUI`, no download) or RealESRGAN_x4plus.
  - Hero close-ups only: SeedVR2 3B Q4_K_M (about 2.5 GB), which is slow on a 3060.
- **Avoid for a released film (non-commercial or research-only licenses):** FLUX.1 dev, Krea, Kontext, FLUX.2 klein 9B, 4x-UltraSharp, and Qwen-Image-2.1.
- **Time budget:** 1,200 shots × 2 takes × 5–8 min is about 200–320 GPU-hours (8–13 days non-stop), before upscaling and retakes. Confirm it with the step 3 timing.

## Rules
- Follow the production bible's safety staging: PG-13, no gore, remains shown with dignity, robots never touch a child, no real people or brand logos.
- Never type look descriptions by hand; the JSONL prompts already contain the fixed wording.
- Keep the user's machine healthy: don't delete their files, keep renders inside the `output_dir` set in `config.json` (the storage folder on the roomiest drive, or `film/tools/local_render/renders/` by default), and warn before anything that uses a lot of disk.
- Commit nothing large (videos, model weights) to git.
