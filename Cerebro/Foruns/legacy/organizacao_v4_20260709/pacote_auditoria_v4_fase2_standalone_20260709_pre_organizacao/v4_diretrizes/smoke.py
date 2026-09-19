from __future__ import annotations

import argparse
import json
from pathlib import Path

from .composer import ContractComposer
from .llm_validator import LLMTierValidator


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke local da camada de diretrizes V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--editoria", default="v4_politica_economia")
    parser.add_argument("--funcao", default="redacao")
    parser.add_argument("--json", action="store_true", help="Saida JSON resumida")
    parser.add_argument("--validate-llm", action="store_true", help="Valida tiers/modelos LLM externos")
    parser.add_argument("--strict", action="store_true", help="Retorna erro se a validacao LLM falhar")
    args = parser.parse_args()

    contract = ContractComposer(Path(args.root)).compose(args.editoria, args.funcao)
    summary = {
        "editoria": contract.editoria,
        "label": contract.label,
        "funcao": contract.funcao,
        "nobre": contract.nobre,
        "contexto_llm": contract.contexto_llm.name,
        "tiers": contract.contexto_llm.tiers,
        "nucleo_sha256": contract.nucleo.sha256,
        "diretriz_sha256": contract.diretriz.sha256,
        "memoria_bugs_count": len(contract.memoria_bugs),
        "metadata": contract.metadata,
    }
    if args.validate_llm:
        report = LLMTierValidator(Path(args.root)).validate(args.editoria, args.funcao)
        summary["llm_validation"] = report.as_dict()

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        for key, value in summary.items():
            print(f"{key}: {value}")
    if args.strict and args.validate_llm and not summary["llm_validation"]["ok"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
