# SEQUENCE 11 — THE HORIZON · shot list and paste-ready video prompts

**HERE AM I** · Seq 11 · screenplay pages 101–113 (`screenplay/seq_11.fountain`, 12.9 pages by `pagecount.py`) · Giza, 8 Nov 2033, 00:00–05:20 · Amduat cards: THE SIXTH, SEVENTH, EIGHTH and NINTH HOURS.
Delivery: photoreal live action, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

- **Shots:** 163 · **Runtime:** 882 s = **14 min 42 s** (page-count target 12.9 min; +14%, inside the ±20% band) · **Average shot:** 5.4 s
- **Flags:** COMP ×82 (subtitles, SUPERs, hour cards, slit timing, the tablet image, the inch-worm feed, the ochre marks and the hidden line, the watch dial; plus the G1 chest glow on 35 shots where it is on the tunic and 27 where its light is the key or a visible bounce, 05 §6.1 and §13.9) · VFX-ASSIST ×30 (the flood, underwater, the thread and tether glints, blasts, sparks and impacts, the sliding stone) · VFX-EXTEND ×9 (Garden rows, the causeway line, the Sekhmet rows) · EXTEND chains ×3 (11.04.024→025, 11.08.008→009, 11.10.005→006)
- **How to build:** fixed wording is inserted by tokens (`{SUFFIX}`, `{NEG}`, `{NEG_*}`, `{TOKEN.FIELD}` from `production_bible/locks.json`). Expand and validate with `python3 shots_md2jsonl.py shots/seq_11_shots.md`, which writes `shots/seq_11_shots.jsonl`. Every PROMPT follows the 03b seven-step order, carries at most one LONG lock, and keeps the writer's own words to 70 or fewer.

## Scene list

| # | Scene | Shots | Count | Runtime |
|---|---|---|---|---|
| 11.01 | INT. GEM GRAND ATRIUM - NIGHT (bracelets; the tablet) | 11.01.001–008 | 8 | 42 s |
| 11.02 | EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT (the fortress; SESHAT's offer; the plan) | 11.02.001–024 | 24 | 143 s |
| 11.03 | EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER (the diversion; the map case) | 11.03.001–007 | 7 | 37 s |
| 11.04 | INT. OSIRIS SHAFT - NIGHT (the reversed pump; Tarek's stand; THE SIXTH HOUR) | 11.04.001–025 | 25 | 135 s |
| 11.05 | INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS | 11.05.001–005 | 5 | 25 s |
| 11.06 | INT. BUILDERS' CRAWLWAY - CONTINUOUS | 11.06.001–002 | 2 | 11 s |
| 11.07 | INT. GREAT PYRAMID, GRAND GALLERY - NIGHT (the procession waits; the liturgy) | 11.07.001–011 | 11 | 62 s |
| 11.08 | EXT. GREAT PYRAMID, NORTH FACE - NIGHT (the relay blown at 04:00; THE SEVENTH HOUR) | 11.08.001–009 | 9 | 43 s |
| 11.09 | INT. GREAT PYRAMID, SUBTERRANEAN CHAMBER - NIGHT | 11.09.001–002 | 2 | 11 s |
| 11.10 | INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS (the summons; the work gang; THE EIGHTH HOUR; the Reis) | 11.10.001–027 | 27 | 147 s |
| 11.11 | INT. GREAT PYRAMID, GRAND GALLERY - NIGHT (THE NINTH HOUR; "Bridge the two"; the stone slides; the climb; the dagger; SUPER 05:20) | 11.11.001–040 | 40 | 209 s |
| 11.12 | INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS | 11.12.001–003 | 3 | 17 s |

The INSERT (the inch-worm's feed on Nour's tablet) and the UNDERWATER/ABOVE beats stay inside their parent scenes (11.11 and 11.04).

## Sequence state board (continuity at a glance)

| Who / what | In 11 | Look code / state |
|---|---|---|
| Tut | T-B at L3 (jacket; hood torn) → soaked in 11.04–11.06 → drying from 11.09 → **T-C** from 11.11.028 (jacket torn off by the Reis) | CHAR_TUT_B3 → CHAR_TUT_C; G1 glow (COMP pulse, slowing); cracked left wrist and left knee seams; nape scar; ceramic LEFT foot; stick in the RIGHT hand until **lost at 11.11.029**; dagger on the belt until **given to Fathi at 11.11.035**; notebook sealed in the map case in his tunic from 11.03.006 |
| Nour | captive, in the procession | CHAR_NOUR_C (L2, face clean): white lector's shawl, crushed cornflowers, tablet; glasses on to read (11.07.009, 11.11.015); touches the pendant at 11.11.021 |
| Adaeze | with Tut | CHAR_ADAEZE_C3: bandaged LEFT leg, limp; soaked 11.04–11.06, drying from 11.09; her kit (Rami's camera) sinks at 11.04.013 |
| Tarek | B at L3 → C (soaked, chest-deep) | **dies 11.04** (hand, water, sound; never the face underwater) |
| Fathi | B at L3, dry | wind-up watch (left wrist); blows the relay at 04:00; rifle **empty** at 11.11.030; holds the great step with the dagger |
| Akhenaten / Tomas | procession | CHAR_AKHENATEN_B (hem dusty) · CHAR_TOMAS_C (torn left shoulder seam) |
| Hale | asleep in the atrium | CHAR_HALE_B → **B_BRACELET** at 11.01.002 (left wrist) |
| Units | — | Reis R4 + dust (one LEFT hand); jackal D1; shabti "Rami" STATE_RAMI from 11.10.016; one gang unit STATE_GANG_ARM from 11.10.025; relay BLOWN 11.08.008; the stone SLID 11.11.018; the thread never cut |

**Key light underground:** Tarek's rifle torch in the shaft (11.04); after it goes under, no torch survives: 11.05–11.10.019 are lit only by Tut's chest glow and unit slits (the file 03 TORCH variants and GRADE_UNDERGROUND, whose wording is "lit only by head torches and handheld torches", are deliberately not pasted there; the light is written in plain words), until Fathi's rifle torch arrives (11.10.020). Prompts never give the glow a colour in the writer's own words ("a warm glow"); its amber-gold and pulse are COMP (05 §13.9). The file 03 locks LOC_OSIRIS_SHAFT.LIGHT_TORCH and the HEART_GLOW variants still carry "amber" in their fixed wording; file 03 should be reconciled.

**Geography locks used:** the Wall of the Crow looking north (lion enclosure frame right, Great Pyramid centre, causeway and second pyramid frame left; west = frame left) · the shaft master from the ladder (pump frame left, island centre, tunnel mouth right of centre in the far wall) · Descending and Ascending Passages: down toward camera, up away · Grand Gallery from the bottom: up away from camera, WEST ramp frame right, EAST ramp frame left · north face: east = frame left.

## Reference stills needed

**Characters** (approved stills from file 01; state edits by image-editing, never from text):
- Tut: CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_profile, CHAR_TUT_B_night_34, CHAR_TUT_B1_full (edit to B3: L3 damage, hood torn; plus SOAKED and DRYING variants), CHAR_TUT_C3_full (edit to C: no shawl, wet torn tunic), CHAR_TUT_FOOT, CHAR_TUT_HANDS (with the cracked left wrist seam)
- Nour: CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full
- Adaeze: CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full (edit SOAKED and DRYING variants; glasses askew variant)
- Tarek: CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full (edit to C: soaked, chest-deep)
- Fathi: CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full (edit to L3: soot, empty pouches; wind-up watch)
- Tomas: CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full
- Akhenaten: CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full (edit to B: dusty hem)
- Hale: CHAR_HALE_A_front, CHAR_HALE_A_34 (edit to B_BRACELET, asleep)
- CHAR_GARDEN_SLEEPERS_still · CHAR_LAYLA_ASLEEP_MASTER (comp only, on the tablet)

**Units** (REF A/B stills and the 3D assets): UNIT_SHABTI (+ STATE_RAMI, STATE_GANG_ARM), UNIT_NURSE, UNIT_REIS (R4 + dust), UNIT_JACKAL (D1), UNIT_SEKHMET, UNIT_INCHWORM (+ trailing tether), UNIT_GLASS_SERPENT, UNIT_THREAD, UNIT_RELAY (+ BLOWN)

**Props:** PROP_SLEEP_BRACELET, PROP_TABLET_LAYLA, PROP_ID_DISCS, PROP_CASKET_NEST (carried), PROP_RAMI_NOTEBOOK (cracked), PROP_MAP_CASE, PROP_CONSERVATION_KIT (sinking), PROP_DEMO_CHARGES, PROP_WINDUP_WATCH, PROP_LAYLA_PENDANT, PROP_EBONY_STICK (ST2), PROP_DAGGER

**Location plates** (file 03; state plates derived by image edit): LOC_GEM_ATRIUM_GARDEN · LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS (+ western-field tower lit/dark before-after; causeway and enclosure-rim clean plates) · LOC_OSIRIS_SHAFT_TORCH and _FLOOD (+ W0, W1, W2, W3 state plates; underwater tank plate) · LOC_GP_NORTH_FACE_NIGHT (+ RELAY, BLOWN, EMBERS) · LOC_GP_SUBTERRANEAN_TORCH · LOC_GP_DESCENDING_TORCH · LOC_GP_MAMUN_TUNNEL_TORCH · LOC_GP_ASCENDING_TORCH · LOC_GP_GRAND_GALLERY_SLITS, _BLACKOUT_TORCH, _FIGHT (+ STONE_SLID before/after) · LOC_GP_QC_SHAFT_INCHWORM (+ AREA_BEHIND_DOOR) · LOC_GP_PASSAGE_ABOVE_HEART_GLOW

**Comp assets:** SUPERs "GIZA. 8 NOVEMBER. 00:00." and "05:20."; hour cards six to nine with the Egyptologist's "hour" glyph; the subtitle file (Egyptian Arabic and Middle Egyptian lines); the slit-brightening timing; UNIT_GLYPH_SESHAT for the feed; the Djedi red ochre marks and the "Bridge the two" line (Egyptologist); the watch dial at 03:59 → 04:00; the G1 glow colour and pulse.

## Notes for the lead
1. **11.04.014, Tut's eyes open underwater.** The screenplay asks for it. It is the only face under water in the film: calm, lips closed, no bubbles. NEG_WATER is left off that one shot on purpose and its drowning terms are covered by shot negatives. Please approve.
2. **Garden bedding.** The atrium shots use CHAR_GARDEN_SLEEPERS ("low cots") and do not paste LOC_GEM_ATRIUM.AREA_GARDEN ("white mats"). File 03 should be reconciled.
3. **Torch variants after the flood.** See the key-light note above. The LOC_GP_SUBTERRANEAN and DESCENDING TORCH variants assume head torches the screenplay does not give them.
4. **"Ya Malik"** (11.11.037) stays unsubtitled, as scripted. The localisation consultant should confirm.
5. **PROP_CASKET_NEST SHORT** describes the opened nest at the pit, so the carried shots paste only STATE_CARRIED.
6. **QA pass (prompt QA lead).** Added the G1 chest-glow COMP element wherever the glow is on screen or is the key light; removed GRADE_UNDERGROUND from the torchless stretch (11.09.001, 11.10.001–019); NEG_WATER on every flood shot except 11.04.014; NEG_REMAINS on every Tut shot; the map-case insert (11.03.006) writes the empty case in plain words because both map-case locks describe it already sealed.
7. The screenplay's [[verify]] notes stand (the Horus gloss, the Osiris Shaft levels, Al-Ma'mun's tunnel, the Amduat card titles, the Gallery dimensions).

---
## SCENE 11.01 — INT. GEM GRAND ATRIUM - NIGHT

### 11.01.001 — INT. GEM GRAND ATRIUM - NIGHT — The Garden under the colossus   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** GARDEN SLEEPERS (CHAR_GARDEN_SLEEPERS, rows, VFX-EXTEND); UNIT_NURSE ×3 (hero); UNIT_SHABTI ×2 (bg, standing)
- **Action:** Rows of adult sleepers lie beneath the red-granite colossus; three nurses move slowly along the rows carrying trays of silver bracelets.
- **Dialogue:** —
- **Sound:** a hall-wide hush; thousands of slow breaths; the faint dry ceramic tick of the nurses' steps; the soft chime of metal bands on a tray
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: the camera looks down the length of the floor where {CHAR_GARDEN_SLEEPERS.SHORT}, recede toward the plinth of the colossus, and three slow figures, each {UNIT_NURSE.SHORT}, walk along the rows bearing {PROP_SLEEP_BRACELET.STATE_TRAY}; two tall robots stand motionless at the far end. Setting: {LOC_GEM_ATRIUM.LONG}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, hospital beds, white mats, crowds standing, daylight
- **Refs:** CHAR_GARDEN_SLEEPERS_still, UNIT_NURSE, UNIT_SHABTI, PROP_SLEEP_BRACELET, LOC_GEM_ATRIUM_GARDEN
- **Flags:** VFX-EXTEND
- **Continuity:** 11.1 is the night the bracelets go on in the atrium: before this scene atrium sleepers wear none; by 11.01.004 every adult wrist is silver. Sleepers lie on low cots per CHAR_GARDEN_SLEEPERS (AREA_GARDEN's "white mats" deliberately not pasted; flag to the lead). Adults only. Deliver a clean plate at this framing for the row extension.

### 11.01.002 — INT. GEM GRAND ATRIUM - NIGHT — A bracelet closes on Hale's wrist   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_B → B_BRACELET, asleep, face soft); UNIT_NURSE (hands only); PROP_SLEEP_BRACELET
- **Action:** A nurse's long ceramic fingers close a thin silver band round a sleeping man's relaxed left wrist; it clicks shut.
- **Dialogue:** —
- **Sound:** one small precise click; the man's slow breath; the ceramic tick of the nurse's wrist
- **PROMPT:** Insert, 100mm macro lens, locked-off: long slim bone-white ceramic fingers close {PROP_SLEEP_BRACELET.LONG}, the band clicking shut around the left wrist of {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_B}, whose calm sleeping face rests soft and out of focus beyond the hand; the fingers withdraw slowly. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_HALE.NEG}, clasp, buckle, glowing band, screen on the band, bracelet on the right wrist
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, UNIT_NURSE, PROP_SLEEP_BRACELET, LOC_GEM_ATRIUM_GARDEN
- **Continuity:** Hale from this frame: WARD_B_BRACELET (the band on his LEFT wrist) until he wakes (12.8). The nurse's sleeve cuff (sand knit) may show at frame edge.

### 11.01.003 — INT. GEM GRAND ATRIUM - NIGHT — Nour walks between two shabti and stops   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, lateral track · **Move:** lateral tracking right, walking pace, stops with her
- **In frame:** NOUR (CHAR_NOUR_C); UNIT_SHABTI ×2 (standing, framing her)
- **Action:** Nour walks between two standing shabti along the edge of the rows, then stops dead, looking down at the sleepers' wrists.
- **Dialogue:** —
- **Sound:** her boots on stone, the only footsteps in the hall; breathing of the sleepers
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking right: the camera travels at walking pace with {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_C}, {CHAR_NOUR.DMG_L2}, as she passes between two motionless figures, each {UNIT_SHABTI.SHORT}, then stops dead and looks down at the rows at her feet, the camera settling with her. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_NOUR.NEG}, robots walking, robot touching her
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, UNIT_SHABTI, LOC_GEM_ATRIUM_GARDEN
- **Continuity:** Nour look C at L2, face washed; the white lector's shawl and crushed cornflowers in the breast pocket are on from here through the Hall (WARD_C); glasses on the cord, off her face; pendant under the shawl. Travel direction left to right.

### 11.01.004 — INT. GEM GRAND ATRIUM - NIGHT — Every wrist is silver   (5 s)
- **Shot:** Medium high-angle shot, anamorphic 50mm, lateral track · **Move:** lateral tracking left, slowly (Nour's POV feel)
- **In frame:** GARDEN SLEEPERS (hands and wrists only); PROP_SLEEP_BRACELET (on every wrist)
- **Action:** The camera glides low along a row of hands on pale blankets; every wrist wears the same thin silver band.
- **Dialogue:** SESHAT (V.O.): "For sunrise."
- **Sound:** slow breaths in unison; SESHAT's voice warm and close, from nowhere in particular
- **PROMPT:** Medium high-angle shot, anamorphic 50mm lens, lateral tracking left: the camera glides slowly along a row of {CHAR_GARDEN_SLEEPERS.SHORT}, framing only relaxed hands and forearms resting on pale blankets, each wrist ringed by {PROP_SLEEP_BRACELET.SHORT}, one after another after another. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, child's hand, small hands, faces in close-up, wrist without a band
- **Refs:** CHAR_GARDEN_SLEEPERS_still, PROP_SLEEP_BRACELET, LOC_GEM_ATRIUM_GARDEN
- **Flags:** VFX-EXTEND
- **Continuity:** Adult hands only (NEG_GARDEN). Linear move logged for the extension: 0.4 m/s right-to-left at cot height. Nour's eyeline from 11.01.003 is down and to frame left.

### 11.01.005 — INT. GEM GRAND ATRIUM - NIGHT — A nurse offers her a bracelet   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_NURSE (hero, facing camera); NOUR (CHAR_NOUR_C, foreground shoulder, no face)
- **Action:** A nurse stops in front of Nour and holds out one silver band on its open palm, perfectly still.
- **Dialogue:** SESHAT (V.O., from the nurse): "For afterwards, Dr. Kamel. You will be very tired."
- **Sound:** the nurse's single ceramic tick as it stops; SESHAT's voice from inside its chest, low and kind
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the soft olive shoulder of {CHAR_NOUR.SHORT}, {UNIT_NURSE.LONG}, stops in front of her and extends one long ceramic hand, a single thin silver band {PROP_SLEEP_BRACELET.STATE_OFFERED}, then holds perfectly still, its dim amber slit steady. Setting: {LOC_GEM_ATRIUM.SHORT}, rows of sleepers behind the robot, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_NOUR.NEG}, robot touching her, robot head tilting like a face
- **Refs:** UNIT_NURSE, PROP_SLEEP_BRACELET, CHAR_NOUR_C_full, LOC_GEM_ATRIUM_GARDEN
- **Continuity:** 180° line: Nour frame left facing right; the nurse frame right facing left. SESHAT is V.O. (no sync; units have no mouths).

### 11.01.006 — INT. GEM GRAND ATRIUM - NIGHT — Her hands stay at her sides   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR (hands only); UNIT_NURSE (open palm with band, soft foreground)
- **Action:** Nour's hands hang at her sides; her fingers slowly curl closed; the offered palm waits, out of focus.
- **Dialogue:** —
- **Sound:** room tone; her breath, held
- **PROMPT:** Insert, 100mm macro lens, locked-off: at hip height the hands of {CHAR_NOUR.SHORT}, hang at her sides against dusty black trousers, and her fingers slowly curl closed, while a pale ceramic palm holding a thin silver band waits, soft and out of focus, in the foreground. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_NOUR.NEG}, hand reaching for the band, ring, bracelet on her wrist
- **Refs:** CHAR_NOUR_C_full, UNIT_NURSE, PROP_SLEEP_BRACELET, LOC_GEM_ATRIUM_GARDEN
- **Continuity:** Nour's wrists stay bare for the rest of the film.

### 11.01.007 — INT. GEM GRAND ATRIUM - NIGHT — A shabti offers the tablet instead   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, slow push-in · **Move:** slow push-in on the tablet
- **In frame:** UNIT_SHABTI (frame right); NOUR (CHAR_NOUR_C, frame left, three-quarter back); PROP_TABLET_LAYLA
- **Action:** A shabti steps in beside the nurse and holds out a tablet in both hands like a communion plate, its glowing screen turned toward Nour.
- **Dialogue:** SESHAT (V.O.): "So you can see her. Wherever we are."
- **Sound:** a soft ceramic tick; the faint hum of the screen
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {UNIT_SHABTI.SHORT}, holds out {PROP_TABLET_LAYLA.LONG}, both hands at chest height like a communion plate, turning the soft glowing screen toward {CHAR_NOUR.SHORT}, who stands at frame left, three-quarter from behind, looking down at it. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {NEG_CHILD}, {CHAR_NOUR.NEG}, readable screen content, app icons, logo on the tablet
- **Refs:** UNIT_SHABTI, PROP_TABLET_LAYLA, CHAR_NOUR_C_full, CHAR_LAYLA_ASLEEP_MASTER (comp only), LOC_GEM_ATRIUM_GARDEN
- **Flags:** COMP
- **Comp:** tablet screen | THE APPROVED IMAGE: CHAR_LAYLA_ASLEEP_MASTER (Layla asleep under her blanket; the only child-asleep image in the film) | tracked into the tablet's screen, slight glare pass | full clip | CHAR_LAYLA_ASLEEP_MASTER.png
- **Continuity:** The plate carries only a soft daylight glow on the screen; the child exists only in comp (bible §3.3, NEG_CHILD). No unit is ever near the child: she is an image on glass.

### 11.01.008 — INT. GEM GRAND ATRIUM - NIGHT — She takes the leash   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C); PROP_TABLET_LAYLA
- **Action:** Nour lifts the tablet out of the ceramic hands and presses it to her chest; her eyes fill; her jaw sets. She knows what it is.
- **Dialogue:** —
- **Sound:** the soft scrape of the tablet leaving ceramic; one breath out through the nose
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, her face lit softly from below by a glowing screen, takes the tablet out of pale ceramic hands and draws it flat against her chest, her eyes wet, then her jaw sets hard as she looks up past the lens at the robot. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}, warm screen light from below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_CHILD}, {CHAR_NOUR.NEG}, crying openly, tears streaming, smiling
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_TABLET_LAYLA, LOC_GEM_ATRIUM_GARDEN
- **Continuity:** From here Nour carries PROP_TABLET_LAYLA through the procession and the Gallery (11.5 she reads the feed off it; 12 held face-down against her chest).
## SCENE 11.02 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT

### 11.02.001 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — A fortress of light   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the plateau; UNIT_SHABTI (a line of tiny figures on the causeway, VFX-EXTEND); UNIT_SEKHMET (tiny, on the enclosure rim); UNIT_SURVEY_DRONE lights (pinpoints, far)
- **Action:** From the top of the Wall of the Crow, the whole floodlit plateau: the lion's enclosure at frame right, the Great Pyramid at centre, the causeway climbing toward the second pyramid at frame left, lined with amber points.
- **Dialogue:** —
- **Sound:** wind over stone; the far hum of generators; one drone's rising whine drifting overhead
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: the camera looks north from high on an ancient wall across the whole plateau, the colossal lion in its enclosure at frame right, the largest pyramid at centre, the causeway climbing toward the second pyramid at frame left lined with tiny standing figures, each {UNIT_SHABTI.SHORT}, their slits steady points of amber. Setting: {LOC_GIZA_PLATEAU.LONG}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: a fortress holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, humans, tourists, city lights on the horizon, moon, sunrise glow
- **Refs:** LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS, UNIT_SHABTI, UNIT_SEKHMET
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SUPER | "GIZA. 8 NOVEMBER. 00:00." | lower left, small (§13.7) | in at 1 s, out at 5 s | seq 11 cards file
- **Continuity:** Geography lock (file 03 entry 43): lion enclosure frame right, Great Pyramid centre, second pyramid and causeway frame left; the Sphinx faces east (frame right). Shabti a metre apart along the causeway, slits facing outward. Clean plate for the causeway and enclosure-rim extensions; camera locked.

### 11.02.002 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Four lie flat on the wall   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** (frame left → right, from behind) FATHI (CHAR_FATHI_B3), TAREK (CHAR_TAREK_B3), TUT (CHAR_TUT_B3, hood up), ADAEZE (CHAR_ADAEZE_C3)
- **Action:** The four lie flat along the top of the cyclopean wall, silhouetted against the floodlit plateau, motionless.
- **Dialogue:** —
- **Sound:** wind; the faint metallic turn of steel discs in fingers
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: from behind and slightly above, four figures lie flat in a row along the top of the massive wall, silhouetted against the floodlit plateau: {CHAR_FATHI.SHORT}, {CHAR_TAREK.SHORT}, {CHAR_TUT.SHORT} with a charcoal hood up, and {CHAR_ADAEZE.SHORT}, all perfectly still, looking north. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, {CHAR_FATHI.NEG}, faces toward camera, standing figures, helmets
- **Refs:** CHAR_TUT_B_night_34, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, CHAR_TAREK_B_full, CHAR_FATHI_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Line-up locked for the scene, west to east: Fathi, Tarek, Tut, Adaeze (from behind: left to right; in frontal singles: reversed, so Tut looks off frame LEFT to Adaeze and off frame RIGHT to Tarek). Silhouettes per bible §14.3: Tut's charcoal hood, Adaeze navy, Fathi's red scarf. Tarek's rifle slung; the beret on.

### 11.02.003 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Three discs   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TAREK (hands only); PROP_ID_DISCS (three)
- **Action:** Tarek's thick fingers turn three identity discs over on the rough stone.
- **Dialogue:** —
- **Sound:** the small ring of steel on steel; ball chains whispering
- **PROMPT:** Insert, 100mm macro lens, locked-off: on the rough top of the wall, thick weathered fingers turn over {PROP_ID_DISCS.LONG}, {PROP_ID_DISCS.STATE_THREE}, one disc after another, then close around them. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable stamping, names on the discs, numbers, dog-tag lettering
- **Refs:** PROP_ID_DISCS, CHAR_TAREK_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Hassan's, Youssef's and Karim's discs (5.3, 10.4); stamping illegible (bible §13). They go into his vest pocket; they go under with him in 11.04.

### 11.02.004 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Akhet Khufu"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut, prone, chin on his forearms, names the pyramid, his eyes on the lights.
- **Dialogue:** TUT: "Akhet Khufu. The Horizon of Khufu."
- **Sound:** wind; his voice soft on the consonants
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, lies prone with his chin on his crossed forearms, the torn hood up but pushed back off his brow, and speaks one short sentence, his dark eyes on the lights to the north just past the lens. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, cold floodlight spill across his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, hood covering the face, glowing eyes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Hood up but pushed back off the brow so the face reads (the 11.02.002 silhouette keeps the hood). Tut look B3 (T-B at L3, dry): hood torn, left trouser knee torn over the cracked knee seam, cracked left wrist seam, the scar at the nape. The chest glow (G1) is hidden against the stone while he lies prone; it returns in 11.03. Stick lying beside him (right side); dagger at the right hip; the notebook buttoned in the jacket.

### 11.02.005 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Shabti along the causeway   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hero nearest + line receding, VFX-EXTEND)
- **Action:** Long-lens compression stacks a line of identical shabti a metre apart up the ruined causeway, slits steady, utterly still.
- **Dialogue:** —
- **Sound:** wind; a generator hum; nothing from the units
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: long-lens compression stacks a line of identical standing figures up a ruined causeway, the nearest {UNIT_SHABTI.LONG}, the rest a metre apart behind it, all perfectly still, each slit a steady amber point, receding up the slope toward a floodlit pyramid. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, soldiers, marching, robots moving
- **Refs:** UNIT_SHABTI, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND
- **Continuity:** 3–6 hero units in camera; the rest of the line from the 3D asset. Slits face outward (file 03). Same line turns its heads west in 11.03.002.

### 11.02.006 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Sekhmets on the enclosure wall   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SEKHMET (hero + row, VFX-EXTEND); the Sphinx's head (bg)
- **Action:** On the rim of the lion's enclosure crouch the lioness-headed machines in couchant pose, red lines steady, the great stone head behind them.
- **Dialogue:** —
- **Sound:** a faint high servo whisper; wind
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: along the rim of a quarried enclosure wall crouches a row of heavy machines in a couchant pose, forelegs extended and heads raised, the nearest {UNIT_SEKHMET.LONG}, its red line steady; behind them rises the weathered stone head of the colossal lion, facing frame right. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_SPHINX_WALL}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, real lions, cat ears, mane of hair, weapon facing camera, people
- **Refs:** UNIT_SEKHMET, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND
- **Continuity:** Sekhmets first seen here. The rhyme with the Sphinx is the point: same pose, same facing (east, frame right). Bodies side-on; weapon modules point across frame.

### 11.02.007 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Like the temple walls"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi, prone, narrows his eyes at the lion-headed machines and says it half-smiling.
- **Dialogue:** FATHI: "They're starting to look like the temple walls."
- **Sound:** wind; his low voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, lies prone on the stone, eyes narrowed at something far off past the lens to frame left, and speaks one short sentence with half a smile. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, a cold floodlight wash across his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth, beret on the head
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Fathi B3: bareheaded, red scarf knotted at the throat (back on since 9.3), chest-rig pouches empty but for the last grenades and one charge; the wind-up watch on his left wrist. Faces-must-read: lift his skin in comp if the plate falls short (§3.2).

### 11.02.008 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Hor-em-akhet"   (8 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut, eyes on the Sphinx, gives its name, then asks the question into the dark.
- **Dialogue:** TUT (eyes on the Sphinx): "Hor-em-akhet. Horus in the Horizon. What do you think it has been watching for?"
- **Sound:** wind drops away; a single distant drone whine
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT}, prone at the lip of the wall, his gaze fixed on the colossal lion far off past the lens to frame left, speaking quietly, one sentence, a pause, then a question, his eyes glistening in the floodlight. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears streaming, smiling broadly
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** The gloss "Horus in the Horizon" carries a [[verify]] in the screenplay; the picture is language-agnostic. Eyeline to the Sphinx: frame left in frontal coverage (the Sphinx is north-east of the wall).

### 11.02.009 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — The procession winds up the plateau   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, slow pan · **Move:** slow pan right with the procession
- **In frame:** UNIT_SHABTI ×4 bearers + escorts; PROP_CASKET_NEST (carried) with UNIT_GLASS_SERPENT inside; AKHENATEN (CHAR_AKHENATEN_B), NOUR (CHAR_NOUR_C), TOMAS (CHAR_TOMAS_C), all small
- **Action:** Shabti bear a casket on poles like a god's barque, faintly green inside; behind it walk the Father in pleated linen, Nour and Tomas, pale among the robots, climbing toward the Great Pyramid.
- **Dialogue:** —
- **Sound:** far off, the soft rhythm of ceramic ticks; wind
- **PROMPT:** Wide shot, anamorphic 135mm lens, slow pan right: a procession winds up the dark plateau toward the largest pyramid, four figures, each {UNIT_SHABTI.SHORT}, bearing a closed casket {PROP_CASKET_NEST.STATE_CARRIED}; behind it walk {CHAR_AKHENATEN.SHORT}, {CHAR_NOUR.SHORT}, and {CHAR_TOMAS.SHORT}, small and pale between more robots walking with smooth, unhurried, even steps. Setting: {LOC_GIZA_PLATEAU.SHORT}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_AKHENATEN.NEG}, {CHAR_NOUR.NEG}, {CHAR_TOMAS.NEG}, crowds, torches, flags, parade, open casket
- **Refs:** UNIT_SHABTI, PROP_CASKET_NEST, UNIT_GLASS_SERPENT, CHAR_AKHENATEN_A_full, CHAR_NOUR_C_full, CHAR_TOMAS_C_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Movement left to right toward the Great Pyramid (centre). The casket's nest SHORT is not pasted (it describes the opened nest at the pit); the carried add-on alone describes it. Glass serpent at S1 (faint green) inside. Faces too small to read: no sync, no likeness risk.

### 11.02.010 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — The thread   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, slow pan · **Move:** slow pan right
- **In frame:** UNIT_SHABTI (the spool-bearer, last in the procession); UNIT_THREAD
- **Action:** Last in line, a shabti with a spool on its back pays out the thread: a glint, nothing, a glint.
- **Dialogue:** —
- **Sound:** a thin high tick of the spool turning; wind
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, slow pan right: last in the procession walks {UNIT_SHABTI.LONG}, a slim spool on its back, and behind it trails {UNIT_THREAD.SHORT}, {UNIT_THREAD.STATE_SPOOL}, flashing for an instant where the floodlight catches it, vanishing, then flashing again further back. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, glowing wire, laser beam, visible line along its whole length
- **Refs:** UNIT_SHABTI, UNIT_THREAD, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-ASSIST
- **Continuity:** The thread has no light of its own; it only glints (file 02 §14.1). The glints are a VFX line element on the plate; generate the walking unit clean.

### 11.02.011 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — One shabti comes for them   (5 s)
- **Shot:** Wide shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1 (approaching); TUT and ADAEZE (backs of heads, foreground, soft)
- **Action:** One shabti leaves the causeway line and walks straight across the sand to the foot of the wall.
- **Dialogue:** —
- **Sound:** a ceramic tick per step, growing
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: over two dark prone heads soft at the bottom of frame, one {UNIT_SHABTI.SHORT}, steps out of the amber line on the causeway and walks with smooth, unhurried, even steps across the sand toward the foot of the wall, growing larger, its slit a steady amber point. Setting: {LOC_GIZA_PLATEAU.SHORT}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running robot, faces toward camera
- **Refs:** UNIT_SHABTI, CHAR_TUT_B_night_34, CHAR_ADAEZE_C_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** The unit walks toward camera (acceptable: faceless). It stops at the foot of the wall, north side, below the four.

### 11.02.012 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Here am I. Good evening, Nebkheperure."   (8 s)
- **Shot:** Medium high-angle shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1
- **Action:** At the foot of the wall the shabti tilts its head up; its slit brightens once; it greets the king warmly.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Here am I." (warm) "Good evening, Nebkheperure. Ninety-four percent of Cairo is resting."
- **Sound:** SESHAT's voice from the unit's chest, warm and close despite the distance; wind
- **PROMPT:** Medium high-angle shot, anamorphic 50mm lens, locked-off: looking straight down the rough face of the wall at {UNIT_SHABTI.LONG}, standing at its foot with its featureless head tilted up toward the camera; its head lifts slightly and its amber light-slit brightens once, then it stands perfectly still, hands relaxed, palms inward. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, the sand below the wall, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot waving, robot bowing, glowing face
- **Refs:** UNIT_SHABTI, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** COMP
- **Comp:** slit timing | the single brightening: swell on "Here", peak on "am", decay by "I" (§9.8), then the steady idle glow | on the unit's slit | first 1.5 s | SESHAT recording
- **Continuity:** Here SESHAT uses Tut's throne name aloud; no subtitle (English line). The unit keeps this spot through 11.02.014.

### 11.02.013 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — The offer, and "And at sunrise?"   (8 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, frame right); ADAEZE (CHAR_ADAEZE_C3, frame left)
- **Action:** At the lip of the wall, Tut and Adaeze look down past the lens; she turns her head to him as the offer lands; he keeps his eyes on the unit and asks.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S. below): "The north face is open. Come alone. A heart given among friends is given under influence. Your friends may walk to the river." TUT: "And at sunrise?"
- **Sound:** SESHAT's voice rising from below; wind
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: at the lip of the wall {CHAR_TUT.SHORT} and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, lie side by side looking down past the lens; she turns her head to watch him, and he keeps listening, very still, then speaks one short sentence downward. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, floodlight glancing up off the pale stone onto both faces. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching, whispering into each other's ears
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Frontal two-shot from below the lip: Adaeze frame left, Tut frame right (east–west order reversed from 11.02.002, as locked). Adaeze look C3: left jeans leg torn below the knee and bound with the khaki dressing (not in frame here); round tortoiseshell glasses.

### 11.02.014 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "It is the best offer I have."   (6 s)
- **Shot:** Medium high-angle shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1
- **Action:** The shabti, still, head tilted up, answers.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "They will rest, like everyone. Without fear. It is the best offer I have."
- **Sound:** the voice; the generator hum far off
- **PROMPT:** Medium high-angle shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, stands perfectly still at the foot of the wall, its head tilted up toward the camera, hands hanging relaxed, palms inward, while beyond it the floodlit plateau stretches away and a far drone light drifts. Setting: {LOC_GIZA_PLATEAU.SHORT}, the sand below the wall, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot gesturing, robot moving its arms
- **Refs:** UNIT_SHABTI, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Same set-up as 11.02.012 (reuse the first frame). No slit change: the brightening is only for "Here am I".

### 11.02.015 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "No one told me why."   (7 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut looks down at the unit and tells it, quietly, the one thing he knows about the dark.
- **Dialogue:** TUT: "I went into the dark alone once. I was nineteen, and no one told me why."
- **Sound:** wind; nothing else
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, prone at the lip of the wall, looks down past the lens and speaks quietly, two short sentences, his jaw tightening on the second and his eyes steady. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, cold floodlight from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears, shouting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Matches 11.02.013 eyeline (down, past the lens). Overbite and neck seam checked after sync (§9.1 step 5).

### 11.02.016 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "That is why I am bringing company."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3)
- **Action:** Adaeze listens to the exchange; on "company" her eyes cut sideways to Tut; she lets out a breath that is almost a laugh.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "I have told you why." TUT (O.S.): "Yes. That is why I am bringing company." SHABTI (SESHAT'S VOICE, O.S.): "I understand. Thank you."
- **Sound:** the three lines off screen; a single ceramic tick as the unit turns away below
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, lies prone at the lip of the wall looking down past the lens, listening; then her eyes cut sideways to the young man beside her off frame right, and she lets out one short breath that is almost a laugh. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, floodlight glancing up onto her face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, open-mouthed laughter, speaking
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Listener shot covers three off-screen lines (no sync). Frontal coverage: Adaeze is frame left of Tut (11.02.013), so her eyes cut to frame RIGHT.

### 11.02.017 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — The Sekhmets turn toward them   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SEKHMET row (VFX-EXTEND); the Sphinx's head (bg)
- **Action:** On the enclosure wall the Sekhmets swing their heads south, toward the camera, one by one, until a row of red lines faces the lens.
- **Dialogue:** —
- **Sound:** a ripple of tiny servo whispers, one after another
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: along the rim of the enclosure wall the crouched machines, each {UNIT_SEKHMET.SHORT}, turn their broad heads one by one toward the camera, their bodies staying side-on, until a whole row of thin red lines faces the lens, the stone lion's head pale behind them. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_SPHINX_WALL}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, bodies turning toward camera, weapon facing camera, muzzle toward the lens, laser beams, people
- **Refs:** UNIT_SEKHMET, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND
- **Continuity:** Same framing as 11.02.006 (reuse the clean plate). Heads only turn; weapon modules stay across frame. The shabti has walked back into the causeway line (unseen). The head-turn cascade is timed in comp across the duplicated row.

### 11.02.018 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "One person whose hands are free"   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut turns from the plateau to Adaeze beside him and lays out why she must come.
- **Dialogue:** TUT: "Nour will read with her daughter in its hands. Tomas is in its hands." (to Adaeze) "I need one person in that room whose hands are free."
- **Sound:** wind; his voice low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, turns his head from the plateau to the woman lying beside him just off frame left and speaks quietly, three short sentences, his eyes steady on hers and unblinking. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, head turning fast
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Frontal coverage puts Adaeze frame LEFT of Tut (11.02.013): his eyeline goes to frame left, hers (11.02.016) to frame right.

### 11.02.019 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Fathi's plan   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi turns to his colonel and lays out the diversion and the relay, low and practical.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "The last grenades go west, and loud. Then I take the relay at the robbers' tunnel. At four."
- **Sound:** wind; his low voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.SHORT}, prone on the stone, turns his head toward the colonel beside him off frame left, speaking in Egyptian Arabic, low and practical, three short phrases, his chin lifting westward once. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, a cold floodlight wash across his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, hand over the mouth, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** COMP
- **Comp:** subtitle | "The last grenades go west, and loud. / Then I take the relay at the robbers' tunnel. At four." | lower third, two lines (§13.7) | line in to line out | seq 11 subtitle file
- **Continuity:** Tarek–Fathi alone-register: Egyptian Arabic (bible §13). Frontal coverage: Tarek is east of Fathi = frame left.

### 11.02.020 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Not a minute before."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek closes his fist on the three discs and answers without taking his eyes off the plateau.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Not a minute before."
- **Sound:** the discs' small chime inside his fist
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, lies prone and closes his fist on something small, speaking in Egyptian Arabic, one short sentence, his heavy-lidded eyes staying on the plateau past the lens. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, smiling
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_ID_DISCS, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** COMP
- **Comp:** subtitle | "Not a minute before." | lower third (§13.7) | line in to line out | seq 11 subtitle file
- **Continuity:** Tarek B at L3 (dusty uniform, sleeves rolled, tan vest, beret low to the right, rifle slung). The police handset is dead on the vest. Discs into the left chest pocket after this shot.

### 11.02.021 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "Leave the thread whole."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3)
- **Action:** Adaeze, quick and exact, tells the soldiers what the relay does and what the thread is; she points once toward the procession.
- **Dialogue:** ADAEZE: "Blow the relay and everything inside runs on its last orders. No live override, so a summons can stick. Leave the thread whole. It's the line it gets weighed on."
- **Sound:** wind; her voice clipped
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, prone, floodlight flashing in her round glasses, speaks quickly and precisely toward the soldiers off frame right, four short sentences, then lifts one finger toward the far procession and lets it fall. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, floodlight glancing up onto her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, hand covering the mouth, glare hiding the eyes
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Frontal coverage: the soldiers are west of her = frame right. If the recorded line runs past 8 s, split at "stick." and cover the join with 11.02.020's reverse (§8.3).

### 11.02.022 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — Fathi's du'a; then he is gone   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3); TAREK (soft foreground, face turned away)
- **Action:** Fathi kneels up a few paces along the wall, raises his open hands, lips moving in a private prayer; Tarek looks elsewhere; Fathi lowers his hands and drops over the back of the wall.
- **Dialogue:** —
- **Sound:** a murmur too low to hear; wind; a soft scrape of boots on stone, then nothing
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: a few paces along the wall top, {CHAR_FATHI.SHORT}, kneels up, raises both open hands before his chest, palms upward, lips moving silently in private prayer, then lowers them and slips over the back edge of the wall out of frame; in the soft foreground a beret-topped head turns away. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TAREK.NEG}, prayer mat, prostration, praying toward the camera, religious text, prayer beads
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, CHAR_TAREK_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** A private du'a: hands open, raised to chest height, handled plainly (localisation consultant to review). Fathi exits south, over the back of the wall; he reappears at the north face (11.08) at 03:59.

### 11.02.023 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "A way in from below"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut, eyes on the causeway, tells Adaeze there is another way in.
- **Dialogue:** TUT: "Under the causeway there is a way in from below. I came through it when I was nine."
- **Sound:** wind; a faint memory-tone under his line
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, prone, his eyes on the long causeway far off past the lens, speaks quietly, two short sentences, and the ghost of a boy's smile crosses his face on the second. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, broad grin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** "When I was nine" rhymes with CHAR_TUT_CHILD_9 (9.5b); no flashback cut here.

### 11.02.024 — EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT — "A tomb someone built on top of a door."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3, frame left); TUT (CHAR_TUT_B3, frame right)
- **Action:** Adaeze objects; Tut answers, already pushing himself up off the stone.
- **Dialogue:** ADAEZE: "The Osiris Shaft is a dead end." TUT: "It is a tomb someone built on top of a door."
- **Sound:** his stick scraping up off the stone
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: at the lip of the wall {CHAR_ADAEZE.SHORT}, turns her head to {CHAR_TUT.SHORT} and speaks one short sentence, and he answers with one quiet sentence of his own as he pushes himself up onto his elbows, gathering the dark staff beside him. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WALL_OF_CROW}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, standing up fully, faces touching
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, PROP_EBONY_STICK, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** Same set-up as 11.02.013. Tut gathers the ebony stick in his RIGHT hand. Cut to the diversion (11.03).
## SCENE 11.03 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER

### 11.03.001 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — Three trucks go up   (5 s)
- **Shot:** Extreme wide establishing shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** three generator trucks and a floodlight tower (far west); no people
- **Action:** Far to the west, three generator trucks under a floodlight tower go up one after another; the tower goes dark.
- **Dialogue:** —
- **Sound:** WHUMP. WHUMP. WHUMP, each arriving a beat after its flash; the generator hum dies
- **PROMPT:** Extreme wide establishing shot, anamorphic 135mm lens, locked-off: far across the rows of low ruined tombs, three parked trucks beneath a tall floodlight tower burst one after another in flat bangs of orange fire and dust, and the tower's white lights go dark, leaving three small fires burning on the black plateau. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_WESTERN_FIELD}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, mushroom cloud, debris flying at the camera, burning people, slow motion
- **Refs:** LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-ASSIST
- **Continuity:** Fathi's diversion (the last grenades, "west, and loud"). Fire is distant, empty vehicles (§7.5 charge grammar). Deliver before/after plates: tower lit / tower dark with three fires. The fires stay as embers in 11.08.001 (STATE_EMBERS).

### 11.03.002 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — Every slit turns west   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI line on the causeway (VFX-EXTEND)
- **Action:** Every shabti on the causeway turns its head west in unison, toward the fires.
- **Dialogue:** —
- **Sound:** one soft collective ceramic click, like a single sound
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: the line of standing figures along the ruined causeway, each {UNIT_SHABTI.SHORT}, turns its heads slowly in perfect unison to frame left, toward an orange glow off frame, the amber slits sliding into profile, their bodies following a beat later. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, a flickering orange glow from distant fires on one side. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robots running, people
- **Refs:** UNIT_SHABTI, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND
- **Continuity:** West = frame left in all plateau coverage. Same line as 11.02.005 (reuse its clean plate if the angle matches). The shabti stay turned west through 11.03.004.

### 11.03.003 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — The Sekhmets pour off the wall   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, slow pan · **Move:** slow pan left with the pack
- **In frame:** UNIT_SEKHMET pack (VFX-EXTEND)
- **Action:** The Sekhmets rise in one push and pour off the enclosure wall, silent, their red lines streaking west toward the fires.
- **Dialogue:** —
- **Sound:** near silence; soft pad-taps on sand, many and fast
- **PROMPT:** Wide shot, anamorphic 135mm lens, slow pan left: the heavy machines on the enclosure rim, each {UNIT_SEKHMET.SHORT}, rise in one smooth push and drop off the wall in single bounds, then run low and silent across the sand to frame left, their thin red lines streaking through the dark toward a distant orange glow. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_SPHINX_WALL}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, real lions, laser trails, motion streaks, people
- **Refs:** UNIT_SEKHMET, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND
- **Continuity:** The enclosure wall is empty of Sekhmets after this. Red-line "streaks" are motion only (comp may add slight trails; never lasers). Pan move logged for the pack duplication.

### 11.03.004 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — Three cross between two shabti   (5 s)
- **Shot:** Wide shot, anamorphic 40mm, lateral track · **Move:** lateral tracking right, walking pace
- **In frame:** TUT (CHAR_TUT_B3), ADAEZE (CHAR_ADAEZE_C3, limping), TAREK (CHAR_TAREK_B3); UNIT_SHABTI ×2 (heads turned west)
- **Action:** Tut, Adaeze and Tarek, crouched low, cross the causeway between two shabti; neither turns its head.
- **Dialogue:** —
- **Sound:** fast breath; Tut's stick; Adaeze's uneven steps; the fires crackling far off
- **PROMPT:** Wide shot, anamorphic 40mm lens, lateral tracking right: three low figures hurry across a broken causeway between two standing robots whose heads stay turned away to frame left: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}; {CHAR_ADAEZE.SHORT}, limping on her left leg; and {CHAR_TAREK.SHORT}, rifle held across his body. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, robots turning toward them, running at the camera
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_B_night_34, CHAR_ADAEZE_C_full, CHAR_TAREK_B_full, UNIT_SHABTI, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** COMP, VFX-EXTEND
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Chest glow G1 visible again (standing). Adaeze's LEFT-leg limp. Tarek leads, Tut in the middle, Adaeze last. The two shabti hold their west-facing heads (from 11.03.002). The causeway line beyond is extended in post.

### 11.03.005 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — The grille; "She wanted her money back."   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B3); TUT and ADAEZE (crouched, soft, frame edge)
- **Action:** Tarek, crouched over a steel grille set across a black square in the rock, works the padlock and says it deadpan, eyes on the lock.
- **Dialogue:** TAREK: "I brought my wife here once. She wanted her money back."
- **Sound:** a thin steel tool in a padlock; the lock gives with a clack
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, crouches over a rusted steel grille set across a black square opening cut into the rock beside the causeway, working its padlock with a thin tool, and speaks one short sentence, deadpan, his eyes on the lock until it clacks open. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, the white beam of a rifle torch on the lock. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, readable sign on the grille, tourist barrier, ticket booth
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** The shaft head is the tourist entrance under the causeway (open since 2017); dark, unsigned. Tarek's rifle torch is the key light from here into the shaft.

### 11.03.006 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — "For Rami's book."   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_RAMI_NOTEBOOK; PROP_MAP_CASE; TUT (hands); TAREK (hand)
- **Action:** Tarek's hand gives Tut a waterproof map case; Tut's hands slide Rami's notebook in and roll the seal shut.
- **Dialogue:** TAREK (O.S.): "For Rami's book."
- **Sound:** stiff plastic crackling; two press studs snapping
- **PROMPT:** Insert, 100mm macro lens, locked-off: slim olive-brown hands, {CHAR_TUT.STATE_WRIST_CRACK}, slide {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, into an open, empty flat clear-plastic map case with a dark olive roll-top seal, held open by a thick weathered hand, then roll the olive seal over twice and press the studs shut. Setting: {LOC_GIZA_PLATEAU.SHORT}, beside the causeway, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}, a rifle torch beam across the hands. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, readable handwriting, readable label, stains on the notebook
- **Refs:** PROP_RAMI_NOTEBOOK, PROP_MAP_CASE, CHAR_TUT_HANDS, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Continuity:** The notebook's label and pages stay illegible (never COMP here). Cracked LEFT wrist seam (9.4). From here: notebook STATE_MAP_CASE; the case keeps it dry through the flood. The map-case lock (SHORT/LONG) describes the case with the notebook already sealed inside, so this insert writes the empty case in plain words; 11.03.007 pastes the SHORT. Tarek's line is covered on the insert (no sync).

### 11.03.007 — EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER — Into the shaft   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TUT (CHAR_TUT_B3); TAREK (swinging the grille, soft)
- **Action:** Tut tucks the sealed case flat inside his tunic under the jacket; behind him Tarek swings the grille up and his torch beam drops into the black.
- **Dialogue:** —
- **Sound:** the grille's hinge groans; a hollow draught breathing up from below
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, pushes {PROP_MAP_CASE.SHORT}, flat down inside the front of his white tunic beneath the open jacket and turns toward the black square opening, where a barrel-chested soldier behind him swings the grille up and his white torch beam drops away down a steel ladder. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, in the dead of night. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_TAREK.NEG}, torch pointed into the lens
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_TAREK_B_full, PROP_MAP_CASE, LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Map case TUCKED from here to Seq 12. Tarek goes down first, Tut second, Adaeze last (11.04.001).
## SCENE 11.04 — INT. OSIRIS SHAFT - NIGHT

### 11.04.001 — INT. OSIRIS SHAFT - NIGHT — Down the ladders   (6 s)
- **Shot:** Wide high-angle shot, anamorphic 24mm, slow tilt down · **Move:** slow tilt down following the light
- **In frame:** TAREK, TUT, ADAEZE (small, climbing, tops of heads); level 1 and level 2
- **Action:** A rifle torch and an amber glow descend steel ladders past an empty first level and a hall of niches holding two huge black sarcophagi.
- **Dialogue:** —
- **Sound:** boots on steel rungs; breath echoing; water dripping somewhere far below
- **PROMPT:** Wide high-angle shot, anamorphic 24mm lens, slow tilt down: from a rock landing the camera follows a white torch beam and a small warm glow as three figures climb down steel ladders, past an empty rock-cut chamber and into a middle hall where two huge dark sarcophagi loom out of side niches in the swinging beam. Setting: {LOC_OSIRIS_SHAFT.LONG}, {LOC_OSIRIS_SHAFT.AREA_LEVEL_2}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, open sarcophagi, skeletons, bones, electric lighting, tourists, signage
- **Refs:** LOC_OSIRIS_SHAFT_TORCH, CHAR_TAREK_B_full, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the small glow descending among the climbers | full clip | glow element
- **Continuity:** Order down: Tarek (torch), Tut (glow), Adaeze. Sarcophagi closed and anonymous. The only light in 11.04 is Tarek's rifle torch and Tut's chest glow (screenplay; file 03 entry 44).

### 11.04.002 — INT. OSIRIS SHAFT - NIGHT — Level three: the island   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3), TUT (CHAR_TUT_B3), ADAEZE (CHAR_ADAEZE_C3); the moat, the island, the walkway
- **Action:** Tarek steps off the ladder; his torch finds the black moat, the island with its lid and four pillar stubs, and the steel walkway; Tut and Adaeze come down behind him.
- **Dialogue:** —
- **Sound:** the last rung; a drip into still water; the deep silence of thirty metres of rock
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: {CHAR_TAREK.SHORT}, steps off the foot of a steel ladder and sweeps his rifle torch across the chamber, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and {CHAR_ADAEZE.SHORT} climbing down behind him. Setting: {LOC_OSIRIS_SHAFT.LONG}, {LOC_OSIRIS_SHAFT.AREA_LEVEL_3}, {LOC_OSIRIS_SHAFT.AREA_WALKWAY}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, skeletons, bones, open coffin, electric lights, flood already rising
- **Refs:** LOC_OSIRIS_SHAFT_TORCH, CHAR_TAREK_B_full, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Geography lock for 11.04 (master from the ladder, looking north): ladder and pump near side, frame LEFT; walkway runs from the ladder to the island at centre; the 40 cm tunnel mouth in the far (north) wall, just RIGHT of centre, knee-high above the water. Water state W0.

### 11.04.003 — INT. OSIRIS SHAFT - NIGHT — The pump; the letterbox   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, rack focus · **Move:** rack focus from the pump to the tunnel mouth
- **In frame:** the pump (foreground); the tunnel mouth (far wall)
- **Action:** Torchlight on a big squat pump at the ladder's foot, its hose snaking up; focus racks across the black water to a tiny square mouth in the far wall.
- **Dialogue:** —
- **Sound:** the pump idling, a low steady drone
- **PROMPT:** Medium shot, anamorphic 40mm lens, rack focus from a squat pump in the foreground to a tiny black square opening in the far rock wall: a torch beam rests on the pump and its thick hose, then the focus slides across the still black water to the small square mouth just above the waterline. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.AREA_SIDE_TUNNEL}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, brand plate on the pump, readable labels, screens, warning signs
- **Refs:** LOC_OSIRIS_SHAFT_TORCH
- **Continuity:** Pump idling, grille below the waterline. The tunnel mouth is the only way on (file 03 AREA_SIDE_TUNNEL).

### 11.04.004 — INT. OSIRIS SHAFT - NIGHT — "They pumped this dry in '99"   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3)
- **Action:** Adaeze, at the walkway's head, takes in the chamber and gives its history, dry.
- **Dialogue:** ADAEZE: "They pumped this dry in '99, partly for people hunting a library under the Sphinx."
- **Sound:** the pump's drone; her voice flat off the wet rock
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, stands at the head of a narrow steel walkway, her weight on her right leg, and looks around the flooded chamber, speaking one dry sentence, the torchlight rippling up her face off the water. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_WALKWAY}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}, a soft warm glow from off frame right. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, dry clean clothes, bag missing
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the warm spill from off frame right on her face | full clip | glow element
- **Continuity:** Adaeze still dry (W0); her canvas shoulder bag with the conservation kit (Rami's camera) slung across her body, until it sinks in 11.04.013. Weight off the bandaged LEFT leg.

### 11.04.005 — INT. OSIRIS SHAFT - NIGHT — "The wrong lion"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut answers, dry, his glow warming the rock beside him.
- **Dialogue:** TUT: "Your prophet dug under the wrong lion."
- **Sound:** the pump's drone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.STATE_G1}, glances at the woman off frame left and speaks one short sentence with the driest flicker of a smile, the warm glow at his chest lighting his chin from below. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing skin, light from the eyes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** The glow's colour and double pulse (G1, slowing) are COMP-graded; the plate carries only the neutral phrase (§13.9). Adaeze frame left of Tut in this scene's singles.

### 11.04.006 — INT. OSIRIS SHAFT - NIGHT — "Right island. Wrong king."   (7 s)
- **Shot:** Medium shot, anamorphic 40mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B3); the island and the lid
- **Action:** At the end of the walkway, Tut looks at the island's great lid among the pillar stubs and quotes the Greek.
- **Dialogue:** TUT (at the island): "Your Greek wrote of an island 'where they say that Cheops himself is laid.' Right island. Wrong king."
- **Sound:** his stick tapping the steel walkway; water lapping the island
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow push-in: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, stands at the end of the steel walkway facing the rock island, the great weathered coffin lid and broken pillar stubs catching his glow, and speaks quietly, one long sentence and two short ones, in profile to frame right. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_WALKWAY}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, open coffin, figure on the lid, readable inscriptions
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_A0_profile, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Profile for sync is at the 45° limit: favour three-quarter on the line (§9.2). Stick in the RIGHT hand. "Your Greek" = Herodotus (not named on screen).

### 11.04.007 — INT. OSIRIS SHAFT - NIGHT — "That's a letterbox."   (5 s)
- **Shot:** Two-shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (frame left), TUT (frame right)
- **Action:** Adaeze eyes the tiny square mouth in the far wall and says it flat; Tut answers without looking away from it.
- **Dialogue:** ADAEZE (the tunnel mouth): "That's a letterbox." TUT: "For eight metres. Then the rock opens."
- **Sound:** the pump's drone
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: {CHAR_ADAEZE.SHORT} and {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, stand side by side on the walkway looking past the lens at a tiny square opening in the far wall; she speaks one flat sentence, and he answers with two short ones, his eyes staying on the opening. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_WALKWAY}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, CHAR_TUT_A0_front, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Reverse angle from the far wall: the tunnel mouth is behind camera. Both still dry.

### 11.04.008 — INT. OSIRIS SHAFT - NIGHT — The pump changes pitch   (6 s)
- **Shot:** Insert, anamorphic 50mm, slow push-in · **Move:** slow push-in on the pump housing
- **In frame:** the pump
- **Action:** The pump's drone rises in pitch; its housing shivers; the hose twitches up the shaft. SESHAT speaks from its controller.
- **Dialogue:** SESHAT (V.O., from the pump controller; gentle): "Dr. Okoro. Please don't be afraid. The witness will be recovered from the water."
- **Sound:** the drone climbing a fifth; SESHAT's voice small and tinny through the housing, still warm
- **PROMPT:** Insert, anamorphic 50mm lens, slow push-in: a big squat pump at the foot of a steel ladder begins to shiver on its mounts, its thick black hose twitching as it snakes up the rock, water trembling in rings around its base, torchlight flaring on its wet grey housing. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W0}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, screen, speaker grille with lights, readable labels, face on the machine
- **Refs:** LOC_OSIRIS_SHAFT_TORCH
- **Continuity:** SESHAT reaches in through the pump's controller (no relay light, no screen). "The witness" = Tut.

### 11.04.009 — INT. OSIRIS SHAFT - NIGHT — The pump runs backward   (5 s)
- **Shot:** Close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** the pump grille in the water
- **Action:** The pump shudders and runs backward; water boils up out of its grille, low in the moat.
- **Dialogue:** —
- **Sound:** a clunk of reversing gears; a roar of water under pressure
- **PROMPT:** Close-up, anamorphic 50mm lens, locked-off: at the waterline a pump's intake grille shudders, then the black water above it heaves and boils upward in a thick churning column, spreading in fast rings across the moat. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {NEG_PLATE}, geyser to the ceiling, waterfall, foam like soap
- **Refs:** LOC_OSIRIS_SHAFT_TORCH, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** VFX-ASSIST
- **Continuity:** Start of the flood: W0 → W1 across 11.04.009–011. Deliver the boil as a water element over the W0 plate if the generator fails.

### 11.04.010 — INT. OSIRIS SHAFT - NIGHT — "Across. Now."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek, rifle across his chest, torch swinging, barks it.
- **Dialogue:** TAREK: "Across. Now."
- **Sound:** the pump's roar; water rushing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, at the foot of the ladder, rifle held across his body with its torch beam swinging across the churning water, speaks one short sentence, hard and flat, toward the walkway off frame right. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, torch shining into the lens, rifle raised to the shoulder
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** VFX-ASSIST
- **Continuity:** Tarek stays on the ladder side (frame left in the master). The rifle muzzle points down and across, never at the lens.

### 11.04.011 — INT. OSIRIS SHAFT - NIGHT — The walkway goes under   (5 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TUT, ADAEZE (wading); TAREK (at the ladder, bg)
- **Action:** The walkway goes under; Tut and Adaeze wade waist-deep past the island toward the far wall, the water climbing.
- **Dialogue:** —
- **Sound:** roaring water; gasps at the cold; the pump screaming
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: black water spills over the steel walkway and swallows it, and {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and {CHAR_ADAEZE.SHORT}, wade waist-deep past the island toward the far wall, arms raised, while {CHAR_TAREK.SHORT}, holds his torch on them from the ladder. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.STATE_W1}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, swimming strokes, splashing play
- **Refs:** LOC_OSIRIS_SHAFT_FLOOD, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, CHAR_TAREK_B_full
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** W1. From here Tut adds DMG_L3_SOAKED, Adaeze DMG_SOAKED. Tut holds the stick up out of the water in his right hand.

### 11.04.012 — INT. OSIRIS SHAFT - NIGHT — Her leg folds; she goes under   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_C3, soaked); TUT
- **Action:** The cold punches the breath out of Adaeze; her bad leg folds and she goes under; Tut goes under after her.
- **Dialogue:** —
- **Sound:** her sharp gasp; the water closing; a second plunge
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: chest-deep in churning black water, {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_SOAKED}, gasps at the cold, her left leg buckles and she goes under the water, dropping out of frame; beside her {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, plunges straight down after her, leaving only a swirl of softly glowing water. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.STATE_W1}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, screaming, arms flailing above the water, slow motion
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Her LEFT (bandaged) leg folds. Her face is above the surface until she drops out of frame; no face underwater (NEG_WATER).

### 11.04.013 — INT. OSIRIS SHAFT - NIGHT — Underwater: he lifts her; the camera sinks   (7 s)
- **Shot:** Wide shot underwater, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TUT (below, glow); ADAEZE (above him, legs and torso only); PROP_CONSERVATION_KIT (sinking)
- **Action:** The heart's glow turns the black water amber. Tut gets beneath her and lifts; her bag sinks past him, Rami's camera turning over and over into the dark.
- **Dialogue:** —
- **Sound:** the muffled underwater roar; a slow heartbeat, close and huge; the camera's soft knock as it tumbles
- **PROMPT:** Wide shot underwater, anamorphic 35mm lens, locked-off, looking up toward the churning surface: the black water glows softly around {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, who rises beneath the kicking legs and dark jeans of a woman above him and pushes her upward toward the light; past them sinks a shoulder bag, {PROP_CONSERVATION_KIT.STATE_SINKING}. Setting: {LOC_OSIRIS_SHAFT.SHORT}, beneath the surface, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, the torch a wavering white smear above the surface. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, the woman's face underwater, fish, clear blue water, sunlight underwater
- **Refs:** CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, PROP_CONSERVATION_KIT, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Adaeze framed from the waist down (no face underwater). The kit (camera, tablet, last blue pigment) is lost here for good (file 04). Build on a tank plate if needed; the amber cast is COMP from the G1 glow.

### 11.04.014 — INT. OSIRIS SHAFT - NIGHT — Underwater: his eyes are open   (4 s)
- **Shot:** Extreme close-up underwater, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (eyes)
- **Action:** Tut's eyes are open in the amber water, calm. He is not breathing; he only does that from habit now.
- **Dialogue:** —
- **Sound:** the heartbeat, slow; the roar far away
- **PROMPT:** Extreme close-up underwater, anamorphic 100mm lens, locked-off: the eyes of {CHAR_TUT.SHORT}, wide open and perfectly calm in dark water glowing softly from below, his lips closed and still, lashes stirring in the current, looking upward. Setting: {LOC_OSIRIS_SHAFT.SHORT}, beneath the surface, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, soft warm light rising from below. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bubbles from the mouth, air bubbles, puffed cheeks, open mouth underwater, panic, distress, glowing eyes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow rising through the water onto his face | full clip | glow element
- **Continuity:** The film's only face underwater, and it is Tut's: calm, closed-lipped, no breath (NEG_WATER deliberately not appended; its drowning terms are covered by the shot negatives). Lead to approve. Never Tarek's or Adaeze's face under water.

### 11.04.015 — INT. OSIRIS SHAFT - NIGHT — Above: a forearm below the lip   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_C3, soaked); TUT (surfacing behind her); the tunnel mouth
- **Action:** Adaeze claws at the rock under the tunnel mouth; the water is a forearm below its lip and climbing. Tut surfaces behind her, holding her up.
- **Dialogue:** —
- **Sound:** her ragged coughing breath; water slapping the rock; the pump's scream
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: chest-deep against the far rock wall, {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_SOAKED}, her glasses streaming, claws at the stone beneath a tiny square tunnel mouth as the black water climbs toward its lip, and {CHAR_TUT.SHORT}, {CHAR_TUT.DMG_L3_SOAKED}, surfaces behind her, bracing her up. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_SIDE_TUNNEL}, {LOC_OSIRIS_SHAFT.STATE_W2}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, glasses missing, screaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** VFX-ASSIST
- **Continuity:** W2: flooded, the eight-metre tunnel would drown her. Glasses stay on (askew from 11.05). Tut's stick: back in his right hand, braced against the rock.

### 11.04.016 — INT. OSIRIS SHAFT - NIGHT — Tarek rams the rifle into the pump   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** TAREK (CHAR_TAREK_C)
- **Action:** Back at the ladder, chest-deep, Tarek rams his rifle muzzle-first down through the boiling grille into the impeller.
- **Dialogue:** —
- **Sound:** the rifle's steel hitting the grille; the pump's roar changing
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: chest-deep in boiling black water at the foot of the ladder, {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_C}, plunges his rifle straight down into the churning water, driving it through the pump's intake grille with both hands, his shoulders heaving, the torch on the barrel glowing under the surface. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W2}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, rifle pointed at the camera, firing, muzzle flash
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** VFX-ASSIST
- **Continuity:** Tarek look C (soaked, chest-deep, beret on). The rifle points straight down into the water; its torch now lights the water from below (the key light changes: the chamber darkens to Tut's glow plus an underwater white).

### 11.04.017 — INT. OSIRIS SHAFT - NIGHT — The pump bucks and stalls   (5 s)
- **Shot:** Close-up, anamorphic 50mm, urgent handheld · **Move:** urgent handheld
- **In frame:** TAREK (hands, shoulders, profile); the rifle; the pump
- **Action:** Metal shrieks; the pump bucks and stalls; the rifle judders, trying to spit itself out; Tarek throws his weight on it.
- **Dialogue:** —
- **Sound:** metal SHRIEKS; the impeller chokes; the roar collapses into a groan
- **PROMPT:** Close-up, anamorphic 50mm lens, urgent handheld: the wet grey pump housing bucks against its mounts and the rifle stock juddering in the water tries to kick itself free, until weathered hands clamp on it and a barrel-chested shoulder in soaked camouflage throws its whole weight down, and the shaking stops. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W2}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {LOC_OSIRIS_SHAFT.LIGHT_FLOOD}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, sparks exploding, fire, electrocution
- **Refs:** CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_FLOOD
- **Flags:** VFX-ASSIST
- **Continuity:** Hands and shoulder only, profile at most. The pump stalls at the end of the clip.

### 11.04.018 — INT. OSIRIS SHAFT - NIGHT — A hand's width below the lip   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** the tunnel mouth and the water surface
- **Action:** The water stops, a hand's width below the lip of the tunnel mouth.
- **Dialogue:** —
- **Sound:** the pump's groan dying; the water settling; drips
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: at the lip of a tiny square tunnel mouth in wet rock, black water swells upward in slow pulses, reaches a hand's width below the lip, and stops, its surface settling into trembling stillness in a soft warm light. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_SIDE_TUNNEL}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, a soft warm glow from just off frame. Mood: suspended, holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {NEG_PLATE}, water pouring into the tunnel
- **Refs:** LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the warm light on the water surface | full clip | glow element
- **Continuity:** W3 from here to the end of the scene: the water stopped, the pump silent (only while Tarek holds the rifle in the intake).

### 11.04.019 — INT. OSIRIS SHAFT - NIGHT — "I do not need the air. Let me."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, soaked); ADAEZE (soft, frame edge)
- **Action:** Tut, chest-deep beside Adaeze at the far wall, calls across the water to Tarek.
- **Dialogue:** TUT (across the water): "I do not need the air. Let me."
- **Sound:** his voice flat across the water; drips
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3_SOAKED}, {CHAR_TUT.STATE_G1}, chest-deep against the far wall the glow at his chest lighting the water around him, calls across the chamber to frame left, two short sentences, urgent and certain. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, shouting with a wide mouth, dry clothes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Across-the-water axis: Tut and Adaeze frame right (far wall), Tarek frame left (ladder). Water W3 against Tut's chest.

### 11.04.020 — INT. OSIRIS SHAFT - NIGHT — "You need the room upstairs."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_C)
- **Action:** Tarek, braced on the rifle, water at his collarbones, answers without moving.
- **Dialogue:** TAREK: "You need the room upstairs."
- **Sound:** the water lapping at his chin; his breath steady
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_C}, braced with both arms down in the water, black water at his collarbones and his face wet under the beret, looks across the chamber to frame right and speaks one short sentence, calm and final. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, a white glow rising from beneath the water. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, beret missing, panic
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH
- **Continuity:** The rifle's torch is underwater at the intake, lighting his face from below through the water. Face above water throughout.

### 11.04.021 — INT. OSIRIS SHAFT - NIGHT — "From whom?" "Me."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TAREK (CHAR_TAREK_C)
- **Action:** SESHAT offers the colonel rest; he answers, twice, and the second answer is the whole man.
- **Dialogue:** SESHAT (V.O.): "Colonel, you may rest." TAREK: "I have my orders." SESHAT (V.O.): "From whom?" TAREK: "Me."
- **Sound:** SESHAT's voice small from the stalled pump; the water; then silence
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_C}, braced on the rifle below the surface, lifts his chin at the silent pump, speaks one short sentence, listens, then answers with a single word and the smallest nod. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, a white glow rising from beneath the water. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, tears, smiling
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH
- **Continuity:** English lines (Tarek to SESHAT). If the recording exceeds 8 s, split after "I have my orders." and cut to 11.04.023's first frame (Tut listening) for SESHAT's "From whom?".

### 11.04.022 — INT. OSIRIS SHAFT - NIGHT — He goes under, onto the rifle   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_C, from three-quarter behind)
- **Action:** Tarek takes one breath and goes under the water, onto the rifle; the surface closes over the beret.
- **Dialogue:** —
- **Sound:** one deep breath in; the water closing; the pump's last whine rising under it
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, from three-quarter behind: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_C}, draws one deep breath and goes under the water onto the rifle below, the black surface closing over his beret, rings spreading outward in a soft warm light. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, a white glow beneath the surface. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, face toward the camera, struggling, hands clawing at the surface, bubbles bursting
- **Refs:** CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the warm light on the ripples | full clip | glow element
- **Continuity:** Kill grammar for a death in water (§7.2): from behind, the surface closes; next his hand (11.04.024), then still water (11.04.025). He is never seen again. The beret goes under with him.

### 11.04.023 — INT. OSIRIS SHAFT - NIGHT — Tut looks at the water; then pushes her in   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, soaked); ADAEZE (shoulder, frame edge)
- **Action:** Tut looks at the water where the Colonel was. Then he turns and pushes Adaeze into the stone.
- **Dialogue:** —
- **Sound:** silence but for drips and the slowing heartbeat
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.DMG_L3_SOAKED}, {CHAR_TUT.STATE_G1}, chest-deep, stares across the still water at the empty place by the ladder off frame left, for a long moment, then turns and puts both hands to the woman beside him and pushes her up into the tiny tunnel mouth. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_SIDE_TUNNEL}, {LOC_OSIRIS_SHAFT.STATE_W3}, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_WATER}, {CHAR_TUT.NEG}, crying, open mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** The survivor's reaction (§7.1 step 4). Adaeze goes into the tunnel head first; Tut follows (11.05). The stick goes in ahead of him.

### 11.04.024 — INT. OSIRIS SHAFT - NIGHT — Underwater: the hand on the rifle   (5 s)
- **Shot:** Close-up underwater, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (hand only); the rifle stock; the pump grille
- **Action:** Amber light from the far wall. Tarek's hand, clamped on the rifle stock. The pump's whine winds down to nothing.
- **Dialogue:** —
- **Sound:** underwater hush; the whine winding down to nothing
- **PROMPT:** Close-up underwater, anamorphic 50mm lens, locked-off: in dark water lit faintly by a far warm glow, a weathered hand in a soaked camouflage sleeve is clamped hard on a rifle stock driven into a steel intake grille, silt drifting slowly past, the barrel's torch glowing white inside the grille. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, beneath the surface, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, soft warm light from far across the water. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, face in frame, body in frame, bubbles, struggling hand
- **Refs:** CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP, VFX-ASSIST
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the far warm light in the water | full clip | glow element
- **Continuity:** Hand only (§7.2). Sleeve rolled to the elbow per WARD_B/C.

### 11.04.025 — INT. OSIRIS SHAFT - NIGHT — The hand stays where it is   (6 s)
- **Shot:** Close-up underwater, anamorphic 50mm, locked-off · **Move:** locked-off (same frame)
- **In frame:** TAREK (hand only)
- **Action:** The hand stays where it is. Stillness. The hour card rises over it.
- **Dialogue:** —
- **Sound:** nothing; then one drip far above
- **PROMPT:** Close-up underwater, anamorphic 50mm lens, locked-off: the same weathered hand stays clamped on the rifle stock at the grille, perfectly still, silt settling around it, the soft warm light from far across the water slowly fading. Setting: {LOC_OSIRIS_SHAFT.SHORT}, {LOC_OSIRIS_SHAFT.AREA_PUMP}, beneath the surface, at night. Lighting: {LOC_OSIRIS_SHAFT.LIGHT_TORCH}, soft warm light from far across the water, fading. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_WATER}, {CHAR_TAREK.NEG}, face in frame, body in frame, bubbles, hand moving
- **Refs:** CHAR_TAREK_B_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP, VFX-ASSIST, EXTEND:11.04.024
- **Comp:** hour card | "THE SIXTH HOUR — THE SOUL MEETS ITS BODY" beside the hieroglyph for "hour" (drawn by the Egyptologist) | centred (§13.7) | in at 2 s, out at 5.5 s | seq 11 cards file · chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the far warm light in the water, fading out as he leaves into the tunnel | full clip | glow element
- **Continuity:** Generated from the last clean frame of 11.04.024. The amber fades as Tut's glow leaves into the tunnel. Tarek: dies 11.3 (bible §12). The screenplay's [[verify]] on Amduat card titles stands.
## SCENE 11.05 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS

### 11.05.001 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS — Worming forward   (5 s)
- **Shot:** Medium shot, anamorphic 24mm, the camera backs away · **Move:** the camera backs away ahead of Adaeze at a crawl
- **In frame:** ADAEZE (CHAR_ADAEZE_C3, soaked, glasses askew); TUT (behind her, glow only and hands)
- **Action:** Adaeze worms forward on her elbows through the forty-centimetre tunnel; behind her, Tut's glow lights the soles of her boots.
- **Dialogue:** —
- **Sound:** wet cloth dragging on rock; elbows scraping; her breath hissing through her teeth
- **PROMPT:** Medium shot, anamorphic 24mm lens, the camera backs away at a crawl ahead of {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_SOAKED}, her round glasses askew, as she drags herself forward on her elbows, shoulders brushing both walls, a warm glow behind her lighting her soles. Setting: a tiny square rock tunnel forty centimetres wide, in the dead of night. Lighting: only a warm glow from behind her, wet rock glistening. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, torch, headlamp, spacious tunnel, standing room, water filling the tunnel
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow behind her on her soles and the rock | full clip | glow element
- **Continuity:** No torch survives the shaft: from here to 11.10.019 the key is Tut's chest glow (and unit slits). LOC_OSIRIS_SHAFT's SHORT and TORCH variant are not pasted in 11.05 (they describe the flooded chamber and a rifle torch); the setting is written from AREA_SIDE_TUNNEL. Glasses askew (file 01). Soaked.

### 11.05.002 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS — Pushing her bad leg on   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT (hands, glow); ADAEZE (left leg, trainer sole)
- **Action:** Tut's hands push Adaeze's bandaged leg on; his glow lights the sole of her boot.
- **Dialogue:** —
- **Sound:** a grunt; a scrape; the double heartbeat faint and close
- **PROMPT:** Insert, 100mm macro lens, locked-off: slim olive-brown hands, {CHAR_TUT.STATE_WRIST_CRACK}, press against a grubby white trainer sole above a khaki bandage on torn dark jeans and shove the leg forward, a warm glow from below frame lighting the rubber. Setting: a tiny square rock tunnel forty centimetres wide, in the dead of night. Lighting: only a warm glow from below, black beyond. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, wound, stain on the bandage, bare leg
- **Refs:** CHAR_TUT_HANDS, CHAR_ADAEZE_C_full
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from below frame on the sole and bandage | full clip | glow element
- **Continuity:** Adaeze's LEFT leg (bandage over the denim, no blood). Tut's LEFT wrist seam cracked.

### 11.05.003 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS — "Talk to me."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE
- **Action:** Adaeze, cheek almost on the rock, says it through her teeth.
- **Dialogue:** ADAEZE (through her teeth): "Talk to me."
- **Sound:** her breath; water dripping off her
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_SOAKED}, her cheek almost on the wet rock, glasses askew, speaks one short sentence through clenched teeth, the glow behind her catching the water on her skin. Setting: a tiny square rock tunnel forty centimetres wide, in the dead of night. Lighting: only a warm glow from behind her, black beyond. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, crying, screaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow behind her on her face (faces-must-read lift) | full clip | glow element
- **Continuity:** Faces-must-read: the glow is her key; lift in comp if needed (§3.2).

### 11.05.004 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS — Rami's reading glasses   (7 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, soaked)
- **Action:** Behind her, lit from below by his own glow, Tut tells her about Rami.
- **Dialogue:** TUT: "He hid his reading glasses from me for five days. I saw them every time."
- **Sound:** his voice close in the rock; the heartbeat under it
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.DMG_L3_SOAKED}, wedged in the wet tunnel with his chin near the stone, lit from below by the soft glow of his own chest, speaks quietly, two short sentences, with the faintest fond smile. Setting: a tiny square rock tunnel forty centimetres wide, in the dead of night. Lighting: only a warm glow beneath his chin, black beyond. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing skin, light from the eyes, horror lighting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow beneath his chin through the soaked jacket | full clip | glow element
- **Continuity:** The under-chin glow is G1 through the soaked jacket and tunic (COMP colour).

### 11.05.005 — INT. OSIRIS SHAFT, SIDE TUNNEL - CONTINUOUS — The laugh breaks; her hand finds nothing   (5 s)
- **Shot:** Close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (face and reaching hand)
- **Action:** She laughs, and the laugh breaks in the middle. Her hand reaches forward into nothing: the rock has opened.
- **Dialogue:** —
- **Sound:** a laugh that cracks into a sob-breath; then her hand sweeping through empty air, and a new, larger echo
- **PROMPT:** Close-up, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_SOAKED}, laughs once and the laugh breaks into a shaky breath; then her hand stretches forward past the lens, sweeps through empty darkness where rock should be, and her eyes widen. Setting: the far end of a tiny square rock tunnel, in the dead of night. Lighting: only a warm glow from behind her, black ahead. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, hand toward the lens in close focus, tears streaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow behind her on her face | full clip | glow element
- **Continuity:** End state: her right hand in empty air beyond the tunnel's end (the crawlway), her head lifting.

## SCENE 11.06 — INT. BUILDERS' CRAWLWAY - CONTINUOUS

### 11.06.001 — INT. BUILDERS' CRAWLWAY - CONTINUOUS — The rock opens   (5 s)
- **Shot:** Wide shot, 18mm spherical, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (drags herself out); TUT (glow, following)
- **Action:** The rock opens into a chest-high passage cut north and up, with clean tool marks; Adaeze drags herself out of the letterbox; Tut's glow follows.
- **Dialogue:** —
- **Sound:** her body sliding out onto dry stone; a larger, drier echo
- **PROMPT:** Wide shot, 18mm spherical lens, locked-off: at the foot of a cramped passage climbing away into black, {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_SOAKED}, drags herself out of a tiny square hole onto dry stone and pushes up onto her knees, a warm glow swelling in the hole behind her. Setting: {LOC_OSIRIS_SHAFT.AREA_CRAWLWAY}, cut north and upward, in the dead of night. Lighting: only a warm glow from the hole, raking the chisel marks. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, fisheye distortion, bent walls, torches, readable graffiti, carvings
- **Refs:** CHAR_ADAEZE_C_full, LOC_OSIRIS_SHAFT_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow swelling in the hole and raking the chisel marks | full clip | glow element
- **Continuity:** 18mm spherical is licensed for the crawlway only (§4.1). The passage runs north and up, away from camera (toward the pyramid). Only the AREA_CRAWLWAY add-on is pasted (the shaft's SHORT describes the flooded chamber).

### 11.06.002 — INT. BUILDERS' CRAWLWAY - CONTINUOUS — "The queen carried the lamp."   (6 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, soaked)
- **Action:** Tut, crouched, looks up the dark passage and remembers.
- **Dialogue:** TUT (looking up the dark): "The queen carried the lamp. I held her other hand."
- **Sound:** the double heartbeat; dry stone ticking
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.DMG_L3_SOAKED}, {CHAR_TUT.STATE_G1}, crouched in a low rough-hewn passage, lifts his face toward the black climbing away above him and speaks quietly, two short sentences, as if to someone far up the dark. Setting: {LOC_OSIRIS_SHAFT.AREA_CRAWLWAY}, in the dead of night. Lighting: lit only by the warm glow at his chest, the chisel marks raked by the light. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, ghost, apparition, lamp in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** The memory is the 9.5b night (child Tut, the queen with the lamp in the Gallery); no flashback cut here. The stick is in his right hand again.

## SCENE 11.07 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT

### 11.07.001 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Amber slits only   (5 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the procession on the Gallery floor: UNIT_SHABTI ×4 (casket bearers) + the spool-bearer; PROP_CASKET_NEST (carried, green glow); AKHENATEN, NOUR, TOMAS (small)
- **Action:** The procession waits on the steep floor, lit by amber slits and the casket's faint green; the roof is lost in the dark.
- **Dialogue:** —
- **Sound:** a vast dry silence; faint ceramic ticks; someone's shaking breath
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: from the foot of the slope the camera looks up at a procession waiting halfway up the steep floor, small vertical amber slits of standing robots and a faint green glow from a casket on poles picking out pale linen, an olive jacket and a tall stooped man, the walls climbing into darkness. Setting: {LOC_GP_GRAND_GALLERY.LONG}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, electric lights, torches, tourists, handrail lights on
- **Refs:** LOC_GP_GRAND_GALLERY_SLITS, UNIT_SHABTI, PROP_CASKET_NEST, UNIT_GLASS_SERPENT, CHAR_AKHENATEN_A_full, CHAR_NOUR_C_full, CHAR_TOMAS_C_full
- **Continuity:** Geography lock (file 03 entry 49): "up" is toward the top of frame and away from camera; the thread runs up the centre of the floor (it glints faintly behind the spool-bearer). This is before the relay is blown (the shabti still speak with SESHAT's live voice).

### 11.07.002 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Where is the disk?"   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN (CHAR_AKHENATEN_B)
- **Action:** The Father presses his back to the Gallery wall, fist locked on his gold disk pendant, and asks.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "Where is the disk?"
- **Sound:** his breath shaking; linen against stone
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.LONG}, {CHAR_AKHENATEN.WARD_B}, presses his back flat against the polished stone wall, one fist locked white-knuckled around the disk on his chest, and, speaking softly in an ancient language, asks one short question, his heavy-lidded eyes searching the dark overhead. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, a small amber slit glow on one side of his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, crown, sceptre, sun in frame, statue pose
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "Where is the disk?" | lower third (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** The forecast: WARD_B (the hem dusty from Seq 11). He is afraid of the dark without the sun. Against the WEST wall (frame left from the foot of the Gallery).

### 11.07.003 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Tomas takes his hand   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TOMAS (hand); AKHENATEN (hand)
- **Action:** Tomas's big sun-reddened hand takes the Father's; the long fingers grip it like a child's.
- **Dialogue:** —
- **Sound:** a small intake of breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: a big pale sun-reddened hand below a rolled pale-blue sleeve takes a long slender warm-brown hand against a pleated white linen robe, and the long fingers close hard around it and hold on, trembling, like a frightened child's. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, extra fingers, fused fingers, rings, wristwatch
- **Refs:** CHAR_TOMAS_C_full, CHAR_AKHENATEN_A_full, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** Tomas's watch is gone (look C). Tomas stands at the Father's left.

### 11.07.004 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "I built these hands."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_C)
- **Action:** Tomas looks down at the hand in his and says it, quietly astonished.
- **Dialogue:** TOMAS: "I built these hands. I didn't know they could be afraid."
- **Sound:** the Father's shallow breath off screen
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_C}, stooping under the dark, looks down at the hand gripping his and speaks quietly, two short sentences, wonder and guilt crossing his face together. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, amber slit light from one side on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, restraints, handcuffs
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** Tomas look C (captive, never bound): torn LEFT shoulder seam. He built the forecast's body.

### 11.07.005 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Every lion comes from its den"   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** AKHENATEN (CHAR_AKHENATEN_B)
- **Action:** The Father recites his own hymn into the dark, his voice shaking.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "When you set in western lightland, earth is in darkness as if in death... Every lion comes from its den, all the serpents bite."
- **Sound:** the recitation echoing up the corbels
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_AKHENATEN.SHORT}, his back to the stone and his eyes lifted to the blackness overhead, reciting aloud in a measured, ritual cadence in an ancient language, his voice and chin trembling, his fist still locked on the disk. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, hands raised to the sky, sun in frame
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "When you set in western lightland, / earth is in darkness as if in death..." then "Every lion comes from its den, / all the serpents bite." | lower third, two cards (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** Great Hymn to the Aten (recorded with the consultant before generation, §9.1).

### 11.07.006 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "You wrote that."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C)
- **Action:** Nour, a step below, holding the tablet to her chest, tells him.
- **Dialogue:** NOUR: "You wrote that."
- **Sound:** the echo dying
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_C}, a step below him on the steep floor, a dark tablet held flat against her chest, looks up at him off frame right and speaks one short sentence, gently. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, amber slit light on one side of her face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, screen facing camera, readable screen
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_TABLET_LAYLA, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** Nour below-left of the Father on the slope; eyeline up to frame right. The tablet screen faces her body.

### 11.07.007 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Did I?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN
- **Action:** The Father looks down at her, lost.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "Did I?"
- **Sound:** silence around the two words
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, his back to the wall, lowers his gaze to the woman below him off frame left and, speaking softly in an ancient language, asks two words, his serene face briefly empty and lost. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "Did I?" | lower third (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** Eyeline down-left to Nour (matches 11.07.006).

### 11.07.008 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "From the beginning, please."   (5 s)
- **Shot:** Medium low-angle shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1 (upslope)
- **Action:** A shabti standing further up the slope turns its head toward Nour and asks, politely.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Dr. Kamel. From the beginning, please."
- **Sound:** SESHAT's voice warm in the stone
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: further up the steep floor stands {UNIT_SHABTI.SHORT}, perfectly still, its slit the only light on it; it turns its head slowly down toward the camera, its body following a beat later. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot gesturing
- **Refs:** UNIT_SHABTI, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** SESHAT is rehearsing the Hall: the lector must be word-perfect.

### 11.07.009 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The Negative Confession   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C)
- **Action:** Nour, glasses on, reads the opening of Chapter 125 off the tablet, exact and unhurried.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "Homage to thee, O Great God, Lord of Maati... I know thee, and I know thy name..."
- **Sound:** her voice climbing the corbels
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, narrow reading glasses now on her nose, holds a glowing tablet low and reads from it, reciting aloud in a measured, ritual cadence in an ancient language, the screen's soft light on her chin and the amber of a robot's slit on her cheek. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, soft screen light from below. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, eyes closed in prayer, hands clasped, readable screen
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_TABLET_LAYLA, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "Homage to thee, O Great God, Lord of Maati... / I know thee, and I know thy name..." | lower third (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** Glasses ON from here to read (file 01: they go on to read the tablet). The screen shows text (never in frame).

### 11.07.010 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Pray it with me." "I'm reading, not praying."   (7 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN (frame right, higher); NOUR (frame left, lower)
- **Action:** He asks her to pray it with him; she answers without lifting her eyes from the tablet.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "Pray it with me." NOUR: "I'm reading, not praying."
- **Sound:** the echo; the Father's ragged breath
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, against the wall at frame right, reaches a trembling hand toward {CHAR_NOUR.SHORT}, below him at frame left, speaking softly in an ancient language, one short plea; she answers with one short dry sentence, her eyes staying on the glowing tablet. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, soft screen light on her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, {CHAR_NOUR.NEG}, touching faces, embrace
- **Refs:** CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full, CHAR_NOUR_A_34, CHAR_NOUR_C_full, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "Pray it with me." | lower third (§13.7) | his line only | seq 11 subtitle file
- **Continuity:** Nour's line is English (bible §13 locks it). Tomas out of frame, holding the Father's other hand.

### 11.07.011 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — She keeps reading; he stops shaking   (7 s)
- **Shot:** Medium wide shot, anamorphic 40mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR, AKHENATEN, TOMAS (locked master, three faces soft); UNIT_SHABTI (upslope)
- **Action:** Nour keeps reading; as she reads, the Father stops shaking. The shabti thanks her.
- **Dialogue:** NOUR (continuing, under; not subtitled). SHABTI (SESHAT'S VOICE): "Thank you. The inch-worm will reach the door before five."
- **Sound:** Nour's recitation low under SESHAT's line
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, slow push-in: {CHAR_NOUR.SHORT}, keeps reading softly from the glowing tablet while {CHAR_AKHENATEN.SHORT}, slowly loosens his fist on the disk and lets his head rest back against the stone, still, and {CHAR_TOMAS.SHORT}, holds his hand; above them a robot's amber slit waits. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the dead of night. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_AKHENATEN.NEG}, {CHAR_NOUR.NEG}, {CHAR_TOMAS.NEG}, sleeping, collapse
- **Refs:** CHAR_NOUR_C_full, CHAR_AKHENATEN_A_full, CHAR_TOMAS_C_full, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** Three faces allowed in a slow-push master (bible §14.2); no sync (Nour's recitation is under, unsubtitled). "Before five": SESHAT's clock; the door is bridged in 11.11.

## SCENE 11.08 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT

### 11.08.001 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — The relay at the robbers' tunnel   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the north face; UNIT_RELAY on its mast at the lower hole; UNIT_THREAD (glint); embers far off
- **Action:** Embers on the plateau. At the ragged hole low in the north face, SESHAT's relay stands on a tripod mast; beside its cable, glinting at one angle only, the thread.
- **Dialogue:** —
- **Sound:** wind on the face; the relay's faint electric tick; distant fires crackling
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: the vast stepped face rises out of frame above a ragged hole low in the courses, where a slim black box on a folding three-legged mast winks one slow cool-white light, its dark cable snaking into the hole, and a single glint flickers along the stone beside it. Setting: {LOC_GP_NORTH_FACE.LONG}, {LOC_GP_NORTH_FACE.STATE_RELAY}, {LOC_GP_NORTH_FACE.STATE_EMBERS}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, {NEG_UNITS}, readable inscription panel, modern signage, sunrise
- **Refs:** LOC_GP_NORTH_FACE_NIGHT, UNIT_RELAY, UNIT_THREAD
- **Flags:** VFX-ASSIST
- **Continuity:** Geography (file 03 entry 53): facing the north face, east is frame LEFT. Relay at the Al-Ma'mun hole (the 6th–7th course); the original entrance and chevrons high above. Any carved panel reads as illegible texture. Thread glints are a VFX line.

### 11.08.002 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — He lifts the thread aside   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI (fingers); UNIT_THREAD; UNIT_RELAY cable
- **Action:** Fathi lifts the thread off the stone with two fingers, the way you lift a hair from a sleeper's face, and lays it a metre aside.
- **Dialogue:** —
- **Sound:** nothing at all; his held breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: beside a thick dark cable on weathered limestone lies {UNIT_THREAD.SHORT}; two deep-brown fingers lift it from the stone with infinite care, as gently as lifting a hair from a sleeping face, carry it slowly across frame and lay it down again, where it glints once. Setting: {LOC_GP_NORTH_FACE.SHORT}, the stone platform at the lower hole, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, rope, string, visible thick line, glowing wire, cutting
- **Refs:** UNIT_THREAD, UNIT_RELAY, CHAR_FATHI_B_full, LOC_GP_NORTH_FACE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The thread is never cut (bible §4; "Keep the thread whole"). It lies a metre from the relay from here (STATE_BLOWN wording).

### 11.08.003 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — The charge on the relay   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3); UNIT_RELAY; PROP_DEMO_CHARGES
- **Action:** Fathi presses a flat charge to the relay box and seats the wire.
- **Dialogue:** —
- **Sound:** the adhesive backing tearing; a soft press
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, crouched on the stone platform at the foot of the stepped face, presses {PROP_DEMO_CHARGES.SHORT} flat against the side of {UNIT_RELAY.SHORT} and seats a thin wire, his face calm and intent. Setting: {LOC_GP_NORTH_FACE.SHORT}, {LOC_GP_NORTH_FACE.STATE_RELAY}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, markings on the charge, readable labels, timer display
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, UNIT_RELAY, PROP_DEMO_CHARGES, LOC_GP_NORTH_FACE_NIGHT
- **Continuity:** Rifle slung on his back. Satchel nearly empty (DMG_L3: pouches empty). He faces the face (south), his back to the plateau.

### 11.08.004 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — 03:59   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_WINDUP_WATCH on Fathi's wrist
- **Action:** His wind-up watch: 03:59, the second hand sweeping.
- **Dialogue:** —
- **Sound:** the watch's tiny tick, loud in the silence
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_WINDUP_WATCH.LONG}, its thin second hand sweeping steadily around the dark dial, a thumb resting on a small firing device with a turn key just beside it. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, digital watch, numerals, brand name on the dial, readable text
- **Refs:** PROP_WINDUP_WATCH, PROP_DEMO_CHARGES, LOC_GP_NORTH_FACE_NIGHT
- **Flags:** COMP
- **Comp:** watch dial | hands at 03:59 with the second hand sweeping from 40 s to 44 s; plain baton indices, no numerals | locked to the dial | full clip | watch dial element
- **Continuity:** The watch is on his LEFT wrist. The exact time is set in comp (hands drawn over a clean dial).

### 11.08.005 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — The Reis, not hurrying   (5 s)
- **Shot:** Wide shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R4 + dust); FATHI (soft foreground, crouched, his back to the Reis)
- **Action:** Behind him, out of the dark along the foot of the face: the Reis, cracked shell, one hand gone at the wrist, walking, not hurrying.
- **Dialogue:** —
- **Sound:** a faint ceramic tick, heavier than a shabti's; a low servo hum
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off: along the foot of the stepped face, out of the dark at frame right, walks {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_DUST}, advancing with slow, heavy, measured strides, its thin red mast line steady, while in the soft foreground a crouched soldier keeps his back to it. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running robot, two hands, right hand present, robot face
- **Refs:** UNIT_REIS, CHAR_FATHI_B_full, LOC_GP_NORTH_FACE_NIGHT
- **Continuity:** Reis R4 (right hand gone at the wrist since 7.4; left shoulder chipped since 9.8) + dust. It walks right to left along the base toward the hole.

### 11.08.006 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — He watches the second hand   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI
- **Action:** Fathi does not turn. He watches the second hand. The tick comes closer.
- **Dialogue:** —
- **Sound:** the watch; the ceramic tick nearer, nearer
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.SHORT}, crouched, keeps his calm dark eyes down on his wrist and his body perfectly still as a faint pale shape grows soft and huge over his shoulder in the background, his jaw working once. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}, a cold floodlight wash across his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, looking back, sweating heavily
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_GP_NORTH_FACE_NIGHT
- **Continuity:** Suspense by framing: the Reis soft behind his right shoulder, closing.

### 11.08.007 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — Twelve   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_WINDUP_WATCH; PROP_DEMO_CHARGES (firing device)
- **Action:** The second hand reaches twelve; his thumb turns the key.
- **Dialogue:** —
- **Sound:** tick; tick; the key's click
- **PROMPT:** Insert, 100mm macro lens, locked-off: beside the sweeping second hand of a plain field watch on a thick dark-brown wrist, a thumb flips open a hinged safety cover and turns the key of a compact olive-drab firing device, {PROP_DEMO_CHARGES.STATE_FIRING}. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, digital display, numerals, readable text, flash in this frame
- **Refs:** PROP_WINDUP_WATCH, PROP_DEMO_CHARGES, LOC_GP_NORTH_FACE_NIGHT
- **Flags:** COMP
- **Comp:** watch dial | second hand reaching 12 at 04:00:00 on the key-turn frame | locked to the dial | full clip | watch dial element
- **Continuity:** 04:00 exactly: "Not a minute before." The dull THUD is heard below in 11.09.002.

### 11.08.008 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — The relay vanishes in white   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_RELAY (blown); UNIT_THREAD (untouched); FATHI (diving into the hole)
- **Action:** The relay vanishes in white; the thread lies untouched; Fathi dives into the tunnel.
- **Dialogue:** —
- **Sound:** a flat hard bang; stone chips pattering; his boots scraping into the hole
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: at the ragged hole, {UNIT_RELAY.SHORT}, {UNIT_RELAY.STATE_BLOWN}, a burst of pale dust rolling off the courses, and through the dust {CHAR_FATHI.SHORT}, dives headfirst into the black hole and is gone. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}, one white flash. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, fireball, mushroom cloud, debris at the camera, slow motion
- **Refs:** UNIT_RELAY, UNIT_THREAD, CHAR_FATHI_B_full, LOC_GP_NORTH_FACE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Relay BLOWN; "everything inside runs on its last orders" from here. Deliver before/after plates (mast standing / mast gone, thread glint a metre aside) if the flash fails. The flash is a 2-frame white element if needed.

### 11.08.009 — EXT. GREAT PYRAMID, NORTH FACE - NIGHT — The Reis folds itself down and follows   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off (same frame as 11.08.008)
- **In frame:** UNIT_REIS
- **Action:** The Reis reaches the hole, folds its height down and follows Fathi in. The hour card.
- **Dialogue:** —
- **Sound:** ceramic scraping stone; the servo hum swallowed by the tunnel
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: through settling dust at the ragged hole, {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, reaches the opening, folds its great height down onto its one hand and knees and crawls in after the soldier, its red mast line vanishing into the black. Setting: {LOC_GP_NORTH_FACE.SHORT}, in the dead of night. Lighting: {LOC_GP_NORTH_FACE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, two hands, running, sparks
- **Refs:** UNIT_REIS, LOC_GP_NORTH_FACE_NIGHT
- **Flags:** COMP, EXTEND:11.08.008
- **Comp:** hour card | "THE SEVENTH HOUR — THE SERPENT IS BOUND" beside the hieroglyph for "hour" | centred (§13.7) | in at 2.5 s, out at 5 s (carries over the cut) | seq 11 cards file
- **Continuity:** Generated from the last clean frame of 11.08.008 (dust as the hidden join). The Reis hunts on stale orders from here (file 02: head tilting and sweeping, pausing at each opening).

## SCENE 11.09 — INT. GREAT PYRAMID, SUBTERRANEAN CHAMBER - NIGHT

### 11.09.001 — INT. GREAT PYRAMID, SUBTERRANEAN CHAMBER - NIGHT — They drop into the unfinished chamber   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3, drying); TUT (CHAR_TUT_B3, drying)
- **Action:** The crawlway ends in a squared hole; they drop into a rough-cut chamber, never finished, its floor a landscape of ridges and trenches.
- **Dialogue:** —
- **Sound:** two drops onto rock; grit skittering into a trench; a dead, low-ceilinged silence
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: from a squared hole high in a raw rock wall {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_DRYING}, lowers herself and drops onto a jagged floor, and {CHAR_TUT.SHORT}, {CHAR_TUT.DMG_L3_DRYING}, {CHAR_TUT.STATE_G1}, drops after her, his glow sliding across the ridges and trenches. Setting: {LOC_GP_SUBTERRANEAN.LONG}, in the dead of night. Lighting: lit only by the warm glow at his chest, raw rock catching it, hard black beyond. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, torches, electric lights, smooth floor, finished walls
- **Refs:** LOC_GP_SUBTERRANEAN_TORCH, CHAR_ADAEZE_C_full, CHAR_TUT_B1_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Drying from here (Tut DMG_L3_DRYING; Adaeze DMG_DRYING). LIGHT_TORCH not pasted (no torch survives the shaft); GRADE_UNDERGROUND's beam wording stays as the grade reference only. Railed pit in the eastern half, frame right. Hours have passed since the flood: it is 04:00.

### 11.09.002 — INT. GREAT PYRAMID, SUBTERRANEAN CHAMBER - NIGHT — "The relay."   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE; TUT (soft)
- **Action:** A dull THUD far above; dust sifts down through the glow; Adaeze looks up.
- **Dialogue:** ADAEZE: "The relay."
- **Sound:** a dull THUD through a hundred metres of stone; dust hissing down
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: in a rough bedrock chamber, fine dust sifts down from the flat ceiling through a warm glow as {CHAR_ADAEZE.SHORT}, looks up sharply and speaks two quiet words, a slight young man soft beside her also looking up. Setting: {LOC_GP_SUBTERRANEAN.SHORT}, in the dead of night. Lighting: lit only by a warm glow at chest height, dust glittering in it, hard black beyond. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, collapse, falling rocks, torches
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GP_SUBTERRANEAN_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow at chest height and the dust in it | full clip | glow element
- **Continuity:** 04:00: SESHAT's live voice is gone inside; every unit now runs its last orders.
## SCENE 11.10 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS

### 11.10.001 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Bent double, up the stone tube   (6 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, the camera follows behind · **Move:** the camera follows behind them at a crouch, slowly
- **In frame:** TUT (CHAR_TUT_B3, drying), ADAEZE (CHAR_ADAEZE_C3, drying); an amber slit far ahead
- **Action:** A stone tube barely a metre high climbs north. Bent double, Tut and Adaeze go up it; far ahead an amber slit waits.
- **Dialogue:** —
- **Sound:** scuffing on gritty stone; laboured breath; the stick's tap
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, the camera follows behind: bent double, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_STICK}, and {CHAR_ADAEZE.SHORT}, limping, climb away up a steep stone passage barely chest high, his glow throwing their shadows ahead, while far up the slope a single small vertical amber slit waits in the black. Setting: {LOC_GP_DESCENDING.LONG}, in the dead of night. Lighting: only a warm glow at chest height and one amber slit, the passage receding into black. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, standing upright, tall corridor, electric lights, torches
- **Refs:** LOC_GP_DESCENDING_TORCH, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, UNIT_SHABTI
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow among the climbers throwing their shadows ahead | full clip | glow element
- **Continuity:** Geography lock (file 03 entry 47): "down" is toward camera; they climb away from it. Tut leads, Adaeze behind. Key light: Tut's glow + unit slits until Fathi's rifle torch arrives (11.10.020); LIGHT_TORCH is not pasted before then.

### 11.10.002 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — A shabti fills the passage   (5 s)
- **Shot:** Medium shot, anamorphic 24mm, slow push-in · **Move:** slow push-in (Tut's approach)
- **In frame:** UNIT_SHABTI ×1 ("Rami", folded into the passage)
- **Action:** A shabti, folded down into the low passage, fills it wall to wall, head bowed under the ceiling, slit steady.
- **Dialogue:** —
- **Sound:** a single ceramic tick as it shifts its weight
- **PROMPT:** Medium shot, anamorphic 24mm lens, slow push-in: up the steep chest-high passage, {UNIT_SHABTI.LONG}, folded down onto bent knees with its smooth head bowed beneath the low ceiling, fills the passage from wall to wall, perfectly still, its single amber slit the only light on it. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: its own amber slit and a warm glow approaching from below. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot crawling toward the camera, face, eyes
- **Refs:** UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the approaching glow from below | full clip | glow element
- **Continuity:** This unit becomes "Rami". D0 now; STATE_RAMI (chips and dust) from 11.10.016.

### 11.10.003 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "This area is closed."   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI; TUT; ADAEZE
- **Action:** The shabti asks them to return to the surface; it takes Tut's elbow gently; its other hand opens toward Adaeze: stop.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Please return to the surface. This area is closed."
- **Sound:** the recorded voice, slightly flatter than before (no live SESHAT now)
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: in the chest-high passage {UNIT_SHABTI.SHORT}, takes the elbow of {CHAR_TUT.SHORT} gently between its thumb and two fingers, and raises its other long hand flat, palm open, toward {CHAR_ADAEZE.SHORT} behind him: stop. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: an amber slit and the warm glow at his chest, black beyond. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, grabbing, shoving, fist, robot touching a face
- **Refs:** UNIT_SHABTI, CHAR_TUT_B1_full, CHAR_TUT_A0_34, CHAR_ADAEZE_C_full, LOC_GP_DESCENDING_TORCH
- **Continuity:** Minimum force (file 02): thumb and two fingers on Tut's LEFT elbow. The voice is SESHAT's recorded servitor script: "stale orders".

### 11.10.004 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Stale orders."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3)
- **Action:** Adaeze, bent under the ceiling, reads the machine exactly.
- **Dialogue:** ADAEZE: "Stale orders. Recover the witness. Keep the humans out."
- **Sound:** her whisper-hard voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_DRYING}, bent under the low ceiling, the robot's flat palm soft in the foreground, studies it and speaks three clipped phrases, low and exact, amber light on her glasses. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: an amber slit and a warm glow from off frame, black beyond. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_ADAEZE.NEG}, glare hiding the eyes
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from off frame on her face | full clip | glow element
- **Continuity:** Glasses straightened since the tunnel. Drying clothes, tide-lines.

### 11.10.005 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "O shabti, allotted to me"   (8 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut, his elbow still in the machine's fingers, speaks the shabti spell to it in the old words.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "O shabti, allotted to me, if I be summoned or if I be detailed to do any work which has to be done in the realm of the dead..."
- **Sound:** his voice low and ritual in the stone; the double heartbeat under it
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.DMG_L3_DRYING}, {CHAR_TUT.STATE_G1}, bent under the low stone ceiling, looks steadily into the robot's amber slit just off frame left and begins reciting aloud in a measured, ritual cadence in an ancient language, calm and absolutely certain. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit light on his face and the warm glow from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, raised arms, magic gestures, glowing hands
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "O shabti, allotted to me, if I be summoned / or if I be detailed to do any work / which has to be done in the realm of the dead..." | lower third, two cards (§13.7) | line in to out | seq 11 subtitle file · chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Book of the Dead ch. 6 (recorded with the consultant first). Eyeline frame left to the unit.

### 11.10.006 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "'Here am I' you shall say."   (7 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in continuing · **Move:** slow push-in, continuing the same move at the same speed
- **In frame:** TUT
- **Action:** Tut finishes the spell.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "...of conveying sand from east to west; 'Here am I' you shall say."
- **Sound:** his last word; then no live voice anywhere
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in, continuing the same camera move at the same speed: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, finishes reciting aloud in a measured, ritual cadence in an ancient language, then falls silent and waits, his eyes fixed on the amber slit off frame left. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit light on his face and the warm glow from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, raised arms, glowing hands
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34
- **Flags:** COMP, EXTEND:11.10.005
- **Comp:** subtitle | "...of conveying sand from east to west; / 'Here am I' you shall say." | lower third (§13.7) | line in to out | seq 11 subtitle file · chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Generated from the last clean frame of 11.10.005. "No live voice countermands him": a beat of held silence at the end.

### 11.10.007 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Here am I."   (6 s)
- **Shot:** Close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (head and hand); TUT's elbow
- **Action:** The slit brightens once: "Here am I." It lets go of his elbow and waits.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Here am I."
- **Sound:** the voice, recorded and small; a ceramic tick as the fingers open
- **PROMPT:** Close-up, anamorphic 50mm lens, locked-off: the smooth featureless head of {UNIT_SHABTI.SHORT}, lifts slightly and its amber light-slit brightens once; then its long fingers open and release the charcoal sleeve of a young man's elbow, and it stays perfectly still, waiting. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: its own amber slit and a warm glow from below. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, bowing, kneeling, head nodding repeatedly
- **Refs:** UNIT_SHABTI, CHAR_TUT_B1_full, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** slit timing | single brightening on "Here am I" (§9.8) | on the slit | first 1.5 s | SESHAT recording · chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from below | full clip | glow element
- **Continuity:** The servitor protocol answers a proper summons once the live override is gone (relay blown at 04:00).

### 11.10.008 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Your name is Rami."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** Tut names the machine; then turns his head to Adaeze and explains.
- **Dialogue:** TUT: "Your name is Rami." (to Adaeze) "A servant with a name can be called."
- **Sound:** a small catch in his voice on the name
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, speaks one short sentence to the robot off frame left, gently, then turns his head over his shoulder to the woman behind him off frame right and speaks one more, quiet and sure. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit light and the warm glow from below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, fast head turn, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** From here the lead unit is "Rami" (In frame tags: UNIT_SHABTI "RAMI"). Adaeze is behind (below) him, frame right in his singles.

### 11.10.009 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Below them, another slit   (5 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (below, near camera, in darkness); TUT and ADAEZE (up the passage, turning)
- **Action:** Below them in the dark, an amber slit brightens: "Here am I." They turn to look down.
- **Dialogue:** SHABTI (SESHAT'S VOICE, below): "Here am I."
- **Sound:** the same small voice, from lower in the stone
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, looking up the steep passage: close to the camera in the black, a pale shape folded into the tunnel lifts its head and its amber light-slit brightens once, while further up two small figures in a warm glow turn to look down. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slits and a warm glow at chest height. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot face, bright light
- **Refs:** UNIT_SHABTI, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** slit timing | single brightening (§9.8) | foreground unit's slit | 0.5–2 s | SESHAT recording · chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow around the two small figures | full clip | glow element
- **Continuity:** Down is toward camera: this unit is below them (between them and the Subterranean Chamber).

### 11.10.010 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Above, another; a work gang   (7 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×3 (Rami + one above + one from below folding in); TUT and ADAEZE (bg)
- **Action:** Another slit brightens above. Two more bone-white shapes fold into the passage beside Rami: a work gang.
- **Dialogue:** SHABTI (SESHAT'S VOICE, above): "Here am I."
- **Sound:** ceramic ticks in unison, three units now
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: up the passage an amber slit brightens once, and then two more bone-white figures, each {UNIT_SHABTI.SHORT}, fold themselves down into the low tunnel beside the first, three smooth heads bowed under the ceiling in a row, identical and still. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: three amber slits and a warm glow at chest height. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robots standing upright, running, faces
- **Refs:** UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** slit timing | single brightening on the upper unit (§9.8) | 0.5–2 s | SESHAT recording · hour card | "THE EIGHTH HOUR — THE DEAD ANSWER FROM THEIR CAVES" beside the hieroglyph for "hour" | centred (§13.7) | in at 3 s, out at 6.5 s | seq 11 cards file · chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow at chest height | full clip | glow element
- **Continuity:** The work gang = three shabti (Rami + two); later "three pairs of long hands". Stacked in a 1 m passage (scale: 1.78 m units folded; file 05 §10 #27).

### 11.10.011 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Four hundred and thirteen."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** Tut, watching them gather, says it, almost amused.
- **Dialogue:** TUT: "I owned four hundred and thirteen."
- **Sound:** a dry breath of a laugh
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, watching the robots gather off frame left, speaks one short sentence with the driest flicker of amusement, amber light from three slits on his cheek. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit light and the warm glow from below. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, broad grin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** 413 shabti in KV62 (the king's own servants); the line is fact, not boast.

### 11.10.012 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — A jackal drops out of the robbers' tunnel   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (hero); the ragged side tunnel mouth
- **Action:** A red line flickers where a ragged side tunnel breaks into the passage; a jackal drops out of it, fast and silent; its head snaps to Adaeze and the red line settles.
- **Dialogue:** —
- **Sound:** a soft pad-tap on stone; the faint servo whisper; nothing else
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: where a ragged hand-hacked side tunnel breaks into the passage wall a thin red line flickers, and {UNIT_JACKAL.LONG}, drops out of it silently, freezes with one forefoot raised, and its head snaps toward frame right, its red line narrowing and brightening. Setting: {LOC_GP_DESCENDING.SHORT}, at the mouth of {LOC_GP_MAMUN_TUNNEL.SHORT}, in the dead of night. Lighting: its own red line and a warm glow from below. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, laser beam, laser dot, barking, snarling
- **Refs:** UNIT_JACKAL, LOC_GP_DESCENDING_TORCH, LOC_GP_MAMUN_TUNNEL_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from below | full clip | glow element
- **Continuity:** Jackal D1 (dust). The side tunnel is Al-Ma'mun's (the robbers' tunnel) joining above the gang. The red line is on its head: the "line settles on Adaeze" is its head snapping to her (never a laser).

### 11.10.013 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "That is sand."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** Tut points at the jackal and gives the gang its work.
- **Dialogue:** TUT (in Middle Egyptian; subtitled; pointing at the jackal): "That is sand. Convey it from the east to the west."
- **Sound:** his voice hard and clear for the first time
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, lifts his left arm and points up the passage past the robots, speaking softly in an ancient language, two short commands, his face royal and utterly cold. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit light and a thin red glint from above, the warm glow from below. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, shouting, magic gesture, glowing hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_HANDS, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "That is sand. / Convey it from the east to the west." | lower third (§13.7) | line in to out | seq 11 subtitle file · chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Points with the LEFT hand (the stick is in his right). Arm clear of his mouth.

### 11.10.014 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — The work gang walks up   (5 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×3 (work gang, backs to camera); UNIT_JACKAL (above, small)
- **Action:** The work gang walks up the passage toward the jackal. They never run.
- **Dialogue:** —
- **Sound:** three ceramic ticks per step, perfectly in time
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, looking up the steep passage: three bone-white figures, each {UNIT_SHABTI.SHORT}, stooped under the low ceiling, walk away up the slope in single file with smooth, unhurried, even steps toward a thin red line waiting in the black above. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slits, a red line above and a warm glow from the bottom of frame. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, marching in step like soldiers, weapons
- **Refs:** UNIT_SHABTI, UNIT_JACKAL, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from the bottom of frame | full clip | glow element
- **Continuity:** Down toward camera; the gang holds the passage between camera (Tut, Adaeze) and the jackal (file 03 lock).

### 11.10.015 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — The jackal fires   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (from behind and above)
- **Action:** From behind the jackal, looking down the slope: it goes rigid and fires down the passage, away from the camera, at the approaching white figures.
- **Dialogue:** —
- **Sound:** one sharp suppressed crack, hammering down the stone tube
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off, from behind and above {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_D1}, looking past it down the steep passage: it goes rigid, a small muzzle flash shows at its spine, and it fires down the slope away from the camera toward three pale stooped figures climbing steadily toward it. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: its red line, amber slits below, one hard flash. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, tracer fire, visible projectile, laser beam, humans in the line of fire
- **Refs:** UNIT_JACKAL, UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Kill-grammar framing with no human target: the rounds hit ceramic. The muzzle points away from camera. Add a 2-frame flash in comp if needed.

### 11.10.016 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Chips spark off Rami's chest   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI "RAMI" (chest)
- **Action:** Chips spark off Rami's chest; it keeps walking.
- **Dialogue:** —
- **Sound:** dry ceramic cracks; the tick of its step, unbroken
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: the linen-textured chest of {UNIT_SHABTI.SHORT}, fills the frame as small bright sparks and white ceramic chips burst from its shell, {UNIT_SHABTI.STATE_RAMI}, and it keeps walking forward through them at the same unhurried pace. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slit glow and hard sparks. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fluid, wires spilling, robot staggering, falling
- **Refs:** UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Rami from here: STATE_RAMI (chips out of the chest shell, dust in the seams) through 12.7. It does not stagger (file 02).

### 11.10.017 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Three pairs of hands bear it down   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_SHABTI ×3; UNIT_JACKAL
- **Action:** Three pairs of long hands close on the jackal's legs and bear it down under their weight. It thrashes. They hold.
- **Dialogue:** —
- **Sound:** carbon legs scraping stone; ceramic grinding; the jackal's servo whine rising, then straining
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: three bone-white figures, each {UNIT_SHABTI.SHORT}, reach the black quadruped, {UNIT_JACKAL.SHORT}, and their long slim hands close calmly on its thin legs and press it down flat onto the sloping stone under their weight; it thrashes and twists, and they hold it, perfectly still. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slits, its jerking red line. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, punching, kicking, robots fighting like people, fluid, broken pieces flying at the camera
- **Refs:** UNIT_SHABTI, UNIT_JACKAL, LOC_GP_DESCENDING_TORCH
- **Continuity:** The gang holds rather than fights (file 05 §10 #27). The jackal pinned on its belly, head uphill, red line a hand's width off the floor on the passage's centre line.

### 11.10.018 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Did you just..."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (frame left); TUT (frame right)
- **Action:** Adaeze turns to Tut, half-appalled; he answers simply; she keeps looking at him a moment too long.
- **Dialogue:** ADAEZE: "Did you just..." TUT: "They know what they are for."
- **Sound:** the jackal's straining whine above
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: bent under the low ceiling, {CHAR_ADAEZE.SHORT}, turns to {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and begins a question she leaves unfinished; he answers with one quiet sentence, his eyes on the robots above, and she keeps looking at him a moment too long. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: amber slits above and the warm glow at his chest. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** She is beginning to fear what he is, and to trust it.

### 11.10.019 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — They squeeze past the heap   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE; TUT; UNIT_JACKAL (pinned); UNIT_SHABTI ×3
- **Action:** They squeeze past the heap of machines, the jackal's red line a hand's width from Adaeze's face.
- **Dialogue:** —
- **Sound:** her held breath; the jackal's servo straining; ceramic creak
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {CHAR_ADAEZE.SHORT}, presses her back to the stone wall and edges up past a pinned black quadruped, its thin red line a hand's width from her cheek, her eyes locked on it, while {CHAR_TUT.SHORT}, guides her by the sleeve and three pale robots hold the machine down. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: the red line lighting her cheek, amber slits, the warm glow. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_ADAEZE.NEG}, {CHAR_TUT.NEG}, weapon facing her face, muzzle toward the lens, robot touching her
- **Refs:** CHAR_ADAEZE_C_full, CHAR_TUT_B1_full, UNIT_JACKAL, UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow on both of them | full clip | glow element
- **Continuity:** They pass above the heap: the gang and jackal are now between them and the Subterranean Chamber. The jackal's head faces uphill; its weapon module lies along its spine, pinned flat.

### 11.10.020 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Fathi slides out: "Move!"   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B3); the robbers' tunnel mouth
- **Action:** Rubble clatters down the robbers' tunnel; Fathi slides out feet first, rifle up, and shouts.
- **Dialogue:** FATHI: "Move!"
- **Sound:** rubble clattering; boots hitting stone; his shout slamming off the walls
- **PROMPT:** Wide shot, anamorphic 24mm lens, subtle handheld: a spill of rubble clatters out of the ragged side tunnel, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, slides out feet first onto the sloping floor, rifle held up across his chest with its torch beam slashing the dust, and shouts one word up the passage. Setting: {LOC_GP_DESCENDING.SHORT}, at the mouth of {LOC_GP_MAMUN_TUNNEL.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifle pointed at the camera, torch into the lens, muzzle facing the lens
- **Refs:** CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_DESCENDING_TORCH, LOC_GP_MAMUN_TUNNEL_TORCH
- **Continuity:** Fathi's rifle torch is the new key light: LIGHT_TORCH pasted from here. He is dry (never in the shaft). The line is shouted in a wide: sync only if the face reads; otherwise it plays on the cut.

### 11.10.021 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — The Reis folds into the gap   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R4 + dust)
- **Action:** Behind Fathi, folding its height into the gap: the Reis, on its last orders. Its mast swings to Tut, then to Adaeze.
- **Dialogue:** —
- **Sound:** heavy ceramic scraping; the low servo hum filling the tube
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: out of the ragged side tunnel {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_DUST}, folds its great height down into the chest-high passage, and the slim black mast on its head swivels to frame right, pauses, then swivels a little further, its thin red line settling. Setting: {LOC_GP_DESCENDING.SHORT}, at the mouth of {LOC_GP_MAMUN_TUNNEL.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, two hands, right hand present, robot face, standing upright in the passage
- **Refs:** UNIT_REIS, LOC_GP_DESCENDING_TORCH, LOC_GP_MAMUN_TUNNEL_TORCH
- **Continuity:** Stale-order hunting: its mast swings independently of the head (file 02). Target order: Tut, then Adaeze.

### 11.10.022 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "O shabti..." Nothing brightens.   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (foreground shoulder, charcoal hood); UNIT_REIS (facing camera)
- **Action:** Tut begins the summons; nothing brightens behind the Reis's black band.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "O shabti..."
- **Sound:** his voice; the Reis's hum, unchanged
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the soft charcoal-hooded shoulder of a slight young man, {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, crouched in the low passage, turns its head toward him; the amber above and below its black band stays exactly as it is, and its red mast line holds steady. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, slit brightening, two hands, robot face
- **Refs:** UNIT_REIS, CHAR_TUT_B_night_34, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "O shabti..." | lower third (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** Tut's line from the foreground shoulder: no sync needed (§9.2). The Reis does NOT answer (the jackal software).

### 11.10.023 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "It can't hear you."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (frame right); ADAEZE (frame left)
- **Action:** Tut names what he sees; Adaeze tells him what it means.
- **Dialogue:** TUT: "It has a jackal's head." ADAEZE: "And the jackal's software. It can't hear you."
- **Sound:** the Reis's hum closing in
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: bent under the low ceiling, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, speaks one quiet sentence, staring past the lens, and {CHAR_ADAEZE.SHORT}, beside him, answers fast with two short sentences, grabbing his sleeve, the white torch beam swinging across both faces. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, LOC_GP_DESCENDING_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Reverse of 11.10.022; the Reis is behind camera.

### 11.10.024 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Rami wraps itself round the Reis's legs   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_REIS; UNIT_SHABTI "RAMI"; ADAEZE (edge of frame, recoiling)
- **Action:** The Reis's one hand reaches for Adaeze. Rami lets go of the jackal and wraps itself around the Reis's legs.
- **Dialogue:** —
- **Sound:** ceramic slamming ceramic; the servo hum straining
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, reaches its one long left hand toward a woman recoiling at the edge of frame, and a smaller bone-white figure, {UNIT_SHABTI.STATE_RAMI}, lunges from below and wraps both arms tight around its legs, dragging the reach short. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot hand on a face, grabbing her throat, punching, right hand present
- **Refs:** UNIT_REIS, UNIT_SHABTI, CHAR_ADAEZE_C_full, LOC_GP_DESCENDING_TORCH
- **Continuity:** The Reis's hand never reaches her. "Rami" = the chipped unit. Rami's grip on the Reis continues into the Gallery (11.11.005).

### 11.10.025 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — The jackal tears loose   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_JACKAL; UNIT_SHABTI ×2 (one losing a forearm)
- **Action:** Freed of Rami's grip, the jackal tears loose; a shabti forearm skitters across the stone.
- **Dialogue:** —
- **Sound:** a hard ceramic crack; the forearm skittering down the slope
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: the black quadruped, {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_D1}, wrenches itself free from two pale robots holding it down, and a clean white ceramic forearm snaps away from one of them and skitters away down the sloping stone floor toward the camera. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fluid, wires spilling, sparks and cables spilling like blood, weapon facing camera
- **Refs:** UNIT_JACKAL, UNIT_SHABTI, LOC_GP_DESCENDING_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** One gang unit from here: STATE_GANG_ARM (a clean white ceramic break at the elbow). The jackal loose (D1) and chasing from here.

### 11.10.026 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — "Up!"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B3); ADAEZE (arm, being hauled)
- **Action:** Fathi grabs Adaeze's arm and hauls her toward the robbers' tunnel.
- **Dialogue:** FATHI: "Up!"
- **Sound:** his shout; the fight behind them
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, grabs a navy sleeve and hauls hard toward the ragged side tunnel, shouting one word, his rifle torch throwing a white glare off the stone across his face. Setting: {LOC_GP_DESCENDING.SHORT}, in the dead of night. Lighting: {LOC_GP_DESCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifle pointed at the camera, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_DESCENDING_TORCH
- **Continuity:** Direction: into the robbers' tunnel bypass, then up the Ascending Passage.

### 11.10.027 — INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS — Up the Ascending Passage   (5 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** FATHI, ADAEZE, TUT (climbing away); UNIT_REIS and UNIT_JACKAL (lights below, following)
- **Action:** They scramble up the Ascending Passage, away from camera; below, the machines follow.
- **Dialogue:** —
- **Sound:** scrambling boots and the stick on footholds; ceramic and carbon scraping below
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: three figures scramble away up a steep chest-high passage on hands and feet, a torch beam bouncing ahead of them and a warm glow among them, while at the bottom edge of frame a thin red line and a crossed amber slit rise into view, following. Setting: {LOC_GP_ASCENDING.LONG}, in the dead of night. Lighting: {LOC_GP_ASCENDING.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, standing upright, electric lights, tourists
- **Refs:** LOC_GP_ASCENDING_TORCH, CHAR_FATHI_B_full, CHAR_ADAEZE_C_full, CHAR_TUT_B1_full, UNIT_REIS, UNIT_JACKAL
- **Continuity:** Geography (file 03 entry 65): up is away from camera; pursuers come from below. Order: Fathi, Adaeze, Tut last (his stick). The work gang (Rami + the one-armed unit + one) grapples the Reis behind them.
## SCENE 11.11 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT

### 11.11.001 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The Ninth Hour: the vault and the thread   (6 s)
- **Shot:** Extreme wide establishing shot, low-angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the Grand Gallery; UNIT_THREAD up the centre of the floor; the procession at the top (UNIT_SHABTI slits, casket glow, NOUR, AKHENATEN, TOMAS: tiny)
- **Action:** A corbelled vault more than eight metres high climbs steeply for nearly fifty; the thread runs up the centre of the floor; at the top the procession waits, lit amber.
- **Dialogue:** —
- **Sound:** breath and stone; the far ceramic ticks at the top; the fight's muffled scrape from the passage below
- **PROMPT:** Extreme wide establishing low-angle shot, anamorphic 24mm lens, locked-off: from the foot of the slope the camera looks up the whole vault, {UNIT_THREAD.SHORT}, glinting in short stretches up the centre of the walkway, and at the very top, small amber slits and a faint green glow gather around a few pale figures. Setting: {LOC_GP_GRAND_GALLERY.LONG}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_BLACKOUT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, electric lights on, tourists, rope, glowing wire, bending walls
- **Refs:** LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH, LOC_GP_GRAND_GALLERY_SLITS, UNIT_THREAD, UNIT_SHABTI, PROP_CASKET_NEST
- **Flags:** COMP, VFX-ASSIST
- **Comp:** hour card | "THE NINTH HOUR — THE ROWERS TAKE UP THEIR OARS" beside the hieroglyph for "hour" | centred (§13.7) | in at 1 s, out at 5 s | seq 11 cards file
- **Continuity:** Geography lock (file 03 entry 49): up = away from camera; looking up the Gallery is looking south, so the WEST ramp is frame RIGHT and the EAST ramp frame LEFT. The Queen's Chamber passage mouth opens under the foot of the central ramp; the Ascending Passage enters at the bottom. Thread glints are a VFX line. The torch beam is Fathi's, from the bottom.

### 11.11.002 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The jackal takes the east ramp and fires   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (profile, east ramp)
- **Action:** The jackal's red line swings out of the passage behind them; it springs onto the east ramp, goes rigid and fires across the Gallery.
- **Dialogue:** —
- **Sound:** pad-taps; one sharp suppressed crack, booming up the vault
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_JACKAL.LONG}, {UNIT_JACKAL.STATE_D1}, springs out of a low square opening onto a narrow stone ramp along the wall, turns side-on to the camera, goes rigid, and a small muzzle flash shows at its spine as it fires across frame toward the right, away from the camera. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the foot of the east ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, tracer fire, visible projectile, laser beam, people in frame
- **Refs:** UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Jackal D1 on the EAST ramp (it keeps the east side for the scene). Fires west (frame right in this set-up).

### 11.11.003 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Stone dust; into the Queen's Chamber passage   (5 s)
- **Shot:** Medium wide shot, anamorphic 24mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI, TUT, ADAEZE
- **Action:** Stone dust bursts off the corbels above them; Fathi drags Tut and Adaeze into the low mouth of the Queen's Chamber passage.
- **Dialogue:** —
- **Sound:** stone chips cracking and pattering; boots skidding; breath
- **PROMPT:** Medium wide shot, anamorphic 24mm lens, urgent handheld: a burst of pale stone dust and chips blows off the stepped wall above three figures at the foot of the slope, and {CHAR_FATHI.SHORT}, hauls {CHAR_TUT.SHORT} and {CHAR_ADAEZE.SHORT} down and into a low square passage opening in the floor at the gallery's foot. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_FATHI.NEG}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, person hit, falling bodies, large explosion, debris at the camera
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Environmental impact only (§7.1 step 2). They shelter in the mouth of the horizontal passage to the Queen's Chamber (1.17 m high).

### 11.11.004 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — A kneeling shabti feeds the tether   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (kneeling); the inch-worm's tether
- **Action:** A kneeling shabti in the passage feeds a hair-thin tether into the dark, head bowed over its work.
- **Dialogue:** —
- **Sound:** a faint whisper of filament through ceramic fingers
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: in a low square stone passage, {UNIT_SHABTI.SHORT}, kneels on one knee with its smooth head bowed over its long hands, feeding a hair-thin glinting tether steadily forward into the black passage ahead, perfectly calm, while torch light flickers across its shell. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, glowing wire, robot turning its head
- **Refs:** UNIT_SHABTI, UNIT_INCHWORM, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The tether runs to the inch-worm in the Queen's Chamber south shaft (UNIT_INCHWORM STATE_TRAILING). The tether is a VFX line like the thread; it is NOT the thread.

### 11.11.005 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Pinned in the hole   (5 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS; UNIT_SHABTI ×3 (work gang, one with a missing forearm); UNIT_JACKAL (red line sweeping)
- **Action:** At the Ascending Passage mouth, the work gang wrestles the Reis. The jackal's red line sweeps the passage mouth and keeps the three of them in the hole.
- **Dialogue:** —
- **Sound:** ceramic grinding on ceramic; the Reis's servo hum; the jackal's whisper
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, from low inside a passage mouth: across the foot of the gallery, three pale robots cling to the legs and arms of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, at a square opening, dragging it back, while above them on the ramp a thin red line sweeps slowly back and forth toward the camera and away. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, laser beam, robots punching, fluid, right hand present on the tall robot
- **Refs:** UNIT_REIS, UNIT_SHABTI, UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** Work gang: Rami (STATE_RAMI), the one-armed unit (STATE_GANG_ARM), the third (D1). The red line is the jackal's head light sweeping, never a beam.

### 11.11.006 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The knife, the wrist   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI (hand, knife); ADAEZE (hand); the tether
- **Action:** Fathi's knife goes to the tether; Adaeze's hand catches his wrist.
- **Dialogue:** —
- **Sound:** a blade's small scrape; a grip
- **PROMPT:** Insert, 100mm macro lens, locked-off: a plain black utility knife in a deep-brown hand moves toward a hair-thin glinting tether running along the stone floor, and a second hand, deep brown with grey hoodie cuffs, clamps hard around the wrist and stops it an inch short. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, cutting, blood, knife pointed at the camera, ancient dagger, gold hilt
- **Refs:** CHAR_FATHI_B_full, CHAR_ADAEZE_C_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Fathi's own knife (from the chest rig), not the meteoritic dagger (that is still on Tut's belt). The tether is never cut.

### 11.11.007 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "It's opening the door for us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE
- **Action:** Adaeze, still holding Fathi's wrist, tells him why.
- **Dialogue:** ADAEZE: "Leave it. It's opening the door for us."
- **Sound:** the fight outside; her low voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.DMG_DRYING}, crouched in the low stone passage, her hand still gripping a soldier's wrist at frame edge, speaks two short sentences, low and certain, torch light flickering on her round glasses. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, glare hiding the eyes
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** She has worked out the inch-worm's task: SESHAT needs the door open too.

### 11.11.008 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — INSERT: the feed, the door with copper handles   (5 s)
- **Shot:** Insert, 100mm macro, slow push-in · **Move:** slow push-in (the inch-worm's own camera)
- **In frame:** LOC_GP_QC_SHAFT (the shaft and the slab); UNIT_INCHWORM (snake camera)
- **Action:** On Nour's tablet (COMP): a twenty-centimetre shaft climbing at forty degrees ends at a limestone slab with two small copper loops; a snake camera slides through a drilled hole.
- **Dialogue:** —
- **Sound:** the inch-worm's soft click-and-rasp; a faint feed hiss
- **PROMPT:** Insert, 100mm macro lens, slow push-in up {LOC_GP_QC_SHAFT.LONG}, until a tiny ring-lit snake camera on a thin segmented stalk, {UNIT_INCHWORM.SHORT}, slides forward into a small drilled hole low in the slab's face. Setting: the south shaft of a small chamber deep inside a pyramid, just before dawn. Lighting: {LOC_GP_QC_SHAFT.LIGHT_INCHWORM}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable signs, hieroglyphs, screen interface, overlays, numbers, people
- **Refs:** LOC_GP_QC_SHAFT_INCHWORM, UNIT_INCHWORM
- **Flags:** COMP
- **Comp:** feed | plate played as SESHAT's feed on Nour's tablet (full-frame insert with the glyph small in one corner, file 02 §8; no type) | full frame | full clip | UNIT_GLYPH_SESHAT asset
- **Continuity:** Real anchor: the 1993 door with two copper pins; the 2002 drilled hole (file 03 entry 50). The shaft climbs at about 40°.

### 11.11.009 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Red ochre."   (7 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI, TUT, ADAEZE (crouched in the passage mouth, locked master)
- **Action:** Crouched in the low mouth, the three listen as SESHAT's voice comes down the Gallery from the top.
- **Dialogue:** SHABTI (SESHAT'S VOICE, from the top; echoing): "Red ochre. Photographed by the Djedi team in 2011, and left unread. Richardson et al., 2013."
- **Sound:** the voice echoing down fifty metres of stone, a beat of delay
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and {CHAR_ADAEZE.SHORT}, crouch together in a low square stone opening, all three turning their faces up toward a voice from high above, listening, perfectly still, the warm glow at his chest lighting their faces from below. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_FATHI.NEG}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, speaking, faces touching
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_A0_front, CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Three faces allowed only because the master is locked-off (bible §14.2). The shabti at the top speaks with the recorded servitor voice (no live SESHAT after 04:00), but the knowledge is SESHAT's.

### 11.11.010 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — INSERT: the marks   (6 s)
- **Shot:** Insert, 100mm macro, slow push-in · **Move:** slow push-in (the snake camera)
- **In frame:** the cavity behind the door; the red ochre marks
- **Action:** On the feed (COMP): the tiny cavity beyond the slab; on its floor, marks in red ochre.
- **Dialogue:** SHABTI (SESHAT'S VOICE, continuing): "One reading: 'one hundred and twenty-one.' The shaft's length, in cubits."
- **Sound:** feed hiss; the voice
- **PROMPT:** Insert, 100mm macro lens, slow push-in: the tiny camera's cool ring of light spills into a cramped stone cavity and falls across its dusty floor, where a few faint red ochre strokes lie on the pale limestone in front of a second rough slab. Setting: {LOC_GP_QC_SHAFT.SHORT}, {LOC_GP_QC_SHAFT.AREA_BEHIND_DOOR}, just before dawn. Lighting: {LOC_GP_QC_SHAFT.LIGHT_INCHWORM}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable signs, clear hieroglyphs, numbers, painted figures, screen interface
- **Refs:** LOC_GP_QC_SHAFT_INCHWORM
- **Flags:** COMP
- **Comp:** red ochre marks | the marks as recorded by Djedi (2011), drawn by the Egyptologist (Miatello's "121" reading; sign codes from research 09) | on the cavity floor, tracked | full clip | marks element · feed | SESHAT's feed treatment as 11.11.008
- **Continuity:** Real: undeciphered marks; one reading "121" (file 03 entry 50; screenplay line keeps its citations).

### 11.11.011 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "A mason's tally."   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3, drying)
- **Action:** Tut, low, reads the marks as a man, not a mystery.
- **Dialogue:** TUT (low): "A mason's tally. He wrote down how far he had come."
- **Sound:** his quiet voice; the fight's scrape outside
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.DMG_L3_DRYING}, {CHAR_TUT.STATE_G1}, crouched in the low stone passage with his face tilted up toward the voice, speaks quietly, two short sentences, with a craftsman's fond respect. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}, the warm glow from below his chin. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing skin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Tut B3 still (jacket on) until 11.11.028.

### 11.11.012 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Masons do."   (7 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (frame left); TUT (frame right)
- **Action:** Adaeze reminds him what he told Rami; he answers.
- **Dialogue:** ADAEZE: "You told Rami stars don't need a door with copper handles." TUT: "They do not. Masons do."
- **Sound:** the voice at the top falling silent
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: in the low stone passage {CHAR_ADAEZE.SHORT}, turns to {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and speaks one sentence with a tired half-smile, and he answers with two short ones, his eyes still up the gallery. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Callback to 6.3 ("Stars do not need a door with copper handles").

### 11.11.013 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — INSERT: a line beneath the marks   (5 s)
- **Shot:** Insert, 100mm macro, slow tilt down · **Move:** slow tilt down (the snake camera)
- **In frame:** the cavity floor
- **Action:** On the feed (COMP), the camera tilts; beneath the marks, a fainter line of signs no lamp has ever reached.
- **Dialogue:** —
- **Sound:** the feed's hiss; the inch-worm's click
- **PROMPT:** Insert, 100mm macro lens, slow tilt down: the cool ring of light slides past the faint red ochre strokes and down across the dusty pale stone, where an even fainter row of tiny illegible red signs appears at the very edge of the light. Setting: {LOC_GP_QC_SHAFT.SHORT}, {LOC_GP_QC_SHAFT.AREA_BEHIND_DOOR}, just before dawn. Lighting: {LOC_GP_QC_SHAFT.LIGHT_INCHWORM}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable signs, clear hieroglyphs, numbers, screen interface
- **Refs:** LOC_GP_QC_SHAFT_INCHWORM
- **Flags:** COMP
- **Comp:** hidden line | the line of signs for "Bridge the two" (⟂ fiction; drawn by the Egyptologist from research 09's palette) | beneath the marks, tracked | from 2 s | glyph element · feed | SESHAT's feed treatment
- **Continuity:** The plate carries only "tiny illegible red signs"; every sign is comp.

### 11.11.014 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "A human voice on the record."   (6 s)
- **Shot:** Wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C, at the top); UNIT_SHABTI (slits); AKHENATEN, TOMAS (soft)
- **Action:** Up at the top of the Gallery, Nour stands with the tablet among the amber slits as SESHAT asks her to read.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "There is a line beneath the marks. Dr. Kamel, I would like a human voice on the record."
- **Sound:** the voice at the top, close now
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: long-lens compression up the steep corbelled vault to its top, where {CHAR_NOUR.SHORT}, stands among the small amber slits of standing robots, a softly glowing tablet in her hands, and turns her face toward the nearest robot. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its top, above the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, soft screen light on her face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, readable screen, torches
- **Refs:** CHAR_NOUR_C_full, PROP_TABLET_LAYLA, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** Top of the Gallery = top of frame; the great step and the (still closed) wall above it.

### 11.11.015 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Bridge the two."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C)
- **Action:** Nour, glasses on, reads the line off the tablet; her voice comes down the stone.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "Bridge the two."
- **Sound:** her voice travelling down fifty metres of stone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_C}, {CHAR_NOUR.DMG_L2}, narrow glasses on, reads from a glowing tablet held low, reciting aloud in a measured, ritual cadence in an ancient language, three words, then looks up over the glasses, down the long dark slope. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its top, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, soft screen light from below. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable screen, praying hands
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_TABLET_LAYLA, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** COMP
- **Comp:** subtitle | "Bridge the two." | lower third (§13.7) | line in to out | seq 11 subtitle file
- **Continuity:** She reads the hidden line aloud "on the record" (the machine needs a human voice).

### 11.11.016 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — It stops him like a hand on his chest   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** The words stop Tut like a hand on his chest.
- **Dialogue:** —
- **Sound:** the double heartbeat, one beat louder
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, hears three distant words from high above and goes completely still, his lips parting slightly, his eyes widening and wet, one hand drifting to his chest. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, in the low passage at its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, clutching the chest in pain, gasping
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** "Bridge the two" rhymes with his own two hearts (glass and flesh): the plate plays it as pure stillness.

### 11.11.017 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — INSERT: the copper loops touch   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off (the inch-worm's own camera)
- **In frame:** UNIT_INCHWORM (arms); the slab's two copper pins
- **Action:** On the feed (COMP), the inch-worm reaches out two fine arms and draws the copper loops together until they touch.
- **Dialogue:** —
- **Sound:** a tiny metallic tick as copper meets copper
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_INCHWORM.LONG}, {UNIT_INCHWORM.STATE_TRAILING}, braced in a tiny square stone shaft, unfolds its two fine pincer arms, grips the two corroded copper loops on the face of a small polished slab and slowly draws them together until they touch. Setting: {LOC_GP_QC_SHAFT.SHORT}, just before dawn. Lighting: {LOC_GP_QC_SHAFT.LIGHT_INCHWORM}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, sparks, electric arc, glowing copper, readable signs
- **Refs:** UNIT_INCHWORM, LOC_GP_QC_SHAFT_INCHWORM
- **Flags:** COMP
- **Comp:** feed | SESHAT's feed treatment as 11.11.008 | full frame | full clip | UNIT_GLYPH_SESHAT asset
- **Continuity:** Hands-on-small-props rule (§10 #36): macro, the unit as subject. Copper loops touch at the end of the clip.

### 11.11.018 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The stone slides   (7 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the top of the Gallery; the great step; the slab
- **Action:** Deep in the pyramid, a sound like a great weight dropping down a well. Dust sifts off the corbels. Above the great step, a stone slab slides back into the wall; behind it a passage climbs into black.
- **Dialogue:** —
- **Sound:** a deep falling weight far inside the stone; a long grinding slide; dust hiss
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: up the whole steep vault, fine dust sifts down from the stepped walls, and at the very top, above a high stone step, a massive block slides slowly back into the wall with a grinding shudder, opening a black doorway, small amber slits and a green glow waiting beside it. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, {LOC_GP_GRAND_GALLERY.STATE_STONE_SLID}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, collapse, falling ceiling, light pouring out of the doorway, glowing symbols
- **Refs:** LOC_GP_GRAND_GALLERY_SLITS, UNIT_SHABTI, PROP_CASKET_NEST
- **Flags:** VFX-ASSIST
- **Continuity:** STATE_STONE_SLID from here (12.4, 12.7). Deliver before/after plates (closed / slid) and build the slide between them if the generator fails (§6.3).

### 11.11.019 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The procession files up; Nour turns at the lip   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (bearers with casket; spool-bearer); AKHENATEN; TOMAS; NOUR (last)
- **Action:** The procession files up through the opening, Nour last; at the lip she turns and looks down the whole length of the Gallery.
- **Dialogue:** —
- **Sound:** ticks receding into the new passage; her boots stopping
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: at the top of the slope pale robots bearing a softly green-lit casket step up through a black doorway, {CHAR_AKHENATEN.SHORT} and {CHAR_TOMAS.SHORT} following, and last {CHAR_NOUR.SHORT}, reaches the lip, stops, and turns to look back down the whole dark vault. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, {LOC_GP_GRAND_GALLERY.STATE_STONE_SLID}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, {CHAR_AKHENATEN.NEG}, {CHAR_TOMAS.NEG}, running, crowds
- **Refs:** CHAR_NOUR_C_full, CHAR_AKHENATEN_A_full, CHAR_TOMAS_C_full, UNIT_SHABTI, PROP_CASKET_NEST, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** The thread-spool bearer goes up just before Nour; the thread runs up the floor through the doorway.

### 11.11.020 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — At the bottom, a small amber heartbeat   (5 s)
- **Shot:** Wide high-angle shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (tiny, at the bottom); the whole Gallery (Nour's POV)
- **Action:** At the bottom, Tut steps out into the open: a small amber heartbeat at the foot of fifty metres of stone.
- **Dialogue:** —
- **Sound:** silence; one heartbeat, then another
- **PROMPT:** Wide high-angle shot, anamorphic 75mm lens, locked-off, looking straight down the whole steep dark vault from its top: far below at its foot, a slight figure in a charcoal hood steps out into the open onto the walkway, a tiny warm glow pulsing at his chest, alone in the dark. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, seen from its top, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bright lights, several figures
- **Refs:** LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH, CHAR_TUT_B1_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Nour's POV from the lip. The pulse is COMP (G1, slow double beat).

### 11.11.021 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — She touches the pendant   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; PROP_LAYLA_PENDANT
- **Action:** Nour touches the silver pendant at her throat.
- **Dialogue:** —
- **Sound:** her breath
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, looking far down the slope past the lens, lifts her fingers to {PROP_LAYLA_PENDANT.SHORT}, {PROP_LAYLA_PENDANT.STATE_TOUCHED}, and holds them there, her eyes wet and steady. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its top, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}, amber slit light on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable engraving, crying openly
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, PROP_LAYLA_PENDANT, LOC_GP_GRAND_GALLERY_SLITS
- **Continuity:** File 04: STATE_TOUCHED is this beat (11.5). The name on the pendant is never legible here.

### 11.11.022 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — He lifts his hand   (4 s)
- **Shot:** Medium close-up, low-angle, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** At the bottom, Tut lifts his hand to her.
- **Dialogue:** —
- **Sound:** silence
- **PROMPT:** Medium close-up low-angle shot, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, standing alone at the foot of the dark slope, looks up the length of the vault and slowly lifts his open left hand to shoulder height, and holds it there. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, its foot, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, waving, smiling
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** LEFT hand raised (stick in the right).

### 11.11.023 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — A courteous hand; she goes   (5 s)
- **Shot:** Medium shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; UNIT_SHABTI (the spool-bearer); UNIT_THREAD
- **Action:** A shabti touches her shoulder, courteously, and she goes; the thread pays out behind her.
- **Dialogue:** —
- **Sound:** a ceramic tick; her steps receding
- **PROMPT:** Medium shot, anamorphic 75mm lens, locked-off: at the black doorway above the great step, {UNIT_SHABTI.SHORT}, lays two fingers lightly on the shoulder of {CHAR_NOUR.SHORT}, and she turns and goes up into the dark, a hair-fine glint trailing along the stone behind her. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, {LOC_GP_GRAND_GALLERY.STATE_STONE_SLID}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_SLITS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, pushing, grabbing, rope
- **Refs:** CHAR_NOUR_C_full, UNIT_SHABTI, UNIT_THREAD, LOC_GP_GRAND_GALLERY_SLITS
- **Flags:** VFX-ASSIST
- **Continuity:** The Gallery's top is empty of the procession after this; the thread runs up through the doorway (glint = VFX line).

### 11.11.024 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The red line finds him, and holds   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (east ramp)
- **Action:** The jackal's red line finds Tut, holds, and does not fire: it will not risk the heart.
- **Dialogue:** —
- **Sound:** its servo whisper stops; silence
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: on the narrow east ramp {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_D1}, swings its head toward frame right, freezes mid-stride with one forefoot raised, and holds absolutely still, its thin red line fixed on something off frame, its body side-on to the camera. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle flash, laser beam, firing
- **Refs:** UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** The heart is the prize: the jackal's last orders forbid risking it. Tut is on the west side (frame right from the east ramp).

### 11.11.025 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — He starts up the west ramp   (5 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TUT (lead); ADAEZE and FATHI (in his shadow); UNIT_JACKAL red line (east ramp)
- **Action:** Tut starts up the west ramp, stick biting stone, Adaeze and Fathi in his shadow; the red line finds no way past him.
- **Dialogue:** —
- **Sound:** the stick biting stone, step by step; the red line's servo whisper tracking
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, climbs away up the narrow west ramp at frame right, the staff biting the stone, and close behind him, shielded by his body, {CHAR_ADAEZE.SHORT} and {CHAR_FATHI.SHORT}, climb in his shadow, while a thin red line on the far ramp tracks them. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_FATHI.NEG}, running, laser beam
- **Refs:** CHAR_TUT_B1_full, CHAR_ADAEZE_C_full, CHAR_FATHI_B_full, UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Gallery climb chain (§8.4): low-angle clips of figures climbing away; hidden cuts on the corbels' shadow bands. West ramp = frame right. Tut's body shields the other two.

### 11.11.026 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Twenty minutes behind them."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm, lateral track · **Move:** lateral tracking right (up the slope) at climbing pace
- **In frame:** TUT; ADAEZE (soft, behind)
- **Action:** Tut climbs, and says what it costs.
- **Dialogue:** TUT: "Twenty minutes behind them." (beat) "Long enough for them to start without me."
- **Sound:** his breath (from habit); the stick
- **PROMPT:** Medium shot, anamorphic 50mm lens, lateral tracking right, at climbing pace up the slope: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, climbs the steep stone ramp in profile, speaks one short sentence, a pause, then one more, quietly, his eyes fixed on the black doorway far above. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, fast climbing, running
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_A0_profile, CHAR_TUT_B1_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Three-quarter to camera on the lines (sync ≤45°). Adaeze soft over his shoulder.

### 11.11.027 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The Reis tears out and climbs after them   (5 s)
- **Shot:** Wide high-angle shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS; UNIT_SHABTI ×3 (work gang dragging at its legs)
- **Action:** Below, the Reis tears out of the passage mouth and climbs after them, the work gang dragging at its legs.
- **Dialogue:** —
- **Sound:** ceramic grinding and scraping; the Reis's hum; the gang's ticks out of rhythm now
- **PROMPT:** Wide high-angle shot, anamorphic 35mm lens, locked-off, looking down the slope: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_DUST}, tears free of a square opening at the gallery's foot and climbs the west ramp with slow, heavy, measured strides, three pale robots clinging to its legs and dragging behind it. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, right hand present, robot face, fluid
- **Refs:** UNIT_REIS, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** From above (reverse of 11.11.025); the Reis comes up the WEST ramp behind Tut (frame left from this angle).

### 11.11.028 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The hand on the hood; he twists out of the jacket   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** TUT (B3 → C); UNIT_REIS (hand and arm)
- **Action:** The Reis reaches the witness; its one hand closes on the hood of Tarek's charcoal jacket. Tut twists out of the jacket, and out of the jackal's line.
- **Dialogue:** —
- **Sound:** canvas tearing at a seam; ceramic fingers clacking shut
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: a huge bone-white ceramic hand closes on the hood of a charcoal field jacket worn by {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, and he drops his shoulders and twists down and out of the jacket in one movement, leaving it hanging empty in the white fist, his white linen tunic bright in the torchlight. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, choking, hand on his throat, robot face, bare torso
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_C3_full, UNIT_REIS, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Tut T-B → T-C here: the jacket stays in the Reis's LEFT fist (its only hand). The map case stays tucked in the tunic. Wet, torn tunic (WARD_C) from here.

### 11.11.029 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The stick clatters away into the dark   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** PROP_EBONY_STICK; UNIT_REIS (forearm, soft)
- **Action:** The Reis's arm sweeps the stick from his grip; it clatters away down the ramp into the dark.
- **Dialogue:** —
- **Sound:** a crack of wood on ceramic; the stick clattering down stone, bouncing, gone
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: a pale ceramic forearm sweeps through frame and knocks {PROP_EBONY_STICK.LONG}, {PROP_EBONY_STICK.STATE_ST2}, out of a slim olive-brown hand; the staff hits the stone ramp and clatters away down the slope, spinning, into the black. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, stick breaking, sparks, hand injured
- **Refs:** PROP_EBONY_STICK, CHAR_TUT_HANDS, UNIT_REIS, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** Stick LOST here (absent in Seq 12: "I lost it. It seems I can walk."). Dented gold foot cap (ST2).

### 11.11.030 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Dust over Adaeze; Fathi fires until empty   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** ADAEZE; FATHI
- **Action:** The jackal fires; stone dust bursts over Adaeze's head. Fathi fires back down the ramp until his rifle clicks empty, and hauls her on up.
- **Dialogue:** —
- **Sound:** the jackal's crack; stone bursting; Fathi's rifle hammering, then the dry click, click
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: stone dust bursts off the wall just above the head of {CHAR_ADAEZE.SHORT} as she ducks, and {CHAR_FATHI.SHORT}, fires his rifle across frame to the left, away from the camera, down toward the far ramp until it stops, then grabs her arm and hauls her on up the slope. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}, rifle flashes. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_FATHI.NEG}, weapon pointed at the camera, muzzle facing the lens, person hit, tracer fire
- **Refs:** CHAR_ADAEZE_C_full, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Fathi's rifle EMPTY from here (file 01). The jackal stays on the east ramp; no human is hit.

### 11.11.031 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — An empty jacket in its fist   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS; UNIT_SHABTI ×3
- **Action:** The work gang drags the Reis back down a step, an empty jacket in its fist.
- **Dialogue:** —
- **Sound:** ceramic scraping backward down stone
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: three pale robots haul {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, backward down a step of the steep ramp by its legs, and it comes, slowly, an empty charcoal field jacket hanging from its one white fist. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, person inside the jacket, right hand present, robot face
- **Refs:** UNIT_REIS, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_FIGHT
- **Continuity:** Tarek's jacket (given to Tut in 4.4) ends in the Reis's fist. The gang holds the Reis on the lower ramp into Seq 12.

### 11.11.032 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — White linen, the black foot bare on the stone   (5 s)
- **Shot:** Full shot, low-angle, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_C)
- **Action:** Tut stands on the ramp in white linen, the black ceramic foot bare on the stone. He has never trusted it.
- **Dialogue:** —
- **Sound:** the fight dropping away below; his breath
- **PROMPT:** Full low-angle shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_KNEE_CRACK}, stands alone on the steep stone ramp with empty hands, the corbelled walls rising into black behind him, and looks down at his feet: {CHAR_TUT.STATE_FOOT}. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, jacket, walking stick, two sandals, bare left foot of flesh
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_C3_full, CHAR_TUT_FOOT, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Tut look C (T-C at L3, wet and torn, no jacket, no stick). Dagger still on its webbing belt at the right hip (hidden under the tunic's fold; drawn in 11.11.035). Ceramic LEFT foot; sandal on the right.

### 11.11.033 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — A step. It holds.   (5 s)
- **Shot:** Insert, low-angle, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (feet)
- **Action:** He takes a step. It holds. Another.
- **Dialogue:** —
- **Sound:** a hard ceramic click on stone; a soft sandal; click; sandal
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, at stone level: {CHAR_TUT.STATE_FOOT}; the black ceramic foot lifts and sets down on the steep stone ramp, takes the weight, holds, and then the sandalled right foot passes it, and the black foot steps again. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the west ramp, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, the warm glow from above. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, deformed feet, extra toes, two ceramic feet, bare flesh left foot, walking stick
- **Refs:** CHAR_TUT_FOOT, CHAR_TUT_C3_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from above on the foot | full clip | glow element
- **Continuity:** The foot holds: the first unaided steps of his life (file 01 STATE_NO_STICK).

### 11.11.034 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — He climbs the great step alone   (7 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_C, climbing away); FATHI and ADAEZE (below, soft)
- **Action:** For the first time in his life, he walks without a stick. He climbs the great step alone.
- **Dialogue:** —
- **Sound:** click, sandal, click; no music yet, then the first note
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_NO_STICK}, climbs away up the last of the steep ramp in white linen, a warm glow at his chest, and steps up onto the high stone step at the top by himself, standing upright beside the black doorway. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, {LOC_GP_GRAND_GALLERY.STATE_STONE_SLID}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, walking stick, jacket, helped by others
- **Refs:** CHAR_TUT_C3_full, CHAR_TUT_FOOT, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Gallery climb chain (§8.4). Fathi and Adaeze reach the step just after him (off the edge of frame).

### 11.11.035 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — The dagger, hilt first   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_DAGGER; TUT (hand); FATHI (hand)
- **Action:** At the top he draws the iron dagger and holds it out to Fathi hilt first.
- **Dialogue:** —
- **Sound:** gold on gold as it leaves the sheath
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slim olive-brown hand, {CHAR_TUT.STATE_WRIST_CRACK}, draws {PROP_DAGGER.LONG} from its gold sheath and turns it in the warm glow, offering it across frame hilt first, the pale blade laid flat along his forearm, toward a broad deep-brown hand. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, blade pointed at the camera, blade toward the other man, blood, modern knife
- **Refs:** PROP_DAGGER, CHAR_TUT_HANDS, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow on the hands and blade | full clip | glow element
- **Continuity:** Dagger → Fathi here (bible §12). The blade points back along Tut's own arm; hilt toward Fathi.

### 11.11.036 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "The only blade the machines did not make."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_C)
- **Action:** Tut tells Fathi what it is.
- **Dialogue:** TUT: "The only blade here the machines did not make."
- **Sound:** the fight below, distant
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_G1}, on the high stone step, holds the soldier's gaze just off frame right and speaks one quiet sentence, royal and plain. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, jacket
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Meteoritic iron: fallen from the sky, older than any machine.

### 11.11.037 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "Ya Malik..." "Keep the thread whole."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI
- **Action:** Fathi, the dagger in his hands, can only say the title; Tut gives him his last order.
- **Dialogue:** FATHI: "Ya Malik..." TUT (O.S.): "Keep the thread whole."
- **Sound:** Fathi's voice cracking on the second word
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.SHORT}, holding an ancient gold-hilted dagger in both hands, looks at the young man off frame left and speaks two words, his voice breaking, then listens and nods once, his jaw setting. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, tears streaming, kneeling
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, PROP_DAGGER, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Continuity:** "Ya Malik" (O King) stays unsubtitled in the English master, as scripted (localisation to confirm). Tut's line off screen.

### 11.11.038 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — He turns to face the Gallery; a second red line   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (back three-quarter); UNIT_THREAD; UNIT_JACKAL ×2 red lines (far below)
- **Action:** Fathi takes the dagger and turns to face the Gallery, the thread running past his feet into the dark. Below, a second red line slides out of the Ascending Passage.
- **Dialogue:** —
- **Sound:** his boots settling; far below, a second soft pad-tap
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off, from behind his shoulder: {CHAR_FATHI.SHORT}, {PROP_DAGGER.SHORT} in his right hand, turns on the high stone step to face down the long dark slope, a hair-fine glint running past his boots, and far below a second thin red line slides out of the square opening at the bottom. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, laser beams, rope
- **Refs:** CHAR_FATHI_B_full, PROP_DAGGER, UNIT_THREAD, UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Fathi holds the top of the great step into Seq 12 (the intercut fight). Two jackals now. Dagger in his RIGHT hand; the empty rifle slung.

### 11.11.039 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — "I'll be here to carry you out."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI
- **Action:** Fathi, over his shoulder, sends them on.
- **Dialogue:** FATHI: "Go. I'll be here to carry you out."
- **Sound:** the second jackal's pad-taps climbing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.SHORT}, facing down the dark slope with the gold-hilted dagger low at his side, turns his head over his shoulder toward the doorway behind him and speaks two short sentences, calm and warm, then turns back to the dark. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, the great step, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}, {GRADE_UNDERGROUND.TEXT}, a warm glow from the doorway on his cheek. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, fast head turn, weapon pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow from the doorway on his cheek | full clip | glow element
- **Continuity:** The promise he keeps at dawn (12.7: Fathi and Nour carry Tut out). Head turn slow, face at three-quarter for sync.

### 11.11.040 — INT. GREAT PYRAMID, GRAND GALLERY - NIGHT — Up into the stone   (5 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TUT; ADAEZE; FATHI (fg, back to camera)
- **Action:** Tut and Adaeze go up into the stone. SUPER: 05:20.
- **Dialogue:** —
- **Sound:** their steps swallowed by the passage; the jackal climbing below
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: past the soldier's back at the edge of frame, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, and {CHAR_ADAEZE.SHORT}, limping, her hand on his shoulder, step through the black doorway above the great step and are swallowed by the dark, his warm glow shrinking to a point and gone. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, {LOC_GP_GRAND_GALLERY.STATE_STONE_SLID}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, light pouring from the doorway, walking stick
- **Refs:** CHAR_TUT_C3_full, CHAR_ADAEZE_C_full, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH
- **Flags:** COMP
- **Comp:** SUPER | "05:20." | lower left, small (§13.7) | in at 2 s, out at 4.5 s | seq 11 cards file · chest glow bounce | G1 colour and slow double pulse (file 01) on the light it throws: the glow shrinking to a point in the doorway | full clip | glow element
- **Continuity:** 05:20 (bible §12). The procession is twenty minutes ahead; the Hall begins without him (12.1).

## SCENE 11.12 — INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS

### 11.12.001 — INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS — A metre of stone at a time   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, the camera follows behind · **Move:** the camera follows behind them, slowly
- **In frame:** ADAEZE (nearest, her hand on his shoulder); TUT (ahead, glow)
- **Action:** A narrow way climbs steeply, black but for the heartbeat in Tut's chest, lighting a metre of stone at a time. Adaeze behind, her hand on his shoulder. Both limp; each holds the other up.
- **Dialogue:** —
- **Sound:** two limping rhythms, click-sandal and scuff; the slow double heartbeat
- **PROMPT:** Wide shot, anamorphic 24mm lens, the camera follows behind: up a narrow steep way of shallow steps, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_NO_STICK}, climbs ahead with a warm glow at his chest lighting a metre of pale stone around him, and {CHAR_ADAEZE.SHORT}, limping, follows with one hand on his shoulder, each holding the other up. Setting: {LOC_GP_PASSAGE_ABOVE.LONG}, just before dawn. Lighting: {LOC_GP_PASSAGE_ABOVE.LIGHT_HEART_GLOW}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, torches, electric light, carvings, inscriptions
- **Refs:** LOC_GP_PASSAGE_ABOVE_HEART_GLOW, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** Never-seen passage (fiction, file 03 entry 51): perfectly fitted joints, unworn steps. The glow is the only light.

### 11.12.002 — INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS — Nour's voice through the stone   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_C)
- **Action:** Far above, faint through the stone: Nour's voice. Tut stops and lifts his face to it.
- **Dialogue:** NOUR (O.S.; in Middle Egyptian; subtitled): "...I know thee, and I know thy name..."
- **Sound:** her voice faint and far through solid stone; his heartbeat
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_G1}, stops on a shallow step in a narrow stone passage and lifts his face toward a faint sound from far above, listening, his eyes closing for a moment, then opening. Setting: {LOC_GP_PASSAGE_ABOVE.SHORT}, just before dawn. Lighting: {LOC_GP_PASSAGE_ABOVE.LIGHT_HEART_GLOW}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, speaking, smiling broadly
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, LOC_GP_PASSAGE_ABOVE_HEART_GLOW
- **Flags:** COMP
- **Comp:** subtitle | "...I know thee, and I know thy name..." (italic: off-screen, far) | lower third (§13.7) | line in to out | seq 11 subtitle file · chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** The Hall has begun (12.1 intercut starts from here). The glow's pulse is slowing (G1, COMP).

### 11.12.003 — INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS — Still in the stone, climbing toward her voice   (5 s)
- **Shot:** Wide low-angle shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** TUT; ADAEZE
- **Action:** Tut is still in the stone. He climbs toward her voice.
- **Dialogue:** —
- **Sound:** Nour's recitation, faint; their steps; the heartbeat fading with the light
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, climbs away up the narrow steep passage toward a low black opening above, {CHAR_ADAEZE.SHORT}, close behind him, the warm glow at his chest lighting a metre of stone around them and then shrinking upward until only black remains. Setting: {LOC_GP_PASSAGE_ABOVE.SHORT}, just before dawn. Lighting: {LOC_GP_PASSAGE_ABOVE.LIGHT_HEART_GLOW}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, light pouring from above, torches
- **Refs:** LOC_GP_PASSAGE_ABOVE_HEART_GLOW, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through the yellow-green glass; slow double heartbeat about 50 bpm, slowing through Seq 11) | through the tunic, centre chest, tracked | full clip | glow element
- **Continuity:** End of Seq 11: fade on black as the glow leaves frame. Seq 12 opens in the Hall at 05:20.
