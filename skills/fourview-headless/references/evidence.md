# Evidence: sample metadata and controlled comparisons

All values read from PNG `prompt` metadata (ComfyUI workflow chunk). Character counts are prompt string lengths.

## A. Sample table

| Sample | Garment | Family | 478 input | Canvas | Identity (522) | 478 pos/neg | 515 pos/neg | Outcome |
|---|---|---|---|---|---|---|---|---|
| 00436 | cream round-neck T-shirt dress | round | 00401 | old (shoulder-cut-no-neck) | 清透 | 3144 / 1266 | 1618 / 1224 | success |
| 00438 | floral slip (ends cleanly at straps) | strap | — | — | — | — | 2410 / 1326 | heads in panels 1-2 (retain-shoulders sentence removed) |
| 00439 | floral slip (empty background) | strap | — | — | — | — | 2531 / 1326 | heads in panels 1-2 (same deletion) |
| 00442 | wine-red slip (Codex base) | strap | — | top | 清透 | 3875 / 1788 | 3167 / 1430 | headless, shoulder horizontal cut |
| 00441 | white-purple floral slip | strap | 00420 | top | 清透 | 3346 / 1610 | 2970 / 1326 | success |
| 00476 | pink watercolour bodycon, wide straps | strap | 00474 | top | 清透 | 3282 / 1843 | 2831 / 1480 | success |
| 00478 (1792430858798, 1792432857487) | red/blue painterly cowl slip | strap | 00449 | top | 清透 | 3274 / 1839 | 2792 / 1465 | success, horizontal shoulder edge |
| 00480 | camel suit, white V top | V/open | 00468 | top | Sakura | 3214 / 1650 | 1739 / 1385 | heads in panels 1-3 |
| 00481 | camel suit, white V top | V/open | 00468 | top | Sakura | 3214 / 1650 | 1814 / 1385 | heads in panels 1-3 |
| 00485 | camel suit, white V top | V/open | 00468 | top | Sakura | 3214 / 1650 | 2793 / 1384 | success |
| 00487 | navy suit (first navy run) | V/open | 00470 | top | Sakura | 2993 / 1556 | 2908 / 1497 | headless; colour too dark |
| 00489 | navy suit (colour sentences added) | V/open | 00470 | top | Sakura | 3302 / 1699 | 3286 / 1648 | colour and detail insufficient |
| 00491 | red/blue painterly cowl slip | strap | 00449 | top | 清透 | 3274 / 1839 | 2971 / 1631 | success, best strap result |
| 00492 | navy board (459 pipeline, 1440 px) | — | 00470 (jpg) | — | — | 459 board: 4328 / 1883 | — | board only |
| 00494 | navy suit | V/open | 00492 | top | Sakura | 3302 / 1699 | 3286 / 1648 | detail still insufficient |

Notes:
- The uploaded file `1792434604609_..._00478.png` and `1792432857487_..._00478.png` carry the same parameters; they are repeat exports of the same baseline.
- 00438, 00439, 00442 values come from the earlier metadata extraction recorded in `fourview-skill-reference.md`, not from a fresh read in this batch.

## B. Controlled comparisons

### B1. Shoulder sentence, single variable (00491 vs 00478)
- Identical: 478 wardrobe prompt, input 00449, canvas, identity, seeds.
- Changed: the 515 shoulder sentence (retain-shoulders + not-a-horizontal-cut → soft continuous contour), plus four appended negatives (negative length 1465 → 1631).
- Result: 00491 preferred by the user. The two changes are semantically one variable (shoulder contour), so this is treated as one controlled change.

### B2. Anchor text identity across floral strap samples (00441 vs 00476 vs 00478)
- The 515 shoulder/neck anchor text is byte-identical across the three.
- Differences are limited to the outfit sentence, the colour lock, and the 478 wardrobe board/input (00420, 00474, 00449).
- Result: identical anchor, different outcome. The wardrobe board and outfit photo are a real variable.

### B3. Input source with identical prompts (00489 vs 00494)
- Identical: 478 prompt (3302 / 1699) and 515 prompt (3286 / 1648).
- Changed: 480 input, 00470 (608 px display) → 00492 (1440 px board regenerated from the same source jpg via the 459 pipeline).
- Result: no visible improvement on navy detail. Regenerating a board from a low-resolution source does not add information.

### B4. Colour sentences (00487 vs 00489/00494)
- 00487 has no colour-positive sentences; the navy turned black.
- 00489/00494 add undertone, exposure and shadow-lift sentences.
- Result: the navy became readable (user: "亮了一个度"). Detail loss remained, so colour and detail are separate problems.

### B5. Round-family anchor (00436 vs V and strap anchors)
- No controlled test exists for round garments on the top-enlarged canvas. The only round sample uses the old canvas.

## C. Shared settings across all samples
- Sampler: 30 steps, cfg 3.5, euler, simple, denoise 1.0 (every sample).
- Seeds: 478:458 = 494 and 515:510 = 518 in most samples (recorded in `fourview-skill-reference.md`).
- Canvas: `four-view-shoulder-top-enlarged.png` for every sample except 00436.
