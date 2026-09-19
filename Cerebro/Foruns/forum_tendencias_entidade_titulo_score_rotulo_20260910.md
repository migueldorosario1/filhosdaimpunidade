# Fórum — /v6/tendencias: título com &#8220; no CCTV + validação do Score V2 (rótulos honestos)

**Data:** 10/09/2026 ~22:4x BRT · **Autor:** ZCode/GLM-5.3 · **Ref:** ZM-20260910-024
**Gatilho:** Miguel viu no /v6/tendencias o card #10 (post 269603, Andrei×Dino) com `&#8220;` visível no título e perguntou: é só no CCTV ou o post também está quebrado? As tendências estão corretas?

## Diagnóstico (pergunta 1 — o título)

- **Post público: SAUDÁVEL.** Banco limpo (post_title com aspas RETAS; varredura dos últimos 600 títulos = 0 entidades), H1 renderiza “ ” curvas (wptexturize) e `<title>`/og usam `&quot;` — leitor não vê nada quebrado.
- **CCTV: QUEBRADO por escape duplo.** O painel lê o título do endpoint REST `wp-json/cafezinho/v1/top-tendencias`, que devolve `get_the_title()` já filtrado (aspas curvas como entidade `&#8220;` crua); o `_card()` do painel aplicava `html.escape` em cima → `&amp;#8220;` → navegador exibe "&#8220;" literal.
- **Cura:** `html.unescape(title)` no bloco Top 10 antes do escape do card (backup `.bak_pre_tend_score_20260910`, py_compile, restart, prova: 0 escapes duplos, título renderiza “retardaria” com aspas curvas).

## Diagnóstico (pergunta 2 — os números)

Validei a matemática item a item contra o produtor (`nyc:/root/top_tendencias_push.py`):

- **Fórmula REAL (v3, ordem Miguel 24/08):** `v_score = views/h nas últimas 6h + 0,15 × [Views_48h / (Idade_h + 1,5)^1,2]` — velocidade recente manda; a gravidade acumulada entra com peso 15%.
- Conferência: 269603 → 0,84 + 0,15×0,63 = **0,93 ✓**; líder 269641 → 9,84 + 0,15×2,89 = **10,27 ✓**. Números corretos e consistentes.
- **O defeito era o RÓTULO:** a página chamava o score de "Score Gravidade V2" e exibia só `Views_48h/(Idade+1.5)^1.2` (a parcela de 15%), e "Velocidade: X views/h" sem dizer que é das últimas 6h — daí o 0,8 ≠ 48/35,6 que poderia parecer erro.
- **Cura (rotulagem honesta):** "Score Tendência V2" + fórmula completa no rodapé do bloco + "Ritmo agora: X views/h (últimas 6h)".

## Estado / o que falta

- Pronto: página corrigida e provada ao vivo (título com aspas curvas, rótulos e fórmula honestos).
- Não há cura necessária no WP (banco e público OK); a entidade na REST é comportamento padrão do WP (`get_the_title` filtrado).
- Rollback: restaurar `.bak_pre_tend_score_20260910` + restart cctv-v6.
- Memória técnica par: `Foruns/memoria_tendencias_entidade_titulo_score_rotulo_20260910.md`.
