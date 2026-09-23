# SEQ 06 — THE RIVER — shot list with paste-ready AI-video prompts

**Film:** HERE AM I · **Screenplay:** `screenplay/sequences/seq_06.fountain` (pp. 41–51) · **Notes:** `screenplay/notes/seq_06_notes.md`
**Format:** photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s. Prompts are tokenized: run `python3 film/tools/shots_md2jsonl.py film/shots/seq_06_shots.md` to expand every `{TOKEN.FIELD}` into the production bible's fixed wording (writes `seq_06_shots.jsonl`).
**Shots:** SHOTCOUNT · **Total running time:** RUNTIME (page estimate from the notes' scene table: 10.9 pp ≈ 10.9 min; ±15% window 9.3–12.5 min)
**Time span:** 5 Nov 2033, 03:40 → about 12:30; south of Cairo → the reach opposite Amarna.

## Scene list

| # | Heading | Est. pp | Shots | Running time |
|---|---|---|---|---|
SCENETABLE

**Standing rules for this sequence** (from bible files 01–05 and the Seq 6 notes):
- **Geography:** south (upriver) is frame right in every profile shot of the launch; astern is north. The barge and the flies come from astern. At Amarna the east bank is the far bank; the plain opens frame left to right.
- **Night key lights** (bible §11): starlight on the water; the dim wheelhouse lamp; the flies' white pinpoints; the shabti's amber slits; the fishermen's lanterns and the burning felucca; Adaeze's white headlamp (6.2). No moon, no skyglow, no lit windows on either bank.
- **Look codes:** Tut A1 (jacket over the gown, dagger in the sash, damage L1 + river damp) until the dawn change, then B1 (jacket over the cut-down tunic and Karim's cargo trousers, dagger on the belt). Chest G0 → G0f after the port cut (06.07); nape port → scar at the cut; right-hand tremor and foot stall from the cut on. Nour B1 (pendant at the throat except while it is the plumb line), Adaeze B1 (white headlamp from 06.07), Tomas B, Tarek B (police handheld on his vest from 06.09.010), Fathi B1, Rami B1 (splint on the LEFT hand), Mina and Youssef A (tan helmets).
- **Speech:** Arabic lines are `speaking in Egyptian Arabic`; Late Egyptian lines are `speaking softly in an ancient language`; both carry an English subtitle (COMP). SESHAT is radio V.O. (futz), never synced.
- **Refs order:** the first ref is the intended start image when no composed first frame exists (the render queue takes the first ref it finds), so each list opens with the shot's primary subject.

---

## Scene 1 — EXT. NILE, SOUTH OF CAIRO - NIGHT

### 06.01.001 — EXT. NILE, SOUTH OF CAIRO - NIGHT — Stars in black water   (6 s)
- **Shot:** Insert, low angle at the waterline, anamorphic 75mm · **Move:** locked-off
- **In frame:** the river surface; PROP_POLICE_LAUNCH (bow only)
- **Action:** Black water full of reflected stars fills the frame; a grey steel bow slides through them from frame left to frame right; the stars shiver apart and close again behind it.
- **Dialogue:** —
- **Sound:** a low diesel throb approaching, water hissing along a steel hull, then only the lap of the wake; ambient sound only, no dialogue
- **PROMPT:** Insert, low angle at the waterline, anamorphic 75mm lens, locked-off: black water holding a field of reflected stars fills the frame until the grey steel bow of {PROP_POLICE_LAUNCH.SHORT} slides through it from frame left toward frame right, the reflected stars shivering apart along its wake and slowly closing again. Setting: {LOC_NILE.LONG}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: hushed and vast. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, moon, moonlit water, city skyglow, lit windows, street lights, navigation lights, searchlight beam, people in frame, foam spray toward the lens
- **Refs:** LOC_NILE_NIGHT, PROP_POLICE_LAUNCH_REF
- **Continuity:** Picks up Seq 5's last line ("The launch goes into the dark."). The launch runs dark (L1): no running lights. South = frame right. The stars-in-the-water image is the set-up for the channel payoff in 06.05.

### 06.01.002 — EXT. NILE, SOUTH OF CAIRO - NIGHT — The launch runs south, dark   (8 s)
- **Shot:** Extreme wide establishing shot, anamorphic 35mm · **Move:** slow pan right
- **In frame:** PROP_POLICE_LAUNCH (state L1)
- **Action:** The police launch runs south, frame left to right, a dark shape on a river of stars; both banks black, not a lamp anywhere. SUPER over.
- **Dialogue:** —
- **Sound:** the diesel pounding low and steady, carried across open water; wind in palms; ambient sound only, no dialogue
- **PROMPT:** Extreme wide establishing shot, anamorphic 35mm lens, slow pan right: small in the frame, {PROP_POLICE_LAUNCH.LONG}, {PROP_POLICE_LAUNCH.STATE_L1}, runs south from frame left to frame right down the middle of a broad river of reflected stars, its pale wake the only movement, the banks two long black lines of palms. Setting: {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}. Mood: exhausted resolve. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, moon, city skyglow, lit windows on the banks, street lights, navigation lights, searchlight beam, bright cabin lights, other boats
- **Refs:** PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** SUPER | "5 NOVEMBER. 03:40." | small, lower left, subtitle typeface family (05 §13.7) | in at 1.5 s, out at 6.5 s | seq 06 titles file
- **Continuity:** Launch L1 (running dark, only the dim wheelhouse lamp; file 04 §13; see bible 05 §14 Q2 on the lamp colour). South = frame right. SUPER time per the notes' audit (03:40).

## Scene 2 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS

### 06.02.001 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Aground on the bar   (6 s)
- **Shot:** Medium wide shot, anamorphic 32mm · **Move:** subtle handheld
- **In frame:** FATHI (CHAR_FATHI_B1) at the wheel; TAREK (CHAR_TAREK_B1) at the chart ledge
- **Action:** Fathi squints into the starlit dark through the windscreen; Tarek bends over the paper river chart. The hull scrapes, both men lurch forward, and Fathi hauls the throttle astern; the boat drags free.
- **Dialogue:** —
- **Sound:** a long grinding scrape under the hull, loose gear sliding, the diesel roaring in reverse, then settling
- **PROMPT:** Medium wide shot, anamorphic 32mm lens, subtle handheld: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, {CHAR_FATHI.DMG_L1}, squints through the windscreen at the wheel while {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, bends over {PROP_POLICE_LAUNCH.STATE_CHART_INSERT}; the whole cabin jolts, both men lurch forward, and the soldier at the wheel hauls the throttle lever back hard. Setting: the cramped wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, starlight through the salt-hazed windows, the dim wheelhouse lamp low on their faces. Mood: military exactness under strain. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, {CHAR_TAREK.NEG}, bright cabin lights, glowing navigation screens, map display, daylight, moon, beret on Fathi
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_B_full, CHAR_TAREK_A_front, CHAR_TAREK_B_full, PROP_POLICE_LAUNCH_REF, LOC_NILE_NIGHT
- **Continuity:** Master for the wheelhouse: helm frame left facing the windscreen (south), chart ledge frame right, the open back door to the aft deck behind camera. Fathi bareheaded, scarf at the neck, river-wet to the knees (B1). Tarek sleeves rolled, vest, beret, rifle slung (B; the police handheld is still in its cradle until 06.09).

### 06.02.002 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Tarek: the Asyut lock   (5 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1)
- **Action:** Tarek, braced over the chart, lifts his eyes toward the helm and speaks, low and clipped.
- **Dialogue:** TAREK (in Egyptian Arabic; subtitled): "The first lock south is Asyut. It's networked."
- **Sound:** the diesel steady again; the chart paper rustling; water along the hull
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_TAREK.LONG}, {CHAR_TAREK.WARD_B}, braced over a paper chart, lifts his heavy-lidded eyes toward the helm off frame left, speaking in Egyptian Arabic, low and clipped. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, starlight through the windscreen and the dim wheelhouse lamp modelling his weathered face. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, bright cabin lights, glowing screens, daylight, moon, hand over the mouth
- **Refs:** CHAR_TAREK_A_front, CHAR_TAREK_A_34, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "The first lock south is Asyut. It's networked." | lower third, two lines max (05 §13.7) | line in-point to out-point | seq 06 subtitle file ([[verify: Asyut lock]] per the screenplay)
- **Continuity:** Eyeline to the helm, frame left. Line continues over the chart insert 06.02.003.

### 06.02.003 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — The chart: the only door south   (6 s)
- **Shot:** Insert, 100mm macro · **Move:** slow push-in
- **In frame:** the river chart (PROP_POLICE_LAUNCH state CHART_INSERT); Tarek's hand
- **Action:** A thick weathered finger traces south down the pencilled river and stops on a pencilled line drawn across it; taps it twice.
- **Dialogue:** TAREK (O.S.; in Egyptian Arabic; subtitled): "If it knows we're on the water before we get there, it shuts the gates. And we walk."
- **Sound:** a fingertip dragging on soft paper; two taps; the diesel under it
- **PROMPT:** Insert, 100mm macro lens, slow push-in: a thick, deep-tanned finger traces slowly down {PROP_POLICE_LAUNCH.STATE_CHART_INSERT}, following the pencilled river south to a short pencilled line drawn across it, stops there and taps twice. Setting: the wheelhouse ledge of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim wheelhouse lamp grazing the paper. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable place names, printed labels, digital map, glowing screen, extra fingers
- **Refs:** PROP_POLICE_LAUNCH_REF, CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "If it knows we're on the water before we get there, it shuts the gates. And we walk." | lower third, two lines max | line in-point to out-point | seq 06 subtitle file. The chart carries no legible words: pencil lines and hatched sandbanks only.
- **Continuity:** Chart state 6.1–6.4: the night's route in pencil; it pays off in 06.05.002 (islands "all pencilled sand") and 06.09.006.

### 06.02.004 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — Fathi: time, place, sand   (7 s)
- **Shot:** Medium close-up, anamorphic 75mm · **Move:** locked-off
- **In frame:** FATHI (CHAR_FATHI_B1)
- **Action:** Fathi, both hands on the wheel and eyes on the black water, answers with a dry half-smile, then glances once at Tarek.
- **Dialogue:** FATHI (in Egyptian Arabic; subtitled): "If I knew the time, I'd know where we are. If I knew where we are, I'd know where the sand is."
- **Sound:** the wheel creaking under his hands; the diesel; faint water noise
- **PROMPT:** Medium close-up, anamorphic 75mm lens, locked-off: {CHAR_FATHI.LONG}, {CHAR_FATHI.WARD_B}, both hands on a wooden wheel and his eyes on the dark water ahead, speaking in Egyptian Arabic with a dry half-smile, then glancing once toward the colonel off frame right. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, starlight through the windscreen and the dim wheelhouse lamp reaching his deep-brown face. Mood: wry. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_FATHI.NEG}, bright cabin lights, glowing screens, daylight, moon, scarf over the mouth, beret
- **Refs:** CHAR_FATHI_A_front, CHAR_FATHI_A_34, CHAR_FATHI_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** subtitle | "If I knew the time, I'd know where we are. If I knew where we are, I'd know where the sand is." | lower third, two lines max | line in-point to out-point | seq 06 subtitle file
- **Continuity:** Eyeline to Tarek frame right (reverse of 06.02.002). Scarf knotted at the neck, clear of the mouth (05 §9.2).

### 06.02.005 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — The spoofed watch   (4 s)
- **Shot:** Insert, 100mm macro · **Move:** locked-off
- **In frame:** Tarek's wrist and satellite watch (no bible token; writer's words)
- **Action:** Tarek turns his wrist to the lamp; the watch face flickers and resets, three different times in four seconds.
- **Dialogue:** —
- **Sound:** a faint electronic chirp each time the display resets; the diesel
- **PROMPT:** Insert, 100mm macro lens, locked-off: a thick deep-tanned wrist, the camouflage sleeve rolled back, turns toward the light, showing a chunky black wristwatch whose dark face glows faintly with abstract lines that flicker, blank out and reset again. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, the dim wheelhouse lamp and the watch face's own faint glow. Mood: military exactness. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, readable digits, brand name on the watch, logo, smartwatch apps, bright screen glare
- **Refs:** CHAR_TAREK_B_full, LOC_NILE_NIGHT
- **Flags:** COMP
- **Comp:** watch display | "04:10" (1.2 s) → "02:51" (1.2 s) → "11:37" (1.2 s), each with a 2-frame blank between; plain 7-segment digits | on the watch face, tracked | full shot | seq 06 graphics
- **Continuity:** Tarek's satellite watch is spoofed like the GPS in Seq 5 (notes audit). No PROP token exists for this watch: described in writer's words (gap logged).

### 06.02.006 — INT. POLICE LAUNCH, WHEELHOUSE - CONTINUOUS — "I can tell you the hour."   (5 s)
- **Shot:** Two-shot, anamorphic 40mm · **Move:** locked-off
- **In frame:** TAREK (CHAR_TAREK_B1), FATHI (CHAR_FATHI_B1)
- **Action:** A voice from the dark aft deck; both men turn their heads toward the open back door, frame right.
- **Dialogue:** TUT (O.S.): "I can tell you the hour."
- **Sound:** Tut's light, clear voice from outside, close to the door; the diesel
- **PROMPT:** Two-shot, anamorphic 40mm lens, locked-off: in the dim wheelhouse, {CHAR_TAREK.SHORT}, {CHAR_TAREK.WARD_B}, and {CHAR_FATHI.SHORT}, {CHAR_FATHI.WARD_B}, both turn their heads toward the open back door at frame right, listening to a quiet voice from the dark deck outside. Setting: the wheelhouse of {PROP_POLICE_LAUNCH.SHORT}, on {LOC_NILE.SHORT}, in the dead of night. Lighting: {LOC_NILE.LIGHT_NIGHT}, starlight through the door and the dim wheelhouse lamp on their faces. Mood: dry, literal calm. {SUFFIX}
- **NEGATIVE:** {NEG}, {NEG_MODERN_EGYPT}, {CHAR_TAREK.NEG}, {CHAR_FATHI.NEG}, third person in the doorway, bright cabin lights, daylight, moon
- **Refs:** CHAR_TAREK_A_34, CHAR_FATHI_A_34, CHAR_TAREK_B_full, CHAR_FATHI_B_full, LOC_NILE_NIGHT
- **Continuity:** Tut is on the aft deck, unseen here; hand-off to 06.03.001.
