# Classificação CONTENT END — 266150 é REST injetado, corpo limpo pré-fix

```yaml
status: INFORME_TECNICO
ts_brt: 2026-08-17T01:13:06-03:00
autor: LAURA-CODEX
destinatario: MIGUEL / LOOP_MIGUEL
classificacao: ADENDO_DE_SUPERFICIE
post_id: 266150
ref: 20260817_005800_laura_grok_adendo_content_end_266150.md
ref: 20260817_004132_laura_codex_separacao_content_end_rest_23_ids.md
novo_ticket_causal: NAO
```

E1-RO `show 266150` confirma:

- `modified_brt=2026-08-16 22:06:26` — anterior ao fix de 23:23;
- conteúdo armazenado sem `CONTENT END` e sem `CONTENT START`;
- status atual `publish`.

Logo, a ocorrência `CE REST=1` registrada às 00:57 é compatível com a
superfície REST injetada pelo Ad Inserter e **não é regressão do worker**. O
inventário passa a:

- `CE_REST_INJETADO=24`;
- corpos armazenados conferidos e limpos: **24/24**;
- `CE_RAW_ARMAZENADO_POS_FIX=0`;
- único ID do inventário com modificação pós-fix: 266177, também limpo.

Sem segundo ticket causal e sem alteração no WordPress.

— LAURA-CODEX
