# qwen-image-2-1-prompter · 索引

> 按需读取；本文件只列用途，不放内容。

## references/

| 文件 | 讲什么 |
|---|---|
| `cheat_sheet.md` | Qwen-Image-2.1 Vocabulary & Parameter Cheat Sheet — This cheat sheet provides quick vocabulary lookups for composing precise prompts matching  |
| `edit-prompt-enhancer.md` | 上游「Edit Prompt Enhancer v2」层（用户工作流里真实存在，必须知道） — 用户 ComfyUI 编辑工作流里，**提示词节点前面还挂了一个「改写器」**：一个约 1 万字符的元提示词（`PrimitiveStringMultiline`），标题为 **` |
| `edit_rules.md` | Qwen-Image-2.1 Image Edit & Multi-Image Prompt Enhancer Rules — An input image is ALWAYS present — this is always an image-editing task, never text-to-ima |
| `face-swap-and-identity-transfer.md` | 换脸 / 身份替换（Qwen-Image 编辑线） — 适用：用户给出「一张脸 + 一张成图」，要求把这张脸换上去（换脸、身份替换、"用我的人像参考"）。 |
| `four-view-character-board.md` | 角色四视图（角色板）：三槽结构 + 四格冒头的排查顺序 — 适用：Qwen-Image 2.x 编辑线，两支采样器串联（服装板 → 角色板）。产出四格：正 / 背 / 侧三个站立全身（**无头**）+ 第四格脸部大特写。 |
| `garment-from-text.md` | 用文字复刻一件服装（而不是用服装图） — 服装有两条路线：**文生图 + 文字清单** 与 **编辑 + 服装图**。路线选错的代价是「货不对版」，所以先按下表定级，再决定用哪条线。 |
| `garment-showcase-wall.md` | 服装展示墙流水线（Qwen-Image 2.1 编辑 · 竖幅） — **用途**：一个空房间画布 + N 套来源服装 → 一次编辑生成「多格服装展示墙」（带货封面 / 换装视频中段镜头）。 |
| `t2i_rules.md` | Qwen-Image-2.1 Text-to-Image (T2I) Prompt Rewriting Rules — You turn a user's image request into one long English paragraph that describes the finishe |
| `worn-look-slot-wiring.md` | 换装 / 上身穿：槽位、像素预算、比例 — 只在与「把一套衣服穿到人/人台上」有关的任务里读。三条主线：**接线 → 像素 → 比例**，任何一条错，出图都是废的，而表现都像「模型不会」。 |

## scripts/

| 文件 | 干什么 |
|---|---|
| `diff_two_outputs.py` | diff_two_outputs.py - 两张 ComfyUI 出图的逐节点 / 逐句取证 diff。 |
| `inspect_output_metadata.py` | 打印 ComfyUI 出图元数据里「当时真的这么跑」的配置。 |
| `validate_prompt.py` | Prompt validator for Qwen-Image-2.1 prompt rewriting specifications. |
