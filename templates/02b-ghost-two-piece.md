# 02b · 幽灵服装台 B 版（上衣 + 下装 · 两件套）

- 状态：✅ 已验证（2026-10-19，样本 `00453 / 00454 / 00455`，同一份提示词 547 词 + 负向 192 词）
- 适用：输入图是**两件**（上衣 + 裤/裙），**不叠穿**
- 不适用：一件式连衣裙（用 `02` A 版）、上身叠穿 ≥2 层（用 `02c` C 版）
- 参考图：1 张；提示词正文与负向**逐字取自** `Qwen_image_2.1_00453.png` 内嵌 `prompt`，非手抄

## 变量

| 变量 | 取值 |
|---|---|
| 件数 | 固定 2（上 + 下） |
| 鞋来源 | 输入图自带 / 无鞋自动配一双 |
| 画幅 | 跟随输入图（`custom_size` 关） |

## 正向（逐字）

```
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. The photograph shows two separate garments, one top and one bottom, and both must appear in the frame as two distinct pieces: the top keeps its own neckline, its own sleeves or straps, its own opening and its own hem, and the bottom keeps its own waistband, its own closure, its own pockets and its own hem. Never join the two into a single garment: the top's hem and the bottom's waistband stay two separate edges with their own stitching, the waistband stays a complete band that belongs to the bottom piece, and the top stays a separate piece worn over it.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame on the floor beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the neckline, the sleeves, the waist, the hems and the shoes. Present the two garments as two pieces worn in order: the bottom piece hangs first with its waistband fully visible as a separate band, and the top piece hangs over it with its own hem ending above or exactly at that waistband, so a clear step and a visible edge remain between the two pieces. Both hems stay fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 负向（逐字）

```
one-piece dress, merged into a single garment, the top sewn onto the skirt, joined at the waist, fused into one dress, missing waistband, waistband hidden under the top, the top's hem tucked into the waistband, only one garment shown, top and bottom fused, missing either piece, missing garment, missing piece, only the top shown, only the skirt shown, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 参数

| 项 | 值 |
|---|---|
| 采样 | 30 步 · cfg 3.5 · euler / simple · denoise 1.0 |
| 尺寸 | 跟随输入图（`custom_size` 关） |
| 张数 | 同提示词同参数跑 2–3 张挑一张 |

## 判据

1. 两件分开，腰头可见
2. 无人体、无皮肤
3. 鞋成对
4. 背景纯白
