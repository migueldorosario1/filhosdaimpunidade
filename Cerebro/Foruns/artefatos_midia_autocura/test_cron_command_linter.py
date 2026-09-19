import json
import tempfile
import unittest
from pathlib import Path

import cron_command_linter as subject


class CronCommandLinterTests(unittest.TestCase):
    def test_detects_inline_comment_and_missing_inner_script(self):
        line = "0 * * * * /usr/bin/flock -n /tmp/job.lock /usr/bin/timeout 5m /usr/bin/python3 /missing/job.py # cortou /usr/bin/true\n"
        findings = subject.lint_text(line, exists=lambda path: path != "/missing/job.py")
        codes = {item["code"] for item in findings}
        self.assertIn("COMMAND_TRUNCATED_BY_COMMENT", codes)
        self.assertIn("EXECUTABLE_MISSING", codes)
        self.assertNotIn("LOCK_WRAPPER_MISSING", codes)
        self.assertNotIn("TIMEOUT_WRAPPER_MISSING", codes)

    def test_quoted_hash_is_not_comment(self):
        line = "0 * * * * flock -n /tmp/x timeout 5m echo 'tema #1'\n"
        findings = subject.lint_text(line, exists=lambda _: True)
        self.assertNotIn("COMMAND_TRUNCATED_BY_COMMENT", {item["code"] for item in findings})

    def test_harmless_trailing_annotation_is_not_cut_command(self):
        line = "0 * * * * flock -n /tmp/x timeout 5m /job.sh # wrapper c/ retry (06/08)\n"
        findings = subject.lint_text(line, exists=lambda _: True)
        self.assertNotIn("COMMAND_TRUNCATED_BY_COMMENT", {item["code"] for item in findings})

    def test_missing_lock_and_timeout_are_warnings(self):
        findings = subject.lint_text("0 * * * * /bin/true\n", exists=lambda _: True)
        self.assertEqual({"LOCK_WRAPPER_MISSING", "TIMEOUT_WRAPPER_MISSING"},
                         {item["code"] for item in findings})

    def test_system_crontab_user_field(self):
        line = "0 * * * * root flock -n /tmp/x timeout 1m /bin/true\n"
        self.assertEqual([], subject.lint_text(line, source_format="system", exists=lambda _: True))

    def test_wrappers_inside_shell_script_count_as_guards(self):
        line = "0 * * * * /job.sh\n"
        findings = subject.lint_text(
            line,
            exists=lambda _: True,
            read_text=lambda _: "flock -n /tmp/x timeout 5m /bin/true\n",
        )
        self.assertEqual([], findings)

    def test_receipt_is_schema_shaped_and_atomic(self):
        receipt = subject.make_receipt([], ["fixture"])
        self.assertEqual("receipt-v0.1.1", receipt["metadata"]["schema_version"])
        self.assertEqual("codex", receipt["metadata"]["model_identity"]["environment"])
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "DROP_antigravity_test.jsonl"
            subject.write_jsonl_atomic(str(path), [receipt])
            self.assertEqual(receipt, json.loads(path.read_text()))


if __name__ == "__main__":
    unittest.main()
