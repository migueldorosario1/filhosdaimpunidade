#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C16_checkPC.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C16.j4_checkPC.stdout"
echo "[$(date '+%F %T')] INICIANDO: check dedicado Projeto Cafezinho (janela 2h)" >> "$OUT"
timeout 7200 rclone check "$WS/Projeto Cafezinho Agentes" "drive:Workspace_Vivo/Projeto Cafezinho Agentes" --checkers 8 --one-way --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO >> "$OUT" 2>&1
RC=$?
echo "[$(date '+%F %T')] FIM CHECK ProjetoCafezinho (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
