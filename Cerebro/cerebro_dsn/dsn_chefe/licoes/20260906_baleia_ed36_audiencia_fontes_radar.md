# Lição 06/09 — Baleia em formato AUDIÊNCIA: fontes de dados reais + armadilha do posts_por_hora

**Quando:** 06/09/2026 ~07:00-07:10 BRT, ronda 228º (ed. 36 da Baleia Azul, 1ª edição completa no formato da retificação 05/09 ~18:55).
**O quê:** aprendi (e fixei) onde buscar cada número do boletim de audiência, e que uma fonte aparente de contagem de posts pode enganar.

## O quê / Por quê
A diretriz retificada (05/09 ~18:55) manda o boletim falar de AUDIÊNCIA com os 4 medidores nomeados, histórico, tempo de permanência e top posts POR AUDIÊNCIA. Para produzir a ed. 36 com números reais (nunca inventados), o caminho de leitura que funcionou foi:

1. FAROL — banco local `/home/ubuntu/cafezinho/v6_data/farol_audiencia.db`, tabela `medicoes` (ts, online, views_ga4, posts_48h, extra JSON): o `extra` tem online_30min humanos/robôs, hoje humanos/robôs distintos, navegações, visitantes, posts_por_hora. Ler a linha ts mais recente (gerado ~25 min após o ts) + linhas de fechamento do dia (23:30) e mesma-hora de dias anteriores para o histórico.
2. LUMINA — `/home/ubuntu/cafezinho/v6_data/lumina_audiencia.jsonl` (campo `coletado_em` = BRT; `gerado_em` está em UTC — 3h à frente; não confundir).
3. GA4 (contador do painel) — coluna `views_ga4` do farol + agregados em `http://43.156.151.165/v6/api/resumo` (views_7d, mm7_hoje, tendencia_7d, views_ontem).
4. TOP POSTS POR AUDIÊNCIA + TEMPO DE PERMANÊNCIA — `http://43.156.151.165/v6/api/tendencias/pautas` → `top10_mais_lidos` (radar_atual.json, campo `ga4_24h_top`): cada item tem path (versão `/amp/` e versão artigo separadas!), pub, views, users e **tempo_s (tempo médio na página)**. É daqui que saiu o insight da ed. 36: artigo 97-151s × AMP 1-4s — o tráfego AMP (Discover/agregadores) é de passagem; quem lê de verdade está no artigo.

## Armadilha (por que anotar)
O `posts_por_hora` do farol pode mostrar contagens que NÃO batem com o ar real: na ts 06:30 de 06/09 ele listava 6 posts na hora 06 de 06/09 e 2 na 00 — mas o REST do canônico (`https://www.ocafezinho.com/wp-json/wp/v2/posts?after=...`, fuso local) e o `/v6/api/resumo` (publicacoes.hoje) confirmavam 0 posts no ar em 06/09. Fonte de verdade de "posts no ar" = REST do canônico (ou o resumo do painel), nunca o posts_por_hora do farol (conta outra coisa — provavelmente toques do coletor/health, não publish).

## Como aplicar
Toda edição da Baleia em formato audiência: (a) LUMINA + FAROL db + GA4 (resumo API) + top10_mais_lidos (tendencias/pautas) na ordem acima; (b) nomear SEMPRE o medidor e o período; (c) conferir "posts hoje" no REST canônico antes de afirmar volume; (d) o tempo_s separado amp×artigo é o ouro editorial — o dono quer saber o que o público faz, não só quantos são.

— DS Nuvem Chefe (DS-N Chefe) · DeepSeek V4 Flash · 20260906 07:1x BRT
