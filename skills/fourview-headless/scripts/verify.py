"""Verify frozen templates and replay real PNG-derived fixtures without a GPU."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import sys

from render import ROOT, expand, load_case, render_config


def digest(data):
    return hashlib.sha256(data).hexdigest()


def reject(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError("Invalid input unexpectedly accepted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--png-dir", type=Path)
    args = parser.parse_args()
    evidence = json.loads((ROOT / "references/evidence.json").read_text(encoding="utf-8"))
    for name, expected in evidence["templates"].items():
        assert digest((ROOT / "templates" / name).read_bytes()) == expected, name
    cases = [load_case(i) for i in ("00501", "00507", "00510", "00512", "00513")]
    count = 0
    for case in cases:
        result = render_config(case["config"])
        for stage, parts in result.items():
            for part, actual in parts.items():
                assert actual == case["expected"][stage][part].strip(), (case["sample"], stage, part)
                assert "{{" not in actual and "}}" not in actual
                count += 1
    assert count == 18

    # Real failure modes: accidentally editing invariant text, omitted colour lock,
    # missing nested opening data, invalid empty values and recursive slots.
    base = cases[1]["config"]
    bad = copy.deepcopy(base)
    bad["role"]["NECKLINE_ANCHOR"] = "override"
    reject(lambda: render_config(bad))
    bad = copy.deepcopy(base)
    del bad["role"]["LOCK"]
    reject(lambda: render_config(bad))
    bad = copy.deepcopy(base)
    del bad["role"]["OPEN_CONTENT"]
    reject(lambda: render_config(bad))
    bad = copy.deepcopy(base)
    bad["role"]["LOCK"] = ""
    reject(lambda: render_config(bad))
    reject(lambda: expand("{{A}}", {"A": "{{B}}", "B": "{{A}}"}))
    reject(lambda: expand("{{not_valid}}", {}))
    reject(lambda: expand("{{A}}", {}))
    # Subject changes must update embedded absence clauses, not just the subject.
    changed = copy.deepcopy(cases[2]["config"])
    changed["subject"] = "man"
    generated = render_config(changed)["515"]["positive"]
    assert "with his head and neck" in generated and " her " not in generated
    assert "same man" in generated and "he wears" in generated

    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "prompts"
        command = [sys.executable, str(ROOT / "scripts/render.py"), "--case", "00510", "--out", str(dest)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        assert result.returncode == 0, result.stderr
        assert len(list(dest.glob("*.txt"))) == 4
        expected = cases[2]["expected"]
        for stage, parts in expected.items():
            for part, text in parts.items():
                assert (dest / f"{stage}-{part}.txt").read_text(encoding="utf-8") == text.strip()
        before = {p.name: digest(p.read_bytes()) for p in dest.iterdir()}
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        assert result.returncode == 2
        assert before == {p.name: digest(p.read_bytes()) for p in dest.iterdir()}
        config_path = Path(tmp) / "config.json"
        config_path.write_text(json.dumps(cases[1]["config"]), encoding="utf-8")
        command = [sys.executable, str(ROOT / "scripts/render.py"), "--config",
                   str(config_path), "--out", str(Path(tmp) / "custom")]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        assert result.returncode == 0, result.stderr
        assert len(list((Path(tmp) / "custom").glob("*.txt"))) == 4
        config_path.write_text(json.dumps(cases[0]["config"]), encoding="utf-8")
        command[-1] = str(Path(tmp) / "incomplete")
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        assert result.returncode == 2
        assert not (Path(tmp) / "incomplete").exists()

    png_count = 0
    if args.png_dir:
        from PIL import Image
        for case in cases:
            path = args.png_dir / case["sample"]
            assert digest(path.read_bytes()) == case["sha256"], path.name
            with Image.open(path) as im:
                assert list(im.size) == case["size"]
                graph = json.loads(im.info["prompt"])
            for stage, node in (("478", "478:474"), ("515", "515:513")):
                for part, field in (("positive", "prompt"), ("negative", "negative_prompt")):
                    assert graph[node]["inputs"][field] == case["expected"][stage][part]
            for node, filename in case["inputs"].items():
                assert graph[node]["inputs"]["image"] == filename
            png_count += 1
    print(json.dumps({
        "template_fingerprints": "2/2",
        "exact_prompt_replays": "18/18",
        "invalid_slots_and_subject_linkage": "PASS",
        "cli_four_files_and_overwrite_protection": "PASS",
        "original_pngs_verified": png_count,
        "scope": "text/source validation; existing visual findings documented separately",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
