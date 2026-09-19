#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C16.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C16.j2.stdout"
FAIL=0
echo "[$(date '+%F %T')] INICIANDO: C16 top-up Cerebro (retentativa 2 — pasta viva)" >> "$OUT"
timeout 1500 rclone copy "$WS/Cerebro" "drive:Workspace_Vivo/Cerebro" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
[ $RC -ne 0 ] && FAIL=1
echo "[$(date '+%F %T')] TERMINADO: C16 top-up Cerebro (rc=$RC)" >> "$OUT"
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
