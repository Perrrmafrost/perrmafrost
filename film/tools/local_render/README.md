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
- **Pick a model that fits 12 GB:** a small or quantized (GGUF) open video model with an image-to-video mode. Test one 5-second clip first and note the time; that number × 1,781 shots × takes = your render budget. Expect days to weeks of GPU time for the full film on this card — start with one sequence.
- **Consistency comes from stills:** generate the reference stills from `production_bible/` first (characters, units, locations), approve them, save them in `stills/` named by token (e.g. `CHAR_NOUR_A_front.png`), and use an image-to-video workflow so every shot starts from an approved face.

## 2. The workflows (shipped, validated against ComfyUI)
| File | Model | Used by |
|---|---|---|
| `workflow_api.json` | Wan 2.2 I2V-A14B GGUF Q4_K_M + lightx2v 4-step LoRAs (2 high-noise + 2 low-noise steps, cfg 1, shift 5), 848×480, 81 frames at 16 fps, RIFE ×3 → 48 fps, H.264 | `render_queue.py` |
| `workflow_stills_api.json` | Z-Image Turbo GGUF Q8_0, 8 steps, cfg 1 | `render_stills.py` |
| `workflow_edit_api.json` | Qwen-Image-Edit-2511 GGUF Q4_0 + Lightning 4-step, up to three reference images | `compose_first_frames.py`, derived stills |

`config.json` already holds their node IDs. The model file names in the workflows are the ones in the brief's model list; if you download a different quant, change the name in the loader node (or open the JSON in ComfyUI). Custom nodes needed: ComfyUI-GGUF, ComfyUI-VideoHelperSuite, ComfyUI-Frame-Interpolation (RIFE downloads its small checkpoint on first use).
At cfg 1 (the speed LoRAs), negative prompts have no effect; the positive prompts carry the style and safety wording. For a shot that keeps showing something the NEGATIVE forbids, re-take it, or run it without the LoRAs at cfg 3.5 and 20 steps (slower).

## 3. Stills → first frames → shots
```
python render_stills.py                                  # priority-1 stills (brief step 5), 4 candidates each
python render_stills.py --approve CHAR_NOUR_A_front=3 ...  # after looking at stills/contact_sheet.html
python compose_first_frames.py ../../shots/seq_01_shots.jsonl --takes 2
python compose_first_frames.py --approve 01.01.001=2 ...   # after looking at stills/first_frames.html
python render_queue.py ../../shots/seq_01_shots.jsonl --takes 2
```
- Still prompts come verbatim from `stills_manifest.jsonl` (rebuilt from the bible with `extract_stills.py`). Stills the bible derives from a parent (child Tut, the 1336 king) wait until the parent is approved.
- A first frame is the location plate plus up to two subject stills from the shot's `Refs:`, composed by the edit model (file 05 §12 step 4). `--auto` approves candidate 1 for unattended runs.
- `render_queue.py` starts each shot from its approved first frame; an `EXTEND:<id>` shot starts from the last frame of its parent's take. Image-to-video gets the shot's `motion_prompt` (05 §5.5).
- All three are resumable: re-run the same command after a crash or reboot. Results: `renders/<shot id>/take_N.mp4`, log in `renders/status.json` (`renders` = your `output_dir`). To pick a take, set `"approved": N` for that shot in `status.json`.

## 4. Assemble
```
python assemble_film.py ../../shots/seq_01_shots.jsonl --out seq01.mp4
```
Missing shots become black slates of the right length, so you can watch a sequence while it is still rendering.

## 5. Sound (separate pass)
Dialogue: record or generate voices, then lip-sync the speaking shots (production bible 05 §9). Music, effects and the final mix go in an editor (e.g. DaVinci Resolve) over the assembled picture.
