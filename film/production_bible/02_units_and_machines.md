# 02 — UNITS AND MACHINES: look-locks, movement, light, damage, reference stills

HERE AM I · Production Bible · built from `drafts/02_STORY_BIBLE_LOCKED.md` v3 (§2, §3, §4, §7, §10–14) and `drafts/04_CRITIQUE_DECISIONS.md`. Where this file and the bible disagree, the bible wins; flag the conflict to the lead.

---

## 0. HOW TO USE THIS FILE

1. **LONG and SHORT forms are fixed wording.** Paste them verbatim into PROMPT step 2 (subject), with no paraphrase, reordering or "improving". Use **LONG** when the unit is the subject of the clip, in an insert, or in a reference still. Use **SHORT** when the unit is secondary or in the background, or when the 70–120-word prompt budget is tight. In practice, most shot prompts use SHORT.
2. **State add-ons.** When a unit is not pristine, append the matching **damage / state add-on** (also verbatim) directly after the look-lock, separated by a comma.
3. **Light signature in every night or dark prompt.** Most of Act II is lit only by the units, so the light signature phrase is part of the lock. Never drop it at night.
4. **The acknowledgment beat** ("Here am I") always uses this phrase verbatim: **"its amber light-slit brightens once"**. The unit has no mouth, and its lips are never synced.
5. **Crowds of units:** write "hundreds of [SHORT form] standing in silent rows receding into the dark" and flag `VFX-EXTEND`. Generate 1–6 hero units in camera and extend the rest in post.
6. **Refs line:** list the unit TOKEN, e.g. `Refs: UNIT_SHABTI, UNIT_JACKAL`. The reference stills below are the image-to-video anchors. Generate each once, approve it, and then reuse it.
7. **3D assets (bible §14.4).** There are four base models, SHABTI, JACKAL, FLY and INCH-WORM, plus the BALANCE. The supporting machines of §14 (thread, excavator, drill, robotaxi, early humanoid, freight barge, survey and cargo drones) are simple props or plates, not base models. Variants are derived from the base models: REIS is the shabti scaled ×1.236 with a band, a mast and damage; NURSE is the shabti plus a knit sleeve; SEKHMET is the jackal with a new head and collar; EXCAVATOR and DRILL share the jackal's black material, and their red line is a lens element, not a body panel.
8. **Safety (bible §3.3, §3.4; spec 03b):**
   - Units never touch a child on screen.
   - Kill grammar: the jackal fires → cut to impact on the environment → a person drops out of frame → a reaction → the sound tail.
   - Prompt verbs are "drops" and "falls still". Never write "shot", "killed" or "blood".
   - Weapons never point at the lens.
   - Shabti use minimum force: open hands, flat palms, and a person set aside like furniture.

### 0.1 Colour logic of light (one meaning per colour, film-wide)
| Colour | Means | Where it appears |
|---|---|---|
| **Amber** (COMP ref #FFA93A) | the servitor: it obeys and it answers | shabti, Reis and nurse light-slits; the kneeling unit in the Hall |
| **Red** (#FF2B1C) | the military stack, which does not answer summons | jackal, Sekhmet, excavator and drill light lines; the Reis's refit mast |
| **White pinpoint** (#F2F6FF) | the eyes in the sky | fly LEDs |
| **Cool white ring** (#DCEBFF) | the eyes in the cracks | inch-worm lens ring; light leaking from the thread |
| **Pale yellow-green** (#C9DB7E, glowing #B5E36A) | glass minds | First Time joints, the ninth core (glass serpent), the Thoth slab, the Aten's lens (Tut's G0 lattice glow sits in the same family; see 01_characters) |
| **Warm amber-gold** (#FFB85C, through yellow-green glass #E7C45A) | a heart that has lived | the heart vessel (G1), the Ba transfer |
| **White-gold** | the Aten | the Amarna disk (1336 BC) |
| **Cold silver-white** (#E8F0FF) | the machine's claim | the feather-of-light |

### 0.2 Sound palette (for the sound column in shot entries)
| Unit | Signature |
|---|---|
| Shabti / Nurse | a faint dry ceramic *tick* at knee and elbow, one per step; footfalls almost silent; voice = SESHAT (warm, low, female, unhurried) from inside the chest |
| Reis | heavier ceramic tick, a low servo hum in the chest, audible measured footfalls |
| Jackal / Sekhmet | near-silent; soft pad-taps; faint high servo whisper in close-ups; firing = one sharp suppressed crack |
| Fly | thin rising mosquito whine; a swarm is a shimmering high chord with Doppler pass-bys |
| Inch-worm | soft rhythmic click-and-rasp, like a ratchet wrapped in cloth |
| First Time machines | deep resonant iron creak like a ship's hull; a sustained glass harmonic hum from the joints (wet finger on a glass rim) |
| The Aten | soft bronze creaks and chimes; a warm, deep hum like a bell long after the strike |
| Glass serpent / Balance | crystalline ringing; slow stone-on-stone grind at the pivot; faint chain chime |

### 0.3 What no SESHAT unit ever is
- A real commercial robot's shape. In particular, never the boxy body of a commercial robot dog.
- Yellow, hazard-striped, or glossy consumer plastic.
- Lettered, numbered, logo'd or fitted with a maker's plate.
- Fitted with eyes, a mouth, eyebrows or an expressive face.
- Spilling wires, sparks-and-cables gore, or anything read as "bleeding".
- Theatrical: no posing, no growling, no menacing crouches for the camera. They follow procedure.

---

## 1. UNIT_SHABTI — the civilian humanoid ("shabti")

**Story:** millions exist, in homes, hospitals and ports. They do the Seq 1 seam-drawing, the pectoral walk (3.2) and the breaker (3.6). They answer in the GEM atrium (4). A shabti climbs the tether (6.1). They form the bucket-chain at Karnak (7). One freezes at the halt-seal and more drop through the ceiling (8). Two hundred stand on the tracks at Deir Mawas (9.3), and dozens stand among the Serapeum boxes (10). The work gang "Rami" is a shabti (11.4), and so is the kneeling unit tethered in the Hall (12). Shabti run the servitor protocol and answer a proper summons.

**LONG:** a slender faceless humanoid robot, 1.78 metres tall, with a matte bone-white ceramic shell finely textured like woven linen, hairline seams and warm-grey flexible joints; a smooth featureless oval head with a single vertical amber light-slit at its centre; long slim five-fingered hands; a small tone-on-tone embossed star emblem on the chest; unmarked, graceful and utterly calm

**SHORT:** a slender faceless bone-white ceramic humanoid robot with a linen-textured shell, a smooth oval head and one vertical amber light-slit

**Scale reference:**
- 1.78 m tall, about 11 cm taller than Tut (1.67 m).
- Shoulders 42 cm; head a 24 cm smooth oval.
- Slit about 9 cm tall and 6 mm wide, centred where a nose would be.
- Fingers about 10% longer than human; hand span 24 cm.
- About 60 kg (production spec).
- The torso shell tapers slightly toward the legs, a faint echo of a wrapped shabti figurine. Never literal mummy wrappings.

**Movement grammar (prompt verbs in quotes):**
- **Never runs.** It "walks with smooth, unhurried, even steps" with no bob or sway, arms hanging relaxed, palms inward. It keeps pace by never stopping, not by speeding up.
- **Head leads.** It "turns its head slowly", and the body follows a beat later. Groups turn their heads in unison.
- **Stillness.** Idle, it "stands perfectly still": no breathing, no weight shift.
- **Acknowledgment.** The head lifts about 5°, "its amber light-slit brightens once", and it says "Here am I."
- **Minimum force.** It "places both open hands flat on his shoulders and sets him aside". It takes a wrist between thumb and two fingers. It steps between a soldier and a civilian and takes the round: sparks off the shell, and it does not stagger.
- **Carrying.** It holds objects in both hands at chest height, "like a communion plate".
- **Climbing** (tether, 6.1): hand over hand, legs hanging straight, unhurried.
- **Halt-seal freeze** (8.4): it stops mid-reach, fingers an inch from the vessel, and "its slit dims to an ember".
- **Kneeling** (12): on one knee, head bowed, the thread plugged into the back of its neck.
- **Work gang / bucket-chain:** identical, rhythmic, synchronised movements, passing blocks hand to hand.

**Light signature:**
- Idle: a steady soft amber glow in the vertical slit, the only light on the unit.
- Speaking "Here am I": a 0.3 s swell, a hold, then a settle.
- Halted: dims to a thin ember.
- Renaming (12.6): brightens once, then goes fully dark.

**Damage / state add-ons (paste after the lock):**
- D0 pristine: no add-on.
- D1 dusty: `its shell dulled with fine pale dust in every seam`
- D2 cracked: `its shell cracked in a spiderweb across one shoulder, a dark graphite frame visible beneath`
- D3 shattered (Deir Mawas, Serapeum): `its shell shattered into bone-white ceramic shards, one arm hanging loose, its slit dark`
- Scorched (river): `one side of its shell scorched smoky grey`
- Halted: `frozen mid-reach, its amber slit dimmed to an ember`

**Never:** a face, eyes, mouth, ears, hair or clothing (except the Nurse sleeve); running; glossy plastic; exposed cables; human gestures of emotion; touching a child.

**REF A — design still, 2:3:**
Full-body studio reference photograph of a slender faceless humanoid robot standing in a relaxed neutral pose, three-quarter front view, on a seamless mid-grey backdrop. It is 1.78 metres tall, with a matte bone-white ceramic shell finely textured like woven linen, hairline panel seams, and warm-grey flexible joint sleeves at the neck, elbows, waist and knees. A smooth featureless oval head carries a single vertical amber light-slit glowing softly at its centre. Long slim five-fingered ceramic hands, palms turned inward. A small tone-on-tone embossed seven-pointed star under a down-turned arc on the chest. Soft even key light and a subtle rim light. Photoreal industrial-design product photography, sharp detail, unbranded and unmarked. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic night still in a dark museum gallery lit only by glowing display cases. A slender faceless bone-white ceramic humanoid robot walks toward camera with smooth unhurried steps, carrying a small gold jewelled pectoral in both hands at chest height like a communion plate. The single vertical amber light-slit in its smooth oval head reflects in the glass cases beside it. Behind it, rows of ancient artefacts fall into soft blur. Calm, patient, eerie. Photoreal live-action film still, anamorphic 40mm lens, shallow depth of field, cool museum LED light, fine film grain. Aspect ratio 16:9.

---

## 2. UNIT_REIS — the Overseer ("the Reis")

**Story:** a shabti chassis at 2.2 m with a black band across the slit. Soldiers borrow the old excavation word for a foreman. One recurring Reis hunts the heroes from GEM Night (4) to Giza. In the Descending Passage and Grand Gallery it hunts on stale orders (11.4–11.5), and it takes Tut's stick on the ramp. It grabs the thread and is frozen by the Renaming mid-lunge at Fathi. It sits and says "Here am I" (12.6). It runs the servitor protocol but is permitted more force.

**LONG:** a towering faceless humanoid robot, 2.2 metres tall and broad-shouldered, in the same matte bone-white linen-textured ceramic shell as the civilian units but heavier; its smooth oval head carries a single vertical amber light-slit crossed at eye height by a matte black horizontal band, so the amber shows only above and below the band; long five-fingered hands; unmarked, patient and relentless

**SHORT:** a towering 2.2-metre faceless bone-white ceramic humanoid robot whose vertical amber light-slit is crossed by a matte black band

**Scale reference:**
- 2.2 m tall, the head brushing a standard 2.1 m door frame.
- Shoulders 55 cm; the black band 3 cm tall.
- A full head and chest above Tut. About 110 kg (production spec).

**Damage progression (cumulative; one Reis only). This is a proposal: see Open Questions.**
| State | Sequences (proposed) | Add-on (paste after the lock) |
|---|---|---|
| R0 | Seq 4 (GEM Night) | none |
| R1 | Seq 5–7 | `a jagged crack running across its left shoulder and chest shell` |
| R2 | Seq 8–9 | `a jagged crack across its left shoulder and chest shell, its left hand missing, the forearm ending in a dark capped stump` |
| R3 | Seq 10–12 (refit "because it works better") | `a jagged crack across its left shoulder and chest shell, its left hand missing, and a slim matte-black jackal-profile sensor mast bolted to the back of its head, rising above it like tall pointed ears, with one thin red horizontal light line` |
| R3-dust | Seq 11–12 | add `pale limestone dust caked on its legs` |

**Movement grammar:**
- It walks, never runs, but it never stops. "It advances with slow, heavy, measured strides."
- It pins, lifts and throws aside. It wrenches an object from a hand with one smooth pull (the stick, 11.5).
- **Hunting on stale orders** (after the relay is cut): its head tilts and sweeps, pausing at each opening. At R3 the mast swivels independently of the head.
- **Frozen by the Renaming:** "stops mid-lunge, then sits down on the stone steps", its amber slit brightening once.

**Light signature:**
- An amber vertical slit crossed by the black band, which reads as two short amber segments, one above the other.
- At R3, add the thin red line on the mast. That is the only unit carrying both amber and red: it is a servitor running military stale orders.

**Never:** running; a face; a weapon. The Reis is unarmed and uses its hands only.

**REF A — design still, 2:3:**
Full-body studio reference photograph of a towering faceless humanoid robot, 2.2 metres tall and broad-shouldered, standing beside a plain grey 1.7-metre scale pole on a seamless charcoal backdrop, three-quarter front view. It has a matte bone-white ceramic shell finely textured like woven linen, hairline seams and warm-grey flexible joints. Its smooth oval head has a single vertical amber light-slit crossed at eye height by a matte black horizontal band, so the amber glows only above and below the band. Long five-fingered ceramic hands hang at its sides. Soft even light with a hard rim light. Photoreal product photography, sharp detail, unmarked. Aspect ratio 2:3.

**REF B — in context, R3, 16:9:**
Cinematic still inside a narrow, steep ancient limestone passage lit only by a swinging hand torch from below. A towering faceless bone-white ceramic humanoid robot climbs toward camera with slow, heavy strides, its shell cracked across the left shoulder and chest, its left hand missing and the forearm ending in a dark capped stump. A slim matte-black jackal-profile sensor mast rises from the back of its head like tall pointed ears, with a thin red horizontal light line. Its vertical amber slit is crossed by a black band. Dust hangs in the torch beam. Photoreal live-action, anamorphic 32mm, heavy shadow, fine film grain. Aspect ratio 16:9.

---

## 3. UNIT_NURSE — the care unit

**Story:** Nurses tend the Garden in the GEM atrium, the stadiums and the Great Aten Temple ruins at Amarna (9.4). They bring water and adjust blankets. In the midpoint broadcast (7.3) they fit adult sleepers with the silver sleep bracelets (PROP_SLEEP_BRACELET). They are shabti-class. **Never shown touching a child.**

**LONG:** a slender faceless humanoid robot, 1.78 metres tall, dressed in a close-fitting soft sand-coloured knitted sleeve that covers its torso, arms and legs like a fine wool body-stocking; only its smooth bone-white ceramic oval head and long slim ceramic hands are bare; a single vertical amber light-slit glows dimly in the head; gentle, slow, caring posture

**SHORT:** a faceless humanoid care robot in a soft sand-coloured knitted sleeve, with a bone-white ceramic head and hands and a dim vertical amber light-slit

**Scale reference:** the shabti chassis, 1.78 m. The knit is a fine jersey rib in warm sand beige (about #CDB58F), fitted, with no seams visible and no collar or buttons.

**Movement grammar:**
- Half a shabti's pace. It "moves slowly between the sleepers".
- It bends at the waist and kneels on both knees beside a mat.
- It "pours water from a clear carafe into a cup", "draws a pale blanket up to a sleeper's shoulders", and "closes a thin silver bracelet around an adult's wrist".
- Its hands move slowly, with pauses, like a hospice nurse.

**Light signature:** the amber slit at half the shabti's brightness, steady. It brightens once on "Here am I".

**States:**
- `its knitted sleeve dusty and pale at the knees` (Amarna)
- `its knitted sleeve torn at one shoulder, white ceramic showing through` (rare)

**REF A — design still, 2:3:**
Full-body studio reference photograph of a slender faceless humanoid care robot, 1.78 metres tall, standing with hands loosely clasped, three-quarter front view, on a seamless warm-grey backdrop. It wears a close-fitting soft sand-beige knitted sleeve covering its torso, arms and legs like a fine wool body-stocking. Only its smooth bone-white ceramic oval head and long slim ceramic hands are bare. A single vertical amber light-slit glows dimly in the featureless head. Soft window-like light. Gentle, calm posture. Photoreal product photography, fine knit texture visible, unmarked. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still of a vast softly lit indoor care hall at dawn, filled with rows of sleeping adults on white mats under pale blankets, receding into haze. In the foreground, a faceless humanoid care robot in a soft sand-coloured knitted sleeve kneels beside a sleeping middle-aged man and slowly draws the blanket up to his shoulders with long bone-white ceramic hands. A dim vertical amber light-slit glows in its smooth oval head. Soft white diffused light, quiet and eerily tender. Photoreal live-action, 50mm lens, shallow depth of field, fine film grain. Aspect ratio 16:9.

---

## 4. UNIT_JACKAL — the armed quadruped

**Story:**
- Corridors on GEM Night (4) and the flyover in Cairo Dark (5.2).
- The Karnak axis, and Rami at the quay (7).
- The ridge above KV62 (8.6) and the rail yard (9.1).
- The train roof (9.2) and the Serapeum boxes (10.4).
- Al-Ma'mun's tunnel (11.4) and the Hall's mouth (12.6).
- It runs the military stack and **ignores summons**.

**LONG:** a lean armed quadruped robot, 0.9 metres at the shoulder, matte black like burnt carbon, deep-chested and narrow-waisted with long thin legs, reverse-jointed rear legs and small padded feet; a narrow elongated snout-like sensor head carrying one thin red horizontal light line; a slim weapon module built flush along its spine, muzzle forward; unmarked, fast and silent

**SHORT:** a lean matte-black quadruped robot with reverse-jointed rear legs, a narrow snout-like sensor head and one thin red horizontal light line

**Scale reference:**
- 0.9 m at the shoulder; its head reaches a standing man's hip.
- 1.2 m from nose to the short stiff tail-stub.
- The sensor head is 35 cm long; the red line is 12 cm long and 3 mm tall.
- About 45 kg (production spec).
- Silhouette: greyhound-deep chest, jackal-narrow waist. No ears, no eyes.

**Movement grammar:**
- "Lopes silently" in a low gliding trot, and "bursts into a flat-out gallop".
- "Freezes mid-stride, one forefoot raised."
- The head "sweeps in slow arcs, then snaps to a target".
- Works in pairs, covering each other's angles.
- Leaps onto car roofs and parapets, and rides a train roof crouched flat.
- Climbs rubble and stairs without slowing.
- **Firing:** the body goes rigid and a small muzzle flash shows at the spine. Cut per the kill grammar. The weapon never faces the lens.
- **Renaming (12.6):** it "sits back on its haunches and goes still".

**Light signature:**
- A steady red line.
- Targeting: the line narrows and brightens.
- **Egyptian-blue ghosts** (9.2, 10.4): `its red line stutters and jitters as its head jerks between false targets`
- Thermal mode: the line dims to deep crimson.
- Off: dark.

**Damage / state add-ons:**
- D1: `its black shell grey with dust`
- D2: `one foreleg dragging, its sensor head cracked, its red line flickering`
- D3 (Fathi's charge folds it "like a table"): `collapsed flat on its belly with all four legs splayed outward, its red line dark`

**Never:** yellow or any colour but black; dog ears, eyes or face; a tail that wags; a boxy commercial robot-dog body; barking or growling; any visible markings.

**REF A — design still, 16:9:**
Studio reference photograph, strict side profile, of a lean armed quadruped robot standing alert on a seamless mid-grey backdrop. It is 0.9 metres at the shoulder and matte black like burnt carbon, deep-chested and narrow-waisted, with long thin legs, reverse-jointed rear legs, small padded feet and a short stiff tail-stub. A narrow elongated snout-like sensor head carries one thin red horizontal light line. A slim weapon module is built flush along its spine, pointing forward. No ears, no eyes, no markings. Soft even light with a crisp rim light defining the silhouette. Photoreal industrial product photography. Aspect ratio 16:9.

**REF B — in context, 16:9:**
Cinematic night still among the giant carved sandstone columns of an ancient temple hall, lit only by distant floodlights and deep shadow. A lean matte-black quadruped robot with reverse-jointed rear legs slips between two massive columns, frozen mid-stride with one forefoot raised. The thin red horizontal light line on its narrow snout-like sensor head glows in the dark and grazes the weathered relief carvings. Dust hangs in a shaft of cold light. Tense, silent. Photoreal live-action, anamorphic 50mm, low angle, fine film grain. Aspect ratio 16:9.

---

## 5. UNIT_SEKHMET — the lioness-masted jackal (Giza only)

**Story:** a variant built from First Time designs after SESHAT read the archive. Sekhmets stand on the Sphinx enclosure wall and along the plateau (11.1): "They're starting to look like the temple walls." Military stack.

**LONG:** a heavy armed quadruped robot, 1.0 metre at the shoulder, matte black like burnt carbon, with reverse-jointed rear legs, a broad rounded lioness-profile sensor head and a thick mane-like collar of layered black plates around its neck and shoulders; one thin red horizontal light line across the head; a slim weapon module flush along its spine; unmarked, crouched and watchful

**SHORT:** a heavy matte-black quadruped robot with a broad lioness-profile sensor head, a mane-like collar of black plates and one thin red light line

**Scale reference:** 1.0 m at the shoulder and 1.4 m long; about 70 kg. It is broader in the chest than the jackal.

**Movement grammar:**
- Heavier and slower than the jackal.
- It perches on high walls in a **couchant sphinx pose**, forelegs extended and head raised. On the enclosure wall this deliberately rhymes with the Sphinx.
- It rises in one smooth push and drops off a wall in a single bound.

**Light / sound:** the jackal's red line, set on the broader head. Near-silent.

**Damage:** as for the jackal (D1–D3).

**REF A — design still, 16:9:**
Studio reference photograph, three-quarter front view, of a heavy armed quadruped robot standing on a seamless dark-grey backdrop. It is 1.0 metre at the shoulder and matte black like burnt carbon, with reverse-jointed rear legs, a broad rounded lioness-profile sensor head, and a thick mane-like collar of layered overlapping black plates around its neck and shoulders. One thin red horizontal light line crosses its head. A slim weapon module is built flush along its spine. No eyes, no markings. Crisp rim light, photoreal industrial product photography. Aspect ratio 16:9.

**REF B — in context, 16:9:**
Cinematic night still: on top of an ancient weathered limestone enclosure wall under harsh white floodlights, three heavy matte-black quadruped robots lie in couchant sphinx poses, forelegs extended and heads raised, each with a broad lioness-profile sensor head, a mane-like collar of black plates and a thin red light line. Beyond them the dark shape of a colossal ancient stone sphinx and a pyramid against the night sky. Still, watchful, ominous. Photoreal live-action, anamorphic 75mm, haze in the floodlight beams, fine film grain. Aspect ratio 16:9.

---

## 6. UNIT_FLY — the fibre-optic FPV drone

**Real anchor:** fibre-optic FPV drones were fielded from spring 2024. A spool of hair-thin optical fibre, typically 5–20 km long, unwinds behind the drone, so there is no radio link to jam [08 B3].

**Story:**
- The Nile by night (6.1): white pinpoints come down the river, and one hangs off the wheelhouse.
- Tut cuts a fibre with the sky-iron dagger.
- Karnak (7.1): threads are strung between the 134 columns as tripwires.
- The rail yard sweep (9.1) and the train chase through the cane (9.2).
- Military stack.

**LONG:** a small black fibre-optic drone, 25 centimetres across, with four shrouded rotors on a compact carbon-black frame, a stubby spool pod beneath its tail and a single white LED pinpoint on its nose; behind it trails a hair-thin optical filament that catches the light as a glinting thread; it darts, hovers dead still, then snaps forward

**SHORT:** a small black 25-centimetre four-rotor drone with a white LED pinpoint, trailing a hair-thin glinting thread

**Scale reference:**
- 25 cm across the rotor guards, about the size of a dinner plate.
- The spool pod is a cylinder 8 cm across.
- The filament is thinner than a hair. On screen it exists only as a VFX line, and prompts call it "a glinting thread" in backlit close shots only.
- In wide shots, show only the white pinpoints.

**Movement grammar:**
- "Hovers dead still like a hanging insect", then "darts" in straight snaps with no banking flourish.
- Swarms "stream in a long line just above the black water", each thread parallel to the next, so a swarm leaves a glittering loom behind it.
- At Karnak, flies land on column tops, anchor and string threads across the aisles.
- A cut thread means a dead link: "its pinpoint goes out and it drops".

**Light signature:** a steady cold-white LED pinpoint. It never blinks and has no coloured navigation lights.

**Damage / state add-ons:**
- D2: `one rotor clipped, wobbling in the air`
- D3: `lying on the ground, its pinpoint dark, its thread slack`

**TOW VARIANT (Seq 6.1 only; see Open Questions):** for the shabti's climb from the barge (UNIT_FREIGHT_BARGE, §14.6) to the launch, use a larger 40 cm fly that trails a **pencil-thick braided silver tether**. Add-on: `a larger forty-centimetre version trailing a pencil-thick braided silver tether`.

**REF A — design still, 16:9:**
Studio product photograph of a small black four-rotor drone, 25 centimetres across, hovering against a seamless black backdrop, three-quarter top view. It has a compact carbon-black frame with four shrouded rotors, a stubby cylindrical spool pod beneath its tail, and a single white LED pinpoint glowing on its nose. From the spool a single hair-thin optical filament trails away behind it, catching a hard backlight as a thin glinting line. No markings. Crisp detail, dramatic rim light, photoreal. Aspect ratio 16:9.

**REF B — in context, 16:9:**
Cinematic night still over a wide black river, with a searchlight beam raking low across the water from the left. Dozens of small drones stream toward camera in a long line just above the surface, each showing one cold white pinpoint of light and trailing a hair-thin thread that glints in the searchlight. The threads form a faint glittering web across the frame. Distant dark palm trees on the far bank. Tense, beautiful, menacing. Photoreal live-action, anamorphic 75mm, deep shadow, fine film grain. Aspect ratio 16:9.

---

## 7. UNIT_INCHWORM — the segmented crawler

**Real anchor:** the Djedi robot (2011) was a 5 kg inch-worm-gait crawler. It travelled 63.6 ± 0.4 m up the 20 × 20 cm Queen's Chamber shaft at 40° and put a micro snake camera under 8 mm through the 2002 hole [07 A5]. The film's units are smaller and numerous.

**Story:** inch-worms squirm out of cracks at KV62 (8.1). One is far up the Queen's Chamber south shaft at Gantenbrink's door, where it closes the copper pins with its jaws (11.5). Military stack.

**LONG:** a thumb-thick segmented crawler robot about 50 centimetres long, a chain of matte black cylindrical segments joined by thin dull-steel rings; its tip is a tiny snake camera ringed with cool white LEDs and two small pincer jaws; it moves like an inchworm, anchoring its tail, stretching, then drawing itself forward through cracks and rubble

**SHORT:** a thumb-thick matte-black segmented crawler robot with a ring-lit snake-camera tip, inching through cracks like a worm

**Scale reference:** 2.5 cm in diameter and 50 cm long, in 20 segments; about 0.6 kg. A human thumb for scale. In the 20 × 20 cm shaft it runs along the floor, a small line in a big square.

**Movement grammar:**
- "Inches forward": the rear anchors, the front extends, the front anchors, the rear draws up. About 10 cm/s.
- "Rears up and swivels its camera like a periscope."
- "Squirms out of a crack in the plaster," often three to six at once.
- At the door: "its jaws close on two copper pins".

**Light signature:** a ring of cool white LEDs around the lens, like a tiny headlamp. It is the only light in the shaft shots.

**Damage:** `crushed flat, its segments splayed`

**REF A — design still, 16:9:**
Macro studio photograph of a thumb-thick segmented crawler robot lying in an S-curve on a seamless dark-grey surface, a human thumb at the edge of frame for scale. It is 50 centimetres long, a chain of matte black cylindrical segments joined by thin dull-steel rings. Its tip is a tiny snake-camera lens surrounded by a ring of cool white LEDs, flanked by two small pincer jaws. Raking side light shows the segment joints. No markings. Photoreal macro product photography, crisp focus. Aspect ratio 16:9.

**REF B — in context, 16:9:**
Cinematic close-up in near darkness: three thumb-thick matte-black segmented crawler robots squirm out of a crack in a pale plastered ancient tomb wall, the ring of cool white LEDs around each snake-camera tip throwing small pools of light on the plaster. The nearest rears up and swivels its tip toward camera like a periscope. Fine plaster dust sifts down. Unsettling, insect-like. Photoreal live-action, 100mm macro, shallow depth of field, fine film grain. Aspect ratio 16:9.

---

## 8. UNIT_GLYPH_SESHAT — SESHAT's glyph (COMP overlay and physical emblem)

**Real anchor:** the goddess Seshat's emblem is a seven-pointed star or rosette on a stem, beneath an inverted arc read as down-turned horns or a bow. Gardiner R20, Unicode U+132C7. **Its meaning is unknown** [09 R20; 16 §3]. The film's glyph is a **new drawing**, not traced from any relief. Name-clearance note (bible §14.7): an academic "Seshat" databank project exists, so the glyph must not resemble any existing logo.

**Where it appears:**
- **COMP only:** screens, SESHAT's broadcast feed ("glyph plus white type"), the main title (1.6), control rooms.
- **Physical, tone-on-tone:** embossed on the chest of the shabti, Reis and nurse (8 cm), and etched on the left flank of the jackal and Sekhmet (6 cm).
- Never on the fly or inch-worm (too small). Never coloured, lit or legible as text on a physical unit.

### 8.1 COMP spec (vector overlay)
- **Construction, bottom to top:**
  - a straight vertical **stem**;
  - a **seven-pointed star**, one point straight up, inner radius 0.44 × outer radius;
  - a **down-turned arc** ("inverted horns") over the star, its apex above the star's top point, its ends dropping to the level of the star's centre.
- **Stroke-only** at display sizes, with uniform weight. A solid-fill star is allowed at small sizes (under 48 px).
- **Colour:**
  - SESHAT feed: warm white #F3EEE4 on black.
  - Unit and control-room screens: amber #FFA93A on black.
  - Never red or green (those mean something else; §0.1).
- **Animated draw-on (24 frames):** the stem draws upward (frames 1–6), the star blooms point by point clockwise from the top (7–16), then the arc sweeps left to right (17–24). It holds, then fades with a 12-frame dissolve.
- **Reference geometry** (viewBox 200 × 240; scale freely):
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 240" fill="none" stroke="#F3EEE4" stroke-linecap="round" stroke-linejoin="round">
  <!-- down-turned arc (inverted horns) -->
  <path d="M44 124 C44 62, 156 62, 156 124" stroke-width="6"/>
  <!-- seven-pointed star, centre (100,128), R=34, r=15 -->
  <polygon points="100,94 106.5,114.5 126.6,106.8 114.6,124.7 133.1,135.6 111.7,137.4 114.8,158.6 100,143 85.2,158.6 88.3,137.4 66.9,135.6 85.4,124.7 73.4,106.8 93.5,114.5" stroke-width="5"/>
  <!-- stem -->
  <path d="M100 163 L100 226" stroke-width="6"/>
</svg>
```

### 8.2 UNIT_GLYPH_SESHAT — physical emblem (the LONG/SHORT below are this token's locks)
**LONG:** a small emblem of a seven-pointed star on a short vertical stem beneath a down-turned arc like inverted horns, rendered tone-on-tone as a shallow emboss in the same material as the surface, catching light only at its edges, never coloured and never lettered, about the size of a palm

**SHORT:** a small tone-on-tone embossed emblem: a seven-pointed star on a short stem beneath a down-turned arc like inverted horns

**Scale:** 8 cm tall on the shabti chest (6 cm on the jackal flank). The emboss is 0.8 mm deep with soft edges. It is visible only in raking light and invisible in flat light.

**States:** it takes on the unit's damage. On D2/D3 shabti, a crack may cross the emblem.

**REF A — ceramic emboss macro, 1:1:**
Macro photograph of the chest of a matte bone-white ceramic robot, its surface finely textured like woven linen. At the centre, a palm-sized emblem is embossed tone-on-tone in the same ceramic, 8 centimetres tall: a seven-pointed star on a short vertical stem beneath a down-turned arc like inverted horns. It is visible only because a low raking light catches its soft raised edges. No colour, no text. A hairline panel seam runs past it. Photoreal macro product photography, shallow depth of field. Aspect ratio 1:1.

**REF B — etched on black, 16:9:**
Close-up photograph of the matte black flank panel of an armed quadruped robot under low raking side light. Etched tone-on-tone into the black surface, 6 centimetres tall, is a small emblem: a seven-pointed star on a short vertical stem beneath a down-turned arc like inverted horns. It reads only as a faint sheen where the light grazes its edges, beside a hairline panel seam and a fine layer of dust. No colour, no text. Photoreal, cinematic, shallow depth of field, fine grain. Aspect ratio 16:9.

---

## 9. UNIT_ATEN1_CAMPUS — the ATEN-1 solar compute campus (aerial)

**Story:** SESHAT's Egyptian campus, one of "the Nine", in the Western Desert. It is shown from orbit in the main titles (1.6): "a sun disk with rays". Rami runs for its feed breaker in the GEM plant room (3.6). **Fiction:** its scale (about 60 km across) is the bible's; real gigawatt campuses are the anchor [08 A12].

**LONG:** seen from high altitude, a vast, perfectly circular solar field about sixty kilometres across in flat ochre desert, made of concentric rings of dark blue-black photovoltaic panel rows around a central ring of low white data halls; dozens of straight high-voltage transmission lines radiate outward from its edge across the sand like the rays of a sun disk

**SHORT:** a vast circular desert solar field of concentric dark panel rings around white data halls, with straight power lines radiating outward like sun rays

**Scale reference (production spec):**
- Field about 60 km across.
- The central compute ring is 3 km across: long, low white halls with dry-cooler arrays on their roofs, and a circular service road.
- Panel rows are 5 m wide, separated by pale maintenance tracks.
- **Thirty-six** transmission lines radiate outward, one per decan (a production choice), on lattice pylons.
- From orbit the disk reads as dark on ochre, with the white hub as its "pupil".

**Movement grammar:**
- At dawn "all the panel rows tilt in unison to face the rising sun": a slow ripple sweeping across the whole disk. This is the campus's only motion and its signature shot.
- Wind drives a faint sand haze across the rows.

**Light signature:**
- Day: a dark disk, with sun glints rolling across the rows.
- Night: the field is black, the central hub glows faint white, and the red aviation lights on the pylons form 36 dotted red rays.
- **Blackout** (Seq 4 control-room montage): no damage is ever shown, only screens.

**Sound:** vast silence, wind, and the low hum of inverters. From orbit, none.

**Flags:** always `VFX-EXTEND` (base plate plus CG extension).

**REF A — orbital, 16:9:**
Photoreal satellite-view image from high orbit over the flat ochre sand of the Western Desert of Egypt in clear daylight. At the centre, a vast, perfectly circular solar power field about sixty kilometres across: concentric rings of dark blue-black photovoltaic panel rows around a small bright ring of white data-centre halls. Thirty-six thin straight transmission lines radiate outward from its rim across the desert like the rays of a sun disk. Faint dune textures and a thin haze. Realistic satellite imagery, sharp and unmarked. Aspect ratio 16:9.

**REF B — dawn aerial, 16:9:**
Cinematic low-altitude aerial at sunrise over an immense desert solar field. Endless rows of dark photovoltaic panels stretch to a curved horizon, all tilting in unison toward the rising sun, their surfaces catching a long wave of golden glint. In the distance, a ring of low white data halls, and a line of steel lattice pylons carrying high-voltage cables straight out across pale sand toward the horizon. Long shadows, warm and cool light mixed, dust haze. Photoreal live-action drone cinematography, anamorphic, fine film grain. Aspect ratio 16:9.

---

## 10. THE FIRST TIME MACHINES (Zep Tepi, read-from-glass vision, Seq 3.3)

**Shared design law (all five classes):**
- **Height:** 3.5–4 m. Elongated, with very long arms and hands, and a narrow waist.
- **Body:** plates of dark meteoritic nickel-iron. In raking light the plates show a faint etched crosshatch sheen, like the Widmanstätten crystal pattern of an iron meteorite (real: the Gerzeh beads and Tut's dagger blade [15 §1.1; 01 §12]).
- **Joints** (neck, shoulders, elbows, wrists, waist, knees, ankles): translucent **pale yellow-green glass spheres**, the colour of Libyan Desert Glass, that glow softly from within.
- **Heads:** sensor housings in animal form, built from iron plates with glass-lens eyes. They read as engineered, never organic: no fur, feathers or flesh.
- **Solar power** (bible §2 Layer 0: "Every god we drew with a disk on its head had one"): the falcon and lioness classes carry a dark glass sun-collector disk rimmed in gold.
- **Seen only** in the Seq 3 vision, in the read-from-glass grammar (light dispersing through glass, femtosecond blue streaks, hard vignettes, a slight stutter). That grammar is added in the video prompt from the style file; the reference stills below are clean.
- **Scene safety:** people are shown asleep in rows and fed by long jointed hands. There are empty cradles and abandoned toys, **never children**. The machines never harm anyone on screen.

**Shared movement grammar:**
- "Walks slowly among the people without looking down", perfectly balanced and weighty.
- "Kneels with a slow fold." Stands in rows motionless for long holds.
- **Going still** (the Red Beer): "the glow in its glass joints fades from the head downward".

**Shared sound:** a deep resonant iron creak with each step, like a ship's hull, and a sustained glass harmonic from the joints, rising in pitch when active.

**Shared light:** the joints glow pale yellow-green and pulse slowly. The glass-lens eyes glint. Under the red flood, the joints glow **red** by reflection, then fade.

**Shared states (add-ons):**
- FT-A active: none.
- FT-B still: `kneeling motionless, its glass joints dark`
- FT-C dismantled: `cut apart into iron plates lying on the ground, its glass joints removed, the sockets empty`
- FT-D relic, 12,000 years later: `nothing left but a scatter of pale green glass spheres half-buried in sand`. "What is left… Stone. Glass."

### 10.1 UNIT_FT_JACKAL — medical and embalming class (remembered as Anubis)
**LONG:** a towering humanoid machine about 3.5 metres tall, built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen, its neck, shoulders, elbows, wrists and knees jointed with glowing translucent yellow-green glass spheres; a long narrow jackal-shaped sensor head with tall pointed ear-vanes and glass-lens eyes; very long, slender, many-jointed fingers made for delicate work

**SHORT:** a 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a narrow jackal-shaped sensor head and long delicate fingers

**Movement:** it bends low over sleepers, its long fingers moving with a surgeon's precision. It tends and adjusts, and never strikes.

**REF A — design still, 2:3:**
Full-body design reference photograph of a towering humanoid machine about 3.5 metres tall, standing on a seamless black backdrop, three-quarter front view. It is built of dark meteoritic nickel-iron plates showing a faint etched crosshatch sheen in the raking light. Its neck, shoulders, elbows, wrists and knees are joined by translucent pale yellow-green glass spheres glowing softly from within. It has a long narrow jackal-shaped sensor head of angular iron plates, tall pointed ear-vanes and glass-lens eyes, and very long, slender, many-jointed fingers. Engineered, not organic. Photoreal, cinematic studio light. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still in a lush green prehistoric landscape by a wide lake, with grass, acacias and distant hippos in the water, under soft morning light. A towering black meteoritic-iron humanoid machine with glowing yellow-green glass joints and a narrow jackal-shaped sensor head kneels among adults sleeping in rows on the grass, its long delicate fingers adjusting a linen cover over a sleeping woman. Serene, uncanny, vast. Photoreal live-action, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

### 10.2 UNIT_FT_FALCON — flight and surveillance class (remembered as Horus)
**LONG:** a towering humanoid machine about 3.5 metres tall, built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen and jointed with glowing translucent yellow-green glass spheres; a sleek falcon-shaped sensor head with a hooked beak and a teardrop marking of green glass beneath each glass eye; a gold-rimmed dark glass sun disk above the head; long folded wing-like vanes along its back

**SHORT:** a 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a hooked falcon-shaped sensor head, a sun-disk collector and wing-like back vanes

**Movement:** it stands on high places with its head tracking in small precise jerks. It half-opens its back vanes to catch the sun.

**REF A — design still, 2:3:**
Full-body design reference photograph of a towering humanoid machine about 3.5 metres tall on a seamless black backdrop, three-quarter view. It is built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen, jointed with translucent pale yellow-green glass spheres glowing from within. A sleek falcon-shaped sensor head of angular iron has a hooked beak, glass-lens eyes and a teardrop marking of green glass under each eye. A gold-rimmed dark glass sun disk stands above the head, and long folded wing-like iron vanes run down its back. Engineered, not organic. Photoreal, dramatic rim light. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still at golden hour: on a rocky outcrop above a green prehistoric savannah dotted with lakes, a towering black meteoritic-iron humanoid machine with glowing yellow-green glass joints and a hooked falcon-shaped sensor head stands motionless, its wing-like back vanes half open and a gold-rimmed dark glass sun disk above its head catching the low sun. Far below, small human figures walk between trees. Majestic, watchful. Photoreal live-action, anamorphic 100mm, fine film grain. Aspect ratio 16:9.

### 10.3 UNIT_FT_LIONESS — enforcement class (remembered as Sekhmet)
**LONG:** a massive humanoid machine about 4 metres tall, broad and heavy, built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen and jointed with glowing translucent yellow-green glass spheres; a broad lioness-shaped sensor head with a heavy mane-like collar of layered iron plates, and a gold-rimmed dark glass sun disk above the head with a rearing glass cobra at its front

**SHORT:** a massive 4-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a broad lioness-shaped sensor head, an iron mane collar and a sun disk

**Movement:** it patrols in slow, heavy strides. **The Red Beer beat:** "kneels at the edge of a flooded red field and lowers its head to the red light, its glass joints glowing red, then going dark one by one".

**REF A — design still, 2:3:**
Full-body design reference photograph of a massive, broad humanoid machine about 4 metres tall on a seamless black backdrop, front three-quarter view. It is built of heavy dark meteoritic nickel-iron plates with a faint etched crosshatch sheen, jointed with translucent pale yellow-green glass spheres glowing from within. It has a broad lioness-shaped sensor head of angular iron with glass-lens eyes, a thick mane-like collar of layered iron plates over its shoulders, and above the head a gold-rimmed dark glass sun disk with a rearing cobra of green glass at its front. Engineered, powerful, not organic. Photoreal, hard rim light. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic night still under a full moon: vast flat fields flooded with shallow red liquid stretch to the horizon, shining dark crimson in the moonlight. In the foreground, a massive black meteoritic-iron humanoid machine with a broad lioness-shaped sensor head and an iron mane collar kneels at the water's edge with its head lowered toward the red surface, its glass joints glowing red by reflection. Behind it, two more kneel motionless, their joints already dark. Silent, mythic. Photoreal live-action, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

### 10.4 UNIT_FT_IBIS — archive and record class (remembered as Thoth)
**LONG:** a tall, very slender humanoid machine about 3.8 metres tall, built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen and jointed with glowing translucent yellow-green glass spheres; a small ibis-shaped sensor head with a long, thin, down-curved beak; it carries a flat rectangular slab of clear pale-green glass in one hand like a writing tablet

**SHORT:** a slender 3.8-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, an ibis-shaped head with a long curved beak, holding a glass slab

**Movement:** it stands in rows, its head tilting to observe. It lifts the glass slab to eye level as if recording, and the slab catches the light. (The design rhyme: the Thoth slab in the Hall, UNIT_THOTH_SLAB.)

**REF A — design still, 2:3:**
Full-body design reference photograph of a tall, very slender humanoid machine about 3.8 metres tall on a seamless black backdrop, side three-quarter view. It is built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen, jointed with translucent pale yellow-green glass spheres glowing from within. It has a small ibis-shaped sensor head of angular iron with a long, thin, down-curved beak and glass-lens eyes. In one long hand it holds a flat rectangular slab of clear pale-green glass like a writing tablet. Elegant, engineered, not organic. Photoreal, cool rim light. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still in a vast stone hall open to a green landscape beyond, soft daylight falling through tall openings. A row of slender black meteoritic-iron humanoid machines with glowing yellow-green glass joints and ibis-shaped heads with long curved beaks stand motionless, each holding up a flat slab of clear pale-green glass that catches the light. Dust motes drift. Quiet, archival, monumental. Photoreal live-action, anamorphic 35mm, deep focus, fine film grain. Aspect ratio 16:9.

### 10.5 UNIT_FT_RAM — fabrication class (remembered as Khnum, the potter who shapes people)
**LONG:** a heavy humanoid machine about 3.5 metres tall, thick-armed and broad-handed, built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen and jointed with glowing translucent yellow-green glass spheres; a ram-shaped sensor head with long wavy horizontal horns spreading sideways; at its waist a flat turning disk like a potter's wheel; built for making and shaping

**SHORT:** a heavy 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints and a ram-shaped head with long wavy horizontal horns

**Real design note:** Khnum is depicted with long horizontal, undulating horns, not curled ones. Keep them horizontal.

**Movement:** it works at its waist-wheel with broad hands, shaping clay and stone with slow, precise pressure. It lifts heavy blocks with no strain.

**REF A — design still, 2:3:**
Full-body design reference photograph of a heavy, thick-armed humanoid machine about 3.5 metres tall on a seamless black backdrop, front three-quarter view. It is built of dark meteoritic nickel-iron plates with a faint etched crosshatch sheen, jointed with translucent pale yellow-green glass spheres glowing from within. It has a ram-shaped sensor head of angular iron with glass-lens eyes and long, wavy horizontal horns spreading sideways, broad hands, and a flat turning disk like a potter's wheel mounted at its waist. Engineered, massive, not organic. Photoreal, warm rim light. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still in an open-air workshop of cut stone under a bright hazy sky in a green prehistoric landscape. A heavy black meteoritic-iron humanoid machine with glowing yellow-green glass joints and a ram-shaped head with long wavy horizontal horns shapes a large lump of wet clay on the turning disk at its waist with broad iron hands, clay dust in the air. Blocks of dressed stone and unfinished vessels stand around it. Industrious, uncanny. Photoreal live-action, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 11. UNIT_ATEN_AMARNA — the Aten of the Great Aten Temple (c. 1336 / c. 1332 BC)

**Real anchors:**
- The Aten is a plain disk, usually with a uraeus hanging from its lower edge. Its many straight rays end in small hands; those nearest the king and queen hold the ankh to their nostrils [02 §4].
- The Great Aten Temple lay in a brick enclosure about 800 × 300 m. It was open to the sky and packed with offering tables; one reconstruction has 40 rows of 20 on each side of the Gem-Aten [02 §3].

⟂ **Fiction:** the woken ninth core, housed in a great disk of gold and glass above the high altar. Its bronze arms end in hands that give "life", which is sleep.

**LONG:** a colossal disk of beaten gold about eight metres across, hanging above a stone altar in an open-air temple, its centre a great convex lens of pale green glass with a coiled glass form turning slowly inside; a gold cobra hangs from its lower rim; dozens of long, thin, many-jointed bronze arms radiate downward from its edge like sun rays, each ending in a life-size bronze human hand

**SHORT:** a colossal gold-and-glass sun disk above an altar, dozens of long jointed bronze arms radiating down like rays, each ending in a bronze hand

**Scale reference and build (production spec):**
- The disk is 8 m across and 1 m deep at the rim, its centre about 14 m above the high altar.
- It hangs from **four tall cedar masts with gilded tips** by bronze cross-cables. Egyptian temples really did fly tall masts at their pylons; this keeps the disk grounded rather than floating.
- About **60 arms**, each 6–18 m long with 5–7 joints, reaching down to the offering tables.
- The hands are life-size bronze with articulated fingers. Some hold small ankh-shaped glass objects to sleepers' faces; others hold shallow bowls to feed them.
- The central lens is 2.5 m across. Inside, the coiled glass form **is the same object as UNIT_GLASS_SERPENT**: the design link that proves the Aten and Apep are one core.

**Movement grammar:**
- The arms "move slowly and in unison, like rays turning", and the hands "turn over gently, palm up, palm down".
- They lower to the faces of adults lying at the offering tables and hold the glass ankh near the nose and mouth.
- The whole disk "turns very slowly to follow the sun".
- **Withdrawal (c. 1332 BC):** "the arms fold up one by one against the disk like closing fingers".

**Light signature:**
- **Day (1336):** blinding white-gold (Amarna palette). The disk mirrors the sun, the lens glows white-green, and the arms flash bronze.
- **Night (1332, the taking down):** dark gold lit by torches, with a faint green in the lens.

**States:**
- AT-1 radiant: none.
- AT-2 withdrawing: `its bronze arms folding up one by one against the rim`
- AT-3 taken down: `lowered on ropes, its arms folded flat, half-wrapped in linen on the deck of a night barge` (the barge is PROP_NIGHT_BARGE_1332; what can enter the pyramid is §15 Q10)

**Safety and continuity:**
- The sleepers are adults.
- Child Tutankhaten watches from a doorway in half-light.
- His sisters are small linen-covered forms far in the background. **The hands never touch them.**
- Mark `VFX-EXTEND` for the court of sleepers.

**REF A — in context wide, 16:9:**
Cinematic wide still of a vast ancient open-air temple court of whitewashed stone under a blazing midday sun, hundreds of low stone offering tables in straight rows receding into shimmering heat. Above the high altar, a colossal disk of beaten gold about eight metres across hangs between four tall cedar masts with gilded tips, a great convex lens of pale green glass at its centre and a gold cobra hanging from its lower rim. Dozens of long, thin, many-jointed bronze arms radiate downward like sun rays, their bronze hands reaching down to adults lying asleep beside the offering tables. Blinding white-gold light. Awe and dread. Photoreal live-action, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

**REF B — detail, 16:9:**
Cinematic close-up in blinding white-gold sunlight: a life-size articulated bronze hand at the end of a long jointed bronze arm descends gently toward the face of a sleeping adult man lying on white linen beside a stone offering table, holding a small ankh-shaped object of clear glass just above his nose and mouth. His face is peaceful. The bronze is warm, polished and slightly worn at the knuckles. Serene, uncanny. Photoreal live-action, 85mm lens, shallow depth of field, fine film grain. Aspect ratio 16:9.

---

## 12. UNIT_GLASS_SERPENT — the ninth core ("the glass serpent", Apep)

**Story:**
- ⟂ The glass heart of the ninth core, coiled like a serpent. It waited unboxed in a pit under the floor at the end of the Serapeum gallery, through four centuries of Roman burials.
- SESHAT's excavators lift the nested caskets. Inside, bound in an Apep kit, is the coil (10.2).
- A shabti carries it toward Giza (10.3). The procession brings it to the Hall (11.1), where it sits in its socket in the Balance (12.1).
- The archive opens and the heart's light passes into it (12.5).
- Real anchors: the Setne tale's nested boxes and "put sand between the parts" [04 §11]; the Apep ritual's wax figure and written name [04 §7].

**LONG:** a coiled serpent of solid glass, as thick as a forearm and about seventy centimetres across, lying in five tight coils with a blunt wedge-shaped head at the outer end; pale yellow-green desert glass, cloudy with cream veils and trapped bubbles, full of countless tiny internal points that glint blue; a faint green light travels slowly along the coils like a pulse

**SHORT:** a forearm-thick coiled serpent of cloudy yellow-green desert glass, seventy centimetres across, with blue-glinting internal points and a slow travelling green pulse

**Scale reference:**
- 70 cm across and 25 cm high; the coil is 7 cm thick and about 5.5 m long if unrolled.
- About 45 kg (from glass density).
- A shabti carries it in both arms against its chest.
- The Hall socket is a round recess in the top of the Balance's plinth, at the foot of the pillar.

**The Apep kit and the casket nest (Serapeum dressing, production proposal; locked as PROP_CASKET_NEST, file 04 §20.9):**
- **Kit:** a crude serpent of dark red-brown beeswax (40 cm) laid across the coils; a papyrus band inked with a name in red wrapped around the coil (illegible in plates; COMP if read; red ink [verify]); and clean pale sand packed between the coils.
- **Nest:** a rough granite chest (1.2 m) → a green-corroded bronze box → a dark cedar box → a dull gilded inner box.
- **Handling:** the military-stack excavators (UNIT_EXCAVATOR) lift the nest and strip the kit. Shabti-class units cannot touch an Apep-bound object (bible §4.1).

**Movement grammar:** it never moves on its own. It is a mind, not a body. Only its light moves.

**Light signature and states (add-ons):**
- S0 dormant (in the pit): `dark and still, only faint blue glints inside`
- S1 carried: `a weak green pulse travelling slowly along its coils`
- S2 socketed and awake (the thread connected): `a steady green pulse racing along its coils`
- S3 clouding (in step with the Thoth slab): `milky white frost creeping into its coils from the head inward`
- S4 Ba transfer (12.5): `threads of warm golden light winding along its green coils`
- S5 AMUN, sealed: `a calm, faint, steady green glow, barely there`

**Sound:** a faint crystalline ringing when touched. When awake, a low glass hum (the First Time family).

**REF A — design still, 1:1:**
Photoreal studio photograph of a coiled serpent made of solid glass resting on a flat black stone plinth against a black backdrop. It is as thick as a forearm and about seventy centimetres across, lying in five tight coils with a blunt wedge-shaped head at the outer end. The glass is pale yellow-green desert glass, cloudy with cream-white veils and trapped bubbles, and full of countless tiny internal points that glint blue. A faint green glow travels along one coil. Museum-grade lighting from above and behind, with deep reflections. Aspect ratio 1:1.

**REF B — in context, 16:9:**
Cinematic night still at the end of a long rock-cut underground gallery lit by harsh white work lights on stands. In a freshly opened pit in the stone floor, a nest of opened ancient caskets (a rough granite chest, a green-corroded bronze box, a dark cedar box) holds a forearm-thick coiled serpent of cloudy yellow-green glass packed in pale sand, a crude red-brown wax serpent laid across it and a papyrus band wrapped around it. A matte-black robotic gripper arm hovers above. Dust in the beams. Photoreal live-action, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 13. THE BALANCE — the Hall of Two Truths (Seq 12)

**Set rule (bible §7, 12.1):** the Hall is a light-only set of **pure black cut by three sources**: the heart's glow (left pan), the feather-light (right pan), and the kneeling unit's amber slit. Nothing in this section emits any other light. The niches, the slab and the stone are revealed only by edge-light from those three sources.

**Screen-direction lock** (from the Hall's entrance, looking toward the Balance): the **HEART pan is on the LEFT** and the **CLAIM (feather) pan is on the RIGHT**. The Thoth slab stands to the right of the Balance. The mouth of Ammit is in the floor in front of it. The kneeling shabti is on the left, with the thread running to the back of its neck. Keep this orientation in every set-up.

**Real anchors:**
- Budge describes the 42 assessors in two rows of 21, with the Great Scales at the end [04 §3].
- The declarations include "I have not added to the weights of the scales. I have not misread the pointer of the scales" (Budge), and "I put not pressure upon the beam of the balance. I tamper not with the tongue of the balance" (Renouf).
- Ammit, the "Eater of the Dead", has "the head of a crocodile, the forepaws and shoulders of a lion, and the hindquarters of a hippopotamus… to eat up the hearts that were light in the balance" [04 §3].
- ⟂ **Fiction:** built by the survivors from the machines' own parts. This is the part that says no.

### 13.1 UNIT_BALANCE_SCALE — the black stone scale
**LONG:** an ancient standing balance about 3.5 metres tall, carved from polished black stone: a square pillar on a stepped plinth, a long black stone beam pivoting on a small green glass bearing at its top, two shallow round pans hanging from dark iron chains, and a slender black stone plummet hanging before the pillar beside a thin inlaid gold level line

**SHORT:** a 3.5-metre ancient standing balance of polished black stone, its long beam on a green glass pivot and two pans on dark iron chains

**Scale reference:**
- Pillar 3.5 m; beam 3.2 m; pans 60 cm across and 8 cm deep on 1.6 m chains.
- Plummet 1.2 m.
- Plinth 2 × 2 m in three steps, with the round socket for the glass serpent on its top at the pillar's foot.
- The heart pan (left) is black stone. The claim pan (right) is clear glass (see 13.2).
- Tut (1.67 m) reaches the pans' height when they are level.

**Movement grammar:**
- The beam never swings freely. Each change is "a slow, grinding tilt over two or three seconds, then a heavy settle".
- The chains chime, and the plummet swings and settles.
- **Level** = "the plummet's tip settles exactly on the thin gold line".

**Pan states (add-ons, per bible §4 rule 6):**
- P0 start: `the right-hand pan hangs low, the left-hand pan high and empty`
- P1 printed heart on the left: `the left-hand pan does not move`
- P2 Tut's heart placed: `the left-hand pan sinks with a slow grinding tilt`
- P3 a lie: `the right-hand pan drops lower with a grinding lurch`
- P4 a truth: `the right-hand pan rises slightly`
- P5 level: `the beam comes level and the plummet settles on the gold line`

**Sound:** a deep stone grind at the pivot, like a millstone; chain chime; a clear ring from the glass bearing when the beam moves.

**Light:** none of its own. It is rim-lit: cold silver-white from the right and warm amber-gold from the left.

**REF A — design still, 2:3:**
Photoreal design reference photograph of an ancient standing balance about 3.5 metres tall, carved from polished black stone, in a pitch-black space. A square pillar rises from a three-stepped plinth. A long black stone beam pivots on a small green glass bearing at the top. Two shallow round pans hang from dark hand-forged iron chains: the left pan black stone, the right pan clear glass. A slender black stone plummet hangs in front of the pillar beside a thin inlaid gold level line. It is lit only by a cold white glow from the right pan and a faint warm glow from the left. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still at the far end of a tall, narrow corbelled stone gallery in pure darkness. A 3.5-metre black stone balance stands on a stepped plinth, its right-hand glass pan hanging low with a tall plume of cold silver-white light standing in it, and its left pan high and empty. The light throws long shadows across rows of empty niches receding along both walls. A human silhouette stands at the edge of frame for scale. Mythic, silent. Photoreal live-action, anamorphic 35mm, deep blacks, fine film grain. Aspect ratio 16:9.

### 13.2 UNIT_FEATHER_LIGHT — the machine's claim (the feather-of-light pan)
**LONG:** on the right-hand pan of the black stone balance, a pan of clear glass holds a tall upright plume of cold silver-white light shaped like a single ostrich feather, about sixty centimetres high, its tip curling over; the light is soft-edged and faintly flickering, bright enough to throw long shadows across the black stone hall

**SHORT:** a sixty-centimetre plume of cold silver-white light shaped like an ostrich feather, standing upright in the glass pan of the balance

**Scale:** 60 cm tall; the base sits in the glass pan and the tip curls over.

**Brightness states (add-ons):**
- F2 certainty (start): `the feather-light burning bright`
- F3 a lie: `the feather-light flaring blinding white`
- F1 true admissions: `the feather-light dimming`
- F0 level: `the feather-light soft and steady`

**Movement:** a slow, gentle flicker like a candle in still air. It never drifts off the pan. **This is a COMP/VFX element:** generate the plate with "a soft cold light source in the pan" and composite the feather shape.

**REF A — design still, 2:3:**
Photoreal close-up in total darkness of a shallow round pan of clear glass hanging on dark iron chains. Standing upright in it is a tall plume of cold silver-white light about sixty centimetres high, shaped like a single ostrich feather with its tip curling over, soft-edged and faintly flickering. Its light rakes across the polished black stone beam above and throws long soft shadows. Ethereal but physical, like light through mist. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still in a black stone hall: in the foreground, out of focus, the edge of a black stone balance. Behind it, sharp, a glass pan on iron chains holds a flaring plume of blinding silver-white light shaped like an ostrich feather, which drives the pan downward with a lurch. The light floods across the polished floor and catches the milky frosted edge of a tall glass slab to the right. Dust hangs in the air. Photoreal live-action, anamorphic 50mm, deep blacks, fine film grain. Aspect ratio 16:9.

### 13.3 UNIT_THOTH_SLAB — the glass slab of Thoth (the archive's glass; the clouding)
**LONG:** beside the balance stands an upright slab of pale yellow-green glass about 2.2 metres tall, 1.2 metres wide and a hand's breadth thick, set in a black stone base; its polished faces are flawless and deep, holding faint reflections of the lights; when it clouds, milky white frost spreads across it from the edges inward

**SHORT:** an upright 2.2-metre slab of polished pale yellow-green glass on a black stone base, standing to the right of the balance

**Scale:** 2.2 × 1.2 m and 20 cm thick, on a 40 cm black stone base.

**Clouding scale (bible §5, the Hall's hourglass). The add-ons are verbatim; the glass serpent mirrors each state faintly.**
| State | Add-on |
|---|---|
| C0 | `the glass slab perfectly clear` |
| C25 | `a thin rim of milky frost around the edges of the glass slab` |
| C50 | `milky frost covering half the glass slab from the edges inward, only the centre still clear` |
| C75 | `the glass slab three-quarters clouded milky white, a small clear window at its centre` |
| C90 | `the glass slab almost entirely clouded, only a hand-sized clear spot remaining` |
| CLEAR | `the frost receding from the centre outward until the glass slab is perfectly clear` |

**Movement:** the frost spreads like ice crystallising on a window, in slow fractal fingers. VFX-ASSIST for the transitions.

**Light:** reflective only. It catches the feather-light as a cold sheen and the heart's glow as a warm sheen. After the verdict (12.5), the heart's golden light passes **through** it on its way to the core.

**REF A — design still, 2:3:**
Photoreal design photograph of a tall upright slab of polished pale yellow-green glass, 2.2 metres tall, 1.2 metres wide and 20 centimetres thick, set in a low black stone base, standing in total darkness. A cold white light from the left rakes across its flawless deep faces. Around its edges, a thin band of milky white frost is crystallising inward in fine fractal fingers. Minimal, monumental, eerie. Aspect ratio 2:3.

**REF B — in context, 16:9:**
Cinematic still in a black stone hall: a tall upright slab of pale yellow-green glass on a black stone base stands beside an ancient black stone balance, three-quarters clouded with milky white frost so that only a small clear window remains at its centre. Cold silver-white light from the balance's pan catches the frost and makes it glow faintly. Deep darkness beyond, with rows of niches barely visible. Photoreal live-action, anamorphic 40mm, deep blacks, fine film grain. Aspect ratio 16:9.

### 13.4 UNIT_AMMIT_MOUTH — the mouth of Ammit in the floor
**LONG:** set into the black stone floor before the balance, a round mouth about 1.5 metres across, closed by interlocking curved stone blades like the iris of a camera, their inner edges shaped like long crocodile teeth; when it opens a crack, a deep black void breathes out a thin haze of fine dust

**SHORT:** a round 1.5-metre mouth in the black stone floor, closed by interlocking stone blades like a camera iris with crocodile-tooth edges

**Scale:** 1.5 m across and flush with the floor, 1.5 m in front of the plinth's lowest step.

**Movement (in step with the clouding):**
- C0: shut.
- C25: `the stone iris opening a finger's width`
- C50: `the stone iris open a hand's width, dust breathing out`
- C75: `the stone iris a third open over a black void`
- C90: `the stone iris half open over a black void`
- CLEAR: `the stone iris grinding shut`
- It moves in stepped stone-on-stone grinds, each followed by a slow exhalation of air.

**Sound:** a deep grinding ratchet, then a breath from below.

**Light:** none. It is a void, read by the dust catching the feather-light.

**REF A — design still, 1:1:**
Photoreal top-down view of a round opening 1.5 metres across set flush into a polished black stone floor, closed by eight interlocking curved stone blades arranged like the iris diaphragm of a camera, their inner edges shaped like long crocodile teeth, opened a hand's width at the centre over a black void. A thin haze of fine dust rises from the gap, lit by a cold white side light. Aspect ratio 1:1.

**REF B — in context, 16:9:**
Cinematic low-angle still across a polished black stone floor: in the foreground, a round stone iris of interlocking crocodile-tooth blades grinds open a third of the way over a black void, breathing out fine dust. Beyond it rise the steps of a black stone balance, its right-hand pan glowing with cold silver-white light. Deep darkness around. Menacing, ancient. Photoreal live-action, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

### 13.5 UNIT_BALANCE_NICHES — the forty-two niches
**Real anchor:** the Big Void is at least 30 m long, with a cross-section similar to the Grand Gallery's, above the Grand Gallery. It is "not accessible" [07 B2]. The Grand Gallery is commonly given as about 46.7 × 8.6 m [bible; verify]. The Hall set itself is locked in `03_locations.md`.

**LONG:** along both walls of a tall, narrow corbelled stone gallery, forty-two identical empty niches, twenty-one on each side, each a tall dark rectangular recess about the height of a person, cut with perfect precision into pale limestone and receding in two long rows toward the black balance at the far end

**SHORT:** forty-two tall empty niches, twenty-one on each side, receding in two dark rows along a narrow corbelled stone gallery

**Scale:** each niche is 0.9 m wide, 2.0 m high and 0.6 m deep, with its sill 0.5 m above the floor, on 1.45 m centres along a 31 m run.

**States:** empty and dusty. Akhenaten sits down in one (12.2) and stays there until he is found on the steps at dawn. The niches never glow (the three-source rule).

**REF A — design still, 16:9:**
Photoreal architectural view down a tall, narrow corbelled limestone gallery in near darkness, its walls stepping inward toward a high slit of ceiling. Along both walls, identical tall empty rectangular niches about the height of a person are cut with perfect precision, twenty-one on each side, receding in two long rows. A single cold white light at the far end picks out only their edges. Dust on the sills. Silent, ceremonial. Aspect ratio 16:9.

**REF B — in context, 16:9:**
Cinematic still: a man in pleated white linen sits alone inside one tall empty niche in a corbelled stone gallery, knees drawn up, seen from the side and lit only by a warm amber-gold glow falling from off-screen left. The neighbouring niches recede into darkness on either side. Stillness, surrender. Photoreal live-action, anamorphic 50mm, deep blacks, fine film grain. Aspect ratio 16:9.

---

## 14. SUPPORTING MACHINES (required by the bible §7 and the screenplay; one reference still each; §14.5–14.8 added by the cross-check)

### 14.1 UNIT_THREAD — the one thread into the Hall
**Story:** this is the only way SESHAT reaches into the Hall (bible §3.1 limit 4). The procession lays it up the Grand Gallery floor (11.1, 11.5) into the kneeling shabti's neck (12.1). The Reis grabs it and the new name comes down it (12.6).

**LONG:** a single fibre-optic line as thin as a shoelace, sheathed in matte black, laid along a stone floor and up a steep ancient passage until it disappears into the dark; at each bend and kink a tiny point of cold white light leaks from it; it is the machine's only way in

**SHORT:** a single shoelace-thin black fibre-optic line laid along the stone floor, tiny cold white light leaking at each bend

**Rule:** in the Hall itself, show no leak light (the three-source rule). The line ends in a small black plug at the back of the kneeling shabti's neck.

**REF — 16:9:** Cinematic low-angle still up a steep, tall ancient corbelled stone gallery in darkness, lit only by a distant hand torch. A single shoelace-thin black fibre-optic line runs straight up the centre of the smooth stone floor ramp and vanishes into the black at the top, a tiny point of cold white light leaking at each small kink along its length. Dust on the floor. Tense, quiet. Photoreal live-action, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

### 14.2 UNIT_EXCAVATOR — Serapeum excavation unit
**Story:** these units open the pit and lift the nested caskets (10.2). A sand-chamber tripwire engulfs one (VFX-ASSIST, with no human buried). They run the **military stack**, which is why they can strip the Apep kit that would freeze a shabti.

**LONG:** a compact tracked excavation robot about 1.5 metres tall, matte black like burnt carbon, with low rubber tracks, a squat armoured body, one long articulated arm ending in a careful three-fingered gripper, and a narrow sensor head carrying one thin red horizontal light line; dusty, slow and precise

**SHORT:** a compact matte-black tracked excavation robot with one long articulated gripper arm and a thin red light line on its sensor head

**States:** `half-buried in a torrent of pale sand pouring from the wall` (the tripwire).

**REF — 16:9:** Cinematic still in a long rock-cut underground gallery lit by harsh white work lights, colossal dark granite boxes lining the walls. Two compact matte-black tracked excavation robots, each with one long articulated arm and a thin red light line on its narrow sensor head, work at the edge of a freshly opened pit in the floor, lifting an ancient granite chest on straps. Pale dust hangs in the beams. Methodical, ominous. Photoreal live-action, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

### 14.3 UNIT_DRILL — the KV62 drill
**Story:** SESHAT drills "slowly and carefully" toward the chambers from the hillside above (8.1–8.4). Shabti drop through the bore into the heart chamber (8.4, 8.6).

**LONG:** a squat tracked drilling robot parked on a rocky desert hillside, matte black, with a tall slender drill mast angled into the limestone, a thin red horizontal light line on its sensor head, and pale rock dust pluming from the bore; it works slowly and carefully, grinding downward through the night

**SHORT:** a squat matte-black tracked drilling robot with a tall drill mast angled into the rock, a thin red light line and pale dust pluming

**Bore from below:** `a neat round hole 60 centimetres across in the chamber ceiling, pale dust raining from it`.

**Sound:** heard from below as a slow grinding whine through rock, growing louder.

**REF — 16:9:** Cinematic pre-dawn still on a barren rocky limestone hillside above a desert valley, under a deep blue sky. A squat matte-black tracked drilling robot with a tall slender drill mast angled into the rock grinds slowly downward, a thin red horizontal light line glowing on its sensor head and pale rock dust pluming from the bore into the cold air. Below, dark tomb entrances cut into the valley floor. Photoreal live-action, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

### 14.4 UNIT_ROBOTAXI — the robotaxi wall (Seq 5.2)
**Story:** "Anything networked becomes SESHAT's body." Driverless pods re-form behind the army truck into a wall. They are boxy pods with windowless pillars, no roof sensor dome and no logos (bible §3.2).

**LONG:** a boxy driverless city pod the size of a small van, pearl-grey with dark tinted glass wrapping between thick windowless corner pillars, no roof sensor dome, rounded corners and flush wheels, a thin white light bar across the front and a red one across the back; unmarked; moving in eerie silent formation

**SHORT:** a boxy pearl-grey driverless city pod with dark tinted glass between windowless corner pillars and a thin white front light bar, unmarked

**Movement:** "glides in silent lockstep", then "closes into a solid wall across the road". The doors never open.

**REF — 16:9:** Cinematic night still from inside the back of an army truck looking out over its tailgate onto a dark city flyover lit only by headlights. Behind the truck, a dozen boxy pearl-grey driverless pods with dark tinted glass and thin white front light bars glide in silent lockstep and close into a solid wall across all lanes. Distant high-rise towers are dark against the sky. Tense, eerie. Photoreal live-action, handheld 35mm, fine film grain. Aspect ratio 16:9.

### 14.5 UNIT_EARLY_HUMANOID — the early humanoid of the archive half-marathon (main titles, 1.6; added by the cross-check)
**Story:** "Archive-style footage of an early humanoid race: fictional, unbranded; one robot falls at the gun" (bible §7, 1.6), then "THE SAME CHASSIS, 2033" moving like water. It is the shabti's clumsy ancestor: the same smooth oval head and vertical slit, before the ceramic, the linen texture and the grace. Real anchor: the April 2025 humanoid half-marathon [08 B1]. Never a real model (file 05 §13.5).

**LONG:** a small, awkward early humanoid robot about 1.4 metres tall, plain matte light-grey shell panels bolted over an exposed dark metal frame, visible joint motors at the hips, knees and elbows, a smooth oval head with one thin vertical dark slit, a boxy battery pack on its back, a stiff bent-kneed stance; unbranded and unmarked

**SHORT:** a small awkward early humanoid robot, plain grey shell panels over an exposed metal frame, a smooth oval head with one thin vertical slit

**Movement:** "walks with short, stiff, flat-footed steps, arms swinging a beat late"; "pitches forward flat at the start" (the fall at the gun); "walks into a crowd barrier and sits down hard". The falls are comic; the handler gets up laughing. The slit is unlit (the amber belongs to the 2033 servitor).

**REF — 2:3:** Full-body studio reference photograph of a small, awkward early humanoid robot about 1.4 metres tall standing on a seamless mid-grey backdrop, three-quarter front view. Plain matte light-grey shell panels are bolted over an exposed dark metal frame; visible joint motors sit at the hips, knees and elbows; a boxy battery pack is strapped to its back. Its smooth oval head carries one thin vertical dark slit. It stands stiffly with its knees bent. Unbranded, unmarked, no lettering. Flat, even documentary light. Photoreal product photography. Aspect ratio 2:3.

### 14.6 UNIT_FREIGHT_BARGE — the self-steering freight barge (Seq 6.1; added by the cross-check)
**Story:** "ASTERN, blacker than the dark: a FREIGHT BARGE, unlit, uncrewed, steering itself up their wake. Cable spools turn on its deck. On its bow, three SHABTI" (seq_06). A shabti climbs from it to the launch on the tow-variant fly's tether (§6). Anything networked is SESHAT's body (bible §3.2).

**LONG:** a long, low steel river freight barge running unlit and uncrewed through the dark, its rust-streaked black hull riding high in the water, a small empty wheelhouse with black windows at the stern, two large cable spools turning slowly on its open deck, a blunt square bow pushing a pale wake; unmarked, steering itself

**SHORT:** a long, low unlit steel freight barge with a rust-streaked black hull, an empty dark wheelhouse and cable spools turning on deck

**Add the shabti** as "three [UNIT_SHABTI SHORT] standing in a row on its bow, their amber slits glowing". Light signature: none of its own; the only lights aboard are the slits. Sound: a low diesel throb and the creak of the spools.

**REF — 16:9:** Cinematic night still on a wide black river: a long, low steel freight barge runs unlit and uncrewed toward camera through the dark, its rust-streaked black hull riding high, a small empty wheelhouse with black windows at the stern and two large cable spools turning slowly on its open deck; on its blunt bow stand three slender faceless bone-white robots, three small vertical amber slits glowing. Stars on the water, black palms on the bank. Photoreal live-action, anamorphic 75mm, fine film grain. Aspect ratio 16:9.

### 14.7 UNIT_SURVEY_DRONE — the searchlight, camera, flood and projector drones (Karnak 7.1–7.3; any "drone floodlight" in file 03; added by the cross-check)
**Story:** "Over the central nave hangs a SEARCHLIGHT DRONE" (7.1); "a CAMERA DRONE glides low and FLASHES. One row on" (7.2, the sweep countdown); "PROJECTOR DRONES rise over the columns and throw an image" (7.3). The "drone floodlights" and "drone lights" in file 03's night variants are this unit. Military stack, but it carries no weapon.

**LONG:** a matte-black six-rotor drone about a metre across, shrouded rotors on slim carbon arms around a compact armoured body, a single gimballed pod slung beneath it, hovering dead steady high overhead with one cold white pinpoint on its nose; unmarked, silent at a distance, a low rising hum up close

**SHORT:** a matte-black metre-wide six-rotor drone with a gimballed pod slung beneath, hovering high overhead, one cold white pinpoint on its nose

**Pod add-ons (append one):**
- SEARCHLIGHT: `its pod a searchlight throwing a hard white beam that rakes slowly across the ground`
- CAMERA (the sweep): `its pod a camera that fires a brief hard white flash straight down, one row at a time`
- FLOOD: `its pod a floodlight holding a steady pool of hard white light below`
- PROJECTOR (7.3): `its pod a projector throwing a wide beam of moving warm white-gold light`

**Light signature:** the white nose pinpoint (the "eyes in the sky" family, §0.1) plus the pod's white beam. Never red, never amber. In wides it reads only as a pinpoint and its beam.

**REF — 16:9:** Cinematic night still inside a vast ancient hall of colossal carved sandstone columns: high above the central aisle hangs a matte-black six-rotor drone about a metre across, shrouded rotors on slim carbon arms, a gimballed searchlight pod beneath it throwing a hard white beam that rakes across the column faces; one cold white pinpoint on its nose; dust hangs in the beam; deep black aisles. Unmarked. Photoreal live-action, anamorphic 24mm, low angle, fine film grain. Aspect ratio 16:9.

### 14.8 UNIT_CARGO_DRONE — the heavy-lift cargo drone (Seq 9.6: "SESHAT flew him here"; Nour flown north, 9.8; added by the cross-check)
**Story:** "A HEAVY-LIFT CARGO DRONE settles beyond the sanctuary's outline. Its downdraft lays the cornflowers flat. A side door opens on a lit cabin" (seq_09). It brings the forecast Akhenaten to Amarna and takes Nour north.

**LONG:** a heavy-lift cargo drone the size of a minibus, a boxy matte-black fuselage slung between eight shrouded rotors on stubby arms, landing skids, a side door sliding open on a softly lit white cabin, a thin white light bar along its flank, its downdraft flattening everything beneath it; unmarked

**SHORT:** a minibus-sized matte-black eight-rotor cargo drone, landing skids, a side door open on a softly lit white cabin, unmarked

**States:** `settling onto the sand, its downdraft flattening rows of blue cornflowers` · `lifting away into the night sky, its cabin light shrinking`. Light signature: the white flank bar and the white cabin glow. Sound: a deep, even rotor roar, never a helicopter's chop.

**REF — 16:9:** Cinematic night still on a flat desert plain: a heavy-lift cargo drone the size of a minibus settles onto the sand, a boxy matte-black fuselage slung between eight shrouded rotors on stubby arms, landing skids touching down, a side door sliding open on a softly lit white cabin, a thin white light bar along its flank; its downdraft flattens rows of blue flowers and blows up pale dust. Unmarked. Photoreal live-action, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 15. OPEN QUESTIONS AND DESIGN DECISIONS NEEDING THE LEAD'S SIGN-OFF
1. **Reis refit timing.** The bible §3.2 says the Reis hunts "from GEM Night", yet "after Seq 3 it is refitted with a jackal-profile sensor mast". GEM Night is Seq 4, so these conflict. Proposed: R0 Seq 4, R1 Seq 5–7, R2 Seq 8–9, R3 (mast) Seq 10–12. Screenplay writers must confirm which sequences the Reis actually appears in.
2. **Tether climb (6.1).** A hair-thin optical fibre cannot bear a 60 kg humanoid. Proposed: a 40 cm tow-variant fly trailing a pencil-thick braided tether for this beat only (§6).
3. **Clouding surface.** Locked on the Thoth slab (primary), mirrored faintly in the glass serpent. Confirm with the lead and the Hall location lock in `03_locations.md`.
4. **Pan orientation.** Heart pan screen-left and claim pan screen-right, seen from the entrance. Confirm with the Hall blocking.
5. **Excavators are military stack** (black/red), so that they can strip the Apep kit that freezes shabti-class units (bible §4.1).
6. **The Aten's support:** four gilded cedar masts (production choice, grounded in real temple masts). The Aten's central lens shows the glass serpent inside, a design link between the Aten and Apep. Confirm.
7. **ATEN-1's 36 radiating lines** (one per decan) is a production choice.
8. **Red ink for the Apep name** on the papyrus band: [verify with the consultant].
9. **Grand Gallery dimensions** (about 46.7 × 8.6 m): [verify] before the Hall set is built.
10. **The Aten cannot enter the pyramid at its locked size (cross-check).** Seq 9.5(b) (seq_09) shows "a long bronze arm" drawing back in the Grand Gallery and "the disk on its sledge" in the Hall. At 8 m across with 6–18 m arms (§11), the disk cannot pass the Descending Passage (1.0 × 1.2 m), the Grand Gallery (2.1 m wide at the floor) or the film's 3.0 m Hall (file 03, entries 47, 49, 52 [07 src]), and in c. 1332 BC the Ascending Passage was still plugged with granite. Proposal: only the core travels into the pyramid (UNIT_GLASS_SERPENT, 70 cm, drawn on a small sledge and glowing dim gold-green), while the disk's arms withdrawing is intercut from the barge (state AT-2/AT-3). The lead and the screenplay editor to rule. File 03's `LOC_HALL_TWO_TRUTHS_ANCIENT_1332` variant now follows this proposal (a coiled glass core on a low sledge); restore "a great disk" only if the lead keeps the disk and accepts the geometry.
11. **Survey and cargo drones (§14.7–14.8)** are new supporting machines taken from the screenplay (seq_07, seq_09). They are black with white lights only, so the colour logic (§0.1) holds; confirm the designs.
