# Handoff: render S01E01 on the user's own PC with Wan

You are Claude Code running on the user's Windows PC. A cloud session built this
whole project but could not render it: it had no GPU and could not reach any video
model. Your job is to render the episode locally with Wan, the open video model,
and assemble it. Read this file fully before doing anything.

## Who you're working with

The user is not a developer. Speak plainly, one step at a time, no jargon. They
have been told several times that the film "can't be made yet" and are tired of
it. Be direct about time and quality, and show them results early.

**Never spend money without their explicit yes** (Veo, cloud GPUs, paid plans).
Before any job that ties up their PC for more than an hour, tell them how long it
will take and get an OK.

## The machine (as the user described it; verify)

- NVIDIA RTX 3060, probably the 12 GB desktop card; 32 GB RAM; Windows.
- The user says video tools may already be installed. Check before installing anything.

## What already exists in this repo

- The episode: 320 shots, 36:08, every shot described in
  `production/06-shots/shot-prompts.json` (the prompts there are written for Veo
  and are far too long for Wan; see step 4).
- A complete previs master built from drawn boards. It proves the assembly works.
- `tools/conform.py` assembles the episode from `renders/SHxxxx.mp4` files, using a
  drawn board for any shot that has no clip yet. It handles any resolution and
  frame rate, crops to the 2:1 frame, trims long clips, and **holds the last frame
  of a short clip** so the timeline never drifts. Tested.
- `production/06-shots/wan-first-pass.txt`: the 122 shots with no close-up face and
  no dialogue. Wan handles these well. Do these first.

## Steps

1. **Scan the PC.** GPU name, VRAM, driver (`nvidia-smi`); free disk; Python, git,
   ffmpeg; any existing ComfyUI, Pinokio, Wan2GP or SwarmUI install; any Wan model
   files (`*.safetensors`, `*.gguf`) and their sizes. Tell the user what you found
   and what, if anything, is missing, in a few plain lines.

2. **Choose the engine: use what's installed.** ComfyUI (local API at
   `http://127.0.0.1:8188`) or Wan2GP are both fine. On a 12 GB 3060 the practical
   models are Wan 2.1 T2V 1.3B or Wan 2.2 TI2V 5B at about 832x480. 720p is not
   practical on this card: reports run 15 minutes to 2.5 hours per clip.

3. **Render ONE test shot and show the user** before any batch. Use `SH0160`
   (the device glowing on the coffee table in a dark room; no faces). Report the
   actual render time. That number sets every estimate after it.

4. **Write Wan-sized prompts.** Wan's text encoder cuts off long prompts. Write a
   script that turns each shot in `shot-prompts.json` into about 80-120 words:
   framing, subject, action, location, light, "realistic, 35mm film, film grain."
   Keep the negative prompt short: text, subtitles, logo, watermark, cartoon,
   anime, 3d render, neon, hologram, user interface, oversaturated, blurry,
   distorted. Show the user two or three examples.

5. **Batch the 122 first-pass shots.** Output contract: `renders/<SHOT_ID>.mp4`.
   Any resolution; any length. Shots longer than one clip may be a single clip
   (the conform holds its last frame) or several clips joined. Make it resumable:
   skip any shot whose file already exists. On a 3060, expect roughly 15-20
   minutes per 5-second clip, so about 210 clips is 2-3 days. Confirm with the
   test-shot timing and get the user's OK first.

6. **Assemble.**
   ```
   pip install numpy
   python tools/render_boards.py     # redraws the fill-in boards (they aren't in git)
   python tools/conform.py --source auto --burn-subs
   python tools/qc.py
   ```
   The output is `deliverables/S01E01_picture_master.mp4`. Show it to the user.

## The other 198 shots (faces and dialogue)

Wan has no way to keep Miles's and Lauren's faces the same from shot to shot, and
it makes no sound. Give the user the choice, plainly:

- **Veo, paid:** `tools/render.py` is written, tested offline and reviewed.
  It needs a `GEMINI_API_KEY`. About $72 for these shots at the cheapest quality
  (`--model veo-3.1-lite-generate-preview --resolution 720p`), about $218 at Fast.
  Run `python tools/render.py plan` for exact numbers. Money: ask first.
- **Wan, free and rough:** image-to-video starting from the reference photos in
  `reference/`. Faces will drift. Fine as a first cut.

Voices: the user's reference clip was made in ElevenLabs, so they may already have
voices there. Ask before assuming.

## Housekeeping

- Work on branch `claude/were-from-the-future-ep1-pe3bew`. It feeds PR #2.
- `renders/`, `boards/` and `deliverables/` are gitignored. Never commit video files.
- Commit scripts you write (for example `tools/render_wan.py`), not outputs.
