---
name: feedback-auditores-devem-ser-preventivos-nao-reativos
description: "Aprendizado sistêmico — todo agente rotulado \"auditor\" no ecossistema deve olhar rascunhos/pending (preventivo), não posts já publicados (reativo). Auditar depois de publicar é apenas validação passiva"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 13/08/2026 ~22:15 BRT: *"essa era pra ser a ideia. é um erro conceitual"* — ao confirmar que o `agente_auditor_titulos_gpt.py` deveria desde o início auditar `pending`, não `publish`.

## Padrão conceitual

**Auditor** no ecossistema Cafezinho tem obrigação preventiva. O sujeito do verbo "auditar" precisa poder INFLUENCIAR o output antes que ele vá pro leitor. Depois do publish, é só validação passiva — não previne erro, só registra que aconteceu.

**Preventivo** (correto): auditor lê `draft`/`pending` → aponta problema → agente humano/IA revisor corrige → publish sai limpo.

**Reativo** (errado): auditor lê `publish` → aponta problema tarde → correção in-place chura métrica de qualidade OU deixa o erro no ar até alguém notar.

## Padrão identificado no ecossistema (13/08)

**Auditores atuais que estão reativos (deveriam ser preventivos):**
- `agente_auditor_titulos_gpt.py` (cron `*/10`) — audita só `publish` do repetidor estatal. Não olha pending do worker V4. → cartinha ZCode `[CLAUDE-PEDIDO-AUDITOR-TITULOS-GPT-MODO-PREVENTIVO-20260813-2210-BRT]` propõe modo `advisor` que olha pending.

**Casos legítimos de agente reativo** (não é auditor, é operação):
- `agente_comentarista_v4.py` — comentário só existe em post publish por design (não tem como comentar rascunho).
- `daemon_indexador.py` — indexação Google só faz sentido em URL publish.
- `agente_autocura_v4.py` — cura estado após incidente por natureza.

**Casos borderline** — deveriam ser mais preventivos:
- `agente_manchete.py` (cron `0 */2`) — escolhe manchete DEPOIS que posts já estão publish. Sprint atual (política manchete curadoria [[project-politica-manchete-curadoria-inteligente-20260813]]) tenta destravar: juiz LLM decide entre candidatos ANTES da capa mudar. Mesmo padrão preventivo.
- `sync_cerebro_to_github.py` — filtra sensíveis DEPOIS de já ter copiado. Poderia rejeitar no diff (mas custo/benefício não justifica hoje).

## Regra pra aplicar em novos agentes

Ao propor/revisar novo agente rotulado "auditor", "revisor", "curador", "validador", "árbitro" no ecossistema Cafezinho, primeira pergunta: **ele age antes ou depois do output ir pro leitor?**

- **Antes** → auditor de verdade (preventivo)
- **Depois** → não use o rótulo "auditor". Use "monitor", "log", "métrica", "QA retro"

O rótulo importa porque cria expectativa. "Auditor" que só valida é enganoso — parece que está protegendo qualidade quando na verdade só documenta erro.

## Como identificar auditor mal-implementado

Sinal de alerta em código de agente rotulado "auditor":
- Query com `post_status = 'publish'` sem também olhar `draft`/`pending`
- Trigger `on_publish` sem trigger `on_pending` ou `on_scheduled`
- Output que só serve pra métrica/log (nada consome pra corrigir)
- Nome tipo `poll_publish.py` mascarando função reativa

Se identificar isso em revisão de código futuro, **escalar Miguel/ZCode** pra fix conceitual, não deixar acumular tech debt.

## Aplicação retroativa 13/08

Cartinha ZCode enviada com contexto de bug conceitual explicitado. Aguarda implementação. Depois de rodando o modo `advisor`, atualizar meu prompt Vigília V6 pra ler `advisor_pending.jsonl` antes do patch.

Regras irmãs: [[project-politica-manchete-curadoria-inteligente-20260813]] (mesmo padrão preventivo pra manchete) · [[feedback-auditor-titulos-v4-7-regras-canonico]] (as regras que auditor deve aplicar) · [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]].
