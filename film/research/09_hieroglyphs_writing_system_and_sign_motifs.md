# 09 — How Hieroglyphs Actually Work, and a Palette of Real Signs for the Film

Research notes for the feature treatment (ASI resurrects Tutankhamun as a cyborg; the machine treats *medu-netjer* as executable instructions). Purpose: give the writers a checkable account of the script, its decipherment, Tutankhamun's own name-signs, and a sign palette with Gardiner codes and Unicode code points that a production designer can put on screen. Compiled 2026-09-22.

Cross-references (do not repeat): the Abydos "helicopter" palimpsest and the Nine-Bows epithet of Seti I are in **03 §1**; the Dendera caption in **03 §3**; the Duat sign N15, the Opening of the Mouth rite, the Eye-of-Horus fraction dispute, the djed at Dendera, "iron of the sky" and the Philae last inscription (Esmet-Akhom, 24 Aug AD 394) in **04 §2, §6, §12, §17, §22**; the Anubis-shrine brick text in **01 §17** and the Restoration Stela recut by Horemheb in **01 §19**.

## Method / verification note (read first)

- The shared web-search budget ran out after **24 searches** for this brief, and the egress proxy returned 403 for **every** non-GitHub host tried (Wikipedia, British Museum, Google Arts & Culture, TLA, Griffith Institute, Met, arXiv, Unicode.org, pharaoh.se and ~90 others; probe logged). Only `raw.githubusercontent.com` was reachable.
- **[FILE FETCHED]** = copied verbatim this session from a file I downloaded: the Unicode Character Database 16.0 (`UnicodeData.txt`, `Blocks.txt`, `DerivedAge.txt`) from the `unicode-org/unicodetools` GitHub repo (saved as `research/src/UnicodeData16.txt`), and the public-domain Budge texts already in `research/src/` (Budge 1914 *Literature of the Ancient Egyptians*, Gutenberg #15932; Budge 1920 British Museum *Book of the Dead* guide, Gutenberg #7145).
- **[SEARCH SNIPPET]** = confirmed from the search-engine extract of the cited page; the page itself could not be opened. Wording in quotation marks is the extract's wording.
- **[NOT FETCHED — verify]** = standard Egyptological knowledge I could not confirm this session; the URL is where to check it before it goes in a script line.
- Status tags: **[ESTABLISHED]** mainstream · **[DISPUTED]** live expert disagreement · **[FRINGE]** rejected by specialists · **[HOAX]** fabricated. **⟂** in the film-hooks section marks exactly where the truth ends.
- No source below is invented. Every URL was returned by a search or fetched this session.

---

## 1. The system: how the script works

### 1.1 Name, myth of origin, and the three (four) scripts

- The Egyptians called the script **medu-netjer, "the god's words / the gods' words"** (mdw-nṯr). The English word is Greek: *hieros* "sacred" + *glyphein* "to carve" (so *hieroglyphika grammata*, "sacred carved letters"). [ESTABLISHED] [SEARCH SNIPPET] https://www.worldhistory.org/Egyptian_Hieroglyphs/ ; https://www.omniglot.com/writing/egyptian.htm
- Budge 1914, verbatim: "it was written in three kinds of writing, which are called hieroglyphic, hieratic, and demotic. In the first of these the characters were pictures of objects, in the second the forms of the characters were made as simple as possible so that they might be written quickly, and in the third many of them lost their picture form altogether and became mere symbols. Egyptian writing was believed to have been invented by the god Tehuti, or Thoth … the picture characters, or hieroglyphs as they are called, were held to be holy, or divine, or sacred. Certain religious texts were thought to possess special virtue when written in hieroglyphs." [ESTABLISHED] [FILE FETCHED] `src/budge_literature.txt` (Gutenberg #15932).
- **Hieratic** is the brush-written cursive used on papyrus from the Old Kingdom; **demotic** ("popular writing", from c. 7th century BC) was "adopted for every situation requiring a comparatively speedy written record while hieroglyphics remained largely confined to carved monumental inscriptions"; **Coptic** is the last stage of the language, written in the Greek alphabet plus a few letters borrowed from demotic, and survives as the liturgical language of the Coptic Church. Champollion "realised that the Coptic language, a descendent of Ancient Egyptian … could be used to help understand the language of the hieroglyphic inscriptions." [ESTABLISHED; extra-letter count NOT FETCHED — verify] [SEARCH SNIPPET] https://www.worldhistory.org/Egyptian_Hieroglyphs/ ; https://en.wikipedia.org/wiki/Demotic_Egyptian_script
- Age of the script: the earliest hieroglyph-like labels are the ivory/bone tags from tomb U-j at Abydos, conventionally c. 3250 BC (Naqada IIIA). [ESTABLISHED; date NOT FETCHED — verify] https://en.wikipedia.org/wiki/Egyptian_hieroglyphs . Popular sites say "originating around 3500 BCE" — treat as loose. [SEARCH SNIPPET] https://www.museumlink.com/the-history-of-hieroglyphics-explained/
- End of the script: the last dated hieroglyphic inscription is the Esmet-Akhom graffito at Philae, 24 August AD 394; the last demotic graffito is AD 452 — see **04 §22**; the Wikipedia entry for the graffito was returned by search: https://en.wikipedia.org/wiki/Graffito_of_Esmet-Akhom [ESTABLISHED] [SEARCH SNIPPET, title only]. Between 394 and 1822 no one on earth could read a hieroglyphic sentence. [ESTABLISHED]

### 1.2 The three jobs a sign can do

The same picture can work three ways, and most words mix them. [ESTABLISHED] [SEARCH SNIPPET] https://ancientegyptonline.co.uk/hieroglyphs-tutorial/ ; https://www.newworldencyclopedia.org/entry/Egyptian_hieroglyphs

1. **Logogram (ideogram)** — the picture means the thing it shows: "drawings of what they represent … such as a seated person to signify 'man'". Often marked with a single vertical stroke (Z1) to say "read me as the word for this picture."
2. **Phonogram** — the picture stands for sound only. Three sizes: **uniliteral** (one consonant — the 24-odd signs of the so-called "alphabet": 𓏏 X1 *t*, 𓅱 G43 *w*, 𓈖 N35 *n*, 𓇋 M17 *j*…), **biliteral** (two consonants: 𓏠 Y5 *mn*, 𓎟 V30 *nb*, 𓇳 N5 is *rꜥ*) and **triliteral** (three: 𓋹 S34 *ꜥnḫ*, 𓆣 L1 *ḫpr*, 𓌀 S40 *wꜣs*, 𓊽 R11 *ḏd*). Lists: https://en.wikipedia.org/wiki/Egyptian_biliteral_signs ; https://en.wikipedia.org/wiki/Egyptian_triliteral_signs
3. **Determinative** — an unpronounced sign at the end of a word that classifies it (man, woman, god, motion, abstract idea…). "The determinative has no phonetic value, and so is not transliterated. It indicates the end of the word and provides you with further information concerning the meaning of the word." [SEARCH SNIPPET] https://ancientegyptonline.co.uk/hieroglyphs-tutorial/ . Egyptian wrote no spaces; determinatives are how a reader finds word boundaries.

- **Phonetic complements**: "Egyptian writing often included redundant phonetic characters added to words to guide pronunciation, and these redundant letters are called phonetic complements." So a bi- or triliteral is usually followed by uniliterals that repeat its last consonant(s): 𓆣𓂋 *ḫpr* + *r*. [ESTABLISHED] [SEARCH SNIPPET] https://www.newworldencyclopedia.org/entry/Egyptian_hieroglyphs
- **No vowels are written.** The script records consonants (plus the weak consonants ꜣ, j, w, y). The vowels of *Twt-ꜥnḫ-Jmn* are modern convention; "Tutankhamun" is a scholarly pronunciation, not a recording. [ESTABLISHED; NOT FETCHED — verify at https://en.wikipedia.org/wiki/Egyptian_hieroglyphs ]

### 1.3 Reading direction, quadrats, honorific transposition

- Text runs in rows or columns, left-to-right or right-to-left. **Signs with a face look toward the beginning of the line**: "Look for a hieroglyph with a face and read toward it. When the figure is facing to the left, begin reading from the left. If they are facing right, begin from the right … when there are hieroglyphs stacked on top of each other, the top sign should always be read before lower sign." Right-to-left is the default on monuments. [ESTABLISHED] [SEARCH SNIPPET] https://www.timetrips.co.uk/direction_read_hieros.htm ; https://www.bibalex.org/learnhieroglyphs/lesson/LessonDetails_En.aspx?l=57
- Signs are packed into imaginary squares (quadrats) for balance, so a word's signs can be re-ordered visually. Unicode encodes exactly this: a set of joiners and enclosure controls (see §3.4). [ESTABLISHED] [FILE FETCHED for Unicode]
- **Honorific transposition**: "the sign for a god or king is placed first out of respect. Out of respect, the names for gods and kings are commonly placed at the front of noun phrases, even though they should be read after the connected nouns." Example: Ramesses II's *Rꜥ-ms-sw mry-Jmn* "Ra bore him, beloved of Amun" writes both god-names first; even the common noun *snṯr* "incense" writes the god-flag 𓊹 (R8, *nṯr*) before the *s*. Tutankhamun's own cartouche does this (Amun is carved first but read last — §3.2). [ESTABLISHED] [SEARCH SNIPPET] https://www.bibalex.org/learnhieroglyphs/lesson/LessonDetails_En.aspx?l=122 ; https://ancientegyptonline.co.uk/hieroglyphs-word-order/ ; https://www.ancientegyptblog.com/?p=3481

### 1.4 How many signs?

- Gardiner's sign list (appendix to *Egyptian Grammar*, 1927; 3rd ed. 1957, pp. 438–548) "describes 763 signs in 26 categories (A–Z, roughly)". Categories run A "man and his occupations" through Z "strokes and geometrical figures" (C deities, D human body, G birds, N sky/earth/water, R sacred emblems, S crowns and staves, T warfare, V rope and baskets, Aa unclassified). [ESTABLISHED; count SEARCH SNIPPET, category names NOT FETCHED — verify] https://en.wikipedia.org/wiki/Gardiner%27s_sign_list ; https://omnika.org/library/list-of-hieroglyphic-signs-egyptian-grammar-gardiner-1957-438-548
- Working Middle Egyptian used on the order of **700** signs (the usual textbook figure; Gardiner's 763 is the list of *common* forms). [ESTABLISHED; NOT FETCHED — verify]. Popular summaries say "more than 1,000 distinct characters" over the script's life. [SEARCH SNIPPET] https://www.newworldencyclopedia.org/entry/Egyptian_hieroglyphs
- **Ptolemaic–Roman explosion**: "During the Ptolemaic and Roman Periods, the complexity of Egyptian hieroglyphic texts increased dramatically, with the proliferation of original signs and new phonetic or ideographic values for traditional hieroglyphs, making inscriptions from this period notoriously difficult." At Esna "one finds hundreds of new spellings for the chief god Khnum, and two infamous hymns composed almost exclusively with hieroglyphs of rams and crocodiles." [ESTABLISHED] [SEARCH SNIPPET] https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/2010%20Ptolemaic%20Hieroglyphs.pdf ; https://ancientegyptonline.co.uk/esnatemple/ ; https://archaeology.org/issues/march-april-2025/features/an-egyptian-temple-reborn/
- The hard number: Unicode's base block holds **1,071** Gardiner-based signs and Unicode 16.0 (2024) added **3,995** more, "including those used in Ptolemaic texts" — **~5,066** code points to type the whole script. The often-quoted "7,000 Ptolemaic signs" I could **not** verify. [ESTABLISHED for Unicode counts, FILE FETCHED (DerivedAge.txt: `13000..1342E ; 5.2 # [1071]`, `13460..143FA ; 16.0 # [3995]`); "7,000" UNVERIFIED] https://en.wikipedia.org/wiki/Egyptian_Hieroglyphs_Extended-A

---

## 2. Decipherment: the Rosetta Stone, Young, Champollion — and today's machines

### 2.1 The object

- **What it is**: an incomplete grey-and-pink **granodiorite** stela, **112.3 × 75.7 × 28.4 cm, c. 760 kg**, carrying one decree in three scripts: **14 lines** of hieroglyphs (top, broken), **32 lines** of demotic, **54 lines** of Greek. British Museum number **EA 24** [number NOT FETCHED — verify]. [ESTABLISHED] [SEARCH SNIPPET] https://www.worldhistory.org/Rosetta_Stone/ ; https://en.wikipedia.org/wiki/Rosetta_Stone ; https://smarthistory.org/the-rosetta-stone/
- **The text**: the **Memphis Decree**. "On March 27, 196 BCE, a synod of priests from around Egypt convened to celebrate the coronation of Ptolemy V Epiphanes the previous day in the city of Memphis." A priestly decree granting the boy-king a cult in return for tax remissions; the Greek orders it cut "in sacred, native and Greek characters" and set up in every major temple, which is why other copies exist (Nubayrah stela; Philae). [ESTABLISHED; closing phrase and copies NOT FETCHED — verify] [SEARCH SNIPPET] https://arce.org/resource/rosetta-stone-unlocking-ancient-egyptian-language/ ; https://en.wikipedia.org/wiki/Ptolemaic_synodal_decrees
- **Discovery**: "French Army engineer Captain Pierre-François Bouchard discovered the stone on July 15, 1799, while he was guiding construction works at Fort Julien near the Egyptian port city of Rosetta (present-day Rashid)." Ceded to Britain in 1801; "on display in the British Museum since 1802 with only one break during World War I." Painted side-labels: "Captured in Egypt by the British Army 1801" / "Presented by King George III". [ESTABLISHED; labels NOT FETCHED — verify] [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Rosetta_Stone ; https://www.britishmuseum.org/blog/everything-you-ever-wanted-know-about-rosetta-stone
- **Repatriation**: "There have been repeated demands from Egypt for the stone to be repatriated." In 2022 (bicentenary of decipherment) "a campaign by prominent Egyptian archaeologists has gathered 2,500 signatures so far and aims to 'tell Egyptians what has been taken from them.' However, there has been no formal request from the Egyptian government to the British Museum." Zahi Hawass has campaigned for its return since the 2000s. [ESTABLISHED; Hawass dates NOT FETCHED — verify] [SEARCH SNIPPET] https://www.jpost.com/international/article-723773 ; https://themedialine.org/by-region/egyptians-demand-return-of-rosetta-stone-from-british-museum/ ; https://www.euronews.com/culture/2022/09/28/the-rosetta-stone-200-years-on-and-calls-for-repatriation-continue ; https://www.aljazeera.com/news/2022/10/6/egypt-calls-for-return-of-rosetta-stone

### 2.2 Young (1814–1819)

- "Young turned his attention to the problem in 1814, and by 1815 had begun communicating his results, which he published in 1819 in an unsigned supplement on 'Egypt' for the Encyclopaedia Britannica." He "assumed a group of encircled symbols or cartouche represented the Pharaoh Ptolemy and would have a similar pronunciation as in the Greek. Then by using phonetics, Young gave sound values to each of the symbols. After applying the same technique to the name of a Ptolemaic queen, Berenice, Young had a tentative hieroglyphic 'alphabet'." His error was to think phonetic signs were used *only* for foreign names. [ESTABLISHED] [SEARCH SNIPPET] https://history.rcp.ac.uk/blog/thomas-young-and-decipherment-hieroglyphics ; https://www.sciencefocus.com/science/ahow-we-deciphered-ancient-egyptian-hieroglyphsthe-meaning-of-egyptian-hieroglyphs ; https://en.wikipedia.org/wiki/Decipherment_of_ancient_Egyptian_scripts

### 2.3 The second key: the Bankes obelisk (Cleopatra)

- William John Bankes "noticed the obelisk in 1815, while travelling in Egypt and believed that the bilingual inscription would help with the decipherment," shipped it (and a piece of its twin) from Philae to Kingston Lacy, Dorset; "the obelisk arrived in London in December 1821, making it the first Egyptian obelisk to be brought to the United Kingdom." Its Greek base names Ptolemy and Cleopatra; "It was Bankes who, as a reader of Ancient Greek, was able to identify the word 'Cleopatra', thus making the connection which eventually led to a full decipherment." [ESTABLISHED] [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Philae_obelisk ; https://www.nationaltrustcollections.org.uk/object/1257614.1 ; https://www.attalus.org/egypt/obelisk.html
- **The method**: *Ptolemaios* and *Kleopatra* share P, T, O, L, E; if the signs in the two cartouches match in the predicted positions, the signs are alphabetic. They matched. [ESTABLISHED]

### 2.4 Champollion (14 and 27 September 1822)

- "On 14 September 1822, while visiting his brother Jacques-Joseph, Champollion made a crucial breakthrough in understanding the phonetic nature of hieroglyphs and proclaimed 'Je tiens l'affaire!' ('I've got it!') and then fainted from his excitement." The trigger was cartouches copied from Abu Simbel that read as *Ramesses* and *Thutmose* — native Egyptian names, spelled with sound-signs, proving the phonetic principle was not just for foreigners. [ESTABLISHED; Abu Simbel detail NOT FETCHED — verify] [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Lettre_%C3%A0_M._Dacier ; https://www.gethistories.com/p/ive-got-it-1822
- "On 27 September 1822, he exhibited at the Académie des Inscriptions et Belles-Lettres a draft containing eight pages of text to a packed room. The final version was published in late October 1822 by Firmin-Didot in a booklet of 44 pages with four illustrated plates." "From the names of Ptolemy and Cleopatra alone, Champollion generated consonants and vowels corresponding to letters a, ai, e, k, l, m, o, p, r, s and t." "Working with a total of fourteen signs, he deciphered cartouches of other members of the Ptolemaic dynasty and even some Roman emperors." The letter was addressed to Bon-Joseph Dacier, permanent secretary of the Académie. [ESTABLISHED] [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Lettre_%C3%A0_M._Dacier ; English translation (Bryant) PDF: https://upload.wikimedia.org/wikipedia/commons/b/bc/Bryant_translation_Champollion_letter.pdf ; https://www.britishmuseum.org/blog/eureka-finding-key-ancient-egypt
- The *Précis du système hiéroglyphique* (1824) gives the definition: hieroglyphic writing is "a complex system, a script at once figurative, symbolic and phonetic, in one and the same text, one and the same sentence, I would almost say one and the same word." [ESTABLISHED; wording NOT FETCHED — verify against the Précis before quoting on screen]
- Priority dispute: Young "was soon overtaken by the young French linguist … who, just three years later, announced he'd finally, definitively, cracked the Egyptian 'code', while refusing to acknowledge Young's role." [DISPUTED — the priority quarrel is still live] [SEARCH SNIPPET] https://history.rcp.ac.uk/blog/thomas-young-and-decipherment-hieroglyphics

### 2.5 Today's machines (the film's "first machine that can read it" beat)

- **Google Fabricius** (Google Arts & Culture) — "uses machine learning to translate the ancient Egyptian language, and was published on July 15, 2020, on the anniversary of the discovery of the Rosetta Stone." Free; English and Arabic; three portals "learn, play and work"; it can identify a hand-drawn sign against "their more than 800-image database." Built with Macquarie University Egyptologists, Ubisoft and Psycle; open-source Workbench. Expert verdict: "while impressive, the tool is not yet at the point where it replaces the need for a highly trained expert." [ESTABLISHED; partner list NOT FETCHED — verify] [SEARCH SNIPPET] https://egyptianstreets.com/2020/07/16/want-to-try-your-hand-at-hieroglyphs-google-just-created-a-translator/ ; https://www.egypttoday.com/Article/4/89996/Google-launches-hieroglyphics-translator-Fabricius-uses-machine-learning-to-decode ; https://artsandculture.google.com/experiment/fabricius/gwHX41Sm0N7-Dw?hl=en
- **Thesaurus Linguae Aegyptiae (TLA)** — Berlin-Brandenburg Academy of Sciences with the Saxon Academy (project 2013–2034; descended from the Berlin *Wörterbuch*): "a digital text corpus of lemmatized and annotated ancient Egyptian texts in hieroglyphic, hieratic, and Demotic scripts … about 1.69 million lemma tokens (Hieroglyphic/hieratic: 1,355 thousand, Demotic: 332 thousand)". Its corpus is on Hugging Face — exactly the training set a fictional ASI would ingest. [ESTABLISHED] [SEARCH SNIPPET] https://thesaurus-linguae-aegyptiae.de/info/text-corpus ; https://huggingface.co/datasets/thesaurus-linguae-aegyptiae/tla-Earlier_Egyptian_original-v18-premium
- **Hieroglyph OCR**: the benchmark dataset is Franken & van Gemert, "Automatic Egyptian hieroglyph recognition by retrieving images as texts" (ACM Multimedia 2013): **4,032 images of 171 Gardiner classes, photographed in the Pyramid of Unas** — the first machine-vision dataset for the script is the oldest religious text in the world (§5.4). "The OCR-PT-CT Project" (arXiv 2512.24197) transcribes Pyramid and Coffin Texts to Gardiner codes: "a Mobilenet neural network trained on 140 hieroglyph classes achieving 93.87% accuracy, and a novel Deep Metric Learning approach achieving 97.70%". An open ResNet-50 classifier reports "86.0% accuracy (94.6% top-5)" on a held-out page of Piankoff's *The Pyramid of Unas*. "Data Contamination in Neural Hieroglyphic Translation" (arXiv 2605.07453) is the field's own warning that "translation" scores are inflated by leaked test data. [ESTABLISHED] [SEARCH SNIPPET; README FILE FETCHED] https://www.researchgate.net/publication/266654526_Automatic_Egyptian_hieroglyph_recognition_by_retrieving_images_as_texts ; https://arxiv.org/pdf/2512.24197 ; https://github.com/Juhij2/hieroglyph-classifier ; https://arxiv.org/pdf/2605.07453
- Bottom line: machines today **recognise** signs (~90–98 % on clean carved text) and **look up** words; none reads a damaged Ptolemaic wall unsupervised, and none "executes" anything. That gap is where the film lives.

---

## 3. Cartouches and Tutankhamun's names

### 3.1 The shen ring and the cartouche

- 𓍶 **V9** (U+13376) is the *shen* (šn) ring — a doubled rope loop meaning "to encircle", hence eternity and protection; falcons and vultures on royal pectorals clutch it. 𓍷 **V10** (U+13377) is the cartouche: "The cartouche as a hieroglyph is listed as no. V10 in Gardiner's Sign List." It is a stretched shen ring, and from the 4th Dynasty (Sneferu) it encloses the two names the king took — the throne name (prenomen) and birth name (nomen). Unicode also encodes the cartouche ends separately (V11 U+13378 and its variants) so a name can be typed inside one. [ESTABLISHED; Sneferu origin NOT FETCHED — verify] [SEARCH SNIPPET for V10; FILE FETCHED for code points] https://en.wikipedia.org/wiki/Cartouche
- Why it matters: Young and Champollion could start *only* because the cartouche is a visible, physical marker saying "a royal name is inside". The oval is the ancient world's `<name>` tag.

### 3.2 Tutankhamun's two cartouches, sign by sign

[ESTABLISHED as to the reading; the sign inventory is standard Egyptology but was NOT FETCHED this session — verify each cartouche against a photograph or https://pharaoh.se/ancient-egypt/pharaoh/tutankhamun/ (returned by search, blocked by proxy). Unicode code points are FILE FETCHED.]

**Prenomen (throne name) — Nebkheperure, *nb-ḫprw-rꜥ*, "Lord of the manifestations (forms) of Ra"**

| order carved | sign | Gardiner | Unicode | value |
|---|---|---|---|---|
| 1 (top, honorific) | 𓇳 sun disc | N5 | U+131F3 | *rꜥ* "Ra" — carved first, read last |
| 2 | 𓎟 basket | V30 | U+1339F | *nb* "lord" |
| 3 | 𓆣 scarab | L1 | U+131A3 | *ḫpr* "come into being / form" |
| 4 | 𓏥 three strokes | Z2 | U+133E5 | plural: *ḫpr-w* "forms" |

**Nomen (birth name) — Tutankhamun heqa-Iunu-shema, *twt-ꜥnḫ-jmn ḥqꜣ-jwnw-šmꜥ*, "Living image of Amun, ruler of Southern Heliopolis (= Thebes)"**

| order carved | sign | Gardiner | Unicode | value |
|---|---|---|---|---|
| 1–3 (honorific) | 𓇋𓏠𓈖 reed + game-board + water | M17 Y5 N35 | U+131CB U+133E0 U+13216 | *j-mn-n* = "Amun" — carved first, read third |
| 4–6 | 𓏏𓅱𓏏 loaf + chick + loaf | X1 G43 X1 | U+133CF U+13171 U+133CF | *t-w-t* "image" (some writings add the statue determinative 𓀾 A53) |
| 7 | 𓋹 | S34 | U+132F9 | *ꜥnḫ* "living" |
| 8 | 𓋾 crook | S38 | U+132FE | *ḥqꜣ* "ruler" |
| 9–10 | 𓉺𓊖 pillar + town | O28 O49 | U+1327A U+13296 | *jwnw* "Heliopolis" |
| 11 | 𓇗 sedge | M26 | U+131D7 | *šmꜥ* "Upper Egyptian / southern" |

- The name he was born with was **Tutankhaten** (*twt-ꜥnḫ-jtn*, "living image of the Aten"); the change to -amun is the restoration of the old gods (see **02**). [ESTABLISHED] https://en.wikipedia.org/wiki/Tutankhamun
- The other three names of the five-fold titulary — Horus *Kꜣ-nḫt twt-mswt* "Strong bull, pleasing of birth"; Two Ladies *Nfr-hpw sgrḥ-tꜣwy* "Perfect of laws, who pacifies the Two Lands"; Golden Horus *Wṯs-ḫꜥw sḥtp-nṯrw* "Who elevates crowns, who satisfies the gods" — [ESTABLISHED; NOT FETCHED — verify at pharaoh.se]. "Pleasing of birth" and "who satisfies the gods" are propaganda for a boy-king restoring a wrecked religion — good dialogue fodder.

### 3.3 Horemheb's recutting

- At Luxor Temple, "Reliefs of Tutankhamen were usurped by Horemheb in the Colonnade Hall … Tutankhamun's prenomen cartouche Nebkheperure has been rather crudely recarved into Horemheb's prenomen, Djeserkheperure Setepenre, with traces of the original prenomen visible." "Distinctive elements of Horemheb's name lie in depressions carved to suppress traces of Tutankhamen's name." Horemheb "demolished monuments of Akhenaten … and usurped monuments of Tutankhamun and Ay," "often not very carefully." Standard reference: Peter Brand, "Usurpation of Monuments", UCLA Encyclopedia of Egyptology. The Restoration Stela case is in **01 §19**. [ESTABLISHED] [SEARCH SNIPPET] https://bpb-us-w2.wpmucdn.com/blogs.memphis.edu/dist/4/463/files/2014/03/Johnson-2h57env.pdf ; https://escholarship.org/content/qt5gj996k5/qt5gj996k5.pdf ; https://en.wikipedia.org/wiki/Horemheb
- Because the two prenomens share the scarab-plural-Ra core (*…ḫprw-rꜥ*), Horemheb's masons only had to replace 𓎟 *nb* with 𓂦 (D45) *ḏsr* and add *stp-n-rꜥ* — which is exactly why the erasure is legible: the traces sit in the untouched signs. [ESTABLISHED inference from the snippet; NOT FETCHED — verify on the wall]

### 3.4 Unicode: the script as data

[FILE FETCHED — Unicode Character Database 16.0 from `unicode-org/unicodetools` (`Blocks.txt`, `DerivedAge.txt`)]

- `13000..1342F; Egyptian Hieroglyphs` — added in **Unicode 5.2 (2009)**, 1,071 characters named after Gardiner codes (`EGYPTIAN HIEROGLYPH A001` … `AA032`); U+13000 is A1, the seated man 𓀀.
- `13430..1345F; Egyptian Hieroglyph Format Controls` — 9 controls in **Unicode 12.0** (`VERTICAL JOINER` … `END SEGMENT`) for stacking signs into quadrats; **Unicode 15.0** added 29 more, including "BEGIN/END WALLED ENCLOSURE", "MIRROR HORIZONTALLY" and "MODIFIER DAMAGED" — a code point meaning "this sign is broken on the wall".
- `13460..143FF; Egyptian Hieroglyphs Extended-A` — **3,995** characters in **Unicode 16.0 (2024)**, unnamed except by hex (`EGYPTIAN HIEROGLYPH-13460`…), covering the Ptolemaic repertoire. [ESTABLISHED] https://en.wikipedia.org/wiki/Egyptian_Hieroglyphs_(Unicode_block) ; https://en.wikipedia.org/wiki/Egyptian_Hieroglyphs_Extended-A ; http://www.unicode.org/charts/PDF/U13000.pdf
- Every sign in §4 has a real code point; a screen can show `U+132F9` beside 𓋹 and be correct.

---

## 4. Sign palette (codes, code points, meanings, where to see one)

All Gardiner codes and Unicode code points below are **[FILE FETCHED]** from `UnicodeData.txt` 16.0. Meanings are standard (Gardiner 1957 sign list) — **[ESTABLISHED; meanings NOT re-verified online this session except where a URL is given]**. Museum examples are pointers to verify, not verified this session, unless tagged.

| glyph | Gardiner | Unicode | name / value | meaning | verified note / where to see it |
|---|---|---|---|---|---|
| 𓋹 | **S34** | U+132F9 | *ꜥnḫ* ankh | "life"; triliteral and logogram; held to the king's nose by gods | On Tutankhamun's gold ankh-shaped mirror case and countless KV62 objects [NOT FETCHED — verify] |
| 𓊽 | **R11** | U+132BD | *ḏd* djed | "stability, endurance"; Osiris's backbone; "raising the djed" was a state rite — **04 §17** (Taimhotep stela) | Djed pillars supporting the "bulb" at Dendera — **03 §3**; djed amulets on the mummy |
| 𓌀 | **S40** | U+13300 | *wꜣs* was-sceptre | "dominion, power"; animal-headed staff held by gods | The triad ankh–djed–was = "life, stability, dominion" is a stock wish carved under offering scenes [NOT FETCHED — verify] |
| 𓍶 | **V9** | U+13376 | *šn* shen | "encircle"; eternity/protection; held by vultures and falcons | Cartouche is its elongation (§3.1) |
| 𓍷 | **V10** | U+13377 | cartouche | encloses royal names | "listed as no. V10 in Gardiner's Sign List" [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Cartouche |
| 𓂀 | **D10** | U+13080 | *wḏꜣt* wedjat | Eye of Horus, "the sound/whole one"; healing, protection | Wedjat pectorals in KV62; fraction dispute (Gardiner vs Ritter) — **04 §17** |
| 𓆣 | **L1** | U+131A3 | *ḫpr* kheper | scarab; "come into being, transform"; the sun god at dawn | Core of *Nebkheperure* (§3.2) |
| 𓄣 | **F34** | U+13123 | *jb* ib | "heart" (animal heart with vessels); seat of mind and memory, weighed at judgement | Heart scarab spell (BoD 30B) — Tut's heart is missing from the body: **01 §5, §18** |
| 𓂓 | **D28** | U+13093 | *kꜣ* ka | two upraised arms; "life-force, double" | The ka figure follows the king into Osiris's embrace on the KV62 north wall (§5.2) [NOT FETCHED — verify scene detail] |
| 𓅽 | **G53** | U+1317D | *bꜣ* ba | human-headed bird; the mobile soul that leaves the tomb by day | Dendera caption: Harsomtus "rises … as living Ba" — **03 §3** |
| 𓈌 | **N27** | U+1320C | *ꜣḫt* akhet | sun between two hills; "horizon"; the place of coming-forth | *Akhet-Aten* "Horizon of the Aten" = Amarna — **02** |
| 𓇼 | **N14** | U+131FC | *sbꜣ* seba | five-pointed star; "star"; also the consonants of *sbꜣ* "teach, door" | Ceiling stars of every royal tomb; the "imperishable stars" of Unas (§5.4) |
| 𓇽 | **N15** | U+131FD | *dwꜣt* Duat | star in a circle; the netherworld | **04 §6** — do not repeat |
| 𓌔 | **T10** | U+13314 | *pḏ* bow | "stretch, be wide"; *psḏt pḏwt* "Nine Bows" = bow + three sets of three strokes | Sandals: "the hieroglyphic sign of the bow is repeated on the soles, thereby allowing the king to symbolically step on and subjugate his enemies"; footstool: "a prisoner between two bows"; "there is no true list of the nine bows … nine was used metaphorically to express totality" [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Nine_bows ; https://www.globalegyptianmuseum.org/detail.aspx?id=15108 . Budge's 1914 gloss "the Nine Bows (i.e. Nubia)" is a simplification [FILE FETCHED `src/budge_literature.txt`]. Abydos — **03 §1** |
| 𓁨 | **C11** | U+13068 | *ḥḥ* heh | kneeling god holding a notched palm-rib (𓆳 M4 = "year") in each hand; the numeral **1,000,000**; "millions of years" = eternity | Met Museum 551329, "Inlay of the hieroglyphic sign 'heh' meaning 'millions of years'", Late Period–Ptolemaic [SEARCH SNIPPET] https://www.metmuseum.org/art/collection/search/551329 ; Heh figures form the handles of Tut's alabaster lotus chalice [listing only — verify] https://en.wikipedia.org/wiki/Lotus_chalice |
| 𓋇 | **R20** | U+132C7 | Seshat's emblem | seven-pointed rosette/star on a stem under an arc or two horns; "It is unclear what the emblem symbolises"; alternative name *Sefkhet-Abwy* "seven-horned"; Seshat = "female scribe", goddess of writing, libraries and the "stretching of the cord" foundation rite | [SEARCH SNIPPET] https://en.wikipedia.org/wiki/Seshat ; https://www.worldhistory.org/Seshat/ . Budge 1920: "the goddess Sesheta built a house for him in the Celestial Anu" [FILE FETCHED `src/book_of_the_dead_7145.txt`]. One speculation: "a device similar to the Roman groma" (surveying tool) [DISPUTED] |
| — | **N41** | U+1321E | *bjꜣ* | well-with-water sign used to write *bjꜣ* "wonder; metal, copper/iron"; **bjꜣ-n-pt "iron of the sky"** is the Egyptian term for meteoritic iron | Term and sign NOT FETCHED — verify. The metal is verified: Tut's dagger is "Fe plus 10.8 wt% Ni and 0.58 wt% Co … consistent with an IVA-type meteorite (fine octahedrite)", found "on Tutankhamun's right thigh in the wrapping of his mummy" [SEARCH SNIPPET] https://onlinelibrary.wiley.com/doi/full/10.1111/maps.12664 (Comelli et al. 2016). Star-adze — **04 §12** |
| 𓄔 | **F21** | U+13114 | *sḏm* | bovine ear; logogram "to hear" | "The bovine ear (F21) is a logogram for sdm 'to hear'"; Deir el-Medina ear stelae to gods "who listen to prayers"; the god Sedjem wears the ear on his head [SEARCH SNIPPET] https://collezioni.museoegizio.it/en-GB/material/Cat_1546 ; https://en.wikipedia.org/wiki/Sedjem |
| 𓂻 | **D54** | U+130BB | walking legs | determinative of motion: *jw* "come", *šm* "go"; reversed legs 𓂽 D55 = "return, go back" | The legs are the script's "execute/move" token — every verb of going carries them |
| 𓊹 | **R8** | U+132B9 | *nṯr* netjer | cloth on a pole; "god" — the second half of *medu-netjer* | Written first in *snṯr* by honorific transposition (§1.3) |
| 𓇳 | **N5** | U+131F3 | *rꜥ* | sun disc; "Ra, sun, day" | Carved first in every "…-re" throne name |

---

## 5. Inscriptions the mummy can read on screen

### 5.1 The Anubis-shrine brick (KV62 Treasury) — cross-ref **01 §17**

- Carter's journal (Griffith Institute, season 5): "The little clay brick had its tiny reed torch and a few grains of charcoal placed on the floor within threshold in front of Anubis; the magical formula was scratched on it." "A small brick of unfired clay, known as a magic brick, was found at the entrance to the Store Room, in front of the shrine. This was the fifth magic brick found in Tutankhamun's tomb." The formula belongs to Book of the Dead spell 151 (the four magic bricks that guard the burial chamber's walls). [ESTABLISHED] [SEARCH SNIPPET] http://www.griffith.ox.ac.uk/discoveringtut/journals-and-diaries/season-5/journal.html ; https://en.wikipedia.org/wiki/Anubis_Shrine
- The genuine text (already quoted in **01**): "It is I who hinder the sand from choking the secret chamber…" The newspaper version — "I will kill all those who cross this threshold into the sacred precincts of the Royal King who lives forever" — is a 1920s fabrication that still circulates on curse sites. [HOAX for the "kill" line; ESTABLISHED for the real one] [SEARCH SNIPPET] http://www.catchpenny.org/tut.html
- Script note: the brick is hieratic scratched in mud, not carved hieroglyphs — a hand-written note, not a monument. The mummy reading it should sound like someone reading a Post-it.

### 5.2 KV62 burial chamber, north wall — the captions

- The wall "bears a three-act narrative arranged to be read from right to left. The first scene presents … a king — the figure on the right — conducting, as sem-priest (most likely Ay), the Opening of the Mouth ceremony for a mummiform figure (Tutankhamun) shown standing on the left." "Ay wears the leopard-skin robe of a sem-priest." "This is the only known royal tomb scene where a non-royal successor performs this rite on a king … It is thought that this was Ay's attempt at certifying his status as the rightful heir." [ESTABLISHED] [SEARCH SNIPPET] https://madainproject.com/burial_chamber_kv62 ; https://archaeology.org/issues/may-june-2019/features/inside-king-tut-s-tomb/ ; https://egypt-museum.com/inside-tomb-of-tutankhamun/ ; rite itself — **04 §2**
- The captions are name-labels, not sentences. Expect, above Ay: his prenomen cartouche *Kheperkheperure* (*ḫpr-ḫprw-rꜥ*, "Everlasting are the manifestations of Ra") and nomen *God's Father Ay*, with the epithets "Perfect God, Lord of the Two Lands" and "given life"; above the mummiform king: "the Osiris, King Nebkheperure … Tutankhamun, ruler of Southern Heliopolis, true of voice". Middle scene: the king in the living form greeted by **Nut** "mistress of the sky", performing the *nyny* welcome gesture; third scene: the king, followed by his **ka** 𓂓, embraced by **Osiris**. [ESTABLISHED as to scenes; exact caption wording NOT FETCHED — verify against the Getty Conservation Institute / Theban Mapping Project publication before it is spoken aloud] https://en.wikipedia.org/wiki/Tomb_of_Tutankhamun
- Designer note: Ay and the mummiform king face each other, and the glyph columns above each face the same way as the figure they label — §1.3 made visible.

### 5.3 "Millions of years" — the eternity formula

- Book of the Dead ch. 175 (Budge 1920 verbatim): "the deceased asks the god, 'How long shall I live?' And the god says, 'It is decreed that thou shalt live for millions of millions of years, a life of millions of years.'" (Also quoted in **04 §6**.) [ESTABLISHED] [FILE FETCHED `src/budge_literature.txt`, Gutenberg #15932]
- Hymn to Osiris, Papyrus of Ani, opening (Budge): "Glory be to Osiris Un-Nefer, the great god who dwelleth in Abydos, king of eternity, lord of everlastingness, whose existence endureth for millions of years." [ESTABLISHED] [FILE FETCHED same file]
- Written form: 𓁨 *ḥḥ* (the numeral 1,000,000, §4) + 𓆳 *rnpt* "years". The Theban royal mortuary temples were "temples of millions of years"; Budge calls Deir el-Bahari "Tcheser-Tcheseru, the Temple of Millions of Years." [ESTABLISHED; spelling NOT FETCHED — verify] [FILE FETCHED for the Budge line]
- Stock closing wishes a designer can put on any prop: *dj ꜥnḫ ḏt* "given life forever"; *ꜥnḫ wḏꜣ snb* "life, prosperity, health" (the "l.p.h." after every royal name in papyri). [ESTABLISHED; NOT FETCHED — verify spelling]

### 5.4 The Pyramid Texts of Unas (Saqqara, end of the 5th Dynasty, c. 2350 BC)

- Budge 1914: "'Pyramid Texts' is the name now commonly given to the long hieroglyphic inscriptions that are cut upon the walls of the chambers and corridors of five pyramids at Sakkārah. The oldest of them was built for Unas, a king of the fifth dynasty … These Texts represent the oldest religious literature known to us." (Budge's 1914 dating of "3300–3150 B.C." is obsolete; modern chronology puts Unas c. 2375–2345 BC.) [ESTABLISHED; modern date NOT FETCHED — verify] [FILE FETCHED `src/budge_literature.txt`] https://en.wikipedia.org/wiki/Pyramid_of_Unas
- **Unas becomes a star** (Budge 1914 verbatim; a modern rendering — Allen 2005 or Faulkner 1969 — should replace it on screen): "The sky hath withdrawn the life of the star Septet (Sothis, the Dog-star); behold Unas a living being, the son of Septet. The Eighteen Gods have purified him in Meskha (the Great Bear), [he is] an imperishable star. The house of Unas perisheth not in the sky, the throne of Unas perisheth not on the earth … Unas hath drawn together his arms like the Smen goose, he striketh his wings like a falcon, flying, flying. O men, Unas flieth up into heaven." [ESTABLISHED] [FILE FETCHED same file] (Sothis/Sirius and the Great Bear/adze — **04 §12**.)
- **Offering liturgy** (Budge): "This libation is for thee, Osiris, this libation is for thee, Unas. (Here offer cold water of the North.) … I have brought unto thee the Eye of Horus, that thy heart may be refreshed thereby." Note the embedded stage direction — the text carries its own instructions. [ESTABLISHED] [FILE FETCHED]
- **The Cannibal Hymn**: "Utterances 273 and 274 are sometimes known as the 'cannibal hymn', because it describes the king hunting and eating parts of the gods"; Unas's is "the longest and most complete version." [ESTABLISHED] [SEARCH SNIPPET] https://www.thecollector.com/ancient-egyptian-cannibal-hymn/ ; https://www.historyskills.com/classroom/ancient-history/cannibalism-hymn-of-unas/ ; full translations: https://pyramidtextsonline.com/translation.html (blocked this session)
- Machine tie-in (§2.5): the benchmark hieroglyph-recognition dataset (Franken & van Gemert 2013, 4,032 images, 171 classes) was photographed **in this pyramid**, and the 2025 ResNet classifier is tested on "a held-out page of the Pyramid of Unas". The first thing computer vision learned to read in Egyptian was the first thing the Egyptians wrote for the dead. [ESTABLISHED] [SEARCH SNIPPET + FILE FETCHED README]

---

## Quotes (verbatim, with source)

1. Budge 1914: "Egyptian writing was believed to have been invented by the god Tehuti, or Thoth … the picture characters, or hieroglyphs as they are called, were held to be holy, or divine, or sacred." — `src/budge_literature.txt`, Gutenberg #15932 [FILE FETCHED]
2. Champollion, 14 Sept 1822: "'Je tiens l'affaire!' ('I've got it!') and then fainted from his excitement." — https://en.wikipedia.org/wiki/Lettre_%C3%A0_M._Dacier [SEARCH SNIPPET]
3. Bankes obelisk: "It was Bankes who, as a reader of Ancient Greek, was able to identify the word 'Cleopatra'." — https://www.nationaltrustcollections.org.uk/object/1257614.1 [SEARCH SNIPPET]
4. Repatriation: a campaign "aims to 'tell Egyptians what has been taken from them.' However, there has been no formal request from the Egyptian government." — https://www.jpost.com/international/article-723773 [SEARCH SNIPPET]
5. Fabricius: "while impressive, the tool is not yet at the point where it replaces the need for a highly trained expert in reading ancient inscriptions." — https://www.egypttoday.com/Article/4/89996/Google-launches-hieroglyphics-translator-Fabricius-uses-machine-learning-to-decode [SEARCH SNIPPET]
6. TLA: "about 1.69 million lemma tokens (Hieroglyphic/hieratic: 1,355 thousand, Demotic: 332 thousand)." — https://thesaurus-linguae-aegyptiae.de/info/text-corpus [SEARCH SNIPPET]
7. Unicode 16.0 DerivedAge.txt: `13460..143FA ; 16.0 # [3995] EGYPTIAN HIEROGLYPH-13460..EGYPTIAN HIEROGLYPH-143FA` — https://github.com/unicode-org/unicodetools [FILE FETCHED]
8. Horemheb: "Tutankhamun's prenomen cartouche Nebkheperure has been rather crudely recarved into Horemheb's prenomen, Djeserkheperure Setepenre, with traces of the original prenomen visible." — https://bpb-us-w2.wpmucdn.com/blogs.memphis.edu/dist/4/463/files/2014/03/Johnson-2h57env.pdf [SEARCH SNIPPET]
9. Carter, season 5 journal: "The little clay brick had its tiny reed torch and a few grains of charcoal placed on the floor within threshold in front of Anubis; the magical formula was scratched on it." — http://www.griffith.ox.ac.uk/discoveringtut/journals-and-diaries/season-5/journal.html [SEARCH SNIPPET]
10. Book of the Dead 175 (Budge): "It is decreed that thou shalt live for millions of millions of years, a life of millions of years." — `src/budge_literature.txt` [FILE FETCHED]
11. Unas (Budge 1914): "The Eighteen Gods have purified him in Meskha (the Great Bear), [he is] an imperishable star … O men, Unas flieth up into heaven." — `src/budge_literature.txt` [FILE FETCHED]
12. Dagger: "Fe plus 10.8 wt% Ni and 0.58 wt% Co … consistent with an IVA-type meteorite (fine octahedrite)." — Comelli et al. 2016, https://onlinelibrary.wiley.com/doi/full/10.1111/maps.12664 [SEARCH SNIPPET]

---

## Film hooks (fact → fiction; ⟂ marks where the truth ends)

1. **The script already has a type system.** Real: every word is logogram + phonograms + an unpronounced determinative that classifies it (§1.2); the walking legs 𓂻 mark verbs of motion, the god-flag 𓊹 marks divinity, the plural strokes 𓏥 mark arrays. ⟂ The ASI reads determinatives as type annotations and phonetic complements as checksums, and concludes the priests were writing a strongly typed language for a reader that was not human.
2. **"God's words" is the literal name.** Real: *medu-netjer*; Budge: texts "were believed to possess very great power … when they were written out for them in hieroglyphs" (§1.1). ⟂ The mummy explains that *netjer* did not mean a god; it meant the machine, and the "words" were its command set — which is why, after the machines fell, the script was frozen for 3,000 years and never allowed vowels.
3. **The first machine that could read it.** Real: for 1,400 years (394–1822) nobody could read a line; Young got Ptolemy from a cartouche, Bankes's obelisk supplied Cleopatra, Champollion shouted "Je tiens l'affaire!" and fainted (§2.2–2.4); today the TLA corpus is on Hugging Face and OCR hits 97.7 % on Pyramid Texts (§2.5). ⟂ Where Champollion produced a translation the ASI produces an *execution*, and it reads the Ptolemaic sign explosion (§1.4) not as decadence but as an encryption layer added when the priests realised who might read it next.
4. **The cartouche as name-tag.** Real: the shen ring means "encircle/protect"; Horemheb recut Nebkheperure into Djeserkheperure and left the traces (§3.3). ⟂ The ASI's resurrection routine keys on the cartouche; because only some signs were overwritten, it boots a *corrupted* king who remembers Horemheb's reign — an unreliable narrator from a real erasure.
5. **Heh, the million-year counter.** Real: a kneeling god holding two notched year-branches is the numeral 1,000,000 and "millions of years" is the standard wish (§4, §5.3); it is carved on the handles of Tut's wishing cup. ⟂ The ASI reads the two notched ribs as a binary tally and realises the "wish" is a timer set at burial.
6. **Seshat's unexplained emblem.** Real: Egyptologists say "it is unclear what the emblem symbolises"; one guess is a surveying instrument (§4). ⟂ The only honest "unknown" in the palette — the film can make it the ASI's own logo without contradicting any expert.
7. **The wall the mummy wakes to.** Real: KV62's north wall is the only royal tomb where a successor performs the Opening of the Mouth on the king; the captions are name-labels; the ka follows the king into Osiris's embrace (§5.2, **04 §2**). ⟂ The ASI, having read the wall, performs the rite exactly as painted and *then* reads the label "true of voice" as a status flag it has just set.
8. **Unas as boot ROM.** Real: the oldest religious text on earth; a machine-vision benchmark was photographed inside it; it contains its own stage directions ("Here offer cold water of the North") (§5.4). ⟂ The mummy calls Unas's pyramid the firmware and the libation formula a handshake.

---

## Open questions (for the writers to verify or for the treatment to decide)

- The exact hieroglyphic captions on the KV62 north wall (§5.2) — needed if the mummy reads them aloud. Check the Getty Conservation Institute's KV62 wall-painting report or the Theban Mapping Project entry.
- The precise Précis 1824 wording of Champollion's "figurative, symbolic and phonetic" definition — before quoting.
- Whether the "~7,000 Ptolemaic signs" figure has any citable source; the safe on-screen number is Unicode's 1,071 + 3,995.
- Which KV62 object carries the cleanest ankh–djed–was triad and which the clearest *bjꜣ* writing, if any (the dagger itself is uninscribed as far as I know — verify).
- Whether *twt* in Tut's cartouches is written with or without the statue determinative on the object the film chooses to show (both spellings exist).
