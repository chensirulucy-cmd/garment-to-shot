# 模板 · 幽灵服装台套装（上装 / 下装 / 鞋 三件套）

> **状态**：✅ 已验证 —— 正文逐字 = `00393`（白T + **修身**浅蓝牛仔 + 白板鞋，492 词，相似度 1.000）。直筒变体见「二·B」，⚠️ **无样本，未验证**。
> **工作流**：Qwen-Image 2.1 **编辑线**（`TextEncodeQwenImage21`，节点 `459:452`）· **cfg 3.5** · 30 步 · euler-simple · **768×1376**（00393 实测元数据）
> **用途**：一张衣服照/一组搭配 → 干净的「隐形人台」套装展示图，下游给服装板 / 展示墙 / 上身段当服装来源。
> **负向**：cfg 3.5 下**生效**（早期 00235/00241 是 T2I 线 25 步 / cfg 1.0，那时负向不生效，别混用）。

## 一、六段分工

| # | 段 | 写什么 | 写坏会怎样 |
|---|---|---|---|
| 1 | 定调句 | `costume-department garment reference photograph of an invisible-mannequin display` + 光 | 换成 "product photo" → 出成电商白底截屏 |
| 2 | 三件清单 | `[TOP: …], [BOTTOM: …], [SHOES: …]`，每件写：版型 + 领型/腰型 + 长短 + 闭合 + 工艺点 | 少写一件 → 自己补一件；少写工艺 → 细节糊成一片 |
| 3 | 隐形身体 | 圆肩、空领口、空袖口、空腰头、空裤脚、鞋成对站位；**逐个点名"没有人"** | 漏掉就长出人/模特 |
| 4 | 视角与可见细节 | 正面、领到鞋、留白多少、逐项列出要看清的工艺 | 不列 → 该有的细节没画出来 |
| 5 | 廓形 | 上装贴身程度 + 下装腿型（直筒/修身/阔腿）+ 有没有塞进腰头 | 不写 → 默认阔腿或超紧 |
| 6 | 光/背景 + 只含这几件 + 颜色保真 + 无字 | 浅灰无缝底、前上左柔光、接触影；三色不许互相串 | 不写颜色保真 → 白变米、浅蓝变深蓝 |

## 二、本版成品 = 00393 原文（逐字，492 词）

```text
Photorealistic costume-department garment reference photograph of an invisible-mannequin display, presented in a warm, soft commercial studio light:

[TOP: a plain white heavyweight cotton-jersey crew-neck long-sleeve T-shirt with a ribbed crew collar, a straight hem at the hip and long sleeves ending in narrow ribbed cuffs at the wrist], [BOTTOM: slim light-blue washed stretch denim jeans with a flat mid-rise waistband, a brass front button, a covered zip fly, belt loops, five-pocket construction, tonal topstitching and legs tapered to a narrow ankle opening], [SHOES: low-top white canvas court sneakers with a white rubber cupsole, flat white laces through five eyelets, a plain white canvas upper and no branding anywhere].

The outfit appears worn by an invisible body with natural hollow volume: rounded shoulders, an open empty neckline, two empty sleeve openings hanging at the wrist, an empty waistband with the jeans holding their hip shape, two empty leg openings with the ankle cuffs hanging loose above the shoes, and both sneakers standing as a pair in the position feet would occupy with nothing inside them. No person, no mannequin, no dress form, no display figure, no body, no torso, no arms, no hands, no legs, no feet, no toes and no skin anywhere in the frame.

Front view, the complete outfit from the crew collar down to both sneakers filling most of the frame height, with only a small margin above the collar and below the soles: visible are the shoulder seams, the ribbed crew collar, the sleeve cuffs, the straight tee hem, the jeans waistband, the brass button, the covered fly, the belt loops, the pocket edges, the tonal topstitching, the tapered ankle openings, and the sneakers' canvas uppers, laces, eyelets and cupsole edges, with the cotton knit weave and the denim twill both readable.

The silhouette is slim and easy: the tee sits close to the torso without pulling and drops straight over the top of the jeans without being tucked in, and the jeans follow the hip and thigh closely then taper to the ankle, so the outfit reads as a fitted white tee over slim light-blue jeans rather than anything oversized, baggy or flared.

Plain warm light-grey seamless studio background, soft even studio light from the front-upper left, a gentle contact shadow under the sneakers, accurate colour reproduction, and clear tonal separation between the white cotton tee, the light-blue denim and the white sneakers.

The outfit consists of the tee, the jeans and the sneakers only: no bag, no belt, no jewellery and no other accessory anywhere in the frame.

The white cotton must read as clean white cotton with visible knit texture and never as cream, grey or blue; the denim must read as light washed blue — never navy, never black, never grey — with the fade running down the front of each thigh; and the sneakers must read as clean white canvas and white rubber, not cream and not grey.

No text, no labels, no watermark.
```

## 二·B、直筒变体（⚠️ 未验证，无样本）

只把 `[BOTTOM: …]` 换成：

```text
[BOTTOM: light-blue washed straight-leg jeans with a flat mid-rise waistband, a brass front button, a covered zip fly, belt loops, five-pocket construction, tonal topstitching, legs cut straight from the hip to the hem with the same width at the ankle as at the knee, and a plain hem breaking once over the top of the shoe]
```

并把第 4 段的 `the tapered ankle openings` 改成 `the plain ankle hems`、第 5 段整段改成直筒写法（`falls straight to the ankle without tapering, with one soft break`）。

**同时必须换负向**：直筒版不能禁 `straight-leg`，改禁 `slim-fit jeans, tapered jeans, skinny jeans, wide-leg jeans, bootcut jeans`。

## 三、负向（配 00393 修身版；cfg 3.5 生效）

```text
human model, person, character, face, head, skin, hands, arms, legs, dress form, mannequin body, mannequin face, mannequin head, visible anatomy, hanger, hook, flat lay, folded garment, cropped collar, cropped hem, cropped shoes, short sleeves, missing footwear, tucked-in tee, baggy jeans, straight-leg jeans, wide-leg jeans, bootcut jeans, flared jeans, skinny jeans, ripped denim, distress, redesign, different outfit, altered costume, invented clothing, changed colours, the white tee rendered cream, the white tee rendered grey, the denim rendered navy, the denim rendered black, the denim rendered grey, the sneakers rendered cream, the sneakers rendered grey, colour cast, plastic-looking fabric, illustration, concept art, sketch, anime, cartoon, CGI, 3D render, text, labels, watermark, busy background, dramatic lighting, harsh shadows, low resolution, blurry details
```

## 四、判据（四条）

1. **三件齐**：上装 / 下装 / 鞋都在，没有多出第四件
2. **人不存在**：领口空、袖口空、腰头空、裤脚空，没有任何皮肤
3. **腿型与正文一致**：00393 = 修身（髋与大腿贴身，收到脚踝窄口）；直筒 = 膝到踝同宽；阔腿 = 外扩
4. **三色分离**：白不能发米、浅蓝不能发深蓝或灰、鞋白不能发灰

## 五、失败模式

| 现象 | 根因 | 修法 |
|---|---|---|
| 长出人/模特 | 第 3 段漏项 | 逐项补齐"no person / no body / no arms / no legs / no skin" |
| 裤型跑掉 | 第 5 段没写腿型，或负向禁错方向 | 正向写死 `slim / straight / wide`，负向禁**其它**腿型（别禁自己想要的） |
| 白T发米、浅蓝发深 | 第 6 段没写颜色保真 | 写 `never cream/grey/blue`、`never navy/black/grey` |
| 细节糊 | 第 4 段没列工艺点 | 逐项列：领口/袖口/腰头/五袋/走线/裤脚/鞋带 |

## 六、变量 / 不变量 / 真正决定画面的三句

**变量（换一身衣服只动这 4 个）**：① `[TOP]/[BOTTOM]/[SHOES]` 三件清单（每件的版型 + 工艺点）② 腿型词（`slim / straight / wide`）③ 三色保真句 ④ 背景布色。

**不变量（五条）**：定调句（costume-department / invisible-mannequin）｜ 第 3 段整段「隐形身体」｜ 第 4 段的工艺列举结构 ｜ 「只含这几件」句 ｜ 「无文字无标签」句。

**真正决定画面的三句**：

1. **三件清单** —— 决定有几件、什么款
2. **隐形身体段**（圆肩 / 空领口 / 空袖口 / 空腰头 / 空裤脚 / 鞋成对 / 逐项 `no person … no skin`）—— 决定**有没有人**
3. **颜色保真句**（`never cream/grey/blue`、`never navy/black/grey`）—— 决定三色会不会糊成一片

其余段落是修饰：改它们只改质感，不会改款。

## 七、00393（修身版）实测偏差

| 项 | 提示词写的 | 出图实际 | 判定 |
|---|---|---|---|
| 腿型 | 修身（收到脚踝窄口） | 修身 ✅ | 硬约束，能锁住 |
| 裤长 | `ankle cuffs hanging loose above the shoes` | 及踝、搭在鞋面上 ✅ | 可锁 |
| 腰位 | `mid-rise waistband` | 偏 **high-rise** | **软约束**，漂一档 |
| 上装松量 | `sits close to the torso` | 偏宽松 | **软约束**，漂一档 |
| 三件之外 | 无腰带无包 | 无 ✅ | 可锁 |
| 人体 | 无人无皮肤 | 无 ✅ | 可锁 |

**结论**：**腿型、裤长、颜色、有没有人 = 硬约束（一句话能锁）**；**腰位、松量 = 软约束（写死也会漂 ±1 档）**，要精确只能靠后续局部编辑，别指望一句提示词锁死。
