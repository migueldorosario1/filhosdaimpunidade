from __future__ import annotations

import argparse
import json
from pathlib import Path

from .imagem_destacada import DEFAULT_FEATURED_IMAGE_CONTRACT
from .media_sources import V4MediaSourceCollector


def main() -> int:
    parser = argparse.ArgumentParser(description="Coletores V4 de candidatos de midia.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_FEATURED_IMAGE_CONTRACT, help="Contrato de imagem destacada V4")
    parser.add_argument("--source", default="ouro_sqlite", choices=["ouro_sqlite"])
    parser.add_argument("--title", required=True)
    parser.add_argument("--text", default="")
    parser.add_argument("--primary-entity", default="")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    collector = V4MediaSourceCollector(Path(args.root), args.contract)
    if args.source == "ouro_sqlite":
        result = collector.collect_ouro_sqlite(args.title, args.text, args.primary_entity, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
