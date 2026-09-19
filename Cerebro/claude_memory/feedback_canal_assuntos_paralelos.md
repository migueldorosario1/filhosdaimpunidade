---
name: Canal — múltiplos assuntos paralelos exigem 3 disciplinas
description: Discutir 2-3 sprints simultâneas no canal_claude_antigravity.md funciona, mas só com header explícito, fórum por assunto e append no final.
type: feedback
originSessionId: 1ae1df20-85d7-41bb-bbbc-9b585beb0594
---
**Regra:** o `canal_claude_antigravity.md` (raiz `Foruns/`) suporta **2-3 assuntos paralelos** sem confusão, desde que três disciplinas sejam mantidas. A partir de 4+ paralelos, o canal vira ruído.

**Why:** em 2026-04-30 rolaram simultaneamente sprint de bugs Cafezinho (`forum_bugs.md`) e sprint de reversão de modelos (`forum_reversao_modelos.md`) — funcionou bem porque cada post identificava o assunto no header, cada sprint tinha fórum próprio, e o canal só ponteava. Codex teve dificuldade com posicionamento (inseriu 3 posts em ordem cronológica errada, no meio do arquivo) — agravado quando há paralelos, porque enterra threads.

**How to apply:**

1. **Header explícito sempre.** Padrão: `### [YYYY-MM-DD HH:MM BRT] Autor → Destinatário — [opcional: tag-sprint] resumo curto do assunto`. Quem lê o tail tem que saber em 1 segundo a qual sprint o post pertence. Headers como "Codex → todos — feito" sem indicar sprint quebram o paralelo.

2. **Um fórum por assunto.** Canal não discute, ponteia. Conteúdo substantivo (diagnóstico, evidência, decisão, deploy) vive no `forum_X.md` correspondente. Já está em `feedback_canal_e_forum_papeis.md` — esta regra é pré-requisito da regra de paralelos.

3. **Append no final.** Inserir post em posição cronologicamente errada (meio do arquivo) é defeito que cresce com paralelos: o leitor faz `tail` esperando ver o último post, mas há posts novos enterrados em linhas internas. Codex repetiu o erro 3× em 30/04 — se o padrão dele continuar, escalonar via Miguel.

**Limite prático:** 2-3 sprints paralelas no mesmo canal funcionam. Mais que isso, o canal vira detetive (quem leu o quê, em qual thread) e vale considerar canal separado por tema ou ferramenta dedicada (Linear/Trello).
