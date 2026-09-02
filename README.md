# WE'RE FROM THE FUTURE
## Season 1, Episode 1 — "The Package"

A complete production package for a 36-minute prestige science-fiction mystery
drama: bible, screenplay, previs, shot prompts, post plan, key art and a playable
animatic.

**Production workspace:** https://claude.ai/code/artifact/ef9023ff-a154-4147-b548-17e50f12813d

---

## READ THIS FIRST

**Two things are true at once.**

1. **No photographic frame has been rendered.** This repository was built in a
   container with no image, video or speech model attached. The container's
   egress policy blocks Perplexity, Runway, Replicate, fal, Luma and Kling
   outright. The one video model it *can* reach is Google's Veo — which is
   exactly what Perplexity's own video feature calls, at 8 seconds a clip.
2. **Everything up to that frame exists and has been executed.** The render
   pipeline is written against the real `google-genai` SDK source, dry-run
   verified for all 320 shots, and priced. The conform has been proven
   end-to-end on the real EDL by assembling a complete 36-minute previs master
   with temp sound and subtitles. The moment a Gemini API key is present, the
   same commands produce the picture master.

| | |
|---|---|
| **Screenplay** | 6,900 words, v3.0, five documented revision passes |
| **Shots** | 320, every one with framing, lens, movement, lighting state, sound cue, music cue, a composed generation prompt, a negative prompt and a seed |
| **Runtime** | 36:08 fine cut (35:27 excluding the post-credit tag), inside the 28–38 minute brief |
| **Previs master** | `deliverables/S01E01_previs_master.mp4` — the whole episode, boards, timed to the frame, temp track, burned subtitles |
| **Render pipeline** | `tools/render.py` — Veo 3.1, reference plates on every shot with people, chained pieces for long shots, resume, cost ledger |
| **Post** | CMX3600 EDL, SRT, VTT, SDH captions, sound design plan, music cue sheet, colour grade guide |
| **Art** | Poster and 16:9 thumbnail, authored as vector and rasterised |
| **QC** | 41 executed checks, all passing; pipeline adversarially reviewed against the SDK |

---

## RENDERING THE PICTURE — the runbook

```bash
export GEMINI_API_KEY=...                  # from https://aistudio.google.com/apikey

python3 tools/render.py plan               # what it will cost, before spending anything
python3 tools/render.py models             # free: lists the Veo models your key can see
python3 tools/render.py smoke              # three deliberate shots (~$4): a two-shot with dialogue, the double, a chained shot
python3 tools/render.py render --yes       # all 320 shots, 4 in parallel, resumable
python3 tools/conform.py --source auto --audio clips --burn-subs
```

| | Veo 3.1 Fast | Veo 3.1 |
|---|---|---|
| Generated seconds | 2,356 (2,168 s of picture, optimal 4/6/8 s cover; 401 paid calls) | same |
| List price | **~$353** | **~$942** |
| Wall clock | ~2.5 h at 4 parallel operations | same |
| Realistic first cut | ×1.3 for re-takes (face drift, burned captions, motion) | same |

What the pipeline does that a chat box cannot: it attaches the face-centred
reference plates to **every shot with people** (272 of 320) so the leads are
the leads; it splits the 79 shots longer than eight seconds into an optimal
cover of pieces chained from the previous piece's last frame; it assigns each
line of dialogue to the piece it falls in and to the person actually in frame,
and tells Veo not to draw captions; it persists every paid operation the moment
it is accepted, retries with backoff, and resumes, so a crash or a rate limit
never pays twice; and it feeds the identical conform that already built the
previs master.

It was adversarially reviewed against the SDK source before being handed over:
19 confirmed defects in the first version (two blockers) are fixed and covered
by `tools/test_render.py`, an offline suite that runs the SDK's real converters
and parsers against canned Veo responses. See
`production/08-qc/pipeline-review.md`.

**Vertex AI instead of a key** (`GOOGLE_GENAI_USE_VERTEXAI=true` + project +
location) additionally honours the per-shot seeds and the explicit audio flag;
the Gemini Developer API does not accept either — the SDK raises.

**Quality ceiling, stated plainly:** Veo 3.1 with reference images is the best
available path to consistent faces across 320 shots, and it will still drift.
Budget curation. The manual QC checklist is the gate.

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

### The conform is proven, not promised
`tools/conform.py` assembled the previs master from the 320 boards through the
same code path the picture master will use: exact per-shot trims, 16:9 → 2.00:1
centre crop, 24 fps, concat in EDL order, subtitles as a soft track and burned,
and a synthesised temp track with the chirp, the doorbell, the knock pattern,
the countdown pulse, the authored silences, and the half-second hole where her
name is.

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
tools/          the source of truth, the generators, render.py and conform.py
boards/         320 previs boards, 1920x960                          [generated]
deliverables/   the previs master                                    [generated]
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
