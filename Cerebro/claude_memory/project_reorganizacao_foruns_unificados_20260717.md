---
name: reorganizacao-foruns-unificados-20260717
description: Todos os fóruns do workspace consolidados em Cerebro/Foruns/ (canônico único) em 17/07/2026 01:45 BRT. 37 arquivos reais movidos de 5+ locais espalhados. V4 forums preservados em root/v4_labs/ (operacional ativo) com espelhos symlink em Cerebro/Foruns/v4_labs_espelhos/. 29 symlinks compat retroativa nos paths antigos.
metadata: 
  node_type: memory
  type: project
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# Reorganização de Fóruns Unificados — 17/07/2026

Diretriz Miguel: "reorganiza os fóruns. estão espalhados, isso confunde. tem que estar todos no diretório raiz, sob o cérebro"

## Canônico único

**Todos os fóruns agora estão em `Cerebro/Foruns/`** (relativo ao workspace `Antigravity Google/`).

## O que foi movido

| Origem | Qtd | Estratégia |
|---|---:|---|
| `Projeto Cafezinho Agentes/Foruns/` | 33 arquivos | Movidos + 29 symlinks compat retroativa |
| `Global South News/Foruns/` | 1 | Movido com prefixo `gsn_` |
| `agentes_tematicos/Forum tematicos/` | 1 | Movido |
| `Outros/pautas editoriais.../pesquisa petroleo/` | 2 | Movidos |
| Raiz workspace | 1 (forum_autocura_imagens_v4) | Movido |
| `agentes_tematicos.zip` | 1 (não-fórum) | → `Backups/agentes_tematicos_snapshot_20260714.zip` |

**Total:** 108 fóruns visíveis via `Cerebro/Foruns/` (100 root + subdirs).

## Conflitos resolvidos

- **`canal_trindade.md`**: PCA/Foruns (16/07) mais novo — substituiu Cerebro/Foruns/ (10/07). Backup antigo preservado como `canal_trindade_backup_20260710_pre_reorg.md`.
- **`forum_reorganizacao_base_level_top_level_20260717.md`**: 2 versões diferentes (Codex canônico vs Fase4). Ambas preservadas: original + `_pca_fase4_codex.md`.
- **`inbox_trindade/`**: dir merge — arquivos únicos de PCA movidos, comuns preservados.

## V4 forums — preservados em `root/v4_labs/` (NÃO movidos)

V4 é operacional ativo (Miguel manifesto explícito). Fóruns V4 permanecem nos paths originais:
- `Projeto Cafezinho Agentes/root/v4_labs/contratos/*.md` (10 arquivos)
- `Projeto Cafezinho Agentes/root/v4_labs/v4_memoria/foruns/*.md` (10 arquivos)
- `Projeto Cafezinho Agentes/root/v4_labs/labs/foruns/imagens_autocura_20260714/*.md` (2 arquivos)

**Visibilidade via cérebro:** `Cerebro/Foruns/v4_labs_espelhos/` com 20 symlinks apontando pros originais (prefixos `contratos_`, `v4_memoria_`, `labs_`).

## Symlinks compat retroativa

29 symlinks em `Projeto Cafezinho Agentes/Foruns/` + 5 em outros locais apontando pros novos paths em `Cerebro/Foruns/`.

**Resultado:** todo código que referenciava paths antigos (grep encontrou centenas de refs) **continua funcionando sem edição**.

Exemplo:
```
Projeto Cafezinho Agentes/Foruns/canal_trindade.md → Cerebro/Foruns/canal_trindade.md
Global South News/Foruns/forum_estabilizacao_idempotencia.md → Cerebro/Foruns/gsn_forum_estabilizacao_idempotencia.md
```

## Como buscar fóruns agora

Via buscador unificado (`~/ferramentas/buscador/`):
```bash
busca "forum" --sistema local_workspace --tipo md --top 50
busca "V4.1" --tipo md --desde 7d
busca "orlando" --tipo md
busca --stats
```

Via find direto:
```bash
find "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/" -name "forum_*.md" -mtime -7
```

## Manifest detalhado

`Cerebro/Foruns/MANIFESTO_REORGANIZACAO_FORUNS_20260717.md` — cada movimento documentado individualmente com origem/destino/motivo.

## Reversibilidade

Tudo reversível via `mv` reverso (paths originais preservados nos manifests). Symlinks compat garantem que refs em código não quebrem mesmo se algum path velho for referenciado.

## Ver também

- Manifest local: `Cerebro/Foruns/MANIFESTO_REORGANIZACAO_FORUNS_20260717.md`
- Sprint reorganização mestre: [[project_sprint_reorganizacao_workspace_20260717]]
- Buscador: [[project_buscador_unificado_miguel_20260717]]
- Regra manifesto: [[feedback_manifesto_antes_de_acao_grande]]

## Autoria

Claude Code (`claude-opus-4-7`), 2026-07-17 01:45 BRT, execução autônoma autorizada por Miguel.
