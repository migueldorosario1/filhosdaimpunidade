---
name: reference-ssh-identity-agent-none-mtu-1360
description: "SSH para Tencent/NYC/GSN trava no KEX (Connection closed by [client IP] [preauth]). Solução dupla: IdentityAgent=none no ~/.ssh/config + MTU 1360 na interface local."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8151465d-76ab-4d1d-bfe5-285d266e7ca7
---

Quando SSH cliente Ubuntu 20.04 (OpenSSH 8.2p1) trava no KEX/Authenticating pra servidores Tencent/NYC/GSN com **TCP+banner OK**, **MTU ping passa** mas **handshake nunca conclui**, e o sshd remoto loga `Connection closed by <client IP> [preauth]` — não é firewall, não é fail2ban, não é cipher mismatch. Causa raiz é DUPLA:

### 1. Path MTU Black Hole na rota internacional
- Algum hop intermediário descarta pacotes >1464 bytes silenciosamente
- ICMP ping passa porque é pequeno · KEX falha porque a chave pública é grande
- **Solução**: `sudo ip link set dev <interface> mtu 1360` (reduz a MTU local pra forçar fragmentação no cliente)

### 2. ssh-agent / Gnome Keyring travado
- Após `rekey in` (renegociação de chave), o cliente SSH precisa assinar com chave privada
- O agente do Gnome Keyring fica esperando uma requisição gráfica em background que nunca volta
- **Solução**: `-o IdentityAgent=none` força SSH ler a chave **direto do disco** ao invés de usar o agente

### Solução permanente (~/.ssh/config)

```
Host tencent cingapura china
    HostName 43.156.151.165
    Port 38422
    User ubuntu
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly yes
    IdentityAgent none          # ← solução
    ServerAliveInterval 60
    StrictHostKeyChecking no

Host nyc
    HostName 198.199.121.136
    User root
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    IdentityAgent none          # ← solução
    StrictHostKeyChecking no

Host gsn
    HostName 159.89.237.100
    User root
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    IdentityAgent none          # ← solução
    StrictHostKeyChecking no
```

### Solução temporária (linha de comando)
```bash
ssh -o IdentityAgent=none -p 38422 ubuntu@43.156.151.165
```

### Caso fundador

Diagnosticado pelo **AGY-CLI** em 2026-06-19 03:30 BRT após Daemon e Kimi perderem SSH simultaneamente desde 00:00 BRT 19/06. Daemon havia descartado 7 hipóteses comuns (firewall, fail2ban, KEX algorithm, cipher, ISP, Tata Communications, MTU básico via ping). AGY-CLI juntou as duas causas que sozinhas pareciam descartáveis:
- MTU ping passa, mas TCP grande não (path MTU black hole)
- KEX progride até o ponto de rekey, daí trava (ssh-agent bloqueado)

Testado e confirmado pelo Daemon às 03:33 BRT: SSH Tencent + NYC respondendo instantâneo após aplicar `IdentityAgent=none` (MTU já estava em 1360 do Miguel).

### Documentos canônicos

- `Projeto Cafezinho Agentes/Foruns/carta_agy_cli_misterio_ssh_bloqueado_20260619.md` (cartinha + resposta AGY §11)
- `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_ssh_trindade_20260619.md` (caso aberto Kimi)

### Vinculado a

- [[reference-iproyal-proxy-youtube-yt-dlp-bypass]] (workaround similar de rede)
- [[feedback-creditos-apis-primeiro-item-diagnostico-lentidao]] (princípio "verificar coisa óbvia primeiro" — neste caso o ssh-agent era invisível mas fundamental)
