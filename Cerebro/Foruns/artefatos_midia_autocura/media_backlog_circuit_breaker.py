#!/usr/bin/env python3
"""Circuit breaker shadow/read-only para backlog de mídia V4.

Consome amostras JSONL, calcula o estado por vertical e declara o freio que
SERIA aplicado. Nesta fase nunca pausa workers nem cria pautas. Toda abertura
inclui causa_suspeita explícita e ticket L0.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path


AUTHORIZATION_REF = "chat_miguel_20260807_TRINDADE-F2-CONSTRUCAO-AUTOCURA-V4-MIDIA"


def _parse_ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_samples(path: str) -> list[dict]:
    samples: list[dict] = []
    with open(path, encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                sample = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"linha {line_number}: JSON inválido: {exc}") from exc
            for key in ("ts", "vertical"):
                if not sample.get(key):
                    raise ValueError(f"linha {line_number}: campo obrigatório ausente: {key}")
            if "pending_count" not in sample and "image_pending" not in sample:
                raise ValueError(f"linha {line_number}: pending_count ou image_pending obrigatório")
            sample["pending_count"] = int(sample.get("pending_count", sample.get("image_pending")))
            _parse_ts(sample["ts"])
            samples.append(sample)
    if not samples:
        raise ValueError("arquivo sem amostras")
    return samples


def evaluate(samples: list[dict], *, consecutive_growth: int = 3, age_p95_limit: float = 180.0) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for sample in samples:
        grouped[sample["vertical"]].append(sample)

    results: list[dict] = []
    for vertical, rows in sorted(grouped.items()):
        rows.sort(key=lambda item: _parse_ts(item["ts"]))
        deltas = [rows[index]["pending_count"] - rows[index - 1]["pending_count"]
                  for index in range(1, len(rows))]
        growth_streak = 0
        for delta in reversed(deltas):
            if delta > 0:
                growth_streak += 1
            else:
                break

        last = rows[-1]
        hard_invariant = bool(last.get("hard_invariant_broken", False))
        age_p95 = float(last.get("age_p95_minutes", 0) or 0)
        triggers: list[str] = []
        if growth_streak >= consecutive_growth:
            triggers.append("BACKLOG_NET_GROWTH")
        if age_p95 > age_p95_limit:
            triggers.append("AGE_P95_EXCEEDED")
        if hard_invariant:
            triggers.append("HARD_INVARIANT_BROKEN")

        if triggers:
            state = "CIRCUIT_OPEN"
        elif growth_streak > 0 or age_p95 > age_p95_limit * 0.75:
            state = "DEGRADED"
        else:
            state = "HEALTHY"

        cause = last.get("causa_suspeita") or "unknown"
        ticket = None
        if state == "CIRCUIT_OPEN":
            safe_vertical = "".join(c if c.isalnum() else "_" for c in vertical).strip("_")
            ticket = {
                "ticket_id": f"L0_MEDIA_{safe_vertical}_{_parse_ts(last['ts']).strftime('%Y%m%d_%H%M%S')}",
                "level": "L0",
                "status": "open",
                "vertical": vertical,
                "causa_suspeita": cause,
                "triggers": triggers,
                "required_action": "diagnosticar causa; shadow não autoriza pausa real",
            }
        results.append({
            "vertical": vertical,
            "state": state,
            "enforced": False,
            "action": "would_pause_new_drafts" if state == "CIRCUIT_OPEN" else "observe",
            "causa_suspeita": cause if state == "CIRCUIT_OPEN" else last.get("causa_suspeita"),
            "ticket": ticket,
            "evidence": {
                "samples": len(rows),
                "pending_counts": [row["pending_count"] for row in rows],
                "net_deltas": deltas,
                "positive_growth_streak": growth_streak,
                "age_p95_minutes": age_p95,
                "age_p95_limit_minutes": age_p95_limit,
                "hard_invariant_broken": hard_invariant,
                "triggers": triggers,
                "last_ts": last["ts"],
            },
        })
    return results


def make_receipts(results: list[dict], source: str, timestamp: datetime | None = None) -> list[dict]:
    timestamp = timestamp or datetime.now().astimezone()
    stamp = timestamp.strftime("%Y%m%d_%H%M%S")
    receipts: list[dict] = []
    for sequence, result in enumerate(results, 1):
        opened = result["state"] == "CIRCUIT_OPEN"
        if opened and (not result["causa_suspeita"] or not result["ticket"]):
            raise ValueError("CIRCUIT_OPEN exige causa_suspeita e ticket L0")
        receipts.append({
            "sinal": f"backlog {result['vertical']}: {result['state']} (shadow)",
            "causa_raiz": "unknown" if opened else "none_observed",
            "correcao": "none — read-only; would_pause_new_drafts" if opened else "none — observe",
            "prova": {
                "before": {"source": source},
                "after": result,
                "checks": ["estado calculado deterministicamente", "enforced=false",
                           "ticket L0 presente" if opened else "nenhum freio proposto"],
                "artifacts": ["media_backlog_circuit_breaker.py"],
            },
            "rollback": "n/a — read-only",
            "regra_derivada": "crescimento líquido 3 ciclos, age/p95 excedido ou hard invariant → propor freio + ticket L0",
            "alcance": "vertical",
            "risco_promocao": "L0",
            "policy_version": "midia-v0.1",
            "origem": "machine_autocure",
            "system_state": {"seletor": "n/a", "cotas": "n/a", "fontes_ativas": [source],
                             "prompt_juiz": "n/a", "schema_versions": {"receipt": "v0.1.1"}},
            "role": "shadow",
            "gold_source": None,
            "reason_code": "CIRCUIT_BREAKER_OPEN" if opened else None,
            "metadata": {
                "schema_version": "receipt-v0.1.1",
                "receipt_id": f"rcpt_{stamp}_antigravity_backlog_{sequence:02d}",
                "ref": None,
                "vertice": "antigravity",
                "ts": timestamp.isoformat(timespec="seconds"),
                "generalizabilidade": "medium",
                "causa_suspeita": result["causa_suspeita"] if opened else None,
                "actor_roles": {"proposer": ["antigravity"], "technical_reviewer": [],
                                "authorizer": ["miguel"], "executor": ["codex"], "verifier": []},
                "decision_state": "executed",
                "authorization_ref": AUTHORIZATION_REF,
                "delivery_state": "delivered",
                "model_identity": {"model": "codex-gpt-5", "environment": "codex",
                                   "session_ref": "antigravity-f2-20260807"},
            },
        })
    return receipts


def write_jsonl_atomic(path: str, receipts: list[dict]) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            for receipt in receipts:
                handle.write(json.dumps(receipt, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples", help="JSONL: ts, vertical, pending_count/image_pending e sinais opcionais")
    parser.add_argument("--growth-cycles", type=int, default=3)
    parser.add_argument("--age-p95-limit", type=float, default=180.0)
    parser.add_argument("--receipt-out", help="drop-file JSONL v0.1.1 (escrita atômica)")
    args = parser.parse_args(argv)
    if args.growth_cycles < 1 or args.age_p95_limit <= 0:
        parser.error("limites devem ser positivos")
    try:
        samples = load_samples(args.samples)
        results = evaluate(samples, consecutive_growth=args.growth_cycles,
                           age_p95_limit=args.age_p95_limit)
    except (OSError, ValueError) as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 1
    if args.receipt_out:
        write_jsonl_atomic(args.receipt_out, make_receipts(results, args.samples))
    print(json.dumps({"mode": "shadow-read-only", "results": results}, ensure_ascii=False,
                     indent=2, sort_keys=True))
    return 2 if any(result["state"] == "CIRCUIT_OPEN" for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
