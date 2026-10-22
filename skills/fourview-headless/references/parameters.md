# Parameters: invariants and slots

## 1. The one structure
Every stage 515 prompt is `templates/skeleton_515.txt` with slots filled. Text outside the slots is invariant and must not be edited per garment.

## 2. Invariant text (all families, all garments)
| Element | Text (abridged) | Source |
|---|---|---|
| Opening | `Edit the four-figure sheet in <image1> into a finished character reference sheet: keep <image1> as the canvas…` | 00485, 00491 |
| Panel 1-3 subject line | `The leftmost panel shows the standing {{SUBJECT}} from <image2> in full-length front view` | 00485, 00491 |
| Skin rule | `rendered as living human skin matching <image2>` | all validated |
| Background rule | `The absent head and neck occupy only the background above the shoulders; …` | 00485, 00491 |
| Panel-4 crop | `filling its panel from just above the crown of {{POSS}} head down to the base of {{POSS}} neck` (long form) | 00441, 00476, 00478, 00485, 00491 |
| Single-face rule | `this panel is the only one that contains a head or a face` | all validated |
| Closing | `Nothing else is added, removed, restyled or re-lit.` | 00485, 00491 |
| Canvas | `four-view-shoulder-top-enlarged.png` | all except 00436 |
| Sampler | 30 steps, cfg 3.5, euler, simple, denoise 1.0 | all samples |

## 3. Slots (what changes)
| Slot | Round | V / open | Strap | Notes |
|---|---|---|---|---|
| `{{SUBJECT}}` / `{{PRONOUN}}` / `{{POSS}}` | woman / she / her | woman / she / her | woman / she / her | match <image2> sex |
| `{{ABSENCE_FRONT_BACK}}` | with her head and neck absent above the shoulders | with her head and neck absent above the shoulders, and with both shoulders, both arms and both hands present | …and with both rounded shoulders, both arms and both hands present | strap uses "rounded shoulders" |
| `{{ABSENCE_SIDE}}` | …shoulder, arm and hand visible in the same side-view pose | same | same | |
| `{{NECKLINE_ANCHOR}}` | ends cleanly at the garment's own neckline | blazer's own shoulder line + only upper chest in the opening | soft continuous shoulder contour, no horizontal edge | **the core** |
| `{{CHANGE_SCOPE}}` | figures | figures | heads | 00485 vs 00491 |
| `{{GARMENT_WORD}}` | garment | garments | garment | 00485 vs 00491 |
| `{{IDENTITY_TERMS}}` | facial identity and hair | facial identity, hair and expression | facial identity and hair | 00485 vs 00491 |
| `{{OUTFIT}}` | per garment | per garment | per garment | must match the board; end with the garment list, no "on both feet" added |
| `{{LOCK}}` | colour lock | colour lock + shape lock (collar fully shown, cuffs at wrists, straight silhouette) | colour lock | validated text per family |
| `{{NEG_FAMILY}}` | neck exclusions | neck exclusions + horizontal-edge exclusions | horizontal-edge exclusions | |
| `{{NEG_GARMENT}}` | per garment | per garment | per garment | only contradictions with the outfit |

## 4. Validation of the structure
Replay of the skeleton against the metadata:
- strap family filled from `families/strap.txt` reproduces 00491's stage 515 positive with 0 differing sentences.
- V/open family filled from `families/vneck.txt` reproduces 00485's stage 515 positive with 0 differing sentences.
- round family: not replayed. 00436 uses a different opening and a short panel-4 form. The skeleton applies the long form and the skeleton opening. This is an adaptation, not a validated reproduction.

## 5. Wardrobe stage (478)
Slots: `{{GARMENT_LIST}}`, `{{FOOTWEAR}}`, `{{DETAIL_TILES}}` (neckline-dependent, listed in `templates/wardrobe_478.txt`), `{{COLOUR_LOCK}}`, `{{NEG_GARMENT}}`. Input at slot 480: original high-resolution garment photo.

## 6. V family opening slots (updated for 00503)
- `{{OPEN_LABEL}}` and `{{OPEN_CONTENT}}` replace the fixed "open V of the {{INNER}}" wording.
- 00485: OPEN_LABEL = open V of the white top; OPEN_CONTENT = upper chest (replay: 0 differing sentences).
- 00503: OPEN_LABEL = open front of the cardigan; OPEN_CONTENT = the white crew neckline of the tee and the upper chest.

## 7. COLLAR_DETAIL (v1.0.1)
- Not a separate skeleton slot. The skeleton has only {{NECKLINE_ANCHOR}}.
- For the closed-collar round variant, COLLAR_DETAIL is written inside the value of NECKLINE_ANCHOR_COLLAR (families/round.txt).
- Evidence: 00500 (without the clause) lost zip and white collar; 00501 (with it) kept both and stayed headless.
