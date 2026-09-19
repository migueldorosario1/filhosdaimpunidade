# Fórum — GSC: 49.356 páginas "Excluída pela tag noindex" no CANÔNICO (investigação ZM)

**Data:** 06/09/2026 ~18:3x–19:0x BRT
**Agente:** ZCode (GLM-5.3, pelo Dell)
**Gatilho:** Miguel viu no Google Search Console (propriedade `ocafezinho.com`, o CANÔNICO — não o espelho) a lista de "Páginas não indexadas" e perguntou com urgência: por que tantas páginas excluídas por noindex? Ainda tem robô fazendo noindex no Cafezinho?
**Exports do Miguel analisados:** `Outros/google search/google search/google search 6 set 2026/` (Coverage, Performance, AMP, HTTPS, CWV ×2).

## RESUMO EM 1 PARÁGRAFO (a resposta ao Miguel)

NÃO existe robô novo ou fugindo do controle injetando noindex. Os noindex do canônico vêm de **operações deliberadas da própria casa** — o saneamento SEO do recovery do Google Discover (autorizado pelo Miguel em 27/06 e 01/07/2026) — mais mecanismos estáticos de SEO (Yoast + 4 mu-plugins). O sincronizador do saneamento automatizado **parou em 20/07/2026** e nenhum cron na Tencent o alimenta desde então. O número é alto (49.356) porque o GSC congela o estado da ÚLTIMA avaliação de cada URL e quase nunca re-rastreia URL noindex — a lista acumulou tudo que passou pelos lotes de junho/julho + páginas institucionais antigas. E o site está SAUDÁVEL no Search: o recovery funcionou.

## Composição do noindex no canônico (o que responde noindex HOJE)

| Mecanismo | Origem/data | Volume | Prova ao vivo (06/09) |
|---|---|---|---|
| `cafezinho-noindex-pruning.php` (mu-plugin) | Sprint Trindade 27/06/2026, AUTORIZADO pelo Miguel (recovery Discover) | 358 posts clickbait fora-do-nicho | `/2026/04/14/nasa-anuncia-sr-1-freedom.../` → `<meta name='robots' content='noindex, follow'/>` ✓ |
| Meta Yoast `_yoast_wpseo_meta-robots-noindex=1` | Auditoria de categorias 28/06 (2.368 candidatos; ~550 efetivados) | 550 posts (Ciência/Tec, Sobrenatural, Fantástico) | via wp db query ✓ |
| `cafezinho-noindex-pages.php` (mu-plugin) | GLM 06/07 + regra temporal do editor 10/08/2026 | ~570 pages antigas (577 pages no total) | `/logout/` (page 77275) → `noindex` ✓ |
| `cafezinho-seo-pruning.php` (mu-plugin + robô Tencent) | GLM 01/07 — listas via REST; **CONGELADO em 20/07/2026 00:07** | option atual: 1.317 URLs em **410-Gone** + 1 em noindex | option lida no banco ✓ |
| `cafezinho-gone-pending-review.php` | Codex/Miguel | 10 URLs em 410 (revisão editorial) | — |
| Yoast global | config `wpseo_titles` | post_format + CPT produto noindex; anexos = redirect 301; tags (18.542), categorias (310) e datas INDEXÁVEIS | `/tag/lula/` 200 sem noindex ✓ |

**Posts novos: saudáveis.** Post comum de 2025 provado `index, follow`; posts de set/2026 indexáveis; a esteira de robôs NÃO contamina post novo com noindex.

## Por que 49.356 se os mecanismos ativos somam ~2 mil?

1. O GSC reporta o estado da ÚLTIMA avaliação de cada URL conhecida; URL noindex é re-rastreada raramente (o Google propositalmente quase não volta) → a lista é um ACÚMULO histórico, não um retrato do que responde noindex hoje.
2. O saneamento automatizado rodou em LOTES durante julho (a option guarda só a última lista — as anteriores eram sobrescritas). Prova no gráfico do Coverage: em **24/07 as não-indexadas pularam +11.041 de uma vez**, logo após a última sincronização (20/07 00:07).
3. Os 1.317 "410 Gone" da última lista aparecem no GSC como "Não encontrado (404)" (3.860 atuais — coerente).

## Os outros números do Coverage (contexto, ~280k URLs conhecidas / 74.847 indexadas)

- **68.554 "Página alternativa com tag canônica adequada"** = AMP (~13k URLs válidas) + `/embed/` dos ~79k posts (ambos provados ao vivo: 200 com canonical → post) + feeds. Comportamento PADRÃO e saudável de WP+AMP.
- **70.872 "Rastreada, mas não indexada"** + **7.867 "Detectada..."** = decisão do GOOGLE (conteúdo fino/duplicado), NÃO é noindex nosso. É o único número que merece atenção editorial contínua.
- 3.090 robots.txt / 1.665 redirect / 162 5xx — pequenos e normais.

## Performance (últimos 3 meses, Web) — o recovery FUNCIONOU

- ~180k cliques, 6,3M impressões; mobile: CTR 3,25%, posição média 3,65; desktop 1,71%/6,04.
- **AMP = 101.448 cliques** (3,2M impressões, posição 2,51) — desligar AMP seria atirar no pé.
- Top consultas: "o cafezinho" 25.886 cliques, "irã" 9.848, "flávio bolsonaro" 5.188 — nicho certo, marca forte.
- HTTPS: 0 problemas. CWV: apenas melhorias (INP/CLS/LCP mobile), zero URLs "ruins" reportadas.
- Últimos dias ~1,1k–2,6k cliques/dia (04/09: 2.598).

## O que aconteceu / o que falta / o que preciso de você (Miguel)

**O que aconteceu:** investigação completa, leitura-only (NADA foi alterado no site). Diagnóstico fechado com provas ao vivo em 3 famílias de URL + banco + crons + exports GSC.

**O que falta:** nada urgente. Nenhum robô precisa ser desligado (já estão parados desde 20/07) e nenhuma página nova está sendo contaminada.

**O que preciso de você (decisões OPCIONAIS, sem urgência):**
1. Quer que eu peça re-rastreamento das ~2 mil URLs que hoje são noindex para "limpar" o relatório? (NÃO recomendo — o objetivo do saneamento era exatamente tirá-las do índice; o número alto do GSC é assinatura do trabalho bem-feito.)
2. Quer reduzir as 68.554 "alternativas canônicas" (ex.: desligar /embed/)? NÃO recomendo mexer no AMP (101k cliques).
3. O único indicador que recomendo acompanhar: "Rastreada, mas não indexada" (70.872) — cresce se a esteira produzir conteúdo fino. Já é vigilância editorial, não de noindex.

## Rollback / referências

- Rollback de cada mecanismo: ver cabeçalhos dos mu-plugins (`rm mu-plugins/cafezinho-noindex-pruning.php` etc.).
- Fóruns irmãos: `forum_central_recuperacao_seo_cafezinho_20260627.md`, `Projeto Cafezinho Agentes/Foruns/forum_saneamento_seo_automatizado_lotes_20260701.md`.
- Espelho `cafezinho.news` NÃO entra nessa conta: é sandbox noindex site-wide de propósito (X-Robots-Tag provado; README "Cafezinho Espelho No-Index").
- Memória técnica completa: `Memorias/memoria_gsc_noindex_49mil_canonico_20260906.md`.
