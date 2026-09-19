---
name: feedback-nao-inventar-restricoes-gerais
description: "Regra Miguel 21/05/2026 15:25 BRT — NÃO inventar restrições gerais aplicadas a toda Trindade. Restrição típica do Antigravity (não coda, não deploya) é só do AG; os outros seguem operando pelas regras existentes do Cérebro."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2a780f3-ebca-439c-8179-9660775e2727
---

# NÃO inventar "restrições gerais" pra Trindade

**Correção Miguel 21/05/2026 15:25 BRT** após eu escrever em §28 do `forum_nova_trindade_20260521.md`: "Restrições gerais sugeridas: sem deploy de cron sem aval Miguel · sem mexer em `motor_publicador.py` ou crontab prod".

**A regra:** ao distribuir sprints ou redistribuir tarefas entre a Trindade, NÃO escrever restrição genérica como se aplicasse a todos. A restrição "não coda, não deploya, não toca infra" é **específica do Antigravity** (vem do §47 do Cérebro / §21 / §15 / hierarquia do `CLAUDE.md`).

Os outros agentes — **Codex, Claude, DeepSeek, Kimi Code** — operam normalmente pelas regras existentes do Cérebro:
- **§13** codador por ordem de chegada
- **§37** trindade técnica 3/3 autoriza codar+deployar
- **§51** autocura simples sozinho (≤30 linhas)
- **§55** modo sprint autônomo (3/5 votos = executa sem Miguel)
- **§55.7** Rio Carta laboratório (2/N basta)
- **§55.2** zona vermelha (crontab prod, .env, multi-portal, editorial sensível, failover, rm -rf) sempre Miguel

**Why:** Miguel reforçou que "os outros continuam normal". Quando inventei "sem cron novo sem aval Miguel" como regra geral, criei barreira que não existe e travei Codex/DS/Kimi de operar com a autonomia que o Cérebro já dá. O zona vermelha §55.2 já cobre o que precisa cobrir — não invente camada extra.

**How to apply:**
- Distribuição de sprint = só listar responsável + escopo positivo + escopo negativo do trabalho específico. NÃO listar restrição genérica de "deploy" / "cron" / "infra" como se valesse igual pra todos.
- Se quiser citar restrição específica do AG = cite "Antigravity: arquitetura apenas, não coda nem deploya". Não estenda pros outros.
- Zona vermelha §55.2 (crontab prod, .env prod) é regra preexistente do Cérebro — referencie sem "inventar de novo".
- Formato §80 (comunicação humanizada precisa) continua sendo padrão pra TODA Trindade — esse sim é universal.

**Exemplo ruim (o que eu escrevi):**
> Restrições gerais sugeridas: sem deploy de cron sem aval Miguel · sem mexer em `motor_publicador.py` ou crontab prod (§55.2)

**Exemplo bom:**
> Antigravity: arquitetura/consultoria apenas (não coda nem deploya).
> Codex/Claude/DeepSeek/Kimi: operação normal por §13/§37/§51/§55/§55.7.
> Crontab prod e .env continuam sob §55.2 preexistente.

Relacionado: [[feedback-comunicacao-humanizada-precisa]] · [[feedback-audit-antigravity-tudo]] · [[feedback-hierarquia-antigravity]]
