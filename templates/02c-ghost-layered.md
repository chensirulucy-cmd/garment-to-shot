# 02c · 幽灵服装台 C 版（上身叠穿 2–3 层）

- 状态：✅ 已验证（2026-10-19，样本 `00470 / 00472`，745 词 + 负向 255 词，30 步 / cfg 3.5）
- ⛔ 早期版（660 词 / 负向 226 词，样本 `00466`）已被本版取代：**领口写成 `open empty neckline … nothing inside` 会把内搭整层抹掉**
- 适用：上身 2–3 层（衬衫+毛衣 / T恤+夹克 / 衬衫+连帽），下装 1 件
- 不适用：一件式（`02` A 版）、不叠穿的两件套（`02b` B 版）
- 参考图：1 张；正文与负向逐字取自 `Qwen_image_2.1_00472.png`

## 变量（换服装只改这几处）

| 变量 | 位置 | 换什么 |
|---|---|---|
| 输入图 | `<image1>` | 换任何「上身叠穿 + 一件下装 + 鞋」的照片，**提示词不动** |
| 层数 | 件数段 | 默认从图里数（2 或 3），无需手改；只有明确知道是 3 层时才写死 `three layers` |
| 鞋来源 | 鞋段 | 图里带鞋 → 照抄；图里没鞋 → 自动配一双中性款（同一段已覆盖） |
| 画幅 | `custom_size` | 关（跟随输入图）；要固定才改 9:16 |

**不改的**：去人清单、`Copy, do not redraw` 段、领口段（`the inner garment fills that opening`）、纯白底、去字段。

## 硬规则（违反必失败）

1. 正向**不能**出现 `empty neckline` / `nothing inside the garments` —— 这句会删掉内搭
2. 领口必须写成「外层的开口里由内搭填满」：`the inner garment fills that opening`
3. 参数必须 **30 步 / cfg 3.5**；cfg 1.0 时负向权重为 0
4. 送图前确认原图内搭**至少露出领口或一截袖口**，否则本版不适用

## 正向（逐字）

```
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet and no toes anywhere in the frame, and hold the garments with natural hollow volume as if worn by an invisible body — rounded shoulders, empty sleeve openings, an open empty hem, and no body inside them.

The outfit is layered on the upper body. Count the layers the photograph actually shows — two, or three if a third is visible — and keep exactly that many layers, each as its own separate hollow shell, worn in the same order as the photograph: the innermost piece closest in, each outer piece over it. The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth and the same shape as the photograph, its front closure stays pulled down to exactly the same point on the chest as the photograph, and the inner garment fills that opening — its collar rising above the outer edge by the same amount the photograph shows, its collar points lying open over the outer layer, its buttoned placket and its inner surface visible down inside the opening. The inner garment is the only thing inside the outer one, and no skin, no neck and no body appears in that opening. Where the photograph shows an inner cuff emerging beyond an outer sleeve end, keep it emerging by the same amount; where the photograph shows no inner cuff, the outer sleeve end finishes the arm cleanly. Never merge two layers into one garment, never drop a layer, never add a layer, never reverse the order, and never close an opening the photograph leaves open.

There is one lower garment, trousers or a skirt exactly as photographed, worn below the upper layers with its waistband sitting under the outer layer's hem, its own closure, pockets and hem unchanged, and its hem ending at the same point on the leg or the ankle as in the photograph.

Copy, do not redraw. Every garment must come out of the photograph unchanged, piece for piece and stitch for stitch: the same fabric, weave, knit or twill texture at the same scale, the same colour, the same print or pattern, the same collar shape, the same closures and hardware in the same places, the same cuffs, pockets and hems, the same cut and proportions, and the same shoes with the same sole, toe shape and material. Do not describe these garments from words, do not improve them, do not substitute a similar-looking piece and do not change any colour, fabric or pattern — a close lookalike is a failure, only the photographed garment is correct.

Handle the footwear as follows. If the photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height. If the photograph shows no shoes at all, add one single pair of plain, understated shoes that belongs with this outfit, in a neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment. Either way the shoes appear once, as one matched pair, placed side by side on the studio floor at the bottom of the frame beneath the hem, angled slightly outward, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain white seamless studio background, every piece complete inside the frame with generous margins around the collars, the cuffs, the waist, the hems and the shoes, all pieces hung in the order they are worn so every layer's edge remains visible, presented as a straight front view rather than a walking or seated pose. Remove any bag, tote, hat or accessory that the photograph shows, so the frame contains the garments and the shoes only.

Remove every brand text, logo, watermark, price tag and caption from the photograph, including any printed advertising text and brand marks, so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with the fabric texture, knit stitch, drape and seam detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 负向（逐字）

```
neckline closed that the photograph leaves open, zip pulled up to the collar, collar closed to the throat, missing inner collar, missing inner placket, the opening filled with skin, bare neck in the neckline, merged layers, fused into one garment, two layers joined into one, one piece split into two, missing layer, missing inner layer, missing inner cuffs, extra layer, invented layer, layer order reversed, the inner layer worn outside, the outer layer worn inside, single top layer, only the outer garment shown, only the inner garment shown, missing garment, extra garment, missing lower garment, skirt replaced by trousers, trousers replaced by a skirt, missing waistband, waistband hidden, redrawn garment, similar-looking substitute, different garment, restyled garment, simplified texture, invented knit pattern, changed closure, different collar shape, changed pocket placement, changed trouser cut, changed shoe design, different shoes than the photograph, mismatched pair, only one shoe, two different shoes, added belt, added scarf, added bag, handbag, tote, added accessories, walking pose, mid-stride, seated pose, motion blur, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, Chinese characters, price tag, embroidery, added pattern, added print, redesign, recolour, changed fabric, different colour, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, street scene, environmental scene, buildings, pedestrians, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 参数

| 项 | 值 |
|---|---|
| 采样 | 30 步 · cfg 3.5 · euler / simple · denoise 1.0 |
| 尺寸 | 跟随输入图（`custom_size` 关） |
| 张数 | 2–3 张挑一张 |

## 判据

1. 领口里是衣服不是空的（内搭领子/门襟可见，无脖子）
2. 拉链/开口停在原图位置，不被拉到顶
3. 两层有可见分界
4. 无人体、纯白底、鞋成对
