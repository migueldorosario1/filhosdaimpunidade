---
name: feedback-seo-pruning-uso-restrito
description: "SEO Pruning (marcar URLs com HTTP 410 Gone permanente pra Google) requer AUTORIZAÇÃO EXPLÍCITA do Miguel para cada uso. Sistema NYC do Codex operou em 21/07 sob autorização pontual — era pra URLs PROBLEMÁTICAS causando degradação de autoridade, não simplesmente URLs de baixa audiência. Sentinela e qualquer agente NÃO ativa pruning sem novo pedido do Miguel."
metadata:
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-23 09:55 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra inviolável

**SEO Pruning (marcar URLs com HTTP `410 Gone` permanente pra desindexar do Google) é ação DELICADA e IRREVERSÍVEL. Requer AUTORIZAÇÃO EXPLÍCITA do Miguel para CADA batch/aplicação.**

Nunca ativar/aplicar/estender SEO pruning sem novo pedido dele. Nem "porque tem URL parecida", nem "porque bug de dedup gerou lixo", nem "porque me pareceu razoável".

## Contexto histórico

Codex operou pruning em 2026-07-01 → 2026-07-21 03:07 BRT sob autorização pontual do Miguel para atacar problema específico: **URLs problemáticas que estavam causando degradação de autoridade do domínio no Google**. Resultado: 1.318 URLs marcadas 410 Gone → tráfego orgânico Cafezinho +164% MA7 nas semanas seguintes.

**MAS o critério de seleção foi específico e humano** — Miguel + Codex identificaram URLs problemáticas ativas (não simplesmente "baixa audiência"). Confundir "baixa audiência" com "problemática" é erro de framing e leva a decisões erradas.

**Diretriz clara do Miguel (2026-07-23 09:50 BRT):**
> "Aquilo foi um uso específico autorizado por mim, que não era propriamente URL sem audiência orgânica, eram URLs problemáticas, que a gente identificou que poderiam estar causando degradação de autoridade do Google. Mas não é para ficar usando esse SEO pruning sem autorização não, tá?"

## How to apply

### 1. Sentinela e outros agentes autônomos
NUNCA acionar `seo_pruning_state.json` ou `remover_no_home.py` como ferramenta editorial. Essas rotinas continuam nos crons legítimos do Codex (`0 */2 * * *` para remover no-home; pruning batch já concluído).

### 2. Ações permitidas por agente autônomo em posts velhos:
- ✅ `DELETE /wp-json/wp/v2/posts/{id}` → move pra `trash` clássico WP (recuperável 30d, seguro, autorizado quando Miguel liberar drafts velhos)
- ✅ `POST /wp-json/wp/v2/posts/{id}` com mudança de categoria pra `NO_HOME` (20699) — não afeta SEO, só visual do site
- ❌ Marcar URL com `410 Gone` — NÃO fazer, é território do Codex sob autorização Miguel

### 3. Ao encontrar URL retornando 410 Gone
- Reconhecer como resultado de pruning legítimo anterior
- NÃO tentar "reverter" (é intencional)
- NÃO estender pra URLs semelhantes ("já que essa foi, essa outra também deve ser") — errado
- Registrar como observação apenas, não como ação

### 4. Se surgir necessidade legítima de novo pruning
- Levantar hipótese fundamentada (com dados GSC, GA4, evidência de degradação)
- Escrever proposta em `Cerebro/Foruns/` com URLs candidatas + critério
- Aguardar autorização explícita do Miguel
- Só então executar (ou delegar ao Codex)

## Erro que precisa ser evitado

**Imprecisão de framing** — chamar SEO pruning de "poda genérica de URLs sem audiência". Errado. Descrição correta: **poda cirúrgica de URLs problemáticas identificadas como causadoras de degradação de autoridade do domínio**.

Se num relatório futuro eu descrever pruning como "URLs sem audiência", significa que perdi o framing correto — Miguel deve me corrigir de novo.

## Relacionadas

- Estado do pruning NYC: `/root/agent_data/seo_pruning_state.json` (1.318 URLs processadas, status `active` mas sem candidatos pendentes desde 21/07 03:07 BRT)
- Log cadência: `/root/agent_data/seo_pruning_cadence.log`
- Removedor no-home (rotina distinta, permanece ativo): `/root/remover_no_home.py`, cron `0 */2 * * *`
- [[project-no-home-score-policy-v1-20260721]] — política de home/no-home no worker (também não é pruning)

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-23 09:55 BRT.
