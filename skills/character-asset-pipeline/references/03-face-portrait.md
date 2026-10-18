# ③ 面部特写人像（身份图）

职责：**只出脸与头发**，不做服装展示。它是四视图角色版第 4 格的来源，也是下游视频里「她是谁」的唯一根据。服装在这个资产里**完全不写**。

- 取景：头肩以上，脸尽量大（官方参考实现里脸占画面高 30–50%；这里更紧：**接近面部特写**）。
- 比例：**1:1**（同 MP 下脸最大）或 3:4（脸像素多约 15%）。**绝不用 16:9**——两侧空白会把脸挤小。
- 画幅：2.0–2.5 MP。
- LoRA：**这一步插**（`LoraLoaderModelOnly`，`strength 1.0`）；**正向里不写任何五官清单**。
- 触发词写法**只有一种**：作为锚句的主语名词**内联**——`The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait …`。**不许另起一行、不许写成「触发词独立首行」**（实测：独立首行 + 删掉年龄 + 把取景放宽到带上胸，脸会明显变通用、不像本人）。
- 下方模板是**冻结原文**：换服装、换场景都不改它；只有换角色或换触发词时才动那一个词。

## 正向（一段到底 · 观察者描述）

```
The image is a square realistic studio photograph of sakurawomanC, a young East Asian woman in her mid-twenties, framed as a tight facial portrait against a plain neutral backdrop. The background is a flat seamless mid-neutral field with nothing standing in it, its tone even from the upper-left corner to the lower-right corner of the frame, with only a faint falloff behind her head and no object of any kind anywhere in the picture. She is placed at the centre of the frame and faces the camera directly, her head upright and level, her neck straight and her chin neither raised nor lowered, and the lower edge of the frame closes just below the base of her neck, so her face and hair fill most of the picture and only the very tops of her shoulders reach the bottom edge. Her long straight black hair is parted down the middle and tucked back behind both ears, so her whole face, her cheekbones and the line of her jaw stay uncovered, with the rest of it falling away behind her neck and shoulders and a soft sheen running along the crown and through the hair at the temples. A few fine strands lift clear of the hairline, and the parting itself is clean and narrow. Her eyes look level into the lens with a small highlight in each of them, and her expression stays calm and closed-mouthed, her lips resting together with a faint natural colour and no tension in the mouth or brow. Her skin appears light and unretouched, with its natural texture and fine detail visible across the forehead, down the bridge of the nose, across both cheeks and along the jaw, and the faintest warmth in the shaded side of her neck. Her eyebrows sit in their natural shape and her lashes stay separate and unclumped. The lighting is soft and even and comes from just above and slightly to the left of the lens, filling the whole of her face from the hairline to the jaw without a hard shadow, holding a soft highlight on the forehead, the cheekbones and the tip of her nose, and leaving only a faint shading beneath the jaw and behind the ears. That same light raises the sheen along the crown of her hair and holds the backdrop at one even value behind her. Nothing else enters the frame — no hands, no arms and no garments beyond the tops of her bare shoulders at the very bottom edge — and no text, signage or prop appears anywhere in it. The overall composition is centred and symmetrical, with her head and shoulders filling the frame edge to edge and a calm, uncluttered studio mood.
```

> `sakurawomanC` 是本文的触发词示例；换角色就换这一个词（无 LoRA 时删掉它）。

## 负向

```
low resolution, blurry, blurry face, soft focus, noise, compression artifacts, small face, distant framing, wide shot, waist-up framing, full body, half body, arms, hands, visible hands, torso, chest below the collarbones, deformed face, distorted facial features, facial asymmetry, extra fingers, extra limbs, malformed hands, waxy skin, plastic skin, over-smoothed skin, airbrushed skin, poreless skin, doll-like appearance, illustration, painting, anime, cartoon, CGI, obvious 3D render, text, watermark, logo, border, frame, hat, headwear, earrings, necklace, props, multiple people, duplicate person
```

## 已知失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 脸很像但「不是那个人」 | LoRA 文件挂了错基座（同名文件分属 zimage/krea2/sdxl/qwen） | 读 safetensors 元数据中的 `ss_base_model_version`，选与底模一致的（如 `qwen_image_2`）+ 触发词匹配 |
| 脸变小、变成半身像 | 用 16:9 出图，或提示词里出现了服装/身体的描述 | 改 1:1，删掉服装相关句 |
| 出成「AI 模板美女」 | 正向写了五官清单 / `beautiful` 这类吹词 | 删掉五官清单；身份交给触发词 |
| 脸不像、但 LoRA 已挂对 | 参考图路径不对，或强度 <0.8 | `strength 1.0`，再不行提到 1.15；LoRA 要在缓存节点之前 |

## 人物状态 = 三个旋钮（不要改别处）

骨相锁死，能让"人变了"的只有三段：**② 发型**（最伤身份，改头型轮廓）→ **① 表情**（calm ↔ tired ↔ smiling 决定气质）→ **③ 皮肤**（light & unretouched ↔ tired cast ↔ luminous，写 luminous 会越做越白）。

改人物只动这三段，其余逐字保留。完整表与冻结原文见仓库 `templates/07-portrait-headshot.md`。
