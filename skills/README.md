# 技能分工与入口

本页只整理入口，不改变各技能已固化的提示词、参数或规则。使用时先核对具体节点与已有成功样本。

| 主任务 | 首选入口 | 参考用途与边界 |
|---|---|---|
| 四视图无头（478→515） | [fourview-headless](fourview-headless/SKILL.md) | 固定骨架与三族槽位；515样本已验证，478缺视角另列限制 |
| 服装资产、人像、其他资产流程 | [character-asset-pipeline](character-asset-pipeline/SKILL.md) | 负责资产阶段和接线；Qwen 提示词格式按需读下面的模型技能 |
| Qwen 文生图或编辑措辞 | [qwen-image-2-1-prompter](qwen-image-2-1-prompter/SKILL.md) | 模型级写法参考，不覆盖已验收配方 |
| 多来源六格陈列 | [multi-source-image-composition](multi-source-image-composition/SKILL.md) | 保留一次生成完整陈列图；不自动重开已退出的返修项目 |
| 人物与场景合成 | [qwen-image-edit-composite](qwen-image-edit-composite/SKILL.md) | 仅在实际请求这类任务时参考；不能自动替换现用 12→11 流程 |
| H3 叙事与镜头描述 | [cinematic-narrative-h3](cinematic-narrative-h3/SKILL.md) | 09 B 当前默认，09 A 可用存档；按题材选择 |

已纠正的跨文件冲突及原始依据见 [审阅证据](../evidence/skill-audit-2026-10-19/README.md)。按当前任务只读相关入口；外部依赖仍须核可用性。影响生成效果的新写法须实测，静态证据锁定的文档/工具错误直接纠正。
