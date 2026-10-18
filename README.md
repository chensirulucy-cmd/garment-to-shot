# garment-to-shot

**Garment photo → normalized asset → character sheet → display wall → shot frames.**

面向 AI 短视频（电商/带货）的服装视觉素材生产：商家手里只有**服装照片**，我们要输出**一整套能进短视频的镜头素材** —— 衣服规范化成可复用资产、人物跨镜可识别、多套能一屏陈列并被点选、最后落到具体场景。

> 策略见 [`POLICY.md`](POLICY.md)：**一切提示词资料按「通用骨架」组织（模板 / 案例分离）；不做过高 GPU 成本的对照实验。**
> 状态标记：✅ 已验证 ｜ 🗄️ 暂定存档 ｜ ⚠️ 未验证 ｜ ⛔ 弃用

## 模块状态

| 模块 | 做什么 | 状态 | 证据 / 备注 |
|---|---|---|---|
| `01-canvas` | 场景画布（空镜） | ✅ | 00336（正向 = 交付版 498 词逐字一致） |
| `02-ghost-mannequin` | 服装照 → 幽灵服装台 | ✅ | 00235（基础）/ 00241（件数锁 + 鞋补全）；**三件套配方** 00393（白T + 浅蓝直筒牛仔 + 白板鞋）→ `templates/02-ghost-set-trio.md` |
| `03-two-source-merge` | 上装 + 下装/鞋 两源合并 | ✅ | 00315 |
| `04-character-sheet` | 角色四视图（角色板，三槽：画布 / 人物参考 / 服装板） | ✅ | 00307 / 00308 / 00321 / **00418** → `templates/04-character-sheet.md`（含「脸词外溢」铁律 + 服装类型判定：两件式稳、连身裙不稳） |
| `05-display-wall` | 六格陈列墙 | ✅ 维持现状 | 00339（n=1）。单格返修已弃用 → 要能改单格，改成「六格各自生成 + 拼墙」 |
| `06-tap-select` | 手指点选高亮 | ✅ | 00341 |
| `07-portrait-headshot` | **AI 人物建模特写**（写法指南：九段骨架 + 三旋钮 + 有/无 LoRA 双版） | ✅ | 00397（暖米·中分·LoRA 1.0）；对照 00390 / 00392（邋遢版）、00394（侧分·脸型漂移）→ `templates/07-portrait-headshot.md` |
| `08-worn-look` | 人物 + 服装 → 上身 | ⛔ **被 12 取代** | 两槽必失败（00319）。现走 `12-white-model-to-body` 两段式（00382 / 00383） |
| `09-video · A 版` | 8 秒单镜 · **逐秒编排**（官方六列分镜表骨架） | 🗄️ **暂定存档** | 00060。本案例 B 版更受欢迎；**换运镜/换题材时逐秒写法可能更优，保留待用，不淘汰** |
| `09-video · B 版` | 8 秒单镜 · **连贯写法** | ✅ 当前默认 | 00061，用户选定 |
| `10-single-cell-repair` | 单格返修（在编辑工作流里改一格） | ⛔ **弃用（2026-10-18）** | 编辑 = 整图重绘，**改一格必然重画全图**，每轮等于换一张，无法验收；替代 = **六格各自单独生成 + 拼墙**（零漂移） |
| `11-faceswap-head` | **换头**：人像特写的脸 → 全身照的身体（BFS LoRA） | ✅ 已验证 | 00367（euler）/ 00366（deis_2m）。衣服单通道 Δ≤5.2，脸被"网红化" → `templates/11-faceswap-head.md` + `cases/11-faceswap-2026-10-18.md` |
| `12-white-model-to-body` | **两段式**：服装照→服装板→真人全身（白模文生图先出姿势） | ✅ 已验证 | 00382 / 00383（+ 白模 00378–00381）。服装板尺寸随输入图；换姿势只在白模段 → `templates/12-white-model-to-body.md` + `cases/12-white-model-2026-10-18.md` |
| 换装/换场景远景 | — | ⛔ 弃用 | 脸像素预算不足，必漂 |
| 撞色受控 A/B（锁 seed） | — | ⛔ 不做 | GPU 成本 > 收益；"避开重复色"降为**软启发式**（见 POLICY 四） |

## 参数基线（实测元数据）

| 线 | steps | cfg | sampler | 尺寸 |
|---|---|---|---|---|
| 幽灵台（02） | 25 | **1.0**（负向权重 0） | euler / simple | 9:16 · 1.0 MP |
| 编辑（03 / 04 / 05 / 06） | 30 | 3.5（06 用 3.0） | euler / simple | 四视图 16:9 · 2.0 MP；展示墙 9:16 · 2.0 MP |
| **换头（11）** | **8**（配 Pruna 蒸馏；无 Pruna 改 20–30） | **1.0** | **euler / simple**（`deis_2m` 本机不存在） | **目标 1088×1920 不缩**（00373）· 参考 576–1088 · 约 80 秒 |
| **两段式（12）** | 30 | 3.5 | euler / simple | 服装板随输入图（00254 → 1216×1600）· 真人 9:16·2MP（1088×1920） |

## 两个上游改写器（全文在 `enhancers/`）

| 线 | 改写器 | 大小 | 影响 |
|---|---|---|---|
| T2I | `Image Prompt Rewriting Expert`（8 步） | 10,308 字符 | 短指令扩写成 400–500 词观察者段落 |
| Edit | `Edit Prompt Enhancer — General (v2)` | 10,494 字符 | 实测 00338/00339 两轮负向**完全一致**，未被删减（先前假设已推翻） |

## 目录

```
templates/     通用骨架（带变量位，不含案例）
cases/         具体案例记录（只作参考）
prompts/       已交付的提示词（按模块分目录）
skills/        本线用到的技能（版本化权威副本）
sources/       官方原文与出处（含 GitHub 链接）
enhancers/     两个改写器原文
docs/          生产设定、未验证清单
evidence/      对照结论与登记表（图/视频不进库）
scripts/       校验器（技能规范 / 模板结构）
```

## 依赖（不在本仓库）

`character-reference-sheet`、`minimax-h3-video-prompt`、`ai-video-forensics`、`qwen-image-edit-compositing`（均以 knowledge-base 为准）

## 进度

- **2026-10-17**：仓库建立；导入 5 个已修正技能；官方原文入库；A/B 视频对照完成；A 版转"暂定存档"、B 版为默认；撞色受控实验标记为"不做"。
- **2026-10-18**：人像特写（无 LoRA）验证通过；编辑线"真人全身换装"用实测数字否决（头宽比 0.19×→0.24×，衣服漂到 240,237,233）；**新增 `11-faceswap-head` 换头线并跑通**（BFS LoRA，00367）—— 衣服 ΔRGB ≤5.2、身份迁移成立、脸偏"网红化"；ReActor 插件线仅完成调研未安装。

## 技能与模板规范（agentskills.io）

技能按 [agentskills.io/specification](https://agentskills.io/specification) 组织，本仓库的 5 个 `skills/` 与其上游副本都过校验。

**硬性要求**

| 项 | 规则 |
|---|---|
| 目录 | 一个技能 = 一个目录，必须含 `SKILL.md`（YAML frontmatter + 正文） |
| `name` | 1–64 字符，仅小写字母/数字/连字符，不以连字符开头或结尾，无 `--`，**必须等于父目录名** |
| `description` | 1–1024 字符，非空，包含"做什么 + 何时用"（`Use when …` / `当…时`） |
| 正文 | 建议 ≤500 行；超出拆到 `references/` |
| 引用 | 相对路径、只深入一层；**跨技能写成 `skill-name:references/x.md`** |
| 编码 | 文件开头不得有 BOM（否则 `---` 不被识别为 frontmatter） |

**一键校验**

```bash
python scripts/validate_skills.py                 # 本仓库 skills/
python scripts/validate_skills.py <技能目录> …     # 指定目录（单技能目录也认）
python scripts/check_templates.py                 # templates/ 的四态 + 三段结构
```

当前状态：`skills/` **5/5 通过**，`templates/` **7/7 通过**。

**模板三段结构**（`check_templates.py` 会查）

1. 头 10 行内有 `**状态**`，且是 ✅ / 🗄️ / ⚠️ / ⛔ 之一
2. 有"变量"表：换服装/换场景只改哪几处
3. 有自查/判据清单；除 `09-video-*` 外必须有负向段
