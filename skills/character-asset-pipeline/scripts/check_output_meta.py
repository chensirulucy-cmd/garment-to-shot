#!/usr/bin/env python
"""列出 ComfyUI 输出图的真实配置：尺寸 / LoRA / 提示词开头。

为什么需要它：文件名和工作流界面都不算凭据。一张图到底有没有挂 LoRA、挂在什么
强度、出图多大，只有 PNG 内嵌的 prompt chunk 说了算。拿错一次，整轮对照实验作废。

用法（用 ComfyUI 的 venv 解释器跑，PIL 装在那一边）：
    python check_output_meta.py <output_dir> --glob "Qwen_image_2.1_*.png" --last 12
    python check_output_meta.py <output_dir> --glob "*.png" --from 389 --to 397
    python check_output_meta.py <output_dir> --expect 1088x1920 --last 6

每个 LoRA 节点打印 (文件名, strength_model)；没有则打印「无」。
带 --expect 时，尺寸不符的行尾标 ⚠。
"""
import argparse
import glob
import json
import os
import re
import sys

from PIL import Image


def index_of(path):
    m = re.search(r"(\d{3,})", os.path.basename(path))
    return int(m.group(1)) if m else -1


def lora_nodes(meta):
    out = []
    for node in meta.values():
        ctype = node.get("class_type", "")
        if "Lora" not in ctype:
            continue
        ins = node.get("inputs", {})
        out.append((ins.get("lora_name", "?"), ins.get("strength_model", ins.get("strength"))))
    return out


def prompt_heads(meta, limit=48):
    heads = []
    for node in meta.values():
        if node.get("class_type", "").startswith("TextEncode"):
            text = (node.get("inputs", {}).get("prompt") or "").replace("\n", " ").strip()
            if text:
                heads.append(text[:limit])
    return heads


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output_dir")
    ap.add_argument("--glob", default="*.png")
    ap.add_argument("--last", type=int, default=10)
    ap.add_argument("--from", dest="lo", type=int)
    ap.add_argument("--to", dest="hi", type=int)
    ap.add_argument("--expect", help="WxH，例如 1088x1920")
    args = ap.parse_args()

    expect = None
    if args.expect:
        w, h = args.expect.lower().split("x")
        expect = (int(w), int(h))

    files = glob.glob(os.path.join(args.output_dir, args.glob))
    if args.lo is not None:
        files = [f for f in files if index_of(f) >= args.lo]
    if args.hi is not None:
        files = [f for f in files if index_of(f) <= args.hi]
    files.sort(key=index_of)
    if args.lo is None and args.hi is None:
        files = files[-args.last:]

    if not files:
        print("(没有匹配的文件)")
        return 1

    for path in files:
        try:
            img = Image.open(path)
        except Exception as exc:  # 打不开就当坏图，继续
            print("%-46s 打不开: %s" % (os.path.basename(path), exc))
            continue
        try:
            meta = json.loads(img.info.get("prompt") or "{}")
        except Exception:
            meta = {}
        lo = lora_nodes(meta)
        heads = prompt_heads(meta)
        flag = ""
        if expect and tuple(img.size) != expect:
            flag = "  ⚠ 期望 %dx%d" % expect
        print("%-46s %-11s LoRA=%s | %s%s" % (
            os.path.basename(path),
            "%dx%d" % img.size,
            lo if lo else "无",
            heads[0] if heads else "(无提示词)",
            flag,
        ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
