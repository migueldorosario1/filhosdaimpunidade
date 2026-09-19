from __future__ import annotations

import argparse
import json
from pathlib import Path

from .telemetry import DEFAULT_TELEMETRY_CONTRACT, LLMCallDetail, TelemetryReceipt, V4Telemetry


def main() -> int:
    parser = argparse.ArgumentParser(description="Telemetria V4 JSONL + Prometheus labels")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_TELEMETRY_CONTRACT, help="Contrato de telemetria V4")
    parser.add_argument("--check-label", action="append", default=[], help="Label Prometheus para validar")
    parser.add_argument("--write-sample", action="store_true", help="Grava recibo de exemplo")
    args = parser.parse_args()

    telemetry = V4Telemetry(Path(args.root), args.contract)
    payload: dict[str, object] = {"contract": args.contract}
    if args.check_label:
        labels = {label: "x" for label in args.check_label}
        payload["label_errors"] = telemetry.validate_prometheus_labels(labels)
    if args.write_sample:
        payload["receipt"] = telemetry.record_receipt(
            TelemetryReceipt(
                event_type="telemetry_sample",
                item_id="sample",
                vertical="v4_ciencia_tecnologia_ia",
                agent="codex",
                operation="sample",
                status="ok",
                idempotency_key="sample",
                llm=LLMCallDetail(provider="mock", model="v4-mock-local", tier="mock"),
            ),
            execute=True,
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 2 if payload.get("label_errors") else 0


if __name__ == "__main__":
    raise SystemExit(main())
