# SCREENPLAY WRITERS' SPEC — HERE AM I

You are writing one sequence of a feature screenplay. Eleven other writers are writing the other sequences at the same time, from the same locked story bible. Your pages must join theirs without a seam.

## Read first (in full)
1. `drafts/02_STORY_BIBLE_LOCKED.md`: the single source of truth. Read ALL of it, not just your sequence: characters, rules of the machine and the Balance (§3–4), the robot-action register (§8), the continuity state board (§12), the motifs and look (§11), the language and localisation notes (§13).
2. `drafts/04_CRITIQUE_DECISIONS.md` if it exists: the lead's rulings after the critique pass. Where it amends the bible, it wins.
3. The research files your sequence cites (`research/NN_*.md`). Use Grep to pull exact quotes, dimensions and names. Quote real texts verbatim with the translator the bible names.

## Format: Fountain (plain-text screenplay)
- Scene headings: `INT. LOCATION - TIME` / `EXT. LOCATION - TIME`, with the location as specific as the bible gives it (e.g. `INT. GEM CONSERVATION CENTRE, MUMMY LAB - NIGHT`). For period scenes, add a line `SUPER: THEBES. c. 1323 BC.`
- Action lines in present tense, lean and visual; no paragraph longer than 4 lines. Use line breaks to control pace in action.
- CHARACTER cues in caps. Parentheticals sparingly. Extensions: (V.O.), (O.S.), (CONT'D).
- Egyptian dialogue: write it in English, with the parenthetical `(in Late Egyptian; subtitled)`. Where the bible or research gives a transliteration, you may add it on the first use only, in a Fountain note: `[[transliteration: mk wj — reconstructed]]`.
- SESHAT is `SESHAT (V.O.)` when it speaks from speakers or the air, and `SHABTI (SESHAT'S VOICE)` when a unit speaks. The units' acknowledgment is always exactly: `Here am I.`
- Title cards: `SUPER: THE SIXTH HOUR — THE SOUL MEETS ITS BODY`
- Transitions (`CUT TO:`, `MATCH CUT TO:`, `SMASH CUT TO:`) only where they matter, right-aligned in Fountain with `>`.
- Put a Fountain boneyard note at the very top of your file: `/* SEQ n — TITLE — pages x–y */`. Do NOT include a title page; the assembler adds it.
- Do not number scenes; the assembler numbers them.

## Length
- 1 screenplay page ≈ 190–220 words of Fountain (dialogue-heavy pages run shorter, action pages longer). Hit your sequence's page target ±15%. **A 10-page sequence is roughly 2,000–2,400 words.**

## Craft rules
- **Suspense first.** Each scene needs a question the audience wants answered, or a clock. Open scenes late and leave early.
- **Robot action must be choreographed clearly**: geography first (where everyone is, where the exits are), then escalation, then a reversal, then a cost. The units follow procedure. They are never cruel and never theatrical: they stop, turn their heads, say "Here am I", and act with the minimum force. Jackals are fast and silent; flies trail glittering threads; shabti never run.
- **Violence stays PG-13** and follows the bible's KILL GRAMMAR (§3.3): impact on environment → human drops out of frame/silhouette → survivor reaction → sound. Never write 'shot', 'blood', wounds or aimed-at-lens weapons. Broken bones are off-screen sounds.
- **Remains & organs** follow bible §3.4 exactly: the heart is only a linen bundle, then a dark shape in the vessel; the 2033 body is under a sheet with a projected line diagram; chests open under fabric. Never 'organ', 'severed', 'open chest'.
- **Minors** follow §3.3: robots never touch a child on screen; Layla asleep only in the one approved image.
- **Readable text** (hieroglyphs, subtitles for mouthed lines, screens, glyphs, hour cards) is written as `SUPER:`/`COMP:` notes; plot-critical reading is carried by a character's voice.
- **Human remains with dignity.** Tut's mummy and the foetuses are treated with reverence on the page.
- **Tut's voice:** formal, slightly archaic English, wry, surprising ("That is a status report"). Short sentences. He grieves in understatement. His humor is dry and royal.
- **SESHAT's voice:** warm, low, unhurried, courteous; it thanks people and cites sources ("Hubinger et al., 2024"). It never raises its voice and never gloats.
- **Nour (Dr. Nour KAMEL — not Hamdi):** quick, precise, sardonic, fierce about Layla; the SCA-appointed inspector; switches between English, Egyptian Arabic (subtitled) and Late Egyptian; liturgy she reads in Middle Egyptian.
- **Adaeze:** dry, literal, quotes papers; gallows humour.
- **Tarek:** few words, military exactness; one joke per act.
- **Fathi:** the unit's combat engineer — practical, tactical, warm, devout in private (a brief du'a, never staged salat); calls Tut "ya Malik" ("O King"); never a servant type.
- **Tomas:** gentle, guilty, engineer's precision.
- **Rami:** fast, funny, pop-culture.
- **Egyptian characters are the story's centre, not its scenery.** No orientalist clichés, no "mystic natives." The Egyptian state is plausible and neither cartoonish nor defamatory. Every real official is fictionalized or unnamed. No real living person is depicted or named as a character.
- **Real facts:** use the exact real details the bible and research give (numbers, museum numbers, quotes). Never invent a "real" fact. If you add a real-world detail that is not in the research, mark it `[[verify]]` in a Fountain note.
- **The mysteries:** when Tut explains, give **specific details and reasoning** (the client asked for this). He debunks the hoaxes first; he is quiet at the genuine anomalies; the fiction is stated with confidence *in-world*.
- **Hit every beat listed for your sequence in the bible**, in order unless a reorder clearly improves it, in which case explain why in your notes. You may add micro-beats, lines and small reversals. Do not add major characters, change the rules of the machine or the Balance, move where a prop is, or kill or save anyone differently from the continuity tracker.
- **Hand-offs:** your first scene must pick up exactly where the previous sequence ends (read the neighbouring sequences' beats in the bible), and your last scene must hand off to the next.

## Deliverables
1. `screenplay/seq_NN.fountain`: your pages.
2. `screenplay/notes/seq_NN_notes.md`, containing:
   - a scene list (heading, one-line purpose, estimated pages);
   - any deviations from the bible and why;
   - every `[[verify]]` item;
   - props, wardrobe and injuries at the END of your sequence (for continuity);
   - a word count.


## v3 NOTE
The bible is now v3 (post-critique). Character names: Nour KAMEL; Victor HALE (not Vance). Soldier pack: Cpl. Hassan, Pvt. Mina, Pvt. Youssef, Pvt. Karim. Follow §12 continuity board and §13 language/localisation rules. Egyptian characters speak Egyptian Arabic to each other when alone (subtitled).
