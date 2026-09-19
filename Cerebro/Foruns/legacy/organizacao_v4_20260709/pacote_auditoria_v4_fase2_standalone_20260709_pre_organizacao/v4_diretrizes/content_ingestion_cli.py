from __future__ import annotations

import argparse
import json
from pathlib import Path

from .content_ingestion import DEFAULT_CONTENT_INGESTION_CONTRACT, V4ContentIngestion


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingestao V4: bruto -> intermediario -> auditado.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_CONTENT_INGESTION_CONTRACT)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    result = V4ContentIngestion(Path(args.root), args.contract).run_fixture(execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
