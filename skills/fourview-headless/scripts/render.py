"""Render recorded or newly filled prompt slots. No model or network calls."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")
IDENTITIES = {"woman": ("she", "her"), "man": ("he", "his")}
ROLE = {"OUTFIT", "LOCK", "NEG_GARMENT"}
EXTRA = {
    "strap": set(),
    "vneck": {"OUTER", "OPEN_LABEL", "OPEN_CONTENT"},
    "round": {"COLLAR_OBJECT", "COLLAR_DETAIL", "SLEEVES", "NEG_COLLAR"},
}
WARDROBE = {"GARMENT_LIST", "FOOTWEAR", "DETAIL_TILES", "COLOUR_LOCK", "NEG_GARMENT"}


def sections(path):
    text = path.read_text(encoding="utf-8")
    return {
        name.lower(): body.strip()
        for name, body in re.findall(
            r"\[(POSITIVE|NEGATIVE)\]\s*(.*?)(?=\n\[|\n# ----|\Z)", text, re.S
        )
    }


def expand(text, values):
    """Resolve nested slots; report missing slots and cycles without partial output."""
    def resolve(value, stack):
        def sub(match):
            key = match[1]
            if key not in values:
                raise ValueError(f"Missing slot: {key}")
            if key in stack:
                raise ValueError(f"Cyclic slot: {' -> '.join((*stack, key))}")
            if not isinstance(values[key], str):
                raise ValueError(f"Slot must be a string: {key}")
            return resolve(values[key], (*stack, key))
        result = TOKEN.sub(sub, value)
        if "{{" in result or "}}" in result:
            raise ValueError("Malformed or unresolved placeholder")
        return result
    return resolve(text, ())


def check_fields(values, allowed, required):
    if not isinstance(values, dict):
        raise ValueError("Slots must be an object")
    if values.keys() - allowed:
        raise ValueError(f"Unknown slots: {sorted(values.keys() - allowed)}")
    if required - values.keys():
        raise ValueError(f"Missing slots: {sorted(required - values.keys())}")
    for k, v in values.items():
        if not isinstance(v, str) or (not v.strip() and k != "COLLAR_DETAIL"):
            raise ValueError(f"Empty or invalid slot: {k}")


def role_values(config):
    family = config.get("family")
    subject = config.get("subject")
    if family not in EXTRA or subject not in IDENTITIES:
        raise ValueError("Choose family strap/vneck/round and subject woman/man")
    role = config.get("role")
    required = ROLE | (EXTRA[family] if family == "vneck" else set())
    check_fields(role, ROLE | EXTRA[family], required)
    source = (ROOT / f"templates/families/{family}.txt").read_text(encoding="utf-8")
    values = dict(re.findall(r"^([A-Z_]+): ?(.*)$", source, re.M))
    pronoun, poss = IDENTITIES[subject]
    values.update(SUBJECT=subject, PRONOUN=pronoun, POSS=poss)
    values.update(role)
    return values


def render_config(config):
    if not isinstance(config, dict):
        raise ValueError("Configuration must be an object")
    if config.keys() - {"family", "subject", "role", "wardrobe"}:
        raise ValueError("Unknown configuration fields")
    values = role_values(config)
    role = {
        k: expand(v, values)
        for k, v in sections(ROOT / "templates/skeleton_515.txt").items()
    }
    result = {"515": role}
    if "wardrobe" in config:
        check_fields(config["wardrobe"], WARDROBE, WARDROBE)
        result["478"] = {
            k: expand(v, config["wardrobe"])
            for k, v in sections(ROOT / "templates/wardrobe_478.txt").items()
        }
    return result


def load_case(case_id):
    if not re.fullmatch(r"\d{5}", case_id):
        raise ValueError("Case ID must be five digits")
    return json.loads((ROOT / f"references/cases/{case_id}.json").read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choose = parser.add_mutually_exclusive_group(required=True)
    choose.add_argument("--case")
    choose.add_argument("--config", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.case:
            case = load_case(args.case)
            result = render_config(case["config"])
            if "478" not in result:
                result["478"] = case["expected"]["478"]
                print("478: copying historical raw prompts, not a current-template replay.")
        else:
            config = json.loads(args.config.read_text(encoding="utf-8"))
            if "wardrobe" not in config:
                raise ValueError("New configs must include wardrobe; do not skip stage 478")
            result = render_config(config)
        files = {
            args.out / f"{stage}-{part}.txt": prompt
            for stage, parts in result.items() for part, prompt in parts.items()
        }
        if any(p.exists() for p in files):
            raise ValueError("Output files already exist; use a fresh output directory")
        args.out.mkdir(parents=True, exist_ok=True)
        for path, prompt in files.items():
            path.write_text(prompt, encoding="utf-8")
        print(f"Wrote {len(files)} prompts. No images generated.")
    except (ValueError, OSError) as error:
        parser.exit(2, f"{error}\n")


if __name__ == "__main__":
    main()
