# ④ 四视图角色板：现行路线与证据边界

> **2026-10-21 当前生成入口**：[fourview-headless](../../fourview-headless/SKILL.md)。515按固定骨架填族槽；以下既有文字供历史与接线参考，不覆盖新入口的槽位范围和验证状态。

采用 478 服装板 → 515 一次生成完整四视图。永久排除分格生成后拼接。先读 [2026-10-19 证据复核](../../../evidence/four-view-2026-10-19/README.md)；该页纠正此前跨输出阶段比较、反引号因果、服装类别因果和尺寸随机等错误结论。

## 接线与尺寸

| 槽 | 实际职责 |
|---|---|
| image1 | 四格画布，身体姿势、位置、比例、肩臂手轮廓与第四格构图 |
| image2 | 人像身份与肤色；头肩特写不提供全身身高和手部证据 |
| image3 | 478 的服装板产出，不能把其上游 LoadImage 误写为直连 |

核对 515:511 的分支。所审 18 张角色板均 switch=false，latent 由 TextEncodeQwenImage21 的输出 2 提供；当前实现 resolution=0 时按第一参考图尺寸取整至 32 倍数。2075×1184 对应 2080×1184。不要用同一整图中另一个保存节点的尺寸来推断此分支随机换尺寸。

## 历史正向（00233 存档，本轮未重新验收该样本）

以下保留原文供历史回溯，不宣称其中每句适用于吊带裙；实际六个已核验成功样本原文在证据目录。

```text
Edit the four-figure sheet in <image1> into a finished character reference sheet: keep <image1> as the canvas, with its four-panel layout, the width and height of each panel, the camera height, the plain white background, the soft even studio light and the faint contact shadows under the shoes all exactly as they are, and change only the heads and the outfit. The leftmost panel is the full-length front view of the woman from <image2>, the second panel is the same woman seen from directly behind, and the third panel is the same woman in true side profile, each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it, and each keeping the stance, position and scale of the corresponding figure in <image1>; her body build, height, skin tone and hands come from <image2>. The fourth panel is a large frontal face-and-shoulders portrait of that same woman, filling its panel from just above the crown of her head down to the base of her neck so her face dominates the panel, framed and scaled exactly like the fourth figure of <image1>; her facial identity and hair are those shown in <image2> exactly as <image2> shows them, and this panel is the only one that contains a head or a face. In all four panels she wears one outfit taken from <image3>: a mid-grey ribbed knit long-sleeve cardigan with a pointed collar in brown, cream, black and white checks, five small round brown buttons down the centre front and turned-back tartan cuffs, closed over a mid-grey knife-pleated mini skirt that ends at mid-thigh, with black round-toe chunky-sole loafers on both feet. The two greys read clearly as mid-grey rather than black or white, the knit keeps its vertical rib and the collar checks stay legible in every panel, and the skirt keeps its sharp pleat shadows. Nothing else is added, removed, restyled or re-lit.
```

## 历史负向

```text
three identical front views, all three standing panels showing a front view, identical panels, missing back view, missing side view, all-black outfit, black cardigan, black skirt, knit rendered as flat black, collapsed garment detail, grey rendered as black, grey rendered as white, a head in the first three panels, a face in the first three panels, hair falling over the shoulders in the first three panels, head added above the shoulders, repaired crop, figure rescaled to fit the whole body, different person between panels, different face between panels, different hairstyle between panels, different outfit between panels, mixed outfits, wardrobe from <image2>, mannequin appearance, white mannequin material, featureless face, a second person, extra limbs, extra fingers, malformed hands, fused garments, warped buttons, distorted tartan, text, captions, labels, watermark, panel borders, comic panels, frame lines, low resolution, blurry, plastic skin, waxy skin, illustration, painting, anime, cartoon, CGI, 3D render
```

## 当前判据

前三格正/背/侧无头，同时肩部、手臂与手完整，衣服款式与件数不变，第四格身份正确，画布布局与比例保留。00426 没有头但也删除肩臂手，仍是失败。不能用像素顶部空白或文字相似度代替完整画面验收。

旧正向把前三格共用的无头句放在侧面后，并使用 collar closing the top edge；对无领吊带服装，服装领口与肩膀不是同一边界。这是待检验的提示词作用范围/身体保留问题，不是已查明的模型内部因果。允许在保留完整基线的前提下做单个描述块的措辞对照；没有证据支持禁止所有措辞实验。

00418 带 skin condition / expression 仍成功；00405→00406 去掉反引号仍失败。不能将这些词或格式作自动失败判据。00428 不支持将连身裙伪写成两件式。固定 seed 是控制条件，既不承诺跨环境必然像素相同，也不推荐多次抽样碰运气。

## 技术后备

若提示词不足，评估同一次采样中的保护遮罩。mask=0 保护原 latent，mask=1 允许生成；必须检查实际通道、原图尺寸和肩部边界。Muse JSON 缺 channel 与实际 mask，且编码路径尺寸不一致，当前不能作为已可运行方案。遮罩不等于拆图拼接，也不保证任何姿态下语义上的绝对无头。
