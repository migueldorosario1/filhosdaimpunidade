---
name: feedback-nunca-churn-publish-draft-seo
description: "NUNCA rebaixar publish→draft e depois republicar. Google Index/Bing/agregadores punem URLs que alternam 200 OK↔404. Derruba ranking do site inteiro. Uma vez publicado, decisão é: correção in-place OU escalar ao Miguel. NUNCA churn."
metadata:
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-21 16:55 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra inviolável

**Uma vez publicado (`status = publish`), o post NUNCA é rebaixado pra `draft` pra depois republicar.** Sem exceção — nem "ah só um minuto pra corrigir", nem "vou rebaixar e refazer melhor".

### O que fazer se detectar problema em post publicado:
- ✅ **Correção in-place** — editar título, corpo, categoria diretamente via `POST /wp-json/wp/v2/posts/{id}` sem mudar status
- ✅ **Escalar ao Miguel via `alertas`** se problema for grave/irrecuperável — ele decide se remove ou não
- ❌ **NUNCA** `status: publish → status: draft → status: publish` (churn = ping-pong SEO)
- ❌ **NUNCA** ficar num loop "publica, rebaixa, decide, publica, rebaixa"

**Why:** Google Index, Bing e agregadores penalizam URLs que alternam `200 OK` ↔ `404/redirect` ↔ `200 OK`. Cada rebaixamento faz URL responder 404 (ou redirect), quando volta o crawler vê churn e diminui trust. Derruba **ranking do site inteiro**, não só do post afetado. Um único post fazendo ping-pong prejudica visibilidade orgânica do Cafezinho todo.

**Caso fundador 2026-07-21 16:50 BRT:** Post 262403 (Hugging Face — cyberattack) ficou o dia inteiro em ciclo publica-rebaixa-decide por causa da regra D2 (nome próprio de tech desconhecida sem contexto no título). Sentinela (Claude) publicava, DeepSeek do próximo ciclo achava que precisava contextualizar título, rebaixava proposta de correção, e assim indefinidamente. Miguel interveio: *"esse hugging face está o dia inteiro nessa palhaçada... deixa publicado, deixa no home. Está resolvido. Esse hugging face aí. Mas fica ligado aí, não pode ficar brincando de ficar botando rascunho, tirando rascunho e botar de novo não, tá? Toma cuidado com isso. Google Index pune isso, viu?"*

## Como aplicar

### 1. Prompt Sentinela (`~/ferramentas/sentinela/config/prompts.md`)
Seção "🚫 CHURN PUBLISH↔DRAFT — PROIBIDO" adicionada 2026-07-21 16:55 BRT. Se DeepSeek/Opus sugerir rebaixar publish → ignorar.

### 2. Ação `restaurar_publish` no schema JSON
Existe SÓ pra caso oposto (worker externo/agente errado rebaixou um publish legítimo → restauramos pra publish). **NUNCA usar pra rebaixar** publish→draft.

### 3. Decisão editorial em UM único ciclo
Quando um draft entra em análise, **decida uma vez**: publica agora ou não publica. Se publica → não mexer mais no status. Se não publica → gera `propor_correcao_semantica` E deixa como draft, não fica publicando e rebaixando pra "reavaliar".

### 4. Ao detectar padrão recorrente de churn
Se algum post aparecer em >2 ciclos consecutivos com decisões opostas (publica/rebaixa), é um bug do agente decisor — parar, gravar alerta e escalar ao Miguel.

## Regra correlata (mesma sessão)

**Leitura dupla obrigatória do corpo antes de publicar** (Miguel 16:50 BRT: "tá fazendo a checagem dupla? tá lendo uma vez, duas vezes, pra checar se o texto tá certo?"):
1. Primeira leitura (skim): título + lide + p1
2. Segunda leitura (integral): todo o corpo procurando nome errado, data errada, valor absurdo, contradição, falta de fonte, tom anti-linha, rodapé com sujeira
3. Se as duas passam → publique. Se qualquer tropeça → NÃO publica.

## Relacionadas

- [[feedback-sentinela-nunca-publicar-rascunhos-antigos]] — cap 2h continua valendo
- [[feedback-diretrizes-editoriais-21jul]] — R1-R4 continuam
- [[project-no-home-score-policy-v1-20260721]] — política de home/no-home
- `~/ferramentas/sentinela/config/prompts.md` seções "🚫 CHURN PUBLISH↔DRAFT" e "🔎 LEITURA DUPLA DO CORPO"

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-21 16:55 BRT.
