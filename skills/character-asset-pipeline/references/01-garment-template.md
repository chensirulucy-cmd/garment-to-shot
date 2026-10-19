# ① 服装模板（单张 · 幽灵人台成品展示图）

用途：把**任意一张服装照/上身照**变成干净的「隐形人台」单品展示图。变量只有两个：**鞋从哪来**、**件数**。

## 变量

| 变量 | 取值 | 影响 |
|---|---|---|
| 鞋的来源 | ① 输入图自带 ② 无鞋时自动配一双 ③ 第二张参考图 `<image2>` | 决定结尾那段怎么写 |
| 件数 | 由输入图决定 | 一件套（连衣裙）**不能**被切成两件 |
| 画幅 | 跟第 1 张输入图（`custom_size=false`） | 竖版服装照 → 竖版出图 |
| 底色 | `plain white` / `plain light-grey` | 按这条线原有产物的底色走：电商白底就写 `plain white seamless studio background`，并在颜色保真句加 `the white ground must stay pure white and never turn grey, cream or blue`。模板默认的浅灰只在复刻 00235/00393 那批时用；用户说「背景不是纯白」＝底色句选错，改这一句，别去改光或负向 |

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

## 变体：上装 / 下装 / 鞋 三件套（纯文生图）

三件套不是上面那个编辑版的改写，而是**另一支工作流**：9 节点纯文生图、cfg 1、30 步、euler-simple、实测 768×1376。没有输入图，所以每件的版形必须写死：

| 必写 | 不写会怎样 |
|---|---|
| 下装腿型：`straight-leg`（膝到脚踝同宽）/ `slim`（收到脚踝）/ `wide-leg`（外扩） | 默认出阔腿或紧贴腿，之后调词也拉不回来 |
| 上装贴身程度 + 有没有塞进腰头（`without being tucked in`） | 默认塞进去或半塞，腰线位置错 |
| 鞋型：`low-top canvas court sneakers with a white rubber cupsole, flat laces through five eyelets` | 默认出跑鞋/板鞋混血款 |
| 三色分离句：白不许变米/灰/蓝，浅蓝不许变深蓝/黑/灰，鞋白不许变灰 | 白会变米白、浅牛仔会变深蓝 |

结构仍是六段：定调句 → `[TOP: …], [BOTTOM: …], [SHOES: …]` 清单 → 隐形身体（逐项否定）→ 视角与可见细节 → 廓形 → 光/背景 + 只含这几件 + 颜色保真 + 无字。**cfg=1 时负向权重为 0**，“没有人”全靠隐形身体那段的逐项否定撑。成品与词库：仓库 `templates/02-ghost-set-trio.md`。

**哪些写得死、哪些写不死（实测）**：

| 类型 | 项 | 结果 |
|---|---|---|
| 硬约束（一句话能锁） | 下装腿型（直筒：膝到踝同宽）、裤长（及踝搭鞋面）、三色分离、画面里没有人、件数 | 出图与文字一致 ✅ |
| 软约束（写死也漂 ±1 档） | 腰位（`mid-rise` → 出图偏高腰）、上装松量（`sits close` → 出图偏宽松） | 漂了，且加词拉不回来 ✗ |

软约束只承诺「档位」，不承诺「精确值」；要精确只能出图后局部编辑。

**出图先读元数据**：这条线最容易在「上一支工作流的节点还挂着」时出错——实测出现过服装台把人物 LoRA（strength 1.0）带进链路、以及无 LoRA + 768×1376 的误跑被当成证据。判定一张图能不能当证据，只看 PNG 内嵌 prompt 里的 `LoraLoaderModelOnly` 与尺寸，不看文件名、不看界面：`python scripts/check_output_meta.py <output_dir> --glob 'Qwen_image_2.1_*.png' --last 8`。

## 件数三分支（一件 / 两件 / 叠穿）—— 通用版负向只配一件式

通用版正向里 `If it shows separate garments, keep exactly that number of separate pieces` 只是**一句条件句**，压不住负向；而通用版负向里有四条反两件套的词：`two-piece set, split into a top and a skirt, separated bodice and skirt, two garments where the image shows one` —— **cfg>1 时遇到两件套输入，模型会把上下合并成一件连衣裙**（用户实测报错：「这套提示词会将 2 件套也解成一整件」）。

| 输入 | 用哪版 | 关键改动 |
|---|---|---|
| 1 件（连衣裙 / 连体裤） | 通用版原样 | 不动 |
| 上衣 + 下装（不叠穿） | **两件套版** | 件数段改成 `two separate garments, one top and one bottom`；构图段要求「下装先挂、waistband 完整可见当独立一条带、上装下摆停在 waistband 上方或正好到它、两片之间留可见台阶」；**负向删掉上面四条**，换成 `one-piece dress, merged into a single garment, the top sewn onto the skirt, joined at the waist, missing waistband, waistband hidden under the top` |
| 上身叠穿 ≥2 层 | **叠穿版**（下节） | 内层露出位置逐处点名 |

### 叠穿版（衬衫 + 毛衣/夹克 + 下装 + 鞋）

1. **报件数**：`a layered set of N pieces and it stays N pieces`，逐件点名（内层 / 外层 / 下装 / 鞋）。
2. **内层露出的位置必须逐处写**：`its collar standing above the outer garment's neckline at the throat, and its cuffs showing beyond the outer garment's sleeve ends at both wrists` —— 只写「里面还有一件衬衫」会被吃掉（领口与袖口是叠穿唯一能看见的证据）。
3. **构图写成两个空壳**：`the outer garment holds its volume as if over an invisible torso, and the inner shirt sits inside it, its collar and both cuffs emerging from under it`；
   负向禁 `merged layers, fused into one garment, missing inner collar, missing shirt cuffs, layer order reversed, only the sweater shown`。
4. **必须删掉通用正向里的「空领口」句——这是叠穿丢内层的真正原因。** 通用版写着 `an open empty neckline … and nothing inside the garments`，对单件成立，对叠穿就是「把里面那件删掉」的直接指令：实测内层白衬衫整件消失，领口只剩外层立领。叠穿版把领口判给衣服：`The neckline belongs to the layers, not to the empty space: the outer layer's opening stays open to exactly the same depth as the photograph, its front closure stays pulled down to exactly the same point on the chest, and the inner garment fills that opening — its collar rising above the outer edge by the same amount the photograph shows, its collar points lying open over the outer layer`。负向补 `neckline closed that the photograph leaves open, zip pulled up to the collar, collar closed to the throat, missing inner placket, the opening filled with skin, bare neck in the neckline`。
5. **露出量写「和照片一样」，不写厘米**：`rising above the outer edge by the same amount the photograph shows` / `stays pulled down to exactly the same point on the chest`。写死 2–4 cm 这类绝对值，模型会按数字重排整个领口。袖口同理：照片里没拍到内层袖口就别要求 `cuffs emerging`，改成 `where the photograph shows an inner cuff emerging, keep it emerging by the same amount; where it does not, the outer sleeve end finishes the arm cleanly`。
6. **写提示词前先确认源图里内层真的露着**：把源图领口区域裁出来放大看一眼（外层拉链/领口是否敞开、内层领子是翻领还是立领、露出多少）。外层拉到顶、内层一点没露的输入，这条线不适用——先如实说明，让用户换图或先做别的处理。
7. **参数**：叠穿版跑编辑线 **30 步 · cfg 3.5**。实测用户会用文生图那套 **25 步 / cfg 1.0** 来跑，cfg 1 时负向权重为 0，上面这些禁令全部失效，内层照丢。

配件（包 / 围巾 / 帽子）默认**不上画面**：正向写 `X is not part of the outfit and does not appear in the frame`，负向补 `tote bag, handbag, added accessories`。

街拍输入另加两条：正向 `a straight front view rather than a walking pose`（否则保留行走姿态）；负向 `walking pose, mid-stride, motion blur, street scene, buildings, pedestrians`。海报类输入再加 `the large Chinese text and the brand marks printed across the photograph are removed completely` + 负向 `Chinese characters, price tag, logo`。

## 变体：单件连体款（睡裙 / 连衣裙）的三件套式结构

同一支 9 节点文生图，把 `[TOP]/[BOTTOM]/[SHOES]` 三槽换成**一个 `[GARMENT]` 槽**：

```
[GARMENT: a loose short-sleeve sleep tee-dress in soft matte cotton jersey, cut as one piece with an easy A-line body: a wide round neckline finished with a narrow self-fabric binding of the same colour, short straight sleeves ending at mid-upper-arm in a plain turned hem with no elastic, a relaxed body with no waist seam, no drawstring and no belt, and a plain turned hem sitting above the knee]
```

- **隐形身体段要多写一句「空下摆 + 地面接触影」**：`a hem hanging loose and empty with nothing below it but a faint contact shadow on the floor`。单件款没有裤脚可写，只写「空」不够 —— 不写就会给你长出一双拖鞋或一截腿。
- **廓形段写死裙型与下摆位置**（A 字 / 直筒；膝上 / 及膝 / 小腿）。单件款最常见的两种自作主张：自己加一条腰封、自己配一双拖鞋 —— 两个都要进负向。
- **颜色按参考图定档**：`warm ivory white — a soft off-white with a slight warm cast, never grey, never yellow, never blue and never a cold paper white`。电商真实色与参考图的暖光色不是一个值，改色只改这一句，别只换一个词然后把 `never grey/yellow/blue` 留在原地自相矛盾。
- **负向反向禁**：`belt, drawstring, waist seam, pockets, lace, ruffles, slippers, shoes, long sleeves, sleeveless, elastic cuffs`。

## 验收（逐项看）

1. 件数对不对（连衣裙没被拦腰切开）；2. 有没有长出手/头/皮肤；3. 下摆、袖口有没有被裁；4. 鞋是否成对、是否搭调（不要尖头细跟配运动装）；5. 品牌文字是否清掉；6. 背景是否单一浅灰、没有格线或黑底。

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 连衣裙被切成上衣+裙子 | 旧版正向写了「top garment above / bottom garment below / 上衣下摆压住裙腰」——**这句假定两件套** | 用本文的「件数保持」段 |
| 凭空长出一双鞋 / 尖头细跟配休闲装 | 旧版正向写了「the pair of shoes standing side by side」——**这句假定有鞋** | 用「有则照抄，无则配一双中性款」段或鞋图变体 |
| 灰衣服出成黑色 | 没点颜色 + 输入底色偏深（实测亮度 87）+ 输出像素不足 | 正向点名 `mid-grey`，写「不是黑也不是白」 |
| 输出跟着输入图变成奇怪比例 | 输出尺寸**继承某一张参考图**（可能是 `<image1>` 画布，也可能是 `<image3>` 服装图），`ResolutionSelector` 不参与 | 先把参考图统一到目标像素，别在 selector 上调 |
| 幽灵台下方长出一双脚（鞋里有脚趾 / 脚踝） | ① 鞋是**开口 / 细带**款：不画脚就立不住；② 正向写了 `in the position feet would occupy`、`as if a foot had just stepped out of it`、`open toe / low vamp` —— 等于点名要脚。**与 cfg 无关**：实测 cfg 3.5、负向里已有 `feet, toes, skin`，仍然出脚 | ① 鞋换**包头尖头细跟**（closed toe，不给脚留位置）；② 正向把鞋写成**空物件**：`empty shoes standing on the studio floor … the toe boxes fully closed with nothing visible inside them`；③ 删掉 `feet would occupy` / `stepped out of it` 这类句式，只写 `side by side on the floor beneath the hem, angled slightly outward`；④ 负向补 `a foot inside a shoe, toes visible, skin visible in the shoes, open-toe shoes, strappy sandals` |
| 源图只有上半身（只到胯），出图下半身是编的 | 裙长、下摆、鞋全部没有参考 | 提示词里**写死**裙长（及膝 / 小腿中部 / 踝上）与鞋型，并在交付时说清「这两处是补的，不是复刻」；不要声称整套照原图还原 |
| 叠穿出图只剩外层，内层（衬衫领/袖口）全没了 | 正向的 `an open empty neckline … nothing inside the garments` 与叠穿冲突；再叠加 cfg 1.0 负向失效 | 按上节第 4–7 条：领口判给内层 + 负向补 `neckline closed / zip pulled up / collar closed to the throat` + 改 30/cfg3.5 |
| 出图「像这套」但不是这套（鞋从运动鞋变系带皮鞋、织纹变通用纹） | 正向里用**款式形容词**复述衣服（`beige cable-knit half-zip sweater / ribbed cuffs`）→ 模型按词重画；源图里衣服像素占比又小 | 删掉款式形容词，只留件数、层级与位置；改写成 `Copy, do not redraw … a close lookalike is a failure, only the photographed garment is correct`；量不够就把参考图裁到「衣服+下装+鞋」再送（编辑线按像素照抄） |


---

## 实测参数与一个致命细节（来自 00235 / 00241 的 PNG 内嵌元数据）

- 实际运行：`steps 25 · cfg 1.0 · euler / simple · denoise 1.0` · `9:16 / 1.0 MP` · 参考图 1 张（原服装照）。
- **线别先分清**：`00393`（492 词）是**文生图线**（9 节点、无 `LoadImage`、`EmptyLatentImage` 吃 `ResolutionSelector` 9:16·1MP·multiple 8 → 768×1376）；`00449`（511 词）/ `00472`（745 词）才是**编辑线**，尺寸跟随输入图按 32 对齐。别拿文生图线的 768×1376 当编辑线的尺寸基线。
- **cfg = 1.0 时负向权重为 0**：00241 那段 1355 字符的负向（`two-piece set / split into a top and a skirt / only one shoe / two different shoes …`）**完全没有生效** —— 防拆件、防补鞋全靠正向句在扛。
- 推论（C 级）：要负向兜底就必须把 cfg 提到 >1（会拉紧色彩风格，需重调）；否则别在负向上花字数，把约束都写成正向句。
- 正向里真正起作用的四段（A2 结构，可直接复用）：①**去人清单**（head/face/skin/arms/hands/legs/feet/toes/body）②**件数锁**（单件连衣裙：一个领口、一条肩线、连续前后片、腰线只是构造线，无横向断裂、无独立腰头压在裙上；分开就保持原数量）③**保真清单**（末尾必须有 `add or divide` 的反向约束）④**鞋的两支**（有鞋原样；无鞋→补一双朴素深中性、取自本套自身色板、无 logo 无装饰，一双并排、朝外八、带接触阴影）。


---

## A / B / C 三版路由（按输入图选，不要混用）

幽灵服装台只有一个骨架，**件数/层数决定用哪一版**。三版共用「去人 + 保真照抄 + 鞋 + 纯白底 + 去字」，差别只在「件数段」和「领口怎么写」。

| 输入图 | 版本 | 正向特征句 | 负向关键 | 参数 | 取证 |
|---|---|---|---|---|---|
| 一件（连衣裙/连体裤） | **A** | `If it shows a single one-piece garment such as a dress, keep it as one continuous garment` | `two-piece set, split into a top and a skirt, separated bodice and skirt` | 25/1.0 或 30/3.5 | 00449 / 00446 / 00473 / 00474 |
| 上衣 + 下装，不叠穿 | **B** | `two distinct pieces` + `Never join the two into a single garment` + `waistband fully visible` | 去掉上面那四条，改成 `one-piece dress, merged into a single garment` | 25/1.0（实测可出）或 30/3.5 | 00453 / 00454 / 00455 |
| 上身叠穿 2–3 层 | **C** | `Count the layers … keep exactly that many layers` + `the inner garment fills that opening` | `neckline closed that the photograph leaves open, zip pulled up to the collar, missing inner collar` | **30/3.5** | 00470 / 00472 |

### 三条硬规则（踩过坑）

1. **A 版的负向不能用在两件套上**：`two-piece set / split into a top and a skirt / separated bodice and skirt / two garments where the image shows one` 这四条在 cfg>1 时会把两件合并成一件 —— 用户实测两件套被解成一整件，根因就是这四条 + 正向只有一句条件句。
2. **C 版正向绝对不能写 `open empty neckline … nothing inside the garments`**：这句要求「领口里什么都没有」，模型会照做，把内搭（衬衫/T恤）整层删掉，只剩外层。正确写法是 `the neckline belongs to the layers, not to the empty space` + `the inner garment fills that opening`。
3. **C 版必须 30 步 / cfg 3.5**：cfg 1.0 时负向权重为 0，而 C 版的「拉链不许拉到顶」「内搭不许丢」全靠负向兜底（实测 00466 用 25/1.0 + 早期文案 → 内搭消失）。

### 交付前读三个数

1. 正向/负向 sha256 前 12 位 —— 同版必须同指纹（本次四版指纹：A `e2284262dfa1` / B `ca058df58e64` / C 早期 `65f51900007a` / C 修正 `639013b3f3ee`）
2. `steps / cfg` —— 与版本表对齐，别把 T2I 线的 25/1.0 当成编辑线默认
3. 输入图尺寸 —— 出图尺寸**跟随输入图按 32 对齐**（1200×1600→1216×1600、614×612→608×608）。`ResolutionSelector` 被 `ComfySwitchNode(switch=False)` 旁路，改它无效；要换尺寸就换输入图。另：尺寸不同的两张图不得互比像素

### 暖色像素不能当「有没有人体」的判据

驼色/米色大衣的暖色占比可达 25%（00473 实测 25.58%，画面里没有任何皮肤）。判人体只能目视。
