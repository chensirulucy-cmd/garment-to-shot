import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/qwen-image-2-1-prompter/scripts/validate_prompt.py'
spec = importlib.util.spec_from_file_location('prompt_validator', SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PromptEnvelopeTests(unittest.TestCase):
    def test_malformed_fields_rejected_without_crashing(self):
        bad = [[], None, 1, {}, {'rewritten_prompt': []}]
        bad += [{'rewritten_prompt': 'A cat.', 'wh_ratio': x} for x in [1, None, [], True, '0:0', '0:1', '1:0', '1:-2', '']]
        bad += [{'rewritten_prompt': 'Edit.', 'ratio_follow': x} for x in [1, None, [], '<image0>', '<image01>', 'image1']]
        for payload in bad:
            with self.subTest(payload=payload):
                ok, errors = validator.validate_qwen_prompt(payload)
                self.assertFalse(ok)
                self.assertTrue(errors)

    def test_baseline_with_newlines_and_4k_is_preserved(self):
        prompt = (ROOT / 'prompts/11-faceswap/00373-positive.txt').read_text(encoding='utf-8')
        payload = {'rewritten_prompt': prompt, 'ratio_follow': '<image1>', 'wh_ratio': ''}
        before = json.dumps(payload)
        report = validator.inspect_qwen_prompt(payload)
        self.assertFalse(report['errors'])
        self.assertTrue(report['warnings'])
        self.assertEqual(json.dumps(payload), before)

    def test_one_size_source_only(self):
        for ratio, follow, ok in [('16:9', '', True), ('', '<image1>', True), ('16:9', '<image1>', False), ('', '', False)]:
            with self.subTest(ratio=ratio, follow=follow):
                self.assertEqual(validator.validate_qwen_prompt({'rewritten_prompt': 'Edit.', 'wh_ratio': ratio, 'ratio_follow': follow})[0], ok)

    def test_cli_exit_status_and_explicit_style_lint(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'input.json'
            for payload, extra, expected in [([], [], 1), ({'rewritten_prompt': 'Line one.\nLine two. 4k', 'wh_ratio': '1:1'}, [], 0), ({'rewritten_prompt': 'Line one.\nLine two. 4k', 'wh_ratio': '1:1'}, ['--strict-style'], 1)]:
                p.write_text(json.dumps(payload), encoding='utf-8')
                result = subprocess.run([sys.executable, str(SCRIPT), str(p), *extra], capture_output=True)
                self.assertEqual(result.returncode, expected, result.stderr)


if __name__ == '__main__':
    unittest.main()
