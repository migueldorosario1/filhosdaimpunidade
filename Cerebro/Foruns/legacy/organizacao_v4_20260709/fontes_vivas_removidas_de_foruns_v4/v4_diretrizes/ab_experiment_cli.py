from __future__ import annotations

import argparse
import json

from .ab_experiment import V4CuradoriaABExperiment


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa experimento A/B dry-run da curadoria V4.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--case", default="261439", choices=["261439"])
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    result = V4CuradoriaABExperiment(args.root).run_261439(execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
