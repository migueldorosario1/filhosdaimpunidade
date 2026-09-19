from __future__ import annotations

import argparse
import json
from pathlib import Path

from .operacao import DEFAULT_CONTRACT, V4OperationRunner


def main() -> int:
    parser = argparse.ArgumentParser(description="Operacao V4: limpeza, organizacao e backup")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_CONTRACT, help="Contrato operacional V4")
    parser.add_argument("--execute-safe", action="store_true", help="Executa apenas acoes seguras do contrato")
    parser.add_argument("--json", action="store_true", help="Saida JSON")
    parser.add_argument("--summary", action="store_true", help="Mostra apenas contagem por acao/modo")
    args = parser.parse_args()

    report = V4OperationRunner(Path(args.root), args.contract).inspect(execute_safe=args.execute_safe)
    payload = report.as_dict()
    if args.summary:
        counts: dict[str, int] = {}
        for action in payload["actions"]:
            key = f"{action['action']}:{action['mode']}"
            counts[key] = counts.get(key, 0) + 1
        print(json.dumps({"dry_run": payload["dry_run"], "counts": counts, "warnings": payload["warnings"]}, indent=2))
    elif args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"dry_run: {payload['dry_run']}")
        print(f"contract_path: {payload['contract_path']}")
        print(f"actions: {len(payload['actions'])}")
        for warning in payload["warnings"]:
            print(f"warning: {warning}")
        for action in payload["actions"]:
            print(
                f"{action['mode']}: {action['action']} "
                f"{action['target']} {action['path']} - {action['reason']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
