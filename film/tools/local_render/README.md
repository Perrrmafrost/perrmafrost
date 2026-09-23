# Local render kit — HERE AM I on your own GPU

Everything here runs **on your computer**. It talks only to ComfyUI on `127.0.0.1` and sends nothing anywhere.

## 0. Scan your setup (read-only)
```
python scan_setup.py            # or: python scan_setup.py "D:\path\to\ComfyUI"
```
Paste the printed report back into the Claude session so the model choice and settings can be tuned to your machine.

## 0b. Put renders and models on the roomiest drive
The scan lists free space on every drive and names the fixed drive with the most room under `storage_suggestion` (e.g. `E:\HERE_AM_I`). It does not have to be the drive this project is on. Budget about 380 GB there (300 GB renders + 80 GB models).
1. **Renders:** in `config.json` set `"output_dir": "E:/HERE_AM_I/renders"`. `render_queue.py` and `assemble_film.py` both follow it, and assembly's temporary clips go there too.
2. **ComfyUI's own copies:** ComfyUI also keeps every clip in its `output` folder. Start it with `--output-directory E:/HERE_AM_I/comfy_output` (portable build: add the flag to the end of the line in `run_nvidia_gpu.bat`).
3. **Models:** keep the weights in `E:\HERE_AM_I\models\` and point ComfyUI at them with `extra_model_paths.yaml` in the ComfyUI folder (next to `main.py`; the ComfyUI Desktop app uses `%APPDATA%\ComfyUI\extra_models_config.yaml` instead):
   ```yaml
   hereami:
       base_path: E:/HERE_AM_I/models/
       is_default: true
       checkpoints: checkpoints/
       diffusion_models: |
           diffusion_models
           unet
       text_encoders: |
           text_encoders
           clip
       clip_vision: clip_vision/
       vae: vae/
       loras: loras/
       upscale_models: upscale_models/
   ```
   Restart ComfyUI afterwards. `is_default: true` lists these folders first, so new downloads normally land there; check where the first one went.

## 1. Realistic plan for an RTX 3060 + 32 GB RAM
- The 3060 usually has **12 GB VRAM** (some are 8 GB — the scan shows which). Native 1080p video with the largest open models will not fit comfortably.
- **Render small, deliver at 1080p:** generate at 848×480 (or 1280×720 if it fits), then `assemble_film.py` scales to 1920×1080. An AI upscaler pass in ComfyUI before assembly gives a sharper result.
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
Resumable: re-run the same command after a crash or reboot. Results: `renders/<shot id>/take_N.*`, log in `renders/status.json` (`renders` = your `output_dir`). To pick a take, set `"approved": N` for that shot in `status.json`.

## 4. Assemble
```
python assemble_film.py ../../shots/seq_01_shots.jsonl --out seq01.mp4
```
Missing shots become black slates of the right length, so you can watch a sequence while it is still rendering.

## 5. Sound (separate pass)
Dialogue: record or generate voices, then lip-sync the speaking shots (production bible 05 §9). Music, effects and the final mix go in an editor (e.g. DaVinci Resolve) over the assembled picture.
