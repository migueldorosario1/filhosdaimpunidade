---
name: buscador-unificado-miguel-20260717
description: "Buscador unificado em /home/migueldorosario/ferramentas/buscador/ com CLI global `busca`, índice SQLite+FTS5, indexação local funcional (77k arquivos), planejamento pra indexar Drive+B2+R2+servidores. Integração via Bash tool pra Claude/Codex/GLM. MCP server planejado."
metadata: 
  node_type: memory
  type: project
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# Buscador Unificado Miguel — 17/07/2026

Ferramenta pra Miguel (e agentes Claude/Codex/GLM) buscar arquivos em qualquer sistema com um só comando.

## Instalação

- **Root:** `/home/migueldorosario/ferramentas/buscador/`
- **Comando global:** `busca` (alias em `~/.bashrc` + symlink `~/bin/busca`)
- **Índice:** SQLite + FTS5 em `indice/busca.sqlite`
- **README:** `/home/migueldorosario/ferramentas/buscador/README.md`
- **Fórum:** `Cerebro/Foruns/forum_buscador_inteligente_unificado_20260717.md`

## Estado atual (MVP local)

- ✅ Indexação local funcional: `local_workspace` (62.568 arquivos) + `legacy_unificado` (15.492 arquivos) = **77.060 arquivos, 133 GB**
- ✅ CLI `busca` com FTS5 (nome + conteúdo), filtros (sistema, tipo, tamanho, desde), formatos (texto, json)
- ⏳ Indexação Drive/B2/R2 (Fase 2 — a implementar)
- ⏳ Indexação servidores via SSH (Fase 3 — a implementar)
- ⏳ MCP server pra Claude Code (Fase 4 — a implementar)

## Uso rápido

```bash
busca "seo pruning"                                # nome + conteúdo
busca "V4.1" --tipo md --desde 7d --top 20         # filtros
busca "" --min-tamanho 100M --sistema local_workspace
busca --stats                                       # visão geral
busca --sistemas                                    # lista sistemas indexados
busca "backup" --formato json | jq '.[].path'      # pra pipes
```

**Nota FTS5:** query com pontos/hífens (ex: "V4.1") é auto-envolvida em aspas duplas por termo pra evitar erro de sintaxe.

## Como reindexar

```bash
# Local workspace
python3 ~/ferramentas/buscador/indexador/indexar_local.py local_workspace "/home/migueldorosario/Downloads/Antigravity Google"

# Legacy unificado
python3 ~/ferramentas/buscador/indexador/indexar_local.py legacy_unificado /home/migueldorosario/legacy
```

## Cadência sugerida (crons — a instalar)

```
0 4 * * * python3 ~/ferramentas/buscador/indexador/indexar_local.py local_workspace "/home/migueldorosario/Downloads/Antigravity Google"
15 4 * * * python3 ~/ferramentas/buscador/indexador/indexar_local.py legacy_unificado /home/migueldorosario/legacy
```

## Excludes padrão

Ver `config/sistemas.yaml` ou `DEFAULT_EXCLUDES` em `indexador/indexar_local.py`:
- `**/node_modules/**`, `**/__pycache__/**`, `**/venv/**`, `**/.git/**`, `**/*.pyc`
- `**/.wwebjs_auth/**`, `**/.cache/**`, `**/.local/**`, `**/.nvm/**`

## Autor

Claude Code (`claude-opus-4-7`), 2026-07-17 01:20 BRT.
