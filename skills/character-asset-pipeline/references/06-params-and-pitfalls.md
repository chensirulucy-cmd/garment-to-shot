# ⑥ 参数、接线与踩过的坑

## 一、模块参数（ComfyUI · Character Sheets 类工作流）

| 项 | 值 | 说明 |
|---|---|---|
| 底模 / CLIP / VAE | `qwen_image_2.1_int8_convrot` / `qwen3vl_8b_int8_convrot` / `qwen_image_2.1_vae_bf16` | 三个模块共用 |
| 采样 | **cfg 3.5 / steps 30 / euler / simple** | 作者值。**cfg=1 时负向完全不生效**（截图里常见 1.0/25 的残留值） |
| ResolutionSelector | 比例 / 百万像素 / 尺寸对齐倍数（8 或 32） | 三个模块**各自一个**，互不影响 |
| `custom_size` | `false`＝输出尺寸**跟随第 1 张输入图**；`true`＝用 ResolutionSelector | 它对应子图里的 `switch` 输入 |
| 种子 | 人像可 `fixed`（复现）；四视图 `fixed`（同一提示词 A/B 对比时用同一个种子） | |
| 模块链 | 服装板 →（SaveImageAdvanced）→ 角色表 `<image3>`；人像 →（SaveImageAdvanced）→ 角色表 `<image2>`；白模 → LoadImage → `<image1>` | 想换身份源就重跑人像模块，而不是手动换图槽 |
| 缓存节点 | `QwenImage21Cache`（auto/default） | **LoRA 必须插在缓存之前**（`UNETLoader → LoraLoaderModelOnly → Cache → KSampler`），否则缓存可能吃掉 LoRA |

## 二、LoRA 插点与选文件

- **只插人像模块**（那一步才用权重造脸）。服装板/服装模板/四视图都不插。
- `LoraLoaderModelOnly`：`UNETLoader.model → LoraLoaderModelOnly.model → KSampler.model`，`strength_model = 1.0`。
- **先读文件元数据再选**：`ss_base_model_version`（zimage / krea2 / sdxl / qwen_image_2 …）与 `ss_tag_frequency`（触发词）。同名文件常分属不同基座，挂错基座等于没挂。

## 三、验证方法（不要靠肉眼）

| 要验的 | 怎么量 |
|---|---|
| 站立格真的无头 | 取每格**顶部 18% 带**的暗像素（亮度<80）占比：无头应 <2%；有黑发人头会 >8% |
| 背景是否单色 | 取每格四角平均 RGB：若右列明显暗于左列 → 混底色 |
| 脸占格高比例 | 裁出第 4 格，量脸（发际线→下巴）高度 ÷ 格高 |
| 裁剪是否到位 | 找前景首次变宽的行（即肩线），量它距格顶的像素与百分比；<1% 已经算封好 |
| 颜色是否塔黑 | 取服装区域平均亮度：中灰约 130；实得 5–30 就是塔黑了 |

## 四、下游 H3（参考图生视频）注意

- 标签是 **1-based**：界面插槽显示「图片0/图片1」，但提示词里必须写 `<Picture 1>` / `<Picture 2>`（ComfyUI 内核 `nodes_minimax_h3.py` 的 `MiniMaxH3ReferenceToVideo` 注释：*Ordinals are 1-based per type*）。写 `<Picture 0>`＝无效标签＝那张图没被绑定。
- 三图分工：**脸图＝身份、角色板＝服装、场景图＝环境**；只用定义内容的图不建独立条目，只在 `<Subject N>` 行里引用。
- 角色板里**无头的站立格**会向视频泄露「无头」：必须写 `Her head, neck and hair are always present in every shot.`
- 场景板里**没有的人**（如会议室里的同事）只能纯文字定义，模型可能漏画 → 要么接受，要么换一张已经坐著人的场景图。
- 两张身份类图同时喂时，加优先级句：`Where <Picture 1> and <Picture 2> differ in any detail of her face, her hair or her skin, <Picture 1> is followed and <Picture 2> is ignored.`
- 位置漂移（人物站位不对）**不是**模型能力上限，而是**缺帧锚**：参考图里没有人 → 位置无锚。解法是让参考图自带人（或在时间线上加 Guide 锚定首帧）。

## 五、坑列表（按出现频率）

1. 把「编辑式标签清单」当 T2I 提示词用，或反之——格式错。
2. 把要保留的东西逐项描述 → 模型当「重画指令」→ 漂。
3. 负向里写了正向要求的东西 → 自相矛盾，成败交给种子。
4. 同名 LoRA 挂错基座。
5. `custom_size=false` 时以为 ResolutionSelector 在生效（实际输出跟输入图）。
6. 负向里留了 `back view`，结果三格全正面。
7. 两套颜色/两套服装的资产混着喂（人像写灰、服装板给绿）→ 四格身子穿一套、脸戴一套。
8. 四视图 1 MP → 第 4 格脸只有二百多像素 → 细节重画。
9. 组③ 里又插了 LoRA → 身份双源互拉。
10. 凭肉眼看图说「上方还有留白」→ 实测只有 0.76% → 白折腾一轮。
