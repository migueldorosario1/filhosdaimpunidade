from __future__ import annotations

import argparse
import json
from pathlib import Path

from .operational_dashboard import DEFAULT_OPERATIONAL_DASHBOARD_CONTRACT, V4OperationalDashboard


def main() -> int:
    parser = argparse.ArgumentParser(description="Painel operacional local V4.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_OPERATIONAL_DASHBOARD_CONTRACT)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    args = parser.parse_args()

    dashboard = V4OperationalDashboard(Path(args.root), args.contract)
    result = dashboard.build(execute=args.execute)
    if args.markdown:
        print(dashboard.to_markdown(result["report"]), end="")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
