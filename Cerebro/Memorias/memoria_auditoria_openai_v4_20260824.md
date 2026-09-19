# 🧠 Memória — Auditoria do gasto OpenAI / superprodução V4 (24/08/2026, ZCode/GLM-5.3 sess_c3b1edeb)

Complemento técnico do `Foruns/forum_auditoria_gasto_openai_v4_superproducao_20260824.md`.

## Fontes
- CSVs oficiais OpenAI (Downloads/Antigravity Google/Outros/Gastos IA/open ai/): `completions_usage_2026-08-20_2026-08-24.csv` (por hora/modelo/api_key) e `cost_2026-08-20_2026-08-24.csv` (por dia, org "O Cafezinho", US$ 39,03).
- NYC (ssh `nyc` = 198.199.121.136): `/root/v4_labs/` (`v41_ciclo.py` com `gpt-5.5` + tool `web_search`), crontab com `coletor.py`+`v4_vertical_intake.py`+`v4_vertical_draft_worker.py` por vertical: **geo `0,30 * * * *`** (48×/dia), nacional `20 */6` (reduzido 22/08, comentário `# V41_F1_20260823 … V4.1 sombra carrega volume`), economia/cultura `*/4h`, meio_ambiente diário 13:15. `gerenciador_tokens.py` menciona os modelos (candidato a teto de gasto).
- WP (ssh `cafezinho-wp`, path `/var/www/ocafezinho`): draft **>500** (saturou), **pending 361**, future 6, publish 17-24/08 ≥200; rascunhos novos 51 em 23/08 e 17 em 24/08 até ~09h.

## Números por modelo (20-24/08)
- gpt-5.5: 364 reqs · in 8,82M · out 814k — redação+FC luxo (pico 23/08: 106 reqs, 3,52M in, 284k out).
- gpt-4o-mini: 1.920 reqs · in 2,33M — coleta/intake 24/7 (838/dia em 20/08 → 131/dia em 24/08, já amenizando).
- gpt-4.1: 108 reqs; gpt-4o: 131 reqs.
- Padrão horário: 4o-mini roda toda hora inclusive de madrugada (assinatura do coletor no servidor).
- Chaves: `key_ucN30bx4MKqz7X2N` (dominante) e `key_9tHwtfm58iieOtAM` (1 req em 23/08 00h — identificar).

## Causa do pico de 23/08 (US$ 21,26)
Ronda V4 de 22/08 (memória rollout): "3 rascunhos v4.1 saudáveis → nacional worker reduzido; **V4.1 sombra carrega volume**" — a sombra gera rascunhos em paralelo sem o gate de publicação V4.1 liberar → produção ~2× publicação (51 rascunhos/dia vs ~28 publicados) → pagar gpt-5. pra estocar.

## Regras novas registradas
1. **Zero produção no Dell** (ordem Miguel 24/08): tudo em servidor/nuvem. Pendência: migrar crons `youtube_cafezinho.py` do Dell (8/14/20h, jornal 22:30/23h, forum11 14:30/15:30).
2. Sugestões pendentes de decisão: geo 30min→2h; sombra V4.1 pausada até gate liberar; teto diário no gerenciador_tokens.py; drenar 361 pending.
