# Fórum — Correção matéria 264661 + Painel CCTV V6 + Errata "falso incidente 404"

**Data:** 2026-08-07 · **Agente:** ZCode/Qwen 3.8 · **Memória par:** `Memorias/memorias_correcao_materia_264661_painel_v6_falso_incidente_404_20260807.md`

## Decisões / estado

1. ✅ **Título 264661 corrigido** (autorização Miguel msg 15): "Irã desdenha da diplomacia de Trump" — via REST controle, HTTP 200, slug mantido, texto relido e íntegro. No ar: `https://www.ocafezinho.com/2026-08-07/ira-desdenha-diplomacia-de-trump-teatro-em-loop-e-rejeita-ameacas/` (200).
2. ✅ **Painel CCTV V6 "publicações" corrigido**: `html.unescape()` na ingestão (fim das entidades `&amp;#8220;`) + normalização `controle → www` nos links/thumbs. Backup no servidor, cache limpo, serviço reiniciado, verificado ao vivo (0 entidades cruas, 20 links www).
3. ⚠️ **ERRATA: o "incidente site todo 404" nunca existiu.** Os testes usavam URL em formato inexistente (`/2026-08-07/slug` com hífens; o real é `/2026-08-07/slug`). O site serviu leitores normalmente o dia todo (22.852×200 no log; a própria matéria do Irã 200 às 13:13). Estrutura de permalink, rewrite_rules (1743 regras, ordem correta) e caches: tudo íntegro. Intervenções feitas durante o falso diagnóstico (`wp rewrite flush`, purge WP Rocket, DEL notoptions): inócuas/reversíveis.
4. **Observações sem ação:** arquivos de mês/dia sempre foram 404 neste site (até 2011!) — pré-existente; Redis do WP sob pressão de memória (2,78M evictions, maxmemory 256MB) — candidato a ajuste futuro.

## Próximos passos
- Miguel confirmar visualmente título + painel.
- Nada mais pendente deste tema.
