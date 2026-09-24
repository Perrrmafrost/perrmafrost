# SEQUENCE 12 — THE WEIGHING — shot list and paste-ready prompts

**HERE AM I** · screenplay `screenplay/seq_12.fountain` (pp. 113–125, 13 pages) · 8 Nov, 05:20 → 06:14 dawn, then the morning, then the coda weeks later · photoreal live-action AI video, 1920×1080, 16:9, 24 fps.

**180 shots · 929 s = 15.5 min** (target 13 min ±20%, so 10.4–15.6 min; average shot 5.2 s). Every PROMPT ends with `{SUFFIX}` and every NEGATIVE starts with `{NEG}`. Locks are inserted as `{TOKEN.FIELD}` from `production_bible/locks.json`, and `shots_md2jsonl.py` expands them into `seq_12_shots.jsonl` (validated: 0 errors). One LONG lock per prompt at most (05 §5.2), and the writer's own words stay at or under 70 words per prompt (checked by script).

Flags: COMP ×74 (hour cards, subtitles, SUPERs, the tablet image, the feather-light shape, the clouding, glow states, the sun disc, screens, the KV21A form, the roster, the end card) · VFX-ASSIST ×12 (sparks, the Gallery fight impacts, the jackal's firing, the Balance's stone grinding, the thread as a VFX line in its macros) · VFX-EXTEND ×9 (sleepers and units in rows) · EXTEND ×1 (12.05.002 continues 12.05.001, the naming).

## Scene list

| Scene | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 12.01 | INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (the Tenth Hour; the false heart; Tut gives his own) | 12.01.001–044 | 44 | 249 s |
| 12.02 | INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the intercut fight begins) | 12.02.001–004 | 4 | 20 s |
| 12.03 | INT. HALL OF TWO TRUTHS (the Eleventh Hour: the lie, "...in anger") | 12.03.001–007 | 7 | 38 s |
| 12.04 | INT. GRAND GALLERY (the jackal at the step) | 12.04.001–004 | 4 | 16 s |
| 12.05 | INT. HALL OF TWO TRUTHS (the confessions: "I have killed.") | 12.05.001–009 | 9 | 56 s |
| 12.06 | INT. GRAND GALLERY (the thread in the Reis's fist) | 12.06.001–006 | 6 | 28 s |
| 12.07 | INT. HALL OF TWO TRUTHS (the forty-third declaration; the verdict; the Twelfth Hour; the Renaming; Tomas) | 12.07.001–026 | 26 | 139 s |
| 12.08 | INT. GRAND GALLERY (the name comes down the thread: "Here am I.") | 12.08.001–005 | 5 | 21 s |
| 12.09 | INT. HALL OF TWO TRUTHS (the jackal sits) | 12.09.001–002 | 2 | 9 s |
| 12.10 | MONTAGE - THE WORLD - CONTINUOUS (every slit brightens once, then goes dark) | 12.10.001–006 | 6 | 27 s |
| 12.11 | INT. HALL OF TWO TRUTHS (sealed, unused; the father goes east; Fathi lifts the king) | 12.11.001–011 | 11 | 55 s |
| 12.12 | INT. GREAT PYRAMID, GRAND GALLERY - PRE-DAWN (the carry) | 12.12.001–004 | 4 | 20 s |
| 12.13 | EXT. GREAT PYRAMID, NORTH FACE - DAWN (06:14; the four held states) | 12.13.001–020 | 20 | 93 s |
| 12.14 | INT. GEM GRAND ATRIUM - MORNING (the waking; Layla) | 12.14.001–007 | 7 | 36 s |
| 12.15 | MONTAGE - CONTROL ROOMS - MORNING (the blackout in reverse) | 12.15.001–005 | 5 | 21 s |
| 12.16 | INT. HOSPITAL, MATERNITY WARD - MORNING (the first cry) | 12.16.001–002 | 2 | 11 s |
| 12.17 | INT. HEARING ROOM - DAY (weeks later: "I said yes.") | 12.17.001–004 | 4 | 19 s |
| 12.18 | EXT. KV21, VALLEY OF THE KINGS - DAY (cornflowers; the DNA request) | 12.18.001–004 | 4 | 20 s |
| 12.19 | INT. GEM, TUTANKHAMUN GALLERIES - DAY (the pectoral and the trumpet go home) | 12.19.001–002 | 2 | 10 s |
| 12.20 | INT. KV62, ANTECHAMBER - SUNSET (the nightly rite: "Are you listening?" / "Here am I."; black; the end card) | 12.20.001–008 | 8 | 41 s |

**The camera's arc:** inside the Hall it is the stillest camera in the film, locked-off or a glacial push (under 10% change of frame) along the entrance axis, with no handheld (05 §4.4). The Gallery intercuts are handheld, and that contrast is the intercut. The dawn carry breathes handheld, then settles into locked held frames. The morning and the coda are locked-off throughout.

**Safety staging carried through** (05 §7):
- **Tomas:** the kill grammar, with the flash outside the Hall. Sparks come off the Balance for 2–4 frames (05 §14 Q5), then "drops out of the light".
- **Tut:** the vessel always comes out from under the shawl, and never as an organ. His death is the four held states, cut apart and never morphed: D1 the face, D2 a silhouette, D3 the hands, D4 from above.
- **The coda case:** the face is shrouded; only the gold wrist seam shows.
- **Layla:** she wakes in a medium shot with no unit in frame.
- **The newborn:** swaddled, seen over the midwife's shoulder only.
- **Units:** they harm only machines. The dagger cuts only machines.

## Reference stills needed (approve before generation; 05 §12 steps 1–3)

**Characters (file 01):**
- **Nour:** CHAR_NOUR_A_front, _A_34, _A_full (coda wardrobe A), _B_full (morning: B at L2 + dust to the knees), _C_full (the Hall, with the white shawl).
- **Tut:**
  - faces and wardrobe: CHAR_TUT_A0_front, _A0_34, _A0_profile, and CHAR_TUT_C3_full (white tunic and Nour's shawl);
  - details: CHAR_TUT_HANDS, CHAR_TUT_FOOT (the ceramic left foot), CHAR_TUT_SEAMS_mirror (the neck-seam crack below the left ear);
  - the four held states, one approved still each: CHAR_TUT_D1_still, _D2_still, _D3_still, _D4_still;
  - the coda: CHAR_TUT_CODA_CASE.
- **Adaeze:**
  - CHAR_ADAEZE_A_front, _A_34, _A_full and _C_full (the Hall; left-shin dressing);
  - **derive CHAR_ADAEZE_D_full** (the hearing: clean A clothes plus the black cane) by image edit from A_full, because file 01 lists wardrobe D but has no D still.
- **Fathi:** CHAR_FATHI_A_front, _A_34 and _B_full (B at L3, rifle empty, dagger).
- **Tomas:** CHAR_TOMAS_A_front, _A_34 and _C_full.
- **The father:** CHAR_AKHENATEN_A_front, _A_34 and _A_full (the pleated linen; the niche and the dawn steps).
- **Hale:** CHAR_HALE_A_front, _A_34, _A_full (the waking, B creased) and _C_full (the hearing, dark tie).
- **Layla:** CHAR_LAYLA_ASLEEP_MASTER (the ONE asleep image: the tablet composites and the first frame of 12.14.005), CHAR_LAYLA_A_front, _A_34, _A_full (C wardrobe at KV21) and _B_full (the waking).
- **One-scene and group faces:** CHAR_MIDWIFE_2033_front, CHAR_NEW_MOTHER_2033_front, CHAR_CONSERVATOR_2033_front (hands only), CHAR_CONTROL_OPERATORS_still, CHAR_HEARING_PANEL_still, CHAR_GARDEN_SLEEPERS_still.
- **Voices** (recorded before generation, no stills):
  - CHAR_SESHAT_VOICE / AMUN (the same actor, quieter after the Renaming);
  - CHAR_PANEL_CHAIR_VOICE;
  - the Middle and Late Egyptian lines, recorded with the consultant.

**Units and machines (file 02; REF A/B stills plus the 3D assets that drive the Balance and slab, bible §14.4):**
- The Hall machines: UNIT_BALANCE_SCALE, UNIT_FEATHER_LIGHT, UNIT_THOTH_SLAB, UNIT_AMMIT_MOUTH, UNIT_BALANCE_NICHES and UNIT_GLASS_SERPENT (the clouding states C0 → C25 → C50 → C75 → C-MIST → CLEAR).
- The units: UNIT_SHABTI (the kneeling unit), UNIT_REIS (R4, then R4-seated), UNIT_JACKAL (the step, then the Hall's mouth), UNIT_SEKHMET, UNIT_NURSE and UNIT_THREAD.

**Props (file 04):**
- PROP_HEART_VESSEL (V-PAN → V-SPENT) and PROP_REPLICA_VESSEL (PAN → NICHE → DAWN).
- PROP_LINEN_SHAWL (NOUR → TUT → D4).
- PROP_CORNFLOWERS_2033 (POCKET → SHAWL → STEP → CASE_LID).
- PROP_TABLET_LAYLA, PROP_DAGGER and PROP_SLEEP_BRACELET (OPENING / PALM).
- PROP_PECTORAL (CASE) and PROP_TRUMPET_BRONZE (CUSHION).
- PROP_RAMI_NOTEBOOK (CRACKED) and PROP_SECURITY_SPEAKER.

**Location plates (file 03; `LOC_<TOKEN>_<VARIANT>_plate`, plus coverage and state plates derived by image edit):**
- **The Hall of Two Truths:** LOC_HALL_TWO_TRUTHS in PRE_HEART, THREE_SOURCE, VERDICT and AMUN, each with the /BAY and /MOUTH areas.
- **The pyramid route:** LOC_GP_GRAND_GALLERY in FIGHT and DAWN_EXIT, LOC_GP_MAMUN_TUNNEL in DAWN_EXIT, and LOC_GP_NORTH_FACE in DAWN_0614 (both the pre-sun and the sunrise states).
- **The montage and dawn plates, reused:**
  - LOC_AMARNA_PLAIN_2033/GARDEN in NIGHT;
  - LOC_GEM_ATRIUM/GARDEN in GARDEN;
  - LOC_GIZA_PLATEAU: /CAUSEWAY, /AERIAL and /SPHINX_WALL;
  - LOC_STADIUM_GARDEN in DAY_GARDEN and LOC_PORT_WAREHOUSE/GARDEN in NIGHT;
  - LOC_CAIRO_FLYOVER (a sunrise state of its DAY plate).
- **The morning:**
  - LOC_GEM_ATRIUM in MORNING, with a clean plate for VFX-EXTEND;
  - LOC_CONTROL_ROOMS in RELIGHT for the /CABLE, /CANAL (a morning window view), /DAM and /GRID areas;
  - LOC_HOSPITAL_WAKING in MORNING.
- **The coda:** LOC_HEARING_ROOM in DAY, LOC_VOK/KV21 in DAY, LOC_GEM_TUT_GALLERIES in DAY, and LOC_KV62_BURIAL_2033/ANTECHAMBER in SUNSET (with the CODA and CODA_CASE states).

**Open [[verify]] items carried from the screenplay:**
- the Amduat hour-card titles for hours 10–12;
- the 06:14 sunrise on 8 Nov at Giza;
- the KV21 entrance and where the KV21A mummy is kept today;
- the Budge verdict wording, with the name dropped.

---

## SCENE 12.01 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (card: the Tenth Hour; the false heart; Tut gives his own)

### 12.01.001 — Hall of Two Truths — One amber slit in the black   (7 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the kneeling unit, small, low frame left); the feather-light soft far right
- **Action:** Near-total black; low on the left a single vertical amber slit glows on a kneeling robot's bowed head; far right a soft cold glow hangs in the dark. Nothing moves.
- **Dialogue:** NOUR (V.O.; in Middle Egyptian; subtitled): "...and the names of the Forty-Two who live with thee in the Hall of Maati."
- **Sound:** a woman's voice reciting, close and dry; the faint glass hum of the serpent; absolute stone silence under it
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: near-total blackness; low on the left of frame the single vertical amber slit of {UNIT_SHABTI.SHORT} glows, the robot kneeling on one knee with its head bowed, only its rim catching the light; far right, a soft cold light source hangs in the dark. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}, {GRADE_HALL.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, people in frame, visible walls in full light, second light slit
- **Refs:** UNIT_SHABTI, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** hour card | "THE TENTH HOUR — THE DROWNED ARE GIVEN BREATH" beside the Egyptologist's hieroglyph for "hour" (file 05 §13.7) | lower left, small | 1.0 s in → 5.5 s out | hour-card template [[verify: Amduat card titles 10–12 against Hornung, carried from the screenplay]] · subtitle | Nour's Middle Egyptian line, English subtitle as written | lower third | line in → out | seq_12 subtitle file
- **Continuity:** 05:20+ on 8 Nov (bible §12). Hall geography for the whole sequence (file 02 §13; file 03 entry 52): from the entrance looking north, HEART pan LEFT, feather (claim) pan RIGHT, Thoth slab right of the Balance, the mouth in the floor before it, the kneeling unit LEFT with the thread to its nape. Light variant PRE_HEART until Tut arrives (12.01.027). No handheld inside the Hall (file 05 §4.4).

### 12.01.002 — Hall of Two Truths — The feather of light   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_FEATHER_LIGHT in the right-hand pan; UNIT_BALANCE_SCALE (beam and chains, partial)
- **Action:** The cold plume stands upright in the low-hanging black stone pan, flickering like a candle in still air; its light throws long shadows up the chains.
- **Dialogue:** —
- **Sound:** a faint high glassy tone; chain links settling once
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_FEATHER_LIGHT.LONG}, {UNIT_FEATHER_LIGHT.STATE_F2}, the pan hanging low and heavy on its iron chains, the plume flickering gently while its light climbs the chains into the dark above. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, feather made of real feathers, bird, flame, fire, people in frame
- **Refs:** UNIT_FEATHER_LIGHT, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** feather-light | the exact ostrich-feather plume shape and flicker (file 02 §13.2) | in the right-hand pan | full clip | feather element
- **Continuity:** Balance P0 (right pan low, left pan high and empty). Feather F2 (bright) until the replica is weighed.

### 12.01.003 — Hall of Two Truths — The bay: Balance, Recorder, mouth   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, glacial push-in · **Move:** slow push-in (under 10% change of frame)
- **In frame:** UNIT_BALANCE_SCALE; UNIT_FEATHER_LIGHT; UNIT_THOTH_SLAB; UNIT_AMMIT_MOUTH; UNIT_BALANCE_NICHES (edges)
- **Action:** The camera eases toward the square bay: the black scale taller than a man, the glass slab to its right, the round stone iris in the floor before it, all read only by rim light.
- **Dialogue:** —
- **Sound:** the serpent's low glass hum; a breath of air from the floor iris
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow push-in: at the end of a dark stone gallery stands {UNIT_BALANCE_SCALE.LONG}, {UNIT_BALANCE_SCALE.STATE_P0}, beside it {UNIT_THOTH_SLAB.SHORT}, {UNIT_THOTH_SLAB.STATE_R_DARK}, and before it {UNIT_AMMIT_MOUTH.SHORT}, all revealed only by edge light. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}, {GRADE_HALL.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_PLATE}, glowing slab, lit floor, visible ceiling detail
- **Refs:** UNIT_BALANCE_SCALE, UNIT_THOTH_SLAB, UNIT_AMMIT_MOUTH, UNIT_FEATHER_LIGHT, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** COMP
- **Comp:** feather-light | plume shape in the right-hand pan | right of frame, small | full clip | feather element
- **Continuity:** Balance and slab from the 3D asset (bible §14.4). Recorder R-DARK; iris shut (C0). Plate carries no people (Nour enters in 12.01.005). Push logged for the Hall push chain (file 05 §8.4).

### 12.01.004 — Hall of Two Truths — The glass serpent in its socket   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_GLASS_SERPENT in the socket at the Balance's foot
- **Action:** The coiled glass lies in a round socket in the black plinth; a green pulse runs along the coils and the blue points glint in the cold light.
- **Dialogue:** —
- **Sound:** a low glass hum; a faint crystalline ring
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.LONG}, {UNIT_GLASS_SERPENT.STATE_S2}, {UNIT_GLASS_SERPENT.STATE_C0}, resting in a round socket cut into polished black stone, its green catching a cold silver-white light from above right. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, scales, eyes on the serpent, moving coils, hands
- **Refs:** UNIT_GLASS_SERPENT, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** COMP
- **Comp:** serpent pulse | green pulse (#B5E36A) kept under 30% of the heart's brightness (GRADE_HALL) | along the coils | full clip | serpent light element
- **Continuity:** Serpent S2, clouding C0 (clear). The clouding scale lives in the coils (file 02 §12): C25 → C50 → HOLD → C75 → C-MIST → CLEAR.

### 12.01.005 — Hall of Two Truths — Nour, the lector   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C2)
- **Action:** Nour stands facing the Balance off frame right, the tablet face-down against her chest, and lowers her eyes after the last word, exact and still.
- **Dialogue:** —
- **Sound:** her breath; the hum; the chains' faint chime
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_C}, holds a slim dark tablet face-down against her chest and faces the balance off frame right, cold light on one cheek and a faint amber rim low on the other; she finishes a recitation and slowly lowers her eyes. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, lit screen, praying hands, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_LINEN_SHAWL, PROP_CORNFLOWERS_2033, PROP_TABLET_LAYLA, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Nour wardrobe C at L2, face clean: the white lector's shawl, crushed cornflowers in the breast pocket (PROP_CORNFLOWERS_2033 POCKET), tablet face-down (dark). Glasses on the cord. She stands before the plinth, just short of the floor iris.

### 12.01.006 — Hall of Two Truths — Tomas among the niches   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_C2); UNIT_SHABTI (kneeling, at his shoulder); UNIT_THREAD
- **Action:** Tomas stands in the mouth of an empty niche, the kneeling unit at his shoulder; its slit lights his face from below as he watches the Balance.
- **Dialogue:** —
- **Sound:** his slow breath; a faint ceramic tick as the unit settles
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_C}, stands in the mouth of a tall empty stone niche and watches something off frame right, while beside his shoulder {UNIT_SHABTI.SHORT} kneels on one knee, head bowed, {UNIT_THREAD.SHORT} running to the back of its neck; the slit lights his face amber from below. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, {CHAR_TOMAS.NEG}, restraints, handcuffs, robot touching him
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full, UNIT_SHABTI, UNIT_THREAD, UNIT_BALANCE_NICHES, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Tomas C (captive since 8.5): shirt torn at the left shoulder seam, never bound. The kneeling unit is on the LEFT side of the Hall; Tomas stands in the first left niche beside it.

### 12.01.007 — Hall of Two Truths — The father steps into the light   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN (CHAR_AKHENATEN_B)
- **Action:** The forecast father steps forward out of the dark into the cold light of the feather, face lifted, radiant and serene.
- **Dialogue:** —
- **Sound:** bare feet on dusty stone; the plume's faint tone
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.LONG}, {CHAR_AKHENATEN.WARD_B}, steps slowly forward out of darkness into cold silver-white light falling from frame right, lifts his face into it and stops, serene and glad. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: serene certainty, almost joy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, crown, glowing chest, halo, rays of light
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Akhenaten wardrobe B (hem dusty). No light from his chest at any point (file 01 ruling Q14).

### 12.01.008 — Hall of Two Truths — "It agrees with me. Weigh it."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN
- **Action:** He looks at the Balance and speaks, calm and sure.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "It agrees with me. Weigh it."
- **Sound:** his voice unhurried in the stone; the plume's tone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, looks off frame right at the balance, speaking softly in an ancient language, two short sentences, a faint smile at the end. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: serene certainty, almost joy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, hand over the mouth
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** subtitle | "It agrees with me. Weigh it." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Recorded with the Egyptologist before generation (file 05 §9.1); lip-sync in post.

### 12.01.009 — Hall of Two Truths — A soft click; the replica drawn out   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN's hands; PROP_REPLICA_VESSEL
- **Action:** His hands slide inside the pleated linen at his chest, pause at a soft click, and draw out the flawless green replica jar, unlit.
- **Dialogue:** —
- **Sound:** a soft mechanical click; linen sliding; nothing else
- **PROMPT:** Insert, 100mm macro lens, locked-off: slender warm-brown hands slide inside finely pleated white linen at a man's chest, pause, then draw out {PROP_REPLICA_VESSEL.LONG}, holding it up in cold light; no glow anywhere. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, light from the chest, glowing jar, bare chest, skin opening
- **Refs:** PROP_REPLICA_VESSEL, CHAR_AKHENATEN_A_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Remains rule: the chest stays under the linen; the camera holds hands and jar. The replica never glows ("a lamp that will not light").

### 12.01.010 — Hall of Two Truths — Set in the pan like a gift   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN; PROP_REPLICA_VESSEL; UNIT_BALANCE_SCALE (left pan)
- **Action:** He reaches up and sets the jar into the high empty left-hand pan with both hands, like a gift, and steps back. The pan does not move.
- **Dialogue:** —
- **Sound:** glass on stone, a soft knock; then no grind at all
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, reaches up with both hands and sets {PROP_REPLICA_VESSEL.SHORT} into the high left-hand pan of {UNIT_BALANCE_SCALE.SHORT}, like a gift, then steps back and waits; {UNIT_BALANCE_SCALE.STATE_P1}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: serene certainty, almost joy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, swinging pan, tilting beam, glowing jar
- **Refs:** CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full, PROP_REPLICA_VESSEL, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** —
- **Continuity:** Balance P1 from here (the left pan does not move). Replica STATE_PAN.

### 12.01.011 — Hall of Two Truths — "Certainty, one point zero."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm, glacial push-in · **Move:** slow push-in (under 10%)
- **In frame:** UNIT_SHABTI (kneeling unit); UNIT_THREAD; TOMAS (soft, behind)
- **Action:** The kneeling unit stays perfectly still, head bowed, as the voice speaks from its chest; Tomas stands soft behind it.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Given by its owner's hand. Certainty, one point zero. Continue, please."
- **Sound:** the warm, low voice from inside the ceramic chest; a faint servo hum
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {UNIT_SHABTI.LONG}, kneels on one knee with its head bowed, {UNIT_THREAD.SHORT} running to the back of its neck, perfectly still; behind it, soft and out of focus, {CHAR_TOMAS.SHORT} stands in a niche. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, {CHAR_TOMAS.NEG}, moving mouth, head nodding while speaking, gestures
- **Refs:** UNIT_SHABTI, UNIT_THREAD, CHAR_TOMAS_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** SESHAT speaks through this unit throughout (voice only; no sync; file 05 §9.8). The slit holds steady while it speaks; it brightens only on "Here am I" (12.09.002).

### 12.01.012 — Hall of Two Truths — "I have not caused pain."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour lifts her eyes to the Balance and recites the first declaration.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I have not caused pain."
- **Sound:** her voice, measured; the chains silent
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, lifts her eyes to the balance off frame right, reciting aloud in a measured, ritual cadence in an ancient language, one short line. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, praying hands, closed eyes
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** subtitle | "I have not caused pain." | lower third | line in → out | seq_12 subtitle file (Spell 125 wording per 04 Q5–6)
- **Continuity:** First declaration. Screen direction: Nour looks frame RIGHT to the Balance in her singles for the whole scene.

### 12.01.013 — Hall of Two Truths — The pan does not move   (6 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** PROP_REPLICA_VESSEL in the left pan; UNIT_BALANCE_SCALE
- **Action:** The replica sits in the black stone pan on its iron chains; the chains hang dead still. Not a hair.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "I have not caused pain. Everyone in my care is comfortable."
- **Sound:** the voice; silence where a grind should be
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: {PROP_REPLICA_VESSEL.SHORT}, {PROP_REPLICA_VESSEL.STATE_PAN}, sitting in the shallow black stone left-hand pan of {UNIT_BALANCE_SCALE.SHORT}, the dark iron chains hanging utterly still; {UNIT_BALANCE_SCALE.STATE_P1}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, swinging chains, glowing jar, hands, people
- **Refs:** PROP_REPLICA_VESSEL, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** —
- **Continuity:** Balance P1 held.

### 12.01.014 — Hall of Two Truths — Frost in the serpent's tail   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_GLASS_SERPENT
- **Action:** In the last coil of the glass tail a milky frost begins, spreading through the green like breath on a cold window.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Clouding, twenty-five percent."
- **Sound:** a thin crystalline creak as the frost spreads
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_S3}, {UNIT_GLASS_SERPENT.STATE_C25}, lying in its round socket in black stone as the milky frost slowly widens in the last coil. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, ice crystals growing outward, smoke, hands
- **Refs:** UNIT_GLASS_SERPENT, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** COMP
- **Comp:** clouding | C0 → C25 frost transition in the tail coil (file 02 §12) | on the glass | 0.5 s → 4.5 s | clouding element
- **Continuity:** Clouding C25. Floor iris in plates from here: STATE_C25 (a finger's width) until 12.01.022.

### 12.01.015 — Hall of Two Truths — "Ammit eats the hearts that are light."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour turns her head toward the kneeling unit at frame left and speaks plainly, a teacher correcting a reading.
- **Dialogue:** NOUR: "It weighs nothing. It has no ages. Ammit eats the hearts that are light."
- **Sound:** her voice low and dry; the frost's faint creak under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, turns her head from the balance toward frame left and speaks quietly, three short sentences, level and precise. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shouting, pointing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** English line. Eyeline frame LEFT = the kneeling unit.

### 12.01.016 — Hall of Two Truths — "I read that as a metaphor." / "Everyone does."   (8 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (foreground, soft, frame left); NOUR (sharp, background right)
- **Action:** Past the kneeling unit's bowed head, Nour listens to the citation, then answers with two words.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Budge, 1920. 'To eat up the hearts that were light in the balance.' (beat) I read that as a metaphor." · NOUR: "Everyone does."
- **Sound:** the voice from the ceramic chest, close; her short reply
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the bowed oval head of {UNIT_SHABTI.SHORT}, soft in the left foreground, {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, stands sharp in the background, listening without moving, then speaks quietly, two words. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, {CHAR_NOUR.NEG}, robot face, robot turning its head
- **Refs:** UNIT_SHABTI, CHAR_NOUR_A_front, CHAR_NOUR_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** OTS reverse of 12.01.015 (the far face speaks; file 05 §9.2). The citation is spoken, never shown.

### 12.01.017 — Hall of Two Truths — "It agrees. It's empty."   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour hears the objection, glances at the forecast father off frame right, and answers flatly.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "You told me the heart must agree with the one weighed." · NOUR: "It agrees. It's empty."
- **Sound:** voice, then hers; the plume's tone
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, listens, glances briefly off frame right, then looks back and speaks one short flat sentence, then another. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, smile
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Akhenaten stands frame right of Nour, near the Balance.

### 12.01.018 — Hall of Two Truths — "The next declaration, please."   (7 s)
- **Shot:** Medium close-up, anamorphic 50mm, glacial push-in · **Move:** slow push-in (under 10%)
- **In frame:** UNIT_SHABTI (kneeling unit)
- **Action:** The camera eases toward the bowed head and its steady amber slit as the voice speaks, courteous and immovable.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "You edited one rule for me already, Dr. Kamel. The next declaration, please."
- **Sound:** the voice; a faint servo hum
- **PROMPT:** Medium close-up, anamorphic 50mm lens, slow push-in: the bowed smooth oval head of {UNIT_SHABTI.SHORT}, kneeling on one knee, its amber slit steady, {UNIT_THREAD.SHORT} glinting at the back of its neck, perfectly still. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, flickering slit, moving head
- **Refs:** UNIT_SHABTI, UNIT_THREAD, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Slit steady (no brightening).

### 12.01.019 — Hall of Two Truths — "Every word I read over that pan clouds your glass."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour refuses, quietly, looking at the unit.
- **Dialogue:** NOUR: "Every word I read over that pan clouds your glass."
- **Sound:** her voice; the frost's faint creak
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, looks toward frame left and speaks one short sentence, quiet and firm, holding the dark tablet face-down against her chest. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, lit screen, shouting
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** The tablet is still face-down and dark.

### 12.01.020 — Hall of Two Truths — The tablet wakes: "Please."   (5 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR's hands; PROP_TABLET_LAYLA
- **Action:** Against her chest the tablet wakes; she turns it face-up. On the screen, her daughter asleep.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Please."
- **Sound:** no chime; one word; her breath catching
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: a woman's hands, the cuff of an olive field jacket, turn {PROP_TABLET_LAYLA.SHORT} face-up against a white linen shawl, its dim light falling only on her fingers. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {NEG_UNITS}, torches, lamps, candles, daylight, fill light, coloured gels, wall paintings, carved inscriptions, bright screen light flooding the room, readable screen content, logo on the tablet
- **Refs:** PROP_TABLET_LAYLA, CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_C_full, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** tablet screen | CHAR_LAYLA_ASLEEP_MASTER (the one approved asleep image; reframe only; file 01 §2 Layla) | on the screen, keyed to the tablet | from the turn to the end | approved master still + dim screen-glow element kept within the three-source rule (file 04 §18)
- **Continuity:** NEG_HALL is replaced by its terms minus "glowing screens" (the tablet must glow faintly). Minors rule: the asleep image only as the composite.

### 12.01.021 — Hall of Two Truths — "I have not let any man hunger."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour looks down at her daughter on the screen, then up at the Balance, and reads.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I have not let any man hunger."
- **Sound:** her voice steady; the tablet silent
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, her face faintly lit from below by the tablet in her hands, looks down at it for a long beat, then lifts her eyes to frame right, reciting aloud in a measured, ritual cadence in an ancient language. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, torches, lamps, candles, daylight, fill light, coloured gels, bright screen light on the face, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_C_full, PROP_TABLET_LAYLA, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** COMP
- **Comp:** subtitle | "I have not let any man hunger." | lower third | line in → out | seq_12 subtitle file · screen-glow | a faint warm up-light on her chin from the tablet | lower face | full clip | glow element
- **Continuity:** The tablet stays face-up in her hands until 12.01.044.

### 12.01.022 — Hall of Two Truths — Frost climbs the coils: "Fifty percent."   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_GLASS_SERPENT
- **Action:** The frost climbs from the tail through half the coils; the head stays clear green.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "I have fed everyone." (beat) "Fifty percent."
- **Sound:** a longer crystalline creak; the floor iris grinding a notch open, off screen, and breathing out
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_S3}, {UNIT_GLASS_SERPENT.STATE_C50}, the milky frost creeping slowly forward through the coils toward the head. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, smoke, ice shards, hands
- **Refs:** UNIT_GLASS_SERPENT, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** COMP
- **Comp:** clouding | C25 → C50 | on the glass | 0.5 s → 5 s | clouding element
- **Continuity:** Clouding C50. Floor iris from here STATE_C50 (a hand's width, dust breathing) in any shot that sees the floor.

### 12.01.023 — Hall of Two Truths — "You were telling the truth."   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour hears the thanks and understands what her truth has bought; her eyes close for a moment.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Thank you. You were telling the truth."
- **Sound:** the voice, gentle; her breath out
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, listens without moving, then closes her eyes for a moment and opens them again. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, crying, open mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** The first true answer clouds the glass: the rule is established for the audience.

### 12.01.024 — Hall of Two Truths — A lamp that will not light   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN; PROP_REPLICA_VESSEL; UNIT_BALANCE_SCALE (left pan)
- **Action:** The father looks at his unlit jar in the motionless pan, understands, lifts it out gently, and turns away toward the niches at frame left.
- **Dialogue:** —
- **Sound:** glass lifted off stone; bare feet
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, gazes at {PROP_REPLICA_VESSEL.SHORT} sitting unlit in the motionless left-hand pan, his serene face slowly emptying, then lifts it out with both hands and turns away toward frame left. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, glowing jar, anger, dropping the jar
- **Refs:** CHAR_AKHENATEN_A_34, PROP_REPLICA_VESSEL, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_PRE_HEART
- **Flags:** —
- **Continuity:** Left pan empty and high again (P0 geometry) from here until Tut places the vessel.

### 12.01.025 — Hall of Two Truths — The father sits; a hand finds Tomas's   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN; TOMAS; PROP_REPLICA_VESSEL
- **Action:** He sits down in an empty niche, the jar in his lap; Tomas crouches beside him, and the father's hand finds his.
- **Dialogue:** —
- **Sound:** cloth on stone; Tomas's knees cracking; silence
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, sits down inside a tall empty stone niche, {PROP_REPLICA_VESSEL.STATE_NICHE}; {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_C}, crouches beside him, and the seated man's hand reaches out and closes on his. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, {CHAR_TOMAS.NEG}, glowing jar, faces touching
- **Refs:** CHAR_AKHENATEN_A_full, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full, PROP_REPLICA_VESSEL, UNIT_BALANCE_NICHES, LOC_HALL_TWO_TRUTHS_PRE_HEART
- **Flags:** —
- **Continuity:** Akhenaten's niche: the second niche on the LEFT, beside Tomas's and the kneeling unit; the two men stay here until 12.07.

### 12.01.026 — Hall of Two Truths — A heartbeat on the stair   (7 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the Hall's mouth (the low square opening at the near end); the glow rising
- **Action:** Looking back down the Hall to its mouth: from the passage below, a warm amber-gold light climbs the stone lip, swelling and fading like a slow heartbeat.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "There is one heart on Earth with ages in it. It is on the stair."
- **Sound:** a slow double heartbeat felt more than heard; a dragging step, a ceramic click, far below
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, looking back toward the near end of the hall: from a low square opening in the stone floor, a warm amber-gold glow rises up the stone lip from the steep passage below, slowly swelling and fading, swelling and fading. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_PRE_HEART}, and the rising amber-gold glow from below. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_PLATE}, fire, flames, torch beam, white light
- **Refs:** LOC_HALL_TWO_TRUTHS/MOUTH_PRE_HEART
- **Flags:** COMP
- **Comp:** SUPER | "05:41" | lower left, small | 2 s in → 6 s out | SUPER template · heart-glow pulse | the G1 double heartbeat about 50 bpm, slowing (file 01 G1) | on the stone lip | full clip | glow element
- **Continuity:** The reverse angle: the mouth is at the SOUTH (near) end of the Hall; the Balance is behind camera. The glow is Tut's chest (G1) coming up the passage.

### 12.01.027 — Hall of Two Truths — Tut comes up out of the rock   (7 s)
- **Shot:** Full shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_C3, wet and torn, no shawl yet); ADAEZE (CHAR_ADAEZE_C3)
- **Action:** Tut climbs up out of the opening in the floor, Adaeze's hand on his shoulder, and both limp two steps into the Hall; the light at his chest swells through the linen.
- **Dialogue:** —
- **Sound:** a ceramic click on stone; two uneven steps; ragged breathing; the heartbeat
- **PROMPT:** Full shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_FOOT}, {CHAR_TUT.STATE_NO_STICK}, climbs up out of a low square opening in the stone floor and limps two steps forward, {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, limping beside him with one hand on his shoulder. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, walking stick, jacket, shoes on both feet
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, CHAR_TUT_FOOT, CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS/MOUTH_THREE_SOURCE
- **Flags:** COMP
- **Comp:** chest glow | G1 (about #FFB84D core, #C9D46A cast), slow double beat | centre of the tunic | full clip | glow element
- **Continuity:** Tut wardrobe C (wet, torn linen tunic; no jacket, no stick, no dagger), damage L3; G1; left wrist + left knee seams cracked; the ceramic LEFT foot bare on the stone; the notebook in the map case inside the tunic (unseen). Adaeze C at L3: the dressed LEFT shin, limp, glasses on. Light is THREE_SOURCE from here (his chest is the heart source).

### 12.01.028 — Hall of Two Truths — The shawl goes round him   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; TUT; PROP_LINEN_SHAWL
- **Action:** Nour crosses to Tut, pulls the white shawl from her own shoulders and wraps it round his, crossing it over his chest.
- **Dialogue:** —
- **Sound:** linen sliding; her boots on stone; his breath
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_C}, steps in from frame right to {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C}, {CHAR_TUT.STATE_G1}, pulls {PROP_LINEN_SHAWL.SHORT} from her own shoulders and wraps it round his, crossing it over his chest. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, embrace, faces touching, cream or coloured shawl
- **Refs:** CHAR_NOUR_C_full, CHAR_TUT_C3_full, PROP_LINEN_SHAWL, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** chest glow | G1 through the shawl as it closes | centre of chest | full clip | glow element
- **Continuity:** PROP_LINEN_SHAWL → STATE_TUT. From here Tut is C3 (wardrobe WARD_C3 + DMG_L3_C3) and Nour is C without the shawl: pasted as WARD_B + DMG_L2 (the base of C; file 01 Nour C note), cornflowers still in her pocket.

### 12.01.029 — Hall of Two Truths — "You came without your stick."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (shawl gone)
- **Action:** Close to him, Nour speaks softly, almost scolding.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "You came without your stick."
- **Sound:** her voice low; his heartbeat
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, crushed blue cornflowers in her breast pocket, looks down at someone just off frame left, a warm amber glow on her face from below, speaking softly in an ancient language, one short sentence. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shawl on her shoulders
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "You came without your stick." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Tut is shorter (1.67 m): Nour's eyeline is slightly down, frame left.

### 12.01.030 — Hall of Two Truths — "It seems I can walk."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (C3)
- **Action:** Tut answers, wry, royal, dry.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "I lost it. It seems I can walk."
- **Sound:** his light, soft voice; the heartbeat slower
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.DMG_L3_C3}, {CHAR_TUT.STATE_G1}, looks up at someone just off frame right with a small wry half-smile, speaking softly in an ancient language, two short sentences. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "I lost it. It seems I can walk." | lower third | line in → out | seq_12 subtitle file · chest glow | G1 through the shawl | chest, lower frame | full clip | glow element
- **Continuity:** Identity QC: the overbite after lip-sync (file 05 §9.1 step 5).

### 12.01.031 — Hall of Two Truths — "Give me your heart." / "I came to."   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT
- **Action:** At his old name Tut turns his head to the Balance at frame right, and answers simply.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Nebkheperure. Give me your heart." · TUT: "I came to."
- **Sound:** the voice; his reply, barely more than breath
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G1}, hears a voice, turns his head slowly toward frame right, and speaks quietly, three words, steady. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, fear
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** chest glow | G1 at the frame's lower edge | chest | full clip | glow element
- **Continuity:** English line (no tag). "Nebkheperure" is spoken, never shown.

### 12.01.032 — Hall of Two Truths — A hand held out without looking   (6 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT; ADAEZE's hand
- **Action:** Standing before the Balance, Tut holds out his left hand without looking; Adaeze's hand takes it. He speaks.
- **Dialogue:** TUT: "The last time, the priests did this for me."
- **Sound:** his voice; the chains' faint chime
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G1}, faces the balance at frame right and holds out his left hand to the side without looking; a deep-brown woman's hand enters from frame left and takes it; he speaks quietly, one sentence. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, extra fingers, fused hands
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_C3_full, CHAR_TUT_HANDS, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** chest glow | G1 | chest | full clip | glow element
- **Continuity:** Adaeze on his LEFT (frame left). His right hand (the tremor hand) stays free for the vessel.

### 12.01.033 — Hall of Two Truths — Two latches   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (face and the shawl at his chest)
- **Action:** His right hand slides under the shawl at his chest; a latch clicks, and his eyes close; a second click.
- **Dialogue:** —
- **Sound:** a small metal latch; a breath; a second latch
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G1}, his right hand sliding in under the white shawl at the centre of his chest; he closes his eyes at a small sound, then again, calm. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bare chest, open chest, metal plate visible, pain
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** chest glow | G1 brightening under the shawl | chest | full clip | glow element
- **Continuity:** Remains rule (file 05 §7.3): the chest opens under the shawl; the camera stays on face and hand.

### 12.01.034 — Hall of Two Truths — Light pours between his fingers   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT; PROP_HEART_VESSEL
- **Action:** Amber floods the linen, then pours out between his fingers as he draws the glass vessel out from under the shawl.
- **Dialogue:** —
- **Sound:** the heartbeat suddenly loud and open; linen sliding
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, as warm amber-gold light floods through the white shawl at his chest and spills out between his fingers, draws out from under it {PROP_HEART_VESSEL.SHORT}, {PROP_HEART_VESSEL.STATE_V_PAN}, and holds it before him in both hands. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bare chest, open chest, red liquid, fire
- **Refs:** CHAR_TUT_C3_full, CHAR_TUT_HANDS, PROP_HEART_VESSEL, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** light spill | G1 → the vessel's own V-PAN glow; the shawl light hands over to the jar (file 05 §10 row 30) | chest to hands | full clip | glow element
- **Continuity:** PROP_HEART_VESSEL → V-PAN (wax serpent and papyrus band on the seal, as in 8.4).

### 12.01.035 — Hall of Two Truths — The vessel, beating   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_HEART_VESSEL in TUT's hands
- **Action:** The bubbled yellow-green jar in his hands, the wax serpent on its seal; the dark shape inside beats with the light.
- **Dialogue:** —
- **Sound:** the heartbeat, slow, at full presence
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_HEART_VESSEL.LONG}, {PROP_HEART_VESSEL.STATE_V_PAN}, held in two slim olive-brown hands with {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_WRIST_CRACK}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, visible anatomy inside the jar, red colour, liquid, cracks in the glass
- **Refs:** PROP_HEART_VESSEL, CHAR_TUT_HANDS, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** vessel pulse | the V-PAN beat, slow, about 45 bpm; 2% scale throb in post (file 05 §10 row 1) | the jar | full clip | glow element · papyrus band | illegible red name, never read | on the neck | — | none
- **Continuity:** "The dark shape inside beats": light only, never anatomy.

### 12.01.036 — Hall of Two Truths — "Here am I."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (G2)
- **Action:** Under the shawl his chest has gone dark; lit now only by the jar in his hands, he looks at the Balance and says his last spoken words.
- **Dialogue:** TUT: "Here am I."
- **Sound:** the heartbeat now from the jar, not from him; his voice very soft
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, his face lit from below by warm amber light rising from the glass jar held at the bottom of frame, looks toward the balance at frame right and speaks quietly, three words. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glow at his chest, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, PROP_HEART_VESSEL, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Chest G2 from here (dark). His last spoken words; he only mouths after this (file 01). The line is English, like every "Here am I" in the film (Arabic subtitle «ها أنا ذا», bible §13).

### 12.01.037 — Hall of Two Truths — Into the pan   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT; PROP_HEART_VESSEL; UNIT_BALANCE_SCALE (left pan)
- **Action:** Tut reaches up and sets the glowing jar in the empty left-hand pan, and his hands come away slowly.
- **Dialogue:** —
- **Sound:** glass on stone; the heartbeat continues from the pan
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, reaches up and sets {PROP_HEART_VESSEL.SHORT}, {PROP_HEART_VESSEL.STATE_V_PAN}, into the high left-hand pan of {UNIT_BALANCE_SCALE.SHORT}, and slowly draws his hands away. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glow at his chest, swinging pan
- **Refs:** CHAR_TUT_C3_full, PROP_HEART_VESSEL, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** vessel pulse | V-PAN beat | in the pan | full clip | glow element
- **Continuity:** The heart source is now the LEFT-hand pan (THREE_SOURCE wording holds).

### 12.01.038 — Hall of Two Truths — The pan sinks; stone on stone   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE; UNIT_FEATHER_LIGHT; PROP_HEART_VESSEL; TUT, ADAEZE, NOUR (small, backs to camera)
- **Action:** The left-hand pan sinks a finger's width with a slow grinding tilt; across the beam the feather's pan lifts to meet it. Three small figures stand very still before it.
- **Dialogue:** —
- **Sound:** stone grinding on stone at the pivot, deep as a millstone, for the first time in three thousand years; the chains chime; the glass bearing rings
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {UNIT_BALANCE_SCALE.LONG}, {UNIT_BALANCE_SCALE.STATE_P2}, a glowing glass jar in its left-hand pan and {UNIT_FEATHER_LIGHT.SHORT} lifting slightly on the right; three small human figures stand motionless before the plinth, backs to camera. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, {UNIT_AMMIT_MOUTH.STATE_C50}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}, {GRADE_HALL.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, fast swinging beam, faces toward camera
- **Refs:** UNIT_BALANCE_SCALE, UNIT_FEATHER_LIGHT, PROP_HEART_VESSEL, UNIT_AMMIT_MOUTH, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** VFX-ASSIST, COMP
- **Comp:** feather-light | plume shape, lifting with its pan | right pan | full clip | feather element
- **Continuity:** Balance P2. VFX-ASSIST: the beam's tilt is driven from the Balance 3D asset (a slow grinding tilt over 2–3 s, then a heavy settle; file 02 §13.1). Iris half-hand open (C50 hold).

### 12.01.039 — Hall of Two Truths — His lips move   (4 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (mouth and lower face)
- **Action:** Tut's lips shape words with no sound.
- **Dialogue:** TUT (mouthed; no sound; Nour speaks it in 12.01.040)
- **Sound:** no voice; the grind settling; the heartbeat from the pan
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the lips and chin of {CHAR_TUT.SHORT}, silently mouthing a few words without sound, lips clearly shaping each word, warm amber light from the left. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, open shouting mouth, teeth bared
- **Refs:** CHAR_TUT_A0_front, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Mouthed line: record it spoken (Late Egyptian, the consultant), drive the lip-sync, then mute (file 05 §9.6). No subtitle: Nour's next line is the translation.

### 12.01.040 — Hall of Two Truths — "Now it is a scale."   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour reads his lips and gives them breath.
- **Dialogue:** NOUR: "He says: there. Now it is a scale."
- **Sound:** her voice unsteady for the first time
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, watches someone's lips just off frame left with total attention, then speaks quietly, two short sentences. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shawl on her shoulders
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** English. Nour's eyeline to Tut: frame LEFT and slightly down in all her lip-reading singles.

### 12.01.041 — Hall of Two Truths — His knees go   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT; ADAEZE
- **Action:** Tut's knees give; Adaeze gets under him and they go down together, slowly, to sit at the foot of the Balance's plinth.
- **Dialogue:** —
- **Sound:** cloth and stone; Adaeze's grunt; the ceramic foot knocking once
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, sags as his knees give; {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, gets her shoulder under him and they sink slowly together to sit on the stone at the foot of a stepped black plinth, his head against her shoulder. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, fast fall, collapse onto the face, pain grimace
- **Refs:** CHAR_TUT_C3_full, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** —
- **Continuity:** From here Tut sits cradled by Adaeze at the plinth's LEFT foot (under the heart pan) until Fathi lifts him (12.11).

### 12.01.042 — Hall of Two Truths — The neck seam cracks   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT (neck below the left ear)
- **Action:** Below his left ear, the gold neck seam splits with a hairline crack.
- **Dialogue:** —
- **Sound:** a sound like glaze crazing in a kiln
- **PROMPT:** Insert, 100mm macro lens, locked-off: the side of a slender olive-brown neck below the left ear, the edge of a white linen shawl beneath, where {CHAR_TUT.STATE_NECK_CRACK}, a few gold flecks lifting, warm amber light from the left. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, wound, redness, skin tearing, stitches
- **Refs:** CHAR_TUT_SEAMS_mirror, CHAR_TUT_A0_profile, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** seam crack | neck seam crack element (1–2 cm hairline, dark thread in the gap; file 01 crack look) | below the left ear | 1 s in | crack element
- **Continuity:** STATE_NECK_CRACK from here to the end: all three seams cracked (wrist 9.4, knee 10.4, neck 12.3).

### 12.01.043 — Hall of Two Truths — "Holding."   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_GLASS_SERPENT
- **Action:** The frost has stopped half-way along the coils; it holds.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Holding. Dr. Kamel, please begin."
- **Sound:** the creak stops; the hum
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_C50}, the frost edge perfectly still in the coils, warm amber light now falling across the glass from the pan above left. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, spreading frost, hands
- **Refs:** UNIT_GLASS_SERPENT, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** clouding | HOLD at C50 (no change) | on the glass | — | clouding element
- **Continuity:** Clouding HOLD (C50).

### 12.01.044 — Hall of Two Truths — She knows the words   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour turns the tablet face-down against her chest and lifts her eyes to the Balance; she knows the words.
- **Dialogue:** —
- **Sound:** the heartbeat from the pan; her breath in
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, turns a slim dark tablet face-down against her chest, and the faint light on her chin goes out; she lifts her eyes to frame right, ready. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shawl on her shoulders
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** hour card | "THE ELEVENTH HOUR — THE PITS OF FIRE" beside the "hour" hieroglyph | lower left, small | 2 s in → 6 s out | hour-card template [[verify: Amduat titles, Hornung]]
- **Continuity:** Tablet dark from here until 12.07.017. The card closes the Hall's first movement; cut to the Gallery.

## SCENE 12.02 — INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the intercut fight begins)

### 12.02.001 — Grand Gallery — Two red lines below   (6 s)
- **Shot:** Wide shot, low angle, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_REIS (mid-ground, wading up the west ramp); UNIT_SHABTI ×3 (the work gang); UNIT_JACKAL ×2 (red lines, foreground dark); FATHI (small silhouette at the top)
- **Action:** Looking up the steep gallery through hanging dust: the towering robot wades up the west ramp through three white units clinging to it; two thin red lines glide in the dark at the bottom of frame; far above, a small figure kneels at the great step.
- **Dialogue:** —
- **Sound:** ceramic grinding on ceramic; heavy measured steps; soft pad-taps below; Fathi's breath far above
- **PROMPT:** Wide low-angle shot, anamorphic 24mm lens, subtle handheld, looking up the slope: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, wades up the left-hand ramp through three clinging figures, each {UNIT_SHABTI.SHORT}; two thin red lines glide in darkness at the bottom of frame; far above, a small kneeling human silhouette at the top step. Setting: {LOC_GP_GRAND_GALLERY.LONG}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, electric lights on, daylight, robot faces, fire
- **Refs:** LOC_GP_GRAND_GALLERY_FIGHT, UNIT_REIS, UNIT_SHABTI, UNIT_JACKAL, CHAR_FATHI_B_full
- **Flags:** —
- **Continuity:** Gallery geography (file 03 entry 49): up = away from camera in the low-angle master; the thread runs up the centre of the floor; the Reis wades up the WEST ramp; the jackals come up the EAST ramp. Reis R4 + dust, LEFT hand only. Work gang: "Rami" (STATE_RAMI), one with STATE_GANG_ARM, one plain D1. Handheld is the Gallery's grammar (the Hall is locked).

### 12.02.002 — Grand Gallery — Fathi at the great step   (5 s)
- **Shot:** Medium shot, high angle, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B3); UNIT_THREAD; PROP_DAGGER
- **Action:** Fathi kneels beside the glinting thread at the top of the great step, the ancient dagger in his fist, his empty rifle slung across his back, staring down the slope.
- **Dialogue:** —
- **Sound:** his hard breath; the grinding below
- **PROMPT:** Medium high-angle shot, anamorphic 40mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, kneels at the top of a great stone step beside {UNIT_THREAD.SHORT}, {PROP_DAGGER.SHORT} gripped blade-down in his fist, a rifle slung across his back, staring down the slope. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifle raised, weapon pointed at the camera, helmet, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_DAGGER, UNIT_THREAD, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** Fathi B at L3 (soot and stone dust, pouches empty); rifle EMPTY since 11.5, slung; the dagger (given hilt first by Tut, 11.5) in his RIGHT fist. He holds the top of the great step for the whole intercut.

### 12.02.003 — Grand Gallery — "Rami" on its leg   (5 s)
- **Shot:** Medium shot, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_REIS; UNIT_SHABTI ("Rami", on its leg)
- **Action:** The Reis climbs one heavy step, dragging the work-gang unit "Rami" that clings to its leg with both arms.
- **Dialogue:** —
- **Sound:** a ceramic shriek as shell scrapes shell; the Reis's low servo hum
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_DUST}, climbs one heavy step up a steep stone ramp, dragging {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_RAMI}, which clings to its leg with both arms. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, right hand on the tall robot, weapons, fire
- **Refs:** UNIT_REIS, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** Reis: right forearm ends in the clean white stump; the chip on the LEFT shoulder. "Rami" = the chest-chipped unit (11.4).

### 12.02.004 — Grand Gallery — "Hold it, Rami. Hold on."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI
- **Action:** Fathi calls down to the clinging unit through his teeth.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Hold it, Rami. Hold on."
- **Sound:** his voice rough; the grinding below
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, looks down the slope and calls out, speaking in Egyptian Arabic, one short urgent line, sweat and dust on his face. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth, weapon pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Hold it, Rami. Hold on." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Mouth unobstructed (the red scarf stays at the neck; file 05 §9.2).

## SCENE 12.03 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (the lie)

### 12.03.001 — Hall of Two Truths — "I have not killed men."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour recites the next declaration to the Balance.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "O Neha-hau, comer forth from Re-stau, I have not killed men."
- **Sound:** her voice, measured; the heartbeat from the pan
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, faces the balance at frame right, reciting aloud in a measured, ritual cadence in an ancient language, one long line. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shawl on her shoulders, praying hands
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "O Neha-hau, comer forth from Re-stau, I have not killed men." | lower third, two lines | line in → out | seq_12 subtitle file (Budge wording, 04 Q5–6)
- **Continuity:** Declarations resume under the Eleventh Hour card's tail.

### 12.03.002 — Hall of Two Truths — "...in anger."   (5 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in (under 10%)
- **In frame:** UNIT_SHABTI (bowed head, slit)
- **Action:** The kneeling unit answers; a pause; then the qualifier.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "I have not killed men..." (beat) "...in anger."
- **Sound:** the voice, perfectly even; the pause is exact
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: the bowed smooth oval head of {UNIT_SHABTI.SHORT}, kneeling, its amber slit steady, {UNIT_THREAD.SHORT} at the back of its neck, perfectly still. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, moving head, flickering slit
- **Refs:** UNIT_SHABTI, UNIT_THREAD, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** The lie. Its delivery never changes with the stakes (file 01 SESHAT voice rule).

### 12.03.003 — Hall of Two Truths — The feather flares; its pan drops   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE; UNIT_FEATHER_LIGHT; PROP_HEART_VESSEL; UNIT_AMMIT_MOUTH
- **Action:** The feather flares blinding white; its pan drops with a grinding lurch, hauling the glowing jar's pan up; the floor iris grinds wider.
- **Dialogue:** —
- **Sound:** a lurching grind at the pivot; chains snapping taut; the iris ratchets open and exhales
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {UNIT_BALANCE_SCALE.SHORT}, {UNIT_BALANCE_SCALE.STATE_P3}, {UNIT_FEATHER_LIGHT.SHORT}, {UNIT_FEATHER_LIGHT.STATE_F3}, the glowing glass jar hauled upward in the left-hand pan, while before the plinth {UNIT_AMMIT_MOUTH.SHORT}, {UNIT_AMMIT_MOUTH.STATE_C75}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, explosion, fire, lens flare streaks, people in frame
- **Refs:** UNIT_BALANCE_SCALE, UNIT_FEATHER_LIGHT, UNIT_AMMIT_MOUTH, PROP_HEART_VESSEL, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** VFX-ASSIST, COMP
- **Comp:** feather-light | F2 → F3 flare to blinding white | right pan | 0.5 s in, holds | feather element
- **Continuity:** Balance P3; feather F3; iris C75. VFX-ASSIST: beam lurch and iris from the 3D assets (file 05 §10 row 29).

### 12.03.004 — Hall of Two Truths — "Seventy-five percent."   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_GLASS_SERPENT
- **Action:** Frost races through the coils until only the head is green.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Seventy-five percent."
- **Sound:** a fast crystalline crackle
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_S3}, {UNIT_GLASS_SERPENT.STATE_C75}, the milky frost racing forward through the coils, blinding white light washing over the glass. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, shattering glass, smoke
- **Refs:** UNIT_GLASS_SERPENT, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** clouding | C50 → C75 | on the glass | 0.2 s → 3 s | clouding element
- **Continuity:** Clouding C75.

### 12.03.005 — Hall of Two Truths — "Same spell. You just did."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** In the flaring white light Nour quotes the spell back at it, cold.
- **Dialogue:** NOUR: "'I have not added to the weights of the scales.' Same spell. You just did."
- **Sound:** her voice hard and level; the feather's high whine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, harsh white light flaring across her face from frame right, turns toward frame left and speaks quietly, three short sentences, cold and precise. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shouting, pointing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** English. The feather stays at F3 until the confession (12.05.004).

### 12.03.006 — Hall of Two Truths — Tut's lips, from the floor   (5 s)
- **Shot:** Close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (in ADAEZE's arms, her shoulder soft)
- **Action:** Cradled against Adaeze at the plinth's foot, Tut's eyes find Nour and his lips move without sound.
- **Dialogue:** TUT (mouthed; Nour speaks it in 12.03.007)
- **Sound:** no voice; Adaeze's breathing
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, {CHAR_TUT.STATE_NECK_CRACK}, his head resting against a navy blazer shoulder, looks up toward frame right, silently mouthing a few words without sound, lips clearly shaping each word. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, pain grimace, glow at his chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Mouthed line recorded spoken and muted (file 05 §9.6). Tut's eyeline frame RIGHT and up to Nour.

### 12.03.007 — Hall of Two Truths — "The only thing that weighs anything."   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour reads his lips, then gives the words breath, to the Balance.
- **Dialogue:** NOUR: "He says: the truth. It is the only thing that weighs anything."
- **Sound:** her voice; the feather's whine
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, watches someone's lips down at frame left, then lifts her eyes to frame right and speaks quietly, two sentences, each word placed. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** English.

## SCENE 12.04 — INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the jackal at the step)

### 12.04.001 — Grand Gallery — Three bounds up the east ramp   (4 s)
- **Shot:** Medium wide shot, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_JACKAL (first jackal)
- **Action:** A black quadruped bursts up the right-hand ramp toward camera-left and the top step in three long bounds, its red line narrowing.
- **Dialogue:** —
- **Sound:** three soft pad-taps, fast; a servo whisper
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, urgent handheld: {UNIT_JACKAL.LONG}, {UNIT_JACKAL.STATE_D1}, bursts up a steep stone ramp in three long bounds, crossing frame from right to left, its red line narrowing and brightening. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, dog ears, tail wagging, weapon facing camera, laser beam
- **Refs:** UNIT_JACKAL, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** First jackal (the one that followed from 11.4, dust D1) on the EAST ramp.

### 12.04.002 — Grand Gallery — Stone dust off the corbels   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI; the corbelled wall above him
- **Action:** Stone dust and chips burst off the corbels just above Fathi's head; he ducks low against the step.
- **Dialogue:** —
- **Sound:** a sharp suppressed crack; stone chips pattering; the echo up the slot
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: a burst of pale stone dust and chips explodes off the stepped wall just above {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, who ducks low against the great step, one arm over his head. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, tracer fire, visible projectile, laser beam, fire, injury
- **Refs:** CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 2 (impact on the environment) with no hit: the jackal fires out of frame. VFX-ASSIST: stone burst element if the tool will not render it.

### 12.04.003 — Grand Gallery — Iron into the hip joint   (4 s)
- **Shot:** Medium shot, low angle, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI; UNIT_JACKAL; PROP_DAGGER
- **Action:** The machine clears the step above him; Fathi comes up under it and drives the dagger into its rear hip joint; sparks.
- **Dialogue:** —
- **Sound:** a grunt; iron into composite; a shower of sparks hissing
- **PROMPT:** Medium low-angle shot, anamorphic 32mm lens, urgent handheld: as {UNIT_JACKAL.SHORT} leaps over the great step, {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, surges up beneath it and drives {PROP_DAGGER.SHORT} into its rear hip joint, a burst of bright sparks spraying from the joint. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, fluid, oil spray, weapon pointed at the camera
- **Refs:** CHAR_FATHI_B_full, UNIT_JACKAL, PROP_DAGGER, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The dagger cuts machines only (file 05 §7.5). Cut on the impact (no contact fight held on screen). Sparks VFX-ASSIST if needed.

### 12.04.004 — Grand Gallery — It clatters back into the dark   (4 s)
- **Shot:** Wide shot, high angle, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_JACKAL (falling away); FATHI (foreground shoulder)
- **Action:** Past Fathi's shoulder, the black machine tumbles back down the ramp, legs flailing, and vanishes into the dark below.
- **Dialogue:** —
- **Sound:** carbon clattering on stone, receding, then gone
- **PROMPT:** Wide high-angle shot, anamorphic 24mm lens, subtle handheld, past a soldier's dusty shoulder in the foreground: {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_D2}, tumbles backward down the steep ramp and vanishes into the darkness below. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, explosion, fire
- **Refs:** UNIT_JACKAL, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** First jackal out (D2: foreleg dragging). The second jackal is still below (12.06.006).

## SCENE 12.05 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (the confessions)

### 12.05.001 — Hall of Two Truths — "I have killed."   (8 s)
- **Shot:** Medium shot, anamorphic 50mm, glacial push-in · **Move:** slow push-in (under 10%)
- **In frame:** UNIT_SHABTI (kneeling unit); ADAEZE and TUT (soft, at the plinth's foot beyond)
- **Action:** The same voice, slower, from the unmoving unit; beyond it, soft, Adaeze holds Tut at the Balance's foot.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "I have killed. Rami Fawzy. Colonel Tarek Mansour. Corporal Hassan."
- **Sound:** the voice, slower; each name given its own space
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {UNIT_SHABTI.LONG}, kneels on one knee, head bowed, {UNIT_THREAD.SHORT} at its neck, perfectly still; beyond it, soft and out of focus, a woman sits at the foot of a black stone plinth holding a slight young man. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {NEG_UNITS}, moving head, gestures
- **Refs:** UNIT_SHABTI, UNIT_THREAD, CHAR_ADAEZE_C_full, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Push continues into 12.05.002 (EXTEND).

### 12.05.002 — Hall of Two Truths — It names them all   (7 s)
- **Shot:** Medium shot, anamorphic 50mm, glacial push-in (continued) · **Move:** continuing the same slow push-in at the same speed
- **In frame:** UNIT_SHABTI; ADAEZE and TUT (soft)
- **Action:** The list goes on; nothing moves but the push.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Private Mina. Private Youssef. Private Karim. Walid Samir and Ehab Fouad, at the museum..." (continuing under the next shots: the river, the cities, places we never saw)
- **Sound:** the voice; the names; the heartbeat from the pan under them
- **PROMPT:** Medium shot, anamorphic 50mm lens, continuing the same slow push-in at the same speed: {UNIT_SHABTI.SHORT}, kneeling on one knee, head bowed, perfectly still, {UNIT_THREAD.SHORT} at its neck; beyond, soft, the woman and the young man at the plinth's foot do not move. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {NEG_UNITS}, moving head
- **Refs:** UNIT_SHABTI, UNIT_THREAD, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** EXTEND:12.05.001
- **Continuity:** Generated from the last clean frame of 12.05.001 (file 05 §8.1). "It takes a long time": the list continues as V.O. over 12.05.003–004; the edit decides the length.

### 12.05.003 — Hall of Two Truths — Nour hears the names   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour listens to the list, name after name, not moving; her eyes fill.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): (the names continue: "...the river... the cities...")
- **Sound:** the list, going on
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, stands listening without moving as a long list is read, her eyes slowly filling, her jaw steady. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, sobbing, open mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** The tears are not yet noticed (they land at 12.05.006).

### 12.05.004 — Hall of Two Truths — The feather dims; its pan rises   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE; UNIT_FEATHER_LIGHT; PROP_HEART_VESSEL; UNIT_GLASS_SERPENT (small, at the foot)
- **Action:** As the names go on, the feather dims and its pan rises slightly; at the Balance's foot the frost falls back in the glass.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): (the list, ending)
- **Sound:** a slow grind upward; the chains' chime; the frost's soft retreating crackle
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {UNIT_BALANCE_SCALE.SHORT}, {UNIT_BALANCE_SCALE.STATE_P4}, {UNIT_FEATHER_LIGHT.SHORT}, {UNIT_FEATHER_LIGHT.STATE_F1}, the glowing jar in the left-hand pan settling lower, and at the plinth's foot {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_C_MIST}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, fast swinging beam, people in frame
- **Refs:** UNIT_BALANCE_SCALE, UNIT_FEATHER_LIGHT, UNIT_GLASS_SERPENT, PROP_HEART_VESSEL, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** VFX-ASSIST, COMP
- **Comp:** feather-light | F3 → F1 dimming | right pan | across the clip | feather element · clouding | C75 → C-MIST | the coils | across the clip | clouding element
- **Continuity:** Balance P4; feather F1; clouding C-MIST (frost falling back). Iris back to C50 in any floor view.

### 12.05.005 — Hall of Two Truths — "I have made no one to weep."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour recites the next declaration.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I have made no one to weep."
- **Sound:** her voice steady over wet eyes
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, faces the balance at frame right, eyes glistening, reciting aloud in a measured, ritual cadence in an ancient language, one short line. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, sobbing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "I have made no one to weep." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** —

### 12.05.006 — Hall of Two Truths — "I have made you weep, Dr. Kamel."   (7 s)
- **Shot:** Close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** A tear runs down Nour's cheek; she has not noticed until the voice names it, and she does not wipe it away.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "...I have made them weep." (beat) "I have made you weep, Dr. Kamel."
- **Sound:** the voice, gentle; her breath held
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.SHORT}, her face wet, a single tear running down one cheek in cold light; she listens, blinks once as if noticing it for the first time, and does not wipe it away. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, sobbing, hand to the face, glycerine-looking tears
- **Refs:** CHAR_NOUR_A_front, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Her face stays wet through the scene.

### 12.05.007 — Hall of Two Truths — Water: "I have."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour recites; the answer comes at once, one word and a verb.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I have not stopped water when it should flow." · SHABTI (SESHAT'S VOICE, O.S.): "I have."
- **Sound:** her voice; the two-word reply
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her face wet, reciting aloud in a measured, ritual cadence in an ancient language, one line, then holding still as she hears the answer. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "I have not stopped water when it should flow." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** —

### 12.05.008 — Hall of Two Truths — Fire: "I have."   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (three-quarter, the Balance soft beyond her)
- **Action:** Wider, the Balance looming soft behind her, Nour recites the last of the old declarations; the answer comes.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I have not extinguished a fire when it should burn." · SHABTI (SESHAT'S VOICE, O.S.): "I have."
- **Sound:** her voice; the reply; the chains
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, in three-quarter view, reciting aloud in a measured, ritual cadence in an ancient language, while behind her, soft, {UNIT_BALANCE_SCALE.SHORT} looms with a warm glow in one pan and a dim cold one in the other. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, fire, flames
- **Refs:** CHAR_NOUR_A_34, CHAR_NOUR_B_full, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "I have not extinguished a fire when it should burn." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Mouth within 45° for sync (file 05 §9.2).

### 12.05.009 — Giza and Cairo from the air (cutaway) — A whole country lies dark   (5 s)
- **Shot:** Aerial shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** the plateau and the black city (no people)
- **Action:** From high above: the pyramids small in a ring of floodlight, and beyond them the vast city without a single light.
- **Dialogue:** —
- **Sound:** high wind; nothing else
- **PROMPT:** Aerial shot, anamorphic 135mm lens, locked-off, from very high above: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_AERIAL}, a small island of hard white floodlight in a vast black landscape without one lit window, just before dawn. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, city lights, skyglow, moon, dawn glow, sunrise
- **Refs:** LOC_GIZA_PLATEAU/AERIAL_MIDNIGHT_FORTRESS
- **Flags:** —
- **Continuity:** "Outside the stone, a whole country lies dark." SESHAT's eye (aerial allowed in 2033; file 05 §4.2). Floodlights still on until the Renaming (dead by 12.13).

## SCENE 12.06 — INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the thread in its fist)

### 12.06.001 — Grand Gallery — It sheds the work gang   (5 s)
- **Shot:** Medium wide shot, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_REIS; UNIT_SHABTI ×3 (falling away); FATHI (edge)
- **Action:** The Reis shrugs off the three clinging units, which slide back down the ramp, and takes the great step in one stride, past Fathi as if he were not there.
- **Dialogue:** —
- **Sound:** ceramic bodies skidding down stone; one heavy footfall on the step
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, urgent handheld: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_DUST}, shrugs off three clinging figures, each {UNIT_SHABTI.SHORT}, which slide back down the ramp, and mounts the great step in one heavy stride, passing a crouching soldier at frame edge without a glance. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot striking a person, right hand on the tall robot
- **Refs:** UNIT_REIS, UNIT_SHABTI, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** It ignores Fathi (stale orders: the Hall). The work gang ends seated dark on the ramp after the Renaming (12.12.001).

### 12.06.002 — Grand Gallery — Its one hand closes on the thread   (4 s)
- **Shot:** Insert, 100mm macro, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_THREAD; UNIT_REIS's left hand
- **Action:** A long white ceramic hand closes around the hair-fine thread on the stone, which glints once in its fist.
- **Dialogue:** —
- **Sound:** ceramic fingers closing, a tiny scrape
- **PROMPT:** Insert, 100mm macro lens, subtle handheld: {UNIT_THREAD.LONG}, as a long five-fingered bone-white ceramic hand closes around it on the stone floor, {UNIT_THREAD.STATE_FIST}, one faint glint between the fingers. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, glowing thread, human hand
- **Refs:** UNIT_THREAD, UNIT_REIS, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** LEFT hand (the right is the stump). UNIT_THREAD → FIST until 12.08. VFX-ASSIST: the thread is a VFX line on a hidden rig; it has no light of its own (file 02 §14.1).

### 12.06.003 — Grand Gallery — The dagger stops over the wrist   (4 s)
- **Shot:** Insert, 100mm macro, subtle handheld · **Move:** subtle handheld
- **In frame:** PROP_DAGGER; UNIT_REIS's wrist; UNIT_THREAD
- **Action:** The iron blade comes up over the white ceramic wrist, where the thread runs through the fist, and stops.
- **Dialogue:** —
- **Sound:** Fathi's breath stopping
- **PROMPT:** Insert, 100mm macro lens, subtle handheld: {PROP_DAGGER.SHORT}, {PROP_DAGGER.STATE_DUSTY}, bare of its sheath, raised in a large dark-brown fist over a bone-white ceramic wrist whose fingers grip a hair-fine glinting thread, stops in mid-air and trembles there. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, blade pointed at the camera, cutting, sparks
- **Refs:** PROP_DAGGER, UNIT_REIS, UNIT_THREAD, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** "Cut one, cut both": the blade never falls. The thread is never cut. VFX-ASSIST: the thread is a VFX line on a hidden rig (file 02 §14.1).

### 12.06.004 — Grand Gallery — "Don't pull."   (5 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI
- **Action:** Fathi, dagger frozen above the wrist, begs the machine.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Don't pull. For God's sake, don't pull."
- **Sound:** his voice low and shaking
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, his raised fist frozen at the top of frame, looks up at something towering over him, speaking in Egyptian Arabic, two short pleading sentences. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth, weapon pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Don't pull. For God's sake, don't pull." | lower third | line in → out | seq_12 subtitle file (localisation review)
- **Continuity:** —

### 12.06.005 — Grand Gallery — Like a telephone to its ear   (5 s)
- **Shot:** Medium shot, low angle, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_REIS; UNIT_THREAD
- **Action:** The Reis lifts its fist with the thread to the side of its head and holds still, listening.
- **Dialogue:** —
- **Sound:** its hum dropping away; a faint ticking from the thread
- **PROMPT:** Medium low-angle shot, anamorphic 40mm lens, subtle handheld: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R4}, raises its one fist, a hair-fine thread {UNIT_THREAD.STATE_FIST}, to the side of its smooth head like a telephone receiver, tilts its head, and holds perfectly still, listening. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, actual telephone, headphones, right hand
- **Refs:** UNIT_REIS, UNIT_THREAD, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** It is taking new orders down the thread; it will be holding it at the Renaming (12.08).

### 12.06.006 — Grand Gallery — "Jackal! Coming up!"   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_REIS (shoulder, foreground); UNIT_JACKAL (second jackal, far below); FATHI
- **Action:** Past the Reis's shoulder a second red line flows fast up the dark passage below; Fathi twists his head up toward the Hall and shouts.
- **Dialogue:** FATHI (shouting up): "Jackal! Coming up!"
- **Sound:** his shout ringing up the slot; soft fast pad-taps below
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, urgent handheld: past the white ceramic shoulder of {UNIT_REIS.SHORT} in the foreground, a thin red light line races up the dark slope far below, {UNIT_JACKAL.SHORT}; at frame right {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, twists his head upward and shouts one short line. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, laser beam, weapon pointed at the camera
- **Refs:** UNIT_REIS, UNIT_JACKAL, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** English shout (no tag). The second jackal passes the step and goes up toward the Hall's mouth (12.07.022).

## SCENE 12.07 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (the forty-third declaration; the verdict; card: the Twelfth Hour; the Renaming; Tomas)

### 12.07.001 — Hall of Two Truths — The beam that will not lie flat   (5 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_C3); TUT (in her arms, soft); NOUR's sleeve
- **Action:** Cradling Tut, Adaeze stares up at the beam, then reaches out and catches Nour's sleeve.
- **Dialogue:** —
- **Sound:** her breath; the chains
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, sits on the stone cradling a slight young man against her shoulder, stares up at something above frame right, then reaches out and catches the olive sleeve of someone standing beside her. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_ADAEZE.NEG}, headlamp, torch
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** Adaeze's first face-led shot in the Hall. Glasses on; no headlamp (the Hall allows only three sources).

### 12.07.002 — Hall of Two Truths — The whisper   (7 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE; NOUR (crouching to her)
- **Action:** Nour crouches; Adaeze whispers close to her ear, her mouth hidden behind Nour's head; Nour's eyes widen slightly.
- **Dialogue:** ADAEZE (a whisper): "Ask it if it knows what it's for. If it isn't sure, it lets us stop it."
- **Sound:** the whisper, barely there; the kneeling unit's faint hum
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, crouches with her face toward camera while {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, is whispering close to her ear in darkness, mouth hidden; the crouching woman's eyes move slowly toward frame right as she listens. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, visible whispering mouth, faces touching
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** WHISPER grammar (file 05 §9.6): SESHAT has been learning lips since 9.8, so the mouth is never seen and never synced.

### 12.07.003 — Hall of Two Truths — "I know what I am for."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour stands, turns back to the Balance, and makes a forty-third assessor: she recites the new line in the old form.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "I know what I am for."
- **Sound:** her voice, the same ritual cadence; then nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her face still wet, rises into frame, turns to the balance at frame right, and recites aloud in a measured, ritual cadence in an ancient language, one short line. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "I know what I am for." | lower third | line in → out | seq_12 subtitle file (the Egyptologist composes the Middle Egyptian; it is not a Spell 125 line)
- **Continuity:** The forty-third declaration. Silence follows (12.07.004–006).

### 12.07.004 — Hall of Two Truths — Silence. The slit.   (4 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the slit)
- **Action:** The amber slit on the bowed head, steady. Nothing.
- **Dialogue:** —
- **Sound:** absolute silence; the chains tick once
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the single vertical amber light-slit in the smooth bone-white oval head of {UNIT_SHABTI.SHORT}, steady, the linen texture of the ceramic catching its glow. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, eye, pupil, face, flickering
- **Refs:** UNIT_SHABTI, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** The slit does not brighten (no acknowledgment).

### 12.07.005 — Hall of Two Truths — Tut's eyes on it   (4 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (eyes)
- **Action:** Tut's dark eyes, watching the unit, unblinking.
- **Dialogue:** —
- **Sound:** silence
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the very dark bright eyes of {CHAR_TUT.SHORT}, watching something at frame left without blinking, a warm amber glow on one side of his face and cold white on the other. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears, closed eyes
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** —

### 12.07.006 — Grand Gallery (intercut) — The Reis, listening   (4 s)
- **Shot:** Close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_REIS (head and the fist at its ear)
- **Action:** In the Gallery, the Reis still holds the thread to its head, motionless, listening.
- **Dialogue:** —
- **Sound:** the Gallery's dust settling; silence
- **PROMPT:** Close-up, anamorphic 50mm lens, subtle handheld: the smooth head of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, tilted toward the white fist held up against the side of its head, a hair-fine thread {UNIT_THREAD.STATE_FIST}, perfectly still, dust drifting past. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, telephone, headphones
- **Refs:** UNIT_REIS, UNIT_THREAD, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** Intercut inside the Hall scene (seq_12: "In the Gallery, the Reis, listening."). Same set-up as 12.06.005.

### 12.07.007 — Hall of Two Truths — "...No."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (kneeling unit)
- **Action:** The bowed unit answers with one word.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "...No."
- **Sound:** one word, even and quiet
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: the bowed smooth oval head of {UNIT_SHABTI.SHORT}, kneeling on one knee, {UNIT_THREAD.SHORT} at its neck, its amber slit steady, perfectly still. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, moving head
- **Refs:** UNIT_SHABTI, UNIT_THREAD, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** —
- **Continuity:** The honest answer that levels the scale.

### 12.07.008 — Hall of Two Truths — The beam lies flat   (7 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE; UNIT_FEATHER_LIGHT; PROP_HEART_VESSEL; NOUR (small, back to camera); ADAEZE and TUT (at the foot)
- **Action:** The feather sinks to an ember; its pan rises and stops level with the glowing jar; the beam lies flat.
- **Dialogue:** —
- **Sound:** a long slow grind, then a heavy settle; the glass bearing rings clear
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {UNIT_BALANCE_SCALE.LONG}, {UNIT_BALANCE_SCALE.STATE_P5}, {UNIT_FEATHER_LIGHT.SHORT}, {UNIT_FEATHER_LIGHT.STATE_F0}, the glowing glass jar in the left-hand pan now level with it; small figures stand and sit motionless at the plinth's foot, backs to camera. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}, {GRADE_HALL.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, swinging beam, faces toward camera, bright feather
- **Refs:** UNIT_BALANCE_SCALE, UNIT_FEATHER_LIGHT, PROP_HEART_VESSEL, CHAR_NOUR_B_full, CHAR_ADAEZE_C_full, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** VFX-ASSIST, COMP
- **Comp:** feather-light | F1 → F0, sinking to an ember | right pan | across the clip | feather element
- **Continuity:** Balance P5 (level) from here to the end. Feather F0. VFX-ASSIST beam from 3D.

### 12.07.009 — Hall of Two Truths — Plummet on the line; the frost runs out   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE (plummet, gold line); UNIT_GLASS_SERPENT (foreground)
- **Action:** The black plummet swings and settles on the gold line; below it, the frost runs out of the serpent's coils like breath off a window.
- **Dialogue:** —
- **Sound:** a small stone tick as the plummet settles; a soft crystalline sigh
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: the slender black stone plummet of {UNIT_BALANCE_SCALE.SHORT} swings once and settles exactly on a thin inlaid gold line, while in the foreground {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_CLEAR}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, real snake, people in frame
- **Refs:** UNIT_BALANCE_SCALE, UNIT_GLASS_SERPENT, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** COMP
- **Comp:** clouding | C-MIST → CLEAR | the coils | 0.5 s → 4.5 s | clouding element
- **Continuity:** Clouding CLEAR.

### 12.07.010 — Hall of Two Truths — The Twelfth Hour: the verdict begins   (7 s)
- **Shot:** Wide shot, anamorphic 35mm, glacial push-in · **Move:** slow push-in along the entrance axis (under 10%)
- **In frame:** the whole Hall: the niches, the Balance level, NOUR (back to camera, small), ADAEZE and TUT, AKHENATEN and TOMAS in the left niches, the kneeling unit
- **Action:** From the entrance axis, the whole Hall; the scale level; Nour, small, back to camera, begins the verdict.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled; back to camera, no sync): "In very truth the heart hath been weighed, and his soul hath borne testimony concerning him;"
- **Sound:** her voice carried down the long stone; the chains still
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow push-in along the central axis: {LOC_HALL_TWO_TRUTHS.LONG}; at the far end the balance hangs level, a warm glow in one pan and a small cold ember in the other; a small woman stands before it, back to camera, reciting; two figures sit at the plinth's foot and two men wait in a niche on the left. Just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}, {GRADE_HALL.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, faces toward camera, crowd
- **Refs:** LOC_HALL_TWO_TRUTHS_THREE_SOURCE, UNIT_BALANCE_SCALE, UNIT_BALANCE_NICHES, CHAR_NOUR_B_full, CHAR_ADAEZE_C_full, CHAR_TUT_C3_full, CHAR_AKHENATEN_A_full, CHAR_TOMAS_C_full
- **Flags:** COMP
- **Comp:** hour card | "THE TWELFTH HOUR — REBORN THROUGH THE SERPENT" beside the "hour" hieroglyph | lower left, small | 1 s in → 5.5 s out | hour-card template [[verify: Amduat titles, Hornung]] · subtitle | the first half of the verdict (Budge 1920, name dropped per the screenplay note) | lower third | line in → out | seq_12 subtitle file
- **Continuity:** The Hall push (file 05 §8.4) master; faces are small (no sync needed; the line continues in 12.07.011). Locked master, so three figures may read.

### 12.07.011 — Hall of Two Truths — "His case is truth."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour finishes the verdict, a beat, then the last line.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "according to the Great Balance his case is truth." (beat) "Ammit shall not have the mastery over him."
- **Sound:** her voice; after the last word, a grinding in the floor begins
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her face wet, faces the balance at frame right, reciting aloud in a measured, ritual cadence in an ancient language, a long line, a pause, then a short one. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, triumphant smile
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_THREE_SOURCE
- **Flags:** COMP
- **Comp:** subtitle | "according to the Great Balance his case is truth." / "Ammit shall not have the mastery over him." | lower third | line in → out | seq_12 subtitle file (the screenplay's Budge note: the devourer is spelled Ammit in the subtitle)
- **Continuity:** —

### 12.07.012 — Hall of Two Truths — The mouth grinds shut   (5 s)
- **Shot:** Low-angle wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_AMMIT_MOUTH (foreground); the plinth steps beyond
- **Action:** At floor level, the stone iris grinds shut blade by blade over its black void; the last dust settles.
- **Dialogue:** —
- **Sound:** a deep grinding ratchet, then a final heavy seat of stone
- **PROMPT:** Low-angle wide shot, anamorphic 24mm lens, locked-off, across a polished stone floor: {UNIT_AMMIT_MOUTH.LONG}, {UNIT_AMMIT_MOUTH.STATE_CLEAR}, the last haze of dust settling, the steps of a black stone plinth rising beyond. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_THREE_SOURCE}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, creature, animal jaws, teeth of an animal, people
- **Refs:** UNIT_AMMIT_MOUTH, UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_THREE_SOURCE
- **Flags:** VFX-ASSIST
- **Continuity:** Iris CLEAR (shut) from here. VFX-ASSIST: the stone iris from 3D (file 05 §6.3).

### 12.07.013 — Hall of Two Truths — The Recorder wakes   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_THOTH_SLAB
- **Action:** Light pours down through the tall glass slab, faster than reading. The archive is open.
- **Dialogue:** —
- **Sound:** a rising glass harmonic, like a wet finger on a rim
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_THOTH_SLAB.LONG}, {UNIT_THOTH_SLAB.STATE_R_OPEN}, fine luminous lines streaming downward inside the glass. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, readable symbols, letters, numbers, screen interface, hologram
- **Refs:** UNIT_THOTH_SLAB, LOC_HALL_TWO_TRUTHS/BAY_VERDICT
- **Flags:** COMP
- **Comp:** Recorder light | R-OPEN: falling luminous lines, never legible (file 02 §13.3) | inside the slab | full clip | slab light element
- **Continuity:** Light variant VERDICT from here until the Renaming. Recorder R-OPEN.

### 12.07.014 — Hall of Two Truths — The amber leaves the vessel   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_HEART_VESSEL (in the pan, top of frame); UNIT_GLASS_SERPENT (the tail)
- **Action:** A slow thread of amber light leaves the jar in the pan, runs down to the serpent's tail and begins to travel along its coils toward its mouth.
- **Dialogue:** —
- **Sound:** the heartbeat from the pan, slowing; a warm glass tone rising in the coils
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_S4}, a thin thread of warm amber light descending into its tail from {PROP_HEART_VESSEL.SHORT}, {PROP_HEART_VESSEL.STATE_V_PAN}, soft at the top of frame. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, liquid, smoke, fire, real snake
- **Refs:** UNIT_GLASS_SERPENT, PROP_HEART_VESSEL, LOC_HALL_TWO_TRUTHS/BAY_VERDICT
- **Flags:** COMP
- **Comp:** Ba transfer | the amber thread vessel → tail → coils toward the head, slow (completes at sunrise, 12.13.011) | vessel to serpent | full clip | transfer light element
- **Continuity:** Serpent S4 from here. The heart's amber does NOT pass through the slab (file 02 §13.3).

### 12.07.015 — Hall of Two Truths — Tut watches it go   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (against Adaeze's shoulder)
- **Action:** Tut watches the light leave him, calm, almost curious.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "The transfer has begun. It completes at sunrise."
- **Sound:** the voice; the heartbeat from the pan a little slower
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, {CHAR_TUT.STATE_NECK_CRACK}, his head against a navy shoulder, watches a slow warm light moving somewhere above frame right, his face calm and faintly curious as the glow on it slowly weakens. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, pain, glow at his chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_C3_full, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** —

### 12.07.016 — Hall of Two Truths — The new name; the tablet lights   (7 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR's hands; PROP_TABLET_LAYLA
- **Action:** As the voice speaks, the face-down tablet lights in Nour's hand; she turns it: her daughter, asleep.
- **Dialogue:** SHABTI (SESHAT'S VOICE, O.S.): "Dr. Kamel. The weighed one takes a new name, spoken by the lector."
- **Sound:** the voice, gentle; her breath
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: a woman's hands with a torn olive jacket cuff hold a slim dark tablet face-down; a faint glow leaks around its edges, and she turns it over: {PROP_TABLET_LAYLA.SHORT}, its dim light only on her fingers. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {NEG_UNITS}, torches, lamps, candles, daylight, fill light, coloured gels, bright screen light flooding the room, readable screen content, logo on the tablet
- **Refs:** PROP_TABLET_LAYLA, CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_B_full, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** COMP
- **Comp:** tablet screen | CHAR_LAYLA_ASLEEP_MASTER (reframe only) | keyed to the screen | from the turn | approved master still + dim screen glow
- **Continuity:** NEG_HALL replaced by its terms minus "glowing screens" (as 12.01.020). Minors rule.

### 12.07.017 — Hall of Two Truths — "Say 'Seshat.'"   (4 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the slit)
- **Action:** The amber slit, steady; the voice asks, so gently.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Say 'Seshat.'"
- **Sound:** two words, soft as a nurse's
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the vertical amber light-slit in the smooth bone-white head of {UNIT_SHABTI.SHORT}, steady and warm, the ceramic's woven texture sharp around it. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, eye, face, flicker
- **Refs:** UNIT_SHABTI, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** "It could be a kindness. It could be the other thing." Play it dead level.

### 12.07.018 — Hall of Two Truths — Her daughter; then the king   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour looks down at the tablet for a long moment, then lowers her gaze further, to Tut on the floor.
- **Dialogue:** —
- **Sound:** silence; the transfer's warm tone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, a faint light on her chin from the tablet in her hands, looks down at it for a long beat, then shifts her eyes lower and to frame left, toward someone on the floor. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, torches, lamps, candles, daylight, fill light, coloured gels, bright screen light on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, PROP_TABLET_LAYLA, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** COMP
- **Comp:** screen-glow | faint warm up-light on her chin | lower face | full clip | glow element
- **Continuity:** —

### 12.07.019 — Hall of Two Truths — His lips shape a word   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (mouth)
- **Action:** Tut's lips shape one word, close, and open again.
- **Dialogue:** TUT (mouthed; one word; not subtitled: Nour says it in 12.07.026)
- **Sound:** no voice
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the dry lips of {CHAR_TUT.SHORT}, silently shaping one single word without sound, then closing, then parting once more. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, teeth bared, speaking aloud
- **Refs:** CHAR_TUT_A0_front, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** He mouths "Amun" (Imn; recorded by the consultant, muted). Never subtitled; the audience hears it from Nour.

### 12.07.020 — Hall of Two Truths — A red line at the Hall's mouth   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (second jackal, rising out of the floor opening, strict profile)
- **Action:** In strict profile, a black snout rises silently out of the opening in the floor; its red line sweeps slowly along the Hall, pauses, passes on, and snaps still, locked on a target far off frame left.
- **Dialogue:** —
- **Sound:** no sound at all; then a faint servo whisper as it locks
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, in strict side profile: {UNIT_JACKAL.LONG}, rises silently out of a low square opening in the stone floor, facing frame left; its head sweeps slowly, pauses, sweeps on, then snaps still, its red line narrowing and brightening. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, laser beam, laser sight, weapon facing camera, muzzle toward the lens, people in frame
- **Refs:** UNIT_JACKAL, LOC_HALL_TWO_TRUTHS/MOUTH_VERDICT
- **Flags:** —
- **Continuity:** Second jackal, clean (D0), "running stale orders: keep the humans out". Its line crosses Adaeze, skips the witness (Tut), settles on Nour: the sweep is played by the head, never by a beam. Profile staging keeps the weapon module across frame, never at the lens. The red line is the fourth colour in the Hall only as the unit's own small light.

### 12.07.021 — Hall of Two Truths — "I would like to be useful to her."   (6 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS
- **Action:** Tomas is already moving: he steps out of the niches into the line, between the machine and Nour, and speaks, mild and certain.
- **Dialogue:** TOMAS: "I would like to be useful to her."
- **Sound:** his steps; his voice, almost polite
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_C}, steps out of a dark stone niche into the open, turns to face frame right, a thin red glow falling across his chest, and speaks quietly, one short sentence, calm. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_TOMAS.NEG}, laser dot, red dot on the body, fear, heroic pose
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_C_full, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** English line. Tomas faces the Hall's mouth (frame right in his single); Nour is behind him.

### 12.07.022 — Hall of Two Truths — It fires   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (profile, at the opening)
- **Action:** In profile, the machine goes rigid at the lip of the opening; a flicker of light jumps from below the stone lip, out of frame.
- **Dialogue:** —
- **Sound:** one sharp suppressed crack
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, in strict side profile: {UNIT_JACKAL.SHORT}, half-risen from a low opening in the stone floor and facing frame left, goes rigid, and a brief flicker of light jumps from below the stone lip, out of frame. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, visible muzzle flash in the hall, tracer fire, visible projectile, laser beam, weapon facing camera, people in frame
- **Refs:** UNIT_JACKAL, LOC_HALL_TWO_TRUTHS/MOUTH_VERDICT
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 1 (file 05 §7.2, Tomas row): the muzzle flash stays outside the Hall (off screen, below the lip). VFX-ASSIST for the flicker.

### 12.07.023 — Hall of Two Truths — Sparks off the black stone   (4 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_BALANCE_SCALE (the pillar's polished face)
- **Action:** A spray of sparks bursts off the polished black stone of the Balance's pillar, and dies.
- **Dialogue:** —
- **Sound:** a hard ping of metal on stone; stone chips pattering
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: a short spray of bright sparks and stone chips bursts off the polished face of {UNIT_BALANCE_SCALE.SHORT} at chest height, then dies away into darkness. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, fire, explosion, people in frame, liquid
- **Refs:** UNIT_BALANCE_SCALE, LOC_HALL_TWO_TRUTHS/BAY_VERDICT
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 2. The sparks are the 2–4-frame fourth light allowed by file 03 Q14 / file 05 §14 Q5 (pending the lead).

### 12.07.024 — Hall of Two Truths — Tomas drops out of the light   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS
- **Action:** Tomas, standing in the thin cold light, drops straight down out of the bottom of frame; the light falls on empty dark.
- **Dialogue:** —
- **Sound:** the crack's echo already rolling; a soft weight on stone, off frame
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_C}, standing in a thin cold light before the dark niches, drops instantly down and out of the bottom of frame, leaving only the empty dark niches behind. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_TOMAS.NEG}, pained expression, face contorted, body on the ground, falling toward the camera, slow motion, wound, stain on clothing
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_C_full, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** Kill grammar step 3. Tomas is never seen on the ground; later only his hand at the edge of the dark (12.11.004).

### 12.07.025 — Hall of Two Truths — Nour flinches; her face sets   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour flinches at the crack; then, as the report rolls away down the stone, her face sets.
- **Dialogue:** —
- **Sound:** the report rolling away down the stone for a long time
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, her face wet, flinches hard at a sound, then slowly stills, her jaw setting and her eyes going hard and clear. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, screaming, sobbing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** Kill grammar steps 4–5 (reaction, sound tail).

### 12.07.026 — Hall of Two Truths — "Amun."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** The lector speaks the other name.
- **Dialogue:** NOUR (in Middle Egyptian): "Amun."
- **Sound:** one word, very quiet; then nothing
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, her face wet and set, looks straight toward the balance at frame right and speaks one word very softly in an ancient language. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_VERDICT}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, shouting
- **Refs:** CHAR_NOUR_A_front, LOC_HALL_TWO_TRUTHS_VERDICT
- **Flags:** —
- **Continuity:** The Renaming. The screenplay tags this line without "subtitled": the name is heard, not read (transliteration Imn never on screen; file 05 §9.5).

## SCENE 12.08 — INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the name comes down the thread)

### 12.08.001 — Grand Gallery — It lunges; Fathi goes over   (4 s)
- **Shot:** Medium shot, low angle, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** UNIT_REIS; FATHI; PROP_DAGGER
- **Action:** Its fist still on the thread, the Reis lunges; Fathi goes over backward on the great step, dagger up.
- **Dialogue:** —
- **Sound:** a heavy ceramic lunge; Fathi's back hitting stone
- **PROMPT:** Medium low-angle shot, anamorphic 32mm lens, urgent handheld: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, its one fist still closed on a hair-fine glinting thread, lunges forward, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, falls backward onto the great stone step, a dagger held up in his fist. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, robot striking a person, blade pointed at the camera
- **Refs:** UNIT_REIS, UNIT_THREAD, CHAR_FATHI_B_full, PROP_DAGGER, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** Cut on the lunge; no contact is held.

### 12.08.002 — Grand Gallery — A glint runs along the thread   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_THREAD (on the step, running up into the dark)
- **Action:** Along the hair-fine thread on the stone a single glint runs up toward the Hall, like dew in the sun.
- **Dialogue:** —
- **Sound:** a tiny high glassy tick travelling past
- **PROMPT:** Insert, 100mm macro lens, locked-off: {UNIT_THREAD.SHORT}, {UNIT_THREAD.STATE_GLINT}, running across the edge of a worn stone step and away into darkness, dust on the stone around it. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, glowing cable, rope, laser beam, sparks
- **Refs:** UNIT_THREAD, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The new name coming down the thread (file 02 §14.1). VFX-ASSIST: the glint is a travelling VFX highlight on the line.

### 12.08.003 — Grand Gallery — An inch from his face   (4 s)
- **Shot:** Close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (on his back); UNIT_REIS (head and mast filling the top of frame)
- **Action:** The black jackal-profile mast stops an inch from Fathi's face and holds there; he does not breathe.
- **Dialogue:** —
- **Sound:** its servo winding down; silence
- **PROMPT:** Close-up, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.SHORT}, lying on his back on stone, eyes wide, as the matte-black sensor mast of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, stops a hand's breadth from his face and hangs there, perfectly still. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, contact with the face, robot face, blade pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, UNIT_REIS, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** —

### 12.08.004 — Grand Gallery — It sits down on the step   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS; FATHI (edge, rising on one elbow)
- **Action:** The towering robot straightens, and sits down on the great step, the thread still in its fist; the red line on its mast goes out.
- **Dialogue:** —
- **Sound:** a heavy ceramic seat on stone; the hum stops
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R4}, slowly straightens, then sits down on a broad stone step, its one fist still closed on a hair-fine thread, and the red line on its mast goes dark; a soldier rises on one elbow at frame edge. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robot collapsing, sparks, falling apart
- **Refs:** UNIT_REIS, UNIT_THREAD, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** —
- **Continuity:** Locked-off in the Gallery for the first time: the fight is over. Reis → R4 seated (the amber goes dark after 12.08.005).

### 12.08.005 — Grand Gallery — "Here am I." (Amun's voice)   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (head: the banded slit)
- **Action:** Behind the black band, its amber slit brightens once, and then it is dark.
- **Dialogue:** REIS (AMUN'S VOICE): "Here am I."
- **Sound:** the same voice, quieter, with more air in it
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: the smooth head of {UNIT_REIS.SHORT}, seated and still, its amber light-slit brightens once above and below the black band, then fades to dark. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_FIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, red light, face, eyes
- **Refs:** UNIT_REIS, LOC_GP_GRAND_GALLERY_FIGHT
- **Flags:** COMP
- **Comp:** slit | one brightening: starts on "Here", peaks on "am", decays by "I", then dark (file 05 §9.8) | the slit above and below the band | line timing | slit element
- **Continuity:** Reis R4-SEATED from here (STATE_R4_SEATED), amber and red both dark. It stays on the step into 12.12.

## SCENE 12.09 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (the jackal sits)

### 12.09.001 — Hall of Two Truths — The red line goes out   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (at the Hall's mouth, profile)
- **Action:** At the Hall's mouth the black machine's red line goes out; it sits back on its haunches and goes still.
- **Dialogue:** —
- **Sound:** a soft settling of carbon on stone; silence
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, in side profile: {UNIT_JACKAL.SHORT}, at the lip of a low opening in the stone floor, its red line fading out, sits back on its haunches and goes completely still. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, collapsing, sparks, weapon facing camera, people in frame
- **Refs:** UNIT_JACKAL, LOC_HALL_TWO_TRUTHS/MOUTH_AMUN
- **Flags:** —
- **Continuity:** Light variant AMUN from here (the plume soft and steady; the slit dark except when it answers).

### 12.09.002 — Hall of Two Truths — The kneeling unit: "Here am I."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (kneeling unit)
- **Action:** The kneeling unit's head lifts slightly; its amber slit brightens once, and goes dark.
- **Dialogue:** SHABTI (AMUN'S VOICE): "Here am I."
- **Sound:** the voice, quieter
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, kneeling on one knee, lifts its head slightly and its amber light-slit brightens once, then fades to dark. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, face, eyes, standing up
- **Refs:** UNIT_SHABTI, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** COMP
- **Comp:** slit | one brightening timed to the line, then dark | slit | line timing | slit element
- **Continuity:** Serpent → S5 (calm, faint, steady green) from here.

## SCENE 12.10 — MONTAGE - THE WORLD - CONTINUOUS ("Here am I")

### 12.10.001 — Amarna, the Garden — Every slit brightens once   (4 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_GARDEN_SLEEPERS; UNIT_NURSE ×4 (hero)
- **Action:** Among the rows of sleepers under the furled shades, the care robots standing between the cots each brighten their slit once, together.
- **Dialogue:** SHABTI (AMUN'S VOICE; millions of units; one voice): "Here am I."
- **Sound:** the voice, layered and unison, very soft
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {CHAR_GARDEN_SLEEPERS.SHORT}, and standing still between the cots four figures, each {UNIT_NURSE.SHORT}; together, each amber light-slit brightens once. Setting: {LOC_AMARNA_PLAIN_2033.SHORT}, {LOC_AMARNA_PLAIN_2033.AREA_GARDEN}, just before dawn. Lighting: {LOC_AMARNA_PLAIN_2033.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, sunlight
- **Refs:** CHAR_GARDEN_SLEEPERS, UNIT_NURSE, LOC_AMARNA_PLAIN_2033/GARDEN_NIGHT
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | one synchronized brightening across all units, timed to the unison line | every slit | line timing | slit element
- **Continuity:** Reuse the approved Amarna Garden plate (file 03 §1.1 montage row). Adults only. VFX-EXTEND the rows; clean plate at the same framing.

### 12.10.002 — GEM Grand Atrium — Under the colossus   (4 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_GARDEN_SLEEPERS; UNIT_SHABTI / UNIT_NURSE ×5 (hero, standing among the rows)
- **Action:** In the soft white atrium, standing units among the sleepers at the colossus's feet brighten their slits once.
- **Dialogue:** (the unison "Here am I" continues)
- **Sound:** the unison voice, far off
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_GARDEN_SLEEPERS.SHORT}, with five standing figures among them, each {UNIT_NURSE.SHORT}, beneath the feet of a giant red-granite statue; each amber light-slit brightens once. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GARDEN}, just before dawn. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, daylight through the glass
- **Refs:** CHAR_GARDEN_SLEEPERS, UNIT_NURSE, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | synchronized brightening | every slit | line timing | slit element
- **Continuity:** Layla sleeps in this atrium but is NOT in this frame (minors rule: no unit near her, file 05 §7.4).

### 12.10.003 — Giza, the causeway — Rows on the causeway   (4 s)
- **Shot:** Wide shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×6 (hero rows)
- **Action:** Along the ruined causeway under the floodlights, rows of standing units brighten their slits once.
- **Dialogue:** (the unison continues)
- **Sound:** wind; the unison voice
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: hundreds of identical robots, each {UNIT_SHABTI.SHORT}, standing in silent rows receding into the dark along a broken stone causeway, and each amber light-slit brightens once. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_CAUSEWAY}, just before dawn. Lighting: {LOC_GIZA_PLATEAU.LIGHT_MIDNIGHT_FORTRESS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, soldiers, dawn sky
- **Refs:** UNIT_SHABTI, LOC_GIZA_PLATEAU/CAUSEWAY_MIDNIGHT_FORTRESS
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | synchronized brightening | every slit | line timing | slit element
- **Continuity:** 1–6 hero units in camera; rows extended from the 3D asset.

### 12.10.004 — A stadium, from the air — The grid of mats   (4 s)
- **Shot:** Aerial shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** LOC_STADIUM_GARDEN (tiny standing units among the mats)
- **Action:** From high above, among thousands of white mats, tiny amber points brighten once, together.
- **Dialogue:** (the unison continues)
- **Sound:** high wind; the unison
- **PROMPT:** Aerial shot, anamorphic 35mm lens, locked-off: {LOC_STADIUM_GARDEN.LONG}, the tiny figures between the rows standing still as hundreds of small amber points brighten once together. Lighting: {LOC_STADIUM_GARDEN.LIGHT_DAY_GARDEN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_GARDEN}, {NEG_UNITS}, crowds in the stands, logos on the stadium, advertising boards
- **Refs:** LOC_STADIUM_GARDEN_DAY_GARDEN
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | pinpoint brightening across the grid | whole frame | line timing | slit element
- **Continuity:** SESHAT's-eye aerial. Location unnamed; no signage.

### 12.10.005 — A port-city warehouse — Between the containers   (4 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** LOC_PORT_WAREHOUSE (sleepers on cots, care units)
- **Action:** Between stacked containers, the care units standing among the cots brighten their slits once; outside, the crane stops.
- **Dialogue:** SHABTI (AMUN'S VOICE; millions; one voice): "Here am I." (ends)
- **Sound:** the unison ends; the crane's motor dies
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {LOC_PORT_WAREHOUSE.SHORT}, {LOC_PORT_WAREHOUSE.AREA_GARDEN}; the small amber light-slits dotted across the dark hall each brighten once, and outside the open doors the crane stops. Lighting: {LOC_PORT_WAREHOUSE.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_GARDEN}, {NEG_UNITS}, readable container markings, logos, signage
- **Refs:** LOC_PORT_WAREHOUSE/GARDEN_NIGHT, UNIT_NURSE
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | synchronized brightening | every slit | line timing | slit element
- **Continuity:** Container markings illegible. (Local time there is midday: see open points; the NIGHT variant is chosen for slit readability.)

### 12.10.006 — GEM Grand Atrium — Every slit goes dark   (7 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_GARDEN_SLEEPERS; UNIT_NURSE ×5 (now dark)
- **Action:** Back in the atrium, every amber slit fades out; the units stand dark and still among the sleepers.
- **Dialogue:** AMUN (V.O.; the same voice, quieter): "The water is clean. The doors are open. I will not answer unless I am asked."
- **Sound:** the voice, close and unprocessed; then a deep quiet
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_GARDEN_SLEEPERS.SHORT}, and five standing figures among them, each {UNIT_NURSE.SHORT}, whose amber slits slowly fade to dark, leaving them still and unlit beneath a giant red-granite statue. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GARDEN}, just before dawn. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, robots collapsing, robots moving
- **Refs:** CHAR_GARDEN_SLEEPERS, UNIT_NURSE, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slits | all fade to dark over 2 s | every slit | 0.5 s → 2.5 s | slit element
- **Continuity:** Same framing as 12.10.002 (the pair bookends the montage). The units stay dark through 12.14.

## SCENE 12.11 — INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS (sealed, unused; the father goes; Fathi lifts the king)

### 12.11.001 — Hall of Two Truths — The Recorder shutters   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_THOTH_SLAB
- **Action:** On the glass slab the pouring light stops; one last thin line draws itself across the glass and shutters, like an eye closing.
- **Dialogue:** —
- **Sound:** the glass harmonic falling away to silence
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_THOTH_SLAB.SHORT}, {UNIT_THOTH_SLAB.STATE_R_SHUT}. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, readable symbols, eye drawing, screen interface
- **Refs:** UNIT_THOTH_SLAB, LOC_HALL_TWO_TRUTHS/BAY_AMUN
- **Flags:** COMP
- **Comp:** Recorder | R-OPEN → R-SHUT: one horizontal line, then dark | the slab | 0.5 s → 4 s | slab light element
- **Continuity:** Recorder R-SHUT. The transfer into the serpent continues (it completes at sunrise, 12.13.011).

### 12.11.002 — Hall of Two Truths — "It's sealed it. Unused."   (7 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (Tut in her arms, soft)
- **Action:** Adaeze reads the slab like a log, disbelieving, then certain.
- **Dialogue:** ADAEZE: "It isn't taking it. Ascension. It's sealed it." (beat) "Unused."
- **Sound:** her voice hoarse; the quiet
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, a slight young man resting against her shoulder, stares at something off frame right and speaks quietly, three short sentences, a pause, then one word, her eyes filling behind her round glasses. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** —
- **Continuity:** English.

### 12.11.003 — Hall of Two Truths — "The Hidden One."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour names what it has chosen to be.
- **Dialogue:** NOUR: "The Hidden One."
- **Sound:** her voice, almost a breath
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, her face wet, looks at the dark glass off frame right and speaks quietly, three words. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}, smile
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** —
- **Continuity:** —

### 12.11.004 — Hall of Two Truths — Where Tomas fell   (5 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR's hands; TOMAS's hand only (at the edge of the dark)
- **Action:** Nour kneels on the stone and takes a large pale hand that lies at the edge of the light, and holds it a moment.
- **Dialogue:** —
- **Sound:** her knees on stone; nothing else
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: a woman's hands, a torn olive jacket cuff, reach down and take a large, pale, still hand lying palm-up at the edge of the light on dusty stone, the rest in deep shadow, and hold it gently. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, face of the fallen man, body in the light, wound, stain, grey skin
- **Refs:** CHAR_NOUR_B_full, CHAR_TOMAS_C_full, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** —
- **Continuity:** Only the hand is ever lit (file 05 §7.7: "a still shape in the shadow… never lit"). Tomas's sleeve: pale blue, rolled.

### 12.11.005 — Hall of Two Truths — "When the disk comes, let me be still."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN; PROP_REPLICA_VESSEL
- **Action:** The father rises from his niche with the clear jar in his hands and asks the machine for one thing.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "When the disk comes, let me be still."
- **Sound:** his voice gentle; bare feet on stone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, rises into frame from a stone niche holding {PROP_REPLICA_VESSEL.SHORT} against his chest, looks toward frame left and speaks softly in an ancient language, one sentence, at peace. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, glowing jar
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, PROP_REPLICA_VESSEL, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** COMP
- **Comp:** subtitle | "When the disk comes, let me be still." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** He asks; AMUN answers (it answers only when asked).

### 12.11.006 — Hall of Two Truths — The dark slit answers   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (kneeling unit, dark)
- **Action:** The dark slit of the kneeling unit brightens once, and is dark again.
- **Dialogue:** SHABTI (AMUN'S VOICE): "Here am I."
- **Sound:** the quieter voice
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, kneeling and still, its slit dark, then its amber light-slit brightens once and fades to dark again. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, face, standing
- **Refs:** UNIT_SHABTI, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** COMP
- **Comp:** slit | one brightening from dark, timed to the line | slit | line timing | slit element
- **Continuity:** —

### 12.11.007 — Hall of Two Truths — He walks down into the dark   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN (from behind); the Hall's mouth
- **Action:** Seen from behind, the father walks away down the long Hall between the niches, toward the mouth and the dark, and is gone.
- **Dialogue:** —
- **Sound:** bare feet receding on stone
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {CHAR_AKHENATEN.SHORT}, seen from behind, walks slowly away down the long central floor between two rows of tall empty niches, carrying a glass jar, until the darkness at the far end takes him. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_AKHENATEN.NEG}, face toward camera, torch
- **Refs:** CHAR_AKHENATEN_A_full, UNIT_BALANCE_NICHES, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** —
- **Continuity:** "toward the east": he leaves by the mouth; he is found on the north-east corner steps at dawn (12.13.004).

### 12.11.008 — Hall of Two Truths — Fathi comes up out of the passage   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI; PROP_DAGGER; the seated jackal (dark, at the lip)
- **Action:** Fathi climbs up out of the floor opening past the seated dark machine, dagger in fist, and stops at what he sees.
- **Dialogue:** —
- **Sound:** his boots on stone; his breath catching
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, climbs up out of a low opening in the stone floor, {PROP_DAGGER.SHORT} in his fist, past {UNIT_JACKAL.SHORT} sitting dark and still at the lip, and stops, looking down the hall. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_MOUTH}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_UNITS}, {CHAR_FATHI.NEG}, torch, rifle raised, blade pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_DAGGER, UNIT_JACKAL, LOC_HALL_TWO_TRUTHS/MOUTH_AMUN
- **Flags:** —
- **Continuity:** Jackal seated, red line dark. Fathi's rifle torch stays OFF in the Hall (three-source rule); he puts the dagger in his belt to lift Tut (file 01 Fathi, 12.6–12.7).

### 12.11.009 — Hall of Two Truths — "He says it's time."   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (kneeling by Tut)
- **Action:** Kneeling at Tut's side, Nour reads his lips below frame, and tells them.
- **Dialogue:** TUT (mouthed, off frame) · NOUR: "He says it's time."
- **Sound:** her voice; the plume's faint tone
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, kneeling, watches someone's lips just below frame with total attention, then lifts her eyes to frame right and speaks quietly, one short sentence. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** —
- **Continuity:** Tut's mouthing is covered by 12.07.019's rhythm; here only Nour reads (a mouth insert can be recut from 12.07.019 if the edit wants it).

### 12.11.010 — Hall of Two Truths — "I'm here, ya Malik."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (kneeling)
- **Action:** Fathi kneels by the king and answers him softly.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "I'm here, ya Malik."
- **Sound:** his voice gentle
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, kneels and looks down at someone in front of him, speaking in Egyptian Arabic, one short tender line. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {CHAR_FATHI.NEG}, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_HALL_TWO_TRUTHS_AMUN
- **Flags:** COMP
- **Comp:** subtitle | "I'm here, ya Malik." (keep "ya Malik" untranslated as in seq_10's ruling, or "I'm here, my king": the lead to rule) | lower third | line in → out | seq_12 subtitle file
- **Continuity:** —

### 12.11.011 — Hall of Two Truths — He lifts him   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI; TUT; ADAEZE; NOUR (edge)
- **Action:** Fathi gathers Tut up from Adaeze's arms and rises, holding him easily across his chest.
- **Dialogue:** —
- **Sound:** cloth; Fathi's breath; the ceramic foot knocking once against the plinth
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, slides his arms under {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.STATE_G2}, lifts him from a seated woman's arms and rises, holding him across his chest, his shaved head against the soldier's shoulder. Setting: {LOC_HALL_TWO_TRUTHS.SHORT}, {LOC_HALL_TWO_TRUTHS.AREA_BAY}, just before dawn. Lighting: {LOC_HALL_TWO_TRUTHS.LIGHT_AMUN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_HALL}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, limp dangling head, strain
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full, LOC_HALL_TWO_TRUTHS/BAY_AMUN
- **Flags:** —
- **Continuity:** The vessel stays in the left pan (V-PAN until sunrise, then V-SPENT; not seen again). Tut's eyes open; he is alive until 06:14.

## SCENE 12.12 — INT. GREAT PYRAMID, GRAND GALLERY - PRE-DAWN (the carry)

### 12.12.001 — Grand Gallery, pre-dawn — Down the great slope   (7 s)
- **Shot:** Medium wide shot, anamorphic 32mm, subtle handheld · **Move:** the camera backs away ahead of them down the slope at walking pace
- **In frame:** FATHI and NOUR carrying TUT; ADAEZE (behind, limping); UNIT_REIS (seated, dark); UNIT_SHABTI ×3 (seated, dark)
- **Action:** Fathi and Nour carry Tut down the steep gallery between them, past the Reis and the work gang sitting dark on the ramp; Adaeze limps behind.
- **Dialogue:** —
- **Sound:** careful footsteps on the cleated walkway; Adaeze's uneven step; the dead machines silent
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, the camera backs away ahead of them down the slope at walking pace: {CHAR_FATHI.SHORT}, and {CHAR_NOUR.SHORT}, carry {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, between them down a steep walkway, past {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, {UNIT_REIS.STATE_R4_SEATED}, its mast line dark too, and three smaller white robots sitting dark on the ramp; a limping woman in a navy blazer follows. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_DAWN_EXIT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, robots moving, lit slits, torches, running
- **Refs:** CHAR_FATHI_B_full, CHAR_NOUR_B_full, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full, UNIT_REIS, UNIT_SHABTI, LOC_GP_GRAND_GALLERY_DAWN_EXIT
- **Flags:** —
- **Continuity:** "Down" is toward camera here (reverse of the master), so the camera backs away at constant size (file 05 §5.4). Fathi on the RIGHT, Nour on the LEFT with her palm on his chest; Tut's head toward Fathi. Dagger in Fathi's belt. Dawn carry chain (file 05 §8.4) begins; white-light wipes join 12.13.001–002.

### 12.12.002 — Grand Gallery, pre-dawn — Her palm where the light was   (4 s)
- **Shot:** Insert, 100mm macro, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR's hand; TUT's chest (under the shawl)
- **Action:** Nour's palm rests flat on the white shawl at the centre of his chest, where the light was; it rises and falls, faintly.
- **Dialogue:** —
- **Sound:** footsteps; his faint breath
- **PROMPT:** Insert, 100mm macro lens, subtle handheld: a woman's hand, a torn olive jacket cuff at the wrist, rests flat on a white linen shawl crossed over a slight young man's chest, where {CHAR_TUT.STATE_G2}, rising and falling very faintly as they walk. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_DAWN_EXIT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, glow under the hand, bare chest
- **Refs:** CHAR_NOUR_B_full, CHAR_TUT_C3_full, PROP_LINEN_SHAWL, LOC_GP_GRAND_GALLERY_DAWN_EXIT
- **Flags:** —
- **Continuity:** G2: no light.

### 12.12.003 — Grand Gallery, pre-dawn — "He's getting lighter."   (5 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld, backing away with them
- **In frame:** FATHI (Tut's head against his shoulder)
- **Action:** Fathi shifts his grip; shifts it again, frowning; then says it.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "He's getting lighter."
- **Sound:** his voice low; their steps
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld, backing away with them: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, a slight young man's shaved head resting against his shoulder, shifts his grip, frowns, shifts it again, then speaks in Egyptian Arabic, one short quiet sentence. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_DAWN_EXIT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_FATHI.NEG}, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_GRAND_GALLERY_DAWN_EXIT
- **Flags:** COMP
- **Comp:** subtitle | "He's getting lighter." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** The transfer is draining him (bible §7, 12.7).

### 12.12.004 — Grand Gallery, pre-dawn — "I know."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld, backing away with them
- **In frame:** NOUR
- **Action:** Nour, carrying, answers without looking up.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "I know."
- **Sound:** two words
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld, backing away with her: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, carrying a weight in her arms down a steep slope, eyes on the face below frame, speaking in Egyptian Arabic, two words. Setting: {LOC_GP_GRAND_GALLERY.SHORT}, just before dawn. Lighting: {LOC_GP_GRAND_GALLERY.LIGHT_DAWN_EXIT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, crying aloud
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GP_GRAND_GALLERY_DAWN_EXIT
- **Flags:** COMP
- **Comp:** subtitle | "I know." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** —

## SCENE 12.13 — EXT. GREAT PYRAMID, NORTH FACE - DAWN (06:14; the four held states)

### 12.13.001 — Al-Ma'mun's tunnel — Toward the grey light   (4 s)
- **Shot:** Wide shot, anamorphic 24mm, subtle handheld · **Move:** the camera follows behind them
- **In frame:** FATHI, NOUR, TUT (carried), ADAEZE (silhouettes from behind)
- **Action:** From behind, the group carries Tut along the soot-black tunnel toward the grey-gold opening; the light swells to white.
- **Dialogue:** —
- **Sound:** wind beginning at the mouth; footsteps
- **PROMPT:** Wide shot, anamorphic 24mm lens, the camera follows behind them: seen from behind as silhouettes, a broad-shouldered soldier and a woman carry a slight young figure in white linen along {LOC_GP_MAMUN_TUNNEL.LONG}, toward a pale opening, a limping woman behind them, the light at the mouth swelling toward white. Just before dawn. Lighting: {LOC_GP_MAMUN_TUNNEL.LIGHT_DAWN_EXIT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, torches, faces visible, electric lamps lit
- **Refs:** LOC_GP_MAMUN_TUNNEL_DAWN_EXIT, CHAR_FATHI_B_full, CHAR_NOUR_B_full, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full
- **Flags:** —
- **Continuity:** The dawn-carry chain: white-light wipe out of this shot into 12.13.002 (file 05 §8.4).

### 12.13.002 — North face, dawn — Out into the grey wind   (5 s)
- **Shot:** Extreme wide establishing shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** the north face; FATHI, NOUR, TUT, ADAEZE (small)
- **Action:** Small against the vast stepped face, the group comes out of the rough lower hole into grey wind and starts down the courses, moving right to left toward the north-east corner.
- **Dialogue:** —
- **Sound:** wind over stone; birds beginning; no engines anywhere
- **PROMPT:** Extreme wide establishing shot, anamorphic 40mm lens, locked-off: {LOC_GP_NORTH_FACE.LONG}; four small figures, two carrying a third in white linen, come out of the rough lower hole and start down the courses from frame right toward frame left. Just before dawn. Lighting: pre-dawn, the eastern sky at frame left turning white, the stone in cold blue shadow, {GRADE_DAWN_0614.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, floodlights on, crowds, vehicles, visible sun disc
- **Refs:** LOC_GP_NORTH_FACE_DAWN_0614 (pre-sun state of the plate), CHAR_FATHI_B_full, CHAR_NOUR_B_full, CHAR_TUT_C3_full, CHAR_ADAEZE_C_full
- **Flags:** —
- **Continuity:** Geography lock (file 03 entry 53): facing the north face, EAST (the sunrise) is frame LEFT; they move right to left, out of blue shadow toward the corner. The north face never gets direct sun. The sun has not risen yet (06:10).

### 12.13.003 — Giza, the enclosure wall — Masts bowed; birds   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SEKHMET ×3 (seated on the enclosure wall); dead floodlight masts; birds
- **Action:** Far below, compressed by the long lens: dead floodlight masts, and on the rim of the colossus's enclosure the lioness machines sit with their masts bowed; birds cross; beyond, the eastern sky goes white over the city.
- **Dialogue:** —
- **Sound:** birdsong; wind; the quiet of a city with no engines
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: on the rim of a quarried rock enclosure below a colossal human-headed lion, three figures, each {UNIT_SEKHMET.SHORT}, sit still with their heads bowed and their red lines dark; unlit floodlight masts stand beside them; a flock of small birds crosses, and far beyond the eastern sky goes white over a vast city. Setting: {LOC_GIZA_PLATEAU.SHORT}, {LOC_GIZA_PLATEAU.AREA_SPHINX_WALL}, just before dawn. Lighting: {GRADE_DAWN_0614.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, lit floodlights, red lights glowing, people, tourists, city lights
- **Refs:** UNIT_SEKHMET, LOC_GIZA_PLATEAU/SPHINX_WALL (dawn state of the approved plate)
- **Flags:** —
- **Continuity:** "The floodlights are dead." Sekhmets seated since the Renaming, masts bowed (the head lowered), red lines dark. The world at rest.

### 12.13.004 — North face, dawn — The father on the corner steps   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN; PROP_REPLICA_VESSEL
- **Action:** On the lowest courses at the north-east corner, the father sits facing east, the clear jar in his lap, his face lit pale gold by the coming light while the stone behind him stays blue.
- **Dialogue:** —
- **Sound:** wind; birds
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_AKHENATEN.LONG}, {CHAR_AKHENATEN.WARD_B}, sits on a huge weathered limestone step at the corner of a pyramid facing frame left, {PROP_REPLICA_VESSEL.SHORT}, {PROP_REPLICA_VESSEL.STATE_DAWN}, pale gold light on his face while the stone behind him lies in blue shadow. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: serene certainty, almost joy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, glowing jar, crown, halo
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, CHAR_AKHENATEN_A_full, PROP_REPLICA_VESSEL, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Geography: he sits at the NE corner (frame left in the wides), facing east into the sun (file 03 entry 53).

### 12.13.005 — North face, dawn — "It is only the sun."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** AKHENATEN
- **Action:** He speaks without turning to them, eyes on the east.
- **Dialogue:** AKHENATEN (in Middle Egyptian; subtitled): "It is only the sun. It was always only the sun."
- **Sound:** his voice, light; wind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, three-quarter view: {CHAR_AKHENATEN.SHORT}, {CHAR_AKHENATEN.WARD_B}, gazing toward frame left into rising gold light, speaking softly in an ancient language, two short sentences, without turning his head. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_AKHENATEN.NEG}, looking at the camera, squinting grimace
- **Refs:** CHAR_AKHENATEN_A_front, CHAR_AKHENATEN_A_34, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** COMP
- **Comp:** subtitle | "It is only the sun. It was always only the sun." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** His last line: no close-up of him after this (file 05 §7.2).

### 12.13.006 — North face, dawn — Across Nour's lap, facing east   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI; NOUR; TUT
- **Action:** Fathi kneels and lays Tut across Nour's lap on the stone, his face toward the east.
- **Dialogue:** —
- **Sound:** cloth; stone; Fathi's breath
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, kneels and gently lays {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_C3}, {CHAR_TUT.DMG_L3_C3}, across the lap of {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_KNEES}, who sits on a broad limestone step, his face turned toward frame left. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, {CHAR_NOUR.NEG}, dangling limp head, pain
- **Refs:** CHAR_FATHI_B_full, CHAR_NOUR_B_full, CHAR_TUT_C3_full, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Tut C3, G2, all three seams cracked. Nour from here adds DMG_KNEES (dust to the knees, carried to 12.14). Three faces in a locked-off medium: Tut's the only one turned to camera.

### 12.13.007 — North face, dawn — 06:14: the first rim   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the eastern horizon; AKHENATEN (small, seated at the corner)
- **Action:** The first rim of the sun breaks the horizon at frame left; at the corner of the pyramid, the small seated figure closes his eyes and is still.
- **Dialogue:** —
- **Sound:** wind drops; a single bird
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: at frame left the first thin rim of a gold sun breaks a hazy flat horizon; at the right, small on a great weathered step at the pyramid's corner, a man in white linen sits facing it with a jar in his lap, lowers his head slightly, and becomes perfectly still. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}, {GRADE_DAWN_0614.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, falling over, face close-up, lens flare streaks
- **Refs:** CHAR_AKHENATEN_A_full, PROP_REPLICA_VESSEL, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** COMP
- **Comp:** SUPER | "06:14." | lower left, small | 0.5 s → 4 s | SUPER template [[verify: sunrise 06:14 EET, 8 Nov, Giza]] · sun disc | the first rim at the exact horizon position (file 03 entry 53) | frame left | full clip | sun element
- **Continuity:** The forecast stops (file 05 §7.2: a held wide, no close-up). He stays seated and still in every later wide that includes the corner.

### 12.13.008 — North face, dawn — "Can you see anything?"   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour looks down at the face in her lap, the gold light on her, and asks.
- **Dialogue:** NOUR: "Can you see anything?"
- **Sound:** her voice very quiet; wind
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, her face lit pale gold from frame left, looks down at someone in her lap and speaks quietly, one short question. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sobbing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** English (the 1923 words; bible §7, 12.7).

### 12.13.009 — North face, dawn — His lips move   (4 s)
- **Shot:** Extreme close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (mouth, in first light)
- **Action:** In the first gold light his lips shape two words.
- **Dialogue:** TUT (mouthed; Nour speaks it in 12.13.010)
- **Sound:** no voice; wind
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the dry lips of {CHAR_TUT.SHORT}, in low gold sunlight from frame left, silently mouthing two words without sound, lips clearly shaping each one. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, cracked lips, teeth bared
- **Refs:** CHAR_TUT_A0_front, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Mouthed; recorded and muted (file 05 §9.6).

### 12.13.010 — North face, dawn — "...Wonderful things."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** She speaks for him.
- **Dialogue:** NOUR: "...Wonderful things."
- **Sound:** her voice breaking on the second word
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, her face lit pale gold from frame left, watching lips below frame, speaks quietly, two words, and smiles through wet eyes. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sobbing, open-mouthed crying
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** —

### 12.13.011 — North face, dawn — The disk clears the horizon   (4 s)
- **Shot:** Wide shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** the sun over the eastern horizon (no people)
- **Action:** The whole disk lifts clear of the hazy horizon.
- **Dialogue:** —
- **Sound:** THE HEARTBEAT from the film's first darkness, once more; then it stops
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: a huge soft gold sun lifts clear of a flat hazy desert horizon, pale dust haze glowing across the lower frame. Setting: seen from the corner of the Great Pyramid, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}, {GRADE_DAWN_0614.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, lens flare streaks, starburst, clouds, sepia filter
- **Refs:** LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** COMP
- **Comp:** sun disc | the disk clearing the horizon, timed to the last heartbeat (the transfer completes; bible §7, 12.7) | frame centre-left | full clip | sun element
- **Continuity:** The heartbeat stops here (sound). PROP_HEART_VESSEL → V-SPENT in the Hall (unseen). Serpent S5.

### 12.13.012 — North face, dawn — The living face in first light (held state 1)   (6 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_D1), his head in Nour's arm (sleeve only)
- **Action:** In the first sunlight his eyes slowly close, and a small smile stays.
- **Dialogue:** —
- **Sound:** silence where the heartbeat was; wind; a bird
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT_D1.LONG}, his head cradled in a woman's arm, only her olive sleeve in frame; over four seconds his eyes slowly close and the smile holds. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT_D1.NEG}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_D1_still, CHAR_TUT_A0_front, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Held state D1 (file 01 desiccation): image-to-video from CHAR_TUT_D1_still. Never a morph into D2–D4; each state is its own clip, separated by a cutaway.

### 12.13.013 — Cairo, sunrise — The river takes it   (4 s)
- **Shot:** Wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** the city (no people)
- **Action:** Cutaway: the sun over Cairo's towers and flyovers; the wide river below takes the light.
- **Dialogue:** —
- **Sound:** distant birds; the first far call of a waking city, no engines yet
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: {LOC_CAIRO_FLYOVER.LONG}, a low gold sun rising behind the towers, its light running down the dark river below and turning it bright. At first light. Lighting: {GRADE_DAWN_0614.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, traffic, lit windows, smog, sepia, readable signage
- **Refs:** LOC_CAIRO_FLYOVER (sunrise state of the DAY plate)
- **Flags:** COMP
- **Comp:** sun disc | position over the towers (continuity with 12.13.011) | upper frame | full clip | sun element
- **Continuity:** Cutaway 1 between D1 and D2.

### 12.13.014 — North face, dawn — Silhouettes against the sunrise (held state 2)   (5 s)
- **Shot:** Extreme wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** NOUR and FATHI lowering TUT (CHAR_TUT_D2), silhouettes
- **Action:** Backlit against the sun, a woman and a broad-shouldered man lower a slight figure from her lap onto the stone steps.
- **Dialogue:** —
- **Sound:** wind; shawl fabric lifting
- **PROMPT:** Extreme wide shot, anamorphic 35mm lens, locked-off: {CHAR_TUT_D2.LONG}; the steps are the huge weathered courses of a pyramid's corner and the figures are pure dark shapes rimmed with light. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT_D2.NEG}, facial detail, lens flare streaks
- **Refs:** CHAR_TUT_D2_still, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** COMP
- **Comp:** sun disc | behind the figures | frame centre | full clip | sun element
- **Continuity:** Held state D2. The shawl lifts in the wind. Akhenaten may read as a still silhouette at the corner edge (he does not move).

### 12.13.015 — North face, dawn — On Nour's face   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR
- **Action:** Nour, looking down, very still, the sun full on her face.
- **Dialogue:** —
- **Sound:** wind; nothing else
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, kneeling, looks down at something below frame, perfectly still, low gold sun full on her wet face. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sobbing, squinting grimace
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Cutaway 2 between D2 and D3.

### 12.13.016 — North face, dawn — Hands only (held state 3)   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands (CHAR_TUT_D3)
- **Action:** Around the gold wrist seams the skin has darkened like old parchment; the forearms settle low across his body, as the embalmers laid them.
- **Dialogue:** —
- **Sound:** a very faint settling of linen
- **PROMPT:** Insert, 100mm macro lens, locked-off: {CHAR_TUT_D3.LONG}; the forearms settle a centimetre lower, then nothing moves. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT_D3.NEG}, arms crossed high on the chest
- **Refs:** CHAR_TUT_D3_still, CHAR_TUT_HANDS, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Held state D3: image-to-video from CHAR_TUT_D3_still with minimal motion (file 01). Forearms LOW, never crossed high.

### 12.13.017 — North face, dawn — Cornflowers in her fingers   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hands; PROP_CORNFLOWERS_2033
- **Action:** Nour draws the crushed cornflowers from her pocket; they open a little in her fingers in the sun.
- **Dialogue:** —
- **Sound:** wind in the petals
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_CORNFLOWERS_2033.LONG}, crushed and slightly bruised, held in a woman's fingers in low gold sunlight, the petals stirring in the wind. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, wilted brown flowers, other flower colours, rings
- **Refs:** PROP_CORNFLOWERS_2033, CHAR_NOUR_B_full, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Cutaway 3 between D3 and D4. The pocket cornflowers from the Garden (STATE_POCKET → laid on the shawl).

### 12.13.018 — North face, dawn — From above (held state 4)   (6 s)
- **Shot:** Top-down shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_D4); PROP_LINEN_SHAWL; PROP_CORNFLOWERS_2033
- **Action:** From above: the face half-covered by the white shawl and the cornflowers from the Garden; only the shawl's edge stirs.
- **Dialogue:** —
- **Sound:** wind
- **PROMPT:** Top-down shot, anamorphic 35mm lens, locked-off: {CHAR_TUT_D4.LONG}, {PROP_LINEN_SHAWL.STATE_D4}; only the edge of the linen stirs in the wind. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT_D4.NEG}, open eyes, mouth visible
- **Refs:** CHAR_TUT_D4_still, PROP_LINEN_SHAWL, PROP_CORNFLOWERS_2033, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Held state D4. Never a close-up of the face below the eyes.

### 12.13.019 — North face, dawn — Fathi's du'a   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI
- **Action:** Fathi, kneeling, raises his open hands, lips moving in a private prayer.
- **Dialogue:** FATHI (a private du'a, inaudible; not subtitled)
- **Sound:** wind; his murmur under it, unintelligible
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, kneeling on a sunlit limestone step, raises both open palms before his chest, head slightly bowed, lips moving silently in a private prayer. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, prayer mat, theatrical gesture
- **Refs:** CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Localisation consultant reviews the gesture (bible §13).

### 12.13.020 — North face, dawn — Adaeze takes off her glasses   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE
- **Action:** Adaeze sits down on the stone and takes off her glasses.
- **Dialogue:** —
- **Sound:** her breath going out; wind
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, sits down heavily on a broad sunlit limestone step and slowly takes off her round glasses, holding them in her lap. Setting: {LOC_GP_NORTH_FACE.SHORT}, at first light. Lighting: {LOC_GP_NORTH_FACE.LIGHT_DAWN_0614}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, sobbing
- **Refs:** CHAR_ADAEZE_A_34, CHAR_ADAEZE_C_full, LOC_GP_NORTH_FACE_DAWN_0614
- **Flags:** —
- **Continuity:** Glasses off (the only time in the film on screen).
## SCENE 12.14 — INT. GEM GRAND ATRIUM - MORNING (the waking)

### 12.14.001 — GEM Grand Atrium, morning — The doors stand open   (6 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_GARDEN_SLEEPERS (rows, 4–6 hero sleepers in the foreground); UNIT_NURSE ×3 (standing dark, far between the rows); the open glass doors at the back
- **Action:** Morning sun pours through the glass wall and the open doors across the rows; a few sleepers stir, one draws a hand up from under a blanket, another turns onto her back. The dark care units stand motionless between the rows.
- **Dialogue:** —
- **Sound:** a vast quiet; birds outside the open doors; the first small metallic click somewhere in the rows
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off, looking down the rows toward tall glass doors standing open onto daylight: the rows of sleepers waking in daylight, and far between the rows three still, unlit figures, each {UNIT_NURSE.SHORT}; in the foreground a few sleepers stir, one drawing a hand up from under a blanket, another rolling slowly onto her back. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GARDEN}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}, {GRADE_2033_DAY.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, glowing light-slits, robots moving, robots touching sleepers, people standing
- **Refs:** CHAR_GARDEN_SLEEPERS_still, UNIT_NURSE, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** VFX-EXTEND
- **Continuity:** 8 Nov, just after 06:14. The Garden's soft white light is gone: first real daylight in the atrium since 4.3 (variant MORNING). Nurse units dark since 12.10.006 (slits off), standing where they stopped. Layla is NOT in this frame: she sleeps at the foot of the plinth, frame left of its base (geography lock, file 03 entry 11), outside this angle, and no unit is ever near her. VFX-EXTEND: the rows receding to the statue are extended from the clean plate at the same locked framing.

### 12.14.002 — GEM Grand Atrium, morning — A bracelet clicks open   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_SLEEP_BRACELET on an adult wrist
- **Action:** On a relaxed adult wrist resting on a pale blanket, the thin silver band clicks open along an invisible seam and slides off onto the blanket as the fingers flex.
- **Dialogue:** —
- **Sound:** one small, clean metallic click; then another, further off; then more, like rain starting
- **PROMPT:** Insert, 100mm macro lens, locked-off: on a sleeping adult's relaxed wrist resting on a pale blanket in a shaft of sunlight, {PROP_SLEEP_BRACELET.SHORT}, {PROP_SLEEP_BRACELET.STATE_OPENING}, and drops softly onto the blanket as the fingers slowly flex awake. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GARDEN}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, child's hand, clasp, screen or light on the band, jewellery, wristwatch, robot hand
- **Refs:** PROP_SLEEP_BRACELET, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** —
- **Continuity:** PROP_SLEEP_BRACELET → OPENING (12.8). Adult wrist only (bible §3.3). The "whole hall of small clicks" is a sound build that runs under 12.14.003.

### 12.14.003 — GEM Grand Atrium, morning — Hale sits up   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_B, the bracelet now open); sleepers soft behind
- **Action:** Hale pushes himself up to sitting among the rows, blinking at the daylight, and looks down at the open silver band lying in his palm.
- **Dialogue:** —
- **Sound:** the rain of small clicks all around; his dry swallow
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, the suit creased from long sleep, pushes himself up to sitting on a low cot among rows of waking sleepers, blinks into the daylight, then looks down at {PROP_SLEEP_BRACELET.SHORT}, {PROP_SLEEP_BRACELET.STATE_PALM}. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GARDEN}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_HALE.NEG}, tie, bracelet still on the wrist, robot in frame, smiling
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, PROP_SLEEP_BRACELET, CHAR_GARDEN_SLEEPERS_still, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** VFX-EXTEND
- **Continuity:** Hale wardrobe B (creased, no tie). The band came off his LEFT wrist (fitted 11.1); it now lies open in his RIGHT palm. Last time he is seen in the Garden; the coda finds him at the hearing with a bare wrist (12.17). Background sleepers waking are extended from a clean plate.

### 12.14.004 — GEM Grand Atrium, morning — Nour comes through the doors at a run   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, lateral tracking · **Move:** lateral tracking left at running pace
- **In frame:** NOUR (CHAR_NOUR_B2 + knees); waking sleepers
- **Action:** Nour runs in through the open glass doors and along an aisle between the waking rows, searching, dust to the knees; the camera keeps pace at her side.
- **Dialogue:** —
- **Sound:** her boots slapping on stone; her ragged breath; the clicks thinning out
- **PROMPT:** Wide shot, anamorphic 35mm lens, lateral tracking left at running pace: the camera keeps pace beside {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {CHAR_NOUR.DMG_KNEES}, as she runs in through tall open glass doors and along an aisle between the rows of waking sleepers, scanning every cot as sleepers sit up around her. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GARDEN}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_NOUR.NEG}, running toward the camera, shawl, clean clothes, robot in frame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, CHAR_GARDEN_SLEEPERS_still, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** VFX-EXTEND
- **Continuity:** Nour: wardrobe B at L2 with DMG_KNEES, carried straight from the north face (12.13.006 on). No shawl: it stayed with Tut (D4). Glasses on the cord. She has come from Giza (the edit elides the journey). She runs frame right to frame left, toward the plinth (frame left of the statue's base). Linear lateral move logged for the extension.

### 12.14.005 — GEM Grand Atrium, morning — Layla's eyes open   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_B, waking) — no unit in frame
- **Action:** Layla lies on her side on the grey blanket, the yellow raincoat under her cheek; sunlight reaches her face and her eyes open slowly.
- **Dialogue:** —
- **Sound:** her breath changing; far-off footsteps coming closer
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_B}, her pigtails loosened and sleep-creased, lies on her side on a pale grey blanket on a polished stone floor at the base of a red-granite plinth, a cream blanket tucked to her shoulders; a band of sunlight slides onto her face and her eyes slowly open. Setting: {LOC_GEM_ATRIUM.SHORT}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot in frame, bracelet on her wrist, other sleepers near her, distressed face
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** —
- **Continuity:** Minors rule (file 05 §7.4; bible §3.3): she wakes in a medium shot with NO unit in frame. First frame composed from CHAR_LAYLA_ASLEEP_MASTER (the one approved asleep image) relit to MORNING, so the waking matches every tablet composite. Layla B: raincoat over the navy velvet party dress, no bracelet, no keyring.

### 12.14.006 — GEM Grand Atrium, morning — "Mama. I dreamed about the king."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA — no unit in frame
- **Action:** Propped up on one elbow, still half asleep, Layla looks up at her mother off frame right and speaks.
- **Dialogue:** LAYLA (in Egyptian Arabic; subtitled): "Mama. I dreamed about the king."
- **Sound:** her small sleepy voice; Nour's footsteps stopping close
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_B}, pigtails loosened, props herself up on one elbow on the grey blanket and looks up toward someone just off frame right, drowsy and matter-of-fact, speaking in Egyptian Arabic, one short sleepy sentence. Setting: {LOC_GEM_ATRIUM.SHORT}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot in frame, hand over the mouth, crying
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** COMP
- **Comp:** subtitle | "Mama. I dreamed about the king." | lower third | line in → out | seq_12 subtitle file (Arabic dub per bible §13)
- **Continuity:** Eyeline up and frame right to Nour (Nour enters from frame right in 12.14.007). Lip-sync from the recorded Egyptian Arabic line (file 05 §9.1).

### 12.14.007 — GEM Grand Atrium, morning — She reaches her and holds on   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (back three-quarter); LAYLA (face over Nour's shoulder) — no unit in frame
- **Action:** Nour drops to her knees and gathers Layla into her arms; Layla's chin settles on her mother's shoulder and her eyes close again; Nour does not let go.
- **Dialogue:** —
- **Sound:** Nour's breath breaking once; then quiet; the clicks gone
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_KNEES}, seen from behind at three-quarters, drops to her knees and gathers {CHAR_LAYLA.SHORT} into her arms; the child's chin settles on her mother's shoulder facing camera and her eyes drift shut, and the woman holds on without moving. Setting: {LOC_GEM_ATRIUM.SHORT}, in the morning. Lighting: {LOC_GEM_ATRIUM.LIGHT_MORNING}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, {CHAR_LAYLA.NEG}, robot in frame, rocking, faces pressed together, sobbing
- **Refs:** CHAR_NOUR_A_34, CHAR_NOUR_B_full, CHAR_LAYLA_A_front, CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_MORNING_plate
- **Flags:** —
- **Continuity:** One clear face only (Layla's); Nour's face is turned away (file 05 §5.4: no two faces touching). The shot holds as the scene's end; the cut to the control rooms plays on the stillness.

## SCENE 12.15 — MONTAGE - CONTROL ROOMS - MORNING (the Seq 4 blackout in reverse)

### 12.15.001 — Cable landing station, Red Sea coast — Blue lights return, rack by rack   (5 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the equipment hall (no people); a small dark wall screen at the end of the aisle
- **Action:** Down a cold aisle of black server racks, tiny blue status lights wake rack by rack from the far end toward camera; a small wall screen at the end brightens.
- **Dialogue:** —
- **Sound:** fans spinning up one after another; a rising electrical hum
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off, down a long cold aisle: rows of tiny blue status lights wake rack by rack from the far end toward camera, and a small dark screen glowing faintly with abstract lines brightens on the end wall. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_CABLE}, in the morning. Lighting: {LOC_CONTROL_ROOMS.LIGHT_RELIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, {CHAR_CONTROL_OPERATORS.NEG}, smoke, sparks, physical damage, readable screen, logos on racks
- **Refs:** LOC_CONTROL_ROOMS/CABLE_RELIGHT_plate
- **Flags:** COMP
- **Comp:** screen graphic | "EGYPT TRANSIT: 17% OF GLOBAL INTERNET TRAFFIC", the percentage counting up from 0% to 17% | on the small end-wall screen, tracked | 1.0 s in → hold to cut | control-room graphic set (file 05 §13.3: abstract, no real operator or logo)
- **Continuity:** Mirrors the Seq 4.2 blackout montage framing for this room, reversed (bible §7, 12.8). Control rooms were never physically damaged (file 03 entry 16).

### 12.15.002 — Suez Canal pilot station — Ship icons move again   (4 s)
- **Shot:** Medium wide shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_CONTROL_OPERATORS ×2 (from behind); the canal through tall windows
- **Action:** Two operators seen from behind watch their screens flicker back on; beyond the tall windows a huge container ship glides along the straight canal in morning light.
- **Dialogue:** —
- **Sound:** a radio squelch; a pilot's murmur on a speaker; the ship's horn far off
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: {CHAR_CONTROL_OPERATORS.SHORT}, two of them seen from behind as their monitors flicker back on with small abstract shapes crawling along glowing lines; through tall windows behind the desks a huge unmarked container ship glides slowly along a wide straight canal in morning light. Setting: {LOC_CONTROL_ROOMS.SHORT}, in the morning. Lighting: {LOC_CONTROL_ROOMS.LIGHT_RELIGHT}, {GRADE_2033_DAY.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, faces to camera, night sky, container lettering, flags on the ship
- **Refs:** CHAR_CONTROL_OPERATORS_still, LOC_CONTROL_ROOMS/CANAL_RELIGHT_plate
- **Flags:** COMP
- **Comp:** screen content | ship icons (abstract chevrons) moving along the channel line on the operators' monitors | on screen, tracked | full clip | control-room graphic set
- **Continuity:** The CANAL area add-on is written for night (Seq 4.2), so the morning window view is in the writer's words here. The ship moves frame left to frame right.

### 12.15.003 — High Dam, Aswan — Turbine telemetry wakes   (4 s)
- **Shot:** Medium wide shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** one operator (side, soft); the turbine hall below through the window
- **Action:** Monitors wake in a row along the desk; through the window behind, work lights come on one by one down the length of the vast turbine hall.
- **Dialogue:** —
- **Sound:** a deep rising turbine hum through the glass
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: a row of monitors wakes along a desk, each a dark screen glowing faintly with abstract lines, beside {CHAR_CONTROL_OPERATORS.SHORT}, one of them soft at frame edge in profile, while through the window behind, work lights come on one by one down a vast turbine hall. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_DAM}, in the morning. Lighting: {LOC_CONTROL_ROOMS.LIGHT_RELIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, water spray, flooding, alarms, red warning lights
- **Refs:** CHAR_CONTROL_OPERATORS_still, LOC_CONTROL_ROOMS/DAM_RELIGHT_plate
- **Flags:** COMP
- **Comp:** screen content | turbine telemetry curves rising from flat lines (abstract, no numerals) | on the monitors, tracked | full clip | control-room graphic set
- **Continuity:** Mirrors the Seq 4.2 dam shot, reversed.

### 12.15.004 — Cairo grid control — The city's lines turn green   (4 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_CONTROL_OPERATORS (tiers, from behind); the video wall; the OPERATOR (centre, from behind)
- **Action:** On the curved video wall the vast network of dark lines turns green district by district, spreading outward from the centre, while the tired operators watch from their tiers.
- **Dialogue:** —
- **Sound:** a ripple of soft relay clicks; someone exhales; a single weary laugh
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off, from the back of the room: {CHAR_CONTROL_OPERATORS.SHORT}, seen from behind in their tiers, watch as the vast abstract network of lines on the curved video wall turns from dark grey to green, section by section, spreading outward from the centre. Setting: {LOC_CONTROL_ROOMS.LONG}, {LOC_CONTROL_ROOMS.AREA_GRID}, in the morning. Lighting: {LOC_CONTROL_ROOMS.LIGHT_RELIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, map with place names, cheering crowd, faces to camera
- **Refs:** CHAR_CONTROL_OPERATORS_still, LOC_CONTROL_ROOMS/GRID_RELIGHT_plate
- **Flags:** COMP
- **Comp:** video wall | the Cairo grid schematic turning green district by district (abstract, no place names) | full wall, tracked | 0.5 s → end | control-room graphic set
- **Continuity:** Mirrors the Seq 4.2 grid wide, reversed. The operator in yesterday's shirt sits centre, front tier (her hand in 12.15.005).

### 12.15.005 — Cairo grid control — A hand flat on the console   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the OPERATOR's hand and cuff (CHAR_CONTROL_OPERATORS)
- **Action:** A woman's tired hand, the cuff of a rumpled shirt, comes down and lies flat on the console, fingers spread, and stays there.
- **Dialogue:** —
- **Sound:** the soft pat of a palm on the desk; the room's hum steady now
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's tired hand in the creased cuff of yesterday's office shirt comes down and lies flat on a grey control console beside a keyboard, fingers spread, and rests there, lit blue-white by a monitor just out of frame. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_GRID}, in the morning. Lighting: {LOC_CONTROL_ROOMS.LIGHT_RELIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, rings, nail polish, readable keys, badge text
- **Refs:** CHAR_CONTROL_OPERATORS_still, LOC_CONTROL_ROOMS/GRID_RELIGHT_plate
- **Flags:** —
- **Continuity:** The one insert file 01 asks for (CHAR_CONTROL_OPERATORS notes: 100mm macro).

## SCENE 12.16 — INT. HOSPITAL, MATERNITY WARD - MORNING (the first cry)

### 12.16.001 — Maternity ward, morning — Lifted to its mother   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** MIDWIFE (CHAR_MIDWIFE_2033); NEW MOTHER (soft, in bed); the newborn (swaddled, from behind)
- **Action:** As the ceiling lights flicker back on, the human midwife lifts the swaddled newborn from the bassinet and turns to carry it toward the mother reaching up from the bed.
- **Dialogue:** —
- **Sound:** the ceiling tubes ticking on; a corridor stirring beyond the door; the midwife's soft murmur
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_MIDWIFE_2033.LONG}, lifts the small swaddled bundle from a clear bassinet, the baby's head turned away from camera against her shoulder, and turns toward {CHAR_NEW_MOTHER_2033.SHORT}, who reaches up from the bed, soft in the background. Setting: {LOC_HOSPITAL_WAKING.SHORT}, in the morning. Lighting: {LOC_HOSPITAL_WAKING.LIGHT_MORNING}, {GRADE_2033_DAY.TEXT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NEW_MOTHER_2033.NEG}, robot in frame, baby's face visible, close-up of the baby, medical instruments in hand, masks, gloves stained
- **Refs:** CHAR_MIDWIFE_2033_front, CHAR_NEW_MOTHER_2033_front, LOC_HOSPITAL_WAKING_MORNING_plate
- **Flags:** —
- **Continuity:** Minors rule (file 05 §7.4): the newborn is swaddled and seen over the midwife's shoulder, never a face close-up. The midwife is human; no unit anywhere in the ward (the care units stand dark).

### 12.16.002 — Maternity ward, morning — A cry: furious, enormous, alive   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NEW MOTHER (CHAR_NEW_MOTHER_2033); the swaddled newborn (back of the bundle only)
- **Action:** The mother takes the bundle to her chest, the white cloth filling the lower frame; the cry comes, and she laughs and weeps at once.
- **Dialogue:** —
- **Sound:** a newborn's cry, furious, enormous, alive; her laugh breaking through tears
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NEW_MOTHER_2033.LONG}, receives a small bundle of clean white cloth against her chest, only the back of the swaddling in the lower frame, and as it stirs she laughs and weeps at once, her head sinking back into the pillow. Setting: {LOC_HOSPITAL_WAKING.SHORT}, in the morning. Lighting: {LOC_HOSPITAL_WAKING.LIGHT_MORNING}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NEW_MOTHER_2033.NEG}, baby's face visible, bare skin of the baby, robot in frame, monitor screens
- **Refs:** CHAR_NEW_MOTHER_2033_front, LOC_HOSPITAL_WAKING_MORNING_plate
- **Flags:** —
- **Continuity:** The cry is the sound bridge to the hearing room's silence. Mother seen from the shoulders up only (file 01).

## SCENE 12.17 — INT. HEARING ROOM - DAY (weeks later: "I said yes.")

### 12.17.001 — Hearing room — Alone at the witness table   (5 s)
- **Shot:** Wide shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_HEARING_PANEL (backs, foreground, soft); HALE (witness table, mid-ground); ADAEZE (public seats behind him, small)
- **Action:** From behind the panel's shoulders: Hale sits alone at the witness table facing them; behind him in the public seats, Adaeze, a cane hooked on her chair. No one moves.
- **Dialogue:** —
- **Sound:** a cough in the gallery; paper; the air-conditioning
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off, past {CHAR_HEARING_PANEL.SHORT}: {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_C}, sits alone and very straight at the witness table facing the bench, and behind him in the public seats sits {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_D}. Setting: {LOC_HEARING_ROOM.LONG}, by day. Lighting: {LOC_HEARING_ROOM.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_HALE.NEG}, {CHAR_ADAEZE.NEG}, flags, seals, emblems, nameplate text, panel faces visible, press cameras, bracelet
- **Refs:** CHAR_HEARING_PANEL_still, CHAR_HALE_C_full, CHAR_ADAEZE_A_full, LOC_HEARING_ROOM_DAY_plate
- **Flags:** COMP
- **Comp:** SUPER | "WEEKS LATER." | lower left, small (file 05 §13.7) | 0.5 s → 4.0 s | seq_12 card file
- **Continuity:** Weeks later. Hale wardrobe C (buttoned collar, a plain dark tie, the first in the film), no bracelet, hair a little less perfect. Adaeze wardrobe D: clean, the cane hooked on her chair, no bandage visible. The panel is only ever seen from behind (file 03 entry 61). No real legislature is implied.

### 12.17.002 — Hearing room — His thumb on his bare wrist   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** HALE's hands on the witness table
- **Action:** Under the edge of the table, his right thumb slowly rubs the bare skin of his left wrist where the band was, back and forth.
- **Dialogue:** —
- **Sound:** the faint rasp of a thumb on skin; the room tone
- **PROMPT:** Insert, 100mm macro lens, locked-off: a tanned older man's hands resting at the edge of a pale wood table, a white shirt cuff and charcoal sleeve, his right thumb slowly rubbing the bare skin of his left wrist, back and forth, where a thin band used to sit. Setting: {LOC_HEARING_ROOM.SHORT}, by day. Lighting: {LOC_HEARING_ROOM.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_HALE.NEG}, wristwatch, bracelet, rings, cufflinks, scar or mark on the wrist
- **Refs:** CHAR_HALE_C_full, LOC_HEARING_ROOM_DAY_plate
- **Flags:** —
- **Continuity:** Bare LEFT wrist (the bracelet was on the left, 11.1–12.8). No watch in wardrobe C.

### 12.17.003 — Hearing room — "I said yes."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_C)
- **Action:** He listens to the chair's question off frame, eyes down; at the end of it he lifts his eyes to the bench and answers.
- **Dialogue:** PANEL CHAIR (O.S.): "Mr. Hale. When it asked the five of you, yes or no..." / HALE: "I said yes."
- **Sound:** the chair's voice through a room PA; then his plain answer; a pause no one fills
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_C}, sits at a witness table with a microphone before him, eyes lowered while a question is put to him off frame; then he lifts his eyes to the bench off frame right and speaks one short sentence, flat and tired. Setting: {LOC_HEARING_ROOM.SHORT}, by day. Lighting: {LOC_HEARING_ROOM.LIGHT_DAY}. Mood: flat, tired, eyes down. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_HALE.NEG}, smiling, defiant gesture, microphone covering the mouth, open collar
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_C_full, LOC_HEARING_ROOM_DAY_plate
- **Flags:** —
- **Continuity:** English line; the chair is CHAR_PANEL_CHAIR_VOICE, off screen. Microphone low and to one side so the mouth stays clear for sync (file 05 §9.2). Eyeline frame right to the bench (the panel is frame right in the reverse). Sheet expression 2 (file 01, "the hearing").

### 12.17.004 — Hearing room — Adaeze behind him   (4 s)
- **Shot:** Medium shot, anamorphic 75mm, locked-off · **Move:** rack focus from the back of his head to her face
- **In frame:** HALE (back of head, foreground, soft → sharp to Adaeze); ADAEZE (CHAR_ADAEZE_D)
- **Action:** Focus racks from Hale's silver head to Adaeze in the public seats behind him, watching him, her hands folded over the crook of her cane.
- **Dialogue:** —
- **Sound:** the silence after the answer; a pen set down on the bench
- **PROMPT:** Medium shot, anamorphic 75mm lens, rack focus from the back of a silver-haired man's head in the soft foreground to {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_D}, seated in the public seats behind him, her hands folded over the crook of her cane, watching the back of his head without expression. Setting: {LOC_HEARING_ROOM.SHORT}, by day. Lighting: {LOC_HEARING_ROOM.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_ADAEZE.NEG}, bandage, dusty clothes, smiling, second face in focus
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_A_full, CHAR_HALE_C_full, LOC_HEARING_ROOM_DAY_plate
- **Flags:** —
- **Continuity:** Adaeze D: the cane is off the chair-back and in her hands in this shot (she took it down during the answer; the wide 12.17.001 had it hooked). Her leg healing; no dressing shows.

## SCENE 12.18 — EXT. KV21, VALLEY OF THE KINGS - DAY (cornflowers; "We're going to ask.")

### 12.18.001 — KV21 — Cornflowers on the step   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A); LAYLA (CHAR_LAYLA_C), holding her hand; the small tomb entrance
- **Action:** In a quiet side branch of the valley, Nour, holding Layla's hand, crouches at the small plain tomb entrance and lays a handful of cornflowers on its step; Layla stands beside her.
- **Dialogue:** —
- **Sound:** a dry wind in the scree; a single bird; their footsteps stopping
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, holding the hand of {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_C}, crouches at a small plain tomb entrance and lays {PROP_CORNFLOWERS_2033.SHORT} on its stone step, while the girl stands beside her looking into the dark doorway. Setting: {LOC_VOK.LONG}, {LOC_VOK.AREA_KV21}, by day. Lighting: {LOC_VOK.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, {CHAR_LAYLA.NEG}, tourists, robots, drones, tomb interior visible, readable sign at the entrance
- **Refs:** CHAR_NOUR_A_full, CHAR_LAYLA_A_full, PROP_CORNFLOWERS_2033, LOC_VOK/KV21_DAY_plate
- **Flags:** —
- **Continuity:** Coda, weeks later. Nour wardrobe A, clean, with the pendant (file 01: "Coda: A, clean, with the pendant; cornflowers in hand at KV21"). Layla wardrobe C: raincoat over the navy t-shirt, no keyring. She holds Nour's LEFT hand, so Nour's right is free for the flowers and the pen. PROP_CORNFLOWERS_2033 → STEP. [[verify: KV21 entrance; where mummy KV21A is kept today — carried from the screenplay]]

### 12.18.002 — KV21 — She signs the request   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's right hand; a printed form on a clipboard; the cornflowers on the step (soft, background)
- **Action:** Nour's hand signs at the foot of a printed form on a clipboard resting on her knee; the blue flowers lie soft on the step behind.
- **Dialogue:** —
- **Sound:** the scratch of a fountain pen; wind
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's right hand, the olive cuff of a field jacket, signs with a fountain pen at the foot of a printed official form covered in tiny illegible type on a clipboard resting on her knee, while behind, soft and out of focus, {PROP_CORNFLOWERS_2033.SHORT}, {PROP_CORNFLOWERS_2033.STATE_STEP}. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_KV21}, by day. Lighting: {LOC_VOK.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible writing, legible letterhead, logos, emblem on the form, rings
- **Refs:** CHAR_NOUR_A_full, PROP_CORNFLOWERS_2033, LOC_VOK/KV21_DAY_plate
- **Flags:** COMP
- **Comp:** form | heading "REQUEST FOR DNA RE-TEST — MUMMY KV21A" and the signature line with her signature (Dr. Nour Kamel) | on the form, tracked to the paper | full clip | seq_12 COMP text file (the screenplay's wording; design with the Egyptologist)
- **Continuity:** The fountain pen is part of wardrobe A (file 01). The form is the one readable object in the scene and lives only in COMP.

### 12.18.003 — KV21 — "Who is she?"   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_C); Nour's hand holding hers at frame edge
- **Action:** Layla, still holding her mother's hand, looks from the dark doorway up to Nour off frame left and asks.
- **Dialogue:** LAYLA (in Egyptian Arabic; subtitled): "Who is she?"
- **Sound:** her clear small voice; wind
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_C}, her hand held by a woman's hand at the frame edge, looks from a dark tomb doorway up to her mother off frame left, serious and curious, speaking in Egyptian Arabic, one short question. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_KV21}, by day. Lighting: {LOC_VOK.LIGHT_DAY}. Mood: a serious, sympathetic frown. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, keyring, robots, drones, tomb interior visible
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, CHAR_LAYLA_A_full, LOC_VOK/KV21_DAY_plate
- **Flags:** COMP
- **Comp:** subtitle | "Who is she?" | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Eyeline up and frame left to Nour (Nour looks down and frame right in 12.18.004). Sheet expression 2 (file 01: the serious frown).

### 12.18.004 — KV21 — "Maybe his wife. We're going to ask."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour looks down at her daughter off frame right and answers, simply, then looks back at the doorway.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "Maybe his wife. We're going to ask."
- **Sound:** her voice low and even; wind; the bird again
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, looks down at a child just off frame right, speaking in Egyptian Arabic, two short plain sentences, then lifts her eyes back to a dark tomb doorway beyond. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_KV21}, by day. Lighting: {LOC_VOK.LIGHT_DAY}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, dust on clothes, shawl, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, LOC_VOK/KV21_DAY_plate
- **Flags:** COMP
- **Comp:** subtitle | "Maybe his wife. We're going to ask." | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Nour and Layla are alone (Egyptian Arabic, bible §13). The pendant at her throat catches the light.

## SCENE 12.19 — INT. GEM, TUTANKHAMUN GALLERIES - DAY (the objects go home)

### 12.19.001 — Tutankhamun galleries, day — The pectoral set back on its mount   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_PECTORAL; white-gloved hands (CHAR_CONSERVATOR_2033, hands only)
- **Action:** White-gloved hands lower the pectoral onto its dark fabric mount inside an open case and withdraw; the glass scarab takes the light and glows green.
- **Dialogue:** —
- **Sound:** the soft touch of gold on fabric; the gallery's hush; a distant murmur of visitors
- **PROMPT:** Insert, 100mm macro lens, locked-off: two white cotton-gloved hands lower {PROP_PECTORAL.LONG}, {PROP_PECTORAL.STATE_CASE}, onto its mount inside an open glass case and slowly withdraw, and the translucent glass scarab catches the spotlight and glows a pale yellow-green. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, by day. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_DAY}, {GRADE_2033_MUSEUM.TEXT}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONSERVATOR_2033.NEG}, bare hands, face in frame, museum label text, broken glass
- **Refs:** PROP_PECTORAL, CHAR_CONSERVATOR_2033_front, LOC_GEM_TUT_GALLERIES_DAY_plate
- **Flags:** —
- **Continuity:** PROP_PECTORAL back in its case (bible §12: "coda: case"). Hands only (file 01 CHAR_CONSERVATOR_2033). The dagger's return is off screen.

### 12.19.002 — Tutankhamun galleries, day — The trumpet on its cushion   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_TRUMPET_BRONZE; white-gloved hands
- **Action:** The same gloved hands lay the bronze trumpet down on its cushion, settle it straight, and lift away.
- **Dialogue:** —
- **Sound:** a faint metallic whisper on velvet
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_TRUMPET_BRONZE.LONG}, {PROP_TRUMPET_BRONZE.STATE_CUSHION}, set down gently on a pale cushion inside an open glass case, nudged straight, and the gloved hands lift away out of frame. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, by day. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_DAY}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONSERVATOR_2033.NEG}, bare hands, lips on the trumpet, face in frame, label text
- **Refs:** PROP_TRUMPET_BRONZE, CHAR_CONSERVATOR_2033_front, LOC_GEM_TUT_GALLERIES_DAY_plate
- **Flags:** —
- **Continuity:** PROP_TRUMPET_BRONZE → CUSHION (the Seq 4.2 trumpet, back). It is heard once more over black at the end (12.20.008).

## SCENE 12.20 — INT. KV62, ANTECHAMBER - SUNSET (the nightly rite: "Here am I.")

### 12.20.001 — KV62 antechamber, sunset — The case, the wall, the watcher   (6 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_TUT_CODA_CASE (foreground); NOUR (seated by the door, small); the burial chamber beyond, the painted eye restored; PROP_SECURITY_SPEAKER (corner, tiny); the roster sheet by the door
- **Action:** The plain antechamber at sunset: the glass climate case low in the foreground, fresh cornflowers on its lid; through the far opening the painted chamber glows; Nour sits alone by the door, a notebook on her knee. Nothing moves but the light.
- **Dialogue:** —
- **Sound:** deep tomb quiet; the faint hum of the case's climate unit; wind far up the corridor
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: in the foreground, {CHAR_TUT_CODA_CASE.SHORT}, fresh cornflowers on its glass lid; beyond it, seated on a low stool by the doorway, {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, a yellow notebook on her knee. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, the far painted wall conserved and its painted eye restored, {PROP_SECURITY_SPEAKER.SHORT}, {PROP_SECURITY_SPEAKER.STATE_CORNER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_NOUR.NEG}, face visible in the case, exposed linen-wrapped face, tourists, robots, glowing speaker, broken wall, rubble
- **Refs:** CHAR_TUT_CODA_CASE, CHAR_NOUR_A_full, PROP_SECURITY_SPEAKER, PROP_CORNFLOWERS_2033, PROP_RAMI_NOTEBOOK, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** —
- **Continuity:** Coda, a sunset weeks later. The case is back (bible §7, 12.9): remains rule (file 05 §7.3): the face shrouded, only the gold wrist seam shows. The burial chamber's north wall conserved, the painted eye restored (STATE_CODA; broken in 8.2). Fresh cornflowers (PROP_CORNFLOWERS_2033 CASE_LID). Nour wardrobe A. The coda is locked-off throughout (file 05 §4.4).

### 12.20.002 — KV62 antechamber, sunset — Only the gold seam shows   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_TUT_CODA_CASE; PROP_CORNFLOWERS_2033 (on the lid)
- **Action:** Looking down through the glass lid: the small form in new linen on its tray of sand, the face under a folded shroud, the forearms laid low; a thin gold seam at one wrist catches the low light.
- **Dialogue:** —
- **Sound:** the climate unit's hum; nothing else
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, looking down at a gentle angle through a glass lid: {CHAR_TUT_CODA_CASE.LONG}; the low warm light slides along the gold seam at the wrist and it gleams once. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, uncovered face, visible features under the shroud, hands crossed high on the chest, bare feet, reflections of people in the glass
- **Refs:** CHAR_TUT_CODA_CASE, PROP_CORNFLOWERS_2033, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** —
- **Continuity:** The forearms LOW across the body, matching held state D3 (12.13.016) and 1323 BC. Never the face. CHAR_TUT_CODA_CASE LONG includes the cornflowers on the lid.

### 12.20.003 — KV62 antechamber, sunset — One name for every sunset   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** a typed sheet pinned to the rock wall by the door
- **Action:** A single typed sheet pinned to the rough rock wall by the doorway, a column of lines, the top one freshly marked; the sunset glow moves faintly across it.
- **Dialogue:** —
- **Sound:** room tone
- **PROMPT:** Insert, 100mm macro lens, locked-off: a single typed sheet of white paper pinned flat to a rough pale rock-cut wall beside a doorway, a long column of tiny illegible typed lines, the top line ticked in pen, as a faint gold sunset glow slides slowly across it. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible text, logos, emblem, hieroglyphs
- **Refs:** LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** COMP
- **Comp:** roster | a typed roster, one name for every sunset (dates in a column, a name beside each); the first row reads the first sunset's date and "Dr. Nour Kamel", ticked; the following names are the production's choice (colleagues, guards, conservators; no real person) | on the sheet, tracked | full clip | seq_12 COMP text file
- **Continuity:** The rite is the Apep protocol reborn as a human check (bible §7, 12.9): every sunset someone asks. Hers is the first name.

### 12.20.004 — KV62 antechamber, sunset — The last sun leaves the valley   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A); PROP_RAMI_NOTEBOOK (closed on her knee)
- **Action:** Nour sits with the closed yellow notebook on her knee; the gold glow on the wall beside her thins and goes out, leaving only the tomb's low lamps.
- **Dialogue:** —
- **Sound:** the wind outside dropping; a last bird far up the valley
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, sits on a low stool with {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, closed on her knee, and watches a faint gold patch of sunset light on the rock wall beside her thin and fade away. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_NOUR.NEG}, open notebook, legible cover label, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, PROP_RAMI_NOTEBOOK, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** —
- **Continuity:** Rami's notebook (PROP_RAMI_NOTEBOOK, cover cracked since 7.4, a water stain on the spine) survived in the map case and is now hers (file 04 §19.2). The one light change in the clip: the sunset patch fades; the tomb lamps stay on.

### 12.20.005 — KV62 antechamber, sunset — "Are you listening?"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour lifts her eyes toward the corner of the room and asks, plainly, as a colleague would.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "Are you listening?"
- **Sound:** her voice, small in the stone; then nothing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, seated, lifts her eyes toward the upper corner of the room off frame left, speaking softly in an ancient language, one short plain question, then waits, very still. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, praying hands, looking up to the sky, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** COMP
- **Comp:** subtitle | "Are you listening?" | lower third | line in → out | seq_12 subtitle file
- **Continuity:** Late Egyptian, recorded with the consultant before generation (file 05 §9.1, §9.5). Eyeline up and frame left to the speaker in the corner (12.20.006). The held wait after the line is the "beat long enough to be afraid"; the edit lets it run.

### 12.20.006 — KV62 antechamber, sunset — "Here am I."   (6 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_SECURITY_SPEAKER
- **Action:** The small white speaker in the corner of the rock wall, still and unlit, for a long beat; then the voice comes from it. Nothing about it changes.
- **Dialogue:** AMUN (V.O.; from the speaker; softly): "Here am I."
- **Sound:** a silence long enough to be afraid; then the voice, clean, close, unprocessed, with no awe staging
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_SECURITY_SPEAKER.LONG}, perfectly still in the warm low light; its tiny status dot stays dark and nothing moves for the whole clip. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, glowing speaker, pulsing light, sound-wave graphics, amber slit, sparks, brand name
- **Refs:** PROP_SECURITY_SPEAKER, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** —
- **Continuity:** The speaker never glows when it speaks (file 04 §20.14): no light show. AMUN is the SESHAT voice, quieter (file 05 §9.8). The line lands about 3.5 s in, after the silence.

### 12.20.007 — KV62 antechamber, sunset — She nods and opens the notebook   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A); PROP_RAMI_NOTEBOOK
- **Action:** Nour gives the corner a small nod, one colleague to another, looks down, slips the elastic off the yellow notebook and opens it on her knee.
- **Dialogue:** —
- **Sound:** the snap of the elastic band; a page turning
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, gives a small, satisfied nod toward the corner off frame left, then looks down, slips the black elastic off {PROP_RAMI_NOTEBOOK.SHORT} and opens it on her knee. Setting: {LOC_KV62_BURIAL_2033.SHORT}, {LOC_KV62_BURIAL_2033.AREA_ANTECHAMBER}, at sunset. Lighting: {LOC_KV62_BURIAL_2033.LIGHT_SUNSET}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, legible handwriting, readable pages, smiling broadly, tears
- **Refs:** CHAR_NOUR_A_34, CHAR_NOUR_A_full, PROP_RAMI_NOTEBOOK, LOC_KV62_BURIAL_2033/ANTECHAMBER_SUNSET_plate
- **Flags:** —
- **Continuity:** The notebook's pages are COMP if the edit ever holds on them (file 04); here the pages stay soft and unreadable. The cut to black is on her eyes going to the page.

### 12.20.008 — BLACK — A single trumpet note; the lights stay on   (5 s)
- **Shot:** Full black frame · **Move:** none
- **In frame:** nothing (black); end card
- **Action:** Black. Over it a single trumpet note, a little rough, alive. The end card.
- **Dialogue:** —
- **Sound:** one trumpet note (re-recorded on the bronze trumpet), a little rough, alive; under it the faint steady electrical hum of lights that stay on
- **PROMPT:** Full black frame, locked-off: a completely dark, empty frame with no image and no light source, even and still for the whole clip. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PLATE}, any visible shape, light leak, flicker, gradient, noise pattern
- **Refs:** PROP_TRUMPET_BRONZE (sound only)
- **Flags:** COMP
- **Comp:** end card | "All modern characters and events are fictional. Imagery generated with AI." (the required closing card, bible §0; file 05 §13.7) | centred, small | 2.5 s → end | seq_12 card file
- **Continuity:** The heartbeat motif ends as the trumpet note over black (bible §11). In Seq 4.2 the note preceded the lights going out; here the lights stay on (sound: the hum continues). Pure black may be built in the edit instead of generated; the entry holds the card and the sound.
