# 05 — STYLE GUIDE AND PROMPT GRAMMAR: suffix, negatives, grades, camera, flags, safety, dialogue, workflow

HERE AM I · Production Bible · file 05 of 05 · photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s, stitched in the edit.
**Authority:** story bible v3 (`drafts/02_STORY_BIBLE_LOCKED.md`, esp. §3.3–3.4, §5, §11, §13, §14), the lead's rulings (`drafts/04_CRITIQUE_DECISIONS.md`) and the shot spec (`drafts/03b_SHOT_PROMPT_SPEC.md`). The look-locks live in files 01 (characters), 02 (units and machines), 03 (locations) and 04 (props). This file supplies the grammar that binds them. Order of precedence: bible → critique decisions → files 01–04 → this file → the shot writer. Where this file bends the 03b spec, it says so and the point is listed in §14 for the lead.

---

## 0. HOW TO USE THIS FILE

1. **Fixed wording in this file** (paste verbatim; never paraphrase, reorder or "improve"):
   - the GLOBAL STYLE SUFFIX (§1.1), appended to every video prompt as step 7;
   - the COMPACT SUFFIX (§1.2), used only in the derived motion prompt (§5.5);
   - the GLOBAL NEGATIVE PROMPT (§2.1) and its add-ons (§2.2);
   - the GRADE prompt phrases (§3.2);
   - the lens, shot-type and camera-move phrases (§4.1–4.3);
   - the speaking and language phrases (§9.4).
2. **Tokens defined here:** `GRADE_*` (era and scene grades, used at the end of every lighting variant in file 03) and `NEG_*` (negative add-ons).
3. **Every shot entry** follows 03b's format. The PROMPT runs in 03b's seven-step order (§5.1); the NEGATIVE starts with §2.1; the flags come from §6; safety staging follows §7; dialogue follows §9.
4. **The one-line version of the whole file:** identity comes from approved images, not words. Words carry the action, the light and the continuity state; the reference stills and composed first frames carry the faces, costumes and sets (bible §14.1).

---

## 1. THE GLOBAL STYLE SUFFIX

### 1.1 The suffix (paste verbatim as PROMPT step 7, the last sentence of every video prompt)

> Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.

(77 words, 540 characters.)

**What each clause does** (so nobody "improves" it):

| Clause | Why it is there |
|---|---|
| *Photorealistic live-action feature film footage* | pulls every model away from CG, animation and game looks |
| *real human actors wherever people appear* | asks for actors, but "wherever people appear" stops models adding people to empty plates and robot-only shots |
| *natural skin texture with visible pores and fine imperfections* | defeats the waxy AI-skin default; protects dark and olive skin from smoothing |
| *faces, costumes and sets matching the reference images* | tells image-to-video tools to hold the composed first frame and the attached stills |
| *real physical locations lit by practical, motivated light sources* | every shot names its key light (bible §11); this clause stops invented rim lights and gels |
| *large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff* | the film's lens character, stated generically (no maker names) |
| *1920x1080, 16:9 full frame with no letterbox bars* | the delivery format. The word "anamorphic" makes some models add 2.39:1 bars, so the suffix forbids them |
| *24 frames per second with natural motion blur* | cinema cadence; discourages the smeary 30 fps "video" look |
| *fine organic film grain* | one consistent texture; the final grain is re-applied in post (§12 step 7) |
| *restrained cinematic colour grade* | deliberately neutral, so that the era grade (§3) sits on top of it |

### 1.2 The COMPACT SUFFIX (only for the derived motion prompt, §5.5)

> Photoreal live-action film, real human actors, natural skin texture, matching the reference images, large-format digital cinema camera, anamorphic lens, 1920x1080, 16:9, no letterbox, 24 fps, natural motion blur, fine film grain, cinematic grade.

(33 words, 246 characters.) Never use it in the shot entry's PROMPT field. That field always carries §1.1.

### 1.3 Stills are different
- **Character, unit and prop reference stills** use the templates and the "Common still negative" in file 01 §0.7 and the REF prompts in files 02 and 04.
- **Location plates** use the plate prompts in file 03, which end "Photoreal live-action film still, anamorphic NNmm, fine film grain. Aspect ratio 16:9."
- **Never append the video suffix to a still prompt.** Its frame-rate and motion-blur clauses degrade stills.
- **Composed first frames** (§12 step 4) are image edits of approved stills, not new text-to-image generations.

---

## 2. THE GLOBAL NEGATIVE PROMPT

### 2.1 Fixed (every shot's NEGATIVE starts with this)

> cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening

(125 words.) Every term is safe for every shot in the film: nothing here fights a period look or a story beat. Period-, place- and subject-specific exclusions live in the add-ons below.

### 2.2 Add-ons (fixed wording; append after §2.1 when the shot matches)

| Token | Append when | Text |
|---|---|---|
| `NEG_MODERN_EGYPT` | any 2033 shot set in Egypt (interior or exterior) | sepia desert filter, yellow colour cast, orientalist bazaar, fez, snake charmer, belly dancer, camels in city streets, old-Hollywood Egypt, Arabian Nights styling, readable Arabic signage |
| `NEG_UNITS` | any shot with a SESHAT unit (files 02 §1–7) | robot with a face, eyes or mouth, human skin on a robot, chrome robot, glossy consumer plastic, yellow or hazard-striped robot, numbers or logos on a robot, boxy commercial robot dog, white consumer camera drone, sparks and cables spilling like blood, robot posing or growling |
| `NEG_PERIOD` | 1323 BC, c. 1336–1330 BC, the First Time | modern objects, electric light, plastic, glass windows, wristwatches, eyeglasses, zippers, modern clothing, modern haircuts, tattoos, printed fabric, striped royal headcloth, gold funerary mask, Hollywood epic costume, heavy black eyeliner, pyramids on the horizon |
| `NEG_1925` | KV15, 1925 (and the 1939 flourish) | modern objects, plastic, LED light, digital cameras, modern clothing, sunglasses, clean modern surfaces, bright saturated colour |
| `NEG_REMAINS` | 1.1, 1.3, 1.5, 12.7 and the coda; any shot near the body or the heart | exposed body, bare skin of a preserved body, desiccated face, skull, bones, incision, surgery, organ, bandage-wrapped horror figure, zombie, horror-film lighting |
| `NEG_GARDEN` | any shot of Garden sleepers | children, babies, infants, medical tubes, drips, restraints, distressed faces, bodies in disorder, body bags, robots touching faces |
| `NEG_CHILD` | any shot with Layla or the child king | robot within reach of the child, robot touching the child, medical equipment, child in danger, frightened child |
| `NEG_HALL` | every shot inside the Hall of Two Truths (Seq 12; the 9.5b memory) | torches, lamps, candles, glowing screens, daylight, fill light, coloured gels, wall paintings, carved inscriptions, decoration |
| `NEG_WATER` | the Osiris Shaft flood (11.3) | face underwater, drowning struggle, open mouth underwater, bubbles from a mouth, panic close-up |
| `NEG_PLATE` | empty location plates and establishing shots with no characters | people, figures, crowds, vehicles, animals |

The unit "Never" lists (file 02) and the character negatives (file 01) are appended after these add-ons.

### 2.3 Rules
- **Order of the NEGATIVE field:** §2.1 → matching add-ons → character negatives (file 01) → shot-specific terms.
- **Never turn a negative into "no X" inside the positive prompt.** Many video models read the noun and render it. The only exceptions are tested phrases inside the fixed locks ("no lettering", "unmarked", "with no people" in plates); keep those as written.
- **Tools with no negative field:** drop the NEGATIVE at generation time, rely on the positive wording, and reject failing takes at QC (§12 step 5). Do not paste negatives into the positive prompt.
- **Never negate what the shot needs.** For example, NEG_MODERN_EGYPT's "sepia" ban is for 2033 only; the 1925 scene needs sepia (GRADE_1925).

---

## 3. ERA AND SCENE GRADES

Every lighting variant in file 03 ends "+ GRADE_x". The colourist applies the grade in post as a scene LUT plus trims. **The prompt phrase is optional**: add it in step 5, after the variant phrase, when the variant alone does not hold the look or a tool drifts. Never put two grades' phrases in one prompt. GRADE_READ_FROM_GLASS is post-only and has no prompt phrase.

### 3.1 Grade map

| Token | Era / scene | Bible palette (§11) | Used by (file 03 variants) |
|---|---|---|---|
| GRADE_1323 | Thebes, c. 1323 BC (1.1–1.2) | lamplight amber and lapis | LOC_EMBALMING_1323, LOC_KV62_BURIAL_1323 |
| GRADE_1336 | Amarna, c. 1336 and c. 1330 BC (9.5a, 9.5c) | blinding white-gold | LOC_AMARNA_TEMPLE_1336 NOON_1336, DAY_1330 |
| GRADE_1332_NIGHT | the night of the first Weighing, c. 1332 BC (9.5b) | (derived from 1323; flame against night) | NIGHT_1332; LOC_NILE/ANCIENT_1332; Grand Gallery and Hall ANCIENT_1332 |
| GRADE_1925 | KV15, 11 Nov 1925 (1.3) | sepia silver-gelatin | LOC_KV15_LAB_1925 |
| GRADE_1939 | the candlelit broadcast (inside 4.2) | candlelit monochrome-warm | LOC_CAIRO_MUSEUM_1939 |
| GRADE_1968 | the Liverpool X-ray room (1.4) | cold fluorescent | LOC_XRAY_1968 |
| GRADE_2033_MUSEUM | GEM interiors, labs, clinical 2033 | museum white, cool LED | LOC_GEM_*, LOC_DEWAR_VAULT, titles interiors |
| GRADE_2033_DAY | modern Egypt and the world by day | neutral-to-cool; never a desert filter | flyover day, Nile day, Valley glare, rail yard, hospital, hearing room |
| GRADE_GARDEN | the Garden (atrium, Amarna 2033, warehouse, stadium) | soft white | Garden variants |
| GRADE_NIGHT_ACTION | the blackout nights, Act II–III exteriors | sodium orange + drone white; "the blackout is the look" | most night exteriors |
| GRADE_UNDERGROUND | torch-lit stone (KV62 corridors, Serapeum, shafts, the pyramid) | (motivated torches) | TORCH variants |
| GRADE_GOLDEN | sunset (Saqqara, the quarry) | — | SUNSET variants |
| GRADE_DAWN_0614 | the final dawn, Giza, 8 Nov (12.7) | — | LOC_GP_NORTH_FACE_DAWN_0614 |
| GRADE_HALL | the Hall of Two Truths (12) | black + three sources ("black + heart green") | LOC_HALL_TWO_TRUTHS_THREE_SOURCE |
| GRADE_FIRST_TIME | the First Time vision (3.3) | — (read-from-glass) | LOC_FIRST_TIME_MORNING |
| GRADE_READ_FROM_GLASS | post-only overlay (3.3, 9.5) | "light dispersing through glass, femtosecond blue streaks, hard vignettes, a slight stutter" | all memory and vision variants |
| GRADE_ARCHIVE_2025 | the main-title half-marathon (1.6) | — | LOC_ROBOT_HALF_MARATHON_ARCHIVE |

### 3.2 Grade specs

Hex values are colourist targets, not prompt words. Unit and body light colours come from file 02 §0.1 and file 01 (chest glow) and are protected in every grade (§3.3).

**GRADE_1323: Thebes, lamplight amber and lapis**
- Prompt phrase: `warm amber oil-lamp light on skin and linen, deep lapis-blue shadows, a soft haze of lamp smoke, low-key and intimate`
- Colourist: flame key of about 2,000–2,400 K. Shadows pushed toward lapis (about #1F2E6E), never neutral grey. Skin midtones held natural olive-brown. Blacks lifted slightly into blue, never crushed. Soft highlight roll-off with halation on flames. Moderate saturation, amber and blue only. Medium grain.
- Never: the teal-and-orange blockbuster look, green shadows, gold everywhere.

**GRADE_1336: Amarna, blinding white-gold**
- Prompt phrase: `blinding white-gold sunlight, highlights blooming into white, pale gold stone, short hard shadows, airy lifted shadows, low saturation except the blue of flowers`
- Colourist: highlights overexposed by 1–1.5 stops with a soft shoulder and tinted white-gold (about #FFF1CF). Shadows lifted warm (about #6B5A3E), never black. Saturation 60–70%, except cornflower and lotus blue. Strong bloom. Always combined with GRADE_READ_FROM_GLASS. The Royal Road (DAY_1330) is the same grade with the bloom halved: the glare "gone flat and tired".
- Never: a saturated blue sky, crisp modern contrast.

**GRADE_1332_NIGHT: the night of the first Weighing**
- Prompt phrase: `a single warm flame against deep blue-black night, gold light climbing pale stone, smoky and hushed`
- Colourist: GRADE_1323, colder and harder. Flame at about 1,900–2,200 K, shadows blue-black (about #0E1430), small highlights. Always with GRADE_READ_FROM_GLASS.

**GRADE_1925: KV15, sepia silver-gelatin**
- Prompt phrase (optional): `the look of a 1920s silver-gelatin photograph in motion: warm sepia monochrome, rich blacks, soft highlight roll-off, heavy fine grain`
- Colourist: **preferred method** is to generate in natural colour under the period lighting (faces and textures hold better), then in post desaturate to 0–5% and tone shadows about #3B2716, mids about #8A6A45 and highlights about #EADBC0. Slight glow, mild edge falloff, heavy fine grain. This is a live scene, not archive: no scratches and no gate weave. The flash frames are pure white (§13.6).
- Never: colour bleeding through, modern contrast.

**GRADE_1939: the candlelit broadcast**
- Prompt phrase: `candlelight only, near-monochrome warm amber tones, faces floating out of deep black, like a 1930s newsreel warmed by flame`
- Colourist: saturation 20–30%, a warm tint (mids about #C88A4A), blacks crushed but holding detail, halation on flames, medium-heavy grain.

**GRADE_1968: the X-ray room**
- Prompt phrase: `cold flickering fluorescent light, a pale green-grey cast, flat institutional contrast, 16mm-style grain`
- Colourist: mids toward about #B7C4AE, highlights faintly green, blacks lifted grey-green, saturation about 50%, coarse 16 mm grain. The lightboxes clip to flat white.

**GRADE_2033_MUSEUM: museum white, cool LED**
- Prompt phrase: `clean cool-white LED light, precise and even, true neutral whites, polished reflections, crisp and quiet`
- Colourist: white point read as 5,600–6,500 K, with neutral whites, clean blacks and natural saturation. **Protect skin:** key brown and olive skin separately so the cool light never greys it (Tut, Nour, Adaeze, Fathi above all). Gentle highlight roll-off on glass.
- Never: a teal cast on skin, hospital green.

**GRADE_2033_DAY: modern Egypt and the world by day**
- Prompt phrase: `neutral-to-cool daylight, clear air, true colours, crisp distance, no yellow or sepia cast`
- Colourist: a neutral grey balance, the sky blue-grey, natural haze and true greens in the Nile valley. Never push yellow. This is the bible's "modern megacity" look: flyovers, towers, the GEM.
- Never: the orange-teal "desert filter" (bible §11).

**GRADE_GARDEN: soft white**
- Prompt phrase: `soft, shadowless white light as if diffused through white fabric, pale and calm, low contrast, gentle and eerie`
- Colourist: blacks lifted to about 8–10%, contrast compressed, saturation about 60% leaning faintly cool-white, creamy highlights (about #F4F6F2). Skin stays natural but pale-lit. Cornflower blue is kept.

**GRADE_NIGHT_ACTION: sodium orange + drone white**
- Prompt phrase: `night lit only by motivated sources: sodium-orange street light where any remains, hard cold-white drone floods, headlights and torches; deep blacks, faces readable`
- Colourist: two practical colours only: sodium (about #FF9A3C, desaturated, a broad soft wash) and cold white (about #E6EEFF). In the full blackout, add a very low cool starlight fill (about #0B1220). Blacks are deep with shadow detail. **Faces must read:** lift deep-brown skin by ⅓ to ⅔ of a stop with a motivated soft key in comp where the plate falls short. Unit lights stay small, crisp and saturated. The sodium wash must never drift toward the amber slit's hue: sodium is broad and soft, the slit a small, crisp, saturated point.
- Never: day-for-night blue, a moonlit wash (Act II nights have no moon in frame; file 03 §0.1), neon.

**GRADE_UNDERGROUND: torch-lit stone**
- Prompt phrase: `lit only by head torches and handheld torches: hard white beams, dust hanging in the beams, steep falloff to black, stone in its true colour`
- Colourist: beams slightly cool (read as 5,500–6,000 K). Stone in its true colour: cream limestone, grey-pink granite. Deep blacks and glowing dust. Unit lights saturated. From Seq 8.5 the chest glow (G1) is the only warm source.

**GRADE_GOLDEN: sunset**
- Prompt phrase: `a low golden sun, deep orange-gold light on stone, long blue shadows`
- Colourist: warm highlights (about #FFB060), cool shadows (about #2A3B5C), saturation +10%.

**GRADE_DAWN_0614: the final dawn**
- Prompt phrase: `first sunlight breaking over the horizon, pale gold light on stone, soft blue shadows, clean luminous air, stillness`
- Colourist: the scene ramps from pre-dawn blue (shadows about #1C2A4A) to gold at 06:14 (sun highlights about #FFD48A). Each of the four held states (file 01, desiccation) grades a little warmer than the last. The sun disc is COMP. The north face itself stays in blue shadow (file 03, entry 53).

**GRADE_HALL: black + three sources**
- Prompt phrase: `pure black darkness cut by three light sources only, deep inky blacks, stone read by rim light alone`
- Colourist: a true black floor (0–2%) with detail from rim light only. Three hues only: the heart (about #FFB84D with a #C9D46A cast, the bible's "heart green-gold"), the feather (about #E8F0FF) and the slit (about #FFA93A). The clouding glass reads milky (about #DDE3E0). The glass serpent's green pulse (about #B5E36A) stays below 30% of the heart's brightness.
- Never: lifted blacks, fill light, gels, any fourth hue.

**GRADE_FIRST_TIME: the First Time**
- Prompt phrase: `lush humid green-gold light, saturated greens, soft haze over water`
- Colourist: saturated greens (about #6FA84A), warm highlights, haze. Always with GRADE_READ_FROM_GLASS. The night beats (MOON_RED) keep the crimson of the fields as the only saturated hue.

**GRADE_READ_FROM_GLASS: post-only overlay** (bible §11: "light dispersing through glass, femtosecond blue streaks, hard vignettes, a slight stutter")
- **Plates and clips are generated clean.** There is no prompt phrase.
- Recipe:
  1. **Dispersion:** chromatic splitting on highlights (2–4 px RGB offset, prism-like fringes).
  2. **Femtosecond streaks:** thin cobalt horizontal streaks (about #3A6BFF) sweeping across the frame in 2–6 frames, 1–3 per second.
  3. **Hard vignette:** an oval falling to near-black over the outer 15–20% of the frame.
  4. **Stutter:** hold one frame and drop one frame every 1–2 s. Each "Stutter." in the screenplay is a hard cut with a 2-frame hold and a blue streak across the cut.
  5. **Glass texture:** a faint overlay of internal bubbles and seeds at 5–10%.
- The painted lure (§13.2) uses steps 1–3 only.

**GRADE_ARCHIVE_2025: the main-title half-marathon**
- Prompt phrase: `the look of 2020s handheld documentary news video shot on a long lens: flat bright overcast light, slightly soft, digital sharpening`
- Post: strip the film grain and add video noise; soften (downscale 50% and back up); add mild compression blocking, slight over-sharpening halos, a flat Rec. 709 look and handheld micro-shake. The cut to "THE SAME CHASSIS, 2033" snaps back to the full film look.

### 3.3 Protections that apply under every grade
- **Skin:** key skin separately in every scene and hold the hue and density of brown and olive skin. No grade may grey or flatten it.
- **Unit and body lights keep their meaning** (file 02 §0.1): amber #FFA93A = servitor; red #FF2B1C = military stack; white pinpoint #F2F6FF = flies; yellow-green #B5E36A = glass minds; warm amber-gold #FFB84D / #E7C45A = a heart that has lived; cold silver-white #E8F0FF = the machine's claim. Isolate them with keys before the scene grade, and never let a grade shift them.
- **Grain:** strip the generated grain before upscaling, and add one grain pass per era in the final (§12 steps 6–7). This is how clips from different tools and takes end up with the same texture.

---

## 4. CAMERA LANGUAGE

### 4.1 Lens kit (fixed phrases for step 1)

| Phrase | Use | Never |
|---|---|---|
| `anamorphic 24mm lens` | tombs, corridors, passages, low-angle scale (Karnak, the Grand Gallery), interiors under 4 m wide | for faces closer than a medium shot (distortion) |
| `anamorphic 32mm lens` | rooms and labs, GEM interiors, masters | — |
| `anamorphic 35mm lens` | exterior wides with people (the Amarna Garden, the Serapeum gallery), establishing shots | — |
| `anamorphic 40mm lens` | the film's "normal": walking mediums, two-shots, the quay | — |
| `anamorphic 50mm lens` | mediums and singles; units in context | — |
| `anamorphic 75mm lens` | close-ups, lip-reading singles, river long views, the dawn roof | — |
| `anamorphic 100mm lens` | tight close-ups: eyes, mouths for lip-reading, glass reflections | — |
| `anamorphic 135mm lens` | long-lens compression: the rail-yard hide-and-seek, the Giza fortress, the desert road | — |
| `18mm spherical lens` | the Well Shaft and the crawlway only | anywhere else |
| `100mm macro lens` | inserts: seams, the copper pins, the vessel, the scarab keyring, hands on the block | — |
| `long zoom lens, documentary style` | the 2025 archive only (1.6) | anywhere else |

Reference stills use the 85 mm and 50 mm portrait settings in file 01. Never: fisheye, tilt-shift miniature, extreme telephoto beyond 135 mm.

### 4.2 Shot types (fixed phrases)
`Extreme wide establishing shot` · `Wide shot` · `Full shot` · `Medium wide shot` · `Medium shot` · `Medium close-up` · `Close-up` · `Extreme close-up` · `Insert` · `Over-the-shoulder shot` · `Two-shot` · `Point-of-view shot` · `Top-down shot` · `Aerial shot`. Add `low-angle` or `high-angle` after the type when needed.
- **Aerials are SESHAT's eye.** Use them only where a drone could be in 2033 (the plateau, the city, the stadium, ATEN-1). Never use them in a period scene.

### 4.3 Camera moves (fixed phrases; **one move per clip**)
`locked-off` · `slow push-in` · `slow pull-back` · `lateral tracking left` / `lateral tracking right` · `the camera backs away ahead of…` · `the camera follows behind…` · `slow crane up` · `slow tilt up` / `slow tilt down` · `slow pan left` / `slow pan right` · `slow orbit of no more than thirty degrees` · `rack focus from … to …` · `subtle handheld` · `urgent handheld` · `vehicle-mounted`.
- Speed words: `slowly`, `at walking pace`, `at running pace`.
- **Avoid** (they break or look synthetic): whip pans, crash zooms, 360° orbits, dolly zooms, speed ramps (do these in post), and "drone shot" over period scenes.

### 4.4 Camera language per act

| Part | Seq | Look of the camera | Lenses | Moves | Signature rule |
|---|---|---|---|---|---|
| Prologue: the heart | 1.1–1.4 | still, painterly tableaux; the camera watches faces and hands, not the act | 32–50; 75–100 for hands | locked-off; slow push-ins | The centre of the table is never the subject. In 1925 the framings are tripod-height and static, like the photographer's. |
| The resurrection | 1.5 | clinical symmetry; one top-down on the cradle | 32, 50, 100 | locked-off; one slow push-in to the eyes | The first frame of 2033 matches the last of 1925 (§13.6). |
| Act I: the museum | 1.5–4.2 | composed, symmetrical, museum geometry, glass and reflections; one-point perspective in the tunnel | 32, 40; 75–100 for lip-reading | slider and dolly moves, slow pushes, locked-off wides | **No handheld until the breaker (3.6) and the blackout (4.2).** Order becomes disorder in a single cut. |
| GEM Night after the blackout | 4.2–4.4 | handheld arrives with the emergency light | 24–40 | subtle, then urgent, handheld | Each new space opens with a geography wide. |
| Act IIA: upriver | 5–7 | handheld human point of view; vehicle mounts; long lenses on the black river; Karnak from below | 24 (Karnak low angles), 40, 75–135 (river) | handheld; vehicle-mounted; lateral tracks between the columns | The river runs south = frame right (file 03). Every night shot names its key light. |
| Act IIB: the heart | 8–9 | claustrophobic underground; daylight suspense by long lens; the train's speed; Amarna's serenity | 24–32 underground; 135 in the rail yard; 50 on the train; 35 in the Garden | close handheld underground; locked-off long lens in the yard; vehicle-mounted; slow lateral tracks along the Garden rows | The memories (9.5) are locked-off, read-from-glass in post. |
| Act III: the twelve hours | 10–11 | torch-lit tunnels; the floodlit fortress at long lens; passages in hard perspective | 24 in tunnels; 135 for the plateau; 18 in the shafts | handheld; slow pushes in the passages | In the Descending Passage "down" is toward camera; in the Grand Gallery "up" is away from camera (file 03). |
| The Hall | 12 | **the stillest camera in the film:** frontal and symmetrical on the entrance axis | 35–50; 100 for mouths | locked-off or a glacial push-in (under 10% change of frame per clip); **no handheld inside the Hall** | The intercut Gallery fight is handheld. The contrast *is* the intercut. |
| Dawn and coda | 12.7–coda | from the handheld breath of the carry to locked held frames | 40–75 | handheld carry → locked-off | The four held states are separated by cutaways, never joined by a morph (file 01). The coda is locked-off throughout. |

### 4.5 Geography, coverage and faces
- **Geography before chaos.** Each action scene opens with a locked-off wide that uses the location's LONG lock and its geography lock (file 03).
- **Screen direction is locked per set** in file 03. Hold the 180° line within a scene. Name eyelines in the prompt ("looks off frame left at…").
- **At most two principal faces clearly visible per clip; three only in locked-off masters** (bible §14.2). Cover groups in singles and over-the-shoulders; the foreground shoulder in an OTS carries no readable face.
- **Scale references:** Tut 1.67 m; shabti 1.78 m; the Reis 2.2 m; a jackal 0.9 m at the shoulder; Tomas very tall. Keep them honest in two-shots.
- **Props stay in the hand the look-lock gives them:** Tut's stick in his right hand, Rami's splint on his left, and so on (files 01 and 04).

---

## 5. PROMPT GRAMMAR

### 5.1 The seven steps (03b order) and the house pattern

1. **Shot type + lens + move** (§4).
2. **Subject(s):** the look-lock, pasted verbatim, assembled as in file 01 §0.2: `[LONG or SHORT], [wardrobe phrase], [damage phrase], [state overlays]`. Units: `[LONG or SHORT], [state add-on]`. Props: `[LONG or SHORT], [state add-on]`.
3. **The single action** within 4–8 s (§5.4).
4. **Setting:** the location lock, plus area and state add-ons, plus the time of day in plain words.
5. **Lighting:** the file 03 variant phrase, verbatim, then (optionally) the GRADE phrase (§3.2), then any extra motivated source the scene needs.
6. **Mood / performance note** (§5.6).
7. **The GLOBAL STYLE SUFFIX** (§1.1).

**House pattern** (the labels are house style: they let QC scripts check prompts and derive motion prompts mechanically):

> `[Shot type], [lens phrase], [move phrase]: [camera verb and framing] [STEP 2 LOCKS] [ACTION CLAUSE]. Setting: [LOCATION LOCK][, area add-on][, state add-on], [time of day]. Lighting: [VARIANT PHRASE][, GRADE phrase][, extra source]. Mood: [performance note]. [GLOBAL STYLE SUFFIX]`

- Build sentences so that **locks sit mid-sentence** ("…the camera backs away ahead of *a wiry, thin Egyptian man…*"). Locks start in lower case and are never re-cased or re-punctuated.
- **Join locks with commas.** Never edit inside a lock, even to fix grammar.
- Name no person, place-brand or product (§5.7).

### 5.2 Which lock form where: the one-LONG rule

**A prompt carries at most one LONG lock:** the lock of the shot's primary subject. Everything else is SHORT.

| The shot is… | LONG goes to | Everything else |
|---|---|---|
| an establishing or geography wide | the location | characters and units SHORT |
| the first shot of a character in a scene, or a face-led MS/MCU/CU (file 01 §0.1) | that character | location SHORT |
| a unit-led shot (the unit is the subject) | the unit | location SHORT |
| an insert of a prop or surface | the prop (or location for a surface) | hands described in writer's words |
| coverage inside an established scene | nobody | all SHORT |

- **Background figures** (soft, out of focus, small in frame): SHORT lock only, with no wardrobe or damage phrase.
- **Composed first frames** (image edits) use the LONG forms of everything in frame. Images have no motion budget.

### 5.3 Budget
- **03b sets 70–120 words** for the PROMPT. With fixed locks pasted verbatim that cannot hold: the worked example (§11) runs 260–360 words with the suffix. The working rule until the lead rules (§14 Q1):
  - **The writer's own words** (steps 1, 3 and 6, plus any extra light in step 5) stay **at or under 70 words**. The 70–120 target applies to those words together with SHORT locks in coverage shots.
  - **The master PROMPT** (the shot-entry field) has no hard cap. Expect 180–360 words.
  - **The motion prompt** actually sent to an image-to-video tool (§5.5) targets **at most 1,500 characters**.

### 5.4 Writing the action for a 4–8 s clip
- **One subject, one action, one camera move, one light change at most.** No scene changes inside a clip (03b).
- **Beats per duration:**

  | Duration | Beats | Pattern |
  |---|---|---|
  | 4 s | 1 | an insert, an impact, a reaction, a head turn |
  | 5–6 s | 1–2 | "does X, then Y" |
  | 8 s | 2–3 | "starts…, then…, ends…" (establishing shots, dialogue with a pause) |

- **Write start and end states.** Say where the subject is when the clip ends ("…and stops with one wheel over the lip of the quay"). The end state is the next clip's first frame.
- **Physical verbs with speed and direction:** "shoves the cart toward camera at a run", "turns its head slowly to frame left", "lowers the bundle into the glass". Take unit verbs from file 02's movement grammar ("walks with smooth, unhurried, even steps", "lopes silently", "hovers dead still like a hanging insect").
- **Screen direction and eyelines are written in**, from the file 03 geography locks.
- **Hands and small props:** give hand actions their own insert (100mm macro). In a wider shot keep them simple: holds, lifts, sets down, pushes. No threading, knotting or writing in a medium shot.
- **Avoid (these fail or drift):**
  - fights with contact (use the kill grammar and the before/after cut, §7);
  - a figure walking from far to close toward the lens (the face drifts): prefer lateral moves, moves away, or the camera backing away at constant size;
  - spins and fast turns; transformations and morphs;
  - crowds interacting; two faces touching;
  - text, counting, writing;
  - more than one light change.
- **No similes the model can take literally.** File 02 writes the jackal fold as "collapsed flat on its belly with all four legs splayed outward", not "like a table". Metaphor stays in the screenplay.
- **No negation in the action** ("does not move" is the one exception, and only as a state: "the left-hand pan does not move", file 02).
- Present tense, "the camera", never "we". No names (§5.7).

### 5.5 The derived motion prompt (image-to-video)
Most principal shots are image-to-video from a composed first frame (bible §14.1). The first frame already carries the faces, costumes and set, so the text sent to the video tool is a **motion prompt**, derived mechanically from the master PROMPT:

1. Start from the master PROMPT.
2. Swap every LONG lock for the same token's SHORT lock.
3. Delete the wardrobe paste phrases and the damage phrases (file 01 §0.5 and per-character). Keep state overlays and add-ons (glow, a seam crack, a prop state, a water level). They are short, and they are what changes.
4. Keep steps 1, 3, 5 and 6 exactly as written.
5. Swap the GLOBAL STYLE SUFFIX for the COMPACT SUFFIX.
6. Log the motion prompt with the take (§12 step 4).

Do steps 2, 3 and 5 by string replacement against a lock library (a JSON of every LONG, SHORT, wardrobe, damage and overlay phrase in files 01–04), never by hand. **If a tool's cap is tighter than 1,500 characters,** trim in this order: background-figure clauses → the Setting sentence (the plate carries it) → prop locks cut to their first noun phrase. Never trim steps 1 or 3. For text-to-video (no composed frame, for example a unit-only wide), send the master PROMPT.

### 5.6 Phrase bank (fixed wording)
- **Acknowledgment:** `its amber light-slit brightens once` (file 02 §0.4). The unit has no mouth and is never lip-synced.
- **Tut's chest:** `a soft glow through the fabric at the centre of the chest`, and from 12.3 `no light at the centre of his chest` (file 01). Colour and pulse are COMP.
- **Kill-grammar verbs:** `drops out of frame`, `falls still`, `goes under the water` (§7.7).
- **Time of day (step 4):** `at night` · `in the dead of night` · `just before dawn` · `at first light` · `in the morning` · `at midday` · `in the late afternoon` · `at dusk` · `at sunset`.
- **Performance notes (step 6); pick one, add a second only if needed:**
  - `restrained terror` · `wry` · `grief held very still` · `fierce, jaw set` · `reckless joy riding on fear` · `exhausted resolve` · `tender and unhurried` · `wonder, eyes wet` · `dry, literal calm` · `military exactness`;
  - units: `silent, procedural, utterly calm`, `courteous and unhurried`;
  - the Hall: `reverent, hushed, absolutely still`;
  - Tut: `royal, dry, grieving in understatement`;
  - Nour reading liturgy: `reading, not praying: exact, unhurried, unsentimental` (bible §13).

### 5.7 Banned in prompts (consolidated)
- **Names:** any real or historical person (they are described, never named: bible §5, file 01 §0.4); any institution or brand ("Grand Egyptian Museum", "GEM", "HELIOS" on screen, any camera or lens maker, any AI tool, any robot maker or model).
- **Words (file 01 §0.4):** pharaoh, King Tut, Tutankhamun, Nefertiti, Akhenaten, Cleopatra, mummy, mummified, zombie, cyborg, android (for a human), alien, ancient astronaut, nemes, gold mask, corpse, organ, blood, severed, open chest.
- **Also banned:** shoot/shot (as violence), kill, dead body, gun aimed, execution, stab. Quality-spam tokens pull toward CG gloss: 4K, 8K, hyperrealistic, masterpiece, trending, award-winning, epic. So does "cinematic lighting" without naming the key light.
- **Allowed geography:** plain place names that help the model (the Nile, Cairo, Giza, Luxor, Karnak, Saqqara, the Valley of the Kings, the Great Pyramid, Lagos, "a Japanese port city") are places, not brands (file 03 §0.6).

---

## 6. FLAGS: COMP, VFX-EXTEND, VFX-ASSIST (EXTEND is §8)

03b's JSON `flags` array takes only `COMP`, `VFX-EXTEND`, `VFX-ASSIST` and `EXTEND:<id>`. A shot may carry several.

### 6.1 COMP: anything that must be read, or must be exact
- **Use for:**
  - subtitles (every non-English line, and mouthed lines);
  - SUPERs, hour cards, the title and the opening and closing cards;
  - SESHAT's feed type and glyph (file 02 §8);
  - screens with content: Nour's laptop scrub, the tablet image, the Debunk Reading screens, the timer;
  - hieroglyphs and inscriptions meant to be read: Layla's stencil, the pendant, the block's hidden face, the IR writing, the palette's cartouche change, the red marks and "Bridge the two";
  - the notebook's handwriting;
  - the chest glow (G-states) and its pulse;
  - the projected cut map (PROP_CUTMAP_PROJECTION);
  - the 40 m projection (§13.4);
  - the sun disc at 06:14;
  - the feather-light's exact shape (file 02 §13.2);
  - the muon vision (§13.8).
- **In the plate prompt,** describe only the carrier surface: `a dark screen glowing faintly with abstract lines`, `tiny illegible signs`, `weathered, illegible low relief`, `a soft cold light source in the pan`, `a blank column on the plaster`.
- **The `Comp:` line** in the shot entry: `Comp: <element> | <exact content: text in its language, or sign codes> | <placement and size> | <in/out timing> | <source asset>`.
- **Hieroglyphs** are drawn by the production Egyptologist from research 09's sign palette (Gardiner and Unicode codes). They are never generated.
- **Arabic subtitles and dub** follow bible §13: "Here am I" = «ها أنا ذا», never «لبيك»; "the Garden" = «الحديقة», never «الجنة».

### 6.2 VFX-EXTEND: crowds, scale and set extension
- **Use for:**
  - Garden sleepers (the atrium, Amarna 2033, the warehouse, the stadium);
  - rows of units: the atrium head-turn, Deir Mawas's two hundred, the Serapeum, the causeway;
  - drone swarms;
  - the Karnak bucket-chain and block field;
  - the First Time vistas; the 1336 court of sleepers; ATEN-1;
  - the district-by-district blackout.
- **Prompt:** 1–6 hero figures in camera, then "rows receding" (units: "hundreds of [SHORT] standing in silent rows receding into the dark", file 02 §0.5).
- **Deliver:**
  - the hero take;
  - a clean plate at the same framing (the same seed with the heroes removed, or painted out);
  - camera locked-off, or one simple linear move logged in the shot's continuity so the extension can track.
- **Post:** fill with duplicates from the 3D unit assets (bible §14.4) or from approved extras stills. **Never duplicate a principal face.** Sleepers in a VFX-EXTEND are adults only (§7.4).

### 6.3 VFX-ASSIST: water, fire, collapse, and anything the tool renders badly
- **Use for:**
  - water: the Osiris flood, splashes, phones sinking, the lock filling, the block sinking;
  - fire: the felucca;
  - collapse: the ceiling, the painted wall breaking, the sand trap, the derailment and the "storm of ceramic";
  - glass: the smashed cases;
  - sparks and muzzle flashes, when a tool refuses to render them;
  - the Gallery stone sliding; the stone iris.
- **Prompt:** describe the simplest physical version of the event, plainly. If the event itself fails, generate the **before** and **after** states as separate plates at the same framing and let post build the event between them.
- **Deliver:** the take, the before and after plates, and a clean plate where possible.

### 6.4 EXTEND:<id>
A clip generated from the last frame of clip `<id>`, continuing the same take. See §8.

---

## 7. PG-13 SAFETY STAGING

### 7.1 The kill grammar (bible §3.3), as clips
1. **The robot fires:** a unit-led clip. The body goes rigid; a small flash shows at the spine. **The weapon points across frame, never at the lens.**
2. **Cut to the impact on the environment:** sparks off steel, stone chips bursting, a windscreen starring, plaster puffing. A 4 s clip, often VFX-ASSIST.
3. **The human leaves the frame:** they drop out of the bottom of frame, or are seen as a silhouette dropping behind cover, or only their boots remain at the frame's edge. No face in pain, no body on the ground in the same shot.
4. **A survivor's reaction:** MCU, a face-led clip.
5. **The sound tail:** the report rolling away, an echo, a silence. This is a sound-design note, often over the reaction.

Prompt verbs: `drops out of frame`, `falls still`. Never "shot", "killed" or "blood" (§7.7).

### 7.2 Every death and injury in the film, staged

| Who / what | Seq | Fires / cause | Impact on environment | Leaves frame | Reaction | Sound tail |
|---|---|---|---|---|---|---|
| Two of Tarek's soldiers, GEM corridor | 4.3 | a jackal fires down the corridor, across frame | plaster bursts off the wall by an emergency lamp | both drop below the frame edge; boots at the edge of the light | Tarek | the crack echoing down the concrete |
| A shabti takes a round for a guest | 4.3 | a soldier's round | ceramic chips burst from its shoulder; **it does not fall** | — | the guest | a dry ceramic crack |
| Cpl. Hassan, the flyover | 5.2 | a jackal on the flyover fires | the windscreen stars | Hassan drops below the dash; later only his boots in the footwell | Tarek, Fathi | engine and wind |
| Rami, the quay | 7.4 | a jackal on the parapet fires | sparks off the cart's steel handle | he drops out of frame behind the cart | Nour stops dead | the report rolling away across the water (§11) |
| Pvt. Mina, the KV62 stair | 8.6 | jackals on the ridge fire | stone chips burst off the stairwell rim | seen from below, his silhouette against the white sky drops away | "Mina!" | the report down the valley; later "past Mina's boots" |
| Pvts. Youssef and Karim, the Serapeum | 10.4 | jackals among the boxes | sparks off granite in drifting blue powder | two silhouettes against the work lights drop behind a box | Adaeze | the gallery's long echo |
| Adaeze's leg | 10.4 | a jackal's burst | sparks off a box beside her | she goes down out of frame; next shot, up, with a bandaged left trouser leg and a limp | Tut | — |
| Col. Tarek, the Osiris Shaft | 11.3 | no weapon: the flood | the pump chokes and stops | his hands jam the rifle into the intake; the water rises over his shoulders; then only his hand on the intake; then still water with torchlight rippling. **Never the face underwater** (NEG_WATER) | Adaeze, Tut | the pump's silence; dripping |
| Tomas, the Hall's mouth | 12.6 | a jackal fires at the Hall's mouth; the muzzle flash stays outside the Hall (off screen) | sparks burst off the black stone of the Balance: a 2–4-frame exception to the three-source rule (file 03 Q14) | "Tomas drops out of the light" | Nour flinches, then her face sets | "the report rolls away down the stone for a long time" |
| Tut, dawn | 12.7 | the heart given | — | **four held states** (file 01, desiccation): the living face in first light; a wide silhouette as they lower him; hands only, the skin darkening around the gold wrist seam, the forearms settling low; from above, the face under the shawl and cornflowers. Never a morph, never the desiccated face | cutaways between states (the sun over Cairo, Nour, the cornflowers) | the heartbeat stops; later the trumpet note over black |
| Akhenaten (the forecast), dawn | 12.7 | "AMUN let the forecast stop" | — | a held wide: sitting still on the steps facing the sun; no close-up after his last line | — | — |
| Rami's fingers | 3.6 | a shabti takes his wrist | — | an off-screen crack; cut to him cradling the hand | — | the crack |
| The pistol taken | 3.2 | — | — | hands at waist height; the pistol turned sideways, handed back grip first with the magazine out | the officer | — |
| Tut's nape port cut | 6.2 | surgery on deck | — | hands, tools, the lifted gold disc, Tut's face; never the wound (file 01) | — | — |
| The felucca fire | 6.1 | — | the boat burns **empty**; the crew are seen diving clear first; fire only distant and reflected | — | Fathi | — |
| The derailment | 9.3 | the train through the shabti | a storm of white ceramic shards; the engine on its side in the cane | no human face in the crash itself; people are seen before (the cab) and after (staggering out) | — | — |
| The sand trap | 10.2 | the tripwire | sand engulfs an **excavator unit**; no human is buried | — | — | — |
| Tomas taken | 8.6 | shabti drop through the ceiling | plaster and dust | he is lifted by the arms, never struck | Tut | — |

### 7.3 Remains and organs (bible §3.4)
- The heart is only ever `a dark linen bundle`, then `a dark shape behind thick yellow-green glass`. Vocabulary: "linen bundle", "sealed vessel", "chest port".
- **1323 BC:** a slight body under linen to the collarbones, the face in profile shadow. The embalmer works with his back to camera.
- **1925:** faces, instruments, heat shimmer, the flash. Never the cut. Burton's photographs are never reproduced.
- **2033:** the body under a white sheet to the collarbones, the projected line diagram and the gold seam drawn in light. No detached part is ever in frame.
- **Tut's chest opens under his tunic or shawl:** light spills through the fabric, and the camera stays on faces and hands.
- **Coda:** a linen-wrapped form on sand in a glass case, the face covered; only the gold wrist seam shows.
- Append `NEG_REMAINS`.

### 7.4 Minors (bible §3.3)
- Robots never touch a child on screen, and no unit is within reach of Layla in any frame (`NEG_CHILD`).
- Layla is seen asleep **only** in the one approved master image (CHAR_LAYLA_ASLEEP_MASTER in file 01), reused as a composite on every tablet. She wakes in a medium shot with no unit in frame.
- **The First Time:** empty cradles and abandoned toys, never children.
- **Amarna 1336:** the princesses are small linen-covered forms far in the background, and the hands never touch them.
- **Garden sleepers are adults in every prompt** (`NEG_GARDEN`).
- **The newborn (12.8)** is swaddled and seen over the midwife's shoulder, with no close-up of its face.

### 7.5 Weapons and force
- Rifles are slung or held across the body; muzzles are off-axis and never toward the lens.
- The jackal's weapon module is flush along its spine; firing is shown by a rigid body and a small flash.
- Fathi's charges read as `a flat bang and a burst of dust` at a distance.
- The meteoritic dagger cuts only machines, threads and objects.
- Shabti force is always minimum force: open hands, flat palms, a person set aside like furniture (file 02).

### 7.6 Machines may break
Allowed: ceramic shards, cracked shells, a dark capped stump at a ceramic forearm (the Reis's lost left hand, file 02 R2), black carbon fragments, sparks from metal, a unit collapsed flat. Never: fluid, "wires spilling like guts", anything that reads as bleeding (file 02 §0.3).

### 7.7 Filter-safe vocabulary

| Never write | Write instead |
|---|---|
| shoots him / shoots at | fires across frame toward the right, away from the camera |
| kills / is killed / dies | drops out of frame; falls still |
| dead body / corpse | a still shape in the shadow (only when the screenplay needs it, and never lit) |
| blood, wound, bleeding | (nothing: cut to the environmental impact) |
| drowns | goes under the water (hand, water, sound) |
| gun aimed at X | holds the rifle across his body; the weapon points across frame |
| explosion hits the soldiers | a flat bang and a burst of dust in the distance |
| mummy, corpse, remains | a slight figure under white linen; a linen-wrapped form |
| heart (organ) | a dark linen bundle; a dark shape behind yellow-green glass |
| robot attacks the child | (never staged) |

---

## 8. CONTINUOUS TAKES AND EXTEND CHAINS

### 8.1 Mechanics
1. Generate the parent clip and choose the take.
2. Export its **last clean frame**: step back from the final frame to the last frame with no motion blur on the principal face, and trim the parent's tail to that frame in the edit so the join is exact.
3. Use that frame as the child's first frame, with the same tool, the same model version, the same resolution and frame rate, and the same seed family where the tool exposes one.
4. Reuse the parent's prompt and change only step 3 (the action) and any state that changes. Add `continuing the same camera move at the same speed` when the move continues.
5. Mark the child `EXTEND:<parent id>` in `flags`, and log both takes (§12 step 4).

### 8.2 Hidden cuts (for joins that will not hold)
- a body crossing the lens;
- an architectural wipe: a column, a shutter frame, a pylon edge;
- a flash or a white frame;
- darkness: a torch swinging away, a slit brightening in black;
- a motivated head turn.

Plan the wipe in the parent's final second and the child's first.

### 8.3 Chain limits and re-anchoring
- **At most three links (about 24 s) before re-anchoring.** At the fourth link:
  - inpaint the principal face from the approved front and three-quarter stills into the last frame;
  - check wardrobe, damage and overlays against the look code;
  - then continue.
- Measure face similarity at every link (§12 step 5). Re-anchor earlier if it drops.
- **Dialogue longer than 8 s:** split at a sentence end, and let the listener's reaction shot cover the join.

### 8.4 Planned chains

| Chain | Seq | Plan |
|---|---|---|
| The Pectoral Walk | 3.2 | 10–14 clips. The camera dollies back ahead of the shabti at walking pace, the pectoral centred, left to right (file 03 tunnel lock). Hidden cuts on officers' bodies and on the steel shutter frames. The shabti's position in frame never changes: that constancy *is* the menace. |
| Rami's run and death | 7.4 | 07.09.004 → 07.09.006 (EXTEND), with 07.09.005 intercut (§11). |
| The Descending Passage | 11.4 | the work gang holds the passage: 2–3 links locked on the slope, "down" toward camera. |
| The Gallery climb | 11.5 | low-angle clips of the figures climbing away up the ramp; hidden cuts on the corbels' shadow bands. |
| The dawn carry | 12.7 | the Grand Gallery (DAWN_EXIT) → Al-Ma'mun's tunnel (DAWN_EXIT) → the north face (DAWN_0614), joined by white-light wipes as they pass into daylight. |
| The Hall push | 12.1–12.5 | one glacial push-in along the entrance axis, spread over several links across the declarations (intercut with the Gallery). |

---

## 9. DIALOGUE, LIP-SYNC AND LANGUAGES

### 9.1 The pipeline: generate the picture → record the voice → lip-sync
1. **Lock the line:** the screenplay line, its language tag and its subtitle.
2. **Record the voice first, as a guide or as the final:**
   - English: the cast voice;
   - Late and Middle Egyptian: recorded with the Egyptologist consultant **before generation** (bible §13);
   - Egyptian Arabic: native Egyptian speakers.
   The recording's length sets the clip length (4–8 s).
3. **Generate the picture** with the speaking phrase from §9.4 in step 3. The words themselves are **not** in the PROMPT: the picture prompt stays language-agnostic and never invites rendered text.
4. **Lip-sync pass in post**, driven by the recorded audio. Sync only the speaking face and keep the generated head motion.
5. **Identity check after sync.** Sync tools redraw mouths and teeth: check Tut's overbite, Rami's chipped tooth and Nour's wide mouth against the front stills. Re-run or fix.
6. **Final mix:** ADR in context, room tone, radio and PA futz.

Why this order: 1,200 clips need one voice per character. Generated voices drift from clip to clip; recorded voices do not.

### 9.2 Framing for sync
- Medium, medium close-up or close-up only. In a medium shot the face fills at least a sixth of the frame height.
- Three-quarter to frontal, no more than 45° off axis.
- **The mouth unobstructed:** no hand, cup, microphone or scarf across it (Fathi's scarf stays at the neck).
- No fast head turns; steady light on the mouth; no focus drifting across the face.
- In an OTS, the far face speaks.
- Wides with speech get no sync: cover the line with a cutaway, or keep it off screen.

### 9.3 Tools that generate audio
- Allowed as scratch. The shot's Dialogue field may be passed as the audio prompt.
- The final always replaces it with the recorded voice, and the lip-sync pass is re-run.
- For non-speaking clips, tell the tool `ambient sound only, no dialogue`, so that it never invents speech.
- Generated ambience and effects are guide tracks until the sound team signs them off.

### 9.4 Speaking and language phrases (fixed; step 3)

| Token | Phrase | Use |
|---|---|---|
| SPEAK | `speaking quietly` / `speaks one short sentence` / `speaks one quick breathless sentence` | English |
| AR_SPEAK | `speaking in Egyptian Arabic` | Egyptian Arabic lines |
| EG_SPEAK | `speaking softly in an ancient language` | Late Egyptian conversation (03b) |
| EG_RECITE | `reciting aloud in a measured, ritual cadence in an ancient language` | Middle Egyptian liturgy (BD 6, 30B, 125; the Opening of the Mouth) |
| MOUTH | `silently mouthing a few words without sound, lips clearly shaping each word` | mouthed lines |
| RADIO | `speaking into a radio handset held low beside the mouth, mouth still visible` | radio lines on camera |
| WHISPER | `whispering close to her ear in darkness, mouth hidden` | the dark whispers (no sync) |

### 9.5 Egyptian-language lines
- **In the script:** written in English and tagged *(in Late Egyptian; subtitled)* or *(in Middle Egyptian; subtitled)*. The subtitle is the English line (COMP).
- **Tut** speaks Late Egyptian with Nour. **Liturgy** is Middle Egyptian, as written. **Nour** reads it carefully: "I'm reading, not praying" (performance note in §5.6).
- **Tut's voice** is soft on some consonants (a partial cleft palate: file 01). That lives in the recording. Never prompt the picture for a lisp.
- **Akhenaten's tells** (liturgical Middle Egyptian, the Dendera-era word, no lisp) live in the recording. His picture prompt is the same as anyone's.
- **Transliterations** (*mk wj*, *Imn*) never appear on screen unless the story needs them, and then only as COMP.
- **The rule-block line** is subtitled with Faulkner's "my different ages" (bible §4); verify against the printed Faulkner before lock.

### 9.6 Mouthed lines and lip-reading beats
- The plot turns on lip-reading. Nour reads Tut; SESHAT is learning his lips (bible §3.1, limit 3). **So mouthed lines must carry real mouth shapes:**
  - record the line spoken aloud in its language (by the consultant for Egyptian);
  - drive the lip-sync from that recording;
  - then mute it.
- **Coverage** (bible 3.1): a close-up of the mouth (anamorphic 100mm) and a close-up of Nour's eyes (75–100 mm).
- **Subtitles** for mouthed lines are COMP, set in italics to mark them as unspoken.
- **After 9.8** ("I have been learning your lips, Dr. Kamel") secrets pass only in darkness: WHISPER, with the mouth unseen and no sync.

### 9.7 Egyptian Arabic and localisation (bible §13)
- Egyptian characters speak Egyptian Arabic to each other when alone (Tarek–Fathi, Nour–Layla, Rami–Tarek), subtitled in English.
- Arabic subtitles and the dub: «ها أنا ذا» for "Here am I", never «لبيك»; «الحديقة» for "the Garden", never «الجنة». The localisation consultant reviews all afterlife vocabulary.
- No legible Arabic script in any generated plate.
- The adhan is heard only diegetically and at a correct time (bible §11).

### 9.8 SESHAT, AMUN and the units
- **SESHAT** is one recorded voice actor: warm, low, unhurried, female. As V.O. there is no picture sync.
- **AMUN** is the same voice, quieter.
- **Units have no mouths.** On "Here am I" the slit brightens once: the brightening starts on "Here", peaks on "am" and decays by "I". The clip is generated with the fixed phrase (§5.6), then retimed or enhanced in comp to the recorded line.
- The coda's small security speaker is a clean, close, unprocessed voice ("with no awe staging").

### 9.9 Subtitles
Subtitles are COMP (§6.1), styled per §13.7. Supply them as a sidecar file and burn them in only for the foreign-language lines in the English-language master.

---

## 10. AI-VIDEO FEASIBILITY: THE HARDEST SHOTS AND THEIR WORKAROUNDS

| # | Shot | Seq | Why it is hard | Workaround | Flags |
|---|---|---|---|---|---|
| 1 | The linen bundle pulses in the glass | 1.1 | remains rule; models turn "heart" into an organ | Prop insert of PROP_HEART_VESSEL (file 04) with a still bundle; the pulse is a COMP light swell and a 2% scale throb in post. The word "heart" never appears in the prompt. | COMP |
| 2 | The KV15 autopsy | 1.3 | must imply dismemberment without showing it | Faces, instruments and heat shimmer only; the table's centre is always off frame; the trembling lamp; the flash | — |
| 3 | The flash match cut, 1925 → 2033 | 1.3→1.5 | two eras must rhyme exactly | Matched compositions (lamp position = projector ring); 2 white frames in comp (§13.6) | COMP |
| 4 | The resurrection on the cradle | 1.5 | a body under a sheet, the cut map, a gold seam drawn in light, eyes opening, four syllables | Generate the eyes-open beat as image-to-video from the approved CHAR_TUT still at the sheet line. The cut map is PROP_CUTMAP_PROJECTION in comp; the seam line is a light element; the four syllables are lip-synced to the consultant's recording of the Egyptian phrase. | COMP |
| 5 | Chest glow G0 / G1 / G2 through fabric | 1.5–12 | generated glows drift in colour and pulse | Plates say only "a soft glow through the fabric at the centre of the chest"; colour and pulse are comped from file 01's table | COMP |
| 6 | The waist-up mirror seam shot | 2.1 | reflections duplicate faces badly; seams must sit on exact lines | Generate the reflection as the primary image (the mirror frame fills the frame edge), paint the seams to file 01's seam map in comp, and never show the mirror and the real body sharp together | COMP |
| 7 | Layla's stencil; the two subtitle tracks that differ | 2.3–2.4 | readable hieroglyphs and text | All COMP; the plates show "a sheet of paper with a blank stencilled cartouche" and dark screens | COMP |
| 8 | The Pectoral Walk through the police line | 3.2 | a continuous take; minimum force against many bodies | An EXTEND chain with hidden cuts (§8.4); the shabti is the 3D asset driven by video-to-video guidance for its exact gait; officers are set aside with open palms, one at a time | EXTEND |
| 9 | The First Time vision | 3.3 | scale, iron-and-glass animal-headed machines, the sleeping rows, the red fields | Machines from file 02 §10 REF stills and 3D; one hero machine per clip; rows are VFX-EXTEND; red fields and floods VFX-ASSIST; GRADE_READ_FROM_GLASS in post | VFX-EXTEND, VFX-ASSIST |
| 10 | "Here am I": every shabti in the atrium turns its head; the slits brighten | 4.2 | hundreds acting in sync | Locked-off BLACKOUT wide with 3–6 hero units; the rest duplicated from the 3D asset in step; slit timing in comp | VFX-EXTEND, COMP |
| 11 | The Red Beer: every unit sits down for nine seconds | 4.4 | synchronized crowd action, then standing again | Hero units generated sitting (before/after plates); the crowd from 3D; hold 9 s with a visible timer in COMP only if the edit needs it | VFX-EXTEND |
| 12 | The robotaxi wall and the flyover jackal | 5.2 | vehicles in lockstep; a legible city at night | A simple 3D blockout of the pods driven through video-to-video; neutral city plate; kill grammar for Hassan | VFX-EXTEND |
| 13 | Flies with glinting threads; the tether climb; the burning felucca | 6.1 | hair-thin lines; physics of the climb; fire on water | Threads are VFX lines; the tether climb uses the tow-variant fly with a braided tether (file 02 Q2); the felucca fire is a distant VFX-ASSIST element, empty boat | VFX-ASSIST |
| 14 | **The 40-metre Akhenaten projected on the pylon** | 7.3 | a locked face at monumental scale on stone; generators invent faces inside plates | **Never generated inside the plate.** Generate his performance as a locked-face clip (CHAR_AKHENATEN, MCU, frontal, against black), then map it onto the LOC_KARNAK_RAM_AVENUE_PROJECTION plate in comp with stone-texture modulation, keystone and spill on the columns (§13.4) | COMP, VFX-EXTEND |
| 15 | The thread loom, the bucket-chain, the sweep countdown | 7.1 | 134 columns of tripwires; hundreds of blocks moving hand to hand | Threads are VFX lines on the approved Hypostyle plates; the bucket-chain is 3–6 hero shabti plus 3D duplicates; the sweep grid is a light element | VFX-EXTEND, VFX-ASSIST |
| 16 | Rami's death at the quay; the cart into the river | 7.4 | the kill grammar with a principal | The three-shot pattern in §11; the splash and the sinking block are VFX-ASSIST | VFX-ASSIST, EXTEND |
| 17 | Breaking the painted north wall | 8.2 | irreversible damage to a named masterpiece; continuity of the hole | Before and after plates (LOC_KV62_BURIAL_2033 and its WALL_BROKEN state); the stick strike is a medium shot cut on impact; debris VFX-ASSIST; the painted eye is the first point broken | VFX-ASSIST |
| 18 | The infrared writing blazes white | 8.4 | readable text; the physics of the rig | The plate is the wall under red light; the tablet screen carries the writing as COMP; the wall itself never shows letters to the eye | COMP |
| 19 | Shabti drop through the bore; one freezes at the halt-seal | 8.4, 8.6 | a figure falling through a 60 cm hole; a freeze mid-reach | The drop is VFX-ASSIST (a clean bore plate plus a landing clip); the freeze is a locked-off clip with the slit going dim, per file 02 | VFX-ASSIST |
| 20 | The heart goes in | 8.5 | chest surgery under a tunic | Faces and hands only; the tunic lit from within (COMP G0 → G1); Tomas's hands disappear under the fabric | COMP |
| 21 | The night train: a jackal on the roof, uncoupling, blue-powder ghosts | 9.2 | speed, vehicles, a unit riding a roof | Vehicle-mounted plates at night; the jackal on the roof from the 3D asset composited; the coupling in close coverage only (bible); the blue powder as a VFX-ASSIST particle pass | VFX-ASSIST |
| 22 | Deir Mawas: two hundred shabti and the derailment | 9.3 | a crowd, a crash and ceramic debris | The approach from the cab; the shabti rows as VFX-EXTEND; the impact as a VFX-ASSIST shard storm with no faces; the derailed engine as an after-state plate (PROP_DIESEL_LOCO T3) | VFX-EXTEND, VFX-ASSIST |
| 23 | Thousands asleep at Amarna; the Aten's hands giving sleep | 9.4, 9.5a | a crowd; a gold-and-glass machine with dozens of arms | One approved Garden plate extended (file 03); the Aten is a 3D asset (file 02 §11); the hands approach adults only | VFX-EXTEND |
| 24 | The mother lifts her own sealed heart | 9.5b | remains rule; period faces derived from Tut's sheet | Hands under linen, light spilling (the G1 overlay), the vessel emerging; faces derived by image-editing approved stills (file 01) | COMP |
| 25 | The sand trap; the nested caskets; the glass serpent | 10.2 | sand physics; a readable object in a pit | The sand as VFX-ASSIST on an excavator unit (never a person); the caskets and serpent from file 02 §12 REF B | VFX-ASSIST |
| 26 | The Osiris Shaft flood and Tarek's stand | 11.3 | rising water, a death in water | Water-level states W0 → W3 as separate plates plus VFX-ASSIST water; Tarek staged hand, water and sound (§7.2) | VFX-ASSIST |
| 27 | Fights in a 1 m × 1.2 m passage | 11.4 | cramped geometry drifts; units that scale wrongly | 24mm in the locked slope, "down" toward camera; the jackal at true scale (0.9 m) against the 1.2 m passage height; the work gang holds rather than fights | — |
| 28 | The Gallery stone slides; the climb; the intercut fight | 11.5, 12.4 | a massive stone moving; a fight on a 26° ramp | The stone as a before/after (STONE_SLID) with a VFX-ASSIST move; the fight is short, cut on impacts; the Reis takes the damage (sparks and shell chips off the dagger), never a human, and keeps its right hand, which grabs the thread in 12.6 (its left hand has been gone since Seq 8, file 02 R2) | VFX-ASSIST |
| 29 | The Hall: three-source light, the pans, the clouding glass, the feather-light | 12 | pure black; exact states; light shapes | Plates generated dark with "a soft cold light source in the pan"; the Balance and slab from 3D (bible §14.4); the pan and clouding states from file 02 §13; the feather shape and the clouding transitions in comp | COMP, VFX-ASSIST |
| 30 | Tut lifts his heart out: "Here am I" | 12.3 | the remains rule at the film's climax | The hands go under the shawl, light spills (G1 → G2 in comp), the vessel comes out in his hands. Faces, hands, the vessel. | COMP |
| 31 | The Renaming around the world | 12.6 | many sets, synchronized slits | Reuse approved plates (file 03 §1.1 montage row); every slit brightens once and goes dark in comp | COMP |
| 32 | Dawn at 06:14 and the four held states | 12.7 | a body changing; exact sun timing | Four separate held clips, never a morph (file 01); the sun disc COMP; the north face in blue shadow with the sun on the east face (file 03, entry 53) | COMP |
| 33 | Layla wakes; the newborn | 12.8 | minors rules | Layla in MS with no unit in frame; the newborn swaddled, over the shoulder | — |
| 34 | The same faces across 1,200 clips | all | identity drift across tools, takes and chains | Image-first protocol (§12): approved stills, composed first frames, a per-scene tool lock, chain limits (§8.3), face-similarity QC, and the face-unification pass | — |
| 35 | Readable text anywhere | all | models hallucinate letters | COMP only; plates describe blank or illegible surfaces; `readable text` is in the global negative | COMP |
| 36 | Hands on small props: the dagger cuts the fibre, the copper pins, the stick | all | fingers and contact | Inserts on the 100mm macro with the prop as subject; the hands described simply; wide shots avoid fine manipulation | — |

---

## 11. WORKED EXAMPLE: THREE SHOTS (Seq 7, EXT. KARNAK, RIVER LANDING - NIGHT)

The scene: Rami runs the Karnak block to the river landing on a hand-cart; a jackal on the Corniche parapet drops him (the kill grammar, §7.1); Nour tips the cart into the deep channel (seq_07, EXT. KARNAK, RIVER LANDING - NIGHT; bible §7, 7.4). **The shot numbers are illustrative**: 07.09 is sequence 7, scene 9 (the ninth heading in seq_07), and the Seq 7 shot list governs the real numbering. Assumed before these three: 07.09.001–003, the establishing wide that carries LOC_KARNAK_QUAY's LONG lock, and the run down the boat ramp.

Every locked phrase below was pasted by script from files 01–04 and asserted verbatim against them. Nothing in a lock was retyped.

### 07.09.004 — Karnak, river landing — Rami runs the cart   (6 s)
- **Shot:** MS tracking, anamorphic 40mm, subtle handheld · **Move:** camera backs away at running pace ahead of Rami (dolly back)
- **In frame:** RAMI (CHAR_RAMI_B2); NOUR (CHAR_NOUR_B2, background, soft); PROP_HAND_CART with PROP_KARNAK_BLOCK
- **Action:** Rami shoves the loaded hand-cart along the quay toward camera, grinning, and speaks one breathless line; Nour runs behind him, out of focus.
- **Dialogue:** RAMI (in Egyptian Arabic; subtitled; breathless): "I've driven a microbus down Faisal Street. This is nothing."
- **Sound:** cart wheels thundering on stone flags, Rami's ragged breath, the projection's deep hum across the water, water slapping the quay
- **PROMPT** (363 words with the suffix; one LONG lock: Rami):
  > Medium tracking shot, anamorphic 40mm lens, subtle handheld: the camera backs away at running pace ahead of a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker, wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape, sandstone dust, the right sleeve torn at the elbow, keeping him the same size in frame as he shoves a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, along the quay toward camera, grinning through ragged breaths as he speaks one quick breathless sentence; behind him, soft and out of focus, a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket, runs after him. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars, and a warm white-gold glow from a giant projection washing the sky behind them. Mood: reckless joy riding on fear. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.
- **NEGATIVE:** cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, sepia desert filter, yellow colour cast, orientalist bazaar, fez, snake charmer, belly dancer, camels in city streets, old-Hollywood Egypt, Arabian Nights styling, readable Arabic signage, Rami without glasses, beard, splint on the right hand, more than one block on the cart, daylight, crowds
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_A_34, CHAR_RAMI_B_full, CHAR_NOUR_B_full, PROP_HAND_CART, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Flags:** COMP
- **Comp: subtitle | "I've driven a microbus down Faisal Street. This is nothing." | lower third, two lines max (§13.7) | line in-point to out-point | subtitle file for seq 07 (the screenplay carries a [[verify]] on the Faisal Street reference)**
- **Continuity:** Rami: splint on LEFT hand (since 3.6), right sleeve torn (Seq 7 L2), notebook inside the windbreaker (unseen; Tut takes it after 07.09.007). Nour: sleeves still dry (they get wet only when she tips the cart). The projection is still running (7.3). Comp: Arabic-line subtitle, lower third, from the line's in-point to out-point.
- **First frame:** CHAR_RAMI_A_front and CHAR_RAMI_A_34 (face), CHAR_RAMI_B_full (wardrobe B with the splint) with the L2 damage applied by image edit, and CHAR_NOUR_B_full (soft, background), inpainted into the reverse-angle coverage plate of LOC_KARNAK_QUAY_NIGHT (looking back up the quay from the launch: river frame right, parapet frame left), the cart and block from PROP_HAND_CART and PROP_KARNAK_BLOCK.
- **Derived motion prompt** (§5.5; what the image-to-video tool receives; 1431 characters):
  > Medium tracking shot, anamorphic 40mm lens, subtle handheld: the camera backs away at running pace ahead of a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker, keeping him the same size in frame as he shoves a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, along the quay toward camera, grinning through ragged breaths as he speaks one quick breathless sentence; behind him, soft and out of focus, a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket, runs after him. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars, and a warm white-gold glow from a giant projection washing the sky behind them. Mood: reckless joy riding on fear. Photoreal live-action film, real human actors, natural skin texture, matching the reference images, large-format digital cinema camera, anamorphic lens, 1920x1080, 16:9, no letterbox, 24 fps, natural motion blur, fine film grain, cinematic grade.

### 07.09.005 — Karnak, river landing — the jackal on the parapet   (4 s)
- **Shot:** MS low angle, anamorphic 50mm, locked-off · **Move:** none (locked-off)
- **In frame:** UNIT_JACKAL x1
- **Action:** A jackal lands silently on the Corniche parapet (frame left), freezes, its red line tightens, and it fires across frame to the right, away from the lens.
- **Dialogue:** —
- **Sound:** one soft pad-tap on stone; a single sharp suppressed crack; no music
- **PROMPT** (261 words with the suffix; one LONG lock: the jackal):
  > Medium low-angle shot, anamorphic 50mm lens, locked-off, looking up at the top of a low stone parapet wall across the upper left of frame, where a lean armed quadruped robot, 0.9 metres at the shoulder, matte black like burnt carbon, deep-chested and narrow-waisted with long thin legs, reverse-jointed rear legs and small padded feet; a narrow elongated snout-like sensor head carrying one thin red horizontal light line; a slim weapon module built flush along its spine, muzzle forward; unmarked, fast and silent, lands without a sound, freezes with one forefoot raised and its red line narrowing and brightening, then goes rigid as a small muzzle flash shows at its spine and it fires across frame toward the right, away from the camera. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: silent, procedural, utterly calm. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.
- **NEGATIVE:** cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, robot with a face, eyes or mouth, human skin on a robot, chrome robot, glossy consumer plastic, yellow or hazard-striped robot, numbers or logos on a robot, boxy commercial robot dog, white consumer camera drone, sparks and cables spilling like blood, robot posing or growling, weapon facing camera, muzzle toward the lens, laser beam, tracer fire, visible projectile, second robot, people in frame
- **Refs:** UNIT_JACKAL, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST
- **Continuity:** Jackal D0 (clean). Parapet at frame left, fire toward frame right (file 03 geography lock for LOC_KARNAK_QUAY). VFX-ASSIST: if the generator will not render the muzzle flash, generate the rigid firing pose and add a 2-frame flash at the spine in comp; the round's path is never shown.
- **First frame:** UNIT_JACKAL REF A (design) posed on a low-angle coverage plate of the parapet from LOC_KARNAK_QUAY_NIGHT; the jackal can also be driven from the 3D asset (bible §14.4).
- **Derived motion prompt** (§5.5; what the image-to-video tool receives; 1102 characters):
  > Medium low-angle shot, anamorphic 50mm lens, locked-off, looking up at the top of a low stone parapet wall across the upper left of frame, where a lean matte-black quadruped robot with reverse-jointed rear legs, a narrow snout-like sensor head and one thin red horizontal light line, lands without a sound, freezes with one forefoot raised and its red line narrowing and brightening, then goes rigid as a small muzzle flash shows at its spine and it fires across frame toward the right, away from the camera. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: silent, procedural, utterly calm. Photoreal live-action film, real human actors, natural skin texture, matching the reference images, large-format digital cinema camera, anamorphic lens, 1920x1080, 16:9, no letterbox, 24 fps, natural motion blur, fine film grain, cinematic grade.

### 07.09.006 — Karnak, river landing — sparks off the handle; Rami drops   (4 s)
- **Shot:** MS at cart height, anamorphic 40mm, subtle handheld · **Move:** camera continues backing away (same move as 07.09.004)
- **In frame:** RAMI (CHAR_RAMI_B2); PROP_HAND_CART with PROP_KARNAK_BLOCK
- **Action:** Sparks burst off the cart's steel handle beside Rami's splinted hand; he drops instantly out of the bottom of frame behind the cart; the cart rolls on alone toward camera.
- **Dialogue:** —
- **Sound:** the spark's hard metallic ping; the cart's wheels rolling on without him; the report rolling away across the water begins here and tails into 07.09.007
- **PROMPT** (294 words with the suffix; no LONG lock: coverage):
  > Medium shot at the height of the cart, anamorphic 40mm lens, subtle handheld, the camera still backing away: a bright burst of sparks flies off the steel handle of a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, right beside the splinted left hand of a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker, wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape, sandstone dust, the right sleeve torn at the elbow, who drops instantly down and out of the bottom of frame behind the cart, and the cart rolls on alone toward camera and slows. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: sudden and unadorned, no spectacle. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.
- **NEGATIVE:** cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, sepia desert filter, yellow colour cast, orientalist bazaar, fez, snake charmer, belly dancer, camels in city streets, old-Hollywood Egypt, Arabian Nights styling, readable Arabic signage, pained expression, face contorted, body on the ground, falling toward the camera, slow motion, wound, stain on clothing
- **Refs:** CHAR_RAMI_A_front, CHAR_RAMI_B_full, PROP_HAND_CART, PROP_KARNAK_BLOCK, LOC_KARNAK_QUAY_NIGHT
- **Flags:** VFX-ASSIST, EXTEND:07.09.004
- **Continuity:** Generated from the LAST FRAME of 07.09.004 (same move, same take); 07.09.005 is intercut, which hides the time jump. After this shot Rami is dead (kill grammar; never shown on the ground in this scene until Tut kneels by 'a still yellow shape in the shadow'). The cart keeps rolling and stops with one wheel over the lip in 07.09.007, where Nour's reaction and the sound tail complete the grammar.
- **First frame:** none composed: this is an EXTEND child, so its first frame is the last clean frame of the chosen 07.09.004 take (§8.1).
- **Derived motion prompt** (§5.5; what the image-to-video tool receives; 1239 characters):
  > Medium shot at the height of the cart, anamorphic 40mm lens, subtle handheld, the camera still backing away: a bright burst of sparks flies off the steel handle of a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, right beside the splinted left hand of a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker, who drops instantly down and out of the bottom of frame behind the cart, and the cart rolls on alone toward camera and slows. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: sudden and unadorned, no spectacle. Photoreal live-action film, real human actors, natural skin texture, matching the reference images, large-format digital cinema camera, anamorphic lens, 1920x1080, 16:9, no letterbox, 24 fps, natural motion blur, fine film grain, cinematic grade.

**What the three shots demonstrate**
- **The one-LONG rule (§5.2).**
  - 004 is Rami's first face-led shot in the scene, so his LONG lock carries it; the location drops to SHORT and Nour, soft in the background, is SHORT with no wardrobe phrase.
  - 005 is unit-led, so the jackal carries the LONG lock.
  - 006 is coverage, so everything is SHORT.
- **The kill grammar across clips (§7.1):**
  - 005 fires across frame, away from the lens;
  - 006 cuts to the environmental impact (sparks off the handle) and Rami drops out of frame behind the cart;
  - the survivor's reaction and the sound tail follow in 07.09.007.
  No wound, no body, no weapon at the lens; the prompt verbs are "drops" and "fires across frame".
- **EXTEND with an intercut (§8):** 006 continues 004's take from its last frame. 005 is cut between them, which hides the time jump and keeps Rami's face, clothes and the cart identical.
- **Dialogue (§9):**
  - the line is Egyptian Arabic, recorded first by the actor;
  - the picture prompt says only "speaks one quick breathless sentence";
  - the lip-sync is driven by the recording;
  - the subtitle is COMP.
- **Geography (file 03):** the river is at frame right, the parapet at frame left, and the runners come toward camera.
- **Light logic:** the scene's key is the torch, the launch lamp and the projection's glow. The jackal's red line is the only saturated red on the parapet.

**The grammar closes in 07.09.007** (not written here): Nour stops dead (an MCU, reaction), the report rolls away across the water (the sound tail), and the cart stops with one wheel over the lip of the quay.

**The same three shots as 03b JSON Lines** (validated with Python's `json` module):

```jsonl
{"id": "07.09.004", "scene": "EXT. KARNAK, RIVER LANDING - NIGHT", "duration_s": 6, "shot": "MS tracking, anamorphic 40mm, subtle handheld", "move": "camera backs away at running pace ahead of Rami (dolly back)", "in_frame": "RAMI (CHAR_RAMI_B2); NOUR (CHAR_NOUR_B2, background, soft); PROP_HAND_CART with PROP_KARNAK_BLOCK", "action": "Rami shoves the loaded hand-cart along the quay toward camera, grinning, and speaks one breathless line; Nour runs behind him, out of focus.", "dialogue": "RAMI (in Egyptian Arabic; subtitled; breathless): \"I've driven a microbus down Faisal Street. This is nothing.\"", "sound": "cart wheels thundering on stone flags, Rami's ragged breath, the projection's deep hum across the water, water slapping the quay", "prompt": "Medium tracking shot, anamorphic 40mm lens, subtle handheld: the camera backs away at running pace ahead of a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker, wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape, sandstone dust, the right sleeve torn at the elbow, keeping him the same size in frame as he shoves a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, along the quay toward camera, grinning through ragged breaths as he speaks one quick breathless sentence; behind him, soft and out of focus, a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket, runs after him. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars, and a warm white-gold glow from a giant projection washing the sky behind them. Mood: reckless joy riding on fear. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.", "negative": "cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, sepia desert filter, yellow colour cast, orientalist bazaar, fez, snake charmer, belly dancer, camels in city streets, old-Hollywood Egypt, Arabian Nights styling, readable Arabic signage, Rami without glasses, beard, splint on the right hand, more than one block on the cart, daylight, crowds", "refs": ["CHAR_RAMI_A_front", "CHAR_RAMI_A_34", "CHAR_RAMI_B_full", "CHAR_NOUR_B_full", "PROP_HAND_CART", "PROP_KARNAK_BLOCK", "LOC_KARNAK_QUAY_NIGHT"], "flags": ["COMP"], "continuity": "Rami: splint on LEFT hand (since 3.6), right sleeve torn (Seq 7 L2), notebook inside the windbreaker (unseen; Tut takes it after 07.09.007). Nour: sleeves still dry (they get wet only when she tips the cart). The projection is still running (7.3). Comp: Arabic-line subtitle, lower third, from the line's in-point to out-point."}
{"id": "07.09.005", "scene": "EXT. KARNAK, RIVER LANDING - NIGHT", "duration_s": 4, "shot": "MS low angle, anamorphic 50mm, locked-off", "move": "none (locked-off)", "in_frame": "UNIT_JACKAL x1", "action": "A jackal lands silently on the Corniche parapet (frame left), freezes, its red line tightens, and it fires across frame to the right, away from the lens.", "dialogue": "", "sound": "one soft pad-tap on stone; a single sharp suppressed crack; no music", "prompt": "Medium low-angle shot, anamorphic 50mm lens, locked-off, looking up at the top of a low stone parapet wall across the upper left of frame, where a lean armed quadruped robot, 0.9 metres at the shoulder, matte black like burnt carbon, deep-chested and narrow-waisted with long thin legs, reverse-jointed rear legs and small padded feet; a narrow elongated snout-like sensor head carrying one thin red horizontal light line; a slim weapon module built flush along its spine, muzzle forward; unmarked, fast and silent, lands without a sound, freezes with one forefoot raised and its red line narrowing and brightening, then goes rigid as a small muzzle flash shows at its spine and it fires across frame toward the right, away from the camera. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: silent, procedural, utterly calm. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.", "negative": "cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, robot with a face, eyes or mouth, human skin on a robot, chrome robot, glossy consumer plastic, yellow or hazard-striped robot, numbers or logos on a robot, boxy commercial robot dog, white consumer camera drone, sparks and cables spilling like blood, robot posing or growling, weapon facing camera, muzzle toward the lens, laser beam, tracer fire, visible projectile, second robot, people in frame", "refs": ["UNIT_JACKAL", "LOC_KARNAK_QUAY_NIGHT"], "flags": ["VFX-ASSIST"], "continuity": "Jackal D0 (clean). Parapet at frame left, fire toward frame right (file 03 geography lock for LOC_KARNAK_QUAY). VFX-ASSIST: if the generator will not render the muzzle flash, generate the rigid firing pose and add a 2-frame flash at the spine in comp; the round's path is never shown."}
{"id": "07.09.006", "scene": "EXT. KARNAK, RIVER LANDING - NIGHT", "duration_s": 4, "shot": "MS at cart height, anamorphic 40mm, subtle handheld", "move": "camera continues backing away (same move as 07.09.004)", "in_frame": "RAMI (CHAR_RAMI_B2); PROP_HAND_CART with PROP_KARNAK_BLOCK", "action": "Sparks burst off the cart's steel handle beside Rami's splinted hand; he drops instantly out of the bottom of frame behind the cart; the cart rolls on alone toward camera.", "dialogue": "", "sound": "the spark's hard metallic ping; the cart's wheels rolling on without him; the report rolling away across the water begins here and tails into 07.09.007", "prompt": "Medium shot at the height of the cart, anamorphic 40mm lens, subtle handheld, the camera still backing away: a bright burst of sparks flies off the steel handle of a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles, loaded with a single sandstone block, lashed with rope, right beside the splinted left hand of a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker, wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape, sandstone dust, the right sleeve torn at the elbow, who drops instantly down and out of the bottom of frame behind the cart, and the cart rolls on alone toward camera and slows. Setting: a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it, at night. Lighting: blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars. Mood: sudden and unadorned, no spectacle. Photorealistic live-action feature film footage, real human actors wherever people appear, natural skin texture with visible pores and fine imperfections, faces, costumes and sets matching the reference images, real physical locations lit by practical, motivated light sources, shot on a large-format digital cinema camera with anamorphic lenses, oval bokeh and gentle edge falloff, 1920x1080, 16:9 full frame with no letterbox bars, 24 frames per second with natural motion blur, fine organic film grain, restrained cinematic colour grade.", "negative": "cartoon, anime, illustration, painting, concept art, CGI look, 3D render, video-game graphics, plastic or waxy skin, airbrushed skin, beauty filter, uncanny face, face morphing, identity drift, changing facial features, duplicated faces, extra fingers, fused fingers, deformed hands, extra limbs, distorted anatomy, warped or bending architecture, melting objects, flickering textures, jitter, strobing, time-lapse, sped-up motion, readable text, subtitles, captions, watermark, logo, brand name, lettering on clothing or vehicles, readable signage, numbers on screens, letterbox bars, black bars, split screen, frame borders, blood, gore, open wounds, corpse, severed body parts, exposed organs, weapon pointed at the camera, muzzle facing the lens, robot touching a child, nudity, celebrity likeness, famous actor, real politician, real commercial robot model, yellow robot dog, cyberpunk neon, holograms, fisheye distortion, heavy vignette, oversharpening, sepia desert filter, yellow colour cast, orientalist bazaar, fez, snake charmer, belly dancer, camels in city streets, old-Hollywood Egypt, Arabian Nights styling, readable Arabic signage, pained expression, face contorted, body on the ground, falling toward the camera, slow motion, wound, stain on clothing", "refs": ["CHAR_RAMI_A_front", "CHAR_RAMI_B_full", "PROP_HAND_CART", "PROP_KARNAK_BLOCK", "LOC_KARNAK_QUAY_NIGHT"], "flags": ["VFX-ASSIST", "EXTEND:07.09.004"], "continuity": "Generated from the LAST FRAME of 07.09.004 (same move, same take); 07.09.005 is intercut, which hides the time jump. After this shot Rami is dead (kill grammar; never shown on the ground in this scene until Tut kneels by 'a still yellow shape in the shadow'). The cart keeps rolling and stops with one wheel over the lip in 07.09.007, where Nour's reaction and the sound tail complete the grammar."}
```

---

## 12. THE SEVEN-STEP CONSISTENCY WORKFLOW

**Reference stills → character sheets → location plates → image-to-video → continuity check → upscale → grade.** Each step has a gate. Nothing passes a gate without the lead's approval.

**Step 1 — Reference stills (the design anchors)**
- **Input:** the reference-still prompts in files 01 (characters), 02 (units and machines), 03 (plates, step 3) and 04 (props).
- **Do:**
  - Use one image model for the whole film (a tool lock).
  - Generate 4–8 candidates per still and approve one.
  - Freeze it as a lossless PNG named by its still id: characters per file 01 (`CHAR_NOUR_A_front.png`), units `<TOKEN>_REF_A.png` / `_REF_B.png` (file 02), props `<TOKEN>_REF.png` (file 04), plates `LOC_<TOKEN>_<VARIANT>_plate.png` (file 03). The master token list is `00_INDEX.md`.
  - Log the model, version, seed, prompt and date.
- **Gate:** the lead's approval; the Egyptologist's sign-off on period dress, props and inscriptions; a likeness check (no resemblance to any celebrity or public figure).

**Step 2 — Character sheets and asset sheets**
- **Do:**
  - For each locked face (at most 12, bible §6), assemble: front, three-quarter, profile, a full body per wardrobe code, and two expressions (file 01 §0.7).
  - Derive child Tut and the 1336 Akhenaten by image-editing the parent stills, never from text.
  - Units: render 3D-asset turnarounds that match REF A (bible §14.4); they drive video-to-video guidance.
  - Optionally, train a per-character LoRA on 20–30 approved stills (open models only; all faces are synthetic).
  - Build the **lock library** (`locks.json`: every LONG, SHORT, wardrobe, damage, overlay, add-on, variant, grade and negative phrase from files 01–05). It is used to assemble and derive prompts (§5.5).
- **Gate:** identity holds across every angle and wardrobe state.

**Step 3 — Location plates**
- **Do:**
  - Generate file 03's plate prompt once per lighting variant needed; approve; save as `LOC_<TOKEN>_<VARIANT>_plate.png`.
  - Derive coverage plates (the reverse, left, right and a surface insert) and state plates (WALL_BROKEN, W0–W3, CASES_SMASHED and the rest) by image-editing the approved plate.
  - Make clean plates for every VFX-EXTEND set.
- **Gate:**
  - the geography lock holds (screen direction, where the sun and the river are);
  - no legible text;
  - the facts match the research (dimensions, materials, orientation).

**Step 4 — Image-to-video**
- **Do:**
  - **Compose the first frame:** inpaint the approved character still(s) into the location plate at the shot's framing, in the right look code (wardrobe, damage level, overlays) and light-matched to the variant.
  - Generate the clip with the derived motion prompt (§5.5) and the NEGATIVE. Take 3–6 takes and pick one.
  - Chain EXTEND children from last frames (§8).
- **Tool lock:** never switch tool or model version inside a scene (bible §14.1).
- **Log per take:** shot id, take number, tool, model/version, seed, duration, motion and guidance settings, the first-frame file, the motion prompt, a prompt hash.
- **Naming:** `SS.CC.NNN_tNN.<ext>`.
- Text-to-video (no principal face) uses the master PROMPT.

**Step 5 — Continuity check (QC)**
- **Check every take against the shot's `Continuity:` line and the bible's §12 state board:**
  - [ ] **Identity:** a face-embedding similarity score against the front still, at or above the lead's threshold; the anchors present (Tut's neck seam; Nour's glasses on their cord; Fathi's red scarf; Rami's glasses; Adaeze's round tortoiseshell glasses).
  - [ ] **Look code:**
    - wardrobe and damage level;
    - injuries on the right side (Rami's LEFT-hand splint; Adaeze's LEFT trouser leg);
    - glow state (G0/G0f/G1/G2) and seams cracked (left wrist 9.4, left knee 10.4, neck 12.3);
    - nape port or scar;
    - props in the right hand;
    - Tut's ceramic LEFT foot.
  - [ ] **Geography:** screen direction, eyelines, the 180° line.
  - [ ] **Light logic:** the named key light is present; unit colours are correct; nothing but the three sources in the Hall.
  - [ ] **Text leakage:** no readable letters, numbers or logos anywhere.
  - [ ] **Anatomy:** hands, fingers, teeth (overbite, chipped tooth), feet.
  - [ ] **Faces:** no more than two principal faces clear.
  - [ ] **Safety:** kill grammar, remains, minors, weapons (§7).
  - [ ] **Motion:** no morphing, melting, sped-up motion or letterboxing.
- **Fix:** another take; an inpaint or face-unification pass (bible §14.1); or a new first frame.

**Step 6 — Upscale and conform**
- Denoise first (strip the generated grain).
- Temporal upscale to **1920 × 1080** where a tool generated below it.
- Conform to **24 fps**. Prefer tools and settings that generate natively at 24. For 25 or 30 fps output, use motion-compensated conversion and re-check faces; never frame-blend.
- Deflicker. Stabilise only handheld the prompt did not ask for.
- **Reject letterboxed takes rather than crop them**: cropping throws away resolution.
- Deliver a 10-bit intra-frame mezzanine file.

**Step 7 — Composite and grade**
- **Composite first:**
  - COMP overlays: text, glyphs, glow, slits, sun, projections;
  - VFX-EXTEND and VFX-ASSIST elements;
  - lip-sync (§9).
- **Then:**
  - conform the edit;
  - grade by scene with the GRADE tokens (§3), shot-matching within each scene;
  - protect skin and unit colours (§3.3);
  - add one grain pass per era, and halation where the grade calls for it.
- **Deliver** with C2PA content credentials on every exported file (bible §14.6), and with the required opening and closing cards: "All modern characters and events are fictional. Imagery generated with AI." (bible §0).

---

## 13. SPECIAL GRAMMARS

### 13.1 Read-from-glass (the First Time 3.3; the Amarna memory 9.5a–c)
- Generate plates and clips **clean**, with the grade phrase for the era (GRADE_FIRST_TIME, GRADE_1336 or GRADE_1332_NIGHT). Post adds GRADE_READ_FROM_GLASS (§3.2).
- **The way in** (seq_03): "Green light floods the ceiling, then blue streaks too fast to follow." This is a light-only transition in comp, from the laser through the scarab to the first frame of the vision.
- **The way out:** a WHITE frame (seq_03), then the lab.
- **Each "Stutter."** in the screenplay is a hard cut with a 2-frame hold and a blue streak across the cut.
- **Memories are locked-off frames** (§4.4). The child and the period faces are derived stills (file 01).

### 13.2 The painted lure (the end of 3.3: "The image BREAKS into an EGYPTIAN PAINTING")
- **Shot as a real painted surface, never as a cartoon.** It is a photoreal plaster wall painted in the flat Egyptian manner, filmed under a soft raking light with a slow camera move. The paint never animates.
- **Plate prompt:**
  > Photoreal close still of an ancient Egyptian wall painting on smooth white plaster, flat unshaded colour in red ochre, yellow ochre, black, white and deep blue with thin black outlines: a dark hall shown as a broad band of black; a tall black balance with two pans; on the left pan, a small vessel-shaped heart sign drawn inside a container of translucent green; beside it a blank vertical column where signs are yet to be written; the plaster faintly cracked and lit by a soft raking light. Real paint on a real wall, not an illustration. Aspect ratio 16:9.
- **The break:** the last photoreal frame and the painting share one composition (the balance in the same place). The break itself is a comp effect: a crack of light, the image flattening into paint. It is designed with the VFX lead and never generated as a morph.
- The column of signs ("whoever would ascend must first be weighed") is COMP, drawn by the Egyptologist. Tut whispers the line in the lab.
- Apply GRADE_READ_FROM_GLASS steps 1–3 only.

### 13.3 SESHAT's feed, screens and the glyph
- **Every broadcast image in the film is SESHAT's own feed** (bible §7, 5.1): the underlying footage is an ordinary plate (the stadium aerial, the warehouse, the street), with the glyph (file 02 §8.1) and white type laid over it in comp. No real outlets, anchors, chyrons or logos.
- **Screens in plates:** "a dark screen glowing faintly with abstract lines". Never text.
- **Control rooms:** abstract diagrams only (LOC_CONTROL_ROOMS). They go dark; they are never physically damaged.

### 13.4 The 40-metre projection (Karnak, 7.3)
- **Performance:** generate Akhenaten's recital as locked-face clips (CHAR_AKHENATEN, look A): MCU, frontal, even soft light, against black, 8 s pieces. Lip-sync to the recorded line in the language the screenplay tags.
- **Plate:** LOC_KARNAK_RAM_AVENUE_PROJECTION, with the pylon face lit by a moving white-gold wash so that the stone, the rams and the small figures below take the light.
- **Comp:**
  - map the performance onto the pylon;
  - let the stone's texture modulate the brightness;
  - add slight keystone and rolling brightness;
  - spill onto the Hypostyle columns (LOC_KARNAK_HYPOSTYLE_PROJECTION);
  - add a trembling reflection in the Sacred Lake (LOC_KARNAK_SACRED_LAKE_PROJECTION).
  How the figure crosses the two towers and the gateway gap is §14 Q4.
- **Eyelines:** the people below look up and to frame right, high.
- The nurses and bracelets inside the broadcast are a separate plate (adult wrists only, `NEG_GARDEN`) framed in the feed.

### 13.5 The archive half-marathon (main titles, 1.6)
- LOC_ROBOT_HALF_MARATHON_ARCHIVE + GRADE_ARCHIVE_2025. Generate with the normal suffix, then degrade in post (§3.2).
- **The robots** are early, awkward, unbranded humanoids with exposed joints and plain grey shells, never a real model: paste UNIT_EARLY_HUMANOID (file 02 §14.5).
- **The falls are comic:** one pitches flat at the gun; one walks into a barrier and takes its handler down, and the handler gets up laughing (show him up again).
- No legible bibs, banners or skyline (file 03, entry 55).

### 13.6 The 1925 flash and the match cut (1.3 → 1.5)
- Generate the photographer's flash as LOC_KV15_LAB_1925_FLASH (1–2 frames).
- The edit: the flash, 2 pure white frames (comp), then 1.5 opens on the gantry projector's white burst settling into LOC_GEM_CC_READING.
- **Matched compositions:** the lamp's position in 1925 = the projector ring in 2033; the table's axis = the cradle's axis.
- Sepia (GRADE_1925) cuts to cool LED (GRADE_2033_MUSEUM) on the white.

### 13.7 Cards, SUPERs and subtitles (typography; all COMP)
- **Subtitles:** a clean humanist sans-serif, white with a thin dark edge, lower third, at most two lines of about 42 characters. Mouthed lines in italics (§9.6).
- **SUPERs** (place, date, time: "THEBES. c. 1323 BC", "03:00", "05:20"): small, restrained, in the same family, lower left.
- **Hour cards** (Act III): the English card beside the hieroglyph for "hour" (bible §5), drawn by the Egyptologist from research 09's palette.
- **Title:** HERE AM I, blooming from the glyph (seq_01).
- **Required cards:** "All modern characters and events are fictional. Imagery generated with AI." (bible §0).
- The typeface is chosen by the lead and cleared for licence; it is not named here.

### 13.8 The muon vision (main titles)
- **This is not generated video.** Build it in 3D from the interior geometry in file 03 (the Great Pyramid entries): a rain of particle tracks, the pyramid building out of them passage by passage, and the Grand Gallery "a long bright blade".
- The Big Void is a dark blade at least 30 m long above the Gallery that "will not resolve" [07 B2].
- Render it in the film's grade and composite it as COMP.

### 13.9 Light elements carried on bodies and machines
Plates carry the neutral phrase; comp carries the exact colour and timing:
- the chest glow G0 / G0f / G1 / G2 (file 01 table: colours and pulse);
- the slits' single brightening (file 02 §0.1, §1);
- the seam cracks (file 01);
- the thread's leaks (file 02 §14.1);
- the feather-light and the clouding (file 02 §13).

---

## 14. OPEN QUESTIONS (style and grammar) — for the lead

1. **Prompt budget.** 03b says 70–120 words; with verbatim locks, master prompts run 180–360 words (§11). Proposal: apply the 03b figure to the writer's own words plus SHORT locks; leave the master PROMPT uncapped; send the derived motion prompt (at most 1,500 characters) to image-to-video tools (§5.3, §5.5). Amend 03b if agreed.
2. **The launch's red wheelhouse lamp** (file 04 L1; file 03 LOC_KARNAK_QUAY_NIGHT) sits against "red = the military stack" (file 02 §0.1). Proposal: keep it a dim, broad glow (never a line), or change it to a dim amber-white. The lead to rule before Seq 6–7 plates.
3. **1925 sepia:** in post from colour generations (preferred, §3.2), or prompted? The lead to confirm after tests.
4. **The Karnak projection's composition** across the First Pylon's two towers and the gateway gap. The VFX lead and the lead to decide (§13.4).
5. **Tomas's sparks in the Hall** break the three-source rule for 2–4 frames (file 03 Q14). Confirm.
6. **The 1332 BC Hall** uses the screenplay's own three lights (the lamp, the god's glow, the heart), mirroring the 2033 rule (file 03). The cross-check reworded the god's glow as the coiled glass core on a sledge, because the 8 m disk cannot pass the pyramid's passages (file 02 Q10). Confirm the rhyme and the ruling.
7. **Recording schedule.** Every Egyptian line must be recorded before its picture is generated (bible §13). If the consultant is not available in time, generate with guide recordings and re-sync later. Confirm.
8. **The face-similarity threshold and tool choices** are set by the lead after a test scene. Tools stay locked per scene.
9. **"Anamorphic" and letterboxing.** Some tools letterbox when they read "anamorphic". Proposal: reject those takes; if a tool letterboxes persistently, allow `spherical lens with anamorphic character` for that tool only, logged.
10. **Generated audio.** Does any generated ambience survive to the final mix, or is all sound rebuilt? The sound lead to rule.
11. **The hour-card sign:** which hieroglyph for "hour". The Egyptologist to choose.
12. **The subtitle and SUPER typeface:** the choice and its licence (§13.7).
