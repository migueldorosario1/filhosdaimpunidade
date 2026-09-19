from __future__ import annotations

import argparse
import json
from pathlib import Path

from .llm_dashboard import DEFAULT_LLM_DASHBOARD_CONTRACT, V4LLMDashboard


def main() -> int:
    parser = argparse.ArgumentParser(description="Painel local V4 de comparacao LLM.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_LLM_DASHBOARD_CONTRACT, help="Contrato do painel V4")
    parser.add_argument("--execute", action="store_true", help="Grava JSON e Markdown em agent_data/v4/reports/.")
    parser.add_argument("--markdown", action="store_true", help="Imprime Markdown em vez de JSON.")
    args = parser.parse_args()

    dashboard = V4LLMDashboard(Path(args.root), args.contract)
    result = dashboard.build(execute=args.execute)
    if args.markdown:
        print(dashboard.to_markdown(result["report"]), end="")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
