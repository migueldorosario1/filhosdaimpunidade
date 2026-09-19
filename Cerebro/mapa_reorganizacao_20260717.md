# 🗺️ Mapa de Reorganização do Workspace — 2026-07-17

**Autor:** Claude Code (`claude-opus-4-7`)
**Diretriz Miguel:** poucos diretórios na base, tudo organizado em subdiretórios, encontrar arquivos e diretórios de maneira intuitiva.

**Precondição pra executar:** backup workspace pro Drive concluído (em curso, `drive:backup 20260717/`).

## Estado atual (2026-07-17 01:15 BRT)

- **28 diretórios top-level** (excessivo)
- **~137 GB total** no workspace
- **Distribuição:** 96G Outros/ + 11G Rio Carta Agentes/ + 4.4G Projeto Cafezinho Agentes/ + resto disperso

## Estrutura alvo simplificada (10 diretórios base)

```
/home/migueldorosario/Downloads/Antigravity Google/
├── README.md
├── CLAUDE.md                                    ← promover pra raiz
│
├── 01_Cerebro/                                  ← todo cérebro operacional
│   ├── nodes/                                   ← CEREBRO_NODE_*.md
│   ├── indices/                                 ← CEREBRO_INDEX_*.md
│   ├── cartoes_de_bolso/                        ← CARTAO_BOLSO_*.md
│   ├── memoria/                                 ← Memorias/ + memorias_provisorias/ + memory/
│   ├── subcerebro_antigravity_desktop/          ← já criado
│   ├── foruns/                                  ← Foruns/ atual
│   ├── cerebro_light/
│   ├── indice_cerebro.json
│   ├── mapa_reorganizacao_20260717.md           ← ESTE ARQUIVO
│   └── manifesto_ativos_sites_e_agentes_v4_20260717.md ← Miguel manifesto
│
├── 02_Cafezinho_Canonico/                       ← renomear de "Projeto Cafezinho Agentes/"
│   ├── V4/                                      ← root/v4 + root/v4_labs
│   ├── root/                                    ← agentes NYC/Tencent
│   ├── Foruns/                                  ← foruns Cafezinho
│   ├── Ponto_de_Retomada/
│   ├── backups_operacionais/
│   ├── sites-tematicos/                         ← permanece aqui (canônico Miguel)
│   └── CLAUDE.md                                ← symlink pra raiz
│
├── 03_Cafezinho_Espelho_NoIndex/                ← já criado skeleton
│
├── 04_Sites_Tematicos_Silos/                    ← silos autônomos independentes
│   ├── rio_carta/                               ← movido de "Rio Carta Agentes/"
│   ├── gsn/                                     ← movido de "Global South News/"
│   ├── cicero/                                  ← movido de "Cicero Agentes/"
│   ├── aiatolah/                                ← movido de "aiatolah/"
│   └── README.md                                ← explica: silos são independentes dos sites-tematicos/ dentro de 02_Cafezinho_Canonico/
│
├── 05_Agentes_Tematicos/                        ← renomeado de "agentes_tematicos/"
│
├── 06_Ferramentas/                              ← utilitários locais
│   ├── buscador/                                ← NOVO - buscador unificado
│   ├── AGY_gdrive_gmail/                        ← movido de "AGY/"
│   ├── github_work/                             ← repo cafezinho-publicador
│   └── scripts_uteis/                           ← scripts one-off (após triagem)
│
├── 07_Dados_e_Bancos/                           ← bancos SQLite grandes
│   ├── banco_midia/                             ← movido
│   └── agent_data/                              ← movido (threads_twitter etc)
│
├── 08_Outros/                                   ← pessoais mistos (permanentes)
│   ├── orlando diniz/                           ← Lawfare (63G — INTOCADO)
│   ├── (pastas jornais, livros, pautas, etc)
│   └── (mesmo Outros/ atual, só limpo de dirs antigos)
│
└── 99_Backups_Locais/                           ← Backups/ + backups_ceo_cerebro/ + banco_midia/backups_frios/
```

**Bônus fora do workspace:**
```
/home/migueldorosario/legacy/                    ← UNIFICADO já criado
/home/migueldorosario/ferramentas/               ← ambiente do buscador (futuro)
```

## Tabela de-para (item por item)

### Diretórios que RENOMEIAM (mudança de nome no mesmo lugar)

| De | Para | Nota |
|---|---|---|
| `Projeto Cafezinho Agentes/` | `02_Cafezinho_Canonico/` | ALTO RISCO — 803 refs em código. Estratégia sed+backup+smoke. |
| `agentes_tematicos/` | `05_Agentes_Tematicos/` | Menor risco — só numeração. |

### Diretórios que MOVEM (mudam de lugar)

| De | Para | Tamanho | Nota |
|---|---|---|---|
| `Rio Carta Agentes/rio_carta/` | `04_Sites_Tematicos_Silos/rio_carta/` | 3.7G | Silo canônico Rio Carta |
| `Rio Carta Agentes/server doin/` | `~/legacy/riocarta_server_doin_20260717/` | 5.3G | Backup droplet antigo — legacy |
| `Rio Carta Agentes/build_backups/` | `~/legacy/riocarta_build_backups_20260717/` | 1.8G | Backups build — legacy |
| `Rio Carta Agentes/root/` | `04_Sites_Tematicos_Silos/rio_carta/root/` | 227M | Root do silo Rio Carta |
| `Global South News/gsn/` | `04_Sites_Tematicos_Silos/gsn/` | 1.9G | Silo canônico GSN |
| `Global South News/root/` | `04_Sites_Tematicos_Silos/gsn/root/` | 222M | Root GSN |
| `Cicero Agentes/cicero/` | `04_Sites_Tematicos_Silos/cicero/` | 735M | Silo canônico Cicero/ceara |
| `Cicero Agentes/root/` | `04_Sites_Tematicos_Silos/cicero/root/` | 226M | Root Cicero |
| `aiatolah/` | `04_Sites_Tematicos_Silos/aiatolah/` | 253M | Silo AIatolah |
| `AGY/` | `06_Ferramentas/AGY_gdrive_gmail/` | 172K | Scripts gdrive/gmail |
| `github_work/` | `06_Ferramentas/github_work/` | 1.4M | Repo cafezinho-publicador |
| `banco_midia/` | `07_Dados_e_Bancos/banco_midia/` | 50M | Bancos SQLite |
| `agent_data/` | `07_Dados_e_Bancos/agent_data/` | 16K | Dados threads_twitter |
| `Backups/` | `99_Backups_Locais/Backups/` | 1.1G | Backups locais (inclui snapshot Codex hoje) |
| `backups_ceo_cerebro/` | `99_Backups_Locais/backups_ceo_cerebro/` | 71M | Backups cérebro CEO |
| `Cerebro/` (interno) | `01_Cerebro/` | 7.6M | Renomeia + reorganiza interno |

### Diretórios que vão pro LEGACY

| De | Para | Tamanho | Motivo |
|---|---|---|---|
| `scratch/` | `~/legacy/scratch_20260717/` | 2.2G | 421 scripts one-off — Miguel decide caso queira preservar algum |
| `brain/` | `~/legacy/brain_uuid_session_20260717/` | 28K | UUID de sessão |
| `memory/` | `~/legacy/memory_orfan_20260717/` | 8K | CSV velho |
| `passo2e_taxonomia_seo/` | `~/legacy/passo2e_taxonomia_seo_v3_20260717/` | 44K | Script V3 antigo |
| `comunicacao_externa/` | `~/legacy/comunicacao_externa_20260717/` | 40K | 1 docx antigo |
| `contratos/` | DELETAR ou `~/legacy/contratos_vazio_20260717/` | 4K (vazio) | Vazio |
| `tmp/` | `~/legacy/tmp_20260717/` | 8.3M | Temporário |
| `tmp_v3_remote/` | `~/legacy/tmp_v3_remote_20260717/` | 1.1M | Temp V3 antigo |
| `tmp_v3_docs/` | `~/legacy/tmp_v3_docs_20260717/` | 16K | Temp V3 antigo |
| `__pycache__/` | DELETAR (regenerável) | 560K | Cache Python |
| `artifacts/` | Analisar caso a caso | 47M | Tem sprint_report + v4 tar.gz — talvez manter algo |

### Diretórios que FICAM (não movem, apenas organizam interior)

| Dir | Ação interna |
|---|---|
| `Cerebro/` → `01_Cerebro/` | Deduplicar CEREBRO_INDEX_*.md sobrepostos com CEREBRO_NODE_*.md. Consolidar. |
| `Outros/` → `08_Outros/` | Manter estrutura interna (é área pessoal), mas revisar se tem duplicatas |
| `v4_memoria/` | **NÃO MEXER** — V4 ativo |
| `v4_telemetry/` | **NÃO MEXER** — V4 ativo |

### Arquivos soltos na raiz que RESTAM (13 arquivos legítimos)

- `README.md` — mantém
- `CLAUDE.md` (criar link/copy do canônico) — nova centralização
- `.env`, `.gitignore`, `.qwenrc`, `.aider.*` — configs mantêm
- `claude-max.sh`, `claude-glm.sh`, `acorde.sh` — scripts diários mantêm
- `files_claude_autocura_imagens_v4_20260714.zip` — V4 recente MANTÉM
- `forum_autocura_imagens_v4_20260714.md` — V4 MANTÉM
- `imagens_autocura_v4_20260714.zip` — V4 MANTÉM
- `Para_mostrar_ao_Claude_zipdoGPT.zip` — V4 recente MANTÉM
- `agentes_tematicos.zip` — dir canônico + zip preserva versão

## Ordem de execução (após backup Drive terminar)

**PASSO 1 (baixo risco)** — Mover legacys claros:
- scratch, brain, memory, passo2e_taxonomia_seo, comunicacao_externa, contratos, tmp*, artifacts (triagem), __pycache__ (delete)

**PASSO 2 (médio risco)** — Consolidar dirs pequenos:
- AGY, github_work, agent_data, banco_midia → 06_Ferramentas + 07_Dados_e_Bancos
- Backups, backups_ceo_cerebro → 99_Backups_Locais

**PASSO 3 (médio risco)** — Reorganizar interno do Cerebro:
- Cerebro/ → 01_Cerebro/ com nodes/, indices/, cartoes_de_bolso/, memoria/ como subdirs

**PASSO 4 (alto risco)** — Criar 04_Sites_Tematicos_Silos/ e mover silos:
- Rio Carta Agentes → 04/rio_carta + legacy dos backups
- Global South News → 04/gsn
- Cicero Agentes → 04/cicero
- aiatolah → 04/aiatolah
- Grep de refs antes, sed em batch, smoke test após

**PASSO 5 (máximo risco)** — Rename Projeto Cafezinho Agentes → 02_Cafezinho_Canonico:
- 803 refs em código. Backup B2 completo antes (Codex já fez). Sed em batch. Smoke.
- Alternativa: symlink `02_Cafezinho_Canonico -> Projeto Cafezinho Agentes` (compat sem sed massivo)

**PASSO 6** — Renomear Outros → 08_Outros, agentes_tematicos → 05_Agentes_Tematicos

**PASSO 7** — Promover CLAUDE.md pra raiz (link ou cópia sincronizada)

**PASSO 8** — Atualizar CLAUDE.md com nova árvore + INDEX no cérebro

## Reversibilidade

Toda operação:
- É `mv` (não `rm` — nunca apaga)
- Passa pelo script `mover_pra_legacy.py` que gera MANIFEST.md + inventario.json
- Grava linha no `~/legacy/INDEX.md`
- Grava log em `~/legacy/_logs/`
- Backup completo Drive existe em `drive:backup 20260717/` como rede segura extra
- Backup B2 V4+Tematicos do Codex em `b2:failover-cafezinho1/backups/v4_tematicos/20260717_004222/`

## Buscador unificado (fase paralela)

Ver: `Cerebro/Foruns/forum_buscador_inteligente_unificado_20260717.md` (a criar).

Após reorganização, buscador vai indexar a nova estrutura + Drive + B2 + servidores + R2 pra retomada intuitiva de qualquer arquivo em qualquer sistema.

---

*Mapa vivo. Atualizar conforme fases avançam.*
