# 模板 · 8 秒单镜 · 逐秒编排（A 式 · 🗄️ 暂定存档）

> **用途**：需要精确指定"第几秒发生什么"的镜头（多节拍、动作戏、产品揭示、悬疑）。
> **状态**：🗄️ 暂定存档 —— 本案例（客厅 8 秒）B 式更受欢迎；**换运镜/换题材先试这一式，不要当成劣势方案**。
> **代价**：写起来长（约 B 式的 1.6 倍），且**比较两式必须锁 seed**。

---

## 一、先填六列分镜表（编译前必须完成）

| 列 | 填什么 | 硬规则 |
|---|---|---|
| **Shot ID & Duration** | `S01 / 8s` | 单镜 ≤15s，超了就拆 |
| **Continuity Handoff** | 这一镜怎么从上一镜的结尾像/道具/视线接过来，怎么给下一镜铺路 | 把这一列逐行读下来要连成一条链 |
| **Reference Anchors** | `Fixed Landmarks`（地标 + 屏幕相对位置）／`Character Positions`（左中右、前中后、朝向、初始姿态）／`Exited Character Status`／`Lighting Baseline`（主/辅/轮廓光方向）+ 身份绑定 | 四个子字段全必填 |
| **Hook Type** | `tender / reveal / reversal / suspense / chase / callback / expression-beat` | 每连续三镜至少一个 reveal/reversal/callback |
| **Shot Description + 每秒指令** | 景别、运镜、荷兰角、表演、SFX + **逐秒 0–1s / 1–2s …** | 每秒必须含五要素 |
| **Audio & Dialogue Track** | 旁白（带时间区间）／台词／SFX（时间锚定）／表演备注 | 画外旁白标 `narrator-mouth-closed: true` |

### 每秒五要素（缺一个就不算填完）
1. 动作 / 姿态 / 表情
2. 机位运动
3. 空间位置（人在哪、拿着什么、哪个地标在画面里）
4. 声音线索（旁白/台词/SFX/呼吸/`silent`）
5. 交接给下一秒或下一镜

---

## 二、骨架（六列表 → Ref2VA 的编译）

```
detailed_description:
{{画质锁定句}}

[Shot 1] The frame opens as a {{景别}} at {{机位}} in {{场景}}: <Subject 1> {{起始姿态}} … Zero to one second: {{动作/表情}}; the camera {{固定/运动}}; {{空间}}; {{声音}}; this second locks {{交接}}. One to two seconds: {{…}}. Two to three seconds: {{…}}. … Seven to eight seconds: {{…}}. The shot uses {{唯一运镜}} and no other camera movement. {{脸/头发/顺滑/无台词/无文字 五句锁定}}
```

其余四段（`subject_definitions` / `summary` / `retention_analysis` / `overall_soundscape` / `non_diegetic_music`）与 B 式**完全相同**，直接取 `09-video-8s-B.md` 的骨架。

---

## 三、自检门（六项，不过不许开跑）

1. **hook 密度**：每镜有 Hook Type；每连续三镜至少一个 reveal/reversal/callback；首尾镜强 hook
2. **单镜 ≤15s**
3. **每镜重要角色 ≤3**
4. **空间锚 + 光基线继承**；变更必须显式写（如 `door-frame moves from right third to centre as camera orbits left`）
5. **每秒覆盖无空隙**：0s 到时长每一秒都有条目，且五要素齐（亚秒节拍允许 `2.0–2.5s`）
6. **连续链条**：`Continuity Handoff` 逐行读下来不断裂；任何视线/位置/道具/光线翻转都要标 `HARD CUT — …`

---

## 四、什么时候该用 A 式（而不是 B 式）

- 一个镜头里要发生**两件以上**的事，且有明确的先后（走位 + 拿起 + 转头）
- 需要**指定停顿**（喜剧节拍、悬疑留白、产品揭示的 0.5 秒静止）
- 动作戏 / 打斗 / 追逐（每个动作窗口都要卡时间）
- 与 B 式做对照时：**锁同一 seed**，否则两个变量同变，结论无效
