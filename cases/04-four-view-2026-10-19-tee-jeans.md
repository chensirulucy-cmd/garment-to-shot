# 案例 · 角色四视图：白长袖 + 浅蓝牛仔 + 小白鞋（2026-10-19 已验证）

> **状态**：✅ 已验证 —— 00418 三格无头；“首次即成功”不由单张 PNG 独立证明
> **产出**：`F:\ComfyUI-Data\output\Qwen_image_2.1_00418.png`（2080×1184）
> **模板**：`templates/04-character-sheet.md`
> **入参**：`<image1>` 四格无头画布 · `<image2>` 清透白底东方面容肖像 · `<image3>` 478 服装板产出（其服装源图为 00396 白长袖+浅蓝牛仔+小白鞋幽灵台）

## 一、参数（元数据实读）

| 项 | 值 |
|---|---|
| 尺寸 | 2080×1184（16:9 · 2 MP · multiple 32） |
| 采样 | steps 30 · cfg 3.5 · euler / simple · denoise 1.0 |
| seed | 494 = `810701216055607`（服装板）／518 = `744522349844629`（角色板） |
| 正向 | 385 词 |
| 负向 | 204 词 |

## 二、正向（逐字，即 00418 的存档原文）

```text
Edit the four-figure sheet in <image1> into a finished character reference sheet: keep <image1> as the canvas, with its four-panel layout, the width and height of each panel, the camera height, the plain white background, the soft even studio light and the faint contact shadows under the shoes all exactly as they are, and change only the heads and the outfit. The leftmost panel is the full-length front view of the woman from <image2>, the second panel is the same woman seen from directly behind, and the third panel is the same woman in true side profile, each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it, and each keeping the stance, position and scale of the corresponding figure in <image1>; her body build, height, skin tone and hands come from <image2>. The fourth panel is a large frontal face-and-shoulders portrait of that same woman, filling its panel from just above the crown of her head down to the base of her neck so her face dominates the panel, framed and scaled exactly like the fourth figure of <image1>; her facial identity, her skin condition, her expression and her hair are those shown in <image2> exactly as <image2> shows them, with nothing added and nothing restyled, and this panel is the only one that contains a head or a face. In all four panels she wears one outfit taken from <image3>: a white long-sleeve cotton crewneck shirt with a narrow ribbed neckband, plain turned cuffs at the wrists and a straight hem at the hip, tucked into a pair of light-blue straight-leg jeans with a high waistband, a front fly, two front pockets and a straight leg ending at the ankle, with a pair of white low-top canvas sneakers on both feet, each with white laces and a pale rubber sole. The shirt reads as a clean warm white and never turns grey, cream or yellow; the denim reads as a light washed blue with its twill grain and its topstitching visible and never turns dark indigo, grey or black; the sneakers stay clean white with white laces and never turn grey or cream. Nothing else is added, removed, restyled or re-lit.

```

## 三、负向（逐字）

```text
three identical front views, all three standing panels showing a front view, identical panels, missing back view, missing side view, the shirt rendered grey, the shirt rendered cream, the shirt rendered yellow, the shirt rendered blue, the denim rendered black, the denim rendered dark indigo, the denim rendered grey, the denim rendered white, missing fly, missing front pockets, the jeans replaced by a skirt, the jeans replaced by trousers, the shirt replaced by a dress, the shirt replaced by a blouse, the sneakers rendered grey, the sneakers rendered cream, closed leather shoes, heels, boots, bare feet, a head in the first three panels, a face in the first three panels, hair falling over the shoulders in the first three panels, head added above the shoulders, repaired crop, figure rescaled to fit the whole body, different person between panels, different face between panels, different hairstyle between panels, different outfit between panels, mixed outfits, wardrobe from <image2>, mannequin appearance, white mannequin material, featureless face, a second person, extra limbs, extra fingers, malformed hands, fused garments, added belt, added belt loops, added jacket, text, captions, labels, watermark, panel borders, comic panels, frame lines, low resolution, blurry, plastic skin, waxy skin, illustration, painting, anime, cartoon, CGI, 3D render



```

## 四、关键对照及结论边界

00418 是有效成功样本，其正负向原文保留。它与 00408 说明同一人像参考能生成成功角色板；含 skin condition / expression 并不必然冒头。它不能单独证明两件式是成功原因。

六个成功样本为 00264、00308、00321、00325、00408、00418。00307 和 00402 是服装板，不计入无头角色板结果。00403、00405、00406、00410 的第三侧面无头而正背面有头，不能写成三格全冒头。

00408→00410 同时改变两支正负向和服装源图（含内容哈希），不构成衣服类型的单变量实验。00410→00411 只换画布，第三侧面由无头变成冒头，画布也是实际可影响结果的输入。详见 [证据与历史线](../evidence/four-view-2026-10-19/README.md)。

保留一次整图生成，不推荐拼接、把裙子改写成两件式或反复改 seed 挑图。候选必须标待实测，不能覆盖本成功记录。
