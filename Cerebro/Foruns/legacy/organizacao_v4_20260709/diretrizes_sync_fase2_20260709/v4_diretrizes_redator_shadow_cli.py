from __future__ import annotations

import argparse
import json
from pathlib import Path

from .redator_shadow import V4ShadowRedator


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera pacote de redacao shadow V4 sem chamada externa.")
    parser.add_argument("curadoria", help="Arquivo JSON de curadoria.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    path = Path(args.root) / args.curadoria
    payload = json.loads(path.read_text(encoding="utf-8"))
    result = V4ShadowRedator(args.root).create(payload, execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not result["issues"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
