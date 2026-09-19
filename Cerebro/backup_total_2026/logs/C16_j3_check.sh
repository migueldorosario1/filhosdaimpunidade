#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C16_check.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C16.j3_check.stdout"
FAIL=0
echo "[$(date '+%F %T')] INICIANDO: C16 verificação final (rclone check --one-way em todos os destinos da FASE 1)" >> "$OUT"
check() {
  local NOME="$1" SRC="$2" DST="$3"; shift 3
  echo "[$(date '+%F %T')] CHECK: $NOME" >> "$OUT"
  timeout 1500 rclone check "$SRC" "$DST" --checkers 8 --one-way --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" "$@" --log-file "$LOG" --log-level INFO >> "$OUT" 2>&1
  local RC=$?
  echo "[$(date '+%F %T')] FIM CHECK $NOME (rc=$RC)" >> "$OUT"
  [ $RC -ne 0 ] && FAIL=1
}
check "Cerebro" "$WS/Cerebro" "drive:Workspace_Vivo/Cerebro"
check "ProjetoCafezinho" "$WS/Projeto Cafezinho Agentes" "drive:Workspace_Vivo/Projeto Cafezinho Agentes"
check "novoLivro" "$WS/Outros/novo livro" "drive:novo livro"
check "Outros" "$WS/Outros" "drive:Workspace_Vivo/Outros" --exclude "novo livro/**"
echo "[$(date '+%F %T')] TERMINADO: verificação final (fail=$FAIL)" >> "$OUT"
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
