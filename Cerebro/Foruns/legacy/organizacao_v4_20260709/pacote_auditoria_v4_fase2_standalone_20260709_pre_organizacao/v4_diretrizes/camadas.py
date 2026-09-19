from __future__ import annotations

from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .schema import LayerAccessDecision


DEFAULT_LAYERS_CONTRACT = "diretrizes/v4_bancos_camadas_v1.json"


class LayerAccessController:
    """Controle tecnico das camadas de dados V4."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_LAYERS_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.layers: dict[str, dict[str, Any]] = self.contract.get("camadas", {})

    def decide(self, role: str, operation: str, layer: str) -> LayerAccessDecision:
        if layer not in self.layers:
            return LayerAccessDecision(False, role, operation, layer, "camada desconhecida")
        if operation not in {"read", "write"}:
            return LayerAccessDecision(False, role, operation, layer, "operacao desconhecida")

        blocked = self._blocked_by_rule(role, operation, layer)
        if blocked is not None:
            return LayerAccessDecision(False, role, operation, layer, blocked)

        key = "read_roles" if operation == "read" else "write_roles"
        allowed_roles = set(self.layers[layer].get(key, []))
        if role in allowed_roles:
            return LayerAccessDecision(True, role, operation, layer, f"{role} autorizado em {key}")
        return LayerAccessDecision(False, role, operation, layer, f"{role} ausente de {key}")

    def validate_contract(self) -> list[LayerAccessDecision]:
        checks = [
            ("produtor", "read", "bruto"),
            ("produtor", "read", "intermediario"),
            ("produtor", "read", "auditado"),
            ("publicador", "read", "auditado"),
            ("publicador", "read", "bruto"),
            ("coletor", "write", "bruto"),
            ("coletor", "write", "auditado"),
            ("produtor", "write", "producao"),
            ("imagem", "write", "producao"),
            ("auditor", "write", "auditado"),
        ]
        return [self.decide(role, operation, layer) for role, operation, layer in checks]

    def ensure_directories(self, execute: bool = False) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for layer, cfg in sorted(self.layers.items()):
            path = self.root / cfg["path"]
            mode = "present" if path.exists() else "planned"
            if execute and not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                mode = "created"
            result.append({"layer": layer, "path": str(path.relative_to(self.root)), "mode": mode})
        return result

    def _blocked_by_rule(self, role: str, operation: str, layer: str) -> str | None:
        field = "cannot_read" if operation == "read" else "cannot_write"
        for rule in self.contract.get("bloqueios", []):
            if rule.get("role") != role:
                continue
            if layer in set(rule.get(field, [])):
                return rule.get("reason", "bloqueado por contrato")
        return None
