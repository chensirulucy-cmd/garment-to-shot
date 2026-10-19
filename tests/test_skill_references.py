import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('skill_validator', ROOT / 'scripts/validate_skills.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SkillReferenceTests(unittest.TestCase):
    def test_missing_external_is_not_silently_passed(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            skill = root / 'caller'; skill.mkdir()
            (skill / 'SKILL.md').write_text('---\nname: caller\ndescription: Use when testing references.\n---\nRead `external:references/guide.md`.\n', encoding='utf-8')
            issues = validator.check(str(skill), str(root), dependencies={})
            self.assertTrue(any('未登记' in i for i in issues))
            issues = validator.check(str(skill), str(root), dependencies={'external': {'status': 'external-unverified'}})
            self.assertFalse(any(not i.startswith('⚠') for i in issues))
            self.assertTrue(any('外部依赖未验证' in i for i in issues))
            target = root / 'external'; target.mkdir()
            (target / 'SKILL.md').write_text('---\nname: external\ndescription: Use when testing.\n---\n', encoding='utf-8')
            issues = validator.check(str(skill), str(root), dependencies={})
            self.assertTrue(any('文件不存在' in i for i in issues))
            (target / 'references').mkdir(); (target / 'references/guide.md').write_text('Guide', encoding='utf-8')
            issues = validator.check(str(skill), str(root), dependencies={})
            self.assertFalse(any(not i.startswith('⚠') for i in issues))


if __name__ == '__main__':
    unittest.main()
