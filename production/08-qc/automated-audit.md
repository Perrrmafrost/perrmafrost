# PHASE 8 — QUALITY CONTROL AUDIT
## We're From The Future · S01E01 "The Package"

Produced by `tools/qc.py`, which reads the actual timeline, screenplay,
EDL and subtitle files. Every row below is an executed check, not a
hand-written assertion. Re-run after any change to the cut.

**41 of 41 checks passing.**

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Runtime inside the 28-38 min brief | PASS | 36.1 min |
| 2 | Shot count plausible for the runtime | PASS | 320 shots, mean 6.8s |
| 3 | No shot under 3 seconds | PASS | shortest 3s |
| 4 | Countdown decreases monotonically | PASS | 89 readings |
| 5 | Countdown hits 00:00 exactly on the knock | PASS | starts 11:00 at 23:25, knock at 34:25 |
| 6 | Countdown start matches the screenplay | PASS | script and picture both read 11:00 |
| 7 | Exactly three physical touches in the episode | PASS | SH0032 @ 02:10, SH0211 @ 22:15, SH0313 @ 34:57 |
| 8 | The last touch is the final shot | PASS | final touch at 34:57 of 36:08 |
| 9 | No daylight lighting state after the teaser | PASS |  |
| 10 | Wardrobe changes are one-way (no reversion) | PASS | jacket from 32:08, cardigan from 21:35 |
| 11 | The double appears only on the leaf | PASS | 19 shots |
| 12 | Device rule shown on screen: reflection lags | PASS |  |
| 13 | Device rule shown on screen: temperature inverts | PASS |  |
| 14 | Device rule shown on screen: needs no power | PASS |  |
| 15 | Device rule shown on screen: ignores Miles | PASS |  |
| 16 | Device rule shown on screen: responds to Lauren | PASS |  |
| 17 | Leaf displays no UI element (five permitted items only) | PASS | clean |
| 18 | Plant and payoff both present: P1 bare picture hooks | PASS |  |
| 19 | Plant and payoff both present: P2 refuses photographs | PASS |  |
| 20 | Plant and payoff both present: P3 the crossed seven | PASS |  |
| 21 | Plant and payoff both present: P4 knows the ending | PASS |  |
| 22 | Plant and payoff both present: P5 the smoke detector | PASS |  |
| 23 | Plant and payoff both present: P6 the sightline | PASS |  |
| 24 | Plant and payoff both present: P7 the circled date | PASS |  |
| 25 | Plant and payoff both present: P9 title drop sideways | PASS |  |
| 26 | Plant and payoff both present: P10 reflection lag | PASS |  |
| 27 | No forbidden sci-fi vocabulary in dialogue | PASS | clean |
| 28 | No year is ever spoken aloud | PASS | clean |
| 29 | Exactly one shouted line, and it is Lauren's | PASS | YOU PUT OUR ADDRESS IN THE AIR ONCE A YEAR FOR SIX YEARS AND... |
| 30 | No score under the three protected revelations | PASS |  |
| 31 | At least eight authored silences | PASS | 21 found |
| 32 | Redacted name is an absence, not a bleep | PASS |  |
| 33 | Mystery preserved: who sent the leaf | PASS |  |
| 34 | Mystery preserved: who Miles writes to | PASS |  |
| 35 | Mystery preserved: what the double is | PASS |  |
| 36 | Lauren's real name is never audible | PASS |  |
| 37 | Subtitle file populated | PASS | 325 cues |
| 38 | No overlapping subtitle cues | PASS | 0 |
| 39 | No subtitle under 0.7s (readability floor) | PASS | 0 |
| 40 | EDL event count matches shot count | PASS | 320 vs 320 |
| 41 | Every shot has a generation prompt and a seed | PASS |  |

## Timeline summary

- **320 shots · 36:08 · mean shot 6.8s**
- Longest shot: 20s · shortest: 3s

| Act | Shots | Runtime | Ends on |
|---|---|---|---|
| TEASER | 49 | 03:37 | MILES' POV: the porch is empty. The street is empty. The mat is dark with r |
| TITLE | 1 | 00:20 | Black. A single low sustained tone, unresolved, more felt than heard. The m |
| ACT ONE | 50 | 05:13 | He does not answer. SMASH TO BLACK. |
| ACT TWO | 55 | 05:43 | CHIRP. Cut to black and total silence. |
| ACT THREE | 66 | 08:49 | Very quietly. |
| ACT FOUR | 60 | 07:18 | From the front hall, very clearly, in a completely silent house: THE DEADBO |
| ACT FIVE | 33 | 04:27 | Black. Silence. Then, thin and wide-tracked: WE'RE FROM THE FUTURE. Below i |
| TAG | 6 | 00:41 | [['SYSTEM VOICE', 'Retrieval is already in progress.']] |

## What this audit cannot check

Honest limits. These require a human or a rendered picture:

- Face consistency against the reference plates (no frames exist yet)
- Lip-sync, performance quality and whether a silence actually plays
- Visual artefacts, hands, eyes, geometry and reflections in generated frames
- Whether the double's eyeline genuinely tracks Miles in the delivered shot
- Whether the mix is dialogue-led, and whether the score stays under it

Those are listed in `production/08-qc/manual-qc-checklist.md` and are the
gate that this file explicitly does not clear.

## Master file audit: S01E01_previs_master.mp4

| Check | Result | Detail |
|---|---|---|
| S01E01_previs_master.mp4: duration matches the cut | PASS | 2168.00s vs 2168.00s |
| S01E01_previs_master.mp4: 1920x960 at 24 fps | PASS |  |
| S01E01_previs_master.mp4: 48 kHz stereo AAC | PASS |  |
| S01E01_previs_master.mp4: subtitle track present | PASS |  |
