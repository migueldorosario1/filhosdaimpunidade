# 📊 Fórum — Gap produção × publicação: por que tem tanta matéria no rascunho (27/08/2026)

> Pergunta do Miguel (~16:1x BRT): "analisa o gap entre produção e publicação. tem muita matéria no rascunho. veja se o número de matérias produzidas está superando muito o número de publicadas."

## Resposta curta

**NÃO — o fluxo atual não está produzindo muito mais do que publica.** O susto do número total de rascunhos (2.383) é **estoque legado**: 2.243 deles (94%) têm mais de 30 dias (os mais antigos são de 2013, do início do site). No ritmo atual, ~95% do que se produz num dia é publicado no mesmo dia.

## Números (WP canônico, controle.ocafezinho.com, medidos 27/08 ~16:15 BRT)

**Totais por status:** publish 78.610 · draft 2.383 · pending 361 · future 3 · private 5.

**Fluxo por dia (BRT):**

| Dia | Publicados | Rascunhos novos | Pendentes |
|-----|-----------|-----------------|-----------|
| 20/08 | 49 | 2 | 3 |
| 21/08 | 46 | 1 | 2 |
| 22/08 | 47 | 3 | 0 |
| 23/08 | 59 | **51** ⚠️ | 6 |
| 24/08 | 56 | 6 | 0 |
| 25/08 | 53 | 5 | 1 |
| 26/08 | 50 | 4 | 3 |
| 27/08 (até 16h) | 37 | 8 | 1 |

**Idade dos 2.383 rascunhos:** hoje 12 · ontem 5 · 2-7 dias 68 · 8-30 dias 55 · **>30 dias 2.243**.

## As duas causas reais do "muita coisa no rascunho"

1. **Legado (94%):** 2.243 rascunhos com mais de 30 dias, incluindo posts de 2013 (era pré-automação). Nunca serão publicados; são lixo de banco que infla o número do painel.
2. **Burst pontual de 23/08:** 51 rascunhos num único dia, criados de madrugada, em grande parte **variações da mesma pauta** (ex.: 3 versões da notícia Serpro/IA-China #267129/#267132/#267165; Datafolha-RJ, dólar, FAB). Um agente/rodada gerou versões redundantes e só uma foi adiante. Não se repetiu nos dias seguintes (voltou a 4-8/dia).

## Estado / o que falta / o que preciso do Miguel (decisão)

- **Feito:** medição completa por dia, idade do estoque e amostragem (dados acima, método reexecutável: script `/tmp/analise_gap_prod_pub.py` no NYC).
- **Pendências menores:** 361 posts "pending" formam um segundo estoque a olhar; mapeamento autor→rascunho não saiu (REST /users não resolveu nomes via lista padrão).
- **Decisão do Miguel (se quiser):** (a) limpeza do legado — ex.: arquivar/apagar rascunhos >1 ano (2.2k, com backup antes); (b) investigar a rodada de madrugada de 23/08 que gerou variações duplicadas. Nenhuma ação foi tomada — só análise, como pedido.

— ZCode/GLM-5.3, 27/08/2026 16:19 BRT
