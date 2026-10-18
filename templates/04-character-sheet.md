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

## 五、铁律：脸词会外溢到整张画布

2026-10-18 实测：把第 4 格那句从

`her facial identity and hair`（旧，无头正确）

改成

`her facial identity, her skin condition, her expression and her hair … with nothing added and nothing restyled`（新，**前三格长出人头**）

原因：`skin condition` 和 `expression` 是**具体的脸词**，在整张画布范围内生效，不只作用于第 4 格。所以：

- 第 4 格只写 `identity` 和 `hair` 两个抽象词；
- `skin` / `expression` / `eyes` / `lips` / `face shape` / `makeup` 一律**不许出现在角色板提示词里**（要脸部状态，改 <image2> 那张参考图）。

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

## 八、服装类型判定：两件式稳、连身裙不稳（2026-10-19 实测）

| 服装 | 类型 | 结果 |
|---|---|---|
| 黑针织上衣 + 米白 A 字裙（00307 / 00308） | 两件式 | ✅ 无头 |
| 香槟缎面睡衣上衣 + 长裤（00321 / 00325） | 两件式 | ✅ 无头 |
| 白长袖 + 浅蓝牛仔 + 小白鞋（00418） | 两件式 | ✅ 无头（首次即中） |
| 奶油短袖 T 恤**连身裙**（00402 / 00403 / 00410 / 00411 / 00416） | 一件式 | ⚠️ 仅 00402 成功一次，其余三格冒头 |

**规则**：

1. **两件式**（上衣与下装分开写）→ 按本页骨架直接跑，稳。
2. **一件式连身裙** → 不稳定，同一份提示词同 seed 会一次无头一次冒头。二选一：
   - 同一份提示词**跑 3–5 张挑一张**（00402 证明能做对，是概率问题）；
   - 或把连身裙**改写成两件式描述**（同色上衣 + 同色半裙/同色下摆），再跑。
3. 换服装时只改**第 5 句（服装名词段）+ 第 6 句（颜色保真句）**，其余 6 句一个字不动。00418（385 词）与 00402（386 词）的差别只有这两处。
4. 不要用后期裁切/铺背景补救冒头 —— 已验证三种像素修法都留半截长发或硬边，不可交付。
