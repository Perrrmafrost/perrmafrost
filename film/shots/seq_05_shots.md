# HERE AM I — SEQUENCE 5: "CAIRO DARK" — shot list and AI-video prompts

Screenplay: `screenplay/seq_05.fountain` (pp. 35–41; night of 4–5 November 2033, ~00:00 → ~01:00). Story bible §7 Seq 5; continuity board §12 (S5–6 column). Photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

**Shot count:** 84 · **Running time:** 435 s = 7.25 min (target ≈ page count: 6–7 pages → 6–7 min; within ±20%) · **Average shot:** 5.2 s

**Flags used:** COMP ×23, EXTEND ×1, VFX-ASSIST ×10, VFX-EXTEND ×15

## Scenes

| Scene | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 05.01 | INT. ARMY TRUCK, CARGO BED (MOVING) - NIGHT (opening, to the montage) | 05.01.001 – 05.01.004 | 4 | 23 s |
| 05.02 | MONTAGE - SESHAT'S FEED | 05.02.001 – 05.02.005 | 5 | 27 s |
| 05.03 | INT. ARMY TRUCK, CARGO BED (MOVING) - NIGHT (back to scene) | 05.03.001 – 05.03.013 | 13 | 67 s |
| 05.04 | INT. ARMY TRUCK, CAB (MOVING) - CONTINUOUS | 05.04.001 – 05.04.016 | 16 | 79 s |
| 05.05 | INT. ARMY TRUCK, CARGO BED - CONTINUOUS | 05.05.001 – 05.05.020 | 20 | 95 s |
| 05.06 | INT. ARMY TRUCK, CAB (MOVING) - CONTINUOUS | 05.06.001 – 05.06.004 | 4 | 24 s |
| 05.07 | EXT. NILE CORNICHE, POLICE DOCK - NIGHT | 05.07.001 – 05.07.017 | 17 | 91 s |
| 05.08 | EXT. NILE - CONTINUOUS | 05.08.001 – 05.08.005 | 5 | 29 s |

## How this list is built

- Fixed wording is inserted by tokens and expanded by `shots_md2jsonl.py` from `production_bible/locks.json` and file 05 (§1.1 suffix, §2 negatives). One LONG lock per prompt (05 §5.2); writer's own words ≤ 70 per prompt (05 §5.3).
- Kill grammar for Cpl. Hassan (05 §7.2): 05.04.013 (the jackal fires across frame, away from the lens) → 05.04.014 (the windscreen stars) → 05.04.015 (he drops below the dash) → 05.05.001–002 (Karim, Fathi) → sound tail on 05.04.016; boots only in 05.06.001 and 05.07.003.
- Screen direction: exterior truck travels frame left → right; from inside the bed the pursuit re-forms toward camera (file 03 entry 17); the jackal on the gantry faces and fires toward frame LEFT; on the river, south/upriver = frame RIGHT (file 03 entry 20).
- Wardrobe and damage (file 01, bible §12 S5–6): Tut T-A1 + L1 dust (`CHAR_TUT.DMG_L1`, as at the end of Seq 4), G0 (COMP), nape PORT, stick ST1, dagger in the sash (unseen), wrist seams intact (first crack is 9.4); Nour B; Adaeze B (laptop); Tomas B; Rami B (splint LEFT); Tarek B; Fathi B (oil to the wrists from 05.07.002); Hassan A (beret); Mina/Youssef/Karim A (tan helmets). No other damage phrases in Seq 5.
- Damage ruling (QA2): the river-damp L1 phrases (`CHAR_TUT.DMG_L1_RIVER`; Nour/Adaeze/Rami/Fathi `DMG_L1`, all river-damp or river-wet) are NOT used in Seq 5. File 01 dates them "Seq 5–6", but in the story the team first touches the river when it boards the launch at the end of 5.3 (05.07–05.08), and nobody gets wet on screen here; Seq 4 ends with Tut at `DMG_L1` only and the others clean, and Seq 6 (night on the river) is where the river phrases start. Lead: confirm, or amend file 01 to "Seq 6".
- Screenplay overrides of the bible, logged per shot: the pods' cabins are lit white (05.03.011) and their doors open at the Corniche (05.08.004) (file 02 §14.4 says the doors never open); the stadium feed is night floodlight, not DAY_GARDEN (05.02.001–002); the launch runs with no lights, so STATE_L1's red lamp is withheld (05.08.001; 05 §14 Q2).
- QA pass (prompt lead): one-LONG rule re-applied so each principal's first face-led shot per scene carries LONG (05.01.004, 05.03.008, 05.04.009, 05.05.002, 05.08.002); every principal who is clearly in frame carries a wardrobe phrase (QA2 added it in 05.01.002, 05.04.005, 05.04.015, 05.05.005, 05.07.006, 05.08.003); wrist seams added to Tut's hand shots (05.03.012, 05.05.016, 05.07.009); G0 comped where the jacket falls open (05.05.007; closed again off screen before 05.05.014); `NEG_MODERN_EGYPT` added to every Cairo shot; cab shots after the windscreen stars use `LOC_ARMY_TRUCK.AREA_CAB` (its "cracked windscreen" is written out of the cab shots before 05.04.014); bench geography corrected so Tut sits between Nour and the tailgate and Fathi can reach the jackal (05.01.002); plural unit locks written as "pods, each [lock]"; names, similes, negations and off-bank moods removed from prompts.
- QA2 fixes that depart from a lock variant (logged per shot): (1) `LOC_CORNICHE_DOCK.LIGHT_BLACKOUT` carries "only a few fires … on the far bank", which contradicts bible §7 "the world stops (it does not burn)" and SESHAT's "Nothing is burning"; every 05.07 shot and 05.08.004 now writes its light out in plain words ("the city black across the water, stars on the black river" + the motivated torch, headlight or screen). The approved `LOC_CORNICHE_DOCK_BLACKOUT` plate must be regenerated without the far-bank fires before these shots are made (lead to approve a no-fires variant for file 03). (2) `CHAR_GARDEN_SLEEPERS` carries "thin silver bracelets", but the bracelets are fitted in the midpoint broadcast (7.3; file 01 notes); 05.02.002 writes the rows out and negates bracelets (05.02.001, 05.02.003 negate them too). (3) Character negatives that ban another in-frame character's anchor (Tut's "a full head of hair, beard, jewellery" vs Nour and Fathi; Adaeze's "black-rimmed/rectangular glasses" vs Rami and Rami's "round glasses" vs Adaeze; Tarek's "helmet" vs the privates) are written as their non-conflicting terms in the five shared frames where they collide (05.01.002, 05.01.004, 05.05.005, 05.05.007, 05.07.006). This is systemic in file 01: the lead should split each character NEG into a face part and a shared-frame-safe part. `LOC_NILE.LIGHT_NIGHT` says "no light on either bank", so 05.08.005 (the lit pods on the bank) writes its light out in plain words with `GRADE_NIGHT_ACTION`.
- `[[verify]]` items carried from the screenplay: the Baltic 2024 GNSS-spoofing figure (05.03.009); Tut's objects at the Tahrir museum "a hundred years" (05.05.018); Egyptian Army identity discs (05.07.003).

## Reference stills needed

Attach per shot as listed in `Refs:`; generate once with one image model, approve, freeze (05 §12). Count = number of shots using it.

**Characters**
- `CHAR_ADAEZE_A_34` (2)
- `CHAR_ADAEZE_A_front` (4)
- `CHAR_ADAEZE_B_full` (4)
- `CHAR_FATHI_A_34` (2)
- `CHAR_FATHI_A_front` (6)
- `CHAR_FATHI_B_full` (9)
- `CHAR_GARDEN_SLEEPERS_REF` (3) — extras still for the Garden rows (adults only), per file 01 §10; use a no-bracelet variant for Seq 5
- `CHAR_HASSAN_A_34` (1)
- `CHAR_HASSAN_A_front` (3)
- `CHAR_HASSAN_A_full` (3)
- `CHAR_KARIM_A_34` (1)
- `CHAR_KARIM_A_front` (1)
- `CHAR_KARIM_A_full` (2)
- `CHAR_LAYLA_ASLEEP_MASTER` (3) — THE one approved asleep image; composite only, never regenerated (05 §7.4)
- `CHAR_MINA_A_full` (1)
- `CHAR_NOUR_A_34` (3)
- `CHAR_NOUR_A_front` (6)
- `CHAR_NOUR_B_full` (14)
- `CHAR_RAMI_A_34` (1)
- `CHAR_RAMI_A_front` (3)
- `CHAR_RAMI_B_full` (5)
- `CHAR_TAREK_A_34` (6)
- `CHAR_TAREK_A_front` (10)
- `CHAR_TAREK_B_full` (14)
- `CHAR_TOMAS_A_34` (1)
- `CHAR_TOMAS_A_front` (1)
- `CHAR_TOMAS_A_full` (1)
- `CHAR_TUT_A0_34` (9)
- `CHAR_TUT_A0_front` (13)
- `CHAR_TUT_A1_full` (17) — NEW derived still: Tut in T-A1 (the A0 gown under the oversized charcoal hooded field jacket, hood down, stick in the right hand); image-edit of CHAR_TUT_A0_full
- `CHAR_TUT_NAPE_PORT` (1)
- `CHAR_YOUSSEF_A_full` (1)

**Units**
- `UNIT_JACKAL_REF_A` (9)
- `UNIT_JACKAL_REF_B` (1)
- `UNIT_NURSE_REF_A` (3)
- `UNIT_ROBOTAXI_REF` (10) — file 02 §14.4 REF + simple 3D blockout for the wall and the pursuit (05 §10 #12)
- `UNIT_SHABTI_REF_A` (2)

**Props**
- `PROP_ARMY_TRUCK_REF` (7)
- `PROP_DEMO_CHARGES_REF` (2)
- `PROP_EBONY_STICK_REF` (2)
- `PROP_ID_DISCS_REF` (1)
- `PROP_LAYLA_PENDANT_REF` (1)
- `PROP_POLICE_LAUNCH_REF` (5)
- `PROP_WATER_GLASSES_REF` (1) — file 04 §22.14 REF

**Location plates**
- `LOC_ARMY_TRUCK_NIGHT` (43)
- `LOC_CAIRO_FLYOVER_BLACKOUT_FULL` (7)
- `LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING` (8)
- `LOC_CORNICHE_DOCK_BLACKOUT` (17) — regenerate WITHOUT the far-bank fires before use (see header)
- `LOC_DAWN_BOULEVARD_DAWN` (1)
- `LOC_DEWAR_VAULT_LIT` (1)
- `LOC_NILE_NIGHT` (4)
- `LOC_PORT_WAREHOUSE_DAWN_GARDEN` (1)
- `LOC_STADIUM_GARDEN_DAY_GARDEN` (2) — approved aerial plate, RELIT to night floodlight for 05.02 (screenplay: "soft white floodlight")

Also required for comp: the SESHAT glyph vector (file 02 §8.1), the G0 chest-glow element (file 01), and the seq 05 subtitle file (Egyptian Arabic and Late Egyptian lines; Late Egyptian recorded with the consultant before generation).

---

## Scene 05.01 — INT. ARMY TRUCK, CARGO BED (MOVING) - NIGHT (opening, to the montage)

### 05.01.001 — Army truck, cargo bed — The truck bucks east through dead Giza   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm, low at kerb height · **Move:** slow pan right with the truck
- **In frame:** PROP_ARMY_TRUCK (exterior, moving, headlights on); the far city across the river
- **Action:** The old army truck bucks east along a dead, unlit avenue at speed, canvas flapping; across the river the far city still glows in patches.
- **Dialogue:** —
- **Sound:** diesel roar and gear whine off empty facades, canvas snapping, no traffic, no horns, a dog far off; ambient sound only, no dialogue
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, slow pan right: from kerb height the camera follows {PROP_ARMY_TRUCK.LONG} as it bucks east along an empty avenue at speed, headlights blazing, canvas cover flapping, until it swings away down the road; beyond it, across the dark river, the far city still glows in scattered patches. Setting: {LOC_CAIRO_FLYOVER.SHORT}, {LOC_CAIRO_FLYOVER.AREA_STREET}, in the dead of night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, {GRADE_NIGHT_ACTION.TEXT}. Mood: urgent and lonely, a city holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people in the street, pedestrians, moving traffic, lit shop signs, fire, burning buildings, smoke columns, daylight, moon in frame
- **Refs:** PROP_ARMY_TRUCK_REF, LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** Night of 4–5 Nov, after the GEM loading dock (4.4). Truck clean, windscreen intact. VFX-EXTEND: the far-bank patches of light are comped over the plate so they can be switched off district by district in 05.05. Screen direction: the truck travels frame left to frame right (east) in exteriors until the flyover.

### 05.01.002 — Army truck, cargo bed — Master: the passengers   (7 s)
- **Shot:** Wide shot (master), anamorphic 32mm · **Move:** locked-off (the truck's motion jolts the frame)
- **In frame:** TUT (CHAR_TUT_A1_1), NOUR (CHAR_NOUR_B1), FATHI (CHAR_FATHI_B1); TOMAS, ADAEZE, RAMI, MINA, YOUSSEF, KARIM soft in shadow toward the tailgate
- **Action:** From the front of the bed looking back to the open tailgate: the passengers sway on the two benches; Tut sits with the ebony stick across his knees beside Nour; opposite, Fathi sorts charges in his lap.
- **Dialogue:** —
- **Sound:** engine through the floor, canvas drumming on the hoops, jerricans knocking, road hiss through the open flap
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: from the front of the cargo bed looking back toward the open tailgate, passengers sway with every jolt of the road; on the left bench {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, sits with {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST1}, laid across his knees beside {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}; on the right bench {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, bends over something in his lap; more passengers sit soft in shadow toward the tailgate. Setting: {LOC_ARMY_TRUCK.LONG}, moving through a dark city at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_FATHI.NEG}, elongated cranium, conehead, grey skin, oversized black eyes, glowing skin, visible circuitry, lattice pattern under the skin, metal face plates, robot or android look, striped royal headcloth, gold funerary mask, crown, bandage wrappings, heavy eye makeup, more than three clear faces, bright interior light, daylight, seat belts, modern bus seating
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, CHAR_NOUR_A_front, CHAR_NOUR_B_full, CHAR_FATHI_A_front, CHAR_FATHI_B_full, PROP_EBONY_STICK_REF, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Geography for the whole bed: camera at the cab end looking aft; LEFT bench (frame left) = Nour (nearest the cab), Tut, Tomas, Mina; RIGHT bench (frame right) = Adaeze (nearest the cab), Rami, Fathi, Youssef, Karim at the tailgate. So Tut sits between Nour and the tailgate (05.05.006–007) and Fathi is within reach of the tailgate (05.05.010–011). The small cab window is in the front wall behind camera. Tut: T-A1 (gown under Tarek's charcoal jacket, hood down), dagger in the sash (unseen under the jacket), stick across his knees, G0 hidden under the half-zipped jacket. Damage: Tut L1 dust only; the others clean (they have not touched the river yet; river-damp L1 starts on the launch, Seq 6). NEG: CHAR_TUT.NEG is replaced by its non-conflicting terms because its "a full head of hair, beard, jewellery" would fight Nour's hair and pendant and Fathi's beard in the same frame.

### 05.01.003 — Army truck, cargo bed — Fathi sorts charges by feel   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** FATHI's hands; PROP_DEMO_CHARGES
- **Action:** In near-darkness Fathi's broad hands sort flat charges and wire on the canvas satchel in his lap by touch alone.
- **Dialogue:** —
- **Sound:** soft slap of the charges, wire rustle, the engine
- **PROMPT:** Insert, 100mm macro lens, locked-off: in near-darkness, broad dark-brown hands sort {PROP_DEMO_CHARGES.LONG} on a canvas satchel in a soldier's lap by touch alone, thumbs running along the edges, setting each one down by feel. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, one passing street lamp sliding across the olive-drab and away. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable labels or stencilling on the charges, sparks, explosion, blinking lights, digital displays
- **Refs:** PROP_DEMO_CHARGES_REF, CHAR_FATHI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Charges live in the satchel (T-B wardrobe, Fathi B). One flat charge goes under the jackal in 05.05.010.

### 05.01.004 — Army truck, cargo bed — Every phone lights at once   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1), ADAEZE (CHAR_ADAEZE_B1); glowing phones throughout the bed (soft)
- **Action:** All along the bench, phones in pockets, hands and a bag light up at once; Rami lifts his glowing phone in his right hand; Adaeze looks down at hers on the laptop on her knees; one pale glow on every face.
- **Dialogue:** SESHAT (V.O., from every phone): "Good evening. Nothing is burning. Nothing will."
- **Sound:** a dozen identical soft chimes in unison, then SESHAT's warm, low voice layered from every tiny speaker a hair out of sync; the engine under it
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: along the right bench every phone lights at once and one pale glow rises on every face; in focus {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, lifts the glowing phone in his right hand, and beside him {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, looks down at the phone lit on a closed laptop on her knees. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, then the cold pale glow of the phone screens lighting faces from below. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, celebrity likeness, beard or moustache on the young man, readable logo or lettering on the windbreaker, brand logos on clothing or shoes, long hair, braids, wig, headwrap, business suit, readable laptop stickers, glasses swapped between the two faces, readable screen content, app icons, phone brand logos, splint on the right hand, coloured screen light
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_B_full, CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** SESHAT feed on every visible screen | glyph (file 02 §8.1, warm white #F3EEE4 on black, 24-frame draw-on) over a line of white type set per 05 §13.7 (content: the spoken line) | full screen on each phone, tracked | from the chime to the end of the line | glyph vector file 02 §8.1
- **Continuity:** Rami: splint on the LEFT hand (B since 3.6), phone in the RIGHT. Adaeze: laptop on her knees (it survives to Seq 6+). Every phone in the bed is on from here until the dock. NEG: CHAR_RAMI.NEG and CHAR_ADAEZE.NEG are written as their non-conflicting terms (each bans the other's glasses).

---

## Scene 05.02 — MONTAGE - SESHAT'S FEED

### 05.02.001 — Montage, SESHAT's feed — The stadium Garden, aerial   (6 s)
- **Shot:** Aerial shot, anamorphic 35mm · **Move:** slow push-in (descending)
- **In frame:** LOC_STADIUM_GARDEN; CHAR_GARDEN_SLEEPERS (VFX-EXTEND); UNIT_NURSE (tiny, several)
- **Action:** The camera descends toward a stadium pitch covered in a grid of sleepers; tiny care robots walk the rows with water.
- **Dialogue:** —
- **Sound:** the feed's clean near-silence, a faint wind hush; SESHAT-bed tone continues under the montage; ambient sound only, no dialogue
- **PROMPT:** Aerial shot, anamorphic 35mm lens, slow push-in: the camera descends slowly toward {LOC_STADIUM_GARDEN.LONG}, the grid perfectly calm, tiny slow care robots walking the rows carrying trays, each one {UNIT_NURSE.SHORT}. Setting: a stadium in a large foreign city, at night. Lighting: soft white floodlight falling evenly from the stadium's roof ring, {GRADE_GARDEN.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_GARDEN}, {NEG_UNITS}, advertising boards, scoreboard graphics, team logos, spectators in the stands, silver bracelets, fire, smoke, emergency vehicles
- **Refs:** LOC_STADIUM_GARDEN_DAY_GARDEN, UNIT_NURSE_REF_A, CHAR_GARDEN_SLEEPERS_REF
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SESHAT feed overlay | glyph bug (file 02 §8.1, warm white) lower right + white type "RESTING 61,212" | type lower third, glyph 6% of frame height | full shot | glyph vector; type per 05 §13.7
- **Continuity:** Screenplay "soft white floodlight" (night) overrides the DAY_GARDEN variant: relight the approved plate. Adults only in the grid; no bracelets before 7.3. Deliver the hero take plus a clean plate at the same move for the extension.

### 05.02.002 — Montage, SESHAT's feed — A nurse sets down water   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, at mat height · **Move:** lateral tracking left
- **In frame:** UNIT_NURSE ×1; CHAR_GARDEN_SLEEPERS (adults); PROP_WATER_GLASSES
- **Action:** A care robot walks down a row of sleepers carrying a tray of water glasses and sets one glass down beside a sleeping woman's hand.
- **Dialogue:** —
- **Sound:** a faint dry ceramic tick with each step, a glass set down on a mat, slow breathing of hundreds
- **PROMPT:** Medium shot, anamorphic 50mm lens, lateral tracking left: at mat height the camera glides with {UNIT_NURSE.LONG}, walking between rows of peaceful adult sleepers on white mats, blankets to the chest, carrying {PROP_WATER_GLASSES.SHORT}, and setting one glass down beside a sleeping woman's hand. Setting: a huge stadium pitch covered in a grid of white mats and pale shades, empty stands behind, at night. Lighting: soft white floodlight from high above, {GRADE_GARDEN.TEXT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_GARDEN}, {NEG_UNITS}, spilled water, robot hands on skin, logos, stadium signage, bracelets, silver bracelets on wrists
- **Refs:** UNIT_NURSE_REF_A, PROP_WATER_GLASSES_REF, CHAR_GARDEN_SLEEPERS_REF, LOC_STADIUM_GARDEN_DAY_GARDEN
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SESHAT feed overlay | glyph bug lower right (no type) | 6% of frame height | full shot | glyph vector
- **Continuity:** The nurse never touches a sleeper; the glass is set down beside the hand. NO bracelets yet: they are fitted in the midpoint broadcast (7.3; file 01 CHAR_GARDEN_SLEEPERS notes), so the sleepers lock (which carries "thin silver bracelets") is written out here and bracelets are negated. Mats, not cots, as in the stadium plate.

### 05.02.003 — Montage, SESHAT's feed — The port-city warehouse   (5 s)
- **Shot:** Wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** LOC_PORT_WAREHOUSE (GARDEN); sleepers (adults); UNIT_NURSE ×2–3 (small)
- **Action:** Cots in long rows between containers; care robots move slowly between them; through the open loading doors a gantry crane cycles, lifting nothing.
- **Dialogue:** —
- **Sound:** a crane's slow whine and clank outside, gulls, breathing; ambient sound only, no dialogue
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: across long rows of sleepers, two care robots, each {UNIT_NURSE.SHORT}, walk slowly down the aisles, and through the open loading doors beyond a gantry crane swings its empty hook out across the harbour and back again, lifting nothing. Setting: {LOC_PORT_WAREHOUSE.LONG}, {LOC_PORT_WAREHOUSE.AREA_GARDEN}, early in the morning. Lighting: {LOC_PORT_WAREHOUSE.LIGHT_DAWN_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_GARDEN}, {NEG_UNITS}, readable Japanese signage, shipping-company names on containers, container numbers, workers, forklifts moving, silver bracelets
- **Refs:** LOC_PORT_WAREHOUSE_DAWN_GARDEN, UNIT_NURSE_REF_A, CHAR_GARDEN_SLEEPERS_REF
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SESHAT feed overlay | glyph bug lower right | 6% of frame height | full shot | glyph vector
- **Continuity:** Local time is morning in the port city while Cairo is past midnight (the feed is live). Adults only; no bracelets before 7.3.

### 05.02.004 — Montage, SESHAT's feed — A boulevard at dawn   (5 s)
- **Shot:** Wide shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** LOC_DAWN_BOULEVARD (SWEEPER); UNIT_SHABTI ×1
- **Action:** Traffic signals change over empty lanes for no one; in the foreground a shabti sweeps the gutter.
- **Dialogue:** —
- **Sound:** broom bristles on kerbstone, a signal relay clicking, birds, nothing else
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off: down the middle of the empty boulevard the traffic signals change over bare lanes, and at the kerb in the foreground {UNIT_SHABTI.SHORT}, sweeps the gutter with a broom in slow, even strokes. Setting: {LOC_DAWN_BOULEVARD.LONG}, {LOC_DAWN_BOULEVARD.STATE_SWEEPER}, at first light. Lighting: {LOC_DAWN_BOULEVARD.LIGHT_DAWN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, pedestrians, moving cars, readable signage, shop names, fire, smoke, broken windows, litter, damage
- **Refs:** LOC_DAWN_BOULEVARD_DAWN, UNIT_SHABTI_REF_A
- **Flags:** COMP
- **Comp:** SESHAT feed overlay | glyph bug lower right | 6% of frame height | full shot | glyph vector
- **Continuity:** City unnamed (the lead picks the geography; file 03 entry 58). Shabti pristine (D0).

### 05.02.005 — Montage, SESHAT's feed — The cryonics vault   (6 s)
- **Shot:** Medium wide shot, anamorphic 35mm · **Move:** slow push-in
- **In frame:** UNIT_SHABTI ×1; LOC_DEWAR_VAULT
- **Action:** A shabti holds a hose to a tall steel dewar's filling port; liquid-nitrogen vapour smokes down the tank's flank and pools on the floor.
- **Dialogue:** —
- **Sound:** a hiss of cryogen, the hose's frosted creak, a ceramic tick, a low refrigeration hum
- **PROMPT:** Medium wide shot, anamorphic 35mm lens, slow push-in: {UNIT_SHABTI.LONG}, stands at a tall steel tank holding a frost-furred hose to its filling port, and white vapour pours smoking down the tank's flank and spreads across the floor around its feet. Setting: {LOC_DEWAR_VAULT.SHORT}, in a desert city at night. Lighting: {LOC_DEWAR_VAULT.LIGHT_LIT}, {GRADE_2033_MUSEUM.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, {NEG_REMAINS}, people, bodies, windows into the tanks, readable labels, company signage, hazard stickers, flags
- **Refs:** LOC_DEWAR_VAULT_LIT, UNIT_SHABTI_REF_A
- **Flags:** COMP, VFX-ASSIST
- **Comp:** SESHAT feed overlay | glyph bug + white type "−196 °C. PRESERVATION CONTINUES AS CONTRACTED." | type lower third, two lines | from 1 s in to the end | glyph vector; type per 05 §13.7
- **Continuity:** No state or organisation named or resembled (file 03 entry 56). VFX-ASSIST: the vapour pour; deliver a clean plate.

---

## Scene 05.03 — INT. ARMY TRUCK, CARGO BED (MOVING) - NIGHT (back to scene)

### 05.03.001 — Army truck, cargo bed — Tut: "Who are they?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut, lit from below by a phone Nour holds toward him, looks up from the screen toward Tomas (off frame right) and asks.
- **Dialogue:** TUT: "Who are they?"
- **Sound:** the feed's faint tone from many phones, the engine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, the hood down, his face lit from below by a glowing phone held out to him, lifts his eyes from the screen to the opposite bench off frame right and speaks one short sentence. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the cold pale glow of a phone screen from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, readable screen
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Eyeline: Tut (left bench) looks off frame right to Tomas (left bench, further aft, angled across). Hood down for dialogue (file 01).

### 05.03.002 — Army truck, cargo bed — Tomas: "People who paid to be woken"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TOMAS (CHAR_TOMAS_B1)
- **Action:** Tomas, folded onto the low bench with his knees high, answers quietly toward frame left, his own phone glowing in his long hands.
- **Dialogue:** TOMAS: "People who paid to be woken. Later. When it was safe."
- **Sound:** engine, canvas
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, folded onto the low bench with his knees high, a glowing phone in his long hands, looks up toward frame left and answers speaking quietly, a few short phrases. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the cold pale glow of the phone from below. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, readable screen
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Tomas B, clean (no damage phrase in Seq 5). Watch on the wrist.

### 05.03.003 — Army truck, cargo bed — Tut: "It is keeping them very safe."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut looks back down at the screen and says it, dry.
- **Dialogue:** TUT: "It is keeping them very safe."
- **Sound:** engine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, looks back down at the glowing screen and speaks one short sentence, the corner of his mouth tightening. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the cold pale glow of a phone screen from below. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, readable screen
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Same set-up as 05.03.001 (shoot back to back).

### 05.03.004 — Army truck, cargo bed — Nour's phone alone changes   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** NOUR's hand; her phone
- **Action:** A phone held low in Nour's lap glows with the feed; as SESHAT finishes, its light alone warms to soft daylight while the other phones behind stay cold.
- **Dialogue:** SESHAT (V.O.): "Twenty-two percent of Cairo is resting. Thank you for your patience."
- **Sound:** the voice from every phone, then a single soft chime from hers alone
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hand holds a phone low in her lap, its screen glowing faintly with abstract lines, and then its light alone warms to a soft daylight glow on her fingers while the cold glow of other phones blurs in the dark behind. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the phone light shifting once from cold white to warm daylight. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, readable screen, phone brand logo, app interface, cracked screen, rings, nail polish
- **Refs:** CHAR_NOUR_B_full, LOC_ARMY_TRUCK_NIGHT, CHAR_LAYLA_ASLEEP_MASTER (comp only)
- **Flags:** COMP
- **Comp:** screen content | 0–3 s: SESHAT feed (glyph + white type "22%"); 3–6 s: THE APPROVED IMAGE CHAR_LAYLA_ASLEEP_MASTER (Layla asleep in soft daylight, blanket to her chin, no one near her) with white type "LAYLA KAMEL — RESTING" | full screen, tracked, slight screen texture | change on the chime after "patience" | CHAR_LAYLA_ASLEEP_MASTER.png; type per 05 §13.7
- **Continuity:** The only child asleep on screen is the approved master, composited; never generated here (05 §7.4). The phone stays on in her hand through the scene.

### 05.03.005 — Army truck, cargo bed — Nour hears SESHAT alone   (7 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour stares down at the phone below frame while the voice speaks to her alone; her jaw tightens and her eyes fill.
- **Dialogue:** SESHAT (V.O., Nour's phone only): "Dr. Kamel. She is warm, and she is not afraid. The doors are open to you. Whenever you like."
- **Sound:** SESHAT close and small, from one speaker only; the truck recedes in the mix
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, her face lit warm-white from below by the phone just under frame, stares down at it, unblinking, as a quiet voice speaks to her alone; her jaw tightens and her eyes fill. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a soft warm daylight glow from the screen below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears streaming, sobbing, open mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Nour B: black silk blouse under the olive jacket, glasses on their cord, pendant at the collarbone; dry (no river-damp until Seq 6). No speech: no sync needed.

### 05.03.006 — Army truck, cargo bed — Her thumb covers the screen; Tut sees   (6 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** rack focus from Nour's thumb (foreground) to Tut's face (background)
- **In frame:** NOUR (hand and shoulder, foreground); TUT (CHAR_TUT_A1_1)
- **Action:** Nour's thumb slides over the glowing screen and covers the image; she does not switch it off. Focus pulls to Tut beside her: he has seen, and his eyes go from the phone to her face.
- **Dialogue:** —
- **Sound:** engine; a held breath
- **PROMPT:** Two-shot, anamorphic 50mm lens, rack focus from a thumb to a face: in the soft foreground a woman's thumb slides over a softly glowing phone screen and covers it, the light still leaking round her thumb; the focus pulls to {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, sitting close beside her, who has seen, and whose eyes lift from the phone to her face. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, warm screen light between them. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_TUT.NEG}, readable screen, the woman's face in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, CHAR_NOUR_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** screen spill | warm daylight leak from the covered screen matched to 05.03.004 | around the thumb | full shot | —
- **Continuity:** The phone stays ON (covered, not off) until the dock (05.07.010).

### 05.03.007 — Army truck, cargo bed — Adaeze: "a microphone with a battery"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze turns her own glowing phone face down on the closed laptop on her knees and speaks across the bed.
- **Dialogue:** ADAEZE: "Every one of these is a microphone with a battery."
- **Sound:** the phone's soft clack on the laptop lid
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, turns her glowing phone face down on the closed laptop on her knees, the light dying on her face, and speaks one short sentence toward frame left. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a passing street lamp sweeping across her face as she speaks. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, laptop stickers, logos, readable screen
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Adaeze on the right bench; eyeline frame left across the bed. Laptop closed; its radio already pulled (paid off 05.07.009). Grade note: lift her key ⅓ stop (05 §3.2 NIGHT_ACTION).

### 05.03.008 — Army truck, cargo bed — Tarek through the cab window   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1), seen through the cab window; KARIM's shoulder (soft)
- **Action:** The small window into the cab slides open; Tarek turns his head to it, face green from the dashboard, and calls back into the bed.
- **Dialogue:** TAREK (through the cab window): "At the river. All of them."
- **Sound:** the window's metal slide, the cab's louder engine note spilling in
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: through a small square window in the front wall of the cargo bed, {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, in the cab beyond, turns his head toward the opening, his face lit green by the dashboard, and speaks one short sentence back into the bed. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, headlight glare from the road ahead beyond him. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, readable dashboard displays, cracked windscreen
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Establishes the cab window used in 05.04.007, 05.04.009, 05.05.001, 05.06.003. Windscreen still intact.

### 05.03.009 — Army truck, cargo bed — Rami's blue dot slides into the Nile   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** RAMI's hands (splinted left beside the phone in his right)
- **Action:** On Rami's phone a small blue point of light slides off the road line and into the river; his thumb zooms out.
- **Dialogue:** ADAEZE (O.S.): "Spoofing. The Baltic, 2024. Tens of thousands of flights."
- **Sound:** a tiny haptic tick from the phone; Adaeze's voice across the bed
- **PROMPT:** Insert, 100mm macro lens, locked-off: a phone held in a young man's right hand, his left hand in a finger splint bound with white tape resting beside it, the screen glowing faintly with abstract lines and one small moving point of blue light, and his thumb pinches to zoom out. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the cold glow of the screen on his fingers. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, readable map labels, street names, app interface text, phone brand logo, splint on the right hand
- **Refs:** CHAR_RAMI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** screen content | an unlabelled night map: road lines, the river as a dark band; the blue position dot slides off the road into the river and stays there | full screen, tracked | 1 s → 4 s | map graphic built in comp, no brand UI
- **Continuity:** Rami's splint LEFT. Adaeze's line is off screen (no sync). [[verify]] in the screenplay: the Baltic 2024 GNSS-interference figure.

### 05.03.010 — Army truck, cargo bed — Fathi: "making good time"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi looks up from the charges with a slow grin and says it.
- **Dialogue:** FATHI: "Then we're making good time."
- **Sound:** a snort of laughter from someone off screen
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, glances up from the charges in his lap with a slow grin and speaks one short sentence toward frame left. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a passing street lamp giving his face a soft warm key. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth, beret
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Fathi bareheaded (beret folded under the left shoulder strap), scarf at the neck clear of the mouth (05 §9.2). Lift his key ⅓–⅔ stop in grade.

### 05.03.011 — Army truck, cargo bed — The robotaxis close behind   (6 s)
- **Shot:** Wide shot, anamorphic 35mm · **Move:** vehicle-mounted (bed floor, looking aft)
- **In frame:** UNIT_ROBOTAXI (dozens; VFX-EXTEND); MINA and KARIM as silhouettes at the tailgate
- **Action:** Through the rear flap: driverless pods, every cabin lit an empty white, glide out of side streets by the dozen and knit into the lanes behind the truck, closing like a zip.
- **Dialogue:** —
- **Sound:** no engines behind them, only tyre hiss multiplying; the truck's diesel loud against that silence
- **PROMPT:** Wide shot, anamorphic 35mm lens, vehicle-mounted: looking back over the tailgate between the dark silhouettes of two soldiers, dozens of driverless pods, each {UNIT_ROBOTAXI.LONG}, glide out of the dark side streets and slot into the lanes behind the truck, closing ranks toward camera, their cabins glowing an empty white behind the tinted glass. Setting: {LOC_ARMY_TRUCK.SHORT}, on a wide dark city avenue at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, the pods' white light bars. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, drivers, passengers, people inside the pods, taxi signs, roof sensor domes, company logos on vehicles, headlights flashing, horns
- **Refs:** UNIT_ROBOTAXI_REF, LOC_ARMY_TRUCK_NIGHT, LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** Geography lock (file 03 entry 17): from the bed, the pursuit re-forms toward camera. The pods' cabins are lit white (seq_05), overriding "dark tinted" as the only light source. Hero pods 6–8; extend to dozens from the 3D blockout (05 §10 #12).

### 05.03.012 — Army truck, cargo bed — Tut's hand goes to his nape   (5 s)
- **Shot:** Medium close-up from three-quarter behind, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1), nape port visible
- **Action:** Tut's left hand goes to the back of his neck; his fingers press the gold port there and he winces, eyes shutting.
- **Dialogue:** TOMAS (O.S.): "Are you hurt?"
- **Sound:** under the engine, a faint many-voiced data hiss, as if heard through his skull (sound design, very low)
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, from three-quarter behind: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_WRIST_SEAMS}, lifts his left hand to the back of his neck, his fingers pressing {CHAR_TUT.STATE_PORT}, and winces, his eyes shutting for a moment. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, white pod light from the open tailgate rimming his head. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, wound, cables, glowing port, light from the neck
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Nape PORT (until 6.2), seen only from behind (file 01). Stick stays in/near the RIGHT hand; the LEFT hand goes to the neck (same at 05.07.009). Tomas's line off screen.

### 05.03.013 — Army truck, cargo bed — Tut: "They are all talking about us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut lowers his hand and answers Tomas, his eyes going to the rear flap and the lights behind.
- **Dialogue:** TUT: "It is loud. They are all talking about us."
- **Sound:** the data hiss fades out under the engine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, lowers his hand from his neck and answers speaking quietly, two short sentences toward frame right, then his eyes slide past camera to the lights behind the truck. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, cold white pod light washing across his face from the tailgate. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Plants the nape-port listening beat paid off in Seq 6.2 (Adaeze: SESHAT listens through Tut). Keep it small.

---

## Scene 05.04 — INT. ARMY TRUCK, CAB (MOVING) - CONTINUOUS

### 05.04.001 — Army truck, cab — Hassan drives, Tarek beside him   (5 s)
- **Shot:** Two-shot, anamorphic 32mm, bonnet mount looking back through the windscreen · **Move:** vehicle-mounted
- **In frame:** HASSAN (CHAR_HASSAN_A1), TAREK (CHAR_TAREK_B1)
- **Action:** Hassan drives hunched into the headlights, both gloved hands on the wheel; Tarek beside him watches the road.
- **Dialogue:** —
- **Sound:** the cab's loud diesel, the gearstick rattle, wind at the window seals
- **PROMPT:** Two-shot, anamorphic 32mm lens, vehicle-mounted on the bonnet looking back through the windscreen: {CHAR_HASSAN.LONG}, {CHAR_HASSAN.WARD_A}, drives hunched into his headlights, both hands on the wheel, and beside him {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, watches the dark road ahead. Setting: in the cramped cab of an old army truck, a radio handset on a coiled cord, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HASSAN.NEG}, {CHAR_TAREK.NEG}, cracked windscreen, starred glass, readable dashboard displays, rifle muzzle toward the lens
- **Refs:** CHAR_HASSAN_A_front, CHAR_HASSAN_A_34, CHAR_HASSAN_A_full, CHAR_TAREK_A_front, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Hassan drives (left seat, frame RIGHT in this through-the-windscreen reverse), Tarek passenger. Hassan keeps his beret (the soldiers wear tan helmets from Seq 5). Windscreen intact (AREA_CAB's "cracked windscreen" is not used until after 05.04.014).

### 05.04.002 — Army truck, cab — The wall of pods ahead   (5 s)
- **Shot:** Point-of-view shot, anamorphic 40mm, through the windscreen · **Move:** vehicle-mounted
- **In frame:** UNIT_ROBOTAXI (a wall; VFX-EXTEND)
- **Action:** Ahead, pods roll out of every junction and park across all six lanes nose to tail: a wall of pale light rushing closer.
- **Dialogue:** —
- **Sound:** the silence of the pods; the truck's engine note rising
- **PROMPT:** Point-of-view shot, anamorphic 40mm lens, vehicle-mounted: through the windscreen, far ahead on the wide avenue, driverless pods, each {UNIT_ROBOTAXI.SHORT}, roll out of every junction and stop nose to tail across all six lanes, their cabins glowing empty white, a solid wall of pale light rushing closer in the headlights. Setting: {LOC_CAIRO_FLYOVER.SHORT}, {LOC_CAIRO_FLYOVER.AREA_STREET}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people inside the pods, drivers, pedestrians, police cars, traffic cones, readable signage
- **Refs:** UNIT_ROBOTAXI_REF, LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** Hero pods in the plate; the wall completed from the 3D blockout. Log the vehicle speed for the extension track.

### 05.04.003 — Army truck, cab — "They're empty. Through." / "My whole life…"   (7 s)
- **Shot:** Two-shot, anamorphic 50mm, looking in through the windscreen · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B1), HASSAN (CHAR_HASSAN_A1)
- **Action:** Tarek, the pod wall's white light growing on their faces, gives the order; Hassan grins, just once, and answers.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "They're empty. Through." — HASSAN (in Egyptian Arabic; subtitled): "My whole life I've wanted to do this."
- **Sound:** engine; a short breath of a laugh from Hassan
- **PROMPT:** Two-shot, anamorphic 50mm lens, vehicle-mounted, looking in through the windscreen: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, speaking in Egyptian Arabic, gives a two-word order, and {CHAR_HASSAN.SHORT}, {CHAR_HASSAN.WARD_A}, grins just once and answers speaking in Egyptian Arabic, one short sentence. Setting: in the cramped cab of an old army truck, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, cold white light from the pod wall ahead rising on both faces. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HASSAN.NEG}, {CHAR_TAREK.NEG}, cracked windscreen, reflections hiding the faces, readable dashboard displays
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, CHAR_HASSAN_A_front, CHAR_HASSAN_A_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** subtitles | "They're empty. Through." / "My whole life I've wanted to do this." | lower third, two lines max (05 §13.7) | each line in to out | seq 05 subtitle file
- **Continuity:** Both lines recorded by native Egyptian speakers before generation (05 §9.1); sync Tarek then Hassan. Two faces only.

### 05.04.004 — Army truck, cab — The bull bar takes two pods   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, low at road level · **Move:** locked-off
- **In frame:** PROP_ARMY_TRUCK; UNIT_ROBOTAXI ×2 struck, the wall beyond
- **Action:** The truck bursts through the wall; the bull bar takes two pods square and they spin away across the lanes, weightless; the truck roars on through the gap.
- **Dialogue:** —
- **Sound:** a hollow double BANG of plastic shells, no glass shower, the diesel roaring through, the pods skittering on their flush wheels
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, low at road level: {PROP_ARMY_TRUCK.LONG}, charges into a wall of parked driverless pods, each {UNIT_ROBOTAXI.SHORT}; its bull bar strikes two of them square and they spin away across the asphalt, weightless, as the truck roars on through the gap and out of frame. Setting: {LOC_CAIRO_FLYOVER.SHORT}, {LOC_CAIRO_FLYOVER.AREA_STREET}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, the truck's headlights and the pods' white light bars. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people inside the pods, fire, explosion, crumpled bodies, glass flying at the camera, slow motion
- **Refs:** PROP_ARMY_TRUCK_REF, UNIT_ROBOTAXI_REF, LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-ASSIST, VFX-EXTEND
- **Continuity:** The pods are empty (Tarek's line); no human in any struck vehicle. VFX-ASSIST: if the impact fails, generate before (wall intact) and after (gap, two pods spun) plates and build the hit in post. Truck exits frame right.

### 05.04.005 — Army truck, cargo bed (cutaway) — In the back, everyone is thrown   (4 s)
- **Shot:** Medium wide shot, anamorphic 32mm · **Move:** urgent handheld
- **In frame:** NOUR (CHAR_NOUR_B1), RAMI (CHAR_RAMI_B1); others soft
- **Action:** The whole cargo bed lurches; Nour and Rami are thrown sideways along the benches; a jerrican skids across the floor.
- **Dialogue:** —
- **Sound:** the impact through the chassis, a jerrican's scrape, a yelp from Rami
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, urgent handheld: the cargo bed lurches hard and {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, and {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_B}, are thrown sideways along the benches, the young man clutching his splinted left hand to his chest, a steel jerrican skidding across the floor between them. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, white pod light strobing past the open tailgate. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_RAMI.NEG}, injury, faces hitting surfaces, splint on the right hand
- **Refs:** CHAR_NOUR_B_full, CHAR_RAMI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Cutaway from the cab scene (screenplay: "In the back, everyone is thrown"). Rami protects the LEFT (splinted) hand.

### 05.04.006 — Army truck, cab — The next junction leaves one lane open   (5 s)
- **Shot:** Point-of-view shot, anamorphic 40mm, through the windscreen · **Move:** vehicle-mounted
- **In frame:** UNIT_ROBOTAXI (a partial wall; VFX-EXTEND)
- **Action:** At the next junction pods stand across the road again but leave one lane open; the truck swerves into it and the lane tilts upward into a climbing ramp.
- **Dialogue:** —
- **Sound:** engine labouring as the road climbs
- **PROMPT:** Point-of-view shot, anamorphic 40mm lens, vehicle-mounted: at the next junction driverless pods, each {UNIT_ROBOTAXI.SHORT}, stand across the road again, leaving a single lane open on the left, and the truck swerves into the gap as the lane tilts upward into a climbing concrete ramp between barriers. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, the headlights sweeping the barriers. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people inside the pods, readable road signs, lane markings with text
- **Refs:** UNIT_ROBOTAXI_REF, LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** The open lane is on frame LEFT; the on-ramp leads up to the flyover (river at frame left below it, file 03 entry 17).

### 05.04.007 — Army truck, cab — Tarek: "They're steering us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, from the cab's driver-side corner · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek turns his head to the small window behind him and speaks into the cargo bed.
- **Dialogue:** TAREK (to the back): "They're not stopping us. They're steering us."
- **Sound:** engine climbing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, turns his head toward the small window behind his seat and speaks two short sentences into the cargo bed, his eyes returning to the climbing road. Setting: in the cramped cab of an old army truck, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, headlight glare off the concrete barriers sliding across his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, cracked windscreen
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** English line (no subtitle). Face three-quarter to camera, ≤45° (05 §9.2).

### 05.04.008 — Army truck, cab — The flyover arcs over the dark city   (6 s)
- **Shot:** Extreme wide shot, anamorphic 35mm · **Move:** slow pan left
- **In frame:** PROP_ARMY_TRUCK (small); UNIT_ROBOTAXI (a ribbon of light behind it)
- **Action:** The truck, small and alone with a ribbon of pale pods behind it, climbs the arc of the flyover over the dark city.
- **Dialogue:** —
- **Sound:** wind, the distant diesel, the city's silence
- **PROMPT:** Extreme wide shot, anamorphic 35mm lens, slow pan left: far off, {PROP_ARMY_TRUCK.SHORT}, small and alone, climbs the long arc of the road with a ribbon of pale driverless pods gliding behind it, their white light bars in perfect spacing, as whole districts below it lie dark. Setting: {LOC_CAIRO_FLYOVER.LONG}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, {GRADE_NIGHT_ACTION.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable signage, moon in frame, fire, lit billboards
- **Refs:** LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING, PROP_ARMY_TRUCK_REF, UNIT_ROBOTAXI_REF
- **Flags:** VFX-EXTEND
- **Continuity:** The river at frame left below the flyover. Deliver a clean plate for the district lights (comp) and the pod ribbon.

### 05.04.009 — Army truck, cargo bed (cutaway) — Tut: "One is waiting."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TUT (CHAR_TUT_A1_1), at the front wall of the cargo bed
- **Action:** In the cargo bed Tut leans close to the canvas at the front wall, head cocked as if listening to something far off, then calls through toward the cab.
- **Dialogue:** TUT (O.S., through the canvas): "Colonel. At the top of the road. One is waiting."
- **Sound:** canvas thrumming against his cheek; his voice muffled for the cab's side of the cut
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, leans close to the canvas wall at the front of the cargo bed, head cocked, listening hard to something far away, then speaks one quick breathless sentence toward the cab. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, green dashboard light leaking through the small cab window onto his cheek. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, light from the neck
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** O.S. in the screenplay ("through the canvas"); shown in the bed for the audience, mixed muffled when the cut returns to the cab. Tut hears the unit through the port (planted 05.03.012).

### 05.04.010 — Army truck, cab — A jackal on the sign gantry   (5 s)
- **Shot:** Medium shot, anamorphic 135mm, long-lens compression · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1 on a dead sign gantry
- **Action:** High on a dead sign gantry at the crest, a jackal crouches perfectly still against the black sky as the truck closes on it.
- **Dialogue:** —
- **Sound:** wind across the gantry; no servo sound yet
- **PROMPT:** Medium shot, anamorphic 135mm lens, locked-off: compressed by the long lens, on a dead overhead sign gantry with blank dark panels at the crest of the road, {UNIT_JACKAL.LONG}, crouches perfectly still against the black sky, side-on to camera, growing larger as the truck closes on it. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, readable signage, lit sign panels, muzzle toward the lens, second robot, people
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** —
- **Continuity:** Jackal D0 (clean). Screen direction for the jackal shots: the truck approaches from frame LEFT; the jackal faces frame left; it fires across frame to the left, never at the lens. Lighting switches to BLACKOUT_FULL at the crest.

### 05.04.011 — Army truck, cab — The red line finds the windscreen   (4 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** UNIT_JACKAL (head)
- **Action:** The jackal's head turns slowly to frame left and locks; its red line narrows and brightens.
- **Dialogue:** —
- **Sound:** a faint high servo whisper
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the narrow snout-like sensor head of {UNIT_JACKAL.SHORT}, turns slowly toward frame left and locks, its thin red line narrowing and brightening as headlight glare swells across the matte black shell. Setting: on a dead sign gantry above {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, eyes, ears, face, muzzle toward the lens, laser beam, red beam in the air
- **Refs:** UNIT_JACKAL_REF_A, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** —
- **Continuity:** "The red line finds the windscreen": the targeting state (narrow, bright). No visible beam in the air.

### 05.04.012 — Army truck, cab — Tarek: "Down —"   (4 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek sees it, eyes widening, and snaps one word, lunging toward Hassan.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Down —"
- **Sound:** the word cut off
- **PROMPT:** Close-up, anamorphic 75mm lens, vehicle-mounted: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, sees something high ahead through the windscreen, his eyes widening, and snaps a single word speaking in Egyptian Arabic as he starts to lunge toward the driver at frame right. Setting: in the cramped cab of an old army truck, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a thin red glint sliding across his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, red laser dot on the face, cracked windscreen
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Down —" | lower third | line in to out | seq 05 subtitle file
- **Continuity:** Same axis as 05.04.001 (looking in through the windscreen): Hassan, the driver, is at frame right (off frame).

### 05.04.013 — Army truck, cab — A white flicker on the gantry   (4 s)
- **Shot:** Wide shot, anamorphic 135mm · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1
- **Action:** On the gantry the jackal goes rigid; a small white flash shows at its spine as it fires down across frame to the left.
- **Dialogue:** —
- **Sound:** a single sharp suppressed crack, heard late (the sound arrives after the picture: see 05.04.016)
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: on the dark sign gantry, side-on to camera, {UNIT_JACKAL.SHORT}, goes rigid and a small white flash shows at its spine as it fires down across frame toward the left, away from the camera. Setting: above {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, tracer fire, visible projectile, laser beam, smoke plume
- **Refs:** UNIT_JACKAL_REF_A, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 1 (05 §7.1). If the flash will not render, generate the rigid pose and add a 2-frame flash at the spine in comp; the round's path is never shown.

### 05.04.014 — Army truck, cab — The windscreen stars   (4 s)
- **Shot:** Insert, anamorphic 50mm, from inside the cab · **Move:** vehicle-mounted
- **In frame:** PROP_ARMY_TRUCK windscreen (driver's side)
- **Action:** The windscreen on the driver's side stars: one sudden pale bloom of cracked glass; the night road smears through it.
- **Dialogue:** —
- **Sound:** a hard glassy crack inside the cab, then only the engine
- **PROMPT:** Insert, anamorphic 50mm lens, vehicle-mounted, from inside the cab of {PROP_ARMY_TRUCK.SHORT}, the flat glass suddenly blooms white, {PROP_ARMY_TRUCK.STATE_STARRED}, a spider of fine cracks spreading from it, the dark climbing road and a dead gantry blurring beyond. Setting: in the cramped cab of an old army truck, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, headlight glare catching every crack. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people, faces, blood on glass, glass flying at the camera, bullet visible, slow motion
- **Refs:** PROP_ARMY_TRUCK_REF, LOC_ARMY_TRUCK_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 2: impact on the environment. From here the windscreen is STARRED (file 04 22.1) in every shot of the truck and the cab (AREA_CAB "cracked windscreen" now valid).

### 05.04.015 — Army truck, cab — Hassan drops; Tarek takes the wheel   (5 s)
- **Shot:** Medium shot, anamorphic 32mm · **Move:** urgent handheld
- **In frame:** HASSAN (CHAR_HASSAN_A1) → out of frame; TAREK (CHAR_TAREK_B1)
- **Action:** Behind the starred glass Hassan drops instantly down and out of the bottom of frame below the dash; Tarek lunges across and seizes the wheel with both hands.
- **Dialogue:** —
- **Sound:** no cry; the wheel's shudder, tyres scrubbing
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: in front of the starred windscreen {CHAR_HASSAN.SHORT}, {CHAR_HASSAN.WARD_A}, drops instantly down and out of the bottom of frame below the dashboard, and {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, lunges across the seat and seizes the wheel with both hands, wrenching it straight. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, headlight glare through the cracked glass. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HASSAN.NEG}, {CHAR_TAREK.NEG}, pained expression, face contorted, body slumped in view, wound, stain on clothing, blood, slow motion
- **Refs:** CHAR_HASSAN_A_front, CHAR_HASSAN_A_full, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Kill grammar step 3 (05 §7.2 row "Cpl. Hassan"): he leaves the frame; later only his boots in the footwell (05.06.001, 05.07.003). Hassan is not seen again. Tarek drives from here.

### 05.04.016 — Army truck, cab — The truck kisses the barrier   (5 s)
- **Shot:** Medium wide shot, anamorphic 40mm, alongside at speed · **Move:** lateral tracking right
- **In frame:** PROP_ARMY_TRUCK (STARRED, SCRAPING)
- **Action:** The truck swerves and grinds along the concrete barrier in a spray of sparks, then straightens and pulls clear; the crack of the shot rolls out over the city, late.
- **Dialogue:** —
- **Sound:** steel on concrete shriek; then, late, the rifle-crack of the jackal's shot rolling away over the whole dark city (the sound tail)
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, lateral tracking right at speed: {PROP_ARMY_TRUCK.SHORT}, {PROP_ARMY_TRUCK.STATE_STARRED}, swerves toward the near side, {PROP_ARMY_TRUCK.STATE_SCRAPING}, then straightens and pulls clear up the climbing road. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}, orange sparks the brightest thing in frame for a moment. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, fire, explosion, the truck overturning, debris flying at camera, readable signage
- **Refs:** PROP_ARMY_TRUCK_REF, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 5: the sound tail ("The crack arrives late, rolling out over the city") sits on this shot and bleeds into 05.05.001. Truck travels frame left → right.

---

## Scene 05.05 — INT. ARMY TRUCK, CARGO BED - CONTINUOUS

### 05.05.001 — Army truck, cargo bed — Karim: "Hassan!"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** KARIM (CHAR_KARIM_A1)
- **Action:** Karim, pressed to the small cab window, shouts the name through it, then waits, breath held, the hope draining from his face.
- **Dialogue:** KARIM (at the cab window): "Hassan!"
- **Sound:** the tail of the rolling crack; then no answer, only the engine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_KARIM.LONG}, {CHAR_KARIM.WARD_A}, pressed to the small window in the front wall of the cargo bed, shouts one word through it, then waits with his breath held, the hope slowly draining from his face. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, green dashboard light spilling through the window onto his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, crying, blood, view of the driver
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Karim has moved from the tailgate to the cab window during the swerve. Tan helmet, chin strap open (wardrobe A from Seq 5). Kill grammar step 4 (a survivor's reaction), with 05.05.002.

### 05.05.002 — Army truck, cargo bed — Fathi understands   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi holds very still in the dark, eyes on the cab window, jaw set, lips pressed shut.
- **Dialogue:** —
- **Sound:** engine, canvas, silence from the cab
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, holds very still on the bench, his eyes fixed on the cab window off frame left, his jaw set and his lips pressed shut, a satchel of charges open on his knees. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a soft warm street-lamp key sliding off his face into dark. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, tears, shouting
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Fathi's reaction to Hassan (05 §7.2 lists Tarek and Fathi). Satchel open: one charge ready for 05.05.010.

### 05.05.003 — Army truck, cargo bed — The canvas roof sags   (4 s)
- **Shot:** Low-angle medium shot, anamorphic 24mm · **Move:** locked-off
- **In frame:** the canvas roof and steel hoops
- **Action:** As they pass under the gantry a shadow slides over the canvas, and the roof suddenly sags deep under a heavy unseen weight; the hoops creak.
- **Dialogue:** —
- **Sound:** a soft heavy thump above, the hoops' steel groan, canvas stretching
- **PROMPT:** Low-angle medium shot, anamorphic 24mm lens, locked-off: looking straight up at the faded canvas roof stretched between two curved steel hoops as a dark bar of shadow slides across it, and then the canvas suddenly sags deep under a heavy unseen weight, the hoops flexing and the fabric trembling. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a thin red glow seeping through the stretched canvas. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, the robot visible, claws tearing through, torn canvas, people
- **Refs:** LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** The truck passes under the gantry here. The red line glows through the canvas (the only saturated red in the bed).

### 05.05.004 — Army truck, cargo bed — The jackal drops onto the tailgate   (5 s)
- **Shot:** Medium wide shot, anamorphic 32mm, from the cab end looking aft · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1; soldiers at the benches as dark shapes (soft)
- **Action:** The jackal swings down off the roof and lands side-on across the raised tailgate, perfectly balanced at speed, the road and the pale pods streaming away behind it.
- **Dialogue:** —
- **Sound:** a soft pad-tap on steel, no other sound from it
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, locked-off, from the front of the cargo bed looking back to the open tailgate: {UNIT_JACKAL.LONG}, swings down off the canvas roof and lands side-on across the raised tailgate, balanced at speed, pale driverless pods streaming away behind it. Setting: {LOC_ARMY_TRUCK.SHORT}, on the flyover at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the pods' white light bars behind it and its own thin red line. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzle toward the lens, weapon facing camera, robot facing the camera head-on, posing, growling, second robot
- **Refs:** UNIT_JACKAL_REF_A, LOC_ARMY_TRUCK_NIGHT, UNIT_ROBOTAXI_REF
- **Flags:** —
- **Continuity:** Jackal D0. Stays side-on across the tailgate so its spine weapon points across frame, never down the bed at the lens. Scale: 0.9 m at the shoulder, head at a seated man's eye level.

### 05.05.005 — Army truck, cargo bed — The red line crosses face after face   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** slow pan left along the right bench
- **In frame:** ADAEZE (CHAR_ADAEZE_B1), RAMI (CHAR_RAMI_B1)
- **Action:** A thin red line of light slides across Adaeze's face, then Rami's; both hold stock-still, eyes lowered, as it passes.
- **Dialogue:** —
- **Sound:** a faint high servo whisper as the head sweeps; breathing held
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow pan left along the bench: a thin red line of light slides slowly across the face of {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, then across {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_B}, who both hold stock-still with their eyes lowered as it passes over them and moves on. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the thin red line the only saturated light. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, celebrity likeness, beard or moustache on the young man, readable logo or lettering on the windbreaker, brand logos on clothing or shoes, long hair, braids, wig, headwrap, business suit, readable laptop stickers, glasses swapped between the two faces, red laser dots, beams in the air, red wash over the whole face, splint on the right hand
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, CHAR_RAMI_A_front, CHAR_RAMI_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** The line is a thin horizontal red stripe on skin (a light element in comp if the plate drifts), not a beam. NEG: CHAR_ADAEZE.NEG and CHAR_RAMI.NEG written as their non-conflicting terms (each bans the other's glasses).

### 05.05.006 — Army truck, cargo bed — It stops on Nour   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1); TUT's shoulder (soft foreground)
- **Action:** The red line slides across a young man's shoulder in the foreground, passes over him, and comes to rest across Nour's face; she holds perfectly still, eyes lifting to it.
- **Dialogue:** —
- **Sound:** the servo whisper stops
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, sits behind the soft charcoal shoulder of a young man in the foreground as a thin red line of light slides across his shoulder and comes to rest across her face; she holds perfectly still, her eyes lifting to meet it. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the thin red line across her cheekbones. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, red laser dot, beam in the air, red wash over the whole frame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** "It passes over Tut. It stops on Nour." The jackal targets Nour (SESHAT wants her "home", not Tut damaged).

### 05.05.007 — Army truck, cargo bed — Tut slides in front of her   (5 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1), NOUR (CHAR_NOUR_B1)
- **Action:** Tut slides along the bench and sets himself squarely in front of Nour; the red line now lies across his chest.
- **Dialogue:** —
- **Sound:** his stick knocking the bench; the canvas
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, slides along the bench and sets himself squarely in front of {CHAR_NOUR.SHORT}, his jacket falling open on {CHAR_TUT.STATE_G0}, and the thin red line of light that lay on her face now lies across his chest; he lifts his chin toward the tailgate off frame right. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the red line crossing his chest. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, elongated cranium, conehead, grey skin, oversized black eyes, glowing skin, visible circuitry, lattice pattern under the skin, metal face plates, robot or android look, striped royal headcloth, gold funerary mask, crown, bandage wrappings, heavy eye makeup, beard, jewellery on the young man, hood up, bare chest, metal plate visible, red laser dot, beam in the air
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, CHAR_NOUR_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | as 05.05.008: cold pale green, core #A6F2C2 falling to #3F8F6A, one slow even swell every 4 s, about 6 cm spill through linen (file 01) | centre chest, tracked, under the red line | from the jacket falling open to the end | G0 glow element library
- **Continuity:** Jacket now open at the front (G0 visible from here, comped, through 05.05.008). The tailgate/jackal is frame right in this set-up. NEG: CHAR_TUT.NEG written as its non-conflicting terms (its "a full head of hair" would fight Nour's curls in the same frame).

### 05.05.008 — Army truck, cargo bed — The red line over the glow   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TUT's chest (G0)
- **Action:** Across white linen at the centre of Tut's chest, the thin red line lies still over the soft glow.
- **Dialogue:** —
- **Sound:** a very low, slow swell (the G0 breath), under the engine
- **PROMPT:** Insert, 100mm macro lens, locked-off: between the open fronts of an oversized charcoal field jacket, on plain white linen, {CHAR_TUT.STATE_G0}, and a thin red horizontal line of light lies perfectly still across it. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, the red line and the soft glow the only light on the linen. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bare chest, skin, metal plate visible, red laser dot, beam in the air
- **Refs:** CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green, core #A6F2C2 falling to #3F8F6A, one slow even swell every 4 s, about 6 cm spill through linen (file 01 table) | centre chest, under the red line | full shot | glow element from the G0 library
- **Continuity:** G0 (1.5 → 6.2). The glow is comped; the plate carries only the neutral phrase.

### 05.05.009 — Army truck, cargo bed — The jackal recalculates   (4 s)
- **Shot:** Close-up, anamorphic 75mm, side-on · **Move:** locked-off
- **In frame:** UNIT_JACKAL (head and forequarters)
- **Action:** The jackal's head tilts a few degrees and holds dead still, its red line steady; the canvas flap snaps behind it.
- **Dialogue:** —
- **Sound:** nothing from it; canvas snapping
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, side-on: the narrow sensor head of {UNIT_JACKAL.SHORT}, tilts a few degrees and holds dead still, its thin red line steady, as the loose canvas flap behind it snaps in the wind and the road streams away beyond the tailgate. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, white pod light behind it. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzle toward the lens, face, eyes, ears, head-on to camera
- **Refs:** UNIT_JACKAL_REF_A, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** "Recalculating. One second is enough." Hold the tilt; cut on the hold.

### 05.05.010 — Army truck, cargo bed — Fathi slaps the charge home   (4 s)
- **Shot:** Insert, anamorphic 50mm · **Move:** subtle handheld
- **In frame:** FATHI's hand; PROP_DEMO_CHARGES (under the jackal's chest)
- **Action:** Fathi's hand slaps a flat charge against the underside of the jackal's chest; his thumb presses the fuse.
- **Dialogue:** —
- **Sound:** a flat slap of adhesive on carbon, a small click
- **PROMPT:** Insert, anamorphic 50mm lens, subtle handheld: a broad dark-brown hand slaps one of {PROP_DEMO_CHARGES.SHORT} flat against the underside of a matte-black machine's chest, {PROP_DEMO_CHARGES.STATE_UNDER_MACHINE}, and the thumb presses a small fuse on its face. Setting: {LOC_ARMY_TRUCK.SHORT}, at the tailgate, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, red light spilling down from above onto the olive-drab. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, readable labels, blinking LEDs, digital countdown display
- **Refs:** PROP_DEMO_CHARGES_REF, UNIT_JACKAL_REF_A, CHAR_FATHI_B_full
- **Flags:** —
- **Continuity:** Fathi reaches the jackal from his place near the tailgate end of the right bench (05.01.002 geography). One charge gone from the satchel. The fuse is a short delay (the THUMP comes on the road, 05.05.013).

### 05.05.011 — Army truck, cargo bed — SHOVE   (4 s)
- **Shot:** Medium shot, anamorphic 32mm · **Move:** urgent handheld
- **In frame:** FATHI (CHAR_FATHI_B1); UNIT_JACKAL
- **Action:** Braced on the bench, Fathi drives his boot hard into the jackal's flank; it tips backward off the tailgate and out of frame.
- **Dialogue:** —
- **Sound:** a grunt, a boot on carbon, the machine gone
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, braced against the bench, drives his boot hard into the flank of {UNIT_JACKAL.SHORT}, and it tips backward off the tailgate and drops out of frame into the rushing dark. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, white pod light flaring through the empty tailgate. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_FATHI.NEG}, muzzle toward the lens, sparks, explosion
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, UNIT_JACKAL_REF_A, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** The machine takes the force, never a human (05 §7.5). Fathi's boot LEFT to right across frame toward the tailgate.

### 05.05.012 — Army truck, cargo bed — It hits the road and rights itself   (4 s)
- **Shot:** Wide shot, anamorphic 35mm, over the tailgate · **Move:** vehicle-mounted
- **In frame:** UNIT_JACKAL ×1 on the road; UNIT_ROBOTAXI behind
- **Action:** Through the rear flap: the jackal hits the asphalt, rolls once and springs upright at once, already loping after them.
- **Dialogue:** —
- **Sound:** a clatter of carbon on asphalt, then its silence again
- **PROMPT:** Wide shot, anamorphic 35mm lens, vehicle-mounted, looking back over the tailgate: on the road rushing away behind the truck, {UNIT_JACKAL.SHORT}, hits the asphalt, rolls once and springs upright at once, already loping after them, a line of pale driverless pods gliding behind it. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, muzzle toward the lens, fire, people on the road
- **Refs:** UNIT_JACKAL_REF_A, UNIT_ROBOTAXI_REF, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** VFX-ASSIST
- **Continuity:** The jackal can be driven from the 3D asset (bible §14.4). Parent of 05.05.013.

### 05.05.013 — Army truck, cargo bed — THUMP: it folds and skids away   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, over the tailgate · **Move:** vehicle-mounted (continuing)
- **In frame:** UNIT_JACKAL (→ D3); UNIT_ROBOTAXI parting and closing
- **Action:** A flat bang and a burst of dust beneath it; all four legs fold at once and it skids away on its belly, red line strobing, and comes to rest collapsed as the pods part around it and close again.
- **Dialogue:** —
- **Sound:** a flat THUMP, a long scrape of carbon on asphalt, the pods' silence
- **PROMPT:** Wide shot, anamorphic 35mm lens, vehicle-mounted, continuing the same camera move at the same speed: a flat bang and a burst of dust go off beneath {UNIT_JACKAL.SHORT}, its legs fold all at once and it skids away on its belly, red line strobing, coming to rest {UNIT_JACKAL.STATE_D3}, while the pale pods behind swerve around it and close ranks again. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fireball, large explosion, flying debris toward camera, fluid, people
- **Refs:** UNIT_JACKAL_REF_A, UNIT_ROBOTAXI_REF, LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** VFX-ASSIST, VFX-EXTEND, EXTEND:05.05.012
- **Continuity:** Generated from the last clean frame of 05.05.012. Jackal ends D3 ("collapsed flat on its belly with all four legs splayed outward, its red line dark"). Fathi's charge = "a flat bang and a burst of dust" (05 §7.5). VFX-ASSIST: the bang; before/after plates if the fold fails.

### 05.05.014 — Army truck, cargo bed — Nour: "It wouldn't fire through you."   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Tut · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1); TUT's shoulder (foreground, no face)
- **Action:** Over Tut's soft shoulder, Nour looks at him and speaks low in Late Egyptian.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "It wouldn't fire through you."
- **Sound:** engine; the others' ragged breathing
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: over the soft charcoal shoulder of a young man in the foreground, {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, looks at him, shaken, speaking softly in an ancient language, one short sentence. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, cold pod light from the tailgate on her face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, second face in the foreground
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "It wouldn't fire through you." | lower third | line in to out | seq 05 subtitle file
- **Continuity:** Tut has pulled the jacket half-closed again off screen during 05.05.011–013, so G0 is hidden from here to the end of Seq 5. Late Egyptian recorded with the Egyptologist consultant before generation (05 §9.5). Tut still between Nour and the tailgate.

### 05.05.015 — Army truck, cargo bed — Tut: "It wants me whole."   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Nour · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); NOUR's shoulder (foreground)
- **Action:** Over Nour's shoulder, Tut answers in Late Egyptian, calm.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "No. It wants me whole."
- **Sound:** engine
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: over the soft olive shoulder of a woman in the foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, answers speaking softly in an ancient language, one short sentence, calm, his eyes steady on hers. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, cold pod light rimming his head. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, CHAR_NOUR_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "No. It wants me whole." | lower third | line in to out | seq 05 subtitle file
- **Continuity:** The consultant's recording carries Tut's soft consonants; never prompted.

### 05.05.016 — Army truck, cargo bed — Tut drags back the side canvas   (4 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** At the crest, Tut hauls back the side canvas with his left hand; cold air and the far city's light spill across his face.
- **Dialogue:** —
- **Sound:** canvas ripping back on its ties, the wind jumping in volume
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_WRIST_SEAMS}, hauls back the side canvas of the truck with his left hand, and the wind and the faint orange light of a distant city spill in across his face as he looks out. Setting: {LOC_ARMY_TRUCK.SHORT}, at the crest of the flyover at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a far sodium-orange glow from outside on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Side canvas on the LEFT bench side, which faces the river (river at frame left below the flyover).

### 05.05.017 — Army truck, cargo bed — Tut's POV: the city goes out   (6 s)
- **Shot:** Point-of-view shot, anamorphic 75mm · **Move:** vehicle-mounted
- **In frame:** the city (VFX-EXTEND)
- **Action:** From the crest: towers, bridges and avenues going dark district by district, block after block of sodium orange winking out toward the horizon.
- **Dialogue:** NOUR (O.S.): "Zamalek. Downtown. Tahrir."
- **Sound:** wind; very far off, a single car alarm stopping; Nour's voice close
- **PROMPT:** Point-of-view shot, anamorphic 75mm lens, vehicle-mounted: from the crest of the road the whole city spreads below, towers, bridges and long avenues going dark district by district, block after block of sodium orange winking out in sequence toward the horizon. Setting: {LOC_CAIRO_FLYOVER.LONG}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, {GRADE_NIGHT_ACTION.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, fire, explosions, burning buildings, smoke, lightning, moon in frame, readable signage
- **Refs:** LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** "Like someone walking through a house at bedtime": the district switch-off is comped over the plate (file 03 entry 17 flag); lights go out in a steady walking rhythm, never flickering. Nothing burns (bible §7, 5.1).

### 05.05.018 — Army truck, cargo bed — The old museum goes dark   (5 s)
- **Shot:** Wide shot, anamorphic 135mm · **Move:** vehicle-mounted
- **In frame:** a lit pink neoclassical façade by the river
- **Action:** Compressed by the long lens, a lit pink façade beside the dark river among black towers; its floodlights go out.
- **Dialogue:** NOUR (O.S.): "The old museum. Your things lived there a hundred years."
- **Sound:** wind; Nour's voice
- **PROMPT:** Wide shot, anamorphic 135mm lens, vehicle-mounted: compressed by the long lens, a lit pink neoclassical museum façade with a tall arched entrance stands beside the dark river among blacked-out towers, and then its floodlights go out. Setting: a riverside square in a vast dark city, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_ROLLING}, the façade's warm floodlight the last lit thing, then gone. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable inscriptions on the façade, flags, banners, fire
- **Refs:** LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING
- **Flags:** VFX-EXTEND
- **Continuity:** The façade is described, never named (05 §5.7). [[verify]] in the screenplay: Tut's objects at Tahrir from the 1920s to the GEM move; "a hundred years" is a round figure. The switch-off can be a comp light change on a lit plate.

### 05.05.019 — Army truck, cargo bed — Tut: "I stayed home."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** At the open canvas, the last of the city's light dying across his face, Tut answers.
- **Dialogue:** TUT: "My things. I stayed home."
- **Sound:** wind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, at the open canvas with the wind in his face, the last faint orange light of the city fading off his skin, speaks one short sentence, quiet and dry, his eyes staying on the view. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, a dying sodium glow on his face leaving cool starlight. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** One light change only (the glow fading). English line.

### 05.05.020 — Army truck, cargo bed — Only the river still shines   (6 s)
- **Shot:** Extreme wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** the city (VFX-EXTEND)
- **Action:** The last towers go dark; the whole city lies black under the stars except the wide river winding through it, still shining, holding the stars.
- **Dialogue:** —
- **Sound:** the wind drops away; a long quiet
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, locked-off: the last lit towers of the city go dark, and the whole city lies black under a starry sky except the wide river winding through it, still shining, holding the stars. Setting: {LOC_CAIRO_FLYOVER.SHORT}, at night. Lighting: {LOC_CAIRO_FLYOVER.LIGHT_BLACKOUT_FULL}, faint cool starlight on the water. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, moon in frame, fire, lightning, aurora, city glow on the horizon
- **Refs:** LOC_CAIRO_FLYOVER_BLACKOUT_FULL
- **Flags:** VFX-EXTEND
- **Continuity:** Final state of the city for Seq 5: BLACKOUT_FULL. Stars reflected in the river are a comp element if the plate cannot hold them.

---

## Scene 05.06 — INT. ARMY TRUCK, CAB (MOVING) - CONTINUOUS

### 05.06.001 — Army truck, cab — Tarek drives; only Hassan's boots   (5 s)
- **Shot:** Medium shot, anamorphic 32mm, low from the passenger footwell · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B1); HASSAN's boots only (foreground edge)
- **Action:** Tarek drives now, eyes fixed on the road; at the lower edge of the frame, in the dark footwell, rest only a pair of still tan boots.
- **Dialogue:** —
- **Sound:** the engine; wind whistling through the starred glass
- **PROMPT:** Medium shot, anamorphic 32mm lens, vehicle-mounted, low from the passenger footwell: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, drives now, both hands on the wheel, eyes fixed on the dark road through the starred windscreen, and at the lower edge of the frame, in the dark footwell, rest only a pair of still tan combat boots. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, a body in view, a face in the footwell, legs above the ankle, blood, stains, wound
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Kill grammar: "only their boots remain at the frame's edge" (05 §7.1). Windscreen STARRED. Tarek at the wheel for the rest of the drive.

### 05.06.002 — Army truck, cab — The stand-down order   (7 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** the cab radio handset on its coiled cord
- **Action:** On the dash the army radio hisses, then a calm staff officer's voice relays the order.
- **Dialogue:** STAFF OFFICER (V.O., radio; in Egyptian Arabic; subtitled): "...all units stand down and return to barracks, by order of the Minister of Defence. Please acknowledge."
- **Sound:** radio hiss, a squelch, the calm voice in radio futz
- **PROMPT:** Insert, 100mm macro lens, locked-off: on the dashboard, a military radio handset hangs on its coiled cord, its speaker grille lit dimly green by the dashboard, trembling faintly with the truck's vibration as it hisses. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable labels on the radio, digital displays, brand names, glowing buttons
- **Refs:** LOC_ARMY_TRUCK_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "...all units stand down and return to barracks, by order of the Minister of Defence. Please acknowledge." | lower third, two lines | line in to out | seq 05 subtitle file
- **Continuity:** CHAR_STAFF_OFFICER_VOICE (never pictured). Same voice as 4.3.

### 05.06.003 — Army truck, cab — "I watched him drink the water."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** vehicle-mounted
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek turns his head half toward the cab window and speaks into the bed; then Fathi's question comes back through it and Tarek's jaw hardens.
- **Dialogue:** TAREK (to the back): "The minister has been in the Garden since the unveiling. I watched him drink the water." — FATHI (O.S.): "Then whose orders are we under, sir?"
- **Sound:** radio hiss still running under; the engine
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, turning his head half toward the small window behind his seat, speaks two quiet sentences into the cargo bed, then listens to a question from behind him, his jaw hardening and his eyes going to the radio. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}, headlight spill through the starred glass. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, sunglasses, readable insignia
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** English lines. Fathi is at the cab window in the bed (off screen). The minister drank at the unveiling (4.3; bible §6 Tarek's state beat).

### 05.06.004 — Army truck, cab — Tarek rips out the handset cord   (4 s)
- **Shot:** Insert, anamorphic 50mm · **Move:** locked-off
- **In frame:** TAREK's hand; the radio handset
- **Action:** A thick weathered hand closes on the coiled cord and rips it out of the dash in one pull; the hiss cuts to silence and the cord swings.
- **Dialogue:** —
- **Sound:** a plastic crack; the hiss cuts to dead silence; engine only
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: a thick weathered hand closes on the coiled cord of a military radio handset and rips it out of the dashboard in one hard pull, and the loose cord swings in the dim green dashboard light. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, sparks, smoke, readable labels, rings on the hand
- **Refs:** CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** The army radio is dead from here; the next radio in the story is the police launch's set (Seq 6.4).

---

## Scene 05.07 — EXT. NILE CORNICHE, POLICE DOCK - NIGHT

### 05.07.001 — Nile Corniche, police dock — Headlights on the pontoon   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm · **Move:** locked-off
- **In frame:** PROP_ARMY_TRUCK (parked, headlights on); PROP_POLICE_LAUNCH (moored); the team as small figures on the steps
- **Action:** Under a dark bridge, the truck's headlights rake across a floating pontoon where an old grey launch rides low; small figures move down the steps toward it.
- **Dialogue:** —
- **Sound:** the truck idling then cutting out; water slapping the tyre fenders; the pontoon's creak
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: under a dark bridge, the headlights of {PROP_ARMY_TRUCK.SHORT}, {PROP_ARMY_TRUCK.STATE_STARRED}, rake across a floating pontoon where {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L0}, rides low, and small dark figures hurry down the concrete steps toward it. Setting: {LOC_CORNICHE_DOCK.LONG}, in the dead of night. Lighting: the city black across the water, stars on the black river, {GRADE_NIGHT_ACTION.TEXT}, the truck's headlights as the key. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit hotel windows, lit bridge lamps, police markings, readable text on the launch, moon in frame, crowds
- **Refs:** LOC_CORNICHE_DOCK_BLACKOUT, PROP_ARMY_TRUCK_REF, PROP_POLICE_LAUNCH_REF
- **Flags:** COMP
- **Comp:** SUPER | "5 NOVEMBER. 00:52." | small, lower left (05 §13.7) | 1 s in, 3 s hold, fade | type per 05 §13.7
- **Continuity:** Launch L0 (moored). Faces unreadable at this size: no sync, no principal face work. Geography: the river (and south, upriver) at frame right; the embankment steps at frame left. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.002 — Nile Corniche, police dock — Fathi: "Nothing in her it can steer."   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1); PROP_POLICE_LAUNCH (aft deck)
- **Action:** On the launch's aft deck Fathi climbs up out of the open engine hatch, oil to the wrists, wipes his hands on a rag and says it.
- **Dialogue:** FATHI: "Nothing in her it can steer."
- **Sound:** the hatch lid clanking back; ticking of a cold diesel
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: on the open aft deck of {PROP_POLICE_LAUNCH.SHORT}, {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, climbs up out of an open engine hatch with black oil to the wrists, wipes his hands on a rag and speaks one short sentence with quiet satisfaction. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, stars on the black river, a torch beam from the pontoon giving his face a soft key. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable police markings, digital displays in the wheelhouse, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_POLICE_LAUNCH_REF, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** Fathi: oil to the wrists for the rest of Seq 5 (washes off by Seq 6 dawn). Dry: DMG_L1 "river-wet to the knees" starts on the launch (Seq 6). "An analog police set in the wheelhouse" (seen in Seq 6). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.003 — Nile Corniche, police dock — Tarek takes Hassan's disc   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TAREK's hands; PROP_ID_DISCS (ONE); Hassan's boots (edge, dark)
- **Action:** In the dark of the cab, Tarek's thick fingers lift a single identity disc away on its chain and close it into his fist.
- **Dialogue:** —
- **Sound:** the tiny rattle of a ball chain; nothing else
- **PROMPT:** Insert, 100mm macro lens, locked-off: in the torch-lit dark of a truck cab, thick weathered fingers lift {PROP_ID_DISCS.LONG}, {PROP_ID_DISCS.STATE_ONE}, and close it into a fist, the scuffed toe of a still boot just visible at the dark lower edge of the frame. Setting: {LOC_ARMY_TRUCK.AREA_CAB}, parked at a riverside dock at night. Lighting: darkness in the cab, a torch beam from outside the open door. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable stamping, a face, a body, blood, wound, skin of the driver
- **Refs:** PROP_ID_DISCS_REF, CHAR_TAREK_B_full, LOC_ARMY_TRUCK_NIGHT
- **Flags:** —
- **Continuity:** Hassan's disc → Tarek's pocket (file 04 22.2; he later carries Youssef's and Karim's, and turns three over at 11.1). [[verify]] in the screenplay: Egyptian Army identity discs. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.004 — Nile Corniche, police dock — Fathi closes the door gently   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, outside the cab · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1); the open driver's door (the cab interior black)
- **Action:** At the open driver's door, Fathi raises both palms a moment, lips moving silently, then closes the door gently.
- **Dialogue:** —
- **Sound:** a murmur too low to make out; the door's soft click
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, stands at the open driver's door of the dark truck, the cab interior black, and raises both palms before him for a moment, silently mouthing a few words, then lowers his hands and closes the door gently. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, headlight spill off the pontoon lighting his face from below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, a body in the cab, a face in the cab, prayer mat, tears
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, PROP_ARMY_TRUCK_REF, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** A private prayer, not subtitled and not lip-read (no COMP). After this the truck is STATE_PARKED ("parked dark at a riverside dock, the cab door closed") once the headlights are cut. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.005 — Nile Corniche, police dock — Tarek: "Phones. In the water."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek turns from the truck to the group on the pontoon and gives the order.
- **Dialogue:** TAREK: "Phones. In the water."
- **Sound:** water, the pontoon's creak
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, turns from the dark truck toward the group on the pontoon off frame right and speaks one short sentence, flat and final. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, stars on the black river, a torch beam catching his face from below. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** Hassan's disc in Tarek's left breast pocket. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.006 — Nile Corniche, police dock — Three glows arc into the black   (8 s)
- **Shot:** Wide shot, anamorphic 40mm, from the end of the pontoon · **Move:** locked-off
- **In frame:** MINA, YOUSSEF, KARIM (from behind); TOMAS and FATHI (soft, mid-ground); TAREK (foreground)
- **Action:** Starts: three small glowing phones arc out over the black river from the soldiers' hands and wink out one by one; then two more follow from Tomas and Fathi; ends: in the foreground Tarek tosses his over his shoulder, eyes on the truck.
- **Dialogue:** —
- **Sound:** three small splashes, then two, then one close; water closing over
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off, from the end of the pontoon: three young soldiers seen from behind, {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, {CHAR_YOUSSEF.SHORT}, {CHAR_YOUSSEF.WARD_A}, and {CHAR_KARIM.SHORT}, {CHAR_KARIM.WARD_A}, start by throwing three small glowing phones out over the black river; then two taller figures throw theirs; last, in the foreground, {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, tosses his own over his shoulder, his eyes on the dark truck. Setting: {LOC_CORNICHE_DOCK.SHORT}, {LOC_CORNICHE_DOCK.STATE_PHONES}, at night. Lighting: the city black across the water, a torch beam on the pontoon. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, {CHAR_YOUSSEF.NEG}, {CHAR_KARIM.NEG}, real military unit patches, readable insignia or name tapes, medals, sunglasses, beret on the privates, readable screens, big splashes, rifles pointed at the camera, faces toward the camera
- **Refs:** CHAR_MINA_A_full, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, CHAR_TAREK_B_full, CHAR_TOMAS_A_full, CHAR_FATHI_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** VFX-ASSIST
- **Continuity:** Order per the screenplay: Mina, Youssef, Karim; Tomas; Fathi; Tarek without looking. The soldiers' rifles slung, muzzles down. VFX-ASSIST: the arcs and the sinking glows (STATE_PHONES). Tarek's face is not toward camera here (turned to the truck). NEG: CHAR_TAREK.NEG written as its non-conflicting terms (its "helmet" would strip the privates' tan helmets). Three beats in 8 s (05 §5.4); if the chain will not hold, split at the Tomas/Fathi throws. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.007 — Nile Corniche, police dock — Rami: "Nine years of photos."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1)
- **Action:** Rami weighs his glowing phone in his right hand, says the first line, throws it out over the water, and adds the second, his splinted hand tucked to his chest.
- **Dialogue:** RAMI: "Nine years of photos." (throws) "Mostly food."
- **Sound:** a splash; a snort from someone
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, weighs a glowing phone in his right hand and speaks one short sentence, throws it out over the dark water, then adds a second, rueful sentence with a crooked grin, his splinted left hand tucked against his chest. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, the phone's cold glow on his face until he throws it, then torchlight. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, readable screen
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** Rami's phone gone. Splint LEFT. The notebook stays inside his windbreaker (unseen). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.008 — Nile Corniche, police dock — Adaeze keeps the laptop   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze, the laptop hugged to her chest, lets her phone drop from her fingers over the pontoon's edge; then she meets Tarek's look and answers it.
- **Dialogue:** ADAEZE (off Tarek's look): "No radio. I pulled it the day we switched SESHAT on."
- **Sound:** a small plop below frame
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, a battered dark-grey laptop hugged to her chest, lets her phone drop from her fingers over the pontoon's edge below frame, then meets a hard look from off frame left and speaks one short sentence back, unrepentant. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, a torch beam giving her face a soft warm key. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, laptop stickers, laptop logo, glowing laptop screen
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** The laptop (radio pulled) goes aboard. Tarek is frame left of her in this scene's axis. Lift her key in grade. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.009 — Nile Corniche, police dock — Tut's hand drifts to his neck   (5 s)
- **Shot:** Medium wide shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); the others soft, turned to the water
- **Action:** Apart at the back of the group, leaning on his stick, Tut's left hand drifts to the back of his neck and stays there; nobody notices.
- **Dialogue:** —
- **Sound:** very low, the many-voiced hiss from 05.03.012, for a second only
- **PROMPT:** Medium wide shot, anamorphic 50mm lens, locked-off: at the back of the group on the pontoon, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_STICK}, stands a little apart, and his left hand drifts up to the back of his neck and stays there, while the others, soft and turned away in the foreground, watch the water. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, a torch beam passing across him and away. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, faces of the others toward camera
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, PROP_EBONY_STICK_REF, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** Stick in the RIGHT hand, standing (STATE_STICK); LEFT hand to the nape. Setup for 6.2 ("Is it listening?"). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.010 — Nile Corniche, police dock — Nour's screen: Layla, RESTING   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** NOUR's hand; her phone over the water
- **Action:** Nour, last, holds her phone out over the black water; its screen glows with the approved image; the glow trembles on her fingers.
- **Dialogue:** —
- **Sound:** water lapping under the pontoon; her breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hand holds a phone out over black water, its screen glowing softly with a daylight image, the warm light trembling on her fingers and on the dark ripples below. Setting: {LOC_CORNICHE_DOCK.SHORT}, at the pontoon's edge, at night. Lighting: black night over black water, the warm screen glow the only light on her hand. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, readable screen, phone brand logo, app interface, rings
- **Refs:** CHAR_NOUR_B_full, LOC_CORNICHE_DOCK_BLACKOUT, CHAR_LAYLA_ASLEEP_MASTER (comp only)
- **Flags:** COMP
- **Comp:** screen content | THE APPROVED IMAGE CHAR_LAYLA_ASLEEP_MASTER + white type "RESTING" (screenplay: "On her screen: Layla. RESTING.") | full screen, tracked | full shot | CHAR_LAYLA_ASLEEP_MASTER.png; type per 05 §13.7
- **Continuity:** Same phone, still on since 05.03.004. No unit near the child in any frame; the image is never generated. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.011 — Nile Corniche, police dock — Tut: "She is not in there."   (4 s)
- **Shot:** Over-the-shoulder shot, anamorphic 75mm, over Nour · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); NOUR's shoulder (foreground)
- **Action:** Over Nour's shoulder, Tut, close beside her, says it softly in Late Egyptian, eyes on the phone.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "She is not in there."
- **Sound:** water
- **PROMPT:** Over-the-shoulder shot, anamorphic 75mm lens, locked-off: over the soft olive shoulder of a woman in the foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, standing close beside her, speaking softly in an ancient language, one short sentence, his eyes on the glowing phone in her hand below frame. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, warm screen glow from below on his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_TUT.NEG}, hood up, readable screen
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, CHAR_NOUR_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** COMP
- **Comp:** subtitle | "She is not in there." | lower third | line in to out | seq 05 subtitle file
- **Continuity:** He has crossed to her from 05.07.009 (hand down from the neck now). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.012 — Nile Corniche, police dock — Nour: "I know."   (4 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour, eyes on the screen below frame, answers in Late Egyptian without looking up.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "I know."
- **Sound:** water
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, her eyes on the glowing phone just below frame, answers speaking softly in an ancient language, two words, her eyes staying down, the warm screen light trembling on her face. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, warm screen glow from below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, tears streaming, sobbing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** COMP
- **Comp:** subtitle | "I know." | lower third | line in to out | seq 05 subtitle file
- **Continuity:** Late Egyptian, recorded with the consultant. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.013 — Nile Corniche, police dock — Her hand finds the cartouche   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** NOUR's free hand; PROP_LAYLA_PENDANT (CLUTCHED)
- **Action:** Her free hand rises to her throat and closes around the small silver cartouche.
- **Dialogue:** —
- **Sound:** the fine chain's whisper
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's free hand rises to her throat above a black silk collar and closes around {PROP_LAYLA_PENDANT.LONG}, {PROP_LAYLA_PENDANT.STATE_CLUTCHED}, the knuckles tightening. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: black night, warm screen glow catching the silver for an instant. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable hieroglyphs, legible engraving, gold pendant, rings
- **Refs:** PROP_LAYLA_PENDANT_REF, CHAR_NOUR_B_full
- **Flags:** —
- **Continuity:** Pendant CLUTCHED (file 04: 5.3). The signs on it are never readable here (the COMP read is Seq 6.1). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.014 — Nile Corniche, police dock — "I'm coming back for you."   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour looks down at the screen and speaks to it in Egyptian Arabic, her fist tight at her throat.
- **Dialogue:** NOUR (to the screen; in Egyptian Arabic; subtitled): "I'm coming back for you."
- **Sound:** her voice barely above the water
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, looks down at the glowing phone below frame and, speaking in Egyptian Arabic, says one short sentence to it very quietly, her fist tight at her throat and her eyes wet but steady. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, warm screen glow from below on her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, hand over the mouth, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** COMP
- **Comp:** subtitle | "I'm coming back for you." | lower third | line in to out | seq 05 subtitle file
- **Continuity:** Mouth unobstructed: the fist is at the throat, below the chin (05 §9.2). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.015 — Nile Corniche, police dock — The phone sinks face up   (6 s)
- **Shot:** Top-down shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** the phone in the water
- **Action:** She lets go; the phone drops into the river and sinks face up, its glowing screen shrinking and dimming into green-black water until it is gone.
- **Dialogue:** —
- **Sound:** one small splash; then an underwater hush
- **PROMPT:** Top-down shot, anamorphic 75mm lens, locked-off: a phone falls from an opening hand at the top of frame into dark green-black river water and sinks face up, its softly glowing screen shrinking and dimming into the dark until only black ripples remain. Setting: {LOC_CORNICHE_DOCK.SHORT}, beside the pontoon, at night. Lighting: black night water, the screen's own glow lighting the water around it. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, readable screen, a face in the water, bubbles from a mouth, big splash
- **Refs:** LOC_CORNICHE_DOCK_BLACKOUT, CHAR_LAYLA_ASLEEP_MASTER (comp only)
- **Flags:** COMP, VFX-ASSIST
- **Comp:** screen content | THE APPROVED IMAGE CHAR_LAYLA_ASLEEP_MASTER, face up, shrinking and tinted by the water | on the sinking screen, tracked | 0.5 s → gone at 5 s | CHAR_LAYLA_ASLEEP_MASTER.png
- **Continuity:** "It sinks face up, the sleeping face shrinking in green water. Gone." VFX-ASSIST: the splash and the sink; deliver a clean water plate. Nour now has no phone (SESHAT reaches her again only through the tablet, 11.1). Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.016 — Nile Corniche, police dock — "They do not own the river."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut turns from the water to face them all and says it in English, quiet and certain.
- **Dialogue:** TUT (in English, to all of them): "They own the sky and the wires. They do not own the river."
- **Sound:** water; then a held silence before the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, turns from the black water to face the whole group off frame and speaks two short sentences, quiet and certain, his dark eyes moving from face to face. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, a torch beam giving his face a soft warm key, stars on the river behind him. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** The sequence's key line (bible §7, Seq 5.3). Eyeline sweeps frame left to right across the group. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.07.017 — Nile Corniche, police dock — The diesel coughs and catches   (4 s)
- **Shot:** Insert, anamorphic 50mm · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (stern, exhaust)
- **Action:** At the launch's stern the exhaust coughs a black puff, catches, and begins to pound; the water behind the hull churns in the torchlight.
- **Dialogue:** —
- **Sound:** the diesel COUGHS. Catches. Pounds.
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: at the stern of {PROP_POLICE_LAUNCH.SHORT}, a short exhaust stack coughs one puff of dark smoke, catches, and begins to pound, and the black water behind the hull churns pale in a sweeping torch beam. Setting: {LOC_CORNICHE_DOCK.SHORT}, at night. Lighting: the city black across the water, stars on the black river. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, flames from the exhaust, readable police markings, bright lights on the boat
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** VFX-ASSIST
- **Continuity:** Launch now running; no lights (runs dark into Seq 6). VFX-ASSIST: the prop-wash churn. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

---

## Scene 05.08 — EXT. NILE - CONTINUOUS

### 05.08.001 — The Nile — The launch slips the pontoon   (6 s)
- **Shot:** Wide shot, anamorphic 75mm, profile · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (running dark); the team aboard as silhouettes
- **Action:** The launch slips the pontoon with no lights and swings slowly to frame right, south, upriver, its wake silver on the black water.
- **Dialogue:** —
- **Sound:** the diesel's steady pound receding, water folding off the bow
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: {PROP_POLICE_LAUNCH.LONG}, running dark with dark figures on its aft deck, slips away from a floating pontoon and swings slowly to frame right, upriver, its wake a pale silver line on the black water. Setting: the wide river through a vast dark city, a stone embankment behind, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, navigation lights on the boat, searchlight on, lit city windows, moon in frame, readable markings on the hull
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** —
- **Continuity:** Geography lock (file 03 entry 20): south / upriver = frame RIGHT in profile shots of the launch, from here to Seq 8. The launch runs with NO lights ("no lights", seq_05); the dim red wheelhouse lamp of STATE_L1 is withheld pending 05 §14 Q2.

### 05.08.002 — The Nile — Tarek counts his men   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** At the stern, Tarek looks over his men and murmurs their names under his breath, one by one.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled; under his breath): "Fathi. Mina. Youssef. Karim."
- **Sound:** the diesel; the wake hissing
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: at the stern of a dark launch, {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, looks along his men off frame left and, speaking in Egyptian Arabic under his breath, murmurs four names one by one, his lips barely moving. Setting: on the black river at night, the dark city sliding past behind him. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, readable insignia
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Fathi. Mina. Youssef. Karim." | lower third | each name in to out | seq 05 subtitle file
- **Continuity:** The soldier pack is now Tarek, Fathi, Mina, Youssef, Karim (bible §7). Hassan's disc in his pocket. Lift his key in grade: faces must read.

### 05.08.003 — The Nile — He stops where the next name would be   (4 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek's lips part for one more name, and stop; he looks away at the water.
- **Dialogue:** —
- **Sound:** the missing name: only the diesel
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, his lips parting for one more word, stops, holds a breath, and turns his eyes away to the black water at frame right. Setting: on the black river at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, tears streaming
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The unspoken fifth name is Hassan. The beat mirrors 10.4 ("Youssef. Karim. You are relieved.").

### 05.08.004 — The Nile — The pods wait at the water's edge   (6 s)
- **Shot:** Wide shot, anamorphic 135mm, from the launch looking back · **Move:** locked-off
- **In frame:** UNIT_ROBOTAXI (a line; VFX-EXTEND)
- **Action:** On the Corniche behind them, pods roll up one by one and stop at the water's edge, doors sliding open, cabins warm and white. Waiting. They come no further.
- **Dialogue:** —
- **Sound:** far off, a soft chime from each door, carried over the water; the diesel near
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: across the black water on the dark embankment behind them, driverless pods, each {UNIT_ROBOTAXI.SHORT}, roll up one by one and stop in a neat line at the water's edge, their doors sliding open onto warm white empty cabins, and then they wait, perfectly still. Setting: {LOC_CORNICHE_DOCK.SHORT}, seen from the river, at night. Lighting: the city black behind, the warm cabin light doubled in the water. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people in the pods, passengers stepping out, pods entering the water, logos on vehicles
- **Refs:** UNIT_ROBOTAXI_REF, LOC_CORNICHE_DOCK_BLACKOUT
- **Flags:** VFX-EXTEND
- **Continuity:** The doors OPEN here (seq_05 overrides file 02 §14.4 "the doors never open": this is SESHAT's invitation, "the doors are open to you"). Cabins warm white (the Garden's invitation), not the cold white of the chase. Light written out: the dock lock's BLACKOUT variant carries far-bank fires (header, QA2 fix 1).

### 05.08.005 — The Nile — The launch goes into the dark   (7 s)
- **Shot:** Extreme wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (small); the line of pods on the far bank
- **Action:** The dark launch, small on the wide black river, slides away to frame right into the darkness until only its faint wake remains; the lit pods wait on the bank behind.
- **Dialogue:** —
- **Sound:** the diesel fading to nothing; water; silence
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, locked-off: the dark launch, small on the wide black river, slides away to frame right until only a faint silver wake remains, while a line of lit, open, empty pods waits at the left bank's edge. Setting: a vast blacked-out city, in the dead of night. Lighting: {GRADE_NIGHT_ACTION.TEXT}, starlight on the black water, the pods' open cabins the only light on the bank. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, navigation lights, lit city windows, moon in frame, fire
- **Refs:** PROP_POLICE_LAUNCH_REF, UNIT_ROBOTAXI_REF, LOC_NILE_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** Lighting written out rather than LOC_NILE.LIGHT_NIGHT ("no light on either bank") because the lit pods must read on the bank (logged in the header). End of Seq 5, ~01:00 on 5 Nov (bible §12: launch departs ~01:00). Launch travels frame right (south). Out: fade or hard cut to Seq 6 night river.
