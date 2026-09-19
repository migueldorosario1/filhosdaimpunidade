from __future__ import annotations

import argparse
import json
from pathlib import Path

from .wordpress_media import DEFAULT_WORDPRESS_MEDIA_CONTRACT, V4WordPressMediaMapper, WordPressMediaMapping


def main() -> int:
    parser = argparse.ArgumentParser(description="Mapeamento V4 entre imagem auditada e WordPress Media.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_WORDPRESS_MEDIA_CONTRACT, help="Contrato WordPress Media V4")
    parser.add_argument("--image-id", required=True)
    parser.add_argument("--wp-media-id", type=int)
    parser.add_argument("--source", default="")
    parser.add_argument("--url", default="")
    parser.add_argument("--credit", default="")
    parser.add_argument("--license", default="")
    parser.add_argument("--operator", default="codex")
    parser.add_argument("--lookup", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    mapper = V4WordPressMediaMapper(Path(args.root), args.contract)
    if args.lookup:
        result = {"ok": True, "mapping": mapper.lookup(args.image_id)}
    else:
        if args.wp_media_id is None:
            raise SystemExit("--wp-media-id e obrigatorio fora de --lookup")
        result = mapper.add_mapping(
            WordPressMediaMapping(
                image_id=args.image_id,
                wp_media_id=args.wp_media_id,
                source=args.source,
                url=args.url,
                credit=args.credit,
                license=args.license,
                operator=args.operator,
            ),
            execute=args.execute,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
