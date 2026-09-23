# SEQUENCE 09 — THE FATHER — shot list and AI-video prompts

**HERE AM I** · end of Act Two (B) · screenplay `screenplay/sequences/seq_09.fountain` (pp. 74–92) · notes `screenplay/notes/seq_09_notes.md` · 6 Nov 2033, 11:20 → 7 Nov, 06:06 · the Luxor rail yard, the night train, Deir Mawas, Amarna, the Amarna memory (c. 1336, 1332 and 1330 BC), the quarry.

**Format:** 1920×1080, 16:9, 24 fps, clips of 4–8 s. Every PROMPT follows file 05 §5.1 (house pattern, one LONG lock at most) and ends with `{SUFFIX}`; every NEGATIVE starts with `{NEG}`. Tokens expand from `production_bible/locks.json` via `tools/shots_md2jsonl.py`.

**Shot count:** 4 · **Total running time:** 0:20 (20 s, 0.3 min) · **Page estimate:** 16.2–18 pp (the notes' table sums 17.8 pp without the deleted scene 1; the pace review's rebuilt PDF after the applied cuts gives 16.2 pp; bible target 18 pp), so the running time sits inside ±15% of every one of these figures.

**Scene numbering (CC):** CC is the scene number in the notes' scene table. Scene 1 of that table (EXT. NILE, LUXOR EAST BANK - DAY) was deleted in the editor pass, so this sequence has no 09.01 shots and runs 09.02 → 09.27: 26 scene headings, 26 scene numbers.

| CC | Heading | Shots | Seconds |
|---|---|---|---|
| 02 | EXT. LUXOR RAILWAY YARD - DAY | 4 | 20 |

**Sequence rules applied here**
- **Grades:** the rail yard by day GRADE_2033_DAY (no desert filter); the night train, Deir Mawas and the ferry GRADE_NIGHT_ACTION in post (the variant phrase carries the look, so the prompt phrase is left out); the Amarna Garden GRADE_GARDEN; the memory GRADE_1336 (1336 and 1330 BC) and GRADE_1332_NIGHT (the barge, the Gallery, the Hall), each with GRADE_READ_FROM_GLASS added in post only (05 §13.1); the quarry dawn has no grade token (LOC_QUARRY_DAWN carries it).
- **Geography:** rail yard: the shed at frame left, the diesel on the far siding at frame right facing north (frame left). Night train and Deir Mawas: north is frame left, the train enters from frame right, the jackal comes forward right to left, flies chase from frame right; the stelae are across the river to the east (background). The Nile memory: upriver (south) frame right, so the barge glides frame left. Amarna Garden: the rows run away from camera toward the cliffs; Tut walks down a row toward camera; the father and the drone come from the far (north) end; the ferry path is behind camera. Grand Gallery: "up" is away from camera. Hall: the left-hand pan is the one that takes the vessel.
- **Continuity in (end of Seq 8):** party of seven off the farmer's boat; Tut T-B at L2, glow G1 (the vessel seated, wax serpent and papyrus band on its seal), nape scar, stick in the RIGHT hand, dagger sheathed at the belt, Rami's notebook; Adaeze carries the conservation kit (one Egyptian-blue jar, full); Tarek the police handset on his vest; Fathi the red scarf at his throat.
- **Continuity out (end of Seq 9):** party of six under the tarp at the quarry (Tut, Tarek, Fathi, Adaeze, Youssef, Karim); Nour, Tomas, the father and the Reis flown north. Tut: LEFT wrist seam cracked (09.19), G1, stick, dagger unused, notebook open at Q.100 with nothing written under it. Fathi's scarf back at his throat (09.17). Adaeze's jar half full, blue powder on her fingers and blazer. The Reis at R4 (Tarek's round, 09.25). Tarek's handset battery back in (09.06).
- **Safety:** nobody dies in this sequence. Every round hits a machine or the environment (sparks off the jackal's shell, sparks off the diesel's handrail, ceramic chips off the Reis). Rifles across the body, muzzles off-axis, never toward the lens. The derailment shows no face in the crash itself. Minors: the child king is touched only by the queen; the sisters are small linen-covered shapes far back, never touched; every Garden sleeper is an adult. The mother's gift is hands, fabric, light and the glass vessel only (NEG_REMAINS). No banned word in any prompt; nobody is named in a prompt.
- **COMP in this sequence:** SUPER cards (11:20, 22:04, 23:10, c. 1336 / 1332 / 1330 BC, 06:06); subtitles for every Egyptian Arabic, Late Egyptian and Middle Egyptian line and for the whisper; the mouthed "It will fail." (italics); the chest glow G1 (ember under the scarf 09.03–09.17) and its flare; the wrist-seam crack; the jackal's near-infrared and thermal POVs; the CALMING FLORA placard; the red target marks and the slits going dark; the cartouche change on the palette; the PLAN A card and Rami's handwriting.

## 09.02 — EXT. LUXOR RAILWAY YARD - DAY

Geography before the hide-and-seek: the shed (frame left) with the dead modern trainset over the inspection pit, forty metres of open ballast, the scrap row and the chalky 1970s diesel on the far siding (frame right, facing north = frame left). A jackal checks the parked coaches door by door. The party is already hidden in the pit (unseen).

### 09.02.001 — EXT. LUXOR RAILWAY YARD - DAY — The yard, the shed, the scrap and the diesel   (7 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1 (small, foreground); PROP_DIESEL_LOCO (far siding, frame right); the maintenance shed (frame left)
- **Action:** Across the sun-bleached sidings: the long open shed at frame left, forty metres of open ballast, the scrap row and the chalky diesel at frame right; small in the foreground a jackal walks the parked coaches, pausing at each door.
- **Dialogue:** —
- **Sound:** heat tick of steel rails, a far dog, cicadas; the jackal's soft pad-taps; no voices
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: the camera looks across sun-bleached sidings to a long open shed at frame left and, beyond forty metres of open ballast at frame right, a row of rusting scrap where {PROP_DIESEL_LOCO.SHORT}, {PROP_DIESEL_LOCO.STATE_T0}, faces frame left; small in the foreground {UNIT_JACKAL.SHORT} walks along the parked coaches from right to left, pausing at each door. Setting: {LOC_LUXOR_RAIL_YARD.LONG}, at midday. Lighting: {LOC_LUXOR_RAIL_YARD.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, soldiers, running figures, lit screens, moving trains, second robot
- **Refs:** LOC_LUXOR_RAIL_YARD_DAY, UNIT_JACKAL_REF_A, PROP_DIESEL_LOCO_REF
- **Flags:** COMP
- **Comp:** SUPER | "6 NOVEMBER. 11:20." | lower left, small, the subtitle family (05 §13.7) | in at 1 s, out at 5 s | seq 09 SUPER file
- **Continuity:** Opens Seq 9 at 11:20 on 6 Nov (Seq 8 hands off on the farmer's boat with "The railway yard."). Geography lock for the whole yard: shed frame left, diesel frame right facing north (frame left). Jackal D0. The party of seven is already in the pit, unseen. The diesel is PROP_DIESEL_LOCO T0 (no plates, the pale maker's-plate rectangle).

### 09.02.002 — EXT. LUXOR RAILWAY YARD - DAY — The unlit trainset over the pit   (4 s)
- **Shot:** WS, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** the maintenance shed interior; the modern trainset (dark)
- **Action:** Inside the open-ended shed a sleek modern trainset sits unlit over a concrete inspection trench, its cab windows and screens black; hard daylight blazes at both open ends.
- **Dialogue:** —
- **Sound:** wind booming softly in the corrugated roof, pigeons shifting on the rafters
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: the camera looks down the length of a long open-ended shed where a sleek modern trainset sits unlit and silent over a narrow concrete trench, its cab windows and small screens black, blades of hard daylight blazing at both open ends and dust hanging in the sunbeams. Setting: {LOC_LUXOR_RAIL_YARD.SHORT}, at midday. Lighting: {LOC_LUXOR_RAIL_YARD.LIGHT_DAY}, sunbeams slanting through gaps in the corrugated roof. Mood: hushed and watchful. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people, glowing screens, lit headlights, logos on the train, readable train numbers
- **Refs:** LOC_LUXOR_RAIL_YARD_DAY, LOC_LUXOR_RAIL_YARD/INSPECTION_PIT_DAY
- **Continuity:** The dead modern trainset: its screens black (no content, so no COMP). The trench beneath it is the inspection pit where the party hides (09.03). Shed axis runs frame left to right in the master.

### 09.02.003 — EXT. LUXOR RAILWAY YARD - DAY — The jackal checks a coach door   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL ×1; a parked passenger coach
- **Action:** At an open coach door the jackal stops, dips its narrow head inside, withdraws, and walks on to the next door.
- **Dialogue:** —
- **Sound:** soft pad-taps on ballast, a faint high servo whisper as the head dips; the heat tick of the rails
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: beside the open door of a faded parked coach, {UNIT_JACKAL.LONG}, stops, dips its narrow head into the dark doorway, holds, withdraws, and walks on to the next door at frame left. Setting: {LOC_LUXOR_RAIL_YARD.SHORT}, at midday. Lighting: {LOC_LUXOR_RAIL_YARD.LIGHT_DAY}, {GRADE_2033_DAY.TEXT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people, second robot, sniffing like a dog, wagging tail, weapon facing camera
- **Refs:** UNIT_JACKAL_REF_A, UNIT_JACKAL_REF_B, LOC_LUXOR_RAIL_YARD_DAY
- **Continuity:** Jackal D0, moving right to left along the coaches ("Car. Car. Car."). Its weapon module is flush along the spine, never toward the lens.

### 09.02.004 — EXT. LUXOR RAILWAY YARD - DAY — The red line never flickers   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** UNIT_JACKAL (sensor head)
- **Action:** Close on the sensor head as it draws back out of a dark doorway into the sun: the thin red line holds steady.
- **Dialogue:** —
- **Sound:** a tiny servo whisper; silence
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the narrow snout-like sensor head of {UNIT_JACKAL.SHORT} draws slowly back out of a dark coach doorway into hard sunlight and turns toward frame left, its thin red line perfectly steady. Setting: {LOC_LUXOR_RAIL_YARD.SHORT}, at midday. Lighting: {LOC_LUXOR_RAIL_YARD.LIGHT_DAY}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, eyes, ears, face, flickering light, laser beam
- **Refs:** UNIT_JACKAL_REF_A, LOC_LUXOR_RAIL_YARD_DAY
- **Continuity:** The red line is steady (not targeting). The turn to frame left leads the eye along the coaches, away from the shed.
