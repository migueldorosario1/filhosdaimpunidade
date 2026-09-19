---
name: SSH para servidores do Cafezinho
description: Comandos SSH corretos para Tencent SG (Cingapura) e DigitalOcean NYC — regras de usuário, chave e alias.
type: reference
originSessionId: a6af224d-901d-4c7d-ab75-58b5eae63f5b
---
## Tencent SG (Cingapura) — Servidor MESTRE de produção

- **Alias:** `ssh cingapura` ou `ssh china`
- **IP:** 43.156.151.165
- **Porta SSH:** **38422**
- **Usuário:** **ubuntu** (NUNCA root — root é bloqueado silenciosamente)
- **Chave:** `~/.ssh/id_rsa` com `IdentitiesOnly yes`
- **Comandos root:** usar `sudo`

## DigitalOcean NYC — Failover

- **Alias:** `ssh nyc`
- **IP:** 45.55.50.249
- **Porta SSH:** 22 (padrão)
- **Usuário:** root (NYC aceita root)
- **Chave:** `~/.ssh/id_ed25519` com `IdentitiesOnly yes`
- **Armadilha conhecida:** o `/root` precisa pertencer a root:root (uid 0). Se a ownership mudar (ex: deploy ou rsync acidental), SSH rejeita com "bad ownership or modes". Fix: `chown root:root /root`

## Regras críticas

1. **Sempre usar `IdentitiesOnly yes`** — sem isso o SSH tenta múltiplas chaves e causa "Too many authentication failures"
2. **Cingapura = ubuntu, NYC = root** — não misturar
3. **Cingapura usa id_rsa, NYC usa id_ed25519** — não misturar
