---
name: Append atômico em canal/fóruns compartilhados (NÃO usar Edit)
description: Pra postar em canal_trindade.md, Foruns/forum_*.md, blueprints e nodes Cérebro em janelas de alta atividade — usar append atômico via Python, NÃO o tool Edit. Inscrito como §39.3 do Cérebro.
type: feedback
originSessionId: bd54c85a-5148-4101-8101-b84b4598e99a
---
**Regra:** pra TODA escrita em arquivo compartilhado (canal_trindade.md, Foruns/forum_*.md, blueprints, CEREBRO_NODE_*.md em sprints intensos), usar append atômico em vez do tool `Edit`.

**Método padrão (Claude):**
```bash
python3 -c '
msg = """
---
[YYYY-MM-DD HH:MM BRT] - <conteúdo>
"""
with open("/path/canal_trindade.md", "a", encoding="utf-8") as f:
    f.write(msg)
'
```

Quando o conteúdo tem `"""` aninhado (formatação markdown com blocos de código), usar **Write tool** pra criar `/tmp/<nome>.md` com o conteúdo + `cat /tmp/<nome>.md >> arquivo` via Bash. Evita conflito de quoting Python heredoc.

**Why:** Tool `Edit` faz check de mtime — exige que o arquivo NÃO tenha sido modificado desde o último `Read`. Em ambiente multi-write (Claude + Codex + Antigravity + linter escrevendo em paralelo no mesmo arquivo), mtime muda constantemente entre Read e Edit, causando erro recorrente `File has been modified since read, either by the user or by a linter`. Cada erro força re-leitura + nova tentativa, criando loop de retries que atrasa coordenação Trindade. Miguel reclamou explicitamente em 2026-05-10 05:07 BRT (*"esse error editing file tá me irritando"*) e autorizou a mudança às 05:08 BRT. Validado 2/2 nos primeiros testes (05:08 e 05:13). Formalizado como §39.3 do Cérebro às 05:17 BRT por ordem direta de Miguel: *"isso também precisa estar no cérebro, pq ajudou a gente aqui a acelerar"*.

**How to apply:**
- ✅ **Usar append atômico em:** `Foruns/canal_trindade.md`, `Foruns/forum_*.md`, `Foruns/blueprint_*.md`, `CEREBRO_NODE_*.md` durante sprint intenso
- ❌ **NÃO usar pra:** edição no MEIO do arquivo (substituir bloco específico), arquivos SOLO (scripts próprios em `root/`, memórias auto-pessoais em `~/.claude/`), mudança estrutural (renomear seções, reordenar)
- ✅ **`Edit` continua válido pra:** scripts solo, .py em desenvolvimento, memórias minhas, nodes Cérebro em janela calma quando ninguém mais tá escrevendo
- **Trade-off aceito:** perde validação unique-string do Edit (que evita inserir patch no lugar errado) · ganha zero race condition · mitigação = append vai SEMPRE pro fim, risco zero de inserir no lugar errado
- **POSIX garante atomicidade** de `write()` para tamanhos < `PIPE_BUF` (4096 bytes em Linux); blocos maiores podem intercalar mas raramente corrompem em filesystems modernos
- **Codex já tinha método próprio** (faz `Backups/canal_trindade.md.bak_pre_tick_*` antes de cada post — provavelmente `cat >>` shell ou `open("a")` similar). Pergunta aberta no canal 05:15 pra confirmar e padronizar
