# ⑤ 派生规则：给一版新服装，怎么得到这几套提示词

> **2026-10-21 当前生成入口**：[fourview-headless](../../fourview-headless/SKILL.md)。515按固定骨架填族槽；以下既有文字供历史与接线参考，不覆盖新入口的槽位范围和验证状态。

**结论先行：服装模板与服装板是「通用版」，换衣服不用改字；只有四视图要改一处，人像通常不用改。**

**改动量上界（硬指标）：四视图 1 处、人像 0 处、服装类 0 处。超过这个改动量就是违规**——把模板重写一遍会让已验证的效果回退（实测：三块全重写后，人物变通用、服装板不再分解）。想改结构，先按下面的回滚协议留好 baseline。

## 回滚协议（改坏了怎么办）

1. 动提示词之前，先把当前可用版本导出成 **API 格式 json**（`*_baseline.json`）：子图会被摊平成真正会跑的那张表，能逐节点 diff。
2. 出问题先 **diff 两版**，按节点列差异。**若差异只有提示词文本** → 就是提示词的锅，**不许去怀疑种子/开关/LoRA/比例/强度**。
3. 回滚**只回滚提示词**；LoRA、强度、cfg、steps、采样器、比例、两个 `custom_size/switch`、seed 全部保持原样。
4. 回到 baseline 后再做「一次只动一个变量」的微调（例：先只把 `strength_model` 1.0 → 1.15 跑一张比）。

## 变量总表

| 变量 | 出现在 | 取值方式 |
|---|---|---|
| 触发词 | 人像正向句首 | LoRA 训练触发词（读 safetensors `ss_tag_frequency`） |
| 发型/发长 | 人像 `Hair` 句；四视图第 4 格 | 与身份图一致；换发长时两处同步 |
| 服装名词段 | **四视图正向最后一段** | 颜色 + 材质 + 品类 + 3 个必需细节（领型/扣子/下摆或鞋） |
| 颜色保真句 | 四视图、服装板 | 把新颜色写进去（如 `mid-grey … rather than black or white`） |
| 鞋的来源 | 服装模板/服装板 | 输入图自带 / 自动配 / `<image2>` 鞋图 |
| 画幅与像素 | 三个模块的 ResolutionSelector | 人像 1:1；四视图 16:9；服装类跟随输入图 |
| LoRA 挂不挂 | 仅人像模块 | 1.0，只在人像链上 |

## 五步派生流程

1. **读一遗服装**，写下六项：件数、每件的品类、颜色（带修饰词）、材质/图案、3 个标志性细节、鞋。
2. **服装模板**（`01`）：通用版**直接跑**，不改字；若这版要固定鞋，就切到 `<image2>` 鞋图变体。
3. **服装板**（`02`）：通用版**直接跑**；把鞋的来源段切成与上一步一致。
4. **人像**（`03`）：**通常不改**；只有换角色、换发长、换触发词时改那两三处。
5. **四视图**（`04`）：**只改一处**——正向最后那段服装名词，把旧套装换成新套装，并确认颜色保真句里用的是新颜色。

## 服装名词段的写法（唯一要手工写的字段）

模板：

```
a ⟨colour + fabric⟩ ⟨garment class⟩ with ⟨detail 1⟩, ⟨detail 2⟩ and ⟨detail 3⟩, closed over a ⟨colour + fabric⟩ ⟨lower garment⟩, with ⟨colour + material⟩ ⟨shoes⟩ on both feet
```

例（旧 → 新）：

- 旧：`a light sage-green ribbed knit short-sleeve V-neck top … a cream mini skirt … cream flat ballet shoes`
- 新：`a mid-grey ribbed knit long-sleeve cardigan with a pointed collar in brown, cream, black and white checks, five small round brown buttons down the centre front and turned-back tartan cuffs, closed over a mid-grey knife-pleated mini skirt that ends at mid-thigh, with black round-toe chunky-sole loafers on both feet`

配套改颜色保真句：

```
The ⟨新颜色A⟩ and the ⟨新颜色B⟩ read clearly as ⟨…⟩ rather than black or white, the ⟨布料A⟩ keeps its ⟨纹理⟩, and the ⟨图案/细节⟩ stays legible in every panel.
```

## 换装检查单（6 项，逐项打勾）

1. 件数对不对（连衣裙不能被写成两件）。
2. 颜色写了、且写了「不是黑也不是白」。
3. 三个标志性细节（领/扣/下摆/裙型/鞋）里至少三个进了四视图那段。
4. 发型句与身份图一致（长发/短发、分缝、是否搭在肩前）。
5. 服装模板/服装板没漏改鞋的来源段。
6. 画幅与像素没变（人像 1:1；四视图 16:9）。

## 一个真实对比（同一流程两次跑）

| 环节 | A 版（sage-green 上衣 + 米白裙 + 芭蕾鞋） | B 版（灰格纹领开衫 + 灰百褶裙 + 黑乐福鞋） |
|---|---|---|
| 服装模板 | 通用版直接跑 | 通用版直接跑（另加 `no embroidery`——原图左胸有小刺绣） |
| 服装板 | 通用版直接跑 | 鞋的来源段切为「输入图自带」→ 自动配 |
| 人像 | 触发词 + 长发句 | 同 |
| 四视图 | 旧服装段 | 换成新服装段 + 颜色保真句改 `mid-grey` |

→ 实际改动量：**四视图 1 处、人像 0 处、服装类 0 处**。以后「你只说场景」的接口就是靠这套变量收敛做到的。
