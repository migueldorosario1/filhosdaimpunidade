---
name: Crontab Tencent restaurado em 2026-04-17 (36 linhas, via crontab_server.txt)
description: Após 2 sobrescritas consecutivas no crontab do Tencent em 16-17/04, estado final é 36 linhas ativas — todas aplicadas via espelho crontab_server.txt, que é o arquivo canônico.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
História do dia 2026-04-17:

**Estado inicial (achado 06:53):** só 8 linhas ativas no Tencent (toda Trindade Editorial + redes sociais tinham sumido desde 2026-04-16 23:xx, provavelmente durante deploys). NYC failover publicou ~7 posts enquanto o Tencent estava parado.

**1ª reativação (06:53) pelo Claude:** reaplicou `crontab_atual.txt` → 27 linhas. Depois adicionou `agente_facebook.py (*/15)` e `robo_coleta_imagens.py (0 3,15)` → 29 linhas.

**2ª reativação (~08:20) pelo Miguel:** aplicou `crontab_server.txt` (espelho oficial mais completo) → **36 linhas**. Sobrescreveu as linhas do Claude, mas tem equivalentes melhores:
- Facebook: `10,25,40,55 * * * *` com venv (antes era `*/15`)
- robo_coleta_imagens: `15,45 * * * *` (a cada 30min, muito mais agressivo)
- **ADICIONADO:** `gerenciador_fila_redes.py (*/15)` + `agente_twitter.py (*/5)` — que o Claude não sabia que existiam

**Estado final (2026-04-17):** 36 linhas inicialmente. Ao longo do dia cresceu:
- +1 linha pela ativação da **Patrulha YouTube** (RSS primário `25 * * * *` + Brave fallback `0 */2`) → 37-38
- +2 linhas pelo **Agente Militar** novo (coletor `8,38` + publicador `0 9,14,20`) → ~39
- +N linhas pelos **5 agentes temáticos** (IA, petróleo, mercado, energias, inflação) que o Antigravity deployou em paralelo → **46 linhas totais**

Arquivo espelho canônico: `Projeto Cafezinho Agentes/root/crontab_server.txt`.

**Why:** o Miguel mantém múltiplos arquivos de crontab no projeto (`crontab_atual.txt`, `crontab_novo.txt`, `crontab_server.txt`, `crontab_backup_emergency.txt`, etc). Usar o errado causa regressão. Ver `crontab_espelho_oficial.md`.

**How to apply:**
- Se precisar editar o crontab, **abrir `root/crontab_server.txt`** (não outro).
- Deploy: `cat crontab_server.txt | ssh cingapura 'sudo crontab -'` (ou scp + sudo crontab /tmp/crontab_server.txt).
- Conferir estado: `ssh cingapura 'sudo crontab -l | grep -cvE "^(#|$)"'` deve retornar **36**.
- Se só der 8 (como aconteceu em 17/04 06:53), reaplicar imediatamente.
