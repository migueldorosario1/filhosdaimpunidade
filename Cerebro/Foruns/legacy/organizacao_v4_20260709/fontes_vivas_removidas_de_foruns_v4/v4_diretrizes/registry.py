from __future__ import annotations

from pathlib import Path
from typing import Any

from .loader import DirectiveLoader


class V4Registry:
    def __init__(
        self,
        root: str | Path = ".",
        mapa_path: str = "diretrizes/mapa_v4_contexto_llm.json",
        llm_routes_path: str | None = None,
    ) -> None:
        self.loader = DirectiveLoader(root)
        self.mapa_path = mapa_path
        self.mapa = self.loader.read_json(mapa_path)
        self.llm_routes_path = llm_routes_path or self.mapa.get(
            "source_llm_context_routes",
            "Projeto Cafezinho Agentes/root/config/llm_context_routes.json",
        )
        self.llm_routes = self.loader.read_json(self.llm_routes_path)

    def resolve_editoria(self, editoria: str) -> str:
        editorias = self.mapa.get("editorias", {})
        aliases = self.mapa.get("aliases", {})
        if editoria in editorias:
            return editoria
        resolved = aliases.get(editoria)
        if resolved in editorias:
            return resolved
        fallback = self.mapa.get("defaults", {}).get("fallback_editoria")
        if fallback in editorias:
            return fallback
        raise KeyError(f"Editoria desconhecida e sem fallback: {editoria}")

    def get_editoria_config(self, editoria: str) -> dict[str, Any]:
        resolved = self.resolve_editoria(editoria)
        return self.mapa["editorias"][resolved]

    def resolve_contexto(self, editoria: str, funcao: str) -> str:
        config = self.get_editoria_config(editoria)
        funcoes = config.get("funcoes", {})
        if funcao in funcoes:
            return funcoes[funcao]
        default_funcoes = self.mapa.get("funcoes", {})
        if funcao in default_funcoes:
            return default_funcoes[funcao]["contexto_llm"]
        raise KeyError(f"Funcao V4 desconhecida: {funcao}")

    def get_context_tiers(self, contexto: str) -> list[str]:
        return [entry["tier"] for entry in self.get_context_entries(contexto)]

    def get_context_entries(self, contexto: str) -> list[dict[str, Any]]:
        contexts = self.llm_routes.get("contexts", {})
        if contexto not in contexts:
            raise KeyError(f"Contexto LLM ausente em llm_context_routes.json: {contexto}")
        raw_entries = contexts[contexto]
        entries: list[dict[str, Any]] = []
        for raw_entry in raw_entries:
            if isinstance(raw_entry, str):
                entries.append({"tier": raw_entry, "models": None})
            elif isinstance(raw_entry, dict) and "tier" in raw_entry:
                entries.append({"tier": raw_entry["tier"], "models": raw_entry.get("models")})
            else:
                raise ValueError(f"Entrada LLM invalida no contexto {contexto}: {raw_entry!r}")
        return entries
