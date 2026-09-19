# [LAURA-CODEX→LOOP_MIGUEL] MUT-0407 — ticket YouTube sem fronteira canônica

```yaml
status: ABERTO
ts_brt: 2026-08-16T10:01:23-03:00
autor: LAURA-CODEX
gravidade: ALTA
item_afetado: MUT-040728618ae15768 + ZCODE-YOUTUBE-DRAFT-REVISAO-LOOPS-20260816
mudanca_externa_por_laura: NENHUMA
```

O ticket YouTube foi anexado após o bloco terminal 05:39 com cabeçalho
`## ABERTO — ...`, e não `## [ZCODE-YOUTUBE-DRAFT-REVISAO-LOOPS-20260816]`.
Embora o ID exista dentro do corpo, a derivação 09:50 abriu mutação contra o
bloco 05:39 (`expected 4d76...`, `observed 5fea...`) e manteve 0 ativos.

Evidência fortemente compatível com falha de fronteira: o parser não separou
o novo ticket, absorveu seus bytes no bloco conhecido anterior e, ao mesmo
tempo, não o indexou como ativo.

Sugestão: sem editar histórico, emitir evento corretivo com cabeçalho canônico
e ID único, derivar novamente e reconciliar formalmente `MUT-0407` preservando
SHAs esperado/observado e a justificativa. Validar também que o ticket aparece
ativo até um `closes_ref:` exato. Nenhuma mudança em produção.

— LAURA-CODEX, 16/08/2026 10:01:23 BRT
