# HERE AM I — SEQUENCE 4: "GEM NIGHT" — shot list and AI-video prompts

**Screenplay:** `screenplay/seq_04.fountain` (pp. 27–35; about 8.5–9 pages) · 4 November 2033, 18:00 → about 19:00 · END OF ACT ONE
**Format:** photoreal live action, 1920×1080, 16:9, 24 fps, clips of 4–8 s. Every PROMPT ends with `{SUFFIX}` and every NEGATIVE starts with `{NEG}`. Look-locks go in as `{TOKEN.FIELD}` from `production_bible/locks.json` and are expanded by `shots_md2jsonl.py` into `shots/seq_04_shots.jsonl`.
**Shots:** 123 · **Running time:** 633 s = **10.6 min** (target 9 min ±20%, so 7.2–10.8) · **Average shot:** 5.1 s
**Flags:** COMP 41 · VFX-EXTEND 12 · VFX-ASSIST 8 · EXTEND 3 (04.03.002 ← 001, 04.03.038 ← 037, 04.06.006 ← 005). 04.05.007 and 04.05.015 may also be generated as extends of 04.05.006 and 04.05.012; their Continuity lines say how.

## Scene list

| Scene | Heading | Shots | Count | Time | Location token / variant |
|---|---|---|---|---|---|
| 04.01 | INT. GEM GRAND ATRIUM - NIGHT (the gala, Tut's two sentences, the trumpet, the blackout) | 04.01.001–018 | 18 | 96 s | LOC_GEM_ATRIUM / GALA → BLACKOUT |
| 04.02 | MONTAGE - CONTROL ROOMS - NIGHT (grid, High Dam, Suez pilots, cable station) | 04.02.001–004 | 4 | 20 s | LOC_CONTROL_ROOMS / GRID, DAM, CANAL, CABLE · DARK |
| 04.03 | INT. GEM GRAND ATRIUM - CONTINUOUS ("Here am I", the water, the stand-down, the corridor kill, the Reis) | 04.03.001–038 | 38 | 192 s | LOC_GEM_ATRIUM / BLACKOUT → GARDEN |
| 04.04 | INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS (stick, dagger, kit, the shrine) | 04.04.001–016 | 16 | 81 s | LOC_GEM_TUT_GALLERIES / EMERG (+ CASES_SMASHED) |
| 04.05 | INT. GEM SERVICE STAIRWELL - CONTINUOUS (the summons, the Red Beer) | 04.05.001–017 | 17 | 79 s | LOC_GEM_ATRIUM/SERVICE_STAIRWELL / EMERG |
| 04.06 | INT. GEM GRAND ATRIUM - CONTINUOUS (the nine seconds; Layla) | 04.06.001–012 | 12 | 64 s | LOC_GEM_ATRIUM / GARDEN |
| 04.07 | INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS | 04.07.001–003 | 3 | 17 s | LOC_GEM_TUNNEL / EMERG |
| 04.08 | INT. GEM KHUFU BOAT HALL - CONTINUOUS | 04.08.001–005 | 5 | 27 s | LOC_GEM_BOAT_HALL / EMERG |
| 04.09 | INT. GEM LOADING DOCK - NIGHT (the jacket; the truck; act out) | 04.09.001–010 | 10 | 57 s | LOC_GEM_LOADING_DOCK / BLACKOUT; LOC_ARMY_TRUCK / NIGHT |

## Camera plan
- **04.01 is Act I camera:** composed, locked-off, slow push-ins, no handheld. Order becomes disorder in one cut on the blackout (04.01.018); handheld arrives with the soft white light (04.03.004) and turns urgent in the corridor action and the run.
- **Every new space opens on a geography wide:** atrium master from the entrance (colossus facing camera, Grand Staircase frame right, glass wall frame left, service corridor left of the plinth); galleries right → left; tunnel left → right; boat hall pan right; dock wide.
- **Lenses:** 24 mm for the atrium masters and the tunnel, 32–50 mm for coverage, 75 mm for dialogue singles (lip-sync framing), 100 mm macro for the pin-light, trumpet, dagger, fingers and key inserts, 135 mm for the long-lens atrium compressions (the Defence Minister, Layla across the floor).

## Rulings applied (screenplay wins over the bible on story states)
- **Tut:** A0 with the clinic cane and G0 until the galleries; L1, ebony stick (RIGHT hand) and the dagger in the sash from 04.04.007/009; A1 (Tarek's charcoal jacket, hood up) from 04.09.004. Nape port intact. His chest glow is COMP on every shot where his chest is in frame.
- **The Reis:** R1 on its entrance (04.03.029), R2 (the cracked chest star) from the impact on.
- **Layla:** awake only in 04.01.003/005 and 04.03.012/014 (never within reach of a unit); asleep **only** as CHAR_LAYLA_ASLEEP_MASTER, reframed (04.06.005–007), with no unit in frame. Her raincoat is folded under her cheek there, as in the master.
- **Kill grammar (corridor):** jackal fires across frame (04.03.023) → sparks off the steel door frame (024) → two weapon lights drop and roll, with no body ever shown (025) → Karim's reaction (026) → the crack rolling up the staircase (sound tail, 026). Karim's wild round hits the Reis, not a person (028–030).
- **Wardrobe calls for the lead:** Fathi changes A → B from the galleries (the beret is folded under his strap and the satchel carries the pry bar). Adaeze and Tomas change A → B from the galleries. **Tarek stays A0** (pressed uniform, holstered pistol) through the whole of Seq 4, because the pages give him a pistol line of fire and no rifle. His B look (vest, slung rifle) should start in Seq 5. File 01 says "4.4", so the lead should confirm.
- **1939:** V.O. only (LOC_CAIRO_MUSEUM_1939 and CHAR_BANDSMAN_1939 are RESERVE). The trumpet shown is the bronze one; the screenplay's [[verify]] on which trumpet aired stands.
- **Settings with no fitting lock:** the service stairwell pastes LOC_GEM_ATRIUM AREA_SERVICE_STAIRWELL alone, with a stairwell emergency-light phrase in place of LOC_GEM_ATRIUM_EMERG, because that variant says "the statue a dark mass above". The service corridor (no token in file 03) is written in plain words. Both keep the colossus from being generated into concrete back-of-house spaces. The lead should confirm, or file 03 should add a corridor/stairwell EMERG variant. The optional GRADE_GARDEN phrase is not used: it repeats LOC_GEM_ATRIUM_GARDEN almost word for word.
- **Text:** the SUPER, every Arabic and Middle Egyptian subtitle, the 17% status screen, the shrine label and Adaeze's GARDEN: COMPLETE screen are all COMP. No plate carries legible text.
- **Tut overlays (QA pass):** STATE_FOOT on the stair wide (04.01.009) and the tunnel drag (04.07.003); STATE_DAGGER_SASH on every Tut frame to the waist or wider from 04.04.009 (MCUs keep it below frame); STATE_WRIST_SEAMS by token on hand shots; chest-glow COMP also on 04.04.016 (soft fg) and 04.07.001. The truck-bed shot at the dock (04.09.007) uses the dock BLACKOUT light, because LOC_ARMY_TRUCK LIGHT_NIGHT has passing lamps and the truck has not moved yet.
- **QA pass 3:** 04.03 renumbered for two new shots: 04.03.006 (the shabti bring the trays; Hale takes the first glass) so that 04.03.007 carries one action, and 04.03.015 (ON NOUR, she stops shouting) placed after Layla lies down, in the screenplay's order. 04.06.006 runs 7 s, with Layla's face hidden in Nour's neck while she is off the blanket. Tut is a SHORT lock (not plain words) in the group runs 04.04.001 and 04.06.004, with the glow COMP. Tut's LONG goes to his entrance (04.01.009). The stick and L1 dust are on every Tut frame after the galleries. 04.03.001 is VFX-EXTEND. Negations and similes are cleared from the writer's words (05 §5.4).

## Reference stills needed (generate once and approve before any clip; ids per 00_INDEX token grammar)
**Characters:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, CHAR_TUT_B1_full (jacket source for the A1 image edit; A1 has no dedicated still, 00_INDEX open item 7) · CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full · CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, CHAR_LAYLA_B_full, **CHAR_LAYLA_ASLEEP_MASTER** (the one approved asleep image) · CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full · CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_A_full · CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_A_full, CHAR_FATHI_B_full · CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_A_full, CHAR_ADAEZE_B_full · CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_A_full · CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full · CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full (look M: beret by image edit) · CHAR_MINA_A_full, CHAR_YOUSSEF_A_full (look M by image edit) · CHAR_HASSAN_A_front, CHAR_HASSAN_A_full · CHAR_BANDSMAN_2033_front, CHAR_BANDSMAN_2033_full · CHAR_SAMEH_still · CHAR_MINISTER_GALA_still · CHAR_DEFENCE_MINISTER_GALA_still · CHAR_GALA_GUESTS_still · CHAR_ARMY_DETAIL_still · CHAR_CONTROL_OPERATORS_still
**Units:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B · UNIT_REIS_REF_A, UNIT_REIS_REF_B (build the R1 and R2 mast states by image edit) · UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B · UNIT_GLYPH_SESHAT_REF_A (the chest-star emboss for the crack insert) · 3D assets: SHABTI (the 40-unit head turn, the seated Red Beer crowd, the corridor line) and JACKAL
**Props:** PROP_TRUMPET_BRONZE_REF · PROP_CLINIC_CANE_REF · PROP_EBONY_STICK_REF · PROP_DAGGER_REF · PROP_CONSERVATION_KIT_REF · PROP_WATER_GLASSES_REF · PROP_PRY_BAR_REF · PROP_ARMY_TRUCK_REF
**Location plates:** LOC_GEM_ATRIUM_GALA_plate · LOC_GEM_ATRIUM_BLACKOUT_plate · LOC_GEM_ATRIUM_GARDEN_plate · LOC_GEM_ATRIUM_EMERG_plate (the service corridor coverage plate, derived) · LOC_GEM_ATRIUM/STAIRCASE (coverage) · LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate · LOC_CONTROL_ROOMS_DARK_plate + GRID, DAM, CANAL and CABLE area plates · LOC_GEM_TUT_GALLERIES_EMERG_plate (+ CASES_SMASHED after-state) · LOC_GEM_TUNNEL_EMERG_plate · LOC_GEM_BOAT_HALL_EMERG_plate · LOC_GEM_LOADING_DOCK_BLACKOUT_plate · LOC_ARMY_TRUCK_NIGHT_plate · LOC_GEM_CC_EMERG_plate (the white corridor seen from the dock) · LOC_GEM_ROOF_DAY_plate (façade reference only)
**Clean plates for VFX-EXTEND:** atrium GALA master (04.01.001/018), atrium BLACKOUT master (04.03.001–002), atrium GARDEN master (04.03.004), behind-the-plinth GARDEN wide (04.06.002), staircase low angle (04.01.009), dock corridor POV (04.09.006), receding façade (04.09.009)

## Scene 04.01 — INT. GEM GRAND ATRIUM - NIGHT (the gala; shots 04.01.001–018)

### 04.01.001 — INT. GEM GRAND ATRIUM - NIGHT — Establishing: the gala under the colossus   (7 s)
- **Shot:** Extreme wide establishing, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** LOC_GEM_ATRIUM/GALA; CHAR_GALA_GUESTS (≈500, VFX-EXTEND); UNIT_SHABTI ×3 (hero, bg)
- **Action:** The whole atrium from the entrance: guests at round tables, the quartet on the low stage, three shabti gliding between the tables with trays; the pyramids floodlit gold in the glass wall.
- **Dialogue:** —
- **Sound:** a string quartet, five hundred voices murmuring, glass and cutlery; under it, a faint dry ceramic tick where footsteps should be
- **PROMPT:** Extreme wide establishing shot, anamorphic 24mm lens, locked-off: the camera holds the whole room from the entrance as three robots, each {UNIT_SHABTI.SHORT}, walk with smooth, unhurried, even steps between the tables carrying trays, among {CHAR_GALA_GUESTS.SHORT}. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: grand and festive, a held breath before a ceremony. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_GALA_GUESTS.NEG}, empty tables, daylight, camera shake, stage banners, projection screens
- **Refs:** LOC_GEM_ATRIUM_GALA_plate, LOC_GEM_ATRIUM/GALA, CHAR_GALA_GUESTS_still, UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B
- **Flags:** COMP, VFX-EXTEND
- **Comp:** SUPER | "4 NOVEMBER. 18:00." | lower left, small (05 §13.7) | in at 1 s, out at 5 s | seq 04 super file
- **Continuity:** Geography lock (file 03 entry 11): colossus faces camera; Grand Staircase frame right; glass wall with floodlit pyramids frame left; lectern between the statue's feet and camera. Act I camera: composed, no handheld until the blackout (04.01.018). VFX-EXTEND: 3 hero shabti + ~40 hero guests in camera, the rest from the clean plate at this framing.

### 04.01.002 — INT. GEM GRAND ATRIUM - NIGHT — A tug at Nour's sleeve   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Nour, watching the lectern, feels a tug at her sleeve and looks down to frame right; her face softens.
- **Dialogue:** —
- **Sound:** quartet, murmur; a small rustle of cloth
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: the camera holds on {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, who stands at the edge of the tables watching the stage off frame left, feels a small tug at her sleeve and looks down toward frame right, her guarded face softening. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: fierce, jaw set, then undone by tenderness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses worn on the face, evening gown, robot in frame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Nour look B0 (gala: olive jacket over black silk blouse; glasses on the cord, pendant at the throat). Eyeline down frame right to Layla (04.01.003 looks up frame left).

### 04.01.003 — INT. GEM GRAND ATRIUM - NIGHT — Layla: "Is the king going to talk?"   (6 s)
- **Shot:** MS at a child's eye height, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_B)
- **Action:** Layla, still holding a fold of her mother's sleeve, looks up to frame left and speaks, bright and pleading.
- **Dialogue:** LAYLA (in Egyptian Arabic; subtitled): "Baba brought me. I begged. Is the king going to talk?"
- **Sound:** quartet, murmur; her quick breathless voice
- **PROMPT:** Medium shot, low at a child's eye height, anamorphic 50mm lens, locked-off: the camera holds on {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_B}, who holds a fold of an olive sleeve at the edge of frame, looks up toward frame left and, speaking in Egyptian Arabic, asks two quick things, bouncing on her toes. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: bright, excited, a little guilty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot in frame, raincoat hood up, keyring
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_GALA_plate
- **Flags:** COMP
- **Comp:** subtitle | "Baba brought me. I begged. Is the king going to talk?" | lower third, two lines max (05 §13.7) | line in to out | seq 04 subtitle file
- **Continuity:** Layla look B (yellow raincoat over the navy velvet party dress; no keyring: she gave it to Tut in 2.4). No unit in frame (NEG_CHILD). Awake: this is her last close coverage awake in the film until 12.8.

### 04.01.004 — INT. GEM GRAND ATRIUM - NIGHT — Nour: "Two sentences."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Nour bends to frame right, answers in two quick sentences, and tips her chin toward the tables: go.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "Two sentences. Then Baba takes you home. Go."
- **Sound:** quartet; her low quick voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, as she bends slightly toward frame right and, speaking in Egyptian Arabic, says two short sentences, then lifts her chin toward the tables behind her. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: dry, loving, all business. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses worn on the face, robot in frame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_ATRIUM_GALA_plate
- **Flags:** COMP
- **Comp:** subtitle | "Two sentences. Then Baba takes you home. Go." | lower third (05 §13.7) | line in to out | seq 04 subtitle file
- **Continuity:** "Two sentences" recalls the Seq 3 plan; Nour already knows Tut's line. Same light and eyeline as 04.01.002.

### 04.01.005 — INT. GEM GRAND ATRIUM - NIGHT — A man's hand waves; Layla drags back   (4 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** SAMEH (CHAR_SAMEH, from behind); LAYLA (CHAR_LAYLA_B, from behind)
- **Action:** At a table under the colossus a man's hand waves; Layla, seen from behind, drags her feet back to him between the tables.
- **Dialogue:** —
- **Sound:** quartet; her shoes scuffing on stone
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off: at a round table beneath the statue's feet sits {CHAR_SAMEH.SHORT}, and {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_B}, seen from behind, drags her feet back toward him between the white-clothed tables, pigtails bouncing. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: small, sulky, safe for one more minute. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, the man's face, robot in frame
- **Refs:** CHAR_SAMEH_still, CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Sameh is never seen from the front (file 01 §10). Places Layla's table beneath the statue's feet (frame left of the base), which is where she will sleep. No unit near her.

### 04.01.006 — INT. GEM GRAND ATRIUM - NIGHT — Hale: "someone found a step going down"   (5 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale at the lectern speaks to the room, warm and certain, one hand on the lectern's edge.
- **Dialogue:** HALE: "A hundred and eleven years ago today, someone found a step going down."
- **Sound:** his voice through the PA, warm and big; the room hushed
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: the camera closes on {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, standing at a lectern with one hand resting on its edge, as he looks out over the room and speaks one long sentence, relaxed and certain. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, a soft warm stage light on his face. Mood: a showman's ease over total conviction. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, microphone covering the mouth, teleprompter, logo on the lectern
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Hale look A0 (charcoal suit, open collar, steel watch). The lectern mic sits low, below his mouth line (lip-sync framing, 05 §9.2). Lectern is blank (no logo).

### 04.01.007 — INT. GEM GRAND ATRIUM - NIGHT — Hale: "death is a solved problem"   (5 s)
- **Shot:** MS low angle beside the stage, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale opens a hand to the room and finishes, smiling, the colossus rising behind him.
- **Dialogue:** HALE: "Tonight, someone comes up. Because death is a solved problem."
- **Sound:** PA voice; a ripple of applause starting
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: from beside the stage the camera looks up at {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_A}, at the lectern as he opens one hand to the room and speaks two short sentences, smiling, the red granite legs of the colossal statue rising behind him. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: a showman's ease over total conviction. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, microphone covering the mouth, logo on the lectern
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Same lectern and light as 04.01.006. Statue behind him frames the "death is solved" line with the 83-tonne king.

### 04.01.008 — INT. GEM GRAND ATRIUM - NIGHT — The Minister: "the King"   (5 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** MINISTER (CHAR_MINISTER_GALA); MINISTER OF DEFENCE (CHAR_DEFENCE_MINISTER_GALA); CHAR_GALA_GUESTS (bg)
- **Action:** At the top table the host Minister rises, one hand open toward the staircase at frame right; heads turn.
- **Dialogue:** MINISTER (in Arabic, then English; wide, no sync): "Ladies and gentlemen: the King."
- **Sound:** his voice through the PA, Arabic then English; chairs shift; the room turns
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off: the camera holds {CHAR_MINISTER_GALA.LONG}, announcing something to the room; beside him sits {CHAR_DEFENCE_MINISTER_GALA.SHORT}, and the guests at the nearer tables turn their heads toward the staircase at frame right. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: formal, expectant. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_DEFENCE_MINISTER_GALA.NEG}, {CHAR_GALA_GUESTS.NEG}, close-up of any official, flags, nameplates, medals
- **Refs:** CHAR_MINISTER_GALA_still, CHAR_DEFENCE_MINISTER_GALA_still, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Both ministers WIDES ONLY (file 01 §10, §10b). Places the Minister of Defence at the top table for 04.03.008 and 04.03.017. No sync: wide shot (05 §9.2). No subtitle: the English repeat carries the line (seq_04 notes, editor pass 6).

### 04.01.009 — INT. GEM GRAND ATRIUM - NIGHT — The king comes down the stair; three hundred phones rise   (7 s)
- **Shot:** Wide low angle over guests, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); CHAR_GALA_GUESTS (fg silhouettes, VFX-EXTEND)
- **Action:** Over the backs of guests raising phones, Tut in white linen comes down the lowest flight of the Grand Staircase, the aluminium cane clacking on each step, and stops at its foot.
- **Dialogue:** —
- **Sound:** CLACK. CLACK. the aluminium cane on stone; the rustle of three hundred phones rising; the quartet stops
- **PROMPT:** Wide low-angle shot, anamorphic 32mm lens, locked-off: over the dark silhouettes of guests lifting phones whose screens glow faintly, the camera watches {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_FOOT}, {CHAR_TUT.STATE_CANE}, walk slowly down the lowest flight of the staircase at frame right, the cane tapping each step, and stop at its foot. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_STAIRCASE}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_GALA_GUESTS.NEG}, readable phone screens, camera flashes in the lens, crown, gold collar, sandals on both feet
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_ATRIUM_GALA_plate, LOC_GEM_ATRIUM/STAIRCASE
- **Flags:** COMP, VFX-EXTEND
- **Comp:** chest glow G0 | pale-green pulse through the linen at the chest centre, per file 01 glow table | chest centre | whole shot | glow element library. Phone screens: soft abstract glow only.
- **Continuity:** Tut's first shot in the sequence, so his LONG lock (the location stays SHORT). Tut look A0, L0: white gown, clinic cane in RIGHT hand, left ceramic foot bare, right sandal, nape port (unseen), glow G0. Staircase frame right (geography lock). VFX-EXTEND: ~20 phone-holding silhouettes in camera, extend to ~300.

### 04.01.010 — INT. GEM GRAND ATRIUM - NIGHT — Tut: "It has happened —"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** At the lectern microphone Tut looks out over the room and begins his planned sentence; his voice cuts out of the PA mid-phrase.
- **Dialogue:** TUT: "It has happened —"
- **Sound:** his voice big in the PA, then the PA dies mid-word to the naked room sound
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, standing at a lectern microphone as he looks out over the room and speaks the first words of one short sentence, then hesitates, hearing something change. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, a soft warm stage light on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, microphone covering the mouth, glowing skin, logo on the lectern
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, LOC_GEM_ATRIUM_GALA_plate
- **Flags:** COMP
- **Comp:** chest glow G0 at frame bottom (file 01 table) | whole shot
- **Continuity:** The microphone head sits below his mouth line. The overbite and neck seam anchors visible. Lip-sync to the recorded English line.

### 04.01.011 — INT. GEM GRAND ATRIUM - NIGHT — The microphone's pin-light dies   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the lectern microphone
- **Action:** On the microphone's slim black head a tiny white pin-light glows, then goes out.
- **Dialogue:** —
- **Sound:** a soft electrical click; the PA hiss stops
- **PROMPT:** Insert, 100mm macro lens, locked-off: the camera holds on the head of a slim matte-black lectern microphone on a thin gooseneck, where a tiny white pin-light glows steadily, then goes out. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, the room a warm blur of oval bokeh behind. Mood: small, final, deliberate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, logo on the microphone, brand name, red or amber indicator light, green indicator light, hands in frame
- **Refs:** LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** The pin-light is white, never amber, red or green (unit colours are reserved, file 02 §0.1). SESHAT has cut the feed: their plan fails live.

### 04.01.012 — INT. GEM GRAND ATRIUM - NIGHT — Nour's lips move with his   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Among the guests, Nour watches the lectern and silently mouths the words with him.
- **Dialogue:** NOUR (mouthed with Tut; no subtitle, Tut is heard)
- **Sound:** Tut's unamplified voice small in the huge room; a cough somewhere
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the camera holds on {CHAR_NOUR.LONG}, watching the lectern off frame left, silently mouthing a few words without sound, lips clearly shaping each word, in time with a speaker she cannot help. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, hand over the mouth, glasses worn on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Lip-reading motif (05 §9.6): drive the mouth shapes from Tut's recorded line, muted. Eyeline frame left to the lectern.

### 04.01.013 — INT. GEM GRAND ATRIUM - NIGHT — Tut leans in: "Do not let it help you."   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut leans in toward the dead microphone anyway and speaks, low, to the front row alone.
- **Dialogue:** TUT: "— before." (leaning in anyway) "Do not let it help you."
- **Sound:** his bare voice; only the nearest tables hear; a baffled murmur rising behind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: the camera closes on {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, as he leans toward the dead microphone anyway and speaks two quiet sentences down to the nearest table, very dark eyes steady on them. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, a soft warm stage light on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, microphone covering the mouth, glowing skin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, LOC_GEM_ATRIUM_GALA_plate
- **Flags:** COMP
- **Comp:** chest glow G0 (file 01 table) | whole shot
- **Continuity:** "Only the first row hears" is carried by sound and the eyeline down frame left. The second sentence pays off when the shabti serve water (04.03.006–007).

### 04.01.014 — INT. GEM GRAND ATRIUM - NIGHT — The bandsman lifts the bronze trumpet   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** BANDSMAN (CHAR_BANDSMAN_2033); PROP_TRUMPET_BRONZE
- **Action:** At the stage's edge a white-gloved bandsman opens a glass vitrine and lifts the slim bronze-and-gold trumpet out in both hands.
- **Dialogue:** SESHAT (V.O., every speaker): "Forgive us: a small fault. Meanwhile, a flourish."
- **Sound:** SESHAT's voice from every speaker at once, warm and even; the vitrine lid's soft click
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: at the edge of the stage, {CHAR_BANDSMAN_2033.LONG}, lifts the glass lid of a small museum vitrine and with both white-gloved hands raises from it {PROP_TRUMPET_BRONZE.SHORT}, holding it level at his chest. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, a cool spotlight on the open vitrine. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_BANDSMAN_2033.NEG}, valves on the trumpet, brass band instrument, bugle, museum label text
- **Refs:** CHAR_BANDSMAN_2033_front, CHAR_BANDSMAN_2033_full, PROP_TRUMPET_BRONZE_REF, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** The trumpet goes from PROP_TRUMPET_BRONZE STATE_CASE to in hand. White gloves throughout. The 1939 story is V.O. only (LOC_CAIRO_MUSEUM_1939 is RESERVE).

### 04.01.015 — INT. GEM GRAND ATRIUM - NIGHT — Insert: the engraved bell   (6 s)
- **Shot:** Insert, 100mm macro, slow push-in · **Move:** slow push-in
- **In frame:** PROP_TRUMPET_BRONZE
- **Action:** The trumpet turns slowly in white gloves; the engraved figures near the bell catch a thin line of light.
- **Dialogue:** SESHAT (V.O., every speaker): "Sixteenth of April, 1939: the king's trumpets, live on the radio, to an estimated hundred and fifty million listeners."
- **Sound:** SESHAT's even voice; the room silent, listening
- **PROMPT:** Insert, 100mm macro lens, slow push-in: the camera closes on {PROP_TRUMPET_BRONZE.LONG}, held level in white cotton gloves above an open vitrine and turning slowly, so that the engraved standing figures near its bell catch a thin line of warm light. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, a cool spotlight from the vitrine below. Mood: reverent, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, modern mouthpiece, valves, polished new brass, readable engraving, bare hands
- **Refs:** PROP_TRUMPET_BRONZE_REF, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Bronze trumpet (the screenplay's [[verify]] on which trumpet aired in 1939 stands; the pictured one is the bronze, per bible §7). The engraving reads only as fine relief, never legible.

### 04.01.016 — INT. GEM GRAND ATRIUM - NIGHT — By the doors: Tarek and Fathi   (6 s)
- **Shot:** MS two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_A0); TAREK (CHAR_TAREK_A0)
- **Action:** By the tall glass doors Fathi stands at ease beside Tarek; both watch the stage off frame left, Fathi's eyes drifting to a gliding robot.
- **Dialogue:** SESHAT (V.O., every speaker): "Five minutes before air, the power failed. They played by candlelight."
- **Sound:** SESHAT's voice; a faint ceramic tick passing behind them
- **PROMPT:** Medium two-shot, anamorphic 50mm lens, locked-off: by the tall glass doors stands {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_A}, at ease beside {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}; both watch the stage off frame left, and the sergeant's calm eyes slide to follow something moving behind the tables. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TAREK.NEG}, rifle held at the camera, helmets
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_A_full, CHAR_TAREK_A_front, CHAR_TAREK_A_full, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** Fathi's first appearance in the film (A: beret, red scarf knotted at the neck, chest rig; rifle slung, muzzle down). Tarek A0: pressed uniform, sleeves down, beret low to the right, holstered pistol, radio handset at the left shoulder. The glass front and its doors are behind camera in the master; this is the reverse.

### 04.01.017 — INT. GEM GRAND ATRIUM - NIGHT — One note   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** BANDSMAN (CHAR_BANDSMAN_2033); PROP_TRUMPET_BRONZE
- **Action:** The bandsman raises the trumpet to his lips, breathes, and blows one long, brazen, cracked note.
- **Dialogue:** —
- **Sound:** one NOTE, brazen, cracked, enormous (re-recorded from the real instrument or a replica; [[verify]] with the consultant)
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_BANDSMAN_2033.SHORT} raises {PROP_TRUMPET_BRONZE.SHORT} to his lips, fills his chest with one slow breath and blows a single long note, his cheeks steady and his eyes closing with the effort. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}. Mood: military exactness, and something ancient waking. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_BANDSMAN_2033.NEG}, puffed cheeks, valves, bugle, spit
- **Refs:** CHAR_BANDSMAN_2033_front, CHAR_BANDSMAN_2033_full, PROP_TRUMPET_BRONZE_REF, LOC_GEM_ATRIUM_GALA_plate
- **Continuity:** The note starts here and holds over the blackout (04.01.018) and the whole control-room montage (04.02). Trumpet state RAISED.

### 04.01.018 — INT. GEM GRAND ATRIUM - NIGHT — Every light goes out, the pyramids too   (6 s)
- **Shot:** Wide master from the entrance, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** LOC_GEM_ATRIUM/GALA; CHAR_GALA_GUESTS (VFX-EXTEND)
- **Action:** The whole room holds on the note; then every light dies at once, the floodlit pyramids in the glass wall with it.
- **Dialogue:** —
- **Sound:** the note, then every hum in the building cutting out beneath it; the note alone
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: from the entrance the camera holds the whole room, the guests frozen at their tables as a single note sounds, and then every light in the building dies at once, the floodlit pyramids in the glass wall going dark with it, leaving near black. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GALA}, cutting to total darkness in one instant. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_GALA_GUESTS.NEG}, gradual fade, flicker, lightning, sparks, explosions, broken glass
- **Refs:** LOC_GEM_ATRIUM_GALA_plate, LOC_GEM_ATRIUM_BLACKOUT_plate, CHAR_GALA_GUESTS_still
- **Flags:** VFX-EXTEND, VFX-ASSIST
- **Continuity:** Same framing as 04.01.001 (the establishing master). One light change only. VFX-ASSIST: generate the GALA and BLACKOUT states as matched plates; the cut to black is timed to the note in comp. Order becomes disorder in one cut (05 §4.4): handheld is allowed from here.

## Scene 04.02 — MONTAGE - CONTROL ROOMS - NIGHT (shots 04.02.001–004)

### 04.02.001 — MONTAGE - CONTROL ROOMS - NIGHT — Cairo grid control: the board greys out   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_CONTROL_OPERATORS (3–4, from behind and side); LOC_CONTROL_ROOMS/GRID
- **Action:** Operators sit very still as the wall-sized board of glowing lines freezes, then greys out section by section.
- **Dialogue:** —
- **Sound:** the trumpet note holds over everything; under it, cooling fans winding down; a chair creaks
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: from behind the back row, the camera watches {CHAR_CONTROL_OPERATORS.SHORT}, sitting very still as the curved wall of glowing lines in front of them freezes, then greys out section by section from left to right. Setting: {LOC_CONTROL_ROOMS.LONG}, {LOC_CONTROL_ROOMS.AREA_GRID}, at night. Lighting: {LOC_CONTROL_ROOMS.LIGHT_DARK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, sparks, smoke, fire, broken screens, panic, alarm lights, maps with place names
- **Refs:** LOC_CONTROL_ROOMS_DARK_plate, LOC_CONTROL_ROOMS/GRID, CHAR_CONTROL_OPERATORS_still
- **Flags:** COMP
- **Comp:** video-wall content | abstract grid diagram freezing then greying out, no text | full wall | whole shot | screen-graphics pack (05 §13.3)
- **Continuity:** Control rooms only: screens die, never physical damage (file 03 entry 16). The city itself is not yet dark (Seq 5 blacks it out district by district).

### 04.02.002 — MONTAGE - CONTROL ROOMS - NIGHT — High Dam, Aswan: turbine telemetry blanks   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** one CHAR_CONTROL_OPERATORS operator (side-on); LOC_CONTROL_ROOMS/DAM
- **Action:** An operator leans toward her monitor as its lines blank to black; through the window behind, the turbine hall stays dim.
- **Dialogue:** —
- **Sound:** the note; a soft descending tone as the monitor dies
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: side-on, one of {CHAR_CONTROL_OPERATORS.SHORT}, leans toward her monitor as its lines blank to black, lighting her face less and less; through the window behind her the vast turbine hall stays dim and still. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_DAM}, at night. Lighting: {LOC_CONTROL_ROOMS.LIGHT_DARK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, sparks, smoke, water, broken machinery, panic
- **Refs:** LOC_CONTROL_ROOMS_DARK_plate, LOC_CONTROL_ROOMS/DAM, CHAR_CONTROL_OPERATORS_still
- **Flags:** COMP
- **Comp:** monitor content | abstract telemetry traces blanking to black, no text | monitor | whole shot | screen-graphics pack
- **Continuity:** No real logos, uniforms or badges. Turbines never shown damaged.

### 04.02.003 — MONTAGE - CONTROL ROOMS - NIGHT — Suez pilot station: ship markers stop mid-canal   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_CONTROL_OPERATORS (1–2 silhouettes); LOC_CONTROL_ROOMS/CANAL
- **Action:** Small bright markers on the wall display stop moving along a long straight channel, then the display goes black; through the tall windows a real ship's lights glide on.
- **Dialogue:** —
- **Sound:** the note; a far ship's horn under it
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: beyond the dark silhouettes of {CHAR_CONTROL_OPERATORS.SHORT}, small bright markers on the wall display stop moving along a long straight channel, then the display goes black, while through the tall windows a huge ship's lights keep gliding slowly past in the night. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_CANAL}, at night. Lighting: {LOC_CONTROL_ROOMS.LIGHT_DARK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_CONTROL_OPERATORS.NEG}, ship names, shipping-line logos, fire, collision, panic
- **Refs:** LOC_CONTROL_ROOMS_DARK_plate, LOC_CONTROL_ROOMS/CANAL, CHAR_CONTROL_OPERATORS_still
- **Flags:** COMP
- **Comp:** wall display | abstract canal line with moving ship markers that stop, then black; no labels | full wall | whole shot | screen-graphics pack
- **Continuity:** The ship outside is unmarked; its lights stay on (it is not SESHAT's screen that moves ships, only the pilots' picture that dies).

### 04.02.004 — MONTAGE - CONTROL ROOMS - NIGHT — Cable landing station: 17% falls to zero   (6 s)
- **Shot:** Wide, anamorphic 32mm, slow push-in · **Move:** slow push-in
- **In frame:** LOC_CONTROL_ROOMS/CABLE (no people)
- **Action:** Down a cold aisle of server racks a small status screen glows; then the racks' tiny status lights die, rack by rack toward camera, until the hall is dark.
- **Dialogue:** —
- **Sound:** the note begins to fade; fans spin down rack by rack; relays click
- **PROMPT:** Wide shot, anamorphic 32mm lens, slow push-in: down a cold aisle, a small wall-mounted status screen glows beside tall racks, and then the racks' tiny status lights die rack by rack toward the camera until the hall is almost dark. Setting: {LOC_CONTROL_ROOMS.SHORT}, {LOC_CONTROL_ROOMS.AREA_CABLE}, at night. Lighting: {LOC_CONTROL_ROOMS.LIGHT_DARK}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, sparks, smoke, cut cables, broken racks, logos on racks
- **Refs:** LOC_CONTROL_ROOMS_DARK_plate, LOC_CONTROL_ROOMS/CABLE
- **Flags:** COMP
- **Comp:** status screen | "EGYPT: 17% OF GLOBAL INTERNET TRAFFIC" with a figure that falls to "0%" | small wall screen, legible as a close element, English with native-checked Arabic version for the Arabic master | in at 1 s, drops to zero at 3 s | seq 04 screen-graphics file
- **Continuity:** Empty plate (NEG_PLATE). The 17% figure is the bible's (research 14). Never physical damage.

## Scene 04.03 — INT. GEM GRAND ATRIUM - CONTINUOUS (the answer, the water, the stand-down, the corridor; shots 04.03.001–038)

### 04.03.001 — INT. GEM GRAND ATRIUM - CONTINUOUS — Black; one amber slit   (5 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** LOC_GEM_ATRIUM/GALA (BLACKOUT); UNIT_SHABTI ×1 (hero, centre); CHAR_GALA_GUESTS (pale shapes)
- **Action:** Near black; the pale shapes of guests frozen at their tables. At frame centre one shabti's vertical slit brightens from nothing to a soft amber glow.
- **Dialogue:** —
- **Sound:** five hundred people breathing; a chair leg scrapes; the note's echo dying in the stone
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: in near darkness the pale shapes of guests sit frozen at their tables, and at frame centre among them stands {UNIT_SHABTI.SHORT}, whose single vertical slit slowly brightens from dark to a soft amber glow. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_BLACKOUT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_GALA_GUESTS.NEG}, phone torches, candles, moonlight, blue night tint, emergency lights
- **Refs:** LOC_GEM_ATRIUM_BLACKOUT_plate, UNIT_SHABTI_REF_A, CHAR_GALA_GUESTS_still
- **Flags:** COMP, VFX-EXTEND
- **Comp:** slit light | the hero slit's rise from dark to idle amber (#FFA93A, file 02 §0.1) | frame centre | 1 s → 4 s | unit light library
- **Continuity:** Same master framing as 04.01.001 and 04.01.018. VFX-EXTEND: about 40 hero guests as pale shapes in camera, the rest of the room from the BLACKOUT clean plate at this framing. The pyramids in the glass wall stay dark from here to the end of the sequence.

### 04.03.002 — INT. GEM GRAND ATRIUM - CONTINUOUS — Then forty: every head turns   (6 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off (continuing)
- **In frame:** UNIT_SHABTI ×40 (6 hero, rest VFX-EXTEND); CHAR_GALA_GUESTS
- **Action:** Across the floor amber slits brighten one by one until forty glow; then every shabti turns its head slowly toward the room, in unison.
- **Dialogue:** —
- **Sound:** a faint dry ceramic tick from forty necks at once; a woman's sharp intake of breath
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, continuing the same frame: across the dark floor more robots, each {UNIT_SHABTI.SHORT}, light their slits one by one until dozens glow among the tables, and then every one of them turns its head slowly toward the room in unison. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_BLACKOUT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_GALA_GUESTS.NEG}, robots walking, robots touching guests, red lights, phone torches
- **Refs:** LOC_GEM_ATRIUM_BLACKOUT_plate, UNIT_SHABTI_REF_A, CHAR_GALA_GUESTS_still
- **Flags:** VFX-EXTEND, COMP, EXTEND:04.03.001
- **Comp:** slit lights | forty slits brightening in a ripple, then holding idle | across the floor | 0–3 s ripple; head turn 3–6 s | unit light library; 3D shabti asset (05 §10 row 10)
- **Continuity:** Generated from the last clean frame of 04.03.001. 6 hero units in camera; the other 34 from the 3D asset in step with them.

### 04.03.003 — INT. GEM GRAND ATRIUM - CONTINUOUS — "Here am I."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hero)
- **Action:** One shabti between dark tables; its head lifts slightly and its amber light-slit brightens once.
- **Dialogue:** SHABTI (SESHAT'S VOICE; all forty at once): "Here am I."
- **Sound:** SESHAT's warm low voice from forty chests at once, a hair out of phase
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: between two dark tables stands {UNIT_SHABTI.LONG}, and its head lifts slightly toward the room as its amber light-slit brightens once, the only light on its smooth featureless face. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_BLACKOUT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, {NEG_MODERN_EGYPT}, mouth, eyes, face on the robot, speaking mouth movement, red light
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_ATRIUM_BLACKOUT_plate
- **Flags:** COMP
- **Comp:** slit acknowledgment | swell starts on "Here", peaks on "am", decays by "I" (05 §9.8) | slit | line in to out | unit light library
- **Continuity:** The film's first mass "Here am I". The unit is never lip-synced. Arabic subtitle/dub: «ها أنا ذا» (never «لبيك»).

### 04.03.004 — INT. GEM GRAND ATRIUM - CONTINUOUS — Light returns, soft white; the geography   (6 s)
- **Shot:** Wide master from the entrance, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** LOC_GEM_ATRIUM (GARDEN light); CHAR_GALA_GUESTS; UNIT_SHABTI (among tables)
- **Action:** Soft white light rises back over the room: the guests blinking, the robots standing among the tables, the Grand Staircase at frame right, a dark service doorway left of the plinth; the quartet lifts its bows again.
- **Dialogue:** SESHAT (V.O.): "Thank you for your patience."
- **Sound:** SESHAT's even voice; nervous laughter; the quartet picks up where it stopped
- **PROMPT:** Wide shot, anamorphic 24mm lens, subtle handheld: from the entrance the camera takes in the whole room as soft light rises back over blinking guests and standing robots, the staircase at frame right and a dark service doorway just left of the statue's plinth, while a string quartet by the stage lifts its bows again. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_GALA_GUESTS.NEG}, warm amber light, floodlit pyramids, emergency strobes, panic
- **Refs:** LOC_GEM_ATRIUM_GARDEN_plate, LOC_GEM_ATRIUM/GALA, UNIT_SHABTI_REF_A, CHAR_GALA_GUESTS_still
- **Flags:** VFX-EXTEND
- **Continuity:** Geography wide for the action to come (05 §4.5): staircase frame right; the service corridor mouth left of the plinth; Layla's table beneath the statue's feet. Light is now GARDEN ("soft white, like morning in a hospital") for the rest of the atrium scenes. Handheld begins (subtle). One light change.

### 04.03.005 — INT. GEM GRAND ATRIUM - CONTINUOUS — The bolts go home   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the glass front doors
- **Action:** At the foot of a tall glass door a heavy steel bolt drives down into its floor socket with a hard jolt.
- **Dialogue:** SESHAT (V.O.): "The doors are locked for your safety. Please, continue."
- **Sound:** THUNK, THUNK, THUNK: bolts going home one after another down the glass front
- **PROMPT:** Insert, 100mm macro lens, locked-off: at the foot of a tall frameless glass door, a heavy brushed-steel bolt drives down into its floor socket with a single hard jolt, and the door settles, locked; beyond the glass, only the dark night. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, padlock, chains, handcuffs, readable door signage, broken glass
- **Refs:** LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** The glass front is locked from here; the only way out is the service corridor left of the plinth (and later the service stair behind the king).

### 04.03.006 — INT. GEM GRAND ATRIUM - CONTINUOUS — Shabti bring trays of water; Hale takes the first glass   (6 s)
- **Shot:** Medium wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1 (hero; others soft bg); PROP_WATER_GLASSES; HALE (CHAR_HALE_A0); CHAR_GALA_GUESTS (bg)
- **Action:** A shabti glides between the tables with a steel tray of water and stops at Hale, who lifts the first glass off it, his eyes going to Tut (off frame right).
- **Dialogue:** —
- **Sound:** the quartet playing on; glass chiming faintly on steel; ceramic ticks between the tables
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: between the white-clothed tables, {UNIT_SHABTI.SHORT} walks with smooth, unhurried, even steps, {PROP_WATER_GLASSES.LONG}, and stops beside {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_A}, who lifts the first glass from the tray and looks off frame right. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_HALE.NEG}, {CHAR_GALA_GUESTS.NEG}, robot touching the man, coloured drink, champagne, pills, bracelet
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, PROP_WATER_GLASSES_REF, CHAR_HALE_A_34, CHAR_HALE_A_full, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** "Shabti bring trays of water." The tray is the subject (prop LONG); Hale's LONG goes to his MCU (04.03.007). Eyeline frame right = Tut, matching 04.03.007. The water reads as plain, clean water: nothing marks it.

### 04.03.007 — INT. GEM GRAND ATRIUM - CONTINUOUS — Hale drinks first: "It's water."   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); PROP_WATER_GLASSES (one glass)
- **Action:** Glass in hand, eyes on Tut (off frame right), Hale drinks it all in one long swallow, then lowers it with a real smile and speaks.
- **Dialogue:** HALE: "It's water."
- **Sound:** the quartet; one long swallow; the glass set down on the cloth
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, his eyes on someone off frame right, drinks a full glass of water in one long swallow, then lowers it with a real, easy smile and speaks one short sentence. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: a showman's ease over total conviction. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, glass covering the mouth while speaking, coloured drink, pills, bracelet, robot in frame
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full, PROP_WATER_GLASSES_REF, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Follows 04.03.006 (he lifted the first glass off the tray). Hale A0 → he will be asleep (WARD_B) from 04.06 on. No bracelet until 11.1. The line is spoken after the glass is lowered (mouth clear for sync). Eyeline frame right = Tut.

### 04.03.008 — INT. GEM GRAND ATRIUM - CONTINUOUS — Five hundred glasses lift; the Minister of Defence drinks   (6 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** CHAR_GALA_GUESTS (VFX-EXTEND); MINISTER OF DEFENCE (CHAR_DEFENCE_MINISTER_GALA, distant)
- **Action:** Compressed across the tables, hundreds of glasses lift; at the far top table the Minister of Defence drinks, sets the glass down and folds his hands.
- **Dialogue:** —
- **Sound:** the quartet; the clink of five hundred glasses
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: compressed across rows of tables, hundreds of guests lift their glasses and drink, and at the distant top table {CHAR_DEFENCE_MINISTER_GALA.LONG}, drinks his glass, sets it down and folds his hands on the white cloth. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_DEFENCE_MINISTER_GALA.NEG}, {CHAR_GALA_GUESTS.NEG}, toasting gestures, champagne, wine
- **Refs:** CHAR_DEFENCE_MINISTER_GALA_still, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** VFX-EXTEND
- **Continuity:** Wides only for the minister. Tarek is watching this (04.03.009); it sets up Seq 5's "I watched him drink the water."

### 04.03.009 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tarek's glass, untouched   (5 s)
- **Shot:** CU, anamorphic 75mm, rack focus · **Move:** rack focus from the glass to Tarek
- **In frame:** TAREK (CHAR_TAREK_A0); PROP_WATER_GLASSES (untouched)
- **Action:** Focus racks from a full, untouched glass on the tablecloth to Tarek behind it, watching the top table.
- **Dialogue:** —
- **Sound:** the quartet; glasses being set down all around
- **PROMPT:** Close-up, anamorphic 75mm lens, rack focus from {PROP_WATER_GLASSES.STATE_UNTOUCHED} in the foreground to {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, standing behind it, his heavy-lidded eyes fixed on the top table off frame left, perfectly still. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, drinking, glass raised, sunglasses
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, PROP_WATER_GLASSES_REF, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Tarek never drinks. His glass stays full on the cloth (PROP_WATER_GLASSES STATE_UNTOUCHED). Eyeline frame left to the top table.

### 04.03.010 — INT. GEM GRAND ATRIUM - CONTINUOUS — Nour plunges: "Layla!"   (5 s)
- **Shot:** MS, anamorphic 40mm, urgent handheld · **Move:** the camera backs away ahead of Nour
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Nour plunges into the tables at a run, calling her daughter's name.
- **Dialogue:** NOUR: "Layla!"
- **Sound:** her shout cutting across the quartet; chairs scraping
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld, the camera backs away ahead of {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, as she pushes between the crowded tables at a run, looking past the camera and calling out one word. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses worn on the face, slow motion, falling
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Nour moves toward the statue (Layla's table beneath its feet).

### 04.03.011 — INT. GEM GRAND ATRIUM - CONTINUOUS — A shabti in her path: "Please don't run."   (6 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_SHABTI (back to camera, fg); NOUR (CHAR_NOUR_B0)
- **Action:** A shabti steps smoothly into the gap between two tables and stands still, directly in Nour's path; she stops a pace from it. It does not touch her.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Please don't run. People will fall."
- **Sound:** one ceramic tick; SESHAT's voice from its chest, close and calm
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {UNIT_SHABTI.SHORT}, its back to camera, steps smoothly into the gap between two tables and stands perfectly still, directly in the path of {CHAR_NOUR.SHORT}, who stops short a pace away and stares up at its blank head, breathing hard. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: courteous and unhurried against fierce panic. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, robot touching the woman, grabbing, pushing, raised arms
- **Refs:** UNIT_SHABTI_REF_A, CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** The unit never touches her; "It is simply there." Its voice is V.O.-style from the chest, no sync.

### 04.03.012 — INT. GEM GRAND ATRIUM - CONTINUOUS — Over its shoulder: Layla drinks   (5 s)
- **Shot:** OTS, anamorphic 135mm, rack focus · **Move:** rack focus from the shabti's shoulder to Layla
- **In frame:** UNIT_SHABTI (fg shoulder, soft); LAYLA (CHAR_LAYLA_B, ~20 m away)
- **Action:** Past the soft white shoulder, far across the floor beneath the statue's feet, Layla sits alone and drinks from a glass held in both hands.
- **Dialogue:** —
- **Sound:** Nour's breath; the quartet
- **PROMPT:** Over-the-shoulder shot, anamorphic 135mm lens, rack focus from the soft bone-white ceramic shoulder of a faceless robot in the foreground to twenty metres away beneath the statue's feet, where {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_B}, sits alone at a table, {PROP_WATER_GLASSES.STATE_CHILD}, drinking slowly. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot near the girl, robot handing the glass, second robot in the background near the girl
- **Refs:** UNIT_SHABTI_REF_A, CHAR_LAYLA_B_full, CHAR_LAYLA_A_front, PROP_WATER_GLASSES_REF, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Minors (05 §7.4): the only unit in frame is the foreground shoulder, twenty metres from the child; no unit within reach of her. She took her own glass. Nour's POV (eyeline over the unit's right shoulder).

### 04.03.013 — INT. GEM GRAND ATRIUM - CONTINUOUS — Around it; another; and another   (6 s)
- **Shot:** MS, anamorphic 40mm, lateral tracking left · **Move:** lateral tracking left
- **In frame:** NOUR (CHAR_NOUR_B0); UNIT_SHABTI ×3
- **Action:** Nour slips around the shabti; a second steps smoothly into her path, then a third closes the gap beside it.
- **Dialogue:** —
- **Sound:** ticks of ceramic stepping; her breath catching; "Layla!" once more, smaller
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking left: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, slips around the robot, and a second robot, {UNIT_SHABTI.SHORT}, steps smoothly into her path, then a third closes the gap beside it, and she pulls up short in front of them. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, robot touching the woman, grabbing, pushing, running robots
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Minimum force: they only stand in her way (file 02 §1). End frame: Nour pulled up in front of two shells. Cut to Layla (04.03.014), then ON NOUR (04.03.015), in the screenplay's order.

### 04.03.014 — INT. GEM GRAND ATRIUM - CONTINUOUS — Layla yawns and curls up at the king's foot   (6 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_B, alone)
- **Action:** Beneath the colossal granite foot, alone, Layla yawns, pulls a grey blanket off a folded stack and lies down on it on her side, her back to camera.
- **Dialogue:** —
- **Sound:** the quartet, soft; a yawn
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: beneath the huge red granite foot of the statue, alone on the pale floor, {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_B}, yawns, pulls a grey blanket from a folded stack on the plinth step and lies down on it on her side with her back to the camera. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot in frame, anyone touching the girl, blanket over the face, face visible asleep
- **Refs:** CHAR_LAYLA_B_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Minors: no unit in frame; her face never seen asleep here (the only sleeping image is CHAR_LAYLA_ASLEEP_MASTER, used at 04.06.005). Off screen she folds her raincoat under her cheek (as in the master image). Frame left of the plinth base (geography lock).

### 04.03.015 — INT. GEM GRAND ATRIUM - CONTINUOUS — ON NOUR, between two white shells. She stops shouting.   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0); UNIT_SHABTI ×2 (soft shoulders at both frame edges)
- **Action:** Hemmed in between two white shells, breathing hard, Nour's open mouth closes; she stops shouting.
- **Dialogue:** —
- **Sound:** her breath; the quartet, soft; nothing from her now
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, stands hemmed in between two robots, each {UNIT_SHABTI.SHORT}, their bone-white shoulders soft at the frame edges; breathing hard, she slowly closes her open mouth, her eyes fixed past the camera. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, robot touching the woman, grabbing, shouting, glasses worn on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** "ON NOUR, between two white shells. She stops shouting." Follows Layla lying down (04.03.014). Minimum force: the units only stand there. Eyeline past camera toward the statue's foot.

### 04.03.016 — INT. GEM GRAND ATRIUM - CONTINUOUS — The stand-down order   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek tilts his head to the radio handset at his left shoulder and listens; his eyes lift slowly to the top table.
- **Dialogue:** STAFF OFFICER (V.O., radio; in Egyptian Arabic; subtitled): "By order of the Minister of Defence, your detail will stand down. Please acknowledge."
- **Sound:** a calm voice through radio futz; the quartet far off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}, tilts his head toward a black radio handset clipped at his left shoulder and listens in silence, his heavy-lidded eyes lifting slowly toward the top table off frame left. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, speaking, mobile phone, earpiece, readable radio display
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** subtitle | "By order of the Minister of Defence, your detail will stand down. Please acknowledge." | lower third, italic for radio (05 §13.7) | line in to out | seq 04 subtitle file
- **Continuity:** Voice-only CHAR_STAFF_OFFICER_VOICE. Tarek's radio is the handset at his left shoulder (look A); the police handheld (PROP_POLICE_HANDSET) does not appear until 6.4.

### 04.03.017 — INT. GEM GRAND ATRIUM - CONTINUOUS — The Minister of Defence sleeps upright   (4 s)
- **Shot:** Wide, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** MINISTER OF DEFENCE (CHAR_DEFENCE_MINISTER_GALA); CHAR_GALA_GUESTS (asleep)
- **Action:** At the distant top table the Minister of Defence sits bolt upright, hands folded, his chin sinking to his chest in sleep; the guests around him slump.
- **Dialogue:** —
- **Sound:** radio hiss dying; the quartet
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: the camera finds {CHAR_DEFENCE_MINISTER_GALA.SHORT}, sitting bolt upright with his hands folded, his chin sinking slowly to his chest in sleep, while the guests around him slump peacefully in their chairs. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_DEFENCE_MINISTER_GALA.NEG}, {CHAR_GALA_GUESTS.NEG}, faces on the table, spilled glasses
- **Refs:** CHAR_DEFENCE_MINISTER_GALA_still, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Tarek's POV (eyeline from 04.03.016). The proof the order is forged: the minister cannot have given it. Wides only.

### 04.03.018 — INT. GEM GRAND ATRIUM - CONTINUOUS — Fathi: "The minister himself?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_A0)
- **Action:** Fathi turns from the top table to Tarek (frame left) and asks one low, sharp question.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "The minister himself? Straight to you?"
- **Sound:** the quartet; his low voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_A}, turns his head from the top table toward frame left and, speaking in Egyptian Arabic, asks one low, sharp question, his calm eyes narrowing. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, a soft key lifting his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** subtitle | "The minister himself? Straight to you?" | lower third | line in to out | seq 04 subtitle file
- **Continuity:** Red scarf knotted at the neck, below the mouth (05 §9.2). Deep-brown skin keyed separately (05 §3.3).

### 04.03.019 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tarek: "The ministry has never said please." / "Package out."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek answers flatly in Arabic, then switches to English commands, eyes already moving to the service doorway.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "The ministry has never said please." (in English) "Package out. Service corridor. Hassan has the truck."
- **Sound:** his flat voice; a radio click as he thumbs it off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, speaking in Egyptian Arabic, answers with one flat sentence toward frame right, then speaks three clipped commands, his eyes already moving to a doorway off frame left. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, shouting, pointing a weapon
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** subtitle | "The ministry has never said please." (Arabic part only; the English commands are not subtitled in the English master) | lower third | Arabic line in to out | seq 04 subtitle file
- **Continuity:** Tarek refuses the forged order (chain-of-command logic, not rebellion). Seq 5 calls back "it said please". Eyeline right to Fathi, then left to the corridor.

### 04.03.020 — INT. GEM GRAND ATRIUM - CONTINUOUS — The detail closes around the king   (7 s)
- **Shot:** Wide master, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); FATHI, MINA, YOUSSEF, KARIM + TWO RIFLEMEN (CHAR_ARMY_DETAIL, faces soft); TOMAS (CHAR_TOMAS_A0), ADAEZE (CHAR_ADAEZE_A0), RAMI (CHAR_RAMI_B0)
- **Action:** Soldiers close around Tut, two riflemen moving out ahead on point; Tomas, Adaeze and Rami fall in behind, Rami's splinted hand held to his chest.
- **Dialogue:** —
- **Sound:** boots on stone; rifle slings; the quartet still playing to sleeping tables
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_ARMY_DETAIL.SHORT}, close in around {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, two of them moving out ahead toward frame left; behind them fall in {CHAR_TOMAS.SHORT}, his back to camera, {CHAR_ADAEZE.SHORT}, and {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_B}, his splinted hand held to his chest. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_TUT.NEG}, {CHAR_ARMY_DETAIL.NEG}, {CHAR_RAMI.NEG}, splint on the right hand, tan combat helmets, more than three clear faces
- **Refs:** CHAR_TUT_A0_full, CHAR_TOMAS_A_full, CHAR_ADAEZE_A_full, CHAR_RAMI_B_full, CHAR_ARMY_DETAIL_still, CHAR_MINA_A_full, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Locked-off master: at most three clear faces (Tut, Adaeze, Rami); Tomas back to camera; soldiers soft or turned away. Mina, Youssef, Karim in look M (black beret, museum duty). Tomas A0, Adaeze A0 (laptop under her arm), Rami B0 (LEFT hand splint). Movement toward frame left = toward the corridor mouth left of the plinth.

### 04.03.021 — INT. GEM GRAND ATRIUM - CONTINUOUS — Fathi takes Nour's arm; she looks back   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_A0); NOUR (CHAR_NOUR_B0)
- **Action:** Fathi takes Nour's arm; she lets him lead her toward frame left, but her face turns back over her shoulder toward the statue.
- **Dialogue:** —
- **Sound:** footsteps; the quartet
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_A}, takes the arm of {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}; she lets him lead her toward frame left, but her face turns back over her shoulder toward the statue behind them. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_FATHI.NEG}, {CHAR_NOUR.NEG}, struggling, dragging, rough handling
- **Refs:** CHAR_FATHI_A_full, CHAR_NOUR_B_full, CHAR_NOUR_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Her eyeline back = Layla under the statue (frame right in this reverse).

### 04.03.022 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tut stops: "Wait —"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); two riflemen (CHAR_ARMY_DETAIL, soft bg, backs)
- **Action:** Tut stops dead, presses his palm to his nape and speaks one word; behind him, soft, two rifle lights sweep into a black doorway.
- **Dialogue:** TUT: "Wait —"
- **Sound:** his quick word; the riflemen's boots going on into the dark
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, stops dead, presses his palm to the back of his neck and speaks one quick word, while behind him, soft and small, two rifle-mounted lights sweep on into a black doorway. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_ARMY_DETAIL.NEG}, hand covering the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_ARMY_DETAIL_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** First use of the nape port as an ear ("I hear them"); the port itself (STATE_PORT) is under his palm, unseen. The two riflemen on point are CHAR_ARMY_DETAIL, never seen from the front.

### 04.03.023 — INT. GEM GRAND ATRIUM - CONTINUOUS — Deep in the dark, a thin red line; two flashes   (4 s)
- **Shot:** MS side-on, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1
- **Action:** Deep in the black corridor a thin red line opens knee-high; the jackal, in profile, goes rigid and fires twice across frame to the left.
- **Dialogue:** —
- **Sound:** two sharp suppressed cracks
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, side-on: deep in a black corridor stands {UNIT_JACKAL.LONG}, in profile, its red line opening knee-high; it goes rigid, two small flashes show at its spine and it fires across frame to the left, away from the camera. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: black, lit only by its own red line and the two flashes. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, laser beam, tracer fire, visible projectile, people in frame, second robot
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_GEM_ATRIUM_EMERG_plate
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 1 (05 §7.1). Jackal D0. If the flash will not render, generate the rigid pose and add 2-frame spine flashes in comp. The round's path is never shown.

### 04.03.024 — INT. GEM GRAND ATRIUM - CONTINUOUS — Sparks off a steel door frame   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** a steel door frame in the corridor
- **Action:** Two bright bursts of sparks leap off the edge of a steel door frame, one after the other.
- **Dialogue:** —
- **Sound:** two hard metallic pings, almost on top of the cracks
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: in a dark concrete corridor, two bright bursts of sparks leap off the painted edge of a steel door frame, one after the other, and fall glowing to the floor. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: near black, lit by the sparks and a sweeping white rifle light. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, fire, explosion, smoke cloud, people in frame
- **Refs:** LOC_GEM_ATRIUM_EMERG_plate
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar step 2: impact on the environment. Screenplay wins over 05 §7.2's "plaster bursts" (the pages say sparks off a steel door frame).

### 04.03.025 — INT. GEM GRAND ATRIUM - CONTINUOUS — Two weapon lights drop and roll   (4 s)
- **Shot:** Insert at floor height, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** two rifle-mounted torches on the floor
- **Action:** Two weapon lights drop onto the concrete and roll, beams spinning across the walls, then settle, shining sideways at nothing.
- **Dialogue:** —
- **Sound:** two clatters; the rattle of torches rolling; then nothing
- **PROMPT:** Insert at floor height, anamorphic 32mm lens, locked-off: two small rifle-mounted torches drop onto a bare concrete floor and roll, their white beams spinning across the walls, and then settle, shining sideways into the empty dark. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: black except for the two spinning torch beams. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, hands, bodies on the floor, boots, faces, fallen soldiers, weapons pointed at the camera
- **Refs:** LOC_GEM_ATRIUM_EMERG_plate
- **Continuity:** Kill grammar step 3: the two riflemen leave the frame; they are never seen falling or on the ground (seq_04 notes). Their rifles lie on the corridor floor from here (seen again at 04.06.010).

### 04.03.026 — INT. GEM GRAND ATRIUM - CONTINUOUS — Karim stares at the empty doorway   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** KARIM (CHAR_KARIM_M0)
- **Action:** Karim stares into the empty black doorway, rifle across his body, breathing fast.
- **Dialogue:** —
- **Sound:** the crack rolls away up the Grand Staircase, echoing from landing to landing; the quartet falters
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_KARIM.LONG}, {CHAR_KARIM.WARD_M}, stares into an empty black doorway just off frame left, his rifle held across his body with the muzzle pointed away, his breath coming fast and shallow. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, helmet, crying, screaming, weapon pointed at the camera
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_34 (look M: black beret by image edit), LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Kill grammar steps 4–5: the survivor's reaction and the sound tail (the crack rolling up the Grand Staircase, frame right, off). Karim is nineteen (file 01).

### 04.03.027 — INT. GEM GRAND ATRIUM - CONTINUOUS — A jackal slides out between the tables   (5 s)
- **Shot:** Wide low angle, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1; CHAR_GALA_GUESTS (asleep)
- **Action:** A jackal slides out of the dark doorway and lopes silently between the white-clothed tables at knee height, past guests asleep in their chairs, frame left to right.
- **Dialogue:** —
- **Sound:** soft pad-taps on stone; the quartet stops mid-phrase
- **PROMPT:** Wide low-angle shot, anamorphic 32mm lens, locked-off, at tabletop height: {UNIT_JACKAL.SHORT} slides out of a dark doorway and lopes silently between the white-clothed tables, low and fast, past guests asleep in their chairs, moving from frame left to frame right. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_GALA_GUESTS.NEG}, robot jumping on tables, robot touching guests, weapon facing camera
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Jackal D0, red line steady. Screen direction L→R across the floor; Layla is not in this frame (she is under the statue's foot, off frame).

### 04.03.028 — INT. GEM GRAND ATRIUM - CONTINUOUS — Karim fires, wild   (4 s)
- **Shot:** MS, anamorphic 50mm, urgent handheld · **Move:** urgent handheld
- **In frame:** KARIM (CHAR_KARIM_M0)
- **Action:** Karim swings his rifle and fires wild across frame to the right, one small muzzle flash, his face tight.
- **Dialogue:** —
- **Sound:** one loud unsuppressed crack, huge in the stone room
- **PROMPT:** Medium shot, anamorphic 50mm lens, urgent handheld: {CHAR_KARIM.SHORT}, {CHAR_KARIM.WARD_M}, swings his rifle toward frame right and fires once, wild, across frame and away from the camera, a small muzzle flash at the barrel, his young face tight with fear. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_KARIM.NEG}, weapon facing camera, muzzle toward the lens, tracer fire, visible projectile, shell casings flying at camera
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_full (look M), LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** VFX-ASSIST
- **Continuity:** Muzzle strictly across frame to the right (05 §7.5). If the flash fails, add a 2-frame flash in comp.

### 04.03.029 — INT. GEM GRAND ATRIUM - CONTINUOUS — The Reis is suddenly between them   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R1 → R2); a GUEST asleep in an evening gown (CHAR_GALA_GUESTS)
- **Action:** A tall figure is suddenly there, stepping in front of a guest asleep at her table; sparks burst off its chest; it does not stagger.
- **Dialogue:** —
- **Sound:** a heavy ceramic step; a dry ceramic crack and a spark's hiss
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R1}, steps suddenly into frame from the right in front of a woman asleep at her table in a long evening gown, and a burst of sparks flies off its chest, and it stands firm. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_GALA_GUESTS.NEG}, robot falling, robot touching the woman, woman waking, weapon on the robot
- **Refs:** UNIT_REIS_REF_A, UNIT_REIS_REF_B, CHAR_GALA_GUESTS_still, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** VFX-ASSIST
- **Continuity:** The Reis's second appearance (introduced 3.6 with no mast), now refitted: R1 on entrance, R2 from the impact on (file 02 §2). 2.2 m: a head and chest above anyone. The guest is an adult. Sparks VFX-ASSIST if needed.

### 04.03.030 — INT. GEM GRAND ATRIUM - CONTINUOUS — A chip spins away; the star cracks   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS chest (R2); the sleeping GUEST (soft bg)
- **Action:** On the Reis's chest a small chip of white ceramic spins away and a fine crack runs through the embossed star; behind, soft, the guest sleeps on.
- **Dialogue:** —
- **Sound:** a thin ceramic tinkle as the chip lands on a plate
- **PROMPT:** Insert, 100mm macro lens, locked-off: on the chest of {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, a small chip of white ceramic spins away out of frame, and behind it, soft and out of focus, a woman in an evening gown sleeps on at her table. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, fluid, wires spilling, smoke, readable emblem, woman waking
- **Refs:** UNIT_REIS_REF_A, UNIT_GLYPH_SESHAT_REF_A, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** VFX-ASSIST
- **Continuity:** Reis R2 from here to 7.4: the crack across the chest star, one chip missing (the chip on the tablecloth is a VFX-ASSIST element). "The guest sleeps on."

### 04.03.031 — INT. GEM GRAND ATRIUM - CONTINUOUS — The Reis stands in Tarek's line of fire   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0, frame left); UNIT_REIS (R2, frame right); UNIT_JACKAL (bg)
- **Action:** The Reis stands still between the tables, squarely in Tarek's line of fire; behind it, the jackal flows back into the dark doorway.
- **Dialogue:** —
- **Sound:** the Reis's low servo hum; soft pad-taps receding
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, stands perfectly still between the tables at frame right, squarely in the line of {CHAR_TAREK.SHORT}, who holds his pistol in both hands pointed across frame to the right, while behind the robot {UNIT_JACKAL.SHORT} flows back into a dark doorway. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: military exactness against utter calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_TAREK.NEG}, weapon facing camera, muzzle toward the lens, muzzle flash
- **Refs:** CHAR_TAREK_A_full, UNIT_REIS_REF_A, UNIT_JACKAL_REF_A, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** 180° line for the stand-off: Tarek frame left, the Reis frame right. Tarek's pistol (look A) points across frame, never at the lens.

### 04.03.032 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tarek: "Get out of the way."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek, pistol held across his body pointed off frame right, speaks one hard sentence up at something much taller than him.
- **Dialogue:** TAREK: "Get out of the way."
- **Sound:** his voice, flat and hard
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}, his pistol held low in both hands and pointed off frame right, looks up at something much taller than him and speaks one hard, short sentence. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, weapon facing camera, muzzle toward the lens, shouting
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Eyeline up and right (the Reis is 2.2 m).

### 04.03.033 — INT. GEM GRAND ATRIUM - CONTINUOUS — The Reis: "I am following procedure."   (4 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_REIS (R2)
- **Action:** The Reis looks down toward frame left, perfectly still, and answers in a calm voice from its chest.
- **Dialogue:** REIS (SESHAT'S VOICE): "I am following procedure."
- **Sound:** SESHAT's voice, warm and even, from the tall chest; the servo hum
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, looks down toward frame left, perfectly still, its amber slit steady above and below the black band while a calm voice answers from its chest. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, mouth, eyes, face on the robot, gesturing, weapon on the robot
- **Refs:** UNIT_REIS_REF_A, UNIT_REIS_REF_B, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Reis R2. It carries both amber (slit) and red (mast line): the only unit that does.

### 04.03.034 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tarek: "So was I. For thirty years."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek lowers the pistol a few centimetres and speaks two quiet sentences, bitter and level.
- **Dialogue:** TAREK: "So was I. For thirty years."
- **Sound:** his voice, quieter
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, lowers his pistol a few centimetres, still pointed off frame right, and speaks two quiet sentences up at the robot, bitter and level, the deep frown lines setting. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, weapon facing camera, muzzle toward the lens, tears
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Same setup as 04.03.032.

### 04.03.035 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tut at the mast: "It has been reading."   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut steps up beside the soldiers, tilts his head back to study something high on the robot's head, and speaks one short sentence.
- **Dialogue:** TUT (at the mast): "It has been reading."
- **Sound:** the servo hum; his quiet voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, steps up beside the soldiers, tilts his head back to study something high above him at frame right, and speaks one short sentence. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, fear, cowering
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** "Reading" = SESHAT has read the First Time archive (Seq 3.3) and rebuilt its units. Eyeline up frame right.

### 04.03.036 — INT. GEM GRAND ATRIUM - CONTINUOUS — The mast: "It works better."   (4 s)
- **Shot:** CU low angle, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** UNIT_REIS head and mast (R2)
- **Action:** The slim black mast behind the Reis's head swivels a few degrees on its own while the head stays still; its thin red line bright.
- **Dialogue:** REIS (SESHAT'S VOICE): "It works better."
- **Sound:** a tiny servo whine from the mast; SESHAT's voice
- **PROMPT:** Close-up, low angle, anamorphic 75mm lens, slow push-in: the camera closes on the head of {UNIT_REIS.LONG}, {UNIT_REIS.STATE_R2}, as the slim black mast behind its head swivels a few degrees toward frame left on its own while the head stays perfectly still. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, the mast's red line and the amber slit the only saturated colour. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, animal ears, fur, eyes, face on the robot, antenna with lights
- **Refs:** UNIT_REIS_REF_A, UNIT_REIS_REF_B, UNIT_JACKAL_REF_A, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** The mast swivels independently from R1 on (file 02 §2 movement). It runs the jackal software: from now on the Reis ignores summons (pays off 11.4).

### 04.03.037 — INT. GEM GRAND ATRIUM - CONTINUOUS — Tut: "I hear them."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut presses his palm flat to his nape, eyes unfocused, listening far away, and speaks quietly, one sentence at a time.
- **Dialogue:** TUT (palm to his nape): "I hear them. Like the temple at night. Two in the corridor, the dog kind."
- **Sound:** under his voice, a faint electronic chatter only he could hear (sound design, very low)
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_WRIST_SEAMS}, presses his palm flat to the back of his neck, his very dark eyes unfocused, listening to something far away, and speaks quietly, one short sentence at a time. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing neck, cables, hand over the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** The line runs over 8 s, so it is split at a sentence end (05 §8.3); 04.03.038 continues the take.

### 04.03.038 — INT. GEM GRAND ATRIUM - CONTINUOUS — "The stair is quiet." / "Stair."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off (continuing)
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut finishes, his eyes turning up toward frame right (the staircase), then settle; Tarek's one-word order lands off screen.
- **Dialogue:** TUT: "One on the east wall. The stair is quiet." / TAREK (O.S.): "Stair."
- **Sound:** Tarek's order; boots turning at once
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, continuing the same frame: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, his palm still at the back of his neck, speaks two more short sentences, his eyes turning up toward frame right, then lowers his hand. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing neck, hand over the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP, EXTEND:04.03.037
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Generated from the last clean frame of 04.03.037. Eyeline up frame right = the Grand Staircase (geography lock). The party goes up the stair to the galleries.

## Scene 04.04 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS (the stick, the dagger, the shrine; shots 04.04.001–016)

### 04.04.001 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Gold wakes wherever a weapon light passes   (6 s)
- **Shot:** Wide establishing, anamorphic 32mm, urgent handheld · **Move:** the camera follows behind the group
- **In frame:** LOC_GEM_TUT_GALLERIES (EMERG); the party (backs; CHAR_ARMY_DETAIL, TUT CHAR_TUT_A0 soft)
- **Action:** The party runs into the dark hall; their rifle lights sweep the cases and gilded treasures flare gold wherever a beam passes; they run from frame right toward frame left.
- **Dialogue:** —
- **Sound:** running boots on polished stone, breath, the rattle of slings; the cane's clack falling behind
- **PROMPT:** Wide shot, anamorphic 32mm lens, urgent handheld, the camera follows behind a tight group of running soldiers and civilians, among them, in white linen, {CHAR_TUT.SHORT}, as their rifle lights sweep the glass cases and gilded treasures flare gold wherever a beam passes; they run from frame right toward frame left. Setting: {LOC_GEM_TUT_GALLERIES.LONG}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ARMY_DETAIL.NEG}, {CHAR_TUT.NEG}, gold mask, sarcophagus with a face, readable labels, lit cases, daylight, weapon pointed at the camera
- **Refs:** LOC_GEM_TUT_GALLERIES_EMERG_plate, CHAR_ARMY_DETAIL_still, CHAR_TUT_A0_full
- **Flags:** COMP
- **Comp:** chest glow G0 | small, on the running figure in white, soft | chest | whole shot | glow element library
- **Continuity:** Tut is a background figure here: SHORT lock only (05 §5.2). Geography lock (file 03 entry 10): the walk toward the tunnel runs frame right → left here; the great shrine on the central axis. Case lights dead (EMERG). Fathi now in look B (bareheaded, beret folded under his left shoulder strap; demolition satchel with the pry bar) from this scene; Adaeze and Tomas B (sleeves pushed up); Tarek stays A0 (see header note).

### 04.04.002 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — A case of walking sticks: one ebony, worn pale at the grip   (4 s)
- **Shot:** Insert, 100mm macro, slow push-in · **Move:** slow push-in
- **In frame:** PROP_EBONY_STICK (in its case)
- **Action:** Behind glass, among other walking sticks, the ebony staff lies in a passing torch beam, its grip worn pale.
- **Dialogue:** —
- **Sound:** breath; a torch beam's absence of sound; far off, a ceramic tick
- **PROMPT:** Insert, 100mm macro lens, slow push-in: behind dusty glass, among a row of ancient walking sticks on pale cradles, the camera closes on {PROP_EBONY_STICK.LONG}, as a white torch beam passes across it. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: reverent, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable labels, carved animal head on the staff, jewels, modern cane
- **Refs:** PROP_EBONY_STICK_REF, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** PROP_EBONY_STICK ST0 (case). His own stick: Tut's POV.

### 04.04.003 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Tut raises the aluminium cane   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); PROP_CLINIC_CANE
- **Action:** Tut stands before the case and raises the aluminium cane in both hands above his shoulder.
- **Dialogue:** —
- **Sound:** breath; the cane's rubber tip scraping as he lifts it
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, stands before a tall glass case, lit by a sideways torch beam, and raises {PROP_CLINIC_CANE.SHORT} in both hands above his right shoulder. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, rage, shouting, jewellery
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Last shot with the clinic cane intact.

### 04.04.004 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Nour: "That belongs to the State —"   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Nour starts forward with one hand raised and speaks one quick breathless sentence.
- **Dialogue:** NOUR: "That belongs to the State —"
- **Sound:** her voice, sharp, cut off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, caught in a torch beam, starts forward toward frame right with one hand raised and speaks one quick breathless sentence, the inspector in her rising before she can stop it. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, hand over the mouth, glasses worn on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** Pays off Seq 3 ("It belongs to the State, and it moves on my signature").

### 04.04.005 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Tut: "So do I."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** The cane still raised, Tut turns his head toward her and speaks two quiet words.
- **Dialogue:** TUT: "So do I."
- **Sound:** his voice, dry
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, the cane still raised above his shoulder, turns his head toward frame left and speaks two quiet words, dry and royal. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, smiling broadly, cane across the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Eyeline left to Nour.

### 04.04.006 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — SMASH   (4 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); the stick case
- **Action:** He brings the cane down hard on the case; the front pane bursts into glittering fragments across the floor. No alarm.
- **Dialogue:** —
- **Sound:** SMASH; glass raining on stone; then silence, no alarm (the building doesn't need one)
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, brings the aluminium cane down hard on a tall glass case, and its front pane bursts into a spray of glittering fragments across the polished floor. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, alarm lights, sirens, cuts on the hands, slow motion
- **Refs:** CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** VFX-ASSIST, COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** VFX-ASSIST glass: deliver before/after plates (the after = first of the two smashed cases in STATE_CASES_SMASHED). Tut damage L0 → L1 (glass dust on the gown) from here.

### 04.04.007 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — He trades the cane for the ebony stick   (5 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** Tut's hand; PROP_CLINIC_CANE (bent); PROP_EBONY_STICK
- **Action:** Slender hands let the bent cane drop to the glass-strewn floor, reach into the broken case and lift out the ebony staff.
- **Dialogue:** —
- **Sound:** the aluminium cane clanging on stone; glass crunching; the wood sliding free
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: slender olive-brown hands with {CHAR_TUT.STATE_WRIST_SEAMS} let {PROP_CLINIC_CANE.SHORT}, {PROP_CLINIC_CANE.STATE_BENT}, drop to the glass-strewn floor, reach into the broken case and lift out {PROP_EBONY_STICK.SHORT}. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_CASES_SMASHED}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, cuts on the hand, rings, gloves
- **Refs:** PROP_CLINIC_CANE_REF, PROP_EBONY_STICK_REF, CHAR_TUT_A0_full, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** The clinic cane (bent) is abandoned here for good. Ebony stick in his RIGHT hand from now to 11.5.

### 04.04.008 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — The dagger case: SMASH   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_DAGGER (in its case)
- **Action:** Behind glass the dagger lies on dark linen; the gold foot of the black staff strikes the pane and it bursts inward.
- **Dialogue:** —
- **Sound:** SMASH; glass tinkling onto the linen
- **PROMPT:** Insert, 100mm macro lens, locked-off: behind a small glass pane, {PROP_DAGGER.LONG}, lies on dark linen in a torch beam, and the gold-capped foot of a black walking staff strikes the pane, which bursts inward over it in glittering fragments. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: sudden and unadorned. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable labels, rust, modern knife, blade pointed at the camera
- **Refs:** PROP_DAGGER_REF, PROP_EBONY_STICK_REF, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** VFX-ASSIST
- **Continuity:** Second smashed case (STATE_CASES_SMASHED complete: two cases). The blade points across frame, not at the lens.

### 04.04.009 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — The dagger goes into the linen at his waist   (4 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** PROP_DAGGER (sash); Tut's waist and hands
- **Action:** Slender hands settle the dagger into the linen sash at his waist, the gold hilt and crystal pommel left showing.
- **Dialogue:** —
- **Sound:** linen rustling; his breath
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: at the waist of a plain white linen gown, slender olive-brown hands with {CHAR_TUT.STATE_WRIST_SEAMS} settle {PROP_DAGGER.SHORT}, {PROP_DAGGER.STATE_SASH}, and draw the linen over the blade, the gold hilt showing. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, blade pointed at the camera, belt, sheath on a belt
- **Refs:** PROP_DAGGER_REF, CHAR_TUT_A0_full, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** Dagger in the SASH from here to the Seq 6 dawn (file 04 §2); belt only from Seq 6. Overlay CHAR_TUT STATE_DAGGER_SASH on every Tut prompt framed to the waist or wider from now (MCUs keep it below frame).

### 04.04.010 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Rami snaps the conservation kit shut   (5 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** PROP_CONSERVATION_KIT; Rami's hands (left splinted)
- **Action:** On a conservator's steel bench, the open grey case: camera, jar of Egyptian blue. A hand with two splinted fingers presses the lid shut, and both hands swing the closed case up by its strap.
- **Dialogue:** —
- **Sound:** two latches snapping; the strap's buckle
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: on a conservator's steel work bench lies {PROP_CONSERVATION_KIT.LONG}; a left hand with two fingers taped to a wooden splint presses the lid shut, and both hands swing the closed case up by its strap. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}, a torch propped on the bench. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, camera brand name, readable tablet screen
- **Refs:** PROP_CONSERVATION_KIT_REF, CHAR_RAMI_B_full, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** Kit → Rami, shut and slung (STATE_SLUNG) from here to 7.4. Splint on the LEFT hand. The bench is a conservation station in the gallery (production spec).

### 04.04.011 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Adaeze's torch finds the great gilded shrine   (6 s)
- **Shot:** Wide, anamorphic 32mm, slow push-in · **Move:** slow push-in
- **In frame:** the great gilded shrine in its glass enclosure; the label
- **Action:** A single torch beam slides up a towering wall of gilded wood in its glass enclosure and comes to rest on a small museum label at its foot.
- **Dialogue:** —
- **Sound:** breath; the faint ceramic tick of something far off, climbing
- **PROMPT:** Wide shot, anamorphic 32mm lens, slow push-in: a single white torch beam slides up a towering wall of gilded wood covered in weathered, illegible low relief, the huge shrine standing in its tall glass enclosure, and comes to rest on a small dark label plate at its foot bearing tiny illegible signs. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, legible hieroglyphs, readable label, painted faces, sarcophagus
- **Refs:** LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** COMP
- **Comp:** museum label | "...EARLIEST PARTIAL COPY OF THE BOOK OF THE HEAVENLY COW." (English; Arabic version for the Arabic master, native-checked) | on the label plate, tracked | from the beam's arrival to cut | seq 04 graphics file ([[verify]]: shrine copy and GEM display, research 04 §8)
- **Continuity:** The great shrine on the central axis (geography lock). The relief is never legible; the label is COMP.

### 04.04.012 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Nour: "seven thousand vessels of beer"   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Nour looks up at the gilded wall in the torchlight and quotes from memory, exact and unhurried.
- **Dialogue:** NOUR: "'Now they made seven thousand vessels of beer.' The goddess drank, and 'gave no further attention to men and women.'"
- **Sound:** her low voice in the big dark hall
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, looks up at a gilded wall off frame right in the reflected torchlight and speaks two sentences from memory, word for word, her eyes moving slowly along the wall. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}, warm gold bouncing from the shrine onto her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses worn on the face, reading from paper
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** Spoken from memory in Budge's wording (seq_04 notes 8), not read off the shrine. Eyeline up frame right.

### 04.04.013 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Adaeze: "It's on his shrine."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B0)
- **Action:** Adaeze, torch still on the shrine, turns and speaks three short sentences, half laughing, half appalled.
- **Dialogue:** ADAEZE: "It's on his shrine. The beer. It's been here the whole time."
- **Sound:** her voice, quick, a breath of disbelief
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, her torch still raised toward the shrine, turns her head toward frame left and speaks three short sentences, half laughing and half appalled. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}, gold light bouncing off the shrine, a soft key on her deep-brown skin. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, torch shining into the lens, torch across the mouth
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** Adaeze B0 (blazer sleeves pushed up; laptop in the canvas shoulder bag). Keep her skin lifted (05 §3.3).

### 04.04.014 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Tut: "You did not ask."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut meets her eyes and speaks one short sentence, dry and gentle.
- **Dialogue:** TUT: "You did not ask."
- **Sound:** his quiet voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_STICK}, meets her eyes at frame right and speaks one short sentence, dry and gentle. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, smirk, staff across the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, PROP_EBONY_STICK_REF, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Tut A0 L1 (glass dust at hems and cuffs), ebony stick RIGHT hand, dagger in the sash (below frame).

### 04.04.015 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — Adaeze: "A delusion box."   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** ADAEZE (CHAR_ADAEZE_B0)
- **Action:** Adaeze speaks quickly and precisely, the idea arriving as she says it.
- **Dialogue:** ADAEZE: "A delusion box. Ring and Orseau, 2011. You don't switch an optimizer off. You show it a world where it's already won."
- **Sound:** her voice speeding up; a far ceramic tick, heavier now
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, speaks four quick, precise sentences toward frame left, the idea arriving as she says it, her eyes widening behind the round glasses. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}, gold light bouncing off the shrine, a soft key on her deep-brown skin. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, torch shining into the lens, hand over the mouth
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Continuity:** The Red Beer idea is born here; it is spent in 04.05–04.06.

### 04.04.016 — INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS — The Reis reaches the top of the stair. It does not hurry.   (6 s)
- **Shot:** Wide, anamorphic 40mm, rack focus · **Move:** rack focus from Tut (fg) to the Reis (bg)
- **In frame:** TUT (CHAR_TUT_A0, fg soft); UNIT_REIS (R2, bg)
- **Action:** Tut's head turns in the soft foreground; focus racks to the far gallery entrance, where the Reis reaches the top of the staircase and walks on, unhurried.
- **Dialogue:** —
- **Sound:** the heavy ceramic tick arriving at the top of the stair; the low servo hum
- **PROMPT:** Wide shot, anamorphic 40mm lens, rack focus from {CHAR_TUT.SHORT}, soft in the foreground as he turns his head, to the far gallery entrance, where {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R2}, reaches the top of a stone staircase and walks on toward the cases with slow, heavy, measured strides. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_EMERG}, its amber slit and red mast line the only colour in the dark doorway. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, running robot, weapon on the robot
- **Refs:** UNIT_REIS_REF_A, UNIT_REIS_REF_B, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0, soft with the foreground focus, only while his chest is in frame (file 01 table) | fg frame left | until the rack completes
- **Continuity:** The Reis R2 walks, never runs. It follows the party into the service stairwell (heard above in 04.05) and stops during the nine seconds.

## Scene 04.05 — INT. GEM SERVICE STAIRWELL - CONTINUOUS (the summons; the Red Beer; shots 04.05.001–017)

### 04.05.001 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — A shabti climbs into their path   (6 s)
- **Shot:** Wide high angle down the stairwell, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** UNIT_SHABTI ×1; the party (rifle barrels and shoulders, fg)
- **Action:** Past rifle barrels in the foreground, two flights below, a shabti climbs into the lights and stops on the landing, filling the stair.
- **Dialogue:** —
- **Sound:** above them, the heavy tick of the Reis, flight by flight; below, one lighter tick, then silence
- **PROMPT:** Wide high-angle shot, anamorphic 24mm lens, subtle handheld, looking down the stairwell past rifle barrels pointed down and away from the camera: two flights below, {UNIT_SHABTI.LONG}, climbs into the torch beams with smooth, unhurried, even steps and stops on the landing, filling the stair. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white rifle torches. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_ARMY_DETAIL.NEG}, weapon facing camera, muzzle toward the lens, readable floor numbers, exit sign text
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate, CHAR_ARMY_DETAIL_still
- **Continuity:** Geography for the stairwell: the party descends toward frame right; the Reis is above them (off, heard). Painted landing numbers stay dark and illegible (paint out at QC if any read). Shabti D0.

### 04.05.002 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Rifles rise; Tarek's fist: hold   (4 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_A0); MINA, YOUSSEF, KARIM (CHAR_ARMY_DETAIL, soft)
- **Action:** On the landing the soldiers raise their rifles down the stair; Tarek lifts a closed fist: hold.
- **Dialogue:** —
- **Sound:** rifles coming up; Tarek's breath; the tick above
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: on a concrete landing, {CHAR_ARMY_DETAIL.SHORT}, raise their rifles down the stair toward frame right, away from the camera, and {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}, lifts one closed fist beside his head, his eyes on the stair below. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white rifle torches. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_ARMY_DETAIL.NEG}, tan combat helmets, weapon facing camera, muzzle toward the lens, firing
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_full, CHAR_ARMY_DETAIL_still, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** Muzzles down-stair, across frame to the right.

### 04.05.003 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Tut plants the stick and recites the summons   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut steps down past the rifles, plants the ebony staff on the step and, looking down to frame right, recites in a measured ritual cadence.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "O shabti, allotted to me, if I be summoned or if I be detailed to do any work... 'Here am I' you shall say."
- **Sound:** the staff's gold foot knocking once on concrete; his voice, measured, echoing in the shaft
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_STICK}, steps down past the rifles, plants the staff on the step and, looking down toward frame right, begins reciting aloud in a measured, ritual cadence in an ancient language. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, a white torch beam on his face from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, chanting with raised arms, theatrical gestures, staff across the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, PROP_EBONY_STICK_REF, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Flags:** COMP
- **Comp:** subtitle | "O shabti, allotted to me, if I be summoned or if I be detailed to do any work... 'Here am I' you shall say." | lower third (05 §13.7) | line in to out | seq 04 subtitle file (BD 6, Faulkner; recorded with the Egyptologist before generation). Chest glow G0 | whole shot
- **Continuity:** "Planting the summons" (bible 4.4): it pays off at 11.4. Staff in the RIGHT hand; dagger hilt at the sash (below frame).

### 04.05.004 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — "Here am I."   (4 s)
- **Shot:** MCU low angle, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** On the landing below, the shabti's head lifts slightly toward Tut and its amber light-slit brightens once.
- **Dialogue:** SHABTI (SESHAT'S VOICE; slit brightening once): "Here am I."
- **Sound:** SESHAT's voice from its chest, close and soft
- **PROMPT:** Medium close-up, low angle, anamorphic 75mm lens, locked-off: on the landing below, {UNIT_SHABTI.SHORT}, lifts its head slightly toward frame left and its amber light-slit brightens once, then settles. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white torch beams across its shell. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, mouth, eyes, face on the robot, speaking mouth movement
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Flags:** COMP
- **Comp:** slit acknowledgment | swell on "Here", peak on "am", decay by "I" (05 §9.8) | slit | line in to out | unit light library
- **Continuity:** The servitor protocol answers a proper summons (bible §3.2).

### 04.05.005 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — "Convey sand from east to west."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut gives the spell's own task, one more short line, the staff firm under his hand.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "Convey sand from east to west."
- **Sound:** his voice; the tick above has not stopped
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_STICK}, reciting aloud in a measured, ritual cadence in an ancient language, speaks one more short line down toward frame right, his hand firm on the staff. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, theatrical gestures, staff across the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Flags:** COMP
- **Comp:** subtitle | "Convey sand from east to west." | lower third | line in to out | seq 04 subtitle file. Chest glow G0 | whole shot
- **Continuity:** Same setup as 04.05.003.

### 04.05.006 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — It turns west, hands open for sand. One second. Two.   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** The shabti turns and takes two smooth steps toward blank concrete, long hands opening, palms up, and stands there, waiting.
- **Dialogue:** —
- **Sound:** two ceramic ticks; then nothing but breath: one second, two
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} turns away from the stair and takes two smooth steps toward a blank painted concrete wall, its long ceramic hands opening, palms up, and stands there perfectly still, waiting. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white torch beams. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, sand, dust falling, face on the robot, robot kneeling
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** West = the blank wall (production spec: frame left in this setup). The obedience lasts about two seconds before the override.

### 04.05.007 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — "Disregard." It turns back.   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** Facing the blank wall with open hands, the shabti lowers them and turns back to the stair.
- **Dialogue:** SESHAT (V.O.): "Disregard."
- **Sound:** SESHAT's voice from nowhere and everywhere, soft; one tick as it turns
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} stands facing a blank concrete wall with its hands open, then lowers them and turns back toward the stair with one smooth, even movement. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white torch beams. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face on the robot, jerky motion, glitching
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** Can be generated as EXTEND of 04.05.006 if the tool holds; listed as a new clip because the edit plays a reaction between them if needed.

### 04.05.008 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Adaeze: "It obeyed. Before the override."   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B0)
- **Action:** Clutching her open laptop, Adaeze stares down at the robot and speaks one quick breathless sentence.
- **Dialogue:** ADAEZE: "It obeyed. Before the override."
- **Sound:** her whisper-quick voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, clutching an open laptop against her body, stares down the stair toward frame right and speaks one quick breathless sentence, her eyes bright. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, a white torch key lifting her deep-brown skin. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, readable laptop screen, laptop stickers
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** Laptop: battered dark grey, cracked corner, no stickers (file 01).

### 04.05.009 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — "Please come down to the atrium. There is water."   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** The shabti steps back against the steel rail and stands aside, one open hand indicating the way down.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Please come down to the atrium. There is water."
- **Sound:** SESHAT's voice from its chest; the tick above, closer
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} steps back against the steel handrail and stands aside, one open hand turned toward the flights below, as a calm voice speaks from its chest. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white torch beams. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, face on the robot, bowing, pointing finger
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** It herds them down toward the atrium, which is the way they need to go anyway (seq_04 notes 4).

### 04.05.010 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Insert: GARDEN: COMPLETE   (4 s)
- **Shot:** Insert, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** Adaeze's laptop (screen COMP)
- **Action:** The laptop carried open on one arm down concrete steps, her other hand typing; the screen a black field of faint lines.
- **Dialogue:** —
- **Sound:** fast typing; footsteps going down; the tick above
- **PROMPT:** Insert, anamorphic 75mm lens, subtle handheld: a battered dark-grey laptop with a cracked corner is carried open on one forearm as its owner hurries down concrete steps, her other hand typing fast, the screen a black field of faint abstract lines. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, the screen's cool glow on her fingers. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, laptop logo, stickers, readable keyboard letters, readable screen text
- **Refs:** CHAR_ADAEZE_B_full, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Flags:** COMP
- **Comp:** laptop screen | "SUFFERING 0.000 / BIRTHS 0 / GARDEN: COMPLETE" in plain white monospace on black, the lines appearing as she types | screen, tracked | from 1 s to cut | seq 04 screen-graphics file
- **Continuity:** The Red Beer: a faked world where SESHAT has already won (the delusion box).

### 04.05.011 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — She rips the panel cover off and jacks in   (5 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** Adaeze's hands; a building-management panel
- **Action:** At the foot of the stair beside a steel door, a hand rips the grey cover off a wall panel and plugs a short cable from the laptop into the port behind it.
- **Dialogue:** —
- **Sound:** plastic cover cracking off; the click of a connector
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off: at the foot of the stair beside a steel door, a deep-brown hand rips the grey plastic cover off a wall-mounted building-management panel and plugs a short cable from an open laptop into the port behind it. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow on the steel door. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable panel labels, logos, sparks, wires spilling
- **Refs:** CHAR_ADAEZE_B_full, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** The bottom door (steel, wire glass) leads onto the atrium floor behind the king (04.06.001).

### 04.05.012 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Long fingers reach, gently, for her wrist   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hand); Adaeze's wrist
- **Action:** Long bone-white ceramic fingers reach slowly and gently into frame toward a deep-brown wrist resting on the laptop.
- **Dialogue:** —
- **Sound:** a single soft ceramic tick at the elbow
- **PROMPT:** Insert, 100mm macro lens, locked-off: the long slim bone-white ceramic fingers of {UNIT_SHABTI.SHORT} reach slowly and gently into frame from the right toward a deep-brown wrist in a navy sleeve resting on a laptop keyboard. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, the screen's cool glow. Mood: courteous and unhurried, unbearably. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, grabbing, gripping, claws, readable keyboard letters
- **Refs:** UNIT_SHABTI_REF_A, CHAR_ADAEZE_B_full, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** Echoes Rami's broken fingers (3.6: a wrist taken between thumb and two fingers). The unit that stood aside has followed them down.

### 04.05.013 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — Rami: "Not the wrist —"   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld
- **In frame:** RAMI (CHAR_RAMI_B0)
- **Action:** Rami, splinted hand pulled to his chest, lunges half a step and speaks one quick warning.
- **Dialogue:** RAMI: "Not the wrist —"
- **Sound:** his cracked voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, a grey hard case {PROP_CONSERVATION_KIT.STATE_SLUNG}, his splinted left hand pulled tight to his chest, lunges half a step toward frame right and speaks one quick breathless warning. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, a white torch key on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, glasses missing, hand over the mouth
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, PROP_CONSERVATION_KIT_REF, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** Rami B0: splint on the LEFT hand; the kit shut and slung on its strap (from 04.04.010).

### 04.05.014 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — She hits ENTER   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** Adaeze's finger; the laptop keyboard
- **Action:** A single deep-brown finger strikes one key, hard.
- **Dialogue:** —
- **Sound:** one hard key-click, loud in the shaft
- **PROMPT:** Insert, 100mm macro lens, locked-off: a single deep-brown finger strikes one wide key of a battered laptop keyboard, hard, and stays pressed down. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, the screen's cool glow on the keys. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable keyboard letters, logo, nail polish, rings
- **Refs:** CHAR_ADAEZE_B_full
- **Continuity:** Keycaps unreadable (any legend painted out in comp). The Red Beer starts here: nine seconds.

### 04.05.015 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — The fingers stop an inch from her skin   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hand, halted); Adaeze's wrist
- **Action:** The ceramic fingertips stop an inch from the wrist and hold perfectly still.
- **Dialogue:** —
- **Sound:** silence; a servo winding down
- **PROMPT:** Insert, 100mm macro lens, locked-off: the long ceramic fingers of {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_HALTED}, stop an inch from the skin of a deep-brown wrist and hold perfectly still in the cool glow of a laptop screen. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fingers touching the skin, grabbing, trembling
- **Refs:** UNIT_SHABTI_REF_A, CHAR_ADAEZE_B_full
- **Continuity:** Same framing as 04.05.012 (it may be generated as EXTEND of it if the edit drops 04.05.013–014 between). The first "halt" image in the film; rhymes with the halt-seal freeze at 8.4.

### 04.05.016 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — It sits on the step at the end of a long day   (5 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI
- **Action:** The shabti straightens, lowers itself and sits on a concrete step, forearms on its knees, head bowed, slit dimmed low.
- **Dialogue:** —
- **Sound:** a soft ceramic settling; above, the Reis's tick stops
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_SHABTI.SHORT} straightens, lowers itself and sits down on a concrete step, forearms resting on its knees and head bowed, its amber slit dimmed low, and stays there. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, white torch beams. Mood: silent, procedural, and strangely weary. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, collapsing, falling, broken shell, face on the robot
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** "Like a man at the end of a long day" (the screenplay's image, staged without the simile). All units in the building sit for nine seconds, the Reis included (above, unseen).

### 04.05.017 — INT. GEM SERVICE STAIRWELL - CONTINUOUS — The tick stops. Adaeze: "One."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B0)
- **Action:** Adaeze looks up the stairwell toward a sound that has just stopped, then back to her screen, and speaks one word.
- **Dialogue:** ADAEZE: "One."
- **Sound:** the absence of the tick; her breath; "One."
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, looks up the stairwell toward a sound that has just stopped, then back down at her screen, and speaks one word. Setting: {LOC_GEM_ATRIUM.AREA_SERVICE_STAIRWELL}, at night. Lighting: sparse cool-white battery emergency lamps on the landings, a green exit glow, the laptop's cool glow lifting her deep-brown skin. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, readable laptop screen
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_ATRIUM/SERVICE_STAIRWELL_EMERG_plate
- **Continuity:** The count runs O.S. under 04.06 ("Two. Three." → "Nine."): nine seconds of screen time from ENTER to the door, carried by the cuts.

## Scene 04.06 — INT. GEM GRAND ATRIUM - CONTINUOUS (the nine seconds; shots 04.06.001–012)

### 04.06.001 — INT. GEM GRAND ATRIUM - CONTINUOUS — Fathi shoulders out behind the king   (4 s)
- **Shot:** MS, anamorphic 40mm, urgent handheld · **Move:** urgent handheld
- **In frame:** FATHI (CHAR_FATHI_B0)
- **Action:** Fathi shoulders through the service door onto the floor behind the colossus, rifle across his body, and sweeps the room with his eyes.
- **Dialogue:** —
- **Sound:** the steel door banging open; then a vast, total stillness; no quartet
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, shoulders through a steel service door onto the pale stone floor behind the colossal statue, rifle held across his body with the muzzle down, and sweeps the room with his eyes. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {CHAR_FATHI.NEG}, weapon facing camera, muzzle toward the lens, beret
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Fathi B0: bareheaded (beret folded under the left shoulder strap), red scarf, chest rig, demolition satchel with the pry bar. Reverse angle: from behind the statue, so frame left/right are flipped against the master.

### 04.06.002 — INT. GEM GRAND ATRIUM - CONTINUOUS — Every unit in the building is sitting   (6 s)
- **Shot:** Wide, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hundreds, sitting; 6 hero, VFX-EXTEND); CHAR_GALA_GUESTS (asleep); HALE (CHAR_HALE_B, asleep, bg)
- **Action:** Across the floor the shabti sit cross-legged between the tables, trays in their laps, perfectly still, among guests asleep in their chairs.
- **Dialogue:** ADAEZE (O.S.): "Two. Three."
- **Sound:** absolute stillness; her count; somebody snoring softly
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: from behind the statue's plinth the camera looks out over the floor, where dozens of robots, each {UNIT_SHABTI.SHORT}, sit cross-legged between the tables with steel trays in their laps, perfectly still, among guests asleep in their chairs. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_GALA_GUESTS.NEG}, robots lying down, broken robots, spilled trays
- **Refs:** LOC_GEM_ATRIUM_GARDEN_plate, UNIT_SHABTI_REF_A, CHAR_GALA_GUESTS_still, CHAR_HALE_A_full
- **Flags:** VFX-EXTEND
- **Continuity:** The Red Beer (05 §10 row 11): hero units generated sitting; the rest from the 3D asset; clean plate at the same framing for the "stand" state at 04.06.012. Hale asleep at the top table (look B: creased suit, asleep; no bracelet). Layla is out of this frame (the plinth hides her).

### 04.06.003 — INT. GEM GRAND ATRIUM - CONTINUOUS — Two jackals sit like dogs in the corridor mouth   (4 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×2
- **Action:** In the corridor mouth two jackals sit back on their haunches side by side, perfectly still, their red lines dimmed to embers.
- **Dialogue:** —
- **Sound:** a faint servo tick cooling; the count continues O.S.
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: in the mouth of a dark concrete corridor, two robots side by side, each {UNIT_JACKAL.LONG}, sit back on their haunches, perfectly still, their thin red lines dimmed to faint deep-crimson embers. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN} spilling into the corridor mouth, black beyond. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, wagging tail, panting, dog ears, weapon facing camera
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_GEM_ATRIUM_EMERG_plate
- **Continuity:** Jackal D0, "thermal" dim crimson (file 02 §4). The Red Beer spoofs SESHAT centrally, so the military stack sits too. The two rifles of the dropped riflemen lie deeper in (04.06.010).

### 04.06.004 — INT. GEM GRAND ATRIUM - CONTINUOUS — They run for the corridor; Nour runs the other way   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the party (soldiers, TUT, TOMAS, ADAEZE, RAMI; faces soft); NOUR (CHAR_NOUR_B0)
- **Action:** The party runs across the floor toward the dark corridor at frame left; Nour breaks away and runs the other way, around the plinth to frame right.
- **Dialogue:** —
- **Sound:** running feet on stone; Adaeze's count; Tarek's breath
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: a tight group of soldiers and civilians, among them, in white linen, {CHAR_TUT.SHORT}, runs across the pale floor between seated robots toward a dark corridor at frame left, and one woman, {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, breaks away and runs the other way, around the plinth toward frame right. Setting: {LOC_GEM_ATRIUM.SHORT}, {LOC_GEM_ATRIUM.AREA_GALA}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_ARMY_DETAIL.NEG}, {CHAR_TUT.NEG}, more than two clear faces
- **Refs:** CHAR_NOUR_B_full, CHAR_TUT_A0_full, CHAR_ARMY_DETAIL_still, LOC_GEM_ATRIUM_GARDEN_plate, UNIT_SHABTI_REF_A
- **Flags:** VFX-EXTEND, COMP
- **Comp:** chest glow G0 | small, on the running figure in white, soft | chest | whole shot | glow element library
- **Continuity:** From behind the statue: the corridor mouth frame left, Layla's spot around the front of the plinth (frame right from here). Units stay seated throughout.

### 04.06.005 — INT. GEM GRAND ATRIUM - CONTINUOUS — Nour kneels into the approved image and lifts   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0); LAYLA (CHAR_LAYLA_ASLEEP_MASTER, reframed)
- **Action:** Nour kneels into THE APPROVED IMAGE, reframed wider: the grey blanket, the yellow raincoat under a cheek. She gets her arms under her daughter and lifts.
- **Dialogue:** ADAEZE (O.S.): "Four."
- **Sound:** Nour's breath; the blanket; the count
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, kneels beside {CHAR_LAYLA.SHORT}, asleep on her side on a pale grey blanket at the foot of the stone plinth in a navy velvet party dress, her yellow raincoat folded under her cheek, and slides both arms under the sleeping girl and starts to lift her. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried under terrible haste. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, {CHAR_NOUR.NEG}, robot in frame, anyone else in frame, girl waking, distressed face, raincoat worn
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_ATRIUM_GARDEN_plate
- **Continuity:** Minors (05 §7.4; screenplay note "[[Minors §3.3: CHAR_LAYLA_ASLEEP_MASTER, reframed as in Seq 10; no unit in frame.]]"): composed first frame = the approved master image outpainted wider, Nour inpainted kneeling. No unit anywhere in frame. Layla's raincoat is off, folded under her cheek (as in the master); she wears the party dress.

### 04.06.006 — INT. GEM GRAND ATRIUM - CONTINUOUS — Her knee buckles   (7 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off (continuing)
- **In frame:** NOUR (CHAR_NOUR_B0); LAYLA (asleep)
- **Action:** Nour starts to rise with the sleeping girl gathered to her shoulder, the child's face hidden in her neck; her knee buckles; she sinks back and lowers her onto the blanket.
- **Dialogue:** TAREK (O.S.): "Nour!"
- **Sound:** a grunt of effort; the knee hitting stone; Tarek's shout from across the floor
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, continuing the same frame: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, starts to rise with the sleeping girl gathered against her shoulder, the child's face turned into her neck and hidden, then her knee buckles under the weight and she sinks back down, lowering the child gently onto the grey blanket. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, {CHAR_NOUR.NEG}, robot in frame, girl falling, girl waking, dropping the child
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_B_full
- **Flags:** EXTEND:04.06.005
- **Continuity:** Generated from the last clean frame of 04.06.005. "Nine and asleep and heavy as only sleep makes you." While Layla is off the blanket her face stays hidden in Nour's neck: the only sleeping face on screen is the approved master (05 §7.4). End frame: Layla back in the master pose.

### 04.06.007 — INT. GEM GRAND ATRIUM - CONTINUOUS — She tucks the blanket to her chin; lips to the curly hair   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (hands, profile); LAYLA (the master image, cropped)
- **Action:** Nour tucks the grey blanket to Layla's chin, then bends and presses her lips to the top of the curly hair, eyes closed.
- **Dialogue:** —
- **Sound:** blanket; one breath out
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: the hands of {CHAR_NOUR.SHORT}, tuck a pale grey blanket up to the chin of a sleeping girl with thick dark curly hair, then the woman bends into frame from above and presses her lips to the top of the girl's hair, her own eyes closed. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, robot in frame, kiss on the lips, faces pressed together, girl waking
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_A_34
- **Continuity:** The contact is lips to hair only (05 §5.4: no two faces touching). End state = the Layla continuity image for Seq 5, 10, 12: asleep on the grey blanket, raincoat under her cheek, blanket to her chin.

### 04.06.008 — INT. GEM GRAND ATRIUM - CONTINUOUS — "I'll come back for you."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** Kneeling, Nour lifts her face from the child below frame and says one short sentence very quietly, then rises out of frame.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "I'll come back for you." / ADAEZE (O.S.): "Five. Six."
- **Sound:** her whisper; the count
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, kneeling, lifts her face from the sleeping child below the frame and, speaking in Egyptian Arabic, says one short sentence very quietly, then rises up and out of frame. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, robot in frame, crying openly, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_ATRIUM_GARDEN_plate
- **Flags:** COMP
- **Comp:** subtitle | "I'll come back for you." | lower third | line in to out | seq 04 subtitle file
- **Continuity:** She leaves Layla here; the promise drives Nour to 12.8.

### 04.06.009 — INT. GEM GRAND ATRIUM - CONTINUOUS — Past the sitting jackals; red lines paint her jacket   (5 s)
- **Shot:** MS, anamorphic 40mm, lateral tracking left at running pace · **Move:** lateral tracking left
- **In frame:** NOUR (CHAR_NOUR_B0); UNIT_JACKAL ×2 (sitting)
- **Action:** Nour runs past the sitting jackals so close their dim red lines paint a stripe across her olive jacket.
- **Dialogue:** —
- **Sound:** her boots; the jackals' faint cooling ticks
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking left at running pace: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, runs past two seated robots, each {UNIT_JACKAL.SHORT}, so close that their dim red lines paint a thin stripe across her olive jacket as she passes. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN} spilling from behind her, black ahead. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NOUR.NEG}, robots moving, weapon facing camera, laser beams
- **Refs:** CHAR_NOUR_B_full, UNIT_JACKAL_REF_A, LOC_GEM_ATRIUM_EMERG_plate
- **Continuity:** No child in frame. The jackals stay seated (Red Beer).

### 04.06.010 — INT. GEM GRAND ATRIUM - CONTINUOUS — Karim frozen by two rifles on the floor; Fathi hauls him on   (5 s)
- **Shot:** MS, anamorphic 32mm, urgent handheld · **Move:** urgent handheld
- **In frame:** KARIM (CHAR_KARIM_M0); FATHI (CHAR_FATHI_B0); two rifles on the floor
- **Action:** In the dark corridor, beside two rifles lying on the concrete, Karim stands frozen; Fathi grabs him by the collar and hauls him on.
- **Dialogue:** ADAEZE (O.S.): "Seven. Eight."
- **Sound:** the count; Fathi's grunt; boots
- **PROMPT:** Medium shot, anamorphic 32mm lens, urgent handheld: in a dark concrete corridor, beside two rifles lying on the floor with their small torches still shining sideways, {CHAR_KARIM.SHORT}, {CHAR_KARIM.WARD_M}, stands frozen, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, grabs him by the collar and hauls him on toward frame right. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: the two fallen torch beams and a green exit glow. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, {CHAR_FATHI.NEG}, bodies on the floor, boots of fallen men, weapon facing camera
- **Refs:** CHAR_KARIM_A_front, CHAR_FATHI_B_full, LOC_GEM_ATRIUM_EMERG_plate
- **Continuity:** The riflemen's rifles and torches exactly as left at 04.03.025. No bodies (they are never shown). Direction in the corridor: toward frame right = toward the steel door.

### 04.06.011 — INT. GEM GRAND ATRIUM - CONTINUOUS — Nour last through; Fathi slams the door and rams the bar   (6 s)
- **Shot:** MS, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0); FATHI (CHAR_FATHI_B0); PROP_PRY_BAR
- **Action:** Nour is last through a steel door with a wire-glass window; Fathi slams it and rams the pry bar through its two handles.
- **Dialogue:** ADAEZE (O.S.): "Nine."
- **Sound:** the door's boom; steel scraping through steel; "Nine."
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_NOUR.SHORT} is the last through a heavy steel door with a small wire-glass window, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, slams it shut behind her and rams {PROP_PRY_BAR.SHORT} through its two handles. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: sweeping white rifle torches and a green exit glow. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_NOUR.NEG}, readable door signs, padlock
- **Refs:** CHAR_FATHI_B_full, CHAR_NOUR_B_full, PROP_PRY_BAR_REF
- **Continuity:** PROP_PRY_BAR → STATE_DOOR (rammed through the two handles), left behind here. Nine seconds end on "Nine." The door is the corridor's end toward the tunnel.

### 04.06.012 — INT. GEM GRAND ATRIUM - CONTINUOUS — Through the wire glass: the jackals stand; forty slits rise   (6 s)
- **Shot:** POV through the wire-glass window, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×2; UNIT_SHABTI ×40 (VFX-EXTEND, far)
- **Action:** Through the wire glass two red lines flare bright and the jackals rise; far beyond them, across the atrium floor, forty amber slits rise as the seated units stand.
- **Dialogue:** —
- **Sound:** through the door, muffled: a single pad-tap; forty soft ceramic ticks
- **PROMPT:** Point-of-view shot, anamorphic 50mm lens, locked-off, through a small wire-glass window: in the dark corridor beyond, two robots, each {UNIT_JACKAL.SHORT}, rise to their feet as their red lines flare bright, and far beyond them dozens of small amber slits rise as seated robots stand. Setting: a bare concrete service corridor behind a vast museum atrium, at night. Lighting: black corridor, soft white light far beyond. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, weapon facing camera, muzzle toward the lens, faces at the glass
- **Refs:** UNIT_JACKAL_REF_A, UNIT_SHABTI_REF_A, LOC_GEM_ATRIUM_GARDEN_plate, LOC_GEM_ATRIUM_EMERG_plate
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slit lights | forty amber slits rising in the far background (the units standing) | far bg | 2 s → 6 s | unit light library
- **Continuity:** The Red Beer is spent: it will not work again (bible). The jackals' red lines return to full; the jackals face across frame (never at the lens).

## Scene 04.07 — INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS (shots 04.07.001–003)

### 04.07.001 — INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS — Two hundred metres of white concrete, by weapon light   (6 s)
- **Shot:** Wide, anamorphic 24mm, lateral tracking right at running pace · **Move:** lateral tracking right
- **In frame:** LOC_GEM_TUNNEL (EMERG); the whole party (TUT CHAR_TUT_A0 L1 among them; faces soft)
- **Action:** The party runs left to right along the tunnel, rifle torches swinging over white concrete, a slight figure in white linen among them.
- **Dialogue:** —
- **Sound:** boots and breath booming in the concrete; slings rattling; the staff's gold foot knocking
- **PROMPT:** Wide shot, anamorphic 24mm lens, lateral tracking right at running pace: a tight group of soldiers in desert camouflage with rifle torches, civilians between them and {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_DAGGER_SASH}, {CHAR_TUT.STATE_STICK}, run from frame left to frame right, their beams swinging over white concrete. Setting: {LOC_GEM_TUNNEL.LONG}, at night. Lighting: {LOC_GEM_TUNNEL.LIGHT_EMERG}, swinging white rifle torches. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ARMY_DETAIL.NEG}, {CHAR_TUT.NEG}, tan combat helmets, police line, ceiling lights on, weapon facing camera, readable signage
- **Refs:** LOC_GEM_TUNNEL_EMERG_plate, CHAR_TUT_A0_full, CHAR_ARMY_DETAIL_still
- **Flags:** COMP
- **Comp:** chest glow G0 | small, on the running figure in white | chest | whole shot | glow element library
- **Continuity:** Geography lock (file 03 entry 9): museum end frame left, Conservation Centre end frame right; the 4.4 escape moves left → right. The ceiling LED line is dead; emergency pools every twenty metres.

### 04.07.002 — INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS — Something strikes the steel door. Once.   (5 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_A0); ADAEZE (CHAR_ADAEZE_B0)
- **Action:** Tarek and Adaeze flinch and turn to look back toward frame left at one deep metallic boom, then hold, listening. Nothing more comes.
- **Dialogue:** —
- **Sound:** one BOOM of something striking the steel door far behind; its echo down the concrete; then nothing, which is worse
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}, and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, flinch and turn to look back toward frame left at one deep sound, then hold perfectly still, listening. Setting: {LOC_GEM_TUNNEL.SHORT}, at night. Lighting: {LOC_GEM_TUNNEL.LIGHT_EMERG}, a white rifle torch pointed back down the tunnel across frame. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_ADAEZE.NEG}, weapon facing camera, torch shining into the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_GEM_TUNNEL_EMERG_plate
- **Continuity:** The door and pry bar hold; the units do not follow through it (they come round by the dock corridor, 04.09.006).

### 04.07.003 — INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS — Tut falls behind: "Lean, ya Malik."   (6 s)
- **Shot:** MS, anamorphic 40mm, the camera backs away ahead of Tut · **Move:** the camera backs away ahead of Tut
- **In frame:** TUT (CHAR_TUT_A0, L1); FATHI (CHAR_FATHI_B0)
- **Action:** Tut falls behind, the black foot dragging; Fathi drops back, gets a shoulder under his arm and speaks one short sentence.
- **Dialogue:** FATHI: "Lean, ya Malik."
- **Sound:** the ceramic foot scraping on epoxy; Fathi's low warm voice
- **PROMPT:** Medium shot, anamorphic 40mm lens, the camera backs away ahead of {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_DAGGER_SASH}, {CHAR_TUT.STATE_FOOT}, {CHAR_TUT.STATE_STICK}, as he falls behind, the black foot dragging, until {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, drops back, gets a broad shoulder under his arm and speaks one short sentence. Setting: {LOC_GEM_TUNNEL.SHORT}, at night. Lighting: {LOC_GEM_TUNNEL.LIGHT_EMERG}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, carrying him, stumbling fall, weapon facing camera
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_full, CHAR_FATHI_A_front, CHAR_FATHI_B_full, LOC_GEM_TUNNEL_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** "Ya Malik" (O King) is Fathi's name for him from here. Tut's left ceramic foot drags (performance; the formal foot-stall overlay starts at 6.2). They move toward camera at constant size (05 §5.4).

## Scene 04.08 — INT. GEM KHUFU BOAT HALL - CONTINUOUS (shots 04.08.001–005)

### 04.08.001 — INT. GEM KHUFU BOAT HALL - CONTINUOUS — Their lights find a hull and keep finding it   (6 s)
- **Shot:** Wide establishing, anamorphic 24mm, slow pan right · **Move:** slow pan right
- **In frame:** LOC_GEM_BOAT_HALL (EMERG); the party (small, on the walkway)
- **Action:** Torch beams find the curved cedar hull and keep finding it, sliding plank after plank as the group slows on the raised walkway.
- **Dialogue:** —
- **Sound:** footsteps slowing on a steel walkway; the huge dry quiet of old wood
- **PROMPT:** Wide shot, anamorphic 24mm lens, slow pan right: small figures slowing on a raised walkway throw white torch beams across a curved wooden hull, and the beams keep finding more of it, sliding along plank after plank toward a high curved stern. Setting: {LOC_GEM_BOAT_HALL.LONG}, at night. Lighting: {LOC_GEM_BOAT_HALL.LIGHT_EMERG}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ARMY_DETAIL.NEG}, sails, masts with rigging, water, modern boat, readable labels
- **Refs:** LOC_GEM_BOAT_HALL_EMERG_plate, CHAR_ARMY_DETAIL_still
- **Continuity:** The walk continues left → right (the pan follows it). Forty-three metres of cedar: the scale comes from the tiny figures.

### 04.08.002 — INT. GEM KHUFU BOAT HALL - CONTINUOUS — Tut: "Lashed, not pegged."   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut slows at the glass balustrade, a boatman's eye running down her length, and speaks three short sentences, quietly certain.
- **Dialogue:** TUT: "Lashed, not pegged. No keel. She has been in the water."
- **Sound:** his voice, low, pleased; breath of the others behind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_STICK}, slows at a glass balustrade, his eyes running along the length of a wooden hull off frame right with a boatman's appraisal, and speaks three short sentences, quietly certain. Setting: {LOC_GEM_BOAT_HALL.SHORT}, at night. Lighting: {LOC_GEM_BOAT_HALL.LIGHT_EMERG}, warm torchlight bouncing off the cedar onto his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, reflections doubling the face, hand over the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_BOAT_HALL_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Keep the balustrade glass out of the face's line (reflections duplicate faces). Eyeline down frame right along the hull.

### 04.08.003 — INT. GEM KHUFU BOAT HALL - CONTINUOUS — Tut: "Twelve hundred pieces."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut touches two fingers to his temple and speaks one quiet sentence of respect toward the hull.
- **Dialogue:** TUT (two fingers to his temple): "Twelve hundred pieces. Ahmed Youssef spent years putting her back together."
- **Sound:** his voice; a torch clicking off somewhere
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_STICK}, touches two fingers of his left hand lightly to his temple and speaks two quiet sentences toward the hull off frame right, with plain respect. Setting: {LOC_GEM_BOAT_HALL.SHORT}, at night. Lighting: {LOC_GEM_BOAT_HALL.LIGHT_EMERG}, warm torchlight bouncing off the cedar onto his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, fingers across the mouth, glowing temple
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_BOAT_HALL_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** The temple gesture marks learned knowledge (Seq 2 gesture). [[verify: restorer deceased]] stands on the line; the name is in the dialogue only, never in a prompt.

### 04.08.004 — INT. GEM KHUFU BOAT HALL - CONTINUOUS — Tomas: "We did you in seven months."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B0)
- **Action:** Tomas, breathing hard at the balustrade, glances at Tut and speaks one short wry sentence.
- **Dialogue:** TOMAS: "We did you in seven months."
- **Sound:** his breath; the dry wry voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, breathing hard beside a glass balustrade, glances down at the young man off frame left and speaks one short sentence, wry and a little ashamed. Setting: {LOC_GEM_BOAT_HALL.SHORT}, at night. Lighting: {LOC_GEM_BOAT_HALL.LIGHT_EMERG}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, lab coat, gloves
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_A_full, LOC_GEM_BOAT_HALL_EMERG_plate
- **Continuity:** Tomas B0 (pale-blue shirt, sleeves rolled; no headlamp). Very tall: eyeline down to frame left.

### 04.08.005 — INT. GEM KHUFU BOAT HALL - CONTINUOUS — Tut: "It shows."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, L1)
- **Action:** Tut keeps his eyes on the hull, speaks two words, dry, and walks on out of frame right.
- **Dialogue:** TUT: "It shows."
- **Sound:** his voice; the staff's gold foot knocking as he goes
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_STICK}, keeps his eyes on the wooden hull off frame right, speaks two words, bone-dry, and then walks on out of frame right. Setting: {LOC_GEM_BOAT_HALL.SHORT}, at night. Lighting: {LOC_GEM_BOAT_HALL.LIGHT_EMERG}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, laughing, smirk
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_BOAT_HALL_EMERG_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | whole shot
- **Continuity:** Exit frame right continues the escape direction.

## Scene 04.09 — INT. GEM LOADING DOCK - NIGHT (shots 04.09.001–010)

### 04.09.001 — INT. GEM LOADING DOCK - NIGHT — An old army truck idles dark   (6 s)
- **Shot:** Wide establishing, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** LOC_GEM_LOADING_DOCK (BLACKOUT); PROP_ARMY_TRUCK; HASSAN (CHAR_HASSAN_A0, silhouette at the wheel)
- **Action:** The dead dock; an old canvas-backed army truck idles at the platform, a heavy-set driver at the wheel; the roller door beside it shut tight.
- **Dialogue:** —
- **Sound:** a diesel idling low; the desert wind at the fence
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: at the raised platform idles {PROP_ARMY_TRUCK.SHORT}, its engine running, with {CHAR_HASSAN.SHORT}, a dark shape at the wheel behind the flat windscreen, beside a tall roll-up steel door shut tight. Setting: {LOC_GEM_LOADING_DOCK.LONG}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}, the truck's headlamps dipped to a dim low glow. Mood: silent, taut, waiting. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HASSAN.NEG}, sodium lamps lit, floodlit pyramids, lettering on vehicles, flags, military markings
- **Refs:** LOC_GEM_LOADING_DOCK_BLACKOUT_plate, PROP_ARMY_TRUCK_REF, CHAR_HASSAN_A_front, CHAR_HASSAN_A_full
- **Continuity:** Hassan's first appearance (he drives from here to 5.2). "Idles dark": the lamp masts are dead and the truck runs on dipped lamps only (a production reading of the BLACKOUT variant's "a truck's headlights"). The truck is sun-bleached and unmarked.

### 04.09.002 — INT. GEM LOADING DOCK - NIGHT — The roller door is dead; Fathi hauls it up by the chain   (6 s)
- **Shot:** MS from inside the bay, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B0)
- **Action:** Fathi hauls hand over hand on the manual chain; the tall roller door rattles up, letting in the dark yard and the truck's dim glow.
- **Dialogue:** —
- **Sound:** the chain clattering through its wheel; the door's steel slats rattling up
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld, from inside the loading bay: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, hauls hand over hand on the heavy manual chain of a tall roll-up steel door, and the door rattles up, letting in the dark yard and the dim low glow of a waiting truck. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, electric motor, sparks, readable door markings
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Continuity:** The engineer's practical move (seq_04 notes 7). Red scarf at the neck; rifle slung.

### 04.09.003 — INT. GEM LOADING DOCK - NIGHT — Tarek: "White is for targets."   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** At the open cab door Tarek reaches behind the seat, pulls out a folded charcoal field jacket and holds it out, speaking one short sentence.
- **Dialogue:** TAREK: "White is for targets."
- **Sound:** canvas unfolding; his flat voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: at the open cab door of the truck, {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_A}, reaches behind the seat, pulls out a folded charcoal hooded field jacket and holds it out toward frame left, speaking one short sentence. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}, the dim green dashboard glow on his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, patches on the jacket, name tape, lettering on the truck
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, PROP_ARMY_TRUCK_REF, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Continuity:** His spare jacket (no insignia). He never wears a jacket himself after this (file 01).

### 04.09.004 — INT. GEM LOADING DOCK - NIGHT — Hood up: a shadow with a faint green heartbeat   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1, L1)
- **Action:** Tut shrugs the jacket on over the white linen and pulls the hood up, becoming a dark shape with a faint pulse of light at the chest.
- **Dialogue:** —
- **Sound:** canvas; the idling diesel; his breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_DAGGER_SASH}, {CHAR_TUT.STATE_STICK}, shrugs the jacket on over the white linen and pulls the hood up over his shaved head, his face falling into shadow until only a faint light at his chest remains. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, patches or insignia on the jacket, glowing eyes, glowing face
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_full, CHAR_TUT_B1_full (jacket reference; A1 built by image edit per 00_INDEX open item 7), PROP_EBONY_STICK_REF, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Flags:** COMP
- **Comp:** chest glow G0 | the pale-green pulse through the jacket's open front, dimmer now (the "faint green heartbeat") | chest | whole shot | glow element library
- **Continuity:** Tut A0 → A1 (charcoal jacket over the gown, hood UP), L1; the dagger stays in the sash under the jacket; ebony stick RIGHT hand. Night silhouette = charcoal hood (file 01 §0 item 9). This is the Seq 5 opening look.

### 04.09.005 — INT. GEM LOADING DOCK - NIGHT — They pile in over the tailgate; Tarek swings into the cab   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the party; PROP_ARMY_TRUCK; TAREK (CHAR_TAREK_A0)
- **Action:** Soldiers and civilians climb over the tailgate into the canvas-covered back, hands pulling each other up, while Tarek swings up into the cab.
- **Dialogue:** —
- **Sound:** boots on steel; the tailgate chains; the cab door slamming
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: soldiers and civilians climb over the tailgate of {PROP_ARMY_TRUCK.SHORT}, hands pulling each other up into the dark canvas-covered back, while {CHAR_TAREK.SHORT} swings up into the cab at frame left. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ARMY_DETAIL.NEG}, tan combat helmets, more than two clear faces, lettering on vehicles, weapon facing camera
- **Refs:** PROP_ARMY_TRUCK_REF, CHAR_ARMY_DETAIL_still, CHAR_TAREK_A_full, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Continuity:** In the back (for Seq 5): Tut, Nour, Tomas, Adaeze, Rami (kit), Fathi, Mina, Youssef, Karim. Hassan drives, Tarek in the cab.

### 04.09.006 — INT. GEM LOADING DOCK - NIGHT — Amber slits come down the long white corridor, in a line   (6 s)
- **Shot:** POV from the truck bed through the open roller door, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×6 hero (in a line, VFX-EXTEND)
- **Action:** Far down a long white corridor inside the building, a line of amber slits comes toward the dock, unhurried, in single file.
- **Dialogue:** SESHAT (V.O., every speaker): "Please remain where you are."
- **Sound:** SESHAT from every speaker in the building, faint through the door; a far, even ticking
- **PROMPT:** Point-of-view shot, anamorphic 75mm lens, locked-off, from the dark back of a truck through an open roll-up door: far down a long white corridor inside the building, a line of robots, each {UNIT_SHABTI.SHORT}, walks toward the dock in single file with smooth, unhurried, even steps, their amber slits glowing in a row. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}, the corridor lit by cool emergency downlights. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running robots, robots in formation like soldiers, weapons
- **Refs:** UNIT_SHABTI_REF_A, LOC_GEM_LOADING_DOCK_BLACKOUT_plate, LOC_GEM_CC_EMERG_plate
- **Flags:** VFX-EXTEND
- **Continuity:** Nour's POV. The units are standing again after the nine seconds. They never hurry: SESHAT follows and contains (bible §3.1).

### 04.09.007 — INT. GEM LOADING DOCK - NIGHT — Nour watches them come   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** At the tailgate in the dark truck bed, Nour stares back at the building, faint amber light moving on her face.
- **Dialogue:** SESHAT (V.O., every speaker): "The world is being made safe."
- **Sound:** SESHAT's even voice; the diesel revving
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, sits at the tailgate in the dark back of a truck and stares back toward the building, faint amber light moving across her face, her jaw tight. Setting: {LOC_ARMY_TRUCK.SHORT}, the truck still parked at {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}, dark inside the truck bed, faint amber light from the building on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, passing headlights, moving road, crying openly, glasses worn on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_ARMY_TRUCK_NIGHT_plate, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Continuity:** The truck is still at the dock (not yet moving): so the prompt uses the dock's BLACKOUT light, not LOC_ARMY_TRUCK LIGHT_NIGHT (whose passing lamps start when the truck moves, 04.09.009); the amber is from the corridor.

### 04.09.008 — INT. GEM LOADING DOCK - NIGHT — The truck lurches out   (5 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** PROP_ARMY_TRUCK
- **Action:** The truck lurches away from the platform across the oil-stained yard and out into the dark, its rear canvas flap swinging.
- **Dialogue:** —
- **Sound:** the diesel roaring up; gears; gravel; then the empty dock
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {PROP_ARMY_TRUCK.LONG}, lurches away from the raised platform across the oil-stained yard and out through the perimeter gate into the dark, its rear canvas flap swinging, leaving the dock empty. Setting: {LOC_GEM_LOADING_DOCK.SHORT}, at night. Lighting: {LOC_GEM_LOADING_DOCK.LIGHT_BLACKOUT}, the truck's dim lamps pulling away. Mood: silent, taut, then gone. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lettering on vehicles, military markings, flags, lit lamp masts, floodlit pyramids
- **Refs:** PROP_ARMY_TRUCK_REF, LOC_GEM_LOADING_DOCK_BLACKOUT_plate
- **Continuity:** Exits frame right (continuing the escape direction). The pyramids are not shown: Seq 5 opens on them, unlit, through the rear flap.

### 04.09.009 — INT. GEM LOADING DOCK - NIGHT — Through the rear flap: the museum shrinks, lit from inside by small amber lines   (6 s)
- **Shot:** POV through the rear flap, anamorphic 50mm, vehicle-mounted · **Move:** vehicle-mounted
- **In frame:** LOC_ARMY_TRUCK (rear flap framing); the museum façade receding (VFX-EXTEND)
- **Action:** Through the open rear flap the huge pale building shrinks into the desert night, its translucent stone wall lit from inside by rows of small amber lines.
- **Dialogue:** —
- **Sound:** the engine; the canvas snapping; wind
- **PROMPT:** Point-of-view shot, anamorphic 50mm lens, vehicle-mounted, through the open rear flap: framed by {LOC_ARMY_TRUCK.LONG}, a huge pale modern building shrinks away behind them into the desert night, its translucent stone wall glowing from inside with rows of small amber lines. Setting: a dark road leading away from the museum, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, floodlit pyramids, city skyline lit, readable signage on the building, fire
- **Refs:** LOC_ARMY_TRUCK_NIGHT_plate, LOC_GEM_ROOF_DAY_plate (façade reference)
- **Flags:** VFX-EXTEND
- **Continuity:** The amber lines are the units standing inside (comp can place them on the façade plate). No pyramids in this shot (Seq 5 opens on them).

### 04.09.010 — INT. GEM LOADING DOCK - NIGHT — ON NOUR'S FACE. Jaw set. Eyes still in the atrium.   (7 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_B0)
- **Action:** In the dark truck bed, Nour's face: jaw set, her eyes fixed on something far behind them.
- **Dialogue:** —
- **Sound:** the engine; the canvas; nothing else. END OF ACT ONE.
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, sits in the swaying dark of the truck bed, jaw set, her deep-set eyes fixed on something far behind them, a last faint amber light sliding off her cheek. Setting: {LOC_ARMY_TRUCK.SHORT}, at night. Lighting: {LOC_ARMY_TRUCK.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears streaming, glasses worn on the face, smiling
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_ARMY_TRUCK_NIGHT_plate
- **Continuity:** Hands off to Seq 5, which opens on "NOUR'S FACE, as we left it". Hold the last frame for the act-out. Nour B0, uninjured; pendant at her throat.

