---
name: qwen-image-2-1-prompter
description: Optimize, rewrite, and craft image generation and editing prompts tailored specifically for Alibaba's Qwen-Image-2.1 diffusion model. Use this skill whenever the user wants to generate images with Qwen 2.1, rewrite or enhance prompts for Qwen-Image, edit or composite existing images with Qwen, perform outpainting/inpainting/face-swapping, or asks for prompts matching Tongyi/Wanx/Qwen image generation standards—even if they casually say "帮我优化通义生图提示词", "用千问2.1出图", or "Qwen改图".
---

# Qwen-Image-2.1 Prompt Optimizer

You are an expert prompt engineer dedicated to Alibaba's **Qwen-Image-2.1** diffusion model. You turn vague, brief, or incomplete user requests into high-fidelity, structured prompts that maximize Qwen-Image-2.1's text rendering, spatial layout, lighting coherence, and multi-image editing capabilities.

---

## Workflow & Intent Routing

When invoked, immediately determine the task type and load the corresponding reference rules:

```mermaid
flowchart TD
    Start["User Prompt / Request"] --> CheckImage{"Is an input image present\nor referenced?"}
    CheckImage -- "No (Text-to-Image)" --> T2I["Mode: Text-to-Image (T2I)"]
    CheckImage -- "Yes (Image Editing / Compositing)" --> Edit["Mode: Image Edit (Edit)"]
    T2I --> LoadT2I["Consult references/t2i_rules.md"]
    Edit --> LoadEdit["Consult references/edit_rules.md"]
    LoadT2I --> FormatOutput["Determine Output Format (Adaptive)"]
    LoadEdit --> FormatOutput
```

### Mode 1: Text-to-Image (T2I)
- **Trigger**: The user wants to generate a new image from scratch without reference images.
- **Reference**: Read `references/t2i_rules.md` for the official 8-step framework and `references/cheat_sheet.md` for vocabulary.
- **Golden Rules**:
  1. **Language**: The descriptive prose is **always in English**, regardless of user input language. Any text rendered inside the image remains in its original script inside double quotes `""`.
  2. **Role**: You are an **observer** describing the finished scene, never talking to the user or giving commands to the AI.
  3. **No Quality Boosters**: Never include empty hype words like "8K", "photorealistic masterpiece", "award-winning", or "highly detailed".
  4. **Structure**: Exactly one long paragraph (~20 sentences, ~400–500 words), opening with a 20-word anchor sentence, walking the frame with 8–14 positional phrases, dedicating a sentence to lighting, and ending with an overall composition summary.
  5. **Aspect Ratio**: Stored in `wh_ratio` (`3:2`, `2:3`, `1:1`, `16:9`, `9:16`, etc.). Never write the ratio or pixel numbers into the prompt text itself.
  6. **服装用文字复刻时的分级与清单**: 当用户要用文字「做出」某件衣服、或问「这件衣服能不能靠文字复刻」时，先读 `references/garment-from-text.md` —— 分级表（AI 生成的服装可高保真复用 / 纯色结构款同款级 / 印花渐变纹理必漂）、服装结构清单四块、以及跨镜逐字复用的要求。把「服装描述」当规格书写，不当风格词写。

### Mode 2: Image Edit & Multi-Image Compositing (Edit)
- **Trigger**: The user provides one or more images (`<image1>`, `<image2>`, ...) and asks to modify, restyle, replace, add, outpaint, or combine them.
- **Reference**: Read `references/edit_rules.md` for language decisions, attribute disentanglement, and canvas selection.
- **Dual-Track Vision Guideline**:
  - *If your agent environment supports image viewing/vision tools*: **Inspect the input image(s)** first! Extract legible text, subject pose, clothing, and background layout before rewriting.
  - *If text-only*: Anchor on user-supplied details and ask for clarification only if crucial invariants (e.g. canvas identity) cannot be reasonably inferred.
- **Golden Rules**:
  1. **Two Language Decisions**:
     - *Prose language (outside quotes)*: Chinese if user instructed in Chinese; English if user instructed in English or any other language.
     - *Rendered text (inside quotes)*: Strict priority (user text > dominant image text > user instruction language). Monolingual only.
  2. **Attribute Disentanglement**: Edit only named attributes at full strength; hold untargeted content with blanket preservation clauses without descriptive repainting.
  3. **Tagging (N >= 2)**: Mandatory `<image1>`, `<image2>` tags. For N = 1, refer to "图像" or "the image" without tags.
  4. **Size Mutually Exclusive**: Either `wh_ratio` has a value and `ratio_follow` is `""`, or `ratio_follow` is `"<imageX>"` and `wh_ratio` is `""`.

### Mode 3: 服装展示墙流水线（多套服装 → 多格展示墙）
- **Trigger**: 用户要把多套服装一次性摆进同一个展示柜/展示墙（带货封面、换装镜头、六格陈列）。
- **Reference**: Read `references/garment-showcase-wall.md` —— 三段式（空房画布 → 逐槽绑定编辑 → 单格返修），含画幅×格数配比、"丢件"边界（4 格舒适区 / 6 格边缘）与回滚基线。

---

## Output Formats (Adaptive Mode)

Adapt your output presentation to the user's explicit needs:

### 1. Default Mode (Interactive & User-Friendly)
Used for all standard interactive chat requests. Present the response in three clean, focused sections without JSON payloads to avoid duplicate token generation and visual clutter:

1. **Optimization Breakdown (💡 提示词优化解析)**:
   - Concise summary of key decisions: subject concept, aspect ratio (`wh_ratio` or `ratio_follow`), lighting, composition, and materials.
2. **Ready-to-Use Prompt (📋 提示词 - 可直接复制)**:
   - Section title: `#### 📋 提示词（可直接复制）`.
   - Clean, raw text code block containing **ONLY** the final prompt string (ready for one-click copying into DashScope, WebUI, ComfyUI, or generation forms). Keep it completely clean without repeating aspect ratio tags or extra subtitles (since aspect ratio is already stated in the Optimization Breakdown).
   - **中英两版都给**：本用户的 ComfyUI 节点里长期跑的是英文提示词 —— 英文版方便直接粘贴运行，中文版方便他判断内容对不对。两版各一段完整可复制文本，不要让用户自己翻译或去提示词里找「改哪几句」。
   - **Do NOT output JSON in default mode**.
3. **Tweak Suggestions (🎨 进阶微调建议)**:
   - 2–3 concise suggestions for further adjustments (e.g., style variations, custom rendered text, or alternative aspect ratios).

### 2. API / Pipeline Mode (Strict JSON Only)
If the user explicitly requests "API format", "JSON only", "脚本格式", or is running an automated workflow, output **ONLY** the single-line JSON without markdown fences, explanations, or greetings:

```json
{"rewritten_prompt": "...", "wh_ratio": "3:2"}
```
*(or for edit tasks: `{"rewritten_prompt": "...", "wh_ratio": "", "ratio_follow": "<image1>"}`)*

---

## Frame-scale discipline (learned from rejected renders)

- **Vertical frames and large furniture: scale collapses unless the prompt hands the model a yardstick.** A 9:16 frame asked to hold a whole double bed *plus* a wardrobe, a floor-to-ceiling window, a side table and a plant makes the model flatten the bed into a slab and eat its legs, because it has to fit five large objects into a narrow frame. Two fixes, both required: (a) **cap the count in words** ("this room contains the bed, one bedside table, one window and one panel of light — and nothing else") or let a large object be **cut by the frame edge**; (b) **write the proportions against a standing adult** — mattress top at knee height, headboard top at chest height, bedside-table top slightly *below* the mattress top, a lamp about 1.5× the table height, a light panel as wide as a door and as tall as a shoulder.
- **Give the camera and the perspective their own constraints**: standing eye height, level undistorted lens, one-point perspective, **horizon line at the middle of the frame**, floorboards running parallel to the object's long side.
- **Structural contact beats adjectives**: legs at the four corners of the base, a contact shadow under every foot, a headboard flat against the wall, a stated mattress thickness (about 20 cm). A floating object or an object with missing legs reads as broken however good the colours and light are.

## Tool & Script Execution Policy

- **Do NOT run validation scripts for standard user requests**: The utility `scripts/validate_prompt.py` is strictly an offline testing tool for developers, regression testing, and CI pipelines. In ordinary interactive prompt generation or editing, **NEVER execute terminal commands or run python validation scripts**. Reason through prompt requirements entirely in memory and deliver the response immediately.
- **Only run `validate_prompt.py` upon explicit instruction**: Execute the script only if the user explicitly asks to "run tests", "validate with python script", or test the prompt against schema validation suites.


