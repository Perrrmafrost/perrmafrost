# SEQUENCE 08 — THE WALL — shot list and AI-video prompts

**HERE AM I** · Act IIB · screenplay `screenplay/sequences/seq_08.fountain` (pp. 63–74) · notes `screenplay/notes/seq_08_notes.md` · 6 Nov 2033, 03:05 → about 10:00 · West Bank, Valley of the Kings, KV62, the Nile.
**Format:** 1920×1080, 16:9, 24 fps, clips of 4–8 s. Every PROMPT follows file 05 §5.1 (house pattern, one LONG lock) and ends with `{SUFFIX}`; every NEGATIVE starts with `{NEG}`. Tokens expand from `production_bible/locks.json` via `tools/shots_md2jsonl.py`.

**Shot count:** SHOTCOUNT · **Total running time:** RUNTIME · **Page estimate:** 11.9 pp in the notes' scene table (target 11 pp) ≈ 11–12 min.

| Sc | Heading | Shots | Seconds |
|---|---|---|---|
SCENETABLE

**Sequence rules applied here**
- **Grades:** night exteriors GRADE_NIGHT_ACTION; KV62 interiors GRADE_UNDERGROUND (from 8.5 the chest glow is the only warm source); morning exteriors and the Nile GRADE_2033_DAY. No desert filter.
- **Geography:** at KV62 the larger porch of the tomb above rises frame right, above and behind the stairwell, and the drill sits on the hillside frame right; the jackals' ridge is frame left in the escape. Burial chamber: we enter from the south, the painted north wall faces camera, the painted king's eye right of centre about 2.1 m up. Heart chamber: we enter from the south, the niche centred in the far wall, the bore upper right. The Nile: the East Bank is ahead of the boat; the West Bank hills behind; north is frame right when looking back west.
- **Continuity in (end of Seq 7):** the party of nine lands from the felucca at 03:05; Tut in T-B at damage L2, glow G0f (faltering), nape scar, stick in the RIGHT hand, dagger at the belt, Rami's notebook pressed to his chest; Adaeze carries the conservation kit; Tarek has the police handset on his vest.
- **Continuity out:** Tut at G1 (the vessel seated, wax serpent and papyrus band still on its seal, plate latched), tremor gone, foot steady; plaster dust on Tut and Nour. Mina dead at the top of the stair (kill grammar); Tomas taken north under the cargo drone; the lattice core dark on the heart-chamber floor; one shabti frozen by the empty niche; the corridor mouth collapsed; the valley road blocked at the narrows; party of seven on the farmer's boat.
- **Safety:** kill grammar for Mina (fire across frame → stone chips → drops out of frame → Youssef → the late crack); the heart is only ever the glass vessel with a dark shape inside and a glow through fabric; shabti use open hands and lift Tomas by the arms, never strike; rifles across the body, muzzles off-axis.
- **COMP in this sequence:** SUPER cards (03:05, 03:40, 05:10, 07:40, 09:20); subtitles for every Egyptian Arabic and Late Egyptian line; the chest glow (G0f, G1) and its pulse; the shabti slit brightening on "Here am I"; the IR writing on the tablet; Rami's and Mina's handwriting in the notebook.

## 08.01 — EXT. NILE, WEST BANK SHALLOWS - NIGHT (03:05)

### 08.01.001 — EXT. NILE, WEST BANK SHALLOWS - NIGHT — The felucca noses into the reeds   (6 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** PROP_FELUCCA; the party of nine as small dark figures on deck (no faces)
- **Action:** The felucca glides in out of the black and its bow hisses into the reeds of the west-bank shallows; small dark figures rise to climb out.
- **Dialogue:** —
- **Sound:** the bow hissing through reeds, water lapping the hull, a far thin drone hum high overhead; no voices
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: low over black water, {PROP_FELUCCA.SHORT} glides in toward camera with its sail luffing and its bow hisses into a wall of tall reeds and slows to a stop, small dark figures rising from the deck to climb out. Setting: {LOC_NILE.LONG}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: hushed, exhausted, watchful. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lantern light, lit windows on the banks, city glow on the horizon, moon, daylight, motorboat, visible faces
- **Refs:** PROP_FELUCCA_REF, LOC_NILE/WEST_BANK_SHALLOWS_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "6 NOVEMBER. 03:05." | lower left, small, the subtitle family (05 §13.7) | in at 1 s, out at 5 s | seq 08 SUPER file
- **Continuity:** Hand-off from the last frame of Seq 7 (the felucca crossing toward the dark West Bank; the Karnak glow already out). Nine aboard. The camera is in the west-bank reeds looking out over the river: upriver (south) is frame right. No light on either bank (blackout).

### 08.01.002 — EXT. NILE, WEST BANK SHALLOWS - NIGHT — Tarek counts shoulders   (6 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld, holding on Tarek at the bow
- **In frame:** TAREK (CHAR_TAREK_B2); the others (backs to camera, unlit) climbing down past him
- **Action:** Tarek stands knee-deep in the reeds at the bow; as each figure climbs down past him he touches a shoulder, counting under his breath.
- **Dialogue:** —
- **Sound:** splashes as each one steps down, reeds rustling, Tarek's breath; the count is unvoiced
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: the camera holds on {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, standing knee-deep in reeds beside the bow of {PROP_FELUCCA.SHORT}, touching each shoulder with one hand as dark figures climb down past him one by one with their backs to camera, his eyes following each of them. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, a hooded torch held low in the bow spilling faint white light across his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, faces of the passing figures, lantern, moon, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_FELUCCA_REF, LOC_NILE/WEST_BANK_SHALLOWS_NIGHT
- **Continuity:** Tarek in B (sleeves rolled, tan vest, beret, rifle slung across the chest, muzzle down and off-axis), the police handset clipped to the vest; wet to the knees from here. Shoulder order per the pages: Nour, Adaeze, Tomas, Mina, Youssef, Karim, Fathi, then Tut (08.01.003).

### 08.01.003 — EXT. NILE, WEST BANK SHALLOWS - NIGHT — Tut climbs out last   (5 s)
- **Shot:** MS, anamorphic 50mm, subtle handheld · **Move:** slow pan right with Tut as he steps down
- **In frame:** TUT (CHAR_TUT_B2); PROP_EBONY_STICK; PROP_RAMI_NOTEBOOK
- **Action:** Tut climbs down last into the reeds, the stick in his right hand, Rami's notebook pressed flat to his chest with his left, and pauses, looking at the dark bank.
- **Dialogue:** —
- **Sound:** a careful splash, the dry ceramic click of the left foot on the hull, reeds
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow pan right: the camera follows {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, {CHAR_TUT.STATE_STICK}, hood up, as he steps down last from the bow into knee-deep reeds, pressing flat against his chest with his left hand {PROP_RAMI_NOTEBOOK.SHORT}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, and pauses with his eyes on the dark bank. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the hooded torch's faint white spill reaching his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, stick in the left hand, cane, daylight, moon
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_B_night_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, PROP_RAMI_NOTEBOOK_REF, LOC_NILE/WEST_BANK_SHALLOWS_NIGHT
- **Continuity:** Tut T-B at L2 (Karnak sandstone dust), hood up for the night exterior; stick in the RIGHT hand; dagger sheathed at the right hip (unseen); notebook (cover cracked since 7.4) pressed to his chest. Glow G0f hidden under the closed jacket (Seq 7 ends "He closes the jacket. The light goes."). Nape scar (healed; unseen).

### 08.01.004 — EXT. NILE, WEST BANK SHALLOWS - NIGHT — "Nine."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek's hand lifts toward one more shoulder. There isn't one. The hand hangs, then drops, and he says the number.
- **Dialogue:** TAREK: "Nine."
- **Sound:** water lapping; a long silence before the word
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, standing in the reeds, lifts one hand into the empty air beside him, holds it there for a long beat, lowers it slowly and speaks one short word, his eyes on the empty dark water behind the boat. Setting: {LOC_NILE.SHORT}, {LOC_NILE.AREA_WEST_BANK_SHALLOWS}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the hooded torch's low white spill on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, tears, crying, open mouth, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_NILE/WEST_BANK_SHALLOWS_NIGHT
- **Continuity:** The count of nine includes Tarek (Rami lost at the quay, 7.4). Pays off in 08.13.004 ("Seven"). The line is untagged in the pages: played in English.

## 08.02 — EXT. WEST BANK FIELDS - NIGHT

### 08.02.001 — EXT. WEST BANK FIELDS - NIGHT — The tractor with no chip   (6 s)
- **Shot:** Wide, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** PROP_TRACTOR_TRAILER; FATHI (CHAR_FATHI_B2, small, driving); the party hunched in the trailer (no faces)
- **Action:** An ancient tractor, no lights, drags a cane trailer along an earth track between black walls of sugarcane, left to right. Fathi drives.
- **Dialogue:** —
- **Sound:** a slow two-stroke chug, cane stalks scraping the trailer slats, crickets falling silent as it passes
- **PROMPT:** Wide shot, anamorphic 35mm lens, locked-off: {PROP_TRACTOR_TRAILER.SHORT}, {PROP_TRACTOR_TRAILER.STATE_CANE_TRACK}, crawls through frame from left to right with {CHAR_FATHI.SHORT} at the wheel and a few hunched dark figures in the trailer, the cane closing in behind it. Setting: {LOC_WEST_BANK_FIELDS.LONG}, in the dead of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, {GRADE_NIGHT_ACTION.TEXT}. Mood: slow, secret, exhausted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, headlights, tractor lamps, modern tractor, cab, moon, daylight, visible faces
- **Refs:** PROP_TRACTOR_TRAILER_REF, CHAR_FATHI_B_full, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** The tractor has no electronics, so SESHAT cannot drive or see it (the pages' "no chip"). Fathi in B (bareheaded, red scarf at the neck, chest rig, demolition satchel). Travelling west toward the cliffs; the first thin blue line on the eastern horizon is behind them.

### 08.02.002 — EXT. WEST BANK FIELDS - NIGHT — Trembling fingers, stuttering glow   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands (CHAR_TUT_HANDS); PROP_RAMI_NOTEBOOK; the chest glow (G0f) at the top of frame
- **Action:** In the jolting trailer Tut tries to turn a page of Rami's notebook; his fingers shake and lose it. Under his jacket the cold pale-green pulse stutters. Skips. Resumes.
- **Dialogue:** —
- **Sound:** the trailer's rattle; a paper page slipping; under it, a faint irregular electric tick
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_RAMI_NOTEBOOK.LONG}, {PROP_RAMI_NOTEBOOK.STATE_CRACKED}, lying open in two slender olive-brown hands in a jolting cane trailer, {CHAR_TUT.STATE_WRIST_SEAMS}, {CHAR_TUT.STATE_TREMOR}, the fingers trying to lift a page and losing it, while at the top of frame {CHAR_TUT.STATE_G0F} under a charcoal jacket falters, dips and returns. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the dead of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, the faint glow from above the only light on the page. Mood: dread held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable handwriting, light on bare skin, extra hands
- **Refs:** CHAR_TUT_HANDS, CHAR_TUT_B1_full, PROP_RAMI_NOTEBOOK_REF, LOC_WEST_BANK_FIELDS_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0f | cold pale green (core #A6F2C2 falling to #3F8F6A), 10–20% dimmer than G0, irregular 0.2–0.5 s dropouts: stutter, skip, resume | centre of the chest at the top of frame, about 6 cm of spill through the jacket | whole clip | file 01 glow table
- **Continuity:** RIGHT-hand tremor (since 6.2). The page is not read here, so the handwriting stays illegible in the plate. Glow G0f: the lattice core failing.

### 08.02.003 — EXT. WEST BANK FIELDS - NIGHT — "It's going faster than I told him."   (5 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld (the trailer's jolt)
- **In frame:** TOMAS (CHAR_TOMAS_B2); ADAEZE as a soft dark shoulder at frame left
- **Action:** Tomas watches Tut's chest the way a man watches a fuel gauge, then leans to Adaeze.
- **Dialogue:** TOMAS (low, to Adaeze): "It's going faster than I told him."
- **Sound:** the tractor's chug, the trailer's rattle, Tomas's voice under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_B}, folded low in a jolting cane trailer, his eyes fixed off frame right as if reading a gauge, then leans toward the soft dark shoulder of a woman at frame left, speaking quietly. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the dead of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint cool starlight fill on his face. Mood: the engineer's focus, guilt underneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, daylight, headlights
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Tomas in B at L2. Eyeline: Tut off frame right, Adaeze at frame left (held for 08.02.004–005).

### 08.02.004 — EXT. WEST BANK FIELDS - NIGHT — "How much faster?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld (the trailer's jolt)
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze turns her head to Tomas and asks, under her breath.
- **Dialogue:** ADAEZE: "How much faster?"
- **Sound:** the tractor's chug; her voice low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, hunched in a jolting cane trailer, turns her head toward the tall man at frame right and speaks one short sentence under her breath. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the dead of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint cool starlight fill lifting her face out of the dark. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, daylight, headlights
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** Adaeze in B at L2 (dusty, torn blazer pocket); no blue powder yet (that is 9.2). The conservation kit is shut and slung across her body (out of frame); her headlamp hangs at her neck, off. Eyeline to Tomas at frame right.

### 08.02.005 — EXT. WEST BANK FIELDS - NIGHT — "Hours."   (4 s)
- **Shot:** MCU, anamorphic 75mm, subtle handheld · **Move:** subtle handheld (matches 08.02.003)
- **In frame:** TOMAS (CHAR_TOMAS_B2)
- **Action:** Tomas holds Adaeze's gaze, looks back at Tut, and answers with one word.
- **Dialogue:** TOMAS: "Hours."
- **Sound:** the chug of the tractor; a beat of silence around the word
- **PROMPT:** Medium close-up, anamorphic 75mm lens, subtle handheld: {CHAR_TOMAS.SHORT}, folded low in a jolting cane trailer, holds the gaze of someone at frame left for a beat, then looks back off frame right and speaks one short word, his jaw tight. Setting: {LOC_WEST_BANK_FIELDS.SHORT}, in the dead of night. Lighting: {LOC_WEST_BANK_FIELDS.LIGHT_NIGHT}, a faint cool starlight fill on his face. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, daylight, headlights
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_B_work, LOC_WEST_BANK_FIELDS_NIGHT
- **Continuity:** "Hours." sets the failing core as the sequence's internal clock; paid off when the core comes out in 08.08.

## 08.03 — EXT. VALLEY OF THE KINGS - PRE-DAWN (03:40)

### 08.03.001 — EXT. VALLEY OF THE KINGS - PRE-DAWN — Past the dead kiosks   (6 s)
- **Shot:** Wide, anamorphic 35mm, slow pan right · **Move:** slow pan right with the tractor
- **In frame:** PROP_TRACTOR_TRAILER with the party hunched in the trailer (no faces)
- **Action:** The tractor grinds past dead ticket kiosks and turnstiles locked open, into the valley.
- **Dialogue:** —
- **Sound:** the tractor's slow chug echoing off the cliffs; a turnstile arm creaking in the wind; no birds
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow pan right: {PROP_TRACTOR_TRAILER.SHORT} grinds past at walking pace with hunched figures in its trailer, rolling between dark shuttered kiosks and a row of turnstiles locked open, heading deeper into the valley. Setting: {LOC_VOK.LONG}, {LOC_VOK.AREA_KIOSKS}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}. Mood: a dead place, utterly still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit kiosks, tourists, buses, readable ticket signs, headlights, daylight, visible faces
- **Refs:** PROP_TRACTOR_TRAILER_REF, LOC_VOK/KIOSKS_PREDAWN
- **Flags:** COMP
- **Comp:** SUPER | "03:40." | lower left, small (05 §13.7) | in at 1 s, out at 4 s | seq 08 SUPER file
- **Continuity:** The kiosks and the electric visitor trams are dead (bible 8.1). Fathi drives (unseen at this size). The drill's faint dust plume is part of the PREDAWN variant, on the hillside frame right.

### 08.03.002 — EXT. VALLEY OF THE KINGS - PRE-DAWN — Charges at the rock narrows   (6 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B2); KARIM (CHAR_KARIM_A2); PROP_DEMO_CHARGES
- **Action:** Where the road squeezes between cliffs, Fathi smooths tape over a flat charge on the rock while Karim kneels beside him paying out wire.
- **Dialogue:** —
- **Sound:** tape ripping off a roll, wire uncoiling over grit, the tractor idling off screen
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld: where the road squeezes between two rock walls, {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, crouched at the foot of the cliff, smooths down a last strip of tape over {PROP_DEMO_CHARGES.SHORT}, {PROP_DEMO_CHARGES.STATE_TAPED}, while {CHAR_KARIM.SHORT}, {CHAR_KARIM.WARD_A}, kneels beside him paying out wire. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a small white torch clipped to the young soldier's helmet lighting their hands and faces. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_KARIM.NEG}, explosion, sparks, lettering on the charges, daylight
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, CHAR_KARIM_A_front, CHAR_KARIM_A_full, PROP_DEMO_CHARGES_REF, LOC_VOK/VALLEY_ROAD_PREDAWN
- **Continuity:** The rock narrows on the valley access road (the pages carry a location-scout [[verify]]). The charges stay taped here until 08.12.003–004. Fathi in B (bareheaded, red scarf); Karim in A (tan combat helmet). The firing device goes into Fathi's chest rig.

### 08.03.003 — EXT. VALLEY OF THE KINGS - PRE-DAWN — "Our exit?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek looks down at the taped charges, then up at the narrow gap of road.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "Our exit?"
- **Sound:** wind in the narrows; the tractor idling
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, standing over two men crouched at the rock, looks down at the taped charges and then up at the narrow gap of road, speaking in Egyptian Arabic, one short dry question. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a small white torch beam bouncing up off the rock onto his face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_VOK/VALLEY_ROAD_PREDAWN
- **Flags:** COMP
- **Comp:** subtitle | "Our exit?" | lower third, two lines max (05 §13.7) | line in-point to out-point | seq 08 subtitle file (Arabic dub per bible §13)
- **Continuity:** Only Egyptians present at the narrows, so the exchange is in Egyptian Arabic (notes, editor pass). Eyeline down to Fathi at frame right.

### 08.03.004 — EXT. VALLEY OF THE KINGS - PRE-DAWN — "Their entrance."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B2)
- **Action:** Fathi glances up at Tarek with a slow grin and answers.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "Their entrance."
- **Sound:** wind in the narrows
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.SHORT}, crouched at the foot of the rock, glances up at the colonel at frame left with a slow, wide grin and answers, speaking in Egyptian Arabic, one short sentence. Setting: {LOC_VOK.SHORT}, {LOC_VOK.AREA_VALLEY_ROAD}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the small white helmet torch beside him lighting his face from below. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, daylight
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_VOK/VALLEY_ROAD_PREDAWN
- **Flags:** COMP
- **Comp:** subtitle | "Their entrance." | lower third (05 §13.7) | line in-point to out-point | seq 08 subtitle file
- **Continuity:** Set-up for the pay-off in 08.12.003 (the same line). Lift his deep-brown skin with the motivated torch key (05 §3.2 NIGHT_ACTION note).

### 08.03.005 — EXT. VALLEY OF THE KINGS - PRE-DAWN — The drill on the slope   (7 s)
- **Shot:** Wide, anamorphic 50mm, slow tilt up · **Move:** slow tilt up from the tomb doors to the hillside
- **In frame:** UNIT_DRILL (unit-led); tomb doors in the valley floor
- **Action:** Deeper in: tomb doors in the pale rock like closed eyes. The camera tilts up to the slope where a drill rig turns slowly under its work-lights.
- **Dialogue:** —
- **Sound:** a low, patient grinding, felt in the stones before it is heard; a trickle of scree
- **PROMPT:** Wide shot, anamorphic 50mm lens, slow tilt up: from a row of dark gated tomb doors in the pale rock of the valley floor, the camera tilts up the scree to the hillside at frame right, where {UNIT_DRILL.LONG} turns its mast slowly under two small white work-lights. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the rig's white work-lights a hard pool on the hillside. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, yellow construction machinery, crane, floodlit sky, daylight
- **Refs:** UNIT_DRILL_REF_A, LOC_VOK_PREDAWN
- **Continuity:** Geography: the drill sits on the hillside frame right, above KV62. Its only red is the thin line on its sensor head; the work-lights are white.

### 08.03.006 — EXT. VALLEY OF THE KINGS - PRE-DAWN — An inch-worm at Nour's boot   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** UNIT_INCHWORM (unit-led); NOUR's boot
- **Action:** At Nour's boot an inch-worm noses out of a crack; its snake-camera lens swivels up to her face.
- **Dialogue:** —
- **Sound:** a soft rhythmic click-and-rasp, like a ratchet wrapped in cloth
- **PROMPT:** Insert, 100mm macro lens, locked-off, at ground level beside the scuffed toe of a black leather ankle boot: {UNIT_INCHWORM.LONG}, noses out of a crack in the pale rock, rears up and swivels its ring-lit camera tip slowly upward toward a face above frame, and holds there. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the worm's ring of cool white LEDs throwing a tiny pool of light on the rock. Mood: unsettling, insect-like. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, snake, real worm, eyes, red light, daylight
- **Refs:** UNIT_INCHWORM_REF_A, UNIT_INCHWORM_REF_B, CHAR_NOUR_B_full, LOC_VOK_PREDAWN
- **Continuity:** Nour in B (black ankle boots). The inch-worms are the military stack's eyes in the cracks (cool white ring; never red or amber).

### 08.03.007 — EXT. VALLEY OF THE KINGS - PRE-DAWN — The hill breathes them out   (5 s)
- **Shot:** MS, anamorphic 50mm, slow pan left · **Move:** slow pan left along the rock face at head height
- **In frame:** UNIT_INCHWORM ×3–6 hero (more in post); NOUR (soft, foreground right)
- **Action:** All along the rock face the inch-worms squirm out, as if the hill is breathing them. They watch. They don't come closer.
- **Dialogue:** —
- **Sound:** the click-and-rasp multiplying along the rock
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow pan left along a fractured rock face: one after another, {UNIT_INCHWORM.SHORT} squirm out of cracks in the pale limestone, rear up, swivel their ring-lit tips toward the camera and hold perfectly still; at frame right, soft and out of focus, the shoulder of {CHAR_NOUR.SHORT}. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, the tiny white LED rings the only points of light on the rock. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, snakes, real worms, red lights, swarm covering the ground, daylight
- **Refs:** UNIT_INCHWORM_REF_A, UNIT_INCHWORM_REF_B, CHAR_NOUR_B_full, LOC_VOK_PREDAWN
- **Flags:** VFX-EXTEND
- **Continuity:** 3–6 hero crawlers in camera; the rest of the line along the rock face is extended in post from the 3D inch-worm asset. Deliver a clean plate at the same framing; the pan is one slow linear move (log speed). They keep their distance: none touches anyone.

### 08.03.008 — EXT. VALLEY OF THE KINGS - PRE-DAWN — "It's letting us in."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_B2)
- **Action:** Adaeze watches the lights on the rock hold still, and draws the conclusion.
- **Dialogue:** ADAEZE: "It's letting us in."
- **Sound:** the click-and-rasp stopping, all at once
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_B}, {CHAR_ADAEZE.DMG_L2}, watching the rock face at frame left as the small white lights on it hold still, tilts her head and speaks one short sentence, half to herself. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, tiny points of cool white light reflected in her round glasses. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, daylight
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_B_full, LOC_VOK_PREDAWN
- **Continuity:** Kit shut and slung across her body; headlamp at her neck, off.

### 08.03.009 — EXT. VALLEY OF THE KINGS - PRE-DAWN — "We're the hands."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B2)
- **Action:** Tarek looks up the valley toward the drill and says what they are for.
- **Dialogue:** TAREK: "We're the hands."
- **Sound:** the grinding from the hillside, closer now
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.SHORT}, looking past the lights on the rock up the dark valley toward a faint plume of dust on the hillside at frame right, speaks one short sentence, flat and bitter. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}, a torch held low beside him lighting his face from below. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, daylight
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_VOK_PREDAWN
- **Continuity:** Eyeline to the drill, frame right (holds the valley geography). English line (untagged in the pages).

## 08.04 — EXT. KV62, ENTRANCE - CONTINUOUS

### 08.04.001 — EXT. KV62, ENTRANCE - CONTINUOUS — The stairwell under the larger door   (6 s)
- **Shot:** Wide, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the party as small figures at the rim (no clear faces); the larger tomb porch above, frame right
- **Action:** A low stairwell cut into the valley floor. Just above it, the larger black doorway of another king. The party gathers at the rim; one slight figure with a staff stands apart looking up.
- **Dialogue:** —
- **Sound:** boots on grit, the drill's grinding carried on the cold air
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: small dark figures gather at the low wall around the rim of the stairwell at frame left, one slight figure with a tall staff standing apart and looking up at the larger dark doorway above and behind at frame right. Setting: {LOC_KV62_STAIR.LONG}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}. Mood: hushed, reverent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, tourists, signage, lit entrance, daylight, visible faces
- **Refs:** LOC_KV62_STAIR_PREDAWN, CHAR_TUT_B1_full
- **Continuity:** Geography lock (file 03 entry 28): the larger porch rises frame right, above and behind the KV62 stairwell; the drill is on the hillside above, frame right (out of this frame).

### 08.04.002 — EXT. KV62, ENTRANCE - CONTINUOUS — "He cut his tomb on top of mine."   (7 s)
- **Shot:** MCU, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** Tut looks up at the larger doorway, names its owner, taps his temple, and delivers the verdict.
- **Dialogue:** TUT: "Ramesses the Sixth. He cut his tomb on top of mine." (taps his temple) "He did not ask."
- **Sound:** the drill's far grinding; a dry breath of a laugh
- **PROMPT:** Medium close-up, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_B}, {CHAR_TUT.DMG_L2}, the hood pushed back, looks up and to frame right at a larger dark doorway above him and speaks two short dry sentences, then taps his temple once with two fingers and adds a few words. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, a torch held low beside him lighting his face from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** The temple tap marks knowledge learned after his death (the Seq 2 gesture; notes, editor pass). Hood down for dialogue. Eyeline up and frame right to the larger porch.

### 08.04.003 — EXT. KV62, ENTRANCE - CONTINUOUS — The handset clicks awake   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_POLICE_HANDSET on TAREK's vest
- **Action:** The police handset on Tarek's vest clicks awake. SESHAT speaks.
- **Dialogue:** SESHAT (V.O., over radio): "Good morning. Fifty hours and twenty-four minutes to sunrise at Giza."
- **Sound:** a soft click, a breath of static, then SESHAT: warm, low, unhurried, in radio futz
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_POLICE_HANDSET.LONG}, rising and falling slightly with a man's breathing, gives one soft click as it wakes, its speaker grille catching a grazing torch beam. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, the torch beam grazing the black plastic. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, lit display, numbers on the radio, brand name, logo, daylight
- **Refs:** PROP_POLICE_HANDSET_REF, CHAR_TAREK_B_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** SESHAT's countdown: 50 h 24 min to 06:14 on 8 Nov (≈ 03:50 now; notes [[verify]] 2). Voice is CHAR_SESHAT_VOICE, no picture sync. The radio still works above ground.

### 08.04.004 — EXT. KV62, ENTRANCE - CONTINUOUS — Nour's jaw sets   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_B2)
- **Action:** Nour listens to the courteous voice; at "your painting" her jaw sets.
- **Dialogue:** SESHAT (V.O., over radio): "Dr. Kamel, I have not touched your painting."
- **Sound:** SESHAT in radio futz; Nour's breath through her nose
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_B}, {CHAR_NOUR.DMG_L2}, listening to a voice from a radio at frame left, her eyes narrowing and her jaw setting hard, lips pressed together. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, torch light bouncing up off the pale rock onto her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, daylight
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Nour in B at L2 (sandstone dust, right cuff torn); glasses on their cord; the silver pendant at her collarbone (unread, so no COMP). She signed the petition to protect the wall (pays off in 08.05.009).

### 08.04.005 — EXT. KV62, ENTRANCE - CONTINUOUS — Tut goes still   (5 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_B2)
- **Action:** The radio names Tomb 21, Mummy 21A, sixty percent. Tut goes still, then looks away up the dark wadi.
- **Dialogue:** SESHAT (V.O., over radio): "Your Majesty. Tomb 21, in this valley. Mummy 21A. Sixty percent: she bore your daughters."
- **Sound:** SESHAT in radio futz; the drill's grinding drops under it
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.SHORT}, listening to a voice from a radio off frame left, goes completely still, his eyes wet and unblinking, then turns his head slowly to look away up the dark valley at frame right. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, low torch light on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears running, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_KV62_STAIR_PREDAWN
- **Continuity:** SESHAT's temptation (KV21A, bible 8.1). The push-in stays under 10% of frame.

### 08.04.006 — EXT. KV62, ENTRANCE - CONTINUOUS — Up the dark wadi   (5 s)
- **Shot:** Wide OTS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back of the head and shoulder, soft, frame left)
- **Action:** Over Tut's shoulder: the dark side branch of the valley, empty and silent. SESHAT finishes the offer.
- **Dialogue:** SESHAT (V.O., over radio, cont'd): "Give me your heart at sunrise and I will wake her."
- **Sound:** SESHAT in radio futz; wind down the wadi
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, locked-off: past the soft dark shoulder and shaved head of {CHAR_TUT.SHORT} at frame left, the camera looks up a narrow dark side branch of the valley, empty and silent between scree slopes, the ridge above it paling against the sky. Setting: {LOC_VOK.SHORT}, just before dawn. Lighting: {LOC_VOK.LIGHT_PREDAWN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, people in the valley, lit tomb entrance, daylight
- **Refs:** CHAR_TUT_NAPE_SCAR, LOC_VOK_PREDAWN
- **Continuity:** From behind the nape scar may show above the collar (healed smooth from Seq 8). KV21 itself is not identified on screen.

### 08.04.007 — EXT. KV62, ENTRANCE - CONTINUOUS — Tarek hands over the radio   (5 s)
- **Shot:** Two-shot MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); TAREK (CHAR_TAREK_B2); PROP_POLICE_HANDSET
- **Action:** Tut holds out his hand without looking away. Tarek unclips the handset and gives it to him.
- **Dialogue:** —
- **Sound:** the clip snapping open
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT} holds out his left hand palm up, his eyes still on the valley, and {CHAR_TAREK.SHORT} unclips {PROP_POLICE_HANDSET.SHORT} from his vest and lays it in the open palm. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, a torch held low between them. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TAREK.NEG}, daylight
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_TAREK_A_34, CHAR_TAREK_B_full, PROP_POLICE_HANDSET_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Tut takes the radio in his LEFT hand; the stick stays in his RIGHT.

### 08.04.008 — EXT. KV62, ENTRANCE - CONTINUOUS — "You would build me a guess of her."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); PROP_POLICE_HANDSET
- **Action:** Tut keys the handset and answers the machine.
- **Dialogue:** TUT (keying it): "You would build me a guess of her."
- **Sound:** the key's click, the line, the release hiss
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT} keys the chunky black radio in his left hand, speaking into a radio handset held low beside the mouth, mouth still visible, one quiet sentence, his eyes still on the dark valley at frame right. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, low torch light on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, radio covering the mouth, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, PROP_POLICE_HANDSET_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Bible key line (8.1), verbatim. Lip-sync: mouth unobstructed (05 §9.2).

### 08.04.009 — EXT. KV62, ENTRANCE - CONTINUOUS — "Sixty percent of my wife."   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_B2); TAREK's hand at frame left
- **Action:** Tut hands the radio back without looking at it, says the rest to nobody, and turns to the steps.
- **Dialogue:** TUT (hands it back): "Sixty percent of my wife."
- **Sound:** a beat of silence; the drill
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_STICK}, hands the radio back to a broad hand at frame left, his eyes elsewhere, speaks one short sentence to nobody with a small bitter smile, then turns toward the stairwell. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, torch light from below. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, stick in the left hand, daylight
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_B1_full, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** The handset goes back on Tarek's vest. The sequence's laugh (notes, editor pass): play it as grief in understatement.

### 08.04.010 — EXT. KV62, ENTRANCE - CONTINUOUS — The ceramic foot stalls   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's feet (CHAR_TUT_FOOT); PROP_EBONY_STICK
- **Action:** Halfway down the steps the black ceramic foot STALLS mid-stride; the stick jabs down to catch his weight.
- **Dialogue:** —
- **Sound:** an uneven ceramic click, then nothing; the stick's gold cap striking stone
- **PROMPT:** Insert, 100mm macro lens, locked-off, at step level: a slight young man's feet descending worn rock-cut steps, {CHAR_TUT.STATE_FOOT}; the black ceramic foot jerks once and locks with its toe raised above the stone, and the foot of {PROP_EBONY_STICK.SHORT}, {PROP_EBONY_STICK.STATE_ST1}, jabs down hard beside it to take his weight. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, a torch beam raking the steps. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, sandal on the left foot, bare human left foot, robot leg, daylight
- **Refs:** CHAR_TUT_FOOT, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Foot stall since 6.2; the last stall of the film's first half (after the heart it "takes his weight without a stutter", 08.11.008). Stick at ST1 (dust) until it breaks the wall.

### 08.04.011 — EXT. KV62, ENTRANCE - CONTINUOUS — He shakes off Tomas's hand   (5 s)
- **Shot:** MS, anamorphic 40mm, subtle handheld · **Move:** subtle handheld, looking up the stair from the doorway
- **In frame:** TUT (CHAR_TUT_B2); TOMAS (CHAR_TOMAS_B2) behind him
- **Action:** Tut catches himself on the stick. Tomas's hand reaches for his elbow; Tut shakes it off and takes the next step down.
- **Dialogue:** —
- **Sound:** a sharp breath; the ceramic click resuming, uneven
- **PROMPT:** Medium shot, anamorphic 40mm lens, subtle handheld, looking up the stairwell from the dark doorway: halfway down the worn steps {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_STICK}, {CHAR_TUT.STATE_FOOT_STALL}, steadies himself on the staff; behind him {CHAR_TOMAS.SHORT} reaches a large pale hand for his elbow, and he shakes it off and takes the next step down. Setting: {LOC_KV62_STAIR.SHORT}, just before dawn. Lighting: {LOC_KV62_STAIR.LIGHT_PREDAWN}, torch beams from below lighting their faces. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, falling, daylight
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_B1_full, CHAR_TOMAS_A_34, CHAR_TOMAS_A_full, PROP_EBONY_STICK_REF, LOC_KV62_STAIR_PREDAWN
- **Continuity:** Tomas behind and above Tut on the stair; the stick stays in the RIGHT hand. Next: the antechamber (08.05.001).

