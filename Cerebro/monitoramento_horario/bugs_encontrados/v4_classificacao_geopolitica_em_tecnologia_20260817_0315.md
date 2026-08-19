# V4-CLASSIFICACAO — Geopolítica (China etc.) entrando no bloco TECNOLOGIA (aviso Miguel 17/08)

**Tag:** V4-CLASSIFICACAO
**Achado por:** ZCode (DeepSeek via failover) — aviso direto do Miguel: "matérias de geopolítica sobre a china, no bloco tecnologia, que deveriam estar no geopolítica"
**Status:** 🟡 CONTIDO (15 posts recentes recategorizados + causa mapeada) — fix de gate pendente com o dono do intake (NYC)

## Sintoma

Posts claramente geopolíticos aparecendo no bloco Tecnologia da home (canônico E espelho):
"Xi Jinping lidera homenagem ao centenário de Jiang Zemin", "China debate usar navios civis em
conflitos armados", "Disputa de narrativas expõe impasse geopolítico entre China e Índia",
"China protesta contra visita de ministros japoneses ao santuário de Yasukuni" etc.

## Causa

O vertical `ciencia` do V4 (NYC `v4_vertical_draft_worker.py`, cfg category_ids **[735, 5008, 30]**)
recebe pautas do estoque "tecnologia" sem reclassificação. O gate do intake
(`v4_vertical_intake.py::technology_geopolitical_score`, exigência ≥4) aceita artigo SEM termo de
tecnologia no TÍTULO quando `reported_nexus = (title_tech OR title_geo) AND body_tech AND body_geo AND mechanisms`
— o corpo de qualquer pauta militar/geopolítica menciona "satélites/drones/mísseis/IA" e passa
(mecanismos + termo tech incidental). Resultado: pauta de geopolítica pura vira "Tecnologia".
O guard de precedência (Tecnologia sobrepõe) NÃO ajuda aqui: o post nunca recebeu 5003.

## O que JÁ foi feito (ZCode, 17/08 ~03:10)

1. **15 posts recentes (09-17/08) recategorizados** canônico+espelho: 266204, 266121, 266150,
   265947, 265651, 265107, 265079, 265030, 264963, 264842, 264805, 264638, 264557, 264462, 264093
   → `category 5003` (Geopolítica) + `_yoast_wpseo_primary_category=5003`. Espelho: 11 aplicados
   direto + 4 chegam corretos no próximo sync.
2. **Acidente corrigido:** `wp post term set` sem `--by=id` criou a categoria fantasma "5003"
   (id 21158) — apagada, posts refeitos com `--by=id`.
3. Bloco Tecnologia verificado limpo dos 15 (canônico REST + espelho REST + cache flush).

## Pendente (dono do intake = NYC; arquivo ocupado pela sessão V4 TENDÊNCIAS)

1. **Gate:** exigir termo TECH no TÍTULO (`title_tech > 0`) para aceitar na seção tecnologia —
   mata a classe "geopolítica pura" sem rejeitar "painel solar chinês". Alternativa: rotear
   pauta com geo alto/tech baixo para o banco `geopolitica.sqlite3`.
2. **Batch histórico:** lista de candidatos de julho/ago (262407, 262412, 262429, 262458, 262654,
   262739, 262819, 263153, 263703, 265220...) — aplicar a mesma recategorização após o "vai" do
   Miguel (critério = geopolítica pura, sem tech no título).
3. Conferir queries do coletor `estoque_tecnologia.json` (Tencent) — se a fonte já mistura feeds
   de geopolítica, estreitar lá também.

## Lição

Gate semântico baseado só no CORPO é frágil: vocabulário militar/geopolítico ("drones",
"mísseis", "IA") casa com o dicionário tech. Exigir o nexo no TÍTULO é o controle mais barato
e mais preciso. E wp-cli `term set` interpreta o argumento como SLUG por padrão — usar
`--by=id` sempre (custou uma categoria fantasma).

**ADENDO 18/08 ~13:50 — GATE APLICADO (fecha o item Pendente 1):** o gate `title_tech > 0` foi implementado em `v4_vertical_intake.py` (reason `missing_tech_term_in_title`, com dobra de acentos via `_fold`) junto com o gate-espelho da geopolitica (veto `off_theme_title_veto`). Ver `forum_v4_gate_tema_geopolitica_tecnologia_20260818.md`. O batch histórico (item 2) segue aguardando o "vai" do Miguel.
