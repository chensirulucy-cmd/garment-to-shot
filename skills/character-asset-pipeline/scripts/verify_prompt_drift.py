#!/usr/bin/env python
"""Check a candidate prompt against a verified baseline before delivery.

Why: the expensive failures in this pipeline are never "the words were ugly" --
they are "I rewrote the skeleton", "a markdown backtick broke an anchor token",
or "the slot I was allowed to change is not the only thing that changed".
This script turns all three into numbers so you can report them instead of claiming
"I did not touch anything else".

Usage
-----
    # baseline straight from a verified output PNG (reads the embedded prompt chunk)
    python verify_prompt_drift.py out/Qwen_image_2.1_00308.png candidate.txt \
        --pick "Edit the four-figure" \
        --slot "a black fine-rib knit long-sleeve V-neck top:::the pumps stay nude." \
        --ban "tee-dress" --ban "falls from the shoulders" --ban "no belt"

    # baseline from a text file
    python verify_prompt_drift.py baseline.txt candidate.txt --slot "START:::END"

Exit code 0 = all hard checks pass, 1 = do not deliver.
Hard checks: similarity >= --min-sim, every slot's outside text byte-identical,
zero markdown-wrapped anchor tokens, zero banned phrases.
"""

import argparse
import difflib
import json
import re
import sys

DEFAULT_BAN = [
    # body verbs in a garment slot -> the model paints a person
    "tee-dress",
    "falls from the shoulders",
    "wraps around the body",
    # negations -> the model paints the thing you denied
    "no waist seam",
    "no belt",
    "no drawstring",
    # face words in a four-view prompt -> heads appear in the headless panels
    "skin condition",
]


def load_text(path, pick=None):
    """Text file, or the embedded `prompt` chunk of a ComfyUI output PNG."""
    if path.lower().endswith(".png"):
        try:
            from PIL import Image
        except ImportError:
            sys.exit("PIL missing: export the prompt to a .txt first, or run this with ComfyUI's venv")
        info = json.loads(Image.open(path).info.get("prompt", "{}"))
        texts = [
            v["inputs"].get("prompt", "")
            for v in info.values()
            if isinstance(v, dict) and isinstance(v.get("inputs"), dict)
            and isinstance(v["inputs"].get("prompt"), str)
        ]
        if pick:
            texts = [t for t in texts if pick in t]
        if not texts:
            sys.exit(f"no prompt text found in {path} (pick={pick!r})")
        return max(texts, key=len).strip()
    return open(path, encoding="utf-8").read().strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Verify prompt drift against a verified baseline")
    ap.add_argument("baseline", help="baseline .txt or verified output .png")
    ap.add_argument("candidate", help="the prompt you are about to deliver (.txt or .md)")
    ap.add_argument("--pick", help="substring to choose which prompt chunk to read from a PNG")
    ap.add_argument("--slot", action="append", default=[],
                    help='allowed-to-differ span, as "START:::END" (repeatable)')
    ap.add_argument("--ban", action="append", default=[], help="extra banned phrase")
    ap.add_argument("--allow-ban", action="append", default=[],
                    help="phrase from DEFAULT_BAN that is legitimate here")
    ap.add_argument("--min-sim", type=float, default=0.90)
    a = ap.parse_args(argv)

    base = load_text(a.baseline, a.pick)
    cand = load_text(a.candidate)
    ok = True

    bw, cw = base.split(), cand.split()
    sim = difflib.SequenceMatcher(None, bw, cw).ratio()
    print(f"words        : baseline {len(bw)} / candidate {len(cw)}")
    print(f"similarity   : {sim:.3f}  (min {a.min_sim:.2f})")
    if sim < a.min_sim:
        print("  FAIL: too far from the baseline -- you rewrote it instead of filling the slot")
        ok = False

    if not a.slot:
        print("slot         : none given, skipping the outside-the-slot identity check")
    for spec in a.slot:
        if ":::" not in spec:
            sys.exit(f'bad --slot {spec!r}: expected "START:::END"')
        start, end = spec.split(":::", 1)
        try:
            i, j = base.index(start), base.index(end) + len(end)
            i2, j2 = cand.index(start), cand.index(end) + len(end)
        except ValueError:
            print(f"  FAIL: slot anchors not found on both sides: {start[:40]}…:::…{end[-40:]}")
            ok = False
            continue
        pre, suf = base[:i] == cand[:i2], base[j:] == cand[j2:]
        print(f"slot outside : prefix identical={pre} suffix identical={suf}  [{start[:38]}…]")
        if not (pre and suf):
            print("  FAIL: something outside the named slot changed")
            ok = False

    wrapped = re.findall(r"`<image\d>`", cand)
    bare = re.findall(r"(?<!`)<image\d>", cand)
    print(f"anchors      : bare {len(bare)} / markdown-wrapped {len(wrapped)}")
    if wrapped:
        print("  FAIL: backticks become part of the text -- slot binding silently dies")
        ok = False

    allowed = {p.lower() for p in a.allow_ban}
    bans = list(DEFAULT_BAN) + list(a.ban)
    hits = [p for p in bans if p.lower() not in allowed and p.lower() in cand.lower()]
    if hits:
        print("banned       : " + " | ".join(hits))
        print("  FAIL: these are the exact phrases that reintroduce a person / negate themselves")
        ok = False
    else:
        print("banned       : none")

    print("RESULT:", "PASS" if ok else "FAIL")
    if not ok:
        print("Do not deliver. Take the baseline, change only the named slot, re-run this.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
