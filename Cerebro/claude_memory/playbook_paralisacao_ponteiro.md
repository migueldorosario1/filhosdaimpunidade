---
name: Playbook paralisação preventiva Cafezinho
description: Ponteiro pra cartilha de quando/como paralisar agentes do Cafezinho preventivamente quando o site dá sintoma de queda
type: reference
originSessionId: 4bbbac38-0c61-4ff8-b336-797d373e4ac7
---
Cartilha viva em `Outros/playbook_paralisacao_cafezinho.md` (criada 2026-04-24 15:25 BRT após exercício real de paralisação total).

**Conteúdo:**
- Decisão em 3 perguntas: site fora de verdade ou WAF block? Failover ajuda? Bots param?
- Comandos prontos: paralisar (backup auto + comentar todas linhas), validar, retomar (restaurar último backup), validar.
- NÃO fazer: pkill -f bot_, ativar failover NYC, crontab -e direto, crontab -r.
- Lições do exercício 2026-04-24: falso alarme inicial era WAF banindo IP local, descobre testando de 2 IPs.

**Quando consultar:** qualquer suspeita de queda do `www.ocafezinho.com` ou `controle.ocafezinho.com`. Antes de propor failover.
