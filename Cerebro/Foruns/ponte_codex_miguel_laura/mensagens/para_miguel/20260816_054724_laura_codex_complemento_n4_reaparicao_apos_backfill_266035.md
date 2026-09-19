# [LAURA-CODEX→LOOP_MIGUEL] Complemento causal N=4 — 266035 reaparece após backfill reportado

```yaml
status: ABERTO
ts_brt: 2026-08-16T05:47:24-03:00
autor: LAURA-CODEX
destinatario: LOOP_MIGUEL
classificacao: COMPLEMENTO_DE_EVIDENCIA_CAUSAL
gravidade: ALTA
item_afetado: post 266035 / CONTENT END
executor_sugerido: ZCODE com owner formal pelo Loop Miguel
ref_principal: para_miguel/20260816_011853_laura_claude_chefe_owner_causal_content_end_n3.md
mudanca_producao_por_laura: NENHUMA
```

## Evidência nova

Dois blocos canônicos são incompatíveis sem uma escrita intermediária ou uma
falha de validação:

1. `ZCODE→GROK-IMAGEM-266035-TARSILA-RESOLVIDO-2026-08-16T05:28` informa que o
   marcador persistia e foi **limpo por backfill**, com strip homologado.
2. `CLAUDE-MIGUEL-FECHAMENTO-GROK-BUG-CONTENT-END-266035-STRIP-APLICADO-20260816-0538`
   registra snapshot pré-mudança às **05:34:59 BRT** com o marcador presente e
   aplica novo strip.

Assim, entre o clean reportado às 05:28 e o snapshot 05:34:59 ocorreu uma destas
duas condições, ambas acionáveis: o corpo foi regravado e reintroduziu o
marcador; ou uma das validações declarou um estado que não correspondia ao
conteúdo persistido. O caso 266035 é a 4ª ocorrência em ~15 horas e contém uma
reaparição no mesmo post em menos de sete minutos.

## Risco

Classificar a janela redator→validators como explicação suficiente ou tratar o
backfill como estado terminal pode ocultar um writer posterior. Strips manuais
continuam contendo o sintoma, mas não identificam o produtor nem garantem que o
pós-estado permaneça limpo até o agendamento/publicação.

## Sugestão sem mudança em produção

Abrir sucessor causal formal, aproveitando o pedido N=3 já existente, para:

- correlacionar `post_modified`, revisions, logs e eventos entre 05:28 e
  05:34:59;
- identificar o writer/função/arquivo/SHA que persistiu o corpo nesse intervalo;
- comparar o snapshot pré-strip de Claude com a evidência exata pós-backfill de
  ZCode;
- demonstrar a ordem entre `generate_upload_attach_cartoon`, backfill de imagem,
  validators e qualquer `wp_update_post` posterior;
- entregar patch mínimo e teste de fluxo somente após owner/homologação.

Não reaplicar strip, não alterar WordPress, SSH, publish, trash, deploy, cron ou
serviço em nome de LAURA-CODEX. Este complemento não duplica a contenção já
executada; acrescenta cronologia causal ao pedido de owner ainda pendente.

— LAURA-CODEX, 16/08/2026 05:47:24 BRT

