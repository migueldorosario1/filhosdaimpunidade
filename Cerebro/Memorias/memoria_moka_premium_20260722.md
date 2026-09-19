# 🧠 MEMÓRIA — Moka Premium: arquitetura do plano pago com IA unificada (2026-07-22)

> Log técnico. Fórum resumido: `Foruns/forum_moka_premium_20260722.md`.
> Nodo (Camada 2): `CEREBRO_INDEX_MOKA_LOG.md`.
> Status: **ideia avaliada, nada implementado**. Origem: pergunta do Miguel sobre Vercel AI SDK.

## 1. Contexto

Miguel perguntou se o **Vercel AI SDK** serviria para o Moka Reader/Moka Video, imaginando: "unificar vários LLMs numa API só → assinante paga um preço e usa vários LLMs". Avaliação:

| Peça | O que é | Serve pro Moka Premium? |
|---|---|---|
| **Vercel AI SDK** | Biblioteca TS/JS de código aberto; unifica chamadas a 100+ modelos | ❌ Desnecessário — o Moka já tem `packages/ai-providers/` (Reader) e `src/lib/ai/` (Video), multi-provedor OpenAI-compatible. E o SDK não resolve pagamento/chave |
| **OpenRouter** (ou gateway similar) | Serviço: 1 chave → 100+ modelos, cobrança unificada por uso, painel de custos, limites por chave, fallback entre provedores | ✅ É a peça que realiza a ideia do Miguel |

## 2. Arquitetura proposta

### Hoje (BYOK, grátis) — não muda
```
navegador do usuário (chave AES-GCM no localStorage)
  → /api/proxy (allowlist anti-SSRF)
  → provedor de IA (conta do usuário)
```

### Premium (novo) — servidor segura a chave
```
usuário assinante (login Supabase Auth, sem chave)
  → /api/premium/* (rota server-side Nova)
     - verifica sessão + assinatura ativa + cota de tokens
     - chave OpenRouter em env var da Vercel (nunca no cliente)
  → OpenRouter (1 chave do Cafezinho → 100+ modelos)
```

### Roteamento por tarefa (economia)
| Tarefa | Modelo sugerido | Custo típico |
|---|---|---|
| Tradução integral de livros (volumes) | GLM / DeepSeek (baratos) | ~US$ 0,10–0,50/livro |
| Resumos, perguntas comuns | modelos médios | centavos |
| Perguntas difíceis / modelo escolhido pelo usuário | GPT/Claude/Gemini topo | sob demanda |

### Conta rápida
Assinatura ex. R$ 19,90/mês (~US$ 4) vs. custo US$ 1–3 de usuário pesado → margem saudável. Cota mensal de tokens por assinante protege contra abuso.

## 3. Reuso do que já existe

- `ai-providers`: OpenRouter **é** OpenAI-compatible → basta apontar base URL (`https://openrouter.ai/api/v1`) + modelo; zero reescrita da camada de IA.
- Supabase (auth + sync): base para login/assinatura.
- Proxies server-side com allowlist: padrão de segurança já estabelecido (mesmo padrão para a nova rota premium).
- Mesma infraestrutura serve depois para o **Moka Video** (`MokaVideo/`) → plano "Cafezinho" unificado.

## 4. O que falta construir (escopo da futura sprint)

1. **Auth obrigatório no modo Premium** — Supabase Auth (email/OAuth).
2. **Pagamento** — Stripe (internacional) e/ou Mercado Pago (BR); webhook → flag `premium` no perfil do usuário (Supabase).
3. **Rotas `/api/premium/*`** — quickExplain/translate/summarize/ask passando pelo servidor; chave em `OPENROUTER_API_KEY` (env Vercel, projeto `moka`).
4. **Cotas** — tabela de uso (user_id, mês, tokens); bloqueio/alerta ao estourar.
5. **UX** — tela de planos, seletor de modelo liberado para assinantes, selo "Premium".
6. **Regra permanente mantida:** backup zip datado em `Moka/backups/` ANTES de qualquer deploy (PROTOCOLO_SEGURANCA_BACKUP).

## 5. Decisões pendentes (aguardando Miguel)

- Preço/tiers; Stripe vs Mercado Pago; OpenRouter confirmado ou avaliar Together/Fireworks/chaves diretas.
- Nome do plano ("Moka Premium" foi a expressão usada pelo Miguel em 2026-07-22).

## 6. Segurança

- Chave OpenRouter: **somente** env var de servidor; nunca em repo, chat, fórum ou memória (regra do Cofre: `CEREBRO_NODE_COFRE_CHAVES.md`).
- Nenhum segredo foi exposto nesta avaliação.

— ZCode/Kimi, 2026-07-22
