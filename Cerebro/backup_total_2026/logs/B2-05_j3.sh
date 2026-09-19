#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-05.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-05.j3.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-05 (legacy -> B2, janela 3, 25 min, multi-thread OFF)" >> "$OUT"
timeout 1500 rclone copy "/home/migueldorosario/legacy" "gdrive-backup-b2:backup-total-local-2026/Backup_Total/legacy" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: B2-05 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
