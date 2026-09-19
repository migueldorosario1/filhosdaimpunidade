from __future__ import annotations

import base64
import fcntl
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .loader import DirectiveLoader
from .wordpress_media import V4WordPressMediaMapper


DEFAULT_WORDPRESS_PUBLISHER_CONTRACT = "diretrizes/v4_wordpress_publicador_v1.json"


@dataclass(frozen=True)
class WordPressPublishAttempt:
    item_id: str
    editoria: str
    mode: str
    outcome: str
    payload: dict[str, Any]
    issues: list[str]
    wp_response: dict[str, Any] | None = None
    timestamp: str | None = None
    schema_version: str = "v1"

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "timestamp": self.timestamp or datetime.now(timezone.utc).isoformat(),
            "item_id": self.item_id,
            "editoria": self.editoria,
            "mode": self.mode,
            "outcome": self.outcome,
            "payload": self.payload,
            "issues": self.issues,
            "wp_response": self.wp_response or {},
        }


class V4WordPressPublisher:
    """Publicador WordPress V4 seguro: dry-run por padrao, real bloqueado no contrato inicial."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_WORDPRESS_PUBLISHER_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract_path = contract_path
        self.contract = self.loader.read_json(contract_path)
        self.media_mapper = V4WordPressMediaMapper(self.root)

    def publish_file(
        self,
        source_path: str | Path,
        status: str | None = None,
        real: bool = False,
        execute: bool = False,
    ) -> dict[str, Any]:
        path = self.root / source_path
        payload = json.loads(path.read_text(encoding="utf-8"))
        return self.publish_payload(payload, status=status, real=real, execute=execute)

    def publish_payload(
        self,
        source: dict[str, Any],
        status: str | None = None,
        real: bool = False,
        execute: bool = False,
    ) -> dict[str, Any]:
        issues = self._validate_source(source)
        wp_payload = self._build_wp_payload(source, status=status)
        if real:
            issues.extend(self._validate_real_publish(wp_payload))
        outcome = "blocked" if issues else ("ready_real" if real else "dry_run")
        wp_response: dict[str, Any] | None = None
        if real and not issues:
            wp_response = self._post_wordpress(wp_payload)
            outcome = "posted" if wp_response.get("ok") is True else "blocked_wp_error"
            if wp_response.get("ok") is not True:
                issues.append(str(wp_response.get("error", "wp_error")))
        attempt = WordPressPublishAttempt(
            item_id=str(source.get("item_id", "")),
            editoria=str(source.get("editoria", "")),
            mode="real" if real else "dry_run",
            outcome=outcome,
            payload=wp_payload,
            issues=issues,
            wp_response=wp_response,
        )
        if execute:
            self._append_attempt(attempt)
        return {
            "ok": not issues,
            "mode": "real" if real else "dry_run",
            "outcome": outcome,
            "attempt": attempt.as_dict(),
        }

    def _validate_source(self, source: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        for field_name in self.contract["source"]["required_fields"]:
            if source.get(field_name) in (None, ""):
                issues.append(f"campo_publicacao_ausente:{field_name}")
        featured = source.get("featured_media") or {}
        for field_name in self.contract["source"]["featured_media_required_fields"]:
            if featured.get(field_name) in (None, ""):
                issues.append(f"featured_media_campo_ausente:{field_name}")
        if featured and featured.get("safe_to_publish") is not True:
            issues.append("featured_media_nao_auditada")
        return issues

    def _validate_real_publish(self, wp_payload: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        real_cfg = self.contract["real_publish"]
        if real_cfg.get("enabled") is not True:
            issues.append("publicacao_real_desabilitada_no_contrato")
        status = wp_payload.get("status")
        if status not in set(real_cfg["allowed_statuses"]):
            issues.append(f"status_wp_nao_permitido:{status}")
        if status in set(real_cfg["forbidden_statuses"]):
            issues.append(f"status_wp_proibido:{status}")
        if not isinstance(wp_payload.get("featured_media"), int):
            issues.append("featured_media_wp_id_ausente")
        issues.extend(self._encoding_issues(wp_payload))
        env = real_cfg["env"]
        for label, env_name in env.items():
            if not os.environ.get(env_name):
                issues.append(f"env_wp_ausente:{label}")
        return issues

    def _encoding_issues(self, wp_payload: dict[str, Any]) -> list[str]:
        cfg = self.contract.get("encoding_validation", {})
        if cfg.get("enabled_for_real_publish") is not True:
            return []
        text = " ".join([str(wp_payload.get("title", "")), str(wp_payload.get("content", ""))])
        issues: list[str] = []
        for marker in cfg.get("reject_mojibake_markers", []):
            if marker and marker in text:
                issues.append("encoding_mojibake_detectado")
                break
        letters = [char for char in text if char.isalpha()]
        min_letters = int(cfg.get("min_letters_for_ascii_check", 120))
        if (
            cfg.get("reject_ascii_only_long_portuguese_payload") is True
            and len(letters) >= min_letters
            and all(ord(char) < 128 for char in letters)
        ):
            issues.append("encoding_portugues_ascii_sem_acentos")
        return issues

    def _build_wp_payload(self, source: dict[str, Any], status: str | None = None) -> dict[str, Any]:
        featured = source.get("featured_media") or {}
        wp_media_field = self.contract["source"]["wp_media_id_field"]
        wp_media_id = featured.get(wp_media_field)
        if not isinstance(wp_media_id, int):
            mapping = self.media_mapper.lookup(str(featured.get("image_id", "")))
            if mapping:
                wp_media_id = mapping.get("wp_media_id")
        content = source.get("texto_dry_run") or source.get("conteudo") or ""
        credit = featured.get("credit")
        license_text = featured.get("license")
        if credit or license_text:
            content = f"{content}\n\n<p><em>Imagem: {credit or 'credito nao informado'} — {license_text or 'licenca nao informada'}</em></p>"
        return {
            "title": source.get("titulo", ""),
            "content": content,
            "status": status or self.contract["wordpress_payload"]["status_default"],
            "featured_media": wp_media_id,
            "meta": {
                "v4_item_id": source.get("item_id"),
                "v4_curadoria_id": source.get("curadoria_id"),
                "v4_editoria": source.get("editoria"),
                "v4_primary_entity": source.get("primary_entity"),
                "v4_featured_media_image_id": featured.get("image_id"),
            },
        }

    def _post_wordpress(self, wp_payload: dict[str, Any]) -> dict[str, Any]:
        env = self.contract["real_publish"]["env"]
        base_url = os.environ[env["url"]].rstrip("/")
        user = os.environ[env["user"]]
        password = os.environ[env["app_password"]]
        token = base64.b64encode(f"{user}:{password}".encode("utf-8")).decode("ascii")
        req = urllib.request.Request(
            f"{base_url}/wp-json/wp/v2/posts",
            data=json.dumps(wp_payload, ensure_ascii=False).encode("utf-8"),
            headers={"Authorization": f"Basic {token}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                body = json.loads(response.read().decode("utf-8", errors="replace"))
            return {"ok": True, "status": response.status, "body": body}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            return {"ok": False, "status": exc.code, "error": body[:1000]}
        except Exception as exc:  # noqa: BLE001 - fronteira de rede
            return {"ok": False, "error": str(exc)}

    def _append_attempt(self, attempt: WordPressPublishAttempt) -> None:
        payload = attempt.as_dict()
        output_dir = self.root / self.contract["store"]["path"]
        output_dir.mkdir(parents=True, exist_ok=True)
        day = datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00")).date().isoformat().replace("-", "")
        path = output_dir / f"{self.contract['store']['filename_prefix']}_{day}.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
