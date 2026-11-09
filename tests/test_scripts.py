from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from scripts.new_feature import create_feature, next_feature_number, slugify
from scripts.validate_docs import validate


class NewFeatureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "specs").mkdir()
        template = self.root / "templates" / "feature"
        (template / "diagrams").mkdir(parents=True)
        for name in ("spec.md", "plan.md", "tasks.md", "verification.md"):
            (template / name).write_text("# Feature NNN: [Feature title]\nCreated YYYY-MM-DD\nFR-NNN\n")
        (template / "diagrams" / "sequence.mmd").write_text("sequenceDiagram\n    title NNN\n")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_slug_normalization(self) -> None:
        self.assertEqual(slugify("Café & User Authentication!"), "cafe-user-authentication")
        self.assertEqual(slugify("!!!"), "")

    def test_next_id_selection(self) -> None:
        (self.root / "specs" / "003-old").mkdir()
        (self.root / "specs" / "010-later").mkdir()
        self.assertEqual(next_feature_number(self.root / "specs"), 11)

    def test_creates_from_templates_with_metadata(self) -> None:
        target = create_feature("User Authentication", self.root, date(2026, 1, 2))
        self.assertEqual(target.name, "001-user-authentication")
        spec = (target / "spec.md").read_text()
        self.assertIn("Feature 001: User Authentication", spec)
        self.assertIn("2026-01-02", spec)
        self.assertIn("FR-001", spec)
        self.assertTrue((target / "diagrams" / "sequence.mmd").exists())

    def test_refuses_duplicate_directory(self) -> None:
        target = self.root / "specs" / "001-user-authentication"
        target.mkdir()
        sentinel = target / "keep.txt"
        sentinel.write_text("preserve")
        with patch("scripts.new_feature.next_feature_number", return_value=1):
            with self.assertRaises(FileExistsError):
                create_feature("User Authentication", self.root)
        self.assertEqual(sentinel.read_text(), "preserve")


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for required in ("README.md", "AGENTS.md", "CLAUDE.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md", "docs/framework", "docs/project", "specs", "templates", "scripts", "tests", ".github/workflows"):
            path = self.root / required
            if "." in path.name and not path.suffix:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("stub")
            elif path.suffix:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("stub")
            else:
                path.mkdir(parents=True, exist_ok=True)
        for required in ("scripts/new_feature.py", "scripts/validate_docs.py", ".github/workflows/validate-docs.yml"):
            path = self.root / required
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("stub")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_detects_unbalanced_markdown_fence(self) -> None:
        (self.root / "README.md").write_text("# Test\n```python\nprint('x')\n")
        self.assertTrue(any("unclosed fenced" in item for item in validate(self.root).errors))

    def test_detects_duplicate_requirement_declarations(self) -> None:
        (self.root / "README.md").write_text("| FR-001 | first |\n| FR-001 | duplicate |\n")
        self.assertTrue(any("duplicate declared ID FR-001" in item for item in validate(self.root).errors))

    def test_detects_short_requirement_id(self) -> None:
        (self.root / "README.md").write_text("A requirement is FR-01.\n")
        self.assertTrue(any("at least three digits" in item for item in validate(self.root).errors))

    def test_detects_empty_and_invalid_mermaid(self) -> None:
        (self.root / "README.md").write_text("```mermaid\n```\n\n```mermaid\nnotADiagram\n```\n")
        errors = validate(self.root).errors
        self.assertTrue(any("empty Mermaid" in item for item in errors))
        self.assertTrue(any("unrecognized Mermaid" in item for item in errors))

    def test_detects_broken_internal_markdown_link(self) -> None:
        (self.root / "README.md").write_text("[missing](no-such-file.md)\n")
        self.assertTrue(any("broken local Markdown link" in item for item in validate(self.root).errors))

    def test_valid_and_invalid_json(self) -> None:
        (self.root / "valid.json").write_text('{"ok": true}')
        (self.root / "invalid.json").write_text('{"broken": }')
        errors = validate(self.root).errors
        self.assertTrue(any("invalid JSON" in item and "invalid.json" in item for item in errors))
        self.assertFalse(any(item.split(":", 1)[0].endswith("/valid.json") for item in errors))

    def test_checks_feature_files_and_status(self) -> None:
        feature = self.root / "specs" / "001-example"
        feature.mkdir()
        (feature / "spec.md").write_text("# Example\n- **Status:** unknown\n")
        errors = validate(self.root).errors
        self.assertTrue(any("missing plan.md" in item for item in errors))
        self.assertTrue(any("unsupported feature status" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
