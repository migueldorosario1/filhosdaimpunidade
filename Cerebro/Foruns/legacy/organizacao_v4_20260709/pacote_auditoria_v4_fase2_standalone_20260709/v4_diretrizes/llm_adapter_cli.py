from __future__ import annotations

import argparse
import json
from pathlib import Path

from .llm_adapter import DEFAULT_ADAPTER_CONTRACT, LLMRequest, V4LLMAdapter


def main() -> int:
    parser = argparse.ArgumentParser(description="Testa adaptador LLM V4")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_ADAPTER_CONTRACT, help="Contrato do adapter V4")
    parser.add_argument("--editoria", default="v4_ciencia_tecnologia_ia")
    parser.add_argument("--funcao", default="redacao")
    parser.add_argument("--titulo", default="Teste mock V4")
    parser.add_argument("--conteudo", default="Conteudo auditado para teste mock.")
    parser.add_argument("--idempotency-key", default="cli")
    parser.add_argument("--previous-provider", default=None, help="Provider anterior a excluir, usado em revisao")
    parser.add_argument("--mode", default=None)
    args = parser.parse_args()

    request = LLMRequest(
        editoria=args.editoria,
        funcao=args.funcao,
        titulo=args.titulo,
        conteudo=args.conteudo,
        idempotency_key=args.idempotency_key,
        previous_provider=args.previous_provider,
    )
    try:
        response = V4LLMAdapter(Path(args.root), args.contract).generate(request, mode=args.mode)
    except RuntimeError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2, sort_keys=True))
        return 2
    print(json.dumps({"ok": True, "response": response.as_dict()}, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
