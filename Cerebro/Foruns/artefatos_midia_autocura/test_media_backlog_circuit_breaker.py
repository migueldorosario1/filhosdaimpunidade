import json
import tempfile
import unittest
from pathlib import Path

import media_backlog_circuit_breaker as subject


def sample(index, pending, **extra):
    row = {"ts": f"2026-08-07T0{index}:00:00-03:00", "vertical": "regional", "pending_count": pending}
    row.update(extra)
    return row


class MediaBacklogCircuitBreakerTests(unittest.TestCase):
    def test_opens_after_three_positive_growth_cycles(self):
        result = subject.evaluate([sample(1, 0), sample(2, 1), sample(3, 2), sample(4, 3)])[0]
        self.assertEqual("CIRCUIT_OPEN", result["state"])
        self.assertFalse(result["enforced"])
        self.assertEqual("unknown", result["causa_suspeita"])
        self.assertEqual("L0", result["ticket"]["level"])

    def test_non_positive_delta_breaks_streak(self):
        result = subject.evaluate([sample(1, 0), sample(2, 1), sample(3, 1), sample(4, 2)])[0]
        self.assertEqual("DEGRADED", result["state"])
        self.assertIsNone(result["ticket"])

    def test_age_p95_opens_with_explicit_cause(self):
        result = subject.evaluate([sample(1, 2, age_p95_minutes=181, causa_suspeita="worker_timeout")])[0]
        self.assertEqual("CIRCUIT_OPEN", result["state"])
        self.assertEqual("worker_timeout", result["ticket"]["causa_suspeita"])

    def test_hard_invariant_opens(self):
        result = subject.evaluate([sample(1, 1, hard_invariant_broken=True)])[0]
        self.assertIn("HARD_INVARIANT_BROKEN", result["evidence"]["triggers"])

    def test_receipt_has_ticket_and_schema(self):
        result = subject.evaluate([sample(1, 0), sample(2, 1), sample(3, 2), sample(4, 3)])[0]
        receipt = subject.make_receipts([result], "fixture.jsonl")[0]
        self.assertEqual("CIRCUIT_BREAKER_OPEN", receipt["reason_code"])
        self.assertIsNotNone(receipt["prova"]["after"]["ticket"])
        self.assertEqual("receipt-v0.1.1", receipt["metadata"]["schema_version"])

    def test_load_and_atomic_receipt(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "samples.jsonl"
            source.write_text(json.dumps(sample(1, 0)) + "\n", encoding="utf-8")
            rows = subject.load_samples(str(source))
            receipt = subject.make_receipts(subject.evaluate(rows), str(source))[0]
            destination = Path(temp_dir) / "DROP_antigravity_test.jsonl"
            subject.write_jsonl_atomic(str(destination), [receipt])
            self.assertEqual(receipt, json.loads(destination.read_text()))


if __name__ == "__main__":
    unittest.main()
