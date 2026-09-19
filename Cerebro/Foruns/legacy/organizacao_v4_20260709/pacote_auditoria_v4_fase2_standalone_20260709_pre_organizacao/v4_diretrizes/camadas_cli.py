from __future__ import annotations

import argparse
import json
from pathlib import Path

from .camadas import DEFAULT_LAYERS_CONTRACT, LayerAccessController


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida camadas de dados V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_LAYERS_CONTRACT, help="Contrato de camadas V4")
    parser.add_argument("--role", help="Papel a testar")
    parser.add_argument("--operation", choices=["read", "write"], help="Operacao a testar")
    parser.add_argument("--layer", help="Camada a testar")
    parser.add_argument("--ensure-dirs", action="store_true", help="Planeja criacao dos diretorios")
    parser.add_argument("--execute", action="store_true", help="Cria diretorios quando usado com --ensure-dirs")
    args = parser.parse_args()

    controller = LayerAccessController(Path(args.root), args.contract)
    payload: dict[str, object] = {"contract": args.contract}
    if args.role and args.operation and args.layer:
        payload["decision"] = controller.decide(args.role, args.operation, args.layer).as_dict()
    else:
        payload["checks"] = [decision.as_dict() for decision in controller.validate_contract()]
    if args.ensure_dirs:
        payload["directories"] = controller.ensure_directories(execute=args.execute)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
