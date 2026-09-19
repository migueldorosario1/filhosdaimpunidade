---
name: Crontab do Tencent — espelho oficial é crontab_server.txt
description: O arquivo de referência canônico para o crontab do servidor Tencent é Projeto Cafezinho Agentes/root/crontab_server.txt (não crontab_atual.txt). Toda edição deve passar por ele.
type: feedback
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
O arquivo espelho **canônico** do crontab do Tencent é `Projeto Cafezinho Agentes/root/crontab_server.txt`. É ele — não `crontab_atual.txt` — que deve ser editado localmente e depois aplicado via `scp` + `sudo crontab /tmp/crontab_server.txt`.

**Why:** em 2026-04-17 o Miguel restaurou 7 linhas que tinham sumido do crontab produção (inclusive agentes de Redes Sociais Autônomas: `gerenciador_fila_redes.py`, `agente_twitter.py` e `agente_facebook.py`) usando o espelho `crontab_server.txt`. O `crontab_atual.txt` estava desatualizado. Miguel disse: *"Toda e qualquer modificação futura gerida no Crontab da VPS deve obrigatoriamente operar sobre o espelho nativo-local do projeto (crontab_server.txt). É expressamente PROIBIDA as edições voláteis (crontab -e) sem backup direto na infraestrutura do usuário."*

**How to apply:**
- **Antes de editar o crontab:** abrir `crontab_server.txt` (não `crontab_atual.txt`), fazer as mudanças lá.
- **Deploy:** `scp -P 38422 -i ~/.ssh/id_rsa <arquivo> ubuntu@...:/tmp/crontab_server.txt && ssh cingapura 'sudo crontab /tmp/crontab_server.txt'`.
- **Proibido:** `crontab -e` direto no servidor (edição volátil, sem espelho).
- O crontab_server.txt atual tem **36 linhas ativas** (estado 2026-04-17) — inclui Trindade Editorial, Corretor, Sentinela, Manchete, Feminino, Eleições, Fantástico, Ferroviário, Historiador, Reciclador, Memória, Backup, Analytics, Performance, Observador, Patrulha YouTube, **Redes Sociais (gerenciador_fila_redes */15, agente_twitter */5, agente_facebook 10,25,40,55)**, robo_coleta_imagens (15,45 — a cada 30min), agente_china (5x/dia).
- O `crontab_atual.txt` pode estar desatualizado em relação ao `crontab_server.txt`. **Sempre consultar `crontab_server.txt` primeiro.**
