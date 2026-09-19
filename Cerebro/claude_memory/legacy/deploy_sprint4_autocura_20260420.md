---
name: Sprint 4 Autocura (Quórum) módulo deployado 2026-04-20
description: autocura_quarentena.py copiado pra /root/ em Cingapura. Gatilhos em agente_autocura_v4.py NÃO integrados ainda — aguarda Sprint 3 amadurecer ≥1 semana. Smoke test 2/2 OK no servidor.
type: project
originSessionId: 50202c88-5137-43d9-ac6f-5fb1c3ffc1d6
---
**Deployado 2026-04-20 ~19:26 BRT em Cingapura.** Só o módulo; integração adiada conforme parecer do Antigravity.

## O que entrou
- `/root/autocura_quarentena.py` (11760 bytes, root:root, 644)
- Dependências já presentes: `util_safe_json.py`, `autocura_licoes.py`

## Smoke test no servidor (passou)
`QUARENTENA_PATH=/tmp/test_quarentena.json /root/venv/bin/python3 -c "..."`
- R1 (1ª ocorrência): `count=1, pronta_para_promover=False` ✓
- R2 (2ª ocorrência mesmo princípio, origem diferente): `count=2, pronta_para_promover=True` ✓
- `estado_atual()` retorna 1 entry (hash único pela normalização) ✓

## O que NÃO entrou (decisão deliberada)
- Gatilhos em `agente_autocura_v4.py` (quando V3/V4 rebaixa autonomamente) → chamariam `registrar_e_promover(principio, origem="V3_auto"|"V4_auto", post_id, motivo)`.
- Motivo: Antigravity recomendou ≥1 semana de Sprint 3 em produção antes de integrar. Sprint 3 deployado às 16:46 BRT hoje (2026-04-20) — reavaliar ~2026-04-27.

## Parâmetros fixos (Seção 10 do FORUM_AUTOCURA.md)
- `QUARENTENA_JANELA_DIAS=7`
- `JACCARD_LIMITE_PROMOCAO=0.7`
- `QUORUM_MIN=2`
- Hash: SHA-256[:16] sobre princípio NORMALIZADO (case/acento/pontuação-insensível)

## Como ativar depois
1. Em `agente_autocura_v4.py`, onde há rebaixamento autônomo, trocar `adicionar_licao(..., origem="V3_auto")` por:
   ```python
   from autocura_quarentena import registrar_e_promover
   registrar_e_promover(principio, origem="V3_auto", post_id=pid, motivo_original=motivo)
   ```
2. Opcional: adicionar cron diário de `decair_quarentena()` pra limpar entries > 7 dias.
3. Lições humanas (`miguel_escalacao` / `miguel_rlhf_reverso`) continuam entrando direto via `adicionar_licao` — quórum=1.
