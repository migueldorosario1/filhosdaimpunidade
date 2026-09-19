# 💎 Fórum — Moka Premium: ideia do plano pago com IA unificada (2026-07-22)

> Tema: modelo de negócio do Moka — plano **Premium** (assinatura) ao lado do modo grátis BYOK.
> Nodo (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.
> Memória técnica: `MEMORIA/memoria_moka_premium_20260722.md`.
> Status: **ideia em discussão** (nada implementado).

## A pergunta do Miguel

Miguel viu material sobre o **Vercel AI SDK** e perguntou se ele serviria para o Moka Reader e o Moka Video. A ideia que passou pela cabeça dele (voz→texto):

> "Ele unifica as APIs para vários LLMs… poderia servir para o **Moka Premium**: a gente unificava vários LLMs numa API só, e a pessoa que pagava podia usar vários LLMs com o preço de um só, usando uma API só."

## Resposta dada (resumo)

1. **Vercel AI SDK: não é a peça.** É só uma biblioteca de código (unifica chamadas, mas não paga conta nem segura chave). E o Moka **já tem** essa camada: `packages/ai-providers/` (Reader) e `src/lib/ai/` (Video) — multi-provedor OpenAI-compatible.
2. **A peça que realiza a ideia é um gateway tipo OpenRouter** — serviço que dá **uma chave → 100+ modelos** (GPT, Claude, Gemini, DeepSeek, GLM, Kimi…), com cobrança unificada por uso, painel de custos e limites por chave.
3. **A inversão-chave do Premium:** hoje (BYOK) a chave fica no navegador do usuário e a conta da IA é dele; no Premium, **uma chave OpenRouter do Cafézinho fica escondida no servidor** (env var da Vercel) e o usuário assina, faz login e usa sem configurar nada. O Miguel paga a conta por uso e embute no preço da assinatura.

## Por que o Premium faz sentido (decisões registradas)

- **Barreira do BYOK:** usuário comum não sabe gerar chave de API → desiste na configuração. Premium remove essa fricção.
- **Receita:** hoje o app é grátis e não gera renda; assinatura (ex.: R$ 19,90/mês) com custo real de US$ 1–3/usuário pesado → margem saudável.
- **Sinergia com a Tradução Integral em Volumes** (ideia aprovada 2026-07-21): traduzir livro inteiro com modelo barato (GLM/DeepSeek, centavos por volume) e reservar modelo caro para perguntas difíceis — roteamento por tarefa via OpenRouter.
- **Uma assinatura, dois produtos:** a mesma chave/infraestrutura server-side serve para o **Moka Video** no futuro (plano "Cafezinho" unificado).

## O que falta construir (quando a sprint for aberta)

1. Login (Supabase Auth — infra já existe).
2. Pagamento (Stripe internacional / Mercado Pago BR).
3. Rotas `/api/premium/*` com a chave OpenRouter em env var do servidor.
4. Cota de tokens por assinante (anti-abuso).
5. Manter o modo **Grátis (BYOK)** — os dois convivem.

## Decisões pendentes do Miguel

- Preço e tiers (Grátis BYOK / Premium / Cafezinho completo?).
- Stripe ou Mercado Pago (ou ambos).
- OpenRouter confirmado como gateway, ou avaliar alternativas (Together, Fireworks, chaves diretas por provedor).

— ZCode/Kimi, 2026-07-22
