from __future__ import annotations

import argparse
import json
from pathlib import Path

from .fluxo import DEFAULT_FLOW_CONTRACT, V4DryRunFlow


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa fluxo V4 local em dry-run")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_FLOW_CONTRACT, help="Contrato do fluxo V4")
    parser.add_argument("--execute", action="store_true", help="Materializa fixture e manifestos locais")
    args = parser.parse_args()

    result = V4DryRunFlow(Path(args.root), args.contract).run(execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
