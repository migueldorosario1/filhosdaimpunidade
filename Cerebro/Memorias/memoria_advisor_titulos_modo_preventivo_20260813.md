# Memória técnica — Modo Advisor (preventivo) do Auditor de Títulos GPT

**Data:** 2026-08-13 22:45 BRT · **Autor:** ZCode (GLM-5.2) · **Sprint:** adicionar modo preventivo ao auditor de títulos
**Fórum gêmeo:** `Foruns/forum_advisor_titulos_modo_preventivo_20260813.md`

## Contexto
Cartinha do Claude (`Foruns/inbox_trindade/zcode.md` tag `[CLAUDE-PEDIDO-AUDITOR-TITULOS-GPT-MODO-PREVENTIVO-20260813-2210-BRT]`) pediu modo `advisor` no `agente_auditor_titulos_gpt.py` (query `draft/pending author 5786 últimos 4h`, 7 regras + fórmula por vertical, output JSONL). Errata 22:15 reframing: **bug conceitual, não feature** (Miguel: "essa era pra ser a ideia").

## Arquivos tocados
- **Produção (NYC `198.199.121.136`, alias `nyc`):** `/root/agente_auditor_titulos_gpt.py` (1048→1363 linhas).
- **Espelho local:** `/home/migueldorosario/Downloads/Antigravity Google/.codex_work/agente_auditor_titulos_gpt.py` (hardlink em `.vercel/output/static/.codex_work/`).
- Pré-mudança eram **idênticos** (sha `49aebe2bf03293da58e7f3bf76a80cf0727c1f6c1a0563025b4e476d3e1f20ee`).
- Pós-mudança ambos sha `c19ae30542126a6f84fec7d3f4db98668070224cb0ec074dad93d776259822f4` (idênticos).

## Backups
- Script NYC: `/root/agente_auditor_titulos_gpt.py.bak_pre_advisor_20260813_2240` (sha `49aebe2b…`).
- Crontab NYC: `/tmp/crontab_backup_20260813_2241`.

## Implementação (8 edits aditivos)
1. `from datetime import date, datetime` → `+ timedelta`.
2. Constantes: `ADVISOR_SCHEMA`, `ADVISOR_PENDING_PATH`, `ADVISOR_HISTORY_PATH`.
3. `DEFAULT_CONFIG`: `modelo_advisor_mini` (gpt-4o-mini, $0.15/$0.60 per Mtok), `advisor_author_id=5786`, `advisor_janela_horas=4`, threshold `hardstop_advisor_dia_usd=2.0`.
4. `wp_get_advisor_posts()` + `VERTICAL_POR_CATEGORIA` (10 verticais) + `vertical_do_post()`.
5. `_advisor_system_prompt()` (7 regras + fórmula), `_advisor_payload()`, `mock_advisor()` (heurística offline), `_chamar_openai_mini()` (JSON mode).
6. `append_jsonl_advisor_history()` + `run_advisor()` (orquestração, snapshot atômico + histórico).
7. `parse_args`: `choices=["poll","advisor"]` + `--author` + `--horas`.
8. `main()`: ramificação `if args.modo == "advisor"` antes de `run()` (poll intocado).

## Decisões técnicas chave
- **Filtro author client-side:** `author=<id>` na REST deste WP = 404 (anti-enumeração). Query = `status=draft,pending`+`after=<4h>`+`per_page=100` server-side; filtro `author==5786` em Python.
- **LLM:** gpt-4o-mini (não a cascata websearch do poll — advisor é análise de forma, não fact-check). `response_format: json_object`, `temperature=0`, `max_tokens=300`.
- **chars_mb = `len(titulo)`** (Python 3 conta code points = mb_strlen do PHP para PT-BR).
- **Snapshot atômico** (tmp+rename) do `advisor_pending.jsonl` a cada rodada + **append** no `advisor_pending_history.jsonl` (flock).
- **Estado isolado:** contadores `advisor_*` (daily_key) separados do `poll`; não poluem `custo_dia_usd`/`correcoes`.

## Comandos executados (provas)
```bash
# deploy
scp ".codex_work/agente_auditor_titulos_gpt.py" nyc:/root/
ssh nyc 'cp /root/agente_auditor_titulos_gpt.py /root/agente_auditor_titulos_gpt.py.bak_pre_advisor_20260813_2240'
ssh nyc 'cd /root && /root/venv/bin/python3 -m py_compile agente_auditor_titulos_gpt.py'  # PYC_OK_NYC
# validação query REST (antes de codificar)
ssh nyc 'python3 -c "..."'  # 8 posts draft/pending author 5786 últimos 4h; author= retorna 404
# teste mock (zero custo)
ssh nyc '/root/venv/bin/python3 /root/agente_auditor_titulos_gpt.py --modo advisor --mock-gpt'
#   → {"posts":8,"veredito_ok":6,"veredito_ajustar":2,"erros":0}
# rodada real gpt-4o-mini
ssh nyc '/root/venv/bin/python3 /root/agente_auditor_titulos_gpt.py --modo advisor'
#   → {"posts":8,"veredito_ok":7,"veredito_ajustar":1,"erros":0}  custo US$ 0.000833
# cron
(crontab -l; echo '*/30 * * * * ... flock -n /tmp/auditor_advisor.lock ... --modo advisor >> advisor.log 2>&1') | crontab -
```

## Cron adicionado (NYC crontab)
```
# === ADVISOR DE TÍTULOS (modo preventivo, draft/pending autor 5786 janela 4h) — ZCode 13/08/2026 ===
*/30 * * * * cd /root && /usr/bin/flock -n /tmp/auditor_advisor.lock /root/venv/bin/python3 /root/agente_auditor_titulos_gpt.py --modo advisor >> /root/agent_data/auditor_titulos_gpt/advisor.log 2>&1
```
Intactos: `poll` (`*/10`, flock `/tmp/auditor_titulos_gpt.lock`) e `relatorio-diario` (`:58`).

## Custo medido
- **US$ 0.000833/rodada** (8 posts, gpt-4o-mini). ×48 rodadas/dia (`*/30`) ≈ **US$ 0.04/dia**. Hardstop defensivo $2/dia (jamais chega perto).

## Achados / lições
- **LLM > heurística:** o gpt-4o-mini ignorou o falso-positivo "chineses e soldados" (enumeração legítima vs concatenação de ideias) que o mock pegava. Vale o custo ínfimo.
- **Anti-enumeração de autores:** confirmado operando no REST do controle.ocafezinho.com. Qualquer agente que precise filtrar por author via REST → fazer client-side.
- **Bug conceitual corrigido na raiz:** o auditor agora age **antes** do publish (pending), não depois (publish). É o framing que o Miguel endossou.

## Pendências
- Claude integrar leitura do `advisor_pending.jsonl` na Vigília V6.
- Opcional: cache por `(post_id, hash_titulo)` se volume crescer.
- Miguel decide harmonização regra-mãe × 7 regras (pendente desde 12/08).

## Estado final
✅ Implementado, testado (mock + real), deployado, cron ativo, documentado. Snapshot vivo em `/root/agent_data/auditor_titulos_gpt/advisor_pending.jsonl` atualizado a cada 30 min.
