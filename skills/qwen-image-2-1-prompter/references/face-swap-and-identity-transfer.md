# 换脸 / 身份替换（Qwen-Image 编辑线）

> 历史诊断资料，非当前执行配方。当前上身与换头读取仓库 templates/12-white-model-to-body.md、templates/11-faceswap-head.md。本文旧像素门槛、裁脸回贴和单格返修建议不覆盖现用路线；不据本文重开08/10或拼接项目。


适用：用户给出「一张脸 + 一张成图」，要求把这张脸换上去（换脸、身份替换、"用我的人像参考"）。

---

## 0. 先判死路：编辑线做不做得到

编辑是**整图重绘**，不是贴图 —— 参考图只提供「内容提示」，不提供像素。因此：

| 硬门槛 | 数值 |
|---|---|
| 保真所需 | **出图脸宽 ≥ 0.5 × 参考脸宽**（理想 0.7–1.5×） |
| 全身 9:16 · 2 MP（1088×1920） | 脸宽 ≈ 200–230 px；特写参考 550–750 px → **0.3×，做不到** |
| 半身（腰以上，脸占画面 ≈30%） | 1920 高上 ≈ 550 px → 0.75× → **可做** |

比值低于 0.5：**不要继续改措辞**。换构图（半身）或换工具（T2I + LoRA，人物在权重里，不靠像素搬运）。
判定用**头宽**，不要用头长或脸高 —— 见 §4。

---

## 1. 两图换脸的提示词结构（五段，顺序不能换）

1. **第一句定角色**（模型靠这句建立绑定，也顺便消掉槽号歧义）：
   `<image1> supplies the face and nothing else. <image2> is the photograph being edited and it stays the canvas.`
   标签 + 描述词（`the close-up portrait` / `the full-length photograph`）同时给。
2. **一句总括保留**：body / stance / arms and hands / legs / **whole outfit including its colours, its cut, its fabric and its footwear** / hair length and style / framing / backdrop / light / shadows，收一句 `The clothing is not part of this edit and is not redrawn.`
   —— **绝不逐件描述衣服**（`knotted bow / ruffles / bell cuffs` 会被当成「重新生成」的清单，实测灰整套被重画成米白）。
3. **只改脸**：逐项写五官（眉与眉峰、眼型与双眼皮宽度、眼距、鼻梁与鼻头、唇形与厚薄、下颌与下巴、颧骨、肤色）+ **独特标记**（痣／疤／发际线），位置一律用观者视角（`below the outer corner of her left eye`）；写死头的大小、高度、倾角不变，脸接在同一脖子上、同角度同朝向。
4. **反贴图句**：`no seam, no mask edge, no halo, no cut line at the jaw or at the hairline, no size difference between the face and the head, no pasted look`。
5. **收尾**：`Nothing else in the frame changes.`

短比长好。换脸任务里多写的每一句衣服描述，都是给模型的一条「重画这里」的许可。

---

## 2. 负向：颜色与鞋型必须点名

换脸死在三处：衣服串色、五官被美颜化、贴图边缘。

```
cream blouse, ivory blouse, white blouse, off-white outfit, beige blouse, nude shoes, white shoes, pointed stiletto heels, recoloured garment, colour shift on the outfit, changed outfit, changed skirt length, added belt, different person, another woman's face, generic face, changed body, changed pose, changed background, changed light, face too large, face too small, oversized head, tiny head, mask edge, seam at the jaw, halo, cut line, pasted face, two faces, blurred face, plastic skin, over-smoothed skin, waxy skin, different hairline, floating head, tilted head, looking away, open mouth, teeth showing, text, watermark, low resolution, blurry, noise, compression artifacts
```

规律：**「要保住什么颜色」写进负向，不写进正向。** 正向写 `stays grey` 仍会被当作要生成的内容；负向点名 `cream / ivory / white / beige / nude` 才拦得住。

---

## 3. 脸要清楚：裁脸 → 放大 → 回贴（未在本管线实测，先小步验证）

原理：遮罩重绘能保住衣服，但遮罩内的脸仍是原分辨率（130–230 px），还是糊；只有放大才有像素。

1. 按**头宽**定位，裁一个方形（边长 ≈ **2.35 × 头宽**，含颈肩与领口上缘），Lanczos 放大到 1024。
2. **校准尺度**：让裁切图里的脸宽占画面比例 ≈ 参考图的比例（例：参考 44% → 裁切图调到 ~43%）。这一步消掉的是「尺度差」，比放大参考图有用得多。
3. 用 §1 的两图换脸提示词跑一次（画布 = 裁切图，尺寸 1024×1024）。
4. 把新脸**按原定位羽化回贴**（羽化 8–12 px）到原图，其余像素一个不动。

**放大参考图没用**：出图脸只有 130 px 时，参考从 553 px 放大到 1106 px 只是被缩小两次，信息不增；插值只会更糊，ESRGAN 一类会替你「编造」毛孔与眼型，结果更像 AI 美女而不是她。

---

## 4. 量法（不要用眼睛判断）

- **头宽**：上部 30% 区域内，暗像素（亮度 < 90）最宽那一行的宽度。
- **不要用「宽度剖面找脖子最窄处」量头长**：碎发会让最窄处落在第 3 行，量出 14 头身、105 倍肩宽这类荒谬值。要头长就用暗色像素 bbox 的高度。
- **颜色**：在固定相对坐标取矩形块求 RGB 均值（灰 ≈150–180；米白 ≥230；全黑 ≤60）。
- **实际出图尺寸**：直接读保存下来的 PNG（`Image.open(p).size`）—— 尺寸控件的状态不落盘，每次都要读回来核对。
- **写进结论的是比值**：`出图头宽 / 参考头宽 = 0.24×` 比「看起来不像」有用一百倍，也是让用户接受「换工具」的唯一依据。

---

## 6. 换脸只搬「身份」，不搬「状态」

实测：源 = 疲惫素颜特写、目标 = 干净全身 → 脸和头发都换过去了，黑眼圈、妆感、皮肤光泽一项没跟过去。

机制：`head_swap:` 换的是**整个头部区域**（含发际线、发丝、皮肤纹理、表情、瞳色），所以发型必然跟着换，属于「头」的状态也被源像素覆盖；属于「身体 + 环境」的状态（姿态、服装、光照、背景、身体皮肤）永远留在目标图。

推论：**同一个人 × N 种状态 = N 次生成 + N 次换脸**，不是 1 次生成 + 换 N 张脸。状态写在生成端的提示词或参考图里，别指望换脸搬运。

## 7. 两张图的比例与像素

- **同画幅比例**（1:1 ↔ 1:1、9:16 ↔ 9:16）对齐误差最小；比例不同时头区在两图里占比不同，脸型会漂。
- 两边长边 **≥ 1024**；低于 1088 会把 1–2 px 的特征（痣、发丝缺口）糊没 —— 是糊不是抹掉，抬尺寸能回来。
- 参考图**不大于**目标（作者实测「参考比场景大」是最差设置），但也**不必压到 512–768** —— 那条是给 9:16 全身目标用的；1:1 特写线取参考边长 ≈ 目标的 60–100%。

---

## 5. 什么时候直接判死

- 比值 < 0.5 → 换构图或换工具，别调措辞。
- 同一处连败两轮、且**失败方式每次不同**（白模关节残留 / 衣服串成米白 / 塌成黑 T 黑裤）→ 这是「整图重绘 + 像素不足」的必然表现，不是提示词能收敛的。此时给结论与代价，不要再交第 N 版提示词。
