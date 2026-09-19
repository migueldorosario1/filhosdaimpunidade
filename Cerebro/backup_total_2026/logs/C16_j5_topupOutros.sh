#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C16.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C16.j5.stdout"
echo "[$(date '+%F %T')] INICIANDO: C16 top-up Outros (churn pós-C13)" >> "$OUT"
timeout 1500 rclone copy "$WS/Outros" "drive:Workspace_Vivo/Outros" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "pautas editoriais o cafezinho/**" --exclude "Jornais do dia/**" --exclude "novo livro/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: top-up Outros (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
