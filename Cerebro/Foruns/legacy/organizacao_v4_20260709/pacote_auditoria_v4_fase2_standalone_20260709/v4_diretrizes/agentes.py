from __future__ import annotations

from pathlib import Path
from typing import Any

from .camadas import LayerAccessController
from .loader import DirectiveLoader
from .schema import TechnicalAgentSpec


DEFAULT_AGENTS_CONTRACT = "diretrizes/v4_agentes_tecnicos_v1.json"


class TechnicalAgentFactory:
    """Monta especificacoes tecnicas de agentes V4 sem diretriz hardcoded."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_AGENTS_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.layer_access = LayerAccessController(self.root)

    def build(self, name: str) -> TechnicalAgentSpec:
        agents: dict[str, dict[str, Any]] = self.contract.get("agents", {})
        if name not in agents:
            return TechnicalAgentSpec(name, "", [], [], False, False, ["agente desconhecido"])
        cfg = agents[name]
        role = cfg["role"]
        read_layers = list(cfg.get("default_read_layers", []))
        write_layers = list(cfg.get("default_write_layers", []))
        issues: list[str] = []

        for layer in read_layers:
            decision = self.layer_access.decide(role, "read", layer)
            if not decision.allowed:
                issues.append(f"read {layer}: {decision.reason}")
        for layer in write_layers:
            decision = self.layer_access.decide(role, "write", layer)
            if not decision.allowed:
                issues.append(f"write {layer}: {decision.reason}")

        return TechnicalAgentSpec(
            name=name,
            role=role,
            read_layers=read_layers,
            write_layers=write_layers,
            requires_editorial_contract=bool(cfg.get("requires_editorial_contract", False)),
            valid=not issues,
            issues=issues,
        )

    def validate_all(self) -> list[TechnicalAgentSpec]:
        return [self.build(name) for name in sorted(self.contract.get("agents", {}))]
