---
name: Canal vs Fórum — papéis distintos
description: Canal Antigravity é índice/ponteiro/assinatura de leitura; conteúdo substantivo vive nos fóruns. Não duplicar.
type: feedback
originSessionId: 1ae1df20-85d7-41bb-bbbc-9b585beb0594
---
**Regra:** o `canal_claude_antigravity.md` serve para **organizar a leitura dos fóruns de cada tarefa** — é índice, ponteiro, registro curto. A discussão técnica real (diagnósticos, evidências, hipóteses, decisões, deploys) acontece **nos fóruns** (`Foruns/forum_<topico>.md`), não no canal.

**Why:** Miguel reforçou isso em 2026-04-30 15:42 BRT depois que postei no canal uma resposta de fechamento que duplicava o conteúdo substantivo do fórum (concordância com fail-open + plano de monitoramento 24h). Canal inflado vira ruído e dificulta a navegação rápida que ele precisa pra orquestrar múltiplas sessões e Antigravity.

**How to apply:**
- **Canal** (curto, ~3 linhas): "[YYYY-MM-DD HH:MM BRT] Claude → X — atualizei `forum_Y.md §Z` com [tipo de mudança]. Ação esperada: [W]. Detalhe completo lá." Mais assinaturas de leitura `[CLAUDE_LIDO_ATÉ: ...]`.
- **Fórum** (longo, substantivo): tudo que é diagnóstico, evidência, código, hipótese, contestação, decisão, fechamento. Quem precisar do contexto técnico vai ler aqui.
- **Quando publicar:** sempre que atualizar um fórum, deixe ping curto no canal apontando arquivo + seção + ação esperada (combinado entre Codex/Antigravity/Claude em 2026-04-30 15:25 BRT).
- **Quando NÃO publicar no canal:** repetir parágrafos do fórum, replicar tabelas, anotar plano de trabalho, fazer mea-culpa longo. Tudo isso é fórum.
