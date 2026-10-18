# 模板 · 角色四视图（角色板）

> **状态**：✅ 已验证（00307 / 00308 / 00321 / **00418**，以「正确产出过无头」的那版原文为准）
> **工作流**：Qwen-Image 2.1 **编辑**线（两支 KSampler：478 服装板 → 515 角色板）· 30 步 · cfg 3.5 · euler-simple · denoise 1.0 · 16:9 · 2 MP
> **本页只讲角色板（515）**；服装板见 `02-ghost-set-trio.md`。

## 一、三槽

| 槽 | 放什么 |
|---|---|
| <image1> | 四格预留画布 `four-view-shoulder-cut-no-neck.png`（前三格无头、第四格是脸位） |
| <image2> | **人物参考图**（人像模块那张特写，直接接进来，提示词里不描述她） |
| <image3> | 服装板（478 的产出，直连） |

## 二、骨架（整段，只换两个 `{}`）

```text
Edit the four-figure sheet in <image1> into a finished character reference sheet: keep <image1> as the canvas, with its four-panel layout, the width and height of each panel, the camera height, the plain white background, the soft even studio light and the faint contact shadows under the shoes all exactly as they are, and change only the heads and the outfit. The leftmost panel is the full-length front view of the woman from <image2>, the second panel is the same woman seen from directly behind, and the third panel is the same woman in true side profile, each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it, and each keeping the stance, position and scale of the corresponding figure in <image1>; her body build, height, skin tone and hands come from <image2>. The fourth panel is a large frontal face-and-shoulders portrait of that same woman, filling its panel from just above the crown of her head down to the base of her neck so her face dominates the panel, framed and scaled exactly like the fourth figure of <image1>; her facial identity and hair are those shown in <image2> exactly as <image2> shows them, and this panel is the only one that contains a head or a face. In all four panels she wears one outfit taken from <image3>: {{服装名词段}}. {{颜色保真句}} Nothing else is added, removed, restyled or re-lit.
```

## 三、变量只有两个

| 变量 | 写什么 | 不能写什么 |
|---|---|---|
| `{服装名词段}` | 件数 + 版型 + 关键结构（领型/袖长/腰/下摆/鞋），**全部用肯定陈述** | ❌ 否定词（`no waist seam` / `no belt` / `no pocket`）—— 模型把 "no X" 当概念，反而画出 X |
| `{颜色保真句}` | 每件一个颜色值 + `stays / never turns …` | ❌ 新增颜色名之外的东西 |

## 四、不变量（原样粘，一个字不改）

1. **前三格无头**那句：`each of the three standing figures ending at the top of the shoulders with the collar of the garment closing the top edge and no head, no face and no hair above it`
2. **只有第四格有头**那句：`and this panel is the only one that contains a head or a face`
3. 第四格的身份只写抽象词：`her facial identity and hair are those shown in <image2> exactly as <image2> shows them`
4. 画布锁定句（`keep <image1> as the canvas … camera height … plain white background`）
5. 收尾句 `Nothing else is added, removed, restyled or re-lit.`

## 五、「脸词外溢」这条已被推翻（2026-10-19 反证）

旧结论：`her skin condition` / `her expression` 会让前三格长出人头。

**反证**：`00418`（白长袖 + 浅蓝牛仔）用的正是这句完整写法 ——

`her facial identity, her skin condition, her expression and her hair are those shown in <image2> … with nothing added and nothing restyled`

结果**前三格干净无头**。而 `00416`（奶油连身裙）同样的写法 → 三格冒头。

| 样本 | 服装 | 含 skin/expression | 结果 |
|---|---|---|---|
| 00402 | 奶油连身裙 | 含 | ✅ 无头 |
| 00403 / 00410 / 00411 / 00416 | 奶油连身裙 | 含 | ❌ 冒头 |
| **00418** | 白长袖 + 浅蓝牛仔（两件式） | 含 | **✅ 无头** |

**现在的结论**：脸词**不是**主因；主因是**服装类型**（两件式稳 / 一件式连身裙不稳），见第八节。这句写法可以照用，但**别再用它解释冒头**。

## 五之二、锚点 token 必须裸写（2026-10-18 更正）

`<image1>` / `<image2>` / `<image3>` 是**锚点 token**。交付时若被写成 `` `<image1>` ``（反引号）、`**<image1>**`（加粗）、或被换行拆开，模型收到的就只是**普通文字**，槽位绑定失效 —— 它会按文字自己发挥，四格里就都会长出人头。

实测对照（同一支工作流、同一套参数）：

| 交付写法 | 结果 |
|---|---|
| 裸 token：`Edit the four-figure sheet in <image1> …` | ✅ 前三格无头（00308） |
| 8 处 token 被包成 `` `<image1>` `` | ❌ 前三格出现人头（本轮） |

**规则**：从仓库复制提示词时，token 前后不留任何 markdown 修饰；在聊天里交付也一律裸写，我不用反引号包裹。

## 六、判据（四条）

1. 前三格肩上**没有头**、第四格**只有一个头**
2. 衣服四格一致（件数/颜色/鞋），无混搭
3. 剪裁与留白没动（和 <image1> 逐格对齐）
4. 第四格的脸 = <image2>，不是"另一个人"

## 七、负向

```text
three identical front views, all three standing panels showing a front view, identical panels, missing back view, missing side view, a head in the first three panels, a face in the first three panels, hair falling over the shoulders in the first three panels, head added above the shoulders, repaired crop, figure rescaled to fit the whole body, different person between panels, different face between panels, different hairstyle between panels, different outfit between panels, mixed outfits, wardrobe from <image2>, mannequin appearance, white mannequin material, featureless face, a second person, extra limbs, extra fingers, malformed hands, fused garments, warped buttons, text, captions, labels, watermark, panel borders, comic panels, frame lines, low resolution, blurry, plastic skin, waxy skin, illustration, painting, anime, cartoon, CGI, 3D render
```

## 八、同一件衣服连试两次不行就换，别在这一张图上硬磕（2026-10-19）

**观察到的**（只对这几件具体衣服成立，不能推广成"某类服装都不行"）：

| 衣服 | 结果 |
|---|---|
| 黑针织上衣 + 米白 A 字裙（00307 / 00308） | ✅ 无头 |
| 香槟缎面睡衣上衣 + 长裤（00321 / 00325） | ✅ 无头 |
| 白长袖 + 浅蓝牛仔 + 小白鞋（00418） | ✅ 无头 |
| 奶油短袖 **T 恤连身裙**（00402 / 00403 / 00410 / 00411 / 00416） | ⚠️ 00402 中过一次，其余冒头 |

**不能得出的结论**：不能说"一件式连身裙都不行"。上面失败的 5 次**用的是同一件衣服**（同一张幽灵台、同一张画布、同一套骨架），变量只有 run 次数 —— 所以更可能是**这一张服装图本身**（圆领位置正好压在裁切线上、版型太素）不适合这个画布，而不是"连身裙这一类"有问题。样本量 1 件，不够下类结论。

**规则（写死）**：

1. 同一件衣服**连试两次**还在冒头 → **换衣服 / 换画布**，不要在那一张图上继续加实验。继续堆只会在一个本来就跑不通的输入上消耗时间。
2. 一件式连身裙第一次就冒头时，直接换**胸口裁切画布**（前三格从顶部再裁 ~17%，领口不入画），不要先改提示词。
3. 只有换过 ≥3 件**不同**的连身裙、都失败，才允许写"连身裙这一类不稳"。

