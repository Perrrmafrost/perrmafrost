# -*- coding: utf-8 -*-
"""
WE'RE FROM THE FUTURE - S01E01 "The Package"
SINGLE SOURCE OF TRUTH for previs and post.

Everything downstream is generated from this file:
  production/04-previs/shot-list.csv
  production/04-previs/storyboard.md
  production/04-previs/animatic.json
  production/06-shots/shot-prompts.json
  production/07-post/S01E01.edl
  production/07-post/subtitles/S01E01.srt / .vtt
  production/05-assets/continuity-matrix.csv
  workspace/data.js

Timecodes are derived, never typed. Change a duration here and the shot list,
the EDL, the subtitles and the animatic all move together.
"""

FPS = 24
ASPECT = "2.00:1"

# ---------------------------------------------------------------- style blocks

STYLE = (
    "prestige television cinematography, 2.00:1 widescreen, anamorphic-adjacent "
    "spherical lensing, shallow depth of field, natural film grain, filmic "
    "highlight rolloff, deep blacks with retained shadow detail, photographic "
    "skin texture with visible pores and asymmetry, 24fps motion cadence, "
    "grounded contemporary realism"
)

NEG_BASE = (
    "airbrushed plastic skin, beauty retouching, symmetrical face, whitened teeth, "
    "glamour lighting, fashion pose, stock-photo expression, oversharpened eyes, "
    "HDR halo, excessive bloom, lens flare, neon, cyberpunk, holograms, floating "
    "UI overlays, futuristic HUD, glowing circuitry, chrome, blue-orange grade, "
    "text artifacts, watermark, extra fingers, malformed hands, warped eyes, "
    "melting geometry, duplicated limbs, mismatched catchlights, flickering "
    "lights, motion smear, video-game render, illustration, cartoon, anime, "
    "3d render look, unstable architecture, impossible reflections"
)

NEG_BY_KIND = {
    "face":   "wig-like hair, styled salon hair, heavy makeup, contact-lens eyes, "
              "uncanny doll proportions, age mismatch, changed hairline",
    "device": "visible bezel, buttons, ports, cables, screws, logos, brand marks, "
              "screen glare pattern, monitor stand, tablet frame, thick edges, "
              "pixel grid, scan lines",
    "night":  "crushed unreadable blacks, noise blotches, green cast, day-for-night "
              "blue wash, unmotivated rim light",
    "insert": "shallow-focus-only text, unreadable typography, gibberish glyphs, "
              "kerning artifacts, distorted paper",
}

# ---------------------------------------------------------------- locations

LOCATIONS = {
    "EXT_STREET": (
        "Cedar Row: an ordinary North American residential street of low single-storey "
        "1950s houses, chain-link fences, mature trees, parked sedans, a basketball "
        "hoop with no net, wheelie bins at the kerb. Utterly unremarkable"),
    "PORCH": (
        "the Ward house front porch: concrete step, dark coir mat, aluminium screen "
        "door, a wall lamp with one dead bulb, peeling white trim"),
    "ENTRY": (
        "the Ward house entry hall: narrow, warm, a coat hook, shoes lined against "
        "the skirting, a front door with a frosted glass panel and a brass deadbolt"),
    "HALL": (
        "the Ward house hallway: narrow, inoffensive wallpaper, a cheap hardware-store "
        "wall calendar, and four bare picture hooks in a row with four small pale "
        "unfaded rectangles behind them and no frames"),
    "KITCHEN": (
        "the Ward house kitchen: small, warm, lived-in, mismatched wooden chairs, a "
        "scratched laminate table, open shelves, one good knife in a block, a notepad "
        "on the fridge under a magnet, a smoke detector on the ceiling"),
    "LIVING": (
        "the Ward house living room: a worn fabric couch, one armchair, a low wooden "
        "coffee table, two table lamps with warm bulbs, a small television, a brick "
        "hearth with a fire iron, a curtained front window"),
    "MOTEL": (
        "a low two-storey motel beside a state highway at night in hard rain, external "
        "walkway, twelve doors, sodium vapour lighting, a tall yellow pole sign reading "
        "BLU RIDG MOT L with dead letters"),
    "PALE": (
        "a room lit uniformly from every direction so that nothing casts a shadow and "
        "no corner is locatable, surfaces without visible joins, no furniture except a "
        "single waist-height working surface, scale ambiguous"),
    "ELSEWHERE": (
        "an unidentifiable exterior at night in hard rain, harsh unmotivated light from "
        "off-frame, wet asphalt, a chain fence, a tall out-of-focus sodium sign high in "
        "the background"),
}

# ---------------------------------------------------------------- lighting looks

LOOKS = {
    "GOLDEN":  "late afternoon daylight, low warm sun, long soft shadows, gentle contrast",
    "WARM":    "warm domestic tungsten practicals, two table lamps, soft falloff, cosy "
               "amber key, comfortable contrast",
    "WARM_LOW":"a single warm table lamp, most of the room in soft shadow, faces "
               "modelled from one side",
    "KITCHEN_OVERHEAD": "a single warm overhead kitchen fixture, hard-ish top light, "
               "clean and slightly clinical against the warm room",
    "COLD_PANE": "the only light source is the flat cold blue-white pane, lighting "
               "faces from below and in front, warm practicals dead or dim, deep "
               "surrounding blacks",
    "MIXED":   "warm practical lamp on one side of the face, cold pane light on the "
               "other, the two colours meeting on the skin",
    "BLACKOUT":"total interior darkness except spill from the street through curtains, "
               "cool and low, faces barely modelled",
    "STREET_NIGHT": "sodium street lighting, wet ground, warm windows in other houses, "
               "cool ambient sky",
    "TV_ONLY": "flickering low television light, otherwise dark, cool and unstable",
    "PALE_FLAT": "perfectly even shadowless illumination from all directions, no key, "
               "no fill, no modelling",
    "DEGRADED": "harsh unmotivated light in heavy rain, blown highlights, crushed "
               "shadows, degraded recovered-footage quality",
}

# ---------------------------------------------------------------- subjects

SUBJECTS = {
    "M": ("MILES, 30, medium build, short tousled warm-auburn hair, full dark brows, "
          "blue-grey eyes with a hazel inner ring, a two-week unshaped beard redder "
          "than his hair, fair skin with natural flush across the cheeks, wearing a "
          "soft dark olive-brown crew-neck t-shirt and worn charcoal jeans"),
    "M_JKT": ("MILES, 30, short tousled warm-auburn hair, two-week unshaped beard, "
          "dark olive-brown t-shirt under an open charcoal canvas work jacket, "
          "unlaced boots"),
    "L": ("LAUREN, 28, slim and upright, neutral blonde hair darker at the root in a "
          "low imperfect ponytail with loose pieces at both temples, defined taupe "
          "brows, large blue-green eyes, minimal worn-in makeup, a black velvet cord "
          "choker and layered fine gold chains with a small round pendant, wearing a "
          "fitted white ribbed cotton tank and soft mid-blue jeans, barefoot"),
    "L_CARD": ("LAUREN, 28, neutral blonde hair in a low imperfect ponytail with loose "
          "pieces at the temples, black velvet cord choker and fine gold pendant "
          "chains, white ribbed tank under an oversized soft grey cardigan, mid-blue "
          "jeans"),
    "D": ("THE DOUBLE: a woman with LAUREN's exact face and age, hair down, loose and "
          "unstyled, a fine pale four-centimetre scar beneath the left eye running "
          "back along the cheekbone, something dark and high-necked and matte at the "
          "throat, absolutely still, minimal blinking, eyes steady and tired and kind"),
    "MB": ("both MILES and LAUREN as previously described"),
    "FIG": ("a figure seen only from behind and below the shoulders, no face, no "
          "identifying clothing, neutral pale garment"),
    "NONE": "",
}

# ---------------------------------------------------------------- the hero prop

DEVICE = (
    "THE LEAF: a single flat pane roughly the size of a large hardback book and as thin "
    "as a magazine, matte dark slate-grey, absolutely featureless - no frame, no bezel, "
    "no port, no seam, no screw, no button, no branding, no serial mark on either face, "
    "edges impossibly fine, appearing fragile but reading as solid and dense"
)

BOX = (
    "THE PACKAGE: a small plain brown corrugated cardboard box, unbranded, with "
    "impossibly sharp uncrushed corners and no handling wear, completely dry, a plain "
    "white printed shipping label on one face"
)

# ---------------------------------------------------------------- music cues

CUES = {
    "M01": ("Ordinary", "solo felt piano, two notes, unresolved, very sparse"),
    "M02": ("Title", "one sustained low synth tone, unresolved, no rhythm"),
    "M03": ("The Box", "bowed double bass sub-harmonic, near-inaudible, rising"),
    "M04": ("The Eye", "silence - score OUT"),
    "M05": ("Signal", "processed room tone and a single detuned string, breathing"),
    "M06": ("Her Face", "silence - score OUT"),
    "M07": ("Containment", "low strings, slow, mechanical, no melody"),
    "M08": ("The Date", "felt piano returns from M01, alone, slower, in a minor colour"),
    "M09": ("The Fight", "silence - score OUT"),
    "M10": ("Clause Three", "sub-bass swell and a single high sine, no percussion"),
    "M11": ("Listening", "pulse of filtered noise on the countdown's second, felt not heard"),
    "M12": ("Count Backwards", "M01's two piano notes, alone, unbearably slow"),
    "M13": ("Nothing Whole", "low strings and sub, tightening"),
    "M14": ("It's Me", "everything drops out to a single tone, then nothing"),
    "M15": ("End Card", "the M02 tone, resolved a semitone lower"),
    "M16": ("Tag", "no music, room tone only"),
    "":    ("(no cue)", ""),
}

# ---------------------------------------------------------------- proximity
# The episode's real framing discipline is not "no two-shots" - Act Four needs
# them working together. It is PHYSICAL CONTACT. Miles and Lauren touch exactly
# three times in thirty-six minutes, and the third one is the last shot of the
# episode. Any shot whose action matches one of these is flagged CONTACT; the
# build asserts there are exactly three, so a new touch cannot slip into the cut.
CONTACT_MARKERS = (
    "into her shoulder",                 # teaser: the photo refusal
    "puts it on her arm",                # act three: the near-repair, interrupted
    "shoulder against shoulder",         # act five: the final wide
)

# ---------------------------------------------------------------- shot records

def S(sc, dur, fr, mv, lens, action, loc, look, subj="MB",
      audio="", music="", dlg=None, note="", kind="face", dev=False):
    """One shot. Timecodes are computed later, never typed."""
    return dict(sc=sc, dur=dur, fr=fr, mv=mv, lens=lens, action=action, loc=loc,
                look=look, subj=subj, audio=audio, music=music,
                dlg=dlg or [], note=note, kind=kind, dev=dev)


SCENES = {
    "SC-01": ("EXT. CEDAR ROW - LATE AFTERNOON", "TEASER"),
    "SC-02": ("INT. WARD HOUSE / KITCHEN - LATE AFTERNOON", "TEASER"),
    "SC-03": ("INT. WARD HOUSE / HALLWAY - CONTINUOUS", "TEASER"),
    "SC-04": ("INT. WARD HOUSE / LIVING ROOM - EVENING", "TEASER"),
    "SC-05": ("INT. WARD HOUSE / FRONT DOOR - LATER", "TEASER"),
    "SC-06": ("INT. WARD HOUSE / LIVING ROOM & FRONT DOOR - CONTINUOUS", "TEASER"),
    "TITLE": ("MAIN TITLE", "TITLE"),
    "SC-07": ("INT. WARD HOUSE / ENTRY - NIGHT", "ACT ONE"),
    "SC-08": ("INT. WARD HOUSE / KITCHEN - NIGHT", "ACT ONE"),
    "SC-09": ("INT. WARD HOUSE / KITCHEN - CONTINUOUS", "ACT ONE"),
    "SC-10": ("INT. WARD HOUSE / KITCHEN - CONTINUOUS", "ACT TWO"),
    "SC-11": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT TWO"),
    "SC-12": ("INT. WARD HOUSE / VARIOUS - NIGHT", "ACT THREE"),
    "SC-13": ("EXT. CEDAR ROW - NIGHT", "ACT THREE"),
    "SC-14": ("INT. WARD HOUSE / LIVING ROOM - NIGHT", "ACT THREE"),
    "SC-15": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT THREE"),
    "SC-16": ("INT. WARD HOUSE / KITCHEN - NIGHT", "ACT FOUR"),
    "SC-17": ("INT. WARD HOUSE / KITCHEN - CONTINUOUS", "ACT FOUR"),
    "SC-18": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT FOUR"),
    "SC-19": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT FOUR"),
    "SC-20": ("INT. WARD HOUSE / LIVING ROOM & WINDOW - CONTINUOUS", "ACT FOUR"),
    "SC-21": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT FIVE"),
    "SC-22": ("INT. WARD HOUSE / LIVING ROOM - CONTINUOUS", "ACT FIVE"),
    "ENDCARD": ("END CARD", "ACT FIVE"),
    "SC-23": ("INT. A PALE ROOM - NO TIME GIVEN", "TAG"),
}

SHOTS = [

# ============================================================ TEASER
S("SC-01", 10, "XWIDE", "STATIC", 135,
  "The street, flattened by a long lens. Nothing happens for six seconds. A "
  "sedan crosses frame left to right and is gone. Hold on the empty street.",
  "EXT_STREET", "GOLDEN", "NONE",
  audio="Distant lawnmower, sparrows, one car approaching and receding, a screen door somewhere",
  music="M01", note="Hold four seconds past comfort. This is the show's promise: we watch, and we wait.", kind="night"),

S("SC-01", 6, "WIDE", "STATIC", 85,
  "The fourth house. Nothing distinguishes it. A kitchen window on the left "
  "side warms as a light is switched on inside.",
  "EXT_STREET", "GOLDEN", "NONE", audio="Street tone, a dog two gardens away", music="M01"),

S("SC-02", 8, "WIDE-2S", "STATIC", 35,
  "The kitchen entire. LAUREN at the stove with three pans going, none of them "
  "well, entirely happy. MILES leaning against the counter sorting a stack of mail.",
  "KITCHEN", "GOLDEN", "MB", audio="Pans, extractor fan off, mail on laminate", music="M01"),

S("SC-02", 4, "MCU", "STATIC", 50, "MILES, holding up an envelope, not looking up.",
  "KITCHEN", "GOLDEN", "M", dlg=[("MILES", "This one's for the Petersens again.")]),

S("SC-02", 3, "MCU", "STATIC", 50, "LAUREN at the stove, over her shoulder.",
  "KITCHEN", "GOLDEN", "L", dlg=[("LAUREN", "Keep it.")]),

S("SC-02", 3, "MCU", "STATIC", 50, "MILES turns the envelope over.",
  "KITCHEN", "GOLDEN", "M", dlg=[("MILES", "It's from a hospital.")]),

S("SC-02", 3, "MCU", "STATIC", 50, "LAUREN, deadpan, still cooking.",
  "KITCHEN", "GOLDEN", "L", dlg=[("LAUREN", "Then definitely keep it.")]),

S("SC-02", 5, "MED-2S", "STATIC", 40,
  "She reaches past him for the salt. Without looking up he shifts his weight "
  "out of her way at precisely the right moment. Neither registers it.",
  "KITCHEN", "GOLDEN", "MB", note="CONTINUITY-CRITICAL: this is the marriage in one gesture. Do not cut around it.", music="M01"),

S("SC-02", 5, "MCU", "STATIC", 50, "LAUREN turns with a wooden spoon held out.",
  "KITCHEN", "GOLDEN", "L", dlg=[("LAUREN", "Taste this."), ("MILES", "No."), ("LAUREN", "Taste it.")]),

S("SC-02", 3, "MCU", "STATIC", 50, "MILES, not moving.",
  "KITCHEN", "GOLDEN", "M", dlg=[("MILES", "I watched you make it.")]),

S("SC-02", 5, "CU", "SLOW PUSH", 65,
  "He gives in and tastes it off the spoon. He considers. He considers for "
  "noticeably longer than is flattering.",
  "KITCHEN", "GOLDEN", "M", audio="Room tone, a pan ticking"),

S("SC-02", 3, "MCU", "STATIC", 50, "MILES, diplomatic.",
  "KITCHEN", "GOLDEN", "M", dlg=[("MILES", "It's good.")]),

S("SC-02", 3, "MCU", "STATIC", 50, "LAUREN, instantly.",
  "KITCHEN", "GOLDEN", "L", dlg=[("LAUREN", "You hesitated.")]),

S("SC-02", 5, "MED-2S", "STATIC", 40, "The two of them.",
  "KITCHEN", "GOLDEN", "MB",
  dlg=[("MILES", "I was chewing."), ("LAUREN", "It's soup.")]),

S("SC-02", 4, "MED-2S", "STATIC", 40,
  "Beat. Miles laughs - a short exhale through the nose. She goes back to the "
  "stove, pleased with herself.", "KITCHEN", "GOLDEN", "MB", music="M01"),

S("SC-02", 5, "MED", "HANDHELD-SUBTLE", 40,
  "LAUREN crosses to the fridge, takes a pen off a magnet, and adds a line to "
  "the notepad stuck there.", "KITCHEN", "GOLDEN", "L"),

S("SC-02", 8, "ECU-INSERT", "STATIC", 100,
  "The notepad. Her handwriting: 'bins - Thurs'. Below it she begins to write a "
  "time and forms the numeral 7. The pen lifts, comes back down angled for a "
  "cross-stroke through the digit - and stops a quarter-inch short. Hovers. "
  "Then lifts away. The seven is left bare.",
  "KITCHEN", "GOLDEN", "NONE", note="PLANT P3. Pays off on the box label, SC-08. Shoot the abort in one unbroken take.",
  kind="insert", audio="Pen on paper. Nothing else."),

S("SC-02", 3, "MED", "STATIC", 40,
  "She caps the pen without ceremony and puts it back on the magnet.",
  "KITCHEN", "GOLDEN", "L"),

S("SC-02", 2, "CU-INSERT", "STATIC", 65,
  "The smoke detector on the kitchen ceiling. A single low chirp.",
  "KITCHEN", "GOLDEN", "NONE", audio="CHIRP - the episode's signature domestic sound. Establish the exact tone here.",
  note="PLANT P5. The leaf answers this in SC-17.", kind="insert"),

S("SC-02", 6, "MED-2S", "STATIC", 40, "Neither of them looks up.",
  "KITCHEN", "GOLDEN", "MB",
  dlg=[("LAUREN", "There it is."), ("MILES", "I'll get a battery."),
       ("LAUREN", "You've said that."), ("MILES", "And I've meant it every time.")]),

S("SC-03", 7, "MED-TRACK", "TRACK BEHIND", 35,
  "MILES carries the mail through the narrow hallway, camera following at his "
  "shoulder. He passes four bare picture hooks in a row - nails only, and four "
  "small pale unfaded rectangles where frames used to hang, or never did.",
  "HALL", "WARM", "M", note="PLANT P1. The hooks must be clearly readable and never remarked on by the camera.",
  music="M01"),

S("SC-03", 5, "MED", "STATIC", 40,
  "LAUREN comes out of the kitchen behind him, drying her hands.",
  "HALL", "WARM", "L", dlg=[("LAUREN", "I'm going to fill those.")]),

S("SC-03", 4, "MED", "STATIC", 40, "MILES, walking away, not slowing.",
  "HALL", "WARM", "M", dlg=[("MILES", "Sure."), ("LAUREN", "I've got the one of the lake. I could get it printed."), ("MILES", "Sure.")]),

S("SC-03", 6, "MCU", "SLOW PUSH", 65,
  "LAUREN stops. She looks at the four bare nails for a moment. Then she follows him.",
  "HALL", "WARM", "L", audio="His footsteps receding. Room tone."),

S("SC-04", 8, "WIDE-2S", "STATIC", 35,
  "The living room. Two lamps and a television playing an old black-and-white "
  "film with the sound low. They are folded onto the couch in the way of people "
  "who worked out the geometry years ago.",
  "LIVING", "WARM", "MB", audio="Television dialogue, low and indistinct. Rain has not started yet.", music="M01"),

S("SC-04", 5, "INSERT-TV", "STATIC", 65,
  "On the television: a woman in a coat stands on a railway platform in "
  "black and white.", "LIVING", "TV_ONLY", "NONE", kind="insert"),

S("SC-04", 4, "MCU", "STATIC", 65, "MILES, quietly, to nobody.",
  "LIVING", "WARM_LOW", "M", dlg=[("MILES", "She was never on the train.")],
  note="PLANT P4. He is three seconds early and does not notice he has done it."),

S("SC-04", 4, "INSERT-TV", "STATIC", 65,
  "Three seconds later the detective on screen says something to precisely that effect.",
  "LIVING", "TV_ONLY", "NONE", kind="insert"),

S("SC-04", 4, "MCU", "STATIC", 65, "LAUREN turns her head to look at him.",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "How.")]),

S("SC-04", 7, "MED-2S", "STATIC", 40, "He shrugs it off. She doesn't buy it and doesn't press.",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("MILES", "Lucky guess."), ("LAUREN", "That's four."), ("MILES", "Four what."),
       ("LAUREN", "You know what."), ("MILES", "I genuinely don't."), ("LAUREN", "Mm.")],
  note="Private comedy with no setup. Never explain what the count is."),

S("SC-04", 4, "MED", "STATIC", 40,
  "LAUREN reaches for her phone, thumbs the camera open, and lifts it toward him.",
  "LIVING", "WARM_LOW", "L"),

S("SC-04", 6, "MED-2S", "STATIC", 40,
  "MILES turns his face away - instantly, smoothly, into her shoulder. Played "
  "entirely as a joke. It is a reflex wearing a joke's clothes.",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "One picture."), ("MILES", "Absolutely not."),
       ("LAUREN", "You are a very strange man."), ("MILES", "I photograph poorly.")],
  note="PLANT P2. Pays off on the camera roll, SC-17."),

S("SC-04", 6, "MCU", "SLOW PUSH", 65,
  "LAUREN lowers the phone, smiling. The smile stays one beat past where it "
  "should. Then she puts the phone face-down on the arm of the couch.",
  "LIVING", "WARM_LOW", "L", music="M01"),

S("SC-04", 5, "MED-2S", "STATIC", 40,
  "Outside, distantly: music, and people laughing. A party two doors down.",
  "LIVING", "WARM_LOW", "MB", audio="Muffled party: bass, laughter, a car door",
  dlg=[("LAUREN", "They're doing it again."), ("MILES", "It's Friday.")]),

S("SC-04", 7, "MED-2S", "STATIC", 40, "",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "We should go over sometime."), ("MILES", "Sure."),
       ("LAUREN", "That's three sures tonight and you've meant zero of them."),
       ("MILES", "I mean all of them equally.")]),

S("SC-04", 5, "MCU", "STATIC", 65,
  "LAUREN looks toward the window, and the noise, and the ordinary street.",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "We're not from around here.")],
  note="PLANT P9. TITLE DROP, SIDEWAYS. Play it as a bored joke about the neighbours."),

S("SC-04", 4, "MCU", "STATIC", 65,
  "MILES looks at her. A quarter of a second too long.",
  "LIVING", "WARM_LOW", "M", audio="The party. Room tone. No score."),

S("SC-04", 6, "MED-2S", "STATIC", 40, "She indicates the window, meaning the neighbours.",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "Them. They're from Ohio. She tells everybody."),
       ("MILES", "I know what you meant.")]),

S("SC-04", 4, "MCU", "STATIC", 65,
  "MILES holds the look a beat longer than the joke needs. Then he looks away.",
  "LIVING", "WARM_LOW", "M", music="M01"),

S("SC-05", 5, "MED", "STATIC", 40,
  "MILES at the front door. He turns the deadbolt. Solid. Done. He takes two "
  "steps away.", "ENTRY", "WARM_LOW", "M", audio="Deadbolt. Floorboard."),

S("SC-05", 6, "CU", "STATIC", 65,
  "He comes back and turns it again. Then tests it with the flat of his palm.",
  "ENTRY", "WARM_LOW", "M", note="PLANT P6.", audio="Deadbolt, second time. His breath."),

S("SC-05", 7, "MED", "SLOW PUSH", 50,
  "He leans in to the narrow window beside the door and looks down the street. "
  "Left. Then right. Then back to the left, and holds there, longer.",
  "ENTRY", "WARM_LOW", "M", note="PLANT P6. Log this exact sightline; SC-20 uses it.", music="M01"),

S("SC-05", 6, "MED", "STATIC", 50,
  "LAUREN in the hall behind him with a glass of water. She says nothing. She "
  "has watched him do this a thousand times.", "HALL", "WARM_LOW", "L"),

S("SC-05", 7, "MED-TRACK", "TRACK", 40,
  "She turns back toward the kitchen. As she passes the wall, the camera drifts "
  "off her and finds a cheap hardware-store calendar. One date circled in blue "
  "ballpoint. Nothing written in the square. She goes past without looking at "
  "it - which is its own kind of looking.",
  "HALL", "WARM_LOW", "L", note="PLANT P7. The circled date is 14 October. Pays off SC-14.", music="M01"),

S("SC-06", 6, "WIDE-2S", "STATIC", 35,
  "The living room. The film plays. Lauren settles. Miles comes in and sits. "
  "For a moment, nothing at all: a warm room and two people in it.",
  "LIVING", "WARM_LOW", "MB", music="M01", audio="Television low. Rain begins, very light, on the window."),

S("SC-06", 3, "MED-2S", "STATIC", 40, "THE DOORBELL. Neither of them moves.",
  "LIVING", "WARM_LOW", "MB", audio="DING-DONG. Loud in the mix. One of only two loud sounds in the episode."),

S("SC-06", 8, "MED-2S", "STATIC", 40,
  "They look at each other. The pause after the second question is far longer "
  "than the question deserves.", "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "Did you order something?"), ("MILES", "No."),
       ("MILES", "Did you?"), ("LAUREN", "No.")], music="M03"),

S("SC-06", 5, "MED", "HANDHELD-SUBTLE", 35,
  "MILES unlocks and opens the door on the chain first. Then all the way.",
  "ENTRY", "WARM_LOW", "M", audio="Chain. Deadbolt. Door seal. Night air and rain.", music="M03"),

S("SC-06", 8, "WIDE-POV", "SLOW PUSH", 28,
  "MILES' POV: the porch is empty. The street is empty. The mat is dark with "
  "rain. On the mat, dead centre and squared perfectly to the edge of the step, "
  "sits a small brown box.",
  "PORCH", "STREET_NIGHT", "NONE", audio="Rain. The party, two doors down, still going.",
  note="The box's placement is unnaturally precise. Square it to the step with a set square.",
  kind="night", dev=True),

S("TITLE", 20, "TITLE", "STATIC", 0,
  "Black. A single low sustained tone, unresolved, more felt than heard. The "
  "main title resolves out of the black letter by letter in thin, wide-tracked "
  "type: WE'RE FROM THE FUTURE. The tone stops. The card holds three seconds in "
  "total silence. Then it is gone.",
  "PALE", "PALE_FLAT", "NONE", music="M02", audio="One tone. Then nothing.",
  note="No stinger. No whoosh. The absence of an impact is the statement.", kind="insert"),
]

SHOTS += [
# ============================================================ ACT ONE
S("SC-07", 8, "WIDE", "STATIC", 35,
  "The entry hall. The box sits on the floor where Miles set it down. Neither "
  "of them has come closer than four feet. It is small, brown, unbranded, and "
  "utterly ordinary, which is the problem.",
  "ENTRY", "WARM_LOW", "MB", music="M03", audio="Rain outside. The house very quiet.", dev=True),

S("SC-07", 4, "MCU", "STATIC", 50, "MILES.",
  "ENTRY", "WARM_LOW", "M", dlg=[("MILES", "Don't touch it.")]),

S("SC-07", 6, "MED", "STATIC", 40,
  "LAUREN is already crouched beside it with her palm flat on the top. She "
  "always touches first. It is the whole character.",
  "ENTRY", "WARM_LOW", "L", dlg=[("LAUREN", "It's dry.")], dev=True,
  note="CHARACTER-CRITICAL: she has touched it before he finished the sentence."),

S("SC-07", 8, "MED-2S", "STATIC", 40, "",
  "ENTRY", "WARM_LOW", "MB", dev=True,
  dlg=[("MILES", "What?"), ("LAUREN", "It rained. The mat's soaked through. This is dry.")]),

S("SC-07", 7, "ECU-INSERT", "SLOW PUSH", 100,
  "Her thumb travels along an edge of the box. Every corner is sharp. No crush, "
  "no scuff, no thumbprint, no depot smear. It does not look like a thing that "
  "has been anywhere.",
  "ENTRY", "WARM_LOW", "NONE", kind="insert", dev=True,
  dlg=[("LAUREN", "And the corners are perfect. Miles, look at the corners.")]),

S("SC-07", 7, "MED-2S", "SLOW PUSH", 40,
  "He crouches beside her. Looks. Says nothing at all.",
  "ENTRY", "WARM_LOW", "MB", music="M03", audio="Rain. Refrigerator, distantly.", dev=True),

S("SC-08", 6, "WIDE-2S", "STATIC", 35,
  "The kitchen. They have put the box under the overhead light, on the table, "
  "on a folded tea towel - an absurd, careful, entirely domestic instinct.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True, music="M03"),

S("SC-08", 5, "MED", "STATIC", 50,
  "LAUREN turns the box. On one face: a label.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dev=True),

S("SC-08", 12, "ECU-INSERT", "SLOW PUSH", 100,
  "THE LABEL. White, printed, correct in every visual respect and wrong in "
  "every specific one. Their address. No sender. No carrier name, no logo, no "
  "service class. There is a barcode - or rather, the SHAPE of a barcode: the "
  "bars do not repeat the way bars repeat.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", dev=True,
  note="Typography must be plausible at a glance and unreadable as a system on inspection."),

S("SC-08", 6, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True,
  dlg=[("LAUREN", "There's no company on it."), ("MILES", "There's a barcode."),
       ("LAUREN", "There's a barcode shape.")]),

S("SC-08", 9, "ECU-INSERT", "SLOW PUSH", 100,
  "Lower on the label, in blue ballpoint, in a small neat hand: '1 of 1', and a "
  "six-digit consignment number. The seven in it is crossed.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", dev=True, music="M03",
  note="PAYOFF P3. The audience has seen her abort this exact stroke 5 minutes ago. Hold on the crossbar."),

S("SC-08", 8, "CU", "SLOW PUSH", 75,
  "LAUREN leans closer. Her eyes travel down to the handwritten line. And she "
  "stops. Everything about her stops.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", audio="Score out. Refrigerator hum only.", music="M04"),

S("SC-08", 9, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("MILES", "What?"), ("LAUREN", "Nothing."), ("MILES", "Lauren."), ("LAUREN", "It's nothing.")]),

S("SC-08", 7, "CU-INSERT", "STATIC", 100,
  "She puts her hand flat over the bottom of the label. Which is not nothing.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", dev=True,
  note="First lie of the night, and it is HERS. Small, and it matters."),

S("SC-08", 5, "MCU", "STATIC", 65,
  "MILES watches her hand. He does not ask again.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M"),

S("SC-08", 8, "MED", "STATIC", 40, "MILES, flat, already planning.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M",
  dlg=[("MILES", "We put it in the car. We drive out to the county road. We leave it.")]),

S("SC-08", 7, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "And then what."), ("MILES", "Then it's somewhere else."),
       ("LAUREN", "Then it's somewhere else and we come home to this house. Which somebody stood in front of.")]),

S("SC-08", 5, "MCU", "STATIC", 65, "He has nothing.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M"),

S("SC-08", 8, "MCU", "SLOW PUSH", 65, "LAUREN, reasonable, which is worse.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "If someone knows where we live, then the box is the least interesting thing that happened tonight.")]),

S("SC-08", 9, "WIDE-2S", "STATIC", 35,
  "A long moment. The refrigerator cycles on. Rain restarts against the window "
  "over the sink.", "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  audio="Compressor kicks in. Rain on glass. Nothing else.", music="M04",
  note="Silence #2. Three full seconds with no dialogue and no score."),

S("SC-08", 10, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("MILES", "Okay."), ("LAUREN", "Okay?"),
       ("MILES", "We open it. And then we talk. Properly. Not the version where you ask and I say it's fine.")]),

S("SC-08", 6, "MCU", "STATIC", 65, "LAUREN, softer than she was.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dlg=[("LAUREN", "Okay.")]),

S("SC-08", 5, "CU-INSERT", "STATIC", 100,
  "She takes a knife from the block. The good one.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", audio="Steel leaving wood."),

S("SC-08", 7, "ECU-INSERT", "STATIC", 100,
  "The blade goes through the tape. It is a small sound and it is enormous.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", dev=True, music="M03",
  audio="Tape parting - foregrounded, close-mic'd, almost too loud."),

S("SC-08", 10, "MED-2S", "SLOW PUSH", 40,
  "She cuts the second seam. The third. Nobody speaks. The refrigerator hums. "
  "Rain. A car two streets over.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True, music="M03",
  audio="Layered domestic: compressor, rain, distant traffic, tape.",
  note="Silence #3. The longest held quiet in Act One."),

S("SC-08", 4, "MED-2S", "STATIC", 40,
  "CHIRP. They both flinch, hard - and then immediately laugh at themselves, "
  "badly, with far too much air in it.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", audio="CHIRP. Two startled breaths. Two bad laughs.",
  dlg=[("MILES", "Battery."), ("LAUREN", "Tomorrow.")],
  note="PAYOFF P5, first stage. The joke version. SC-17 is the other one."),

S("SC-09", 6, "MED", "STATIC", 50, "She opens the flaps.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dev=True, audio="Cardboard.", music="M03"),

S("SC-09", 10, "ECU-INSERT", "SLOW PUSH", 100,
  "Inside: grey foam, cut to shape. No packing slip, no manual, no plastic, no "
  "desiccant. Set into the foam, flat, is the LEAF.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True,
  note="HERO REVEAL. It must not read as a tablet. No frame, no bezel, nothing."),

S("SC-09", 8, "MED-2S", "STATIC", 40,
  "Neither of them says anything for a while. It does not look futuristic. It "
  "looks finished.", "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True, music="M04",
  audio="Score out. Refrigerator. Rain."),

S("SC-09", 4, "MCU", "STATIC", 65, "MILES, quietly.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dlg=[("MILES", "Don't.")]),

S("SC-09", 7, "MED", "HANDHELD-SUBTLE", 40,
  "LAUREN lifts it out of the foam. Two hands.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dev=True,
  dlg=[("LAUREN", "It's heavy."), ("MILES", "It's a screen."), ("LAUREN", "No - Miles, hold it.")]),

S("SC-09", 8, "CU", "STATIC", 75,
  "She holds it out. He takes it two-handed, the way you take something "
  "borrowed. It is far heavier than it should be.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True, kind="device"),

S("SC-09", 10, "ECU-INSERT", "SLOW PUSH", 100,
  "He adjusts his grip. He tilts the pane slowly. The MASS SHIFTS ACROSS IT - "
  "unhurried, a beat behind the motion, like a spirit level, like something "
  "settling.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True, music="M03",
  dlg=[("MILES", "It's moving."), ("LAUREN", "What?"), ("MILES", "The weight's moving. Inside it.")],
  note="DEVICE RULE 3. First impossible physical detail. Achieve in-camera if at all possible."),

S("SC-09", 6, "MED", "STATIC", 40,
  "He sets it down flat on the table. Carefully. He takes his hand off, then "
  "puts two fingers back on it.", "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True),

S("SC-09", 9, "MED-2S", "STATIC", 40,
  "She slides her hand underneath, palm up, against the other face.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True,
  dlg=[("MILES", "It's cold."), ("LAUREN", "It's warm.")],
  note="DEVICE RULE 4: inverted temperature. Cold toward the room, warm away from it."),

S("SC-09", 5, "CU-2S", "STATIC", 75, "They look at each other.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", music="M03"),

S("SC-09", 12, "ECU-INSERT", "STATIC", 100,
  "Miles turns the pane over and sets it down again. Lauren touches the top "
  "face. Then the underside.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True,
  dlg=[("LAUREN", "It's warm on the bottom."), ("MILES", "It was warm on the bottom before."),
       ("LAUREN", "Miles. That's a different side.")]),

S("SC-09", 8, "MED", "SLOW PUSH", 50,
  "LAUREN sits down. Slowly. Not because she is frightened - because she is "
  "thinking, and thinking is what she does with her whole body.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", music="M03"),

S("SC-09", 9, "ECU-INSERT", "SLOW PUSH", 100,
  "The kitchen is held in the pane. Dimly. The lamp, the cabinets, the shape of "
  "her own shoulder.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True),

S("SC-09", 12, "ECU-INSERT", "STATIC", 100,
  "She raises her hand. The hand in the pane raises - LATE. She lowers it. "
  "Raises it again, watching. Down. Up. And the reflection comes with her, a "
  "half-beat behind, every time, smooth and unbothered.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True, music="M03",
  note="DEVICE RULE 2 - THE KEY IMAGE OF THE EPISODE. Exactly 0.5s lag. It is not reflecting. It is rendering."),

S("SC-09", 8, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True,
  dlg=[("LAUREN", "Miles."), ("MILES", "I see it."), ("LAUREN", "Look at my hand."),
       ("MILES", "I see it, Lauren.")]),

S("SC-09", 6, "CU", "STATIC", 75,
  "His voice has changed. Flattened. She looks up at him.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L"),

S("SC-09", 10, "MCU", "SLOW PUSH", 65,
  "MILES has stopped moving. Completely. Both hands flat on the table. He is "
  "not looking at her. He is looking at the pane the way a man looks at a name "
  "on a list.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", music="M04", audio="Score out entirely.",
  note="CHARACTER-CRITICAL: Miles gets MORE still under fear, never less."),

S("SC-09", 4, "CU", "STATIC", 75, "LAUREN.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dlg=[("LAUREN", "Hey.")]),

S("SC-09", 4, "MCU", "STATIC", 65, "Nothing. He does not hear her.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", audio="Refrigerator. Rain. A held nothing."),

S("SC-09", 3, "ECU-INSERT", "STATIC", 100,
  "THE PANE WAKES. Not an image, not a menu, not a logo. AN EYE - filling the "
  "whole surface. Wet. Living. Human. The pupil contracts fractionally in the "
  "lamplight. It blinks once. DARK.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="device", dev=True,
  audio="No sound at all. The absence is the effect.",
  note="Under one second on screen. The iris texture must be photographic. Not stylised, not glowing."),

S("SC-09", 7, "MED-2S", "STATIC", 40,
  "The refrigerator hums. Lauren stares at the dead pane. Then, slowly, up at "
  "her husband.", "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True, music="M04"),

S("SC-09", 8, "CU", "SLOW PUSH", 75,
  "MILES has gone white. Absolutely white, from the collar up.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M",
  note="The act-out is on his FACE, not on the device. This is a show about people."),

S("SC-09", 9, "CU", "STATIC", 75, "LAUREN, watching him understand something.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "Miles?"), ("LAUREN", "You know what that is.")]),

S("SC-09", 4, "MCU", "STATIC", 65, "He does not answer. SMASH TO BLACK.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", audio="Hard cut to absolute silence."),
]

SHOTS += [
# ============================================================ ACT TWO
S("SC-10", 7, "MED", "HANDHELD-SUBTLE", 35,
  "MILES moves, fast. He has the box in one hand and is reaching for the pane "
  "with the other.", "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True, music="M05",
  dlg=[("MILES", "It's a display unit. It's a demo. Somebody's testing a-")]),

S("SC-10", 8, "MED-2S", "HANDHELD-SUBTLE", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True,
  dlg=[("LAUREN", "Miles."), ("MILES", "-there's a cell in it, a printed cell, they do that now, it holds a charge for-"), ("LAUREN", "Miles.")]),

S("SC-10", 5, "MCU", "STATIC", 65, "He stops, one hand over the pane.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True, audio="Score out on the stop."),

S("SC-10", 5, "CU", "STATIC", 75, "LAUREN.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dlg=[("LAUREN", "You didn't jump.")]),

S("SC-10", 4, "MCU", "STATIC", 65, "", "KITCHEN", "KITCHEN_OVERHEAD", "M",
  dlg=[("MILES", "What?")]),

S("SC-10", 9, "CU", "SLOW PUSH", 75, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "It turned on. In our kitchen. In the middle of the night. And you didn't jump.")]),

S("SC-10", 11, "MED-2S", "STATIC", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "I jumped. The smoke alarm made me jump."),
       ("LAUREN", "That thing opened an eye at me and you stood there like you were reading a bill.")]),

S("SC-10", 6, "MED", "HANDHELD-SUBTLE", 40, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True,
  dlg=[("MILES", "I'm putting it in the car."), ("LAUREN", "No."), ("MILES", "Lauren-"), ("LAUREN", "No.")]),

S("SC-10", 10, "MED-2S", "STATIC", 40,
  "She does not raise her voice. She puts one hand flat on the pane and leaves "
  "it there and looks at him. He could move her. They both know he could move "
  "her. He does not.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True, music="M05",
  note="BLOCKING-CRITICAL: her hand on the device, his hand withdrawn. The marriage in one frame."),

S("SC-10", 6, "MCU", "STATIC", 65, "", "KITCHEN", "KITCHEN_OVERHEAD", "M",
  dlg=[("MILES", "We agreed."), ("LAUREN", "We didn't agree to this.")]),

S("SC-10", 9, "MCU", "HANDHELD-SUBTLE", 65, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "M",
  dlg=[("MILES", "We agreed that if anything ever came near us we don't pick it up, we don't turn it over, we don't keep it in the house-")]),

S("SC-10", 7, "CU", "HANDHELD-SUBTLE", 75, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "That is not what we agreed."), ("MILES", "It is exactly-"),
       ("LAUREN", "We agreed we wouldn't go looking!")],
  note="First raised voice of the episode. It is hers. It lasts one line."),

S("SC-10", 7, "MED-2S", "STATIC", 40, "Back down, immediately.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "Nobody ever said what to do when it comes to the door.")],
  audio="Refrigerator. Rain. Score out."),

S("SC-10", 6, "MCU", "STATIC", 65, "MILES, very quiet.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dlg=[("MILES", "Don't be found.")], music="M05"),

S("SC-10", 12, "CU", "SLOW PUSH", 75,
  "LAUREN says it flat and fast, without effort, the way you say a thing you "
  "have said ten thousand times.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "Don't be found. Don't be recorded. Don't go back. Don't answer. Don't send anything forward.")],
  note="THE TERMS, first full statement. Never explained. Never labelled. Delivered as recitation, not exposition."),

S("SC-10", 11, "CU", "STATIC", 75, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "I know them, Miles. I say them at three in the morning. In order. Every night. Have done for six years.")],
  note="PLANT: the double repeats this back to her in SC-11. Place it cleanly."),

S("SC-10", 6, "MCU", "STATIC", 65, "Something crosses him.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dlg=[("MILES", "Six years.")]),

S("SC-10", 12, "CU", "HANDHELD-SUBTLE", 75, "",
  "KITCHEN", "KITCHEN_OVERHEAD", "L",
  dlg=[("LAUREN", "Six years and four months, and we have not said one word about any of it out loud in this house, and I have kept that."),
       ("LAUREN", "I kept it because you asked me to.")]),

S("SC-10", 7, "MED-2S", "STATIC", 40, "She takes her hand off the pane.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", dev=True,
  dlg=[("LAUREN", "So don't tell me what we agreed.")]),

S("SC-10", 8, "MED", "TRACK", 40,
  "She picks the leaf up. Both hands, careful, like a tray.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", dev=True, music="M05",
  dlg=[("MILES", "Where are you going."), ("LAUREN", "I'm putting it on the table where we can see it."), ("MILES", "Don't put it down.")]),

S("SC-11", 7, "WIDE", "STATIC", 35,
  "She puts it down. Flat on the coffee table, dead centre. She sits back on "
  "the couch.", "LIVING", "WARM_LOW", "L", dev=True, audio="Pane on wood. Couch. Rain."),

S("SC-11", 9, "WIDE-2S", "STATIC", 35,
  "MILES stays standing in the doorway - which is exactly between Lauren and "
  "the front hall, and he does not appear to know he has done that. The "
  "television is still on, sound low. Nobody is watching it.",
  "LIVING", "WARM_LOW", "MB", dev=True,
  note="BLOCKING: ninth instance of Miles interposing himself. Never remarked on."),

S("SC-11", 10, "MED-2S", "STATIC", 40,
  "Nothing happens. Nothing keeps happening. Lauren pulls a cushion into her "
  "lap. Miles shifts his weight.",
  "LIVING", "WARM_LOW", "MB", dev=True, music="M05",
  audio="Television, low and indistinct. Rain. Room tone.",
  note="Silence #4. Let it get uncomfortable. The audience must start to relax."),

S("SC-11", 3, "MCU", "STATIC", 65, "",
  "LIVING", "WARM_LOW", "M", dlg=[("MILES", "This is-")]),

S("SC-11", 5, "WIDE-2S", "STATIC", 35,
  "THE LEAF WAKES. No sound, no boot, no logo. The light simply arrives, and it "
  "is on their faces. Miles goes silent mid-word.",
  "LIVING", "MIXED", "MB", dev=True, kind="device", music="M06",
  audio="Absolute silence on the wake. Even the television seems to recede.",
  note="LIGHTING TURN: from here the cold pane is a light source in every living-room shot."),

S("SC-11", 12, "ECU-INSERT", "SLOW PUSH", 100,
  "ON THE PANE: a face in darkness, lit from somewhere low and moving, so that "
  "light shifts across it slowly, as if from water. It is LAUREN'S FACE. Same "
  "age. Same eyes. Same mouth. Hair down and unstyled. A fine pale scar beneath "
  "the left eye, running back along the cheekbone. Old, well healed. She is "
  "absolutely still.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M06",
  note="THE REVEAL. Not monstrous. Not aged. Correct - and too still. That is the entire effect."),

S("SC-11", 6, "CU", "STATIC", 75, "LAUREN does not move. Neither does Miles.",
  "LIVING", "MIXED", "L", audio="Room tone. Rain. No score."),

S("SC-11", 5, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "Lauren.")],
  note="VOICE: Lauren's instrument, flatter, slower, no smile in the timbre. NO BREATH before the line."),

S("SC-11", 8, "CU", "SLOW PUSH", 75,
  "Lauren's hand has gone to her own mouth without her deciding to do it.",
  "LIVING", "MIXED", "L", music="M06"),

S("SC-11", 6, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "I know. Take a second.")]),

S("SC-11", 4, "CU", "STATIC", 75, "", "LIVING", "MIXED", "L",
  dlg=[("LAUREN", "What is this.")]),

S("SC-11", 10, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "You have a burn on the inside of your left wrist. Two inches, curved."),
       ("DOUBLE", "You got it on a stove that isn't in this house.")]),

S("SC-11", 6, "CU-INSERT", "STATIC", 100,
  "Lauren's other hand closes over her own left wrist.",
  "LIVING", "MIXED", "NONE", kind="insert"),

S("SC-11", 8, "ECU-INSERT", "SLOW PUSH", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "You still say them at three in the morning."), ("DOUBLE", "In order.")],
  note="PAYOFF: she said this two minutes ago in SC-10. Let the audience make the connection unaided."),

S("SC-11", 6, "CU", "STATIC", 75, "LAUREN makes a sound. Not a word.",
  "LIVING", "MIXED", "L", audio="One broken intake of breath. Nothing else.", music="M06"),

S("SC-11", 5, "MED", "HANDHELD-SUBTLE", 40, "MILES takes one step into the room.",
  "LIVING", "MIXED", "M", dlg=[("MILES", "Who is this.")]),

S("SC-11", 8, "ECU-INSERT", "STATIC", 100,
  "The face does not answer him. But she is looking at him. She has been "
  "looking at him this entire time.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  note="THE DEEPEST REWATCH PAYLOAD. Her eyeline is on MILES in every shot. Never remarked on."),

S("SC-11", 6, "ECU-INSERT", "STATIC", 100, "To Lauren.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "You've been here too long.")]),

S("SC-11", 4, "CU", "STATIC", 75, "", "LIVING", "MIXED", "L",
  dlg=[("LAUREN", "What?")]),

S("SC-11", 11, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "It was supposed to be short. Somewhere to be, for a while."),
       ("DOUBLE", "Six years isn't a while. It's started to hold.")]),

S("SC-11", 9, "MED-2S", "STATIC", 40, "She talks over him without hurrying.",
  "LIVING", "MIXED", "MB", dev=True,
  dlg=[("MILES", "Hold-"), ("DOUBLE", "There's a correction. I don't know how far out it is. I don't think it's far.")]),

S("SC-11", 4, "CU", "STATIC", 75, "", "LIVING", "MIXED", "L",
  dlg=[("LAUREN", "A correction of what?")]),

S("SC-11", 7, "ECU-INSERT", "SLOW PUSH", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "Of the part where you stayed.")], music="M06",
  note="Hold three seconds of silence after this line. It is the thesis of the season."),

S("SC-11", 9, "MED", "HANDHELD", 35,
  "MILES crosses the room fast. He gets one hand flat on the pane - and stops. "
  "Because his hand is on it and nothing changes. The face keeps talking. He "
  "might as well have put his hand on a wall.",
  "LIVING", "MIXED", "M", dev=True,
  note="DEVICE RULE 5: it does not respond to Miles. Established here, exploited by Lauren in SC-18."),

S("SC-11", 9, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "Lauren, listen. There's a thing you need to not do, and I need you to hear it from me, because you won't hear it from-")]),

S("SC-11", 5, "CU", "STATIC", 75, "LAUREN, cutting across her.",
  "LIVING", "MIXED", "L", dlg=[("LAUREN", "How do you have my face?")]),

S("SC-11", 8, "ECU-INSERT", "SLOW PUSH", 100,
  "For the first time, the face hesitates. It is a small thing. Half a second. "
  "But it is the first human beat she has had, and it is horrible, because it "
  "means she is deciding what to say.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M06",
  dlg=[("DOUBLE", "Because I-")]),

S("SC-11", 4, "INSERT-FOOTAGE", "HANDHELD", 24,
  "THE FOOTAGE. Degraded, narrow, recovered-looking. Night, outdoors, hard rain "
  "in a hard light. MILES and LAUREN, older - not much, enough. Moving fast, "
  "not running: escorting, one holding the other up. Miles has blood in his "
  "hairline and down the side of his face. Behind them, badly out of focus and "
  "high up, a sodium-yellow SIGN with half a word legible.",
  "ELSEWHERE", "DEGRADED", "MB", kind="night", dev=True,
  audio="Rain, distorted. Somebody off-frame shouting a name that is not Miles and is not Lauren.",
  note="UNDER FOUR SECONDS. Cut on movement. Never let a face resolve fully. The SIGN pays off in SC-18."),

S("SC-11", 8, "WIDE-2S", "STATIC", 35,
  "BLACK. The pane is dead. The room is dark except for the television, still "
  "playing its old film to nobody. Neither of them moves.",
  "LIVING", "TV_ONLY", "MB", dev=True, music="M06",
  audio="Television. Rain. Nothing else.", note="Silence #5."),

S("SC-11", 5, "CU", "STATIC", 75, "", "LIVING", "TV_ONLY", "L",
  dlg=[("LAUREN", "There was a sign.")]),

S("SC-11", 4, "MCU", "STATIC", 65, "", "LIVING", "TV_ONLY", "M",
  dlg=[("MILES", "There wasn't.")]),

S("SC-11", 8, "MED-2S", "STATIC", 40, "",
  "LIVING", "TV_ONLY", "MB",
  dlg=[("LAUREN", "Behind us. Yellow. Up high."), ("MILES", "Lauren, it was three seconds of-"),
       ("LAUREN", "There was a sign, Miles.")]),

S("SC-11", 10, "CU", "SLOW PUSH", 75,
  "She turns and looks at him properly for the first time since it started.",
  "LIVING", "TV_ONLY", "L",
  dlg=[("LAUREN", "And you saw it. Because you stopped breathing.")]),

S("SC-11", 12, "MCU", "STATIC", 65,
  "He does not answer. He does not answer for a long time. Rain on the window. "
  "The film ends and the credits roll, silently, on a television nobody is "
  "watching.",
  "LIVING", "TV_ONLY", "M", audio="Rain. Television credits music, thin and far away.",
  note="Silence #6, and the longest in the act. Hold on his face until it is unbearable."),

S("SC-11", 3, "WIDE-2S", "STATIC", 35, "CHIRP. Cut to black and total silence.",
  "LIVING", "TV_ONLY", "MB", audio="CHIRP. Then a hard cut to absolute silence.",
  note="ACT OUT. The chirp is the last sound. No stinger."),
]

SHOTS += [
# ============================================================ ACT THREE
S("SC-12", 7, "MED", "STATIC", 40,
  "No music. Almost no sound. Just a man working. MILES slides the pane "
  "face-down into the bottom drawer of the sideboard and shuts it.",
  "LIVING", "WARM_LOW", "M", dev=True, music="M07",
  audio="Drawer runners. His breathing. Nothing else."),

S("SC-12", 8, "ECU-INSERT", "SLOW PUSH", 100,
  "He stands there. Then he reaches out and touches the brass drawer pull. It "
  "is cold. He takes his hand back.",
  "LIVING", "WARM_LOW", "NONE", kind="insert", music="M07",
  note="Containment failure #1. No effect, no sound. A cold handle. That is all."),

S("SC-12", 8, "MED", "STATIC", 40,
  "He puts it in a camping cooler. Clips the lid. Stands back. Then, slowly, he "
  "puts his palm flat on the lid. It is warm.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M", dev=True, music="M07",
  note="Containment failure #2."),

S("SC-12", 10, "MED", "HANDHELD-SUBTLE", 35,
  "He goes to the breaker panel in the hall closet and throws the main. The "
  "house dies - refrigerator, television, the lamp in the hall, all of it, gone "
  "at once.",
  "HALL", "WARM_LOW", "M", music="M07",
  audio="Breaker. Then the entire sound bed of the house stops. This is the quietest moment in the episode."),

S("SC-12", 12, "WIDE", "SLOW PUSH", 28,
  "He comes back to the living room in the dark. The pane is lying on the "
  "coffee table where Lauren has put it back. It is glowing.",
  "LIVING", "COLD_PANE", "M", dev=True, kind="device", music="M07",
  note="Containment failure #3, and the reason the audience now believes the rules."),

S("SC-13", 15, "XWIDE", "STATIC", 50,
  "The street. Every house has its lights on except one. A dog barks twice "
  "somewhere. A television flickers blue through a window. Two doors down the "
  "party is still going: laughter, a car door, somebody calling somebody else "
  "an idiot with enormous affection. The world is completely, insultingly fine.",
  "EXT_STREET", "STREET_NIGHT", "NONE", kind="night", music="M07",
  audio="Rain. Party. A dog. Traffic on a main road four streets away.",
  note="The only exterior in Act Three. It exists to make the house smaller."),

S("SC-14", 9, "WIDE-2S", "STATIC", 35,
  "Power back on, one lamp. LAUREN sits in the armchair facing the coffee "
  "table. She has put Miles's canvas jacket over the pane. She has not moved in "
  "a while. Miles comes in and stands.",
  "LIVING", "WARM_LOW", "MB", dev=True, music="M08"),

S("SC-14", 10, "MCU", "STATIC", 65, "She does not look up.",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "I know what it is."),
       ("MILES", "Not who sent it. I don't know that. But I know what it is.")]),

S("SC-14", 8, "CU", "STATIC", 75, "",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "You've seen one."), ("MILES", "I've held one."), ("LAUREN", "When?")]),

S("SC-14", 7, "MCU", "STATIC", 65, "He does not answer.",
  "LIVING", "WARM_LOW", "M", audio="Lamp hum. Rain. Score out.", music="M09"),

S("SC-14", 6, "CU", "STATIC", 75,
  "LAUREN, not being generous. Filing it.",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "Okay."), ("LAUREN", "Then here's the one I actually want.")]),

S("SC-14", 13, "CU", "SLOW PUSH", 75, "She looks up.",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "Why me? It knows my wrist. It knows what I do at three in the morning."),
       ("LAUREN", "It's got my face, Miles. Why does it want me and not you?")]),

S("SC-14", 9, "MCU", "STATIC", 65,
  "Miles opens his mouth. Nothing comes out.",
  "LIVING", "WARM_LOW", "M", note="Silence #7."),

S("SC-14", 8, "CU-INSERT", "STATIC", 100,
  "Lauren watches his hands go flat on the back of the couch. She has seen that "
  "before too.", "LIVING", "WARM_LOW", "NONE", kind="insert",
  note="MILES'S TELL, established in the character bible. This is its first on-screen naming."),

S("SC-14", 8, "MED", "TRACK", 40,
  "She gets up, crosses to the table, lifts the jacket and takes the label out "
  "from under the pane where she left it. She reads it. Then she walks out of "
  "the room.", "LIVING", "WARM_LOW", "L", dev=True,
  dlg=[("MILES", "Where are you-")]),

S("SC-14", 14, "MED", "SLOW PUSH", 50,
  "LAUREN stops in front of the wall calendar. The circled date. Blue pen. "
  "Nothing written in it. She looks down at the label in her hand. She looks up "
  "at the calendar. She stands there a long time.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L", music="M08",
  audio="Refrigerator. Rain. Absolutely no dialogue.",
  note="THE BEST PASSAGE IN THE ACT. Fourteen seconds of a woman doing arithmetic. Do not cover it in dialogue. Do not cut away."),

S("SC-14", 6, "MED", "STATIC", 40,
  "She comes back in with the label held up between two fingers.",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "What happens on the fourteenth.")]),

S("SC-14", 4, "MCU", "STATIC", 65, "", "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "Nothing.")]),

S("SC-14", 12, "CU", "STATIC", 75, "",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "It's on the box, Miles. It's the consignment date."),
       ("LAUREN", "And it's the one day of the year you circle on a calendar and don't write anything in.")],
  note="PAYOFF P7."),

S("SC-14", 14, "CU", "SLOW PUSH", 75, "",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "Six years I've watched you circle that. I never asked."),
       ("LAUREN", "I decided it was somebody's birthday, and that you'd tell me when you could.")]),

S("SC-14", 7, "MED", "STATIC", 40, "She lowers the label.",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "So tell me when you can.")], music="M08"),

S("SC-14", 8, "MED", "STATIC", 40,
  "MILES sits down on the arm of the couch. It takes him a moment to do it.",
  "LIVING", "WARM_LOW", "M", audio="Score out."),

S("SC-14", 8, "MCU", "STATIC", 65, "",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "Once a year."), ("LAUREN", "Once a year what."), ("MILES", "I send nine words.")],
  note="THE CONFESSION. Play it as small as possible. He is not confessing; he is being drained."),

S("SC-14", 6, "WIDE-2S", "STATIC", 35, "The room is very quiet.",
  "LIVING", "WARM_LOW", "MB", audio="Rain. Nothing else.", music="M09"),

S("SC-14", 12, "MED-2S", "STATIC", 40, "One syllable at a time.",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "You send."), ("MILES", "Yes."), ("LAUREN", "Forward."), ("MILES", "Yes."),
       ("LAUREN", "That's five."), ("MILES", "I know what it is."), ("LAUREN", "Say it."),
       ("MILES", "That's clause five.")]),

S("SC-14", 7, "CU", "STATIC", 75, "",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "How many times."), ("MILES", "Six.")]),

S("SC-14", 9, "MED", "HANDHELD-SUBTLE", 40,
  "LAUREN turns away from him. All the way around, hands on top of her head, "
  "looking at nothing.", "LIVING", "WARM_LOW", "L"),

S("SC-14", 8, "MED-2S", "STATIC", 40, "",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "What are the nine words."), ("MILES", "Lauren-"),
       ("LAUREN", "What are the nine words, Miles.")]),

S("SC-14", 11, "CU", "SLOW PUSH", 75, "MILES.",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "We're still here. We're okay. Don't come. I'm sorry.")],
  note="THE NINE WORDS. Absolutely flat. He has said them six times into a void and they have worn smooth.",
  music="M08"),

S("SC-14", 9, "CU", "STATIC", 75, "She turns back.",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "Who's I'm sorry for?"), ("LAUREN", "Who is it for?")]),

S("SC-14", 7, "MCU", "STATIC", 65, "",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "There's somebody who thinks we didn't make it.")]),

S("SC-14", 8, "MED-2S", "STATIC", 40, "",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "Who."), ("MILES", "Lauren."), ("LAUREN", "Who?")]),

S("SC-14", 10, "CU", "STATIC", 75,
  "He cannot. He physically cannot get it out. His mouth works and nothing comes.",
  "LIVING", "WARM_LOW", "M", music="M09", audio="Score out. Rain.",
  note="The name is never spoken in this episode. It arrives as a voice in SC-22 instead."),

S("SC-14", 10, "CU", "SLOW PUSH", 75,
  "And Lauren - watching him fail - understands something, and goes absolutely "
  "still.", "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "Oh.")]),

S("SC-14", 8, "ECU-INSERT", "STATIC", 100,
  "She looks down at the label in her hand. At the crossed seven. At the date.",
  "LIVING", "WARM_LOW", "NONE", kind="insert", dev=True),

S("SC-14", 12, "MED-2S", "STATIC", 40, "THE TURN.",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("LAUREN", "Miles."), ("LAUREN", "You didn't get a package."), ("MILES", "Don't."),
       ("LAUREN", "You got an answer.")],
  note="THE PIVOT OF THE EPISODE. Quiet. No music. She is not accusing him; she is solving it."),

S("SC-14", 7, "CU", "HANDHELD", 75,
  "It rips out of her. It is the loudest thing in this house in six years and "
  "it is over in two seconds.",
  "LIVING", "WARM_LOW", "L",
  dlg=[("MILES", "Lauren-"), ("LAUREN", "YOU PUT OUR ADDRESS IN THE AIR ONCE A YEAR FOR SIX YEARS AND LET ME THINK I WAS SAFE!")],
  note="THE LOUDEST HUMAN SOUND IN THE EPISODE. One line. Then the silence afterward is enormous."),

S("SC-14", 6, "MCU", "STATIC", 65, "Miles has not moved.",
  "LIVING", "WARM_LOW", "M", audio="Total silence for two seconds after her line."),

S("SC-14", 9, "MCU", "STATIC", 65, "Low.",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "It's nine words. There's no address in it. There's no-"),
       ("LAUREN", "There's a when.")]),

S("SC-14", 13, "CU", "SLOW PUSH", 75, "That stops him.",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "Every year. Same day. Same time, I'd bet."),
       ("LAUREN", "You didn't tell them where we are. You told them we're regular.")]),

S("SC-14", 6, "CU", "STATIC", 75,
  "Miles puts his hand over his mouth and holds it there.",
  "LIVING", "WARM_LOW", "M"),

S("SC-14", 7, "CU", "STATIC", 75, "",
  "LIVING", "WARM_LOW", "L", dlg=[("LAUREN", "They didn't find us. You waved.")],
  note="The cruellest line in the episode and she does not raise her voice for it."),

S("SC-14", 8, "WIDE-2S", "STATIC", 35, "Long silence.",
  "LIVING", "WARM_LOW", "MB", audio="Rain. Refrigerator. Score out.", music="M09",
  note="Silence #8. Separated framing: they are at opposite ends of the widest lens in the room."),

S("SC-14", 8, "MED-2S", "STATIC", 40, "",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("MILES", "They told us nobody would come looking."), ("LAUREN", "They told us a lot of things.")]),

S("SC-14", 16, "MCU", "SLOW PUSH", 65, "",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "They said the whole point - the entire point, Lauren, the reason for all of it,"),
       ("MILES", "the reason we don't have photographs and I check a street I have checked eleven thousand times -"),
       ("MILES", "was that if we did it properly, nobody would ever have to come.")],
  note="PAYOFF P1. The picture hooks are explained here, in an argument, at speed, and never returned to."),

S("SC-14", 10, "CU", "STATIC", 75, "",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "And you did it properly."), ("MILES", "I did it properly for three hundred and sixty-four days a year.")]),

S("SC-14", 9, "MED", "STATIC", 40,
  "She sits down on the coffee table, right beside the covered pane, because "
  "her legs have stopped being interested.",
  "LIVING", "WARM_LOW", "L", dev=True, dlg=[("LAUREN", "Yeah.")]),

S("SC-14", 10, "MED-2S", "STATIC", 40,
  "Almost - almost - the ghost of the two people from the beginning of the "
  "evening. Then it is gone.",
  "LIVING", "WARM_LOW", "MB", music="M08",
  dlg=[("LAUREN", "I'm not angry that you lied."), ("MILES", "You are."),
       ("LAUREN", "I'm a little angry that you lied.")]),

S("SC-14", 13, "CU", "SLOW PUSH", 75, "The thesis of the marriage.",
  "LIVING", "WARM_LOW", "L",
  dlg=[("LAUREN", "You didn't protect me, Miles."),
       ("LAUREN", "You just made sure that when it came, I'd be the one who was surprised.")],
  note="THE MOST IMPORTANT LINE IN THE EPISODE. It must be the QUIETEST. No music under it."),

S("SC-14", 7, "MCU", "STATIC", 65,
  "He has no answer to that. There isn't one.",
  "LIVING", "WARM_LOW", "M", audio="Rain. Nothing else."),

S("SC-15", 9, "MED", "STATIC", 40,
  "The room has just got colder. You can see it: her arms come in. She gets up, "
  "takes a grey cardigan off the back of the chair, and pulls it on.",
  "LIVING", "WARM_LOW", "L_CARD", music="M10",
  note="WARDROBE CHANGE WRD-L-A -> WRD-L-B. Cold is a device rule, not a mood. Log to continuity."),

S("SC-15", 9, "MED-2S", "STATIC", 40, "",
  "LIVING", "WARM_LOW", "MB",
  dlg=[("MILES", "It does that."), ("LAUREN", "Does what."), ("MILES", "When it's about to.")]),

S("SC-15", 8, "CU", "STATIC", 75,
  "She looks at him. Six years of not asking, and now every single answer is a "
  "new injury.", "LIVING", "WARM_LOW", "L_CARD",
  dlg=[("MILES", "Lauren."), ("LAUREN", "Don't."), ("MILES", "Lauren.")]),

S("SC-15", 6, "MED-2S", "SLOW PUSH", 40,
  "She stops. He comes over. He does not touch her. He gets close enough to.",
  "LIVING", "WARM_LOW", "MB", music="M08",
  note="FIRST SHARED FRAME SINCE 20:15. The reunion is aborted, but the framing is the promise."),

S("SC-15", 14, "CU", "SLOW PUSH", 75, "The only articulate thing Miles says all night.",
  "LIVING", "WARM_LOW", "M",
  dlg=[("MILES", "I have been so scared for so long that I forgot it was a thing that could end."),
       ("MILES", "I thought if I could just hold it - for long enough-")]),

S("SC-15", 10, "MED-2S", "STATIC", 40,
  "He raises his hand and puts it on her arm, just above the elbow. She lets "
  "him. Ten seconds of two people almost, almost getting back.",
  "LIVING", "WARM_LOW", "MB", music="M08",
  audio="Rain. Two people breathing. Nothing else.",
  note="Silence #9. The near-repair. It must be genuinely tender or the interruption is worthless."),

S("SC-15", 5, "WIDE-2S", "STATIC", 35,
  "LIGHT. The pane, under the jacket, comes on so brightly that the canvas "
  "glows from underneath.",
  "LIVING", "MIXED", "MB", dev=True, kind="device", music="M10",
  audio="No sound. Light only."),

S("SC-15", 5, "MED", "HANDHELD-SUBTLE", 40, "Miles pulls the jacket off.",
  "LIVING", "MIXED", "M", dev=True),

S("SC-15", 9, "ECU-INSERT", "SLOW PUSH", 100,
  "ON THE PANE: no face. A black field. Four words in thin white wide-tracked "
  "type. DO NOT GO BACK.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M10",
  note="Typography must match the main title card exactly. That is the point: it is the same house style."),

S("SC-15", 13, "MED", "STATIC", 40, "Lauren stares at it.",
  "LIVING", "MIXED", "L_CARD", dev=True,
  dlg=[("LAUREN", "Okay. That's what you've been saying. That's what you've been saying all night."),
       ("LAUREN", "Stay put. Do nothing. That's good, isn't it-")]),

S("SC-15", 10, "MED", "SLOW PUSH", 50,
  "She turns to him. MILES has taken a step BACK from the table. Not a flinch - "
  "a retreat. He has put distance between himself and four words on a screen "
  "and he is looking at them like they are a person in the room.",
  "LIVING", "MIXED", "M", dev=True,
  note="THE ACT'S REAL TURN. He is not reacting to the content. He is reacting to the grammar."),

S("SC-15", 11, "MED-2S", "STATIC", 40, "",
  "LIVING", "MIXED", "MB", dev=True,
  dlg=[("LAUREN", "Miles?"), ("MILES", "That's not advice."), ("LAUREN", "What?"),
       ("MILES", "That's not somebody warning us. That's - Lauren, that's word for word.")]),

S("SC-15", 8, "CU", "STATIC", 75,
  "She looks at the screen. Then at him. And then she gets it, and it takes all "
  "the blood out of her too.",
  "LIVING", "MIXED", "L_CARD", dlg=[("MILES", "That's clause three.")]),

S("SC-15", 10, "MED-2S", "SLOW PUSH", 40, "",
  "LIVING", "MIXED", "MB", dev=True, music="M10",
  dlg=[("LAUREN", "Somebody over there is reading us our own Terms."),
       ("MILES", "Somebody over there has them.")]),

S("SC-15", 12, "ECU-INSERT", "SLOW PUSH", 100,
  "Beneath the four words, small, precise, unhurried, a number appears. 11:00. "
  "It becomes 10:59. Then 10:58.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M11",
  audio="A filtered noise pulse arrives on each second. Felt more than heard.",
  note="THE COUNTDOWN BEGINS. From here it runs in real time and reaches 00:00 at the knock in SC-22."),

S("SC-15", 6, "CU", "STATIC", 75, "Very quietly.",
  "LIVING", "MIXED", "L_CARD", dlg=[("LAUREN", "Down to what.")],
  note="ACT OUT. Cut to black on her face, not on the number."),
]

SHOTS += [
# ============================================================ ACT FOUR
S("SC-16", 9, "WIDE-2S", "STATIC", 35,
  "Overhead light on. Everything visible. Two people working. There is no panic "
  "in this room, and that is the frightening part.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", music="M11",
  note="Their competence IS the horror. Nobody hurries. Nobody drops anything."),

S("SC-16", 11, "MED-2S", "STATIC", 40,
  "Lauren has a pad and is writing a list in fast legible capitals. Miles is at "
  "the back door.", "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("MILES", "Back door, alley, left, and you're on Weir in ninety seconds."),
       ("MILES", "Front door, you're on Cedar, and Cedar only goes two ways.")]),

S("SC-16", 9, "MED-2S", "STATIC", 40, "He says it the way you'd say the milk's off.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "Car?"), ("MILES", "Car's on Cedar."), ("LAUREN", "So the car's decorative."),
       ("MILES", "The car's a place somebody would wait.")]),

S("SC-16", 8, "MED", "TRACK", 40,
  "He goes to the hall closet, reaches up past the coats, and takes down two "
  "canvas duffels. They are grey with dust across the top.",
  "HALL", "WARM", "M", music="M11"),

S("SC-16", 11, "MED-2S", "STATIC", 40, "Lauren stares at them.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "How long have those been up there?"), ("MILES", "Since we moved in."),
       ("LAUREN", "Six years."), ("MILES", "Yes."), ("LAUREN", "You packed one for me."),
       ("MILES", "I packed two.")],
  note="Complicating grace note: he DID prepare for her. He just never told her."),

S("SC-16", 10, "ECU-INSERT", "SLOW PUSH", 100,
  "She unzips hers. Cash in a band. A phone still in its box. Socks. A folding "
  "knife. A coat she does not remember owning. And at the bottom, face-down, a "
  "small photograph.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", music="M11"),

S("SC-16", 12, "CU", "SLOW PUSH", 75,
  "She turns it over. We do not see it. She looks at it for a long moment.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L_CARD",
  dlg=[("LAUREN", "We're not allowed to have this."), ("MILES", "I know.")],
  note="PAYOFF P1 / clause two. NEVER show the photograph. Not this season."),

S("SC-16", 5, "MED", "STATIC", 40, "She puts it in her back pocket.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L_CARD"),

S("SC-16", 6, "MED", "STATIC", 40,
  "Her phone buzzes on the counter. She picks it up. Reads it. Then stops.",
  "KITCHEN", "KITCHEN_OVERHEAD", "L_CARD", audio="Phone buzz on laminate."),

S("SC-16", 9, "ECU-INSERT", "STATIC", 100,
  "THE PHONE. A message from no one. Blank body. Received: 3:14 AM. The clock "
  "at the top of the screen reads 11:26 PM.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", music="M11",
  note="Impossibility #1. Give the audience three full seconds to do the subtraction themselves."),

S("SC-16", 10, "MED-2S", "STATIC", 40,
  "She turns the phone around and shows him. He looks at it for two full seconds.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("MILES", "Okay."), ("LAUREN", "Okay?"), ("MILES", "I'm putting it in the drawer.")]),

S("SC-16", 9, "MED", "STATIC", 40,
  "He takes the phone, opens a drawer, puts it in, and closes it. It is such a "
  "calm, useless, human thing to do that Lauren almost laughs.",
  "KITCHEN", "KITCHEN_OVERHEAD", "M",
  note="The episode's only laugh in the back half. It must be almost, and it must be sad."),

S("SC-16", 11, "ECU-INSERT", "STATIC", 100,
  "The microwave clock. 11:26. It becomes 11:25. Then it sits there. And then, "
  "without hurrying, it goes back to 11:25 again - the same minute twice, four "
  "seconds of a night happening a second time.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", music="M11",
  audio="The refrigerator compressor stutters once, on the repeat.",
  note="Impossibility #2. Neither of them says one word about it. That restraint is the scene."),

S("SC-16", 8, "MED-2S", "STATIC", 40,
  "They both see it. Neither says anything. Lauren picks up her list. Her hand "
  "is not entirely steady. She keeps writing.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("LAUREN", "Money, coats, the label. What else."),
       ("MILES", "Nothing else. That's the whole point of the bags.")]),

S("SC-17", 8, "MED", "STATIC", 40,
  "She goes to reach for her phone in the drawer - stops herself - takes it out "
  "anyway. She opens the camera roll to check something. And her thumb stops "
  "moving.", "KITCHEN", "KITCHEN_OVERHEAD", "L_CARD", music="M11"),

S("SC-17", 12, "ECU-INSERT", "SLOW PUSH", 100,
  "THE PHONE. The most recent photograph: the living room of this house, "
  "tonight - the lamp in tonight's position, the jacket on the arm of the "
  "couch. MILES and LAUREN, asleep, folded together on the couch. Taken from "
  "across the room. From the doorway.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", music="M11",
  note="Impossibility #3, and PAYOFF P2. The most frightening image in the episode is a photograph of them sleeping."),

S("SC-17", 12, "MED-2S", "STATIC", 40,
  "Lauren holds the phone out to him without a word. Miles looks.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  dlg=[("MILES", "When."), ("LAUREN", "Tonight. That's the lamp. That's your jacket."),
       ("MILES", "We didn't sleep tonight."), ("LAUREN", "No.")]),

S("SC-17", 5, "CU-2S", "STATIC", 75, "They look at each other.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB", audio="Score out."),

S("SC-17", 4, "CU-INSERT", "STATIC", 65,
  "CHIRP. The smoke detector above them. Same as it has been all week.",
  "KITCHEN", "KITCHEN_OVERHEAD", "NONE", kind="insert", audio="CHIRP - identical to SC-02."),

S("SC-17", 6, "MED-2S", "STATIC", 40,
  "And then, from the living room: CHIRP. The same tone. The same length. A "
  "half-beat late.",
  "KITCHEN", "KITCHEN_OVERHEAD", "MB",
  audio="CHIRP from off-screen right, spatially placed in the living room. Half a beat late.",
  note="PAYOFF P5. This is the moment the house stops being a house."),

S("SC-17", 10, "MED", "SLOW PUSH", 50,
  "Miles goes to the doorway and looks through into the dark living room. The "
  "pane is lying face-up on the coffee table. It is black. The countdown is not "
  "showing. It is doing nothing at all.",
  "LIVING", "COLD_PANE", "M", dev=True),

S("SC-17", 8, "ECU-INSERT", "STATIC", 100,
  "CHIRP. It comes from the pane, while he is standing there looking at it, and "
  "there is nothing on it to make a sound.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M11",
  audio="CHIRP, sourced precisely at the coffee table. Then absolute silence."),

S("SC-18", 9, "MED-2S", "STATIC", 40, "Lauren comes in behind him.",
  "LIVING", "COLD_PANE", "MB", dev=True,
  dlg=[("LAUREN", "It won't do anything for you."), ("MILES", "What?"),
       ("LAUREN", "You put your whole hand on it and it kept talking. I walk past it, it wakes up.")]),

S("SC-18", 8, "MED", "STATIC", 40,
  "She crouches down in front of the coffee table. Level with the pane.",
  "LIVING", "COLD_PANE", "L_CARD", dev=True,
  dlg=[("MILES", "Lauren."), ("LAUREN", "I know.")]),

S("SC-18", 10, "MED-2S", "STATIC", 40, "",
  "LIVING", "COLD_PANE", "MB", dev=True,
  dlg=[("MILES", "That's four. Don't answer it. That's four, Lauren, that's the one you've never-"),
       ("LAUREN", "And five's yours. So we're even.")],
  note="LAUREN BREAKS A CLAUSE TOO. The marriage is now symmetrical. This is deliberate."),

S("SC-18", 5, "MCU", "STATIC", 65, "That lands. He stops.",
  "LIVING", "COLD_PANE", "M"),

S("SC-18", 10, "CU", "SLOW PUSH", 75, "She looks at the black pane.",
  "LIVING", "COLD_PANE", "L_CARD", dev=True,
  dlg=[("LAUREN", "If you want us to do something, show me where.")],
  audio="Rain. Nothing. Nothing.", music="M11"),

S("SC-18", 8, "WIDE-2S", "STATIC", 35, "Nothing. Nothing.",
  "LIVING", "COLD_PANE", "MB", dev=True, audio="Held silence, five seconds.",
  note="Make the audience believe it isn't going to answer."),

S("SC-18", 9, "INSERT-STILL", "STATIC", 50,
  "THE STILL. Night, rain. A low, long two-storey motel beside a state highway. "
  "External walkway, twelve doors, sodium light. A tall yellow pole sign with "
  "one dead letter: BLU RIDG MOT L. Held. Four seconds. Gone. Black.",
  "MOTEL", "STREET_NIGHT", "NONE", kind="night", dev=True, music="M12",
  note="PAYOFF: this is the sign from the SC-11 footage. Same sign, same dead letter."),

S("SC-18", 9, "MED", "HANDHELD-SUBTLE", 40, "Lauren is on her feet.",
  "LIVING", "COLD_PANE", "L_CARD",
  dlg=[("LAUREN", "That's the sign. Miles, that's the sign from the - that's the sign.")]),

S("SC-18", 8, "MCU", "SLOW PUSH", 65,
  "He is not looking at the pane. He is looking at the middle distance, and he "
  "has gone somewhere else entirely.",
  "LIVING", "COLD_PANE", "M", dlg=[("LAUREN", "Miles. What is it?")]),

S("SC-18", 6, "CU", "STATIC", 75, "",
  "LIVING", "COLD_PANE", "M", dlg=[("MILES", "That's where we came in.")], music="M12"),

S("SC-18", 11, "MED-2S", "STATIC", 40,
  "He says the largest thing he has said all night the way you'd say a street "
  "name.", "LIVING", "COLD_PANE", "MB",
  dlg=[("LAUREN", "What?"), ("MILES", "Room eleven. Second floor, end of the walkway. That's the crossing.")]),

S("SC-18", 11, "CU", "SLOW PUSH", 75, "",
  "LIVING", "COLD_PANE", "L_CARD",
  dlg=[("LAUREN", "I don't remember that."), ("MILES", "No."),
       ("LAUREN", "Miles, I don't remember any of that."), ("MILES", "I know.")],
  note="A SPENT MYSTERY REPLACED BY A BETTER ONE. This is the episode's most important structural move."),

S("SC-18", 9, "MCU", "STATIC", 65, "He finally looks at her.",
  "LIVING", "COLD_PANE", "M",
  dlg=[("MILES", "And I have never once known what to do with that.")]),

S("SC-18", 8, "WIDE", "SLOW PUSH", 28,
  "Lauren stands in the middle of her own living room and feels the floor go.",
  "LIVING", "COLD_PANE", "L_CARD", music="M12", audio="Score thins to one piano note."),

S("SC-18", 13, "MED-2S", "STATIC", 40, "The contradiction lands.",
  "LIVING", "COLD_PANE", "MB", dev=True,
  dlg=[("LAUREN", "It told us not to go back."), ("MILES", "Yes."),
       ("LAUREN", "And then it showed us where to go."), ("MILES", "Yes."),
       ("LAUREN", "So one of those is a lie."), ("MILES", "Yes."), ("LAUREN", "Which one?"),
       ("MILES", "I don't know.")]),

S("SC-19", 8, "ECU-INSERT", "SLOW PUSH", 100,
  "THE PANE COMES ON. The face again, closer than before, filling more of the "
  "frame. Steady. Tired. Kind.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M12",
  dlg=[("DOUBLE", "Lauren.")]),

S("SC-19", 5, "CU", "STATIC", 75, "Lauren does not answer her.",
  "LIVING", "COLD_PANE", "L_CARD"),

S("SC-19", 10, "ECU-INSERT", "STATIC", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "I'm going to say something, and it's going to be unkind, and I'm sorry, and I'd do it again.")]),

S("SC-19", 7, "ECU-INSERT", "SLOW PUSH", 100, "",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M12",
  dlg=[("DOUBLE", "Count backwards for me. I'll be here at one.")],
  note="THE BREAK. Deliver it warmly. It is a mother's line and she means it kindly."),

S("SC-19", 12, "CU", "SLOW PUSH", 75,
  "Lauren's face comes apart. It is not a scream and it is not tears. It is the "
  "specific and terrible expression of a person hearing, in their own voice, "
  "out of a machine, a sentence that has only ever existed in one room in the "
  "world - and that room does not exist yet.",
  "LIVING", "COLD_PANE", "L_CARD", audio="Score out entirely. Rain. Her breathing.",
  note="THE PERFORMANCE HIGH POINT OF THE EPISODE. Hold. Do not cut away for comfort."),

S("SC-19", 9, "MED", "STATIC", 40,
  "She sits down on the floor. Her hand goes to the pendant at her throat and "
  "closes around it. A reflex much older than her marriage.",
  "LIVING", "COLD_PANE", "L_CARD",
  note="CONTINUITY: first appearance of the pendant reflex. Logged in the character bible."),

S("SC-19", 11, "CU", "STATIC", 75, "Barely audible.",
  "LIVING", "COLD_PANE", "L_CARD",
  dlg=[("LAUREN", "My mother said that."), ("MILES", "Lauren-"),
       ("LAUREN", "My mother said that to me. Every night. Nobody knows that.")]),

S("SC-19", 10, "CU", "STATIC", 75, "She looks up at the screen.",
  "LIVING", "COLD_PANE", "L_CARD",
  dlg=[("LAUREN", "I have never said that out loud. Not once. Not here. Not to him.")]),

S("SC-19", 9, "ECU-INSERT", "STATIC", 100,
  "The double's face does something small and very sad.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "I know."), ("DOUBLE", "She said it to me too.")]),

S("SC-19", 7, "ECU-INSERT", "SLOW PUSH", 100,
  "Her mouth makes a name. Two syllables. It is not Lauren. And where the sound "
  "should be there is a clean, absolute, half-second ABSENCE. Not a bleep. Not "
  "static. A hole.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M12",
  dlg=[("DOUBLE", "Didn't she, [ - - - ]")],
  audio="CRITICAL: the audio bed itself stops for 0.5s. Room tone, rain, everything. Then resumes.",
  note="Do NOT bleep, mute, distort or cover with a sound. REMOVE the audio. The absence must be authored."),

S("SC-19", 8, "MCU", "STATIC", 65,
  "Miles's head snaps around. He heard it. Or heard the shape of it.",
  "LIVING", "COLD_PANE", "M", dlg=[("MILES", "What did you just call her.")]),

S("SC-19", 8, "ECU-INSERT", "STATIC", 100,
  "The double does not answer him. She never has. But she is looking at him.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M12"),

S("SC-19", 8, "MED", "HANDHELD-SUBTLE", 40, "Lauren gets up, unsteady.",
  "LIVING", "COLD_PANE", "L_CARD",
  dlg=[("LAUREN", "What am I?"), ("DOUBLE", "You're the one who-")]),

S("SC-20", 4, "WIDE-2S", "STATIC", 35,
  "BLACK. Every light in the house goes out at once. The refrigerator stops. "
  "The microwave clock dies. The whole building drops into darkness in a single "
  "beat.", "LIVING", "BLACKOUT", "MB", kind="night",
  audio="The entire sound bed cuts. This is the second and last loud moment: the SILENCE is the impact.",
  music="M13"),

S("SC-20", 7, "MED", "HANDHELD-SUBTLE", 40,
  "Lauren freezes. Miles goes straight to the window and pulls the curtain "
  "aside two inches.", "LIVING", "BLACKOUT", "M", kind="night"),

S("SC-20", 9, "WIDE-POV", "STATIC", 50,
  "MILES' POV: the street. Every porch light on. Every window lit. The party "
  "two doors down still going, warm and yellow and loud. Every house on the "
  "street has power.",
  "EXT_STREET", "STREET_NIGHT", "NONE", kind="night", music="M13",
  audio="Muffled through glass: the party, warm and completely indifferent."),

S("SC-20", 7, "WIDE", "SLOW PUSH", 28,
  "Behind Miles, on the coffee table, the pane is glowing steadily. It is the "
  "only light in the house.",
  "LIVING", "COLD_PANE", "M", dev=True, kind="device"),

S("SC-20", 9, "MED", "SLOW PUSH", 50,
  "Miles looks out along the street - left, right, and then back to the left. "
  "To the same spot he checks every night of his life.",
  "LIVING", "BLACKOUT", "M", kind="night", note="PAYOFF P6. Same sightline as SC-05."),

S("SC-20", 6, "WIDE-POV", "STATIC", 85,
  "There is a FIGURE standing at the edge of the streetlight's throw. Not "
  "close. Not moving.",
  "EXT_STREET", "STREET_NIGHT", "FIG", kind="night", music="M13",
  note="Soft, small in frame, absolutely still. No detail. Do not silhouette dramatically."),

S("SC-20", 5, "MCU", "STATIC", 65,
  "Miles turns his head fully to look at it directly.",
  "LIVING", "BLACKOUT", "M", kind="night"),

S("SC-20", 5, "WIDE-POV", "STATIC", 85, "There is nobody there.",
  "EXT_STREET", "STREET_NIGHT", "NONE", kind="night",
  note="No whip-pan. No sting. Just an empty pavement, held one beat too long."),

S("SC-20", 8, "MCU", "STATIC", 65, "He does not move for a long moment.",
  "LIVING", "BLACKOUT", "M", kind="night", audio="Rain. The party. His breathing."),

S("SC-20", 8, "ECU-INSERT", "STATIC", 100,
  "From the front hall, very clearly, in a completely silent house: THE "
  "DEADBOLT TURNS. One full revolution.",
  "ENTRY", "BLACKOUT", "NONE", kind="insert", music="M13",
  audio="The brass mechanism, close-mic'd, unhurried. The single most important sound effect in the episode.",
  note="ACT OUT. Nobody touches it. Cut to black on the sound, not after it."),
]

SHOTS += [
# ============================================================ ACT FIVE
S("SC-21", 10, "WIDE-2S", "STATIC", 35,
  "Dark. The pane is the only light in the world and it is the wrong colour for "
  "a home. Neither of them screams. Neither of them runs.",
  "LIVING", "COLD_PANE", "MB", dev=True, kind="night", music="M13",
  note="THE THESIS OF ACT FIVE: they are competent, and it is worse."),

S("SC-21", 11, "MED", "HANDHELD-SUBTLE", 40,
  "Miles crosses the room, takes the armchair by the back, and drags it - "
  "quietly, without hurry - into the mouth of the hallway. Not a barricade. An "
  "obstacle. A thing to trip on in the dark.",
  "LIVING", "COLD_PANE", "M", kind="night", audio="Chair legs on carpet, then on board."),

S("SC-21", 12, "MED", "HANDHELD-SUBTLE", 40,
  "Lauren shoulders her bag, picks up the pane, wraps it in the cardigan and "
  "puts it in the bag. Then she takes the fire iron from the hearth and puts it "
  "on the coffee table where either of them can reach it.",
  "LIVING", "COLD_PANE", "L_CARD", dev=True, kind="night",
  note="She arms them both. She does not hand him the iron; she puts it where either can take it."),

S("SC-21", 8, "WIDE-2S", "STATIC", 35,
  "They move around each other in the dark like people who have done a drill. "
  "Because they have.",
  "LIVING", "COLD_PANE", "MB", kind="night", music="M13"),

S("SC-21", 9, "MED-2S", "STATIC", 40, "",
  "LIVING", "COLD_PANE", "MB", kind="night",
  dlg=[("MILES", "Back door."), ("LAUREN", "No."),
       ("MILES", "Lauren, the alley's clear, you go left and you're-"), ("LAUREN", "No."), ("MILES", "Please.")]),

S("SC-21", 9, "CU", "STATIC", 75, "",
  "LIVING", "COLD_PANE", "L_CARD", kind="night",
  dlg=[("LAUREN", "I'm not doing the part where you decide for me twice in one night.")]),

S("SC-21", 11, "MED-2S", "STATIC", 40, "That stops him dead.",
  "LIVING", "COLD_PANE", "MB", kind="night",
  dlg=[("MILES", "That's not what this is."), ("LAUREN", "That's exactly what this is."),
       ("LAUREN", "You've done it for six years. It's the only thing you're actually good at.")]),

S("SC-21", 9, "CU", "SLOW PUSH", 75, "Gentler, and worse.",
  "LIVING", "COLD_PANE", "L_CARD", kind="night",
  dlg=[("LAUREN", "Miles. We're doing this one together or we're not doing it.")]),

S("SC-21", 7, "MCU", "STATIC", 65, "He looks at her in the light off the bag.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night",
  dlg=[("MILES", "Okay."), ("LAUREN", "Okay.")],
  note="WARDROBE: jacket is now on. WRD-M-B from here to end."),

S("SC-21", 7, "ECU-INSERT", "STATIC", 100,
  "She checks the pane through the fabric. The number is showing through the "
  "weave. 01:20. 01:19.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M13",
  note="COUNTDOWN CHECK: this must read 01:20 at exactly 1:20 before the knock. Bound in the EDL."),

S("SC-21", 8, "MED-2S", "STATIC", 40, "",
  "LIVING", "COLD_PANE", "MB", kind="night",
  dlg=[("MILES", "There's something you need to know before that gets to zero."),
       ("LAUREN", "Then say it fast.")]),

S("SC-21", 11, "CU", "SLOW PUSH", 75, "",
  "LIVING", "COLD_PANE", "M_JKT", kind="night",
  dlg=[("MILES", "Nobody comes over."), ("LAUREN", "What?"),
       ("MILES", "It's not against the rules. It's - Lauren, it isn't a rule, it's a fact.")]),

S("SC-21", 12, "MED-2S", "STATIC", 40, "",
  "LIVING", "COLD_PANE", "MB", kind="night",
  dlg=[("MILES", "People don't cross. Things don't cross."), ("LAUREN", "We crossed."),
       ("MILES", "We came out. That's different. That's falling. Anyone can fall.")]),

S("SC-21", 11, "CU", "SLOW PUSH", 75,
  "He is not trying to frighten her. He is telling her a load-bearing fact "
  "about the world, and he is terrified.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night", music="M13",
  dlg=[("MILES", "Coming the other way costs something. It costs more than a person has."),
       ("LAUREN", "Meaning what."), ("MILES", "Meaning nothing comes through whole.")],
  note="THE SERIES' DARKEST RULE. Six words. Never elaborated this season."),

S("SC-21", 13, "MED-2S", "STATIC", 40, "",
  "LIVING", "COLD_PANE", "MB", kind="night",
  dlg=[("MILES", "So whatever is out there - whatever it used to be - it paid everything it had to stand on our step."),
       ("MILES", "And it did that on purpose. And it did it tonight.")]),

S("SC-21", 5, "ECU-INSERT", "STATIC", 100, "The number in the bag: 00:41.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M13"),

S("SC-21", 10, "CU", "STATIC", 75, "Lauren stares at him in the dark.",
  "LIVING", "COLD_PANE", "L_CARD", kind="night",
  dlg=[("LAUREN", "Miles, I have to ask you something and I need you to not manage me."),
       ("MILES", "Okay.")]),

S("SC-21", 8, "CU", "SLOW PUSH", 75, "",
  "LIVING", "COLD_PANE", "L_CARD", kind="night",
  dlg=[("LAUREN", "That message."), ("LAUREN", "Did it come from me?")],
  audio="Score out. Absolute silence under the question."),

S("SC-21", 11, "CU", "STATIC", 75,
  "Miles opens his mouth. He does not lie to her. He genuinely, visibly, does "
  "not lie to her. He also does not say anything. Three seconds.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night", music="M14",
  note="THE MOST IMPORTANT PAUSE IN THE EPISODE. Three full seconds. Hold it."),

S("SC-21", 6, "CU", "STATIC", 75,
  "That is the answer, and she takes it standing up.",
  "LIVING", "COLD_PANE", "L_CARD", kind="night", dlg=[("LAUREN", "Okay.")]),

S("SC-22", 6, "MED", "STATIC", 40,
  "LIGHT. Inside the bag, through the cardigan, the pane brightens. Lauren "
  "pulls it out.", "LIVING", "COLD_PANE", "L_CARD", dev=True, kind="night", music="M14"),

S("SC-22", 10, "ECU-INSERT", "SLOW PUSH", 100,
  "THE DOUBLE. Closer than she has ever been. Her face nearly fills the pane. "
  "She is looking straight out - and her eyes are not on Lauren. They are on "
  "Miles. Where they have been all night.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face", music="M14",
  note="THE PAYLOAD. Do not underline it. Do not rack focus to Miles. Just let her eyeline be wrong."),

S("SC-22", 5, "CU", "STATIC", 75, "",
  "LIVING", "COLD_PANE", "L_CARD", kind="night", dlg=[("LAUREN", "Who are you?")]),

S("SC-22", 12, "ECU-INSERT", "SLOW PUSH", 100,
  "And for the first time in the entire episode, the double looks away from "
  "Miles. She looks at Lauren.",
  "LIVING", "COLD_PANE", "D", dev=True, kind="face",
  dlg=[("DOUBLE", "I'm the one who left when they told me to."), ("DOUBLE", "Don't.")],
  audio="Score out on 'Don't'. Nothing under it.",
  note="She is not a threat. She is evidence of what obedience cost. Play it as grief."),

S("SC-22", 8, "ECU-INSERT", "STATIC", 100,
  "The number, small, beneath her face. 00:04. 00:03. 00:02. 00:01. 00:00.",
  "LIVING", "COLD_PANE", "NONE", kind="device", dev=True, music="M14"),

S("SC-22", 8, "WIDE-2S", "STATIC", 35,
  "Nothing happens. The house is silent. The pane holds her face, perfectly "
  "still, waiting with them.",
  "LIVING", "COLD_PANE", "MB", dev=True, kind="night",
  audio="TOTAL SILENCE. No rain, no room tone, nothing. The mix floor drops to zero.",
  note="Eight seconds of nothing after zero. The audience must conclude it is over."),

S("SC-22", 6, "MED-2S", "STATIC", 40,
  "KNOCK. KNOCK. KNOCK. A pause. KNOCK. KNOCK. Three, then two.",
  "LIVING", "COLD_PANE", "MB", kind="night",
  audio="Five knuckle knocks on a wooden door, unhurried, patterned. Dry. No reverb tail.",
  note="It is not a stranger's knock. It has a shape. A private meaning between two people."),

S("SC-22", 10, "CU", "SLOW PUSH", 75,
  "Miles's head comes up. And everything in his face falls apart at once - not "
  "fear. Not fear at all. RECOGNITION.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night", music="M14",
  note="THE EPISODE LIVES OR DIES HERE. Hold on him. It is the answer to who he has been writing to."),

S("SC-22", 8, "CU", "STATIC", 75, "Watching him.",
  "LIVING", "COLD_PANE", "L_CARD", kind="night",
  dlg=[("LAUREN", "Miles."), ("LAUREN", "Miles, what.")]),

S("SC-22", 7, "MED", "STATIC", 50,
  "And from outside - through the door, muffled, unhurried, and warm.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night",
  dlg=[("VOICE (O.S.)", "It's me.")],
  audio="Through a wooden door and a wall. Warm. Kind. Utterly unhurried. Gender deliberately unclear.",
  note="Two syllables. They must sound like an embrace. That is why it is frightening."),

S("SC-22", 5, "CU", "STATIC", 75, "Miles closes his eyes.",
  "LIVING", "COLD_PANE", "M_JKT", kind="night", audio="Nothing at all."),

S("SC-22", 18, "XWIDE", "SLOW PUSH", 24,
  "FINAL SHOT. The dark house. The two of them side by side at last, shoulder "
  "against shoulder, lit from below by a pane of glass that should not exist. "
  "Behind them, deep in frame, the front door - its frosted panel a soft "
  "rectangle of streetlight. Something on the other side moves: a shift of "
  "weight, a change in the light, a shape that is a person and is not quite the "
  "right size for a person. It does not resolve. The deadbolt is already open.",
  "LIVING", "COLD_PANE", "MB", dev=True, kind="night", music="M14",
  audio="One tone, low, and then nothing. Rain returns very faintly at the last second.",
  note="THE ONLY SHARED FRAME SINCE 20:15. It cost them the entire episode to stand next to each other. CUT TO BLACK BEFORE THE DOOR OPENS."),

S("ENDCARD", 12, "TITLE", "STATIC", 0,
  "Black. Silence. Then, thin and wide-tracked: WE'RE FROM THE FUTURE. Below "
  "it, smaller: END OF EPISODE ONE.",
  "PALE", "PALE_FLAT", "NONE", kind="insert", music="M15",
  audio="The main-title tone returns, resolved a semitone lower. Then out."),

# ============================================================ TAG
S("SC-23", 8, "WIDE", "STATIC", 40,
  "A room lit uniformly from everywhere, so that nothing casts a shadow and no "
  "corner can be located. A FIGURE stands at a waist-height surface, seen from "
  "behind and below the shoulders. We will not see their face.",
  "PALE", "PALE_FLAT", "FIG", music="M16",
  audio="Room tone with no reflections in it - an acoustically dead space. Deeply wrong."),

S("SC-23", 8, "ECU-INSERT", "SLOW PUSH", 100,
  "They hold a flat unlit sheet, roughly the size and thickness of the pane. On "
  "it: two records side by side. No photographs. Designations that do not "
  "resolve as language. The first record's status field reads LOST.",
  "PALE", "PALE_FLAT", "NONE", kind="insert",
  note="The sheet is a leaf. Same object, institutional context. Never say so."),

S("SC-23", 6, "CU-INSERT", "STATIC", 100,
  "The figure touches it, once. LOST becomes LOCATED.",
  "PALE", "PALE_FLAT", "NONE", kind="insert",
  audio="No confirmation sound. Nothing acknowledges it."),

S("SC-23", 8, "ECU-INSERT", "SLOW PUSH", 100,
  "They move to the second record. Its status field ALREADY reads LOCATED. "
  "Beside it, a date. It is nineteen years old.",
  "PALE", "PALE_FLAT", "NONE", kind="insert",
  note="THE TAG'S ENTIRE PURPOSE. Nineteen years. Hold long enough to read it and no longer."),

S("SC-23", 6, "MED", "STATIC", 40,
  "The figure stops. Just stops. The only human thing that happens in this room.",
  "PALE", "PALE_FLAT", "FIG"),

S("SC-23", 5, "WIDE", "STATIC", 40, "",
  "PALE", "PALE_FLAT", "FIG",
  dlg=[("SYSTEM VOICE", "Retrieval is already in progress.")],
  audio="Flat, female, pleasant, unhurried. No processing. It sounds like a lift announcement.",
  note="BLACK on the last syllable. No music. No sting."),
]
