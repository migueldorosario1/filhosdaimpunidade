from __future__ import annotations

import argparse
import json
from pathlib import Path

from .curadoria_tese import V4CuradoriaTese


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa curadoria de tese V4 em dry-run.")
    parser.add_argument("source", help="Arquivo JSON auditado de entrada.")
    parser.add_argument("--leitura", help="Arquivo JSON com leitura_corrente_timestamped.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    source_path = Path(args.root) / args.source
    source = json.loads(source_path.read_text(encoding="utf-8"))
    if args.leitura:
        leitura = json.loads((Path(args.root) / args.leitura).read_text(encoding="utf-8"))
    else:
        leitura = source.get("leitura_corrente_timestamped", {})
    payload = V4CuradoriaTese(args.root).create(source, leitura)
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if payload.get("status") != "curadoria_invalida" else 2


if __name__ == "__main__":
    raise SystemExit(main())
