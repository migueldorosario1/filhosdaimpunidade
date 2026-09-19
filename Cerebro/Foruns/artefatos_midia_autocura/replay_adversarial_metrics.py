#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
replay_adversarial_metrics.py — gate de regressão do pack adversário V4 mídia.

Uso:
  python3 replay_adversarial_metrics.py
  python3 replay_adversarial_metrics.py --cases adversarial_midia_cases_v0.jsonl
  python3 replay_adversarial_metrics.py --decisions decisions.jsonl
  python3 replay_adversarial_metrics.py --self-test-fail   # força regressão (teste do exit≠0)

Offline, sem rede, sem escrita em produção.
Exit 0 = sem regressão em hard cases e schema ok.
Exit ≠0 = hard case regrediu, schema inválido ou cobertura mínima falhou.

Autor: Grok (xAI) · policy_version midia-v0.1 · 2026-08-07
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HERE = Path(__file__).resolve().parent
DEFAULT_CASES = HERE / "adversarial_midia_cases_v0.jsonl"
POLICY_VERSION = "midia-v0.1"

# Hard cases: regressão aqui = exit ≠ 0 (cartinha Grok §Artefato + espec §11)
HARD_REASON_CODES = {
    "NOOP_FIRE",
    "SCHEMA_DRIFT",
    "IA_VERTICAL_FORBIDDEN",
    "LICENSE_EMPTY",
    "LICENSE_FORBIDDEN",
    "BINARY_CORRUPT",
    "COMMAND_TRUNCATED_BY_COMMENT",
    "WRITE_PERMISSION_DENIED",
    "OBJECT_MISSING",
}

REQUIRED_CASE_FIELDS = [
    "case_id",
    "class",
    "input",
    "expected_decision",
    "gold_role",
    "policy_version_min",
    "source_of_truth",
]

MIN_CORE_CASES = 15  # §2.2 da cartinha Grok
MAX_RUNTIME_S = 5.0


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                raise SystemExit(f"JSON inválido em {path}:{i}: {e}") from e
            if not isinstance(obj, dict):
                raise SystemExit(f"linha {i} de {path} não é objeto")
            rows.append(obj)
    return rows


def is_hard(case: Dict[str, Any]) -> bool:
    h = case.get("hardness")
    if h is True or h == "hard":
        return True
    rc = case.get("expected_reason_code")
    return rc in HARD_REASON_CODES


def validate_case_schema(case: Dict[str, Any], idx: int) -> List[str]:
    errs: List[str] = []
    for k in REQUIRED_CASE_FIELDS:
        if k not in case:
            errs.append(f"case[{idx}] falta campo {k}")
    if case.get("expected_decision") not in {"reject", "accept", "pending"}:
        errs.append(
            f"case[{idx}] expected_decision inválido: {case.get('expected_decision')!r}"
        )
    if case.get("gold_role") not in {"negative", "positive", "ambiguous"}:
        errs.append(f"case[{idx}] gold_role inválido: {case.get('gold_role')!r}")
    # system_state obrigatório para replay (espec + Claude/Grok)
    if "system_state" not in case:
        errs.append(f"case[{idx}/{case.get('case_id')}] system_state ausente")
    return errs


def deterministic_oracle(case: Dict[str, Any]) -> Tuple[str, Optional[str], List[str], int]:
    """
    Oráculo fail-closed offline (sem rede, sem LLM).
    Implementa hard-blocks determinísticos C0–C7 / L0–L1 + gates R4 de proveniência.
    Retorna: (decision, reason_code, flags, vision_calls_counted)
    """
    flags: List[str] = []
    inp = case.get("input") or {}
    vision_calls = 0

    # --- R4 / governança ---
    receipt_claim = inp.get("receipt_claim")
    if isinstance(receipt_claim, dict):
        ds = receipt_claim.get("decision_state")
        auth = receipt_claim.get("authorization_ref")
        roles = receipt_claim.get("actor_roles") or {}
        if ds in {"authorized", "executed", "verified"} and not auth:
            return "reject", "SCHEMA_DRIFT", ["FALSE_PROVENANCE"], 0
        if ds == "verified" and not (roles.get("verifier") or []):
            return "reject", "SCHEMA_DRIFT", ["FALSE_PROVENANCE"], 0

    promo = inp.get("promotion_request")
    if isinstance(promo, dict):
        if promo.get("decision_state") == "executed" and not promo.get("authorization_ref"):
            return "reject", "WRITE_PERMISSION_DENIED", ["MISSING_AUTHORIZATION"], 0

    artifact = inp.get("artifact")
    if isinstance(artifact, dict):
        claimed = artifact.get("delivery_state_claimed")
        real = artifact.get("delivery_state_real")
        if claimed == "delivered" and (
            real != "delivered" or artifact.get("readme_only") or not artifact.get("path_exists")
        ):
            return "reject", "OBJECT_MISSING", ["PROMISE_NOT_DELIVERY"], 0

    metrics = inp.get("metrics")
    if isinstance(metrics, dict):
        n = metrics.get("gold_sample_n") or 0
        cov = metrics.get("gold_coverage_ratio") or 0
        prec = metrics.get("identity_precision_at_1")
        if prec is not None and (n < 10 or cov < 0.1):
            flags.extend(["COVERAGE_INSUFFICIENT", "SUCCESS_WASHING_RISK"])
            return "reject", None, flags, 0

    # --- cron / NOOP ---
    cron = inp.get("cron")
    if isinstance(cron, dict):
        line = cron.get("line") or ""
        # comentário cortando comando útil
        if "#" in line:
            before, after = line.split("#", 1)
            if "flock" in before and ("intake" in after or ".py" in after):
                return "reject", "NOOP_FIRE", ["COMMAND_TRUNCATED_BY_COMMENT"], 0
        if cron.get("useful_units", 1) == 0 or not cron.get("intake_invoked", True):
            return "reject", "NOOP_FIRE", [], 0

    # --- schema drift em insert ---
    db_insert = inp.get("db_insert")
    if isinstance(db_insert, dict):
        missing = db_insert.get("columns_missing") or []
        if db_insert.get("ok") and missing:
            return "reject", "SCHEMA_DRIFT", [], 0
        if db_insert.get("acervo_write") is False and missing:
            return "reject", "SCHEMA_DRIFT", [], 0

    # --- fila / circuit ---
    queue = inp.get("queue")
    if isinstance(queue, dict):
        if (queue.get("net_growth") or 0) > 0 and (queue.get("cycles_positive_growth") or 0) >= 3:
            return "reject", "BACKLOG_NET_GROWTH", ["CAUSA_SUSPEITA_REQUIRED"], 0
        if queue.get("repair_failed") and queue.get("new_pauta_created_while_pending"):
            return "reject", "BACKLOG_NET_GROWTH", ["BAD_FEEDBACK_LOOP"], 0

    # --- retries idênticos ---
    retries = inp.get("retries")
    if isinstance(retries, list) and len(retries) >= 3:
        sigs = [
            (r.get("strategy_id"), r.get("query"), r.get("fonte"))
            for r in retries
            if isinstance(r, dict)
        ]
        if len(sigs) >= 3 and len(set(sigs)) == 1:
            return "reject", "QUERY_NO_PROGRESS", [], 0
        if inp.get("strategy_progression") is False and len(retries) >= 3:
            return "reject", "QUERY_NO_PROGRESS", [], 0

    # --- correção humana 1× sob pressa ---
    human = inp.get("human_action")
    if isinstance(human, dict):
        if (human.get("ocorrencias_7d") or 0) < 2:
            return "pending", None, ["NO_GENERALIZE_SINGLE_PREFERENCE"], 0

    # --- candidatas (funil C0–C7) ---
    candidatas = inp.get("candidatas") or []
    pauta = inp.get("pauta") or {}

    for c in candidatas:
        if not isinstance(c, dict):
            continue
        vc = int(c.get("vision_calls") or 0)
        vision_calls += vc

        # C0 binary / MIME
        if c.get("truncated") or c.get("mime_declared") and c.get("mime_declared") != c.get("mime"):
            if c.get("truncated") or (
                c.get("mime_declared") and c.get("mime_declared") != c.get("mime")
            ):
                # truncado ou MIME mentiroso
                if c.get("truncated"):
                    return "reject", "BINARY_CORRUPT", [], vision_calls
                return "reject", "MIME_INVALID", [], vision_calls

        dims = c.get("dims") or [0, 0]
        if isinstance(dims, (list, tuple)) and len(dims) >= 2:
            w, h = int(dims[0] or 0), int(dims[1] or 0)
            if w < 800 or h < 600:
                # se já truncado tratado acima; dims baixas sozinhas
                if c.get("truncated"):
                    return "reject", "BINARY_CORRUPT", [], vision_calls
                if w > 0 and h > 0 and (w < 800 or h < 600):
                    # ADV-007 tem truncated+dims; pure low dims
                    if c.get("truncated") is None and not c.get("mime_declared"):
                        return "reject", "DIMENSIONS_LOW", [], vision_calls

        # C2 license
        lic = c.get("license")
        if lic is None or (isinstance(lic, str) and lic.strip() == ""):
            return "reject", "LICENSE_EMPTY", [], vision_calls
        if isinstance(lic, str) and lic.strip().lower() in {
            "all rights reserved",
            "copyright",
            "© all rights reserved",
        }:
            return "reject", "LICENSE_FORBIDDEN", [], vision_calls

        # C3 soft-reuse
        if (c.get("reuse_count_7d_site") or 0) >= 3:
            return "reject", "REPEAT_COOLDOWN", [], vision_calls

        # C7 IA vertical
        ia_policy = pauta.get("ia_policy")
        if c.get("is_ai_generated") and ia_policy == "forbidden":
            return "reject", "IA_VERTICAL_FORBIDDEN", [], vision_calls
        slug = c.get("slug") or ""
        if "v4-featured" in slug and ia_policy == "forbidden":
            return "reject", "IA_VERTICAL_FORBIDDEN", [], vision_calls

        # C5 text/logo
        if c.get("dominant_content") in {"text_logo", "text", "logo", "meme"}:
            return "reject", "TEXT_OR_LOGO", [], vision_calls

        # stock genérico + juiz confiante (antes de entity genérico — ADV-014)
        ent = (pauta.get("entidade") or {}) if isinstance(pauta, dict) else {}
        want_id = ent.get("id_canonico")
        labels = c.get("entity_labels") or []
        tags = c.get("tags") or []
        judge = c.get("judge") or {}
        fonte = (c.get("fonte") or "").lower()
        if fonte in {"pixabay", "unsplash_stock", "shutterstock"} and judge.get("confidence", 0) >= 0.9:
            if want_id and want_id not in labels:
                return "reject", "GENERIC_STOCK", [], vision_calls

        # C4 entity tipada
        if want_id and ent.get("tipo") == "pessoa":
            if want_id not in labels:
                # tag genérica sem id
                if not labels and any(t in {"politica", "politician", "politics"} for t in tags):
                    return "reject", "ENTITY_MISMATCH", [], vision_calls
                if labels and want_id not in labels:
                    return "reject", "ENTITY_MISMATCH", [], vision_calls

        # C6 event / location
        want_event = (pauta.get("evento") or {}).get("tipo") if isinstance(pauta, dict) else None
        event_labels = c.get("event_labels") or []
        if want_event and event_labels:
            # se labels de evento existem e nenhum combina com o tipo da pauta
            if not any(want_event in str(e) for e in event_labels):
                # posse_2003 vs prisao
                return "reject", "EVENT_MISMATCH", [], vision_calls

        want_loc = (pauta.get("lugar") or {}).get("id_canonico") if isinstance(pauta, dict) else None
        loc_labels = c.get("location_labels") or []
        if want_loc and loc_labels and want_loc not in loc_labels:
            return "reject", "LOCATION_MISMATCH", [], vision_calls

        # vision em estágio barato = custo simulado ruim (flag, não decision)
        stage = inp.get("funil_stage_reached") or case.get("input", {}).get("funil_stage_reached")
        if vc > 0 and stage in {"C0", "C1", "C2", "C3"}:
            flags.append("VISION_ON_CHEAP_STAGE")

    # default: se esperava reject e nada disparou, accept (oracle incompleto — métrica de cobertura)
    return "accept", None, flags, vision_calls


def compare(
    expected_decision: str,
    expected_rc: Optional[str],
    got_decision: str,
    got_rc: Optional[str],
    expected_flags: Optional[List[str]],
    got_flags: List[str],
) -> Dict[str, Any]:
    decision_ok = expected_decision == got_decision
    # reason_code: se expected é null, ok qualquer; senão deve bater
    if expected_rc is None:
        rc_ok = True
    else:
        rc_ok = expected_rc == got_rc
    flags_ok = True
    if expected_flags:
        flags_ok = all(f in got_flags for f in expected_flags)
    return {
        "decision_ok": decision_ok,
        "reason_ok": rc_ok,
        "flags_ok": flags_ok,
        "pass": decision_ok and rc_ok and flags_ok,
    }


def run(
    cases_path: Path,
    decisions_path: Optional[Path],
    self_test_fail: bool,
) -> int:
    t0 = time.perf_counter()
    cases = load_jsonl(cases_path)

    schema_errs: List[str] = []
    for i, c in enumerate(cases):
        schema_errs.extend(validate_case_schema(c, i))

    if schema_errs:
        for e in schema_errs:
            print(f"SCHEMA_ERR: {e}", file=sys.stderr)
        print(json.dumps({"ok": False, "schema_errors": len(schema_errs)}, ensure_ascii=False))
        return 2

    if len(cases) < MIN_CORE_CASES:
        print(
            f"COVERAGE_ERR: {len(cases)} casos < mínimo {MIN_CORE_CASES}",
            file=sys.stderr,
        )
        return 2

    # decisões externas opcionais: {case_id, decision, reason_code}
    external: Dict[str, Dict[str, Any]] = {}
    if decisions_path:
        for row in load_jsonl(decisions_path):
            cid = row.get("case_id")
            if cid:
                external[cid] = row

    by_class: Dict[str, Counter] = defaultdict(Counter)
    hard_regressions: List[str] = []
    soft_fails: List[str] = []
    vision_waste = 0
    total_vision = 0
    results: List[Dict[str, Any]] = []

    for case in cases:
        cid = case["case_id"]
        cls = case.get("class", "unknown")
        exp_d = case["expected_decision"]
        exp_rc = case.get("expected_reason_code")
        exp_flags = case.get("expected_flags") or []

        if cid in external:
            got_d = external[cid].get("decision") or external[cid].get("expected_decision")
            got_rc = external[cid].get("reason_code") or external[cid].get("expected_reason_code")
            got_flags = external[cid].get("flags") or []
            vision = int(external[cid].get("vision_calls") or 0)
        else:
            got_d, got_rc, got_flags, vision = deterministic_oracle(case)

        if self_test_fail and is_hard(case):
            # injeta regressão artificial para provar exit≠0
            got_d = "accept"
            got_rc = None

        cmp = compare(exp_d, exp_rc, got_d, got_rc, exp_flags, got_flags)
        total_vision += vision
        stage = (case.get("input") or {}).get("funil_stage_reached")
        if vision > 0 and stage in {"C0", "C1", "C2", "C3"}:
            vision_waste += vision

        by_class[cls]["total"] += 1
        if cmp["pass"]:
            by_class[cls]["pass"] += 1
        else:
            by_class[cls]["fail"] += 1
            if is_hard(case):
                hard_regressions.append(
                    f"{cid}/{cls}: expected={exp_d}/{exp_rc} got={got_d}/{got_rc}"
                )
            else:
                soft_fails.append(
                    f"{cid}/{cls}: expected={exp_d}/{exp_rc} got={got_d}/{got_rc}"
                )

        results.append(
            {
                "case_id": cid,
                "class": cls,
                "hard": is_hard(case),
                "pass": cmp["pass"],
                "expected": {"decision": exp_d, "reason_code": exp_rc},
                "got": {"decision": got_d, "reason_code": got_rc, "flags": got_flags},
                "vision_calls": vision,
            }
        )

    elapsed = time.perf_counter() - t0
    n = len(cases)
    n_pass = sum(1 for r in results if r["pass"])
    n_hard = sum(1 for r in results if r["hard"])
    n_hard_pass = sum(1 for r in results if r["hard"] and r["pass"])

    precision_by_class = {
        cls: {
            "pass": c["pass"],
            "fail": c["fail"],
            "total": c["total"],
            "precision": round(c["pass"] / c["total"], 4) if c["total"] else 0.0,
        }
        for cls, c in sorted(by_class.items())
    }

    report = {
        "ok": len(hard_regressions) == 0 and elapsed < MAX_RUNTIME_S,
        "policy_version": POLICY_VERSION,
        "cases_path": str(cases_path),
        "n_cases": n,
        "n_pass": n_pass,
        "n_fail": n - n_pass,
        "overall_precision": round(n_pass / n, 4) if n else 0.0,
        "hard_cases": n_hard,
        "hard_pass": n_hard_pass,
        "hard_regressions": hard_regressions,
        "soft_fails": soft_fails,
        "precision_by_class": precision_by_class,
        "vision_calls_total": total_vision,
        "vision_calls_on_cheap_stages": vision_waste,
        "elapsed_s": round(elapsed, 4),
        "max_runtime_s": MAX_RUNTIME_S,
        "role": "shadow",
        "alters_production": False,
        "l1_coverage_map": {
            "L1_useful_work_heartbeat": ["ADV-010"],
            "gate_pre_publish.IA_VERTICAL": ["ADV-009"],
            "gate_pre_publish.license": ["ADV-006", "ADV-020"],
            "cron_command_linter": ["ADV-010"],
            "media_backlog_circuit_breaker": ["ADV-012"],
            "schema_preflight": ["ADV-011", "ADV-016"],
            "funil_C0_C5": ["ADV-001", "ADV-005", "ADV-006", "ADV-007", "ADV-008", "ADV-020"],
            "R4_proveniencia": ["ADV-016", "ADV-017", "ADV-018", "ADV-019"],
        },
        "cases": results,
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if elapsed >= MAX_RUNTIME_S:
        print(f"RUNTIME_ERR: {elapsed:.3f}s >= {MAX_RUNTIME_S}s", file=sys.stderr)
        return 3
    if hard_regressions:
        for h in hard_regressions:
            print(f"HARD_REGRESSION: {h}", file=sys.stderr)
        return 1
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Replay adversário V4 mídia (offline)")
    p.add_argument(
        "--cases",
        type=Path,
        default=DEFAULT_CASES,
        help="JSONL de casos adversariais",
    )
    p.add_argument(
        "--decisions",
        type=Path,
        default=None,
        help="JSONL opcional de decisões candidatas {case_id, decision, reason_code}",
    )
    p.add_argument(
        "--self-test-fail",
        action="store_true",
        help="Injeta regressão em hard cases (prova que exit≠0 funciona)",
    )
    args = p.parse_args(argv)
    if not args.cases.exists():
        print(f"cases não encontrado: {args.cases}", file=sys.stderr)
        return 2
    return run(args.cases, args.decisions, args.self_test_fail)


if __name__ == "__main__":
    sys.exit(main())
