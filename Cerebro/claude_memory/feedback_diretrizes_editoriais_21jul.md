---
name: feedback-diretrizes-editoriais-21jul
description: 4 diretrizes editoriais adicionadas em 2026-07-21 08:20 BRT — rate limit 1 publish/ciclo (2/hora), esporte com siglas rejeitar, título com nome próprio desconhecido reformular, siglas partido político MAIÚSCULAS. Miguel decide home vs no-home (Sentinela NÃO decide).
metadata:
  type: feedback
  author: Claude Code (Anthropic, claude-opus-4-7 → deepseek-v4-pro)
  written_at: 2026-07-21 08:52 BRT
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## 4 regras editoriais definidas 2026-07-21 07:57-08:20 BRT

### R1. Rate limit 1 publish/ciclo (2/hora max)

**Sentinela NUNCA publica mais de 1 draft por ciclo, MAX_PUBLISH_POR_CICLO=1.**

Contexto: Miguel 08:20 BRT: *"não pode entrar mais de 2 posts por hora, então tem que pegar leve"*. Ciclo Sentinela via `/loop` roda 2/hora (`:03/:33`). Máx 1 publish por ciclo = 2 publish/hora max.

Falha prévia: ciclo 08:44 publicou 2 posts (incluindo 262409 esporte que Miguel pediu rebaixar às 07:57). Rate limit implementado depois, corrige próximo ciclo.

### R2. Esporte com siglas → REJEITAR

Cafezinho NÃO cobre esporte com siglas (F1, FIFA, UEFA, AFA, CBF, MotoGP, NBA, NFL, NHL, MLB, ATP, WTA, Champions, Libertadores, Fórmula 1, Fórmula E).

Sentinela: se draft V4 tem título com essas siglas OU tema esportivo → NÃO PUBLICA. `propor_correcao_semantica` com motivo `tema_esporte_siglas_rejeitado`.

Exceção: matéria política/denúncia sobre esporte (FBI investiga AFA, corrupção FIFA) — publicar normal (é política, não cobertura esportiva).

Caso fundador: post 262409 "Simulações revelam fragilidade dos carros de F1 de 2026 no circuito de Spa" — Miguel pediu rebaixar 07:57 BRT, Sentinela publicou por erro 08:44, rebaixado 08:52.

### R3. Título com nome próprio desconhecido → REFORMULAR genérico

Título de post não pode começar com nome próprio de empresa/pessoa/tecnologia que leitor médio não conhece antes de contexto.

**Conhecidas SUFICIENTES pra usar direto no título:** OpenAI, Google, Apple, Microsoft, Amazon, Meta, Facebook, Instagram, WhatsApp, Twitter/X, TikTok, Uber, Netflix, Tesla, SpaceX, ChatGPT, Claude, Gemini, iPhone, Android.

**Exigem contextualização:** Hugging Face, Anthropic, Nvidia (dependendo público), Waymo, PsiQuantum, Infinity, Current AI, Andon Labs, Snowflake, Databricks, HashiCorp, Cloudflare.

Padrão de reformulação: `{qualificador editorial genérico} {nome próprio} {verbo/complemento}`.
- ❌ "Hugging Face sofre ataque cibernético"
- ✅ "Plataforma de IA de código aberto Hugging Face sofre ataque cibernético"

### R4. Siglas de partido político → MAIÚSCULAS

Todo partido brasileiro em MAIÚSCULAS: PP, PT, PSDB, PL, MDB, PDT, PSOL, PSB, REDE, PODE, UNIÃO, NOVO, CIDADANIA, AVANTE, PATRIOTA, REPUBLICANOS.

Sentinela: se draft tem título com sigla partido em minúscula/mista, aplicar `corrigir_grafia` antes de publicar (NÃO bloquear — só corrigir).

Exemplos:
- "atrair União Brasil e Pp" → "atrair União Brasil e PP"
- "Filiado Ao Pt" → "Filiado ao PT"

## Distribuição home vs no-home (Miguel decide, Sentinela NÃO)

Miguel 08:23 BRT: *"vou dizer quais posts podem entrar na home, e quais ficam no-home"*

Miguel 08:25 BRT (proporção alvo):
- **Ciência/Tecnologia:** 80% home, 20% no-home
- **Geopolítica:** 60% home, 40% no-home
- **Nacional:** 0% home, 100% no-home

**Modo de decisão** (pendente ainda de fluxo definitivo):
- Opção A: Sentinela mantém contador diário por editoria e decide algoritmicamente pra atingir target (ratio acumulado < target = home; ratio ≥ target = no-home)
- Opção B: Miguel diz caso a caso ("publica 262403 home, 262400 no-home")
- Opção C: Sentinela publica tudo default no-home, Miguel promove pra home manual via wp-admin

Implementação atual: código tem `PROPORCAO_HOME_POR_EDITORIA` + `_decidir_home_ou_nohome()` mas ainda **não ativo no fluxo publish**. Aguarda decisão Miguel de modo.

## Contexto — migração Anthropic → DeepSeek

Sentinela mudou de Anthropic Opus 4.7 (crédito zerou 21/07 00:44 BRT) para DeepSeek V4 Pro (21/07 07:56 BRT). max_tokens=8000 pra permitir reasoning_tokens embutidos. response_format=json_object. Custo ~30x menor.

## Relacionadas

- [[feedback-sentinela-nunca-publicar-rascunhos-antigos]] — cap 2h idade
- [[feedback-diretriz-editorial-governos-esquerda]] — linha editorial anti-imperialista
- [[feedback-sujeira-metadata-pipeline-v4]] — detecção sujeira
- [[feedback-baleia-azul-diario-obrigatorio]] — Baleia todo dia
- Post rebaixado por diretriz: 262409 (F1 Spa)

## Assinatura

Registro escrito por Claude Code (Anthropic → DeepSeek V4 Pro no Sentinela), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020`, 2026-07-21 08:52 BRT.
