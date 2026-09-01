# WE'RE FROM THE FUTURE
## Season 1, Episode 1 — "The Package"

A complete production package for a 36-minute prestige science-fiction mystery
drama: bible, screenplay, previs, shot prompts, post plan, key art and a playable
animatic.

**Production workspace:** https://claude.ai/code/artifact/ef9023ff-a154-4147-b548-17e50f12813d

---

## READ THIS FIRST

**No picture, dialogue or score has been rendered, and none can be from here.**

This repository was built in a Linux container with Python, Node, ffmpeg and git.
There is no image model, no video model and no speech synthesis attached to it.
A finished film was not produced and nothing in this repository pretends to be
one.

What *is* here is everything the film is made of, at a standard where a crew — or
a generation pipeline — could execute it without asking a question:

| | |
|---|---|
| **Screenplay** | 6,900 words, v3.0, five documented revision passes |
| **Shots** | 320, every one with framing, lens, movement, lighting state, sound cue, music cue, a composed generation prompt, a negative prompt and a seed |
| **Runtime** | 36:08 fine cut (35:27 excluding the post-credit tag), inside the 28–38 minute brief |
| **Post** | CMX3600 EDL, SRT, VTT, SDH captions, sound design plan, music cue sheet, colour grade guide |
| **Art** | Poster and 16:9 thumbnail, authored as vector and rasterised |
| **QC** | 41 executed checks, all passing |

The `Export` section of the workspace lists exactly what exists and exactly what
does not, and why.

---

## THE EPISODE

> A couple who have spent six years hiding the fact that they are not from this
> century receive an unmarked package containing a device that should not exist —
> and the face on its screen is hers.

The engine underneath it is not time travel. It is that **Miles has been quietly
breaking the one rule that keeps them alive** — nine words, once a year, sent
forward, to tell someone they are alive. The package is dated to that same day.

*You didn't get a package. You got an answer.*

---

## HOW THIS REPOSITORY WORKS

The important design decision: **`tools/shots_data.py` is the single source of
truth**, and everything downstream is generated from it. The shot list, the
storyboard, the animatic, the generation prompts, the EDL, the subtitles, the
continuity matrix and the workspace dataset are all derived, so they cannot drift
apart. Change a duration in one place and the whole package moves together.

```bash
python3 tools/build.py            # shot list, storyboard, animatic, prompts, EDL, subs, continuity
python3 tools/qc.py               # 41 executed checks; non-zero exit on failure
python3 tools/build_promos.py     # 30s teaser and 60s trailer cut sheets + EDLs
python3 tools/build_workspace.py  # assembles workspace/index.html
```

### Three constraints the build enforces, rather than hopes for

1. **The countdown is bound to the cut.** The leaf's clock runs in real time with
   the episode. `build.py` measures the gap between the countdown's first frame
   and the knock, pushes the difference onto the longest unprotected shots in
   that window, and **asserts** the result reads `11:00` when it appears and
   `00:00` on the knock. If it can't, the build fails.
2. **Contact discipline.** Miles and Lauren touch exactly three times in
   thirty-six minutes, and the third is the last shot. The build asserts the
   count, so a fourth touch cannot drift into the cut.
3. **Subtitle conform.** Cues are placed by a reading-speed model and swept once
   for a readability floor and zero overlaps, both asserted.

### The fine cut is a real editorial pass
The assembly runs **41:32**. `build.py` applies a documented 14% compression to
every shot except 24 protected ones — the reveal, the reflection lag, the
three-second pause, the performance high point, the final shot — and lands at
**36:08**. See `production/04-previs/trim-log.md`.

---

## LAYOUT

```
production/
  01-bible/     episode bible, character bible (locked identities)
  02-story/     three structures scored, the chosen beat sheet
  03-script/    screenplay (.fountain) + the five revision passes
  04-previs/    storyboard, shot list, animatic data, trim log      [generated]
  05-assets/    lookbook, locations & props, continuity matrix, manifest
  06-shots/     per-shot prompts, negatives, seeds, QC gates        [generated]
  07-post/      EDL, subtitles, sound design, music cues, grade, titles
  08-qc/        automated audit + the manual gate it cannot clear
  09-marketing/ poster, thumbnail, teaser and trailer cuts
reference/      the supplied plates the leads are locked against
tools/          the source of truth and the generators
workspace/      the production workspace (published as an Artifact)
```

---

## WHAT THE AUDIT FOUND

The QC tool is not decorative. Two real defects surfaced and were fixed:

- The lookbook asserted a framing rule (*"no shared frames between 20:15 and
  28:40"*) that the cut does not implement — Act Four needs them working the
  problem together. The cut was right and the document was wrong; the rule was
  rewritten to the discipline the cut actually keeps, which is now asserted.
- The subtitle conform produced a cue with **negative duration**. Replaced with a
  proper reading-speed model. The SDH file was also leaking production notes as
  viewer captions (`[CHIRP - the episode's signature domestic sound]`); those are
  now authored viewer-facing text.

---

## THE NEXT STEP

`production/06-shots/shot-prompts.json` is the handoff. Every shot carries a
prompt composed from locked blocks — subject, location, lighting, style — plus a
negative prompt, a deterministic seed and its own QC gate. Point a generation
pipeline at it in shot order, conform against `production/07-post/S01E01.edl`,
and work `production/08-qc/manual-qc-checklist.md` — the face-lock, eyeline,
hands and lip-sync checks that no script can perform.
