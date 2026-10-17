# 上游改写器（原文抽取）

两个改写器都跑在用户的 ComfyUI 工作流里，提示词会先被它们改写再进模型。

- `t2i-image-prompt-rewriting-expert.txt` ← 从 00336 的 PNG 元数据 `PrimitiveStringMultiline.value` 抽出
- `edit-prompt-enhancer-v2.txt` ← 从 00341 的 PNG 元数据抽出

抽取脚本见 `docs/未验证清单.md` 末尾说明；原文可在本地 `F:\Sakura_Project\prompt_extract\` 复核。
