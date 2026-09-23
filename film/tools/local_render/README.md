# Local render kit — HERE AM I on your own GPU

Everything here runs **on your computer**. It talks only to ComfyUI on `127.0.0.1` and sends nothing anywhere.

## 0. Scan your setup (read-only)
```
python scan_setup.py            # or: python scan_setup.py "D:\path\to\ComfyUI"
```
Paste the printed report back into the Claude session so the model choice and settings can be tuned to your machine.

## 1. Realistic plan for an RTX 3060 + 32 GB RAM
- The 3060 usually has **12 GB VRAM** (some are 8 GB — the scan shows which). Native 1080p video with the largest open models will not fit comfortably.
- **Render small, deliver at 1080p:** generate at 832×480 (or 1280×720 if it fits), then `assemble_film.py` scales to 1920×1080. An AI upscaler pass in ComfyUI before assembly gives a sharper result.
- **Pick a model that fits 12 GB:** a small or quantized (GGUF) open video model with an image-to-video mode. Test one 5-second clip first and note the time; that number × ~1,200 shots × takes = your render budget. Expect days to weeks of GPU time for the full film on this card — start with one sequence.
- **Consistency comes from stills:** generate the reference stills from `production_bible/` first (characters, units, locations), approve them, save them in `stills/` named by token (e.g. `CHAR_NOUR_A_front.png`), and use an image-to-video workflow so every shot starts from an approved face.

## 2. Wire your workflow
1. In ComfyUI, get one clip rendering well by hand.
2. `Workflow → Export (API)` → save as `workflow_api.json` here.
3. `copy config.example.json config.json`, open `workflow_api.json`, and set each `"nodes"` entry to `<node id>.<input name>` (prompt text, negative, seed, width, height, length/frames, filename prefix, and start image for image-to-video). Set `model_fps`/`frame_rule`/`max_frames` for your model.

## 3. Render
```
python render_queue.py ../../shots/seq_01_shots.jsonl --takes 2
```
Resumable: re-run the same command after a crash or reboot. Results: `renders/<shot id>/take_N.*`, log in `renders/status.json`. To pick a take, set `"approved": N` for that shot in `status.json`.

## 4. Assemble
```
python assemble_film.py ../../shots/seq_01_shots.jsonl --out seq01.mp4
```
Missing shots become black slates of the right length, so you can watch a sequence while it is still rendering.

## 5. Sound (separate pass)
Dialogue: record or generate voices, then lip-sync the speaking shots (production bible 05 §9). Music, effects and the final mix go in an editor (e.g. DaVinci Resolve) over the assembled picture.
