# ③ 面部特写人像（身份图）

职责：**只出脸与头发**，不做服装展示。它是四视图角色版第 4 格的来源，也是下游视频里「她是谁」的唯一根据。服装在这个资产里**完全不写**。

- 取景：头肩以上，脸尽量大（官方参考实现里脸占画面高 30–50%；这里更紧：**接近面部特写**）。
- 比例：**1:1**（同 MP 下脸最大）或 3:4（脸像素多约 15%）。**绝不用 16:9**——两侧空白会把脸挤小。
- 画幅：**≤2.2 MP**（8 GB 卡的安全线）。实测通过尺寸 1:1 `1280×1280` = 1.64 MP；`1600×1600` = 2.56 MP **超线**，别用。
- LoRA：**这一步插**（`LoraLoaderModelOnly`，`strength 1.0`）；**LoRA 生效时正向里不写任何五官清单**（写了会跟权重抢身份）。**无 LoRA 时相反 —— 五官必须逐项写全，见下节。**
- 触发词写法**只有一种**：作为锚句的主语名词**内联**——`The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait …`。**不许另起一行、不许写成「触发词独立首行」**（实测：独立首行 + 删掉年龄 + 把取景放宽到带上胸，脸会明显变通用、不像本人）。
- 模板的**冻结**只在一个 IP、一个资产内部成立（同一个人、同一风格反复出图时不复读改写）。**换 IP／换风格／新建人物时不许复读，按仓库 `templates/07-portrait-headshot.md` 的九段骨架重写对应段落**（背景 / 取景 / 发型 / 表情 / 皮肤 / 光），其余句式照抄。用户说「固化」指的是「会写」，不是「背下来」。

## 正向（一段到底 · 观察者描述）

```
The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait against a plain neutral backdrop. The background is a flat seamless mid-neutral field with nothing standing in it, its tone even from the upper-left corner to the lower-right corner of the frame, with only a faint falloff behind her head and no object of any kind anywhere in the picture. She is placed at the centre of the frame and faces the camera directly, her head upright and level, her neck straight and her chin neither raised nor lowered, and the lower edge of the frame closes just below the base of her neck, so her face and hair fill most of the picture and only the very tops of her shoulders reach the bottom edge. Her long straight black hair is parted down the middle and tucked back behind both ears, so her whole face, her cheekbones and the line of her jaw stay uncovered, with the rest of it falling away behind her neck and shoulders and a soft sheen running along the crown and through the hair at the temples. A few fine strands lift clear of the hairline, and the parting itself is clean and narrow. Her eyes look level into the lens with a small highlight in each of them, and her expression stays calm and closed-mouthed, her lips resting together with a faint natural colour and no tension in the mouth or brow. Her skin appears light and unretouched, with its natural texture and fine detail visible across the forehead, down the bridge of the nose, across both cheeks and along the jaw, and the faintest warmth in the shaded side of her neck. Her eyebrows sit in their natural shape and her lashes stay separate and unclumped. The lighting is soft and even and comes from just above and slightly to the left of the lens, filling the whole of her face from the hairline to the jaw without a hard shadow, holding a soft highlight on the forehead, the cheekbones and the tip of her nose, and leaving only a faint shading beneath the jaw and behind the ears. That same light raises the sheen along the crown of her hair and holds the backdrop at one even value behind her. Nothing else enters the frame — no hands, no arms and no garments beyond the tops of her bare shoulders at the very bottom edge — and no text, signage or prop appears anywhere in it. The overall composition is centred and symmetrical, with her head and shoulders filling the frame edge to edge and a calm, uncluttered studio mood.
```

> `sakurawomanC` 是本文的触发词示例；换角色就换这一个词（无 LoRA 时删掉它）。

## 负向

```
low resolution, blurry, blurry face, soft focus, noise, compression artifacts, small face, distant framing, wide shot, waist-up framing, full body, half body, arms, hands, visible hands, torso, chest below the collarbones, deformed face, distorted facial features, facial asymmetry, extra fingers, extra limbs, malformed hands, waxy skin, plastic skin, over-smoothed skin, airbrushed skin, poreless skin, doll-like appearance, illustration, painting, anime, cartoon, CGI, obvious 3D render, text, watermark, logo, border, frame, hat, headwear, earrings, necklace, props, multiple people, duplicate person
```

## 九段骨架（换 IP / 换风格 / 新建人物时按这个重写）

同一套句式，九个槽位；换人只重写对应那几段，**不要整篇重写，也不要复读上一版**：

| # | 段 | 槽位 |
|---|---|---|
| 1 | 锚句 | `{{方/竖}} {{影棚/自然光}} photograph of {{触发词}}, a {{年龄阶段}} {{族裔}} woman, framed as a {{紧特写/头肩}}, against a {{白/中性灰/暖米}} backdrop` |
| 2 | 背景 | 一整块纯色、四角同值、无物无影 |
| 3 | 站位 | 居中正对、头平颈直、**下缘收到颈根以下**、只留肩最上沿 |
| 4 | 发型 | 分缝/走向/掖哪只耳/露出哪些骨相/发丝/光泽 |
| 5 | 表情 | 眼（视线+高光）+ 嘴（闭合+唇色）+ 眉（有无张力），三处都要有 |
| 6 | 皮肤 | 肤色档 + 质感在哪看得见 + 阴影侧一点暖 |
| 7 | 光 | 方向 + 软硬 + 高光落点 + 阴影位置（**写在皮肤之后**） |
| 8 | 收边 | 无手无臂无衣物 + 无字无道具 |
| 9 | 收束 | 构图 + 情绪一句 |

句式固定、槽位可换。发型/表情/皮肤的词库（含每档的身份代价）在仓库 `templates/07-portrait-headshot.md`。

## 人物只有三段旋钮（换人设只动这三段）

骨相在 LoRA 版里是锁死的（不写五官）。真正让人物「看起来换了一个状态」的只有三段，**一次只动一段**：

| 顺序 | 旋钮 | 默认写法 | 动了会怎样 |
|---|---|---|---|
| ② | **发型** | 中分长直、掖到双耳后、额头/颧骨/下颌全露 | 换成高丸子头／刘海遮额＝**头型轮廓变了**，身份掉最多；发型是这三段里对相似度伤害最大的 |
| ① | **表情** | `calm and closed-mouthed, no tension in the mouth or brow` | 换成 `half-awake, flat, unbothered`→疲惫的人；`a faint closed-lipped smile`→亲和的人。表情必须落到眼（视线+高光）/嘴（闭合+唇色）/眉（有无张力）三处，缺一处就空 |
| ③ | **皮肤** | `light and unretouched … faintest warmth in the shaded side of her neck` | 加 `tired cast`→憔悴/临床感；加 `luminous / even`→瓷白。肤色要选**具体档**（light／warm beige／deeper olive／pale cool），不选档就默认最白那一档 |

## 两个「看不见」的漂移源：头发遮挡骨相、表情写肌肉词

触发词在整段里只出现一次；它之的**每一个描述头骨、遮挡、肌肉形变的词都在和它分权重**。真正把脸型推歪的往往不是 LoRA，是下面这三类句子：

| 写法 | 为什么会漂 | 改法 |
|---|---|---|
| 头发垂在颊前（`tucked behind her right ear while the left side falls forward past her cheekbone`） | 一侧颧骨与下颌线被盖住，被遮的那半张脸只能由模型按「通用脸」补齐 → 轮廓走形 | 侧分可以，但**不许头发垂在颊前**；额头 / 颧骨 / 下颌线至少完整露出一侧（最好两侧） |
| 表情写肌肉动作（`a smile that lifts the apples of her cheeks`、`the jaw set`） | 这是在改骨相不是改情绪；笑会加宽颧骨与下半脸 | 只写 `no tension in the mouth or brow`，或干脆不写表情句；要笑只用极淡的 `a faint closed-lipped smile`，**不加 “lifts…” 这类动作从句** |
| 肤色写成「从脸到脖子渐变」 | 等于要求重新建模面部轮廓 | 只写「质感在哪看得见 + 阴影侧一点暖」，不写渐变方向 |

**验收**：与上一版同 seed 出图，两张脸裁到同尺寸并排，只看三处 —— 颧骨最宽点、下颌角位置、下巴长度。三处任一移动就是漂了，先查上面三条，别去降 LoRA 强度。

## 素颜只能写「缺什么」，不能写「长什么样」

素颜/淡妆靠**缺失式否定**表达：`no foundation, no concealer, no powder, no blusher, no eyeliner, no mascara, no curled lashes, no lip colour`，唇色写 `in her own natural tone`。

两个反例（都会跟 LoRA 抢脸）：

- **长相类**：`the lashes sparse and uncurled`、`the lids heavy` —— 这是在描述骨相，不是描述状态。
- **妆色类**：`a muted dusty rose` —— 具体口红色号等于给这张脸换了一张嘴。

## 无 LoRA 版：五官必须写全

既没有触发词也没有参考图时，脸的唯一来源就是文字 —— 漏一项就是让模型补一项。按这个顺序一次写完（顺序即重要度）：

脸型 + 下颌线 + 下巴 → 眉（粗细 / 弧度 / 眉尾）→ 眼（大小 / 眼皮 / 眼尾 / 睫毛 / 眼线）→ 鼻（鼻梁 / 鼻头 / 鼻翼）→ 唇（厚薄 / 唇峰 / 唇色）→ 肤色。

- 只写 `oval face / big eyes` = 交出一张通用脸。
- 唇色必须**带修饰词**（`warm coral brick orange-red`），写成单色词（`red` / `pink`）会跑到正红正粉。
- 漏写眼线 → 眼神发直发呆；漏写睫毛 → 眼睛像塑料。

## 身份锚的优先级（决定「像不像」的不是漂亮程度）

**独特标记 > 发型状态 > 唇色 > 五官量词。** 一颗痣、一道疤、发际线形状、额角胎毛，比十几个形容词更能锁住一个人。

**但标记是 per-IP 变量，不是默认值。** 同一个模板服务多个 IP 时，该 IP 没有痣就写 `none`，并把 `mole, beauty mark, freckle, birthmark` 放进负向；**绝不沿用上一个 IP 的标记** —— 多写一颗痣等于把甲的脸按到乙的头上，而且是「看起来很像、就是不对」那种最难查的错。

- 标记位置一律用**观者视角**写（`below the outer corner of the viewer's left eye`），不要写「左眼下方」—— 左右在生成里会翻。
- 标记写进正向还不够：**负向要反过来护住它**（`mole removed, no mole, clear cheek`），否则模型做「净脸」美化时第一件事就是抹掉它。跑完第一眼先看标记在不在。
- 发型状态要落到颗粒度：是否后梳、有无分缝、耳朵露不露、鬓角与额角碎发、后面是否收拢 —— 只写 `black hair` 等于没写。

## 真实皮肤（不蜡、不塑料）必须成对写

正向：`her skin keeps its real texture: fine pores across the nose and the inner cheeks, the faint grain of skin on the forehead and chin, a matte-satin finish carrying only a soft sheen on the forehead, the bridge of the nose and the cheekbones`

负向：`flawless skin, poreless skin, airbrushed, beauty filter, wax skin, plastic skin, oily sheen, harsh specular highlights, over-smoothed, heavy retouch`

- 两句必须成对：只写正向 → 模型仍按「精修美妆」出；只写负向 → 皮肤变干变糙。
- **负向要 cfg > 1 才生效**（cfg=1.0 时权重为 0，等于白写）。本线实测口径：**cfg 3.5 / steps 30 / euler · simple**。

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 脸很像但「不是那个人」 | LoRA 文件挂了错基座（同名文件分属 zimage/krea2/sdxl/qwen） | 读 safetensors 元数据中的 `ss_base_model_version`，选与底模一致的（如 `qwen_image_2`）+ 触发词匹配 |
| 脸变小、变成半身像 | 用 16:9 出图，或提示词里出现了服装/身体的描述 | 改 1:1，删掉服装相关句 |
| 出成「AI 模板美女」 | **有 LoRA 却**写了五官清单 / 用了 `beautiful` 这类吹词；或**无 LoRA 却漏写五官** | 有 LoRA：删掉五官清单；无 LoRA：按「无 LoRA 版」逐项写全 |
| 痣 / 疤 / 特定发际线不见了 | 模型做「净脸」美化时会主动抹掉标记 | 正向写死位置（观者视角）+ 负向加 `mole removed, no mole, clear cheek` |
| 皮肤蜡、像塑料、明显磨皮 | 正向只说了「真实」却没配负向，或 cfg=1 让负向失效 | 用「真实皮肤成对写法」，cfg 提到 3.5 |
| 脸不像、但 LoRA 已挂对 | 参考图路径不对，或强度 <0.8 | `strength 1.0`，再不行提到 1.15；LoRA 要在缓存节点之前 |
| **越做越白、像瓷娃娃** | 正向写 `luminous / even / flawless`，负向又同时压 `dull / greyish / visible pores` —— 两头夹击后皮肤只剩白 | 删掉这些词；肤色改成具体档 + `faintest warmth in the shaded side of her neck`；负向加 `porcelain skin, milky skin, bleached skin, washed out, face brighter than the neck`；验收时量脸与脖子的均值差 |
| **素颜出成临床/证件照** | 用皮肤清单（`tired cast / dark circles / visible pores`）去表达疲惫 | 疲惫交给表情段；皮肤只写质感位置与血色，不写症状清单 |
| **人物换了个气质、不像本人** | 同时改了发型与表情（两个旋钮） | 一次只改一段；先定发型（伤害最大），再表情，最后皮肤 |
