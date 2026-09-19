---
name: feedback-sujeira-metadata-pipeline-v4
description: "Pipeline V4 pode vazar slug de categoria, campos JSON, UUIDs, timestamps, comentários debug como TEXTO dentro do corpo do post. Sentinela deve pegar ANTES de publicar. Se passou pra publicado, limpar retroativo."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-20 23:15 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra

**Toda auditoria de draft/publicado deve verificar sujeira estrutural de METADATA/SLUG vazando como texto no corpo do post — não só vazamento de fala IA.**

Padrões conhecidos (9 grupos, expandidos no `PADROES_VAZAMENTO_IA` do `sentinela_ciclo.py`):

1. `<p><em>ciencia-tecnologia</em></p>` — slug categoria em `<em>` (o que Miguel achou no 262378)
2. `<p><strong>geopolitica</strong></p>` — variante com `<strong>`
3. `<p>nacional</p>` — slug puro em parágrafo
4. `<p>"vertical": "ciencia"</p>` — campo JSON vazando literal
5. `<p>vertical=nacional</p>` — chave=valor sem parsing
6. `<p>5f9b197632f64e5c</p>` ou `<p>v4d_geopolitica_xxx</p>` — UUID/hash job_id
7. `<p>2026-07-20T12:15</p>` — timestamp isolado
8. `<!-- TODO/DEBUG/FIXME/WIP: -->` — comentários debug esquecidos
9. `{{categoria}}` ou `<<PAUTA>>` — placeholder de prompt não substituído

**Why:** Miguel identificou 2026-07-20 22:XX BRT que post 262378 ("Infinity desafia Nvidia") tinha `<p><em>ciencia-tecnologia</em></p>` como primeira linha do corpo — slug interno da categoria WP vazando como texto editorial. Sentinela publicou sem detectar porque as 14 regex iniciais só cobriam "fala de IA" (aqui está, como assistente, etc), não sujeira estrutural. Miguel: *"porque essa tag perdida ciencia-tecnologia no inicio, isso é vazamento de sujeira interna do agente. não teve auditoria? corrige urgente e toma as medidas necessárias para não ocorrer de novo... pedi pro codex corrigir mas quero que voce fique mais atento a sujeiras como essa. voce deve limpar."*

Codex corrigiu 262378 às 23:00 BRT. Escaneamento completo dos 39 posts V4 publicados hoje: zero outros afetados.

**How to apply:**

### 1. No código Python (`sentinela_ciclo.py`)

`PADROES_VAZAMENTO_IA` expandido de 14 → **23 padrões**, agrupados em "A) Fala IA" (14) e "B) Sujeira METADATA" (9). Todo draft elegível + todo publicado nas últimas 2h passa pelos 23 padrões.

### 2. No prompt do Sentinela (`config/prompts.md`)

Instruções específicas por grupo:

**Sujeira METADATA em DRAFT:**
- NÃO PUBLICA — bug estrutural do V4
- Registrar alerta com `sujeira_metadata_v4_pipeline` (Codex precisa saber)
- Se conseguir remover automaticamente (`trecho_remover` bem definido), fazer

**Sujeira METADATA em PUBLICADO (auditoria retroativa):**
- **REMOÇÃO IMEDIATA via `editar_corpo_publicado`** (fix seguro, linha isolada sem contexto editorial)
- Log em `mudancas_aplicadas/YYYY-MM-DD.jsonl` como `action: "limpar_sujeira_metadata_slug"`

### 3. Alertar Codex se recorrer

Se o mesmo padrão aparecer em >2 posts V4 em janela de 24h, é **bug persistente do pipeline** — não conserta só limpando publicados, precisa Codex investigar `v4_vertical_draft_worker.py` ou o redator específico.

### 4. Escaneamento retroativo periódico

A cada 24h (idealmente no ciclo Baleia Azul da noite), Sentinela pode fazer scan amplo em posts V4 dos últimos 7 dias procurando sujeiras que possam ter escapado antes desta regra estar ativa.

## Casos conhecidos

- **2026-07-20 22:XX BRT — post 262378** ("Infinity Nvidia") — `<p><em>ciencia-tecnologia</em></p>` na primeira linha do corpo. Codex corrigiu 23:00 BRT.

## Relacionadas

- [[feedback-sentinela-nunca-publicar-rascunhos-antigos]] — cap 2h de idade
- [[feedback-diretriz-editorial-governos-esquerda]] — regra editorial
- [[feedback-biblioteca-nao-sobrescreve-identidade-agente]] — identidade caller
- Padrão de vazamento: `PADROES_VAZAMENTO_IA` em `~/ferramentas/sentinela/sentinela_ciclo.py` (agora com 23 padrões)

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-20 23:15 BRT.
