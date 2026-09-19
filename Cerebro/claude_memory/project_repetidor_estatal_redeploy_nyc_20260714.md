---
name: repetidor-estatal-redeploy-nyc-14-07-modo-rascunho-1x-hora
description: "Estado operacional do agente_repetidor_estatal.py após redeploy no NYC em 14/07/2026, decisões arquiteturais, configuração de cron e critério de promoção draft→publish"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1bb17b73-7603-4ca4-8fbc-e3a059066760
---

**Fato:** Em 14/07/2026, `agente_repetidor_estatal.py` (706 ln, Labs) foi redeployado no NYC `198.199.121.136` rodando em cron `17 * * * *` (1x/hora, minuto 17), **modo rascunho** (`status: draft` na linha ~466) pra homologação do Miguel no wp-admin antes de religar publish.

**Configuração operacional:**
- Script: `/root/agente_repetidor_estatal.py` (rsync do Labs com REGRA #1 `--no-o --no-g`)
- Banco: `/root/agent_data/estatal_news.db` (resetado — velharia de 13/04 descartada)
- Threshold PUBLICAR: 65 (curadoria rigorosa)
- Fontes: 6 (Senado, Câmara, Agência Brasil, Planalto, IBGE, STF via Google News RSS)
- Notificação: Telegram bot Maura
- Indexing API + cap_150_diario: inativos enquanto status=draft (só disparam em publish)

**Why:** NYC é master primário desde 01/07 (Tencent silenciada por agentes descontrolados). Repetidor é o "sobrevivente do holocausto" — última linha de defesa editorial, tem que funcionar quando tudo cai. Estava parado há 3+ meses no NYC com versão velha 23/06. Miguel pediu religar em modo rascunho pra validar antes de produção real.

**How to apply:**
- Antes de sugerir mudança no repetidor, ler o fórum canônico: `Cerebro/Foruns/forum_repetidor_estatal_redeploy_nyc_20260714.md`
- Decisão arquitetural vigente: **MANTER VERTICAL** (opção A). Não propor separação em 3 blocos (coletor+banco+publicador) sem consumidor secundário justificando. Razão: [[feedback-repetidor-estatal-sobrevive-holocausto]] (cada contrato entre blocos = nova superfície de falha) + [[feedback-auditoria-contrato-entre-blocos]] (bugs de contrato são invisíveis até produção).
- Promoção draft→publish: (1) editar linha ~466 do NYC e do Labs (espelho), (2) validar 1 rodada manual, (3) confirmar `agente_observador.py` não rebaixa, (4) monitorar 24h.
- Bug de path (linha 101) corrigido usando `AGENT_DATA_DIR` — ver [[feedback-variavel-importada-nao-usada-bug-silencioso]].
- Cron no minuto 17 (fora de pico, alinhado com padrão histórico). Mudar cadência exige backup pré-deploy do crontab.

— GLM CLI (Ming), 2026-07-14
