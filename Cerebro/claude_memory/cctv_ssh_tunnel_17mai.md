---
name: cctv-ssh-tunnel-setup-17-05
description: SSH reverse tunnel pra expor CCTV localhost ao IP externo Tencent
metadata: 
  node_type: memory
  type: project
  originSessionId: 65dba477-db6e-40a3-b94a-ea6212c77e90
---

**[2026-05-17 20:46 BRT]** — SSH tunnel remoto ativado pra expor CCTV

## Problema Original

- IP externo 43.156.151.165:8080 retornava 404 do Werkzeug (painel antigo)
- Painel v2 não existia no Tencent
- Mesmo copiando, caminho `CANAL_TRINDADE` não existe lá

## Solução

**SSH Reverse Tunnel:**
```bash
ssh -i ~/.ssh/id_rsa -p 38422 -R 8080:127.0.0.1:8080 ubuntu@43.156.151.165 -N
```

- `-R 8080:...` = mapeia porta 8080 remota → localhost 8080 aqui
- `-N` = só forward portas, não execute comando
- Rodando em background (PID 20629)

## Link Externo

🔗 **http://43.156.151.165:8080**

- Status: ✅ ATIVO
- Fornecedor: localhost:8080 daqui
- Tunnel: SSH remoto ativo
- Restart: Tunnel é persistent, CCTV rodando localmente

## Como Reativar se Cair

```bash
nohup ssh -i ~/.ssh/id_rsa -p 38422 -R 8080:127.0.0.1:8080 ubuntu@43.156.151.165 -N > /tmp/cctv_tunnel.log 2>&1 &
```

Ou verificar se tunnel morreu:
```bash
ps aux | grep "ssh.*-R 8080"
```

---

**Criado:** 2026-05-17 20:46 BRT (Claude Code)  
**Status:** Operacional
