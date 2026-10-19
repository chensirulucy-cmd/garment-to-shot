# 02 · 幽灵服装台（文生图线 · 三件套骨架）

> **状态**：✅ 已验证（`00393` 修身三件套单次成功）；⚠️ 直筒及其他派生款需各自验收。
> **线**：Qwen-Image 2.1 **文生图线** —— 9 节点、**无 `LoadImage`**、`TextEncodeQwenImage21` 只有 `prompt`/`negative_prompt`；尺寸由 `ResolutionSelector`（9:16 · 1.0MP · multiple 8）喂 `EmptyLatentImage` 得 **768×1376**；30 步 / cfg 3.5 / euler-simple / denoise 1.0，seed `919066758927647`
> **逐字原文**：`prompts/02-ghost-set/T2I-00393-positive.txt` / `T2I-00393-negative.txt`
> 单张幽灵台不是多视角服装板；需要服装板时读 [服装板骨架](../skills/character-asset-pipeline/references/02-garment-board.md)

## 先选版本（按输入图：有图走编辑线，无图走本文件）

| 输入 | 用哪份 | 文件 | 取证 |
|---|---|---|---|
| **有参考图** · 一件（连衣裙/连体裤） | **A 版**（编辑线） | `02a-ghost-one-piece.md` | `00449 / 00446 / 473 / 474` |
| **有参考图** · 上衣 + 下装，不叠穿 | **B 版**（编辑线） | `02b-ghost-two-piece.md` | `00453 / 00454 / 00455` |
| **有参考图** · 上身叠穿 2–3 层 | **C 版**（编辑线） | `02c-ghost-layered.md` | `00470 / 00472` |
| **无参考图** · 纯文字生成 | **本文件**（文生图线） | `02-ghost-set-trio.md` | `00393` |

- 编辑线的出图尺寸**跟随输入图按 32 对齐**（1200×1600→1216×1600）；`ResolutionSelector` 被 `ComfySwitchNode(switch=False)` 旁路，调它无效
- 三份编辑线模板都是「标准模式（逐字成品）+ 骨架版（槽位）」两套写法，换服装只动槽位
- **⛔ 不要混用**：A 版负向含 `two-piece set, split into a top and a skirt`，用在两件套上会把两件合并；C 版的领口句一旦写成 `nothing inside`，内搭会整层消失
- 全部取证：`evidence/2026-10-19-ghost-ABC-baseline.md`

## 变量与骨架

保持顺序：定调 → 三件清单 → 隐形身体 → 视角与细节 → 廓形 → 光背景 → 限定件数 → 色彩 → 无字。

| 变量 | 从哪里填 | 同步项 |
|---|---|---|
| TOP / BOTTOM / SHOES | 实际来源图可见的版型、颜色、结构 | 不得凭空加部件 |
| 空开口与细节清单 | 该服装实际存在的领口、袖口、裤脚等 | 无袖就不保留长袖袖口词 |
| 廓形、落点 | 所选腿型、松量、长度与穿法 | 负向不得禁自身腿型 |
| 色彩保真 | 来源颜色与可见质感 | 不把黑衣/黑鞋列为通用禁词 |

```text
Photorealistic costume-department garment reference photograph of an invisible-mannequin display, presented in a warm, soft commercial studio light:

[TOP: {{上装完整规格}}], [BOTTOM: {{下装完整规格}}], [SHOES: {{鞋完整规格}}].

The outfit appears worn by an invisible body with natural hollow volume: {{与实际衣物对应的空领口、空袖口、空腰头、空裤脚与成对鞋的描述}}. No person, no mannequin, no dress form, no display figure, no body, no torso, no arms, no hands, no legs, no feet, no toes and no skin anywhere in the frame.

Front view, the complete outfit from {{衣物顶端}} down to both {{鞋}} filling most of the frame height, with only a small margin above {{衣物顶端}} and below the soles: visible are {{该款实际结构与工艺清单}}, with {{可见面料纹理}} readable.

The silhouette is {{廓形、腿型、长度、上装是否塞入下装的完整描述}}.

Plain warm light-grey seamless studio background, soft even studio light from the front-upper left, a gentle contact shadow under {{鞋}}, accurate colour reproduction, and clear tonal separation between {{三件服装及各自颜色}}.

The outfit consists of {{这三件}} only: no bag, no belt, no jewellery and no other accessory anywhere in the frame.

{{逐件颜色和纹理保真句}}.

No text, no labels, no watermark.
```

## 负向

```text
human model, person, character, face, head, skin, hands, arms, legs, dress form, mannequin body, mannequin face, mannequin head, visible anatomy, hanger, hook, flat lay, folded garment, cropped collar, cropped hem, cropped shoes, missing footwear, {{与本款相反的腿型、袖长、穿法和色彩}}, redesign, different outfit, altered costume, invented clothing, changed colours, colour cast, plastic-looking fabric, illustration, concept art, sketch, anime, cartoon, CGI, 3D render, text, labels, watermark, busy background, dramatic lighting, harsh shadows, low resolution, blurry details
```

## 不变量与判据

定调、隐形身体要求、完整单幅展示、只含指定三件、无字等结构保持。三件清单、廓形、颜色段是主要控制块；文字不是生成保证。

交付时填满所有变量，整段给出正负向；检查件数、无人、腿型/长度、配色与鞋。00393 原图观察为修身、及踝、无额外配件；腰位偏高、上装略宽松。不能据这一张宣布任何指标“一句话能锁”。单件连衣裙不要硬套三件清单，应使用对应单件模板。
