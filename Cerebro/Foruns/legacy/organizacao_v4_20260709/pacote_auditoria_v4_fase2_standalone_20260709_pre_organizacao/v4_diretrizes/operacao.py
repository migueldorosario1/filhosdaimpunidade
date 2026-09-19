from __future__ import annotations

import fnmatch
import shutil
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .schema import OperationAction, OperationReport


DEFAULT_CONTRACT = "diretrizes/v4_operacao_limpeza_ordem_backup_v1.json"


class V4OperationRunner:
    """Executa checks operacionais V4 a partir de contrato externo."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        scope = self.contract.get("escopo_operacional", {})
        self.scan_roots = [self.root / item for item in scope.get("scan_roots", ["."])]
        self.ignored_roots = [self.root / item for item in scope.get("ignored_roots", [])]

    def inspect(self, execute_safe: bool = False) -> OperationReport:
        actions: list[OperationAction] = []
        warnings: list[str] = []
        actions.extend(self._inspect_autolimpeza(execute_safe=execute_safe))
        actions.extend(self._inspect_autoorganizacao(warnings=warnings))
        actions.extend(self._inspect_autobackup(warnings=warnings))
        return OperationReport(
            dry_run=not execute_safe,
            contract_path=self.contract_path,
            actions=actions,
            warnings=warnings,
        )

    def _inspect_autolimpeza(self, execute_safe: bool) -> list[OperationAction]:
        actions: list[OperationAction] = []
        for rule in self.contract.get("autolimpeza", {}).get("regras", []):
            action = rule.get("acao")
            target = rule.get("alvo", "desconhecido")
            if action == "remover_pycache":
                actions.extend(self._pycache_actions(rule, target, execute_safe))
            elif action == "compactar_resolvidos":
                actions.extend(self._inbox_actions(rule, target))
            elif action == "mover_para_tmp_ou_backup":
                actions.extend(self._temporary_artifact_actions(rule, target))
        return actions

    def _pycache_actions(self, rule: dict[str, Any], target: str, execute_safe: bool) -> list[OperationAction]:
        actions: list[OperationAction] = []
        for path in self._scoped_glob(rule.get("padrao", "**/__pycache__")):
            if not path.is_dir():
                continue
            mode = "executed" if execute_safe and rule.get("seguro_em_dry_run") is True else "dry_run"
            if mode == "executed":
                shutil.rmtree(path)
            actions.append(
                OperationAction(
                    action="remover_pycache",
                    target=target,
                    path=str(path.relative_to(self.root)),
                    mode=mode,
                    reason="cache Python removivel e recriavel",
                )
            )
        return actions

    def _inbox_actions(self, rule: dict[str, Any], target: str) -> list[OperationAction]:
        actions: list[OperationAction] = []
        limit = int(rule.get("limite_linhas_recomendado", 120))
        for inbox_dir in self._scoped_glob("**/inbox_trindade"):
            if not inbox_dir.is_dir():
                continue
            for path in sorted(inbox_dir.glob("*.md")):
                try:
                    line_count = len(path.read_text(encoding="utf-8").splitlines())
                except UnicodeDecodeError:
                    continue
                if line_count <= limit:
                    continue
                actions.append(
                    OperationAction(
                        action="compactar_resolvidos",
                        target=target,
                        path=str(path.relative_to(self.root)),
                        mode="needs_review",
                        reason=f"{line_count} linhas; limite recomendado {limit}",
                    )
                )
        return actions

    def _temporary_artifact_actions(self, rule: dict[str, Any], target: str) -> list[OperationAction]:
        actions: list[OperationAction] = []
        patterns = list(rule.get("padroes", []))
        for path in self._scoped_rglob("*"):
            rel = str(path.relative_to(self.root))
            name = path.name
            if not any(fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(rel, pattern) for pattern in patterns):
                continue
            actions.append(
                OperationAction(
                    action="mover_para_tmp_ou_backup",
                    target=target,
                    path=rel,
                    mode="needs_review",
                    reason="artefato temporario detectado; contrato exige confirmacao para deletar",
                )
            )
        return sorted(actions, key=lambda item: item.path)

    def _inspect_autoorganizacao(self, warnings: list[str]) -> list[OperationAction]:
        actions: list[OperationAction] = []
        for category, pattern in self.contract.get("autoorganizacao", {}).get("categorias", {}).items():
            matches = self._match_pattern(pattern)
            if not matches:
                warnings.append(f"Categoria {category} sem arquivos: {pattern}")
            for path in matches:
                actions.append(
                    OperationAction(
                        action="catalogar_categoria",
                        target=category,
                        path=str(path.relative_to(self.root)),
                        mode="indexed",
                        reason=f"categoria V4: {category}",
                    )
                )

        for rel_path in self.contract.get("autoorganizacao", {}).get("indices_obrigatorios", []):
            path = self.root / rel_path
            actions.append(
                OperationAction(
                    action="verificar_indice_obrigatorio",
                    target="indice",
                    path=rel_path,
                    mode="present" if path.exists() else "missing",
                    reason="indice obrigatorio do V4",
                )
            )
        return actions

    def _inspect_autobackup(self, warnings: list[str]) -> list[OperationAction]:
        actions: list[OperationAction] = []
        backup = self.contract.get("autobackup", {})
        if backup.get("nao_usar_sync") is not True:
            warnings.append("Contrato de backup deveria manter nao_usar_sync=true.")
        if backup.get("exige_rclone_check") is not True:
            warnings.append("Contrato de backup deveria exigir rclone check.")
        for pattern in backup.get("escopo_padrao", []):
            for path in self._match_pattern(pattern):
                actions.append(
                    OperationAction(
                        action="incluir_em_checkpoint",
                        target="autobackup",
                        path=str(path.relative_to(self.root)),
                        mode="planned",
                        reason=f"escopo_padrao: {pattern}",
                    )
                )
        return actions

    def _match_pattern(self, pattern: str) -> list[Path]:
        if pattern.endswith("/"):
            path = self.root / pattern
            return [path] if path.exists() else []
        if "/" in pattern:
            return sorted(path for path in self.root.glob(pattern) if not self._is_ignored(path))
        return self._scoped_glob(pattern)

    def _scoped_glob(self, pattern: str) -> list[Path]:
        matches: list[Path] = []
        for base in self.scan_roots:
            if not base.exists():
                continue
            matches.extend(base.glob(pattern))
        return sorted({path for path in matches if not self._is_ignored(path)})

    def _scoped_rglob(self, pattern: str) -> list[Path]:
        matches: list[Path] = []
        for base in self.scan_roots:
            if not base.exists():
                continue
            matches.extend(base.rglob(pattern))
        return sorted({path for path in matches if not self._is_ignored(path)})

    def _is_ignored(self, path: Path) -> bool:
        resolved = path.resolve()
        for ignored in self.ignored_roots:
            if resolved == ignored.resolve() or ignored.resolve() in resolved.parents:
                return True
        return False
