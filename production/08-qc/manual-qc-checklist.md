# MANUAL QC CHECKLIST
## The gate `tools/qc.py` explicitly does not clear

The automated audit reads the timeline, screenplay, EDL and subtitles. It cannot
look at a picture or listen to a mix. Everything below requires a human and a
rendered frame, and **none of it has been performed**, because no frames exist.

Sign-off requires all four sections at PASS.

---

## A. CHARACTER CONSISTENCY — per shot, against the reference plates

| # | Check | Method |
|---|---|---|
| A1 | Face matches `reference/miles_reference_source.jpg` | Side-by-side at 200%, eyes/nose/mouth landmarks |
| A2 | Face matches `reference/lauren_reference_source.jpg` | As above |
| A3 | Miles's left-eye asymmetry preserved when smiling | Frame-grab comparison |
| A4 | Lauren's loose temple strands present in every shot | Visual |
| A5 | Beard length consistent (no growth across one evening) | Sequential compare |
| A6 | Hair position — the ponytail loosens across the episode and never re-tightens | Sequential compare |
| A7 | **The double is the same face, same age, with only the scar differing** | A/B against Lauren in the adjacent shot |
| A8 | The double's scar is the same length, side and shape in all 19 shots | Overlay |
| A9 | **The double's eyeline is on MILES in every shot but the last** | Frame-by-frame eyeline trace |
| A10 | The double's blink rate is roughly one-third of Lauren's | Count blinks per 10s |
| A11 | No plastic skin, no beauty retouch, pores visible on both leads | 100% crop |

## B. CONTINUITY — against `production/05-assets/continuity-matrix.csv`

| # | Check |
|---|---|
| B1 | Wardrobe ID in every frame matches the matrix; no reversion after a change |
| B2 | The choker and pendant are present and identical in every Lauren shot |
| B3 | The leaf's physical position matches the matrix shot to shot |
| B4 | **No photograph is visible anywhere in the house, in any frame, ever** |
| B5 | The four bare hooks are in every hallway frame, unchanged |
| B6 | The circled calendar date is legible and identical in both appearances |
| B7 | **The two crossed-seven inserts match** — pen weight, crossbar angle, ink colour |
| B8 | The motel sign has the same dead letters in the footage and the still |
| B9 | Rain is continuous from 03:15 and never gets heavier |
| B10 | Practical lamp positions consistent; the lamp in the phone photograph matches the room that night |
| B11 | Shadow direction consistent across every cut within a scene |
| B12 | The leaf has no bezel, port, seam, screw, logo or mark in any frame |

## C. PICTURE INTEGRITY

| # | Check |
|---|---|
| C1 | Hands: five fingers, correct articulation, no fusion, in every frame |
| C2 | Eyes: pupils round, gaze consistent, catchlights match the practicals |
| C3 | Text: the label, the calendar, the phone, the motel sign and the leaf's type are all legible and stable frame to frame |
| C4 | Reflections in windows and the pane are geometrically plausible |
| C5 | **The reflection lag is exactly 0.5s and reads clearly on first viewing** |
| C6 | No warping in door frames, worktops, skirting or the couch across a move |
| C7 | No flicker in any practical |
| C8 | Grain present and consistent in every frame, including black frames |
| C9 | No shot exceeds the lookbook's movement ladder for its act |
| C10 | Every face has a readable eye at IRE 8 or above |

## D. SOUND AND MIX

| # | Check |
|---|---|
| D1 | Dialogue intelligible at -27 LKFS dialnorm without raising the master |
| D2 | **Score never audible under a line** — check M08 and M13 specifically |
| D3 | The three protected revelations play with no music |
| D4 | The chirp is the identical recording in all four appearances |
| D5 | The answering chirp is spatially placed at the coffee table |
| D6 | The countdown pulse is inaudible as a discrete sound |
| D7 | **The double is unprocessed and takes no breath before any phrase** |
| D8 | The redacted name is a true 0.5s hole in the bed, not a bleep or a mute |
| D9 | The 8s of silence before the knock reaches an absolute floor |
| D10 | The knock is dry, with no reverb tail |
| D11 | The party gets louder in the mix during the SC-20 blackout |
| D12 | The tag's room has no reflections at all |
| D13 | Lip-sync within one frame throughout |

---

## Regeneration protocol

If any check fails:

1. Regenerate **only** the affected shot. Approved neighbours are never re-run.
2. Increment the version in `shot-prompts.json` (`v1` → `v2`); keep the seed
   unless the failure is compositional.
3. Log the failure, the fix and the new version in the continuity matrix.
4. Re-run `python3 tools/build.py && python3 tools/qc.py`.
5. Re-check the two shots either side for a new continuity break at the seam.

**Approved assets are never overwritten. A new version is created.**
