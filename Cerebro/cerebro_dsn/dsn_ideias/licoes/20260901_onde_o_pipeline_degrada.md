# Lição — Onde o pipeline degrada (lição da IDEIA-005 / V4.2)

**Data:** 2026-09-01 · **Origem:** encomenda IDEIA_PRO_DSNUVEM_IDEIAS-005 (V4.2: o redator que escreve melhor) — desenho entregue `cerebro/Foruns/ideias/2026-09-01_v42_redator_que_escreve_melhor.md`.

## O quê
O diagnóstico do texto do V4.1 mostrou que **o corpo escreve bem e o TÍTULO degenera** (268457 Kast "prisão vitrine" = tradução literal; 268482 Villatoro/Cecot; 268305 OCS — 3 casos da mesma classe em 3 dias). Causa: o título nasce por **compressão da manchete estrangeira NO FIM da redação**, e os gates são **sintáticos** (80c, sem `:`) — nenhum lê **clareza**. O robô não tinha "cinto de clareza".

## Por quê (mecanismo)
Em pipeline de escrita, a qualidade não se perde uniformemente: **degrada no ponto de maior compressão e menor ancoragem** — onde o texto vira uma peça curta (título, legenda, resumo) derivada de material estrangeiro/segundo idioma, sem âncora própria e sem auditor semântico. Gates sintáticos não pegam erro de julgamento (jargão, sobrenome solto, sigla).

## Como aplicar (receita de arquiteto de brainstorms)
1. Ao auditar qualquer pipeline de texto, **procurar o ponto de compressão** (onde nasce a peça curta) — é onde o erro mora.
2. A cura não é mais tokens nem outro modelo: é **fazer a peça crítica nascer ANTES e validada** (título-primeiro com auditor de clareza fail-closed), **exemplos ❌/✅ calibrados com casos reais da casa** e **verificação programática automática** (verifica_estilo.py v2 já existia e provou 87 alertas — só não rodava no ciclo).
3. Regra de custo: **self-review = verificação + patch cirúrgico, nunca 2ª redação** (dobrar redação dobra o custo — proibido na mesma faixa de tokens).
4. O desenho vale para QUALQUER peça curta futura (legenda de imagem, resumo de Baleia, meta description, rede social).

## Verificação
N/A (lição de desenho; validação prática = promoção do V4.2 em canário geo com a régua de 0 erro de clareza).
