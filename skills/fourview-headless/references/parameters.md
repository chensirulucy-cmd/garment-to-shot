# 槽位组装与回放

两个主模板来自交付包，逐字节保留。固定正文不变，所有替换发生在双大括号槽内。案例衣服内容在 cases/，不写入通用模板。

## 生成方式

在 skill 目录运行：

```powershell
python scripts/render.py --case 00510 --out <输出目录>
python scripts/render.py --config <配置.json> --out <输出目录>
python scripts/verify.py
```

自定义配置结构与 `cases/00510.json` 的 `config` 相同。`--case` 用于复现该案例，不是自动换衣。要换款，提取 config 后根据图片填写新服装数据。

## 515 角色板

| 槽组 | 规则 |
|---|---|
| family | strap / vneck / round；round 当前只验证闭合高领 |
| subject | woman 或 man；组装器同步 she/he、her/his 及 ABSENCE_* 内的代词 |
| OUTFIT | 完整服装结构与鞋履，按参考服装填写，保留句末标点 |
| LOCK | 颜色、形状、细节保真句；不可遗失 |
| NEG_GARMENT | 当前服装不应出现的变化；不能把正向所需内容写成禁项 |
| ABSENCE_* / CHANGE_SCOPE / GARMENT_WORD / IDENTITY_TERMS / NEG_FAMILY | 从 family 文件取，不允许 config 偷偷覆盖固定措辞 |
| vneck 的 OUTER / OPEN_LABEL / OPEN_CONTENT | 外衣名、实际开口、开口内可见内搭；00507 是 cardigan / open front of the cardigan / the white crew neckline of the tee and the upper chest |
| round 的 COLLAR_OBJECT / SLEEVES / NEG_COLLAR | 默认为 garment / sleeves / collar；00501 为 sweater / raglan sleeves / sweater collar |
| round 的 COLLAR_DETAIL | 默认空串；有实测的拉链/白领细节见 00501 config，包含开头分号 |

COLLAR_DETAIL 位于 NECKLINE_ANCHOR 内 `no trapezius tapering upward` 之后、`; the … sleeves` 之前。不是在骨架末尾额外加一句。00501 精确子句：

```text
; the short zip pull and the white shirt collar sit on the garment at the base of the neck and remain visible as part of the outfit, while the neck itself stays absent above them
```

只在对应服装确有拉链/白领时使用；其他领口细节需依据参考填槽并标明新适配范围，不把白领复制到无衬衫衣服。00500→00501 还将 high mock collar 改成 high collar，不能声称仅追加文字。

## 478 服装板

独立填 GARMENT_LIST、FOOTWEAR、DETAIL_TILES、COLOUR_LOCK、NEG_GARMENT 五槽。保留三整装视图＋细节栏的文字目标。DETAIL_TILES 随实际服装选择，不能给无褶皱裙子硬加褶皱。

00501 的 478 使用旧模板，完整原文保留在案例 expected 中；`--case 00501` 只将 515 从现行骨架组装，478 复制已测原文，不谎称能从现行 478 回放。

## 回放边界

最终 00507/510/512/513：四段均精确回放；00501：515 两段精确回放。比较只忽略首尾空白，不改内部空格、大小写、标点和词序。

00485/491 的零差仅指历史正向，旧负向不等同现行骨架。00491 的肩线负向曾追加在 `3D render.` 之后，现行版位置已变化，最终样本为现行版的实测依据。
