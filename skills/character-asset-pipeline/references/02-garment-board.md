# ② 服装板（多格 · 供角色表的 `<image3>`）

与①的区别：①是一张成品展示图；**②是一张多格「服装板」**，给角色表当服装来源（前后侧 + 细节格），所以它必须**多视角、单底色、颜色保真**。

## 变量

| 变量 | 取值 |
|---|---|
| 衣服 | `<image1>`（任意一版服装照） |
| 鞋 | 输入图自带 / 文字点名 / `<image2>` 鞋图（推荐） |
| 版式 | 三整装（正/背/侧）+ 一列细节格（固定，别写「flexible layout」） |

> ⚠️ **版式是「分解」这个动作的唯一载体**：正向里那段 `Use a multi-panel layout: one full-outfit front view, one full-outfit back view and one full-outfit side view … plus a column of zoomed detail tiles for …` **必须整段保留**。把它换成「竖排单品 + 少量细节格」＝服装不再分解（实测只得到一张平铺图）。注意区分：**「竖排单品」是 `01-garment-template.md`（单帧成品图）的布局，不是服装板的布局**。本模板为冻结原文，禁止改写。
| 底色 | **单一浅灰**（写死，否会出现右列黑底） |

## 正向

```
Use `<image1>` as the only outfit reference and `<image2>` as the only footwear reference.

Create a photorealistic wardrobe reference sheet that breaks down the outfit in `<image1>` together with the shoes in `<image2>`. Show attire only, not the person. No face, no skin, no visible body, no mannequin and no dress form of any kind — the garments hold their shape as ghost-mannequin volumes, hollow and empty, with an open empty neckline, empty sleeve openings and nothing inside them.

Extract and preserve from `<image1>`: every garment present, its silhouette and layering, its cut, its true colours, its fabric, weave and sheen, its print or pattern, its seams, stitching, buttons, zips, fastenings, belts, straps, pockets and hems, and its proportions — with the garment count exactly as `<image1>` shows it, so a single one-piece garment such as a dress stays one continuous piece with a single neckline and a single hem and is never divided at the waist or overlaid with a separate waistband, while a genuine separates outfit keeps exactly its own number of pieces.

Extract and preserve from `<image2>`: the exact pair of shoes, keeping their design, colour, material, toe shape, strap, heel or sole height and every surface detail, with nothing worn inside them.

If some parts are hidden, reconstruct them logically and consistently from the visible design: show the back of each garment, the underside of the hems, and both shoes of the pair as a complete matched set.

Use a multi-panel layout: one full-outfit front view, one full-outfit back view and one full-outfit side view — each with the pair of shoes from `<image2>` standing side by side at the bottom of the frame in the position feet would occupy, angled slightly outward — plus a column of zoomed detail tiles for the collar and neckline, the buttons and front edge, the cuffs, the fabric weave and texture, the waist and hem construction, and the shoes' toes, straps and soles.

Set the whole sheet on one single plain seamless light-grey studio backdrop held at one even value: the same backdrop behind the full-outfit views and behind every detail tile, with no darker, black, charcoal or gradient background anywhere in the frame.

Light every tile with the same neutral, bright studio light, evenly exposed, with soft shadows and accurate colour reproduction, so each garment keeps its true colour value and darker pieces never collapse toward black, while the weave, the folds and the leather grain stay clearly readable.

Style: professional costume department wardrobe board, clean layout, neutral studio background, realistic fabric, knit, leather and stitching, sharp detail, production-ready presentation.

Important: preserve the outfit and the shoes faithfully, do not redesign, recolour or divide them, do not turn it into a character sheet, do not show a human model or any mannequin, keep the result photorealistic and detailed, and carry no embroidery or lettering anywhere.
```

## 负向

```
missing footwear, bare feet, only one shoe, mismatched pair, two different shoes, wrong shoe design, changed shoe colour, invented shoes not in the reference, two-piece set, split into a top and a skirt, separated bodice and skirt, two garments where the image shows one, cut dress, dress divided at the waist, waist seam opened, skirt laid over the dress, extra garment, invented second garment, added belt, added bag, added jewellery, missing garment, missing piece, only the top shown, only the skirt shown, cropped hem, cropped sleeves, cropped shoes, human model, person, character, face, head, skin, visible body, hands, arms, legs, feet, mannequin, dress form, display figure, mannequin torso, mannequin stand, neck block, dark mannequin, black mannequin torso, brand text, logo, watermark, caption, lettering, embroidery, chest logo, add pattern, add print, redesign, recolour, simplified detail, changed fabric, different colour, grey rendered as black, black garment, fused garments, impossible folds, broken seams, warped buttons, melted fabric, plastic-looking fabric, fake texture, mixed backgrounds, a different background behind any tile, black background, dark backdrop, charcoal background, gradient background, vignette, dark floor, illustration, painting, anime, cartoon, CGI, obvious 3D render, busy background, environmental scene, harsh shadows, dramatic lighting, low resolution, blurry details, soft focus, noise, compression artifacts
```

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 右列细节格是黑底、左列白底 | 正向只写 `neutral studio background`（形容词不是数值），且版式写「flexible」 | 用本文的单底色段 + 固定版式段 |
| 长出黑色无头人台 | 只说 `no face, no skin, no visible body`，没禁人台 | 正向写 `no mannequin, no dress form …`；负向加 `mannequin, dress form, display figure, mannequin torso` |
| 只有正面、没有背/侧 | 负向里有 `back view` 这类词 | **删掉** `back view`；正向逐个点名 front / back / side |
| 品牌刺绣被带进下游 | 输入图左胸有小刺绣 | 正向 `no embroidery, no lettering`；负向 `embroidery, lettering, chest logo` |

## 变体：没有鞋图时（纯文字点名鞋）

把正向第一行改成 `Use \`<image1>\` as the only outfit reference.`（去掉 `<image2>`），并把「Extract and preserve from `<image2>`: …」那一段换成一句文字点名，例：

```
Extract and preserve the footwear: one matched pair of black round-toe chunky-sole penny loafers, keeping their strap, smooth leather uppers and thick black rubber soles exactly as described, with nothing worn inside them.
```

负向追加：`missing footwear, bare feet, only one shoe, mismatched pair`。

## 交付前核对

三整装是否齐（正/背/侧）、是否都是同一套衣服、颜色是否保住（灰没塔黑）、细节格里有没有出现人体或人台、品牌字是否清干净。
