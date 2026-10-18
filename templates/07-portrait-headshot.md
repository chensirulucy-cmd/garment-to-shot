# 模板 · 人像近脸特写（影棚美妆头）

> **状态**：✅ 已验证（2026-10-17）。验证案例见 `cases/07-portrait-2026-10-17.md`。
> **用途**：产出一张可直接当"身份插槽"的正面特写 —— 裸肩无衣物，避免服装污染。
> **本模板不含具体人物**：人物形象按剧本变量填。

## 一、变量表

| 变量 | 必填 | 写法要求 | 坑 |
|---|---|---|---|
| `{{年龄阶段}}` | ✅ | `in her mid-twenties` 这类人生阶段，不写岁数 | 写"25岁"→ 模型不认识 |
| `{{发型句}}` | ✅ | 具体到**分缝 / 是否后梳 / 耳朵露不露 / 碎发位置** | 只写"black hair"→ 每张都不一样 |
| `{{脸型句}}` | ✅ | 脸型 + 下颌线 + 下巴（3 项） | 只写"oval face"→ 脸会变通用 |
| `{{眉/眼句}}` | ✅ | 眉：粗细+弧度+眉尾；眼：大小+眼皮+眼尾+睫毛+眼线 | 漏眼线 → 眼神变呆 |
| `{{鼻/唇句}}` | ✅ | 鼻梁高矮 + 鼻头 + 鼻翼；唇厚薄 + 唇峰 + 唇色（**带修饰词**，如 coral brick orange-red） | 写"red lips"→ 会跑到正红 |
| `{{独特标记}}` ★ | ✅ | **按 IP 填**：痣 / 疤 / 发际线形状 / 胎毛，位置用**观者视角**写（`the viewer's left eye`）；**该 IP 没有就写 `none`，并在负向加 `mole, beauty mark, freckle, birthmark`** | 多个 IP 共用一套模板时，**绝不许沿用上一个 IP 的标记** —— 痣是某一个 IP 的特征，不是默认值；写错就等于换了一个人 |
| `{{皮肤句}}` | ✅ | 真实版：可见毛孔 + 皮肤纹理 + 哑光缎面，只在额头/鼻梁/颧骨留柔和光泽 | 想要"磨皮版"就删掉毛孔半句，但别两头都要 |
| `{{妆容}}` | ◻︎ | 眼影/睫毛/腮红/唇；不写就按素颜 | 与唇色句重复描述会打架 |
| `{{取景}}` | ✅ | 头顶留白 % + 下缘切到哪 + 脸占画面高 % | 脸占比 <25% → 身份不保 |
| `{{光线}}` | ✅ | 方向 + 软硬 + 色温 + 眼神光 | 写"studio light"太笼统 |
| `{{背景}}` | ✅ | 颜色 + 是否渐变 + **无道具/无字** | 忘了禁字 → 冒出 logo |

## 二、不变量（原样粘）

- 唯一光句：`The lighting is …`（单独一句，写方向/软硬/色温/高光落点）
- 唯一收束句：`The overall composition is …`（一句，写对称/居中/两侧边距）
- 禁词：`cinematic / beautiful / 8K / masterpiece / highly detailed`
- 比例只进 `wh_ratio`，正文只写 `square / vertical` 这类方向词

## 三、骨架（一段到底，400–500 词）

```
The image is a {{square|vertical}} studio beauty headshot of a {{年龄阶段}} East Asian woman, seen front-on and centred, against a {{背景色}} seamless background in soft neutral light. The frame runs from {{头顶留白}} above her hair down to {{下缘位置}}, so her face fills about {{脸占比}} of the picture height and sits on the vertical centre axis, with {{颈部/肩/锁骨可见到什么程度}} and no jewellery and no clothing anywhere in the picture. Her hair {{发型句}}. Her face {{脸型句}}. Her eyebrows {{眉}}. Her eyes {{眼}}. Her nose {{鼻}}. Her lips {{唇 + 唇色}}. {{独特标记}}. Her skin {{皮肤句}}. The lighting is {{光线句}}. The background is {{背景句}}, with no prop, no horizon line and no lettering anywhere. The overall composition is {{收束句}}.
```

## 四、参数（实测）

| 项 | 值 |
|---|---|
| 模型 | Qwen-Image 2.1 |
| cfg / steps / sampler | **3.5 / 30 / euler · simple**（cfg>1 负向才生效） |
| 尺寸 | 1:1 → 1280×1280（1.64 MP）｜2:3 → 832×1216｜≤2.2 MP |
| LoRA | 有 LoRA 时：触发词**内联锚句主语**，并**删掉整个脸型/眉/眼/鼻/唇段**（否则跟 LoRA 抢身份） |

## 五、判据（四条，10 秒）

1. **独特标记在不在**（痣/疤/发际线）← 第一眼就看这个
2. 发型状态对不对（分缝 / 后梳 / 耳朵露不露）
3. 皮肤：不蜡不塑料；真实版要有毛孔
4. 背景：中心到边缘有没有那道渐变；眼里有没有眼神光
