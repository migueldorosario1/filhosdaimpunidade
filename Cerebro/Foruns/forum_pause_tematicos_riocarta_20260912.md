# Fórum — Pause dos temáticos (só Rio Carta ativo) — ZM-20260912-001

**Data:** 12/09/2026 ~19:0x-19:1x BRT · **Ator:** ZCode/Kimi K3 (Dell) · **Estado: EXECUTADO — temáticos pausados no NYC; Rio Carta segue publicando.**

## Ordem do Miguel (12/09 ~18:5x, chat, sem prefixo → só chat)

"Sabe se os temáticos estão ativos, gastando token? Se estiverem, deixe todos desligados... nada gastando token pelos sites temáticos. Deixa apenas o rio carta. Os outros você pode deixar pausados." + "vai".

## Diagnóstico (antes de agir)

- Dell/Tencent: nenhum cron ou processo de temáticos (logs sem vida hoje).
- NYC: 6 disparadores gastando token — orquestrador --all (8 sites: aiatolah, ceara, discoverbrazil, globalsouth, mapario, mundotrilhos, railpost, riocarta) diário 12h; mapario --so-youtube ter/sáb 9h; aiatolah --so-youtube dom 9h; cicero_robo_coleta a cada 2h; youtube_v2_pipeline 11h/17h; espelho GSN→Cafezinho 12h/18h.
- Já pausados antes (plano mínimo 11/09): dsn_*, cafezinho_hourly, v41/v42, alimentador_yt — intactos.

## Ações (reversíveis, com backup)

1. Backup crontab: /root/crontab_backup_pre_pause_tematicos_20260912_HHMM.txt (212 linhas).
2. Flag nativa: /root/controles_pause/cicero_tematicos.pause (113b) — cron 25 */2 sai em silêncio.
3. Crontab editado (5 linhas, 199 preservadas, diff conferido): orquestrador --all --sem-youtube → COMENTADO e substituído por --site riocarta --sem-youtube (Rio Carta diário 12h VIVO); comentados com etiqueta # PAUSADO_TEMATICOS_20260912_ZM: mapario --so-youtube, aiatolah --so-youtube, youtube_v2_pipeline.sh, agente_youtube_v2_espelho.
4. Conferência pós: crontab mostra riocarta ativo + 5 linhas etiquetadas.

## Estado final

- VIVO: Rio Carta (orquestrador --site riocarta, diário 12h, coleta+produção+publicação, sem-youtube).
- PAUSADO: aiatolah, ceara, discoverbrazil, globalsouth, mapario, mundotrilhos, railpost (via corte do --all) + cicero coleta 2h + pipeline GSN 11/17h + espelho GSN 12/18h.
- Não tocado (não é temático): produção Cafezinho mínimo (7/19h + 13h economia), vigílias, autocura, auditor_titulos etc.
- Religa: apagar cicero_tematicos.pause + descomentar as 5 linhas (backup datado disponível).

## O que falta

Nada nesta missão. Observar na próxima vigília: consumo de token cai a partir de 13/09 (ciclo diário 12h de 13/09 já roda só riocarta).
