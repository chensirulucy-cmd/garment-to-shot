# 02E · 幽灵服装台（编辑线 · 有参考图）

> **状态**：✅ 已验证 —— A `00449 / 446 / 473 / 474`（511+186 词）· B `00453 / 454 / 455`（547+192 词）· C `00470 / 472`（745+255 词）
> **线**：Qwen-Image 2.1 **编辑线**（`LoadImage` → `TextEncodeQwenImage21.images.image_1` → `ComfySwitchNode(switch=False)` → `KSampler`）
> **尺寸**：跟随输入图按 32 对齐（1200×1600 → 1216×1600）；`ResolutionSelector` 被旁路，调它无效
> **逐字原文**：`prompts/02-ghost-set/` 下 `A-00449-*` / `B-00453-*` / `C-00472-*`（正负向各一份）
> **无参考图（纯文字创造服装）请用**：`02-ghost-set-trio.md`（文生图线）

## 选版（按输入图，三步选一）

| 输入图 | 版本 | 本文件位置 | 取证 |
|---|---|---|---|
| **一件**（连衣裙 / 连体裤 / 单件睡裙） | **A** | 第二节 | 449 / 446 / 473 / 474 |
| **两件**（上衣 + 裤/裙），**不叠穿** | **B** | 第三节 | 453 / 454 / 455 |
| 上身**叠穿 2–3 层** | **C** | 第四节 | 470 / 472 |

## 一、变量（换服装只改这几处）

| 变量 | 改哪里 | 填什么 | 不填会怎样 |
|---|---|---|---|
| 服装规格 | 第 3 段（保真清单） | 默认「原样照抄」；要加工艺点只在清单末尾追加 | 改写清单 → 模型开始自己设计衣服 |
| 领口 | 第 1 段 | 空领口 ／ 内搭填满（C 版必须写「内搭填满」） | 写成 `nothing inside` 又要内搭 → 内搭整层被抹掉 |
| 下摆 | 第 1 段 | 空下摆 ／ 单件裙加地面影 | 单件裙不写空 → 长出腿或拖鞋 |
| 底色 | 构图段 | `white` ／ `light-grey` | 默认不是纯白；要纯白必须改这里 |
| 鞋 | 鞋段 | 图上带鞋照抄 ／ 无鞋配一双 ／ 第二参考图用 `<image2>` 变体 | 自带两种分支，通常不用改 |
| 件数锁 | 第 2 段 | A 一件式 ／ B 两件腰头外露 ／ C 数层数 | 选错版本 → 拆件、合并、或内搭消失 |

## 二、A 版 · 一件套

### A-1 标准模式（逐字 · 直接粘贴）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. If it shows a single one-piece garment such as a dress, keep it as one continuous garment: one neckline, one shoulder line, one continuous front and back panel running from the shoulders down to the hem, and the waist staying a construction line of that same garment with no horizontal break, no overlap and no separate waistband laid over it. If it shows separate garments, keep exactly that number of separate pieces and no more.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain light-grey seamless studio background, every piece complete inside the frame with generous margins around the collar, the sleeves, the waist, the hems and the shoes. Where the outfit photograph shows separate garments, stack them in the order they are worn so the upper piece's hem falls naturally over the lower piece's waistband; where it shows a single dress, present that dress whole, hanging with its own natural drape and its hem fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### A-2 骨架（槽位）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, {{领口写法：空领口 → an open empty neckline showing the inner back fabric ／ 有内搭 → the inner garment fills that opening}}, empty sleeve openings, {{下摆写法：空 → an open empty hem ／ 单件裙 → a hem hanging loose and empty with nothing inside}}，and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. {{件数锁：① 一件式（本版默认）→ If it shows a single one-piece garment such as a dress, keep it as one continuous garment: one neckline, one shoulder line, one continuous front and back panel running from the shoulders down to the hem, and the waist staying a construction line of that same garment with no horizontal break, no overlap and no separate waistband laid over it. ② 两件套 → 用 02b 的件数锁 ③ 叠穿 → 用 02c 的层数锁}} If it shows separate garments, keep exactly that number of separate pieces and no more.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：light-grey ／ pure white}} seamless studio background, every piece complete inside the frame with generous margins around the collar, the sleeves, the waist, the hems and the shoes. Where the outfit photograph shows separate garments, stack them in the order they are worn so the upper piece's hem falls naturally over the lower piece's waistband; where it shows a single dress, present that dress whole, hanging with its own natural drape and its hem fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

| 槽位 | 可填值 |
|---|---|
| `{{领口写法}}` | 空领口 `an open empty neckline showing the inner back fabric` ／ 内搭填满 `the inner garment fills that opening` |
| `{{下摆写法}}` | `an open empty hem` ／ `a hem hanging loose and empty with nothing inside` |
| `{{件数锁}}` | 一件式（默认）／ 两件（转 B）／ 叠穿（转 C） |
| `{{底色}}` | `light-grey` ／ `pure white` |

### A-3 判据

1. 件数对：连衣裙没被拆成上衣 + 半裙
2. 没有人：无头、无手、无脚、无皮肤
3. 领口/下摆是空的
4. 鞋成对
5. 底色正确
6. 无字

## 三、B 版 · 两件套

### B-1 标准模式（逐字）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. The photograph shows two separate garments, one top and one bottom, and both must appear in the frame as two distinct pieces: the top keeps its own neckline, its own sleeves or straps, its own opening and its own hem, and the bottom keeps its own waistband, its own closure, its own pockets and its own hem. Never join the two into a single garment: the top's hem and the bottom's waistband stay two separate edges with their own stitching, the waistband stays a complete band that belongs to the bottom piece, and the top stays a separate piece worn over it.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame on the floor beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the neckline, the sleeves, the waist, the hems and the shoes. Present the two garments as two pieces worn in order: the bottom piece hangs first with its waistband fully visible as a separate band, and the top piece hangs over it with its own hem ending above or exactly at that waistband, so a clear step and a visible edge remain between the two pieces. Both hems stay fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### B-2 骨架（槽位）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. The photograph shows {{件数：two separate garments, one top and one bottom ／ one single dress}}, and both must appear in the frame as two distinct pieces: the top keeps its own neckline, its own sleeves or straps, its own opening and its own hem, and the bottom keeps its own waistband, its own closure, its own pockets and its own hem. Never join the two into a single garment: the top's hem and the bottom's waistband stay two separate edges with their own stitching, the waistband stays a complete band that belongs to the bottom piece, and the top stays a separate piece worn over it.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame on the floor beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：white ／ light-grey}} seamless studio background, every piece complete inside the frame with generous margins around the neckline, the sleeves, the waist, the hems and the shoes. {{构图段：两件 → Present the two garments as two pieces worn in order: ／ 一件式 → present that dress whole, hanging with its own natural drape}} the bottom piece hangs first with its waistband fully visible as a separate band, and the top piece hangs over it with its own hem ending above or exactly at that waistband, so a clear step and a visible edge remain between the two pieces. Both hems stay fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

| 槽位 | 可填值 |
|---|---|
| `{{件数}}` | `two separate garments, one top and one bottom` ／ `one single dress`（改一件式转 A） |
| `{{构图段}}` | 两件叠放：`Present the two garments as two pieces worn in order` |
| `{{底色}}` | `white` ／ `light-grey` |

### B-3 判据

1. 两件分开，腰头/裤袢可见（**这句是 B 版命门，不许删**）
2. 没有人、没有皮肤
3. 鞋成对
4. 底色正确
5. 无字

## 四、C 版 · 上身叠穿

### C-1 标准模式（逐字）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet and no toes anywhere in the frame, and hold the garments with natural hollow volume as if worn by an invisible body — rounded shoulders, empty sleeve openings, an open empty hem, and no body inside them.

The outfit is layered on the upper body. Count the layers the photograph actually shows — two, or three if a third is visible — and keep exactly that many layers, each as its own separate hollow shell, worn in the same order as the photograph: the innermost piece closest in, each outer piece over it. The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth and the same shape as the photograph, its front closure stays pulled down to exactly the same point on the chest as the photograph, and the inner garment fills that opening — its collar rising above the outer edge by the same amount the photograph shows, its collar points lying open over the outer layer, its buttoned placket and its inner surface visible down inside the opening. The inner garment is the only thing inside the outer one, and no skin, no neck and no body appears in that opening. Where the photograph shows an inner cuff emerging beyond an outer sleeve end, keep it emerging by the same amount; where the photograph shows no inner cuff, the outer sleeve end finishes the arm cleanly. Never merge two layers into one garment, never drop a layer, never add a layer, never reverse the order, and never close an opening the photograph leaves open.

There is one lower garment, trousers or a skirt exactly as photographed, worn below the upper layers with its waistband sitting under the outer layer's hem, its own closure, pockets and hem unchanged, and its hem ending at the same point on the leg or the ankle as in the photograph.

Copy, do not redraw. Every garment must come out of the photograph unchanged, piece for piece and stitch for stitch: the same fabric, weave, knit or twill texture at the same scale, the same colour, the same print or pattern, the same collar shape, the same closures and hardware in the same places, the same cuffs, pockets and hems, the same cut and proportions, and the same shoes with the same sole, toe shape and material. Do not describe these garments from words, do not improve them, do not substitute a similar-looking piece and do not change any colour, fabric or pattern — a close lookalike is a failure, only the photographed garment is correct.

Handle the footwear as follows. If the photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height. If the photograph shows no shoes at all, add one single pair of plain, understated shoes that belongs with this outfit, in a neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment. Either way the shoes appear once, as one matched pair, placed side by side on the studio floor at the bottom of the frame beneath the hem, angled slightly outward, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the collars, the cuffs, the waist, the hems and the shoes, all pieces hung in the order they are worn so every layer's edge remains visible, presented as a straight front view rather than a walking or seated pose. Remove any bag, tote, hat or accessory that the photograph shows, so the frame contains the garments and the shoes only.

Remove every brand text, logo, watermark, price tag and caption from the photograph, including any printed advertising text and brand marks, so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with the fabric texture, knit stitch, drape and seam detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### C-2 骨架（槽位）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet and no toes anywhere in the frame, and hold the garments with natural hollow volume as if worn by an invisible body — rounded shoulders, empty sleeve openings, an open empty hem, and no body inside them.

The outfit is layered on the upper body. Count the layers the photograph actually shows — {{层数：two ／ two, or three if a third is visible}} — and keep exactly that many layers, each as its own separate hollow shell, worn in the same order as the photograph: the innermost piece closest in, each outer piece over it. The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth and the same shape as the photograph, its front closure stays pulled down to exactly the same point on the chest as the photograph, and the inner garment fills that opening — {{内层露出量：its collar rising above the outer edge by the same amount the photograph shows ／ its collar and both cuffs emerging by the same amount the photograph shows}}, its collar points lying open over the outer layer, its buttoned placket and its inner surface visible down inside the opening. The inner garment is the only thing inside the outer one, and no skin, no neck and no body appears in that opening. Where the photograph shows an inner cuff emerging beyond an outer sleeve end, keep it emerging by the same amount; where the photograph shows no inner cuff, the outer sleeve end finishes the arm cleanly. Never merge two layers into one garment, never drop a layer, never add a layer, never reverse the order, and never close an opening the photograph leaves open.

There is one lower garment, {{下装：trousers ／ a skirt}} exactly as photographed, worn below the upper layers with its waistband sitting under the outer layer's hem, its own closure, pockets and hem unchanged, and its hem ending at the same point on the leg or the ankle as in the photograph.

Copy, do not redraw. Every garment must come out of the photograph unchanged, piece for piece and stitch for stitch: the same fabric, weave, knit or twill texture at the same scale, the same colour, the same print or pattern, the same collar shape, the same closures and hardware in the same places, the same cuffs, pockets and hems, the same cut and proportions, and the same shoes with the same sole, toe shape and material. Do not describe these garments from words, do not improve them, do not substitute a similar-looking piece and do not change any colour, fabric or pattern — a close lookalike is a failure, only the photographed garment is correct.

Handle the footwear as follows. If the photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height. If the photograph shows no shoes at all, add one single pair of plain, understated shoes that belongs with this outfit, in a neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment. Either way the shoes appear once, as one matched pair, placed side by side on the studio floor at the bottom of the frame beneath the hem, angled slightly outward, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：white ／ light-grey}} seamless studio background, every piece complete inside the frame with generous margins around the collars, the cuffs, the waist, the hems and the shoes, all pieces hung in the order they are worn so every layer's edge remains visible, presented as a straight front view rather than a walking or seated pose. Remove any bag, tote, hat or accessory that the photograph shows, so the frame contains the garments and the shoes only.

Remove every brand text, logo, watermark, price tag and caption from the photograph, including any printed advertising text and brand marks, so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with the fabric texture, knit stitch, drape and seam detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

| 槽位 | 可填值 |
|---|---|
| `{{层数}}` | `two` ／ `two, or three if a third is visible` |
| `{{内层露出量}}` | 只露领口 ／ 领口 + 两袖口 |
| `{{下装}}` | `trousers` ／ `a skirt` |
| `{{底色}}` | `white` ／ `light-grey` |

### C-3 判据

1. 领口里是衣服不是空的（内层领子/门襟可见，没有脖子）
2. 拉链/开口停在原图位置，不被拉到顶
3. 两层有可见分界
4. 没有人、没有皮肤
5. 底色正确

## 五、负向（三版各一段，按版本取用）

### A 负向

```text
two-piece set, split into a top and a skirt, separated bodice and skirt, two garments where the image shows one, cut dress, dress divided at the waist, waist seam opened, skirt laid over the dress, extra garment, invented second garment, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, missing garment, missing piece, only the top shown, only the skirt shown, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

### B 负向

```text
one-piece dress, merged into a single garment, the top sewn onto the skirt, joined at the waist, fused into one dress, missing waistband, waistband hidden under the top, the top's hem tucked into the waistband, only one garment shown, top and bottom fused, missing either piece, missing garment, missing piece, only the top shown, only the skirt shown, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

### C 负向

```text
neckline closed that the photograph leaves open, zip pulled up to the collar, collar closed to the throat, missing inner collar, missing inner placket, the opening filled with skin, bare neck in the neckline, merged layers, fused into one garment, two layers joined into one, one piece split into two, missing layer, missing inner layer, missing inner cuffs, extra layer, invented layer, layer order reversed, the inner layer worn outside, the outer layer worn inside, single top layer, only the outer garment shown, only the inner garment shown, missing garment, extra garment, missing lower garment, skirt replaced by trousers, trousers replaced by a skirt, missing waistband, waistband hidden, redrawn garment, similar-looking substitute, different garment, restyled garment, simplified texture, invented knit pattern, changed closure, different collar shape, changed pocket placement, changed trouser cut, changed shoe design, different shoes than the photograph, mismatched pair, only one shoe, two different shoes, added belt, added scarf, added bag, handbag, tote, added accessories, walking pose, mid-stride, seated pose, motion blur, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, Chinese characters, price tag, embroidery, added pattern, added print, redesign, recolour, changed fabric, different colour, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, street scene, environmental scene, buildings, pedestrians, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 六、参数

| 项 | A | B | C |
|---|---|---|---|
| steps / cfg | 25/1.0 或 30/3.5（两种都出过合格图） | 25/1.0（负向无效仍出图） | **30/3.5**（cfg 1.0 内搭易丢） |
| sampler | euler / simple | euler / simple | euler / simple |
| denoise | 1.0 | 1.0 | 1.0 |
| 尺寸 | 跟随输入图，32 对齐 | 同 | 同 |
| 张数 | 2–3 张挑一张 | 2–3 张 | 2–3 张 |

## 七、取证

| 版本 | 图号 → 尺寸 | 词数 |
|---|---|---|
| A | 449/446/473/474 → 1216×1600 | 511（4 张同指纹 `e2284262dfa1`） |
| B | 453 → 1216×2112；454/455 → 1216×1600 | 547（3 张同指纹 `ca058df58e64`） |
| C | 470 → 608×608；472 → 1216×1600 | 745（2 张同指纹 `639013b3f3ee`） |

逐张元数据：`evidence/2026-10-19-ghost-ABC-baseline.md`
