#!/usr/bin/env bash
# ============================================================================
# manutencao_cerebro.sh — Manutenção quinzenal do Cérebro (SÓ O SEGURO)
# ----------------------------------------------------------------------------
# Criado: 14/08/2026 (ZCode GLM-5.2 — sprint organização do Cérebro)
# Agenda: 0 5 1,15 * *  (crontab do usuário — dias 1 e 15, 05:00 BRT)
# Fórum:  Foruns/forum_organizacao_cerebro_manutencao_regular_20260814.md
#
# PRINCÍPIOS (faxina canônica — Memorias/memoria_missao_faxina_diaria_legacy_20260811.md):
#   • NUNCA apaga nada — só move para quarentena/Backups (com log de movimentação)
#   • Regra dos 15 dias: item ≤15d é intocável; >15d vira CANDIDATO (só relata)
#   • Retirada dupla obrigatória: mover no Cérebro E remover no repo cerebro-miguel
#     (o rsync */15 repo→Cérebro re-traz o que só sair do vivo — se o push falhar,
#     o script DESFAZ o move local; nada se perde)
#   • Destrutivos (descer quarentena p/ B2, limpar quarentena) = SÓ com "vai" do Miguel
#
# O QUE FAZ SOZINHO (idempotente):
#   1. Snapshots MONITORAMENTO_DE_TRABALHO_YYYY_MM_DD_*.md da raiz → Backups/monitoramentos_arquivados/
#   2. MEMORIA/ legada: .md avulsos → Memorias/ (se voltarem a aparecer)
#   3. Redirecionador MEMORIA/_MOVIDO_PARA_Memorias.md: recolhe após 14 dias de idade
#   4. RELATÓRIO: candidatos >15d (raiz), tamanho de logs append-only, tamanho total
#      → Relatos/manutencao_cerebro_YYYYMM.md + aviso curto no Telegram
# ============================================================================
set -u
CER="/home/migueldorosario/Downloads/Antigravity Google/Cerebro"
REPO="/home/migueldorosario/cerebro-miguel"
REPO_CER="$REPO/cerebro"
PONTE="/home/migueldorosario/Downloads/Antigravity Google/ponte_cafezinho/ponte_cafezinho.py"
HOJE=$(date +%Y%m%d_%H%M)
DATA_ISO=$(date '+%Y-%m-%d %H:%M')
Q="$CER/_organizacao_cerebro_$HOJE"   # quarentena desta rodada (só se mover algo)
REL="$CER/Relatos/manutencao_cerebro_$(date +%Y%m).md"
LIMITE_DATA=$(date -d '15 days ago' +%s)
MOVI=0; AVISOS=""; CANDIDATOS=""; CAND_N=0

log() { echo "[$(date '+%H:%M:%S')] $*"; }

repo_commit_push() {  # retorna 0 se push OK
  cd "$REPO" || return 1
  git add -A >/dev/null 2>&1
  git commit -m "manutencao cerebro automatica $HOJE: $1" --quiet >/dev/null 2>&1
  git push origin main >/dev/null 2>&1 && return 0
  git pull --rebase --autostash --quiet >/dev/null 2>&1
  git push origin main >/dev/null 2>&1
}

retirada_dupla() {  # $1=origem absoluta no Cérebro  $2=destino absoluto  $3=rótulo
  local origem="$1" destino="$2" rotulo="$3"
  local nome; nome=$(basename "$origem")
  mkdir -p "$(dirname "$destino")" "$Q"
  mv "$origem" "$destino" 2>/dev/null || { AVISOS+="⚠️ falha ao mover $nome; "; return 1; }
  rm -f "$REPO_CER/${origem#"$CER"/}"   # mesma retirada no repo espelho
  if repo_commit_push "$rotulo"; then
    MOVI=$((MOVI+1)); log "→ $nome ($rotulo)"
    echo "$(date -Is) | $origem | -> $destino | $rotulo" >> "$Q/MOVIMENTADOS.log"
  else
    mv "$destino" "$origem" 2>/dev/null   # DESFAZ: push falhou, rsync traria de volta
    AVISOS+="⚠️ push falhou — $nome mantido no lugar (nada perdido); "
  fi
}

mkdir -p "$CER/Relatos"
touch "$REL"
cd "$CER" || exit 1

# ── 1. Snapshots de monitoramento soltos na raiz ──
for f in MONITORAMENTO_DE_TRABALHO_20*_*_*.md; do
  [ -f "$f" ] || continue
  retirada_dupla "$CER/$f" "$CER/Backups/monitoramentos_arquivados/$f" "snapshot monitoramento → Backups"
done

# ── 2. MEMORIA/ legada (se algum .md voltar a nascer lá) ──
if [ -d "$CER/MEMORIA" ]; then
  while IFS= read -r -d '' f; do
    retirada_dupla "$f" "$CER/Memorias/$(basename "$f")" "MEMORIA legada → Memorias"
  done < <(find "$CER/MEMORIA" -maxdepth 1 -name "*.md" ! -name "_MOVIDO*" -type f -print0)
  # 3. Redirecionador expirado (>14d)
  REDIR="$CER/MEMORIA/_MOVIDO_PARA_Memorias.md"
  if [ -f "$REDIR" ] && [ "$(stat -c %Y "$REDIR")" -lt "$(( $(date +%s) - 14*86400 ))" ]; then
    retirada_dupla "$REDIR" "$Q/MEMORIA_redirecionador/_MOVIDO_PARA_Memorias.md" "redirecionador MEMORIA expirado → quarentena"
  fi
fi

# ── 4. Relatório: candidatos >15d na raiz (SÓ LISTA — mover exige 'vai') ──
while IFS= read -r -d '' f; do
  [ "$(stat -c %Y "$f")" -lt "$LIMITE_DATA" ] || continue
  case "$f" in
    "$CER"/MONITORAMENTO_DE_TRABALHO.md|"$CER"/MEMORY.md|"$CER"/00_CEREBRO_CANONICO.md) continue;;
  esac
  CANDIDATOS+="- ${f#"$CER"/} (mod. $(date -r "$f" '+%d/%m')); "
  CAND_N=$((CAND_N+1))
done < <(find "$CER" -maxdepth 1 -name "*.md" -print0)

# Logs append-only (monitorar crescimento)
# NOTA/limitação conhecida: arquivos com mtime 29/07 01:0x herdaram a data da
# migração em massa (não edição real) e aparecem como candidatos — decisão final
# é sempre do Miguel; candidato ≠ autorização.
ATZ_LINHAS=$(wc -l < CEREBRO_NODE_ATUALIZACOES.md 2>/dev/null || echo 0)
CANAL_KB=$(du -sk Foruns/canal_trindade.md 2>/dev/null | cut -f1 || echo 0)
TOTAL=$(du -sh "$CER" 2>/dev/null | cut -f1)
RAIZ_MD=$(find "$CER" -maxdepth 1 -name "*.md" | wc -l)

# ── 5. Escreve relatório ──
{
echo ""
echo "## Rodada $DATA_ISO (automática)"
echo "- Cérebro: **$TOTAL** · .md na raiz: $RAIZ_MD · ATUALIZACOES: ${ATZ_LINHAS} linhas · canal_trindade: ${CANAL_KB}KB"
echo "- Movidos nesta rodada: $MOVI"
echo "- Candidatos >15d (aguardam 'vai' do Miguel): ${CANDIDATOS:-nenhum}"
echo "- Avisos: ${AVISOS:-nenhum}"
} >> "$REL"

# ── 6. Telegram (sem segredos) ──
EMOJI="🟢"; [ "$CAND_N" -gt 0 ] && EMOJI="🟡"; [ -n "$AVISOS" ] && EMOJI="🟠"
MSG="$EMOJI Manutenção do Cérebro ($DATA_ISO): $MOVI movidos · total $TOTAL · candidatos>15d: $CAND_N · detalhe em Cerebro/Relatos/manutencao_cerebro_$(date +%Y%m).md"
if [ -f "$PONTE" ]; then python3 "$PONTE" --send "$MSG" >/dev/null 2>&1 || true; fi
log "$MSG"

# ── 7. Sync imediato Cérebro→repo (PROTEÇÃO ANTI-REGRESSÃO: o rsync */15
#      repo→Cérebro regredi arquivos cuja edição ainda não chegou ao repo) ──
if [ -f "$REPO/scripts/sync_cerebro_to_github.py" ]; then
  ( cd "$REPO" && CEREBRO_DRY_RUN=0 /usr/bin/python3 scripts/sync_cerebro_to_github.py >/dev/null 2>&1 ) \
    && log "sync Cérebro→repo OK (anti-regressão)" \
    || AVISOS+="⚠️ sync final falhou — rodar manualmente; "
fi
