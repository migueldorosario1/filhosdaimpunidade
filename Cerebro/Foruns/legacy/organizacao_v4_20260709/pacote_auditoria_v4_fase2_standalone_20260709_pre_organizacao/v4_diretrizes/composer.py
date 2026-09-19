from __future__ import annotations

from pathlib import Path
from typing import Any

from .registry import V4Registry
from .schema import EditorialContract, LLMContext


class ContractComposer:
    """Monta o contrato editorial V4 a partir de arquivos externos."""

    def __init__(self, root: str | Path = ".") -> None:
        self.registry = V4Registry(root)
        self.loader = self.registry.loader

    def compose(self, editoria: str, funcao: str = "redacao") -> EditorialContract:
        resolved = self.registry.resolve_editoria(editoria)
        config = self.registry.get_editoria_config(resolved)
        defaults = self.registry.mapa.get("defaults", {})

        contexto = self.registry.resolve_contexto(resolved, funcao)
        tiers = self.registry.get_context_tiers(contexto)

        nucleo = self.loader.read_text_doc(defaults["nucleo_editorial"])
        diretriz = self.loader.read_text_doc(config["diretriz"])
        freios = self.loader.read_json(defaults["freios_llm"])
        memoria = self.loader.read_optional_docs(defaults.get("memoria_bugs", []))

        metadata: dict[str, Any] = {
            "mapa_version": self.registry.mapa.get("_version"),
            "mapa_status": self.registry.mapa.get("_status"),
            "source_llm_context_routes": self.registry.mapa.get("source_llm_context_routes"),
            "reference_llm_context_routes": self.registry.mapa.get("reference_llm_context_routes"),
            "diretriz_path": config["diretriz"],
            "nucleo_path": defaults["nucleo_editorial"],
            "freios_path": defaults["freios_llm"],
            "operacao_path": defaults.get("operacao"),
        }

        return EditorialContract(
            editoria=resolved,
            label=config.get("label", resolved),
            funcao=funcao,
            contexto_llm=LLMContext(name=contexto, tiers=tiers),
            nobre=bool(config.get("nobre", False)),
            nucleo=nucleo,
            diretriz=diretriz,
            freios_llm=freios,
            memoria_bugs=memoria,
            metadata=metadata,
        )
