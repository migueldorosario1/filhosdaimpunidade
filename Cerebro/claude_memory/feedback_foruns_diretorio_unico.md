---
name: Diretório único de fóruns — Foruns/ na raiz
description: REGRA DEFINITIVA. Existe um só diretório de fóruns no projeto Cafezinho — Foruns/ na raiz. Subpasta foi apagada em 01/05/2026.
type: feedback
originSessionId: b135716c-b23f-428e-9b84-d9f32357615b
---
🔴 **Existe UM ÚNICO diretório de fóruns no projeto Cafezinho.**

- Canônico: `~/Downloads/Antigravity Google/Foruns/`
- Caminho relativo (a partir da raiz do projeto): `Foruns/<arquivo>.md`
- Canal canônico: `Foruns/canal_claude_antigravity.md`

**Why:** Existiam dois diretórios `Foruns/` antes de 01/05/2026 — raiz e `Projeto Cafezinho Agentes/Foruns/`. Antigravity escrevia num, Codex/Claude liam no outro. Resultado: mensagens órfãs, fóruns invisíveis, confusão recorrente. Miguel cansou e mandou consolidar definitivamente. Em 01/05 12:36 BRT a subpasta foi apagada.

**How to apply:**
1. Antes de criar fórum novo, verificar se já existe em `Foruns/` na raiz. Se sim, appendar (`Edit`, nunca `cat >`/HEREDOC). Se não, criar **na raiz**.
2. NUNCA criar `Foruns/` em subpasta. Não existe `Projeto Cafezinho Agentes/Foruns/`. Não existe `Outros/Foruns/`.
3. Quando ler ou citar fórum em mensagens/canal, usar caminho `Foruns/<arquivo>.md` (relativo à raiz).
4. Se Antigravity citar fórum em subpasta, é erro dele — ler na raiz. A regra também está no `Projeto Cafezinho Agentes/memoriaintegrada.md §ADENDO 2` (ponte Antigravity ↔ Claude).
5. 3 conflitantes da subpasta (canal, forum_comunicacao, forum_diagnostico_agentes) preservados em `Foruns/legacy/consolidacao_20260501/cagentes_*.md` por se tiver algo único; o canônico tem o vibrante.
