#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 agentskills.io 规范校验技能目录。

规范要点（2026-10 版）：
  · SKILL.md 必须有 YAML frontmatter + Markdown 正文
  · name：1–64 字符，仅小写字母/数字/连字符，不以连字符开头结尾，无连续连字符，**必须等于父目录名**
  · description：1–1024 字符，非空，说明"做什么 + 何时用"
  · license / compatibility（≤500）/ metadata / allowed-tools 可选
  · 正文建议 ≤500 行，超出应拆到 references/
  · 文件引用用相对路径，只深入一层；跨技能引用写成 `skill-name:references/x.md`

用法：
  python scripts/validate_skills.py                # 校验本仓库 skills/
  python scripts/validate_skills.py <目录> [<目录> …]
  python scripts/validate_skills.py --strict       # 把"建议项"也当失败
"""
from __future__ import annotations

import os
import re
import sys
import json

try:
    import yaml
except ImportError:  # 无 PyYAML 时退化为最小解析
    yaml = None

FM_RE = re.compile(r"^(?:\ufeff)?---\r?\n(.*?)\r?\n---\r?\n", re.S)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REF_RE = re.compile(r"`([A-Za-z0-9_:./-]+\.(?:md|py|json|txt|yaml|yml|png|jpg))`")
LEGACY_REFS = {"cheat_sheet.md", "edit_rules.md", "t2i_rules.md"}  # 旧命名，保留兼容（有跨技能引用，不改名）

WHEN_HINTS = ("use when", "use this skill", "whenever", "当", "用于", "适用于", "需要")


def parse_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, "缺少 frontmatter（文件必须以 --- 开头，且不能有 BOM）"
    raw = m.group(1)
    if yaml is None:
        data = dict(re.findall(r"^([a-z][a-z0-9-]*):\s*(.*)$", raw, re.M))
        return data, None
    try:
        data = yaml.safe_load(raw) or {}
    except Exception as exc:  # noqa: BLE001
        return None, f"YAML 解析失败：{exc}"
    if not isinstance(data, dict):
        return None, "frontmatter 不是键值映射"
    return data, None


def find_skill_root(skills_root: str, name: str):
    """跨技能引用解析：在 skills_root 下一层或两层目录里找同名技能。"""
    for depth in (1, 2, 3):
        pattern = os.path.join(skills_root, *(["*"] * (depth - 1)), name)
        import glob

        for hit in glob.glob(pattern):
            if os.path.isfile(os.path.join(hit, "SKILL.md")):
                return hit
    return None


def check(skill_dir: str, skills_root: str, strict: bool = False, dependencies=None):
    errors: list[str] = []
    warns: list[str] = []
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        return ["缺少 SKILL.md"]

    with open(skill_md, encoding="utf-8", errors="replace") as stream:
        text = stream.read()
    fm, err = parse_frontmatter(text)
    if err:
        return [err]

    if yaml is None:
        warns.append("未安装PyYAML：仅检查字段，未完整验证YAML")
    for key in sorted(set(fm) - {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}):
        warns.append(f"非通用规范顶层字段 {key}：保留现有Hermes格式，跨客户端兼容性未验证")
    meta = fm.get("metadata")
    if yaml is not None and meta is not None and (not isinstance(meta, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in meta.items())):
        warns.append("metadata不是通用规范字符串映射；保留现有Hermes嵌套元数据")

    dirname = os.path.basename(os.path.normpath(skill_dir))
    name = fm.get("name")
    if not name:
        errors.append("缺少 name")
    else:
        name = str(name)
        if not NAME_RE.match(name):
            errors.append(f"name 非法（小写字母/数字/连字符）：{name!r}")
        if len(name) > 64:
            errors.append(f"name 超长（{len(name)}>64）")
        if name != dirname:
            errors.append(f"name 与父目录不一致：{name!r} vs {dirname!r}")

    desc = fm.get("description")
    if not desc or not str(desc).strip():
        errors.append("缺少 description")
    else:
        desc = str(desc).strip()
        if len(desc) > 1024:
            errors.append(f"description 超长（{len(desc)}>1024）")
        if not any(h in desc.lower() for h in WHEN_HINTS):
            warns.append("description 未说明“何时用”（建议含 Use when / 当…时）")

    # 本仓库约定（规范里是可选项，这里当"house rule"检查，只警告）
    for key in ("license", "version", "author"):
        if key not in fm:
            warns.append(f"frontmatter 缺 {key}（本仓库约定必填）")
    if "references" in os.listdir(skill_dir) if os.path.isdir(skill_dir) else False:
        ref_dir = os.path.join(skill_dir, "references")
        if os.path.isdir(ref_dir) and not os.path.isfile(os.path.join(ref_dir, "README.md")):
            warns.append("references/ 没有 README.md 索引")
        for fn in os.listdir(ref_dir):
            if fn == "README.md" or fn in LEGACY_REFS:
                continue
            if not re.fullmatch(r"(?:\d{2}-)?[a-z0-9]+(?:-[a-z0-9]+)*\.(md|txt|json|yaml|yml|png|jpg)", fn):
                warns.append(f"references 命名不规范（建议 kebab-case 或 NN- 前缀）：{fn}")

    comp = fm.get("compatibility")
    if comp and len(str(comp)) > 500:
        errors.append(f"compatibility 超长（{len(str(comp))}>500）")

    lines = len(text.splitlines())
    if lines > 500:
        warns.append(f"正文 {lines} 行 > 500，建议拆分到 references/")

    # 引用检查（忽略 fenced code 之外的纯文本）
    body = text[len(FM_RE.match(text).group(0)):]
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if dependencies is None:
        try:
            with open(os.path.join(repo_root, "dependencies.json"), encoding="utf-8") as stream:
                dependencies = json.load(stream)
        except (OSError, ValueError) as exc:
            dependencies = {}
            errors.append(f"依赖登记不可读：{exc}")
    for ref in sorted(set(REF_RE.findall(body))):
        if ref.startswith(("http://", "https://")):
            continue
        if ":" in ref:  # 跨技能：skill-name:references/x.md
            skill_name, _, rel = ref.partition(":")
            target = find_skill_root(skills_root, skill_name)
            if not target:
                if skill_name in dependencies:
                    warns.append(f"外部依赖未验证可用：{ref}")
                else:
                    errors.append(f"跨技能引用找不到技能且未登记：{skill_name}")
            elif not os.path.exists(os.path.join(target, rel)):
                errors.append(f"跨技能引用文件不存在：{ref}")
            continue
        # 只校验"路径式"引用；裸文件名（install.py、nodes_qwen.py 等）不当作技能内引用
        if "/" not in ref:
            continue
        head, _, tail = ref.partition("/")
        if find_skill_root(skills_root, head):
            tgt = find_skill_root(skills_root, head)
            if os.path.exists(os.path.join(tgt, tail)):
                continue
        # 依次在：技能目录 → scripts/references/assets → skills 根 → 仓库根 里找
        if not any(
            os.path.exists(os.path.join(base, ref))
            for base in (skill_dir, os.path.join(skill_dir, "scripts"),
                         os.path.join(skill_dir, "references"),
                         os.path.join(skill_dir, "assets"), skills_root, repo_root)
        ):
            errors.append(f"引用文件不存在：{ref}")
        if ref.count("/") > 2:
            warns.append(f"引用层级过深（应≤1 层）：{ref}")

    if strict:
        errors.extend(warns)
        warns = []
    return errors + [f"⚠ {w}" for w in warns]


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    argv = [a for a in argv if a != "--strict"]
    roots = argv[1:] or [os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skills")]
    skills_root = roots[0]
    if os.path.isfile(os.path.join(skills_root, "SKILL.md")):
        skills_root = os.path.dirname(os.path.abspath(skills_root))
    total = failed = warning_count = 0
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            if "SKILL.md" not in filenames:
                continue
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            total += 1
            issues = check(dirpath, skills_root, strict)
            hard = [i for i in issues if not i.startswith("⚠")]
            warning_count += sum(i.startswith("⚠") for i in issues)
            if issues:
                failed += 1 if hard else 0
                print(("❌ " if hard else "⚠  ") + os.path.relpath(dirpath, root))
                for i in issues:
                    print("     -", i)
    print(f"\n共 {total} 个技能，结构错误 {failed} 个，警告 {warning_count} 条。检查不证明生成效果、外部依赖可用或跨客户端兼容。")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
