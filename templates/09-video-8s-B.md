# 模板 · 8 秒单镜 · 连贯写法（B 式 · 默认）

> **用途**：一条 8 秒单镜视频提示词（H3 Ref2VA）。只填变量，不动结构。
> **状态**：✅ 当前默认（实测 00061，用户选定）。
> **本模板不含任何案例内容** —— 具体场景/服装/人物填在变量位里，案例记录放 `cases/`。

---

## 一、变量表（填完再动笔）

| 变量 | 必填 | 说明 | 常见坑 |
|---|---|---|---|
| `{{人物}}` | ✅ | 身份：脸锚图里那个人；有 LoRA 时触发词**内联在锚句主语里** | 触发词独立成行 → 脸变通用；正文复述五官 → 脸被重画 |
| `{{身份补充}}` | ◻︎ | 无 LoRA 时才写五官（脸型/眉/眼/鼻/唇/肤色/发） | 有 LoRA 还写五官 = 跟 LoRA 抢身份 |
| `{{服装}}` | ✅ | 逐件枚举：件数 → 品类 → 颜色（带修饰词）→ 材质 → 结构细节 → 鞋 | 只写"上衣"→ 模型自由发挥下装；漏鞋 |
| `{{服装素材类型}}` | ✅ | 服装是从哪种素材给的（四联排 / 单件产品图 / 实拍） | 忘了写"版式/白底/模特不出现"→ 版式渗透 |
| `{{场景}}` | ✅ | 场景卡：3–6 个地标 + **屏幕相对位置** + 光基线 | 写成散文 → 无法跨镜继承 |
| `{{时长}}` | ✅ | 秒数（H3 单条 4–15s） | 写进正文 = 无意义，时长只在参数里 |
| `{{景别}}` | ✅ | 起始景别（中景 / 中近景 / 全身坐姿…） | 起始景别太大 → 脸像素不够 |
| `{{机位}}` | ✅ | 眼高 / 平视 / 略俯 | 不写 → 模型自己选，常偏高或偏低 |
| `{{事件}}` | ✅ | **一件有结果的事**（不是"抬头微笑"这种半个动作） | 只有情绪没有事件 = 摆拍 |
| `{{情绪走向}}` | ✅ | 用**肯定句**写"从 A 到 B"（H3 无负向） | 写"不要生气"= 反向提示，效果差 |
| `{{运镜}}` | ✅ | 类型 + 幅度 + 速度，**全片只允许一种** | 堆两种运动 → 抖 |
| `{{声音}}` | ✅ | 环境底噪 + 动作声 + 非语言人声（1–4 句） | 把台词写进 soundscape（属于 multimodal） |

---

## 二、固定不变量（一个字都不要改）

1. **画质锁定句**（写实线，直接粘）：
   `Live-action, real available light, natural skin with visible pores and no beauty smoothing, matte finish with no oily highlights, true-to-life colour, no over-sharpening and no HDR glow.`
2. **脸的锁定句**：`Her face remains identical to <Subject 1> in every frame.`
3. **头发锁定句**：`Her very long jet-black hair keeps the exact same length, centre part and style, with no flickering and no morphing.`（按 IP 发型改）
4. **顺滑句**：`The motion stays buttery smooth and continuous: constant speed, no stuttering, no frame jumps.`
5. **无台词句**：`She says nothing and her lips stay closed.`（若有画外音，改成 `her lips remain completely closed`）
6. **无文字句**：`No lettering appears anywhere in the frame.`
7. **参考声明**：`All references are references only; none is aligned to any moment of the video.`

---

## 三、骨架（复制后只替换 `{{ }}`）

```
subject_definitions:
<Subject 1> is the {{人物}} defined by the portrait — {{身份补充（无 LoRA 时写；有 LoRA 写触发词内联）}}. The portrait defines the face, hair and skin only, so its plain background and any garment it shows never appear in the video.
<Subject 2> is the {{服装}} shown in {{服装素材类型}} — {{逐件枚举：件数、品类、颜色（带修饰词）、材质、结构细节、鞋}}. The sheet defines these garments only, so its layout, its background and any model in it never appear in the video.
<Subject 3> is the {{场景}} described here: {{场景卡：地标 + 屏幕相对位置 + 光基线}}.

summary:
[reference generation] The target video is one continuous {{时长}}-second shot of <Subject 1> in <Subject 3> wearing <Subject 2>, {{事件}}. All references are references only; none is aligned to any moment of the video.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - her facial identity, hair, skin tone and build stay exactly as the portrait defines them.
<Subject 2> (appears in [Shot 1]): fully_preserved - {{服装}} keeps its exact colour, cut, sheen and garment count.
<Subject 3> (appears in [Shot 1]): partially_preserved - {{地标清单}} keep their positions and their light while the camera moves.

detailed_description:
Live-action, real available light, natural skin with visible pores and no beauty smoothing, matte finish with no oily highlights, true-to-life colour, no over-sharpening and no HDR glow.

[Shot 1] The frame opens as a {{景别}} at {{机位}}: <Subject 1> {{起始姿态 + 视线落在哪个场景对象上 + 手上的道具}}, with {{前景/背景各一个地标}} and {{光从哪来、落在哪}}. {{动作链第一段：触发}}. {{动作链第二段：反应}}. {{动作链第三段：结果}}. The camera {{运镜：类型 + 幅度 + 速度}} throughout, and {{运镜结束后画面落点}}. Her face remains identical to <Subject 1> in every frame, and {{头发锁定句}}. The motion stays buttery smooth and continuous: constant speed, no stuttering, no frame jumps. She says nothing and her lips stay closed, and no lettering appears anywhere in the frame.

overall_soundscape:
{{环境底噪}}, {{动作声 1–2 个}}, {{非语言人声（呼吸/轻笑）}}. No dialogue and no other voices are heard.

non_diegetic_music:
N/A.
```

---

## 四、自查（发出去之前逐条打勾）

- [ ] 有**一件有结果的事**（不是只有一个表情变化）
- [ ] **视线落在场景里的对象**上，不是落在镜头上（落镜头 = 广告语言）
- [ ] 全片**只有一种运镜**，且写明了幅度与速度
- [ ] **景别只变一次**（或不变），没有来回跳
- [ ] 每一句都在描述**看得见的东西**，没有 `cinematic / 高级感 / 8K`
- [ ] 时长与景别匹配：**起始景别越大，脸越小** → 全身镜别指望脸保真
- [ ] 声音段落里**没有台词**；台词只进 `detailed_description`（且本线默认无台词）

## 实测参数（00060 / 00061 内嵌元数据，2026-10-19 读出）

| 项 | 值 |
|---|---|
| 一采分辨率 | `9:16 · 0.5 MP · multiple 32` |
| 二采 | `MinimaxH3LatentUpscaler3D`：`scale by multiplier 1.5`、`align 32`、`force_unload true`、`cuda / fp16` |
| 成片 | **832×1440 · 8.00 s · 192 帧 · 24 fps · 带音轨** |
| 调度 | `BasicScheduler` steps 10 / denoise 1.0 / simple；`SplitSigmas` step 6（一采 6 步、二采 4 步） |
| seed | `999`（RandomNoise） |
| 模型 | UNET `minimax_h3_fl2va_pruned_int8_convrot` · CLIP `qwen3vl_32b_minimax_h3_nvfp4_awq` · LoRA `minimax_h3_fl2v_turbo_8step_v1.0` 1.0 |
| 参考图 | `<Subject 1>` = 人像特写（`ComfyUI-Z-Image_00024_.png`）；`<Subject 2>` = 四视图板（`Qwen_image_2.1_00321.png`） |

**怎么自己核**：mp4 的 `format.tags` 里带 `prompt` 与 `workflow` 两段 JSON（`ffprobe -show_format` 就能看），二采是否真的跑了看节点 `263` 在不在、`mode.scale` 是不是 1.5。**别再从日志或 PNG 里找 —— 找不到。**
