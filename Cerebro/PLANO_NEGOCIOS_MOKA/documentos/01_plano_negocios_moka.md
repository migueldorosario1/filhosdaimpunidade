# Plano de Negócios — Moka: Assinatura, Capital (20.000 títulos) e Página do Investidor

**Data:** 2026-07-22 | **Para:** Miguel do Rosário | **Escopo:** modelo de receita, estrutura de capital, painel público do investidor e arquitetura cripto

---

## 1. Preço de assinatura — pesquisa de mercado (jul/2026)

| Concorrente | Preço/mês |
|---|---|
| Kindle Unlimited (Amazon BR) | R$ 24,90 (reajustado de 19,90) |
| Substack (mínimo por newsletter) | US$ 5 (~R$ 28) |
| Valor Econômico | R$ 24,90–59,90 |
| VEJA | R$ 9,90–14,99 |
| Gazeta do Povo | ~R$ 19,90 |

**Posicionamento sugerido do Moka Premium: R$ 24,90/mês** — âncora exata do Kindle Unlimited, com o diferencial que nenhum deles tem: resumo de vídeo, tradução de livros e áudio sob demanda, além dos 7 portais de notícia. Plano anual: R$ 249 (2 meses grátis).

*O sistema de pontos (já construído) continua como porta de entrada: amostra 200 pts grátis → pacotes avulsos → upsell para assinatura ilimitada.*

## 2. Unit economics por assinante

| Item | Valor/mês |
|---|---|
| Receita bruta | R$ 24,90 |
| Gateway (MP/Stripe ~4%) | − R$ 1,00 |
| Custo LLM por assinante ativo típico¹ | − R$ 3,50 a 7,00 |
| **Margem por assinante** | **≈ R$ 17–20** |

¹ Uso típico: 10 resumos de vídeo + 5 livros + 2 traduções + TTS leve ≈ US$ 0,65–1,30.

**Custos fixos mensais:** Vercel Pro ($20) + Transkriptor (~$30) + LLM base + domínios + servidores ≈ **R$ 900/mês**.

**Ponto de equilíbrio: ~50–60 assinantes pagantes.** Abaixo disso, prejuízo controlado de até ~R$ 900/mês; acima, tudo é lucro marginal.

## 3. Estrutura de capital — 20.000 títulos

- **Capital:** 20.000 títulos; Miguel detém os 20.000 no início e pode vender cotas
- **Cada título = 0,005% do lucro distribuído** (20.000 × 0,005% = 100%)
- **Waterfall:** (1) receita → (2) custos operacionais → (3) reserva de reinvestimento (sugestão 30%) → (4) **lucro distribuído proporcional aos títulos**
- **Preço do título na venda inicial:** referência de valuation. Ex.: projetando R$ 250 mil de lucro no ano 2, payout/título = R$ 12,50/ano → título pode ser vendido a R$ 50–100 (múltiplo 4–8× payout). **O painel mostra o valor de mercado implícito do título em tempo real.**
- **Fundadores (primeiros sócios):** bônus de entrada — ex.: 2× títulos pelo preço de 1 nos primeiros 1.000 títulos vendidos.

## 4. A página do investidor (pública, atualizada)

**URL sugerida:** `moka.app/investidores` — dois modos:

### Modo REAL (dados vivos)
- Assinantes ativos agora, MRR, receita acumulada
- Custos do mês, lucro/prejuízo acumulado desde o início
- **Gráfico rumo ao breakeven** (barra de progresso até 60 assinantes)
- Por título: payout acumulado, valor implícito, % do lucro
- "Seu painel": login do sócio mostra seus títulos e seu total a receber

### Modo SIMULAÇÃO (o "link L Simula")
- Slider de assinantes (0 → 10.000) → calcula ao vivo: MRR, custos, lucro, payout por título, valor da cota do visitante
- Cenários prontos: pessimista (150 ass.), base (500 ass.), otimista (2.000 ass.)
- **Botão "quero ser sócio"** → checkout do título

## 5. Arquitetura cripto (com pé no chão jurídico)

**Caminho seguro (recomendado agora):**
- Títulos como **unidades contábeis** no nosso ledger (não token em blockchain) — escritura/contrato privado
- **Payout opcional em USDC/stablecoin** para sócios internacionais (Pix para BR, USDC para fora) — atrai investidor cripto sem emitir security token

**Caminho futuro (só com advogado):**
- Tokenização real dos títulos (ERC-20 ou similar)
- ⚠️ **Alerta jurídico:** vender participação em lucros a investidores é oferta de valor mobiliário. No Brasil, exige enquadramento — crowdfunding de investimento regulado (Resolução CVM 88) ou estrutura contratual privada bem desenhada. **Antes de vender o 1º título: parecer jurídico.** Isso vale 10× mais para token.

## 6. Entregáveis técnicos (ordem sugerida)

1. `moka_pontos/` (✅ pronto: schema + API de pontos)
2. Tabela `assinantes` + `titulos_capital` no mesmo banco (extensão do schema v1)
3. Página pública `/investidores` (modo real + simulador)
4. Painel do sócio com login (mesma auth da API)
5. Gerador de convites + landing da amostra grátis
6. Webhook gateway → métricas reais na página

---

*Relatório gerado por ZCode (Kimi) em 22/07/2026. Arquivos relacionados: `estudo_sistema_pontos_moka_20260722.md`, `moka_pontos_schema_v1.sql`, `moka_pontos/app.py`.*
