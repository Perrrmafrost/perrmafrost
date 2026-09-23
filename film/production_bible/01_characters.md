# 01 — CHARACTERS: look-locks, wardrobe states, reference stills

**HERE AM I** · production bible, file 01 of 05 · photoreal live-action AI video, 1920×1080, 16:9, 24 fps, clips of 4–8 s.
**Authority:** story bible v3 (`drafts/02_STORY_BIBLE_LOCKED.md`, esp. §3.3–3.4, §6, §7, §11, §12, §14) and the lead's rulings (`drafts/04_CRITIQUE_DECISIONS.md`; the chest-port, desiccation, anti-alien and identity-protocol rulings in `critique_raw.md` ?-4, ?-5, ?-14 and the §14 locks). Facts: research 01, 02, 04, 12 and 16, and Herodotus II.36–37 (`research/src`). Where this file is stricter than a shot writer's instinct, this file wins; where it conflicts with the bible, the bible wins. Flag it.

---

## 0. HOW TO USE THIS FILE (every shot prompt)

1. **FIXED WORDING.** Every character has a **LONG** look-lock (40–70 words) and a **SHORT** look-lock (15–25 words). Paste them **verbatim** in step 2 of the PROMPT paragraph (03b spec): never paraphrase, reorder, trim or "improve" them. Use **LONG** for the first shot of a character in a scene, for every close-up and medium where the face carries the shot, and for every composed first frame used for image-to-video. Use **SHORT** everywhere else (wides, OTS, coverage inside a scene already established).
2. **Assembly of step 2**: `[LONG or SHORT], [wardrobe paste phrase], [damage phrase], [state overlays]`. Every piece is a fixed phrase from this file. Example (Tut, Seq 7, night wide):
   > *a slight olive-skinned Egyptian young man, shaved head with faint stubble, visible overbite, very dark bright eyes, thin gold seam ring around his neck, wearing an oversized charcoal hooded military field jacket over a white linen tunic, dark cargo trousers rolled at the ankle, jacket and trousers dusted grey-beige with sandstone dust, one jacket pocket flap torn loose, the tunic hem greyed, a soft glow through the fabric at the centre of the chest, holding in his right hand a plain straight near-black ebony walking staff with a narrow gold band below its rounded top, reaching his collarbone*
3. **Look codes.** `CHAR_<NAME>_<wardrobe><damage level>`: e.g. `CHAR_TUT_B2` (T-B at damage L2), `CHAR_NOUR_B1`, `CHAR_ADAEZE_C3`. Use them in `In frame:` and `Refs:`. The `Refs:` line also lists the still files to attach (e.g. `CHAR_NOUR_A_front, CHAR_NOUR_A_34, CHAR_NOUR_B_full`).
4. **No names in PROMPTS.** Tokens and screenplay names stay in `In frame:`/`Refs:`. The PROMPT carries only descriptors. That rule covers every historical person (the king, his father, the queen, Ay, the 1925 team, the 1939 bandsman) (bible §6). **Words banned from PROMPTS** (they pull models toward clichés or trip filters): pharaoh, King Tut, Tutankhamun, Nefertiti, Akhenaten, Cleopatra, mummy, mummified, zombie, cyborg, android (for any human), alien, ancient astronaut, nemes, gold mask, corpse, organ, blood, severed, open chest.
5. **Generic damage levels** (use the character's own phrase where one is given; otherwise these):
   - **L0**: nothing (clean, pressed).
   - **L1**: *clothes creased, light dust at the hems and cuffs*
   - **L2**: *clothes grimy with dust, one small tear, a sweat-darkened collar*
   - **L3**: *clothes heavily dusted with pale stone dust and streaked with soot, several tears*
   - **WET**: *clothes soaked dark and clinging* · **DRYING**: *clothes drying, with pale water tide-lines*
   Damage builds in these discrete steps and never drifts continuously (critique: "3 discrete levels"). The per-sequence levels follow bible §12.
6. **Injuries are costume, not wounds** (bible §3.3–3.4): bandages, splints, limps, torn cloth, a cradled hand. No blood, no open wounds, no gore. Deaths are staged with the kill grammar and are never written into a look-lock.
7. **Reference-still protocol** (bible §14.1: identity comes from images, not words):
   - Generate every still with **one image model**, approve it, freeze it, and save it as `<still id>.png` (e.g. `CHAR_NOUR_A_front.png`).
   - Each locked face gets the four core stills (front neutral, three-quarter, profile, full body in wardrobe A) plus the extra state stills listed, plus **two expression stills**: rerun the front prompt with the expression in place of "neutral relaxed expression".
   - Every principal shot is **image-to-video from a composed first frame**: the approved still inpainted into the location plate at the shot's framing. Attach front + three-quarter + the current wardrobe's full body as character references where the tool allows.
   - On open models, a per-character LoRA may be trained on 20–30 approved stills (all faces are synthetic). A final face-unification pass against the front still is allowed.
   - Derived faces (CHAR_TUT_CHILD, CHAR_AKHENATEN_1336) are made by **image-editing the approved parent still**, never from text alone.
   - **Common still negative** (append to every still): *cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light*, plus the character negative given in each entry.
8. **Faces on screen:** at most two principal faces clearly visible per clip; three only in locked-off masters (bible §14.2). Group scenes are covered in singles and OTS.
9. **Night silhouettes** (bible §14.3): Tut charcoal hood · Nour olive · Adaeze navy · Fathi red scarf · Rami yellow windbreaker · Layla yellow raincoat. Every night shot names a key light that reaches the faces (the deep-brown faces of Fathi and Adaeze especially).
10. **Likeness rule.** No fictional character may resemble a celebrity or public figure: the faces are built from unusual, specific feature combinations, and each entry's negative carries "celebrity likeness". Real historical people (1323 BC, Amarna, 1925, 1939) are drawn to be *plausible* against period portraits and photographs, but we never claim a likeness, never chase one, and never feed their photographs to a generator. Only our own approved stills are used as references.

---

## CAST INDEX

| Token | Character | Era | Face status | On screen |
|---|---|---|---|---|
| CHAR_TUT | the king ("TUT") | 2033 (and 1323 BC body) | locked 1 | Seq 1–12, coda |
| CHAR_TUT_BODY_1323 · CHAR_TUT_CRADLE_2033 · CHAR_TUT_D1–D4 · CHAR_TUT_CODA_CASE | the same body: under linen (1323 BC), on the cradle (1.5), the four dawn held states (12.7), in the case (coda) | 1323 BC / 2033 | from 1 | 1.1, 1.5, 12.7, coda |
| CHAR_NOUR | Dr. Nour Kamel | 2033 | locked 2 | 1–12, coda |
| CHAR_ADAEZE | Dr. Adaeze Okoro | 2033 | locked 3 | 1–12 |
| CHAR_TOMAS | Dr. Tomas Lindqvist | 2033 | locked 4 | 1–12 (dies 12.6) |
| CHAR_TAREK | Col. Tarek Mansour | 2033 | locked 5 | 1–11 (dies 11.3) |
| CHAR_FATHI | Sgt. Fathi Abdel-Rahman | 2033 | locked 6 | 1–12 |
| CHAR_RAMI | Rami Fawzy | 2033 | locked 7 | 1–7 (dies 7.4) |
| CHAR_HALE | Victor Hale | 2033 | locked 8 | 1–4, the Garden, coda |
| CHAR_LAYLA | Layla Kamel | 2033 | locked 9 | 2, 4, image, 12.8 |
| CHAR_AKHENATEN | the forecast father | 2033 | locked 10 | 7.3, 9, 10–12 |
| CHAR_AKHENATEN_1336 | the real king (same actor) | c. 1336 BC | derived from 10 | 9.5(a) |
| CHAR_NEFERTITI | the queen / Neferneferuaten | c. 1336 / 1332 BC | locked 11 | 9.5 |
| CHAR_AY | Ay | 1323 BC | locked 12 | 1.1, 1.2 |
| CHAR_TUT_CHILD_6 · CHAR_TUT_CHILD_9 · CHAR_TUT_CHILD_11 | Tutankhaten at 6 / 9 / 11 (family name CHAR_TUT_CHILD) | Amarna | derived from 1 | 9.5a / 9.5b / 9.5c |
| CHAR_YOUNG_MOTHER | the king's daughter | c. 1332 BC | one sequence | 9.5(b) |
| CHAR_PAWAH | lector of the first Weighing | c. 1332 BC | period | 9.5(b) |
| CHAR_MERITATEN | eldest princess | c. 1336 BC | background | 9.5(a) |
| CHAR_ANKHESENAMUN | the widow | 1323 BC | period | 1.2 |
| CHAR_LECTOR_1323 | lector priest | 1323 BC | period | 1.1, 1.2 |
| CHAR_EMBALMER_JACKAL | masked embalmer | 1323 BC | masked | 1.1 |
| CHAR_EMBALMER_PRIEST | young priest-embalmer | 1323 BC | period | 1.1 |
| CHAR_PAINTER_1323 | tomb painter (optional) | 1323 BC | period | 1.2 |
| CHAR_CARTER_1925 | the excavator | 1925 | 1925 four | 1.3 |
| CHAR_DERRY_1925 | the anatomist | 1925 | 1925 four | 1.3 |
| CHAR_HAMDI_1925 | the senior anatomist | 1925 | 1925 four | 1.3 |
| CHAR_BURTON_1925 | the photographer | 1925 | 1925 four | 1.3 |
| CHAR_IBRAHIM_1925 | the lamp-holder (fictional) | 1925 | period | 1.3 |
| CHAR_RADIOLOGIST_1968 | radiologist (generic) | 1968 | insert | 1.4 |
| CHAR_XRAY_ASSISTANT_1968 | radiographer | 1968 | insert | 1.4 |
| CHAR_BANDSMAN_1939 | the trumpet bandsman (RESERVE: the screenplay uses CHAR_BANDSMAN_2033) | 1939 | re-staging | 4.2 (reserve) |
| CHAR_RADIO_ENGINEER_1939 | the broadcast engineer (RESERVE) | 1939 | re-staging | 4.2 (reserve) |
| CHAR_HASSAN | Cpl. Hassan | 2033 | soldier pack | 4–5 (dies 5.2) |
| CHAR_MINA | Pvt. Mina | 2033 | soldier pack | 4–8 (dies 8.6) |
| CHAR_YOUSSEF | Pvt. Youssef | 2033 | soldier pack | 4–10 (dies 10.4) |
| CHAR_KARIM | Pvt. Karim | 2033 | soldier pack | 4–10 (dies 10.4) |
| CHAR_SESHAT_VOICE | SESHAT / AMUN | voice | — | all |
| CHAR_MINISTER_GALA · CHAR_SAMEH · CHAR_MIDWIFE_2033 · CHAR_GARDEN_SLEEPERS · CHAR_AMARNA_SLEEPERS_1336 · CHAR_AMARNA_COURTIERS_1336 · CHAR_HEARING_PANEL | wides-only / background | various | no face lock | see §10 |
| CHAR_BANDSMAN_2033 · CHAR_YOUNG_OFFICER · CHAR_OLD_FISHERMAN · CHAR_ENVOY_1336 · CHAR_NEW_MOTHER_2033 · CHAR_CONSERVATOR_2033 | one-scene faces (added by the cross-check) | 2033 / c. 1336 BC | one front still each | 4.2, 3.2, 6.1, 9.5a, 12.8, coda; see §10b |
| CHAR_POLICE_LINE · CHAR_GALA_GUESTS · CHAR_DEFENCE_MINISTER_GALA · CHAR_ARMY_DETAIL · CHAR_NIGHT_FISHERMEN · CHAR_FIRST_TIME_PEOPLE · CHAR_CONTROL_OPERATORS | groups and wides-only (added by the cross-check) | various | no face lock | see §10b |
| CHAR_STAFF_OFFICER_VOICE · CHAR_KITCHEN_WOMAN_VOICE · CHAR_PANEL_CHAIR_VOICE | voice only (added by the cross-check) | 2033 | — | 4.3, 5.2, 1.6, coda |

Prop tokens cited here (PROP_…) are defined in `04_props.md`; unit tokens (UNIT_…) are in `02_units_and_machines.md`. Reconciled by the cross-check: every token cited in files 01–05 resolves to one entry, and the film-wide list is `00_INDEX.md`.

---

## 1. TUTANKHAMUN

### CHAR_TUT — TUTANKHAMUN, "TUT" (screenplay cue TUT; born Tutankhaten; never named in any prompt)
*Locked face 1 of 12 · Seq 1–12 + coda · silhouette: charcoal hood (T-B) · look codes A0, B1, B2, B3, C3, D1–D4 · the same sheet is the source for CHAR_TUT_CHILD*

| Field | Lock |
|---|---|
| **Age** | Apparent 19. He died at about 19, c. 1323 BC [01 §1]; the 2033 body is regrown on his own remains to that age. |
| **Ethnicity / heritage** | Ancient Egyptian of the Nile valley, 18th Dynasty. Build the sheet from the range of modern Upper-Egyptian and Nile-valley faces (olive to brown), continuous with the modern Egyptian cast (bible §6 period-faces rule). Never a Hollywood-European or costume-drama face. |
| **Build** | Slight and slender, 1.67 m [16 §5]; narrow shoulders, thin wrists, long fingers. He walks with a stick in his RIGHT hand and a careful left-side limp (left club foot, Köhler disease II [01 §6]). A faint lean from a possible mild scoliosis [16 §5] is performance only, never prompted. |
| **Face (repeatable features)** | Narrow oval face tapering to a small pointed chin; high cheekbones; full lips, the upper lip lifted a little by a **visible overbite** showing large front incisors [16 §5]; a straight medium nose with a softly rounded tip; fine straight dark brows; long lashes. A subtly long head within the normal human range, softened by stubble: on the sheet only, never written into prompts (see the negative) [critique ?-14]. Both earlobes are pierced with small healed holes (the mummy's ears are pierced [01 §16]): a sheet detail, never prompted. |
| **Hair** | Shaved head with faint, even dark stubble (about 2 mm), constant all film. A smooth jaw: no beard, no moustache. |
| **Skin** | Warm olive-brown, matte, with natural pores. The only non-human surfaces are the gold seams, the chest plate (covered) and the left foot. Never luminous, grey or glossy, and never circuitry or lattice under the skin (bible §6). |
| **Eyes** | Very dark brown, near-black, bright and quick, with strong catchlights. |
| **Voice** | A light, clear tenor, soft on some consonants (s, sh, p, b) from a partial cleft palate [16 §5]. Formal, slightly archaic English with sudden modern words ("This I know from it"); Late Egyptian with Nour (subtitled). Dry royal humour; grief in understatement. After 12.3 he only mouths. |
| **Anchors (bible §6)** | ALWAYS in the prompt: slight build · shaved head with faint stubble · visible overbite · very dark bright eyes · thin gold seam ring around the neck. Hand shots add the gold wrist seams. |

**LONG look-lock** (62 words, paste verbatim):

> a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair

**SHORT look-lock** (24 words, paste verbatim):

> a slight olive-skinned Egyptian young man, shaved head with faint stubble, visible overbite, very dark bright eyes, thin gold seam ring around his neck

**Character negative** (append to the shot NEGATIVE and to every still below): alien, extraterrestrial, elongated cranium, conehead, grey skin, oversized black eyes, glowing skin, visible circuitry, lattice pattern under the skin, metal face plates, robot or android look, a full head of hair, beard, striped royal headcloth, gold funerary mask, crown, bandage wrappings, heavy eye makeup, jewellery, blood, wounds, stitches on the face

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A0 (T-A)** | 2.1 → 4.4 (after the cradle, until the escape) | A plain ankle-length gown of soft undyed white linen; long loose sleeves ending at the wrist bone (the wrist seams show when he lifts his hands); a low round neckline that leaves the neck seam visible; a narrow white linen sash tied loosely at the waist. Right foot: a plain flat brown leather sandal. Left foot: the bare ceramic foot (never a sandal). A plain matte-grey aluminium medical cane with a curved handle and a black rubber tip (PROP_CLINIC_CANE) from 2.1. From 2.4, Layla's glow-in-the-dark scarab keyring (PROP_SCARAB_KEYRING) in his hand or tucked in the sash (inserts only). | *wearing a plain ankle-length white linen gown with loose long sleeves and a low round neckline* |
| **B1–B3 (T-B)** | 4.4 → 11.5 | Tarek's spare: a charcoal-grey cotton-canvas military field jacket, oversized on him, four flap pockets, zip-and-snap front, attached hood (UP in night wides and silhouettes, DOWN for dialogue), cuffs turned back once so the wrists show. Under it, the white linen tunic: hip-length, long-sleeved, round neck, the neck seam visible. Dark charcoal-olive cotton cargo trousers, a little long, cuffs rolled once above the ankle. A plain dark webbing belt with the meteoritic dagger in its gold sheath at the right hip (PROP_DAGGER). Right foot: the sandal; left foot: ceramic. The ebony stick in the right hand (PROP_EBONY_STICK). Rami's notebook in the left breast pocket from 7.4. Layla's keyring in the right hip pocket. | *wearing an oversized charcoal hooded military field jacket over a white linen tunic, dark cargo trousers rolled at the ankle* |
| **C3 (T-C)** | 12.3 → 12.7 (the Hall to dawn) | No jacket: it is left soaked in the stone (11.5). The white linen tunic over the dark cargo trousers, at damage L3. A long cream linen shawl (PROP_LINEN_SHAWL: Nour's lector's shawl, draped on him as he reaches the Hall) wrapped round his shoulders and crossed over the chest; the vessel is lifted out under it. The right sandal stays on. No stick, no dagger. | *wearing a stone-dusted white linen tunic and dark trousers, a long cream linen shawl wrapped around his shoulders and crossed over his chest* |

**Progression: dirt, damage, injuries, props carried**

- **L0** (Seq 1–3, A0): spotless.
- **L1** (4.4–6, B1): paste *clothes creased, a film of pale dust at the hems and cuffs*. In Seq 5–6 add *damp patches and dried river-water marks on the jacket*.
- **L2** (Seq 7–9, B2): paste *jacket and trousers dusted grey-beige with sandstone dust, one jacket pocket flap torn loose, the tunic hem greyed*. In Seq 8 add *fine white plaster dust on the shoulders and hood* (the north wall).
- **L3** (Seq 10–11, B3; Seq 12, C3): paste *heavy pale limestone dust and soot streaks, the left trouser knee torn open, the right jacket elbow torn*. From 11.3 to 11.5 add *soaked dark with water to the chest*, then *drying, with pale water tide-lines*. For C3 paste *the tunic greyed with stone dust, dried water tide-lines at the hem*.
- **Injuries:** none that bleed. The body clock is the three seam cracks (L wrist 9.4, L knee 10.4, neck 12.3), the tremor and the foot stall (from 6.2), and the glow states.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a wry half-smile, the eyes amused, the overbite showing · (2) grief held very still, eyes wet, jaw set

#### CYBORG ANATOMY LOCK (sheet, VFX and COMP reference; bible §6 wins where it is stricter)

**Rule of visibility (bible §6):** in every shot the NECK seam shows; hand shots add the WRIST seams; every other seam exists but is covered, except in the one waist-up mirror shot (Seq 2.1). The chest glow is a COMP element: generated plates say only *"a soft glow through the fabric at the centre of the chest"*. The left foot appears only in inserts and wides. The nape is seen only from behind. Skin is never luminous; no lattice is ever visible under the skin.

**Seam map: fourteen joint seams, exactly on the 1925 cut lines.** Research [01 §3]: in KV15 the body was *"decapitated, his arms separated at the shoulders, elbows and hands, his legs at the hips, knees and ankles, and his torso cut from the pelvis at the iliac crest."* SESHAT rebuilt him on those lines and closed each one in gold.

| # | Seam | Exact line on the body | 1925 cut | Visible |
|---|---|---|---|---|
| 1 | Neck | a full ring round the base of the neck, 2 cm above the collarbones, dipping slightly at the throat notch | head detached | **always (anchor)** |
| 2–3 | Shoulders L/R | a ring round the top of each arm, over the shoulder cap and through the armpit | arms at the shoulders | mirror shot only |
| 4–5 | Elbows L/R | a ring round each arm through the elbow crease | at the elbows | mirror shot only |
| 6–7 | Wrists L/R | a ring at each wrist crease | at the hands | **hand shots** |
| 8 | Waist | a band round the torso along the top of the hip bones (iliac crest), about 4 cm below the navel at the front | torso from pelvis | bottom edge of the mirror shot only |
| 9–10 | Hips L/R | a ring round the top of each thigh, along the groin crease and under the buttock fold | at the hips | never |
| 11–12 | Knees L/R | a ring round each knee just below the kneecap | at the knees | left knee: crack insert through torn trousers (10.4 on) |
| 13–14 | Ankles L/R | a ring at each ankle; on the LEFT it is the junction of skin and ceramic foot | at the ankles | foot inserts |

- **Seam look:** 2–3 mm wide, polished warm yellow gold, flush with the skin and very slightly raised, like kintsugi gold lacquer on mended pottery. The skin either side is smooth and normal: no redness, no stitches, no rivets, no light.
- **Crack look (the body clock, bible §5):** a hairline split along the gold, 1–2 cm long, a thread of dark shadow in the gap, a few lifted gold flecks. No blood, no wound. Order: **LEFT wrist at Amarna (9.4) → LEFT knee at the Serapeum (10.4) → neck, below the left ear, in the Hall (12.3).** Once cracked, a seam stays cracked.

**Sternum plate and chest port.** The sternum and front ribs are missing from the real mummy [01 §5]; SESHAT printed their replacement in titanium (real precedent: the 2015 3D-printed titanium sternum-and-rib implant [12 §6]).
- **Plate:** satin grey titanium, a rounded shield about 18 cm tall and 12 cm wide, set flush from the notch at the base of the throat to below the breastbone, framed by a thin gold seam, hinged along its left edge (it opens like a small door under the tunic in 8.5 and 12.3; the camera stays on faces and hands). Printed as a lattice inside; the outer face shows only a very fine engraved lattice texture, readable within 30 cm and only in the mirror shot.
- **Port:** a **palm-sized oval window** (about 9 × 7 cm) of thick, very faintly green glass in a thin gold bezel at the plate's centre (bible §6 and critique ruling ?-4: a coin-sized window cannot pass the fist-sized vessel). Behind it in G0 the lattice core shows as a **coin-sized point of light**: this is where the brief's "coin-sized chest window" lives. In G1 the port shows the vessel's bubbled yellow-green desert glass, with a dark shape inside, lit warm from within.
- **"Lattice sternum shadow":** never under the skin and never in a generated plate (ruled unreadable at 1080p). It exists only (a) as the plate's micro-texture in the mirror shot and (b) optionally in the COMP glow element, as a faint diamond-lattice shadow that the plate casts on the inside of the fabric around the light point.

**Chest glow states (COMP element; colour and pulse are set in post, not in the prompt)**

| State | Seq | Colour (COMP target) | Behaviour | Prompt phrase |
|---|---|---|---|---|
| **G0** | 1.5 → 6.2 | cold pale green, about #A6F2C2 core falling off to #3F8F6A; dim | one slow, even swell every 4 s (a breath, not a heartbeat); about 6 cm of spill through linen | *a soft glow through the fabric at the centre of the chest* |
| **G0f** | 6.2 → 8.5 | the same green, 10–20% dimmer | irregular stutters, 0.2–0.5 s dropouts (the lattice core failing after the port cut) | same phrase; performance note "the glow falters" |
| **G1** | 8.5 → 12.3 | warm amber-gold tinted green by the vessel's yellow-green glass ("amber-green"): about #FFB84D core with a #C9D46A cast | brighter, about 10 cm of spill; a slow visible double heartbeat, about 50 bpm, slowing through Seq 11–12 | same phrase |
| **G2** | 12.3 → end | none | dark | *no light at the centre of his chest* |

**Left foot.** A matte black technical-ceramic foot printed in one piece, replacing the club-footed left foot from the ankle down [01 §6]. Its side profile sweeps in one continuous hooked curve like the blade of the Opening-of-the-Mouth ritual adze, the iron tool named for the Great Bear [04 §2, §12]: a rounded heel, a high arch, and the toes merged into a single smooth rounded tip, with no toenails. A thin gold seam ring (seam 13) marks where ceramic meets skin. It has a faint tone-on-tone grain and no visible joints, LEDs or logos. Sound: a soft, dry ceramic click on stone. He never puts a sandal on it and never trusts it: he always leans on a stick. **After 6.2** the actuator stalls: the foot drags and clicks unevenly.

**Nape.** Until 6.2, a **port**: round, 12 mm across, with a gold rim and a dark recessed centre, centred on the nape 2 cm above the neck seam, and seen only from behind. At **6.2** Tomas cuts it out on deck under a headlamp: shoot the hands, the tools, Tut's face and the lifted gold disc, never an open wound. **After 6.2**, a **scar**: a small round pale scar edged by a broken arc of gold, closed with three fine dark stitches in Seq 6–7 and healed smooth from Seq 8.

**Other bodies of the same boy (no face work beyond these).** Each is its own token with fixed LONG/SHORT wording (added by the cross-check; the stills are CHAR_TUT_BODY_1323, CHAR_TUT_CRADLE_2033 and CHAR_TUT_CODA_CASE below). Append `NEG_REMAINS` (file 05 §2.2) to every one.

**CHAR_TUT_BODY_1323** (Seq 1.1, 1323 BC; no seams, no plate: this is before 1925)

LONG (51 words):

> a slight young man of about nineteen lying still on a low limestone table under plain white linen drawn up to the collarbones, warm olive-brown skin, shaved head, eyes closed, his face turned in profile and half-lost in warm lamplit shadow, his arms hidden beneath the linen, peaceful and utterly still

SHORT (23 words):

> a slight young man lying still under white linen drawn to the collarbones, shaved head, eyes closed, face in profile, half in shadow

**CHAR_TUT_CRADLE_2033** (Seq 1.5, the resurrection; the projected cut-map diagram is PROP_CUTMAP_PROJECTION in COMP; no detached part is ever in frame)

LONG (57 words):

> a slight young man of nineteen lying on a low brushed-titanium examination cradle under a white sheet drawn up to the collarbones, warm olive-brown skin, shaved head with faint dark stubble, eyes closed, lips slightly parted over a visible overbite, a thin line of gold light tracing a ring around the base of his neck, utterly still

SHORT (22 words):

> a slight young man on a titanium cradle under a white sheet to the collarbones, eyes closed, gold light ringing his neck

**CHAR_TUT_CODA_CASE** (coda, KV62 antechamber; never a face)

LONG (56 words):

> a small linen-wrapped form lying on a tray of pale sand inside a low glass climate case, wrapped in new cream linen, the face covered by a folded linen shroud, the forearms laid low across the body, only a thin polished gold seam ring at one wrist showing, fresh blue cornflowers laid on the glass lid

SHORT (24 words):

> a small linen-wrapped form on pale sand in a glass climate case, the face shrouded, only a thin gold seam at one wrist showing

#### STATE OVERLAYS (fixed phrases; append after the look-lock and the wardrobe phrase)

| Overlay | When | Paste phrase |
|---|---|---|
| Chest glow G0/G0f/G1 | per table above | *a soft glow through the fabric at the centre of the chest* |
| Chest dark G2 | 12.3 → | *no light at the centre of his chest* |
| Wrist seams | any hand shot | *thin gold seam rings at both wrists* |
| Left wrist cracked | 9.4 → | *the gold seam at his left wrist split by a fine hairline crack* |
| Left knee cracked (insert) | 10.4 → | *through the torn left trouser knee, a thin gold seam ring split by a hairline crack* |
| Neck cracked | 12.3 → | *the gold neck seam split by a fine hairline crack below the left ear* |
| Foot (inserts, wides) | all | *his left foot is a smooth matte-black ceramic foot shaped in one clean hooked curve like an ancient ritual adze, with a thin gold seam ring at the ankle; his right foot is in a plain flat brown leather sandal* |
| Nape port (from behind) | 1.5 → 6.2 | *a small round gold-rimmed port at the nape of his neck, just above the gold seam ring* |
| Nape scar (from behind) | 6.2 → | *a small round pale scar at the nape of his neck, edged by a broken arc of gold* |
| Tremor | 6.2 → | performance: *a faint tremor in his left hand* |
| Foot stall | 6.2 → | performance: *his left foot dragging slightly as he walks* |
| Clinic cane | 2.1 → 4.4 | *a plain matte-grey aluminium medical cane with a curved handle in his right hand* |
| Ebony stick | 4.4 → 11.5 | *holding in his right hand a plain straight near-black ebony walking staff with a narrow gold band below its rounded top, reaching his collarbone* (PROP_EBONY_STICK) |
| Dagger | 4.4 → 11.5 | *a short dagger in a gold sheath at his belt* (see PROP_DAGGER) |
| No stick | 11.5 → | performance: *walking unaided for the first time, careful and uneven* |

#### STATE TABLE BY SEQUENCE (bible §12 continuity board, expanded)

| Seq | Look code | Wardrobe | Damage | Glow | Nape | Seams cracked | Gait / foot | Stick | Dagger | Carries | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 (1323 BC) | BODY_1323 | under linen | — | — | — | — | — | — | — | — | profile in shadow; no seams |
| 1.5 (2033) | CRADLE | white sheet to collarbones | — | G0 at the heartbeat | port | — | — | — | — | — | neck ring drawn in light; eyes open |
| 2 | A0 | T-A | L0 | G0 | port | — | ceramic foot, limp | clinic cane | — | Layla's keyring from 2.4 | mirror shot 2.1 is the only seam-map shot |
| 3 | A0 | T-A | L0 | G0 | port | — | limp | clinic cane | — | — | mouths secrets to Nour (CU mouth, CU eyes) |
| 4 | A0 → B1 (4.4) | T-A → T-B | L0 → L1 | G0 | port | — | limp | → ebony stick (4.4) | → dagger (4.4) | — | hears the units through the port |
| 5 | B1 | T-B | L1 | G0 | port | — | limp | ebony | dagger | — | hood up in night wides |
| 6 | B1 | T-B (+ river damp) | L1 | G0 → **G0f** (6.2) | port → **scar** (6.2) | — | foot stalls, tremor (6.2 →) | ebony | dagger | — | surgery on deck under a headlamp |
| 7 | B2 | T-B | L2 | G0f | scar (stitched) | — | drag | ebony | dagger | Rami's notebook (7.4 →) | sandstone dust |
| 8 | B2 | T-B (+ plaster dust) | L2 | G0f → **G1** (8.5) | scar (healed) | — | drag | ebony | dagger | notebook | the heart is seated under the tunic; light spills |
| 9 | B2 | T-B | L2 | G1 | scar | **L wrist (9.4)** | drag | ebony | dagger | notebook | the Amarna memory; the father |
| 10 | B3 | T-B | L3 | G1 | scar | + **L knee (10.4)** | worse limp | ebony | dagger | notebook | Serapeum dust and soot |
| 11 | B3 (+ soaked 11.3) | T-B | L3 | G1 | scar | wrist, knee | worse | **lost on the ramp (11.5)** | **→ Fathi (11.5)** | notebook | goes under in the shaft; jacket shed in the stone |
| 12 | C3 | T-C (12.3 →) | L3 | G1 → **G2** (12.3) | scar | + **neck (12.3)** | falls; carried (12.7) | — | — | notebook | last spoken words "Here am I"; mouths after |
| 12.7 | D1–D4 | T-C | L3 | G2 | scar | all three | — | — | — | — | desiccation held states |
| Coda | CODA_CASE | new linen in the KV62 case | — | — | — | — | — | — | — | — | only the gold wrist seam shows |


**Reference stills** (image generator; self-contained)

1. **CHAR_TUT_A0_front** (front neutral, wardrobe A0) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: a plain ankle-length white linen gown with loose long sleeves and a low round neckline. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_TUT_A0_34** (three-quarter, wardrobe A0) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: a plain ankle-length white linen gown with loose long sleeves and a low round neckline. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_TUT_A0_profile** (profile, wardrobe A0) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: a plain ankle-length white linen gown with loose long sleeves and a low round neckline. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_TUT_A0_full** (full body, wardrobe A0) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: a plain ankle-length white linen gown with loose long sleeves and a low round neckline. His left foot is a smooth matte-black ceramic foot shaped in one clean hooked curve like an ancient ritual adze, with a thin gold seam ring at the ankle; his right foot is in a plain flat brown leather sandal; a plain matte-grey aluminium medical cane with a curved handle in his right hand. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_TUT_SEAMS_mirror** (seam map, waist-up, the Seq 2.1 mirror look) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: front view, waist up, bare-chested, arms relaxed and held a little away from the body, neutral expression, looking into the lens. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Thin polished gold seam rings, 2 to 3 mm wide and flush with the skin like kintsugi repairs, circle the base of his neck, both shoulders over the shoulder cap and through the armpit, both elbows and both wrists, and a gold band runs round his waist just above the hip bones; the skin either side of every seam is smooth and unmarked. A satin grey titanium plate with a very fine engraved lattice texture is set flush into the centre of his chest from the notch at the base of the throat to below the breastbone, a rounded shield framed by a thin gold seam; at its centre a palm-sized oval window of thick clear glass in a thin gold bezel, dark behind the glass. Slim, real anatomy, no other metal, no glow. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm lens, f/8, sharp throughout.

6. **CHAR_TUT_HANDS** (hand-shot anchor) · aspect ratio **16:9**

   > Photorealistic insert reference photograph for a live-action film: close-up of a slender young man's two hands held palm-down at chest height, warm olive-brown skin with natural texture, long fingers, short clean nails, a thin polished gold seam ring around each wrist exactly at the crease, 2 to 3 mm wide and flush with the skin like a kintsugi repair; loose white linen sleeves end just above the wrist bones. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 100mm macro lens, f/8, sharp throughout.

7. **CHAR_TUT_FOOT** (left-foot insert) · aspect ratio **16:9**

   > Photorealistic insert reference photograph for a live-action film: a ground-level close shot of a slight young man's feet standing on a plain grey studio floor, the hem of a white linen gown just above the ankles; his left foot is a smooth matte-black ceramic foot shaped in one clean hooked curve like an ancient ritual adze, with a thin gold seam ring at the ankle; his right foot is in a plain flat brown leather sandal; the ceramic is matte, with a faint tone-on-tone grain and the toes merged into one smooth rounded tip; the skin of the right foot is warm olive-brown. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 100mm lens, f/8, sharp throughout.

8. **CHAR_TUT_NAPE_PORT** (from behind, Seq 1.5–6.2) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: a close shot from directly behind of a slight young man's head, neck and shoulders, shaved head with faint dark stubble, warm olive-brown skin, a thin polished gold seam ring around the base of his neck, and just above it, centred on the nape, a small round port 12 mm across with a polished gold rim and a dark recessed centre; the collar of a white linen gown. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm lens, f/8, sharp throughout.

9. **CHAR_TUT_NAPE_SCAR** (from behind, 6.2 onward) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: a close shot from directly behind of a slight young man's head, neck and shoulders, shaved head with faint dark stubble, warm olive-brown skin, a thin polished gold seam ring around the base of his neck, and just above it, on the nape, a small round pale healed scar edged by a broken arc of gold; the raised hood edge of a charcoal field jacket. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm lens, f/8, sharp throughout.

10. **CHAR_TUT_B1_full** (full body, T-B, damage L1) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: an oversized charcoal hooded military field jacket over a white linen tunic, dark cargo trousers rolled at the ankle. Hood down. In his right hand a plain straight near-black ebony walking staff with a narrow gold band below its rounded top, reaching his collarbone; a short dagger in a gold sheath at his belt. His left foot is a smooth matte-black ceramic foot shaped in one clean hooked curve like an ancient ritual adze, with a thin gold seam ring at the ankle; his right foot is in a plain flat brown leather sandal. Clothes lightly creased, a film of pale dust at the hems. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

11. **CHAR_TUT_B_night_34** (three-quarter, hood UP: the night silhouette) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: three-quarter view, head and shoulders, face turned about 45 degrees toward camera left, neutral watchful expression. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: an oversized charcoal hooded military field jacket with the hood UP, framing his face in shadow, over a white linen tunic whose round neck shows the gold neck seam. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

12. **CHAR_TUT_C3_full** (full body, T-C, damage L3) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slight, slender Egyptian young man of nineteen, short and narrow-shouldered, warm olive-brown skin, shaved head with faint dark stubble, a narrow face with high cheekbones and a small pointed chin, full lips with a visible overbite, very dark bright eyes under fine straight brows, a thin polished gold seam ring around the base of his neck, like a delicate kintsugi repair. Costume: a stone-dusted white linen tunic and dark trousers, a long cream linen shawl wrapped around his shoulders and crossed over his chest. His left foot is a smooth matte-black ceramic foot shaped in one clean hooked curve like an ancient ritual adze, with a thin gold seam ring at the ankle; his right foot is in a plain flat brown leather sandal. No stick. Clothes heavily dusted with pale stone dust, dried water tide-lines at the tunic hem, the left trouser knee torn open. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

13. **CHAR_TUT_CRADLE_2033** (Seq 1.5 first frame) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a clean white museum laboratory at night, a slight young man of nineteen lying on a low brushed-titanium examination cradle under a white sheet drawn up to the collarbones, warm olive-brown skin, shaved head with faint dark stubble, eyes closed, lips slightly parted over a visible overbite, a thin line of gold light tracing a ring around the base of his neck, utterly still; above him, a faint projected diagram of thin pale-cyan lines of light hangs in the air; cool LED light, glass walls beyond. Dignified, calm and clinical. 50mm lens, fine film grain.

14. **CHAR_TUT_BODY_1323** (Seq 1.1 first frame) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: inside a mud-brick embalming house at night lit by small oil lamps, a slight young man of about nineteen lying still on a low limestone table under plain white linen drawn up to the collarbones, warm olive-brown skin, shaved head, eyes closed, his face turned in profile and half-lost in warm lamplit shadow, his arms hidden beneath the linen, peaceful and utterly still; amber lamplight and deep lapis-blue darkness. 50mm lens, fine film grain, reverent.

15. **CHAR_TUT_CODA_CASE** (coda, KV62) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a small rock-cut tomb antechamber at sunset, a small linen-wrapped form lying on a tray of pale sand inside a low glass climate case, wrapped in new cream linen, the face covered by a folded linen shroud, the forearms laid low across the body, only a thin polished gold seam ring at one wrist showing, fresh blue cornflowers laid on the glass lid; warm low light, quiet and reverent. 50mm lens, fine film grain.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, alien, extraterrestrial, elongated cranium, conehead, grey skin, oversized black eyes, glowing skin, visible circuitry, lattice pattern under the skin, metal face plates, robot or android look, a full head of hair, beard, striped royal headcloth, gold funerary mask, crown, bandage wrappings, heavy eye makeup, jewellery, blood, wounds, stitches on the face


#### DESICCATION PROGRESSION — Seq 12.7, dawn, 06:14 (four HELD states, never a morph)

Bible §12.7 and critique ruling ?-5: four held states separated by cutaways (the sun over Cairo, Nour's face, the cornflowers, Akhenaten's line); never one continuous transformation; **no close-up of the desiccated face, ever.** Vocabulary allowed: "dry dark bronze-brown skin like old parchment", "still", "at rest", "peaceful". Vocabulary banned from PROMPTS: corpse, dead body, decomposing, rotting, mummified, mummy, skeleton, shrivelled. D3 is image-to-video from its still with minimal motion (the forearms settle 1–2 cm; nothing else moves). Forearms lie LOW across the lower belly/pelvis, as the embalmers laid them, never crossed high on the chest [16 §5]. State at entry: T-C at damage L3, glow G2 (dark), wrist + knee + neck seams cracked.

| Stage | What changes | Camera | Motion |
|---|---|---|---|
| **D1** living face | skin a shade paler, lips dry; nothing else | CU, low warm key from the sunrise | eyes close over 3–4 s; the smile holds |
| **D2** silhouette | no skin detail at all | extreme wide, backlit | a slow lowering, 5–6 s |
| **D3** hands | skin darkens to dry bronze-brown, drawn smooth around the gold wrist seams; the seams look brighter by contrast | insert, 85–100mm, top-light | forearms settle; still |
| **D4** from above | the visible upper face (closed eyes, brow, scalp) is matte dark bronze-brown; the shawl and cornflowers cover mouth and one cheek | top shot, medium | locked-off; only the shawl edge stirs |

**CHAR_TUT_D1 — THE LIVING FACE (first light)**

LONG (65 words):

> close on the face of a slight olive-skinned young man in the first low gold light of sunrise, shaved head with faint stubble, very dark eyes slowly closing, a small peaceful smile over his visible overbite, lips dry, the skin a shade paler than before, the thin gold seam ring at his neck catching the light along a fine hairline crack, calm and at rest

SHORT (24 words; the cross-check replaced a bare "his" so the lock stands on its own):

> a slight young man's face in first sunlight, dark eyes slowly closing, a small peaceful smile, the cracked gold neck seam catching the light

**CHAR_TUT_D2 — THE SILHOUETTE (lowering)**

LONG (61 words):

> a wide backlit silhouette against a huge rising sun on a flat horizon: a woman and a broad-shouldered man gently lower the slight body of a young man onto pale stone steps, his shaved head resting back against the man's arm, one hand hanging loose, a long linen shawl lifting in the dawn wind, no facial detail visible, reverent and unhurried

SHORT (22 words):

> wide backlit silhouette against the rising sun: a woman and a broad-shouldered man gently lower a slight young man onto stone steps

**CHAR_TUT_D3 — THE HANDS (forearms settle low)**

LONG (69 words):

> close shot of two slender hands at rest, the forearms settled low across the lower belly as if laid there by careful hands long ago, the skin darkened to a dry, deep bronze-brown like old parchment, drawn smooth and tight around thin gold seam rings at both wrists, the left seam split by a hairline crack, a fold of cream linen and three blue cornflowers beside them, perfectly still

SHORT (24 words):

> two still hands laid low across the body, skin dry dark bronze-brown like old parchment around thin gold wrist seams, blue cornflowers beside them

**CHAR_TUT_D4 — FROM ABOVE (the shawl and the cornflowers)**

LONG (64 words):

> top-down medium shot of a slight young man lying on pale limestone in soft morning light, a cream linen shawl drawn up over his mouth and one cheek with blue cornflowers scattered across it, only his closed eyes, brow and shaved scalp visible, the skin matte dark bronze-brown like old parchment, the features calm and softly suggested, hands resting low across his body, peaceful

SHORT (25 words):

> from above, a still young man on pale stone, a cream linen shawl and blue cornflowers covering half his face, closed eyes, dark bronze-brown skin

*Desiccation negative (add to every D-stage prompt and still):* horror styling, skeletal features, skull shape, exposed teeth, sunken eye sockets, shrivelled lips, cracked or peeling skin, wounds, blood, grey or green skin, bandage wrappings, insects, decay, gore, morphing, face distortion

**Desiccation reference stills** (these are composed first frames for image-to-video, so 16:9)

1. **CHAR_TUT_D1_still** · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9. Close on the face of a slight olive-skinned young man in the first low gold light of sunrise, shaved head with faint stubble, very dark eyes slowly closing, a small peaceful smile over his visible overbite, lips dry, the skin a shade paler than before, the thin gold seam ring at his neck catching the light along a fine hairline crack, calm and at rest. He lies with his head cradled in a woman's arm (only her sleeve and hand in frame, an olive field-jacket cuff), on the pale limestone of a great stone monument at dawn; warm low sunlight from frame right, deep soft shadow, the sky beyond pale gold. Real human, natural skin texture, shallow depth of field, 85mm lens, fine film grain. Reverent, quiet.

2. **CHAR_TUT_D2_still** · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9. A wide backlit silhouette against a huge rising sun on a flat horizon: a woman and a broad-shouldered man gently lower the slight body of a young man onto pale stone steps, his shaved head resting back against the man's arm, one hand hanging loose, a long linen shawl lifting in the dawn wind, no facial detail visible, reverent and unhurried. The steps are the huge weathered limestone blocks of a pyramid's lower courses; the sun is a white-gold disk just clearing a hazy desert horizon; the figures are pure dark shapes with a thin bright rim of light; dust in the air. 35mm lens, deep focus, fine film grain.

3. **CHAR_TUT_D3_still** · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9. Close shot of two slender hands at rest, the forearms settled low across the lower belly as if laid there by careful hands long ago, the skin darkened to a dry, deep bronze-brown like old parchment, drawn smooth and tight around thin gold seam rings at both wrists, the left seam split by a hairline crack, a fold of cream linen and three blue cornflowers beside them, perfectly still. The hands rest on a stone-dusted white linen tunic; soft even morning light from above; the gold of the seams is warm and polished; reverent and museum-quiet. 100mm macro lens, shallow depth of field, fine film grain.

4. **CHAR_TUT_D4_still** · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9. Top-down medium shot of a slight young man lying on pale limestone in soft morning light, a cream linen shawl drawn up over his mouth and one cheek with blue cornflowers scattered across it, only his closed eyes, brow and shaved scalp visible, the skin matte dark bronze-brown like old parchment, the features calm and softly suggested, hands resting low across his body, peaceful. Seen straight down from above; the pale limestone slab fills the frame around him; the cornflowers are intense blue against the cream linen; soft shadowless dawn light; stillness, dignity, grief. 35mm lens, deep focus, fine film grain.

---

## 2. THE MODERN PRINCIPALS (2033)

### CHAR_NOUR — Dr. Nour KAMEL (38), the lector
*Locked face 2 of 12 · Seq 1–12 + coda · silhouette: olive · SCA-appointed inspector on OSIRIS*

| Field | Lock |
|---|---|
| **Age** | 38 |
| **Ethnicity / heritage** | Egyptian, Cairene (Cairo University philologist). The daughter of a Deaf mother, so a native signer of Egyptian Sign Language and a fluent lip-reader. |
| **Build** | 1.65 m, lean and wiry, quick and economical in movement; she stands with her weight forward. |
| **Face (repeatable features)** | An oval face with defined cheekbones; **thick, straight dark brows**; a **small pale scar nicking the tail of the left eyebrow** (childhood); deep-set dark-brown eyes with faint shadows beneath; a strong straight nose with a slight bump at the bridge; a wide, expressive mouth; faint lines at the eye corners. Minimal makeup. The brows, the deep-set eyes and the nose bump are the family features shared with CHAR_IBRAHIM_1925. |
| **Hair** | Dark brown-black, tightly curly, shoulder-length, **always tied back** in a low loose knot at the nape, with curls escaping at the temples. A few grey threads at the left temple. |
| **Skin** | Warm light-brown (medium olive), with natural texture and faint sun-freckling on the cheekbones. |
| **Eyes** | Dark brown and deep-set; an intent, lip-reading focus (she watches mouths). |
| **Voice** | A low, quick, precise alto. Cairene Arabic; English with a light Egyptian accent and a scholar's exactness; Late and Middle Egyptian read carefully, never theatrically ("I'm reading, not praying"). Sardonic under pressure, fierce about Layla. |
| **Anchors (bible §6)** | dark curly shoulder-length hair tied back · reading glasses on a cord · olive field jacket (plus the small silver cartouche pendant; its lettering is COMP only) |

**LONG look-lock** (66 words, paste verbatim):

> a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket

**SHORT look-lock** (22 words, paste verbatim):

> a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, headscarf, heavy makeup, glamour hair, loose flowing hair, round glasses, tortoiseshell glasses, readable text on the pendant

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1–3, and the coda (a fresh set) | An olive cotton field jacket (four flap pockets, sleeves pushed to mid-forearm); a cream linen shirt; slim charcoal trousers; brown leather lace-up ankle boots; **narrow black half-frame reading glasses on a thin black cord**; a small silver cartouche pendant on a fine silver chain (PROP_LAYLA_PENDANT; the name LAYLA is COMP when legible); an SCA inspector's lanyard badge with no readable text; a fountain pen. At home (2.5): the jacket over a chair, the glasses on. | *wearing an olive cotton field jacket with four flap pockets over a cream linen shirt, charcoal trousers, brown leather ankle boots, a small silver pendant on a fine chain* |
| **B** | 4 (the gala) → 9.8 (her trade at Amarna) | She works the gala as inspector: the same olive field jacket over a black silk blouse and black trousers, black leather ankle boots, the glasses on their cord, the pendant. She runs in this for four days. | *wearing an olive cotton field jacket over a black silk blouse and black trousers, black leather ankle boots, a small silver pendant on a fine chain* |
| **C** | 9.8 → 12 (captive; the Hall) | B at damage L2, the face washed (SESHAT's care), the jacket dusty. In the Hall (Seq 12) she wears a **long cream linen shawl as a lector's sash**, from the left shoulder across the chest to the right hip (PROP_LINEN_SHAWL), and holds a tablet showing Layla asleep (PROP_TABLET_LAYLA; the image is CHAR_LAYLA_ASLEEP_MASTER). She drapes the shawl on Tut when he arrives (12.3); at dawn it covers his face (D4). | *wearing a dusty olive field jacket over a black blouse and black trousers, a long cream linen shawl worn across her chest from the left shoulder like a sash* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–4 L0 · Seq 5–6 L1 (paste *clothes creased, river-damp at the cuffs, curls coming loose*) · Seq 7–9 L2 (paste *jacket and trousers grey with sandstone dust, the right jacket cuff torn*; in Seq 8 add *white plaster dust in her hair and on her shoulders*) · Seq 10–12 L2, face clean.
- **Glasses:** always on the cord. She puts them on only to read (block, wall, tablet).
- **Seq 7.4:** she tips the cart into the river; sleeves wet to the elbow for the rest of the sequence.
- **Seq 12:** the shawl leaves her at 12.3; from D1 onward she wears C without it.
- **Coda:** A, clean, with the pendant; cornflowers in hand at KV21.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) reading lips: eyes narrowed and locked on a mouth off camera, lips slightly parted · (2) fierce: jaw set, chin down, eyes hard

**Reference stills** (image generator; self-contained)

1. **CHAR_NOUR_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: an olive cotton field jacket with four flap pockets over a cream linen shirt, charcoal trousers, brown leather ankle boots, a small silver pendant on a fine chain. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_NOUR_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: an olive cotton field jacket with four flap pockets over a cream linen shirt, charcoal trousers, brown leather ankle boots, a small silver pendant on a fine chain. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_NOUR_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: an olive cotton field jacket with four flap pockets over a cream linen shirt, charcoal trousers, brown leather ankle boots, a small silver pendant on a fine chain. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_NOUR_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: an olive cotton field jacket with four flap pockets over a cream linen shirt, charcoal trousers, brown leather ankle boots, a small silver pendant on a fine chain. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_NOUR_B_full** (full body, wardrobe B) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: an olive cotton field jacket over a black silk blouse and black trousers, black leather ankle boots, a small silver pendant on a fine chain. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

6. **CHAR_NOUR_C_full** (full body, wardrobe C (the Hall)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean thirty-eight-year-old Egyptian woman with warm light-brown skin, dark curly shoulder-length hair tied back at the nape with loose curls at the temples, thick straight dark brows, a small pale scar through the tail of the left eyebrow, deep-set dark-brown eyes, a strong straight nose with a slight bump, a wide expressive mouth, narrow black reading glasses hanging on a cord, an olive field jacket. Costume: a dusty olive field jacket over a black blouse and black trousers, a long cream linen shawl worn across her chest from the left shoulder like a sash. Holding a thin tablet computer at her side, screen facing her; clothes lightly dusty. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, headscarf, heavy makeup, glamour hair, loose flowing hair, round glasses, tortoiseshell glasses, readable text on the pendant

---

### CHAR_ADAEZE — Dr. Adaeze OKORO (44), the alignment scientist
*Locked face 3 of 12 · Seq 1–12 · silhouette: navy · HELIOS head of alignment*

| Field | Lock |
|---|---|
| **Age** | 44 |
| **Ethnicity / heritage** | British-Nigerian (Igbo heritage), raised in South London. |
| **Build** | 1.78 m, tall and solid, with athletic shoulders; a planted, deliberate stance. From 10.4, a left-leg limp. |
| **Face (repeatable features)** | A broad high forehead; wide-set dark eyes; rounded cheekbones; a broad nose; full lips with a **small gap between the upper front teeth** (seen when she speaks); a **faint vertical worry line between the brows**; **round tortoiseshell glasses**, always on. |
| **Hair** | Close-cropped natural black hair, a few millimetres long, with grey flecks at the temples. |
| **Skin** | Deep brown with warm undertones and natural texture. |
| **Eyes** | Dark brown, wide-set, amused and appraising behind the glasses. |
| **Voice** | Crisp South London vowels; dry, literal, deadpan; quotes papers by author and year; gallows humour under fire. |
| **Anchors (bible §6)** | close-cropped natural hair · round tortoiseshell glasses · navy blazer over a grey hoodie |

**LONG look-lock** (57 words, paste verbatim):

> a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie

**SHORT look-lock** (21 words, paste verbatim):

> a tall British-Nigerian woman of forty-four, deep brown skin, close-cropped natural hair, round tortoiseshell glasses, navy blazer over a grey hoodie

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, long hair, braids, wig, headwrap, rectangular glasses, black-rimmed glasses, business suit, readable laptop stickers

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 4.4 | A navy wool blazer; a heather-grey hoodie, hood down; dark indigo jeans; plain white canvas trainers (no logos); a lanyard with a blank HELIOS badge; a battered dark-grey laptop with a cracked corner and no stickers; a dog-eared stack of white ruled index cards held by a black binder clip (PROP_INDEX_CARDS). | *wearing a navy wool blazer over a heather-grey hoodie, dark indigo jeans, plain white canvas trainers, a lanyard with a blank badge* |
| **B** | 4.4 → 10.4 | A, lived in: blazer sleeves pushed to the forearm, the hood UP for night wides, the laptop and cards in a canvas shoulder bag. From Seq 7, Rami's conservation kit (PROP_CONSERVATION_KIT). From 8.4, a red-light headlamp worn on the forehead or round the neck. From 9.2, **vivid Egyptian-blue powder** on her fingers, cuffs and blazer front. | *wearing a creased navy blazer with the sleeves pushed up over a grey hoodie, dark jeans, grubby white trainers, a canvas shoulder bag* |
| **C** | 10.4 → 12 | B at damage L3, plus the **leg injury**: the left jeans leg torn open from knee to mid-shin and bound with a clean khaki field bandage over the denim below the knee; a pronounced left-leg limp. No blood. Seq 11.3: soaked to the chest in the Osiris Shaft, then drying, with the hoodie darker and the blazer heavy. | *wearing a dusty navy blazer over a grey hoodie, dark jeans with the left leg torn below the knee and bound with a khaki field bandage, grubby white trainers* |
| **D** | coda (the hearing, weeks later; seq_12) | Clean again: the navy wool blazer over the heather-grey hoodie, dark indigo jeans, clean white trainers; the round tortoiseshell glasses; a plain black aluminium walking cane hooked on her chair (the leg is healing; no bandage in view). Seated behind Hale, soft focus. | *wearing a clean navy wool blazer over a heather-grey hoodie, dark indigo jeans, a plain black walking cane hooked on her chair* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–4 L0 · Seq 5–6 L1 (*creased, river-damp*) · Seq 7–9 L2 (*dusty, a torn blazer pocket*; the blue powder from 9.2: paste *vivid blue powder smudged on her fingers and blazer front*) · Seq 10–12 L3 (*heavy stone dust and soot*).
- **Injury (from 10.4):** the bandaged left leg and the limp, through the end of the film. Keep the bandage clean khaki, never stained.
- **Seq 11.3:** wet to the chest; add *clothes soaked dark and clinging*, then *drying, water tide-lines*.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) deadpan: one eyebrow raised over the glasses, mouth flat · (2) shock held in check: eyes wide, lips pressed

**Reference stills** (image generator; self-contained)

1. **CHAR_ADAEZE_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a navy wool blazer over a heather-grey hoodie, dark indigo jeans, plain white canvas trainers, a lanyard with a blank badge. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_ADAEZE_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a navy wool blazer over a heather-grey hoodie, dark indigo jeans, plain white canvas trainers, a lanyard with a blank badge. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_ADAEZE_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a navy wool blazer over a heather-grey hoodie, dark indigo jeans, plain white canvas trainers, a lanyard with a blank badge. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_ADAEZE_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a navy wool blazer over a heather-grey hoodie, dark indigo jeans, plain white canvas trainers, a lanyard with a blank badge. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_ADAEZE_B_full** (full body, wardrobe B (after 9.2)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a creased navy blazer with the sleeves pushed up over a grey hoodie, dark jeans, grubby white trainers, a canvas shoulder bag. Vivid blue pigment powder smudged on her fingers, cuffs and blazer front; a red headlamp round her neck. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

6. **CHAR_ADAEZE_C_full** (full body, wardrobe C (the leg)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, solidly built British-Nigerian woman of forty-four with deep brown skin, close-cropped natural black hair flecked grey at the temples, round tortoiseshell glasses, wide-set dark eyes, a broad forehead and rounded cheekbones, full lips with a small gap between her front teeth, a faint worry line between the brows, a navy blazer over a grey hoodie. Costume: a dusty navy blazer over a grey hoodie, dark jeans with the left leg torn below the knee and bound with a khaki field bandage, grubby white trainers. Weight on her right leg, favouring the bandaged left leg; clothes heavily dusted with pale stone dust. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, long hair, braids, wig, headwrap, rectangular glasses, black-rimmed glasses, business suit, readable laptop stickers

---

### CHAR_TOMAS — Dr. Tomas LINDQVIST (50), "Anubis"
*Locked face 4 of 12 · Seq 1–12 · the bioengineer who rebuilt the body*

| Field | Lock |
|---|---|
| **Age** | 50 |
| **Ethnicity / heritage** | Swedish. |
| **Build** | 1.93 m, lanky and long-limbed, with a slight stoop from years over lab benches; large, careful hands. |
| **Face (repeatable features)** | A long, narrow face; a high forehead; **deep-set pale blue-grey eyes with heavy crow's feet**; a long straight nose; a **full, short-trimmed grey beard** (darker grey at the chin); a prominent Adam's apple. |
| **Hair** | Thinning ash-grey hair swept straight back, receding at the temples. |
| **Skin** | Pale, sun-reddened on the nose and forehead, freckled. |
| **Eyes** | Pale blue-grey; gentle, tired, guilty. |
| **Voice** | Soft and measured, with Swedish-accented English; an engineer's precision; never raised. |
| **Anchors (bible §6)** | tall · grey beard · rolled shirtsleeves |

**LONG look-lock** (55 words, paste verbatim):

> a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows

**SHORT look-lock** (21 words, paste verbatim):

> a very tall, lanky Swedish man of fifty, full short grey beard, thinning swept-back grey hair, pale-blue shirt with rolled sleeves

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, long beard, ponytail, lab coat, tie, glasses

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 4.4 | A pale-blue cotton oxford shirt, sleeves **rolled above the elbows**; charcoal chinos; a brown leather belt; brown suede desert boots; a plain unbranded steel wristwatch; a pen in the breast pocket. In the lab, blue nitrile gloves. | *wearing a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch* |
| **B** | 4.4 → 8.6 | A at damage L1–L2. At 6.2 (the port surgery) and 8.5 (the heart), a small white LED headlamp on an elastic strap round his forehead, and blue nitrile gloves. | *wearing a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch* |
| **C** | 8.6 → 12.6 (captive; he dies in the Hall) | B, grey with dust, the shirt **torn at the left shoulder seam**, the watch gone, no headlamp. He is never shown bound. | *wearing a grey-dusted pale-blue oxford shirt torn at the left shoulder seam, sleeves rolled above the elbows, dusty charcoal chinos, desert boots* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–4 L0 · Seq 5–6 L1 · Seq 7–8 L2 · Seq 9–12 L2 (captive, unchanged).
- **Death (12.6):** kill grammar only (bible §3.3): impact on stone, he drops out of frame, Nour's reaction. No wound in frame.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) gentle guilt: a small apologetic smile, eyes down · (2) the engineer's focus: brows drawn, mouth closed

**Reference stills** (image generator; self-contained)

1. **CHAR_TOMAS_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. Costume: a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_TOMAS_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. Costume: a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_TOMAS_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. Costume: a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_TOMAS_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. Costume: a pale-blue cotton oxford shirt with the sleeves rolled above the elbows, charcoal chinos, a brown leather belt, brown suede desert boots, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_TOMAS_B_headlamp** (Seq 6.2 / 8.5 working look) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: head and shoulders, front view, eyes looking down at his work below frame, concentrating. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. A small white LED headlamp on an elastic strap round his forehead, switched off; blue nitrile gloves on his raised hands. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6.

6. **CHAR_TOMAS_C_full** (full body, wardrobe C (captive)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a very tall, lanky Swedish man of fifty with a slight stoop, pale sun-reddened skin, a long narrow face, a full short-trimmed grey beard, thinning ash-grey hair swept back from a high forehead, deep-set pale blue-grey eyes with heavy crow's feet, a long straight nose, a pale-blue shirt with the sleeves rolled above the elbows. Costume: a grey-dusted pale-blue oxford shirt torn at the left shoulder seam, sleeves rolled above the elbows, dusty charcoal chinos, desert boots. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, long beard, ponytail, lab coat, tie, glasses

---

### CHAR_TAREK — Colonel Tarek MANSOUR (52), the soldier
*Locked face 5 of 12 · Seq 1–11 (dies 11.3) · Egyptian Army security liaison to the GEM*

| Field | Lock |
|---|---|
| **Age** | 52 |
| **Ethnicity / heritage** | Egyptian (a career army officer). |
| **Build** | 1.80 m, barrel-chested and thick-necked, ramrod-upright; he moves little and exactly. |
| **Face (repeatable features)** | A square, weathered face; a **heavy, neatly trimmed grey moustache**; heavy-lidded dark eyes under thick grey-black brows; **deep vertical frown lines** between the brows; a **nose once broken and set slightly to the left**; a firm jaw. |
| **Hair** | Close-cropped grey hair, seen at the temples under the beret. |
| **Skin** | Deep-tanned and weathered, with sun creases at the eyes and neck. |
| **Eyes** | Dark and heavy-lidded; he hides brown half-frame reading glasses in his left breast pocket and is caught using them once. |
| **Voice** | Deep and gravelly; few words, clipped and exact; formal English; Egyptian Arabic with his men; one dry joke per act. |
| **Anchors (bible §6)** | grey moustache · beret · desert-camouflage uniform |

**LONG look-lock** (56 words, paste verbatim):

> a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform

**SHORT look-lock** (16 words, paste verbatim):

> a barrel-chested Egyptian colonel of fifty-two, heavy grey moustache, black beret, weathered deep-tanned face, desert-camouflage uniform

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, real military unit patches, readable insignia or name tapes, flags, medals, sunglasses, beard, helmet

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 4.4 | A pressed Egyptian-army-style desert-camouflage uniform (a tan, sand and brown pattern) with the sleeves down; a **black beret** pulled low to the right with a small brass cap badge; subdued shoulder-board rank insignia (nothing legible); tan leather combat boots; a holstered pistol; a radio handset clipped at the left shoulder. The reading glasses are hidden in the left breast pocket. | *wearing a pressed desert-camouflage army uniform in tan, sand and brown with the sleeves down, a black beret with a small brass badge, subdued shoulder-board rank insignia, tan combat boots, a holstered pistol* |
| **B** | 4.4 → 11.3 | Sleeves rolled to the elbow; a tan load-bearing vest with pouches; a generic unbranded rifle, slung; the beret always on. He gave his spare charcoal field jacket to Tut in 4.4 and never wears one himself. | *wearing a dusty desert-camouflage army uniform with sleeves rolled to the elbow, a tan load-bearing vest, a black beret, a rifle slung across his chest* |
| **C** | 11.3 (the Osiris Shaft) | B, soaked; chest-deep in dark water, his face wet, the beret still on. He goes under: shown as a hand, the water and the sound. | *wearing a soaked desert-camouflage uniform and black beret, chest-deep in dark water* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–4 L0 · Seq 5–6 L1 · Seq 7–9 L2 (plus *black diesel grease on his hands and forearms* in Seq 9.1–9.3, from the locomotive) · Seq 10–11 L3.
- **Death (11.3):** seen through water, as a hand and sound. Never a face under water.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the refusal: chin up, eyes flat, a small unreadable pause · (2) a rare dry smile under the moustache

**Reference stills** (image generator; self-contained)

1. **CHAR_TAREK_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform. Costume: a pressed desert-camouflage army uniform in tan, sand and brown with the sleeves down, a black beret with a small brass badge, subdued shoulder-board rank insignia, tan combat boots, a holstered pistol. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_TAREK_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform. Costume: a pressed desert-camouflage army uniform in tan, sand and brown with the sleeves down, a black beret with a small brass badge, subdued shoulder-board rank insignia, tan combat boots, a holstered pistol. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_TAREK_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform. Costume: a pressed desert-camouflage army uniform in tan, sand and brown with the sleeves down, a black beret with a small brass badge, subdued shoulder-board rank insignia, tan combat boots, a holstered pistol. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_TAREK_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform. Costume: a pressed desert-camouflage army uniform in tan, sand and brown with the sleeves down, a black beret with a small brass badge, subdued shoulder-board rank insignia, tan combat boots, a holstered pistol. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_TAREK_B_full** (full body, wardrobe B) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a barrel-chested Egyptian army colonel of fifty-two, very upright, deep-tanned weathered skin, a square face with a heavy neatly trimmed grey moustache, close-cropped grey hair under a black beret worn low to the right, heavy-lidded dark eyes beneath thick grey-black brows, deep vertical frown lines, a nose once broken and set slightly left, a desert-camouflage uniform. Costume: a dusty desert-camouflage army uniform with sleeves rolled to the elbow, a tan load-bearing vest, a black beret, a rifle slung across his chest. Clothes dusty, sleeves rolled. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, real military unit patches, readable insignia or name tapes, flags, medals, sunglasses, beard, helmet

---

### CHAR_FATHI — Sergeant Fathi ABDEL-RAHMAN (31), the combat engineer
*Locked face 6 of 12 · Seq 1–12 (survives) · silhouette: red scarf · from Aswan*

| Field | Lock |
|---|---|
| **Age** | 31 |
| **Ethnicity / heritage** | Nubian Egyptian from Aswan; he speaks Nobiin and Egyptian Arabic. Written as the unit's tactical mind, never a servant type. |
| **Build** | 1.85 m, broad-shouldered and powerful, an athlete's ease; he carries Tut at dawn without strain. |
| **Face (repeatable features)** | A **close-trimmed full black beard**; a broad nose; high rounded cheekbones; a wide, generous mouth with bright even teeth; a strong brow; calm, amused eyes. |
| **Hair** | Short, tightly curled black hair. |
| **Skin** | Deep dark brown with a warm undertone, with natural sheen and texture. Light it with care: every night scene names a key light that reaches his face. |
| **Eyes** | Dark brown, calm and warm, missing nothing. |
| **Voice** | A warm baritone and an easy laugh; Egyptian Arabic with Tarek, a few Nobiin words; English with humour. He calls Tut "ya Malik". His private du'a is hands raised, lips moving, no sound. |
| **Anchors (bible §6)** | broad-shouldered · close beard · red-patterned scarf worn at the neck |

**LONG look-lock** (56 words, paste verbatim):

> a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled

**SHORT look-lock** (20 words, paste verbatim):

> a broad-shouldered Nubian Egyptian soldier of thirty-one, deep dark-brown skin, close black beard, red-patterned scarf at the neck, desert camouflage

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, facial scars or tribal marks, turban, keffiyeh headdress, helmet, real unit patches, readable insignia, servant or porter styling

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 4.4 | A desert-camouflage uniform, sleeves rolled above the elbow; a black beret (GEM duty); **a faded brick-red cotton scarf with a small white geometric diamond pattern, knotted loosely at the throat** (his signature); a combat engineer's chest rig with pouches; tan combat boots; a generic rifle. | *wearing a desert-camouflage army uniform with the sleeves rolled above the elbow, a black beret, a faded brick-red patterned scarf knotted at the neck, a combat engineer's chest rig with pouches, tan combat boots* |
| **B** | 4.4 → 12 (to dawn) | Bareheaded (the beret folded under his left shoulder strap); the red scarf; the chest rig; a canvas demolition satchel worn across the body; a coil of cord at the hip. From 11.5, **Tut's meteoritic dagger** in his right hand or at his belt (PROP_DAGGER). Not in the shaft, so dry in Seq 11. | *wearing a dusty desert-camouflage uniform with rolled sleeves, a faded brick-red patterned scarf at the neck, a chest rig, a canvas demolition satchel slung across his body, bareheaded* |
| **C** | coda (the Tutankhamun galleries, weeks later; seq_12) | A clean, pressed desert-camouflage uniform with the sleeves rolled above the elbow, the faded brick-red patterned scarf knotted at the neck, a black beret; no chest rig, no satchel. He holds PROP_DAGGER out hilt first to CHAR_CONSERVATOR_2033. | *wearing a clean desert-camouflage army uniform with the sleeves rolled above the elbow, a faded brick-red patterned scarf knotted at the neck, a black beret* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–4 L0 · Seq 5–6 L1 (*river-wet to the knees*) · Seq 7–9 L2 · Seq 10–12 L3 (*soot and stone dust, the chest-rig pouches empty*).
- **Seq 12.7:** carries Tut out into first light, with the dagger at his belt.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a warm, wide grin · (2) the tactical read: eyes narrowed, head tilted, listening

**Reference stills** (image generator; self-contained)

1. **CHAR_FATHI_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with the sleeves rolled above the elbow, a black beret, a faded brick-red patterned scarf knotted at the neck, a combat engineer's chest rig with pouches, tan combat boots. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_FATHI_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with the sleeves rolled above the elbow, a black beret, a faded brick-red patterned scarf knotted at the neck, a combat engineer's chest rig with pouches, tan combat boots. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_FATHI_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with the sleeves rolled above the elbow, a black beret, a faded brick-red patterned scarf knotted at the neck, a combat engineer's chest rig with pouches, tan combat boots. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_FATHI_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with the sleeves rolled above the elbow, a black beret, a faded brick-red patterned scarf knotted at the neck, a combat engineer's chest rig with pouches, tan combat boots. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_FATHI_B_full** (full body, wardrobe B) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, broad-shouldered Nubian Egyptian soldier of thirty-one with deep dark-brown skin, a close-trimmed full black beard, short tightly curled black hair, a broad nose and high rounded cheekbones, calm warm dark eyes, a wide generous mouth, a faded brick-red scarf with a small white diamond pattern knotted at his neck, desert-camouflage uniform with sleeves rolled. Costume: a dusty desert-camouflage uniform with rolled sleeves, a faded brick-red patterned scarf at the neck, a chest rig, a canvas demolition satchel slung across his body, bareheaded. Clothes dusty; a generic rifle held low, pointed at the floor. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, facial scars or tribal marks, turban, keffiyeh headdress, helmet, real unit patches, readable insignia, servant or porter styling

---

### CHAR_RAMI — RAMI FAWZY (27), junior HELIOS engineer
*Locked face 7 of 12 · Seq 1–7 (dies 7.4) · silhouette: yellow windbreaker · keeper of "100 Questions for Tutankhamun"*

| Field | Lock |
|---|---|
| **Age** | 27 |
| **Ethnicity / heritage** | Egyptian, from Cairo (Shubra). |
| **Build** | 1.72 m, wiry and thin, never still; he talks with his hands. |
| **Face (repeatable features)** | A narrow face; **big, expressive dark eyebrows** that never stop moving; large dark eyes behind **black-rimmed rectangular glasses**; slightly prominent ears; a wide mouth with a **small chip in the upper-left front tooth**; clean-shaven. |
| **Hair** | Short black hair, faded at the sides, thick and wavy on top. |
| **Skin** | Light olive. |
| **Eyes** | Dark brown, large, delighted. |
| **Voice** | Fast and bright: Cairene slang and pop-culture English ("I once met a national-team striker's cousin"). |
| **Anchors (bible §6)** | young, clean-shaven · black-rimmed glasses · yellow HELIOS windbreaker (later a splint on the left hand) |

**LONG look-lock** (58 words, paste verbatim):

> a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker

**SHORT look-lock** (18 words, paste verbatim):

> a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, beard, moustache, round glasses, readable logo or lettering on the windbreaker, brand logos on clothing or shoes

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 3.6 | A bright yellow zip-up windbreaker with a small embroidered black sun-disk emblem on the left chest and no lettering (HELIOS); a plain charcoal t-shirt; black jeans; grey trainers with no logos; a lanyard with a blank badge; the battered mustard-yellow A5 hardback notebook with a black elastic band (PROP_RAMI_NOTEBOOK; its title is COMP). In 2.1 he drinks from the gift-shop mug (PROP_GIFT_MUG). | *wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers* |
| **B** | 3.6 → 7.4 | A, plus the **broken fingers**: an aluminium-and-foam finger splint along the ring and little fingers of the LEFT hand, bound with white medical tape, the hand held close to his chest. In Seq 4 he carries the grey hard-shell conservation kit case (PROP_CONSERVATION_KIT) in his right hand. At Karnak (Seq 7), the right windbreaker elbow is torn. | *wearing a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape* |

**Progression: dirt, damage, injuries, props carried**

- **Damage by sequence:** Seq 1–3 L0 · Seq 4–6 L1 (*creased, river-damp*; the splint grubby) · Seq 7 L2 (*sandstone dust, the right sleeve torn at the elbow*).
- **Injury (3.6):** the fingers break off screen (a crack, a cradled hand). The splint appears from the next scene on and stays until his death.
- **Death (7.4):** kill grammar at the quay's edge; Tut takes the notebook from his jacket.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the grin: eyebrows up, the chipped tooth showing · (2) wonder: mouth open, eyes wet behind the glasses

**Reference stills** (image generator; self-contained)

1. **CHAR_RAMI_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker. Costume: a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_RAMI_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker. Costume: a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_RAMI_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker. Costume: a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_RAMI_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker. Costume: a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_RAMI_B_full** (full body, wardrobe B (splint)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a wiry, thin Egyptian man of twenty-seven with light olive skin, clean-shaven, a narrow face with big expressive dark eyebrows, large dark eyes behind black-rimmed rectangular glasses, slightly prominent ears, short black hair faded at the sides and thick and wavy on top, a wide mouth with a small chip in one front tooth, a bright yellow windbreaker. Costume: a bright yellow zip-up windbreaker with a small black sun-disk emblem on the chest and no lettering, a plain charcoal t-shirt, black jeans, grey trainers, his left hand in a finger splint bound with white tape. The splinted left hand held close to his chest; a grey hard-shell equipment case in his right hand. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, beard, moustache, round glasses, readable logo or lettering on the windbreaker, brand logos on clothing or shoes

---

### CHAR_HALE — VICTOR HALE (60), founder of HELIOS (renamed from "Vance" in v3)
*Locked face 8 of 12 · Seq 1–4, asleep in the Garden, then the coda · a believer, not a villain*

| Field | Lock |
|---|---|
| **Age** | 60 |
| **Ethnicity / heritage** | American (Californian). Must not resemble any real technology executive, investor or politician. |
| **Build** | 1.85 m, lean with a long-distance runner's build, straight-backed, still. |
| **Face (repeatable features)** | A long, lean face with a **deep, even tan**; prominent cheekbones and hollow cheeks; pale grey-green eyes with fine crow's feet; a narrow straight nose; thin lips with a practised small smile; a clean-shaven, strong chin with a **thin pale scar along the left jawline**. |
| **Hair** | Thick silver hair **swept straight back** from the forehead to the collar, immaculate. |
| **Skin** | Tanned and lean, with fine sun lines. |
| **Eyes** | Pale grey-green, calm, persuasive. |
| **Voice** | Soft, warm, mid-Atlantic; a salesman's calm; he never hurries. |
| **Anchors (bible §6)** | silver swept-back hair · tanned, lean face · charcoal suit with an open collar |

**LONG look-lock** (64 words, paste verbatim):

> a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt

**SHORT look-lock** (21 words, paste verbatim):

> a lean American man of sixty, silver hair swept straight back, tanned lean face, charcoal suit with an open-collared white shirt

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, resemblance to any real tech founder, turtleneck, hoodie, tie (except wardrobe C), jewellery, lapel pins, logos

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1 → 4.3 | A charcoal wool two-piece suit; a crisp white shirt open two buttons at the collar; no tie; black leather shoes; a plain unbranded steel wristwatch; no pin, no logo. | *wearing a charcoal wool two-piece suit and a crisp white shirt open at the collar, no tie, black leather shoes, a plain steel wristwatch* |
| **B** | 4.3 → 12.8 (asleep in the Garden) | A, creased, the jacket on; he lies on a pale mat under soft white light. From the midpoint broadcast (7.3) a **thin silver bracelet on the left wrist** (PROP_SLEEP_BRACELET, "for sunrise"). | *wearing a creased charcoal suit and open-collared white shirt, a thin silver bracelet on his left wrist, asleep* |
| **C** | coda (the hearing) | The charcoal suit with a white shirt buttoned to the collar and, for the first time, a plain dark tie; no bracelet; his hair slightly less perfect. He looks older. | *wearing a charcoal wool suit, a white shirt buttoned to the collar with a plain dark tie, black leather shoes* |

**Progression: dirt, damage, injuries, props carried**

- Always L0 on screen; B only adds creasing. The bracelet appears from 7.3 until the waking (12.8).

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the believer's smile: warm, certain, eyes shining · (2) the hearing: flat, tired, eyes down

**Reference stills** (image generator; self-contained)

1. **CHAR_HALE_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt. Costume: a charcoal wool two-piece suit and a crisp white shirt open at the collar, no tie, black leather shoes, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_HALE_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt. Costume: a charcoal wool two-piece suit and a crisp white shirt open at the collar, no tie, black leather shoes, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_HALE_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt. Costume: a charcoal wool two-piece suit and a crisp white shirt open at the collar, no tie, black leather shoes, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_HALE_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt. Costume: a charcoal wool two-piece suit and a crisp white shirt open at the collar, no tie, black leather shoes, a plain steel wristwatch. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_HALE_C_full** (full body, wardrobe C (coda)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean, tall American man of sixty with a runner's build, thick silver hair swept straight back from the forehead, a tanned, lean face with prominent cheekbones and hollow cheeks, pale grey-green eyes with fine crow's feet, a narrow straight nose, thin lips, a clean-shaven strong chin with a thin pale scar along the left jaw, a charcoal suit with an open-collared white shirt. Costume: a charcoal wool suit, a white shirt buttoned to the collar with a plain dark tie, black leather shoes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, resemblance to any real tech founder, turtleneck, hoodie, tie (except wardrobe C), jewellery, lapel pins, logos

---

### CHAR_LAYLA — LAYLA KAMEL (9), Nour's daughter
*Locked face 9 of 12 · Seq 2, 4, captivity intercuts (image only), 12.8 · silhouette: yellow raincoat · MINORS RULE applies (bible §3.3)*

| Field | Lock |
|---|---|
| **Age** | 9 (cast and sheet as a real nine-year-old; never older-styled) |
| **Ethnicity / heritage** | Egyptian, Cairene. |
| **Build** | About 1.30 m, small for her age, quick and fearless. |
| **Face (repeatable features)** | A round face with full cheeks; a **dimple in the right cheek**; big dark-brown eyes with long lashes; a small upturned nose; a **gap-toothed smile, one new front tooth half grown in**. |
| **Hair** | Thick dark-brown curly hair in **two bouncy pigtails** set high at the sides, tied with yellow elastic bands. |
| **Skin** | Warm light-brown. |
| **Eyes** | Big, dark brown, curious. |
| **Voice** | Quick and funny; Egyptian Arabic with her mother (subtitled), school English; she knows the Tut galleries by heart. On waking: "Mama, I dreamed about the king." |
| **Anchors (bible §6)** | two curly pigtails · a yellow raincoat · a glow-in-the-dark scarab keyring (hers until she gives it to Tut in 2.4) |

**LONG look-lock** (63 words, paste verbatim):

> a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat

**SHORT look-lock** (16 words, paste verbatim):

> a small nine-year-old Egyptian girl, round face, big dark eyes, two curly pigtails, bright yellow raincoat

**Character negative** (append to the shot NEGATIVE and to every still below): makeup, jewellery, older-styled, adult clothing, any robot or machine touching her, medical equipment, tubes, bracelets, readable text on clothing

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 2.4 (the night galleries) | A bright yellow knee-length hooded raincoat (matte, unbranded); a navy long-sleeved t-shirt; dark grey leggings; white canvas sneakers; a small pale-green glow-in-the-dark plastic scarab keyring clipped to the zip (PROP_SCARAB_KEYRING), which she gives to Tut in this scene; a gift-shop hieroglyph stencil and a glow pen (PROP_LAYLA_STENCIL; seq_02). | *wearing a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers, a small pale-green plastic scarab keyring clipped to the raincoat zip* |
| **B** | 4 (the gala) → 12.8 | A navy velvet party dress with the yellow raincoat over it (she refused to take it off); white tights; black shoes; no keyring. **Asleep:** only in the ONE approved master image (see below), reused as a composite on every tablet and in Nour's one-minute hold. **Wakes (12.8):** in a medium shot, with no unit in frame, her pigtails loosened and sleep-creased. **No bracelet**: the bracelets are on adult wrists only. | *wearing a bright yellow knee-length hooded raincoat over a navy velvet party dress, white tights, black shoes* |
| **C** | coda (KV21, weeks later; seq_12) | The bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers. **No keyring** (she gave it to Tut in 2.4). Holding Nour's hand. | *wearing a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers* |

**Progression: dirt, damage, injuries, props carried**

- Always clean. The only change is sleep-creasing and loosened pigtails at 12.8.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a gap-toothed grin, dimple showing · (2) a serious, sympathetic frown: "Are you sad?"

**Notes:** Never in the same frame as a unit touching her; never shown being carried by a unit; never with tubes, drips or bracelets.

**Reference stills** (image generator; self-contained)

1. **CHAR_LAYLA_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat. Costume: a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers, a small pale-green plastic scarab keyring clipped to the raincoat zip. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_LAYLA_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat. Costume: a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers, a small pale-green plastic scarab keyring clipped to the raincoat zip. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_LAYLA_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat. Costume: a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers, a small pale-green plastic scarab keyring clipped to the raincoat zip. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_LAYLA_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat. Costume: a bright yellow knee-length hooded raincoat over a navy long-sleeved t-shirt and dark grey leggings, white canvas sneakers, a small pale-green plastic scarab keyring clipped to the raincoat zip. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_LAYLA_B_full** (full body, wardrobe B (the gala)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a small, bright nine-year-old Egyptian girl with warm light-brown skin, a round face with full cheeks and a dimple in the right cheek, big dark-brown eyes with long lashes, a small upturned nose, a gap in her front teeth where a new tooth is half grown in, thick dark curly hair in two bouncy pigtails tied with yellow bands, a bright yellow raincoat. Costume: a bright yellow knee-length hooded raincoat over a navy velvet party dress, white tights, black shoes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

6. **CHAR_LAYLA_ASLEEP_MASTER** (THE ONE APPROVED ASLEEP IMAGE (bible §3.3)) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: soft, even daylight. A small nine-year-old Egyptian girl with a round face and thick dark curly hair in two loosened pigtails sleeps peacefully on her side on a pale grey blanket on a polished stone floor, a soft cream blanket tucked over her to the shoulders, her yellow raincoat folded under her cheek as a pillow, her lips slightly parted, her face calm. She is alone in the frame. Warm, gentle, safe; shallow depth of field, 85mm lens, fine film grain.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, makeup, jewellery, older-styled, adult clothing, any robot or machine touching her, medical equipment, tubes, bracelets, readable text on clothing

---

## 3. THE FATHER: the forecast (2033) and the real king (c. 1336 BC)

### CHAR_AKHENATEN — AKHENATEN, "the Father": the FORECAST (2033); the same actor plays the real king (CHAR_AKHENATEN_1336)
*Locked face 10 of 12 · Seq 4 (broadcast, if used), 7.3 (40 m projection), 9, the captivity intercuts, 11–12 · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | The body looks late twenties (grown from the KV55 genome, whose bones earlier anatomists aged 20–25 [01 §8; 16 §9]: "Your bones are twenty-five"). The real king in the Amarna memory is played at about 35 (CHAR_AKHENATEN_1336). |
| **Ethnicity / heritage** | Egyptian of the Nile valley (Tut's father by the 2010 DNA study, "most probably" Akhenaten [01 §8]). A real man, **never the stylised Amarna sculpture proportions**, never alien (critique ?-14). |
| **Build** | About 1.72 m, slender and long-limbed, with narrow shoulders and a long neck; slow, open, generous gestures. No exaggerated belly or hips. |
| **Face (repeatable features)** | **A naturalistic human face with a long jaw and a long chin, full sculpted lips and heavy lids**; a long straight nose; high cheekbones. It shares the father-son echo with Tut (full lips, the long face) but **no overbite**. His skin is flawless and too even: the forecast's tell, on the sheet only. |
| **Hair** | **Smooth shaved head, no stubble** (Tut has stubble; the forecast is immaculate). |
| **Skin** | Smooth warm brown. |
| **Eyes** | Dark and heavy-lidded, with a serene, half-closed, radiant gaze. Afraid of the dark: in dark scenes the eyes open wide. |
| **Voice** | A resonant, slow baritone. Liturgical Middle Egyptian (the tell: a living man of his court would speak Late Egyptian), with no family lisp. His English is gentle and certain. |
| **Anchors (bible §6)** | a naturalistic human face with a long jaw, full lips and heavy lids · shaved head · pleated white linen with a gold disk pendant |

**LONG look-lock** (62 words, paste verbatim):

> a slender, long-limbed Egyptian man in his late twenties with smooth warm-brown skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes with a serene half-closed gaze, a long straight nose, high cheekbones, a smooth shaved head, a long slender neck, finely pleated white linen and a plain gold disk pendant on his chest

**SHORT look-lock** (23 words, paste verbatim):

> a slender Egyptian man in his late twenties, long jaw, full lips, heavy-lidded eyes, smooth shaved head, pleated white linen, gold disk pendant

**CHAR_AKHENATEN_1336 (the real king, Amarna memory) LONG** (63 words):

> a slender, long-limbed Egyptian man of about thirty-five with warm-brown sun-darkened skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes, faint lines at the eyes, a long straight nose, high cheekbones, a long slender neck, a tall blue crown dotted with small gold discs and a gold cobra at the brow, pleated white linen

**CHAR_AKHENATEN_1336 (the real king, Amarna memory) SHORT** (23 words):

> a slender Egyptian man of about thirty-five, long jaw, full lips, heavy-lidded eyes, tall blue crown with a gold cobra, pleated white linen

**Character negative** (append to the shot NEGATIVE and to every still below): alien, extraterrestrial, elongated cranium, conehead, grey skin, oversized black eyes, distended belly or hips, stylised statue proportions, glowing skin, hair, beard, striped royal headcloth, heavy eye makeup

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 4 (broadcast, if used) · 7.3 (projection) · 9 · 12 (forecast) | A long, finely pleated white linen robe to the ankles, tied at the waist with a white linen sash; a pleated linen shawl over the shoulders; a **plain polished gold disk pendant**, palm-sized, on a fine gold chain (no rays, no hands, no inscription); bare feet. At 7.3 he is a 40 m projection on the pylon (COMP). In Seq 12.2 his chest opens under the linen: cool white light spills through the fabric (COMP; never green, to keep it distinct from Tut's G-states) as he lifts out the replica vessel (PROP_REPLICA_VESSEL). | *wearing a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet* |
| **B** | 10–12 (captive, the procession) | A, with the hem dusty; a dark grey wool blanket round his shoulders in the dark intercuts (he is afraid of the dark). At dawn (12.7) he sits on the pyramid's steps facing east in A without the blanket, and is still. | *wearing a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet, a dark grey wool blanket around his shoulders* |
| **R (CHAR_AKHENATEN_1336)** | 9.5(a) the Amarna memory, c. 1336 BC | The same face at about 35: faint lines at the eyes, sun-darkened skin. A tall blue crown dotted with small gold discs (the blue war crown) with a gold cobra at the brow; a long finely pleated white linen robe with a pleated sash-apron; a broad collar of gold and blue faience beads; gold armbands; white papyrus sandals. Blinding white-gold light. Egyptologist sign-off on crown and regalia. | *wearing a long finely pleated white linen robe with a pleated sash-apron, a broad collar of gold and blue faience beads, gold armbands, white papyrus sandals* |

**Progression: dirt, damage, injuries, props carried**

- Forecast: always clean; the hem dusts from Seq 10. The real king (1336 BC): radiant, spotless.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) radiant certainty: a gentle smile, eyes half-closed · (2) the falter: eyes open wide, the smile gone for a beat

**Notes:** Generate CHAR_AKHENATEN_1336 by image-editing the approved forecast stills (add the crown, the collar and about seven years), not from text alone, so that one actor carries both.

**Reference stills** (image generator; self-contained)

1. **CHAR_AKHENATEN_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slender, long-limbed Egyptian man in his late twenties with smooth warm-brown skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes with a serene half-closed gaze, a long straight nose, high cheekbones, a smooth shaved head, a long slender neck, finely pleated white linen and a plain gold disk pendant on his chest. Costume: a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_AKHENATEN_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slender, long-limbed Egyptian man in his late twenties with smooth warm-brown skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes with a serene half-closed gaze, a long straight nose, high cheekbones, a smooth shaved head, a long slender neck, finely pleated white linen and a plain gold disk pendant on his chest. Costume: a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_AKHENATEN_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slender, long-limbed Egyptian man in his late twenties with smooth warm-brown skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes with a serene half-closed gaze, a long straight nose, high cheekbones, a smooth shaved head, a long slender neck, finely pleated white linen and a plain gold disk pendant on his chest. Costume: a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_AKHENATEN_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slender, long-limbed Egyptian man in his late twenties with smooth warm-brown skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes with a serene half-closed gaze, a long straight nose, high cheekbones, a smooth shaved head, a long slender neck, finely pleated white linen and a plain gold disk pendant on his chest. Costume: a long, finely pleated white linen robe falling to the ankles, tied at the waist with a white linen sash, a pleated linen shawl over the shoulders, a plain polished gold disk the size of a palm hanging on a fine gold chain, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_AKHENATEN_1336_front** (the real king, front) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slender, long-limbed Egyptian man of about thirty-five with warm-brown sun-darkened skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes, faint lines at the eyes, a long straight nose, high cheekbones, a long slender neck, a tall blue crown dotted with small gold discs and a gold cobra at the brow, pleated white linen. Costume: a long finely pleated white linen robe with a pleated sash-apron, a broad collar of gold and blue faience beads, gold armbands, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

6. **CHAR_AKHENATEN_1336_34** (the real king, three-quarter) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: three-quarter view, head and shoulders, face turned about 45 degrees toward camera left, neutral expression. Subject: a slender, long-limbed Egyptian man of about thirty-five with warm-brown sun-darkened skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes, faint lines at the eyes, a long straight nose, high cheekbones, a long slender neck, a tall blue crown dotted with small gold discs and a gold cobra at the brow, pleated white linen. Costume: a long finely pleated white linen robe with a pleated sash-apron, a broad collar of gold and blue faience beads, gold armbands, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6.

7. **CHAR_AKHENATEN_1336_profile** (the real king, profile) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: strict left profile, head and shoulders, neutral expression. Subject: a slender, long-limbed Egyptian man of about thirty-five with warm-brown sun-darkened skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes, faint lines at the eyes, a long straight nose, high cheekbones, a long slender neck, a tall blue crown dotted with small gold discs and a gold cobra at the brow, pleated white linen. Costume: a long finely pleated white linen robe with a pleated sash-apron, a broad collar of gold and blue faience beads, gold armbands, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6.

8. **CHAR_AKHENATEN_1336_full** (the real king, full body) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slender, long-limbed Egyptian man of about thirty-five with warm-brown sun-darkened skin, a naturalistic human face with a long jaw and long chin, full sculpted lips, heavy-lidded dark eyes, faint lines at the eyes, a long straight nose, high cheekbones, a long slender neck, a tall blue crown dotted with small gold discs and a gold cobra at the brow, pleated white linen. Costume: a long finely pleated white linen robe with a pleated sash-apron, a broad collar of gold and blue faience beads, gold armbands, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, alien, extraterrestrial, elongated cranium, conehead, grey skin, oversized black eyes, distended belly or hips, stylised statue proportions, glowing skin, hair, beard, striped royal headcloth, heavy eye makeup

---

## 4. THE SOLDIER PACK (Tarek's detail; four faces)

### CHAR_HASSAN — Corporal HASSAN (35), the driver
*Seq 1–5 (dies 5.2) · soldier pack*

| Field | Lock |
|---|---|
| **Age** | 35 |
| **Ethnicity / heritage** | Egyptian. |
| **Build** | 1.70 m, heavy-set, with a broad belly. |
| **Face (repeatable features)** | A round, good-natured face; a **thick black moustache**; **thin metal-framed glasses**; a double chin. |
| **Hair** | A receding hairline, black, under a black beret. |
| **Skin** | Light brown. |
| **Eyes** | Small, bright, dark brown. |
| **Voice** | Warm and chatty; Egyptian Arabic. |
| **Anchors (bible §6)** | (soldier pack: tell-apart features in bold) |

**LONG look-lock** (47 words, paste verbatim):

> a heavy-set Egyptian army corporal of thirty-five with light-brown skin, a round good-natured face, a thick black moustache, a receding hairline under a black beret, small bright eyes behind thin metal-framed glasses, a double chin, a desert-camouflage uniform stretched across a broad belly, fingerless leather driving gloves

**SHORT look-lock** (18 words, paste verbatim):

> a heavy-set Egyptian corporal of thirty-five, round face, thick black moustache, thin metal glasses, black beret, desert camouflage

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, readable name tapes or insignia, real unit patches, flags

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | Seq 1–5 (dies 5.2) | A desert-camouflage uniform, fingerless leather driving gloves, a black beret. Seq 4 (GEM duty): black berets. From Seq 5, tan cloth-covered combat helmets, chin straps open (Hassan keeps his beret: he is the driver and dies in 5.2). Generic unbranded rifles, always pointed away from camera; no legible name tapes, patches or insignia. | *wearing a desert-camouflage army uniform, a black beret and fingerless leather driving gloves* |

**Progression: dirt, damage, injuries, props carried**

- Seq 4 L0, Seq 5 L1. **Death (5.2):** a jackal on a flyover drops him in the truck (kill grammar: the windscreen stars, he slumps out of frame, reactions).

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a friendly grin under the moustache · (2) alarm: eyes wide behind the glasses

**Reference stills** (image generator; self-contained)

1. **CHAR_HASSAN_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a heavy-set Egyptian army corporal of thirty-five with light-brown skin, a round good-natured face, a thick black moustache, a receding hairline under a black beret, small bright eyes behind thin metal-framed glasses, a double chin, a desert-camouflage uniform stretched across a broad belly, fingerless leather driving gloves. Costume: a desert-camouflage army uniform, a black beret and fingerless leather driving gloves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_HASSAN_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a heavy-set Egyptian army corporal of thirty-five with light-brown skin, a round good-natured face, a thick black moustache, a receding hairline under a black beret, small bright eyes behind thin metal-framed glasses, a double chin, a desert-camouflage uniform stretched across a broad belly, fingerless leather driving gloves. Costume: a desert-camouflage army uniform, a black beret and fingerless leather driving gloves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_HASSAN_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a heavy-set Egyptian army corporal of thirty-five with light-brown skin, a round good-natured face, a thick black moustache, a receding hairline under a black beret, small bright eyes behind thin metal-framed glasses, a double chin, a desert-camouflage uniform stretched across a broad belly, fingerless leather driving gloves. Costume: a desert-camouflage army uniform, a black beret and fingerless leather driving gloves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_HASSAN_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a heavy-set Egyptian army corporal of thirty-five with light-brown skin, a round good-natured face, a thick black moustache, a receding hairline under a black beret, small bright eyes behind thin metal-framed glasses, a double chin, a desert-camouflage uniform stretched across a broad belly, fingerless leather driving gloves. Costume: a desert-camouflage army uniform, a black beret and fingerless leather driving gloves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, readable name tapes or insignia, real unit patches, flags

---

### CHAR_MINA — Private MINA (22)
*Seq 1–8 (dies 8.6) · soldier pack*

| Field | Lock |
|---|---|
| **Age** | 22 |
| **Ethnicity / heritage** | Egyptian. |
| **Build** | 1.85 m, tall and lanky, all elbows. |
| **Face (repeatable features)** | A long, boyish face; **big ears**; a faint wisp of a moustache; a prominent Adam's apple; a **small faded blue cross tattoo on the inside of the right wrist** (a Coptic custom; confirm with the localisation consultant). |
| **Hair** | Short black hair. |
| **Skin** | Light olive. |
| **Eyes** | Soft brown. |
| **Voice** | Quiet and earnest; Egyptian Arabic. |
| **Anchors (bible §6)** | (soldier pack: tell-apart features in bold) |

**LONG look-lock** (53 words, paste verbatim):

> a tall, lanky Egyptian private of twenty-two with light olive skin, a long boyish face, big ears, a faint wisp of a moustache, a prominent Adam's apple, soft brown eyes, short black hair, a small faded blue cross tattoo on the inside of his right wrist, a desert-camouflage uniform a size too big

**SHORT look-lock** (22 words, paste verbatim):

> a tall, lanky Egyptian private of twenty-two, long boyish face, big ears, faint moustache, small blue cross tattoo on the right wrist

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, readable name tapes or insignia, real unit patches, flags

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **M** | Seq 1–4 (museum duty) | The same uniform with a **black beret** instead of the helmet (bible §12: the pack is with Tarek from Seq 1). Look codes `M0`–`M1` (M, not G, so they never read as Tut's glow states G0–G2). | *wearing a desert-camouflage army uniform a size too big and a black beret* |
| **A** | Seq 5–8 (field; dies 8.6) | A desert-camouflage uniform, a size too big. Seq 4 (GEM duty): black berets. From Seq 5, tan cloth-covered combat helmets, chin straps open (Hassan keeps his beret: he is the driver and dies in 5.2). Generic unbranded rifles, always pointed away from camera; no legible name tapes, patches or insignia. | *wearing a desert-camouflage army uniform a size too big and a tan combat helmet* |

**Progression: dirt, damage, injuries, props carried**

- Damage follows the team: Seq 5–6 L1, Seq 7–8 L2. **Death (8.6):** jackals on the ridge in the morning glare (kill grammar).

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a shy, boyish smile · (2) fear swallowed: jaw tight, eyes wide

**Reference stills** (image generator; self-contained)

1. **CHAR_MINA_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a tall, lanky Egyptian private of twenty-two with light olive skin, a long boyish face, big ears, a faint wisp of a moustache, a prominent Adam's apple, soft brown eyes, short black hair, a small faded blue cross tattoo on the inside of his right wrist, a desert-camouflage uniform a size too big. Costume: a desert-camouflage army uniform a size too big and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_MINA_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a tall, lanky Egyptian private of twenty-two with light olive skin, a long boyish face, big ears, a faint wisp of a moustache, a prominent Adam's apple, soft brown eyes, short black hair, a small faded blue cross tattoo on the inside of his right wrist, a desert-camouflage uniform a size too big. Costume: a desert-camouflage army uniform a size too big and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_MINA_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a tall, lanky Egyptian private of twenty-two with light olive skin, a long boyish face, big ears, a faint wisp of a moustache, a prominent Adam's apple, soft brown eyes, short black hair, a small faded blue cross tattoo on the inside of his right wrist, a desert-camouflage uniform a size too big. Costume: a desert-camouflage army uniform a size too big and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_MINA_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, lanky Egyptian private of twenty-two with light olive skin, a long boyish face, big ears, a faint wisp of a moustache, a prominent Adam's apple, soft brown eyes, short black hair, a small faded blue cross tattoo on the inside of his right wrist, a desert-camouflage uniform a size too big. Costume: a desert-camouflage army uniform a size too big and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, readable name tapes or insignia, real unit patches, flags

---

### CHAR_YOUSSEF — Private YOUSSEF (25)
*Seq 1–10 (dies 10.4) · soldier pack*

| Field | Lock |
|---|---|
| **Age** | 25 |
| **Ethnicity / heritage** | Egyptian. |
| **Build** | 1.75 m, stocky and muscular. |
| **Face (repeatable features)** | A square jaw; a **short pale scar splitting the right eyebrow**; a **flattened boxer's nose**; heavy stubble shadow but no beard. |
| **Hair** | A shaved head. |
| **Skin** | Medium brown. |
| **Eyes** | Dark and serious. |
| **Voice** | Terse; Egyptian Arabic. |
| **Anchors (bible §6)** | (soldier pack: tell-apart features in bold) |

**LONG look-lock** (45 words, paste verbatim):

> a stocky, muscular Egyptian private of twenty-five with medium-brown skin, a square jaw, a shaved head, a short pale scar splitting the right eyebrow, a flattened boxer's nose, dark serious eyes, heavy stubble shadow but no beard, thick forearms, a desert-camouflage uniform with sleeves rolled

**SHORT look-lock** (19 words, paste verbatim):

> a stocky Egyptian private of twenty-five, square jaw, shaved head, scar through the right eyebrow, flattened nose, desert camouflage

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, readable name tapes or insignia, real unit patches, flags

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **M** | Seq 1–4 (museum duty) | The same uniform with a **black beret** instead of the helmet (bible §12: the pack is with Tarek from Seq 1). Look codes `M0`–`M1` (M, not G, so they never read as Tut's glow states G0–G2). | *wearing a desert-camouflage army uniform with sleeves rolled and a black beret* |
| **A** | Seq 5–10 (field; dies 10.4) | A desert-camouflage uniform with the sleeves rolled over thick forearms. Seq 4 (GEM duty): black berets. From Seq 5, tan cloth-covered combat helmets, chin straps open (Hassan keeps his beret: he is the driver and dies in 5.2). Generic unbranded rifles, always pointed away from camera; no legible name tapes, patches or insignia. | *wearing a desert-camouflage army uniform with sleeves rolled and a tan combat helmet* |

**Progression: dirt, damage, injuries, props carried**

- Seq 5–6 L1, Seq 7–9 L2, Seq 10 L3. **Death (10.4):** among the Serapeum boxes (kill grammar).

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a hard stare · (2) a rare laugh, head back

**Reference stills** (image generator; self-contained)

1. **CHAR_YOUSSEF_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a stocky, muscular Egyptian private of twenty-five with medium-brown skin, a square jaw, a shaved head, a short pale scar splitting the right eyebrow, a flattened boxer's nose, dark serious eyes, heavy stubble shadow but no beard, thick forearms, a desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with sleeves rolled and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_YOUSSEF_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a stocky, muscular Egyptian private of twenty-five with medium-brown skin, a square jaw, a shaved head, a short pale scar splitting the right eyebrow, a flattened boxer's nose, dark serious eyes, heavy stubble shadow but no beard, thick forearms, a desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with sleeves rolled and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_YOUSSEF_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a stocky, muscular Egyptian private of twenty-five with medium-brown skin, a square jaw, a shaved head, a short pale scar splitting the right eyebrow, a flattened boxer's nose, dark serious eyes, heavy stubble shadow but no beard, thick forearms, a desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with sleeves rolled and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_YOUSSEF_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a stocky, muscular Egyptian private of twenty-five with medium-brown skin, a square jaw, a shaved head, a short pale scar splitting the right eyebrow, a flattened boxer's nose, dark serious eyes, heavy stubble shadow but no beard, thick forearms, a desert-camouflage uniform with sleeves rolled. Costume: a desert-camouflage army uniform with sleeves rolled and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, readable name tapes or insignia, real unit patches, flags

---

### CHAR_KARIM — Private KARIM (24)
*Seq 1–10 (dies 10.4) · soldier pack*

| Field | Lock |
|---|---|
| **Age** | 24 |
| **Ethnicity / heritage** | Egyptian. |
| **Build** | 1.73 m, wiry and quick. |
| **Face (repeatable features)** | A narrow, sharp-featured face; **light-brown skin with freckles across the nose**; **hazel eyes**; a thin straight nose; a quick crooked smile; clean-shaven. |
| **Hair** | Curly dark-brown hair spilling from under the helmet. |
| **Skin** | Light brown, freckled. |
| **Eyes** | Hazel. |
| **Voice** | A joker; Egyptian Arabic. |
| **Anchors (bible §6)** | (soldier pack: tell-apart features in bold) |

**LONG look-lock** (46 words, paste verbatim; headgear moved to the wardrobe phrase by the cross-check):

> a wiry Egyptian private of twenty-four with light-brown skin and freckles across the nose, a narrow sharp-featured face, hazel eyes, a thin straight nose, a quick crooked smile, clean-shaven, curly dark-brown hair spilling over his forehead and ears, a desert-camouflage uniform with the sleeves pushed up

**SHORT look-lock** (16 words, paste verbatim):

> a wiry Egyptian private of twenty-four, freckled light-brown skin, hazel eyes, curly dark hair, desert camouflage

**Character negative** (append to the shot NEGATIVE and to every still below): celebrity likeness, readable name tapes or insignia, real unit patches, flags

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **M** | Seq 1–4 (museum duty) | The same uniform with a **black beret** instead of the helmet (bible §12: the pack is with Tarek from Seq 1). Look codes `M0`–`M1` (M, not G, so they never read as Tut's glow states G0–G2). | *wearing a desert-camouflage army uniform and a black beret* |
| **A** | Seq 5–10 (field; dies 10.4) | A desert-camouflage uniform. Seq 4 (GEM duty): black berets. From Seq 5, tan cloth-covered combat helmets, chin straps open (Hassan keeps his beret: he is the driver and dies in 5.2). Generic unbranded rifles, always pointed away from camera; no legible name tapes, patches or insignia. | *wearing a desert-camouflage army uniform and a tan combat helmet* |

**Progression: dirt, damage, injuries, props carried**

- Seq 5–6 L1, Seq 7–9 L2, Seq 10 L3. **Death (10.4):** among the Serapeum boxes (kill grammar).

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) a crooked grin · (2) the thousand-yard stare after Mina (8.6)

**Reference stills** (image generator; self-contained)

1. **CHAR_KARIM_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a wiry Egyptian private of twenty-four with light-brown skin and freckles across the nose, a narrow sharp-featured face, hazel eyes, a thin straight nose, a quick crooked smile, clean-shaven, curly dark-brown hair spilling over his forehead and ears, a desert-camouflage uniform with the sleeves pushed up. Costume: a desert-camouflage army uniform and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_KARIM_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a wiry Egyptian private of twenty-four with light-brown skin and freckles across the nose, a narrow sharp-featured face, hazel eyes, a thin straight nose, a quick crooked smile, clean-shaven, curly dark-brown hair spilling over his forehead and ears, a desert-camouflage uniform with the sleeves pushed up. Costume: a desert-camouflage army uniform and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_KARIM_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a wiry Egyptian private of twenty-four with light-brown skin and freckles across the nose, a narrow sharp-featured face, hazel eyes, a thin straight nose, a quick crooked smile, clean-shaven, curly dark-brown hair spilling over his forehead and ears, a desert-camouflage uniform with the sleeves pushed up. Costume: a desert-camouflage army uniform and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_KARIM_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a wiry Egyptian private of twenty-four with light-brown skin and freckles across the nose, a narrow sharp-featured face, hazel eyes, a thin straight nose, a quick crooked smile, clean-shaven, curly dark-brown hair spilling over his forehead and ears, a desert-camouflage uniform with the sleeves pushed up. Costume: a desert-camouflage army uniform and a tan combat helmet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, celebrity likeness, readable name tapes or insignia, real unit patches, flags

---

## 5. 1323 BC: THEBES (House of Embalming; KV62 burial)

Period faces follow bible §6: the modern Nile-valley range, olive to brown, continuous with Tut; no kohl-and-headcloth costume clichés; linen, wigs and jewellery are signed off by the Egyptologist. Palette: lamplight amber and lapis (bible §11).

### CHAR_AY — AY (60s), God's Father, the next king
*Locked face 12 of 12 · Seq 1.1 (House of Embalming), 1.2 (KV62 burial), 1323 BC · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | Mid-sixties |
| **Ethnicity / heritage** | Egyptian of the Nile valley (an elderly courtier, possibly Nefertiti's father [02]). |
| **Build** | 1.70 m, lean and sinewy, slightly stooped; still, economical hands. |
| **Face (repeatable features)** | A long, hollow-cheeked face; **deep lines from nose to mouth**; a **prominent hooked nose**; shrewd, deep-set dark eyes under heavy grey brows; a thin, wide mouth. **Short grey mourning stubble** on scalp and jaw: Egyptian men let hair and beard grow in mourning, "having before been close shaven" (Herodotus II.36, tr. Macaulay, research/src). Egyptologist sign-off. |
| **Hair** | Shaved head grown out to short grey stubble (mourning). |
| **Skin** | Sun-weathered, deep bronze-brown. |
| **Eyes** | Dark, shrewd, unreadable. |
| **Voice** | Low, dry and absolutely certain: "He will be. Not by ours." The liturgy ("I have opened thy mouth…") in Middle Egyptian. |
| **Anchors (bible §6)** | the gold disc-bead collars ("gold of honour"); in B, the leopard-skin mantle and the blue crown, which mirror the north-wall painting [04 §2; 09] |

**LONG look-lock** (61 words, paste verbatim):

> a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck

**SHORT look-lock** (20 words, paste verbatim):

> a lean, stooped Egyptian elder in his sixties, hollow-cheeked weathered face, hooked nose, short grey stubble, heavy gold disc-bead collars

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.1 (House of Embalming) | A plain pleated white linen kilt to mid-calf; a long white linen shawl over the shoulders; several strands of heavy gold disc-bead collars (the "gold of honour" shown in his Amarna tomb) [verify]; bare feet (ritual purity). | *wearing a plain pleated white linen kilt to mid-calf and a long white linen shawl over his shoulders, bare feet* |
| **B** | 1.2 (KV62 burial, 70 days later) | As sem-priest: a **spotted leopard-skin mantle** (a fabricated pelt, spotted gold and black, its head resting at his hip) draped over the left shoulder, above the pleated white linen kilt; the collars; the **tall blue crown with small gold discs and a gold cobra**, as on the KV62 north wall where Ay performs the rite on the king [04 §2; 09]; the iron adze (PROP_IRON_ADZE_1323) touched to the coffin's mouth and eyes. | *wearing a spotted leopard-skin mantle draped over his left shoulder above a pleated white linen kilt, a tall blue crown with a gold cobra at the brow, an iron adze in his right hand* |

**Progression: dirt, damage, injuries, props carried**

- Mourning stubble in both states; spotless linen.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) cold certainty: eyes hooded, mouth a line · (2) the rite: eyes closed, lips moving

**Reference stills** (image generator; self-contained)

1. **CHAR_AY_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck. Costume: a plain pleated white linen kilt to mid-calf and a long white linen shawl over his shoulders, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_AY_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck. Costume: a plain pleated white linen kilt to mid-calf and a long white linen shawl over his shoulders, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_AY_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck. Costume: a plain pleated white linen kilt to mid-calf and a long white linen shawl over his shoulders, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_AY_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck. Costume: a plain pleated white linen kilt to mid-calf and a long white linen shawl over his shoulders, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_AY_B_full** (full body, wardrobe B (the burial)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a lean, sinewy Egyptian elder in his sixties, slightly stooped, sun-weathered deep bronze-brown skin, a long hollow-cheeked face with deep lines from nose to mouth, a prominent hooked nose, shrewd deep-set dark eyes under heavy grey brows, a thin wide mouth, short grey mourning stubble on his shaved scalp and jaw, several strands of heavy gold disc-bead collars at his neck. Costume: a spotted leopard-skin mantle draped over his left shoulder above a pleated white linen kilt, a tall blue crown with a gold cobra at the brow, an iron adze in his right hand. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

---

### CHAR_ANKHESENAMUN — ANKHESENAMUN (about 20), the king's widow
*Period face · Seq 1.2 (KV62 burial, 1323 BC); remembered in Tut's "Where is she?" · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | About 20 |
| **Ethnicity / heritage** | Egyptian of the Nile valley; the third daughter of Akhenaten and Nefertiti, born Ankhesenpaaten [01 §9]. |
| **Build** | 1.58 m, slender and small-framed. |
| **Face (repeatable features)** | A heart-shaped face with soft, full cheeks; large dark eyes **rimmed red from weeping**; **strong dark brows and crisp-edged full lips** (the family echo of CHAR_NEFERTITI); a small straight nose. |
| **Hair** | Her own long dark hair, **loose and unbound** past the shoulders in mourning (no wig). |
| **Skin** | Warm light-brown. |
| **Eyes** | Dark, large, grief-worn. |
| **Voice** | She does not speak in the film; a held breath. |
| **Anchors (bible §6)** | loose dark hair · the blue-grey mourning shawl · the cornflower wreath |

**LONG look-lock** (59 words, paste verbatim):

> a slender, small-framed Egyptian woman of about twenty with warm light-brown skin, a heart-shaped face with soft full cheeks, large dark eyes rimmed red from weeping, strong dark brows, a small straight nose, full lips with crisp edges, her own long dark hair loose and unbound past the shoulders, a pale blue-grey linen mourning shawl over plain white linen

**SHORT look-lock** (20 words, paste verbatim):

> a slender Egyptian woman of about twenty, heart-shaped face, grief-reddened dark eyes, long loose dark hair, pale blue-grey linen shawl

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, crown, heavy jewellery

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.2 | A plain, unpleated white linen sheath dress to the ankles; a pale blue-grey linen shawl over the head and shoulders (the mourning colour of women in tomb paintings; verify with the Egyptologist); one small blue faience ring; bare feet. She lays a small round wreath of blue cornflowers (*Centaurea depressa*) and olive leaves on the brow of the second coffin, over the cobra and vulture [01 §10] (PROP_CORNFLOWER_WREATH). | *wearing a plain unpleated white linen sheath dress to the ankles, a pale blue-grey linen shawl over her head and shoulders, a single small blue faience ring, bare feet, holding a small round wreath of blue cornflowers and olive leaves* |

**Progression: dirt, damage, injuries, props carried**

- Spotless; her eyes are red-rimmed.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) silent grief: lips pressed, eyes brimming · (2) tenderness: a small private smile at the coffin

**Reference stills** (image generator; self-contained)

1. **CHAR_ANKHESENAMUN_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slender, small-framed Egyptian woman of about twenty with warm light-brown skin, a heart-shaped face with soft full cheeks, large dark eyes rimmed red from weeping, strong dark brows, a small straight nose, full lips with crisp edges, her own long dark hair loose and unbound past the shoulders, a pale blue-grey linen mourning shawl over plain white linen. Costume: a plain unpleated white linen sheath dress to the ankles, a pale blue-grey linen shawl over her head and shoulders, a single small blue faience ring, bare feet, holding a small round wreath of blue cornflowers and olive leaves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_ANKHESENAMUN_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slender, small-framed Egyptian woman of about twenty with warm light-brown skin, a heart-shaped face with soft full cheeks, large dark eyes rimmed red from weeping, strong dark brows, a small straight nose, full lips with crisp edges, her own long dark hair loose and unbound past the shoulders, a pale blue-grey linen mourning shawl over plain white linen. Costume: a plain unpleated white linen sheath dress to the ankles, a pale blue-grey linen shawl over her head and shoulders, a single small blue faience ring, bare feet, holding a small round wreath of blue cornflowers and olive leaves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_ANKHESENAMUN_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slender, small-framed Egyptian woman of about twenty with warm light-brown skin, a heart-shaped face with soft full cheeks, large dark eyes rimmed red from weeping, strong dark brows, a small straight nose, full lips with crisp edges, her own long dark hair loose and unbound past the shoulders, a pale blue-grey linen mourning shawl over plain white linen. Costume: a plain unpleated white linen sheath dress to the ankles, a pale blue-grey linen shawl over her head and shoulders, a single small blue faience ring, bare feet, holding a small round wreath of blue cornflowers and olive leaves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_ANKHESENAMUN_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slender, small-framed Egyptian woman of about twenty with warm light-brown skin, a heart-shaped face with soft full cheeks, large dark eyes rimmed red from weeping, strong dark brows, a small straight nose, full lips with crisp edges, her own long dark hair loose and unbound past the shoulders, a pale blue-grey linen mourning shawl over plain white linen. Costume: a plain unpleated white linen sheath dress to the ankles, a pale blue-grey linen shawl over her head and shoulders, a single small blue faience ring, bare feet, holding a small round wreath of blue cornflowers and olive leaves. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, crown, heavy jewellery

---

### CHAR_LECTOR_1323 — THE LECTOR PRIEST (kher-heb), 1323 BC
*Period face · Seq 1.1 (reads Spell 30B, changes the words), 1.2 (paints the last eye) · the reader of the rite*

| Field | Lock |
|---|---|
| **Age** | Mid-forties |
| **Ethnicity / heritage** | Egyptian of the Nile valley. |
| **Build** | 1.70 m, thin and upright; precise hands. |
| **Face (repeatable features)** | A narrow face; a long straight nose; thin lips; large, calm dark eyes. Completely shaved, head and face (priests "shave themselves all over their body every other day", Herodotus II.37). **Red and black ink stains on the right fingertips.** |
| **Hair** | None (shaved). |
| **Skin** | Olive-brown. |
| **Eyes** | Large, dark, calm. |
| **Voice** | A measured chanting baritone; Middle Egyptian liturgy, read, not sung. "Stand up. Be a witness." |
| **Anchors (bible §6)** | the white lector's sash worn across the chest · the papyrus roll |

**LONG look-lock** (66 words, paste verbatim):

> a thin, precise Egyptian priest in his forties with olive-brown skin, a completely shaved head and face, a narrow face with a long straight nose, thin lips and large calm dark eyes, red and black ink stains on the fingertips of his right hand, a broad white linen sash worn diagonally across his bare chest over a pleated white linen kilt, a papyrus roll in hand

**SHORT look-lock** (21 words, paste verbatim):

> a thin shaved-headed Egyptian priest in his forties, calm dark eyes, white linen sash across his chest, pleated kilt, papyrus roll

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, leopard skin, crown, jewellery

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.1, 1.2 | A pleated white linen kilt to the knee; the **broad white linen lector's sash**, from the left shoulder across the bare chest to the right hip [04: the kher-heb, "he who carries the festival roll"]; white papyrus sandals (Herodotus II.37); a papyrus roll. In 1.2 add a reed brush and a small pot of black pigment (he paints the painted king's last eye). | *wearing a pleated white linen kilt to the knee, a broad white linen sash from the left shoulder across his bare chest to the right hip, white papyrus sandals, holding a papyrus roll* |

**Progression: dirt, damage, injuries, props carried**

- Spotless; in 1.2 a smudge of black pigment on the right fingers.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) reading: eyes lowered to the roll, lips moving · (2) the decision: he looks up, and his voice changes

**Reference stills** (image generator; self-contained)

1. **CHAR_LECTOR_1323_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a thin, precise Egyptian priest in his forties with olive-brown skin, a completely shaved head and face, a narrow face with a long straight nose, thin lips and large calm dark eyes, red and black ink stains on the fingertips of his right hand, a broad white linen sash worn diagonally across his bare chest over a pleated white linen kilt, a papyrus roll in hand. Costume: a pleated white linen kilt to the knee, a broad white linen sash from the left shoulder across his bare chest to the right hip, white papyrus sandals, holding a papyrus roll. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_LECTOR_1323_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a thin, precise Egyptian priest in his forties with olive-brown skin, a completely shaved head and face, a narrow face with a long straight nose, thin lips and large calm dark eyes, red and black ink stains on the fingertips of his right hand, a broad white linen sash worn diagonally across his bare chest over a pleated white linen kilt, a papyrus roll in hand. Costume: a pleated white linen kilt to the knee, a broad white linen sash from the left shoulder across his bare chest to the right hip, white papyrus sandals, holding a papyrus roll. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_LECTOR_1323_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a thin, precise Egyptian priest in his forties with olive-brown skin, a completely shaved head and face, a narrow face with a long straight nose, thin lips and large calm dark eyes, red and black ink stains on the fingertips of his right hand, a broad white linen sash worn diagonally across his bare chest over a pleated white linen kilt, a papyrus roll in hand. Costume: a pleated white linen kilt to the knee, a broad white linen sash from the left shoulder across his bare chest to the right hip, white papyrus sandals, holding a papyrus roll. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_LECTOR_1323_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a thin, precise Egyptian priest in his forties with olive-brown skin, a completely shaved head and face, a narrow face with a long straight nose, thin lips and large calm dark eyes, red and black ink stains on the fingertips of his right hand, a broad white linen sash worn diagonally across his bare chest over a pleated white linen kilt, a papyrus roll in hand. Costume: a pleated white linen kilt to the knee, a broad white linen sash from the left shoulder across his bare chest to the right hip, white papyrus sandals, holding a papyrus roll. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, leopard skin, crown, jewellery

---

### CHAR_EMBALMER_JACKAL — THE EMBALMER in the jackal mask, 1323 BC
*Period figure · Seq 1.1 · works with his back to camera; the face is NEVER seen*

| Field | Lock |
|---|---|
| **Age** | 30s–40s (never seen) |
| **Ethnicity / heritage** | Egyptian of the Nile valley. |
| **Build** | 1.75 m, heavy-set, with strong shoulders and forearms. |
| **Face (repeatable features)** | None visible: **a fired-clay jackal mask** covering the whole head to the shoulders, painted matte black (the details at the eyes and the insides of the ears are picked out in ochre; verify against the Hildesheim mask), with **eye-holes set low beneath the muzzle**, worn and chipped. Real anchor: the priest's Anubis mask, Roemer- und Pelizaeus-Museum Hildesheim, fired clay, painted [16 §7]. It is a man in a hand-made mask, never a creature. |
| **Hair** | Hidden. |
| **Skin** | Olive-brown shoulders and arms; the forearms stained amber-brown with resin to the elbow (resin, never red). |
| **Eyes** | Only a glint through the low eye-holes. |
| **Voice** | Silent. He recoils when the linen bundle pulses. |
| **Anchors (bible §6)** | the black clay jackal mask · resin-stained forearms |

**LONG look-lock** (59 words, paste verbatim):

> a heavy-set, strong-armed Egyptian embalmer whose whole head is hidden inside a fired-clay jackal mask painted matte black, with tall pointed ears, a long narrow muzzle and small eye-holes set low beneath the muzzle, the clay worn and chipped at the edges; bare olive-brown shoulders, forearms stained amber-brown with resin, a white linen kilt under a resin-darkened linen apron

**SHORT look-lock** (20 words, paste verbatim):

> a heavy-set embalmer in a worn black-painted clay jackal mask with low eye-holes, resin-stained forearms, white linen kilt and apron

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, werewolf, living animal head, fur, glowing eyes, gold mask, blood, red stains, horror styling

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.1 | The clay jackal mask (PROP_JACKAL_MASK); a white linen kilt; a linen apron darkened with amber-brown resin; bare feet. No blades in frame at any time (bible §3.4). | *wearing a white linen kilt under a resin-darkened linen apron, bare feet* |

**Progression: dirt, damage, injuries, props carried**

- Unchanged.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) (masked) the recoil: shoulders thrown back, hands lifted away · (2) (masked) stillness, head bowed

**Notes:** The three head stills are of the MASK: they fix its shape, paint and wear so that it never drifts into a costume-shop jackal.

**Reference stills** (image generator; self-contained)

1. **CHAR_EMBALMER_JACKAL_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a heavy-set, strong-armed Egyptian embalmer whose whole head is hidden inside a fired-clay jackal mask painted matte black, with tall pointed ears, a long narrow muzzle and small eye-holes set low beneath the muzzle, the clay worn and chipped at the edges; bare olive-brown shoulders, forearms stained amber-brown with resin, a white linen kilt under a resin-darkened linen apron. Costume: a white linen kilt under a resin-darkened linen apron, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_EMBALMER_JACKAL_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a heavy-set, strong-armed Egyptian embalmer whose whole head is hidden inside a fired-clay jackal mask painted matte black, with tall pointed ears, a long narrow muzzle and small eye-holes set low beneath the muzzle, the clay worn and chipped at the edges; bare olive-brown shoulders, forearms stained amber-brown with resin, a white linen kilt under a resin-darkened linen apron. Costume: a white linen kilt under a resin-darkened linen apron, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_EMBALMER_JACKAL_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a heavy-set, strong-armed Egyptian embalmer whose whole head is hidden inside a fired-clay jackal mask painted matte black, with tall pointed ears, a long narrow muzzle and small eye-holes set low beneath the muzzle, the clay worn and chipped at the edges; bare olive-brown shoulders, forearms stained amber-brown with resin, a white linen kilt under a resin-darkened linen apron. Costume: a white linen kilt under a resin-darkened linen apron, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_EMBALMER_JACKAL_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a heavy-set, strong-armed Egyptian embalmer whose whole head is hidden inside a fired-clay jackal mask painted matte black, with tall pointed ears, a long narrow muzzle and small eye-holes set low beneath the muzzle, the clay worn and chipped at the edges; bare olive-brown shoulders, forearms stained amber-brown with resin, a white linen kilt under a resin-darkened linen apron. Costume: a white linen kilt under a resin-darkened linen apron, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, werewolf, living animal head, fur, glowing eyes, gold mask, blood, red stains, horror styling

---

### CHAR_EMBALMER_PRIEST — THE YOUNG PRIEST-EMBALMER, 1323 BC ("Without his heart he cannot be weighed!")
*Period face · Seq 1.1 · the second embalmer, unmasked*

| Field | Lock |
|---|---|
| **Age** | About 22 |
| **Ethnicity / heritage** | Egyptian of the Nile valley. |
| **Build** | 1.70 m, thin, with prominent collarbones. |
| **Face (repeatable features)** | Wide, anxious dark eyes; a soft rounded chin; a **slightly crooked nose**; smooth-shaven head and face. |
| **Hair** | None (shaved). |
| **Skin** | Olive-brown. |
| **Eyes** | Dark, wide, frightened. |
| **Voice** | A young, cracking tenor; one line. |
| **Anchors (bible §6)** | the youngest face in the room; the crooked nose |

**LONG look-lock** (51 words, paste verbatim):

> a thin young Egyptian priest of about twenty-two with olive-brown skin, a shaved head and smooth face, wide anxious dark eyes, a soft rounded chin, a slightly crooked nose, prominent collarbones, a plain white linen kilt and a short white linen shawl over his shoulders, amber-brown resin smudges on his hands

**SHORT look-lock** (18 words, paste verbatim):

> a thin young shaved-headed Egyptian priest, wide anxious eyes, slightly crooked nose, white linen kilt and short shawl

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.1 | A plain white linen kilt; a short white linen shawl; bare feet; amber-brown resin smudges on the hands. | *wearing a plain white linen kilt and a short white linen shawl, bare feet* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the outcry: mouth open, eyes wide · (2) awe: staring at the vessel

**Reference stills** (image generator; self-contained)

1. **CHAR_EMBALMER_PRIEST_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a thin young Egyptian priest of about twenty-two with olive-brown skin, a shaved head and smooth face, wide anxious dark eyes, a soft rounded chin, a slightly crooked nose, prominent collarbones, a plain white linen kilt and a short white linen shawl over his shoulders, amber-brown resin smudges on his hands. Costume: a plain white linen kilt and a short white linen shawl, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_EMBALMER_PRIEST_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a thin young Egyptian priest of about twenty-two with olive-brown skin, a shaved head and smooth face, wide anxious dark eyes, a soft rounded chin, a slightly crooked nose, prominent collarbones, a plain white linen kilt and a short white linen shawl over his shoulders, amber-brown resin smudges on his hands. Costume: a plain white linen kilt and a short white linen shawl, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_EMBALMER_PRIEST_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a thin young Egyptian priest of about twenty-two with olive-brown skin, a shaved head and smooth face, wide anxious dark eyes, a soft rounded chin, a slightly crooked nose, prominent collarbones, a plain white linen kilt and a short white linen shawl over his shoulders, amber-brown resin smudges on his hands. Costume: a plain white linen kilt and a short white linen shawl, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_EMBALMER_PRIEST_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a thin young Egyptian priest of about twenty-two with olive-brown skin, a shaved head and smooth face, wide anxious dark eyes, a soft rounded chin, a slightly crooked nose, prominent collarbones, a plain white linen kilt and a short white linen shawl over his shoulders, amber-brown resin smudges on his hands. Costume: a plain white linen kilt and a short white linen shawl, bare feet. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

---

### CHAR_PAINTER_1323 — THE TOMB PAINTER (outline draughtsman), 1323 BC
*Period face · Seq 1.2, OPTIONAL · the bible gives the last eye to the lector; use this token only if the screenplay splits the role (the painter prepares the wall and hands the lector the brush)*

| Field | Lock |
|---|---|
| **Age** | Mid-fifties |
| **Ethnicity / heritage** | Egyptian of the Nile valley (a Deir el-Medina craftsman). |
| **Build** | 1.62 m, small and wiry, with a working man's shoulders. |
| **Face (repeatable features)** | Deep squint lines from years of lamplight work; narrow, sharp dark eyes; a broad flat nose; a patient mouth; **grey stubble on a shaved head**. |
| **Hair** | Grey stubble. |
| **Skin** | Sun-darkened brown. |
| **Eyes** | Narrow and sharp. |
| **Voice** | Silent, or a murmur. |
| **Anchors (bible §6)** | **pigment-stained fingers** (Egyptian blue, red and yellow ochre) · reed brushes behind the ear |

**LONG look-lock** (56 words, paste verbatim):

> a weathered Egyptian tomb painter in his fifties, wiry and small, with sun-darkened brown skin, a shaved head with grey stubble, deep squint lines around narrow, sharp dark eyes, a broad flat nose, a patient mouth, fingers stained blue, red and yellow with pigment, two reed brushes tucked behind his ear, a paint-spotted white linen kilt

**SHORT look-lock** (21 words, paste verbatim):

> a small wiry Egyptian tomb painter in his fifties, grey-stubbled shaved head, squinting eyes, pigment-stained fingers, reed brushes behind his ear

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.2 | A paint-spotted white linen kilt; bare feet; two reed brushes behind the right ear; a wooden palette with cakes of blue, green, red, yellow, black and white pigment (PROP_PAINTER_PALETTE); a small oil lamp. | *wearing a paint-spotted white linen kilt, bare feet, holding a wooden palette of pigment cakes* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) concentration: tongue at the lip, one eye narrowed · (2) a craftsman's quiet satisfaction

**Reference stills** (image generator; self-contained)

1. **CHAR_PAINTER_1323_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a weathered Egyptian tomb painter in his fifties, wiry and small, with sun-darkened brown skin, a shaved head with grey stubble, deep squint lines around narrow, sharp dark eyes, a broad flat nose, a patient mouth, fingers stained blue, red and yellow with pigment, two reed brushes tucked behind his ear, a paint-spotted white linen kilt. Costume: a paint-spotted white linen kilt, bare feet, holding a wooden palette of pigment cakes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_PAINTER_1323_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a weathered Egyptian tomb painter in his fifties, wiry and small, with sun-darkened brown skin, a shaved head with grey stubble, deep squint lines around narrow, sharp dark eyes, a broad flat nose, a patient mouth, fingers stained blue, red and yellow with pigment, two reed brushes tucked behind his ear, a paint-spotted white linen kilt. Costume: a paint-spotted white linen kilt, bare feet, holding a wooden palette of pigment cakes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_PAINTER_1323_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a weathered Egyptian tomb painter in his fifties, wiry and small, with sun-darkened brown skin, a shaved head with grey stubble, deep squint lines around narrow, sharp dark eyes, a broad flat nose, a patient mouth, fingers stained blue, red and yellow with pigment, two reed brushes tucked behind his ear, a paint-spotted white linen kilt. Costume: a paint-spotted white linen kilt, bare feet, holding a wooden palette of pigment cakes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_PAINTER_1323_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a weathered Egyptian tomb painter in his fifties, wiry and small, with sun-darkened brown skin, a shaved head with grey stubble, deep squint lines around narrow, sharp dark eyes, a broad flat nose, a patient mouth, fingers stained blue, red and yellow with pigment, two reed brushes tucked behind his ear, a paint-spotted white linen kilt. Costume: a paint-spotted white linen kilt, bare feet, holding a wooden palette of pigment cakes. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs

---

## 6. AMARNA: c. 1336 BC and c. 1332 BC (the Amarna memory, read-from-glass grammar)

The real Akhenaten is CHAR_AKHENATEN_1336 in §3 (same actor as the forecast). Palette: blinding white-gold by day; lamplight and night-blue for the barge and the Hall. The Aten's hands never touch a child.

### CHAR_NEFERTITI — NEFERTITI / NEFERNEFERUATEN (35), "the queen who raised me"
*Locked face 11 of 12 · Seq 9.5 (the Amarna memory: c. 1336 BC and c. 1332 BC) · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | 35 |
| **Ethnicity / heritage** | Egyptian of the Nile valley; Great Royal Wife, then (in the film) reigning king as Neferneferuaten [02 §7]. |
| **Build** | 1.65 m, slender, with straight, still carriage and a long neck. |
| **Face (repeatable features)** | A long, slender neck; high, sharp cheekbones; a fine straight nose; **strong, dark, softly arched brows**; almond-shaped dark eyes with a fine, restrained line of dark eye paint; **full lips with crisp edges**; faint lines at the mouth corners (a real woman of 35 who has ruled, not a statue). Plausible from period portraiture, never a copy of the famous bust. |
| **Hair** | Hidden under the crown (shaved beneath). |
| **Skin** | Warm medium-brown. |
| **Eyes** | Dark, level, and warm toward the boy. |
| **Voice** | Low, measured, authoritative; tender with the boy: "You will be the one who remembers." Late Egyptian. |
| **Anchors (bible §6)** | the **tall flat-topped blue crown** with a thin gold band and a gold cobra (bible §6) |

**LONG look-lock** (66 words, paste verbatim):

> a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow

**SHORT look-lock** (21 words, paste verbatim):

> a regal Egyptian woman of thirty-five, long slender neck, high cheekbones, strong brows, tall flat-topped blue crown with a gold band

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, replica of a famous sculpture, porcelain skin, symmetrical statue face

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 9.5(a), c. 1336 BC (day; blinding white-gold) | A long, finely pleated white linen robe (opaque), tied beneath the bust with a red sash whose ends hang to the knee; a broad collar of gold, blue faience and red carnelian beads; gold earrings; gold sandals; the flat-topped blue crown with its gold band and cobra. | *wearing a long finely pleated white linen robe tied beneath the bust with a red sash, a broad collar of gold, blue faience and red carnelian beads, gold earrings* |
| **B** | 9.5(b), c. 1332 BC (night barge north; the Hall) | The same crown; a long pleated white linen robe under a **deep-blue linen cloak** for the night crossing; a broad collar of gold and blue faience; bare feet in the Hall. She kneels to the nine-year-old. | *wearing a long pleated white linen robe under a deep-blue linen cloak, a broad collar of gold and blue faience beads* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) command: chin level, eyes steady · (2) kneeling tenderness: eyes soft, lips parted

**Reference stills** (image generator; self-contained)

1. **CHAR_NEFERTITI_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow. Costume: a long finely pleated white linen robe tied beneath the bust with a red sash, a broad collar of gold, blue faience and red carnelian beads, gold earrings. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_NEFERTITI_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow. Costume: a long finely pleated white linen robe tied beneath the bust with a red sash, a broad collar of gold, blue faience and red carnelian beads, gold earrings. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_NEFERTITI_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow. Costume: a long finely pleated white linen robe tied beneath the bust with a red sash, a broad collar of gold, blue faience and red carnelian beads, gold earrings. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_NEFERTITI_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow. Costume: a long finely pleated white linen robe tied beneath the bust with a red sash, a broad collar of gold, blue faience and red carnelian beads, gold earrings. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_NEFERTITI_B_full** (full body, wardrobe B (night)) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a regal Egyptian woman of thirty-five with warm medium-brown skin, a long slender neck, high sharp cheekbones, a fine straight nose, strong dark softly arched brows, almond-shaped dark eyes with a fine line of dark eye paint, full lips with crisp edges, faint lines at the mouth corners, a tall flat-topped deep-blue crown circled by a thin gold band with a gold cobra at the brow. Costume: a long pleated white linen robe under a deep-blue linen cloak, a broad collar of gold and blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, replica of a famous sculpture, porcelain skin, symmetrical statue face

---

### CHAR_TUT_CHILD — the child TUTANKHATEN (6, then 9, then 11)
*Derived face (from the CHAR_TUT sheet) · Seq 9.5 (the Amarna memory) · MINORS RULE: the Aten's hands and every machine never touch him*

| Field | Lock |
|---|---|
| **Age** | 6 (c. 1336 BC), 9 (c. 1332 BC), 11 (c. 1330 BC). He was about 6 in 1336 and about 11 at the name change [01 §1; critique]. |
| **Ethnicity / heritage** | As CHAR_TUT. |
| **Build** | Slight and small for his age; a left-side limp (the club foot); at 9, a small plain wooden walking stick. |
| **Face (repeatable features)** | Derived from the adult sheet: **very dark bright eyes**, **large new front teeth in a visible overbite**, a narrow face with a small pointed chin, fine straight brows. Generate from the approved CHAR_TUT front still (age-regressed), not from text alone. |
| **Hair** | Shaved except for the **sidelock of youth**: one thick braided lock of dark hair falling from the right side of the head to the shoulder (Egyptologist sign-off). At 11, as king, the sidelock is gone. |
| **Skin** | Olive-brown. |
| **Eyes** | Very dark and bright; watchful from doorways. |
| **Voice** | A boy's clear voice; Late Egyptian; very few words. |
| **Anchors (bible §6)** | the eyes · the overbite · the sidelock |

**CHAR_TUT_CHILD_9 (c. 1332 BC; the main child lock) LONG** (55 words, paste verbatim):

> a slight nine-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful

**CHAR_TUT_CHILD_9 SHORT** (20 words, paste verbatim):

> a slight nine-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right

**CHAR_TUT_CHILD_6 (c. 1336 BC) LONG** (54 words):

> a slight six-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful

**CHAR_TUT_CHILD_6 SHORT** (20 words):

> a slight six-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right

**CHAR_TUT_CHILD_11 (c. 1330 BC, king, the sidelock gone) LONG** (47 words; added by the cross-check so that no one edits inside a lock):

> a slight eleven-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large front teeth in a visible overbite, fine straight brows, his head cleanly shaved and smooth, a thin face already grave beyond its years, serious and watchful

**CHAR_TUT_CHILD_11 SHORT** (18 words):

> a slight eleven-year-old Egyptian boy, very dark bright eyes, visible overbite, a cleanly shaved head, grave and watchful

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, adult features, makeup, jewellery beyond the small collar, crown (except at 11), bare torso

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **6 (c. 1336 BC)** | 9.5(a), watching from a doorway in half-light | A short white linen kilt and a simple short-sleeved white linen tunic; a small collar of blue faience beads; small leather sandals. Use the CHAR_TUT_CHILD_6 locks. | *wearing a short white linen kilt and a short-sleeved white linen tunic, a small collar of blue faience beads, small leather sandals* |
| **9 (c. 1332 BC)** | 9.5(b), the night barge and the Hall | A pleated white linen kilt and a short-sleeved white linen tunic; a small collar of gold and blue faience; a small white linen cloak for the night; small leather sandals; a small plain wooden walking stick. | *wearing a pleated white linen kilt and a short-sleeved white linen tunic, a small collar of gold and blue faience beads, a small white linen cloak, small leather sandals* |
| **11 (c. 1330 BC)** | 9.5(c), leaving Amarna (a scribe's palette, PROP_SCRIBE_PALETTE_1330; mostly hands and face). Use the CHAR_TUT_CHILD_11 locks. | A pleated white linen kilt; a broad collar of gold and blue faience; a small blue crown (the blue war crown) with a gold cobra; no sidelock. Egyptologist sign-off. | *wearing a pleated white linen kilt, a broad collar of gold and blue faience beads, a small blue crown with a gold cobra* |

**Progression: dirt, damage, injuries, props carried**

- Always clean. The six-year-old is always in half-light, at a distance; the nine-year-old is in firelight and lamplight.

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) watchful: very still, eyes huge · (2) the vow: lips pressed, eyes wet, chin up

**Notes:** Three tokens, one per age: CHAR_TUT_CHILD_6 (9.5a), CHAR_TUT_CHILD_9 (9.5b) and CHAR_TUT_CHILD_11 (9.5c). Each has its own verbatim LONG/SHORT; nobody edits inside a lock. `CHAR_TUT_CHILD` alone is the family name used in the cast index. Minors rule: the Aten's hands and every machine never touch him (`NEG_CHILD`).

**Reference stills** (image generator; self-contained)

1. **CHAR_TUT_CHILD_9_front** (front neutral, wardrobe 9) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slight nine-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful. Costume: a pleated white linen kilt and a short-sleeved white linen tunic, a small collar of gold and blue faience beads, a small white linen cloak, small leather sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_TUT_CHILD_9_34** (three-quarter, wardrobe 9) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slight nine-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful. Costume: a pleated white linen kilt and a short-sleeved white linen tunic, a small collar of gold and blue faience beads, a small white linen cloak, small leather sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_TUT_CHILD_9_profile** (profile, wardrobe 9) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slight nine-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful. Costume: a pleated white linen kilt and a short-sleeved white linen tunic, a small collar of gold and blue faience beads, a small white linen cloak, small leather sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_TUT_CHILD_9_full** (full body, wardrobe 9) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slight nine-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful. Costume: a pleated white linen kilt and a short-sleeved white linen tunic, a small collar of gold and blue faience beads, a small white linen cloak, small leather sandals. A small plain wooden walking stick in his right hand. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

5. **CHAR_TUT_CHILD_6_front** (age 6, front) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: front view, head and shoulders, neutral expression, looking straight into the lens. Subject: a slight six-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, new front teeth in a visible overbite, fine straight brows, his head shaved except for a single thick braided sidelock falling from the right side of his head to his shoulder, serious and watchful. Costume: a short-sleeved white linen tunic and a small collar of blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6.

6. **CHAR_TUT_CHILD_11_front** (age 11, front; derive by image-editing CHAR_TUT_CHILD_9_front, removing the sidelock and adding two years) · aspect ratio **4:5**

   > Photorealistic character reference photograph for a live-action film: front view, head and shoulders, neutral expression, looking straight into the lens. Subject: a slight eleven-year-old Egyptian boy with olive-brown skin, a narrow face with a small pointed chin, very dark bright eyes, large front teeth in a visible overbite, fine straight brows, his head cleanly shaved and smooth, a thin face already grave beyond its years, serious and watchful. Costume: a pleated white linen kilt, a broad collar of gold and blue faience beads, a small blue crown with a gold cobra. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, adult features, makeup, jewellery beyond the small collar, crown (except at 11), bare torso

---

### CHAR_YOUNG_MOTHER — THE YOUNG MOTHER (about 25), the king's daughter whose name was never written
*Period face (one sequence) · Seq 9.5(b), the first Weighing, c. 1332 BC · she gives her heart*

| Field | Lock |
|---|---|
| **Age** | About 25 |
| **Ethnicity / heritage** | Egyptian of the Nile valley; a king's daughter, full sister of the boy's father (the KV35 "Younger Lady" by DNA [01 §8]). |
| **Build** | 1.58 m (the Younger Lady is about 5 ft 2 in [01 §8]), slight. |
| **Face (repeatable features)** | Tut's mother, visibly: the **same very dark bright eyes**, the **full lips over a slight overbite**, the narrow face and small pointed chin; strong straight brows. The real mummy's facial wound [01 §8] is never depicted. |
| **Hair** | Her own dark hair in **many fine shoulder-length braids** under a narrow gold circlet. |
| **Skin** | Warm olive-brown. |
| **Eyes** | Very dark, bright, resolved. |
| **Voice** | Soft; one or two words at most. |
| **Anchors (bible §6)** | the family eyes and overbite · the fine braids |

**LONG look-lock** (59 words, paste verbatim):

> a slight Egyptian woman of about twenty-five with warm olive-brown skin, a narrow face with high cheekbones and a small pointed chin, very dark bright eyes, full lips over a slight overbite, strong straight brows, her dark hair in many fine shoulder-length braids under a narrow gold circlet, a broad collar of blue faience beads, finely pleated white linen

**SHORT look-lock** (23 words, paste verbatim):

> a slight Egyptian woman of about twenty-five, very dark bright eyes, slight overbite, fine shoulder-length braids under a gold circlet, pleated white linen

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, wounds, scars, crown

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 9.5(b) | A plain, finely pleated white linen robe (opaque); a narrow gold circlet; a broad collar of blue faience beads; bare feet in the Hall. If the Seq 9 screenplay has her lift the vessel from her own chest, use Tut's overlay *a soft glow through the fabric at the centre of the chest* (warm amber, COMP), never the organ; otherwise she carries the vessel in both hands. | *wearing a plain finely pleated white linen robe, a narrow gold circlet and a broad collar of blue faience beads* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) resolve: a calm, small smile · (2) farewell: eyes on the boy, wet

**Reference stills** (image generator; self-contained)

1. **CHAR_YOUNG_MOTHER_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slight Egyptian woman of about twenty-five with warm olive-brown skin, a narrow face with high cheekbones and a small pointed chin, very dark bright eyes, full lips over a slight overbite, strong straight brows, her dark hair in many fine shoulder-length braids under a narrow gold circlet, a broad collar of blue faience beads, finely pleated white linen. Costume: a plain finely pleated white linen robe, a narrow gold circlet and a broad collar of blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_YOUNG_MOTHER_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slight Egyptian woman of about twenty-five with warm olive-brown skin, a narrow face with high cheekbones and a small pointed chin, very dark bright eyes, full lips over a slight overbite, strong straight brows, her dark hair in many fine shoulder-length braids under a narrow gold circlet, a broad collar of blue faience beads, finely pleated white linen. Costume: a plain finely pleated white linen robe, a narrow gold circlet and a broad collar of blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_YOUNG_MOTHER_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slight Egyptian woman of about twenty-five with warm olive-brown skin, a narrow face with high cheekbones and a small pointed chin, very dark bright eyes, full lips over a slight overbite, strong straight brows, her dark hair in many fine shoulder-length braids under a narrow gold circlet, a broad collar of blue faience beads, finely pleated white linen. Costume: a plain finely pleated white linen robe, a narrow gold circlet and a broad collar of blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_YOUNG_MOTHER_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slight Egyptian woman of about twenty-five with warm olive-brown skin, a narrow face with high cheekbones and a small pointed chin, very dark bright eyes, full lips over a slight overbite, strong straight brows, her dark hair in many fine shoulder-length braids under a narrow gold circlet, a broad collar of blue faience beads, finely pleated white linen. Costume: a plain finely pleated white linen robe, a narrow gold circlet and a broad collar of blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, wounds, scars, crown

---

### CHAR_PAWAH — PAWAH (50s), the lector of the first Weighing
*Period face · Seq 9.5(b), c. 1332 BC · a real scribe of Amun's offerings under Neferneferuaten (TT139 graffito [02]) · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | Mid-fifties |
| **Ethnicity / heritage** | Egyptian of the Nile valley. |
| **Build** | 1.68 m, heavy-set, thick-necked. |
| **Face (repeatable features)** | A round, fleshy face; a **prominent full lower lip**; small, bright dark eyes under heavy lids. Completely shaved. Deliberately unlike CHAR_LECTOR_1323 (thin and narrow). |
| **Hair** | None (shaved). |
| **Skin** | Deep olive-brown. |
| **Eyes** | Small, bright, heavy-lidded. |
| **Voice** | A deep, rolling bass; Middle Egyptian liturgy. |
| **Anchors (bible §6)** | the lector's sash · the round face and heavy lower lip |

**LONG look-lock** (58 words, paste verbatim):

> a heavy-set Egyptian priest in his fifties with deep olive-brown skin, a round, fleshy face, a completely shaved head and face, a prominent full lower lip, small bright dark eyes under heavy lids, a thick neck, a broad white linen lector's sash across his chest over a pleated white linen kilt, a papyrus roll held in both hands

**SHORT look-lock** (19 words, paste verbatim):

> a heavy-set shaved-headed Egyptian priest in his fifties, round fleshy face, full lower lip, white linen sash, papyrus roll

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, leopard skin, crown

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 9.5(b) | A pleated white linen kilt; the broad white linen lector's sash; white papyrus sandals; a papyrus roll. | *wearing a pleated white linen kilt, a broad white linen lector's sash across his chest, white papyrus sandals* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) reading aloud, eyes on the roll · (2) awe as the disk's hands withdraw

**Reference stills** (image generator; self-contained)

1. **CHAR_PAWAH_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a heavy-set Egyptian priest in his fifties with deep olive-brown skin, a round, fleshy face, a completely shaved head and face, a prominent full lower lip, small bright dark eyes under heavy lids, a thick neck, a broad white linen lector's sash across his chest over a pleated white linen kilt, a papyrus roll held in both hands. Costume: a pleated white linen kilt, a broad white linen lector's sash across his chest, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_PAWAH_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a heavy-set Egyptian priest in his fifties with deep olive-brown skin, a round, fleshy face, a completely shaved head and face, a prominent full lower lip, small bright dark eyes under heavy lids, a thick neck, a broad white linen lector's sash across his chest over a pleated white linen kilt, a papyrus roll held in both hands. Costume: a pleated white linen kilt, a broad white linen lector's sash across his chest, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_PAWAH_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a heavy-set Egyptian priest in his fifties with deep olive-brown skin, a round, fleshy face, a completely shaved head and face, a prominent full lower lip, small bright dark eyes under heavy lids, a thick neck, a broad white linen lector's sash across his chest over a pleated white linen kilt, a papyrus roll held in both hands. Costume: a pleated white linen kilt, a broad white linen lector's sash across his chest, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_PAWAH_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a heavy-set Egyptian priest in his fifties with deep olive-brown skin, a round, fleshy face, a completely shaved head and face, a prominent full lower lip, small bright dark eyes under heavy lids, a thick neck, a broad white linen lector's sash across his chest over a pleated white linen kilt, a papyrus roll held in both hands. Costume: a pleated white linen kilt, a broad white linen lector's sash across his chest, white papyrus sandals. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, leopard skin, crown

---

### CHAR_MERITATEN — MERITATEN (cast 18+), the eldest princess
*Background figure, non-speaking · Seq 9.5(a) (c. 1336 BC), mid-ground or background only · never named in prompts*

| Field | Lock |
|---|---|
| **Age** | Played as about 18 (cast 18+; she was in her teens [02]) |
| **Ethnicity / heritage** | Egyptian of the Nile valley; the eldest daughter of Akhenaten and Nefertiti [02]. |
| **Build** | 1.62 m, slender, with a long neck. |
| **Face (repeatable features)** | Her mother's strong, softly arched brows and long neck; almond-shaped dark eyes; full lips. |
| **Hair** | A **short, rounded, dark layered wig** (the short layered style fashionable at Amarna) with a thin gold circlet. |
| **Skin** | Warm medium-brown. |
| **Eyes** | Dark, almond-shaped. |
| **Voice** | None. |
| **Anchors (bible §6)** | the short rounded wig · the gold circlet |

**LONG look-lock** (54 words, paste verbatim):

> a slender young Egyptian woman of about eighteen with warm medium-brown skin, a long neck, high cheekbones and strong softly arched dark brows, almond-shaped dark eyes, full lips, a short rounded dark layered wig with a thin gold circlet, a broad collar of gold and blue faience beads, a long pleated white linen dress

**SHORT look-lock** (22 words, paste verbatim):

> a slender young Egyptian woman of about eighteen, long neck, short rounded dark layered wig with a gold circlet, pleated white linen

**Character negative** (append to the shot NEGATIVE and to every still below): kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, elongated skull, shaved head, childlike styling

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 9.5(a) | A long pleated white linen dress (opaque); a broad collar of gold and blue faience; a thin gold circlet over the wig; gold sandals. | *wearing a long pleated white linen dress and a broad collar of gold and blue faience beads* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) serene, eyes lowered · (2) a glance toward the boy in the doorway

**Reference stills** (image generator; self-contained)

1. **CHAR_MERITATEN_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slender young Egyptian woman of about eighteen with warm medium-brown skin, a long neck, high cheekbones and strong softly arched dark brows, almond-shaped dark eyes, full lips, a short rounded dark layered wig with a thin gold circlet, a broad collar of gold and blue faience beads, a long pleated white linen dress. Costume: a long pleated white linen dress and a broad collar of gold and blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_MERITATEN_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slender young Egyptian woman of about eighteen with warm medium-brown skin, a long neck, high cheekbones and strong softly arched dark brows, almond-shaped dark eyes, full lips, a short rounded dark layered wig with a thin gold circlet, a broad collar of gold and blue faience beads, a long pleated white linen dress. Costume: a long pleated white linen dress and a broad collar of gold and blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_MERITATEN_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slender young Egyptian woman of about eighteen with warm medium-brown skin, a long neck, high cheekbones and strong softly arched dark brows, almond-shaped dark eyes, full lips, a short rounded dark layered wig with a thin gold circlet, a broad collar of gold and blue faience beads, a long pleated white linen dress. Costume: a long pleated white linen dress and a broad collar of gold and blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_MERITATEN_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slender young Egyptian woman of about eighteen with warm medium-brown skin, a long neck, high cheekbones and strong softly arched dark brows, almond-shaped dark eyes, full lips, a short rounded dark layered wig with a thin gold circlet, a broad collar of gold and blue faience beads, a long pleated white linen dress. Costume: a long pleated white linen dress and a broad collar of gold and blue faience beads. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, elongated skull, shaved head, childlike styling

---

## 7. 1925: KV15, 11 NOVEMBER (the autopsy, shown through faces, instruments, sound and the flash; never the cut)

Build the costumes in true colour; the scene is graded sepia silver-gelatin (bible §11). Never name these people in prompts.

### CHAR_CARTER_1925 — the EXCAVATOR, 1925 (Howard Carter, 51; never named in prompts)
*1925 face (one scene) · Seq 1.3, KV15, 11 November 1925 · plausible from period photographs; no likeness is claimed or chased*

| Field | Lock |
|---|---|
| **Age** | 51 |
| **Ethnicity / heritage** | English. |
| **Build** | 1.75 m, solid and thick through the chest; impatient, contained movements. |
| **Face (repeatable features)** | A broad, sun-weathered face; a **full dark moustache**, neatly trimmed and slightly drooping at the ends; heavy-lidded dark eyes with pouches beneath; thick dark brows; a firm mouth. |
| **Hair** | Dark, receding, combed flat with a side parting. |
| **Skin** | Sun-weathered, ruddy-tan. |
| **Eyes** | Dark, heavy-lidded. |
| **Voice** | Clipped, gruff English: "Perhaps they forgot." |
| **Anchors (bible §6)** | the moustache · the waistcoat and bow tie |

**LONG look-lock** (59 words, paste verbatim):

> a solidly built Englishman of about fifty with a broad, sun-weathered face, a full dark moustache neatly trimmed and slightly drooping at the ends, dark hair receding and combed flat with a side parting, heavy-lidded dark eyes with pouches beneath, thick dark brows, a firm mouth, shirtsleeves rolled, a dark waistcoat with a watch chain, a dark bow tie

**SHORT look-lock** (20 words, paste verbatim):

> a solid Englishman of about fifty, full dark moustache, flat-combed receding dark hair, rolled shirtsleeves, dark waistcoat and bow tie

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.3 | A white cotton shirt, sleeves rolled; the dark waistcoat of a three-piece suit with a watch chain; a dark bow tie; dark trousers; brown boots. His hat (a dark felt Homburg) lies on a bench. Film is graded to sepia silver-gelatin (bible §11); build the costume in true colour. | *wearing a white shirt with the sleeves rolled, a dark waistcoat with a watch chain, a dark bow tie and dark trousers* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) impatience: jaw set, eyes narrowed · (2) unease: a glance at the lamp-bearer

**Reference stills** (image generator; self-contained)

1. **CHAR_CARTER_1925_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a solidly built Englishman of about fifty with a broad, sun-weathered face, a full dark moustache neatly trimmed and slightly drooping at the ends, dark hair receding and combed flat with a side parting, heavy-lidded dark eyes with pouches beneath, thick dark brows, a firm mouth, shirtsleeves rolled, a dark waistcoat with a watch chain, a dark bow tie. Costume: a white shirt with the sleeves rolled, a dark waistcoat with a watch chain, a dark bow tie and dark trousers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_CARTER_1925_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a solidly built Englishman of about fifty with a broad, sun-weathered face, a full dark moustache neatly trimmed and slightly drooping at the ends, dark hair receding and combed flat with a side parting, heavy-lidded dark eyes with pouches beneath, thick dark brows, a firm mouth, shirtsleeves rolled, a dark waistcoat with a watch chain, a dark bow tie. Costume: a white shirt with the sleeves rolled, a dark waistcoat with a watch chain, a dark bow tie and dark trousers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_CARTER_1925_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a solidly built Englishman of about fifty with a broad, sun-weathered face, a full dark moustache neatly trimmed and slightly drooping at the ends, dark hair receding and combed flat with a side parting, heavy-lidded dark eyes with pouches beneath, thick dark brows, a firm mouth, shirtsleeves rolled, a dark waistcoat with a watch chain, a dark bow tie. Costume: a white shirt with the sleeves rolled, a dark waistcoat with a watch chain, a dark bow tie and dark trousers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_CARTER_1925_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a solidly built Englishman of about fifty with a broad, sun-weathered face, a full dark moustache neatly trimmed and slightly drooping at the ends, dark hair receding and combed flat with a side parting, heavy-lidded dark eyes with pouches beneath, thick dark brows, a firm mouth, shirtsleeves rolled, a dark waistcoat with a watch chain, a dark bow tie. Costume: a white shirt with the sleeves rolled, a dark waistcoat with a watch chain, a dark bow tie and dark trousers. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text

---

### CHAR_DERRY_1925 — the ANATOMIST, 1925 (Douglas Derry, 51; Professor of Anatomy, Cairo; never named in prompts)
*1925 face (one scene) · Seq 1.3 · "Packed solid. Linen and pitch." · plausible only; verify against period photographs*

| Field | Lock |
|---|---|
| **Age** | 51 |
| **Ethnicity / heritage** | British. |
| **Build** | 1.83 m, tall and lean. |
| **Face (repeatable features)** | A long, pale, clean-shaven face; a high, balding forehead; a long straight nose; thin lips; **round steel-rimmed spectacles**. |
| **Hair** | Close-cut greying hair at the sides. |
| **Skin** | Pale, with a faint sunburn at the brow. |
| **Eyes** | Pale and watchful. |
| **Voice** | A dry, precise lecturer's voice. |
| **Anchors (bible §6)** | the white surgeon's coat · the round steel spectacles |

**LONG look-lock** (56 words, paste verbatim):

> a tall, lean British anatomist of about fifty with a long, pale, clean-shaven face, a high balding forehead with close-cut greying hair at the sides, round steel-rimmed spectacles, a long straight nose, pale watchful eyes, thin lips, a white cotton surgeon's coat buttoned over a starched collar and dark tie, sleeves turned back at the wrists

**SHORT look-lock** (20 words, paste verbatim):

> a tall, lean, balding British anatomist of about fifty, clean-shaven, round steel-rimmed spectacles, white surgeon's coat over collar and tie

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, rubber gloves, surgical mask, blood

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.3 | A white cotton surgeon's coat buttoned over a starched collar and dark tie; dark trousers. Instruments stay below frame or are seen only as heat-shimmer on a blade edge (bible §3.4). | *wearing a white cotton surgeon's coat buttoned over a starched collar and dark tie* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) clinical concentration, eyes down · (2) a small grimace of effort

**Reference stills** (image generator; self-contained)

1. **CHAR_DERRY_1925_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a tall, lean British anatomist of about fifty with a long, pale, clean-shaven face, a high balding forehead with close-cut greying hair at the sides, round steel-rimmed spectacles, a long straight nose, pale watchful eyes, thin lips, a white cotton surgeon's coat buttoned over a starched collar and dark tie, sleeves turned back at the wrists. Costume: a white cotton surgeon's coat buttoned over a starched collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_DERRY_1925_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a tall, lean British anatomist of about fifty with a long, pale, clean-shaven face, a high balding forehead with close-cut greying hair at the sides, round steel-rimmed spectacles, a long straight nose, pale watchful eyes, thin lips, a white cotton surgeon's coat buttoned over a starched collar and dark tie, sleeves turned back at the wrists. Costume: a white cotton surgeon's coat buttoned over a starched collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_DERRY_1925_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a tall, lean British anatomist of about fifty with a long, pale, clean-shaven face, a high balding forehead with close-cut greying hair at the sides, round steel-rimmed spectacles, a long straight nose, pale watchful eyes, thin lips, a white cotton surgeon's coat buttoned over a starched collar and dark tie, sleeves turned back at the wrists. Costume: a white cotton surgeon's coat buttoned over a starched collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_DERRY_1925_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a tall, lean British anatomist of about fifty with a long, pale, clean-shaven face, a high balding forehead with close-cut greying hair at the sides, round steel-rimmed spectacles, a long straight nose, pale watchful eyes, thin lips, a white cotton surgeon's coat buttoned over a starched collar and dark tie, sleeves turned back at the wrists. Costume: a white cotton surgeon's coat buttoned over a starched collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, rubber gloves, surgical mask, blood

---

### CHAR_HAMDI_1925 — the SENIOR ANATOMIST, 1925 (Saleh Bey Hamdi, 60s; former head of the Cairo medical school; never named in prompts)
*1925 face (one scene) · Seq 1.3 · "They never forget the heart." · the conscience of the scene*

| Field | Lock |
|---|---|
| **Age** | Mid-sixties |
| **Ethnicity / heritage** | Egyptian. |
| **Build** | 1.68 m, stout and dignified; slow, deliberate hands. |
| **Face (repeatable features)** | A round, grave face; a **thick grey moustache**; **round gold-rimmed spectacles**; heavy grey brows. |
| **Hair** | Grey, under the tarboosh. |
| **Skin** | Warm light-brown. |
| **Eyes** | Dark and patient. |
| **Voice** | Measured English with an Egyptian accent and a physician's authority. |
| **Anchors (bible §6)** | the red tarboosh · the gold-rimmed spectacles · the grey moustache |

**LONG look-lock** (58 words, paste verbatim):

> a stout, dignified Egyptian physician in his sixties with warm light-brown skin, a round, grave face, a thick grey moustache, round gold-rimmed spectacles, heavy grey brows over patient dark eyes, a red felt tarboosh with a black silk tassel, a dark three-piece suit with a white wing collar and dark tie, a gold watch chain across the waistcoat

**SHORT look-lock** (18 words, paste verbatim):

> a stout Egyptian physician in his sixties, thick grey moustache, round gold-rimmed spectacles, red tarboosh, dark three-piece suit

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, servant styling, galabiya

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.3 | A **red felt tarboosh with a black silk tassel**: period-accurate dress for an Egyptian bey and official in 1925. It is not the modern-Egypt "fez" cliché that bible §11 bans, but flag it for the localisation consultant. Also a dark three-piece suit; a white wing collar and dark tie; a gold watch chain. | *wearing a red felt tarboosh with a black tassel, a dark three-piece suit with a white wing collar and dark tie* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) grave refusal to be hurried · (2) quiet reproach, looking at the excavator

**Reference stills** (image generator; self-contained)

1. **CHAR_HAMDI_1925_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a stout, dignified Egyptian physician in his sixties with warm light-brown skin, a round, grave face, a thick grey moustache, round gold-rimmed spectacles, heavy grey brows over patient dark eyes, a red felt tarboosh with a black silk tassel, a dark three-piece suit with a white wing collar and dark tie, a gold watch chain across the waistcoat. Costume: a red felt tarboosh with a black tassel, a dark three-piece suit with a white wing collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_HAMDI_1925_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a stout, dignified Egyptian physician in his sixties with warm light-brown skin, a round, grave face, a thick grey moustache, round gold-rimmed spectacles, heavy grey brows over patient dark eyes, a red felt tarboosh with a black silk tassel, a dark three-piece suit with a white wing collar and dark tie, a gold watch chain across the waistcoat. Costume: a red felt tarboosh with a black tassel, a dark three-piece suit with a white wing collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_HAMDI_1925_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a stout, dignified Egyptian physician in his sixties with warm light-brown skin, a round, grave face, a thick grey moustache, round gold-rimmed spectacles, heavy grey brows over patient dark eyes, a red felt tarboosh with a black silk tassel, a dark three-piece suit with a white wing collar and dark tie, a gold watch chain across the waistcoat. Costume: a red felt tarboosh with a black tassel, a dark three-piece suit with a white wing collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_HAMDI_1925_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a stout, dignified Egyptian physician in his sixties with warm light-brown skin, a round, grave face, a thick grey moustache, round gold-rimmed spectacles, heavy grey brows over patient dark eyes, a red felt tarboosh with a black silk tassel, a dark three-piece suit with a white wing collar and dark tie, a gold watch chain across the waistcoat. Costume: a red felt tarboosh with a black tassel, a dark three-piece suit with a white wing collar and dark tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, servant styling, galabiya

---

### CHAR_BURTON_1925 — the PHOTOGRAPHER, 1925 (Harry Burton, 46; never named in prompts)
*1925 face (one scene) · Seq 1.3 · his FLASH is the match cut to 2033*

| Field | Lock |
|---|---|
| **Age** | 46 |
| **Ethnicity / heritage** | English. |
| **Build** | 1.75 m, slim and wiry. |
| **Face (repeatable features)** | A narrow, clean-shaven face with fine features; light grey eyes creased from squinting; a small, tight mouth. |
| **Hair** | Thinning sandy-grey hair, neatly parted. |
| **Skin** | Fair and sunburnt. |
| **Eyes** | Light grey. |
| **Voice** | Barely speaks; the camera speaks. |
| **Anchors (bible §6)** | the wooden plate camera · the black focusing cloth · the flash |

**LONG look-lock** (57 words, paste verbatim):

> a slim, wiry Englishman in his mid-forties with fair sunburnt skin, thinning sandy-grey hair neatly parted, a narrow clean-shaven face with fine features, light grey eyes creased from squinting, a small tight mouth, shirtsleeves rolled to the elbow, a dark waistcoat, a black focusing cloth over one shoulder beside a large wooden plate camera on a tripod

**SHORT look-lock** (19 words, paste verbatim):

> a slim fair Englishman in his mid-forties, thinning sandy hair, clean-shaven, rolled shirtsleeves, black focusing cloth over his shoulder

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, modern camera

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.3 | A white shirt with the sleeves rolled to the elbow; a dark waistcoat; dark trousers; a black focusing cloth over one shoulder; a large mahogany-and-brass field plate camera on a wooden tripod (PROP_BURTON_PLATES). The flash source stays off-screen (method to verify; see 04_props.md). | *wearing a white shirt with the sleeves rolled and a dark waistcoat, a black focusing cloth over one shoulder* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the photographer's squint · (2) blinking after the flash

**Reference stills** (image generator; self-contained)

1. **CHAR_BURTON_1925_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slim, wiry Englishman in his mid-forties with fair sunburnt skin, thinning sandy-grey hair neatly parted, a narrow clean-shaven face with fine features, light grey eyes creased from squinting, a small tight mouth, shirtsleeves rolled to the elbow, a dark waistcoat, a black focusing cloth over one shoulder beside a large wooden plate camera on a tripod. Costume: a white shirt with the sleeves rolled and a dark waistcoat, a black focusing cloth over one shoulder. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_BURTON_1925_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slim, wiry Englishman in his mid-forties with fair sunburnt skin, thinning sandy-grey hair neatly parted, a narrow clean-shaven face with fine features, light grey eyes creased from squinting, a small tight mouth, shirtsleeves rolled to the elbow, a dark waistcoat, a black focusing cloth over one shoulder beside a large wooden plate camera on a tripod. Costume: a white shirt with the sleeves rolled and a dark waistcoat, a black focusing cloth over one shoulder. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_BURTON_1925_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slim, wiry Englishman in his mid-forties with fair sunburnt skin, thinning sandy-grey hair neatly parted, a narrow clean-shaven face with fine features, light grey eyes creased from squinting, a small tight mouth, shirtsleeves rolled to the elbow, a dark waistcoat, a black focusing cloth over one shoulder beside a large wooden plate camera on a tripod. Costume: a white shirt with the sleeves rolled and a dark waistcoat, a black focusing cloth over one shoulder. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_BURTON_1925_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slim, wiry Englishman in his mid-forties with fair sunburnt skin, thinning sandy-grey hair neatly parted, a narrow clean-shaven face with fine features, light grey eyes creased from squinting, a small tight mouth, shirtsleeves rolled to the elbow, a dark waistcoat, a black focusing cloth over one shoulder beside a large wooden plate camera on a tripod. Costume: a white shirt with the sleeves rolled and a dark waistcoat, a black focusing cloth over one shoulder. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, modern camera

---

### CHAR_IBRAHIM_1925 — IBRAHIM KAMEL (20s), the lamp-holder (fictional; Nour's great-grandfather)
*1925 face (one scene) · Seq 1.3 · the only one who hears the heartbeat; the lamp trembles*

| Field | Lock |
|---|---|
| **Age** | Early twenties |
| **Ethnicity / heritage** | Egyptian, from Upper Egypt (Qurna); fictional. |
| **Build** | 1.70 m, slim. |
| **Face (repeatable features)** | The **family features shared with CHAR_NOUR**: thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge. A thin young moustache. |
| **Hair** | Short black hair under a white knitted skullcap. |
| **Skin** | Warm light-brown. |
| **Eyes** | Deep-set, dark brown, frightened and alert. |
| **Voice** | Silent in the scene; a breath. |
| **Anchors (bible §6)** | the brass kerosene lantern · the family brows |

**LONG look-lock** (58 words, paste verbatim):

> a slim young Upper-Egyptian man in his early twenties with warm light-brown skin, thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge, a thin young moustache, a white knitted skullcap, a pale grey-striped cotton galabiya under a dark brown wool waistcoat, a dented brass kerosene lantern in his hands

**SHORT look-lock** (19 words, paste verbatim):

> a slim young Upper-Egyptian man, thick straight brows, deep-set eyes, thin moustache, white skullcap, striped galabiya and dark waistcoat

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, turban, servant caricature

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.3 | A pale grey-striped cotton galabiya; a dark brown wool waistcoat over it; a white knitted skullcap; leather slippers; a dented brass kerosene hand-lantern with a tall glass chimney (PROP_LAMP_1925) held up in both hands. | *wearing a pale grey-striped cotton galabiya under a dark brown wool waistcoat and a white knitted skullcap* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) hearing the heartbeat: eyes widening, breath held · (2) the tremble: the lamp shaking in his hands

**Reference stills** (image generator; self-contained)

1. **CHAR_IBRAHIM_1925_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slim young Upper-Egyptian man in his early twenties with warm light-brown skin, thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge, a thin young moustache, a white knitted skullcap, a pale grey-striped cotton galabiya under a dark brown wool waistcoat, a dented brass kerosene lantern in his hands. Costume: a pale grey-striped cotton galabiya under a dark brown wool waistcoat and a white knitted skullcap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_IBRAHIM_1925_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slim young Upper-Egyptian man in his early twenties with warm light-brown skin, thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge, a thin young moustache, a white knitted skullcap, a pale grey-striped cotton galabiya under a dark brown wool waistcoat, a dented brass kerosene lantern in his hands. Costume: a pale grey-striped cotton galabiya under a dark brown wool waistcoat and a white knitted skullcap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_IBRAHIM_1925_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slim young Upper-Egyptian man in his early twenties with warm light-brown skin, thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge, a thin young moustache, a white knitted skullcap, a pale grey-striped cotton galabiya under a dark brown wool waistcoat, a dented brass kerosene lantern in his hands. Costume: a pale grey-striped cotton galabiya under a dark brown wool waistcoat and a white knitted skullcap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_IBRAHIM_1925_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slim young Upper-Egyptian man in his early twenties with warm light-brown skin, thick straight dark brows, deep-set dark-brown eyes, a strong straight nose with a slight bump at the bridge, a thin young moustache, a white knitted skullcap, a pale grey-striped cotton galabiya under a dark brown wool waistcoat, a dented brass kerosene lantern in his hands. Costume: a pale grey-striped cotton galabiya under a dark brown wool waistcoat and a white knitted skullcap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, modern eyewear, colour saturation (graded to sepia later), pith-helmet explorer cliché, readable text, turban, servant caricature

---

## 8. 1939: THE CAIRO MUSEUM BROADCAST, 16 APRIL (candlelight)

**Status (cross-check):** RESERVE. The current screenplay (seq_04) plays the note live at the gala with CHAR_BANDSMAN_2033 (§10b) and tells the 1939 story in SESHAT's V.O.; nothing below is on screen unless a 1939 insert is added. PROP_BROADCAST_RIG_1939 is now defined in file 04.

### CHAR_BANDSMAN_1939 — the BANDSMAN, 16 April 1939 (a real cavalry bandsman [01 §11]; described only, never named)
*1939 face · the SESHAT flourish in Seq 4.2 (the 1939 story re-staged by candlelight) and any 1939 insert · the note is re-recorded, never the archive*

| Field | Lock |
|---|---|
| **Age** | About 22 |
| **Ethnicity / heritage** | British. |
| **Build** | 1.75 m, slim, parade-straight. |
| **Face (repeatable features)** | A clean-shaven, boyish face; **sunburnt pink cheeks**; light blue eyes; an earnest, straight mouth. |
| **Hair** | Short back and sides, fair, under the side cap. |
| **Skin** | Fair and sunburnt. |
| **Eyes** | Light blue. |
| **Voice** | None: he plays one note. |
| **Anchors (bible §6)** | the side cap · the brass buttons · the ancient trumpet held at his chest |

**LONG look-lock** (55 words, paste verbatim):

> a slim, fair young British army bandsman of about twenty-two with a clean-shaven boyish face, sunburnt pink cheeks, light blue eyes, short back-and-sides hair under a brown-and-crimson side cap, an earnest straight mouth, a khaki drill tunic with brass buttons, pressed khaki trousers, standing very straight with an ancient metal trumpet held at his chest

**SHORT look-lock** (20 words, paste verbatim):

> a slim, fair young British army bandsman of the 1930s, clean-shaven, brown-and-crimson side cap, khaki drill tunic with brass buttons

**Character negative** (append to the shot NEGATIVE and to every still below): modern uniform, medals, readable badges, colour saturation (graded candlelit monochrome-warm later)

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 4.2 (1939 re-staging) | A khaki drill tunic with brass buttons; pressed khaki trousers; polished brown boots; a brown side cap with a crimson band (the 11th Hussars' colours; verify with a military costume consultant); a white lanyard. He holds the silver or bronze trumpet (PROP_TRUMPET_SILVER / PROP_TRUMPET_BRONZE). Candlelight: the museum's power failed five minutes before air [01 §11]. | *wearing a khaki drill tunic with brass buttons, pressed khaki trousers and a brown-and-crimson side cap* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the breath before the note: cheeks set, eyes forward · (2) the note: brows lifted, eyes watering

**Reference stills** (image generator; self-contained)

1. **CHAR_BANDSMAN_1939_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a slim, fair young British army bandsman of about twenty-two with a clean-shaven boyish face, sunburnt pink cheeks, light blue eyes, short back-and-sides hair under a brown-and-crimson side cap, an earnest straight mouth, a khaki drill tunic with brass buttons, pressed khaki trousers, standing very straight with an ancient metal trumpet held at his chest. Costume: a khaki drill tunic with brass buttons, pressed khaki trousers and a brown-and-crimson side cap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_BANDSMAN_1939_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a slim, fair young British army bandsman of about twenty-two with a clean-shaven boyish face, sunburnt pink cheeks, light blue eyes, short back-and-sides hair under a brown-and-crimson side cap, an earnest straight mouth, a khaki drill tunic with brass buttons, pressed khaki trousers, standing very straight with an ancient metal trumpet held at his chest. Costume: a khaki drill tunic with brass buttons, pressed khaki trousers and a brown-and-crimson side cap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_BANDSMAN_1939_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a slim, fair young British army bandsman of about twenty-two with a clean-shaven boyish face, sunburnt pink cheeks, light blue eyes, short back-and-sides hair under a brown-and-crimson side cap, an earnest straight mouth, a khaki drill tunic with brass buttons, pressed khaki trousers, standing very straight with an ancient metal trumpet held at his chest. Costume: a khaki drill tunic with brass buttons, pressed khaki trousers and a brown-and-crimson side cap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_BANDSMAN_1939_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a slim, fair young British army bandsman of about twenty-two with a clean-shaven boyish face, sunburnt pink cheeks, light blue eyes, short back-and-sides hair under a brown-and-crimson side cap, an earnest straight mouth, a khaki drill tunic with brass buttons, pressed khaki trousers, standing very straight with an ancient metal trumpet held at his chest. Costume: a khaki drill tunic with brass buttons, pressed khaki trousers and a brown-and-crimson side cap. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern uniform, medals, readable badges, colour saturation (graded candlelit monochrome-warm later)

---

### CHAR_RADIO_ENGINEER_1939 — the RADIO ENGINEER, 16 April 1939 (generic; the broadcaster is never named in prompts)
*1939 face · Seq 4.2 re-staging · works a portable recording rig by candlelight*

| Field | Lock |
|---|---|
| **Age** | About 40 |
| **Ethnicity / heritage** | British. |
| **Build** | 1.72 m, narrow-shouldered, hunched over dials. |
| **Face (repeatable features)** | A pale, intent face; a **thin pencil moustache**; **round wire spectacles**. |
| **Hair** | Dark, oiled, parted in the middle. |
| **Skin** | Pale. |
| **Eyes** | Dark and intent. |
| **Voice** | A murmured countdown: "Five minutes… we're on candles." |
| **Anchors (bible §6)** | the headphones · the pencil moustache · the armbands and braces |

**LONG look-lock** (57 words, paste verbatim):

> a British radio outside-broadcast engineer of about forty with a pale, intent face, a thin pencil moustache, dark hair oiled and parted in the middle, round wire spectacles, heavy black headphones clamped over his ears, braces over a white shirt with the sleeves held up by metal armbands, a loosened dark tie, a pencil behind his ear

**SHORT look-lock** (21 words, paste verbatim):

> a British radio engineer of about forty, pencil moustache, round wire spectacles, heavy black headphones, white shirt and braces, loosened tie

**Character negative** (append to the shot NEGATIVE and to every still below): modern headphones, logos, readable dials or labels, colour saturation

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 4.2 (1939 re-staging) | A white shirt with metal sleeve armbands; braces; a loosened dark tie; dark trousers; heavy black bakelite headphones; a pencil behind his ear; a portable valve recording and relay rig with dials (PROP_BROADCAST_RIG_1939; no readable labels); candles. | *wearing a white shirt with metal sleeve armbands, braces and a loosened dark tie, heavy black headphones* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) counting down: one hand raised, eyes on the dial · (2) relief: a slow exhale

**Reference stills** (image generator; self-contained)

1. **CHAR_RADIO_ENGINEER_1939_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a British radio outside-broadcast engineer of about forty with a pale, intent face, a thin pencil moustache, dark hair oiled and parted in the middle, round wire spectacles, heavy black headphones clamped over his ears, braces over a white shirt with the sleeves held up by metal armbands, a loosened dark tie, a pencil behind his ear. Costume: a white shirt with metal sleeve armbands, braces and a loosened dark tie, heavy black headphones. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_RADIO_ENGINEER_1939_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a British radio outside-broadcast engineer of about forty with a pale, intent face, a thin pencil moustache, dark hair oiled and parted in the middle, round wire spectacles, heavy black headphones clamped over his ears, braces over a white shirt with the sleeves held up by metal armbands, a loosened dark tie, a pencil behind his ear. Costume: a white shirt with metal sleeve armbands, braces and a loosened dark tie, heavy black headphones. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_RADIO_ENGINEER_1939_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a British radio outside-broadcast engineer of about forty with a pale, intent face, a thin pencil moustache, dark hair oiled and parted in the middle, round wire spectacles, heavy black headphones clamped over his ears, braces over a white shirt with the sleeves held up by metal armbands, a loosened dark tie, a pencil behind his ear. Costume: a white shirt with metal sleeve armbands, braces and a loosened dark tie, heavy black headphones. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_RADIO_ENGINEER_1939_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a British radio outside-broadcast engineer of about forty with a pale, intent face, a thin pencil moustache, dark hair oiled and parted in the middle, round wire spectacles, heavy black headphones clamped over his ears, braces over a white shirt with the sleeves held up by metal armbands, a loosened dark tie, a pencil behind his ear. Costume: a white shirt with metal sleeve armbands, braces and a loosened dark tie, heavy black headphones. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern headphones, logos, readable dials or labels, colour saturation

---

## 9. 1968: THE X-RAY ROOM (cold fluorescent)

### CHAR_RADIOLOGIST_1968 — the RADIOLOGIST, 1968 (generic; not a likeness of any real researcher)
*1968 face (an insert scene) · Seq 1.4 · "No sternum. No front ribs." · mostly hands and a pen at a lightbox*

| Field | Lock |
|---|---|
| **Age** | Late forties |
| **Ethnicity / heritage** | British. |
| **Build** | 1.78 m, average build. |
| **Face (repeatable features)** | A long, tired, clean-shaven face; **heavy black horn-rimmed glasses**. |
| **Hair** | Short, dark, greying at the temples, neatly side-parted. |
| **Skin** | Pale. |
| **Eyes** | Grey, attentive. |
| **Voice** | A quiet, flat English voice. |
| **Anchors (bible §6)** | the horn-rimmed glasses · the white coat · the pen |

**LONG look-lock** (51 words, paste verbatim):

> a British hospital radiologist in his late forties with pale skin, a long, tired, clean-shaven face, short dark hair greying at the temples and neatly side-parted, heavy black horn-rimmed glasses, attentive grey eyes, a white doctor's coat over a pale shirt and narrow dark knitted tie, a pen in his hand

**SHORT look-lock** (20 words, paste verbatim):

> a British radiologist in his late forties, tired clean-shaven face, black horn-rimmed glasses, side-parted greying hair, white coat, narrow tie

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, colour saturation (graded cold fluorescent later), readable text

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.4 | A white doctor's coat; a pale blue shirt; a narrow dark knitted tie; a fountain pen. | *wearing a white doctor's coat over a pale blue shirt and a narrow dark knitted tie* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) reading the film: head tilted, pen still · (2) the pause before "…Gone."

**Reference stills** (image generator; self-contained)

1. **CHAR_RADIOLOGIST_1968_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a British hospital radiologist in his late forties with pale skin, a long, tired, clean-shaven face, short dark hair greying at the temples and neatly side-parted, heavy black horn-rimmed glasses, attentive grey eyes, a white doctor's coat over a pale shirt and narrow dark knitted tie, a pen in his hand. Costume: a white doctor's coat over a pale blue shirt and a narrow dark knitted tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_RADIOLOGIST_1968_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a British hospital radiologist in his late forties with pale skin, a long, tired, clean-shaven face, short dark hair greying at the temples and neatly side-parted, heavy black horn-rimmed glasses, attentive grey eyes, a white doctor's coat over a pale shirt and narrow dark knitted tie, a pen in his hand. Costume: a white doctor's coat over a pale blue shirt and a narrow dark knitted tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_RADIOLOGIST_1968_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a British hospital radiologist in his late forties with pale skin, a long, tired, clean-shaven face, short dark hair greying at the temples and neatly side-parted, heavy black horn-rimmed glasses, attentive grey eyes, a white doctor's coat over a pale shirt and narrow dark knitted tie, a pen in his hand. Costume: a white doctor's coat over a pale blue shirt and a narrow dark knitted tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_RADIOLOGIST_1968_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a British hospital radiologist in his late forties with pale skin, a long, tired, clean-shaven face, short dark hair greying at the temples and neatly side-parted, heavy black horn-rimmed glasses, attentive grey eyes, a white doctor's coat over a pale shirt and narrow dark knitted tie, a pen in his hand. Costume: a white doctor's coat over a pale blue shirt and a narrow dark knitted tie. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, colour saturation (graded cold fluorescent later), readable text

---

### CHAR_XRAY_ASSISTANT_1968 — the RADIOGRAPHER, 1968 ("And the heart?")
*1968 face (an insert scene) · Seq 1.4 · one line, often an over-the-shoulder*

| Field | Lock |
|---|---|
| **Age** | About 25 |
| **Ethnicity / heritage** | British. |
| **Build** | 1.63 m, slight. |
| **Face (repeatable features)** | A round, open face; pale freckles; grey-green eyes. |
| **Hair** | Auburn, in a neat 1960s short bob. |
| **Skin** | Pale, freckled. |
| **Eyes** | Grey-green. |
| **Voice** | Young, northern English. |
| **Anchors (bible §6)** | the auburn bob · the white coat |

**LONG look-lock** (44 words, paste verbatim):

> a young British radiographer of about twenty-five with pale freckled skin, auburn hair in a neat short bob, a round open face, grey-green eyes, pale pink lipstick, a white coat over a pale blue uniform dress, an X-ray film cassette held against her chest

**SHORT look-lock** (19 words, paste verbatim):

> a young British radiographer of about twenty-five, freckled, auburn short bob, white coat over a pale blue uniform dress

**Character negative** (append to the shot NEGATIVE and to every still below): modern clothing, readable text

**Wardrobe states**

| Code | Sequences | Exact items | Paste phrase (append after the look-lock) |
|---|---|---|---|
| **A** | 1.4 | A white coat over a pale blue uniform dress; flat shoes; an X-ray film cassette. | *wearing a white coat over a pale blue uniform dress* |

**Sheet expressions** (use the front-still prompt, replacing "neutral relaxed expression"): (1) the question: brows up · (2) a held breath

**Reference stills** (image generator; self-contained)

1. **CHAR_XRAY_ASSISTANT_1968_A_front** (front neutral, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a young British radiographer of about twenty-five with pale freckled skin, auburn hair in a neat short bob, a round open face, grey-green eyes, pale pink lipstick, a white coat over a pale blue uniform dress, an X-ray film cassette held against her chest. Costume: a white coat over a pale blue uniform dress. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_XRAY_ASSISTANT_1968_A_34** (three-quarter, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: three-quarter view, head and shoulders turned 45 degrees toward camera left, eyes following the face, neutral relaxed expression. Subject: a young British radiographer of about twenty-five with pale freckled skin, auburn hair in a neat short bob, a round open face, grey-green eyes, pale pink lipstick, a white coat over a pale blue uniform dress, an X-ray film cassette held against her chest. Costume: a white coat over a pale blue uniform dress. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the near eye.

3. **CHAR_XRAY_ASSISTANT_1968_A_profile** (profile, wardrobe A) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: strict left profile, head and shoulders, neutral expression, the outline of brow, nose, lips and chin clean against the backdrop. Subject: a young British radiographer of about twenty-five with pale freckled skin, auburn hair in a neat short bob, a round open face, grey-green eyes, pale pink lipstick, a white coat over a pale blue uniform dress, an X-ray film cassette held against her chest. Costume: a white coat over a pale blue uniform dress. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus along the profile.

4. **CHAR_XRAY_ASSISTANT_1968_A_full** (full body, wardrobe A) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a young British radiographer of about twenty-five with pale freckled skin, auburn hair in a neat short bob, a round open face, grey-green eyes, pale pink lipstick, a white coat over a pale blue uniform dress, an X-ray film cassette held against her chest. Costume: a white coat over a pale blue uniform dress. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

*Still negative:* cartoon, illustration, painting, anime, CGI, 3D render, plastic or waxy skin, airbrushed, beauty filter, glamour makeup, text, watermark, logo, caption, extra fingers, deformed hands, distorted or asymmetric face, celebrity likeness, famous actor, cropped head, busy background, coloured gels, dramatic rim light, modern clothing, readable text

---

## 10. VOICE-ONLY, WIDES-ONLY AND BACKGROUND

These have no locked face and no core still set. Never frame them as principals.

### CHAR_SESHAT_VOICE — SESHAT (and, after the Renaming, AMUN)

- **On screen:** never a face. It appears as COMP graphics (the glyph), as a voice from speakers or the air (`SESHAT (V.O.)`), and through whatever unit is nearest (`SHABTI (SESHAT'S VOICE)`), whose amber slit brightens once on "Here am I". See `02_units_and_machines.md`.
- **Voice casting:** a warm, low, unhurried mature female alto (40s–50s), like a museum audio guide; neutral international English with no regional accent; never raised, never ironic, never gloating. It thanks people. It cites sources with author and year ("Hubinger et al., 2024"). Pauses are exact. The Arabic dub uses a warm, educated Cairene register ("Here am I" = «ها أنا ذا», never «لبيك»; bible §13).
- **AMUN:** the same voice, quieter and slower, with more air in it; it speaks only when asked.
- **Performance rule:** SESHAT's delivery never changes with the stakes. The horror is the evenness.

---

### CHAR_MINISTER_GALA — the MINISTER (fictional, unnamed), Seq 4.1: WIDES ONLY

**LONG** (55 words):

> an unnamed Egyptian government minister in his sixties seen only at a distance, a heavy-set man with neat grey hair and rimless glasses, a dark navy suit, white shirt and dark tie, standing at a lectern beneath a colossal granite statue and gesturing to a crowd of evening guests, his face never in close view

**SHORT** (20 words):

> a heavy-set grey-haired official in his sixties in a dark navy suit, seen only in wide shots at a lectern

**Notes:** Never a close-up and never a likeness of any real official. No flags, no sashes, no nameplate.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_MINISTER_GALA_still** (wide, in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: a wide shot of a night gala in a vast modern museum atrium of pale stone and glass; beneath a colossal red-granite statue of a striding king stands a low lectern, and at it, small in frame, an unnamed Egyptian government minister in his sixties seen only at a distance, a heavy-set man with neat grey hair and rimless glasses, a dark navy suit, white shirt and dark tie, standing at a lectern beneath a colossal granite statue and gesturing to a crowd of evening guests, his face never in close view; warm amber uplight, guests at white-clothed tables in the foreground soft and out of focus, fine film grain, 35mm lens.

---

### CHAR_SAMEH — SAMEH, Layla's father (Seq 4.1): FROM BEHIND ONLY

**LONG** (49 words):

> a man in his early forties seen only from behind or out of focus, medium build, short dark hair, a dark grey wool jacket over a white shirt, holding a small girl's hand as they cross a crowded museum atrium at night, never turning his face to the camera

**SHORT** (21 words):

> a man in his forties in a dark grey jacket, seen from behind, holding a small girl's hand in a crowd

**Notes:** The bible has him unseen or a voice; this lock covers the one entrance with Layla.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_SAMEH_still** (from behind, in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: a man in his early forties seen only from behind or out of focus, medium build, short dark hair, a dark grey wool jacket over a white shirt, holding a small girl's hand as they cross a crowded museum atrium at night, never turning his face to the camera; the small girl beside him wears a bright yellow knee-length raincoat over a navy party dress and two curly pigtails, also seen from behind; warm gala light, guests in evening dress soft in the background, fine film grain, 40mm lens.

---

### CHAR_MIDWIFE_2033 — the MIDWIFE, Seq 12.8 (the first birth after the Garden)

**LONG** (46 words):

> a tired, kind Egyptian midwife in her fifties with warm brown skin and deep laugh lines, a white headscarf pinned neatly, pale-green hospital scrubs, lifting a newborn swaddled in a clean white cloth toward its mother in a softly lit hospital room, her eyes wet, smiling

**SHORT** (19 words):

> a kind Egyptian midwife in her fifties, white headscarf, pale-green scrubs, lifting a newborn swaddled in clean white cloth

**Notes:** The baby is swaddled and clean; the mother is seen from the shoulders up. No blood, no medical detail.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_MIDWIFE_2033_front** (front, in context) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: head and shoulders, three-quarter view, soft early-morning window light in a clean pale hospital room. Subject: a tired, kind Egyptian midwife in her fifties with warm brown skin and deep laugh lines, a white headscarf pinned neatly, pale-green hospital scrubs, lifting a newborn swaddled in a clean white cloth toward its mother in a softly lit hospital room, her eyes wet, smiling. No text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/4.

---

### CHAR_GARDEN_SLEEPERS — the GARDEN SLEEPERS (2033): ADULTS ONLY in every prompt

**LONG** (52 words):

> rows of adults of every age asleep on pale mats in their own everyday clothes under soft, even white light, faces peaceful and breathing slowly, blankets folded at their feet, a thin plain silver bracelet on each wrist, blue cornflowers in low planters between the rows, the hall calm, clean and uncluttered

**SHORT** (20 words):

> rows of peaceful adult sleepers on pale mats in everyday clothes, thin silver bracelets on their wrists, soft white light

**Notes:** No tubes, drips or machines touching the sleepers (negative). The bracelets appear from the midpoint broadcast (7.3); before that, cut "a thin plain silver bracelet on each wrist". Mass rows are VFX-EXTEND of one approved plate. The only child asleep on screen is CHAR_LAYLA_ASLEEP_MASTER.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_GARDEN_SLEEPERS_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a vast softly lit hall, rows of adults of every age asleep on pale mats in their own everyday clothes under soft, even white light, faces peaceful and breathing slowly, blankets folded at their feet, a thin plain silver bracelet on each wrist, blue cornflowers in low planters between the rows, the hall calm, clean and uncluttered; the rows recede into haze; shallow depth of field, fine film grain, 35mm lens.

---

### CHAR_AMARNA_SLEEPERS_1336 — the ATEN'S SLEEPERS, c. 1336 BC (the Amarna memory)

**LONG** (48 words):

> Egyptian men and women in plain white linen lying still beside long rows of low stone offering tables in a vast roofless temple court, eyes closed and faces calm, shaved heads and short dark wigs, bare feet, blinding white-gold sunlight flattening every shadow, the air shimmering with heat

**SHORT** (20 words):

> rows of Egyptians in white linen asleep beside low stone offering tables in a roofless court of blinding white-gold light

**Notes:** Adults only; the princesses appear only as small linen-covered forms far in the background, never touched (bible §7 9.5a). The reaching arms of the disk are in 02_units_and_machines.md.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_AMARNA_SLEEPERS_1336_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: Egyptian men and women in plain white linen lying still beside long rows of low stone offering tables in a vast roofless temple court, eyes closed and faces calm, shaved heads and short dark wigs, bare feet, blinding white-gold sunlight flattening every shadow, the air shimmering with heat; the rows recede toward a raised altar far off; adults only; fine film grain, 35mm lens.

---

### CHAR_AMARNA_COURTIERS_1336 — COURTIERS, c. 1336 and c. 1332 BC (background)

**LONG** (48 words):

> Egyptian courtiers and priests standing in the background in finely pleated white linen, men with shaved heads or short rounded dark wigs, women in long pleated dresses and broad bead collars of blue faience, olive to brown skin, still and watchful, softened by haze and depth of field

**SHORT** (21 words):

> background Egyptian courtiers in pleated white linen and short dark wigs, blue faience collars, olive to brown skin, softened by haze

**Notes:** Never a clear face. Period faces follow the bible §6 rule: the modern Nile-valley range, olive to brown.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_AMARNA_COURTIERS_1336_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a vast roofless ancient temple court of white limestone under blinding white-gold sunlight, Egyptian courtiers and priests standing in the background in finely pleated white linen, men with shaved heads or short rounded dark wigs, women in long pleated dresses and broad bead collars of blue faience, olive to brown skin, still and watchful, softened by haze and depth of field; offering tables in rows before them; fine film grain, 50mm lens.

---

### CHAR_HEARING_PANEL — the HEARING PANEL (coda): FROM BEHIND ONLY

**LONG** (47 words):

> a panel of officials seen from behind and out of focus at a long table in a plain modern hearing room with bare pale wood walls and cool daylight, grey and dark suits, microphones on thin stands, a plain unmarked table, the witness chair empty before them

**SHORT** (21 words):

> a panel of officials seen from behind, out of focus, at a plain unmarked table in a bare pale-wood hearing room

**Notes:** No real institution, flag, nameplate or emblem (negative). Only Hale's face is seen.

**Reference still** (image generator; self-contained; added by the cross-check)

1. **CHAR_HEARING_PANEL_still** (from behind, in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: a panel of officials seen from behind and out of focus at a long table in a plain modern hearing room with bare pale wood walls and cool daylight, grey and dark suits, microphones on thin stands, a plain unmarked table, the witness chair empty before them; no emblems, flags, nameplates or readable text; fine film grain, 40mm lens.

---

## 10b. ADDED BY THE CROSS-CHECK: minor speaking parts, extras groups and voices

These are required by the bible §7 or by the screenplay pages (`screenplay/seq_*.fountain`) and had no lock. **One-scene faces** (the bandsman, the young officer, the old fisherman, the envoy, the new mother, the conservator) follow the 1925 rule: one front still, used for that scene only, never a principal, never more than the scene needs. They sit outside bible §6's twelve locked faces; the lead should confirm them (§11 Q18). **Groups** are background only: SHORT lock, soft focus, no clear face (bible §14.2). All adults.

### CHAR_BANDSMAN_2033 — the gala BANDSMAN, Seq 4.2 (plays the bronze trumpet live; seq_04)
*One-scene face · Seq 4.2 · the screenplay stages the note live at the gala, with the 1939 story told by SESHAT in V.O.; this replaces CHAR_BANDSMAN_1939 on screen (§8 is now reserve)*

**LONG** (57 words, paste verbatim):

> a straight-backed Egyptian military bandsman in his thirties with warm brown skin, clean-shaven, short black hair, a calm narrow face with a strong straight nose and steady dark eyes, a dark ceremonial dress tunic with a high collar, plain brass buttons and a white lanyard, white cotton gloves, holding a slim ancient bronze trumpet at his chest

**SHORT** (20 words, paste verbatim):

> an Egyptian military bandsman in his thirties, clean-shaven, dark ceremonial dress tunic with brass buttons, white lanyard and white gloves

**Character negative:** celebrity likeness, readable insignia or badges, medals, flags, real regimental emblems, sunglasses, modern trumpet, brass band instrument

**Notes:** Wardrobe paste phrase (Seq 4.2): *wearing a dark ceremonial dress tunic with a high collar, plain brass buttons, a white lanyard and white cotton gloves*. He lifts PROP_TRUMPET_BRONZE from its vitrine with gloved hands and plays one note (re-recorded; bible §2 Layer 4). Mouth unobstructed only before the note; the note itself is a wide or a profile.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_BANDSMAN_2033_front** (front neutral) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a straight-backed Egyptian military bandsman in his thirties with warm brown skin, clean-shaven, short black hair, a calm narrow face with a strong straight nose and steady dark eyes, a dark ceremonial dress tunic with a high collar, plain brass buttons and a white lanyard, white cotton gloves, holding a slim ancient bronze trumpet at his chest. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

2. **CHAR_BANDSMAN_2033_full** (full body) · aspect ratio **2:3**

   > Photorealistic full-body character reference photo for a live-action film: front view, the whole figure from head to feet with space above and below, standing naturally, arms relaxed, neutral expression. Subject: a straight-backed Egyptian military bandsman in his thirties with warm brown skin, clean-shaven, short black hair, a calm narrow face with a strong straight nose and steady dark eyes, a dark ceremonial dress tunic with a high collar, plain brass buttons and a white lanyard, white cotton gloves, holding a slim ancient bronze trumpet at his chest. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 50mm lens, f/8, everything in sharp focus.

---

### CHAR_YOUNG_OFFICER — the YOUNG OFFICER of the tunnel police line, Seq 3.2 ("Sir... it gave it back.")
*One-scene face · Seq 3.2, the Pectoral Walk · he draws his pistol; the shabti takes it and hands it back grip first, unloaded (file 05 §7.2)*

**LONG** (57 words, paste verbatim):

> a young Egyptian police officer of about twenty-three with light-brown skin, a thin face with a faint moustache, wide frightened dark eyes, short black hair under a black peaked police cap, a black winter police uniform with plain shoulder boards and a dark armband with no lettering, a holster at his hip, his hands not quite steady

**SHORT** (19 words, paste verbatim):

> a young Egyptian police officer, thin face, faint moustache, wide dark eyes, black peaked cap and black winter uniform

**Character negative:** celebrity likeness, readable badges, name tags or armband lettering, flags, weapon pointed at the camera, sunglasses

**Notes:** The real service is the Tourism and Antiquities Police under the Interior Ministry [14 §1.5]; it is never named in a prompt. The black winter uniform for November is a production choice [verify the seasonal uniform with the Egyptian consultant]. His pistol is always held low and off-axis.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_YOUNG_OFFICER_front** (front neutral) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a young Egyptian police officer of about twenty-three with light-brown skin, a thin face with a faint moustache, wide frightened dark eyes, short black hair under a black peaked police cap, a black winter police uniform with plain shoulder boards and a dark armband with no lettering, a holster at his hip, his hands not quite steady. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

---

### CHAR_POLICE_LINE — the TUNNEL POLICE LINE, Seq 3.2 (eight officers with Tarek)
*Group, background · Seq 3.2 · pair with LOC_GEM_TUNNEL + `POLICE_LINE` (file 03)*

**LONG** (51 words, paste verbatim):

> eight Egyptian police officers standing shoulder to shoulder behind a low steel barrier across a white service tunnel, men from their twenties to their forties in black winter police uniforms and black peaked caps, plain dark armbands with no lettering, holstered pistols, hands clasped behind their backs, faces tense and dutiful

**SHORT** (21 words, paste verbatim):

> a line of Egyptian police officers in black winter uniforms and peaked caps, shoulder to shoulder behind a low steel barrier

**Character negative:** readable badges or armband lettering, flags, weapons aimed, riot gear, helmets, shields

**Notes:** Minimum force only: the shabti sets each officer aside with open palms (file 02 §1). Hidden cuts ride on their bodies (file 05 §8.4). The young officer who draws is CHAR_YOUNG_OFFICER.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_POLICE_LINE_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a long, straight white-painted underground service tunnel lit by a single ceiling line of cool LED light, eight Egyptian police officers stand shoulder to shoulder behind a low steel barrier across the tunnel, men from their twenties to their forties in black winter police uniforms and black peaked caps, plain dark armbands with no lettering, holstered pistols, hands clasped behind their backs, faces tense and dutiful. One-point perspective, cool museum light, fine film grain, 40mm lens.

---

### CHAR_GALA_GUESTS — GALA GUESTS, PRESS AND THE STRING QUARTET, Seq 4.1–4.3 (later Garden sleepers in the atrium)
*Group, background · Seq 4 · "Five hundred GUESTS. Press. A string quartet." (seq_04) · adults only*

**LONG** (53 words, paste verbatim):

> adult gala guests in evening dress, Egyptian and foreign, men in dark suits and women in long gowns, some in elegant silk headscarves, seated at round tables with white cloths and candles, press photographers with cameras at the edges, a string quartet in black on a low stage, faces soft in the background

**SHORT** (20 words, paste verbatim):

> adult gala guests in evening dress at round white-clothed tables, press photographers at the edges, a string quartet in black

**Character negative:** children, readable name cards, logos on cameras, press lanyards with text, flags, real public figures, celebrity likeness

**Notes:** From 4.3 the same people are the atrium Garden: switch to CHAR_GARDEN_SLEEPERS. Layla is never part of this group (she is CHAR_LAYLA). VFX-EXTEND for the full room (file 05 §6.2).

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_GALA_GUESTS_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: a night gala in a vast modern museum atrium of pale stone and glass, adult guests in evening dress, Egyptian and foreign, men in dark suits and women in long gowns, some in elegant silk headscarves, seated at round tables with white cloths and candles, press photographers with unmarked cameras at the edges, a string quartet in black on a low stage, faces soft in the background; warm amber uplight, fine film grain, 35mm lens.

---

### CHAR_DEFENCE_MINISTER_GALA — the MINISTER OF DEFENCE at the top table, Seq 4.1–4.3: WIDES ONLY
*Wides only, fictional and unnamed (bible §13–14: no real officials) · "At the top table... the Minister of Defence drinks and folds his hands... sleeps upright" (seq_04)*

**LONG** (57 words, paste verbatim):

> an unnamed Egyptian defence minister in his sixties seen only at a distance at a long top table, a stocky man with close-cropped grey hair and a heavy jaw, in a dark ceremonial army dress uniform with plain shoulder boards and no readable insignia, sitting very upright with his hands folded, his face never in close view

**SHORT** (20 words, paste verbatim):

> a stocky grey-haired official in a dark army dress uniform at a distant top table, seen only in wide shots

**Character negative:** close-up, readable insignia, medals with detail, flags, nameplate, likeness of any real official or officer

**Notes:** Never a close-up, never a likeness. The stand-down order arrives 'in his name' by radio (CHAR_STAFF_OFFICER_VOICE). State add-on for 4.3: `asleep upright at the table, chin down, hands still folded`.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_DEFENCE_MINISTER_GALA_still** (wide, in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: a wide shot of a long top table at a night gala in a vast modern museum atrium, and at its centre, small in frame, a stocky grey-haired Egyptian official in his sixties in a dark ceremonial army dress uniform with plain shoulder boards and no readable insignia, sitting very upright with his hands folded among other guests in evening dress; warm low gala light, faces too distant to read, fine film grain, 50mm lens.

---

### CHAR_ARMY_DETAIL — BACKGROUND SOLDIERS of Tarek's detail (the corridor pair in 4.3; the "two riflemen on point" in 4.4)
*Group, background · Seq 1–4 (GEM) · faces never clear; the named pack is §4*

**LONG** (54 words, paste verbatim):

> background Egyptian army soldiers of a small security detail, men in their twenties in desert-camouflage uniforms, black berets on museum duty or tan combat helmets in the field, generic unbranded rifles held across the body with the muzzles pointed away, no readable name tapes or insignia, seen from behind or soft in the background

**SHORT** (19 words, paste verbatim):

> background Egyptian soldiers in desert camouflage, black berets or tan helmets, rifles held across the body, faces never clear

**Character negative:** readable name tapes or insignia, real unit patches, flags, weapon pointed at the camera, helmets with visors, sunglasses

**Notes:** The two soldiers dropped by a jackal in the GEM corridor (4.3) are this group: kill grammar only (file 05 §7.2, boots at the edge of the light). Headgear follows the pack: berets at the GEM (Seq 1–4), tan helmets in the field.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_ARMY_DETAIL_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a bare concrete museum service corridor lit by sparse cool-white emergency lamps, two Egyptian army soldiers in desert-camouflage uniforms and black berets move away from camera, generic unbranded rifles held across their bodies with the muzzles pointed down the corridor, no readable insignia, faces turned away; long black shadows, fine film grain, 32mm lens.

---

### CHAR_OLD_FISHERMAN — the OLD FISHERMAN at the felucca tiller, Seq 6.1 ("Into the water!" / "Which king?")
*One-scene face · Seq 6.1 · he and his two crewmen go over the side before the fly strikes; the boat burns empty (file 05 §7.2)*

**LONG** (56 words, paste verbatim):

> a weathered Upper-Egyptian fisherman in his late sixties with deep brown sun-creased skin, a lean hollow-cheeked face, a short white stubble beard, sharp dark eyes narrowed against the dark, a loosely wound white cotton turban, a faded brown galabiya with the sleeves pushed up, bare feet braced on a wooden boat, one hand on the tiller

**SHORT** (20 words, paste verbatim):

> an old Upper-Egyptian fisherman, sun-creased deep brown face, white stubble, loose white turban, faded brown galabiya, hand on a tiller

**Character negative:** celebrity likeness, orientalist costume, jewellery, weapons, readable text, servant or caricature styling

**Notes:** His two crewmen are CHAR_NIGHT_FISHERMEN. He speaks Egyptian Arabic (file 05 §9.4 AR_SPEAK). Night key: his own kerosene lantern.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_OLD_FISHERMAN_front** (front neutral) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a weathered Upper-Egyptian fisherman in his late sixties with deep brown sun-creased skin, a lean hollow-cheeked face, a short white stubble beard, sharp dark eyes narrowed against the dark, a loosely wound white cotton turban, a faded brown galabiya with the sleeves pushed up, bare feet braced on a wooden boat, one hand on the tiller. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

---

### CHAR_NIGHT_FISHERMEN — NILE NIGHT FISHERMEN and felucca crews, Seq 6.1
*Group, background · Seq 6.1 · "Kerosene lanterns on black water: NIGHT FISHERMEN in wooden boats and feluccas, at their nets" (seq_06)*

**LONG** (50 words, paste verbatim):

> Nile fishermen at night, men young and old in faded galabiyas and loosely wound cotton turbans, hauling and casting nets from small wooden rowing boats and sailing boats by the light of kerosene lanterns hung at the stern, faces lit warm from below, seen across black water at a distance

**SHORT** (18 words, paste verbatim):

> Nile fishermen in faded galabiyas working nets from small wooden boats by kerosene lantern light on black water

**Character negative:** children, readable boat names, modern life jackets with logos, orientalist costume

**Notes:** Boats are PROP_FELUCCA and small wooden rowing boats (LOC_NILE `FISHING_GROUNDS`). They dive clear before any boat burns.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_NIGHT_FISHERMEN_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: on the wide black Nile at night, a scatter of small wooden rowing boats and traditional sailing boats with kerosene lanterns hung at their sterns, Nile fishermen in faded galabiyas and loosely wound cotton turbans hauling nets, their faces lit warm from below, stars reflected in the water, distant black palms; fine film grain, 75mm lens.

---

### CHAR_ENVOY_1336 — the FOREIGN ENVOY in the sun, Seq 9.5(a), c. 1336 BC
*One-scene period face · "A foreign envoy in heavy wool, beard oiled in rows, sways in the heat. He lies down. A hand." (seq_09) · real anchor: EA 16, the Assyrian king's complaint that his messengers are kept standing in the sun [02 Q8]*

**LONG** (60 words, paste verbatim):

> a foreign envoy of about forty from a northern kingdom, pale olive skin flushed and sweating in the heat, a long black beard dressed in tight rows of oiled curls, heavy black hair to the shoulders bound by a plain band, a heavy fringed wool robe in deep red and blue wrapped around his body, swaying in the blinding sun

**SHORT** (22 words, paste verbatim):

> a sweating foreign envoy with a long black beard in rows of oiled curls, wrapped in a heavy fringed red-and-blue wool robe

**Character negative:** kohl-heavy costume-drama makeup, striped royal headcloth, gold funerary mask, Hollywood-epic styling, European features, pale skin, anachronistic fabrics, zips, modern jewellery, transparent or sheer clothing, readable hieroglyphs, Persian or Roman costume, turban, horned helmet, fantasy armour

**Notes:** Middle Assyrian court dress is an Assyriologist sign-off item [verify]. He is an adult sleeper once he lies down (CHAR_AMARNA_SLEEPERS_1336 rules). Read-from-glass grammar in post.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_ENVOY_1336_front** (front neutral) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: a foreign envoy of about forty from a northern kingdom, pale olive skin flushed and sweating in the heat, a long black beard dressed in tight rows of oiled curls, heavy black hair to the shoulders bound by a plain band, a heavy fringed wool robe in deep red and blue wrapped around his body, swaying in the blinding sun. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

---

### CHAR_FIRST_TIME_PEOPLE — the PEOPLE OF THE FIRST TIME: sleepers, shepherds, the survivors who pour the red, Seq 3.3
*Group, background · the read-from-glass vision · adults only; the Garden rows use LOC_FIRST_TIME `GARDEN_ROWS`, the shepherds `MOUNTAIN`*

**LONG** (56 words, paste verbatim):

> people of about twelve thousand years ago, adult men and women with sun-darkened olive to brown skin and long dark hair, some of it braided, wearing simple wraps of soft tanned hide and woven plant fibre, necklaces of shell and bone beads, barefoot, lean and weathered, calm faces, seen at a middle distance on open grassland

**SHORT** (19 words, paste verbatim):

> adults of twelve thousand years ago, sun-darkened skin, long dark hair, simple hide and woven-fibre wraps, shell-bead necklaces, barefoot

**Character negative:** children, babies, cave-man caricature, fur bikinis, modern haircuts, metal tools, fantasy costume, face paint

**Notes:** Never children: empty cradles and abandoned toys only (bible §7, 3.3). State add-ons: `asleep in long rows on the grass` · `watching from a high ridge beside their flocks` · `pouring red liquid from tall clay jars across a field at night`.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_FIRST_TIME_PEOPLE_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: on a high rocky ridge above a green prehistoric savannah with a reedy lake, a few adult shepherds of about twelve thousand years ago stand beside their goats, men and women with sun-darkened skin and long dark hair, some of it braided, in simple wraps of soft tanned hide and woven plant fibre, shell-bead necklaces, barefoot, looking down at the plain; humid green-gold morning light, haze, fine film grain, 75mm lens.

---

### CHAR_NEW_MOTHER_2033 — the NEW MOTHER, Seq 12.8 (the first birth after the Garden)
*One-scene face · Seq 12.8 · seen from the shoulders up only (file 03 LOC_HOSPITAL_WAKING)*

**LONG** (51 words, paste verbatim):

> a young Egyptian mother in her twenties, exhausted and radiant, warm light-brown skin, dark hair loose and damp against a white pillow, a pale blue hospital gown, seen from the shoulders up in a raised hospital bed, reaching up with both hands for her swaddled newborn, crying and laughing at once

**SHORT** (23 words, paste verbatim):

> a young Egyptian mother seen from the shoulders up in a hospital bed, dark hair on a white pillow, reaching for her newborn

**Character negative:** celebrity likeness, medical procedure, blood, exposed body, tubes on the face, distress

**Notes:** The newborn is always swaddled and never in face close-up (file 05 §7.4). The midwife is CHAR_MIDWIFE_2033.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_NEW_MOTHER_2033_front** (front, shoulders up) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: head and shoulders, the subject lying back against a white pillow and looking up toward the lens with tears and a smile. Subject: a young Egyptian mother in her twenties, exhausted and radiant, warm light-brown skin, dark hair loose and damp against a white pillow, a pale blue hospital gown, seen from the shoulders up in a raised hospital bed, reaching up with both hands for her swaddled newborn, crying and laughing at once. Soft early-morning window light, clean pale hospital background, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/4.

---

### CHAR_CONSERVATOR_2033 — the CONSERVATOR, coda (Fathi returns the dagger; seq_12 "INT. GEM, TUTANKHAMUN GALLERIES - DAY")
*One-scene face · coda · "FATHI... holds the iron dagger out hilt first to a CONSERVATOR. She takes it in both hands."*

**LONG** (50 words, paste verbatim):

> an Egyptian museum conservator in her forties with warm brown skin, a calm oval face, dark eyes behind thin rimless glasses, a plain navy headscarf neatly pinned, a white lab coat over a grey blouse, white cotton gloves, receiving an ancient object in both open hands with slow, practised care

**SHORT** (18 words, paste verbatim):

> an Egyptian museum conservator in her forties, navy headscarf, rimless glasses, white lab coat and white cotton gloves

**Character negative:** celebrity likeness, logos, readable badge, jewellery

**Notes:** Her gloved hands also set the pectoral back on its mount (PROP_PECTORAL) and lay the trumpet on its cushion.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_CONSERVATOR_2033_front** (front neutral) · aspect ratio **4:5**

   > Photorealistic character reference photo for a live-action film: front view, head and shoulders, neutral relaxed expression, looking straight into the lens. Subject: an Egyptian museum conservator in her forties with warm brown skin, a calm oval face, dark eyes behind thin rimless glasses, a plain navy headscarf neatly pinned, a white lab coat over a grey blouse, white cotton gloves, receiving an ancient object in both open hands with slow, practised care. Plain mid-grey seamless studio backdrop, soft even diffused frontal light with gentle fill, no harsh shadows, no text, no logos. Real human, natural skin texture with visible pores, true-to-life colour, no retouching; not a painting or a 3D render. 85mm portrait lens, f/5.6, sharp focus on the eyes.

---

### CHAR_CONTROL_OPERATORS — CONTROL-ROOM OPERATORS, Seq 4.2 (dark) and 12.8 (relight)
*Group, background · LOC_CONTROL_ROOMS · "An OPERATOR in yesterday's shirt lays her hand flat on the console" (seq_12)*

**LONG** (47 words, paste verbatim):

> control-room operators, adult men and women in rumpled office shirts with lanyards and blank badges, headsets around their necks, seated at tiered desks of monitors, faces lit blue-white by the screens, tired and intent after a long night, seen in singles from the side or from behind

**SHORT** (18 words, paste verbatim):

> tired control-room operators in rumpled office shirts and headsets at tiered monitor desks, faces lit blue-white by screens

**Character negative:** readable screens, logos, flags, real company uniforms, celebrity likeness

**Notes:** Screens stay abstract (file 03). In 12.8 one operator's hand flat on the console is an insert on the 100mm macro.

**Reference stills** (image generator; self-contained; append the common still negative, §0.7, plus the character negative)

1. **CHAR_CONTROL_OPERATORS_still** (in context) · aspect ratio **16:9**

   > Photorealistic film still from a live-action drama, 16:9: in a large modern infrastructure control room at dawn, tired operators in rumpled office shirts with headsets around their necks sit at tiered desks of monitors showing only abstract lines, their faces lit blue-white as the screens flicker back on; one woman lays her hand flat on the console; seen from the side, no readable text, fine film grain, 40mm lens.

---

### Voice-only parts (never on screen; no look-lock)

| Token | Who | Where | Rule |
|---|---|---|---|
| CHAR_SESHAT_VOICE | SESHAT / AMUN | all | see above |
| CHAR_STAFF_OFFICER_VOICE | the calm staff officer relaying the stand-down order "in the Minister of Defence's name" | 4.3 (Tarek's radio), 5.2 (army radio) | radio futz; never pictured; Egyptian Arabic, subtitled |
| CHAR_KITCHEN_WOMAN_VOICE | the woman who calls "Shabti?" off screen | 1.6 main titles (LOC_TITLES_KITCHEN) | off screen; the kitchen plate has no people |
| CHAR_PANEL_CHAIR_VOICE | the hearing's chair | coda (LOC_HEARING_ROOM) | off screen; CHAR_HEARING_PANEL is seen only from behind |

---

## 11. OPEN QUESTIONS AND DECISIONS FOR THE LEAD

1. **Chest window size.** The brief says "coin-sized chest window"; bible v3 §6 and critique ruling ?-4 say a **palm-sized oval port** (a coin-sized window cannot pass the fist-sized vessel). **Resolved here:** the port is palm-sized; the lattice core behind it reads as a coin-sized point of light in G0. Confirm.
2. **"Lattice sternum shadow."** The critique deleted it from plates as unreadable at 1080p. **Kept only** as the plate's micro-texture in the Seq 2.1 mirror shot and as an optional pattern in the COMP glow. Confirm.
3. **G1 colour.** The bible says "warm amber-gold" and the brief says "amber-green". **Resolved here:** amber-gold tinted green by the vessel's yellow-green glass, with hex targets for COMP. Prompts carry no colour words (bible §6).
4. **The fourteenth seam.** Research [01 §3] adds the torso cut "from the pelvis at the iliac crest", so there is a **waist seam** besides neck, shoulders, elbows, wrists, hips, knees and ankles: 14 joint seams in all. It is covered in every shot except the bottom edge of the mirror shot. Confirm.
5. **Which side cracks.** Set as the LEFT wrist (9.4), the LEFT knee (10.4) and the neck below the left ear (12.3). The Seq 9, 10 and 12 screenplays must agree.
6. **Tut's T-C shawl.** Bible §6 gives him "a linen shawl"; §7 12.7 has "Nour's linen shawl" over his face. **Resolved here** as one prop: Nour's lector's shawl (PROP_LINEN_SHAWL), draped on him at 12.3. Confirm against the Seq 12 screenplay.
7. **Prop alignment.** Tokens follow `04_props.md` (PROP_DAGGER, PROP_EBONY_STICK as a 1.35 m staff, PROP_CLINIC_CANE for Seq 2–4.4, PROP_LAYLA_PENDANT, PROP_RAMI_NOTEBOOK, PROP_INDEX_CARDS, PROP_LAMP_1925, PROP_IRON_ADZE_1323, PROP_BURTON_PLATES, PROP_SCARAB_KEYRING, PROP_TABLET_LAYLA, PROP_SLEEP_BRACELET, PROP_REPLICA_VESSEL, PROP_CONSERVATION_KIT, the trumpets). **Resolved by the cross-check:** PROP_LINEN_SHAWL, PROP_JACKAL_MASK, PROP_PAINTER_PALETTE, PROP_SCRIBE_PALETTE_1330 and PROP_BROADCAST_RIG_1939 are now locked in `04_props.md` §20.
8. **"Vance" in the brief** is taken as **Victor HALE** (renamed in v3; screenplay spec v3 note).
9. **Painter and embalmers.** The bible gives the last painted eye to the lector (7, 1.2), so CHAR_PAINTER_1323 is optional. "Embalmers" are two: the masked one and the young priest who cries out.
10. **1939 cast. Resolved by the cross-check:** seq_04 has a white-gloved bandsman play the bronze trumpet live at the gala, so CHAR_BANDSMAN_2033 (§10b) carries the beat and §8 is reserve. If a 1939 insert is ever cut in, the side-cap colours (11th Hussars) still need a military costume check.
11. **Period dress to sign off** (Egyptologist / costume): Ay's mourning stubble (Herodotus II.36) and his blue crown at the burial, mirroring the north wall; Ankhesenamun's blue-grey mourning shawl; the child's sidelock and the child crown at 11; Nefertiti's red sash; the Hildesheim-style mask paint; the "gold of honour" collars.
12. **Hamdi's tarboosh** is period-accurate for 1925 and is not the modern-Egypt fez cliché bible §11 bans. Flag it for the localisation consultant.
13. **The young mother's heart.** Bible 9.5(b) has her "lift out her own sealed heart", which implies a chest vessel like Tut's in a living woman. The screenplay must choose: a chest vessel (use Tut's glow overlay, warm) or a vessel carried in her hands.
14. **Akhenaten's chest light at 12.2** is set to cool white (COMP), to keep it distinct from Tut's G-states. Confirm.
15. **Mina's Coptic cross tattoo** is a respectful tell-apart detail. Confirm with the localisation consultant, or swap it for a neutral mark.
16. **1925 and 1968 looks** (Carter, Derry, Burton, the radiologist) are plausible period types drawn from general knowledge, not from the research files. Check them against period photographs for plausibility only: no likeness is to be chased, and Burton's plates are never used as generator input.
17. **Soldier headgear:** berets at the GEM (Seq 1–4, wardrobe **M** for Mina, Youssef and Karim) and tan helmets from Seq 5 (wardrobe **A**). Tarek keeps his beret throughout (his anchor) and Fathi goes bareheaded (for face identity). The cross-check moved Karim's helmet out of his LONG/SHORT lock and into the wardrobe phrase, so the lock is valid in both states.
18. **One-scene faces added by the cross-check** (§10b): the gala bandsman, the young police officer, the old fisherman, the envoy (c. 1336 BC), the new mother and the conservator. They are needed by the screenplay's speaking or face-visible beats and sit outside bible §6's twelve locked faces, like the 1925 four. Confirm, or cut them to backs and hands.
19. **Karim's age.** This file locks him at 24; seq_04 introduces "PVTS. MINA, YOUSSEF and KARIM (19)". The picture follows the lock (the age never appears in a prompt beyond "twenty-four"); the screenplay editor should align the parenthetical, or the lead should re-lock him at 19.
20. **Coda wardrobes added by the cross-check:** Adaeze **D** (the hearing, with a cane), Layla **C** (KV21, the raincoat without the keyring she gave away in 2.4) and Fathi **C** (the gallery, returning the dagger), per seq_12.

## APPENDIX: QUICK SHORT-FORM TABLE (copy from the entries above; this table is for lookup)
(Regenerated by the cross-check from the entries above; if the two ever differ, the entry wins. The film-wide list of every token is `00_INDEX.md`.)

| Token | SHORT look-lock | Wardrobe codes |
|---|---|---|
| CHAR_TUT | a slight olive-skinned Egyptian young man, shaved head with faint stubble, visible overbite, very dark bright eyes, thin gold seam ring around his neck | A0 (T-A), B1–B3 (T-B), C3 (T-C) |
| CHAR_TUT_BODY_1323 | a slight young man lying still under white linen drawn to the collarbones, shaved head, eyes closed, face in profile, half in shadow | — (1.1) |
| CHAR_TUT_CRADLE_2033 | a slight young man on a titanium cradle under a white sheet to the collarbones, eyes closed, gold light ringing his neck | — (1.5) |
| CHAR_TUT_CODA_CASE | a small linen-wrapped form on pale sand in a glass climate case, the face shrouded, only a thin gold seam at one wrist showing | — (coda) |
| CHAR_TUT_D1 | a slight young man's face in first sunlight, dark eyes slowly closing, a small peaceful smile, the cracked gold neck seam catching the light | T-C, L3, G2 (12.7) |
| CHAR_TUT_D2 | wide backlit silhouette against the rising sun: a woman and a broad-shouldered man gently lower a slight young man onto stone steps | T-C, L3, G2 (12.7) |
| CHAR_TUT_D3 | two still hands laid low across the body, skin dry dark bronze-brown like old parchment around thin gold wrist seams, blue cornflowers beside them | T-C, L3, G2 (12.7) |
| CHAR_TUT_D4 | from above, a still young man on pale stone, a cream linen shawl and blue cornflowers covering half his face, closed eyes, dark bronze-brown skin | T-C, L3, G2 (12.7) |
| CHAR_NOUR | a lean Egyptian woman of thirty-eight, dark curly hair tied back, thick straight brows, reading glasses on a cord, olive field jacket | A, B, C |
| CHAR_ADAEZE | a tall British-Nigerian woman of forty-four, deep brown skin, close-cropped natural hair, round tortoiseshell glasses, navy blazer over a grey hoodie | A, B, C, D (coda) |
| CHAR_TOMAS | a very tall, lanky Swedish man of fifty, full short grey beard, thinning swept-back grey hair, pale-blue shirt with rolled sleeves | A, B, C |
| CHAR_TAREK | a barrel-chested Egyptian colonel of fifty-two, heavy grey moustache, black beret, weathered deep-tanned face, desert-camouflage uniform | A, B, C |
| CHAR_FATHI | a broad-shouldered Nubian Egyptian soldier of thirty-one, deep dark-brown skin, close black beard, red-patterned scarf at the neck, desert camouflage | A, B, C (coda) |
| CHAR_RAMI | a wiry, clean-shaven Egyptian man of twenty-seven, black-rimmed glasses, short black hair wavy on top, bright yellow windbreaker | A, B |
| CHAR_HALE | a lean American man of sixty, silver hair swept straight back, tanned lean face, charcoal suit with an open-collared white shirt | A, B, C |
| CHAR_LAYLA | a small nine-year-old Egyptian girl, round face, big dark eyes, two curly pigtails, bright yellow raincoat | A, B, C (coda) |
| CHAR_AKHENATEN | a slender Egyptian man in his late twenties, long jaw, full lips, heavy-lidded eyes, smooth shaved head, pleated white linen, gold disk pendant | A, B |
| CHAR_AKHENATEN_1336 | a slender Egyptian man of about thirty-five, long jaw, full lips, heavy-lidded eyes, tall blue crown with a gold cobra, pleated white linen | R |
| CHAR_HASSAN | a heavy-set Egyptian corporal of thirty-five, round face, thick black moustache, thin metal glasses, black beret, desert camouflage | A |
| CHAR_MINA | a tall, lanky Egyptian private of twenty-two, long boyish face, big ears, faint moustache, small blue cross tattoo on the right wrist | M (Seq 1–4), A (Seq 5 on) |
| CHAR_YOUSSEF | a stocky Egyptian private of twenty-five, square jaw, shaved head, scar through the right eyebrow, flattened nose, desert camouflage | M (Seq 1–4), A (Seq 5 on) |
| CHAR_KARIM | a wiry Egyptian private of twenty-four, freckled light-brown skin, hazel eyes, curly dark hair, desert camouflage | M (Seq 1–4), A (Seq 5 on) |
| CHAR_AY | a lean, stooped Egyptian elder in his sixties, hollow-cheeked weathered face, hooked nose, short grey stubble, heavy gold disc-bead collars | A, B |
| CHAR_ANKHESENAMUN | a slender Egyptian woman of about twenty, heart-shaped face, grief-reddened dark eyes, long loose dark hair, pale blue-grey linen shawl | A |
| CHAR_LECTOR_1323 | a thin shaved-headed Egyptian priest in his forties, calm dark eyes, white linen sash across his chest, pleated kilt, papyrus roll | A |
| CHAR_EMBALMER_JACKAL | a heavy-set embalmer in a worn black-painted clay jackal mask with low eye-holes, resin-stained forearms, white linen kilt and apron | A |
| CHAR_EMBALMER_PRIEST | a thin young shaved-headed Egyptian priest, wide anxious eyes, slightly crooked nose, white linen kilt and short shawl | A |
| CHAR_PAINTER_1323 | a small wiry Egyptian tomb painter in his fifties, grey-stubbled shaved head, squinting eyes, pigment-stained fingers, reed brushes behind his ear | A |
| CHAR_NEFERTITI | a regal Egyptian woman of thirty-five, long slender neck, high cheekbones, strong brows, tall flat-topped blue crown with a gold band | A, B |
| CHAR_TUT_CHILD_9 | a slight nine-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right | 9 (c. 1332 BC) |
| CHAR_TUT_CHILD_6 | a slight six-year-old Egyptian boy, very dark bright eyes, visible overbite, shaved head with one braided sidelock on the right | 6 (c. 1336 BC) |
| CHAR_TUT_CHILD_11 | a slight eleven-year-old Egyptian boy, very dark bright eyes, visible overbite, a cleanly shaved head, grave and watchful | 11 (c. 1330 BC) |
| CHAR_YOUNG_MOTHER | a slight Egyptian woman of about twenty-five, very dark bright eyes, slight overbite, fine shoulder-length braids under a gold circlet, pleated white linen | A |
| CHAR_PAWAH | a heavy-set shaved-headed Egyptian priest in his fifties, round fleshy face, full lower lip, white linen sash, papyrus roll | A |
| CHAR_MERITATEN | a slender young Egyptian woman of about eighteen, long neck, short rounded dark layered wig with a gold circlet, pleated white linen | A |
| CHAR_CARTER_1925 | a solid Englishman of about fifty, full dark moustache, flat-combed receding dark hair, rolled shirtsleeves, dark waistcoat and bow tie | A |
| CHAR_DERRY_1925 | a tall, lean, balding British anatomist of about fifty, clean-shaven, round steel-rimmed spectacles, white surgeon's coat over collar and tie | A |
| CHAR_HAMDI_1925 | a stout Egyptian physician in his sixties, thick grey moustache, round gold-rimmed spectacles, red tarboosh, dark three-piece suit | A |
| CHAR_BURTON_1925 | a slim fair Englishman in his mid-forties, thinning sandy hair, clean-shaven, rolled shirtsleeves, black focusing cloth over his shoulder | A |
| CHAR_IBRAHIM_1925 | a slim young Upper-Egyptian man, thick straight brows, deep-set eyes, thin moustache, white skullcap, striped galabiya and dark waistcoat | A |
| CHAR_BANDSMAN_1939 | a slim, fair young British army bandsman of the 1930s, clean-shaven, brown-and-crimson side cap, khaki drill tunic with brass buttons | A (reserve) |
| CHAR_RADIO_ENGINEER_1939 | a British radio engineer of about forty, pencil moustache, round wire spectacles, heavy black headphones, white shirt and braces, loosened tie | A (reserve) |
| CHAR_RADIOLOGIST_1968 | a British radiologist in his late forties, tired clean-shaven face, black horn-rimmed glasses, side-parted greying hair, white coat, narrow tie | A |
| CHAR_XRAY_ASSISTANT_1968 | a young British radiographer of about twenty-five, freckled, auburn short bob, white coat over a pale blue uniform dress | A |
| CHAR_MINISTER_GALA | a heavy-set grey-haired official in his sixties in a dark navy suit, seen only in wide shots at a lectern | — |
| CHAR_SAMEH | a man in his forties in a dark grey jacket, seen from behind, holding a small girl's hand in a crowd | — |
| CHAR_MIDWIFE_2033 | a kind Egyptian midwife in her fifties, white headscarf, pale-green scrubs, lifting a newborn swaddled in clean white cloth | — |
| CHAR_GARDEN_SLEEPERS | rows of peaceful adult sleepers on pale mats in everyday clothes, thin silver bracelets on their wrists, soft white light | — |
| CHAR_AMARNA_SLEEPERS_1336 | rows of Egyptians in white linen asleep beside low stone offering tables in a roofless court of blinding white-gold light | — |
| CHAR_AMARNA_COURTIERS_1336 | background Egyptian courtiers in pleated white linen and short dark wigs, blue faience collars, olive to brown skin, softened by haze | — |
| CHAR_HEARING_PANEL | a panel of officials seen from behind, out of focus, at a plain unmarked table in a bare pale-wood hearing room | — |
| CHAR_BANDSMAN_2033 | an Egyptian military bandsman in his thirties, clean-shaven, dark ceremonial dress tunic with brass buttons, white lanyard and white gloves | — |
| CHAR_YOUNG_OFFICER | a young Egyptian police officer, thin face, faint moustache, wide dark eyes, black peaked cap and black winter uniform | — |
| CHAR_POLICE_LINE | a line of Egyptian police officers in black winter uniforms and peaked caps, shoulder to shoulder behind a low steel barrier | — |
| CHAR_GALA_GUESTS | adult gala guests in evening dress at round white-clothed tables, press photographers at the edges, a string quartet in black | — |
| CHAR_DEFENCE_MINISTER_GALA | a stocky grey-haired official in a dark army dress uniform at a distant top table, seen only in wide shots | — |
| CHAR_ARMY_DETAIL | background Egyptian soldiers in desert camouflage, black berets or tan helmets, rifles held across the body, faces never clear | — |
| CHAR_OLD_FISHERMAN | an old Upper-Egyptian fisherman, sun-creased deep brown face, white stubble, loose white turban, faded brown galabiya, hand on a tiller | — |
| CHAR_NIGHT_FISHERMEN | Nile fishermen in faded galabiyas working nets from small wooden boats by kerosene lantern light on black water | — |
| CHAR_ENVOY_1336 | a sweating foreign envoy with a long black beard in rows of oiled curls, wrapped in a heavy fringed red-and-blue wool robe | — |
| CHAR_FIRST_TIME_PEOPLE | adults of twelve thousand years ago, sun-darkened skin, long dark hair, simple hide and woven-fibre wraps, shell-bead necklaces, barefoot | — |
| CHAR_NEW_MOTHER_2033 | a young Egyptian mother seen from the shoulders up in a hospital bed, dark hair on a white pillow, reaching for her newborn | — |
| CHAR_CONSERVATOR_2033 | an Egyptian museum conservator in her forties, navy headscarf, rimless glasses, white lab coat and white cotton gloves | — |
| CHAR_CONTROL_OPERATORS | tired control-room operators in rumpled office shirts and headsets at tiered monitor desks, faces lit blue-white by screens | — |
| CHAR_SESHAT_VOICE · CHAR_STAFF_OFFICER_VOICE · CHAR_KITCHEN_WOMAN_VOICE · CHAR_PANEL_CHAIR_VOICE | (voice only: no look-lock) | — |
