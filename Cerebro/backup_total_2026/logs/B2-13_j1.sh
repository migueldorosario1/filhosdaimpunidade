#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-13.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-13.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-13 (Outros -> B2, janela 1, 25 min, multi-thread OFF, 3 exclusoes do plano)" >> "$OUT"
timeout 1500 rclone copy "$WS/Outros" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/Outros" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "pautas editoriais o cafezinho/**" --exclude "Jornais do dia/**" --exclude "novo livro/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] TERMINADO: B2-13 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
