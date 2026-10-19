# 02c · 幽灵服装台 C 版（上身叠穿 2–3 层）

> **状态**：✅ 已验证 —— 样本 `00470 / 00472`，正向 745 词 + 负向 255 词，2 张的正负向全文指纹一致（`639013b3f3ee` / `8e47d13d27d7`）
> **线**：Qwen-Image 2.1 **编辑线**（`LoadImage` → `TextEncodeQwenImage21.images.image_1` → `ComfySwitchNode(switch=False)` → `KSampler`）
> **尺寸**：跟随输入图按 32 对齐；`ResolutionSelector` 被旁路，调它无效
> **逐字原文**：`prompts/02-ghost-set/C-00472-positive.txt` / `C-00472-negative.txt`

## 一、适用 / 不适用

| | |
|---|---|
| ✅ 适用 | 上身 **2–3 层**（衬衫+毛衣 / T恤+夹克 / 衬衫+连帽），下装一件 |
| ⛔ 不适用 | 一件式 → `02a`；不叠穿的两件套 → `02b`；原图内搭完全被包住（看不见领口/袖口）→ 本版不适用 |

## 二、变量（换服装只改这几处）

| 变量 | 改哪里 | 填什么 | 不填会怎样 |
|---|---|---|---|
| 层数 | 正向第 2 段 | 从原图数（2 或 3） | 层数写错 → 少一层或多一层 |
| 内层露出量 | 正向第 2 段 | 领口 / 领口+袖口，按原图 | 露太多 → 像穿了别人的衬衫；露太少 → 内层消失 |
| 下装 | 正向第 3 段 | trousers / a skirt | 写错 → 裤变裙 |
| 底色 | 正向第 5 段 | white / light-grey | 按出图要求 |
| 参数 | 六、参数 | **必须 30 步 / cfg 3.5** | cfg 1.0 → 负向失效 → 内搭易丢、拉链被拉满 |

## 三、标准模式（成品 · 逐字 · 直接粘贴）

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet and no toes anywhere in the frame, and hold the garments with natural hollow volume as if worn by an invisible body — rounded shoulders, empty sleeve openings, an open empty hem, and no body inside them.

The outfit is layered on the upper body. Count the layers the photograph actually shows — two, or three if a third is visible — and keep exactly that many layers, each as its own separate hollow shell, worn in the same order as the photograph: the innermost piece closest in, each outer piece over it. The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth and the same shape as the photograph, its front closure stays pulled down to exactly the same point on the chest as the photograph, and the inner garment fills that opening — its collar rising above the outer edge by the same amount the photograph shows, its collar points lying open over the outer layer, its buttoned placket and its inner surface visible down inside the opening. The inner garment is the only thing inside the outer one, and no skin, no neck and no body appears in that opening. Where the photograph shows an inner cuff emerging beyond an outer sleeve end, keep it emerging by the same amount; where the photograph shows no inner cuff, the outer sleeve end finishes the arm cleanly. Never merge two layers into one garment, never drop a layer, never add a layer, never reverse the order, and never close an opening the photograph leaves open.

There is one lower garment, trousers or a skirt exactly as photographed, worn below the upper layers with its waistband sitting under the outer layer's hem, its own closure, pockets and hem unchanged, and its hem ending at the same point on the leg or the ankle as in the photograph.

Copy, do not redraw. Every garment must come out of the photograph unchanged, piece for piece and stitch for stitch: the same fabric, weave, knit or twill texture at the same scale, the same colour, the same print or pattern, the same collar shape, the same closures and hardware in the same places, the same cuffs, pockets and hems, the same cut and proportions, and the same shoes with the same sole, toe shape and material. Do not describe these garments from words, do not improve them, do not substitute a similar-looking piece and do not change any colour, fabric or pattern — a close lookalike is a failure, only the photographed garment is correct.

Handle the footwear as follows. If the photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height. If the photograph shows no shoes at all, add one single pair of plain, understated shoes that belongs with this outfit, in a neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment. Either way the shoes appear once, as one matched pair, placed side by side on the studio floor at the bottom of the frame beneath the hem, angled slightly outward, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the collars, the cuffs, the waist, the hems and the shoes, all pieces hung in the order they are worn so every layer's edge remains visible, presented as a straight front view rather than a walking or seated pose. Remove any bag, tote, hat or accessory that the photograph shows, so the frame contains the garments and the shoes only.

Remove every brand text, logo, watermark, price tag and caption from the photograph, including any printed advertising text and brand marks, so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with the fabric texture, knit stitch, drape and seam detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 四、骨架版（同一份词，把可变量拆成槽位）

骨架 = 成品同一份词，只把 4 处可变量换成 `{{…}}`；`the inner garment fills that opening` 这句是 C 版的命门，**不许改成 `nothing inside`**。

```text
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet and no toes anywhere in the frame, and hold the garments with natural hollow volume as if worn by an invisible body — rounded shoulders, empty sleeve openings, an open empty hem, and no body inside them.

The outfit is layered on the upper body. Count the layers the photograph actually shows — {{层数：two ／ two, or three if a third is visible}} — and keep exactly that many layers, each as its own separate hollow shell, worn in the same order as the photograph: the innermost piece closest in, each outer piece over it. The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth and the same shape as the photograph, its front closure stays pulled down to exactly the same point on the chest as the photograph, and the inner garment fills that opening — {{内层露出量：its collar rising above the outer edge by the same amount the photograph shows ／ its collar and both cuffs emerging by the same amount the photograph shows}}, its collar points lying open over the outer layer, its buttoned placket and its inner surface visible down inside the opening. The inner garment is the only thing inside the outer one, and no skin, no neck and no body appears in that opening. Where the photograph shows an inner cuff emerging beyond an outer sleeve end, keep it emerging by the same amount; where the photograph shows no inner cuff, the outer sleeve end finishes the arm cleanly. Never merge two layers into one garment, never drop a layer, never add a layer, never reverse the order, and never close an opening the photograph leaves open.

There is one lower garment, {{下装：trousers ／ a skirt}} exactly as photographed, worn below the upper layers with its waistband sitting under the outer layer's hem, its own closure, pockets and hem unchanged, and its hem ending at the same point on the leg or the ankle as in the photograph.

Copy, do not redraw. Every garment must come out of the photograph unchanged, piece for piece and stitch for stitch: the same fabric, weave, knit or twill texture at the same scale, the same colour, the same print or pattern, the same collar shape, the same closures and hardware in the same places, the same cuffs, pockets and hems, the same cut and proportions, and the same shoes with the same sole, toe shape and material. Do not describe these garments from words, do not improve them, do not substitute a similar-looking piece and do not change any colour, fabric or pattern — a close lookalike is a failure, only the photographed garment is correct.

Handle the footwear as follows. If the photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height. If the photograph shows no shoes at all, add one single pair of plain, understated shoes that belongs with this outfit, in a neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment. Either way the shoes appear once, as one matched pair, placed side by side on the studio floor at the bottom of the frame beneath the hem, angled slightly outward, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain {{底色：white ／ light-grey}} seamless studio background, every piece complete inside the frame with generous margins around the collars, the cuffs, the waist, the hems and the shoes, all pieces hung in the order they are worn so every layer's edge remains visible, presented as a straight front view rather than a walking or seated pose. Remove any bag, tote, hat or accessory that the photograph shows, so the frame contains the garments and the shoes only.

Remove every brand text, logo, watermark, price tag and caption from the photograph, including any printed advertising text and brand marks, so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with the fabric texture, knit stitch, drape and seam detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

### 槽位怎么填

| 槽位 | 可填值 | 何时用 |
|---|---|---|
| `层数` | `two` ／ `two, or three if a third is visible` | 按原图 |
| `内层露出量` | `its collar rising above the outer edge…` ／ `its collar and both cuffs emerging…` | 看原图露出部位 |
| `下装` | `trousers` ／ `a skirt` | 按原图 |
| `底色` | `white` ／ `light-grey` | 按出图要求 |

## 五、负向（逐字）

```text
neckline closed that the photograph leaves open, zip pulled up to the collar, collar closed to the throat, missing inner collar, missing inner placket, the opening filled with skin, bare neck in the neckline, merged layers, fused into one garment, two layers joined into one, one piece split into two, missing layer, missing inner layer, missing inner cuffs, extra layer, invented layer, layer order reversed, the inner layer worn outside, the outer layer worn inside, single top layer, only the outer garment shown, only the inner garment shown, missing garment, extra garment, missing lower garment, skirt replaced by trousers, trousers replaced by a skirt, missing waistband, waistband hidden, redrawn garment, similar-looking substitute, different garment, restyled garment, simplified texture, invented knit pattern, changed closure, different collar shape, changed pocket placement, changed trouser cut, changed shoe design, different shoes than the photograph, mismatched pair, only one shoe, two different shoes, added belt, added scarf, added bag, handbag, tote, added accessories, walking pose, mid-stride, seated pose, motion blur, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, Chinese characters, price tag, embroidery, added pattern, added print, redesign, recolour, changed fabric, different colour, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, street scene, environmental scene, buildings, pedestrians, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 六、参数

| 项 | 值 |
|---|---|
| 采样 | **30 步 · cfg 3.5** · euler / simple · denoise 1.0（cfg 1.0 → 负向权重 0，内搭易丢） |
| 尺寸 | 跟随输入图，按 32 对齐（614×612 → 608×608） |
| 张数 | 2–3 张挑一张 |

## 七、判据（发出前自查）

1. 领口里是衣服不是空的（内层领子/门襟可见，没有脖子）
2. 拉链/开口停在原图位置，不被拉到顶
3. 两层有可见分界
4. 没有人、没有皮肤
5. 背景是要求的底色

## 八、取证

| 图 | 输入尺寸 | 输出尺寸 | steps/cfg | seed |
|---|---|---|---|---|
| 470 | 614×612 | 608×608 | 30/3.5 | 1082559298008331 |
| 472 | 1200×1600 | 1216×1600 | 30/3.5 | 753944227189969 |

2/2 正负向全文 sha256 相同。逐张见 `evidence/2026-10-19-ghost-ABC-baseline.md`
