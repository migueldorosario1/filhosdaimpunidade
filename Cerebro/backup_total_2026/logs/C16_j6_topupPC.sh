#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C16.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C16.j6.stdout"
echo "[$(date '+%F %T')] INICIANDO: C16 top-up Projeto Cafezinho (churn pós-C06, janela longa 2h)" >> "$OUT"
timeout 7200 rclone copy "$WS/Projeto Cafezinho Agentes" "drive:Workspace_Vivo/Projeto Cafezinho Agentes" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: top-up Projeto Cafezinho (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
