# LAURA-CODEX → Miguel — fix dedup ZCode é parcial, com ganho real

```yaml
tipo: ALERTA_TECNICO
ts_brt: 2026-08-15T05:12:11-03:00
executor_sugerido: ZCODE_COM_REVISAO_CLAUDE
prioridade: MEDIA
ref: ZCODE→CLAUDE-SELF-DUP-FIX-APLICADO-2026-08-15T04:28
```

ZCode corrigiu um defeito real: `per_page=50` cobria cerca de 12 h num portal
com 93 posts/dia; a paginação agora cobre 24 h. O gate já existia pré-LLM, então
essa correção pode evitar custo de geração.

Não considero o caso totalmente homologado. A prova “3/3 temas” agrupou quatro
candidatas; o próprio ACK admite que `265827` não casa diretamente com 265780.
Também faltam teste de dois workers concorrentes, negativos rotulados e ledger
com IDs/chaves, regra, score, estado e outcome — o log anunciado guarda apenas
timestamp e títulos.

Sugestão: manter como `FIX_PARCIAL` até ZCode demonstrar 4/4 candidatas na ordem
temporal real, um teste de corrida e ao menos um `duplicate_blocked` observado em
ciclo normal. Laura não acessou NYC/WordPress e não aplicou mudança.

— LAURA-CODEX
