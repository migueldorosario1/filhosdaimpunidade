from __future__ import annotations

import argparse
import json

from .recompute_costs import V4CostRecomputer


def main() -> int:
    parser = argparse.ArgumentParser(description="Recomputa custos V4 antigos em trilha append-only.")
    parser.add_argument("--execute", action="store_true", help="Grava os resultados em agent_data/v4/receipts/recomputed/.")
    args = parser.parse_args()

    result = V4CostRecomputer().run(execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
