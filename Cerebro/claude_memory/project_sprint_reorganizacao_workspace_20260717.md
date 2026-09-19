---
name: sprint-reorganizacao-workspace-20260717
description: "Sprint 17/07/2026 de reorganização massiva do workspace Antigravity Google - moveu 22 itens (~10GB) pra ~/legacy/ unificado com manifest+INDEX+inventario, criou skeleton Cafezinho Espelho No-Index, consolidou subcerebro em Cerebro/subcerebro_antigravity_desktop/, mapeou estrutura alvo simplificada em Cerebro/mapa_reorganizacao_20260717.md. Backup Drive workspace completo em curso. Buscador unificado local MVP funcionando em /home/migueldorosario/ferramentas/buscador/. Fases estruturais grandes (rename Cafezinho Canonico, Sites Tematicos, organizar Cerebro) aguardando backup completo."
metadata: 
  node_type: memory
  type: project
  originSessionId: 37e2f19f-f9dc-43d8-a2fa-f9029a716a89
---

# Sprint reorganização workspace 17/07/2026

**Duração:** sessão ~5h (16/07 22:00 → 17/07 01:30 BRT)

## Diretrizes Miguel

1. **Poucos diretórios na base**, tudo organizado em subdiretórios
2. **Buscador inteligente** vinculado a Claude/Codex/GLM
3. **Fórum específico** pra ferramenta de busca
4. **Manifesto extremamente detalhado** antes de qualquer ação — permite reverter
5. **MOVE only, never DELETE** — nada é apagado, tudo vai pra legacy
6. **Backup Drive + B2 antes de continuar** com reorganização estrutural (rede de segurança)
7. **Cuidado com V4** — sistema em construção, não mover arquivos ativos
8. **Autonomia autorizada** desde que manifesto rigoroso + move-only

## O que foi feito

### FASES CONCLUÍDAS (baixo/médio risco)

| Fase | Descrição | Resultado |
|---|---|---|
| 1 | 12 legacys explícitos → `~/legacy/` | 5.8 GB, 63.855 arquivos |
| 3 | 84 arquivos soltos raiz (V3, análises solar, testes, lixo) → `~/legacy/` em 7 categorias | 184 MB |
| 4 | 6 backups históricos Cerebro/Foruns → `~/legacy/` | ~1 MB |
| 5 | Subcérebro consolidado em `Cerebro/subcerebro_antigravity_desktop/` + symlinks compat retroativa | 4 arquivos + 3 baks pro legacy |
| 7 | Skeleton `Cafezinho Espelho No-Index/` criado | README |
| 2 (parcial) | Duplicatas antigas óbvias (Rio Carta Outros 4G, RC App, MT antigo, rio_carta smoke raiz) → `~/legacy/` | 4.8 GB |

### FASES A/B/C CONCLUÍDAS (planning + buscador)

| Fase | Descrição | Local |
|---|---|---|
| A | Mapa reorganização estrutural completa (10 dirs base) | `Cerebro/mapa_reorganizacao_20260717.md` |
| B | Fórum buscador inteligente unificado + arquitetura | `Cerebro/Foruns/forum_buscador_inteligente_unificado_20260717.md` |
| C | Buscador MVP local funcionando | `/home/migueldorosario/ferramentas/buscador/` |

### REVERSÕES importantes

Depois de Miguel enviar manifesto canônico `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`, reverti 4 movimentos que afetavam dirs ATIVOS:
- `sites-tematicos/mapa_rio` (146 MB) — Miguel trabalhando hoje
- `sites-tematicos/discover_brazil_news` (63 MB) — canônico Miguel
- `sites-tematicos/rio_carta` — canônico Miguel
- `agentes_tematicos.zip` — relacionado ao dir canônico

**Lição:** timestamp isolado NÃO indica ativo/inativo — pode haver plano V4.1 em curso mesmo sem mods recentes. **Consultar manifesto Miguel ANTES de julgar "antigo".**

### FASES PENDENTES (alto risco, aguardando backup)

- **Fase 6**: Rename `Projeto Cafezinho Agentes` → `Cafezinho Canonico` (803 refs em código)
- **Fase 8**: Criar `Sites Tematicos/` + mover silos (Rio Carta Agentes, Global South News, Cicero Agentes, aiatolah)
- **Fase 9**: Organizar Cerebro (deduplicar índices)
- **Fase 10B**: Backup workspace Drive (63.89 GB — em curso agora)

## Estruturas criadas

### Legacy unificado

**Path:** `/home/migueldorosario/legacy/`

**Estrutura:**
```
~/legacy/
├── INDEX.md                                       # linha por item, grep-friendly
├── PLANO_REORGANIZACAO_20260717.md                # plano completo detalhado
├── BACKUP_DRIVE_20260717/
│   ├── MANIFEST.md                                # backup Drive workspace
│   └── inventario_local_completo.tsv              # 296k arquivos
├── scripts/mover_pra_legacy.py                    # gera manifest+inventario ao mover
├── _logs/                                         # logs cronológicos
└── <slug>_20260717/                               # 22+ items movidos
    ├── MANIFEST.md
    ├── inventario.json
    └── (conteúdo)
```

**Script canônico:** `python3 ~/legacy/scripts/mover_pra_legacy.py "<origem>" "<slug>" "<motivo>"`

### Buscador unificado

**Path:** `/home/migueldorosario/ferramentas/buscador/`

**Comando global:** `busca` (alias `.bashrc` + symlink `~/bin/busca`)

**Índice:** SQLite + FTS5 em `indice/busca.sqlite`

**Uso:**
```bash
busca "seo pruning"                                # nome + conteúdo
busca "V4.1" --tipo md --desde 7d --top 20
busca --stats
busca --sistemas
busca "" --min-tamanho 100M --sistema local_workspace
```

**Indexadores:**
- ✅ `indexar_local.py` — feito, 77k arquivos indexados (workspace + legacy)
- ⏳ `indexar_rclone.py` — a implementar (Drive + B2 + R2)
- ⏳ `indexar_ssh.py` — a implementar (Tencent, NYC, ServerDo.in, GSN, cafezinho.news)
- ⏳ `mcp_server_busca.py` — a implementar (integração nativa Claude Code)

### Subcerebro consolidado

**Path:** `Cerebro/subcerebro_antigravity_desktop/`

Contém:
- `sub_cerebro_antigravity_desktop.md` (arquivo principal)
- `sub_cerebro_antigravity_miguel.md`
- `inbox_antigravity_desktop.md`
- `snapshots/` (Ponto de Retomada Antigravity Desktop)
- `README.md`

**Symlinks compat retroativa criados** nos paths antigos (`Projeto Cafezinho Agentes/Foruns/sub_cerebro_*`) apontando pros novos. Refs antigas continuam funcionando.

## Backups em curso/concluídos

### Codex (concluído)

- **B2:** `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/`
- **Escopo:** V4 (root/v4 + root/v4_labs) + Sites Tematicos (10 dirs)
- **Formato:** 2 tar.gz + manifest + hashes SHA256 + índice origem→destino
- **Validação:** `rclone check --one-way --size-only` = 0 diferenças
- **Fórum:** `Projeto Cafezinho Agentes/Foruns/forum_backup_v4_tematicos_backblaze_20260717_004222.md`

### Claude (em curso)

- **Drive:** `drive:orlando diniz/` (delta 256 arquivos) + `drive:backup 20260717/` (workspace 63.89 GB)
- **Escopo:** workspace completo excluindo Orlando (já espelhado), node_modules, __pycache__, venv, .git, sessions, cache
- **Progresso:** Orlando 188 restantes (de 256), backup workspace v2 iniciando
- **Manifest:** `~/legacy/BACKUP_DRIVE_20260717/MANIFEST.md`

## Estrutura alvo (proposta em mapa_reorganizacao_20260717.md)

```
Antigravity Google/
├── README.md, CLAUDE.md
├── 01_Cerebro/
├── 02_Cafezinho_Canonico/                    # renomeado de Projeto Cafezinho Agentes
├── 03_Cafezinho_Espelho_NoIndex/             # já criado
├── 04_Sites_Tematicos_Silos/                 # rio_carta, gsn, cicero, aiatolah movidos
├── 05_Agentes_Tematicos/                     # renomeado
├── 06_Ferramentas/                           # buscador, AGY, github_work
├── 07_Dados_e_Bancos/                        # banco_midia, agent_data
├── 08_Outros/                                # pessoais mistos
└── 99_Backups_Locais/                        # Backups + backups_ceo_cerebro
```

## Próximo (retomar depois do backup Drive terminar)

1. Executar Fase 6 (rename Projeto Cafezinho Agentes → 02_Cafezinho_Canonico) — 803 refs, estratégia sed em batch
2. Executar Fase 8 (mover silos pra 04_Sites_Tematicos_Silos) — cuidado com refs
3. Executar Fase 9 (organizar Cerebro internamente)
4. Implementar Fase C.2 (buscador cloud: Drive + B2 + R2)
5. Implementar Fase C.3 (buscador servidores via SSH)
6. Implementar Fase C.4 (MCP server pro Claude Code)

## Links vivos

- Mapa: `Cerebro/mapa_reorganizacao_20260717.md`
- Fórum buscador: `Cerebro/Foruns/forum_buscador_inteligente_unificado_20260717.md`
- Manifesto Miguel: `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
- Manifest backup: `~/legacy/BACKUP_DRIVE_20260717/MANIFEST.md`
- INDEX legacy: `~/legacy/INDEX.md`
- Buscador README: `~/ferramentas/buscador/README.md`
