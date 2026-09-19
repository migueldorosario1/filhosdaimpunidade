#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-02.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-02.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-02 (ZCodeProject -> B2, janela 25 min, multi-thread OFF)" >> "$OUT"
timeout 1500 rclone copy "/home/migueldorosario/ZCodeProject" "gdrive-backup-b2:backup-total-local-2026/Backup_Total/ZCodeProject" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: B2-02 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
