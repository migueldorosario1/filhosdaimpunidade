from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DirectiveDocument:
    path: Path
    content: str
    sha256: str


@dataclass(frozen=True)
class LLMContext:
    name: str
    tiers: list[str]


@dataclass(frozen=True)
class LLMValidationIssue:
    severity: str
    code: str
    message: str
    tier: str | None = None
    provider: str | None = None
    model: str | None = None


@dataclass(frozen=True)
class LLMValidationReport:
    editoria: str
    funcao: str
    contexto_llm: str
    qualidade_minima: int
    issues: list[LLMValidationIssue] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not any(issue.severity == "error" for issue in self.issues)

    def as_dict(self) -> dict[str, Any]:
        return {
            "editoria": self.editoria,
            "funcao": self.funcao,
            "contexto_llm": self.contexto_llm,
            "qualidade_minima": self.qualidade_minima,
            "ok": self.ok,
            "issues": [
                {
                    "severity": issue.severity,
                    "code": issue.code,
                    "message": issue.message,
                    "tier": issue.tier,
                    "provider": issue.provider,
                    "model": issue.model,
                }
                for issue in self.issues
            ],
        }


@dataclass(frozen=True)
class OperationAction:
    action: str
    target: str
    path: str
    mode: str
    reason: str


@dataclass(frozen=True)
class OperationReport:
    dry_run: bool
    contract_path: str
    actions: list[OperationAction] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "dry_run": self.dry_run,
            "contract_path": self.contract_path,
            "actions": [
                {
                    "action": action.action,
                    "target": action.target,
                    "path": action.path,
                    "mode": action.mode,
                    "reason": action.reason,
                }
                for action in self.actions
            ],
            "warnings": self.warnings,
        }


@dataclass(frozen=True)
class LayerAccessDecision:
    allowed: bool
    role: str
    operation: str
    layer: str
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "allowed": self.allowed,
            "role": self.role,
            "operation": self.operation,
            "layer": self.layer,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class TechnicalAgentSpec:
    name: str
    role: str
    read_layers: list[str]
    write_layers: list[str]
    requires_editorial_contract: bool
    valid: bool
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "role": self.role,
            "read_layers": self.read_layers,
            "write_layers": self.write_layers,
            "requires_editorial_contract": self.requires_editorial_contract,
            "valid": self.valid,
            "issues": self.issues,
        }


@dataclass(frozen=True)
class EditorialContract:
    editoria: str
    label: str
    funcao: str
    contexto_llm: LLMContext
    nobre: bool
    nucleo: DirectiveDocument
    diretriz: DirectiveDocument
    freios_llm: dict[str, Any]
    memoria_bugs: list[DirectiveDocument] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_prompt_blocks(self) -> list[tuple[str, str]]:
        blocks = [
            ("nucleo_editorial", self.nucleo.content),
            ("diretriz_editoria", self.diretriz.content),
            ("freios_llm_json", self._freios_as_text()),
        ]
        for item in self.memoria_bugs:
            blocks.append((f"memoria_bugs:{item.path}", item.content))
        return blocks

    def _freios_as_text(self) -> str:
        import json

        return json.dumps(self.freios_llm, ensure_ascii=False, indent=2, sort_keys=True)
