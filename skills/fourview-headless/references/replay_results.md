# Replay results (v1.0.2)

Each row: skeleton_515.txt filled from families/*.txt, compared with the metadata of the validated sample.

| case | unfilled slots | built chars | metadata chars | differing sentences | result |
|---|---|---|---|---|---|
| strap / 00491 (*00491*.png) | none | 2971 | 2971 | 0 | EXACT MATCH |
| vneck / 00485 (*1792434615625*.png) | none | 2792 | 2793 | 0 | MATCH except one trailing newline in the metadata text |
| round collar / 00501 (*00501.png) | none | 2823 | 2823 | 0 | EXACT MATCH |

## 478 wardrobe template vs the board actually used (00499/00500/00501)

The generic template wardrobe_478.txt does NOT reproduce the knit board text. The board text used for 00499-00501 is stored verbatim in templates/wardrobe_variants/knit-male-half-zip.*.txt.
Template positive and variant positive are different texts; the template contains placeholders {{GARMENT_LIST}} {{FOOTWEAR}} {{DETAIL_TILES}} {{COLOUR_LOCK}}.

## Not covered by replay
- Plain round on top-enlarged canvas (not validated).
- Dark colours (navy, burgundy, indigo): colour behaviour not solved; replay checks text only, not images.
- Video neck/shoulder seam: not tested.
