# 02a · 幽灵服装台 A 版（一件套 / 连衣裙 · 编辑线）

> **状态**：✅ 已验证 —— 样本 `00449 / 00446 / 473 / 474`，正向 511 词 + 负向 186 词，4 张的正负向全文指纹一致（`e2284262dfa1` / `b683add4d83a`）
> **线**：Qwen-Image 2.1 **编辑线**（`LoadImage` → `TextEncodeQwenImage21.images.image_1` → `ComfySwitchNode(switch=False)` → `KSampler`）
> **尺寸**：跟随输入图按 32 对齐；`ResolutionSelector` 被旁路，调它无效
> **逐字原文**：`prompts/02-ghost-set/A-00449-positive.txt` / `A-00449-negative.txt`

## 一、适用 / 不适用

| | |
|---|---|
| ✅ 适用 | 输入图是**一件**（连衣裙 / 连体裤 / 单件睡裙） |
| ⛔ 不适用 | 两件套 → `02b`；上身叠穿 2–3 层 → `02c`；无参考图的纯文字生成 → `02-ghost-set-trio.md` |

## 二、变量（换服装只改这几处）

| 变量 | 改哪里 | 填什么 | 不填会怎样 |
|---|---|---|---|
| 服装规格 | 正向第 3 段（保真清单） | 默认原样照抄；要加工艺点只在清单末尾追加 | 清单被改写 → 模型开始自己设计衣服 |
| 领口 | 正向第 1 段 | 空领口 / 有内搭填满，二选一 | 写成 nothing inside 又要内搭 → 内搭整层被抹掉 |
| 下摆 | 正向第 1 段 | 空下摆 / 单件裙加地面影 | 单件裙不写空 → 长出腿或拖鞋 |
| 底色 | 正向第 5 段 | light-grey / pure white | 默认浅灰；要纯白必须改这里 |
| 鞋 | 正向第 4 段 | 图上带鞋照抄 / 无鞋自动配一双 / 换 image2 变体 | 本版自带两种分支，通常不用改 |
| 件数锁 | 正向第 2 段 | 本版默认一件式；两件/叠穿改用 02b、02c | 写松 → 连身裙被拆成上衣+半裙 |

## 三、标准模式（成品 · 逐字 · 直接粘贴）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. If it shows a single one-piece garment such as a dress, keep it as one continuous garment: one neckline, one shoulder line, one continuous front and back panel running from the shoulders down to the hem, and the waist staying a construction line of that same garment with no horizontal break, no overlap and no separate waistband laid over it. If it shows separate garments, keep exactly that number of separate pieces and no more.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain light-grey seamless studio background, every piece complete inside the frame with generous margins around the collar, the sleeves, the waist, the hems and the shoes. Where the outfit photograph shows separate garments, stack them in the order they are worn so the upper piece's hem falls naturally over the lower piece's waistband; where it shows a single dress, present that dress whole, hanging with its own natural drape and its hem fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 四、骨架版（同一份词，把可变量拆成槽位）

骨架 = 成品同一份词，只把 4 处可变量换成 `{{…}}`；**未替换部分与成品逐字相同**。

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, {{领口写法：空领口 → an open empty neckline showing the inner back fabric ／ 有内搭 → the inner garment fills that opening}}, empty sleeve openings, {{下摆写法：空 → an open empty hem ／ 单件裙 → a hem hanging loose and empty with nothing inside}}，and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. {{件数锁：① 一件式（本版默认）→ If it shows a single one-piece garment such as a dress, keep it as one continuous garment: one neckline, one shoulder line, one continuous front and back panel running from the shoulders down to the hem, and the waist staying a construction line of that same garment with no horizontal break, no overlap and no separate waistband laid over it. ② 两件套 → 用 02b 的件数锁 ③ 叠穿 → 用 02c 的层数锁}} If it shows separate garments, keep exactly that number of separate pieces and no more.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：light-grey ／ pure white}} seamless studio background, every piece complete inside the frame with generous margins around the collar, the sleeves, the waist, the hems and the shoes. Where the outfit photograph shows separate garments, stack them in the order they are worn so the upper piece's hem falls naturally over the lower piece's waistband; where it shows a single dress, present that dress whole, hanging with its own natural drape and its hem fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### 槽位怎么填

| 槽位 | 可填值 | 何时用 |
|---|---|---|
| `领口写法` | 空领口 `an open empty neckline showing the inner back fabric` ／ 内搭填满 `the inner garment fills that opening` | 有无内搭 |
| `下摆写法` | `an open empty hem` ／ `a hem hanging loose and empty with nothing inside` | 单件长裙 |
| `件数锁` | 一件式（默认）／ 两件（转 02b）／ 叠穿（转 02c） | 按输入图件数 |
| `底色` | `light-grey` ／ `pure white` | 按出图要求 |

## 五、负向（逐字）

```text
two-piece set, split into a top and a skirt, separated bodice and skirt, two garments where the image shows one, cut dress, dress divided at the waist, waist seam opened, skirt laid over the dress, extra garment, invented second garment, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, missing garment, missing piece, only the top shown, only the skirt shown, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 六、参数

| 项 | 值 |
|---|---|
| 采样 | 30 步 · cfg 3.5 · euler / simple · denoise 1.0（负向要生效必须 cfg>1；样本里 25/1.0 也出过合格图） |
| 尺寸 | 跟随输入图，按 32 对齐（1200×1600 → 1216×1600） |
| 张数 | 同词同参数 2–3 张挑一张 |

## 七、判据（发出前自查）

1. 件数对：连衣裙没被拆成上衣+半裙
2. 没有人：无头、无手、无脚、无皮肤
3. 领口/下摆是空的：看不到脖子与腿
4. 鞋成对
5. 底色正确
6. 无字

## 八、取证

| 图 | 尺寸 | seed | steps/cfg |
|---|---|---|---|
| 449 | 1216×1600 | 562518119128287 | 25/1.0 |
| 446 | 1216×1600 | 409394909693465 | 25/1.0 |
| 473 | 1216×1600 | 562518119128287 | 30/3.5 |
| 474 | 1216×1600 | 313501990439121 | 30/3.5 |

逐张元数据：`evidence/2026-10-19-ghost-ABC-baseline.md`
