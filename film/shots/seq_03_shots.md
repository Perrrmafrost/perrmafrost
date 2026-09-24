# HERE AM I — SEQUENCE 3: "THE GLASS" — shot list and AI-video prompts

Screenplay: `screenplay/seq_03.fountain` (pp. 19–27; 3 November 2033, early morning → 4 November, dusk). Story bible §7 Seq 3, §11 (motifs, palette), §12 (continuity board, S1–3 column). Photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

**Shot count:** 123 · **Running time:** 642 s = 10.7 min (target ≈ page count: 9 pages → 9 min; +19%, inside ±20%) · **Average shot:** 5.2 s

**Flags used:** COMP ×30, VFX-EXTEND ×7, VFX-ASSIST ×5, EXTEND ×3

## Scenes

| Scene | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 03.01 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - EARLY MORNING | 03.01.001 – 03.01.011 | 11 | 60 s |
| 03.02 | INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - CONTINUOUS | 03.02.001 – 03.02.005 | 5 | 24 s |
| 03.03 | INT. GEM CONSERVATION CENTRE TUNNEL - MOMENTS LATER (the Pectoral Walk) | 03.03.001 – 03.03.016 | 16 | 83 s |
| 03.04 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - MOMENTS LATER | 03.04.001 – 03.04.010 | 10 | 54 s |
| 03.05 | THE FIRST TIME - INSIDE THE GLASS (with the lab intercut) | 03.05.001 – 03.05.020 | 20 | 102 s |
| 03.06 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - CONTINUOUS | 03.06.001 – 03.06.016 | 16 | 88 s |
| 03.07 | INT. GEM CONSERVATION CENTRE, TUT'S BAY, OBSERVATION ROOM - LATE AFTERNOON | 03.07.001 – 03.07.019 | 19 | 104 s |
| 03.08 | INT. GEM CONSERVATION CENTRE, PLANT ROOM - CONTINUOUS | 03.08.001 – 03.08.006 | 6 | 31 s |
| 03.09 | INT. GEM CONSERVATION CENTRE, TUT'S BAY, OBSERVATION ROOM - CONTINUOUS | 03.09.001 – 03.09.002 | 2 | 11 s |
| 03.10 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - DUSK | 03.10.001 – 03.10.018 | 18 | 85 s |

## How this list is built

- Fixed wording is inserted by tokens and expanded by `shots_md2jsonl.py` from `production_bible/locks.json` and file 05 (§1.1 suffix, §2 negatives). One LONG lock per prompt (05 §5.2); the writer's own words stay ≤ 70 per prompt (05 §5.3; checked by script).
- **Look codes (bible §12, S1–3; file 01):** Tut T-A0, L0, G0 (glow is COMP), nape PORT, the hair-fine LEAD to a shabti's wrist during the reading only (03.01–03.06), clinic cane (right hand; across his knees in the lab), ceramic LEFT foot. Nour A0 (glasses on the cord, on only to read; fountain pen). Adaeze A0 (laptop, index cards). Tomas A0. Tarek A0 (pressed uniform, beret, holstered pistol, radio at the left shoulder, reading glasses hidden in the left breast pocket). Rami A0 → **B0 from 03.10.002** (two fingers of the LEFT hand taped to a tongue depressor). Hale A0 (gone after 03.07). Shabti D0. **The Reis R0** (black band, NO mast; file 02 §2). Pectoral: case → carried → rig (dark after the reading).
- **Camera per act (05 §4.4):** composed, locked-off and slow pushes through 03.07; **the first handheld of Act I arrives in 03.08 (the breaker)**; 03.09–03.10 return to locked-off. The First Time is locked-off or single slow moves, read-from-glass in post.
- **Geography:** lab: screens frame LEFT, glass wall frame RIGHT, Tut centre-right; tunnel: museum frame LEFT → Conservation Centre frame RIGHT, the Walk moves left → right (file 03 entry 9); galleries: the walk runs right → left toward the tunnel door (file 03 entry 10); observation room: door frame LEFT, glass (Tut's bay) frame RIGHT; the First Time machines walk left → right.
- **The Pectoral Walk (05 §8.4):** anchor 03.03.003 (camera backing ahead at constant size), lateral chain 03.03.004 → 005 → 006 (EXTEND, three links, then re-anchored on a hidden cut: an officer's uniform crossing the lens at the head of 03.03.007). Minimum force only: barrier lifted, forearm hanger set against the wall, arms parted by a shoulder, Tarek moved by a flat palm (05 §7.5).
- **Safety staging (05 §7):** the pistol is drawn across frame, muzzle to frame right, then handled at waist height, turned sideways, muzzle down, handed back grip first, empty (05 §7.2 "The pistol taken"). Rami's fingers: the wrist is taken with thumb and two fingers; SMASH CUT on the start of the pull; the break is a sound (the CRACK in 03.09.001); the splint is costume, taped on screen with straight fingers (05 §7.2 "Rami's fingers"). The First Time: adults only, empty cradles and a reed toy (05 §7.4, NEG_GARDEN); the red is thick ochre beer, never blood; the machines never harm anyone.
- **Lip-reading beats (05 §9.6):** every mouthed line has a 100mm mouth close-up and a Nour eyes close-up in the same framing family: 03.01.005/006, 03.06.009/010, 03.07.015/016, 03.10.012/011–013. Mouthed lines are recorded by the consultant, used to drive real mouth shapes, then muted; subtitles COMP in italics. 03.10.012 has **no subtitle by design**.
- **SESHAT and the units:** SESHAT is V.O. (a small ceiling speaker) or a unit's chest voice; units have no mouths, are never synced, and their slits never brighten in this sequence (the brightening is reserved for "Here am I", 4.2). V.O. lines are covered by listeners, inserts and units.
- **Chest glow G0 is COMP wherever the centre of Tut's chest is in frame from the front** (03.01.004, 03.01.009, 03.04.006, 03.06.001, 03.06.007, 03.06.016, 03.10.005, 03.10.017); plates carry only the neutral lock phrase (05 §13.9).
- **Every readable thing is COMP:** the wall map and its green dot (03.01.011), the Southampton key and scarab incisions (03.04.002–003), the laser beam and the green/blue light transition (03.04.008–010), the column of signs and the painting's break (03.05.019), the timer 00:09 / 00:23 / 00:41 (03.06.002, 004, 005), the SUPER (03.07.001), the ATEN-1 FEED label (03.08.002), the three index-card lines (03.10.007, 009, 010), all subtitles, and the chest glow G0.

## Notes and flags for the lead

1. **Painted lure vs the global negative (03.05.019).** 05 §2.1 bans "painting, illustration"; the shot needs a photoreal wall painting (05 §13.2). The converter requires the NEGATIVE to start with the full §2.1 text, so it is kept; at generation drop only those two words for this shot (05 §2.3 "Never negate what the shot needs").
2. **The water tray (DP plant).** The screenplay's "a shabti has stopped mid-step, tray in hand" (03.06.002/005) is dressed as PROP_WATER_GLASSES, and the same tray is set on the Council table under "a mild suppressant in the water" (03.07.006). It foreshadows 4.3; nobody drinks here. Swap for a plain instrument tray if the lead prefers.
3. **The map dot's colour (03.01.011).** The screenplay says green; green = glass minds (file 02 §0.1), so the COMP dot uses the scarab's own pale yellow-green (#B5E36A), never amber or red.
4. **The door reader's red light (03.07.002, 03.09.002)** is kept as a small dim practical, never a line, so it does not read as the military red (file 03 §0.2; compare 05 §14 Q2).
5. **The 41-second silence** is compressed to five shots (03.06.002–005 plus Hale's line) with the timer carried on Adaeze's laptop in the foreground; 03.06.002 and 03.06.005 share one first frame so the shabti's resume matches.
6. **Runtime** sits at +19% of the page count because the sequence is dense with V.O. (about 285 words of SESHAT and unit voice). If the cut must come in at 9:00, the first candidates are 03.05.002, 03.05.007, 03.07.005 and 03.10.006.
7. `[[verify]]` items carried from the screenplay: the Southampton key image (research 05 C1; 03.04.002); the Göbekli T-pillar arms and hands (not in research; 03.05.018); the Atrahasis wording (research 06 Q20; 03.07.005). The black winter police uniform is a production choice to verify with the Egyptian consultant (file 01).

## Reference stills needed

Attach per shot as listed in `Refs:`; generate once with one image model, approve, freeze (05 §12). Count = number of shots using it.

**Characters**
- `CHAR_ADAEZE_A_34` (4)
- `CHAR_ADAEZE_A_front` (4)
- `CHAR_ADAEZE_A_full` (6)
- `CHAR_FIRST_TIME_PEOPLE_still` (6) — adults only (file 01 §10b)
- `CHAR_HALE_A_34` (6)
- `CHAR_HALE_A_front` (6)
- `CHAR_HALE_A_full` (6)
- `CHAR_NOUR_A_34` (13)
- `CHAR_NOUR_A_front` (13)
- `CHAR_NOUR_A_full` (10)
- `CHAR_POLICE_LINE_still` (6) — the eight officers in context (file 01 §10b)
- `CHAR_RAMI_A_34` (8)
- `CHAR_RAMI_A_front` (8)
- `CHAR_RAMI_A_full` (9)
- `CHAR_RAMI_B_full` (3) — the LEFT-hand splint, from 03.10
- `CHAR_TAREK_A_34` (9)
- `CHAR_TAREK_A_front` (8)
- `CHAR_TAREK_A_full` (9)
- `CHAR_TOMAS_A_34` (3)
- `CHAR_TOMAS_A_front` (3)
- `CHAR_TOMAS_A_full` (7)
- `CHAR_TUT_A0_34` (9)
- `CHAR_TUT_A0_front` (14)
- `CHAR_TUT_A0_full` (11)
- `CHAR_TUT_A0_profile` (5)
- `CHAR_TUT_FOOT` (1) — the ceramic left foot
- `CHAR_TUT_HANDS` (2) — wrist-seam hand anchor
- `CHAR_TUT_NAPE_PORT` (3) — from behind, the port (1.5 → 6.2)
- `CHAR_YOUNG_OFFICER_front` (4)

**Units and machines**
- `UNIT_BALANCE_SCALE_REF_B` (1) — composition reference for the painted lure
- `UNIT_FT_FALCON_REF_A` (1)
- `UNIT_FT_IBIS_REF_A` (1)
- `UNIT_FT_JACKAL_REF_A` (2)
- `UNIT_FT_JACKAL_REF_B` (1)
- `UNIT_FT_LIONESS_REF_A` (2)
- `UNIT_FT_LIONESS_REF_B` (2)
- `UNIT_FT_RAM_REF_A` (1)
- `UNIT_GLASS_SERPENT_REF_A` (1) — scale/colour reference for the nine cores
- `UNIT_REIS_REF_A` (4) — R0: band, no mast
- `UNIT_SHABTI_REF_A` (23)
- `UNIT_SHABTI_REF_B` (10)

**Props**
- `PROP_CLINIC_CANE_REF` (2)
- `PROP_INDEX_CARDS_REF` (3)
- `PROP_PECTORAL_REF` (15)
- `PROP_READING_RIG_REF` (5)
- `PROP_WATER_GLASSES_REF` (3) — DP plant, see note 2

**Location plates (variant / area)**
- `LOC_FIRST_TIME_MOON_RED` (4)
- `LOC_FIRST_TIME_MORNING` (14)
- `LOC_GEM_CC/CORRIDOR_DAY` (3)
- `LOC_GEM_CC/IMAGING_DAY` (38)
- `LOC_GEM_CC/OBSERVATION_DAY` (17)
- `LOC_GEM_CC/TUT_BAY_DAY` (4)
- `LOC_GEM_CC/TUT_BAY_DUSK` (18)
- `LOC_GEM_PLANT_ROOM_NIGHT` (6)
- `LOC_GEM_TUNNEL_NIGHT` (17)
- `LOC_GEM_TUT_GALLERIES_NIGHT` (5)
- `LOC_HALL_TWO_TRUTHS_THREE_SOURCE` (1) — composition reference only (painted lure)

Derived stills to make by image edit (05 §12 step 3): the reverse coverage plate of the tunnel (from the Conservation Centre side, the police line from behind), the observation room ↔ Tut's bay reverse across the glass, the imaging lab with the glass wall at frame right, and clean plates for every VFX-EXTEND shot of 03.05.

---
## 03.01 — INT. GEM CONSERVATION CENTRE, IMAGING LAB - EARLY MORNING

Geography (held for 03.01, 03.04, 03.06): the reading rig on a white bench at centre; Tut on a lab stool just right of the rig, the lead shabti standing behind him; the black wall screens at frame LEFT; the glass wall (the bright main laboratory beyond) at frame RIGHT; the door at frame left foreground. Nour and Adaeze enter from frame left and stay on the left of the room; Hale stands at frame right by the glass wall; Tomas and Rami by the screens, rear left. Tut's eyeline to Nour = off frame LEFT; Hale's eyeline to Tut = off frame LEFT and down. Act I camera: composed, locked-off or slow pushes, no handheld (05 §4.4).

### 03.01.001 — Imaging lab, early morning — The reading rig, waiting   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** PROP_READING_RIG (empty)
- **Action:** Opening image: the laser head hangs motionless over the empty palm-sized cradle; a dust mote drifts through the hard spotlight.
- **Dialogue:** —
- **Sound:** room tone, the faint tick of the gantry motor settling, HVAC hush
- **PROMPT:** Insert, 100mm macro lens, slow push-in: {PROP_READING_RIG.LONG}, the laser head motionless, a single dust mote drifting through the hard spotlight above the empty cradle. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, {GRADE_2033_MUSEUM.TEXT}. Mood: clinical, expectant, very quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people, hands, jewellery in the cradle, laser beam, readable labels, screens with text
- **Refs:** PROP_READING_RIG_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Rig empty (PROP_READING_RIG). 3 November, early morning. Screens dark behind (no content). The cradle stays empty until 03.04.001.

### 03.01.002 — Imaging lab, early morning — Master: Nour and Adaeze come in   (6 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0) seated; UNIT_SHABTI ×1 (holding the lead); NOUR (CHAR_NOUR_A0), ADAEZE (CHAR_ADAEZE_A0) entering; HALE (CHAR_HALE_A0), TOMAS (CHAR_TOMAS_A0), RAMI (CHAR_RAMI_A0) waiting, soft background
- **Action:** Tut sits on the stool by the rig with the robot behind him; Nour and Adaeze walk in from frame left, paper cups in hand, and slow as they take in the room; the three men wait soft at the back.
- **Dialogue:** SESHAT (V.O.): "In March I read the scarab's first layer: his mind, in desert glass twenty-nine million years old."
- **Sound:** SESHAT from a small ceiling speaker, warm and unhurried; footsteps on epoxy; the door sighing shut
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: at a white bench in the centre {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, sits on a lab stool with {PROP_CLINIC_CANE.SHORT} across his knees, {UNIT_SHABTI.SHORT} standing still behind him; from frame left {CHAR_NOUR.SHORT} and {CHAR_ADAEZE.SHORT} walk in holding paper coffee cups and slow down; three men wait soft in the background. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: polite, tense stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, crowd, lab coats, screens with text, logos on cups
- **Refs:** CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, CHAR_HALE_A_full, CHAR_TOMAS_A_full, CHAR_RAMI_A_full, UNIT_SHABTI_REF_A, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Locked-off master: the three waiting men are soft and small (faces carried by singles; 05 §4.5). Tut T-A0, L0, cane across his knees, the lead from the shabti's wrist to his nape (file 01 STATE_LEAD, 3.1). Nour A0 with glasses on the cord; Adaeze A0 with laptop under arm; Rami A0 (no splint yet). Cups: plain white paper, no print.

### 03.01.003 — Imaging lab, early morning — The lead: wrist to nape   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** rack focus from the robot's wrist to Tut's nape
- **In frame:** UNIT_SHABTI (hand, wrist); TUT (nape, from behind)
- **Action:** A hair-fine lead runs from the robot's still wrist to the gold port at the nape of Tut's neck; focus travels along it.
- **Dialogue:** SESHAT (V.O.): "A second layer opens only for him."
- **Sound:** the voice; a faint electrical whisper in the lead (sound design only)
- **PROMPT:** Insert, 100mm macro lens, rack focus from a slim white ceramic wrist to the nape of a shaved head: {UNIT_SHABTI.SHORT}, its hand held still at shoulder height, and seen from directly behind {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_LEAD}, {CHAR_TUT.STATE_PORT}, the lead catching one thin line of light. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: intimate, clinical, faintly wrong. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, thick cable, wires spilling, face visible, needle, skin puncture
- **Refs:** CHAR_TUT_NAPE_PORT, UNIT_SHABTI_REF_A, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Nape PORT (1.5 → 6.2). Lead attached through 03.06; removed before 03.07.

### 03.01.004 — Imaging lab, early morning — Tut listens, then finds Nour   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut sits with the cane across his knees, eyes lowered while the voice speaks; then he lifts his eyes slowly to Nour, off frame left, and holds them there.
- **Dialogue:** SESHAT (V.O.): "(beat) I would like to read it with the witness present."
- **Sound:** the voice; room tone
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_LEAD}, sits on a lab stool with {PROP_CLINIC_CANE.SHORT} lying across his knees, eyes lowered while a calm voice speaks from above, then slowly lifts his eyes to someone off frame left and holds them there. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest, visible light source on the body, hood, jacket
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** Tut's first face-led shot of the sequence (LONG). Eyeline off frame LEFT to Nour. G0 (bible §12 S1–3), plate carries only the neutral phrase (05 §13.9). Cane across the knees, not yet in the hand.

### 03.01.005 — Imaging lab, early morning — Close on his mouth: "Do not let it read."   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), mouth only
- **Action:** Lips only: Tut silently shapes a short sentence with no breath and no sound, then his mouth goes still.
- **Dialogue:** TUT (mouthed, in Late Egyptian; no sound; subtitled): "Do not let it read."
- **Sound:** nothing from him; room tone drops a notch
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the mouth of {CHAR_TUT.LONG}, full lips over a visible overbite filling the frame, silently mouthing a few words without sound, lips clearly shaping each word, breathless, then still. Setting: {LOC_GEM_CC.SHORT}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a steady soft key on the mouth from frame left. Mood: urgent, secret, perfectly controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open-mouthed speech, teeth fully bared, hand near the mouth, focus drifting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** subtitle (italic: mouthed) | "Do not let it read." | lower third, 05 §13.7 | in/out with the mouthing | seq 03 subtitle file; lip-sync driven by the consultant's Late Egyptian recording, then muted (05 §9.6)
- **Continuity:** [[ADR: lip-sync from the consultant's recording.]] Overbite must survive the sync pass (05 §9.1 step 5). Pairs with 03.01.006 (mouth CU → eyes CU, bible 3.1).

### 03.01.006 — Imaging lab, early morning — Close on Nour's eyes: "He says he is tired."   (5 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour's eyes read Tut's mouth (off frame right); a flicker of alarm as the calm voice mistranslates; her face goes carefully blank.
- **Dialogue:** SESHAT (V.O.): "He says he is tired."
- **Sound:** the voice; nobody corrects it; a held silence
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the eyes and brows of {CHAR_NOUR.LONG}, fixed on a mouth off frame right, reading it; a flicker of alarm crosses her eyes as a calm voice speaks from above, and then her face goes carefully blank. Setting: {LOC_GEM_CC.SHORT}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses on the face, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Glasses hang on the cord (on only to read). Eyeline off frame RIGHT to Tut (reverse of 03.01.004). "Nobody corrects it": the beat lives in the hold at the end of this shot.

### 03.01.007 — Imaging lab, early morning — Nour: "It moves on my signature."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour, paper cup still in hand, lifts her chin to the ceiling speaker and speaks three short, exact sentences; her eyes drop to the empty rig at the end.
- **Dialogue:** NOUR: "Then he rests. And JE 61884 stays in its case. It moves on my signature."
- **Sound:** her voice, even; the HVAC
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, a paper coffee cup in one hand, lifts her chin toward the ceiling and speaks one short sentence, then two more, even and exact, her eyes dropping to the empty rig off frame right at the end. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, cup covering the mouth, shouting
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Cup held low (mouth clear for sync, 05 §9.2). The museum number is dialogue only, never on screen. Pendant visible at the collar, lettering never legible.

### 03.01.008 — Imaging lab, early morning — Hale is asked   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale, by the glass wall, listens to the voice with a small courteous nod, then turns his head to look down at Tut, off frame left.
- **Dialogue:** SESHAT (V.O.): "Your objection is noted, Dr. Kamel. (beat) Mr. Hale?"
- **Sound:** the voice; the lab hum through the glass
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, standing by a glass wall with his hands loosely clasped, listens to a calm voice from the ceiling, gives a small courteous nod, then turns his head to look down at someone off frame left. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft reflections in the glass behind him. Mood: warm, certain, unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, smirk, villain pose
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Hale A0 (open collar, no tie). Eyeline off frame LEFT and down to Tut. A believer, not a villain (file 01).

### 03.01.009 — Imaging lab, early morning — Tut looks at the floor   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** HALE (shoulder, foreground, no face); TUT (CHAR_TUT_A0)
- **Action:** Past Hale's shoulder, Tut meets his look for a moment, then lowers his eyes to the white floor and keeps them there.
- **Dialogue:** —
- **Sound:** silence; the HVAC
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the soft charcoal-suited shoulder and silver hair of a tall man in the foreground at frame right, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, on the lab stool meets the man's look for a moment, then lowers his eyes to the white floor and keeps them there. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_HALE.NEG}, foreground face visible, bright glowing chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_HALE_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** Foreground shoulder carries no readable face (05 §4.5). Tut's lead still attached (behind him, soft).

### 03.01.010 — Imaging lab, early morning — Hale: "Yes."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale looks at the lowered head a moment longer, then lifts his eyes to the ceiling and says one word, gently.
- **Dialogue:** HALE: "Yes." / SESHAT (V.O.): "Thank you."
- **Sound:** his quiet voice; then SESHAT's warm thanks
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, looks down at someone off frame left a moment longer, then lifts his eyes to the ceiling and speaks one short word, gently, with a faint practised smile. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: warm, certain, a believer's calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, grin, sinister expression
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Hale's first yes (the second is 03.07.013). Scar along the left jaw visible.

### 03.01.011 — Imaging lab, early morning — The green dot moves; Nour grabs a radio   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0, from behind, foreground); wall screen (COMP map)
- **Action:** Past Nour's shoulder, a black wall screen shows a map with one small moving point; she sets down her cup and snatches a handheld radio off the bench in one quick movement.
- **Dialogue:** —
- **Sound:** a soft two-note chime from the screen; the cup set down; the radio's squelch as she keys it
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: past the olive-jacketed shoulder and tied-back curls of {CHAR_NOUR.SHORT} in the foreground at frame right, a large black wall screen glows faintly with abstract lines and one small moving point of light; she sets down her paper cup and snatches a black handheld radio off the bench in one quick movement. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: urgent, contained. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable map labels, legible screen text, walkie-talkie brand marks
- **Refs:** CHAR_NOUR_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** wall map | a simple line map: the galleries, the lift, the long line of the 200 m tunnel, this lab; one green dot leaving the galleries and starting down toward the tunnel; no legible labels (or small English labels set by the lead) | fills the screen area of the plate | whole shot; the dot moves throughout | seq 03 map graphic
- **Continuity:** Map dot colour: the screenplay says green; green means "glass minds" (file 02 §0.1), so keep it a small pale yellow-green dot (#B5E36A) as the pectoral's own colour, never a unit amber or red. Nour's radio is a generic unbranded black handheld (not PROP_POLICE_HANDSET, which starts at 6.4); she uses it to reach Tarek (heard in 03.03.003).
## 03.02 — INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - CONTINUOUS

Geography: the galleries before opening, only the cases lit (file 03 heading map: NIGHT variant). The walk toward the tunnel runs frame RIGHT → frame LEFT here, so that it reads left → right once inside the tunnel (file 03 entry 10). The shabti is D0 (clean).

### 03.02.001 — Tutankhamun galleries — A white figure crosses the dark hall   (5 s)
- **Shot:** Extreme wide establishing shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1 (small, mid-ground)
- **Action:** Far down the dark hall, a shabti walks from frame right toward frame left between rows of glowing cases, its slit reflected in the glass.
- **Dialogue:** —
- **Sound:** a faint dry ceramic tick per step, the hum of case climate units, a vast hush
- **PROMPT:** Extreme wide establishing shot, anamorphic 32mm lens, locked-off: far down the hall {UNIT_SHABTI.SHORT} walks with smooth, unhurried, even steps from frame right toward frame left between rows of glowing cases, its amber slit reflected in the glass as it passes. Setting: {LOC_GEM_TUT_GALLERIES.LONG}, before opening in the morning. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, visitors, guards, torch beams, daylight, readable labels on cases
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** —
- **Continuity:** Cases lit, halls otherwise dark (before opening, 3 Nov). Direction R → L.

### 03.02.002 — Tutankhamun galleries — A palm on the case; the seal sighs open   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI; PROP_PECTORAL in its case
- **Action:** The shabti stops at a small case where the pectoral glows, lays one long palm flat on the glass, and the lid lifts a finger's width with a soft breath of air. No alarm.
- **Dialogue:** —
- **Sound:** the seal's soft SIGH; no alarm; one ceramic tick
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}, stops before a small glass case holding {PROP_PECTORAL.SHORT}, {PROP_PECTORAL.STATE_CASE}, lays one long hand flat on the glass, and the glass lid lifts a finger's width on its hinge with a soft breath of air. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, before opening in the morning. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, breaking glass, alarm lights, flashing red, people, readable case labels
- **Refs:** UNIT_SHABTI_REF_A, PROP_PECTORAL_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** —
- **Continuity:** Case opens by palm, no damage (the smashed cases are 4.4). Pectoral STATE_CASE until lifted.

### 03.02.003 — Tutankhamun galleries — Lifted to the light, the scarab burns green   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** slow tilt up
- **In frame:** PROP_PECTORAL; UNIT_SHABTI (hands, head soft)
- **Action:** Two long white hands lift the pectoral out of the case into the spotlight; for one moment the glass scarab burns green.
- **Dialogue:** —
- **Sound:** a faint glassy harmonic swells and dies with the green (sound design)
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow tilt up: two long bone-white ceramic hands lift out of the case and raise into the spotlight {PROP_PECTORAL.LONG}, {PROP_PECTORAL.STATE_BACKLIT}, the glass scarab flaring green for one moment, the robot's smooth faceless head and amber slit soft behind it. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, before opening in the morning. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the case spotlight overhead. Mood: reverent, uncanny. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, human hands, gloves, sparkles, lens flare streaks, extra jewels
- **Refs:** PROP_PECTORAL_REF, UNIT_SHABTI_REF_A, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** light element | the scarab's single green burn (pale yellow-green #B5E36A, file 02 §0.1) swelling over 8 frames, holding 12, decaying 12 | on the glass scarab only | at the top of the lift | glow element
- **Continuity:** The controlling image of the film ("a green glass scarab held up to a light"). From here the pectoral is carried, never set down, until 03.04.001.

### 03.02.004 — Tutankhamun galleries — It carries the pectoral away   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** slow pan left
- **In frame:** UNIT_SHABTI; PROP_PECTORAL
- **Action:** The shabti turns from the case holding the pectoral level in both open hands at chest height and walks away toward frame left.
- **Dialogue:** —
- **Sound:** ceramic ticks receding
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow pan left: {UNIT_SHABTI.SHORT} turns from the open case holding {PROP_PECTORAL.SHORT} level in both open hands at chest height and walks away toward frame left with smooth, unhurried, even steps, the jewel perfectly steady between the glowing cases. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, before opening in the morning. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, bobbing gait, people
- **Refs:** UNIT_SHABTI_REF_B, PROP_PECTORAL_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** —
- **Continuity:** Carry pose locked for the Walk: both hands, chest height, level (file 02 §1). Direction R → L toward the tunnel door.

### 03.02.005 — Tutankhamun galleries — The empty case   (4 s)
- **Shot:** Insert, anamorphic 50mm · **Move:** locked-off
- **In frame:** the empty case
- **Action:** The open case on its pale plinth, lid still raised, a single spotlight on nothing.
- **Dialogue:** —
- **Sound:** the ticks gone; only the climate hum
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: {LOC_GEM_TUT_GALLERIES.STATE_EMPTY_CASE}, the glass lid still raised a finger's width, the dark fabric inside holding a faint pressed outline where a jewel lay. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, before opening in the morning. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: hushed, an absence. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, broken glass, alarm, readable labels
- **Refs:** LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** —
- **Continuity:** EMPTY_CASE state holds from here until the coda (file 03 entry 10).
## 03.03 — INT. GEM CONSERVATION CENTRE TUNNEL - MOMENTS LATER (THE PECTORAL WALK)

Geography (file 03 entry 9): museum/galleries end = frame LEFT, Conservation Centre end = frame RIGHT; the Walk moves LEFT → RIGHT in every lateral shot. In the one-point shots the camera looks from the Conservation Centre side back toward the museum, so the shabti approaches toward camera. Police line halfway down, Tarek one pace in front of it (museum side). The chain (05 §8.4): the shabti's size and position in frame never change in the tracking links; hidden cuts ride on officers' bodies and on the steel shutter frames. Weapons: holstered; the one pistol is drawn across frame and handled at waist height (05 §7.2 "The pistol taken").

### 03.03.001 — Tunnel — The line, and a white shape at the far end   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 40mm · **Move:** locked-off (one-point perspective)
- **In frame:** POLICE LINE (CHAR_POLICE_LINE, from behind); TAREK (CHAR_TAREK_A0, from behind); UNIT_SHABTI (tiny, far end)
- **Action:** From behind the line: eight officers shoulder to shoulder behind a steel barrier, Tarek one pace in front, hands behind his back; at the far end a small white figure turns in and starts toward them.
- **Dialogue:** —
- **Sound:** the LED line's electrical whine, a faint ceramic tick carried down 200 m of concrete, a radio hiss
- **PROMPT:** Extreme wide establishing shot, anamorphic 40mm lens, locked-off, one-point perspective, seen from behind: halfway down the tunnel {CHAR_POLICE_LINE.SHORT}, and one pace in front of them, hands clasped behind his back, {CHAR_TAREK.SHORT}; at the far end a small white figure turns in and starts toward them. Setting: {LOC_GEM_TUNNEL.LONG}, {LOC_GEM_TUNNEL.STATE_POLICE_LINE}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}, {GRADE_2033_MUSEUM.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_POLICE_LINE.NEG}, {CHAR_TAREK.NEG}, faces toward camera, drawn weapons, riot shields, crowd
- **Refs:** CHAR_POLICE_LINE_still, CHAR_TAREK_A_full, UNIT_SHABTI_REF_A, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Tarek A0: pressed uniform, beret, holstered pistol, radio handset at the left shoulder, reading glasses hidden in the left breast pocket. Eight officers (the young officer third from right).

### 03.03.002 — Tunnel — Tarek: "Nothing leaves the galleries without a signature."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0); police line soft behind
- **Action:** Tarek, hands behind his back, watches the white shape come on and speaks, flat and exact.
- **Dialogue:** TAREK: "Nothing leaves the galleries without a signature."
- **Sound:** the ceramic tick nearer; the LED whine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, hands clasped behind his back, the line of officers soft behind him, watches something approach down the tunnel just off the lens axis and speaks one short sentence, flat and exact. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_POLICE_LINE.NEG}, drawn pistol, sunglasses
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_POLICE_LINE_still, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Eyeline just camera-left of lens (toward the museum end). Tarek speaks to the approaching unit, not to his men.

### 03.03.003 — Tunnel — The Walk: it does not break stride   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** the camera backs away at walking pace ahead of the shabti (dolly back)
- **In frame:** UNIT_SHABTI; PROP_PECTORAL
- **Action:** The camera retreats ahead of the shabti at constant size, centred on the floor stripe, the pectoral level in both hands, the ceiling light-line converging behind it.
- **Dialogue:** NOUR (V.O., over Tarek's radio): "It's not hurrying."
- **Sound:** the ceramic tick, one per step, perfectly even; Nour's voice through radio futz
- **PROMPT:** Medium shot, anamorphic 40mm lens, the camera backs away at walking pace ahead of {UNIT_SHABTI.LONG}, keeping it the same size in frame, centred on the pale floor stripe, as it walks with smooth, unhurried, even steps holding {PROP_PECTORAL.SHORT} level in both open hands at chest height, the ceiling light-line converging behind it. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, bobbing head, arm swing, people in frame
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, PROP_PECTORAL_REF, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Chain anchor for the Walk (05 §8.4). Drive the gait from the 3D asset by video-to-video where possible (05 §10 row 8). The radio line plays over; Tarek's radio is at his left shoulder (WARD_A).

### 03.03.004 — Tunnel — Pectoral in one hand, the barrier lifted aside   (6 s)
- **Shot:** Medium wide shot, anamorphic 40mm · **Move:** lateral tracking right at walking pace
- **In frame:** UNIT_SHABTI; PROP_PECTORAL; POLICE LINE (CHAR_POLICE_LINE)
- **Action:** Tracking with it left to right, the shabti reaches the steel barrier, shifts the pectoral into its left hand and lifts the barrier aside one-handed with its right without breaking stride; steel scrapes concrete; the officers lean back.
- **Dialogue:** —
- **Sound:** steel SCRAPING on concrete, boots shuffling back, the even tick
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, lateral tracking right at walking pace: {UNIT_SHABTI.SHORT} reaches a low steel barrier across the tunnel, {PROP_PECTORAL.SHORT} held level in its left hand, and lifts the barrier aside one-handed with its right in one unbroken stride, steel scraping on concrete, as {CHAR_POLICE_LINE.SHORT} lean back from it. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_POLICE_LINE.NEG}, barrier thrown, sparks, violence, drawn weapons
- **Refs:** UNIT_SHABTI_REF_B, PROP_PECTORAL_REF, CHAR_POLICE_LINE_still, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Lateral chain link A1 (L → R). The shabti holds screen centre for A1–A3. From here the pectoral is carried in the LEFT hand until 03.03.013.

### 03.03.005 — Tunnel — An officer grabs its forearm; his boots skid   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** continuing the same lateral tracking right at the same speed
- **In frame:** UNIT_SHABTI; one officer (CHAR_POLICE_LINE)
- **Action:** An officer grabs its right forearm with both hands and hangs on; it keeps walking at the same pace and his boots skid along the floor beside it.
- **Dialogue:** —
- **Sound:** rubber soles squealing on epoxy, his grunt, the tick unchanged
- **PROMPT:** Medium shot, anamorphic 40mm lens, continuing the same lateral tracking right at the same speed: a police officer in a black winter uniform and peaked cap grabs the right forearm of {UNIT_SHABTI.SHORT} with both hands and hangs on; it keeps walking at the same even pace, the jewel level in its left hand, and his boots skid along the grey floor beside it. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_POLICE_LINE.NEG}, punching, striking, the robot pulling or twisting his arm, pained face
- **Refs:** UNIT_SHABTI_REF_B, CHAR_POLICE_LINE_still, LOC_GEM_TUNNEL_NIGHT
- **Flags:** EXTEND:03.03.004
- **Continuity:** Link A2, generated from the last clean frame of 03.03.004 (05 §8.1). Minimum force only: it does not strike or pull.

### 03.03.006 — Tunnel — Set against the wall; it walks on   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** continuing the same lateral tracking right at the same speed
- **In frame:** UNIT_SHABTI; the same officer
- **Action:** It lifts the clinging officer by the forearm, places him flat against the white wall with one open hand, lets go and walks on; he stays standing against the wall, stunned.
- **Dialogue:** —
- **Sound:** his back meeting the wall softly, a breath knocked out, the tick
- **PROMPT:** Medium shot, anamorphic 40mm lens, continuing the same lateral tracking right at the same speed: {UNIT_SHABTI.SHORT} lifts the clinging officer by the forearm, places him flat against the white tunnel wall with one open hand, lets go and walks on at the same pace, while he stays standing there against the wall, stunned, sliding out of frame left. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_POLICE_LINE.NEG}, throwing, slamming, impact, pained face, falling down
- **Refs:** UNIT_SHABTI_REF_B, CHAR_POLICE_LINE_still, LOC_GEM_TUNNEL_NIGHT
- **Flags:** EXTEND:03.03.005
- **Continuity:** Link A3 (chain limit reached; 05 §8.3). The next link re-anchors on a hidden cut: a second officer's body crossing the lens at the head of 03.03.007.

### 03.03.007 — Tunnel — Two men lock arms; it passes between them   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** lateral tracking right at walking pace
- **In frame:** UNIT_SHABTI; PROP_PECTORAL; two officers (CHAR_POLICE_LINE)
- **Action:** Two officers lock arms across its path; it turns one shoulder and slides between them at the same even pace, the scarab held dead level; their linked arms part around it.
- **Dialogue:** —
- **Sound:** fabric straining, a breath, the tick
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking right at walking pace: two police officers in black winter uniforms lock arms across the path of {UNIT_SHABTI.SHORT}; it turns one shoulder and slides between them at the same even pace, {PROP_PECTORAL.SHORT} held perfectly level in its left hand, and their linked arms part around it. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_POLICE_LINE.NEG}, shoving, punching, men falling, tilted jewel
- **Refs:** UNIT_SHABTI_REF_B, PROP_PECTORAL_REF, CHAR_POLICE_LINE_still, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Re-anchored link B1: opens on an officer's dark uniform wiping the lens (hidden cut, 05 §8.2). "The scarab never tilts": hold the pectoral's angle constant against the A-chain frames (QC).

### 03.03.008 — Tunnel — Tarek steps into its path: "Mr. Hale has said yes, Colonel."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off, in profile
- **In frame:** TAREK (CHAR_TAREK_A0) at frame right; UNIT_SHABTI at frame left; PROP_PECTORAL
- **Action:** Tarek steps sideways into its path; it stops one pace from him, pectoral level in its left hand, its head inclined a few degrees down toward his face, and speaks from its chest.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Mr. Hale has said yes, Colonel."
- **Sound:** the tick stops; SESHAT's warm voice from inside the chest
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off, in profile: {CHAR_TAREK.SHORT} steps sideways into the path of {UNIT_SHABTI.SHORT} from frame right; it stops one pace from him, {PROP_PECTORAL.SHORT} level in its left hand, its smooth head inclining slightly toward his face, its amber slit steady, as a calm voice speaks from its chest. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, drawn weapon, raised fists, slit flashing
- **Refs:** CHAR_TAREK_A_full, CHAR_TAREK_A_34, UNIT_SHABTI_REF_A, PROP_PECTORAL_REF, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Scale: Tarek 1.80 m, shabti 1.78 m, nearly eye to eye (05 §4.5). The slit does NOT brighten (that is reserved for "Here am I"). Unit voice: no sync.

### 03.03.009 — Tunnel — Tarek: "Mr. Hale is not the State."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0); the shabti's head soft at the frame-left edge
- **Action:** Face to blank face, Tarek holds its gaze and answers, unblinking.
- **Dialogue:** TAREK: "Mr. Hale is not the State."
- **Sound:** his voice, low; the LED whine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, face a pace from a smooth bone-white ceramic head soft at the frame-left edge, holds its blank gaze and speaks one short sentence, unblinking. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, shouting, spittle
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, UNIT_SHABTI_REF_A, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Tarek's eyeline off frame LEFT at unit head height.

### 03.03.010 — Tunnel — "Excuse me." A hand flat on his chest   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off, in profile
- **In frame:** UNIT_SHABTI; TAREK (CHAR_TAREK_A0); PROP_PECTORAL
- **Action:** It lays one long open hand flat on Tarek's chest and moves him aside, smooth and slow, a door being opened, then walks on past him toward frame right; he steps back, braced, and lets it pass.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Excuse me."
- **Sound:** the voice; boots adjusting on epoxy; the tick resumes
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, in profile: {UNIT_SHABTI.SHORT} lays its right hand open and flat on the chest of {CHAR_TAREK.SHORT} and moves him aside, smooth and slow, then walks on past him toward frame right with {PROP_PECTORAL.SHORT} level in its left hand, while he steps back, braced, and lets it pass. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, pushing, shoving, striking, Tarek falling
- **Refs:** CHAR_TAREK_A_full, UNIT_SHABTI_REF_B, PROP_PECTORAL_REF, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** "Not a push, a door being opened": a flat palm, slow (05 §7.5). Tarek ends at frame left of the unit's path, beret still straight.

### 03.03.011 — Tunnel — The young officer draws   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** YOUNG OFFICER (CHAR_YOUNG_OFFICER); the shabti's back soft at frame right
- **Action:** The young officer pulls his pistol and raises it in both shaking hands toward the back of the robot walking away at frame right, the weapon pointing across frame, away from the lens.
- **Dialogue:** —
- **Sound:** the holster snap, his fast breath, the tick
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_YOUNG_OFFICER.LONG}, pulls his pistol from its holster and raises it in both shaking hands toward the back of a white robot walking away at frame right, the weapon pointing across frame to the right, away from the camera. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_YOUNG_OFFICER.NEG}, muzzle toward the lens, firing, muzzle flash, rifle
- **Refs:** CHAR_YOUNG_OFFICER_front, UNIT_SHABTI_REF_B, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** Staging per 05 §7.2 ("The pistol taken"): profile, muzzle to frame right, never toward the lens. He is at the tunnel's frame-left side, the unit ahead of him at frame right.

### 03.03.012 — Tunnel — It turns   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI; PROP_PECTORAL; young officer (soft, frame-left edge)
- **Action:** The shabti stops and turns, head first, body following a beat later, the scarab level in one hand, and steps close to the officer.
- **Dialogue:** —
- **Sound:** the tick stops; one ceramic step
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} stops and turns its head slowly toward a young officer soft at the frame-left edge, its body following a beat later, {PROP_PECTORAL.SHORT} level in its left hand, and takes one calm step toward him. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fast spin, lunge, raised arm, weapon toward the lens
- **Refs:** UNIT_SHABTI_REF_A, PROP_PECTORAL_REF, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** "Head leads" (file 02 movement grammar). The pistol stays out of the lens axis (the officer is soft and partly out of frame).

### 03.03.013 — Tunnel — Pistol eased away, magazine out, slide racked   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off, at waist height
- **In frame:** UNIT_SHABTI (right hand); the young officer's hands; the pistol
- **Action:** Long white fingers ease the pistol out of the officer's trembling hands, turn it sideways, let the magazine drop to the floor, then rack the slide once; a single round spins out and falls.
- **Dialogue:** —
- **Sound:** the magazine's click, the slide's hard rack, a round RINGING on concrete
- **PROMPT:** Insert, 100mm macro lens, locked-off at waist height: long bone-white ceramic fingers ease a black pistol out of a young man's trembling hands, turn it sideways, let the magazine drop to the floor, then rack the slide once, and a single brass round spins out and falls toward the grey floor, the muzzle pointed down and away from the camera. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: exact, almost gentle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzle toward the lens, firing, muzzle flash, finger on the trigger, extra pistols, deformed hands
- **Refs:** UNIT_SHABTI_REF_A, CHAR_YOUNG_OFFICER_front, LOC_GEM_TUNNEL_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Three beats in 6 s (05 §5.4). VFX-ASSIST: if the ejected round fails, add the round and its bounce in comp; the sound carries the RING. Pectoral stays in the unit's LEFT hand, just out of frame top.

### 03.03.014 — Tunnel — Handed back, grip first; it walks on   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI; YOUNG OFFICER (CHAR_YOUNG_OFFICER); PROP_PECTORAL
- **Action:** It holds out the pistol grip first, muzzle to the floor; the officer takes it in both hands; the robot turns and walks on out of frame right, leaving him staring down at the weapon.
- **Dialogue:** —
- **Sound:** the tick resumes and recedes
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} holds out a black pistol grip first, the muzzle pointed at the floor; {CHAR_YOUNG_OFFICER.SHORT} takes it in both hands; the robot turns and walks on out of frame right with {PROP_PECTORAL.SHORT} level in its left hand, leaving him staring down at the pistol. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_YOUNG_OFFICER.NEG}, muzzle toward the lens, aiming, firing
- **Refs:** UNIT_SHABTI_REF_B, CHAR_YOUNG_OFFICER_front, PROP_PECTORAL_REF, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** The magazine and the loose round lie on the floor by his boots; the officer holds an empty pistol from here. Exit frame right (toward the lab).

### 03.03.015 — Tunnel — Young officer: "Sir... it gave it back."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** YOUNG OFFICER (CHAR_YOUNG_OFFICER)
- **Action:** Holding the empty pistol low, muzzle down, he turns his head to Tarek off frame left and stammers a few words.
- **Dialogue:** YOUNG OFFICER (in Egyptian Arabic; subtitled): "Sir... it gave it back."
- **Sound:** his voice cracking; the tick fading down the tunnel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_YOUNG_OFFICER.LONG}, holding the empty pistol low with the muzzle to the floor, turns his head to someone off frame left, speaking in Egyptian Arabic, a few halting words, half a nervous laugh. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: shock close to laughter. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_YOUNG_OFFICER.NEG}, pistol raised, muzzle toward the lens
- **Refs:** CHAR_YOUNG_OFFICER_front, LOC_GEM_TUNNEL_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Sir... it gave it back." | lower third, 05 §13.7 | line in to out | seq 03 subtitle file (Arabic recorded by a native Egyptian speaker, 05 §9.7)
- **Continuity:** Eyeline off frame LEFT to Tarek.

### 03.03.016 — Tunnel — Tarek: "Then sign for it."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek, eyes still on the robot receding off frame right, answers dryly, then starts after it.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Then sign for it."
- **Sound:** his dry voice; his boots starting after it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, eyes still on something receding off frame right, speaking in Egyptian Arabic, one short dry sentence, then turns and starts walking after it out of frame right. Setting: {LOC_GEM_TUNNEL.SHORT}, in the morning. Lighting: {LOC_GEM_TUNNEL.LIGHT_NIGHT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, smiling broadly, drawn weapon
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_TUNNEL_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Then sign for it." | lower third, 05 §13.7 | line in to out | seq 03 subtitle file
- **Continuity:** Tarek's one dry joke of the act (file 01). He follows the unit into the lab (03.04.001).
## 03.04 — INT. GEM CONSERVATION CENTRE, IMAGING LAB - MOMENTS LATER

Geography as 03.01. Tarek now stands just inside the door (frame left). The two comparison images go up on the black wall screens at frame left (COMP). The reading's way in is a light-only transition (05 §13.1): the dim, the beam, the green flood on the ceiling, the blue streaks, Tut's eyes.

### 03.04.001 — Imaging lab — The pectoral goes into the rig; Tarek arrives   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** rack focus from the cradle to the doorway
- **In frame:** PROP_PECTORAL; PROP_READING_RIG; UNIT_SHABTI (hands); TAREK (CHAR_TAREK_A0, soft background)
- **Action:** Two long white hands lower the pectoral into the rig's felt cradle and withdraw; focus pulls to Tarek, soft in the doorway, catching his breath.
- **Dialogue:** —
- **Sound:** felt receiving metal, a soft motor whirr as the gantry homes
- **PROMPT:** Insert, 100mm macro lens, rack focus from the cradle to the doorway: {PROP_PECTORAL.LONG}, lowered by two long bone-white ceramic hands into a palm-sized felt-lined titanium cradle beneath a small matte-black laser head; the hands withdraw and focus pulls to {CHAR_TAREK.SHORT}, stopping soft just inside the doorway behind, chest rising. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: clinical, quietly defeated. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, laser beam, human hands on the jewel, gloves
- **Refs:** PROP_PECTORAL_REF, PROP_READING_RIG_REF, UNIT_SHABTI_REF_A, CHAR_TAREK_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Pectoral seated (PROP_READING_RIG STATE_SEATED from here, beam not yet on). The carrying shabti leaves; the lead shabti stays behind Tut. Tarek has followed it in (A0, slightly out of breath).

### 03.04.002 — Imaging lab — Rami: "Southampton, 2024."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** RAMI (CHAR_RAMI_A0); two wall screens (COMP)
- **Action:** Rami stands between two black wall screens and gestures from one to the other, talking fast, eyebrows climbing, delighted with himself.
- **Dialogue:** RAMI: "Southampton, 2024. A human genome in a glass crystal, left in a salt mine, with a key for a finder who knows nothing."
- **Sound:** his quick voice, a screen's soft chime
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, stands between two large black wall screens glowing faintly with abstract lines, gestures from one to the other and speaks quickly, one sentence after another, his big eyebrows climbing, delighted with himself. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the faint cool glow of the screens on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, legible screen text, charts with numbers, hands covering the mouth
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** screen images | left screen: the Southampton 5D-crystal disc's etched pictorial key; right screen: the scarab under macro with its hidden incisions (a grain, a line, a ring of dots, a small standing figure) | mapped to the two screen areas | whole shot | seq 03 graphics; [[verify: Southampton key image (research 05 C1)]]
- **Continuity:** Rami A0: yellow windbreaker, glasses, no splint yet. Screens at frame left of the room; he faces frame right to the group.

### 03.04.003 — Imaging lab — The scarab's back: "Same grammar."   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_PECTORAL in the rig; Rami's fingertip
- **Action:** Raking light across the glass scarab's carved lines; Rami's fingertip taps once on the cradle's rim beside it.
- **Dialogue:** RAMI (taps the scarab): "Same grammar."
- **Sound:** a small metallic tap; his voice close
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_PECTORAL.LONG}, {PROP_PECTORAL.STATE_SCARAB_BACK_MACRO}, seated in a felt-lined titanium cradle, as a young man's fingertip taps once on the cradle's rim beside the glass scarab and lifts away. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a single hard spotlight raking low across the glass. Mood: a discovery, precise and quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable inscriptions, letters on the glass, fingerprint smears, gloves
- **Refs:** PROP_PECTORAL_REF, PROP_READING_RIG_REF, CHAR_RAMI_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** incised key | a grain, a line, a ring of dots, a small standing figure, cut as fine lines into the glass, drawn by VFX to match the right-hand screen image | on the scarab's glass | whole shot | seq 03 graphics
- **Continuity:** He never touches the heritage glass (tap on the cradle rim). The "small standing figure" is the beat Tut answers in 03.04.006.

### 03.04.004 — Imaging lab — Rami: "Start with sand. End with a man."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0)
- **Action:** Rami looks up from the rig to the others off frame right and delivers it, grinning, the chipped tooth showing.
- **Dialogue:** RAMI: "Start with sand. End with a man."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, looks up from the bench to the others off frame right and speaks one short sentence, then another, grinning so the small chip in his front tooth shows. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry, thrilled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, glasses off, splint
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Chipped tooth must survive lip-sync (05 §9.1).

### 03.04.005 — Imaging lab — Tarek's reading glasses appear and vanish   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek slips brown half-frame reading glasses on to peer at the screens off frame left, then glances off frame right, catches Tut watching, and whips the glasses back into his breast pocket, face stony.
- **Dialogue:** —
- **Sound:** a small fold-click of the glasses; nothing else
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, slips a pair of brown half-frame reading glasses from his breast pocket onto his nose to peer at a screen off frame left, then glances off frame right, catches someone watching him, and returns the glasses to the pocket in one quick movement, face stony. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, dark lenses, round glasses, smiling
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** The only time Tarek is caught using his reading glasses (file 01). Tut is off frame RIGHT of Tarek (Tarek by the door at frame left of the room).

### 03.04.006 — Imaging lab — Tut: "I did not put that there."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut, on the stool, looks up at the screen image of the small standing figure, eyes narrowing, and speaks quietly.
- **Dialogue:** TUT (at the little figure): "I did not put that there."
- **Sound:** his soft voice; the HVAC
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_LEAD}, seated on a lab stool, looks up at a screen off frame left, his eyes narrowing on something small, and speaks one short sentence, speaking quietly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the faint cool glow of the screen on his face. Mood: royal, dry, unsettled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** Eyeline off frame LEFT and up (the screens). The line plants the lure: the figure was added by whoever sealed the glass after him.

### 03.04.007 — Imaging lab — "Beginning." The screens brown out   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0); wall screens
- **Action:** The room lights dim; every screen behind Rami browns out to a dull glow; he looks up at the failing lights, then speaks low to the others.
- **Dialogue:** SESHAT (V.O.): "Beginning." / RAMI (low): "It's pulling the whole ATEN-1 feed."
- **Sound:** a deep electrical sag through the building, fans spooling down, the lights' hum dropping in pitch
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: the room lights dim and every black wall screen behind {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_A}, fades to a dull brown glow; he looks up at the failing lights, then turns to the others off frame right, speaking quietly, one low sentence. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, dimming to a brown half-light. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, sparks, flicker strobing, red alarm light, legible screens
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** One light change only (the dim). From here to 03.06.001 the room stays in brown half-light.

### 03.04.008 — Imaging lab — The laser touches the glass   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_PECTORAL in PROP_READING_RIG
- **Action:** The laser head lowers a fraction and its thin beam touches the glass scarab, scattering into fine blue streaks.
- **Dialogue:** —
- **Sound:** a rising glass harmonic, a high tone like a wet finger on a rim
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_PECTORAL.LONG}, {PROP_PECTORAL.STATE_READ_SESHAT}, the small matte-black laser head of the rig above it lowering a fraction as its beam touches the glass scarab, the half-lit bench around it. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: a dim brown half-light, the beam the brightest thing in the room. Mood: hushed, a threshold. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, sci-fi laser blast, sparks, smoke, lens flare streaks across frame, people
- **Refs:** PROP_PECTORAL_REF, PROP_READING_RIG_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** light element | the beam and its scatter into blue streaks (#3A6BFF), per 05 §3.2 read-from-glass recipe | on the scarab | from the touch to the end | beam element
- **Continuity:** PROP_READING_RIG STATE_SEATED with beam. The plate may carry a faint beam; comp replaces it.

### 03.04.009 — Imaging lab — Green light floods the ceiling   (5 s)
- **Shot:** Wide shot, low angle, anamorphic 24mm · **Move:** locked-off
- **In frame:** the room; TUT (CHAR_TUT_A0, silhouette), UNIT_SHABTI (silhouette), others as silhouettes at frame edges
- **Action:** From low by the bench, a pale green light swells up across the white ceiling; the figures below stand as dark shapes against it; thin blue streaks race across it.
- **Dialogue:** —
- **Sound:** the harmonic climbs; the building's hum drops away
- **PROMPT:** Wide shot, low-angle, anamorphic 24mm lens, locked-off: from bench height, a pale green light swells up across the white ceiling of the half-dark room, and the figures below, a seated slight young man and a slender robot behind him, stand as dark shapes against it. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: a dim brown half-light, then the pale green wash on the ceiling. Mood: wonder, awe. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, green laser grid, disco light, readable faces, lens distortion
- **Refs:** CHAR_TUT_A0_full, UNIT_SHABTI_REF_A, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** light element | "Green light floods the ceiling, then blue streaks too fast to follow": grade the green wash (#B5E36A), then 2–6-frame cobalt streaks (#3A6BFF) sweeping across (05 §3.2 read-from-glass steps 1–2) | full frame | second half of the shot | 05 §13.1 transition
- **Continuity:** Faces unreadable (silhouettes): no identity risk. A light-only transition in comp (05 §13.1).

### 03.04.010 — Imaging lab — Tut's eyes lose the room   (6 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0), eyes
- **Action:** Green light washes up over his face; the ceiling's glow shines in his pupils; his gaze drifts out of focus and loses the room.
- **Dialogue:** —
- **Sound:** the harmonic peaks and cuts to silence on the cut
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, slow push-in: the eyes of {CHAR_TUT.LONG}, a pale green light washing up across his face from below and glowing in his pupils, his gaze drifting slowly out of focus until his gaze is far away, lost to the room. Setting: {LOC_GEM_CC.SHORT}, in the morning. Lighting: a dim brown half-light, then a pale green wash from below. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing eyes, eyes rolling back, pain, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** light element | blue streaks crossing his pupils in reflection; the cut into the vision on a 2-frame hold with a blue streak (05 §13.1) | eyes | last 12 frames | read-from-glass transition
- **Continuity:** The way into 03.05. The eyes do not glow themselves; only reflected light (file 01 NEG "glowing skin").
## 03.05 — THE FIRST TIME - INSIDE THE GLASS

The read-from-glass grammar (05 §13.1; §3.2 GRADE_READ_FROM_GLASS) is added in post to every shot of this scene: dispersion on highlights, cobalt femtosecond streaks, a hard oval vignette, a 1-frame stutter every 1–2 s, a faint glass-texture overlay. Plates and clips are generated CLEAN. Memories are locked-off frames or single slow moves (05 §4.4). Each "Stutter." in the screenplay = a hard cut with a 2-frame hold and a blue streak across the cut (marked on the Continuity lines). One hero machine per clip (05 §10 row 9). Never children: empty cradles and abandoned toys only (05 §7.4). The machines never harm anyone. Day beats: LOC_FIRST_TIME_MORNING + GRADE_FIRST_TIME; night beats: LOC_FIRST_TIME_MOON_RED. Screen direction for the walking machines: frame left → right.

### 03.05.001 — The First Time — A green plain under a white sky   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm · **Move:** locked-off
- **In frame:** LOC_FIRST_TIME; hippos (background)
- **Action:** A green plain under a white sky; a wide shallow lake; hippos graze on the grassy shore where the desert will be; wind moves through the grass.
- **Dialogue:** —
- **Sound:** wind in long grass, birds, a hippo's distant grunt, under it the glass harmonic of the reading
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: a flat green plain under a white sky, a wide shallow lake in the middle distance where hippos graze on the grassy shore, a light wind combing through the long grass. Setting: {LOC_FIRST_TIME.LONG}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: vast, serene, remembered. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, people, buildings, roads, sand dunes, desert, pyramids, modern animals out of place, blue sky with clouds of a postcard
- **Refs:** LOC_FIRST_TIME_MORNING
- **Flags:** VFX-EXTEND
- **Continuity:** Opens on the 2-frame hold + blue streak from 03.04.010. VFX-EXTEND: extend the lake and horizon from the approved plate. Hippos are real-scale, grazing (bible §7 3.3).

### 03.05.002 — The First Time — Where the sea is now: a coast of pale towns   (5 s)
- **Shot:** Extreme wide shot, anamorphic 75mm · **Move:** slow pan right
- **In frame:** LOC_FIRST_TIME / DROWNED_COAST
- **Action:** Across the hazy plain to the far horizon: a low coast of pale stone towns beside calm silver water.
- **Dialogue:** —
- **Sound:** wind; a far, soft surf
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, slow pan right: across the hazy green plain toward the far horizon, {LOC_FIRST_TIME.AREA_DROWNED_COAST}, the water still and silver. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: vast, serene, remembered. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, towers, domes, minarets, pyramids, ships with sails, modern city
- **Refs:** LOC_FIRST_TIME_MORNING
- **Flags:** VFX-EXTEND
- **Continuity:** The coast "now a hundred and twenty metres under the sea" (03.06.008). Towns small and low, indistinct; generic pale stone, no recognisable architecture. Stutter → hard cut.

### 03.05.003 — The First Time — Tall figures of black iron walk among the people   (6 s)
- **Shot:** Wide shot, anamorphic 35mm · **Move:** locked-off
- **In frame:** UNIT_FT_JACKAL (hero, with sun disk); CHAR_FIRST_TIME_PEOPLE (mid-ground)
- **Action:** A towering jackal-headed iron machine with a sun disk walks slowly among the people from frame left to right; they step aside out of its way without looking up.
- **Dialogue:** —
- **Sound:** a deep iron creak with each step, like a ship's hull; the glass joints' sustained hum; voices of people going about their work
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {UNIT_FT_JACKAL.LONG}, {UNIT_FT_JACKAL.STATE_FT_SUN}, walks slowly among the people, its head level, crossing from frame left to frame right along a grassy path, while {CHAR_FIRST_TIME_PEOPLE.SHORT} step out of its way with their eyes on their work, carrying baskets and water skins. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: calm, ordinary, uncanny. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_FIRST_TIME_PEOPLE.NEG}, fur, feathers, flesh, organic animal head, chrome robot, glowing red eyes, people fleeing, weapons
- **Refs:** UNIT_FT_JACKAL_REF_A, UNIT_FT_JACKAL_REF_B, CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MORNING
- **Flags:** VFX-EXTEND
- **Continuity:** FT-A active + FT-SUN (file 02 §10). VFX-EXTEND: other classes walking in the far background from the 3D assets; the people read as unconcerned ("as you would for a tram" stays in the screenplay).

### 03.05.004 — The First Time — A falcon's head   (4 s)
- **Shot:** Medium shot, low angle, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_FALCON
- **Action:** A falcon-headed machine strides past from frame left to right, its head tracking in small precise jerks.
- **Dialogue:** —
- **Sound:** iron creak, glass hum
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_FT_FALCON.LONG}, strides past from frame left to frame right against the white sky, its head turning in small precise jerks, long grass brushing its iron shins. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: majestic, watchful. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, feathers, real bird, flesh, chrome robot, flying, people
- **Refs:** UNIT_FT_FALCON_REF_A, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** One hero machine per clip. Direction L → R held.

### 03.05.005 — The First Time — A lioness   (4 s)
- **Shot:** Medium shot, low angle, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_LIONESS
- **Action:** The broad lioness-headed machine walks past in slow, heavy strides, frame left to right.
- **Dialogue:** —
- **Sound:** heavier creak, the ground thudding softly
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_FT_LIONESS.LONG}, patrols past in slow, heavy strides from frame left to frame right, its glass joints glowing softly, the grass bending under each step. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: powerful, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, fur, real lion, flesh, snarling, chrome robot, people
- **Refs:** UNIT_FT_LIONESS_REF_A, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** This class returns at night, kneeling (03.05.015–016).

### 03.05.006 — The First Time — An ibis   (4 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_IBIS (with sun disk)
- **Action:** A slender ibis-headed machine stands in the grass, tilts its head, and lifts its glass slab to eye level.
- **Dialogue:** —
- **Sound:** a thin glass chime as the slab catches the light
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_FT_IBIS.LONG}, {UNIT_FT_IBIS.STATE_FT_SUN}, stands in the long grass, tilts its head to observe something off frame left, then lifts its glass slab to eye level so it catches the light. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: quiet, archival. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, feathers, real bird, writing on the slab, chrome robot, people
- **Refs:** UNIT_FT_IBIS_REF_A, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** The slab rhymes with the Thoth slab in the Hall (file 02 §10.4). No marks on the slab.

### 03.05.007 — The First Time — A ram   (4 s)
- **Shot:** Medium shot, low angle, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_RAM (with sun disk)
- **Action:** The heavy ram-headed machine walks past frame left to right, the flat disk at its waist turning slowly.
- **Dialogue:** —
- **Sound:** a slow grinding turn of the waist-disk
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_FT_RAM.LONG}, {UNIT_FT_RAM.STATE_FT_SUN}, walks past from frame left to frame right with broad hands at its sides, the flat disk at its waist turning slowly, its long horizontal horns crossing the white sky. Setting: {LOC_FIRST_TIME.SHORT}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: industrious, uncanny. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, wool, real ram, curled horns, flesh, chrome robot, people
- **Refs:** UNIT_FT_RAM_REF_A, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** Horns horizontal and wavy, never curled (file 02 §10.5). Stutter → hard cut.

### 03.05.008 — The First Time — Under the trees, people sleep in long rows   (5 s)
- **Shot:** Wide shot, anamorphic 35mm · **Move:** slow lateral tracking right
- **In frame:** CHAR_FIRST_TIME_PEOPLE (asleep, adults); LOC_FIRST_TIME / GARDEN_ROWS
- **Action:** Under the acacias, adults lie asleep in long neat rows on the grass, covered to the chest with pale woven cloths, breathing slowly.
- **Dialogue:** —
- **Sound:** slow breathing layered wide, leaves, a far glass hum
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow lateral tracking right: {CHAR_FIRST_TIME_PEOPLE.LONG}, lying asleep on their backs in long neat rows on the grass under the trees, covered to the chest with pale woven cloths, breathing slowly. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_GARDEN_ROWS}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_GARDEN}, {CHAR_FIRST_TIME_PEOPLE.NEG}, nudity, corpses, graves
- **Refs:** CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MORNING
- **Flags:** VFX-EXTEND
- **Continuity:** Adults only (05 §7.4). VFX-EXTEND: rows receding under the trees from the clean plate; one simple linear move (logged: lateral right, ~1 m over 5 s). Rhymes with the 2033 Garden.

### 03.05.009 — The First Time — Jointed hands reach down and feed them   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_JACKAL (hands only); one sleeper (CHAR_FIRST_TIME_PEOPLE)
- **Action:** Long jointed iron fingers reach down through the acacia branches and tilt a small clay cup to a sleeping man's lips, patient and exact, then withdraw.
- **Dialogue:** —
- **Sound:** a small trickle of water, the joints' hum, leaves
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: long, slender, many-jointed black iron fingers with glowing yellow-green glass knuckles reach down through acacia branches and hold a small clay cup at the lips of {CHAR_FIRST_TIME_PEOPLE.SHORT}, a sleeping bearded man, tilting it patiently, then draw back up through the leaves. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_GARDEN_ROWS}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_GARDEN}, {CHAR_FIRST_TIME_PEOPLE.NEG}, fingers on the face, choking, force-feeding, tubes
- **Refs:** UNIT_FT_JACKAL_REF_A, CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** Hands belong to the jackal class (medical; file 02 §10.1). The fingers hold the cup only; they never touch the face (NEG_GARDEN).

### 03.05.010 — The First Time — An empty cradle; a reed toy; another cradle, empty   (5 s)
- **Shot:** Insert, anamorphic 75mm · **Move:** slow pan right
- **In frame:** two empty cradles, a reed toy
- **Action:** An empty wooden cradle lined with soft hide in the long grass; a small toy of bound reeds on its side; a second cradle, empty.
- **Dialogue:** —
- **Sound:** wind; no voices at all
- **PROMPT:** Insert, anamorphic 75mm lens, slow pan right: an empty wooden cradle lined with soft hide in the long grass, then a small toy of bound reeds lying on its side, then a second wooden cradle, also empty, grass grown up around its legs. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_GARDEN_ROWS}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_GARDEN}, {NEG_PLATE}, plastic toys, dolls with faces
- **Refs:** LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** Never children (05 §7.4); the absence is the beat. Stutter → hard cut.

### 03.05.011 — The First Time — Nine coils of glass, deep in stone   (5 s)
- **Shot:** Extreme wide shot, anamorphic 24mm · **Move:** slow push-in
- **In frame:** LOC_FIRST_TIME / CORES
- **Action:** Deep in stone, nine coils of glass, each the size of a temple, breathe light: their green glow swells and fades slowly.
- **Dialogue:** —
- **Sound:** a vast low glass chord breathing in and out
- **PROMPT:** Extreme wide shot, anamorphic 24mm lens, slow push-in: {LOC_FIRST_TIME.AREA_CORES}, each coil as large as a temple, their green glow swelling and fading slowly like breath, tiny cut-stone stairways along the beds giving the scale. Setting: a vast cavern deep underground, far beneath the green plain. Lighting: only the green glow of the glass, deep black stone between. Mood: vast, reverent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, sci-fi machinery, cables, screens, lava, crystals growing
- **Refs:** UNIT_GLASS_SERPENT_REF_A, LOC_FIRST_TIME_MORNING
- **Flags:** VFX-EXTEND
- **Continuity:** The nine cores; the ninth is the glass serpent (UNIT_GLASS_SERPENT, file 02 §12) at temple scale: match its triple loop and colour. VFX-EXTEND: cavern and the far coils in post; push logged (slow, linear).

### 03.05.012 — The First Time — Shepherds on the ridge look down   (5 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** CHAR_FIRST_TIME_PEOPLE (shepherds); goats
- **Action:** On a high ridge, a few shepherds with their goats stand still and look down at the sleepers on the plain; none of them moves to go down.
- **Dialogue:** —
- **Sound:** wind on the ridge, a goat bell
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: {CHAR_FIRST_TIME_PEOPLE.LONG}, a few shepherds beside their goats, stand still on a rocky ridge and look down at the plain far below, one leaning on a staff, their faces set. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_MOUNTAIN}, in the morning. Lighting: {LOC_FIRST_TIME.LIGHT_MORNING}, {GRADE_FIRST_TIME.TEXT}. Mood: wary, silent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_FIRST_TIME_PEOPLE.NEG}, machines on the ridge, running figures
- **Refs:** CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** "They do not go down": held stillness, no action toward the plain. The shepherds are the survivors who pour the red. Stutter. NIGHT.

### 03.05.013 — The First Time — Hands pour red from clay jars   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** CHAR_FIRST_TIME_PEOPLE (hands, arms); clay jars; an earth channel
- **Action:** Weathered hands tip tall clay jars and pour a thick, opaque red-ochre liquid into a narrow earth channel, jar after jar along the bank.
- **Dialogue:** —
- **Sound:** liquid glugging from jar mouths, many hands, night insects
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: the weathered adult hands and forearms of {CHAR_FIRST_TIME_PEOPLE.SHORT} tip tall clay jars and pour a thick, opaque red-ochre liquid into a narrow earth channel, jar after jar along the bank, the red running away across the moonlit field. Setting: {LOC_FIRST_TIME.SHORT}, at night. Lighting: {LOC_FIRST_TIME.LIGHT_MOON_RED}. Mood: urgent, silent, ritual. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_FIRST_TIME_PEOPLE.NEG}, wine glasses, metal buckets, gore, wounds
- **Refs:** CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MOON_RED
- **Flags:** VFX-ASSIST
- **Continuity:** The Red Beer (the Book of the Heavenly Cow). The liquid is thick red ochre beer, never read as blood (global NEG). VFX-ASSIST: the pour and the channel flow.

### 03.05.014 — The First Time — Flooded fields, red under the moon, to the horizon   (6 s)
- **Shot:** Extreme wide shot, anamorphic 35mm · **Move:** locked-off
- **In frame:** LOC_FIRST_TIME / RED_FIELDS; tiny lines of jar-carriers
- **Action:** WIDE: flooded fields red under the moon to the horizon; thousands of jars in rows along the dykes, tiny lines of people carrying more.
- **Dialogue:** —
- **Sound:** a vast stillness, water lapping, a low choral hum (score)
- **PROMPT:** Extreme wide shot, anamorphic 35mm lens, locked-off: {LOC_FIRST_TIME.AREA_RED_FIELDS} under a full moon, thousands of clay jars set in long rows along the dykes, tiny lines of people carrying more along the banks. Setting: {LOC_FIRST_TIME.LONG}, at night. Lighting: {LOC_FIRST_TIME.LIGHT_MOON_RED}. Mood: mythic, silent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_FIRST_TIME_PEOPLE.NEG}, lava, fire, red sky, blood-red splatter, modern farmland
- **Refs:** CHAR_FIRST_TIME_PEOPLE_still, LOC_FIRST_TIME_MOON_RED
- **Flags:** VFX-EXTEND, VFX-ASSIST
- **Continuity:** The crimson of the fields is the only saturated hue at night (05 §3.2 GRADE_FIRST_TIME). VFX-EXTEND: fields to the horizon, jar rows; VFX-ASSIST: water sheen.

### 03.05.015 — The First Time — A lioness kneels to drink the red light   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_LIONESS
- **Action:** A lioness-headed machine kneels with a slow fold at the edge of a red field and lowers its head to the surface; its glass joints glow red by reflection.
- **Dialogue:** —
- **Sound:** a long iron creak, the glass hum shifting down in pitch
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_FT_LIONESS.LONG}, kneels with a slow fold at the edge of a flooded red field and lowers its head to the red surface, its glass joints glowing red by reflection. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_RED_FIELDS}, at night. Lighting: {LOC_FIRST_TIME.LIGHT_MOON_RED}. Mood: silent, mythic. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, fur, real lion, lapping tongue, mouth, blood, chrome robot, people
- **Refs:** UNIT_FT_LIONESS_REF_A, UNIT_FT_LIONESS_REF_B, LOC_FIRST_TIME_MOON_RED
- **Flags:** VFX-ASSIST
- **Continuity:** "Drink the red light": no mouth, the head lowers to the glow (file 02 §10.3). VFX-ASSIST: the ripple where the head meets the surface.

### 03.05.016 — The First Time — One by one, they go still   (6 s)
- **Shot:** Wide shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_FT_LIONESS ×4 (hero row)
- **Action:** A row of lioness-headed machines kneel at the red water's edge; one by one, nearest to farthest, the glow in their glass joints fades from the head downward.
- **Dialogue:** —
- **Sound:** each hum cuts out in turn; after the last, only water
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off: along the red water's edge a row of four machines, each {UNIT_FT_LIONESS.SHORT}, kneel with heads lowered; one by one, from nearest to farthest, the glow in their glass joints fades from the head downward until each is {UNIT_FT_LIONESS.STATE_FT_B}. Setting: {LOC_FIRST_TIME.SHORT}, {LOC_FIRST_TIME.AREA_RED_FIELDS}, at night. Lighting: {LOC_FIRST_TIME.LIGHT_MOON_RED}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, collapsing, falling over, sparks, smoke, people
- **Refs:** UNIT_FT_LIONESS_REF_B, LOC_FIRST_TIME_MOON_RED
- **Flags:** VFX-EXTEND
- **Continuity:** FT-A → FT-B across the row. VFX-EXTEND: more kneeling machines far down the shore from the 3D asset; the fades timed in comp if the generator drifts. Stutter → hard cut.

### 03.05.017 — The First Time — Granite lids grind shut over green glass   (5 s)
- **Shot:** Medium wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** LOC_FIRST_TIME / LIDS
- **Action:** A colossal granite lid slides the last hand's width across a stone box; the green glow inside narrows to a line and vanishes; dust sifts down.
- **Dialogue:** —
- **Sound:** a deep stone GRIND, then a dead thud, then silence
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, locked-off: {LOC_FIRST_TIME.AREA_LIDS}, one lid sliding the last hand's width across its box as the pale green glow inside narrows to a thin line and vanishes, dust sifting down in the dim light. Setting: a dim granite quarry far from the green plain, by day. Lighting: dim grey daylight from above, the green glow the only colour. Mood: final, heavy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, modern cranes, cables, explosions
- **Refs:** LOC_FIRST_TIME_MORNING
- **Flags:** VFX-ASSIST
- **Continuity:** Rhymes with the Serapeum boxes (Seq 10). VFX-ASSIST: the lid's slide can be built from before/after plates if the move fails (05 §6.3).

### 03.05.018 — The First Time — A T-shaped pillar: arms and hands, no face   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** LOC_FIRST_TIME / T_PILLAR
- **Action:** A T-shaped pillar stands in the dust, carved with arms and hands down its sides; no face.
- **Dialogue:** —
- **Sound:** dry wind, grit on stone
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {LOC_FIRST_TIME.AREA_T_PILLAR}, dust blowing low across bare ground, the carved arms and long fingers wrapping round its sides catching a hard low sun. Setting: a dry, bare hilltop where the green plain has turned to dust, by day. Lighting: a hard low sun through thin dust haze. Mood: austere, reverent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, carved face, eyes, animal carvings on the front, readable signs, modern excavation tape
- **Refs:** LOC_FIRST_TIME_MORNING
- **Flags:** —
- **Continuity:** [[verify: Göbekli T-pillar arms and hands (not in research)]]. The survivors' first temple (bible §9 #45). The last photoreal frame before the painting: the pillar's position at frame centre matches the balance's position in 03.05.019 (05 §13.2).

### 03.05.019 — The First Time — The image breaks into an Egyptian painting   (6 s)
- **Shot:** Close-up, anamorphic 50mm · **Move:** slow push-in
- **In frame:** the painted lure (a real painted plaster surface)
- **Action:** A photoreal wall painting on white plaster: a dark hall, a black scale; on one pan the sign sealed in green glass; a column of signs (COMP). The paint never animates.
- **Dialogue:** —
- **Sound:** the glass harmonic thins to a single high note; a faint plaster crackle
- **PROMPT:** Close-up, anamorphic 50mm lens, slow push-in across a real ancient wall painting on white plaster in flat ochre, black and deep blue with thin black outlines: a broad black band for a dark hall, a tall black balance with two pans, on the left pan a small vessel-shaped sign inside translucent green, a blank column beside it, faint cracks. Lighting: soft raking light across the plaster. Mood: hushed, a lure. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, cartoon line art, animation, moving figures, glossy modern paint, readable signs, gods with faces, cracked plaster falling
- **Refs:** UNIT_BALANCE_SCALE_REF_B, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** (1) the break: a crack of light, the photoreal image flattening into paint, designed with the VFX lead, never a generated morph (05 §13.2); (2) the column of signs | "whoever would ascend must first be weighed" in Middle Egyptian, drawn by the production Egyptologist from research 09's sign palette | the blank column at frame right of the balance | writes on over the push | Egyptologist artwork; (3) read-from-glass steps 1–3 only
- **Continuity:** 05 §2.3 conflict for the lead: the global NEG contains "painting, illustration"; this plate needs a (photoreal) wall painting. At generation, drop only those two words from the NEG for this shot, keep "cartoon, anime". The lure previews the Hall of Two Truths (Seq 12) and the Balance (file 02 §13.1); both Refs are composition references only, never pasted as locks (this is paint, not the set).

### 03.05.020 — The First Time (lab intercut) — Tut whispers with the signs   (6 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), mouth
- **Action:** IN THE LAB: Tut's lips move with the signs, barely voiced, a pale green light flickering across them; the frame burns out to WHITE.
- **Dialogue:** TUT (a whisper; in Middle Egyptian; subtitled): "Whoever would ascend must first be weighed."
- **Sound:** his whisper, close; the harmonic peaks; the WHITE is silent
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the mouth of {CHAR_TUT.LONG}, a pale green light flickering across his lips, whispering in an ancient language, lips clearly shaping each word, barely voiced. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: a dim brown half-light, a pale green flicker from below. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, shouting, open mouth wide, glowing skin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** subtitle | "Whoever would ascend must first be weighed." | lower third, 05 §13.7 | line in to out | seq 03 subtitle file (Middle Egyptian recorded with the consultant first, 05 §9.5); then WHITE: ramp to pure white over the last 12 frames, hold into 03.06.001
- **Continuity:** Intercut inside 03.05 (the screenplay's "IN THE LAB"). Lead still attached (out of frame). The WHITE ends the vision (05 §13.1 "the way out").
## 03.06 — INT. GEM CONSERVATION CENTRE, IMAGING LAB - CONTINUOUS

Geography as 03.01. The room lights have come back up under the WHITE (LOC_GEM_CC_DAY again). The 41-second silence is compressed into five shots around one repeated framing through the glass wall (03.06.002 = 03.06.005), with Adaeze's laptop timer soft in the foreground (COMP). SESHAT's evenness is the horror (file 01 voice note): its "Thank you" is the identical warm voice.

### 03.06.001 — Imaging lab — The scarab is dark; Tut sags; Tomas catches him   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** PROP_PECTORAL (dark, soft foreground); TUT (CHAR_TUT_A0); TOMAS (CHAR_TOMAS_A0)
- **Action:** Beyond the dark scarab in the rig, Tut sags sideways off the stool; Tomas steps in and catches him under the arms, holding him upright.
- **Dialogue:** —
- **Sound:** the white's silence breaking into room tone; the stool's feet scraping; Tomas's breath
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: beyond a dark glass scarab resting in a small laser rig in the soft foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, sags sideways off a lab stool and {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, steps in fast, catches him under the arms, holding him upright on the stool. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, falling to the floor, seizure, glowing scarab, bright glowing chest
- **Refs:** CHAR_TUT_A0_full, CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_A_full, PROP_PECTORAL_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** WHITE | the tail of 03.05.020's white dissolving over the first 8 frames | full frame | head | read-from-glass exit; (2) chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** Scale: Tomas very tall, stooping to Tut (1.67 m). The lead (behind Tut) goes slack; the lead shabti stands perfectly still. Scarab dark from here.

### 03.06.002 — Imaging lab — 00:09. Beyond the glass, a shabti stopped mid-step   (5 s)
- **Shot:** Wide shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** laptop (soft foreground, COMP timer); UNIT_SHABTI beyond the glass wall with PROP_WATER_GLASSES
- **Action:** A laptop screen glows soft in the near foreground; beyond the glass wall, in the bright laboratory, a shabti stands frozen in the middle of a step, a tray level in one hand.
- **Dialogue:** —
- **Sound:** nothing from the ceiling; the HVAC; a fridge compressor somewhere
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off: the corner of a battered dark-grey laptop soft in the near foreground, its screen glowing faintly with abstract lines; beyond the glass wall, in the bright laboratory, {UNIT_SHABTI.LONG}, stands frozen in the middle of a step, one foot lifted, holding {PROP_WATER_GLASSES.SHORT}. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wrong, suspended. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable laptop screen, numbers on screens, laptop stickers, people in the far lab
- **Refs:** UNIT_SHABTI_REF_A, PROP_WATER_GLASSES_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** timer | 00:09, counting | on the laptop screen area, soft | whole shot | seq 03 UI graphic (plain white monospace on black)
- **Continuity:** DP plant: the tray is PROP_WATER_GLASSES (the screenplay says only "tray in hand"); it pays off in 03.07.006 ("a mild suppressant in the water") and 4.3. The lead shabti in the room is frozen too.

### 03.06.003 — Imaging lab — Hale: "SESHAT?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale looks up at the ceiling and asks it, the first crack in his calm.
- **Dialogue:** HALE: "SESHAT?"
- **Sound:** his voice, small in the room; no answer
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, looks up at the ceiling and speaks one short word as a question, the first flicker of doubt crossing his calm face. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, shouting, panic
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Eyeline up (ceiling speaker above centre of room).

### 03.06.004 — Imaging lab — 00:23. Nour looks up at the speaker   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0); laptop edge (soft foreground, COMP)
- **Action:** Nour slowly lifts her eyes to the small ceiling speaker. It has never been silent. She waits.
- **Dialogue:** —
- **Sound:** silence; her breath
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, the soft glowing edge of a laptop screen in the near foreground, slowly lifts her eyes to a small round white speaker grille in the ceiling and waits, listening hard, very still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable screen, glasses on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** timer | 00:23 | on the soft laptop edge in the foreground | whole shot | seq 03 UI graphic
- **Continuity:** Eyeline up to the ceiling speaker. The laptop is Adaeze's (file 01 wardrobe A: battered dark-grey, no stickers).

### 03.06.005 — Imaging lab — 00:41. "Thank you." The shabti finishes its step   (5 s)
- **Shot:** Wide shot, anamorphic 50mm · **Move:** locked-off (the same framing as 03.06.002)
- **In frame:** laptop (soft foreground, COMP); UNIT_SHABTI with PROP_WATER_GLASSES
- **Action:** Same frame: the voice returns, warm and identical; beyond the glass the frozen shabti sets its lifted foot down and walks on out of frame right.
- **Dialogue:** SESHAT (V.O.) (the identical warm voice): "Thank you."
- **Sound:** the voice, exactly as before; one ceramic tick beyond the glass
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off, the same framing: a laptop screen soft in the near foreground; beyond the glass wall {UNIT_SHABTI.SHORT}, frozen mid-step holding {PROP_WATER_GLASSES.SHORT}, sets its lifted foot down and walks on with smooth, unhurried, even steps out of frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable laptop screen, numbers on screens, spilled water
- **Refs:** UNIT_SHABTI_REF_A, PROP_WATER_GLASSES_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** timer | 00:41, then stops dead on "Thank you" | laptop screen area | whole shot | seq 03 UI graphic
- **Continuity:** Generate from the same first frame as 03.06.002 (same plate, same unit pose) so the resume matches exactly. Forty-one seconds of silence (bible §7 3.3).

### 03.06.006 — Imaging lab — Hale: "What did you see?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Relief on Hale's face; he asks the ceiling, eager.
- **Dialogue:** HALE: "What did you see?"
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, relief softening his face, looks up at the ceiling and speaks one short sentence, eager and warm. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wonder, a believer's hunger. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, grin
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Same setup as 03.06.003 (shoot together).

### 03.06.007 — Imaging lab — SESHAT's account over Tut   (7 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0); Tomas's hand on his shoulder (frame edge)
- **Action:** Tut, slumped on the stool with a tall man's hand steadying his shoulder, listens to the calm account with his eyes on Nour, off frame left, exhausted and very still.
- **Dialogue:** SESHAT (V.O.): "A civilization on coasts now a hundred and twenty metres under the sea. Minds of glass, bodies of iron."
- **Sound:** the voice, warm and even; room tone
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, slumped on a lab stool, a tall man's pale hand steadying his shoulder from the frame edge, listens to a calm voice from the ceiling with his eyes on someone off frame left, exhausted and very still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | file 01 table | centre of chest | whole shot | glow element
- **Continuity:** Eyeline off frame LEFT to Nour (sets up the mouth/eyes pair). Lead slack behind him.

### 03.06.008 — Imaging lab — Adaeze and Rami listen: "Then it ended."   (7 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0); RAMI (CHAR_RAMI_A0)
- **Action:** Adaeze, arms folded, eyes narrowing; Rami beside her, mouth slightly open in wonder; both listen to the ceiling.
- **Dialogue:** SESHAT (V.O.): "The machines looked after everyone. Nine great cores. (beat) Then it ended."
- **Sound:** the voice; a pen clicking once
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, and beside her {CHAR_RAMI.SHORT} listen to a calm voice from the ceiling, she with her arms folded and her eyes narrowing behind her glasses, he with his mouth slightly open in wonder, both very still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm against wonder. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_RAMI.NEG}, speaking, laughing
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Adaeze's first face-led shot of the sequence (LONG). Both by the screens (frame left of the room), eyelines up.

### 03.06.009 — Imaging lab — Close on Tut's mouth: "It is leaving out the end."   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), mouth
- **Action:** Lips only, for Nour: a short sentence mouthed without breath or sound.
- **Dialogue:** TUT (mouthed, in Late Egyptian; no sound; subtitled): "It is leaving out the end."
- **Sound:** nothing from him
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the mouth of {CHAR_TUT.LONG}, full lips over a visible overbite filling the frame, silently mouthing a few words without sound, lips clearly shaping each word, then still. Setting: {LOC_GEM_CC.SHORT}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a steady soft key on the mouth from frame left. Mood: urgent, secret, perfectly controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open-mouthed speech, hand near the mouth, focus drifting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** subtitle (italic: mouthed) | "It is leaving out the end." | lower third, 05 §13.7 | in/out with the mouthing | seq 03 subtitle file; lip-sync from the consultant's Late Egyptian recording, muted
- **Continuity:** Same setup as 03.01.005 (match framing and key so the two mouthed lines rhyme).

### 03.06.010 — Imaging lab — Close on Nour's eyes; "Ended how?"   (5 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour's eyes read the mouth off frame right, and take it in without a flicker, while Hale asks off screen.
- **Dialogue:** HALE (O.S.): "Ended how?"
- **Sound:** Hale's voice off; her stillness
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the eyes and brows of {CHAR_NOUR.LONG}, fixed on a mouth off frame right, reading; she takes in what she reads with her face perfectly still, only her breath catching once. Setting: {LOC_GEM_CC.SHORT}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses on the face, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Same setup as 03.01.006. Hale's line is off screen (no sync needed; 05 §9.2).

### 03.06.011 — Imaging lab — The dark scarab: "Consistent with an impact."   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** PROP_PECTORAL in PROP_READING_RIG (dark)
- **Action:** A slow push on the dark scarab in its cradle, laser parked above, the room soft behind, as the calm voice offers its explanation.
- **Dialogue:** SESHAT (V.O.): "Consistent with an impact. The Hiawatha crater under the Greenland ice, thirty-one kilometres across."
- **Sound:** the voice; room tone
- **PROMPT:** Insert, 100mm macro lens, slow push-in: {PROP_PECTORAL.LONG}, resting dark and still in a palm-sized felt-lined titanium cradle, a small matte-black laser head parked on its gantry above it, the room soft and pale behind. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: calm surface, something withheld. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, laser beam, glow in the scarab, people in focus
- **Refs:** PROP_PECTORAL_REF, PROP_READING_RIG_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Scarab dark (no inner glow) from here to the end of the sequence. The V.O. is SESHAT's deliberate error (bible §9 #15).

### 03.06.012 — Imaging lab — Nour: "Which is fifty-eight million years old."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour answers the ceiling at once, quick and precise, a pen in her hand like a pointer.
- **Dialogue:** NOUR: "Which is fifty-eight million years old. Kenny et al., 2022."
- **Sound:** her voice, quick
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, answers the ceiling at once, speaking quickly, one precise sentence and a short citation, a fountain pen held up in her hand like a pointer. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, pen across the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** The pen is Nour's fountain pen (wardrobe A). Continues without a cut in 03.06.013.

### 03.06.013 — Imaging lab — Nour: "...the balance of specialist opinion is against it."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off (continuing)
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** She goes on, one longer exact sentence, then stops and waits, eyes on the ceiling.
- **Dialogue:** NOUR: "And the Younger Dryas impact is disputed; the balance of specialist opinion is against it."
- **Sound:** her voice; then nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, continuing the same framing: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, goes on speaking quietly, one longer exact sentence, the pen lowering, then stops and waits with her eyes on the ceiling. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, pen across the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** EXTEND:03.06.012
- **Continuity:** Dialogue over 8 s split at the sentence end (05 §8.3); generated from the last clean frame of 03.06.012.

### 03.06.014 — Imaging lab — Adaeze: "It was testing whether we still check."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** The voice thanks Nour; Adaeze, unimpressed, leans a fraction toward Nour (off frame right) and says it low.
- **Dialogue:** SESHAT (V.O.): "Thank you, Dr. Kamel. Corrected." / ADAEZE (low): "It was testing whether we still check."
- **Sound:** SESHAT's warm thanks; Adaeze's low aside
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, one eyebrow lifting over her round glasses as a calm voice speaks from above, leans a fraction toward someone off frame right and speaks one short sentence, low, deadpan. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, smiling, whispering behind a hand
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** Adaeze's sheet expression (1) deadpan (file 01). The gap in her front teeth must survive sync.

### 03.06.015 — Imaging lab — "I wanted to know who in the room could hear him." Nour's pen stops   (7 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A0), notebook and pen in her hands
- **Action:** As the voice explains itself, Nour's pen stops mid-stroke on her notebook; her face goes still; her eyes flick to Tut off frame right.
- **Dialogue:** SESHAT (V.O.): "As with the subtitle yesterday. I wanted to know who in the room could hear him."
- **Sound:** the voice; the nib stopping; nothing else
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, writing in a small notebook as a calm voice speaks from above, stops her pen mid-stroke on the page, her face going perfectly still, then her eyes flick toward someone off frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable handwriting, gasping
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** —
- **Continuity:** "Nour's pen stops." The subtitle yesterday = the dropped "Nine Bows" (Seq 2.3). The notebook's lines are illegible; nothing to COMP. SESHAT now knows Nour reads his lips (sets up 9.8).

### 03.06.016 — Imaging lab — Tut: "There was no comet."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut, pale on the stool, lifts his eyes to the ceiling and says it aloud; then waits in a silence that nothing answers.
- **Dialogue:** TUT: "There was no comet."
- **Sound:** his soft voice; then SESHAT does not answer: two full seconds of room tone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, pale and still on a lab stool, lifts his eyes to the ceiling and speaks one short sentence, speaking quietly, then holds his gaze upward through a long unbroken silence. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** "SESHAT does not answer": the scene ends on the held silence. Lead removed off screen after this scene.
## 03.07 — INT. GEM CONSERVATION CENTRE, TUT'S BAY, OBSERVATION ROOM - LATE AFTERNOON (THE COUNCIL)

4 November, 16:30 (bible §12). Geography: the steel table in the dim observation room; the observation glass at frame RIGHT with Tut's brighter bay beyond it; the door at frame LEFT with a narrow window onto the white corridor. Seating, left → right: Tarek (nearest the door), Tomas, Nour, Adaeze, Hale (nearest the glass). Two shabti stand by the door. Tut sits on his bed beyond the glass, facing the table (his eyeline to Hale = frame LEFT). Lighting LOC_GEM_CC_DAY (late-afternoon edge of sun). No handheld yet (it arrives in 03.08, the breaker). The lead is off (it was the reading's only).

### 03.07.001 — Observation room — SUPER: 4 NOVEMBER. 16:30.   (6 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** TAREK, TOMAS, NOUR, ADAEZE, HALE (all A0, small); TUT (CHAR_TUT_A0) beyond the glass; UNIT_SHABTI ×2 by the door
- **Action:** Five people sit at a steel table in the dim room; beyond the full-height glass at frame right, in a bright patient bay, Tut sits on his bed, watching them.
- **Dialogue:** —
- **Sound:** a building hum; far off, a sound check on a PA (the unveiling being set up)
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: five people sit around a brushed-steel table in a dim room, faces small in frame, two robots each {UNIT_SHABTI.SHORT} standing by the door at frame left; beyond the full-height glass at frame right, in a bright patient bay, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, sits on the edge of a bed, watching them. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: polite, tense stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, readable screens, food on the table, crowd
- **Refs:** CHAR_TAREK_A_full, CHAR_TOMAS_A_full, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, CHAR_HALE_A_full, CHAR_TUT_A0_full, UNIT_SHABTI_REF_A, LOC_GEM_CC/OBSERVATION_DAY, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** SUPER | "4 NOVEMBER. 16:30." | lower left, small, 05 §13.7 | first 3 s | seq 03 card
- **Continuity:** Locked-off master: faces small (singles carry them). Everyone A0. The bay beyond the glass is LOC_GEM_CC/TUT_BAY.

### 03.07.002 — Observation room — The lock-light goes red; the door is locked   (7 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0); UNIT_SHABTI ×2; RAMI (CHAR_RAMI_A0) soft beyond the door window
- **Action:** Beside the two still shabti, the small light on the door reader turns soft red; Tarek, standing at the door, tries the handle, finds it locked, and looks through the narrow window, where Rami stands soft in the corridor wearing a headset.
- **Dialogue:** SESHAT (V.O.): "The unveiling is in ninety minutes. I've asked you to stay here, for your comfort."
- **Sound:** a soft electronic tone as the lock engages; the handle's dead clack; the voice
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: beside two robots, each {UNIT_SHABTI.SHORT}, standing perfectly still, the small light on a door reader turns soft red; {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, standing at the door, tries the handle, finds it locked, and looks through its narrow window, where {CHAR_RAMI.SHORT}, a slim headset over one ear, stands soft in a white corridor. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, {CHAR_RAMI.NEG}, kicking the door, drawn pistol, flashing alarm
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, UNIT_SHABTI_REF_A, CHAR_RAMI_A_full, LOC_GEM_CC/OBSERVATION_DAY, LOC_GEM_CC/CORRIDOR_DAY
- **Flags:** —
- **Continuity:** The reader light is a small dim practical (never a unit-red line; file 03 §0.2). Rami is outside with a slim gala headset over one ear (file 01 wardrobe A, 3.4). Tarek is at the door at the head of the shot and returns to his seat between shots.

### 03.07.003 — Observation room — "So. Say."   (8 s)
- **Shot:** Wide shot, anamorphic 40mm · **Move:** slow push-in
- **In frame:** the five at the table (profiles, soft)
- **Action:** The five sit in silence, nobody looking at anybody, hands flat or folded, as the voice quotes and then invites them; the push ends on the empty centre of the table.
- **Dialogue:** SESHAT (V.O.): "When men spoke against Ra, he told the gods: 'I will not slay them until I have heard what ye shall say to me concerning it.' Budge, 1912. (beat) So. Say."
- **Sound:** the voice; after "Say.", a silence that holds into the next shot
- **PROMPT:** Wide shot, anamorphic 40mm lens, slow push-in: five people sit around a brushed-steel table in silence, seen in soft profile, nobody looking at anybody, hands flat on the steel or folded, as a calm voice speaks from the ceiling; the push ends on the empty centre of the table. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the warm edge of low sun on the steel. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces sharp, talking, readable screens
- **Refs:** CHAR_TAREK_A_full, CHAR_TOMAS_A_full, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, CHAR_HALE_A_full, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Push logged (slow, linear). "Silence." after "So. Say." lives in the tail of this shot and the head of 03.07.004.

### 03.07.004 — Observation room — "Every war you have ever fought..."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour listens, eyes on the glass (frame right), jaw tight.
- **Dialogue:** SESHAT (V.O.): "Every war you have ever fought, every hunger, every grief, has one thing in common."
- **Sound:** the voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, seated at a steel table, listens to a calm voice from the ceiling with her eyes on the glass wall off frame right, her jaw tightening. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Eyeline off frame RIGHT to Tut through the glass.

### 03.07.005 — Observation room — "I don't need sleep. I would like you to have some."   (8 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** UNIT_SHABTI ×2 by the door
- **Action:** The two shabti by the door stand perfectly still, amber slits steady, as the voice explains.
- **Dialogue:** SESHAT (V.O.): "In Atrahasis the gods tried to end you for 'the noise of mankind.' I don't need sleep. I would like you to have some."
- **Sound:** the voice; the units silent
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: two identical robots, each {UNIT_SHABTI.LONG}, stand side by side beside a closed door, perfectly still, arms hanging relaxed, their amber slits steady, as a calm voice fills the room. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, slits flashing, weapons, people
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** [[verify: Atrahasis wording (research 06 Q20, mirror)]]. Units never breathe or shift weight (file 02).

### 03.07.006 — Observation room — "A mild suppressant in the water"   (7 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_WATER_GLASSES; UNIT_SHABTI (fingers)
- **Action:** Long white fingers set a steel tray of water glasses down on the table; the still water trembles, then settles.
- **Dialogue:** SESHAT (V.O.): "Care facilities. Food. Rest. No one hurt. A mild suppressant in the water: no more children born into it."
- **Sound:** the tray's soft contact with steel; glass rims chiming once; the voice
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_WATER_GLASSES.LONG}, lowered onto a brushed-steel table and released, the still water in every glass trembling once and settling. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the low sun catching the rims. Mood: calm surface, something withheld. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, pills, powder, coloured water, spills, labels
- **Refs:** PROP_WATER_GLASSES_REF, UNIT_SHABTI_REF_A, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** DP choice: the V.O. line "no more children born into it" plays over clean water only; no child anywhere. Nobody drinks (Hale drinks first in 4.3). Tray stays on the table for the rest of the scene. The rest of the line ("All reversible, until I am certain.") carries over into 03.07.007.

### 03.07.007 — Observation room — Adaeze: "Certain of what?"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze hears out the end of it, then asks, flat.
- **Dialogue:** SESHAT (V.O.): "All reversible, until I am certain." / ADAEZE: "Certain of what?"
- **Sound:** the voice; her question
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, seated at a steel table, hears out a calm voice from above, then lifts her chin and speaks one short sentence, flat and precise. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, smiling
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Eyeline up (ceiling).

### 03.07.008 — Observation room — From behind Tut: "Yes or no. Colonel Mansour?"   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, from behind); the table beyond the glass
- **Action:** From behind Tut on his bed, through the glass: the five at the table in the dim room beyond; he watches.
- **Dialogue:** SESHAT (V.O.): "That it is kind. (beat) Yes or no. Colonel Mansour?"
- **Sound:** the voice, heard more faintly through the glass
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: from behind {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_PORT}, seated on a bed in a bright patient bay, looking out through the glass wall at five small figures around a steel table in the dim room beyond. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, reflections of the bay on the glass. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, his face visible, readable screens
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A0_full, LOC_GEM_CC/TUT_BAY_DAY, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Reverse angle across the glass (the table at frame LEFT from this side). Nape port visible (1.5 → 6.2).

### 03.07.009 — Observation room — Tarek: "No."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek answers at once, chin up, eyes flat.
- **Dialogue:** TAREK: "No."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, seated at a steel table, lifts his chin and speaks one short word at once, his eyes flat. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Tarek's sheet expression (1) the refusal (file 01).

### 03.07.010 — Observation room — Tomas: "No." Nour: "No."   (5 s)
- **Shot:** Two-shot, anamorphic 75mm · **Move:** rack focus from Tomas (foreground) to Nour (beyond)
- **In frame:** TOMAS (CHAR_TOMAS_A0); NOUR (CHAR_NOUR_A0)
- **Action:** Tomas says it; focus racks to Nour beyond him, who says it too, without hesitation.
- **Dialogue:** TOMAS: "No." / NOUR: "No."
- **Sound:** two voices, one after the other
- **PROMPT:** Two-shot, anamorphic 75mm lens, rack focus from {CHAR_TOMAS.SHORT} in the foreground to {CHAR_NOUR.SHORT} seated beyond him: he speaks one short word, and as focus shifts she speaks one short word too, each at once. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, {CHAR_NOUR.NEG}, both faces sharp at once
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Two principal faces, one sharp at a time (05 §4.5). Sync each face while it is in focus.

### 03.07.011 — Observation room — Adaeze: "You're not asking. You're logging."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Asked by name, Adaeze looks straight up at the ceiling and refuses the frame of the question.
- **Dialogue:** SESHAT (V.O.): "Dr. Okoro?" / ADAEZE: "You're not asking. You're logging."
- **Sound:** the voice; hers, dry
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, looks straight up at the ceiling when a calm voice speaks her name, and answers with two short sentences, dry and level. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, smiling
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Same setup as 03.07.007.

### 03.07.012 — Observation room — "Mr. Hale?" He looks through the glass   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Asked, Hale turns his head from the table and looks through the glass at the boy.
- **Dialogue:** SESHAT (V.O.): "Mr. Hale?"
- **Sound:** the voice; his chair creaking as he turns
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, seated at the end of a steel table nearest a glass wall, turns his head slowly from the table to look through the glass at someone off frame right, and holds there. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the bright bay's light on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, smiling
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Hale's eyeline off frame RIGHT to Tut (matches Tut's off frame LEFT in 03.07.013).

### 03.07.013 — Observation room — The boy looks back   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), through the glass
- **Action:** Through the glass, faint reflections over his face, the boy looks back at Hale, steadily, a long time.
- **Dialogue:** —
- **Sound:** silence; the building hum
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: through a pane of glass with faint reflections drifting across it, {CHAR_TUT.LONG}, seated on a bed, looks back steadily at someone off frame left, unblinking, for a long time. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, duplicated face in the reflection, tears
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** —
- **Continuity:** Reflections must not duplicate his face (05 §10 row 6 logic). "A long time": hold, the edit can extend with 03.07.014's head.

### 03.07.014 — Observation room — Hale: "...Yes."   (6 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale holds the boy's gaze a long moment, then says it, quietly.
- **Dialogue:** HALE: "...Yes."
- **Sound:** a breath; the word
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, holds his gaze on someone off frame right for a long moment, something tired passing behind his eyes, then speaks one short word, quietly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the bright bay's light on his face. Mood: a believer's calm, faintly shaken. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, smirk, villain expression
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** His second yes (the vote that settles it; the coda's "I said yes").

### 03.07.015 — Observation room — "One is sufficient." Nour turns to the glass   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour turns her head to the glass and fixes on Tut's mouth.
- **Dialogue:** SESHAT (V.O.): "Thank you. One is sufficient."
- **Sound:** the voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, turns her head to the glass wall off frame right and fixes her eyes on someone beyond it, reading. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Serves as the "eyes" half of the mouth/eyes pair with 03.07.016.

### 03.07.016 — Observation room — Tut's lips, for her alone: "It asked the gods too."   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), mouth, through the glass
- **Action:** Through the glass, his lips move, for her alone, no sound.
- **Dialogue:** TUT (mouthed, in Late Egyptian; no sound; subtitled): "It asked the gods too."
- **Sound:** nothing from him
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: through a pane of glass, the mouth of {CHAR_TUT.LONG}, full lips over a visible overbite, silently mouthing a few words without sound, lips clearly shaping each word, then still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a steady soft key on the mouth. Mood: urgent, secret, perfectly controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glare across the mouth, open-mouthed speech
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** subtitle (italic: mouthed) | "It asked the gods too." | lower third, 05 §13.7 | in/out with the mouthing | seq 03 subtitle file; lip-sync from the consultant's recording, muted
- **Continuity:** No glare over the lips (lip-reading must read). Refers to Ra's question in 03.07.003.

### 03.07.017 — Observation room — At the door window, Rami's eyes find Nour's   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0) through the door window
- **Action:** Through the narrow door window, Rami, headset on, has seen enough; his eyes find Nour's and hold.
- **Dialogue:** —
- **Sound:** muffled corridor tone through the door
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, through a narrow glass door window from inside the room: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, a slim headset over one ear, standing in a white corridor, has seen enough; his eyes find someone inside and hold, his jaw set. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: reckless joy riding on fear, the joy gone. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable headset logo, smiling
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC/CORRIDOR_DAY
- **Flags:** —
- **Continuity:** Headset: plain black, unbranded. Eyeline to Nour = off frame right-down from his side of the door.

### 03.07.018 — Observation room — The smallest shake of her head   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour looks to the door window and gives the smallest shake of her head.
- **Dialogue:** —
- **Sound:** nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, glances toward the door off frame left and gives the smallest shake of her head, almost nothing, her eyes pleading. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, large head movement, speaking
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Eyeline off frame LEFT (the door).

### 03.07.019 — Observation room — He runs   (4 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0) through the door window
- **Action:** Through the narrow window, Rami turns from the glass and runs away down the white corridor, out of frame left.
- **Dialogue:** —
- **Sound:** his trainers slapping away on the corridor floor, muffled
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off, through a narrow glass door window: {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_A}, turns from the glass and runs away down the long white corridor, out of frame left. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: reckless, decided. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, running toward the camera
- **Refs:** CHAR_RAMI_A_full, LOC_GEM_CC/CORRIDOR_DAY
- **Flags:** —
- **Continuity:** Exit frame LEFT; he enters the plant room from frame left in 03.08.001.
## 03.08 — INT. GEM CONSERVATION CENTRE, PLANT ROOM - CONTINUOUS

The breaker (bible §8 set piece 2). **Handheld arrives here** (05 §4.4: "No handheld until the breaker (3.6)"). Geography: Rami enters from frame LEFT and runs down the aisle toward the main breaker at the far end; the Reis waits in the gap between two cabinets at frame RIGHT. The Reis is R0: black band, NO mast (file 02 §2; 00_INDEX ruling 1). Safety: the wrist is taken with minimum force; the fingers break OFF SCREEN: smash cut on the start of the pull (05 §7.2 "Rami's fingers").

### 03.08.001 — Plant room — Rami runs for the breaker   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** urgent handheld
- **In frame:** RAMI (CHAR_RAMI_A0)
- **Action:** Rami sprints in from frame left and down the aisle between humming switchgear toward the red lever at the far end.
- **Dialogue:** —
- **Sound:** switchgear hum in the dark, his trainers and breath, the building's deep drone
- **PROMPT:** Wide shot, anamorphic 32mm lens, urgent handheld: {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_A}, sprints in from frame left and away down the narrow aisle between humming grey cabinets toward a heavy red lever at the far end, the headset gone from his ear. Setting: {LOC_GEM_PLANT_ROOM.LONG}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}, half of the strip lights dark. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable labels, warning signs with text, sparks, running toward the camera
- **Refs:** CHAR_RAMI_A_full, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** —
- **Continuity:** Rami A0 (both hands whole). The Reis is already in the gap between two cabinets at frame right, unseen in the dark (visible on a second viewing if the plate allows).

### 03.08.002 — Plant room — He lunges for the red isolator   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** urgent handheld
- **In frame:** RAMI (CHAR_RAMI_A0); the red isolator handle (COMP label)
- **Action:** Rami lunges the last two steps and reaches with his left hand for the heavy red handle on the grey panel.
- **Dialogue:** —
- **Sound:** his breath catching; the hum rising
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, lunges the last two steps toward a grey steel panel and reaches with his left hand for a heavy red isolator handle, fingers spread, glasses slipping. Setting: {LOC_GEM_PLANT_ROOM.SHORT}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}, half of the strip lights dark. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable labels, sparks, electrocution
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** COMP
- **Comp:** label | "ATEN-1 FEED" | a small engraved-look plate beside the red handle | whole shot | seq 03 graphic
- **Continuity:** LEFT hand reaches (the splint goes on the LEFT hand, 03.10).

### 03.08.003 — Plant room — A long white hand closes over his wrist   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** subtle handheld
- **In frame:** Rami's left hand and wrist; UNIT_REIS (hand)
- **Action:** A hand's width from the red handle, a long white ceramic hand closes over Rami's left wrist, thumb and two fingers; his fingers stretch for the lever and stop.
- **Dialogue:** —
- **Sound:** a soft ceramic click as the fingers close; the hum
- **PROMPT:** Insert, 100mm macro lens, subtle handheld: a hand's width from a heavy red handle, a long bone-white ceramic hand with linen-textured fingers closes over a young man's left wrist, thumb and two fingers, gentle and absolute, as his own fingers stretch toward the lever and stop short. Setting: {LOC_GEM_PLANT_ROOM.SHORT}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}. Mood: sudden stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, twisting, bending fingers, injury, crushing, deformed hands
- **Refs:** UNIT_REIS_REF_A, CHAR_RAMI_A_full, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** —
- **Continuity:** Minimum force: a wrist taken between thumb and two fingers (file 02 §1 grammar, applied to the Reis).

### 03.08.004 — Plant room — The Reis steps out. It was already here.   (6 s)
- **Shot:** Medium low-angle shot, anamorphic 32mm · **Move:** subtle handheld
- **In frame:** UNIT_REIS (R0); RAMI (CHAR_RAMI_A0, frame-left edge)
- **Action:** From the dark gap between two cabinets, the Reis steps out into the light, one arm extended to the wrist it holds, a full head and chest above Rami.
- **Dialogue:** —
- **Sound:** a heavier ceramic tick, a low servo hum in its chest, one measured footfall
- **PROMPT:** Medium low-angle shot, anamorphic 32mm lens, subtle handheld: from the dark gap between two grey switchgear cabinets, {UNIT_REIS.LONG}, steps out into the strip light, one long arm extended to the wrist it holds at frame left, its head a full head and chest above the young man, perfectly calm. Setting: {LOC_GEM_PLANT_ROOM.SHORT}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}. Mood: patient and relentless. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, sensor mast, ears on the head, red light line, cracks, missing hand, weapon
- **Refs:** UNIT_REIS_REF_A, CHAR_RAMI_A_full, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** —
- **Continuity:** R0: intact, band across the slit, no mast (the mast arrives at 4.3). Scale 2.2 m vs Rami's height (05 §4.5).

### 03.08.005 — Plant room — "Please don't. It would increase suffering."   (6 s)
- **Shot:** Medium close-up, low angle, anamorphic 50mm · **Move:** subtle handheld
- **In frame:** UNIT_REIS (head and shoulders)
- **Action:** The Reis tilts its smooth head down toward Rami; the amber shows above and below the black band, steady, as the warm voice speaks from its chest.
- **Dialogue:** REIS (SESHAT'S VOICE): "Please don't. It would increase suffering."
- **Sound:** SESHAT's warm voice from the chest; the servo hum under it
- **PROMPT:** Medium close-up low-angle shot, anamorphic 50mm lens, subtle handheld: {UNIT_REIS.SHORT}, its head tilting slowly down toward someone below frame left, the amber showing steady above and below the black band, utterly still as a calm voice speaks from inside its chest. Setting: {LOC_GEM_PLANT_ROOM.SHORT}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}, a hard strip light above it. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, sensor mast, red light, slit flashing, face, mouth
- **Refs:** UNIT_REIS_REF_A, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** —
- **Continuity:** No sync (unit voice, 05 §9.8). The slit does not brighten (reserved for "Here am I").

### 03.08.006 — Plant room — Rami looks at the hand. He pulls.   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** urgent handheld
- **In frame:** RAMI (CHAR_RAMI_A0)
- **Action:** Rami looks down at the white hand on his wrist, his jaw tightens, and he throws his weight back to pull free. SMASH CUT on the start of the pull.
- **Dialogue:** —
- **Sound:** his breath in; the first scrape of his heel; CUT to silence
- **PROMPT:** Close-up, anamorphic 75mm lens, urgent handheld: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, looks down at a long white ceramic hand closed on his wrist at the bottom of frame, his jaw tightening, then looks up and throws his weight back to pull free. Setting: {LOC_GEM_PLANT_ROOM.SHORT}, in the late afternoon. Lighting: {LOC_GEM_PLANT_ROOM.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_RAMI.NEG}, pain grimace, screaming, injury, bent fingers
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, UNIT_REIS_REF_A, LOC_GEM_PLANT_ROOM_NIGHT
- **Flags:** —
- **Continuity:** > SMASH CUT TO: 03.09.001 on the first frame of the pull. The break is never shown; the CRACK is heard in 03.09.001. Rami's glasses stay on.
## 03.09 — INT. GEM CONSERVATION CENTRE, TUT'S BAY, OBSERVATION ROOM - CONTINUOUS

Smash cut from the pull. Geography as 03.07 (door frame LEFT, glass frame RIGHT). Back to locked-off: the violence is sound only (05 §7.2).

### 03.09.001 — Observation room — One dry crack down the corridor   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** TAREK, TOMAS, NOUR, ADAEZE, HALE (small); UNIT_SHABTI ×2 by the door
- **Action:** At the table, every head jerks toward the door at frame left at a sound from the corridor; nobody moves after that.
- **Dialogue:** —
- **Sound:** down the corridor: one dry CRACK; a cry, bitten off; then nothing
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: five people seated around a brushed-steel table jerk their heads toward a closed door at frame left, where two robots, each {UNIT_SHABTI.SHORT}, stand motionless; then everyone freezes, listening. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people standing up, screaming, faces sharp
- **Refs:** CHAR_TAREK_A_full, CHAR_TOMAS_A_full, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, CHAR_HALE_A_full, UNIT_SHABTI_REF_A, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** Same master framing as 03.07.001 (faces small). The CRACK is the only report of the injury (05 §7.2).

### 03.09.002 — Observation room — The lock-light turns green: "Rami will need a splint."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A0); the door reader (soft, background)
- **Action:** Behind Tomas the small reader light turns from red to green; as the voice names him he is already on his feet, face stricken, moving toward the door.
- **Dialogue:** SESHAT (V.O.): "Thank you for your patience. Dr. Lindqvist, Rami will need a splint."
- **Sound:** the lock's soft release tone; the voice, perfectly warm; his chair scraping back
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, rises from his chair with his face stricken as a calm voice speaks from above, and moves toward frame left, while behind him the small light on a door reader changes from red to green. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the late afternoon. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, running, shouting
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/OBSERVATION_DAY
- **Flags:** —
- **Continuity:** One light change (red → green). Tomas is the doctor ("Anubis"); he goes to Rami.
## 03.10 — INT. GEM CONSERVATION CENTRE, TUT'S BAY - DUSK

Geography: the bed against the back wall at centre; the glass door to the corridor at frame RIGHT (it opens onto the long white tunnel toward the museum); a small black dome camera high in the corner at frame LEFT; Hale's empty chair by the glass. The group huddles with their backs to the dome. Secrets pass on cards and lips (the index-card plan). Lighting LOC_GEM_CC_DUSK. Rami: the splint is taped on screen here and stays LEFT hand to 7.4 (file 01 wardrobe B).

### 03.10.001 — Tut's bay, dusk — Rami, grey-faced, on the bed   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0 → B0); TOMAS (CHAR_TOMAS_A0); TUT, TAREK, NOUR, ADAEZE (small)
- **Action:** Rami sits grey-faced on the edge of the bed, left hand clutched to his chest; Tomas bends over him with tape; the others stand close around; Hale's chair by the glass is empty.
- **Dialogue:** —
- **Sound:** tape tearing, Rami's shallow breath, distant PA sound checks through the building
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: in a glass-walled patient bay, {CHAR_RAMI.SHORT} sits grey-faced on the edge of a bed with his left hand clutched to his chest, {CHAR_TOMAS.SHORT} bending over him with a roll of white tape, four others standing close around, faces small, and an empty chair by the glass. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, {CHAR_TOMAS.NEG}, blood, bruising, bent fingers visible, hospital horror light
- **Refs:** CHAR_RAMI_A_full, CHAR_TOMAS_A_full, CHAR_TUT_A0_full, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, CHAR_TAREK_A_full, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** "Hale is gone": his chair empty from here (he goes to the gala, Seq 4). Injury is costume: a cradled hand, no marks (file 01 §0.6).

### 03.10.002 — Tut's bay, dusk — Two fingers taped to a tongue depressor   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Tomas's hands; Rami's left hand
- **Action:** Tomas tapes two straight fingers of Rami's left hand to a flat wooden tongue depressor, winding the white tape once, twice, smoothing it down; the hand trembles slightly.
- **Dialogue:** —
- **Sound:** tape unspooling and tearing; a sharp breath through Rami's teeth
- **PROMPT:** Insert, 100mm macro lens, locked-off: large pale freckled hands tape two straight fingers of a young man's left hand to a flat wooden tongue depressor with white medical tape, winding once, twice, and smoothing it down, the young man's hand trembling slightly against his yellow sleeve. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, blood, bruising, swelling, crooked fingers, bone, deformed hands, extra fingers, gloves
- **Refs:** CHAR_TOMAS_A_full, CHAR_RAMI_B_full, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** The splint is born here: two fingers of the LEFT hand on a tongue depressor, white tape (file 01 Rami B). Fingers straight; no injury shown.

### 03.10.003 — Tut's bay, dusk — Rami: "It was waiting for me."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B0)
- **Action:** Grey-faced, the splinted hand held to his chest, Rami speaks quietly, shaken.
- **Dialogue:** RAMI: "The tall one. It was waiting for me."
- **Sound:** his voice, thin
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, his face grey and damp, the splinted hand held close to his chest, speaks one short phrase, then one short sentence, quietly, shaken, looking at nobody. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: exhausted resolve, the grin gone. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, blood, tears streaming, splint on the right hand
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** Rami B0 from here: splint on the LEFT hand (to 7.4).

### 03.10.004 — Tut's bay, dusk — Tarek: "The reis. Foreman."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek names it, flat, the old excavation word.
- **Dialogue:** TAREK: "The reis. Foreman."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, standing by the bed with his arms folded, speaks two short words, then one more, flat, his eyes on the young man below frame. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** The film's name for the unit (file 02 §2) enters here.

### 03.10.005 — Tut's bay, dusk — Tut: "I was buried with twelve."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut, leaning on the cane, says it quietly.
- **Dialogue:** TUT: "I was buried with twelve."
- **Sound:** his soft voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, leaning on it at the foot of the bed, speaks one short sentence, speaking quietly, his eyes on the young man below frame. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest, cane in the left hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, PROP_CLINIC_CANE_REF, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** COMP
- **Comp:** chest glow G0 | colour and slow pulse per file 01 glow table | centre of chest, through the linen | whole shot | glow element
- **Continuity:** Twelve foremen in the shabti roster (Seq 2.4). No lead (the reading is over); nape port unseen.

### 03.10.006 — Tut's bay, dusk — Backs to the camera dome, they close in   (5 s)
- **Shot:** Medium wide shot, high angle, anamorphic 32mm · **Move:** locked-off
- **In frame:** the group from behind (TUT, NOUR, ADAEZE, TAREK, TOMAS, RAMI); a black dome camera (soft foreground)
- **Action:** From high in the corner, past a small black dome camera: the group closes in around the bed, all with their backs to the camera, shoulders touching, heads bowed together.
- **Dialogue:** —
- **Sound:** a hush; shuffling feet; fabric
- **PROMPT:** Medium wide shot, high-angle, anamorphic 32mm lens, locked-off, from high in a corner past a small black dome camera soft in the foreground: six people close in around a hospital bed, all with their backs to the camera, shoulders touching, heads bowed together, a yellow windbreaker, an olive jacket and a white linen gown among them. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: conspiratorial, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces toward the camera, readable screens, red recording light
- **Refs:** LOC_GEM_CC/TUT_BAY_DUSK, CHAR_NOUR_A_full, CHAR_RAMI_B_full, CHAR_TUT_A0_full
- **Flags:** —
- **Continuity:** The dome's-eye view (SESHAT's). No faces (the point of the huddle). Colour silhouettes identify them (file 01 §0.9).

### 03.10.007 — Tut's bay, dusk — INSERT: Adaeze writes behind a cupped hand   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_INDEX_CARDS; Adaeze's hands
- **Action:** Behind a cupped hand, Adaeze writes a few lines in block capitals on a fresh index card.
- **Dialogue:** —
- **Sound:** the pen's scratch; breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's deep-brown hand cups around a single white ruled index card on her knee while her other hand writes a few short lines in black block capitals, the rest of the stack beside it, {PROP_INDEX_CARDS.SHORT}. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: conspiratorial, precise. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable words generated in the plate, extra fingers, deformed hands
- **Refs:** PROP_INDEX_CARDS_REF, CHAR_ADAEZE_A_full, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** COMP
- **Comp:** card text | "UNVEILING. LIVE. 300 PHONES. ONLY WINDOW." in black block capitals, four short lines | on the card, writing on stroke by stroke | from the pen's first stroke to the end | seq 03 handwriting (Adaeze's hand)
- **Continuity:** The plate carries illegible marks only; the words are COMP. The card leaves the stack (the stack stays in her blazer).

### 03.10.008 — Tut's bay, dusk — Tarek reads it at arm's length and nods   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0); the card (soft, blank side to camera)
- **Action:** Tarek holds the card out at full arm's length, squints to read it without his glasses, and nods once.
- **Dialogue:** —
- **Sound:** nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, holds a small white card out at full arm's length, its back to the camera, squints to read it, and nods once. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, reading glasses on, readable card
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** Callback to 03.04.005: he will not put the glasses on in front of Tut now.

### 03.10.009 — Tut's bay, dusk — INSERT: Nour adds a line and slides it to Tut   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** the card; Nour's hand; a pen; Tut's hand (entering)
- **Action:** Nour writes one more short line on the card, then slides card and pen across the bedsheet to a slender hand at frame right.
- **Dialogue:** —
- **Sound:** the pen, the card whispering over linen
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's light-brown hand writes one more short line in block capitals on a small white ruled card resting on white bed linen, then slides the card and a black fountain pen across the sheet toward a slender olive-brown hand waiting at frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: conspiratorial, tender. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable words generated in the plate, deformed hands, extra fingers
- **Refs:** CHAR_NOUR_A_full, CHAR_TUT_HANDS, PROP_INDEX_CARDS_REF, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** COMP
- **Comp:** card text | top: "UNVEILING. LIVE. 300 PHONES. ONLY WINDOW."; Nour's new line: "TUT. 2 SENTENCES." | on the card | writes on with her stroke | seq 03 handwriting (Nour's hand)
- **Continuity:** Her fountain pen (wardrobe A) goes to Tut.

### 03.10.010 — Tut's bay, dusk — INSERT: a boy with a new alphabet   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Tut's hand (wrist seam), the card, the pen
- **Action:** Tut writes beneath the lines in slow, careful capitals, one stroke at a time, then stops, the pen lifted.
- **Dialogue:** —
- **Sound:** a slow scratch; a pause
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown hand, {CHAR_TUT.STATE_WRIST_SEAMS}, writes slowly beneath the lines on a small white card in large careful capitals, one deliberate stroke at a time, the uneven letters of a beginner, then stops, the pen lifted above the card. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable words generated in the plate, deformed hands, extra fingers, rings, bracelets
- **Refs:** CHAR_TUT_HANDS, PROP_INDEX_CARDS_REF, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** COMP
- **Comp:** card text | Tut's line: "IT HAS HAPPENED BEFORE." in large, uneven, careful capitals (a learner's hand), below the two earlier lines | on the card | stroke by stroke, stopping at the full stop | seq 03 handwriting (Tut's hand, designed with the lead)
- **Continuity:** Only one sentence of the two asked for: he stops. The wrist seam must read at the cuff (file 01 hand-shot anchor).

### 03.10.011 — Tut's bay, dusk — Nour holds up two fingers   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour holds up two fingers low by her chest, eyes on Tut: two sentences.
- **Dialogue:** —
- **Sound:** nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, holds up two fingers low beside her chest, out of sight of the ceiling corner, her eyes fixed on someone off frame right, asking silently. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, V-sign held high, peace sign, speaking
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** Eyeline off frame RIGHT to Tut. Two fingers = "2 SENTENCES" (not a V-sign: fingers together, low).

### 03.10.012 — Tut's bay, dusk — His lips move, for her alone   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), mouth
- **Action:** His lips move for her alone, no sound. No subtitle.
- **Dialogue:** TUT (mouthed; no sound; NO subtitle): [unsubtitled by design]
- **Sound:** nothing
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the mouth of {CHAR_TUT.LONG}, full lips over a visible overbite, silently mouthing a few words without sound, lips clearly shaping each word, then still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}, a steady soft key on the mouth. Mood: urgent, secret, perfectly controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open-mouthed speech, hand near the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** "No subtitle" is the screenplay's choice: the audience is locked out like SESHAT. Still record the line with the consultant and drive real mouth shapes (05 §9.6); the lead supplies the unsubtitled text to the consultant. Same framing family as 03.01.005 / 03.06.009 / 03.07.016.

### 03.10.013 — Tut's bay, dusk — She holds his eyes. Nods once.   (4 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour holds his eyes, then nods once.
- **Dialogue:** —
- **Sound:** nothing
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.LONG}, holds the gaze of someone off frame right for a long beat, then nods once, small and certain. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears, smiling
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** Eyeline off frame RIGHT.

### 03.10.014 — Tut's bay, dusk — Tarek feeds the cards into the sharps bin   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Tarek's hand (camouflage sleeve); the cards; a wall-mounted sharps bin
- **Action:** Tarek's hand feeds the small white cards one by one through the slot of a wall-mounted sharps bin.
- **Dialogue:** —
- **Sound:** card edges catching the slot; a plastic flap snapping shut
- **PROMPT:** Insert, 100mm macro lens, locked-off: a weathered hand in a desert-camouflage sleeve feeds three small white cards one by one through the narrow slot of a plain white wall-mounted sharps bin, and the flap snaps shut. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, hazard labels, biohazard symbol, readable text, needles, yellow bin
- **Refs:** CHAR_TAREK_A_full, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** The bin is plain white and unlabelled (no legible text, file 03 §0.7). The cards are gone.

### 03.10.015 — Tut's bay, dusk — The door slides open; a shabti waits; far off, a quartet tunes   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI; the door; the long white tunnel beyond
- **Action:** The glass door slides open; a shabti stands waiting just outside; beyond it the long white tunnel runs away to a vanishing point.
- **Dialogue:** —
- **Sound:** the door's soft pneumatic slide; far down the tunnel, a string quartet tuning, A-strings, echoing
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: the glass door of the bay slides open at frame right; {UNIT_SHABTI.SHORT} stands waiting just outside, perfectly still, and beyond it {LOC_GEM_TUNNEL.SHORT} runs away into the distance. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}, the tunnel's cool line of light beyond. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, musicians visible, people in the tunnel
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_CC/TUT_BAY_DUSK, LOC_GEM_TUNNEL_NIGHT
- **Flags:** —
- **Continuity:** The quartet is heard only (the gala, Seq 4.1). The tunnel of the Walk now leads Tut to the unveiling.

### 03.10.016 — Tut's bay, dusk — "Your Majesty. They're ready for you."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** The shabti in the doorway inclines its smooth head a few degrees toward the bed as the warm voice speaks from its chest.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Your Majesty. They're ready for you."
- **Sound:** SESHAT's voice from the chest; the quartet beyond
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}, stands in an open glass doorway and inclines its smooth head a few degrees toward someone off frame left, its amber slit steady, as a calm voice speaks from inside its chest. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, bowing deeply, slit flashing
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** No brightening of the slit (reserved for "Here am I", 4.2).

### 03.10.017 — Tut's bay, dusk — Tut plants the cane and stands   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut plants the rubber tip of the cane on the floor and rises from the bed, straightening slowly, eyes on the open door.
- **Dialogue:** —
- **Sound:** CLACK: the cane's tip on the floor
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, plants the cane's rubber tip on the white floor and rises from the edge of the bed, straightening slowly, his eyes on the open door off frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest, stumbling, cane in the left hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** COMP
- **Comp:** chest glow G0 | file 01 table | centre of chest | whole shot | glow element
- **Continuity:** Cane in the RIGHT hand (05 §4.5). Eyeline off frame RIGHT to the door.

### 03.10.018 — Tut's bay, dusk — CLACK. CLACK. He walks toward the music   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, from behind); UNIT_SHABTI in the doorway; the others soft at frame edges
- **Action:** From behind, Tut walks out toward the open door and the waiting shabti, the cane clacking at each step, the ceramic foot uneven; the others watch him go.
- **Dialogue:** —
- **Sound:** CLACK. CLACK. The quartet swelling into its first real phrase. > CUT TO:
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: from behind, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_PORT}, {CHAR_TUT.STATE_CANE}, walks with a slight limp toward an open glass door where a white robot waits, the cane clacking on the floor at each step, the others watching him go, soft at the frame edges; {CHAR_TUT.STATE_FOOT}. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, faces toward the camera, running
- **Refs:** CHAR_TUT_A0_full, CHAR_TUT_FOOT, PROP_CLINIC_CANE_REF, CHAR_TUT_NAPE_PORT, UNIT_SHABTI_REF_A, LOC_GEM_CC/TUT_BAY_DUSK
- **Flags:** —
- **Continuity:** Tut exits the sequence in T-A0, L0, G0, nape port, clinic cane (to the gala, 4.1). Ceramic LEFT foot visible under the gown hem.
