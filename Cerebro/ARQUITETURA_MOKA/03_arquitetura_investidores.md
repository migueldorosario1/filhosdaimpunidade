# 03 — Arquitetura de Investidores (capital 20.000 títulos)

## Estrutura
- **20.000 títulos**; Miguel detém todos no início e vende cotas
- **1 título = 0,005% do lucro distribuído**
- **Waterfall:** receita → custos → reserva 30% reinvestimento → lucro × (títulos/20.000)
- **Valuation inicial:** payout projetado × múltiplo 4–8× (ex.: R$12,50 payout/ano → título R$50–100)
- **Bônus fundadores:** 2× títulos pelo preço de 1 nos primeiros 1.000

## Página pública `/investidores` (a construir)

**Modo REAL:** assinantes ativos · MRR · receita acumulada · custos do mês · lucro/prejuízo total · **barra rumo ao breakeven (~60 ass.)** · payout e valor implícito por título · login do sócio (seus títulos, seu total)

**Modo SIMULAÇÃO ("link L Simula"):** slider 0–10.000 assinantes → MRR/custos/lucro/payout ao vivo · cenários pessimista 150 / base 500 / otimista 2.000 · CTA "quero ser sócio"

## Cripto (decisão arquitetural)
1. **AGORA:** títulos = unidades contábeis no ledger (contrato privado) + **payout opcional em USDC** para sócios internacionais (Pix BR / USDC fora)
2. **FUTURO (só c/ advogado):** token ERC-20 real
3. ⚠️ **Bloqueio jurídico:** venda de participação em lucros = valor mobiliário → parecer (CVM 88 ou contrato privado) **antes da 1ª venda**

## Unit economics (base do painel)
Assinatura R$24,90 − gateway R$1 − LLM R$3,50–7 = **margem ~R$17–20/ass./mês** · fixos ~R$900/mês · **breakeven ~50–60 assinantes**
