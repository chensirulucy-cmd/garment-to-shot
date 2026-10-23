# 四视图技能入库证据

角色板515按已验证范围发布，478视角缺口保留，不宣称全流程全项通过。不新增GPU试验。

- [审定结论](../../skills/fourview-headless/references/evidence.md)
- [参数](../../skills/fourview-headless/references/parameters.md)，[文件指纹](../../skills/fourview-headless/MANIFEST.sha256)
- [逐样本完整原文与配置](../../skills/fourview-headless/references/sample_configs.md)
- [验证范围](../../skills/fourview-headless/references/verification.md)

复算：2026-10-22 v1.0.2 整体替换技能（PR #1）时，`scripts/verify.py`、`references/evidence.json`、`references/README.md` 已移除，main 上不能再复算。要复算，先检出旧版 `29d0060`，再运行 `python skills/fourview-headless/scripts/verify.py --png-dir <本地原图目录>`。

2026-10-24 复验：在 `29d0060` 上跑这条命令，结果为模板指纹 2/2、提示词回放 18/18、`original_pngs_verified: 5`，退出码 0。5 张原图（00501、00507、00510、00512、00513，均为 2080×1184）的 sha256 与该版 `evidence.json` 的登记值全长一致。
