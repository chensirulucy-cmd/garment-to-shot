# 模板 · 换头（LoRA 版，Qwen-Image 2.1 + BFS）

> **状态**：✅ 已验证（2026-10-18）。验证案例见 `cases/11-faceswap-2026-10-18.md`。
> **用途**：把「人像特写」的脸，安到「全身照」的身体上 —— **不靠提示词求它别改，靠一个只学换头的 LoRA**。
> **本模板不含具体人物/服装**：人物形象与服装按剧本变量填。

## 一、适用与不适用

| 能做 | 不能做 / 别指望 |
|---|---|
| 保留目标图的姿势、构图、光照、背景、**服装** | 保不住脸的"本来长相"—— LoRA 会把五官往参考脸的审美特征拉（眼更大、唇更厚、皮肤更平） |
| 一张特写脸迁到任意全身照 | 脸在画面里很小时（< 100 px 宽）身份会明显掉分 |
| 保留目标图的微表情与视线方向（V1.1 弱一些，alternative 强） | 手挡脸、极度侧脸、强逆光 —— 作者列为已知失败场景 |

## 二、输入槽约定（顺序不能反）

| 槽 | 放什么 | 提供什么 | 反了会怎样 |
|---|---|---|---|
| `image1` | **目标全身图**（要保留身体和衣服的那张） | 身体、姿势、构图、光照、环境、服装 | 会把人换成参考图那个人 |
| `image2` | **参考头像**（特写/证件照） | 身份、发型、瞳色、鼻型 | 同上 |

参考头像建议裁到 **下巴下方 5–10%** 即可；带头肩会连肩线/锁骨一起搬过去，容易出现肤色断层。

## 三、变量表

| 变量 | 必填 | 写法要求 | 坑 |
|---|---|---|---|
| `{{目标全身图}}` | ✅ | 全身、头顶到鞋完整，服装清楚 | 人物太小的远景脸不够像素 |
| `{{参考头像}}` | ✅ | 正面、纯背景、下颌完整 | 带肩颈会多搬一条肩线 |
| `{{服装保真句}}` | ◻︎ | 逐件点名衣服（颜色 + 款式 + 鞋子 + 背景），只在 A/B 的"锁衣服"组用 | 逐件描述可能触发重绘（编辑线已证），**不要默认开** |
| `{{额外质感句}}` | ◻︎ | 如 `real skin texture, visible pores` | 与 LoRA 的平滑倾向对抗，力度有限 |

## 四、不变量（原样粘）

- 提示词**必须以 `head_swap:` 开头** —— 这是 LoRA 的训练触发前缀。
- `<image1>` / `<image2>` 是**锚点 token**，不能改成"第一张图"之类的自然语言。
- 采样器用 `euler`（本机实例没有 `deis_2m`），scheduler `simple`，**cfg 必须 1**（cfg=1 时负向提示词无效，留空即可）。
- LoRA 强度起点 **1.0**；BFS LoRA 叠在 Pruna 8 步 LoRA **之后**（顺序：UNet → Pruna → BFS）。
- 目标图分辨率**不要低于原图**：Resize 只用来对齐 32 的倍数，不要顺手降采样。

## 五、骨架

**A · 基线（默认）**

```text
head_swap: start with <image1> as the base image, keeping its lighting, environment, and background. remove the head from <image1> completely and replace it with the head from <image2>, strictly preserving the hair, eye color, nose structure from <image2>. copy the direction of the eye, head rotation, micro expressions from <image1>, high quality, sharp details, 4k
```

**B · 锁衣服（A/B 对照，非默认）**

```text
head_swap: start with <image1> as the base image, keeping its lighting, environment, and background. remove the head from <image1> completely and replace it with the head from <image2>, strictly preserving the hair, eye color, nose structure from <image2>. copy the direction of the eye, head rotation, micro expressions from <image1>. keep everything below the neck from <image1> exactly as it is: {{服装保真句}}. high quality, sharp details, 4k
```

**负向**：留空。要用负向必须把 cfg 抬到 >1，但 BFS 是照 cfg=1 训的，**不要动**。

## 六、参数（实测）

| 项 | 值 |
|---|---|
| 底模 | `qwen_image_2.1_int8_convrot.safetensors`（7.26 GB） |
| 文本编码 | `qwen3vl_8b_int8_convrot.safetensors`（9.35 GB） |
| VAE | `qwen_image_2.1_vae_bf16.safetensors`（675 MB） |
| LoRA | Pruna 8step（1.0）→ BFS `bfs_head_v1.1_qwen_2.1`（1.0） |
| cfg / steps / sampler / scheduler | **1.0 / 8 / euler / simple**（不装 Pruna 则 steps 20–30） |
| 尺寸 | 目标图按原比例、长边 ≤ 1440；参考图单独 512–768，**不要和成品同大** |
| 出图耗时 | 8 步 800×1440 ≈ **80 秒**（含 15 秒模型初始化），日志实测 80.08s / 83.55s |

## 七、判据（四条，10 秒）

1. **接缝**：下颌→脖子、发际线、耳周有没有硬边/双影/色块断层。
2. **衣服**：颜色、款式、鞋子、背景有没有换掉（用 RGB 均值对比，不靠眼看）。
3. **身份**：眼型/唇形/鼻头是否已向参考靠拢，而**不是**只做了磨皮。
4. **比例**：头顶到下巴的脸高占画面 10–15% 属正常；头身比失衡＝换崩了。

量化三项（必做，写进案例）：脸宽 px ≥ 参考脸 1/2 ｜ 衣服区均值 RGB Δ ≤ 10 ｜ 头区与衣服区平均像素差分别记录。

## 八、已知偏差（用之前先认）

- **脸被"网红化"**：眼更大、唇更厚、皮肤更平。作者在 V1.1 说明里承认这是 LoRA 固有倾向，只是被压到"约三分之二"。
- **参考图比目标图大是最差设置**（作者 body 版实测）。骨架里两张图都走同一个分辨率选择器时，参考会被放大到和长边一样大 —— 这是本线当前的已知偏差，见 `cases/11-faceswap-2026-10-18.md`。
- **参考脸本身若是 AI 生成的**，换上去的是"经过两次 AI 转述的脸"，偏差在参考图就锁定了。
