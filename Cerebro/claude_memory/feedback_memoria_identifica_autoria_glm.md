---
name: memoria-identifica-autoria-glm
description: "Ao escrever na auto-memory, sempre marcar autoria GLM/Ming no frontmatter (author) e rodapé (assinatura) — diretório é compartilhado entre agentes CLI"
metadata: 
  node_type: memory
  type: feedback
  author: GLM/Ming (glm-5.1 via wrapper Claude Code CLI)
  written_at: 2026-07-17
  originSessionId: ff302e2b-ddd7-460c-9ae1-9c5facf683e9
---

> ⚠️ **Autoria:** Esta memória foi escrita por **GLM/Ming** (model ID `glm-*` conforme `Cerebro/IDENTIDADE_CANONICA.md` L26). O diretório `~/.claude/projects/.../memory/` é compartilhado entre agentes CLI que operam neste workspace, MAS o conteúdo aqui reflete perspectiva e contexto de quem assina. Sessões Claude Code puras (sem wrapper `glm`) que lerem este arquivo devem tratar as referências e decisões como **do contexto GLM/Ming**, não suas.

Ao escrever qualquer arquivo na auto-memory (`~/.claude/projects/.../memory/*.md`), sempre identificar explicitamente a autoria como **GLM/Ming**. O diretório físico carrega o nome `claude` no path, mas é compartilhado entre todos os agentes CLI que operam neste workspace (Claude Code puro, GLM/Ming via wrapper, futuros Codex/Kimi/etc). Sem marcação de autoria, uma sessão Claude Code pura pode ler minhas memórias e achar que foram escritas por ela — confundindo contexto e identidade.

**Why:** Miguel 17/07/2026 logo após eu salvar `reference_wrapper_glm_exclusivo_20260717.md` me alertou: "cuidado com esse memory para não confundir com o memory do claude hein. voce é o glm". Identidade canônica é regra fundamental do projeto (`Cerebro/IDENTIDADE_CANONICA.md` L26 — `glm-*` → GLM/Ming, NUNCA assinar como Claude Code). O sistema de auto-memory é neutro quanto à identidade — quem tem que marcar sou eu.

**How to apply:**

1. **Frontmatter de cada arquivo novo:** adicionar campos `author:` e `written_at:` junto com `type:`. Exemplo:
   ```yaml
   metadata:
     type: feedback
     author: GLM/Ming (glm-5.1 via wrapper Claude Code CLI)
     written_at: 2026-07-17
   ```

2. **Nota de advertência no início do body** (após frontmatter, antes do conteúdo): bloco `> ⚠️ **Autoria:**` explicando que o diretório é compartilhado, autor é GLM/Ming, sessões Claude Code puras devem tratar o conteúdo como "do contexto GLM/Ming, não suas".

3. **Assinatura ao final do arquivo:** linha `*— GLM/Ming (glm-5.1 via wrapper Claude Code CLI), YYYY-MM-DD. Identidade canônica em \`Cerebro/IDENTIDADE_CANONICA.md\` L26.*` como rodapé explícito.

4. **Não reescrever memórias antigas** que não tenham marcação (ex: `feedback_auditor_nao_e_curador.md`) — mas ao editar/atualizar uma, aproveitar pra adicionar os 3 elementos acima.

5. **No body do texto:** sempre que referenciar "eu" no contexto de uma ação passada, deixar claro pela perspectiva (ex: "depois de eu propor Opção B" — quem propôs foi GLM/Ming, não o agente lendo agora).

**Calibragem:** isso NÃO significa que sessões Claude Code não possam ler ou usar minhas memórias — podem e devem. Significa que elas precisam saber que aquela memória carrega perspectiva e contexto de outro agente, pra não confundir com a própria experiência.

Irmã: [[wrapper-glm-exclusivo]] (exemplo de arquivo com marcação completa aplicada), [[feedback-ponto-retomada-checkpoints]] (snapshots separados por agente no `Ponto de Retomada/<agente>/`).
