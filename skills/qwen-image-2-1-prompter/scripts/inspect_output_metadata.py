#!/usr/bin/env python3
"""打印 ComfyUI 出图元数据里「当时真的这么跑」的配置。

用法:
    python inspect_output_metadata.py <输出.png | 输出目录> [更多路径...]

每张图打印: 尺寸 / 每个 LoadImage 槽位放了什么文件 / KSampler 参数 /
LoRA 名与强度 / 每个 TextEncode 的词数、反引号计数、首 60 字。

为什么需要它: 交接文档、工作流文件名、界面印象都可能与真实连线不符。
PNG 的 prompt chunk 是唯一可核的证据。典型用途——
  * 「参数和我以为的不一样」→ 直接看 KSampler
  * 「槽位接错 / 服装板里混进人」→ 看 LoadImage 的文件名
  * 「token 被 markdown 包住」→ 看反引号计数是否 > 0
  * 「衣服图怎么挂了人物 LoRA」→ 看 LoraLoaderModelOnly
需 PIL（ComfyUI 的 .venv 自带）。
"""
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("需要 PIL：用 ComfyUI 的 .venv/Scripts/python.exe 跑这个脚本")


def collect(paths):
    for p in map(Path, paths):
        if p.is_dir():
            yield from sorted(p.glob("*.png"), key=lambda f: f.stat().st_mtime)
        elif p.suffix.lower() == ".png":
            yield p


def describe(f: Path) -> None:
    try:
        im = Image.open(f)
    except Exception as exc:
        print(f"!! {f.name}: 打不开 ({exc})")
        return
    graph = json.loads(im.info.get("prompt", "{}") or "{}")
    if not graph:
        print(f"!! {f.name}: 没有 prompt chunk（不是 ComfyUI 出图？）")
        return

    print(f"===== {f.name}  {im.size[0]}x{im.size[1]}")
    loads = {k: v["inputs"].get("image") for k, v in graph.items()
             if v.get("class_type") == "LoadImage"}
    if loads:
        print("  LoadImage:", loads)

    for k, v in graph.items():
        if v.get("class_type") == "KSampler":
            i = v["inputs"]
            print(f"  KSampler {k}: steps={i.get('steps')} cfg={i.get('cfg')} "
                  f"denoise={i.get('denoise')} {i.get('sampler_name')}/{i.get('scheduler')}")

    loras = [(k, v["inputs"].get("lora_name"), v["inputs"].get("strength_model"))
             for k, v in graph.items() if v.get("class_type") == "LoraLoaderModelOnly"]
    if loras:
        print("  LoRA:", loras)
    else:
        print("  LoRA: 无")

    for k, v in graph.items():
        if not v.get("class_type", "").startswith("TextEncode"):
            continue
        for field in ("prompt", "negative_prompt"):
            t = v["inputs"].get(field)
            if not isinstance(t, str) or not t.strip():
                continue
            ticks = t.count("`<image")
            flag = "  << 反引号包住锚点 token" if ticks else ""
            print(f"  {field}[{k}]: {len(t.split())} 词, 反引号 {ticks}{flag}")
            print("    " + t[:60].replace("\n", " "))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for path in collect(sys.argv[1:]):
        describe(path)
