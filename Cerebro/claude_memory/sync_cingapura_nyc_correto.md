---
name: Sincronização Cingapura → NYC (modo correto)
description: Comando rsync seguro (sem -a) pra replicar .py de Cingapura pro NYC, validado em 2026-04-18.
type: reference
originSessionId: 45d53b87-5aea-4ee1-bde2-cc8f6a6aec6e
---
Workflow testado e validado em 2026-04-18 00:10 (depois de quebrar SSH do NYC por usar `-a`).

**Passo 1 — puxar .py da Cingapura pra staging local:**
```bash
mkdir -p /tmp/sync_cin2nyc
rsync -az --checksum -e "ssh -i ~/.ssh/id_rsa -p 38422" \
  --include='*.py' --exclude='*' \
  ubuntu@43.156.151.165:/root/ /tmp/sync_cin2nyc/
```
O `-a` aqui é OK porque destino é `/tmp/` local (não é /root de servidor).

**Passo 2 — enviar staging pro NYC SEM -a:**
```bash
rsync -rlptvz --no-o --no-g --checksum -e "ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes" \
  /tmp/sync_cin2nyc/ root@45.55.50.249:/root/
```
`--no-o --no-g` é o que impede o transplante de UID que quebra o StrictModes do sshd.

**Passo 3 — validar gêmeos (MD5 idênticos):**
```bash
ssh cingapura "cd /root && md5sum *.py 2>/dev/null | LC_ALL=C sort -k2" > /tmp/cin_md5.txt
ssh nyc "cd /root && md5sum *.py 2>/dev/null | LC_ALL=C sort -k2" > /tmp/nyc_md5.txt
diff /tmp/cin_md5.txt /tmp/nyc_md5.txt
# Vazio = gêmeos perfeitos.
```

**Quando fazer:** sempre depois de deploy/fix em Cingapura, pra NYC ficar pronto pro failover.

**Não sincronizar:** crontab (NYC tem `run_if_master.sh` próprio), `.ssh/`, `.env.unificado` (mesmas keys mas paths podem divergir), `agent_data/youtube_vistos.json` (estado próprio do NYC).
