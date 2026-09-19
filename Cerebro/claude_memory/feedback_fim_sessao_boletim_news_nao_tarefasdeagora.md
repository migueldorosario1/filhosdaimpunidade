---
name: feedback-fim-sessao-boletim-news-nao-tarefasdeagora
description: Ritual de fim-de-sessão NÃO usa Tarefasdeagora.md (legacy desde 12/05). Hoje a sequência é Boletim News + fórum ativo + canal_trindade + inbox do agente.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

A skill `fim` ainda menciona `Tarefasdeagora.md`, mas esse arquivo foi movido para `legacy_Tarefasdeagora.md` em 12/05/2026 e **NÃO deve ser recriado**. Hoje (28/05/2026) o fluxo correto é:

1. **Boletim News** (`CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md` ou `_RIOCARTA.md`) — ponto único de contato. Atenção: alimentado deterministicamente por `root/gerar_boletim_news.py`; só editar manualmente a seção "Estado atual"/"Frentes recentes" quando pertinente.
2. **Fórum ativo da tarefa** (em `Foruns/`).
3. **Canal Trindade** (`Foruns/canal_trindade.md`) — recado curto pra Trindade saber que sessão fechou.
4. **Inbox do agente** (`Foruns/inbox_trindade/claude.md`) — recado curto na cauda (§24) pra próxima sessão Claude.

**Why:** Miguel corrigiu em 28/05 17:16 BRT após eu criar `Tarefasdeagora.md` na raiz: "esse tarefasdeagora.md a gente não tinha colocado no legacy há dias? hoje a gente está usando o boletim news". Logo depois: "além dos fóruns, canal e inbox" — confirmando que o fim-de-sessão tem 4 canais (Boletim News + fórum + canal + inbox), não apenas 1-2.

**How to apply:** Ao executar ritual de fim-de-sessão, NUNCA recriar `Tarefasdeagora.md`. Apender resumo em: (a) fórum ativo da frente, (b) `canal_trindade.md`, (c) inbox próprio (`inbox_trindade/claude.md`) na cauda com assinatura `— Claude` + timestamp, (d) Boletim News do portal pertinente se houver mudança estrutural relevante. Se a skill `fim` mandar tocar `Tarefasdeagora.md`, interpretar como instrução desatualizada e seguir o fluxo Boletim News.
