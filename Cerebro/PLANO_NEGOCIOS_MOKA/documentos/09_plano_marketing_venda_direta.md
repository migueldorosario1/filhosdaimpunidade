# Plano de Marketing — Venda Direta do Moka (funil R$5 → assinatura)

**Data:** 2026-07-22 | **Estratégia:** vender a EXPERIÊNCIA por R$5, converter para assinatura R$24,90/mês. Investidores seguem em paralelo (não dependemos deles).

---

## 1. O funil (a máquina de venda)

```
ANÚNCIO (FB/IG/Google/X)
   ↓ clique (R$0,50–3,00)
LANDING: "Resuma qualquer vídeo ou livro em 2 minutos — teste por R$5"
   ↓ conversão landing 3–8%
CHECKOUT R$5 (Pix ou cartão — Mercado Pago)
   ↓ 100 pontos na hora
EXPERIÊNCIA: 3 vídeos + 1 livro + 1 áudio
   ↓ conversão p/ assinatura 8–15%
ASSINATURA R$24,90/mês
```

## 2. A promoção de lançamento ("pague R$5 e experimente")

| Item | Valor |
|---|---|
| Preço | **R$ 5,00** (Pix/cartão) |
| Entrega | **100 pontos** (3 vídeos de 10min + 1 livro + 1 áudio TTS) |
| Nosso custo | ~R$ 2,00 (LLM+transcrição) |
| Margem direta | ~R$ 3,00 (60%) — **a promoção quase se paga sozinha** |
| Alternativa $1 US | R$5 já É o "$1 experimente" para o público BR |

Upsell dentro da experiência: a cada ação concluída, mostrar "com assinatura isso é ILIMITADO por R$24,90/mês".

## 3. As contas de CAC (custo por assinante)

| Métrica | Conservador | Base | Otimista |
|---|---|---|---|
| Custo por clique | R$ 2,00 | R$ 1,00 | R$ 0,60 |
| Conversão landing → R$5 | 3% | 5% | 8% |
| Custo por compra R$5 | R$ 67 | R$ 20 | R$ 7,50 |
| Conversão R$5 → assinatura | 8% | 12% | 15% |
| **CAC por assinante** | **R$ 835 ❌** | **R$ 167** | **R$ 50** |
| CAC ajustado c/ margem do R$5* | R$ 770 | R$ 155 | R$ 47 |

*desconta os ~R$3 de margem de cada venda R$5.

**Leitura:** o plano só fecha as contas se a landing converter ≥5% E a experiência converter ≥12%. O cenário conservador é inviável — por isso a landing e a experiência R$5 precisam ser IMPECÁVEIS (poucos campos, Pix em 1 clique).

**LTV (valor do assinante):** R$24,90 × retenção média 8 meses × margem 75% ≈ **R$ 150/assinante** → meta: **CAC ≤ R$ 75** (LTV 2× CAC).

## 4. Plano de mídia por canal (onde anunciar)

| Canal | CPC BR típico | Perfil do público | Veredito |
|---|---|---|---|
| **Facebook/Instagram** | R$ 0,80–2,00 | 30–60 anos, notícia/política, lookalike dos leitores dos portais | **#1 para começar** — público certo, barato, criativo com vídeo do produto |
| **Google Ads (busca)** | R$ 1,50–4,00 | intenção quente ("resumir livro", "resumo de vídeo") | **#2** — volume baixo mas conversão alta |
| **X/Twitter** | R$ 1,00–3,00 | política em tempo real, mas ads fracos no BR | teste pequeno (R$ 300) |
| **AdSense (display)** | R$ 0,30–1,00 | rede de sites, frio | só retargeting depois |

**Tático matador (custo zero):** anunciar NOS NOSSOS 7 PORTAIS — banner central já é do Moka! Campanha própria na home de cada um: "Resuma vídeos e livros por R$5". Isso é mídia gratuita antes de pagar qualquer centavo.

## 5. Plano de investimento (escada de 8 semanas)

| Semana | Ação | Mídia paga | Meta |
|---|---|---|---|
| 1–2 | Landing + checkout Pix + banner nos 7 portais (mídia própria) | R$ 0 | 20–50 vendas R$5 → validar funil |
| 3–4 | FB/IG R$ 1.500 (3 criativos × R$500) | R$ 1.500 | CAC compra-R$5 ≤ R$ 20; primeiras 10 assinaturas |
| 5–6 | Otimizar criativo vencedor + Google busca R$ 800 | R$ 2.300 | 30–60 assinantes (**breakeven**) |
| 7–8 | Escalar o que deu lucro | R$ 3.000 | 150+ assinantes, CAC ≤ R$ 75 |

**Total mídia até breakeven: ~R$ 3.800–6.800** — comparável a vender ZERO títulos de sócio. Por isso este plano é melhor: não depende de investidor.

## 6. A arquitetura técnica do funil (o que construir)

1. **Landing `/experimente`** — 1 página: promessa + 1 botão Pix R$5 (Mercado Pago Checkout Bricks, sem cadastro prévio)
2. **Webhook MP** → cria usuário no `moka_pontos` + credita 100 pts + manda link de acesso por e-mail (rota Tencent)
3. **Experiência guiada** — tela "seus 100 pontos": 3 botões prontos (resumir vídeo / resumir livro / ouvir áudio) para fricção zero
4. **Upsell** — ao zerar pontos: tela de assinatura com 7 dias de desconto de lançamento
5. **Métricas** — eventos GA4: `ad_click → landing_view → compra_r5 → primeira_acao → assinatura` (funil medido por etapa)
6. **Retargeting** — pixel FB no site; público dos 7 portais vira lookalike 1%

## 7. Riscos e mitigações

1. **Criativo fraco mata o CAC** — testar 3 abordagens: (a) dor "não tem tempo de ler", (b) mágica "livro inteiro em 2 min", (c) política "os vídeos que você não assiste, resumidos"
2. **Fraude no R$5** — 1 compra por e-mail/cartão no lançamento
3. **Gateway** — Mercado Pago: Pix ~0,6% + cartão ~4,99%; precificar cartão a R$5,90 se precisar (ou absorver no lançamento)
4. **Custo de LLM por curioso** — cap de 100 pts fixo; sem recarga grátis

## 8. O que os investidores ganham com isso

O plano de 20.000 títulos continua — mas agora o painel do investidor mostrará **números reais de um funil que vende desde a semana 1**, não projeção. Venda direta primeiro, sócio depois com prova de tração.
