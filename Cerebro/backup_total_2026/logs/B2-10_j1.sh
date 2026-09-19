#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-10.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-10.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-10 (Cicero Agentes -> B2, janela 1, 25 min, multi-thread OFF)" >> "$OUT"
timeout 1500 rclone copy "$WS/Cicero Agentes" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/Cicero Agentes" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: B2-10 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
