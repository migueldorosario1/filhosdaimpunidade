---
name: crontab-fonte-verdade-agentes-ativos
description: "Para saber quais agentes estão ATIVOS no Cafezinho, ler o crontab — NÃO a pilha de .py soltos no /root (cheia de legacy órfão)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

Para saber o que está **ativo/vivo** no Cafezinho, a fonte de verdade é o **`crontab -l`** (linhas não-comentadas), nunca a lista de arquivos `.py` em `/root`.

**Why:** o `/root` do servidor Tencent tem ~156 arquivos `.py`, dos quais ~71 são legacy "morto" + dezenas de `.bak`/`.bkp`/rascunhos. Há duplicatas confusas: `agente_eleicoes.py` × `agente_eleicoes_legado.py` × `agente_eleicoes_produtor.py`; `agente_master_trends.py` × `agente_master_trends_v9.py`. Num tick de monitoramento (02/06) eu me perdi tratando arquivos soltos como inventário e quase classifiquei vivos como lixo. Miguel corrigiu: "voce está meio perdido com os agentes, pq tem muitos agentes legacy perdidos no root."

**How to apply:** ao auditar saúde de agentes ou responder "agente X está ligado?", começar por `sudo crontab -l | grep -i <agente>` (ativo vs comentado). Um traceback num `.py` que NÃO está no crontab é provavelmente ruído de legacy, não regressão. Cuidado com a exceção: `agente_master_trends_v9.py` (sufixo _v9) é o agente PRINCIPAL/mais ativo, não legacy — confirmar pelo crontab/banco_custos, não pelo nome. Inventário vivo: [[project_faxina_agentes_legacy_root]]. Faxina geral agendada 08-12/06/2026.
