# MiniMax H3 官方提示词资料 · 出处与引用

写 H3 提示词时的**权威依据**都在这一个仓库里；这一页记的是「哪个文件管什么」以及「怎么把出处交出去让对方能自证」。

## 一、仓库与结构

- `MiniMax-AI/MiniMax-H3`，分支 `main`（注意：不是 `MiniMaxAI/…`，那个名字是 404）。
- 提示词相关全部在 `skills/` 下：**1 个语法技能 + 8 个风格生成器**。
- 同一份 `h3-prompt-writing` 在 `.agents/skills/` 与 `.claude/skills/` 下各有一份镜像，内容相同。
- **别指望从根 README 点进 `skills/`**：根 README 讲的是模型/权重，不链技能目录。找不到时直接给路径或 raw 链接，不要让人顺着页面点。

| 文件 | 管什么 |
|---|---|
| `skills/h3-prompt-writing/SKILL.md` | 入口：T2VA / I2VA / FL2VA / L2VA / Ref2VA 路由 + 输出规则 |
| `skills/h3-prompt-writing/references/base-en.txt` | **基础模式语法**：三种核心字段、运镜词表（类型/幅度/速度）、说话人 ID 与 `<d>`、`<scenetrans>`/`<cutoff>`、声音两段 |
| `skills/h3-prompt-writing/references/ref-en.txt` | **Ref2VA 六段语法**：`subject_definitions` → `summary` → `retention_analysis` → `detailed_description` → `overall_soundscape` → `non_diegetic_music`，四种参考标签与四个关系标记 |
| `skills/3d-animation-short-generator/references/shot-table-spec.md` | 六列分镜表 + **每秒五要素** + STEP 5.5 六项自检门（本库 「A 式逐秒写法」的来源） |
| `skills/3d-animation-short-generator/references/storyboard-guidelines.md` | 分镜文档结构、per-panel 四象限、`[BEAT]` / `[HANDOFF → …]` 标记、铅笔分镜三次降级 |
| `skills/3d-animation-short-generator/references/qc-checklist.md` | 成片质检项 |
| `skills/3d-animation-short-generator/references/model-selection.md` | 模型选型与分辨率 |
| `skills/3d-animation-short-generator/references/fallback-policy.md` | 生成失败时的降级顺序 |
| `skills/README.md` | 9 个技能的分工表 |
| 其余 7 个生成器（`brand-promo` / `co-op-game-intro` / `handdrawn` / `minimalist-product-ad` / `music-video-subtitle` / `paper-collage` / `papercraft`） | 各自的风格锁与模板，多数带 `.cn.md` 中文版 |

## 二、引用纪律（贴给用户或另一个 AI 时）

1. **钉 commit SHA，不给 `main`**：`main` 会漂，对方明天打开就对不上。
2. **给 raw 地址**，一行就能验：`https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/<sha>/<path>`。
3. **带字节数与 sha256**（至少前 16 位）：对方 `curl | wc -c` 就能自证，不必信任何一方。
4. **原样转录**：不改写、不节译、不改文件名。要精简就给「节选 + 原文位置」，不要重写一份「差不多的版本」。

## 三、对方说「找不到这个文件」时

按这个顺序查，不要凭记忆断言路径：

1. `curl -s https://api.github.com/repos/<owner>/<repo>` → 200 才算仓库在；
2. `curl -s "https://api.github.com/repos/<owner>/<repo>/git/trees/HEAD?recursive=1"` → 在树里 grep 真实路径；
3. 常见原因：仓库改名、目录挪过、文件在 `.agents/` / `.claude/` 镜像里、或对方用的是代码搜索（需要登录才索引）。

## 四、语法与叙事的边界

- 本文件只解决**出处与语法**；「怎么写出电影感」在 `cinematic-narrative-h3`，两者不要混写。
- 官方明确劝退 `cinematic` 这类抽象词（`base-en.txt` 的 Tips），写实画质句官方**没有** —— 那是本库自建的风格锁，别记成官方要求。
