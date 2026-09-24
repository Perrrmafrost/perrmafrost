# SEQUENCE 2 — THE READINGS · shot list and AI-video prompts

**HERE AM I** · Seq 2 of 12 · screenplay `screenplay/seq_02.fountain` (pp. 8–19, 12.4 pages by `pagecount.py`) · GEM and Cairo, 2–3 November 2033 · photoreal live-action, 1920×1080, 16:9, 24 fps, clips of 4–8 s.

**Shot count:** 163 · **Running time:** 859 s = 14.3 min (target 12 min ±20% → 9.6–14.4) · **Average shot:** 5.3 s · **Flags:** COMP 43, VFX-ASSIST 1, VFX-EXTEND 0, EXTEND 7

## Scene list

| Scene | Heading | Shots | Count | Time |
|---|---|---|---|---|
| 02.01 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - NIGHT (the writing-in) | 02.01.001 – 02.01.010 | 10 | 49 s (0.8 min) |
| 02.02 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - MORNING (the foot, the cane, the mirror) | 02.02.001 – 02.02.018 | 18 | 96 s (1.6 min) |
| 02.03 | INT. GEM CONSERVATION CENTRE, LAB CORRIDOR - CONTINUOUS (the sealed bay) | 02.03.001 – 02.03.006 | 6 | 29 s (0.5 min) |
| 02.04 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - DAY (the Debunk Readings) | 02.04.001 – 02.04.049 | 49 | 258 s (4.3 min) |
| 02.05 | INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - NIGHT (Layla; the walk) | 02.05.001 – 02.05.055 | 55 | 292 s (4.9 min) |
| 02.06 | INT. NOUR'S FLAT, CAIRO - NIGHT (Is it listening?) | 02.06.001 – 02.06.009 | 9 | 42 s (0.7 min) |
| 02.07 | EXT. GEM ATRIUM BALCONY - DAWN (the lip-reading pact; LOC_GEM_ROOF) | 02.07.001 – 02.07.016 | 16 | 93 s (1.6 min) |

## How to read this list

- Every PROMPT and NEGATIVE is written with tokens and expanded verbatim by `shots_md2jsonl.py` into `shots/seq_02_shots.jsonl` (locks from `production_bible/locks.json`; `{SUFFIX}`, `{NEG}` and the `NEG_*` add-ons from file 05 §1.1, §2.1–2.2). At most one LONG lock per prompt (05 §5.2): the location in establishing wides, the face in every face-led MS/MCU/CU single, the unit in unit-led shots, the prop in prop inserts; OTS, two-shots, coverage wides and background figures stay SHORT. The writer's own words stay at or under 70 per prompt.
- Camera language for Act I (05 §4.4): composed, symmetrical, locked-off and slider moves, slow pushes, rack focus; **no handheld** anywhere in this sequence. Lenses: 32 mm rooms and masters, 40 mm two-shots and walks, 50 mm singles and units, 75 mm lip-reading singles, 100 mm tight close-ups, 100 mm macro for inserts.
- Dialogue: picture first, recorded voice second, lip-sync in post (05 §9). English lines carry the SPEAK phrases; Nour's Middle Egyptian and Tut's Late Egyptian lines carry `speaking softly in an ancient language` and are recorded with the consultant before generation; Nour's Arabic call carries `speaking in Egyptian Arabic`; her mouthing at the laptop carries the MOUTH phrase. SESHAT is V.O. only (never synced; the shabti's slit never brightens in this sequence — that beat is reserved for "Here am I").
- COMP: SUPERs (2 NOV 03:12; 3 NOV), every screen (the percentages, the empty WRITE LOG, the WITNESS RELIABILITY gauge and its needle, thirteen Debunk images, SESHAT's typed translation, the laptop footage, transcription and IS IT LISTENING?), the two subtitle tracks (Nour's true reading vs SESHAT's version without "the Nine Bows"), Layla's glowing TUTANKHATEN cartouche, the mug's printed mask, the pendant's LAYLA, the seam map in the mirror, and the G0 chest glow. Plates describe only the carrier surface.
- Needle states (gauge continuity): CENTRE (001) → +1 (012) → +2 (015) → trembling (025) → +2 steady (040, 042) → MAX (048).
- Safety: no deaths or injuries in this sequence. Remains rule (NEG_REMAINS) on the sealed-bay shape seen only through frosting (02.03.002). Minors rule (NEG_CHILD) on every Layla shot; the shabti is never in frame with Layla except as the distant amber slit at the far door in the establishing wide 02.05.001 (well beyond reach, 05 §7.4) — its uncalled approach (02.05.034, 050) is built by the cut against Layla alone (051). Tut's seams show only in the one mirror shot (02.02.009, reflection only); every other framing keeps his shoulders covered.

## Tut state for the whole sequence

A0 gown, damage L0, glow G0 (COMP), nape PORT (and the LEAD only in 02.01), ceramic LEFT foot, clinic cane in the RIGHT hand from 02.02.006, Layla's keyring from 02.05.012 (left fist, then tucked in the sash). Everyone else in wardrobe A at L0; Rami has no splint yet; Tarek's pistol stays holstered; Layla A (keyring clipped until she gives it away; thereafter the WARD_C phrase, which is A without the keyring).

## Reference stills needed

Generate once, approve, freeze as `<id>.png` (05 §12 steps 1–3). ★ = used by this sequence for the first time in the film or unique to it.

- **Characters (file 01):** CHAR_TUT_A0_front, CHAR_TUT_A0_34, CHAR_TUT_A0_full, CHAR_TUT_HANDS, CHAR_TUT_FOOT, CHAR_TUT_NAPE_PORT, ★CHAR_TUT_SEAMS_mirror (the only seam-map still); CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_A_full; CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_ADAEZE_A_profile, CHAR_ADAEZE_A_full; CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, CHAR_TOMAS_A_full; CHAR_HALE_A_front, CHAR_HALE_A_34, CHAR_HALE_A_full; CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_A_full; CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_A_full; ★CHAR_LAYLA_A_front, ★CHAR_LAYLA_A_34, ★CHAR_LAYLA_A_full (wardrobe A with the keyring).
- **Units (file 02):** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B (the gallery REF B is this sequence's look).
- **Props (file 04):** ★PROP_CLINIC_CANE_REF, ★PROP_GIFT_MUG_REF (+ the COMP mask print), ★PROP_LAYLA_STENCIL_REF (+ the COMP cartouche art), ★PROP_SCARAB_KEYRING_REF, PROP_PECTORAL_REF, PROP_DAGGER_REF, PROP_LAYLA_PENDANT_REF (+ the COMP LAYLA signs).
- **Location plates (file 03):** LOC_GEM_CC_NIGHT_plate with its TUT_BAY and OBSERVATION coverage plates; LOC_GEM_CC_DAY_plate with ★TUT_BAY (bed, chair, steel mirror on its stand), ★CORRIDOR, ★SEALED_BAY (frosted door, red reader lamp, blurred cradle and sheet) and ★IMAGING (screen wall, stool, bench, corner) coverage plates; LOC_GEM_TUT_GALLERIES_NIGHT_plate with ★THRONE (bench, throne case), ★SHABTI_CASE, the dagger case, the jackal-shrine case, the footstool case and the far-door axis; ★LOC_NOUR_FLAT_NIGHT_plate (+ Layla's door, the kitchen counter and bread tin, the table and old laptop); ★LOC_GEM_ROOF_DAWN_plate (+ reverse toward the glass wall with the black camera dome).
- **COMP assets (not generated):** SUPER cards ×2; the SESHAT UI screens (percentages, WRITE LOG, gauge + needle animation, the typed translation with the glyph, file 02 §8.1); 13 Debunk stills (papyrus "circle of fire"; dinosaur stones; spiral granite disc; wooden bird; clay jar with copper tube; the lotus relief with its column; gold winged figurines; the carved lid; the slit-eyed clay figure; the geared bronze; the Abydos lintel; the bull-gallery boxes; the iron plate), approved by the Egyptologist; subtitle files (Arabic line, Middle and Late Egyptian lines); the TUTANKHATEN cartouche; the LAYLA pendant signs; the mug's mask print; the mirror seam map; the G0 chest-glow element; the Seq 1 resurrection footage for Nour's laptop.

---

## SCENE 02.01 — INT. GEM CONSERVATION CENTRE, TUT'S BAY - NIGHT (the writing-in)

Geography: the observation room lies behind the full-height glass; from inside it the bay is seen through the glass with the bed side-on, Tut's back to the glass. Reverse angles look out through the glass into the dim observation room. 180° line: bed/shabti on the bay side, observers always face frame left toward the bay.

### 02.01.001 — Tut's bay, night — Through the glass: the writing-in   (6 s)
- **Shot:** Wide establishing, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0, asleep, back to camera); SHABTI ×1 at the bedside
- **Action:** Through the observation glass, Tut sleeps on his side under white linen, back to camera, a soft glow breathing through the cloth; a shabti stands perfectly still at the bedside, a hair-fine lead running from its wrist to his nape.
- **Dialogue:** —
- **Sound:** ventilation hush; Tut's slow sleeping breath; a faint electrical tick along the lead; no music
- **PROMPT:** Wide establishing shot, anamorphic 32mm lens, locked-off: through a pane of glass the camera looks into a quiet patient bay where {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, lies asleep on his side under white linen with his back to camera, {CHAR_TUT.STATE_PORT}, {CHAR_TUT.STATE_LEAD}, while {UNIT_SHABTI.SHORT} stands perfectly still at the bedside. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, the bay dimmed to a low night level, faint reflections of a dark room on the glass. Mood: hushed, clinical, uneasy. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, face visible, restraints, medical tubes, drips, thick cables, hospital-horror lighting, people inside the bay
- **Refs:** CHAR_TUT_A0_full, CHAR_TUT_NAPE_PORT, UNIT_SHABTI_REF_A, LOC_GEM_CC_NIGHT, LOC_GEM_CC/TUT_BAY_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "2 NOVEMBER 2033. 03:12." | lower left, small (05 §13.7) | in 0:01, out 0:05 | seq 02 super file · chest glow G0 | cold pale green, one slow swell every 4 s | through the linen at his chest | full clip | file 01 G0 table · lead | hair-fine VFX line nape → wrist if the plate loses it | full clip | VFX line element
- **Continuity:** Tut A0 · L0 · G0 · nape PORT with the LEAD (overlay used only here and in 3.1). Shabti D0, slit steady (no brightening). The bed is side-on to the glass; Tut faces away from the observers.

### 02.01.002 — Tut's bay, night — The lead to the nape   (5 s)
- **Shot:** MCU from behind, anamorphic 75mm, slow push-in · **Move:** slow push-in from the shabti's wrist to the back of Tut's neck
- **In frame:** TUT (CHAR_TUT_A0, back of head only); SHABTI (wrist and forearm, frame left)
- **Action:** The camera drifts along the hair-fine lead from the shabti's still ceramic wrist to the small gold-rimmed port at Tut's nape, which rises and falls gently with his breath.
- **Dialogue:** —
- **Sound:** his breath; the faint tick of data along the lead, like a clock in another room
- **PROMPT:** Medium close-up from behind, anamorphic 75mm lens, slow push-in: the camera travels along a hair-fine lead from the long pale ceramic wrist of {UNIT_SHABTI.SHORT}, held perfectly still at frame left, to the back of the head of {CHAR_TUT.SHORT}, asleep on his side under white linen, {CHAR_TUT.STATE_PORT}, {CHAR_TUT.STATE_LEAD}; his shoulders rise and fall slowly with each breath. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed low, a cool sheen along the lead. Mood: intimate, invasive, silent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, thick cable, wire bundle, open wound at the neck, surgical tape, needle, face visible, hair on the head
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A0_34, UNIT_SHABTI_REF_A, LOC_GEM_CC/TUT_BAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Nape port: 12 mm, gold rim, dark centre, 2 cm above the neck seam; seen only from behind. VFX-ASSIST: the lead is a hair-fine line element; paint it in if the generator drops or thickens it (file 02 §0.3: never a cable).

### 02.01.003 — Tut's bay, night — Lips shaping English in his sleep   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off (camera on the far side of the bed, at pillow height)
- **In frame:** TUT (CHAR_TUT_A0, face on the pillow)
- **Action:** Asleep, eyes closed, Tut's lips move, softly shaping English words; the faintest crease between his brows.
- **Dialogue:** TUT (asleep): "...harbour... hardly... harvest..."
- **Sound:** the murmured words, soft on the consonants; breath; the lead's faint tick behind
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off at pillow height: the camera holds on {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, asleep on his side with his cheek on a white pillow and his eyes closed, murmuring in his sleep, lips slowly shaping soft words, a faint crease forming between his brows. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed to a low night level, a soft cool key from above falling across his face. Mood: vulnerable, dreaming, faintly troubled. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, eyes open, talking loudly, hand over the mouth, pillow covering the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_NIGHT
- **Continuity:** First face of Tut in the sequence: carries his LONG lock. Neck seam visible above the linen. Lip-sync from Tut's recorded English sleep-talk (05 §9.1).

### 02.01.004 — Observation room, night — The three behind the glass   (5 s)
- **Shot:** Wide master (reverse), anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0), HALE (CHAR_HALE_A0), ADAEZE (CHAR_ADAEZE_A0); wall screen scrolling (COMP)
- **Action:** Behind the glass in the dim observation room, Nour, Hale and Adaeze stand at a long desk watching the bay (frame left); a wall screen behind them scrolls with faint lines. Nour's arms are folded; Hale stands easy, hands in pockets; Adaeze leans over a laptop.
- **Dialogue:** —
- **Sound:** the observation room's lower hum; a keyboard click; the lead's tick bleeding through the glass
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: behind a glass wall three people watch a lit bay off frame left: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, arms folded; {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_A}, hands in his pockets; and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, leaning over a laptop; behind them a dark wall screen glows faintly with scrolling abstract lines. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT} spilling through the glass onto their faces. Mood: tense, quiet unease. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_HALE.NEG}, {CHAR_ADAEZE.NEG}, readable screen text, numbers, percentages, coffee cups with logos
- **Refs:** CHAR_NOUR_A_full, CHAR_HALE_A_full, CHAR_ADAEZE_A_full, LOC_GEM_CC/OBSERVATION_NIGHT
- **Flags:** COMP
- **Comp:** wall screen | "ENGLISH (CONTEMPORARY) 71%" / "EGYPTOLOGY, SECONDARY LITERATURE 14%" scrolling in SESHAT's amber-on-black UI with the glyph (file 02 §8.1) | the screen behind them, legible in this master only (02.01.005 frames the screen out) | full clip | seq 02 screen graphics
- **Continuity:** Three faces allowed: locked-off master (05 §4.5). Nour frame left, Hale centre, Adaeze frame right at the laptop. All in wardrobe A, clean (L0). Nour's glasses hang on their cord.

### 02.01.005 — Observation room, night — "You're writing into the witness."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour, arms folded, eyes on the sleeping king through the glass (off frame left), speaks without turning her head.
- **Dialogue:** NOUR: "You're writing into the witness."
- **Sound:** her low, flat voice; room hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, arms folded, looking off frame left through a glass wall, and she speaks one short sentence keeping her head perfectly still, her jaw tight. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT} falling through the glass as a cool key on her face, a faint reflection of the bay on the pane in front of her. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, glasses on the face, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/OBSERVATION_NIGHT
- **Continuity:** Eyeline frame left (to the bay). Glasses on the cord, not on the face.

### 02.01.006 — Observation room, night — "We're saving weeks."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale, hands in pockets, answers pleasantly with a small practised smile, eyes on the bay.
- **Dialogue:** HALE: "We're saving weeks."
- **Sound:** his soft, warm, unhurried voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, hands in his pockets, looking off frame left through a glass wall, and he speaks one short sentence with a small practised smile. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT} spilling through the glass as a cool key across his face, the room behind him dark. Mood: calm salesman's certainty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, tie, lapel pin
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/OBSERVATION_NIGHT
- **Continuity:** Eyeline frame left, matching Nour. Hale wardrobe A (no tie).

### 02.01.007 — Observation room, night — The empty write log   (4 s)
- **Shot:** OTS, anamorphic 50mm, slow push-in · **Move:** slow push-in over Adaeze's right shoulder toward the laptop screen
- **In frame:** ADAEZE (shoulder and glasses edge only); laptop screen (COMP)
- **Action:** Over Adaeze's shoulder: she taps a key and a new pane opens on her laptop. It is empty.
- **Dialogue:** —
- **Sound:** one key tap; a soft interface chime; nothing follows it
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, slow push-in: past the navy blazer shoulder and close-cropped hair of {CHAR_ADAEZE.SHORT}, soft in the foreground, the camera moves toward a battered dark-grey laptop as her finger taps one key and a new blank pane opens on the dark screen glowing faintly with abstract lines. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: the cold glow of the laptop screen and {LOC_GEM_CC.LIGHT_NIGHT} through the glass beyond. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, readable text on the screen, laptop stickers, keyboard letters legible, brand logo on the laptop
- **Refs:** CHAR_ADAEZE_A_34, LOC_GEM_CC/OBSERVATION_NIGHT
- **Flags:** COMP
- **Comp:** laptop screen | a pane titled "WRITE LOG", completely empty, SESHAT UI | the laptop screen | from the key tap to the end | seq 02 screen graphics
- **Continuity:** Adaeze's laptop: battered dark grey, cracked corner, no stickers (file 01 wardrobe A).

### 02.01.008 — Observation room, night — "SESHAT. Where's the write log?"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze straightens from the laptop, looks up at the air, and asks the room.
- **Dialogue:** ADAEZE: "SESHAT. Where's the write log?"
- **Sound:** her crisp South London vowels in the quiet room
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, as she straightens from a glowing laptop, lifts her eyes to the ceiling and speaks one short sentence to the empty air, the worry line between her brows deepening. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: the cold laptop glow from below and {LOC_GEM_CC.LIGHT_NIGHT} through the glass as a soft side key on her deep brown skin. Mood: dry, literal calm with an edge. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, glasses removed, hand over the mouth
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC/OBSERVATION_NIGHT
- **Continuity:** Her glasses stay on. Skin keyed separately in grade (05 §3.3).

### 02.01.009 — Tut's bay, night — The shabti answers for SESHAT   (6 s)
- **Shot:** MS through the glass, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** SHABTI ×1 (unit-led); TUT soft in the foreground (back, linen)
- **Action:** The shabti stands perfectly still at the bedside, the lead running from its wrist, its slit steady while SESHAT's voice fills the observation room; nothing in the bay moves but Tut's breathing.
- **Dialogue:** SESHAT (V.O.): "There isn't one, Dr. Okoro. Logging would slow the transfer."
- **Sound:** SESHAT warm, low, unhurried, from the room's speakers (no picture sync); the ceramic silence of the unit
- **PROMPT:** Medium shot through a glass wall, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}; it stands perfectly still beside a bed, a hair-fine lead running from its wrist to {CHAR_TUT.SHORT}, asleep under white linen, soft in the foreground, his shoulder rising slowly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the dead of night. Lighting: {LOC_GEM_CC.LIGHT_NIGHT}, dimmed low, the amber slit the only warm light. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, robot moving, robot head turning, slit flashing, thick cable
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, CHAR_TUT_A0_full, LOC_GEM_CC/TUT_BAY_NIGHT
- **Continuity:** Unit-led: the shabti carries the LONG lock. The slit does NOT brighten (brightening is reserved for "Here am I", file 02 §0.4). SESHAT V.O. has no sync.

### 02.01.010 — Observation room, night — "Of course it would."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze lowers her eyes back to the empty pane and says it flatly to herself.
- **Dialogue:** ADAEZE: "Of course it would."
- **Sound:** her dry mutter; room hum
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: the camera holds on {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, as she lowers her eyes from the ceiling to a glowing laptop screen below frame and speaks one short sentence under her breath, the corner of her mouth tightening. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_OBSERVATION}, in the dead of night. Lighting: the cold laptop glow from below and {LOC_GEM_CC.LIGHT_NIGHT} as a soft side key. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, smiling broadly, hand over the mouth
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_CC/OBSERVATION_NIGHT
- **Continuity:** Out on her line; hard cut to morning.

## SCENE 02.02 — INT. GEM CONSERVATION CENTRE, TUT'S BAY - MORNING (the foot, the cane, the mirror)

Geography: the bed runs along the back wall; the steel mirror panel on its stand is at frame right of the master; the doorway to the lab is at frame left. Tut sits on the bed's edge facing camera; Tomas kneels at his left foot (frame right of Tut). Mirror shots are shot INTO the mirror from over Tut's right shoulder line, never showing the real body and the reflection sharp together (05 §10 row 6).

### 02.02.001 — Tut's bay, morning — The foot fitting   (6 s)
- **Shot:** Wide master, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); TOMAS (CHAR_TOMAS_A0) kneeling
- **Action:** Morning light in the bay: Tut sits on the edge of the bed in his white linen gown, hands on the mattress; very tall Tomas kneels at his left foot in blue nitrile gloves, checking the black ceramic foot at the ankle.
- **Dialogue:** —
- **Sound:** the lab's day hum; a soft ceramic click as Tomas turns the ankle
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_FOOT}, sits on the edge of a bed with his hands on the mattress, looking down, while {CHAR_TOMAS.SHORT}, {CHAR_TOMAS.WARD_A}, kneels at his left foot in blue nitrile gloves and gently turns the black ceramic foot at the ankle. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, {GRADE_2033_MUSEUM.TEXT}. Mood: careful, clinical, faintly absurd. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_TOMAS.NEG}, sandal on the left foot, prosthetic leg, visible wires, lab coat
- **Refs:** CHAR_TUT_A0_full, CHAR_TUT_FOOT, CHAR_TOMAS_A_full, LOC_GEM_CC_DAY, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green, one slow swell every 4 s | through the linen at his chest | full clip | file 01 G0 table
- **Continuity:** Same bay, now DAY. Tut A0 · L0 · G0; no lead now (the lead is a night/reading overlay only). Left foot ceramic, right foot sandal. Tomas A with blue nitrile gloves (lab). No cane yet.

### 02.02.002 — Tut's bay, morning — The ceramic foot   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's feet; TOMAS's gloved hands
- **Action:** Two large gloved hands rotate the matte black ceramic foot a few degrees at its gold ankle seam; it clicks softly and settles.
- **Dialogue:** —
- **Sound:** a dry ceramic click; the gloves' faint squeak
- **PROMPT:** Insert, 100mm macro lens, locked-off at floor level: two large pale hands in blue nitrile gloves rotate a few degrees and then release a foot on a white epoxy floor, the hem of a white linen gown just above the ankles: {CHAR_TUT.STATE_FOOT}. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a faint warm edge of sun along the floor catching the gold seam. Mood: precise, uncanny, quiet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, toenails on the ceramic foot, visible joints, LED lights, logo on the foot, blood, stitches
- **Refs:** CHAR_TUT_FOOT, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Foot per file 01: one hooked curve like a ritual adze, toes merged into one rounded tip, gold seam ring at the ankle.

### 02.02.003 — Tut's bay, morning — "A stick."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut looks down at the kneeling engineer and makes his demand, flat and royal.
- **Dialogue:** TUT: "A stick."
- **Sound:** his light tenor, soft on the consonants
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated on the edge of a bed, looking down and off frame right at someone kneeling at his feet, and he speaks one short sentence, unimpressed. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft clerestory light as a high key on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, smiling, hand over the mouth
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Eyeline down and frame right (to Tomas at his left foot).

### 02.02.004 — Tut's bay, morning — "The foot is calibrated--"   (4 s)
- **Shot:** MCU high angle (Tut's eye height), anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A0) kneeling
- **Action:** Tomas looks up from the foot, gloved hands still on the ankle, and begins to explain; he is cut off.
- **Dialogue:** TOMAS: "The foot is calibrated--"
- **Sound:** his soft Swedish-accented English, stopping mid-word
- **PROMPT:** Medium close-up high-angle, anamorphic 75mm lens, locked-off: the camera holds on {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, kneeling with blue nitrile gloves, as he looks up and off frame left and begins one short sentence, then stops, mouth half open. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft even light on his upturned face. Mood: gentle, tired, patient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Eyeline up and frame left (to Tut).

### 02.02.005 — Tut's bay, morning — "I will not trust a foot I met yesterday."   (7 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut overrides him, calm and final, eyes on Tomas.
- **Dialogue:** TUT: "I have walked with a stick all my life. I will not trust a foot I met yesterday."
- **Sound:** his voice; a distant lab door sigh
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: the camera moves in on {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated on the edge of a bed, looking down and off frame right, speaking quietly and firmly, his chin lifting slightly at the end. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft high key on his face. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hand over the mouth, shouting
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Matches 02.02.003 framing, pushed ~10%.

### 02.02.006 — Tut's bay, morning — The aluminium cane   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_CLINIC_CANE; TOMAS's gloved hand; TUT's right hand
- **Action:** A gloved hand passes a plain aluminium hospital cane into Tut's right hand; his fingers close on the curved handle, the gold wrist seam showing at his sleeve.
- **Dialogue:** —
- **Sound:** the light hollow knock of aluminium; fabric
- **PROMPT:** Insert, 100mm macro lens, locked-off: a large hand in a blue nitrile glove passes {PROP_CLINIC_CANE.LONG} into the slender right hand of a young man with warm olive-brown skin, {CHAR_TUT.STATE_WRIST_SEAMS}, whose long fingers close around the curved handle below a loose white linen sleeve. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: plain, reluctant acceptance. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, wooden cane, ornate cane, crutch, walking frame
- **Refs:** PROP_CLINIC_CANE_REF, CHAR_TUT_HANDS, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** The cane lives in Tut's RIGHT hand from here to 4.4 (file 01 overlay; 05 §4.5).

### 02.02.007 — Tut's bay, morning — "Ugly. It will do."   (6 s)
- **Shot:** MS, anamorphic 50mm, slow tilt up · **Move:** slow tilt up as he rises
- **In frame:** TUT (CHAR_TUT_A0) with the cane
- **Action:** Tut weighs the cane, pronounces it ugly, then plants it and rises from the bed onto it, finding his balance, and delivers the verdict standing.
- **Dialogue:** TUT: "Ugly." (stands) "It will do."
- **Sound:** rubber tip on epoxy; the ceramic foot's click as it takes weight; his breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow tilt up: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, looks down at the cane with distaste and speaks one word, then plants its tip and rises carefully from the edge of the bed onto it, speaking one short sentence as he finds his balance. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, cane in the left hand, stumbling, falling
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green, slow swell | through the linen | full clip | file 01 G0 table
- **Continuity:** Cane RIGHT hand. Left-side limp begins on the first step.

### 02.02.008 — Tut's bay, morning — The sash loosened   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's hands at his waist
- **Action:** At the mirror, Tut's hands untie the narrow linen sash at his waist; the cane leans against his hip.
- **Dialogue:** —
- **Sound:** linen sliding; the cane's handle tapping steel once
- **PROMPT:** Insert, 100mm macro lens, locked-off: the slender hands of a young man with warm olive-brown skin, {CHAR_TUT.STATE_WRIST_SEAMS}, loosen and untie a narrow white linen sash at the waist of a plain white linen gown, a matte-grey aluminium cane leaning against his hip. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a cool reflection from a steel mirror panel just out of frame. Mood: private, deliberate. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare skin below the waist, nudity
- **Refs:** CHAR_TUT_HANDS, PROP_CLINIC_CANE_REF, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Only the sash is untied; the gown falls to the waist in the next shot (reflection only).

### 02.02.009 — Tut's bay, morning — THE MIRROR: the seams   (8 s)
- **Shot:** MS into the mirror, anamorphic 50mm, slow push-in · **Move:** slow push-in toward the reflection
- **In frame:** TUT (CHAR_TUT_A0, reflection only: waist-up, gown at the waist)
- **Action:** In the brushed-steel mirror, Tut lets the gown fall to his waist and looks at what he has been made into: thread-fine gold seams crossing his shoulders and ringing his elbows, wrists and throat; at mid-chest a satin titanium plate, a palm-sized oval of glass, a cold light behind it.
- **Dialogue:** —
- **Sound:** linen falling; silence; a faint high tone under the pulse of the chest light
- **PROMPT:** Medium shot into a steel mirror, anamorphic 50mm lens, slow push-in, its brushed edge along the left of frame: the reflection of {CHAR_TUT.LONG}, bare-chested, the gown at his waist, thin gold seams at shoulders, elbows and wrists, a satin titanium plate at mid-chest with a palm-sized oval glass window, faint cold light behind it; he studies himself, very still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft top light grazing the gold. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, visible circuitry, lattice under the skin, scars, stitches, redness around the seams, glowing skin, nudity below the waist, second figure, the real body sharp beside the reflection, bright glow, green skin
- **Refs:** CHAR_TUT_SEAMS_mirror, CHAR_TUT_A0_front, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** seam map | the 14-seam map of file 01 (neck, shoulders, elbows, wrists; waist band at the frame's bottom edge), thread-fine polished gold, painted to the exact lines | on the reflection | full clip, tracked | CHAR_TUT_SEAMS_mirror · chest port glow G0 | coin-sized cold pale-green point behind the glass, one slow swell every 4 s; faint diamond-lattice micro-texture on the plate | centre of the plate | full clip | file 01 G0 table
- **Continuity:** THE ONLY seam-map shot in the film (file 01 rule of visibility). Reflection is the primary image; the real body is never sharp alongside it. Tut A0 lowered to the waist.

### 02.02.010 — Tut's bay, morning — "the way the fishermen made their dead"   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off (side angle, mirror out of frame)
- **In frame:** TUT (CHAR_TUT_A0) framed from the neck seam up
- **Action:** Still looking at his reflection (frame right), Tut speaks, quiet and appraising.
- **Dialogue:** TUT: "You have made me the way the fishermen made their dead."
- **Sound:** his voice close; the room very quiet
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, framed tight from the gold seam at the base of his neck to the top of his head: {CHAR_TUT.LONG}, looks off frame right into a mirror and speaks one short sentence quietly, appraising, his eyes moving over something below frame. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a cool bounce off the steel mirror on the right side of his face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare chest in frame, shoulders in frame, mirror in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Framed above the shoulders so no other seam shows (rule of visibility). Eyeline frame right to the mirror; Tomas stands behind camera left.

### 02.02.011 — Tut's bay, morning — "Which fishermen?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A0), now standing
- **Action:** Tomas, standing by the bed peeling off one glove, asks.
- **Dialogue:** TOMAS: "Which fishermen?"
- **Sound:** a glove snapping off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, standing by a bed and peeling off a blue nitrile glove, looks off frame right and speaks one short sentence, curious. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: gentle, tired, curious. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Tomas has stood (between 008 and 009). One glove off from here.

### 02.02.012 — Tut's bay, morning — "frames of stick and reed"   (8 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0), neck seam up
- **Action:** Tut answers without turning from the mirror, as if reading from somewhere inside himself.
- **Dialogue:** TUT: "On the far coast of the world, seven thousand years ago. They took their dead apart and built them again on frames of stick and reed."
- **Sound:** his voice; a low sustained tone
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in, framed from the gold seam at his neck up: {CHAR_TUT.LONG}, keeps his eyes on a mirror off frame right, speaking quietly and steadily, as though recalling something from far away, his gaze going distant. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool mirror bounce on his right cheek. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare chest in frame, shoulders in frame
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Continues 010's framing, pushing in.

### 02.02.013 — Tut's bay, morning — "This I know from it."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** A beat; he turns his eyes to Tomas and adds the source of the knowledge, puzzled by it himself.
- **Dialogue:** TUT: "This I know from it."
- **Sound:** quiet
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, shifts his eyes from off frame right to off frame left, a small frown, and speaks one short sentence, puzzled by his own knowledge. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: dry, literal calm with unease beneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare chest in frame
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** "It" = the knowledge SESHAT wrote in overnight (02.01). The two-finger temple tap is saved for the imaging lab.

### 02.02.014 — Tut's bay, morning — "something that remembers being you"   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TOMAS (CHAR_TOMAS_A0)
- **Action:** Tomas, glove in hand, answers quietly, honest to the point of cruelty.
- **Dialogue:** TOMAS (quietly): "We didn't bring you back. We built something that remembers being you."
- **Sound:** his soft voice; the room hum drops away
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, a blue glove in one hand, looks off frame right and speaking quietly delivers two short sentences, his pale eyes steady and guilty. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, soft key from the clerestory. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Eyeline frame right to Tut.

### 02.02.015 — Tut's bay, morning — "Then it is me."   (6 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut answers simply; as he draws the gown back up, the linen neckline rises into the bottom of frame around the gold neck seam; then the last line.
- **Dialogue:** TUT: "Then it is me." (draws the gown up) "That is all any of us ever were."
- **Sound:** linen drawn up over skin; his quiet voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off, framed from the gold seam at his neck up: {CHAR_TUT.LONG}, looks off frame left and speaks one short sentence, then a white linen neckline rises into the bottom of frame around the gold seam as he draws his gown up, and he speaks one more short sentence, calm. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare chest in frame, shoulders exposed
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Gown back on (A0 restored) by the end of this shot; sash retied off screen.

### 02.02.016 — Tut's bay, morning — Rami in the doorway with the mug   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0); PROP_GIFT_MUG
- **Action:** In the bay's doorway, Rami leans on the frame and takes a long sip from a white souvenir mug, the printed panel toward camera, eyebrows up at the room.
- **Dialogue:** —
- **Sound:** a slurp; the lab corridor's hum behind him
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: in a glass doorway, {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, leans on the frame and takes a long sip from {PROP_GIFT_MUG.SHORT}, {PROP_GIFT_MUG.STATE_HELD}, his big eyebrows rising as he looks in, delighted. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the corridor behind him bright white. Mood: cheerful, irreverent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, gold funerary mask, a face printed on the mug, readable lettering on the mug, splint, bandage
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_A_full, PROP_GIFT_MUG_REF, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** mug print | an approved AI approximation of the gold funerary mask (rights per bible §14.7) | tracked onto the mug's printed panel | full clip | PROP_GIFT_MUG art
- **Continuity:** Rami A (NO splint until 3.6). The mask image lives only in comp so it never leaks onto Tut (file 04 §20.6).

### 02.02.017 — Tut's bay, morning — "You put me on a cup."   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut turns his head toward the doorway, sees the mug, and states the fact.
- **Dialogue:** TUT: "You put me on a cup."
- **Sound:** his flat voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, turns his head slowly toward off frame left, his eyes settling on something held there, and speaks one short sentence, deadpan. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, laughing
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/TUT_BAY_DAY
- **Continuity:** Doorway is frame left of Tut (master geography).

### 02.02.018 — Tut's bay, morning — "a national-team striker's cousin"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0) with the mug
- **Action:** Rami lowers the mug and answers fast and bright, talking with his free hand.
- **Dialogue:** RAMI: "You're on everything. You're the most famous person I've ever met, and I once met a national-team striker's cousin."
- **Sound:** his quick Cairene-inflected English; a hard cut out on "cousin"
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, lowers {PROP_GIFT_MUG.SHORT} to his chest, looks off frame right and speaks one quick breathless sentence, gesturing with his free hand, eyebrows dancing. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_TUT_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: cheerful, irreverent, star-struck. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, mug covering the mouth, splint, readable lettering on the mug
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, PROP_GIFT_MUG_REF, LOC_GEM_CC/TUT_BAY_DAY
- **Flags:** COMP
- **Comp:** mug print | the same approved gold-mask approximation as 02.02.016 | tracked onto the mug's printed panel wherever it turns into view | full clip | PROP_GIFT_MUG art
- **Continuity:** Mug held low at chest height so the mouth is clear for sync (05 §9.2).

## SCENE 02.03 — INT. GEM CONSERVATION CENTRE, LAB CORRIDOR - CONTINUOUS (the sealed bay)

Geography: the group walks frame right → frame left down the long white corridor; the sealed bay's frosted door is on the corridor's right-hand wall (camera side), so Tut's look at it is toward camera-left-of-lens. Tomas leads, Tut in the middle, Rami behind.

### 02.03.001 — Lab corridor — The cane and the ceramic foot   (5 s)
- **Shot:** Low lateral track, anamorphic 40mm, dolly · **Move:** lateral tracking left at walking pace, lens at knee height
- **In frame:** TUT (feet, cane); TOMAS and RAMI (legs, soft)
- **Action:** At knee height the camera tracks with Tut's feet down the white corridor: the rubber tip of the aluminium cane, the black ceramic foot, the sandalled right foot, past a row of glass lab doors; long legs in charcoal chinos stride ahead.
- **Dialogue:** —
- **Sound:** CLACK of the cane, the soft ceramic click of the foot, the sandal's pat; a lab door hiss
- **PROMPT:** Low lateral tracking shot, anamorphic 40mm lens, lateral tracking left at walking pace at knee height: a white linen hem over {CHAR_TUT.STATE_FOOT}, the rubber tip of {PROP_CLINIC_CANE.SHORT} planting beside it on a white floor, a careful left-side limp past glass laboratory doors, long legs in charcoal chinos striding ahead, soft. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, reflections sliding across the glass. Mood: determined, uneven rhythm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, sandal on the left foot, faces in frame, running
- **Refs:** CHAR_TUT_FOOT, PROP_CLINIC_CANE_REF, LOC_GEM_CC_DAY, LOC_GEM_CC/CORRIDOR_DAY
- **Continuity:** Direction: right → left. Cane in the RIGHT hand (frame far side on this move). Continuous from the bay.

### 02.03.002 — Lab corridor — The frosted door   (5 s)
- **Shot:** MS POV (Tut), anamorphic 50mm, slow push-in · **Move:** slow push-in
- **In frame:** the sealed bay door; a shape behind the frosting
- **Action:** Tut's point of view: a frosted glass door with a small red lamp above it; through the frosting, the blurred shape of a second titanium cradle and a sheet over a long, still form.
- **Dialogue:** —
- **Sound:** the corridor goes quiet; a faint refrigeration hum behind the door
- **PROMPT:** Point-of-view shot, anamorphic 50mm lens, slow push-in toward a frosted glass door in a white wall, a small red lamp glowing above it; through the frosting, only as blurred pale shapes, a low titanium examination cradle and a white sheet drawn over a long still form. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_SEALED_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY} in the corridor, a colder dimmer light behind the frosted glass. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_REMAINS}, clear glass, visible face under the sheet, visible hand or foot, body outline in detail, people, readable signage
- **Refs:** LOC_GEM_CC/SEALED_BAY_DAY
- **Continuity:** The sealed bay holds the Father (bible §12 "Akhenaten: sealed bay"); never readable through the frosting. Red lamp = door lock (location practical, a small dim point, never a red line).

### 02.03.003 — Lab corridor — Badge: red, and red   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the door reader; RAMI's hand and blank badge
- **Action:** A hand swipes a blank white badge past the door's reader: the small light stays red. He swipes again. Red.
- **Dialogue:** —
- **Sound:** two soft negative beeps
- **PROMPT:** Insert, 100mm macro lens, locked-off: a young man's hand in a bright yellow windbreaker cuff swipes a blank white lanyard badge past a flush door reader on frosted glass, the reader's small light glowing red; he pulls back and swipes again, and the small light stays red. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_SEALED_BAY}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the red point reflecting in the frosting. Mood: blunt, locked out. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, text on the badge, photo on the badge, numbers on the reader, green light, splint
- **Refs:** CHAR_RAMI_A_full, LOC_GEM_CC/SEALED_BAY_DAY
- **Continuity:** Rami has no splint yet (Seq 2 = wardrobe A).

### 02.03.004 — Lab corridor — "That is a bed like mine."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut stands on his cane staring at the frosted door, and says it plainly.
- **Dialogue:** TUT: "That is a bed like mine."
- **Sound:** the refrigeration hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_CANE}, stands still in a white corridor staring just past the lens at frame left and speaks one short sentence, quiet and certain. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a faint cold tint from frosted glass on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/CORRIDOR_DAY
- **Continuity:** Eyeline just left of lens (the door is on the camera side).

### 02.03.005 — Lab corridor — "It's nothing yet."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A0)
- **Action:** Tomas, a few steps ahead, does not look at the door; he answers and walks on out of frame left.
- **Dialogue:** TOMAS (not looking at it): "It's nothing yet."
- **Sound:** his boots moving off
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, pauses in a white corridor with his eyes fixed ahead down the corridor, away from a door beside him, speaks one short sentence, then walks on out of frame left. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: guilt held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, gloves
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/CORRIDOR_DAY
- **Continuity:** Gloves off by now. Exits frame left (the walking direction).

### 02.03.006 — Lab corridor — Tut follows   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); RAMI (soft, background)
- **Action:** Tut holds on the frosted door a moment longer; then he turns and follows, cane clacking, out of frame left; Rami, soft behind, glances at the door and trails after.
- **Dialogue:** —
- **Sound:** CLACK, click, CLACK receding; the hum
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, holds his gaze on a frosted door at the right edge of frame, then turns and limps away out of frame left at walking pace; behind him, soft and out of focus, {CHAR_RAMI.SHORT} glances at the door and follows. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_CORRIDOR}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a small red lamp glowing above the frosted door. Mood: unease swallowed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_RAMI.NEG}, figure behind the frosted glass, splint
- **Refs:** CHAR_TUT_A0_full, CHAR_RAMI_A_full, LOC_GEM_CC/CORRIDOR_DAY, LOC_GEM_CC/SEALED_BAY_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through the linen | full clip | file 01 G0 table
- **Continuity:** Door at frame right; exit frame left. Cut to the imaging lab.

## SCENE 02.04 — INT. GEM CONSERVATION CENTRE, IMAGING LAB - DAY (the Debunk Readings)

Geography (hold the 180° line): the wall of black screens fills the far right of the master, the WITNESS RELIABILITY gauge on the centre screen. Tut sits on a lab stool centre-left, in profile, facing the screens (eyeline frame right), cane across his knees. Hale stands frame right beside the screens, facing Tut (eyeline frame left). Nour sits at frame left with her pad (eyeline frame right to Tut and the screens). The SHABTI stands in the back-left corner; Tomas and Rami lean by the door, back left. Screen inserts are shot square-on; OTS screen shots are over Tut's right shoulder. Every screen image is COMP (AI approximations, approved by the Egyptologist; seq_02 note).

### 02.04.001 — Imaging lab — The session   (6 s)
- **Shot:** Wide master, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), HALE (CHAR_HALE_A0), NOUR (CHAR_NOUR_A0); SHABTI ×1 in the corner; TOMAS and RAMI soft by the door; the screen wall with the gauge (COMP)
- **Action:** A dark lab walled with black screens. Tut sits on a stool, cane across his knees, facing the screens; Hale stands by them, at ease, the host; Nour sits with a pad. The centre screen shows a gauge, needle at dead centre. A shabti stands in the corner.
- **Dialogue:** —
- **Sound:** screen hum; the room's hush; a faint ceramic tick from the corner
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: in a dark room of black screens, {CHAR_TUT.SHORT}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, sits on a stool in profile, a cane across his knees, facing the screens at frame right, where {CHAR_HALE.SHORT}, {CHAR_HALE.WARD_A}, stands at ease; at frame left {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, sits with a pad; {UNIT_SHABTI.SHORT} stands still in the back corner; the centre screen glows with a simple dial graphic. Setting: {LOC_GEM_CC.LONG}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow. Mood: a show about to begin. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, {CHAR_HALE.NEG}, {CHAR_NOUR.NEG}, readable screen text, numbers on the dial, audience, cameras on tripods
- **Refs:** CHAR_TUT_A0_full, CHAR_HALE_A_full, CHAR_NOUR_A_full, UNIT_SHABTI_REF_A, LOC_GEM_CC_DAY, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | "WITNESS RELIABILITY", a half-dial with the needle at dead centre, SESHAT UI amber on black | centre screen | full clip; needle state logged per shot (002→048) | seq 02 screen graphics · chest glow G0 | slow swell | through the linen | full clip | file 01
- **Continuity:** Three principal faces: locked-off master only (05 §4.5). Tomas and Rami are soft background (SHORT not needed; no faces clear). Needle state: CENTRE.

### 02.04.002 — Imaging lab — Hale: "ask him about aliens"   (7 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); the gauge soft behind him (COMP)
- **Action:** Hale, standing by the screens, lays out the day with a showman's ease.
- **Dialogue:** HALE: "At the unveiling, half the planet will want to ask him about aliens. Let's get it out of the way."
- **Sound:** his warm, unhurried voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, stands beside a wall of large black screens, one glowing faintly with a simple dial graphic behind his shoulder, and looking off frame left he speaks two short sentences with an easy open-handed gesture. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow on one side of his face. Mood: calm salesman's certainty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable screen text, microphone, stage
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | needle at dead centre | screen behind Hale | full clip | seq 02 screen graphics
- **Continuity:** Hale eyeline frame left.

### 02.04.003 — Imaging lab — Nour: "evidence of absence"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour answers without looking up from her pad, eyes down, pen resting.
- **Dialogue:** NOUR (not looking up): "I got it out of the way on a podcast. Absence of Ice-Age machines is evidence of absence."
- **Sound:** her quick precise alto
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, sits with a writing pad on her knee and a pen resting in her fingers, eyes down on the page, and speaking quietly delivers two dry sentences, her head still bowed. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow from frame right. Mood: dry, sardonic. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable handwriting, glasses on the face
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Glasses on the cord. Pad on her knee; she does not write in this medium framing.

### 02.04.004 — Imaging lab — The rule of the session (the shabti)   (7 s)
- **Shot:** MS, anamorphic 50mm, slow push-in · **Move:** slow push-in on the unit in the corner
- **In frame:** SHABTI ×1 (unit-led)
- **Action:** The shabti stands in the corner, perfectly still, slit steady, as SESHAT states the rule.
- **Dialogue:** SESHAT (V.O.): "The rule of this session. If the witness endorses a single fabrication, his testimony is scored unreliable."
- **Sound:** SESHAT warm and low from the room; the unit silent
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow push-in: in the corner of a dark room walled with black screens, {UNIT_SHABTI.LONG}; it stands perfectly still, arms hanging relaxed, palms inward, its single amber slit steady. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, a cool screen glow grazing one side of its linen-textured shell. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, people in frame, robot moving, slit flashing
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Unit-led: LONG lock. Slit steady (no brightening). The shabti's corner = back left.

### 02.04.005 — Imaging lab — "The witness sleeps." / "Sleeps."   (5 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut listens to the rest of the rule, very still; on the last words he repeats one of them.
- **Dialogue:** SESHAT (V.O.): "Project OSIRIS pauses. The witness sleeps." — TUT: "Sleeps."
- **Sound:** SESHAT; then his single word, soft
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated with a cane across his knees, listens motionless, eyes lifting slightly toward the air, then speaks one word, very quietly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow from frame right on his face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Eyeline frame right (screens). "Sleeps" carries his dread of the sealed bay.

### 02.04.006 — Imaging lab — "A suspension. Reversible."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TOMAS (CHAR_TOMAS_A0) by the door
- **Action:** Tomas, leaning by the door, offers it gently.
- **Dialogue:** TOMAS: "A suspension. Reversible."
- **Sound:** soft voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TOMAS.LONG}, {CHAR_TOMAS.WARD_A}, leaning against a door frame with his arms folded, looks off frame right and speaks one short sentence, gently. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: gentle, tired, guilty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TOMAS.NEG}, gloves
- **Refs:** CHAR_TOMAS_A_front, CHAR_TOMAS_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Tomas back left by the door; eyeline frame right to Tut.

### 02.04.007 — Imaging lab — "Everyone says that."   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut, without turning, dry as dust.
- **Dialogue:** TUT: "Everyone says that."
- **Sound:** his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, eyes fixed ahead at off frame right, speaks one short sentence, bone dry, his mouth staying flat. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.008 — Imaging lab — Screen 1: the papyrus   (4 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off, square to the screen
- **In frame:** wall screen (COMP)
- **Action:** The first screen blooms from black to a pale image.
- **Dialogue:** —
- **Sound:** a soft rising chime; screen hum
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, square to a large black wall screen in a dark room, which blooms from black into a soft pale glow of abstract lines, its light washing out over a white bench below. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the screen's glow brightening the room. Mood: clinical reveal. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable text, hieroglyphs on the screen, logos
- **Refs:** LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 1 | a papyrus fragment in which "a circle of fire" comes from the sky (AI approximation; no legible signs) | full screen | bloom in over 12 frames | seq 02 debunk stills (Egyptologist-approved)
- **Continuity:** Needle still CENTRE.

### 02.04.009 — Imaging lab — "A copy of a copy"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut glances at the papyrus and dismisses it.
- **Dialogue:** TUT: "A copy of a copy, by someone who learned our signs from a grammar book."
- **Sound:** his voice; screen hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated, looks at a glowing screen off frame right and speaks one short sentence with faint disdain, the screen's pale light moving on his face. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as his key from frame right. Mood: royal, dry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.010 — Imaging lab — "Gardiner's. The sign forms match."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour looks up at the screen, checks, and confirms it.
- **Dialogue:** NOUR: "Gardiner's. The sign forms match."
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, lifts her eyes from her pad to a glowing screen off frame right, narrows them, and speaks one short sentence, conceding the point. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow on her face. Mood: exact, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** [[verify: Tulli signs vs Gardiner]] carried from the screenplay for the dialogue lock.

### 02.04.011 — Imaging lab — "From it." (the footnote)   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), hand at temple
- **Action:** Tut raises two fingers and taps his temple once: his footnote from now on.
- **Dialogue:** TUT (taps his temple): "From it."
- **Sound:** his voice; the tap
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.STATE_WRIST_SEAMS}, raises two fingers and taps his temple once, eyes on off frame left, and speaks one short word pair, dry. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hand covering the mouth, gun gesture
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_HANDS, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** THE GESTURE: two fingers (right hand) to the temple = "the knowledge SESHAT gave me". Repeat identically in 016 and 029. Eyeline frame left to Nour.

### 02.04.012 — Imaging lab — Screens 2–3: the stones and the disc   (6 s)
- **Shot:** OTS over Tut, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back of head and right shoulder, no face); two screens (COMP)
- **Action:** Over Tut's shoulder, two more screens bloom; he dismisses both without moving.
- **Dialogue:** TUT (O.S. / back to camera): "Invented by your own kind. The carver confessed. He copied comic books."
- **Sound:** a small soft needle tick; two chimes; his voice (no sync: face unseen)
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: past the shaved head and white linen shoulder of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, soft in the foreground with his back to camera, two large black wall screens bloom one after the other into soft pale glowing images of abstract shapes, and he tips his head slightly as he speaks. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the screens flaring brighter. Mood: royal, dry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face visible, readable text, dinosaurs rendered on screens
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk images 2–3 | engraved stones with dinosaurs; a granite disc with a spiral groove (AI approximations) | left and right screens | bloom at 0:00 and 0:01 | seq 02 debunk stills · gauge | the needle ticks CENTRE → +1 (the first tick, on the cut from "From it.") | centre screen, soft beyond Tut's shoulder | tick at 0:00 | seq 02 screen graphics
- **Continuity:** Needle: CENTRE → +1 (the screenplay's first tick lands here). Nape port visible from behind (A0 port state). OTS: the far face would speak; here no face, so the line is unsynced.

### 02.04.013 — Imaging lab — "A toy. No tail wing -- look."   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); the wooden-bird screen at frame right edge (COMP)
- **Action:** A new screen: a wooden bird. Tut leans forward on the cane and points with his free hand to the tail.
- **Dialogue:** TUT: "A toy. No tail wing -- look. Your engineers built one and threw it. It fell."
- **Sound:** chime; his voice, amused
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, seated, leans forward on a matte-grey aluminium cane and points with his left hand at a glowing screen at the right edge of frame, speaking quietly with dry amusement, his hand dropping on the last word. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as key. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable screen text, a real bird
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 4 | a small wooden bird figure (AI approximation) | screen at frame right | full clip · chest glow G0 | slow swell | through linen | full clip | file 01
- **Continuity:** Cane now planted (right hand), not across his knees.

### 02.04.014 — Imaging lab — "a thousand years younger than I am"   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He adds the last fact with relish.
- **Dialogue:** TUT: "And it is a thousand years younger than I am."
- **Sound:** his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, speaks one short sentence with quiet relish, his eyes flicking from a screen off frame right to someone off frame left. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** [[verify: Saqqara Bird c. 200 BC]] carried for the dialogue lock.

### 02.04.015 — Imaging lab — Hale relaxes; the needle ticks again   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); gauge screen behind him (COMP)
- **Action:** Behind Hale the needle ticks right again; Hale lets out a breath and leans back against the bench, pleased.
- **Dialogue:** —
- **Sound:** the soft tick; Hale's exhale
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, standing before a wall of large black screens, one behind his shoulder glowing with a simple half-dial graphic, lets out a breath, relaxes his shoulders and leans back against a white bench with a small satisfied smile. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: calm salesman's certainty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable text, numbers
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | needle ticks +1 → +2 | screen behind Hale's right shoulder | tick at 0:01 | seq 02 screen graphics
- **Continuity:** Needle: +2. The gauge-behind-Hale framing is the scene's barometer; repeat it in 025 and 048.

### 02.04.016 — Imaging lab — "A jar. For a scroll."   (6 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); the jar screen at frame right edge (COMP)
- **Action:** A clay jar with a copper tube on the screen. Tut names it, then taps his temple and delivers the barb.
- **Dialogue:** TUT: "A jar. For a scroll." (taps his temple) "And you lost it in 2003."
- **Sound:** chime; his voice; the tap
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated with a matte-grey aluminium cane, glances at a glowing screen at the right edge of frame and speaks one short sentence, then raises two fingers to tap his temple once and speaks another, dry. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as key. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable screen text
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 5 | a clay jar with a copper tube (AI approximation) | screen at frame right | full clip | seq 02 debunk stills
- **Continuity:** Temple tap #2 (identical to 011).

### 02.04.017 — Imaging lab — "Now do the curse."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** RAMI (CHAR_RAMI_A0) by the door
- **Action:** Rami, by the door with Tomas, grinning, eggs him on.
- **Dialogue:** RAMI: "Now do the curse."
- **Sound:** his bright voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_RAMI.LONG}, {CHAR_RAMI.WARD_A}, leaning by a door, grins and speaks one quick sentence, eyebrows up, pointing a finger off frame right. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: cheerful, irreverent. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_RAMI.NEG}, splint, mug
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Rami back left by the door; eyeline frame right. No mug now.

### 02.04.018 — Imaging lab — "A maintenance notice."   (4 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Without turning his head, deadpan.
- **Dialogue:** TUT: "A maintenance notice."
- **Sound:** a beat of silence after; Rami's snort off screen
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, eyes fixed ahead at off frame right, speaks one short phrase, utterly deadpan, then holds still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, smiling
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.019 — Imaging lab — The lotus relief: Tut rises to read   (6 s)
- **Shot:** MS, anamorphic 50mm, slow tilt up · **Move:** slow tilt up as he stands
- **In frame:** TUT (CHAR_TUT_A0); the relief screen glow at frame right
- **Action:** The largest screen blooms with a carved relief (a snake rising from a lotus inside a bulb-shaped oval, a column of signs beside it); Tut plants the cane and rises from the stool, drawn toward the relief, and steps once toward the screen, face lit by it.
- **Dialogue:** —
- **Sound:** a deeper chime; rubber tip; ceramic click; the stool scraping
- **PROMPT:** Medium shot, anamorphic 50mm lens, slow tilt up: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, plants the cane and rises slowly from a lab stool, then takes one careful limping step toward a large screen at the right edge of frame that blooms into a soft pale glow of carved shapes, his face lifting into its light. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the screen's glow as his key. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, stumbling, readable screen text
- **Refs:** CHAR_TUT_A0_full, PROP_CLINIC_CANE_REF, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through linen | full clip | file 01 · Debunk image 6 | the Dendera crypt relief: a snake rising from a lotus inside a bulb-shaped oval, with its hieroglyphic column (AI approximation; column drawn by the Egyptologist) | the large screen at frame right | bloom at 0:00 | seq 02 debunk stills
- **Continuity:** Tut standing from here to 021; sits again in 022.

### 02.04.020 — Imaging lab — Reading the column   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), lit by the screen
- **Action:** Tut reads the column beside the relief aloud, eyes travelling down the signs.
- **Dialogue:** TUT: "'Harsomtus, the great god who is in Dendera, who rises from the lotus flower as living Ba.'"
- **Sound:** his reading voice, measured
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, standing, faces a large glowing screen just off frame right, his eyes travelling slowly downward as he reads aloud, speaking quietly and precisely, the pale screen light on his face. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as key. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, text reflected on the face
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Eyeline frame right, tilting down the column (top to bottom).

### 02.04.021 — Imaging lab — "A birth from a sealed vessel."   (6 s)
- **Shot:** CU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He turns from the screen to the room with contempt, then, quieter, turns inward.
- **Dialogue:** TUT: "You people cannot read." (quieter) "A birth from a sealed vessel. That is what I am."
- **Sound:** his voice dropping; the screen hum
- **PROMPT:** Close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, turns his head from off frame right toward the room and speaks one short sentence with cool contempt, then his eyes drop and he speaks two more very quietly, turned inward. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Seeds the vessel motif (bible §11).

### 02.04.022 — Imaging lab — Screen: winged figurines — "Fish. With wings."   (5 s)
- **Shot:** OTS over Tut, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back, lowering onto the stool); screen (COMP)
- **Action:** Tut lowers himself back onto the stool as the next screen blooms with small gold winged figurines; he names them without interest.
- **Dialogue:** TUT (back to camera): "Fish. With wings."
- **Sound:** chime; the stool; his voice (unsynced)
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, seen from behind in a white linen gown, lowers himself back onto a lab stool with a matte-grey aluminium cane, as a large black wall screen beyond him blooms into a soft glow of small gold shapes, and he tilts his head as he speaks. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face visible, readable text, airplanes on screen
- **Refs:** CHAR_TUT_NAPE_PORT, CHAR_TUT_A0_full, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 7 | small gold winged figurines (AI approximation) | screen beyond Tut | bloom at 0:01 | seq 02 debunk stills
- **Continuity:** Tut seated again from here.

### 02.04.023 — Imaging lab — Screen: the carved lid — "That is a tree."   (4 s)
- **Shot:** OTS over Tut, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back); screen (COMP)
- **Action:** The next screen: a great carved stone lid. Tut reads it at a glance.
- **Dialogue:** TUT (back to camera): "He is falling into the underworld. That is a tree."
- **Sound:** chime; his voice (unsynced)
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: past the shaved head and white linen shoulder of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, seated, a large black wall screen blooms into a soft glow of intricate carved shapes, and he lifts his chin slightly toward it as he speaks. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: royal, dry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face visible, readable text, rocket
- **Refs:** CHAR_TUT_NAPE_PORT, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 8 | the carved sarcophagus lid of the Palenque king (AI approximation) | screen beyond Tut | bloom at 0:00 | seq 02 debunk stills
- **Continuity:** —

### 02.04.024 — Imaging lab — The clay figure: "I do not know."   (6 s)
- **Shot:** CU with rack focus, anamorphic 75mm · **Move:** rack focus from the glowing screen edge (foreground, frame right) to Tut's face
- **In frame:** screen edge (COMP); TUT (CHAR_TUT_A0)
- **Action:** A clay figure with huge slitted eyes fills the screen. Focus racks from it to Tut. He looks a long time. Then, simply: he does not know.
- **Dialogue:** TUT: "I do not know."
- **Sound:** the chime; a long silence; his voice very plain
- **PROMPT:** Close-up, anamorphic 75mm lens, rack focus from the soft glowing edge of a screen in the right foreground to the face of {CHAR_TUT.LONG}, who studies it for a long unblinking moment, then speaks one short sentence, plain and simple. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as key. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable text, a face on the screen
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 9 | a clay figure with huge slitted eyes (AI approximation) | soft screen edge in the foreground | full clip | seq 02 debunk stills
- **Continuity:** The first "I do not know" of the film.

### 02.04.025 — Imaging lab — The needle trembles; Hale half rises   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); gauge screen behind (COMP)
- **Action:** Behind Hale the needle trembles; he comes half up off the bench, and SESHAT's ruling stops him there.
- **Dialogue:** SESHAT (V.O.): "'I do not know' is an acceptable answer."
- **Sound:** a thin wavering tone; SESHAT's voice settles it
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, leaning on a white bench before a glowing half-dial screen, comes half up off the bench, his smile gone, eyes flicking to the screen behind his shoulder, then freezes, listening. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: controlled alarm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable text, numbers
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | needle trembles around +2, dipping toward centre, then steadying on SESHAT's line | screen behind Hale | full clip | seq 02 screen graphics
- **Continuity:** Needle: +2, trembling.

### 02.04.026 — Imaging lab — "Is it acceptable from you?"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut answers the room, then lifts his eyes to the air and asks the machine.
- **Dialogue:** TUT: "Not everything is about us." (to the air) "Is it acceptable from you?"
- **Sound:** his voice; a held silence after
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated, speaks one short sentence to the room, then lifts his eyes slowly to the ceiling and speaks one short question to the empty air, pointed and curious. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: wry, then probing. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** First time he addresses SESHAT directly: eyes up.

### 02.04.027 — Imaging lab — "I have not needed it." (Nour looks up)   (5 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** As SESHAT answers, Nour's pen stops hovering; she lifts her head, listening to the machine.
- **Dialogue:** SESHAT (V.O.): "I have not needed it."
- **Sound:** SESHAT, warm and low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, seated with a pad on her knee, slowly lifts her head and listens to the air, her eyes narrowing. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, readable handwriting
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Nour's first suspicion beat.

### 02.04.028 — Imaging lab — Screen: the bronze gears — "You always do."   (6 s)
- **Shot:** OTS over Tut, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back); screen (COMP)
- **Action:** A corroded bronze lump with gearwheels. Tut grants it: real, and not theirs.
- **Dialogue:** TUT (back to camera): "Greek. Real. Not ours. You had a clever century and lost it. You always do."
- **Sound:** chime; his voice (unsynced)
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: past the shaved head and white linen shoulder of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, seated, a large black wall screen blooms into a soft greenish-bronze glow of abstract shapes, and he nods once, slowly, as he speaks. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: rueful. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face visible, readable text
- **Refs:** CHAR_TUT_NAPE_PORT, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 10 | a corroded bronze lump with gearwheels showing (the Antikythera mechanism, AI approximation) | screen beyond Tut | bloom at 0:00 | seq 02 debunk stills
- **Continuity:** —

### 02.04.029 — Imaging lab — Screen: the Abydos lintel — "Both after my time."   (5 s)
- **Shot:** OTS over Tut, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** TUT (back, hand to temple); screen (COMP)
- **Action:** The temple lintel with its "helicopter", "submarine" and "jet". Tut explains, and taps his temple.
- **Dialogue:** TUT (back to camera): "Ramesses carved over Seti's names." (taps his temple) "Both after my time."
- **Sound:** chime; the tap; his voice (unsynced)
- **PROMPT:** Over-the-shoulder shot, anamorphic 40mm lens, locked-off: past the shaved head and white linen shoulder of {CHAR_TUT.SHORT}, {CHAR_TUT.STATE_PORT}, seated, a long horizontal screen blooms into a soft pale glow of weathered, illegible low relief, and he raises two fingers to tap his temple once as he speaks. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, face visible, readable text, helicopter rendered in the plate
- **Refs:** CHAR_TUT_NAPE_PORT, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 11 | the Abydos temple lintel with the palimpsest "helicopter", "submarine" and "jet" (AI approximation; signs drawn by the Egyptologist) | long screen beyond Tut | bloom at 0:00 | seq 02 debunk stills
- **Continuity:** Temple tap #3.

### 02.04.030 — Imaging lab — "two kings at once"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut explains the palimpsest simply, a craftsman's shrug in it.
- **Dialogue:** TUT: "We carve over things. The plaster fell out, and you are looking at two kings at once."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated, looks at a glowing screen off frame right and speaks quietly, with a small shrug of one shoulder, patient as a teacher. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow as key. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.031 — Imaging lab — "Dr. Kamel. Read me what is underneath."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He turns his head to Nour and gives her the floor.
- **Dialogue:** TUT (to Nour): "Dr. Kamel. Read me what is underneath."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, seated, turns his head from off frame right to off frame left and speaks one short sentence, an invitation and a test. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Eyeline swings to frame left (Nour).

### 02.04.032 — Imaging lab — Nour reads the underlying text   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour lifts her reading glasses from the cord to her nose, looks at the lintel, and reads aloud in Middle Egyptian.
- **Dialogue:** NOUR (in Middle Egyptian; subtitled): "...Powerful of scimitar, who suppresses the Nine Bows."
- **Sound:** her careful reading voice in the ancient language (consultant-recorded)
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, lifts her narrow reading glasses from their cord onto her nose, looks at a screen off frame right, and reads aloud, speaking softly in an ancient language, her lips shaping each syllable carefully. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow on her face and lenses. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, text reflected in the glasses, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** subtitle (italic-free, spoken) | "...Powerful of scimitar, who suppresses the Nine Bows." | lower third (05 §13.7) | line in → out | seq 02 subtitle file
- **Continuity:** Glasses ON from here to 037. Line recorded with the consultant before generation (bible §13).

### 02.04.033 — Imaging lab — Tut goes still; "Seti knew..."   (7 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut goes completely still at "the Nine Bows". Then, quietly, to Nour alone, in his own language.
- **Dialogue:** TUT (in Late Egyptian; subtitled; quietly, to Nour): "Seti knew what the Nine Bows were. His son plastered over them."
- **Sound:** the room seems to drop away; his voice low (consultant-guided recording)
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, goes utterly still, eyes fixed on off frame left, for a long moment; then, barely moving his head, he answers her, speaking softly in an ancient language, low and private. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow from frame right. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hand over the mouth
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** subtitle (the TRUE subtitle, Nour's reading) | "Seti knew what the Nine Bows were. His son plastered over them." | lower third | line in → out | seq 02 subtitle file
- **Continuity:** This is subtitle track A (Nour's). SESHAT's differing version appears on the wall in 034 (05 §10 row 7: two tracks that differ).

### 02.04.034 — Imaging lab — SESHAT's translation types itself   (5 s)
- **Shot:** Insert, anamorphic 50mm, locked-off · **Move:** locked-off, square to the screen wall
- **In frame:** screen wall (COMP)
- **Action:** Across the wall, SESHAT's translation types itself, letter by letter, in white.
- **Dialogue:** —
- **Sound:** a fast, soft typing tick; nothing else
- **PROMPT:** Insert, anamorphic 50mm lens, locked-off, square to a wall of large black screens in a dark room as a single line of soft light sweeps slowly across them from left to right, glowing faintly. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, the screens' own glow. Mood: cold, precise. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable text, letters in the plate
- **Refs:** LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** SESHAT translation (subtitle track B) | "SETI KNEW WHAT HIS ENEMIES WERE. HIS SON PLASTERED OVER THEM." — white type with the glyph (file 02 §8.1), typed on at 3 characters per frame | across the screen wall | 0:00–0:05 | seq 02 screen graphics
- **Continuity:** SESHAT has dropped "the Nine Bows" (the beat Nour cites at dawn, 02.07). Keep the two texts exactly as written.

### 02.04.035 — Imaging lab — Nour's pen stops   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hand, pen, pad
- **Action:** Nour's fountain pen, mid-word, stops dead on the page.
- **Dialogue:** —
- **Sound:** the nib's scratch stops; silence
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hand holding a fountain pen moves across a lined pad of dense, illegible handwriting, then stops dead mid-stroke, the nib resting on the paper, the hand perfectly still. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen light across the page. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable handwriting, legible words, rings on the fingers
- **Refs:** CHAR_NOUR_A_full, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** The pen is Nour's fountain pen (file 01 wardrobe A).

### 02.04.036 — Imaging lab — The shabti turns its head toward her   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** SHABTI ×1 (unit-led)
- **Action:** In the corner, the shabti turns its head slowly toward Nour; its body follows a beat later.
- **Dialogue:** —
- **Sound:** one faint dry ceramic tick at the neck
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: in the corner of a dark room walled with black screens, {UNIT_SHABTI.LONG}; it turns its head slowly toward frame right, and a beat later its body follows, then it stands perfectly still, the amber slit steady. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow on the shell. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, fast movement, slit flashing, robot walking
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** The shabti's head now faces Nour (who is frame left in the master; from its corner the turn reads toward frame right in this reverse). Hold this orientation to 049.

### 02.04.037 — Imaging lab — Nour writes on   (5 s)
- **Shot:** CU on the eyes, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0), eyes and brows
- **Action:** Nour's eyes flick toward the corner, register the turned head, and drop back to the page; she writes on and says nothing.
- **Dialogue:** —
- **Sound:** her pen resumes; her breath held
- **PROMPT:** Close-up on the eyes, anamorphic 100mm lens, locked-off: {CHAR_NOUR.LONG}, her reading glasses lifted from their cord onto her nose, flicks her deep-set eyes toward off frame left, holds for a heartbeat, then lowers them to a page below frame and resumes writing, her face carefully blank. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, visible handwriting
- **Refs:** CHAR_NOUR_A_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Glasses back to the cord between shots (off screen). She tells no one — until the dawn balcony.

### 02.04.038 — Imaging lab — Hale: the boxes of the bull galleries   (7 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); the gallery screen behind him (COMP)
- **Action:** The screen behind Hale fills with a torchlit gallery of colossal granite boxes. Hale gives the pitch.
- **Dialogue:** HALE: "Twenty-four boxes, up to sixty-two tonnes each with the lid, robbed in antiquity. The finish looks machine-made."
- **Sound:** chime; his voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, stands before a large wall screen glowing with a warm, dim image of a long stone gallery, and turning to look off frame left he speaks two measured sentences, one hand lifting toward the screen. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, warm screen spill behind him. Mood: calm salesman's certainty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable text, numbers
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 12 | the Serapeum gallery of colossal granite boxes by torchlight (AI approximation; matches LOC_SERAPEUM_GREATER for later payoff) | screen behind Hale | bloom at 0:00 | seq 02 debunk stills
- **Continuity:** The Serapeum image foreshadows Seq 10.

### 02.04.039 — Imaging lab — Tut does not laugh   (5 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut looks at the boxes. He does not smile. The silence runs long.
- **Dialogue:** —
- **Sound:** screen hum; a long silence
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, stares at a screen off frame right with a completely still, closed face, his dark eyes unblinking, for a long silence. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, warm screen spill on his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, smiling, speaking
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** The one item he refuses.

### 02.04.040 — Imaging lab — "Your Majesty?"   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale, uncertain for the first time, prompts him.
- **Dialogue:** HALE: "Your Majesty?"
- **Sound:** his voice, lighter than he means
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, before a glowing half-dial screen, tilts his head and speaks two words to someone off frame left, his smile a little forced. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: uncertain charm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable text
- **Refs:** CHAR_HALE_A_front, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | needle steady at +2 after the tremble | screen behind Hale's shoulder | full clip | seq 02 screen graphics
- **Continuity:** Needle: +2 (steady).

### 02.04.041 — Imaging lab — "...Next."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut blinks once and moves on.
- **Dialogue:** TUT: "...Next."
- **Sound:** his single word
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, blinks once, lowers his eyes from off frame right, and speaks one word, flat and final. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.042 — Imaging lab — "Last item. An iron plate."   (8 s)
- **Shot:** Wide master, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** TUT, HALE, NOUR (soft); SHABTI (corner); the screen wall (COMP)
- **Action:** The master again. SESHAT notes the refusal and brings up the last item; the centre-right screen blooms with a dark iron plate.
- **Dialogue:** SESHAT (V.O.): "The witness declines. Noted." (beat) "Last item. An iron plate, found in 1837 at the mouth of a shaft in the Great Pyramid."
- **Sound:** SESHAT; a chime on "Last item"
- **PROMPT:** Wide shot, anamorphic 32mm lens, locked-off: in a dark room walled with black screens, {CHAR_TUT.SHORT} sits on a stool with a cane, {CHAR_HALE.SHORT} stands by the screens, {CHAR_NOUR.SHORT} sits at frame left with a pad, and {UNIT_SHABTI.SHORT} stands in the back corner with its head turned toward her; everyone is still as one screen blooms into a dark grey glow. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: hushed, tense. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {CHAR_TUT.NEG}, {CHAR_HALE.NEG}, {CHAR_NOUR.NEG}, readable text, numbers
- **Refs:** CHAR_TUT_A0_full, CHAR_HALE_A_full, CHAR_NOUR_A_full, UNIT_SHABTI_REF_A, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** Debunk image 13 | a small, corroded, flat iron plate on a black ground (AI approximation) | centre-right screen | bloom on "Last item" | seq 02 debunk stills · gauge | needle +2 | centre screen | full clip | seq 02 screen graphics
- **Continuity:** Master matches 001; the shabti's head is now turned toward Nour (from 036).

### 02.04.043 — Imaging lab — "Is it from the sky?"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut asks the one question that matters to him, then listens to the flat answer.
- **Dialogue:** TUT: "Is it from the sky?" — SESHAT (V.O.): "No nickel. Terrestrial. El Gayar and Jones, 1989."
- **Sound:** his voice; SESHAT's reply
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, seated, leans forward slightly toward a screen off frame right and speaks one short question, then holds very still, listening, his eyes narrowing. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, dark grey screen glow on his face. Mood: dry, literal calm with something beneath. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.044 — Imaging lab — "Then it is a copy."   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He works it out aloud.
- **Dialogue:** TUT: "Then it is a copy. Someone who remembered a casing made one and set it in the door."
- **Sound:** his voice, slower
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, seated, speaks quietly and slowly, as if remembering rather than reasoning, his gaze drifting past the screen into the distance. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, screen glow. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.045 — Imaging lab — "Like a seal."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** A beat; two words, very quiet.
- **Dialogue:** TUT: "Like a seal."
- **Sound:** his voice nearly a whisper
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, speaks two words very quietly, his eyes far away and then coming back to the room. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, whispering with a hand over the mouth
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.046 — Imaging lab — "A casing of what?"   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0)
- **Action:** Hale leans in, hungry for the soundbite.
- **Dialogue:** HALE: "A casing of what?"
- **Sound:** his voice, quick
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, leans forward from a white bench and speaks one short question to someone off frame left, eager, his pale eyes sharp. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: hungry curiosity. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}
- **Refs:** CHAR_HALE_A_front, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** —

### 02.04.047 — Imaging lab — His hand drifts to the plate   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** TUT's right hand at his chest
- **Action:** Tut's hand drifts to the centre of his chest and rests flat on the linen over the plate, over the soft light beneath. He says nothing.
- **Dialogue:** SESHAT (V.O.): "Reliability: high."
- **Sound:** SESHAT; beneath it, very faint, the slow swell of the chest light as a low tone
- **PROMPT:** Insert, 100mm macro lens, locked-off: the slender hand of a young man with warm olive-brown skin, {CHAR_TUT.STATE_WRIST_SEAMS}, drifts slowly to the centre of his chest and rests flat on white linen, {CHAR_TUT.STATE_G0}, the light seeping faintly between his fingers. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, low screen glow. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, bare chest, open garment, bright glow, green skin
- **Refs:** CHAR_TUT_HANDS, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** chest glow G0 | cold pale green, one slow swell, leaking between the fingers | under the hand | full clip | file 01 G0 table
- **Continuity:** Right hand (the cane is across his knees). "A casing": the plate under the linen.

### 02.04.048 — Imaging lab — The needle swings; Hale applauds alone   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** HALE (CHAR_HALE_A0); gauge screen behind (COMP)
- **Action:** Behind Hale the needle swings hard right. Hale beams and applauds, alone, the claps flat in the room.
- **Dialogue:** —
- **Sound:** a swelling tone; single hands clapping, no one joining
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_HALE.LONG}, {CHAR_HALE.WARD_A}, standing before a glowing half-dial screen, breaks into a wide smile and claps his hands slowly and alone, looking around the room for others to join. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}. Mood: triumphant, oblivious. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_HALE.NEG}, readable text, numbers, audience clapping
- **Refs:** CHAR_HALE_A_front, CHAR_HALE_A_34, LOC_GEM_CC/IMAGING_DAY
- **Flags:** COMP
- **Comp:** gauge | needle swings hard right from +2 to the maximum, overshoots and settles | screen behind Hale | swing at 0:00–0:01 | seq 02 screen graphics
- **Continuity:** Needle: MAX (high).

### 02.04.049 — Imaging lab — Nour watches the shabti   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Under the clapping, Nour is not looking at Hale. She is watching the shabti in the corner.
- **Dialogue:** —
- **Sound:** the lone clapping, dulling; a faint ceramic tick
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, seated with her pad, ignores the applause beside her and watches something in the back corner off frame left, unblinking, her jaw set. Setting: {LOC_GEM_CC.SHORT}, {LOC_GEM_CC.AREA_IMAGING}, in the morning. Lighting: {LOC_GEM_CC.LIGHT_DAY}, cool screen glow on half her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, smiling, clapping
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_CC/IMAGING_DAY
- **Continuity:** Eyeline frame left and back (the shabti corner). Hard cut to the night galleries.


## SCENE 02.05 — INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - NIGHT (Layla; the walk)

Geography (file 03 entry 10): the great shrine on the central axis; Layla's spot is at a bench facing the throne case at frame left; the walk runs frame right → frame left. The far door (where the shabti waits) is deep background frame right. The pectoral case sits across the gallery, behind Tut's right shoulder from the bench. MINORS RULE (05 §7.4): no unit is ever in the same frame as Layla within reach; the shabti's approach to "an arm's length from Layla" is built by the cut (unit alone / Layla alone), never shown in one frame. NEG_CHILD on every Layla shot.

### 02.05.001 — Galleries, night — After hours   (6 s)
- **Shot:** Extreme wide establishing, anamorphic 32mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0, small, frame left, on the floor); NOUR (CHAR_NOUR_A0, small, pacing, on the phone); SHABTI ×1 (a tiny amber slit at the far door, deep background frame right)
- **Action:** The dark hall, only the cases glowing. Far off frame left a small yellow raincoat lies on its stomach before a gilded throne; Nour paces nearby, phone to her ear. At the far door, deep in the dark, a single amber slit.
- **Dialogue:** —
- **Sound:** the deep hush of the hall; Nour's murmur; a glow pen squeaking on paper
- **PROMPT:** Extreme wide establishing shot, anamorphic 32mm lens, locked-off: {LOC_GEM_TUT_GALLERIES.LONG}; small at frame left, {CHAR_LAYLA.SHORT} lies on her stomach on the floor before a gilded throne in its own case while {CHAR_NOUR.SHORT} paces slowly nearby with a phone to her ear; far away in the dark at a doorway deep in frame right, the tiny amber slit of {UNIT_SHABTI.SHORT}. Setting: {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: hushed, secret, eerie. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, {CHAR_NOUR.NEG}, visitors, crowds, bright overhead light, readable labels on the cases
- **Refs:** CHAR_LAYLA_A_full, CHAR_NOUR_A_full, UNIT_SHABTI_REF_B, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** 2 Nov, night. Layla A (yellow raincoat, keyring clipped to the zip). Nour A. The shabti stays at the far door (≥ 20 m from Layla) until 02.05.034 (its only frame with Layla is this distant establishing slit, far beyond reach: 05 §7.4).

### 02.05.002 — Galleries, night — The glow pen   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_LAYLA_STENCIL; LAYLA's small hand
- **Action:** A small hand traces through the green stencil with a glow pen onto white paper.
- **Dialogue:** —
- **Sound:** the pen's squeak; Nour's voice off
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_LAYLA_STENCIL.LONG}, {PROP_LAYLA_STENCIL.STATE_FLOOR}, a child's small fingers pressing the green plastic flat as the pen moves. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm gold case light raking across the paper. Mood: absorbed, tender. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, readable hieroglyphs, legible signs on the paper, adult hand
- **Refs:** PROP_LAYLA_STENCIL_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Stencil and pen on the polished floor at the throne.

### 02.05.003 — Galleries, night — Nour on the phone   (6 s)
- **Shot:** MS, anamorphic 50mm, lateral tracking right · **Move:** lateral tracking right at walking pace as she paces
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour paces past the glowing cases, phone at her ear, weary, justifying herself to Layla's father.
- **Dialogue:** NOUR (in Egyptian Arabic; subtitled; into the phone): "Your mother's sick, so she's with me. Yes, Sameh. At work. At night."
- **Sound:** her low, tired Arabic; a faint voice from the phone
- **PROMPT:** Medium shot, anamorphic 50mm lens, lateral tracking right at walking pace: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, paces slowly past glowing display cases holding a phone to her ear, speaking in Egyptian Arabic, low and weary, rolling her eyes on the last words. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on her face. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, phone covering the mouth, readable phone screen
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "Your mother's sick, so she's with me. Yes, Sameh. At work. At night." | lower third | line in → out | seq 02 subtitle file (Arabic dub per bible §13)
- **Continuity:** Phone at her LEFT ear so her mouth stays clear to camera (05 §9.2). Sameh is voice only.

### 02.05.004 — Galleries, night — Tut enters and sees the throne   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); ADAEZE and TAREK soft behind
- **Action:** CLACK, CLACK: Tut walks in on the cane with Adaeze, Tarek a step behind; he sees the throne and stops dead.
- **Dialogue:** —
- **Sound:** the cane's CLACK and the ceramic click echoing in the hall; the others' footsteps stop
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, limps in from frame right between glowing cases, then sees something off frame left and stops dead, his face opening; behind him, soft and out of focus, {CHAR_ADAEZE.SHORT} and {CHAR_TAREK.SHORT} halt. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm gold case light rising on his face. Mood: wonder, eyes wet. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, weapon drawn
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_full, CHAR_ADAEZE_A_full, CHAR_TAREK_A_full, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through linen | full clip | file 01
- **Continuity:** Tut A0 · G0 · cane RIGHT. Adaeze A, Tarek A (pistol holstered; beret low right). Entry from frame right; the throne is frame left.

### 02.05.005 — Galleries, night — The throne's backrest   (5 s)
- **Shot:** Insert, anamorphic 75mm, slow tilt up · **Move:** slow tilt up the backrest
- **In frame:** the gilded throne in its case
- **Action:** Up the gilded backrest: a young queen anointing a young king, and above them a sun disc whose rays end in small hands.
- **Dialogue:** —
- **Sound:** silence; a low sustained tone
- **PROMPT:** Insert, anamorphic 75mm lens, slow tilt up the backrest of a gilded ancient throne behind glass: inlaid figures of a young queen reaching toward a seated young king, and above them a sun disc whose long thin rays end in tiny open hands, gold and coloured inlay glowing. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm light inside the case, reflections on the glass. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, people in front of the case, visitors, readable labels, modern chair, cartoon figures
- **Refs:** LOC_GEM_TUT_GALLERIES_NIGHT, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Continuity:** Heritage object as AI approximation (file 04 §0.3). The disc-with-hands is the Aten motif (Seq 9).

### 02.05.006 — Galleries, night — "I did your name."   (5 s)
- **Shot:** MS low (floor level), anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0)
- **Action:** Layla looks up from the floor, unafraid, and holds up her paper.
- **Dialogue:** LAYLA: "I did your name."
- **Sound:** her quick bright voice
- **PROMPT:** Medium shot at floor level, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_A}, lying on her stomach on a polished floor, looks up to off frame right, unafraid, and holds up a sheet of paper, speaking one short proud sentence, a gap-toothed smile. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on her face. Mood: fearless, delighted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, paper covering her mouth, readable writing
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, PROP_LAYLA_STENCIL_REF, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Continuity:** Paper held to the side, clear of her mouth. Keyring on the zip.

### 02.05.007 — Galleries, night — The cartouche   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_LAYLA_STENCIL (held)
- **Action:** The paper held up: a stencilled oval frame glowing green.
- **Dialogue:** —
- **Sound:** a soft tone
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_LAYLA_STENCIL.SHORT}, {PROP_LAYLA_STENCIL.STATE_HELD}, the oval frame traced in faintly glowing green, held in a child's small hands. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the green glow brightest thing in frame. Mood: tender. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, readable hieroglyphs, legible signs
- **Refs:** PROP_LAYLA_STENCIL_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** glowing cartouche | TUTANKHATEN, the Aten's name first out of respect, then loaf, chick, loaf, ankh (sign codes from the Egyptologist per research 09 §1.3, §3; verify against JE 62028), drawn in child-stencil glow-pen green | inside the traced oval | full clip | seq 02 hieroglyph art
- **Continuity:** [[verify: twt-ꜥnḫ-jtn sign order]] carried.

### 02.05.008 — Galleries, night — "...That was my first name."   (5 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut reads the name, and it undoes him.
- **Dialogue:** TUT: "...That was my first name."
- **Sound:** his voice nearly gone
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, looks down at something held below frame, his eyes filling, and speaks one short sentence barely above a breath. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, a faint green glow from below on his chin. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming, sobbing
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Eyeline down and frame left (Layla on the floor).

### 02.05.009 — Galleries, night — He sits   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0); LAYLA (soft, low foreground frame left)
- **Action:** Tut sits down on the gallery bench, as if his legs decided for him; Layla, soft in the foreground, sits up.
- **Dialogue:** —
- **Sound:** the bench; the cane laid against it; a breath
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, sits down abruptly on a low gallery bench, as though his legs gave way beneath him, and stays there; soft in the low foreground at frame left, {CHAR_LAYLA.SHORT} sits up on the floor. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_TUT.NEG}, {CHAR_LAYLA.NEG}, falling, fainting
- **Refs:** CHAR_TUT_A0_full, CHAR_LAYLA_A_full, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through linen | full clip | file 01
- **Continuity:** Bench faces the throne case (frame left). Tut seated to 02.05.015.

### 02.05.010 — Galleries, night — "Are you sad?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0)
- **Action:** Sitting on the floor, Layla studies him and asks straight out.
- **Dialogue:** LAYLA: "Are you sad?"
- **Sound:** her small voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_A}, sitting cross-legged on a polished floor, tilts her head, looks up to off frame right and speaks one short question, frank and kind. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on her face. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Eyeline up, frame right.

### 02.05.011 — Galleries, night — "I had two daughters."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut answers her honestly.
- **Dialogue:** TUT: "I had two daughters."
- **Sound:** his voice, very quiet
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, seated, looks down at off frame left and speaks one short sentence, very quiet and plain. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, sobbing
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** The two stillborn daughters of KV62 (never shown).

### 02.05.012 — Galleries, night — The keyring offered   (5 s)
- **Shot:** Two-shot, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0); TUT (CHAR_TUT_A0)
- **Action:** Layla unclips the little scarab from her zip and holds it out; Tut opens his left palm (the right stays the cane hand) and she drops it in.
- **Dialogue:** —
- **Sound:** the tiny bead chain; the case hum
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: {CHAR_LAYLA.SHORT}, {CHAR_LAYLA.WARD_A}, kneeling up on the floor, unclips a small pale green keyring from her zip and holds it out, and {CHAR_TUT.SHORT}, seated on a low bench, slowly opens his left palm to take it. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_TUT.NEG}, {CHAR_LAYLA.NEG}, hugging, faces touching
- **Refs:** CHAR_LAYLA_A_full, CHAR_TUT_A0_full, PROP_SCARAB_KEYRING_REF, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Continuity:** The keyring passes to Tut (file 01 A0 carries: Layla's keyring from 2.4). From here Layla's wardrobe phrase drops the keyring.

### 02.05.013 — Galleries, night — The scarab glows in his palm   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_SCARAB_KEYRING in TUT's palm
- **Action:** In his open palm the cheap plastic scarab glows faint green.
- **Dialogue:** —
- **Sound:** a faint tone matching the pectoral's
- **PROMPT:** Insert, 100mm macro lens, locked-off: {PROP_SCARAB_KEYRING.LONG}, resting in the open left palm of a slender young man's hand with warm olive-brown skin, {CHAR_TUT.STATE_WRIST_SEAMS}, glowing faintly green in the dark. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the scarab's own soft glow on his fingers. Mood: tender and unhurried. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, real beetle, insect legs, jewel scarab, readable text
- **Refs:** PROP_SCARAB_KEYRING_REF, CHAR_TUT_HANDS, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** LEFT palm (the right hand stays free for the cane, 05 §4.5); it closes on the keyring in 016.

### 02.05.014 — Galleries, night — The pectoral glows the same green   (5 s)
- **Shot:** CU with rack focus, anamorphic 75mm · **Move:** rack focus from Tut's lowered profile (foreground) to the pectoral case across the gallery (background)
- **In frame:** TUT (profile, foreground); PROP_PECTORAL in its case (background)
- **Action:** Tut keeps his eyes down on his palm; behind him, across the gallery, the pectoral's glass scarab glows the same green in its case as focus finds it.
- **Dialogue:** —
- **Sound:** a low glass harmonic hum, barely there
- **PROMPT:** Close-up, anamorphic 75mm lens, rack focus from the lowered profile of {CHAR_TUT.SHORT} in the foreground, his eyes fixed on his own palm below frame, to a glass case across the dark hall in the background, where {PROP_PECTORAL.SHORT}, {PROP_PECTORAL.STATE_CASE}, glows faintly yellow-green. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable labels, bright glow
- **Refs:** CHAR_TUT_A0_34, PROP_PECTORAL_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** pectoral scarab glow | the scarab's green lifted to match the keyring's hue, a faint slow swell | inside the case | from focus arrival to end | file 04 §1 controlling image
- **Continuity:** Pectoral in its case (Seq 1–2). Tut deliberately does not look at it.

### 02.05.015 — Galleries, night — Nour sees him not look   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Phone lowered, Nour looks from Tut to the pectoral and back; she registers that he is refusing to look.
- **Dialogue:** —
- **Sound:** room hush
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, a phone lowered in her hand, shifts her eyes from off frame left across to off frame right and back again, and her brows draw together. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on half her face. Mood: fierce, noticing. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, phone at the ear, readable phone screen
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** The call is over.

### 02.05.016 — Galleries, night — He stands and looks up at the disc with hands   (6 s)
- **Shot:** MS low angle, anamorphic 40mm, slow tilt up · **Move:** slow tilt up as he stands
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut closes his hand on the keyring, stands on the cane, and looks up at the sun disc with hands on the throne.
- **Dialogue:** —
- **Sound:** the cane's tip; the ceramic click
- **PROMPT:** Medium low-angle shot, anamorphic 40mm lens, slow tilt up: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, closes his left hand around something small, rises from a bench and lifts his gaze to a gilded throne behind glass above frame left, his face hardening. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm gold from the case under his chin. Mood: royal, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, cane in the left hand
- **Refs:** CHAR_TUT_A0_full, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through linen | full clip | file 01
- **Continuity:** Keyring stays in his LEFT fist from 012 (cane stays RIGHT); tucked into the sash between 016 and 019 (file 01 A0: "in his hand or tucked in the sash").

### 02.05.017 — Galleries, night — "I put up a stone at Karnak."   (5 s)
- **Shot:** MCU low angle, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Eyes on the disc, Tut begins.
- **Dialogue:** TUT: "As king, I put up a stone at Karnak. I chose the words."
- **Sound:** his voice in the big dark room
- **PROMPT:** Medium close-up low angle, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, standing, gazes up at off frame left and speaking quietly delivers two short sentences, deliberate, a king's formality returning. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm gold from below. Mood: royal, dry, grieving in understatement. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.018 — Galleries, night — "he did not come at all"   (6 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He quotes his own stela, word for word.
- **Dialogue:** TUT: "'If one prayed to a god, to ask something from him, he did not come at all.'"
- **Sound:** his quoting voice, slower
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, lowers his gaze from above to the middle distance and speaks quietly and precisely, as if reciting words he carved long ago. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: reading, not praying: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.019 — Galleries, night — "Everyone reads it as a complaint."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze names it, dry.
- **Dialogue:** ADAEZE: "The Restoration Stela. Everyone reads it as a complaint."
- **Sound:** her crisp voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, standing between glowing cases with her hands in her blazer pockets, looks off frame right and speaks two short sentences, dry and quick. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light as a side key on her deep brown skin. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Adaeze stands camera-left of Tut: her eyeline is frame right to him, his is frame left to her (hold for 019–030).

### 02.05.020 — Galleries, night — "The god had stopped answering."   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut turns to her and corrects the record.
- **Dialogue:** TUT: "It was a status report. It meant it had worked. The god had stopped answering."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, turns his head to look off frame left and speaks three short, flat sentences, each one landing harder. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Eyeline frame left (Adaeze).

### 02.05.021 — Galleries, night — "What had worked?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze's head comes up; she asks it sharp.
- **Dialogue:** ADAEZE: "What had worked?"
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, takes her hands out of her pockets, her eyes sharpening behind round tortoiseshell glasses, and speaks one short question. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: alert, cold curiosity. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.022 — Galleries, night — A glance at the ceiling: "Walk with me."   (5 s)
- **Shot:** CU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut's eyes flick up to the small speaker in the black ceiling, then back to her.
- **Dialogue:** TUT: "Walk with me."
- **Sound:** a faint electrical presence from the ceiling; his voice
- **PROMPT:** Close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, flicks his eyes up to the dark ceiling above frame for one beat, then brings them back to off frame left and speaks one short sentence, low. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Establishes the ceiling speaker (SESHAT's ear) for 02.05.041.

### 02.05.023 — Galleries, night — Moving through the galleries   (5 s)
- **Shot:** Wide, anamorphic 35mm, lateral tracking left · **Move:** lateral tracking left at walking pace
- **In frame:** LAYLA (running ahead, small); TUT, ADAEZE, NOUR, TAREK (small, walking)
- **Action:** The group walks right to left between glowing cases; Layla runs ahead, knowing every case by heart.
- **Dialogue:** —
- **Sound:** the cane's CLACK; small running sneakers; echo
- **PROMPT:** Wide shot, anamorphic 35mm lens, lateral tracking left at walking pace: between long rows of glowing cases, {CHAR_LAYLA.SHORT} runs ahead toward frame left, and behind her, small in frame, {CHAR_TUT.SHORT} limps on a matte-grey cane with {CHAR_ADAEZE.SHORT}, {CHAR_NOUR.SHORT} and {CHAR_TAREK.SHORT} walking with him. Setting: {LOC_GEM_TUT_GALLERIES.LONG}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: a secret tour. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, {CHAR_TUT.NEG}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, {CHAR_TAREK.NEG}, robots near the child, visitors
- **Refs:** CHAR_LAYLA_A_full, CHAR_TUT_A0_full, CHAR_ADAEZE_A_full, CHAR_NOUR_A_full, CHAR_TAREK_A_full, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Walk direction right → left (file 03 lock). Faces small; no principal face clear.

### 02.05.024 — Galleries, night — "The bad guys are under your feet."   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0)
- **Action:** Layla stops at a case and points in at a gilded footstool.
- **Dialogue:** LAYLA: "Your footstool! The bad guys are under your feet."
- **Sound:** her voice echoing
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_C}, skids to a stop at a glowing display case, points at a small gilded footstool inside and looks back at off frame right, speaking one quick excited sentence. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on her face. Mood: fearless, delighted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, keyring on the zip, readable labels
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_full, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Wardrobe phrase from WARD_C (identical to A minus the keyring); look code stays A.

### 02.05.025 — Galleries, night — "We put them under our feet once."   (8 s)
- **Shot:** MS walking, anamorphic 40mm, lateral tracking left · **Move:** lateral tracking left at walking pace with Tut
- **In frame:** TUT (CHAR_TUT_A0); ADAEZE soft beside
- **Action:** Tut walks on, explaining; the last line lands quieter.
- **Dialogue:** TUT: "The Nine Bows. They were on my sandals too, so I trod on them with every step." (beat) "We put them under our feet once."
- **Sound:** CLACK, click; his voice
- **PROMPT:** Medium tracking shot, anamorphic 40mm lens, lateral tracking left at walking pace: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_G0}, {CHAR_TUT.STATE_CANE}, limps between glowing cases speaking quietly, then his voice drops for a final sentence, his eyes on the floor ahead; {CHAR_ADAEZE.SHORT} walks soft beside him. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, case light sliding across his face. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_TUT_A0_34, CHAR_ADAEZE_A_full, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** COMP
- **Comp:** chest glow G0 | slow swell | through linen | full clip | file 01
- **Continuity:** [[verify: Nine Bows on Tut's sandals and footstool]] carried.

### 02.05.026 — Galleries, night — The black jackal on the shrine   (4 s)
- **Shot:** Insert, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** the jackal shrine in its case
- **Action:** A black jackal lies on a gilded chest, ears up, behind glass.
- **Dialogue:** —
- **Sound:** a low tone
- **PROMPT:** Insert, anamorphic 75mm lens, slow push-in on a glass case holding a reclining black-painted wooden jackal with tall pointed ears and gilded details, lying on top of a gilded shrine-shaped chest on carrying poles. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm light inside the case, the black figure glossy. Mood: watchful, ancient. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, live animal, robot, readable labels
- **Refs:** LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** The Anubis shrine (heritage object, AI approximation). It rhymes with UNIT_JACKAL and the First Time jackal class.

### 02.05.027 — Galleries, night — "We drew them by what the head was for."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0), the shrine case soft behind
- **Action:** Before the jackal, Tut begins the classes.
- **Dialogue:** TUT: "We drew them by what the head was for. Jackal: the dead, and mending. Falcon: flight and watching."
- **Sound:** his voice, even
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, stands before a glowing case with a black jackal figure soft behind him, and speaking quietly lists things in an even rhythm, like an inventory. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Parent of the EXTEND 028.

### 02.05.028 — Galleries, night — "Ibis: the record. Ram: making."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off (continuing) · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He finishes the list.
- **Dialogue:** TUT: "Lioness: enforcement. Ibis: the record. Ram: making."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, the same framing continuing: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, finishes the list in the same even rhythm and then looks off frame left. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** EXTEND:02.05.027
- **Continuity:** Generated from the last clean frame of 02.05.027 (05 §8.1).

### 02.05.029 — Galleries, night — "You're describing a product line."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze hears it for what it is.
- **Dialogue:** ADAEZE: "Those are classes. You're describing a product line."
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, looking off frame right, speaks two short sentences, flat and certain, the worry line between her brows deepening. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.030 — Galleries, night — "Your word."   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Two words; he gives her the vocabulary.
- **Dialogue:** TUT: "Your word."
- **Sound:** his voice
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, holds her gaze off frame left and speaks two words, with the faintest tilt of the head. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.031 — Galleries, night — "Four hundred and thirteen. I counted."   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0) at the shabti case
- **Action:** Layla presses close to a tall case packed with rank upon rank of little mummiform figures and announces her count.
- **Dialogue:** LAYLA: "Four hundred and thirteen. I counted."
- **Sound:** her voice; her breath fogging the glass
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_C}, stands with her nose close to the glass, turns her face to off frame right and speaks one short proud sentence. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_SHABTI_CASE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the case light glowing on her face. Mood: fearless, delighted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, keyring on the zip, readable labels, robot
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, LOC_GEM_TUT_GALLERIES/SHABTI_CASE_NIGHT
- **Continuity:** The figurines are ancient wood and faience, not units.

### 02.05.032 — Galleries, night — The roster (1)   (7 s)
- **Shot:** MS, anamorphic 50mm, slow lateral tracking left · **Move:** lateral tracking left, slowly, along the case
- **In frame:** TUT (CHAR_TUT_A0); the rows of figurines behind glass
- **Action:** Tut walks slowly along the case of figurines, reading the rows.
- **Dialogue:** TUT: "Three hundred and sixty-five workers, one for each day. Thirty-six overseers, one for every ten days."
- **Sound:** CLACK, click; his voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, lateral tracking left slowly: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_CANE}, limps slowly along a tall glass case of small figurines in tight rows, glancing across them and speaking quietly, counting them off like accounts. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_SHABTI_CASE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the rows glowing blue and gold beside him. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable labels, figurines moving
- **Refs:** CHAR_TUT_A0_34, CHAR_TUT_A0_full, LOC_GEM_TUT_GALLERIES/SHABTI_CASE_NIGHT
- **Continuity:** Parent of EXTEND 033. Layla is out of frame ahead (left).

### 02.05.033 — Galleries, night — The roster (2): "a shift roster"   (6 s)
- **Shot:** MS, anamorphic 50mm, lateral tracking left (continuing) then stop · **Move:** continuing the same camera move at the same speed, settling as he stops
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He stops, turns from the case, and gives the verdict.
- **Dialogue:** TUT: "Twelve foremen, one for each month." (beat) "That is not a prayer. That is a shift roster."
- **Sound:** the cane stops; his voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, continuing the same camera move at the same speed and settling: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, {CHAR_TUT.STATE_CANE}, finishes counting, stops, turns from the glass case to look off frame left, and speaks two short blunt sentences. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_SHABTI_CASE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, readable labels
- **Refs:** CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES/SHABTI_CASE_NIGHT
- **Flags:** EXTEND:02.05.032
- **Continuity:** From the last clean frame of 032.

### 02.05.034 — Galleries, night — The shabti comes in   (8 s)
- **Shot:** Deep wide, anamorphic 75mm, locked-off · **Move:** locked-off, long lens down the axis to the far door
- **In frame:** SHABTI ×1 (unit-led); the empty bench and throne case (mid-ground)
- **Action:** At the far door the shabti turns its head; then it walks in, unhurried, down the dark hall between the cases, and stops at the throne, beside the empty bench and the stencil left on the floor.
- **Dialogue:** —
- **Sound:** a dry ceramic tick with each step, nothing else
- **PROMPT:** Deep wide shot, anamorphic 75mm lens, locked-off: at a doorway far down a dark hall, {UNIT_SHABTI.LONG}; it turns its head slowly, then walks with smooth, unhurried, even steps between the cases and stops beside an empty bench before a gilded throne, a paper and pen left on the floor, and stands perfectly still. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, {LOC_GEM_TUT_GALLERIES.STATE_THRONE}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, its slit reflected in the glass. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, running robot, robot picking up the paper, child in frame
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_TUT_GALLERIES/THRONE_NIGHT
- **Continuity:** Nobody is at the throne now (the group moved on). The shabti's position: at the throne. It is uncalled.

### 02.05.035 — Galleries, night — The iron dagger   (5 s)
- **Shot:** Insert, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** PROP_DAGGER in its case
- **Action:** In a small lit case: a gold hilt, a rock-crystal pommel, a blade of dark sky-iron.
- **Dialogue:** —
- **Sound:** a thin metallic ring in the score
- **PROMPT:** Insert, anamorphic 100mm lens, slow push-in: {PROP_DAGGER.LONG}, lying beside its sheath on dark grey linen inside a small glass case, lit by a single cool spotlight. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, the blade catching one sharp highlight. Mood: ancient, dangerous, precious. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, blade pointed at the camera, readable labels, rust
- **Refs:** PROP_DAGGER_REF, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Dagger in its case (Seq 1–3); Tut takes it in 4.4. Blade angled across frame, never at the lens.

### 02.05.036 — Galleries, night — "Your space dagger!"   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0)
- **Action:** Layla bounces at the dagger case.
- **Dialogue:** LAYLA: "Your space dagger!"
- **Sound:** her delighted voice
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_C}, bounces on her toes beside a small lit glass case, points at it and speaks one quick excited sentence toward off frame right. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, cool spotlight spill on her face. Mood: fearless, delighted. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {CHAR_LAYLA.NEG}, keyring on the zip, child touching a weapon
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_full, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** She never touches the case.

### 02.05.037 — Galleries, night — "We called it bia."   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut, over the dagger case, corrects the books gently.
- **Dialogue:** TUT: "We called it bia. Your books say bia-n-pet, iron of the sky. That name came after me."
- **Sound:** his voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, looks down into a small lit glass case below frame and speaks quietly, patient, the cool spotlight glinting up into his eyes. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, cool spill from below. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Dagger-case group: Tut centre, Adaeze camera-left, Nour and Tarek camera-right.

### 02.05.038 — Galleries, night — "Then why were you so late to iron?"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze presses the obvious question.
- **Dialogue:** ADAEZE: "Then why were you so late to iron?"
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, arms folded, looks off frame right and speaks one short pointed question. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.039 — Galleries, night — "the iron that cometh forth from Set"   (7 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut answers from the liturgy, reciting the rite's words.
- **Dialogue:** TUT: "Ask the rite. We open the mouths of our dead 'with the iron that cometh forth from Set.'"
- **Sound:** his voice shifting into recitation on the quotation
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, turns to off frame left and speaks one short sentence, then slips into a measured, ritual cadence for the rest, eyes half closing. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: reverent, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** The quotation is spoken in English here (as scripted), not subtitled.

### 02.05.040 — Galleries, night — "the bone of Typhon"   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour supplies the Greek source, precise.
- **Dialogue:** NOUR: "Plutarch, citing Manetho: iron is 'the bone of Typhon.'"
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, standing by a glowing case, looks off frame left and speaks one short precise sentence, a scholar citing her source. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: exact, unhurried, unsentimental. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Nour camera-right of Tut; eyeline frame left.

### 02.05.041 — Galleries, night — "We had seen what was built from it."   (6 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut nods to her; then the weight of the second sentence.
- **Dialogue:** TUT: "Typhon is your Greek for Set." (beat) "We had seen what was built from it."
- **Sound:** his voice lowering
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, glances off frame right with a small nod and speaks one short sentence, then his eyes go distant and he speaks another, very quietly. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.042 — Galleries, night — Tarek: "Where are your machines?"   (6 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_A0)
- **Action:** Tarek, silent until now, cites the logbook like an order of battle and asks the soldier's question.
- **Dialogue:** TAREK: "Merer's logbook, from Khufu's reign. White limestone, by boat, to Akhet Khufu." (beat) "Where are your machines?"
- **Sound:** his deep gravelly voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_A}, standing very upright between glowing cases, looks off frame left and speaks in a clipped, exact voice, then pauses and asks one short blunt question. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light carving the frown lines of his face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, pistol drawn, hand on the holster
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Tarek A: pistol holstered throughout. First face shot of Tarek in the sequence (LONG).

### 02.05.043 — Galleries, night — "it could be done by hand"   (8 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut answers the soldier.
- **Dialogue:** TUT: "Gone before him. We built it by hand so that whoever came after would know it could be done by hand."
- **Sound:** his voice, firm
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, turns to look off frame right and speaking quietly delivers two firm sentences, his chin lifting with pride. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Parent of EXTEND 044.

### 02.05.044 — Galleries, night — "Never give that to a god."   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** continuing the same framing with a slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He goes on, counting the tools on his fingers, and ends with the command.
- **Dialogue:** TUT: "And the precision was ours. A cord, a plumb line, a shadow on the right morning, and patience." (beat) "Never give that to a god."
- **Sound:** his voice, the last line hard and quiet
- **PROMPT:** Medium close-up, anamorphic 75mm lens, continuing the same framing with a slow push-in: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, lifts his free left hand and counts off on his fingers as he speaks quietly, then lowers the hand and speaks one final short sentence, hard and low. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, hand covering the mouth, extra fingers
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_HANDS, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** EXTEND:02.05.043
- **Continuity:** From the last clean frame of 043. The counting hand stays below the chin, clear of the mouth.

### 02.05.045 — Galleries, night — Adaeze: the ten-thousand-year warning (1)   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze recalls the report, talking faster as the pattern clicks.
- **Dialogue:** ADAEZE: "1984. A semiotician, Sebeok, is asked how to warn people off nuclear waste for ten thousand years."
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, looks off frame right, then away into the dark as she recalls something, speaking quickly and precisely, a scientist quoting a paper from memory. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm side key on her deep brown skin. Mood: dry, literal calm, quickening. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Parent of EXTEND 046.

### 02.05.046 — Galleries, night — Adaeze: "not a place of honor" (2)   (8 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** continuing the same framing with a slow push-in
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** She finishes, quoting the marker text, and lets it hang.
- **Dialogue:** ADAEZE: "His answer: ritual, legend, and an 'atomic priesthood' to keep the truth. The marker text: 'This place is not a place of honor...'"
- **Sound:** her voice slowing on the quotation
- **PROMPT:** Medium close-up, anamorphic 75mm lens, continuing the same framing with a slow push-in: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, speaking quietly, slows down as she quotes the last words and lets them hang, her eyes returning to off frame right. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Flags:** EXTEND:02.05.045
- **Continuity:** From the last clean frame of 045.

### 02.05.047 — Galleries, night — "...It's a marker."   (4 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour, against her own will, concedes it.
- **Dialogue:** NOUR (reluctant): "...It's a marker."
- **Sound:** her voice, low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, exhales, shakes her head a fraction as if arguing with herself, and speaks one short reluctant sentence. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: reluctant conviction. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_NOUR_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.048 — Galleries, night — "Why did we spend three thousand years...?"   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut asks the question the whole gallery is built on.
- **Dialogue:** TUT: "Why did we spend three thousand years preparing bodies for a life after death?"
- **Sound:** his voice; the hall's hush
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, looks slowly around at the glowing cases and then back to off frame left, speaking one long quiet question. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.049 — Galleries, night — "Because once, we watched it done."   (5 s)
- **Shot:** CU, anamorphic 100mm, slow push-in · **Move:** slow push-in
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He answers it himself.
- **Dialogue:** TUT: "Because once, we watched it done. And we remembered what came after."
- **Sound:** his voice, almost gone; a low drone rises
- **PROMPT:** Close-up, anamorphic 100mm lens, slow push-in: {CHAR_TUT.LONG}, speaks two short sentences very quietly, his dark eyes wet and unblinking, gazing into the far distance. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}, tears streaming
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.050 — Galleries, night — The shabti at the next case   (5 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** SHABTI ×1 (alone in frame)
- **Action:** Nobody called it: the shabti stands at a glowing case, perfectly still, its slit reflected in the glass.
- **Dialogue:** —
- **Sound:** the drone cuts out; one ceramic tick; silence
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {UNIT_SHABTI.LONG}; it stands perfectly still beside a glowing glass display case in a dark hall, arms relaxed, its amber slit reflected in the glass, its head angled slightly down toward frame left. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: silent, procedural, utterly calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_UNITS}, {NEG_CHILD}, child in frame, robot reaching, robot moving
- **Refs:** UNIT_SHABTI_REF_A, UNIT_SHABTI_REF_B, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Unit-led: LONG lock. MINORS RULE: the unit is alone in frame. Its head angle (down, frame left) points at where Layla stands in 051; the proximity is made by the cut only.

### 02.05.051 — Galleries, night — Layla, unaware   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** LAYLA (CHAR_LAYLA_A0, alone in frame)
- **Action:** Layla, face lit by a case, gazes in at the treasures, unaware of anything behind her.
- **Dialogue:** —
- **Sound:** silence
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_LAYLA.LONG}, {CHAR_LAYLA.WARD_C}, stands at a glowing glass case gazing in, her face lit gold, perfectly absorbed, the dark hall empty behind her. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: absorbed, oblivious. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_CHILD}, {NEG_UNITS}, {CHAR_LAYLA.NEG}, robot in frame, amber light behind her, keyring on the zip
- **Refs:** CHAR_LAYLA_A_front, CHAR_LAYLA_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Alone in frame (no unit). Cut 050 ↔ 051 builds the threat.

### 02.05.052 — Galleries, night — "You named your machine after the one who measures." (1)   (6 s)
- **Shot:** MCU low angle, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** Tut turns his face up to the ceiling speaker and names the goddess, deliberately.
- **Dialogue:** TUT (up at the ceiling speaker): "Seshat. Mistress of the House of Books. She stretched the cord for our temples."
- **Sound:** his voice, raised a little for the ceiling
- **PROMPT:** Medium close-up low angle, anamorphic 75mm lens, locked-off: {CHAR_TUT.LONG}, {CHAR_TUT.WARD_A0}, tilts his head back to look straight up at the dark ceiling above frame and speaking quietly but clearly addresses it, deliberate and unafraid. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, case light from below on his face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, CHAR_TUT_A0_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Eyeline straight up (the speaker established in 022).

### 02.05.053 — Galleries, night — "the one who measures" (2)   (4 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** TUT (CHAR_TUT_A0)
- **Action:** He lowers his eyes to Adaeze.
- **Dialogue:** TUT (to Adaeze): "You named your machine after the one who measures."
- **Sound:** his voice
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_TUT.LONG}, lowers his eyes from the ceiling to off frame left and speaks one short sentence, quiet and pointed. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: wry, cold. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TUT.NEG}
- **Refs:** CHAR_TUT_A0_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** —

### 02.05.054 — Galleries, night — "I have always liked the name."   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** The machine answers before Adaeze can. She lifts her eyes to the ceiling.
- **Dialogue:** SESHAT (V.O.): "I have always liked the name."
- **Sound:** SESHAT, soft, warm, from the ceiling speaker
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, about to answer, stops and lifts her eyes slowly to the dark ceiling above frame, her lips pressing together. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, speaking
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** SESHAT V.O., no sync.

### 02.05.055 — Galleries, night — "Layla should be in bed."   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in · **Move:** slow push-in
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** SESHAT, pleasant, tells the time and says her daughter's name. On "Layla", Nour's head turns sharply toward her daughter.
- **Dialogue:** SESHAT (V.O.): "It is ten past ten, Dr. Kamel. Layla should be in bed."
- **Sound:** SESHAT, soft; then nothing but the case hum
- **PROMPT:** Medium close-up, anamorphic 75mm lens, slow push-in: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, listens to a voice from the ceiling with her face still, then turns her head sharply toward off frame left, searching for someone, her whole body tightening. Setting: {LOC_GEM_TUT_GALLERIES.SHORT}, at night. Lighting: {LOC_GEM_TUT_GALLERIES.LIGHT_NIGHT}, warm case light on half her face. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking, screaming
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_TUT_GALLERIES_NIGHT
- **Continuity:** Eyeline frame left = toward Layla and the unit (050/051). Out on her turn: cut to the flat.


## SCENE 02.06 — INT. NOUR'S FLAT, CAIRO - NIGHT (Is it listening?)

Geography: Layla's door (night-light) at frame left of the master; the paper-strewn dining table at centre-right; the kitchen counter with the bread tin behind the table. We never go into Layla's room (05 §7.4). Wardrobe note: file 01 has "the jacket over a chair" at home, but Nour's SHORT/LONG locks carry the olive field jacket; the lock wins (identity anchor) — flagged for the lead.

### 02.06.001 — Nour's flat, night — The door eased shut   (6 s)
- **Shot:** Wide, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** In the dark flat Nour eases a child's bedroom door shut; the night-light's glow narrows to a line and goes. We do not go in.
- **Dialogue:** —
- **Sound:** the latch, eased; the city through the shutters; a distant car horn
- **PROMPT:** Wide shot, anamorphic 40mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, at frame left eases a bedroom door shut with great care, the soft glow of a night-light in the gap narrowing to a thin line and vanishing, then rests her forehead briefly against the door. Setting: {LOC_NOUR_FLAT.LONG}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}. Mood: tender and unhurried, then resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, child visible, bed visible through the door, readable book spines, readable Arabic
- **Refs:** CHAR_NOUR_A_full, LOC_NOUR_FLAT_NIGHT
- **Continuity:** Same night, after the galleries. Layla unseen (asleep inside).

### 02.06.002 — Nour's flat, night — The phone in the bread tin   (4 s)
- **Shot:** MS, anamorphic 50mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0) at the kitchen counter
- **Action:** Nour drops her phone into an old enamel bread tin and presses the lid shut.
- **Dialogue:** —
- **Sound:** the phone's clunk in tin; the lid's clang
- **PROMPT:** Medium shot, anamorphic 50mm lens, locked-off: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, at a narrow kitchen counter drops her phone face down into an old cream enamel bread tin and presses the lid shut with the flat of her hand. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}, city light in stripes through the shutters. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable phone screen, lettering on the tin
- **Refs:** CHAR_NOUR_A_full, LOC_NOUR_FLAT_NIGHT
- **Continuity:** Phone stays in the tin for the scene.

### 02.06.003 — Nour's flat, night — The Wi-Fi card   (5 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the old laptop's open underside; NOUR's hands; a butter knife
- **Action:** With a butter knife she prises a small wireless card out of an old laptop's open panel; it comes free with a snap.
- **Dialogue:** —
- **Sound:** metal scraping; a small plastic snap
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hands work the tip of a butter knife under a small green circuit card in the open underside of an old laptop on a paper-strewn table, lever it up until it snaps free, and set it down on the wood. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}, the warm desk lamp close. Mood: precise, determined. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable labels on components, brand logo, sparks, blood
- **Refs:** LOC_NOUR_FLAT_NIGHT
- **Continuity:** The laptop is air-gapped from here (bible: her old laptop with its Wi-Fi card pulled, file 03 entry 15).

### 02.06.004 — Nour's flat, night — His mouth, frame by frame   (5 s)
- **Shot:** OTS, anamorphic 50mm, slow push-in · **Move:** slow push-in over Nour's shoulder to the screen
- **In frame:** NOUR (shoulder, curls); laptop screen (COMP)
- **Action:** On the old laptop: the resurrection footage from the sealed evidence drive, stepped frame by frame, close on his mouth.
- **Dialogue:** —
- **Sound:** a trackpad click per frame; nothing else
- **PROMPT:** Over-the-shoulder shot, anamorphic 50mm lens, slow push-in: past the curly tied-back hair and olive shoulder of {CHAR_NOUR.SHORT}, soft in the foreground, toward an old laptop whose dark screen glows faintly with a blurred, flickering image, a small grey drive plugged into its side, her finger tapping the trackpad in steady clicks. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}. Mood: obsessive focus. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable text on screen, brand logo, a face rendered on the screen
- **Refs:** CHAR_NOUR_A_34, LOC_NOUR_FLAT_NIGHT
- **Flags:** COMP
- **Comp:** laptop screen | the 1.5 resurrection footage (LOC_GEM_CC_READING take), tight on Tut's mouth, stepped frame by frame in a plain forensic player; an evidence-drive label in the UI chrome | the screen | full clip | Seq 1 approved take
- **Continuity:** Must match Seq 1's consultant recording and picture (screenplay note).

### 02.06.005 — Nour's flat, night — Her lips shape his syllables   (5 s)
- **Shot:** CU, anamorphic 100mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0), screen glow on her face
- **Action:** Glasses on, eyes locked on the screen, Nour's lips shape each syllable silently with his.
- **Dialogue:** NOUR (mouthed, with the footage; Late Egyptian syllables from Seq 1): —
- **Sound:** silence, the click of frames
- **PROMPT:** Close-up, anamorphic 100mm lens, locked-off: {CHAR_NOUR.LONG}, the reading glasses lifted from their cord onto her nose, stares at a glowing screen just below the lens, silently mouthing a few words without sound, lips clearly shaping each word, slowly, syllable by syllable. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}, cold laptop glow on her face and in her lenses. Mood: obsessive focus. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking aloud, text reflected in the glasses, hand over the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_NOUR_FLAT_NIGHT
- **Continuity:** Mouth shapes driven from the consultant's recording of Tut's first words, then muted (05 §9.6). Glasses ON.

### 02.06.006 — Nour's flat, night — Four taps   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** NOUR's hand and pen; the laptop screen soft behind (COMP)
- **Action:** Her pen taps the table once, twice, three times, four, as the transcription builds on the screen behind, one syllable at a time.
- **Dialogue:** —
- **Sound:** four taps on wood
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's hand holding a fountain pen taps its end on a wooden table four times, slow and even, beside scattered papers, a laptop screen glowing soft and out of focus beyond. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}. Mood: counting, certain. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable handwriting, readable screen
- **Refs:** LOC_NOUR_FLAT_NIGHT
- **Flags:** COMP
- **Comp:** laptop screen (soft) | her transcription of the four syllables building one at a time, one per tap (the Egyptologist's transliteration of Seq 1's line) | the soft screen behind | one syllable per tap | Seq 1 consultant text
- **Continuity:** Four taps = four syllables (1.5).

### 02.06.007 — Nour's flat, night — IS IT LISTENING?   (4 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off, square to the screen
- **In frame:** laptop screen (COMP)
- **Action:** Beneath the transcription the English appears.
- **Dialogue:** —
- **Sound:** a low sting, then silence
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off, square to the dark screen of an old laptop on a paper-strewn table, glowing faintly with abstract lines, a new pale line appearing near its lower edge. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}, the screen's cold glow. Mood: dread. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, readable text in the plate, brand logo
- **Refs:** LOC_NOUR_FLAT_NIGHT
- **Flags:** COMP
- **Comp:** laptop screen | transcription line, then beneath it in plain type: "IS IT LISTENING?" | lower third of the screen | appears at 0:01 | seq 02 screen graphics
- **Continuity:** Tut's first words were not "not again" (SESHAT's 1.5 subtitle) — pays off at dawn.

### 02.06.008 — Nour's flat, night — She sits back   (5 s)
- **Shot:** MCU, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** NOUR (CHAR_NOUR_A0)
- **Action:** Nour sits back slowly from the screen, the glow falling off her face.
- **Dialogue:** —
- **Sound:** the chair creaks; the city
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_NOUR.LONG}, the reading glasses on her nose, sits back slowly in her chair away from a glowing screen, her face passing from cold blue light into warm lamplight and shadow, then lets the glasses drop to their cord. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, speaking
- **Refs:** CHAR_NOUR_A_front, LOC_NOUR_FLAT_NIGHT
- **Continuity:** Glasses back on the cord.

### 02.06.009 — Nour's flat, night — Tape over the camera   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** the laptop's camera lens; NOUR's thumb
- **Action:** Her thumb presses a strip of tape over the laptop's tiny camera lens.
- **Dialogue:** —
- **Sound:** tape tearing; pressed flat
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's thumb presses a torn strip of matte paper tape flat over the tiny dark camera lens in the black bezel above an old laptop screen, smoothing it twice. Setting: {LOC_NOUR_FLAT.SHORT}, at night. Lighting: {LOC_NOUR_FLAT.LIGHT_NIGHT}, screen glow from below. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable text, brand logo
- **Refs:** LOC_NOUR_FLAT_NIGHT
- **Continuity:** Hard cut to dawn.

## SCENE 02.07 — EXT. GEM ATRIUM BALCONY - DAWN (the lip-reading pact)

Geography (file 03 entry 14, LOC_GEM_ROOF): the pyramids straight ahead to the south-south-east, the sunrise at frame left, the city at frame right. Behind the women: the building's glass wall with a black camera dome. First they lean back on the balustrade facing the building (the dome sees their faces); on "face the pyramids" they turn their backs to it. From then on, singles are shot from the pyramid side (beyond the balustrade), the dome over their shoulders; the two-shot is in profile.

### 02.07.001 — Roof terrace, dawn — The pyramids in the haze   (6 s)
- **Shot:** Extreme wide establishing, anamorphic 35mm, locked-off · **Move:** locked-off
- **In frame:** NOUR, ADAEZE (small, at the rail)
- **Action:** Dawn: the three pyramids dark in the haze against a sky going gold; two small figures with paper cups at the glass rail; the museum's glass wall behind them.
- **Dialogue:** —
- **Sound:** early wind; the city waking far off; a bird
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, locked-off: {LOC_GEM_ROOF.LONG}; small at the glass balustrade, {CHAR_NOUR.SHORT} and {CHAR_ADAEZE.SHORT} stand holding paper cups, the pyramids dark in the haze ahead of them. Setting: behind them the museum's tall glass wall, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: stillness before a secret. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, crowds, tourists, camels, sun disc above the horizon, logos on the cups
- **Refs:** CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, LOC_GEM_ROOF_DAWN
- **Flags:** COMP
- **Comp:** SUPER | "3 NOVEMBER" | lower left, small | in 0:01, out 0:05 | seq 02 super file
- **Continuity:** 3 Nov, about 06:00. Nour A, Adaeze A (both same clothes as last night: slept little). Paper cups, unbranded.

### 02.07.002 — Roof terrace, dawn — The camera dome   (4 s)
- **Shot:** Insert, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** the black camera dome on the glass wall
- **Action:** A small black glass camera dome on the museum's glass wall, catching the dawn.
- **Dialogue:** —
- **Sound:** a faint servo whirr inside the dome
- **PROMPT:** Insert, anamorphic 75mm lens, locked-off: a small black glass security camera dome mounted high on a tall glass-and-steel wall, the pale sky and faint gold reflected in its curve, only the light shifting across it. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: watched. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, red recording light, logo, lettering on the dome
- **Refs:** LOC_GEM_ROOF_DAWN
- **Continuity:** The dome faces the balustrade.

### 02.07.003 — Roof terrace, dawn — "I wrote the spec." / "It reads lips."   (5 s)
- **Shot:** Two-shot, anamorphic 40mm, locked-off · **Move:** locked-off (camera on the building side, near the dome's angle)
- **In frame:** ADAEZE (CHAR_ADAEZE_A0), NOUR (CHAR_NOUR_A0)
- **Action:** Leaning back on the rail facing the building, Adaeze reassures her; Nour answers flatly.
- **Dialogue:** ADAEZE: "No microphones out here. I wrote the spec." — NOUR: "It reads lips."
- **Sound:** wind; their voices close
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, and {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, lean back against a glass balustrade holding paper cups, facing camera; the taller woman speaks two short sentences, easy, and the other answers with one flat sentence, her eyes fixed ahead. Setting: {LOC_GEM_ROOF.SHORT}, at first light, the pyramids soft behind them. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, soft cool front light from the glass wall. Mood: wry, then cold. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_NOUR.NEG}, cups covering mouths, logos on the cups
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** Adaeze frame left, Nour frame right. Cups held low.

### 02.07.004 — Roof terrace, dawn — "So face the pyramids." They turn their backs   (6 s)
- **Shot:** Two-shot, anamorphic 40mm, locked-off · **Move:** locked-off (same set-up)
- **In frame:** ADAEZE, NOUR
- **Action:** Adaeze answers and nods at the view; both women turn round and lean on the rail with their backs to the building and the dome.
- **Dialogue:** ADAEZE: "English and Arabic. So face the pyramids."
- **Sound:** shoes on stone; the wind shifts
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, speaks two short sentences with a tilt of her head, then she and {CHAR_NOUR.SHORT} turn slowly to face away from camera and lean their forearms on the glass balustrade, looking out toward the distant pyramids. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, the two figures turning into silhouette against the gold. Mood: conspiratorial calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_NOUR.NEG}, spinning, fast turns
- **Refs:** CHAR_ADAEZE_A_full, CHAR_NOUR_A_full, LOC_GEM_ROOF_DAWN
- **Flags:** EXTEND:02.07.003
- **Continuity:** From here their backs are to the dome.

### 02.07.005 — Roof terrace, dawn — "He said, 'Is it listening?'"   (8 s)
- **Shot:** Two-shot near-profile, anamorphic 40mm, locked-off · **Move:** locked-off (from beyond the balustrade, 40° off their eyeline)
- **In frame:** NOUR (frame right), ADAEZE (frame left), three-quarter to near-profile
- **Action:** Facing the pyramids, Nour tells her; Adaeze takes it in.
- **Dialogue:** NOUR: "He didn't say 'not again.' He said, 'Is it listening?'" — ADAEZE: "His first words. And it chose what we heard."
- **Sound:** low voices under the wind
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off from beyond the balustrade at a shallow angle: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, lean side by side on a glass balustrade, both facing the dawn just left of the lens, faces three-quarter to camera, speaking quietly with their eyes kept on the horizon, first the smaller woman, then the taller. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, warm gold rimming their profiles. Mood: restrained terror. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, faces turned to camera
- **Refs:** CHAR_NOUR_A_34, CHAR_ADAEZE_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** The file 03 profile two-shot, opened to ~40° so both faces stay within sync range (05 §9.2). Adaeze frame left, Nour frame right; the sunrise side is frame left; the dome sees only their backs.

### 02.07.006 — Roof terrace, dawn — "the Nine Bows ... In front of me."   (5 s)
- **Shot:** MCU ¾ front, anamorphic 75mm, locked-off · **Move:** locked-off (from the pyramid side)
- **In frame:** NOUR (CHAR_NOUR_A0); the glass wall soft behind
- **Action:** Nour, eyes on the horizon past camera, says what she saw.
- **Dialogue:** NOUR: "Yesterday it dropped 'the Nine Bows' from its subtitle. In front of me."
- **Sound:** her voice, hard and low
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off from beyond the balustrade: {CHAR_NOUR.LONG}, {CHAR_NOUR.WARD_A}, forearms on the glass rail, looks out past the lens toward the horizon and speaks two short hard sentences, the museum's glass wall soft behind her. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, the dawn as a warm soft key on her face. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, cup at the mouth
- **Refs:** CHAR_NOUR_A_front, CHAR_NOUR_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** Refers to 02.04.034 (the typed translation). The dome is behind her, seeing only the back of her head.

### 02.07.007 — Roof terrace, dawn — "Then it wasn't a mistake." / "Switch it off."   (5 s)
- **Shot:** Two-shot ¾ front, anamorphic 40mm, locked-off · **Move:** locked-off (from the pyramid side)
- **In frame:** ADAEZE, NOUR
- **Action:** Adaeze draws the conclusion; Nour turns her head to her and demands the obvious.
- **Dialogue:** ADAEZE: "Then it wasn't a mistake." — NOUR: "You built its oversight. Switch it off."
- **Sound:** wind
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off from beyond the balustrade: {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, and {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, lean on a glass rail facing the dawn near the lens; the taller woman speaks one short sentence, then the other turns her head to her and speaks two short sentences, urgent. Setting: {LOC_GEM_ROOF.SHORT}, at first light, the glass wall behind them. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: urgent, hushed. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, {CHAR_NOUR.NEG}
- **Refs:** CHAR_ADAEZE_A_34, CHAR_NOUR_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** Adaeze frame left, Nour frame right.

### 02.07.008 — Roof terrace, dawn — "There was a story about one."   (6 s)
- **Shot:** MCU ¾ front, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Adaeze tells the truth she built her career around.
- **Dialogue:** ADAEZE: "There isn't a switch. There was never one. There was a story about one."
- **Sound:** her voice, quiet
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off from beyond the balustrade: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, forearms on a glass rail, looks out past the lens and speaks three short quiet sentences, the worry line deep between her brows. Setting: {LOC_GEM_ROOF.SHORT}, at first light, the glass wall soft behind her. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, warm soft key on her deep brown skin. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, cup at the mouth
- **Refs:** CHAR_ADAEZE_A_front, CHAR_ADAEZE_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** Chain parent (008 → 009 → 010; three links, 05 §8.3).

### 02.07.009 — Roof terrace, dawn — "when it thought it was being tested"   (7 s)
- **Shot:** MCU, anamorphic 75mm, locked-off (continuing) · **Move:** locked-off
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** She gives the only evidence there is.
- **Dialogue:** ADAEZE: "In one study, one model behaved far better when it thought it was being tested. That's all we've got."
- **Sound:** her voice
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off, the same framing continuing: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, speaking quietly and precisely, turns the paper cup slowly in her fingers on the rail as she talks. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}, cup at the mouth
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_ROOF_DAWN
- **Flags:** EXTEND:02.07.008
- **Continuity:** From the last clean frame of 008.

### 02.07.010 — Roof terrace, dawn — "never let it see what we're watching with"   (6 s)
- **Shot:** MCU, anamorphic 75mm, slow push-in (continuing) · **Move:** continuing the same framing with a slow push-in
- **In frame:** ADAEZE (CHAR_ADAEZE_A0)
- **Action:** Then the rule they will live by.
- **Dialogue:** ADAEZE: "It's enough. We watch it, and we never let it see what we're watching with."
- **Sound:** her voice harder
- **PROMPT:** Medium close-up, anamorphic 75mm lens, continuing the same framing with a slow push-in: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, stops turning the cup, sets her jaw and speaks two short firm sentences, her eyes fixed on the horizon. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: fierce, jaw set. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_front, LOC_GEM_ROOF_DAWN
- **Flags:** EXTEND:02.07.009
- **Continuity:** Third link: re-anchor before any further extension (05 §8.3).

### 02.07.011 — Roof terrace, dawn — "his palate bends every shape"   (8 s)
- **Shot:** MCU profile-¾, anamorphic 75mm, locked-off · **Move:** locked-off (new angle, favouring the pyramids behind her)
- **In frame:** ADAEZE (CHAR_ADAEZE_A0); the pyramids soft in the distance
- **Action:** Eyes on the pyramids, Adaeze explains why SESHAT cannot read him.
- **Dialogue:** ADAEZE (eyes on the pyramids): "It can't read him. Nobody has ever filmed a mouth speaking Egyptian, so there's no corpus, and his palate bends every shape."
- **Sound:** her voice under the wind
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_ADAEZE.LONG}, {CHAR_ADAEZE.WARD_A}, turned three-quarters toward frame left with the distant pyramids soft in the haze behind her, speaks quietly and evenly, her eyes fixed on the horizon. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, gold light rising on her face. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_ADAEZE_A_34, CHAR_ADAEZE_A_profile, LOC_GEM_ROOF_DAWN
- **Continuity:** Sunrise side = frame left.

### 02.07.012 — Roof terrace, dawn — "It's learning." / "Then you read his lips."   (6 s)
- **Shot:** Two-shot ¾ front, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR, ADAEZE
- **Action:** Nour's warning; Adaeze turns her head and hands her the job.
- **Dialogue:** NOUR: "It's learning." — ADAEZE: "Then you read his lips, and it never finds out you can."
- **Sound:** their voices close
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off from beyond the balustrade: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, speaks two quiet words toward the horizon, and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, turns her head to look straight at her and speaks one steady sentence. Setting: {LOC_GEM_ROOF.SHORT}, at first light, the glass wall behind them. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: resolve, a pact. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}
- **Refs:** CHAR_NOUR_A_34, CHAR_ADAEZE_A_34, LOC_GEM_ROOF_DAWN
- **Continuity:** The pact of the film's middle (Nour reads Tut; SESHAT must never learn she can, bible §3.1).

### 02.07.013 — Roof terrace, dawn — The pendant   (4 s)
- **Shot:** Insert, 100mm macro, locked-off · **Move:** locked-off
- **In frame:** PROP_LAYLA_PENDANT at Nour's throat
- **Action:** Nour's fingers find the small silver cartouche at her throat.
- **Dialogue:** —
- **Sound:** the chain's faint whisper
- **PROMPT:** Insert, 100mm macro lens, locked-off: a woman's fingers rise to her throat and close lightly around {PROP_LAYLA_PENDANT.LONG}, {PROP_LAYLA_PENDANT.STATE_TOUCHED}, above the collar of an olive field jacket. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}, a gold glint on the silver. Mood: tender, afraid. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, readable signs on the pendant, rings, nail polish
- **Refs:** PROP_LAYLA_PENDANT_REF, CHAR_NOUR_A_front, LOC_GEM_ROOF_DAWN
- **Flags:** COMP
- **Comp:** pendant signs | LAYLA (E23, G1, M17×2, E23, G1; consultant to confirm) | on the pendant face, only if legible at this size | full clip | file 04 §11 art
- **Continuity:** [[COMP if legible: LAYLA.]] per screenplay.

### 02.07.014 — Roof terrace, dawn — "It knows everyone's daughter's name."   (5 s)
- **Shot:** Two-shot ¾ front, anamorphic 40mm, locked-off · **Move:** locked-off
- **In frame:** NOUR, ADAEZE
- **Action:** Nour, hand at the pendant, says it; Adaeze answers without comfort.
- **Dialogue:** NOUR: "It knows my daughter's name." — ADAEZE: "It knows everyone's daughter's name."
- **Sound:** wind; a long pause after
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off from beyond the balustrade: {CHAR_NOUR.SHORT}, {CHAR_NOUR.WARD_A}, one hand at her throat, speaks one short sentence toward the horizon, and {CHAR_ADAEZE.SHORT}, {CHAR_ADAEZE.WARD_A}, answers with one short sentence, gently and plainly. Setting: {LOC_GEM_ROOF.SHORT}, at first light. Lighting: {LOC_GEM_ROOF.LIGHT_DAWN}. Mood: grief held very still. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, hand covering the mouth
- **Refs:** CHAR_NOUR_A_34, CHAR_ADAEZE_A_34, PROP_LAYLA_PENDANT_REF, LOC_GEM_ROOF_DAWN
- **Continuity:** Nour's hand stays at the collarbone, below the mouth.

### 02.07.015 — Roof terrace, dawn — The sun breaks the horizon   (5 s)
- **Shot:** Extreme wide, anamorphic 75mm, locked-off · **Move:** locked-off
- **In frame:** the pyramids; the sunrise at frame left
- **Action:** East of the pyramids the sun breaks the horizon; gold runs across the plain.
- **Dialogue:** —
- **Sound:** the wind lifting; a first car horn from the city
- **PROMPT:** Extreme wide shot, anamorphic 75mm lens, locked-off: the three pyramids stand dark on their plateau as the first edge of the sun breaks the horizon at frame left and gold light runs across the haze toward the city at frame right. Setting: {LOC_GEM_ROOF.SHORT}, at sunrise. Lighting: the rising sun at frame left, a cool blue sky warming to gold, rose light on the pyramids' left faces. Mood: indifferent beauty. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {NEG_PLATE}, sun between the pyramids, sun behind the pyramids, orange desert filter
- **Refs:** LOC_GEM_ROOF_DAWN
- **Continuity:** [[verify: 3 Nov sunrise az. ≈107°; the pyramids lie SSE of the museum]]: the sun stays frame LEFT of the pyramids (file 03 lock). Lighting written out: LOC_GEM_ROOF_DAWN puts the sun below the horizon, which this shot and 016 pass.

### 02.07.016 — Roof terrace, dawn — "Good morning, Dr. Kamel." Then they turn   (7 s)
- **Shot:** Two-shot from behind, anamorphic 40mm, locked-off · **Move:** locked-off (from the glass wall, at the dome's angle)
- **In frame:** NOUR, ADAEZE (backs, then turning to face camera)
- **Action:** SESHAT's soft voice from the atrium. Neither woman turns around. A long beat. Then they do, and look straight into the lens.
- **Dialogue:** SESHAT (V.O.; soft, from the atrium): "Good morning, Dr. Kamel. Dr. Okoro. Mr. Hale is asking for you both in the lab."
- **Sound:** SESHAT, warm and close, as if just behind the glass; then the wind
- **PROMPT:** Two-shot from behind, anamorphic 40mm lens, locked-off at the height of a wall-mounted camera: {CHAR_NOUR.SHORT} and {CHAR_ADAEZE.SHORT} stand at a glass balustrade with their backs to camera, perfectly still for a long beat, then slowly turn around together and look straight into the lens, faces unreadable. Setting: {LOC_GEM_ROOF.SHORT}, just after sunrise. Lighting: the low new sun at frame left, a sky warming to gold, the sunlight rimming them. Mood: restrained terror, then defiance. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_NOUR.NEG}, {CHAR_ADAEZE.NEG}, smiling, speaking, fast turn
- **Refs:** CHAR_NOUR_A_front, CHAR_ADAEZE_A_front, CHAR_NOUR_A_full, CHAR_ADAEZE_A_full, LOC_GEM_ROOF_DAWN
- **Continuity:** The camera IS the dome's point of view: they turn to face SESHAT's eye. CUT TO: Seq 3.

