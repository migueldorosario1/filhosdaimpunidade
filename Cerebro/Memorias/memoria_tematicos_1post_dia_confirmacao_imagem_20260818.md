# Memória — Temáticos V4: 1 post/dia + confirmação de imagem (18/08/2026)

**Sessão:** ZCode/DeepSeek — "TEMÁTICOS: 1 POST/DIA + CONFIRMAÇÃO DE IMAGEM" · 21:30–21:45 BRT

## Arquivos tocados (PC do Miguel, `agentes_tematicos/v4/`)

1. `nucleo_visao.py` — `_extrair_veredito(texto, esperado="APROVADA")` parametrizado; `_julgar_gemini`/`_julgar_qwen` ganharam `esperado`; **nova `confirmar_imagem(caminho, titulo, categoria, log)`** com `_CONFIRM_PROMPT` (binário CONFIRMADA/NAO_CONFIRMADA, critério estrito anti-stock-genérica) e **FAIL-CLOSE** (provedores fora = False + Telegram `confirmacao_img_down` throttle 1×/dia).
2. `publicador.py` — import de `confirmar_imagem`; **gate obrigatório** no `rodar()` logo após a legenda obrigatória: `confirmar_imagem(public/hero/<arq>, titulo, categoria)` → reprovada = remove arquivo, `hero_path=""`, `_adiar_por_falta_de_hero` e `continue` (antes do commit/push). Cobre acervo default (antes sem juiz).
3. Configs `agent_data/configs/*.json` — `posts_por_rodada` 2→1 (8 arquivos; `.bak_pre_1post_dia_20260818`).
4. Crontab local — removidas: `0 3 --all`, `0 */8 --site ceara`, `10 */8 --site riocarta`; mantida `0 13 --all`. Backup `/tmp/crontab.bak_pre_1post_dia_20260818`.
5. NYC — `CEARA_BATCH_SIZE=2→1` no cron `15 9 * * *` (pipeline `cicero_remote` paralelo do Ceará). Backup `/tmp/crontab.bak_pre_1post_dia_20260818` (NYC).

## Provas

- `py_compile` com o Python do cron (pyenv 3.10.13) OK nos 2 arquivos.
- **Teste unitário da confirmação (imagem real do RioCarta):** par positivo (hero de cultura × matéria de cultura) = **CONFIRMADA** (gemini); par negativo (mesma imagem × "trem Paris-Londres") = **NAO_CONFIRMADA**. VEREDITO: PASSOU.
- Rodadas reais com `--limite 1`: `riocarta` (fila vazia), `mundotrilhos` e `globalsouth` (posts adiados por hero indisponível/duplicada pós-padronização — fluxo sem erro; gate não chegou a atuar por falta de hero vencedora).

## Diagnóstico das imagens erradas do RioCarta

Últimos 12 posts com `hero_credit` quase 100% stock (Pexels/Pixabay) — foto genérica casada por tema amplo (ex.: CET-Rio interdita Rebouças = foto genérica de estrada). Furos: juiz fail-open + acervo default sem juiz + cascata stock vence fácil. O gate novo barrará daqui pra frente; posts antigos = faxina retroativa pendente de ordem.

## Gotchas / lições

- `agentes_tematicos/` é repo git mas `v4/*.py` estão UNTRACKED (nunca commitados) — não há rollback via git; rollback pré-edição = reversão cirúrgica (2 edits no publicador + 6 no nucleo_visao, todos descritos acima). Snapshots pós-edição em `.bak_pre_confirmacao_img_20260818`.
- Frontmatter dos sites usa `heroImage` (não `hero`) e o caminho público `/hero/*` corresponde a `public/hero/` no repo.
- Campo de "hero" no Banco auditado = `hero_path` interno do publicador.
- `aprovados_pendentes(3)` devolve no máx 3 — contar >3 exige ler o jsonl.

Tema Duplo: `Foruns/forum_tematicos_1post_dia_confirmacao_imagem_20260818.md` + esta memória.
