---
name: fourview-headless
description: Build ComfyUI four-view character sheets for Qwen Image 2.1 editing workflows, where panels 1-3 are headless garment figures and only panel 4 carries a face. Use when writing or debugging the stage 478 wardrobe-board prompt or the stage 515 four-view prompt, choosing a neckline family (round, V/open, strap), fixing head growth above the shoulders, horizontal shoulder cuts, lost dark-colour detail, or garment mismatch.
---

# fourview-headless

## 1. What is produced

Two stages in one ComfyUI chain:

- **Stage 478, wardrobe board**: a garment photo (slot 480) becomes a ghost-mannequin board. Its output is `<image3>` of stage 515.
- **Stage 515, four-view**: panels 1-3 are the headless front, back and side of the model wearing the outfit. Panel 4 is the only panel with a head and face.

Stage 515 input slots:

| Slot | Content | Standard |
|---|---|---|
| `<image1>` | canvas | `four-view-shoulder-top-enlarged.png` (shoulders touch the top edge). Only 00436 used the older `four-view-shoulder-cut-no-neck.png`. |
| `<image2>` | identity | a clean white-background portrait of the same sex as the garment's wearer (清透白底东方面容肖像 or Sakura, keep fixed within one test) |
| `<image3>` | wardrobe board | stage 478 output |

Sampler for every validated run: 30 steps, cfg 3.5, euler, simple, denoise 1.0.

## 2. The one structure

Every four-view prompt is built from `templates/skeleton_515.txt`. The body text never changes. Only the slots change:

| Slot | Set by | Varies by |
|---|---|---|
| `{{SUBJECT}}`, `{{PRONOUN}}`, `{{POSS}}` | identity | sex of the wearer |
| `{{ABSENCE_FRONT_BACK}}`, `{{ABSENCE_SIDE}}` | family | family |
| `{{NECKLINE_ANCHOR}}` | family | **family (the core)** |
| `{{CHANGE_SCOPE}}`, `{{GARMENT_WORD}}`, `{{IDENTITY_TERMS}}` | family | family (validated wording differs between 00485 and 00491) |
| `{{OUTFIT}}`, `{{LOCK}}` | garment | garment (`{{LOCK}}` = colour and shape locks, validated text per family) |
| `{{NEG_FAMILY}}` | family | family |
| `{{NEG_GARMENT}}` | garment | garment |

Wardrobe stage 478 (`templates/wardrobe_478.txt`) uses its own slots: `{{GARMENT_LIST}}`, `{{FOOTWEAR}}`, `{{DETAIL_TILES}}` (neckline-dependent), `{{COLOUR_LOCK}}`, `{{NEG_GARMENT}}`.

Family values live in `templates/families/round.txt`, `vneck.txt`, `strap.txt`.

## 3. Pick the family

Decide from the garment, not from prompt history.

| Family | Garment | Cut line | Validated |
|---|---|---|---|
| Round, plain | full coverage, crew or round neck, sleeves cover shoulders | the garment's own neckline | not validated on top-enlarged canvas (00436, old canvas only) |
| Round, closed collar | mock neck or half-zip collar that closes around the neck; add COLLAR_DETAIL if zip or shirt collar shows | the closed collar | 00501 (male, PASS), 00510 (female, PASS) |
| V / open | long sleeves cover shoulders; V neck or open jacket over a top | the outer garment's shoulder seam; opening shows only upper chest | 00485 |
| Strap | exposed shoulders, spaghetti or wide straps | a soft continuous shoulder contour; shoulders kept | 00491 (best), 00441, 00476, 00478 |

Stand-collar jackets over an open top are still untested; treat them as a candidate, not as a validated sample.

## 4. Core anchor per family (the only neckline-dependent sentence)

- Round: `The figure in panels 1-3 ends cleanly at the garment's own neckline, no bare skin, no neck stump, no trapezius tapering upward.`
- Round, closed collar (validated 00501, 00510): stored as the value `NECKLINE_ANCHOR_COLLAR` in `templates/families/round.txt`. That name is a key inside round.txt, not a skeleton slot. COLLAR_DETAIL is part of that sentence.
- V / open (OUTER = blazer, INNER = white top in 00485): `The top edge of each of these three figures is the blazer's own shoulder line: the shoulder seams and the rounded shoulders of the blazer form a soft clean edge where the figure ends, not a harsh horizontal cut, and inside the open V of the white top only upper chest shows, with nothing rising above the collarbones.`
- Strap: `Let the top of each figure be the natural slope of the shoulders, the shoulder line curving softly up toward the base of the neck and back down into the collarbones, one continuous rounded contour with no straight horizontal edge anywhere along the top; the exposed shoulders and upper chest stay open around the straps, and the skin melts gently into the white background along the shoulder line.`

Do not put `not a harsh horizontal cut` on strap garments. The negated phrase keeps a horizontal edge alive (00478 against 00491).

## 5. Rules that held across samples

1. One variable per test. Keep seeds, canvas, identity and wardrobe input fixed.
2. Identical anchor text does not guarantee an identical result. The wardrobe board and outfit photo carry real weight (00441, 00476, 00478 share one anchor).
3. Do not shorten the absence phrases or the panel-4 long form. Deleting the retain-shoulders sentence grows heads on strap garments (00438, 00439).
4. Input resolution is a hard limit. A 608 px display image cannot carry buckle, weave or collar-print detail. Re-generating a board from the same small source does not help (00492 vs 00489).
5. Negatives do not fix colour. Use positive colour sentences plus an exposure sentence.
6. Round panel-4 form: the skeleton uses the long form for all families. The round family's old sample used the short form. Test the long form on round before trusting it.

## 6. Navy / dark colour (special case, not a template)

- Colour sentences (undertone, brighter exposure, lifted shadows) moved 00487 from black to readable navy.
- Remaining loss of buckle, weave and collar pattern traces to input resolution (00489, 00494).
- Order of work: high-resolution original photo at slot 480, prompt unchanged, then single-variable lighting or colour tests.

## 7. Diagnosis checklist

1. Heads above the shoulders in panels 1-3 → the family anchor is wrong or a slot was edited. Compare with section 4.
2. Flat horizontal shoulder edge → a negated horizontal phrase is present, or the soft contour is missing.
3. Garment colour drifts dark → add a positive colour sentence and exposure; do not use negatives.
4. Detail missing on zoom → check input resolution before editing the prompt.
5. Outfit does not match the garment → rewrite `{{OUTFIT}}` from the wardrobe board, not from memory.
6. Body text differs from the skeleton → someone edited invariant text. Restore the skeleton.

## 8. Files

- `templates/skeleton_515.txt`: the single four-view structure.
- `templates/families/round.txt`, `vneck.txt`, `strap.txt`: slot values per family, with validation status.
- `templates/wardrobe_478.txt`: wardrobe board structure with neckline-dependent detail tiles.
- `references/evidence.md`, `parameters.md`, `neckline_families.md`, `failure_catalog.md`, `verification.md`.
