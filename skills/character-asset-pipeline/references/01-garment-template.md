# ① 服装模板（单张 · 幽灵人台成品展示图）

用途：把**任意一张服装照/上身照**变成干净的「隐形人台」单品展示图。变量只有两个：**鞋从哪来**、**件数**。

## 变量

| 变量 | 取值 | 影响 |
|---|---|---|
| 鞋的来源 | ① 输入图自带 ② 无鞋时自动配一双 ③ 第二张参考图 `<image2>` | 决定结尾那段怎么写 |
| 件数 | 由输入图决定 | 一件套（连衣裙）**不能**被切成两件 |
| 画幅 | 跟第 1 张输入图（`custom_size=false`） | 竖版服装照 → 竖版出图 |

## 正向（通用版 · 无鞋时自动配一双，最常用）

> **格式说明**：官方编辑规则建议「单段、无换行」；本模板保留的是原工作流的分段形式（实测可用）。若要严格按规则，把空行删掉合成一段即可，字句不用动。

```
Edit the referenced outfit photograph into a single-frame ghost-mannequin outfit display in the look of a clean commercial studio garment shot: remove the person completely, with no head, no face, no skin, no arms, no hands, no legs, no feet, no toes and no body anywhere in the frame, and hold the exact garments from the image with natural hollow volume as if worn by an invisible body — rounded shoulders, an open empty neckline showing the inner back fabric, empty sleeve openings, an open empty hem, and nothing inside the garments.

Keep the garment count exactly as the outfit photograph shows it. If it shows a single one-piece garment such as a dress, keep it as one continuous garment: one neckline, one shoulder line, one continuous front and back panel running from the shoulders down to the hem, and the waist staying a construction line of that same garment with no horizontal break, no overlap and no separate waistband laid over it. If it shows separate garments, keep exactly that number of separate pieces and no more.

Preserve from the outfit photograph exactly each garment's design, cut, silhouette, garment count, colour, fabric, weave, sheen, print, pattern, knit or twill texture, seams, stitching, number and position of buttons, zips, fastenings, belts, straps, buckles, pockets and hems, and do not redesign, simplify, recolour, replace, add or divide any garment.

Handle the footwear as follows. If the outfit photograph shows shoes, keep exactly that pair, unchanged in design, colour, material, toe shape, heel or sole height and detail. If the outfit photograph shows no shoes at all, add one single pair of simple, understated shoes that clearly belongs with this outfit — a plain closed or low-cut style in a dark neutral tone taken from the outfit's own palette, with a moderate heel or a flat sole, no platform, no logo and no embellishment — and place that pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward. Either way the shoes appear once, as one matched pair, with nothing worn inside them and a soft contact shadow under them.

Arrange everything in one vertical composition on a plain light-grey seamless studio background, every piece complete inside the frame with generous margins around the collar, the sleeves, the waist, the hems and the shoes. Where the outfit photograph shows separate garments, stack them in the order they are worn so the upper piece's hem falls naturally over the lower piece's waistband; where it shows a single dress, present that dress whole, hanging with its own natural drape and its hem fully inside the frame above the shoes.

Remove every brand text, logo, watermark and caption that appears in the image so the finished frame carries no lettering anywhere. Light it with soft even studio light from the front upper left, gentle natural shadow, neutral white balance and accurate colour reproduction, with fabric weave, drape and stitch detail sharp and clearly readable, in a photorealistic commercial garment display with a clean presentation.
```

## 负向（通用版）

```
two-piece set, split into a top and a skirt, separated bodice and skirt, two garments where the image shows one, cut dress, dress divided at the waist, waist seam opened, skirt laid over the dress, extra garment, invented second garment, mismatched pair, only one shoe, two different shoes, clashing shoe style, platform shoes, chunky boots, sneakers with a formal outfit, sandals with a formal outfit, socks, logos on the shoes, embellished shoes, added accessories, added belt, added handbag, missing garment, missing piece, only the top shown, only the skirt shown, cropped hem, cropped sleeves, cropped shoes, human model, person, mannequin, dress form, display figure, mannequin torso, head, face, skin, arms, hands, legs, feet, toes, body, exposed flesh, brand text, logo, watermark, caption, lettering, embroidery, added pattern, added print, redesign, recolour, simplified detail, changed fabric, different colour, merged garments, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, excessive wrinkles, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, dark background, charcoal background, gradient background, vignette, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 变体：鞋来自第二张参考图 `<image2>`（零维护，长期推荐）

接线：`LoadImage(鞋的单品图) → 模块 image_2`。把正向里从 `Handle the footwear as follows.` 起那一段整段换成：

```
Add the footwear from <image2>: take the exact pair of shoes shown in <image2> and keep their design, colour, material, toe shape, strap, heel or sole height and every surface detail, then stand the pair side by side at the bottom of the frame in the position feet would occupy beneath the hem, angled slightly outward with a soft contact shadow under them. The shoes appear once, as one matched pair, with nothing worn inside them.
```

负向在通用负向基础上保留 `mismatched pair, only one shoe, two different shoes, clashing shoe style`，并追加 `missing footwear, bare feet, wrong shoe design, changed shoe colour, invented shoes not in the reference`。

## 验收（逐项看）

1. 件数对不对（连衣裙没被拦腰切开）；2. 有没有长出手/头/皮肤；3. 下摆、袖口有没有被裁；4. 鞋是否成对、是否搭调（不要尖头细跟配运动装）；5. 品牌文字是否清掉；6. 背景是否单一浅灰、没有格线或黑底。

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 连衣裙被切成上衣+裙子 | 旧版正向写了「top garment above / bottom garment below / 上衣下摆压住裙腰」——**这句假定两件套** | 用本文的「件数保持」段 |
| 凭空长出一双鞋 / 尖头细跟配休闲装 | 旧版正向写了「the pair of shoes standing side by side」——**这句假定有鞋** | 用「有则照抄，无则配一双中性款」段或鞋图变体 |
| 灰衣服出成黑色 | 没点颜色 + 输入底色偏深（实测亮度 87）+ 输出像素不足 | 正向点名 `mid-grey`，写「不是黑也不是白」 |
| 输出跟着输入图变成奇怪比例 | `custom_size=false` 时尺寸跟第 1 张输入图 | 确认第 1 张的比例，或开 `custom_size` |


---

## 实测参数与一个致命细节（来自 00235 / 00241 的 PNG 内嵌元数据）

- 实际运行：`steps 25 · cfg 1.0 · euler / simple · denoise 1.0` · `9:16 / 1.0 MP` · 参考图 1 张（原服装照）。
- **cfg = 1.0 时负向权重为 0**：00241 那段 1355 字符的负向（`two-piece set / split into a top and a skirt / only one shoe / two different shoes …`）**完全没有生效** —— 防拆件、防补鞋全靠正向句在扛。
- 推论（C 级）：要负向兜底就必须把 cfg 提到 >1（会拉紧色彩风格，需重调）；否则别在负向上花字数，把约束都写成正向句。
- 正向里真正起作用的四段（A2 结构，可直接复用）：①**去人清单**（head/face/skin/arms/hands/legs/feet/toes/body）②**件数锁**（单件连衣裙：一个领口、一条肩线、连续前后片、腰线只是构造线，无横向断裂、无独立腰头压在裙上；分开就保持原数量）③**保真清单**（末尾必须有 `add or divide` 的反向约束）④**鞋的两支**（有鞋原样；无鞋→补一双朴素深中性、取自本套自身色板、无 logo 无装饰，一双并排、朝外八、带接触阴影）。
