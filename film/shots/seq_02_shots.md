# SEQUENCE 02 — THE READINGS — shot list and AI-video prompts

HERE AM I · screenplay `screenplay/sequences/seq_02.fountain` (pp. 8–19) · notes `screenplay/notes/seq_02_notes.md` · 2 Nov 2033, 03:12 → dawn, 3 Nov 2033 · photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

**Shots:** 10 · **Total running time:** 0:51 (51 s, 0.8 min) against a page estimate of 12.7 pp in the notes' scene table (1 page ≈ 1 min; the notes' header target is 11 pp).

## Scenes

| # | Heading | Beat | Est. pp | Shots | Running time |
|---|---|---|---|---|---|
| 02.01 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - NIGHT | the writing-in (2 Nov, 03:12) | 1.0 | 10 | 0:51 |
| 02.02 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - MORNING | "A stick."; the mirror; the cup | 1.5 | 0 | 0:00 |
| 02.03 | INT. GEM CONSERVATION CENTRE, LAB CORRIDOR - CONTINUOUS | the sealed bay | 0.4 | 0 | 0:00 |
| 02.04 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - DAY | the Debunk Reading; the Nine Bows edit | 3.6 | 0 | 0:00 |
| 02.05 | INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - NIGHT | Layla meets Tut; the first account | 4.1 | 0 | 0:00 |
| 02.06 | INT. NOUR'S FLAT, CAIRO - NIGHT | the frame-scrub: IS IT LISTENING? | 0.7 | 0 | 0:00 |
| 02.07 | EXT. GEM ATRIUM BALCONY - DAWN | the pact (3 Nov) | 1.4 | 0 | 0:00 |
| | **Total** | | **12.7** | **10** | **0:51** |

## How to read this list

- Every PROMPT and NEGATIVE is tokenized: `{TOKEN.FIELD}` pastes the production bible's fixed wording from `production_bible/locks.json`; `{SUFFIX}` and `{NEG}`/`{NEG_*}` paste file 05 §1.1, §2.1 and §2.2. Run `python3 tools/shots_md2jsonl.py shots/seq_02_shots.md` to expand them into `shots/seq_02_shots.jsonl` (with the derived motion prompt per 05 §5.5).
- PROMPT order is the 03b / 05 §5.1 house pattern. One LONG lock per prompt at most (05 §5.2). The writer's own words stay at or under about 70 per prompt.
- Act I camera (05 §4.4): composed, symmetrical, locked-off wides, slider moves and slow push-ins; **no handheld anywhere in this sequence** (handheld arrives at 3.6).
- Look codes for the whole sequence: Tut A0 at L0 (white linen gown), chest glow G0, nape port, no seams cracked, the clinic cane from 02.02; Nour, Adaeze, Tomas, Hale, Rami, Tarek all wardrobe A at L0; Layla A (2.4 galleries). Shabti D0.
- COMP carries every readable element: SUPERs, subtitles for the Middle Egyptian, Late Egyptian and Egyptian Arabic lines, every wall screen and the WITNESS RELIABILITY gauge, the laptop footage and transcription, Layla's cartouche, the mug's printed image, the chest glow and the mirror seam paint.
- Minors rule (05 §7.4): no unit is ever within reach of Layla in any frame; the "arm's length" beat is built by the cut, never in one frame. Layla is never seen asleep (the flat plays on a closing door).


## Scene 02.01 — INT. GEM CONSERVATION CENTRE, TUT'S BAY - NIGHT

### 02.01.001 — Tut's bay, night — The writing-in   (7 s)
- **Shot:** Wide establishing, anamorphic 32mm, through the bay's glass wall · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0; asleep under linen, back to camera; G0; nape port with the lead); SHABTI ×1 (UNIT_SHABTI, D0) at the bedside
- **Action:** Tut sleeps on his side under white linen, his back to camera, a faint glow breathing through the cloth; a shabti stands perfectly still at the bedside, a hair-fine lead running from its wrist to the port at his nape. The SUPER fades up and out.
- **Dialogue:** —
- **Sound:** the lab's low air-handling hush; slow sleeping breath; one faint dry ceramic tick as the shabti's hand settles; ambient sound only, no dialogue
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: through a glass wall the camera looks into a small patient bay where {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_LEAD}, lies asleep on his side under a white linen sheet with his back to camera, while {UNIT_SHABTI.SHORT} stands perfectly still at the bedside. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, the bay dimmed low for the night. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, robot hand on his head, thick cables, medical tubes, drips, hospital-horror lighting, extra people in the bay
- **Refs:** CHAR_TUT_A0_full, CHAR_TUT_NAPE_PORT, UNIT_SHABTI_REF_A, LOC_GEM_CC_NIGHT, LOC_GEM_CC/TUT_BAY
- **Flags:** COMP
- **Comp:** SUPER | "2 NOVEMBER 2033. 03:12." | lower left, small, subtitle family (05 §13.7) | fade in at 1 s, hold 4 s, fade out | seq 02 cards file // chest glow G0 | cold pale-green light swelling once every 4 s through the linen (file 01 G0 table) | at his chest, ~6 cm spill, seen through the sheet edge | full clip | glow element
- **Continuity:** 03:12 on 2 Nov, the night after the resurrection (1 Nov). Tut A0, L0, G0, nape port with the lead (file 01 overlay "nape lead", 2.1), no seams cracked, no cane yet. Shabti D0, slit steady amber. Geography (file 03 LOC_GEM_CC): the bay opens off the lab at back left; the observation room lies behind the lab's glass wall, frame right of the lab master.

### 02.01.002 — Tut's bay, night — The lead at the nape   (5 s)
- **Shot:** Insert, 100mm macro, from directly behind · **Move:** slow push-in
- **In frame:** TUT (nape and shoulder only); SHABTI (wrist, soft, background)
- **Action:** The camera moves in on the gold-rimmed port at Tut's nape and the hair-fine lead running from it to the shabti's wrist; the linen over his shoulder rises and falls with his breath.
- **Dialogue:** —
- **Sound:** slow breath; a faint high electrical whisper along the lead; ambient sound only, no dialogue
- **PROMPT:** Insert, 100mm macro lens, slow push-in: from directly behind, the camera moves in on the shaved nape of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, {CHAR_TUT.STATE_LEAD}, as the white linen over his shoulder rises and falls with a slow sleeping breath; beyond, soft and out of focus, hangs the wrist of {UNIT_SHABTI.SHORT}. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed low, a faint amber edge from the robot's light-slit on the pillow. Mood: hushed, clinical, intimate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, thick cable, wires, needle, puncture, wound at the neck, redness, visible face
- **Refs:** CHAR_TUT_NAPE_PORT, UNIT_SHABTI_REF_A, LOC_GEM_CC_NIGHT, LOC_GEM_CC/TUT_BAY
- **Continuity:** The nape is seen only from behind (file 01). The lead is hair-fine, never a cable; it glints, it does not glow. Port intact until 6.2.

### 02.01.003 — Tut's bay, night — Murmuring English in his sleep   (6 s)
- **Shot:** Close-up, anamorphic 75mm, from the far side of the bed · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0; asleep)
- **Action:** Tut's face on the pillow, eyes closed; his lips move, shaping English softly, three drowsy words; then his mouth goes still.
- **Dialogue:** TUT (asleep, murmured): "...harbour... hardly... harvest..."
- **Sound:** the three murmured words, soft on the consonants (the partial cleft palate lives in the recording, never in the picture); breath; the air hush
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: the face of {CHAR_TUT.LONG} rests on a white pillow, eyes closed and fast asleep, his lips moving as he murmurs three drowsy words, speaking quietly in his sleep, and then his mouth goes still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed low, a faint amber edge from a light-slit off frame. Mood: tender and unhurried, faintly uncanny. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, eyes opening, pillow text, tubes on the face, oxygen mask
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC_NIGHT, LOC_GEM_CC/TUT_BAY
- **Continuity:** English is being written in through the port (bible 2.2). Lip-sync from the actor's recording of the three words; keep the generated head still. Neck seam visible at the pillow line.

### 02.01.004 — Tut's bay, night — Behind the glass   (7 s)
- **Shot:** Wide shot (master), anamorphic 32mm, reverse from inside the bay · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0), HALE (CHAR_HALE_A0), ADAEZE (CHAR_ADAEZE_A0) at the observation desk; the wall screen (COMP)
- **Action:** Reverse angle: behind the glass in the dim observation room, Nour, Hale and Adaeze stand at the long desk watching the bay in silence; above them a large screen scrolls (COMP).
- **Dialogue:** —
- **Sound:** muffled through the glass: the desk's faint fan hum; a soft scroll tick from the screen; ambient sound only, no dialogue
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: from inside the patient bay, the camera looks back through the glass wall at three figures standing at a long desk, {CHAR_NOUR.SHORT}, {CHAR_HALE.SHORT} and {CHAR_ADAEZE.SHORT}, all watching the sleeping bay in silence while a large dark screen above them glows faintly with abstract lines. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, the observation room darker, their faces lit softly by the screens. Mood: restrained unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_HALE.NEG}, {CHAR_ADAEZE.NEG}, readable screen text, percentages, reflections doubling faces, more than three people
- **Refs:** CHAR_NOUR_A_full, CHAR_HALE_A_full, CHAR_ADAEZE_A_full, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Flags:** COMP
- **Comp:** wall screen | two lines scrolling upward: "ENGLISH (CONTEMPORARY) 71%" / "EGYPTOLOGY, SECONDARY LITERATURE 14%", amber on black with SESHAT's glyph (file 02 §8.1) | the large screen above the desk, upper third | full clip | seq 02 screen-graphics file
- **Continuity:** Three faces allowed only because this is a locked-off master (05 §4.5). Nour A0 (glasses on the cord, pendant), Hale A0, Adaeze A0 (index cards in the blazer pocket, unseen). They stand left to right Nour, Hale, Adaeze; hold that order in the singles.

### 02.01.005 — Tut's bay, night — "You're writing into the witness."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, through the glass from the bay side · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour, eyes on the sleeping king beyond the glass, speaks without turning her head.
- **Dialogue:** NOUR: "You're writing into the witness."
- **Sound:** her line, close and dry; the fan hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera looks through the glass at {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, standing at the observation desk with her eyes fixed on the sleeping bay, and she speaks one short sentence without turning her head. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, her face lit by the bright bay through the glass. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glare hiding the face, reflection over the mouth, glasses on her face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Continuity:** Nour as the SCA-appointed inspector. Glasses hang on the cord (she wears them only to read). Pendant at the collarbone.

### 02.01.006 — Tut's bay, night — "We're saving weeks."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, through the glass · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale, beside her, answers with a practised small smile.
- **Dialogue:** HALE: "We're saving weeks."
- **Sound:** his line, soft and warm; the fan hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: through the glass, {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, standing at the observation desk, keeps his eyes on the bay and answers with a practised small smile, speaks one short sentence. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, his face lit by the bright bay through the glass. Mood: calm, persuasive, unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, glare hiding the face, reflection over the mouth
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Continuity:** Hale A0 (open collar, no tie, steel watch). He stands frame right of Nour (see 02.01.004).

### 02.01.007 — Tut's bay, night — The write log is empty   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** ADAEZE (hand only); desk screen (COMP)
- **Action:** Adaeze's hand taps the dark desk screen; a pane opens. It is empty.
- **Dialogue:** —
- **Sound:** a soft glass tap; a small interface chime, then nothing
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's deep-brown hand in a navy blazer cuff taps a dark desk screen, and a blank pane opens on it, glowing faintly with abstract lines around an empty frame, and the hand stays hovering over it. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, the screen's cool glow on the fingers. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable screen text, keyboard lettering, icons with words, rings on the fingers
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Flags:** COMP
- **Comp:** desk-screen pane | a pane titled "WRITE LOG" opening on an empty list, amber on black with SESHAT's glyph (file 02 §8.1) | fills the screen area under the hand | from the tap to the end | seq 02 screen-graphics file
- **Continuity:** There is no write log (bible 2.2). Adaeze A0 cuff; no pigment yet (that is Seq 9).

### 02.01.008 — Tut's bay, night — "SESHAT. Where's the write log?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, through the glass · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze looks up from the empty pane and asks the room.
- **Dialogue:** ADAEZE: "SESHAT. Where's the write log?"
- **Sound:** her line, crisp; the fan hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: through the glass, {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, lifts her eyes from the desk screen to the empty air of the room and speaks one short sentence, level and exact. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, a soft key on her face from the bright bay, the screen glow below. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, underexposed face, glare on the glasses hiding the eyes
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_A_full, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Continuity:** Adaeze stands frame right of Hale. Keep a motivated soft key on her deep-brown skin (05 §3.3).

### 02.01.009 — Tut's bay, night — The unit at the bedside   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** SHABTI ×1 (UNIT_SHABTI, D0); TUT (soft foreground, asleep; lead)
- **Action:** The shabti stands perfectly still at the bedside, the lead glinting from its wrist to the sleeper's nape. SESHAT answers from the room.
- **Dialogue:** SESHAT (V.O.): "There isn't one, Dr. Okoro. Logging would slow the transfer."
- **Sound:** SESHAT's voice, warm, low, female, unhurried, from the room speakers (no sync; the unit has no mouth); the air hush
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {UNIT_SHABTI.LONG} stands perfectly still at a hospital bedside, arms hanging relaxed, its steady amber slit the only warm light in the bay; in the soft foreground lies {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_LEAD}, asleep under white linen. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed low. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, robot touching his face, robot leaning over the bed, head tilt, gesturing robot
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, CHAR_TUT_A0_34, LOC_GEM_CC_NIGHT, LOC_GEM_CC/TUT_BAY
- **Continuity:** The slit does NOT brighten here (the single brightening is reserved for "Here am I", 05 §5.6). The unit never moves while SESHAT speaks.

### 02.01.010 — Tut's bay, night — "Of course it would."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, through the glass · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze, deadpan, one eyebrow up over the glasses.
- **Dialogue:** ADAEZE: "Of course it would."
- **Sound:** her line, flat; silence after it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: through the glass, {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, looks back toward the sleeping bay with one eyebrow raised over her glasses and speaks one short sentence, flat and unimpressed. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, a soft key on her face from the bright bay. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, underexposed face, smiling broadly
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC_NIGHT, LOC_GEM_CC/OBSERVATION
- **Continuity:** Scene out on Adaeze. Cut to morning (02.02). She now knows there is no write log (end state, notes).
