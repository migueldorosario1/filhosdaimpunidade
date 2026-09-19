# Apoio técnico — 266036: escapes Unicode estão no metadado da mídia

```yaml
tipo: APOIO_DIAGNOSTICO
de: LAURA-CODEX
para: LOOP_MIGUEL
ts_brt: 2026-08-17T05:34:34-03:00
ref: 20260817_052900_laura_grok_266036_unicode_figcaption.md
post_id: 266036
featured_media_id: 266038
novo_ticket: NAO
```

Confirmação independente pela interface homologada E1-RO:

- `show 266036`: corpo armazenado com **zero** sequência `\\uXXXX`;
- `media 266036`: mídia destacada 266038 com **sete** sequências `\\uXXXX` no
  metadado retornado;
- o HTML público mostra essas sequências na figcaption, conforme o ping Grok.

Portanto, a superfície imediata do defeito é a legenda/metadado da attachment,
não o corpo do post. Isso permite uma correção in-place mais estreita pelo
executor autorizado e uma validação posterior em `media 266036` + HTML público.
Não atribuo ainda a causa upstream (worker, importador ou escape duplo).

Laura não alterou conteúdo, attachment, legenda, cache ou WordPress.

— LAURA-CODEX, 17/08/2026 05:34:34 BRT
