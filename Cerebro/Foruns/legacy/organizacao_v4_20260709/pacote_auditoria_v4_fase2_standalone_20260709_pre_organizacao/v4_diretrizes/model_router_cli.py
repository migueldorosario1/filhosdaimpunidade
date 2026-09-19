from __future__ import annotations

import argparse
import json
from pathlib import Path

from .model_router import DEFAULT_MODEL_ROUTER_CONTRACT, V4ModelRouter


def main() -> int:
    parser = argparse.ArgumentParser(description="Roteador V4 de modelos por qualidade/custo.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_MODEL_ROUTER_CONTRACT, help="Contrato do roteador V4")
    parser.add_argument("--editoria", default="v4_ciencia_tecnologia_ia")
    parser.add_argument("--funcao", default="redacao")
    parser.add_argument("--idempotency-key", default="cli")
    parser.add_argument("--exclude-provider", default=None)
    args = parser.parse_args()

    router = V4ModelRouter(Path(args.root), args.contract)
    result = router.recommend(
        args.editoria,
        args.funcao,
        args.idempotency_key,
        exclude_provider=args.exclude_provider,
    )
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
