from __future__ import annotations

import argparse
import json
from pathlib import Path

from .memoria import DEFAULT_MEMORY_CONTRACT, MemoryEvent, V4MemoryStore


def main() -> int:
    parser = argparse.ArgumentParser(description="Memoria append-only V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_MEMORY_CONTRACT, help="Contrato de memoria V4")
    parser.add_argument("--event-type", default="validacao")
    parser.add_argument("--severity", default="info")
    parser.add_argument("--source", default="codex")
    parser.add_argument("--summary", default="smoke memoria V4")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--payload-json", default="{}")
    parser.add_argument("--execute", action="store_true", help="Grava evento no JSONL")
    parser.add_argument("--tail", type=int, help="Mostra ultimos N eventos")
    args = parser.parse_args()

    store = V4MemoryStore(Path(args.root), args.contract)
    if args.tail is not None:
        print(json.dumps({"events": store.tail(args.tail)}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    event = MemoryEvent(
        event_type=args.event_type,
        severity=args.severity,
        source=args.source,
        summary=args.summary,
        tags=args.tag,
        payload=json.loads(args.payload_json),
    )
    result = store.append(event, execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
