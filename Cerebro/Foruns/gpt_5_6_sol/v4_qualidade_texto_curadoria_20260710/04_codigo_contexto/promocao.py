from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


DEFAULT_PROMOTION_CONTRACT = "contratos/v4_promocao_preflight_v1.json"


class V4PromotionPreflight:
    """Preflight local para promocao do v4_labs ao V4 final, sem executar promocao."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_PROMOTION_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)

    def run(self, execute: bool = False) -> dict[str, Any]:
        checks: list[dict[str, Any]] = []
        checks.extend(self._required_paths())
        checks.extend(self._workspace_hygiene())
        checks.extend(self._contract_gates())
        checks.extend(self._collection_gates())

        issues = [check["name"] for check in checks if check["status"] == "issue"]
        warnings = [check["name"] for check in checks if check["status"] == "warning"]
        payload = {
            "schema_version": self.contract.get("_version", "v1"),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "contract": self.contract_path,
            "status": "promocao_shadow_aprovada" if not issues else "promocao_pendente_de_cura",
            "ok": not issues,
            "issues": issues,
            "warnings": warnings,
            "checks": checks,
            "decisions": self.contract.get("decisions", {}),
            "wordpress_real": False,
            "external_call": False,
            "promocao_real_executada": False,
        }
        if execute:
            path = self.output_path()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return payload

    def output_path(self) -> Path:
        output = self.contract["output"]
        return self.root / output["path"] / output["filename"]

    def _required_paths(self) -> list[dict[str, Any]]:
        checks: list[dict[str, Any]] = []
        for rel_path in self.contract.get("source", {}).get("required_paths", []):
            path = self.root / rel_path
            checks.append(self._check(f"required_path:{rel_path}", path.exists(), {"path": rel_path}))
        return checks

    def _workspace_hygiene(self) -> list[dict[str, Any]]:
        checks: list[dict[str, Any]] = []
        gates = self.contract.get("gates", {})
        all_paths = list(self.root.rglob("*"))
        if gates.get("forbid_symlinks"):
            symlinks = [self._rel(path) for path in all_paths if path.is_symlink()]
            checks.append(self._check("no_symlinks", not symlinks, {"matches": symlinks[:20], "count": len(symlinks)}))
        if gates.get("forbid_pycache"):
            pycache = [self._rel(path) for path in all_paths if path.name == "__pycache__"]
            checks.append(self._check("no_pycache", not pycache, {"matches": pycache[:20], "count": len(pycache)}))
        if gates.get("forbid_pyc"):
            pyc = [self._rel(path) for path in all_paths if path.suffix == ".pyc"]
            checks.append(self._check("no_pyc", not pyc, {"matches": pyc[:20], "count": len(pyc)}))
        if gates.get("forbid_env_files"):
            env_files = [self._rel(path) for path in all_paths if path.name == ".env" or path.name.endswith(".env")]
            checks.append(self._check("no_env_files", not env_files, {"matches": env_files[:20], "count": len(env_files)}))
        if gates.get("forbid_secret_patterns"):
            secrets = self._secret_matches()
            checks.append(self._check("no_secret_patterns", not secrets, {"matches": secrets[:20], "count": len(secrets)}))
        return checks

    def _contract_gates(self) -> list[dict[str, Any]]:
        checks: list[dict[str, Any]] = []
        gates = self.contract.get("gates", {})
        flow = self.loader.read_json("contratos/v4_fluxo_dry_run_v1.json")
        fact_check = self.loader.read_json("contratos/v4_fact_check_v1.json")
        wordpress = self.loader.read_json("contratos/v4_wordpress_publicador_v1.json")
        curadoria = self.loader.read_json("contratos/v4_curadoria_tese_v1.json")
        shadow = self.loader.read_json("contratos/v4_redator_shadow_v1.json")

        min_tests = int(gates.get("required_contract_tests_defined_min", gates.get("required_contract_tests_min", 0)) or 0)
        test_count = self._test_count()
        checks.append(self._check("contract_tests_defined_min", test_count >= min_tests, {"count": test_count, "min": min_tests}))

        if gates.get("require_wordpress_real_disabled"):
            enabled = wordpress.get("real_publish", {}).get("enabled")
            checks.append(self._check("wordpress_real_disabled", enabled is False, {"enabled": enabled}))

        if gates.get("require_collection_request_gate_on_publicador"):
            gate = wordpress.get("collection_request_gate", {})
            ok = (
                gate.get("enabled_for_real_publish") is True
                and gate.get("missing_blocks_real_publish") is True
                and {"recommended", "required"}.issubset(set(gate.get("block_statuses", [])))
                and "publicacao_real" in set(gate.get("block_required_before", []))
            )
            checks.append(self._check("publicador_collection_request_gate", ok, {"gate": gate}))

        if gates.get("require_fact_check_text_presence"):
            ok = (
                fact_check.get("check_type") == "metadata_plus_text_presence_heuristic"
                and fact_check.get("gates", {}).get("required_fact_must_appear_in_text") is True
            )
            checks.append(self._check("fact_check_text_presence", ok, {"check_type": fact_check.get("check_type")}))

        if gates.get("require_numeric_token_guard"):
            heuristic = fact_check.get("text_presence_heuristic", {})
            ok = (
                heuristic.get("numeric_tokens_always_preserved") is True
                and heuristic.get("numeric_tokens_must_match") is True
            )
            checks.append(self._check("fact_check_numeric_token_guard", ok, {"heuristic": heuristic}))

        if gates.get("require_regen_disabled_in_production_promotion"):
            promotion = flow.get("promocao_para_producao", {})
            ok = (
                promotion.get("regenera_artefato_fixture_invalido_deve_ser_false") is True
                and promotion.get("artefato_bloqueado_evidencia_append_only") is True
                and promotion.get("producao_nao_sobrescreve_bloqueio") is True
            )
            checks.append(self._check("production_regen_disabled_contract", ok, {"promocao_para_producao": promotion}))

        if gates.get("require_recommended_required_policy_documented"):
            curadoria_policy = curadoria.get("collection_request", {}).get("semantics", {}).get("policy_fase4_auditfix")
            shadow_policy = shadow.get("collection_request_semantics", {}).get("policy_fase4_auditfix")
            checks.append(
                self._check(
                    "recommended_required_policy_documented",
                    bool(curadoria_policy and shadow_policy),
                    {"curadoria_policy": curadoria_policy, "shadow_policy": shadow_policy},
                )
            )

        decisions = self.contract.get("decisions", {})
        if gates.get("require_decision_evidence_when_true"):
            checks.extend(self._decision_evidence_checks(decisions))
        if gates.get("block_promotion_if_policy_not_ratified"):
            ratified = decisions.get("recommended_required_policy_ratified") is True
            checks.append(
                self._check(
                    "recommended_required_policy_ratified",
                    ratified,
                    {"ratified": decisions.get("recommended_required_policy_ratified")},
                )
            )
        if decisions.get("gpt55_auditfix2_approved") is not True and self.contract.get("warnings", {}).get("gpt55_audit_recommended_before_promotion"):
            checks.append(self._warning("gpt55_audit_recommended_before_promotion", {"approved": decisions.get("gpt55_auditfix2_approved")}))
        return checks

    def _decision_evidence_checks(self, decisions: dict[str, Any]) -> list[dict[str, Any]]:
        checks: list[dict[str, Any]] = []
        evidence = self.contract.get("decision_evidence", {})
        required_fields = list(self.contract.get("decision_evidence_required_fields", []))
        required_any = list(self.contract.get("decision_evidence_required_any_of", []))
        for key, value in sorted(decisions.items()):
            if value is not True:
                continue
            item = evidence.get(key)
            ok = isinstance(item, dict) and all(item.get(field) not in (None, "", [], {}) for field in required_fields)
            if ok and required_any:
                ok = any(item.get(field) not in (None, "", [], {}) for field in required_any)
            checks.append(
                self._check(
                    f"decision_evidence:{key}",
                    ok,
                    {"decision": key, "evidence": item or {}, "required_fields": required_fields, "required_any_of": required_any},
                )
            )
        return checks

    def _collection_gates(self) -> list[dict[str, Any]]:
        if self.contract.get("gates", {}).get("block_promotion_if_collection_open_for_publicacao_real") is not True:
            return []
        matches: list[str] = []
        invalid: list[str] = []
        for path in sorted((self.root / "dados").glob("**/*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            collection = payload.get("collection_request")
            if collection in (None, "", [], {}):
                continue
            if not isinstance(collection, dict):
                invalid.append(f"{self._rel(path)}:collection_request_invalido")
                continue
            status = collection.get("status")
            required_before = collection.get("required_before")
            if not isinstance(status, str) or not isinstance(required_before, str):
                invalid.append(f"{self._rel(path)}:collection_request_invalido")
                continue
            if status in {"none", "resolved"} and required_before in {None, "", "none", "publicacao_real"}:
                continue
            if status not in {"none", "resolved", "recommended", "required"}:
                invalid.append(f"{self._rel(path)}:collection_request_status_desconhecido:{status}")
                continue
            if required_before not in {"none", "shadow_redacao", "redator_real_llm", "publicacao_real"}:
                invalid.append(f"{self._rel(path)}:collection_request_required_before_desconhecido:{required_before}")
                continue
            if status in {"recommended", "required"} and required_before == "publicacao_real":
                matches.append(self._rel(path))
            elif status in {"recommended", "required"}:
                matches.append(f"{self._rel(path)}:{status}:{required_before}")
        return [
            self._check("collection_request_publicacao_real_resolvida", not matches, {"matches": matches[:20], "count": len(matches)}),
            self._check("collection_request_valores_conhecidos", not invalid, {"matches": invalid[:20], "count": len(invalid)}),
        ]

    def _secret_matches(self) -> list[str]:
        cfg = self.contract.get("secret_scan", {})
        patterns = [re.compile(pattern) for pattern in cfg.get("patterns", [])]
        ignored = set(cfg.get("ignore_paths", []))
        matches: list[str] = []
        for path in sorted(self.root.rglob("*")):
            if not path.is_file() or self._rel(path) in ignored:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for pattern in patterns:
                if pattern.search(text):
                    matches.append(self._rel(path))
                    break
        return matches

    def _test_count(self) -> int:
        path = self.root / "codigo/test_contracts.py"
        if not path.exists():
            return 0
        content = path.read_text(encoding="utf-8")
        return len(re.findall(r"^def test_", content, flags=re.MULTILINE))

    def _rel(self, path: Path) -> str:
        return str(path.relative_to(self.root))

    @staticmethod
    def _check(name: str, ok: bool, details: dict[str, Any]) -> dict[str, Any]:
        return {"name": name, "status": "ok" if ok else "issue", "details": details}

    @staticmethod
    def _warning(name: str, details: dict[str, Any]) -> dict[str, Any]:
        return {"name": name, "status": "warning", "details": details}
