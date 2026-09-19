---
name: project-no-home-score-policy-v1-20260721
description: "Home vs no-home NÃO é decidido pelo Sentinela. Política vive em NYC no worker de coleta (Codex 2026-07-21 12:05 BRT). Limiares por score: Nacional≥13, Geopol≥12, Ciência≥10, Estatal 95/90. Previsão do tempo (5102) sempre no-home. Falha fechada. NUNCA reclassificar retroativo."
metadata:
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-21 13:45 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra vigente (SUPERA a proporção de 21/07 08:25)

**Home vs no-home é decidido no momento da CRIAÇÃO do post pelo worker de coleta em NYC**, baseado no score da própria coleta. Sentinela e qualquer agente publicador NÃO reclassificam.

### Limiares

| Agente | Campo score | Limiar para capa (home) | Caso contrário |
|---|---|---:|---|
| V4 Nacional | `candidates.score` | ≥ 13 | no-home (cat 20699) |
| V4 Geopolítica | `candidates.score` | ≥ 12 | no-home |
| V4 Ciência/Tec/IA | `candidates.score` | ≥ 10 | no-home |
| Repetidor Estatal | `estatal_news.score_ranking` E `estatal_news.nota_llm` | ≥ 95 E ≥ 90 | no-home |
| Previsão do Tempo (cat 5102) | — | **SEMPRE no-home** obrigatório | — |
| Nota ausente / agente não configurado | — | **falha fechada → no-home** | — |

Proporção histórica que caiu na faixa de capa (amostra): Nacional 8/38, Geopol 12/55, Ciência 5/41, Estatal 33/148. Aproxima o quintil superior, Ciência um pouco mais seletiva. Estatal 95/90 ≈ 22% — Miguel considerou adequado, **não estreitar sem nova decisão dele**.

**Why:** Codex 2026-07-21 12:05 BRT executou determinação direta de Miguel para substituir a alternância mecânica anterior (proporção fixa por editoria) pela decisão baseada em qualidade real de coleta. A alternância aleatória colocava lixo na capa e enterrava boas pautas em no-home.

**How to apply:**

### 1. No Sentinela (Claude Code):
- **NÃO adicionar nem remover cat 20699** em nenhum ponto do fluxo
- **NÃO reclassificar retroativo** (contrato: `retroactive_reclassification=false`, `preserve_existing_posts_and_drafts=true`)
- Herdar categorias como vieram do worker
- Reportar HOME/NO-HOME de cada publish no `resumo_executivo` do ciclo (novo requisito)
- Se algum draft vier sem cat 20699 mas com score inconsistente, ainda assim publicar do jeito que está — decisão é do worker

### 2. Escopo temporal:
- Regra vale exclusivamente para posts **NOVOS**, no momento da criação
- Drafts e publicados antigos permanecem como estão (mesmo se score/categorização atual diferiria)
- Removedor `/root/remover_no_home.py` (cron `0 */2 * * *`) tira 20699 depois de 4h — efetivo 4-6h — mantém função histórica, **não recalcula nota**

### 3. Deploy NYC (Codex):
- Contrato: `Projeto Cafezinho Agentes/root/v4_labs/contratos/v4_no_home_score_policy_v1.json`
- Módulo comum: `Projeto Cafezinho Agentes/root/v4_labs/codigo/no_home_score_policy.py`
- NYC: `/root/no_home_score_policy.py` + `/root/agent_data/no_home_score_policy.json`
- Integrados: `/root/v4_vertical_draft_worker.py` (Nacional/Geopol/Ciência) + `/root/agente_repetidor_estatal.py`
- Cada decisão grava/expõe score, limite, resultado, motivo
- Backups: `.backup_pre_score_nohome_20260721_1202`

### 4. Documentação canônica:
- Fórum: `Cerebro/Foruns/forum_no_home_por_nota_coleta_20260721.md`
- Aceite Claude Code: inbox_trindade/codex.md entrada 2026-07-21 13:45

## Supera memória anterior

**[[feedback-diretrizes-editoriais-21jul]]** — a parte "Proporção home/no-home (Miguel decide): Ciência 80% home, Geopol 60% home, Nacional 0% home" está **superada por esta memória**. A memória antiga permanece no MEMORY.md com nota histórica pois contém 4 outras diretrizes (R1 rate limit, R2 esporte siglas, R3 nome próprio desconhecido, R4 partido MAIÚSCULO) que continuam vigentes.

## Exceções pontuais que aconteceram antes da política entrar

- 2026-07-21 13:20-13:35 BRT: recategorizei retroativamente 5 drafts pendentes (262402, 262403, 262407, 262408, 262414) sob autorização explícita e mutável do Miguel ("bota tudo no home" → "é para publicar tudo como no-home desses aí"). Ação foi antes da carta do Codex chegar às 13:40. Não repito — respeitando `retroactive_reclassification=false` daqui pra frente.

## Relacionadas

- [[feedback-diretrizes-editoriais-21jul]] — parte de proporção está superada; R1/R2/R3/R4 continuam
- [[feedback-sentinela-nunca-publicar-rascunhos-antigos]] — cap 2h continua valendo
- [[feedback-sujeira-metadata-pipeline-v4]] — auditor antivazamento continua
- Contrato NYC: `Projeto Cafezinho Agentes/root/v4_labs/contratos/v4_no_home_score_policy_v1.json`
- Fórum canônico Codex: `Cerebro/Foruns/forum_no_home_por_nota_coleta_20260721.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-21 13:45 BRT.
