# 13 — DESENHO V3: Premium como DEFAULT (decisão do Miguel, 23/07/2026)

> **Ditado pelo Miguel em 23/07 ~12:50.** Versão avançada do funil Moka. Baseline de retorno gravada ANTES de codar (§regra permanente): `Moka/backups/moka_V2.3.2_lab_PRE_V3_2026-07-23.zip` + `moka_pontos_api_v1.1_checkout_PIX_2026-07-23.zip` + tag git `v2.3.2-pre-v3`.

## 1. Os 3 produtos (a prateleira nova)

| Produto | Preço | O que é | IA |
|---|---|---|---|
| **🎣 Trial** | **R$ 5 → 200 pontos** | "Teste por R$5" — o segredo do funil. Preço de café, experiência completa | **Servidor (premium default)** |
| **🔑 BYOK** | **R$ 15/mês** | Usa a PRÓPRIA chave de IA (fica no navegador, não guardamos). Assinatura = acesso ao app premium sem IA incluída | **Do usuário** |
| **⭐ Premium** | **R$ 24,90/mês** | Tudo ilimitado*, sem chave nenhuma. IA nossa de fábrica | **Servidor** |

*ilimitado = cap mensal de pontos generoso (definir; ex.: 2.000 pts/mês) para proteger margem.

**A lógica do funil:** o R$5 com 200 pts é quase breakeven/prejuízo controlado (custo real de 200 pts ≈ R$4–8 — doc 02) — é a ISCA que prova o valor. A conversão para assinatura paga o CAC (doc 09: meta ≥12%).

## 2. Premium como DEFAULT (a mudança de arquitetura)

- Hoje: o app pede chave de IA do usuário (BYOK) na 1ª tela → fricção enorme, mata conversão.
- V3: **entra e usa** — a IA sai do NOSSO gateway de servidor, debitando pontos da conta.
- BYOK vira opção (⚙️ "usar minha própria chave") — a chave segue local, nunca sobe pro servidor.

### Gateway de IA do servidor (a peça nova central)
```
Moka-Lab → POST /ia/resumir  (auth: email+senha da conta)
         → pontos_api valida saldo → chama DeepSeek/Kimi/etc com NOSSA chave
         → debita pontos via /consumir → devolve o resultado
```
- Cascata de custo (doc 02): resumo DeepSeek V3 → fallback GLM; livro Kimi (moonshot-v1-128k); tradução DeepSeek; TTS OpenAI (fallback Edge-TTS).
- Anti-estouro já existe: HTTP 402 quando zera → tela de upsell (assinatura).

## 3. Os 2 painéis (pedidos explícitos do Miguel)

| Painel | Para quem | O que mostra | Estado |
|---|---|---|---|
| **Painel de pontos** | Trial + Premium | saldo, histórico de consumo, totais creditados/consumidos | ✅ **JÁ EXISTE** (`/painel` na API, login email+senha) |
| **Painel de gastos BYOK** | BYOK R$15 | gasto estimado da PRÓPRIA chave: tokens de entrada/saída × preço do modelo, por dia/mês, por recurso | 🆕 a construir (viável: toda resposta de LLM traz `usage`; acumular no IndexedDB/localStorage do app — nada sobe pro servidor) |

## 4. Mudanças por componente

### pontos_api (Tencent)
- [x] Pacote trial: `r5_100` → **`r5_200`** (R$5 = 200 pts) — FEITO 23/07
- [ ] Tabela `assinantes` (user_id, plano byok|premium, gateway_sub_id, status, renova_em) — schema v2
- [ ] Recorrência MP (preapproval) p/ R$15 e R$24,90 + webhook de assinatura
- [ ] Endpoints gateway `/ia/*` (resumir/traduzir/tts) com débito de pontos
- [ ] Tela de upsell 402 → assinatura

### Moka-Lab (app)
- [ ] Modo default "Sem chave": chama o gateway com login da conta
- [ ] BYOK como opção em ⚙️ (fluxo atual vira o "modo avançado")
- [ ] Painel de gastos BYOK (usage tokens × tabela de preços, client-side)
- [ ] Tela de login/conta dentro do app (linka com pontos_api)

### Landing /experimente
- [x] Copy: 100 → **200 pontos** — FEITO 23/07
- [ ] Seção comparativa dos 2 planos (BYOK R$15 × Premium R$24,90)

## 5. Riscos e guardas

1. **Isca R$5/200pts pode dar prejuízo unitário** — aceito conscientemente (loss leader); monitorar custo médio real por comprador no 1º fim de semana (view `v_custo_diario`).
2. **Abuso do default sem chave** — conta + pagamento R$5 como barreira; cap de pontos; device fingerprint se virar farm.
3. **Margem do Premium** — cap mensal + cascata barata (DeepSeek 1º) + TTS limitado.
4. **Chave BYOK** — nunca sobe pro servidor (regra permanente); painel de gastos é 100% client-side.
