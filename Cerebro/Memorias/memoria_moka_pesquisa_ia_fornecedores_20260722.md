# 🧠 MEMÓRIA — Pesquisa de fornecedores de IA pra assinatura Moka + estratégia de investimento (2026-07-22)

> Pedido do Miguel: pesquisa ampla de IAs (leitura, transcrição Whisper, voz neural), custos, programas pra startups, custo de implementação e estratégia de investidor (crowdfunding / participação / modelo dos 200 sócios).
> Pesquisa web com fontes oficiais (2 agentes, 22/07/2026) + catálogo interno CEREBRO_NODE_CATALOGO_MODELOS_LLM.

## 1. LLM — escolhas por função (preços oficiais jul/2026)

| Função | Recomendado | Preço in/out por 1M | Por quê |
|---|---|---|---|
| **Volume (resumos, análises)** | **DeepSeek v4-flash** | $0,14 / $0,28 (cache $0,0028!) | Melhor custo absoluto, 1M de contexto (livro inteiro numa chamada) |
| Alternativa barata | **qwen-flash** (Alibaba) | $0,05 / $0,40 | Mais barato ainda; 1M tokens GRÁTIS por modelo/90 dias (conta intl.) |
| Qualidade editorial | **GLM-4.5-Air** (Z.ai) | $0,20 / $1,10 | Equilíbrio; GLM-4.5/4.7-Flash são **grátis** (limitações) |
| Premium | **claude-haiku-4-5** | $1,00 / $5,00 | Haiku p/ tier alto; Sonnet 5 ($2/$10 promo até 31/08) p/ Família |
| Grátis real | **gemini-2.5-flash-lite** | $0,10/$0,40 + free tier AI Studio | Rede de segurança de custo zero |

⚠️ `deepseek-chat`/`deepseek-reasoner` viram `deepseek-v4-flash` em 24/07/2026. Batch APIs (OpenAI/Anthropic/Google/Mistral) = **50% off** — usar pra volumes (tradução de livros).

## 2. Transcrição (o "Whisper" da assinatura)

| Modelo | Empresa | Preço/min | Nota |
|---|---|---|---|
| **whisper-large-v3-turbo** | **Groq** | **$0,0007** | 4-8x mais barato que OpenAI, rápido |
| whisper | **Cloudflare Workers AI** | **$0,0005** | O mais barato; ~10k neurônios/dia grátis |
| gpt-4o-mini-transcribe | OpenAI | $0,003 | (hoje usamos gpt-4o-transcribe $0,006) |
| gpt-4o-transcribe | OpenAI | $0,006 | Qualidade atual do app |

**Decisão técnica sugerida:** migrar transcrição pra Groq turbo (ou Cloudflare) com fallback OpenAI — mesma qualidade, custo cai ~85%.

## 3. Voz neural (TTS) — o item mais caro

| Serviço | Preço | pt-BR | Free tier |
|---|---|---|---|
| **Google Cloud TTS WaveNet** | **$4/1M chars** | Muito boa | **4M chars/mês GRÁTIS** (~6-8 livros!) |
| Google Neural2 / Chirp HD | $16 / $30 por 1M | Muito boa/excelente | 1M/mês |
| **Azure Speech (voz Francisca)** | $15/1M | **A mais natural (exceto ElevenLabs)** | 0,5M/mês |
| Amazon Polly Neural/Standard | $16 / $4 | Boa (Camila/Vitória/Thiago) | 1M/5M por 12 meses |
| ElevenLabs v3 | ~$165/1M efetivo | Referência absoluta | 10k/mês — inviável p/ livros inteiros |
| Kokoro-82M (self-hosted) | ~$0 (CPU) | Boa (3 vozes, Apache-2.0) | Total |
| Edge-TTS | Grátis | Muito boa (mesmas vozes Azure) | ⚠️ **NÃO usar em produto pago** (ToS, GPL, sem SLA) |

**Decisão sugerida:** Google TTS WaveNet como motor padrão (free tier generoso cobre o início), Neural2/Azure Francisca nos tiers altos. Resumo-em-áudio de vídeo (~10k chars) custa centavos — incluir em todos os tiers; livro inteiro falado fica pros tiers altos ou com cota.

## 4. Programas de créditos pra startups (aplicar JÁ)

| Programa | O que dá | Ação |
|---|---|---|
| **Microsoft for Startups** | Até **$150k Azure** (inclui Azure OpenAI) | Cadastro grátis, sem exigir funding |
| **Google for Startups Cloud** | $2k (MVP) → **$200-350k** (seed/AI-first) | Aplicar online |
| **AWS Activate** | Até $200k (vale Bedrock) | Aplicar |
| Claude for Startups | Créditos + rate limits altos | Exige funding institucional — fase 2 |
| Alibaba Model Studio | 1M tokens/modelo grátis (90 dias) | Já disponível |
| Cloudflare/Groq/Z.ai flash | free tiers permanentes | Já disponível |

**Com Google + Microsoft, o Moka roda 1-2 anos de IA quase de graça.**

## 5. Unit economics (assinante PESADO/mês: 30 vídeos + 5 livros)

- Transcrição 300 min (Groq turbo): **$0,21** (era $1,80 c/ OpenAI)
- LLM análises (deepseek-v4-flash): **$0,79**
- TTS resumos em áudio: ~$0,30 | TTS 1 livro inteiro (WaveNet): $2 (free tier cobre)
- Infra (Vercel/Supabase): ~$0,50
- **Custo total: ~US$ 2-4/mês (R$ 11-22)** → assinatura a R$ 29,90 = margem 85-90%+

## 6. Estratégia de investimento (pedido do Miguel)

### Custo pra colocar vendendo (MVP comercial)
- Já está no ar (Moka 2.0) — falta: gateway + cotas (~2 sprints), i18n, página premium
- Custo direto inicial: domínio (~R$40/ano ✅), Vercel/Supabase (free tiers servem no início), IA (~R$15/assinante pesado), gateway (Mercado Pago ~0,99-4,99% por transação; Paddle ~5%+$0,50)
- **Conclusão: dá pra lançar vendendo com quase zero capital** — o dinheiro de investimento é pra ESCALAR (marketing, time, app de loja, voz premium).

### ⚠️ Modelo dos "200 sócios" — ALERTA JURÍDICO IMPORTANTE
A ideia (200 primeiros clientes viram sócios, com acesso online ao nº de assinantes + **percentual de cada assinatura nova**) é forte como comunidade, MAS: **promessa de participação em receita/lucro a investidores = valor mobiliário** (Lei 6.385/76 + CVM). Vender isso direto ao público sem plataforma autorizada é **oferta irregular** (risco CVM).

Caminhos compliant:
1. **Equity crowdfunding regulamentado** (CVM instrução 88/2022): plataformas autorizadas (Kria, EqSeed, CapTable, StartMeUp…). Aí SIM pode vender participação com transparência de números. Ticket típico R$ 500-5.000 — dá pra captar R$ 100k-1M com 200 sócios.
2. **Pré-venda recompensa (NÃO é valor mobiliário):** "Sócio-Fundador" como MARKETING: os 200 primeiros compram 2 anos de assinatura + selo fundador + acesso ao painel de crescimento (sem % de receita). Pode fazer via Catarse/Benfeitoria ou direto (PIX).
3. **Revenue share contratual** (contrato de parceria de risco/mútuo conversível): com advogado, pra poucos investidores maiores (não varejo).

**Recomendação:** começar com (2) — pré-venda "Sócio-Fundador" (200 × R$ 299/ano = ~R$ 60k de verba inicial, zero risco CVM) — e preparar (1) se a tração vier. O painel público de assinantes (transparência) pode existir nas duas rotas e é um ótimo marketing de prova social.

### Reunião com investidor (one-pager mental)
- **O quê:** Moka — leia livros, veja vídeos em 1 minuto, com IA. 2 produtos lançados, 1 app (V 2.0).
- **Mágica da margem:** custo de IA R$ 11-22/assinante pesado → preço R$ 29,90-99,90 → margem >85%.
- **Tração:** 2 apps no ar, stack própria, fusão feita, motor local (IP do usuário — vantagem contra bloqueio do YouTube que concorrentes não têm).
- **Moat:** BYOK grátis (privacidade) + assinatura simples (sem chave) + i18n 12 idiomas + leitura via IP do usuário.
- **Uso do dinheiro:** marketing/aquisição, app de loja (Capacitor), voz premium, equipe enxuta.

— ZCode/Kimi, 2026-07-22 (fontes: páginas oficiais de pricing — ver relatórios completos nos agentes; catálogo LLM interno)
