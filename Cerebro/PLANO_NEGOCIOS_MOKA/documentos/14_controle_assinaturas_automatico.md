# 14 — CONTROLE DE ASSINATURAS (100% automático — decisão Miguel 23/07 noite)

> **⚠️ PIVÔ (23/07 ~23h30, decisão do Miguel): NADA DE ASSINATURA.** O modelo virou **PACOTES DE PONTOS** (pague uma vez, pontos não expiram). Isso MELHORA este plano: não há recorrência, carência nem cancelamento pra controlar — o webhook do Pix credita e pronto. Cappuccino R$25=1.000 pts · Latte R$45=2.000 pts · Espresso R$70=3.500 pts (testado E2E: espresso gerou Pix de R$70/3.500 pts real ✅). O texto abaixo fica como referência caso a assinatura volte um dia.

> **Pedido do Miguel:** "você tem que me apresentar um plano de controle de assinatura — as pessoas vão assinar e como é que a gente vai controlar? Tem que ser tudo automático, eu não vou ter tempo pra nada."
> Este é o plano. Regra: **Miguel não opera nada manualmente** — o sistema cobra, ativa, credita, suspende e avisa sozinho.

## 1. Os planos (planos-café — nomes finais do Miguel)

| Plano | Preço | IA | Pontos | O que inclui |
|---|---|---|---|---|
| 🎣 **Teste** | R$ 5 (único) | servidor | 200 (uma vez) | experimentar tudo |
| ☕ **Cappuccino** | R$ 25/mês | **do usuário (BYOK)** | — | app completo + painel de gastos da própria chave |
| 🤎 **Latte** | R$ 45/mês | servidor | 1.000/mês | IA incluída com teto mensal |
| ⚫ **Espresso** | R$ 70/mês | servidor | ~60 livros ou ~80 vídeos/sem | IA incluída, sem pensar em nada |

*Nunca dizer "ilimitado" (regra do Miguel): comunicar as médias concretas. Cap interno anti-abuso ~10.000 pts/mês, invisível pro usuário normal.
**Toda assinatura vale para livros E vídeos** (decisão do Miguel).

## 2. A máquina automática (como funciona sem ninguém tocar)

```
ASSINAR (checkout MP com recorrência — preapproval)
   ↓ webhook MP: assinatura autorizada
ATIVAR → tabela `assinantes` (plano, status, renova_em)
   ↓ webhook MP: cobrança mensal aprovada (authorized_payment)
CREDITAR → Latte: +1.000 pts/mês · Espresso: cap liberado · Cappuccino: acesso liberado
   ↓ se a cobrança FALHAR
SUSPENDER → carência de 3 dias (avisa por e-mail) → pausa o acesso sozinho
   ↓ se o usuário cancelar no MP
ENCERRAR → acesso até o fim do período pago → downgrade automático
```

**O Mercado Pago faz a cobrança recorrente sozinho** (produto "Assinaturas"/preapproval). A nossa API só reage aos webhooks — os mesmos que já validamos no checkout R$5 (assinatura HMAC + idempotência).

## 3. O que o Miguel vê (e o que NUNCA precisa fazer)

### Painel admin (já existe — `/admin` na API de pontos)
- Totais: usuários, receita, compras pagas, Pix pendentes, cupons usados
- Tabela por usuário: saldo, consumo, receita, origem
- Próxima versão (com `assinantes`): plano, status, renova_em, MRR

### Alertas automáticos no Telegram do Miguel (via `_telegram`, já implementado)
- 🎉 "Novo assinante Espresso — fulano@…" (receita!)
- ⚠️ "Pagamento falhou — fulano@… (carência até dia X)"
- 😢 "Cancelamento — fulano@… (acesso até dia Y)"
- 📊 Resumo semanal automático (cron): assinantes por plano + MRR + receita do mês

### O Miguel NUNCA precisa:
- cobrar ninguém (MP cobra), creditar pontos (webhook credita), suspender calote (regra de 3 dias), cancelar (MP avisa), gerar relatório (chega no Telegram).

### Casos manuais raros (via painel admin ou script)
- Reembolso: no painel do MP (2 cliques) — webhook `refunded` já estorna pontos automaticamente.
- Cortesia: `creditar.py` / cupons (já prontos).

## 4. Implementação (ordem)

1. **Schema v2**: tabela `assinantes` (user_id, plano, mp_preapproval_id, status, renova_em, created_at) — backlog item antigo do doc 07.
2. **Checkout de assinatura**: botão do plano → MP preapproval (Cappuccino/Latte/Espresso) → volta pra tela de "assinatura ativa".
3. **Webhook de assinatura**: eventos `subscription_preapproval` e `subscription_authorized_payment` no endpoint MP existente (mesma assinatura HMAC).
4. **Motor de crédito mensal**: authorized_payment → credita pontos do plano + atualiza renova_em.
5. **Carência automática**: cobrança falhou → status `carencia` + 3 dias → `suspenso` (sem IA).
6. **Alertas Telegram** nos 3 eventos + resumo semanal via cron na Tencent.
7. **Painel admin v2**: aba assinantes (plano, status, MRR).

## 5. Guardas de margem

- Latte 1.000 pts/mês ≈ custo máx. R$ 20–40 de IA (uso pesado) vs R$ 45 → margem ok.
- Espresso: cap invisível anti-abuso + cascata barata (DeepSeek primeiro).
- Cappuccino: custo zero de IA (chave do usuário) — R$ 25 quase líquido.
- Toda ação cara (tradução de livro inteiro) sempre debita pontos, mesmo no Espresso — é o cap natural.
