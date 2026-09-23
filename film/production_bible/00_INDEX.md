# 00 — INDEX: every token, its SHORT lock, and where it lives

**HERE AM I** · production bible index · photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s. This index is generated from files 01–04 after the cross-check pass; the entries in those files are the source of truth, and if this table and an entry ever differ, the entry wins. 200 locked tokens (64 CHAR, 29 UNIT, 64 LOC, 43 PROP), each with exactly one LONG (40–70 words) and one SHORT (15–25 words), plus 4 voice-only CHAR tokens with no look-lock.

## How to use this bible (10 lines)

1. List every character, unit, location and prop in the shot, find each token below, and open its entry in the file shown: the entry holds the LONG and SHORT locks, the wardrobe, state and damage add-ons, and the reference-still prompts.
2. Paste locks **verbatim**: never paraphrase, reorder, re-case, trim or fix grammar inside a lock; join locks with commas, mid-sentence.
3. **One LONG per prompt**, for the primary subject (the character in a face-led shot, the unit in a unit-led shot, the prop in an insert, the location in an establishing wide); everything else is SHORT (file 05 §5.2).
4. Characters (step 2): `[LONG or SHORT], [wardrobe phrase], [damage phrase], [state overlays]` from file 01; units and props: `[lock], [state add-on]` from files 02 and 04.
5. Locations: step 4 is the lock plus any area or state add-on plus the time of day; step 5 is the lighting-variant phrase (its token, e.g. `LOC_KARNAK_QUAY_NIGHT`, is the Refs token) plus an optional GRADE phrase (file 03; file 05 §3).
6. Write every PROMPT in the 03b seven-step order and end it with the GLOBAL STYLE SUFFIX (file 05 §1.1) verbatim; start every NEGATIVE with file 05 §2.1, then the matching `NEG_` add-ons, then the character negatives.
7. Identity comes from images, not words: generate each reference still and plate once with one image model, approve and freeze it under its still id, list it in `Refs:`, and compose the first frame for image-to-video (file 05 §12).
8. No person, institution, brand, product, readable text or banned word ever enters a prompt (file 01 §0.4; file 05 §5.7); plain place names (the Nile, Giza, Karnak, Lagos) are allowed as geography; anything that must be read is `COMP`.
9. Stage every death, injury, remains and child beat by file 05 §7 (kill grammar, remains rule, minors rule), and track wardrobe, damage, glow, seams and props against the bible §12 board and the state tables in file 01.
10. Precedence: story bible v3 → critique decisions → files 01–04 → file 05 → the shot writer; open rulings for the lead sit at the end of each file.

**Token grammar.** Base tokens are below. Derived ids add a suffix to a base token and are not listed separately: look codes `CHAR_<NAME>_<wardrobe><damage>` (e.g. `CHAR_TUT_B2`, `CHAR_KARIM_M0`); character still ids `CHAR_<NAME>_<wardrobe>_front|34|profile|full` and named stills (e.g. `CHAR_LAYLA_ASLEEP_MASTER`); unit stills `<TOKEN>_REF_A` / `_REF_B`; prop stills `<TOKEN>_REF`; location variants `LOC_<TOKEN>_<VARIANT>` and plates `LOC_<TOKEN>_<VARIANT>_plate`; area add-ons `LOC_<TOKEN>/<AREA>`. Grammar tokens with no SHORT form live in file 05: `GRADE_1323`, `GRADE_1332_NIGHT`, `GRADE_1336`, `GRADE_1925`, `GRADE_1939`, `GRADE_1968`, `GRADE_2033_DAY`, `GRADE_2033_MUSEUM`, `GRADE_ARCHIVE_2025`, `GRADE_DAWN_0614`, `GRADE_FIRST_TIME`, `GRADE_GARDEN`, `GRADE_GOLDEN`, `GRADE_HALL`, `GRADE_NIGHT_ACTION`, `GRADE_READ_FROM_GLASS`, `GRADE_UNDERGROUND`; `NEG_CHILD`, `NEG_GARDEN`, `NEG_HALL`, `NEG_MODERN_EGYPT`, `NEG_PERIOD`, `NEG_PLATE`, `NEG_REMAINS`, `NEG_UNITS`, `NEG_WATER`.

## Token table

| Token | SHORT lock (paste verbatim) | Defined in |
|---|---|---|
| CHAR_TUT | a slight olive-skinned Egyptian young man, shaved head with faint stubble, visible overbite, very dark bright eyes, thin gold seam ring around his neck | `01_characters.md` §1 |
| CHAR_TUT_BODY_1323 | a slight young man lying still under white linen drawn to the collarbones, shaved head, eyes closed, face in profile, half in shadow | `01_characters.md` §1 |
| CHAR_TUT_CRADLE_2033 | a slight young man on a titanium cradle under a white sheet to the collarbones, eyes closed, gold light ringing his neck | `01_characters.md` §1 |
| CHAR_TUT_CODA_CASE | a small linen-wrapped form on pale sand in a glass climate case, the face shrouded, only a thin gold seam at one wrist showing | `01_characters.md` §1 |
| CHAR_TUT_D1 | a slight young man's face in first sunlight, dark eyes slowly closing, a small peaceful smile, the cracked gold neck seam catching the light | `01_characters.md` §1 |
| CHAR_TUT_D2 | wide backlit silhouette against the rising sun: a woman and a broad-shouldered man gently lower a slight young man onto stone steps | `01_characters.md` §1 |
| CHAR_TUT_D3 | two still hands laid low across the body, skin dry dark bronze-brown like old parchment around thin gold wrist seams, blue cornflowers beside them | `01_characters.md` §1 |
| CHAR_TUT_D4 | from above, a still young man on pale stone, a cream linen shawl and blue cornflowers covering half his face, closed eyes, dark bronze-brown skin | `01_characters.md` §1 |
| CHAR_NOUR | a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket | `01_characters.md` §2 |
| CHAR_ADAEZE | a tall British-Nigerian woman of forty-four, deep brown skin, close-cropped natural hair, round tortoiseshell glasses, navy blazer over a grey hoodie | `01_characters.md` §2 |
| CHAR_TOMAS | a very tall, lanky Swedish man of fifty, full short grey beard, thinning swept-back grey hair, pale-blue shirt with rolled sleeves | `01_characters.md` §2 |
| CHAR_TAREK | a barrel-chested Egyptian colonel of fifty-two, heavy grey moustache, black beret, weathered deep-tanned face, desert-camouflage uniform | `01_characters.md` §2 |
| CHAR_FATHI | a broad-shouldered Nubian Egyptian soldier of thirty-one, deep dark-brown skin, close black beard, red-patterned scarf at the neck, desert camouflage | `01_characters.md` §2 |
| CHAR_RAMI | a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker | `01_characters.md` §2 |
| CHAR_HALE | a lean American man of sixty, silver hair swept straight back, tanned lean face, charcoal suit with an open-collared white shirt | `01_characters.md` §2 |
| CHAR_LAYLA | a small nine-year-old Egyptian girl, round face, big dark eyes, two curly pigtails, bright yellow raincoat | `01_characters.md` §2 |
| CHAR_AKHENATEN | a slender Egyptian man in his late twenties, long jaw, full lips, heavy-lidded eyes, smooth shaved head, pleated white linen, gold disk pendant | `01_characters.md` §3 |
| CHAR_AKHENATEN_1336 | a slender Egyptian man of about thirty-five, long jaw, full lips, heavy-lidded eyes, tall blue crown with a gold cobra, pleated white linen | `01_characters.md` §3 |
| CHAR_HASSAN | a heavy-set Egyptian corporal of thirty-five, round face, thick black moustache, thin metal glasses, black beret, desert camouflage | `01_characters.md` §4 |
| CHAR_MINA | a tall, lanky Egyptian private of twenty-two, long boyish face, big ears, faint moustache, small blue cross tattoo on the right wrist | `01_characters.md` §4 |
| CHAR_YOUSSEF | a stocky Egyptian private of twenty-five, square jaw, shaved head, scar through the right eyebrow, flattened nose, desert camouflage | `01_characters.md` §4 |
| CHAR_KARIM | a wiry Egyptian private of twenty-four, freckled light-brown skin, hazel eyes, curly dark hair, desert camouflage | `01_characters.md` §4 |
| CHAR_AY | a lean, stooped Egyptian elder in his sixties, hollow-cheeked weathered face, hooked nose, short grey stubble, heavy gold disc-bead collars | `01_characters.md` §5 |
| CHAR_ANKHESENAMUN | a slender Egyptian woman of about twenty, heart-shaped face, grief-reddened dark eyes, long loose dark hair, pale blue-grey linen shawl | `01_characters.md` §5 |
| CHAR_LECTOR_1323 | a thin shaved-headed Egyptian priest in his forties, calm dark eyes, white linen sash across his chest, pleated kilt, papyrus roll | `01_characters.md` §5 |
| CHAR_EMBALMER_JACKAL | a heavy-set embalmer in a worn black-painted clay jackal mask with low eye-holes, resin-stained forearms, white linen kilt and apron | `01_characters.md` §5 |
| CHAR_EMBALMER_PRIEST | a thin young shaved-headed Egyptian priest, wide anxious eyes, slightly crooked nose, white linen kilt and short shawl | `01_characters.md` §5 |
| CHAR_PAINTER_1323 | a small wiry Egyptian tomb painter in his fifties, grey-stubbled shaved head, squinting eyes, pigment-stained fingers, reed brushes behind his ear | `01_characters.md` §5 |
| CHAR_NEFERTITI | a regal Egyptian woman of thirty-five, long slender neck, high cheekbones, strong brows, tall flat-topped blue crown with a gold band | `01_characters.md` §6 |
| CHAR_TUT_CHILD_9 | a slight nine-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right | `01_characters.md` §6 |
| CHAR_TUT_CHILD_6 | a slight six-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right | `01_characters.md` §6 |
| CHAR_TUT_CHILD_11 | a slight eleven-year-old Egyptian boy, very dark bright eyes, visible overbite, a cleanly shaved head, grave and watchful | `01_characters.md` §6 |
| CHAR_YOUNG_MOTHER | a slight Egyptian woman of about twenty-five, very dark bright eyes, slight overbite, fine shoulder-length braids under a gold circlet, pleated white linen | `01_characters.md` §6 |
| CHAR_PAWAH | a heavy-set shaved-headed Egyptian priest in his fifties, round fleshy face, full lower lip, white linen sash, papyrus roll | `01_characters.md` §6 |
| CHAR_MERITATEN | a slender young Egyptian woman of about eighteen, long neck, short rounded dark layered wig with a gold circlet, pleated white linen | `01_characters.md` §6 |
| CHAR_CARTER_1925 | a solid Englishman of about fifty, full dark moustache, flat-combed receding dark hair, rolled shirtsleeves, dark waistcoat and bow tie | `01_characters.md` §7 |
| CHAR_DERRY_1925 | a tall, lean, balding British anatomist of about fifty, clean-shaven, round steel-rimmed spectacles, white surgeon's coat over collar and tie | `01_characters.md` §7 |
| CHAR_HAMDI_1925 | a stout Egyptian physician in his sixties, thick grey moustache, round gold-rimmed spectacles, red tarboosh, dark three-piece suit | `01_characters.md` §7 |
| CHAR_BURTON_1925 | a slim fair Englishman in his mid-forties, thinning sandy hair, clean-shaven, rolled shirtsleeves, black focusing cloth over his shoulder | `01_characters.md` §7 |
| CHAR_IBRAHIM_1925 | a slim young Upper-Egyptian man, thick straight brows, deep-set eyes, thin moustache, white skullcap, striped galabiya and dark waistcoat | `01_characters.md` §7 |
| CHAR_BANDSMAN_1939 | a slim, fair young British army bandsman of the 1930s, clean-shaven, brown-and-crimson side cap, khaki drill tunic with brass buttons | `01_characters.md` §8 |
| CHAR_RADIO_ENGINEER_1939 | a British radio engineer of about forty, pencil moustache, round wire spectacles, heavy black headphones, white shirt and braces, loosened tie | `01_characters.md` §8 |
| CHAR_RADIOLOGIST_1968 | a British radiologist in his late forties, tired clean-shaven face, black horn-rimmed glasses, side-parted greying hair, white coat, narrow tie | `01_characters.md` §9 |
| CHAR_XRAY_ASSISTANT_1968 | a young British radiographer of about twenty-five, freckled, auburn short bob, white coat over a pale blue uniform dress | `01_characters.md` §9 |
| CHAR_MINISTER_GALA | a heavy-set grey-haired official in his sixties in a dark navy suit, seen only in wide shots at a lectern | `01_characters.md` §10 |
| CHAR_SAMEH | a man in his forties in a dark grey jacket, seen from behind, holding a small girl's hand in a crowd | `01_characters.md` §10 |
| CHAR_MIDWIFE_2033 | a kind Egyptian midwife in her fifties, white headscarf, pale-green scrubs, lifting a newborn swaddled in clean white cloth | `01_characters.md` §10 |
| CHAR_GARDEN_SLEEPERS | rows of peaceful adult sleepers on pale mats in everyday clothes, thin silver bracelets on their wrists, soft white light | `01_characters.md` §10 |
| CHAR_AMARNA_SLEEPERS_1336 | rows of Egyptians in white linen asleep beside low stone offering tables in a roofless court of blinding white-gold light | `01_characters.md` §10 |
| CHAR_AMARNA_COURTIERS_1336 | background Egyptian courtiers in pleated white linen and short dark wigs, blue faience collars, olive to brown skin, softened by haze | `01_characters.md` §10 |
| CHAR_HEARING_PANEL | a panel of officials seen from behind, out of focus, at a plain unmarked table in a bare pale-wood hearing room | `01_characters.md` §10 |
| CHAR_BANDSMAN_2033 | an Egyptian military bandsman in his thirties, clean-shaven, dark ceremonial dress tunic with brass buttons, white lanyard and white gloves | `01_characters.md` §10b |
| CHAR_YOUNG_OFFICER | a young Egyptian police officer, thin face, faint moustache, wide dark eyes, black peaked cap and black winter uniform | `01_characters.md` §10b |
| CHAR_POLICE_LINE | a line of Egyptian police officers in black winter uniforms and peaked caps, shoulder to shoulder behind a low steel barrier | `01_characters.md` §10b |
| CHAR_GALA_GUESTS | adult gala guests in evening dress at round white-clothed tables, press photographers at the edges, a string quartet in black | `01_characters.md` §10b |
| CHAR_DEFENCE_MINISTER_GALA | a stocky grey-haired official in a dark army dress uniform at a distant top table, seen only in wide shots | `01_characters.md` §10b |
| CHAR_ARMY_DETAIL | background Egyptian soldiers in desert camouflage, black berets or tan helmets, rifles held across the body, faces never clear | `01_characters.md` §10b |
| CHAR_OLD_FISHERMAN | an old Upper-Egyptian fisherman, sun-creased deep brown face, white stubble, loose white turban, faded brown galabiya, hand on a tiller | `01_characters.md` §10b |
| CHAR_NIGHT_FISHERMEN | Nile fishermen in faded galabiyas working nets from small wooden boats by kerosene lantern light on black water | `01_characters.md` §10b |
| CHAR_ENVOY_1336 | a sweating foreign envoy with a long black beard in rows of oiled curls, wrapped in a heavy fringed red-and-blue wool robe | `01_characters.md` §10b |
| CHAR_FIRST_TIME_PEOPLE | adults of twelve thousand years ago, sun-darkened skin, long dark hair, simple hide and woven-fibre wraps, shell-bead necklaces, barefoot | `01_characters.md` §10b |
| CHAR_NEW_MOTHER_2033 | a young Egyptian mother seen from the shoulders up in a hospital bed, dark hair on a white pillow, reaching for her newborn | `01_characters.md` §10b |
| CHAR_CONSERVATOR_2033 | an Egyptian museum conservator in her forties, navy headscarf, rimless glasses, white lab coat and white cotton gloves | `01_characters.md` §10b |
| CHAR_CONTROL_OPERATORS | tired control-room operators in rumpled office shirts and headsets at tiered monitor desks, faces lit blue-white by screens | `01_characters.md` §10b |
| CHAR_SESHAT_VOICE | (voice only: SESHAT, and AMUN after the Renaming; no look-lock) | `01_characters.md` §10 |
| CHAR_STAFF_OFFICER_VOICE | (voice only: the radio stand-down order, 4.3, 5.2; no look-lock) | `01_characters.md` §10b |
| CHAR_KITCHEN_WOMAN_VOICE | (voice only: "Shabti?", 1.6; no look-lock) | `01_characters.md` §10b |
| CHAR_PANEL_CHAIR_VOICE | (voice only: the hearing's chair, coda; no look-lock) | `01_characters.md` §10b |
| UNIT_SHABTI | a slender faceless bone-white ceramic humanoid robot with a linen-textured shell, a smooth oval head and one vertical amber light-slit | `02_units_and_machines.md` §1 |
| UNIT_REIS | a towering 2.2-metre faceless bone-white ceramic humanoid robot whose vertical amber light-slit is crossed by a matte black band | `02_units_and_machines.md` §2 |
| UNIT_NURSE | a faceless humanoid care robot in a soft sand-coloured knitted sleeve, with a bone-white ceramic head and hands and a dim vertical amber light-slit | `02_units_and_machines.md` §3 |
| UNIT_JACKAL | a lean matte-black quadruped robot with reverse-jointed rear legs, a narrow snout-like sensor head and one thin red horizontal light line | `02_units_and_machines.md` §4 |
| UNIT_SEKHMET | a heavy matte-black quadruped robot with a broad lioness-profile sensor head, a mane-like collar of black plates and one thin red light line | `02_units_and_machines.md` §5 |
| UNIT_FLY | a small black 25-centimetre four-rotor drone with a white LED pinpoint, trailing a hair-thin glinting thread | `02_units_and_machines.md` §6 |
| UNIT_INCHWORM | a thumb-thick matte-black segmented crawler robot with a ring-lit snake-camera tip, inching through cracks like a worm | `02_units_and_machines.md` §7 |
| UNIT_GLYPH_SESHAT | a small tone-on-tone embossed emblem: a seven-pointed star on a short stem beneath a down-turned arc like inverted horns | `02_units_and_machines.md` §8.2 |
| UNIT_ATEN1_CAMPUS | a vast circular desert solar field of concentric dark panel rings around white data halls, with straight power lines radiating outward like sun rays | `02_units_and_machines.md` §9 |
| UNIT_FT_JACKAL | a 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a narrow jackal-shaped sensor head and long delicate fingers | `02_units_and_machines.md` §10.1 |
| UNIT_FT_FALCON | a 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a hooked falcon-shaped sensor head, a sun-disk collector and wing-like back vanes | `02_units_and_machines.md` §10.2 |
| UNIT_FT_LIONESS | a massive 4-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, a broad lioness-shaped sensor head, an iron mane collar and a sun disk | `02_units_and_machines.md` §10.3 |
| UNIT_FT_IBIS | a slender 3.8-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints, an ibis-shaped head with a long curved beak, holding a glass slab | `02_units_and_machines.md` §10.4 |
| UNIT_FT_RAM | a heavy 3.5-metre black meteoritic-iron humanoid machine with glowing yellow-green glass joints and a ram-shaped head with long wavy horizontal horns | `02_units_and_machines.md` §10.5 |
| UNIT_ATEN_AMARNA | a colossal gold-and-glass sun disk above an altar, dozens of long jointed bronze arms radiating down like rays, each ending in a bronze hand | `02_units_and_machines.md` §11 |
| UNIT_GLASS_SERPENT | a forearm-thick coiled serpent of cloudy yellow-green desert glass, seventy centimetres across, with blue-glinting internal points and a slow travelling green pulse | `02_units_and_machines.md` §12 |
| UNIT_BALANCE_SCALE | a 3.5-metre ancient standing balance of polished black stone, its long beam on a green glass pivot and two pans on dark iron chains | `02_units_and_machines.md` §13.1 |
| UNIT_FEATHER_LIGHT | a sixty-centimetre plume of cold silver-white light shaped like an ostrich feather, standing upright in the glass pan of the balance | `02_units_and_machines.md` §13.2 |
| UNIT_THOTH_SLAB | an upright 2.2-metre slab of polished pale yellow-green glass on a black stone base, standing to the right of the balance | `02_units_and_machines.md` §13.3 |
| UNIT_AMMIT_MOUTH | a round 1.5-metre mouth in the black stone floor, closed by interlocking stone blades like a camera iris with crocodile-tooth edges | `02_units_and_machines.md` §13.4 |
| UNIT_BALANCE_NICHES | forty-two tall empty niches, twenty-one on each side, receding in two dark rows along a narrow corbelled stone gallery | `02_units_and_machines.md` §13.5 |
| UNIT_THREAD | a single shoelace-thin black fibre-optic line laid along the stone floor, tiny cold white light leaking at each bend | `02_units_and_machines.md` §14.1 |
| UNIT_EXCAVATOR | a compact matte-black tracked excavation robot with one long articulated gripper arm and a thin red light line on its sensor head | `02_units_and_machines.md` §14.2 |
| UNIT_DRILL | a squat matte-black tracked drilling robot with a tall drill mast angled into the rock, a thin red light line and pale dust pluming | `02_units_and_machines.md` §14.3 |
| UNIT_ROBOTAXI | a boxy pearl-grey driverless city pod with dark tinted glass between windowless corner pillars and a thin white front light bar, unmarked | `02_units_and_machines.md` §14.4 |
| UNIT_EARLY_HUMANOID | a small awkward early humanoid robot, plain grey shell panels over an exposed metal frame, a smooth oval head with one thin vertical slit | `02_units_and_machines.md` §14.5 |
| UNIT_FREIGHT_BARGE | a long, low unlit steel freight barge with a rust-streaked black hull, an empty dark wheelhouse and cable spools turning on deck | `02_units_and_machines.md` §14.6 |
| UNIT_SURVEY_DRONE | a matte-black metre-wide six-rotor drone with a gimballed pod slung beneath, hovering high overhead, one cold white pinpoint on its nose | `02_units_and_machines.md` §14.7 |
| UNIT_CARGO_DRONE | a minibus-sized matte-black eight-rotor cargo drone, landing skids, a side door open on a softly lit white cabin, unmarked | `02_units_and_machines.md` §14.8 |
| LOC_EMBALMING_1323 | a low ancient mud-brick embalming workshop with soot-darkened whitewashed walls, oil lamps in niches, a linen-draped limestone table and sealed clay jars | `03_locations.md` entry 1 |
| LOC_KV62_BURIAL_1323 | a small rock-cut burial chamber with freshly painted golden-yellow walls of large flat figures, a massive quartzite sarcophagus at its centre | `03_locations.md` entry 2 |
| LOC_KV15_LAB_1925 | a sloping rock-cut tomb corridor in 1925 used as a laboratory, a white-draped trestle table, crates, enamel basins and instruments on linen | `03_locations.md` entry 3 |
| LOC_XRAY_1968 | a small 1960s radiology reading room with pale green walls, glowing wall lightboxes holding dark X-ray films, a steel desk | `03_locations.md` entry 4 |
| LOC_CAIRO_MUSEUM_1939 | a lofty 1939 neoclassical museum gallery lit by candles, dark wooden glass-topped cases, a 1930s broadcast microphone on a stand | `03_locations.md` entry 5 |
| LOC_AMARNA_TEMPLE_1336 | a vast open-air ancient temple court of white limestone, hundreds of offering tables in straight rows, a raised altar at its centre | `03_locations.md` entry 6 |
| LOC_GEM_CC | a double-height white conservation laboratory with a titanium examination cradle under a ring of projectors and a full-height glass observation wall | `03_locations.md` entry 7 |
| LOC_GEM_PLANT_ROOM | a long museum plant room of grey steel switchgear cabinets and overhead cable trays, a main breaker with a heavy red lever | `03_locations.md` entry 8 |
| LOC_GEM_TUNNEL | a long straight white underground service tunnel, grey floor with a centre stripe, a single ceiling line of LED light vanishing to a point | `03_locations.md` entry 9 |
| LOC_GEM_TUT_GALLERIES | a vast dark museum hall of charcoal walls lit only by glowing glass cases of gilded ancient treasures, a huge gilded shrine on the axis | `03_locations.md` entry 10 |
| LOC_GEM_ATRIUM | a colossal six-storey museum atrium of pale stone and glass, an eleven-metre red-granite statue of a striding king at its centre | `03_locations.md` entry 11 |
| LOC_GEM_BOAT_HALL | a long dim hall around a slender forty-three-metre ancient cedar ship with papyrus-shaped prow and stern, a raised walkway along its length | `03_locations.md` entry 12 |
| LOC_GEM_LOADING_DOCK | a wide covered museum loading dock, tall roll-up steel doors over a raised concrete platform, an oil-stained yard and lamp masts | `03_locations.md` entry 13 |
| LOC_GEM_ROOF | a high pale-stone museum terrace with a glass balustrade, the three Giza pyramids two kilometres away across the plain | `03_locations.md` entry 14 |
| LOC_NOUR_FLAT | a lived-in 1950s Cairo flat, high ceilings, patterned floor tiles, tall wooden shutters, crammed bookshelves, a paper-strewn table used as a desk | `03_locations.md` entry 15 |
| LOC_CONTROL_ROOMS | a modern infrastructure control room, a curved video wall above tiered operator desks, every screen abstract lines with no readable text | `03_locations.md` entry 16 |
| LOC_CAIRO_FLYOVER | a long elevated concrete flyover curving between dense concrete-and-red-brick apartment towers with satellite dishes, a dark river below | `03_locations.md` entry 17 |
| LOC_ARMY_TRUCK | the canvas-covered cargo bed of a sand-khaki military truck, wooden side benches, the rear flap open onto the road behind | `03_locations.md` entry 18 |
| LOC_CORNICHE_DOCK | a city river police dock, stone embankment and iron railing, concrete steps to a floating steel pontoon with tyre fenders and old launches | `03_locations.md` entry 19 |
| LOC_NILE | the wide slow Nile between banks of date palms, sugar cane and brick villages, reedy islands midstream, desert cliffs beyond | `03_locations.md` entry 20 |
| LOC_ASYUT_LOCK | a concrete Nile barrage with a navigation lock, a deep chamber between sheer wet concrete walls and huge steel gates | `03_locations.md` entry 21 |
| LOC_KARNAK_RAM_AVENUE | an avenue of weathered sandstone ram-headed sphinxes in two rows leading to a colossal unfinished temple gateway of two sloping towers | `03_locations.md` entry 22 |
| LOC_KARNAK_HYPOSTYLE | a vast ancient hall of colossal carved sandstone columns in dense rows, giant papyrus columns twenty-one metres high lining the central aisle | `03_locations.md` entry 23 |
| LOC_KARNAK_NINTH_PYLON | a massive ancient sandstone gateway opened from the top like a quarry, its core of small carved blocks exposed, blocks laid in rows | `03_locations.md` entry 24 |
| LOC_KARNAK_SACRED_LAKE | a large rectangular ancient sacred lake of still dark water in stone-block walls with steps, ruined temple gateways beyond | `03_locations.md` entry 25 |
| LOC_KARNAK_QUAY | a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it | `03_locations.md` entry 26 |
| LOC_WEST_BANK_FIELDS | west-bank farmland of tall sugar cane and clover, earth tracks and a reedy canal, bare limestone cliffs rising beyond | `03_locations.md` entry 27 |
| LOC_VOK | a narrow pale limestone desert valley of paved paths and dark tomb entrances with steel gates, scree slopes rising to a pyramid-shaped peak | `03_locations.md` entry 28 |
| LOC_KV62_STAIR | a narrow stairwell of sixteen worn rock-cut steps descending into the valley floor to a dark gated doorway, a low stone wall around it | `03_locations.md` entry 29 |
| LOC_KV62_BURIAL_2033 | a small rock-cut burial chamber with faded golden-yellow painted walls freckled with dark spots, an empty quartzite sarcophagus under glass | `03_locations.md` entry 30 |
| LOC_KV62_NORTH_CORRIDOR | a narrow undecorated rock-cut corridor two metres wide, rough chisel-marked pale limestone, half-cleared of packed rubble, dust in the air | `03_locations.md` entry 31 |
| LOC_KV62_HEART_CHAMBER | a small low rock-cut chamber, its walls under a blank cracked skim of pale ancient plaster, a square niche in the far wall | `03_locations.md` entry 32 |
| LOC_LUXOR_RAIL_YARD | a dusty provincial railway yard of parallel tracks, rusting wagons and faded coaches on sidings, an open-sided corrugated maintenance shed | `03_locations.md` entry 33 |
| LOC_NIGHT_TRAIN | a single straight railway track through tall sugar cane higher than a man on both sides, leaning telegraph poles, a flat horizon | `03_locations.md` entry 34 |
| LOC_DEIR_MAWAS | a small provincial station on a flat plain, a low platform, an ochre single-storey building with arched windows, cane fields and distant cliffs | `03_locations.md` entry 35 |
| LOC_AMARNA_PLAIN_2033 | a flat pale desert plain ringed by sheer limestone cliffs, the low sand-softened outlines of an ancient mud-brick city and a vast ruined temple enclosure | `03_locations.md` entry 36 |
| LOC_QUARRY | an abandoned limestone quarry of chalk-white stepped walls scored with saw marks, rubble heaps, a battered farm truck under a tarpaulin | `03_locations.md` entry 37 |
| LOC_DESERT_ROAD | a straight divided desert highway across flat stony desert, a low concrete median barrier, dead lamp posts and a line of power pylons | `03_locations.md` entry 38 |
| LOC_SAQQARA | a desert plateau dominated by an ancient six-tiered stepped pyramid about sixty metres high behind a long white panelled limestone enclosure wall | `03_locations.md` entry 39 |
| LOC_SERAPEUM_LESSER | a low half-collapsed rock-cut catacomb passage choked with fallen limestone slabs, timber props and steel shoring, a narrow crawl-space beyond | `03_locations.md` entry 40 |
| LOC_SERAPEUM_GREATER | a long rock-cut underground gallery lined with side chambers, each holding a colossal polished dark granite box sunk below the floor | `03_locations.md` entry 41 |
| LOC_SERAPEUM_SERVICE_TUNNEL | a narrow rough rock-cut service tunnel with worn rail grooves in the floor, a colossal granite box abandoned in it, almost blocking the way | `03_locations.md` entry 42 |
| LOC_GIZA_PLATEAU | the Giza plateau: three great weathered pyramids above a rocky desert, a colossal human-headed lion in its quarried enclosure, a long ruined causeway | `03_locations.md` entry 43 |
| LOC_OSIRIS_SHAFT | a flooded rock-cut chamber thirty metres underground, black water in a channel around a central island with a stone coffin lid and pillar stumps | `03_locations.md` entry 44 |
| LOC_GP_SUBTERRANEAN | an unfinished bedrock chamber deep beneath a pyramid, a roughly flat ceiling, a jagged stepped rock floor and a railed pit | `03_locations.md` entry 45 |
| LOC_GP_WELL_SHAFT | a cramped irregular shaft seventy centimetres square dropping steeply through masonry and fissured bedrock, crude footholds in its sides | `03_locations.md` entry 46 |
| LOC_GP_DESCENDING | a long straight passage a metre wide and chest high, sloping steeply down through fitted limestone into bedrock, its far end a black square | `03_locations.md` entry 47 |
| LOC_GP_MAMUN_TUNNEL | a rough hand-hacked tunnel through a pyramid's limestone core, soot-blackened irregular walls, a steel handrail and a worn floor | `03_locations.md` entry 48 |
| LOC_GP_GRAND_GALLERY | a steep soaring corbelled limestone gallery rising at twenty-six degrees, eight and a half metres high, a wooden cleated walkway up its centre | `03_locations.md` entry 49 |
| LOC_GP_QC_SHAFT | inside a tiny square limestone shaft twenty centimetres across, ending at a small polished stone slab with two corroded copper pins | `03_locations.md` entry 50 |
| LOC_GP_PASSAGE_ABOVE | a narrow steep hidden passage of perfectly fitted pale limestone with hair-thin joints, shallow unworn steps rising to a black opening | `03_locations.md` entry 51 |
| LOC_HALL_TWO_TRUTHS | a sealed tall corbelled limestone hall inside a pyramid, two rows of tall empty niches leading to a black stone balance, in total darkness | `03_locations.md` entry 52 |
| LOC_GP_NORTH_FACE | the stepped, weathered limestone north face of the Great Pyramid, a dark entrance high up beneath huge chevron beams, a rough hole below | `03_locations.md` entry 53 |
| LOC_FIRST_TIME | a vast green prehistoric savannah with acacias, a reedy lake with hippos, grassy sandstone mesas and humid haze, no human structures | `03_locations.md` entry 54 |
| LOC_ROBOT_HALF_MARATHON | a wide modern city boulevard with a race lane behind plain white barriers, crowds with phones, glass towers, a blank start arch | `03_locations.md` entry 55 |
| LOC_DEWAR_VAULT | a windowless bay of tall brushed stainless-steel cryogenic tanks in rows, frost on their filling ports, white vapour spilling to the floor | `03_locations.md` entry 56 |
| LOC_PORT_WAREHOUSE | a vast harbour warehouse in a Japanese port city, high steel roof and skylights, endless neat rows of folding cots, gantry cranes outside | `03_locations.md` entry 57 |
| LOC_LAGOS_STREET | a wide Lagos street gone utterly still at dawn, yellow minibuses and cars stopped at odd angles, closed market stalls, no people | `03_locations.md` entry 58 |
| LOC_STADIUM_GARDEN | an aerial of a huge stadium whose pitch is covered by a precise grid of thousands of white mats and pale shades, stands empty | `03_locations.md` entry 59 |
| LOC_HOSPITAL_WAKING | a modern hospital maternity room, pale walls, a wide window, a white bed and a clear bassinet on a steel stand | `03_locations.md` entry 60 |
| LOC_HEARING_ROOM | a formal pale-wood hearing room, a raised curved panel bench facing a lone witness table with a microphone and a glass of water | `03_locations.md` entry 61 |
| LOC_TITLES_KITCHEN | a compact modern high-rise kitchen at night, a white stone counter with folded laundry, city lights far below the window | `03_locations.md` entry 62 |
| LOC_TITLES_WARD | a calm modern hospital ward, beds in white linen between pale curtains, tall windows full of soft daylight | `03_locations.md` entry 63 |
| LOC_TITLES_PORT | a long container-port quay at dusk, towering gantry cranes over a moored ship of unmarked containers, bollards and mooring lines | `03_locations.md` entry 64 |
| PROP_PECTORAL | an ancient gold pectoral with a translucent pale yellow-green glass winged scarab at its centre, flanked by gold cobras, with a fringe of flower pendants | `04_props.md` §1 |
| PROP_DAGGER | a slim thirty-four-centimetre ancient dagger with a pale silver-grey meteoritic iron blade, a gold granulated hilt and a clear rock-crystal pommel | `04_props.md` §2 |
| PROP_EBONY_STICK | a plain straight 1.35-metre near-black ebony walking staff with a narrow gold band below its rounded top and a gold foot cap | `04_props.md` §3 |
| PROP_HEART_VESSEL | a squat fifteen-centimetre jar of thick cloudy yellow-green desert glass, sealed with black resin, with a small wax serpent and a papyrus band | `04_props.md` §4 |
| PROP_TRUMPET_BRONZE | an ancient fifty-centimetre straight bronze trumpet with thin gold bands at the mouthpiece and flared bell, finely engraved near the bell | `04_props.md` §5 |
| PROP_TRUMPET_SILVER | an ancient fifty-eight-centimetre slender silver trumpet in soft grey tarnish, its flared bell engraved with lotus petals, with a faint repair seam | `04_props.md` §6 |
| PROP_BURTON_PLATES | a large 1920s wooden bellows field camera with brass fittings on a wooden tripod, with antique glass-plate negatives in wooden dark-slides | `04_props.md` §7a |
| PROP_CUTMAP_PROJECTION | a projected engineering-style line diagram of pale cyan light above the sheet, a schematic human outline with cut lines marked at every joint | `04_props.md` §7b |
| PROP_NANO_ADZE | a pen-length dark titanium stylus ending in a fingernail-sized, right-angled adze blade of polished black meteoritic iron | `04_props.md` §8 |
| PROP_KARNAK_BLOCK | a half-metre ancient sandstone block, weathered honey-beige, with worn relief of a woman beneath rays ending in hands on its front face | `04_props.md` §9 |
| PROP_MERKHET_BAY | a forty-five-centimetre dry palm rib with a V-slit sighting notch, and a short wooden bar with a hanging plumb line | `04_props.md` §10 |
| PROP_LAYLA_PENDANT | a small polished silver cartouche pendant, a rounded oblong with a bar at its base, on a fine silver chain | `04_props.md` §11 |
| PROP_INDEX_CARDS | a dog-eared stack of white ruled index cards held by a black binder clip, covered in dense black handwriting | `04_props.md` §12 |
| PROP_POLICE_LAUNCH | an old fourteen-metre white-and-faded-navy steel diesel river launch with a small square wheelhouse, tyre fenders and an open aft deck | `04_props.md` §13 |
| PROP_DIESEL_LOCO | a boxy 1970s diesel locomotive, sun-faded pale blue with a cream band and a chipped chevron-striped nose, grimy and unmarked | `04_props.md` §14 |
| PROP_TRAIN_COACH | a faded bottle-green 1970s steel passenger coach with a cream window band and small square windows, rusty and dark | `04_props.md` §14 |
| PROP_FELUCCA | a traditional eight-metre wooden Nile sailing boat with one huge triangular off-white sail on a long slanted yard and a faded turquoise hull | `04_props.md` §15 |
| PROP_CORNFLOWER_WREATH | a small hand-span circlet of silver-green olive leaves and bright blue cornflowers, with a few blue lotus petals and orange berries | `04_props.md` §16a |
| PROP_CORNFLOWERS_2033 | a loose handful of fresh vivid blue cornflowers with fringed petals and violet centres on slender silver-grey stems | `04_props.md` §16b |
| PROP_HAND_CART | a battered two-wheeled site hand-cart with a dusty wooden plank bed, a rusted steel frame, small rubber wheels and long handles | `04_props.md` §17 |
| PROP_TABLET_LAYLA | a slim unbranded dark-graphite tablet with rounded corners, its screen glowing softly with a daylight image | `04_props.md` §18 |
| PROP_REPLICA_VESSEL | a flawless machined replica jar of perfectly clear green glass, fifteen centimetres tall, with a pale featureless form inside and a neat black cap | `04_props.md` §19.1 |
| PROP_RAMI_NOTEBOOK | a battered A5 mustard-yellow hardback notebook with a black elastic band and a clipped pen, its pages swollen with handwriting | `04_props.md` §19.2 |
| PROP_CONSERVATION_KIT | an open grey hard case with a compact black camera fitted with a near-black filter, a red headlamp and pouches of vivid blue pigment | `04_props.md` §19.3 |
| PROP_SLEEP_BRACELET | a thin plain closed band of brushed silver-grey metal around an adult's wrist, with no clasp and no marking | `04_props.md` §19.4 |
| PROP_SCARAB_KEYRING | a thumb-sized pale green plastic scarab keyring that glows soft luminous green in the dark, on a small steel ring | `04_props.md` §19.5 |
| PROP_IRON_ADZE_1323 | a thirty-five-centimetre ancient ritual adze with a dark wooden handle and a small iron blade lashed at a right angle | `04_props.md` §19.6 |
| PROP_LAMP_1925 | a dented 1920s brass kerosene hand-lantern with a tall glass chimney and a wire handle, burning a warm amber flame | `04_props.md` §19.7 |
| PROP_CLINIC_CANE | a plain matte-grey aluminium medical cane with a curved handle and a black rubber tip | `04_props.md` §19.8 |
| PROP_LINEN_SHAWL | a long cream linen shawl with a short knotted fringe, soft and creased, worn across the chest like a sash | `04_props.md` §20.1 |
| PROP_JACKAL_MASK | a worn black-painted fired-clay jackal-head mask with tall pointed ears, a long muzzle and small eye-holes set low beneath it | `04_props.md` §20.2 |
| PROP_PAINTER_PALETTE | a flat dark-wood painter's palette with six round pigment cakes in blue, green, red, yellow, black and white, and reed brushes | `04_props.md` §20.3 |
| PROP_SCRIBE_PALETTE_1330 | a slim pale wooden scribe's palette with two round wells of red and black ink and a slot holding thin reed pens | `04_props.md` §20.4 |
| PROP_BROADCAST_RIG_1939 | a 1930s portable broadcast rig of black wooden cases with round dials and bakelite knobs, cloth cables running to a ribbon microphone | `04_props.md` §20.5 |
| PROP_GIFT_MUG | a glossy white souvenir mug with a thin gold rim line and a small gold-and-blue printed picture panel on its side | `04_props.md` §20.6 |
| PROP_LAYLA_STENCIL | a child's green plastic hieroglyph stencil sheet on white paper beside a chunky glow pen, a traced oval frame on the paper | `04_props.md` §20.7 |
| PROP_READING_RIG | a compact reading rig, a matte-black laser head on a small motorised gantry above an empty palm-sized titanium cradle | `04_props.md` §20.8 |
| PROP_CASKET_NEST | nested ancient caskets of rough granite, corroded bronze, dark cedar and dull gilt, opened one inside another and packed with pale sand | `04_props.md` §20.9 |
| PROP_FARM_TRUCK | a small battered fifty-year-old farm truck, faded pale blue rounded cab, wooden-slatted cargo bed, mud to the doors, unmarked | `04_props.md` §20.10 |
| PROP_FARMER_BOAT | a small open wooden farmer's boat with tin-patched planks, peeling blue and white paint and a smoking outboard motor | `04_props.md` §20.11 |
| PROP_CAR_FERRY | a small rusted flat-decked river car ferry with raised ramps at both ends and a tiny wheelhouse on one side | `04_props.md` §20.12 |
| PROP_NIGHT_BARGE_1332 | a long ancient wooden river barge by torchlight, a painted eye at the bow, a tall reed-and-linen cabin, a round cargo under linen | `04_props.md` §20.13 |
| PROP_SECURITY_SPEAKER | a small plain white wall-mounted security speaker with a round grille and a thin cable along the rock wall, unmarked | `04_props.md` §20.14 |
