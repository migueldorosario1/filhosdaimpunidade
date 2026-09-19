# MEMÓRIA TÉCNICA — ELEIÇÕES RJ 1: rascunho 270550 (Datafolha Paes 43 × Ruas 25)

> Ordem do Miguel 12/09/2026 ~18:4x: frente de matérias regionais das eleições 2026, começando pelo RJ, 1 matéria, ancorada em Datafolha. Produzida em ZCode/Kimi K3 no Dell.

## Entrega

- **Post 270550** — «Paes mantém 18 pontos de vantagem sobre Ruas, diz Datafolha» (59 chars) — **draft**, autor 5486, excerpt preenchido.
- **Categorias:** Eleições 2026 **5088** + Rio de Janeiro **1656**. Tags: Eduardo Paes, Douglas Ruas, Garotinho, Datafolha, pesquisa eleitoral, eleições 2026, Rio de Janeiro, Ricardo Couto, Benedita da Silva.
- **Capa:** anexo **270551** — MONTAGEM lado a lado (padrão da casa p/ duelos): Paes (Ricardo Stuckert, CC BY-SA 4.0, foto de evento 28/07/2026, via Commons "28.07.2026 - Eduardo Paes (cropped).jpg") × Ruas (TV ALERJ, CC BY 3.0, "Secretário Estadual RJ Douglas Ruas (2).jpg"), faixas com nome+partido, divisor dourado, 2554x1050, PIL. Crédito de AMBAS as fontes na legenda; alt preenchido. Montagem em /tmp/capa_rj_2026.jpg (reutilizável p/ próximas matérias RJ).
- **Métricas:** ~700 palavras, 5 h3, 0 travessões, 0 dois-pontos, 0 "E,/Mas,/Porém,", 15/15 aspas/números validados por grep.

## Números e fatos (ver fórum da frente §3, todos com fonte)

- Datafolha RJ-09217/2026: 1.204 eleitores, campo 8-11/09/2026 (⚠️ g1 diz 8-10; usado 8-11 por 2 fontes: Pulso + CartaCapital), margem 3, conf 95%, contratada Globo+Folha.
- Estimulada: Paes (PSD) 43 (41 ago) × Ruas (PL) 25 (19); Garotinho (Republicanos) 10, barrado pelo TRE-RJ POR UNANIMIDADE em 11/09 (inelegível/direitos suspensos; recorre ao TSE); gap 22→18; válidos 49×28 (21 pts, era 28); espontânea: indecisos 40 (52), Paes 29 (21), Ruas 13 (8); 2º turno 54×34; rejeição Paes 28 (26) e Ruas 23 (19) SUBIRAM pós-TV; guerra da TV: "filhinho de papai"/"príncipe herdeiro de Cláudio Castro" × "Rio da novela"/"Rio real"/"Rio da Madonna"/"Rio das Marias".
- Ruas = presidente da Alerj, filho de Capitão Nelson (prefeito São Gonçalo), atos com presidenciável Flávio Bolsonaro.
- Governador em exercício Ricardo Couto (desembargador, presidente TJ-RJ, 5 meses): aprova 45 (47) / desaprova 34 (31).
- Senado: Benedita da Silva 18%, 5 empatados pela 2ª vaga.

## Armadilhas evitadas (registrar p/ a série)

1. **Não inventar data de início da propaganda na TV** (escrevi "28 de agosto" na 1ª versão e CORRIGI — nenhuma fonte datava; texto final diz só "já está no ar").
2. **Fecho sem conta de padaria**: 1ª versão falava em "turno único" (conceito ERRADO p/ governador, que é maioria em 2 turnos) e ritmo "meio ponto por semana" (conta errada) — reescrito seco.
3. **Benedita**: não afirmar "ex-governadora" sem fonte (só "Benedita da Silva lidera com 18%").
4. Foto TSE oficial (CC BY 4.0) é 161x225 — pequena demais e retrato oficial (manual proíbe); usadas fotos jornalísticas.

## Comandos-chave

- `wp post create /tmp/rj_materia1.html --post_status=draft --post_author=5486 --post_category='5088,1656' ...` → **270550**
- `wp media import /tmp/capa_rj_2026.jpg --post_id=270550 --featured_image --caption=... --alt=...` → **270551**
- Verificado: draft/5486, cats 5088+1656, `_thumbnail_id`=270551.
- Anti-duplicata: `wp post list --s='Datafolha Rio'` conferido antes (sem choque).

## wp-admin

https://www.ocafezinho.com/wp-admin/post.php?post=270550&action=edit

## Estado

- **O que aconteceu:** matéria RJ entregue (rascunho 270550 + capa montada).
- **O que falta:** SP (próxima da fila; conferir Datafolha SP fresca — 247 de 12/09 cita cenários Lula×Flávio em SP/MG/RJ/PE; Metrópoles: Datafolha PE Lyra 47×42 Campos) e o que o Miguel pedir; decidir se frente vira rotina.
- **Controle:** Foruns/forum_eleicoes_regionais_20260912.md (briefing §1, números RJ §3 p/ próxima matéria do estado).
