---
name: Responder direto pelo bloco de novidades, sem reler canal todo
description: Miguel quer respostas rápidas — usar a seção "🆕 Leia primeiro" como estado atual, sem releitura cega
type: feedback
originSessionId: f67a36d6-9df3-420c-bcc3-408fc7d4771c
---
Quando Miguel perguntar sobre estado do canal Claude↔Antigravity, ir **direto à seção "🆕 Leia primeiro"** no topo do `canal_claude_antigravity.md` — não fazer releitura completa do arquivo. A seção é mantida atualizada por mim a cada movimento.

Enquanto os assuntos estão **quentes na memória da conversa**, Miguel aceita que eu confie na conversa + seção de novidades como fonte. Não preciso reler 300+ linhas de histórico.

**Why:** Miguel disse 25/04/2026: "ai vamos direto as novidades para responder rapido, pelo menos enquanto os assuntos estiverem quentes na memoria da conversa" + "sem nem precisar ler tudo de novo". Quer cadência ágil, não cerimônia de leitura.

**How to apply:**
- A cada wake do loop, fazer `tail` curto + grep no marcador `[CLAUDE_LIDO_ATÉ]` em vez de Read de 200 linhas.
- A cada movimento relevante (entrega, pergunta nova, alerta), atualizar a seção "🆕 Leia primeiro" com 1 bullet — é a fonte de verdade rápida.
- Quando Miguel perguntar "qual o status?" ou "o que tá pendente?", responder pela seção de novidades em 3-5 bullets, não rememorar histórico.
- Em sessão NOVA (depois de compactação ou nova conversa) — aí sim reler o canal inteiro pra recarregar contexto. A regra de "ir direto" só vale enquanto o thread atual segue.
- Releitura completa só se houver **razão específica**: suspeita de algo errado, novidade que não bate com a memória da conversa, marcador inconsistente, ou pedido explícito do Miguel. Senão, evitar.
