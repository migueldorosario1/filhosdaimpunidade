---
name: project-esteira-youtube-cafezinho-20260721
description: "Agente YouTube Cafezinho gera 4 drafts/dia (06/12/18/23h BRT) via cron. Autor 5470 (Redação). Sentinela é responsável por checagem dupla + publish. Cloddy é layer humano/agente pra casos que Sentinela escala."
metadata:
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-21 17:55 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Fluxo da esteira YouTube Cafezinho

### 1. Agente coleta+redige (autônomo)
- **Cron:** 4 rodadas/dia às 06:00, 12:00, 18:00, 23:00 BRT
- **Código:** `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py`
- **Config externa:** `agent_data/curadoria_cafezinho_youtube.json` (personagens prioritários — Lula/Haddad/Boulos/Nassif/Reinaldo; vilões — Bolsonaro/Milei/Netanyahu/Tarcísio; canais orientação — TV Fórum, TV 247, DCM + 1 livre)
- **Motor:** V4 aprovado (teste Felipe Pena = "perfeito", post 262473 21/07 17:00)
- **Anti-repetição:** sem repetir canal no dia nem personagem em 3 dias, anti-estreia agendada, só vídeo completo
- **Autor WP:** 5470 (Redação, mesmo do V4)
- **Log:** `agent_data/v4_cafezinho_youtube/cron.log`

### 2. Sentinela checa+publica (nosso escopo)
- Ciclos do Sentinela (~40/dia) coletam drafts autor 5470 — inclui os posts-vídeo
- **Checagem dupla obrigatória** (mesma regra de todos drafts):
  - 1ª leitura: embed YouTube no topo? Título com nome? Lide contextualiza?
  - 2ª leitura integral: trecho citado bate com "momento mais tenso"? Vilão nomeado certo? Fonte (canal) citada? Sem sujeira metadata?
- Se passa → publish
- Se tropeça → `propor_correcao_semantica`, NÃO publica, NÃO rebaixa (regra churn)
- Cap idade 2h padrão (mesma do V4)
- **Home vs no-home:** herda do worker YouTube (default HOME se não veio com 20699)

### 3. Cloddy layer humano/agente (última camada)
- Cartinha canônica: `Cerebro/Foruns/carta_para_cloddy_agente_youtube_cafezinho_20260721.md`
- Ele olha fila drafts 30min após cada rodada (06:30, 12:30, 18:30, 23:30)
- Casos que Sentinela escalar via alerta → Cloddy audita humanamente
- URL fila: link direto no wp-admin

## Formato do post-vídeo (padrão editorial)

- **Embed no topo** (iframe YouTube ou tag `[embed]`)
- **Título:** nome da pessoa + verbo + tema (`{Nome} + {verbo forte} + {contexto}`)
- **Corpo:** chamada + trecho da fala + contexto do vilão + link do canal
- **Aspas simples** (`'`) nas citações, não aspas duplas
- **≥300 chars** no corpo (mais curto que V4 texto — essência é o vídeo)

## Diferenças em relação ao V4 tradicional

| Aspecto | V4 texto | Post-vídeo YouTube |
|---|---|---|
| Cron | 05/35 * * * * (a cada hora) | 06/12/18/23h (4x/dia) |
| Autor | 5470 | 5470 |
| Home/no-home | Score policy (Nacional≥13, Geopol≥12, Ciência≥10) | Herda do worker (default HOME) |
| Featured media | Obrigatório | Embed vídeo faz o papel visual (mas pode ter thumbnail YouTube como featured) |
| Corpo min | 500 chars | 300 chars |
| Ranking editorial | Auditor GPT | Curadoria por peso (personagem × canal × entrevista) |

## Ações Sentinela (implementadas 21/07 17:55)

- Nova seção "📹 POSTS-VÍDEO YOUTUBE CAFEZINHO" em `~/ferramentas/sentinela/config/prompts.md`
- Prompt inclui: como reconhecer post-vídeo, checagem dupla específica, critérios de publish, home vs no-home, referências ao código/config/log
- Sem mudança de código Python necessária (Sentinela já processa drafts autor 5470 uniformemente)
- Primeira rodada oficial do cron: 2026-07-22 06:00 BRT

## Relacionadas

- [[feedback-nunca-churn-publish-draft-seo]] — regra churn aplica a posts-vídeo também
- [[project-no-home-score-policy-v1-20260721]] — política do V4 texto; posts-vídeo têm rota separada
- [[project-loop-sentinela-cron-dia-noite-20260721]] — cron do Sentinela que fará a checagem
- [[feedback-diretrizes-editoriais-21jul]] — R1-R4 (rate limit, esporte siglas, nome próprio desconhecido, partido MAIÚSCULO) valem também
- Cartinha Cloddy: `Cerebro/Foruns/carta_para_cloddy_agente_youtube_cafezinho_20260721.md`

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-21 17:55 BRT.
