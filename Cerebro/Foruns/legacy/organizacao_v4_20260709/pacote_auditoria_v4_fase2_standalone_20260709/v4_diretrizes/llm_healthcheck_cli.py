from __future__ import annotations

import argparse
import json
from pathlib import Path

from .llm_healthcheck import DEFAULT_ADAPTER_CONTRACT, V4LLMHealthcheck


def main() -> int:
    parser = argparse.ArgumentParser(description="Healthcheck local LLM real V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_ADAPTER_CONTRACT, help="Contrato do adapter V4")
    parser.add_argument("--editoria", default="v4_ciencia_tecnologia_ia")
    parser.add_argument("--funcao", default="redacao")
    parser.add_argument("--strict", action="store_true", help="Retorna erro se modo real nao estiver liberado")
    args = parser.parse_args()

    report = V4LLMHealthcheck(Path(args.root), adapter_contract=args.contract).check(args.editoria, args.funcao)
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2, sort_keys=True))
    if args.strict and not report.ok:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
