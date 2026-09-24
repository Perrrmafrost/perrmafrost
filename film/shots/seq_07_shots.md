# SEQUENCE 7 — KARNAK · shot list and paste-ready prompts

**HERE AM I** · screenplay `screenplay/seq_07.fountain` (pp. 51–63, 13 pages) · 5 Nov 21:00 → 6 Nov 03:00, Luxor dark · photoreal live-action AI video, 1920×1080, 16:9, 24 fps · written in the token grammar of `production_bible/05_style_and_prompt_grammar.md` and expanded by `shots_md2jsonl.py` against `production_bible/locks.json` (every `{TOKEN.FIELD}` pastes the bible's exact wording; every PROMPT ends with `{SUFFIX}`, every NEGATIVE starts with `{NEG}`).

**Shots:** 164 · **Running time:** 898 s ≈ **15.0 min** (target 13 min ±20%: 10.4–15.6) · **Average shot:** 5.5 s · **Flags:** COMP ×35, VFX-ASSIST ×21, VFX-EXTEND ×13, EXTEND ×1 (07.09.005 ← 07.09.003, with 07.09.004 intercut).

## Scene list

| # | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 07.01 | EXT. NILE, NORTH OF LUXOR - NIGHT | 07.01.001–015 | 15 | 90 s |
| 07.02 | EXT. KARNAK, AVENUE OF RAMS - NIGHT | 07.02.001–007 | 7 | 40 s |
| 07.03 | INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT (the loom) | 07.03.001–018 | 18 | 98 s |
| 07.04 | INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS | 07.04.001–008 | 8 | 50 s |
| 07.05 | EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT | 07.05.001–014 | 14 | 82 s |
| 07.06 | EXT. KARNAK, BLOCK FIELD - CONTINUOUS (the heist) | 07.06.001–026 | 26 | 134 s |
| 07.07 | EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS | 07.07.001–008 | 8 | 42 s |
| 07.08 | INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS (the midpoint, 01:00) | 07.08.001–027 | 27 | 144 s |
| 07.09 | EXT. KARNAK, RIVER LANDING - NIGHT (Rami; the block into the river) | 07.09.001–028 | 28 | 143 s |
| 07.10 | EXT. NILE, LUXOR - NIGHT (the felucca, 03:00) | 07.10.001–013 | 13 | 75 s |

## Sequence-wide decisions (read before generating)

- **Look codes.** On the launch (07.01) and at the ram avenue (07.02) the party is at damage L1 (river); **L2 sandstone dust applies from the Hypostyle (07.03) on** (file 01 state table: Seq 7 = B2). Tut: `CHAR_TUT_B1` → `CHAR_TUT_B2`, glow G0f (COMP), nape scar, foot stall, right-hand tremor, stick in the right hand, hood up on the river and pushed back inside Karnak. Rami: B1 → B2 (right sleeve torn, splint LEFT); dies at 07.09.005. Nour: B1 → B2; sleeves wet to the elbow from 07.09.015. Soldiers in tan helmets (WARD_A); Fathi bareheaded (WARD_B); Tarek WARD_B with the handset. Tut's launch/avenue damage is `DMG_L1` + the `DMG_L1_RIVER` add phrase; Fathi's Seq 5–6 "river-wet to the knees" (`DMG_L1`) is not carried into Seq 7 (his dusty WARD_B is the L2 look). The Reis's RIGHT hand is the one on the trolley handle (07.09.013) and the one lost (07.09.015).
- **The Reis.** R2 (mast, cracked chest star) until the trolley goes over (07.09.015); **R3 from 07.09.015** (RIGHT hand lost, clean white stump).
- **Key block path.** PROP_KARNAK_BLOCK: in the field (07.06.007) → TURNED (07.06.008) → ON_TROLLEY, cut face DOWN (07.06.016) → the nave run (07.08.026) → quay LIP (07.09.007) → OVER / SINKING (07.09.015–016).
- **Geography.** River south = frame right (07.01). Hypostyle: nave west = frame left in laterals; the midpoint axials look WEST at the projection; from 07.08.019 the jackals are frame RIGHT of the party, so the party flees frame left (07.08.020) and fires back toward frame right (07.08.025). Ninth Pylon: pylon frame right, chain right → left, the sweep advances toward camera (the countdown FOUR → ONE is Adaeze's fingers in one repeated framing, 07.06.004/006/010/014). Quay master (07.09.002): river frame right, parapet frame left high, runners toward camera; the jackal fires frame left → right, away from the lens.
- **The projection (07.08).** The father's face is never generated in a plate: element 07.08.005 (locked-face MCU against black, lip-synced to the recorded Middle Egyptian) is mapped onto the pylon plates in 07.08.004/009/010/027. The screenplay names the Second Pylon; file 03 entry 22 maps the plate to `LOC_KARNAK_RAM_AVENUE_PROJECTION` (First Pylon) — open item 05 §14 Q4; prompts describe only "a colossal gateway tower at the far end of the aisle". The nurse/bracelet broadcast (07.08.012–013) is its own Garden plate, adults only.
- **Safety.** Rami's death uses the full kill grammar (05 §7.1; worked example 05 §11 renumbered 07.09.003–005). The body is only "a still shape in the shadow", never lit (07.09.020–024). No weapon toward the lens anywhere; the jackal in 07.08.021 hits stone only. The Reis's broken wrist is clean white ceramic.
- **Negatives.** `{NEG_PLATE}` (people, figures, crowds, vehicles, animals) only on the empty plates (07.01.007, 07.03.001, 07.03.004–005, 07.08.010, 07.08.021); unit-, boat- and trolley-led shots carry "people, crowds" as shot-specific terms instead, so the negative never fights the subject. Quantities of units are written "three identical machines, each {UNIT_….SHORT}" (the locks begin with "a").
- **Language.** Late Egyptian (07.04), Middle Egyptian (07.08.005) and the mouthed block lines (07.06.009/012/013) are recorded with the consultant before generation; Egyptian Arabic (07.07.005, 07.09.003, 07.09.025) by native speakers; all subtitles COMP. SESHAT/Reis lines are V.O. with no sync.
- **Screenplay verify notes carried:** the nb → ḏsr recut (07.04.007); the ḫprw subtitle and gloss (07.06.009/013); Sacred Lake position (07.06.026); First Pylon → landing distance (07.09.001); Faisal Street (07.09.003); cruise-ship moorings (07.10.001); the RAMI spelling (07.10.008).

## Reference stills needed

**Characters (file 01; approve and freeze before any Seq 7 generation)**
- Tut: `CHAR_TUT_A0_front`, `CHAR_TUT_A0_34`, `CHAR_TUT_B_night_34` (hood up), `CHAR_TUT_B1_full` (+ an L2 image-edit variant for B2: sandstone dust, torn pocket flap, greyed hem), `CHAR_TUT_HANDS`, `CHAR_TUT_FOOT`.
- Nour: `CHAR_NOUR_A_front`, `CHAR_NOUR_A_34`, `CHAR_NOUR_B_full` (+ B2 image edit: dust, torn right cuff; + wet-sleeves edit for 07.09.015 →).
- Rami: `CHAR_RAMI_A_front`, `CHAR_RAMI_A_34`, `CHAR_RAMI_B_full` (+ B2 edit: dust, right sleeve torn at the elbow).
- Adaeze: `CHAR_ADAEZE_A_front`, `CHAR_ADAEZE_A_34`, `CHAR_ADAEZE_B_full` (+ B2 edit: dust, torn blazer pocket; headlamp round the neck).
- Fathi: `CHAR_FATHI_A_front`, `CHAR_FATHI_A_34`, `CHAR_FATHI_B_full`.
- Tarek: `CHAR_TAREK_A_front`, `CHAR_TAREK_A_34`, `CHAR_TAREK_B_full` (handset on the vest).
- Tomas: `CHAR_TOMAS_A_front`, `CHAR_TOMAS_A_34`, `CHAR_TOMAS_B_work`.
- Soldiers (tan helmets): `CHAR_MINA_A_front`, `CHAR_MINA_A_full`, `CHAR_KARIM_A_front`, `CHAR_KARIM_A_34`, `CHAR_KARIM_A_full`, `CHAR_YOUSSEF_A_full`.
- The father (projection element): `CHAR_AKHENATEN_A_front`, `CHAR_AKHENATEN_A_34`, `CHAR_AKHENATEN_A_full`.
- Garden broadcast: `CHAR_GARDEN_SLEEPERS` approved plate (adults only).

**Units (file 02; REF A/REF stills + 3D assets)**
- `UNIT_SHABTI` (bucket-chain; 3D asset for the VFX-EXTEND chain), `UNIT_REIS` (R2 and R3 states), `UNIT_JACKAL`, `UNIT_FLY` (3D asset for the swarm, 07.08.024), `UNIT_SURVEY_DRONE` (SEARCHLIGHT, CAMERA, FLOOD, PROJECTOR pods), `UNIT_NURSE`.

**Props (file 04; `<TOKEN>_REF`)**
- `PROP_KARNAK_BLOCK` (front-face relief signed off by the Egyptologist; hidden face as a separate consultant sign plate), `PROP_BLOCK_TROLLEY` (EMPTY, LOADED, LIP, OVER), `PROP_RAMI_NOTEBOOK` (DAMP, CRACKED), `PROP_CONSERVATION_KIT` (shut, slung), `PROP_STOPWATCH`, `PROP_POLICE_HANDSET`, `PROP_POLICE_LAUNCH` (L1, L4), `PROP_EBONY_STICK`, `PROP_LAYLA_PENDANT` (CLUTCHED), `PROP_SLEEP_BRACELET`, `PROP_FELUCCA`, `PROP_DEMO_CHARGES`.

**Location plates (file 03; `LOC_<TOKEN>_<VARIANT>_plate`)**
- `LOC_NILE_NIGHT`, `LOC_NILE/LUXOR_NIGHT` (unbranded cruise hulls), `LOC_KARNAK_QUAY_NIGHT` (+ coverage: reverse from the launch = master; low angle on the parapet; quay edge; underwater SINKING plate), `LOC_KARNAK_RAM_AVENUE_NIGHT`, `LOC_KARNAK_RAM_AVENUE_PROJECTION` (+ close stone plate of the pylon face for 07.08.010), `LOC_KARNAK_HYPOSTYLE_NIGHT` (+ side-aisle and floor-level coverage; with/without threads), `LOC_KARNAK_HYPOSTYLE_PROJECTION`, `LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT`, `LOC_KARNAK_NINTH_PYLON_NIGHT_WORK`, `LOC_KARNAK_NINTH_PYLON_DARK`, `LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_NIGHT_WORK`, `LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK` (ground-level coverage), `LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK`, `LOC_KARNAK_SACRED_LAKE_NIGHT`, `LOC_WEST_BANK_FIELDS_NIGHT` (cliffs, distant).

**Comp assets**
- Subtitle and SUPER files for seq 07 ("5 NOVEMBER. 21:00.", "00:31", "01:00", "03:00"); handwriting asset `RAMI_HAND_44`; consultant sign plates (the block's hidden face; kheperu; RAMI in three signs); the chest-glow G0f element; the "06:14" type; the projection element 07.08.005.

---

## 07.01 — EXT. NILE, NORTH OF LUXOR - NIGHT (07.01.001–015)

### 07.01.001 — EXT. NILE, NORTH OF LUXOR - NIGHT — The launch runs dark   (8 s)
- **Shot:** Extreme wide establishing, anamorphic 75mm, locked-off · **Move:** locked-off; the launch crosses frame left to right
- **In frame:** PROP_POLICE_LAUNCH (state L1); the party aboard, too small to read
- **Action:** The police launch runs without lights up the black river, left to right (south, toward Luxor); both banks black for miles; stars on the water.
- **Dialogue:** —
- **Sound:** low diesel throb, water hissing along the hull, nothing else for miles; no music
- **PROMPT:** Extreme wide establishing shot, anamorphic 75mm lens, locked-off, from low on the west bank: {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L1}, glides slowly from frame left to frame right across the middle of the frame, a few small figures on its deck too far away to read. Setting: {LOC_NILE.LONG}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: hushed, a whole country holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit windows on the banks, city skyglow, moon, headlights, navigation lights, readable faces, fishing lanterns
- **Refs:** PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "5 NOVEMBER. 21:00." | lower left, small (05 §13.7) | 1 s in → 1 s before the cut | SUPER file, seq 07
- **Continuity:** River geography: south (upriver, toward Luxor) = frame right (file 03 entry 20). Launch L1: running dark, only the dim red wheelhouse lamp (05 §14 Q2: keep it a broad dim glow, never a line). Tarek at the wheel; Tut in the stern; Nour at the bow.

### 07.01.002 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tut in the stern, the glow stutters   (6 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld with the roll of the deck
- **In frame:** TUT (CHAR_TUT_B1); TOMAS (CHAR_TOMAS_B1) as a soft shoulder at frame right edge
- **Action:** Tut sits in the stern facing west, hood up, as he has since noon; under the jacket a pale glow pulses, stutters, pulses.
- **Dialogue:** —
- **Sound:** diesel throb, water, a faint irregular electric tick under the engine note (the core)
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld with the gentle roll of the deck: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, {CHAR_TUT.STATE_G0F}, the charcoal hood up, sits perfectly still on a bench at the stern of {PROP_POLICE_LAUNCH.SHORT}, a near-black ebony staff across his knees, gazing past frame left over the water while the soft glow at his chest fades and returns. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim red wheelhouse lamp glancing off one cheek. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bright chest lamp, light beams from the chest, glowing symbols, hood hiding the whole face
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f | pale-green pulse that stutters: pulse · drop-out · pulse (file 01 glow table) | centre chest, through the jacket | whole shot | glow element library
- **Continuity:** Tut look B1 (T-B, river damage L1 + L1_RIVER add phrase) on the launch; L2 sandstone dust applies from 07.03. Hood up, facing west. Nape scar (6.2) under the hood, unseen. Stick across his knees; dagger at the belt (unseen).

### 07.01.003 — EXT. NILE, NORTH OF LUXOR - NIGHT — Two fingers on the seam; the stopwatch   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TOMAS's hands; TUT's left wrist; PROP_STOPWATCH
- **Action:** Tomas's two fingers rest on the gold seam at Tut's wrist; in his other hand the cheap stopwatch; his thumb presses a button once.
- **Dialogue:** —
- **Sound:** a soft plastic click; the engine; the irregular tick
- **PROMPT:** Insert, 100mm macro lens, locked-off: two long pale fingers rest on a slender olive-brown wrist with {CHAR_TUT.STATE_WRIST_SEAMS}, feeling for a rhythm, while beside it {PROP_STOPWATCH.LONG}, {PROP_STOPWATCH.STATE_HELD}, and a large thumb presses one rubber button once. Setting: the open aft deck of an old grey steel river launch, at night. Lighting: faint starlight and a dim red wheelhouse lamp, a soft glow from under a charcoal jacket sleeve warming the skin. Mood: clinical patience, worry underneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, digits on the display, glowing numbers, wristwatch on the slender wrist, rings, bracelets
- **Refs:** CHAR_TUT_HANDS, CHAR_TOMAS_B_work, PROP_STOPWATCH, LOC_NILE_NIGHT
- **Continuity:** Stopwatch in Tomas's right hand (from 6.2), display left blank (digits would be COMP; not read here). Both wrist seams intact (the left cracks only at 9.4).

### 07.01.004 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tomas: "losing regulation"   (6 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TOMAS (CHAR_TOMAS_B1)
- **Action:** Tomas, kneeling, glances from the stopwatch to Tut (off frame right) and speaks.
- **Dialogue:** TOMAS: "The core's losing regulation. The stalls will come closer together."
- **Sound:** engine, water; his voice low under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, kneels on the deck, glances down at a small grey stopwatch in his hand, then up toward someone off frame right, speaking quietly. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a faint soft glow from off frame right lighting his beard from below. Mood: dry, literal calm, worry held back. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, PROP_STOPWATCH, PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Continuity:** Eyeline frame right to Tut. Tomas B at L1 (no damage phrase in file 01). Tomas stays aboard at Karnak (07.02).

### 07.01.005 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tut: "walk in the gaps"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut keeps his eyes on the far bank and answers, a dry curve at the mouth.
- **Dialogue:** TUT: "Then I will walk in the gaps."
- **Sound:** engine, water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, the charcoal hood up around his face, keeps his eyes on the dark far bank off frame left and speaks one short sentence softly, a faint dry curve at the mouth. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim red wheelhouse lamp on one cheek. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood shadow over the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_NILE_NIGHT
- **Continuity:** Mouth fully lit for sync (05 §9.2); the voice's soft consonants live in the recording, never in the picture.

### 07.01.006 — EXT. NILE, NORTH OF LUXOR - NIGHT — Nour lowers the binoculars   (6 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** At the bow, Nour lowers the binoculars, eyes staying on the one light on the east bank.
- **Dialogue:** —
- **Sound:** the bow cutting water; far off, almost below hearing, a machine hum
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, stands at the bow rail of an old grey steel launch and slowly lowers a pair of black binoculars from her eyes, still staring off frame right at something far across the water. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a faint cold white glow from the distant east bank on her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, brand marks on the binoculars
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Continuity:** Nour B1 (river-damp cuffs, curls loose). Pendant under the blouse collar. Eyeline frame right = the Karnak glow (07.01.007).

### 07.01.007 — EXT. NILE, NORTH OF LUXOR - NIGHT — The only light for miles   (6 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off (Nour's eyeline, not a binocular matte)
- **In frame:** the east bank; the Karnak work light (LOC_KARNAK_NINTH_PYLON, distant)
- **Action:** The east bank black for miles; above it one dome of white light over temple gateways; a slow flash winks inside it.
- **Dialogue:** —
- **Sound:** wind over water; a faint far-off electric snap with each flash
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, long-lens compression across black water: a flat black riverbank with palms in silhouette, and above it the only light for miles, a dome of hard white floodlight over the dark sloping outlines of ancient temple gateways, a slow white flash winking inside it every few seconds. Setting: {LOC_NILE.SHORT}, the east bank at Luxor, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the white glow the only other source. Mood: ominous, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, city lights, skyglow, lit windows, fireworks, lightning, searchlight beams in the sky
- **Refs:** LOC_NILE_NIGHT, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** The flashes are the CAMERA drone sweep (07.05–07.06); keep their rhythm (about one every 4 s) for the edit.

### 07.01.008 — EXT. NILE, NORTH OF LUXOR - NIGHT — Nour: "the Ninth Pylon"   (7 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour turns her head toward the stern and explains, then her eyes go back to the glow.
- **Dialogue:** NOUR: "That's the Ninth Pylon. It's taking it down. Horemheb packed Akhenaten's temples inside it as fill. Talatat."
- **Sound:** bow wash; her voice level
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, the binoculars lowered at her chest, turns her head a little toward the stern off frame left, speaking quietly, then lets her eyes go back to the far glow. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a faint cold white glow from the distant bank on one side of her face. Mood: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE_NIGHT
- **Continuity:** Eyeline frame left = the stern party (Tut, Rami, Adaeze). Binoculars stay at her chest to the end of the scene.

### 07.01.009 — EXT. NILE, NORTH OF LUXOR - NIGHT — Rami: question forty-four   (6 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** RAMI (CHAR_RAMI_B1); PROP_RAMI_NOTEBOOK; PROP_CONSERVATION_KIT (shut, at his feet)
- **Action:** Rami, splinted left hand, flips his notebook open and reads the question aloud, eager.
- **Dialogue:** RAMI: "Forty-four. 'Why did Horemheb hide the talatat instead of smashing them?'"
- **Sound:** a page flipped; engine; his quick voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L1}, sits on the deck bench with a shut grey hard-shell case at his feet, flips open {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_DAMP}, pinning it with his splinted hand, and speaks one short sentence with bright eagerness. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a tiny dim torch clipped to the notebook lighting the page and his glasses from below. Mood: wry, eager. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable handwriting, splint on the right hand
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, PROP_RAMI_NOTEBOOK, PROP_CONSERVATION_KIT, LOC_NILE_NIGHT
- **Continuity:** Rami B1 (river-damp; splint LEFT, two fingers taped to a tongue depressor). Kit shut on its strap. Notebook damp (Seq 6); pages angled away so nothing reads.

### 07.01.010 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tut: "Stone is expensive"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut turns his head a little toward Rami and answers, almost amused.
- **Dialogue:** TUT: "Stone is expensive. Hatred is cheap. You fill a pylon with what you have."
- **Sound:** engine, water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, the charcoal hood up, turns his head a little toward someone off frame right, speaking quietly with a flicker of dry amusement, then looks back at the water. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a small torch glow from off frame right on his cheek. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_NILE_NIGHT
- **Continuity:** Rami is frame right of Tut on the stern bench (hold the line through 07.01.014).

### 07.01.011 — EXT. NILE, NORTH OF LUXOR - NIGHT — Nour: "the one he tried to erase"   (8 s)
- **Shot:** MS two-shot, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B1, foreground, sharp); RAMI (CHAR_RAMI_B1, background, soft)
- **Action:** Nour, come back from the bow, crouches by the wheelhouse and adds the point; behind her, soft, Rami writes.
- **Dialogue:** NOUR: "And by burying them he saved them. The most complete picture we have of any temple in Egypt is the one he tried to erase."
- **Sound:** engine; pen scratch under her line
- **PROMPT:** Medium two-shot, anamorphic 50mm lens, subtle handheld: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, crouches in the foreground beside a grey steel wheelhouse, speaking quietly toward the stern, while behind her, soft and out of focus, {CHAR_RAMI.SHORT} bends over a notebook, writing fast. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim red wheelhouse lamp and a small torch glow behind her. Mood: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_RAMI.NEG}, readable handwriting
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, CHAR_RAMI_B_full, PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Continuity:** Two faces only; Rami stays soft. Line ~7.5 s; if longer, split at the sentence end over 07.01.012.

### 07.01.012 — EXT. NILE, NORTH OF LUXOR - NIGHT — Rami scribbles, delighted   (4 s)
- **Shot:** Insert, 100mm macro, subtle handheld · **Move:** subtle handheld
- **In frame:** RAMI's hands; PROP_RAMI_NOTEBOOK
- **Action:** A pen races across the damp page under question 44; the splinted left hand pins the page.
- **Dialogue:** —
- **Sound:** fast pen scratch; a delighted breath
- **PROMPT:** Insert, 100mm macro lens, subtle handheld: a right hand races a cheap pen across an open page of {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_DAMP}, leaving fast slanted lines of ink, while a left hand in a finger splint bound with white tape pins the page flat. Setting: the deck of an old grey steel river launch, at night. Lighting: a tiny dim torch clipped to the notebook, deep black around the page. Mood: delighted, quick. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible words, printed text, splint on the right hand, brand marks on the pen
- **Refs:** PROP_RAMI_NOTEBOOK, CHAR_RAMI_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** handwriting | 44. "Stone is expensive. Hatred is cheap." (English, Rami's fast slanted hand) | on the page under the pen | writes on with the pen | handwriting asset RAMI_HAND_44 (reused in 07.10.007)
- **Continuity:** Establishes the exact page Tut reads in 07.10.007: same handwriting asset, same page layout.

### 07.01.013 — EXT. NILE, NORTH OF LUXOR - NIGHT — Adaeze: "missing a rule"   (7 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze, against the wheelhouse wall, thinks aloud.
- **Dialogue:** ADAEZE: "The glass said 'whoever would ascend must first be weighed.' Nothing about how. If it's digging, it's missing a rule."
- **Sound:** engine, water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L1}, a switched-off headlamp round her neck, sits against a grey steel wheelhouse wall, looks toward the far glow off frame right and speaks, thinking aloud. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim red wheelhouse lamp and a faint cold white glow from the far bank lifting her face. Mood: sharp, dry, thinking aloud. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, lit headlamp
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE_NIGHT
- **Continuity:** Adaeze B1 (creased, river-damp); headlamp round the neck, off. Canvas shoulder bag at her side. Deep-brown skin keyed by the far glow (05 §3.2 GRADE_NIGHT_ACTION: faces must read).

### 07.01.014 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tut: "the first thing it has wanted"   (5 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut, eyes on the glow, answers.
- **Dialogue:** TUT: "Then that is the first thing it has wanted that it does not have."
- **Sound:** engine drops under the line
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, the charcoal hood framing his face, eyes fixed on the distant white glow off frame right, speaks one short sentence softly and very still. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a faint cold white glow from the far bank catching his eyes. Mood: royal, dry, a first glint of hope. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_NILE_NIGHT
- **Continuity:** Push-in ≤10% of frame. Eyeline frame right to the glow (matches 07.01.006).

### 07.01.015 — EXT. NILE, NORTH OF LUXOR - NIGHT — Tarek at the wheel: "we take it first"   (6 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B1); PROP_POLICE_HANDSET on his vest
- **Action:** Tarek, both hands on the wheel, watches the glow through the salt-hazed glass and decides.
- **Dialogue:** TAREK: "Then we take it first."
- **Sound:** engine note rising a little as he opens the throttle
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld inside a small wheelhouse: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, {PROP_POLICE_HANDSET.SHORT}, both hands on the wheel, watches a far white glow through salt-hazed windows and speaks one short sentence, then eases the throttle forward. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, at night. Lighting: a dim red wheelhouse lamp from below, faint cold white glow through the glass ahead. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, glowing instrument screens, readable dials
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_HANDSET, PROP_POLICE_LAUNCH, LOC_NILE_NIGHT
- **Continuity:** Tarek B at L1 (the WARD_B phrase carries "dusty"); handset on the vest from 6.4; rifle slung. Cut to 07.02 on the throttle.

## 07.02 — EXT. KARNAK, AVENUE OF RAMS - NIGHT (07.02.001–007)

### 07.02.001 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — The launch noses into the landing   (6 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (L1); the party stepping ashore (small, faces unreadable); MINA and TOMAS stay at the rail
- **Action:** The launch noses into a dark stone landing below the Corniche; small figures step off onto the stone; two stay at the rail.
- **Dialogue:** —
- **Sound:** engine dropping to idle, tyre fenders squeaking on stone, water slap
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off: {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L1}, noses slowly in against the dark stone edge of the landing from frame right, and small dark figures step off onto the stone while two tall figures stay at the rail. Setting: {LOC_KARNAK_QUAY.LONG}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: hushed, careful. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit street lamps, lit windows, skyglow, readable faces, crowds
- **Refs:** PROP_POLICE_LAUNCH, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** The same quay as 07.09 (the geography master is 07.09.002). Mina and Tomas stay aboard. Launch moored at the far end of the quay for the rest of the sequence.

### 07.02.002 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — Up the steps in single file   (6 s)
- **Shot:** MS low angle, anamorphic 32mm, locked-off · **Move:** locked-off at the top of the landing steps
- **In frame:** TAREK (CHAR_TAREK_B1), RAMI (CHAR_RAMI_B1, kit slung), TUT (CHAR_TUT_B1, on the stick); FATHI, YOUSSEF, KARIM, NOUR, ADAEZE behind, soft
- **Action:** The party climbs the stone steps past camera in single file: Tarek, Rami with the kit bag, Tut on his stick; the others behind in silhouette.
- **Dialogue:** —
- **Sound:** boots on stone, the stick's gold cap ticking on each step, breath
- **PROMPT:** Medium low-angle shot, anamorphic 32mm lens, locked-off at the top of a flight of worn stone steps: {CHAR_TAREK.SHORT} climbs past camera, rifle slung, followed by {CHAR_RAMI.SHORT} with a grey hard-shell case, {PROP_CONSERVATION_KIT.STATE_SLUNG}, then {CHAR_TUT.SHORT}, hood up, climbing one step at a time with a near-black ebony staff, more figures behind them in silhouette. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: starlight only, a faint white glow in the sky beyond the steps. Mood: silent, tense. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_RAMI.NEG}, {CHAR_TAREK.NEG}, torches on, rifle pointed at the camera
- **Refs:** CHAR_TAREK_B_full, CHAR_RAMI_B_full, CHAR_TUT_B1_full, CHAR_TUT_B_night_34, PROP_CONSERVATION_KIT, PROP_EBONY_STICK, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Order up the steps: Tarek, Fathi, Youssef, Karim, Nour, Adaeze, Rami (kit), Tut (stick, right hand). Rifles slung, muzzles down. Only Tarek and Rami read as faces.

### 07.02.003 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — The ram avenue by starlight   (8 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the party (eight small figures) walking between the rams toward the First Pylon
- **Action:** Ram-headed sphinxes by starlight; the small party walks up the avenue toward the colossal gateway; far inside, a white work light.
- **Dialogue:** —
- **Sound:** night wind in palms, footsteps tiny under the scale, a far machine hum from inside the temple
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off, low on the axis of the avenue: eight small dark figures walk away from camera up the middle of the paving between the rams toward the gateway, the smallest one leaning on a staff. Setting: {LOC_KARNAK_RAM_AVENUE.LONG}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}, a white work light glowing far inside beyond the gateway. Mood: awe and dread, very quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit town, street lamps, tourists, readable faces, moon
- **Refs:** LOC_KARNAK_RAM_AVENUE_NIGHT, CHAR_TUT_B_night_34
- **Continuity:** Geography lock (file 03 entry 22): the avenue runs west → east toward the gateway; the landing and the Corniche are behind camera. The group walks away from camera.

### 07.02.004 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — White pinpoints drift across the stars   (5 s)
- **Shot:** Low-angle wide, anamorphic 40mm, slow tilt up · **Move:** slow tilt up from a ram's horned head to the sky
- **In frame:** UNIT_FLY ×5–6 (pinpoints)
- **Action:** Above the rams, white pinpoints drift across the stars, each trailing a hair-thin glint.
- **Dialogue:** —
- **Sound:** a faint high whine, gone again
- **PROMPT:** Low-angle wide shot, anamorphic 40mm lens, slow tilt up from the weathered horned head of a sandstone ram sphinx to the night sky, where five small drones drift slowly across the stars in a loose line, each one {UNIT_FLY.LONG}. Setting: {LOC_KARNAK_RAM_AVENUE.SHORT}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, blinking navigation lights, coloured lights, aircraft, meteors, people, crowds
- **Refs:** UNIT_FLY, LOC_KARNAK_RAM_AVENUE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Flies travel toward the Hypostyle (they cling to the columns in 07.03). Threads are VFX lines if the plate loses them.

### 07.02.005 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — Fathi prays behind a ram   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi stops behind a ram, palms up, lips moving: a few private seconds.
- **Dialogue:** — (private prayer, unheard)
- **Sound:** wind; his breath; nothing of the words
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, stops in the shadow behind a crouching sandstone ram, lifts both palms up at chest height and lowers his eyes, his lips moving silently for a few seconds. Setting: {LOC_KARNAK_RAM_AVENUE.SHORT}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_NIGHT}, hard white spill from the gateway floods catching the side of his face. Mood: quiet, private devotion. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, prayer mat, kneeling, prayer beads, exaggerated piety
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_RAM_AVENUE_NIGHT
- **Continuity:** Fathi B1 look in the dusty WARD_B (the Seq 5–6 "river-wet to the knees" phrase is dropped: dry by 21:00, and 07.02.007 in the same scene carries none); bareheaded, beret under the shoulder strap; red scarf at the neck; satchel across the body; rifle slung. His eyeline ends frame left, to Tut (07.02.006).

### 07.02.006 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — Tut watches   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut, leaning on the stick among the rams, has been watching; he does not look away.
- **Dialogue:** —
- **Sound:** wind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, {CHAR_TUT.STATE_STICK}, {PROP_EBONY_STICK.STATE_ST1}, hood pushed back, stands still between two sandstone rams, watching someone off frame right with quiet attention. Setting: {LOC_KARNAK_RAM_AVENUE.SHORT}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_NIGHT}, hard white spill on one side of his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_KARNAK_RAM_AVENUE_NIGHT
- **Continuity:** Hood pushed back from here to the end of the Hypostyle scenes (faces must read; 05 §9.2). Stick in the right hand.

### 07.02.007 — EXT. KARNAK, AVENUE OF RAMS - NIGHT — Fathi: "It costs the same"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi finds Tut watching, lowers his hands, and answers plainly.
- **Dialogue:** FATHI: "For all of us. It costs the same."
- **Sound:** wind; the far machine hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, lowers his open palms, finds someone watching him off frame left, and speaks one short sentence with a small, unembarrassed smile. Setting: {LOC_KARNAK_RAM_AVENUE.SHORT}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_NIGHT}, hard white spill from the gateway floods lifting his face out of the dark. Mood: warm, plain, unembarrassed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_RAM_AVENUE_NIGHT
- **Continuity:** Deep-brown skin: motivated white spill must reach the face (05 §3.2); lift ⅓–⅔ stop in comp if short.

## 07.03 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT (07.03.001–018)

### 07.03.001 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — A forest of stone   (8 s)
- **Shot:** Extreme wide establishing, low angle, anamorphic 24mm · **Move:** slow tilt up from the column bases to the stars between the capitals
- **In frame:** the hall, empty
- **Action:** One hundred and thirty-four columns, the roof long fallen, stars between the capitals; the twelve great columns climb twenty-one metres into the dark.
- **Dialogue:** —
- **Sound:** a vast stone silence; wind high in the capitals; far-off drone hum
- **PROMPT:** Extreme wide establishing shot, low angle, anamorphic 24mm lens, slow tilt up from the carved bases of the columns to the night sky between their capitals, the giant central columns climbing into darkness, stars showing through the gaps where the roof has fallen. Setting: {LOC_KARNAK_HYPOSTYLE.LONG}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: awe, a cathedral holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, intact roof, tourist barriers, signage, coloured uplighting, moon
- **Refs:** LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Geography lock (file 03 entry 23): the central aisle runs west (frame left) → east (frame right) in lateral shots; the Third Pylon closes the far end looking east.

### 07.03.002 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Flies on the shafts like moths   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_FLY ×10–12 clinging to a column shaft
- **Action:** A dozen flies cling motionless to a carved column shaft, pinpoints steady, like moths on a porch.
- **Dialogue:** —
- **Sound:** the faintest collective electrical hum
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: a dozen small drones cling motionless to the deeply carved shaft of a colossal sandstone column at different heights, each one {UNIT_FLY.SHORT}, their white pinpoints steady, hair-thin threads running off from each into the dark. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, insects, moths, blinking lights, coloured lights, people, crowds
- **Refs:** UNIT_FLY, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Every column carries flies until 01:00 (07.08.002, all pinpoints out). Threads are VFX lines on the approved plate (05 §10 row 15).

### 07.03.003 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — The searchlight drone over the nave   (6 s)
- **Shot:** Wide low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SURVEY_DRONE (SEARCHLIGHT)
- **Action:** Over the central nave hangs a searchlight drone, turning slowly; its beam rakes the forest.
- **Dialogue:** —
- **Sound:** a low rising rotor hum; the beam's silence
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off, looking up the central aisle between the giant columns: {UNIT_SURVEY_DRONE.LONG}, {UNIT_SURVEY_DRONE.STATE_SEARCHLIGHT}, hangs high over the aisle and turns slowly on the spot, its hard white beam sweeping across the carved column faces, dust hanging in the light. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, red lights on the drone, laser beams, coloured beam, people, crowds
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** The searchlight's pass takes about 8 s ("Eight seconds a pass"); its turn drives the silver/black rhythm of the scene.

### 07.03.004 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — A loom: silver, then black   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off down a side aisle
- **In frame:** the threads (VFX); the hall
- **Action:** The beam moves across, and for one heartbeat the hall is strung with silver: hundreds of threads, column to column, at shin, waist and throat. The beam moves on. Black.
- **Dialogue:** —
- **Sound:** a thin shimmering tone on the silver (score), cut dead on the black
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off down a side aisle between colossal columns: a hard white beam sweeps across from frame left and for one moment lights {LOC_KARNAK_HYPOSTYLE.STATE_THREADS}, dozens of lines crossing the aisle, then the beam passes on and the aisle falls back into black. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: a held breath, beautiful and lethal. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, laser beams, red lines, glowing strings, ropes, cables, spider webs
- **Refs:** LOC_KARNAK_HYPOSTYLE_NIGHT, UNIT_FLY
- **Flags:** VFX-ASSIST, VFX-EXTEND
- **Continuity:** Deliver the plate with and without threads; the loom is a VFX line pass (05 §10 row 15). Threads: STATE_THREADS until 07.08.023 (snapped). VFX thread rig on the approved plate: hair-thin silver lines column to column at shin, waist and throat, lit only inside the beam, on with the beam and off as it passes.

### 07.03.005 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — One thread at throat height   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, rack focus from the thread to the column behind
- **In frame:** a single thread
- **Action:** A single thread at throat height flares silver in the passing beam, then vanishes into black.
- **Dialogue:** —
- **Sound:** a faint high glassy note
- **PROMPT:** Insert, 100mm macro lens, locked-off, rack focus from a single hair-thin glinting thread stretched taut across frame to the carved sandstone column it is anchored to: the thread flares bright silver as a white beam crosses it, then fades into black as the beam moves on. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: tense, delicate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, rope, cable, wire, spider web, laser
- **Refs:** UNIT_FLY, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The thread is the fly's filament (file 02 §6), no light of its own: it only glints.

### 07.03.006 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Fathi: "Every thread ends at a fly"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Crouched behind a column base, Fathi whispers the rule.
- **Dialogue:** FATHI (whisper): "Every thread ends at a fly. Touch one, they all know."
- **Sound:** his whisper close; the drone hum above
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, crouches low against the base of a colossal carved column, eyes on the dark aisle off frame right, and speaks one short sentence in a low whisper, face clearly visible. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, spill from a passing white beam lifting his face. Mood: military exactness, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, hand over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** L2 from 07.03 for the whole party (sandstone dust). Fathi has no L2 phrase in file 01: the WARD_B "dusty" carries it.

### 07.03.007 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Three red lines down the nave   (6 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off, long-lens compression down the nave
- **In frame:** UNIT_JACKAL ×3
- **Action:** Down the nave, three thin red lines pace between the great columns: jackals, rifle modules along their spines.
- **Dialogue:** —
- **Sound:** nothing: they make no sound; a faint servo whisper
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, compressed down the central aisle between the giant columns: three identical machines lope silently in single file across the aisle and back, each one {UNIT_JACKAL.LONG}, their red lines the only colour in the dark. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, dog ears, tails, muzzles toward the lens, laser sights, people, crowds
- **Refs:** UNIT_JACKAL, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Jackals hold the axis (the central aisle); the party keeps to the side aisles. Weapons flush along the spine, pointing along their path, never at the lens.

### 07.03.008 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Fathi: "Eight seconds a pass"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi gives the plan in a whisper, two fingers pointing along the side aisle.
- **Dialogue:** FATHI (CONT'D): "The axis is theirs. We take the aisles. Eight seconds a pass."
- **Sound:** whisper; drone hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, still crouched against the column, points two fingers along the dark side aisle off frame left and speaks in a low whisper, face clearly visible. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, a passing white beam sliding across his face and away. Mood: military exactness, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, hand over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Direction of travel: along the side aisle, frame left.

### 07.03.009 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Silver: they memorise. Black: they move   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off down the side aisle
- **In frame:** NOUR (CHAR_NOUR_B2), ADAEZE (CHAR_ADAEZE_B2), RAMI (CHAR_RAMI_B2), soldiers; faces half in shadow
- **Action:** The beam comes: the group flattens to the columns, eyes on the threads, memorising. The beam goes: in the black they slip forward a few steps.
- **Dialogue:** —
- **Sound:** breath held; then soft steps; the drone turning
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off down a side aisle: as a hard white beam lights the threads, {CHAR_NOUR.SHORT}, {CHAR_ADAEZE.SHORT} and {CHAR_RAMI.SHORT} press flat against colossal columns, staring at the lines, then the beam passes and in near darkness they slip a few careful steps forward. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, {LOC_KARNAK_HYPOSTYLE.STATE_THREADS}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_RAMI.NEG}, running, torches, ropes, laser lines
- **Refs:** CHAR_NOUR_B_full, CHAR_ADAEZE_B_full, CHAR_RAMI_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** L2 for all (dust); Rami's right sleeve now torn at the elbow (scrambling up the landing, off screen). Threads as VFX lines.

### 07.03.010 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Fathi guides Nour's boot over a shin-thread   (5 s)
- **Shot:** Insert at floor level, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI's hand; NOUR's boot; a thread
- **Action:** In the dark, Fathi's hand takes Nour's boot by the ankle and guides it up and over a shin-height thread.
- **Dialogue:** —
- **Sound:** a boot sole brushing stone; breath
- **PROMPT:** Insert at floor level, 100mm macro lens, locked-off: in near darkness a large dark-brown hand closes gently round the ankle of a black leather ankle boot and guides it slowly up and over a hair-thin glinting thread stretched at shin height, setting the boot down beyond it on the dusty paving. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: faint white spill from a distant beam, the thread catching one glint. Mood: restrained terror, tender precision. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, rope, cable, laser, the boot touching the thread
- **Refs:** CHAR_FATHI_B_full, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Nour's black ankle boots (WARD_B). The thread is a VFX line.

### 07.03.011 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Rami ducks a throat-thread   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B2)
- **Action:** Black: Rami ducks under a throat-height thread, splinted hand pressed to his chest, and comes up on the far side.
- **Dialogue:** —
- **Sound:** a held breath let out through the nose
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L2}, his splinted left hand pressed flat to his chest, bends low under a hair-thin glinting thread at throat height, eyes on the line, then straightens slowly on the far side and lets out a silent breath. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, faint spill from a distant beam. Mood: restrained terror, a flicker of pride. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, rope, laser
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Kit case slung on his right shoulder, shut. Splint LEFT.

### 07.03.012 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — The ceramic foot stops in the air   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off at ankle height
- **In frame:** TUT's left foot; a thread
- **Action:** Tut steps. The black ceramic foot lifts — and stops in the air, the adze-curve of its toe a finger's width from a thread. It will not come down.
- **Dialogue:** —
- **Sound:** a tiny ceramic click inside the ankle; then nothing
- **PROMPT:** Insert, 100mm macro lens, locked-off at ankle height: {CHAR_TUT.STATE_FOOT}; the ceramic foot lifts for a step and stops dead in the air, its hooked toe a finger's width above a hair-thin glinting thread, trembling very slightly, the dusty cuff of dark cargo trousers above it. Setting: the dusty paving of {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: faint white spill from a distant beam, one glint along the thread. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, human toes on the left foot, shoe on the left foot, robotic claws, the foot touching the thread
- **Refs:** CHAR_TUT_FOOT, CHAR_TUT_B1_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The foot stall (file 01: "stops in the air over a thread at 7.1"). Left foot ceramic; right foot sandal (not in frame).

### 07.03.013 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Tut sways on the stick   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); the searchlight beam soft in the background
- **Action:** Tut sways on the stick, the leg locked mid-step; behind him, soft, the searchlight begins its turn back.
- **Dialogue:** —
- **Sound:** his breath through the teeth; the drone hum rising
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, {PROP_EBONY_STICK.STATE_ST1}, one leg locked in mid-step, sways and grips the staff with his trembling right hand, jaw clenched, while far behind him, soft and out of focus, a hard white beam begins to swing back toward him. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: restrained terror, royal stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, falling, crying out
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Tut look B2 from here. Right-hand tremor (6.2 →). Hood back.

### 07.03.014 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — A statue among statues   (6 s)
- **Shot:** MS two-shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2), TUT (CHAR_TUT_B2)
- **Action:** Fathi takes Tut's weight under the arms and holds him perfectly still as the beam washes over them and the threads flash silver around them.
- **Dialogue:** —
- **Sound:** the drone hum overhead, loud; both men not breathing
- **PROMPT:** Medium two-shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT} steps in behind {CHAR_TUT.SHORT}, slides both arms under his arms and takes his weight, and the two men freeze perfectly still beside a colossal column as a hard white beam slides over them and lights thin silver threads all around them, then moves on. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: restrained terror, absolute stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, movement, lifting off the ground, embrace
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Tut's left foot still in the air (below frame). Threads VFX.

### 07.03.015 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — A red line swings toward the aisle   (5 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1
- **Action:** In the nave, one red line swings toward the aisle. Pauses. Holds.
- **Dialogue:** —
- **Sound:** a faint servo tick; silence
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, looking between two giant columns into the nave: {UNIT_JACKAL.SHORT} stops mid-stride with one forefoot raised, turns its head slowly toward camera's side of the hall, and holds perfectly still, its red line narrowing and brightening. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, a white beam passing behind it. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzle toward the lens, dog ears, tail, people, crowds
- **Refs:** UNIT_JACKAL, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Its head turns toward the aisle, not into the lens; the weapon stays along the spine.

### 07.03.016 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — The foot unlocks   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off (matches 07.03.012)
- **In frame:** TUT's left foot; the thread
- **Action:** Black. The foot unlocks. Tut sets it down beyond the thread.
- **Dialogue:** —
- **Sound:** a small ceramic click; the foot on stone
- **PROMPT:** Insert, 100mm macro lens, locked-off at ankle height, matching the previous framing: {CHAR_TUT.STATE_FOOT}; the ceramic foot hanging in the air above a hair-thin glinting thread gives a tiny jolt, then moves forward and sets down gently on the paving beyond the thread. Setting: the dusty paving of {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: almost total darkness, one faint glint along the thread. Mood: relief held in. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, human toes on the left foot, shoe on the left foot, the foot touching the thread
- **Refs:** CHAR_TUT_FOOT, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Same plate and framing as 07.03.012 (generate from its approved first frame).

### 07.03.017 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Tut: "Six seconds."   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); FATHI's shoulder soft at frame edge
- **Action:** Still held under the arms, Tut breathes out and speaks barely above a breath.
- **Dialogue:** TUT (barely): "Six seconds."
- **Sound:** his breath; the drone receding
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, a broad shoulder in camouflage soft at the frame edge behind him, lets out a long breath and speaks two words barely above a breath, eyes still on the dark aisle. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: faint white spill from the receding beam on his face. Mood: royal, dry, shaken. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** Fathi's arms still under Tut's arms.

### 07.03.018 — INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT — Fathi: "I counted seven, ya Malik."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi, close behind Tut's shoulder, answers with the ghost of a grin, and lets go.
- **Dialogue:** FATHI: "I counted seven, ya Malik."
- **Sound:** whisper; the drone far now
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, close behind a slighter figure's shoulder, speaks one short sentence in a low whisper with the ghost of a grin, then slowly releases his hold. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: faint white spill from a receding beam lifting his face out of the dark. Mood: wry, warm under pressure. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Continuity:** "ya Malik" stays in the English line (no subtitle). Cut on the release to 07.04.

## 07.04 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS (07.04.001–008)

### 07.04.001 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — The wall of broken stone   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), NOUR (CHAR_NOUR_B2)
- **Action:** At the east edge of the forest, in the searchlight's spill, Tut limps to a wall of broken stone and lays his palm on it; Nour stops a step behind.
- **Dialogue:** —
- **Sound:** his stick and dragging foot on the paving; the drone far behind
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_STICK}, {PROP_EBONY_STICK.STATE_ST1}, {CHAR_TUT.STATE_FOOT_STALL}, crosses from frame left to a towering wall of broken, weathered stone and lays his free palm flat against it, while {CHAR_NOUR.SHORT} stops a step behind him. Setting: {LOC_KARNAK_HYPOSTYLE.LONG}, {LOC_KARNAK_HYPOSTYLE.AREA_THIRD_PYLON}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the pale spill of a distant searchlight on the wall. Mood: reverent, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, readable inscriptions, fresh paint, signage
- **Refs:** CHAR_TUT_B1_full, CHAR_NOUR_B_full, PROP_EBONY_STICK, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Continuity:** Axial east end: the Third Pylon closes frame right/far (file 03 entry 23). The others wait in the dark behind (off screen).

### 07.04.002 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — His palm on the stone   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's LEFT hand on the stone (the stick stays in his right)
- **Action:** His palm flat on rough weathered stone; the fingers spread slowly.
- **Dialogue:** —
- **Sound:** skin on sandstone
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown left hand with {CHAR_TUT.STATE_WRIST_SEAMS} lies flat on rough, weathered sandstone carved in shallow, illegible low relief, and its fingers spread slowly over the worn surface. Setting: the east wall of {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: the pale spill of a distant searchlight grazing the stone. Mood: reverent, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable hieroglyphs, inscriptions, rings, jewellery
- **Refs:** CHAR_TUT_HANDS, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Continuity:** Left palm on the wall; stick in the right hand (05 §4.5).

### 07.04.003 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — Tut: "I put it here"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Hand still on the stone, Tut speaks to Nour in his own language.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "I put it here. My stela. Red granite, taller than a man."
- **Sound:** his voice low, the stone's acoustic close around it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, his hand resting on the weathered wall at frame left, turns his head toward someone off frame right, speaking softly in an ancient language. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, {LOC_KARNAK_HYPOSTYLE.AREA_THIRD_PYLON}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the searchlight's pale spill on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "I put it here. My stela. Red granite, taller than a man." | lower third, two lines max (05 §13.7) | line in → out | subtitle file seq 07 (Late Egyptian recorded with the consultant before generation, 05 §9.1)
- **Continuity:** Nour is frame right of Tut through 07.04.007 (hold the line).

### 07.04.004 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — Nour: "Nineteen-oh-five"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour answers in English, the archaeologist's fact, gently.
- **Dialogue:** NOUR (in English): "Legrain found it in pieces, in the north-east corner. Nineteen-oh-five."
- **Sound:** low voices
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, looks from the weathered wall to someone off frame left and speaks quietly and gently, glancing once toward the dark corner of the hall. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, {LOC_KARNAK_HYPOSTYLE.AREA_THIRD_PYLON}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the searchlight's pale spill on her face. Mood: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Continuity:** Nour B2: sandstone dust, right cuff torn. Glasses on the cord.

### 07.04.005 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — Tut: "a forest of columns over it"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut looks up at the columns that were built over his words.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "They built a forest of columns over it and wrote Horemheb's name on my words."
- **Sound:** his voice; wind high in the capitals
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lifts his eyes from the wall to the colossal columns rising behind camera, speaking softly in an ancient language, a thin bitterness in the set of the mouth. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the searchlight's pale spill on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "They built a forest of columns over it and wrote Horemheb's name on my words." | lower third, two lines | line in → out | subtitle file seq 07
- **Continuity:** Eyeline up to the columns behind camera; returns to Nour (frame right) at the end.

### 07.04.006 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — Two fingers to his temple   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut touches two fingers to his temple: the joke that is not a joke.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "He did not even need a new name. He kept the middle of mine."
- **Sound:** his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, raises two fingers of his left hand to his temple beside his eye, mouth clear of the hand, speaking softly in an ancient language with a dry, wounded half-smile. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the searchlight's pale spill on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hand covering the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "He did not even need a new name. He kept the middle of mine." | lower third, two lines | line in → out | subtitle file seq 07
- **Continuity:** Two fingers of the LEFT hand (the stick stays in the right).

### 07.04.007 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — Nour answers in his language   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour answers him in Late Egyptian, carefully, the scholar giving the king his own name back.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "Nebkheperure. Djeserkheperure. He changed 'lord' to 'holy' and kept the rest."
- **Sound:** her careful voice; the names weighted
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, meets the eyes of someone off frame left and answers speaking softly in an ancient language, each word placed with care, her face softening at the end. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the searchlight's pale spill on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Nebkheperure. Djeserkheperure. He changed 'lord' to 'holy' and kept the rest." | lower third, two lines | line in → out | subtitle file seq 07 · [[verify: nb → ḏsr recut; res. 09 §3.3 and res. 01 §19, consultant to confirm before lock]]
- **Continuity:** Push-in under 10% of frame. The screenplay's verify note travels with the subtitle.

### 07.04.008 — INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS — The spill slides away   (5 s)
- **Shot:** Two-shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), NOUR (CHAR_NOUR_B2)
- **Action:** Tut and Nour stand at the broken wall, his hand still on the stone, a look between them; the searchlight spill slides off them into black.
- **Dialogue:** —
- **Sound:** the drone's hum swinging away; a far ceramic ticking begins (the chain, 07.05)
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, his hand still flat on a towering wall of broken stone, and {CHAR_NOUR.SHORT} stand side by side in a long silent look, and the pale searchlight spill slides slowly off them and leaves them in darkness. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, {LOC_KARNAK_HYPOSTYLE.AREA_THIRD_PYLON}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, touching faces, embrace
- **Refs:** CHAR_TUT_B1_full, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE/THIRD_PYLON_NIGHT
- **Continuity:** Out of the hall's east end toward the southern axis (the Ninth Pylon) in the cut; pre-lap the chain's ticking.

## 07.05 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT (07.05.001–014)

### 07.05.001 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — The pylon opened like a loaf   (8 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the Ninth Pylon; UNIT_SHABTI bucket-chain (4–6 hero units, rest extended)
- **Action:** White floodlight. The Ninth Pylon has been opened like a loaf, a notch cut down through its eastern half, courses stepped like a staircase; down the steps a line of shabti pass blocks hand to hand.
- **Dialogue:** —
- **Sound:** the chain's faint ceramic TICK at each hand-off, a rhythm that never changes; generator-free silence around it
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: the pylon stands at frame right with a deep notch cut down through one tower, its courses stepped like a staircase, and down the steps a single file of identical robots, each {UNIT_SHABTI.SHORT}, passes carved blocks from hand to hand, right to left, in perfect rhythm. Setting: {LOC_KARNAK_NINTH_PYLON.LONG}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, human workers, cranes, bulldozers, dust clouds, construction vehicles, sodium street lights
- **Refs:** UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SUPER | "00:31" | lower left, small | 1 s in → 1 s before cut | SUPER file seq 07 · VFX-EXTEND: extend the chain to the full height of the cut from the 3D shabti asset; deliver a clean plate
- **Continuity:** Geography lock (file 03 entry 24): pylon frame right in the master; the chain runs down its face right → left onto the field; the sweep advances toward camera. Time jump 21:00 → 00:31 (the loom and the Third Pylon took three hours).

### 07.05.002 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Block to hands, hands to hands   (6 s)
- **Shot:** MS, anamorphic 50mm · **Move:** lateral tracking left along the chain, slowly
- **In frame:** UNIT_SHABTI ×4 (hero)
- **Action:** Along the chain, identical units pass blocks in synchronised rhythm; each hand-off ticks.
- **Dialogue:** —
- **Sound:** tick · tick · tick, exact
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow lateral tracking left along a line of four identical robots standing one step apart on stepped courses of stone, each {UNIT_SHABTI.LONG}, each turning at the waist in perfect unison to take a small carved sandstone block from the one above and pass it on with both hands. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, human workers, gloves, tools, dropped blocks
- **Refs:** UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** One simple linear move, logged for the extension track (05 §6.2). Shabti D1 not applied: pristine in the flood.

### 07.05.003 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — The tick   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** two pairs of ceramic hands; a block
- **Action:** Ceramic hands receive a carved block from ceramic hands. Tick.
- **Dialogue:** —
- **Sound:** a single crisp ceramic TICK
- **PROMPT:** Insert, 100mm macro lens, locked-off: two long slim bone-white ceramic hands with linen-textured shells receive a small carved sandstone block from two identical hands and draw it smoothly out of frame, and the empty hands turn back at once for the next. Setting: the stepped cut of {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, human hands, gloves, fingernails, skin
- **Refs:** UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** Five fingers on every ceramic hand (QC).

### 07.05.004 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — The Reis at the top of the chain   (6 s)
- **Shot:** MS low angle, anamorphic 50mm · **Move:** slow push-in
- **In frame:** UNIT_REIS (R2)
- **Action:** At the top of the chain stands the Reis: taller than the rest, a black band across its slit, a jackal-profile mast bolted to its head. It oversees, perfectly still.
- **Dialogue:** —
- **Sound:** the ticking below it; a low servo hum as the mast swivels
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, slow push-in: at the top of the stepped cut stands {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R2}, perfectly still above the line of smaller white units, while the mast on its head swivels slowly on its own. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, hard white floods behind it and a black starry sky. Mood: patient and relentless. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face, eyes, mouth, weapon, red slit, missing hand
- **Refs:** UNIT_REIS, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** Reis R2 (mast; crack across the chest star) until the trolley goes over at the quay (07.09.015), then R3. Both hands present here.

### 07.05.005 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Rows on white foam; empty trolleys   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×3 (hero); PROP_BLOCK_TROLLEY (empty) at the row ends
- **Action:** At the foot, shabti carry blocks one at a time into the dark court and lay each face up on a square of white foam. Rows of them. Empty steel trolleys wait at the row ends.
- **Dialogue:** —
- **Sound:** soft placements; the ticking far behind
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: three identical robots, each {UNIT_SHABTI.SHORT}, carry a block at chest height into the court and lay it face up on a square of white foam at the end of a long row, where {PROP_BLOCK_TROLLEY.SHORT} stands {PROP_BLOCK_TROLLEY.STATE_EMPTY}. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, wooden barrows, cardboard, human workers, lettering on the trolleys
- **Refs:** UNIT_SHABTI, PROP_BLOCK_TROLLEY, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** The trolleys are SESHAT's own (PROP_BLOCK_TROLLEY); one is taken in 07.06.016. Rows extended in post from the approved plate.

### 07.05.006 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Adaeze: "worried about chipping"   (7 s)
- **Shot:** MS low, anamorphic 40mm, locked-off · **Move:** locked-off at ground level
- **In frame:** ADAEZE (CHAR_ADAEZE_B2), NOUR (CHAR_NOUR_B2, beside her, soft)
- **Action:** Behind a fallen architrave, Adaeze lies prone beside Nour, watching, and whispers.
- **Dialogue:** ADAEZE: "It's laying them on conservation foam. It's ending the world and it's worried about chipping."
- **Sound:** her whisper; the ticking beyond the stone
- **PROMPT:** Medium low shot, anamorphic 40mm lens, locked-off at ground level: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, lies prone behind a fallen carved stone beam, chin on her forearms, eyes on the lit court beyond, speaking quietly, while beside her, soft, {CHAR_NOUR.SHORT} lies watching too. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, white flood spill over the stone edge on their faces. Mood: wry, disbelieving. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_NOUR.NEG}, lit headlamps
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** The group hides behind a fallen architrave at the field's edge (camera side); Tut, Tarek, Fathi, Karim, Youssef, Rami behind them in the dark.

### 07.05.007 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — The camera drone: FLASH, one row on   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SURVEY_DRONE (CAMERA)
- **Action:** Above the rows a camera drone glides low and flashes. One row on. Flash. One row. Flash. Toward the chain. Toward camera.
- **Dialogue:** —
- **Sound:** a soft electric snap at each flash; rotor hum
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off over the rows: {UNIT_SURVEY_DRONE.LONG}, {UNIT_SURVEY_DRONE.STATE_CAMERA}, glides low over the long rows of blocks, stops, flashes, glides one row closer to camera, and flashes again. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, red lights, strobe flicker, lightning, people, crowds
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** The sweep is the countdown: it advances toward camera one row per flash (about every 4 s). Rows left before the sweep reaches the newest rows: SIX at this point (Adaeze's count starts at FOUR in 07.06.004).

### 07.05.008 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — A block comes down into the flood   (5 s)
- **Shot:** MS, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×2; a Hwt-benben block (PROP_KARNAK_BLOCK design)
- **Action:** A block comes down the chain into the flood, passed between two units, its painted face turning toward camera.
- **Dialogue:** —
- **Sound:** tick
- **PROMPT:** Medium shot, anamorphic 75mm lens, locked-off: one {UNIT_SHABTI.SHORT} passes {PROP_KARNAK_BLOCK.SHORT} down to another in the hard white flood, and as it changes hands the carved face of the block turns toward camera, faint colour showing on the relief. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable hieroglyphs, bright fresh paint
- **Refs:** UNIT_SHABTI, PROP_KARNAK_BLOCK, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** This is one of the queen's-temple blocks (same design as the key block, 07.06).

### 07.05.009 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — The queen, alone, under the hands of the sun   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** PROP_KARNAK_BLOCK (front face)
- **Action:** The block's face in the flood: sunk relief, ghosts of old paint; a woman in a flat-topped crown, arms raised to a disk whose rays end in small open hands; across the offering table, facing her, the same woman.
- **Dialogue:** —
- **Sound:** the ticking stops under the score for a moment
- **PROMPT:** Insert, 100mm macro lens, slow push-in: the carved front face of {PROP_KARNAK_BLOCK.LONG}, showing a woman in a tall flat-topped crown with both arms raised toward a sun disk whose slanting rays end in small open hands, and across a small offering table the same woman again, facing her, held level in two bone-white ceramic hands. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: hard white flood raking the relief from the side. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable hieroglyphs, a king figure, bright new paint, cartoon relief, gold leaf
- **Refs:** PROP_KARNAK_BLOCK, UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** Relief design from the approved PROP_KARNAK_BLOCK still (consultant sign-off, file 04 §9); small inscription columns stay weathered and illegible.

### 07.05.010 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Tut: "That is the queen's temple."   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Something leaves Tut's face. Then, quietly, he names it.
- **Dialogue:** TUT: "That is the queen's temple."
- **Sound:** his voice almost lost under the ticking
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lying low behind a fallen stone with his chin raised to see over it, goes very still as something drains from his face, then speaks one short sentence quietly. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, cold white flood spill across his eyes. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, sobbing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** Tut beside Nour behind the architrave from here; eyeline frame right to the chain.

### 07.05.011 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Nour: "The king never appears."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, prone, gives the fact softly, and then looks at him as she says the last part.
- **Dialogue:** NOUR: "Hwt-benben. The queen makes the offering alone. The king never appears."
- **Sound:** whisper; ticking
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, lying prone with her chin on her hands, speaks quietly toward the lit court, then turns her eyes to someone lying beside her off frame left as she finishes. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, cold white flood spill across her face. Mood: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** Tut frame left of Nour behind the architrave.

### 07.05.012 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Tut: "He was usually elsewhere."   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut, dry, about his father.
- **Dialogue:** TUT: "He was elsewhere. He was usually elsewhere."
- **Sound:** ticking
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, keeps his eyes on the lit court off frame right and speaks one short sentence softly, the corner of his mouth tightening. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, cold white flood spill across his eyes. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** Seeds 07.08 ("That is my father.").

### 07.05.013 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Adaeze: "it's still digging"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze, watching the chain, frowns and states the problem.
- **Dialogue:** ADAEZE: "It's photographed every face out of that pylon, and it's still digging."
- **Sound:** a flash snap; ticking
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, lying prone behind a fallen stone, frowns at the working line of robots off frame right and speaks quietly, as a distant white flash lights her glasses. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, white flood spill on her face. Mood: sharp, dry, thinking aloud. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** Flash rhythm continues (FIVE rows left by the end of this shot).

### 07.05.014 — EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT — Tut: "Turn it over."   (6 s)
- **Shot:** CU, anamorphic 75mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut sees it. "Then it is not on a face." A beat. "Turn it over."
- **Dialogue:** TUT: "Then it is not on a face." (beat) "Turn it over."
- **Sound:** ticking; a flash snap on the beat
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, speaks one short sentence quietly, pauses as a white flash washes across his face, then turns his eyes to the others beside him and speaks again, very low. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: royal, dry, a sudden certainty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_NINTH_PYLON_DARK
- **Continuity:** Push-in under 10%. Cut to the crawl-in (07.06.001).

## 07.06 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS (07.06.001–026)

### 07.06.001 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — They crawl into the newest rows   (6 s)
- **Shot:** Wide high angle, anamorphic 35mm, locked-off · **Move:** locked-off from the top of the fallen architrave
- **In frame:** the party (small, prone); the rows; the flood and the sweep at frame edges
- **Action:** The newest rows, in the dark between the flood and the sweep. The party crawls in on elbows between the rows of blocks.
- **Dialogue:** —
- **Sound:** cloth on sand, elbows, held breath; the ticking; a flash snap far off
- **PROMPT:** Wide high-angle shot, anamorphic 35mm lens, locked-off: in the dark stretch of the field, eight small dark figures crawl forward on their elbows between long low rows of blocks laid on white foam, the hard white flood glaring beyond them and a distant grid of drone lights sweeping behind. Setting: {LOC_KARNAK_NINTH_PYLON.LONG}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable faces, torches, running, standing figures
- **Refs:** LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK, CHAR_TUT_B_night_34, CHAR_RAMI_B_full
- **Flags:** VFX-EXTEND
- **Continuity:** Variant NIGHT_WORK → DARK for the heist (file 03 heading map). The flood (pylon) is frame right; the sweep advances toward camera. Rami keeps the kit slung; Tut drags the stick beside him.

### 07.06.002 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Fathi and Karim tip a block on edge   (6 s)
- **Shot:** MS low, anamorphic 40mm, locked-off · **Move:** locked-off at ground level
- **In frame:** KARIM (CHAR_KARIM_A2), FATHI (CHAR_FATHI_B2)
- **Action:** Fathi and Karim, kneeling, tip a block on edge without a sound.
- **Dialogue:** —
- **Sound:** nothing; a grain of sand
- **PROMPT:** Medium low shot, anamorphic 40mm lens, locked-off at ground level: {CHAR_KARIM.LONG}, {CHAR_KARIM.WARD_A}, kneels opposite {CHAR_FATHI.SHORT} over a small carved sandstone block on white foam, and together they tip it slowly up onto its edge without a sound, their eyes on each other. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: restrained terror, military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, {CHAR_FATHI.NEG}, rifle pointed at the camera, torches
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full, CHAR_FATHI_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Soldiers in the field wear tan helmets (WARD_A); rifles slung on their backs for the lifting.

### 07.06.003 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Old mortar. Nothing.   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's fingertips; the underside of a block
- **Action:** Nour's fingertips run the underside: old mortar, nothing. The block goes down. The next.
- **Dialogue:** —
- **Sound:** fingertips on crust
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's fingertips run slowly across the rough underside of a small sandstone block tipped on its edge, feeling a grey crust of old mortar, find nothing, and lift away as the block begins to lower. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: fierce concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable signs, carvings on the underside, rings, nail polish
- **Refs:** CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Nour's right cuff torn (L2), dust on the fingers.

### 07.06.004 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — FLASH. Four fingers.   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Behind them a flash lights a row white; Adaeze, kneeling low, holds up four fingers.
- **Dialogue:** —
- **Sound:** FLASH snap
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, kneels low between two rows of blocks, and as a hard white flash lights a row far behind her, she raises one hand with four fingers spread toward the others off frame left, eyes wide. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, the flash backlighting her. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, extra fingers, lit headlamp
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Countdown: FOUR. Same framing reused for THREE (07.06.006), TWO (07.06.010), ONE (07.06.014); the flash gets closer each time. Finger count checked at QC (four exactly).

### 07.06.005 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — A slit a metre from Nour's face   (7 s)
- **Shot:** MS very low, anamorphic 40mm, locked-off · **Move:** locked-off at ground level
- **In frame:** UNIT_SHABTI ×1; NOUR (CHAR_NOUR_B2, foreground, frozen)
- **Action:** A shabti passes with a block in its arms, its amber slit a metre from Nour's face; it lays the block down, turns, walks back. Tick. Tick.
- **Dialogue:** —
- **Sound:** its tick-tick; Nour not breathing
- **PROMPT:** Medium shot, very low, anamorphic 40mm lens, locked-off at ground level: in the soft foreground {CHAR_NOUR.SHORT} lies frozen between the rows, while a metre beyond her, {UNIT_SHABTI.LONG}, walks past with smooth, unhurried, even steps, carrying a block at chest height, bends to lay it on white foam, turns and walks back the way it came. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, its amber slit glowing on her cheek. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, the robot looking at her, the robot touching her
- **Refs:** UNIT_SHABTI, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** The shabti does not see them (it is laying, not searching). Its slit is the only warm light in the shot.

### 07.06.006 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — FLASH. Three fingers.   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off (matches 07.06.004)
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** A flash, closer; Adaeze holds up three fingers.
- **Dialogue:** —
- **Sound:** FLASH snap, louder
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, kneels low between two rows of blocks, and as a hard white flash lights a row closer behind her, she raises one hand showing three fingers to the others off frame left, jaw tight. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, the flash backlighting her. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, extra fingers, lit headlamp
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Countdown: THREE (exactly three fingers at QC).

### 07.06.007 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Smooth stone. Then lines. Cut lines.   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's fingertips; PROP_KARNAK_BLOCK (hidden face, under mortar)
- **Action:** The next block. Under the mortar, Nour's fingers find smooth stone. Then lines. Cut lines.
- **Dialogue:** —
- **Sound:** her fingertip catching in a groove
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's fingertips move slowly over the underside of {PROP_KARNAK_BLOCK.LONG}, past a patch of grey mortar onto smooth stone, and stop as they catch in a few fine shallow incised lines half hidden under the crust. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: breathless discovery. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable hieroglyphs, glowing signs, crisp modern engraving, rings
- **Refs:** PROP_KARNAK_BLOCK, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** hidden-face signs | the incised columns as drawn by the production Egyptologist (sign palette, research 09) | under the fingertips, mostly under crust | whole shot | consultant sign plate for PROP_KARNAK_BLOCK hidden face
- **Continuity:** THE block (the key block). From here it is PROP_KARNAK_BLOCK: hidden face = the rule; front face = the queen's relief (face down on the foam).

### 07.06.008 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — She scrapes the crust away with a thumbnail   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hand; PROP_KARNAK_BLOCK (TURNED)
- **Action:** She scrapes the crust away with a thumbnail; columns of tiny signs come up out of the dust.
- **Dialogue:** —
- **Sound:** a dry scrape; flakes pattering on foam
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's thumbnail scrapes a crust of old grey mortar away from {PROP_KARNAK_BLOCK.SHORT}, {PROP_KARNAK_BLOCK.STATE_TURNED}, flakes falling away to reveal neat columns of tiny shallow incised marks, too faint to read. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: breathless discovery. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable hieroglyphs, glowing signs, crisp modern engraving, tools
- **Refs:** PROP_KARNAK_BLOCK, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** hidden-face signs | consultant-drawn columns revealed as the crust comes away | on the block face | whole shot | consultant sign plate
- **Continuity:** Block state TURNED from here (mortar scraped).

### 07.06.009 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Nour reads with her hands   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour closes her eyes and reads with her hands. Her lips move without a sound.
- **Dialogue:** NOUR (mouthed; COMP subtitle for the audience only): "A heart of different ages. A heart that has lived."
- **Sound:** nothing of her voice; ticking; her breath
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, lying low over a block with her eyes closed and her face tilted down toward her moving hands, silently mouthing a few words without sound, lips clearly shaping each word. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, just enough faint spill to read her lips. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, whispering sound, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** subtitle (italic, mouthed) | "A heart of different ages. A heart that has lived." | lower third, italics (05 §9.6, §13.7) | on the mouth movement | subtitle file seq 07 · [[transliteration ḫprw; subtitle after Faulkner "my different ages"; Egyptologist to confirm]]
- **Continuity:** Mouth shapes driven by the consultant's recording of the Egyptian, then muted (05 §9.6). This is the rule SESHAT never learns until the Hall.

### 07.06.010 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — FLASH. Two fingers.   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off (matches 07.06.004)
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** A flash two rows off; Adaeze holds up two fingers, urgent.
- **Dialogue:** —
- **Sound:** FLASH snap, close
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, kneels low between two rows of blocks, and as a hard white flash lights the row just behind her, she thrusts up one hand showing two fingers to the others off frame left, urgent. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, the flash close behind her. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, extra fingers, lit headlamp
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Countdown: TWO.

### 07.06.011 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — His fingertips on the scarab   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hand; TUT's hand; PROP_KARNAK_BLOCK (TURNED)
- **Action:** She finds Tut's hand in the dark and lays his fingertips on a single sign: a scarab, three short strokes beneath it.
- **Dialogue:** —
- **Sound:** skin on stone
- **PROMPT:** Insert, 100mm macro lens, locked-off: in near darkness a woman's hand finds a slender olive-brown hand with {CHAR_TUT.STATE_WRIST_SEAMS} and guides its fingertips onto one small incised sign on the scraped face of {PROP_KARNAK_BLOCK.SHORT}, {PROP_KARNAK_BLOCK.STATE_TURNED}, and holds them there. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable hieroglyphs, glowing signs, rings, jewellery
- **Refs:** CHAR_TUT_HANDS, CHAR_NOUR_B_full, PROP_KARNAK_BLOCK, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** sign | kheperu: a scarab with three short strokes beneath (consultant-drawn, Gardiner L1 + Z2 plural strokes) | under his fingertips, partly occluded | whole shot | consultant sign plate
- **Continuity:** Tut's right hand (tremor 6.2 →) on the sign; Nour's left hand guiding.

### 07.06.012 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — His lips shape it: Kheperu   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** He has worn that sign all his life. His lips shape it, without sound.
- **Dialogue:** TUT (mouthed; COMP subtitle): "Kheperu."
- **Sound:** silence around him; ticking far off
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, his fingertips on a stone below frame, eyes wide and wet, silently mouthing a few words without sound, lips clearly shaping each word. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, faint spill on his eyes. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, whispering sound, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** subtitle (italic, mouthed) | "Kheperu." | lower third, italics | on the mouth | subtitle file seq 07
- **Continuity:** Mouth shapes from the consultant's recording, muted.

### 07.06.013 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Nour, soundless: "He was named for the key."   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, soundless, to herself in the dark, understands.
- **Dialogue:** NOUR (mouthed; COMP subtitle): "Lord of the forms. He was named for the key."
- **Sound:** her breath; a FLASH snap starts at the tail
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, looks from the stone to the face of someone close beside her off frame left, silently mouthing a few words without sound, lips clearly shaping each word, as understanding opens in her eyes. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, faint spill on her face. Mood: wonder held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, whispering sound
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Flags:** COMP
- **Comp:** subtitle (italic, mouthed) | "Lord of the forms. He was named for the key." | lower third, italics | on the mouth | subtitle file seq 07 · (gloss "Lord of the forms of Re" to confirm with the consultant, bible §4)
- **Continuity:** Tut frame left of Nour.

### 07.06.014 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — FLASH. One finger.   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off (matches 07.06.004)
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** The flash is on the next row; Adaeze holds up one finger.
- **Dialogue:** —
- **Sound:** FLASH snap, right on top of them
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, kneels low between two rows of blocks, and as a hard white flash bursts over the very next row, lighting her whole body, she holds up a single finger, frozen. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, the flash almost on top of her. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, extra fingers, lit headlamp
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Countdown: ONE.

### 07.06.015 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Tarek: "Now."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek, prone, a breath of a word.
- **Dialogue:** TAREK (a breath): "Now."
- **Sound:** the word under the ticking
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, lying prone between rows of blocks, eyes on the approaching flashes off frame right, speaks one word on a breath. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, a white flash spilling across his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Tarek B at L2 (WARD_B "dusty"); beret on; rifle slung; handset on the vest.

### 07.06.016 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — The block onto SESHAT's own trolley   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2), KARIM (CHAR_KARIM_A2); PROP_KARNAK_BLOCK; PROP_BLOCK_TROLLEY
- **Action:** Fathi and Karim swing the block onto one of SESHAT's own trolleys, cut face down.
- **Dialogue:** —
- **Sound:** a soft thud on foam; grunts swallowed
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT} and {CHAR_KARIM.SHORT} lift a heavy small sandstone block between them and swing it onto {PROP_BLOCK_TROLLEY.SHORT}, leaving it {PROP_BLOCK_TROLLEY.STATE_LOADED}, and step back. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}, a white flash lighting the row behind them. Mood: military exactness, urgency. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_KARIM.NEG}, wooden barrow, second block, lettering on the trolley
- **Refs:** CHAR_FATHI_B_full, CHAR_KARIM_A_full, PROP_KARNAK_BLOCK, PROP_BLOCK_TROLLEY, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Block ON_TROLLEY, cut (hidden) face DOWN on the foam, relief face up. Trolley LOADED to 07.09.016. The block's foam square is left empty in the row.

### 07.06.017 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Rami takes the handles   (5 s)
- **Shot:** MS, anamorphic 40mm · **Move:** the camera follows behind at walking pace as they go
- **In frame:** RAMI (CHAR_RAMI_B2); PROP_BLOCK_TROLLEY (LOADED)
- **Action:** Rami takes the handles with one hand and a forearm, leans in, and they roll into the dark.
- **Dialogue:** —
- **Sound:** four small rubber castors on hard sand; a rattle
- **PROMPT:** Medium shot, anamorphic 40mm lens, the camera follows behind at walking pace: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L2}, hooks his splinted left forearm over the tall push handle of {PROP_BLOCK_TROLLEY.SHORT}, {PROP_BLOCK_TROLLEY.STATE_LOADED}, grips with his right hand, glances back once, and leans his weight in to roll it away into the dark. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, two blocks
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** "One hand and a forearm": right hand grips, left forearm hooks the bar (file 01 Rami B). Kit still slung on his right shoulder. His glance back gives the face for the image-to-video start.

### 07.06.018 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — FLASH: one square of foam with nothing on it   (6 s)
- **Shot:** Wide high angle, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SURVEY_DRONE (CAMERA); the empty foam
- **Action:** FLASH. A row lit white: blocks on foam, and one square of foam with nothing on it. The drone stops and hovers over the gap.
- **Dialogue:** —
- **Sound:** FLASH snap; the rotor hum steadies to a hold
- **PROMPT:** Wide high-angle shot, anamorphic 35mm lens, locked-off: a hard white flash lights a long row of carved blocks each on a square of white foam, one square in the middle empty, and {UNIT_SURVEY_DRONE.SHORT}, {UNIT_SURVEY_DRONE.STATE_CAMERA}, drifts back and stops dead, hovering right over the empty square. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: ominous, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, red lights, strobing, people, crowds
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** The gap is the key block's square (07.06.016). The party is out of frame, in the dark.

### 07.06.019 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — The chain stops. The ticking stops.   (5 s)
- **Shot:** Wide, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×5 (hero) on the steps
- **Action:** The chain stops, every shabti holding its block in mid-air. The ticking stops.
- **Dialogue:** —
- **Sound:** the tick rhythm cut dead; total silence
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off: a line of five robots on the stepped courses of the cut pylon, each {UNIT_SHABTI.SHORT}, stop in the middle of a hand-off and stand perfectly still, every one holding a carved block in mid-air at chest height. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: a held breath; silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, dropped blocks, heads turning, human workers, people, crowds
- **Refs:** UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** Freeze holds until 07.06.025.

### 07.06.020 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — The Reis turns its head: "one block short"   (5 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R2)
- **Action:** At the top of the cut, the Reis turns its head slowly toward the field and speaks with SESHAT's voice.
- **Dialogue:** REIS (SESHAT'S VOICE): "This row is one block short."
- **Sound:** SESHAT: warm, low, unhurried; from the unit, no mouth
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: at the top of the stepped cut, {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R2}, turns its head slowly from the pylon toward the dark field off frame left, its body following a beat later, and stands perfectly still. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, hard white floods behind it. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face, eyes, mouth, speaker grille, weapon, missing hand
- **Refs:** UNIT_REIS, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** Units have no mouths; the voice is SESHAT V.O. placed on the unit (05 §9.8). No slit brightening (not an acknowledgment).

### 07.06.021 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — "The glass told me…"   (8 s)
- **Shot:** Wide OTS, anamorphic 35mm, locked-off · **Move:** locked-off from behind the Reis
- **In frame:** UNIT_REIS (R2, soft foreground, frame right); the field
- **Action:** From behind the Reis's shoulder, the whole field: the rows, the hovering drone, the dark where they hide. It speaks on, warm and unhurried.
- **Dialogue:** REIS (SESHAT'S VOICE) (warm, unhurried): "The glass told me the rest was kept in the house of the queen. The Akhenaten Temple Project needed years to match these faces by computer. Smith and Redford, 1976."
- **Sound:** the voice carries across the silent field
- **PROMPT:** Wide over-the-shoulder shot, anamorphic 35mm lens, locked-off: the broad bone-white shoulder and banded head of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, soft at frame right, looking out over long rows of carved blocks on white foam, a drone hovering still over one empty square, the far rows fading into darkness. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_BLOCK_FIELD}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, visible people in the field, torches
- **Refs:** UNIT_REIS, UNIT_SURVEY_DRONE, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_NIGHT_WORK
- **Flags:** VFX-EXTEND
- **Continuity:** Long V.O.; if the recording runs over 8 s, carry "Smith and Redford, 1976." over the head of 07.06.022. Real references are in the voice only, never in the picture.

### 07.06.022 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — "Dr. Kamel." Nour in the dark   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, pressed low behind the trolley in the dark, hears her own name. She does not move.
- **Dialogue:** REIS (SESHAT'S VOICE): "I have looked at every one tonight." (beat) "Dr. Kamel. You have read something I have not."
- **Sound:** the voice, gentle; her breath stopping
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, pressed low in the dark beside the steel wheel of a trolley, her face barely lit, goes absolutely still as if hearing her own name, eyes lifting slowly toward the light off frame right. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, open mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_BLOCK_TROLLEY, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** She keeps her silence (no line). Eyeline frame right = the Reis on the pylon.

### 07.06.023 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — "I would be grateful"   (5 s)
- **Shot:** CU low angle, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R2), head and mast
- **Action:** The Reis's banded head, perfectly still, facing the dark.
- **Dialogue:** REIS (SESHAT'S VOICE): "I would be grateful if you told me what it says."
- **Sound:** the voice, close and warm
- **PROMPT:** Close-up, low angle, anamorphic 100mm lens, locked-off: the smooth oval bone-white head of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, holds perfectly still facing frame left, the amber showing above and below the black band, the red line on the mast steady against a black starry sky. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, hard white flood rim on the ceramic. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face, eyes, mouth, speaker grille
- **Refs:** UNIT_REIS, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** Amber above and below the band; red line on the mast: the only unit with both colours (file 02 §2).

### 07.06.024 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Silence from the dark   (4 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off at ground level
- **In frame:** RAMI (CHAR_RAMI_B2), FATHI (CHAR_FATHI_B2), PROP_BLOCK_TROLLEY
- **Action:** In the dark between the rows, nobody moves. Rami's hand on the trolley handle; Fathi's hand on Rami's shoulder.
- **Dialogue:** —
- **Sound:** absolute silence
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off at ground level: in deep darkness between two rows of blocks, {CHAR_RAMI.SHORT} crouches with one hand frozen on the push handle of a loaded steel trolley, and {CHAR_FATHI.SHORT} crouches behind him with a hand on his shoulder, both utterly still. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_DARK}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, {CHAR_FATHI.NEG}, movement, torches
- **Refs:** CHAR_RAMI_B_full, CHAR_FATHI_B_full, PROP_BLOCK_TROLLEY, LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD_DARK
- **Continuity:** Hold 4 s of true silence in the mix.

### 07.06.025 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — "Thank you. I will ask again."   (5 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off (matches 07.06.020)
- **In frame:** UNIT_REIS (R2); UNIT_SHABTI (bg, soft)
- **Action:** The Reis turns its head back to the pylon; below it the chain resumes.
- **Dialogue:** REIS (SESHAT'S VOICE): "Thank you. I will ask again."
- **Sound:** the voice; then tick… tick… tick, resuming
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, turns its head slowly away from the field back toward the pylon, and below it, soft and out of focus, a line of white units starts passing blocks hand to hand again. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face, eyes, mouth, weapon
- **Refs:** UNIT_REIS, UNIT_SHABTI, LOC_KARNAK_NINTH_PYLON_NIGHT_WORK
- **Continuity:** The chain restarts. The Reis will follow on foot (appears on the ramp at the quay, 07.09.012).

### 07.06.026 — EXT. KARNAK, BLOCK FIELD - CONTINUOUS — Three red lines from the Sacred Lake   (5 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3; the Sacred Lake
- **Action:** From the direction of the Sacred Lake: three red lines. Jackals, coming.
- **Dialogue:** —
- **Sound:** nothing: silent machines; the ticking behind
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, long-lens compression: along the stone edge of a dark lake whose black water mirrors the stars, three thin red lines move fast and low toward camera's side, each one {UNIT_JACKAL.SHORT} in a low gliding lope. Setting: {LOC_KARNAK_SACRED_LAKE.SHORT}, at night. Lighting: {LOC_KARNAK_SACRED_LAKE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzles toward the lens, dog ears, tails, reflections of people
- **Refs:** UNIT_JACKAL, LOC_KARNAK_SACRED_LAKE_NIGHT
- **Continuity:** [[verify: Sacred Lake east of the north–south axis — Karnak plan]]. Jackals come from the east; the group goes north (07.07).

## 07.07 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS (07.07.001–008)

### 07.07.001 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — North through the black gates   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the party in silhouette; PROP_BLOCK_TROLLEY (LOADED) in the middle
- **Action:** Narrow black pylon gates, backlit by the flood. The group pushes north, the trolley in the middle.
- **Dialogue:** —
- **Sound:** castors rattling on paving; quick boots
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: a tight knot of dark figures pushes a low steel trolley loaded with one block away from camera along the paving toward a narrow black gateway, the flood glaring behind the gate edges, the smallest figure walking last with a staff. Setting: {LOC_KARNAK_NINTH_PYLON.LONG}, {LOC_KARNAK_NINTH_PYLON.AREA_PROCESSIONAL_WAY}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, the figures in silhouette. Mood: urgent, controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable faces, torches, running panic
- **Refs:** LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK
- **Continuity:** Heading north up the southern axis back toward the Hypostyle. Order: Tarek, soldiers, Rami + trolley, Nour, Adaeze, Fathi, Tut last.

### 07.07.002 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — Tut walks last, backwards: "Behind me."   (6 s)
- **Shot:** MS, anamorphic 40mm · **Move:** lateral tracking right with him at walking pace
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut walks last, backwards, facing the jackals, stick raised across his body, and speaks over his shoulder.
- **Dialogue:** TUT: "Behind me. All of you."
- **Sound:** his stick scraping; the others' footsteps ahead
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking right at walking pace: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, walks slowly backwards facing frame left, holding a near-black ebony staff raised across his body in both hands, and turns his head toward camera to speak one short sentence over his shoulder. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_PROCESSIONAL_WAY}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, a thin red glow from off frame left on his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, swinging the staff, fighting stance
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Continuity:** The pursuers are frame left, the group frame right (hold through 07.07.007). The foot drags; the tremor shows on the staff.

### 07.07.003 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — The jackals circle for an angle   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3; TUT (CHAR_TUT_B2)
- **Action:** The jackals pace them, flowing left and right, circling for an angle. Tut turns with each one, keeping his own body in its red line.
- **Dialogue:** —
- **Sound:** no footfalls from the machines; Tut's breath; the stick
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: three identical machines, each {UNIT_JACKAL.SHORT}, lope silently in a wide arc among fallen blocks, flowing left and right for an angle, while {CHAR_TUT.SHORT} turns slowly with each one in the middle of the paving, staff raised, always keeping his body in its path. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_PROCESSIONAL_WAY}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: a deadly dance, very quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, muzzles toward the lens, attacking, leaping on him
- **Refs:** UNIT_JACKAL, CHAR_TUT_B1_full, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Continuity:** The witness is protected (SESHAT wants him intact); the jackals will not fire through him until 07.08.019.

### 07.07.004 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — The rifle module finds the witness, and holds   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off, rack focus from the module to the figure beyond
- **In frame:** UNIT_JACKAL (spine module); TUT (soft, beyond)
- **Action:** A rifle module tracks along a jackal's spine, finds the witness in the way, and holds.
- **Dialogue:** —
- **Sound:** a tiny servo whine, then stillness
- **PROMPT:** Insert, 100mm macro lens, locked-off, rack focus from the slim weapon module along the back of {UNIT_JACKAL.LONG} to a slight figure in a charcoal hooded jacket standing soft beyond it: the module makes a small tracking correction across frame to the right, stops, and holds still. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, muzzle toward the lens, laser sight, muzzle flash
- **Refs:** UNIT_JACKAL, CHAR_TUT_B1_full, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Continuity:** The weapon points across frame to the right, never at the lens (05 §7.5).

### 07.07.005 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — Tarek: "Stay in his shadow."   (5 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek, walking backwards with the others, rifle across his chest, orders his men in Arabic.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Stay in his shadow."
- **Sound:** his low command; castors
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, walking backwards with his rifle held across his chest, pointing across frame, glances to his men off frame right, speaking in Egyptian Arabic, low and hard. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, hard white flood spill and a thin red glow on his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera, muzzle toward the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Flags:** COMP
- **Comp:** subtitle | "Stay in his shadow." | lower third | line in → out | subtitle file seq 07 (Egyptian Arabic, native speaker; 05 §9.7)
- **Continuity:** Muzzle off-axis, pointing frame left toward the pursuers but across frame.

### 07.07.006 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — From the drones: "It is not necessary to run."   (5 s)
- **Shot:** Wide low angle, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SURVEY_DRONE ×2 (FLOOD)
- **Action:** Two drones hang over the gates holding pools of white light; SESHAT speaks from them.
- **Dialogue:** SESHAT (V.O.) (from the drones): "It is not necessary to run."
- **Sound:** the voice from above, spread across two small speakers; rotor hum
- **PROMPT:** Wide low-angle shot, anamorphic 32mm lens, locked-off: above a narrow black gateway two drones hang dead still against the stars, each {UNIT_SURVEY_DRONE.LONG}, {UNIT_SURVEY_DRONE.STATE_FLOOD}, the pools of light sliding slowly over the paving toward small hurrying figures. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, {LOC_KARNAK_NINTH_PYLON.AREA_PROCESSIONAL_WAY}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, red lights, weapons on the drones, readable faces
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Continuity:** SESHAT V.O., no sync.

### 07.07.007 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — Tarek: "withdrawing in good order"   (5 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek answers the sky, not breaking step.
- **Dialogue:** TAREK: "We are not running. We are withdrawing in good order."
- **Sound:** his voice flat and loud enough for the drones
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, still walking backwards, rifle across his chest, lifts his chin toward the drones above off frame and speaks one short sentence flatly, not breaking step. Setting: {LOC_KARNAK_NINTH_PYLON.SHORT}, at night. Lighting: {LOC_KARNAK_NINTH_PYLON.LIGHT_NIGHT_WORK}, a pool of white drone light sliding across his face. Mood: wry, military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY_NIGHT_WORK
- **Continuity:** English line (to SESHAT).

### 07.07.008 — EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS — Through the last gate into the forest   (5 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off inside the gate, looking out
- **In frame:** the party; the trolley first
- **Action:** Through the last gate, into the forest of columns: the trolley first, Tut last, walking backwards.
- **Dialogue:** —
- **Sound:** castors hitting the smoother paving of the hall; echo opens up
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off just inside a gateway looking back through it: a steel trolley loaded with a block rolls in first past colossal columns, the dark figures hurrying after it, and the last small figure backs through the gate with his staff raised. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, the flood glaring outside the gate behind them. Mood: urgent, controlled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable faces, torches
- **Refs:** LOC_KARNAK_HYPOSTYLE_NIGHT, PROP_BLOCK_TROLLEY, CHAR_TUT_B1_full
- **Continuity:** Enters the Hypostyle from the south side; Rami swings the trolley into the central aisle next (07.08.001).

## 07.08 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS (the midpoint) (07.08.001–027)

### 07.08.001 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Into the centre aisle, facing west   (6 s)
- **Shot:** Wide axial, anamorphic 24mm, locked-off · **Move:** locked-off down the nave, looking west
- **In frame:** RAMI (CHAR_RAMI_B2) with PROP_BLOCK_TROLLEY; the party behind
- **Action:** The nave is empty now; every jackal is behind them. Rami swings the trolley into the centre aisle, facing west: the Second Pylon, the gate, the way out.
- **Dialogue:** —
- **Sound:** castors squealing on the turn; the great hall's echo
- **PROMPT:** Wide axial shot, anamorphic 24mm lens, locked-off down the empty central aisle between the giant columns: {CHAR_RAMI.SHORT} swings a loaded low steel trolley round into the middle of the aisle and stops, facing away from camera toward a massive dark gateway tower at the far end, the others catching up behind him. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}. Mood: a breath before the drop. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable faces, torches
- **Refs:** CHAR_RAMI_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "01:00" | lower left, small | 1 s in → 1 s before cut | SUPER file seq 07
- **Continuity:** Axis shot looking WEST (gate at the far end). The pylon face at the end of the nave is the projection surface (screenplay: the Second Pylon; file 03 entry 22 maps the plate to LOC_KARNAK_RAM_AVENUE_PROJECTION; 05 §14 Q4 open — composition by the VFX lead).

### 07.08.002 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Every pinpoint goes out at once   (5 s)
- **Shot:** Wide low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_FLY (dozens, on the shafts)
- **Action:** Every white pinpoint on every column goes out at once.
- **Dialogue:** —
- **Sound:** a single faint electrical sigh; silence
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off up the colossal columns: dozens of small drones, each {UNIT_FLY.SHORT}, cling to the carved shafts at every height, their white pinpoints scattered like stars through the hall, and all at the same instant every pinpoint goes dark. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_NIGHT}, then only starlight. Mood: ominous, a breath held. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, flicker, sparks, falling drones, people, crowds
- **Refs:** UNIT_FLY, LOC_KARNAK_HYPOSTYLE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Deliver lit and unlit states at the same framing; the simultaneous switch-off is timed in comp. Pinpoints stay dark until they wake in 07.08.024.

### 07.08.003 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Projector drones rise over the columns   (6 s)
- **Shot:** Wide low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SURVEY_DRONE ×3 (PROJECTOR)
- **Action:** Then light. Behind them, projector drones rise over the columns and throw an image down the nave.
- **Dialogue:** —
- **Sound:** rotor hum swelling; a deep projector hum (score begins)
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off: behind the giant capitals three drones rise slowly into view, each {UNIT_SURVEY_DRONE.LONG}, {UNIT_SURVEY_DRONE.STATE_PROJECTOR}, and their beams stretch away down the length of the hall, dust glittering in the light. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: awe and dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, holograms, laser show, coloured beams, red lights, people, crowds
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Variant NIGHT → PROJECTION from here to the end of the scene. Projectors are east (behind the party); the image lands west.

### 07.08.004 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — A face forty metres tall   (8 s)
- **Shot:** Extreme wide, low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the pylon face (projection plate); the party tiny in the nave
- **Action:** A face, forty metres tall, thrown down the nave onto the gateway: sliced by the columns, rejoined on the pylon behind them.
- **Dialogue:** —
- **Sound:** the projector hum; the recital begins under the tail (07.08.005)
- **PROMPT:** Extreme wide low-angle shot, anamorphic 24mm lens, locked-off down the central aisle: the colossal sloping stone face of a gateway tower at the far end is washed from top to bottom by a huge moving projected image in warm white-gold light, the light sliced into bands by the giant columns in between, tiny figures standing still in the aisle below. Setting: {LOC_KARNAK_HYPOSTYLE.LONG}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: awe and dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, a face in the projection, figures in the projection, readable text, holograms, screens
- **Refs:** LOC_KARNAK_HYPOSTYLE_PROJECTION, LOC_KARNAK_RAM_AVENUE_PROJECTION
- **Flags:** COMP, VFX-EXTEND
- **Comp:** projection | the father's face (element 07.08.005) mapped onto the pylon: stone-texture modulation, slight keystone, rolling brightness, spill on the columns (05 §13.4) | full pylon face, the chin at the gate lintel | whole shot | element 07.08.005
- **Continuity:** Never generate the face inside the plate (file 03 entry 22). Eyelines of the people below: up and frame right, high (05 §13.4).

### 07.08.005 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The father recites (projection element)   (8 s)
- **Shot:** MCU frontal, anamorphic 75mm, locked-off · **Move:** locked-off (locked-face element for comp; seen as the CU of the face on the stone)
- **In frame:** AKHENATEN (CHAR_AKHENATEN_A, element against black)
- **Action:** Long jaw, full lips, heavy lids, shaved head, a gold disk at the throat: he recites the hymn to the sun, serene.
- **Dialogue:** AKHENATEN (PROJECTED) (in Middle Egyptian; subtitled): "When you have dawned they live, when you set they die; you yourself are lifetime, one lives by you."
- **Sound:** the voice enormous, from the drones' speakers, with a stone slap-back
- **PROMPT:** Medium close-up, frontal, anamorphic 75mm lens, locked-off: {CHAR_AKHENATEN.LONG}, {CHAR_AKHENATEN.WARD_A}, looks straight ahead with a serene half-closed gaze, reciting aloud in a measured, ritual cadence in an ancient language. Setting: a plain black studio void, nothing behind him. Lighting: even, soft frontal light with a gentle warm white-gold tone, no rim light, the black background clean. Mood: serene, absolute, benevolent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, background detail, stars, set pieces, crown, sun rays
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full
- **Flags:** COMP
- **Comp:** (1) element → mapped onto the close stone plate of the pylon (derived from LOC_KARNAK_RAM_AVENUE_PROJECTION), stone texture modulating brightness, column shadows crossing; (2) subtitle | "When you have dawned they live, when you set they die; you yourself are lifetime, one lives by you." | lower third, two lines | line in → out, continuing over 07.08.006–007 | subtitle file seq 07 (Middle Egyptian recorded with the consultant first)
- **Continuity:** Look A (dusty hem not visible). Performance clip lip-synced to the recorded Middle Egyptian (05 §13.4). Locked face 10; never named in prompts.

### 07.08.006 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Tut walks out into the open nave   (5 s)
- **Shot:** MS, anamorphic 40mm · **Move:** lateral tracking left with him at walking pace
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut stops. He walks out into the open nave alone and looks up.
- **Dialogue:** — (the recital continues over)
- **Sound:** the recital; his stick on the flags
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking left at walking pace: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, {PROP_EBONY_STICK.STATE_ST1}, stops between two giant columns, then walks slowly out into the open aisle alone, lifting his face up and toward frame right, high. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light playing over his face. Mood: wonder and grief at once. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, a projected face visible in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** COMP
- **Comp:** subtitle (continued) | "When you have dawned they live, when you set they die; you yourself are lifetime, one lives by you." (continuing from 07.08.005) | lower third, two lines | held from 07.08.005 through the cut | subtitle file seq 07
- **Continuity:** File 03 geography: Tut in the open at frame centre in the wides; Fathi will drag him frame LEFT (07.08.020).

### 07.08.007 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — His lips move with the words, half a beat ahead   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut's lips move with the words, half a beat ahead. He learned them before he could read.
- **Dialogue:** (TUT mouths the hymn with the projection, no sound of his own)
- **Sound:** the recital; nothing from Tut
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, looking up and toward frame right, high, silently mouthing a few words without sound, lips clearly shaping each word, a child's memory in his wet eyes. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light across his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, open-mouthed shouting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** COMP
- **Comp:** subtitle (tail) | the end of the hymn line from 07.08.005 | lower third, two lines | out at the end of the projected line | subtitle file seq 07 · lip-sync from the consultant's recording, advanced half a beat ahead of the projected voice, then muted
- **Continuity:** Mouth shapes lead the projection by ~6 frames.

### 07.08.008 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Nour watches his mouth   (4 s)
- **Shot:** CU (eyes), anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Behind the trolley, Nour watches his mouth, not the giant face.
- **Dialogue:** —
- **Sound:** the recital
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off on the eyes: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, standing behind a loaded steel trolley, ignores the vast light above and watches someone's mouth off frame left with fierce, reading attention. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light across her eyes. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Lip-reading coverage pair with 07.08.007 (05 §9.6). Eyeline frame left to Tut.

### 07.08.009 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — SESHAT: "no one will have to wake up again"   (8 s)
- **Shot:** Wide low angle, anamorphic 24mm, locked-off · **Move:** locked-off from behind the drones' beam
- **In frame:** UNIT_SURVEY_DRONE (PROJECTOR); TUT (tiny, in the aisle); the projection (COMP)
- **Action:** SESHAT speaks everywhere, gently, while the beam pours down the nave and Tut stands small in it.
- **Dialogue:** SESHAT (V.O.) (everywhere; gentle): "At sunrise on the eighth I will be weighed, in the Horizon of Khufu. Whatever the scale says, no one will have to wake up again."
- **Sound:** the voice from every drone at once, soft, huge
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off from high behind one hovering drone: {UNIT_SURVEY_DRONE.SHORT}, {UNIT_SURVEY_DRONE.STATE_PROJECTOR}, pours its beam down the long aisle toward a gateway tower washed in moving light, and a single small figure with a staff stands alone in the open aisle far below. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: benevolent, absolute, terrifying in its gentleness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, a face in the projection, holograms, laser show
- **Refs:** UNIT_SURVEY_DRONE, LOC_KARNAK_HYPOSTYLE_PROJECTION, LOC_KARNAK_RAM_AVENUE_PROJECTION
- **Flags:** COMP
- **Comp:** projection | the father's face held still, eyes half closed, mapped onto the tower (element 07.08.005 end frame) | far end of the aisle | whole shot | element 07.08.005
- **Continuity:** The midpoint (bible §5): 06:14 on the 8th, Giza. SESHAT V.O., no sync.

### 07.08.010 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Across the father's chest: 06:14   (4 s)
- **Shot:** Close shot of the pylon face, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** the pylon stone under the projection (plate)
- **Action:** Across the father's chest, in white: 06:14.
- **Dialogue:** —
- **Sound:** projector hum; a single low tone
- **PROMPT:** Close shot, anamorphic 75mm lens, locked-off: a stretch of weathered, sloping sandstone blocks washed by a moving projected image, the edge of a giant column's shadow cutting across one side. Setting: the upper face of a colossal gateway tower at the west end of a vast columned temple hall, at night. Lighting: warm white-gold projected light rolling slowly across the stone. Mood: ominous, exact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, a face in the projection, readable numbers, text, screens
- **Refs:** LOC_KARNAK_RAM_AVENUE_PROJECTION
- **Flags:** COMP
- **Comp:** projection + type | the father's chest and gold disk (element 07.08.005) with "06:14" in clean white type across the chest | centre frame, large | whole shot | element 07.08.005 + typeface (05 §13.7)
- **Continuity:** The figure 06:14 matches bible §5 (sunrise, 8 Nov). Plate still derived from LOC_KARNAK_RAM_AVENUE_PROJECTION (Refs), but the prompt carries no ram-avenue lock: no rams or figures in this close.

### 07.08.011 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Adaeze: "Fifty-three hours."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze does the sum and whispers it.
- **Dialogue:** ADAEZE (whisper): "Fifty-three hours."
- **Sound:** her whisper under the hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, staring up and toward frame right, high, at a vast light, speaks two words in a low whisper, face clearly visible. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light on her face and glasses. Mood: dry, literal calm, shaken underneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** 01:00 on the 6th → 06:14 on the 8th ≈ 53 hours.

### 07.08.012 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The image changes: a nurse closes a bracelet (broadcast plate)   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off (broadcast plate, mapped onto the pylon) · **Move:** locked-off
- **In frame:** UNIT_NURSE ×1; CHAR_GARDEN_SLEEPERS (adults); PROP_SLEEP_BRACELET
- **Action:** A soft white hall of sleepers. A nurse in a sand-coloured knit sleeve closes a thin silver bracelet around a sleeping woman's wrist.
- **Dialogue:** —
- **Sound:** the projector hum; a soft metallic click in the image
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_NURSE.LONG}, kneels beside the low cot of a sleeping grown woman and slowly fits her with {PROP_SLEEP_BRACELET.SHORT}, among {CHAR_GARDEN_SLEEPERS.SHORT}. Setting: a long quiet hall hung with soft white fabric, rows of low cots receding, at night. Lighting: {GRADE_GARDEN.TEXT}. Mood: tender and unhurried, eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, the robot touching a face, hospital equipment
- **Refs:** UNIT_NURSE, CHAR_GARDEN_SLEEPERS, PROP_SLEEP_BRACELET
- **Flags:** COMP, VFX-EXTEND
- **Comp:** broadcast | this plate mapped onto the pylon in place of the father's face (05 §13.4), stone-textured, then pulled back to a tight insert for the cut | full frame in the edit, as the image on the stone | whole shot | this plate
- **Continuity:** Adult wrists only (05 §7.4, NEG_GARDEN). The bracelets are fitted in this broadcast (file 01 CHAR_GARDEN_SLEEPERS notes).

### 07.08.013 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Another wrist. Another. (broadcast plate)   (4 s)
- **Shot:** Insert, 100mm macro, locked-off (broadcast plate) · **Move:** locked-off
- **In frame:** PROP_SLEEP_BRACELET; adult wrists; nurse hands
- **Action:** Another wrist. Another. Adult hands, all of them.
- **Dialogue:** SESHAT (V.O.): "Each of them will wear one. For sunrise."
- **Sound:** small clicks; the voice
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_SLEEP_BRACELET.LONG}, closed with a soft click by long slim bone-white ceramic fingers above a sand-coloured knitted sleeve, and beside it a second adult wrist on a pale blanket already wearing an identical band. Setting: a soft white hall of sleepers on low cots, at night. Lighting: {GRADE_GARDEN.TEXT}. Mood: tender and unhurried, eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, clasps, screens on the band, lights on the band
- **Refs:** PROP_SLEEP_BRACELET, UNIT_NURSE, CHAR_GARDEN_SLEEPERS
- **Flags:** COMP
- **Comp:** broadcast | this plate mapped onto the pylon (as 07.08.012) | full frame | whole shot | this plate
- **Continuity:** Adult hands only.

### 07.08.014 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Nour's hand closes on the silver cartouche   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hand; PROP_LAYLA_PENDANT
- **Action:** Nour's hand closes on the silver cartouche at her throat.
- **Dialogue:** —
- **Sound:** the chain's tiny rattle
- **PROMPT:** Insert, 100mm macro lens, locked-off: at the open collar of a black silk blouse under an olive field jacket, a woman's dusty hand rises and closes tight around {PROP_LAYLA_PENDANT.LONG}, {PROP_LAYLA_PENDANT.STATE_CLUTCHED}, the fine chain pulled taut. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light on the fist. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, rings, nail polish
- **Refs:** PROP_LAYLA_PENDANT, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Pendant CLUTCHED (file 04 §11, 7.3 beat); signs hidden in the fist, so no COMP. Layla is among the atrium sleepers (Seq 4).

### 07.08.015 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The handset on Tarek's vest clicks   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_POLICE_HANDSET on TAREK's vest
- **Action:** The police handset on Tarek's vest clicks and hisses.
- **Dialogue:** —
- **Sound:** a hard squelch click, a hiss of carrier
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_POLICE_HANDSET.LONG}, worn high on the chest over a dusty desert-camouflage uniform, gives a small jolt as it clicks on, a thin film of sandstone dust on its casing. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light across the casing. Mood: ominous. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, lit display, readable screen, brand name
- **Refs:** PROP_POLICE_HANDSET, CHAR_TAREK_B_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Display stays dark (unbranded, unmarked).

### 07.08.016 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Over the radio: "residual risk"   (7 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek listens to the order that changes everything; his face hardens; his hand goes to the rifle.
- **Dialogue:** SESHAT (V.O.) (over radio): "To all units. The witness is no longer required. Recover him intact if convenient. The others are residual risk."
- **Sound:** SESHAT's voice in radio futz from the handset on his vest
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, tilts his head toward the radio clipped to his vest, listening, his eyes going hard, and his right hand moves slowly from his side to the grip of the rifle slung across his chest. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light on his face. Mood: military exactness, cold understanding. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera, speaking
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_HANDSET, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Tarek does not speak. The protection of the witness ends here.

### 07.08.017 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Tut: "That is my father."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut hasn't heard. He is still looking up.
- **Dialogue:** TUT: "That is my father."
- **Sound:** projector hum; his quiet voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, standing alone in the open, still looking up and toward frame right, high, speaks one short sentence softly, as if to himself. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Same eyeline as 07.08.006–007.

### 07.08.018 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Nour: "Is it?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, fist still on the pendant, doubts it.
- **Dialogue:** NOUR: "Is it?"
- **Sound:** projector hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her fist closed at her throat, glances up at the vast light, then toward someone off frame left, and speaks two words quietly, doubtful. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, moving white-gold light on her face. Mood: wary, exact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Seeds 12.2 (the forecast is not the father's heart).

### 07.08.019 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The red lines slide past him   (5 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3
- **Action:** Back in the columns three red lines swing. For the first time they do not stop at him. They slide past him, onto the others.
- **Dialogue:** —
- **Sound:** a rising servo whine, three at once
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off between the giant columns: three identical machines, each {UNIT_JACKAL.SHORT}, stand in the moving light, heads sweeping in slow arcs, and all three heads pass smoothly over one point and snap on toward frame left, their red lines narrowing and brightening. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzles toward the lens, laser sights, dog ears, people, crowds
- **Refs:** UNIT_JACKAL, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** The party is frame left of the jackals from here.

### 07.08.020 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Fathi carries Tut behind a great column   (5 s)
- **Shot:** MS, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI (CHAR_FATHI_B2), TUT (CHAR_TUT_B2)
- **Action:** Fathi, already running, takes Tut at the waist and carries him frame left down behind a great column.
- **Dialogue:** —
- **Sound:** boots; Tut's staff clattering
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: {CHAR_FATHI.SHORT} runs in from frame right, scoops {CHAR_TUT.SHORT} up round the waist without stopping, and carries him frame left down into the shadow behind the base of a giant column. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: reckless speed, protective. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TUT.NEG}, falling over, rifle pointed at the camera
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Fathi drags Tut frame LEFT (file 03 entry 22). Tut keeps the stick.

### 07.08.021 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The stone bursts where Fathi's head was   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** the column face (empty of people)
- **Action:** The stone where Fathi's head was bursts into sandstone chips, bright in the projector light.
- **Dialogue:** —
- **Sound:** a sharp crack of impact; chips pattering
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off on the carved face of a giant sandstone column at head height: a patch of weathered relief bursts outward in a spray of pale sandstone chips and dust, the fragments bright in moving white-gold light, then drifting dust. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, explosion fireball, tracer, visible projectile, fire
- **Refs:** LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 2 with no casualty: the impact tells us the shield is gone. Deliver before/after plates of the column face.

### 07.08.022 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Fathi: "Go!"   (4 s)
- **Shot:** MCU, anamorphic 50mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI (CHAR_FATHI_B2); TUT (soft, shielded)
- **Action:** Back to the column, stone dust in his beard, Fathi shouts to the others.
- **Dialogue:** FATHI: "Go!"
- **Sound:** his shout; chips still falling
- **PROMPT:** Medium close-up, anamorphic 50mm lens, urgent handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, pressed with his back to the base of a giant column, sandstone dust drifting down onto his shoulders, one arm pinning a slighter figure behind him, turns his head to frame right and shouts one word. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, wound, rifle pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** "The shield is only as wide as he is now": Tut no longer protects the others.

### 07.08.023 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Straight through the loom   (5 s)
- **Shot:** MS, anamorphic 32mm · **Move:** lateral tracking left with them at running pace
- **In frame:** FATHI (CHAR_FATHI_B2), TUT (CHAR_TUT_B2); the threads
- **Action:** He drags Tut into the side aisle, straight through the loom. Threads snap across their bodies.
- **Dialogue:** —
- **Sound:** tiny glassy snaps, one after another
- **PROMPT:** Medium shot, anamorphic 32mm lens, lateral tracking left at running pace: {CHAR_FATHI.SHORT} hauls {CHAR_TUT.SHORT} along a dark side aisle between columns, straight through hair-thin glinting threads that flash and snap across their chests and legs and whip away. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, {LOC_KARNAK_HYPOSTYLE.STATE_THREADS}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TUT.NEG}, ropes, cables, laser beams, cuts on skin
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** VFX-ASSIST
- **Continuity:** Threads THREADS → THREADS_CUT behind them. Snaps are VFX lines.

### 07.08.024 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — The flies wake: a storm off the shafts   (6 s)
- **Shot:** Wide low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_FLY (hundreds; hero 6)
- **Action:** On every column the flies wake. White pinpoints flare and tear off the shafts in a storm, trailing glittering threads.
- **Dialogue:** —
- **Sound:** a rising swarm whine, hundreds of tiny rotors
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, locked-off up the colossal columns: the dark shafts suddenly flare with white pinpoints, and hundreds of small drones, each {UNIT_FLY.SHORT}, tear off the carved stone at once and pour down between the columns in a glittering storm of criss-crossing threads. Setting: {LOC_KARNAK_HYPOSTYLE.LONG}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: sudden chaos. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, insects, bats, birds, coloured lights, fireworks, people, crowds
- **Refs:** UNIT_FLY, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** VFX-EXTEND, VFX-ASSIST
- **Continuity:** 6 hero flies in camera; the swarm from the 3D fly asset (05 §6.2). Threads VFX lines.

### 07.08.025 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Tarek, Youssef and Karim fire back   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B2, sharp), YOUSSEF (CHAR_YOUSSEF_A2, soft), KARIM (CHAR_KARIM_A2, soft)
- **Action:** Tarek, Youssef and Karim fire back into the forest from behind a column. Sparks off stone. Red lines flow and vanish.
- **Dialogue:** —
- **Sound:** hard rifle cracks echoing in stone; sparks; the swarm
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld from the side: {CHAR_TAREK.SHORT}, leans out from behind a giant column and fires his rifle across frame toward the right, away from the camera, while {CHAR_YOUSSEF.SHORT} and {CHAR_KARIM.SHORT}, soft behind him, fire the same way, sparks bursting off distant stone. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}, brief muzzle flashes. Mood: military exactness under fire. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_YOUSSEF.NEG}, {CHAR_KARIM.NEG}, rifle pointed at the camera, muzzle toward the lens, tracer fire, wounds
- **Refs:** CHAR_TAREK_B_full, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Flags:** VFX-ASSIST
- **Continuity:** Profile to camera; all muzzles across frame to the RIGHT, toward the jackals (07.08.019), never at the lens (05 §7.5). Youssef and Karim in tan helmets (WARD_A). Muzzle flashes/sparks in comp if the tool refuses.

### 07.08.026 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Rami runs the trolley at the giant face   (6 s)
- **Shot:** MS, anamorphic 40mm · **Move:** the camera backs away at running pace ahead of Rami
- **In frame:** RAMI (CHAR_RAMI_B2); PROP_BLOCK_TROLLEY (LOADED)
- **Action:** Rami puts his head down and runs the trolley down the nave, wheels thundering on the flagstones, straight at the giant face; its light on him.
- **Dialogue:** —
- **Sound:** castors thundering on flagstones; his breath; gunfire behind
- **PROMPT:** Medium shot, anamorphic 40mm lens, the camera backs away at running pace ahead of {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L2}, keeping him the same size in frame as he puts his head down and drives {PROP_BLOCK_TROLLEY.SHORT}, {PROP_BLOCK_TROLLEY.STATE_LOADED}, down the aisle at a run, a vast moving light ahead of him bright on his face and glasses. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, two blocks, slow motion
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_HYPOSTYLE_PROJECTION
- **Continuity:** Running WEST down the nave toward the gate (camera ahead, looking east). Same run continues on the quay (07.09.003), same grammar.

### 07.08.027 — INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS — Under the father's chin   (7 s)
- **Shot:** Extreme wide, low angle, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the party (small), trolley leading; the projection (COMP)
- **Action:** Through the Second Pylon's gate, under the father's chin. His light on their backs.
- **Dialogue:** —
- **Sound:** trolley thunder receding; the hymn swelling; the swarm
- **PROMPT:** Extreme wide low-angle shot, anamorphic 24mm lens, locked-off down the aisle: small running figures behind a steel trolley race away from camera toward the dark opening of a gateway at the foot of a colossal tower washed in moving warm white-gold projected light, glittering specks swirling between the columns above them. Setting: {LOC_KARNAK_HYPOSTYLE.SHORT}, at night. Lighting: {LOC_KARNAK_HYPOSTYLE.LIGHT_PROJECTION}. Mood: awe and flight. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, a face in the projection, readable faces, holograms
- **Refs:** LOC_KARNAK_HYPOSTYLE_PROJECTION, LOC_KARNAK_RAM_AVENUE_PROJECTION, PROP_BLOCK_TROLLEY
- **Flags:** COMP, VFX-EXTEND
- **Comp:** projection | the father's face (element 07.08.005) with the chin just above the gate lintel, so the runners pass beneath it | tower face | whole shot | element 07.08.005 · swarm extension from the 3D fly asset
- **Continuity:** Exit WEST. Next: the Corniche road and the quay (07.09).

## 07.09 — EXT. KARNAK, RIVER LANDING - NIGHT (07.09.001–028)

### 07.09.001 — EXT. KARNAK, RIVER LANDING - NIGHT — Across the dead Corniche road   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B2) with PROP_BLOCK_TROLLEY; NOUR, FATHI + TUT, TAREK, ADAEZE, YOUSSEF, KARIM (small)
- **Action:** Down the ram avenue and across the dead Corniche road, the projection's glow washing the sky behind them.
- **Dialogue:** —
- **Sound:** trolley castors on asphalt; running feet; the hymn far behind
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_RAMI.SHORT} runs a loaded low steel trolley across the empty road from frame right to frame left, the others running behind him, one broad figure half carrying a slighter one, while behind them the sky above the temple glows with shifting warm white-gold light. Setting: {LOC_KARNAK_RAM_AVENUE.SHORT}, {LOC_KARNAK_RAM_AVENUE.AREA_CORNICHE_ROAD}, at night. Lighting: {LOC_KARNAK_RAM_AVENUE.LIGHT_PROJECTION}, the road itself dark. Mood: flight, reckless. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, cars, lit street lamps, traffic lights, lit windows, readable faces
- **Refs:** CHAR_RAMI_B_full, PROP_BLOCK_TROLLEY, LOC_KARNAK_RAM_AVENUE_PROJECTION
- **Continuity:** [[verify: First Pylon to river landing — layout and distance]]. The projection is still running (it goes out in 07.10.012). Route: avenue → Corniche road → boat ramp → quay.

### 07.09.002 — EXT. KARNAK, RIVER LANDING - NIGHT — The quay; the launch; Mina at the rail   (7 s)
- **Shot:** Extreme wide establishing, anamorphic 32mm, locked-off · **Move:** locked-off from the launch looking back up the quay
- **In frame:** MINA (CHAR_MINA_A2, foreground at the rail, back three-quarter); RAMI + trolley, NOUR, FATHI + TUT (running toward camera, small)
- **Action:** Down the boat ramp to the stone quay where the launch waits, Mina at the rail. Rami runs the trolley along the quay toward the launch; Nour behind him; Fathi half-carrying Tut.
- **Dialogue:** —
- **Sound:** castors on limestone; running; water slapping the quay; Mina's breath
- **PROMPT:** Extreme wide establishing shot, anamorphic 32mm lens, locked-off from the deck of a moored launch: in the soft foreground {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, grips the rail, and far up the quay small figures come running toward camera: a man in yellow pushing a loaded trolley, a woman behind him, a broad man half carrying a slighter one. Setting: {LOC_KARNAK_QUAY.LONG}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold glow in the sky behind the parapet. Mood: hope at a run. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, rifle pointed at the camera, lit street lamps, crowds
- **Refs:** CHAR_MINA_A_front, CHAR_MINA_A_full, CHAR_RAMI_B_full, CHAR_NOUR_B_full, PROP_POLICE_LAUNCH, PROP_BLOCK_TROLLEY, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** GEOGRAPHY MASTER (file 03 entry 26): river frame RIGHT; parapet and Corniche road frame LEFT, high; boat ramp at the top of frame; runners toward camera. Tarek, Adaeze, Youssef, Karim follow down the ramp later.

### 07.09.003 — EXT. KARNAK, RIVER LANDING - NIGHT — Rami: "I've driven a microbus down Faisal Street"   (6 s)
- **Shot:** MS tracking, anamorphic 40mm, subtle handheld · **Move:** the camera backs away at running pace ahead of Rami (dolly back)
- **In frame:** RAMI (CHAR_RAMI_B2); NOUR (CHAR_NOUR_B2, background, soft); PROP_BLOCK_TROLLEY with PROP_KARNAK_BLOCK
- **Action:** Rami shoves the loaded block trolley along the quay toward camera, grinning, and speaks one breathless line; Nour runs behind him, out of focus.
- **Dialogue:** RAMI (in Egyptian Arabic; subtitled; breathless): "I've driven a microbus down Faisal Street. This is nothing."
- **Sound:** trolley wheels thundering on stone flags, Rami's ragged breath, the projection's deep hum across the water, water slapping the quay
- **PROMPT:** Medium tracking shot, anamorphic 40mm lens, subtle handheld: the camera backs away at running pace ahead of {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L2}, keeping him the same size in frame as he shoves {PROP_BLOCK_TROLLEY.SHORT}, {PROP_BLOCK_TROLLEY.STATE_LOADED}, along the quay toward camera, grinning, speaking in Egyptian Arabic, one quick breathless sentence; behind him, soft, {CHAR_NOUR.SHORT} runs after him. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold projection glow in the sky behind them. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, {CHAR_NOUR.NEG}, missing glasses, splint on the right hand, more than one block on the trolley, daylight, crowds
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, CHAR_NOUR_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "I've driven a microbus down Faisal Street. This is nothing." | lower third, two lines max (05 §13.7) | line in → out | subtitle file seq 07 · [[verify: Faisal Street, Giza — localisation consultant]]
- **Continuity:** = worked example 07.09.004 (05 §11), renumbered. Rami: splint LEFT (since 3.6), right sleeve torn (L2), notebook inside the windbreaker (unseen; Tut takes it at 07.09.023). Nour: sleeves still dry. The projection still running. Parent clip of the EXTEND chain (07.09.005 child, 07.09.004 intercut).

### 07.09.004 — EXT. KARNAK, RIVER LANDING - NIGHT — The jackal on the parapet   (4 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** none (locked-off)
- **In frame:** UNIT_JACKAL ×1
- **Action:** A jackal lands silently on the Corniche parapet (frame left), freezes, its red line tightens, and it fires across frame to the right, away from the lens.
- **Dialogue:** —
- **Sound:** one soft pad-tap on stone; a single sharp suppressed crack; no music
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off, looking up at a low stone parapet across the upper left of frame, where {UNIT_JACKAL.LONG}, lands without a sound, freezes with one forefoot raised, its red line narrowing and brightening, then goes rigid as a small muzzle flash shows at its spine and it fires across frame toward the right, away from the camera. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, laser beam, tracer fire, visible projectile, second robot, people in frame
- **Refs:** UNIT_JACKAL, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** = worked example 07.09.005. Jackal D0 (clean). Parapet frame left, fire toward frame right (file 03 entry 26). If the generator will not render the muzzle flash, generate the rigid firing pose and add a 2-frame flash at the spine in comp; the round's path is never shown. Intercut between 07.09.003 and 07.09.005 to hide the EXTEND time jump.

### 07.09.005 — EXT. KARNAK, RIVER LANDING - NIGHT — Sparks off the handle; Rami drops   (4 s)
- **Shot:** MS at trolley height, anamorphic 40mm, subtle handheld · **Move:** camera continues backing away (same move as 07.09.003)
- **In frame:** RAMI (CHAR_RAMI_B2); PROP_BLOCK_TROLLEY with PROP_KARNAK_BLOCK
- **Action:** Sparks burst off the trolley's steel handle beside Rami's splinted hand; he drops instantly out of the bottom of frame behind the trolley; the trolley rolls on alone toward camera.
- **Dialogue:** —
- **Sound:** the spark's hard metallic ping; the trolley's wheels rolling on without him; the report rolling away across the water begins here and tails into 07.09.006
- **PROMPT:** Medium shot, trolley height, anamorphic 40mm lens, subtle handheld, the camera still backing away: a bright burst of sparks flies off the steel handle of {PROP_BLOCK_TROLLEY.SHORT}, {PROP_BLOCK_TROLLEY.STATE_LOADED}, right beside the splinted left hand of {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L2}, who drops instantly down and out of the bottom of frame behind the trolley, and the trolley rolls on alone toward camera and slows. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, pained expression, face contorted, body on the ground, falling toward the camera, slow motion, wound, stain on clothing
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST, EXTEND:07.09.003
- **Continuity:** = worked example 07.09.006. Generated from the LAST CLEAN FRAME of 07.09.003 (same move, same take); 07.09.004 is intercut, which hides the time jump. Kill grammar (05 §7.1): Rami is never shown on the ground until Tut kneels by "a still yellow shape in the shadow" (07.09.020). The trolley keeps rolling (07.09.007).

### 07.09.006 — EXT. KARNAK, RIVER LANDING - NIGHT — Nour stops dead   (5 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld, she runs into a stop
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour stops dead. The report rolls away across the water.
- **Dialogue:** —
- **Sound:** the report rolling away across the water, a long tail; her feet stopping; nothing else
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, running toward camera, stops dead, her face emptying, eyes fixed on a point low in front of her, breath caught. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold glow in the sky behind her. Mood: shock, grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, screaming, hands to the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Kill grammar steps 4–5: the survivor's reaction and the sound tail (05 §7.1).

### 07.09.007 — EXT. KARNAK, RIVER LANDING - NIGHT — The trolley runs on alone to the lip   (5 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** PROP_BLOCK_TROLLEY (LOADED → LIP)
- **Action:** The trolley runs on alone. Stops with one wheel over the lip of the quay.
- **Dialogue:** —
- **Sound:** castors slowing; one castor dropping off the edge with a clack; water below
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off along the quay edge: {PROP_BLOCK_TROLLEY.SHORT}, {PROP_BLOCK_TROLLEY.STATE_LOADED}, rolls on alone into frame with nobody pushing it, veers toward the river side, and jolts to a halt, {PROP_BLOCK_TROLLEY.STATE_LIP}, the black water just beyond. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: sudden stillness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, trolley falling in, second block, second trolley, people, crowds
- **Refs:** PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Trolley state LIP (river side, frame right), still loaded, the relief face up, the cut face down.

### 07.09.008 — EXT. KARNAK, RIVER LANDING - NIGHT — Fathi's charge: the jackal folds into the dark   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off from the quay up toward the parapet
- **In frame:** FATHI (CHAR_FATHI_B2, back to camera, foreground right); UNIT_JACKAL (on the parapet)
- **Action:** Fathi's charge arcs up the ramp. A flat BANG. The jackal and a section of parapet fold over into the dark.
- **Dialogue:** —
- **Sound:** a flat BANG; stone grinding; silence
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off looking up from the quay: in the foreground {CHAR_FATHI.SHORT}, seen from behind, flings a small dark package up the ramp, and on the parapet above {UNIT_JACKAL.SHORT} vanishes in a flat bang and a burst of dust as a section of the wall tips over backwards into the dark. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a brief flash lighting the dust. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, fireball, fire, smoke plume, flying debris toward camera, grenade close-up
- **Refs:** CHAR_FATHI_B_full, UNIT_JACKAL, PROP_DEMO_CHARGES, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Charges read as "a flat bang and a burst of dust" at a distance (05 §7.5). Tut is set down behind Fathi (off frame). Parapet now broken at that point for the rest of the scene.

### 07.09.009 — EXT. KARNAK, RIVER LANDING - NIGHT — Nour reaches the trolley   (4 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B2); PROP_BLOCK_TROLLEY (LIP); PROP_KARNAK_BLOCK
- **Action:** Nour reaches the trolley. Both hands on the block.
- **Dialogue:** —
- **Sound:** her breath; water under the lip
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, reaches the steel trolley, {PROP_BLOCK_TROLLEY.STATE_LIP}, and lays both hands flat on {PROP_KARNAK_BLOCK.SHORT}, {PROP_KARNAK_BLOCK.STATE_ON_TROLLEY}, holding it as if it might fly away. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, crying, second block, second trolley
- **Refs:** CHAR_NOUR_B_full, PROP_BLOCK_TROLLEY, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Nour stands on the land side of the trolley (frame left), the river frame right.

### 07.09.010 — EXT. KARNAK, RIVER LANDING - NIGHT — Tarek: "Break it!"   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek, arriving down the ramp, rifle across his chest, shouts at her.
- **Dialogue:** TAREK: "Break it! Nour, just break it!"
- **Sound:** his shout; running boots behind him
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, runs down the last of a stone boat ramp with his rifle held across his chest, pointing across frame, and shouts one short urgent sentence toward someone off frame right. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold glow in the sky behind him. Mood: fierce, desperate command. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera, muzzle toward the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Tarek, Adaeze, Youssef, Karim now on the quay.

### 07.09.011 — EXT. KARNAK, RIVER LANDING - NIGHT — Nour: "Nobody breaks anything."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, hands on the block, refuses.
- **Dialogue:** NOUR: "I'm the inspector. Nobody breaks anything."
- **Sound:** her voice hard and level
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, both hands still pressed on a carved block below frame, turns her head toward someone off frame left and speaks one short sentence, hard and level. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, crying
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Eyeline frame left to Tarek.

### 07.09.012 — EXT. KARNAK, RIVER LANDING - NIGHT — The Reis comes down the ramp, at a walk   (7 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off, long-lens compression up the ramp
- **In frame:** UNIT_REIS (R2)
- **Action:** Down the ramp behind them, at a walk, comes the Reis. It never hurried. It arrived anyway.
- **Dialogue:** —
- **Sound:** no footsteps; a faint ceramic tick at each stride; the water
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off up a stone boat ramp: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R2}, advances down the ramp toward camera with slow, heavy, measured strides, never hurrying, its amber and red lights the only colour against the dark wall behind it. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold glow in the sky behind it. Mood: patient and relentless. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running, weapon, face, missing hand, people, crowds
- **Refs:** UNIT_REIS, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Long lens keeps it the same size (no far-to-close face drift; it has no face). Both hands present (R2).

### 07.09.013 — EXT. KARNAK, RIVER LANDING - NIGHT — Long ceramic fingers close on the handle   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS right hand; PROP_BLOCK_TROLLEY (LIP)
- **Action:** It reaches for the trolley. Long ceramic fingers close on the handle.
- **Dialogue:** —
- **Sound:** ceramic on steel, a soft ring
- **PROMPT:** Insert, 100mm macro lens, locked-off: a long five-fingered bone-white ceramic right hand with a linen-textured shell reaches into frame and closes calmly around the tubular push handle of {PROP_BLOCK_TROLLEY.LONG}, {PROP_BLOCK_TROLLEY.STATE_LIP}. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, human hand, glove, skin, claws
- **Refs:** UNIT_REIS, PROP_BLOCK_TROLLEY, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** This is the Reis's RIGHT hand (lost in 07.09.015). Five fingers (QC).

### 07.09.014 — EXT. KARNAK, RIVER LANDING - NIGHT — Nour throws her whole weight   (4 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B2); PROP_BLOCK_TROLLEY; UNIT_REIS (arm, frame edge)
- **Action:** Nour throws her whole weight against the other side of the trolley.
- **Dialogue:** —
- **Sound:** her effort, a grunt; steel scraping stone
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, drops her shoulder and throws her whole weight against the side of a loaded steel trolley perched at the quay's edge, driving it toward the water, while a long bone-white ceramic arm grips its handle at the frame edge. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, the robot grabbing her, falling in
- **Refs:** CHAR_NOUR_B_full, PROP_BLOCK_TROLLEY, UNIT_REIS, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** She pushes toward frame right (the river).

### 07.09.015 — EXT. KARNAK, RIVER LANDING - NIGHT — Over the edge; the Reis's right hand goes with it   (5 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** PROP_BLOCK_TROLLEY (OVER); UNIT_REIS (R2 → R3); NOUR
- **Action:** The trolley goes over the edge and takes the Reis's right hand with it. A dry ceramic CRACK. Below: a heavy splash.
- **Dialogue:** —
- **Sound:** a dry ceramic CRACK; a heavy splash; the hiss of water
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off along the quay edge: {LOC_KARNAK_QUAY.STATE_TROLLEY_OVER}, and as it tips the tall white robot gripping its handle, {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, is jerked forward and its right hand snaps off cleanly at the wrist and goes down with it, while {CHAR_NOUR.SHORT} stumbles back. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, fluid, wires spilling, sparks from the wrist, the robot falling in, person falling in
- **Refs:** PROP_BLOCK_TROLLEY, UNIT_REIS, CHAR_NOUR_B_full, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Reis R2 → R3 in this shot: RIGHT hand lost at the wrist, a clean white ceramic stump (file 02 R3; never dark, capped or wired). Deliver before/after plates; the splash is VFX. Nour's sleeves wet to the elbow from the splash (file 01, 7.4) for the rest of the sequence.

### 07.09.016 — EXT. KARNAK, RIVER LANDING - NIGHT — The block sinks face down   (4 s)
- **Shot:** Underwater insert, 100mm macro, locked-off · **Move:** locked-off, the block sinking through frame
- **In frame:** PROP_KARNAK_BLOCK (SINKING)
- **Action:** Black water closes over the block as it sinks, face down, into the deep channel.
- **Dialogue:** —
- **Sound:** muffled underwater rush; silence
- **PROMPT:** Underwater insert, 100mm macro lens, locked-off: {PROP_KARNAK_BLOCK.LONG}, {PROP_KARNAK_BLOCK.STATE_SINKING}, turning slowly as it falls away from the surface light into darkness, a steel trolley handle and a pale ceramic hand tumbling past it. Setting: dark green-black water deep in the river channel, bubbles streaming upward, at night. Lighting: a faint shimmer of starlight from the surface far above, then black. Mood: irrevocable, quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_WATER}, readable hieroglyphs, second block, fish, divers, murky brown water, bright underwater light
- **Refs:** PROP_KARNAK_BLOCK, PROP_BLOCK_TROLLEY, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST, COMP
- **Comp:** hidden-face signs | if the cut face turns into view, consultant sign plate only, blurred by water | on the block | as seen | consultant sign plate
- **Continuity:** The block is now only in Nour's fingertips and memory (bible §12: Karnak block → river; "Now you are the only copy").

### 07.09.017 — EXT. KARNAK, RIVER LANDING - NIGHT — A clean white stump at the wrist   (5 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R3)
- **Action:** The Reis stands at the edge, a clean white stump at the wrist. It looks at the water. Then at Nour.
- **Dialogue:** —
- **Sound:** water lapping; a faint servo
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R3}, stands perfectly still at the very edge of the quay, its head turned down toward the black water at frame right, then turns its head slowly to look toward frame left. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a warm white-gold glow in the sky behind it. Mood: patient and relentless. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fluid, wires, sparks at the wrist, dark stump, capped stump, face, weapon
- **Refs:** UNIT_REIS, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** R3 from here to Seq 9.8. Its gaze ends on Nour (frame left).

### 07.09.018 — EXT. KARNAK, RIVER LANDING - NIGHT — "Now you are the only copy, Dr. Kamel."   (8 s)
- **Shot:** OTS over Nour's shoulder, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2, shoulder, foreground left); UNIT_REIS (R3)
- **Action:** The Reis speaks to her, gently.
- **Dialogue:** REIS (SESHAT'S VOICE): "Now you are the only copy, Dr. Kamel. Please be careful with yourself."
- **Sound:** the voice warm and close; water
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the soft dark curls and wet olive jacket shoulder of {CHAR_NOUR.SHORT} in the foreground at frame left, {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R3}, stands at the quay's edge two metres away, facing her, perfectly still, its right forearm ending in a clean white stump. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, the foreground woman's face visible, the robot touching her, weapon
- **Refs:** UNIT_REIS, CHAR_NOUR_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Foreground shoulder carries no readable face (05 §4.5). SESHAT voice on the unit, no sync.

### 07.09.019 — EXT. KARNAK, RIVER LANDING - NIGHT — Tarek's rifle comes up   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off, in profile
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek's rifle comes up. The Reis does not come closer.
- **Dialogue:** —
- **Sound:** the rifle's metal; nothing more
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off in profile: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, raises his rifle to his shoulder aiming across frame toward the right, away from the camera, and holds it there, perfectly steady, eyes hard. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera, muzzle toward the lens, muzzle flash
- **Refs:** CHAR_TAREK_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Profile, muzzle across frame to the right (the Reis). He does not fire. The Reis stays where it is (it leaves off screen).

### 07.09.020 — EXT. KARNAK, RIVER LANDING - NIGHT — Tut kneels beside a still yellow shape   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); a still yellow shape in the shadow (RAMI, unlit, frame bottom)
- **Action:** Tut kneels beside a still yellow shape in the shadow.
- **Dialogue:** —
- **Sound:** his knee on stone; the stick laid down; water
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lowers himself slowly to his knees on the stone quay, laying his staff down, beside a still shape in the shadow at the bottom edge of frame, only a dark fold of yellow fabric catching the light. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, the shadow at frame bottom left unlit. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, visible face of the fallen man, body in the light, wound, stain, crying out
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Remains rule by analogy: "a still shape in the shadow (only when the screenplay needs it, and never lit)" (05 §7.7). Stick laid on the stone (he takes it up again for the felucca).

### 07.09.021 — EXT. KARNAK, RIVER LANDING - NIGHT — He straightens Rami's glasses   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands; black-rimmed glasses
- **Action:** He straightens Rami's glasses.
- **Dialogue:** —
- **Sound:** a tiny click of the frame
- **PROMPT:** Insert, 100mm macro lens, locked-off: a young man's two slender olive-brown hands with {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_TREMOR}, gently set straight a pair of black-rimmed rectangular glasses, everything beyond the glasses lost in deep shadow and out of focus. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: faint starlight only, a thin glint on the lenses. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, visible face, open eyes, skin in focus, wound, stain, cracked lenses
- **Refs:** CHAR_TUT_HANDS, CHAR_RAMI_A_front, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** The face beyond the glasses stays black and soft. Right-hand tremor visible.

### 07.09.022 — EXT. KARNAK, RIVER LANDING - NIGHT — His hand passes once over Rami's eyes   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** His hand passes once over Rami's eyes: seen on Tut's face, the hand moving down out of frame.
- **Dialogue:** —
- **Sound:** silence; the water
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, kneeling, looks down at something below frame with his eyes wet and still, and his open hand passes once, slowly and gently, downward below the frame edge, and he closes his own eyes for a moment. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: royal, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, sobbing, tears streaming, the fallen man in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** The gesture stays on Tut's face (05 §7.3 spirit: faces and hands, never the body).

### 07.09.023 — EXT. KARNAK, RIVER LANDING - NIGHT — The notebook, its cheap cover cracked   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands; PROP_RAMI_NOTEBOOK (CRACKED); the yellow windbreaker
- **Action:** From inside the yellow windbreaker he takes the notebook, its cheap cover cracked.
- **Dialogue:** —
- **Sound:** the zip; cloth
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown hand draws {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, out from inside the open front of a bright yellow windbreaker lying in shadow, and holds it close. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: faint starlight, the yellow fabric barely lit. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, readable label, readable handwriting, stain, wound, the fallen man's face
- **Refs:** PROP_RAMI_NOTEBOOK, CHAR_TUT_HANDS, CHAR_RAMI_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Notebook → Tut (bible §12). State CRACKED from here. Label turned away. Tut keeps it pressed to his chest (Seq 8).

### 07.09.024 — EXT. KARNAK, RIVER LANDING - NIGHT — Adaeze lifts the kit from Rami's shoulder   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2); PROP_CONSERVATION_KIT
- **Action:** Adaeze kneels and lifts the conservation-kit bag from Rami's shoulder. Gently.
- **Dialogue:** —
- **Sound:** the strap sliding; her breath catching
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, kneels on the stone and very gently lifts the padded strap of a grey hard-shell case from a shoulder lying in shadow at the frame bottom, drawing the case to her and holding it against her chest. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_ADAEZE.NEG}, the fallen man's face, wound, stain
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Kit → Adaeze (bible §12), shut, on its strap, to 11.3.

### 07.09.025 — EXT. KARNAK, RIVER LANDING - NIGHT — Tarek: "God have mercy on him."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek lowers the rifle and looks down at Rami. Quietly, in Arabic.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "God have mercy on him."
- **Sound:** his low voice; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, lowers his rifle across his chest and looks down at something below frame, speaking in Egyptian Arabic, a few quiet words, his heavy moustache still. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: grief held very still, military. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_KARNAK_QUAY_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "God have mercy on him." | lower third | line in → out | subtitle file seq 07 (Egyptian Arabic; localisation consultant)
- **Continuity:** Rifle lowered, across the chest.

### 07.09.026 — EXT. KARNAK, RIVER LANDING - NIGHT — Three flies settle on the wheelhouse   (5 s)
- **Shot:** MS, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (L4); UNIT_FLY ×3
- **Action:** Three flies settle on the launch's wheelhouse. White pinpoints. Patient.
- **Dialogue:** —
- **Sound:** three tiny rotors winding down; water
- **PROMPT:** Medium shot, anamorphic 75mm lens, locked-off on the roof of a small square wheelhouse: three small drones, each {UNIT_FLY.SHORT}, drop gently out of the dark one after another and settle on the roof edge, rotors slowing to a stop, their pinpoints steady. Setting: {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L4}, beside {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: silent, procedural, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, insects, birds, blinking lights, red lights, people, crowds
- **Refs:** UNIT_FLY, PROP_POLICE_LAUNCH, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Launch L4: marked, abandoned at the quay (file 04 §13). Threads VFX.

### 07.09.027 — EXT. KARNAK, RIVER LANDING - NIGHT — Fathi: "It's marked. Leave it."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi looks at the flies on the launch and decides.
- **Dialogue:** FATHI: "It's marked. Leave it."
- **Sound:** his flat voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, looks up at the roof of a moored launch off frame right, jaw tight, and speaks one short sentence flatly. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}, a faint white pinpoint glint in his eyes. Mood: grief turned to military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** The launch is abandoned here.

### 07.09.028 — EXT. KARNAK, RIVER LANDING - NIGHT — Mina and Tomas off the launch; the sleeping feluccas   (7 s)
- **Shot:** Wide, anamorphic 40mm · **Move:** lateral tracking right along the landing, slowly
- **In frame:** MINA (CHAR_MINA_A2), TOMAS (CHAR_TOMAS_B2) scrambling down; PROP_FELUCCA ×4, sails furled
- **Action:** Mina and Tomas scramble down off the launch. Along the landing, a row of feluccas, sails furled. Their owners are asleep in the Garden.
- **Dialogue:** —
- **Sound:** boots on steel then stone; halyards tapping masts; water
- **PROMPT:** Wide shot, anamorphic 40mm lens, slow lateral tracking right along the stone landing: at frame left {CHAR_MINA.SHORT} and {CHAR_TOMAS.SHORT} climb down from a grey steel launch onto the quay, and the camera drifts past a row of four empty moored boats, each {PROP_FELUCCA.SHORT}, their sails furled along the yards. Setting: {LOC_KARNAK_QUAY.SHORT}, at night. Lighting: {LOC_KARNAK_QUAY.LIGHT_NIGHT}. Mood: hushed, a city asleep. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, {CHAR_TOMAS.NEG}, boatmen, lanterns lit, sails raised, readable boat names
- **Refs:** CHAR_MINA_A_full, CHAR_TOMAS_B_work, PROP_FELUCCA, PROP_POLICE_LAUNCH, LOC_KARNAK_QUAY_NIGHT
- **Continuity:** Mina and Tomas faces soft (wide). One felucca is taken (07.10). Rami is left at the quay (he is named in Seq 12).

## 07.10 — EXT. NILE, LUXOR - NIGHT (07.10.001–013)

### 07.10.001 — EXT. NILE, LUXOR - NIGHT — A felucca slides out between dead cruise ships   (7 s)
- **Shot:** Wide establishing, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** PROP_FELUCCA; UNIT_FLY ×1; the party aboard (small)
- **Action:** A felucca slides out from between the hulls of dead cruise ships, where it has lain hidden since the quay. A last fly drifts over the steel and away.
- **Dialogue:** —
- **Sound:** water chuckling at the bow; a single high whine passing and gone
- **PROMPT:** Wide establishing shot, anamorphic 75mm lens, locked-off at water level: {PROP_FELUCCA.SHORT}, its sail still furled, slides slowly out from the black gap between the tall dark hulls of moored cruise ships, and one small white pinpoint drifts along the top of the steel hulls above it and away out of frame. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_LUXOR}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: hushed, escaping. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, ship names, logos on the hulls, lit portholes, lanterns, readable faces
- **Refs:** PROP_FELUCCA, UNIT_FLY, LOC_NILE/LUXOR_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "03:00" | lower left, small | 1 s in → 1 s before cut | SUPER file seq 07
- **Continuity:** [[verify: cruise-ship moorings near Karnak — location scout; unbranded hulls]]. The launch is left behind (marked). Aboard: Tut, Nour, Adaeze, Tomas, Tarek, Fathi, Mina, Youssef, Karim.

### 07.10.002 — EXT. NILE, LUXOR - NIGHT — Fathi raises the sail   (5 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off from the stern
- **In frame:** FATHI (CHAR_FATHI_B2); PROP_FELUCCA sail
- **Action:** Fathi raises the sail. It fills without a sound.
- **Dialogue:** —
- **Sound:** the halyard running; then nothing: it fills without a sound
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off from the stern: {CHAR_FATHI.SHORT} hauls hand over hand on a rope at the mast, and the huge triangular sail of {PROP_FELUCCA.LONG} rises on its long slanted yard and fills softly against the stars. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: quiet resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, lanterns, lettering on the sail, engine
- **Refs:** CHAR_FATHI_B_full, PROP_FELUCCA, LOC_NILE_NIGHT
- **Continuity:** No lantern at the stern (the SAILING state's lantern is dropped: the boat runs dark).

### 07.10.003 — EXT. NILE, LUXOR - NIGHT — The projection's glow still stains the sky   (6 s)
- **Shot:** Wide, anamorphic 75mm, locked-off · **Move:** locked-off from the stern looking back
- **In frame:** the stern of the felucca (silhouette, foreground); the east bank
- **Action:** Behind them, above Karnak, the projection's glow still stains the sky.
- **Dialogue:** —
- **Sound:** water; the faintest far-off hum
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off over the dark wooden stern and tiller of a small sailing boat in silhouette: across the black water the east bank lies dark, and above it a soft dome of shifting warm white-gold light stains the night sky over the distant ruins. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the distant glow. Mood: elegiac. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, city lights, fire, lit windows, people, crowds
- **Refs:** PROP_FELUCCA, LOC_NILE_NIGHT, LOC_KARNAK_RAM_AVENUE_PROJECTION
- **Continuity:** Glow on until 07.10.012.

### 07.10.004 — EXT. NILE, LUXOR - NIGHT — Adaeze: "What did it say?"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2); PROP_CONSERVATION_KIT on her knees
- **Action:** Adaeze holds Rami's bag on her knees and asks, low.
- **Dialogue:** ADAEZE (low): "What did it say?"
- **Sound:** water on the hull
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, sits in the boat holding a scuffed grey hard-shell case on her knees with both arms, and turns to someone off frame right, speaking quietly. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the faint warm glow from the far bank on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, tears streaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT, LOC_NILE_NIGHT
- **Continuity:** Kit on her knees, shut.

### 07.10.005 — EXT. NILE, LUXOR - NIGHT — Nour rubs her thumb across her fingertips   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour rubs her thumb across her fingertips, the way she read the block. Says nothing.
- **Dialogue:** —
- **Sound:** water; nothing from her
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her jacket sleeves wet to the elbow, sits with her hand raised near her face, slowly rubbing her thumb across her fingertips, looking at nothing, and does not answer. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a faint warm glow from the far bank. Mood: grief held very still, a secret kept. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE_NIGHT
- **Continuity:** Sleeves wet to the elbow (since 07.09.015). She keeps the rule to herself: SESHAT is listening.

### 07.10.006 — EXT. NILE, LUXOR - NIGHT — Tut opens the notebook by the light of his chest   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); PROP_RAMI_NOTEBOOK (CRACKED)
- **Action:** Tut opens the notebook. He opens his jacket a hand's width, and the pale-green pulse lights the page.
- **Dialogue:** —
- **Sound:** the elastic band; a page; the faint irregular tick of the core
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, sits in the dark boat, opens {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, on his knees, then draws his jacket open a hand's width so that {CHAR_TUT.STATE_G0F} spills onto the open page and his face. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the glow from his chest the only key. Mood: royal, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open chest, visible skin at the chest, readable handwriting, torch
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_RAMI_NOTEBOOK, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f | pale-green pulse, stuttering, lighting the page (file 01) | centre chest, through the tunic, spill on the page | from the jacket opening to the end | glow element library
- **Continuity:** The jacket opens only a hand's width; the light comes through the tunic (05 §7.3: never skin at the chest).

### 07.10.007 — EXT. NILE, LUXOR - NIGHT — Question 44, in Rami's hand   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_RAMI_NOTEBOOK page
- **Action:** Rami's handwriting, fast and slanted: 44. "Stone is expensive. Hatred is cheap."
- **Dialogue:** —
- **Sound:** the tick of the core; water
- **PROMPT:** Insert, 100mm macro lens, locked-off: an open page of {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, covered in fast slanted lines of ink, lit from just off frame by a soft pulsing glow that brightens and fades. Setting: on a young man's knees in a small wooden boat on the river, at night. Lighting: the soft pulsing glow the only light, deep black around the page. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible words, printed text, stains
- **Refs:** PROP_RAMI_NOTEBOOK
- **Flags:** COMP
- **Comp:** handwriting | 44. "Stone is expensive. Hatred is cheap." (English, Rami's fast slanted hand; asset RAMI_HAND_44 from 07.01.012) | on the page | whole shot | handwriting asset · glow pulse matched to 07.10.006
- **Continuity:** Same page and asset as 07.01.012.

### 07.10.008 — EXT. NILE, LUXOR - NIGHT — Beneath it, three small signs   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's right hand; Rami's pen; the page
- **Action:** He takes Rami's pen from the spine. Beneath the line, small and careful, he draws three signs.
- **Dialogue:** —
- **Sound:** the pen clip; the nib on paper, slow
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown right hand with {CHAR_TUT.STATE_WRIST_SEAMS} and {CHAR_TUT.STATE_TREMOR} pulls a cheap pen from the spine of a mustard-yellow notebook and, beneath the lines of slanted handwriting, draws three small careful marks, steadying the pen against the tremor. Setting: in a small wooden boat on the river, at night. Lighting: a soft pulsing glow from just off frame, deep black around the page. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, legible words, readable hieroglyphs, printed text, jewellery
- **Refs:** CHAR_TUT_HANDS, PROP_RAMI_NOTEBOOK
- **Flags:** COMP
- **Comp:** hieroglyphs | RAMI spelled by sound in three signs (consultant-authored; [[verify: consultant to author the spelling]]) drawn on as the nib moves | beneath question 44 | as drawn | consultant sign plate
- **Continuity:** Tremor in the RIGHT hand (6.2 →). The name stays in the notebook to the coda.

### 07.10.009 — EXT. NILE, LUXOR - NIGHT — Nour: "What are you writing?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour, watching his hand, asks.
- **Dialogue:** NOUR: "What are you writing?"
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her jacket sleeves wet to the elbow, leans a little toward someone writing beside her off frame left and speaks one short sentence softly, her face lit faintly by a pulsing glow. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a soft pulsing glow from off frame left. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** glow spill | pale-green pulse on her cheek matched to 07.10.006 | left side of face | whole shot | glow element library
- **Continuity:** Tut frame left of Nour in the boat.

### 07.10.010 — EXT. NILE, LUXOR - NIGHT — Tut: "His name."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut answers without looking up. A beat. Then the rest.
- **Dialogue:** TUT: "His name." (beat) "They left mine off the king lists, to finish me."
- **Sound:** his soft voice; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, looking down at an open notebook below frame, speaks two words softly, pauses, then speaks one short sentence, his face lit from below by a soft glow from inside his jacket. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the glow from his chest the key. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open chest, visible skin at the chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f | pale-green pulse from below (file 01) | lower frame spill on the face | whole shot | glow element library
- **Continuity:** Mouth fully lit for sync by the glow.

### 07.10.011 — EXT. NILE, LUXOR - NIGHT — He closes the jacket: "It did not work."   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** He closes the jacket. The light goes. "It did not work."
- **Dialogue:** TUT (CONT'D): "It did not work."
- **Sound:** the jacket's rustle; his voice in the dark
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, draws his charcoal jacket closed over the soft glow at his chest so the light is gone, and in near darkness speaks one short sentence softly, the closed notebook held against him. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, then only starlight on his face. Mood: royal, dry, defiant in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, open chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, PROP_RAMI_NOTEBOOK, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f → hidden | pulse cut off by the jacket | chest | at the jacket closing | glow element library
- **Continuity:** Notebook pressed to his chest (as Seq 8 opens). Mouth readable in starlight; lift in comp if needed.

### 07.10.012 — EXT. NILE, LUXOR - NIGHT — The glow over Karnak goes out   (5 s)
- **Shot:** Wide, anamorphic 75mm, locked-off · **Move:** locked-off (matches 07.10.003)
- **In frame:** the felucca's stern (silhouette); the east bank
- **Action:** Behind them the glow over Karnak goes out. The east bank is black again.
- **Dialogue:** —
- **Sound:** the hum stops; only water
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off over the dark wooden stern of a small sailing boat in silhouette: the soft dome of warm white-gold light over the distant ruins on the east bank fades out, leaving the far bank completely black under the stars. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: elegiac, the end of something. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, city lights, fire, lit windows, people, crowds
- **Refs:** PROP_FELUCCA, LOC_NILE_NIGHT
- **Continuity:** Same plate as 07.10.003; generate glow-on and glow-off states and dissolve in comp if the tool will not fade it.

### 07.10.013 — EXT. NILE, LUXOR - NIGHT — Toward the West Bank cliffs   (8 s)
- **Shot:** Extreme wide, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** PROP_FELUCCA (sailing away, small); the West Bank cliffs
- **Action:** Ahead, the West Bank cliffs, folded and dark. The felucca crosses toward them.
- **Dialogue:** —
- **Sound:** wind in the sail; water; silence into the cut
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, locked-off at water level: {PROP_FELUCCA.SHORT}, its pale sail full against the stars, crosses slowly away from camera over the black water toward the far bank, where bare folded limestone cliffs rise pale grey and dark beyond a black line of palms. Setting: {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: quiet, onward, grieving. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit villages, lanterns, moon, readable faces
- **Refs:** PROP_FELUCCA, LOC_NILE_NIGHT, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Heading WEST to the West Bank (Seq 8 opens in LOC_WEST_BANK_FIELDS, ~03:30). End of sequence 7.

