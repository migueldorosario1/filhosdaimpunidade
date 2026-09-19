# Memórias Claude — sincronizadas entre MIGUEL e LAURA

Este diretório contém TODAS as memórias auto do Claude Code do projeto Cafezinho, sincronizadas via GitHub `cerebro-miguel` pra que ambas instâncias (Claude Miguel + Claude Laura) tenham conhecimento simétrico.

## Origem canônica

- **Escrita canônica:** `~/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory/` no PC MIGUEL
- **Sincronizado para:** este diretório (`cerebro-miguel/cerebro/claude_memory/`) via cron
- **Distribuído para:** Laura via `git pull` (cron `*/15`)

## Como Claude Laura carrega essas memórias

Em Laura (Windows 11 ARM64, Claude Code), o path canônico de memórias é:
```
%USERPROFILE%\.claude\projects\<encoded_path>\memory\
```

Ou dentro do WSL Ubuntu:
```
~/.claude/projects/<encoded_path>/memory/
```

Onde `<encoded_path>` é o path do projeto Cafezinho onde Claude Laura foi iniciado, com `/` substituído por `-`.

**Setup uma vez em Laura:**
```bash
# Descobrir o encoded path da sessão Laura
ls ~/.claude/projects/
# Ex: -mnt-c-Users-Miguel-Cerebro   ou similar

# Sincronizar memórias
LAURA_MEM=~/.claude/projects/<encoded_path>/memory
mkdir -p "$LAURA_MEM"
rsync -a --exclude='00_COMO_USAR.md' ~/cerebro-miguel/cerebro/claude_memory/ "$LAURA_MEM/"
```

**Depois disso, todo ciclo:**
```bash
# Cron a cada 15min: puxa novidades do Miguel
cd ~/cerebro-miguel && git pull --quiet
rsync -a --exclude='00_COMO_USAR.md' ~/cerebro-miguel/cerebro/claude_memory/ ~/.claude/projects/<encoded_path>/memory/
```

## Escrita bidirecional

Se Claude Laura escrever memória nova (aprendizado local), deve **também** copiar pro repo:
```bash
rsync -a ~/.claude/projects/<encoded_path>/memory/ ~/cerebro-miguel/cerebro/claude_memory/
cd ~/cerebro-miguel && git add cerebro/claude_memory/ && git commit -m "claude-laura: memória atualizada" && git push
```

Claude Miguel tem cron `*/15` que puxa e re-sincroniza local.

**Conflito de merge:** se dois lados editarem MEMORY.md ao mesmo tempo, prevalece a versão do MIGUEL (canônico). Perda mínima porque MEMORY.md é só índice — arquivos individuais raramente colidem.

## O que Laura ganha carregando essas memórias

Todo o conhecimento acumulado por Claude Miguel:
- Regras editoriais Cafezinho (título auditor 7 regras, fonte invisível, metalinguagem = bug #1, etc)
- Protocolo Trindade Daemon + reservas + loops sincronizados
- Contexto operacional (worker V4, ponte imagens ZCode, Grok Fase 2+, cadência 30min/1h, teto fila 12h)
- Referências permanentes (Mojtaba Khamenei líder supremo Irã, computadores MIGUEL/LAURA, backups)
- Feedback correcional (migração canal, erros reincidentes estruturais, aparelhos que Grok pode/não pode)

Sem essas memórias, Laura reinicia do zero a cada sessão. Com elas, comporta-se como continuação da mesma inteligência editorial.

## Sync automatizado (a implementar)

Script `sync_claude_memory.sh` em `~/bin/` pode automatizar isso. Estrutura sugerida:

```bash
#!/bin/bash
# Executa a cada 15min via cron nos 2 PCs
LOCAL_MEM="$HOME/.claude/projects/-home-migueldorosario-Downloads-Antigravity-Google/memory"
REPO_MEM="$HOME/cerebro-miguel/cerebro/claude_memory"

# Push local → repo
rsync -a --exclude='00_COMO_USAR.md' "$LOCAL_MEM/" "$REPO_MEM/"

# Pull repo → local (após git pull do repo)
rsync -a --exclude='00_COMO_USAR.md' "$REPO_MEM/" "$LOCAL_MEM/"

# Commit se houver mudança
cd "$HOME/cerebro-miguel" && git add cerebro/claude_memory/ && git diff --cached --quiet || {
  git commit -m "claude-memory: sync automático $(date -u +%Y%m%d-%H%M%S)"
  git push
}
```

Miguel precisa criar isso em ambos os PCs e agendar via cron.

---

*Este arquivo é meta-documentação, NÃO é memória Claude (ficaria estranho carregar isso na sessão). Manter fora do rsync final via `--exclude='00_COMO_USAR.md'`.*
