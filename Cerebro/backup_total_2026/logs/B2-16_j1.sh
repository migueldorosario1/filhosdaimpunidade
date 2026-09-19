#!/bin/bash
# B2-16: VERIFICAÇÃO FINAL + TOP-UPS DE PASTAS VIVAS (último chunk da FASE 2)
# Top-ups cirúrgicos (rclone idempotente — só copia o que mudou desde B2-02/B2-11/B2-14):
#   1. ZCodeProject (.vigilia_claude_state.json muda a cada ronda)
#   2. Cerebro (B2-11.log e arquivos vivos)
#   3. scratch (pasta viva, +6 obj/14 MB desde B2-14)
#   4. agent_data (banco do agente de imagens, +1 obj/2,2 MB)
# Depois: verificação rclone size local×B2 dos 4 + relatório.
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-16.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-16.j1.stdout"
DEST="gdrive-backup-b2:backup-total-local-2026"
EXCL="--exclude node_modules/** --exclude __pycache__/** --exclude *.pyc --exclude .Trash*/** --exclude .next/**"
echo "[$(date '+%F %T')] INICIANDO: B2-16 (top-ups pastas vivas + verificação final)" >> "$OUT"
RC_TOTAL=0

echo "=== TOP-UPS ===" >> "$OUT"
# 1. ZCodeProject
timeout 1500 rclone copy "/home/migueldorosario/ZCodeProject" "$DEST/Backup_Total/ZCodeProject" --transfers 8 --checkers 8 --multi-thread-cutoff 100G $EXCL --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; echo "[$(date '+%F %T')] ZCodeProject top-up: rc=$RC" >> "$OUT"; [ $RC -ne 0 ] && [ $RC -ne 6 ] && RC_TOTAL=$RC

# 2. Cerebro
timeout 1500 rclone copy "$WS/Cerebro" "$DEST/Workspace_Vivo/Cerebro" --transfers 8 --checkers 8 --multi-thread-cutoff 100G $EXCL --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; echo "[$(date '+%F %T')] Cerebro top-up: rc=$RC" >> "$OUT"; [ $RC -ne 0 ] && [ $RC -ne 6 ] && RC_TOTAL=$RC

# 3. scratch
timeout 1500 rclone copy "$WS/scratch" "$DEST/Workspace_Vivo/scratch" --transfers 8 --checkers 8 --multi-thread-cutoff 100G $EXCL --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; echo "[$(date '+%F %T')] scratch top-up: rc=$RC" >> "$OUT"; [ $RC -ne 0 ] && [ $RC -ne 6 ] && RC_TOTAL=$RC

# 4. agent_data
timeout 1500 rclone copy "$WS/agent_data" "$DEST/Workspace_Vivo/agent_data" --transfers 8 --checkers 8 --multi-thread-cutoff 100G $EXCL --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
RC=$?; echo "[$(date '+%F %T')] agent_data top-up: rc=$RC" >> "$OUT"; [ $RC -ne 0 ] && [ $RC -ne 6 ] && RC_TOTAL=$RC

echo "" >> "$OUT"
echo "=== VERIFICAÇÃO FINAL (rclone size local × B2) ===" >> "$OUT"
for par in \
  "/home/migueldorosario/ZCodeProject|$DEST/Backup_Total/ZCodeProject" \
  "$WS/Cerebro|$DEST/Workspace_Vivo/Cerebro" \
  "$WS/scratch|$DEST/Workspace_Vivo/scratch" \
  "$WS/agent_data|$DEST/Workspace_Vivo/agent_data"; do
  SRC="${par%%|*}"; DST="${par##*|}"
  LOC=$(rclone size "$SRC" $EXCL 2>/dev/null | grep -E "Total size" | head -1)
  REM=$(rclone size "$DST" 2>/dev/null | grep -E "Total size" | head -1)
  echo "  $SRC:" >> "$OUT"; echo "    local: $LOC" >> "$OUT"; echo "    B2:    $REM" >> "$OUT"
done

echo "[$(date '+%F %T')] TERMINADO: B2-16 (RC_TOTAL=$RC_TOTAL)" >> "$OUT"
echo "EXIT=$RC_TOTAL" >> "$OUT"
exit $RC_TOTAL
