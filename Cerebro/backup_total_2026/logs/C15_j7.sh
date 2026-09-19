#!/bin/bash
# C15 janela 2 — só Dados_Frios (novo livro já rc=0 na J1); rclone retoma de onde parou
LOG="/home/migueldorosario/Downloads/Antigravity Google/Cerebro/backup_total_2026/logs/C15.log"
OUT="/home/migueldorosario/Downloads/Antigravity Google/Cerebro/backup_total_2026/logs/C15.j7.stdout"
FAIL=0
echo "[$(date '+%F %T')] INICIANDO: Dados_Frios (retomada J7)" >> "$OUT"
timeout 1500 rclone copy "/home/migueldorosario/Dados_Frios" "drive:Dados_Frios" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "orlando diniz/**" --exclude "Jornais do dia/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; [ $RC -ne 0 ] && FAIL=1
echo "[$(date '+%F %T')] TERMINADO: Dados_Frios (rc=$RC)" >> "$OUT"
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
