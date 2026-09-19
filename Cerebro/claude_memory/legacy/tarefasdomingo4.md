---
name: Tarefas domingo 4 (2026-04-19 → 100% resolvido 2026-04-22) — Fix Mailchimp LIVE
description: Caixa de newsletter AJAX + agente_turismo_embratur deployados 2026-04-20. Envio diário 07:30 validado em produção — últimas execuções 20+21/04 OK.
type: project
originSessionId: 5463c220-6a29-496f-875a-64c9d5fac390
---
# Tarefas — domingo 2026-04-19 (retomado e concluído 2026-04-20 ~09:15)

## ✅ Concluído

### 1. Formulário AJAX no `motor_publicador.py`
- Constante `CAIXA_NEWSLETTER_AJAX` no topo (linha 39), consumida via `html += CAIXA_NEWSLETTER_AJAX` (linha 1143).
- Servidor Tencent e local têm md5 idêntico em 2026-04-20.
- A "duplicação LOCAL" mencionada na versão antiga desta memória já havia sido reconciliada.

### 2. `agente_newsletter_mailchimp.py` — path do .env corrigido
- Fallback `/root/.env` quando rodando no servidor. Deployado em 2026-04-19.
- API Mailchimp responde "Everything's Chimpy!".

### 3. `agente_turismo_embratur.py` — caixa de newsletter injetada (2026-04-20)
- Deploy cirúrgico: partimos da versão do servidor e aplicamos só 2 hunks.
- Import: `from motor_publicador import CAIXA_NEWSLETTER_AJAX` (com fallback `""`).
- Antes do `postar_wp` Cafezinho: `body_pt_com_caixa = pt_data["body_html"] + CAIXA_NEWSLETTER_AJAX`.
- Post GSN/EN fica intocado (sem caixa).
- Backup server: `/root/agente_turismo_embratur.py.bak_antes_caixa_20260420_091501`.
- md5 final confirmado idêntico local↔servidor.

## ⚠️ Atenção pra próxima sessão

A versão local do `agente_turismo_embratur.py` tem OUTRAS mudanças que NÃO estão no servidor
(figcaption injection com `injetar_figcaption_do_media` + legenda aprovada pelo Tribunal passada
pro upload via `fazer_upload_imagem_wp(..., legenda=legenda_aprovada)`). Essas mudanças são de
outra sessão, não foram validadas e NÃO foram deployadas. Se for retomar esse arquivo, decidir
o que fazer com elas antes de rsync geral.

## ✅ Envio matinal validado em produção (2026-04-22)

- Cron `30 7 * * *` rodou em 19, 20 e 21/04 (syslog confirma disparo).
- Últimas 2 execuções OK: campanhas `59e52384cb` (20/04) e `81c4f10966` (21/04) enviadas.
- Erro 400 "address not ready" não reaparece — painel Mailchimp (Sender Domain/DKIM) foi acertado.
- Log canônico: `/root/agent_data/newsletter.log` no Cingapura.
