---
name: REGRA CRÍTICA — rsync com -a derruba SSH do servidor
description: NUNCA usar rsync com -a, --owner ou --group para /root de servidor. Transplanta UID local → quebra StrictModes do sshd → banimento.
type: feedback
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
**NUNCA** usar `rsync -a`, `rsync --owner`, `rsync --group` para enviar arquivos a `/root/` de qualquer servidor (Cingapura, NYC, GSN).

**Why:** o flag `-a` preserva ownership. Quando envio de `migueldorosario@local` com `-a`, os arquivos ficam com UID=1000 (meu usuário local) no servidor. Isso quebra `StrictModes` do sshd (ownership errado em `/root` ou `/root/.ssh/*` → rejeita login com "Permission denied (publickey)"). Em 2026-04-17 derrubei o SSH do NYC exatamente assim, mesmo com a regra documentada no CLAUDE.md. Só recupera abrindo console do painel DigitalOcean/Tencent e rodando `chown -R root:root /root`.

**How to apply:**
- Sempre usar `rsync -rlptvz --no-o --no-g` (ou `-rlptvzP`) para servidor — PERMITE permissions/times/links, mas NÃO owner/group.
- Adicionar `--exclude=".ssh"` como proteção extra.
- Se for só copiar Python entre servidores: `rsync -rlptvz --no-o --no-g --checksum --include='*.py' --exclude='*'`.
- Antes de executar qualquer rsync com /root como destino, RELER este memória e checar que não tem `-a` no comando.
- Fix quando acontecer (só via console do painel cloud, SSH não volta): `chown -R root:root /root && chmod 700 /root/.ssh && chmod 600 /root/.ssh/authorized_keys /root/.ssh/id_rsa /root/.ssh/id_ed25519`.
