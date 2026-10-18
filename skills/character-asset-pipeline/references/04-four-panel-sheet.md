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

> ⚠️ **基准指纹（可复算）**：上面这段正向 = `Qwen_image_2.1_00233.png` 内嵌 `prompt` chunk 的原文，**334 词 / 1922 字符，归一化后逐字相同（相似度 1.000）**，出图 2080×1184（16:9 / 2 MP / steps 30 / cfg 3.5 / euler-simple）。
> 同一段文本还跑过两张不同尺寸：`00231`（1216×1600）、`00232`（1440×1440）—— 同提示词三尺寸，说明**尺寸控件状态不落盘，每次跑完必须核对保存节点**。
> 变体（**不是**本页基准，别拿来复算）：`00307 = 00308`（367 词，黑针织 + 奶油 A 字裙，与本段相似度 0.682）｜`00320/00321/00324/00325`（2181 字符，香槟缎面睡衣，0.669）。
>
> 换服装时**只改**「服装名词段」（`a ⟨colour + fabric⟩ ⟨garment class⟩ …`）与紧跟其后的颜色保真句，**其余一个词都不动**——重写骨架句、把「保留画布、只换头和衣服」改成「替换所有人台」这类改写都会让效果回退（改动量上界见 `05-derivation-rules.md`）。
>
> 真要复算就取产出 PNG 内嵌的 `prompt` chunk（`scripts/check_output_meta.py`），再用 `scripts/verify_prompt_drift.py` 做三重校验（相似度 / 槽外逐字相同 / 无被 markdown 包住的 token）。**比对前先确认比对的是同一套服装的产出**：拿 367 词的黑针织去比 334 词的格纹卡迪根，必然得到 0.7 左右的假低分，进而把真基准误判成「无产出背书」。

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
| 前三格长出人头（画布本身无头、服装板里也没人、参数一致） | 服装名词段把「人」带出来了：带身体动词（`tee-dress` / `falls from the shoulders` / `wraps around the body`）或否定式（`no waist seam` / `no belt` → 会被画出来） | 改成纯单品描述：`a straight cut from the neckline to a plain turned hem`，通篇肯定句、不出现 body / shoulder / falls。**这不是充分条件** —— 清干净后仍会冒头（`00410` 实测），真因至今未定，见文末「排查状态」 |
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

---

## 冒头复现证据（同工作流同参数，唯一变量是服装段）

先做**节点级 diff**：`00408`（成功）与 `00410`（失败）27 个节点全同，画布 / 人像 / seed 链 / steps / cfg / resolution 全同，唯一差别是 `480 LoadImage`（`00235` 1216×1600 黑针织 vs `00401` 768×1376 圆领裙）—— 变量确实在 `image3`，但**不是「衣服好不好看」，是「领口落在裁切线的哪个位置」**。

> 用户贴截图问「这张为什么长这样」时，先反查它是哪一号产出再谈因果：`scripts/find_output_by_screenshot.py <图片> <输出目录>` —— aHash 找到对应 PNG，然后把那次的 prompt / negative / 槽位 / 采样参数一次打全。

五张产出，**无头句逐字相同**（`each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it`），画布 / 人像 / 画幅 / seed / steps / cfg 全同：

| 产出 | 服装段关键措辞 | 词数 | 结果 |
|---|---|---|---|
| `00307` / `00308` / `00408` | `a black fine-rib knit … V-neck top … tucked into a cream A-line skirt`（无 body 词） | 367 | ✅ 三格无头 |
| `00405` / `00406` | `a relaxed straight **body that falls from the shoulders** …` | 357 | ❌ 三格冒头 |
| `00403` | `a relaxed straight **body** with **no waist seam, no drawstring and no belt**` | 386 | ❌ 三格冒头 |
| `00410` | **清版**：`a cream short-sleeve T-shirt dress … a straight cut from the neckline widening into a gentle A-line`（无 body 词、无否定式） | 383 | ❌ 三格冒头 |

### 决定性证据（先看这条）：**同输入复跑结果不同 → 这条线不可复现**

`00402` 与 `00403` 是同一份输入：正向 **386 词逐字相同（相似度 1.0000，完全一致 True）**、seed 同值（`494 = 810701216055607` / `518 = 744522349844629`）、三槽接同一批文件、**27 个节点逐字段比对差异 0**。结果：`00402` 三格无头、`00403` 三格冒头（裁图后视觉确认）。

结论：**单次对照在这条线上没有证据力** —— “换了服装图 / 领型 / 脸词 / 反引号 / body 动词 就好了或坏了”都不能由一次跑得出；同一提示词也能一次成、一次不成。

操作规则（当下唯一稳定用法）：
1. **同 seed 跑 3 张，只留三格顶边是干净裁切线的那张**，不是凑合，是这条线目前的正确用法。
2. 把两个采样器前各挂的 `QwenImage21Cache` **bypass 或删掉**，用同一 seed 复跑两次 —— 两次一致才算找到确定性来源。
3. **跑前清一次缓存**：478（服装板）与 515（角色板）共用同一个 UNet/CLIP 实例，上一段采样的残留会带进下一段。

### 被这条推翻的旧结论（留着只为别再走回头路）

`00410` 用的是清干净的服装段（无 `body`、无否定式），画布/人像/参数全同，仍然冒头 —— 所以 body 词只是次因。按领型分组，规律是确定的：

| 服装形态 | 产出 | 结果 |
|---|---|---|
| **两件式**（上衣止于腰 + 独立下装） | `00307/00308/00408`（V 领针织 + A 字裙）｜`00321/00325`（睡衣上衣 + 长裤）｜`00418`（**圆领**长袖 + 浅蓝直筒牛仔 + 小白鞋） | ✅ 全部无头；`00418` **首次即中** |
| **一件式连身**（领口到裙摆一整片） | `00402/00403/00405/00406/00410/00411/00416` | ⚠️ 7 跑 1 中（仅 `00402`） |

**判定的变量是「件数/形态」，不是「领型」**：`00408` 是 V 领、`00418` 是**圆领**，两个都出无头 —— 早期「有领才能无头 / 圆领必冒头」的推断被这两条推翻；骨架句里的 `with the collar of the garment closing the top edge` 不是必要条件。

**操作规则**：两件式按本页骨架直接跑；一件式连身**同 seed 跑 3–5 张挑一张**（不要动提示词），或把它改写成「同色上衣 + 同色下装」两件式描述再跑。

已排除的变量（同工作流、逐节点 differ 过）：

| 变量 | 排除依据 |
|---|---|
| 画布 | `four-view-shoulder-cut-no-neck.png` 与另做的 `four-view-shoulder-top-enlarged.png` **两张都冒头** |
| 人像 | 同一张 `清透白底东方面容肖像.png` 在 `00408` 成功、在 `00410/00411` 失败 |
| 提示词控制句 | 两份 8 句里前 3 句（含全部无头规则）**逐字相同**，只差 `skin condition, expression` 六个词 |
| 参数 / 节点图 | 27 节点全同；steps 30 / cfg 3.5 / euler-simple / resolution 0 / seed 链一致 |
| 服装段措辞（body 动词 / 否定式） | 清干净的 `00410` 仍然冒头 |

剩下唯一不变的共同项：**`<image3>` 服装参考图本身**。

| | 失败侧（`00403/405/406/410/411`） | 成功侧（`00307/308/408`） |
|---|---|---|
| 参考图尺寸 | 768×1376（**1.06 MP**） | 1216×1600（**1.95 MP**） |
| 宽高比 | **0.558**（与站立人形同比例） | **0.760** |
| 形态 | 连身裙（领口到裙摆一整片） | 两件式（上衣止于腰 + 半裙） |

候选解释（**未验证**）：`TextEncodeQwenImage21` 的 `resolution=0` 按参考图自身比例切 token，0.558 的竖长条更容易被读成「站立人形」而非「一件衣服」，于是无头格被补出人。

### 两条判决实验（各一次跑，只改一个槽）

1. **形状隔离**：把失败那张服装板原样铺到 1216×1600（衣服不动、补背景到 0.76），其余全不动 —— 不冒头即锁定「参考图的形状/像素」。
2. **呈现方式隔离**：同一件衣服换成两件式参考（上衣 + 下装各一张）—— 不冒头即锁定「连身 vs 分件」。

两条都失败，再查 token 绑定（`<imageN>` 是否被反引号包住）与服装板生成链。**每次只改一个槽，否则又多两个变量。**

### 候选修法（均未证实，按成本排）

1. **换掉那句骨架**（零成本先试）：把
   `each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it`
   换成
   `each of the three standing figures cut clean across the top edge of its panel exactly at the garment's neckline, so the neckline itself forms the top edge of the picture, with nothing above it — no neck, no chin, no head, no face and no hair`
2. **负向追加**：`neck, throat, chin, jawline above the collar, shoulders rising to the ears, neckline with a neck inside it, turtleneck, mock neck, collar band standing up`
3. **换画布（圆领的正解）**：现有 `four-view-shoulder-cut-no-neck.png` 是齐肩裁切，裁切线正好压在圆领开口上 → 模型必须补脖子。要的是**裁切线更低**（不是更高）：前三格从顶部再裁 ~17%，把裁切线推到胸口上方、**领口整个不入画**，再拉回原尺寸；第四格脸位原样拷贝。产出仍 2075×1184，工作流只换 `image1` 文件。逐格配方：`crop(i*pw, 0.17*H, (i+1)*pw, H) → resize(pw, H) → paste(i*pw, 0)`，第 4 格直接 `paste(原图, 3*pw)`。代价：三格看不到领口（领口仍在第 4 格与服装板上可见）。
4. **放弃无头格**：四格全有头、靠同一张 `<image2>` 维持同一个人 —— 代价是四张脸一致性下降，需后续挑选。

### 已试并否决：靠后期像素修补冒头（不要再走这条）

| 做法 | 实测结果 |
|---|---|
| 按画布肩线横切，上部铺同色背景 | 头没了，但**长发的下半截落在肩线以下**，切不掉；把切线下移就切进肩膀 |
| 按画布轮廓抹掉轮廓外的像素 | 侧发/背发去掉一部分，**下巴与嘴仍留在画面里** |
| 加羽化过渡 | 接缝更显眼；衣服没坏，但截断处是硬边 |

机制：模型会把头发画到肩线**以下**，任何水平裁切都会留半截头发，切到头发结束的位置就切到衣服。**结论：冒头只能在生成阶段解决，不能后期救** —— 不要把它当兜底方案交给用户。

## 服装段禁用词与替换写法

| 禁用 | 为什么 | 改成 |
|---|---|---|
| `body` | 触发「画身体」→ 补头 | `a straight cut from the neckline to a plain turned hem` |
| `falls from the shoulders` | 同上 | `hangs from the neckline` |
| `wraps around the body` | 同上 | `closes at the centre front` |
| `tee-dress` 单独出现 | 带「穿在人身上」的语义 | `a cotton jersey dress, straight cut, mid-calf` |
| `no waist seam` / `no belt` / `no drawstring` | 否定式被当内容画出来 | 从正向删除，移进负向 |

负向补：`waist seam, drawstring, drawstring tunnel, belt, belt buckle, defined waist, tailored waist, cinched waist, wrap front, robe, nightgown`。

## 一处误源（会让第 4 格找错参考）

第 4 格的脸/皮肤/表情/头发**只认 `<image2>`**。写成 `her skin condition, her expression and her hair are those shown in <image3>` 是错源 —— `<image3>` 是服装板，里面没有人；这会让第 4 格同时受到两套参考拉扯，脸既不像也不稳。
