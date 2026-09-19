#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-01.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-01.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-01 pautas editoriais → B2 (janela 1)" >> "$OUT"
timeout 1500 rclone copy "$WS/Outros/pautas editoriais o cafezinho" "gdrive-backup-b2:backup-total-local-2026/pautas editoriais o cafezinho" --transfers 8 --checkers 8 --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: B2-01 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
