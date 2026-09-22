# SHOT LIST & AI-VIDEO PROMPT SPEC — HERE AM I

Goal: turn each screenplay sequence into a shot list whose every shot carries a **self-contained, paste-ready prompt** for photorealistic AI video at **1920×1080, 16:9, 24 fps**, with realistic human actors and consistent characters across hundreds of clips.

## Read first
1. `production_bible/`: every file. The **look-lock descriptors** for characters, units, locations and props are FIXED WORDING. Paste them verbatim (or their short form where the bible gives one); never paraphrase them. Consistency across 1,200 clips depends on this.
2. Your sequence's screenplay: `screenplay/seq_NN.fountain`.
3. `drafts/02_STORY_BIBLE_LOCKED.md` §10 (motifs and palette) and §11 (continuity).

## Coverage
- Cover **every scene** of your sequence. Target an average shot length of 5–7 s: roughly **8–12 shots per screenplay page** for action and 5–8 for dialogue. A clip is 4–8 s. For a longer take, split it into chained clips marked `EXTEND of <previous id>`, with the same framing continuing.
- Coverage grammar: an establishing shot → a master → singles and over-the-shoulders for dialogue → inserts for props and hands → reaction shots. Action uses clear geography shots before chaos.
- Dialogue shots: one line (or a short exchange) per clip.

## Shot entry format (Markdown; one block per shot)

```
### 07.03.012 — Karnak, Hypostyle Hall — Rami runs the cart   (6 s)
- **Shot:** MS tracking, 35mm, handheld · **Move:** lateral track right with Rami
- **In frame:** RAMI (look A2), JACKAL ×1 (bg)
- **Action:** Rami shoves a hand-cart carrying a sandstone block between two giant columns; a black quadruped robot slips between columns behind him.
- **Dialogue:** RAMI: "Heavy! Why is history always heavy?"
- **Sound:** cart wheels on stone, distant drone whine, his breath
- **PROMPT:** <one self-contained paragraph, 70–120 words, in the fixed order below>
- **NEGATIVE:** <global negative + shot-specific>
- **Refs:** CHAR_RAMI_A, LOC_KARNAK_HYPOSTYLE_NIGHT, UNIT_JACKAL
- **Continuity:** block now on cart; Rami's left sleeve torn (from 07.02)
```

### PROMPT paragraph: fixed order
1. **Shot type + lens + camera move** ("Medium tracking shot, 35mm lens, handheld, the camera tracks right with…").
2. **Subject(s), with the look-lock descriptor pasted in** (short form allowed only if the bible provides one). Name no real person, brand or trademark.
3. **The single clear action** within 4–8 seconds (one verb chain; no scene changes inside a clip).
4. **Setting**, with the location lock pasted in, plus time of day.
5. **Lighting and palette** per era or scene (bible §10 and the style guide).
6. **Mood / performance note** ("restrained terror", "wry").
7. **The GLOBAL STYLE SUFFIX** from `production_bible/05_style_and_prompt_grammar.md`, pasted verbatim.

### Rules
- Photorealism: every prompt specifies live-action, real human actors, natural skin texture and film grain, via the style suffix.
- **No text rendering reliance.** Avoid prompts that need readable on-screen text, hieroglyph accuracy, screens with words, or signs. Where the story needs readable text (title cards, subtitles, hieroglyph close-ups, SESHAT's glyph), mark the shot `COMP` (composite in post) and describe the plate only. Supply the overlay text or glyph separately in the entry's `Comp:` line.
- **Safety staging (so clips generate and stay PG-13):** no gore, wounds or dismemberment. Deaths happen by cut-away, silhouette, a fall out of frame, a reaction shot or sound. Weapons point away from camera. The mummy and human remains are shown with reverence: wrapped, partly covered, or seen through glass. Robots are never shown harming a child.
- **Crowds and huge scale:** describe it as "hundreds of sleeping figures in rows receding to the horizon" and mark it `VFX-EXTEND` (generate a base plate, extend in post).
- **Water, fire, collapse:** describe it simply; mark `VFX-ASSIST`.
- **Continuous takes:** break them into chained clips (`EXTEND of`).
- **Consistent faces:** always attach the character's reference stills (the `Refs:` line) and use image-to-video from the matching still where the tool allows.
- **Dialogue and audio:** put the line in `Dialogue:`. Tools that generate audio can use it directly, but the recommended pipeline is to generate the picture, then record the dialogue (ADR or a voice actor), then run lip-sync in post. Keep speaking shots to medium or close-up with the face clearly visible.
- **Egyptian-language lines:** the dialogue field gives the English subtitle; the picture prompt says "speaking softly in an ancient language".
- IDs: `SS.CC.NNN` = sequence number . scene number within the sequence . shot number (e.g. `07.03.012`).

## Deliverables per sequence
1. `shots/seq_NN_shots.md`: a header (sequence title, scene list, shot count, total running time), then every shot block.
2. `shots/seq_NN_shots.jsonl`: one JSON object per line with keys `id, scene, duration_s, shot, move, in_frame, action, dialogue, sound, prompt, negative, refs, flags, continuity`, where `flags` is an array drawn from `COMP`, `VFX-EXTEND`, `VFX-ASSIST` and `EXTEND:<id>`. It must be valid JSON Lines; validate it with python before finishing.
