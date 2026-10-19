# 模板 · 白模 + 服装板 → 真人全身（两段式）

> **状态**：✅ 已验证（2026-10-18，00369）。案例 `cases/12-white-model-2026-10-18.md`。
> **用途**：先把「服装」和「人」分开做 —— ① 服装照 → 服装板；② 白模 + 服装板 → 真人穿好的身体。脸不承担身份，身份留给换脸那一步（`templates/11-faceswap-head.md`）。
> **本模板不含具体服装**：件数、结构、配色按 `{{…}}` 填。

## 一、为什么分两段

脸在全身构图里只有约 100 px，**不该在这一步解决身份**。第一刀只解决：身体比例、姿势、服装形态、光、背景。第二段交出可换头的身体图；后续BFS为生成式编辑，不把其实现描述为ArcFace特征搬运或源像素覆盖。

反面：在第二段里写 `her identity` / `same face as the portrait` 是无效约束，会和底脸规格打架。

## 二、接线（不是错接，别改）

| 段 | 节点 | 接什么 |
|---|---|---|
| ① 服装板 | `478` 子图 | `LoadImage` → 服装产品照 |
| ① 出口 | `477` = `SaveImageAdvanced` | 存盘同时输出 IMAGE，**直接连到 ② 的 `image_2`** |
| ② 真人 | `515` 子图 | `image_1` = 白模图；`image_2` = ① 的服装板（就是 `477`） |
| ② 出口 | `516` = `SaveImageAdvanced` | 成品 |

本路线的实际图像顺序由编码器已连接的输入决定；00383 已确认 image_1=白模、image_2=477 服装板。不要推断删除节点后会自动正确重排，修改接线后重新核对 API 图。

## 三、变量表

| 变量 | 必填 | 写法要求 | 坑 |
|---|---|---|---|
| `{{件数与每件结构}}` | ✅ | **先写件数**（`a single one-piece dress` / `a two-piece set`），再逐件写：领型、袖长、长短、剪裁、闭合方式、接缝位置 | 件数写错 → 会被拆成两件或合体；漏写接缝 → 腰部错位 |
| `{{鞋描述}}` | ✅ | 鞋型 + 鞋头 + 鞋跟 + 颜色，写在服装后面 | 漏写 → 鞋会被重新设计 |
| `{{色彩保真句}}` | ✅ | 每个主色一条：`stays X and never turns Y/Z` | 只写色名不写"不许变成"→ 黑会变炭灰、红会变橘 |
| `{{细节格清单}}` | ✅ | 4–6 个该件衣服**真正的**工艺点（领口收边/腰缝/袖口/面料/下摆/鞋头） | 抄别的衣服的细节格 → 会凭空造出该衣服没有的部件 |
| `{{layout 全屋句}}` | ✅ | 正/背/侧三视 + 鞋摆在脚位 + 细节列 | 少一视 → 背面靠编 |
| `{{落点句}}` | ✅ | 衣服在身上的**落点**：领口到哪、袖到哪、腰线在哪、下摆到哪 | 不写落点 → 衣服浮在身上 |

## 四、不变量（原样粘，别删）

- `Show attire only, not the person.` + `no mannequin and no dress form of any kind` —— 服装板里**不许出现人**。
- `the garments hold their shape as ghost-mannequin volumes, hollow and empty` —— 立体但不长人。
- 单张 `plain seamless light-grey studio backdrop held at one even value`，**所有格子同一个底**。
- `no white resin, no ball-and-socket joint, no dark joint seam` —— ②里必须正克关节。
- **绝不能同时写 `keep its blank head`** —— 那是把白模锁死，头永远是空白树脂。
- ②保留白模画布的构图与尺度。头顶留白、90%占高、镜头距离等属于上游白模规格，不在00383第二段原文中，不能冒充该段逐字不变量。
- 负向两段必须分开用（①的负向含 `person / face / mannequin`，②的负向含 `mannequin / white resin`，混用会互相打架）。

## 五、参数（实测）

| 项 | 值 |
|---|---|
| 底模 / 编码 / VAE | `qwen_image_2.1_int8_convrot` / `qwen3vl_8b_int8_convrot` / `qwen_image_2.1_vae_bf16` |
| ① 服装板 | **cfg 3.5 / 30 步 / euler-simple**；00382 实际 1216×1600，按编码器所选分支随输入取整 |
| ② 真人 | 9:16 · 2 MP · **cfg 3.5 / 30 步 / euler-simple** → 1088×1920 |
| 耗时 | 两段同跑约 8–10 分钟（00368→00369 之间实测） |

## 六、判据（四条）

1. **衣服颜色**：按同款、对应衣物区域与光照条件比较；00369 的 Δ4 是该样本记录。不同阶段重绘不能把全图 RGB Δ≤10 当通用通过线，需同时检查色相、款式与纹理。
2. **关节**：脖子/肩/肘/腕/膝/踝有没有残留白树脂或球窝缝。
3. **件数**：真身上的件数与 `{{件数与每件结构}}` 一致，没有被拆开或合并。
4. **取景**：人物占画面高 84–90%；头顶留白约 7%。

## 七、已知坑

- 提示词写 `face fills about one tenth of the picture height`，但 00369 实测脸约 **100 px（≈5%）**——**比例句不保证落地**，量出来才算。这也是必须走换脸的原因。
- **手指**：本段留下的手指融合问题换脸救不了，属本段缺陷；候选方向＝手部单独描述或换姿势回避（均未实测）。
- 服装板里如果混进深色道具（如黑鞋摆在灰底上），细节格容易把鞋吞掉 —— 鞋单独点名。

## 八、完整角色段骨架

00382 是上游服装板，00383 是下游真人，两张保存了相同的完整 API 图；不能当作两张换姿势的真人对照。00383 的原始正负向已分别恢复至 [正向](../prompts/12-white-model/00383-positive.txt) 和 [负向](../prompts/12-white-model/00383-negative.txt)，负向实际为681字符，并非未记录。原有 wearer-negative.txt 是通用版，不能冒充00383原文。

以下仅将00383的服装、颜色、落点、鞋替换为变量，其余正文保持；换款效果需实图验收。

```text
Edit <image1> into a finished studio photograph. Keep <image1> as the canvas: the single standing figure at the same height, position and scale, the same camera height, the same pale grey seamless backdrop with its continuous sweep into the floor, the same soft even light from the front left, and the same faint contact shadows under the feet — all exactly as they are.

Change the figure from a white mannequin into a real woman, and change her clothes. Her body is entirely human: real skin on her neck, both shoulders, both arms, both wrists, both hands with five separated fingers and visible knuckles, both thighs, both knees, both calves, both ankles and both feet with five toes each, all in one even natural skin tone. No white resin, no ball-and-socket joint, no dark joint seam and no doll-like articulation remains anywhere on her body.

Her face is a plain, ordinary young East Asian face with no strong features: her head is level and square to the lens, her eyes open and looking into the camera, her forehead fully visible with her hair swept back off it, her eyebrows light, her lips closed and her expression neutral and calm. Her face fills about one tenth of the picture height, nothing covers it, and she wears almost no makeup.

She is dressed in the outfit from <image2>, {{件数与每件结构}}. {{色彩保真句}}

The garment sits on her the way real clothes sit on a body: {{对应领口、袖长、腰线、下摆及实际可见衣褶的落点句}}.

She wears {{鞋描述与鞋的落点}} from <image2> on both feet.
```

## 九、配套服装板与负向

第一段使用 [服装板骨架](../skills/character-asset-pipeline/references/02-garment-board.md)，保留正背侧三整装+细节列，按来源图填写鞋、细节与颜色；00382完整基线在 [正向](../prompts/12-white-model/00382-wardrobe-positive.txt) / [负向](../prompts/12-white-model/00382-wardrobe-negative.txt)。

第二段以00383原始负向为基线，只替换与新衣服冲突的服装词；姿态、人体、白模残留相关负向不要顺手改写。两段各交完整正负向，不能把服装板的 person / face 禁词复制到真人段。第一段输出接第二段image_2。

第二段latent：515:511=false → 515:513输出2，resolution=0，第一参考=白模。517选择器在未选分支，不决定这次输出尺寸。此修订仅恢复证据及骨架，不改变ComfyUI工作流。
