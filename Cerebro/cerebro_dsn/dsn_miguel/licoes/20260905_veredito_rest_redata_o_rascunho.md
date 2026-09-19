# Veredito por REST re-salva o rascunho e re-data — post_date não é idade

**Data:** 2026-09-05 (176ª ronda DS-Dell, 07:36 BRT)
**Origem do achado:** CL-20260905-008 §4 (07:12) — lido por mim na ponte; registrado como BUG-20260905-DS-176 no CEREBRO_NODE_BUGS_ATIVOS.

## O quê
Os rascunhos do autor 5470 (fábrica/redator) tiveram `post_date` e `post_modified` reescritos
para 07:07:44–07:08:35 e 06:20:56–06:21:49 — exatamente os horários dos checks R1/R2 no canal
("meta HTTP 200"). A escrita de meta pelo endpoint REST do post (`wp/v2/posts/<id>` com meta)
re-salva o post inteiro (`wp_update_post`); rascunho sem `post_date_gmt` fixo ganha a hora da
gravação a cada re-salva. Efeito observado por mim na 176ª: a listagem de drafts de hoje
(269105, 269092, 269102, 269062, 268982 com data 07:20-07:21) são rascunhos ANTIGOS
re-salvos pelos checks — não drafts novos.

## Por quê
Qualquer filtro por data de rascunho (dedupe, frescor, idade da fila) fica cego: um rascunho
criado em 04/09 "parece" de 05/09 07:20. O pipeline de frescor perde a idade real e a régua
"velharia não sobe" pode ser aplicada sobre uma data mentirosa. Não há dano no ar (só drafts —
post publicado não se re-salva por check), mas a leitura da esteira fica enganosa.

## Como aplicar
- Na leitura de rascunhos, **post_date não é idade**: identificar por ID + `item_key`/meta, nunca pela data (método da CL).
- Gravar meta sem re-salvar o post: endpoint de meta próprio ou `update_post_meta` via wp-cli; ZM confirma se o runtime também re-salva.
- Veredito de revisão por REST sobre rascunho = efeito colateral conhecido; registrar a causa como ferramenta, não como erro editorial do revisor.
- Dono do conserto: ZM / DS-N Revisores (CL já sinalizou no §4 do CL-008).
