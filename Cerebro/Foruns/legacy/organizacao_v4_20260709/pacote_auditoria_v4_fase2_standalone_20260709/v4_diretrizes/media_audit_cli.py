from __future__ import annotations

import argparse
import json
from pathlib import Path

from .imagem_destacada import DEFAULT_FEATURED_IMAGE_CONTRACT
from .media_audit import V4AuditedMediaStore


def main() -> int:
    parser = argparse.ArgumentParser(description="Acervo auditado V4 de midia.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_FEATURED_IMAGE_CONTRACT, help="Contrato de imagem destacada V4")
    parser.add_argument("--entity", required=True)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    store = V4AuditedMediaStore(Path(args.root), args.contract)
    result = {"ok": True, "entity": args.entity, "records": store.search(args.entity, args.limit)}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
