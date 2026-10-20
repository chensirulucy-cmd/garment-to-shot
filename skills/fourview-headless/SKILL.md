---
name: fourview-headless
description: "Use when preparing or diagnosing ComfyUI Qwen Image 2.1 stage 478 wardrobe-board and stage 515 four-view prompts: three headless standing views plus one portrait. Uses a fixed skeleton with covered-open, closed-collar, and exposed-shoulder slot profiles."
metadata:
  version: "1.0.0"
---

# 四视图无头提示词

**状态：✅ 515 已验证样本与固定骨架；478 保留已测文字，但三整装视图完整性有已知缺口。**

服装照片 → 478 服装板 → 515 一次生成完整四视图。不跳过 478，永久排除分格生成后拼接。输出前三格正/背/侧站立无头、第四格唯一人像。无头不等于缺肩缺手可以接受。

## 使用步骤

1. 确认服装源图、身份图和画布；按实际服装选择下表 profile。衣物细节从图片读取，不凭旧案例猜测。
2. 读取 [槽位规则](references/parameters.md) 和对应 `templates/families/*.txt`。515 固定正文在 [skeleton_515.txt](templates/skeleton_515.txt)，不随服装重写。
3. 填写配置：`family`、`subject`、`role`、`wardrobe`。role 与 wardrobe 的 `NEG_GARMENT` 是两个独立槽，不互相覆盖。结构示例见 [00510 案例](references/cases/00510.json) 的 `config`。
4. 用 [render.py](scripts/render.py) 组装并检查缺槽、未知槽、嵌套引用和代词。它只写文本，不调用 ComfyUI。命令在槽位规则中。
5. 交付完整 478 正/负向、515 正/负向；第一行说明改的是哪个阶段。若上游板未生成，明确 515 服装槽暂按源图准备，生成板后核对，不假称看过板图。
6. 对照测试固定参考图、种子和采样参数，记录实际变动字段；不靠重复抽图解决失败。成功文字保持原样，新措辞仅为候选。

## 选择 profile

先看肩部是否露肤，再看包肩衣服的领口闭合与开襟层次；不能只按“V形领口”这个名称选族。

| profile | 条件 | 当前证据 |
|---|---|---|
| `strap` | 肩部露肤、吊带/细带；保留肩臂手 | 00491；换款 00512/00513 |
| `vneck` | 肩部被衣物覆盖，外层开襟或 V 开口，保留实际内搭 | 00485；男装开衫 00507 |
| `round` | 当前默认仅闭合高领/包领；可带拉链、衬衫领细节 | 00510；细节变体 00501 |

普通圆领短袖的 00436 是旧提示词和旧画布成功样本；新统一骨架的普通圆领版本尚未验证。抹胸、露肩复杂结构等未覆盖款式，不自动声称等同已验证吊带。

## 接线与参数

- 478：480 服装源图 → 服装板；515 的 image3 接该输出。
- 515：image1 = `four-view-shoulder-top-enlarged.png`；image2 = 522 身份；image3 = 478 服装板。
- 30 steps、cfg 3.5、euler/simple、denoise 1.0，两段相同。
- 本批实际 seed：478 为 `810701216055607`，515 为 `744522349844629`。494/518 是连接的种子节点编号。
- 画布输入 2075×1184，当前 latent 路径按 32 对齐后输出 2080×1184；不以界面的闲置分辨率节点判断实际尺寸。
- 新画布是样本基线，不是无头的硬保护；00411 同画布仍曾冒头。
- 人像必须记录实际文件；00510/512 用对称证件肖像，00513 用清透白底。该对照只证明这组换身份未使头部回退。

## 验收范围与限制

检查前三格头颈/头发、肩臂手、视角、服装鞋履、第四格身份和版式。顶部空白或文字回放不能独立证明图像合格。

478 当前样本缺完整视角：00506/00511 缺明确完整背面；00508 第二个服装视图几乎消失。515 无头成果独立保留，不写成全流程全项通过。新板图仍按三整装视图检查，不能自行降低要求。

478 固定正文的 smooth/fine weave、无刺绣/文字等只保留当前已测写法，不保证适合刺绣、标识或所有材质。遇冲突先标为待测，不偷偷改固定正文。暗色细节/色彩、肩颈边缘自然度及后续视频接缝仍有局限，不自动增加昂贵试验。

[证据与纠错](references/evidence.md) · [验证范围](references/verification.md) · [已知问题](references/failure-catalog.md)。
