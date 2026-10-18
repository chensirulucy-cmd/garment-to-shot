# 模板 · AI 人物建模特写（单工作流专用）

> **状态**：✅ 已验证（2026-10-17 通过，2026-10-18 修订为「三段旋钮」结构）
> **工作流**：Qwen-Image 2.1 · 文生图（T2I）· 1:1 · 1280×1280 · cfg 3.5 / 30 步 / euler-simple · LoRA 可选
> **用途**：产出一张「建模级」正脸特写 —— 脸大、背景干净、无衣物、无道具，下游给四视图第 4 格、换脸的 `image2`、视频参考帧。
> **不含具体人物**：触发词与人物状态按 IP 填。

## 一、两个版本

| 版本 | 正向里写什么 | 什么时候用 |
|---|---|---|
| **有 LoRA** | 触发词内联锚句主语 + **不写任何五官清单** + 三段状态句 | 有该 IP 的 LoRA（首选） |
| **无 LoRA** | 触发词删掉，**补回五官清单**（脸型/眉/眼/鼻/唇/独特标记）+ 三段状态句 | 没有 LoRA 或 LoRA 基座不对 |

触发词**只有一种写法**：`... of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait ...`（主语内联）。独立成行、或删掉年龄，脸会变通用。

## 二、人物三段旋钮（"换了个人"就出在这三段）

脸的骨头（骨相）在这条线上是**锁死**的：LoRA 版不写五官、无 LoRA 版照抄清单。真正让人物"变了"的只有下面三段 —— 改人物只改这三段，别处一个字不动。

| 旋钮 | 默认（冻结原文里的句子） | 改成什么会怎样 |
|---|---|---|
| **① 表情** | `her expression stays calm and closed-mouthed, her lips resting together with a faint natural colour and no tension in the mouth or brow` | 换成 `half-awake, flat, unbothered, worn out` → 立刻变成"疲惫、没精神"的另一个人；换成 `a light smile lifts the apples of her cheeks` → 变成"亲和、甜美" |
| **② 发型** | `long straight black hair parted down the middle and tucked back behind both ears, so her whole face, her cheekbones and the line of her jaw stay uncovered` | 换成高丸子头 → **头型轮廓全变**，LoRA 的脸会被拉扯，这是最伤身份的一段；换刘海/遮额 → 脸被切掉一角 |
| **③ 皮肤状态** | `skin appears light and unretouched, with its natural texture and fine detail visible … and the faintest warmth in the shaded side of her neck` | 加 `tired cast under the eyes` → 憔悴/临床感；加 `luminous / even / no dullness` → 越做越白；两句都不写 → 模型默认往瓷白走 |

**顺序**：先定发型（影响最大）→ 再定表情（决定气质）→ 最后调皮肤（决定"健康/疲惫"）。一次只改一段，改完对比。

## 三、冻结原文（有 LoRA · 白底 · 裸肩）

```text
The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait against a plain white backdrop. The background is a flat seamless pure white field with nothing standing in it, its tone even from the upper-left corner to the lower-right corner of the frame, with only a faint falloff behind her head and no object of any kind anywhere in the picture. She is placed at the centre of the frame and faces the camera directly, her head upright and level, her neck straight and her chin neither raised nor lowered, and the lower edge of the frame closes just below the base of her neck, so her face and hair fill most of the picture and only the very tops of her shoulders reach the bottom edge. Her long straight black hair is parted down the middle and tucked back behind both ears, so her whole face, her cheekbones and the line of her jaw stay uncovered, with the rest of it falling away behind her neck and shoulders and a soft sheen running along the crown and through the hair at the temples. A few fine strands lift clear of the hairline, and the parting itself is clean and narrow. Her eyes look level into the lens with a small highlight in each of them, and her expression stays calm and closed-mouthed, her lips resting together with a faint natural colour and no tension in the mouth or brow. Her skin appears light and unretouched, with its natural texture and fine detail visible across the forehead, down the bridge of the nose, across both cheeks and along the jaw, and the faintest warmth in the shaded side of her neck. Her eyebrows sit in their natural shape and her lashes stay separate and unclumped. The lighting is soft and even and comes from just above and slightly to the left of the lens, filling the whole of her face from the hairline to the jaw without a hard shadow, holding a soft highlight on the forehead, the cheekbones and the tip of her nose, and leaving only a faint shading beneath the jaw and behind the ears. That same light raises the sheen along the crown of her hair and holds the backdrop at one even value behind her. Nothing else enters the frame — no hands, no arms and no garments beyond the tops of her bare shoulders at the very bottom edge — and no text, signage or prop appears anywhere in it. The overall composition is centred and symmetrical, with her head and shoulders filling the frame edge to edge and a calm, uncluttered studio mood.
```

> 背景默认取**纯白**。要中性灰（更耐看、更少反光）就把 `plain white backdrop` / `pure white field` 换回 `plain neutral backdrop` / `mid-neutral field`，其余不动。

## 四、无 LoRA 版怎么改

只改两处：
1. 删掉锚句里的触发词（`of sakurawomanC, `）；
2. 在发型句后插入五官清单（变量表见 `templates/07` 的旧版变量表）：脸型 + 下颌 + 下巴、眉（粗细/弧度/眉尾）、眼（大小/眼皮/眼尾/睫毛/眼神光）、鼻（鼻梁/鼻头/鼻翼）、唇（厚薄/唇峰/唇色）、**独特标记**（该 IP 没有就写 `none`，并在负向禁 `mole, beauty mark, freckle, birthmark`）。

## 五、负向（必含"保脸"词）

```text
low resolution, blurry, blurry face, soft focus, noise, compression artifacts, small face, distant framing, wide shot, waist-up framing, full body, half body, arms, hands, visible hands, torso, chest below the collarbones, clothing, collar, strap, textile, deformed face, distorted facial features, facial asymmetry, waxy skin, plastic skin, over-smoothed skin, airbrushed skin, poreless skin, doll-like appearance, porcelain skin, milky skin, bleached skin, washed out, overexposed face, face brighter than the neck, illustration, painting, anime, cartoon, CGI, obvious 3D render, text, watermark, logo, border, frame, hat, headwear, earrings, necklace, props, multiple people, duplicate person
```

`small face / distant framing / waist-up framing / full body / arms / hands / torso` 这几条**不能删** —— 删了就会退成半身像、脸变小。

## 六、参数

| 项 | 值 |
|---|---|
| 尺寸 | **1:1 · 1280×1280**（脸最大；3:4 可多约 15% 脸像素） |
| cfg / steps / sampler | **3.5 / 30 / euler · simple** |
| LoRA | `LoraLoaderModelOnly`，strength **1.0**（不足再 1.15），**挂在缓存节点之前** |
| 负向 | cfg>1 才生效，所以这条线负向**要写** |

## 七、判据（六条）

1. 脸占画面高 ≥45%，下缘收在颈根以下（不能到胸）
2. 只有肩膀最上沿入画，无衣物、无首饰
3. 背景是一整块纯色（白或中性灰），无渐变、无道具、无投影
4. 发型与旋钮②一致；额头/颧骨/下颌线没被头发遮掉
5. 表情与旋钮①一致，眉眼无紧张
6. 脸**不亮于**脖子（判"有没有被白背景带白"）

## 八、已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 越做越白、像瓷娃娃 | 正向写 `luminous / even / flawless`，负向又压 `dull / grey / pores`，两头夹击 | 删掉这些词；只留 `light and unretouched … faintest warmth` |
| 像"临床/证件照" | 写了 `tired cast / dark circles / visible pores` 清单 | 删掉；疲惫感由旋钮①的表情承担，不由皮肤清单 |
| 人物"不是她" | 改了旋钮②（发型） | 发型是头型轮廓，改它必伤身份；要换发型就重训/换 LoRA |
| 脸变小、变半身 | 负向删了 `small face / waist-up / torso`，或正向出现服装 | 恢复负向；删掉任何衣物句 |
| 出成"AI 模板美女" | 正向写了五官清单（有 LoRA 时）或 `beautiful` 类吹词 | 删清单，身份交给触发词 |
