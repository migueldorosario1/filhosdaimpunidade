#!/usr/bin/env bash
# ============================================================================
# 🔐 COFRE SSH — segredos SSH criptografados (GPG simétrico, AES-256 + SHA512
# com KDF forte). Ordem do Miguel, 22/08/2026: os segredos SSH vivem cifrados
# em 3 lugares (pendrive físico + GitHub repo Cérebro + Google Drive) e a
# PALAVRA (passphrase) nunca é armazenada em arquivo nenhum — só na cabeça do
# Miguel ou passada a um LLM na sessão (via env COFRE_PASS), e o comando
# `esquecer` apaga os rastros da palavra dos transcripts/históricos.
#
# Comandos:
#   selar            empacota ~/.ssh + senha WP → cifra → espelha nos 3 lugares
#   abrir            decripta para /dev/shm (RAM, não toca disco)
#   fechar           apaga a cópia aberta (shred)
#   verificar        testa a palavra + lista o conteúdo SEM abrir nada
#   trocar-palavra   re-cifra o cofre com uma palavra nova
#   esquecer         COFRE_PASS='...' — remove a palavra dos transcripts/histórico
#   espelhar         copia o blob cifrado p/ pendrive + GDrive (com conferência)
#   status           onde estão os blobs, hashes e frescor
#   sugerir          sugere uma passphrase forte (apenas DECORE, nunca salve)
#   selftest         teste ponta a ponta com chaves FICTÍCIAS (não toca no real)
#
# Fluxo do LLM (ordem do Miguel): o Miguel dá a palavra no chat → o agente roda
#   COFRE_PASS='<palavra>' bash cofre_ssh.sh abrir
#   ...usa o que precisa de /dev/shm/cofre_ssh_aberto/...
#   bash cofre_ssh.sh fechar
#   COFRE_PASS='<palavra>' bash cofre_ssh.sh esquecer   # apaga dos transcripts
# A palavra NUNCA vai para fórum, memória, commit ou arquivo.
# ============================================================================
set -euo pipefail

COFRE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOB="$COFRE_DIR/cofre_ssh_v1.tar.gpg"
SSH_SRC="$HOME/.ssh"
PENDRIVE_DIR="/media/migueldorosario/2079-8A26/cofre_segredos"
GDRIVE_REMOTE="drive:Cofres/cofre_ssh"   # drive: e gdrive: = mesma conta Google
STAGING="/dev/shm/cofre_ssh_staging"
ABERTO="/dev/shm/cofre_ssh_aberto"
SENHA_WP="/home/migueldorosario/Downloads/Antigravity Google/Outros/chaves/ssh_servidor_wp_cafezinho.md"

GPG_OPTS=(--batch --yes --pinentry-mode loopback
  --s2k-cipher-algo AES256 --s2k-digest-algo SHA512
  --s2k-mode 3 --s2k-count 65011712)

# Arquivos de ~/.ssh que entram no cofre (chaves privadas + pubs + config).
# known_hosts fica FORA (não é segredo e muda toda hora).
VAULT_SSH=(config id_ed25519 id_ed25519.pub id_ed25519_gsn id_ed25519_gsn.pub
  id_ed25519_manus id_ed25519_manus.pub id_rsa id_rsa.pub)

vermelho() { printf '\033[31m%s\033[0m\n' "$*"; }
verde()    { printf '\033[32m%s\033[0m\n' "$*"; }
amarelo()  { printf '\033[33m%s\033[0m\n' "$*"; }

pedir_senha() {  # $1 = rótulo; usa COFRE_PASS se definido, senão pergunta 2x
  if [[ -n "${COFRE_PASS:-}" ]]; then return 0; fi
  local a b
  while true; do
    read -rsp "Palavra do cofre ($1): " a; echo
    read -rsp "Confirme a mesma palavra: " b; echo
    [[ "$a" == "$b" ]] && { COFRE_PASS="$a"; return 0; }
    vermelho "As palavras não batem, tente de novo."
  done
}

cifra() {  # stdin: senha; $1 = arquivo de entrada; $2 = saída .gpg
  gpg "${GPG_OPTS[@]}" --passphrase-fd 0 --output "$2" -c "$1"
}

decifra() { # stdin: senha; $1 = blob; $2 = saída (ou - para stdout)
  gpg "${GPG_OPTS[@]}" --passphrase-fd 0 --output "$2" -d "$1" 2>/dev/null
}

limpar_ram() {  # apaga com shred tudo que ficou em /dev/shm
  for d in "$STAGING" "$ABERTO"; do
    if [[ -e "$d" ]]; then
      find "$d" -type f -exec shred -u {} \; 2>/dev/null || true
      rm -rf "$d"
    fi
  done
}

cmd_selar() {
  local faltando=0 f
  for f in "${VAULT_SSH[@]}"; do
    [[ -f "$SSH_SRC/$f" ]] || { amarelo "AVISO: $SSH_SRC/$f não existe (pulando)"; faltando=1; }
  done
  limpar_ram
  mkdir -p "$STAGING/ssh"
  for f in "${VAULT_SSH[@]}"; do
    [[ -f "$SSH_SRC/$f" ]] && cp -p "$SSH_SRC/$f" "$STAGING/ssh/$f"
  done
  if [[ -f "$SENHA_WP" ]]; then cp -p "$SENHA_WP" "$STAGING/ssh/"; fi
  {
    echo "# MANIFESTO DO COFRE SSH — $(date '+%d/%m/%Y %H:%M') em $(hostname)"
    echo "# fingerprints públicos (seguros de expor) para conferência futura"
    for f in "$STAGING"/ssh/id_* "$STAGING"/ssh/config "$STAGING"/ssh/*.md; do
      [[ -f "$f" ]] || continue
      echo "- $(basename "$f")  sha256=$(sha256sum "$f" | cut -d' ' -f1)"
      if [[ "$f" == "$STAGING"/ssh/id_* ]] && [[ "$f" != *.pub ]]; then
        ssh-keygen -lf "$f" 2>/dev/null | sed 's/^/    /' || true
      fi
    done
  } > "$STAGING/MANIFESTO.txt"
  pedir_senha "para SELAR o cofre"
  tar czf /dev/shm/cofre_ssh_tmp.tar -C "$STAGING" .
  printf '%s' "$COFRE_PASS" | cifra /dev/shm/cofre_ssh_tmp.tar "$BLOB"
  shred -u /dev/shm/cofre_ssh_tmp.tar
  limpar_ram
  verde "✅ Cofre selado: $BLOB ($(du -h "$BLOB" | cut -f1))"
  sha256sum "$BLOB"
  cmd_espelhar
}

cmd_abrir() {
  [[ -f "$BLOB" ]] || { vermelho "Blob não encontrado: $BLOB"; exit 1; }
  if [[ -e "$ABERTO" ]]; then vermelho "Já existe cópia aberta em $ABERTO — rode `fechar` antes."; exit 1; fi
  pedir_senha "para ABRIR"
  mkdir -p "$ABERTO"; chmod 700 "$ABERTO"
  if ! printf '%s' "$COFRE_PASS" | decifra "$BLOB" "$ABERTO/cofre.tar"; then
    rm -rf "$ABERTO"; vermelho "Palavra errada (ou blob corrompido). Nada foi aberto."; exit 1
  fi
  tar xzf "$ABERTO/cofre.tar" -C "$ABERTO" && rm -f "$ABERTO/cofre.tar"
  chmod -R go-rwx "$ABERTO"
  verde "✅ Cofre aberto EM RAM: $ABERTO/ssh/"
  ls -la "$ABERTO/ssh/" | tail -n +2
  amarelo "⚠️  Rode \`bash cofre_ssh.sh fechar\` assim que terminar. Isto é memória, não disco."
}

cmd_fechar() {
  limpar_ram && verde "✅ Cópia aberta destruída (shred em /dev/shm)."
}

cmd_verificar() {
  [[ -f "$BLOB" ]] || { vermelho "Blob não encontrado."; exit 1; }
  pedir_senha "para VERIFICAR (não abre nada)"
  if printf '%s' "$COFRE_PASS" | decifra "$BLOB" - | tar tzf - > /dev/null 2>&1; then
    verde "✅ Palavra correta e blob íntegro. Conteúdo:"
    printf '%s' "$COFRE_PASS" | decifra "$BLOB" - | tar tzf -
  else
    vermelho "❌ Palavra errada ou blob corrompido."; exit 1
  fi
}

cmd_trocar() {
  [[ -f "$BLOB" ]] || { vermelho "Blob não encontrado."; exit 1; }
  pedir_senha "ATUAL"
  if ! printf '%s' "$COFRE_PASS" | decifra "$BLOB" /dev/shm/cofre_ssh_tmp.tar; then
    vermelho "Palavra atual errada."; exit 1
  fi
  unset COFRE_PASS
  pedir_senha "NOVA"
  printf '%s' "$COFRE_PASS" | cifra /dev/shm/cofre_ssh_tmp.tar "$BLOB"
  shred -u /dev/shm/cofre_ssh_tmp.tar
  verde "✅ Palavra trocada e cofre re-selado."
  cmd_espelhar
}

cmd_esquecer() {
  [[ -n "${COFRE_PASS:-}" ]] || { vermelho "Uso: COFRE_PASS='<palavra>' bash cofre_ssh.sh esquecer"; exit 1; }
  python3 - "$COFRE_PASS" <<'PYEOF'
import sys, os, glob
senha = sys.argv[1]
alvos = []
for pat in ("~/.zcode/cli/rollout/*.jsonl", "~/.zcode/cli/log/*.jsonl",
            "~/.zcode/cli/artifacts/**/*.jsonl", "~/.zcode/v2/sessions/**/*.jsonl",
            "~/.zcode/cli/workspace/**/*.jsonl"):
    alvos += glob.glob(os.path.expanduser(pat), recursive=True)
alvos += [os.path.expanduser(p) for p in ("~/.bash_history", "~/.zsh_history") if os.path.exists(os.path.expanduser(p))]
total = 0
for a in sorted(set(alvos)):
    try:
        with open(a, "r", errors="replace") as fh: txt = fh.read()
        n = txt.count(senha)
        if n:
            with open(a, "w") as fh: fh.write(txt.replace(senha, "[🔒PALAVRA-REMOVIDA]"))
            total += n
            print(f"  limpo: {a} ({n} ocorrência(s))")
    except OSError:
        pass
print(f"TOTAL removido: {total} ocorrência(s) da palavra." if total else "Nenhuma ocorrência encontrada — já está limpo.")
PYEOF
  amarelo "⚠️  Se a sessão que recebeu a palavra ainda estiver ABERTA, rode \`esquecer\` de novo depois de fechar o app (o transcript pode ser regravado no final)."
}

cmd_espelhar() {
  [[ -f "$BLOB" ]] || { vermelho "Blob não encontrado — rode \`selar\` primeiro."; exit 1; }
  local h_local; h_local="$(sha256sum "$BLOB" | cut -d' ' -f1)"
  # 1) Pendrive físico
  if [[ -d "$PENDRIVE_DIR" ]] || mkdir -p "$PENDRIVE_DIR" 2>/dev/null; then
    cp -f "$BLOB" "$PENDRIVE_DIR/"
    local h_pd; h_pd="$(sha256sum "$PENDRIVE_DIR/$(basename "$BLOB")" | cut -d' ' -f1)"
    [[ "$h_pd" == "$h_local" ]] && verde "✅ Pendrive: $PENDRIVE_DIR (sha256 confere)" || vermelho "❌ Pendrive divergente!"
  else
    amarelo "⚠️ Pendrive não montado em $PENDRIVE_DIR — espete e rode \`espelhar\`."
  fi
  # 2) Google Drive
  if command -v rclone >/dev/null; then
    if rclone copy "$BLOB" "$GDRIVE_REMOTE" --quiet 2>/dev/null \
       && [[ "$(rclone cat "$GDRIVE_REMOTE/$(basename "$BLOB")" 2>/dev/null | sha256sum | cut -d' ' -f1)" == "$h_local" ]]; then
      verde "✅ Google Drive: $GDRIVE_REMOTE (sha256 confere)"
    else
      vermelho "❌ Falha no upload/conferência do GDrive."
    fi
  fi
  # 3) GitHub: o blob vive dentro do Cérebro → sobe no próximo sync do trilho
  verde "✅ GitHub: o blob está em $COFRE_DIR (dentro do Cérebro) — o sync_cerebro_to_github.py sobe no próximo ciclo (ou rode-o agora)."
}

cmd_status() {
  local h; h="$(sha256sum "$BLOB" 2>/dev/null | cut -c1-16 || echo '—')"
  echo "── Cofre SSH (v1) ──"
  for loc in "Cérebro/GitHub (após sync):$BLOB" "Pendrive:$PENDRIVE_DIR/$(basename "$BLOB")"; do
    local p="${loc#*:}"
    if [[ -f "$p" ]]; then
      echo "  ✅ ${loc%%:*} → $p ($(du -h "$p" | cut -f1), sha8 $(sha256sum "$p" | cut -c1-8), $(date -r "$p" '+%d/%m %H:%M'))"
    else
      echo "  ❌ ${loc%%:*} → AUSENTE"
    fi
  done
  if command -v rclone >/dev/null; then
    rclone lsl "$GDRIVE_REMOTE" 2>/dev/null | grep "$(basename "$BLOB")" | awk '{print "  ✅ Google Drive → "$4" bytes, "$2" "$3}' \
      || echo "  ❌ Google Drive → AUSENTE"
  fi
  [[ -d "$ABERTO" ]] && vermelho "  ⚠️ Cofre ABERTO agora em $ABERTO — rode fechar!" || echo "  Cofre fechado (nada aberto em RAM)."
  echo "  sha256 local completo: $h"
}

cmd_sugerir() {
  # ~60+ bits: 4 palavras sorteadas do dicionário + 2 dígitos
  local p=() w i
  if [[ -r /usr/share/dict/words ]]; then
    while (( ${#p[@]} < 4 )); do
      w="$(grep -E '^[a-z]{4,9}$' /usr/share/dict/words | shuf -n1 || true)"
      if [[ -n "$w" ]]; then
        p+=( "$(printf '%s' "$w" | sed 's/^./\U&\E/')" )
      fi
    done
  fi
  if (( ${#p[@]} == 4 )); then
    echo "Sugestão (DECORE — nunca salve em arquivo/chat): ${p[0]}-${p[1]}-${p[2]}-${p[3]}-$(shuf -i 10-99 -n1)"
  else
    echo "Sem dicionário local — componha você: 4+ palavras SEM RELAÇÃO entre si + 2 dígitos (ex.: método diceware)."
  fi
}

cmd_selftest() {
  local T="/tmp/cofre_ssh_selftest_$$"
  rm -rf "$T"; mkdir -p "$T/ssh"
  ssh-keygen -t ed25519 -N "" -C "selftest-ficticia" -f "$T/ssh/id_teste" -q
  echo "senha-ficticia-servidor" > "$T/ssh/senha_teste.md"
  local blob_t="$T/cofre_TESTE.tar.gpg" senha_t="senha-descartavel-selftest-777"
  tar czf "$T/c.tar" -C "$T" ssh
  printf '%s' "$senha_t" | cifra "$T/c.tar" "$blob_t"
  printf '%s' "$senha_t" | decifra "$blob_t" - | tar tzf - | grep -q id_teste || { vermelho "❌ cifra/decifra"; exit 1; }
  if printf '%s' "senha-ERRADA" | decifra "$blob_t" "$T/out.tar" 2>/dev/null; then
    vermelho "❌ senha errada foi aceita!"; exit 1
  else
    verde "✅ senha errada rejeitada"
  fi
  # esquecer: testa com HOME falso, sem tocar nos transcripts reais
  mkdir -p "$T/fakehome/.zcode/cli/rollout"
  echo "{\"prompt\":\"use a senha senha-descartavel-selftest-777 por favor\"}" > "$T/fakehome/.zcode/cli/rollout/sess_FAKE.jsonl"
  HOME="$T/fakehome" COFRE_PASS="$senha_t" bash "$0" esquecer >/dev/null 2>&1 || true
  if grep -q "PALAVRA-REMOVIDA" "$T/fakehome/.zcode/cli/rollout/sess_FAKE.jsonl" \
     && ! grep -qF "$senha_t" "$T/fakehome/.zcode/cli/rollout/sess_FAKE.jsonl"; then
    verde "✅ esquecer remove a palavra do transcript (HOME falso)"
  else
    vermelho "❌ esquecer não limpou"; exit 1
  fi
  verde "✅ selftest completo OK (chaves fictícias; nada real foi tocado)"
  rm -rf "$T"
}

case "${1:-}" in
  selar)           cmd_selar ;;
  abrir)           cmd_abrir ;;
  fechar)          cmd_fechar ;;
  verificar)       cmd_verificar ;;
  trocar-palavra)  cmd_trocar ;;
  esquecer)        cmd_esquecer ;;
  espelhar)        cmd_espelhar ;;
  status)          cmd_status ;;
  sugerir)         cmd_sugerir ;;
  selftest)        cmd_selftest ;;
  *) sed -n '2,30p' "$0"; exit 1 ;;
esac
