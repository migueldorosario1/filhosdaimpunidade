# 🧠 MEMÓRIA TÉCNICA — Cofre SSH criptografado em 3 destinos + esquecer de transcripts

**Data:** 22/08/2026 01:13→01:30 BRT · **Autor:** ZCode/GLM-5.3 · Sprint: ordem do Miguel "me ajuda a guardar os segredos ssh no pendrive criptografados no github repo cérebro e no gdrive, ambos criptografados? e ai eu apenas dou o segredo a um llm, um a palavra, que ele usa apenas numa sessão depois apaga e esquece. ajuda na segurança?"

## 1. Contexto achado (antes de mexer)

- **Pendrive 2079-8A26 (exFAT, 58G livres, montado)** já tinha segredos EM CLARO: `chaves ssh/` (id_rsa+pub, copiados HOJE 22/08 00:34) e `ssh_cafezinho_2026-08-19/` (config + 3 ed25519 + id_rsa + pubs + known_hosts). Ou seja, o Miguel já vinha espalhando manualmente — o cofre formaliza e cifra.
- `~/.ssh` do Dell: id_rsa (17/03), id_ed25519, id_ed25519_gsn, id_ed25519_manus (abril) + config (aliases tencent/alibaba/cafezinho-wp).
- SEV-1 (18/08): cofres_laura/ (4 chaves + envs + rclone.conf) commitado EM CLARO no histórico do repo cerebro-miguel (contido por git rm ce7eac56; Miguel manteve histórico; rotação recomendada e pendente). `cofres_laura/` não existe mais no working dir.
- Transcripts do ZCode: `~/.zcode/cli/rollout/model-io-sess_*.jsonl` (model IO completo!) e `~/.zcode/cli/log/zcode-AAAA-MM-DD.jsonl`. `~/.zcode/v2/sessions` vazio (era ACP-era).
- Ferramentas: `age` AUSENTE; gpg 2.x, openssl, rclone OK. rclone remotes: `drive:`/`gdrive:` (mesma conta).

## 2. O que foi construído

`Cerebro/Cofres/cofre_ssh/`:
- **`cofre_ssh.sh`** (executável, ~230 linhas): GPG simétrico AES-256, `--s2k-digest-algo SHA512 --s2k-mode 3 --s2k-count 65011712` (KDF máx.). Passphrase via `--passphrase-fd 0` alimentado por pipe do `printf` — **nunca em argv** (não aparece no `ps`). Comandos: selar/abrir/fechar/verificar/trocar-palavra/esquecer/espelhar/status/sugerir/selftest.
- **`LEIA-ME.md`**: protocolo completo (primeira vez, fluxo palavra-ao-LLM, avaliação honesta, regras permanentes p/ agentes).
- Design de destinos: blob vive NO Cérebro (sobe ao GitHub pelo trilho 15min) + `espelhar` copia pra pendrive `cofre_segredos/` e `drive:Cofres/cofre_ssh/` com conferência sha256 dupla (local×destino; GDrive via `rclone cat | sha256sum`).
- `abrir` extrai **em /dev/shm (tmpfs=RAM)**, `fechar` shred. `esquecer` varre `~/.zcode/cli/{rollout,log,artifacts,workspace}/**/*.jsonl` + `~/.zcode/v2/sessions/**` + `~/.bash_history`/`~/.zsh_history`, substitui por `[🔒PALAVRA-REMOVIDA]` (python, `errors="replace"`), reporta contagem por arquivo. Aviso embutido: re-rodar após fechar o app (transcript da sessão aberta é regravado no fim).
- MANIFESTO interno do tar: sha256 de cada arquivo + fingerprints `ssh-keygen -lf` (públicos, seguros).

## 3. Provas

1. **Selftest 3/3 ✅** (chaves fictícias em /tmp): senha errada rejeitada; esquecer limpa transcript fake com HOME falso; cifra/decifra íntegro.
2. **Canais E2E com blob demo** (`cofre_ssh_v1_TESTE.tar.gpg`, conteúdo fictício, senha descartável):
   - Pendrive: sha256 confere ✅
   - GDrive: sha256 confere via rclone cat ✅
   - Ida-e-volta GPG ✅
   - GitHub: dry-run `sync_cerebro_to_github.py` → Cofres/ entra nos 5556 copiados; blob .tar.gpg NÃO bloqueado (lista de bloqueados continua pegando só sensíveis em claro, ex. CARTAO_BOLSO_SSH_SERVIDOR_WP_CAFEZINHO.md) ✅
   - Blob demo REMOVIDO dos 2 destinos após a prova (rclone delete + rm) ✅
3. `bash -n` limpo; `set -euo pipefail` em tudo.

## 4. Bugs de desenvolvimento (registro de lições)

- `gpg -c arquivo -o saida` → usage error; ordem correta: `--output saida` **antes** de `-c arquivo` (o script usa a ordem certa via função `cifra`).
- `[ "$H" = "$Hpd" ]` com hashes vazios = falso positivo — sempre checar `-n "$H"` antes de comparar.
- Selftest v1 falhava por **SIGPIPE**: `cmd | grep -q` mata o producer cedo → pipefail derruba; fix = conferir os ARQUIVOS de saída em vez do stdout pipado.
- `[[ -n "$w" ]] && {...}` como statement solto + `set -e` mata o script quando falso — usar `if` explícito (bug do `sugerir` v1).

## 5. Pendências

- **Miguel:** rodar `selar` com a palavra dele (não passa pelo chat) → `status` → apagar pastas em claro do pendrive. Recomendado: rotação das chaves do SEV-1.
- Espelhar script+LEIA-ME pro pendrive/GDrive (feito nesta sessão — estrutura sem blob).
- Agente do lado da Laura pode reutilizar o script (GPG existe no Windows via gpg4win; blob igual nos 3 lugares).

## 6. State of mind para a próxima sessão

O cofre está pronto e provado, mas VAZIO por design — sem a palavra do Miguel ele é uma lata sem chave e sem conteúdo. Se o Miguel pedir "usa o cofre": ele digita a palavra no chat → `COFRE_PASS='...' bash cofre_ssh.sh abrir` → usar de `/dev/shm/cofre_ssh_aberto/ssh/` → `fechar` → `esquecer` → `esquecer` de novo após fechar o app. A palavra NUNCA vai pra nenhum arquivo do Cérebro.
