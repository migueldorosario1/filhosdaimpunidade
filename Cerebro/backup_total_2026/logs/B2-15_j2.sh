#!/bin/bash
# J2: corrige caminho do Dados_Frios (rc=3 da J1 — pasta fica no HOME, fora do workspace)
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-15.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-15.j2.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-15 J2 (Dados_Frios caminho corrigido -> B2, multi-thread OFF)" >> "$OUT"
RC_TOTAL=0
timeout 1500 rclone copy "/home/migueldorosario/Dados_Frios" "gdrive-backup-b2:backup-total-local-2026/Dados_Frios" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "orlando diniz/**" --exclude "Jornais do dia/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] Dados_Frios: rc=$RC" >> "$OUT"
[ $RC -ne 0 ] && RC_TOTAL=$RC
timeout 1500 rclone copy "$WS/Outros/novo livro" "gdrive-backup-b2:backup-total-local-2026/novo livro" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?
echo "[$(date '+%F %T')] novo livro: rc=$RC" >> "$OUT"
[ $RC -ne 0 ] && RC_TOTAL=$RC
echo "[$(date '+%F %T')] TERMINADO: B2-15 J2 (rc=$RC_TOTAL)" >> "$OUT"
echo "EXIT=$RC_TOTAL" >> "$OUT"
exit $RC_TOTAL
