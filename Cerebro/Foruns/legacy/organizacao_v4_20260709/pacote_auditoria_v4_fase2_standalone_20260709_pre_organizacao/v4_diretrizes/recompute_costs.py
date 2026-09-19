from __future__ import annotations

import fcntl
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .pricing import V4Pricing


DEFAULT_RECOMPUTE_CONTRACT = "diretrizes/v4_recompute_costs_v1.json"


@dataclass(frozen=True)
class RecomputeResult:
    schema_version: str
    timestamp: str
    source_receipt_file: str
    item_id: str
    vertical: str
    operation: str
    provider: str
    model: str
    old_cost_usd_estimated: float
    new_cost_usd_estimated: float
    old_pricing_table_version: str
    new_pricing_table_version: str
    tokens_in: int
    tokens_out: int
    status: str

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


class V4CostRecomputer:
    """Recalcula custos antigos em arquivo append-only separado."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_RECOMPUTE_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.pricing = V4Pricing(self.root)

    def run(self, execute: bool = False) -> dict[str, Any]:
        results: list[RecomputeResult] = []
        existing_keys = self._existing_output_keys()
        for path in sorted((self.root / self.contract["source_receipts_dir"]).glob("*.jsonl")):
            for receipt in self._read_jsonl(path):
                result = self._recompute_receipt(path, receipt)
                if self._output_key(result) in existing_keys:
                    result = self._replace_status(result, "skipped_already_recorded")
                results.append(result)
        appendable = [result for result in results if result.status != "skipped_already_recorded"]
        if execute and appendable:
            self._append_results(appendable)
        return {
            "ok": True,
            "mode": "appended" if execute else "dry_run",
            "count": len(results),
            "appended_count": len(appendable) if execute else 0,
            "results": [result.as_dict() for result in results],
        }

    def _recompute_receipt(self, path: Path, receipt: dict[str, Any]) -> RecomputeResult:
        llm = receipt.get("llm", {})
        provider = llm.get("provider", "")
        model = llm.get("model", "")
        old_cost = float(receipt.get("cost_usd_estimated", 0.0))
        old_version = str(receipt.get("pricing_table_version", "pending"))
        status = self._initial_status(receipt)
        tokens_in = int(llm.get("tokens_in", 0) or 0)
        tokens_out = int(llm.get("tokens_out", 0) or 0)
        new_cost = old_cost
        new_version = old_version

        if status == "recomputed":
            if tokens_in == 0 and tokens_out == 0:
                basis = self._token_basis(receipt)
                if basis is None:
                    status = "skipped_no_token_basis"
                else:
                    tokens_in, tokens_out = basis
            if status == "recomputed":
                estimate = self.pricing.estimate(model, "x" * (tokens_in * 4), "x" * (tokens_out * 4))
                if estimate.pricing_table_version == "pending":
                    status = "skipped_unknown_model"
                else:
                    new_cost = estimate.cost_usd_estimated
                    new_version = estimate.pricing_table_version

        return RecomputeResult(
            schema_version=self.contract["output_schema_version"],
            timestamp=datetime.now(timezone.utc).isoformat(),
            source_receipt_file=str(path.relative_to(self.root)),
            item_id=str(receipt.get("item_id", "")),
            vertical=str(receipt.get("vertical", "")),
            operation=str(receipt.get("operation", "")),
            provider=provider,
            model=model,
            old_cost_usd_estimated=old_cost,
            new_cost_usd_estimated=new_cost,
            old_pricing_table_version=old_version,
            new_pricing_table_version=new_version,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            status=status,
        )

    def _initial_status(self, receipt: dict[str, Any]) -> str:
        llm = receipt.get("llm", {})
        if not llm:
            return "skipped_no_llm"
        if receipt.get("pricing_table_version") not in self.contract["recompute_when"]["pricing_table_version_in"]:
            return "skipped_not_needed"
        if float(receipt.get("cost_usd_estimated", 0.0)) > float(self.contract["recompute_when"]["cost_usd_estimated_lte"]):
            return "skipped_not_needed"
        if self.contract["recompute_when"]["requires_llm_model"] and not llm.get("model"):
            return "skipped_no_llm"
        return "recomputed"

    def _token_basis(self, receipt: dict[str, Any]) -> tuple[int, int] | None:
        item_id = receipt.get("item_id")
        if not item_id:
            return None
        production_path = self.root / "v4_data/producao" / f"{item_id}.producao.json"
        if not production_path.exists():
            return None
        data = json.loads(production_path.read_text(encoding="utf-8"))
        input_text = str(data.get("conteudo", ""))
        output_text = str(data.get("texto_dry_run", ""))
        tokens_in = self.pricing.estimate_tokens(input_text)
        tokens_out = self.pricing.estimate_tokens(output_text)
        if tokens_in == 0 and tokens_out == 0:
            return None
        return tokens_in, tokens_out

    def _append_results(self, results: list[RecomputeResult]) -> None:
        output_dir = self.root / self.contract["output_dir"]
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"recomputed_{datetime.now(timezone.utc).date().isoformat().replace('-', '')}.jsonl"
        with output_path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            for result in results:
                handle.write(json.dumps(result.as_dict(), ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)

    def _existing_output_keys(self) -> set[tuple[str, str, str, str, str]]:
        output_dir = self.root / self.contract["output_dir"]
        keys: set[tuple[str, str, str, str, str]] = set()
        for path in sorted(output_dir.glob("*.jsonl")):
            for item in self._read_jsonl(path):
                keys.add(
                    (
                        str(item.get("source_receipt_file", "")),
                        str(item.get("item_id", "")),
                        str(item.get("operation", "")),
                        str(item.get("model", "")),
                        str(item.get("new_pricing_table_version", "")),
                    )
                )
        return keys

    @staticmethod
    def _output_key(result: RecomputeResult) -> tuple[str, str, str, str, str]:
        return (
            result.source_receipt_file,
            result.item_id,
            result.operation,
            result.model,
            result.new_pricing_table_version,
        )

    @staticmethod
    def _replace_status(result: RecomputeResult, status: str) -> RecomputeResult:
        return RecomputeResult(
            schema_version=result.schema_version,
            timestamp=result.timestamp,
            source_receipt_file=result.source_receipt_file,
            item_id=result.item_id,
            vertical=result.vertical,
            operation=result.operation,
            provider=result.provider,
            model=result.model,
            old_cost_usd_estimated=result.old_cost_usd_estimated,
            new_cost_usd_estimated=result.new_cost_usd_estimated,
            old_pricing_table_version=result.old_pricing_table_version,
            new_pricing_table_version=result.new_pricing_table_version,
            tokens_in=result.tokens_in,
            tokens_out=result.tokens_out,
            status=status,
        )

    @staticmethod
    def _read_jsonl(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
