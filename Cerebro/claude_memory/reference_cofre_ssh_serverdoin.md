---
name: reference-cofre-ssh-serverdoin
description: "Credenciais SSH do hosting WordPress Serverdo.in (servidor 190.89.239.65, controle.ocafezinho.com). NÃO ficam aqui no Cérebro (§82). Valores em /root/.env.unificado Tencent + backup /root/cerebro_trindade/cofre/env_cofre_backup Beijing."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 42789f13-00c9-4e70-9b8c-f37d93570ab6
---

# Cofre SSH Serverdo.in — ponteiro (valores fora do Cérebro)

**Servidor:** hosting WordPress Cafezinho (`controle.ocafezinho.com` → `190.89.239.65`)
**Provedor:** WIM / Serverdo.in
**Suporte:** Vitor R. <Suporte e Infraestrutura | Serverdo.in>

## Onde estão os valores (NÃO aqui — §82 cofre)

- **Primário Tencent (`43.156.151.165:38422 ubuntu`):**
  - Arquivo: `/root/.env.unificado` (chmod 600, owner root)
  - Variáveis: `SERVERDOIN_SSH_HOST`, `SERVERDOIN_SSH_IP`, `SERVERDOIN_SSH_PORT`, `SERVERDOIN_SSH_USER`, `SERVERDOIN_SSH_PASSWORD`, `SERVERDOIN_SSH_NOTE`
- **Backup Beijing (`39.106.184.215:22 root`):**
  - Arquivo: `/root/cerebro_trindade/cofre/env_cofre_backup` (chmod 600, owner root)
  - Mesmo conteúdo, espelho

## Quando usar

- Servidor `controle.ocafezinho.com` precisa diagnóstico técnico (caso 24/05 09:50 BRT — admin caiu)
- Reinício de serviço, verificação de logs, free disk space, status MySQL/nginx no host
- **NÃO usar pra rotina** — só quando suporte WIM não basta ou Miguel autoriza explicitamente

## Como puxar (rapidamente)

Do Tencent:
```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  'sudo grep ^WIM_SSH /root/.env.unificado'
```

Do Beijing:
```bash
ssh -i ~/.ssh/id_ed25519_cerebro_vigias -p 22 root@39.106.184.215 \
  'cat /root/cerebro_trindade/cofre/env_cofre_backup | grep ^WIM_SSH'
```

## Cuidados (§82 + boas práticas)

- ❌ NUNCA copiar senha pra canal_trindade/fóruns/MEMORY.md/Telegram
- ❌ NUNCA logar senha em arquivo `.log`
- ❌ NUNCA passar senha via `ssh -o` em linha de comando que vire `ps aux` (visível a outros usuários)
- ✅ Sempre carregar via `source /root/.env.unificado` ou `sshpass -f /etc/sshpass_wim_secret` (arquivo chmod 600)
- ✅ Rotacionar senha após uso de emergência (boa prática — pedir nova via Vitor R.)

## Histórico

- 2026-05-24 21:29 UTC (18:29 BRT Brasília) Beijing / 09:55 BRT Tencent — credenciais recebidas via suporte Vitor R. e armazenadas no cofre Tencent+Beijing por Claude Maestro a pedido Miguel. Servidor estava em queda no momento do recebimento (esperando normalização).

## Relacionado

- [[feedback_credenciais_nunca_em_forum_canal]] — §82 cofre
- [[reference_sistema_resumo]] — infra geral

— Inscrito por Claude Maestro 2026-05-24 09:58 BRT
