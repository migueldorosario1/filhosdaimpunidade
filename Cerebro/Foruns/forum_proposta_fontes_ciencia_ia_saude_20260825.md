# 🔬 Fórum — Estudo e proposta de fontes: IA · Neurociência · Medicina na vertical Ciência (25/08/2026, ZCode/GLM-5.3)

**Ordem do Miguel:** mais posts de IA (lançamentos de modelos), neurociência (cérebro), doenças/medicina — SEM aumentar o ritmo geral ("está bom, não quero mudar"). · **Estado: PROPOSTA — nada aplicado.**

## 1. O que a vertical ciência lê hoje (editoria "tecnologia" do `config_editorial.py`, NYC)

**RSS (13):** The Verge · Nikkei Asia · Global Times · Tecnoblog · Canaltech · Revista Pesquisa FAPESP · Rest of World · The Register · **Nature** · **Science** · Pandaily · TechNode · China Daily.
**Queries Google News (7):** TODAS com foco China/tech — "China IA soberania", "guerra dos chips", "Qwen Kimi K3 DeepSeek nova IA chinesa", "BRICS tecnologia"…

## 2. Diagnóstico do gap (bate com o que o Miguel sente)
1. **Lançamentos de modelos IA**: só a query chinesa cobre; **zero cobertura de GPT/Gemini/Grok/Claude/Llama** e nenhum feed especializado em IA.
2. **Neurociência/cérebro**: **nenhuma fonte** dedicada.
3. **Medicina/doenças**: **nenhuma fonte** (Nature/Science são gerais — descobertas fortes passam, mas o fluxo diário de saúde não chega).
4. Viés Ásia/chips forte (5 de 13 feeds) — herança do desenho Global South; boa, mas desequilibrada pro apetite do leitor.

## 3. Proposta (mesma fábrica, mesma esteira, mesmo ritmo — só matéria-prima melhor)

**A. Novos feeds RSS (+8):**
| Tema | Feed |
|---|---|
| IA-lançamentos | `techcrunch.com/category/artificial-intelligence/feed` |
| IA-lançamentos | `arstechnica.com/ai/feed` |
| IA-lançamentos | `venturebeat.com/category/ai/feed` |
| IA-lançamentos (labs) | `blog.google/technology/ai/rss` + `openai.com/blog/rss.xml` |
| Neurociência | `neurosciencenews.com/feed` |
| Medicina/doenças | `news-medical.net/rss` · `medicalxpress.com/rss` |
| Ciência geral | `scitechdaily.com/feed` |

**B. Novas queries Google News (+6):** "novo modelo IA lançamento GPT Gemini Grok Claude" · "AI model release benchmark" · "cérebro descoberta neurociência estudo" · "Alzheimer Parkinson tratamento descoberta" · "vacina ensaio clínico resultado" · "cancer terapia descoberta".

**C. Ajuste técnico único:** `MAX_RSS_BIG` 12→20 (var de env do coletor — só abre espaço pros feeds novos; RSS é grátis, coleta 2×/h já dá conta).

**D. O que NÃO muda:** ritmo do ciclo V4.1 (2h) · freio por categoria (80) · gates de tese · slots da esteira · total diário de posts. O volume extra de pautas aumenta a ESCOLHA (melhor tese, menos "sem_pauta"), não o volume de matérias.

**E. Tradução:** fontes em inglês chegam cruas; o redator V4.1 já redige em PT a partir da pauta (como faz com Nikkei/Register hoje) — sem passo novo.

## 4. Efeito esperado
Bloco Tecnologia com mix: lançamentos de IA no dia (Grok/Gemini/GPT/Kimi), descobertas de cérebro e medicina com regularidade, mantida a coluna China/Global South. Volume de produção: igual (limitado pelos gates) — qualidade e variedade: maiores.

## 5. Estado / preciso do Miguel
- **Proposta pronta, nada aplicado.** Aprovação ("aplica") = config_editorial + env MAX_RSS_BIG no cron + prova na próxima coleta (feeds novos no log) — ~15 min, com backup.

## ✅ ADENDO 1 (25/08 ~14:00) — APLICADO com calibração do mix (ordem Miguel "vamos fazer uma alteração, calibrar")
- **Fontes aplicadas** (config_editorial NYC, backup `.bak_fontes_20260825`): tecnologia 16→**27 feeds** (+11 validadas 200: SCMP Tech · 机器之心 jiqizhixin · 36kr · TechCrunch AI · Ars AI · VentureBeat AI · Google AI · OpenAI news · Neuroscience News · SciTechDaily · Maglev.net) e 7→**16 queries** (+lançamentos IA ocidente/china · chips · cérebro/neuro · Alzheimer/Parkinson · vacina/ensaio · câncer · trem alta velocidade/maglev · mobilidade urbana). Teto de feeds: `MAX_RSS_BIG_FEEDS=24` via /root/chaves.sh (todos os crons carregam).
- **Repetidor Estatal calibrado**: `THRESHOLD_PUBLICAVEL` 40→**60** ("tirar um pouco" — mais seletivo, menos matérias/rajada; auditor continua veto-only).
- **Ritmo geral intocado**: ciclo V4.1 2h, freio por categoria (80), gates, slots. Efeito = mix: menos estatal, pautas de IA-chinesa/ocidental, neuro, medicina e trens passando a ter de onde chegar.
- Rejeitadas na validação (404/403): news-medical, medicalxpress, railwaygazette, railway-technology — cobertura de saúde/trens fica com SciTechDaily + queries.
- **Prova:** py_compile + import real (27/16 contados no módulo carregado). Próxima coleta 2×/h já lê as novas — pautas de IA/chips/trens começam a fluir pros gates.
- Vigília §118 da ronda: V4.1 ainda 0 registro (gate de tese rigoroso); Opus: confirmação na próxima rajada com gasto. Kimi 🔴 esgotado (failover GLM; aviso padrão dado).
