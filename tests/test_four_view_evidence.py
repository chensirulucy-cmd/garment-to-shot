"""Regression checks for the evidence tools, not generated-image quality."""
import contextlib
import copy
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


compare = load('compare', 'skills/qwen-image-2-1-prompter/scripts/diff_two_outputs.py')
drift = load('drift', 'skills/character-asset-pipeline/scripts/verify_prompt_drift.py')


class EvidenceTools(unittest.TestCase):
    def test_same_graph_is_not_reported_as_same_output(self):
        graph = {'477': {'class_type': 'SaveImageAdvanced', 'inputs': {'images': ['478', 0]}},
                 '516': {'class_type': 'SaveImageAdvanced', 'inputs': {'images': ['515', 0]}}}
        output = io.StringIO()
        with patch.object(compare, 'load_api', return_value=graph), \
                patch.object(compare, 'size', return_value=(2080, 1184)), \
                contextlib.redirect_stdout(output):
            compare.report('wardrobe.png', 'character.png')
        text = output.getvalue()
        self.assertIn('不证明同一输出节点', text)
        self.assertIn('477', text)
        self.assertIn('516', text)
        self.assertNotIn('先做同输入复跑', text)

    def test_full_graph_changes_are_not_lost(self):
        base = {'1': {'class_type': 'Encoder', 'inputs': {'image': ['2', 0],
                'prompt': 'A  woman'}, 'is_changed': ['hash-a']}}
        variants = []
        for key, value in [('image', ['3', 0]), ('prompt', 'a woman'), ('missing', None)]:
            changed = copy.deepcopy(base)
            changed['1']['inputs'][key] = value
            variants.append(changed)
        changed = copy.deepcopy(base)
        changed['1']['is_changed'] = ['hash-b']
        variants.append(changed)
        changed = copy.deepcopy(base)
        changed['1']['class_type'] = 'OtherEncoder'
        variants.append(changed)
        variants.append({**base, '2': {'class_type': 'New', 'inputs': {}}})
        self.assertEqual(compare.graph_diff(base, copy.deepcopy(base)), [])
        for changed in variants:
            with self.subTest(changed=changed):
                self.assertTrue(compare.graph_diff(base, changed))

    def check_text(self, text, *args):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'text.txt'
            p.write_text(text, encoding='utf-8')
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = drift.main([str(p), str(p), *args])
            return code, output.getvalue()

    def test_face_words_are_not_an_automatic_failure(self):
        code, output = self.check_text('her skin condition and expression from <image2>')
        self.assertEqual(code, 0)
        self.assertIn('TEXT_CHECK_PASS', output)
        self.assertIn('require visual validation', output)

    def test_backticks_warn_without_claiming_broken_wiring(self):
        code, output = self.check_text('Use `<image1>` as the canvas')
        self.assertEqual(code, 0)
        self.assertIn('WARNING', output)

    def test_explicit_restriction_is_still_enforced(self):
        code, output = self.check_text('skin condition', '--ban', 'skin condition')
        self.assertEqual(code, 1)
        self.assertIn('TEXT_CHECK_FAIL', output)


if __name__ == '__main__':
    unittest.main()
