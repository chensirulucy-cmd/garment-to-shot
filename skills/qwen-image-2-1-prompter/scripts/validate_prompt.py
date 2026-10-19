#!/usr/bin/env python3
"""Validate JSON fields separately from prose preferences; never rewrite recipes.

This checks the repository envelope, not image quality or actual ComfyUI sizing.
"""
import argparse
import json
from pathlib import Path
import re
import sys

RATIO_REGEX = re.compile(r"^[1-9][0-9]*:[1-9][0-9]*$")
IMAGE_TAG_REGEX = re.compile(r"^<image[1-9][0-9]*>$")
FORBIDDEN_BOOSTERS = ["8k", "4k", "masterpiece", "award-winning"]


def inspect_qwen_prompt(payload):
    errors, warnings = [], []
    if not isinstance(payload, dict):
        return {"errors": ["Payload must be a JSON object."], "warnings": []}
    prompt = payload.get("rewritten_prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        errors.append("rewritten_prompt must be a non-empty string.")
    else:
        if chr(10) in prompt or chr(13) in prompt:
            warnings.append("Multiline prose: preserve tested recipe line breaks; single paragraph is a style preference.")
        if prompt.count(chr(34)) % 2:
            warnings.append("Unbalanced straight double quotes; check intended rendered text.")
        for word in FORBIDDEN_BOOSTERS:
            if re.search(r"\b" + re.escape(word) + r"\b", prompt, re.I):
                warnings.append(f"Style word {word!r}: review generic prose, but preserve a tested LoRA recipe.")
    fields = ("wh_ratio", "ratio_follow")
    if not any(k in payload for k in fields):
        errors.append("Specify wh_ratio or ratio_follow.")
    values = {}
    for k in fields:
        value = payload.get(k, "")
        if not isinstance(value, str):
            errors.append(f"{k} must be a string.")
            value = ""
        values[k] = value
    ratio, follow = values["wh_ratio"], values["ratio_follow"]
    if bool(ratio) == bool(follow):
        errors.append("Exactly one of wh_ratio and ratio_follow must be non-empty.")
    if ratio and not RATIO_REGEX.fullmatch(ratio):
        errors.append("wh_ratio must be W:H with positive integer dimensions (e.g. 16:9).")
    if follow and not IMAGE_TAG_REGEX.fullmatch(follow):
        errors.append("ratio_follow must be a positive one-based image tag (e.g. <image1>).")
    return {"errors": errors, "warnings": warnings}


def validate_qwen_prompt(payload):
    """Backward-compatible (passed, errors); prose advice is not a hard error."""
    report = inspect_qwen_prompt(payload)
    return not report["errors"], report["errors"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON string or UTF-8 JSON file")
    parser.add_argument("--test", action="store_true", help="Run the offline regression suite")
    parser.add_argument("--strict-style", action="store_true", help="Opt-in generic prose lint, not for frozen recipes")
    args = parser.parse_args(argv)
    if args.test or args.input is None:
        import unittest
        root = Path(__file__).resolve().parents[3]
        suite = unittest.defaultTestLoader.discover(str(root / "tests"), pattern="test_prompt_validator.py")
        return int(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())
    try:
        raw = args.input if args.input.lstrip().startswith(("{", "[")) else Path(args.input).read_text(encoding="utf-8")
        report = inspect_qwen_prompt(json.loads(raw))
    except (OSError, ValueError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(report["errors"] or (args.strict_style and report["warnings"])))


if __name__ == "__main__":
    sys.exit(main())
