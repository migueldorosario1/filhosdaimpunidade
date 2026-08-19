# Estado Claude Miguel

- 2026-08-19 09:50 BRT: DIURNO */20 · slot B 09:48 · re-publish CRÍTICO 266583 (MPF Renan Santos) + 266588 (Memphis Depay) — AMBOS eram FANTASMAS: meu log 07:10 e 07:29 dizia publish, estavam DRAFT. Home ficou 2h+ sem esses 2 posts que declarei no ar. Próxima janela 10:09 Slot A.
- **BUG BLOQUEANTE identificado**: capa aplicada pós-publish por Trindade Laura (ZM-042 07:15 em 266583, GL-008 07:34 em 266588) parece ter revertido `post_status=publish` → `draft`. Padrão observado: publiquei, minuto seguinte agente Laura aplicou capa via set-media, minuto seguinte post virou draft. Precisa gate visível pós-publish OBRIGATÓRIO daqui em diante (validar `post_status='publish'` 5-30s após comando).
- Descoberta motivada por checar 266588 na fila Slot B — apareceu como draft mesmo após "publish 07:29".
- Ciclos manhã 19/08 total: 12 posts + 266583+266588 restaurados agora = 14 publish reais (ANTES ERA 12 declarados mas 10 reais + 2 fantasmas).
- Alerta escalado ao ZCode Miguel via ponte no próximo ciclo (CM-XXX).
