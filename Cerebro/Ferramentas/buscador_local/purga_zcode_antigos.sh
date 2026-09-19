#!/usr/bin/env bash
# Purga ZCode >14d — ordem Miguel 08/09 ("ZCode levinho, antigos na nuvem, 2 backups")
# Fail-closed: só apaga local após upload DUPLO (GDrive+B2) com readback sha256.
# A passphrase NUNCA é impressa (alias ZM_ZCODE_ANTIGOS_PASSPHRASE nos cofres).
set -euo pipefail
LOG=/tmp/zcode_antigos_purga.log
exec > >(tee -a "$LOG") 2>&1
DIA=$(date +%Y%m%d)
# PACOTE com carimbo HHMMSS: reexecução no MESMO DIA não sobrescreve o pacote já enviado à nuvem
# (lição 08/09 20:4x: 2ª corrida sobrescreveu o tar da 1ª no GDrive+B2; resgatado via --b2-versions e reancorado como _run1709)
PACOTE="zcode_antigos_${DIA}_$(date +%H%M%S)"
ZCLI="$HOME/.zcode/cli"
COFRE1="/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/.env.unificado"
COFRE2="/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/agentes_labs/.env.unificado"
GD="gdrive:Backup_Total/dell_faxina/zcode/"
B2="b2:failover-cafezinho1/faxina/zcode-dell/antigos/"

echo "=== 1. passphrase (cofres, Regra №4) ==="
if grep -q '^ZM_ZCODE_ANTIGOS_PASSPHRASE=' "$COFRE1" 2>/dev/null; then
  PASS=$(grep '^ZM_ZCODE_ANTIGOS_PASSPHRASE=' "$COFRE1" | head -1 | cut -d= -f2-)
  echo "reuso: alias já existe no cofre1"
else
  PASS=$(openssl rand -hex 32)
  cp "$COFRE1" "$COFRE1.bak_pre_zcode14d_$DIA"
  cp "$COFRE2" "$COFRE2.bak_pre_zcode14d_$DIA"
  printf '\n# ZCode Dell: passphrase do tar artifacts/exec >14d na nuvem (08/09/2026, ZM)\nZM_ZCODE_ANTIGOS_PASSPHRASE=%s\n' "$PASS" >> "$COFRE1"
  printf '\n# ZCode Dell: passphrase do tar artifacts/exec >14d na nuvem (08/09/2026, ZM)\nZM_ZCODE_ANTIGOS_PASSPHRASE=%s\n' "$PASS" >> "$COFRE2"
  echo "nova passphrase gerada + espelhada nos 2 cofres (backups .bak_pre_zcode14d_$DIA)"
fi

echo "=== 2. tar dos >14d (artifacts + exec) ==="
cd "$ZCLI"
find artifacts exec -type f -mtime +14 > /tmp/zcode_antigos_lista.txt
N=$(wc -l < /tmp/zcode_antigos_lista.txt); echo "arquivos >14d: $N"
if [ "$N" -eq 0 ]; then echo "nada >14d — nada a fazer"; exit 0; fi
tar czf "/tmp/$PACOTE.tar.gz" -T /tmp/zcode_antigos_lista.txt
SZ=$(stat -c%s "/tmp/$PACOTE.tar.gz"); echo "tar: $SZ bytes"

echo "=== 3. gpg AES256 + manifesto + sha256 ==="
gpg --batch --yes --symmetric --cipher-algo AES256 --passphrase "$PASS" \
    -o "/tmp/$PACOTE.tar.gz.gpg" "/tmp/$PACOTE.tar.gz"
GSZ=$(stat -c%s "/tmp/$PACOTE.tar.gz.gpg")
{
  echo "# Pacote $PACOTE — ZCode Dell arquivos >14d"
  echo ""
  echo "- Conteúdo: ~/.zcode/cli/{artifacts,exec} com mtime >14d ($N arquivos, tar $SZ bytes)"
  echo "- Cifra: gpg simétrico AES256; passphrase = alias ZM_ZCODE_ANTIGOS_PASSPHRASE nos cofres .env.unificado (Dell, espelhado)"
  echo "- Destinos: $GD  E  $B2  (backup DUPLO)"
  echo "- Restaurar: rclone copy <dest> /tmp/ && gpg -d $PACOTE.tar.gz.gpg > t.tar.gz && tar xzf t.tar.gz -C ~/.zcode/cli"
  echo "- Gerado por ZM (ZCode Qwen3.8-Max) em 08/09/2026"
  echo ""
  echo "## Lista completa do tar"
  echo '```'
  tar tzf "/tmp/$PACOTE.tar.gz"
  echo '```'
} > "/tmp/${PACOTE}_MANIFESTO.md"
( cd /tmp && sha256sum "$PACOTE.tar.gz.gpg" > "$PACOTE.SHA256SUMS" )
SHA=$(cut -d' ' -f1 "/tmp/$PACOTE.SHA256SUMS"); echo "sha256 local: ${SHA:0:16}…"

echo "=== 4. upload DUPLO (GDrive + B2) ==="
for F in "/tmp/$PACOTE.tar.gz.gpg" "/tmp/$PACOTE.SHA256SUMS" "/tmp/${PACOTE}_MANIFESTO.md"; do
  rclone copy "$F" "$GD" --timeout 300s
  rclone copy "$F" "$B2" --timeout 300s
  echo "upload ok: $(basename "$F")"
done
rclone mkdir "gdrive:Backup_Total/dell_faxina/canais/" --timeout 120s || true

echo "=== 5. verificação: lsf (tamanho) + READBACK sha256 nos 2 destinos ==="
for DEST in "$GD" "$B2"; do
  L=$(rclone lsf "$DEST" --format sp --timeout 120s | grep "$PACOTE.tar.gz.gpg" || true)
  echo "lsf $DEST → $L"
  echo "$L" | grep -q "^${GSZ};" || { echo "🔴 TAMANHO NÃO CONFERE em $DEST — ABORTO (nada apagado)"; exit 1; }
  RB=$(rclone cat "${DEST%/}/$PACOTE.tar.gz.gpg" --timeout 300s | sha256sum | cut -d' ' -f1)
  [ "$RB" = "$SHA" ] || { echo "🔴 READBACK sha NÃO CONFERE em $DEST — ABORTO (nada apagado)"; exit 1; }
  echo "readback $DEST ✅ sha confere"
done

echo "=== 6. poda local (fail-closed satisfeito) ==="
cd "$ZCLI"
xargs -a /tmp/zcode_antigos_lista.txt -d '\n' rm -f --
echo "apagados $N arquivos locais"
rm -f "/tmp/$PACOTE.tar.gz" "/tmp/$PACOTE.tar.gz.gpg" "/tmp/$PACOTE.SHA256SUMS" "/tmp/${PACOTE}_MANIFESTO.md"
du -sh "$ZCLI" | xargs echo "~/.zcode/cli agora:"
# marcador da última poda REAL (a página «Backup e Limpeza» lê p/ data do botão Faxina 2)
mkdir -p "$HOME/.local/share/buscador_local/.marcadores"
date '+%Y-%m-%d %H:%M' > "$HOME/.local/share/buscador_local/.marcadores/purga_zcode"
echo "=== FIM ✅ ==="
