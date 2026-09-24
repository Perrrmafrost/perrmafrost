# Open items from shot-list QA

Each sequence's QA pass fixed what it could in the shot list and left these for the lead (director / production-bible owner). Most are one-word rulings or small edits to `production_bible/locks.json` (then run `validate_locks.py` and regenerate the JSONL). `[[verify]]` items go to the Egyptologist / research consultant.

## Project-wide (decide once)

- **Character negatives ban other characters' features.** e.g. `CHAR_TUT.NEG` bans hair, beard, jewellery; Tarek/Fathi ban helmets; Adaeze/Rami ban each other's glasses. In multi-character frames this can strip the wrong person. Proposed fix: split each NEG into a self-only list and apply it only in single-character shots (Seq 5, 6, 7).
- **Global negative bans 'painting, illustration'** but some shots need real painted walls (03.05.019, 08.05.003/004/013/018). At generation time drop those two words for these shots; reject illustrated-looking takes at QC.
- **Lock wording gaps** to add in `locks.json`: PROP_HEART_VESSEL open 1.1 state; PROP_LAMP_1925 unlit 2033; service corridor + stairwell emergency light (Seq 4); Corniche dock blackout without far-bank fires (Seq 5); Garden sleepers without bracelets (pre-7.3); empty map case (Seq 11); Fathi without scarf (Seq 9); which block face is down (Seq 7).
- **'ya Malik' subtitle** (10.10.007, 11.x, 12.11.010): leave unsubtitled or subtitle 'my king' — localisation consultant to confirm.
- **Runtime**: Seq 2, 3, 10 and 12 sit at the top of their ±20% window; Seq 9 is 22.6 min.

## Sequence 1

- Lock gaps left for the lead, worked around but not edited: (1) PROP_HEART_VESSEL has no open or plain-resin 1.1 state or SHORT; (2) PROP_LAMP_1925 has no unlit 2033 SHORT; (3) CHAR_TUT_CRADLE_2033 carries the gold neck ring before the seam is drawn in 01.05.003 and 01.05.011 (comp holds it dark); (4) LOC_KV62_NORTH_CORRIDOR and LOC_KV62_HEART_CHAMBER have no clean 1323 state.
- For the 2033 multi-wardrobe characters (Nour, Rami, Tarek, Hale, Tomas), LONG + WARD_A still partly repeats the costume ('bright yellow windbreaker, wearing a bright yellow zip-up windbreaker'). This follows file 01 §0.2 assembly, so it was kept. The lead may want WARD-free LONG variants.
- Screenplay [[verify]] notes are carried through to Continuity/Comp: Spell 30B wording against Faulkner, forearms low, Hamdi's age, Burton's flash, and whether the plates were read in Liverpool.
- The Ankhesenamun lock contains 'heart-shaped face', which contains the word 'heart' that 1.1 keeps out of prompts. It is harmless, but a wording choice for the lock owner.

## Sequence 2

- Nour's flat wardrobe: file 01 has her jacket over a chair at home, but her SHORT and LONG locks carry the olive field jacket. The lock wins for now, and this is still flagged for the lead in the 02.06 scene note.
- LOC_GEM_CC.LONG (the double-height cradle lab) is joined to area add-ons for separate rooms (TUT_BAY, IMAGING). The expanded Setting therefore describes the big lab and then the bay or imaging room. This follows the bible's own assembly rule, but the lead may want area-only Setting sentences for 02.02 and 02.04.
- Runtime is 14.3 min against a ceiling of 14.4 min (12 min ±20%). Little headroom is left if more beats are split into extra clips.
- Screenplay [[verify]] notes (Tulli/Gardiner, Saqqara Bird date, TUTANKHATEN sign order, Nine Bows on the sandals, the 3 Nov sunrise azimuth, the LAYLA pendant sign codes) are still open for the Egyptologist and research. They are carried in Continuity and Comp: lines.

## Sequence 3

- 03.05.019 (the painted lure): every NEGATIVE must start with the full global negative, which bans 'painting, illustration', but this shot needs a photoreal wall painting. Nobody can fix this in the shot file: at generation time drop those two words from this shot's negative, as the header notes. The audit script also flags this shot for having no modern-Egypt negative; that is wrong, because it is a First Time shot.
- Still marked [[verify]] from the screenplay: the Southampton key image (03.04.002), the Göbekli T-pillar arms and hands (03.05.018) and the Atrahasis wording (03.07.005). Also unconfirmed: the black winter police uniform needs checking with the Egyptian consultant, and the lead must still decide on the water-tray plant (03.06.002/005, 03.07.006) and the colour of the map dot.
- Runtime is 642 s against about 540 s for 9 pages (+19%). The header lists the first shots to cut if the lead needs 9:00.
- The per-reference-still counts in the header's 'Reference stills needed' list were not recounted after the small reference additions (the cane reference image in 3 shots, Rami's character refs in 03.07.002).

## Sequence 4

- Tarek's wardrobe, for the lead to decide: file 01 puts Tarek in B (vest, slung rifle) from 4.4, but the shot list keeps him in A0 (pistol) for all of Seq 4 and changes him off screen in the truck cab before Seq 5, which already uses WARD_B. I kept this because switching him between the continuous atrium and gallery scenes would be a visible jump on screen.
- File 03 has no lock for the service corridor and no emergency-light variant for the service stairwell. Those shots use plain words and a stairwell light phrase. File 03 should add these variants.
- The screenplay's [[verify]] notes are still open: which trumpet aired in 1939, the shrine copy and GEM label, and whether the restorer is deceased. The Comp and Continuity lines carry them.

## Sequence 5

- Needs the lead: file 03 should get a no-fires variant of LOC_CORNICHE_DOCK.LIGHT_BLACKOUT, and the approved LOC_CORNICHE_DOCK_BLACKOUT plate must be regenerated without the far-bank fires before any 05.07 shot or 05.08.004 is made.
- Needs the lead: file 01 dates the river-damp L1 phrases 'Seq 5-6'. The shot list treats them as starting in Seq 6. Confirm, or amend file 01.
- Needs the lead, a problem across the whole film: several character negatives in file 01 ban anchors that belong to other characters (Tut: hair, beard, jewellery; Adaeze and Rami: each other's glasses; Tarek and Fathi: helmet). Each negative should be split into a part for that character's own face and a part that is safe in shared frames. Seq 5 works around it by hand in 5 shots.
- Needs the lead: CHAR_GARDEN_SLEEPERS.SHORT and LONG always include bracelets. A no-bracelet variant is needed for Garden shots before 7.3, together with a no-bracelet version of CHAR_GARDEN_SLEEPERS_REF.
- Carried over from the previous pass: the pods' lit cabins (05.03.011) and open doors (05.08.004) override file 02 §14.4. The launch's red lamp (STATE_L1) is left out pending 05 §14 Q2.
- Screenplay [[verify]] items still open: the Baltic 2024 GNSS-spoofing figure (05.03.009), Tut's objects at Tahrir for 'a hundred years' (05.05.018), and Egyptian Army identity discs (05.07.003).

## Sequence 6

- The Asyut lock (LOC_ASYUT_LOCK) has no scene in the current pages; Seq 6 ends heading for it. For the lead to decide.
- The screenplay has the flies 'blinking' (06.04.005, 06.10.006), but file 02 says fly lights never blink. The screenplay is followed; the lead should confirm.
- Screenplay [[verify]] items still open: the Asyut lock; the 5 Nov 2033 ephemeris (Sirius on the meridian at 03:40, the Great Bear on end); lantern night-fishing; Fairall 1999; the Nobiin 'Aman Dawu'; the transliteration 'itrw'.
- Lock-level issues I can't fix from the shot list: PROP_POLICE_LAUNCH.LONG says 'salt-hazed windows' on a freshwater river. GRADE_NIGHT_ACTION.TEXT mentions sodium street light, headlights and torches, which contradicts the blackout river. PROP_DAGGER.STATE_UNSHEATHED says 'catching moonlight' on a moonless night (not used in this sequence).
- Project-wide: CHAR_TUT.NEG contains 'a full head of hair, beard, jewellery', which can fight other characters' hair and props in multi-character frames. It is withheld only where the clash is direct (the pendant shots, the dagger insert). A lock-level split into face terms and prop terms would be cleaner.

## Sequence 7

- Still to be ruled on: which face the projection plate uses. The screenplay says the Second Pylon, but file 03 maps the plate to LOC_KARNAK_RAM_AVENUE_PROJECTION, the First Pylon (05 §14 Q4). Prompts avoid naming either tower.
- Screenplay verify notes carried forward for the consultant: the nb → ḏsr recut (07.04.007); the ḫprw gloss (07.06.009/013); where the Sacred Lake sits (07.06.026); the distance from the First Pylon to the river landing (07.09.001); the Faisal Street reference (07.09.003); cruise-ship moorings (07.10.001); the spelling of RAMI in hieroglyphs (07.10.008).
- The block locks (PROP_KARNAK_BLOCK.STATE_ON_TROLLEY and PROP_BLOCK_TROLLEY.STATE_LOADED) say 'face down' without saying which face. The shot list's continuity notes pin it down (cut face down, relief face up), but the fixed lock wording should say so too.
- 07.08.025: Tarek's character negative includes 'helmet'. It applies to the whole shot, so it may strip the tan helmets (WARD_A) from Youssef and Karim, who are soft behind him. Accept it or re-stage them as separate clips.
- The Tomas and Mina codes in 07.09.002 and 07.09.028 (A2/B2) are look-code labels only; the prompts are unaffected. Both men stayed aboard the launch, so B1/A1 may be the more logical code.

## Sequence 8

- Lock conflict for the lead: LOC_KV62_BURIAL_2033.LIGHT_BLACKOUT names 'one red headlamp', but file 01 turns Adaeze's headlamp red only at 8.4 (the heart chamber). This affects the scene 5 burial-chamber shots and 08.09.004–005. The lock can't be edited from the shot list, so the red lamp stays small and in the background, as already noted in the header.
- 08.08.027 and 08.08.054 keep NEG_UNITS without a unit lock token because only part of a shabti is in frame (the fingertips; ceramic shoulders at the frame edge). This is intentional, but an automated 'NEG_UNITS needs a unit token' check will flag them.
- Painted-wall shots (08.05.003, 004, 013, 018) run under the global negative, which bans 'painting' and 'illustration'. The prompts ask for real paint on real plaster; reject illustrated-looking takes at QC (already in the header).

## Sequence 9

- locks.json has no field for Fathi without his scarf. All his lock fields name the scarf at his neck, so the 8 shots between 09.02.008 and 09.16.003 still contradict themselves, and the fix depends on first frames made from the CHAR_FATHI_B_noscarf still. Needs a CHAR_FATHI.STATE_NO_SCARF field or a scarf-free SHORT variant in the bible.
- Conflicts inside the lock file, left as tokens and logged in the Notes for the lead: coach benches are green vinyl in the location lock but wooden in the prop lock; LOC_DEIR_MAWAS.STATE_DERAILED says 'on its side' but PROP_DIESEL_LOCO.STATE_T3 says 'canted'; NEG_HALL bans the queen's lamp in the 1332 Hall; PROP_HEART_VESSEL's lock names the wax serpent and papyrus band, which the V-1332 state does not have yet; CHAR_TUT_CHILD_9/11 and CHAR_YOUNG_MOTHER negatives ban 'crown'.
- The coupling-platform lock uses 'sleepers' for railway ties, which could bring sleeping people into the 09.11 takes. Watch for it at QC.
- The scene files in shots/parts_09/ are now out of date. The fixed shots/seq_09_shots.md is the master; do not rebuild it from parts_09.

## Sequence 10

- Serpent state at the reveal (10.06.011): the screenplay's 'light moves slowly, like breath' is played as S1, while file 02 lists S0 'dormant in the pit'. This is the lead's call; it is open point 1.
- Tut's damage: file 01 lists L3 for all of Seq 10, but the L3 lock includes the torn left knee, so Tut plays L2 until 10.08.016. This needs the lead's sign-off (open point 5).
- Runtime is 12.0 min for 10 pages, inside the ±20% target but long. Cut candidates are listed in open point 3 (10.05.002, 10.06.029, 10.08.013, 10.08.032).
- 'ya Malik' is unsubtitled in the English master (10.10.007). The lead needs to confirm.
- The [[verify]] tags on the Amduat hours, the Philae date and the Giza lights being visible from Saqqara are carried through from the screenplay and still need the Egyptologist or research.

## Sequence 11

- Lead approval still needed for 11.04.014, the only face underwater in the film (Tut, calm, lips closed). NEG_WATER is deliberately left off that shot.
- Fixed lock wording in the production bible conflicts with 05 §13.9. The file 03 locks LOC_OSIRIS_SHAFT.LIGHT_TORCH, LOC_GP_GRAND_GALLERY.LIGHT_HEART_GLOW and LOC_GP_PASSAGE_ABOVE.LIGHT_HEART_GLOW all say 'amber' or 'amber-gold', and GRADE_UNDERGROUND assumes head torches. File 03 and file 05 need reconciling. The locks are pasted verbatim and were not edited.
- Both PROP_MAP_CASE locks (SHORT and LONG) describe the notebook already sealed inside, so there is no lock for the empty case. 11.03.006 describes it in plain words; file 04 could add a STATE_OPEN_EMPTY entry.
- Items carried over from the header notes: the Garden bedding (CHAR_GARDEN_SLEEPERS 'low cots' against LOC_GEM_ATRIUM.AREA_GARDEN 'white mats'); 'Ya Malik' left unsubtitled (localisation consultant to confirm); the screenplay's [[verify]] notes (the Horus gloss, the Osiris Shaft levels, Al-Ma'mun's tunnel, the Amduat card titles, the Gallery dimensions).
- 11.08.002 (Fathi lifting the thread) has no NEG_UNITS. It was left off on purpose: the thread is not a robot unit, so the add-on's robot terms do not apply.

## Sequence 12

- Screenplay [[verify]] items still open: the Amduat hour-card titles for hours 10-12 (Hornung), the 06:14 sunrise at Giza on 8 Nov, the KV21 entrance and where mummy KV21A is kept today, and the Budge verdict wording with the name dropped.
- Rulings still owed by the lead: whether the Balance sparks in 12.07.023 may be a 2-4-frame fourth light in the Hall (05 §14 Q5), and whether 12.11.010 is subtitled 'ya Malik' or 'my king'.
- 12.01.020, 12.01.021, 12.07.016 and 12.07.018 deliberately paste the {NEG_HALL} terms minus 'glowing screens' so the tablet can glow, instead of using the token. This is documented in each shot but differs from the standard.
- 12.10.005: the port warehouse uses the NIGHT variant so the robot light-slits read, although local time there is roughly midday. This is noted in the shot and needs a lead decision.
- The Adaeze D still (the hearing, clean clothes plus cane) must be made by image edit from her A still; file 01 has no D reference still.
- The runtime of 15.5 min is at the top of the 10.4-15.6 min window (13 min target ±20%).
