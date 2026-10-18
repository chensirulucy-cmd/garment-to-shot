#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 templates/ 是否符合本仓库的模板约定（POLICY.md 的四态 + 三段结构）。

每条模板必须满足：
  1. 第 8 行内出现 **状态**：✅已验证 / 🗄️暂定存档 / ⚠️未验证 / ⛔弃用 之一
  2. 有"变量"表（换服装/换场景只改哪几处）
  3. 有"自查 / 判据 / 门"清单（发出前检查）
  4. 有"负向"段（视频类模板可豁免，用 --allow-no-negative 或在文件名上标 09-video）

用法：python scripts/check_templates.py [--root templates]
"""
from __future__ import annotations

import os
import re
import sys

STATES = ("✅", "🗄️", "⚠️", "⛔")
SKIP = {"README.md"}


def check(path: str):
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    issues = []
    head = "\n".join(lines[:10])
    if "状态" not in head:
        issues.append("前 10 行没有 **状态** 行")
    elif not any(s in head for s in STATES):
        issues.append("状态行里没有四态标记（✅ / 🗄️ / ⚠️ / ⛔）")
    if not re.search(r"变量", text):
        issues.append("没有“变量”说明（换服装/换场景改哪几处）")
    if not re.search(r"自查|判据|检查|门", text):
        issues.append("没有自查/判据清单")
    name = os.path.basename(path)
    if not re.search(r"负向|negative", text, re.I) and not name.startswith("09-video"):
        issues.append("没有负向段（视频模板除外）")
    return issues


def main(argv):
    root = "templates"
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), root))
    total = failed = 0
    for name in sorted(os.listdir(root)):
        if not name.endswith(".md") or name in SKIP:
            continue
        total += 1
        issues = check(os.path.join(root, name))
        if issues:
            failed += 1
            print(f"❌ {name}")
            for i in issues:
                print("     -", i)
        else:
            print(f"✅ {name}")
    print(f"\n共 {total} 个模板，失败 {failed} 个。" + ("  ✅ 全部通过" if failed == 0 else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
