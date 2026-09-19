---
name: Sprint 2 da Proposta B (Loop Aprendizado Pós-Escalonamento) LIVE — 2026-04-20
description: Deploy autocura_licoes.py + agente_correcao.py concluído em Cingapura. Hook rb:<post_id> no Caetano grava lição origem=miguel_escalacao. Sprint 3+4 congelados aguardando validação humana.
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Deployado 2026-04-20 09:40 BRT em Cingapura.** Consenso fórum Seção 10.

## O que entrou em produção
- `autocura_licoes.condensar_motivo_para_principio(motivo, regra_violada)` — condensa motivo verbose do V3 em princípio de 1 linha via LLM.
- `adicionar_licao(origem=...)` com retrocompat (default `"V4_auto"`); origens válidas: `V3_auto`, `V4_auto`, `miguel_escalacao`, `miguel_rlhf_reverso`.
- Hook no callback `rb:<post_id>` do Caetano bot (agente_correcao.py linhas ~1102-1135): após HTTP 200 do rebaixamento, dispara `pegar_suspeito` → `condensar_motivo_para_principio` → `adicionar_licao(origem="miguel_escalacao")`. Try/except protege UX.
- Histórico absoluto recebe `[origem]` na linha TXT.

## Backups servidor
- `/root/autocura_licoes.py.bak_pre_sprint2_20260420_0937` (19.365 bytes)
- `/root/agente_correcao.py.bak_pre_sprint2_20260420_0937` (61.320 bytes)

## Caetano bot
Restart via `setsid` (não `nohup &` — esse não pega dentro de `sudo bash -c`). PID novo ativo desde 09:39:27 BRT com mensagem `[CAETANO] Caetano rodando | @caetanoechicobot`.

## Quórum de Consistência (Sprint 4, parâmetros validados)
Quando Sprint 4 for codado:
- `QUARENTENA_JANELA_DIAS = 7`
- Arquivo `/root/agent_data/licoes_quarentena_autocura.json`
- Schema: `{principio_hash: {primeira_vista, ultima_vista, count, origens[], post_ids[]}}`
- Match Jaccard ≥ 0.7 (reusa engine de dedup existente)
- Gatilho promoção: `count ≥ 2 E todos dentro janela` (reset fora)
- Silenciosa até promover; tag `[quorum_2x]` no histórico absoluto quando vira oficial

## Validação pendente (Sprint 2)
Aguardar Miguel clicar `📥 Rebaixar` em algum alerta Tipo A. Procurar em:
- `/root/agent_data/agente_correcao_bot.log` → `[CALLBACK rb] lição gravada pid=... origem=miguel_escalacao: ...`
- `/root/agent_data/licoes_recentes_autocura.json` → nova entrada origem miguel_escalacao
- `/root/agent_data/historico_absoluto_licoes.txt` → nova linha `[miguel_escalacao]`

## Próximos sprints (ordem 2 → 3 → 4 congelada pelo fórum)
- **Sprint 3** ✅ codado local 20/04 10:10 BRT — callbacks `v4rev` + `v4rep` no `agente_correcao.py` trocam `remover_licao_por_post` por `inverter_licao_por_post` (essa função já existia no Sprint 1 e já carimba `miguel_rlhf_reverso`). Log `[CALLBACK v4rev/rep] lições invertidas`. Não deployado.
- **Sprint 4** ✅ engine abstrata codada local 20/04 10:30 BRT — módulo novo `autocura_quarentena.py` (~280 linhas) com `registrar_em_quarentena`, `promover_se_quorum`, `decair_quarentena`, `registrar_e_promover`, `estado_atual`. Hash do princípio é SHA-256[:16] NORMALIZADO. Tag histórica `[quorum_2x]` quando promove. Mudança mínima em `autocura_licoes.adicionar_licao` (parâmetro opcional `evento_historico`, retrocompat). **10/10 testes unitários** em `/tmp/test_autocura_quarentena.py`. Gatilhos (integração em `agente_autocura_v4.py`) NÃO feitos — aguardam validação Sprint 2 antes.
