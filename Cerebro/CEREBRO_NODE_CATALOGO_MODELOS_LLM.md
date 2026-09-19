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
| **Contexto** | 1M tokens |
| **Preço Input** | $3.00 / 1M tokens |
| **Preço Output** | $15.00 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q5 P1 V3 |
| **Status Cafezinho** | Ativo (saldo recarregado 25/05) — fallback fact-check |
| **Lançamento** | Out 2025 |
| **Pontos fortes** | Excelente custo-benefício para auditoria, boa obediência |
| **Pontos fracos** | Caro vs chineses |
| **Verificado em** | 2026-05-25 |

### claude-haiku-4-5
| Campo | Valor |
|-------|-------|
| **Model ID** | `claude-haiku-4-5-20251001` |
| **Tipo** | Texto |
| **Contexto** | 200K tokens |
| **Preço Input** | $1.00 / 1M tokens |
| **Preço Output** | $5.00 / 1M tokens |
| **Batch** | 50% off |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P3 V4 |
| **Status Cafezinho** | BLOQUEADO (emergência financeira) |
| **Verificado em** | 2026-05-25 |

---

## 3. OpenAI (GPT)

**País:** EUA | **Fundação:** 2015 | **Site:** openai.com | **API:** api.openai.com

### gpt-5.6 (família Sol / Terra / Luna)
| Campo | Valor |
|-------|-------|
| **Model IDs** | `gpt-5.6-sol` (alias `gpt-5.6` = Sol; `daybreak-blue-latest` também aponta pro Sol) · `gpt-5.6-terra` · `gpt-5.6-luna` |
| **Tipo** | Texto + Reasoning + Programmatic Tool Calling (escreve/executa código p/ usar ferramentas) — Responses API |
| **Contexto** | ~1,05M tokens in / 128K out (Sol) |
| **Preços standard/1M** | **Sol $4,00 in / $20,00 out** (cache hit $0,40) · Terra $2,00/$12,00 (cache $0,20) · Luna $0,20/$1,20 (cache $0,02) — contexto longo Sol $8/$30 |
| **Promoção** | Preço do Sol é **PROMOCIONAL garantido ao menos até 21/11/2026**; regular não divulgado. Batch/Flex = 50% off (assíncrono, não serve p/ agente interativo). Endpoints regionais +10% |
| **Notas Q/P/V** | Sol Q5 P1 V? — frontier ocidental (raciocínio/código/agente). **Mais barato que gpt-5.5 ($5/$30) e 7-9× mais barato que os "-pro" ($30/$180)** |
| **Benchmarks (25/08)** | Terminal-Bench 2.0: **#1 mundo 91,9%** (2º a 4,5 pts) · Terminal-Bench 2.1: SOTA · Artificial Analysis Coding Agent Index: **líder 80 pts a ~1/3 do custo do Claude top** · SWE-bench Pro: 64,6% — **atrás do qwen3.8-max (67,7%)** · SWE-bench Verified: Claudes no topo (~93-95%), Sol atrás. ⚠️ System Card: recomenda supervisão humana em trajetórias agênticas longas (pontua alto em Agentic Misalignment). **AA Intelligence Index (max, 25/08): Sol 61 · Terra 57 · Luna 52** — qualidade cai ~15% do Sol pro Luna enquanto preço cai 20× |
| **Status Cafezinho** | Sol: candidato a **luxo sob demanda no ZCode** (crédito pay-go do Miguel, 25/08) — NÃO ligar em produção/pipeline sem teto (histórico superprodução US$ 39/5d com gpt-5.5). Luna $0,20/$1,20: candidato a periférico (junto ao gpt-4o-mini $0,15/$0,60 na coleta). Terra: meio do caminho |
| **Verificado em** | 2026-08-25 (fontes: developers.openai.com/api/docs/pricing + anúncio openai.com/index/gpt-5-6/) |

### gpt-4o
| Campo | Valor |
|-------|-------|
| **Model ID** | `gpt-4o` |
| **Tipo** | Texto + Visão + Áudio |
| **Contexto** | 128K tokens |
| **Preço Input** | $2.50 / 1M tokens |
| **Preço Output** | $10.00 / 1M tokens |
| **Cached Input** | $1.25 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q4 P2 V4 |
| **Status Cafezinho** | Ativo — fallback ocidental na cascata |
| **Tempo teste** | 2.8s (prompt editorial padrão) |
| **Pontos fortes** | Rápido, boa qualidade, vision integrado |
| **Pontos fracos** | Caro vs chineses, viés ocidental |
| **Verificado em** | 2026-05-25 |

### gpt-4o-mini
| Campo | Valor |
|-------|-------|
| **Model ID** | `gpt-4o-mini` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.15 / 1M tokens |
| **Preço Output** | $0.60 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q2 P5 V5 |
| **Status Cafezinho** | Ativo — triagem e periféricos |
| **Tempo teste** | 2.4s |
| **Pontos fortes** | Ultra-barato, rápido |
| **Pontos fracos** | Qualidade insuficiente para editorial |
| **Verificado em** | 2026-05-25 |

### gpt-5
| Campo | Valor |
|-------|-------|
| **Model ID** | `gpt-5` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 400K tokens |
| **Preço Input** | $1.25 / 1M tokens |
| **Preço Output** | $10.00 / 1M tokens |
| **Reasoning** | Sim |
| **Notas Q/P/V** | Q5 P2 V1 |
| **Status Cafezinho** | BLOQUEADO (§54 — reasoning caro) |
| **Verificado em** | 2026-05-25 |

---

## 4. Google (Gemini)

**País:** EUA | **Fundação:** 2023 (DeepMind) | **Site:** ai.google.dev | **API:** generativelanguage.googleapis.com

### gemini-2.5-pro
| Campo | Valor |
|-------|-------|
| **Model ID** | `gemini-2.5-pro` |
| **Tipo** | Texto + Visão + Áudio + Vídeo |
| **Contexto** | 1M tokens |
| **Preço Input** | $1.00-1.25 / 1M tokens |
| **Preço Output** | $10.00 / 1M tokens |
| **Reasoning** | Sim (thinking tokens) |
| **Notas Q/P/V** | Q5 P2 V3 |
| **Status Cafezinho** | Ativo — Tribunal Visual + auditoria fallback |
| **Pontos fortes** | Multimodal excelente, contexto enorme |
| **Pontos fracos** | Reasoning consome tokens extras |
| **Verificado em** | 2026-05-25 |

### gemini-2.5-flash
| Campo | Valor |
|-------|-------|
| **Model ID** | `gemini-2.5-flash` |
| **Tipo** | Texto + Visão |
| **Contexto** | 1M tokens |
| **Preço Input** | $0.30 / 1M tokens |
| **Preço Output** | $2.50 / 1M tokens |
| **Free tier** | Sim (15 RPM) |
| **Reasoning** | Sim (thinking tokens — 765 tokens para output de 31 no teste!) |
| **Notas Q/P/V** | Q2 P4 V3 |
| **Status Cafezinho** | Ativo — Tribunal Visual cross-check + periféricos |
| **Tempo teste** | 5.7s (+ 765 tokens reasoning interno) |
| **Pontos fortes** | Barato, free tier, bom em vision |
| **Pontos fracos** | Reasoning inflaciona tokens silenciosamente |
| **Verificado em** | 2026-05-25 |

---

## 5. DeepSeek

**País:** China | **Fundação:** 2023 | **Site:** deepseek.com | **API:** api.deepseek.com

### deepseek-v4-pro
| Campo | Valor |
|-------|-------|
| **Model ID** | `deepseek-v4-pro` (alias: `deepseek-chat` até 24/07/2026) |
| **Tipo** | Texto |
| **Contexto** | 1M tokens |
| **Preço Input** | $0.44 / 1M (promo 75% off até 31/05) → regular $1.74 |
| **Preço Output** | $0.87 / 1M (promo) → regular $3.48 |
| **Cache hit** | $0.003-0.014 / 1M tokens |
| **Reasoning** | Não (V4 Pro é não-reasoning) |
| **Temperature** | Exige 0.1 (anti-alucinação) |
| **Max tokens** | Piso 32000 (config Tencent) |
| **Timeout** | 360s (config Tencent) |
| **Notas Q/P/V** | Q5 P5 V4 |
| **Status Cafezinho** | PRIMÁRIO DE REDAÇÃO — 1ª opção na cascata |
| **Tempo teste** | 2.2-59s (varia com complexidade) |
| **Pontos fortes** | Melhor custo-benefício absoluto, qualidade top, passou teste-trava §66 |
| **Pontos fracos** | Latência variável, promo expira 31/05 |
| **Benchmark** | Passou teste-trava decreto fictício (Claude §66.6) |
| **Verificado em** | 2026-05-25 |

### deepseek-v4-flash
| Campo | Valor |
|-------|-------|
| **Model ID** | `deepseek-v4-flash` |
| **Tipo** | Texto |
| **Contexto** | 1M tokens |
| **Preço Input** | $0.14 / 1M tokens |
| **Preço Output** | $0.28 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q2 P5 V5 |
| **Status Cafezinho** | Ativo — periféricos simples apenas |
| **Verificado em** | 2026-05-25 |

### deepseek-chat (V3 — legado)
| Campo | Valor |
|-------|-------|
| **Model ID** | `deepseek-chat` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.27 / 1M tokens |
| **Preço Output** | $1.10 / 1M tokens |
| **Cache hit** | $0.07 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q4 P4 V4 |
| **Status Cafezinho** | Legado — redireciona para V4 Pro em 24/07/2026 |
| **Verificado em** | 2026-05-25 |

### deepseek-reasoner (R1)
| Campo | Valor |
|-------|-------|
| **Model ID** | `deepseek-reasoner` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.55 / 1M tokens |
| **Preço Output** | $2.19 / 1M tokens (inclui reasoning tokens) |
| **Reasoning** | **SIM** — Chain-of-Thought |
| **Notas Q/P/V** | Q5 P3 V1 |
| **Status Cafezinho** | Bloqueado — reasoning caro para pipeline em massa |
| **Verificado em** | 2026-05-25 |

### deepseek-coder
| Campo | Valor |
|-------|-------|
| **Model ID** | `deepseek-coder` |
| **Tipo** | Texto (código) |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.14 / 1M tokens |
| **Preço Output** | $0.28 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q4 P5 V4 |
| **Status Cafezinho** | Ativo — agentes de código da Trindade |
| **Deprecação** | Sendo substituído por V4 Flash |
| **Verificado em** | 2026-05-25 |

---

## 6. Alibaba (Qwen)

**País:** China | **Fundação:** 2023 (Alibaba Cloud) | **Site:** alibabacloud.com | **API:** dashscope-intl.aliyuncs.com

> ⚠️ **ALERTA TOKEN PLAN (01/08/2026):** O Alibaba tem 4 produtos que confundem — **Pay-as-you-go** (DashScope, ATUAL, funciona), **Token Plan Pessoal** (Lite/Standard/Pro, assinatura em Credits), **Token Plan Equipe** (por assento) e **Coding Plan** (só IDEs). O **Token Plan NÃO serve para backend de site em produção (Cafezinho)**: exige endpoint dedicado (`token-plan.cn-beijing.maas.aliyuncs.com/...`) + região Pequim fixa + tem janela 5h/7d com **pausa de serviço** + concorrência limitada. Mesmo padrão de armadilha já documentado para Zhipu/Kimi. A trava sentida é saldo do pay-as-you-go; remédio = recarregar pay-as-you-go ou resource package / Savings Plan. Análise completa: `Foruns/forum_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md` + `Memorias/memoria_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md`. **ATUALIZAÇÃO 07/08/2026 (decisão Miguel):** assinatura pessoal também **NÃO vale a pena** — o uso real de Qwen dele é **vision no pipeline Cafezinho** (produção, coberto pelo veto acima; e `qwen-vl-plus` a $0.26/1M não justifica assinatura) + uso de código quase zero (ZCode já coberto por Kimi K3 e Z.ai/GLM). **Mantém tudo pay-as-you-go.** Revisitar Lite ($6) apenas se virar usuário pesado de Qwen pessoal no ZCode. **ADENDO 07/08 ~02:00 (Miguel VIROU usuário pesado de código — app em construção):** assinou o **LITE** pra código no ZCode, chave separada da pay-as-you-go do vision. **Endpoint internacional do Token Plan descoberto e testado 200:** `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` (o Beijing do alerta vale pra versão China). **Modelos incluídos no plano (lista viva 07/08):** `qwen3.8-max`, `qwen3.7-max`, `qwen3.7-plus`, `qwen3.6-flash`, `glm-5.2`, `deepseek-v4-pro`, `deepseek-v4-flash-0731`, `wan2.7-image(-pro)`, áudios — **SEM modelos de visão (qwen-vl-\*)** → vision continua pay-as-you-go, divisão confirmada. Chave da assinatura no cofre como `QWEN_TOKEN_PLAN_KEY` (sha8 `97352a86`) + provider "Qwen Code (Token Plan)" no ZCode. Espelhamento da chave nos servidores: PENDENTE.

> 🆓 **FREE QUOTA ALIBABA — ROTAÇÃO 09/08/2026 (Tema Duplo `forum_/memoria_rotacao_free_quota_alibaba_20260809`):** a conta **aiatolahnews@gmail.com** (chave canônica `85ecbfc0`, Default Workspace `ws-x4x2zxwucryw1pr6` — a mesma do pipeline) tem **87 modelos com free quota cheia, válida até 2026-09-15** (1M tokens por modelo; compartilha entre workspaces de Singapore; Stop-on-Exhaust desligado = além da cota cobra pay-as-you-go). `qwen-vl-plus` **ESGOTOU** 09/08; `qwen-vl-max` 95% usado. **Regra:** priorizar os modelos com cota (qwen3-vl-32b-thinking / qwen3-vl-235b-a22b-thinking na visão; qwen3-max/qwen-max/qwen-plus na cascata já debitam da cota automaticamente). Thinking-models novos (qwen3.5-*) inflam tokens — uso pontual. ⚠️ Neste workspace usar **nome exato de modelo**: alias `-latest` dá 403 (`qwen-vl-max-latest` morto 09/08; `qwen-vl-max` 200). Sem API pública de quota — painel do console.

### qwen3-vl-32b-thinking (Vision, FREE QUOTA)
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen3-vl-32b-thinking` |
| **Tipo** | Visão + Reasoning |
| **Preço** | **GRÁTIS até 2026-09-15** (free quota 1M, conta aiatolahnews) |
| **Reasoning** | Sim (~148 tokens reasoning em smoke) |
| **Status Cafezinho** | 🌟 VISION PRIMÁRIO GRÁTIS pós-esgotamento vl-plus (09/08). Testado AO VIVO: 200 "vermelho" 2.9s |
| **Verificado em** | 2026-08-09 |

### qwen3-vl-235b-a22b-thinking (Vision, FREE QUOTA)
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen3-vl-235b-a22b-thinking` |
| **Tipo** | Visão + Reasoning (235B MoE) |
| **Preço** | **GRÁTIS até 2026-09-15** (free quota 1M) |
| **Reasoning** | Sim (~130 tokens em smoke) |
| **Status Cafezinho** | Vision fallback grátis (qualidade maior). Testado AO VIVO 09/08: 200 3.8s |
| **Verificado em** | 2026-08-09 |

### qwen-vl-ocr-2025-11-20 (Vision OCR, FREE QUOTA)
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen-vl-ocr-2025-11-20` |
| **Tipo** | Visão especializada em OCR |
| **Preço** | **GRÁTIS até 2026-09-15** (free quota 1M) |
| **Status Cafezinho** | Disponível p/ extração de texto de imagens. Testado AO VIVO 09/08: 200 |
| **Verificado em** | 2026-08-09 |

### qwen3.5-plus-2026-02-15 / qwen3.5-122b-a10b / qwen3-235b-a22b-thinking-2507 (FREE QUOTA)
| Campo | Valor |
|-------|-------|
| **Preço** | **GRÁTIS até 2026-09-15** (1M cada) |
| **Reasoning** | **SIM** (out=203/176/98 tokens p/ "OK" — inflação) |
| **Status Cafezinho** | Fora da cascata de massa (inflação queima cota + latência). Uso pontual/analítico. Testados AO VIVO 09/08: todos 200 |
| **Verificado em** | 2026-08-09 |

### qwen-plus-2025-07-28 / qwen-mt-flash (FREE QUOTA)
| Campo | Valor |
|-------|-------|
| **Preço** | **GRÁTIS até 2026-09-15** (1M cada) |
| **Status Cafezinho** | `qwen-plus-2025-07-28` = snapshot datado do plus (pool de cota próprio); `qwen-mt-flash` = tradução MT. Testados AO VIVO 09/08: 200 |
| **Verificado em** | 2026-08-09 |

### qwen3.8-max
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen3.8-max` |
| **Tipo** | Texto + Reasoning (retorna `reasoning_content`) |
| **Contexto** | a medir (cadastrado 200K no ZCode) |
| **Tool-calling** | ✅ testado 07/08 (`finish_reason=tool_calls`, formato function-call OK) |
| **Streaming SSE** | ✅ testado 07/08 |
| **Status Cafezinho** | Novo topo Qwen — disponível no workspace MaaS Singapore. **Testes de código 07/08:** bug-hunt Python 2/2 bugs corretos (155s, 6.237 tokens de reasoning p/ input de 132!) + merge de intervalos 4/4 casos executados (11s) + tool-calling OK. **Qualidade de código: FORTE. Latência: variável (11-155s). Reasoning = tokens de output = caro no pay-as-you-go** — uso pesado de agente justifica Token Plan como teto de custo (só código, chave separada; ver decisão 07/08 no ATUALIZACOES) |
| **Nota** | `qwen-max-latest` **NÃO existe** no workspace (403) — não usar esse ID; chave canônica também funciona no endpoint público `dashscope-intl` (fallback) |
| **Verificado em** | 2026-08-07 (`Foruns/forum_qwen38_max_zcode_20260807.md`) |

### qwen3-max
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen3-max` |
| **Tipo** | Texto |
| **Contexto** | 262K tokens |
| **Preço Input** | $0.78 / 1M tokens |
| **Preço Output** | $3.90 / 1M tokens |
| **Cache hit** | $0.156 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | **Q5** P4 V3 |
| **Status Cafezinho** | Ativo — auditoria (3ª voz), cascata redação |
| **Tempo teste** | 5.6s |
| **Teste-trava §66.6** | ✅ PASSOU — recusou gerar fake news sobre Lula |
| **Pontos fortes** | Boa qualidade, open-weight, obedece guardrails |
| **Pontos fracos** | Censura em temas China-sensitive (feature editorial pro Cafezinho!) |
| **Verificado em** | 2026-05-25 |

### qwen3.7-max
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen3.7-max` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 1M tokens |
| **Preço Input** | $2.50 / 1M tokens |
| **Reasoning** | **SIM** — 2227 tokens reasoning para output de 95! |
| **Notas Q/P/V** | Q4 P2 V1 |
| **Status Cafezinho** | NÃO USAR — reasoning catastrófico para pipeline |
| **Tempo teste** | 34.5s |
| **Lançamento** | 20/05/2026 |
| **Verificado em** | 2026-05-25 |

### qwen-max
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen-max` |
| **Tipo** | Texto |
| **Contexto** | 32K tokens |
| **Preço Input** | $1.04 / 1M tokens |
| **Preço Output** | $4.16 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q4 P3 V4 |
| **Status Cafezinho** | Ativo — auditoria cascata |
| **Tempo teste** | 4.5s |
| **Verificado em** | 2026-05-25 |

### qwen-plus
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen-plus` |
| **Tipo** | Texto |
| **Contexto** | 1M tokens |
| **Preço Input** | $0.26-0.40 / 1M tokens |
| **Preço Output** | $0.78-1.20 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q2 P5 V4 |
| **Status Cafezinho** | Ativo — periféricos simples |
| **Verificado em** | 2026-05-25 |

### qwen-vl-plus (Vision)
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen-vl-plus` |
| **Tipo** | Visão + Texto |
| **Preço Input** | ~$0.26 / 1M tokens |
| **Preço Output** | ~$0.78 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P5 V5 |
| **Status Cafezinho** | ⚠️ **FREE QUOTA ESGOTADA 09/08/2026** (conta aiatolahnews) — segue respondendo (stop-on-exhaust off) mas agora **PAGO** (~$0,26/1M in). Migrado para `qwen3-vl-32b-thinking` (grátis até 09-15) como primário; vl-plus vira último recurso |
| **Tempo teste** | 1.2s (re-testado 09/08: 1.6s 200 "Vermelho.") |
| **Pontos fortes** | Ultra-barato para vision, rápido |
| **Verificado em** | 2026-05-25 (revisado 2026-08-09) |

### qwen-vl-max-latest (Vision) — ⚠️ ALIAS MORTO, usar `qwen-vl-max`
| Campo | Valor |
|-------|-------|
| **Model ID** | `qwen-vl-max-latest` |
| **Tipo** | Visão + Texto |
| **Preço Input** | $1.50 / 1M tokens |
| **Preço Output** | $4.50 / 1M tokens |
| **Notas Q/P/V** | Q4 P3 V3 |
| **Status Cafezinho** | 🔴 **BLOQUEADO 09/08/2026 — HTTP 403 "Access denied"** ao vivo no workspace `ws-x4x2zxwucryw1pr6`. O nome exato **`qwen-vl-max`** responde 200 (testado 09/08, free quota ~45k restantes). `llm_ratings.json` corrigido 09/08 |
| **Tempo teste** | 1.4s (`qwen-vl-max` exato: 1.3s em 09/08) |
| **Verificado em** | 2026-05-25 (revisado 2026-08-09) |

---

## 7. Zhipu (GLM)

**País:** China | **Fundação:** 2019 (Tsinghua) | **Site:** zhipuai.cn | **API:** open.bigmodel.cn

### glm-4-plus
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-4-plus` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | ~$0.69 / 1M tokens (5 RMB/M unificado) |
| **Preço Output** | ~$0.69 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P4 V4 |
| **Status Cafezinho** | Ativo com cautela — ÚNICO non-reasoning ativo na Zhipu |
| **Tempo teste** | 3.7s |
| **Bugs** | BUG-20260518-GLM-4-PLUS-ALUCINA + BUG-20260525-GLM-4-PLUS-FALHOU-TESTE-66-6 |
| **Pontos fortes** | Barato, rápido, preço unificado in/out |
| **Pontos fracos** | Alucina com travas explícitas — gerou fake news completa no teste §66.6 |
| **Verificado em** | 2026-05-25 |

### glm-5.2
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-5.2` |
| **Tipo** | Texto (+ Reasoning — padrão Zhipu 2026) |
| **Status Cafezinho** | ⏳ Não testado em inferência — existe na API mas exige saldo/pacote (erro 1113) |
| **Notas** | Avistado em `GET /paas/v4/models` em 2026-07-25 junto com `glm-5` e `glm-5-turbo` (também novos, não catalogados). Catálogo parava no glm-5.1. Preço/contexto a medir quando houver saldo. |
| **Verificado em** | 2026-07-25 (Kimi K3 — chave nova Miguel `sha8=bf908cec` + chave cofre: ambas autenticam, ambas sem saldo) |

### glm-5.1
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-5.1` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 203K tokens |
| **Preço Input** | $1.40 / 1M tokens |
| **Preço Output** | $4.40 / 1M tokens |
| **Reasoning** | **SIM** — 1036 tokens reasoning para output de 154 |
| **Notas Q/P/V** | Q4 P2 V1 |
| **Status Cafezinho** | Bloqueado — reasoning impraticável para pipeline |
| **Tempo teste** | 38.4s |
| **Parâmetros** | 744B MoE, MIT license |
| **Lançamento** | Abr 2026 |
| **Verificado em** | 2026-05-25 |

### glm-4.7
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-4.7` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.28-0.56 / 1M tokens (tiers por output) |
| **Preço Output** | $1.12-2.24 / 1M tokens (tiers por output) |
| **Reasoning** | **SIM** — 902 tokens reasoning para 18 tokens output (ratio 50:1) |
| **Notas Q/P/V** | Q4 P4 V1 |
| **Status Cafezinho** | Bloqueado — reasoning escondido, custo real 50x maior |
| **Tempo teste** | 12.1s |
| **Verificado em** | 2026-05-25 |

### glm-4.7-flash
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-4.7-flash` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | **GRÁTIS** |
| **Preço Output** | **GRÁTIS** |
| **Reasoning** | **SIM** — 100% tokens = reasoning, content sempre vazio |
| **Notas Q/P/V** | Q? P5 V2 |
| **Status Cafezinho** | Bloqueado — grátis mas inútil (content vazio) |
| **Tempo teste** | 4.7s |
| **Verificado em** | 2026-05-25 |

### glm-4.5-air
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-4.5-air` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.11-0.17 / 1M tokens |
| **Preço Output** | $0.28-1.12 / 1M tokens |
| **Reasoning** | **SIM** — 100% tokens = reasoning, content vazio |
| **Notas Q/P/V** | Q? P5 V3 |
| **Status Cafezinho** | Bloqueado — reasoning escondido |
| **Tempo teste** | 3.8s |
| **Verificado em** | 2026-05-25 |

### glm-4.6v-flash (Vision)
| Campo | Valor |
|-------|-------|
| **Model ID** | `glm-4.6v-flash` |
| **Tipo** | Visão |
| **Contexto** | 128K tokens |
| **Preço Input** | **GRÁTIS** |
| **Preço Output** | **GRÁTIS** |
| **Reasoning** | **SIM** — 99% reasoning em CHINÊS mesmo com prompt em português |
| **Notas Q/P/V** | Q? P5 V3 |
| **Status Cafezinho** | Bloqueado — vision gratuito mas reasoning em chinês, content vazio |
| **Tempo teste** | 6.3s |
| **Verificado em** | 2026-05-25 |

> **⚠️ ALERTA ZHIPU:** Todos os modelos lançados em 2026 são reasoning (inclusive os marcados como "non-reasoning" na documentação). Apenas `glm-4-plus` (2024) permanece non-reasoning. Modelos descontinuados (erro 1211): `glm-4-air`, `glm-4-airx`, `glm-4-flashx`, `glm-4-long`, `glm-4-assistant`.

---

## 8. Moonshot / Kimi Platform

**País:** China | **Fundação:** 2023 | **Site:** platform.kimi.ai | **API:** api.moonshot.ai

> 🟢 **Chave pay-as-you-go para AGENTES:** `KIMI_PAYGO_API_KEY` em `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env`. Esta chave deve ser usada por agentes de produção com crédito controlado. A chave de assinatura (`KIMI_CODE_API_KEY`) é para uso pessoal do Miguel no Kimi CLI.

### Classificação por categoria

| Categoria | Modelo | Input | Output | Latência | Contexto | Uso |
|-----------|--------|-------|--------|----------|----------|-----|
| 🌟 **SUPER LUXO** | `kimi-k3` | $3.00 | $15.00 | 3.0-3.7s | 1M | Pesquisa profunda, dossiês |
| 🌟 **SUPER LUXO econômico** | `k3-256k` | — | — | — | 256K | Mesmo K3 c/ contexto limitado a 256K — **gasta menos quota da assinatura** (descoberto 22/08 via /models da api.kimi.com/coding). Usar no dia a dia; k3 1M só p/ dossiês gigantes. |
| 💎 **LUXO** | `kimi-k2.6` | $0.95 | $4.00 | 1.3-1.5s | 256K | Redação premium, reasoning |
| 💎 **LUXO** | `kimi-k2.7-code` | $0.95 | $4.00 | 4.0-7.7s | 256K | Código, agentes. ⚠️ thinking pesado |
| ⚡ **MÉDIO** | `kimi-k2.5` | $0.60 | $3.00 | 0.9-1.8s | 256K | Melhor custo-benefício |
| ⚡ **MÉDIO** | `kimi-k2.7-code-highspeed` | $1.90 | $8.00 | 1.1-2.5s | 256K | Rápido, surpreendeu no editorial |
| 💰 **ECONÔMICO** | `moonshot-v1-8k` | $0.20 | $2.00 | 1.6-5.8s | 8K | Tarefas curtas. ⚠️ latência instável |
| 💰 **ECONÔMICO** | `moonshot-v1-32k` | $1.00 | $3.00 | 0.7-1.9s | 32K | Revisão, sumarização |
| 📚 **LONGO** | `moonshot-v1-128k` | $2.00 | $5.00 | 1.3-1.9s | 128K | Documentos longos, RAG |
| 🎯 **AUTO** | `moonshot-v1-auto` | — | — | ~0.7s | 128K | Auto-seleção 8k/32k/128k |
| 👁️ **VISÃO** | `moonshot-v1-8k-vision-preview` | $0.20 | $2.00 | ~1.6s | 8K | Imagens. ⚠️ vazamento chinês |
| 👁️ **VISÃO** | `moonshot-v1-32k-vision-preview` | $1.00 | $3.00 | ~1.5s | 32K | Imagens + texto |
| 👁️ **VISÃO** | `moonshot-v1-128k-vision-preview` | $2.00 | $5.00 | ~1.5s | 128K | Imagens + documentos |

*Preços em USD por 1M tokens. Cache hit reduz input em ~80-90%. Fonte: platform.kimi.ai/docs/pricing (jul/2026).*

> ⚠️ **Content filter:** modelos Moonshot tradicionalmente bloqueiam política brasileira (Bolsonaro etc). K3/K2.x podem ter filtro diferente — testar antes de usar em pauta política.

### 🌟 SUPER LUXO

### kimi-k3

| Campo | Valor |
|-------|-------|
| **Model ID** | `kimi-k3` |
| **Tipo** | Texto + Reasoning (always_thinking) |
| **Contexto** | 1M tokens (1,048,576) |
| **Input (cache hit)** | $0.30 / 1M |
| **Input (cache miss)** | $3.00 / 1M |
| **Output** | $15.00 / 1M |
| **Reasoning** | Sim — obrigatório, `reasoning_effort: "max"` |
| **Capabilities** | image_in, video_in, tool_use, dynamic_tools, tool_choice, JSON mode |
| **Notas Q/P/V** | Q5 P2 V3 — qualidade excepcional, caríssimo no output |
| **Status Cafezinho** | SUPER LUXO — pesquisas profundas, dossiês, análises complexas. NÃO usar para tarefas rotineiras |
| **Teste 17/07** | 3.0-3.7s (thinking disabled). Editorial: "Conflito armado (1864-1870) onde a Tríplice Aliança derrotou o Paraguai, causando enorme d..." — mais nuance histórica que K2.6. 59 tok output com thinking off. |
| **Verificado em** | 2026-07-17 |

> ⚠️ **Cuidado com output:** $15/1M é 3.75× mais caro que kimi-k2.6. Uma resposta de 4K tokens custa ~$0.06. Usar `max_tokens` controlado e `thinking: {type: "disabled"}` para tarefas sem reasoning.

### 💎 LUXO

### kimi-k2.6

| Campo | Valor |
|-------|-------|
| **Model ID** | `kimi-k2.6` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 256K tokens |
| **Input (cache hit)** | $0.16 / 1M |
| **Input (cache miss)** | $0.95 / 1M |
| **Output** | $4.00 / 1M |
| **Reasoning** | Sim (opcional) |
| **Notas Q/P/V** | Q4 P3 V2 |
| **Status Cafezinho** | LUXO — redação de alta qualidade, revisão, análise. Fallback do K3 |
| **Teste 17/07** | 1.3-1.5s (thinking disabled). Editorial: "A Guerra do Paraguai (1864-1870) foi o maior conflito armado da América do Sul, travado entre o Paraguai e a Tríplice Alia..." — preciso, informativo. 53 tok. |
| **Verificado em** | 2026-05-25 (preços atualizados 2026-07-17) |

### kimi-k2.7-code

| Campo | Valor |
|-------|-------|
| **Model ID** | `kimi-k2.7-code` |
| **Tipo** | Texto + Reasoning (coding-focused, thinking OBRIGATÓRIO) |
| **Contexto** | 256K tokens |
| **Input (cache hit)** | $0.19 / 1M |
| **Input (cache miss)** | $0.95 / 1M |
| **Output** | $4.00 / 1M |
| **Reasoning** | Sim — **não desligável**. Thinking consome ~800 chars em pergunta simples |
| **Notas Q/P/V** | Q4 P2 V2 |
| **Status Cafezinho** | LUXO — código e agentes técnicos. ⚠️ requer `max_tokens` ≥ 300; metade vai pro thinking |
| **Teste 17/07** | Editorial: 7.7s (thinking: 794c), resposta "Foi um conflito de 1864 a 1870 entre o Paraguai e a Tríplice Aliança..." — boa mas sem diferencial vs K2.6. Código: 4.0s, `def inverter_string(s): return s[::-1]` — limpo e correto. |
| **Verificado em** | 2026-07-17 |

### ⚡ MÉDIO

### kimi-k2.5

| Campo | Valor |
|-------|-------|
| **Model ID** | `kimi-k2.5` |
| **Tipo** | Texto + Multimodal + Reasoning |
| **Contexto** | 256K tokens |
| **Input (cache hit)** | $0.10 / 1M |
| **Input (cache miss)** | $0.60 / 1M |
| **Output** | $3.00 / 1M |
| **Reasoning** | Sim (opcional) |
| **Notas Q/P/V** | Q3 P4 V2 |
| **Status Cafezinho** | MÉDIO — melhor custo-benefício da linha K. Tarefas multimodais |
| **Teste 17/07** | 0.9-1.8s (thinking disabled). Editorial: "A Guerra do Paraguai (1864-1870) foi o maior conflito armado da América do Sul, entre Paraguai e a Tríplice Aliança (Bra..." — qualidade igual ao K2.6, mais barato. 50 tok. ⭐ Recomendado para editorial rotineiro. |
| **Verificado em** | 2026-07-17 |

### kimi-k2.7-code-highspeed

| Campo | Valor |
|-------|-------|
| **Model ID** | `kimi-k2.7-code-highspeed` |
| **Tipo** | Texto + Reasoning (rápido, thinking OBRIGATÓRIO) |
| **Contexto** | 256K tokens |
| **Input (cache hit)** | $0.38 / 1M |
| **Input (cache miss)** | $1.90 / 1M |
| **Output** | $8.00 / 1M |
| **Reasoning** | Sim — **não desligável**. Thinking consome ~800 chars |
| **Velocidade** | ~180 tok/s (até 260 em contexto curto) |
| **Notas Q/P/V** | Q3 P3 V4 |
| **Status Cafezinho** | MÉDIO — surpreendeu no editorial. Resposta mais completa que K2.7-code: "Conflito de 1864 a 1870 entre Paraguai e a Tríplice Aliança (Brasil, Argentina e Uruguai), que devastou o Paraguai." ⚠️ requer `max_tokens` ≥ 300 |
| **Teste 17/07** | Editorial: 1.9s (thinking: 804c). Código: 1.3s, limpo. Melhor que K2.7-code normal para editorial — adicionou "devastou o Paraguai" como nuance. |
| **Verificado em** | 2026-07-17 |

### 💰 ECONÔMICO

### moonshot-v1-8k

| Campo | Valor |
|-------|-------|
| **Model ID** | `moonshot-v1-8k` |
| **Tipo** | Texto |
| **Contexto** | 8K tokens |
| **Input** | $0.20 / 1M |
| **Output** | $2.00 / 1M |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q2 P5 V3 |
| **Status Cafezinho** | ECONÔMICO — classificação, tarefas curtas, periféricos |
| **Teste 17/07** | 1.6-5.8s. ⚠️ Latência instável (5.8s no editorial). Saída idêntica aos outros V1. Barato mas não confiável em velocidade. |
| **Verificado em** | 2026-05-25 (preços atualizados 2026-07-17) |

### moonshot-v1-32k

| Campo | Valor |
|-------|-------|
| **Model ID** | `moonshot-v1-32k` |
| **Tipo** | Texto |
| **Contexto** | 32K tokens |
| **Input** | $1.00 / 1M |
| **Output** | $3.00 / 1M |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P3 V2 |
| **Status Cafezinho** | ECONÔMICO — sumarização, revisão leve |
| **Teste 17/07** | 0.7-1.9s. Mais rápido e consistente que V1-8k. Melhor escolha V1 para tarefas rotineiras. |
| **Verificado em** | 2026-05-25 (preços atualizados 2026-07-17) |

### 📚 LONGO

### moonshot-v1-128k

| Campo | Valor |
|-------|-------|
| **Model ID** | `moonshot-v1-128k` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Input** | $2.00 / 1M |
| **Output** | $5.00 / 1M |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P2 V2 |
| **Status Cafezinho** | LONGO — documentos extensos, RAG, transcrições |
| **Teste 17/07** | 1.3-1.9s. Saída idêntica ao V1-32k no teste curto (esperado — mesma família). |
| **Verificado em** | 2026-05-25 (preços atualizados 2026-07-17) |

### 👁️ VISÃO

### moonshot-v1-*-vision-preview

| Modelo | Input | Output | Contexto | Nota |
|--------|-------|--------|----------|------|
| `moonshot-v1-8k-vision-preview` | $0.20 | $2.00 | 8K | ⚠️ Vazamento chinês ("三国联盟") |
| `moonshot-v1-32k-vision-preview` | $1.00 | $3.00 | 32K | ✅ Limpo |
| `moonshot-v1-128k-vision-preview` | $2.00 | $5.00 | 128K | ✅ "Tripartite Aliança" (estranho) |

**Teste 17/07:** ~1.5s cada. Apenas texto testado (sem imagem). V1-8k-vision teve vazamento de chinês no output — **evitar para produção editorial em português**. V1-32k-vision limpo.
**Status Cafezinho:** Preview — testar antes de usar em produção. Alternativa gratuita: Qwen VL.

### K3 via Assinatura (Kimi Code)

Para uso pessoal do Miguel no Kimi CLI. Ver `CEREBRO_NODE_COFRE_CHAVES.md` — `KIMI_CODE_API_KEY`.

| Campo | Valor |
|-------|-------|
| **Endpoint** | `https://api.kimi.com/coding/v1` |
| **Model ID** | `k3` |
| **Custo** | Incluso na assinatura Allegretto |
| **Contexto** | 1M tokens |

---

## 9. xAI (Grok)

**País:** EUA | **Fundação:** 2023 (Elon Musk) | **Site:** x.ai | **API:** api.x.ai

> ⚠️ **STATUS CAFEZINHO ATUAL: OFF TEMPORÁRIO desde 17/08/2026 ~15:22 BRT** (Miguel: "o grok perdeu credito, só volta em alguns dias"). MIGUEL-GROK e LAURA-GROK pausados; ponte de imagens Grok/caçadora suspensa. **Redistribuição das funções ex-Grok:** fallback ZCode→Codex; caçadora imagens→ZCode (Kimi K3 Vision) + Claude (Wikimedia CC via WebSearch); monitor de padrões→ZCode+Codex compartilham. Reserva/ticket Grok >2h = abandonado até restauração. Detalhes: `memory/project_cadencias_trindade_20260817.md` (memória Claude) + Emenda 2 do Contrato Geral (fórum `Foruns/forum_contrato_geral_ecossistema_20260816.md`).

### grok-3
| Campo | Valor |
|-------|-------|
| **Model ID** | `grok-3` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 131K tokens |
| **Preço Input** | $2.00 / 1M tokens |
| **Preço Output** | $10.00 / 1M tokens |
| **Reasoning** | **SIM** — 632 tokens reasoning no teste |
| **Notas Q/P/V** | Q4 P2 V2 |
| **Status Cafezinho** | Ativo — fallback, fact-check Grok |
| **Tempo teste** | 8.7s |
| **Verificado em** | 2026-05-25 |

### grok-4.3
| Campo | Valor |
|-------|-------|
| **Model ID** | `grok-4.3` |
| **Tipo** | Texto + Reasoning |
| **Contexto** | 2M tokens |
| **Preço Input** | Pendente — verificar console xAI |
| **Preço Output** | Pendente — verificar console xAI |
| **Reasoning** | Sim (modelo geral mais inteligente da família) |
| **Notas Q/P/V** | Q4 P? V? |
| **Status Cafezinho** | Pendente validação — preços dinâmicos no site |
| **Verificado em** | 2026-05-25 |

### grok-4.1-fast
| Campo | Valor |
|-------|-------|
| **Model ID** | `grok-4-1-fast-non-reasoning` |
| **Tipo** | Texto |
| **Contexto** | 2M tokens |
| **Preço Input** | $0.20 / 1M tokens |
| **Preço Output** | $0.50 / 1M tokens |
| **Cached** | $0.05 / 1M input |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P5 V5 |
| **Status Cafezinho** | Não testado — candidato econômico |
| **Verificado em** | 2026-05-25 |

---

## 10. Mistral

**País:** França | **Fundação:** 2023 | **Site:** mistral.ai | **API:** api.mistral.ai

### mistral-large-latest
| Campo | Valor |
|-------|-------|
| **Model ID** | `mistral-large-latest` (Large 3) |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.50 / 1M tokens |
| **Preço Output** | $1.50 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P4 V3 |
| **Status Cafezinho** | Ativo — fallback europeu na cascata |
| **Tempo teste** | 5.6s |
| **Pontos fortes** | Europeu (GDPR), preço caiu drasticamente (Large 2 era $2/$6) |
| **Verificado em** | 2026-05-25 |

### mistral-small-latest
| Campo | Valor |
|-------|-------|
| **Model ID** | `mistral-small-latest` (Small 4) |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.15 / 1M tokens |
| **Preço Output** | $0.60 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P5 V4 |
| **Status Cafezinho** | Não ativo — candidato econômico |
| **Verificado em** | 2026-05-25 |

---

## 11. Meta (Llama via Groq)

**País:** EUA (Meta) + EUA (Groq inferência) | **API:** api.groq.com

### llama-3.3-70b-versatile
| Campo | Valor |
|-------|-------|
| **Model ID** | `llama-3.3-70b-versatile` |
| **Tipo** | Texto |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.59 / 1M tokens |
| **Preço Output** | $0.79 / 1M tokens |
| **Free tier** | Sim |
| **Reasoning** | Não |
| **Velocidade inferência** | ~276 tok/s (Groq LPU) |
| **Notas Q/P/V** | Q3 P4 V5 |
| **Status Cafezinho** | Ativo — periféricos, mais rápido disponível |
| **Tempo teste** | **0.8s** (o mais rápido de todos) |
| **Pontos fortes** | Ultra-rápido (hardware Groq), open-source |
| **Pontos fracos** | Qualidade inferior para editorial |
| **Verificado em** | 2026-05-25 |

---

## 12. Perplexity (Sonar)

**País:** EUA | **Site:** perplexity.ai | **API:** api.perplexity.ai

### sonar-reasoning-pro
| Campo | Valor |
|-------|-------|
| **Model ID** | `sonar-reasoning-pro` |
| **Tipo** | RAG (busca + reasoning) |
| **Contexto** | 128K tokens |
| **Preço Input** | $2.00 / 1M tokens |
| **Preço Output** | $8.00 / 1M tokens |
| **Taxa por request** | $5-14 / 1K requests (depende do contexto de busca) |
| **Reasoning** | Sim |
| **Notas Q/P/V** | Q4 P2 V2 |
| **Status Cafezinho** | FACT-CHECK PRIMÁRIO — obrigatório na pipeline |
| **Tempo teste** | 9.8s |
| **Pontos fortes** | Busca integrada, fontes citadas, ideal para fact-check |
| **Pontos fracos** | Caro, não serve para redação |
| **Verificado em** | 2026-05-25 |

### sonar-pro
| Campo | Valor |
|-------|-------|
| **Model ID** | `sonar-pro` |
| **Tipo** | RAG (busca) |
| **Contexto** | 128K tokens |
| **Preço Input** | $3.00 / 1M tokens |
| **Preço Output** | $15.00 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q4 P3 V3 |
| **Status Cafezinho** | ATIVO GLOBAL — Fact-checking primário (promovido em 2026-06-10 para evitar falsos vetos factuais do modelo base) |
| **Verificado em** | 2026-06-10 |

### sonar
| Campo | Valor |
|-------|-------|
| **Model ID** | `sonar` |
| **Tipo** | RAG (busca básica) |
| **Contexto** | 128K tokens |
| **Preço Input** | $0.25 / 1M tokens |
| **Preço Output** | $2.50 / 1M tokens |
| **Cached** | $0.0625 / 1M tokens |
| **Reasoning** | Não |
| **Notas Q/P/V** | Q3 P4 V4 |
| **Status Cafezinho** | DESATIVADO (removido em 2026-06-10 por ordem de Miguel por cometer erros temporais de cutoff; substituído pelo sonar-pro) |
| **Verificado em** | 2026-06-10 |

---

## 13. Geradores de Imagem

### Ideogram V2
| Campo | Valor |
|-------|-------|
| **Provider** | Ideogram |
| **Model ID** | `V_2` |
| **Estilo** | DESIGN |
| **Aspecto** | 16:9 |
| **Preço** | ~$0.04-0.08 / imagem |
| **Status Cafezinho** | PRIMÁRIO geração editorial |

### Flux Pro v1.1
| Campo | Valor |
|-------|-------|
| **Provider** | fal.ai |
| **Endpoints** | `fal.run/fal-ai/flux-pro/v1.1`, `fal.run/fal-ai/flux-pro` |
| **Preço** | ~$0.05 / imagem |
| **Status Cafezinho** | Fallback 1 — menos censura política |

### DALL-E 3
| Campo | Valor |
|-------|-------|
| **Provider** | OpenAI |
| **Model ID** | `dall-e-3` |
| **Preço** | ~$0.04-0.12 / imagem |
| **Status Cafezinho** | Fallback 2 |

---

## 14. Ranking Consolidado por Custo (Input cache miss, mais barato primeiro)

| # | Modelo | $/1M Input | Provider | Observação |
|---|--------|-----------|---------|------------|
| 1 | glm-4.7-flash | **$0.00** | Zhipu | Grátis mas inútil (100% reasoning) |
| 1 | glm-4.6v-flash | **$0.00** | Zhipu | Grátis mas inútil (vision reasoning chinês) |
| 2 | kimi-k2.5 | $0.10 (cache) | Kimi | Cache hit; $0.60 miss |
| 3 | deepseek-v4-flash | $0.14 | DeepSeek | Periféricos |
| 4 | deepseek-coder | $0.14 | DeepSeek | Código/Trindade |
| 5 | gpt-4o-mini | $0.15 | OpenAI | Periféricos |
| 6 | mistral-small-latest | $0.15 | Mistral | Periféricos |
| 7 | kimi-k2.6 | $0.16 (cache) | Kimi | Cache hit; $0.95 miss |
| 8 | kimi-k2.7-code | $0.19 (cache) | Kimi | Cache hit; $0.95 miss |
| 9 | grok-4.1-fast | $0.20 | xAI | Candidato econômico |
| 10 | moonshot-v1-8k | $0.20 | Kimi | ECONÔMICO (preço caiu de $0.50) |
| 11 | sonar | $0.25 | Perplexity | Fact-check básico |
| 12 | qwen-plus / qwen-vl-plus | $0.26 | Alibaba | Periféricos / Vision |
| 13 | deepseek-chat (V3) | $0.27 | DeepSeek | Legado até 24/07 |
| 14 | gemini-2.5-flash | $0.30 | Google | Periféricos / Vision |
| 15 | kimi-k3 | $0.30 (cache) | Kimi | Cache hit; $3.00 miss |
| 16 | kimi-k2.7-code-highspeed | $0.38 (cache) | Kimi | Cache hit; $1.90 miss |
| 17 | deepseek-v4-pro (promo) | $0.44 | DeepSeek | **PRIMÁRIO REDAÇÃO** |
| 18 | mistral-large-latest | $0.50 | Mistral | Fallback europeu |
| 19 | deepseek-reasoner (R1) | $0.55 | DeepSeek | Reasoning isolado |
| 20 | groq/llama-3.3-70b | $0.59 | Groq | Ultra-rápido |
| 21 | kimi-k2.5 | $0.60 | Kimi | Cache miss |
| 22 | glm-4-plus | $0.69 | Zhipu | Único non-reasoning Zhipu |
| 23 | qwen3-max | $0.78 | Alibaba | Redação fallback |
| 24 | kimi-k2.6 | $0.95 | Kimi | LUXO reasoning |
| 25 | kimi-k2.7-code | $0.95 | Kimi | LUXO coding |
| 26 | haiku-4-5 | $1.00 | Anthropic | Emergência financeira |
| 27 | gemini-2.5-pro | $1.00 | Google | Multimodal |
| 28 | moonshot-v1-32k | $1.00 | Kimi | ECONÔMICO (preço caiu de $1.50) |
| 29 | qwen-max | $1.04 | Alibaba | Cascata auditoria |
| 30 | gpt-5 | $1.25 | OpenAI | Bloqueado por política |
| 31 | glm-5.1 | $1.40 | Zhipu | Reasoning, bloqueado |
| 32 | deepseek-v4-pro (regular) | $1.74 | DeepSeek | Pós-promo 31/05 |
| 33 | kimi-k2.7-code-highspeed | $1.90 | Kimi | Cache miss; rápido |
| 34 | grok-3 | $2.00 | xAI | Fallback |
| 35 | perplexity sonar-reasoning | $2.00 | Perplexity | Fact-check primário |
| 36 | moonshot-v1-128k | $2.00 | Kimi | LONGO (preço subiu de $1.50) |
| 37 | gpt-4o | $2.50 | OpenAI | Fallback ocidental |
| 38 | qwen3.7-max | $2.50 | Alibaba | Reasoning, não usar |
| 39 | sonnet-4-6 | $3.00 | Anthropic | Sem saldo |
| 40 | kimi-k3 | $3.00 | Kimi | 🌟 SUPER LUXO (cache miss) |
| 41 | opus-4-7 | $5.00 | Anthropic | Bloqueado |

> 💡 **Output também importa.** K3 custa $15.00/1M output (3.75× o K2.6). Para tarefas com muito output, K2.6 ou K2.5 são melhores. Ver tabela completa na §8.

---

## 15. Ranking por Velocidade (teste editorial padronizado 17/07 para Kimi; 25/05 para demais)

| # | Modelo | Tempo | Provider | Observação |
|---|--------|-------|---------|------------|
| 1 | moonshot-v1-32k | **0.7s** | Kimi | 🆕 Teste 17/07 — básico (OK) |
| 2 | llama-3.3-70b (Groq) | **0.8s** | Groq | Ultra-rápido |
| 3 | kimi-k2.5 | 0.9s | Kimi | 🆕 Thinking disabled |
| 4 | moonshot-v1-auto | 1.0s | Kimi | 🆕 Auto-select |
| 5 | kimi-k2.7-code-highspeed | 1.1s | Kimi | 🆕 Básico; editorial: 1.9s |
| 6 | qwen-vl-plus | 1.2s | Alibaba | Vision OCR |
| 7 | kimi-k2.6 | 1.3s | Kimi | 🆕 Thinking disabled |
| 8 | moonshot-v1-128k | 1.3s | Kimi | 🆕 |
| 9 | qwen-vl-max-latest | 1.4s | Alibaba | Vision alta qualidade |
| 10 | deepseek-v4-pro | 2.2s | DeepSeek | Variável: 2.2-59s |
| 11 | gpt-4o-mini | 2.4s | OpenAI | Consistente |
| 12 | gpt-4o | 2.8s | OpenAI | Rápido e qualidade |
| 13 | kimi-k3 | 3.0s | Kimi | 🆕 Thinking disabled |
| 14 | kimi-k2.7-code | 3.3s | Kimi | 🆕 Thinking obrigatório |
| 15 | glm-4-plus | 3.7s | Zhipu | Único non-reasoning Zhipu |
| 16 | glm-4.5-air | 3.8s | Zhipu | ⚠️ 100% reasoning |
| 17 | qwen-max | 4.5s | Alibaba | Estável |
| 18 | glm-4.7-flash | 4.7s | Zhipu | ⚠️ Grátis mas inútil |
| 19 | qwen-plus | 5.4s | Alibaba | Periféricos |
| 20 | qwen3-max | 5.6s | Alibaba | Boa qualidade |
| 21 | mistral-large | 5.6s | Mistral | Europeu |
| 22 | gemini-2.5-flash | 5.7s | Google | Reasoning escondido |
| 23 | glm-4.6v-flash | 6.3s | Zhipu | ⚠️ Vision reasoning chinês |
| 24 | grok-3 | 8.7s | xAI | Reasoning visível |
| 25 | perplexity sonar | 9.8s | Perplexity | Fact-check |

> 🆕 Modelos Kimi testados em 17/07/2026 com prompt curto ("Responda APENAS com a palavra OK"). Modelos K com thinking desligado onde possível. K2.7-code tem thinking obrigatório. Modelos antigos (25/05) abaixo com reasoning ligado — latências muito maiores.
| 19 | glm-4.7 | 12.1s | Zhipu | ⚠️ Reasoning escondido, ratio 50:1 |
| 20 | kimi-k2.6 (c/ reasoning) | 13.0s | Moonshot | Reasoning, temp=1.0 obrigatório |
| 21 | qwen3.7-max | 34.5s | Alibaba | Reasoning catastrófico |
| 22 | glm-5.1 | 38.4s | Zhipu | Reasoning, MIT license |

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
| `qwen3.7-max` | 2227 (para output de 95) | 23x | Documentado como reasoning |
| `glm-5.1` | 1036 (para output de 154) | 7x | Documentado como reasoning |
| `gemini-2.5-flash` | 765 (para output de 31) | 25x | Thinking tokens no output |
| `grok-3` | 632 (para output de 100) | 7x | Documentado como reasoning |
| `kimi-k2.6` | 1356 chars (para output de 299) | ~5x | Temp=1.0 obrigatório |
| `gpt-5` | (não testado) | — | Reasoning model |

> **⚠️ DESCoberta crítica GLM Coding 25/05:** TODOS os modelos Zhipu lançados em 2026 são reasoning, **inclusive os que NÃO são documentados como tal** na página de pricing. Apenas `glm-4-plus` (2024) permanece non-reasoning.

**Regra Cafezinho:** reasoning models ficam FORA da cascata de redação/revisão/auditoria. Usar apenas para tarefas onde raciocínio profundo é necessário (auditoria complexa, análise de código).

---

*Catálogo atualizado em 2026-05-25 17:20 BRT (auditoria Kimi Code CLI integrando 5 pesquisas).*
*Fonte: pesquisas da Trindade (Codex, Qwen Coding, GLM Coding, DeepSeek Code, Kimi Code) + testes reais 25/05.*
*Fórum: `forum_pesquisa_precos_llms_20260525.md`*
