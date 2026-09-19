---
name: Sprint 3 Autocura (RLHF Reverso) LIVE 2026-04-20
description: Deploy do Sprint 3 da Proposta B em Cingapura. Callbacks v4rev/v4rep agora usam inverter_licao_por_post (carimba origem=miguel_rlhf_reverso) em vez de remover. Sprint 2 validado em produção com 2 lições gravadas via clique real do Miguel.
type: project
originSessionId: 2f45a438-d2f6-430e-b0c5-d2aae3c49947
---
**Deployado 2026-04-20 ~16:46 BRT em Cingapura (Tencent).** Autorizado por Miguel após validação do Sprint 2.

## Validação do Sprint 2 (pré-requisito)
Forçado via rota teste sintético:
- Draft 237249 usado como alvo (WP retorna HTTP 200 em no-op draft→draft → hook dispara sem publicar)
- Suspeito sintético injetado em `/root/agent_data/suspeitos_caetano.json`
- Alerta enviado via Bot API do Caetano (msg 341) pro chat 1894890759
- Miguel clicou `📥 Rebaixar` → hook Sprint 2 disparou corretamente
- **Bonus:** Miguel também clicou Rebaixar no suspeito REAL 237236 (Pezeshkian/Irã) — 2 lições gravadas no total:
  - `pid=237249`: "Nunca apresente projeções, estimativas ou cenários hipotéticos como fatos já ocorridos." (sintético, mantido no banco — útil)
  - `pid=237236`: "Evite colar citações cruas de resultados de busca; sempre reescreva a fonte em prosa ou use link HTML válido." (real, V4→V3 escalação por consenso parcial)
- Log servidor: `[CALLBACK rb] lição gravada pid=... origem=miguel_escalacao:`
- Arquivo `/root/agent_data/licoes_recentes_autocura.json` cresceu de 1→3 entradas
- `/root/agent_data/historico_absoluto_licoes.txt` recebeu tag `[miguel_escalacao]`

## Sprint 3 — o que entrou em produção
- `agente_correcao.py` linha 1016: `from autocura_licoes import inverter_licao_por_post` (era `remover_licao_por_post`)
- `agente_correcao.py` linha 1082: idem pro callback `v4rep`
- `inverter_licao_por_post` já existe em `/root/autocura_licoes.py` linha 192 desde Sprint 1 — carimba `origem=miguel_rlhf_reverso` e muda polaridade pra `tolerar` com prefixo "⚠️ ORDEM DO CEO"
- Backup servidor: `/root/agente_correcao.py.bak_pre_sprint3_20260420_1635` (62654 bytes)
- Novo: 63626 bytes

## Bonus: fix bug `_edit_clean RecursionError`
Durante o teste do Sprint 2 apareceu em TODOS callbacks: `_edit_clean falhou: RecursionError: maximum recursion depth exceeded`. Causa: linha 912 chamava `_edit_clean(query, text, **kwargs)` recursivamente em vez de `query.edit_message_text(text, **kwargs)`. Consequência: bot não conseguia atualizar a mensagem do Telegram pra refletir ação (cosmético, não bloqueia callback). Corrigido e deployado junto com Sprint 3. PID atual: 3976105 (startup 16:46:52 BRT).

## Restart do Caetano — truque que funcionou
Dois restarts hoje, um falhou (bot morreu sem subir), outro funcionou. Comando que subiu:
```bash
ssh ... "sudo bash -c '(setsid /root/venv/bin/python3 /root/agente_correcao.py >> /root/agent_data/agente_correcao_bot.log 2>&1 </dev/null &)'"
```
Isolar o comando em SSH dedicado (sem verificação de PID no mesmo SSH) evita o exit 255 que mata a sessão antes do setsid completar o detach.

## Pendências pós-deploy
- **Post 237236 (Pezeshkian) continua DRAFT** — Miguel clicou `mn:237236` (Manter) depois, mas o callback `mn` só marca suspeito como "aprovado" no JSON, **não republica o post no WP**. Decisão do Miguel: deixar rebaixado (lição útil) ou republicar via API (`status=publish`) e inverter lição via função `inverter_licao_por_post(237236)`.
- **Sprint 3 ainda não testado funcionalmente em produção** — só valida no primeiro alerta Tipo A/B do V4 que traga botões `↩️ Reverter` ou `↩️ Republicar`. Deploy está sã: função `inverter_licao_por_post` disponível no módulo, imports corretos, bot restart limpo.
- **Sprint 4** (Quórum de Consistência) segue local, não deployado. Aguarda Sprint 3 amadurecer ≥1 semana em produção antes de integrar gatilhos em `agente_autocura_v4.py`.
