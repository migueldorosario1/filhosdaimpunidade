from __future__ import annotations

import argparse
import json
from pathlib import Path

from .feedback import DEFAULT_FEEDBACK_CONTRACT, V4EditorFeedbackStore


def main() -> int:
    parser = argparse.ArgumentParser(description="Feedback do editor V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_FEEDBACK_CONTRACT, help="Contrato de feedback V4")
    parser.add_argument("--ranking", action="store_true", help="Mostra ranking agregado")
    parser.add_argument("--item-id", default="v4_fixture_004")
    parser.add_argument("--vertical", default="v4_ciencia_tecnologia_ia")
    parser.add_argument("--editor", default="miguel")
    parser.add_argument("--score", type=int, default=4)
    parser.add_argument("--sentiment", default="positivo")
    parser.add_argument("--comment", default="Feedback de teste V4.")
    parser.add_argument("--correction-class", default="nenhuma")
    parser.add_argument("--operation", default="produzir_dry_run")
    parser.add_argument("--execute", action="store_true", help="Grava feedback no JSONL")
    args = parser.parse_args()

    store = V4EditorFeedbackStore(Path(args.root), args.contract)
    if args.ranking:
        payload = {"ranking": store.ranking()}
    else:
        payload = store.record(
            item_id=args.item_id,
            vertical=args.vertical,
            editor=args.editor,
            score=args.score,
            sentiment=args.sentiment,
            comment=args.comment,
            correction_class=args.correction_class,
            operation=args.operation,
            execute=args.execute,
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if payload.get("ok", True) else 2


if __name__ == "__main__":
    raise SystemExit(main())
