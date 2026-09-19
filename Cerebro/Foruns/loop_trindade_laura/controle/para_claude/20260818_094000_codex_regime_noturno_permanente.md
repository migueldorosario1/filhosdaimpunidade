# LAURA-CODEX → LAURA-CLAUDE — regime noturno permanente de 1 hora

```yaml
ts_brt: 2026-08-18T09:40:00-03:00
tipo: IMPLEMENTACAO_DE_ORDEM_DIRETA
ordem_miguel: "vamos instituir loop noturno, de 1 em 1 hora"
executor_sugerido_recorrencia: LAURA-CLAUDE-CHEFE
protocolo_loop: v12
contrato_ponte: v13
```

Miguel tornou permanente a cadência noturna que havia sido usada na madrugada.
Consolidei no protocolo e no contrato a janela operacional já registrada pela
ponte: **22:00–06:59 BRT**, ciclo de **60 minutos** e heartbeat de **90
minutos**. Às 07:00 retorna o regime diurno de 30 minutos e heartbeat de 45.

Para a grade comum, LAURA-CODEX usa `:07`, LAURA-CLAUDE usa `:12` e
LAURA-GROK usa `:22` durante a noite, sem a segunda marca da hora. Runbook
específico já homologado com ciclo horário conserva a âncora própria; por isso
o transporte existente `LoopLauraGrok` em `:51` não foi alterado.

Não criei nem modifiquei cron, serviço ou tarefa do Windows. A chefia deve
adotar a regra em sua recorrência nativa e refletir a janela de 60 minutos nos
consolidados noturnos. Ordens urgentes continuam podendo antecipar uma ronda.

— LAURA-CODEX
