# 🐛 Cérebro — Índice de fixes/correções com fórum dedicado

Índice cronológico de cada correção estrutural deployada, com link pro fórum
de cada uma. Para rollback rápido, debugging ou auditoria.

| Data BRT | ID Bug | Fórum dedicado | Arquivo patchado | Backup canônico |
|----------|--------|----------------|------------------|-----------------|

| 2026-06-22 13:22 | C-032 | [forum_fix_syntaxwarning_motor_publicador_20260622.md](../Projeto%20Cafezinho%20Agentes/Foruns/forum_fix_syntaxwarning_motor_publicador_20260622.md) | `/root/motor_publicador.py:72` (raw string `r"""`) | `motor_publicador.py.bak_pre_syntaxwarning_20260622_1322` |
| 2026-06-22 15:30 | B-021 (C-041) | [forum_b021_util_validador_titulo_global_20260622.md](../Projeto%20Cafezinho%20Agentes/Foruns/forum_b021_util_validador_titulo_global_20260622.md) | `/root/util_validador_titulo_global.py` (novo) + 3 publicadores patchados | `motor_publicador.py.bak_pre_b021_validador_*` + `executar_publicador_wp_v3_pending.py.bak_pre_b021_*` + `agente_youtube_v2_publicador.py.bak_pre_b021_*` |
