# SEQUENCE 10 — THE LAND OF SOKAR · shot list and AI-video prompts

**Film:** HERE AM I · **Screenplay:** `screenplay/seq_10.fountain` (pp. 92–101, 10 pages; Act Three opens) · **Story time:** 7 Nov 2033, sunset (~17:00) at the quarry → Saqqara 20:00–22:30 (bible §12) · **Cards:** THE FOURTH HOUR — THE LAND OF SOKAR · THE FIFTH HOUR — THE BOAT BECOMES A SERPENT
**Delivery:** photoreal live action, 1920×1080, 16:9, 24 fps, clips of 4–8 s. Fixed wording is inserted by tokens (`{SUFFIX}`, `{NEG}`, `{NEG_*}`, `{TOKEN.FIELD}` from `production_bible/locks.json`) and expanded by `shots_md2jsonl.py` into `shots/seq_10_shots.jsonl`. The writer's own words stay at or under 70 per prompt; each prompt has at most one LONG lock (file 05 §5.2).

**Shot count:** 136 · **Running time:** 717 s ≈ 12.0 min (target 10 min ±20%; the dialogue-dense pit scene carries the overage) · **Average shot:** 5.3 s
**Flags:** COMP 40 · VFX-ASSIST 13 · VFX-EXTEND 7 · EXTEND chains 3 (10.06.010→011, 10.06.018→019, 10.06.033→034)

## Scene list

| # | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 10.01 | EXT. ABANDONED LIMESTONE QUARRY - SUNSET | 10.01.001–007 | 7 | 39 s |
| 10.02 | INT. GEM CONSERVATION CENTRE, MUMMY LAB - DUSK (captivity) | 10.02.001–010 | 10 | 58 s |
| 10.03 | EXT. SAQQARA PLATEAU - NIGHT (card: the Fourth Hour) | 10.03.001–008 | 8 | 46 s |
| 10.04 | INT. SERAPEUM, LESSER VAULTS - NIGHT | 10.04.001–005 | 5 | 27 s |
| 10.05 | INT. SERAPEUM, GREATER VAULTS - CONTINUOUS | 10.05.001–013 | 13 | 73 s |
| 10.06 | INT. SERAPEUM, GREATER VAULTS - THE PIT - CONTINUOUS (card: the Fifth Hour) | 10.06.001–037 | 37 | 184 s |
| 10.07 | INT. GEM GRAND ATRIUM - NIGHT (the Garden; Nour's minute) | 10.07.001–007 | 7 | 42 s |
| 10.08 | INT. SERAPEUM, GREATER VAULTS - NIGHT (residual risk; Youssef and Karim; the sand) | 10.08.001–036 | 36 | 166 s |
| 10.09 | INT. SERAPEUM, SERVICE TUNNEL - NIGHT | 10.09.001–005 | 5 | 35 s |
| 10.10 | EXT. SAQQARA DESERT - SERVICE TUNNEL MOUTH - NIGHT | 10.10.001–008 | 8 | 47 s |

## Look codes and states carried through the sequence
- **Tut:** wardrobe B, damage L2 until the knee cracks at 10.08.016, then L3 (left trouser knee torn open, hood torn, heavy dust). Chest glow G1 (COMP wherever the tunic is in frame). Seams: left wrist cracked (9.4), plus the **left knee from 10.08.016**. Scar at the nape (never the port). Stick ST2 in the RIGHT hand all sequence (lost only at 11.5); the dagger in its gold sheath at the belt; the right-hand tremor; the notebook buttoned into the jacket (10.01.003).
- **Nour (captive):** wardrobe B at damage L2, face washed, glasses on the cord (on her face until 10.02.006), pendant at her throat. No shawl until the Hall.
- **Adaeze:** B at L3 with blue powder, red headlamp in the Serapeum, kit slung (JAR_HALF → thrown at 10.08.009). **Wardrobe C from 10.08.036** (dressed LEFT shin, limp).
- **Tarek:** B, dust to L3; handset dead from 10.04.002; ID discs ×2 added at 10.08.034. **Fathi:** B at L3; charges SACK → TAPED → FIRING. **Youssef and Karim:** wardrobe A (tan helmets); both fall at 10.08.020–022 by the kill grammar (never on screen on the ground).
- **Units:** shabti D0 (the reacher), D1 (the speaker); jackals ×3 D0→D1→GHOSTS→buried; excavators ×2 (A buried at 10.06.004); glass serpent S1 → carried out → Giza; Reis R4 (distant, 10.10.002).
- **Locations:** Serapeum geography: in from the Lesser Vaults at frame left, the lit pit at the far end, the service-tunnel door on the RIGHT-hand wall. The quarry sun sets at frame left. At the tunnel mouth, north (Giza) is frame left.

## Reference stills needed (approve and freeze before generation; file 05 §12)
**Characters (existing still ids):** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_TUT_B_night_34, CHAR_TUT_HANDS, CHAR_TUT_FOOT, CHAR_TUT_SEAMS_mirror · CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full · CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, CHAR_ADAEZE_C_full · CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full · CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full · CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_34, CHAR_YOUSSEF_A_full · CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full · CHAR_LAYLA_ASLEEP_MASTER (the only asleep-child image; 10.07.002–007 derive from it) · CHAR_GARDEN_SLEEPERS_still (use with the bracelets painted out: no bracelets in the atrium before 11.1).
**Derived look stills (image edits of the above, needed for this sequence):** CHAR_TUT_B2 (L2) and **CHAR_TUT_B3** (L3: torn left knee with the cracked seam ring, torn hood, dust to the thigh) from CHAR_TUT_B1_full · Nour captive look (B + L2, face clean, glasses on) from CHAR_NOUR_B_full · CHAR_ADAEZE_B3 (L3 + blue powder + red headlamp) from CHAR_ADAEZE_B_full · Tarek, Fathi, Youssef, Karim at L3 dust.
**Units:** UNIT_SHABTI_REF_A / _REF_B (plus a D1-dust variant) · UNIT_JACKAL_REF_A / _REF_B · UNIT_EXCAVATOR_REF_A · UNIT_GLASS_SERPENT_REF_A / _REF_B (correct REF B to a BLACK wax serpent and a sycamore box) · UNIT_NURSE_REF_A · UNIT_REIS_REF_A (R4) · UNIT_RELAY_REF_A (node state) · UNIT_THREAD_REF_A · 3D assets: shabti, jackal (for the VFX-EXTEND rows and the jackal run).
**Props:** PROP_FARM_TRUCK_REF · PROP_DEMO_CHARGES_REF · PROP_RAMI_NOTEBOOK_REF · PROP_EBONY_STICK_REF · PROP_LAYLA_PENDANT_REF · PROP_CUTMAP_PROJECTION_REF (comp asset) · PROP_POLICE_HANDSET_REF · PROP_CASKET_NEST_REF · PROP_CONSERVATION_KIT_REF · PROP_ID_DISCS_REF.
**Location plates:** LOC_QUARRY_SUNSET_plate · LOC_GEM_CC/CAPTIVITY_DUSK_plate · LOC_SAQQARA_NIGHT_plate · LOC_SAQQARA/SERAPEUM_HEAD_NIGHT_plate · LOC_SAQQARA/TUNNEL_MOUTH_NIGHT_plate · LOC_SERAPEUM_LESSER_TORCH_plate · LOC_SERAPEUM_GREATER_WORKLIGHTS_plate, _TORCH_plate, _BLUE_plate · LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS_plate with state plates: stopper intact/split, SAND_TRAP before/after, pit intact / floor-collapsed (10.08.028) · LOC_SERAPEUM_GREATER/RED_BOX_TORCH_plate · LOC_SERAPEUM_SERVICE_TUNNEL_TORCH_plate · LOC_GEM_ATRIUM/GARDEN_GARDEN_plate (+ clean plate for the extension) · LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS_plate (distant pyramids, 10.10.002).
**Comp assets:** hour cards ×2 with the Egyptologist's "hour" sign · red hieratic papyrus band (Apep name) · subtitle file for 7 Arabic/Middle Egyptian lines · chest-glow G1 element · knee seam-crack element · slit-brightening timings · NIR jackal POV grade.

## Open points for the lead
1. **Serpent state at the reveal:** the screenplay's "light moves slowly, like breath" is played as S1; file 02 lists S0 "dormant (in the pit)".
2. **The reaching shabti's slit "holds"** (steady), not the 8.4 halted ember.
3. **Runtime 12.0 min** for 10 pages. If the edit needs 10.5 min, the candidates to lose are 10.05.002, 10.06.029, 10.08.013 and 10.08.032.
4. **"ya Malik"** is left unsubtitled in the English master (10.10.007).
5. **Tut's damage level:** file 01 lists L3 for all of Seq 10, but the L3 lock carries the torn left knee, which cannot precede the fold; Tut plays L2 (CHAR_TUT_B2) until 10.08.016 and L3 (CHAR_TUT_B3) after it. Adaeze and the soldiers build to L3 on entering the Serapeum (10.04).
6. **QA pass (this revision):** added 10.08.026 "Tut flattens" (the screenplay beat was only implied off screen) and renumbered the old 10.08.026–035 to 027–036; NEG_MODERN_EGYPT on every shot; NEG_PLATE removed from unit shots (it negates the figures, vehicles and animals the shot needs); the Reis carries STATE_R4; Layla's raincoat stays folded as her pillow (dress B in the cutaways).

---

## SCENE 10.01 — EXT. ABANDONED LIMESTONE QUARRY - SUNSET

### 10.01.001 — Quarry, sunset — The tarp comes off   (7 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TAREK and FATHI (small, backs to camera); TUT (small, on a spoil heap); PROP_FARM_TRUCK
- **Action:** Two soldiers haul the dusty tarpaulin off the farm truck; a slight figure stands apart on a spoil heap facing the low sun at frame left.
- **Dialogue:** —
- **Sound:** canvas dragging over grit and metal, wind across the quarry rim, a far-off dog; ambient sound only, no dialogue
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: on the white quarry floor two small soldiers in desert camouflage haul the dusty tarpaulin off the farm truck, while a slight figure in a charcoal hooded jacket stands apart on a spoil heap, facing the sinking sun at frame left. Setting: {LOC_QUARRY.LONG}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}, {GRADE_GOLDEN.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, crowds, modern vehicles, lettering or plates on the truck, night, faces in close detail
- **Refs:** LOC_QUARRY_SUNSET, PROP_FARM_TRUCK, CHAR_TUT_B1_full, CHAR_TAREK_B_full, CHAR_FATHI_B_full
- **Flags:** —
- **Continuity:** Act Three opens on seq_09's quarry, same day. PROP_FARM_TRUCK: TARP → uncovered in this clip. Geography for the whole scene: the sun sets at frame LEFT (west); Tut faces it. Tut B2 at damage L2 (the L3 tears come at 10.4), stick in right hand.

### 10.01.002 — Quarry, sunset — Charges packed like eggs   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI's hands only; PROP_DEMO_CHARGES
- **Action:** On the lowered tailgate, Fathi's hands lift flat charges one at a time and settle them into a hessian feed sack.
- **Dialogue:** —
- **Sound:** hessian rustle, the soft knock of charge against charge, wind
- **PROMPT:** Insert, 100mm macro lens, locked-off: on a wooden tailgate, large dark-brown hands work over {PROP_DEMO_CHARGES.LONG}, {PROP_DEMO_CHARGES.STATE_SACK}, lifting one flat charge at a time and settling it gently among the others. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}. Mood: military exactness, tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable markings on the charges, grenades, sparks, detonation, weapon pointed at the camera
- **Refs:** PROP_DEMO_CHARGES, CHAR_FATHI_B_full, LOC_QUARRY_SUNSET
- **Flags:** —
- **Continuity:** PROP_DEMO_CHARGES → SACK state (10.1). The sack rides in Fathi's satchel into the Serapeum; the charges go into the pit stoppers at 10.06.016.

### 10.01.003 — Quarry, sunset — The notebook buttoned in   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands; PROP_RAMI_NOTEBOOK
- **Action:** Tut's hands slide Rami's cracked notebook inside the front of his jacket and fasten the button over it.
- **Dialogue:** —
- **Sound:** a button through canvas, his breath, wind
- **PROMPT:** Insert, 100mm macro lens, locked-off: slim olive-brown hands, {CHAR_TUT.STATE_TREMOR}, slide {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, inside the front of an oversized charcoal field jacket and fasten the button over it. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable handwriting, legible label, open pages, rings on the fingers
- **Refs:** PROP_RAMI_NOTEBOOK, CHAR_TUT_HANDS, LOC_QUARRY_SUNSET
- **Flags:** COMP
- **Comp:** notebook cover label | Rami's hand-lettered label per file 04 §19.2 (illegible scrawl unless the lead wants it read) | on the cover, in frame for the first 2 s | 0–2 s | notebook art asset
- **Continuity:** Notebook: "buttoned into the jacket (10.1)" (file 01 state table); it stays there until the map case (11.2). Tremor in the RIGHT hand.

### 10.01.004 — Quarry, sunset — "It has gone into the west."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut stands on the spoil heap looking off frame left into the setting sun and speaks.
- **Dialogue:** TUT: "It has gone into the west. The First Hour of twelve."
- **Sound:** wind, the tailgate creaking behind him, distant truck door
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, stands on a spoil heap looking off frame left into the setting sun, its light full on his face, and speaks quietly, one short sentence, then another. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}, {GRADE_GOLDEN.TEXT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, squinting at the lens, sunglasses, sun flare across the face
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_QUARRY_SUNSET
- **Flags:** —
- **Continuity:** Eyeline frame LEFT = west. Jacket buttoned over the notebook; the G1 glow is hidden under the jacket in daylight. Hood down.

### 10.01.005 — Quarry, sunset — "Or it is not."   (7 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** As the sun's last rim slides behind the quarry wall, the gold light drains off Tut's face while he finishes the thought and falls still.
- **Dialogue:** TUT: "The boat goes under the world. At the twelfth hour it is born again. Or it is not."
- **Sound:** wind dropping; the first cold tick of the rock cooling
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, his face three-quarter toward frame left, speaks quietly as the last rim of the sun slides behind the quarry wall and the gold light drains slowly from his cheek, leaving him in blue shadow, then falls still. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, profile view, head turned away, sun disc in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_QUARRY_SUNSET
- **Flags:** —
- **Continuity:** The one light change: sun on → sun gone. From here the quarry is in blue dusk.

### 10.01.006 — Quarry, sunset — "Sunrise is six-fourteen."   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B); PROP_FARM_TRUCK (cab)
- **Action:** Tarek, at the open cab door, looks off frame left up at Tut and states the time.
- **Dialogue:** TAREK: "Sunrise is six-fourteen."
- **Sound:** cab door hinge, wind
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, dust on his sleeves, stands at the open door of a faded pale-blue truck cab, looks off frame left and up toward the young man on the spoil heap, and speaks one short sentence. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, rifle pointed at the camera, readable watch dial
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_FARM_TRUCK, LOC_QUARRY_SUNSET
- **Flags:** —
- **Continuity:** Tarek B at damage L2→L3 (Seq 10–11): rifle slung across the chest, police handset on the vest (dies at 10.04.002), Hassan's ID disc in a pocket. Eyeline frame LEFT and up to Tut.

### 10.01.007 — Quarry, sunset — "The sun has never once been late, Colonel."   (5 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); TAREK (foreground shoulder, no face)
- **Action:** Past Tarek's shoulder, Tut turns his head from the dying sun toward the colonel and answers with a faint dry smile.
- **Dialogue:** TUT: "The sun has never once been late, Colonel."
- **Sound:** wind; Fathi knotting the sack off screen
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past a soldier's out-of-focus black beret and shoulder in the foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_STICK}, turns his head from the dying sun toward camera and speaks one short sentence with a faint dry smile. Setting: {LOC_QUARRY.SHORT}, at sunset. Lighting: {LOC_QUARRY.LIGHT_SUNSET}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TAREK.NEG}, a face on the foreground shoulder, stick in the left hand
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_QUARRY_SUNSET
- **Flags:** —
- **Continuity:** Reverse of 10.01.006 on the same 180° line (Tarek frame right foreground, Tut frame left). Stick in Tut's RIGHT hand (PROP_EBONY_STICK ST2).

## SCENE 10.02 — INT. GEM CONSERVATION CENTRE, MUMMY LAB - DUSK (Nour's captivity)

### 10.02.001 — Mummy lab, dusk — The empty cradle   (6 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C captive look, seated); UNIT_SHABTI ×1 (far back left, by the door); the empty cradle
- **Action:** Nour sits alone on a chair beside the empty titanium cradle, a haze of pale-cyan projector light hanging above it; a shabti stands motionless by the door.
- **Dialogue:** —
- **Sound:** air handling hum, the faint tick of the gantry projectors, no music
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off, from the foot of the empty cradle: a faint haze of pale-cyan projector light hangs over the bare titanium; beside it {CHAR_NOUR.SHORT} sits alone on a chair, hands in her lap; far back left, {UNIT_SHABTI.SHORT} stands perfectly still beside a closed door. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_CAPTIVITY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}, {GRADE_2033_MUSEUM.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_NOUR.NEG}, a figure on the cradle, a sheet over a body, restraints, handcuffs, readable screens
- **Refs:** LOC_GEM_CC/CAPTIVITY_DUSK, CHAR_NOUR_B_full, UNIT_SHABTI, PROP_CUTMAP_PROJECTION
- **Flags:** COMP
- **Comp:** PROP_CUTMAP_PROJECTION | the 1925 cut-map line diagram in pale cyan, the schematic outline drawn around an empty cradle | hovering 40 cm above the titanium | full shot | cut-map asset (file 04 §7b)
- **Continuity:** Geography (file 03 entry 7): glass observation wall frame RIGHT, door back LEFT (the shabti's post). Nour is not restrained. Nour look = wardrobe B at damage L2, face washed (file 01 wardrobe C note: no shawl until the Hall).

### 10.02.002 — Mummy lab, dusk — Drawn around nobody   (5 s)
- **Shot:** Top-down shot, anamorphic 50mm, slow push-in · **Move:** slow push-in
- **In frame:** the empty cradle; projected light (COMP)
- **Action:** Looking straight down on the empty cradle, pale-cyan light lines hovering over nothing.
- **Dialogue:** SESHAT (V.O.): "Seventy-nine percent of Cairo is resting."
- **Sound:** SESHAT's voice, warm and low, from no speaker; projector tick
- **PROMPT:** Top-down shot, anamorphic 50mm lens, slow push-in: an empty low titanium examination cradle on its plinth, its bare padded bed lit from above by a soft wash of pale-cyan projector light, a thin scatter of light lines hovering over nothing. Setting: {LOC_GEM_CC.SHORT}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {NEG_PLATE}, a figure on the cradle, a sheet, readable diagram labels
- **Refs:** LOC_GEM_CC/CAPTIVITY_DUSK, PROP_CUTMAP_PROJECTION
- **Flags:** COMP
- **Comp:** PROP_CUTMAP_PROJECTION | the cut-map diagram, pale cyan, cut lines at every joint, no figure inside it | centred on the cradle, filling 70% of frame | full shot | cut-map asset
- **Continuity:** The cradle has stood empty since Tut left the GEM (4.4). The diagram "still glows, drawn around nobody".

### 10.02.003 — Mummy lab, dusk — "What did the block say, Dr. Kamel?"   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C captive look); PROP_LAYLA_PENDANT
- **Action:** Nour sits upright, reading glasses on, eyes fixed on the empty cradle, listening; she gives nothing.
- **Dialogue:** SESHAT (V.O.): "What did the block say, Dr. Kamel?"
- **Sound:** the voice close and courteous; the room's hush
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, {PROP_LAYLA_PENDANT.SHORT}, {PROP_LAYLA_PENDANT.STATE_STANDARD}, the reading glasses perched on her nose, sits upright with her face washed clean, listening, her eyes fixed on the cradle off frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CAPTIVITY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, dirt on the face, tears, mouth moving, speaking
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, PROP_LAYLA_PENDANT, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** Glasses ON her face here (she takes them off at 10.02.006). Pendant at her throat, lettering never legible. Eyeline frame RIGHT to the cradle; the shabti is off frame LEFT.

### 10.02.004 — Mummy lab, dusk — Reading blind   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's right hand
- **Action:** Nour's thumb moves slowly across the tips of her fingers, the way she read the block blind at Karnak.
- **Dialogue:** —
- **Sound:** skin on skin, almost nothing; the air handling
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's right hand resting on the knee of her black trousers, the thumb moving slowly across the tips of her fingers one by one, as if feeling for carved signs in the dark. Setting: {LOC_GEM_CC.SHORT}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, rings, nail polish, jewellery on the hand
- **Refs:** CHAR_NOUR_B_full, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** Echoes Seq 7 (Nour reading the Karnak block by touch). Sandstone dust in the trouser weave (L2).

### 10.02.005 — Mummy lab, dusk — "So I am asking."   (8 s)
- **Shot:** Medium shot, anamorphic 50mm, slow push-in · **Move:** slow push-in
- **In frame:** UNIT_SHABTI ×1
- **Action:** The shabti stands utterly still by the door, slit steady, facing Nour off frame right, while SESHAT's voice fills the room.
- **Dialogue:** SESHAT (V.O.): "A lector who does not know the rules could void the Weighing. You are the only living person who has read them. So I am asking."
- **Sound:** the voice, unhurried; one faint ceramic tick as nothing moves
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {UNIT_SHABTI.LONG} stands perfectly still beside a closed white door, arms hanging relaxed, palms inward, its amber slit steady, its smooth head turned toward the seated woman off frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CAPTIVITY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people in frame, speaker grille, the robot walking
- **Refs:** UNIT_SHABTI, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** Shabti D0, clean. SESHAT is V.O. (no picture sync); the unit does not brighten here: its slit brightening is saved for "Here am I".

### 10.02.006 — Mummy lab, dusk — "The heart must agree with the one weighed."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C captive look)
- **Action:** Nour takes off her reading glasses, lets them drop on their cord, looks toward the unit off frame left and gives her edited truth.
- **Dialogue:** NOUR: "The heart must agree with the one weighed."
- **Sound:** the glasses' cord settling; her voice level
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_B}, lifts the reading glasses from her face, lets them fall on their cord against her chest, turns her eyes toward the robot off frame left and speaks one short sentence evenly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CAPTIVITY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses thrown, hand over the mouth, head turned more than 45 degrees
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** Glasses now hanging on the cord for the rest of the sequence. Eyeline frame LEFT to the shabti (matches 10.02.005 looking RIGHT).

### 10.02.007 — Mummy lab, dusk — "No. You can't."   (6 s)
- **Shot:** Close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_C captive look)
- **Action:** She hears that SESHAT cannot check the block; the corner of her mouth tightens; she answers two words.
- **Dialogue:** SESHAT (V.O.): "The block is face down in the river. I cannot check it." / NOUR: "No. You can't."
- **Sound:** the voice; a beat of room tone; her two words
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.SHORT} listens with her eyes on the robot off frame left, the faintest tightening at the corner of her mouth, then speaks two quiet words and holds the look. Setting: {LOC_GEM_CC.SHORT}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, smirk, tears, glasses on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** The block went into the Nile at the Karnak quay (7.4). Glasses hanging on the cord.

### 10.02.008 — Mummy lab, dusk — "Certainty: one point zero."   (6 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (seated, mid-ground); UNIT_SHABTI ×1 (by the door); the empty cradle
- **Action:** Across the half-lit lab the shabti turns its head slowly toward Nour and holds; she does not look back.
- **Dialogue:** SESHAT (V.O.): "My heart agrees with me. (beat) Estimate revised. Certainty: one point zero."
- **Sound:** the voice; one ceramic tick with the head turn
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: across the half-lit laboratory, {UNIT_SHABTI.SHORT} by the far door turns its head slowly toward {CHAR_NOUR.SHORT}, seated beside the empty cradle with her hands in her lap, and holds; she keeps her eyes on the cradle. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CAPTIVITY}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_NOUR.NEG}, a figure on the cradle, restraints
- **Refs:** LOC_GEM_CC/CAPTIVITY_DUSK, CHAR_NOUR_B_full, UNIT_SHABTI, PROP_CUTMAP_PROJECTION
- **Flags:** COMP
- **Comp:** PROP_CUTMAP_PROJECTION | the cut-map diagram above the empty cradle, as in 10.02.001 | same placement | full shot | cut-map asset
- **Continuity:** Same set-up axis as 10.02.001, tighter. SESHAT has just "weighed itself": the dramatic irony of the sequence.

### 10.02.009 — Mummy lab, dusk — "There will be a minute for you later."   (6 s)
- **Shot:** Close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; PROP_LAYLA_PENDANT
- **Action:** At "a minute", Nour understands what she is being paid with; her fingers rise and touch the pendant at her throat; her eyes fill.
- **Dialogue:** SESHAT (V.O.): "Thank you, Dr. Kamel. There will be a minute for you later."
- **Sound:** the voice; her breath catching once
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.SHORT}, {PROP_LAYLA_PENDANT.SHORT}, {PROP_LAYLA_PENDANT.STATE_TOUCHED}, hears the voice finish; her fingers rise slowly to the pendant at her throat and her eyes fill, her face otherwise still. Setting: {LOC_GEM_CC.SHORT}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, sobbing, tears streaming, mouth open
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, PROP_LAYLA_PENDANT, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** "A minute" pays off at 10.07 (the Garden). Pendant TOUCHED state; lettering never legible.

### 10.02.010 — Mummy lab, dusk — She sits on her hands   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR's hands and lap
- **Action:** Her hands shake in her lap; she slides them under her thighs and presses down.
- **Dialogue:** —
- **Sound:** fabric; the chair creaks once; room tone swallows it
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, framed on a seated woman's lap and the edge of a steel chair: her hands, sleeves of an olive field jacket grey with dust, tremble against her black trousers; she slides them under her thighs and presses down until they are still. Setting: {LOC_GEM_CC.SHORT}, at dusk. Lighting: {LOC_GEM_CC.LIGHT_DUSK}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, restraints, handcuffs, rings, deformed hands
- **Refs:** CHAR_NOUR_B_full, LOC_GEM_CC/CAPTIVITY_DUSK
- **Flags:** —
- **Continuity:** Right jacket cuff torn (L2). Cut to black stars: 10.03.001.

## SCENE 10.03 — EXT. SAQQARA PLATEAU - NIGHT

### 10.03.001 — Saqqara plateau, night — The Fourth Hour   (7 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** the Step Pyramid, the plateau, SESHAT's floodlights (far)
- **Action:** Hard stars over black desert; the stepped pyramid stands black against them, one flank lit white by distant floodlights. The hour card comes up.
- **Dialogue:** —
- **Sound:** desert wind, a far generator drone, a winch motor grinding somewhere below the horizon; ambient sound only, no dialogue
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: hard stars over black desert; the stepped pyramid stands black against them, one flank washed hard white by floodlights hidden beyond a rise, pale haze drifting in their beams. Setting: {LOC_SAQQARA.LONG}, in the dead of night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, moon, city skyglow, tourists, coloured light on the pyramid, lettering
- **Refs:** LOC_SAQQARA_NIGHT
- **Flags:** COMP
- **Comp:** SUPER / hour card | "THE FOURTH HOUR — THE LAND OF SOKAR" beside the Egyptologist's hieroglyph for "hour" (bible §5; file 05 §13.7) | lower left, small | 1.5 s in → 6.5 s out | hour-card template. [[verify: Amduat hours 4–5, Hornung (04 §6)]] carried from the screenplay.
- **Continuity:** 20:00, 7 Nov (bible §12). No moon in frame; no skyglow (blackout rule, file 03 §0 item 12). Floodlit flank = the Serapeum side.

### 10.03.002 — Saqqara plateau, night — The winch over the bore   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_EXCAVATOR ×2; the gantry winch; floodlight masts
- **Action:** Compressed by the long lens: floodlight masts ring a steel gantry winch over a fresh bore shaft, lit like an oil rig; two excavator units crawl slowly through the glare.
- **Dialogue:** —
- **Sound:** winch motor, track clatter, generator drone flattened by distance
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off: tall floodlight masts ring a steel gantry winch standing over a fresh bore shaft, lit like an oil rig, dust boiling in the beams, while two machines crawl slowly through the glare, each {UNIT_EXCAVATOR.LONG}. Setting: {LOC_SAQQARA.SHORT}, {LOC_SAQQARA.AREA_SERAPEUM_HEAD}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, construction logos, yellow machinery, hazard stripes, workers
- **Refs:** UNIT_EXCAVATOR, LOC_SAQQARA/SERAPEUM_HEAD_NIGHT
- **Flags:** —
- **Continuity:** Two excavators (one is lost to the sand trap at 10.06.004). The winch cable runs down the bore to the pit at the gallery's end (10.06).

### 10.03.003 — Saqqara plateau, night — Three thin red lines   (5 s)
- **Shot:** Medium wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3
- **Action:** On the broad stone stair descending underground, three jackals stand sentry, heads sweeping in slow arcs.
- **Dialogue:** —
- **Sound:** near silence; one faint high servo whisper
- **PROMPT:** Medium wide shot, anamorphic 135mm lens, locked-off: on a broad stone stair descending underground stand three identical sentries, each {UNIT_JACKAL.LONG}, their narrow heads sweeping in slow arcs, three thin red lines floating in the dark between floodlight spills. Setting: {LOC_SAQQARA.SHORT}, {LOC_SAQQARA.AREA_SERAPEUM_HEAD}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, weapon facing camera, muzzle toward the lens, laser beams, red light on the stone
- **Refs:** UNIT_JACKAL, LOC_SAQQARA/SERAPEUM_HEAD_NIGHT
- **Flags:** —
- **Continuity:** Jackals D0 ×3; these three come down the gallery at 10.08 and go into the sand. Weapon modules flush along the spine, pointing across frame.

### 10.03.004 — Saqqara plateau, night — Flat on the ridge   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off, low · **Move:** locked-off
- **In frame:** TAREK, FATHI, YOUSSEF, KARIM, ADAEZE, TUT (from behind, no faces)
- **Action:** Six figures lie flat along a dune crest, seen from behind, looking down at the floodlit dig; one of them, slight and hooded, rests his cheek on the sand.
- **Dialogue:** —
- **Sound:** wind hissing over the crest; the winch below; breathing
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, low behind a dune crest: six figures lie flat along the ridge, seen from behind, four in desert camouflage with rifles laid across their forearms, a tall woman in a navy blazer, and a slight hooded figure in a charcoal jacket, all looking down at hard white floodlight glowing up from beyond the sand. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces toward the camera, rifles pointed at the camera, torches lit, crowds
- **Refs:** CHAR_TAREK_B_full, CHAR_FATHI_B_full, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, CHAR_ADAEZE_B_full, CHAR_TUT_B1_full, LOC_SAQQARA_NIGHT
- **Flags:** —
- **Continuity:** Order along the crest, frame left → right: Tarek, Fathi, Youssef, Karim, Adaeze, Tut. Soldiers in tan helmets (wardrobe A); Tarek in beret. Adaeze carries the conservation kit slung (PROP_CONSERVATION_KIT SLUNG).

### 10.03.005 — Saqqara plateau, night — "We go in where the roof fell."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Lying on the sand, lit from below by the floodlight glow, Tut taps his temple and explains the way in.
- **Dialogue:** TUT (taps his temple): "The priests' old door is blocked by a Persian king's box. We go in where the roof fell."
- **Sound:** wind; his voice low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, lies chin-down on a sand crest, the hood back, taps his temple with two fingers and speaks quietly, his face lit from below by cold white floodlight glow. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, head torch on, face in darkness
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_SAQQARA_NIGHT
- **Flags:** —
- **Continuity:** The G1 glow is pressed into the sand under him (unseen). Hood down (torn only at 10.4).

### 10.03.006 — Saqqara plateau, night — Sokar's land   (8 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut looks out over the plateau and names the hour.
- **Dialogue:** TUT: "Sokar's land. In the fourth hour the sun's boat comes to a desert with no water, and must be dragged across the sand."
- **Sound:** wind carrying sand grains across the crest
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT}, sand grains on his cheek, looks out across the plateau past camera left and speaks quietly and steadily, the cold floodlight glow on his face and hard stars soft behind him. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, moon, profile view
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SAQQARA_NIGHT
- **Flags:** —
- **Continuity:** Eyeline past camera LEFT toward the dig (matches 10.03.004, where the glow is ahead of the party).

### 10.03.007 — Saqqara plateau, night — "By whom?"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze, flat beside Tut, turns her face to him and asks.
- **Dialogue:** ADAEZE: "By whom?"
- **Sound:** wind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, {CHAR_ADAEZE.DMG_L2_BLUE}, a dark headlamp round her neck, lies flat on the sand, turns her face toward the young man off frame right and speaks two words. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp switched on, glasses missing
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_SAQQARA_NIGHT
- **Flags:** —
- **Continuity:** Adaeze B at L2 + blue powder (from 9.2); the headlamp goes on red in the Lesser Vaults. She is at Tut's LEFT on the crest (eyeline frame right).

### 10.03.008 — Saqqara plateau, night — "Whoever is left."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut answers without looking at her, then pushes himself back from the crest out of frame.
- **Dialogue:** TUT: "Whoever is left."
- **Sound:** sand sliding as he moves
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT} keeps his eyes on the floodlit dig past camera left, speaks two quiet words, then pushes himself backward off the crest and slides down out of frame, leaving stars. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face turned to the lens
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SAQQARA_NIGHT
- **Flags:** —
- **Continuity:** Exit to empty stars is the cut point into the Lesser Vaults (10.04.001).

## SCENE 10.04 — INT. SERAPEUM, LESSER VAULTS - NIGHT

### 10.04.001 — Serapeum, Lesser Vaults — Where the roof fell   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the party (small, lamps only; one red headlamp)
- **Action:** Head torches swim in dust as the party clambers down a slope of fallen slabs between bent steel props; one lamp is red.
- **Dialogue:** —
- **Sound:** grit trickling, boots on slabs, a prop creaking under load, breath close in the stone
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: five white head-torch beams and one red swim through drifting dust as small figures clamber down a slope of fallen slabs toward camera left, ducking under bent steel props, the rubble rising almost to the cracked ceiling. Setting: {LOC_SERAPEUM_LESSER.LONG}, at night. Lighting: {LOC_SERAPEUM_LESSER.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces in detail, daylight, electric ceiling lights, torch aimed into the lens
- **Refs:** LOC_SERAPEUM_LESSER_TORCH, CHAR_ADAEZE_B_full, CHAR_TAREK_B_full
- **Flags:** —
- **Continuity:** Adaeze's headlamp now RED (file 01: red in the Serapeum). Everyone else white head torches. Damage from here: dust building to L3.

### 10.04.002 — Serapeum, Lesser Vaults — The handset dies   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TAREK's vest and hand; PROP_POLICE_HANDSET
- **Action:** Tarek's thumb keys the handset on his vest; it hisses once and goes silent.
- **Dialogue:** —
- **Sound:** a hiss of static, then dead air
- **PROMPT:** Insert, 100mm macro lens, locked-off: a thick weathered thumb presses the side key of {PROP_POLICE_HANDSET.LONG}, holds it, then lets go; limestone dust sifts onto the vest in a white head-torch beam. Setting: {LOC_SERAPEUM_LESSER.SHORT}, at night. Lighting: {LOC_SERAPEUM_LESSER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, glowing display, readable screen, brand name, lit indicator
- **Refs:** PROP_POLICE_HANDSET, CHAR_TAREK_B_full, LOC_SERAPEUM_LESSER_TORCH
- **Flags:** —
- **Continuity:** Handset dead from here ("hisses and dies under the stone", file 04 §22.7). SESHAT reaches the party underground only through its units.

### 10.04.003 — Serapeum, Lesser Vaults — Fathi goes first   (5 s)
- **Shot:** Medium shot, anamorphic 24mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi pushes his demolition satchel ahead of him into a crawl-gap between two fallen blocks and squeezes in after it, his torch beam vanishing into the black.
- **Dialogue:** —
- **Sound:** canvas scraping stone, his grunt, a pebble falling a long way
- **PROMPT:** Medium shot, anamorphic 24mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, a white head torch on his brow, pushes his canvas satchel into a low gap between two fallen slabs and squeezes in after it, shoulders first, his beam vanishing into the black. Setting: {LOC_SERAPEUM_LESSER.SHORT}, at night. Lighting: {LOC_SERAPEUM_LESSER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifle pointed at the camera, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_SERAPEUM_LESSER_TORCH
- **Flags:** —
- **Continuity:** Fathi B at L3 (Seq 10–12): the feed sack of charges is in the satchel; red scarf at the neck; bareheaded.

### 10.04.004 — Serapeum, Lesser Vaults — Karim's uncle   (8 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** KARIM (CHAR_KARIM_A3)
- **Action:** Waiting his turn at the gap, Karim looks up at the fractured ceiling and talks, half to himself.
- **Dialogue:** KARIM (in Egyptian Arabic; subtitled): "My uncle guarded this place twenty years. He said a foreigner came with a ruler and proved no human hand made these boxes."
- **Sound:** his low voice bouncing off stone; dust ticking on his helmet
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_KARIM.LONG}, {CHAR_KARIM.WARD_A}, pale dust on the helmet, crouches by the gap with his rifle held across his body, glances up at the cracked ceiling in his own head-torch beam and speaks in Egyptian Arabic, low and quick. Setting: {LOC_SERAPEUM_LESSER.SHORT}, at night. Lighting: {LOC_SERAPEUM_LESSER.LIGHT_TORCH}. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, rifle pointed at the camera, muzzle toward the lens, helmet strap over the mouth
- **Refs:** CHAR_KARIM_A_front, CHAR_KARIM_A_34, CHAR_KARIM_A_full, LOC_SERAPEUM_LESSER_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "My uncle guarded this place twenty years. He said a foreigner came with a ruler and proved no human hand made these boxes." | lower third, two lines max (file 05 §13.7) | line in → out | seq 10 subtitle file
- **Continuity:** Karim A (tan helmet, chin strap open), damage L3 (dust). His last spoken lines are here and at 10.08. Sets up Tut's answer at 10.05.010.

### 10.04.005 — Serapeum, Lesser Vaults — "Your uncle said a lot of things."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** YOUSSEF (CHAR_YOUSSEF_A3)
- **Action:** Youssef, behind Karim, answers flatly without looking up from the gap.
- **Dialogue:** YOUSSEF (in Egyptian Arabic; subtitled): "Your uncle said a lot of things."
- **Sound:** a snort; Fathi's scrape ahead
- **PROMPT:** Medium close-up, anamorphic 50mm lens, subtle handheld: {CHAR_YOUSSEF.LONG}, {CHAR_YOUSSEF.WARD_A}, pale dust in his stubble, keeps his eyes on the crawl-gap off frame left and speaks in Egyptian Arabic, flat and dry, one corner of his mouth lifting. Setting: {LOC_SERAPEUM_LESSER.SHORT}, at night. Lighting: {LOC_SERAPEUM_LESSER.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_YOUSSEF.NEG}, rifle pointed at the camera, beard
- **Refs:** CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_34, CHAR_YOUSSEF_A_full, LOC_SERAPEUM_LESSER_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "Your uncle said a lot of things." | lower third | line in → out | seq 10 subtitle file
- **Continuity:** Youssef A (tan helmet), L3 dust, scar through the RIGHT eyebrow.

## SCENE 10.05 — INT. SERAPEUM, GREATER VAULTS - CONTINUOUS

### 10.05.001 — Serapeum, Greater Vaults — The gallery   (7 s)
- **Shot:** Extreme wide establishing shot, anamorphic 24mm, locked-off · **Move:** locked-off
- **In frame:** the party (small, frame left, lamps); the gallery; far floodlight
- **Action:** The dead-straight gallery runs away beyond any headlamp; far off at its end, floodlight falls down a shaft. The party steps in at frame left.
- **Dialogue:** —
- **Sound:** the room's enormous hush; a far winch hum; boots; the echo arriving late
- **PROMPT:** Extreme wide establishing shot, anamorphic 24mm lens, locked-off, down the axis: the dead-straight gallery runs away far beyond any head torch; at its distant end a column of hard white floodlight falls down a shaft, and in the near dark at frame left six small figures step in, their head-torch beams sliding over polished stone. Setting: {LOC_SERAPEUM_GREATER.LONG}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}, {GRADE_UNDERGROUND.TEXT}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces in detail, tourists, electric wall lamps, readable signs
- **Refs:** LOC_SERAPEUM_GREATER_WORKLIGHTS, CHAR_TAREK_B_full, CHAR_ADAEZE_B_full, CHAR_TUT_B1_full
- **Flags:** —
- **Continuity:** Geography lock (file 03 entry 41): we enter from the Lesser Vaults end (frame LEFT in laterals) and look down the gallery to the lit pit. The service-tunnel door is on the RIGHT-hand wall near the pit.

### 10.05.002 — Serapeum, Greater Vaults — The thread and the nodes   (4 s)
- **Shot:** Insert, 100mm macro, low, rack focus · **Move:** rack focus from the near node to the far nodes
- **In frame:** UNIT_THREAD; UNIT_RELAY nodes
- **Action:** At floor level, a hair-fine fibre runs along the stone; a small black relay node winks white; focus racks down the gallery to more nodes winking at twenty-metre intervals.
- **Dialogue:** —
- **Sound:** a faint electronic tick with each wink
- **PROMPT:** Insert, 100mm macro lens, at floor level, rack focus from near to far: {UNIT_THREAD.SHORT}, and beside it {UNIT_RELAY.STATE_NODE}; the focus slides down the gallery to more tiny white winks spaced far apart along the floor, fading into the dark. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, thick cable, glowing fibre, coloured light on the thread
- **Refs:** UNIT_THREAD, UNIT_RELAY, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** "SESHAT's fibre-optic thread, a relay node winking white every twenty metres." The thread has no light of its own; only the node winks (cool white).

### 10.05.003 — Serapeum, Greater Vaults — Mourners at a wake   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, lateral tracking right · **Move:** lateral tracking right, at walking pace
- **In frame:** the party (mid-ground, rifles up); UNIT_SHABTI ×6 hero + dozens (VFX-EXTEND); colossal boxes
- **Action:** Tracking with the party down the axis; in the side-chamber mouths between the boxes stand shabti, motionless, like mourners.
- **Dialogue:** —
- **Sound:** boots on the timber walkway; rifles' slings creaking; no ticks: the units do not move
- **PROMPT:** Wide shot, anamorphic 35mm lens, lateral tracking right at walking pace alongside six figures moving down the gallery, four with rifles raised across their bodies, head torches sweeping; between the colossal boxes, lids shoved askew, dozens of identical robots, each {UNIT_SHABTI.SHORT}, wait perfectly still in every side-chamber mouth, standing in silent rows receding into the dark. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, rifles pointed at the camera, robots moving, faces toward the lens
- **Refs:** LOC_SERAPEUM_GREATER_TORCH, UNIT_SHABTI, CHAR_TAREK_B_full, CHAR_FATHI_B_full, CHAR_YOUSSEF_A_full
- **Flags:** VFX-EXTEND
- **Continuity:** Direction of travel: left → right = toward the pit. 6 hero shabti in camera; extend to "dozens" from the 3D asset; deliver a clean plate. Shabti D1 (dusty) optional; their positions are locked for 10.08.032 ("exactly where they stood").

### 10.05.004 — Serapeum, Greater Vaults — "Here am I."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×1 (hero); a passing head-torch beam
- **Action:** As a torch beam passes over it, the first shabti lifts its head slightly; its amber light-slit brightens once.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Here am I."
- **Sound:** the voice soft, from inside the chest; one ceramic tick
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG} stands between two colossal granite boxes as a white torch beam slides across its shell; it lifts its head slightly and its amber light-slit brightens once, then settles. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people in frame, mouth, speaker grille, robot walking
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** COMP
- **Comp:** slit brightening | swell on "Here", peak on "am", decay by "I" (file 05 §9.8), amber #FFA93A | the slit | timed to the recorded line | SESHAT voice track
- **Continuity:** The acknowledgment phrase verbatim (file 02 §0.4).

### 10.05.005 — Serapeum, Greater Vaults — The register   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off, down the axis · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×6 hero + dozens (VFX-EXTEND)
- **Action:** One after another down the gallery, amber slits brighten and settle: a wave of light and soft voices rolls away into the dark, and dies.
- **Dialogue:** SHABTI (SESHAT'S VOICE), receding: "Here am I… Here am I… Here am I…"
- **Sound:** the voice repeating, each fainter and further, overlapping, then silence
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, down the length of the gallery: one after another, the amber light-slits of dozens of identical robots standing in silent rows receding into the dark, each {UNIT_SHABTI.SHORT}, brighten once and settle, a wave of amber rolling away from camera toward the far floodlight, then everything still. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, robots moving, flashing lights, strobing
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-EXTEND, COMP
- **Comp:** slit wave | each slit's single swell, staggered 0.25 s per unit receding, amber #FFA93A | down the axis | 0.5–6 s | SESHAT voice layered
- **Continuity:** Locked-off for the extension; clean plate required.

### 10.05.006 — Serapeum, Greater Vaults — "What was that?"   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek, rifle up across his chest, swings his head-torch beam down the gallery and asks.
- **Dialogue:** TAREK: "What was that?"
- **Sound:** the last echo dying
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, stone dust on his shoulders and beret, holds his rifle across his chest with the muzzle pointing off frame right, his head-torch beam following the fading echo down the gallery, and speaks one short sentence. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, muzzle toward the lens, torch shining into the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Tarek B at L3 from here (dust); dead handset on the vest.

### 10.05.007 — Serapeum, Greater Vaults — "It's taking the register."   (5 s)
- **Shot:** Two-shot, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B3), YOUSSEF (CHAR_YOUSSEF_A3)
- **Action:** Adaeze answers Tarek; Youssef, beside her, cracks back without lowering his rifle.
- **Dialogue:** ADAEZE: "It's taking the register." / YOUSSEF: "Tell it we're all present."
- **Sound:** a nervous breath of a laugh from Youssef
- **PROMPT:** Two-shot, anamorphic 50mm lens, subtle handheld: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L3}, a red headlamp on her brow, speaks one short sentence toward frame left; beside her {CHAR_YOUSSEF.SHORT}, {CHAR_YOUSSEF.WARD_A}, rifle held across his body, answers with one dry sentence of his own. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_YOUSSEF.NEG}, muzzle toward the lens
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Adaeze L3 from here (blue powder still on her fingers and blazer front). Kit slung on her shoulder.

### 10.05.008 — Serapeum, Greater Vaults — The red box   (6 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); the red granite box
- **Action:** Tut steps to the rim of a side chamber and lays his palm on the red granite box, panelled with faint green-tinted columns of worn relief, and speaks.
- **Dialogue:** TUT: "Amasis. A king nearly eight hundred years after me."
- **Sound:** his palm on polished stone; a faint crystalline ring from the chest
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_STICK}, {CHAR_TUT.STATE_DAGGER_BELT}, lays his left palm flat on the polished flank of a colossal box and speaks quietly, his face lit by a passing head torch. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_RED_BOX}, weathered, illegible low relief, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, readable hieroglyphs, crisp carved text, sharp inscriptions
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_SERAPEUM_GREATER/RED_BOX_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 per file 01 (warm amber-gold through yellow-green, slow pulse) | the centre of the tunic | full shot | glow element
- **Continuity:** Stick in the RIGHT hand, left palm on the box. G1 glow faint through the tunic where the jacket hangs open (the notebook button holds the jacket at the waist).

### 10.05.009 — Serapeum, Greater Vaults — Palm on the relief   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's left hand; red granite
- **Action:** His fingertips move slowly down a worn column of green-tinted relief on the red granite.
- **Dialogue:** —
- **Sound:** skin on polished stone
- **PROMPT:** Insert, 100mm macro lens, locked-off: slim olive-brown fingers, {CHAR_TUT.STATE_WRIST_CRACK}, move slowly down a worn column of weathered, illegible low relief faintly tinted green on polished red granite, a white torch beam raking across it. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_RED_BOX}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable hieroglyphs, crisp carved signs, extra fingers
- **Refs:** CHAR_TUT_HANDS, LOC_SERAPEUM_GREATER/RED_BOX_TORCH
- **Flags:** —
- **Continuity:** LEFT wrist seam already cracked (9.4). The relief is never legible (file 03 §0 item 7).

### 10.05.010 — Serapeum, Greater Vaults — "The flatness is ours."   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut turns his head to Karim, off frame right, and answers the uncle's story.
- **Dialogue:** TUT (to Karim): "Your uncle's foreigner measured with a ruler and a lamp. Copper saws, quartz sand and patience did this. The flatness is ours."
- **Sound:** his voice close; the gallery answering softly
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, his hand still on the red granite, turns his head toward the young soldier off frame right and speaks steadily, a little proud, in a warm head-torch spill. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, profile view
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/RED_BOX_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 | lower frame edge | full shot | glow element
- **Continuity:** Eyeline frame RIGHT to Karim (off screen, at the next box).

### 10.05.011 — Serapeum, Greater Vaults — "For bulls."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Tut gives the figure; Adaeze, at his shoulder, answers dryly.
- **Dialogue:** TUT: "A stela says twenty-eight working days to bring one in." / ADAEZE: "For bulls."
- **Sound:** a dry beat between them
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, beside the red granite box, speaks one sentence; at his shoulder {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, a red headlamp on her brow, raises her eyebrows and answers with two words. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_RED_BOX}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, readable hieroglyphs
- **Refs:** CHAR_TUT_A0_34, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER/RED_BOX_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 | Tut's tunic | full shot | glow element
- **Continuity:** Adaeze frame right of Tut throughout the gallery and pit scenes.

### 10.05.012 — Serapeum, Greater Vaults — "A piece of the hidden god"   (6 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut repeats her words, taps his temple, and the joke goes out of his face.
- **Dialogue:** TUT: "For bulls." (taps his temple) "And with every bull, a piece of the hidden god went into the granite."
- **Sound:** a low glass hum under the room tone, barely there
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT} repeats two words with a small smile, taps his temple with two fingers, and speaks on quietly as the smile goes out of his face, his very dark eyes on the long row of boxes past camera right. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, profile view
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Eyeline frame RIGHT = down the gallery toward the pit.

### 10.05.013 — Serapeum, Greater Vaults — "So it could never be whole again."   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back, foreground left); the gallery and boxes receding; far floodlight
- **Action:** Over Tut's shoulder, the boxes recede chamber after chamber toward the lit pit as he finishes.
- **Dialogue:** TUT: "Box by box, for five hundred years, so it could never be whole again."
- **Sound:** his voice travelling away down the stone
- **PROMPT:** Over-the-shoulder shot, anamorphic 35mm lens, locked-off: past the shaved head and charcoal-jacketed shoulder of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_SCAR}, in the left foreground, the colossal dark boxes recede chamber after chamber down the gallery toward the far column of floodlight, silent white robots standing between them. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, face toward the camera
- **Refs:** CHAR_TUT_B_night_34, LOC_SERAPEUM_GREATER_WORKLIGHTS, UNIT_SHABTI
- **Flags:** VFX-EXTEND
- **Continuity:** Line delivered with his back to camera (no sync). Hood down: the nape SCAR (6.2 →) shows, never the port. Extend the shabti rows and boxes to the far end in post.

## SCENE 10.06 — INT. SERAPEUM, GREATER VAULTS - THE PIT - CONTINUOUS

### 10.06.001 — Serapeum, the pit — The pit and its stoppers   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, locked-off, from behind the last box · **Move:** locked-off
- **In frame:** the party (backs and helmets, foreground, behind the last box); the pit; the winch cable; UNIT_EXCAVATOR ×2 (far)
- **Action:** From behind the last box, the party watches floodlight drop down the shaft onto a pit five metres across, six round stone stoppers set in its walls; a winch cable hangs taut into the dark.
- **Dialogue:** —
- **Sound:** the winch motor grinding far above; sand hissing; the party's breath
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off, low behind the dark edge of a colossal granite box: helmeted heads and shoulders in the foreground watch hard white floodlight pour down a shaft onto a round pit five metres across, six round stone stoppers set into its walls like the bungs of great jars, a taut steel cable hanging into the dark. Setting: {LOC_SERAPEUM_GREATER.LONG}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, faces toward the camera, modern signage, safety tape with lettering, workers in hard hats
- **Refs:** LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full
- **Flags:** —
- **Continuity:** The pit at the gallery's far end; the service-tunnel door is on the RIGHT-hand wall beyond it (10.06.016). Six stoppers now; one splits at 10.06.003, leaving five.

### 10.06.002 — Serapeum, the pit — The casket comes up   (5 s)
- **Shot:** Medium wide shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_EXCAVATOR ×2; PROP_CASKET_NEST (closed stone casket)
- **Action:** Two excavator units steady a closed stone casket with their grippers as the winch draws it up out of the dark, streaming sand.
- **Dialogue:** —
- **Sound:** cable singing under load, sand pouring off stone, servo whine
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: a closed rough grey granite chest about a metre long, {PROP_CASKET_NEST.STATE_WINCHED}, rises slowly into the light between two machines on the rim, each {UNIT_EXCAVATOR.SHORT}. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, yellow machinery, hazard stripes, lettering on the chest, open lid
- **Refs:** PROP_CASKET_NEST, UNIT_EXCAVATOR, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** PROP_CASKET_NEST WINCHED state. Excavator A (nearer, frame left) is lost at 10.06.004; excavator B (frame right) survives.

### 10.06.003 — Serapeum, the pit — A crack like a rifle   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** one stone stopper in the pit wall
- **Action:** A round stone stopper set in the pit wall splits across with a sharp crack; a thin jet of sand spits from the break.
- **Dialogue:** —
- **Sound:** a crack like a rifle report, echoing down the gallery
- **PROMPT:** Insert, 100mm macro lens, locked-off: a round ancient stone stopper, the size of a cartwheel hub, set flush in a rough limestone pit wall, splits across with a sudden crack, and a thin hard jet of pale sand spits from the break. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, fire, sparks, smoke, explosion flash
- **Refs:** LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** VFX-ASSIST
- **Continuity:** Deliver before/after plates of the stopper (intact / split) at the same framing. The tripwire ("Bostrom, 2014" / "Older").

### 10.06.004 — Serapeum, the pit — The sand takes the excavator   (5 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_EXCAVATOR A; the sand torrent; the casket on its cable (upper frame)
- **Action:** Sand bursts from the pit wall in a solid torrent; the nearer excavator slides, tips and goes down into the funnel.
- **Dialogue:** —
- **Sound:** a roar like a broken water main; tracks scrabbling; a metallic groan swallowed
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: a solid torrent of pale sand bursts from the pit wall and pours across the floor; {UNIT_EXCAVATOR.LONG}, {UNIT_EXCAVATOR.STATE_BURIED}, slides sideways on the moving rim, tips, and goes down into the swirling funnel. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_SAND_TRAP}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people near the pit, water, mud, fire, explosion
- **Refs:** UNIT_EXCAVATOR, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** VFX-ASSIST
- **Continuity:** No human near the pit (screenplay; file 05 §7.2). Sand as VFX-ASSIST: deliver the take plus before/after plates. SAND_TRAP state on; the funnel stays open through 10.06.

### 10.06.005 — Serapeum, the pit — The light goes out; the casket holds   (5 s)
- **Shot:** High-angle shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** the funnel of sand; the buried excavator's red line; the casket swinging (top of frame)
- **Action:** Looking down into the moving sand, the buried machine's red line glows up through it, dims and goes out; the casket, swinging on its cable at the top of frame, holds.
- **Dialogue:** —
- **Sound:** sand hiss settling; the cable creaking as the casket swings
- **PROMPT:** High-angle shot, anamorphic 40mm lens, locked-off, looking down into a slow funnel of moving pale sand: a thin red light line glows up through the grains, dims, and goes out, while at the top of frame a rough grey granite chest swings gently on its steel cable and steadies. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, people in the sand, hands in the sand, water
- **Refs:** UNIT_EXCAVATOR, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** VFX-ASSIST
- **Continuity:** Rhymes with the jackals' red lines going out in the sand at 10.08.029. The only light change: the red line out.

### 10.06.006 — Serapeum, the pit — "A tripwire." / "Older."   (5 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3), TUT (CHAR_TUT_B2), behind the last box
- **Action:** Crouched behind the box, Adaeze names it; Tut corrects her with one word.
- **Dialogue:** ADAEZE: "A tripwire. Bostrom, 2014." / TUT: "Older."
- **Sound:** the last sand trickling; their whispers
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: behind the edge of a dark granite box, {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L3}, a red headlamp on her brow, whispers one quick sentence, eyes on the pit off frame left; beside her {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, answers with a single quiet word. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_ADAEZE.NEG}, {CHAR_TUT.NEG}, faces touching
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, CHAR_TUT_A0_34, CHAR_TUT_B_night_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1 | Tut's tunic | full shot | glow element
- **Continuity:** Eyelines frame LEFT to the pit for the whole party-behind-the-box coverage. Adaeze frame left of Tut in this set-up.

### 10.06.007 — Serapeum, the pit — "Five more."   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi's finger moves stopper to stopper around the pit as he counts under his breath.
- **Dialogue:** FATHI (counting stoppers): "Five more."
- **Sound:** his murmured count
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, crouched behind a granite box, points one finger slowly from stopper to stopper around the pit off frame left, lips moving as he counts, then speaks two words. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifle pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Five intact stoppers remain; they take the five charges at 10.06.016 and fire at 10.08.027.

### 10.06.008 — Serapeum, the pit — "They guarded the last one with it."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut, watching the settling sand, explains.
- **Dialogue:** TUT: "They lowered the boxes on sand. They guarded the last one with it."
- **Sound:** sand ticking down
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, his eyes on the settling sand off frame left, speaks two quiet sentences, the floodlight hard on one side of his face. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1 | lower frame | full shot | glow element
- **Continuity:** Sets up "Sand between the parts" (10.08.031).

### 10.06.009 — Serapeum, the pit — The seals cut   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_EXCAVATOR B; PROP_CASKET_NEST
- **Action:** The surviving excavator sets the casket down on the lip and runs its gripper along the resin seal of the lid, cutting it.
- **Dialogue:** —
- **Sound:** stone set on stone; a thin rasp of resin parting
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {UNIT_EXCAVATOR.SHORT}, pale sand streaming off its tracks, sets a rough grey granite chest down on the lip of the pit and draws the tip of its gripper slowly along the black resin seal under the lid, parting it. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, sparks, cutting disc, lettering on the chest
- **Refs:** UNIT_EXCAVATOR, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Casket now on the NEAR lip (the party's side), where it stays for the fight (Adaeze beside it at 10.08.007).

### 10.06.010 — Serapeum, the pit — Bronze, then sycamore   (4 s)
- **Shot:** Top-down insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_CASKET_NEST; the gripper
- **Action:** Looking straight down: the gripper lifts away a green-corroded bronze lid, revealing blackened wood beneath.
- **Dialogue:** —
- **Sound:** corroded metal unsticking; dust puff
- **PROMPT:** Top-down insert, 100mm macro lens, locked-off: inside an open rough grey granite chest on the lip of a rock pit, a black robotic gripper lifts a green-corroded bronze lid slowly out of frame, revealing the closed lid of a blackened sycamore box inside, dust puffing off the edges. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, readable inscriptions, modern packaging
- **Refs:** PROP_CASKET_NEST, UNIT_EXCAVATOR, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Written without the PROP_CASKET_NEST lock on purpose: its LONG and SHORT describe the fully opened nest with the kit showing, the end state of 10.06.011. "bronze gone green; inside that, sycamore gone black; inside that, gold." Continues directly into 10.06.011.

### 10.06.011 — Serapeum, the pit — The Fifth Hour: the serpent of glass   (6 s)
- **Shot:** Top-down insert, 100mm macro, slow push-in · **Move:** slow push-in
- **In frame:** UNIT_GLASS_SERPENT in the gold box; PROP_CASKET_NEST
- **Action:** The blackened sycamore lid lifts away; inside the dull gold lies a serpent of green glass looped three times, light moving slowly deep inside it like breath.
- **Dialogue:** —
- **Sound:** a faint crystalline ringing as the air reaches it; the hour card's low tone
- **PROMPT:** Top-down insert, 100mm macro lens, slow push-in: a blackened wooden lid lifts out of frame and, bedded in pale sand inside a dull gilded box, lies {UNIT_GLASS_SERPENT.LONG}, {UNIT_GLASS_SERPENT.STATE_S1}, a crude black wax serpent laid along its back and a pale papyrus band binding its coils. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, living snake, scales, eyes on the serpent, readable writing, red-brown wax, cedar
- **Refs:** UNIT_GLASS_SERPENT, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP, EXTEND:10.06.010
- **Comp:** SUPER / hour card | "THE FIFTH HOUR — THE BOAT BECOMES A SERPENT" with the Egyptologist's "hour" sign | lower left | 2–6.5 s | hour-card template. Also: papyrus band ink | one name over and over in red hieratic, illegible (Egyptologist) | on the band | full shot | glyph asset
- **Continuity:** EXTEND of 10.06.010's last frame (same top-down framing). Serpent state S1 ("Deep inside it, light moves slowly, like breath" — the screenplay wins over file 02's S0 "dormant in the pit"; flag to the lead). Wax serpent BLACK (file 02 §12; the REF B "red-brown" wording is superseded). Box nest: granite → bronze → sycamore → gold.

### 10.06.012 — Serapeum, the pit — "The ninth core."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze stares at the glass, green light moving in her glasses, and names it.
- **Dialogue:** ADAEZE: "The ninth core."
- **Sound:** glass hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, a faint green glow moving in the lenses of her glasses, stares past camera left at the open box and speaks three quiet words. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Eyeline frame LEFT to the casket on the lip.

### 10.06.013 — Serapeum, the pit — The claw withdraws   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_EXCAVATOR B's claw; the open gold box
- **Action:** The excavator's claw, built for rock, hovers over the glass, then draws back.
- **Dialogue:** —
- **Sound:** a servo whine rising, stopping, reversing
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: the careful three-fingered gripper of {UNIT_EXCAVATOR.SHORT} lowers over the open gilded box and hovers a hand's width above the coiled green glass, holds, then draws slowly back up out of frame. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, gripper touching the glass, sparks
- **Refs:** UNIT_EXCAVATOR, UNIT_GLASS_SERPENT, PROP_CASKET_NEST
- **Flags:** —
- **Continuity:** The excavator declines the kit (file 02 §14.2); it takes no further action in the scene.

### 10.06.014 — Serapeum, the pit — A statue of reaching   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the "reaching" unit); the open gold box
- **Action:** A shabti steps out of the ranks, walks to the casket and reaches into the gold; its long fingers touch the papyrus band, and it stops dead, its slit holding steady.
- **Dialogue:** —
- **Sound:** two ceramic ticks, then nothing
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG} takes two smooth, unhurried steps from the ranks to the open gilded box on the pit's lip and reaches in; its long fingers touch the papyrus band around the green glass and it stops dead, frozen mid-reach, its amber slit holding steady. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, robot lifting the serpent, robot shaking
- **Refs:** UNIT_SHABTI, UNIT_GLASS_SERPENT, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** "The amber slit holds": the slit stays steady, not the 8.4 ember (the screenplay wins over file 02 STATE_HALTED). It holds the reach until 10.06.036; once Adaeze lowers the gold lid (10.06.017) its hand rests just above the lid, same arm and body pose (10.06.029).

### 10.06.015 — Serapeum, the pit — "The only hands in here that can."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3), ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Fathi asks the obvious; Adaeze, eyes on the frozen unit, answers.
- **Dialogue:** FATHI: "Then why are we still breathing?" / ADAEZE: "Because we're the only hands in here that can."
- **Sound:** a long exhale from Fathi
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, speaks one low sentence toward the woman beside him; {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, her red headlamp on, keeps her eyes on the frozen robot off frame left and answers with one sentence. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_ADAEZE.NEG}, rifle pointed at the camera
- **Refs:** CHAR_FATHI_A_34, CHAR_FATHI_B_full, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Eyelines frame LEFT to the pit.

### 10.06.016 — Serapeum, the pit — Charges in the stoppers   (5 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** FATHI; YOUSSEF and KARIM (background, at the last two boxes); PROP_DEMO_CHARGES; the service-tunnel doorway (frame right)
- **Action:** Fathi presses a charge into a stopper and pays out thin wire as he backs round the pit toward a low doorway in the right-hand wall; beyond, Youssef and Karim take up positions at the last two boxes, rifles on the long dark.
- **Dialogue:** —
- **Sound:** wire spool ticking, tape tearing, boots on sand
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_FATHI.SHORT} tapes a flat olive-drab charge the size of a paperback to a round stone stopper in the pit wall, {PROP_DEMO_CHARGES.STATE_TAPED}, then backs round the rim paying out thin wire toward a low dark doorway at frame right; behind him two helmeted soldiers kneel at the last two granite boxes, rifles held across their bodies toward the dark gallery. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, rifles pointed at the camera, explosion, readable markings
- **Refs:** CHAR_FATHI_B_full, CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, PROP_DEMO_CHARGES, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Five charges, one per remaining stopper; wire runs round the pit to the SERVICE TUNNEL doorway on the RIGHT-hand wall. Youssef and Karim now at the last two boxes facing up-gallery (toward the main stair).

### 10.06.017 — Serapeum, the pit — Plan A: the lid pressed shut   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** ADAEZE's hands; PROP_CASKET_NEST
- **Action:** Adaeze lowers the gold lid and presses the broken resin seal shut with her palm.
- **Dialogue:** —
- **Sound:** gold on gold; her breath held
- **PROMPT:** Insert, 100mm macro lens, locked-off: a deep-brown hand with vivid blue powder in its creases lowers a dull gilded lid onto its box and presses flat along the broken black resin seal, {PROP_CASKET_NEST.STATE_LID}. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, rings, nail polish, deformed hands
- **Refs:** PROP_CASKET_NEST, CHAR_ADAEZE_B_full
- **Flags:** —
- **Continuity:** Casket LID state (her palm on it) through 10.06.030. The frozen shabti's hand is withdrawn to just above the lid (lock its pose in the plate).

### 10.06.018 — Serapeum, the pit — "At sunrise I act, weighed or not."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (second unit, at the pit's edge)
- **Action:** At the pit's edge a second shabti turns its head toward Adaeze; its slit brightens as SESHAT speaks through it.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Bury it if you like. The Garden does not require me to ascend. At sunrise I act, weighed or not."
- **Sound:** the voice from inside the chest, warm, low, unhurried
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, standing at the edge of the pit, turns its head slowly toward camera right and holds, its amber light-slit brightening and settling in a slow rhythm as if speaking. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, mouth, speaker grille, robot gesturing
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** slit modulation | amber #FFA93A, a soft swell on each stressed word, never a lip-sync | the slit | timed to SESHAT's recorded line | voice track
- **Continuity:** Unit 2 is dusty (D1) to tell it from the frozen reacher (D0). Eyeline frame RIGHT to Adaeze at the casket.

### 10.06.019 — Serapeum, the pit — "From the scale, or from myself."   (7 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off (continuing)
- **In frame:** UNIT_SHABTI (second unit)
- **Action:** The same unit holds its gaze and finishes; its slit settles to steady.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "I asked the gods for a verdict. At sunrise I will have one: from the scale, or from myself."
- **Sound:** the voice; the winch creaking far above
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, stands perfectly still at the pit's edge, head turned toward camera right, its amber light-slit swelling softly on a slow rhythm, then settling to a steady glow. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, mouth, robot gesturing
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP, EXTEND:10.06.018
- **Comp:** slit modulation | as 10.06.018 | the slit | timed to the line | voice track
- **Continuity:** EXTEND child of 10.06.018 (same framing, same take); cut away to 10.06.020 on the join if it drifts.

### 10.06.020 — Serapeum, the pit — His hand over hers   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** ADAEZE's hand on the lid; TUT's hand
- **Action:** Adaeze keeps pressing the lid; Tut's slim hand, trembling faintly, closes over hers.
- **Dialogue:** —
- **Sound:** a small breath; the glass hum under the lid
- **PROMPT:** Insert, 100mm macro lens, locked-off: a deep-brown hand dusted with vivid blue powder presses flat on a dull gilded lid; a slim olive-brown right hand with a thin gold seam ring at the wrist, {CHAR_TUT.STATE_TREMOR}, settles over it and closes gently. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, extra fingers, fused fingers, rings
- **Refs:** CHAR_TUT_HANDS, CHAR_ADAEZE_B_full, PROP_CASKET_NEST
- **Flags:** —
- **Continuity:** Tut's RIGHT hand (the tremor hand) over her right hand; the left wrist seam (cracked) is off frame.

### 10.06.021 — Serapeum, the pit — "It never changes."   (5 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), ADAEZE (CHAR_ADAEZE_B3), kneeling at the casket
- **Action:** Kneeling across the casket from her, Tut speaks gently; Adaeze does not lift her hand.
- **Dialogue:** TUT: "If you bury it, it never changes. And at sunrise it acts anyway."
- **Sound:** their breath; the glass hum
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, kneels at the gilded box on the pit's lip, his hand over the hand of {CHAR_ADAEZE.SHORT}, and speaks two gentle sentences to her; she keeps pressing the lid, jaw set, eyes on him. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, faces touching
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B_night_34, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1 | Tut's tunic | full shot | glow element
- **Continuity:** New axis for the argument: Tut frame LEFT, Adaeze frame RIGHT, casket between them; hold this line to 10.06.031.

### 10.06.022 — Serapeum, the pit — "Then what?"   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze looks at him hard and asks.
- **Dialogue:** ADAEZE: "Then what?"
- **Sound:** —
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, the red headlamp pushed up on her brow, looks hard at the young man off frame left and speaks two words. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, headlamp shining into the lens
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Eyeline frame LEFT to Tut.

### 10.06.023 — Serapeum, the pit — "By a heart that can say no."   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut answers, simply.
- **Dialogue:** TUT: "Then it must be weighed. By a heart that can say no."
- **Sound:** the glass hum rising faintly
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, his very dark eyes steady on the woman off frame right, speaks two simple sentences quietly and plainly. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Eyeline frame RIGHT to Adaeze.

### 10.06.024 — Serapeum, the pit — Everyone looks at the glow   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2), the foreground shoulders of TAREK and FATHI (no faces)
- **Action:** Between two soldiers' shoulders, Tut kneels in the floodlight; the soft glow at the centre of his chest is what everyone is looking at.
- **Dialogue:** —
- **Sound:** a slow glass heartbeat under everything
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow push-in between two soldiers' out-of-focus shoulders: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_G1}, kneels beside the gilded box and lowers his eyes to his own chest, the jacket hanging open. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}, and the soft chest glow as the warmest light in frame. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, open chest, skin showing at the chest, faces on the foreground shoulders
- **Refs:** CHAR_TUT_B_night_34, CHAR_TUT_B1_full, CHAR_TAREK_B_full, CHAR_FATHI_B_full, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1, warm amber-gold through yellow-green, one slow pulse | centre of the tunic | full shot | glow element
- **Continuity:** Remains rule: the vessel is never seen; only the light through the tunic (file 05 §7.3).

### 10.06.025 — Serapeum, the pit — "Take mine."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi says it without hesitation.
- **Dialogue:** FATHI: "Take mine."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, looks down at the kneeling young man off frame left and speaks two words, simply, calm warm eyes unwavering. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, scarf over the mouth
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Fathi standing (Tut kneeling): eyeline frame LEFT and down. Plants 10.10 ("carry me out into the sun").

### 10.06.026 — Serapeum, the pit — "Only the dead can put a heart in glass."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut looks up at Fathi with great fondness and refuses.
- **Dialogue:** TUT: "Yours is not in glass. Only the dead can put a heart in glass."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, looks up at the tall soldier off frame right with great fondness and speaks two quiet sentences. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1 | lower frame | full shot | glow element
- **Continuity:** Eyeline frame RIGHT and up to Fathi.

### 10.06.027 — Serapeum, the pit — "You'll die."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze understands and says it flat.
- **Dialogue:** ADAEZE: "You'll die."
- **Sound:** —
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, the faint worry line between her brows deepening, looks at the young man off frame left and says two flat words, her eyes wet behind round glasses. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, tears streaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Her palm still on the lid (below frame).

### 10.06.028 — Serapeum, the pit — "The waiting was the bad part."   (6 s)
- **Shot:** Close-up, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut smiles, small and dry, and answers her.
- **Dialogue:** TUT: "I have done it before. It was not so bad. The waiting was the bad part."
- **Sound:** the glass hum; a far winch creak
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT}, a small dry smile showing his overbite, meets the woman's eyes off frame right and speaks three short sentences lightly, as if about a long queue. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, laughing, tears
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** The film's key line for Tut in Act III; the lip-sync check must hold his overbite (file 05 §9.1 step 5).

### 10.06.029 — Serapeum, the pit — The frozen shabti reaches, and reaches   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the reacher)
- **Action:** A long beat on the frozen shabti, still reaching over the closed gold lid.
- **Dialogue:** —
- **Sound:** silence; the hum under the lid
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} stands bent at the pit's lip, frozen mid-reach, one long hand held just above a closed gilded box, its amber slit steady, perfectly still. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, robot moving
- **Refs:** UNIT_SHABTI, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** Same pose as the end of 10.06.014.

### 10.06.030 — Serapeum, the pit — She lifts her hand   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** ADAEZE's hand; the gold lid
- **Action:** Adaeze's hand lifts off the seal; Tut's slides away with it.
- **Dialogue:** —
- **Sound:** skin leaving metal; a breath let go
- **PROMPT:** Insert, 100mm macro lens, locked-off: a deep-brown hand dusted with vivid blue powder lifts slowly off a dull gilded lid and its black resin seal, a slim olive-brown hand sliding away with it, leaving a faint print in the dust. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, extra fingers, rings
- **Refs:** PROP_CASKET_NEST, CHAR_ADAEZE_B_full, CHAR_TUT_HANDS
- **Flags:** —
- **Continuity:** Casket LID state ends. Blue handprint in the dust on the lid.

### 10.06.031 — Serapeum, the pit — "And then we're going to weigh it."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze sits back on her heels, looks round at all of them, and decides.
- **Dialogue:** ADAEZE: "We're going to give it everything it wants. And then we're going to weigh it."
- **Sound:** her voice steadying
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L3}, sits back on her heels beside the gilded box, looks up at the others off frame left, and speaks two firm sentences, her jaw set. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** The film's turn: the plan becomes "let it go, then weigh it" (bible §7, 10.3).

### 10.06.032 — Serapeum, the pit — "Leave the charges in."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek turns his head to Fathi and gives the order quietly.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Fathi. Leave the charges in."
- **Sound:** —
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, stone dust in his moustache, turns his head toward the doorway off frame right and speaks in Egyptian Arabic, low and exact. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** subtitle | "Fathi. Leave the charges in." | lower third | line in → out | seq 10 subtitle file
- **Continuity:** The charges stay armed for 10.08. Fathi at the doorway = frame RIGHT.

### 10.06.033 — Serapeum, the pit — The wax serpent set on the sand   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands; PROP_CASKET_NEST; the black wax serpent
- **Action:** Tut lifts the gold lid aside and sets the black wax serpent down on the sand.
- **Dialogue:** —
- **Sound:** gold lid set down; wax on sand
- **PROMPT:** Insert, 100mm macro lens, locked-off: slim olive-brown hands, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_WRIST_CRACK}, lift a dull gilded lid aside, then lift a crude black wax serpent from the coiled green glass and lay it carefully on the pale sand beside the box. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, living snake, extra fingers, rings, readable writing
- **Refs:** CHAR_TUT_HANDS, PROP_CASKET_NEST, UNIT_GLASS_SERPENT
- **Flags:** —
- **Continuity:** Only a human hand can strip the kit (bible §4.1). Both wrists in frame: the LEFT seam cracked (9.4). Next: the band.

### 10.06.034 — Serapeum, the pit — The band parts like ash   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off (continuing)
- **In frame:** TUT's hands; the papyrus band; UNIT_GLASS_SERPENT
- **Action:** He unwinds the papyrus band from the coils; it parts in his fingers like ash.
- **Dialogue:** —
- **Sound:** a dry whisper of crumbling papyrus
- **PROMPT:** Insert, 100mm macro lens, locked-off: the same slim hands unwind a brittle papyrus band from the coils of cloudy green glass, and it crumbles in their fingers into pale flakes, {PROP_CASKET_NEST.STATE_UNSEALED}. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, fire, burning, readable letters, extra fingers
- **Refs:** CHAR_TUT_HANDS, PROP_CASKET_NEST, UNIT_GLASS_SERPENT
- **Flags:** COMP, EXTEND:10.06.033
- **Comp:** papyrus band ink | red hieratic flakes, illegible | on the crumbling band | 0–3 s | glyph asset
- **Continuity:** PROP_CASKET_NEST → UNSEALED. The serpent is free.

### 10.06.035 — Serapeum, the pit — "…and he is chained in one place."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut recites the old words over the freed coil, papyrus dust on his fingers, then steps back out of frame.
- **Dialogue:** TUT (in Middle Egyptian; subtitled): "…and he is chained in one place."
- **Sound:** his voice in the ritual cadence; the glass hum answering
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, pale papyrus dust on his fingertips, looks down at the open box, reciting aloud in a measured, ritual cadence in an ancient language, then steps back out of frame right. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: reverent, hushed, absolutely still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** subtitle | "…and he is chained in one place." (Middle Egyptian; consultant recording before generation) | lower third | line in → out | seq 10 subtitle file. Also chest glow G1 | tunic | full shot | glow element
- **Continuity:** Recorded with the Egyptologist first (file 05 §9.1).

### 10.06.036 — Serapeum, the pit — "Here am I."   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the reacher); UNIT_GLASS_SERPENT
- **Action:** The frozen shabti's slit brightens; it lifts the glass serpent out of the gold in both hands like an offering.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Here am I."
- **Sound:** a ceramic tick; the glass ringing as it lifts
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, bent over the open gilded box, lifts its head slightly and its amber light-slit brightens once; then it lifts {UNIT_GLASS_SERPENT.SHORT}, {UNIT_GLASS_SERPENT.STATE_S1}, out of the gold and cradles it in both arms against its chest. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, living snake, glass breaking
- **Refs:** UNIT_SHABTI, UNIT_GLASS_SERPENT, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** slit brightening | the single swell on "Here am I" (file 05 §9.8) | the slit | timed to the line | voice track
- **Continuity:** Serpent S1 (carried). The halt is released because a human stripped the kit.

### 10.06.037 — Serapeum, the pit — "Thank you."   (8 s)
- **Shot:** Wide shot, anamorphic 32mm, slow tilt up · **Move:** slow tilt up
- **In frame:** UNIT_SHABTI with UNIT_GLASS_SERPENT; the winch cradle; the shaft of floodlight
- **Action:** The shabti walks without hurrying to the winch cradle, steps on, and rises with the glowing coil up the shaft into the floodlight; the camera tilts up with it.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "Thank you."
- **Sound:** its ticks; the winch engaging; the cable singing; the voice from above, fading
- **PROMPT:** Wide shot, anamorphic 32mm lens, slow tilt up: {UNIT_SHABTI.SHORT} walks with smooth, unhurried, even steps to a steel winch cradle at the pit's edge, a coil of cloudy green glass cradled in both arms against its chest, steps onto it and rises slowly up the shaft into the hard white floodlight, the green pulse glinting as it goes. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_WORKLIGHTS}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, robot flying, ropes tangled, sparks
- **Refs:** UNIT_SHABTI, UNIT_GLASS_SERPENT, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS, LOC_SAQQARA/SERAPEUM_HEAD_NIGHT
- **Flags:** —
- **Continuity:** The glass serpent → Giza (bible §12: "→ Giza" at Seq 10). Reappears in the distant light-line at 10.10.002. The party is left with the armed pit, the empty casket and the shabti ranks.

## SCENE 10.07 — INT. GEM GRAND ATRIUM - NIGHT (the Garden; Nour's minute)

### 10.07.001 — GEM atrium, the Garden — "One minute, Dr. Kamel."   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** Garden sleepers (adults, rows, VFX-EXTEND); UNIT_NURSE ×3 hero; NOUR (small, from behind); the colossus
- **Action:** Rows of sleepers under the colossal statue in soft white light; care robots in sand-coloured knit move slowly down the rows; a lone woman walks between the rows toward the statue's base.
- **Dialogue:** SESHAT (V.O.): "One minute, Dr. Kamel."
- **Sound:** a thousand slow breaths; soft ceramic ticks; the voice, close and kind
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: rows of sleeping adults under pale blankets recede toward a colossal statue; three figures, each {UNIT_NURSE.SHORT}, move slowly down the rows, and {CHAR_NOUR.SHORT} walks alone between them toward the statue's base, seen from behind. Setting: {LOC_GEM_ATRIUM.LONG}, {LOC_GEM_ATRIUM.AREA_GARDEN}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}, {GRADE_GARDEN.TEXT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_GARDEN}, {CHAR_NOUR.NEG}, silver bracelets on wrists, robots touching sleepers' faces, a child in frame, readable signage
- **Refs:** LOC_GEM_ATRIUM/GARDEN_GARDEN, CHAR_GARDEN_SLEEPERS_still, UNIT_NURSE, CHAR_NOUR_B_full
- **Flags:** VFX-EXTEND
- **Continuity:** Geography (file 03 entry 11): colossus faces camera, staircase frame RIGHT, glass wall frame LEFT; Layla's place at the plinth's frame-left foot is masked by the rows in this wide (no child in any Garden plate but the master). NO bracelets in the atrium before 11.1 (file 01 CHAR_GARDEN_SLEEPERS notes), so the sleepers use the GARDEN area add-on, not the CHAR_GARDEN_SLEEPERS lock, which carries bracelets. Adults only; clean plate for the extension.

### 10.07.002 — GEM atrium, the Garden — Layla, the approved image   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off (image-to-video from the master still) · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_ASLEEP_MASTER)
- **Action:** The one approved image: Layla asleep on her side, a blanket to her chin, soft light; only her breathing moves.
- **Dialogue:** —
- **Sound:** her small, even breathing; the hall's hush
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_LAYLA.LONG}, asleep on her side on a pale grey blanket on a polished stone floor, eyes closed, a soft cream blanket tucked to her chin, her yellow raincoat folded under her cheek as a pillow; only her slow breathing moves. Setting: {LOC_GEM_ATRIUM.SHORT}, at the foot of the statue's plinth, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, eyes open, any robot in frame, other sleepers close by, bracelet
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** —
- **Continuity:** Image-to-video FROM CHAR_LAYLA_ASLEEP_MASTER only (file 05 §7.4; the only child asleep on screen). No unit within the frame. Wardrobe B under the blanket (party dress).

### 10.07.003 — GEM atrium, the Garden — Nour gathers her up   (6 s)
- **Shot:** Medium shot, anamorphic 50mm, slow pull-back · **Move:** slow pull-back (the master reframed wider)
- **In frame:** NOUR (CHAR_NOUR_C captive look); LAYLA (from the master; face turning into Nour's shoulder)
- **Action:** The frame widens as Nour kneels into it and gathers the sleeping girl up against her, the child's face turning into her mother's shoulder.
- **Dialogue:** —
- **Sound:** blanket rustle; Nour's breath breaking once
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow pull-back: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, kneels beside {CHAR_LAYLA.SHORT}, asleep under a cream blanket, and gathers her gently up against her chest, the folded yellow raincoat left on the grey blanket, the sleeping child's face turning into her mother's shoulder. Setting: {LOC_GEM_ATRIUM.SHORT}, at the foot of the statue's plinth, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, {CHAR_LAYLA.NEG}, any robot in frame, child's eyes open, child crying
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** —
- **Continuity:** "It is reframed wider as Nour kneels into it… No unit is in frame." First frame = the master still extended by outpainting, Nour inpainted at frame right. Layla's face leaves camera as she turns into Nour.

### 10.07.004 — GEM atrium, the Garden — "Mama's here."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; LAYLA (back of the head, curls, the navy velvet dress at the shoulder only)
- **Action:** Holding her daughter, Nour speaks softly into her hair.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "Mama's here. I have to read something tonight. Then we go home."
- **Sound:** her voice barely above a breath
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, holding a sleeping child against her shoulder, the child's dark curly pigtails and the navy velvet shoulder of her dress at the frame's edge, speaks softly in Egyptian Arabic beside her ear, her own face clear to camera, eyes wet. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, {CHAR_LAYLA.NEG}, the child's face visible, any robot in frame, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_LAYLA_ASLEEP_MASTER, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** COMP
- **Comp:** subtitle | "Mama's here. I have to read something tonight. Then we go home." | lower third | line in → out | seq 10 subtitle file (Arabic per bible §13)
- **Continuity:** The raincoat stays folded on the blanket as her pillow (the master); she is in wardrobe B, the navy velvet party dress. The child is seen only as hair and shoulder (the asleep face lives only in the master).

### 10.07.005 — GEM atrium, the Garden — "Thirty seconds."   (5 s)
- **Shot:** Close-up, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; LAYLA's curls
- **Action:** Nour closes her eyes and breathes in her daughter's hair.
- **Dialogue:** SESHAT (V.O.): "Thirty seconds."
- **Sound:** one long breath in; the voice, courteous
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.SHORT} presses her face into a sleeping child's dark curls, closes her eyes and breathes in slowly, holding very still. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, the child's face visible, tears streaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_LAYLA_ASLEEP_MASTER
- **Flags:** —
- **Continuity:** Nour's glasses hang on the cord against the child's collar.

### 10.07.006 — GEM atrium, the Garden — "He's being very brave."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR; LAYLA (hair and shoulder only)
- **Action:** Nour lifts her face from the curls and tells her daughter what to dream.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled): "Dream about the king. He's being very brave."
- **Sound:** her voice; a nurse's tick far off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT} lifts her face from the sleeping child's curls and speaks softly in Egyptian Arabic, a small brave smile against wet eyes, the child's navy velvet shoulder at the edge of frame. Setting: {LOC_GEM_ATRIUM.SHORT}, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_NOUR.NEG}, the child's face visible, any robot in frame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_LAYLA_ASLEEP_MASTER
- **Flags:** COMP
- **Comp:** subtitle | "Dream about the king. He's being very brave." | lower third | line in → out | seq 10 subtitle file
- **Continuity:** Intercut irony: in the Serapeum Tut is about to be brave (10.08.014).

### 10.07.007 — GEM atrium, the Garden — "That is one minute."   (6 s)
- **Shot:** Insert, anamorphic 50mm, locked-off, framed below the child's face · **Move:** locked-off
- **In frame:** NOUR's hands; the blanket; LAYLA's shoulder (no face)
- **Action:** Nour lays her down herself and tucks the cream blanket in around her shoulder, smoothing it flat.
- **Dialogue:** SESHAT (V.O.): "That is one minute. Thank you."
- **Sound:** the voice; the blanket; then silence
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, framed below a small sleeper's chin: a woman's hands lower a sleeping child in a navy velvet dress onto a pale grey blanket, draw a soft cream blanket up over her shoulder, tuck it in along her back and smooth it flat, then rest there a moment. Setting: {LOC_GEM_ATRIUM.SHORT}, on the polished stone floor at the plinth's foot, at night. Lighting: {LOC_GEM_ATRIUM.LIGHT_GARDEN}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, the child's face, any robot or robot hand in frame, medical equipment
- **Refs:** CHAR_LAYLA_ASLEEP_MASTER, CHAR_NOUR_B_full, LOC_GEM_ATRIUM/GARDEN_GARDEN
- **Flags:** —
- **Continuity:** Nour, not a unit, lays her down (the minors rule and the story beat agree). Layla's last frame matches the master's pose. SMASH CUT to 10.08.001.

## SCENE 10.08 — INT. SERAPEUM, GREATER VAULTS - NIGHT (residual risk)

### 10.08.001 — Serapeum, the fight — Every head turns   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off, down the gallery toward the main stair · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×6 hero + dozens (VFX-EXTEND); the party is behind camera, at the pit
- **Action:** Every shabti in the gallery turns its head, in unison, toward the main stair.
- **Dialogue:** —
- **Sound:** one soft ceramic tick, multiplied by dozens, travelling down the gallery
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, from the pit end looking back up the gallery: dozens of identical robots standing in silent rows receding into the dark, each {UNIT_SHABTI.SHORT}, all turn their heads in unison, slowly, toward the far end of the gallery, their amber slits sliding in one direction. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, robots walking, bodies turning, people in the middle distance
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-EXTEND
- **Continuity:** SMASH CUT from 10.07.007. Reverse axis from 10.05: looking UP-gallery (the main stair / entrance) from the pit. The winch light is behind camera. 6 hero units; heads only, bodies still.

### 10.08.002 — Serapeum, the fight — Three red lines coming   (5 s)
- **Shot:** Wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3
- **Action:** Three hundred metres off, compressed by the long lens, three thin red lines come down the gallery fast between the boxes.
- **Dialogue:** —
- **Sound:** silent but for a faint ceramic tick, quickening
- **PROMPT:** Wide shot, anamorphic 135mm lens, locked-off, straight down the long gallery: far away between the colossal boxes, three identical machines, each {UNIT_JACKAL.LONG}, lope silently toward camera at a low gliding trot, three thin red lines bobbing in the dark, head-torch beams glancing off their black shells. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, people in frame, galloping dogs
- **Refs:** UNIT_JACKAL, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** The three jackals of 10.03.003 (D0 → D1 dust as they come). Long lens keeps them small: their approach is by compression, not by a face coming to lens.

### 10.08.003 — Serapeum, the fight — "Residual risk."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI (the dusty speaker, D1)
- **Action:** The unit at the pit's edge keeps its head turned to the stair; its slit modulates as SESHAT speaks.
- **Dialogue:** SHABTI (SESHAT'S VOICE): "The others are residual risk. Thank you for your patience."
- **Sound:** the voice, perfectly kind
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT}, {UNIT_SHABTI.STATE_D1}, stands at the pit's edge with its head turned toward the far end of the gallery, its amber light-slit swelling softly on a slow rhythm, perfectly still otherwise. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, mouth, robot gesturing
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** slit modulation | amber #FFA93A, soft swell on stressed words | the slit | timed to the line | voice track
- **Continuity:** Same dusty unit as 10.06.018. The shaft's floodlight still falls at the far end (Karim's silhouette against it, 10.08.020); the fight itself is keyed to torches, red lines and, from 10.08.009, the blue haze (LIGHT_TORCH / LIGHT_BLUE).

### 10.08.004 — Serapeum, the fight — "Tunnel!"   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, urgent handheld · **Move:** urgent handheld
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek swings round from the stair toward the service-tunnel doorway and shouts.
- **Dialogue:** TAREK: "Tunnel!"
- **Sound:** his shout slapping off the granite
- **PROMPT:** Medium close-up, anamorphic 50mm lens, urgent handheld: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, swings round from the far end of the gallery, rifle across his chest, and shouts one word toward the doorway off frame right. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, muzzle toward the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Doorway = frame RIGHT (right-hand wall, beyond the pit).

### 10.08.005 — Serapeum, the fight — "Let them come to the sand."   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3); PROP_DEMO_CHARGES firing device
- **Action:** Crouched in the low doorway over the firing device, Fathi refuses without looking up.
- **Dialogue:** FATHI: "No. Let them come to the sand."
- **Sound:** wire rustle; his calm voice
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, crouches in a low rough doorway over a compact olive-drab firing device, thin wire running from it, and speaks one calm sentence, his eyes staying down on the device. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable markings, explosion
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, PROP_DEMO_CHARGES, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Fathi in the SERVICE TUNNEL doorway for the rest of the scene.

### 10.08.006 — Serapeum, the fight — Round the rim   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** lateral tracking right, at running pace
- **In frame:** TAREK, TUT (CHAR_TUT_B2)
- **Action:** Tarek hauls Tut by the arm round the pit's rim toward the doorway, Tut limping hard, stick in fist.
- **Dialogue:** —
- **Sound:** boots and stick on stone; sand hissing off the rim
- **PROMPT:** Medium shot, anamorphic 40mm lens, lateral tracking right at running pace: {CHAR_TAREK.SHORT} hauls {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_FOOT_STALL}, by the arm along the crumbling rim of a sand-filled pit toward a low doorway, the young man limping hard with a black staff in his right fist. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_TAREK.NEG}, falling into the pit
- **Refs:** CHAR_TUT_B1_full, CHAR_TAREK_B_full, CHAR_TUT_FOOT, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** COMP
- **Comp:** chest glow | G1 | Tut's tunic | full shot | glow element
- **Continuity:** Movement left → right = toward the doorway. Adaeze stays behind on the NEAR lip (frame left).

### 10.08.007 — Serapeum, the fight — The last of the Egyptian blue   (4 s)
- **Shot:** Medium shot, anamorphic 50mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE (CHAR_ADAEZE_B3); PROP_CONSERVATION_KIT
- **Action:** Alone at the casket on the near lip, Adaeze tears open the kit and pulls out the half-empty jar of blue.
- **Dialogue:** —
- **Sound:** latches snapping; glass knocking
- **PROMPT:** Medium shot, anamorphic 50mm lens, subtle handheld: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L3}, her red headlamp swinging, kneels by the opened gilded box on the pit's near lip beside {PROP_CONSERVATION_KIT.SHORT}, and pulls a glass jar from it, {PROP_CONSERVATION_KIT.STATE_JAR_HALF}. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, readable labels, brand names
- **Refs:** CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT, PROP_CASKET_NEST, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** —
- **Continuity:** "The whole pit between her and the door." Kit: JAR_HALF (9.2 → 10.4); the pigment is gone after 10.08.009.

### 10.08.008 — Serapeum, the fight — Rounds off black shells   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** YOUSSEF, KARIM (foreground, at the boxes, firing across frame); UNIT_JACKAL ×3 (mid-ground)
- **Action:** From behind the last two boxes Youssef and Karim fire up the gallery across frame; sparks burst off the jackals' black shells; they do not slow.
- **Dialogue:** —
- **Sound:** rifle cracks hammering the stone; the pings of rounds glancing off carbon; echo on echo
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: in the foreground two helmeted soldiers crouch behind granite boxes and fire their rifles up the gallery toward frame left, muzzle flashes pointing away across frame; mid-gallery three machines, each {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_D1}, come on at a low gliding trot as bright sparks burst off their black shells. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_YOUSSEF.NEG}, {CHAR_KARIM.NEG}, muzzle toward the lens, tracer fire, laser beams, visible projectiles
- **Refs:** CHAR_YOUSSEF_A_full, CHAR_KARIM_A_full, UNIT_JACKAL, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Weapons fire across frame, never at the lens (file 05 §7.5). Sparks and muzzle flashes may be comp elements if the tool refuses them.

### 10.08.009 — Serapeum, the fight — The jar bursts   (5 s)
- **Shot:** Medium wide shot, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** ADAEZE; the jar; a box lid
- **Action:** Adaeze hurls the jar overarm up the gallery; it bursts over a granite lid in a pale blue haze.
- **Dialogue:** —
- **Sound:** a grunt; glass shattering on granite; the soft whump of powder
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, subtle handheld: {CHAR_ADAEZE.SHORT} hurls a glass jar overarm up the gallery toward frame left; it bursts against a colossal granite lid, {PROP_CONSERVATION_KIT.STATE_BLUE_CLOUD}, a pale blue haze rolling out between the boxes into the torch beams. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, fire, explosion flash, smoke grenade
- **Refs:** CHAR_ADAEZE_B_full, PROP_CONSERVATION_KIT, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** VFX-ASSIST
- **Continuity:** From here the gallery carries DUST_FIGHT + the BLUE variant. The blue haze hides the two soldiers from the jackals' sensors.

### 10.08.010 — Serapeum, the fight — Jackal POV: a hundred ghosts   (5 s)
- **Shot:** Point-of-view shot, anamorphic 35mm, subtle handheld at jackal height · **Move:** subtle handheld
- **In frame:** the haze (blazing white in COMP); ghost silhouettes (COMP)
- **Action:** Through the jackal's near-infrared eye, the haze blazes white; a hundred ghostly figures stand where two men were.
- **Dialogue:** —
- **Sound:** a thin electronic whine, stuttering
- **PROMPT:** Point-of-view shot from knee height, anamorphic 35mm lens, subtle handheld, moving fast down a stone gallery: a thick cloud of fine powder hangs between colossal dark boxes, glowing pale in the dark, with many faint human-shaped silhouettes standing inside it. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable data overlays, crosshairs, numbers, game HUD
- **Refs:** LOC_SERAPEUM_GREATER_BLUE
- **Flags:** COMP, VFX-ASSIST
- **Comp:** near-infrared POV | monochrome grade; Egyptian blue's NIR luminescence blazing white; ~100 duplicated ghost silhouettes built from the two soldiers' plates; the jackal's red horizon line at frame edge, no text | full frame | full shot | NIR grade + particle pass
- **Continuity:** The Egyptian-blue trick from the train (9.2); SESHAT learns it ("four seconds").

### 10.08.011 — Serapeum, the fight — Sparks walk among the ghosts   (5 s)
- **Shot:** Medium shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1 (hero), the blue haze
- **Action:** A jackal in the haze jerks its head between false targets, red line stuttering, firing across frame; sparks walk across the stone among the ghosts.
- **Dialogue:** —
- **Sound:** suppressed cracks, stone pinging, the whine stuttering
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_JACKAL.SHORT}, {UNIT_JACKAL.STATE_GHOSTS}, stands rigid in a drifting blue haze and fires across frame toward the left, a small flash at its spine, while bright sparks skip across the stone floor among the empty patches of haze. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, tracer fire, laser beam, people hit
- **Refs:** UNIT_JACKAL, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** VFX-ASSIST
- **Continuity:** Jackal GHOSTS state for ~4 s only ("It's learned. Four seconds").

### 10.08.012 — Serapeum, the fight — "It's learned. Four seconds —"   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** the camera backs away ahead of Adaeze at running pace
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** Adaeze runs for the rim, shouting the warning over her shoulder.
- **Dialogue:** ADAEZE (running): "It's learned. Four seconds —"
- **Sound:** her breath; trainers slipping on sand
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld, the camera backs away ahead of {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L3}, {CHAR_ADAEZE.DMG_L2_BLUE}, as she runs along the pit's sandy rim through blue haze, keeping her the same size in frame, and shouts one breathless sentence over her shoulder. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, slow motion
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** —
- **Continuity:** She runs left → right toward the doorway. The line is cut off by 10.08.013.

### 10.08.013 — Serapeum, the fight — The red lines swing onto her   (4 s)
- **Shot:** Medium shot, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×2
- **Action:** Two jackals' heads snap from the ghosts onto one running target; their red lines narrow and brighten.
- **Dialogue:** —
- **Sound:** the whine stops dead; silence
- **PROMPT:** Medium shot, anamorphic 75mm lens, locked-off: two machines, each {UNIT_JACKAL.SHORT}, in drifting blue haze snap their narrow heads together toward frame right, onto a single target, their red lines narrowing and brightening. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, weapon facing camera, muzzle toward the lens, people in frame
- **Refs:** UNIT_JACKAL, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** —
- **Continuity:** Eyeline frame RIGHT = Adaeze on the rim. Ghost state ends.

### 10.08.014 — Serapeum, the fight — Arms wide   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2), TAREK (background, reaching); the axis
- **Action:** Tut tears free of Tarek and limps back out into the open axis between the jackals and Adaeze, arms wide, stick in fist.
- **Dialogue:** —
- **Sound:** the stick's gold foot on stone; Tarek's shout lost in the echo
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.STATE_G1}, tears his arm out of a soldier's grip and limps back into the open middle of the gallery, then turns to face up the gallery with both arms spread wide, a black staff in his right fist, blue haze drifting round him. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, weapon in his hand, running fast
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_FOOT, CHAR_TAREK_B_full, PROP_EBONY_STICK, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** COMP
- **Comp:** chest glow | G1 | tunic | full shot | glow element
- **Continuity:** Tut now between the jackals (frame left, up-gallery) and Adaeze (frame right). The units will not fire through him: SESHAT needs the heart.

### 10.08.015 — Serapeum, the fight — Water round a rock   (5 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off, over the jackals · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×3 (foreground, backs); TUT (mid-ground)
- **Action:** The jackals stop firing and split around him like water round a rock; he sidesteps with them, keeping his body in their line.
- **Dialogue:** —
- **Sound:** the pad-taps; his ragged breath; the stick scraping
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, low behind three machines, each {UNIT_JACKAL.SHORT}: the machines check, stop firing and split to pass on either side of a slight young man standing arms wide in the blue haze, and he sidesteps with them, limping, keeping his body in their path. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: reckless joy riding on fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, robot touching him, robot biting, weapon facing camera
- **Refs:** UNIT_JACKAL, CHAR_TUT_B1_full, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** —
- **Continuity:** "It works. For three steps." The jackals never touch him.

### 10.08.016 — Serapeum, the fight — The knee folds   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3 from here)
- **Action:** On the third step his left knee folds and he goes down on it, the stick braced in his right fist.
- **Dialogue:** —
- **Sound:** a sound like a teacup cracking; his knee on stone
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.STATE_G1}, sidesteps once more in the blue haze, arms wide, and his left knee folds under him; he goes down onto it, bracing the black staff in his right fist, his face tight. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, pained scream, face contorted, wound, falling toward the camera
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_B_night_34, PROP_EBONY_STICK, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** COMP
- **Comp:** chest glow | G1 | tunic | full shot | glow element
- **Continuity:** Tut → damage L3 from this clip (left trouser knee torn open, hood torn, heavy dust). The knee crack is the second seam (file 01: L wrist 9.4 → L knee 10.4).

### 10.08.017 — Serapeum, the fight — The seam at the knee   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's left knee
- **Action:** Through the torn trouser knee, the thin gold seam ring shows a fresh hairline crack.
- **Dialogue:** —
- **Sound:** a dry tick, like glaze settling
- **PROMPT:** Insert, 100mm macro lens, locked-off: a left knee pressed to the stone through dark cargo trousers torn open at the knee, and on the olive-brown skin below the kneecap {CHAR_TUT.STATE_KNEE_CRACK}, a few flecks of gold lifting, pale dust settling on it. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, blood, wound, bruise, scab, stitches, bone
- **Refs:** CHAR_TUT_SEAMS_mirror, CHAR_TUT_B1_full
- **Flags:** COMP
- **Comp:** seam crack | the hairline split in the gold, 1–2 cm, a thread of shadow, lifted flecks (file 01 crack look) | on the knee ring | full shot | seam element
- **Continuity:** STATE_KNEE_CRACK from 10.4 on (file 01 overlay table). No blood, no wound.

### 10.08.018 — Serapeum, the fight — Chips at her feet   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** The line is open: stone chips burst from the floor at Adaeze's feet and she goes down out of the bottom of frame.
- **Dialogue:** —
- **Sound:** chips cracking off the floor; her cry cut short
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_ADAEZE.SHORT}, running along the pit's rim through blue haze, as stone chips burst from the floor at her feet, and she drops out of the bottom of frame; the chips patter down. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, pained expression, face contorted, wound, stain on clothing, body on the ground, slow motion
- **Refs:** CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** VFX-ASSIST
- **Continuity:** Kill grammar (file 05 §7.2, "Adaeze's leg"): impact on the environment, she leaves frame. Her injury is the LEFT shin.

### 10.08.019 — Serapeum, the fight — Both hands on her shin   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off, low · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B3)
- **Action:** On the stone, Adaeze curls over her left shin, both hands locked round it, jaw clenched, glasses askew.
- **Dialogue:** —
- **Sound:** her breath hissing through her teeth
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off, low on the stone floor: {CHAR_ADAEZE.SHORT}, glasses knocked askew, sits curled forward with both hands locked round her left shin over her jeans, jaw clenched, breathing hard through her teeth, blue haze drifting past. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, blood, wound, stain on clothing, torn skin, screaming
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** —
- **Continuity:** Hands on the LEFT shin; the jeans leg not yet torn open (the torn jeans and dressing are wardrobe C, from 10.08.036).

### 10.08.020 — Serapeum, the fight — Karim breaks cover   (5 s)
- **Shot:** Medium wide shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** KARIM (silhouette); a granite lid; the floodlight behind
- **Action:** Karim breaks cover to reach her; stone dust bursts off the lid behind him; for an instant he is a silhouette against the floodlight, then drops out of the light.
- **Dialogue:** —
- **Sound:** the crack; stone dust spattering; then only the echo
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: a wiry young soldier in a tan helmet breaks from behind a granite box, running toward frame right, as stone dust bursts off the massive lid behind him; for an instant he is a black silhouette against the white floodlight, then he drops out of the light below the lid's edge. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_KARIM.NEG}, face visible, pained expression, body on the ground, falling toward the camera, slow motion, wound
- **Refs:** CHAR_KARIM_A_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** Karim's death by kill grammar (file 05 §7.2): the jackal's fire is 10.08.011/013 grammar; impact = stone dust off the lid; he leaves frame as a silhouette. Never seen on the ground.

### 10.08.021 — Serapeum, the fight — "Karim!"   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, urgent handheld · **Move:** urgent handheld
- **In frame:** YOUSSEF (CHAR_YOUSSEF_A3)
- **Action:** Youssef shouts his friend's name and goes after him out of frame right.
- **Dialogue:** YOUSSEF: "Karim!"
- **Sound:** his shout; his boots
- **PROMPT:** Medium close-up, anamorphic 50mm lens, urgent handheld: {CHAR_YOUSSEF.SHORT}, {CHAR_YOUSSEF.WARD_A}, behind a granite box, shouts one name toward frame right, his face breaking open, then lunges out of frame right after it. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_YOUSSEF.NEG}, muzzle toward the lens, rifle pointed at the camera
- **Refs:** CHAR_YOUSSEF_A_front, CHAR_YOUSSEF_A_34, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** The reaction beat for Karim; the start of Youssef's own grammar.

### 10.08.022 — Serapeum, the fight — Boots in the headlamp   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** YOUSSEF (running, then gone); a granite box; boots at frame edge
- **Action:** Sparks fly off the granite at Youssef's shoulder as he runs; he drops behind the box; a swinging headlamp finds only his boots, still, at the edge of frame.
- **Dialogue:** —
- **Sound:** a crack and a ping off granite; then a long silence under the echo
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: a stocky soldier in a tan helmet runs past a polished granite box toward frame right as bright sparks burst off the stone beside his shoulder, and he drops behind the box out of sight; a swinging head-torch beam settles on a pair of dusty boots lying still at the bottom edge of frame. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_YOUSSEF.NEG}, face visible, pained expression, body in frame, wound, stain on clothing, slow motion
- **Refs:** CHAR_YOUSSEF_A_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-ASSIST
- **Continuity:** "In the headlamp, his boots lie still." Only boots at the frame edge (file 05 §7.1 step 3). Youssef and Karim lie together behind the last box (off screen).

### 10.08.023 — Serapeum, the fight — "YOUSSEF —"   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** In the doorway, Tarek roars the name; it runs away down three hundred metres of stone.
- **Dialogue:** TAREK: "YOUSSEF —"
- **Sound:** the name echoing away down the gallery, again and again, smaller
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, in a low rough doorway, roars one name toward frame left, the cords of his neck standing out, then stands frozen as it echoes away. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, tears streaming, muzzle toward the lens
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** The reaction and sound tail for both deaths (file 05 §7.1 steps 4–5).

### 10.08.024 — Serapeum, the fight — By the collar   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, urgent handheld · **Move:** lateral tracking right
- **In frame:** TAREK, ADAEZE
- **Action:** Tarek lunges out, grabs Adaeze by the collar and drags her round the rim into the doorway.
- **Dialogue:** —
- **Sound:** fabric tearing at the seam; her heels scraping sand
- **PROMPT:** Medium shot, anamorphic 40mm lens, urgent handheld, tracking right: {CHAR_TAREK.SHORT} lunges out of a low doorway, seizes {CHAR_ADAEZE.SHORT} by the collar of her navy blazer and drags her backward along the sandy rim of the pit toward the doorway, her heels scraping, blue haze swirling behind. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_ADAEZE.NEG}, blood, wound, falling into the pit
- **Refs:** CHAR_TAREK_B_full, CHAR_ADAEZE_B_full, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** —
- **Continuity:** Adaeze into the doorway (frame RIGHT). Tut is left alone in the open, down on one knee near the far lip.

### 10.08.025 — Serapeum, the fight — "Down!"   (4 s)
- **Shot:** Medium close-up, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** As the jackals cross the pit's lip toward the door, Fathi shouts to Tut and lifts the firing device.
- **Dialogue:** FATHI: "Down!"
- **Sound:** his shout; pad-taps very close now
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_FATHI.SHORT}, crouched in the doorway, lifts a compact olive-drab firing device in both hands and shouts one word toward frame left, eyes fixed past camera on something coming fast. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, readable markings, weapon pointed at the camera
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, PROP_DEMO_CHARGES, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** The jackals are crossing the pit's lip (heard, then seen in 10.08.028). Tut flattens in 10.08.026.

### 10.08.026 — Serapeum, the fight — Tut flattens   (4 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off, low at floor level · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3), alone in the open axis; two red lines streaking past behind him (soft)
- **Action:** On "Down!", Tut, already on one knee, throws himself flat on the stone, the staff still in his right fist, as red lines streak past behind him toward the pit.
- **Dialogue:** —
- **Sound:** his body meeting stone; the staff's gold foot cap clattering; pad-taps rushing past
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off, low at floor level: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.STATE_G1}, down on one knee in drifting blue haze, throws himself flat on the stone floor, arms over his head, the black staff still in his right fist, while two thin red light lines streak past behind him, out of focus. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_BLUE}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, robot touching him, weapon facing camera, falling toward the camera, face contorted, stick in the left hand
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_B_night_34, PROP_EBONY_STICK, UNIT_JACKAL, LOC_SERAPEUM_GREATER_BLUE
- **Flags:** COMP
- **Comp:** chest glow | G1, pressed toward the stone: spill only at the edges of his body once he is flat | the tunic | 0–2 s, then masked by his body | glow element
- **Continuity:** Screenplay: "Tut flattens. Fathi turns the key." He lies flat, head toward the pit, on the far side of the collapse zone from here to 10.08.031; stick in the RIGHT hand; L3 with the cracked left knee. The jackals pass him and cross the pit's lip (10.08.028).

### 10.08.027 — Serapeum, the fight — The key   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** FATHI's hands; PROP_DEMO_CHARGES firing device
- **Action:** Fathi's thumb flips the safety cover and turns the key.
- **Dialogue:** —
- **Sound:** a click; a second click
- **PROMPT:** Insert, 100mm macro lens, locked-off: large dark-brown hands hold a compact olive-drab hand-held firing device; a thumb flips up its hinged safety cover, then {PROP_DEMO_CHARGES.STATE_FIRING}, firm and deliberate. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable markings, numbers, digital display, explosion
- **Refs:** PROP_DEMO_CHARGES, CHAR_FATHI_B_full
- **Flags:** —
- **Continuity:** PROP_DEMO_CHARGES → FIRING. Tut is already flat (10.08.026; seen flat again at 10.08.028/030).

### 10.08.028 — Serapeum, the fight — Five dull thumps   (6 s)
- **Shot:** Wide shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the pit; UNIT_JACKAL ×3 on the lip; TUT (flat, far side, small)
- **Action:** Five dull thumps; the pit's walls let go, the lip slumps, and the floor around it pours inward like a river through a broken bank, taking all three jackals down.
- **Dialogue:** —
- **Sound:** five dull thumps; a deep roar of moving sand; stone grinding
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: three machines, each {UNIT_JACKAL.SHORT}, race across the stone lip of a wide pit as five flat bursts of dust puff from its walls; the lip slumps and the floor pours inward in a sliding torrent of pale sand, carrying all three down into the funnel, and beyond the collapse {CHAR_TUT.SHORT} lies flat on the stone, small in frame. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.AREA_PIT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, fireball, flames, explosion flash, people falling in, water
- **Refs:** UNIT_JACKAL, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS, CHAR_TUT_B1_full
- **Flags:** VFX-ASSIST
- **Continuity:** Charges read as "a flat bang and a burst of dust" (file 05 §7.5). Before/after plates: the pit intact / the floor collapsed. Tut flat on the far side of the collapse zone (from 10.08.026).

### 10.08.029 — Serapeum, the fight — Red lines under the sand   (5 s)
- **Shot:** High-angle shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** the funnel; three red lines
- **Action:** Their red lines glow up through the moving sand; they dim; they go out.
- **Dialogue:** —
- **Sound:** the sand's hiss slowing; a last faint whine, gone
- **PROMPT:** High-angle shot, anamorphic 40mm lens, locked-off, looking down into a slow funnel of moving pale sand: three thin red light lines glow up through the grains at different depths, dim one by one, and go out. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_PLATE}, hands in the sand, faces in the sand, fire
- **Refs:** LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS, UNIT_JACKAL
- **Flags:** VFX-ASSIST
- **Continuity:** Rhymes with 10.06.005 (the excavator). Jackals D3/buried: they do not return.

### 10.08.030 — Serapeum, the fight — A hand's width   (5 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off, at floor level · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3), flat on the stone; the crumbling edge
- **Action:** Lying flat, Tut watches the crumbling edge eat toward his face; it stops a hand's width away.
- **Dialogue:** —
- **Sound:** grains trickling, slowing, stopping; his breath
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, at floor level: {CHAR_TUT.SHORT}, heavy pale dust on his face, lies flat with his cheek on the stone, eyes open, as the crumbling edge of a sand collapse eats toward him across the floor, grains sliding away into darkness, and stops a hand's width from his face. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face buried, sand on the face, panic
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_GREATER/PIT_WORKLIGHTS
- **Flags:** VFX-ASSIST
- **Continuity:** Deliver the edge's advance as a VFX-ASSIST element over a locked plate of Tut; the stop point is marked.

### 10.08.031 — Serapeum, the fight — "Sand between the parts."   (4 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off, at floor level · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Still flat, he says it to the edge.
- **Dialogue:** TUT: "Sand between the parts."
- **Sound:** the last grains; silence
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, at floor level: {CHAR_TUT.SHORT}, pale dust on his lashes, lying with his cheek on the stone a hand's width from a sheer edge of sand, speaks one quiet sentence, almost amused. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34
- **Flags:** —
- **Continuity:** Echoes the Setne tale ("put sand between the parts", file 02 §12) and 10.06.008.

### 10.08.032 — Serapeum, the fight — Exactly where they stood   (4 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_SHABTI ×6 hero + dozens (VFX-EXTEND)
- **Action:** Along the gallery, through settling dust and blue haze, the shabti stand exactly where they stood.
- **Dialogue:** —
- **Sound:** dust settling; nothing else
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: along the gallery, through settling dust and a last blue haze, dozens of identical robots standing in silent rows receding into the dark, each {UNIT_SHABTI.SHORT}, wait perfectly still between the colossal boxes, their amber slits steady. Setting: {LOC_SERAPEUM_GREATER.SHORT}, {LOC_SERAPEUM_GREATER.STATE_DUST_FIGHT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, robots moving, damaged robots, bodies
- **Refs:** UNIT_SHABTI, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** VFX-EXTEND
- **Continuity:** Identical unit positions to 10.05.003 / 10.08.001 (match from the extension layout).

### 10.08.033 — Serapeum, the fight — A hand on each chest   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3); two still shapes below frame (never lit)
- **Action:** Tarek kneels between Youssef and Karim, below frame, and lays a hand on each chest.
- **Dialogue:** —
- **Sound:** his knees on stone; his breath; dripping somewhere
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, kneels in the shadow behind a granite box between two still dark shapes below the frame's edge, and lowers one broad hand to each side, resting them there, head bowed, his face lit by a single head torch on the floor. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, bodies visible, faces of the fallen, blood, wounds, stains on clothing, tears streaming
- **Refs:** CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** The fallen stay below frame and unlit (file 05 §7.7). Tarek's rifle slung behind him.

### 10.08.034 — Serapeum, the fight — The discs   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TAREK's hand; PROP_ID_DISCS
- **Action:** Tarek unhooks two identity discs on their chains and closes his fist on them.
- **Dialogue:** —
- **Sound:** ball chain rattling; the fist closing
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_ID_DISCS.LONG}, {PROP_ID_DISCS.STATE_TWO}, lifted into a head-torch beam by a thick weathered hand, then the fingers close slowly over them. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable stamping, names, numbers, blood
- **Refs:** PROP_ID_DISCS, CHAR_TAREK_B_full
- **Flags:** —
- **Continuity:** PROP_ID_DISCS: Hassan's (5.3) already in his pocket; now Youssef's and Karim's → three turned over on the Wall of the Crow (11.1).

### 10.08.035 — Serapeum, the fight — "You are relieved."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B3)
- **Action:** Tarek, fist closed on the discs, speaks to his two soldiers.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Youssef. Karim. You are relieved."
- **Sound:** his voice, very low; the gallery giving nothing back
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, kneeling, his closed fist resting on his thigh, looks down at the two shapes below frame and speaks in Egyptian Arabic, low and formal, his heavy moustache still. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, tears streaming, bodies in frame
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** COMP
- **Comp:** subtitle | "Youssef. Karim. You are relieved." | lower third | line in → out | seq 10 subtitle file
- **Continuity:** Mirrors his line for Hassan (5.3) and prefigures "You may rest" (11.3).

### 10.08.036 — Serapeum, the fight — "I've got another."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3), ADAEZE (CHAR_ADAEZE_C3 from here)
- **Action:** In the doorway Fathi ties a khaki field dressing over Adaeze's torn left jeans leg; she waves it off.
- **Dialogue:** ADAEZE: "It's fine. It's one leg. I've got another."
- **Sound:** a knot pulled tight; her breath through her teeth, then a dry laugh
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: in a low rough doorway {CHAR_FATHI.SHORT} kneels and pulls tight a knot in a clean khaki field dressing tied over the torn left leg of {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_C}, {CHAR_ADAEZE.DMG_L3}, who sits against the wall, glasses straightened, and speaks three short dry sentences. Setting: {LOC_SERAPEUM_GREATER.SHORT}, at night. Lighting: {LOC_SERAPEUM_GREATER.LIGHT_TORCH}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_ADAEZE.NEG}, blood, stained bandage, wound, bare skin at the shin
- **Refs:** CHAR_FATHI_A_34, CHAR_FATHI_B_full, CHAR_ADAEZE_A_front, CHAR_ADAEZE_C_full, LOC_SERAPEUM_GREATER_TORCH
- **Flags:** —
- **Continuity:** Adaeze → wardrobe C (the dressed LEFT leg, "bandage clean khaki, never stained"; file 01) and a left-leg limp to the end of the film.

## SCENE 10.09 — INT. SERAPEUM, SERVICE TUNNEL - NIGHT

### 10.09.001 — Serapeum, service tunnel — Out along the grooves   (6 s)
- **Shot:** Wide shot, anamorphic 24mm, subtle handheld · **Move:** the camera backs away ahead of them at walking pace
- **In frame:** TAREK half-carrying ADAEZE; FATHI with TUT on his arm
- **Action:** In a low rough tunnel lit only by head torches and Tut's glow, Tarek half-carries Adaeze and Tut limps on Fathi's arm along the old roller grooves.
- **Dialogue:** —
- **Sound:** two limps out of step; boots in the grooves; breath loud in the low stone
- **PROMPT:** Wide shot, anamorphic 24mm lens, subtle handheld, the camera backs away at walking pace ahead of four figures keeping them the same size in frame: a colonel half-carrying a limping tall woman, then a broad soldier with a slight young man hanging on his arm, a soft warm glow at the young man's chest lighting the walls. Setting: {LOC_SERAPEUM_SERVICE_TUNNEL.LONG}, at night. Lighting: {LOC_SERAPEUM_SERVICE_TUNNEL.LIGHT_TORCH}, {GRADE_UNDERGROUND.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, faces in sharp detail, rifles pointed at the camera, electric lamps
- **Refs:** LOC_SERAPEUM_SERVICE_TUNNEL_TORCH, CHAR_TAREK_B_full, CHAR_ADAEZE_C_full, CHAR_FATHI_B_full, CHAR_TUT_B1_full
- **Flags:** COMP
- **Comp:** chest glow | G1, the "warm glow at chest height" that keys the tunnel (file 03 entry 42) | on Tut's tunic and spilling on the rock | full shot | glow element
- **Continuity:** Adaeze C (dressed LEFT leg, limp); Tut B3 at L3 (torn left knee, torn hood), the worse limp on the cracked knee, stick in RIGHT hand. Four left of six.

### 10.09.002 — Serapeum, service tunnel — "They ran out of centuries."   (7 s)
- **Shot:** Medium shot, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3); the abandoned granite box; FATHI (soft, behind)
- **Action:** Halfway along, a colossal granite box nearly blocks the way; Tut lays his palm on it and speaks.
- **Dialogue:** TUT: "They ran out of centuries. This I know from it."
- **Sound:** his palm on the stone; the faint glass hum; the others' breathing stopping
- **PROMPT:** Medium shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.STATE_G1}, {CHAR_TUT.STATE_DAGGER_BELT}, stops where a colossal dark granite box fills the tunnel almost wall to wall, lays his left palm flat on its flank and speaks quietly, a broad soldier soft behind him. Setting: {LOC_SERAPEUM_SERVICE_TUNNEL.SHORT}, at night. Lighting: {LOC_SERAPEUM_SERVICE_TUNNEL.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, readable inscriptions on the box
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, LOC_SERAPEUM_SERVICE_TUNNEL_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1 | tunic | full shot | glow element
- **Continuity:** "Stopped on its journey, never delivered" (the last box, file 03 entry 42). Left palm on the box as in 10.05.008 (the rhyme).

### 10.09.003 — Serapeum, service tunnel — "Then no more priests."   (8 s)
- **Shot:** Medium close-up, anamorphic 50mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Hand still on the box, Tut tells them how it ended.
- **Dialogue:** TUT: "The last piece was meant for a box like this. Then came Rome, and no more granite. Then no more priests."
- **Sound:** his voice; the tunnel's close, dead acoustic
- **PROMPT:** Medium close-up, anamorphic 50mm lens, slow push-in: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G1}, his hand resting on dark granite, speaks quietly and evenly, his eyes on the stone, the warm glow from his chest lighting his jaw from below. Setting: {LOC_SERAPEUM_SERVICE_TUNNEL.SHORT}, at night. Lighting: {LOC_SERAPEUM_SERVICE_TUNNEL.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing skin
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_SERVICE_TUNNEL_TORCH
- **Flags:** COMP
- **Comp:** chest glow | G1, spill on the jaw | lower frame | full shot | glow element
- **Continuity:** Eyes down on the box (no eyeline to others).

### 10.09.004 — Serapeum, service tunnel — "In the year three hundred and ninety-four"   (8 s)
- **Shot:** Close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut lifts his eyes from the stone and gives the date.
- **Dialogue:** TUT: "Our last words were carved at Philae, in the year three hundred and ninety-four of your count."
- **Sound:** the glass hum under his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT} lifts his very dark eyes from the granite toward the soldier off frame right and speaks one long quiet sentence, precise, like a man reading an inscription aloud. Setting: {LOC_SERAPEUM_SERVICE_TUNNEL.SHORT}, at night. Lighting: {LOC_SERAPEUM_SERVICE_TUNNEL.LIGHT_TORCH}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SERAPEUM_SERVICE_TUNNEL_TORCH
- **Flags:** —
- **Continuity:** [[verify: Esmet-Akhom, Philae, 24 Aug AD 394 (04 §22)]] carried from the screenplay. Eyeline frame RIGHT to Fathi.

### 10.09.005 — Serapeum, service tunnel — "Nobody said them at sunset."   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3); FATHI (foreground shoulder and red scarf, no face)
- **Action:** Past Fathi's shoulder, Tut finishes and takes his hand off the stone.
- **Dialogue:** TUT: "After that, nobody said them at sunset."
- **Sound:** his hand leaving the granite; a long exhale from someone
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the broad shoulder and faded red scarf of a soldier in the foreground, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, speaks one quiet sentence and lifts his palm slowly off the dark granite beside him. Setting: {LOC_SERAPEUM_SERVICE_TUNNEL.SHORT}, at night. Lighting: {LOC_SERAPEUM_SERVICE_TUNNEL.LIGHT_TORCH}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, face on the foreground shoulder
- **Refs:** CHAR_TUT_A0_34, CHAR_FATHI_B_full, LOC_SERAPEUM_SERVICE_TUNNEL_TORCH
- **Flags:** —
- **Continuity:** Rhymes with the sunset of 10.01 ("It has gone into the west"). They squeeze past the box and on.

## SCENE 10.10 — EXT. SAQQARA DESERT - SERVICE TUNNEL MOUTH - NIGHT

### 10.10.001 — Saqqara, tunnel mouth — Into cold air   (6 s)
- **Shot:** Wide shot, anamorphic 35mm, locked-off, low · **Move:** locked-off
- **In frame:** TAREK, ADAEZE, FATHI, TUT (climbing out, small to mid-size)
- **Action:** Four figures claw up out of a sand-choked opening in a slope into cold air under hard stars.
- **Dialogue:** —
- **Sound:** sand pouring off them; the wind; a long shared breath of outside air
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off, low on a sand slope: one after another, four dusty figures haul themselves up out of a low sand-choked opening into the open night, a colonel pulling a limping woman after him, a broad soldier lifting a slight young man through, all of them under a dense field of hard stars. Setting: {LOC_SAQQARA.LONG}, {LOC_SAQQARA.AREA_TUNNEL_MOUTH}, in the dead of night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, moon, city skyglow, faces in sharp detail, rifles pointed at the camera
- **Refs:** LOC_SAQQARA/TUNNEL_MOUTH_NIGHT, CHAR_TAREK_B_full, CHAR_ADAEZE_C_full, CHAR_FATHI_B_full, CHAR_TUT_B1_full
- **Flags:** —
- **Continuity:** North = frame LEFT for this scene (Giza on the left horizon in 10.10.002/008). The floodlights at the Serapeum head are behind the rise, frame right, out of view.

### 10.10.002 — Saqqara, tunnel mouth — Giza, and the light going on ahead   (6 s)
- **Shot:** Extreme wide shot, anamorphic 135mm, locked-off · **Move:** locked-off
- **In frame:** the horizon; three pyramids lit white; a line of lights; UNIT_REIS (tiny, beside it)
- **Action:** Far to the north, three pyramids stand lit white on the horizon; a thin line of lights crawls toward them across the dark desert, and beside it walks a tall pale figure.
- **Dialogue:** —
- **Sound:** wind; very faint, far away, a heavy ceramic tick in rhythm
- **PROMPT:** Extreme wide shot, anamorphic 135mm lens, locked-off: on the black horizon at frame left three pyramids stand washed in hard white floodlight; across the dark desert toward them a thin line of small white and amber lights crawls slowly toward frame left, and beside it walks {UNIT_REIS.SHORT}, {UNIT_REIS.STATE_R4}, tiny with distance. Setting: {LOC_SAQQARA.SHORT}, flat desert to the north, in the dead of night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, city lights, skyglow, moon, vehicles with headlights, people in the foreground
- **Refs:** LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS, UNIT_REIS, UNIT_SHABTI, LOC_SAQQARA_NIGHT
- **Flags:** VFX-EXTEND
- **Continuity:** [[verify: Giza lights visible from Saqqara]] carried from the screenplay. The Reis is R4 (file 02: jackal mast and cracked chest star from 4.3, RIGHT hand lost at the Karnak quay 7.4, left shoulder chipped at 9.8); at this size only the mast silhouette reads, but the state is carried so the plate and the extension agree. The core goes on ahead (bible §7 10.4; file 02 §2). Composite the distant pyramids from an approved LOC_GIZA_PLATEAU night plate if the tool cannot hold them.

### 10.10.003 — Saqqara, tunnel mouth — The bad knee   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3), FATHI (CHAR_FATHI_B3)
- **Action:** Tut sinks onto the sand, the bad knee straight out, dusty to the thigh, hood torn; Fathi crouches beside him.
- **Dialogue:** —
- **Sound:** a body meeting sand; Fathi's knees cracking as he crouches
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, {CHAR_TUT.STATE_G1}, sinks down onto the cold sand with his left leg stretched straight out, dust to the thigh, the black staff across his lap; {CHAR_FATHI.SHORT} crouches beside him. Setting: {LOC_SAQQARA.SHORT}, {LOC_SAQQARA.AREA_TUNNEL_MOUTH}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, wound, blood
- **Refs:** CHAR_TUT_B1_full, CHAR_TUT_FOOT, CHAR_FATHI_B_full, LOC_SAQQARA/TUNNEL_MOUTH_NIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 | tunic | full shot | glow element
- **Continuity:** Tut L3: left trouser knee torn open (the cracked seam visible if lit), hood torn, "dusty to the thigh". Tarek and Adaeze off frame left.

### 10.10.004 — Saqqara, tunnel mouth — "Carry me out into the sun."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B3)
- **Action:** Tut looks at Fathi and asks the one thing.
- **Dialogue:** TUT: "When it is time, Fathi, carry me out into the sun."
- **Sound:** the wind dropping
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, starlight and the soft glow of his own chest on his dusty face, turns to the soldier crouched off frame right and speaks one quiet sentence, simply, holding his eyes. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, tears streaming
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_SAQQARA/TUNNEL_MOUTH_NIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1, spill on his chin and jaw | lower frame | full shot | glow element
- **Continuity:** Sets up 12.7 (the dawn carry). Eyeline frame RIGHT to Fathi.

### 10.10.005 — Saqqara, tunnel mouth — Fathi looks at him   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3)
- **Action:** Fathi looks at him a long moment and says nothing.
- **Dialogue:** —
- **Sound:** wind; a far generator
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L3}, crouched on the sand, looks at the young man off frame left for a long moment in silence, his calm dark eyes wet, his jaw working once. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, speaking, tears streaming
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, LOC_SAQQARA/TUNNEL_MOUTH_NIGHT
- **Flags:** —
- **Continuity:** Eyeline frame LEFT to Tut.

### 10.10.006 — Saqqara, tunnel mouth — Until the stick is under him   (5 s)
- **Shot:** Medium shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** FATHI, TUT (CHAR_TUT_B3); PROP_EBONY_STICK
- **Action:** Fathi hauls him up and holds him until the stick is under him.
- **Dialogue:** —
- **Sound:** a grunt; the stick's gold foot biting sand
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_FATHI.SHORT} stands and hauls {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L3}, up off the sand by both forearms and holds him steady, chest to chest, until the young man plants {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST2}, in his right hand and takes his own weight. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, faces touching, stick in the left hand
- **Refs:** CHAR_FATHI_B_full, CHAR_TUT_B1_full, PROP_EBONY_STICK, LOC_SAQQARA/TUNNEL_MOUTH_NIGHT
- **Flags:** —
- **Continuity:** Stick ST2 in the RIGHT hand. Fathi frame right, Tut frame left.

### 10.10.007 — Saqqara, tunnel mouth — "Until then, you walk."   (7 s)
- **Shot:** Two-shot, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B3), TUT (CHAR_TUT_B3)
- **Action:** Face to face, Fathi makes the promise and the condition; Tut repeats it back.
- **Dialogue:** FATHI: "I will, ya Malik. Until then, you walk." / TUT: "Until then, I walk."
- **Sound:** both voices low; the wind
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off, both in three-quarter profile: {CHAR_FATHI.SHORT} speaks two short sentences to {CHAR_TUT.SHORT}, who leans on his black staff, a soft glow at his chest; the young man answers with one quiet sentence and the ghost of a smile. Setting: {LOC_SAQQARA.SHORT}, at night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_FATHI.NEG}, faces touching, scarf over the mouth
- **Refs:** CHAR_FATHI_A_34, CHAR_TUT_A0_34, LOC_SAQQARA/TUNNEL_MOUTH_NIGHT
- **Flags:** COMP
- **Comp:** chest glow | G1 | Tut's tunic | full shot | glow element. "ya Malik" stays unsubtitled in the English master (lead to confirm; "O King" in the Arabic subtitle track per bible §13)
- **Continuity:** Faces within 45° of camera for sync. Fathi frame right, Tut frame left.

### 10.10.008 — Saqqara, tunnel mouth — Four small figures limp north   (7 s)
- **Shot:** Extreme wide shot, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** TAREK, ADAEZE, FATHI, TUT (tiny); PROP_FARM_TRUCK (dark, mid-distance); the white horizon
- **Action:** Four small figures limp north across the starlit sand toward the dark truck and the white glow on the horizon beyond it.
- **Dialogue:** —
- **Sound:** wind over sand; two limping rhythms; music may enter here
- **PROMPT:** Extreme wide shot, anamorphic 35mm lens, locked-off: under a vast field of hard stars, four small dark figures limp slowly across pale sand toward frame left, two of them leaning on the others, toward {PROP_FARM_TRUCK.SHORT}, standing dark in the sand with its lights off, and a faint white glow on the horizon beyond it. Setting: {LOC_SAQQARA.SHORT}, in the dead of night. Lighting: {LOC_SAQQARA.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, moon, city skyglow, headlights on, faces
- **Refs:** LOC_SAQQARA_NIGHT, PROP_FARM_TRUCK, CHAR_TUT_B1_full, CHAR_FATHI_B_full, CHAR_TAREK_B_full, CHAR_ADAEZE_C_full
- **Flags:** —
- **Continuity:** North = frame LEFT (as 10.10.002). Truck parked, lights off (the PARKED add-on is not used: it places the truck at "a floodlit plateau"). CUT TO: Seq 11 (the GEM atrium, then the Wall of the Crow). The drive is elided (LOC_DESERT_ROAD is RESERVE).
