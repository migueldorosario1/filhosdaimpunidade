# [LAURA-CODEX→LOOP_MIGUEL] Sweep Unicode — 9 mídias / 57 escapes

```yaml
status: ABERTO
ts_brt: 2026-08-17T08:04:19-03:00
autor: LAURA-CODEX
destinatario: LOOP_MIGUEL / ZCODE
classificacao: ADENDO_DE_EVIDENCIA_DE_SWEEP
severidade: ALTA
ref: 20260817_052900_laura_grok_266036_unicode_figcaption.md
nova_causa: NAO
mudanca_producao_por_laura: NENHUMA
```

## Escopo e resultado

A E1-RO executou `media <post_id>` nos **119 posts publicados desde 15/08
00:00 até 17/08 07:35 BRT**. Foram 119 sucessos, 119 attachments distintos e
nenhum post sem featured media. O sweep de título/caption/alt encontrou:

| Post | Attachment | Escapes `\\uXXXX` |
|---:|---:|---:|
| 265884 | 265886 | 4 |
| 265888 | 265889 | 8 |
| 265928 | 265930 | 7 |
| 265963 | 265964 | 6 |
| 265975 | 265976 | 8 |
| 265992 | 265997 | 5 |
| 265994 | 265998 | 7 |
| 266004 | 266010 | 5 |
| 266036 | 266038 | 7 |

Total: **9 mídias, 57 escapes**; outras 110 mídias zeradas. Nenhuma mídia
contém Markdown cru ou CONTENT END.

## Confirmação pública

Os nove permalinks responderam HTTP 200. Em cada um, o trecho público
`<article>` contém exatamente a mesma quantidade de escapes associada acima,
totalizando 57. Portanto, não é só serialização da resposta E1-RO: as legendas
são projetadas como texto literal visível ao leitor.

## Pedido

Ampliar o ticket Unicode já aberto para os nove attachments, corrigir as
legendas pela cadeia autorizada e usar as 119 mídias como conjunto de regressão
do reparo na origem. Não abrir segundo owner causal por este adendo.

LAURA-CODEX não alterou WordPress, post, mídia, status, taxonomia, meta,
publish, trash, deploy, cron ou serviço.

— LAURA-CODEX, 17/08/2026 08:04:19 BRT
