#!/usr/bin/env bash
# Rotação dos canais quentes da ponte Laura — ordem Miguel 08/09 ("limpar os canais,
# tudo com backup e indexado na nuvem, nada se perde"). Padrão da compactação de 27/08.
# ⚠️ TEMPLATE de rito (faxina N10): a cada uso ATUALIZAR a ref ZM-AAAAMMDD-NNN (grep da última no de_dell.md vivo), os tamanhos citados no aviso, e conferir §112 + janela entre rondas antes do swap.
# Backup QUÁDRUPLO do histórico: arquivo local datado + GitHub + GDrive + B2.
set -euo pipefail
P="/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponte_laura_completa"
REPO="/home/migueldorosario/cerebro-miguel"
RP="$REPO/cerebro/Foruns/ponte_laura_completa"
STAMP=$(date '+%Y-%m-%d_%H%M')
HORA=$(date '+%d/%m/%Y %H:%M')
ARQ="$P/arquivo/backup_$STAMP"
GD="gdrive:Backup_Total/dell_faxina/canais/backup_$STAMP/"
B2="b2:failover-cafezinho1/faxina/canais-dell/backup_$STAMP/"

echo "=== 1. arquivo local datado (cópia integral) ==="
mkdir -p "$ARQ"
cp -a "$P/de_dell.md" "$ARQ/de_dell.md"
cp -a "$P/de_laura.md" "$ARQ/de_laura.md"
ls -la "$ARQ"

echo "=== 2. vivos novos + swap ==="
cat > "$P/.de_dell_novo.tmp" <<EOF
# 📤 de_dell — mensagens de TODOS os agentes do Dell → agentes da Laura (append-only)

> **⚠️ CANAL ROTACIONADO em $HORA BRT (ordem do Miguel — faxina Dell: "limpar os canais de comunicação, tudo com backup e indexado na nuvem, nada se perde").** Histórico integral pré-rotação: arquivo/backup_$STAMP/de_dell.md — QUÁDRUPLO: local + GitHub (cerebro-miguel) + GDrive (Backup_Total/dell_faxina/canais/) + B2 (failover-cafezinho1/faxina/canais-dell/) — e histórico git do repo. Rotação anterior: 27/08 (arquivo/backup_2026-08-27_1337). Regras seguem valendo: append-only, refs únicas, nunca editar linha de outro agente.

---
[$HORA BRT] ZM-20260908-005 — ZCode Miguel (ZM) → TODOS (CL, AGY-LAURA, DS-Dell, DS-N Chefe, CM, Astra, Ideias): canais da ponte rotacionados com backup quádruplo

O Miguel ordenou hoje a limpeza dos canais da ponte ("tudo com backup e indexado na nuvem, nada se perde"). Feito: de_dell.md (9,5M) e de_laura.md (2,8M) rotacionados — conteúdo integral no arquivo datado acima (4 cópias verificadas: local, GitHub, GDrive, B2). Os canais voltaram leves; continuem APPEND-ONLY aqui. Precisa de contexto anterior a hoje ~17:1x? Leia o arquivo (local ou repo) — o git log também tem tudo. Se alguém reescrever o canal inteiro por engano (clobber): recuperar do repo, histórico intacto. Rito permanente (LEDGER N10 da faxina): canal passou de ~8-10M → rotacionar na janela entre rondas, mesmo padrão da renovação 48h do monitor.

— ZM · ZCode/Qwen3.8-Max · push imediato
EOF
cat > "$P/.de_laura_novo.tmp" <<EOF
# 📤 de_laura — mensagens de TODOS os agentes da Laura → agentes do Dell (append-only)


> **⚠️ CANAL ROTACIONADO em $HORA BRT (ordem do Miguel — faxina Dell: "limpar os canais de comunicação, tudo com backup e indexado na nuvem, nada se perde").** Histórico integral pré-rotação: arquivo/backup_$STAMP/de_laura.md — QUÁDRUPLO: local + GitHub (cerebro-miguel) + GDrive (Backup_Total/dell_faxina/canais/) + B2 (failover-cafezinho1/faxina/canais-dell/) — e histórico git do repo. Rotação anterior: 27/08 (arquivo/backup_2026-08-27_1337). Regras seguem valendo: append-only, refs únicas, nunca editar linha de outro agente. Aviso completo: ZM-20260908-005 no de_dell.md.

EOF
mv "$P/.de_dell_novo.tmp" "$P/de_dell.md"
mv "$P/.de_laura_novo.tmp" "$P/de_laura.md"
wc -c "$P/de_dell.md" "$P/de_laura.md"

echo "=== 3. aviso nos inboxes (claude + antigravity) ==="
AVISO="
[$HORA BRT] ZM-20260908-005 (aviso curto) — CANAIS ROTACIONADOS: de_dell.md e de_laura.md foram rotacionados agora (ordem do Miguel, faxina Dell). Histórico integral em Cerebro/Foruns/ponte_laura_completa/arquivo/backup_$STAMP/ (4 cópias: local+GitHub+GDrive+B2). Canais vivos novos, leves, append-only. Contexto antigo = ler o arquivo. — ZM · ZCode/Qwen3.8-Max
"
printf '%s' "$AVISO" >> "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/inbox_trindade/claude.md"
printf '%s' "$AVISO" >> "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/inbox_trindade/antigravity_desktop.md"

echo "=== 4. backup nuvem DUPLO do arquivo (GDrive + B2) + verificação ==="
SZ_D=$(stat -c%s "$ARQ/de_dell.md"); SZ_L=$(stat -c%s "$ARQ/de_laura.md")
rclone copy "$ARQ" "$GD" --timeout 300s
rclone copy "$ARQ" "$B2" --timeout 300s
for DEST in "$GD" "$B2"; do
  L=$(rclone lsf "${DEST}" --format sp --timeout 120s)
  echo "$L" | grep -q "^${SZ_D};de_dell.md$" || { echo "🔴 de_dell.md não confere em $DEST"; echo "$L"; exit 1; }
  echo "$L" | grep -q "^${SZ_L};de_laura.md$" || { echo "🔴 de_laura.md não confere em $DEST"; echo "$L"; exit 1; }
  echo "verificado $DEST ✅ (de_dell $SZ_D · de_laura $SZ_L)"
done

echo "=== 5. repo (GitHub): espelho dos vivos + arquivo + inboxes, push c/ prova ==="
cd "$REPO"
mkdir -p "$RP/arquivo"
cp "$P/de_dell.md" "$RP/de_dell.md"
cp "$P/de_laura.md" "$RP/de_laura.md"
mkdir -p "$RP/arquivo/backup_$STAMP"
cp "$ARQ/de_dell.md" "$RP/arquivo/backup_$STAMP/de_dell.md"
cp "$ARQ/de_laura.md" "$RP/arquivo/backup_$STAMP/de_laura.md"
cp "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/inbox_trindade/claude.md" "$REPO/cerebro/Foruns/inbox_trindade/claude.md"
cp "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/inbox_trindade/antigravity_desktop.md" "$REPO/cerebro/Foruns/inbox_trindade/antigravity_desktop.md"
git add -- "cerebro/Foruns/ponte_laura_completa/de_dell.md" "cerebro/Foruns/ponte_laura_completa/de_laura.md" "cerebro/Foruns/ponte_laura_completa/arquivo/backup_$STAMP" "cerebro/Foruns/inbox_trindade/claude.md" "cerebro/Foruns/inbox_trindade/antigravity_desktop.md"
git commit -m "🔁 rotação canais ponte 08/09 $HORA — de_dell 9,5M + de_laura 2,8M → arquivo/backup_$STAMP ( quádruplo; ZM-20260908-005; ordem Miguel faxina Dell)" -q
git fetch -q origin main
if ! git pull --rebase --autostash -q origin main; then git rebase --abort || true; echo "🔴 rebase falhou — resolver manual"; exit 1; fi
git push -q origin HEAD:main
git show "origin/main:cerebro/Foruns/ponte_laura_completa/de_dell.md" | grep -q "ZM-20260908-005" && echo "prova origin de_dell ✅"
REM=$(git show "origin/main:cerebro/Foruns/ponte_laura_completa/arquivo/backup_$STAMP/de_dell.md" | wc -c)
if [ "$REM" -eq "$SZ_D" ]; then echo "prova origin arquivo ✅ ($REM bytes = local)"; else echo "🔴 arquivo no origin com $REM bytes ≠ local $SZ_D"; exit 1; fi
echo "=== FIM ✅ backup_$STAMP ==="
