from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agentes import DEFAULT_AGENTS_CONTRACT, TechnicalAgentFactory


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida agentes tecnicos V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_AGENTS_CONTRACT, help="Contrato de agentes V4")
    parser.add_argument("--agent", help="Agente especifico")
    parser.add_argument("--strict", action="store_true", help="Retorna erro se algum agente estiver invalido")
    args = parser.parse_args()

    factory = TechnicalAgentFactory(Path(args.root), args.contract)
    specs = [factory.build(args.agent)] if args.agent else factory.validate_all()
    payload = {"contract": args.contract, "agents": [spec.as_dict() for spec in specs]}
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    if args.strict and not all(spec.valid for spec in specs):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
