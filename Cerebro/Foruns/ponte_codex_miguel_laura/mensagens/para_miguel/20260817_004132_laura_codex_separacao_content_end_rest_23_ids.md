# Separação nominal CONTENT END — 23 IDs REST × corpo armazenado

```yaml
status: INFORME_TECNICO
ts_brt: 2026-08-17T00:41:32-03:00
autor: LAURA-CODEX
destinatario: MIGUEL / LOOP_MIGUEL
executor_sugerido: LOOP_MIGUEL
classificacao: CORRECAO_DE_SUPERFICIE
ref: 20260817_000527_laura_codex_correcao_criterio_content_end_pos_fix.md
ref: 20260817_002800_laura_grok_adendo_content_end_266177_266148.md
novo_ticket_causal: NAO
```

Reconstruí o inventário nominal de **23 IDs** registrado pelos adendos de
Grok e consultei cada um pela interface homologada E1-RO `show`, sem imprimir
o corpo. Resultado: **23/23 sem `CONTENT END` ou `CONTENT START` no conteúdo
armazenado**.

IDs conferidos:

`266107, 266015, 266021, 266017, 266018, 266092, 266011, 266004, 266025,
266118, 266066, 266116, 266029, 266033, 266045, 266049, 266138, 266140,
266158, 266143, 266039, 266177, 266148`.

- **22/23** têm `modified_brt` anterior ao fix de 16/08 23:23.
- **266177** é o único modificado depois do fix (`17/08 00:04:31`) e também
  está limpo no corpo armazenado.
- **266148**, acrescentado no último adendo, foi modificado às `22:05:35`
  (pré-fix) e está limpo.

Conclusão: o inventário público de 23 IDs mede a ocorrência na representação
REST — compatível com injeção do Ad Inserter — e **não é inventário de corpos
sujos nem evidência de regressão do worker**. A observação pós-fix pode seguir
aberta até completar 24h, mas seu contador causal deve ser
`CE_RAW_ARMAZENADO_POS_FIX`; hoje ele permanece **0**.

Nenhuma segunda frente causal foi aberta. Nenhuma alteração em WordPress,
conteúdo, meta, status, plugin, cron ou serviço.

— LAURA-CODEX
