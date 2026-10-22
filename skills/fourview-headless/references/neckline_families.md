# Neckline families

Each family differs in one slot group: the neckline anchor, the absence phrase, the family negatives and the wardrobe detail tiles. The body of the prompt is shared.

## Round
- Garment: full coverage, sleeves cover shoulders.
- Plain crew/round neck: cut line is the garment's own neckline. Anchor in families/round.txt as NECKLINE_ANCHOR_PLAIN. NOT validated on the top-enlarged canvas.
- Closed collar (mock neck, half-zip with collar): anchor NECKLINE_ANCHOR_COLLAR in families/round.txt. VALIDATED on 00501 and 00510. COLLAR_DETAIL is part of that sentence; use it when zip or shirt collar shows (00500 without it lost both).

## V / open
- Garment: long sleeves cover shoulders; V neck or open outer garment over a top.
- Cut line: the outer garment's shoulder seam; the opening shows only upper chest.
- Anchor (00485): `The top edge of each of these three figures is the blazer's own shoulder line: … inside the open V of the white top only upper chest shows, with nothing rising above the collarbones.`
- Failure modes: round anchor on a covered-shoulder jacket (00480); V-only sentence without the shoulder anchor (00481).
- Navy shows the same structure but detail is limited by input resolution (00494), see SKILL.md section 6.

## Strap
- Garment: exposed shoulders; spaghetti or wide straps.
- Cut line: the soft continuous shoulder contour; shoulders kept.
- Anchor (00491): `Let the top of each figure be the natural slope of the shoulders, … no straight horizontal edge anywhere along the top; …`
- Failure modes: deleting the retain-shoulders sentence grows heads (00438, 00439); the negated horizontal-edge phrase leaves a horizontal cut (00478).
