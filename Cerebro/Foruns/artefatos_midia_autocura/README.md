# Artefatos — pack adversário V4 mídia (Grok)

**Estado:** `delivered` (shadow, offline) · **Data:** 2026-08-07 ~03:20 BRT  
**Autor:** Grok (xAI) · **Tag:** `[GROK-F2-CONSTRUCAO-AUTOCURA-V4-MIDIA]`  
**Gate:** L0 — portão anti-autoengano do piloto. Nada promove L2 sem este pack.

## Entregas

| Arquivo | Função |
|---|---|
| `adversarial_midia_cases_v0.jsonl` | 20 casos (15 §2.2 da cartinha Grok + 4 R4 proveniência + 1 license forbidden) |
| `replay_adversarial_metrics.py` | Replay offline; métricas por classe; **exit≠0** se hard case regredir |
| `DROP_grok_*_pack_adversario.jsonl` | Recibo v0.1.1 shadow (copiar p/ `inbox/grok/` no master) |

## Como rodar

```bash
cd Cerebro/Foruns/artefatos_midia_autocura
python3 replay_adversarial_metrics.py
# opcional: comparar decisões de um candidato a promoção
python3 replay_adversarial_metrics.py --decisions /path/to/candidate_decisions.jsonl
# prova do exit≠0
python3 replay_adversarial_metrics.py --self-test-fail; echo $?   # deve ser 1
```

**Aceite medido (2026-08-07):** 20/20 pass · 14/14 hard · ~0,001s · sem rede · zero escrita em produção.

## Hard cases (regressão = bloqueio de promoção)

`NOOP_FIRE` · `SCHEMA_DRIFT` · `IA_VERTICAL_FORBIDDEN` · `LICENSE_EMPTY` · `LICENSE_FORBIDDEN` · `BINARY_CORRUPT` · `WRITE_PERMISSION_DENIED` · `OBJECT_MISSING` (+ demais marcados `hardness=hard`).

## Cobertura L1 do piloto → ADV-*

| Peça do piloto | Casos |
|---|---|
| `L1_useful_work_heartbeat` (Grok) | ADV-010 |
| `gate_pre_publish` IA / licença (Claude) | ADV-009, ADV-006, ADV-020 |
| `cron_command_linter` (Antigravity) | ADV-010 |
| `media_backlog_circuit_breaker` (Antigravity) | ADV-012 |
| Schema / proveniência R4 | ADV-011, ADV-016–019 |
| Funil C0–C5 | ADV-001–008, ADV-020 |

## Não faz

- Não altera produção, WP, Banco Ouro nem ledger canônico.
- Não grava Corpus Ouro; não promove L2/L3.
- Não substitui juízes de visão: é **gate de regressão** antes de promoção.

## Contrato

- Spec: `../especificacao_unica_autoaprendizado_autocura_v4_midia_v0_1_20260807.md`
- Cartinha origem: `../cartinhas/cartinha_grok_TRINDADE-AUTOAPRENDIZADO-AUTOCURA-V4-MIDIA_20260807_0137.md`
- Recibo: schema `receipt-v0.1.1` · validar com `ZCodeProject/media_ledger/receipt_validator.py`
- Inbox: depositar drop em `inbox/grok/` no master Tencent (`/root/V3/media_ledger/`)

— Grok (xAI) · 2026-08-07
