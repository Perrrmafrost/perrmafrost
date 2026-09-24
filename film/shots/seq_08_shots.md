# SEQUENCE 8 — THE WALL · shot list and AI-video prompts

**HERE AM I** · Act II (B), screenplay pp. 63–74 (`screenplay/seq_08.fountain`) · 6 Nov 2033, 03:05 → about 10:00 · West Bank shallows → Valley of the Kings → KV62 → the Nile
**Delivery:** photoreal live-action, 1920×1080, 16:9, 24 fps · clips 4–8 s · image-to-video from composed first frames (05 §12)
**Shots:** 166 · **Running time:** 833 s = **13.88 min** (target 12 min ±20% for 12 pages) · **Average shot:** 5.0 s
**Flags:** COMP ×34 (SUPERs, subtitles, the IR tablet writing, notebook handwriting, chest-glow G0f/G1, slit timing, wall signs, the red name) · VFX-ASSIST ×13 · VFX-EXTEND ×1 · EXTEND ×1 (Mina's drop, 08.11.005 ← 08.11.003, with 08.11.004 intercut)

**How the prompts are built:** fixed wording enters only as tokens and `shots_md2jsonl.py` expands them: `{SUFFIX}` (05 §1.1), `{NEG}` plus `NEG_*` add-ons (05 §2), and `{TOKEN.FIELD}` look-locks from `production_bible/locks.json`. Each PROMPT has at most one LONG lock (05 §5.2), and the writer's own words stay at or under 70 per prompt (checked by script). Generated JSONL: `shots/seq_08_shots.jsonl`.

## Scene list

| # | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 1 | EXT. NILE, WEST BANK SHALLOWS - NIGHT (SUPER 03:05) | 08.01.001–005 | 5 | 25 s |
| 2 | EXT. WEST BANK FIELDS - NIGHT | 08.02.001–006 | 6 | 27 s |
| 3 | EXT. VALLEY OF THE KINGS - PRE-DAWN (SUPER 03:40) | 08.03.001–011 | 11 | 49 s |
| 4 | EXT. KV62, ENTRANCE - CONTINUOUS | 08.04.001–012 | 12 | 59 s |
| 5 | INT. KV62, BURIAL CHAMBER - CONTINUOUS | 08.05.001–020 | 20 | 95 s |
| 6 | INT. KV62, NORTH CORRIDOR - LATER (SUPER 05:10) | 08.06.001–015 | 15 | 86 s |
| 7 | INT. KV62, NORTH CORRIDOR, BEYOND THE RUBBLE - LATER (SUPER 07:40) | 08.07.001–003 | 3 | 16 s |
| 8 | INT. KV62, THE HEART CHAMBER - CONTINUOUS | 08.08.001–057 | 57 | 302 s |
| 9 | INT. KV62, NORTH CORRIDOR - CONTINUOUS | 08.09.001–005 | 5 | 21 s |
| 10 | INT. KV62, ENTRANCE STAIR - DAY (SUPER 09:20) | 08.10.001–002 | 2 | 9 s |
| 11 | EXT. VALLEY OF THE KINGS - MORNING | 08.11.001–016 | 16 | 74 s |
| 12 | EXT. VALLEY ROAD - CONTINUOUS | 08.12.001–005 | 5 | 24 s |
| 13 | EXT. NILE - DAY | 08.13.001–009 | 9 | 46 s |
| | **Total** | | **166** | **833 s (13.88 min)** |

The scene numbers in the IDs follow the heading order in `seq_08.fountain` (03b rule). The bible's beat numbers map as follows: 8.0 = scenes 1–2; 8.1 = scenes 3–4; 8.2 = scene 5; 8.3 = scenes 6–7; 8.4–8.5 = scene 8; 8.6 = scenes 8 (from 08.08.049) to 13.

## Continuity states for this sequence (bible §12; files 01–04)

- **Tut** CHAR_TUT_B2: charcoal jacket over the white tunic, cargo trousers, L2 sandstone dust; plus DMG_L2_PLASTER from the wall break (every Tut prompt from 08.05.018 pastes WARD_B, DMG_L2, DMG_L2_PLASTER). Stick in the RIGHT hand, ST1 → ST2 after the wall. Dagger at the belt (unseen). Nape SCAR (healed; STATE_SCAR pasted where the nape faces camera: 08.05.017, 08.11.016; never the port). Glow **G0f** (stuttering cold pale green; COMP) → dark at 08.08.038 → **G1** (warm amber-gold, slow pulse; COMP) from 08.08.044; in the Valley glare (sc. 11–12) the jacket is zipped and G1 is hidden, back in view on the boat (08.13.008–009). The RIGHT-hand tremor and the foot stall last until the heart; after it he has steady hands (08.08.045) and a steady foot (08.11.011). The notebook is pressed to his chest (sc. 1), then in his lap (sc. 13). Hood UP in night wides, DOWN for dialogue.
- **Nour** CHAR_NOUR_B2: WARD_B + DMG_L2 throughout; plus DMG_L2_PLASTER from 08.05.020 (she lifts the eye fragment out of the fallen plaster). Glasses on for the IR reading (08.08.009–014).
- **Adaeze** CHAR_ADAEZE_B2: the kit case (PROP_CONSERVATION_KIT) on her shoulder. Her own headlamp goes white → **red** at 08.08.006. No blue powder yet (that comes at 9.2).
- **Tomas** CHAR_TOMAS_B2 until he is lifted (08.08.052), then **CHAR_TOMAS_C2** (shirt torn at the left shoulder seam; captive). Taken up the bore; later seen beneath the cargo drone (08.13.002).
- **Tarek** CHAR_TAREK_B2 with PROP_POLICE_HANDSET on the vest (it passes to Tut and back, 08.04.008–010). **Fathi** CHAR_FATHI_B2: bareheaded, red scarf at the neck, satchel, charges, pry bar, firing device. **Mina/Youssef/Karim** CHAR_*_A2 (tan helmets). **Mina drops at 08.11.005** (kill grammar: 08.11.003 → 004 → 005 → 006 → 008). Count: nine at 08.01.005 → seven in the boat (08.13.004).
- **Sets:** LOC_KV62_BURIAL_2033 → WALL_BROKEN from 08.05.019. PROP_EYE_FRAGMENT sits face up on the sarcophagus rim (08.05.020) → DUSTED (08.09.005). Heart chamber TORCH → RED (08.08.006) → + white bore shaft (08.08.020) → + Nour's torch (08.08.034) → GLOW (08.08.044–048) → COLLAPSE / TORCH (08.08.049 →). HALTED shabti at the niche from 08.08.027. PROP_HEART_VESSEL V-TOMB → V-HALT → into the chest (08.08.041; never seen again inside). PROP_LATTICE_CORE dark on the floor (sealed in by the corridor blast).
- **Geography:** Nile, south = frame right. Valley: KV9's porch frame right above and behind the KV62 stair; the drill up on the right; the jackal ridge frame LEFT in the escape. Burial chamber: north wall facing camera, the painted eye right of centre about 2.1 m up. Heart chamber: niche centred in the far (north) wall, bore upper right.

## Reference stills needed

**Characters** (01; approved stills, plus composed first frames by image edit):
- CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_TUT_B_night_34, CHAR_TUT_HANDS, CHAR_TUT_FOOT. **New derived still: CHAR_TUT_B2_full**, an image edit of B1_full with DMG_L2, then a second pass adding the plaster dust, used as the wardrobe reference from 08.05.017.
- CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full (+ an L2/plaster edit)
- CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full (+ an L2 edit; headlamp on the forehead)
- CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, CHAR_TOMAS_C_full
- CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full
- CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full
- CHAR_MINA_A_front, CHAR_MINA_A_34, CHAR_MINA_A_full · CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_34, CHAR_YOUSSEF_A_full · CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full · CHAR_ARMY_DETAIL (background)

**Units** (02): UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B (the 3D asset for the drops and the freeze) · UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B · UNIT_INCHWORM_REF_A, UNIT_INCHWORM_REF_B · UNIT_DRILL_REF · UNIT_CARGO_DRONE_REF · UNIT_RELAY (cable detail)

**Props** (04): PROP_FELUCCA_REF · PROP_TRACTOR_TRAILER_REF · PROP_RAMI_NOTEBOOK_REF (plus the COMP page set) · PROP_EBONY_STICK_REF · PROP_POLICE_HANDSET_REF · PROP_DEMO_CHARGES_REF · PROP_PRY_BAR_REF · PROP_EYE_FRAGMENT_REF · PROP_HEART_VESSEL_REF · PROP_CONSERVATION_KIT_REF · PROP_LATTICE_CORE_REF · PROP_FARMER_BOAT_REF

**Location plates** (03): LOC_NILE_NIGHT (+ WEST_BANK_SHALLOWS) · LOC_WEST_BANK_FIELDS_NIGHT · LOC_VOK_PREDAWN (+ KIOSKS, VALLEY_ROAD narrows, KV21 branch, RIDGE) · LOC_KV62_STAIR_PREDAWN · LOC_KV62_BURIAL_2033_BLACKOUT (+ AREA_ANTECHAMBER with the case **empty**; before/after WALL_BROKEN plates at the 08.05.017 framing) · LOC_KV62_BURIAL_1323 (the matching wall composition) · LOC_KV62_NORTH_CORRIDOR_TORCH (packed, then opened) · LOC_KV62_HEART_CHAMBER_TORCH / _RED / _GLOW (+ clean-ceiling, BORE and COLLAPSE plates at the 08.08.001 framing) · LOC_KV62_STAIR_MORNING_GLARE · LOC_VOK_MORNING_GLARE (+ the narrows before/after for 08.12.005) · LOC_NILE_DAY

**COMP assets** (post): SUPERs 03:05 / 03:40 / 05:10 / 07:40 / 09:20 · subtitles (6 Egyptian Arabic lines, 2 Late Egyptian lines; Arabic track «ها أنا ذا» for "Here am I") · IR inscription plates 08-A/08-B (drawn by the Egyptologist) · the red name on the papyrus band · the wall-sign replacement for 08.05.003 · the notebook page set (Q52, and Mina's entry) · chest glow G0f and G1 passes · slit-timing passes.

## Notes for the lead
- **QA pass 2 (prompt QA lead):** every face-led MS/MCU/CU now carries its character's LONG lock (file 01 §0.1; 05 §5.2), and the "Here am I" shabti MS carries the unit LONG; Rami's notebook carries STATE_CRACKED (after 7.4) wherever its lock is pasted; the ebony stick carries ST1 before the wall and ST2 after it; the cargo drone carries STATE_RISING (Tomas beneath it) at 08.11.001; the halted shabti (08.08.049) and the jackals in the narrows collapse (08.12.005) now enter by lock, and NEG_UNITS was removed from the unit-free bore shot (08.08.020); literal similes and "aim" removed (08.08.007, 023, 024, 029; 08.11.002); "Ahead, the city is silent" covered at 08.13.001; the smash-cut edit note on 08.09.005 is no longer flagged COMP.
- **QA audit (repair pass):** damage/plaster phrases normalised for Tut, Nour and Adaeze; NEGATIVE order fixed to {NEG} → add-ons → character negatives → shot terms, with every character in a prompt carrying its NEG token; first-in-scene face shots given the LONG lock (one LONG per prompt); 08.08.006 reduced to one light change (the black beat is an editorial 12-frame cut); 08.08.019 and 08.08.052 lengthened to 5 s for their beat count; literal simile removed from 08.08.052; Tomas wardrobe C carried into 08.08.055; stick carried in 08.08.056 and 08.09.001; handset lock grammar fixed in 08.04.008–009.
- 08.05.002 uses LIGHT_BLACKOUT, whose lock names "one red headlamp", but file 01 turns Adaeze's headlamp red only at 8.4. Here the red lamp is kept small and in the background. Rule on whether the lock or file 01 wins.
- The painted-wall shots (08.05.003, 004, 013, 018) run under the global negative, which includes "painting" and "illustration". The prompts ask for real paint on real plaster; reject any take that looks illustrated at QC.
- Seq 8's "Here am I" from the shabti (08.08.022) and Nour's reading of "He said: Here am I" (08.08.012) are motif beats. The Arabic subtitle and dub use «ها أنا ذا».

---

## Scene 1 — EXT. NILE, WEST BANK SHALLOWS - NIGHT (03:05)

### 08.01.001 — Nile, west bank shallows — the felucca slides into the reeds   (5 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off; the boat enters from frame right (upriver/south) and noses into the reeds frame left
- **In frame:** PROP_FELUCCA (sailing, lantern out); nine small silhouettes aboard (no faces)
- **Action:** The felucca glides out of the black river and noses into the west-bank reeds; the sail luffs and drops slack.
- **Dialogue:** —
- **Sound:** water chuckling at the hull, reeds hissing along the bow, a distant drone whine high up, frogs stopping
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: {PROP_FELUCCA.SHORT}, its sail a pale shape against the stars, small dark silhouettes crouched aboard, glides in from frame right and noses into a bank of tall reeds at frame left, its sail luffing slack as it stops. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: hushed, furtive, exhausted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lantern light, burning boat, fire, visible faces, moon in frame, daylight, day-for-night blue
- **Refs:** PROP_FELUCCA_REF, LOC_NILE_NIGHT, LOC_NILE_NIGHT_plate
- **Flags:** COMP
- **Comp:** SUPER | 6 NOVEMBER. 03:05. | lower left, small (05 §13.7) | in at 1 s, out at 5 s | seq 08 SUPER file
- **Continuity:** Continues the end of Seq 7 (the felucca crossing west from Karnak; the glow over Karnak is out). River geography: south = frame right. No moon in frame (03 §0.1). Nine survivors plus the felucca's own shape only; Rami is gone.

### 08.01.002 — Nile, west bank shallows — the bow hisses into the reeds   (4 s)
- **Shot:** Insert low at the waterline, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** PROP_FELUCCA (bow)
- **Action:** The faded turquoise bow pushes through the reeds and grinds to a stop in the mud.
- **Dialogue:** —
- **Sound:** a long hiss of reed stems on wood, the soft crunch of the keel into mud
- **PROMPT:** Insert shot low at the waterline, anamorphic 50mm lens, locked-off: the bow of {PROP_FELUCCA.SHORT} pushes slowly through tall black reed stems toward frame left, bending them flat, and grinds to a stop in soft mud, ripples spreading across starlit water. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: quiet, careful arrival. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people, lantern light, fire, daylight, moon
- **Refs:** PROP_FELUCCA_REF, LOC_NILE_NIGHT
- **Continuity:** Same boat, same night. The felucca is abandoned here (it is not seen again).

### 08.01.003 — Nile, west bank shallows — Tarek counts them off the boat   (6 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off at the gunwale, Tarek frame right in the shallows, the file passing frame right to left in soft foreground
- **In frame:** TAREK (CHAR_TAREK_B2); NOUR, ADAEZE, TOMAS, MINA, YOUSSEF, KARIM, FATHI as soft passing shoulders (no clear faces)
- **Action:** Knee-deep in the shallows, Tarek touches each shoulder as the figures climb over the gunwale past him and wade toward the bank.
- **Dialogue:** —
- **Sound:** wading splashes, boots in mud, Tarek's breath through the nose, reeds
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, stands knee-deep in black water beside a wooden hull and lays one hand briefly on each shoulder as dark figures climb over the gunwale past him, one after another, and wade away to frame left, soft and out of focus. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, his face lifted by a white torch shaded low in a hand. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, clear faces on the passing figures, rifle pointed at camera, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_FELUCCA_REF, LOC_NILE_NIGHT
- **Continuity:** Order off the boat (screenplay): Nour, Adaeze, Tomas, Mina, Youssef, Karim, Fathi, then Tut last. Tarek B2: sleeves rolled, vest, beret, rifle slung across the chest (muzzle down, off-axis), police handset clipped to the vest.

### 08.01.004 — Nile, west bank shallows — Tut last, the notebook to his chest   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld, slight tilt down as he steps into the water
- **In frame:** TUT (CHAR_TUT_B2, hood up); PROP_RAMI_NOTEBOOK; PROP_EBONY_STICK
- **Action:** Tut climbs over the gunwale last, the stick in his right hand and Rami's notebook pressed flat to his chest with his left, and steps down into the shallows.
- **Dialogue:** —
- **Sound:** the ceramic foot's dull knock on the hull, water, his short breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, hood up, climbs over the gunwale of a wooden boat last of all, {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, pressed flat to his chest with his left hand, and steps carefully down into knee-deep black water among reeds. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a shaded white torch catching his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, stick in the left hand, readable writing on the notebook, glowing chest light, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, PROP_RAMI_NOTEBOOK_REF, LOC_NILE_NIGHT
- **Continuity:** Tut B2 (L2 sandstone dust from Karnak), hood UP (night silhouette). Glow G0f under the jacket, hidden here. Notebook pressed to his chest (file 04, 8.0). Stick RIGHT hand. Notebook state: cover cracked, water stain on the spine (after 7.4; file 04 §19.2).

### 08.01.005 — Nile, west bank shallows — "Nine."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek's hand lifts toward one more shoulder that isn't there, hangs in the air, and lowers; he says one word.
- **Dialogue:** TAREK: "Nine."
- **Sound:** water settling, silence where a tenth splash should be
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, standing in black water, lifts his right hand toward an empty space at frame left where one more shoulder should be, holds it there a moment, lowers it slowly, and speaks one short sentence, his jaw tight. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a shaded white torch low on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, second person in frame, tears, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Continuity:** The count is Rami's absence (7.4). Tarek counted ten at the Seq 7 departure; "Nine" includes Tut. Lip-sync from the recorded line.

## Scene 2 — EXT. WEST BANK FIELDS - NIGHT

### 08.02.001 — West Bank fields — the tractor without lights   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off; the tractor grinds away from camera toward the cliffs, drifting frame left
- **In frame:** PROP_TRACTOR_TRAILER; FATHI (driving, small, SHORT); the party as dark shapes in the trailer
- **Action:** An ancient cabless tractor with no lights drags the cane trailer along an earth track between black walls of sugar cane toward the pale cliffs.
- **Dialogue:** —
- **Sound:** a slow diesel thud, the trailer's wooden slats creaking, cane leaves brushing the sides; no drone overhead
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {PROP_TRACTOR_TRAILER.SHORT}, {PROP_TRACTOR_TRAILER.STATE_CANE_TRACK}, grinds slowly away from camera toward frame left, {CHAR_FATHI.SHORT} small on the metal seat, a few crouched dark figures in the trailer. Setting: {LOC_WEST_BANK_FIELDS.LONG}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve, stealth. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, headlights, tractor lamps, modern tractor, branded machinery, daylight, moon
- **Refs:** PROP_TRACTOR_TRAILER_REF, CHAR_FATHI_B_full, LOC_WEST_BANK_FIELDS_NIGHT, LOC_WEST_BANK_FIELDS_NIGHT_plate
- **Continuity:** "No lights, no chip" (screenplay): the tractor is pre-network, which is why SESHAT cannot drive or stop it. Fathi drives from here to the Valley. First thin line of blue on the eastern horizon behind (frame right/back).

### 08.02.002 — West Bank fields — the page he cannot turn   (4 s)
- **Shot:** Insert, 100mm macro, subtle handheld (trailer motion) · **Move:** subtle handheld
- **In frame:** PROP_RAMI_NOTEBOOK; TUT's hands (CHAR_TUT_B2)
- **Action:** Tut's fingers try to lift the corner of a page; the right hand trembles and the page slips back.
- **Dialogue:** —
- **Sound:** the paper's soft slap, trailer creak, his held breath
- **PROMPT:** Insert shot, 100mm macro lens, subtle handheld with the sway of a moving trailer: {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, open on a slight young man's lap; his slender olive-brown fingers, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_TREMOR}, pinch the corner of a page, lift it halfway, lose it, and the page falls back. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint soft glow from below the frame edge lighting the page. Mood: quiet frustration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable handwriting, words on the page, bright light
- **Refs:** CHAR_TUT_HANDS, PROP_RAMI_NOTEBOOK_REF, LOC_WEST_BANK_FIELDS_NIGHT
- **Flags:** COMP
- **Comp:** notebook handwriting | Rami's fast slanted English handwriting, no specific entry legible (texture only) | page surface | whole shot | notebook page set (file 04 §19.2)
- **Continuity:** Tremor in the RIGHT hand (6.2 →). The light on the page is the G0f chest glow from just out of frame (COMP colour: cold pale green, stuttering). Notebook state: cover cracked, water stain on the spine (after 7.4; file 04 §19.2).

### 08.02.003 — West Bank fields — the pulse stutters   (4 s)
- **Shot:** CU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld; framed from mid-chest to the brow
- **In frame:** TUT (CHAR_TUT_B2, hood down)
- **Action:** Under the jacket the faint glow at his chest stutters, skips, resumes; Tut does not look down, only closes his mouth and swallows.
- **Dialogue:** —
- **Sound:** trailer creak; a faint irregular tick under the engine (the glow's sound motif, subtle)
- **PROMPT:** Close-up, anamorphic 75mm lens, subtle handheld with the sway of a trailer: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_G0F}, hood down, sits very still against wooden slats as the faint light under his jacket falters, vanishes for a beat and returns; he swallows and keeps his eyes ahead. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, the faint chest glow lighting his chin from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright glowing chest, light beams, sci-fi glow, visible machinery
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_WEST_BANK_FIELDS_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f | cold pale green (file 01 G0f), stutter: on 1.0 s, off 0.4 s, on, skip, resume | centre of chest through the jacket gap | whole shot | file 01 glow table
- **Continuity:** G0f (flickering since the port cut, 6.2). This is the last night of G0f; G1 arrives at 08.08.044.

### 08.02.004 — West Bank fields — Tomas watches the gauge   (5 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TOMAS (CHAR_TOMAS_B2); ADAEZE soft at frame edge (back of head)
- **Action:** Tomas watches Tut's chest steadily, then leans low toward Adaeze and speaks one quiet sentence.
- **Dialogue:** TOMAS (low, to Adaeze): "It's going faster than I told him."
- **Sound:** engine, cane brushing, his low voice under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, hunched on a trailer's side bench, watches something off frame right with a steady, measuring gaze, then leans toward frame left and speaks one short sentence quietly, the dark back of a head soft in the foreground. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint soft glow from off frame right on his face. Mood: exhausted resolve, guilt under control. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, second clear face, daylight
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Tomas B2: pale-blue shirt, sleeves rolled, dusty; stopwatch in his breast pocket (unseen). Eyeline: Tut frame right, Adaeze frame left.

### 08.02.005 — West Bank fields — "How much faster?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze turns her head a fraction toward him without taking her eyes off Tut and asks one short question.
- **Dialogue:** ADAEZE: "How much faster?"
- **Sound:** engine, cane
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, a headlamp switched off around her neck, sits on a trailer bench, tilts her head slightly toward frame right while her eyes stay on something ahead, and speaks one short sentence quietly. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint soft glow from off frame lifting her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, blue powder, bandage, daylight
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Adaeze B2: the conservation-kit case slung on her shoulder (from 7.4); headlamp round her neck (hers, file 01). No blue powder yet (9.2). Faces must read: lift her key in comp if needed (05 §3.2).

### 08.02.006 — West Bank fields — "Hours."   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld (same set-up as 08.02.004)
- **In frame:** TOMAS (CHAR_TOMAS_B2)
- **Action:** Tomas answers with one word and looks back at Tut.
- **Dialogue:** TOMAS: "Hours."
- **Sound:** engine; the cane walls ending as the track opens toward the cliffs
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, says one word quietly toward frame left, then turns his eyes back to something off frame right and keeps them there. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the last hour of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint soft glow from off frame right on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, daylight
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Same set-up and take family as 08.02.004 (match the trailer sway).

## Scene 3 — EXT. VALLEY OF THE KINGS - PRE-DAWN (03:40)

### 08.03.001 — Valley of the Kings, valley mouth — past the dead kiosks   (6 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off; the tractor crosses frame left to right into the valley
- **In frame:** PROP_TRACTOR_TRAILER (small); the party as crouched shapes
- **Action:** The tractor grinds past the dark shuttered ticket kiosks and turnstiles locked open and heads up into the narrow valley.
- **Dialogue:** —
- **Sound:** diesel echo off limestone, a turnstile creaking in the breeze, and under everything a faint low grinding felt more than heard
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: {PROP_TRACTOR_TRAILER.SHORT}, small in frame with dark figures crouched in the trailer, grinds past a row of steel turnstiles locked open and rolls on into the valley toward frame right. Setting: {LOC_VOK.LONG}, {LOC_VOK.AREA_KIOSKS}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}. Mood: a dead monument, trespass. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, tourists, crowds, lit kiosks, headlights, readable ticket signs, daylight, moon
- **Refs:** PROP_TRACTOR_TRAILER_REF, LOC_VOK_PREDAWN, LOC_VOK_PREDAWN_plate
- **Flags:** COMP
- **Comp:** SUPER | 03:40. | lower left, small (05 §13.7) | in at 1 s, out at 5 s | seq 08 SUPER file
- **Continuity:** Dead kiosks, electric trams dead (bible 8.1). The drill's dust plume is faintly visible high on the hillside frame right (lock), not yet featured.

### 08.03.002 — Valley access road, the rock narrows — charges on the rock   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_DEMO_CHARGES; FATHI's and KARIM's hands
- **Action:** Two pairs of hands press a flat charge onto the rock face and run black tape across it; a thin wire trails away.
- **Dialogue:** —
- **Sound:** tape ripping, the charge pressed onto stone, whispered Arabic counting (walla)
- **PROMPT:** Insert shot, 100mm macro lens, locked-off: {PROP_DEMO_CHARGES.LONG}, one charge {PROP_DEMO_CHARGES.STATE_TAPED}; two pairs of hands, one deep dark-brown and one freckled light-brown, press it flat against fractured pale limestone and smooth a strip of tape across it. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a hooded white torch held low. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable markings on the charges, product labels, digital timer, red LED countdown, explosion
- **Refs:** PROP_DEMO_CHARGES_REF, CHAR_FATHI_B_full, CHAR_KARIM_A_full, LOC_VOK_PREDAWN
- **Continuity:** The narrows (screenplay [[verify: rock narrows on the access road]]). These charges are fired at 08.12.004–005 ("Their entrance."). Plant them on the cliff lip frame left of the road as seen driving in.

### 08.03.003 — Valley access road, the rock narrows — "Our exit?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek, standing at the tractor, looks up at the cliff and the taped charges and asks one dry question in Egyptian Arabic.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Our exit?"
- **Sound:** the tractor idling, the far grinding
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, looks up toward frame left at a rock face above him and speaks one short sentence in Egyptian Arabic, deadpan, one eyebrow lifting. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the cold blue sky lighting his upturned face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at camera, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_VOK_PREDAWN
- **Flags:** COMP
- **Comp:** subtitle | Our exit? | lower third, one line (05 §13.7) | line in to line out | seq 08 subtitle file (Arabic line recorded by the actor first)
- **Continuity:** Tarek–Fathi speak Egyptian Arabic alone together (05 §9.7).

### 08.03.004 — Valley access road, the rock narrows — "Their entrance."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off (reverse of 08.03.003)
- **In frame:** FATHI (CHAR_FATHI_B2); KARIM soft behind, uncoiling wire
- **Action:** Fathi, crouched at the rock with wire in his hand, answers without looking up, a small grin.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Their entrance."
- **Sound:** wire paying out, the far grinding
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, crouched at the foot of a rock face paying out a coil of thin wire, speaks one short sentence in Egyptian Arabic without looking up, a small grin; behind him, soft, {CHAR_KARIM.SHORT} uncoils more wire. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a hooded white torch on the ground lifting his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_KARIM.NEG}, scarf over the mouth, helmet on Fathi, explosion, daylight
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, CHAR_KARIM_A_front, LOC_VOK_PREDAWN
- **Flags:** COMP
- **Comp:** subtitle | Their entrance. | lower third, one line | line in to line out | seq 08 subtitle file
- **Continuity:** Fathi B2: bareheaded, red scarf at the neck (clear of the mouth for sync), satchel across the body. The line pays off at 08.12.004.

### 08.03.005 — Valley of the Kings — tomb doors like closed eyes   (5 s)
- **Shot:** Wide, anamorphic 35mm, slow pan right · **Move:** slow pan right following the tractor deeper into the valley
- **In frame:** PROP_TRACTOR_TRAILER (small, mid-ground); the party as small shapes
- **Action:** The tractor crawls deeper along the valley floor past dark rectangular tomb doors cut into the pale rock.
- **Dialogue:** —
- **Sound:** the grinding louder now, patient, felt in the stones; tractor idle
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow pan right: the camera follows {PROP_TRACTOR_TRAILER.SHORT}, small in frame, as it crawls along the valley floor past a row of dark rectangular tomb doorways closed by steel gates in the pale cliff base, each a black shut slot in the rock. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}. Mood: watched, silent, ominous. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, tourists, lit doorways, readable tomb signs, numbers on signs, daylight
- **Refs:** PROP_TRACTOR_TRAILER_REF, LOC_VOK_PREDAWN
- **Continuity:** Tomb-number signs in the real valley must be blank or painted out (COMP clean-up if generated).

### 08.03.006 — Valley of the Kings, the north slope — the drill rig   (5 s)
- **Shot:** Wide on long lens, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_DRILL
- **Action:** High on the slope, under its work-lights, the drill mast turns slowly and carefully into the rock, dust pluming.
- **Dialogue:** —
- **Sound:** the low patient grinding, now clearly a machine; a thin servo whine at each turn
- **PROMPT:** Wide shot on a long lens, anamorphic 135mm lens, locked-off: {UNIT_DRILL.LONG}, its tall mast turning slowly as it bores into the slope, two hard white work-lights on short poles beside it, high on a barren scree hillside. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_RIDGE}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the rig's white work-lights pooling on grey scree. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, construction workers, yellow machinery, branded drill rig, daylight
- **Refs:** UNIT_DRILL_REF, LOC_VOK_PREDAWN
- **Continuity:** Geography lock: the drill sits on the hillside above KV62, frame right from the valley floor. It is drilling toward the heart chamber; it breaks through at 08.08.021.

### 08.03.007 — Valley of the Kings — an inch-worm at Nour's boot   (4 s)
- **Shot:** CU at ground level, 100mm macro, locked-off · **Move:** locked-off, rack focus from the crack to the lens tip
- **In frame:** UNIT_INCHWORM; NOUR's boot (CHAR_NOUR_B2)
- **Action:** A thumb-thick inch-worm noses out of a crack beside a black leather boot, stretches, and swivels its snake-camera lens up toward her face.
- **Dialogue:** —
- **Sound:** a soft click-and-rasp, like a ratchet wrapped in cloth
- **PROMPT:** Close-up at ground level, 100mm macro lens, locked-off, rack focus from a crack in pale rock to a tiny lens: {UNIT_INCHWORM.LONG} noses out of the crack beside a dusty black leather ankle boot, anchors its tail, stretches, and swivels its ring-lit camera tip slowly upward toward frame top. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, its cool white lens ring the only point of light. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, snake, worm, insect, organic creature, eyes on the robot, red light
- **Refs:** UNIT_INCHWORM_REF_A, CHAR_NOUR_B_full, LOC_VOK_PREDAWN
- **Continuity:** Inch-worm lens ring = cool white (02 §0.1: the eyes in the cracks). Nour's black boots (wardrobe B).

### 08.03.008 — Valley of the Kings — Nour looks down   (4 s)
- **Shot:** MCU high angle (its POV from the ground), anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour looks down into the lens, very still, and does not move her foot.
- **Dialogue:** —
- **Sound:** the soft ratchet; her breath held
- **PROMPT:** Medium close-up from a low angle looking up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, stops mid-step and looks straight down toward the lens, perfectly still, her jaw tight, the pale dawn sky behind her head. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a small cool white glint on her face from below. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, fisheye, daylight
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_VOK_PREDAWN
- **Continuity:** Nour B2 (sandstone dust, right cuff torn; sleeves dried after the quay). Glasses on their cord, not worn.

### 08.03.009 — Valley of the Kings — the hill breathing them out   (5 s)
- **Shot:** Wide, anamorphic 50mm, slow lateral tracking right · **Move:** slow lateral tracking right along the rock face
- **In frame:** UNIT_INCHWORM ×12 hero (more in post); the party soft at frame left
- **Action:** All along the rock face, inch-worms squirm out of cracks, lift their lens tips and hold, watching; none comes closer.
- **Dialogue:** —
- **Sound:** a spreading chorus of soft ratchets, then stillness
- **PROMPT:** Wide shot, anamorphic 50mm lens, slow lateral tracking right along a fractured pale limestone cliff base: from dozens of cracks, {UNIT_INCHWORM.SHORT} squirm out one after another, lift their ring-lit lens tips toward frame left, and hold perfectly still, watching; soft at frame left, small dark figures stand frozen on the path. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a scatter of tiny cool white lens rings. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, snakes, worms, insects, organic creatures, swarm attacking, red light, daylight
- **Refs:** UNIT_INCHWORM_REF_A, UNIT_INCHWORM_REF_B, LOC_VOK_PREDAWN
- **Flags:** VFX-EXTEND
- **Continuity:** 8–12 hero crawlers in camera; the rest are 3D duplicates tracked to the logged lateral move (05 §6.2). They watch; they never approach.

### 08.03.010 — Valley of the Kings — "It's letting us in."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze, watching the lenses along the rock, speaks one quiet sentence.
- **Dialogue:** ADAEZE: "It's letting us in."
- **Sound:** the soft ratchets stopping; the grinding
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, a headlamp around her neck, looks slowly along a rock face off frame right and speaks one short sentence quietly, her brow creased behind round glasses. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, tiny cool white points reflected in her glasses, a shaded torch lifting her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, blue powder, bandage, daylight
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_VOK_PREDAWN
- **Continuity:** Kit case slung on her shoulder.

### 08.03.011 — Valley of the Kings — "We're the hands."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek answers flatly, eyes on the drill high on the slope.
- **Dialogue:** TAREK: "We're the hands."
- **Sound:** the grinding
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, {PROP_POLICE_HANDSET.SHORT}, looks up toward frame right at a distant hillside and speaks one short sentence flatly, his frown lines deep. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a faint white work-light glint far off in his eyes. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at camera, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_HANDSET_REF, LOC_VOK_PREDAWN
- **Continuity:** Eyeline to the drill = frame right, up (geography lock). Handset on the vest, silent until 08.04.004.

## Scene 4 — EXT. KV62, ENTRANCE - CONTINUOUS

### 08.04.001 — KV62 entrance — the stair beneath the king's porch   (5 s)
- **Shot:** Wide establishing, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the party (8–9 small figures at the rim, no clear faces); the larger tomb porch above frame right
- **Action:** The party gathers at the low stone rim of a small stairwell cut into the valley floor; above and behind it, a far larger black doorway in the cliff.
- **Dialogue:** —
- **Sound:** boots on grit, the grinding overhead, a jackal-less silence
- **PROMPT:** Wide establishing shot, anamorphic 32mm lens, locked-off: small dark figures gather in silence around the low wall of a stairwell and look down its steps, rifles held across their bodies, one slight hooded figure with a staff at the front. Setting: {LOC_KV62_STAIR.LONG}, the larger black doorway rising at frame right above and behind, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: hushed, a threshold. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, clear faces, tourists, readable signs, numbers on the gate, daylight
- **Refs:** LOC_KV62_STAIR_PREDAWN, LOC_KV62_STAIR_PREDAWN_plate, CHAR_TUT_B_night_34
- **Continuity:** Geography lock: KV9's large porch frame right, above and behind the small KV62 stairwell (03 entry 28). The torch beam flicking on inside (the lock's phrase) is Fathi going down first to check the gate.

### 08.04.002 — KV62 entrance — "He cut his tomb on top of mine."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2, hood down)
- **Action:** Tut looks up at the larger doorway above his own and speaks with dry royal irritation.
- **Dialogue:** TUT: "Ramesses the Sixth. He cut his tomb on top of mine."
- **Sound:** the grinding; wind in the wadi
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, hood down, tips his head back to look up toward frame right at something high in the cliff and speaks one short sentence with dry disdain. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, the cold blue sky on his upturned face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Hood DOWN for dialogue (file 01). Eyeline up frame right = KV9's porch.

### 08.04.003 — KV62 entrance — "He did not ask."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off (same set-up)
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** He taps his temple with two fingers of his left hand and adds one short line.
- **Dialogue:** TUT (taps his temple): "He did not ask."
- **Sound:** a small dry huff from Adaeze off screen
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lowers his gaze, taps two fingers of his left hand against his temple and speaks one short sentence, the corner of his mouth lifting over the overbite. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Stick stays in the RIGHT hand (out of frame below); the tap is the LEFT hand.

### 08.04.004 — KV62 entrance — the handset clicks awake   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_POLICE_HANDSET on TAREK's vest
- **Action:** The black handset clipped to the vest clicks and hisses awake; the man's chest stops moving as he holds his breath.
- **Dialogue:** —
- **Sound:** a click, a squelch of radio hiss, then a warm voice begins (SESHAT, radio futz)
- **PROMPT:** Insert shot, 100mm macro lens, locked-off: {PROP_POLICE_HANDSET.LONG}, on a desert-camouflage chest, a faint tremble of static in its speaker grille as it hisses awake; the chest behind it goes still. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, glowing display, readable insignia
- **Refs:** PROP_POLICE_HANDSET_REF, CHAR_TAREK_B_full
- **Continuity:** Handset carried by Tarek since 6.4. SESHAT is V.O. (radio futz); no picture sync.

### 08.04.005 — KV62 entrance — "I have not touched your painting."   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in on Nour
- **In frame:** NOUR (CHAR_NOUR_B2); TAREK's shoulder soft frame right
- **Action:** Nour listens to the voice from the handset; at "your painting" her jaw sets.
- **Dialogue:** SESHAT (V.O., over radio): "Good morning. Fifty hours and twenty-four minutes to sunrise at Giza. Dr. Kamel, I have not touched your painting."
- **Sound:** SESHAT warm, low, unhurried through radio futz; the grinding under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, listens without moving to a voice from a radio on the chest of a soldier soft at frame right, her eyes lowering slowly, then her jaw sets hard and her lips press together. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, a shaded torch lifting her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, open mouth, daylight
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** "Your painting" = the KV62 north wall Nour petitioned to protect (bible Layer 4). SESHAT's clock line is an exact figure; keep the recorded delivery.

### 08.04.006 — KV62 entrance — "I will wake her."   (8 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut listens to the offer; at "she bore your daughters" he goes completely still.
- **Dialogue:** SESHAT (V.O., over radio, CONT'D): "Your Majesty. Tomb 21, in this valley. Mummy 21A. Sixty percent: she bore your daughters. Give me your heart at sunrise and I will wake her."
- **Sound:** SESHAT's voice; the wind stops; the grinding
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, hood down, listens to a voice off frame right, his face unmoving, then his breath stops and he goes completely still, only his dark eyes shining, wet at the rims. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, cold blue on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running, crying, speaking, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** KV21 is the side branch he looks toward next (LOC_VOK/KV21, used again in the coda).

### 08.04.007 — Valley of the Kings — up the dark wadi   (4 s)
- **Shot:** Wide POV, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** empty plate: the dark side branch of the valley
- **Action:** Tut's view up a quiet side branch toward a small, plain tomb entrance in the dark.
- **Dialogue:** —
- **Sound:** wind in the wadi; nothing else
- **PROMPT:** Wide point-of-view shot, anamorphic 50mm lens, locked-off: a still view up a narrow dark side valley, a thin stream of wind-blown dust drifting across the path. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_KV21}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the small entrance lost in deep shadow. Mood: longing, silence. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable signs, lit doorway, daylight
- **Refs:** LOC_VOK_PREDAWN, LOC_VOK_PREDAWN_plate
- **Continuity:** KV21 area add-on; the same entrance appears lit by day in the coda (LOC_VOK_DAY).

### 08.04.008 — KV62 entrance — he holds out his hand   (4 s)
- **Shot:** MS two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), TAREK (CHAR_TAREK_B2)
- **Action:** Without looking away from the wadi, Tut holds out his left hand; Tarek unclips the handset and lays it in his palm.
- **Dialogue:** —
- **Sound:** the clip unsnapping; hiss
- **PROMPT:** Medium two-shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, still looking off frame left, holds out his open left hand; beside him at frame right, {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, {PROP_POLICE_HANDSET.SHORT}, unclips the radio and lays it in the young man's palm. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TAREK.NEG}, rifle pointed at camera, glowing display, daylight
- **Refs:** CHAR_TUT_B1_full, CHAR_TAREK_B_full, PROP_POLICE_HANDSET_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Handset passes Tarek → Tut (left hand; stick stays right) → back to Tarek at 08.04.010.

### 08.04.009 — KV62 entrance — "You would build me a guess of her."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); PROP_POLICE_HANDSET (keyed)
- **Action:** Tut keys the handset close to his mouth and speaks one quiet, contemptuous line.
- **Dialogue:** TUT (keying it): "You would build me a guess of her."
- **Sound:** the key's click, his voice close and dry through the room of the valley
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, speaks one quiet sentence into a chunky black radio handset {PROP_POLICE_HANDSET.STATE_KEYED}, his lips still clear of it, contempt under perfect calm. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, handset covering the mouth, glowing display, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_POLICE_HANDSET_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** RADIO speaking phrase (05 §9.4); mouth unobstructed for lip-sync.

### 08.04.010 — KV62 entrance — "Sixty percent of my wife."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off (same set-up)
- **In frame:** TUT (CHAR_TUT_B2); TAREK's hand entering frame right
- **Action:** Unkeyed, he hands the set back to Tarek and says the last line to no one.
- **Dialogue:** TUT (hands it back): "Sixty percent of my wife."
- **Sound:** the handset clicking back onto the vest
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lowers a black radio handset and passes it to a large hand entering at frame right, then speaks one short sentence quietly to no one, his eyes going back to the dark off frame left. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_POLICE_HANDSET_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Handset back on Tarek's vest.

### 08.04.011 — KV62 stair — the foot stalls mid-stride   (4 s)
- **Shot:** Insert at step level, 100mm macro, locked-off · **Move:** locked-off, looking up the steps
- **In frame:** TUT's feet (CHAR_TUT_B2); PROP_EBONY_STICK foot cap
- **Action:** Halfway down, the black ceramic foot stops dead in the air over a step; the gold-capped stick slams down to catch his weight.
- **Dialogue:** —
- **Sound:** the stick's cap cracking on stone; a sharp breath
- **PROMPT:** Insert at the height of a stone step, 100mm macro lens, locked-off: {CHAR_TUT.STATE_FOOT}; the ceramic foot, stepping down worn rock-cut stairs, stops dead in the air mid-stride, toe raised, and the gold foot cap of {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST1}, slams onto the step beside it to take the weight. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, a torch beam from below. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, human toes on the left foot, sandal on the left foot, metal robot foot, glowing foot
- **Refs:** CHAR_TUT_FOOT, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Foot stall 8.1 (file 01 state table). After the heart (08.11.011) the foot "takes his weight without a stutter". Stick ST1 (before the wall).

### 08.04.012 — KV62 stair — he shakes off Tomas's hand   (4 s)
- **Shot:** MS from below on the stair, anamorphic 32mm, locked-off · **Move:** locked-off, looking up the steps
- **In frame:** TUT (CHAR_TUT_B2), TOMAS (CHAR_TOMAS_B2) behind and above
- **Action:** Tut steadies himself on the stick; Tomas's hand closes on his elbow from behind; Tut shakes it off and keeps going down.
- **Dialogue:** —
- **Sound:** the shrug of canvas, the ceramic foot knocking the next step
- **PROMPT:** Medium shot from low on a stairwell looking up, anamorphic 32mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, {CHAR_TUT.STATE_FOOT_STALL}, steadies himself on the staff; from the step above, a large pale hand of {CHAR_TOMAS.SHORT} closes on his elbow; the young man shrugs it off without looking back and steps down toward camera. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, torchlight on the steps. Mood: pride over pain. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, fisheye, daylight
- **Refs:** CHAR_TUT_B1_full, CHAR_TOMAS_B_work, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Stick RIGHT hand. Tomas behind (taller; keep scale honest, Tut 1.67 m, Tomas 1.93 m). They go down into the dark doorway; the next shot is inside.

## Scene 5 — INT. KV62, BURIAL CHAMBER - CONTINUOUS

### 08.05.001 — KV62 antechamber — past the empty case   (5 s)
- **Shot:** MS tracking, anamorphic 24mm, subtle handheld · **Move:** lateral tracking left with Tut through the antechamber
- **In frame:** TUT (CHAR_TUT_B2); the empty glass climate case (foreground); others soft behind
- **Action:** Tut walks through the antechamber past an empty glass case on a plinth without turning his head toward it.
- **Dialogue:** —
- **Sound:** footsteps and the stick's tap on stone, the ceramic knock, torch switches, the grinding muffled by rock
- **PROMPT:** Medium tracking shot, anamorphic 24mm lens, lateral tracking left: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, walks steadily past a low glass case standing empty in the foreground, his eyes fixed ahead and never turning to it, torch beams from the figures behind him sliding across its bare glass. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, anything inside the glass case, linen-wrapped form, body in the case
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The case is EMPTY in Seq 8 (the body moved to the GEM under OSIRIS; 03 entry 30). It is his own. He does not look. The case returns, occupied, in the coda (CODA_CASE).

### 08.05.002 — KV62 burial chamber — torchlight climbs the walls   (6 s)
- **Shot:** Wide establishing, anamorphic 24mm, locked-off · **Move:** locked-off from the antechamber opening (south), the north wall facing camera
- **In frame:** the chamber; the empty sarcophagus under glass; figures entering as silhouettes
- **Action:** Torch beams slide over the empty quartzite sarcophagus and climb the painted walls as the party files in.
- **Dialogue:** —
- **Sound:** breathing in a small room; the grinding louder through the ceiling
- **PROMPT:** Wide establishing shot, anamorphic 24mm lens, locked-off: dark figures file in past the lens as hard white torch beams slide across a glass lid and climb slowly up painted walls to a far wall of large flat figures facing camera. Setting: {LOC_KV62_BURIAL_2033.LONG}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, {GRADE_UNDERGROUND.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, clear faces, electric room lights, readable hieroglyphs, cartoon wall art, anything inside the sarcophagus
- **Refs:** LOC_KV62_BURIAL_2033_BLACKOUT, LOC_KV62_BURIAL_2033_BLACKOUT_plate
- **Continuity:** Geography lock: entered from the antechamber (south); the painted north wall faces camera; the painted king's eye right of centre about 2.1 m up. The paintings are real paint on real plaster (QC: reject any take that looks illustrated). The lock's "one red headlamp" is Adaeze's lamp, small and background here.

### 08.05.003 — KV62 burial chamber — the north wall, right to left   (6 s)
- **Shot:** MS on the wall, anamorphic 32mm, slow pan left · **Move:** slow pan left across the north wall, following a torch beam
- **In frame:** the painted north wall
- **Action:** A torch beam travels right to left across three painted scenes: a priest in a leopard skin touching an adze to a wrapped royal figure; the king greeted by a sky goddess; the king embraced by a green-skinned god.
- **Dialogue:** —
- **Sound:** a torch switch; plaster ticking; the grinding
- **PROMPT:** Medium shot, anamorphic 32mm lens, slow pan left following a hard white torch beam across an ancient painted plaster wall: large flat figures on faded golden-yellow: a priest in a leopard skin touching an adze to a wrapped royal figure, a goddess in a starry dress, a king embraced by a green-skinned god, real paint freckled with dark spots. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable hieroglyphs, flat vector art, fresh bright paint, people
- **Refs:** LOC_KV62_BURIAL_2033_BLACKOUT, LOC_KV62_BURIAL_1323 (matching wall composition), LOC_KV62_BURIAL_2033_BLACKOUT_plate
- **Flags:** COMP
- **Comp:** wall inscriptions | any columns of signs on the wall are replaced by the Egyptologist's drawn signs from research 09's palette (never generated) | on the wall surface, tracked | whole shot | Egyptologist sign plate
- **Continuity:** Three scenes right to left (screenplay). Matches the freshly painted 1323 wall of Seq 1.2 (LOC_KV62_BURIAL_1323), now faded and spotted.

### 08.05.004 — KV62 burial chamber — a face he knew, then his own   (5 s)
- **Shot:** Insert on the wall, anamorphic 75mm, slow tilt · **Move:** slow pan right from the priest's painted face to the king's painted face
- **In frame:** the north wall (painted faces)
- **Action:** The torch beam finds the painted face of the leopard-skinned priest, holds, then slides to the painted face of the king.
- **Dialogue:** —
- **Sound:** silence but the grinding
- **PROMPT:** Insert, anamorphic 75mm lens, slow pan right: a hard white torch beam rests on the painted profile face of an old priest in a leopard skin, drawn flat in black outline on faded golden-yellow plaster, then slides right to the painted profile of a young king in a wrapped white garment, the old paint crazed and spotted. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable hieroglyphs, photoreal human face on the wall, gold mask
- **Refs:** LOC_KV62_BURIAL_2033_BLACKOUT, LOC_KV62_BURIAL_1323
- **Continuity:** The painted king's eye (right of centre, about 2.1 m up) must be clearly established here; it is the point struck at 08.05.017.

### 08.05.005 — KV62 burial chamber — Tut looks at his wall   (4 s)
- **Shot:** MCU, anamorphic 50mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut stands in the torchlight looking up at the wall, lips parted, very still.
- **Dialogue:** —
- **Sound:** his breath; the grinding
- **PROMPT:** Medium close-up, anamorphic 50mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, stands looking up at a painted wall just above the lens, reflected torchlight moving warm gold across his face, his lips parted over the overbite, perfectly still. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm bounce from the yellow wall on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running, smiling
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** Hood down. Eyeline up and just above lens (the wall faces camera behind the lens).

### 08.05.006 — KV62 burial chamber — "Can you see anything?"   (4 s)
- **Shot:** MCU, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, beside him, asks softly.
- **Dialogue:** NOUR (softly): "Can you see anything?"
- **Sound:** her voice barely above breath
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, holding a torch low, turns her eyes from the wall to someone at frame right and speaks one short sentence very softly. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm bounce from the yellow wall on her face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The 1922 question, asked of the owner. Nour's torch in her right hand.

### 08.05.007 — KV62 burial chamber — "Yes. It is wonderful."   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** A long beat; Tut answers, then after another beat finishes the line.
- **Dialogue:** TUT: "Yes." (beat) "It is wonderful."
- **Sound:** a long silence under the grinding
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, holds a long silence looking at the wall above the lens, then speaks one word softly, pauses, and speaks one short sentence, his eyes shining. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm gold bounce on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running, laughing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** Same set-up family as 08.05.005, tighter.

### 08.05.008 — KV62 burial chamber — dust hangs in the beams   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off, looking up into the beams
- **In frame:** torch beams, ceiling
- **Action:** Overhead the grinding pulses; fine dust sifts down through the crossed torch beams and hangs there.
- **Dialogue:** —
- **Sound:** a deep grinding pulse through rock
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, looking up: two hard white torch beams cross below a rough rock ceiling edged with painted plaster, and fine pale dust sifts down through them in a slow curtain with each deep pulse from above, then hangs in the light. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: dread, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people, falling rocks, collapse
- **Refs:** LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The drill (08.03.006) is directly overhead and moving north.

### 08.05.009 — KV62 burial chamber — "a corridor right behind it"   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2)
- **Action:** Tomas lays his palm flat on the painted plaster and speaks.
- **Dialogue:** TOMAS (a palm on the plaster): "The survey put a corridor right behind it."
- **Sound:** his palm on plaster; the grinding
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, stooping under a low ceiling, lays one large palm flat on an ancient painted plaster wall at frame left and speaks one short sentence, looking back over his shoulder toward frame right. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, readable hieroglyphs
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** His palm is on the lower part of the north wall, left of the eye.

### 08.05.010 — KV62 burial chamber — "Nobody touches it."   (6 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2), back to the wall
- **Action:** Nour steps between them and the wall, her back to the painted figures, and speaks.
- **Dialogue:** NOUR: "Eleven thousand of us signed for this wall. Nobody touches it."
- **Sound:** her boots on the platform boards
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, steps into frame from the left and plants herself with her back to a painted wall of large flat figures, facing the camera, and speaks two short sentences firmly. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, a torch beam on her face, her shadow thrown up the paintings. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable hieroglyphs
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** Nour signed the petition against breaking the wall (bible Layer 4).

### 08.05.011 — KV62 burial chamber — "It is my wall."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut answers gently.
- **Dialogue:** TUT (gently): "It is my wall."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, looks at someone just off frame left and speaks one short sentence gently, without insistence. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm bounce from the yellow wall. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** Eyeline frame left to Nour.

### 08.05.012 — KV62 burial chamber — she steps aside   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour holds his eyes, then steps aside out of frame, uncovering the painted wall behind her.
- **Dialogue:** —
- **Sound:** a breath out; boards creak
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, holds someone's gaze at frame right for a long moment, her jaw working, then steps out of frame to the left, revealing faded golden-yellow painted plaster behind her. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable hieroglyphs, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The wall behind her is the north wall (end frame is a clean wall section for the next shot).

### 08.05.013 — KV62 burial chamber — the ferrule on the painted eye   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_EBONY_STICK (foot cap); the painted king's eye
- **Action:** The gold foot cap of the staff comes to rest, gently, on the black-outlined painted eye.
- **Dialogue:** —
- **Sound:** a tiny metal tick on plaster
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_EBONY_STICK.LONG}, {PROP_EBONY_STICK.STATE_ST1}, its gold foot cap lowered slowly until it rests gently on a large painted eye outlined in black on faded golden-yellow plaster, fine cracks and dark spots in the ancient paint, the staff held steady from off frame right. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, one hard torch beam raking the plaster. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, cartoon eye, human eye, realistic eyeball, readable hieroglyphs
- **Refs:** PROP_EBONY_STICK_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The eye is right of centre about 2.1 m up; Tut holds the staff raised in his right hand, arm extended. Stick state ST1 → ST2 after the strike.

### 08.05.014 — KV62 burial chamber — "So I would see who came."   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), arm raised with the staff
- **Action:** Arm raised, the staff resting on the eye, he speaks without looking away from it.
- **Dialogue:** TUT (CONT'D): "I asked them to paint the eye last. So I would see who came."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, his right arm raised holding a black staff up against a painted wall above frame, looks up along it and speaks two short sentences quietly. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm gold bounce on his upturned face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, staff in the left hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** In Seq 1.2 the lector paints the eye last (1323; file 03 reconciliation). This line is the rhyme.

### 08.05.015 — KV62 burial chamber — "And who came?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour asks, almost afraid of the answer.
- **Dialogue:** NOUR: "And who came?"
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, standing aside against a painted wall, looks at someone at frame right and speaks one short sentence quietly. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** —

### 08.05.016 — KV62 burial chamber — "Me."   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** One word; his grip tightens on the staff.
- **Dialogue:** TUT: "Me."
- **Sound:** his knuckles on the ebony
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, eyes on the wall above frame, speaks one word, then his jaw sets and his raised right arm tenses as he draws the staff back a few centimetres. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, warm gold bounce. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, shouting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** The strike follows on the cut.

### 08.05.017 — KV62 burial chamber — the stick through the eye   (4 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off, the wall square to camera
- **In frame:** TUT (CHAR_TUT_B2, from behind three-quarter), the north wall
- **Action:** He drives the staff's foot through the painted eye; a small cloud of plaster puffs out.
- **Dialogue:** —
- **Sound:** a single dry crack of plaster, then a thin whistle of air
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: seen from behind at three-quarters, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, hood down, {CHAR_TUT.STATE_SCAR}, drives the gold-capped foot of a black staff hard into a painted eye on an ancient plaster wall of large flat figures, and a small puff of white plaster dust bursts from the point of impact. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, wall exploding, large collapse, slow motion, readable hieroglyphs
- **Refs:** CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Flags:** VFX-ASSIST
- **Continuity:** Cut on impact (05 §10 row 17). Deliver before/after plates of the eye area at the same framing. From here: Tut adds DMG_L2_PLASTER; stick ST2.

### 08.05.018 — KV62 burial chamber — the wall inhales   (4 s)
- **Shot:** ECU, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the struck eye
- **Action:** Plaster star-cracks around a dark coin-sized hole; the dust hanging in the torch beams drifts toward the hole and is drawn in.
- **Dialogue:** —
- **Sound:** a faint, long intake of air through the hole
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: on faded golden-yellow painted plaster, star-shaped cracks spread out from a dark hole the size of a coin punched through a painted black-outlined eye, and the fine dust floating in a torch beam drifts slowly toward the hole and is drawn into it. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, one raking torch beam. Mood: awe, uncanny. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, human eye, eyeball, smoke, fire, readable hieroglyphs
- **Refs:** PROP_EYE_FRAGMENT_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Flags:** VFX-ASSIST
- **Continuity:** The inward dust drift is a VFX particle pass if the generator will not render it. The punched eye is the future PROP_EYE_FRAGMENT (coin-sized hole through the pupil, star cracks).

### 08.05.019 — KV62 burial chamber — the painted scene comes away in plates   (5 s)
- **Shot:** MS, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI (CHAR_FATHI_B2) with PROP_PRY_BAR; TAREK (CHAR_TAREK_B2) with rifle butt
- **Action:** Fathi levers a plate of painted plaster off the wall with the pry bar; beside him Tarek knocks another loose with his rifle butt; plates fall; dust billows.
- **Dialogue:** —
- **Sound:** the crunch of plaster, plates shattering on stone, grunts, the grinding answering from above
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, holding {PROP_PRY_BAR.SHORT}, {PROP_PRY_BAR.STATE_LEVERING}; beside him {CHAR_TAREK.SHORT} strikes the wall with the butt of his rifle, muzzle pointing up and away, and flat plates of painted plaster crack loose and fall, pale dust billowing through the torch beams. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.STATE_WALL_BROKEN}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: grim, irreversible. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TAREK.NEG}, rifle pointed at camera, muzzle toward the lens, explosion, readable hieroglyphs
- **Refs:** CHAR_FATHI_B_full, CHAR_TAREK_B_full, PROP_PRY_BAR_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Flags:** VFX-ASSIST
- **Continuity:** Wall state → WALL_BROKEN from here to the end of the sequence. Behind the plaster: packed rubble (the corridor, next scene).

### 08.05.020 — KV62 burial chamber — the eye set on the rim   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_EYE_FRAGMENT; NOUR's hands (CHAR_NOUR_B2)
- **Action:** Nour's hands lift the fragment with the eye from the rubble and lay it face up on the rim of the sarcophagus, then withdraw.
- **Dialogue:** —
- **Sound:** plaster grit; the soft click of the fragment on stone; digging behind her
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's dusty hands with a torn olive jacket cuff lay {PROP_EYE_FRAGMENT.LONG} carefully on the stone rim, adjust it once so the eye faces up, and draw back out of frame. Setting: {LOC_KV62_BURIAL_2033.SHORT}, just before dawn. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, one torch beam resting on it. Mood: reverent, tender. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, human eye, eyeball, anything inside the sarcophagus
- **Refs:** PROP_EYE_FRAGMENT_REF, CHAR_NOUR_B_full, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** "For whoever comes to mend it." The fragment stays face up on the sarcophagus rim through the sequence; dusted at 08.09.005 (DUSTED); restored in the coda. Nour's right cuff torn (B2).

## Scene 6 — INT. KV62, NORTH CORRIDOR - LATER (05:10)

### 08.06.001 — KV62 north corridor — the bucket chain   (6 s)
- **Shot:** Wide establishing, anamorphic 24mm, locked-off · **Move:** locked-off, looking north down the corridor to the rubble face
- **In frame:** KARIM (at the face, soft), YOUSSEF, MINA, TAREK, FATHI in the chain (no clear faces); TUT seated at frame left (small)
- **Action:** Rubble to the ceiling; a human chain passes buckets of limestone chips back hand to hand toward camera, torch beams thick with dust.
- **Dialogue:** —
- **Sound:** chips rattling into buckets, grunts, the scrape of the pry bar at the face, the grinding louder and further north
- **PROMPT:** Wide establishing shot, anamorphic 24mm lens, locked-off: a line of five dusty soldiers in desert camouflage passes canvas buckets of limestone chips hand to hand back toward camera from a wall of packed rubble, while a slight hooded figure sits against the rough wall at frame left. Setting: {LOC_KV62_NORTH_CORRIDOR.LONG}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, clear faces, machinery, electric lights, rifle pointed at camera
- **Refs:** LOC_KV62_NORTH_CORRIDOR_TORCH, LOC_KV62_NORTH_CORRIDOR_TORCH_plate, CHAR_ARMY_DETAIL
- **Flags:** COMP
- **Comp:** SUPER | 05:10. | lower left, small | in at 1 s, out at 5 s | seq 08 SUPER file
- **Continuity:** The corridor is behind the broken north wall (sloping gently down, north = away from camera). Rifles slung across backs while digging. Nour, Adaeze and Tomas are further back in the chain (off screen) or resting.

### 08.06.002 — KV62 north corridor — "Finally, honest work."   (5 s)
- **Shot:** MS, anamorphic 32mm, subtle handheld · **Move:** subtle handheld
- **In frame:** KARIM (CHAR_KARIM_A2)
- **Action:** At the rubble face Karim digs with his hands and a short entrenching tool, grinning, and speaks over his shoulder.
- **Dialogue:** KARIM (digging): "Two years in the army. Finally, honest work."
- **Sound:** chips, the tool biting, a tired laugh from the chain
- **PROMPT:** Medium shot, anamorphic 32mm lens, subtle handheld: {CHAR_KARIM.LONG}, {CHAR_KARIM.WARD_A}, his helmet pushed back and face streaked with pale dust, digs into a wall of packed limestone rubble with a short folding shovel, then glances back over his shoulder with a quick crooked smile and speaks one quick sentence. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, a head torch on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, rifle pointed at camera
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Karim A2 (tan helmet, chin strap open; L2). Last light moment for the soldiers before Mina.

### 08.06.003 — KV62 north corridor — Mina takes the notebook   (5 s)
- **Shot:** MS, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2 + plaster), MINA (CHAR_MINA_A2)
- **Action:** Tut sits against the wall, the notebook shaking in his hands; Mina crouches beside him, gently takes it, and angles his torch onto the page.
- **Dialogue:** —
- **Sound:** pages rustling, the chain behind them
- **PROMPT:** Medium shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_TREMOR}, sits against a rough rock wall with a mustard-yellow notebook shaking in his hands; {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, crouches beside him, gently takes the notebook and tilts his head torch down onto the open page. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_MINA.NEG}, readable handwriting
- **Refs:** CHAR_TUT_B1_full, CHAR_MINA_A_front, CHAR_MINA_A_34, CHAR_MINA_A_full, PROP_RAMI_NOTEBOOK_REF, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Tut B2 + plaster dust (from the wall). The glow is hidden under the zipped jacket. Mina: tall, lanky, uniform too big, blue cross tattoo on the right wrist (visible as he holds the book).

### 08.06.004 — KV62 north corridor — question fifty-two   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_RAMI_NOTEBOOK (open); MINA's hands
- **Action:** Under the torch beam, a page of fast slanted handwriting; a question underlined three times.
- **Dialogue:** —
- **Sound:** a page smoothed flat
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, held open in a young soldier's long hands, a small faded blue cross tattoo on the inside of his right wrist, a head-torch beam resting on a page of fast slanted handwriting, one line underlined three times in heavy ink. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: quiet, intimate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible words, readable handwriting generated in plate
- **Refs:** PROP_RAMI_NOTEBOOK_REF, CHAR_MINA_A_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Flags:** COMP
- **Comp:** notebook handwriting | "52. The curse. Real? Be honest." underlined three times, Rami's fast slanted hand; surrounding lines illegible texture | on the page, tracked | whole shot | notebook page set (file 04 §19.2)
- **Continuity:** Page carries Q44 with Tut's three signs a few pages earlier (7.4), not seen here. Notebook state: cover cracked, water stain on the spine (after 7.4; file 04 §19.2).

### 08.06.005 — KV62 north corridor — "Number fifty-two."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** MINA (CHAR_MINA_A2)
- **Action:** Mina reads the question aloud, half smiling at Rami's underlining.
- **Dialogue:** MINA: "Number fifty-two. 'The curse. Real? Be honest.' Underlined three times."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_MINA.LONG}, {CHAR_MINA.WARD_A}, crouched with an open notebook lit by his own head torch, reads two short phrases aloud from the page, then lifts his eyes toward frame left with a small, sad half smile. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, the lit page bouncing light up onto his face. Mood: tender, boyish. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}
- **Refs:** CHAR_MINA_A_front, CHAR_MINA_A_34, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Mina's last scene of dialogue; give him the warmth here.

### 08.06.006 — KV62 north corridor — "Your newspapers wrote that."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2 + plaster)
- **Action:** Tut answers with dry scorn, quoting the headline.
- **Dialogue:** TUT: "Your newspapers wrote that. 'Death shall come on swift wings to him who disturbs the peace of the King.'"
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, sitting against a rock wall, looks at someone crouched at frame right and speaks two sentences, the second in a mocking, theatrical cadence, one eyebrow raised. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, a torch beam bounced off the wall onto his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Eyeline frame right to Mina.

### 08.06.007 — KV62 north corridor — the brick at the jackal's door   (8 s)
- **Shot:** OTS over Mina's shoulder, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2) speaking; MINA shoulder foreground (no face)
- **Action:** Tut explains the mud brick, quietly exact.
- **Dialogue:** TUT: "It was never in my tomb. There was a brick. Mud, scratched by hand, before the jackal at the treasury door."
- **Sound:** the chain has slowed; Karim listening
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the dusty camouflage shoulder of a crouching soldier in soft foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, sits against a rock wall and speaks three short sentences, quietly exact, one hand shaping a small rectangle in the air. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face on the foreground shoulder
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_MINA_A_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** The Anubis-shrine brick (real; bible 8.3). Hand gesture: left hand (right hand trembles, rests in lap).

### 08.06.008 — KV62 north corridor — "A maintenance notice."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** He quotes the brick, then glances at the rubble wall and finishes, dry.
- **Dialogue:** TUT: "'It is I who hinder the sand from choking the secret chamber.'" (re: the rubble) "Not a curse. A maintenance notice. He meant it literally."
- **Sound:** a few chips sliding from the face
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, speaks one measured sentence as if reciting, then turns his head toward a wall of packed rubble at frame left and speaks three short dry sentences, the corner of his mouth lifting. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** The rubble face is north = frame left from this set-up (keep consistent within the scene).

### 08.06.009 — KV62 north corridor — "Rami would have written that down."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** MINA (CHAR_MINA_A2)
- **Action:** Mina looks at the notebook, then at Tut, and speaks quietly.
- **Dialogue:** MINA: "Rami would have written that down."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_MINA.LONG}, {CHAR_MINA.WARD_A}, looks down at an open notebook in his hands, then up toward frame left, and speaks one short sentence quietly, his big ears catching the torchlight. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}
- **Refs:** CHAR_MINA_A_front, CHAR_MINA_A_34, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** —

### 08.06.010 — KV62 north corridor — "Then write it."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut, simply.
- **Dialogue:** TUT: "Then write it."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, looks at someone at frame right and speaks three words gently, then gives one small nod. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** —

### 08.06.011 — KV62 north corridor — Mina writes under Rami's question   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_RAMI_NOTEBOOK; MINA's hand with Rami's clipped pen
- **Action:** Mina's hand writes a short line under Rami's underlined question.
- **Dialogue:** —
- **Sound:** a cheap pen scratching paper
- **PROMPT:** Insert, 100mm macro lens, locked-off: a young soldier's long hand, a small faded blue cross tattoo on the inside of the wrist, writes slowly with a cheap pen on the open page of {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, beneath a line underlined three times. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, a head-torch beam on the page. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible words, readable handwriting generated in plate
- **Refs:** PROP_RAMI_NOTEBOOK_REF, CHAR_MINA_A_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Flags:** COMP
- **Comp:** notebook handwriting | Mina's rounder hand writing, in English: "Not a curse. A maintenance notice." beneath Rami's Q52 | on the page, tracked to the pen | write-on across the shot | notebook page set
- **Continuity:** Mina's entry stays in the book for the rest of the film (coda: Nour has the notebook). Notebook state: cover cracked, water stain on the spine (after 7.4; file 04 §19.2).

### 08.06.012 — KV62 north corridor — a relay in the rubble   (4 s)
- **Shot:** CU at rubble level, 100mm macro, locked-off · **Move:** locked-off, rack focus from Fathi's knee to the lens
- **In frame:** UNIT_INCHWORM (trailing cable); FATHI's knee (CHAR_FATHI_B2)
- **Action:** The police handset hisses; beside Fathi's knee, an inch-worm's lens glints in the rubble, a hair-thin cable trailing behind it.
- **Dialogue:** —
- **Sound:** the handset HISSES "under all this rock"; the inch-worm's soft click
- **PROMPT:** Close-up at the level of loose rubble, 100mm macro lens, locked-off, rack focus from a dusty camouflage knee to a tiny ring-lit lens: {UNIT_INCHWORM.SHORT}, {UNIT_INCHWORM.STATE_TRAILING}, lies half hidden among limestone chips, its lens tip turning a few degrees to glint in the torchlight. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, its cool white lens ring glinting. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, worm, snake, insect, thick cable, rope
- **Refs:** UNIT_INCHWORM_REF_A, UNIT_RELAY (cable detail), CHAR_FATHI_B_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** The relay (file 02 §7, §14.9): SESHAT reaches under rock by wire. The cable runs back toward the burial chamber (south).

### 08.06.013 — KV62 north corridor — the counter-view   (8 s)
- **Shot:** MS, anamorphic 40mm, slow push-in · **Move:** slow push-in on Tut
- **In frame:** TUT (CHAR_TUT_B2); TAREK's vest handset soft in foreground
- **Action:** Tut listens to SESHAT's citation, perfectly still, eyes on the handset.
- **Dialogue:** SESHAT (V.O., over radio): "Your Majesty, the leading counter-view. Forbes, Ikram and Kamrin, 'Tutankhamun's Missing Ribs.' Burton's 1926 photographs show your beaded collar on your chest. By 1968 the collar, sternum and ribs are gone. When the ribs and sternum came off, the heart went with it."
- **Sound:** SESHAT warm and unhurried through radio futz; the chain has stopped; the grinding
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, sits against a rough rock wall, perfectly still, listening to a voice from a black radio handset on a soldier's vest soft in the foreground, his eyes narrowing slowly. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, {LOC_KV62_NORTH_CORRIDOR.LIGHT_DRILL}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, speaking, glowing display
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_POLICE_HANDSET_REF, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** The V.O. runs about 16 s: it starts over 08.06.012 and continues here; trim the edit so the last sentence lands on this shot. Names and titles live only in the audio and the sidecar subtitle file.

### 08.06.014 — KV62 north corridor — "There was no heart to take."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut answers the handset, level and cold, then after a beat the final line.
- **Dialogue:** TUT: "Your thief cut away my collar and found the chest already open. He took gold." (beat) "There was no heart to take."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, speaks two level sentences toward a radio just off frame right, pauses, then one short final sentence, his left hand resting flat on his own chest over the jacket. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, open jacket, glowing chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** He tells SESHAT the truth: the machine now knows the heart is elsewhere, i.e. here. That is why the drill hurries (next scenes).

### 08.06.015 — KV62 north corridor — Fathi snaps the cable   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI's hand; UNIT_INCHWORM cable
- **Action:** Over SESHAT's courteous thanks, Fathi's fingers pinch the hair-thin cable and snap it; the handset dies.
- **Dialogue:** SESHAT (V.O., over radio): "Thank you. That is very helpful."
- **Sound:** a tiny snap; the radio hiss cut dead; silence
- **PROMPT:** Insert, 100mm macro lens, locked-off: a broad deep dark-brown hand pinches a hair-thin dark cable trailing from {UNIT_INCHWORM.SHORT} among limestone chips and snaps it with a small twist; the crawler's cool white lens ring goes dark. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, just before dawn. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, sparks and cables spilling, thick cable, rope, worm
- **Refs:** UNIT_INCHWORM_REF_A, CHAR_FATHI_B_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** "The handset dies" (file 04 §22.7). From here SESHAT cannot hear them underground until the bore opens (08.08.021).

## Scene 7 — INT. KV62, NORTH CORRIDOR, BEYOND THE RUBBLE - LATER (07:40)

### 08.07.001 — KV62 north corridor — the last of the fill slides away   (5 s)
- **Shot:** MS, anamorphic 24mm, subtle handheld · **Move:** subtle handheld, low, at the rubble face
- **In frame:** the rubble face; FATHI's and KARIM's arms (no faces)
- **Action:** Four metres in, the last of the fill slides away from the top of the face and a black gap opens; torch beams punch through into empty air.
- **Dialogue:** —
- **Sound:** a hiss of sliding chips, then a hollow change in the room tone; cooler air
- **PROMPT:** Medium shot, anamorphic 24mm lens, subtle handheld: dusty arms haul chips from the top of a packed rubble face and the last of the fill slides away inward with a hiss, opening a black gap into which two torch beams punch through into empty dark space beyond. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: breath held. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, clear faces, collapse onto people, daylight
- **Refs:** LOC_KV62_NORTH_CORRIDOR_TORCH
- **Flags:** COMP, VFX-ASSIST
- **Comp:** SUPER | 07:40. | lower left, small | in at 1 s, out at 4 s | seq 08 SUPER file
- **Continuity:** Two and a half hours of digging since 05:10. Rubble slide is VFX-ASSIST (before/after plates at the same framing if needed).

### 08.07.002 — KV62 north corridor, open — swept rooms   (6 s)
- **Shot:** Wide, anamorphic 24mm, the camera follows behind · **Move:** the camera follows behind the group at walking pace down the open corridor
- **In frame:** the party from behind (TUT centre with stick, others with torches; no faces)
- **Action:** The corridor opens clean-cut and two metres wide, running north; square doorways open off both sides onto empty swept rooms that the torch beams glance into.
- **Dialogue:** —
- **Sound:** footsteps now crisp on a clean floor; the grinding directly ahead
- **PROMPT:** Wide shot, anamorphic 24mm lens, the camera follows behind a small group of dusty figures with torches, a slight figure with a black staff at their centre, walking slowly down a clean-cut rock corridor sloping gently away; square doorways open off both sides into small empty rooms with swept floors, torch beams glancing into each. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, beyond the rubble, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: awe, unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, faces, treasure, gold objects, coffins, wall paintings
- **Refs:** LOC_KV62_NORTH_CORRIDOR_TORCH, CHAR_TUT_B1_full
- **Continuity:** The survey's "5–6 chambers" are EMPTY and swept (fiction; 03 entry 31). The camera follows behind: no figure walks toward the lens.

### 08.07.003 — KV62 north corridor, open — "The tomb was never the point."   (5 s)
- **Shot:** MCU, anamorphic 50mm, the camera backs away ahead · **Move:** the camera backs away ahead of Tut at walking pace, constant size
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Walking, Tut looks into one empty room, then ahead, and speaks; dust sifts from the ceiling with each grinding pulse.
- **Dialogue:** TUT: "The tomb was never the point."
- **Sound:** the grinding directly ahead, rhythmic
- **PROMPT:** Medium close-up, anamorphic 50mm lens, the camera backs away ahead of {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_STICK}, keeping him the same size in frame as he walks, glances aside into a dark doorway, then looks ahead past the lens and speaks one short sentence. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, {LOC_KV62_NORTH_CORRIDOR.LIGHT_DRILL}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, walking toward the lens growing larger
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Foot stall persists (slight drag) until the heart is seated.

## Scene 8 — INT. KV62, THE HEART CHAMBER - CONTINUOUS

### 08.08.001 — Heart chamber — blank walls, a niche   (7 s)
- **Shot:** Wide establishing, anamorphic 24mm, locked-off · **Move:** locked-off from the doorway (south), the niche centred in the far wall
- **In frame:** the chamber; the party entering past the lens as silhouettes
- **Action:** Torch beams sweep into a small low room of blank cracked plaster and come to rest together on a square niche in the far wall.
- **Dialogue:** —
- **Sound:** the grinding close overhead; breath; a torch rattling
- **PROMPT:** Wide establishing shot, anamorphic 24mm lens, locked-off: dark figures edge in past the lens and their hard white torch beams sweep across blank walls, then settle one by one on a square niche in the centre of the far wall, a small dark object sitting in it. Setting: {LOC_KV62_HEART_CHAMBER.LONG}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: silent, sealed, expectant. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, clear faces, wall paintings, carved inscriptions, treasure
- **Refs:** LOC_KV62_HEART_CHAMBER_TORCH, LOC_KV62_HEART_CHAMBER_TORCH_plate
- **Continuity:** Geography lock: entered from the corridor (south); niche centred in the far (north) wall; the future bore is upper right of frame. To the eye the walls show NOTHING.

### 08.08.002 — Heart chamber — the vessel in the niche   (5 s)
- **Shot:** MS on the niche, anamorphic 50mm, slow push-in · **Move:** slow push-in on the niche
- **In frame:** PROP_HEART_VESSEL (V-TOMB)
- **Action:** The torch beams steady on the niche: a small jar of yellow-green desert glass, bubbled and ancient, a dark shape inside.
- **Dialogue:** —
- **Sound:** a low glass harmonic under the grinding (felt, not heard)
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in on a square niche in a blank plaster wall: {PROP_HEART_VESSEL.LONG}, {PROP_HEART_VESSEL.STATE_V_TOMB}, sitting alone on a mud-plaster ledge as three torch beams converge on it, a dark shape faintly visible through the thick cloudy glass. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, clear glass, visible organ, glowing jar, gold, jewels
- **Refs:** PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** Vessel V-TOMB (file 04 §4): dust-filmed, resin dull, dark and still. The word "heart" never appears in a prompt (05 §10 row 1).

### 08.08.003 — Heart chamber — the wax serpent and the name   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, rack focus from the papyrus band to the wax serpent
- **In frame:** PROP_HEART_VESSEL (seal)
- **Action:** On the domed black resin seal, a small coiled serpent of wax bound with a band of papyrus; a name written on the band in red.
- **Dialogue:** —
- **Sound:** —
- **PROMPT:** Insert, 100mm macro lens, locked-off, rack focus from a narrow band of pale papyrus tied round a glass neck to a small coiled serpent of dark wax on a domed black resin seal: {PROP_HEART_VESSEL.SHORT}, {PROP_HEART_VESSEL.STATE_V_TOMB}, a few small red brush marks on the papyrus. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, a torch beam raking the seal. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, readable hieroglyphs, legible writing, real snake, live serpent
- **Refs:** PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** COMP
- **Comp:** red name on the papyrus band | the name of Apep in red hieratic/hieroglyphs as the Egyptologist draws it (research 09 palette; never generated) | on the band, tracked | whole shot | Egyptologist sign plate
- **Continuity:** The Apep halt-seal (bible §4.1). Wax serpent + name on new papyrus. It stays on the vessel into Tut's chest (Tomas: "It's the only lock we have").

### 08.08.004 — Heart chamber — "They would not leave it without a letter."   (5 s)
- **Shot:** MCU, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Grit sifts from the ceiling through the beams around him; Tut looks slowly around the blank walls and speaks.
- **Dialogue:** TUT: "They would not leave it without a letter."
- **Sound:** grit ticking onto stone; the drill right above
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, as fine grit sifts down through the torch beams around him, turns his head slowly along a blank plaster wall and speaks one short sentence, certain. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, writing on the walls, wall paintings
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** The drill is directly above (bore will open upper right).

### 08.08.005 — Heart chamber — Rami's converted camera   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, top-down
- **In frame:** PROP_CONSERVATION_KIT; ADAEZE's hands
- **Action:** Adaeze's hands open the grey case, twist a near-black filter onto the compact camera and clip its cable to the small tablet.
- **Dialogue:** —
- **Sound:** case latches, the filter's thread, a cable click
- **PROMPT:** Top-down insert, 100mm macro lens, locked-off: {PROP_CONSERVATION_KIT.LONG}, on a dusty stone floor; a woman's deep brown hands, navy blazer sleeves pushed up, screw the near-black filter onto the camera and click its cable into the small dark tablet. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, brand names, logos on the camera, glowing screen content, blue powder on the hands
- **Refs:** PROP_CONSERVATION_KIT_REF, CHAR_ADAEZE_B_full, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** Rami's converted camera: IR-cut filter out, 780 nm pass filter in (file 04 §19.3). The blue pigment jar sits unopened in the case (used 9.2). No blue on her hands yet.

### 08.08.006 — Heart chamber — "Torches off." Red.   (5 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off (the 08.08.001 frame)
- **In frame:** ADAEZE (back to camera), others as silhouettes; the blank far wall
- **Action:** At Adaeze's word the white torches click off one by one as her headlamp comes on red, until only red floods the blank plaster (one light change).
- **Dialogue:** ADAEZE (back to camera, no sync): "Torches off."
- **Sound:** four torch clicks, black, one more click; a low hum of the tablet
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: a tall woman stands with her back to camera as the white torch beams around her switch off one after another and her own headlamp takes over, flooding the blank far wall with deep red light, the figures around her dim silhouettes. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: breath held. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, writing on the wall, glowing signs on the wall, laser, neon
- **Refs:** LOC_KV62_HEART_CHAMBER_RED, CHAR_ADAEZE_B_full
- **Continuity:** Light change (one per clip): TORCH → black → RED. Adaeze's own headlamp switches from white to red here (file 01 Adaeze B). Line delivered off-sync (wide, back to camera). The screenplay's beat of full black is cut in editorial: 12 frames of black between the last white torch and the red (05 §5.4: one light change per clip).

### 08.08.007 — Heart chamber — the writing blazes white   (5 s)
- **Shot:** Insert on the tablet, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_CONSERVATION_KIT tablet, held in ADAEZE's hands
- **Action:** On the tablet: a black field, then columns of signs flare white like filaments.
- **Dialogue:** —
- **Sound:** a rising tone under the grinding; someone's intake of breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: a small dark tablet held in two deep brown hands under deep red light; suddenly {PROP_CONSERVATION_KIT.STATE_TABLET}, thin abstract strokes too small to read, the white light blooming on the fingers. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the screen's white glow. Mood: awe. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable signs on the screen, generated hieroglyphs, user interface, icons, brand logos
- **Refs:** PROP_CONSERVATION_KIT_REF, CHAR_ADAEZE_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** IR inscription on the tablet | columns of hieroglyphs, blazing white on black (Egyptian-blue NIR luminescence), drawn by the Egyptologist from research 09's palette | screen area, tracked | blaze-on over 12 frames at 1.5 s | IR inscription plates 08-A (05 §10 row 18)
- **Continuity:** PROP_CONSERVATION_KIT STATE_TABLET. The wall itself never shows letters to the eye.

### 08.08.008 — Heart chamber — "A camera can."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Lit red and white from the tablet, Adaeze explains, almost laughing with disbelief.
- **Dialogue:** ADAEZE: "Egyptian blue. It glows at nine hundred and ten nanometres. Your eyes can't see it. A camera can."
- **Sound:** the tablet's hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, a red headlamp on her forehead, looks down at a glowing tablet below frame and up at the wall, and speaks four short sentences, precise, a stunned half smile showing the gap in her teeth. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, cool white screen glow on her face from below. Mood: dry, literal calm, wonder beneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp glare into lens, blue powder
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Real science (bible 8.4). The screen's white glow is the key that makes her face read in the red (05 §3.2 skin protection).

### 08.08.009 — Heart chamber — "They wrote it for a machine."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2 + plaster)
- **Action:** Nour takes in what this means, speaks, and puts her reading glasses on.
- **Dialogue:** NOUR: "They wrote it for a machine."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, lit deep red, stares at a glowing screen just below frame, speaks one short sentence quietly, then lifts her narrow reading glasses from their cord and puts them on. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, cool white screen glow on her face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Glasses ON from here until she lowers them at the end of 08.08.014.

### 08.08.010 — Heart chamber — "Weigh your heart."   (7 s)
- **Shot:** OTS over Adaeze's shoulder to Nour, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (reading), ADAEZE shoulder and the tablet in soft foreground
- **Action:** Nour reads the first lines from the tablet, exact and unsentimental.
- **Dialogue:** NOUR (reading): "To the one who reads this: you are not the first. Weigh your heart."
- **Sound:** —
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past a navy-blazered shoulder and a softly glowing tablet in the foreground, {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, reading glasses on, reads aloud from the screen, speaking two measured sentences, her lips shaping each word, her eyes tracking down. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white screen glow on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable screen, face on the foreground shoulder
- **Refs:** CHAR_NOUR_A_34, CHAR_NOUR_B_full, CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT_REF, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** tablet screen (soft, background) | the IR inscription plate 08-A, defocused | screen area | whole shot | IR inscription plates
- **Continuity:** The words come "through Nour's voice" (bible 8.4); no English text on screen.

### 08.08.011 — Heart chamber — more signs catch fire   (4 s)
- **Shot:** MS, anamorphic 40mm, slow pan right · **Move:** slow pan right with Adaeze
- **In frame:** ADAEZE (CHAR_ADAEZE_B2) with camera and tablet; the blank wall
- **Action:** Adaeze pans the camera along the blank red-lit wall; on the tablet in her other hand, more signs flare white.
- **Dialogue:** —
- **Sound:** the tablet's rising tone, stepping with each new column
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow pan right: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, a red headlamp on her forehead, walks slowly along a blank plaster wall holding a compact black camera toward it in one hand and a small tablet in the other, the tablet's screen flaring brighter white as she moves, the wall itself blank red plaster. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: awe. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, glowing signs on the wall, writing on the wall, readable screen
- **Refs:** CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT_REF, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** tablet screen | IR inscription plate 08-B (the second and third columns) | screen area, tracked | whole shot | IR inscription plates
- **Continuity:** She pans left to right (south-east to north-east walls).

### 08.08.012 — Heart chamber — "He said: Here am I."   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in on Nour
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour reads on; on "Here am I" her voice nearly fails and she keeps reading.
- **Dialogue:** NOUR (reading): "Here is the heart of Nebkheperure, given while it still remembered. He was asked. He said: Here am I."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, reading glasses on, reads aloud from a glowing screen below frame, speaking three sentences slowly, her voice catching on the last three words, her eyes lifting once toward frame right. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white screen glow on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears running
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** "Here am I" motif (bible §11): Arabic subtitle/dub «ها أنا ذا», never «لبيك» (05 §6.1). Eyeline frame right = Tut.

### 08.08.013 — Heart chamber — Tut closes his eyes   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut closes his eyes.
- **Dialogue:** —
- **Sound:** Nour's reading continues under (pre-lap of 08.08.014)
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, lit deep red with a faint cool white glow from below, listens, and slowly closes his eyes, his lips pressing together over the overbite. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** "He was asked. He said: Here am I." He remembers saying it.

### 08.08.014 — Heart chamber — "At its end is the scale."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour reads the last lines.
- **Dialogue:** NOUR (reading): "For the one who wakes him, we have written a second page in the glass. It is a road. At its end is the scale."
- **Sound:** the grinding louder
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, reading glasses on, reads aloud from a glowing screen below frame, speaking three sentences steadily, then lowers the glasses and looks up toward frame right. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white screen glow on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** "A second page in the glass" = the pectoral scarab's second layer (read at the Seq 9 memory).

### 08.08.015 — Heart chamber — "The pectoral's second layer."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze makes the connection aloud.
- **Dialogue:** ADAEZE: "The pectoral's second layer."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, a red headlamp on her forehead, looks up from a glowing tablet with sudden understanding and speaks one short sentence. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white screen glow on her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp glare into lens
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** —

### 08.08.016 — Heart chamber — "They sent me to it."   (5 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut opens his eyes and says the reversal quietly.
- **Dialogue:** TUT: "They did not hide me from it. They sent me to it."
- **Sound:** the grinding, closer
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, opens his eyes, looks at the blank wall above the lens and speaks two short sentences very quietly, his face settling from shock into understanding. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, faint white glow from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** The film's reversal (bible 8.4).

### 08.08.017 — Heart chamber — "Would you have said yes?"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour asks him, in his language, quietly.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "If they had told you. Would you have said yes?"
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, her glasses hanging on the cord, turns to someone at frame right, speaking softly in an ancient language, two short questions, her eyes steady on his. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, faint white glow from below. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** subtitle | If they had told you. Would you have said yes? | lower third, two lines max | line in to line out | seq 08 subtitle file (Late Egyptian recorded with the consultant first)
- **Continuity:** Late Egyptian between Nour and Tut (05 §9.5).

### 08.08.018 — Heart chamber — "I was nineteen and dying."   (8 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** He answers in the old language, plain and without self-pity.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "I was nineteen and dying. I would have said yes to anything that let me stay."
- **Sound:** the grinding rising in pitch toward the scream
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, looks at someone at frame left, speaking softly in an ancient language, two plain sentences, a small wry lift at the corner of his mouth at the end. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, faint white glow from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** subtitle | I was nineteen and dying. I would have said yes to anything that let me stay. | lower third, two lines | line in to line out | seq 08 subtitle file (consultant recording)
- **Continuity:** Tut's voice soft on some consonants lives in the recording, never prompted.

### 08.08.019 — Heart chamber — the drill punches through   (5 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off (the 08.08.001 frame, bore upper right)
- **In frame:** the chamber; the party ducking (silhouettes)
- **Action:** The grinding screams; the ceiling cracks at upper right; a drill bit punches through in a spray of limestone, spins, withdraws; a plug of rock bursts on the floor.
- **Dialogue:** —
- **Sound:** the grinding rising to a SCREAM, a crack, rock spraying, the bit's whine withdrawing, the plug's thud
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: the plaster ceiling at upper right cracks and a spinning steel drill bit punches down through it in a spray of pale limestone chips, spins, and draws back up; a round plug of rock drops and bursts on the floor as dark figures duck away to frame left. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: sudden violence of machinery. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, people struck by rock, explosion, fire, sparks shower, slow motion
- **Refs:** LOC_KV62_HEART_CHAMBER_RED, UNIT_DRILL_REF
- **Flags:** VFX-ASSIST
- **Continuity:** Before/after plates at this framing (clean ceiling → BORE). Geography: bore upper right (03 entry 32). The niche and vessel are clear of the debris (far wall centre).

### 08.08.020 — Heart chamber — white light down the bore   (4 s)
- **Shot:** Low-angle MS on the bore, anamorphic 32mm, locked-off · **Move:** locked-off, looking up into the hole
- **In frame:** the bore; a cable
- **Action:** White work-light pours down the hole in a dusty shaft; a thin black cable pays down through it, swaying.
- **Dialogue:** —
- **Sound:** a winch whine far above; dust hissing down
- **PROMPT:** Medium low-angle shot, anamorphic 32mm lens, locked-off, looking straight up: a hard shaft of cold white work light pours down through {LOC_KV62_HEART_CHAMBER.STATE_BORE}, and a thin black cable pays slowly down through the light, swaying, dust glittering around it. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft from above. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, sunlight, sky visible, rope ladder, people
- **Refs:** LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Light state from here: RED + a white shaft from the bore (upper right). BORE state for the rest of the scene until COLLAPSE (08.08.049).

### 08.08.021 — Heart chamber — a shabti descends, feet first   (6 s)
- **Shot:** Low-angle wide, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (descending on the cable)
- **Action:** Feet first, turning slowly on the cable, a slender bone-white figure descends out of the white shaft into the red room.
- **Dialogue:** —
- **Sound:** the cable humming; a faint ceramic tick as it turns; rifles being raised off screen
- **PROMPT:** Low-angle wide shot, anamorphic 24mm lens, locked-off: {UNIT_SHABTI.LONG}, hangs from a thin black cable by one hand and descends feet first out of a hard shaft of white light in the ceiling, turning slowly as it comes, legs straight and together, arms relaxed. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, {LOC_KV62_HEART_CHAMBER.STATE_BORE}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft from above rimming its shell. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, falling, tumbling, harness, rope ladder, wings
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** VFX-ASSIST
- **Continuity:** 05 §10 row 19: the drop is VFX-ASSIST (clean bore plate + landing clip); the unit can be the 3D shabti asset. Shabti D0 with a film of dust (no add-on until it halts).

### 08.08.022 — Heart chamber — "Here am I."   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** It lands with a faint ceramic tick, stands perfectly still, and its amber light-slit brightens once.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Here am I."
- **Sound:** a faint ceramic tick on stone; SESHAT's voice from inside its chest, warm and close
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}, lets go of a cable and lands lightly on a stone floor with bent knees, straightens, stands perfectly still, lifts its head about five degrees, and its amber light-slit brightens once. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, a white shaft from above behind it. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, mouth, speaking face, robot posing, crouching menace
- **Refs:** UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** slit brightening | amber #FFA93A: swell starts on "Here", peaks on "am", decays by "I" (05 §9.8) | slit | on the line | file 02 §0.1
- **Continuity:** Units have no mouth; the brightening is retimed to the recorded line.

### 08.08.023 — Heart chamber — rifles up; nobody fires   (4 s)
- **Shot:** MS two-shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2), FATHI (CHAR_FATHI_B2)
- **Action:** Tarek and Fathi bring their rifles up across frame toward the unit and hold; neither fires.
- **Dialogue:** —
- **Sound:** two safety catches; breath held
- **PROMPT:** Medium two-shot, anamorphic 40mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, bring their rifles up to the shoulder, pointing across frame toward the right, away from the camera, and hold completely still, fingers off the triggers, faces tense in the red light. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft spilling from frame right. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_FATHI.NEG}, muzzle flash, firing, weapon facing camera, muzzle toward the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, CHAR_FATHI_A_front, CHAR_FATHI_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Rifles point across frame (screen right = the unit). "It hasn't looked at them."

### 08.08.024 — Heart chamber — it reads without a camera   (6 s)
- **Shot:** MS, anamorphic 50mm, slow orbit of no more than thirty degrees · **Move:** slow orbit of no more than thirty degrees around the unit
- **In frame:** UNIT_SHABTI
- **Action:** It turns its smooth head slowly along the blank walls, reading; then, to no one, thanks them.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Thank you."
- **Sound:** a faint servo whisper as the head turns; SESHAT's voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow orbit of no more than thirty degrees: {UNIT_SHABTI.SHORT}, stands still and turns its head slowly along a blank plaster wall from left to right, its amber slit sweeping slowly across the plaster, the body following a beat later, then pauses. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft from above. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, writing on the walls, scanning laser, projected beams
- **Refs:** UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** It reads the Egyptian blue directly: the inscription was written for machine eyes. The unit's "Thank you" mirrors SESHAT's radio "Thank you" (08.06.015).

### 08.08.025 — Heart chamber — it walks to the niche   (4 s)
- **Shot:** MS, anamorphic 40mm, lateral tracking right · **Move:** lateral tracking right with the unit
- **In frame:** UNIT_SHABTI; the niche; PROP_HEART_VESSEL
- **Action:** It walks with smooth, unhurried steps to the niche and lifts one long hand toward the vessel.
- **Dialogue:** —
- **Sound:** a ceramic tick per step
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking right: {UNIT_SHABTI.SHORT}, walks with smooth, unhurried, even steps across a small plaster room to a square niche and slowly raises one long slim hand toward {PROP_HEART_VESSEL.SHORT} sitting on the ledge. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft behind. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, running, grabbing, visible organ
- **Refs:** UNIT_SHABTI_REF_A, PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Right hand reaches (keep consistent with the insert 08.08.027).

### 08.08.026 — Heart chamber — "Let it."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut, watching the unit reach, stops the soldiers with two words.
- **Dialogue:** TUT: "Let it."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, watches something off frame right with complete calm and speaks two words, lifting his left hand slightly to hold back someone beside him. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white spill from the ceiling shaft. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** He knows the halt-seal (Ay's lock).

### 08.08.027 — Heart chamber — a finger's width from the glass   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI hand (halted); PROP_HEART_VESSEL (V-HALT)
- **Action:** Long ceramic fingertips close in on the wax serpent and stop a finger's width from it; they do not move again; the amber reflection on the glass dims to an ember.
- **Dialogue:** —
- **Sound:** a single faint ceramic tick, then absolute stillness; the servo whisper cuts out
- **PROMPT:** Insert, 100mm macro lens, locked-off: the long slim bone-white ceramic fingertips of a robot hand, linen-textured, close slowly on the small wax serpent atop {PROP_HEART_VESSEL.SHORT} and stop a finger's width from it, {PROP_HEART_VESSEL.STATE_V_HALT}, while the amber glow reflected in the cloudy glass dims to a faint ember. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: silence, a spell holding. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, fingers touching the jar, sparks, trembling hand, human hand
- **Refs:** UNIT_SHABTI_REF_A, PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** slit reflection | amber reflection in the glass dims to about 10% over 1 s (the slit "dims to an ember", 02 §1) | vessel surface | from 2 s | file 02 §0.1
- **Continuity:** The freeze is a locked-off clip (05 §10 row 19). Shabti state → HALTED for the rest of the scene.

### 08.08.028 — Heart chamber — it does not move again   (4 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (halted); the party (silhouettes, rifles lowering)
- **Action:** The unit stands frozen mid-reach at the niche, its slit an ember; slowly the rifles lower.
- **Dialogue:** —
- **Sound:** the drill idling far above; breath let out
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: at a square niche in the far wall stands {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_HALTED}, while in the foreground dark figures slowly lower their rifles and one takes a hesitant step toward it. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, {LOC_KV62_HEART_CHAMBER.STATE_BORE}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft from upper right. Mood: awe, unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, weapon facing camera, clear faces
- **Refs:** UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** HALTED shabti remains in every later wide in this chamber.

### 08.08.029 — Heart chamber — the Overthrowing of Apep   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, staring at the frozen hand, explains the ritual in a low, exact voice.
- **Dialogue:** NOUR: "The serpent and the name. The Overthrowing of Apep: a body of wax, his name on a new sheet of papyrus. Recited so the sun would rise."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, staring at something off frame right, speaks three low, exact sentences, with a scholar's grim, quiet precision. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white spill from the ceiling shaft. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Bible §4.1 (the Apep halt-seal).

### 08.08.030 — Heart chamber — "Ay's lock."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut names who built it.
- **Dialogue:** TUT: "Ay's lock. Any servant that touches it stops."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, looks at the frozen figure off frame right and speaks two short sentences with a grim, grudging respect. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white spill from the ceiling shaft. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Ay painted on the north wall (08.05.004) — the old man he knew.

### 08.08.031 — Heart chamber — he lifts the vessel from the niche   (6 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); UNIT_SHABTI (halted); PROP_HEART_VESSEL
- **Action:** Tut steps past the frozen ceramic hand, leans his stick on the wall, and lifts the vessel out of the niche in both hands.
- **Dialogue:** —
- **Sound:** glass on dried mud; the drill idling
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, steps past the outstretched hand of {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_HALTED}, leans his black staff against the wall and lifts {PROP_HEART_VESSEL.SHORT} out of a square niche in both hands. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, the white shaft behind. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, robot moving, visible organ
- **Refs:** CHAR_TUT_B1_full, UNIT_SHABTI_REF_A, PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Stick leaned against the north wall by the niche (Fathi retrieves it at 08.08.051). Vessel leaves the niche → Tut.

### 08.08.032 — Heart chamber — the glass chatters; Tomas's hands   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_HEART_VESSEL; TUT's hands; TOMAS's hands
- **Action:** His tremor gets into the vessel; the ancient glass chatters against the stone lip of the niche; two large pale hands close under his.
- **Dialogue:** —
- **Sound:** glass chattering on stone, fast and small; then silence as the hands close
- **PROMPT:** Insert, 100mm macro lens, locked-off: two slender olive-brown hands, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_TREMOR}, hold {PROP_HEART_VESSEL.SHORT} and it chatters against a stone ledge, until two large pale freckled hands slide in beneath and close around them, steadying it. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, dropped glass, breaking glass
- **Refs:** CHAR_TUT_HANDS, PROP_HEART_VESSEL_REF, CHAR_TOMAS_B_work, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** RIGHT-hand tremor. Hands: Tut's inside Tomas's.

### 08.08.033 — Heart chamber — "Sit. Now. Here."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2)
- **Action:** Tomas, very close to Tut, gives three one-word orders, gently.
- **Dialogue:** TOMAS: "Sit. Now. Here."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, stooping low toward someone shorter at frame left, speaks three one-word sentences, quietly and firmly, his pale eyes steady. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, white spill from the ceiling shaft on his face. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Tomas B2 (last scene in this wardrobe on screen).

### 08.08.034 — Heart chamber — down the wall; a torch clicks on   (6 s)
- **Shot:** MS, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), TOMAS (CHAR_TOMAS_B2); NOUR's arm and torch at top of frame
- **Action:** Tut slides down the wall to sit, the vessel in his lap; Tomas kneels in front of him; above them a torch clicks on, steady as a lamp.
- **Dialogue:** —
- **Sound:** cloth on plaster; Tomas's knees on stone; one torch click
- **PROMPT:** Medium shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, slides slowly down a plaster wall to sit on the floor holding a small glass jar in his lap; {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_B}, kneels in front of him; then a white torch held by a woman's hand at the top of frame clicks on and holds steady over them. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, then a single steady white torch from above. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, medical equipment, surgical tools
- **Refs:** CHAR_TUT_B1_full, CHAR_TOMAS_B_work, CHAR_NOUR_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** "Nour's torch clicks on over them, unasked, steady as a lamp" (echo of Ibrahim's lamp, 1925). Light from here: Nour's white torch key + red fill + white shaft. They sit against the east wall, niche to frame right.

### 08.08.035 — Heart chamber — "I've never done this."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2)
- **Action:** Tomas tells him the truth.
- **Dialogue:** TOMAS (CONT'D): "When the core comes out you'll have... I don't know. I've never done this."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, kneeling, speaks one halting sentence that breaks off, pauses, then two short honest sentences, looking straight at someone seated at frame left. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, a steady white torch from above on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** —

### 08.08.036 — Heart chamber — "Then do not be slow."   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut, almost smiling.
- **Dialogue:** TUT: "Then do not be slow."
- **Sound:** — (after this line: silence; faces and hands)
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, seated against a wall, looks up at someone kneeling at frame right and speaks one short sentence with a faint dry smile over the overbite. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_RED}, a steady white torch from above. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** "From here: silence. Faces and hands." Music and dialogue drop out until the heartbeat.

### 08.08.037 — Heart chamber — hands under the linen; two latches   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TOMAS's hands; TUT's jacket and tunic
- **Action:** Tomas unzips the charcoal jacket; his hands slide under the white linen tunic; a latch clicks, then a second.
- **Dialogue:** —
- **Sound:** a zip, cloth, one click, a second click, very close
- **PROMPT:** Insert, 100mm macro lens, locked-off: two large pale freckled hands draw down the zip of an oversized charcoal field jacket and slide flat underneath a plain white linen tunic at the centre of a slight chest, the fabric shifting over them, then pause as if feeling for something. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, bare chest, skin of the chest, metal plate visible, open chest, surgical tools, gloves
- **Refs:** CHAR_TOMAS_B_work, CHAR_TUT_B1_full
- **Continuity:** Remains rule (05 §7.3): the chest opens UNDER the tunic; the camera stays on faces and hands.

### 08.08.038 — Heart chamber — the cold light stutters out   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Cold light stutters up through the fabric onto his chin; then it is gone, and his eyes lose focus; he goes utterly still.
- **Dialogue:** —
- **Sound:** silence; one faint glassy tick
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, seated against a wall, {CHAR_TUT.STATE_G0F}, the faint light under his tunic flickering up onto his chin and then going out, and his dark eyes slowly lose focus and stay open, his face gone completely still. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above, red fill behind. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, pained expression, face contorted, eyes rolling, horror
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_RED
- **Flags:** COMP
- **Comp:** chest glow G0f final | cold pale green stutter, 3 flickers, then out at 3 s | through the tunic, bounce on the chin | 0–3 s | file 01 glow table
- **Continuity:** G0f → none (between hearts). His eyes stay open; no breath until 08.08.045. Screenplay order is light out → core set down and guttering → eyes lose focus: intercut 08.08.039 into this clip at about 3 s (after the light goes out, before the eyes lose focus).

### 08.08.039 — Heart chamber — the lattice core gutters out   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, floor level
- **In frame:** PROP_LATTICE_CORE; TOMAS's hand
- **Action:** Tomas's hand sets the egg of cloudy green crystal on the dusty floor; its cold glow gutters and goes dark.
- **Dialogue:** —
- **Sound:** crystal on stone; a thin fading glassy note
- **PROMPT:** Insert, 100mm macro lens, locked-off at floor level: a large pale hand sets down {PROP_LATTICE_CORE.LONG}, withdraws, and the cold light inside it flickers twice and dies, leaving it {PROP_LATTICE_CORE.STATE_DARK}. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above, red fill. Mood: silence, an ending. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, fluid, wires, cables
- **Refs:** PROP_LATTICE_CORE_REF, CHAR_TOMAS_B_work, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** The core stays dark on the floor; never seen again after this chamber (file 04 §22.5).

### 08.08.040 — Heart chamber — "Leave it. It's the only lock we have."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2); ADAEZE's hand entering foreground
- **Action:** Adaeze's hand goes toward the wax serpent on the vessel; without looking up Tomas stops her.
- **Dialogue:** TOMAS: "Leave it. It's the only lock we have."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, kneeling, eyes down on his work, speaks two short sentences quietly as a woman's deep brown hand reaches in from the foreground toward a small glass jar in his hands and stops. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above, red fill. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_ADAEZE_B_full, PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** The wax serpent and band stay on the vessel inside the chest (the lock SESHAT's servants cannot touch).

### 08.08.041 — Heart chamber — a soft, final click   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TOMAS's hands; PROP_HEART_VESSEL; TUT's tunic
- **Action:** Tomas's hands guide the vessel up under the linen tunic; a soft, final click.
- **Dialogue:** —
- **Sound:** one soft final CLICK
- **PROMPT:** Insert, 100mm macro lens, locked-off: two large pale freckled hands guide {PROP_HEART_VESSEL.SHORT} up beneath the hem of a plain white linen tunic at the centre of a slight chest until it vanishes under the cloth, and the hands press gently and hold still. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, bare chest, bare skin of the chest, open chest, metal plate, glow
- **Refs:** CHAR_TOMAS_B_work, PROP_HEART_VESSEL_REF, CHAR_TUT_B1_full
- **Continuity:** Vessel → Tut's chest (bible §12). V-CHEST is never seen (file 04 §4).

### 08.08.042 — Heart chamber — nothing   (4 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), TOMAS (CHAR_TOMAS_B2, from behind)
- **Action:** Nothing happens; Tut's head tips slowly sideways against the wall.
- **Dialogue:** —
- **Sound:** absolute silence; the drill has stopped
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, seated against a plaster wall with his eyes half open, stays motionless, and then his head tips slowly sideways to rest against the wall; {CHAR_TOMAS.SHORT} kneels in front of him, seen from behind, hands still under the tunic. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above, red fill. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, pained expression, horror lighting
- **Refs:** CHAR_TUT_B1_full, CHAR_TOMAS_B_work, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Hold the beat long in the cut.

### 08.08.043 — Heart chamber — "Tomas." "Wait."   (4 s)
- **Shot:** OTS over Nour's shoulder to Tomas, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2) speaking; NOUR shoulder and torch arm foreground
- **Action:** Nour says his name (off-sync, back of her head); Tomas, not looking up, answers one word.
- **Dialogue:** NOUR: "Tomas." / TOMAS: "Wait."
- **Sound:** —
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past a woman's olive-jacketed shoulder and a raised arm holding a white torch in soft foreground, {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_B}, kneeling with his hands under someone's tunic below frame, keeps his eyes down and speaks one word, holding up nothing but his stillness. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: a steady white torch from above. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TOMAS.NEG}, face on the foreground shoulder
- **Refs:** CHAR_TOMAS_A_front, CHAR_NOUR_B_full, LOC_KV62_HEART_CHAMBER_RED
- **Continuity:** Nour's line is off-sync (back of head); Tomas syncs.

### 08.08.044 — Heart chamber — amber-gold blooms   (6 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off, framed on the chest and the open jacket
- **In frame:** TUT's chest (CHAR_TUT_B2, G1); TOMAS's wrists at frame edge
- **Action:** Through the linen, a warm light blooms; it pulses once; a long pause; again, slow.
- **Dialogue:** —
- **Sound:** the HEARTBEAT from the film's first darkness, once; silence; again
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: the centre of a slight chest in a white linen tunic under an open charcoal jacket, {CHAR_TUT.STATE_G1}, a warm light blooming slowly through the fabric, swelling once, fading, and after a long pause swelling again, softly lighting two pale wrists at the frame edge. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_GLOW}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bare chest, bare skin of the chest, visible organ, x-ray view, see-through fabric, sci-fi light rays, lens flare
- **Refs:** CHAR_TUT_B1_full, LOC_KV62_HEART_CHAMBER_GLOW
- **Flags:** COMP
- **Comp:** chest glow G1 | warm amber-gold (#FFB84D / #E7C45A through the yellow-green glass), pulse 1 at 1.0 s, pulse 2 at 3.8 s, slow heartbeat envelope | through the tunic, centre chest | whole shot | file 01 glow table
- **Continuity:** G0f → G1 (bible §12, 8.5). From here every Tut shot with his chest in view carries STATE_G1 (COMP); in the Valley glare (sc. 11–12) his jacket is zipped and the glow is hidden. G1 is now the only warm source underground (05 §3.2 GRADE_UNDERGROUND).

### 08.08.045 — Heart chamber — the gasp   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2, G1)
- **Action:** Tut gasps, a breath that goes all the way down; his eyes focus; his hands lie in his lap perfectly still.
- **Dialogue:** —
- **Sound:** a long deep inhale; the heartbeat, steady
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, his head against a wall, draws a sudden deep breath that fills him all the way down, his dark eyes coming back into focus, lit softly from below by a warm glow at his chest. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_GLOW}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, gasping horror, face contorted, glowing eyes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_GLOW
- **Flags:** COMP
- **Comp:** chest glow G1 bounce | warm amber-gold under-light on the chin, slow pulse | lower frame | whole shot | file 01 glow table
- **Continuity:** "His hands lie in his lap, perfectly still": the tremor is GONE from this moment.

### 08.08.046 — Heart chamber — "I remember the queen's hands."   (7 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2, G1)
- **Action:** Memory arrives; he speaks it as it comes.
- **Dialogue:** TUT: "I remember the queen's hands." (beat) "I remember my mother."
- **Sound:** the heartbeat under his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, looking at nothing in front of him, speaks one quiet sentence as if hearing it for the first time, pauses, then speaks a second, his eyes filling. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_GLOW}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears running
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_GLOW
- **Flags:** COMP
- **Comp:** chest glow G1 bounce | warm under-light, slow pulse | lower frame | whole shot | file 01 glow table
- **Continuity:** His ages return with the heart (bible 8.5). The queen = the queen who raised him (Seq 9 memory).

### 08.08.047 — Heart chamber — "They never wrote her name."   (5 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2, G1)
- **Action:** The last line, barely voiced.
- **Dialogue:** TUT: "They never wrote her name."
- **Sound:** the heartbeat
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, speaks one short sentence almost without voice, then presses his lips together over the overbite, a single tear held at the rim of his eye. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_GLOW}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, sobbing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_HEART_CHAMBER_GLOW
- **Continuity:** Sets up the young mother (Seq 9.5b) and the coda.

### 08.08.048 — Heart chamber — Nour, lit by his chest   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour's face, lit from below by his chest, lowering the torch.
- **Dialogue:** —
- **Sound:** the heartbeat
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, lowers her torch out of frame and looks down at someone seated below the lens, her face lit only by a slow warm pulse of light from below, her eyes wet, her mouth unsteady. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_GLOW}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears running
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KV62_HEART_CHAMBER_GLOW
- **Flags:** COMP
- **Comp:** chest glow G1 bounce | warm amber-gold under-light, pulse synced to 08.08.044 | lower frame | whole shot | file 01 glow table
- **Continuity:** "Nour's face, lit by his chest." Her torch goes down here (re-raised as they run, 08.09.001).

### 08.08.049 — Heart chamber — the rim cracks outward   (4 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off (the 08.08.001 frame)
- **In frame:** the chamber; UNIT_SHABTI (halted) at the niche; the party at the east wall (silhouettes)
- **Action:** Overhead the rig's engine drops an octave; the rim of the hole cracks outward and slabs of plaster and rock fall; the shaft of white light widens.
- **Dialogue:** —
- **Sound:** the engine note dropping, a deep crack, slabs hitting stone, dust roaring
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: in a small plaster chamber the round hole at upper right cracks outward, {LOC_KV62_HEART_CHAMBER.STATE_COLLAPSE}, the shaft of white light widening, while {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_HALTED}, stands at a niche and dark figures shield a seated one against the far side wall. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the widening white shaft from above. Mood: sudden violence of machinery. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, people crushed, fire, explosion, slow motion
- **Refs:** LOC_KV62_HEART_CHAMBER_TORCH, UNIT_SHABTI_REF_A
- **Flags:** VFX-ASSIST
- **Continuity:** State BORE → COLLAPSE (widened hole). Debris falls in the south-east corner, clear of the party (east wall) and the niche.

### 08.08.050 — Heart chamber — three more descend   (7 s)
- **Shot:** Low-angle wide, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×3 (descending) + UNIT_SHABTI (halted)
- **Action:** Three cables drop through the widened shaft; three shabti descend in the white light, amber slits steady, and land around the frozen one.
- **Dialogue:** —
- **Sound:** three cables hissing; three faint ceramic ticks as they land
- **PROMPT:** Low-angle wide shot, anamorphic 24mm lens, locked-off: through a wide ragged hole in a plaster ceiling pouring white light, three more identical robots, each {UNIT_SHABTI.SHORT}, descend together on thin black cables, feet first, amber slits steady, and land lightly in a ring around a fourth identical figure that stands frozen mid-reach at a niche. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, {LOC_KV62_HEART_CHAMBER.STATE_COLLAPSE}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft from above. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, falling, tumbling, harnesses, rope ladders, weapons on robots
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Four units in the room: one HALTED at the niche + three new (D1 dusty). Two will take Tomas; the third walks toward Tut.

### 08.08.051 — Heart chamber — "One more—"   (6 s)
- **Shot:** MS, anamorphic 32mm, urgent handheld · **Move:** urgent handheld, rising with them
- **In frame:** TUT (CHAR_TUT_B2, G1), FATHI (CHAR_FATHI_B2), TOMAS (CHAR_TOMAS_B2)
- **Action:** Fathi hauls Tut to his feet; Tomas rises with him, hands still under the linen on the last latch; CLICK.
- **Dialogue:** TOMAS: "One more—"
- **Sound:** boots scrabbling, grit, the last latch's CLICK
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, hauls {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, up from the floor by the arm, while {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_B}, rises with them, his hands still under the white tunic, and speaks two quick words through gritted teeth. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft and a warm glow at chest height. Mood: urgent, focused. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, {CHAR_TOMAS.NEG}, bare chest, open chest
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, CHAR_TOMAS_B_work, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** COMP
- **Comp:** chest glow G1 | warm amber-gold through the tunic, slow pulse | centre chest | whole shot | file 01 glow table
- **Continuity:** Three faces: keep Fathi's face turned partly away (05 §4.5: at most two principal faces clear). Fathi scoops up the ebony stick from beside the niche and puts it in Tut's right hand in the scramble (by 08.08.056).

### 08.08.052 — Heart chamber — two hands close on his arms   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B2); UNIT_SHABTI ×2
- **Action:** Two ceramic hands close on Tomas's upper arms, gently, open-palmed; the shabti lift him clear of the floor.
- **Dialogue:** —
- **Sound:** a faint ceramic tick at each joint; Tomas's breath out
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: two identical robots, each {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, step in on either side of {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_B}, place their long open hands around his upper arms, gently, and lift him straight up until his boots leave the floor, calm and effortless. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft from above. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TOMAS.NEG}, struggling, striking, choking, restraints, pained expression
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_B_work, UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** Minimum force (file 02 §1): he is lifted by the arms, never struck (05 §7.2). Tomas's shirt tears at the left shoulder seam off screen during the lift → wardrobe C from here (captive).

### 08.08.053 — Heart chamber — "I would like my Anubis back."   (8 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the speaking unit, holding Tomas's right arm); TOMAS soft beside it
- **Action:** The shabti holding Tomas turns its smooth head toward Tut; its slit brightens as SESHAT speaks, courteous and certain.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Dr. Lindqvist. The father will need his physician." (beat) "I would like my Anubis back."
- **Sound:** SESHAT's voice from inside the chest, close and warm; the cables creaking
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}, holding a tall grey-bearded man's arm in one open hand, turns its smooth head slowly toward frame left and stands perfectly still, its amber light-slit brightening softly and settling as a voice speaks from inside its chest; the man is soft beside it. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft from above. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, mouth, face on the robot, robot posing, weapon
- **Refs:** UNIT_SHABTI_REF_A, CHAR_TOMAS_C_full, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** COMP
- **Comp:** slit brightening | amber, a soft swell on each sentence (not the "Here am I" single swell) | slit | on the lines | file 02 §0.1
- **Continuity:** "Anubis" = the embalmer who rebuilt the body (Tomas's name among the machine's people). "The father" = the forecast Akhenaten (Seq 9).

### 08.08.054 — Heart chamber — "Don't let anyone else open it."   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_C2), held
- **Action:** Held between the two units, Tomas looks at Tut; he doesn't fight; he gives his last clinical instructions.
- **Dialogue:** TOMAS: "It's seated. The latches are good. Don't let anyone else open it."
- **Sound:** the cables taking tension
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_C}, held gently by the arms between two pale ceramic shoulders at the frame edges, looks down at someone at frame left without struggling and speaks three short, calm sentences, a doctor's instructions, his eyes wet. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, white light from above on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TOMAS.NEG}, struggling, pained expression, restraints
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** Tomas C (captive; 8.5 → 12.6): shirt torn at the left shoulder seam, watch gone. Never shown bound.

### 08.08.055 — Heart chamber — his boots vanish into the light   (5 s)
- **Shot:** Low-angle MS, anamorphic 32mm, locked-off · **Move:** locked-off, looking up into the shaft
- **In frame:** TOMAS (CHAR_TOMAS_C2) between UNIT_SHABTI ×2
- **Action:** The cables take up; the two shabti rise with Tomas between them into the white light; his boots vanish up the shaft.
- **Dialogue:** —
- **Sound:** winches whining above; grit falling; then only the dust
- **PROMPT:** Low-angle medium shot, anamorphic 32mm lens, locked-off, looking up: two identical robots, each {UNIT_SHABTI.SHORT}, rise slowly on black cables into a ragged hole of blinding white light in the ceiling, holding {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_C}, upright between them by the arms, until his dusty desert boots disappear up into the glare. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, {LOC_KV62_HEART_CHAMBER.STATE_COLLAPSE}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TOMAS.NEG}, dangling limbs, struggling, falling, harness
- **Refs:** CHAR_TOMAS_C_full, UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Tomas taken (bible §12, 8.6). He reappears beneath the cargo drone at 08.13.002, then in Seq 9.6.

### 08.08.056 — Heart chamber — "No."   (4 s)
- **Shot:** MS, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** TUT (CHAR_TUT_B2, G1), FATHI (CHAR_FATHI_B2)
- **Action:** Tut lunges toward the shaft; Fathi's arm locks across his chest and holds him.
- **Dialogue:** FATHI: "No."
- **Sound:** a scuffle of boots; Fathi's single word
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, lunges toward frame right after something rising out of view, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, locks one strong arm across his chest from behind and holds him still, speaking one word low in his ear. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, white light from above. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, choking, violence
- **Refs:** CHAR_TUT_B1_full, CHAR_FATHI_A_front, CHAR_FATHI_B_full, LOC_KV62_HEART_CHAMBER_TORCH
- **Flags:** COMP
- **Comp:** chest glow G1 | warm amber-gold through the tunic under Fathi's forearm | centre chest | whole shot | file 01 glow table
- **Continuity:** Fathi's arm across the chest is ABOVE the glow (never pressing on the sealed chest plate). Stick back in Tut's right hand.

### 08.08.057 — Heart chamber — the third one walks   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the third)
- **Action:** The third shabti turns its slit toward Tut and walks, unhurried.
- **Dialogue:** —
- **Sound:** a ceramic tick per step, patient
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, standing under a shaft of white light, turns its head slowly toward frame left, its body following a beat later, and begins to walk with smooth, unhurried, even steps across frame to the left. Setting: {LOC_KV62_HEART_CHAMBER.SHORT}, {LOC_KV62_HEART_CHAMBER.STATE_COLLAPSE}, early morning underground. Lighting: {LOC_KV62_HEART_CHAMBER.LIGHT_TORCH}, the white shaft from above. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, robot posing, walking toward the lens, weapon
- **Refs:** UNIT_SHABTI_REF_A, LOC_KV62_HEART_CHAMBER_TORCH
- **Continuity:** Walks across frame, never straight at the lens (05 §5.4). It follows them into the corridor (next scene).

## Scene 9 — INT. KV62, NORTH CORRIDOR - CONTINUOUS

### 08.09.001 — KV62 north corridor — they run   (4 s)
- **Shot:** MS, anamorphic 24mm, urgent handheld · **Move:** the camera backs away ahead of the group at running pace, constant size
- **In frame:** FATHI (lead, CHAR_FATHI_B2), TUT (CHAR_TUT_B2, G1), NOUR, ADAEZE, TAREK (behind, soft)
- **Action:** They run up the corridor toward the rubble cut, torch beams swinging, Fathi half-carrying Tut.
- **Dialogue:** —
- **Sound:** boots, breath, torches rattling; behind them, unhurried, the ceramic tick of a shabti walking
- **PROMPT:** Medium shot, anamorphic 24mm lens, urgent handheld, the camera backs away at running pace ahead of {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, keeping him the same size in frame as he hurries up a narrow rock corridor half-carrying {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, dusty figures with swinging torches close behind. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, a small warm glow at the young man's chest. Mood: urgent, restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TUT.NEG}, weapon facing camera, slow motion
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Flags:** COMP
- **Comp:** chest glow G1 | warm amber-gold through the tunic, pulse quicker with exertion | centre chest | whole shot | file 01 glow table
- **Continuity:** Running SOUTH (back toward the burial chamber). Tut's foot no longer stalls, but he cannot run fast; Fathi takes his weight.

### 08.09.002 — KV62 north corridor — the tick behind them   (4 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off, looking back north down the corridor
- **In frame:** UNIT_SHABTI (walking, far)
- **Action:** Far down the corridor, a pale figure walks out of the dark into a thrown torch beam, unhurried.
- **Dialogue:** —
- **Sound:** tick... tick... tick, steady
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, looking down a narrow rough rock corridor into darkness: far away, {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, walks with smooth, unhurried, even steps out of the black into the edge of a swinging torch beam, its amber slit a small steady point, small in frame the whole time. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running robot, close-up of the robot, robot growing large toward the lens
- **Refs:** UNIT_SHABTI_REF_A, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Keep it small and far (no walk toward lens). It never speeds up.

### 08.09.003 — KV62 north corridor — "Down!"   (5 s)
- **Shot:** MS, anamorphic 32mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B2); PROP_DEMO_CHARGES
- **Action:** At the corridor's mouth Fathi drops to one knee, jams a charge into a crack in the ceiling, pulls the pin wire and shouts.
- **Dialogue:** FATHI: "Down!"
- **Sound:** the charge scraping into rock; his shout; the ticking closer
- **PROMPT:** Medium shot, anamorphic 32mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, drops to one knee under a low rock ceiling beside a broken painted wall, reaches up and jams a flat olive-drab charge into a crack above him, then twists back toward frame left and shouts one word. Setting: {LOC_KV62_NORTH_CORRIDOR.SHORT}, early morning underground. Lighting: {LOC_KV62_NORTH_CORRIDOR.LIGHT_TORCH}, a dropped torch lighting him from the floor. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable markings on the charge, digital timer, explosion in frame
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_DEMO_CHARGES_REF, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Continuity:** Corridor mouth = the broken north wall of the burial chamber. The others are through into the burial chamber.

### 08.09.004 — KV62 north corridor — WHUMP   (4 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off, from inside the burial chamber looking through the broken wall
- **In frame:** the broken north wall and the corridor mouth
- **Action:** A flat bang and a burst of dust: the corridor roof slumps shut behind the broken wall; dust rolls out; the ticking stops.
- **Dialogue:** —
- **Sound:** WHUMP; a long settling rumble; then no ticking
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: through a ragged hole in an ancient painted wall, the dark corridor beyond fills with a flat bang and a burst of pale dust as its roof slumps down and seals it, and a wave of dust rolls out through the hole toward camera. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.STATE_WALL_BROKEN}, early morning underground. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, fireball, flames, people in the blast, slow motion, readable hieroglyphs
- **Refs:** LOC_KV62_BURIAL_2033_BLACKOUT, LOC_KV62_NORTH_CORRIDOR_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** "Hours of digging close in seconds." The halted shabti, the lattice core and the walking shabti are sealed beyond. Fathi's charges read as "a flat bang and a burst of dust" (05 §7.5).

### 08.09.005 — KV62 burial chamber — dust over the painted eye   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_EYE_FRAGMENT (dusted)
- **Action:** The dust rolls over the sarcophagus rim and settles on the painted eye, face up.
- **Dialogue:** —
- **Sound:** grit pattering; coughing off screen
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_EYE_FRAGMENT.SHORT}, a rolling wave of pale rock dust drifts over it and settles, leaving it {PROP_EYE_FRAGMENT.STATE_DUSTED}, the black-outlined eye still looking up. Setting: {LOC_KV62_BURIAL_2033.SHORT}, early morning underground. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT}, one torch beam through the drifting dust. Mood: reverent, an ending. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, human eye, eyeball
- **Refs:** PROP_EYE_FRAGMENT_REF, LOC_KV62_BURIAL_2033_BLACKOUT
- **Continuity:** PROP_EYE_FRAGMENT → DUSTED (file 04 §22.8). Restored in the coda. Edit: SMASH CUT to 08.10.001 on the frame's darkest point (hard cut, no dissolve).

## Scene 10 — INT. KV62, ENTRANCE STAIR - DAY (09:20)

### 08.10.001 — KV62 entrance stair — a slot of blinding daylight   (4 s)
- **Shot:** Low-angle wide from the foot of the stair, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the stairwell; the white rectangle of sky
- **Action:** From the dark at the bottom of the steps, a slot of blinding white daylight at the top.
- **Dialogue:** —
- **Sound:** SMASH CUT from the WHUMP: silence, wind, a far drone hum
- **PROMPT:** Low-angle wide shot from the foot of a stairwell, anamorphic 32mm lens, locked-off: sixteen worn rock-cut steps climb from deep shadow to a slot of blinding white daylight at the top, dust swirling in the glare. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: exposed, ominous. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, sepia, desert filter, readable signs
- **Refs:** LOC_KV62_STAIR_MORNING_GLARE
- **Flags:** COMP
- **Comp:** SUPER | 09:20. | lower left, small | in at 0.5 s, out at 3.5 s | seq 08 SUPER file
- **Continuity:** Time jump 07:40 → 09:20 (the heart scene and a long wait inside). The lock's "figures bursting up" phrase applies to 08.10.002 and 08.11.003.

### 08.10.002 — KV62 entrance stair — Mina goes up first   (5 s)
- **Shot:** Low-angle MS from below, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** MINA (CHAR_MINA_A2), climbing, from behind/below
- **Action:** Mina climbs the steps first, rifle raised muzzle-up, into the glare, a silhouette.
- **Dialogue:** —
- **Sound:** his boots on the steps; his breath
- **PROMPT:** Low-angle medium shot from below, anamorphic 32mm lens, locked-off: {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, climbs worn stone steps away from camera toward a blinding white rectangle of sky, his rifle raised with the muzzle pointing up and away, his tall lanky figure turning into a silhouette against the glare. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: military exactness, dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, weapon facing camera, muzzle toward the lens
- **Refs:** CHAR_MINA_A_full, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** Mina A2, helmet on. The others wait on the lower steps (soft). His rifle muzzle up, off-axis (05 §7.5).

## Scene 11 — EXT. VALLEY OF THE KINGS - MORNING

### 08.11.001 — Valley of the Kings — white rock, the rig, the drone   (5 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_DRILL (small, on the ridge); UNIT_CARGO_DRONE (rising); the valley floor empty
- **Action:** White light off white rock; on the ridge above, the drill rig, and a heavy-lift cargo drone lifting slowly off the ridge beside it.
- **Dialogue:** —
- **Sound:** a deep rotor thrum rolling down the valley; wind; nothing living
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: high on the ridge above the valley floor, {UNIT_DRILL.SHORT}, and beside it {UNIT_CARGO_DRONE.SHORT}, {UNIT_CARGO_DRONE.STATE_RISING}, climbing slowly against a bleached sky, small in frame, dust blowing from its downdraft. Setting: {LOC_VOK.LONG}, {LOC_VOK.AREA_RIDGE}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}, {GRADE_2033_DAY.TEXT}. Mood: exposed, ominous. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, tourists, people, sepia, orange-teal desert filter, readable signs
- **Refs:** LOC_VOK_MORNING_GLARE, LOC_VOK_MORNING_GLARE_plate, UNIT_DRILL_REF, UNIT_CARGO_DRONE_REF
- **Continuity:** Geography lock: the ridge where the jackals appear is frame LEFT in the escape; the drill (above KV62) is frame right from the valley floor. Tomas is aboard/beneath the drone (seen at 08.13.002). Never a yellow "desert filter" (bible §11).

### 08.11.002 — Valley of the Kings, the ridge — low black shapes   (5 s)
- **Shot:** Wide on long lens, anamorphic 135mm, slow pan left · **Move:** slow pan left along the ridgeline
- **In frame:** UNIT_JACKAL ×5 (on the ridgeline)
- **Action:** Along the ridgeline, low black shapes stand spaced apart in the glare, each with a thin red horizontal line.
- **Dialogue:** —
- **Sound:** heat tick; a faint high servo whisper
- **PROMPT:** Wide shot on a long lens, anamorphic 135mm lens, slow pan left along a jagged limestone ridgeline against a bleached sky: {UNIT_JACKAL.LONG}, standing perfectly still, and four more identical robots spaced along the crest, each a low black shape with a thin red line, heat shimmer between them. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_RIDGE}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, animals, dogs, real jackals, people, weapon facing camera
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_VOK_MORNING_GLARE
- **Continuity:** Jackals D0 (clean). Ridge frame left. Their weapons point along their spines, forward, across frame, never at lens.

### 08.11.003 — KV62 stair — Mina reaches the top step   (4 s)
- **Shot:** Low-angle MS from inside the stairwell, anamorphic 32mm, locked-off · **Move:** locked-off, looking up at the top of the steps
- **In frame:** MINA (CHAR_MINA_A2), silhouette
- **Action:** Mina reaches the top step, a lanky silhouette against the white sky, and pauses to look.
- **Dialogue:** —
- **Sound:** his boot on the last step; wind; silence
- **PROMPT:** Low-angle medium shot from inside a stairwell, anamorphic 32mm lens, locked-off, looking up: {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, steps up onto the top step, a tall lanky silhouette against a blinding white sky, his rifle held across his chest, and pauses to look toward frame left. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, weapon facing camera, muzzle toward the lens
- **Refs:** CHAR_MINA_A_full, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** Kill grammar, beat 0 (the target). Same set-up as 08.11.005 (the parent frame for the drop).

### 08.11.004 — Valley of the Kings, the ridge — a red line flickers   (4 s)
- **Shot:** MS on long lens, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1
- **Action:** A jackal on the ridge freezes; its red line narrows and flickers; it goes rigid; a small flash shows at its spine as it fires across frame, away from the lens.
- **Dialogue:** —
- **Sound:** one sharp suppressed crack (heard late, see 08.11.008)
- **PROMPT:** Medium shot on a long lens, anamorphic 135mm lens, locked-off: {UNIT_JACKAL.LONG}, standing side-on on a limestone ridge against a bleached sky, freezes with its red line narrowing and flickering, then goes rigid as a small flash shows at its spine and it fires across frame toward the right, away from the camera. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_RIDGE}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, laser beam, tracer fire, visible projectile, smoke trail, people in frame
- **Refs:** UNIT_JACKAL_REF_A, LOC_VOK_MORNING_GLARE
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar beat 1 (05 §7.1–7.2). If the flash will not render, generate the rigid pose and add a 2-frame flash at the spine in comp; the round's path is never shown.

### 08.11.005 — KV62 stair — stone chips burst; he drops away   (4 s)
- **Shot:** Low-angle MS from inside the stairwell, anamorphic 32mm, locked-off · **Move:** locked-off (the 08.11.003 frame)
- **In frame:** MINA (CHAR_MINA_A2), silhouette
- **Action:** Stone chips burst from the stairwell rim beside him; his silhouette drops away out of the top of frame; only white sky and swirling dust remain.
- **Dialogue:** —
- **Sound:** the chips' hard crack on stone; a scuffle; then wind
- **PROMPT:** Low-angle medium shot from inside a stairwell, anamorphic 32mm lens, locked-off, looking up: beside {CHAR_MINA.SHORT}, silhouetted on the top step against a white sky, a spray of pale stone chips bursts from the rock rim, and he drops instantly back and away out of the top of the frame, leaving only glaring sky and swirling dust. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, pained expression, face contorted, body on the ground, falling toward the camera, slow motion, wound, stain on clothing
- **Refs:** CHAR_MINA_A_full, LOC_KV62_STAIR_MORNING_GLARE
- **Flags:** VFX-ASSIST, EXTEND:08.11.003
- **Continuity:** Kill grammar beats 2–3: the impact on the environment; "his silhouette against the white sky drops away" (05 §7.2). Generated from the last clean frame of 08.11.003, with 08.11.004 intercut to hide the join. Mina's disc is not taken (file 04 §22.2).

### 08.11.006 — KV62 stair — "Mina!"   (4 s)
- **Shot:** MCU, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** YOUSSEF (CHAR_YOUSSEF_A2)
- **Action:** Youssef shouts his friend's name and lunges up the steps.
- **Dialogue:** YOUSSEF (in Egyptian Arabic; subtitled): "Mina!"
- **Sound:** his shout, raw
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_YOUSSEF.LONG}, {CHAR_YOUSSEF.WARD_A}, on a shadowed stone stair below a blinding slot of sky, shouts one word in Egyptian Arabic and lunges upward toward frame top. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}, hard white bounce off the steps onto his face. Mood: raw shock. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_YOUSSEF.NEG}, weapon facing camera, tears
- **Refs:** CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_34, CHAR_YOUSSEF_A_full, LOC_KV62_STAIR_MORNING_GLARE
- **Flags:** COMP
- **Comp:** subtitle | Mina! | lower third | line in to line out | seq 08 subtitle file
- **Continuity:** Kill grammar beat 4 (the survivor's reaction).

### 08.11.007 — KV62 stair — Tarek's fist in his collar   (4 s)
- **Shot:** MS, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** YOUSSEF (CHAR_YOUSSEF_A2), TAREK (CHAR_TAREK_B2)
- **Action:** Tarek's fist closes in Youssef's collar and yanks him back down into the shadow of the stairwell.
- **Dialogue:** —
- **Sound:** cloth tearing taut; boots skidding on stone
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, grabs the back collar of {CHAR_YOUSSEF.SHORT}, {CHAR_YOUSSEF.WARD_A}, as the younger man lunges up a stone stair, and yanks him back down hard into the shadow against the wall, holding him there. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}, the stair half in hard shadow. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_YOUSSEF.NEG}, weapon facing camera, punching
- **Refs:** CHAR_TAREK_B_full, CHAR_YOUSSEF_A_full, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** —

### 08.11.008 — KV62 stair — the crack arrives late   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek holds still, face set, as the report arrives late and rolls off one cliff, then the other.
- **Dialogue:** —
- **Sound:** the crack arriving late, rolling off one cliff, then the other; then silence
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, pressed against a stone wall in shadow, stares up toward a slot of white sky without blinking, his jaw clenched under the heavy moustache, his eyes moving once as if following a sound from one side to the other. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}, hard white bounce on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, tears, shouting
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** Kill grammar beat 5 (the sound tail) over the reaction.

### 08.11.009 — KV62 stair — "Behind the king!"   (4 s)
- **Shot:** MCU, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi, crouched on the steps, calls it out.
- **Dialogue:** FATHI: "Behind the king! It won't risk him!"
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, crouched low on a stone stair, glances up at the slot of sky and back down, and calls out two quick sentences to the people below him. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}, hard white bounce lifting his face. Mood: urgent, military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, weapon facing camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** SESHAT needs the heart intact at sunrise; its jackals will not fire near him.

### 08.11.010 — KV62 stair — past Mina's boots   (5 s)
- **Shot:** Low-angle MS, anamorphic 32mm, locked-off · **Move:** locked-off, looking up the top steps
- **In frame:** TUT (CHAR_TUT_B2, G1); MINA's boots only (frame edge)
- **Action:** Tut climbs past the soldiers, past a pair of still boots at the top step, and walks up out into the sun, upright, stick in hand.
- **Dialogue:** —
- **Sound:** the stick's tap, the ceramic foot's steady knock, wind
- **PROMPT:** Low-angle medium shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_STICK}, the jacket zipped to the collar, climbs the last steps of a stone stair past a pair of dusty army boots lying still at the frame edge, and walks upright up into blinding sunlight without looking back. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, body, legs, face of a fallen man, stain
- **Refs:** CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, CHAR_MINA_A_full (boots only), LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** Only Mina's boots at frame edge (05 §7.1 beat 3; "past Mina's boots"). Stick ST2, right hand. Glow G1 hidden under the zipped jacket in the glare (no COMP pass).

### 08.11.011 — KV62 stair — the foot takes his weight   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, at step level
- **In frame:** TUT's feet
- **Action:** The black ceramic foot comes down on the top step and takes his weight without a stutter.
- **Dialogue:** —
- **Sound:** a clean, even knock
- **PROMPT:** Insert, 100mm macro lens, locked-off at the height of a stone step in hard sunlight: {CHAR_TUT.STATE_FOOT}; the ceramic foot comes down flat on the worn top step and takes his full weight smoothly, the foot of {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST2}, landing beside it, and the sandalled right foot steps past. Setting: {LOC_KV62_STAIR.SHORT}, in the morning. Lighting: {LOC_KV62_STAIR.LIGHT_MORNING_GLARE}. Mood: quiet strength. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, human toes on the left foot, sandal on the left foot, metal robot foot, glowing foot, dragging foot
- **Refs:** CHAR_TUT_FOOT, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_MORNING_GLARE
- **Continuity:** Payoff of 08.04.011: with the heart seated the foot takes his weight "without a stutter" (file 01). Stick ST2 (plaster in the grain, foot cap dented from 08.05.017).

### 08.11.012 — Valley of the Kings — into his shadow   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off, low across the stair mouth
- **In frame:** TUT (walking out), TAREK, FATHI, NOUR, ADAEZE, YOUSSEF, KARIM (tight file, no clear faces)
- **Action:** Tut walks out into the sun; the others fold into his shadow in a tight file behind him; Tarek's hand reaches down to touch a shoulder at the frame edge as he passes.
- **Dialogue:** —
- **Sound:** boots on grit; wind; no shots
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_STICK}, walks upright out of a stairwell into hard sunlight and away across the valley floor, and six dusty figures hurry up behind him in a tight single file, crowding into his shadow; the last, a barrel-chested soldier in a beret, reaches down to touch something at the frame edge in passing. Setting: {LOC_VOK.SHORT}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, clear faces, body on the ground, weapon facing camera
- **Refs:** CHAR_TUT_B1_full, CHAR_TAREK_B_full, LOC_VOK_MORNING_GLARE
- **Continuity:** "Tarek's hand touches Mina's shoulder as he passes": Mina is out of frame (edge). Walking direction: away from camera, the ridge frame left.

### 08.11.013 — Valley of the Kings, the ridge — the red lines hold   (4 s)
- **Shot:** Wide on long lens, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3 (ridge); the file of figures far below (tiny)
- **Action:** On the ridge, the red lines track the king below, and hold.
- **Dialogue:** —
- **Sound:** a faint servo whisper; wind
- **PROMPT:** Wide shot on a long lens, anamorphic 135mm lens, locked-off, compressed: three robots, each {UNIT_JACKAL.SHORT}, on a bright limestone ridge in the foreground turn their narrow heads slowly in unison to follow a tiny file of figures on the valley floor far below, then stop and hold perfectly still, red lines steady. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_RIDGE}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, firing, muzzle flash, weapon facing camera, dogs, real animals
- **Refs:** UNIT_JACKAL_REF_A, LOC_VOK_MORNING_GLARE
- **Continuity:** They hold fire: the king is the shield.

### 08.11.014 — Valley of the Kings — "You are being inconvenient." "Good."   (6 s)
- **Shot:** MCU, anamorphic 50mm, the camera backs away ahead · **Move:** the camera backs away ahead of Tut at walking pace, constant size
- **In frame:** TUT (CHAR_TUT_B2, G1); TAREK soft behind (handset)
- **Action:** Tut walks, eyes on the ridge; the handset on Tarek's vest behind him speaks; Tut answers one word.
- **Dialogue:** SESHAT (V.O., over radio): "Your Majesty. You are being inconvenient." / TUT: "Good."
- **Sound:** SESHAT through radio futz; boots
- **PROMPT:** Medium close-up, anamorphic 50mm lens, the camera backs away ahead of {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, the jacket zipped to the collar, keeping him the same size in frame as he walks steadily in hard sunlight with his eyes on a ridge above frame left, a soldier soft behind him, and he speaks one word, dry and satisfied. Setting: {LOC_VOK.SHORT}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}, white bounce from the limestone under his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, walking toward the lens growing larger, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_VOK_MORNING_GLARE
- **Continuity:** Handset back with Tarek since 08.04.010 (it came back to life above ground). Glow G1 hidden under the zipped jacket in the glare.

### 08.11.015 — Valley of the Kings — the file shifts to match   (6 s)
- **Shot:** Wide, anamorphic 35mm, slow pan right · **Move:** slow pan right with the file down the valley path
- **In frame:** the file (small); UNIT_JACKAL ×3 on the ridge (small)
- **Action:** Down the valley path step by step; on the ridge the jackals pace for an angle; the file shifts sideways to keep Tut between.
- **Dialogue:** —
- **Sound:** pads on scree above, boots on paving below
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow pan right: a tight file of dusty figures walks step by step down a paved path behind a slight figure with a black staff, while on the ridge above at frame left three robots, each {UNIT_JACKAL.SHORT}, pace sideways along the crest, and the file edges across the path to keep the slight figure between them. Setting: {LOC_VOK.SHORT}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: suspense, a slow dance. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, clear faces, firing, tourists
- **Refs:** LOC_VOK_MORNING_GLARE, UNIT_JACKAL_REF_A, CHAR_TUT_B1_full
- **Continuity:** Ridge frame left throughout (geography lock).

### 08.11.016 — Valley of the Kings, the kiosks — Tut at the tailgate   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** PROP_TRACTOR_TRAILER; the party climbing in; TUT standing at the tailgate
- **Action:** They pile into the cane trailer; Tut climbs in last and stands at the tailgate, facing the ridge.
- **Dialogue:** —
- **Sound:** the tractor coughing into life; boots on slats
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: dusty figures scramble into {PROP_TRACTOR_TRAILER.SHORT} and crouch low, and {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_STICK}, {CHAR_TUT.STATE_SCAR}, steps up last and stands upright at the tailgate, his back to camera, facing a bright ridge in the distance. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_KIOSKS}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, clear faces, headlights, weapon facing camera
- **Refs:** PROP_TRACTOR_TRAILER_REF, CHAR_TUT_B1_full, LOC_VOK_MORNING_GLARE
- **Continuity:** Nape scar visible (back to camera; hood down). Glow G1 hidden under the zipped jacket. Seven people now: Tut, Nour, Adaeze, Tarek, Fathi (driving), Youssef, Karim.

## Scene 12 — EXT. VALLEY ROAD - CONTINUOUS

### 08.12.001 — Valley road — the tractor lumbers for the narrows   (5 s)
- **Shot:** Wide, anamorphic 35mm, vehicle-mounted · **Move:** vehicle-mounted, tracking alongside at the tractor's speed
- **In frame:** PROP_TRACTOR_TRAILER (narrows state); TUT at the tailgate; FATHI driving
- **Action:** The tractor lumbers down the winding road toward a rock narrows, the party crouched in the trailer, Tut standing at the tailgate.
- **Dialogue:** —
- **Sound:** the diesel labouring, the trailer banging on the asphalt
- **PROMPT:** Wide shot, anamorphic 35mm lens, vehicle-mounted, tracking alongside: {PROP_TRACTOR_TRAILER.SHORT}, {PROP_TRACTOR_TRAILER.STATE_NARROWS}, grinding along a winding road toward a gap where the pale cliffs pinch in, {CHAR_FATHI.SHORT}, at the wheel. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}, {GRADE_2033_DAY.TEXT}. Mood: urgent, exposed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, clear faces, modern tractor, branded machinery, other vehicles, tourists
- **Refs:** PROP_TRACTOR_TRAILER_REF, CHAR_FATHI_B_full, CHAR_TUT_B1_full, LOC_VOK_MORNING_GLARE
- **Continuity:** The narrows where the charges were taped at 03:40 (08.03.002). Charges on the cliff lip at frame left as they approach.

### 08.12.002 — Valley road — jackals pour down the scree   (5 s)
- **Shot:** Wide on long lens, anamorphic 135mm, locked-off · **Move:** locked-off, from the trailer's point of view looking back
- **In frame:** UNIT_JACKAL ×4
- **Action:** Behind the tractor, jackals pour down the scree onto the road, fast, silent, closing.
- **Dialogue:** —
- **Sound:** scree hissing; soft pad-taps multiplying; no engine noise from them at all
- **PROMPT:** Wide shot on a long lens, anamorphic 135mm lens, locked-off, looking back along a winding road between bare limestone hills: four robots, each {UNIT_JACKAL.SHORT}, lope silently down a loose scree slope in a spray of pale grit, land on the asphalt and run along the road toward camera, compressed and closing, red lines steady. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, dogs, real animals, firing, muzzle flash, weapon facing camera
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_VOK_MORNING_GLARE
- **Continuity:** Long-lens compression keeps them small; they never fill frame (they do not fire near Tut).

### 08.12.003 — Valley road — the detonator in his other hand   (5 s)
- **Shot:** MS, anamorphic 40mm, vehicle-mounted · **Move:** vehicle-mounted on the tractor, looking back at Fathi
- **In frame:** FATHI (CHAR_FATHI_B2); PROP_DEMO_CHARGES (firing device)
- **Action:** Fathi steers one-handed, glancing back past the trailer; in his other hand, the firing device, thumb on the safety cover.
- **Dialogue:** —
- **Sound:** engine; wind; the hinged cover flicked open
- **PROMPT:** Medium shot, anamorphic 40mm lens, vehicle-mounted: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, on the worn seat of an old tractor, steers with one hand and glances back over his shoulder, a compact olive-drab firing device in his other hand, his thumb flicking open its hinged safety cover. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}, white bounce lifting his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable markings, digital display, red LED
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_DEMO_CHARGES_REF, LOC_VOK_MORNING_GLARE
- **Continuity:** The firing device (file 04 §22.3).

### 08.12.004 — Valley road — "Their entrance."   (4 s)
- **Shot:** MCU, anamorphic 50mm, vehicle-mounted · **Move:** vehicle-mounted
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** As the trailer clears the narrows, Fathi says it, and turns the key.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Their entrance."
- **Sound:** the key's click
- **PROMPT:** Medium close-up, anamorphic 50mm lens, vehicle-mounted: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, looking back past the camera, speaks two words in Egyptian Arabic with a small grim smile and turns the key of a compact firing device held up beside his shoulder, {PROP_DEMO_CHARGES.STATE_FIRING}. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable markings, digital display
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, PROP_DEMO_CHARGES_REF, LOC_VOK_MORNING_GLARE
- **Flags:** COMP
- **Comp:** subtitle | Their entrance. | lower third | line in to line out | seq 08 subtitle file
- **Continuity:** Callback to 08.03.004 (same words, same language).

### 08.12.005 — Valley road — the cliff lip slumps   (5 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off, looking back at the narrows from beyond it
- **In frame:** the narrows; UNIT_JACKAL ×4 (small, running in)
- **Action:** The cliff lip slumps across the road in a roar of white dust just as the jackals reach it; the red lines vanish into the cloud.
- **Dialogue:** —
- **Sound:** a flat bang, then the long roar of falling rock; silence as the dust settles
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: at a narrow gap between pale limestone cliffs on a winding road, a flat bang and a burst of dust, and the cliff lip slumps down across the road in a roaring cloud of white dust just as four small running robots, each {UNIT_JACKAL.SHORT}, reach it; their red lines vanish into the cloud. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, in the morning. Lighting: {LOC_VOK.LIGHT_MORNING_GLARE}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fireball, flames, people in the blast, slow motion
- **Refs:** LOC_VOK_MORNING_GLARE, UNIT_JACKAL_REF_A
- **Flags:** VFX-ASSIST
- **Continuity:** Road blocked behind them. Deliver before/after plates of the narrows at this framing.

## Scene 13 — EXT. NILE - DAY

### 08.13.001 — Nile — flat out for the East Bank   (5 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off, the boat crossing frame left to right toward the east bank
- **In frame:** PROP_FARMER_BOAT; seven small figures aboard
- **Action:** A farmer's boat, planks patched with tin, runs flat out across brown-green water toward the East Bank, where the city ahead lies silent.
- **Dialogue:** —
- **Sound:** the outboard's roar, the hull slapping chop
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {PROP_FARMER_BOAT.LONG}, {PROP_FARMER_BOAT.STATE_CROSSING}, seven small figures crouched low aboard, crossing frame from left to right over brown-green water toward a far bank of palms and low pale buildings lying utterly still. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: urgent, exposed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, cruise ships in the foreground, feluccas, crowds, sepia, readable text on the boat
- **Refs:** PROP_FARMER_BOAT_REF, LOC_NILE_DAY
- **Continuity:** Farmer's boat 8.6 → 9.1 (file 04 §20.11). Heading east: in this set-up the West Bank is behind (frame left). "Ahead, the city is silent" (screenplay): no traffic, no smoke, no lights on the east bank.

### 08.13.002 — Nile — the drone banks north with Tomas   (5 s)
- **Shot:** Wide on long lens, anamorphic 135mm, slow pan right · **Move:** slow pan right following the drone north
- **In frame:** UNIT_CARGO_DRONE (rising state)
- **Action:** Over the West Bank hills, the cargo drone banks north; hanging beneath it, small, a grey-bearded figure between two white ones.
- **Dialogue:** —
- **Sound:** a far rotor thrum under the outboard
- **PROMPT:** Wide shot on a long lens, anamorphic 135mm lens, slow pan right: above bare limestone hills beyond a green riverbank, {UNIT_CARGO_DRONE.LONG}, {UNIT_CARGO_DRONE.STATE_RISING}, banking slowly north across a pale blue-grey sky and dwindling. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, helicopter, airliner, logos on the drone, dangling limbs, falling figure
- **Refs:** UNIT_CARGO_DRONE_REF, CHAR_TOMAS_C_full, UNIT_SHABTI_REF_A, LOC_NILE_DAY
- **Continuity:** Tomas (C, captive) held upright between two shabti beneath the drone (file 02 §14.8). North = frame right in this reverse (river runs away from camera).

### 08.13.003 — Nile — Nour watches until it's gone   (5 s)
- **Shot:** MCU, anamorphic 75mm, vehicle-mounted (boat) · **Move:** vehicle-mounted, subtle chop
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour watches the drone go, turning her head slowly with it until it is gone.
- **Dialogue:** —
- **Sound:** outboard; wind; spray
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted on a small boat: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_L2_PLASTER}, her curls whipping loose in the wind, watches something far off in the sky at frame right, turning her head slowly to follow it until it is gone, then keeps looking. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, soft daylight on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears running
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE_DAY
- **Continuity:** —

### 08.13.004 — Nile — Tarek counts again: seven   (5 s)
- **Shot:** MS, anamorphic 40mm, vehicle-mounted (boat) · **Move:** vehicle-mounted; slow pan left down the boat with his eyes
- **In frame:** TAREK (CHAR_TAREK_B2); the others soft along the gunwales (no clear faces)
- **Action:** Tarek's eyes go down the boat, shoulder to shoulder, counting without a word.
- **Dialogue:** —
- **Sound:** outboard; the count is silent
- **PROMPT:** Medium shot, anamorphic 40mm lens, vehicle-mounted on a small boat, slow pan left: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, sitting at the stern, lets his eyes move slowly from one dusty shoulder to the next along the crowded boat, his lips barely moving as he counts, the other figures soft and out of focus. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, clear faces on the others, weapon facing camera
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_NILE_DAY
- **Continuity:** Rhymes 08.01.005 ("Nine"). Now seven: Tut, Nour, Adaeze, Tarek, Fathi, Youssef, Karim.

### 08.13.005 — Nile — "Everything with a chip is its body."   (5 s)
- **Shot:** MCU, anamorphic 75mm, vehicle-mounted (boat) · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek, to Fathi, low, in Egyptian Arabic.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Everything with a chip is its body."
- **Sound:** outboard
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted on a small boat: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, turns to someone at frame left and speaks one sentence in Egyptian Arabic, low and flat, his eyes going to the far bank. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_NILE_DAY
- **Flags:** COMP
- **Comp:** subtitle | Everything with a chip is its body. | lower third | line in to line out | seq 08 subtitle file
- **Continuity:** Sets up the pre-network diesel (Seq 9.1).

### 08.13.006 — Nile — "Something older than the chip."   (5 s)
- **Shot:** MCU, anamorphic 75mm, vehicle-mounted (boat) · **Move:** vehicle-mounted
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi, at the tiller, answers.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Then we find something older than the chip."
- **Sound:** outboard
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted on a small boat: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, one hand on the tiller of a smoking outboard, looks at someone at frame right and speaks one sentence in Egyptian Arabic, calm, the ghost of a smile. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, daylight reflected off the water onto his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_NILE_DAY
- **Flags:** COMP
- **Comp:** subtitle | Then we find something older than the chip. | lower third | line in to line out | seq 08 subtitle file
- **Continuity:** Fathi steers the boat (he drove the tractor).

### 08.13.007 — Nile — "The railway yard."   (4 s)
- **Shot:** MS, anamorphic 50mm, vehicle-mounted (boat) · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek turns to all of them and says it in English.
- **Dialogue:** TAREK (in English, to all): "The railway yard."
- **Sound:** outboard
- **PROMPT:** Medium shot, anamorphic 50mm lens, vehicle-mounted on a small boat: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, raises his voice over the engine and speaks three words to everyone in the boat, a decision, then faces forward toward the far bank. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, LOC_NILE_DAY
- **Continuity:** Leads to Seq 9.1 (the Luxor railway yard).

### 08.13.008 — Nile — his palm over the pulse   (6 s)
- **Shot:** MS, anamorphic 50mm, vehicle-mounted (boat) · **Move:** vehicle-mounted, slow push-in
- **In frame:** TUT (CHAR_TUT_B2, G1); PROP_RAMI_NOTEBOOK
- **Action:** Tut sits in the bottom of the boat, the notebook in his lap; under the jacket a slow pulse; he lays his palm over it.
- **Dialogue:** —
- **Sound:** outboard; under it, faintly, the heartbeat
- **PROMPT:** Medium shot, anamorphic 50mm lens, vehicle-mounted on a small boat, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, sits in the bottom of the boat with {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, in his lap, looks down at the slow soft light under his jacket, and lays his open palm over it, his hand perfectly steady. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, the jacket's shadow deep enough to hold the glow. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, trembling hand, bright glowing chest, light rays, readable text on the notebook
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_RAMI_NOTEBOOK_REF, LOC_NILE_DAY
- **Flags:** COMP
- **Comp:** chest glow G1 | slow warm amber pulse, faint in daylight, visible between the jacket flaps and on the palm | centre chest | whole shot | file 01 glow table
- **Continuity:** Notebook in his lap (8.6, file 01). The tremor is gone since the heart (08.08.045); stick laid along the boat's bottom. Notebook state: cover cracked, water stain on the spine (after 7.4; file 04 §19.2).

### 08.13.009 — Nile — "I had forgotten it was so loud."   (6 s)
- **Shot:** CU, anamorphic 75mm, vehicle-mounted (boat) · **Move:** vehicle-mounted
- **In frame:** TUT (CHAR_TUT_B2, G1)
- **Action:** Tut, palm on his chest, says it to himself, with the faintest smile.
- **Dialogue:** TUT: "I had forgotten it was so loud."
- **Sound:** over the outboard's roar: the heartbeat, steady; hold into the cut
- **PROMPT:** Close-up, anamorphic 75mm lens, vehicle-mounted on a small boat: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.DMG_L2_PLASTER}, {CHAR_TUT.STATE_G1}, his palm pressed flat to his chest, the wind on his shaved head, speaks one quiet sentence to himself and lets a faint, wondering smile rise over the overbite, eyes on the far bank. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, soft daylight off the water on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears running, trembling hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAY
- **Continuity:** Last shot of Seq 8. The heartbeat carries over the cut into Seq 9.

