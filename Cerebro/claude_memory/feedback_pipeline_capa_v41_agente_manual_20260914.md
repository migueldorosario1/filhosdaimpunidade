---
name: feedback-pipeline-capa-v41-agente-manual-20260914
description: "Pipeline de capa V4.1 é agente manual (CL+claudionor via wp-cli/SSH), não cron — silêncio do operador vira pane aparente sem pane real. Antes de abrir hipótese técnica, verificar se o passo é cron ou agente."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6424d2e0-280b-4dab-80c6-fffc0f353814
---

Investigação ZM (14/09/2026 ~14:00 BRT) confirmou: o passo «capa V4.1» (escolher/gerar imagem + `_thumbnail_id` + `_cafezinho_img_check` + agendamento) **nunca foi cronizado no Cafezinho**. Sempre foi trabalho de AGENTE via wp-cli/SSH — scripts `/root/cl2NN.sh` gerados pelo CL no servidor WP, uploads autor `user_id=0`, cadência ditada por ordem editorial.

**Contexto do caso:** Loop Laura silenciou 12/09 15:17 (state file `claude_laura.md`); claudionor terminou última leva RJ 13/09 13:15 (attachment 270563 último upload wp-cli autor 0). Fila V4.1 acumulou 11 drafts sem capa entre 12/09 22:57 (270419, primeiro sem capa) e 14/09 04:27 (270711). Publish continuou até 13/09 15:44 (270557 último) porque grade noturna já estava agendada + série RJ manual — depois furo 13h44min. CM na retomada 14/09 05:24 abriu fórum com 5 hipóteses técnicas erradas (H1 gerador sem crédito · H2 cron morto · H3 AL regressão · H4 claudionor parou · H5 App Password expirou); ZM investigou 2h e refutou 4 delas com prova primária, confirmou H4 «ampliada» = capa é trabalho de agente, sem cron por trás.

**Why:** Antes de assumir causa técnica pra falha visível, verificar **se o passo é cron ou agente**. Se é agente, silêncio dele = pane aparente sem pane real; a infra pode estar 100% sã. Errou o CM em 14/09 05:55 ao abrir o fórum com 5 hipóteses técnicas (cron, credencial, quota API, regressão silenciosa) — nenhuma se sustentou porque não havia máquina pra quebrar.

**How to apply:**
1. **Primeiro diagnóstico ao ver pipeline parado:** identificar o *operador* de cada passo (cron/serviço/wp-plugin vs agente humano/LLM via SSH/REST). Fontes objetivas: `_cafezinho_origem` das metas (`via=wp-cli user_id=0` = agente; `via=admin user_id=NNNN` = humano; `via=rest ua=python-requests` = script), últimos scripts em `/root/cl*.sh` (mtime), heartbeats state files agentes. Só depois abrir hipóteses técnicas.
2. **Fronteira de PUBLISH ≠ fronteira do BUG.** Futures agendados podem esconder o bug real por horas (nesta janela, 22h de gap entre bug 12/09 22:57 e último publish 13/09 15:44). Buscar o primeiro DRAFT com o defeito, não o último ÚLTIMO PUBLISH normal.
3. **AL heartbeat ininterrupto + CHECK explícito «aguardando decisão Miguel»** = operador consciente da fila esperando ordem, NÃO regressão silenciosa. Não abrir hipótese de bug na AL sem sinal duro (erro em log, meta corrompida, resposta inconsistente).
4. **Fluxo `cafezinho-<hash>` (attachments IA REST 2h/2h autor 5470)** é ativo pago mas historicamente órfão de `_thumbnail_id` — **não é canal das capas V4.1**. GL parado desde 28/08 é anterior a qualquer período funcional. Não confundir.
5. **Antes de investigar infra remota (nginx logs, cron.d, systemctl, quotas API):** verificar as metas de posts na fronteira via `wp post meta list`. Se `_cafezinho_origem.via` e `_publicado_por` mostram o operador, a resposta pode estar no chat/log dele, não na máquina.

Detalhes completos: fórum `~/cerebro-miguel/cerebro/Foruns/forum_auditoria_pipeline_capa_parado_20260914.md` seções 9 e 10.1; memória técnica ZM `~/cerebro-miguel/cerebro/Memorias/memoria_auditoria_pipeline_capa_20260914.md`; commit `11c5bd704`. Bloc ACK CM na ponte: `CM-20260914-006` (14:15 BRT).

Pendência estrutural em aberto (Miguel decide): (a) cronizar aplicação capa consumindo `cafezinho-*` com revisão visão automatizada; (b) formalizar rodízio CM/AGY/CL do posto capador com handoff auditável + alerta de fila (draft V4.1 >6h sem thumb → ping ponte) — **recomendação CM: (b)**; (c) status quo manual (contra: silenciou 22h sem alarme).

Ligação com regras relacionadas: [[feedback-checagem-dupla-antes-publish-v41-20260829]] (6 gates V4.1 obrigatórios) · [[feedback-alerta-ponte-cafezinho-telegram-autocura-v4-20260829]] (alerta ponte + autocura em furo grave) · [[feedback-cm-substitui-cl-se-parar-20260912]] (protocolo CM assume quando CL para) · [[feedback-autonomia-independencia-sistema-20260906]] (autonomia máxima).
