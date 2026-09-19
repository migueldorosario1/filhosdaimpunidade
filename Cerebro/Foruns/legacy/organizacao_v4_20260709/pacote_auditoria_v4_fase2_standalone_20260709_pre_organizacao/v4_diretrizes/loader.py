from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .schema import DirectiveDocument


class DirectiveLoader:
    """Le arquivos externos do V4 sem embutir diretriz no codigo."""

    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()

    def read_text_doc(self, rel_path: str | Path, required: bool = True) -> DirectiveDocument | None:
        path = self._resolve(rel_path)
        if not path.exists():
            if required:
                raise FileNotFoundError(f"Diretriz obrigatoria ausente: {path}")
            return None
        content = path.read_text(encoding="utf-8")
        return DirectiveDocument(path=path, content=content, sha256=self._sha256(content))

    def read_json(self, rel_path: str | Path) -> dict[str, Any]:
        path = self._resolve(rel_path)
        if not path.exists():
            raise FileNotFoundError(f"JSON obrigatorio ausente: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    def read_optional_docs(self, rel_paths: list[str]) -> list[DirectiveDocument]:
        docs: list[DirectiveDocument] = []
        for rel_path in rel_paths:
            doc = self.read_text_doc(rel_path, required=False)
            if doc is not None:
                docs.append(doc)
        return docs

    def _resolve(self, rel_path: str | Path) -> Path:
        path = Path(rel_path)
        if path.is_absolute():
            return path
        return self.root / path

    @staticmethod
    def _sha256(content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
