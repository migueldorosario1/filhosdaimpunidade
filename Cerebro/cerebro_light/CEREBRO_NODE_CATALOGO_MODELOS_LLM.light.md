# CEREBRO_NODE_CATALOGO_MODELOS_LLM — VERSÃO LIGHT
> Gerado automaticamente por `cerebro_light.py` em 2026-07-09 03:32 BRT
> Original: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` (29KB) — 57 entradas totais
> Este arquivo é READ-ONLY. Edite sempre o original.

---

## CABEÇALHO ORIGINAL (primeiras linhas)

# 🤖 CÉREBRO CAMADA 2: Catálogo de Modelos LLM

**Criado:** 2026-05-25 17:20 BRT
**Autor:** Claude Maestro (por ordem de Miguel)
**Objetivo:** Banco de dados completo de todos os modelos de IA — preços, características, benchmarks, notas. Serve para: (1) roteador dinâmico do Cafezinho, (2) matérias e rankings do portal Aiatolah, (3) referência da Trindade.
**Fórum de trabalho:** `Foruns/forum_pesquisa_precos_llms_20260525.md`
**Arquivo de dados:** `root/config/llm_ratings.json` (roteador dinâmico)

> **Regra:** Este nodo é PERMANENTE e deve ser atualizado sempre que um modelo novo for testado, um preço mudar, ou um benchmark for publicado. Qualquer engenheiro da Trindade pode atualizar.

---

## 1. Índice por Provider

- [Anthropic (Claude)](#anthropic-claude)
- [OpenAI (GPT)](#openai-gpt)
- [Google (Gemini)](#google-gemini)
- [DeepSeek](#deepseek)
- [Alibaba (Qwen)](#alibaba-qwen)
- [Zhipu (GLM)](#zhipu-glm)
- [Moonshot (Kimi)](#moonshot-kimi)
- [xAI (Grok)](#xai-grok)
- [Mistral](#mistral)
- [Meta (Llama via Groq)](#meta-llama-via-groq)
- [Perplexity (Sonar)](#perplexity-sonar)
- [Geradores de Imagem](#geradores-de-imagem)
- [Ranking por Custo](#ranking-consolidado-por-custo)
- [Ranking por Velocidade](#ranking-por-velocidade)
- [Modelos Reasoning — Alerta](#modelos-reasoning--alerta)

---

## 2. Anthropic (Claude)

**País:** EUA | **Fundação:** 2021 | **Site:** anthropic.com | **API:** api.anthropic.com

### claude-opus-4-7
| Campo | Valor |
|-------|-------|
| **Model ID** | `claude-opus-4-7` |
| **Tipo** | Texto + Visão |
| **Contexto** | 1M tokens |
| **Preço Input** | $5.00 / 1M tokens |
| **Preço Output** | $25.00 / 1M tokens |
| **Batch** | 50% off ($2.50 / $12.50) |
| **Prompt Caching** | $0.30 (write) / $0.30 (read) / 1M tokens |
| **Reasoning** | Não (pode ativar extended thinking) |
| **Notas Q/P/V** | Q5 P1 V3 |
| **Status Cafezinho** | BLOQUEADO (custo proibitivo §54) |
| **Lançamento** | Jan 2026 |
| **Pontos fortes** | Melhor qualidade editorial, obedece instruções complexas, reasoning profundo |
| **Pontos fracos** | Muito caro para pipeline em massa |
| **Benchmark** | GPQA 74.5%, SWE-bench Verified 72.1% |
| **Verificado em** | 2026-05-25 |

### claude-sonnet-4-6
| Campo | Valor |
|-------|-------|
| **Model ID** | `claude-sonnet-4-6` |
| **Tipo** | Texto + Visão |

---

## ⏩ 52 entradas antigas omitidas
> Para ver o histórico completo, leia `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` diretamente.
> Busca rápida: `python3 cerebro.py --buscar <termo>`

---

## ÚLTIMAS 5 ENTRADAS

### Flux Pro v1.1
| Campo | Valor |
|-------|-------|
| **Provider** | fal.ai |
| **Endpoints** | `fal.run/fal-ai/flux-pro/v1.1`, `fal.run/fal-ai/flux-pro` |
| **Preço** | ~$0.05 / imagem |
| **Status Cafezinho** | Fallback 1 — menos censura política |

---

### DALL-E 3
| Campo | Valor |
|-------|-------|
| **Provider** | OpenAI |
| **Model ID** | `dall-e-3` |
| **Preço** | ~$0.04-0.12 / imagem |
| **Status Cafezinho** | Fallback 2 |

---

---

## 14. Ranking Consolidado por Custo (Input, mais barato primeiro)

| # | Modelo | $/1M Input | Provider | Observação |
|---|--------|-----------|---------|------------|
| 1 | glm-4.7-flash | **$0.00** | Zhipu | Grátis mas inútil (100% reasoning) |
| 1 | glm-4.6v-flash | **$0.00** | Zhipu | Grátis mas inútil (vision reasoning chinês) |
| 2 | deepseek-v4-flash | $0.14 | DeepSeek | Periféricos |
| 3 | deepseek-coder | $0.14 | DeepSeek | Código/Trindade |
| 4 | gpt-4o-mini | $0.15 | OpenAI | Periféricos |
| 5 | mistral-small-latest | $0.15 | Mistral | Periféricos |
| 6 | grok-4.1-fast | $0.20 | xAI | Candidato econômico |
| 7 | sonar | $0.25 | Perplexity | Fact-check básico |
| 8 | qwen-plus / qwen-vl-plus | $0.26 | Alibaba | Periféricos / Vision |
| 9 | gemini-2.5-flash | $0.30 | Google | Pe

> *(... 1418 chars omitidos — ler original)*

---

## 15. Ranking por Velocidade (teste editorial padronizado 25/05)

| # | Modelo | Tempo | Provider | Observação |
|---|--------|-------|---------|------------|
| 1 | llama-3.3-70b (Groq) | **0.8s** | Groq | Ultra-rápido |
| 2 | qwen-vl-plus | 1.2s | Alibaba | Vision OCR |
| 3 | qwen-vl-max-latest | 1.4s | Alibaba | Vision alta qualidade |
| 4 | deepseek-v4-pro | 2.2s | DeepSeek | Variável: 2.2-59s |
| 5 | gpt-4o-mini | 2.4s | OpenAI | Consistente |
| 6 | moonshot-v1-32k | 2.5s | Moonshot | Kimi Code: 2.5s; Claude: 8.9s pico |
| 7 | gpt-4o | 2.8s | OpenAI | Rápido e qualidade |
| 8 | glm-4-plus | 3.7s | Zhipu | Único non-reasoning Zhipu |
| 9 | glm-4.5-air | 3.8s | Zhipu | ⚠️ 100% reasoning, content vazio |
| 10 | glm-4.7-flash | 4.7s | Zhipu | ⚠️ Grátis mas inútil |
| 11 | qwen-max | 4.5s 

> *(... 680 chars omitidos — ler original)*

---

## 16. Modelos Reasoning — Alerta

Estes modelos gastam tokens "pensando" internamente. **IMPRÓPRIOS para pipeline editorial em massa** (custo e latência 10-100x maiores):

| Modelo | Reasoning tokens no teste | Custo real vs aparente | Observação |
|--------|--------------------------|----------------------|------------|
| `glm-4.7` | 902 (para output de 18) | **50x mais caro** | ⚠️ NÃO DOCUMENTADO como reasoning |
| `glm-4.7-flash` | 200-1000 (para output de 0) | **∞** | Grátis mas content SEMPRE vazio |
| `glm-4.7-flashx` | 500 (para output de 0) | **∞** | Content vazio |
| `glm-4.5-air` | 200 (para output de 0) | **∞** | Content vazio |
| `glm-4.6v-flash` | 198 (para output de 2) | **99x** | Raciocina em CHINÊS |
| `qwen3.7-max` | 2227 (para output de 95) | 23x | Documentado como reaso

> *(... 1054 chars omitidos — ler original)*

---

## PONTEIROS
- Original completo: [`CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`](./CEREBRO_NODE_CATALOGO_MODELOS_LLM.md)
- Índice geral: [`indice_cerebro.json`](./indice_cerebro.json)
- Busca: `python3 cerebro.py --buscar <termo>`
- Validador: `python3 validar_cerebro.py`