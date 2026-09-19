# 🧠 MEMÓRIA — Monetização + Unificação Moka: especificação técnica (2026-07-22)

> Fórum resumido: `Foruns/forum_moka_monetizacao_unificacao_20260722.md` (decisões do Miguel lá).

## 1. Modelo de cobrança (híbrido aprovado)

- **Free:** BYOK como hoje (vault AES-GCM local). Rótulo sugerido: "modo avançado".
- **Assinatura:** chaves NOSSAS server-side + cota mensal no Supabase.
  - Tabela `subscriptions` (user_id, tier, status, renews_at, gateway, gateway_id).
  - Tabela `usage` (user_id, month, llm_tokens_in, llm_tokens_out, whisper_seconds, videos, books_ops).
  - `/api/proxy*` passa a checar: se usuário logado TEM assinatura ativa → injeta chave do servidor (env do app, nunca no bundle) e registra uso; senão, exige header com BYOK (fluxo atual).
  - Transcrição: assinante → Whisper via `OPENAI_API_KEY` do servidor (já existe como fallback no Video V 0.3.4); BYOK → chave própria (como hoje).
- **Tiers (3):** ☕ Cafezinho / ☕☕ Capuccino / ☕☕☕ Família — quotas e preços a definir com Miguel na sprint de pagamento.

## 2. Gateways

- **Brasil:** Mercado Pago (PIX + cartão). Webhook → atualiza `subscriptions`.
- **Internacional:** Paddle ou Lemon Squeezy (Merchant of Record: VAT/impostos/nota por país). Webhook idem.
- Apple/Google (fase loja): IAP obrigatório nas lojas (regra delas pra conteúdo digital) — planejar na fase Capacitor.

## 3. Unificação (estratégia aprovada: federar agora, fundir na loja)

- **Hoje:** mesma conta Supabase nos dois apps ✅; assinatura única consultada pelos dois; links cruzados; design compartilhado ✅.
- **Loja:** shell único "Moka" (Reader + Video como seções) — reaproveitando packages; Capacitor; botão Fechar real.
- **Risco evitado:** não tocar na estrutura do Reader em produção.

## 4. i18n

- Auto: `x-vercel-ip-country` (Aiatolah já usa) + `navigator.language` fallback; bandeiras grandes p/ troca manual.
- Video: portar `ui-strings.ts` (12 idiomas) do Reader; novas chaves das features de vídeo.

## 5. Pendências técnicas menores (registradas)

- Botão "fechar": impossível em PWA (window.close bloqueado); fazer "⌂ início" + dica de gesto. Real no app nativo.
- Mercado Pago: avaliar conta/CNPJ do Miguel; Paddle: criar conta quando autorizado.

## 6. Bugs corrigidos na mesma sessão (Moka Reader V 1.6.3)

- **Regressão V 1.5 (minha):** timer anti-travamento de 60s disparava com o livro JÁ ABERTO (cleanup não limpava o timer). Fix: `finished` + clearTimeout ao concluir. Reportado pelo Miguel no celular ("o livro estava aberto tranquilo e apareceu o recado").
- **Menu de seleção cortando no celular:** flex-wrap em 2 linhas + botões menores <430px.
- Backup `pre_hotfix_20260722.zip`, push `ec44194` → produção.

— ZCode/Kimi, 2026-07-22
