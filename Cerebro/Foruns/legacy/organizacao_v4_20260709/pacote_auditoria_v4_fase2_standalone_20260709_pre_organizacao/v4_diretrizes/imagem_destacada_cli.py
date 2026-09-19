from __future__ import annotations

import argparse
import json
from pathlib import Path

from .imagem_destacada import DEFAULT_FEATURED_IMAGE_CONTRACT, MediaCandidate, V4FeaturedImageEvaluator
from .media_audit import V4AuditedMediaStore


def main() -> int:
    parser = argparse.ArgumentParser(description="Avaliador V4 de imagem destacada.")
    parser.add_argument("--root", default=".", help="Raiz do workspace")
    parser.add_argument("--contract", default=DEFAULT_FEATURED_IMAGE_CONTRACT, help="Contrato de imagem destacada V4")
    parser.add_argument("--title", required=True)
    parser.add_argument("--primary-entity", required=True)
    parser.add_argument("--candidate-json", required=True, help="JSON de um candidato ou lista de candidatos.")
    parser.add_argument("--requires-person", action="store_true", default=False)
    parser.add_argument("--execute", action="store_true", help="Grava decisao em agent_data/v4/media/decisions/.")
    parser.add_argument("--promote-audited", action="store_true", help="Promove a imagem selecionada para o acervo auditado.")
    args = parser.parse_args()

    raw = json.loads(args.candidate_json)
    items = raw if isinstance(raw, list) else [raw]
    candidates = [MediaCandidate(**item) for item in items]
    evaluator = V4FeaturedImageEvaluator(Path(args.root), args.contract)
    result = evaluator.select(
        candidates,
        title=args.title,
        primary_entity=args.primary_entity,
        requires_person=args.requires_person,
        execute=args.execute,
    )
    if args.promote_audited and result["ok"]:
        selected_id = result["decision"]["selected"]["candidate"]["image_id"]
        selected_eval = next(
            evaluation
            for evaluation in evaluator.evaluate_candidates(candidates, args.title, args.primary_entity, args.requires_person)
            if evaluation.candidate.image_id == selected_id
        )
        result["audit"] = V4AuditedMediaStore(Path(args.root), args.contract).promote(selected_eval, execute=args.execute)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
