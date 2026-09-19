---
name: Fix caixa_newsletter — IndentationError em 6 scripts (2026-04-17)
description: Bug de indentação em 6 agentes com bloco "caixa_newsletter" — 4 espaços extras nas linhas do caixa_newsletter e do html += caixa_newsletter. Corrigido via Edit + scp.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 foi descoberto `IndentationError: unexpected indent` em 6 scripts com bloco de injeção da newsletter Mailchimp. Padrão: 4 espaços a mais na linha `caixa_newsletter = """` E também na linha `html += caixa_newsletter`. Alguém (ou um template) colou o bloco em nível de indentação errado.

**Arquivos corrigidos (deploy 2026-04-17 08:12):**
- `agente_analytics_v9.py` (linhas 800 e 814) — rodava 45 * * * * e crashava sempre
- `agente_eleicoes.py` (linhas 782 e 796) — cron 0 9,21
- `agente_fantastico.py` (linhas 564 e 578) — cron 5 * * * * (crashava toda hora; nunca publicou)
- `agente_feminino.py` (linhas 777 e 791) — cron 0 8,20 — publicava ANTES do crash; newsletter não saía
- `agente_escritor_scifi.py` (linhas 141 e 155) — fora do cron (em configuração pelo Miguel)
- `agente_escritor_scifi_en.py` (linhas 139 e 153) — fora do cron

**Backup no servidor:** `.bak_20260417_0810`

**Why:** bug que impedia o Fantástico de publicar (cron */hora), Analytics de gerar relatório, e outros agentes de injetar a caixa de newsletter no HTML.

**How to apply:** se aparecer `IndentationError` em outro agente com `caixa_newsletter`, conferir ambas as linhas (a do `=` e a do `html +=`). Comparar indentação com as linhas vizinhas — devem bater exatamente.
