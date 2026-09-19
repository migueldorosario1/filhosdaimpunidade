---
name: feedback-limpeza-diaria-inbox
description: "Regra permanente — todo dia limpar os inboxes de todos os agentes (`inbox_trindade/*.md`) com backup antes. Se última mensagem for antiga (>24h) e o inbox estiver poluído, esvaziar (deixar só header) e criar entrada nova."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 07b6c459-6a0f-4880-a779-68996b652812
---

🧹 **Limpeza diária de inbox** — regra estabelecida por Miguel em 2026-07-30 17:25 BRT.

**Regra:** todo dia, no fim do sprint ou no início do dia seguinte, o agente Claude (ou quem estiver responsável pelo Loop Vigília) faz:

1. **Backup completo** de `Cerebro/Foruns/inbox_trindade/*.md` em `Cerebro/Backups/inbox_YYYY-MM-DD/` antes de qualquer edição.
2. **Esvazia inboxes com última mensagem >24h antiga** (deixar só o header ou a última mensagem realmente relevante).
3. **Aplica também ao `canal_trindade.md`** quando o Miguel disser que "canal Trindade está limpinho" ou quando ele tiver >200 linhas. Backup igual.
4. **Cria novo inbox** quando a última missão for muito antiga (>72h sem atividade) e o arquivo estiver com >50 linhas de ruído — isso evita crescimento perpétuo.
5. **Regra do lixo semântico:** entradas de "ping ciente, sem ação" e "ACK" podem ser removidas na limpeza. Entradas com decisões, aprovações, ou marcos importantes NÃO. Se em dúvida, preserva.

**Razão da regra:** Miguel disse literalmente 30/07 17:25 BRT: "esse inbox tem que ser limpado todos os dias, viu? Pra todo mundo ficar sempre o inbox limpinho, bota aí na regra, todos os dias limpar, faz o backup e limpa sempre que demorar muito, faz um novo inbox".

**Motivação:** inboxes acumulados ficam ilegíveis, misturam sinais importantes com ping ciente, e o Miguel perde tempo pra achar o que realmente precisa de atenção. Melhor um inbox pequeno e recente.

**Aplicação prática (ao final do dia ou primeira coisa da manhã):**

```bash
# 1. Backup
mkdir -p Cerebro/Backups/inbox_$(date +%Y-%m-%d)
cp Cerebro/Foruns/inbox_trindade/*.md Cerebro/Backups/inbox_$(date +%Y-%m-%d)/

# 2. Para cada inbox com >24h de idade da última mensagem:
#    - se tem entradas relevantes: preserva as últimas 3-5 relevantes, remove ping/ACK
#    - se só tem pings: esvazia deixando header + timestamp de limpeza
```

**Formato pós-limpeza (mínimo):**
```markdown
# Inbox: <agente>

*Limpo em <YYYY-MM-DD HH:MM BRT> por Claude. Backup em `Cerebro/Backups/inbox_<YYYY-MM-DD>/<agente>.md`.*

---
```

**Vinculações:** [[feedback-canal-inbox-apenas-ponteiro-carta-no-chat-e-forum]] · [[feedback-cartinha-como-md-com-link-no-final]]
