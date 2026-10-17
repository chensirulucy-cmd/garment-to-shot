---
name: cinematic-narrative-h3
description: "Use when writing a cinematic narrative MiniMax H3 prompt."
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
metadata:
  hermes:
    tags: [video, minimax, h3, narrative, directing, shot-table]
    source: official MiniMax-AI/MiniMax-H3 -> skills/3d-animation-short-generator (skeleton extracted)
---

# 电影级叙事 × MiniMax H3

一类任务：要"**电影感 / 叙事感**"的 H3 视频（不是产品广告、不是 MV、不是单张图）。
骨架提取自**官方 `3d-animation-short-generator`**（官方 8 个风格技能里唯一带完整叙事流水线的一个）：把它的 Pixar 风格锁与铅笔故事板，换成本线用的**写实风格锁**与关键帧资产。

## When to Use

- 要叙事短片、多镜有事件、有连续性的视频；或成片被说"**像摆拍 / 像广告 / 没有电影感**"。
- 要定位"电影感"缺在哪一层，并把缺的那层写进提示词。
- 不适用：H3 字段语法（走 `minimax-h3-video-prompt`）；多来源合成静帧（走 `multi-source-image-composition`）；带货分镜（走 `finance-ip-short-video`）。

## 三层分工（不要混写）

| 层 | 归谁 |
|---|---|
| **语法**（字段名/顺序/时间戳/参考标签） | `minimax-h3-video-prompt`（已与官方 base-en / ref-en 同版） |
| **叙事骨架**（本技能） | 风格锁 → 资产卡 → 六列分镜表 → 自检门 → 模型卡 → 组装回退 |
| **验收**（渲染后逐秒核） | `ai-video-forensics` |

## "电影感"五层（先定位缺哪层，再动笔）

1. **运镜** = 类型 + 幅度 + 速度，写进动作句，不堆标签。
2. **景别** = 必须交替（特写/大特写与其他景别交替，禁止连续重复景别）。
3. **质感** = 物理描述（光从哪来、性质、色温、材质、影子）。**永不用** `cinematic / beautiful / 8K / 高级感`。
4. **摄影词** = 带使用条件（荷兰角只用在失衡/惊悚/闹剧节拍；浅景深要与场景同层）。
5. **导演层**（最常缺）= ①每秒五要素 ②视线对象 ③动机性运镜 ④连续性交接 ⑤hook 分布。

## 流水线 P0–P7

| 步 | 产出物 | 硬规则 |
|---|---|---|
| P0 | 规格卡 | 画幅、时长（单镜 ≤15 s，超则拆）、有无台词、平台；确认后再动工 |
| P1 | **风格锁**（一句，贯穿全片） | 写实线模板见下 |
| P2 | **资产卡** | 角色卡（身份锚图/LoRA + 触发词）+ 场景卡（地标 + **屏幕相对位置** + 光基线） |
| P3 | **六列分镜表** | 列序固定：Shot ID & Duration｜Continuity Handoff｜Reference Anchors（Fixed Landmarks / Character Positions / Exited Character Status / Lighting Baseline）｜Hook Type｜Shot Description + **Per-Second Directives**｜Audio & Dialogue Track |
| P4 | **自检门**（六项，不过不进下一步） | ①每镜有 Hook Type，每连续三镜至少一个 reveal/reversal/callback，首尾镜强 hook ②单镜 ≤15 s ③每镜重要角色 ≤3 ④空间锚与光基线继承，变更要显式标注 ⑤**每秒五要素无空隙** ⑥Continuity Handoff 逐行连成一条链 |
| P5 | 编译成 H3 | 单帧首帧→I2VA；首尾帧→FL2VA；带资产参考→Ref2VA 六段；纯文字→T2VA |
| P6 | 验收 | 逐秒抽帧核（`ai-video-forensics`）；先走失败回退再改提示词 |
| P7 | 组装 | 声音在 P3 就排好，不是后期补 |

**每秒五要素**（P3 每一秒都要齐）：①动作/姿态/表情 ②机位运动 ③空间位置 ④声音线索 ⑤交接给下一秒或下一镜。

## 官方有 / 没有的（对官方 61 个文件 grep 实测；本技能其余框架属方法论综合，不是实验结论）

- 官方**有**：景别交替规则、荷兰角使用条件、运镜写进每秒指令、**光影基线**（key/fill/rim + 跨镜继承）、微表情与表情路径、旁白的 "lips closed" 标记、情绪前提卡。
- 官方**没有**：写实画质句（真实/不油腻/自然皮肤/无 HDR/无过度锐化）—— 官方默认是风格化 3D，写实反而写进它的负向；减少 AI 塑料感只有 MV 技能的**后期**手段（35mm 颗粒 + 统一 LUT）。
- 官方**没有**通用情绪禁区清单（如"不要暴躁/伤心"）—— 只能自己写进风格锁与每秒指令。

## 写实线风格锁模板（一句，贯穿全片）

`Live-action, real available light, natural skin with visible pores and no beauty smoothing, matte finish with no oily highlights, true-to-life colour, no over-sharpening and no HDR glow.`
（要手机随手拍感就换成 `Photographed like a real smartphone rear-camera recording:` 开头；两种都不要写 `cinematic`。）

## 下笔前最后一遍（每镜）

- **视线对象**是谁/什么？看镜头 = 广告语言；看场景里的对象 = 叙事语言。
- **机位为什么动**？（由动作或情绪驱动，不是装饰）
- 这一镜的**事件**是什么？（只有"抬头微笑"这种 = 摆拍）
- 景别与前两镜是否重复？hook 与前两镜是否同为弱？
- 声音线索在每一秒都写了吗？
- 镜头前无对白；画外旁白必须标 **lips remain completely closed**。
- 情绪方向（要什么/不要什么）用**肯定句**写进风格锁或每秒指令（H3 无负向）。

## 病灶对照表

| 现象 | 病灶 | 补法 |
|---|---|---|
| 像摆拍 | 单事件 + 单景别 + 固定机位 + 视线落镜头 | 给它事件、景别交替、动机性运镜、视线落在场景对象上 |
| 像广告 | 低光比 + 背景干净 + 人物居中直视 + 微笑收尾 | 加可用光来源与明暗比、前景遮挡、非中心构图 |
| 假 / 塑料 | 写了 cinematic / 8K / 高级感 | 换物理描述 + 上面那句风格锁 |
| 跨镜漂移 | 缺资产卡或空间锚继承 | 补 P2 与 P4 第 4 项 |

## 边界

- 不重复官方语法（引用 `minimax-h3-video-prompt`，不抄写）。
- 官方 8 个风格技能里只有 `3d-animation-short-generator` 是叙事片；要某品类风格锁时再去对应技能取那一段。
