#!/bin/bash
# C15 janela 1 — Dados_Frios (exclusões do plano: orlando diniz + Jornais do dia) + novo livro
LOG="/home/migueldorosario/Downloads/Antigravity Google/Cerebro/backup_total_2026/logs/C15.log"
OUT="/home/migueldorosario/Downloads/Antigravity Google/Cerebro/backup_total_2026/logs/C15.j1.stdout"
WS="/home/migueldorosario/Downloads/Antigravity Google"
FAIL=0
echo "[$(date '+%F %T')] INICIANDO: Dados_Frios (sem orlando diniz / Jornais do dia)" >> "$OUT"
timeout 1500 rclone copy "/home/migueldorosario/Dados_Frios" "drive:Dados_Frios" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --exclude "orlando diniz/**" --exclude "Jornais do dia/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; [ $RC -ne 0 ] && FAIL=1
echo "[$(date '+%F %T')] TERMINADO: Dados_Frios (rc=$RC)" >> "$OUT"
echo "[$(date '+%F %T')] INICIANDO: novo livro" >> "$OUT"
timeout 1500 rclone copy "$WS/Outros/novo livro" "drive:novo livro" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; [ $RC -ne 0 ] && FAIL=1
echo "[$(date '+%F %T')] TERMINADO: novo livro (rc=$RC)" >> "$OUT"
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
