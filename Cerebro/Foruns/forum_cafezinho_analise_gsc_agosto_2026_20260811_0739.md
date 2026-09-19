# Fórum — Análise Google Search Console (O Cafezinho) — Agosto 2026

**Data:** 2026-08-11 ~07:30 BRT
**Agente:** ZCode (GLM-5.2 Z.ai)
**Fonte:** Relatórios GSC baixados pelo Miguel em `Outros/google search/google 11 ago 2026/` (período: últimos 3 meses, 10/05→09/08)

## Pergunta do Miguel
Verificar a situação no GSC após o "baque" de há alguns meses — análise otimista, focar em pontos de recuperação.

## Comparativo www vs não-www (dúvida do Miguel)
- `www.ocafezinho.com`: **233.714 cliques** / 8,7M impressões (3 meses) — **99% do tráfego**
- `ocafezinho.com` (sem www): **2 cliques** / 155 impressões — irrelevante
- **Conclusão:** `www` é o canônico consolidado. Sem problema de conteúdo duplicado. Ambas as propriedades podem coexistir no GSC.

## Evolução mensal (SEARCH)
| Mês | Cliques | Impressões | Média/dia |
|-----|---------|------------|-----------|
| 2026-05 | 78.650 | 3.619.490 | 3.575 |
| 2026-06 | 71.828 | 2.690.585 | 2.394 |
| 2026-07 | 60.038 | 1.740.103 | 1.936 |
| 2026-08 (parcial 9d) | 23.198 | 658.347 | 2.577 |

## Evolução mensal (DISCOVER)
| Mês | Cliques | Impressões | Média/dia |
|-----|---------|------------|-----------|
| 2026-05 | 339.428 | 7.493.579 | 15.428 |
| 2026-06 | 9.314 | 204.165 | 310 (nadir) |
| 2026-07 | 22.648 | 386.566 | 730 |
| 2026-08 (parcial 9d) | 14.271 | 335.065 | 1.585 |

## Evolução mensal (GOOGLE NEWS)
| Mês | Cliques | Impressões | Média/dia |
|-----|---------|------------|-----------|
| 2026-05 | 3.579 | 273.159 | 162 |
| 2026-06 | 3.713 | 178.748 | 123 |
| 2026-07 | 3.722 | 133.208 | 120 |
| 2026-08 (parcial 9d) | 639 | 27.243 | 71 |

## Tendência de curto prazo (últimos 14 dias vs 14 anteriores)
- **SEARCH:** -1,5% (estável ~2.570 cliques/dia). Posição média melhorou 3,96→3,29 ✅
- **DISCOVER:** -29% (1.445→1.024/dia) — oscilação normal do Discover (volátil por natureza)

## Pontos fortes (análise otimista)
1. **SEARCH é estável e robusta:** ~2.500-2.600 cliques/dia consistentes. 8,7M impressões em 3 meses = alcance enorme.
2. **Posição média melhorando:** 3,96 → 3,29 nos últimos 14 dias = subindo no ranking.
3. **Marca consolidada:** "o cafezinho" tem CTR 59,82% na posição 1,14 — busca de marca forte.
4. **Top pages com altíssimo CTR:** home 32%, Eduardo Moreira/demissões 12%, Datafolha/Lula 17%.
5. **DISCOVER em recuperação clara:** depois do nadir de junho (310/dia), voltou pra 730 em julho e 1.585 em agosto = **5x acima do fundo**. O Discover impulsiona muito quando pega.
6. **Mobile domina e bem convertido:** 196k cliques mobile com CTR 3,14% (vs desktop 1,51%).
7. **www é o canônico quase absoluto** (99%) — sem problema duplicação.

## Pontos de atenção (não críticos, oportunidades)
1. **Core Web Vitals mobile:** 3.318 URLs com CLS > 0,1 e 410 com LCP > 4s — oportunidade de UX/SEO.
2. **Cobertura:** 6 URLs "indexadas mas bloqueadas pelo robots.txt" — vale revisar se é intencional.
3. **Discover volátil:** caiu muito em junho, recuperando — sensível à cadência/viralização de pautas.

## Estado / O que falta / Próximos passos
- **Feito:** análise completa entregue ao Miguel.
- **Opcional (Miguel decide):** (1) resolver as 6 URLs bloqueadas no robots; (2) atacar CWV mobile (CLS/LCP); (3) configurar redirect não-www→www para limpeza final (opcional, tráfego sem-www é ~0%).

---

## ADENDO — Investigação das 6 URLs "bloqueadas pelo robots.txt" (~07:55)

**Dúvida do Miguel:** vale resolver os 6 URLs do Coverage crítico/não-crítico?

**Diagnóstico:** As 6 URLs são **arquivos de sistema JavaScript/CSS do WordPress** sob `/wp-includes/` (ex.: `jquery-migrate.min.js`, `jquery.min.js`, `i18n.min.js`, etc.).

**Como surgem:** O Google rastreou e indexou esses arquivos (são públicos, HTTP 200), mas o `robots.txt` tem `Disallow: /wp-includes/` → o Google mantém no índice com a flag "bloqueada".

**Veredito: NÃO É PROBLEMA — nada a corrigir.**
- Arquivos técnicos do core WP, não geram tráfego nem competem com conteúdo.
- O bloqueio no robots.txt é a configuração **correta e recomendada** pelo WordPress e Google.
- 6 URLs num site com 66.564 indexadas = 0,009% (estatisticamente zero).
- GSC mostra como "não crítico" justamente por isso.

**Descoberta adicional:** o `robots.txt` que o Google vê é **híbrido** — o Cloudflare injeta regras próprias no topo (bloqueio de crawlers de IA: GPTBot, ClaudeBot, Google-Extended, etc. + Content-Signal `ai-train=no`), e abaixo vem o robots do portal (`Disallow: /wp-admin/`, `/wp-includes/`). Configuração correta.

**Próximo foco:** Core Web Vitals mobile (CLS 3.318 URLs, LCP 410 URLs) — onde está o ganho real de SEO.
