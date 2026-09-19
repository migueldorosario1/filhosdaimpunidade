from __future__ import annotations

import argparse
import json
from pathlib import Path

from .wordpress_publicador import DEFAULT_WORDPRESS_PUBLISHER_CONTRACT, V4WordPressPublisher


def main() -> int:
    parser = argparse.ArgumentParser(description="Publicador WordPress V4 seguro.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_WORDPRESS_PUBLISHER_CONTRACT, help="Contrato do publicador WordPress V4")
    parser.add_argument("--source-path", required=True, help="Arquivo JSON em v4_data/publicado ou auditado.")
    parser.add_argument("--status", default=None, help="Status WordPress desejado: pending/draft em modo real.")
    parser.add_argument("--real", action="store_true", help="Tenta publicar no WordPress real se o contrato permitir.")
    parser.add_argument("--execute", action="store_true", help="Grava tentativa JSONL.")
    args = parser.parse_args()

    publisher = V4WordPressPublisher(Path(args.root), args.contract)
    result = publisher.publish_file(args.source_path, status=args.status, real=args.real, execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
