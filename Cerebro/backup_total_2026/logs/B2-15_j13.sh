#!/bin/bash
# J13: Dados_Frios continua (J2 rc=124 normal); novo livro ja fechado rc=0 na J1/J2 — fica fora desta janela
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-15.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-15.j13.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-15 J13 (Dados_Frios -> B2, multi-thread OFF)" >> "$OUT"
timeout 1500 rclone copy "/home/migueldorosario/Dados_Frios" "gdrive-backup-b2:backup-total-local-2026/Dados_Frios" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "orlando diniz/**" --exclude "Jornais do dia/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] Dados_Frios: rc=$RC" >> "$OUT"
echo "[$(date '+%F %T')] TERMINADO: B2-15 J13 (rc=$RC)" >> "$OUT"
echo "EXIT=$RC" >> "$OUT"
exit $RC
