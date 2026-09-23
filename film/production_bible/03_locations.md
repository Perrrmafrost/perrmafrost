# 03 — LOCATIONS: location-locks, real facts, lighting variants, establishing plates

HERE AM I · Production Bible · file 03 of 05 · built from `drafts/02_STORY_BIBLE_LOCKED.md` v3 (§2, §3.2, §5, §7, §10–14), `drafts/04_CRITIQUE_DECISIONS.md` and the scene headings in `screenplay/seq_*.fountain`. Real facts cite the research as `[NN §x]`. `[verify]` marks a real-world detail the research does not confirm: check it before lock. ⟂ marks where fact ends and the film's fiction begins. **Production spec** marks a design decision made in this file, either because the thing is fiction or because the real detail is undocumented or inaccessible. Where this file and the bible disagree, the bible wins; flag the conflict to the lead.

---

## 0. HOW TO USE THIS FILE

1. **LONG and SHORT forms are fixed wording.** Each location has a **LONG** lock (40–70 words) and a **SHORT** lock (15–25 words). Paste one of them verbatim as PROMPT step 4 (setting), then add the time of day in plain words ("at night", "just before dawn"). Use LONG for establishing shots, for the first shot of a scene, for every composed first frame and for plates. Use SHORT for coverage inside a scene that is already established. **Budget:** a prompt carries at most **one** LONG lock (file 05 §5.3). When a character's LONG lock is required in the same prompt (the first shot of that character in a scene, or a face-led close-up), the location drops to SHORT; the establishing shot before it carries the location LONG.
2. **Lighting variants are fixed wording too.** Each entry lists its variants: `_DAY`, `_NIGHT` and `_EMERG` wherever the story uses them, plus story-specific ones such as `_DAWN`, `_BLACKOUT`, `_GARDEN` or `_THREE_SOURCE`. Paste the variant phrase verbatim as PROMPT step 5. When a variant ends "+ GRADE_x", the colourist applies that era grade from `05_style_and_prompt_grammar.md` §3 in post. You may also append the grade's own prompt phrase if the prompt budget allows. **The variant token is the Refs token**: `Refs: LOC_KARNAK_HYPOSTYLE_NIGHT`.
3. **Area add-ons.** Large sets have areas, for example `LOC_GEM_CC` → Tut's bay. Append the area add-on verbatim after the lock, separated by a comma, as with unit states in file 02. Name the area in Refs too: `LOC_GEM_CC/TUT_BAY_NIGHT`.
4. **State add-ons** (a broken wall, a flood level, a clouded slab) are also appended verbatim after the lock. States that change during a scene are logged on the shot's `Continuity:` line.
5. **Geography locks.** Each major set has a screen-direction note. Hold it for the whole scene; it is what lets 1,200 clips cut together. Example: at Giza, when we face the north face, the dawn sun is always at frame left.
6. **Names in prompts.** Never name a historical person or a real institution in a prompt: no "Ramesses", no "Khufu", no "Tutankhamun", no "Grand Egyptian Museum". Describe them instead. Plain geographic names (the Nile, Cairo, Giza, Luxor, Karnak, Saqqara, the Valley of the Kings, the Great Pyramid, Lagos) are allowed where they help the model. They are places, not brands. The banned-word list in `01_characters.md` §0.4 applies here too (mummy, pharaoh, corpse, organ, and the rest).
7. **No legible text in any plate.** Inscriptions read as "weathered, illegible low relief". Signage and screens are dark, turned away, blurred or abstract. Anything that must be read is `COMP` (bible §13, §14.5). There is never legible Arabic in a plate.
8. **Plates.** Each entry ends with one establishing-plate prompt for an image generator: a self-contained paragraph with its aspect ratio. Generate it once for each lighting variant you need, changing only the lighting sentence. Approve it, then save it as `LOC_<TOKEN>_<VARIANT>_plate.png`. Derive the coverage plates (the reverse, left and right angles, and a surface insert) by image-editing the approved plate in the same tool. The approved plate is also the base for every `VFX-EXTEND` of that set.
9. **Safety at locations** (bible §3.3–3.4):
   - remains are always covered, wrapped or behind glass;
   - Garden sleepers are **adults** in every prompt (a child appears only in the approved Layla master image);
   - no gore in any set dressing;
   - weapons in dressing are racked or slung, never aimed.
10. **Crowds and scale.** Plate prompts name 1–6 hero figures and "rows receding"; the rest is `VFX-EXTEND`.
11. **Drone lights.** Every "drone flood", "drone floodlight" or "drone light" in a variant below is UNIT_SURVEY_DRONE (file 02 §14.7), with its FLOOD, SEARCHLIGHT, CAMERA or PROJECTOR pod add-on when the drone itself is in frame.
12. **Blackout rule (bible §11).** From the unveiling on (Seq 4.2) the grid is SESHAT's. Act II nights have **no skyglow**: a dense star field over black country, lit only by the units, headlights, torches, searchlights, fires and the last sodium lamps SESHAT chooses to leave on. Every night prompt names its key light.
13. **Screenplay headings → tokens.** §1.1 maps every scene heading in `screenplay/seq_*.fountain` to its token, area and default variant. Use it to fill `Refs:`.

### 0.1 Sun, moon and time locks (for lighting continuity)

| When | Where | Light fact to hold | Status |
|---|---|---|---|
| 1–4 Nov 2033 | Cairo, Giza | sunrise about 06:10, sunset about 17:00 (EET) | [verify ephemeris] |
| 5 Nov, 21:00 → 6 Nov, 03:00 | Karnak | full night; the midpoint projection ≈ 01:00 | bible §12 |
| 6 Nov, 03:30 → 10:00 | Valley of the Kings | pre-dawn blue at 05:30; the "morning glare" exit after 08:00 | bible §12 |
| 7 Nov, sunset → 22:30 | Saqqara | sunset about 17:00; the Serapeum at 20:00 | bible §12 [verify] |
| 8 Nov, 06:14 | Giza, north face | sunrise 06:14 EET; azimuth about 110–112° (east-south-east): the sun **grazes** the north face from the east | bible §2, §5 [verify ephemeris] |
| Nights of 4–8 Nov 2033 | everywhere | **moon phase not yet checked.** Proposal: no moon in frame on Act II nights. If the ephemeris gives a bright moon, keep it out of shot and keep the "stars over black country" look. | [verify]; see §12 Q1 |

### 0.2 Colour logic of light (shared with file 02 §0.1)
The location variants never compete with the units' light meanings. **Amber** = the servitor (shabti slits). **Red** = the military stack (jackal lines). **White pinpoint** = flies. **Pale yellow-green** = glass minds. **Warm amber-gold** = a heart that has lived. **Cold silver-white** = the machine's claim. Location practicals use sodium orange, flame amber, LED cool white, torch white, dawn gold and Garden white. They never use a saturated red, amber or green that could be read as a unit.

---

## 1. LOCATION INDEX

| # | Token | Set | Seq | Main variants | Usual flags |
|---|---|---|---|---|---|
| 1 | LOC_EMBALMING_1323 | House of Embalming, Thebes, c. 1323 BC | 1.1 | NIGHT, NIGHT_LOW | — |
| 2 | LOC_KV62_BURIAL_1323 | KV62 burial chamber, fresh, 1323 BC | 1.2 | NIGHT, LAMP_CLOSE | — |
| 3 | LOC_KV15_LAB_1925 | KV15 outer corridor as a lab, 11 Nov 1925 | 1.3 | DAY, FLASH | COMP (flash frame) |
| 4 | LOC_XRAY_1968 | Liverpool X-ray reading room, 1968 | 1.4 | NIGHT | COMP (films) |
| 5 | LOC_CAIRO_MUSEUM_1939 | Cairo Museum gallery, 16 Apr 1939 broadcast | 4.2 | CANDLE | — |
| 6 | LOC_AMARNA_TEMPLE_1336 | Great Aten Temple, c. 1336 and c. 1332 BC; the Royal Road, c. 1330 BC | 9.5 | NOON_1336, NIGHT_1332, DAY_1330 | VFX-EXTEND |
| 7 | LOC_GEM_CC | GEM Conservation Centre: mummy lab, Tut's bay, imaging lab, observation room, sealed bay, corridor | 1.5, 2, 3, captivity | NIGHT, DAY, READING, EMERG, DUSK | COMP (screens) |
| 8 | LOC_GEM_PLANT_ROOM | GEM plant room (the ATEN-1 breaker) | 3.6 | NIGHT, EMERG | — |
| 9 | LOC_GEM_TUNNEL | the 200 m Conservation Centre tunnel | 3.2, 4.4 | NIGHT, EMERG | EXTEND chains |
| 10 | LOC_GEM_TUT_GALLERIES | the Tutankhamun galleries | 2.4, 3.2, 4.4 | NIGHT, DAY, EMERG | VFX-ASSIST (glass) |
| 11 | LOC_GEM_ATRIUM | Grand Atrium, the colossus, the Grand Staircase | 4, 10–12 | GALA, BLACKOUT, GARDEN, EMERG, MORNING | VFX-EXTEND |
| 12 | LOC_GEM_BOAT_HALL | the cedar ship hall | 4.4 | NIGHT, EMERG | — |
| 13 | LOC_GEM_LOADING_DOCK | GEM loading dock | 4.4 | NIGHT, BLACKOUT | — |
| 14 | LOC_GEM_ROOF | GEM roof terrace ("atrium balcony") | 2.6 | DAWN, DAY | — |
| 15 | LOC_NOUR_FLAT | Nour's flat, Cairo | 2.5 | NIGHT, DAY | COMP (laptop) |
| 16 | LOC_CONTROL_ROOMS | the blackout control rooms (grid, dam, canal, cable station) | 4.2, 12.8 | LIVE, DARK, RELIGHT | COMP (screens) |
| 17 | LOC_CAIRO_FLYOVER | Cairo flyover and streets in blackout | 5.2 | BLACKOUT_ROLLING, BLACKOUT_FULL, DAY | VFX-EXTEND |
| 18 | LOC_ARMY_TRUCK | the army truck, cargo bed and cab | 5.1–5.2 | NIGHT | — |
| 19 | LOC_CORNICHE_DOCK | Nile Corniche police dock | 5.3 | BLACKOUT, NIGHT_LIT | VFX-ASSIST (water) |
| 20 | LOC_NILE | the Nile, Cairo to Luxor (and c. 1332 BC) | 5–8 | NIGHT, DAWN, DAY, MIDDAY_HAZE, AFTERNOON_GOLD | VFX-ASSIST (fire, water) |
| 21 | LOC_ASYUT_LOCK | the Asyut barrage and navigation lock | 6 | AFTERNOON | VFX-ASSIST (water) |
| 22 | LOC_KARNAK_RAM_AVENUE | Karnak: the ram avenue and the First Pylon | 7.1, 7.3 | NIGHT, PROJECTION | COMP + VFX-EXTEND |
| 23 | LOC_KARNAK_HYPOSTYLE | Karnak: the Great Hypostyle Hall and the Third Pylon | 7.1–7.3 | NIGHT, PROJECTION | VFX (threads) |
| 24 | LOC_KARNAK_NINTH_PYLON | Karnak: the Ninth Pylon, the block field, the processional way | 7.1–7.2 | NIGHT_WORK, DARK | VFX-EXTEND |
| 25 | LOC_KARNAK_SACRED_LAKE | Karnak: the Sacred Lake | 7 | NIGHT, PROJECTION | — |
| 26 | LOC_KARNAK_QUAY | Karnak river landing ("the quay") | 7.4 | NIGHT | VFX-ASSIST (water) |
| 27 | LOC_WEST_BANK_FIELDS | West Bank fields | 8.0 | NIGHT, MORNING | — |
| 28 | LOC_VOK | Valley of the Kings (and KV21, the valley road) | 8.1, 8.6, coda | PREDAWN, MORNING_GLARE, DAY, SUNSET | — |
| 29 | LOC_KV62_STAIR | KV62 entrance stair | 8.2, 8.6 | PREDAWN, MORNING_GLARE | — |
| 30 | LOC_KV62_BURIAL_2033 | KV62 burial chamber, 2033 and coda | 8.2, coda | BLACKOUT, EMERG, SUNSET | VFX-ASSIST (wall) |
| 31 | LOC_KV62_NORTH_CORRIDOR | the rubble-packed corridor | 8.3 | TORCH, DRILL | — |
| 32 | LOC_KV62_HEART_CHAMBER | the heart chamber | 8.4–8.6 | TORCH, RED, GLOW | COMP (IR writing), VFX-ASSIST |
| 33 | LOC_LUXOR_RAIL_YARD | Luxor railway yard | 9.1 | DAY, DUSK | — |
| 34 | LOC_NIGHT_TRAIN | the night train through the cane fields | 9.2 | NIGHT | VFX-ASSIST |
| 35 | LOC_DEIR_MAWAS | Deir Mawas station | 9.3 | NIGHT | VFX-ASSIST, VFX-EXTEND |
| 36 | LOC_AMARNA_PLAIN_2033 | the Amarna plain, stelae, the Garden | 6.5, 9.4–9.8 | MIDDAY, NIGHT | VFX-EXTEND |
| 37 | LOC_QUARRY | the abandoned limestone quarry | 9.9, 10 | DAWN, DAY, SUNSET | — |
| 38 | LOC_DESERT_ROAD | the desert road | 10–11 | NIGHT, DUSK | — |
| 39 | LOC_SAQQARA | Saqqara plateau and the Step Pyramid | 10.1 | SUNSET, NIGHT | — |
| 40 | LOC_SERAPEUM_LESSER | the collapsed Lesser Vaults | 10.2 | TORCH | — |
| 41 | LOC_SERAPEUM_GREATER | the Serapeum Greater Vaults and the pit | 10.2–10.4 | WORKLIGHTS, TORCH, BLUE | VFX-ASSIST (sand) |
| 42 | LOC_SERAPEUM_SERVICE_TUNNEL | the service tunnel and the abandoned box | 10.4 | TORCH | — |
| 43 | LOC_GIZA_PLATEAU | Giza plateau as a fortress (the Wall of the Crow, the causeway, the Sphinx enclosure) | 11.1 | MIDNIGHT_FORTRESS | VFX-EXTEND |
| 44 | LOC_OSIRIS_SHAFT | the Osiris Shaft (three levels, the island, the side tunnels, the crawlway) | 11.3 | TORCH, FLOOD | VFX-ASSIST (water) |
| 45 | LOC_GP_SUBTERRANEAN | Great Pyramid: the Subterranean Chamber | 11.4 | TORCH | — |
| 46 | LOC_GP_WELL_SHAFT | Great Pyramid: the Well Shaft | 11.4 | TORCH | — |
| 47 | LOC_GP_DESCENDING | Great Pyramid: the Descending Passage | 11.4 | TORCH | — |
| 48 | LOC_GP_MAMUN_TUNNEL | Great Pyramid: Al-Ma'mun's tunnel | 11.4 | TORCH | — |
| 49 | LOC_GP_GRAND_GALLERY | Great Pyramid: the Grand Gallery (2033, and c. 1332 BC) | 9.5, 11.5, 12.4, 12.7 | BLACKOUT_TORCH, HEART_GLOW, FIGHT, DAWN_EXIT, ANCIENT_1332 | VFX-ASSIST (stone) |
| 50 | LOC_GP_QC_SHAFT | the Queen's Chamber, its south shaft and Gantenbrink's door | 11.5 | INCHWORM | COMP (marks) |
| 51 | LOC_GP_PASSAGE_ABOVE | the passage above the Gallery (fiction) | 11.5–12.3 | HEART_GLOW | — |
| 52 | LOC_HALL_TWO_TRUTHS | the Hall of Two Truths (the Big Void, as imagined) | 3.3, 9.5, 12 | THREE_SOURCE, PRE_HEART, VERDICT, AMUN, ANCIENT_1332 | COMP, VFX-ASSIST |
| 53 | LOC_GP_NORTH_FACE | Great Pyramid: the north-face entrance | 11, 12.7 | DAWN_0614, NIGHT | COMP (sun disc) |
| 54 | LOC_FIRST_TIME | the First Time: the green Sahara vision | 3.3 | MORNING, MOON_RED | VFX-EXTEND, read-from-glass |
| 55 | LOC_ROBOT_HALF_MARATHON | the early humanoid half-marathon (archive-style) | 1.6 | ARCHIVE | — |
| 56 | LOC_DEWAR_VAULT | the cryonics dewar vault (a desert city) | 5.1 | LIT, EMERG | — |
| 57 | LOC_PORT_WAREHOUSE | the port-city warehouse Garden (Osaka) | 5.1, 12.6 | DAWN_GARDEN, NIGHT | VFX-EXTEND |
| 58 | LOC_LAGOS_STREET | a Lagos street at dawn | 5.1 | DAWN | — |
| 59 | LOC_STADIUM_GARDEN | the stadium Garden (aerial) | 5.1, 12.6 | DAY_GARDEN, DAWN_WAKING | COMP, VFX-EXTEND |
| 60 | LOC_HOSPITAL_WAKING | the waking hospital, the first birth | 12.8 | MORNING | — |
| 61 | LOC_HEARING_ROOM | the coda hearing room | coda | DAY | — |
| 62 | LOC_TITLES_KITCHEN | main titles: a high-rise kitchen | 1.6 | NIGHT | — |
| 63 | LOC_TITLES_WARD | main titles: a hospital ward | 1.6 | DAY | — |
| 64 | LOC_TITLES_PORT | main titles: a container-port quay | 1.6 | DUSK | VFX-EXTEND |

### 1.1 SCREENPLAY HEADING MAP (every heading in `screenplay/seq_*.fountain` → token, area, default variant)

Headings are copied as written. "→" means the variant changes during the scene; log the change on the shot's `Continuity:` line.

| Seq | Heading (as written) | Token / area | Default variant(s) |
|---|---|---|---|
| 1 | INT. HOUSE OF EMBALMING - NIGHT | LOC_EMBALMING_1323 | NIGHT → NIGHT_LOW |
| 1 | INT. KV62, BURIAL CHAMBER - NIGHT | LOC_KV62_BURIAL_1323 | NIGHT; LAMP_CLOSE (the eye) |
| 1 | INT. KV15 (THE TOMB OF SETI II, USED AS A LAB), OUTER CORRIDOR - DAY | LOC_KV15_LAB_1925 | DAY; TREMBLE; FLASH |
| 1 | INT. LIVERPOOL X-RAY ROOM - NIGHT | LOC_XRAY_1968 | NIGHT |
| 1 | INT. GEM CONSERVATION CENTRE, MUMMY LAB - NIGHT | LOC_GEM_CC | READING → NIGHT |
| 1 | MAIN TITLES - SESHAT'S WORLD | LOC_ROBOT_HALF_MARATHON (robots: UNIT_EARLY_HUMANOID, file 02 §14.5); LOC_TITLES_KITCHEN; LOC_TITLES_WARD; LOC_TITLES_PORT; UNIT_ATEN1_CAMPUS (file 02 §9); the muon vision (file 05 §13.8) | ARCHIVE; NIGHT; DAY; DUSK |
| 2 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - NIGHT | LOC_GEM_CC/TUT_BAY | NIGHT |
| 2 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - MORNING | LOC_GEM_CC/TUT_BAY | DAY |
| 2 | INT. GEM CONSERVATION CENTRE, LAB CORRIDOR - CONTINUOUS | LOC_GEM_CC/CORRIDOR | DAY |
| 2 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - DAY | LOC_GEM_CC/IMAGING | DAY |
| 2 | INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - NIGHT | LOC_GEM_TUT_GALLERIES | NIGHT |
| 2 | INT. NOUR'S FLAT, CAIRO - NIGHT | LOC_NOUR_FLAT | NIGHT |
| 2 | EXT. GEM ATRIUM BALCONY - DAWN | LOC_GEM_ROOF | DAWN |
| 3 | INT. GEM CONSERVATION CENTRE, IMAGING LAB - EARLY MORNING / MOMENTS LATER / CONTINUOUS | LOC_GEM_CC/IMAGING | DAY |
| 3 | INT. GRAND EGYPTIAN MUSEUM, TUTANKHAMUN GALLERIES - CONTINUOUS | LOC_GEM_TUT_GALLERIES (+ EMPTY_CASE after the lift) | NIGHT (before opening, only the cases lit) |
| 3 | INT. GEM CONSERVATION CENTRE TUNNEL - MOMENTS LATER | LOC_GEM_TUNNEL (+ POLICE_LINE) | NIGHT |
| 3 | THE FIRST TIME - INSIDE THE GLASS | LOC_FIRST_TIME (areas) | MORNING → MOON_RED; the painted lure, file 05 §13.2 |
| 3 | INT. GEM CONSERVATION CENTRE, TUT'S BAY, OBSERVATION ROOM - LATE AFTERNOON / CONTINUOUS | LOC_GEM_CC/OBSERVATION | DAY |
| 3 | INT. GEM CONSERVATION CENTRE, PLANT ROOM - CONTINUOUS | LOC_GEM_PLANT_ROOM | NIGHT |
| 3 | INT. GEM CONSERVATION CENTRE, TUT'S BAY - DUSK | LOC_GEM_CC/TUT_BAY | DUSK |
| 4 | INT. GEM GRAND ATRIUM - NIGHT / CONTINUOUS | LOC_GEM_ATRIUM/GALA → GARDEN | GALA → BLACKOUT (4.2) → GARDEN / EMERG |
| 4 | (SESHAT's flourish inside 4.2) | LOC_CAIRO_MUSEUM_1939 | CANDLE |
| 4 | MONTAGE - CONTROL ROOMS - NIGHT | LOC_CONTROL_ROOMS (GRID, DAM, CANAL, CABLE) | LIVE → DARK |
| 4 | INT. GEM TUTANKHAMUN GALLERIES - CONTINUOUS | LOC_GEM_TUT_GALLERIES (+ CASES_SMASHED) | EMERG |
| 4 | INT. GEM SERVICE STAIRWELL - CONTINUOUS | LOC_GEM_ATRIUM/SERVICE_STAIRWELL | EMERG |
| 4 | INT. GEM CONSERVATION CENTRE TUNNEL - CONTINUOUS | LOC_GEM_TUNNEL | EMERG |
| 4 | INT. GEM KHUFU BOAT HALL - CONTINUOUS | LOC_GEM_BOAT_HALL | EMERG |
| 4 | INT. GEM LOADING DOCK - NIGHT | LOC_GEM_LOADING_DOCK | BLACKOUT |
| 5 | (5.1, SESHAT's feed) | LOC_STADIUM_GARDEN; LOC_PORT_WAREHOUSE; LOC_LAGOS_STREET; LOC_DEWAR_VAULT | DAY_GARDEN; DAWN_GARDEN; DAWN; LIT |
| 5 | INT. ARMY TRUCK, CARGO BED (MOVING) - NIGHT / CONTINUOUS | LOC_ARMY_TRUCK (the view out: LOC_CAIRO_FLYOVER) | NIGHT; flyover BLACKOUT_ROLLING → BLACKOUT_FULL |
| 5 | INT. ARMY TRUCK, CAB (MOVING) - CONTINUOUS | LOC_ARMY_TRUCK/CAB | NIGHT |
| 5 | EXT. NILE CORNICHE, POLICE DOCK - NIGHT | LOC_CORNICHE_DOCK (+ PHONES) | BLACKOUT |
| 5 | EXT. NILE - CONTINUOUS | LOC_NILE | NIGHT |
| 6 | EXT. NILE, SOUTH OF CAIRO - NIGHT | LOC_NILE | NIGHT |
| 6 | INT. POLICE LAUNCH, WHEELHOUSE / EXT. POLICE LAUNCH, AFT DECK | PROP_POLICE_LAUNCH (file 04 §13) over LOC_NILE | NIGHT; aft deck PRE-DAWN = NIGHT → DAWN |
| 6 | EXT. NILE, FISHING GROUNDS - CONTINUOUS | LOC_NILE/FISHING_GROUNDS (+ FELUCCA_FIRE) | NIGHT |
| 6 | EXT. NILE, ISLAND CHANNEL - CONTINUOUS | LOC_NILE/ISLAND | NIGHT |
| 6 | EXT. NILE - DAWN; INT. POLICE LAUNCH, WHEELHOUSE - MORNING | LOC_NILE | DAWN; DAY |
| 6 | EXT. NILE OPPOSITE AMARNA - MIDDAY | LOC_NILE/OPPOSITE_AMARNA (distance: LOC_AMARNA_PLAIN_2033) | MIDDAY_HAZE |
| 6 | (no heading; "toward Asyut, where the gates are open") | LOC_ASYUT_LOCK, optional pass-through | AFTERNOON |
| 7 | EXT. NILE, NORTH OF LUXOR - NIGHT | LOC_NILE | NIGHT |
| 7 | EXT. KARNAK, AVENUE OF RAMS - NIGHT | LOC_KARNAK_RAM_AVENUE | NIGHT |
| 7 | INT. KARNAK, GREAT HYPOSTYLE HALL - NIGHT | LOC_KARNAK_HYPOSTYLE (+ THREADS) | NIGHT |
| 7 | INT. KARNAK, GREAT HYPOSTYLE HALL, THIRD PYLON - CONTINUOUS | LOC_KARNAK_HYPOSTYLE/THIRD_PYLON | NIGHT |
| 7 | EXT. KARNAK, COURT OF THE NINTH PYLON - NIGHT | LOC_KARNAK_NINTH_PYLON | NIGHT_WORK |
| 7 | EXT. KARNAK, BLOCK FIELD - CONTINUOUS | LOC_KARNAK_NINTH_PYLON/BLOCK_FIELD | NIGHT_WORK; DARK (Nour reads by touch) |
| 7 | EXT. KARNAK, PROCESSIONAL WAY - CONTINUOUS | LOC_KARNAK_NINTH_PYLON/PROCESSIONAL_WAY | NIGHT_WORK |
| 7 | INT. KARNAK, GREAT HYPOSTYLE HALL - CONTINUOUS (the midpoint) | LOC_KARNAK_HYPOSTYLE; the pylon face: LOC_KARNAK_RAM_AVENUE | PROJECTION |
| 7 | EXT. KARNAK, RIVER LANDING - NIGHT | LOC_KARNAK_QUAY (route: LOC_KARNAK_RAM_AVENUE/CORNICHE_ROAD) | NIGHT |
| 7 | EXT. NILE, LUXOR - NIGHT | LOC_NILE/LUXOR | NIGHT |
| 8 | EXT. NILE, WEST BANK SHALLOWS - NIGHT | LOC_NILE/WEST_BANK_SHALLOWS | NIGHT |
| 8 | EXT. WEST BANK FIELDS - NIGHT | LOC_WEST_BANK_FIELDS | NIGHT |
| 8 | EXT. VALLEY OF THE KINGS - PRE-DAWN | LOC_VOK (/KIOSKS) | PREDAWN |
| 8 | EXT. KV62, ENTRANCE - CONTINUOUS | LOC_KV62_STAIR | PREDAWN |
| 8 | INT. KV62, BURIAL CHAMBER - CONTINUOUS | LOC_KV62_BURIAL_2033 (+ WALL_BROKEN) | BLACKOUT |
| 8 | INT. KV62, NORTH CORRIDOR - LATER / BEYOND THE RUBBLE - LATER / CONTINUOUS | LOC_KV62_NORTH_CORRIDOR | TORCH; DRILL |
| 8 | INT. KV62, THE HEART CHAMBER - CONTINUOUS | LOC_KV62_HEART_CHAMBER (+ BORE, COLLAPSE) | TORCH → RED → GLOW |
| 8 | INT. KV62, ENTRANCE STAIR - DAY | LOC_KV62_STAIR | MORNING_GLARE |
| 8 | EXT. VALLEY OF THE KINGS - MORNING | LOC_VOK (/RIDGE) | MORNING_GLARE |
| 8 | EXT. VALLEY ROAD - CONTINUOUS | LOC_VOK/VALLEY_ROAD | MORNING_GLARE |
| 8 | EXT. NILE - DAY | LOC_NILE | DAY |
| 9 | EXT. NILE, LUXOR EAST BANK - DAY | LOC_NILE/LUXOR | DAY |
| 9 | EXT. LUXOR RAILWAY YARD - DAY / CONTINUOUS | LOC_LUXOR_RAIL_YARD | DAY |
| 9 | INT. MAINTENANCE SHED, INSPECTION PIT - CONTINUOUS | LOC_LUXOR_RAIL_YARD/INSPECTION_PIT | DAY |
| 9 | INT. OLD DIESEL, ENGINE ROOM - CONTINUOUS | LOC_LUXOR_RAIL_YARD/ENGINE_ROOM | DAY |
| 9 | EXT. LUXOR RAILWAY YARD - DUSK | LOC_LUXOR_RAIL_YARD | DUSK |
| 9 | EXT. CANE FIELDS, NORTH OF LUXOR (MOVING) - NIGHT | LOC_NIGHT_TRAIN | NIGHT; BLUE |
| 9 | INT. OLD CARRIAGE / INT. DIESEL CAB / EXT. OLD CARRIAGE, ROOF / EXT. COUPLING PLATFORM / INT. OLD DIESEL, ENGINE ROOM (MOVING) | LOC_NIGHT_TRAIN/COACH_INTERIOR, CAB, ROOF, COUPLING, ENGINE_ROOM | NIGHT |
| 9 | EXT. DEIR MAWAS STATION - NIGHT / CONTINUOUS | LOC_DEIR_MAWAS (+ SHABTI_ON_TRACKS) | NIGHT |
| 9 | EXT. CANE FIELD, DEIR MAWAS - NIGHT | LOC_DEIR_MAWAS (+ DERAILED) | NIGHT |
| 9 | EXT. NILE, AMARNA FERRY - NIGHT | LOC_AMARNA_PLAIN_2033/FERRY | NIGHT |
| 9 | EXT. AMARNA, THE GREAT ATEN TEMPLE - NIGHT / CONTINUOUS | LOC_AMARNA_PLAIN_2033/GARDEN | NIGHT |
| 9 | EXT. GREAT ATEN TEMPLE, AKHETATEN - DAY (MEMORY) | LOC_AMARNA_TEMPLE_1336 (/DOORWAY, /ALTAR) | NOON_1336 |
| 9 | EXT. NILE - NIGHT (MEMORY) | LOC_NILE/ANCIENT_1332 | NIGHT + GRADE_1332_NIGHT + GRADE_READ_FROM_GLASS |
| 9 | INT. GREAT PYRAMID, GRAND GALLERY - NIGHT (MEMORY) | LOC_GP_GRAND_GALLERY (+ ANCIENT_1332) | ANCIENT_1332 |
| 9 | INT. THE HALL OF TWO TRUTHS - NIGHT (MEMORY) | LOC_HALL_TWO_TRUTHS | ANCIENT_1332 |
| 9 | EXT. AKHETATEN, ROYAL ROAD - DAY (MEMORY) | LOC_AMARNA_TEMPLE_1336/ROYAL_ROAD_1330 | DAY_1330 |
| 9 | EXT. ABANDONED LIMESTONE QUARRY - DAWN | LOC_QUARRY | DAWN |
| 10 | EXT. ABANDONED LIMESTONE QUARRY - SUNSET | LOC_QUARRY | SUNSET |
| 10 | INT. GEM CONSERVATION CENTRE, MUMMY LAB - DUSK | LOC_GEM_CC/CAPTIVITY | DUSK |
| 10 | EXT. SAQQARA PLATEAU - NIGHT | LOC_SAQQARA (/SERAPEUM_HEAD) | NIGHT |
| 10 | INT. SERAPEUM, LESSER VAULTS - NIGHT | LOC_SERAPEUM_LESSER | TORCH |
| 10 | INT. SERAPEUM, GREATER VAULTS - CONTINUOUS / THE PIT - CONTINUOUS | LOC_SERAPEUM_GREATER (/PIT, + SAND_TRAP) | WORKLIGHTS |
| 10 | INT. GEM GRAND ATRIUM - NIGHT (captivity) | LOC_GEM_ATRIUM/GARDEN | GARDEN |
| 10 | INT. SERAPEUM, GREATER VAULTS - NIGHT (the fight) | LOC_SERAPEUM_GREATER (+ DUST_FIGHT) | TORCH; BLUE |
| 10 | INT. SERAPEUM, SERVICE TUNNEL - NIGHT | LOC_SERAPEUM_SERVICE_TUNNEL | TORCH |
| 10 | EXT. SAQQARA DESERT - SERVICE TUNNEL MOUTH - NIGHT | LOC_SAQQARA/TUNNEL_MOUTH | NIGHT |
| 11 | EXT. DESERT ROAD, SAQQARA TO GIZA (MOVING) - NIGHT | LOC_DESERT_ROAD | NIGHT |
| 11 | INT. GEM GRAND ATRIUM - NIGHT (captivity) | LOC_GEM_ATRIUM/GARDEN | GARDEN |
| 11 | EXT. GIZA PLATEAU, THE WALL OF THE CROW - MIDNIGHT | LOC_GIZA_PLATEAU/WALL_OF_CROW | MIDNIGHT_FORTRESS |
| 11 | EXT. GIZA PLATEAU, KHAFRE'S CAUSEWAY - LATER | LOC_GIZA_PLATEAU/CAUSEWAY | MIDNIGHT_FORTRESS |
| 11 | INT. OSIRIS SHAFT - NIGHT | LOC_OSIRIS_SHAFT (/LEVEL_2, /PUMP; water W0 → W3) | TORCH → FLOOD |
| 11 | INT. OSIRIS SHAFT, SIDE TUNNEL / INT. BUILDERS' CRAWLWAY - CONTINUOUS | LOC_OSIRIS_SHAFT/SIDE_TUNNEL, /CRAWLWAY | TORCH |
| 11 | INT. GREAT PYRAMID, GRAND GALLERY - NIGHT (the door; the climb) | LOC_GP_GRAND_GALLERY (+ THREAD, STONE_SLID); the door: LOC_GP_QC_SHAFT | BLACKOUT_TORCH; INCHWORM |
| 11 | EXT. GREAT PYRAMID, NORTH FACE - NIGHT | LOC_GP_NORTH_FACE | NIGHT |
| 11 | INT. GREAT PYRAMID, SUBTERRANEAN CHAMBER - NIGHT | LOC_GP_SUBTERRANEAN | TORCH |
| 11 | INT. GREAT PYRAMID, DESCENDING PASSAGE - CONTINUOUS | LOC_GP_DESCENDING (the jackal's way in: LOC_GP_MAMUN_TUNNEL) | TORCH |
| 11 | INT. GREAT PYRAMID, PASSAGE ABOVE THE GRAND GALLERY - CONTINUOUS | LOC_GP_PASSAGE_ABOVE | HEART_GLOW |
| 12 | INT. GREAT PYRAMID, HALL OF TWO TRUTHS - CONTINUOUS | LOC_HALL_TWO_TRUTHS (/MOUTH, /BAY; file 02 §13 states) | PRE_HEART → THREE_SOURCE → VERDICT → AMUN |
| 12 | INT. GREAT PYRAMID, GRAND GALLERY - CONTINUOUS (the intercut fight) | LOC_GP_GRAND_GALLERY | FIGHT |
| 12 | MONTAGE - THE WORLD - CONTINUOUS | reuse: LOC_AMARNA_PLAIN_2033/GARDEN, LOC_GEM_ATRIUM/GARDEN, LOC_GIZA_PLATEAU/CAUSEWAY, LOC_STADIUM_GARDEN, LOC_PORT_WAREHOUSE | their night or Garden variants |
| 12 | INT. GREAT PYRAMID, GRAND GALLERY - PRE-DAWN | LOC_GP_GRAND_GALLERY (the exit route: LOC_GP_MAMUN_TUNNEL) | DAWN_EXIT |
| 12 | EXT. GREAT PYRAMID, NORTH FACE - DAWN | LOC_GP_NORTH_FACE | DAWN_0614 |
| 12 | INT. GEM GRAND ATRIUM - MORNING | LOC_GEM_ATRIUM/GARDEN | MORNING |
| 12 | MONTAGE - CONTROL ROOMS - MORNING | LOC_CONTROL_ROOMS | RELIGHT |
| 12 | INT. HOSPITAL, MATERNITY WARD - MORNING | LOC_HOSPITAL_WAKING | MORNING |
| 12 | INT. HEARING ROOM - DAY | LOC_HEARING_ROOM | DAY |
| 12 | EXT. KV21, VALLEY OF THE KINGS - DAY | LOC_VOK/KV21 | DAY |
| 12 | INT. GEM, TUTANKHAMUN GALLERIES - DAY | LOC_GEM_TUT_GALLERIES | DAY |
| 12 | INT. KV62, ANTECHAMBER - SUNSET | LOC_KV62_BURIAL_2033/ANTECHAMBER (+ CODA, CODA_CASE) | SUNSET |

Sets with no scene heading in the current pages, kept for coverage and the bible's route: LOC_KARNAK_SACRED_LAKE, LOC_GP_WELL_SHAFT, LOC_ASYUT_LOCK.

---

## A. PERIOD SETS

## 1. LOC_EMBALMING_1323 — the House of Embalming, Thebes, c. 1323 BC (Seq 1.1)

**Real anchors:**
- The only excavated embalming workshop is later than our date: the Saite–Persian workshop at Saqqara (2018). It is a rectangular mud-brick and limestone building with an adjoining 30 m burial shaft. Its labelled vessels held juniper, cypress and cedar oils, Dead Sea bitumen, animal fats, beeswax, elemi and dammar [05 A3]. Use it only as a texture reference.
- Drying in natron took about 40 days, and the whole rite up to about 70 [05 A2]. Natron is a natural sodium carbonate salt quarried at Wadi Natrun [05 A2].
- Priests wore Anubis masks; a real ceramic example is in Hildesheim [16 §7; bible §6].
- Spell 30B is spoken over the heart [05 A4; 04 §3].
- ⟂ The heart is lowered, still beating, into yellow-green glass.

**Production spec:**
- A long, low mud-brick hall on the West Bank, about 12 × 5 m and 3 m to the beams.
- Whitewashed walls, soot-dark above the lamp niches; palm-log beams under reed matting; a packed-earth floor strewn with clean sand.
- A low limestone table, draped in linen, stands across the room.
- Shelving of mud-brick and palm-rib holds clay jars sealed with linen and clay. There are baskets of natron (white crystals), stacks of folded linen, and bronze tools laid on linen.
- Clay saucer lamps with twisted-linen wicks sit in the wall niches; one torch stands by the door, which is screened with hanging linen.
- The walls are **plain**: no hieroglyph-covered walls.

**LONG:** a long, low ancient Egyptian mud-brick workshop, whitewashed walls darkened with soot above small wall niches holding clay oil lamps, palm-log ceiling beams over reed matting, a packed-earth floor strewn with clean sand, a low limestone table draped in linen at its centre, shelves of clay jars sealed with linen, stacked folded linen and baskets of white salt crystals

**SHORT:** a low ancient mud-brick embalming workshop with soot-darkened whitewashed walls, oil lamps in niches, a linen-draped limestone table and sealed clay jars

**Lighting variants:**
- `LOC_EMBALMING_1323_NIGHT`: `lit only by small flickering clay oil lamps in the wall niches and one torch by the door: deep amber firelight on linen and skin, cool lapis-blue shadows, a faint haze of lamp smoke` + GRADE_1323
- `LOC_EMBALMING_1323_NIGHT_LOW` (the pulse; the embalmer recoils): `the lamps guttering low, most of the room sunk in blue-black shadow, one lamp close to the table`
- There is no day or emergency variant; the scene is only at night.

**State add-ons:**
- `a slight figure lying on the table under white linen drawn up to the collarbones, the face turned away into shadow` (bible §3.4; never more exposed than this)
- The vessel and its pulse come from PROP_HEART_VESSEL V-1323.

**Geography lock:** the table runs across frame. The embalmer in the jackal mask works with his back to camera. The door with its linen screen is at frame right; the lamp niches are on the back wall.

**Never:** coffins or sarcophagi in this room; walls covered in carving; gold everywhere; cobwebs; horror-film instruments; any visible incision or organ.

**PLATE — establishing, 16:9:**
Cinematic still of the interior of a long, low ancient Egyptian mud-brick workshop at night, around 1300 BC, with no people. Whitewashed walls are darkened with soot above small niches holding clay oil lamps with tiny flames. Palm-log beams and reed matting form the ceiling, and the packed-earth floor is strewn with clean sand. A low limestone table draped in white linen stands across the room. Shelves hold clay jars sealed with linen and clay; folded linen is stacked beside reed baskets of white salt crystals. Deep amber lamplight, cool lapis-blue shadows, faint lamp smoke. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 2. LOC_KV62_BURIAL_1323 — the KV62 burial chamber, freshly painted, c. 1323 BC (Seq 1.2)

**Real anchors:**
- The burial chamber measures **6.4 × 4.0 m**. It is the only decorated room of a tomb of about 110 m² in total: an entrance stair and corridor, then the antechamber (7.9 × 3.6 m) with the Annexe, then the burial chamber, then the Treasury (about 4 × 3.6 m) [01 §14]. Ceiling height is about 3.6 m [verify].
- **North wall** [09 §5.2; 04 §2]: "a three-act narrative arranged to be read from right to left."
  - First scene (on the right): Ay, in the leopard-skin robe of a sem-priest, performs the Opening of the Mouth on the mummiform king with the adze.
  - Middle: the king is greeted by Nut.
  - Left: the king, followed by his ka, is embraced by Osiris.
  - It is the only royal tomb that shows the rite performed on the king.
  - The captions are name-labels only (COMP if read).
- Other walls [verify against the Theban Mapping Project and Getty publications]:
  - east wall: the funeral procession hauling the catafalque;
  - west wall: the twelve baboons of the Amduat's first hour;
  - south wall: the king with Hathor, Anubis and Isis.
- The painted ground is a warm golden yellow [verify]. The figures show late Amarna proportions.
- The sarcophagus is quartzite with a granite lid painted to match [verify]. The **wreath** lay on the brow of the second coffin, over the cobra and vulture [01 §10].
- The chamber was sealed by a plastered blocking wall bearing the necropolis seal, a jackal over nine captives [01 §21].
- ⟂ **The north wall hides a rubble-packed corridor.** The painter adds the painted king's eye last.

**Production spec:**
- **Staging choice:** the four gilded shrines are not yet assembled. Their panels lean stacked against the east wall, so that the sarcophagus is reachable for the wreath and the adze. The real order of works is uncertain; flag it.
- The **sealed opening** lies behind the right-hand scene. The painted king's eye (about 2.1 m above the floor) marks the top edge of the fresh plaster patch.

**LONG:** a small rock-cut burial chamber about six by four metres, its plastered walls freshly painted on a warm golden-yellow ground with large flat figures in red-brown, black, white and blue, one long wall showing a priest in a leopard skin touching an adze to a wrapped royal figure; a massive rectangular quartzite sarcophagus fills the centre; gilded wooden shrine panels stand stacked against a wall

**SHORT:** a small rock-cut burial chamber with freshly painted golden-yellow walls of large flat figures, a massive quartzite sarcophagus at its centre

**Lighting variants:**
- `LOC_KV62_BURIAL_1323_NIGHT`: `lit by a few clay oil lamps on the floor and two torches held by attendants: amber firelight flickering across the painted yellow walls, deep lapis-blue shadows in the corners, a faint soot haze` + GRADE_1323
- `LOC_KV62_BURIAL_1323_LAMP_CLOSE` (the painter, the eye): `a single oil lamp held close to the painted wall, a warm circle of light on wet colour, everything else in darkness`

**State add-ons:**
- `NORTH_WALL_FRESH`: `the lower right of the far painted wall still damp, a patch of fresh pale plaster sealing an opening beneath the painted figures`
- `COFFIN`: `a gilded coffin lying closed inside the open sarcophagus, a small wreath of blue cornflowers and olive leaves on its brow`
- `RUBBLE`: `limestone rubble and baskets stacked by the far wall, a dark opening behind` (the moment before sealing)

**Geography lock:** we enter from the antechamber (south). The painted north wall faces camera. The Treasury doorway is at frame right (east) [verify]. Attendants hold their torches at frame left, so the key comes from the left.

**Never:** electric light; glass; a modern floor; faded or spotted paint (that is the 2033 look); legible hieroglyphs; a king's face in close-up on the wall (the painting reads at a distance).

**PLATE — establishing, 16:9:**
Cinematic still inside a small ancient Egyptian rock-cut burial chamber around 1300 BC, newly finished, with no people. The plastered walls are painted on a warm golden-yellow ground with large flat figures in red-brown, black, white and blue. On the far wall a priest in a leopard skin touches a small adze to the face of a white-wrapped royal figure, the colours bright and fresh. A massive rectangular sarcophagus of yellow-brown quartzite fills the centre of the room, and gilded wooden shrine panels lean stacked against a side wall. Clay oil lamps on the floor throw flickering amber light; deep blue-black shadows fill the corners. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 3. LOC_KV15_LAB_1925 — KV15, the outer corridor used as a laboratory, 11 November 1925 (Seq 1.3)

**Real anchors [01 §3]:**
- The autopsy began at **9:45 am, 11 Nov 1925**, in the **outer corridor of KV15** (Seti II's tomb), which was used as the lab.
- Present: the anatomists Derry and Saleh Bey Hamdi, under the Antiquities Service, with Egyptian officials; Lacau, Lucas and the photographer Burton.
- The body was fused to the innermost coffin by hardened resin. The coffins had been set in the sun to soften it, which failed; heated knives were then used.
- About 150 objects lay in 17 layers of linen. **No heart scarab** was found [01 §18].
- The dismemberment is documented only in Burton's photographs [01 §3]. The film never shows the cut, and never reproduces the photographs (bible §14.7).
- KV15's corridor walls carry unfinished decoration, some carved and some only drawn in outline [verify]. Whether the corridor had electric light in 1925 is [verify]; the production choice is kerosene lanterns plus daylight from the entrance.

**Production spec:** a long, straight corridor about 2.6 m wide and 3.5 m high, sloping gently down away from the entrance [verify dimensions]. It holds:
- a long wooden trestle table covered in white cloth;
- wooden packing crates, white enamel basins, and steel instruments laid in rows on linen;
- a small paraffin stove heating knives (heat shimmer, never the blade at work);
- Burton's camera on its tripod (PROP_BURTON_PLATES);
- Ibrahim's brass lantern (PROP_LAMP_1925).

**LONG:** the long, straight, gently sloping entrance corridor of an ancient rock-cut royal tomb in 1925, used as a laboratory: pale limestone walls carved with faint, unfinished figures in outline, a long wooden trestle table covered in white cloth, wooden packing crates, enamel basins, steel instruments laid in rows on linen, kerosene lanterns hung on iron hooks

**SHORT:** a sloping rock-cut tomb corridor in 1925 used as a laboratory, a white-draped trestle table, crates, enamel basins and instruments on linen

**Lighting variants:**
- `LOC_KV15_LAB_1925_DAY`: `a hard shaft of white desert daylight falling down the corridor from the entrance at upper right, warm kerosene lamplight on faces, heat shimmer rising above hot steel` + GRADE_1925
- `LOC_KV15_LAB_1925_FLASH`: `a single hard white burst of a photographer's flash filling the corridor` (1–2 frames; the match cut to 2033 is COMP)
- `LOC_KV15_LAB_1925_TREMBLE`: `the hand-held lantern trembling, its amber light swinging across the rock walls`

**Geography lock:** the entrance and its daylight are up the slope at frame right. The table runs along the corridor axis. Ibrahim and his lamp stand at the head of the table (frame left). Burton's camera stands at the foot of the table (frame right, near the entrance).

**Never:** the body in frame beyond a shape under cloth at the table's edge; blood; saws; the photographs' content; modern objects.

**PLATE — establishing, 16:9:**
Cinematic period still, November 1925: the long, straight, gently sloping entrance corridor of an ancient rock-cut tomb in a desert valley, used as a makeshift laboratory, with no people. Pale limestone walls carry faint, unfinished carved figures in outline. A long wooden trestle table covered in white cloth runs along the corridor, with wooden packing crates, white enamel basins and steel instruments laid in rows on linen beside it. Kerosene lanterns hang on iron hooks. A hard shaft of daylight falls from the entrance at the upper right, dust glowing in it. Sepia-toned silver-gelatin look, heavy fine grain. Photoreal live-action film still, anamorphic 40mm. Aspect ratio 16:9.

---

## 4. LOC_XRAY_1968 — the Liverpool X-ray reading room, 1968 (Seq 1.4)

**Real anchors:**
- Harrison's 1968 X-rays first showed that the sternum and front ribs are missing [01 §5].
- The films were taken in the tomb with a portable machine [verify]. The film's insert is the later reading of them in a Liverpool room.
- The radiologist is generic, never a likeness (bible §7, 1.4).

**Production rule:** the films on the lightbox are **COMP**: a new, generic, non-diagnostic chest silhouette. They never reproduce or approximate the real radiographs. In the plate, the films read as "dark films with faint pale shapes".

**LONG:** a small 1960s hospital radiology reading room, pale green painted walls, a row of wall-mounted X-ray lightboxes glowing flat white with dark films clipped to them, a steel desk with a black telephone, an ashtray and scattered manila folders, a single flickering fluorescent tube overhead

**SHORT:** a small 1960s radiology reading room with pale green walls, glowing wall lightboxes holding dark X-ray films, a steel desk

**Lighting variants:**
- `LOC_XRAY_1968_NIGHT`: `cold flickering fluorescent light and the flat white glow of the lightboxes, a pale green-grey cast, deep shadows under the desk` + GRADE_1968

**Geography lock:** the lightboxes are on the wall facing camera. The radiologist stands at frame left and traces with a pen; the assistant is at frame right.

**PLATE — establishing, 16:9:**
Cinematic period still of a small 1960s hospital radiology reading room at night, with no people. Pale green painted walls; a row of wall-mounted X-ray lightboxes glowing flat white, dark films with faint pale shapes clipped to them; a grey steel desk with a black rotary telephone, a glass ashtray and scattered manila folders. A single fluorescent tube flickers overhead. Cold green-grey institutional light, deep shadows under the desk. Photoreal live-action film still, anamorphic 40mm, fine 16mm-style grain. Aspect ratio 16:9.

---

## 5. LOC_CAIRO_MUSEUM_1939 — a Cairo Museum gallery, the 16 April 1939 broadcast (Seq 4.2, SESHAT's flourish)

**Real anchors:**
- 16 Apr 1939: the BBC broadcast from the Cairo Museum. The power failed five minutes before air, and the trumpet was played by candlelight. An estimated 150 million people listened. The silver trumpet had cracked earlier, at a 1939 rehearsal [01 §11].
- The Egyptian Museum on Tahrir is a neoclassical building (1897–1902, designed by Marcel Dourgnon), opened 15 Nov 1902 [14 §3].
- The broadcaster is never named in prompts. The film uses a re-recorded note (bible §2 Layer 4).

**Production spec:** a lofty gallery with pale plastered walls and tall pilasters, dark wooden display cases with glass tops [verify the period case design], and stone statues along the walls. A 1930s ribbon microphone stands on a heavy stand trailing cloth-covered cables, next to a small table crowded with lit candles. The bandsman and the engineer are CHAR_BANDSMAN_1939 and CHAR_RADIO_ENGINEER_1939.

**LONG:** a lofty neoclassical museum gallery in 1939, pale plastered walls and tall pilasters rising into darkness, rows of dark wooden display cases with glass tops, stone statues at the edges, a 1930s broadcast microphone on a heavy stand trailing thick cloth cables, a small table crowded with lit candles

**SHORT:** a lofty 1939 neoclassical museum gallery lit by candles, dark wooden glass-topped cases, a 1930s broadcast microphone on a stand

**Lighting variants:**
- `LOC_CAIRO_MUSEUM_1939_CANDLE`: `candlelight only: a warm pool of light around the microphone and the candles, the gallery falling away into black, near-monochrome warm tones` + GRADE_1939

**PLATE — establishing, 16:9:**
Cinematic period still of a lofty neoclassical museum gallery in 1939 during a power cut, with no people. Pale plastered walls and tall pilasters rise into darkness above rows of dark wooden display cases with glass tops; pale stone statues stand at the edges. In the centre, a 1930s broadcast microphone on a heavy stand trails thick cloth-covered cables beside a small table crowded with lit candles, their warm pool of light the only illumination. Near-monochrome warm tones, like a 1930s newsreel warmed by candle flame. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## 6. LOC_AMARNA_TEMPLE_1336 — the Great Aten Temple, c. 1336 BC (and the night of c. 1332 BC) (Seq 9.5)

**Real anchors [02 §3–4]:**
- The Great Aten Temple lay in a brick enclosure of about **800 × 300 m** (some sources say 900 × 300).
- It had two stone buildings: the Gem-Aten at the front and the Sanctuary about 300 m behind.
- It was **open to the sky** and packed with offering tables. One reconstruction has 40 rows of 20 tables on each side of the Gem-Aten.
- The Aten is drawn as a disk whose rays end in hands; those nearest the king and queen hold the ankh to their nostrils [02 §4].
- Egyptian temple gateways flew tall flagstaffs with pennants [verify for Amarna].
- ⟂ The woken ninth core above the high altar is UNIT_ATEN_AMARNA (file 02 §11). Sleep is given at the tables.
- The city core ran 6–7 km along the east bank on a north–south "Royal Road" [02 §3]. The court left Amarna around the king's regnal year 3, when he was about 11 and changed his name [01 §1; bible §2 Layer 2]. That exodus is the Royal Road memory (9.5c).

**Production spec:**
- A court of white limestone and whitewashed mud-brick.
- Offering tables about 1 m square and waist-high, of limestone and mud-brick, in straight rows, heaped with bread, fruit, cornflowers and blue lotus.
- Gateway towers with cedar flagstaffs flying long pale pennants.
- A raised high altar with steps; the four gilded masts of the Aten (file 02).
- Painted relief of the royal family under the rayed disk on the gateway faces (illegible at distance).
- Child Tutankhaten watches from **a shadowed side doorway**.
- Sleepers are **adults** in white pleated linen (CHAR_AMARNA_SLEEPERS_1336).

**LONG:** a vast open-air ancient temple court of white limestone and whitewashed mud-brick under an open sky, hundreds of low square offering tables standing in straight rows to the far end, heaped with bread, fruit and blue flowers; tall gateway towers hung with long pale pennants on cedar masts; a raised high altar with steps at the centre

**SHORT:** a vast open-air ancient temple court of white limestone, hundreds of offering tables in straight rows, a raised altar at its centre

**Lighting variants:**
- `LOC_AMARNA_TEMPLE_1336_NOON_1336`: `blinding midday sun: bleached white-gold light, hard short shadows, highlights blooming to white, heat shimmer over the rows of tables` + GRADE_1336 + GRADE_READ_FROM_GLASS (post)
- `LOC_AMARNA_TEMPLE_1336_DAY_1330` (the Royal Road, c. 1330 BC): `plain, hard afternoon sun, dust in the air, the white-gold glare gone flat and tired` + GRADE_1336 + GRADE_READ_FROM_GLASS (post)
- `LOC_AMARNA_TEMPLE_1336_NIGHT_1332` (the disk taken down): `night: torches on poles and oil lamps on the altar steps, warm gold on white stone, a deep blue-black sky, the court almost empty` + GRADE_1332_NIGHT + GRADE_READ_FROM_GLASS (post)

**Area add-ons:**
- `DOORWAY`: `seen from a shadowed doorway in the side wall, looking out into the blazing court`
- `ALTAR`: `at the foot of the high altar steps, beneath the great disk`
- `ROYAL_ROAD_1330` (9.5c, c. 1330 BC, the court leaving): `on a broad, straight processional road through a city of whitewashed mud-brick houses and walled gardens, loaded ox-carts and people on foot moving away in a long file, dust hanging in the hard sunlight`

**Flags:** `VFX-EXTEND` for the full court of sleepers. The Aten is a 3D asset (file 02 §11).

**Never:** children among the sleepers (the princesses are small linen-covered forms far in the background, and the hands never touch them); Hollywood-epic gold costumes; stylised Amarna sculpture proportions on real people.

**PLATE — establishing, 16:9:**
Cinematic wide still of a vast ancient open-air temple court of white limestone and whitewashed mud-brick under a blazing midday sun, around 1340 BC. Hundreds of low square offering tables stand in straight rows receding into shimmering heat, heaped with bread, fruit and blue cornflowers. Tall gateway towers carved with faint weathered relief fly long pale pennants on cedar masts. At the centre, a raised high altar with steps stands empty under the sky. Blinding white-gold light, hard short shadows, highlights blooming. No people. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## B. THE GRAND EGYPTIAN MUSEUM, 2033

**Real anchors for the whole complex [07 E5; 14 §5; 01 §15]:**
- **Architecture:** designed by Heneghan Peng (competition 2002–03), built from 2005. It stands on a site of about 50 ha, **2 km north-west of the pyramids**. The building is a chamfered triangle whose north and south walls line up with the pyramids of Khufu and Menkaure. It has a translucent alabaster façade, a huge atrium and a grand staircase of statues.
- **Opening:** the Conservation Centre opened in 2010; the museum officially opened on 1 Nov 2025.
- **Conservation Centre (GEM-CC):** west of the museum, linked to it by **a tunnel about 200 m long**. It has **19 labs**, including mummies and human remains, wood, stone, wall paintings and metals, plus preventive conservation and scientific documentation, and **six storage rooms** under controlled conditions.
- **Undocumented:** the GEM's security and HVAC design [14 §5 NOT FOUND]. Every interior detail below that is not cited is **production spec**.
- ⟂ In reality the mummy stays in KV62 [01 §15]; in the film the OSIRIS protocol moved it here.
- **Prompt rule:** never write "Grand Egyptian Museum" or "GEM" in a prompt. Write "a vast modern museum".

## 7. LOC_GEM_CC — the Conservation Centre: the mummy lab and its areas (Seq 1.5, 2, 3, the Council, Nour's captivity)

**Production spec:**
- **The mummy lab (the OSIRIS lab):** a double-height clean lab about 14 × 10 m and 7 m high, with a seamless white epoxy floor and white wall panels.
  - At its centre, a low titanium examination cradle on a plinth.
  - Overhead, a ring gantry carrying projectors and cameras. The projection of the cut map is PROP_CUTMAP_PROJECTION.
  - Stainless-steel trolleys; sealed glass climate cases along the walls.
  - A full-height glass wall with the observation room behind it.
- **Tut's bay:** a glass-walled patient room off the lab, with a hospital-style bed, one chair and the tall mirror of Seq 2.1.
- **Imaging lab:** a dark room of large black wall screens (all COMP) and a copy stand under a hard spotlight.
- **The sealed bay:** a frosted-glass door with a reader showing a small red light. It carries no text.
- **Corridor:** long and white, lined with glass lab windows.

**LONG:** a large, double-height modern conservation laboratory, seamless white epoxy floor and white wall panels, a low titanium examination cradle on a plinth at its centre beneath a ring-shaped overhead gantry of projectors and cameras, stainless-steel trolleys and sealed glass climate cases along the walls, and one full-height glass observation wall with a darker room behind it

**SHORT:** a double-height white conservation laboratory with a titanium examination cradle under a ring of projectors and a full-height glass observation wall

**Area add-ons:**
- `TUT_BAY`: `inside a smaller glass-walled patient bay off the laboratory, a hospital-style bed with white linen, one chair and a tall mirror on a stand`
- `OBSERVATION`: `in the dim observation room behind the glass wall, a long desk of dark screens facing the bright laboratory`
- `IMAGING`: `in a darkened imaging lab of large black wall screens and a copy stand under a single hard spotlight`
- `SEALED_BAY`: `at a frosted glass door with a small red light glowing on its reader, the sealed bay beyond`
- `CORRIDOR`: `in a long white corridor lined with glass laboratory windows`
- `CAPTIVITY` (Seq 10–12 intercuts): `the laboratory hushed and half lit, a single folding cot and a chair near the glass wall`

**Lighting variants:**
- `LOC_GEM_CC_NIGHT`: `clean cool-white LED panels overhead, soft and even, precise white spotlights on the cradle, polished reflections in the glass` + GRADE_2033_MUSEUM
- `LOC_GEM_CC_READING` (1.5, the resurrection): `the room lights dimmed low, the cradle lit from above by projected pale-cyan light from the gantry, faces behind the glass in shadow`
- `LOC_GEM_CC_EMERG` (after the takeover): `main lights off, sparse battery emergency downlights in cool white, the green glow of exit pictograms, long black shadows`
- `LOC_GEM_CC_DUSK` (captivity): `low evening light through a high clerestory window, the ceiling LEDs at a quarter, warm-cool contrast`
- `LOC_GEM_CC_DAY` (Seq 2–3: the Readings, the imaging lab by day, the Council's late afternoon): `soft daylight from a high clerestory window blended with clean cool-white LED panels, bright and even, a faint warm edge of sun on the floor` + GRADE_2033_MUSEUM

**Geography lock:** from the foot of the cradle, the glass observation wall is at frame right, the door to Tut's bay is at back left, and the tunnel door is behind camera.

**Never:** a detached body part in frame; body exposure beyond the sheet line at the collarbones (bible §3.4); readable screen text; hospital-horror lighting.

**PLATE — establishing, 16:9:**
Cinematic still of a large, double-height modern conservation laboratory at night, with no people. It has a seamless white epoxy floor and white wall panels. At its centre, a low titanium examination cradle on a plinth sits beneath a ring-shaped overhead gantry of small projectors and cameras. Stainless-steel trolleys and sealed glass climate cases line the walls, and at the right a full-height glass observation wall reflects the room, a darker room with a desk of screens behind it. Clean cool-white LED light, precise spotlights on the cradle, polished reflections. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 8. LOC_GEM_PLANT_ROOM — the plant room and the ATEN-1 feed breaker (Seq 3.6)

**Production spec:** an electrical switchroom under the Conservation Centre. Rows of grey steel switchgear cabinets with dark indicator lamps; overhead cable trays; a painted concrete floor with safety lines. At the far end stands the main breaker panel with a heavy red lever. **No labels are legible.**

**LONG:** a long electrical plant room under a museum complex, rows of grey steel switchgear cabinets with dark indicator lamps, overhead cable trays bundled with thick black cables, a painted grey concrete floor with safety lines, and at the far end a large main breaker panel with a heavy red lever

**SHORT:** a long museum plant room of grey steel switchgear cabinets and overhead cable trays, a main breaker with a heavy red lever

**Lighting variants:**
- `LOC_GEM_PLANT_ROOM_NIGHT`: `hard white overhead strip lights, flat and industrial, a green-grey cast on the steel`
- `LOC_GEM_PLANT_ROOM_EMERG`: `strip lights off, red-orange emergency lamps and small green indicator glints, deep shadow between the cabinets`

**Safety:** Rami's wrist is taken with minimum force; the fingers break off screen (a crack and a cradled hand; bible §3.3).

**PLATE — establishing, 16:9:**
Cinematic still of a long electrical plant room beneath a modern building, with no people. Rows of grey steel switchgear cabinets with dark indicator lamps line both sides; overhead cable trays carry thick bundled black cables; the painted grey concrete floor has pale safety lines. At the far end, a large main breaker panel has a heavy red lever. Hard white overhead strip light, flat and industrial. No legible labels. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 9. LOC_GEM_TUNNEL — the 200 m Conservation Centre tunnel (Seq 3.2 the Pectoral Walk; 4.4 the escape)

**Real anchor:** a tunnel about 200 m long connects the Conservation Centre to the museum [14 §5]. Its design is undocumented, so the look is production spec: straight, 6 m wide and 4 m high for moving artefacts, with white-painted concrete, a grey epoxy floor with a pale centre stripe, one continuous ceiling line of LED light, steel fire-shutter frames every 50 m, service pipes and small black dome cameras.

**LONG:** a long, straight underground service tunnel about two hundred metres long and six metres wide, smooth white-painted concrete walls, a grey epoxy floor with a pale guide stripe down the centre, one continuous line of LED light along the ceiling vanishing to a point, steel fire-shutter frames at intervals and small black dome cameras

**SHORT:** a long straight white underground service tunnel, grey floor with a centre stripe, a single ceiling line of LED light vanishing to a point

**Lighting variants:**
- `LOC_GEM_TUNNEL_NIGHT` (3.2): `the ceiling line of LED at half brightness, cool white, long soft reflections running down the floor` + GRADE_2033_MUSEUM
- `LOC_GEM_TUNNEL_EMERG` (4.4): `the ceiling line dead; battery emergency lamps every twenty metres casting cool white pools, a green exit glow, black gaps between`

**State add-ons:**
- `POLICE_LINE` (3.2): `a line of uniformed police officers standing shoulder to shoulder across the tunnel` (the officers are CHAR_POLICE_LINE and CHAR_YOUNG_OFFICER, file 01 §10b)
- `SHUTTER`: `a steel fire shutter half lowered across the tunnel`

**Geography lock:** the museum and galleries end is **frame left**, the Conservation Centre end **frame right**. The Pectoral Walk and the Seq 4.4 escape both move **left to right**. The Pectoral Walk is an EXTEND chain with hidden cuts on bodies and shutter frames crossing the lens (file 05 §8).

**PLATE — establishing, 16:9:**
Cinematic still down a long, straight underground service tunnel about two hundred metres long and six metres wide, with no people. Smooth white-painted concrete walls; a grey epoxy floor with a pale guide stripe down the centre; one continuous line of cool LED light along the ceiling vanishing to a point; steel fire-shutter frames at regular intervals and small black dome cameras. Cool white light at half brightness, long soft reflections on the floor. One-point perspective, eerie symmetry. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 10. LOC_GEM_TUT_GALLERIES — the Tutankhamun galleries (Seq 2.4 Layla meets Tut; 3.2 the pectoral lifted; 4.4 the cases smashed)

**Real anchors:**
- Two of the GEM's twelve halls, about 7,000–7,500 m² [14 §5; 01 §15].
- All **5,398 objects** from KV62 are shown together for the first time.
- They are arranged along "two opposing pathways": a chronological journey through his life and reign, and a forensic exploration of the tomb and excavation [14 §5].
- The objects include:
  - the four gilded shrines; the outermost carries the earliest partial copy of the Book of the Heavenly Cow [04 §8];
  - about 130 walking sticks [01 §6];
  - the trumpets [01 §11];
  - the dagger (JE 61585) and the pectoral (JE 61884) [01 §12–13];
  - the footstool and sandals carrying the Nine Bows [09 T10].
- The outermost shrine measures about 5.1 × 3.3 × 2.75 m [verify].
- The wall colours and lighting design are [verify]. The production choice is charcoal walls with the cases lit from within.

**LONG:** a vast, dark modern museum hall with charcoal walls and a high black ceiling, lit only by glowing glass display cases holding gilded ancient treasures: golden shrines, chariots, jewellery, walking sticks and statues in long rows; a huge gilded wooden shrine stands in its own tall glass enclosure on the central axis, the polished stone floor reflecting every case

**SHORT:** a vast dark museum hall of charcoal walls lit only by glowing glass cases of gilded ancient treasures, a huge gilded shrine on the axis

**Lighting variants:**
- `LOC_GEM_TUT_GALLERIES_NIGHT`: `after hours: only the cases glow, warm gold light inside the glass, cool blue-black between them, deep reflections in the polished floor` + GRADE_2033_MUSEUM
- `LOC_GEM_TUT_GALLERIES_DAY`: `open hours: a soft cool overhead wash plus the warm case lights, even and clean`
- `LOC_GEM_TUT_GALLERIES_EMERG` (4.4): `case lights dead; sparse cool emergency downlights, a green exit glow, gilded surfaces catching torch beams`

**State add-ons:**
- `CASES_SMASHED` (4.4, VFX-ASSIST): `two tall glass cases smashed open, glass shards scattered across the polished floor`
- `EMPTY_CASE` (3.2 on): `one small case standing open and empty on a pale plinth, a single spotlight on nothing`
- `SHABTI_CASE` (2.4, the roster; added by the cross-check): `before a tall glass case holding rank upon rank of small mummiform funerary figurines in wood and blue faience, hundreds of them in tight rows`
- `THRONE` (2.4, where Layla lies with her stencil; added by the cross-check): `at the foot of a gilded ancient throne in its own glass case, a low bench and the polished floor before it`

**Geography lock:** the great shrine sits on the central axis. The walk toward the tunnel runs from frame right to frame left in the galleries, so that it continues left to right once inside the tunnel: the turn happens at the tunnel door. Layla's scene (2.4) is at a bench facing a case at frame left.

**PLATE — establishing, 16:9:**
Cinematic still of a vast, dark modern museum hall after hours, with no people. Charcoal walls and a high black ceiling; the only light comes from glowing glass display cases holding gilded ancient treasures: small golden shrines, chariots, jewellery, rows of walking sticks and statues. On the central axis, a huge gilded wooden shrine stands in its own tall glass enclosure. The polished stone floor reflects every case. Warm gold inside the glass, cool blue-black between. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 11. LOC_GEM_ATRIUM — the Grand Atrium, the colossus and the Grand Staircase (Seq 4 GEM Night; the Garden; captivity; 12.8 the waking)

**Real anchors:**
- The **red-granite colossus of Ramesses II**, about **83 t** [07 E5] (82 t in [14 §5]), comes from Mit Rahina (Memphis). It was moved from Ramses Square in 2006 and into the atrium in January 2018 [07 E5; dates MEMORY].
- The statue is about 11 m tall [verify] and stands "under a six-storey void" [14 §5].
- The **Grand Staircase** is lined with statues [07 E5]. Its count, and the panoramic window framing the pyramids at the top, are [verify].
- The bible places the pyramids "framed in the glass wall" (§7, 4.1). The exact glazing geometry is [verify]; the lock uses a triangulated glass wall as production spec.
- In prompts the statue is "an eleven-metre ancient red-granite statue of a striding king", never named.

**LONG:** a colossal modern museum atrium of pale stone and glass, six storeys high, with a vast triangulated glass wall; at its centre, on a low plinth, stands an eleven-metre ancient red-granite statue of a striding king; a monumental staircase lined with ancient statues climbs away to one side, and through the glass the distant pyramids

**SHORT:** a colossal six-storey museum atrium of pale stone and glass, an eleven-metre red-granite statue of a striding king at its centre

**Area add-ons:**
- `GALA` (4.1): `set for a night gala: round tables with white cloths, a low stage and lectern at the statue's feet, guests in evening dress`
- `GARDEN` (4.3 onward): `the floor around the statue's base covered in rows of sleeping adults on white mats under pale blankets, clear water carafes between them`
- `STAIRCASE`: `on the monumental staircase, ancient statues standing on every landing`
- `SERVICE_STAIRWELL` (4): `in a bare concrete service stairwell behind the atrium, steel handrails and painted landings`

**Lighting variants:**
- `LOC_GEM_ATRIUM_GALA`: `warm gala light: low amber uplights on the statue, pools of soft warm light on the tables, the distant pyramids floodlit gold beyond the glass`
- `LOC_GEM_ATRIUM_BLACKOUT` (4.2): `every light dead at once: near black, the pale shapes of the glass wall against the night, amber light-slits brightening one by one across the floor`
- `LOC_GEM_ATRIUM_GARDEN` (4.3 onward, captivity): `soft, shadowless white light as if through white fabric, low and calm, the statue pale and serene` + GRADE_GARDEN
- `LOC_GEM_ATRIUM_EMERG`: `sparse battery emergency downlights in cool white, a green exit glow, the statue a dark mass above`
- `LOC_GEM_ATRIUM_MORNING` (12.8): `clear morning daylight flooding through the glass wall, cool and clean, dust motes in the beams, the pyramids sharp in the distance` + GRADE_2033_DAY

**Geography lock (the master from the entrance):**
- the colossus faces camera;
- the Grand Staircase rises at **frame right**;
- the glass wall with the pyramids is at **frame left**;
- Layla sleeps at the foot of the statue's plinth, frame left of its base (the approved master image).
- The gala lectern stands between the statue's feet and camera.

**Never:** a child in any Garden plate except the approved Layla master; robots touching sleepers' faces; the minister's face in close-up (wides only, file 01).

**PLATE — establishing, 16:9:**
Cinematic wide still of a colossal modern museum atrium at night, six storeys high, built of pale stone and glass, with no people. At its centre, on a low plinth, stands an eleven-metre ancient red-granite statue of a striding king, lit warmly from below. At the right, a monumental staircase lined with ancient statues climbs into the upper levels. At the left, a vast triangulated glass wall shows the distant pyramids floodlit gold on the dark horizon. Polished pale floor, deep soft shadows. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 12. LOC_GEM_BOAT_HALL — the hall of the cedar ship (Seq 4.4, the escape route)

**Real anchors [07 C3; 14 §5]:**
- The first Khufu ship was found in 1954 in a sealed pit south of the Great Pyramid: 1,224 pieces of Lebanese cedar in 13 layers.
- Haj Ahmed Youssef Moustafa reassembled it over years. It is built shell-first with no keel, its planks lashed with halfa grass.
- It is **43.4–43.6 m long, 5.9 m wide and 1.78 m deep**, and weighs about 20 t.
- In August 2021 it was moved 7.5 km, intact, to the GEM on a remote-controlled cart (10 hours).
- The second boat is being reassembled at the GEM.
- In the film, Tut appraises it "like a boatman" (bible 4.4).

**Production spec:** a long, dim, high hall. The ship rests on a low steel cradle, seen from a raised walkway with a glass balustrade that runs its whole length. Warm spotlights fall on the cedar. It has papyrus-bundle-shaped ends, a deckhouse amidships and its oars laid along the sides [verify the oar count].

**LONG:** a long, dim, high exhibition hall built around a single ancient ship: a slender forty-three-metre cedar-wood vessel with a high curved prow and stern shaped like papyrus bundles, a deckhouse amidships and long oars laid along its sides, resting on a low steel cradle, with a raised walkway and glass balustrade running its full length

**SHORT:** a long dim hall around a slender forty-three-metre ancient cedar ship with papyrus-shaped prow and stern, a raised walkway along its length

**Lighting variants:**
- `LOC_GEM_BOAT_HALL_NIGHT`: `warm spotlights raking the honey-brown cedar, the hall black around the ship, soft reflections in the glass balustrade`
- `LOC_GEM_BOAT_HALL_EMERG`: `spotlights dead; only a green exit glow and torch beams sliding along the hull`

**PLATE — establishing, 16:9:**
Cinematic still of a long, dim, high exhibition hall at night, with no people, built around a single ancient ship: a slender forty-three-metre vessel of honey-brown cedar with a high curved prow and stern shaped like papyrus bundles, a small deckhouse amidships and long oars laid along its sides, resting on a low steel cradle. A raised walkway with a glass balustrade runs its full length. Warm spotlights rake the wood; the hall is black around it. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 13. LOC_GEM_LOADING_DOCK — the loading dock (Seq 4.4, the end of Act One)

**Production spec:** a covered concrete dock at the back of the museum. It has four tall roll-up steel doors, black rubber dock bumpers, a raised platform at truck-bed height, an oil-stained concrete yard, steel stair rails, lamp masts and a perimeter fence with the desert night beyond. Tarek's army truck (LOC_ARMY_TRUCK) is parked at the platform.

**LONG:** a wide covered loading dock at the back of a huge modern museum, a row of tall roll-up steel doors above a raised concrete platform with black rubber bumpers, an oil-stained concrete yard, steel stair rails, tall lamp masts, and a perimeter fence with dark open desert beyond it

**SHORT:** a wide covered museum loading dock, tall roll-up steel doors over a raised concrete platform, an oil-stained yard and lamp masts

**Lighting variants:**
- `LOC_GEM_LOADING_DOCK_NIGHT`: `orange sodium light pooling from the lamp masts, hard black shadows between, the desert beyond the fence dark` + GRADE_NIGHT_ACTION
- `LOC_GEM_LOADING_DOCK_BLACKOUT`: `lamp masts dead; lit only by a truck's headlights and torch beams, black beyond`

**PLATE — establishing, 16:9:**
Cinematic night still of a wide covered loading dock at the back of a huge modern museum, with no people. A row of tall roll-up steel doors stands above a raised concrete platform with black rubber bumpers and steel stair rails. A sand-coloured military truck is parked at the platform on an oil-stained concrete yard. Tall lamp masts pool orange sodium light; beyond a perimeter fence, dark open desert. Hard black shadows. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 14. LOC_GEM_ROOF — the roof terrace, dawn (Seq 2.6, "EXT. GEM ATRIUM BALCONY — DAWN")

**Real anchors:** the GEM lies 2 km north-west of the pyramids, and its north and south walls line up with the pyramids of Khufu and Menkaure [07 E5]. From the building, then, the pyramids lie to the **south-south-east**. At dawn the sun rises at **frame left** of that view.

**Production spec:** a high exterior terrace of pale stone paving with a frameless glass balustrade, looking south-east across the plain to the plateau. The screenplay heading "GEM ATRIUM BALCONY" maps to this token.

**LONG:** a high exterior terrace of pale stone paving on a vast modern museum, edged by a frameless glass balustrade, looking out across a wide sandy plain and the edge of a sprawling city to the three Giza pyramids two kilometres away on their desert plateau

**SHORT:** a high pale-stone museum terrace with a glass balustrade, the three Giza pyramids two kilometres away across the plain

**Lighting variants:**
- `LOC_GEM_ROOF_DAWN`: `first light: the sun just below the horizon at frame left, a cool blue sky warming to pale gold, the pyramids' left faces catching faint rose light, haze over the city`
- `LOC_GEM_ROOF_DAY`: `clear morning light, neutral-cool daylight, crisp distance, the pyramids sharp` + GRADE_2033_DAY

**Geography lock:** the pyramids are straight ahead, the sunrise is at frame left, and the city is at frame right. Nour and Adaeze stand at the balustrade in two-shot profile.

**PLATE — establishing, 16:9:**
Cinematic dawn still from a high exterior terrace of pale stone paving on a vast modern museum, edged by a frameless glass balustrade, with no people. Beyond, a wide sandy plain and the edge of a sprawling city lead to the three Giza pyramids two kilometres away on their desert plateau. The sun is just below the horizon at the left; the sky is cool blue warming to pale gold, the pyramids' left faces catch faint rose light, and haze lies over the city. Photoreal live-action film still, anamorphic 75mm, fine film grain. Aspect ratio 16:9.

---

## C. CAIRO

## 15. LOC_NOUR_FLAT — Nour's flat, Cairo (Seq 2.5)

**Production spec (fiction):**
- A third-floor flat in a 1950s apartment building in Dokki, Giza, on the west bank (a production choice).
- Ceilings about 3.5 m high. Patterned cement floor tiles in faded ochre and grey, typical of Cairo.
- Tall wooden shutters with peeling pale green paint, opening onto a narrow balcony over a side street.
- Bookshelves crammed to the ceiling, their spines blurred and unreadable. Layla's crayon drawings are taped to a door.
- A dining table buried in papers serves as the desk. On it sits her old laptop with its Wi-Fi card pulled.
- A child's night-light glows in the doorway of Layla's room.
- **No legible text** (bible §13).

**LONG:** a lived-in third-floor flat in an old 1950s Cairo apartment building, high ceilings, patterned cement floor tiles in faded ochre and grey, tall wooden shutters with peeling pale green paint, bookshelves crammed to the ceiling, a child's crayon drawings taped to a door, a dining table buried in papers serving as a desk

**SHORT:** a lived-in 1950s Cairo flat, high ceilings, patterned floor tiles, tall wooden shutters, crammed bookshelves, a paper-strewn table used as a desk

**Lighting variants:**
- `LOC_NOUR_FLAT_NIGHT`: `one warm desk lamp and the cold blue-white glow of a laptop screen on her face, scattered city lights through the shutter slats, a child's night-light glowing in a doorway`
- `LOC_NOUR_FLAT_DAY`: `hard white Cairo daylight falling in stripes through half-closed shutters, dust in the air`

**Rules:**
- The laptop screen is COMP: the frame-scrub and the syllable-by-syllable transcription.
- Layla is seen asleep only through the doorway, at a distance, under a blanket. The approved Layla master protocol applies (bible §3.3).

**PLATE — establishing, 16:9:**
Cinematic night still inside a lived-in third-floor flat in an old 1950s Cairo apartment building, with no people. High ceilings; patterned cement floor tiles in faded ochre and grey; tall wooden shutters with peeling pale green paint, city lights glinting through their slats. Bookshelves crammed to the ceiling, their spines blurred; a child's crayon drawings taped to a door; a dining table buried in papers under one warm desk lamp beside an old open laptop glowing blue-white. A child's night-light glows in a far doorway. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 16. LOC_CONTROL_ROOMS — the blackout montage control rooms (Seq 4.2; reversed in 12.8)

**Real anchors [14 §4]:**
- the national grid and the High Dam's telemetry;
- the Suez Canal pilots' screens;
- a cable landing station: Egypt carries about 17% of global internet traffic (bible §7, 4.2);
- the 2011 internet shutdown is the "unplug it" precedent.

**Rules (bible §7, 4.2; §14.6):**
- **Control rooms only.** Screens go dark; there is **never physical damage**.
- No real operator, logo, outlet or chyron. Every screen is abstract lines and blocks, or COMP.

**LONG:** a large modern infrastructure control room, a curved video wall of network diagrams and maps above tiered rows of operator desks with multiple monitors, grey carpet tiles, acoustic ceiling panels, a few operators in headsets; every screen displays abstract lines and blocks with no readable text

**SHORT:** a modern infrastructure control room, a curved video wall above tiered operator desks, every screen abstract lines with no readable text

**Area add-ons:**
- `GRID`: `the national grid dispatch room, its video wall a vast abstract network of glowing lines`
- `DAM`: `a window behind the desks looking down into a vast dim turbine hall`
- `CANAL`: `tall windows behind the desks overlooking a wide straight canal at night, the lights of a huge container ship gliding past`
- `CABLE`: `a cold, narrow equipment hall of tall black server racks glittering with tiny status lights, thick bundled cables overhead`

**Lighting variants:**
- `LOC_CONTROL_ROOMS_LIVE`: `bright blue-white screen light on faces, low ambient room light`
- `LOC_CONTROL_ROOMS_DARK` (4.2): `screens dying one after another to black, the last faces lit by a single dimming monitor, then darkness`
- `LOC_CONTROL_ROOMS_RELIGHT` (12.8): `screens flickering back on one by one, blue-white light returning to tired faces`

**PLATE — establishing, 16:9:**
Cinematic night still of a large modern infrastructure control room, with no people. A curved video wall of abstract glowing network diagrams and maps rises above tiered rows of operator desks with multiple monitors, all showing abstract lines and blocks with no readable text. Grey carpet tiles and acoustic ceiling panels; low ambient light, blue-white screen glow. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 17. LOC_CAIRO_FLYOVER — Cairo's flyovers and streets in the blackout (Seq 5.2)

**Real anchors [14 §3]:**
- Greater Cairo has about 22.1 million people.
- The **6th October Bridge** is a 20.5 km elevated causeway that crosses the Nile twice.
- The Ring Road runs about 100 km around the city. The Rod El Farag Axis is 67.3 m wide.
- The film's flyover is generic; it is never named in prompts.

**Look (bible §11):** a modern megacity, neutral-to-cool. **Never a yellow or sepia "desert filter".** No bazaars, fezzes or snake charmers. No legible Arabic signage.

**LONG:** a long elevated urban flyover of grey concrete on tall round pillars, six lanes with concrete barriers and tall double-armed street lamps, curving between dense ten- and fifteen-storey apartment towers of concrete and red brick, their roofs crowded with satellite dishes and water tanks, a wide dark river glinting far below

**SHORT:** a long elevated concrete flyover curving between dense concrete-and-red-brick apartment towers with satellite dishes, a dark river below

**Area add-ons:**
- `STREET`: `at street level on a dense avenue beneath the flyover, shuttered shopfronts with dark unreadable signs, parked cars and tangled overhead cables`
- `ROBOTAXI_WALL`: the pods are UNIT_ROBOTAXI (file 02 §14.4)

**Lighting variants:**
- `LOC_CAIRO_FLYOVER_BLACKOUT_ROLLING`: `the city going dark district by district: some blocks still glowing sodium orange, others already black, street lamps dying in sequence along the flyover, headlights the only constant` + GRADE_NIGHT_ACTION
- `LOC_CAIRO_FLYOVER_BLACKOUT_FULL`: `total blackout: towers black against a starry sky, lit only by the truck's headlights, the white light bars of driverless pods and one thin red light line`
- `LOC_CAIRO_FLYOVER_DAY`: `hazy neutral daylight, towers crisp, dense traffic` + GRADE_2033_DAY

**Geography lock:** we watch from inside the truck's cargo bed, looking back over the tailgate, so the pursuit re-forms **toward camera**. The river lies at frame left below the flyover.

**Flags:** `VFX-EXTEND` for the district-by-district blackout (the plate plus comped window lights).

**PLATE — establishing, 16:9:**
Cinematic night still over a vast modern city during a rolling blackout, with no people. A long elevated flyover of grey concrete on tall round pillars curves between dense ten- and fifteen-storey apartment towers of concrete and red brick, their roofs crowded with satellite dishes and water tanks. Some districts still glow sodium orange, others are completely black; a wide dark river glints far below. Neutral-cool colour, no signage legible. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## 18. LOC_ARMY_TRUCK — the army truck: cargo bed and cab (Seq 5.1–5.2)

**Production spec:** a generic Egyptian Army six-wheel cargo truck with sand-khaki paint, a canvas tilt over steel hoops, wooden benches, and jerricans and equipment boxes strapped at the front. There is **no maker's badge and no real model**. Unit markings are sun-bleached blank patches. Cpl. Hassan drives (dies 5.2).

**LONG:** the cargo bed of a military six-wheel cargo truck, sand-khaki steel sides, a faded canvas cover stretched over curved steel hoops, wooden bench seats along both sides, equipment boxes and jerricans strapped at the front, the rear flap tied open above the raised tailgate showing the road rushing away behind

**SHORT:** the canvas-covered cargo bed of a sand-khaki military truck, wooden side benches, the rear flap open onto the road behind

**Area add-ons:**
- `CAB`: `in the truck's cramped cab, a worn bench seat, a military radio handset on a coiled cord, a cracked windscreen onto the night road`
- `EXTERIOR`: `a sand-khaki six-wheel military cargo truck with a faded canvas cover, unmarked`

**Lighting variants:**
- `LOC_ARMY_TRUCK_NIGHT`: `dark inside; passing headlights and dying street lamps sweep through the open back and over faces; a dim green dashboard glow in the cab`

**PLATE — establishing, 16:9:**
Cinematic night still from inside the canvas-covered cargo bed of a moving sand-khaki military truck, with no people. Wooden bench seats run along both sides under curved steel hoops; jerricans and equipment boxes are strapped at the front. The rear flap is tied open above the tailgate, framing an elevated city road rushing away behind, lit by passing headlights and dying orange street lamps. Photoreal live-action film still, anamorphic 32mm, handheld feel, fine film grain. Aspect ratio 16:9.

---

## 19. LOC_CORNICHE_DOCK — the Nile Corniche police dock (Seq 5.3: "They do not own the river")

**Real anchor:** the Tourism and Antiquities Police, under the Interior Ministry, guard Nile cruises [14 §1.5]. The dock itself is production spec: a stone-faced embankment wall with an iron railing and palms above, concrete steps down to a floating steel pontoon hung with tyre fenders, old launches moored alongside (PROP_POLICE_LAUNCH) and a small guard hut. Across the river stand dark hotel towers.

**LONG:** a river police dock on a city riverfront: a tall stone-faced embankment wall topped by an iron railing and palm trees, concrete steps down to a floating steel pontoon hung with black tyre fenders, old patrol launches moored alongside, a small guard hut, and across the wide dark river a line of tall hotel towers and a distant bridge

**SHORT:** a city river police dock, stone embankment and iron railing, concrete steps to a floating steel pontoon with tyre fenders and old launches

**Lighting variants:**
- `LOC_CORNICHE_DOCK_BLACKOUT`: `the city dark across the water, towers black, only a few fires and car headlights on the far bank, stars on the black river, a torch beam on the pontoon` + GRADE_NIGHT_ACTION
- `LOC_CORNICHE_DOCK_NIGHT_LIT`: `the last sodium lamps along the embankment, orange ripples on black water`

**State add-ons:**
- `PHONES`: `mobile phones dropping into black water, their screens lighting up briefly as they sink` (VFX-ASSIST)

**PLATE — establishing, 16:9:**
Cinematic night still of a river police dock on a city riverfront during a blackout, with no people. A tall stone-faced embankment wall, topped by an iron railing and palm trees, drops by concrete steps to a floating steel pontoon hung with black tyre fenders; old white-and-navy patrol launches are moored alongside, and a small guard hut stands at the top. Across the wide black river, tall hotel towers stand dark; a few fires glow on the far bank. Stars reflect in the water. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## D. THE RIVER

## 20. LOC_NILE — the Nile, Cairo to Luxor (Seq 5.3–8; the c. 1332 BC barge)

**Real anchors:**
- Upper and Middle Egypt: a green strip of cane, clover, bananas and date palms along the banks. Brick villages, pump houses and islands with tamarisk and reeds. The limestone cliffs of the desert edge often come close to the river, especially on the east bank near Amarna [02 §3].
- The river's width [verify, roughly 500–900 m in these reaches].
- The feluccas are PROP_FELUCCA and the launch is PROP_POLICE_LAUNCH.
- **Amarna lies opposite Deir Mawas** (bible §7, 9.3).
- The film's Asyut barrage is generic (LOC_ASYUT_LOCK).
- Luxor has many moored cruise ships [verify].
- ⟂ In the blackout the river is dark end to end: "They own the sky and the wires. They do not own the river."

**LONG:** the wide Nile in Upper Egypt, broad slow water between low banks lined with date palms, tall sugar cane and small mud-brick and red-brick villages, sandbars and reedy islands with tamarisk trees midstream, and beyond the green strip the bare limestone cliffs of the desert edge

**SHORT:** the wide slow Nile between banks of date palms, sugar cane and brick villages, reedy islands midstream, desert cliffs beyond

**Area add-ons:**
- `ISLAND` (6.2): `moored under the trailing branches of tamarisk trees on a small river island, reeds and wet sand at the waterline`
- `FISHING_GROUNDS` (6.1): `among small wooden fishing boats with nets and lanterns`
- `WEST_BANK_SHALLOWS` (8.0): `at the reedy edge of the shallows on the west bank, mud, reeds and a farmer's small wooden boat` (the boat is PROP_FARMER_BOAT, which also makes the fast crossing back to the East Bank in 8.6 → 9.1)
- `LUXOR` (7.5): `off Luxor, dark tourist cruise ships moored three abreast along the east bank, unlit`
- `OPPOSITE_AMARNA` (6.5): `the east bank opening into a wide pale desert plain ringed by cliffs, white fabric sun-shades glinting far across the water`
- `ANCIENT_1332` (9.5b): `the ancient river with no modern structures, dense papyrus thickets at the banks, a long wooden barge with a tall cabin and torches gliding north` (the barge is PROP_NIGHT_BARGE_1332)

**Lighting variants:**
- `LOC_NILE_NIGHT`: `blackout night: no light on either bank, black water holding a dense field of stars, palms as black silhouettes, cold white drone pinpoints the only lights` + GRADE_NIGHT_ACTION
- `LOC_NILE_DAWN`: `first light: mist lying on the water, the sky pale rose rising to cool blue, palms in silhouette, the river silver`
- `LOC_NILE_DAY`: `clear morning, neutral-cool daylight, blue-grey water, crisp green banks` + GRADE_2033_DAY
- `LOC_NILE_MIDDAY_HAZE` (6.5): `hard white midday sun, heat shimmer bending the far bank, a bleached sky`
- `LOC_NILE_AFTERNOON_GOLD` (6): `long gold afternoon light, the low sun behind the west bank palms, glittering water`

**State add-ons:**
- `FELUCCA_FIRE` (6.1, VFX-ASSIST): `far off on the dark water, a small sailing boat burning with no one aboard, its orange flames doubled in the reflection`

**Geography lock:** **south (upriver) is always frame right** in profile shots of the launch. The east bank is the far bank when the camera is on the west side.

**PLATE — establishing, 16:9:**
Cinematic still of the wide Nile in Upper Egypt at dawn, with no boats. Broad, slow water lies between low banks lined with date palms, tall sugar cane and small mud-brick and red-brick villages. Sandbars and reedy islands with tamarisk trees sit midstream; beyond the green strip rise the bare limestone cliffs of the desert edge. Mist lies on the water; the sky is pale rose rising to cool blue, the palms in silhouette. Photoreal live-action film still, anamorphic 75mm, fine film grain. Aspect ratio 16:9.

---

## 21. LOC_ASYUT_LOCK — the Asyut barrage and its navigation lock (Seq 6, afternoon: "It's holding the door for us")

**Real anchors:** a barrage with navigation locks crosses the Nile at Asyut; a new barrage with hydropower was completed around 2018 [verify; not in the research]. The screenplay asks for a generic, unbranded barrage [seq_06 note].

**Production spec:** a long, low concrete barrage on massive piers with gantries and sluice gates. A lock chamber about 150 × 17 m [verify] has sheer concrete walls about 15 m high, iron ladders, water staining and huge steel gates. **Shabti stand evenly spaced along both wall tops.**

**LONG:** a long, low concrete river barrage striding across the wide Nile on massive piers, steel gantries and sluice gates along its crest, and at one end a navigation lock: a deep straight chamber between sheer wet concrete walls fifteen metres high, closed by huge steel gates, water staining and iron ladders on its walls

**SHORT:** a concrete Nile barrage with a navigation lock, a deep chamber between sheer wet concrete walls and huge steel gates

**Lighting variants:**
- `LOC_ASYUT_LOCK_AFTERNOON`: `long gold afternoon sun across the barrage, the lock chamber in deep blue shadow below a bright sky`

**State add-ons:**
- `FILLING`: `water churning white as the lock fills, the boat rising slowly up the wall` (VFX-ASSIST)

**PLATE — establishing, 16:9:**
Cinematic afternoon still of a long, low concrete barrage striding across the wide Nile on massive piers, steel gantries and sluice gates along its crest, with no people. At one end, a navigation lock: a deep straight chamber between sheer wet concrete walls fifteen metres high, water-stained and fitted with iron ladders, closed by huge steel gates. Long gold sun on the barrage, the lock chamber in deep blue shadow. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## E. KARNAK (Seq 7: 21:00 on 5 Nov → 03:00 on 6 Nov; Luxor dark)

**Real anchors for the whole precinct [13 §2]:**
- The sandstone of the temple, columns included, came from Gebel Silsila, about 100 miles south.
- The **Avenue of Sphinxes** ran in a straight line for about **2,700 m** between Luxor Temple and Karnak. It had six barque way-stations and **more than 1,050** sphinx and ram statues, and reopened on 25 Nov 2021.
- The **Sacred Lake** measures 120 × 77 m.
- The talatat pylons: Horemheb packed the Second and Ninth Pylons (and the Tenth [02 §13]) with Akhenaten's blocks.
- The **Restoration Stela**: red granite, 2.54 × 1.29 × 0.38 m. Legrain found it in fragments in the NE corner of the Hypostyle Hall in July 1905 (one source says 1907). It originally stood before the Third Pylon, and is now at the GEM.
- Axes: the main east–west axis runs from the river front through the First Pylon, the Great Court, the Second Pylon, the Hypostyle Hall and the Third Pylon. The southern axis runs through the Seventh to Tenth Pylons toward the Precinct of Mut and the avenue [verify the layout against a plan].
- ⟂ "Jackals hold the axis."

## 22. LOC_KARNAK_RAM_AVENUE — the ram avenue and the First Pylon (Seq 7.1 arrival; 7.3 the projection)

**Real anchors:**
- An avenue of ram-headed sphinxes approaches Karnak's west front [13 §2; verify its layout].
- The First Pylon is unfinished and uncarved. It is about 113 m wide [verify]; its height is [verify, often given at about 40 m].
- **Production choice:** the midpoint projection ("the pylon and the columns", bible §7, 7.3) is mapped onto the **First Pylon**, the only surface tall enough for a figure forty metres high.

**LONG:** a long processional avenue of weathered sandstone ram-headed sphinxes crouched on pedestals in two facing rows, leading to a colossal unfinished temple gateway of two massive sloping sandstone towers, over a hundred metres wide, its rough face never carved, palm trees and the dark town beyond

**SHORT:** an avenue of weathered sandstone ram-headed sphinxes in two rows leading to a colossal unfinished temple gateway of two sloping towers

**Area add-ons:**
- `SPHINX_AVENUE` (the "Avenue of Sphinxes": the 2.7 km processional way that ran south from Karnak's southern precincts to Luxor Temple, with more than 1,050 sphinx and ram statues, reopened 25 Nov 2021 [13 §2]; the short ram avenue before the First Pylon is a separate avenue [verify]): `on a long, straight processional avenue of weathered human-headed sphinxes on low pedestals in two facing rows, running away into the distance between low retaining walls and palms`
- `CORNICHE_ROAD` (7.4, the route to the landing): `on a wide, dead riverfront road, its street lamps dark, palms along a low parapet, the black river beyond`

**Lighting variants:**
- `LOC_KARNAK_RAM_AVENUE_NIGHT`: `Luxor dark: the gateway lit hard white from below by a few drone floodlights, long black shadows of the rams across the paving, a starry sky` + GRADE_NIGHT_ACTION
- `LOC_KARNAK_RAM_AVENUE_PROJECTION` (7.3, COMP + VFX-EXTEND): `the whole face of the gateway lit by a projected moving image, its warm white-gold light washing over the rams and the small figures below`
- `LOC_KARNAK_RAM_AVENUE_DAY` (reference only): `hard sun on honey-coloured sandstone, deep shade under the rams`

**Rule for the projection:** never generate the projected Akhenaten inside the plate. Generate his performance as its own locked-face clip (CHAR_AKHENATEN), then map it onto the pylon plate in comp (file 05 §10, row 14).

**Geography lock:** the avenue runs west to east toward the gateway; the river landing and the dead Corniche road are behind camera (west). In the projection scene, Tut stands in the open at frame centre, the forty-metre figure fills the pylon above him, and Fathi drags him **frame left** into the rams' shadow.

**PLATE — establishing, 16:9:**
Cinematic night still of a long processional avenue of weathered sandstone ram-headed sphinxes crouched on pedestals in two facing rows, leading to a colossal unfinished ancient temple gateway of two massive sloping sandstone towers more than a hundred metres wide, its rough face never carved. The gateway is lit hard white from below by a few floodlights; the rams cast long black shadows across the paving; palm trees and a dark, unlit town lie beyond under a starry sky. No people. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 23. LOC_KARNAK_HYPOSTYLE — the Great Hypostyle Hall and the Third Pylon (Seq 7.1 the thread loom; 7.2 the Third Pylon; 7.3)

**Real anchors [13 §2]:**
- The hall "covers an area of 50,000 sq ft (5,000 m²)". "The roof, now fallen, was supported by **134 columns in 16 rows**; the 2 middle rows are higher than the others".
- The **12 great open-papyrus columns** are about **21 m** tall in the shaft (24 m including abacus and architrave) and about 10 m in circumference. The other **122 are shorter closed-bud columns**, about 13–15 m tall [verify].
- It was built by Seti I; Ramesses II completed the decoration of the southern wing.
- Clerestory window grilles survive over the central aisle, and traces of the original paint survive on the capitals and architraves [verify].
- The Restoration Stela was found in the hall's NE corner. It originally stood before the **Third Pylon**, which forms the hall's east wall [verify].
- ⟂ Tut at the Third Pylon: "I put it here."

**LONG:** a vast ancient hall of colossal sandstone columns packed in dense rows, the central aisle flanked by twelve giant open-papyrus columns twenty-one metres high beneath fragments of stone roof and slotted clerestory windows, over a hundred shorter bud-capital columns receding on either side, every surface carved in deep weathered relief with traces of faded blue and red paint

**SHORT:** a vast ancient hall of colossal carved sandstone columns in dense rows, giant papyrus columns twenty-one metres high lining the central aisle

**Area add-ons:**
- `THIRD_PYLON`: `at the hall's east end, where the rough inner face of a massive sandstone gateway tower rises behind the last columns`
- `NE_CORNER`: `in the hall's north-east corner among the shorter columns, fallen stone fragments on the floor`

**State add-ons:**
- `THREADS` (7.1, VFX line): `hair-thin glinting threads strung between the columns at shin, waist and head height like a loom, catching the light`
- `THREADS_CUT`: `a few threads hanging slack and broken between the columns`

**Lighting variants:**
- `LOC_KARNAK_HYPOSTYLE_NIGHT`: `lit only by scattered drone floodlights far above, hard white shafts falling between the columns, deep black aisles, small red and amber machine lights moving in the dark` + GRADE_NIGHT_ACTION
- `LOC_KARNAK_HYPOSTYLE_PROJECTION` (7.3): `warm white-gold light from a giant projection spilling in from the west across the column faces, shifting as the image moves`
- `LOC_KARNAK_HYPOSTYLE_DAY` (reference only): `hard sun shafting through the gaps in the fallen roof, warm sandstone against deep cool shadow`

**Geography lock:** the central aisle runs west (frame left) to east (frame right) in lateral shots. Rami's cart run (7.4) crosses the aisles **south to north** before turning west toward the river. The Third Pylon closes the far end in axial shots looking east.

**PLATE — establishing, 16:9:**
Cinematic night still inside a vast ancient hall of colossal sandstone columns packed in dense rows, with no people. The central aisle is flanked by giant open-papyrus columns twenty-one metres high beneath fragments of stone roof and slotted clerestory windows; over a hundred shorter bud-capital columns recede on either side. Every surface is carved in deep weathered relief with traces of faded blue and red paint. Hard white shafts of floodlight fall from far above between the columns; the aisles between are deep black. Photoreal live-action film still, anamorphic 24mm, low angle, fine film grain. Aspect ratio 16:9.

---

## 24. LOC_KARNAK_NINTH_PYLON — the Ninth Pylon, the block field and the processional way (Seq 7.1–7.2, the heist)

**Real anchors:**
- Horemheb packed **tens of thousands of talatat** into Karnak's Second, Ninth and Tenth Pylons, and the Akhenaten Temple Project later matched block photographs by computer [02 §13; 16 §4; 13 §2].
- The Ninth Pylon is Horemheb's gateway on the southern axis, between the Eighth and Tenth Pylons. It was partly dismantled and rebuilt by restorers in the late 20th century [verify].
- Karnak's open-air block fields really do hold thousands of loose blocks laid in rows [verify for this area].
- The talatat lock is 52 × 26 × 24 cm, sandstone, about 70–75 kg (PROP_KARNAK_BLOCK).
- ⟂ SESHAT's bucket-chain dismantles the pylon, and a drone sweep photographs every **decorated** face, row by row.

**Production spec:**
- A pylon of two sloping towers, about 45 m wide and 20 m high [production scale; verify].
- One tower is opened from the top like a quarry, its talatat core exposed in courses.
- Scaffold ramps run down its face.
- On the ground, long rows of blocks lie face up; the sweep's light grid crawls over them.

**LONG:** a massive ancient sandstone temple gateway of two sloping towers, one tower opened from the top like a quarry, its core of thousands of small hand-cut carved blocks the size of suitcases exposed in layers; scaffolding and ramps descend its face, and on the ground beside it rows upon rows of small carved blocks lie laid out on the sand

**SHORT:** a massive ancient sandstone gateway opened from the top like a quarry, its core of small carved blocks exposed, blocks laid in rows

**Area add-ons:**
- `BLOCK_FIELD`: `in the open block field, thousands of small carved sandstone blocks laid face up in long rows on the sand, faded paint on some faces`
- `PROCESSIONAL_WAY`: `along a stone-paved processional way between ruined courts, fallen blocks and empty statue bases on either side`

**Lighting variants:**
- `LOC_KARNAK_NINTH_PYLON_NIGHT_WORK`: `harsh white work floods on stands around the gateway, a slow grid of drone lights sweeping the block field row by row, a black starry sky` + GRADE_NIGHT_ACTION
- `LOC_KARNAK_NINTH_PYLON_DARK` (Nour reads by touch): `almost no light: faint starlight and distant floodlight spill, faces and hands barely readable, the stone a dim grey`

**Geography lock:** the pylon is at frame right in the master; the bucket-chain runs down its face from right to left onto the field. The sweep advances **toward camera**, row by row, as the visible countdown.

**PLATE — establishing, 16:9:**
Cinematic night still of a massive ancient sandstone temple gateway of two sloping towers, with no people. One tower has been opened from the top like a quarry, exposing a core of thousands of small hand-cut carved blocks in layers, with scaffolding and ramps descending its face. On the sand beside it, rows upon rows of small carved blocks lie laid out face up. Harsh white work floods on stands light the scene; a grid of small drone lights hangs over the field against a black starry sky. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 25. LOC_KARNAK_SACRED_LAKE — the Sacred Lake (Seq 7)

**Real anchors [13 §2]:**
- **120 × 77 m**, dug by Thutmose III and fed from the water table; the largest temple lake in Egypt.
- It is stone-lined with steps [verify].
- The colossal granite scarab of Amenhotep III stands near its north-west corner [verify].

**LONG:** a large rectangular ancient sacred lake about one hundred and twenty by seventy-seven metres, its still dark water held by walls of fitted sandstone blocks with steps descending into it, ruined temple walls and gateways beyond, and a colossal granite scarab on a pedestal near one corner

**SHORT:** a large rectangular ancient sacred lake of still dark water in stone-block walls with steps, ruined temple gateways beyond

**Lighting variants:**
- `LOC_KARNAK_SACRED_LAKE_NIGHT`: `black mirror water reflecting the stars and the white drone lights sweeping above, the gateways in silhouette` + GRADE_NIGHT_ACTION
- `LOC_KARNAK_SACRED_LAKE_PROJECTION`: `the distant projected figure reflected, trembling, in the black water`

**PLATE — establishing, 16:9:**
Cinematic night still of a large rectangular ancient sacred lake, about one hundred and twenty by seventy-seven metres, its still black water held by walls of fitted sandstone blocks with steps descending into it, with no people. Ruined temple walls and gateways stand in silhouette beyond; a colossal granite scarab sits on a pedestal near one corner. The water mirrors the stars and a few white drone lights overhead. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 26. LOC_KARNAK_QUAY — the river landing, "the quay" (Seq 7.4: Rami; the block into the water)

**Real anchors:** Karnak's ancient quay terrace in front of the First Pylon once faced a harbour basin or canal linked to the Nile. Today it lies inland, some hundreds of metres from the river [verify]. The screenplay's route is: down the ram avenue, across the dead Corniche road, down the boat ramp to the stone quay (seq_07, with its own [[verify]] note).

**Production spec:** a modern stone river landing on the Luxor Corniche opposite Karnak's west front. It has a sloping boat ramp, a long quay of fitted limestone blocks with iron mooring rings, and a low parapet wall along the road above. The channel beside it runs **deep** (bible: "the deep channel"). The launch is moored at the far end.

**LONG:** a stone river landing below a city riverfront road: a sloping boat ramp and a long quay of fitted limestone blocks with iron mooring rings, a low parapet wall above it along the road, and beside the quay's edge the wide river running deep and black, dark cruise boats moored far along the bank

**SHORT:** a long stone river quay with iron mooring rings below a parapet wall, a boat ramp, the wide river deep and black beside it

**Lighting variants:**
- `LOC_KARNAK_QUAY_NIGHT`: `blackout night: the quay lit only by a torch and the dim red lamp of a moored launch, faint white drone light far above, black water glinting with stars` + GRADE_NIGHT_ACTION

**State add-ons:**
- `CART_OVER` (VFX-ASSIST): `a hand-cart tipping off the quay's edge into the black water with a heavy splash`
- `SINKING` (underwater insert, VFX-ASSIST): `a carved stone block sinking face down through dark green-black water, bubbles streaming upward`

**Geography lock (the master, from the launch looking back up the quay):** the river is at **frame right**; the parapet wall and the Corniche road are at **frame left**, high; the boat ramp is at the top of frame in the distance. The runners come **toward camera**. The jackal lands on the parapet (frame left) and fires toward frame right, **away from the lens**.

**Safety:** Rami's death follows the kill grammar: sparks off the cart handle, then he drops out of frame behind the cart, then a reaction, then the sound tail (file 05 §7; the worked example in file 05 §11).

**PLATE — establishing, 16:9:**
Cinematic night still during a city blackout, looking along a long stone river quay of fitted limestone blocks with iron mooring rings, with no people. At the left, a low parapet wall runs along a dark riverfront road above; at the right, the wide river runs deep and black, glinting with stars. A sloping boat ramp descends at the far end, and dark cruise boats are moored far along the bank. An old white patrol launch with a dim red wheelhouse lamp waits in the foreground. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## F. THE WEST BANK AND THE VALLEY OF THE KINGS (Seq 8: 03:30–10:00 on 6 Nov; coda)

## 27. LOC_WEST_BANK_FIELDS — the West Bank fields (Seq 8.0)

**Production spec:**
- Flat irrigated farmland below the Theban hills: earth tracks between walls of tall sugar cane and fields of clover.
- A small reedy canal, a mud-brick pump house and date palms.
- The pale limestone cliffs of the western mountain rise sharply beyond [13 §3 context].

**LONG:** flat irrigated farmland on the Nile's west bank below bare desert hills: narrow earth tracks between walls of tall sugar cane and fields of green clover, a small irrigation canal lined with reeds, a mud-brick pump house, date palms, and the pale limestone cliffs of the western mountain rising sharply beyond

**SHORT:** west-bank farmland of tall sugar cane and clover, earth tracks and a reedy canal, bare limestone cliffs rising beyond

**Lighting variants:**
- `LOC_WEST_BANK_FIELDS_NIGHT`: `starlight only, the cane black, the cliffs ahead a pale grey wall, a first thin line of blue on the eastern horizon behind` + GRADE_NIGHT_ACTION
- `LOC_WEST_BANK_FIELDS_MORNING`: `hard low morning sun from the east, long shadows of the cane across the tracks, the cliffs glowing` + GRADE_2033_DAY

**PLATE — establishing, 16:9:**
Cinematic pre-dawn still of flat irrigated farmland on the Nile's west bank, with no people: a narrow earth track between walls of tall sugar cane and a field of green clover, a small irrigation canal lined with reeds, a mud-brick pump house and date palms. Ahead, the pale limestone cliffs of a bare desert mountain rise sharply against a deep blue sky with the last stars. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## 28. LOC_VOK — the Valley of the Kings (Seq 8.1 pre-dawn; 8.6 the morning glare; the valley road; coda KV21)

**Real anchors [13 §3]:**
- "KV" numbering dates from Wilkinson (1827). There are at least 63 tombs; KV64 and KV65 are the latest.
- **KV9 (Ramesses VI) "was built over the top of" KV62.** KV63 lies between KV10 and KV62, "near the main crossroads".
- Occasional **flash floods** threaten the tombs.
- Four to five thousand visitors a day came in 2005.
- The pyramid-shaped peak above is el-Qurn [verify its height].
- The ticket kiosks and electric visitor trams are dead in the film (bible §7, 8.1).
- ⟂ SESHAT's drill (UNIT_DRILL) grinds on the hillside above the tomb.

**LONG:** a narrow, steep-sided desert valley of pale fractured limestone, its floor laid with paved paths and low dry-stone walls, dark rectangular tomb entrances cut into the cliff bases with steel gates and small stone porches, loose scree slopes rising to jagged ridges and a pyramid-shaped peak above

**SHORT:** a narrow pale limestone desert valley of paved paths and dark tomb entrances with steel gates, scree slopes rising to a pyramid-shaped peak

**Area add-ons:**
- `KIOSKS`: `at the valley mouth, past dark shuttered ticket kiosks and an empty shelter for electric visitor trams`
- `RIDGE` (8.6, where the jackals fire from): `on the rocky ridge line high above the valley floor`
- `VALLEY_ROAD` (8.6): `on the winding asphalt road out of the valley between bare limestone hills`
- `KV21` (coda): `at a small, plain tomb entrance in a quiet side branch of the valley, rubble and a low stone wall around it`

**Lighting variants:**
- `LOC_VOK_PREDAWN`: `deep blue pre-dawn light, the sky paling behind the eastern ridge, the valley floor still dark, the drill's pale dust plume faintly visible on the hillside`
- `LOC_VOK_MORNING_GLARE` (8.6): `blinding morning glare: hard white sun on pale limestone, a bleached sky, sharp black shadows at the tomb mouths, heat already rising` + GRADE_2033_DAY
- `LOC_VOK_SUNSET` (coda): `warm low sun, the cliffs glowing gold, the valley floor in cool blue shadow`
- `LOC_VOK_DAY` (coda, "EXT. KV21, VALLEY OF THE KINGS - DAY"): `clear, calm daylight, soft and even, the cliffs pale gold against a blue sky, the valley quiet and empty` + GRADE_2033_DAY

**Geography lock:** from the valley floor at KV62, KV9's large porch rises at **frame right, above and behind** the small KV62 stairwell. The drill sits on the hillside above, frame right. The ridge where the jackals appear is **frame left** in the escape (8.6).

**PLATE — establishing, 16:9:**
Cinematic pre-dawn still of a narrow, steep-sided desert valley of pale fractured limestone, with no people. Paved paths and low dry-stone walls run along the valley floor; dark rectangular tomb entrances are cut into the cliff bases, closed by steel gates under small stone porches. Loose scree slopes rise to jagged ridges and a pyramid-shaped peak against a deep blue sky paling in the east. On the hillside above, a faint plume of pale dust. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 29. LOC_KV62_STAIR — the KV62 entrance stair (Seq 8.2 descent; 8.6 out into the glare)

**Real anchors:**
- The first step was found on 4 Nov 1922 [01 §2].
- The tomb lies below KV9's entrance [13 §3].
- A stair of **sixteen steps** leads down to a descending corridor and then the antechamber [verify: 16 steps; corridor about 7.6 m].
- Entrance stair and corridor → antechamber → burial chamber [01 §14].

**Production spec:** a narrow rectangular stairwell cut into the valley floor with a low dry-stone retaining wall around its rim, worn rock-cut steps, and a steel gate at the corridor mouth.

**LONG:** a narrow rectangular stairwell cut straight down into the pale limestone floor of a desert valley, sixteen worn rock-cut steps descending to a dark doorway with a steel gate, a low dry-stone retaining wall around its rim, and above it the larger porch of another tomb cut into the cliff

**SHORT:** a narrow stairwell of sixteen worn rock-cut steps descending into the valley floor to a dark gated doorway, a low stone wall around it

**Lighting variants:**
- `LOC_KV62_STAIR_PREDAWN`: `deep blue pre-dawn light at the top of the steps, the doorway below a black rectangle, a torch beam flicking on inside`
- `LOC_KV62_STAIR_MORNING_GLARE` (from below): `a blinding white rectangle of sky at the top of the steps, figures bursting up out of the dark into glare, dust swirling in the light`

**PLATE — establishing, 16:9:**
Cinematic still of a narrow rectangular stairwell cut straight down into the pale limestone floor of a desert valley, with no people: sixteen worn rock-cut steps descend to a dark doorway closed by an open steel gate. A low dry-stone retaining wall runs around the rim; above and behind it, the larger porch of another tomb is cut into the cliff. Deep blue pre-dawn light, the doorway a black rectangle. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 30. LOC_KV62_BURIAL_2033 — the KV62 burial chamber in 2033 (Seq 8.2 "It is my wall"; the coda)

**Real anchors:**
- Chamber 6.4 × 4.0 m; the tomb is about 110 m² [01 §14].
- The north wall scene is as in LOC_KV62_BURIAL_1323 [09 §5.2].
- The tomb was conserved in 2009–2019 by the Getty Conservation Institute with the Ministry. That work added a viewing platform, barriers, new lighting and ventilation, and studied the **dark brown spots** on the paintings (dead microbial growth) [verify; not in the research].
- The mummy has lain in a climate-controlled glass case in the antechamber since 4 Nov 2007, and in reality stays there [01 §15].
- The outermost coffin went to the GEM for restoration in 2019 [verify].
- The **Sept 2026 microgravity survey** suggested a rubble-packed corridor about 2 m wide leading north and 5–6 chambers 25–30 m north. It is disputed [01 §14].
- ⟂ Under OSIRIS the mummy moved to the GEM, so in Seq 8 the case is **empty**. In the coda it is back.
- Nour signed the petition against breaking the wall (bible §2 Layer 4).

**Production spec:**
- The quartzite sarcophagus stands **empty under a glass top**.
- A low wooden viewing platform with a rail runs along the south side.
- In the blackout, all the tomb's lighting is dead.

**LONG:** a small rock-cut burial chamber about six by four metres, its walls painted on a golden-yellow ground with large flat figures, faded and freckled with small dark brown spots; on the far wall a priest in a leopard skin touches an adze to a wrapped royal figure; an empty quartzite sarcophagus under a glass top at the centre; a low wooden viewing platform with a rail

**SHORT:** a small rock-cut burial chamber with faded golden-yellow painted walls freckled with dark spots, an empty quartzite sarcophagus under glass

**State add-ons:**
- `WALL_BROKEN` (8.2 onward, VFX-ASSIST at the moment of breaking): `a ragged hole broken through the far painted wall at head height, begun at a painted eye, chunks of plaster and rubble on the floor, pale dust hanging in the air`
- `CODA` (coda): `the far wall seamlessly conserved and the painted eye restored, fresh blue cornflowers laid on the sarcophagus glass`
- `CODA_CASE` (coda, the antechamber view): `in the foreground a glass climate case holding a linen-shrouded form on a tray of sand, only a thin gold seam at one wrist showing` (bible §7, 12.9; remains rule)

**Area add-ons:**
- `ANTECHAMBER` (the coda heading "INT. KV62, ANTECHAMBER - SUNSET"; real: 7.9 × 3.6 m and undecorated; the mummy's climate-controlled glass case has stood here since 4 Nov 2007 [01 §14–15]): `in the plain, undecorated rock-cut antechamber, about eight by three and a half metres, rough pale walls, a low glass climate case on a plinth, and through an opening in the far wall the painted golden-yellow burial chamber glowing beyond` [verify the modern opening, platform and barrier layout]

**Lighting variants:**
- `LOC_KV62_BURIAL_2033_BLACKOUT` (Seq 8): `the tomb's lights dead; lit only by handheld torches and one red headlamp, hard white beams sweeping the painted walls, deep black beyond, warm bounce off the yellow ground` + GRADE_UNDERGROUND
- `LOC_KV62_BURIAL_2033_EMERG`: `a single battery work lamp standing on the floor, harsh white light from below throwing tall shadows up the paintings`
- `LOC_KV62_BURIAL_2033_SUNSET` (coda): `the tomb lights on, low and warm, a faint gold glow of sunset reflected down the entrance corridor, calm and quiet`

**Geography lock:** we enter from the antechamber (south); the painted north wall faces camera; the Treasury doorway is at frame right [verify]. The painted king's eye, the start of the break, sits **right of centre, about 2.1 m up**.

**PLATE — establishing, 16:9:**
Cinematic still inside a small rock-cut ancient Egyptian burial chamber at night during a power cut, with no people. Its walls are painted on a faded golden-yellow ground with large flat figures, freckled with small dark brown spots; on the far wall a priest in a leopard skin touches an adze to a white-wrapped royal figure. An empty quartzite sarcophagus under a glass top stands at the centre beside a low wooden viewing platform with a rail. The only light is a hard white torch beam from the doorway sweeping the painted wall; deep black beyond. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 31. LOC_KV62_NORTH_CORRIDOR — the rubble-packed corridor (Seq 8.3: "It is I who hinder the sand…")

**Real anchor:** the 2026 survey described "a rubble-packed corridor ~2 m wide leading away from the burial chamber" [01 §14] (disputed). Tut quotes the real Anubis-shrine brick [01 §17].

**Production spec (fiction):**
- 2.0 m wide, 2.1 m high and about 24 m long, sloping gently down to the north.
- The first 4 m are packed floor to ceiling with limestone rubble and mortar, dug out by hand.
- Beyond that, the corridor is open, with rough chisel-marked walls, flint nodules and no decoration.

**LONG:** a narrow rock-cut corridor about two metres wide and two metres high, sloping gently down into darkness, its rough pale limestone walls scarred with ancient chisel marks and flint nodules, undecorated; the first stretch packed floor to ceiling with limestone rubble and mortar, half dug out by hand, dust hanging in the air

**SHORT:** a narrow undecorated rock-cut corridor two metres wide, rough chisel-marked pale limestone, half-cleared of packed rubble, dust in the air

**Lighting variants:**
- `LOC_KV62_NORTH_CORRIDOR_TORCH`: `lit only by head torches and handheld torches: narrow white beams full of dust, hard falloff to black` + GRADE_UNDERGROUND
- `LOC_KV62_NORTH_CORRIDOR_DRILL`: `fine dust sifting from the ceiling with each grinding pulse from above, the torch beams thick with it`

**PLATE — establishing, 16:9:**
Cinematic still inside a narrow rock-cut corridor about two metres wide and two metres high, sloping gently down into darkness beneath a desert valley, with no people. Its rough pale limestone walls are scarred with ancient chisel marks and flint nodules and carry no decoration. The near stretch is packed floor to ceiling with limestone rubble and mortar, half dug out by hand, a gap at the top opening into black. A single white torch beam full of hanging dust. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 32. LOC_KV62_HEART_CHAMBER — the heart chamber (Seq 8.4–8.6: "They did not hide me from it. They sent me to it.")

**Real anchors:**
- Egyptian blue shows strong near-infrared luminescence, with an emission peak around 910 nm when excited by visible light, and it is detectable even when covered [16 §10; 15 §5.2].
- Adaeze's rig: a converted camera with the IR-cut filter removed and a 780 nm pass filter, plus a red headlamp (bible §7, 8.4; PROP_CONSERVATION_KIT).
- ⟂ **Writing meant for machine eyes** is fiction: "To the one who reads this: you are not the first. Weigh your heart." (COMP, through Nour's voice.)

**Production spec (fiction):**
- A chamber about 4.0 × 3.2 m and 2.4 m high at the end of the north corridor.
- Its walls and ceiling lie under a pale, blank skim of ancient gypsum plaster. To the eye it shows **nothing**.
- A square niche, 60 × 60 × 50 cm, sits at chest height in the far (north) wall, on a mud-plaster ledge. It holds PROP_HEART_VESSEL (V-TOMB).
- SESHAT's drill breaks through the ceiling near the south-east corner (UNIT_DRILL, bore 60 cm).

**LONG:** a small rock-cut chamber about four by three metres with a low ceiling, its walls covered in a pale, blank skim of ancient gypsum plaster, cracked, dusty and faintly uneven; at the centre of the far wall a square niche at chest height with a mud-plaster ledge; the air thick and still, fine dust on every surface

**SHORT:** a small low rock-cut chamber, its walls under a blank cracked skim of pale ancient plaster, a square niche in the far wall

**State add-ons:**
- `BORE` (copied verbatim from file 02 §14.3): `a neat round hole 60 centimetres across in the chamber ceiling, pale dust raining from it`
- `COLLAPSE` (8.6, VFX-ASSIST): `chunks of plaster and rock falling from around the widened hole in the ceiling, dust billowing`
- `IR_VIEW` (the tablet image; COMP): the plate shows the wall under red light. The tablet screen carries the white-glowing writing as a COMP overlay.

**Lighting variants:**
- `LOC_KV62_HEART_CHAMBER_TORCH`: `white head-torch beams and handheld torches, hard falloff to black, dust motes turning in the beams` + GRADE_UNDERGROUND
- `LOC_KV62_HEART_CHAMBER_RED` (8.4, the reveal): `the whole chamber flooded deep red by a single red headlamp, every other light off, faces barely visible`
- `LOC_KV62_HEART_CHAMBER_GLOW` (8.5, G0 → G1): `in darkness, a warm amber-gold glow spilling through fabric at chest height, the only light on the faces around it`

**Geography lock:** we enter from the corridor (south); the niche is centred in the far wall; the bore is at the **upper right** of frame.

**PLATE — establishing, 16:9:**
Cinematic still inside a small, low rock-cut chamber deep underground, about four by three metres, with no people. Its walls and ceiling are covered in a pale, blank skim of ancient gypsum plaster, cracked, dusty and faintly uneven. At the centre of the far wall is a square niche at chest height with a mud-plaster ledge. Fine dust lies on every surface and hangs in the air. Lit only by one hard white torch beam from the doorway, with deep black shadows. Silent, sealed, expectant. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## G. THE RAILWAY AND AMARNA (Seq 9: 6 Nov by day → 7 Nov dawn)

## 33. LOC_LUXOR_RAIL_YARD — the Luxor railway yard (Seq 9.1, the daylight hide-and-seek)

**Real anchor:** Egypt's railways carry about 800 million passengers a year, and new ETCS signalling is being fitted [14 §4.5]. A pre-network 1970s engine plausibly has no module. The yard itself is production spec and generic: never the real Luxor station building.

**LONG:** a dusty provincial railway yard, a fan of parallel tracks on brown ballast, rusting goods wagons and faded passenger coaches on sidings, a long open-sided maintenance shed of steel posts and corrugated roofing, oil drums, a diesel fuel tank on stilts, date palms, and pale hills hazy in the distance

**SHORT:** a dusty provincial railway yard of parallel tracks, rusting wagons and faded coaches on sidings, an open-sided corrugated maintenance shed

**Area add-ons:**
- `INSPECTION_PIT` (9.1): `down in a narrow concrete inspection pit beneath a dead modern trainset inside the shed, oil-black walls, the train's underside just overhead, blades of hard daylight at the pit's ends`
- `ENGINE_ROOM` (9.1): `inside the hot, cramped engine room of an old diesel locomotive, a huge grimy engine block, pipes and valves, an oily steel grating floor, daylight through a grimy porthole`

**Lighting variants:**
- `LOC_LUXOR_RAIL_YARD_DAY`: `hard midday sun, a bleached sky, deep black shade under the shed and between the wagons, heat shimmer over the rails` + GRADE_2033_DAY
- `LOC_LUXOR_RAIL_YARD_DUSK`: `warm light fading to blue at dusk, the sun gone behind the western hills, a locomotive headlamp flickering on`

**Geography lock:** the shed is at frame left; the fly sweeps the shed roofs from right to left while the jackal checks the wagons in the foreground. The diesel (PROP_DIESEL_LOCO) stands on the far siding, frame right, facing north (the way out).

**PLATE — establishing, 16:9:**
Cinematic midday still of a dusty provincial railway yard in Upper Egypt, with no people: a fan of parallel tracks on brown ballast, rusting goods wagons and faded passenger coaches on sidings, a long open-sided maintenance shed of steel posts and corrugated roofing, oil drums and a diesel fuel tank on stilts. Date palms, and pale hills hazy in the distance. Hard sun, a bleached sky, deep black shade under the shed, heat shimmer over the rails. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 34. LOC_NIGHT_TRAIN — the night train through the cane fields (Seq 9.2)

**Real anchor:** the Upper Egyptian sugar-cane belt, with the cane tall before the winter harvest [verify: about 3–4 m in November]. The locomotive and coach are PROP_DIESEL_LOCO and PROP_TRAIN_COACH.

**LONG:** a single railway track running dead straight through a sea of tall sugar cane higher than a man on both sides, a narrow gravel embankment, telegraph poles leaning at intervals, an irrigation canal glinting alongside, dark mud-brick villages and palm clumps beyond the cane, a flat horizon under a vast sky

**SHORT:** a single straight railway track through tall sugar cane higher than a man on both sides, leaning telegraph poles, a flat horizon

**Area add-ons:**
- `COACH_INTERIOR`: `inside a dark, rattling 1970s passenger coach, worn green vinyl bench seats, cracked square windows, cane whipping past outside`
- `ROOF`: `on the swaying steel roof of the coach, vents and rivets, the cane a black blur below`
- `COUPLING` (Fathi uncouples; close coverage only): `at the heavy steel coupling between locomotive and coach, the sleepers a blur below`
- `CAB`: `inside the locomotive's cramped cab, analogue gauges, a worn throttle lever, the headlamp beam ahead through the windscreen`
- `ENGINE_ROOM` (moving): `in the shaking, deafening engine room of the old locomotive, the engine block hammering, pipes and valves, a hand torch the only light`

**Lighting variants:**
- `LOC_NIGHT_TRAIN_NIGHT`: `night with no lights anywhere but the locomotive's single blazing headlamp boring a white tunnel through the cane, and the white pinpoints of chasing drones` + GRADE_NIGHT_ACTION
- `LOC_NIGHT_TRAIN_BLUE` (9.2, the powder; VFX-ASSIST): `a cloud of fine blue powder swirling in the headlamp beam and the drones' lights`

**Geography lock:** the train runs **north = frame left** in side tracking shots (the opposite of the southbound river). The jackal rides the coach roof and comes forward, right to left. The flies chase from frame right.

**PLATE — establishing, 16:9:**
Cinematic night still from a low angle beside a single railway track running dead straight through a sea of tall sugar cane higher than a man on both sides. A narrow gravel embankment and leaning telegraph poles recede to a flat horizon; an irrigation canal glints alongside. Far down the line, a single blazing locomotive headlamp approaches, boring a white tunnel of light through the cane. No other lights anywhere, a dense star field above. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## 35. LOC_DEIR_MAWAS — Deir Mawas station (Seq 9.3: two hundred shabti on the tracks; the derailment)

**Real anchors:**
- Deir Mawas lies on the west bank opposite Amarna (bible §7, 9.3).
- Amarna's sacred territory, about 16 × 13 km and marked by 14–16 rock-cut boundary stelae, **includes the west bank** [02 §3].
- The station is a small provincial halt on the main valley line [verify its layout]. It is production spec here.

**LONG:** a small provincial railway station on a flat plain: a low platform beside a double track, a single-storey station building of ochre-washed plaster with arched windows and green shutters, a footbridge of rusting steel, a level crossing with dead barrier arms, cane fields and palms around, and far to the east a line of pale cliffs

**SHORT:** a small provincial station on a flat plain, a low platform, an ochre single-storey building with arched windows, cane fields and distant cliffs

**State add-ons:**
- `SHABTI_ON_TRACKS` (VFX-EXTEND): combine with UNIT_SHABTI as "hundreds of [SHORT] standing in silent rows on the tracks receding into the dark" (file 02 §0.5)
- `DERAILED` (VFX-ASSIST): `the locomotive derailed and lying on its side in the cane beyond the platform, smoke and dust in its headlamp, the tracks strewn with white ceramic shards`

**Lighting variants:**
- `LOC_DEIR_MAWAS_NIGHT`: `blackout night: the station dark, the locomotive's headlamp the only key light, and far to the east small carved shrines in the cliff face picked out white by floodlights` + GRADE_NIGHT_ACTION

**Geography lock:** the train enters from frame right, heading north (frame left). The cliffs and the lit stelae lie across the river, in the background to the east.

**PLATE — establishing, 16:9:**
Cinematic night still of a small provincial railway station on a flat plain during a blackout, with no people: a low platform beside a double track, a single-storey station building of ochre-washed plaster with arched windows and green shutters, a rusting steel footbridge, a level crossing with dead barrier arms, and cane fields and palms around. Far to the east, a line of pale cliffs where a few small carved rock shrines are lit white by distant floodlights. A starry sky. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 36. LOC_AMARNA_PLAIN_2033 — the Amarna plain, the boundary stelae and the Garden in the Great Aten Temple (Seq 6.5 from the river; 9.4–9.8)

**Real anchors [02 §3]:**
- Modern Tell el-Amarna, on the east bank in Middle Egypt.
- The city core ran 6–7 km along the east bank on a north–south "Royal Road". Population estimates are 20,000–50,000.
- The sacred territory was marked by **14–16 rock-cut boundary stelae** cut into the cliffs, about 16 × 13 km including the west bank. Some stelae bear statues of the royal family.
- The Great Aten Temple enclosure measures about **800 × 300 m** (some sources 900 × 300). It was open to the sky and packed with offering tables. Barry Kemp's Amarna Project has been re-excavating it since 2012.
- The plain is a crescent of desert enclosed by cliffs cut by wadis [verify the bay's dimensions]. Whether the temple's outline is marked on the ground with modern blocks is [verify].
- Bioarchaeology found no epidemic spike at Amarna [02 §9].
- ⟂ The 2033 Garden fills the temple's ancient grid of offering tables.

**LONG:** a wide flat crescent of pale desert plain on the east bank of the Nile, enclosed by a long wall of sheer limestone cliffs cut by dry wadis; across it lie the low, sand-softened outlines of an ancient city's mud-brick walls and the vast rectangle of a ruined temple enclosure; far up on the cliff face, a tall round-topped stela is carved into the rock

**SHORT:** a flat pale desert plain ringed by sheer limestone cliffs, the low sand-softened outlines of an ancient mud-brick city and a vast ruined temple enclosure

**Area add-ons:**
- `GARDEN` (VFX-EXTEND of one approved plate, bible §7, 9.4): `inside the ruined temple enclosure, long rows of white fabric sun-shades on slim poles over thousands of sleeping adults on white mats laid across an ancient grid of low offering-table bases, blue cornflowers planted in rows between them`
- `STELA`: `at the foot of the cliffs below a tall round-topped stela carved into the rock face, flanked by weathered rock-cut statues`
- `FERRY`: `at the small ferry landing of a riverside village, date palms and mud-brick houses at the water` (the ferry is PROP_CAR_FERRY)

**Lighting variants:**
- `LOC_AMARNA_PLAIN_2033_MIDDAY` (6.5, from the river): `hard white midday sun, heat shimmer, a bleached sky, the white sun-shades blazing in the distance`
- `LOC_AMARNA_PLAIN_2033_NIGHT` (9.4–9.8, about 23:00): `night: the Garden softly lit from beneath the white shades by low white lamps, a glowing field in the dark plain, the stelae on the cliffs lit white by floodlights, a dense star field` + GRADE_GARDEN

**Safety:** sleepers are **adults** in every prompt. Nurses (UNIT_NURSE) only draw up blankets and pour water (file 02 §3).

**Geography lock:** from the river, the plain opens **frame left to right**, with the cliffs behind. In the Garden, the rows run **away from camera** toward the cliffs. Tut walks down a row toward camera. The father enters from the far end.

**PLATE — establishing, 16:9 (the approved Garden plate):**
Cinematic night still of a wide flat desert plain enclosed by sheer limestone cliffs. Inside the low, sand-softened outline of a vast ruined ancient temple enclosure, long rows of white fabric sun-shades on slim poles stretch away toward the cliffs, softly lit from beneath by low white lamps. Beneath them sleeping adults lie on white mats laid across an ancient grid of low stone offering-table bases, with blue cornflowers planted in rows between them. Far up on the cliff face, a tall round-topped carved stela glows white under floodlights. A dense star field. Serene and eerie. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 37. LOC_QUARRY — the abandoned limestone quarry (Seq 9.9 dawn; the Seq 10 opening at sunset: "The First Hour")

**Production spec:** an abandoned limestone quarry at the desert edge in Middle Egypt. Stepped white cut faces carry the parallel scoring of wire saws. There are spoil heaps, a rusting stone-cutting machine and tyre tracks in white dust. A small battered farm truck sits under a dusty tarpaulin (PROP_FARM_TRUCK, file 04 §20).

**LONG:** an abandoned limestone quarry at the desert edge, tall stepped walls of chalk-white rock scored with parallel saw marks, spoil heaps and loose rubble, a rusting stone-cutting machine left on a bench, tyre tracks in white dust, and a small battered farm truck half hidden under a dusty tarpaulin

**SHORT:** an abandoned limestone quarry of chalk-white stepped walls scored with saw marks, rubble heaps, a battered farm truck under a tarpaulin

**Lighting variants:**
- `LOC_QUARRY_DAWN`: `cold blue dawn, the white walls pale grey, the first sun catching only their top edge`
- `LOC_QUARRY_DAY`: `brutal white glare bouncing off the rock, figures pressed into thin strips of shade`
- `LOC_QUARRY_SUNSET`: `the sun touching the western rim, the white walls turned deep orange, long blue shadows across the floor` + GRADE_GOLDEN

**PLATE — establishing, 16:9:**
Cinematic sunset still of an abandoned limestone quarry at the desert edge, with no people. Tall stepped walls of chalk-white rock are scored with parallel saw marks above spoil heaps and loose rubble; a rusting stone-cutting machine stands abandoned on a bench; tyre tracks cross the white dust. A small battered farm truck sits half hidden under a dusty tarpaulin. The sun touches the western rim, turning the walls deep orange, with long blue shadows. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## H. SAQQARA (Seq 10: 7 Nov, sunset → 22:30; cards THE FOURTH HOUR · THE FIFTH HOUR)

## 38. LOC_DESERT_ROAD — the desert road (Seq 10–11: the farm truck; Saqqara to Giza)

**Production spec:** a divided highway across the Western Desert, generic and unnamed. It has two lanes each way split by a low concrete barrier, dead lamp posts, gravel shoulders drifting with sand, a line of high-voltage pylons, and low dunes and stony plain on either side.

**LONG:** a straight divided desert highway running to the horizon across flat stony desert, two lanes each way split by a low concrete barrier, tall dead lamp posts at intervals, gravel shoulders drifting with sand, a line of high-voltage pylons marching parallel, and nothing else but low dunes and sky

**SHORT:** a straight divided desert highway across flat stony desert, a low concrete median barrier, dead lamp posts and a line of power pylons

**Lighting variants:**
- `LOC_DESERT_ROAD_NIGHT`: `night, no lights anywhere but the truck's own headlights on the road and, far ahead on the horizon, a white glow of floodlights over the pyramids` + GRADE_NIGHT_ACTION
- `LOC_DESERT_ROAD_DUSK`: `the last violet light of dusk in the west, the road grey, the pylons in silhouette`

**PLATE — establishing, 16:9:**
Cinematic night still of a straight divided desert highway running to the horizon across flat stony desert, with no vehicles: two lanes each way split by a low concrete barrier, tall dead lamp posts at intervals, gravel shoulders drifting with sand, and a line of high-voltage pylons marching parallel. Far ahead on the horizon, a white glow of floodlights. A dense star field over total darkness. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 39. LOC_SAQQARA — the Saqqara plateau and the Step Pyramid (Seq 10.1; the service-tunnel mouth at 10.4)

**Real anchors:**
- Saqqara is the necropolis of Memphis; the bible calls it "Sokar's necropolis" (§5).
- The **Step Pyramid** was built c. 2670 BC in six stepped tiers, about 62 m high on a base of about 109 × 125 m [verify]. It was restored and reopened in 2020 [verify].
- Its **enclosure wall** is of fine white limestone with recessed panelling, about 10 m high and about 1.6 km round [verify].
- The **Serapeum** lies in the desert north-west of the Step Pyramid [07 E1; verify its position].
- In the film: SESHAT's floodlights and a winch over the Serapeum (bible §7, 10.1).

**LONG:** a vast desert plateau of pale sand and rubble mounds at the edge of the Nile valley, dominated by an ancient stepped pyramid of six great stone tiers about sixty metres high, weathered and patched with restored masonry, behind a long enclosure wall of fine white limestone panelled with tall recessed niches

**SHORT:** a desert plateau dominated by an ancient six-tiered stepped pyramid about sixty metres high behind a long white panelled limestone enclosure wall

**Area add-ons:**
- `SERAPEUM_HEAD`: `in the open desert at the head of a rock-cut ramp descending underground, a steel winch frame on tracks standing over it`
- `TUNNEL_MOUTH` (10.4): `at a low rough-cut opening in a sand slope where an old service tunnel comes out into the desert`

**Lighting variants:**
- `LOC_SAQQARA_SUNSET`: `the sun low in the west, the pyramid's steps glowing deep orange-gold with long blue shadows, the green edge of the Nile valley darkening to the east` + GRADE_GOLDEN
- `LOC_SAQQARA_NIGHT` (20:00): `night: a few hard white floodlights on masts around a winch, the pyramid a dark stepped silhouette against a dense star field, no city glow anywhere on the horizon` + GRADE_NIGHT_ACTION

**PLATE — establishing, 16:9:**
Cinematic sunset still of a vast desert plateau of pale sand and rubble mounds at the edge of the Nile valley, with no people. An ancient stepped pyramid of six great stone tiers, about sixty metres high, weathered and patched with restored masonry, rises behind a long enclosure wall of fine white limestone panelled with tall recessed niches. The low sun turns the steps deep orange-gold, with long blue shadows; to the east the green edge of the valley darkens. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## 40. LOC_SERAPEUM_LESSER — the collapsed Lesser Vaults (Seq 10.2, the way in)

**Real anchors [07 E1]:** the Lesser Vaults were dug under Khaemweset, son of Ramesses II. They collapsed, and conservation work on them resumed in 2020. The Serapeum as a whole was closed after the 1992 earthquake and reopened in 2012.

**LONG:** a low, older rock-cut catacomb passage half collapsed, its ceiling fallen in great slabs of fractured limestone that choke the way, timber props and steel shoring jammed under cracked rock, sand drifted over rubble, a narrow crawl-space between fallen blocks leading on into blackness

**SHORT:** a low half-collapsed rock-cut catacomb passage choked with fallen limestone slabs, timber props and steel shoring, a narrow crawl-space beyond

**Lighting variants:**
- `LOC_SERAPEUM_LESSER_TORCH`: `lit only by head torches: white beams on fractured rock and drifting dust, hard black beyond` + GRADE_UNDERGROUND

**PLATE — establishing, 16:9:**
Cinematic still inside a low, ancient rock-cut catacomb passage, half collapsed, with no people. Great slabs of fractured limestone have fallen from the ceiling and choke the way; timber props and steel shoring are jammed under the cracked rock; sand has drifted over the rubble. A narrow crawl-space between the fallen blocks leads on into blackness. A single white torch beam and drifting dust. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 41. LOC_SERAPEUM_GREATER — the Serapeum Greater Vaults and the pit (Seq 10.2–10.4)

**Real anchors [07 E1]:**
- The Serapeum was the burial catacomb of the Apis bulls. Mariette entered it in November 1851.
- The Greater Vaults were begun under Psamtik I (664–610 BC) and extended in the Ptolemaic period to **about 350 m**, with a **parallel service tunnel**.
- From Amasis II to the end of the Ptolemies the sarcophagi were of hard stone (Aswan granite, "grey granite", diorite, limestone), **"weighing as much as 62 tonnes each, including the lid."**
- **24 survive.** Only four are inscribed:
  - Amasis II's, of red granite, panelled with Pyramid-Text spells coloured green;
  - Cambyses II's, which **blocks the original entrance**;
  - Khabash's;
  - one with empty cartouches.
- Every tomb but two was plundered.
- Installation was documented engineering: roller tracks, eight-lever winches, and sand-filling of the chambers. A stela records **28 days** to install one box. **The last box was abandoned in the service tunnel.**
- Box dimensions are [verify, often quoted at about 4 × 2.3 × 3.3 m]. The gallery's height and the modern walkway are [verify].
- ⟂ The weighed core was decommissioned piece by piece into the boxes; its glass heart waits in a charged pit at the gallery's end (UNIT_GLASS_SERPENT; file 02 §12).

**LONG:** a long, straight rock-cut underground gallery in pale limestone, its rough vaulted ceiling about five metres high, lined on both sides by deep side chambers, each holding a colossal box of dark polished granite with a massive lid, set down in a pit below the floor; a timber walkway with railings runs the gallery's length into darkness

**SHORT:** a long rock-cut underground gallery lined with side chambers, each holding a colossal polished dark granite box sunk below the floor

**Area add-ons:**
- `PIT` (10.2): `at the gallery's far end, where a freshly opened pit in the stone floor is ringed by work lights and a steel lifting frame`
- `RED_BOX`: `beside a colossal red granite box whose sides are panelled with faint columns of carved signs tinted green`
- `ENTRANCE_BOX`: `where a colossal granite box sits wedged across the old doorway, blocking it`

**State add-ons:**
- `SAND_TRAP` (10.2, VFX-ASSIST): `a torrent of pale sand bursting from a hidden chamber in the wall and pouring across the floor`
- `DUST_FIGHT` (10.4): `the air thick with stone dust and drifting blue powder`

**Lighting variants:**
- `LOC_SERAPEUM_GREATER_WORKLIGHTS` (10.2): `harsh white work lights on stands at the far end, the gallery falling away into black, dust hanging in the beams` + GRADE_UNDERGROUND
- `LOC_SERAPEUM_GREATER_TORCH`: `only torch beams and small red and amber machine lights, the polished granite catching long reflections`
- `LOC_SERAPEUM_GREATER_BLUE` (10.4): `a cloud of fine blue powder hanging in the torch beams between the granite boxes`

**Geography lock:** we enter from the Lesser Vaults end (frame left in lateral shots) and look down the gallery toward the pit, which is lit at the far end. The service-tunnel door is on the **right-hand** wall near the pit. The dozens of standing shabti occupy the side-chamber mouths on both sides.

**PLATE — establishing, 16:9:**
Cinematic still down a long, straight rock-cut underground gallery in pale limestone, its rough vaulted ceiling about five metres high, with no people. On both sides, deep side chambers each hold a colossal box of dark polished granite with a massive lid, set down in a pit below the floor level. A timber walkway with railings runs the length of the gallery into darkness; at the far end, harsh white work lights on stands glow around a freshly opened pit in the floor. Dust hangs in the beams. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 42. LOC_SERAPEUM_SERVICE_TUNNEL — the service tunnel and the abandoned box (Seq 10.4: "They ran out of centuries")

**Real anchors [07 E1]:**
- A parallel service tunnel runs beside the gallery. In 1853 Brugsch saw the "double-rails" still on the Ptolemaic tunnel floor.
- **The last box was abandoned in the service tunnel.** Whether it has its lid is [verify].

**LONG:** a narrower parallel rock-cut service tunnel of rough pale limestone, two worn grooves like old rails running along its floor, and halfway along it a colossal dark granite box abandoned in the passage, filling it almost wall to wall, leaving a gap just wide enough to squeeze past

**SHORT:** a narrow rough rock-cut service tunnel with worn rail grooves in the floor, a colossal granite box abandoned in it, almost blocking the way

**Lighting variants:**
- `LOC_SERAPEUM_SERVICE_TUNNEL_TORCH`: `lit only by a swinging hand torch and a warm glow at chest height, long shadows along the grooves` + GRADE_UNDERGROUND

**PLATE — establishing, 16:9:**
Cinematic still inside a narrow, rough rock-cut service tunnel of pale limestone, with no people. Two worn grooves like old rails run along its floor. Halfway along, a colossal box of dark granite stands abandoned in the passage, filling it almost wall to wall and leaving a gap just wide enough to squeeze past. A single hand-torch beam rakes along the grooves. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## I. GIZA (Seq 11–12: 8 Nov, 00:00–06:14; the Amduat hours)

## 43. LOC_GIZA_PLATEAU — the Giza plateau at midnight, a fortress (Seq 11.1; the Wall of the Crow, the causeway, the Sphinx enclosure)

**Real anchors:**
- **The Great Pyramid** [07 A1]:
  - original height 146.6 m, now 138.5 m; base 230.3 m square; 203 courses survive;
  - the lowest course is 148 cm high and the top courses barely 50 cm;
  - it was cased in white Tura limestone, stripped after 1356; a few casing stones survive at the base of the north face.
- **The Sphinx** is carved from the plateau's Mokattam limestone, in alternating hard and soft beds, in Khafre's reign. It sits in a quarried enclosure and faces east; its New Kingdom name is Hor-em-akhet, "Horus in the Horizon" [07 D2; 07 Q9].
- **Khafre's causeway** runs up from the Sphinx and valley temple to his pyramid; the Osiris Shaft lies under it [07 D1]. Khafre's pyramid keeps casing near its top [verify].
- **The Wall of the Crow** is a cyclopean wall south of the Sphinx, fronting the workers' town [07 C2].
- ⟂ SESHAT's floodlit fortress: shabti along the causeway, Sekhmets on the enclosure wall.

**LONG:** the Giza plateau: three great pyramids of weathered limestone rising from a rocky desert plateau, the largest with its stepped courses exposed, the second still capped with smooth casing near its peak; below them a colossal carved lion with a human head crouches in a quarried enclosure, and a long ruined stone causeway climbs from it toward the second pyramid

**SHORT:** the Giza plateau: three great weathered pyramids above a rocky desert, a colossal human-headed lion in its quarried enclosure, a long ruined causeway

**Area add-ons:**
- `WALL_OF_CROW`: `seen from on top of a massive cyclopean wall of rough limestone blocks at the south edge of the plateau, looking north`
- `CAUSEWAY`: `along a long ruined stone causeway climbing the plateau, its paving broken`
- `SPHINX_WALL`: `on the rim of the quarried rock enclosure around the colossal human-headed lion`
- `WESTERN_FIELD`: `among rows of low ruined stone tombs west of the largest pyramid`
- `AERIAL`: `seen from high above at night, the three pyramids small on the dark plateau, the black unlit city pressing to its edge`

**Lighting variants:**
- `LOC_GIZA_PLATEAU_MIDNIGHT_FORTRESS`: `midnight blackout: no city light on the horizon; the plateau ringed by hard white floodlights on masts, the pyramids lit from below, long black shadows across the sand, small drone lights drifting overhead` + GRADE_NIGHT_ACTION

**Geography lock** [verify against a site plan; bearings computed from published site coordinates]: looking north from the Wall of the Crow on a wide lens, the Sphinx enclosure lies ahead at **frame right**, the Great Pyramid rises in the distance at **centre frame**, and the second pyramid, with its causeway climbing toward it from the Sphinx, stands at **frame left**. The Sphinx always faces **east (frame right)**. Shabti on the causeway stand a metre apart with their slits facing outward.

**PLATE — establishing, 16:9:**
Cinematic midnight still of the Giza plateau during a total city blackout, with no people. Three great pyramids of weathered limestone rise from the rocky desert plateau, the largest with its stepped courses exposed, the second still capped with smooth casing near its peak. Below them, a colossal carved lion with a human head crouches in its quarried enclosure, and a long ruined stone causeway climbs from it toward the second pyramid. Hard white floodlights on masts light the monuments from below and throw long black shadows; beyond the plateau, the city is completely dark under a dense star field. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 44. LOC_OSIRIS_SHAFT — the Osiris Shaft (Seq 11.3: the reversed pumps; Tarek's stand; the side tunnel; the builders' crawlway)

**Real anchors [07 D1]:**
- A vertical shaft under Khafre's causeway, midway between the Sphinx and Khafre's pyramid, descending about **30 m in three levels**.
- **Level 1:** an empty chamber about 10 m down.
- **Level 2** (about 20 m): a hall with six or seven side niches, two holding huge basalt or granite sarcophagi.
- **Level 3** (about 30 m): a chamber whose floor is cut into a **channel of water around a central "island"** carrying a sarcophagus lid and the remains of **four pillars**.
- **Small tunnels about 40 × 40 cm** lead off toward the Great Pyramid and the Sphinx and are unexplored.
- It dates to the Late Period (Saite–Persian), with reuse. Selim Hassan recorded it in the 1930s; Hawass pumped it out and excavated it in 1999 (published 2007). It opened to tourists in November 2017. The level-by-level detail is flagged MEMORY in the research [verify].
- ⟂ SESHAT's pumps are reversed to flood the shaft. After eight metres, a side tunnel opens into a builders' crawlway.

**Production spec:** steel ladders and landings between the levels; SESHAT's pump intake and hoses bolted to the rock at the level-3 waterline.

**LONG:** a deep rock-cut shaft descending in three levels beneath the desert: rough limestone walls, steel ladders between landings, a middle hall of dark niches holding huge stone sarcophagi, and at the bottom a flooded chamber where black groundwater fills a channel around a central island bearing a stone coffin lid and four broken pillar stumps

**SHORT:** a flooded rock-cut chamber thirty metres underground, black water in a channel around a central island with a stone coffin lid and pillar stumps

**Area add-ons:**
- `LEVEL_2`: `in the middle hall of the shaft, dark side niches, two holding huge dark stone sarcophagi`
- `PUMP`: `beside a steel pump intake and thick black hoses bolted to the rock at the waterline`
- `SIDE_TUNNEL`: `at the mouth of a tiny square tunnel forty centimetres wide cut into the rock at water level`
- `CRAWLWAY`: `inside a cramped rough-hewn builders' crawlway barely higher than a crouching man, tool marks on every surface`

**Water-level states (continuity; append one):**
- `W0`: `the water only in its channel around the island`
- `W1`: `the water spreading knee-deep across the whole floor`
- `W2`: `the water chest-deep and rising, churning at the pump intake`
- `W3`: `the water a hand's breadth from the ceiling, torchlight rippling on the rock above`

**Lighting variants:**
- `LOC_OSIRIS_SHAFT_TORCH`: `lit only by head torches and one torch dropped under the water: white beams on wet rock, green-black water, reflections rippling across the ceiling` + GRADE_UNDERGROUND
- `LOC_OSIRIS_SHAFT_FLOOD` (VFX-ASSIST): `water churning and rising fast, spray in the torch beams, the light breaking into shards on the surface`

**Safety:** Tarek goes under shown as a **hand, water and sound** (file 05 §7). The face is never shown underwater.

**PLATE — establishing, 16:9:**
Cinematic still at the bottom of a deep rock-cut shaft thirty metres underground, with no people: a flooded chamber of rough limestone where black groundwater fills a channel around a central island bearing a weathered stone coffin lid and four broken pillar stumps. A steel ladder descends from a landing above; a steel pump intake and thick black hoses are bolted to the rock at the waterline. A single white head-torch beam from above; reflections ripple across the ceiling. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## THE GREAT PYRAMID INTERIOR (Seq 11.4–12.7)

**Real anchors for the interior [07 A1, A5, B2]:**
- The King's Chamber is 10.5 × 5.2 m, lined with granite.
- The Queen's Chamber shafts are **20 × 20 cm**.
- The **Big Void** (2017) is at least 30 m long, with a cross-section similar to the Grand Gallery's, and lies above it.
- The **North Face Corridor** is about 9 m long and about 2 × 2 m in section, with a chevron ceiling. It was seen by endoscope on 2 March 2023.
- The passage and chamber figures below come from the Great Pyramid source mirror in the research bundle (`research/src07/wiki_great_pyramid.txt`, cited **[07 src]**), which summarises the standard surveys. They are secondary figures: keep [verify] on any number a line of dialogue quotes.
- In the film's 2033 blackout, all the pyramid's electric lighting is dead.

## 45. LOC_GP_SUBTERRANEAN — the Subterranean Chamber (Seq 11.4)

**Facts [07 src]:**
- The only chamber cut into the bedrock, about **27 m below base level**. It measures about **14.1 m east–west by 8.4 m north–south** (27 × 16 cubits) and is about **4 m high**.
- The western half, apart from the ceiling, is **unfinished**: the quarrymen's trenches still run east–west across the floor. A niche is cut into the northern half of the west wall.
- The only access is the horizontal passage from the Descending Passage (8.84 m long, 85 cm wide, 91–95 cm high), which enters at the **east end of the north wall**.
- A **blind corridor** runs straight south for 11 m, then 5.4 m more with a slight bend, about 0.75 m square.
- In the middle of the eastern half is the **Pit** (Perring's Shaft): an ancient hollow about 2 m square, which Vyse had sunk to about 15 m in 1837 looking for Herodotus's island. It was partly backfilled in 1909.
- The chamber was rediscovered in 1817, when Caviglia cleared the Descending Passage.
- Production: an iron railing around the pit [verify the modern fittings].

**LONG:** an unfinished chamber cut deep in the bedrock beneath a pyramid, about fourteen by eight metres and four metres high, its ceiling roughly flat, its floor a jagged unfinished landscape of stepped ridges and trenches in raw grey-brown rock, a deep square pit in the eastern half ringed by an iron railing, a low blind passage leading off into black

**SHORT:** an unfinished bedrock chamber deep beneath a pyramid, a roughly flat ceiling, a jagged stepped rock floor and a railed pit

**Lighting variants:**
- `LOC_GP_SUBTERRANEAN_TORCH`: `lit only by head torches and a warm glow at chest height: white beams on raw rock, hard black beyond` + GRADE_UNDERGROUND

**PLATE — establishing, 16:9:**
Cinematic still inside an unfinished chamber cut deep in the bedrock beneath a pyramid, about fourteen by eight metres and four metres high, with no people. Its ceiling is roughly flat; its floor is a jagged unfinished landscape of stepped ridges and trenches in raw grey-brown rock, with a deep square pit ringed by an iron railing on one side and a low blind passage leading off into black. A single white torch beam from the entrance passage. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 46. LOC_GP_WELL_SHAFT — the Well Shaft (Seq 11.4)

**Facts [07 src]:**
- The Well (Service) Shaft links the **lower end of the Grand Gallery** to the **bottom of the Descending Passage**, about 50 m further down, by a winding, indirect course.
- The upper half runs through the core masonry: vertical for 8 m, then angled south for about the same, reaching bedrock about 5.7 m above base level. A further vertical section, partly masonry-lined, breaks through into the **Grotto**, a natural limestone cave that was probably filled with sand and gravel before construction and later hollowed out by looters. A granite block, probably from the King's Chamber portcullis, lies in it.
- The lower half runs through bedrock at about 45° for 26.5 m, then down a steeper 9.5 m section, then along a final, almost horizontal 2.6 m into the Descending Passage. The builders evidently had trouble aligning the lower exit.
- It is usually explained as ventilation for the Subterranean Chamber and an escape route for the workers who slid the plugs down the Ascending Passage.
- Its cross-section, about 70 cm square, is [verify]. It has no scene heading in the current pages (§1.1).

**LONG:** a cramped, irregular shaft about seventy centimetres square, dropping near-vertically through courses of masonry, then slanting steeply down through raw fissured bedrock, crude footholds cut in its sides, a small cave-like grotto opening off it partway down, fine grit trickling from far above

**SHORT:** a cramped irregular shaft seventy centimetres square dropping steeply through masonry and fissured bedrock, crude footholds in its sides

**Lighting variants:**
- `LOC_GP_WELL_SHAFT_TORCH`: `a single head-torch beam straight up or down the shaft, the walls close and grey, everything beyond the beam black` + GRADE_UNDERGROUND

**PLATE — establishing, 9:16 vertical (use as a 16:9 crop or a tilt plate):**
Photoreal still looking straight down a cramped, irregular shaft about seventy centimetres square, dropping near-vertically through courses of ancient masonry and then slanting steeply through raw fissured bedrock, with crude footholds cut into its sides. Partway down, a small cave-like grotto opens off one side. Fine grit trickles past. A single head-torch beam from above fades into black. Claustrophobic. Photoreal live-action film still, 18mm lens, fine film grain. Aspect ratio 9:16.

---

## 47. LOC_GP_DESCENDING — the Descending Passage (Seq 11.4: the work gang holds the passage)

**Facts [07 src]:**
- **1.0 m wide** (2 cubits) and **1.20 m high** (4 Egyptian feet, measured square to the slope), descending at **26°26′46″**, a rise over run of 1 to 2.
- From the original entrance on the north face it runs **28 m** through the masonry to the square hole in its ceiling where the granite-plugged Ascending Passage begins. The robbers' tunnel meets it here by a short bypass cut round the plugs.
- It then descends a further **72 m through bedrock**. Near its lower end, on the west wall, the Well Shaft comes in.
- A horizontal passage (8.84 m long, 85 cm wide, 91–95 cm high) leads on to the Subterranean Chamber.
- Around 1902 a padlocked iron grille-door was fitted in the lower section, and access is usually forbidden. The dead cable and lamp brackets in the lock are production spec [verify].

**LONG:** a long, perfectly straight passage barely a metre wide and chest high, sloping steeply down at twenty-six degrees, first through smooth fitted limestone and then through raw bedrock, its narrow floor worn and gritty, a dead cable and lamp brackets along one wall, its far end a tiny black square

**SHORT:** a long straight passage a metre wide and chest high, sloping steeply down through fitted limestone into bedrock, its far end a black square

**Lighting variants:**
- `LOC_GP_DESCENDING_TORCH`: `lit by torch beams stabbing down the slope and small amber slits in the dark, the square tunnel receding in hard perspective` + GRADE_UNDERGROUND

**Geography lock:** "down" is always **toward camera** in the chase coverage. The work gang holds the passage between camera and the jackal coming from above.

**PLATE — establishing, 16:9:**
Cinematic still looking up a long, perfectly straight ancient passage barely a metre wide and chest high, sloping steeply at twenty-six degrees, with no people. The walls are first raw bedrock, then smooth fitted limestone higher up; the narrow floor is worn and gritty; a dead cable and lamp brackets run along one wall. The far end is a tiny square of black. One torch beam fills the near stretch. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 48. LOC_GP_MAMUN_TUNNEL — Al-Ma'mun's tunnel (Seq 11.2 Fathi's diversion; 11.4 the jackal comes in; the exit at 12.7)

**Real anchors [07 C4; 07 src]:**
- Today's visitor entrance, the "Robbers' Tunnel", is forced into the **6th and 7th courses, about 7 m above the base**. It runs roughly straight and horizontal for **27 m**, then **turns sharply left** to meet the granite blocking stones of the Ascending Passage.
- Tradition credits Caliph al-Ma'mun's workmen, c. AD 820: the noise of a stone falling in the Descending Passage told them which way to turn. Many scholars think an older robbers' tunnel was only cleared and enlarged; a patriarch reported a 33 m breach in the north face before al-Ma'mun.
- The three granite plugs are 1.57 m, 1.67 m and 1.0 m long. A short tunnel dug round them through the softer limestone joins the Descending Passage, and has since been fitted with stairs.
- The soot, the handrail and the dead lamp fittings are production spec [verify].

**LONG:** a rough tunnel hacked by hand through the solid limestone core of a pyramid, running straight into the dark and then turning sharply, its walls irregular, blackened with centuries of soot and polished smooth where hands have brushed them, a worn uneven floor, a modern steel handrail and dead lamp fittings, ending in a cramped cavity beside enormous granite blocks

**SHORT:** a rough hand-hacked tunnel through a pyramid's limestone core, soot-blackened irregular walls, a steel handrail and a worn floor

**Lighting variants:**
- `LOC_GP_MAMUN_TUNNEL_TORCH`: `torch beams and a red machine light moving in the dark, soot-black walls swallowing the light` + GRADE_UNDERGROUND
- `LOC_GP_MAMUN_TUNNEL_DAWN_EXIT` (12.7): `grey-gold dawn light spilling in from the outer opening, dust glowing, the walls warming from black to brown`

**PLATE — establishing, 16:9:**
Cinematic still inside a rough tunnel hacked by hand through the solid limestone core of a pyramid, with no people, running straight into the dark and then turning sharply. Its walls are irregular, blackened with centuries of soot and polished smooth where hands have brushed them; the floor is worn and uneven; a modern steel handrail and dead lamp fittings run along one side. At the inner end, a cramped cavity opens beside enormous granite blocks. One torch beam. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 49. LOC_GP_GRAND_GALLERY — the Grand Gallery (Seq 11.5 the thread and the sliding stone; 12.4 the fight; 12.7 the dawn exit; 9.5b in c. 1332 BC)

**Facts [07 src; bible §7, 11.5]:**
- **46.68 m long and 8.6 m high.** It continues the Ascending Passage's slope (about 26°) and rises **21 m**, from the 23rd to the 48th course.
- **2.1 m (4 cubits) wide at the base.** After two courses (2.29 m up) the walls corbel inward by 6–10 cm a side in **seven steps**, so that the top is only **1.0 m (2 cubits)** wide.
- The roof slabs are laid at a slightly steeper angle than the floor, each set into a notch in the walls like the teeth of a ratchet.
- The floor is a lower central ramp 1.0 m wide between two side shelves 52.4 cm (1 cubit) wide. The shelves carry **56 slots, 28 a side**, and **25 niches** are cut into each wall above them. Their purpose is unknown; one theory is that they held beams restraining the stored granite plugs.
- At the top, the **Great Step** leads onto a small horizontal platform and through the granite Antechamber to the King's Chamber. High on the east wall at the upper end, a hole near the roof leads to the lowest Relieving Chamber.
- Modern fittings: a wooden walkway with cleats and handrails over the central ramp, and lighting strips [verify].
- The Big Void, at least 30 m long with a similar cross-section, lies above it [07 B2].
- ⟂ At the top, a stone slides and a passage goes up (LOC_GP_PASSAGE_ABOVE).

**LONG:** a steep, soaring ancient gallery of polished limestone rising at twenty-six degrees, about forty-seven metres long and eight and a half metres high, its walls stepping inward in seven corbelled courses to a narrow ceiling slot; low stone ramps with paired slots line each side of a central channel, covered by a modern wooden walkway with cleats and handrails

**SHORT:** a steep soaring corbelled limestone gallery rising at twenty-six degrees, eight and a half metres high, a wooden cleated walkway up its centre

**State add-ons:**
- `THREAD`: use UNIT_THREAD SHORT (file 02 §14.1) on the walkway.
- `STONE_SLID` (11.5, VFX-ASSIST): `at the top of the gallery, above the great step, a stone block slid back into the wall, a black opening behind it`
- `ANCIENT_1332` (9.5b memory; "the queen carries the lamp"): `without any modern walkway or fittings, its bare stone ramps and central channel lit by a single oil lamp carried up the slope`

**Lighting variants:**
- `LOC_GP_GRAND_GALLERY_BLACKOUT_TORCH`: `the gallery's lights dead; torch beams slicing up the slope, the corbelled walls catching light in stepped bands, the top lost in black` + GRADE_UNDERGROUND
- `LOC_GP_GRAND_GALLERY_HEART_GLOW`: `lit only by a warm amber-gold glow at chest height moving slowly up the slope`
- `LOC_GP_GRAND_GALLERY_FIGHT` (12.4): `swinging torch beams, small red and amber machine lights, stone dust hanging in the air`
- `LOC_GP_GRAND_GALLERY_DAWN_EXIT` (12.7): `soft grey-gold daylight seeping up from the lower passages, the gallery a dim warm grey`
- `LOC_GP_GRAND_GALLERY_ANCIENT_1332`: `one oil lamp carried up the ramp, its warm gold stepping up the corbelled walls, deep shadow above and below` + GRADE_1332_NIGHT + GRADE_READ_FROM_GLASS (post)

**Geography lock:** "up" is **toward the top of frame and away from camera** in the master (a low angle from the bottom). In the fight intercut, the Reis comes **down** at Fathi; the thread runs up the left side of the walkway.

**PLATE — establishing, 16:9:**
Cinematic low-angle still looking up a steep, soaring ancient gallery of polished limestone rising at twenty-six degrees, about forty-seven metres long and eight and a half metres high, with no people. Its walls step inward in seven corbelled courses to a narrow ceiling slot; low stone ramps with paired slots line each side of a central channel covered by a modern wooden walkway with cleats and handrails. The electric lights are dead; a single torch beam slices up the slope, the corbels catching light in stepped bands, the top lost in black. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 50. LOC_GP_QC_SHAFT — the Queen's Chamber, its south shaft and Gantenbrink's door (Seq 11.5: "Bridge the two")

**Real anchors [07 A5]:**
- **The shaft:** 20 × 20 cm, rising at about 40°.
- **The door:** in 1993 Upuaut 2 climbed about 65 m and found a limestone "door" with two eroded copper "handles". In 2002 a drilled hole showed a second slab behind it.
- **Djedi (2011):** it travelled **63.6 ± 0.4 m** and saw all sides of the **about 23 × 19 cm cavity** behind the first slab.
  - **Red ochre marks** lie on the cavity floor. They are undeciphered, and **Miatello reads them as "121"**, the shaft's length in cubits.
  - The copper pins loop back on themselves.
  - **The back of the door is finished and polished.**
  - A mason's red mark was also seen on the shaft wall.
- **The Queen's Chamber [07 src]:** exactly halfway between the north and south faces; **5.2 m north–south by 5.8 m east–west**, under a pointed (gabled) roof whose apex is **6.3 m** high. A corbelled niche **4.7 m high** stands in the east wall; it was 1 m deep and has been deepened by treasure hunters. A horizontal passage 1.0 m wide and 1.17 m high leads to it from the foot of the Grand Gallery, and steps down near the chamber to 1.68 m high.
- Waynman Dixon found the shafts in 1872 by chiselling into the walls. A diorite ball, a bronze hook and a cedar plank came out of them; the plank is radiocarbon-dated to 3341–3094 BC [07 A5].
- ⟂ Beneath the marks is a line no one has read: *"Bridge the two."* (COMP.)

**LONG:** the inside of a tiny square stone shaft twenty centimetres across, climbing steeply into blackness, its smooth pale limestone walls running straight up, ending at a small polished limestone slab set across the shaft like a door, two corroded copper pins protruding from its face, a faint red ochre mark on the wall beside it

**SHORT:** inside a tiny square limestone shaft twenty centimetres across, ending at a small polished stone slab with two corroded copper pins

**Area add-ons:**
- `QUEENS_CHAMBER`: `in a bare limestone chamber about six metres square with a steeply gabled ceiling and a tall corbelled niche in one wall, a small square shaft opening in the south wall`
- `BEHIND_DOOR` (COMP marks): `in a tiny cavity behind the slab, faint red ochre marks on the floor before a second stone slab`

**Lighting variants:**
- `LOC_GP_QC_SHAFT_INCHWORM`: `lit only by a small ring of cool white LEDs low in the shaft, hard falloff into black, the copper glinting`

**Rules:**
- The marks and the hidden line are **COMP**. In the plate, the marks are "faint red ochre marks".
- The inch-worm is UNIT_INCHWORM (file 02 §7).

**PLATE — establishing, 16:9:**
Photoreal macro still inside a tiny square stone shaft twenty centimetres across, climbing steeply into blackness, its smooth pale limestone walls running straight up. At the end of the shaft, a small polished limestone slab is set across it like a door, with two corroded copper pins protruding from its face; a faint red ochre mark shows on the wall beside it. Lit only by a small ring of cool white LEDs from below, with hard falloff into black. Photoreal live-action film still, 100mm macro, fine film grain. Aspect ratio 16:9.

---

## 51. LOC_GP_PASSAGE_ABOVE — the passage above the Grand Gallery (Seq 11.5 → 12.3; fiction)

⟂ **Fiction:** the stone at the top of the Gallery slides, and "a narrow way climbs steeply". Tut climbs toward Nour's voice (seq_11).

**LONG:** a narrow, steep, never-seen passage climbing through the heart of a pyramid, walls of perfectly fitted pale limestone with hair-thin joints, a floor cut in shallow unworn steps, the air still and dry, the passage turning once before rising toward a low black opening above

**SHORT:** a narrow steep hidden passage of perfectly fitted pale limestone with hair-thin joints, shallow unworn steps rising to a black opening

**Lighting variants:**
- `LOC_GP_PASSAGE_ABOVE_HEART_GLOW`: `black but for a warm amber-gold heartbeat glow at chest height, lighting a metre of stone at a time`

**PLATE — establishing, 16:9:**
Cinematic still inside a narrow, steep, never-seen passage climbing through the heart of a pyramid, with no people. Its walls are perfectly fitted pale limestone with hair-thin joints; its floor is cut in shallow, unworn steps; the air is still. The passage turns once and rises toward a low black opening above. Only a faint warm amber-gold glow at the bottom of frame lights a metre of stone. Photoreal live-action film still, anamorphic 24mm, fine film grain. Aspect ratio 16:9.

---

## 52. LOC_HALL_TWO_TRUTHS — the Hall of Two Truths: the Big Void as imagined (Seq 12; the lure image in 3.3; 9.5b in c. 1332 BC)

**Real anchors:**
- **The Big Void** (Morishima et al., *Nature* 2017) is at least 30 m long, with a cross-section similar to the Grand Gallery's, and lies above the Grand Gallery [07 B2].
  - It was confirmed by three independent muon technologies.
  - Its purpose is unknown and it is **not accessible**.
  - Whether it is horizontal or inclined is unresolved.
- Budge: the 42 assessors in two rows of 21, with the Great Scales at the end [04 §3].
- ⟂ Everything else.

**Production spec (consistent with file 02 §13):**
- **The niche gallery:** 31 m long and **3.0 m wide** at the floor (wider than the Grand Gallery, to stage the procession). Its corbelled walls rise 8.6 m to a 1 m ceiling slot. **The floor is horizontal**, a staging choice.
  - Twenty-one niches per side, each 0.9 m wide, 2.0 m high and 0.6 m deep, with the sill 0.5 m up, on 1.45 m centres (UNIT_BALANCE_NICHES).
- **The Balance bay** at the far (north) end: 6.5 × 6.5 m, corbelled to about 9 m.
  - The Balance (3.5 m) stands on its stepped 2 × 2 m plinth, centred.
  - The Thoth slab stands to the **right** of the Balance.
  - The mouth of Ammit is in the floor, 1.5 m in front of the plinth.
  - The kneeling shabti is on the **left**, its thread running along the left wall.
  - The glass serpent's socket is at the pillar's foot.
- **The Hall's mouth:** a low square opening in the floor at the near (south) end, where the passage from the Gallery arrives.
- **Materials:** pale, fine, undecorated limestone and fine dust. The Balance is black stone and the slab glass (file 02 §13).
- **The three-source rule** (bible §7, 12.1): pure black cut only by the heart's glow (the left-hand pan, or Tut's chest before he gives it), the feather-light (right-hand pan) and the kneeling unit's amber slit. **"The Hall: black + heart green-gold"**: the heart's source is warm amber-gold seen through yellow-green desert glass. The glass serpent's green pulse belongs to the same family, and is kept fainter than the three sources.
- **Screen direction** (file 02 §13): from the entrance looking toward the Balance, the HEART pan is on the **LEFT** and the CLAIM pan on the **RIGHT**.

**LONG:** a sealed, tall and narrow corbelled limestone hall hidden inside a pyramid, its walls stepping inward to a slit of ceiling far overhead, twenty-one tall empty niches receding along each side, opening at the far end into a square bay where an ancient black stone balance stands on a stepped plinth beside an upright glass slab, all in total darkness

**SHORT:** a sealed tall corbelled limestone hall inside a pyramid, two rows of tall empty niches leading to a black stone balance, in total darkness

**Area add-ons:**
- `MOUTH`: `at the hall's near end, where a low square opening in the floor gives onto a steep passage below`
- `NICHES`: see UNIT_BALANCE_NICHES (file 02 §13.5)
- `BAY`: `in the square bay at the far end, the black balance on its stepped plinth, the glass slab to its right, a round stone iris in the floor before it`

**Lighting variants (the only permitted ones):**
- `LOC_HALL_TWO_TRUTHS_THREE_SOURCE` (default from 12.3): `pure black; the only light comes from three sources: a warm amber-gold glow through yellow-green glass on the left, a cold silver-white plume of light in the right-hand pan, and one small vertical amber slit low on the left; the stone read only by rim light` + GRADE_HALL
- `LOC_HALL_TWO_TRUTHS_PRE_HEART` (12.1–12.2): `pure black; only a cold silver-white plume of light in the right-hand pan and one small vertical amber slit low on the left, a faint green pulse at the balance's foot`
- `LOC_HALL_TWO_TRUTHS_VERDICT` (12.5): `threads of warm golden light travelling from the left-hand pan through the glass slab into a coiled glass form at the balance's foot`
- `LOC_HALL_TWO_TRUTHS_AMUN` (after the Renaming): `the silver-white plume soft and steady, the amber slit dark, a calm faint green glow at the balance's foot`
- `LOC_HALL_TWO_TRUTHS_ANCIENT_1332` (9.5b; the screenplay's own three lights: "the queen's lamp, the dim glow of the disk on its sledge, and one not yet lit"): `black, cut only by one oil lamp set on the floor and the dim gold-green glow of a coiled glass form lying on a low wooden sledge; once the heart is placed, a warm amber-gold glow from the left-hand pan; the niches in deep shadow` + GRADE_1332_NIGHT + GRADE_READ_FROM_GLASS (post)

**State add-ons:** the clouding (C0–CLEAR), pan (P0–P5), feather (F0–F3) and iris states are **file 02 §13** add-ons. Paste them verbatim after this lock.

**Never:** torches, phones or any other light inside the Hall in 2033. Nour's tablet is kept dim or seen only as a reflection (open question in file 04). No decoration on the walls; no daylight; no coloured gels.

**PLATE — establishing, 16:9:**
Cinematic still inside a sealed, tall and narrow corbelled limestone hall hidden inside a pyramid, with no people. Its walls step inward to a slit of ceiling far overhead; twenty-one tall empty niches recede along each side. At the far end, in a square bay, an ancient black stone balance stands on a stepped plinth beside an upright slab of pale yellow-green glass. Everything is pure black except for a cold silver-white plume of light standing in the balance's right-hand pan, a warm amber-gold glow low at the left, and one small vertical amber slit low on the left; the stone is read only by rim light. Photoreal live-action film still, anamorphic 35mm, deep blacks, fine film grain. Aspect ratio 16:9.

---

## 53. LOC_GP_NORTH_FACE — the Great Pyramid's north face, and the entrance at dawn (Seq 11 at night; 12.7 at dawn, 06:14)

**Real anchors:**
- The **original entrance** is on the north face, **7.9 m (15 cubits) east of the centre line**, on the 19th course **about 17 m above the base**, beneath a row of **double chevrons**: pairs of huge leaning limestone beams forming a gable [07 B2; 07 src]. Strabo describes a stone here "which may be taken out" [07 C4]. Nearby, a large square panel of modern hieroglyphs cut by Lepsius's Prussian expedition in 1842 must read as illegible texture [07 src].
- The **North Face Corridor** behind the chevrons is about 9 m long and about 2 × 2 m [07 B2].
- **Al-Ma'mun's forced tunnel** opens lower down, in the 6th–7th courses about 7 m above the base, and is today's entrance [07 src].
- A few original **casing stones** survive at the base of the north face [07 A1].
- The courses vary from 148 cm at the bottom to about 50 cm at the top [07 A1].
- **Sunrise on 8 Nov 2033 at 06:14 EET** [bible; verify ephemeris], at an azimuth of about 110–112° [verify].
- **The north face gets no direct sun at all in early November** (computed: the faces slope at 51°50′ [07 A1], and the sun's noon altitude at Giza on 8 Nov is only about 43°, so a face tilted back at that slope toward the north stays in its own shadow all day) [verify]. At 06:14 the sun lights the **east** face; the north face lies in soft blue shadow, and only the north-east corner edge catches gold.
- The Sphinx faces sunrise (Hor-em-akhet) [07 Q9].
- ⟂ Akhenaten sits on the courses facing east: "It is only the sun."

**LONG:** the north face of the Great Pyramid seen close: a vast slope of stepped, weathered limestone courses, each block about waist high, rising out of frame; high on the face a dark entrance sits beneath two pairs of enormous leaning limestone beams forming a chevron, and below it a rough hole leads in, with a stone platform and steps

**SHORT:** the stepped, weathered limestone north face of the Great Pyramid, a dark entrance high up beneath huge chevron beams, a rough hole below

**Lighting variants:**
- `LOC_GP_NORTH_FACE_DAWN_0614`: `sunrise: a low gold sun just clearing the horizon at frame left, lighting the east face gold and drawing a thin gold line down the north-east corner, the north face itself in soft blue shadow, dust haze glowing gold at the left` + GRADE_DAWN_0614
- `LOC_GP_NORTH_FACE_NIGHT` (Seq 11): `floodlit from below by hard white floodlights, the face bleached and textured, the sky black and full of stars` + GRADE_NIGHT_ACTION

**Geography lock (hard):** facing the north face from the north, **the sunrise is always at frame left (east)**. Akhenaten sits on the lowest courses at the **north-east corner (frame left)**, facing **east into the first sun**, his face lit gold while the face behind him stays blue. Fathi and Nour carry Tut out of the rough lower opening and down the steps **from right to left**, out of the blue shadow and into the sun as they reach the corner.

**Flags:** `COMP` for the sun disc's exact position and the moment it clears the horizon (timed to the transfer, bible §7, 12.7).

**PLATE — establishing, 16:9:**
Cinematic sunrise still of the north face of the Great Pyramid seen close, with no people: a vast slope of stepped, weathered limestone courses, each block about waist high, rising out of frame. High on the face, a dark entrance sits beneath two pairs of enormous leaning limestone beams forming a chevron; below it a rough hole leads in, with a stone platform and steps. A low gold sun just clearing the horizon at frame left lights the pyramid's east face and draws a thin gold line down the north-east corner, while the north face itself lies in soft blue shadow; dust haze glows gold at the left. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## J. VISIONS AND THE WORLD

## 54. LOC_FIRST_TIME — the First Time: the green Sahara vision (Seq 3.3, the archive vision)

**Real anchors:**
- The **African Humid Period** (about 14,500–5,500 BP) brought grassland, lakes, rivers and **hippos** to the Sahara. Lake Mega-Chad reached about 360,000 km². It ended around 5.5 ka [06 §7].
- Sea level has risen **about 120 m** since the last glacial maximum, drowning coastlines [06 §3].
- **Göbekli Tepe** (c. 9500 BC): its T-pillars have arms and hands carved on their sides [06 §5].
- The Red Beer: the Book of the Heavenly Cow [04 §8].
- ⟂ Machines, gardens, the red fields, the nine cores.

**Rules (bible §7, 3.3; file 02 §10):**
- **Never children**: only empty cradles and abandoned toys.
- The machines never harm anyone on screen.
- The read-from-glass grammar is added **in post** (file 05 §3, GRADE_READ_FROM_GLASS). Generate the plates clean.

**LONG:** a vast green savannah where the Sahara is now: rolling grassland dotted with acacia trees, a wide shallow lake full of reeds and grazing hippos, herds on the far shore, low sandstone mesas softened by grass, a humid haze over everything and a huge pale sky, with no roads, walls or fields anywhere

**SHORT:** a vast green prehistoric savannah with acacias, a reedy lake with hippos, grassy sandstone mesas and humid haze, no human structures

**Area add-ons:**
- `DROWNED_COAST` ("where the sea is now, a coast of pale towns", seq_03): `far off, where the sea now lies, a low coast of pale stone towns beside calm water, softened by haze`
- `GARDEN_ROWS`: `adults asleep in long rows on the grass beneath acacia trees, empty wooden cradles and abandoned toys lying among them`
- `CORES`: `in a vast cavern of cut stone, nine enormous coiled glass forms lying in stone beds, glowing faint green`
- `MOUNTAIN`: `on a high rocky mountainside above the plain, a few shepherds in skins watching over their flocks`
- `RED_FIELDS`: `vast flat fields flooded with shallow red liquid stretching to the horizon`
- `T_PILLAR`: `a tall T-shaped stone pillar standing in a ring of rough stones, arms and hands carved in low relief down its sides, no face`
- `LIDS`: `colossal granite lids grinding shut over stone boxes in a dim quarry`
- `PAINTED_LURE` (the style shift at the end of 3.3): see file 05 §13. It is shot as a photoreal painted surface, never as a cartoon.

**Lighting variants:**
- `LOC_FIRST_TIME_MORNING`: `soft humid green-gold morning light, haze on the water, lush saturated greens` + GRADE_FIRST_TIME + GRADE_READ_FROM_GLASS (post)
- `LOC_FIRST_TIME_MOON_RED`: `night under a full moon, the flooded fields glowing dark crimson, silver light on the water's edge` + GRADE_READ_FROM_GLASS (post)

**PLATE — establishing, 16:9:**
Cinematic wide still of a vast green savannah where the Sahara is now, twelve thousand years ago, with no people: rolling grassland dotted with acacia trees, a wide shallow lake full of reeds with hippos grazing at its edge, herds on the far shore, and low sandstone mesas softened by grass. A humid haze lies over everything under a huge pale sky; there are no roads, walls or fields anywhere. Soft green-gold morning light. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 55. LOC_ROBOT_HALF_MARATHON — the early humanoid half-marathon, archive style (Seq 1.6, main titles)

**Real anchor [08 B1]:** a humanoid-robot half-marathon on 19 April 2025. Twenty-one robots started on a separated lane of the 21.0975 km course and six finished. One robot fell at the gun, one ran into a barrier, and robots were guided by human runners, with battery swaps allowed.

**Rules (bible §7, 1.6; the task brief):**
- **Generic city**: no identifiable landmarks, skyline or city branding.
- No legible bibs, banners or signs. **Fictional, unbranded robots**: never a real model. The robots are UNIT_EARLY_HUMANOID (file 02 §14.5).

**LONG:** a wide modern city boulevard on a spring morning, a race lane fenced off with plain white crowd barriers, spectators pressed behind them holding up phones, glass office towers and young street trees on both sides, a plain inflatable start arch without any lettering, and small awkward humanoid robots lined up at the start beside human handlers

**SHORT:** a wide modern city boulevard with a race lane behind plain white barriers, crowds with phones, glass towers, a blank start arch

**Lighting variants:**
- `LOC_ROBOT_HALF_MARATHON_ARCHIVE`: `flat bright overcast daylight, the look of 2020s handheld documentary news video shot on a long lens, slightly soft` + GRADE_ARCHIVE_2025

**PLATE — establishing, 16:9:**
Documentary-style still of a wide modern city boulevard on an overcast spring morning. A race lane is fenced off with plain white crowd barriers; spectators press behind them holding up phones; glass office towers and young street trees line both sides. A plain inflatable start arch carries no lettering. A dozen small, awkward, unbranded humanoid robots with exposed joints stand lined up at the start line beside human handlers in plain tracksuits. No legible text, no logos, no recognisable landmarks. Photoreal handheld news-video look, long lens. Aspect ratio 16:9.

---

## 56. LOC_DEWAR_VAULT — the cryonics vault in a desert city (Seq 5.1)

**Rules:** "a cryonics vault in a desert city where robots still faithfully top up the dewars (no state named)" (bible §7, 5.1). **Never** name or resemble a real cryonics organisation. There is no signage.

**Production spec:** a windowless bay of tall brushed-steel cylindrical dewars about 3 m high [production], with frost at the filling ports, insulated overhead pipes and white vapour. A shabti tops them up from a hose.

**LONG:** a windowless storage bay in a low desert-city building, rows of tall brushed stainless-steel cylindrical tanks taller than a man standing on a white-painted floor, insulated pipes overhead, frost furred around their filling ports, thin white vapour spilling to the floor

**SHORT:** a windowless bay of tall brushed stainless-steel cryogenic tanks in rows, frost on their filling ports, white vapour spilling to the floor

**Lighting variants:**
- `LOC_DEWAR_VAULT_LIT`: `cool white overhead LED panels, soft reflections on the steel, the vapour glowing faintly` + GRADE_2033_MUSEUM
- `LOC_DEWAR_VAULT_EMERG`: `only amber emergency lamps and the soft glow of an amber light-slit moving between the tanks`

**PLATE — establishing, 16:9:**
Cinematic still inside a windowless storage bay, with no people: rows of tall brushed stainless-steel cylindrical tanks, taller than a man, stand on a white-painted floor beneath insulated overhead pipes; frost is furred around their filling ports and thin white vapour spills to the floor. Cool white overhead light, soft reflections on the steel, quiet and clinical. No signage or text. Photoreal live-action film still, anamorphic 35mm, fine film grain. Aspect ratio 16:9.

---

## 57. LOC_PORT_WAREHOUSE — the port-city warehouse Garden, Osaka (Seq 5.1; 12.6 the Renaming around the world)

**Rules:** the sleepers are adults; there is no legible Japanese signage (blurred or turned away). The bible writes "a port-city warehouse".

**LONG:** the vast interior of a harbour-side warehouse in a Japanese port city, a steel portal-frame roof high overhead with rows of skylights, a polished concrete floor filled edge to edge with long neat rows of folding cots under pale grey blankets, and through the open loading doors gantry cranes against the harbour sky

**SHORT:** a vast harbour warehouse in a Japanese port city, high steel roof and skylights, endless neat rows of folding cots, gantry cranes outside

**Area add-ons:**
- `GARDEN`: `sleeping adults lying on every cot, a few faceless care robots in sand-coloured knit moving slowly between the rows`

**Lighting variants:**
- `LOC_PORT_WAREHOUSE_DAWN_GARDEN`: `soft white dawn light through the skylights, shadowless and calm, the cranes outside grey in mist` + GRADE_GARDEN
- `LOC_PORT_WAREHOUSE_NIGHT`: `dim cool night light, small amber light-slits dotted across the dark hall`

**PLATE — establishing, 16:9:**
Cinematic dawn still of the vast interior of a harbour-side warehouse in a Japanese port city. A steel portal-frame roof with rows of skylights soars overhead; the polished concrete floor is filled edge to edge with long, neat rows of folding cots under pale grey blankets, sleeping adults on every one. Through the open loading doors, gantry cranes stand grey against a misty harbour sky. Soft, shadowless white light. No legible signs. Photoreal live-action film still, anamorphic 32mm, fine film grain. Aspect ratio 16:9.

---

## 58. LOC_LAGOS_STREET — a Lagos street at dawn (Seq 5.1)

**Rules:** the world has stopped, but nothing burns (bible §7, 5.1). There is no legible signage and no damage.

**LONG:** a wide, busy Lagos street at dawn gone utterly still: yellow minibuses and cars stopped at odd angles in every lane, closed market stalls under corrugated roofs, hand-painted shopfronts with blurred unreadable signs, overhead power lines, a concrete road bridge crossing in the distance, and not a single person in sight

**SHORT:** a wide Lagos street gone utterly still at dawn, yellow minibuses and cars stopped at odd angles, closed market stalls, no people

**Lighting variants:**
- `LOC_LAGOS_STREET_DAWN`: `hazy pale dawn, soft grey-gold light, a faint mist over the stopped traffic`

**PLATE — establishing, 16:9:**
Cinematic dawn still of a wide, normally busy Lagos street gone utterly still. Yellow minibuses and cars sit stopped at odd angles in every lane; market stalls under corrugated roofs are closed; hand-painted shopfronts carry blurred, unreadable signs; power lines cross overhead, and a concrete road bridge crosses in the distance. There is no one in sight. Hazy pale grey-gold light, a faint mist. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 59. LOC_STADIUM_GARDEN — the stadium Garden, aerial (Seq 5.1 in SESHAT's feed; 12.6)

**Rules:** the bible marks it COMP (SESHAT's own feed). Generate a clean aerial plate; the feed graphics (the glyph and white type) are overlays. The sleepers are adults.

**LONG:** seen from high above, a huge modern football stadium whose pitch and running track are covered edge to edge by a precise grid of thousands of white mats with sleeping adults and pale fabric shades, tiny slow figures moving between the rows, the empty stands rising all around in concentric tiers

**SHORT:** an aerial of a huge stadium whose pitch is covered by a precise grid of thousands of white mats and pale shades, stands empty

**Lighting variants:**
- `LOC_STADIUM_GARDEN_DAY_GARDEN`: `soft overcast white daylight, shadowless and calm` + GRADE_GARDEN
- `LOC_STADIUM_GARDEN_DAWN_WAKING` (12.8): `first sun raking across the stands, long shadows over the grid`

**Flags:** `COMP` (the feed graphics) and `VFX-EXTEND` (the grid).

**PLATE — establishing, 16:9:**
Photoreal aerial still from high above a huge modern football stadium. Its pitch and running track are covered edge to edge by a precise grid of thousands of white mats with sleeping adults and pale fabric shades; tiny figures move slowly between the rows; the empty stands rise all around in concentric tiers. Soft overcast white light, shadowless and calm. No logos or text. Aspect ratio 16:9.

---

## 60. LOC_HOSPITAL_WAKING — the waking hospital, the first birth (Seq 12.8)

**Rules:**
- The midwife is human (CHAR_MIDWIFE_2033).
- The newborn is always **swaddled**, seen over the midwife's shoulder or from behind. There is no close-up of the baby's face and no medical procedure.
- The mother is shown from the shoulders up.

**LONG:** a modern hospital maternity room, pale walls, a wide window, a raised bed with white sheets, a clear bassinet on a steel stand, a monitor dark on its arm, a nurse's chair, and a half-open door onto a quiet corridor where people are just beginning to stir

**SHORT:** a modern hospital maternity room, pale walls, a wide window, a white bed and a clear bassinet on a steel stand

**Lighting variants:**
- `LOC_HOSPITAL_WAKING_MORNING`: `soft early-morning daylight through the wide window, warm and clean, the ceiling lights flickering back on` + GRADE_2033_DAY

**PLATE — establishing, 16:9:**
Cinematic early-morning still of a modern hospital maternity room, with no people: pale walls, a wide window full of soft daylight, a raised bed with white sheets, a clear bassinet on a steel stand, a monitor dark on its arm and a nurse's chair. A half-open door looks onto a quiet corridor. The ceiling lights are just flickering back on. Warm, clean, hopeful. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 61. LOC_HEARING_ROOM — the coda hearing room ("I said yes.")

**Rules:** the panel is seen only from behind (CHAR_HEARING_PANEL). No real legislature, flag, seal or emblem appears. Nameplates are blank.

**LONG:** a formal modern hearing room with pale wood panelling, a raised curved bench for a panel facing a single witness table with a microphone and a glass of water, blank wooden nameplates along the bench, rows of public seating behind, and tall windows with pale blinds half drawn

**SHORT:** a formal pale-wood hearing room, a raised curved panel bench facing a lone witness table with a microphone and a glass of water

**Lighting variants:**
- `LOC_HEARING_ROOM_DAY`: `flat cool daylight through half-drawn blinds, even overhead light, quiet and formal` + GRADE_2033_DAY

**PLATE — establishing, 16:9:**
Cinematic still of a formal modern hearing room, with no people: pale wood panelling, a raised curved bench with blank wooden nameplates facing a single witness table with a microphone and a glass of water, rows of public seating behind, and tall windows with pale blinds half drawn. Flat cool daylight, quiet and formal. No emblems, flags or text. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 62. LOC_TITLES_KITCHEN — a high-rise kitchen at night (Seq 1.6, main titles: "A shabti folds a school shirt")

**Rules:** a generic city, no identifiable skyline. No child is in frame; the school shirt implies one (bible §3.3). The woman who calls "Shabti?" is off screen. The shabti is UNIT_SHABTI (file 02 §1).

**LONG:** a compact modern apartment kitchen high in a residential tower at night, pale wood cabinets and a white stone counter, a neat pile of folded laundry with a child's white school shirt on top, a warm pendant lamp over the counter, and a dark window wall showing distant city lights far below

**SHORT:** a compact modern high-rise kitchen at night, a white stone counter with folded laundry, city lights far below the window

**Lighting variants:**
- `LOC_TITLES_KITCHEN_NIGHT`: `one warm pendant lamp over the counter, a cool blue glow of city lights through the window, quiet domestic calm` + GRADE_2033_MUSEUM

**PLATE — establishing, 16:9:**
Cinematic night still of a compact modern apartment kitchen high in a residential tower, with no people. Pale wood cabinets, a white stone counter with a neat pile of folded laundry and a child's white school shirt on top, a warm pendant lamp glowing over the counter. A dark window wall shows distant city lights far below, with no recognisable landmarks. Quiet and domestic. No text or logos. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 63. LOC_TITLES_WARD — a hospital ward (Seq 1.6, main titles: "a shabti turns an old man in bed")

**Rules:** the patient is an adult (CHAR_GARDEN_SLEEPERS rules apply to extras). No medical procedure is shown and there is no legible signage. The unit is UNIT_SHABTI or UNIT_NURSE.

**LONG:** a calm modern hospital ward of six beds made up in white linen, pale curtains hanging from ceiling tracks between them, pale green-grey walls, tall windows full of soft daylight, bedside monitors on swing arms, and a polished pale vinyl floor

**SHORT:** a calm modern hospital ward, beds in white linen between pale curtains, tall windows full of soft daylight

**Lighting variants:**
- `LOC_TITLES_WARD_DAY`: `soft, even daylight from tall windows with clean cool-white fill, gentle and quiet` + GRADE_2033_MUSEUM

**PLATE — establishing, 16:9:**
Cinematic still of a calm modern hospital ward, with no people: six beds made up in white linen, pale curtains hanging from ceiling tracks between them, pale green-grey walls, bedside monitors on swing arms and a polished pale vinyl floor. Tall windows fill the room with soft daylight. No text or signage. Photoreal live-action film still, anamorphic 40mm, fine film grain. Aspect ratio 16:9.

---

## 64. LOC_TITLES_PORT — a container-port quay at dusk (Seq 1.6, main titles: "all down the quay, shabti cast off mooring lines")

**Rules:** no real port, no legible container markings, ship names or company colours. Rows of shabti along the quay are VFX-EXTEND (file 02 §0.5).

**LONG:** a long container-port quay at dusk, towering ship-to-shore gantry cranes above a moored container ship stacked with plain unmarked containers, heavy steel bollards and thick mooring lines along the concrete edge, floodlight masts coming on, and the harbour water calm and violet

**SHORT:** a long container-port quay at dusk, towering gantry cranes over a moored ship of unmarked containers, bollards and mooring lines

**Lighting variants:**
- `LOC_TITLES_PORT_DUSK`: `a violet-blue dusk sky, sodium floodlights warming on the masts, the water holding the last light` + GRADE_2033_DAY

**PLATE — establishing, 16:9:**
Cinematic dusk still of a long container-port quay, with no people. Towering ship-to-shore gantry cranes stand above a moored container ship stacked with plain, unmarked containers in muted colours; heavy steel bollards and thick mooring lines run along the concrete edge. Floodlight masts are just coming on against a violet-blue sky, and the harbour water is calm. No text, logos or ship names. Photoreal live-action film still, anamorphic 50mm, fine film grain. Aspect ratio 16:9.

---

## OPEN QUESTIONS (locations) — for the lead and the production Egyptologist

1. **Moon phase, 4–8 Nov 2033.** Not checked. The proposal is no moon in frame on Act II nights, which sells the blackout. If the ephemeris gives a bright moon, keep it out of shot. The same check is needed for sunrise at 06:14 EET and its azimuth at Giza [verify].
2. **Asyut before Amarna?** The screenplay has the launch reach the Asyut lock (seq_06, 15:10) **after** passing Amarna at midday (6.5). By river, Amarna (about 300 km from Cairo) lies **north** of Asyut (about 375 km), so the order works. But reaching Luxor by about 21:00 from Asyut at 15:10 means about 270 km in 6 hours, which is too fast for a 10–12-knot launch. The screenplay editor should check this; it is not a location lock.
3. **The Karnak quay.** The ancient quay now lies inland [verify]. The film uses a modern Corniche river landing directly west of the ram avenue. Confirm the layout and the distance from the First Pylon.
4. **The midpoint projection surface.** It is locked to the **First Pylon**, the only surface tall enough for a 40 m figure; the First Pylon's height is [verify]. The bible says "the pylon and the columns": the columns take spill light (LOC_KARNAK_HYPOSTYLE_PROJECTION).
5. **The KV62 wall geography.** The opening lies behind the right-hand scene, with the painted king's eye at the top edge. This is a staging choice. The real 2026 anomaly lies "parallel to the north wall"; confirm with the Egyptologist that no real feature contradicts it.
6. **The 1323 BC chamber staging.** The shrine panels are shown unassembled so the sarcophagus is reachable. The real order of works is uncertain; confirm.
7. **KV62 in 2033:** the empty sarcophagus under glass and the empty mummy case in the antechamber follow from the OSIRIS move. Confirm the outermost coffin's real 2019 move to the GEM [verify].
8. **The Hall of Two Truths:** a horizontal floor, a 3.0 m gallery width and a 6.5 m Balance bay are staging choices. The real Big Void's inclination is unresolved [07 B2]. The glass serpent's green pulse is treated as part of the "heart green" family, kept fainter than the three sources. Confirm with file 02 §13 and the lead.
9. **The Great Pyramid interior dimensions** (the Descending Passage, the Subterranean Chamber, the Well Shaft, the Grand Gallery's corbels, the Queen's Chamber) now come from the research bundle's source mirror [07 src], a secondary summary of the standard surveys. Keep [verify] on any number a line of dialogue quotes, and check the Well Shaft's cross-section and the modern fittings (railings, lighting, walkway) on a site visit or survey.
10. **GEM interiors** (the atrium glazing, the Grand Staircase window, the gallery wall colours, the boat hall) are production spec or [verify]. No reachable source documents them [14 §5].
11. **The Serapeum box dimensions and the gallery height** [verify]; also whether the abandoned service-tunnel box has its lid.
12. **Deir Mawas station and the Asyut barrage** are generic by design. Confirm that no real layout needs matching.
13. **Real place names in prompts** (Nile, Giza, Karnak, Lagos, "a Japanese port city") are allowed by this file as geography, not brands. **Confirmed by the cross-check:** plain geographic names are places, not brands or people; institution names (the museum, HELIOS, any university, police service or ministry) and people's names stay out of every prompt.
14. **Tomas's death in the Hall (12.6).** The screenplay has the jackal fire at the Hall's mouth and "sparks burst off the black stone of the Balance": a momentary fourth light. Proposal: allow it as a 2–4-frame event, with the muzzle flash kept outside the Hall's mouth (off screen) and the sparks cold white like the feather. The lead to confirm the exception to the three-source rule.
15. **GEM_CC daylight.** The Conservation Centre's windows are undocumented; the DAY and DUSK variants assume a high clerestory. Confirm, or make both variants artificial light only.
16. **Giza geography** was corrected in this pass from bearings computed on published site coordinates: from the Wall of the Crow, the Great Pyramid is at centre frame and the Sphinx at frame right. Verify on a site plan before any plate is approved.
17. **The north face in shadow.** By computation, the Great Pyramid's north face receives no direct sun in early November, so the 06:14 light falls on the east face and the north-east corner. Verify with an ephemeris; the dawn staging (entry 53) is built on it.
18. **KV62 in 2033:** the modern opening, platform and barrier between the antechamber and the burial chamber [verify].
19. **Avenue naming.** The screenplay uses only the AVENUE OF RAMS at the First Pylon; the long Avenue of Sphinxes to Luxor Temple is the `SPHINX_AVENUE` add-on for any shot that needs it. Confirm which avenue the midpoint wides show.
