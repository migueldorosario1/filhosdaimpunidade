from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .camadas import LayerAccessController
from .loader import DirectiveLoader


DEFAULT_CONTENT_INGESTION_CONTRACT = "diretrizes/v4_ingestao_conteudo_v1.json"


@dataclass(frozen=True)
class IngestionStep:
    step: str
    ok: bool
    mode: str
    source_path: str | None
    target_path: str | None
    issues: list[str]

    def as_dict(self) -> dict[str, Any]:
        return {
            "step": self.step,
            "ok": self.ok,
            "mode": self.mode,
            "source_path": self.source_path,
            "target_path": self.target_path,
            "issues": self.issues,
        }


class V4ContentIngestion:
    """Fluxo V4 de coleta bruta -> intermediario -> auditado."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_CONTENT_INGESTION_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.layers = LayerAccessController(self.root)

    def run_fixture(self, execute: bool = False) -> dict[str, Any]:
        fixture = self.contract["fixture"]
        steps = [
            self.collect(fixture, execute=execute),
        ]
        if steps[-1].ok:
            steps.append(self.process(fixture["item_id"], execute=execute))
        if steps[-1].ok:
            steps.append(self.audit(fixture["item_id"], execute=execute))
        return {
            "ok": all(step.ok for step in steps),
            "mode": "executed" if execute else "dry_run",
            "contract": self.contract_path,
            "steps": [step.as_dict() for step in steps],
        }

    def collect(self, payload: dict[str, Any], execute: bool = False) -> IngestionStep:
        issues = self._check_write("coletor", "bruto")
        raw = {
            "item_id": payload["item_id"],
            "editoria": payload["editoria"],
            "titulo": payload["titulo"],
            "primary_entity": payload.get("primary_entity"),
            "fonte": payload["fonte"],
            "url": payload.get("url"),
            "conteudo": payload["conteudo"],
            "status": "bruto_coletado",
            "created_at": self._now(),
            "manifesto_origem": {
                "source_agent": "v4_coletor",
                "fonte": payload["fonte"],
                "url": payload.get("url"),
                "capturado_em": self._now(),
            },
        }
        issues.extend(self._required_issues(raw, "required_raw_fields"))
        target = self._path("bruto", f"{payload['item_id']}.bruto.json")
        return self._write_step("collect", None, target, raw, issues, execute)

    def process(self, item_id: str, execute: bool = False) -> IngestionStep:
        issues = self._check_read("processador", "bruto") + self._check_write("processador", "intermediario")
        source = self._path("bruto", f"{item_id}.bruto.json")
        target = self._path("intermediario", f"{item_id}.intermediario.json")
        if not source.exists() and execute:
            issues.append(f"fonte ausente: {source.relative_to(self.root)}")
            return self._write_step("process", source, target, {}, issues, execute)
        raw = self._read_json(source) if source.exists() else {}
        normalized = self._normalize_text(str(raw.get("conteudo", "")))
        hash_conteudo = self._hash(normalized)
        payload = {
            "item_id": raw.get("item_id", item_id),
            "editoria": raw.get("editoria"),
            "titulo": self._normalize_title(str(raw.get("titulo", ""))),
            "primary_entity": raw.get("primary_entity"),
            "fonte": raw.get("fonte"),
            "url": raw.get("url"),
            "conteudo_normalizado": normalized,
            "hash_conteudo": hash_conteudo,
            "dedupe_check": self._dedupe_check(hash_conteudo, item_id),
            "status": "intermediario_processado",
            "created_at": self._now(),
            "manifesto_processamento": {
                "source_agent": "v4_processador",
                "normalizacao": "strip_spaces",
                "hash_algorithm": "sha256",
            },
        }
        issues.extend(self._required_issues(payload, "required_intermediate_fields"))
        return self._write_step("process", source, target, payload, issues, execute)

    def audit(self, item_id: str, execute: bool = False) -> IngestionStep:
        issues = self._check_read("auditor", "intermediario") + self._check_write("auditor", "auditado")
        source = self._path("intermediario", f"{item_id}.intermediario.json")
        target = self._path("auditado", f"{item_id}.json")
        if not source.exists() and execute:
            issues.append(f"fonte ausente: {source.relative_to(self.root)}")
            return self._write_step("audit", source, target, {}, issues, execute)
        inter = self._read_json(source) if source.exists() else {}
        audit_policy = self.contract["audit_policy"]
        if audit_policy["bloquear_conteudo_vazio"] and not str(inter.get("conteudo_normalizado", "")).strip():
            issues.append("conteudo_vazio")
        if audit_policy["bloquear_titulo_vazio"] and not str(inter.get("titulo", "")).strip():
            issues.append("titulo_vazio")
        payload = {
            "item_id": inter.get("item_id", item_id),
            "editoria": inter.get("editoria"),
            "titulo": inter.get("titulo"),
            "primary_entity": inter.get("primary_entity"),
            "fonte": inter.get("fonte"),
            "url": inter.get("url"),
            "conteudo": inter.get("conteudo_normalizado"),
            "hash_conteudo": inter.get("hash_conteudo"),
            "status": "auditado_ingestao",
            "created_at": self._now(),
            "manifesto_auditoria": {
                "source_agent": "v4_auditor_ingestao",
                "fonte_validada": audit_policy["fonte_validada_default"],
                "risco_juridico_revisado": audit_policy["risco_juridico_revisado_default"],
                "qualidade_minima": audit_policy["qualidade_minima_default"],
                "dedupe_check": inter.get("dedupe_check"),
            },
        }
        issues.extend(self._required_issues(payload, "required_audited_fields"))
        return self._write_step("audit", source, target, payload, issues, execute)

    def _write_step(
        self,
        step: str,
        source: Path | None,
        target: Path,
        payload: dict[str, Any],
        issues: list[str],
        execute: bool,
    ) -> IngestionStep:
        mode = "blocked" if issues else "planned"
        if execute and not issues:
            if target.exists():
                mode = "skipped_existing"
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                mode = "created"
        return IngestionStep(
            step=step,
            ok=not issues,
            mode=mode,
            source_path=str(source.relative_to(self.root)) if source else None,
            target_path=str(target.relative_to(self.root)),
            issues=issues,
        )

    def _dedupe_check(self, hash_conteudo: str, item_id: str) -> dict[str, Any]:
        duplicates: list[str] = []
        for layer in ["intermediario", "auditado"]:
            for path in self._layer_path(layer).glob("*.json"):
                if item_id in path.name:
                    continue
                try:
                    data = self._read_json(path)
                except json.JSONDecodeError:
                    continue
                if data.get("hash_conteudo") == hash_conteudo:
                    duplicates.append(str(path.relative_to(self.root)))
        return {"hash_conteudo": hash_conteudo, "duplicate_paths": duplicates, "is_duplicate": bool(duplicates)}

    def _check_read(self, role: str, layer: str) -> list[str]:
        decision = self.layers.decide(role, "read", layer)
        return [] if decision.allowed else [f"read {layer}: {decision.reason}"]

    def _check_write(self, role: str, layer: str) -> list[str]:
        decision = self.layers.decide(role, "write", layer)
        return [] if decision.allowed else [f"write {layer}: {decision.reason}"]

    def _required_issues(self, payload: dict[str, Any], key: str) -> list[str]:
        return [f"campo_obrigatorio_ausente:{field}" for field in self.contract[key] if payload.get(field) in (None, "")]

    def _path(self, layer: str, filename: str) -> Path:
        return self._layer_path(layer) / filename

    def _layer_path(self, layer: str) -> Path:
        return self.root / self.layers.layers[layer]["path"]

    @staticmethod
    def _normalize_text(text: str) -> str:
        return " ".join((text or "").split())

    @staticmethod
    def _normalize_title(text: str) -> str:
        return " ".join((text or "").strip().split())

    @staticmethod
    def _hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))
