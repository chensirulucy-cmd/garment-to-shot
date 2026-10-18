# 模板 · AI 人物建模特写（写法指南，不是范文）

> **状态**：✅ 已验证（2026-10-17 通过）。**这是"怎么写"的规则，不是一段要复读的字符串。**
> **工作流**：Qwen-Image 2.1 · 文生图 · 1:1 · 1280×1280 · cfg 3.5 / 30 步 / euler-simple · LoRA 可选
> **要做的**：换 IP、换风格、新建人物时，**按下面的骨架重写**，不是改两个字。

## 一、九段分工（顺序固定，每段只干一件事）

| # | 段 | 作用 | 写坏的后果 |
|---|---|---|---|
| 1 | 锚句 | 定画幅 + 影棚/自然光 + **触发词内联** + 年龄 + 取景类型 + 背景 | 触发词独立成行 → 脸变通用 |
| 2 | 背景句 | 一整块纯色、四角同值、无物无影 | 出现渐变/家具 → 脸被抢注意力 |
| 3 | 站位句 | 居中、正对、头平、**下缘收到哪**、脸占多少 | 收低了就退成半身，脸变小 |
| 4 | 发型句 | 分缝/走向/掖耳/露出哪些骨相/发丝/光泽 | 遮额或遮下颌 → 身份特征被切掉 |
| 5 | 表情句 | **眼（视线+高光）+ 嘴（闭合+唇色）+ 眉（有无张力）**，三处缺一就空 | 只写 "calm" → 脸呆；只写嘴 → 眼死 |
| 6 | 皮肤句 | 质感在哪看得见 + 阴影侧的一点血色 | 写 "luminous/even" → 瓷白；写 "tired cast" → 临床 |
| 7 | 光句 | 方向 + 软硬 + 高光落点 + 阴影位置 | 光写在皮肤之前 → 肤色被光冲白 |
| 8 | 收边句 | 无手无臂无衣物（只留肩最上沿）+ 无字无道具 | 漏了 → 长出衣服、手、耳环 |
| 9 | 收束句 | 构图 + 情绪一句话 | 漏了 → 构图散 |

## 二、骨架（把 `{}` 换成你要的，其余句式照抄）

```text
The image is a {square|portrait} {realistic studio|natural daylight} photograph of {触发词}, a {年龄阶段} {族裔} woman, framed as a {tight facial portrait|head-and-shoulders portrait} against a {纯白|中性灰|暖米} backdrop. The background is a flat seamless {...} field with nothing standing in it, its tone even from the upper-left corner to the lower-right corner of the frame, with only a faint falloff behind her head and no object of any kind anywhere in the picture. She is placed at the centre of the frame and faces the camera directly, her head upright and level, her neck straight and her chin neither raised nor lowered, and the lower edge of the frame closes {just below the base of her neck|at the top of her chest}, so her face and hair fill most of the picture and only the very tops of {her bare shoulders|her shoulders} reach the bottom edge. {发型句}. Her eyes {视线 + 高光}, and her expression {表情基调}, {嘴部}, {眉部}. Her skin {肤色档 + 质感可见的位置}, {阴影侧的一点暖}. Her eyebrows sit in their natural shape and her lashes stay separate and unclumped. The lighting is {光句：方向 + 软硬 + 高光落点 + 阴影}. {收边句：无手无臂无衣 只留肩最上沿 + 无字无道具}. The overall composition is {收束句}.
```

## 三、词库（按需挑，不要全用）

**背景**：`plain white` ／ `mid-neutral grey` ／ `warm cream` ／ `pale blue-grey` —— 一律加"四角同值、无物、无影"。

**发型**（按对身份的伤害从小到大）：
1. 中分长直、掖到双耳后（**最保脸**，额头颧骨下颌全露）
2. 侧分、掖一侧耳、另一侧垂在颊前
3. 低马尾、鬓角留两缕
4. 贴头皮盘发、额头全露
5. 大波浪侧分、发量盖住一侧下颌（开始掉身份）
6. 高丸子头 + 太阳穴碎发（**头型轮廓变了，身份掉最多**）
7. 齐颌短发（脸型被重新定义）

**表情**（先定"气质"，再落到眼/嘴/眉）：
- 平静：`calm and closed-mouthed, no tension in the mouth or brow`
- 极浅笑：`a faint closed-lipped smile that lifts the apples of her cheeks by the smallest amount`
- 不笑直视：`unsmiling, level gaze, lips resting together`
- 疲惫：`half-awake and flat, the lids low, no tension`（**别再加皮肤清单**）
- 亲和：`a light open smile showing a little of the upper teeth`（会改变脸部比例，慎用）
- 冷感：`serious, the mouth closed and the jaw set`

**皮肤（五档，选一档写，并指明质感在哪看得见）**：
1. `light and unretouched … fine detail visible across the forehead, down the bridge of the nose, across both cheeks and along the jaw, with the faintest warmth in the shaded side of her neck`
2. `fair with a soft warm undertone … a little natural redness across the nose and the apples of her cheeks`
3. `warm beige, its tone deepening slightly along the jaw and down the neck`
4. `deeper olive tone with a natural sheen on the forehead and the cheekbones`
5. `pale and cool-toned, the neck a shade deeper than the face`（要"冷白"时用这档，别靠 negative 硬压）

**光**：`soft and even from just above and slightly to the left of the lens` ／ `daylight from a window at the right, thirty degrees off the lens axis` ／ `a large soft source at chest height, twenty degrees off axis so a gentle falloff crosses one cheek`。

## 四、有 LoRA / 无 LoRA：只差一段

| | 有 LoRA | 无 LoRA |
|---|---|---|
| 锚句 | 触发词**内联**在 `of …` 位 | 删掉触发词 |
| 五官 | **一个字不写**（写了就抢身份） | 在发型句后插入：脸型+下颌+下巴 / 眉 / 眼 / 鼻 / 唇 / 独特标记（该 IP 没有就 `none`，负向禁 `mole`） |
| 其余八段 | 完全一样 | 完全一样 |

## 五、三条铁律

1. **不写 `luminous / even / flawless / glowing`** —— 这些词把皮肤推向瓷白，是"越做越白"的根因。
2. **皮肤写在光之前** —— 先定肤色档，再让光去打；反过来光会把肤色冲淡。
3. **一次只改一段** —— 发型、表情、皮肤、背景、服装，同时改两个就分不清是谁造成的。

## 六、范例（同一骨架，两种风格——都只是示例）

**A · 中性灰影棚 / 中分长直 / 平静（基准款）**

```text
The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait against a plain white backdrop. The background is a flat seamless pure white field with nothing standing in it, its tone even from the upper-left corner to the lower-right corner of the frame, with only a faint falloff behind her head and no object of any kind anywhere in the picture. She is placed at the centre of the frame and faces the camera directly, her head upright and level, her neck straight and her chin neither raised nor lowered, and the lower edge of the frame closes just below the base of her neck, so her face and hair fill most of the picture and only the very tops of her shoulders reach the bottom edge. Her long straight black hair is parted down the middle and tucked back behind both ears, so her whole face, her cheekbones and the line of her jaw stay uncovered, with the rest of it falling away behind her neck and shoulders and a soft sheen running along the crown and through the hair at the temples. A few fine strands lift clear of the hairline, and the parting itself is clean and narrow. Her eyes look level into the lens with a small highlight in each of them, and her expression stays calm and closed-mouthed, her lips resting together with a faint natural colour and no tension in the mouth or brow. Her skin appears light and unretouched, with its natural texture and fine detail visible across the forehead, down the bridge of the nose, across both cheeks and along the jaw, and the faintest warmth in the shaded side of her neck. Her eyebrows sit in their natural shape and her lashes stay separate and unclumped. The lighting is soft and even and comes from just above and slightly to the left of the lens, filling the whole of her face from the hairline to the jaw without a hard shadow, holding a soft highlight on the forehead, the cheekbones and the tip of her nose, and leaving only a faint shading beneath the jaw and behind the ears. That same light raises the sheen along the crown of her hair and holds the backdrop at one even value behind her. Nothing else enters the frame — no hands, no arms and no garments beyond the tops of her bare shoulders at the very bottom edge — and no text, signage or prop appears anywhere in it. The overall composition is centred and symmetrical, with her head and shoulders filling the frame edge to edge and a calm, uncluttered studio mood.
```

**B · 同一骨架换成"暖米背景 + 高丸子头 + 疲惫"**：只改第 2 段背景、第 4 段发型、第 5 段表情，第 6/7/8/9 段一字不动 —— 这就是"新建一个状态"的正确改法，而不是重写整篇。

## 七、判据（六条）

1. 脸占画面高 ≥45%，下缘在颈根以下
2. 只有肩膀最上沿入画，无衣物无首饰
3. 背景一整块纯色，四角同值，无道具无投影
4. 发型与所选档一致；额头/颧骨/下颌线露出程度符合预期
5. 表情三处（眼/嘴/眉）都有交代
6. 脸**不亮于**脖子

## 八、失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 越做越白 / 瓷娃娃 | 正向 `luminous/even` + 负向压 `dull/grey/pores`，两头夹击 | 删词；只留"质感可见 + 颈部微暖" |
| 临床/证件照 | 皮肤写成 `tired cast / dark circles / visible pores` 清单 | 删清单；疲惫交给表情段 |
| 人物"不是她" | 动了发型（第 4 段），头型轮廓变了 | 回到保脸档（中分掖耳）；换发型＝换 LoRA |
| 脸变小 / 半身 | 负向删了 `small face / waist-up / torso`，或正向出现服装 | 恢复负向；删衣物句 |
| AI 模板脸 | 有 LoRA 还写五官清单，或用了 `beautiful` 类吹词 | 删清单，身份交给触发词 |

## 九、变量 / 不变量 / 真正决定画面的三句

**变量（换 IP、换风格只动这 5 个）**：① 背景色 ② 发型档 ③ 表情档 ④ 肤色档 ⑤ 光的方向。

**不变量（六条，逐字保留）**：

| # | 不变量 | 为什么 |
|---|---|---|
| 1 | 触发词**内联**在 `of …` 主语位 | 独立成行 → 脸变通用 |
| 2 | 取景下缘收在**颈根以下**、只留肩最上沿 | 收低了就退半身、脸变小 |
| 3 | 无衣物 / 无手 / 无臂 / 无首饰 / 无道具 | 出现任何一件就抢走视线 |
| 4 | 收边句（`Nothing else enters the frame …`） | 不写就长出东西 |
| 5 | 收束句（构图 + 情绪一句） | 不写构图会散 |
| 6 | 负向里 `small face / waist-up / torso / chest below the collarbones` | 删了脸立刻变小 |

**真正决定画面的只有三句**（改别的只是调气质，改这三句才换人）：

1. `of {{触发词}}, a young East Asian woman in her mid-twenties, framed as a tight facial portrait` —— 决定**像不像**
2. `the lower edge of the frame closes just below the base of her neck … only the very tops of her bare shoulders` —— 决定**脸多大**
3. 发型句里的「**掖到双耳后 + 全脸露出**」—— 决定**骨相有没有被遮**

## 十、实测偏差（2026-10-18）

| 观察 | 结论 |
|---|---|
| 暖米底 + 平光下，皮肤读作「干净无瑕」，`unretouched` 没落地 | 质感靠**光**（第 7 段换侧光），不靠加词；加 `visible pores` 只会把它推成临床照 |
| 侧分 + 一侧头发垂在颊前（00394 那一版），脸型轻微漂移 | **头发不许遮骨相**：额头/颧骨/下颌线两侧至少一侧完整露出；垂颊前＝让模型重估半张脸 |
| 写「极浅笑抬起苹果肌」也会改变脸型 | 表情只写 `no tension in the mouth or brow`，不写肌肉动作 |
