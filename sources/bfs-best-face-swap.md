# 来源 · BFS 换头 LoRA（Qwen-Image 2.1）

> 本线用的唯一第三方资产。**只放出处与核对结果，权重文件不进库。**

## 一、出处

| 项 | 值 |
|---|---|
| 仓库 | https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap |
| 作者 | Alissonerdx |
| 许可 | **MIT**（可商用；作者要求不用于公众人物或未授权者） |
| 体量 | 274,402 次下载 / 1,415 likes / 最后更新 2026-09-27（查询时间 2026-10-18） |
| 基座 | `Qwen/Qwen-Image-2.1` —— 与本机 `qwen_image_2.1_int8_convrot.safetensors` 同代 |
| 说明文档 | 仓库内 `docs/qwen-image-2.1.md`（头）、`docs/qwen-image-2.1-body.md`（全身） |

## 二、本线实际用到的两个文件

| 文件 | 字节数 | 大小 | sha256 | 放哪 |
|---|---|---|---|---|
| `bfs_head_v1.1_qwen_2.1.safetensors` | 260,096,144 | 248.0 MB | `d1d748d5601077f3b6d05766f6823510e901970d916afa404a97e85dc92fa88e` | `models/loras/` |
| `p_qwen_image_2.1_8step_v0.1.safetensors`（Pruna 8 步蒸馏，来自 https://huggingface.co/PrunaAI/Pruna-Qwen-Image-2.1 ） | 335,606,104 | 320.1 MB | `f0865d68b02511a3a0ed232d9d1aa99cac3a94166f574b38bcbab1a7a297bb15` | `models/loras/` |

> 8 步是 Pruna 蒸馏 LoRA 的配套步数；不装 Pruna 就必须把 steps 提到 20–30，否则出糊图。

## 三、同仓库其它权重（**本机不要下**）

`bfs_head_v5_2511_*`（基座 2511）、`bfs_head_v1~v4_*_2509`（基座 2509）、`krea2`、`flux-klein`、`ltx2` —— 基座都不是 Qwen-Image-2.1，下下来加载会失败。

## 四、官方文档要点（原文提取，非改写）

1. **输入顺序不可反**：`<image1>` = 目标/底图（提供身体、姿势、构图、光照、环境）；`<image2>` = 参考头（提供身份、发型、瞳色、鼻型）。反了会换错人。
2. **强度从 1.0 起**，只在检查完身份／发界／肤色融合／表情迁移后才动。
3. **V1.1 做了什么**：把 `img_mlp.gate_up`（blocks 16–31，16/192 个模块）摘掉 —— 皮肤塑料感来自这条 MLP 通路，不是整个 LoRA。实测脸部微细节（bilateral residual）+约 1/3，身份相似度与头部角度误差基本不变，表情迁移略弱于 V1。
4. **V1.1 alternative**：192 个模块全留，只把 `img_mlp` 整体缩到 35% —— 皮肤细节更多、表情迁移最强，代价是头部角度误差平均多约 1°。
5. **作者自述限制**：`Faces get less accurate as the subject gets smaller in frame; the drop is measurable and it is the main open weakness.`（小脸是主要未解弱点）
6. **参考图规则（body 版文档）**：参考放大到与场景同尺寸是**最差**设置；缩到约 0.59 MP（768×768 面积）时场景背景保留得最好。

## 五、为什么不用 ReActor

| | BFS LoRA | ReActor 插件 |
|---|---|---|
| 环境改动 | 无（放一个 safetensors） | pip 装 7 个包 + 1 个 custom_node |
| 下载量 | 248 MB（+ 可选 320 MB） | 529 MB + buffalo_l + 依赖 |
| 像素行为 | 整图重绘，衣服可能漂 | 只贴五官区域，衣服不动 |
| 本机状态 | ✅ 已跑通（00367） | 未装（仅完成调研） |

调研结论见 `docs/` 中 2026-10-18 一轮记录；ReActor 账本：`Gourieff/ComfyUI-ReActor`（★1384，2026-10-15 仍在更新，0.7.x 起不再依赖 insightface）。
