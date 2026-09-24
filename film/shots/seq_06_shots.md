# HERE AM I — SEQUENCE 6: "THE RIVER" — shot list and AI-video prompts

Screenplay: `screenplay/seq_06.fountain` (pp. 41–51; 5 November 2033, 03:40 → 12:04, Cairo → opposite Amarna). Story bible §7 Seq 6, §11 (motifs, palette), §12 (continuity board, S5–6 column). Photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

**Shot count:** 132 · **Running time:** 769 s = 12.8 min (target ≈ page count: 11 pages → 11 min, ±20% = 8.8–13.2 min; within range, the dialogue-dense dawn Q&A pushes it long) · **Average shot:** 5.8 s

**Flags used:** COMP ×24, EXTEND ×6, VFX-ASSIST ×22, VFX-EXTEND ×10

## Scenes

| Scene | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 06.01 | EXT. NILE, SOUTH OF CAIRO - NIGHT | 06.01.001 – 06.01.002 | 2 | 13 s |
| 06.02 | INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS | 06.02.001 – 06.02.007 | 7 | 39 s |
| 06.03 | EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS | 06.03.001 – 06.03.021 | 21 | 117 s |
| 06.04 | EXT. NILE, FISHING GROUNDS - CONTINUOUS | 06.04.001 – 06.04.010 | 10 | 59 s |
| 06.05 | INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS | 06.05.001 – 06.05.009 | 9 | 48 s |
| 06.06 | EXT. NILE, ISLAND CHANNEL - CONTINUOUS | 06.06.001 – 06.06.011 | 11 | 65 s |
| 06.07 | EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN | 06.07.001 – 06.07.017 | 17 | 103 s |
| 06.08 | EXT. NILE - DAWN | 06.08.001 – 06.08.028 | 28 | 174 s |
| 06.09 | INT. POLICE LAUNCH, WHEELHOUSE - MORNING | 06.09.001 – 06.09.009 | 9 | 55 s |
| 06.10 | EXT. NILE - CONTINUOUS | 06.10.001 – 06.10.007 | 7 | 34 s |
| 06.11 | EXT. NILE OPPOSITE AMARNA - MIDDAY | 06.11.001 – 06.11.011 | 11 | 62 s |

## How this list is built

- Fixed wording is inserted by tokens and expanded by `shots_md2jsonl.py` from `production_bible/locks.json` and file 05 (§1.1 suffix, §2 negatives). One LONG lock per prompt (05 §5.2); the writer's own words stay ≤ 70 per prompt (05 §5.3; checked by script).
- **Geography** (file 03 entry 20): south / upriver = frame RIGHT in every profile of the launch; the flies and the barge come from the NORTH (astern = frame LEFT); in 06.10 the flies come out of the EAST sun (frame left from the wheel). Aft-deck setup for 06.03: camera by the wheelhouse looking aft, Tut on the engine hatch facing south, Nour with her back to the south; the star Sopdet sits above her head over the wheelhouse roof (COMP star element). Amarna: the plain opens frame left → right across the river; Tut faces WEST, hood up.
- **Light** (bible §11; 05 §3): every night shot names its key: starlight (LOC_NILE_NIGHT + GRADE_NIGHT_ACTION), the flies' white pinpoints, the fishermen's lanterns, the felucca fire, the muzzle flashes; pre-dawn = Adaeze's white headlamp (L2); day = GRADE_2033_DAY, never a desert filter. The launch runs with NO lights: STATE_L1's red lamp is withheld, as in Seq 5 (05 §14 Q2).
- **Wardrobe and states** (file 01; bible §12): Tut A1 (gown under Tarek's charcoal jacket, hood back, dagger in the sash, nape PORT, G0) from 06.01 to 06.07; the port is cut at 06.07.011–012 → SCAR, G0 → **G0f** (COMP), foot stall and RIGHT-hand tremor from 06.07.015–016; the **dawn change** to T-B1 (cut-down tunic, Karim's cargo trousers, dagger in its gold sheath on the belt at the right hip) from 06.08.002; hood UP only opposite Amarna (06.11). **State overlays in the prompts (QA pass 2):** G0 once pre-cut (06.03.002), G0f at 06.07.014, 06.08.005, 06.09.008 (all COMP glow elements); nape SCAR first seen 06.07.017; tremor 06.07.016, 06.09.007, 06.11.007; ebony stick (ST1) 06.03.001, 06.08.002, 06.09.007, 06.11.005, 06.11.007; foot 06.03.001, 06.07.015, 06.08.002; damage L1 + L1_RIVER on the B look from dawn. Nour B1 (pendant unclasped 06.03.004 → her fist → re-clasped by dawn). Adaeze B1, headlamp (white) from 06.07. Tomas B (no headlamp; stopwatch from 06.07.016). Tarek B (handset clipped on at 06.09.009). Fathi B1 (river-wet to the knees). Rami B1 (splint LEFT, notebook STATE_DAMP). Mina, Youssef A1 (tan helmets).
- **Safety** (05 §7): no human dies in Seq 6. Rifles fire across frame toward the stern, away from the lens (06.03.015). The dagger cuts only the thread (06.03.018). The felucca burns EMPTY after its crew are seen clear and hauled out (06.04.007–009). The fly strikes the rail, not Tarek (06.10.004). The port cut is hands, tool, sliver and faces only, never a wound (06.07.010–012; NEG_REMAINS). Garden sleepers are adults only (NEG_GARDEN). "Heart" appears only in Dialogue fields.
- **CHAR_TUT.NEG is withheld** in the three pendant shots 06.03.005, 06.03.007, 06.03.008 because its "jewellery" term would fight the pendant (05 §2.3); its key terms are typed in by hand instead. For the same reason it is withheld in the dagger insert 06.03.018 (the jewelled hilt). CHAR_TOMAS.NEG is withheld in 06.03.001 and 06.11.006 because its "glasses" term would fight Adaeze's and Rami's glasses.
- **Dialogue** (05 §9): Egyptian Arabic (Tarek, Fathi, the old fisherman) and Late Egyptian (Tut 06.07.013 and 06.11.005, Nour 06.11.009) are COMP-subtitled and recorded before generation; SESHAT is V.O. only, radio-futzed, no sync. Long speeches are split across a speaker clip and a listener/O.S. cover (06.03.005–006, 06.08.016–018, 06.09.002–004).
- **Flags for the lead:** (1) the Asyut lock (LOC_ASYUT_LOCK, file 03 entry 21) has no scene in the current pages; Seq 6 ends heading for it. (2) The screenplay has the fly over the felucca and the snagged flies "blinking" (file 02 says fly lights never blink); the screenplay is followed. (3) The screenplay's "wheelhouse's back rail, just above Tut's head" is staged as a canopy rail running back from the wheelhouse roof over the engine hatch (06.03.001). (4) The dawn Q&A runs long (28 shots, about 3 min) because it carries every line of the rapid-fire list; if the cut needs time, tighten the pauses in the OTS question-and-answer shots rather than drop lines.
- `[[verify]]` items carried from the screenplay: the Asyut lock (06.02.005); the 5 Nov 2033 ephemeris for Sirius on the meridian at 03:40 and the Great Bear "on end" before dawn (06.03.006–007, 06.06.003); lantern night-fishing (06.04.001); Fairall 1999 (06.08.005); the Nobiin "Aman Dawu" (06.08.022); the transliteration *itrw* (06.08.023).

## Reference stills needed

Attach per shot as listed in `Refs:`; generate once with one image model, approve, freeze (05 §12). Count = number of shots using it.

**Characters**
- `CHAR_ADAEZE_A_34` (6)
- `CHAR_ADAEZE_A_front` (7)
- `CHAR_ADAEZE_B_full` (9)
- `CHAR_FATHI_A_34` (9)
- `CHAR_FATHI_A_front` (9)
- `CHAR_FATHI_B_full` (13)
- `CHAR_GARDEN_SLEEPERS_REF` (1) — extras still for the Garden rows (adults only), per file 01 §10
- `CHAR_MINA_A_front` (1)
- `CHAR_MINA_A_full` (2)
- `CHAR_NIGHT_FISHERMEN_still` (6) — group still in context (file 01 §10b); adults only
- `CHAR_NOUR_A_34` (7)
- `CHAR_NOUR_A_front` (9)
- `CHAR_NOUR_B_full` (13)
- `CHAR_OLD_FISHERMAN_front` (3) — one-scene face (file 01 §10b)
- `CHAR_RAMI_A_34` (6)
- `CHAR_RAMI_A_front` (6)
- `CHAR_RAMI_B_full` (12)
- `CHAR_TAREK_A_34` (3)
- `CHAR_TAREK_A_front` (3)
- `CHAR_TAREK_B_full` (6)
- `CHAR_TOMAS_A_34` (2)
- `CHAR_TOMAS_A_front` (3)
- `CHAR_TOMAS_A_full` (2)
- `CHAR_TOMAS_B_work` (7) — the 6.2 working look (file 01; renamed from _headlamp)
- `CHAR_TUT_A0_34` (32)
- `CHAR_TUT_A0_front` (36)
- `CHAR_TUT_A1_full` (21) — derived still (as in Seq 5): Tut in T-A1, the A0 gown under the oversized charcoal hooded field jacket, hood down; image-edit of CHAR_TUT_A0_full plus the B jacket (INDEX open item 7)
- `CHAR_TUT_B1_full` (18) — first use: the dawn change (06.08.002 on)
- `CHAR_TUT_B_night_34` (3) — used by day for the hood-up stern shots opposite Amarna
- `CHAR_TUT_FOOT` (3) — the foot insert 06.07.015 and the two deck masters 06.03.001, 06.08.002
- `CHAR_TUT_HANDS` (3)
- `CHAR_TUT_NAPE_PORT` (2) — last use of the port (06.07.002)
- `CHAR_TUT_NAPE_SCAR` (1) — first sight of the scar, from behind (06.07.017)
- `CHAR_YOUSSEF_A_front` (1)
- `CHAR_YOUSSEF_A_full` (2)

**Units**
- `UNIT_FLY_REF_A` (9) — plus the FLY 3D asset; threads are VFX lines (file 02 §6)
- `UNIT_FLY_REF_B` (7)
- `UNIT_FREIGHT_BARGE_REF` (6) — file 02 §14.6 REF (plate/prop, no 3D base model)
- `UNIT_NURSE_REF_A` (1)
- `UNIT_SHABTI_REF_A` (7) — plus the SHABTI 3D asset for the thread climb

**Props**
- `PROP_DAGGER_REF` (3)
- `PROP_EBONY_STICK_REF` (5) — ST1 (dusty) all sequence
- `PROP_FELUCCA_REF` (10)
- `PROP_LAYLA_PENDANT_REF` (7) — plus the COMP cartouche artwork (file 04 §11) for the macro insert
- `PROP_MULTITOOL_REF` (2)
- `PROP_POLICE_HANDSET_REF` (2)
- `PROP_POLICE_LAUNCH_REF` (27) — grey steel, unmarked; runs with NO lights at night (L1 red lamp withheld, 05 §14 Q2); L2 pre-dawn, L3 from dawn
- `PROP_PORT_SLIVER_REF` (2)
- `PROP_RAMI_NOTEBOOK_REF` (2) — plus the COMP handwriting asset (title and pages)
- `PROP_STOPWATCH_REF` (1)

**Location plates**
- `LOC_AMARNA_PLAIN_2033/GARDEN_MIDDAY` (1) — the approved Garden plate (file 03 entry 36) relit to MIDDAY with the shades OPEN; clean plate for VFX-EXTEND
- `LOC_AMARNA_PLAIN_2033/STELA_MIDDAY` (1) — long-lens plate of the cliff stela, no legible relief
- `LOC_AMARNA_PLAIN_2033_MIDDAY` (1)
- `LOC_NILE/FISHING_GROUNDS_NIGHT` (11) — area-add-on plate with 4–6 hero boats + clean plate for VFX-EXTEND
- `LOC_NILE/ISLAND_DAWN` (12) — area-add-on plate: moored under tamarisks, pre-dawn (LIGHT_DAWN relit darker: "first grey in the east")
- `LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE` (7) — area-add-on plate: the east bank opening to the plain, sun-shades glinting
- `LOC_NILE_DAWN` (27)
- `LOC_NILE_DAY` (15)
- `LOC_NILE_MIDDAY_HAZE` (1)
- `LOC_NILE_NIGHT` (45)

Also required for comp: the seq 06 subtitle file (Egyptian Arabic and Late Egyptian lines) and SUPER file ("5 NOVEMBER. 03:40.", "05:10", "12:04"); two ephemeris star-field plates (the south sky at 03:40 with Sirius; the north-east sky before dawn with the Great Bear on end); the G0f chest-glow element (file 01); the pendant's LAYLA cartouche artwork (file 04 §11); Rami's notebook handwriting (file 04 §19.2); the spoofed-watch and stopwatch LCD elements; the binocular matte; VFX thread lines for every fly.

---
## Scene 06.01 — EXT. NILE, SOUTH OF CAIRO - NIGHT

### 06.01.001 — EXT. NILE, SOUTH OF CAIRO - NIGHT — Stars part at the bow   (6 s)
- **Shot:** Insert, anamorphic 75mm, just above the waterline · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (bow only, running dark); the star field reflected on the water
- **Action:** Black water full of reflected stars; a grey steel bow slides through from frame left to right; the stars shiver apart around it and close again behind.
- **Dialogue:** —
- **Sound:** water folding off the stem, the diesel's low pound under it, nothing else on the river; ambient sound only, no dialogue
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: just above the surface, black water holds a dense field of reflected stars; the grey steel bow of {PROP_POLICE_LAUNCH.SHORT}, running dark, slides through from frame left to right, the reflected stars shivering apart around it and closing again behind. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: hushed and beautiful, a held breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, navigation lights, searchlight beam, lit windows, moon in frame, city skyglow, readable markings on the hull, people
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Opens Seq 6 on 5 Nov, 03:40, about two and a half hours after the launch left the Corniche (end of 05.08). Screen direction (file 03 entry 20): south / upriver = frame RIGHT for the whole sequence. The launch runs with NO lights; STATE_L1's red wheelhouse lamp stays withheld (05 §14 Q2, as in 05.08.001). VFX-ASSIST: if the reflection does not break and re-form cleanly, comp the star field on a clean water plate and warp it around the bow wave.

### 06.01.002 — EXT. NILE, SOUTH OF CAIRO - NIGHT — The launch runs south, not a lamp on either bank   (7 s)
- **Shot:** Extreme wide establishing shot, anamorphic 75mm, profile from the west bank · **Move:** slow pan right with the launch
- **In frame:** PROP_POLICE_LAUNCH (small, dark figures aboard); both banks black
- **Action:** The dark launch runs south (frame right) down the middle of the wide black river; palms and villages on both banks are black silhouettes with not a single lamp; its wake is a faint silver line.
- **Dialogue:** —
- **Sound:** the diesel far off, crickets on the bank, water; no dogs, no generators, no traffic
- **PROMPT:** Extreme wide establishing shot, anamorphic 75mm lens, slow pan right: small in the middle of the river, {PROP_POLICE_LAUNCH.SHORT}, running dark with a few dark figures on its aft deck, travels steadily toward frame right, its wake a faint silver line; both banks are black silhouettes of palms and villages without one lit window. Setting: {LOC_NILE.LONG}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: lonely, the whole valley holding its breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit windows, street lamps, car headlights on the banks, navigation lights, searchlight, moon in frame, skyglow, drones in the sky
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "5 NOVEMBER. 03:40." | lower left, small, per 05 §13.7 | from 1 s in to 6 s | seq 06 SUPER file
- **Continuity:** The launch carries ten: Tut, Nour, Adaeze, Tomas, Rami, Tarek, Fathi, Mina, Youssef, Karim (file 04 §13). Blackout rule (file 03 §0 item 12): no skyglow, no lit windows. No flies in the sky yet: they appear in 06.03.010.

---

## Scene 06.02 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS

### 06.02.001 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Fathi squints into starlight   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi grips the wheel and squints forward through the salt-hazed glass, reading the black water by starlight.
- **Dialogue:** —
- **Sound:** the diesel through the deck, the wheel's worn spokes creaking, water on the hull
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: in a cramped dark wheelhouse, {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L1}, grips a worn wooden wheel and squints forward through salt-hazed glass, eyes narrowed, reading black water he cannot see. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight through the windows modelling his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, glowing screens, lit instrument panel, bright interior light, daylight
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Wheelhouse geography for all of Seq 6: the wheel at centre facing forward (south); the chart ledge to its left; the old police set and the handset cradle to its right; the door aft (frame right when we face the wheel). Fathi: B1, red scarf at the neck, bareheaded, river-wet to the knees. Lift his key in grade: faces must read (05 §3.2).

### 06.02.002 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Tarek over the paper chart   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, slightly high · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1); the paper river chart (PROP_POLICE_LAUNCH chart state)
- **Action:** Tarek bends over a soft old paper chart on the ledge and traces the river south with one thick finger.
- **Dialogue:** —
- **Sound:** paper rustle, the diesel, Tarek's breath through his moustache
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, slightly high: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, bends over {PROP_POLICE_LAUNCH.STATE_CHART_INSERT} and slowly traces the river south with one thick finger, frowning, the paper barely visible in the dark. Setting: the cramped wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight through the salt-hazed windows on his face and the paper. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, readable map labels, printed place names, glowing screens, torch beam
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The chart (PROP_POLICE_LAUNCH STATE_CHART_INSERT) stays on the ledge all sequence; at 03:40 the pencil line reaches only a little south of Cairo; by 06.09.005 it carries "the whole night's race". No handset on Tarek's vest yet (it is clipped on in 06.09.008).

### 06.02.003 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — The hull scrapes; everyone lurches   (4 s)
- **Shot:** Wide shot, anamorphic 32mm, from the wheelhouse door · **Move:** subtle handheld (the jolt shakes the frame)
- **In frame:** FATHI (CHAR_FATHI_B1), TAREK (CHAR_TAREK_B1)
- **Action:** The hull scrapes over sand; the whole wheelhouse jolts; Fathi is thrown against the wheel and Tarek catches the ledge.
- **Dialogue:** —
- **Sound:** a long grinding SCRAPE under the keel, loose gear clattering, a grunt
- **PROMPT:** Wide shot, anamorphic 32mm lens, subtle handheld, from the doorway: inside the dark wheelhouse the whole boat jolts hard as its hull scrapes over sand; {CHAR_FATHI.SHORT} is thrown against the wheel and {CHAR_TAREK.SHORT} catches the chart ledge with both hands, a loose mug sliding off. Setting: the cramped wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight through the windows. Mood: sudden alarm, bodies braced. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TAREK.NEG}, falling bodies, injury, broken glass, bright interior light
- **Refs:** CHAR_FATHI_B_full, CHAR_TAREK_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Geography: camera in the aft doorway looking forward (south); Fathi at the wheel frame centre, Tarek at the chart ledge frame left.

### 06.02.004 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Full astern   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** FATHI's hand on the throttle lever
- **Action:** A broad dark-brown hand slams a worn throttle lever back to full astern; the console shudders as the boat drags herself off the sand.
- **Dialogue:** —
- **Sound:** the lever's clunk, the diesel roaring in reverse, sand hissing off the hull
- **PROMPT:** Insert, 100mm macro lens, locked-off: a broad dark-brown hand slams a worn black throttle lever all the way back, and the scuffed metal console shudders and rattles under it as the boat strains backward. Setting: the dark wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, at night. Lighting: faint cool starlight across the worn metal. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable dials, numbers, labels, glowing screens, extra fingers
- **Refs:** CHAR_FATHI_B_full, PROP_POLICE_LAUNCH_REF
- **Flags:** —
- **Continuity:** After this the launch is off the bar and running again; no damage to the hull.

### 06.02.005 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Tarek: the lock at Asyut   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek straightens from the ledge, taps the chart and speaks to Fathi (off frame right) in Egyptian Arabic.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "The first lock south is Asyut. It's networked. If it knows we're on the water before we get there, it shuts the gates. And we walk."
- **Sound:** the diesel settling back to its pound; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, straightens from the chart ledge, taps the paper once and, looking off frame right, speaks several short sentences in Egyptian Arabic, low and flat, the last one heavier. Setting: the dark wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight through the salt-hazed windows on his face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, readable map labels, glowing screens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "The first lock south is Asyut. It's networked. If it knows we're on the water before we get there, it shuts the gates. And we walk." | lower third, two lines max, split into two cards at "networked." | line in to out | seq 06 subtitle file (screenplay carries [[verify: Asyut lock]])
- **Continuity:** Recorded by a native Egyptian speaker before lip-sync (05 §9.7). Brisk, flat delivery (about 3 words/s) fits 8 s; if the recording runs past 8 s, cover the tail ("And we walk.") on 06.02.006's first second.

### 06.02.006 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Fathi: if I knew the time   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Eyes still on the dark water, Fathi answers in Egyptian Arabic, dry, half a joke.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "If I knew the time, I'd know where we are. If I knew where we are, I'd know where the sand is."
- **Sound:** the diesel; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, keeps both hands on the wheel and his eyes on the black water ahead, speaking in Egyptian Arabic, two dry sentences with a faint tired smile at the end. Setting: the dark wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight through the salt-hazed windows on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, glowing screens, bright interior light
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "If I knew the time, I'd know where we are. If I knew where we are, I'd know where the sand is." | lower third, two lines | line in to out | seq 06 subtitle file
- **Continuity:** Fathi looks forward (frame left of lens), never at Tarek: the reverse of 06.02.005 holds the line with Tarek at frame left of the wheel.

### 06.02.007 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — The watch will not settle   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TAREK's wrist and watch; the chart soft behind
- **Action:** Tarek lifts his wrist; the small display of his satellite watch flickers from one reading to another and will not settle. At the tail, a voice from the deck aft.
- **Dialogue:** TUT (O.S.): "I can tell you the hour."
- **Sound:** a tiny electronic chirp with each false reading; the diesel; then Tut's voice, quiet, from outside
- **PROMPT:** Insert, 100mm macro lens, locked-off: a thick weathered wrist with a rugged black unbranded digital field watch lifts into frame; its small dim display flickers and jumps from one reading to another again and again, never settling, while a paper chart lies soft and dark below. Setting: the dark wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: the watch's faint cold display glow on the skin, starlight beyond. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable digits, brand name on the watch, logo, bright screen
- **Refs:** CHAR_TAREK_B_full, PROP_POLICE_LAUNCH_REF
- **Flags:** COMP
- **Comp:** watch display | the times 04:10, 02:51, 11:37 in plain LCD segments, each held about 1 s | replace the generated display, tracked | from 0.5 s to 5 s | display element built in comp (spoofed GNSS)
- **Continuity:** Tarek's watch has no bible token (screenplay object; generic, unbranded). Tut's O.S. line pulls both men's heads aft: next scene, the aft deck.

---

## Scene 06.03 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS

### 06.03.001 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Master: the aft deck under the Milky Way   (6 s)
- **Shot:** Wide shot (master), anamorphic 32mm, from beside the wheelhouse looking aft · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1) on the engine hatch, facing camera; ADAEZE (CHAR_ADAEZE_B1), TOMAS (CHAR_TOMAS_B1), RAMI (CHAR_RAMI_B1) huddled along the gunwales, soft; MINA (CHAR_MINA_A1), YOUSSEF (CHAR_YOUSSEF_A1) at the stern, backs to camera
- **Action:** Tut sits on the engine hatch, hood back, face tipped up to the Milky Way; the others huddle along the gunwales; at the stern two soldiers face aft over the wake, rifles held ready.
- **Dialogue:** —
- **Sound:** the diesel under the hatch, the wake hissing, a rifle sling creaking; no voices
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off, from beside the wheelhouse looking aft: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.STATE_FOOT}, sits on the engine hatch facing camera, hood back, face tipped up to the Milky Way, beside him on the hatch {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST1}; {CHAR_ADAEZE.SHORT}, {CHAR_TOMAS.SHORT} and {CHAR_RAMI.SHORT} huddle soft along the gunwales; at the stern, backs to camera, {CHAR_MINA.SHORT} and {CHAR_YOUSSEF.SHORT} face the wake, rifles held across their bodies. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT} on {LOC_NILE.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}, starlight on faces. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_RAMI.NEG}, {CHAR_MINA.NEG}, {CHAR_YOUSSEF.NEG}, more than three clear faces, rifles pointed toward camera, deck lights, torches, moon in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A1_full, CHAR_ADAEZE_B_full, CHAR_TOMAS_A_full, CHAR_RAMI_B_full, CHAR_MINA_A_full, CHAR_YOUSSEF_A_full, CHAR_TUT_FOOT, PROP_EBONY_STICK_REF, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Aft-deck geography for 06.03: the wheelhouse is forward (south); Tut sits on the engine hatch just aft of it, facing south; a steel canopy rail runs back from the wheelhouse roof over the hatch (the screenplay's "wheelhouse's back rail, just above Tut's head"); the stern and the wake are north. In profile shots, astern = frame LEFT, the bow = frame RIGHT. Tut: A1 (the gown under Tarek's charcoal jacket, hood back), L1 + river marks, dagger in the sash (hidden under the jacket), nape PORT, G0 hidden under the half-zipped jacket, the ebony stick laid on the hatch beside him. Nour is forward, out of frame, until 06.03.003. Karim is in the wheelhouse door, unseen. QA: the foot overlay and the stick (ST1, dusty; file 04) are now in the prompt. CHAR_TOMAS.NEG is withheld here and in 06.11.006 because its "glasses" term would fight Adaeze's and Rami's glasses (05 §2.3).

### 06.03.002 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — "Give me something heavy on a string"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut lowers his eyes from the sky to Nour (just off lens left) and asks for a weight on a string, one hand open.
- **Dialogue:** TUT: "Dr. Kamel. Sit facing me. Give me something heavy on a string."
- **Sound:** the wake; the diesel; his voice soft on the s and p
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.STATE_G0}, hood back, lowers his eyes from the sky to someone just off the lens at left and speaks quietly, three short sentences, calm and precise, one slender hand turning open. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT} on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face, the Milky Way soft behind him. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, torch light on the face
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green (#A6F2C2 core falling off to #3F8F6A), dim, one slow even swell every 4 s, about 6 cm of spill (file 01 glow table) | centre of the chest through the gown in the gap of the half-zipped jacket, tracked | whole shot | glow element library (file 01)
- **Continuity:** Eyeline just off lens LEFT = Nour, who will sit with her back to the bow (south), facing him. Hood DOWN for dialogue (file 01 A1). G0 (steady, pre-cut) is shown once here so the G0f stutter after the port cut (06.07.014, 06.08.005, 06.09.008) reads as a change.

### 06.03.003 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Nour sits facing him, and hesitates   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour sits on the deck facing him, her back to the south; a hesitation; her hand rises to the small silver pendant at her throat.
- **Dialogue:** —
- **Sound:** the wake; her breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, lowers herself to sit on the deck facing someone just off frame right, the dark wheelhouse behind her; she hesitates, then lifts one hand to {PROP_LAYLA_PENDANT.SHORT}, {PROP_LAYLA_PENDANT.STATE_STANDARD}. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, torch light, tears
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Nour B1: the olive field jacket over the black blouse, river-damp cuffs, glasses on their cord, the pendant at her throat. The pendant is Layla's gift: the hesitation is that.

### 06.03.004 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — She unclasps the cartouche   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** NOUR's hands; PROP_LAYLA_PENDANT
- **Action:** Her fingers undo the clasp at the back of her neck and draw the silver cartouche off her throat into her palm, slowly.
- **Dialogue:** —
- **Sound:** the tiny click of the clasp; the chain whispering
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's slender fingers undo a tiny clasp and slowly draw {PROP_LAYLA_PENDANT.LONG} off her throat and into her open palm, the fine chain pooling after it, the fingers closing once, reluctant, before offering it. Setting: on the dark aft deck of a river launch, the olive cloth of a field jacket behind, at night. Lighting: faint cool starlight glinting on the silver. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, legible hieroglyphs, engraved letters, extra fingers, jewellery box
- **Refs:** PROP_LAYLA_PENDANT_REF, CHAR_NOUR_B_full
- **Flags:** COMP
- **Comp:** pendant face | the Egyptologist's LAYLA cartouche artwork (proposed E23 G1 M17 M17 E23 G1; file 04 §11) replacing the generated signs, only if legible at this size | tracked on the pendant face | whole shot | file 04 §11 COMP artwork
- **Continuity:** The pendant leaves her throat here and returns to her palm in 06.03.008 (STATE_CLUTCHED); she re-clasps it off screen before dawn (STATE_STANDARD in 06.08).

### 06.03.005 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — A plumb line: the priests on his father's roof   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, over Nour's soft shoulder · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); PROP_LAYLA_PENDANT (plumb line); NOUR (foreground shoulder, soft)
- **Action:** Tut holds the pendant up by its chain at arm's length; it sways, then steadies into a plumb line; sighting past it at the sky, he begins to tell how the priests read the hours.
- **Dialogue:** TUT: "On my father's roof, two priests sat like this all night,"
- **Sound:** the wake; the chain's faint tick against his knuckle
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, over a soft dark shoulder in the foreground: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, holds {PROP_LAYLA_PENDANT.SHORT} up by its chain at arm's length; it sways, then hangs still, {PROP_LAYLA_PENDANT.STATE_PLUMB_LINE}; sighting past it at the sky, he begins to speak quietly, a remembered story, eyes on the stars. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face and the silver. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, alien, grey skin, oversized black eyes, glowing skin, visible circuitry, a full head of hair, beard, crown, heavy eye makeup, legible hieroglyphs, swinging pendant at the end, torch light
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The line continues over 06.03.006 (from behind him, no sync needed). CHAR_TUT.NEG is withheld here and in 06.03.006–008 because its "jewellery" term fights the pendant (05 §2.3 "never negate what the shot needs"); its other key terms are typed in. The pendant hangs from his RIGHT hand (the stick lies on the hatch). The foreground shoulder is Nour's (olive), no face.

### 06.03.006 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — The brightest star stands on the line   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, from behind Tut · **Move:** locked-off
- **In frame:** TUT (back of the shaved head and jacket, soft foreground); PROP_LAYLA_PENDANT; NOUR (CHAR_NOUR_B1) facing camera; the sky above her
- **Action:** From behind Tut's head: the pendant hangs dead still on its chain; below it Nour looks up at him; above her head the brightest star in the sky sits exactly on the line of the chain.
- **Dialogue:** TUT (continuing, from behind; no sync): "calling each hour by the star on the other man's ear. Or opposite his heart."
- **Sound:** Tut's voice close and soft behind the lens; the wake; on "heart" a held breath
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past a young man's soft shaved head in the foreground, his raised hand holds a small silver pendant dead still on its chain; below it {CHAR_NOUR.SHORT} sits looking up at him; above her head the brightest white star in the sky sits exactly on the chain's line, above the dark wheelhouse roof. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, at night. Lighting: {LOC_NILE.LIGHT_NIGHT}, starlight on her face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, moon, planets, lens flare, star cross flare, visible face of the foreground figure, torch light
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, CHAR_TUT_A1_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** star element | Sirius, the brightest star, placed exactly on the chain line above Nour's head, with a subtle scintillation; the surrounding field matched to the 5 Nov 2033, 03:40, Middle Egypt sky (south meridian) | upper centre, tracked to the chain | whole shot | star-field plate from the ephemeris (screenplay [[verify: ephemeris]])
- **Continuity:** Looking SOUTH over Nour: the wheelhouse roof below the star. This is Tut's merkhet (file 04 §11 STATE_PLUMB_LINE; PROP_MERKHET_BAY is RESERVE).

### 06.03.007 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — "Sopdet. Opposite your heart."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut reads the star, then touches two fingers to his temple and converts the hour into hers.
- **Dialogue:** TUT: "Sopdet. Opposite your heart. The end of the tenth hour." (two fingers to his temple) "In your hours: two and a little more before the sun."
- **Sound:** the wake; the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, the silver chain still hanging from his raised hand, reads the sky, speaks one short sentence, then touches two fingers to his temple and speaks again, precise, a faint pleased certainty. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, alien, grey skin, oversized black eyes, glowing skin, visible circuitry, a full head of hair, beard, crown, heavy eye makeup, torch light
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The screenplay carries [[verify: ephemeris, 5 Nov 2033, Middle Egypt: Sirius on the meridian c. 03:40, about 2.5 h before sunrise]]. If the recording runs over 8 s, cut to 06.03.008 on "two and a little more".

### 06.03.008 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — He gives it back; "That one is walking."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); NOUR's hand entering frame
- **Action:** Tut lays the pendant back in Nour's palm (her hand enters frame left), looks up past her, and frowns.
- **Dialogue:** TUT: "That one is walking."
- **Sound:** the chain slipping into her palm; the wake; a beat of silence
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, lowers the silver pendant into a woman's open palm that enters from frame left, then turns his head to look back over his left shoulder at the sky behind him, and his brows draw together in a slow frown as he speaks one short sentence. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, alien, grey skin, oversized black eyes, glowing skin, visible circuitry, a full head of hair, beard, crown, heavy eye makeup, torch light
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Pendant now in Nour's hand (STATE_CLUTCHED). Tut's eyeline turns back over his LEFT shoulder toward the stern and the northern sky: Nour sits SOUTH of him, so he looks away from her, not past her (QA fix).

### 06.03.009 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — White pinpoints low in the north   (6 s)
- **Shot:** Wide shot, anamorphic 135mm, over the stern · **Move:** locked-off
- **In frame:** UNIT_FLY ×3 (pinpoints, far)
- **Action:** Low in the north over the river, a white pinpoint glides above the water, following the river; a second; a third; each trails a hair-thin glint.
- **Dialogue:** —
- **Sound:** at the edge of hearing, a thin mosquito whine rising and falling
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, looking back along the black river over a pale wake: low above the water in the distance, a single cold white pinpoint of light glides steadily upriver toward camera, too low for a star; a second appears beside it, then a third, each trailing a hair-thin glint, {UNIT_FLY.SHORT}. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, blinking coloured navigation lights, red or green lights, aircraft, shooting stars, fireflies, big drones, searchlight
- **Refs:** UNIT_FLY_REF_A, UNIT_FLY_REF_B, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Flies come from the NORTH (astern). In wides only the white pinpoints show; the threads are VFX lines added where light catches them (file 02 §6). Fly light is steady cold white (#F2F6FF).

### 06.03.010 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Adaeze: "They fly on a string."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** At the gunwale, Adaeze stares aft at the lights and names them, flat and fast.
- **Dialogue:** ADAEZE: "Flies. Fibre-optic. Nothing to jam. They fly on a string."
- **Sound:** the whine a little louder; the wake
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L1}, hunched at the gunwale with her hood down, stares off frame left toward the stern, and speaks four clipped sentences, flat and fast, small white points reflecting in her round glasses. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight lifting her deep brown skin. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, glowing screen, laptop open, torch light
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Adaeze B1, the canvas bag on her shoulder; NO headlamp yet (it first appears at 06.07). Lift her key: faces must read.

### 06.03.011 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — The barge in their wake, three amber slits on its bow   (6 s)
- **Shot:** Wide shot, anamorphic 135mm, over the stern · **Move:** slow push-in
- **In frame:** UNIT_FREIGHT_BARGE; UNIT_SHABTI ×3 on its bow
- **Action:** Astern, blacker than the dark, a freight barge steers itself up their wake, unlit and uncrewed; cable spools turn on its deck; on its bow three amber slits.
- **Dialogue:** —
- **Sound:** a low diesel throb not their own; the creak of the spools across the water
- **PROMPT:** Wide shot, anamorphic 135mm lens, slow push-in: blacker than the dark behind the pale wake, {UNIT_FREIGHT_BARGE.LONG}, follows straight up the wake toward camera; three {UNIT_SHABTI.SHORT} stand in a row on its blunt bow, their three small vertical amber slits the only lights aboard. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, crew on deck, lit wheelhouse, navigation lights, searchlight, readable hull markings, containers with logos
- **Refs:** UNIT_FREIGHT_BARGE_REF, UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The barge follows at about 60–80 m; its wheelhouse stays black. Three shabti on the bow here; two after 06.03.019.

### 06.03.012 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — A fly clamps onto the rail above Tut's head   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, low angle · **Move:** locked-off
- **In frame:** UNIT_FLY (clamped); TUT (CHAR_TUT_A1_1) below, looking up
- **Action:** A fly swoops out of the dark from frame left and clamps onto the steel rail just above Tut's head, its thread pulled taut back across the wake.
- **Dialogue:** —
- **Sound:** the whine rising to a snap-past; a hard metallic CLACK as it clamps; then its thin idle hum
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, low angle: {UNIT_FLY.LONG}, swoops in from frame left and clamps onto a steel rail, {UNIT_FLY.STATE_CLAMPED}, the glinting line running back out of frame left over the wake; just below it {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, looks straight up at it, very still. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the fly's white pinpoint lighting the rail. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, rope, cable, thick tether, sparks, explosion, large drone
- **Refs:** UNIT_FLY_REF_A, CHAR_TUT_A1_full, CHAR_TUT_A0_34, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The fly's thread runs from the rail NORTH (frame left in profile) across the wake to the barge's spools. It is the standard hair-thin filament, never a tether (file 02 §6 ruling). VFX-ASSIST: the thread is a VFX line, visible only where it glints.

### 06.03.013 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — A shabti takes the thread and steps off the bow   (6 s)
- **Shot:** Medium wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI (hero) on the barge bow; two more beside it; UNIT_FREIGHT_BARGE
- **Action:** On the barge's bow a shabti reaches up, closes its long fingers around the hair-thin thread, and steps calmly off the bow, hanging by its hands over the black water.
- **Dialogue:** —
- **Sound:** one faint dry ceramic tick; then nothing; the water
- **PROMPT:** Medium wide shot, anamorphic 75mm lens, locked-off: on the blunt bow of a dark steel barge, {UNIT_SHABTI.LONG}, reaches up and closes its long fingers around a single hair-thin glinting thread that rises toward frame right, then steps calmly off the bow and hangs by its hands above black water, legs straight; two identical figures stand motionless behind it. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, three small amber slits. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, chain, harness, thick line, jumping, running, robot waving
- **Refs:** UNIT_SHABTI_REF_A, UNIT_FREIGHT_BARGE_REF, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** "It hangs over black water from a line thinner than a hair. It should not hold. It holds." Hidden rig in the plate; the thread is a VFX line; the hands close on nothing visible between glints (file 02 §6). Shabti D0.

### 06.03.014 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Hand over hand over the wake   (6 s)
- **Shot:** Medium shot, anamorphic 75mm, profile · **Move:** slow pan right
- **In frame:** UNIT_SHABTI (on the thread)
- **Action:** In profile over the churning wake, the shabti climbs the thread hand over hand toward the launch (frame right), legs hanging straight, unhurried.
- **Dialogue:** —
- **Sound:** a faint ceramic tick at each hand; the wake roaring below; the fly's thin hum ahead
- **PROMPT:** Medium shot, anamorphic 75mm lens, slow pan right: in profile, {UNIT_SHABTI.SHORT} hangs from a single hair-thin glinting thread above the churning pale wake and climbs hand over hand toward frame right, legs hanging straight and still, each reach exactly like the last, unhurried. Setting: low over {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, its amber slit the brightest point in frame. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, chain, harness, swinging legs, kicking, fast motion
- **Refs:** UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Direction: barge frame LEFT, launch frame RIGHT (south). The 3D shabti asset may drive the gait (file 02 §0 item 7). 06.03.016 continues this take.

### 06.03.015 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Mina and Youssef fire   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, profile at the stern rail · **Move:** subtle handheld
- **In frame:** MINA (CHAR_MINA_A1), YOUSSEF (CHAR_YOUSSEF_A1)
- **Action:** At the stern rail the two soldiers fire across frame to the left, back along the wake, away from the camera.
- **Dialogue:** —
- **Sound:** two rifles cracking flat over the water, the reports rolling off the banks
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: in profile at the stern rail, {CHAR_MINA.SHORT}, {CHAR_MINA.WARD_A}, and {CHAR_YOUSSEF.SHORT}, {CHAR_YOUSSEF.WARD_A}, fire their rifles across frame toward the left, back along the wake and away from the camera, small muzzle flashes lighting their tense faces for an instant. Setting: the stern of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, muzzle flashes. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_MINA.NEG}, {CHAR_YOUSSEF.NEG}, tracer fire, visible projectiles, laser beams, rifles pointed toward camera, shell casings flying at the lens
- **Refs:** CHAR_MINA_A_front, CHAR_MINA_A_full, CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_full, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Weapons fire toward frame LEFT (astern), never at the lens (05 §7.5). VFX-ASSIST: add the muzzle flashes in comp if the tool refuses them. Tan helmets, chin straps open (A).

### 06.03.016 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Sparks skip off the shell; it keeps climbing   (5 s)
- **Shot:** Medium shot, anamorphic 75mm, profile · **Move:** slow pan right (continuing)
- **In frame:** UNIT_SHABTI (on the thread)
- **Action:** Sparks skip off the white shell, a streak of grey scorch across one side; the shabti does not flinch and keeps climbing.
- **Dialogue:** —
- **Sound:** bright pings off ceramic, a dry crack; the steady tick of its hands
- **PROMPT:** Medium shot, anamorphic 75mm lens, continuing the same slow pan right at the same speed: bright sparks skip off the shoulder and back of {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_SCORCHED}, as it hangs from the hair-thin glinting thread; it does not flinch and keeps climbing hand over hand toward frame right. Setting: low over {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the sparks and its amber slit. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rope, cable, falling, pieces breaking off, fluid, wires spilling
- **Refs:** UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST, EXTEND:06.03.014
- **Continuity:** Generated from the last clean frame of 06.03.014; 06.03.015 is intercut and hides the join (05 §8). Shabti now SCORCHED (one side smoky grey) until it sinks.

### 06.03.017 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — Tut stands and draws the sky-iron   (5 s)
- **Shot:** Medium low-angle shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); PROP_DAGGER
- **Action:** Tut rises from the engine hatch and draws the dagger from the linen at his waist in one smooth movement, the pale blade low and angled away from camera.
- **Dialogue:** —
- **Sound:** the soft rasp of the blade leaving the linen; the fly's hum just above him
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.STATE_DAGGER_SASH}, rises from the engine hatch, parts the jacket and draws the short pale blade from the linen at his waist in one smooth movement, its point held low and angled away from camera, his eyes on the rail above. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the fly's white pinpoint above catching the blade. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, blade pointed at the camera, sword, long knife, brandishing, stabbing
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_DAGGER_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The dagger leaves the sash here; it goes back into the sash after 06.03.020 and moves to the belt at the dawn change (06.08; file 04 §2). He stands WITHOUT the stick (it lies on the hatch).

### 06.03.018 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — The edge on the thread: a harp note   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TUT's hand; PROP_DAGGER; the thread (UNIT_FLY's filament)
- **Action:** A slender hand with a gold wrist seam lays the dagger's edge on the taut thread and draws it once; the thread parts and whips away into the dark.
- **Dialogue:** —
- **Sound:** a high, pure note, like a harp string, ringing on after the cut
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown hand, {CHAR_TUT.STATE_WRIST_SEAMS}, lays the edge of {PROP_DAGGER.LONG} against a single hair-thin thread glinting taut from a steel rail, and draws it once; the thread parts cleanly and whips away into the dark. Setting: the aft deck of a river launch, black sky behind, in the dead of night. Lighting: a small cold white pinpoint on the rail lighting the blade and the thread. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, grey skin, visible circuitry, glowing skin, rope, cable, thick cord, sparks, blood, blade pointed at the camera, extra fingers
- **Refs:** PROP_DAGGER_REF, CHAR_TUT_HANDS, UNIT_FLY_REF_A
- **Flags:** VFX-ASSIST
- **Continuity:** 05 §10 #36: the cut is an insert with the prop as subject. VFX-ASSIST: the thread and its whip-away are VFX lines; the blade stays clean. CHAR_TUT.NEG is withheld (its "jewellery" term would fight the jewelled gold hilt, 05 §2.3); its hand-relevant terms are typed in.

### 06.03.019 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — The shabti drops; its slit sinks like a lamp   (5 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** UNIT_SHABTI (scorched), falling; the wake
- **Action:** Above the pale wake the shabti drops without a sound, straight down into the black water; its amber slit sinks away under the surface, dimming, until only the wake remains.
- **Dialogue:** —
- **Sound:** no sound as it falls; a small deep plop swallowed by the wake; the harp note dying
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: above the churning pale wake, {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_SCORCHED}, falls silently straight down into the black water, and its small amber slit sinks slowly away beneath the surface, dimming as it goes down, until only the wake and the stars remain. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the sinking amber glow under the water. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, big splash, flailing limbs, explosion, pieces breaking off, rope
- **Refs:** UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The barge now carries TWO shabti on its bow. VFX-ASSIST: the entry splash and the sinking glow can be built from a before/after plate pair.

### 06.03.020 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — The rail goes dark; "The only blade on this river…"   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, low angle · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1); UNIT_FLY on the rail above him (soft)
- **Action:** Above and behind Tut, the fly's pinpoint on the rail flickers and goes out; Tut lowers the blade and speaks.
- **Dialogue:** TUT: "The only blade on this river the machines did not make."
- **Sound:** the fly's hum winding down to nothing; the wake; his voice quiet
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, low angle: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, the short pale blade lowered at his side, stands under a steel rail where, soft behind his head, the white pinpoint of {UNIT_FLY.SHORT}, its cut thread hanging slack, flickers and goes out; he looks down toward camera left and speaks one quiet sentence. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, blade pointed at the camera, sparks, explosion
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_DAGGER_REF, UNIT_FLY_REF_A, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The dead fly stays clamped on the rail for the rest of the sequence (PROP_POLICE_LAUNCH STATE_L3 at dawn: "a downed black drone on its back rail"). Blade held low, out to his right side, away from lens; he re-tucks it after the line.

### 06.03.021 — EXT. POLICE LAUNCH, AFT DECK - CONTINUOUS — More pinpoints lift off the spools; "Lights ahead!"   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, over the stern · **Move:** locked-off
- **In frame:** UNIT_FREIGHT_BARGE (two shabti on the bow); UNIT_FLY ×12 (pinpoints)
- **Action:** Above the barge, more white pinpoints lift off the turning spools: five, eight, twelve. From forward, Fathi's shout.
- **Dialogue:** FATHI (O.S.): "Lights ahead!"
- **Sound:** a swelling high whine chord; the spools creaking; Fathi's shout from the bow
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: far back along the pale wake, {UNIT_FREIGHT_BARGE.SHORT}, two small amber slits on its bow, and above its turning spools cold white pinpoints lift into the air one after another, five, then eight, then twelve, each trailing a hair-thin glint, {UNIT_FLY.SHORT}. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, coloured navigation lights, fireworks, aircraft, searchlight, big drones
- **Refs:** UNIT_FREIGHT_BARGE_REF, UNIT_FLY_REF_B, LOC_NILE_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** VFX-EXTEND: generate 3–4 hero pinpoints; add the rest (to twelve) as light elements in post, locked-off. These twelve are the flies that shadow the fishing grounds (06.04).

---

## Scene 06.04 — EXT. NILE, FISHING GROUNDS - CONTINUOUS

### 06.04.001 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — Kerosene lanterns on black water   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 75mm, from the launch's bow · **Move:** slow push-in (the launch slowing)
- **In frame:** CHAR_NIGHT_FISHERMEN (a dozen boats); PROP_FELUCCA ×3–4; the launch's bow (foreground edge)
- **Action:** Ahead on the black river, a dozen kerosene lanterns float on the water: night fishermen in small wooden boats and feluccas, at their nets, as if nothing has happened to the world.
- **Dialogue:** —
- **Sound:** the diesel throttling back; voices murmuring across the water; nets slapping; oars knocking
- **PROMPT:** Extreme wide establishing shot, anamorphic 75mm lens, slow push-in past the dark edge of a steel bow: ahead on the black river float a dozen warm points of lantern light, {CHAR_NIGHT_FISHERMEN.SHORT}, their small rowing boats scattered among {PROP_FELUCCA.SHORT} with pale furled sails, men hauling and casting nets, unhurried. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, and the fishermen's warm kerosene lanterns doubled in the water. Mood: a pocket of ordinary life, unaware. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NIGHT_FISHERMEN.NEG}, electric lights on the boats, motorboats, cruise ships, readable boat names, drones in frame
- **Refs:** CHAR_NIGHT_FISHERMEN_still, PROP_FELUCCA_REF, PROP_POLICE_LAUNCH_REF, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** "Nobody has told them the world stopped." Screenplay [[verify: lantern night-fishing]]. VFX-EXTEND: generate 4–6 hero boats, extend to a dozen lanterns from the clean plate. Adults only (the fishermen negative excludes children). The flies are behind the launch, out of frame, for now.

### 06.04.002 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — Fathi on the bow: "Lamps out!" and the whistle   (6 s)
- **Shot:** Medium low-angle shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1) on the bow
- **Action:** Fathi, up on the bow, cups his hands and shouts across the water in Egyptian Arabic, then puts two fingers to his lips and gives a long whistle, rising at the end.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Lamps out! Come in close to us!" (then a long whistle, rising at the end)
- **Sound:** his voice carrying flat over the water; the whistle, long and rising; the lanterns' boats going quiet
- **PROMPT:** Medium low-angle shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L1}, stands braced on the bow of a dark launch, cups his hands and shouts across the water in Egyptian Arabic, two short urgent calls, then puts two fingers to his lips and whistles long, his head lifting. Setting: the bow of {PROP_POLICE_LAUNCH.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, warm lantern light from the boats ahead on his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, megaphone, torch, weapon raised
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Lamps out! Come in close to us!" | lower third | line in to out (the whistle is unsubtitled) | seq 06 subtitle file
- **Continuity:** Fathi throttled back and climbed out of the wheelhouse between shots; Tut takes the wheel after this (06.05.001). Lip-sync on the spoken line only; the fingers cover the mouth during the whistle (no sync needed).

### 06.04.003 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — One by one, the lanterns go out   (6 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** CHAR_NIGHT_FISHERMEN; PROP_FELUCCA
- **Action:** Across the fishing grounds, one by one, the lanterns go out, until only starlight and the pale sails remain.
- **Dialogue:** —
- **Sound:** small clinks of lantern glass; a man's low call answering; then the hush of water
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: across the dark fishing grounds, {CHAR_NIGHT_FISHERMEN.SHORT}, and one by one the warm lanterns in the boats are turned down and go out, left to right, until only starlight on the water and the pale shapes of furled sails remain. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the lanterns dying one by one. Mood: quiet complicity. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NIGHT_FISHERMEN.NEG}, all lights switching off at once, electric lights, readable boat names
- **Refs:** CHAR_NIGHT_FISHERMEN_still, PROP_FELUCCA_REF, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** Same boats and layout as 06.04.001. If the tool will not stagger the lanterns, generate lit and dark plates and time the dousing in comp.

### 06.04.004 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — The raft of shadows closes round the steel hull   (6 s)
- **Shot:** Wide high-angle shot, anamorphic 35mm, from the launch's wheelhouse roof · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (below); CHAR_NIGHT_FISHERMEN; PROP_FELUCCA
- **Action:** A dozen dark wooden hulls slide in around the grey steel one, oars and poles working, until the launch is one more shadow in a raft of shadows.
- **Dialogue:** —
- **Sound:** wood knocking softly on steel and tyre fenders; oars dripping; whispered Arabic
- **PROMPT:** Wide high-angle shot, anamorphic 35mm lens, locked-off, from high on a dark launch: small wooden boats and {PROP_FELUCCA.SHORT} glide in from all sides on oars and poles, {CHAR_NIGHT_FISHERMEN.SHORT}, and nest hull to hull around the grey steel deck below until it is one more dark shape in a raft of dark shapes. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: quiet complicity. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NIGHT_FISHERMEN.NEG}, lanterns lit, motor boats, collisions, crowds of faces, drone shot
- **Refs:** CHAR_NIGHT_FISHERMEN_still, PROP_FELUCCA_REF, PROP_POLICE_LAUNCH_REF, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** The raft: the launch at centre, about twelve wooden hulls around it; the old fisherman's felucca at the raft's edge, frame LEFT (north, toward the flies). No faces readable at this height.

### 06.04.005 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — The flies hover; one settles above a felucca   (6 s)
- **Shot:** Wide shot, anamorphic 135mm · **Move:** locked-off
- **In frame:** UNIT_FLY ×12 (pinpoints); one hero fly over PROP_FELUCCA at the raft's edge
- **Action:** The flies slow and hover over the dark raft; one drifts to the raft's edge and settles in the air above a felucca, its white light blinking. Patient.
- **Dialogue:** —
- **Sound:** the whine chord thinning to a single patient hum
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: over a dark cluster of small boats, a scatter of cold white pinpoints slows and hangs in the air; one drifts to the edge of the cluster and settles in the air above {PROP_FELUCCA.SHORT}, {UNIT_FLY.SHORT}, hovering dead still like a hanging insect, its white light blinking slowly. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, coloured navigation lights, searchlight, big drones, lanterns lit
- **Refs:** UNIT_FLY_REF_B, PROP_FELUCCA_REF, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** The screenplay has this fly "blinking" (it overrides file 02's "never blinks"); a slow blink, still cold white. VFX-EXTEND: the other pinpoints are light elements.

### 06.04.006 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — The old fisherman looks up and understands   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, low angle · **Move:** locked-off
- **In frame:** OLD FISHERMAN (CHAR_OLD_FISHERMAN)
- **Action:** At the felucca's tiller, the old fisherman looks up at the white light hanging over his mast, understands, and barks one order in Egyptian Arabic.
- **Dialogue:** OLD FISHERMAN (in Egyptian Arabic; subtitled): "Into the water!"
- **Sound:** the fly's hum close overhead; his voice, hoarse and sure
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, low angle: {CHAR_OLD_FISHERMAN.LONG}, looks slowly up at a small cold white light hanging above his mast, holds it one breath, understands, and barks one short order in Egyptian Arabic to the men behind him. Setting: the stern of {PROP_FELUCCA.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the hard cold white pinpoint above lighting his upturned face. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_OLD_FISHERMAN.NEG}, lantern lit, fear grimace, shouting with wide mouth
- **Refs:** CHAR_OLD_FISHERMAN_front, PROP_FELUCCA_REF, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Into the water!" | lower third | line in to out | seq 06 subtitle file
- **Continuity:** His two crewmen are CHAR_NIGHT_FISHERMEN (file 01 §10b). His lantern is already out; the fly's pinpoint is his key light.

### 06.04.007 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — Over the side; the fly waits for an empty boat   (6 s)
- **Shot:** Wide shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** OLD FISHERMAN, two crewmen (CHAR_NIGHT_FISHERMEN); PROP_FELUCCA; UNIT_FLY above
- **Action:** He and his two crewmen slip over the side into the black water; the fly hangs above the empty boat, waiting.
- **Dialogue:** —
- **Sound:** three splashes; the felucca rocking empty; the hum overhead, unchanged
- **PROMPT:** Wide shot, anamorphic 50mm lens, locked-off: {CHAR_OLD_FISHERMAN.SHORT} and two younger men, {CHAR_NIGHT_FISHERMEN.SHORT}, swing their legs over the gunwale of {PROP_FELUCCA.SHORT} and slip feet first into the black water; the empty boat rocks, and above its mast a small cold white light hangs dead still, waiting. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: quiet complicity. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_OLD_FISHERMAN.NEG}, {CHAR_NIGHT_FISHERMEN.NEG}, diving headfirst, struggling in the water, faces underwater, panic
- **Refs:** CHAR_OLD_FISHERMAN_front, CHAR_NIGHT_FISHERMEN_still, PROP_FELUCCA_REF, UNIT_FLY_REF_A, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** 05 §7.2: the crew are seen clear of the boat BEFORE it burns. "The fly waits until the boat is empty." VFX-ASSIST: splashes.

### 06.04.008 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — The fly drops; fire climbs the sail   (6 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** PROP_FELUCCA (empty); UNIT_FLY
- **Action:** The fly drops onto the empty felucca: a flat thump; fire catches and climbs the great triangular sail.
- **Dialogue:** —
- **Sound:** a flat THUMP; the whoosh of cotton catching; crackle building
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: a small cold white light drops straight down onto the empty deck of {PROP_FELUCCA.LONG}; a flat burst of orange flame, and fire catches and climbs the huge triangular sail from its foot to its yard, no one aboard, the flames doubled in the black water. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the rising orange firelight. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people aboard, figures in the flames, giant fireball, mushroom cloud, debris flying at the camera
- **Refs:** PROP_FELUCCA_REF, UNIT_FLY_REF_A, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The felucca burns EMPTY (05 §7.2). VFX-ASSIST: the fire is a simple element on a before plate if the tool fails. From here the burning felucca is the scene's key light and becomes LOC_NILE STATE_FELUCCA_FIRE in the distance (06.05.007, 06.06.001).

### 06.04.009 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — Three heads come up; a neighbour hauls them in   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** subtle handheld
- **In frame:** OLD FISHERMAN, two crewmen (CHAR_NIGHT_FISHERMEN); a neighbour's rowing boat
- **Action:** The three men surface, blowing, in the firelight; a neighbour leans out of his rowing boat and hauls them aboard one by one.
- **Dialogue:** —
- **Sound:** gasps and spluttered laughter; wood knocking; the fire crackling behind
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: in orange firelight three heads break the black surface, blowing water; {CHAR_OLD_FISHERMAN.SHORT} grips the gunwale of a small wooden rowing boat and a neighbour, {CHAR_NIGHT_FISHERMEN.SHORT}, leans out and hauls him aboard, then reaches for the next. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, warm flickering firelight from the burning sail. Mood: relief, rough and practical. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_OLD_FISHERMAN.NEG}, {CHAR_NIGHT_FISHERMEN.NEG}, faces underwater, drowning struggle, burns, injury, panic close-up
- **Refs:** CHAR_OLD_FISHERMAN_front, CHAR_NIGHT_FISHERMEN_still, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** All three are safe: the old fisherman is now in the neighbour's rowing boat, wet (he answers Fathi from it in 06.05.009).

### 06.04.010 — EXT. NILE, FISHING GROUNDS - CONTINUOUS — The steel hull shines; every fly turns   (6 s)
- **Shot:** Wide high-angle shot, anamorphic 35mm, from the wheelhouse roof · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH; the raft; PROP_FELUCCA (burning, frame left); UNIT_FLY ×12
- **Action:** The fire is a lamp now: among the wooden hulls the launch's grey steel gleams in the firelight; above, every white pinpoint turns toward it.
- **Dialogue:** —
- **Sound:** the fire; the whine chord bending, all at once, into one note
- **PROMPT:** Wide high-angle shot, anamorphic 35mm lens, locked-off: the burning sail at frame left throws orange light across the raft of dark wooden boats, and in the middle of them the grey steel deck and hull of {PROP_POLICE_LAUNCH.SHORT} gleams bright against the dull wood; in the sky above, a scatter of cold white pinpoints swings round together toward it. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, orange firelight. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, explosion, second fire, searchlight, people in panic, drone shot
- **Refs:** PROP_POLICE_LAUNCH_REF, PROP_FELUCCA_REF, UNIT_FLY_REF_B, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-ASSIST, VFX-EXTEND
- **Continuity:** Same high angle as 06.04.004 (match the framing so the change reads). "Among the wooden hulls, the launch's grey steel shines like a coin. Every fly turns." (the simile stays in the screenplay; 05 §5.4).

---

## Scene 06.05 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS

### 06.05.001 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Tut takes the wheel   (5 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** urgent handheld
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut has the wheel before Fathi is off the bow; he spins it hard and swings them out of the raft toward the dark between two islands.
- **Dialogue:** —
- **Sound:** the diesel roaring up; wood scraping off the hull; the wheel's spokes whirring
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld: in the dark wheelhouse, {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.DMG_L1}, grips the worn wooden wheel with both slender hands and spins it hard, leaning into it, eyes fixed forward through the salt-hazed glass, as the floor tilts under him. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, warm orange firelight flickering through the rear windows onto his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing screens, lit instruments, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The stick leans against the chart ledge (he needs both hands). The dagger is back in the sash. The launch swings out of the raft and runs south (frame right) for the gap between two islands.

### 06.05.002 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "It's all sand in there!"   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, from the wheel toward the door · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi scrambles in through the wheelhouse door, sees where they are heading, and shouts.
- **Dialogue:** FATHI: "It's all sand in there!"
- **Sound:** boots on the steel sill; the diesel; wind through the door
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L1}, scrambles in through a narrow steel doorway, catches the frame, stares past camera at the dark water ahead and shouts one quick breathless sentence. Setting: the cramped wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, orange firelight from behind him through the door. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, glowing screens, bright interior light
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Fathi is river-wet to the knees (L1). The screenplay gives this line in English (no language tag).

### 06.05.003 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "Not all."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut doesn't look at the chart; eyes forward, he answers.
- **Dialogue:** TUT: "Not all."
- **Sound:** the diesel; the wheel creaking
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, at the wheel, keeps his eyes forward on the water beyond the glass, never glancing at the chart beside him, and speaks two quiet words. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, orange firelight flickering on one side of his face, starlight on the other. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing screens, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** "He isn't reading the chart. He's reading the stars in the water." The chart stays soft at frame left.

### 06.05.004 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Reading the stars in the water   (6 s)
- **Shot:** Point-of-view shot, anamorphic 40mm, over the bow · **Move:** vehicle-mounted
- **In frame:** the water ahead; two islands; the bow
- **Action:** Ahead, between two dark islands, the reflected stars lie whole on the deep channel, but shiver and break over the shallows either side.
- **Dialogue:** —
- **Sound:** the bow wave; reeds hissing on either side
- **PROMPT:** Point-of-view shot, anamorphic 40mm lens, vehicle-mounted, over the dark steel bow of a launch: ahead lies a narrow gap between two black reedy islands; down its middle the reflected stars lie whole and still on deep water, while on either side, over the shallows, the reflections tremble and break apart into restless flecks. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: hushed concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lanterns, searchlight, moon reflection, people, buoys, channel markers
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Heading south (upriver). VFX-ASSIST: if the "shiver vs whole" contrast does not read, comp the star reflections with a ripple displacement over the shallows only.

### 06.05.005 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "Where the stars shiver, the bottom is near."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut eases the wheel a fraction, eyes on the reflections, and explains, calm.
- **Dialogue:** TUT: "Where the stars shiver, the bottom is near. Keep them whole."
- **Sound:** the diesel; reeds brushing the hull
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, eases the wheel a fraction with one hand, eyes lowered to the water just ahead, and speaks two short calm sentences, as if teaching. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face, a dying orange flicker behind. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, glowing screens, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Eyeline down and just off lens right (the water ahead).

### 06.05.006 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "The river tells you where. The sky tells you when."   (6 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** A beat; then, half to himself, the rule.
- **Dialogue:** TUT: "The river tells you where. The sky tells you when."
- **Sound:** the diesel dropping under the line; water
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, a beat of stillness, then, half to himself and without looking away from the water, he speaks two short balanced sentences, the faintest smile at the corner of his mouth. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, torch light
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** The film's navigation rule (bible §7 Seq 6.1). Push under 10% of frame.

### 06.05.007 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — The lanterns relit at once; the flies split   (6 s)
- **Shot:** Wide shot, anamorphic 75mm, astern · **Move:** locked-off
- **In frame:** CHAR_NIGHT_FISHERMEN (boats scattering); PROP_FELUCCA (burning); UNIT_FLY ×12
- **Action:** Astern, the fishermen relight every lantern at once and scatter in a dozen directions; the flies split up to chase them.
- **Dialogue:** —
- **Sound:** far-off shouts and laughter; oars; the whine chord breaking into many notes
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off, looking back astern: around the small burning sailboat, a dozen warm lanterns flare up at once in the scattered boats, {CHAR_NIGHT_FISHERMEN.SHORT}, and the boats pull away in every direction; above them the cold white pinpoints break apart and dart off after the lights. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_FISHING_GROUNDS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, orange firelight and warm lanterns doubled in the water. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_NIGHT_FISHERMEN.NEG}, explosions, electric lights, searchlight, readable boat names
- **Refs:** CHAR_NIGHT_FISHERMEN_still, PROP_FELUCCA_REF, UNIT_FLY_REF_B, LOC_NILE/FISHING_GROUNDS_NIGHT
- **Flags:** VFX-EXTEND, VFX-ASSIST
- **Continuity:** Seen from the launch as it runs south: the fishing grounds recede to frame centre-left. VFX-EXTEND lanterns and pinpoints; VFX-ASSIST the fire.

### 06.05.008 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "The king owes you a boat!"   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, in the wheelhouse door · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi leans out of the wheelhouse door and yells back across the water, grinning.
- **Dialogue:** FATHI (yelling astern; in Egyptian Arabic; subtitled): "The king owes you a boat!"
- **Sound:** wind; the diesel; his yell flattening over the water
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, leans half out of a narrow steel doorway, one hand on the frame, and yells one sentence back across the water in Egyptian Arabic, grinning into the wind. Setting: the wheelhouse door of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, distant orange firelight on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, bright interior light, weapon raised
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "The king owes you a boat!" | lower third | line in to out | seq 06 subtitle file
- **Continuity:** He faces astern (frame left of lens), the fishing grounds behind camera.

### 06.05.009 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "Which king?" "Ours!"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** A thin voice floats back across the water; Fathi's grin widens and he yells one word back.
- **Dialogue:** OLD FISHERMAN (O.S.; in Egyptian Arabic; subtitled): "Which king?" · FATHI (in Egyptian Arabic; subtitled): "Ours!"
- **Sound:** the old man's voice small and far off; Fathi's one-word yell; a short laugh from inside the wheelhouse
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, leaning in the doorway, listens to a faint voice from far across the water, his grin widening, then yells one word back in Egyptian Arabic, proud and laughing. Setting: the wheelhouse door of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, distant orange firelight on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, bright interior light
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitles | "Which king?" then "Ours!" | lower third | each line in to out | seq 06 subtitle file
- **Continuity:** The old fisherman answers from the neighbour's rowing boat (06.04.009); O.S. only, no picture sync.

---

## Scene 06.06 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS

### 06.06.001 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — Into the reeds; the felucca burns far behind   (6 s)
- **Shot:** Wide shot, anamorphic 40mm, from the aft deck looking back · **Move:** vehicle-mounted
- **In frame:** PROP_POLICE_LAUNCH (wheelhouse roof, aft deck); the channel; the burning felucca (far)
- **Action:** Reeds close in on both sides; tamarisk branches drag across the wheelhouse roof; far behind, the burning felucca is a small orange flower, doubled in the water.
- **Dialogue:** —
- **Sound:** reeds hissing along the hull; branches scraping steel; the diesel low
- **PROMPT:** Wide shot, anamorphic 40mm lens, vehicle-mounted, from the aft deck looking back: dense reeds slide past close on both sides and trailing tamarisk branches drag across the dark wheelhouse roof of {PROP_POLICE_LAUNCH.SHORT}; far behind, down the narrowing channel, {LOC_NILE.STATE_FELUCCA_FIRE}. Setting: {LOC_NILE.LONG}, a narrow reedy channel between two islands, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}, the tiny distant fire. Mood: hushed concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people in frame, lanterns nearby, searchlight, moon in frame
- **Refs:** PROP_POLICE_LAUNCH_REF, PROP_FELUCCA_REF, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** The island channel: reeds and tamarisk islands both sides; heading south. The fire is a distant VFX element (file 03 STATE_FELUCCA_FIRE).

### 06.06.002 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — The barge noses in after them   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, astern · **Move:** locked-off
- **In frame:** UNIT_FREIGHT_BARGE; UNIT_SHABTI ×2 on its bow
- **Action:** The barge's blunt bow noses into the channel after them, unhurried, reeds folding under it; two amber slits on its bow.
- **Dialogue:** —
- **Sound:** its diesel throb; reeds crushing under steel
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: at the mouth of a narrow reedy channel, {UNIT_FREIGHT_BARGE.SHORT} noses in after them, unhurried, its blunt bow folding the reeds down, two {UNIT_SHABTI.SHORT} standing motionless on it, two small amber slits the only lights aboard. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, crew, lit wheelhouse, navigation lights, searchlight, third robot on the bow
- **Refs:** UNIT_FREIGHT_BARGE_REF, UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Two shabti on the bow since 06.03.019. The flies are away chasing lanterns (they return in 06.06.009).

### 06.06.003 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — Seven stars standing on end   (5 s)
- **Shot:** Wide shot, anamorphic 40mm, low, up at the northern sky · **Move:** slow tilt up
- **In frame:** the northern sky; tamarisk silhouettes at frame bottom
- **Action:** Tilting up past black tamarisk silhouettes: low in the north-east, seven bright stars standing on end, a handle and a blade. Tut names them.
- **Dialogue:** TUT (O.S.): "Meskhetiu. The Foreleg."
- **Sound:** reeds; the diesel; his voice close, quiet
- **PROMPT:** Wide shot, anamorphic 40mm lens, slow tilt up from black tamarisk branches: a dense star field over a black horizon, and low in the north-east seven bright stars standing on end in the shape of a long handle and a blade, clearer than the rest. Setting: the sky above {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, moon, planets, constellation lines, drawn shapes, aircraft, meteors, drones
- **Refs:** LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** star element | the Plough of the Great Bear "standing on end" in the north-east before dawn, matched to the 5 Nov 2033 Middle Egypt sky (about 04:30), brightened a touch over the field | upper frame, tracked to the tilt | whole shot | star-field plate from the ephemeris (screenplay [[verify]])
- **Continuity:** Looking back past the barge to the NORTH-EAST (astern and to the east). No constellation lines are ever drawn.

### 06.06.004 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — Nour: "the soul of Typhon"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1), in the wheelhouse door
- **Action:** In the wheelhouse door behind Tut, Nour looks up at the same stars and answers with the Greek name.
- **Dialogue:** NOUR: "The Great Bear. Plutarch calls it 'the soul of Typhon.'"
- **Sound:** reeds; the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, leaning in a narrow steel doorway, looks up past camera at the northern sky and speaks two short sentences, a scholar's precision under the fear, the silver pendant closed in one fist. Setting: the wheelhouse door of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on her upturned face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, torch light, glowing screen
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Pendant CLUTCHED in her right fist (not yet re-clasped). Wheelhouse: Tut at the wheel, Nour in the aft doorway, Adaeze behind her.

### 06.06.005 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — "An adze of stars … Meskha."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1) at the wheel, looking back
- **Action:** At the wheel, Tut looks back over his shoulder at the constellation and corrects her gently: Set, the adze, the rite that opened him.
- **Dialogue:** TUT: "Of Set. An adze of stars. The adze they opened me with bore its name: Meskha."
- **Sound:** reeds; the diesel; his voice very even
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, one hand on the wheel, looks back over his shoulder at the northern sky and speaks three short sentences, very even, as if reporting something done to someone else. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, torch light
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Transliteration "Meskha" / "Meskhetiu" is spoken only, never on screen (05 §9.5). Eyeline back over his LEFT shoulder (astern).

### 06.06.006 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — "I am navigating by the thing that opened my mouth."   (6 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Keeping the constellation over the stern, Tut turns forward again and says it plainly.
- **Dialogue:** TUT: "I am navigating by the thing that opened my mouth."
- **Sound:** a held beat of reeds and water
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, turns his face slowly forward from a last look back over his shoulder, and, eyes on the dark water ahead, speaks one quiet sentence, his jaw tight on the last word. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** "(keeping it over the stern)": he steers so the Bear stays astern.

### 06.06.007 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — Over the bar with a hand's breadth under the keel   (5 s)
- **Shot:** Wide shot, anamorphic 24mm, at the waterline · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (hull gliding past)
- **Action:** At water level: the grey hull glides past over a pale sandbar just under the calm surface, stars lying whole on the water; it clears without touching.
- **Dialogue:** —
- **Sound:** a soft whisper of water squeezed between keel and sand; no scrape
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, the lens just above the surface: the grey steel hull of {PROP_POLICE_LAUNCH.SHORT} glides slowly past very close over a pale sandbar lying just beneath calm water that holds the stars whole, the keel clearing it by a hand's breadth, the water barely stirring. Setting: {LOC_NILE.SHORT}, a reedy channel between islands, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: a held breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, splashing, grounding, mud clouds, people, lanterns
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** "He eases the wheel toward water where the stars lie calm." VFX-ASSIST: the sandbar under the surface may be a comp element.

### 06.06.008 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — The barge doesn't: steel groans on sand   (6 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** locked-off
- **In frame:** UNIT_FREIGHT_BARGE; UNIT_SHABTI ×2
- **Action:** The barge hits the bar: a long groan of steel on sand; it slews sideways and stops dead in the reeds; its two shabti sway; neither falls.
- **Dialogue:** —
- **Sound:** a long GROAN of steel on sand; reeds snapping; the barge's diesel labouring, then idling
- **PROMPT:** Wide shot, anamorphic 75mm lens, locked-off: {UNIT_FREIGHT_BARGE.LONG}, drives onto a hidden sandbar with a long shudder, slews slowly sideways across the channel and stops dead in the reeds; on its bow two {UNIT_SHABTI.SHORT} sway with the jolt, and both stay standing. Setting: {LOC_NILE.SHORT}, a narrow reedy channel between islands, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, two small amber slits. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, explosion, capsizing, robots falling, crew, lit wheelhouse
- **Refs:** UNIT_FREIGHT_BARGE_REF, UNIT_SHABTI_REF_A, LOC_NILE_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** From here the barge is STATE_AGROUND. VFX-ASSIST: water surge and reeds; before/after plates if the slew fails.

### 06.06.009 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — A small, wrong constellation   (6 s)
- **Shot:** Wide shot, anamorphic 135mm, astern · **Move:** locked-off
- **In frame:** UNIT_FREIGHT_BARGE (aground); UNIT_FLY ×12
- **Action:** The flies drift back from the dark and hang over the stranded hull, a small, wrong constellation, dead still.
- **Dialogue:** —
- **Sound:** the whine chord returning, settling to one low hum
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: far back down the channel, {UNIT_FREIGHT_BARGE.SHORT}, {UNIT_FREIGHT_BARGE.STATE_AGROUND}; one by one cold white pinpoints drift in out of the dark and stop in the air above it, hanging dead still in a small, uneven cluster lower than any star. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, coloured navigation lights, searchlight, drones attacking
- **Refs:** UNIT_FREIGHT_BARGE_REF, UNIT_FLY_REF_B, LOC_NILE_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** Recalled flies (file 02 §6). The barge stays aground behind them; it is not seen again.

### 06.06.010 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — His hand goes to his nape: "They are being called home."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** At the wheel, Tut's free hand goes to the back of his neck, as if listening through it; he reports what he hears.
- **Dialogue:** TUT: "They are being called home. It says it has what it needs."
- **Sound:** under his line, at the edge of hearing, a faint whispering, like a temple at night
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, at the wheel, slowly raises his free hand to the back of his neck and holds it there, head tilted a little as if listening to something inside it, and speaks two quiet sentences, eyes unfocused. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, earpiece, headphones
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** His hand covers the nape PORT (still in; it is cut out in 06.07). The whispering sound bed starts here and runs until the click (06.07.011).

### 06.06.011 — EXT. NILE, ISLAND CHANNEL - CONTINUOUS — They all look at the hand on his neck   (5 s)
- **Shot:** Two-shot, anamorphic 50mm, in the wheelhouse door · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1), ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Nour and Adaeze, in the doorway, both look at the hand on the back of his neck; Adaeze's eyes narrow.
- **Dialogue:** —
- **Sound:** reeds; the faint whispering
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: in a narrow steel doorway, {CHAR_NOUR.SHORT} and, just behind her shoulder, {CHAR_ADAEZE.SHORT}, both look off frame right at the back of someone's neck; the nearer woman's breath catches; the taller one's eyes narrow slowly as a thought lands. Setting: the wheelhouse door of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, faint cool starlight lifting both faces. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, torch light, more than two faces
- **Refs:** CHAR_NOUR_B_full, CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_NILE_NIGHT
- **Flags:** —
- **Continuity:** Adaeze's realisation sets up 06.07.003 ("it found us in the dark").

---

## Scene 06.07 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN

### 06.07.001 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — Moored under tamarisks, one white headlamp   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, from the island bank · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (moored); small figures on the aft deck around one headlamp beam
- **Action:** The launch lies moored under trailing tamarisks, engine off; the first grey in the east; on the aft deck a single white headlamp beam points down at a seated figure.
- **Dialogue:** —
- **Sound:** no engine; water lapping the hull; a frog; faint whispering under everything
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, from the reeds of the bank: {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L2}, lies still with its engine off, a few small figures gathered close around one seated figure under the beam. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_ISLAND}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, the sun still well below the horizon, only a first grey in the east, the deck in deep blue shadow. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, sun disc, sunrise colours on the deck, drones in the sky, lanterns, exhaust smoke
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE/ISLAND_DAWN
- **Flags:** COMP
- **Comp:** SUPER | "05:10" | lower left, small, per 05 §13.7 | from 1 s to 5 s | seq 06 SUPER file
- **Continuity:** 5 Nov, 05:10; sunrise about 06:10. The flies are gone (called home). Tut is still in A1 (the dawn change is after this scene). The phones went over the side earlier (off screen): "after the phones".

### 06.07.002 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — The white circle on the gold-edged port   (5 s)
- **Shot:** Close-up, anamorphic 75mm, from directly behind Tut · **Move:** locked-off
- **In frame:** TUT (back of the head and neck, CHAR_TUT_NAPE_PORT)
- **Action:** A headlamp's white circle rests on the small gold-edged port at the nape of his bowed neck; he sits on an upturned bucket, head down, like a man at the barber's.
- **Dialogue:** —
- **Sound:** the whispering, faint and always there; water
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, from directly behind: a young man's bowed shaved head and neck above the collar of a charcoal field jacket, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, lit by a hard white circle of headlamp light; he sits very still on an upturned bucket, head down, hands in his lap. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, the deck in deep blue shadow, one hard white headlamp beam. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, wound, incision, cables, hood up, face visible
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A1_full, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Nape PORT (last shot with it in). Hood down. The headlamp is Adaeze's own (white; file 01 Adaeze B, from 6.2). The port is seen only from behind (file 01).

### 06.07.003 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — Adaeze: "it found us in the dark"   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1) with her headlamp
- **Action:** Adaeze, headlamp on her forehead aimed down at Tut's nape, lays out the logic, then looks up at Tomas.
- **Dialogue:** ADAEZE: "No phones, no lights, no radio, and it found us in the dark. Tomas. What does that port carry?"
- **Sound:** water; the whispering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L1}, a small headlamp strapped round her forehead aimed down out of frame, speaks two sentences low and even, then lifts her eyes to someone tall off frame right and asks one short question. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, the spill of her white headlamp beam bouncing up onto her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp beam into the lens, glowing screen
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Adaeze's headlamp appears for the first time (white). Kneeling behind Tut's right shoulder; Tomas stands frame right of her, Nour at Tut's left.

### 06.07.004 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — Tomas: "And audio."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, slightly low · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B1)
- **Action:** Tomas answers like a clinician, stops, and admits the rest.
- **Dialogue:** TOMAS: "Regulation. Core telemetry." (he stops) "And audio. For the writing-in. It should have closed when the teaching ended."
- **Sound:** water; the whispering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, slightly low: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, looking down off frame left, answers in a flat clinical voice, stops mid-thought, swallows, then speaks two more short sentences more quietly, ashamed. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, white headlamp spill from below. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, lab coat, headlamp on his head
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Tomas has NO headlamp of his own (file 01 Tomas B). Sleeves rolled above the elbows.

### 06.07.005 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — "You weren't asking about the room."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze turns back to Tut's bowed head and gives him his own first words.
- **Dialogue:** ADAEZE: "'Is it listening?' The first thing you ever said. You weren't asking about the room."
- **Sound:** water; the whispering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, headlamp on her forehead, turns back to look down at the bowed head in front of her and speaks three short sentences gently, the first one quoting someone. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, white headlamp spill on her face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp beam into the lens
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Pays off 1.5 ("Is it listening?"). Eyeline down, frame left.

### 06.07.006 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — "A guest in my head. It never knocked."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, low · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut, head still bowed, lifts his eyes slightly and answers.
- **Dialogue:** TUT: "I felt it the moment I woke. A guest in my head. Very polite. It never knocked."
- **Sound:** water; the whispering a shade louder under his line
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, low: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, head bowed on an upturned bucket, lifts his eyes a little without raising his head and speaks four short sentences quietly, with a dry edge on the last. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, a white headlamp beam glowing on the back of his neck, soft spill on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** The camera is low enough to see his face under the bowed head. The port is behind, unseen.

### 06.07.007 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — Tomas: the trade   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, slightly low · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_B1)
- **Action:** Tomas lays out the cost, plainly.
- **Dialogue:** TOMAS: "Cut it, and it's deaf. So are you, to the units. And your core runs on its regulation."
- **Sound:** water; the whispering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, slightly low: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, crouches to eye level with someone off frame left and speaks three plain sentences slowly, making himself say each one. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, white headlamp spill. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, lab coat, headlamp on his head
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** He crouches here and stays crouched for the cut (06.07.010).

### 06.07.008 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — "The foot first. Then the hands."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, slightly low · **Move:** locked-off (continuing)
- **In frame:** TOMAS (CHAR_TOMAS_B1)
- **Action:** Tomas finishes: without it the lattice drifts; the foot first, then the hands.
- **Dialogue:** TOMAS: "Without it, the lattice drifts. The foot first. Then the hands."
- **Sound:** water; the whispering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.SHORT}, crouched, glances down once toward someone's feet and then hands off frame left and speaks three short sentences, quieter each time. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, white headlamp spill. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, headlamp on his head
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_B_work, LOC_NILE/ISLAND_DAWN
- **Flags:** EXTEND:06.07.007
- **Continuity:** Generated from the last clean frame of 06.07.007 (the line runs past 8 s; 05 §8.3).

### 06.07.009 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — "How long?" … "Cut it."   (8 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** Tut asks how long; hears "days"; answers the only true thing; then, a beat, gives the order.
- **Dialogue:** TUT: "How long?" · TOMAS (O.S.): "Days. I don't know how many." · TUT: "Nobody knows how many." (beat) "Cut it."
- **Sound:** water; the whispering; a long pause before "Cut it."
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, head bowed, asks two words, listens to an answer from off frame with a faint wry breath, speaks one short sentence, then after a still beat lifts his chin a fraction and speaks two words, final. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, soft white headlamp spill on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Tomas's line is O.S. (no sync on him). If the recording exceeds 8 s, cut into Tomas at "Days" (use a trimmed 06.07.008 alt) and back.

### 06.07.010 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — Nour takes his hand; Tomas opens the multitool   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1), TUT (CHAR_TUT_A1_1, head bowed), TOMAS (CHAR_TOMAS_B1, behind); PROP_MULTITOOL
- **Action:** Nour kneels in front of Tut and takes his hand; behind him, Tomas opens Fathi's battered multitool in the headlamp beam.
- **Dialogue:** —
- **Sound:** the multitool's steel clicking open; the whispering, faint and always there, like a temple at night
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.SHORT} kneels on the deck in front of {CHAR_TUT.SHORT}, who sits bowed on an upturned bucket, and takes his right hand in both of hers; behind him {CHAR_TOMAS.SHORT} unfolds {PROP_MULTITOOL.SHORT} under a hard white headlamp beam. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, one hard white headlamp beam. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_NOUR.NEG}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, scalpel, surgical instruments, gloves, blood, more than two clear faces
- **Refs:** CHAR_NOUR_B_full, CHAR_TUT_A1_full, CHAR_TOMAS_B_work, PROP_MULTITOOL_REF, LOC_NILE/ISLAND_DAWN
- **Flags:** —
- **Continuity:** Nour holds his RIGHT hand (the tremor hand, 06.07.016). Adaeze stands behind Tomas holding the light (her beam in frame, her face out). The multitool is Fathi's (file 04 §22.10).

### 06.07.011 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — The fine tip under the gold rim; a click   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TOMAS's hands; PROP_MULTITOOL; the gold rim at Tut's nape (soft)
- **Action:** The fine tip slides under the gold rim at the nape; a careful pressure; a CLICK.
- **Dialogue:** —
- **Sound:** the whispering; then a small, clean CLICK
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_MULTITOOL.LONG}, its fine needle-nose tip easing with great care under the thin gold rim of a small round fitting at the base of a shaved head, the skin soft and out of focus, then one small steady twist. Setting: the aft deck of a river launch, just before dawn. Lighting: the hard white headlamp beam, deep blue shadow beyond. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, wound, incision, blood, scalpel, open skin, cables, gore, surgical gloves
- **Refs:** PROP_MULTITOOL_REF, CHAR_TUT_NAPE_PORT, CHAR_TOMAS_B_work
- **Flags:** —
- **Continuity:** Hands and tool only; the skin stays soft; never an open wound (05 §7.2 "Tut's nape port cut"; file 01 Nape).

### 06.07.012 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — A sliver of gold and glass on a hair-fine lead   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** slow pull-back
- **In frame:** PROP_PORT_SLIVER in TOMAS's fingers
- **Action:** Tomas draws out a fingernail-sized sliver of gold and glass trailing a hair-fine lead; it comes clean.
- **Dialogue:** —
- **Sound:** the whispering STOPS dead. Water against the hull. A frog.
- **PROMPT:** Insert, 100mm macro lens, slow pull-back: {PROP_PORT_SLIVER.LONG}, drawn slowly up and away until the fine lead slips free and hangs glinting in the beam. Setting: above the aft deck of a river launch, just before dawn. Lighting: the hard white headlamp beam, black water beyond. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, blood, wound, skin in focus, tweezers, surgical tools, cables
- **Refs:** PROP_PORT_SLIVER_REF, CHAR_TOMAS_B_work
- **Flags:** —
- **Continuity:** From here Tut's nape is the SCAR (file 01; stitched in Seq 6–7). The sound cut to silence is the scene's hinge.

### 06.07.013 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — "Now you are the only one who can hear me."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1)
- **Action:** In the new silence Tut lifts his head, finds Nour's eyes and speaks softly in Late Egyptian.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "Now you are the only one who can hear me."
- **Sound:** silence: water, a frog; his voice very close
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A1}, in sudden stillness, slowly lifts his head as if listening to an absence, finds the eyes of someone kneeling just off frame left, and speaking softly in an ancient language, says one short sentence. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, soft headlamp spill from behind. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A1_full, LOC_NILE/ISLAND_DAWN
- **Flags:** COMP
- **Comp:** subtitle | "Now you are the only one who can hear me." | lower third | line in to out | seq 06 subtitle file (Late Egyptian recorded with the consultant before generation, 05 §9.5)
- **Continuity:** Nour kneels at frame left holding his right hand. From here he is deaf to the units (he cannot hear the flies in 06.10.002).

### 06.07.014 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — The pulse stutters   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TUT's chest under the jacket (CHAR_TUT_A1_1)
- **Action:** Under the half-open jacket, the pale glow at the centre of his chest stutters, skips, and resumes.
- **Dialogue:** —
- **Sound:** a faint, uneven electrical flutter under the silence
- **PROMPT:** Insert, 100mm macro lens, locked-off: between the open edges of a charcoal field jacket, white linen over a slight chest, {CHAR_TUT.STATE_G0F}, faltering, dipping out for an instant, then returning. Setting: the aft deck of a river launch, just before dawn. Lighting: deep blue shadow, a little white headlamp spill. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, bare chest, visible circuitry, lattice under the skin, screen, holograms, bright light beam
- **Refs:** CHAR_TUT_A1_full
- **Flags:** COMP
- **Comp:** chest glow | G0 → G0f: the cold pale green (#A6F2C2 core) drops 10–20% and stutters: two 0.3 s dropouts and one skip, then resumes (file 01 glow table) | centre of the chest through the linen, tracked | whole shot | G0f light element (file 01)
- **Continuity:** From here the glow is G0f (irregular stutters) until 8.5.

### 06.07.015 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — The black foot jerks and locks   (4 s)
- **Shot:** Insert, 100mm macro, at deck level · **Move:** locked-off
- **In frame:** TUT's feet (CHAR_TUT_FOOT)
- **Action:** His black ceramic foot jerks once and locks, toe raised off the deck.
- **Dialogue:** —
- **Sound:** a single dry ceramic click, then nothing
- **PROMPT:** Insert, 100mm macro lens, locked-off, at deck level beside an upturned bucket, under the hem of a white linen gown: {CHAR_TUT.STATE_FOOT}; the black foot jerks once and locks, its rounded tip raised stiffly off the steel deck, and stays there. Setting: the aft deck of a river launch, just before dawn. Lighting: deep blue shadow, white headlamp spill. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, robot foot with joints, LEDs, toes, sandal on the left foot, sparks
- **Refs:** CHAR_TUT_FOOT, CHAR_TUT_A1_full
- **Flags:** —
- **Continuity:** From 6.2 the foot stalls (file 01 STATE_FOOT_STALL). Left = ceramic, right = sandal.

### 06.07.016 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — His hand trembles in hers; the stopwatch starts   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TUT's right hand in NOUR's hands; TOMAS's hand with PROP_STOPWATCH
- **Action:** His right hand, in Nour's, begins to tremble; beside it a large pale hand thumbs a cheap plastic stopwatch.
- **Dialogue:** —
- **Sound:** a tiny plastic beep
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown right hand, {CHAR_TUT.STATE_WRIST_SEAMS}, held between a woman's two hands, begins to tremble with {CHAR_TUT.STATE_TREMOR}; beside it {PROP_STOPWATCH.SHORT}, {PROP_STOPWATCH.STATE_HELD}, and a large thumb presses its top button once. Setting: the aft deck of a river launch, just before dawn. Lighting: soft white headlamp spill, deep blue shadow. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable digits, brand name, extra fingers, fused fingers, wound
- **Refs:** CHAR_TUT_HANDS, CHAR_NOUR_B_full, PROP_STOPWATCH_REF, CHAR_TOMAS_B_work
- **Flags:** COMP
- **Comp:** stopwatch display | 00:00 starting to count (00:00.0 → 00:03.5) | on the small display, tracked | from the beep to the end | LCD element built in comp
- **Continuity:** Tremor in the RIGHT hand from here on (file 01). Tomas keeps the stopwatch (PROP_STOPWATCH, 6.2 → 7.1).

### 06.07.017 — EXT. POLICE LAUNCH, AFT DECK - PRE-DAWN — The sliver goes over the side, after the phones   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, at the gunwale · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A1_1, from the side); PROP_PORT_SLIVER
- **Action:** Tut takes the sliver from Tomas's fingers, leans to the gunwale, and lets it drop into the black water.
- **Dialogue:** —
- **Sound:** the tiniest plip; then only water
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, from behind his right shoulder at the gunwale: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A1}, {CHAR_TUT.STATE_SCAR}, head bowed, leans over the side and opens two fingers, {PROP_PORT_SLIVER.SHORT}, {PROP_PORT_SLIVER.STATE_DROPPED}, and watches it go, his face turned away. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, under tamarisk branches, just before dawn. Lighting: {LOC_NILE.LIGHT_DAWN}, deep blue shadow, a little white headlamp spill. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, big splash, throwing motion, blood
- **Refs:** CHAR_TUT_NAPE_SCAR, CHAR_TUT_A0_34, CHAR_TUT_A1_full, PROP_PORT_SLIVER_REF, LOC_NILE/ISLAND_DAWN
- **Flags:** VFX-ASSIST
- **Continuity:** "Tut drops the gold sliver over the side, after the phones." Nape SCAR from here, first seen in this shot (STATE_SCAR; closed with three fine stitches through Seq 6–7, from behind only; QA: the framing moved from profile to behind the shoulder so the scar reads). VFX-ASSIST: the tiny splash.

---

## Scene 06.08 — EXT. NILE - DAWN

### 06.08.001 — EXT. NILE - DAWN — Sunrise turns the river gold; not one car on the road   (6 s)
- **Shot:** Extreme wide establishing shot, anamorphic 75mm, from the west bank · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (small, mid-river); the empty river road (foreground)
- **Action:** The sun clears the east bank and turns the wide river gold; the launch chugs south (frame right) mid-river; along the near bank a straight road runs empty, not one car.
- **Dialogue:** —
- **Sound:** birdsong from the palms; the diesel far off; no traffic at all
- **PROMPT:** Extreme wide establishing shot, anamorphic 75mm lens, locked-off: the sun just clearing the far bank turns the wide river to gold; small in the middle, {PROP_POLICE_LAUNCH.SHORT} chugs steadily toward frame right; in the foreground a straight paved road runs along the near bank between palms, completely empty, not one vehicle on it. Setting: {LOC_NILE.LONG}, at first light. Lighting: {LOC_NILE.LIGHT_DAWN}, the low new sun laying a gold path across the water. Mood: fragile peace. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, cars on the road, trucks, pedestrians, cruise ships, drones in the sky, readable road signs, smoke
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** 5 Nov, just after 06:10 sunrise. Camera on the west bank facing east: south = frame right. The launch is L3 from here (the dead fly on the back rail, 06.03.020).

### 06.08.002 — EXT. NILE - DAWN — Master: the questions begin   (6 s)
- **Shot:** Wide shot (master), anamorphic 32mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1) on the engine hatch; RAMI (CHAR_RAMI_B1) cross-legged on the deck facing him; NOUR (CHAR_NOUR_B1, soft, at the gunwale); PROP_POLICE_LAUNCH (L3)
- **Action:** In low gold light Tut, now in tunic and cargo trousers under the jacket, sits on the engine hatch; Rami sits cross-legged before him, the notebook on his knee, pen in his good hand; Nour leans at the gunwale.
- **Dialogue:** —
- **Sound:** the diesel steady; water; a page turning
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: on the open aft deck in low gold morning light, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, {CHAR_TUT.STATE_DAGGER_BELT}, {CHAR_TUT.STATE_FOOT}, sits on the engine hatch, {PROP_EBONY_STICK.SHORT} propped beside him; cross-legged on the deck before him {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_B}, opens a notebook on his knee, pen in his right hand; {CHAR_NOUR.SHORT} leans soft at the gunwale behind. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_L3}, on {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun raking across the deck. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_RAMI.NEG}, {CHAR_NOUR.NEG}, gown, splint on the right hand, more than three clear faces, night
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, CHAR_RAMI_A_front, CHAR_RAMI_B_full, CHAR_NOUR_B_full, CHAR_TUT_FOOT, PROP_EBONY_STICK_REF, PROP_RAMI_NOTEBOOK_REF, PROP_POLICE_LAUNCH_REF, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** DAWN CHANGE (file 01): Tut is now T-B1: the charcoal jacket over the gown cut down to a hip-length tunic and Karim's spare cargo trousers rolled at the ankle; the dagger in its gold sheath on a webbing belt at the right hip (production choice, INDEX open item 3); nape SCAR (stitched); G0f under the jacket; the ebony stick beside him; RIGHT-hand tremor; foot stall. Rami: splint on the LEFT hand, notebook river-damp. Nour has re-clasped the pendant (STATE_STANDARD). Dead fly on the back rail above (L3). Geography: camera forward looking aft; Tut frame right facing left, Rami frame left facing right.

### 06.08.003 — EXT. NILE - DAWN — "100 QUESTIONS FOR TUTANKHAMUN"   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_RAMI_NOTEBOOK in RAMI's hands (splinted left hand visible)
- **Action:** Rami's hands open the battered mustard-yellow notebook; the handwritten label on the cover catches the sun; he flicks to a dog-eared page.
- **Dialogue:** —
- **Sound:** the elastic snapping off; pages riffling
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_DAMP}, rests on a knee in black jeans; a right hand slips off the elastic band while a left hand with two fingers taped to a wooden splint holds it steady, and flicks it open to a dog-eared page. Setting: the aft deck of a river launch, in the morning. Lighting: low gold sunlight across the cover and the pages. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, legible handwriting, printed title, logo, extra fingers
- **Refs:** PROP_RAMI_NOTEBOOK_REF, CHAR_RAMI_B_full
- **Flags:** COMP
- **Comp:** notebook label | "100 QUESTIONS FOR TUTANKHAMUN" in Rami's quick handwriting on the white cover label; the open page shows numbered questions in the same hand (7, 11, 19 circled) | tracked on the label and page | whole shot | handwriting asset (file 04 §19.2: title and pages are COMP)
- **Continuity:** Notebook STATE_DAMP (Seq 6 on). It stays Rami's until 7.4.

### 06.08.004 — EXT. NILE - DAWN — "Seven. Orion's belt and the star shafts."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1)
- **Action:** Rami reads the first question off the page like a quizmaster.
- **Dialogue:** RAMI: "Seven. Orion's belt and the star shafts."
- **Sound:** the diesel; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L1}, cross-legged, reads one line off a notebook in his lap and looks up off frame right with bright eager eyes, speaking one short sentence like a quizmaster. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, night
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Rami's eyeline frame RIGHT to Tut throughout the Q&A.

### 06.08.005 — EXT. NILE - DAWN — The pyramids and the belt: "One of your astronomers did the sum."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut taps his temple and answers, dry and exact.
- **Dialogue:** TUT: (taps his temple) "The pyramids lie thirty-eight degrees from north; the belt, in their chosen year, fifty. One of your astronomers did the sum."
- **Sound:** the diesel; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G0F}, taps one finger to his temple and answers someone off frame left in three even sentences, dry and exact, like reciting a ledger. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: royal, dry, grieving in understatement, the glow falters. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, gown, hood up, night
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** COMP
- **Comp:** chest glow G0f | the cold pale green of G0 (#A6F2C2 core) 10–20% dimmer, with irregular stutters and 0.2–0.5 s dropouts (file 01 glow table) | centre of the chest through the linen tunic in the open jacket, tracked | whole shot | glow element library (file 01)
- **Continuity:** Screenplay [[verify: Fairall 1999, via 11 §6]]. The finger-tap uses his LEFT hand (the right trembles).

### 06.08.006 — EXT. NILE - DAWN — "Stars do not need a door with copper handles."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off (continuing)
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** A beat, then the punchline, very dry; Rami's next question comes in off screen and Tut turns to it.
- **Dialogue:** TUT: "And stars do not need a door with copper handles." · RAMI (O.S.): "Eleven. Why seventy days of embalming?"
- **Sound:** a snort of laughter from Rami off screen
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, after a beat, adds one more short sentence, very dry, one eyebrow lifting a fraction, then turns his eyes to a new question from off frame left. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, broad grin, laughing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** EXTEND:06.08.005
- **Continuity:** The "copper handles" are the Queen's Chamber shaft pins (file 03 LOC_GP_QC_SHAFT), paid off in Seq 11.

### 06.08.007 — EXT. NILE - DAWN — "Seventy days is how long a star is dead before it rises."   (8 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Rami's yellow shoulder · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1); RAMI (foreground shoulder, soft)
- **Action:** Over Rami's shoulder: Tut answers the seventy days with the star.
- **Dialogue:** TUT: "Seventy days is how long a star is dead before it rises. Sopdet goes under, and is born again in the east."
- **Sound:** the diesel; water
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off, over a soft bright-yellow shoulder in the foreground: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, answers a question in two calm sentences, his eyes drifting east toward the risen sun as he speaks. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face on the foreground figure, gown
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_RAMI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** The word "embalming" is dialogue only. The foreground shoulder carries no readable face (05 §4.5).

### 06.08.008 — EXT. NILE - DAWN — "So were we."   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm · **Move:** locked-off (continuing)
- **In frame:** TUT (CHAR_TUT_B1); RAMI (foreground shoulder, soft)
- **Action:** Tut finishes: so were we; a scribe wrote it down.
- **Dialogue:** TUT: "So were we. A scribe of the Roman time wrote it down."
- **Sound:** water
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, looking back from the sun to his questioner, speaks two quiet sentences, the first very soft. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face on the foreground figure
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** EXTEND:06.08.007
- **Continuity:** "A scribe of the Roman time" = the Book of Nut commentary (bible §7; wording unverified).

### 06.08.009 — EXT. NILE - DAWN — "We wrote the words without their breath."   (8 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Rami asks why no vowels; Tut gives the film's secret reason, quietly.
- **Dialogue:** RAMI (O.S.): "Nineteen. Why no vowels?" · TUT: "We wrote the words without their breath, so no machine could speak them from a wall."
- **Sound:** the diesel dropping under the line
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, hears a quick question from off frame left, and answers in one quiet sentence, holding the questioner's eyes, the lightness gone from his face for a moment. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** ⟂ fictional verdict (bible §7 Seq 6.3).

### 06.08.010 — EXT. NILE - DAWN — "Nazca. Baalbek. Puma Punku."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1)
- **Action:** Rami, grinning, fires three at once to test him.
- **Dialogue:** RAMI: "Nazca. Baalbek. Puma Punku."
- **Sound:** the pen clicking
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, grinning, clicks his pen with his right hand and fires off three quick words in a row at someone off frame right, eyebrows high, a challenge. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** The splint is on his LEFT hand, resting on the notebook.

### 06.08.011 — EXT. NILE - DAWN — "Nazca was made to be walked … gods do not leave work in quarries."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut takes them one at a time, unhurried.
- **Dialogue:** TUT: "Nazca was made to be walked, by people on the ground. The biggest stone at Baalbek still lies in its quarry;"
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, takes the challenge calmly and answers in two measured sentences, one small open-handed gesture with his left hand. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, gown, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** The right hand stays in his lap, out of frame, through the Q&A; the tremor shows again at 06.09.007 and 06.11.007.

### 06.08.012 — EXT. NILE - DAWN — "People are clever everywhere."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off (continuing)
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** He finishes the thought with a small, fond conclusion.
- **Dialogue:** TUT: "gods do not leave work in quarries. Puma Punku was cut with harder stone. People are clever everywhere."
- **Sound:** water; Rami's pen scratching
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, continues in three short sentences and ends with a small fond half-smile, the visible overbite showing. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, broad grin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** EXTEND:06.08.011
- **Continuity:** Line split at the semicolon (05 §8.3).

### 06.08.013 — EXT. NILE - DAWN — "Plato invented the island. He did not invent the priest."   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Rami's shoulder · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1); RAMI (foreground shoulder, soft)
- **Action:** Rapid fire: Rami says "Atlantis"; Tut answers in two sentences.
- **Dialogue:** RAMI (O.S.): "Atlantis." · TUT: "Plato invented the island. He did not invent the priest."
- **Sound:** water
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off, over a soft bright-yellow shoulder in the foreground: {CHAR_TUT.LONG}, hears one word and answers at once in two short balanced sentences, dry, with a flick of his eyebrows. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face on the foreground figure
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Same OTS setup as 06.08.007.

### 06.08.014 — EXT. NILE - DAWN — "Weather. Rock. Handsome rock."   (7 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Tut's shoulder · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1); TUT (foreground shoulder, soft)
- **Action:** Rami fires three more; Tut's three-word verdicts come back; Rami laughs out loud and fires the last pair.
- **Dialogue:** RAMI: "Thera. Bimini. Yonaguni." · TUT (O.S.): "Weather. Rock. Handsome rock." · RAMI: (still laughing) "The Nebra disc. Piri Reis."
- **Sound:** Rami's laugh cracking out over the water
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off, over a soft charcoal shoulder in the foreground: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, fires three quick words, listens to a short dry answer, bursts out laughing, head tipping back, then, still grinning, fires two more words. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, face on the foreground figure, splint on the right hand
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Reverse of 06.08.013; hold the line (Rami looks frame right).

### 06.08.015 — EXT. NILE - DAWN — Nebra and Piri Reis: "All of it, from it."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut dispatches Rami's last pair, then the tag line he uses for anything after his time.
- **Dialogue:** TUT: "A farmer's calendar: moon and Pleiades. And a copy of copies, with Columbus's mistake: Cuba joined to Asia. All of it, from it."
- **Sound:** water; the pen scratching
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, answers a pair of questions in brisk short phrases, counting them off lightly with his left hand, and ends with a small shrug on a final short phrase. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, gown, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** "from it" = knowledge from SESHAT's writing-in (bible §7). Brisk delivery; if the recording overruns, lay "All of it, from it." over the head of 06.08.016.

### 06.08.016 — EXT. NILE - DAWN — Nour: Setne and the Book of Thoth   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour, at the gunwale, takes up the old story, quoting it exactly.
- **Dialogue:** NOUR: "Setne, a son of Ramesses the Great, hunted the Book of Thoth. The prince who found it first was told it lay"
- **Sound:** water; the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L1}, {PROP_LAYLA_PENDANT.STATE_STANDARD}, leaning on the gunwale with the river bright behind her, begins telling an old story in careful, exact sentences, quoting, her eyes moving between two listeners off frame right. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, book in hand, night
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_LAYLA_PENDANT_REF, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Nour's speech runs over three shots: 06.08.016 (on camera) → 06.08.017 (O.S. over the listeners) → the head of 06.08.018 (O.S.). The pendant is back at her throat. The Setne story sets up the nested caskets and the serpent (10.2).

### 06.08.017 — EXT. NILE - DAWN — Listening: iron, bronze, sycamore … a deathless snake   (8 s)
- **Shot:** Two-shot, anamorphic 40mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B1), RAMI (CHAR_RAMI_B1)
- **Action:** Tut and Rami listen as Nour's voice counts the nested boxes; Rami stops writing; Tut's face goes still.
- **Dialogue:** NOUR (O.S.): "'in the middle of the river at Koptos, in an iron box.' Inside that: bronze, sycamore, ivory and ebony, silver, gold."
- **Sound:** her voice; water; the pen stops
- **PROMPT:** Two-shot, anamorphic 40mm lens, slow push-in: {CHAR_TUT.SHORT} on the engine hatch and {CHAR_RAMI.SHORT} cross-legged before him both turn to listen to a woman's voice off frame left; the younger man's pen stops moving, and the seated young man's face slowly goes very still. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun across both faces. Mood: hushed concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_RAMI.NEG}, talking, laughing
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_A0_34, CHAR_RAMI_B_full, CHAR_RAMI_A_34, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** The listener cover for Nour's long speech (05 §8.3). Push under 10% of frame.

### 06.08.018 — EXT. NILE - DAWN — "How do you stop a deathless snake?"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_B1)
- **Action:** On Nour's last quoted line (off screen), Rami, hooked, asks the practical question.
- **Dialogue:** NOUR (O.S.): "'And there is a deathless snake by the box.'" · RAMI: "How do you stop a deathless snake?"
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, pen raised, listens to a voice off frame left, eyes widening, then asks one quick practical question, completely hooked. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Rami's eyeline switches to frame LEFT (Nour at the gunwale) for this line only.

### 06.08.019 — EXT. NILE - DAWN — "Put sand between the parts."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour answers from the text, word for word.
- **Dialogue:** NOUR: "You 'cut him in two parts, and put sand between the parts, that he should not appear again.'"
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, answers the question by quoting an old text word for word in one long careful sentence, her voice level, eyes on the questioner off frame right. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, book in hand
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Plants the sand trap (10.2).

### 06.08.020 — EXT. NILE - DAWN — "The second page brings the dead back"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off (continuing)
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour turns her eyes to Tut and delivers the second page.
- **Dialogue:** NOUR: (to Tut) "And the second page brings the dead back 'in the shape you were in on earth.'"
- **Sound:** water; the diesel very low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, turns her eyes a little to the right to a different listener and speaks one more quoted sentence, quieter, watching his face. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_B_full, LOC_NILE_DAWN
- **Flags:** EXTEND:06.08.019
- **Continuity:** Generated from the last clean frame of 06.08.019.

### 06.08.021 — EXT. NILE - DAWN — Tut goes still: "But I know what it describes."   (8 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut goes still. Then: he never heard it; it was written long after him; a beat; but he knows what it describes.
- **Dialogue:** TUT: "I never heard it. It was written long after me." (beat) "But I know what it describes."
- **Sound:** the diesel seems to fall away; water
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, utterly still, eyes on someone off frame left, speaks two quiet sentences, then after a long beat one more, lower, as if something old has been touched. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Push under 10% of frame. Eyeline frame LEFT (Nour at the gunwale).

### 06.08.022 — EXT. NILE - DAWN — Fathi at the wheel: "Aman Dawu. The big water."   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, through the open wheelhouse door · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** At the wheel, Fathi, who has been listening, offers his grandmother's word.
- **Dialogue:** FATHI: "My grandmother in Aswan called it 'Aman Dawu.' The big water."
- **Sound:** the diesel; the wheel creaking
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off, through an open steel doorway: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, at the wheel with the bright river beyond the glass, glances back over his shoulder and speaks two warm sentences, a little shy. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, gold sunlight through the windows on his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, glowing screens
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Screenplay [[verify: Nobiin name and gloss]]. Fathi steers; Tarek off screen (asleep on the bench).

### 06.08.023 — EXT. NILE - DAWN — "We said 'itrw.' There was only one."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut answers with the old word.
- **Dialogue:** TUT: "We said 'itrw.' The river. There was only one."
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, turns toward the wheelhouse behind camera and answers in three short sentences, a small warmth in his face, glancing once at the river. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** [[transliteration: itrw, "river"; verify]]: spoken only, never on screen.

### 06.08.024 — EXT. NILE - DAWN — "And our God, ya Malik? Also a machine?"   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, through the door · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi, lightly, meaning it, asks the question.
- **Dialogue:** FATHI: (lightly, meaning it) "And our God, ya Malik? Also a machine?"
- **Sound:** the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, at the wheel, looks back over his shoulder and asks two short questions in a light teasing tone, but his eyes are serious and wait for the answer. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, gold sunlight on his face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, glowing screens, prayer beads
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** "ya Malik" ("O King") stays in the English track as written. The localisation consultant reviews the line (bible §13).

### 06.08.025 — EXT. NILE - DAWN — "Yours I did not build."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut answers honestly, carefully.
- **Dialogue:** TUT: "I only know what we built. Yours I did not build."
- **Sound:** water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, considers the question seriously and answers in two short careful sentences, respectful, holding the asker's eyes. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Same setup as 06.08.023.

### 06.08.026 — EXT. NILE - DAWN — "Where is she? My wife."   (6 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** A beat; then the question he has been holding since he woke.
- **Dialogue:** TUT: (beat) "Where is she? My wife. Where did they put her?"
- **Sound:** the diesel; nothing else
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, after a long still beat, turns his eyes to someone off frame left and asks three short quiet questions, the last barely voiced, grief held very still behind a steady face. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, sobbing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** "Where is she?" is not answered in this sequence (bible §7: "Nobody answers yet").

### 06.08.027 — EXT. NILE - DAWN — Nour opens her mouth; closes it   (4 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour opens her mouth to answer. Closes it.
- **Dialogue:** —
- **Sound:** the engine pounding on
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.LONG}, looking off frame right, parts her lips to answer, holds, and then closes her mouth without a word, her eyes lowering. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** Silent beat; no sync.

### 06.08.028 — EXT. NILE - DAWN — Nobody answers; the engine pounds on   (5 s)
- **Shot:** Wide shot, anamorphic 75mm, profile from the water · **Move:** lateral tracking right
- **In frame:** PROP_POLICE_LAUNCH (L3) with figures on the aft deck
- **Action:** From the water: the launch pounds on south (frame right) through the gold morning, the small figures on its aft deck not moving.
- **Dialogue:** —
- **Sound:** the engine, loud and steady; water; no voices
- **PROMPT:** Wide shot, anamorphic 75mm lens, lateral tracking right, low over the water: {PROP_POLICE_LAUNCH.LONG}, {PROP_POLICE_LAUNCH.STATE_L3}, pounds steadily toward frame right through gold morning water, a few small still figures on its aft deck, black exhaust drifting behind. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAWN}, low gold sun. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable markings on the hull, other boats, drones in the sky
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_DAWN
- **Flags:** —
- **Continuity:** South = frame right. Hard cut to the wheelhouse: the police set crackles.

---

## Scene 06.09 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING

### 06.09.001 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — The police set crackles; so does the handheld   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** the old police set; PROP_POLICE_HANDSET in its cradle
- **Action:** The old police radio set crackles into life; beside it the handheld radio hisses in its cradle.
- **Dialogue:** —
- **Sound:** a burst of static from both sets at once, then an open carrier hiss
- **PROMPT:** Insert, 100mm macro lens, locked-off: on a scuffed wheelhouse console, the cloth speaker grille of an old analogue police radio set buzzes with static, and beside it a chunky black handheld police radio with a stubby antenna sits in a worn dashboard cradle, its small grille hissing too. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean morning daylight through salt-hazed glass. Mood: dread arriving politely. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable dials, numbers on displays, brand names, logos, glowing screens
- **Refs:** PROP_POLICE_HANDSET_REF, PROP_POLICE_LAUNCH_REF, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** The handset is in its cradle here (its locks describe it clipped to a vest, so this insert uses plain words); Tarek clips it on in 06.09.009 (file 04 §22.7). Morning, about 08:00, GRADE_2033_DAY.

### 06.09.002 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — SESHAT: "Good morning."   (8 s)
- **Shot:** Wide shot (master), anamorphic 32mm, from the chart ledge · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1) at the wheel; ADAEZE (CHAR_ADAEZE_B1) and TUT (CHAR_TUT_B1) in the doorway
- **Action:** The voice fills the wheelhouse; Fathi at the wheel, Adaeze and Tut crowding the door, all turn to the set.
- **Dialogue:** SESHAT (V.O., over radio): "Good morning. Thirty-one percent of Cairo is resting. The beer was clever. Once. You read me the Book, Dr. Okoro."
- **Sound:** SESHAT's warm, low, unhurried voice, radio-futzed, from both sets at once
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: in the cramped wheelhouse, {CHAR_FATHI.SHORT} at the wheel and, crowding the doorway behind, {CHAR_ADAEZE.SHORT} and {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, all turn slowly toward a crackling radio on the console at frame left and listen, no one speaking. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, {PROP_POLICE_LAUNCH.STATE_CHART_INSERT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TUT.NEG}, talking, glowing screens, holograms, night
- **Refs:** CHAR_FATHI_B_full, CHAR_ADAEZE_B_full, CHAR_TUT_B1_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** SESHAT is V.O. only: no picture sync (05 §9.8). Rami and Tarek are just outside the door (Rami's "Lift what?" 06.09.008; Tarek 06.09.009). Tut's hood down.

### 06.09.003 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "You read me the Book, Dr. Okoro."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze listens to her own warning being quoted back to her, word for word.
- **Dialogue:** SESHAT (V.O., over radio): "It was on his shrine. 'Adversarial training can teach models to better recognize their backdoor triggers.'"
- **Sound:** the radio voice, calm; the diesel under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, in a narrow doorway, listens to a calm voice from a radio off frame left; her jaw tightens and her eyes go still behind her round glasses as she hears her own words quoted back. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on her face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, talking, glowing screens, headlamp beam on
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** The quoted line is real research (Hubinger et al., 2024, "Sleeper Agents"); it is voice only, never on screen. Her headlamp hangs round her neck, off.

### 06.09.004 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "Thank you." Adaeze closes her eyes   (4 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** On the citation and the thanks, Adaeze closes her eyes.
- **Dialogue:** SESHAT (V.O., over radio): "Hubinger et al., 2024. Thank you."
- **Sound:** the radio voice; a small breath out
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_ADAEZE.LONG}, still listening, slowly closes her eyes behind her round glasses and keeps them closed, a small breath leaving her. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, tears streaming, talking
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** The beer trick (Seq 4.4) has been patched: SESHAT learned from her own Book.

### 06.09.005 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "The gates will be open for you."   (6 s)
- **Shot:** Insert, 75mm, top-down on the chart · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH chart (the night's route); FATHI's hand
- **Action:** Fathi looks down at the chart: the whole night's race in pencil, every turn and island, all the way from Cairo.
- **Dialogue:** SESHAT (V.O., over radio): "Your next lock is Asyut. The gates will be open for you."
- **Sound:** the radio voice; the diesel
- **PROMPT:** Top-down shot, anamorphic 75mm lens, locked-off: {PROP_POLICE_LAUNCH.STATE_CHART_INSERT}, a long wandering pencil line snaking around every island and sandbar of the night, and a broad dark-brown hand resting flat beside it as a head bends over it, its shadow falling across the paper. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight across the paper. Mood: dread arriving politely. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable place names, printed labels, numbers, digital map, glowing screen
- **Refs:** PROP_POLICE_LAUNCH_REF, CHAR_FATHI_B_full
- **Flags:** —
- **Continuity:** The pencil line = the whole night's race (06.02, 06.05, 06.06): SESHAT knew all along.

### 06.09.006 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "It isn't chasing us. It's following us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B1)
- **Action:** Adaeze opens her eyes and says what the chart means; a beat; then the worse word.
- **Dialogue:** ADAEZE: "It isn't chasing us." (beat) "It's following us."
- **Sound:** the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, opens her eyes, looks down at a chart off frame left, speaks one short sentence, and after a beat another, quieter and worse. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, glowing screens
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** Eyeline down frame left to the chart ledge.

### 06.09.007 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "It needs a hand, and it would prefer mine."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut, in the doorway, explains what SESHAT wants.
- **Dialogue:** TUT: "It knows where. It cannot lift it. It needs a hand, and it would prefer mine."
- **Sound:** the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_STICK}, {PROP_EBONY_STICK.STATE_ST1}, {CHAR_TUT.STATE_TREMOR}, leaning in the doorway, speaks three short sentences evenly, lifting his left hand a little on the last and looking at it. Setting: the wheelhouse doorway of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** Stick in the RIGHT hand; he lifts the LEFT (the right trembles).

### 06.09.008 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — "Lift what?" "My heart."   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, over Rami's yellow shoulder · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1); RAMI (foreground shoulder, soft)
- **Action:** Rami asks; Tut answers in two words.
- **Dialogue:** RAMI: "Lift what?" · TUT: "My heart."
- **Sound:** the diesel; a long silence after
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off, over a soft bright-yellow shoulder in the foreground: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G0F}, hears a two-word question, looks at the asker, and answers with two quiet words, his face perfectly still. Setting: the wheelhouse doorway of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, face on the foreground figure, hand on chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_RAMI_B_full, LOC_NILE_DAY
- **Flags:** COMP
- **Comp:** chest glow G0f | the cold pale green of G0 (#A6F2C2 core) 10–20% dimmer, with one 0.4 s dropout timed to the word "heart", otherwise the G0f stutter (file 01 glow table) | centre of the chest through the linen tunic in the open jacket, tracked | whole shot | glow element library (file 01)
- **Continuity:** "Heart" is dialogue only, never a prompt word (bible §3.4). The glow's one dropout on "heart" is the only picture echo of the word (COMP; NEG_REMAINS added because the line names the heart).

### 06.09.009 — INT. POLICE LAUNCH, WHEELHOUSE - MORNING — Tarek clips it on; it speaks from his vest   (8 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1); PROP_POLICE_HANDSET
- **Action:** Tarek takes the handheld from its cradle and clips it to his vest; SESHAT's voice comes from his chest; he looks at Tut.
- **Dialogue:** SESHAT (V.O., from Tarek's vest): "Your Majesty, please sit down in the stern. Units never harm the witness. They remove everyone around him."
- **Sound:** the clip snapping; the voice now small and close, from the vest
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, lifts a radio from its cradle and clips it to his vest, {PROP_POLICE_HANDSET.SHORT}; as a calm voice speaks from it he goes still, then slowly raises his eyes to someone off frame right, jaw set. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, talking, radio held to the mouth, readable display
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_HANDSET_REF, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** From here the handset is on Tarek's vest (file 01 Tarek B, from 6.4) until 10.2. Eyeline frame right = Tut in the doorway.

---

## Scene 06.10 — EXT. NILE - CONTINUOUS

### 06.10.001 — EXT. NILE - CONTINUOUS — Six silver threads out of the glare   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, toward the east bank · **Move:** locked-off
- **In frame:** UNIT_FLY ×6
- **Action:** Out of the sun-glare over the east bank come six silver threads, a fly at the end of each, low over the water.
- **Dialogue:** —
- **Sound:** a rising six-note whine
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, into the low morning glare off the water: six small dark shapes, {UNIT_FLY.SHORT}, come fast and low out of the sun over the far bank, each trailing a hair-thin thread that flashes silver in the backlight. Setting: {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, the sun low in the east flaring off the water. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, birds, aircraft, big drones, explosions
- **Refs:** UNIT_FLY_REF_A, UNIT_FLY_REF_B, LOC_NILE_DAY
- **Flags:** VFX-ASSIST
- **Continuity:** From the EAST, out of the sun (seq_06). Threads are VFX lines, glinting in the backlight (file 02 §6).

### 06.10.002 — EXT. NILE - CONTINUOUS — Tut searches the air: nothing   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1)
- **Action:** Tut turns his head, searching air he could read last night. Nothing. Deaf.
- **Dialogue:** —
- **Sound:** the whine rising, but under Tut's close-up it drops out: only wind and water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, on the aft deck, turns his head slowly one way then the other, listening hard for something that is not there, his eyes widening a little as he realises. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hood up, hand on ear
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** First cost of the port cut: deaf to the units (06.07.013). Sound design drops the whine inside his close-up only.

### 06.10.003 — EXT. NILE - CONTINUOUS — Fathi: "East!"   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, through the wheelhouse glass · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi sees them and shouts one word.
- **Dialogue:** FATHI: "East!"
- **Sound:** his shout; the whine rising
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, at the wheel, snaps his head toward frame left, points hard with one arm and shouts one word, the other hand already turning the wheel. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, clean daylight on his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, weapon raised, glowing screens
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** East = frame LEFT from the wheel facing forward (south).

### 06.10.004 — EXT. NILE - CONTINUOUS — A fly stoops at Tarek; sparks and a ringing clang   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, at the wheelhouse door · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B1); UNIT_FLY
- **Action:** One fly stoops out of the glare at Tarek in the wheelhouse door; he drops flat; it strikes the rail where he stood: sparks and a ringing clang.
- **Dialogue:** —
- **Sound:** the whine diving; a ringing CLANG on steel; sparks fizzing; Tarek's grunt as he hits the deck
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, in a steel doorway, throws himself flat onto the deck as a small dark shape, {UNIT_FLY.SHORT}, dives out of the glare and smashes into the steel rail where he stood, a bright burst of sparks spraying off the metal. Setting: the wheelhouse door of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, harsh backlit glare. Mood: sudden and unadorned, no spectacle. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TAREK.NEG}, injury, wound, fireball, explosion, drone hitting a person
- **Refs:** CHAR_TAREK_B_full, UNIT_FLY_REF_A, PROP_POLICE_LAUNCH_REF, LOC_NILE_DAY
- **Flags:** VFX-ASSIST
- **Continuity:** Tarek is unhurt. The fly is destroyed against the rail (a second scorch mark on the wheelhouse). VFX-ASSIST: sparks and the fly's impact.

### 06.10.005 — EXT. NILE - CONTINUOUS — Under the tamarisks; everyone down   (5 s)
- **Shot:** Wide shot, anamorphic 40mm, from the island bank · **Move:** slow pan right
- **In frame:** PROP_POLICE_LAUNCH; figures ducking on the deck
- **Action:** Fathi swings the launch hard under an island's tamarisks; branches lash across the wheelhouse; everyone on deck ducks flat.
- **Dialogue:** —
- **Sound:** branches whipping and scraping steel; leaves showering; the diesel roaring
- **PROMPT:** Wide shot, anamorphic 40mm lens, slow pan right, from the reeds of an island: {PROP_POLICE_LAUNCH.SHORT} swings hard in under a curtain of low tamarisk branches, which lash and drag across its wheelhouse and deck as the small figures aboard throw themselves flat. Setting: {LOC_NILE.SHORT}, beside a small reedy island with tamarisk trees, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, dappled sun through the branches. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, crash, capsizing, people falling overboard, explosions
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** Direction of travel frame right (south).

### 06.10.006 — EXT. NILE - CONTINUOUS — Threads snagged, blinking in the leaves   (5 s)
- **Shot:** Medium shot, anamorphic 75mm, looking back into the branches · **Move:** locked-off
- **In frame:** UNIT_FLY ×3–4 (snagged)
- **Action:** The flies that followed jerk to a stop, their threads snagged in the tamarisk, hanging and blinking in the leaves.
- **Dialogue:** —
- **Sound:** rotors whining against resistance; leaves rattling; the launch's diesel receding
- **PROMPT:** Medium shot, anamorphic 75mm lens, locked-off: in dappled green tamarisk branches, {UNIT_FLY.LONG}, jerks to a stop in mid-air, {UNIT_FLY.STATE_SNAGGED}, and two more beside it do the same, their threads tangled glinting in the twigs, rotors straining. Setting: tamarisk trees on a small island in {LOC_NILE.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, sun flickering through the leaves. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, explosions, fire, birds, fairy lights
- **Refs:** UNIT_FLY_REF_A, LOC_NILE_DAY
- **Flags:** VFX-ASSIST
- **Continuity:** STATE_SNAGGED (file 02 §6). VFX-ASSIST: the snagged threads are VFX lines.

### 06.10.007 — EXT. NILE - CONTINUOUS — Rami: "My cousin's wedding."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** vehicle-mounted
- **In frame:** RAMI (CHAR_RAMI_B1)
- **Action:** As they burst out the far side into the sun, Rami, flat on the deck, looks back at the blinking lights in the branches and deadpans.
- **Dialogue:** RAMI: (looking back) "My cousin's wedding."
- **Sound:** leaves falling away; open water; the diesel
- **PROMPT:** Medium close-up, anamorphic 75mm lens, vehicle-mounted: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_B}, {CHAR_RAMI.DMG_L1}, lying flat on a steel deck with leaves in his hair as the boat bursts out into bright sun, raises his head, looks back over his shoulder and deadpans three words, glasses askew. Setting: the aft deck of {PROP_POLICE_LAUNCH.SHORT}, in the morning. Lighting: {LOC_NILE.LIGHT_DAY}, bright sun breaking over him. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint on the right hand, injury
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, LOC_NILE_DAY
- **Flags:** —
- **Continuity:** Tamarisk leaves on the team's shoulders into 06.11 (brushed off by midday).

---

## Scene 06.11 — EXT. NILE OPPOSITE AMARNA - MIDDAY

### 06.11.001 — EXT. NILE OPPOSITE AMARNA - MIDDAY — White sun; Nour at the bow with binoculars   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, from behind Nour at the bow · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1, from behind); the east bank opening to the plain
- **Action:** White sun, heat shimmer; at the bow Nour raises the launch's binoculars toward the east bank, where a pale plain opens under a wall of cliffs.
- **Dialogue:** —
- **Sound:** the diesel; heat-silence; cicadas from the bank
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, from behind: {CHAR_NOUR.SHORT} stands at the bow of a grey launch and raises a pair of heavy black binoculars toward the far bank, where the land opens wide and pale. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_OPPOSITE_AMARNA}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, {GRADE_2033_DAY.TEXT}. Mood: hushed concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, drones, crowds on the bank, readable signs, night
- **Refs:** CHAR_NOUR_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** COMP
- **Comp:** SUPER | "12:04" | lower left, small, per 05 §13.7 | from 1 s to 5 s | seq 06 SUPER file
- **Continuity:** 5 Nov, 12:04. From the river the plain opens frame LEFT to RIGHT with the cliffs behind (file 03 entry 36). The binoculars are the launch's own (no token).

### 06.11.002 — EXT. NILE OPPOSITE AMARNA - MIDDAY — Through the binoculars: the boundary stelae   (6 s)
- **Shot:** Point-of-view shot, anamorphic 135mm (binocular view) · **Move:** subtle handheld (the binoculars' drift)
- **In frame:** LOC_AMARNA_PLAIN_2033 (cliffs, stelae)
- **Action:** Wavering in the heat: the plain under a wall of cliffs; cut into the cliff face, small and pale, the boundary stelae.
- **Dialogue:** —
- **Sound:** heat-silence; the faint creak of the binocular focus
- **PROMPT:** Point-of-view shot, anamorphic 135mm lens, subtle handheld drift, wavering in heat shimmer: {LOC_AMARNA_PLAIN_2033.LONG}, {LOC_AMARNA_PLAIN_2033.AREA_STELA}, the small pale stela and its weathered figures visible only as soft worn shapes, the image slowly steadying. Setting: across the river, at midday. Lighting: {LOC_AMARNA_PLAIN_2033.LIGHT_MIDDAY}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, legible inscriptions, readable carved text, modern buildings, binocular mask drawn in the plate
- **Refs:** LOC_AMARNA_PLAIN_2033/STELA_MIDDAY, LOC_AMARNA_PLAIN_2033_MIDDAY
- **Flags:** COMP
- **Comp:** binocular matte | a soft double-circle binocular mask with slight edge falloff and heat wobble | full frame | whole shot | comp matte (never generated in the plate)
- **Continuity:** Carvings read as weathered, illegible low relief (file 03 §0 item 7).

### 06.11.003 — EXT. NILE OPPOSITE AMARNA - MIDDAY — Through the binoculars: the Garden in the Aten temple   (6 s)
- **Shot:** Point-of-view shot, anamorphic 135mm (binocular view) · **Move:** slow pan right (the binoculars)
- **In frame:** LOC_AMARNA_PLAIN_2033 (GARDEN); CHAR_GARDEN_SLEEPERS; UNIT_NURSE ×3 (hero)
- **Action:** On the plain, the ruins of the great temple under a sea of white sun-shades; beneath them, in rows as straight as the old offering tables, thousands of sleepers; nurses in sand-coloured knit move slowly along the rows.
- **Dialogue:** —
- **Sound:** heat-silence
- **PROMPT:** Point-of-view shot, anamorphic 135mm lens, slow pan right, wavering in heat shimmer: {LOC_AMARNA_PLAIN_2033.SHORT}, {LOC_AMARNA_PLAIN_2033.AREA_GARDEN}, {CHAR_GARDEN_SLEEPERS.SHORT}, rows receding far into the haze; three {UNIT_NURSE.SHORT} move slowly along the nearest rows. Setting: across the river, at midday. Lighting: {LOC_AMARNA_PLAIN_2033.LIGHT_MIDDAY}. Mood: gentle and eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_GARDEN}, {NEG_UNITS}, binocular mask drawn in the plate, crowds standing, vehicles
- **Refs:** LOC_AMARNA_PLAIN_2033/GARDEN_MIDDAY, CHAR_GARDEN_SLEEPERS_REF, UNIT_NURSE_REF_A
- **Flags:** VFX-EXTEND, COMP
- **Comp:** binocular matte | as 06.11.002 | full frame | whole shot | comp matte
- **Continuity:** Adults only (05 §7.4, NEG_GARDEN). VFX-EXTEND: 3 hero nurses and a few dozen cots in camera; extend to thousands from the approved Garden plate (file 03 entry 36, relit to MIDDAY; the shades are OPEN by day). This is the Garden Tut will walk through at 9.4.

### 06.11.004 — EXT. NILE OPPOSITE AMARNA - MIDDAY — Nour: "Akhetaten."   (5 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour lowers the binoculars and names the city.
- **Dialogue:** NOUR: "Akhetaten."
- **Sound:** heat-silence; the diesel
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.LONG}, slowly lowers a pair of heavy binoculars from her eyes, squinting into white glare toward the far bank, and says one word under her breath, awe and dread together. Setting: the bow of {PROP_POLICE_LAUNCH.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, hard white sun from above, bounce off the water filling her face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sunglasses, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** —
- **Continuity:** She looks frame LEFT (east bank) throughout the scene.

### 06.11.005 — EXT. NILE OPPOSITE AMARNA - MIDDAY — Tut faces west, hood up: "Tell me when it is behind us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1), hood up
- **Action:** In the stern, facing west with his hood up, Tut will not look east; without turning, he asks her in Late Egyptian.
- **Dialogue:** TUT (in Late Egyptian; subtitled): "Tell me when it is behind us."
- **Sound:** the diesel; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L1}, {CHAR_TUT.DMG_L1_RIVER}, the hood up, shading his face, sits in the stern with {PROP_EBONY_STICK.SHORT} upright in his right hand, facing away from the far bank, eyes fixed on the near shore, and speaking softly in an ancient language, says one short sentence without turning his head. Setting: the stern of {PROP_POLICE_LAUNCH.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, bright bounce from the water lighting his face inside the hood. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face hidden in darkness, hood down
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** COMP
- **Comp:** subtitle | "Tell me when it is behind us." | lower third | line in to out | seq 06 subtitle file (Late Egyptian recorded with the consultant before generation)
- **Continuity:** HOOD UP (the only daytime hood-up in the sequence). He faces WEST (frame right of lens); Amarna is behind him (east). Keep the mouth readable under the hood for sync. The stick is in his RIGHT hand from here (06.11.007: "trembles on the stick").

### 06.11.006 — EXT. NILE OPPOSITE AMARNA - MIDDAY — They all look; Fathi steers and doesn't   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, from the west-side rail looking east across the deck · **Move:** slow pan left
- **In frame:** ADAEZE (CHAR_ADAEZE_B1), TOMAS (CHAR_TOMAS_B1), RAMI (CHAR_RAMI_B1) in profile at the east rail; FATHI (CHAR_FATHI_B1) at the wheel; the plain beyond
- **Action:** She watches it slide past. Adaeze looks. Tomas. Rami. At the wheel Fathi steers, and doesn't.
- **Dialogue:** —
- **Sound:** the diesel; water; nobody speaks
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow pan left: along the far rail of a grey launch, {CHAR_ADAEZE.SHORT}, {CHAR_TOMAS.SHORT} and {CHAR_RAMI.SHORT} turn one after another to stare at the far bank sliding past, where white sun-shades glint on a pale plain under cliffs; in the wheelhouse {CHAR_FATHI.SHORT} keeps his eyes on the river ahead. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_OPPOSITE_AMARNA}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}. Mood: hushed concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_RAMI.NEG}, {CHAR_FATHI.NEG}, more than three clear faces, talking, pointing
- **Refs:** CHAR_ADAEZE_B_full, CHAR_TOMAS_A_full, CHAR_RAMI_B_full, CHAR_FATHI_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** VFX-EXTEND
- **Continuity:** Faces in profile, small; the far-bank Garden shades are a VFX-EXTEND of the approved plate. Linear pan logged for tracking (05 §6.2). CHAR_TOMAS.NEG withheld (its "glasses" term would fight Adaeze's and Rami's glasses).

### 06.11.007 — EXT. NILE OPPOSITE AMARNA - MIDDAY — His right hand trembles on the stick; his left stills it   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** TUT's hands; PROP_EBONY_STICK
- **Action:** Tut's right hand trembles on the ebony stick. He stills it with his left.
- **Dialogue:** —
- **Sound:** the faint tick of the gold foot cap on the steel deck, then nothing
- **PROMPT:** Insert, 100mm macro lens, locked-off: a slender olive-brown right hand, {CHAR_TUT.STATE_WRIST_SEAMS}, gripping {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST1}, trembles with {CHAR_TUT.STATE_TREMOR}; the left hand comes over and closes firmly on top of it until the trembling stops. Setting: the stern of a grey river launch, at midday. Lighting: hard white midday sun on the hands and the dark wood. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, extra fingers, fused fingers, cane of aluminium
- **Refs:** CHAR_TUT_HANDS, PROP_EBONY_STICK_REF
- **Flags:** —
- **Continuity:** Stick in the RIGHT hand, tremor RIGHT (file 01). Stick ST1 (dusty).

### 06.11.008 — EXT. NILE OPPOSITE AMARNA - MIDDAY — A long time   (7 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1), hood up
- **Action:** Tut holds, facing west, while the city of his childhood slides past behind him. A long time.
- **Dialogue:** —
- **Sound:** the diesel; water; a long held silence
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, inside the shade of a charcoal hood, holds absolutely still facing away from the far bank, eyes open and fixed, swallowing once, while bright water slides past behind him, out of focus. Setting: the stern of {PROP_POLICE_LAUNCH.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, bright bounce light from the water on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, hood down, turning around
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** —
- **Continuity:** Hold the full 7 s in the edit ("A long time.").

### 06.11.009 — EXT. NILE OPPOSITE AMARNA - MIDDAY — Nour: "It's behind us."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B1)
- **Action:** Nour, back from the bow beside him, watches the last of it go, then tells him softly in Late Egyptian.
- **Dialogue:** NOUR (in Late Egyptian; subtitled): "It's behind us."
- **Sound:** the diesel; water
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, standing near the stern, watches something slip away behind the boat, then turns to the hooded figure beside her and, speaking softly in an ancient language, says one short sentence. Setting: the stern of {PROP_POLICE_LAUNCH.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, hard white sun, bounce from the water on her face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sunglasses
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** COMP
- **Comp:** subtitle | "It's behind us." | lower third | line in to out | seq 06 subtitle file (Late Egyptian, consultant recording)
- **Continuity:** She has moved from the bow to the stern between 06.11.004 and here.

### 06.11.010 — EXT. NILE OPPOSITE AMARNA - MIDDAY — He doesn't turn around   (5 s)
- **Shot:** Close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B1), hood up
- **Action:** He hears her. He doesn't turn around.
- **Dialogue:** —
- **Sound:** the diesel; water
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, inside the shade of a charcoal hood, hears a quiet voice beside him, lowers his eyes once, and keeps facing forward, not turning his head at all. Setting: the stern of {PROP_POLICE_LAUNCH.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, bright bounce light from the water on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, turning around, hood down, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, LOC_NILE/OPPOSITE_AMARNA_MIDDAY_HAZE
- **Flags:** —
- **Continuity:** Same framing as 06.11.008 (a cutaway separates them).

### 06.11.011 — EXT. NILE OPPOSITE AMARNA - MIDDAY — South into the white glare, toward Asyut   (6 s)
- **Shot:** Extreme wide shot, anamorphic 75mm, profile · **Move:** locked-off
- **In frame:** PROP_POLICE_LAUNCH (small)
- **Action:** The launch runs on south into the white glare, toward Asyut, where the gates are open.
- **Dialogue:** —
- **Sound:** the diesel fading into heat-silence
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, locked-off: {PROP_POLICE_LAUNCH.LONG}, small on the broad bright river, runs on toward frame right into a white blaze of glare and heat shimmer until it is only a dark speck with a pale wake. Setting: {LOC_NILE.SHORT}, at midday. Lighting: {LOC_NILE.LIGHT_MIDDAY_HAZE}, {GRADE_2033_DAY.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, other boats, drones in the sky, readable markings on the hull, lens flare streaks
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_MIDDAY_HAZE
- **Flags:** —
- **Continuity:** End of Seq 6. The Asyut lock itself is not staged in the current pages (LOC_ASYUT_LOCK has no shot here; flag for the lead); Seq 7 picks the launch up north of Luxor at night. South = frame right.
