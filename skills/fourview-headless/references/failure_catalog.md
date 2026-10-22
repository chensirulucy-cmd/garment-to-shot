# Failure catalogue (recorded mistakes)

| # | Mistake | Evidence | Fix |
|---|---|---|---|
| 1 | Copying a prompt is not copying its result | 00441 / 00476 / 00478 share the anchor and differ in outcome | treat wardrobe board and input as variables too |
| 2 | Round anchor applied to a covered-shoulder jacket | 00480: heads in panels 1-3 | use V-family anchor |
| 3 | Adding a V-neck sentence without changing the shoulder anchor | 00481: still heads | change the shoulder anchor |
| 4 | Deleting the retain-shoulders sentence on a strap garment | 00438, 00439: heads in panels 1-2 | keep the sentence (or use the soft contour) |
| 5 | Negated horizontal phrase leaves a horizontal edge | 00442 and 00478: flat shoulder cut | use the positive soft contour (00491) |
| 6 | Several variables changed in one test | 00480 → 00481 changed anchor and identity | one variable per test |
| 7 | Hard-coded ethnicity in prompt conflicts with identity input | 00480 opener "young East Asian woman" | remove; let 522 decide identity |
| 8 | Hard-coded outfit from an old workflow | old JSON hard-coded black knit and cream skirt | rebuild outfit sentence from the current board |
| 9 | Negatives that contradict the garment | camel suit negatives included `lapelled blazer` | rewrite negatives per garment |
| 10 | Colour fixed only by negatives | `the navy rendered black` had no effect (00487) | positive colour sentence and exposure sentence |
| 11 | Low-resolution wardrobe input | 00470 (608 px) limits detail on navy (00489) | use high-resolution original photo |
| 12 | Re-generating a board from a low-resolution source | 00492 from 00470 jpg; 00494 no better than 00489 | fix the source, not the regeneration |
| 13 | Mixed canvases in comparison | 00436 old canvas vs others top-enlarged | compare on one canvas |
| 14 | Long-form vs short-form panel 4 mixed | 00436 short, others long | prefer the long form |
| 15 | Trusting a file name for its content | `image.png` uploads have no metadata | read PNG `prompt` chunk before analysing |
| 16 | Template drift: one family hand-written as a separate file | round template had a different opening and a short panel-4 form (broke the invariant table) | single skeleton, family files only fill slots |
| 17 | Undocumented wording variants between families | strap "both rounded shoulders" vs V "both shoulders"; V "expression" vs strap without it | make them slots (ABSENCE_*, IDENTITY_TERMS, GARMENT_WORD, CHANGE_SCOPE) |
| 18 | Unvalidated word added to a validated outfit | "on both feet" added to V outfit, absent from 00485 | copy validated text verbatim; replay checks catch it |
| 19 | Placeholder names that do not match between SKILL.md and templates | `{{NEG_EXTRA}}` in SKILL.md vs `{{NEG_OUTFIT}}` in templates | one placeholder list in skeleton, referenced by SKILL.md |
| 20 | Colour lock truncated when rebuilt from memory | V lock lacked the shape-lock sentences present in 00485 | copy lock text from metadata, not from summary |
| 21 | Off-skeleton prompt on a new family | 00498 (male mock-neck sweater): old opening "Edit the four-panel character sheet… Replace the white mannequin", absence stated once, short panel-4; heads grew in panels 1-3. Same garment family as the skeleton but not built from it | build every stage 515 prompt from skeleton_515.txt; reject any prompt whose opening differs |
| 22 | Negated horizontal phrase reused on a non-strap family | 00496 and 00498 both contain "not a harsh horizontal cut"; kept only where validated (V family, 00485) | use positive contour wording in new families |
| 23 | Collar closure anchor overrides outfit details | 00500 (half-zip mock neck + white shirt collar): headless panels 1-3 passed, but the zip and white shirt collar disappeared. Outfit sentence said "half-zip" and "collar show", but the anchor "closes around the base of the neck" won | keep the anchor, add COLLAR_DETAIL slot for zip or shirt collar; test one variable at a time (anchor alone, then anchor plus COLLAR_DETAIL) |
