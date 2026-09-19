---
name: Usar python3 em vez de jq localmente
description: Na máquina local, jq não está instalado. Sempre usar python3 -c para parsear JSON em comandos bash locais.
type: feedback
originSessionId: 9002c7ec-10c3-4489-8dad-6a7a4128f954
---
Na máquina local do Miguel, `jq` não está disponível (comando não encontrado).

**Why:** Tentei usar `jq` em comando local de monitoramento e quebrou.

**How to apply:** Para qualquer `curl | jq ...` local, substituir por `curl | python3 -c "import sys,json; ..."`. No servidor Tencent, jq pode ou não estar disponível — usar python3 por padrão também lá para consistência.
