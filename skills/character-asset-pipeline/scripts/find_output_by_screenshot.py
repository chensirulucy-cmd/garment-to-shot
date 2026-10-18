"""把一张「贴进来的图」反查到它到底是哪个输出文件，并把那次的真实参数全部打印出来。

用途：用户贴一张截图问「为什么这张长这样」时，先定位它是哪一号产出，再读它内嵌的
prompt / negative / 槽位 / 采样参数 —— 不要靠看图猜措辞。

用法：
    python find_output_by_screenshot.py <图片路径> [输出目录]

输出目录默认 F:\\ComfyUI-Data\\output，匹配 Qwen_image_2.1_*.png。
依赖：Pillow、numpy（ComfyUI venv 与 hermes venv 都有）。
"""
import json
import os
import struct
import sys
import glob

import numpy as np
from PIL import Image


def ahash(path, size=16):
    im = Image.open(path).convert("L").resize((size, size), Image.LANCZOS)
    a = np.asarray(im, dtype=float)
    return (a > a.mean()).flatten()


def png_text_chunks(path):
    """读 PNG 的 tEXt 块。ComfyUI 把 prompt/workflow 写在这里，是唯一可信的「那次真用了什么」。"""
    out = {}
    with open(path, "rb") as f:
        if f.read(8) != b"\x89PNG\r\n\x1a\n":
            return out
        while True:
            ln = f.read(4)
            if len(ln) < 4:
                break
            n = struct.unpack(">I", ln)[0]
            typ = f.read(4)
            data = f.read(n)
            f.read(4)
            if typ == b"tEXt":
                try:
                    k, v = data.split(b"\x00", 1)
                    out[k.decode("latin-1")] = v.decode("utf-8", "replace")
                except Exception:
                    pass
    return out


def report(path):
    chunks = png_text_chunks(path)
    if "prompt" not in chunks:
        print(f"  {os.path.basename(path)}: 没有 prompt chunk（不是 ComfyUI 产出？）")
        return
    api = json.loads(chunks["prompt"])
    print(f"\n=== {os.path.basename(path)}  {Image.open(path).size} ===")

    def upstream(nid, depth=0):
        node = api.get(nid, {})
        ins = node.get("inputs", {})
        if node.get("class_type") == "LoadImage":
            return ins.get("image")
        if depth > 12:
            return None
        for v in ins.values():
            if isinstance(v, list) and v and isinstance(v[0], str):
                r = upstream(v[0], depth + 1)
                if r:
                    return r
        return None

    for nid, node in api.items():
        if not isinstance(node, dict):
            continue
        ct = str(node.get("class_type", ""))
        ins = node.get("inputs", {})
        if ct.startswith("TextEncode"):
            pos = ins.get("prompt", "")
            neg = ins.get("negative_prompt", "")
            slots = {
                k: upstream(v[0])
                for k, v in ins.items()
                if k.startswith("image") and isinstance(v, list)
            }
            print(f"[{nid}] {ct} | 正向 {len(pos.split())} 词 / {len(pos)} 字符 | 负向 {len(neg.split())} 词")
            print(f"     首句: {pos[:90]!r}")
            print(f"     槽位: {slots}")
        if "KSampler" in ct:
            print(f"[{nid}] {ct}: " + str({k: ins.get(k) for k in ("seed", "steps", "cfg", "sampler_name", "scheduler", "denoise")}))
        if ct == "ResolutionSelector":
            print(f"[{nid}] {ct}: " + str({k: ins.get(k) for k in ("aspect_ratio", "megapixels", "multiple")}))
        if ct == "LoadImage":
            print(f"[{nid}] LoadImage: {ins.get('image')}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    query = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else r"F:\ComfyUI-Data\output"
    qh = ahash(query)
    scored = []
    for p in glob.glob(os.path.join(outdir, "*.png")):
        try:
            scored.append((int((qh != ahash(p)).sum()), p))
        except Exception:
            continue
    scored.sort()
    print("最佳匹配（汉明距离，0 = 同一张图）：")
    for d, p in scored[:3]:
        print(f"  d={d:3d}  {p}")
    if scored:
        report(scored[0][1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
