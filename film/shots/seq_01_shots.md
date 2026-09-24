# HERE AM I — SEQUENCE 1: "THE HEART" — shot list and AI-video prompts

Screenplay pages 1–8 (`screenplay/seq_01.fountain`) · photoreal live-action AI video, 1920×1080, 16:9, 24 fps · clips of 4–8 s.
Every PROMPT and NEGATIVE below uses `{TOKEN}` / `{TOKEN.FIELD}` fixed wording expanded by `shots_md2jsonl.py` from `production_bible/05` and `production_bible/locks.json`. Nothing inside a lock was typed by hand.

## Header

**Scenes and shot ranges**

| Scene | Heading | Shots | Clips | Running time |
|---|---|---|---|---|
| 01.01 | BLACK + INT. HOUSE OF EMBALMING - NIGHT (Thebes, c. 1323 BC) | 01.01.001–017 | 17 | 1:42 |
| 01.02 | INT. KV62, BURIAL CHAMBER - NIGHT (seventy days later) | 01.02.001–015 | 15 | 1:29 |
| 01.03 | INT. KV15 (THE TOMB OF SETI II, USED AS A LAB), OUTER CORRIDOR - DAY (11 Nov 1925) | 01.03.001–020 | 20 | 1:44 |
| 01.04 | INT. LIVERPOOL X-RAY ROOM - NIGHT (1968) | 01.04.001–005 | 5 | 0:26 |
| 01.05 | INT. GEM CONSERVATION CENTRE, MUMMY LAB - NIGHT (1 Nov 2033) | 01.05.001–033 | 33 | 2:56 |
| 01.06 | MAIN TITLES - SESHAT'S WORLD | 01.06.001–013 | 13 | 1:11 |
| **Total** | | | **103 shots** | **9:28 (568 s)** |

Page count 8 → target 8:00 ±20% (6:24–9:36); this list runs 9:28 (+18%), carried by the four eras plus the title montage. Average clip 5.5 s. Flags: COMP 32 · VFX-EXTEND 3 · VFX-ASSIST 1 · EXTEND 1 (01.05.021 ← 01.05.020).

**Camera plan (file 05 §4.4).** Prologue 1.1–1.4: still, painterly tableaux, locked-off and slow push-ins; the camera watches faces and hands, never the centre of the table. 1925 is tripod-height and static, like the photographer's. 1.5: clinical symmetry, one top-down on the cradle, one slow push-in to the eyes, no handheld. Main titles: documentary handheld for the 2025 archive only, then the film look snaps back.

**Grades.** 1.1–1.2 GRADE_1323 · 1.3 GRADE_1925 (generate in natural colour, desaturate in post; no sepia words in prompts) · 1.4 GRADE_1968 · 1.5 GRADE_2033_MUSEUM · 1.6 GRADE_ARCHIVE_2025 → GRADE_2033_MUSEUM / GRADE_2033_DAY · muon vision and cards are COMP. Grade phrases are optional in prompts (file 05 §3) and are left out wherever the file 03 lighting variant already carries the look (1.1, 1.2, 1.4); they are kept only where they add something (the 2033 day re-light, 01.06.004; ATEN-1, 01.06.009). The grades are applied in post.

**Match cuts.** 01.03.020 (Burton's flash, lantern at upper frame centre, table on the frame's long axis) → 2 white frames → 01.04.001 (lightbox white) … 01.04.005 (the tube's last flare) → 01.05.001 (the gantry projector's white burst; projector ring where the lantern hung; cradle on the table's axis) (file 05 §13.6).

**Reference stills needed** (approve and freeze before generation; file 05 §12 steps 1–3)
- Characters: CHAR_TUT_BODY_1323 · CHAR_TUT_CRADLE_2033 · CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_profile (face for the eyes/mouth close-ups at the sheet line) · CHAR_AY_A_front, CHAR_AY_A_34, CHAR_AY_A_profile, CHAR_AY_A_full, CHAR_AY_B_full · CHAR_ANKHESENAMUN_A_front, CHAR_ANKHESENAMUN_A_34, CHAR_ANKHESENAMUN_A_profile, CHAR_ANKHESENAMUN_A_full · CHAR_LECTOR_1323_A_front, CHAR_LECTOR_1323_A_34, CHAR_LECTOR_1323_A_full · CHAR_EMBALMER_JACKAL_A_full, CHAR_EMBALMER_JACKAL_A_34 · CHAR_CARTER_1925_A_front, _34 · CHAR_DERRY_1925_A_front, _34 · CHAR_HAMDI_1925_A_front, _34 · CHAR_BURTON_1925_A_front, _full · CHAR_IBRAHIM_1925_A_front, _34, _full · CHAR_RADIOLOGIST_1968_A_front, _34 · CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full · CHAR_TOMAS_A_front, CHAR_TOMAS_A_full · CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_full · CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_A_full · CHAR_TAREK_A_front, CHAR_TAREK_A_full · CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full.
- Units: UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B · UNIT_EARLY_HUMANOID_REF · UNIT_ATEN1_CAMPUS_REF_A · UNIT_GLYPH_SESHAT (COMP vector, file 02 §8.1).
- Props: PROP_HEART_VESSEL_REF (plus a 1.1 variant with the wax serpent and papyrus band painted out, see lock gaps) · PROP_EBONY_STICK_REF · PROP_JACKAL_MASK_REF · PROP_IRON_ADZE_1323_REF · PROP_CORNFLOWER_WREATH_REF · PROP_LAMP_1925_REF (lit, 1925) and an unlit 2033 variant · PROP_BURTON_PLATES_REF · PROP_CUTMAP_PROJECTION_REF (COMP asset) · PROP_NANO_ADZE_REF · PROP_RAMI_NOTEBOOK_REF.
- Plates: LOC_EMBALMING_1323_NIGHT_plate (+ NIGHT_LOW) · LOC_KV62_BURIAL_1323_NIGHT_plate (+ LAMP_CLOSE; RUBBLE and NORTH_WALL_FRESH state plates) · LOC_KV62_NORTH_CORRIDOR and LOC_KV62_HEART_CHAMBER 1323 derivations (clean, fresh plaster; see lock gaps) · LOC_KV15_LAB_1925_DAY_plate (+ TREMBLE, FLASH) · LOC_XRAY_1968_NIGHT_plate · LOC_GEM_CC_READING_plate (+ NIGHT; observation-room reverse plate) · LOC_ROBOT_HALF_MARATHON_ARCHIVE_plate · LOC_TITLES_KITCHEN_NIGHT_plate · LOC_TITLES_WARD_DAY_plate · LOC_TITLES_PORT_DUSK_plate · LOC_GIZA_PLATEAU night plate (starlight, no floodlights) · LOC_GP_GRAND_GALLERY reference plate (texture for the 3D muon render).
- Voice first (file 05 §9.1): the Middle Egyptian lines (lector, Ay, Nour) and the Late Egyptian lines (embalmer, Ay, Tut's four syllables) recorded with the Egyptologist consultant before picture; Hamdi's Egyptian Arabic line by a native speaker; SESHAT's voice actor.

**Lock gaps flagged for the lead** (the shots below work around them; none of the fixed wording was edited)
1. `PROP_HEART_VESSEL` LONG/SHORT describe the 1.2 seal (wax serpent, papyrus band). In 1.1 the jar is first open, then sealed with plain resin. Open-jar shots use the writer's words; the sealed 1.1 shots (01.01.016) use the V_1323 state add-ons with a writer's noun phrase, never the LONG/SHORT. Proposal: add a `STATE_V_1323_OPEN` and a serpent-free 1.1 SHORT.
2. `PROP_LAMP_1925` LONG/SHORT say "burning a warm amber flame"; its `STATE_COLD_2033` says unlit. The 2033 shots use a writer's noun ("an old hurricane lantern") plus the COLD state. Proposal: a 2033 SHORT without the flame.
3. `CHAR_TUT_CRADLE_2033` says "eyes closed" and carries the gold neck ring before the seam is drawn. Pre-seam shots keep the neck ring as a comp light element held dark until 01.05.013 (§13.9). After the eyes open (01.05.020 on) the shots use `CHAR_TUT` with the sheet in the writer's words.
4. `LOC_KV62_NORTH_CORRIDOR` and `LOC_KV62_HEART_CHAMBER` are 2033 states (rubble, cracked old plaster, torches). 01.02.011–012 describe the 1323 corridor and chamber in the writer's words and use those tokens only as geometry refs.
5. The muon vision (01.06.010–012) is a 3D render (file 05 §13.8); the prompts there generate background and texture plates only.

**QA pass (prompt QA lead, repaired in place)**
- Coverage: added 01.03.006 (Derry's nod: "He looks at Derry. Derry nods.") and renumbered 01.03.006–019 → 007–020; 01.02.004 is now an objective shot, not her POV, so the screenplay order holds (the lamplight finds the box, then she does not look, then she does); 01.02.006 now touches the mouth and each eye.
- Locks/states: the 1.2 vessel shots use the sealed state `STATE_V_1323_SEALED` ("carried low in both hands") and are re-staged to match (lamp set at the opening's lip); 01.05.008 is unit-led, so UNIT_SHABTI goes LONG; 01.05.033 carries Tut's G0 overlay under its glow comp; Tut's 1.5 state (G0, nape port unseen, no cracks) is noted at 01.05.020. The wardrobe pastes that repeated a LONG lock word for word (lector, the 1925 team, the 1968 radiologist) are dropped after LONG and kept after SHORT.
- Header: the scene table, totals and the muon-vision shot range (01.06.010–012, lock gap 5) are corrected.
- Clips: 01.03.020 goes from 3 s to 4 s; 01.06.003 is 8 s for its three beats; 01.05.028 is cut to one beat.
- Readability: commas after locks that end without punctuation; the ATEN-1, jackal-mask and notebook sentences rebuilt so that the locks sit mid-sentence; redundant grade phrases removed.
- The parser reports 0 errors.

## 01.01 — BLACK + INT. HOUSE OF EMBALMING - NIGHT (Thebes, c. 1323 BC)

### 01.01.001 — House of Embalming — Black; the heartbeat   (6 s)
- **Shot:** Extreme close-up, anamorphic 50mm, near-black plate · **Move:** locked-off
- **In frame:** none (near-black plate: lamp smoke in darkness)
- **Action:** Black. The opening card. A slow, deep heartbeat, then another; in the last second a wisp of lamp smoke catches a faint amber edge.
- **Dialogue:** —
- **Sound:** a HEARTBEAT, slow, deep, patient; a second beat; the hush of a still night room
- **PROMPT:** Extreme close-up, anamorphic 50mm lens, locked-off: near-total darkness, a thin wisp of lamp smoke drifting slowly upward through blue-black shadow, its edge catching the faintest amber glow from a flame out of frame. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: patient, hushed, expectant. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, visible flame, bright light, faces, figures
- **Refs:** LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** opening card | "All modern characters and events are fictional. Imagery generated with AI." | centred, small, white on black (§13.7) | 0:00.5 → 0:04.5, 12-frame fades | seq 01 cards file
- **Continuity:** Graded down to black under the card; the smoke reads only in the last second. The heartbeat carries across the cut into 01.01.002.

### 01.01.002 — House of Embalming — Establishing: the workshop at night   (8 s)
- **Shot:** Wide establishing shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** EMBALMER (CHAR_EMBALMER_JACKAL_A, back to camera), LECTOR (CHAR_LECTOR_1323_A, far end), the body under linen (CHAR_TUT_BODY_1323)
- **Action:** Across the low table the masked embalmer bends over the linen with his back to camera; at the far end the lector stands reading from the roll; lamp smoke drifts between them.
- **Dialogue:** —
- **Sound:** the heartbeat fading under lamp crackle; linen parting; a blade laid down on stone (off-screen); a breath held inside clay
- **PROMPT:** Wide establishing shot, anamorphic 32mm lens, locked-off: across the low table {CHAR_EMBALMER_JACKAL.SHORT} bends over the linen with his back to camera, his hands hidden below the table edge, while at the far end {CHAR_LECTOR_1323.SHORT} stands reading from the open roll, lamp smoke drifting between them. Setting: {LOC_EMBALMING_1323.LONG}, {LOC_EMBALMING_1323.STATE_BODY}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_EMBALMER_JACKAL.NEG}, {CHAR_LECTOR_1323.NEG}, blades in frame, instruments, coffins, carved walls, the embalmer's face
- **Refs:** LOC_EMBALMING_1323_NIGHT, CHAR_EMBALMER_JACKAL_A_full, CHAR_LECTOR_1323_A_full, CHAR_TUT_BODY_1323, PROP_JACKAL_MASK_REF
- **Flags:** COMP
- **Comp:** SUPER | "THEBES. c. 1323 BC." | lower left, small (§13.7) | 0:01 → 0:05 | seq 01 SUPER file
- **Continuity:** Geography lock (file 03): table across frame, embalmer back to camera, door with its linen screen at frame right, lamp niches on the back wall. Lighting NIGHT. The body: linen to the collarbones, face turned away into shadow; arms under the linen.

### 01.01.003 — House of Embalming — The boy under linen   (6 s)
- **Shot:** Medium close-up, anamorphic 50mm · **Move:** slow push-in
- **In frame:** the body (CHAR_TUT_BODY_1323)
- **Action:** The camera drifts toward the young face in profile, half lost in shadow; lamp smoke crosses the frame; a flame beside him wavers once.
- **Dialogue:** —
- **Sound:** lamp crackle; the embalmer's slow work off-screen; no music
- **PROMPT:** Medium close-up, anamorphic 50mm lens, slow push-in: the camera drifts toward {CHAR_TUT_BODY_1323.LONG}, a thin veil of lamp smoke crossing the frame as the small flame beside him wavers once and steadies. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, hands on the body, embalmer in frame, open eyes, bare chest, visible arms
- **Refs:** CHAR_TUT_BODY_1323, LOC_EMBALMING_1323_NIGHT
- **Continuity:** The face stays in profile and in shadow; linen at the collarbones; no seams (this is before 1925). The push ends before the frame reaches the chest.

### 01.01.004 — House of Embalming — The walking sticks in the corner   (5 s)
- **Shot:** Insert, anamorphic 75mm · **Move:** slow push-in
- **In frame:** PROP_EBONY_STICK among a king's walking sticks
- **Action:** In a lamplit corner the camera eases toward a cluster of walking sticks; one plain ebony staff's grip, worn pale, catches the flicker.
- **Dialogue:** —
- **Sound:** lamp crackle; the lector's voice beginning, low, off-screen
- **PROMPT:** Insert, anamorphic 75mm lens, slow push-in: the camera eases toward {PROP_EBONY_STICK.LONG}, {PROP_EBONY_STICK.STATE_ST_1323}, the pale worn grip catching a slow amber flicker from a lamp nearby. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_PLATE}, crutches, modern canes, gold everywhere, carved inscriptions
- **Refs:** PROP_EBONY_STICK_REF, LOC_EMBALMING_1323_NIGHT
- **Continuity:** Plant: this is the stick Tut carries from 4.4 (PROP_EBONY_STICK). Grip worn pale. The corner is at frame left of the table.

### 01.01.005 — House of Embalming — The lector reads Spell 30B   (8 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** LECTOR (CHAR_LECTOR_1323_A)
- **Action:** The lector holds the roll open at chest height and recites, eyes on the roll, steady and exact.
- **Dialogue:** LECTOR (in Middle Egyptian; subtitled): "O my heart which I had from my mother! O my heart which I had from my mother! O my heart of my different ages!"
- **Sound:** his recitation; lamp crackle; off-screen, linen parting and a blade laid on stone
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_LECTOR_1323.LONG}, holds the roll open at chest height, reciting aloud in a measured, ritual cadence in an ancient language, his eyes lowered to the papyrus. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: grave, exact and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_LECTOR_1323.NEG}, legible writing on the papyrus, shouting
- **Refs:** CHAR_LECTOR_1323_A_front, CHAR_LECTOR_1323_A_34, LOC_EMBALMING_1323_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "O my heart which I had from my mother! O my heart which I had from my mother! O my heart of my different ages!" | lower third, two lines max (§13.7) | line in → out | seq 01 subtitle file ([[verify: 30B against printed Faulkner]] before lock)
- **Continuity:** Voice recorded first by the consultant (Middle Egyptian), lip-synced in post. The lector stands at the far (back-wall) end of the table; eyeline down to frame left, toward the table.

### 01.01.006 — House of Embalming — Ay over the glass   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** AY (CHAR_AY_A); the open glass jar (PROP_HEART_VESSEL, unsealed)
- **Action:** Ay stands motionless beside the table over a small squat jar of thick bubbled yellow-green glass on a low stand, its mouth open, lamplight glowing through it.
- **Dialogue:** —
- **Sound:** the lector's recitation continues under; lamp crackle
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: {CHAR_AY.LONG}, {CHAR_AY.WARD_A}, stands motionless beside the table over a squat jar of thick, bubbled yellow-green glass on a low stand, its mouth open, lamplight glowing yellow-green through its walls; he watches the table, waiting. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: shrewd, grave, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_AY.NEG}, crown, adze, wax serpent, papyrus band on the jar, sealed jar
- **Refs:** CHAR_AY_A_front, CHAR_AY_A_34, CHAR_AY_A_full, PROP_HEART_VESSEL_REF (1.1 variant: open, no seal), LOC_EMBALMING_1323_NIGHT
- **Continuity:** Ay look A (leopard-skin mantle over the left shoulder, collars, bare feet; no crown until 1.2). The jar is OPEN (lock gap 1): no seal, no serpent, no band.

### 01.01.007 — House of Embalming — The embalmer turns: the jackal face   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** EMBALMER (CHAR_EMBALMER_JACKAL_A), mask PROP_JACKAL_MASK (turned)
- **Action:** The embalmer straightens and turns slowly from the table until the jackal mask faces camera, a dark bundle of linen cradled in both hands.
- **Dialogue:** —
- **Sound:** a slow breath inside clay; linen settling; the recitation paused
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: a heavy-set embalmer, a dark fist-sized bundle of resin-soaked linen cradled in both his resin-stained hands at his chest, straightens and turns slowly from the table until the camera meets {PROP_JACKAL_MASK.LONG}, {PROP_JACKAL_MASK.STATE_TURNED}. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: uncanny, solemn, utterly still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_EMBALMER_JACKAL.NEG}, human face visible, eyes glowing, blades, dripping, stains
- **Refs:** PROP_JACKAL_MASK_REF, CHAR_EMBALMER_JACKAL_A_34, CHAR_EMBALMER_JACKAL_A_full, LOC_EMBALMING_1323_NIGHT
- **Continuity:** "The jackal face, at last": first time the mask is seen full on. The man's own face is never seen. No blade in frame at any time. The bundle is only ever "a dark linen bundle" (file 05 §7.3).

### 01.01.008 — House of Embalming — The bundle into Ay's hands   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** embalmer's hands, Ay's hands, the linen bundle
- **Action:** Resin-stained hands lay the dark linen bundle into an old man's open, waiting palms.
- **Dialogue:** —
- **Sound:** the soft weight of damp linen; Ay's slow breath
- **PROMPT:** Insert, 100mm macro lens, locked-off: resin-stained hands lay a dark, fist-sized bundle of resin-soaked linen into the open, waiting palms of an old man's weathered bronze-brown hands, strands of heavy gold disc-bead collars just in frame above. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, red stains, dripping, wet flesh, visible tissue, anatomical shape
- **Refs:** CHAR_AY_A_full, CHAR_EMBALMER_JACKAL_A_full, LOC_EMBALMING_1323_NIGHT
- **Continuity:** Hands only. The bundle: dark brown-black linen, indistinct, never an organ shape. It passes embalmer (frame right) → Ay (frame left).

### 01.01.009 — House of Embalming — Ay lowers the bundle into the glass   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** slow tilt down
- **In frame:** Ay's hands, the bundle, the open glass jar
- **Action:** Ay's hands lower the bundle through the open mouth of the yellow-green glass jar until it rests inside, a dark shape behind thick glass.
- **Dialogue:** LECTOR (O.S., in Middle Egyptian; subtitled): "Do not stand up as a witness against me..."
- **Sound:** the lector's line off-screen; linen sliding against glass; a faint dull settle
- **PROMPT:** Insert, 100mm macro lens, slow tilt down: weathered bronze-brown hands lower a dark bundle of resin-soaked linen through the open mouth of a squat jar of thick, bubbled yellow-green glass until it rests inside, a dark indistinct shape behind the cloudy glass. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT}. Mood: reverent, exact, silent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, wax serpent, papyrus band, resin seal, liquid, dripping, red stains
- **Refs:** PROP_HEART_VESSEL_REF (1.1 variant: open), CHAR_AY_A_full, LOC_EMBALMING_1323_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Do not stand up as a witness against me..." | lower third (§13.7) | line in → out | seq 01 subtitle file
- **Continuity:** The lector's line plays off-screen over the insert (recorded first; no sync needed). The jar is still open.

### 01.01.010 — House of Embalming — It pulses   (4 s)
- **Shot:** Extreme close-up, 100mm macro · **Move:** locked-off
- **In frame:** the open glass jar with the dark shape inside
- **Action:** The lamplight inside the thick glass swells faintly once around the dark shape, then settles.
- **Dialogue:** —
- **Sound:** a HEARTBEAT, close and deep: it is coming from the glass
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: a dark indistinct shape rests inside a squat jar of thick, bubbled yellow-green glass, and the light held in the glass around it swells faintly once, then settles back. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, visible organ, anatomical shape, liquid, red glow, bright flash, wax serpent, papyrus band
- **Refs:** PROP_HEART_VESSEL_REF (1.1 variant: open), LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** pulse | one light swell in the glass plus a 2% scale throb of the dark shape, timed to the heartbeat (file 05 §10 #1) | the jar only | frames 20–40 | glow element, matched to the vessel's pale yellow-green
- **Continuity:** Lighting variant changes here: NIGHT → NIGHT_LOW (the lamps gutter at the pulse; held to the end of the scene). The word "heart" never enters a prompt.

### 01.01.011 — House of Embalming — The embalmer lurches back   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** EMBALMER (CHAR_EMBALMER_JACKAL_A) foreground; AY (CHAR_AY_A) beyond, still
- **Action:** The embalmer lurches back a step from the table, hands raised, and cries out from inside the mask; beyond him Ay stays perfectly still over the glass.
- **Dialogue:** EMBALMER (in Late Egyptian; subtitled): "Without his heart he cannot be weighed!"
- **Sound:** a clay foot-scrape on sand; the cry, muffled by the mask; the heartbeat under
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_EMBALMER_JACKAL.SHORT} lurches back a step from the table, raising his hands, and cries out one short sentence from inside the mask, while beyond him {CHAR_AY.SHORT}, {CHAR_AY.WARD_A}, stays perfectly still over the glass jar. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: restrained terror against cold calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_EMBALMER_JACKAL.NEG}, {CHAR_AY.NEG}, blades, falling over, running
- **Refs:** CHAR_EMBALMER_JACKAL_A_full, CHAR_AY_A_full, PROP_JACKAL_MASK_REF, LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** subtitle | "Without his heart he cannot be weighed!" | lower third (§13.7) | line in → out | seq 01 subtitle file
- **Continuity:** The mask has no mouth: no lip-sync; the recorded line (consultant, Late Egyptian) is played muffled. "Ay does not move. He knew." is written as a state ("stays perfectly still").

### 01.01.012 — House of Embalming — "He will be. Not by ours."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** AY (CHAR_AY_A)
- **Action:** Ay, eyes on the glass, speaks two short sentences with a pause between, his face unmoved.
- **Dialogue:** AY (in Late Egyptian; subtitled): "He will be." (beat) "Not by ours."
- **Sound:** the heartbeat, slow; a lamp gutters
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AY.SHORT}, {CHAR_AY.WARD_A}, his eyes on the glass jar below frame, speaking softly in an ancient language, one short sentence, a pause, then a second, his hollow-cheeked face unmoved. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: cold certainty, grief buried deep. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_AY.NEG}, crown, smiling, shouting
- **Refs:** CHAR_AY_A_front, CHAR_AY_A_34, LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** subtitle | "He will be." / "Not by ours." | lower third, two separate events (§13.7) | each line in → out | seq 01 subtitle file
- **Continuity:** Eyeline down to frame right (the jar on its stand). The one lamp close to the table keys his face; the room behind is blue-black.

### 01.01.013 — House of Embalming — Ay's hand on the papyrus: "The other way."   (6 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** LECTOR (CHAR_LECTOR_1323_A), AY (CHAR_AY_A)
- **Action:** The lector falters and lowers the roll; Ay lays his hand flat on the open papyrus and says three words to him.
- **Dialogue:** AY (in Late Egyptian; subtitled): "The other way."
- **Sound:** the recitation breaking off; papyrus crackling under a palm
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_LECTOR_1323.SHORT} falters mid-recitation and lets the open roll sink, and {CHAR_AY.SHORT} lays his hand flat across the papyrus, looks him in the eye and, speaking softly in an ancient language, says one short sentence. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: quiet command against fear. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_LECTOR_1323.NEG}, {CHAR_AY.NEG}, legible writing on the papyrus, grabbing, violence
- **Refs:** CHAR_LECTOR_1323_A_34, CHAR_AY_A_34, LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** subtitle | "The other way." | lower third (§13.7) | line in → out | seq 01 subtitle file
- **Continuity:** Lector frame left, Ay frame right (hold the line from 01.01.011). The papyrus stays illegible.

### 01.01.014 — House of Embalming — The lector changes the words   (6 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** LECTOR (CHAR_LECTOR_1323_A)
- **Action:** The lector swallows, then, without looking at the roll, recites two short phrases no scribe has written.
- **Dialogue:** LECTOR (in Middle Egyptian; subtitled): "Stand up. Be a witness."
- **Sound:** a dry swallow; his voice, low and unsteady, then firm
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_LECTOR_1323.SHORT} swallows hard, lifts his eyes from the roll and, reciting aloud in a measured, ritual cadence in an ancient language, speaks two short phrases, his voice steadying. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_LECTOR_1323.NEG}, tears, shouting
- **Refs:** CHAR_LECTOR_1323_A_front, CHAR_LECTOR_1323_A_34, LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** subtitle | "Stand up. Be a witness." | lower third (§13.7) | line in → out | seq 01 subtitle file
- **Continuity:** The inverted rite (the film's rule-block line, bible §4). Voice recorded first by the consultant.

### 01.01.015 — House of Embalming — Hot resin seals the glass   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** a bronze ladle (Ay's hand), the glass jar
- **Action:** A ladle tips a thick stream of hot black resin over the jar's open mouth; it spreads into a glossy dome and seals, smoking.
- **Dialogue:** —
- **Sound:** a slow hot pour; a hiss; the heartbeat, muffled now
- **PROMPT:** Insert, 100mm macro lens, locked-off: a small bronze ladle held in a weathered hand tips a thick stream of hot black resin over the open mouth of a squat jar of thick yellow-green glass, and the resin spreads into a glossy dome that seals it, thin smoke curling upward. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: reverent, exact, final. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, fire, flames on the jar, wax serpent, papyrus band, spilling, red liquid
- **Refs:** PROP_HEART_VESSEL_REF (1.1 variant: plain resin seal), CHAR_AY_A_full, LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** VFX-ASSIST
- **Continuity:** From here the jar is sealed with plain black resin (glossy, wet). The wax serpent and papyrus band are added off-screen before 1.2. VFX-ASSIST: resin flow and smoke; deliver before (open) and after (sealed) plates at the same framing.

### 01.01.016 — House of Embalming — One beat; one green pulse   (5 s)
- **Shot:** Extreme close-up, 100mm macro · **Move:** locked-off
- **In frame:** the sealed glass jar
- **Action:** The dark shape inside beats once; the glass answers with one faint green pulse; then stillness.
- **Dialogue:** —
- **Sound:** one heartbeat, then the heartbeat recedes far away without stopping
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: a squat jar of thick, cloudy yellow-green glass sealed with a dome of black resin, {PROP_HEART_VESSEL.STATE_V_1323_FRESH}, {PROP_HEART_VESSEL.STATE_V_1323_PULSE}, then falling still, a curl of smoke thinning above it. Setting: {LOC_EMBALMING_1323.SHORT}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: awe held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, visible organ, anatomical shape, red light, strong glow, wax serpent, papyrus band
- **Refs:** PROP_HEART_VESSEL_REF (1.1 variant), LOC_EMBALMING_1323_NIGHT_LOW
- **Flags:** COMP
- **Comp:** pulse | one faint GREEN pulse in the glass (pale yellow-green #B5E36A family, file 02 §0.1) plus a 2% throb of the dark shape | the jar only | one beat, ~12 frames | glow element
- **Continuity:** Lock gap 1: the PROP_HEART_VESSEL LONG/SHORT are not pasted here (they carry the 1.2 serpent and band). The heartbeat recedes but never stops (it returns in 1.3 and 1.5).

### 01.01.017 — House of Embalming — The forearms settled low   (7 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** the embalmer's hands on the linen over the body
- **Action:** Trembling resin-stained hands smooth the linen and settle the shapes of two forearms beneath it, low across the body.
- **Dialogue:** —
- **Sound:** linen smoothed; unsteady breath inside clay; the heartbeat very far away; the lamps guttering to silence
- **PROMPT:** Insert, 100mm macro lens, locked-off: trembling resin-stained hands smooth plain white linen and gently settle the shapes of two forearms lying beneath it, low across the body, then withdraw from frame, leaving the linen still. Setting: {LOC_EMBALMING_1323.SHORT}, {LOC_EMBALMING_1323.STATE_BODY}, in the dead of night. Lighting: {LOC_EMBALMING_1323.LIGHT_NIGHT_LOW}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, bare arms, visible skin of the body, crossed arms on the chest, blades, stains on the linen
- **Refs:** CHAR_EMBALMER_JACKAL_A_full, CHAR_TUT_BODY_1323, LOC_EMBALMING_1323_NIGHT_LOW
- **Continuity:** Forearms LOW, not crossed (screenplay [[verify]]; bible research fix). Only linen and the embalmer's hands are seen. Cut to black (or hold on the still linen) into the KV62 SUPER.

## 01.02 — INT. KV62, BURIAL CHAMBER - NIGHT (seventy days later)

### 01.02.001 — KV62, burial chamber — Establishing: the painted chamber   (7 s)
- **Shot:** Wide establishing shot, anamorphic 24mm · **Move:** slow push-in
- **In frame:** the chamber; the second coffin in the open sarcophagus; attendants' torches at frame left (figures soft)
- **Action:** The camera enters from the antechamber toward the painted far wall; the paint glistens wet; the gilded face of a coffin looks up from the open sarcophagus.
- **Dialogue:** —
- **Sound:** torch flames; a drip of water from wet plaster; distant chanting fading out; the heartbeat, very far away
- **PROMPT:** Wide establishing shot, anamorphic 24mm lens, slow push-in: the camera moves in from a low doorway toward the painted far wall, the colours glistening wet, while in the open sarcophagus the serene gilded face of a coffin lid looks up at the ceiling, two torch-bearers soft at frame left. Setting: {LOC_KV62_BURIAL_1323.LONG}, {LOC_KV62_BURIAL_1323.STATE_RUBBLE}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: hushed, fresh grief. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, electric light, glass, faded or spotted paint, legible hieroglyphs, a king's face in close-up on the wall, wreath on the coffin
- **Refs:** LOC_KV62_BURIAL_1323_NIGHT, LOC_KV62_BURIAL_1323_RUBBLE (state plate)
- **Flags:** COMP
- **Comp:** SUPER | "VALLEY OF THE KINGS. SEVENTY DAYS LATER." | lower left, small (§13.7) | 0:01 → 0:05 | seq 01 SUPER file
- **Continuity:** Geography lock: we enter from the antechamber (south); the painted north wall faces camera; the Treasury doorway at frame right (east); torches at frame left (key from the left). Shrine panels stacked unassembled against a side wall. The low opening at the foot of the north wall is still open (RUBBLE state). No wreath yet.

### 01.02.002 — KV62, burial chamber — The widow at the sarcophagus   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** ANKHESENAMUN (CHAR_ANKHESENAMUN_A)
- **Action:** Ankhesenamun steps to the edge of the sarcophagus and leans over it, the small wreath held in both hands.
- **Dialogue:** —
- **Sound:** bare feet on stone; torch crackle; her held breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_ANKHESENAMUN.LONG}, {CHAR_ANKHESENAMUN.WARD_A}, steps to the edge of a massive stone sarcophagus and leans over it, the wreath held low in both hands, her eyes on the coffin inside. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_ANKHESENAMUN.NEG}, weeping loudly, wailing
- **Refs:** CHAR_ANKHESENAMUN_A_front, CHAR_ANKHESENAMUN_A_34, CHAR_ANKHESENAMUN_A_full, PROP_CORNFLOWER_WREATH_REF, LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** Look A: shawl over head and shoulders, one blue faience ring, bare feet. She stands on the near (south) side of the sarcophagus, facing the north wall.

### 01.02.003 — KV62, burial chamber — The wreath on the brow   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_CORNFLOWER_WREATH; the coffin's gilded brow (cobra and vulture)
- **Action:** A young woman's hands lower the wreath onto the gilded brow of the coffin lid, over the carved cobra and vulture, and let it settle.
- **Dialogue:** —
- **Sound:** dry leaves whispering against gold
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_CORNFLOWER_WREATH.LONG}, is lowered by a young woman's slender hands, a small blue faience ring on one finger, onto the gilded brow of a coffin lid just above a small carved cobra and vulture, and settles there. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, roses, modern flowers, ribbon, legible hieroglyphs
- **Refs:** PROP_CORNFLOWER_WREATH_REF, CHAR_ANKHESENAMUN_A_full, LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** From here the LOC state is COFFIN (wreath on the brow of the second coffin, over the cobra and vulture). Motif: cornflowers (bible §11).

### 01.02.004 — KV62, burial chamber — The small closed box   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** the Treasury doorway; a small closed wooden box
- **Action:** Through a low doorway in the right-hand wall, lamplight finds a small closed wooden box on the floor of a dark side chamber.
- **Dialogue:** —
- **Sound:** silence; a torch flame fluttering
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: through a low doorway in the right-hand wall, a wash of warm lamplight falls across a small closed wooden box resting on the floor of a dark side chamber, its lid shut. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {NEG_PLATE}, open box, contents of the box, infants, small bodies, tiny coffins visible
- **Refs:** LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** The Treasury doorway is at frame right (east). The box is never opened; the two tiny coffins inside are never seen (screenplay). Objective shot, NOT her point of view: the lamplight finds the box before she lets herself look (screenplay order: "She does not look at it. Then she does."); her look lands on it in 01.02.005. Camera from beside the sarcophagus's south-east corner.

### 01.02.005 — KV62, burial chamber — She does not look; then she does   (6 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** ANKHESENAMUN (CHAR_ANKHESENAMUN_A)
- **Action:** Ankhesenamun keeps her eyes on the coffin, then slowly turns her head to look off frame right toward the low doorway.
- **Dialogue:** —
- **Sound:** a shallow breath; the torch
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_ANKHESENAMUN.SHORT} keeps her grief-reddened eyes fixed down on the coffin, then slowly turns her head to look off frame right toward a low doorway, and holds there. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_ANKHESENAMUN.NEG}, sobbing, tears streaming, open mouth
- **Refs:** CHAR_ANKHESENAMUN_A_front, CHAR_ANKHESENAMUN_A_profile, LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** Eyeline: down (coffin) → frame right (the Treasury doorway). Torchlight keys her from frame left.

### 01.02.006 — KV62, burial chamber — The adze to the mouth and eyes   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** PROP_IRON_ADZE_1323 in Ay's right hand; the coffin's gilded face
- **Action:** The iron adze touches the gilded mouth of the coffin's face, lifts, touches one inlaid eye, then the other.
- **Dialogue:** —
- **Sound:** the faintest tick of iron on gold; Ay's recitation begins (pre-lap from 01.02.007)
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_IRON_ADZE_1323.LONG}, gripped in an old man's weathered right hand, touches its dark blade to the gilded mouth of a coffin lid's serene carved face, lifts, touches one inlaid eye, then the other. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: reverent, exact, slow. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, scratching, damage to the gold, sparks
- **Refs:** PROP_IRON_ADZE_1323_REF, CHAR_AY_B_full, LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** Adze in Ay's RIGHT hand (look B). The wreath (from 01.02.003) sits on the brow just above frame. The adze rhymes with the nano-adze in 01.05.015–017.

### 01.02.007 — KV62, burial chamber — Ay opens the mouth   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** AY (CHAR_AY_B)
- **Action:** Ay stands over the coffin, the adze raised at his chest, and recites.
- **Dialogue:** AY (in Middle Egyptian; subtitled): "I have opened thy mouth. I have opened thy two eyes... with the iron that cometh forth from Set."
- **Sound:** his recitation; torch crackle
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AY.LONG}, {CHAR_AY.WARD_B}, stands over the coffin with the adze raised at his chest, reciting aloud in a measured, ritual cadence in an ancient language, his deep-set eyes on the gilded face below frame. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: grave, shrewd, absolutely certain. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_AY.NEG}, shouting, smiling
- **Refs:** CHAR_AY_A_front, CHAR_AY_A_34, CHAR_AY_B_full, PROP_IRON_ADZE_1323_REF, LOC_KV62_BURIAL_1323_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "I have opened thy mouth. I have opened thy two eyes... with the iron that cometh forth from Set." | lower third, two lines (§13.7) | line in → out | seq 01 subtitle file
- **Continuity:** Look B: tall blue crown with a gold cobra, leopard skin over the left shoulder, adze in the right hand. The same words return in Nour's mouth in 01.05.016–018.

### 01.02.008 — KV62, burial chamber — The painted wall; the low opening   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 32mm · **Move:** slow tilt down
- **In frame:** AY (CHAR_AY_B, foreground shoulder, no face); the north wall painting; the low opening
- **Action:** Past Ay's leopard-skin shoulder the camera finds the painted wall, where a painted priest in a leopard skin raises an adze to a royal figure, then tilts down to a low dark opening at its foot.
- **Dialogue:** —
- **Sound:** a breath of cooler air from the opening; the torches lean
- **PROMPT:** Over-the-shoulder shot, anamorphic 32mm lens, slow tilt down: past the leopard-skin shoulder of {CHAR_AY.SHORT} in the soft foreground, the camera holds on the painted far wall, where a painted priest in a leopard skin raises an adze to a royal figure, then tilts down to a low dark opening in the rock at the wall's foot. Setting: {LOC_KV62_BURIAL_1323.SHORT}, {LOC_KV62_BURIAL_1323.STATE_RUBBLE}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: a hidden door, quiet dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_AY.NEG}, legible hieroglyphs, a king's face in close-up on the wall, faded paint, modern floor
- **Refs:** LOC_KV62_BURIAL_1323_NIGHT, LOC_KV62_BURIAL_1323_RUBBLE (state plate), CHAR_AY_B_full
- **Continuity:** The painting mirrors the living Ay (the north-wall first scene, right side). The wall is unfinished; the opening sits below the right-hand scene. The painted figures read at a distance only.

### 01.02.009 — KV62, burial chamber — The lector stoops in with the vessel   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** LECTOR (CHAR_LECTOR_1323_A); PROP_HEART_VESSEL (sealed, 1.2)
- **Action:** The lector stoops and ducks through the low opening, the sealed glass jar carried low in both hands, lit from below by a small clay lamp he has set on the floor at the opening's lip.
- **Dialogue:** —
- **Sound:** bare feet on grit; the lamp flame guttering in the draught
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: {CHAR_LECTOR_1323.SHORT}, the roll tucked into his sash, stoops low and ducks through a dark opening at the foot of the painted wall with {PROP_HEART_VESSEL.SHORT}, {PROP_HEART_VESSEL.STATE_V_1323_SEALED}, a small clay oil lamp burning on the floor at the opening's lip. Setting: {LOC_KV62_BURIAL_1323.SHORT}, {LOC_KV62_BURIAL_1323.STATE_RUBBLE}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: reverent, careful, secret. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_LECTOR_1323.NEG}, dropping the jar, glowing jar
- **Refs:** CHAR_LECTOR_1323_A_full, CHAR_LECTOR_1323_A_34, PROP_HEART_VESSEL_REF, LOC_KV62_BURIAL_1323_NIGHT
- **Continuity:** Vessel state V-1323 sealed (file 04: "carried low in both hands by lamplight"): now the wax serpent and papyrus band are on it. It does not pulse in 1.2. Both his hands are on the jar, so the lamp waits on the floor at the lip; he takes it up once through (01.02.011). The roll is tucked into the sash (WARD_A's "holding a papyrus roll" not pasted). The lector's right fingertips ink-stained (he paints the eye in 01.02.014).

### 01.02.010 — KV62, burial chamber — The halt-seal: serpent and name   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** PROP_HEART_VESSEL (sealed)
- **Action:** In the lector's lamplight the camera eases onto the resin seal: a tiny coiled wax serpent, a papyrus band tied round the neck, faded red marks on it.
- **Dialogue:** —
- **Sound:** the lamp's small flame; his breathing close
- **PROMPT:** Insert, 100mm macro lens, slow push-in: {PROP_HEART_VESSEL.LONG}, {PROP_HEART_VESSEL.STATE_V_1323_SEALED}, the faded red marks on the band sliding slowly through the warm glow. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_LAMP_CLOSE}. Mood: reverent, secret, still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, legible hieroglyphs, legible writing on the band, glow inside the jar, visible organ
- **Refs:** PROP_HEART_VESSEL_REF, LOC_KV62_BURIAL_1323_LAMP_CLOSE
- **Flags:** COMP
- **Comp:** the name on the band | the serpent's name in red ink, drawn by the production Egyptologist from research 09's sign palette (bible §4.1 halt-seal) | on the papyrus band, tracked | full clip | Egyptologist glyph asset
- **Continuity:** Ay's halt-seal (bible §4.1): any shabti-class unit that touches the vessel goes still (pays off in 8.4). The glass is dark and still. Held low in both hands, as 01.02.009; the key is the lamp on the floor at the opening's lip.

### 01.02.011 — KV62, burial chamber — Down the hidden corridor   (6 s)
- **Shot:** Wide shot, anamorphic 24mm · **Move:** locked-off
- **In frame:** LECTOR (CHAR_LECTOR_1323_A, receding, small); the corridor
- **Action:** Down a narrow, undecorated rock-cut corridor sloping into darkness, the lector's small lamp recedes past black side doorways toward a far chamber until it is a point of light.
- **Dialogue:** —
- **Sound:** receding footsteps; stone silence
- **PROMPT:** Wide shot, anamorphic 24mm lens, locked-off: down a narrow rock-cut corridor of clean pale limestone sloping into darkness, the small lamp flame carried by {CHAR_LECTOR_1323.SHORT} recedes past black side doorways toward a far chamber until it is a single point of light. Setting: a hidden corridor behind the painted chamber, at night. Lighting: one small oil lamp moving away, all else blue-black. Mood: secret, patient, final. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, {CHAR_LECTOR_1323.NEG}, torches, electric light, rubble, dust clouds, wall paintings, modern floor
- **Refs:** LOC_KV62_NORTH_CORRIDOR (geometry only; 1323 clean derivation), CHAR_LECTOR_1323_A_full
- **Continuity:** Lock gap 4: the 2033 corridor token shows rubble; here the corridor is clean and empty (the baskets come next). "Down" is away from camera. He has taken up the lamp from the lip: the jar now in the crook of his left arm, the lamp in his right hand (too small to read at this size).

### 01.02.012 — KV62, burial chamber — The vessel in the niche   (5 s)
- **Shot:** Insert, anamorphic 75mm · **Move:** locked-off
- **In frame:** PROP_HEART_VESSEL (sealed); the niche; the lector's hands
- **Action:** The lector's hands set the sealed jar into a square niche at chest height in a blank plastered wall, withdraw, and it sits dark and still.
- **Dialogue:** —
- **Sound:** glass on dry plaster; nothing else; the heartbeat absent
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: ink-stained hands set {PROP_HEART_VESSEL.SHORT} into a square niche at chest height in a freshly plastered wall and withdraw slowly; the jar sits dark and still. Setting: a small low rock-cut chamber, its walls under fresh pale plaster, at night. Lighting: one small oil lamp set on the floor below the niche, a warm circle on the niche, deep darkness beyond. Mood: reverent, final. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {NEG_REMAINS}, glow inside the jar, pulse, cracked plaster, dust, torches, legible writing
- **Refs:** PROP_HEART_VESSEL_REF, LOC_KV62_HEART_CHAMBER (geometry only; 1323 fresh-plaster derivation)
- **Continuity:** "It does not pulse." Vessel set in the far chamber's niche (where it is found in Seq 8). Lock gap 4 (fresh plaster, not the 2033 cracked skim). The lamp is set down below the niche so both hands can place the jar.

### 01.02.013 — KV62, burial chamber — Baskets packed; the opening plastered   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** the low opening packed with baskets; a palm with wet plaster
- **Action:** The low opening, packed to its top with stacked baskets of limestone chips; a bare palm sweeps wet pale plaster across it in one slow arc, sealing it.
- **Dialogue:** —
- **Sound:** the wet slap and drag of plaster; a basket creaks
- **PROMPT:** Medium shot, anamorphic 40mm lens, locked-off: the low opening at the foot of the painted wall is packed to its top with stacked reed baskets of limestone chips, and a bare palm sweeps wet pale plaster across it in one slow arc, sealing it over. Setting: {LOC_KV62_BURIAL_1323.SHORT}, {LOC_KV62_BURIAL_1323.STATE_NORTH_WALL_FRESH}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_NIGHT}. Mood: patient, secret, final. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, trowel of steel, cement, bricks, modern tools, legible hieroglyphs
- **Refs:** LOC_KV62_BURIAL_1323_NIGHT, LOC_KV62_BURIAL_1323_RUBBLE (state plate), LOC_KV62_BURIAL_1323_NORTH_WALL_FRESH (state plate)
- **Continuity:** LOC state RUBBLE → NORTH_WALL_FRESH (the fresh plaster patch sits below the right-hand painted scene; the painted eye marks its top edge, about 2.1 m up). Before/after plates at this framing.

### 01.02.014 — KV62, burial chamber — The last stroke: the painted eye   (6 s)
- **Shot:** Extreme close-up, 100mm macro · **Move:** locked-off
- **In frame:** the painted eye; the lector's brush hand
- **Action:** Later. A reed brush in ink-stained fingers lays one black stroke on the damp painted wall, completing the painted eye of a royal figure in profile; it now seems to gaze into the lens.
- **Dialogue:** —
- **Sound:** the whisper of a reed brush; a lamp flame; the heartbeat, one faint beat, far away
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: a reed brush held in ink-stained fingers lays one smooth black stroke on the damp painted plaster, completing the flat painted eye of a royal figure in profile, which now seems to gaze straight into the lens as the brush lifts away. Setting: {LOC_KV62_BURIAL_1323.SHORT}, {LOC_KV62_BURIAL_1323.STATE_NORTH_WALL_FRESH}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_LAMP_CLOSE}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, legible hieroglyphs, realistic human eye, eye blinking, eye moving, glossy modern paint
- **Refs:** LOC_KV62_BURIAL_1323_LAMP_CLOSE, CHAR_LECTOR_1323_A_full
- **Continuity:** The lector paints (CHAR_PAINTER_1323 not used). The eye is flat Egyptian paint; it never animates. Motif: the painted eye (broken in Seq 8 by the stick, restored in the coda). Lighting LAMP_CLOSE.

### 01.02.015 — KV62, burial chamber — Ay pinches out the lamp   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** AY (CHAR_AY_B)
- **Action:** Ay studies his painted self in silence, then reaches out and pinches the lamp's flame between finger and thumb; the frame falls to black.
- **Dialogue:** —
- **Sound:** a tiny hiss; then silence
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_AY.SHORT}, {CHAR_AY.WARD_B}, studies the painted wall in silence, his face lit by one small flame, then reaches out and pinches the flame of a clay lamp between finger and thumb, and the frame falls into darkness. Setting: {LOC_KV62_BURIAL_1323.SHORT}, at night. Lighting: {LOC_KV62_BURIAL_1323.LIGHT_LAMP_CLOSE}. Mood: shrewd, unreadable, alone. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PERIOD}, {CHAR_AY.NEG}, smiling, speaking, fire spreading
- **Refs:** CHAR_AY_A_front, CHAR_AY_A_profile, CHAR_AY_B_full, LOC_KV62_BURIAL_1323_LAMP_CLOSE
- **Continuity:** Ends on BLACK (screenplay). Eyeline to frame right, up (the painted wall). Hold black ~12 frames before the 1925 SUPER.

## 01.03 — INT. KV15 (THE TOMB OF SETI II, USED AS A LAB), OUTER CORRIDOR - DAY (11 November 1925)

### 01.03.001 — KV15, outer corridor — Establishing: the corridor laboratory   (7 s)
- **Shot:** Wide establishing shot, anamorphic 40mm, tripod height · **Move:** locked-off
- **In frame:** the corridor lab; the gold coffin on trestles; IBRAHIM (head of table, frame left); CARTER, DERRY, HAMDI (soft, bent at the table); BURTON's camera (frame right, near the entrance)
- **Action:** Heat and dust in a shaft of daylight; a gold coffin rests on trestles; the young lamp-holder at its head; three men bent around it; the plate camera on its tripod near the bright entrance.
- **Dialogue:** —
- **Sound:** the tick of cooling steel; a paraffin stove's hiss; flies; wind in the valley outside; no music
- **PROMPT:** Wide establishing shot, anamorphic 40mm lens, locked-off at tripod height: a gold coffin rests on trestles along a white-draped table, {CHAR_IBRAHIM_1925.SHORT}, holding a lantern low at its head, three men in shirtsleeves and coats bent around it, and a wooden plate camera on a tripod near the bright entrance, dust turning in the shaft of daylight. Setting: {LOC_KV15_LAB_1925.LONG}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: heat, silence, concentration. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_IBRAHIM_1925.NEG}, body visible on the table, saws, pith helmets, electric bulbs
- **Refs:** LOC_KV15_LAB_1925_DAY, CHAR_IBRAHIM_1925_A_full, CHAR_CARTER_1925_A_full, CHAR_DERRY_1925_A_full, CHAR_HAMDI_1925_A_full, PROP_BURTON_PLATES_REF, PROP_LAMP_1925_REF
- **Flags:** COMP
- **Comp:** SUPER | "VALLEY OF THE KINGS. 11 NOVEMBER 1925." | lower left, small (§13.7) | 0:01 → 0:05 | seq 01 SUPER file
- **Continuity:** Geography lock: entrance and daylight up the slope at frame right; table on the corridor axis; Ibrahim and lamp at the head (frame left); Burton's camera at the foot (frame right). Generate in natural colour; GRADE_1925 sepia in post (no sepia words in prompts). The table's centre stays below the men's backs.

### 01.03.002 — KV15, outer corridor — The rim crusted black   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** the gold coffin's rim; a linen shape inside, soft
- **Action:** The camera eases toward the rim of the gold coffin, crusted thick with hardened black unguent; inside, a pale linen shape stays soft and out of focus.
- **Dialogue:** —
- **Sound:** heat; a fly; the stove
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: the camera eases toward the rim of a gold coffin lying on trestles, crusted thick with hardened black unguent, a pale linen-wrapped shape soft and out of focus inside it, heat shimmer rising across the frame. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: heat, stillness, unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, sharp focus inside the coffin, face visible, gold mask, instruments at work
- **Refs:** LOC_KV15_LAB_1925_DAY
- **Continuity:** Focus stays on the black crust at the rim; the linen shape never resolves (file 05 §7.3).

### 01.03.003 — KV15, outer corridor — Master: the three at the table   (6 s)
- **Shot:** Medium wide shot, anamorphic 40mm, tripod height · **Move:** locked-off
- **In frame:** CARTER (CHAR_CARTER_1925_A), DERRY (CHAR_DERRY_1925_A), HAMDI (CHAR_HAMDI_1925_A)
- **Action:** Carter, Derry and Hamdi stand at the head of the table looking down at the coffin below frame; Carter's jaw is set.
- **Dialogue:** —
- **Sound:** a slow exhale; heat; the stove
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off at tripod height: {CHAR_CARTER_1925.LONG}, stands at the head of the table beside {CHAR_DERRY_1925.SHORT} and {CHAR_HAMDI_1925.SHORT}, all three looking down at the coffin below the frame edge, faces damp with heat. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_CARTER_1925.NEG}, {CHAR_DERRY_1925.NEG}, {CHAR_HAMDI_1925.NEG}, body on the table, instruments raised
- **Refs:** CHAR_CARTER_1925_A_front, CHAR_CARTER_1925_A_34, CHAR_DERRY_1925_A_34, CHAR_HAMDI_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** Locked-off master: three faces allowed (§4.5). Left to right: Hamdi, Carter, Derry. Hamdi's red tarboosh reads as dark in the sepia grade.

### 01.03.004 — KV15, outer corridor — Ibrahim holds the lamp   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** IBRAHIM (CHAR_IBRAHIM_1925_A), PROP_LAMP_1925 (held)
- **Action:** Ibrahim holds the lantern low at arm's length over the work; his arm trembles with the ache; he tightens his grip and keeps it there.
- **Dialogue:** —
- **Sound:** the lantern's wire bail creaking; his controlled breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_IBRAHIM_1925.LONG}, holds {PROP_LAMP_1925.SHORT}, {PROP_LAMP_1925.STATE_HELD}, his outstretched arm trembling with the ache; he tightens his grip, jaw tight, and keeps it raised. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_IBRAHIM_1925.NEG}, lowering the lamp, electric torch
- **Refs:** CHAR_IBRAHIM_1925_A_front, CHAR_IBRAHIM_1925_A_34, CHAR_IBRAHIM_1925_A_full, PROP_LAMP_1925_REF, LOC_KV15_LAB_1925_DAY
- **Continuity:** Lamp in his RIGHT hand, lit; this dented lantern stands unlit on Nour's lectern in 01.05. Ibrahim at the head of the table (frame left); his eyeline down and to frame right.

### 01.03.005 — KV15, outer corridor — "No amount of legitimate force will."   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** CARTER (CHAR_CARTER_1925_A)
- **Action:** Carter speaks two short sentences, a pause, a third; then looks off frame right to Derry.
- **Dialogue:** CARTER: "Firmly stuck. The sun didn't soften it." (beat) "No amount of legitimate force will."
- **Sound:** his voice flat with heat; the stove
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_CARTER_1925.SHORT}, {CHAR_CARTER_1925.WARD_A}, eyes on the coffin below frame, speaks two short sentences, pauses, speaks a third, then lifts his heavy-lidded eyes off frame right toward a colleague. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_CARTER_1925.NEG}, smiling, shouting
- **Refs:** CHAR_CARTER_1925_A_front, CHAR_CARTER_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** Eyeline to frame right (Derry). Derry's answering nod is its own clip (01.03.006); then the blade (01.03.007).

### 01.03.006 — KV15, outer corridor — Derry nods   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** DERRY (CHAR_DERRY_1925_A)
- **Action:** Derry meets Carter's look from off frame left and gives one small, grave nod, then turns his head toward the stove at frame right.
- **Dialogue:** —
- **Sound:** heat; the stove's hiss; a chair scrape; a step toward the stove
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_DERRY_1925.LONG}, meets a colleague's look from off frame left and gives one small, grave nod, then turns his head slowly toward frame right. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_DERRY_1925.NEG}, speaking, smiling, hands or instruments in frame
- **Refs:** CHAR_DERRY_1925_A_front, CHAR_DERRY_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** "He looks at Derry. Derry nods." Eyeline to frame left (Carter), answering 01.03.005's look to frame right; Derry stands frame right of Carter (the master's line, 01.03.003). His turn to frame right leads into the blade insert (01.03.007). Same set-up as 01.03.011.

### 01.03.007 — KV15, outer corridor — A blade out of the flame   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** a steel blade; a paraffin stove's flame; a hand in a white coat cuff
- **Action:** A long steel blade is drawn up out of the blue flame of a small stove, heat trembling in the air above its edge.
- **Dialogue:** —
- **Sound:** the stove's roar dropping as the blade lifts; a faint metallic tick
- **PROMPT:** Insert, 100mm macro lens, locked-off: a hand in a starched white coat cuff draws a long, slim steel blade slowly up out of the blue flame of a small paraffin stove, heat trembling in the air above its edge. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: clinical, ominous, silent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, cutting, incision, the blade touching anything, rubber gloves, surgical mask
- **Refs:** LOC_KV15_LAB_1925_DAY, CHAR_DERRY_1925_A_full
- **Continuity:** The blade is never seen at work (file 05 §7.3; bible §3.4). It exits frame upward-left toward the table.

### 01.03.008 — KV15, outer corridor — Faces: Derry works, Hamdi watches his hands   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** lateral tracking right
- **In frame:** DERRY (CHAR_DERRY_1925_A), HAMDI (CHAR_HAMDI_1925_A)
- **Action:** From Derry, eyes lowered, working with small steady shoulder movements below frame, the camera drifts to Hamdi, who watches the other man's hands intently.
- **Dialogue:** —
- **Sound:** OFF-SCREEN: steel scraping on resin, slow and patient
- **PROMPT:** Medium close-up, anamorphic 75mm lens, lateral tracking right: from {CHAR_DERRY_1925.SHORT}, eyes lowered, working with small steady movements of his shoulders below frame, the camera drifts slowly to {CHAR_HAMDI_1925.LONG}, who watches the other man's hands intently. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: grave and exact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_DERRY_1925.NEG}, {CHAR_HAMDI_1925.NEG}, hands or instruments in frame, table surface visible
- **Refs:** CHAR_DERRY_1925_A_34, CHAR_HAMDI_1925_A_front, CHAR_HAMDI_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** "We stay on FACES." The table line stays below frame. One lateral move logged: right, about 1 m.

### 01.03.009 — KV15, outer corridor — Carter watches nothing   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** CARTER (CHAR_CARTER_1925_A)
- **Action:** Carter stares past the table into the middle distance, unblinking, sweat at his temple.
- **Dialogue:** —
- **Sound:** steel on resin, off-screen
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_CARTER_1925.SHORT} stares past the table into the middle distance, unblinking, a bead of sweat sliding at his temple. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: fierce, jaw set, far away. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_CARTER_1925.NEG}, speaking, smiling
- **Refs:** CHAR_CARTER_1925_A_front, LOC_KV15_LAB_1925_DAY
- **Continuity:** Eyeline: into the middle distance, just left of lens.

### 01.03.010 — KV15, outer corridor — Ibrahim watches everything; the crack   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** IBRAHIM (CHAR_IBRAHIM_1925_A)
- **Action:** Ibrahim's eyes move from face to face; at a dry crack off-screen he flinches, then steadies; the lamplight holds on his face.
- **Dialogue:** —
- **Sound:** OFF-SCREEN: a dry crack, like a branch; then silence
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_IBRAHIM_1925.SHORT}, his deep-set eyes moving from face to face, flinches at a sudden sharp sound off frame, then steadies, the warm lantern light below his face holding still. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_IBRAHIM_1925.NEG}, crying out, dropping the lamp, looking at the camera
- **Refs:** CHAR_IBRAHIM_1925_A_front, CHAR_IBRAHIM_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** "The lamp holds." The crack is sound only (file 05 §7.3: never the cut).

### 01.03.011 — KV15, outer corridor — "Packed solid. Linen and pitch."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** DERRY (CHAR_DERRY_1925_A)
- **Action:** Derry, at the chest, eyes down, speaks one short line, matter-of-fact.
- **Dialogue:** DERRY (at the chest): "Packed solid. Linen and pitch."
- **Sound:** steel stops; his voice, dry
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_DERRY_1925.LONG}, eyes lowered to the work below frame, pauses and speaks one short sentence, matter-of-fact, then glances up. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_DERRY_1925.NEG}, hands or instruments in frame
- **Refs:** CHAR_DERRY_1925_A_front, CHAR_DERRY_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** Derry stands frame right of Carter (hold the master's line).

### 01.03.012 — KV15, outer corridor — Hamdi searches the wrappings   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Hamdi's hands; dark resin-stiffened linen
- **Action:** An older man's careful hands, a gold watch chain glinting above, part folds of dark, resin-stiffened linen gently and slowly.
- **Dialogue:** —
- **Sound:** stiff linen crackling softly
- **PROMPT:** Insert, 100mm macro lens, locked-off: an older man's careful brown hands, a gold watch chain glinting across the dark waistcoat just above, part folds of dark, resin-stiffened linen very gently, fingertips moving slowly and lightly. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, {CHAR_HAMDI_1925.NEG}, skin, body visible under the linen, amulets being pulled, blood, instruments
- **Refs:** CHAR_HAMDI_1925_A_full, LOC_KV15_LAB_1925_DAY
- **Continuity:** Linen only, dark and stiff; nothing beneath is seen. "Gently, as if the boy could feel it" (performance, not prompt).

### 01.03.013 — KV15, outer corridor — "No heart scarab."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HAMDI (CHAR_HAMDI_1925_A)
- **Action:** Hamdi straightens slightly and speaks two short sentences, grave and exact.
- **Dialogue:** HAMDI: "No heart scarab. Every king is buried with one over the heart."
- **Sound:** his low voice; the stove
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HAMDI_1925.SHORT}, {CHAR_HAMDI_1925.WARD_A}, straightens slightly behind round gold-rimmed spectacles and speaks two short sentences, grave and exact, his patient eyes on the work below frame. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: grave and exact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_HAMDI_1925.NEG}, smiling
- **Refs:** CHAR_HAMDI_1925_A_front, CHAR_HAMDI_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** Real anchor: no heart scarab was found (file 03 §3). Hamdi frame left of Carter.

### 01.03.014 — KV15, outer corridor — "Perhaps they forgot."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** CARTER (CHAR_CARTER_1925_A)
- **Action:** Carter, not looking up, speaks one short dismissive sentence.
- **Dialogue:** CARTER: "Perhaps they forgot."
- **Sound:** heat; a fly
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_CARTER_1925.SHORT} speaks one short sentence without looking up, a slight shrug of his rolled shirtsleeves, his eyes still far away. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: dry, impatient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_CARTER_1925.NEG}, laughing
- **Refs:** CHAR_CARTER_1925_A_front, LOC_KV15_LAB_1925_DAY
- **Continuity:** Same framing as 01.03.009.

### 01.03.015 — KV15, outer corridor — "They never forget the heart."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** HAMDI (CHAR_HAMDI_1925_A)
- **Action:** Hamdi lifts his eyes to Carter and speaks one short sentence, quietly final.
- **Dialogue:** HAMDI: "They never forget the heart."
- **Sound:** his voice; then silence and heat
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_HAMDI_1925.SHORT} lifts his patient dark eyes toward his colleague off frame right and speaks one short sentence, quiet and final, then holds the look. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: grave and exact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_HAMDI_1925.NEG}, smiling
- **Refs:** CHAR_HAMDI_1925_A_front, CHAR_HAMDI_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Continuity:** Eyeline to frame right (Carter). Hold the silence into 01.03.016 ("Silence. Heat.").

### 01.03.016 — KV15, outer corridor — THUMP: only Ibrahim hears it   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** IBRAHIM (CHAR_IBRAHIM_1925_A), PROP_LAMP_1925 (trembling)
- **Action:** Ibrahim goes still; his eyes lift toward the dark lower end of the corridor; the lantern in his hand trembles and its light shivers across the gold below frame.
- **Dialogue:** —
- **Sound:** THUMP: one faint heartbeat, from the dark; nobody else reacts
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_IBRAHIM_1925.SHORT} goes suddenly still, his eyes lifting toward the dark lower end of the corridor, as the lantern in his hand trembles and its amber light shivers across his face and a gleam of gold below him. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_TREMBLE}. Mood: wonder and dread held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_IBRAHIM_1925.NEG}, crying out, dropping the lamp, looking at the camera
- **Refs:** CHAR_IBRAHIM_1925_A_front, CHAR_IBRAHIM_1925_A_34, PROP_LAMP_1925_REF, LOC_KV15_LAB_1925_DAY
- **Continuity:** Lighting variant DAY → TREMBLE for this shot only. The heartbeat from 1.1 returns; the lower (dark) end of the corridor is frame left, away from the entrance.

### 01.03.017 — KV15, outer corridor — "Steady, Ibrahim. And look."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HAMDI (CHAR_HAMDI_1925_A)
- **Action:** Hamdi, not looking up from the work, speaks two quiet sentences in Egyptian Arabic.
- **Dialogue:** HAMDI (in Egyptian Arabic; subtitled; not looking up): "Steady, Ibrahim. And look. Someone in this room should."
- **Sound:** his voice, low; the lantern's wire bail creaks, then settles
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HAMDI_1925.SHORT}, eyes still on the work below frame, speaking in Egyptian Arabic, two quiet sentences, low and steady, the lantern light below him settling. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_HAMDI_1925.NEG}, looking at the camera, smiling
- **Refs:** CHAR_HAMDI_1925_A_front, CHAR_HAMDI_1925_A_34, LOC_KV15_LAB_1925_DAY
- **Flags:** COMP
- **Comp:** subtitle | "Steady, Ibrahim. And look. Someone in this room should." | lower third, two lines (§13.7) | line in → out | seq 01 subtitle file (Arabic source line recorded by a native Egyptian speaker)
- **Continuity:** Hamdi speaks without looking up; the first Egyptian Arabic in the film.

### 01.03.018 — KV15, outer corridor — Ibrahim looks   (4 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** IBRAHIM (CHAR_IBRAHIM_1925_A)
- **Action:** Ibrahim lowers his eyes to the table and looks, steadily; the lantern stills.
- **Dialogue:** —
- **Sound:** silence; heat
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_IBRAHIM_1925.SHORT} breathes once and lowers his eyes to the table below frame, looking steadily now, the lantern light on his face stilled. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_IBRAHIM_1925.NEG}, looking at the camera, tears
- **Refs:** CHAR_IBRAHIM_1925_A_front, LOC_KV15_LAB_1925_DAY
- **Continuity:** The witness who looks: rhymes with Nour watching the mouth in 01.05.

### 01.03.019 — KV15, outer corridor — "Hold that light."   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** BURTON (CHAR_BURTON_1925_A), PROP_BURTON_PLATES (camera)
- **Action:** Burton, behind the plate camera, glances up from the ground glass, speaks one short line and lifts the shutter release.
- **Dialogue:** BURTON: "Hold that light."
- **Sound:** a dark-slide pulled; his voice; a breath held
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_BURTON_1925.LONG}, stands behind {PROP_BURTON_PLATES.SHORT}, glances up from the camera toward the lamp and speaks one short sentence, one hand lifting the shutter release. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_DAY}. Mood: calm, practised, precise. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {CHAR_BURTON_1925.NEG}, flash powder smoke clouds, visible photographs, image on the plates
- **Refs:** CHAR_BURTON_1925_A_front, CHAR_BURTON_1925_A_full, PROP_BURTON_PLATES_REF, LOC_KV15_LAB_1925_DAY
- **Continuity:** Burton at the foot of the table (frame right, near the entrance); eyeline up-left to the lamp. Flash source off-screen ([[verify: Burton's lighting]]). The plates show no image, ever.

### 01.03.020 — KV15, outer corridor — The flash   (4 s)
- **Shot:** Medium wide shot, anamorphic 40mm, tripod height · **Move:** locked-off
- **In frame:** the corridor, the table on the frame's axis, Ibrahim's raised lantern at upper frame centre
- **Action:** The corridor holds perfectly still for a breath, everyone frozen for the exposure; then it bursts into one hard white flash.
- **Dialogue:** —
- **Sound:** a held breath; the stove; the flash's dry crack; a hum rises through the white
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off at tripod height: down the long axis of the white-draped table, the lantern held high at the top centre of frame, the men around the table hold perfectly still for a breath, then the corridor suddenly bursts into a single hard white flash. Setting: {LOC_KV15_LAB_1925.SHORT}, in the morning. Lighting: {LOC_KV15_LAB_1925.LIGHT_FLASH}. Mood: a moment fixed forever. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_1925}, {NEG_REMAINS}, explosion, fire, smoke cloud, body visible on the table, faces turned to the camera
- **Refs:** LOC_KV15_LAB_1925_DAY, LOC_KV15_LAB_1925_FLASH, PROP_LAMP_1925_REF
- **Flags:** COMP
- **Comp:** flash | 1–2 frames of LIGHT_FLASH, then 2 pure white frames | full frame | end of clip | white frames built in comp (§13.6); MATCH CUT into 01.04.001
- **Continuity:** Matched composition: lantern at upper frame centre = the gantry projector ring in 01.05.001; table axis = cradle axis. Ibrahim has lifted the lantern for the exposure on Burton's line. The men are backs and silhouettes only (no face-led framing). Sepia → cold fluorescent on the white.

## 01.04 — INT. LIVERPOOL X-RAY ROOM - NIGHT (1968)

### 01.04.001 — X-ray room — The white is a lightbox   (6 s)
- **Shot:** Medium shot, anamorphic 40mm · **Move:** slow pull-back
- **In frame:** a wall lightbox with one film; the reading room
- **Action:** From a field of flat white the camera eases back to reveal a humming wall lightbox with one dark film clipped to it, in a small green-walled room.
- **Dialogue:** —
- **Sound:** the flash's hum becomes the lightbox's electric hum; a fluorescent tube ticking
- **PROMPT:** Medium shot, anamorphic 40mm lens, slow pull-back: from a field of flat white the camera eases back to reveal a glowing wall lightbox with a single dark film clipped to it, faint pale shapes on the film, the edges of a small pale-green room coming into view. Setting: {LOC_XRAY_1968.LONG}, at night. Lighting: {LOC_XRAY_1968.LIGHT_NIGHT}. Mood: quiet, clinical, late. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_REMAINS}, {NEG_PLATE}, modern objects, LED light, flat-screen monitors, computers, digital displays, readable labels on the film, recognisable anatomy on the film
- **Refs:** LOC_XRAY_1968_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "LIVERPOOL. 1968." | lower left, small (§13.7) | 0:01 → 0:04 | seq 01 SUPER file; film image | a new, generic, non-diagnostic chest silhouette of a young man, never the real radiographs (file 03 §4) | tracked to the lightbox | full clip | VFX asset
- **Continuity:** Match cut from 01.03.020's white. Lightboxes on the wall facing camera. [[verify: plates read in Liverpool? (X-rayed in Egypt, portable unit)]]

### 01.04.002 — X-ray room — The pen down the centre   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** a fountain pen in a man's hand; the film on the lightbox
- **Action:** A pen tip slides slowly down the centre of the film, where bone should be.
- **Dialogue:** —
- **Sound:** the lightbox hum; the faint tick of the pen on the film
- **PROMPT:** Insert, 100mm macro lens, locked-off: the capped tip of a fountain pen held in a man's pale hand, a white coat cuff at the wrist, slides slowly down the centre of a dark film on a glowing lightbox, over faint pale shapes. Setting: {LOC_XRAY_1968.SHORT}, at night. Lighting: {LOC_XRAY_1968.LIGHT_NIGHT}. Mood: clinical, precise, uneasy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_REMAINS}, {CHAR_RADIOLOGIST_1968.NEG}, readable labels on the film, recognisable anatomy on the film, digital screen
- **Refs:** LOC_XRAY_1968_NIGHT, CHAR_RADIOLOGIST_1968_A_full
- **Flags:** COMP
- **Comp:** film image | the same generic chest silhouette as 01.04.001, the central column empty (no sternum, no front ribs) | tracked to the film | full clip | VFX asset
- **Continuity:** Radiologist stands frame left of the lightbox; the pen travels top to bottom.

### 01.04.003 — X-ray room — "No sternum. No front ribs."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RADIOLOGIST (CHAR_RADIOLOGIST_1968_A)
- **Action:** The radiologist, lit by the lightbox, studies the film and speaks two short sentences.
- **Dialogue:** RADIOLOGIST: "No sternum. No front ribs."
- **Sound:** his tired voice; the hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RADIOLOGIST_1968.LONG}, his face lit flat white by a lightbox just off frame right, studies a film and speaks two short sentences, puzzled. Setting: {LOC_XRAY_1968.SHORT}, at night. Lighting: {LOC_XRAY_1968.LIGHT_NIGHT}. Mood: dry, literal calm turning to unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_RADIOLOGIST_1968.NEG}, modern objects, LED light, computers, smiling
- **Refs:** CHAR_RADIOLOGIST_1968_A_front, CHAR_RADIOLOGIST_1968_A_34, LOC_XRAY_1968_NIGHT
- **Continuity:** A generic radiologist, never a likeness of the real researcher (bible §7, 1.4). Eyeline to frame right (the lightbox).

### 01.04.004 — X-ray room — "And the heart?" "...Gone."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** RADIOLOGIST (CHAR_RADIOLOGIST_1968_A)
- **Action:** At a question from off frame the pen stops; he pauses, then says one word.
- **Dialogue:** ASSISTANT (O.S.): "And the heart?" · RADIOLOGIST: "...Gone."
- **Sound:** the assistant's voice off-screen right; the pen stops; the hum; the single word
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_RADIOLOGIST_1968.SHORT} hears a question from off frame right, goes still with his pen raised, holds a long beat, then speaks one quiet word, eyes on the lightbox. Setting: {LOC_XRAY_1968.SHORT}, at night. Lighting: {LOC_XRAY_1968.LIGHT_NIGHT}. Mood: a small chill. {SUFFIX}
- **NEGATIVE:** {NEG}, {CHAR_RADIOLOGIST_1968.NEG}, modern objects, LED light, computers, second face in frame
- **Refs:** CHAR_RADIOLOGIST_1968_A_front, CHAR_RADIOLOGIST_1968_A_34, LOC_XRAY_1968_NIGHT
- **Continuity:** The assistant (CHAR_XRAY_ASSISTANT_1968) is voice only, off frame right (file 03 geography). Pen in his right hand, raised.

### 01.04.005 — X-ray room — The tube stutters out   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** a toggle switch below the lightbox; the lightbox edge; a finger
- **Action:** A finger presses the switch; the white glow blinks, stutters, and flares once before going dark.
- **Dialogue:** —
- **Sound:** a heavy switch click; the tube's stutter; one bright buzz; then the flash's hum rising into the next scene
- **PROMPT:** Insert, 100mm macro lens, locked-off: a man's finger presses down a heavy toggle switch beneath a glowing lightbox, and the white glow blinks, stutters, then flares once brightly before everything goes dark. Setting: {LOC_XRAY_1968.SHORT}, at night. Lighting: {LOC_XRAY_1968.LIGHT_NIGHT}. Mood: abrupt, final. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_REMAINS}, modern objects, LED light, sparks, electrical fire
- **Refs:** LOC_XRAY_1968_NIGHT
- **Flags:** COMP
- **Comp:** flash | the last flare pushed to 2 frames of pure white | full frame | end of clip | MATCH CUT into 01.05.001 (§13.6)
- **Continuity:** Cold fluorescent (GRADE_1968) → museum white (GRADE_2033_MUSEUM) on the white frames.

## 01.05 — INT. GEM CONSERVATION CENTRE, MUMMY LAB - NIGHT (1 November 2033)

### 01.05.001 — Conservation lab — The flash is a projector   (4 s)
- **Shot:** Medium wide shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** the gantry ring (upper frame centre); the cradle on the frame's axis
- **Action:** Down the long axis of the cradle, the ring-shaped projector gantry at the top of frame bursts white, then settles into a soft pale-cyan wash over the white sheet.
- **Dialogue:** —
- **Sound:** a projector's snap and rising fan whine; a clean, cold room tone
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, locked-off: down the long axis of a low titanium cradle draped in a white sheet, a ring-shaped gantry of small projectors hanging at the top centre of frame bursts white, then settles into a soft pale-cyan wash over the sheet below. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: clinical, hushed, precise. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, visible faces, readable screen text, hospital-horror lighting
- **Refs:** LOC_GEM_CC_READING, CHAR_TUT_CRADLE_2033
- **Flags:** COMP
- **Comp:** match cut | 2 pure white frames at the head, the projector burst settling | full frame | first 10 frames | §13.6
- **Continuity:** Matched composition with 01.03.020: projector ring = the lantern's position, cradle axis = table axis. GRADE_2033_MUSEUM from here. Camera from the foot of the cradle (geography lock: observation wall frame right, Tut's bay door back left).

### 01.05.002 — Conservation lab — Establishing: the glass enclosure   (7 s)
- **Shot:** Wide establishing shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** two SHABTI flanking the cradle; the body under the sheet; NOUR (small, at the lectern, frame left); figures behind the observation wall (frame right, in shadow)
- **Action:** Inside a sealed glass enclosure two robots stand motionless either side of the sheeted cradle; outside the glass a woman waits at a lectern; figures stand in shadow behind the observation wall.
- **Dialogue:** —
- **Sound:** room tone; a faint ceramic tick; the projectors' fans
- **PROMPT:** Wide establishing shot, anamorphic 32mm lens, locked-off from the foot of the cradle: inside a sealed glass enclosure two identical robots, each {UNIT_SHABTI.SHORT}, stand perfectly still on either side of the sheeted cradle, while {CHAR_NOUR.SHORT} waits at a lectern outside the glass at frame left and figures stand in shadow behind the observation wall at frame right. Setting: {LOC_GEM_CC.LONG}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: clinical symmetry, held breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, readable screen text, detached body parts, body exposed beyond the collarbones
- **Refs:** LOC_GEM_CC_READING, UNIT_SHABTI_REF_A, CHAR_NOUR_A_full, CHAR_TUT_CRADLE_2033
- **Flags:** COMP
- **Comp:** SUPER | "GRAND EGYPTIAN MUSEUM, GIZA. 1 NOVEMBER 2033." | lower left, small (§13.7) | 0:01 → 0:05 | seq 01 SUPER file
- **Continuity:** Symmetrical frame. The enclosure is a glass box around the cradle; Nour's lectern outside it at frame left; the observation window high at frame right. The prompt never names the museum.

### 01.05.003 — Conservation lab — Top-down: the sheet and the cut map   (6 s)
- **Shot:** Top-down shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** the body on the cradle (CHAR_TUT_CRADLE_2033); the projected cut map (COMP); shabti hands at the cradle edges
- **Action:** Directly above: the slight figure under the white sheet, a pale-cyan wash of projected light over it from neck to ankles; the robots' long hands rest at the cradle's edges.
- **Dialogue:** —
- **Sound:** projector fans; silence
- **PROMPT:** Top-down shot, anamorphic 32mm lens, locked-off: directly above {CHAR_TUT_CRADLE_2033.LONG}, a soft wash of projected pale-cyan light lies over the sheet from neck to ankles, and the long pale ceramic hands of two robots rest at the cradle's edges. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: reverent, clinical, utterly still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, body exposed beyond the collarbones, visible limbs, readable lines or numbers
- **Refs:** CHAR_TUT_CRADLE_2033, PROP_CUTMAP_PROJECTION_REF, UNIT_SHABTI_REF_A, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** cut map | PROP_CUTMAP_PROJECTION: the 1925 cut map as a pale-cyan line diagram, neck to ankles, cut lines at neck, shoulders, elbows, wrists, hips, knees, ankles (an outline, never anatomy) | projected above the sheet, tracked | full clip | VFX asset
- **Continuity:** Lock gap 3: the CRADLE lock's gold neck ring is held dark in comp until 01.05.013. The single top-down of 1.5 (§4.4).

### 01.05.004 — Conservation lab — Nour at the lectern; the old lamp   (6 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A); the 1925 lantern, unlit (PROP_LAMP_1925, COLD_2033)
- **Action:** Nour stands at a lectern outside the glass, pages before her and the old dented lantern beside them, looking through the glass toward the cradle.
- **Dialogue:** —
- **Sound:** room tone; a page settling
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, stands at a lectern outside a glass enclosure, pages before her and an old hurricane lantern, {PROP_LAMP_1925.STATE_COLD_2033}, looking through the glass toward the cradle, perfectly composed. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, lit lantern, flame, readable pages, readable badge
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full, PROP_LAMP_1925_REF (unlit 2033 variant), LOC_GEM_CC_READING
- **Continuity:** Nour look A (L0): olive field jacket, cream shirt, glasses on the cord (off), silver pendant at the throat (its lettering never legible). The lantern stands to her right on the lectern. Lock gap 2 (lamp SHORT not pasted).

### 01.05.005 — Conservation lab — Behind the observation window   (6 s)
- **Shot:** Medium wide shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A), ADAEZE (CHAR_ADAEZE_A), RAMI (CHAR_RAMI_A) with PROP_RAMI_NOTEBOOK
- **Action:** Behind the tall window, Tomas, Adaeze with an open laptop, and Rami hugging his notebook stand side by side looking down into the lab.
- **Dialogue:** —
- **Sound:** the observation room's muffled hush; a laptop fan
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: behind a tall observation window {CHAR_TOMAS.SHORT}, {CHAR_ADAEZE.SHORT}, holding an open laptop whose screen glows faintly with abstract lines, and {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, hugging to his chest {PROP_RAMI_NOTEBOOK.SHORT}, stand side by side looking down into the lab. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass lighting their faces softly. Mood: held breath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_RAMI.NEG}, readable laptop screen, readable notebook label, reflections doubling faces
- **Refs:** CHAR_TOMAS_A_full, CHAR_ADAEZE_A_full, CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_A_full, PROP_RAMI_NOTEBOOK_REF, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** notebook label | "100 QUESTIONS FOR TUTANKHAMUN" (handwritten) | on the notebook's white label, tracked | full clip | handwriting asset
- **Continuity:** Locked-off master: three faces allowed. Left to right: Tomas (very tall), Adaeze, Rami. Tomas look A (sleeves rolled), Adaeze A (navy blazer, grey hoodie, blank lanyard), Rami A (yellow windbreaker; no splint until 3.6). Eyelines down and to frame left (the cradle).

### 01.05.006 — Conservation lab — Tarek watches the robots; Hale's palm on the glass   (6 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A), HALE (CHAR_HALE_A)
- **Action:** Tarek watches the robots, not the body, eyes narrowed; beside him Hale rests one palm flat on the glass.
- **Dialogue:** —
- **Sound:** a palm pressing glass; Tarek's slow breath through the nose
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, watches the robots in the lab below rather than the cradle, eyes narrowed, while beside him {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_A}, leans close and rests one palm flat on the glass. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on their faces. Mood: military exactness beside open hunger. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_HALE.NEG}, weapon drawn, reflections doubling faces
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_full, CHAR_HALE_A_front, CHAR_HALE_A_full, LOC_GEM_CC_READING
- **Continuity:** Tarek look A (pressed uniform, beret low to the right, holstered pistol untouched). Hale look A. Hale's palm on the glass from here to 01.05.026.

### 01.05.007 — Conservation lab — "I'm holding it while they put him back."   (7 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A); her fingers on the lantern
- **Action:** Nour rests two fingers on the old lamp and speaks two quiet sentences, eyes on the cradle.
- **Dialogue:** NOUR (two fingers on the old lamp; quietly): "My great-grandfather held this while they cut him apart. I'm holding it while they put him back."
- **Sound:** her voice, close; room tone
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT} rests two fingers on the cold brass of an old hurricane lantern at the edge of frame and, speaking quietly, says two sentences, her deep-set eyes on the cradle through the glass. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears streaming, lit lantern, flame
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, PROP_LAMP_1925_REF (unlit 2033 variant), LOC_GEM_CC_READING
- **Continuity:** The lamp Ibrahim held in 01.03. Her fingers rest on the brass (not the globe). Glasses still hanging on the cord.

### 01.05.008 — Conservation lab — SESHAT: "the rite is yours"   (7 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** SHABTI (UNIT_SHABTI) at the head of the cradle
- **Action:** The robot at the head of the cradle stands perfectly still, then turns its head slowly toward the lectern outside the glass.
- **Dialogue:** SESHAT (V.O.; warm, unhurried, from everywhere): "Thank you, Dr. Kamel. As the Supreme Council of Antiquities requires, the rite is yours." (beat) "I will follow along."
- **Sound:** SESHAT's voice everywhere at once; a single faint ceramic tick at the neck joint
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: at the head of the sheeted cradle, {UNIT_SHABTI.LONG}, stands perfectly still, then turns its head slowly toward frame left, toward the lectern outside the glass, and holds there. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, robot gesturing, robot speaking with a mouth, readable screens
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_CC_READING
- **Continuity:** Unit-led shot: UNIT_SHABTI LONG (one-LONG rule, file 05 §5.2). SESHAT is V.O. (no sync; the unit has no mouth). The slit stays steady (the single brightening is saved for "Here am I", 01.06.006). Head leads; the body stays still.

### 01.05.009 — Conservation lab — "Say one for us, Doctor."   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A)
- **Action:** Hale, palm flat on the glass, speaks one short line with a faint smile.
- **Dialogue:** HALE: "Say one for us, Doctor."
- **Sound:** his voice through the observation-room speaker, slightly futzed
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, his palm flat on the observation glass, speaks one short sentence with a faint, hopeful smile, looking down into the lab. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on his face. Mood: a believer's hope, lightly worn. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, reflections doubling his face
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC_READING
- **Continuity:** Eyeline down to frame left (Nour at the lectern). His palm stays on the glass.

### 01.05.010 — Conservation lab — "I'm reading, not praying."   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour answers without looking up, then lifts the reading glasses from their cord and puts them on.
- **Dialogue:** NOUR: "I'm reading, not praying."
- **Sound:** her dry voice; the glasses' cord ticking against the lectern
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT} speaks one short sentence without looking up, then lifts the narrow black reading glasses from their cord and puts them on, eyes dropping to the page. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, smiling, readable pages
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** Glasses ON from here to the end of the scene (she puts them on only to read).

### 01.05.011 — Conservation lab — The shabti raise their hands over the throat   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** two SHABTI (UNIT_SHABTI); the body under the sheet (CHAR_TUT_CRADLE_2033)
- **Action:** The two robots raise their long hands together and hold them, palms down, just above the young man's throat.
- **Dialogue:** —
- **Sound:** two faint ceramic ticks, in unison
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: facing an identical twin across the cradle, {UNIT_SHABTI.LONG}, raises its long slim hands in unison with its twin and holds them, palms down, just above the throat of {CHAR_TUT_CRADLE_2033.SHORT}. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, robots gripping the body, body exposed beyond the collarbones
- **Refs:** UNIT_SHABTI_REF_A, CHAR_TUT_CRADLE_2033, LOC_GEM_CC_READING
- **Continuity:** Groups move in unison (file 02 movement grammar). Robot A at the head (frame left of the cradle), robot B opposite.

### 01.05.012 — Conservation lab — Nour reads the rite   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour reads aloud from the page in a measured ritual cadence, exact and unhurried.
- **Dialogue:** NOUR (in Middle Egyptian, unsubtitled; SESHAT's echo carries the rite): "Thou hast received thy head, and thy bones have been brought unto thee before Keb."
- **Sound:** her recitation, dry and clear; SESHAT's echo begins under
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, glasses on, reciting aloud in a measured, ritual cadence in an ancient language, reads from the page on the lectern, glancing up once through the glass toward the cradle. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, praying hands, closed eyes, readable pages
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** Unsubtitled: SESHAT's English echo (V.O.) carries the meaning in 01.05.013. Middle Egyptian recorded first with the consultant; lip-synced.

### 01.05.013 — Conservation lab — A seam of gold light at the neck   (6 s)
- **Shot:** Extreme close-up, 100mm macro · **Move:** locked-off
- **In frame:** the neck at the sheet line (CHAR_TUT_CRADLE_2033); shabti fingertips
- **Action:** Long ceramic fingertips trace slowly around the base of the neck, a hair's breadth above the skin; a thin line of light follows them and closes into a ring.
- **Dialogue:** SESHAT (V.O.; a checklist): "'Thou hast received thy head.' Cervical seam: closing."
- **Sound:** a thin crystalline tone rising as the ring closes; SESHAT's voice
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: at the collarbone line of a white sheet, long bone-white ceramic fingertips trace slowly around the base of the neck of {CHAR_TUT_CRADLE_2033.SHORT}, a hair's breadth above the skin, and a thin line of light follows them, closing into a ring and settling. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, wound, incision, stitches, gap in the neck, fingers pressing into skin, sparks
- **Refs:** CHAR_TUT_CRADLE_2033, CHAR_TUT_A0_profile, UNIT_SHABTI_REF_A, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** seam of gold light | a warm gold line drawn behind the fingertips, closing into a ring and settling to the thin gold neck seam (file 01 seam 1: 2 cm above the collarbones, dipping at the throat notch) | tracked to the neck | frames 12–130 | light element (§13.9)
- **Continuity:** From here the neck ring is on (CRADLE lock's "gold light ringing his neck"; later CHAR_TUT's polished gold seam ring). The skin is smooth either side; no redness.

### 01.05.014 — Conservation lab — Bones: registered   (5 s)
- **Shot:** Top-down shot, anamorphic 32mm · **Move:** locked-off
- **In frame:** the body under the sheet (CHAR_TUT_CRADLE_2033); the projected diagram (COMP)
- **Action:** From above, points of projected light over the sheet brighten one after another, from the shoulders down to the ankles.
- **Dialogue:** SESHAT (V.O.): "Bones: registered."
- **Sound:** a soft chime per joint, rising, like a city switching on
- **PROMPT:** Top-down shot, anamorphic 32mm lens, locked-off: directly above {CHAR_TUT_CRADLE_2033.SHORT}, small points of pale projected light over the white sheet brighten one after another from the shoulders down to the ankles, until every point is lit. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: precise, quietly wondrous. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, body exposed beyond the collarbones, visible limbs, readable lines or numbers
- **Refs:** CHAR_TUT_CRADLE_2033, PROP_CUTMAP_PROJECTION_REF, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** cut map | PROP_CUTMAP_PROJECTION joint lines turning gold one by one (shoulders → elbows → wrists → hips → knees → ankles), "like a city switching on" | projected over the sheet, tracked | full clip | VFX asset
- **Continuity:** Same set-up as 01.05.003 (re-use the plate). The gold neck ring is lit (from 01.05.013).

### 01.05.015 — Conservation lab — The nano-adze   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** PROP_NANO_ADZE in shabti fingers
- **Action:** A shabti lifts the nano-adze into the light, the tiny black blade turning to catch it.
- **Dialogue:** —
- **Sound:** a faint ceramic tick; a high glassy ring as the blade catches the light
- **PROMPT:** Insert, 100mm macro lens, slow push-in: {PROP_NANO_ADZE.LONG}, lifted slowly upward into the pale-cyan light above the sheet, the tiny black blade turning a few degrees to catch it. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: reverent, precise. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, scalpel, needle, sparks, human hand
- **Refs:** PROP_NANO_ADZE_REF, UNIT_SHABTI_REF_A, LOC_GEM_CC_READING
- **Continuity:** Rhymes with Ay's iron adze (01.02.006). Held in robot A's right hand.

### 01.05.016 — Conservation lab — "I have opened thy mouth."   (6 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour recites the next words from the page, steady.
- **Dialogue:** NOUR (in Middle Egyptian, unsubtitled): "I have opened thy mouth. I have opened thy two eyes..."
- **Sound:** her recitation; the room silent under it
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, glasses on, reciting aloud in a measured, ritual cadence in an ancient language, two short phrases, her eyes moving from the page to the cradle and back. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, praying hands, closed eyes, readable pages
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** Ay's words from 01.02.007, now in her mouth.

### 01.05.017 — Conservation lab — The adze touches the lips and the eyes   (6 s)
- **Shot:** Extreme close-up, 100mm macro · **Move:** locked-off
- **In frame:** the face at rest (CHAR_TUT_CRADLE_2033); PROP_NANO_ADZE
- **Action:** The tiny black blade touches the parted lips, lifts, touches the left eyelid, then the right.
- **Dialogue:** SESHAT (V.O.): "'I have opened thy mouth.' Mouth: open. Eyes: open."
- **Sound:** three tiny glass-bright ticks; SESHAT's checklist voice
- **PROMPT:** Extreme close-up, 100mm macro lens, locked-off: a tiny black iron adze blade at the tip of a dark stylus, held in long pale ceramic fingers, touches the parted lips of {CHAR_TUT_CRADLE_2033.SHORT}, lifts, touches the left eyelid, then the right. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, pressing into skin, marks on the skin, eyes opening
- **Refs:** CHAR_TUT_CRADLE_2033, CHAR_TUT_A0_front, PROP_NANO_ADZE_REF, LOC_GEM_CC_READING
- **Continuity:** Eyes stay closed in this clip. Gold neck ring lit at the frame's bottom edge. Left eyelid = frame right (he lies face up, head toward the gantry).

### 01.05.018 — Conservation lab — SESHAT finishes her sentence   (7 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour begins the last phrase and is overtaken mid-phrase by SESHAT's voice; her eyes lift from the page to the empty air above the enclosure, then lower; she says nothing.
- **Dialogue:** NOUR (in Middle Egyptian): "...with the iron that cometh forth from Set--" · SESHAT (V.O.): "And the Osiris shall walk and shall talk."
- **Sound:** her voice cut off; SESHAT's warm voice finishing; a held silence
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.SHORT}, glasses on, reciting aloud in a measured, ritual cadence in an ancient language, stops mid-phrase; her eyes lift from the page to the empty air above the enclosure, hold, then lower again, her lips pressed closed. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: dry, literal calm over a flicker of unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, gasping, speaking at the end, readable pages
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** "It has finished her sentence. Nour notices, and says nothing." Lip-sync only the first 2 s (her half-phrase).

### 01.05.019 — Conservation lab — THUMP: the glow   (5 s)
- **Shot:** Medium close-up, anamorphic 50mm · **Move:** slow push-in
- **In frame:** the body under the sheet, mid-chest (CHAR_TUT_CRADLE_2033)
- **Action:** Under the white sheet at mid-chest, a dim glow swells slowly in time with the heartbeat.
- **Dialogue:** —
- **Sound:** THUMP. The HEARTBEAT, back from the dark: the same beat as 1323 and 1925
- **PROMPT:** Medium close-up, anamorphic 50mm lens, slow push-in: on {CHAR_TUT_CRADLE_2033.SHORT}, {CHAR_TUT.STATE_G0}, the faint light under the white sheet swelling slowly once, then again, the face at rest at the top of frame. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: awe held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, visible machinery, exposed chest, bright flare, red light
- **Refs:** CHAR_TUT_CRADLE_2033, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green, about #A6F2C2 core falling off to #3F8F6A, dim, ~6 cm spill through the sheet; here in time with the heartbeat (file 01 table) | mid-chest, tracked | from the first THUMP | glow element
- **Continuity:** Glow state G0 begins (1.5 → 6.2). Eyes still closed.

### 01.05.020 — Conservation lab — The eyes open: wrong   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** slow push-in
- **In frame:** TUT's eyes (CHAR_TUT)
- **Action:** The eyes open, too wide, swimming, unfocused: a newborn's eyes in a king's face.
- **Dialogue:** —
- **Sound:** the heartbeat; a wet flutter of lashes; silence behind the glass
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, slow push-in: the eyes of {CHAR_TUT.LONG}, lying face up under a white sheet, open suddenly, too wide, unfocused and swimming, the pupils drifting without finding anything. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: raw, newborn, disoriented. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing eyes, red eyes, horror-film lighting, blinking rapidly
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_CRADLE_2033, LOC_GEM_CC_READING
- **Continuity:** Lock gap 3: CHAR_TUT (not the CRADLE lock, which says "eyes closed") from here. Tut state 1.5 (file 01 table): no wardrobe (the sheet), G0 glow, nape PORT present but never seen (he lies face up), neck seam intact, no cracks. The one slow push-in to the eyes of 1.5 (§4.4), continued in 01.05.021. Very dark eyes, strong catchlights from the gantry above.

### 01.05.021 — Conservation lab — The eyes open: right   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** slow push-in (continuing)
- **In frame:** TUT's eyes (CHAR_TUT)
- **Action:** The eyes slow, focus, and find the ceiling, the light.
- **Dialogue:** —
- **Sound:** the heartbeat steadying
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, slow push-in, continuing the same camera move at the same speed: the very dark eyes of {CHAR_TUT.SHORT} slow, focus, and settle on the light above, the catchlights sharpening as they find it. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, glowing eyes, red eyes, blinking rapidly
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34
- **Flags:** EXTEND:01.05.020
- **Continuity:** Generated from the last clean frame of 01.05.020 (same move, same speed). Chain length 2.

### 01.05.022 — Conservation lab — The first breath   (4 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT), on the cradle
- **Action:** He drags in one deep breath through parted lips, like a swimmer surfacing; the sheet rises at the collarbones.
- **Dialogue:** —
- **Sound:** one long ragged inhale, loud in the silence
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, lying face up under a white sheet on a titanium cradle, drags in one deep, ragged breath through parted lips, chin lifting, the sheet rising at the collarbones, then holds. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: raw, newborn, disoriented. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, gasping horror, sitting up, bare chest
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_CRADLE_2033, LOC_GEM_CC_READING
- **Continuity:** Profile three-quarter from frame right of the cradle head. Neck seam visible above the sheet.

### 01.05.023 — Conservation lab — Behind the glass, nobody breathes   (4 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A), ADAEZE (CHAR_ADAEZE_A)
- **Action:** Behind the glass, Tomas and Adaeze stand frozen, lips parted, eyes fixed on the cradle.
- **Dialogue:** —
- **Sound:** nothing: room tone only
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: behind the observation glass, {CHAR_TOMAS.SHORT} and {CHAR_ADAEZE.SHORT} stand frozen side by side, lips parted, eyes fixed on the cradle below, neither of them moving. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on their faces. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, {CHAR_ADAEZE.NEG}, reflections doubling faces, readable screens
- **Refs:** CHAR_TOMAS_A_front, CHAR_ADAEZE_A_front, LOC_GEM_CC_READING
- **Continuity:** Tomas frame left (very tall), Adaeze frame right; as in 01.05.005.

### 01.05.024 — Conservation lab — Four syllables   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** TUT's mouth (CHAR_TUT)
- **Action:** His mouth shapes a few soft syllables, barely voiced, soft on the consonants.
- **Dialogue:** TUT (in Late Egyptian; UNSUBTITLED): four syllables ("Is it listening?"; unsubtitled until 2.5)
- **Sound:** the four syllables, soft on the consonants; the heartbeat
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the mouth of {CHAR_TUT.SHORT}, full lips over a visible overbite, speaking softly in an ancient language, a few soft syllables barely voiced, the chin still against the white sheet. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, teeth misaligned differently from the reference, open-mouthed scream
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_profile
- **Continuity:** Record with the consultant first; lip-sync from that audio (§9.6: real mouth shapes, the plot turns on lip-reading). No subtitle. Check the overbite after sync (§9.1 step 5). Never prompt a lisp.

### 01.05.025 — Conservation lab — Nour's eyes: "He says: 'Not again.'"   (5 s)
- **Shot:** Extreme close-up, anamorphic 100mm · **Move:** locked-off
- **In frame:** NOUR's eyes (CHAR_NOUR_A)
- **Action:** Nour's eyes, behind her reading glasses, fixed on his mouth, unblinking, reading.
- **Dialogue:** SESHAT (V.O.): "He says: 'Not again.'"
- **Sound:** SESHAT's warm translation; the heartbeat
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: the deep-set dark-brown eyes of {CHAR_NOUR.SHORT}, behind narrow black reading glasses, fixed on something below frame, unblinking, reading closely, a faint crease forming between the brows. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill on her face. Mood: dry, literal calm; something does not fit. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, tears, blinking rapidly
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** Lip-reading coverage pair with 01.05.024 (§9.6: CU mouth + CU Nour's eyes). She is reading his lips, and SESHAT's translation does not match.

### 01.05.026 — Conservation lab — Hale breathes out   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A)
- **Action:** Hale, palm still on the glass, lets out one shaking breath: half a laugh, half a sob.
- **Dialogue:** —
- **Sound:** his breath breaking; murmurs rising behind the glass
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_HALE.SHORT}, palm still flat on the glass, lets out one shaking breath, half a laugh and half a sob, his pale eyes wet. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, reflections doubling his face
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC_READING
- **Continuity:** Same set-up as 01.05.009.

### 01.05.027 — Conservation lab — Rami laughs and cries; Tarek's handkerchief   (6 s)
- **Shot:** Two-shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A), TAREK (CHAR_TAREK_A)
- **Action:** Rami laughs and cries at once; without looking, Tarek holds out a folded handkerchief; Rami takes it.
- **Dialogue:** —
- **Sound:** Rami's wet laugh; cloth passed
- **PROMPT:** Two-shot, anamorphic 50mm lens, locked-off: {CHAR_RAMI.SHORT}, {CHAR_RAMI.WARD_A}, laughs and cries at once, and beside him {CHAR_TAREK.SHORT}, his eyes still on the robots below, holds out a folded white handkerchief without looking; the younger man takes it. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on their faces. Mood: reckless joy beside military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, {CHAR_TAREK.NEG}, readable notebook label, hands fused, reflections doubling faces
- **Refs:** CHAR_RAMI_A_34, CHAR_RAMI_A_full, CHAR_TAREK_A_34, CHAR_TAREK_A_full, PROP_RAMI_NOTEBOOK_REF, LOC_GEM_CC_READING
- **Continuity:** Rami frame left, notebook under his left arm; Tarek frame right, eyeline down-left to the robots. The handkerchief passes right → left.

### 01.05.028 — Conservation lab — Tomas sits down   (4 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A)
- **Action:** Tomas sinks slowly down into a chair at the observation desk, his eyes never leaving the lab below.
- **Dialogue:** —
- **Sound:** a chair's soft give; a long exhale
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, sinks slowly down into a chair at a desk of dark screens, his eyes never leaving the lab below, his mouth slightly open. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on his face. Mood: exhausted wonder. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, readable screens, falling
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_full, LOC_GEM_CC_READING
- **Continuity:** The bioengineer who rebuilt the body. One beat for a 4 s clip (sits; the hands-over-face business was cut, file 05 §5.4). Screens on the desk dark (abstract glow only).

### 01.05.029 — Conservation lab — "He's got jokes!"   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A)
- **Action:** Rami, wiping his eyes under his glasses with the handkerchief, laughs and blurts one line.
- **Dialogue:** RAMI: "'Not again'! He's got jokes!"
- **Sound:** his laugh through tears; futzed through the glass
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.SHORT}, dabbing his eyes under his glasses with a white handkerchief, laughs and speaks one quick breathless sentence, grinning wide. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill through the glass on his face. Mood: reckless joy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, handkerchief over the mouth, reflections doubling his face
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC_READING
- **Continuity:** Mouth unobstructed (the handkerchief stays at his eyes). The chipped front tooth visible in the grin: check after sync.

### 01.05.030 — Conservation lab — Nour does not react   (4 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A)
- **Action:** Nour stays perfectly still at the lectern while laughter carries behind the glass; she was watching his mouth.
- **Dialogue:** —
- **Sound:** muffled laughter through the observation glass; her stillness
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.SHORT}, glasses on, stays perfectly still at the lectern while muffled laughter carries from behind her, her eyes fixed on the head of the cradle, her face unreadable. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}, pale-cyan spill softly lighting her face. Mood: dry, literal calm; quietly certain. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, smiling, laughing
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC_READING
- **Continuity:** Eyeline to frame right, to the head of the cradle. A fountain pen in her right hand, low.

### 01.05.031 — Conservation lab — The pen taps the glass   (5 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Nour's hand, a fountain pen; the enclosure glass
- **Action:** Her pen taps the enclosure glass quietly: once, twice, three times, four.
- **Dialogue:** —
- **Sound:** four small, evenly spaced taps of a pen cap on glass
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hand holding a black fountain pen taps the pen's cap against a clear glass wall, quietly and slowly, again and again, evenly spaced, the white cradle soft and out of focus beyond the glass. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: private, deliberate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, cracks in the glass, fused fingers, extra fingers
- **Refs:** CHAR_NOUR_A_full, LOC_GEM_CC_READING
- **Continuity:** Cut the clip to exactly FOUR taps in the edit (counting is unreliable in generation, §5.4); the sound carries four. Right hand.

### 01.05.032 — Conservation lab — The dark eyes find her   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT), on the cradle
- **Action:** Inside the glass, his dark eyes move toward the sound and find her.
- **Dialogue:** —
- **Sound:** the fourth tap's ring fading; the heartbeat
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.SHORT}, lying face up under a white sheet on a titanium cradle, slowly turns his very dark eyes toward frame left, toward a small sound, and holds them there, finding someone. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, {CHAR_TUT.NEG}, head turning fast, glowing eyes, sitting up
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_CRADLE_2033, LOC_GEM_CC_READING
- **Continuity:** Eyeline to frame left (Nour at the lectern, outside the glass), matching 01.05.030's eyeline to frame right. The chest is below frame here: glow G0 continues under the sheet off-frame (no glow comp in this clip; it returns in 01.05.033).

### 01.05.033 — Conservation lab — Hold   (6 s)
- **Shot:** Over-the-shoulder shot, anamorphic 50mm · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A, foreground shoulder, no face); TUT on the cradle (CHAR_TUT); two SHABTI
- **Action:** Past Nour's shoulder, through the glass wall, he lies with his eyes open and turned toward her; the two robots stand still either side. Hold.
- **Dialogue:** —
- **Sound:** the heartbeat; room tone; nothing else
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, slow push-in: past the tied-back dark curls and olive-jacketed shoulder of {CHAR_NOUR.SHORT} in the soft foreground, through a glass wall, {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_G0}, lies under a white sheet on a titanium cradle with his eyes open and turned toward her, a robot standing still on either side. Setting: {LOC_GEM_CC.SHORT}, at night. Lighting: {LOC_GEM_CC.LIGHT_READING}. Mood: two witnesses, perfectly still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_REMAINS}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, foreground face visible, reflections doubling faces
- **Refs:** CHAR_NOUR_A_full, CHAR_TUT_A0_front, CHAR_TUT_CRADLE_2033, UNIT_SHABTI_REF_A, LOC_GEM_CC_READING
- **Flags:** COMP
- **Comp:** chest glow G0 | as 01.05.019, dim swell every beat | under the sheet, tracked | full clip | glow element
- **Continuity:** "Hold." then CUT TO main titles. The scene stays in the READING variant throughout; the heading map's NIGHT variant (lights up) is reached off-screen and opens the lab in Seq 2. Push under 10% of frame.

## 01.06 — MAIN TITLES - SESHAT'S WORLD

### 01.06.001 — Main titles — Archive: the start line   (6 s)
- **Shot:** Wide shot, long zoom lens, documentary style · **Move:** subtle handheld
- **In frame:** early humanoid robots (UNIT_EARLY_HUMANOID) with handlers; crowds behind barriers
- **Action:** Archive-style: at a city road-race start line, small awkward robots wobble on the spot beside their human handlers; spectators hold up phones behind the barriers.
- **Dialogue:** —
- **Sound:** crowd chatter; a race announcer's PA (unintelligible); servo whine; main-title music begins
- **PROMPT:** Wide shot, long zoom lens, documentary style, subtle handheld: at a start line, a row of small robots, each {UNIT_EARLY_HUMANOID.SHORT}, wobbles and shifts stiffly on the spot, each beside a human handler in a plain tracksuit, spectators behind the barriers holding up phones. Setting: {LOC_ROBOT_HALF_MARATHON.LONG}, in the morning. Lighting: {LOC_ROBOT_HALF_MARATHON.LIGHT_ARCHIVE}. Mood: comic, hopeful, a little absurd. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, logos, race bibs with numbers, banners with text, recognisable landmarks, recognisable skyline, real commercial humanoid robot, sponsor branding
- **Refs:** LOC_ROBOT_HALF_MARATHON_ARCHIVE, UNIT_EARLY_HUMANOID_REF
- **Flags:** VFX-EXTEND
- **Continuity:** GRADE_ARCHIVE_2025 in post (strip grain, add video noise, soften, compression; §3.2, §13.5). Generic city, no legible bibs, banners or skyline. VFX-EXTEND: 4–6 hero robots and handlers; extend the crowd behind the barriers from a clean plate. Slits unlit.

### 01.06.002 — Main titles — Archive: one pitches flat at the gun   (4 s)
- **Shot:** Medium wide shot, long zoom lens, documentary style · **Move:** subtle handheld
- **In frame:** one early humanoid (UNIT_EARLY_HUMANOID); a handler beside it
- **Action:** At the gun one robot takes a single stiff step and pitches forward flat on its face on the asphalt.
- **Dialogue:** —
- **Sound:** the starting pistol's crack (off-screen); a clatter of plastic panels; the crowd laughs
- **PROMPT:** Medium wide shot, long zoom lens, documentary style, subtle handheld: {UNIT_EARLY_HUMANOID.LONG}, takes one stiff, flat-footed step off the start line and pitches forward flat on its face on the asphalt, its handler flinching beside it. Setting: {LOC_ROBOT_HALF_MARATHON.SHORT}, in the morning. Lighting: {LOC_ROBOT_HALF_MARATHON.LIGHT_ARCHIVE}. Mood: comic, deadpan. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, logos, race bibs with numbers, banners with text, recognisable skyline, real commercial humanoid robot, sparks, pieces flying
- **Refs:** UNIT_EARLY_HUMANOID_REF, LOC_ROBOT_HALF_MARATHON_ARCHIVE
- **Continuity:** The fall is comic (file 05 §13.5). Direction of the race: frame left → right.

### 01.06.003 — Main titles — Archive: into the barrier, handler and all   (8 s)
- **Shot:** Medium wide shot, long zoom lens, documentary style · **Move:** subtle handheld
- **In frame:** one early humanoid; its handler; a crowd barrier
- **Action:** Another robot walks stiffly into a crowd barrier and sits down hard, pulling its handler down beside it; the handler sits up laughing.
- **Dialogue:** —
- **Sound:** a barrier's metal clang; the crowd's laughter; the handler laughing
- **PROMPT:** Medium wide shot, long zoom lens, documentary style, subtle handheld: {UNIT_EARLY_HUMANOID.SHORT} walks with short, stiff, flat-footed steps straight into a white crowd barrier and sits down hard, tugging its handler in a plain tracksuit down beside it, and the handler sits up laughing. Setting: {LOC_ROBOT_HALF_MARATHON.SHORT}, in the morning. Lighting: {LOC_ROBOT_HALF_MARATHON.LIGHT_ARCHIVE}. Mood: comic, warm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, logos, race bibs with numbers, banners with text, recognisable skyline, real commercial humanoid robot, injury, distress
- **Refs:** UNIT_EARLY_HUMANOID_REF, LOC_ROBOT_HALF_MARATHON_ARCHIVE
- **Continuity:** Show the handler up again, laughing (file 05 §13.5). The last archive clip: the film look snaps back on the cut.

### 01.06.004 — Main titles — The same chassis, 2033   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** lateral tracking right
- **In frame:** SHABTI (UNIT_SHABTI)
- **Action:** The same race lane, 2033: a bone-white shabti walks with smooth, unhurried, even steps, moving like water.
- **Dialogue:** —
- **Sound:** the crowd gone quiet; one faint ceramic tick per step; the music lifts
- **PROMPT:** Medium shot, anamorphic 50mm lens, lateral tracking right at walking pace: {UNIT_SHABTI.LONG}, walks with smooth, unhurried, even steps along a race lane, no bob or sway, arms hanging relaxed, the same boulevard soft behind it. Setting: {LOC_ROBOT_HALF_MARATHON.SHORT}, in the morning. Lighting: clear bright morning daylight, {GRADE_2033_DAY.TEXT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, logos, race bibs with numbers, banners with text, recognisable skyline, running, documentary video look
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_ROBOT_HALF_MARATHON_ARCHIVE (2033 re-light)
- **Continuity:** Match the chassis silhouette to 01.06.002 (same oval head, same vertical slit, now amber and lit). Film look, full grain. Screen direction left → right as the archive race.

### 01.06.005 — Main titles — A kitchen at night: the school shirt   (5 s)
- **Shot:** Medium wide shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** SHABTI (UNIT_SHABTI); the kitchen
- **Action:** High in a tower at night, a shabti folds a child's white school shirt and lays it square on the pile.
- **Dialogue:** —
- **Sound:** fabric; the fridge hum; distant city
- **PROMPT:** Medium wide shot, anamorphic 40mm lens, locked-off: {UNIT_SHABTI.SHORT} stands at the counter folding a child's white school shirt with long slim fingers and lays it square on top of the pile. Setting: {LOC_TITLES_KITCHEN.LONG}, at night. Lighting: {LOC_TITLES_KITCHEN.LIGHT_NIGHT}. Mood: quiet domestic calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, {NEG_CHILD}, child in frame, people in frame, recognisable skyline, readable labels, logos
- **Refs:** LOC_TITLES_KITCHEN_NIGHT, UNIT_SHABTI_REF_A
- **Continuity:** No child in frame; the shirt implies one (file 03 §62; bible §3.3). The woman is off screen (frame right).

### 01.06.006 — Main titles — "Shabti?" "Here am I."   (5 s)
- **Shot:** Close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** SHABTI head (UNIT_SHABTI)
- **Action:** At a voice off frame the shabti's head lifts slightly and its amber light-slit brightens once.
- **Dialogue:** WOMAN (O.S.): "Shabti?" · SHABTI (SESHAT'S VOICE): "Here am I."
- **Sound:** the woman's voice from another room; SESHAT's voice, warm, from inside the chest
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: the smooth oval head of {UNIT_SHABTI.SHORT} lifts slightly toward a voice off frame right, and its amber light-slit brightens once, then settles. Setting: {LOC_TITLES_KITCHEN.SHORT}, at night. Lighting: {LOC_TITLES_KITCHEN.LIGHT_NIGHT}. Mood: courteous and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, {NEG_CHILD}, people in frame, readable labels
- **Refs:** UNIT_SHABTI_REF_A, LOC_TITLES_KITCHEN_NIGHT
- **Flags:** COMP
- **Comp:** slit | the single brightening: starts on "Here", peaks on "am", decays by "I" (file 05 §9.8), amber #FFA93A | the slit | timed to the line | light element
- **Continuity:** The film's first "Here am I" (CHAR_KITCHEN_WOMAN_VOICE, voice only). Head lifts about 5° (acknowledgment grammar).

### 01.06.007 — Main titles — A hospital ward: he pats its hand   (5 s)
- **Shot:** Medium shot, anamorphic 50mm · **Move:** locked-off
- **In frame:** SHABTI (UNIT_SHABTI); an elderly man in bed
- **Action:** A shabti gently turns an old man in bed with open, flat hands; he reaches up and pats the back of its hand.
- **Dialogue:** —
- **Sound:** sheets; a monitor's soft tone; the old man's grateful exhale
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.SHORT} leans over a bed and gently turns an elderly man onto his side with open, flat hands, and he reaches up and pats the back of its hand twice. Setting: {LOC_TITLES_WARD.LONG}, in the morning. Lighting: {LOC_TITLES_WARD.LIGHT_DAY}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, {NEG_GARDEN}, medical procedure, needles, blood, readable signage, readable monitor screens
- **Refs:** LOC_TITLES_WARD_DAY, UNIT_SHABTI_REF_A
- **Continuity:** Adult patient only. Monitors show abstract glow only.

### 01.06.008 — Main titles — A port at dusk: mooring lines cast off   (5 s)
- **Shot:** Wide shot, anamorphic 35mm · **Move:** slow pan left
- **In frame:** a row of SHABTI along the quay (UNIT_SHABTI); a container ship
- **Action:** All down the quay, shabti lift thick mooring lines off the bollards and cast them into the water in unison.
- **Dialogue:** —
- **Sound:** heavy rope slapping water; gulls; a ship's horn, low
- **PROMPT:** Wide shot, anamorphic 35mm lens, slow pan left: all down the quay a row of robots, each {UNIT_SHABTI.SHORT}, lift thick mooring lines off steel bollards in unison and cast them into the water, the row receding into the dusk. Setting: {LOC_TITLES_PORT.LONG}, at dusk. Lighting: {LOC_TITLES_PORT.LIGHT_DUSK}. Mood: vast, calm, perfectly synchronised. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_UNITS}, people in frame, ship names, container markings, company colours, logos, readable text
- **Refs:** LOC_TITLES_PORT_DUSK, UNIT_SHABTI_REF_A
- **Flags:** VFX-EXTEND
- **Continuity:** VFX-EXTEND: 4–6 hero units nearest camera; the receding row from the 3D asset; clean plate at the same framing; the pan logged (linear, left, ~15°).

### 01.06.009 — Main titles — ATEN-1 from orbit   (5 s)
- **Shot:** Aerial shot, anamorphic 35mm · **Move:** slow push-in
- **In frame:** the ATEN-1 campus (UNIT_ATEN1_CAMPUS)
- **Action:** From orbit: a vast circular solar field in the desert, its transmission lines radiating like a sun's rays.
- **Dialogue:** —
- **Sound:** silence; the music's low swell
- **PROMPT:** Aerial shot, anamorphic 35mm lens, slow push-in: {UNIT_ATEN1_CAMPUS.LONG}, a faint haze drifting across it and sun glints rolling over the dark rows as the camera sinks slowly from orbit, looking straight down. Setting: the flat ochre Western Desert, at midday. Lighting: clear high sunlight, {GRADE_2033_DAY.TEXT}. Mood: immense, calm, impersonal. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, map labels, borders, satellite interface graphics, text, cities
- **Refs:** UNIT_ATEN1_CAMPUS_REF_A
- **Flags:** VFX-EXTEND
- **Continuity:** Always VFX-EXTEND (file 02 §9): base plate plus CG extension; 36 radiating lines. Aerials are SESHAT's eye (allowed in 2033).

### 01.06.010 — Main titles — Muon vision: the pyramid builds from the rain   (5 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm · **Move:** locked-off
- **In frame:** the Great Pyramid at night (base plate for the 3D render)
- **Action:** A faint rain of particle tracks falls through the dark; the Great Pyramid builds out of them, transparent.
- **Dialogue:** —
- **Sound:** a fine crackle of particle hits, like rain on glass; the music thins
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: the largest of three pyramids stands as a dark silhouette against a black, star-filled sky, faint desert dust drifting low across the plateau. Setting: {LOC_GIZA_PLATEAU.SHORT}, in the dead of night. Lighting: starlight only, the stone barely separated from the sky. Mood: ancient, silent, watched. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, floodlights, city glow, light show, lasers, tourists, moon
- **Refs:** LOC_GIZA_PLATEAU (night plate, starlight), muon render (3D)
- **Flags:** COMP
- **Comp:** muon vision | 3D render (file 05 §13.8): a faint rain of particle tracks; the Great Pyramid building out of them, transparent, from the interior geometry in file 03 | full frame over the plate | full clip | 3D render in the film's grade
- **Continuity:** Not generated video: the prompt makes the background plate only. SESHAT's point of view.

### 01.06.011 — Main titles — Muon vision: "I can see inside everything now."   (5 s)
- **Shot:** Wide shot, anamorphic 24mm · **Move:** slow push-in
- **In frame:** the Grand Gallery (texture reference plate for the 3D render)
- **Action:** Passage by passage the pyramid lights: the Grand Gallery a long bright blade; the King's Chamber; the Queen's.
- **Dialogue:** SESHAT (V.O.): "I can see inside everything now."
- **Sound:** SESHAT's voice; a glassy chime as each chamber lights
- **PROMPT:** Wide shot, anamorphic 24mm lens, slow push-in: looking up an empty, steep ancient gallery, its corbelled walls stepping inward toward a narrow ceiling slot, the polished limestone catching a soft cold glow from below. Setting: {LOC_GP_GRAND_GALLERY.LONG}, in the dead of night. Lighting: a soft cold glow rising from below, the corbelled walls stepping into black. Mood: vast, precise, revealed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, torches, handheld lights, tourists, signage, readable text
- **Refs:** LOC_GP_GRAND_GALLERY (reference plate), muon render (3D)
- **Flags:** COMP
- **Comp:** muon vision | 3D render: inside the transparent pyramid, the passages light one by one: the Grand Gallery as a long bright blade, then the King's Chamber, then the Queen's (§13.8) | full frame | full clip | 3D render; the gallery plate is used only as texture and light reference
- **Continuity:** The plate is a texture/lighting reference for the render, not a live cut. "Up" the gallery is away from camera (file 03).

### 01.06.012 — Main titles — Muon vision: "Except this."   (5 s)
- **Shot:** Wide shot, anamorphic 75mm · **Move:** slow push-in
- **In frame:** the pyramid's upper faces at night (base plate); the void (COMP)
- **Action:** Above the Gallery the tracks outline a black blade they cannot fill, thirty metres at least; it will not resolve. The music drops out; only the heartbeat.
- **Dialogue:** SESHAT (V.O.): (beat) "Except this."
- **Sound:** the music cuts out; only the HEARTBEAT
- **PROMPT:** Wide shot, anamorphic 75mm lens, slow push-in: the upper stepped faces of a great dark pyramid fill the frame against black stars, the push drifting toward the centre of the dark mass. Setting: {LOC_GIZA_PLATEAU.SHORT}, in the dead of night. Lighting: starlight only, the stone barely separated from the sky. Mood: an unanswered question, held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, floodlights, city glow, light show, lasers, moon
- **Refs:** LOC_GIZA_PLATEAU (night plate, starlight), muon render (3D)
- **Flags:** COMP
- **Comp:** muon vision | 3D render: above the Grand Gallery the tracks outline a black blade at least 30 m long that never resolves (the Big Void, §13.8) | full frame | full clip | 3D render
- **Continuity:** The heartbeat carries across the cut to black and the glyph.

### 01.06.013 — Main titles — The glyph; HERE AM I   (8 s)
- **Shot:** Extreme close-up, anamorphic 100mm, near-black plate · **Move:** locked-off
- **In frame:** none (black plate)
- **Action:** On black, SESHAT's glyph blooms; the title card HERE AM I; black.
- **Dialogue:** —
- **Sound:** the heartbeat alone under the glyph; it recedes far away as the title blooms (it never stops: the heartbeat only stops at 12.7); near-silence into Seq 2
- **PROMPT:** Extreme close-up, anamorphic 100mm lens, locked-off: a matte black surface in near-total darkness, the faintest fine grain moving across it and nothing else. Setting: an empty black void, at night. Lighting: no light source in frame, true black. Mood: silence before a name. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_PLATE}, stars, sparkles, texture patterns, gradients, light leaks
- **Refs:** UNIT_GLYPH_SESHAT (COMP vector, file 02 §8.1)
- **Flags:** COMP
- **Comp:** glyph + title | 1) SESHAT's glyph (seven-pointed star under inverted horns, stroke-only, warm white #F3EEE4 on black), 24-frame draw-on (stem, star clockwise from the top, arc left to right), hold, 12-frame dissolve; 2) TITLE CARD "HERE AM I", blooming from the glyph (§13.7) | centred | glyph 0:00–0:03, title 0:03–0:07, black 0:07–0:08 | glyph vector (file 02 §8.1) + title typeface (lead's choice)
- **Continuity:** Pure black plate (grain only) to carry the comp. End of Seq 1: BLACK.

