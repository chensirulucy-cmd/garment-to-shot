# 换脸与“只修脸”：能走什么、不能走什么

## 一、真人全身换装：编辑线已否决（有实测数字，别重开）

目标曾是「把特写脸放到全身照身上，其余像素不动」。实测三轮：

| 轮次 | 出图 | 头宽 | 参考头宽 | 比值 | 失败方式 |
|---|---|---|---|---|---|
| 1 | 768×1376 | 106 px | 553 px | 0.19× | 只剩白模关节，脸是编的 |
| 2 | 928×1664 | 131 px | 553 px | 0.24× | 脸糊；**灰衣漂成米白 RGB(240,237,233)**；灰圆头低方跟 → 裸色尖头高跟 |
| 3 | — | — | — | — | 塌成黑 T 黑裤，服装全丢 |

结论：**编辑线做“造一个人 + 保一张脸”不成立**，原因是机制而非措辞（整图重绘 + 脸的像素预算不足）。人物上身改走 **LoRA 文生图**（已证可复刻服装）；编辑线只保留局部任务：换色、换鞋、单格返修、加光效。

## 二、“描述即重画”：服装漂色的直接证据

给换脸提示词时把衣服逐件写了一遍（`knotted bow / ruffles / bell cuffs / pencil skirt / shoes`），结果整件被重画：灰 → 米白、圆头低方跟 → 裸色尖头高跟。

修法只有两条，**同时用**：

1. 正克只留**一句总括**：`her whole outfit including its colours, its cut, its fabric and its footwear … stays exactly as <image2> shows them. The clothing is not part of this edit and is not redrawn.`
2. 负向**点名颜色与鞋型**：`cream blouse, ivory blouse, white blouse, off-white outfit, beige blouse, nude shoes, pointed stiletto heels, recoloured garment, colour shift on the outfit, different shoes`。

## 三、裁脸 → 放大 → 重绘 → 回贴（唯一能“衣服不动 + 脸清楚”的组合）

因为整图重绘无法只改一块，必须把脸**单独拿出来放大后再重绘**，其余像素走合成。

配方（已算出，可直接复用）：

1. 在全身图上量头部深色（发）包围盒 → 头宽 `hw`、中心 `cx, cy`。
2. 方形裁切，边长 `≈ 2.35 × hw`，中心对齐头；放大到 **1024×1024**（Lanczos）。
3. 目标：**放大后脸宽占画面 ≈ 43–44%**，与身份参考图的脸占比一致（实测参考 553/1254 = 44%；成品 436/1024 = 43%）→ 尺度匹配才有身份。
4. 这一次编辑：`<image1>`=人像特写、`<image2>`=上面这张方图，尺寸 1:1 · 1 MP · cfg 3.5 · steps 30。
5. 出图后**羽化回贴**到原图（面部区域遮罩羽化 8–20 px），服装/背景/影子像素 100% 不动。

判据：回贴后按 ArcFace 余弦相似度对比原图与参考，两者差值要显著（详见 `references/identity-scoring.md`）。

## 四、真换脸插件的环境结论（本机实测，2026-10）

- 旧仓 `Gourieff/comfyui-reactor-node` **被 GitHub 封禁**（403 staff disabled）；现用新仓 `Gourieff/ComfyUI-ReActor`（节点：`ReActorFaceSwap / ReActorFaceSwapOpt / ReActorRestoreFace / ReActorFaceSimilarity`）。
- 本机 ComfyUI venv = **Python 3.13.12 + torch 2.10.0+cu130**；无 `insightface`、无 `cv2`，有 `onnxruntime 1.29.0`。**Python 3.13 下 insightface 无现成 wheel**，装它要编译 → 高风险。
- `install.py` 的顺序是**先下 `inswapper_128.onnx`（529 MB，HF `Gourieff/ReActor`）再装依赖**：下载中断 = 模型半截、pip 一个没装。回滚只需删 `custom_nodes/ComfyUI-ReActor` + `models/insightface/`。
- 因此：**装之前先确认三件事**（insightface 轮子 / onnxruntime-gpu 与 CUDA 13 是否兼容 / 模型放哪），拿不到明确答案就别装。用户明确要求：**不擅自新增插件**。
- 换脸算法只认 ArcFace 的 512 维特征，**不关心源脸是真人还是 AI 生成**；真正的风险是源脸本身已偏离本人 → 换上去等于把偏差固化。

## 五、什么时候该停

同一目标连续 3 次以上、每次失败方式都不同（白模关节 / 漂色 / 塌成纯黑），说明**工具选错**，不是在调参。这时应当停下来说清：放弃哪条线、保留哪条线、替代路线是什么，并把实测数字写进项目文档，避免下一轮重开。
