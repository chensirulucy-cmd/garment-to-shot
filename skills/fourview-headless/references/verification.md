# Verification status

## A. Structure (replay of templates against metadata)
- strap: skeleton + families/strap.txt reproduces 00491 stage 515 positive, 0 differing sentences.
- V/open: skeleton + families/vneck.txt reproduces 00485 stage 515 positive, 0 differing sentences.
- Replay caught three real drifts and they are now slots: change scope (heads vs figures), garment word (singular vs plural), identity terms (with or without expression). It also caught one unvalidated addition ("on both feet") that is now removed from the V outfit.
- round: NOT replayed. 00436 has a different opening and a short panel-4 form.

## B. Visual results (user-confirmed)
- Soft strap contour improves over the older strap anchor (00491 vs 00478, single variable).
- V-family anchor produces a headless result on a covered-shoulder jacket (00485).
- Navy colour sentences move the output from black to readable navy (00487 to 00489/00494).
- Same prompts with different wardrobe input give different navy detail (00489 vs 00494).

## C. Inferred, not directly tested
- Input resolution is the main limit on navy detail (consistent with 00492 and 00494; not isolated).
- Negated phrases re-activate the negated concept (consistent with 00478 and the earlier HEAD RULE samples).
- The round anchor holds on the top-enlarged canvas with the long panel-4 form.

## D. Candidate extensions, NOT in the skill as validated families
These came from the male test prompts (stage 478 and 515 for two outfits, not yet generated):
- Stand-collar bomber over a crew tee: mapped to V/open with a collar-closure anchor (ribbed stand collar closes at the base of the neck). Untested.
- Half-zip mock-neck sweater over a collared shirt: mapped to round with a collar-closure anchor. Untested.
- Male identity portrait (slot 522) was not available, so no male 515 has been run.
Until these pass a replay and a generation test, they stay outside the three validated families.

## E. Still to test
- Round family on top-enlarged canvas with the long panel-4 form (single variable against 00436 on old canvas).
- Soft strap anchor on a second strap garment (transferability of 00491).
- Navy with a high-resolution original photo at slot 480, prompt unchanged from 00494.
- Male garments through the skeleton with a male identity input.

## F. Male cases (round 2 of testing)
- 00496 (dark suede bomber + white tee, V/open family, skeleton-built): headless panels 1-3 — PASS. Note: its panel text is the V skeleton with the bomber's stand collar; the V family's shoulder-line anchor held.
- 00498 (beige half-zip mock-neck sweater, round family with closed collar): heads grew in panels 1-3 — FAIL. Cause: prompt was not built from the skeleton (structure drift, failure 21).
- Fix applied: 00498 prompt rebuilt from skeleton_515.txt + families/round.txt (collar variant). Replay: 26 sentences differ from the failed prompt, all of them structural; 0 unfilled slots. Status: built, NOT yet generated. Pass/fail pending the next run.
- Male identity 522 used: 东亚男性白底证件肖像.png (both cases).

## G. Male 00500 (round family, collar variant, skeleton-built)
- Headless panels 1-3: PASS (fixes 00498 failure).
- Garment fidelity: FAIL. Half-zip and white shirt collar missing; the output reads as a plain mock-neck pullover. Cause: closure anchor vs outfit conflict (failure 23).
- Source of truth for garment: 00499 wardrobe board (zip pull and white point collar visible).
- Next test: add COLLAR_DETAIL to the collar variant, keep everything else identical. Watch for heads returning above the collar.

## H. Confirmed results, v1.0 (user-confirmed in conversation)
| Case | Family | Result |
|---|---|---|
| 00491 | strap | PASS (soft contour anchor) |
| 00485 | vneck | PASS |
| 00500 | round collar, no COLLAR_DETAIL | headless PASS; garment FAIL |
| 00501 | round collar + COLLAR_DETAIL | PASS |
| 00507 | vneck (cardigan) | PASS |
| 00510 | round collar (00242 garment) | PASS |
| 00512 | strap (00451 garment), identity 纯白证件像 | PASS |
| 00513 | strap (00451 garment), identity 清透 | PASS (same result as 00512) |
Not yet validated: plain round on top-enlarged canvas; dark-colour garments (except navy special case); video neck/shoulder seam.

### v1.0.1 correction
SKILL.md, README.md and neckline_families.md now match section H. Earlier 'candidate' wording for closed-collar round is removed. Plain round is still unvalidated on the top-enlarged canvas.
