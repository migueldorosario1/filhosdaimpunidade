from __future__ import annotations

import argparse
import json
from pathlib import Path

from .llm_orchestrator import DEFAULT_ORCHESTRATION_CONTRACT, V4LLMOrchestrator


def main() -> int:
    parser = argparse.ArgumentParser(description="Orquestracao LLM V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_ORCHESTRATION_CONTRACT, help="Contrato de orquestracao V4")
    parser.add_argument("--editoria", default="v4_ciencia_tecnologia_ia")
    parser.add_argument("--funcao", default="redacao")
    parser.add_argument("--idempotency-key", default="cli")
    parser.add_argument("--exclude-provider", default=None)
    parser.add_argument("--list-candidates", action="store_true")
    args = parser.parse_args()

    orchestrator = V4LLMOrchestrator(Path(args.root), args.contract)
    payload: dict[str, object] = {"contract": args.contract}
    if args.list_candidates:
        payload["candidates"] = [
            candidate.as_dict() for candidate in orchestrator.valid_candidates(args.editoria, args.funcao)
        ]
    payload["selection"] = orchestrator.select(
        args.editoria,
        args.funcao,
        args.idempotency_key,
        exclude_provider=args.exclude_provider,
    ).as_dict()
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
