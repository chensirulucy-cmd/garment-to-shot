# ④ 四视图角色版（正/背/侧全身无头 + 第 4 格大脸）

职责：把身份（人像图）与服装（服装板）**合成到固定版式**，产出可复用的标准表。

## 接线（三个图槽）

| 槽 | 图 | 作用 |
|---|---|---|
| `<image1>` | 四格白模 | **画布**：版式、姿势、取景、裁切高度、各格内人物的位置与尺度 |
| `<image2>` | 面部特写人像 | **身份**（脸/发/肤色/体格） |
| `<image3>` | 服装板 | **服装**（设计/颜色/材质/细节） |

`custom_size`：关（跟随 `<image1>` 的像素）或开（用 ResolutionSelector，建议 16:9 / 3.0 MP，四格横排每格才够像素）。

## 正向（一段到底 · 以动作开头 · 肯定陈述）

```
Edit the four-figure sheet in <image1> into a finished character reference sheet: keep <image1> as the canvas, with its four-panel layout, the width and height of each panel, the camera height, the plain white background, the soft even studio light and the faint contact shadows under the shoes all exactly as they are, and change only the heads and the outfit. The leftmost panel is the full-length front view of the woman from <image2>, the second panel is the same woman seen from directly behind, and the third panel is the same woman in true side profile, each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it, and each keeping the stance, position and scale of the corresponding figure in <image1>; her body build, height, skin tone and hands come from <image2>. The fourth panel is a large frontal face-and-shoulders portrait of that same woman, filling its panel from just above the crown of her head down to the base of her neck so her face dominates the panel, framed and scaled exactly like the fourth figure of <image1>; her facial identity and hair are those shown in <image2> exactly as <image2> shows them, and this panel is the only one that contains a head or a face. In all four panels she wears one outfit taken from <image3>: a mid-grey ribbed knit long-sleeve cardigan with a pointed collar in brown, cream, black and white checks, five small round brown buttons down the centre front and turned-back tartan cuffs, closed over a mid-grey knife-pleated mini skirt that ends at mid-thigh, with black round-toe chunky-sole loafers on both feet. The two greys read clearly as mid-grey rather than black or white, the knit keeps its vertical rib and the collar checks stay legible in every panel, and the skirt keeps its sharp pleat shadows. Nothing else is added, removed, restyled or re-lit.
```

> ⚠️ 本段是**冻结原文**，与已验证版本逐字一致。换服装时**只改**「服装名词段」（`a ⟨colour + fabric⟩ ⟨garment class⟩ … on both feet`）与紧跟其后的颜色保真句，**其余一个词都不动**——重写骨架句、把「保留画布、只换头和衣服」改成「替换所有人台」这类改写都会让效果回退（见 `05-derivation-rules.md` 的改动量上界）。

## 负向

```
three identical front views, all three standing panels showing a front view, identical panels, missing back view, missing side view, all-black outfit, black cardigan, black skirt, knit rendered as flat black, collapsed garment detail, grey rendered as black, grey rendered as white, a head in the first three panels, a face in the first three panels, hair falling over the shoulders in the first three panels, head added above the shoulders, repaired crop, figure rescaled to fit the whole body, different person between panels, different face between panels, different hairstyle between panels, different outfit between panels, mixed outfits, wardrobe from <image2>, mannequin appearance, white mannequin material, featureless face, a second person, extra limbs, extra fingers, malformed hands, fused garments, warped buttons, distorted tartan, text, captions, labels, watermark, panel borders, comic panels, frame lines, low resolution, blurry, plastic skin, waxy skin, illustration, painting, anime, cartoon, CGI, 3D render
```

## 为什么站立格要「无头」

同一张脸在四格里出现四次，模型会把它当四个不同的人分别重画 → 必然漂。所以：前三格**只出身体**（画框上缘切在领口/肩线），头发也必须在格外出镜（长发角色尤其要写这一句）；**全表只允许第 4 格有一张脸**。

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 前三格长出人头 | 正向没点名「无头」，或负向里写了 `four panels` / `cropped full body`（与正向要求矛盾） | 正向逐个写 `headless`/`no head above the collar`；**负向删除** `four panels`、`cropped full body` |
| 三格全是正面 | 只在总括句里说「保留姿势」，或负向里含 `back view` | 正向逐格点名 front / back / true side profile |
| 全套变黑 | 没点颜色；`<image3>` 里颜色就没保住；1 MP 四格分摊像素不足 | 正向点名颜色；先把服装板颜色修对；提到 3.0 MP |
| 第 4 格脸太小 | 取景写到胸口/上胸 | 改「从头顶到颈根，脸占满该格」 |
| 四格之间不是同一个人 | 组③ 里同时插了 LoRA（身份双源互拉） | **组③ 不插 LoRA**，身份只走 `<image2>` |


---

## 从 00307 / 00308 / 00321 元数据补齐的五条（原文级）

1. **颜色锚定句（原文件缺）**：每个色区写两句 ——「读作什么」+「永不变成什么」，并同步写进负向。
   例：`The black knit reads as black with its fine vertical rib visible and never a flat crushed silhouette`；`the cream skirt stays clearly lighter than the knit and never turns white or yellow`；`the belt stays black leather and distinct from the knit, the buckle stays small bright gold-tone metal, the pumps stay nude`。
2. **颜色漂移专项负向**：`the black knit rendered dark grey / washed out / flat black`；`the cream skirt rendered white / yellow / black`；`missing belt, missing buckle`。
3. **品类锁负向**（睡衣套实例）：`a robe, a nightgown, a dress, a jumpsuit, the trousers replaced by a skirt, closed shoes, slippers with socks, bare feet` —— 品类漂是四视图最高频的错。
4. **面板纪律负向**：`three identical front views, identical panels, missing back view, missing side view, a head / face / hair in the first three panels, head added above the shoulders, different person / different face / different outfit between panels, wardrobe from <image2>, panel borders, comic panels, frame lines`。
5. 参数实测：`16:9 · 2.0 MP · steps 30 · cfg 3.5 · euler / simple`；三参考固定为 `<image1>` 四格人台底版（版式/白底/光/影子全保）＋ `<image2>` 身份（脸+身材+手）＋ `<image3>` 服装。
