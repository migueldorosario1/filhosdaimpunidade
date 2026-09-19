from __future__ import annotations

import json
import os
import re
import sqlite3
import unicodedata
from pathlib import Path
from typing import Any

from .imagem_destacada import DEFAULT_FEATURED_IMAGE_CONTRACT, MediaCandidate
from .loader import DirectiveLoader


class V4MediaSourceCollector:
    """Coletores V4 de midia. Apenas normalizam candidatos; nao aprovam imagem."""

    def __init__(self, root: str | Path = ".", contract_path: str = DEFAULT_FEATURED_IMAGE_CONTRACT) -> None:
        self.loader = DirectiveLoader(root)
        self.root = self.loader.root
        self.contract = self.loader.read_json(contract_path)

    def collect_ouro_sqlite(self, title: str, text: str = "", primary_entity: str = "", limit: int = 5) -> dict[str, Any]:
        source = self._source_config("ouro_sqlite")
        db_path = os.environ.get(source.get("path_env", ""), source.get("fallback_path", ""))
        if not db_path or not self._path_exists(db_path):
            return {"ok": False, "source": "ouro_sqlite", "reason": "db_unavailable", "db_path": db_path, "candidates": []}
        tokens = self._tokens(" ".join([title, text, primary_entity]))
        if not tokens:
            return {"ok": False, "source": "ouro_sqlite", "reason": "no_tokens", "candidates": []}
        rows = self._query_ouro(db_path, tokens, limit=max(limit * 8, 20))
        candidates = [self._row_to_candidate(row) for row in rows]
        candidates = [candidate for candidate in candidates if candidate is not None]
        candidates.sort(key=lambda item: item.score, reverse=True)
        return {
            "ok": True,
            "source": "ouro_sqlite",
            "db_path": db_path,
            "count": len(candidates[:limit]),
            "candidates": [candidate.as_dict() for candidate in candidates[:limit]],
        }

    def _query_ouro(self, db_path: str, tokens: list[str], limit: int) -> list[dict[str, Any]]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        try:
            fts = " OR ".join(token for token in tokens[:14] if re.fullmatch(r"[a-z0-9]{3,}", token))
            if fts:
                try:
                    rows = conn.execute(
                        """
                        SELECT i.*, m.r2_key, m.r2_url AS r2_original_url,
                               m.r2_portal_key, m.r2_portal_url, m.largura_portal,
                               m.altura_portal, m.bytes_portal, m.content_type_portal,
                               m.credito, m.licenca, m.status_direitos, m.metadados_json
                        FROM midia_ouro_fts f
                        JOIN midia_ouro_indice i ON i.hash_sha256 = f.hash_sha256
                        JOIN midia_ouro m ON m.hash_sha256 = i.hash_sha256
                        WHERE midia_ouro_fts MATCH ?
                          AND COALESCE(m.uso_automatico,0)=1
                        LIMIT ?
                        """,
                        (fts, limit),
                    ).fetchall()
                    if rows:
                        return [dict(row) for row in rows]
                except sqlite3.Error:
                    pass
            likes = tokens[:5]
            where = " OR ".join(["i.texto_busca LIKE ?" for _ in likes])
            params: list[Any] = [f"%{token}%" for token in likes]
            params.append(limit)
            rows = conn.execute(
                f"""
                SELECT i.*, m.r2_key, m.r2_url AS r2_original_url,
                       m.r2_portal_key, m.r2_portal_url, m.largura_portal,
                       m.altura_portal, m.bytes_portal, m.content_type_portal,
                       m.credito, m.licenca, m.status_direitos, m.metadados_json
                FROM midia_ouro_indice i
                JOIN midia_ouro m ON m.hash_sha256 = i.hash_sha256
                WHERE COALESCE(m.uso_automatico,0)=1
                  AND ({where})
                LIMIT ?
                """,
                params,
            ).fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def _row_to_candidate(self, row: dict[str, Any]) -> MediaCandidate | None:
        image_id = str(row.get("hash_sha256") or row.get("media_id") or "")
        if not image_id:
            return None
        metadata: dict[str, Any] = {}
        try:
            metadata = json.loads(row.get("metadados_json") or "{}")
        except (TypeError, ValueError):
            metadata = {}
        return MediaCandidate(
            image_id=image_id,
            source="ouro_sqlite",
            url=str(row.get("r2_portal_url") or row.get("r2_original_url") or row.get("url_origem") or ""),
            title=str(row.get("titulo") or row.get("entidade") or ""),
            credit=str(row.get("credito") or ""),
            license=str(row.get("licenca") or ""),
            rights_status=str(row.get("status_direitos") or ""),
            width=int(row.get("largura_portal") or row.get("largura") or 0),
            height=int(row.get("altura_portal") or row.get("altura") or 0),
            entity=str(row.get("entidade") or ""),
            score=float(row.get("score") or row.get("match_score") or 0.0),
            content_type=str(row.get("content_type_portal") or "image/jpeg"),
            caption=str(row.get("legenda") or row.get("descricao") or ""),
            metadata=metadata,
        )

    def _source_config(self, name: str) -> dict[str, Any]:
        for source in self.contract.get("sources", []):
            if source.get("name") == name:
                return source
        raise KeyError(f"Fonte de midia V4 ausente: {name}")

    @staticmethod
    def _path_exists(path: str) -> bool:
        try:
            return Path(path).exists()
        except OSError:
            return False

    @staticmethod
    def _tokens(text: str) -> list[str]:
        normalized = "".join(
            char for char in unicodedata.normalize("NFKD", (text or "").lower()) if not unicodedata.combining(char)
        )
        return list(dict.fromkeys(re.findall(r"[a-z0-9]{3,}", normalized)))
