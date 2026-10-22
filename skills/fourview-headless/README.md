# fourview-headless

Two modules in one skill:
- **478 wardrobe board**: templates/wardrobe_478.txt (generic) and templates/wardrobe_variants/ (verbatim boards actually used).
- **515 four-view**: templates/skeleton_515.txt (single structure) + templates/families/{strap,vneck,round}.txt.


ComfyUI skill for Qwen Image 2.1 editing workflows that produce a four-view character sheet: panels 1-3 are headless garment figures (front, back, side) and panel 4 carries the only face.

## Structure
One skeleton, three neckline families. The body text never changes; only slots do.

- `SKILL.md`: entry point, workflow, family selection, diagnosis.
- `templates/skeleton_515.txt`: the single four-view prompt structure, with slot definitions.
- `templates/families/round.txt`, `vneck.txt`, `strap.txt`: slot values per family, with validation status.
- `templates/wardrobe_478.txt`: wardrobe board structure, neckline-dependent detail tiles.
- `references/evidence.md`: sample metadata and controlled comparisons.
- `references/parameters.md`: invariant text, slot table, replay results.
- `references/neckline_families.md`: how each family works and fails.
- `references/failure_catalog.md`: recorded mistakes and fixes.
- `references/verification.md`: what is replayed, user-confirmed, inferred, or still to test.

## Quick start
1. Choose the family from the garment (SKILL.md section 3).
2. Fill `templates/wardrobe_478.txt` for the board (input: original high-resolution photo).
3. Fill `templates/skeleton_515.txt` with the family values and the outfit from the board.
4. Change one variable per test. Keep canvas, identity, seeds and sampler fixed.

## Status
- strap: replayed and user-validated (00491).
- V/open: replayed and user-validated (00485). Navy is a special case.
- Round, closed collar (mock neck / half-zip collar): validated on 00501 (male) and 00510 (female).
- Round, plain crew neck: not validated on the top-enlarged canvas. Test before use.
- Stand-collar jackets over an open top: candidate only.

Read `references/verification.md` before relying on any family.
