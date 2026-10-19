# 02b · 幽灵服装台 B 版（上衣 + 下装 · 两件套）

> **状态**：✅ 已验证 —— 样本 `00453 / 00454 / 00455`，正向 547 词 + 负向 192 词，3 张的正负向全文指纹一致（`ca058df58e64` / `6982a1b160cd`）
> **线**：Qwen-Image 2.1 **编辑线**（`LoadImage` → `TextEncodeQwenImage21.images.image_1` → `ComfySwitchNode(switch=False)` → `KSampler`）
> **尺寸**：跟随输入图按 32 对齐；`ResolutionSelector` 被旁路，调它无效
> **逐字原文**：`prompts/02-ghost-set/B-00453-positive.txt` / `B-00453-negative.txt`

## 一、适用 / 不适用

| | |
|---|---|
| ✅ 适用 | 输入图是**两件**（上衣 + 裤/裙），**不叠穿** |
| ⛔ 不适用 | 一件式 → `02a`；上身叠穿 2–3 层 → `02c`；无参考图 → `02-ghost-set-trio.md` |

## 二、变量（换服装只改这几处）

| 变量 | 改哪里 | 填什么 | 不填会怎样 |
|---|---|---|---|
| 服装规格 | 正向第 3 段（保真清单） | 默认原样照抄 | 改写清单 → 模型重画衣服 |
| 件数锁 | 正向第 2 段 | 固定两件：上衣 + 下装，腰头必须外露 | 写松 → 两件被合并成一件 |
| 腰头 | 正向第 5 段 | `waistband fully visible as a separate band` 不许删 | 删掉 → 上衣压住腰头，看起来像连身裙 |
| 底色 | 正向第 5 段 | white / light-grey | 按出图要求 |
| 鞋 | 正向第 4 段 | 照抄 / 配一双 / image2 变体 | 通常不改 |

## 三、标准模式（成品 · 逐字 · 直接粘贴）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. The photograph shows two separate garments, one top and one bottom, and both must appear in the frame as two distinct pieces: the top keeps its own neckline, its own sleeves or straps, its own opening and its own hem, and the bottom keeps its own waistband, its own closure, its own pockets and its own hem. Never join the two into a single garment: the top's hem and the bottom's waistband stay two separate edges with their own stitching, the waistband stays a complete band that belongs to the bottom piece, and the top stays a separate piece worn over it.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame on the floor beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the neckline, the sleeves, the waist, the hems and the shoes. Present the two garments as two pieces worn in order: the bottom piece hangs first with its waistband fully visible as a separate band, and the top piece hangs over it with its own hem ending above or exactly at that waistband, so a clear step and a visible edge remain between the two pieces. Both hems stay fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 四、骨架版（同一份词，把可变量拆成槽位）

骨架 = 成品同一份词，只把 3 处可变量换成 `{{…}}`；腰头露出的那句是 B 版的命门，**不许删**。

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. The photograph shows {{件数：two separate garments, one top and one bottom ／ one single dress}}, and both must appear in the frame as two distinct pieces: the top keeps its own neckline, its own sleeves or straps, its own opening and its own hem, and the bottom keeps its own waistband, its own closure, its own pockets and its own hem. Never join the two into a single garment: the top's hem and the bottom's waistband stay two separate edges with their own stitching, the waistband stays a complete band that belongs to the bottom piece, and the top stays a separate piece worn over it.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame on the floor beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：white ／ light-grey}} seamless studio background, every piece complete inside the frame with generous margins around the neckline, the sleeves, the waist, the hems and the shoes. {{构图段：两件 → Present the two garments as two pieces worn in order: ／ 一件式 → present that dress whole, hanging with its own natural drape}} the bottom piece hangs first with its waistband fully visible as a separate band, and the top piece hangs over it with its own hem ending above or exactly at that waistband, so a clear step and a visible edge remain between the two pieces. Both hems stay fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### 槽位怎么填

| 槽位 | 可填值 | 何时用 |
|---|---|---|
| `件数` | `two separate garments, one top and one bottom` ／ `one single dress`（改一件式就转 02a） | 按输入图 |
| `构图段` | 两件叠放：`Present the two garments as two pieces worn in order` | 不叠穿的套装 |
| `底色` | `white` ／ `light-grey` | 按出图要求 |

## 五、负向（逐字）

```text
one-piece dress, merged into a single garment, the top sewn onto the skirt, joined at the waist, fused into one dress, missing waistband, waistband hidden under the top, the top's hem tucked into the waistband, only one garment shown, top and bottom fused, missing either piece, missing garment, missing piece, only the top shown, only the skirt shown, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 六、参数

| 项 | 值 |
|---|---|
| 采样 | 30 步 · cfg 3.5 · euler / simple · denoise 1.0（负向要生效必须 cfg>1；样本里 25/1.0 也出过合格图） |
| 尺寸 | 跟随输入图，按 32 对齐（1200×1600 → 1216×1600） |
| 张数 | 同词同参数 2–3 张挑一张 |

## 七、判据（发出前自查）

1. 两件分开，腰头/裤袢可见
2. 没有人、没有皮肤
3. 鞋成对
4. 背景是要求的底色
5. 无字

## 八、取证

| 图 | 输入尺寸 | 输出尺寸 | seed |
|---|---|---|---|
| 453 | 1200×2124 | 1216×2112 | 103178549230204 |
| 454 | 1200×1600 | 1216×1600 | 1016232757575833 |
| 455 | 1200×1600 | 1216×1600 | 708191303321310 |

3/3 正负向全文 sha256 相同；参数同为 25 步 / cfg 1.0。逐张见 `evidence/2026-10-19-ghost-ABC-baseline.md`
