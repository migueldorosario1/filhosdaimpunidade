#!/bin/bash
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/B2-14.log"
OUT="$WS/Cerebro/backup_total_2026/logs/B2-14.j1.stdout"
echo "[$(date '+%F %T')] INICIANDO: B2-14 (resto do workspace, 20 pastas -> B2, janela 1, 25 min, multi-thread OFF)" >> "$OUT"
RC_TOTAL=0
copia() {
  local d="$1"
  if [ ! -d "$WS/$d" ]; then
    echo "[$(date '+%F %T')] PULADO (nao existe): $d" >> "$OUT"
    return 0
  fi
  timeout 1500 rclone copy "$WS/$d" "gdrive-backup-b2:backup-total-local-2026/Workspace_Vivo/$d" --transfers 8 --checkers 8 --multi-thread-cutoff 100G --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
  local rc=$?
  echo "[$(date '+%F %T')] pasta $d: rc=$rc" >> "$OUT"
  [ $rc -ne 0 ] && RC_TOTAL=1
}
for d in "scratch" "Rio Carta Agentes" "Global South News" "Kimi K3" "Fontes" "agent_data" "agentes_tematicos" "artes" "backups_ceo_cerebro" "github_work" "artifacts" "Foruns" "Claude" "api" "backups" "deploy_build" "reportagens_para_fazer_depois" "transcritor" "teste_foto_na_hora_20260728" "tmp_v3_remote"; do
  copia "$d"
done
echo "[$(date '+%F %T')] TERMINADO: B2-14 (rc=$RC_TOTAL)" >> "$OUT"
echo "EXIT=$RC_TOTAL" >> "$OUT"
exit $RC_TOTAL
