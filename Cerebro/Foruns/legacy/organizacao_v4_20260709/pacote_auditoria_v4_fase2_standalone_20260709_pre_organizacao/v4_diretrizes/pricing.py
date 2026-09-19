from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_PRICING_CONTRACT = "diretrizes/v4_pricing_llm_v1.json"


@dataclass(frozen=True)
class CostEstimate:
    tokens_in: int
    tokens_out: int
    cost_usd_estimated: float
    pricing_table_version: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "tokens_in": self.tokens_in,
            "tokens_out": self.tokens_out,
            "cost_usd_estimated": self.cost_usd_estimated,
            "pricing_table_version": self.pricing_table_version,
        }


class V4Pricing:
    """Estimativa local versionada de tokens e custo LLM."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_PRICING_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def estimate(self, model: str, input_text: str, output_text: str) -> CostEstimate:
        tokens_in = self.estimate_tokens(input_text)
        tokens_out = self.estimate_tokens(output_text)
        model_cfg = self.contract.get("models", {}).get(model)
        if not model_cfg:
            fallback = self.contract.get("fallback", {})
            return CostEstimate(
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                cost_usd_estimated=0.0,
                pricing_table_version=fallback.get("pricing_table_version", "pending"),
            )
        cost = (
            tokens_in * float(model_cfg["input_usd_per_1m"])
            + tokens_out * float(model_cfg["output_usd_per_1m"])
        ) / 1_000_000
        return CostEstimate(
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            cost_usd_estimated=round(cost, 8),
            pricing_table_version=str(self.contract.get("_version", "pending")),
        )

    @staticmethod
    def estimate_tokens(text: str) -> int:
        if not text:
            return 0
        return max(1, (len(text) + 3) // 4)
