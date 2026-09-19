#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-07.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-07.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-07 (casadamoeda×4 -> B2, janela 1, multi-thread OFF)" >> "$OUT"
RC_TOTAL=0
copia() {
  timeout 1500 rclone copy "$1" "$2" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
  RC=$?
  echo "[$(date '+%F %T')]   origem '$(basename "$1")' rc=$RC" >> "$OUT"
  [ $RC -ne 0 ] && RC_TOTAL=$RC
}
copia "$WS/casadamoeda" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/casadamoeda"
copia "$WS/casadamoeda-lab" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/casadamoeda-lab"
copia "$WS/casadamoeda_backup_estavel" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/casadamoeda_backup_estavel"
copia "$WS/casadamoeda_backup_20260729.tar.gz" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/casadamoeda_backup_20260729.tar.gz"
echo "[$(date '+%F %T')] TERMINADO: B2-07 (rc=$RC_TOTAL)" >> "$OUT"
echo "EXIT=$RC_TOTAL" >> "$OUT"
exit $RC_TOTAL
