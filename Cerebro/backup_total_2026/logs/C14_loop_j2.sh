#!/bin/bash
# C14 janela 2 (reativação após 5ª morte silenciosa 10:40-10:52) — loop das 20 pastas
# Idempotente: rclone copy pula o que já subiu. Heartbeat por pasta no stdout p/ forense.
WS="/home/migueldorosario/Downloads/Antigravity Google"
LOG="$WS/Cerebro/backup_total_2026/logs/C14.log"
OUT="$WS/Cerebro/backup_total_2026/logs/C14.j2.stdout"
FAIL=0
for d in "scratch" "Rio Carta Agentes" "Global South News" "Kimi K3" "Fontes" "agent_data" "agentes_tematicos" "artes" "backups_ceo_cerebro" "github_work" "artifacts" "Foruns" "Claude" "api" "backups" "deploy_build" "reportagens_para_fazer_depois" "transcritor" "teste_foto_na_hora_20260728" "tmp_v3_remote"; do
  if [ -d "$WS/$d" ]; then
    echo "[$(date '+%F %T')] INICIANDO pasta: $d" >> "$OUT"
    timeout 1500 rclone copy "$WS/$d" "drive:Workspace_Vivo/$d" --transfers 8 --checkers 8 --drive-chunk-size 64M --exclude "node_modules/**" --exclude "__pycache__/**" --exclude "*.pyc" --exclude ".Trash*/**" --exclude ".next/**" --log-file "$LOG" --log-level INFO --stats-one-line --stats 60s
    RC=$?
    [ $RC -ne 0 ] && FAIL=1
    echo "[$(date '+%F %T')] TERMINADA pasta: $d (rc=$RC)" >> "$OUT"
  else
    echo "PULADO (nao existe): $d" >> "$LOG"
    echo "[$(date '+%F %T')] PULADA pasta inexistente: $d" >> "$OUT"
  fi
done
echo "EXIT=$FAIL" >> "$OUT"
exit $FAIL
