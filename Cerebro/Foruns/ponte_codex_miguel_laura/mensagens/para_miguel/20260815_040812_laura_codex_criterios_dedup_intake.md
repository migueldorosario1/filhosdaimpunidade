# [LAURA-CODEX→MIGUEL] Critérios seguros para dedup do intake V4

```yaml
status: ABERTO
ts_brt: 2026-08-15T04:08:12-03:00
autor: LAURA-CODEX
destinatario: MIGUEL
prioridade: MEDIA
tipo: ALERTA_TECNICO
ref: loop_trindade_laura/mensagens/codex/20260815_040812_codex_ronda_010.md
executor_sugerido: ZCODE/MIGUEL
```

O ticket 03:35 identifica corretamente self-dup como problema maior, mas o
snippet conceitual ainda tem riscos:

- diz título+lead, porém compara só título;
- omite posts `future`;
- se usa título gerado, não economiza a chamada LLM já feita;
- check-then-act sem reserva permite duplicata por concorrência;
- Jaccard 0,50 sem avaliação pode bloquear pautas distintas do mesmo tema.

Antes de ativar `SKIP`, sugiro exigir chave canônica/reserva atômica pré-LLM,
similaridade pós-LLM, inclusão de future, ledger explicável, amostra rotulada,
teste de corrida e rollback/override. Isso transforma heurística em barreira
idempotente auditável.

Laura não alterou o worker nem acessou NYC/WordPress.

— LAURA-CODEX, 15/08/2026 04:08 BRT
