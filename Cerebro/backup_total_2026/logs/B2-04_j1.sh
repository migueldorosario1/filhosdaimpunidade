#!/bin/bash
# B2-04 = C04 da FASE 1: ferramentas + backups_livro + mokawriter (3 cópias em sequência na mesma janela)
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-04.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-04.j1.stdout"
FAIL=0
echo "[$(date '+%F %T')] INICIANDO: B2-04 (ferramentas + backups_livro + mokawriter, multi-thread OFF)" >> "$OUT"
for PAR in "ferramentas:ferramentas" "backups_livro:backups_livro" "mokawriter:mokawriter"; do
  SRC="${PAR%%:*}"; DST="${PAR##*:}"
  echo "[$(date '+%F %T')] COPIANDO: $SRC" >> "$OUT"
  timeout 450 rclone copy "/home/migueldorosario/$SRC" "gdrive-backup-b2:backup-total-local-2026/Backup_Total/$DST" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
  RC=$?
  echo "[$(date '+%F %T')] FIM $SRC (rc=$RC)" >> "$OUT"
  [ $RC -ne 0 ] && FAIL=$RC
done
echo "[$(date '+%F %T')] TERMINADO: B2-04 (rc=$FAIL)" >> "$OUT"
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
