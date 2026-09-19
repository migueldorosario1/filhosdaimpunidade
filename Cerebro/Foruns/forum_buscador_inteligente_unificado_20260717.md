# 🔍 Fórum — Buscador Inteligente Unificado (Miguel do Rosário)

**Data:** 2026-07-17 01:20 BRT
**Autor:** Claude Code (`claude-opus-4-7`), a pedido de Miguel
**Status:** aberto — arquitetura proposta, aguardando aprovação Miguel antes de implementar

---

## 1. Motivação

Miguel opera em múltiplos sistemas simultaneamente:

- **Local**: workspace `~/Downloads/Antigravity Google/` (137 GB, 296k arquivos)
- **Google Drive**: 30 TB (420 GB usados), inclui backup workspace, orlando diniz, pautas, jornais, livros
- **Backblaze B2**: 16 buckets, 631 GB (backups servidores, mídia, Rio Carta, dossiê Orlando, snapshots operacionais)
- **Cloudflare R2**: bucket de mídia V3 (`banco_catalogo_midia_r2_v3`) + outros
- **Servidores**:
  - Tencent Cingapura `43.156.151.165:38422` (produção Cafezinho, agentes, cron)
  - NYC failover `198.199.121.136` (réplica dormente, seo pruning, indexação)
  - GSN NYC `159.89.237.100` (WP + agentes GSN)
  - ServerDo.in `us65.serverdo.in:51439` (WP Cafezinho canônico)
  - cafezinho.news `159.65.177.60` (espelho no-index)
- **Legacy unificado**: `~/legacy/` (10 GB, novos)

Encontrar arquivo/informação hoje = ir em vários lugares manualmente. Alto custo cognitivo, alta chance de trabalhar com versão errada, alta chance de duplicar esforço.

**Meta:** um único buscador que indexa TODOS esses sistemas + integra com CLIs Claude/Codex/GLM pra qualquer agente encontrar rápido.

---

## 2. Arquitetura proposta

### 2.1 Componentes

```
/home/migueldorosario/ferramentas/buscador/
├── indexador/
│   ├── indexar_local.py                (find + stat + head/mime)
│   ├── indexar_drive.py                (rclone lsjson drive:)
│   ├── indexar_b2.py                   (rclone lsjson b2:...)
│   ├── indexar_r2.py                   (rclone lsjson r2:...)
│   ├── indexar_servidores.py           (ssh + find nos 5 servidores)
│   └── orquestrador.py                 (roda todos + salva no SQLite)
├── indice/
│   └── busca.sqlite                    (FTS5 - full-text search)
├── cli/
│   ├── busca                           (script principal — comando `busca X`)
│   ├── busca-drive                     (só Drive)
│   ├── busca-b2                        (só B2)
│   └── busca-servidor <nome>           (só servidor específico)
├── config/
│   ├── sistemas.yaml                   (definição de cada sistema indexado)
│   └── excludes.yaml                   (padrões pra pular: node_modules, .git etc)
├── mcp/
│   └── mcp_server_busca.py             (MCP server pra Claude Code integração)
├── logs/
│   └── indexacao_YYYYMMDD.log
└── README.md
```

### 2.2 Índice SQLite (FTS5)

Schema:
```sql
CREATE TABLE arquivos (
  id INTEGER PRIMARY KEY,
  sistema TEXT NOT NULL,           -- 'local', 'drive', 'b2:bucket', 'r2:bucket', 'ssh:tencent', etc
  path TEXT NOT NULL,              -- caminho relativo ao sistema
  path_completo TEXT NOT NULL,     -- fmt "sistema://path"
  nome TEXT NOT NULL,              -- basename do arquivo/dir
  tipo TEXT NOT NULL,              -- 'file' ou 'dir'
  tamanho INTEGER,                 -- bytes
  extensao TEXT,                   -- .py, .md, .jpg, etc
  modificado_em TEXT,              -- ISO datetime
  hash_md5 TEXT,                   -- opcional, pra arquivos pequenos
  conteudo_head TEXT,              -- primeiras 500 chars pra .md/.py/.txt
  indexado_em TEXT NOT NULL,       -- quando o registro foi criado/atualizado
  UNIQUE(sistema, path)
);

CREATE VIRTUAL TABLE arquivos_fts USING fts5(
  nome, path, conteudo_head, content='arquivos', content_rowid='id'
);

CREATE INDEX idx_sistema ON arquivos(sistema);
CREATE INDEX idx_extensao ON arquivos(extensao);
CREATE INDEX idx_modificado ON arquivos(modificado_em);
```

### 2.3 Interface CLI

**Comando principal:** `busca <query> [opções]`

Exemplos de uso:
```bash
# Busca por nome/conteúdo em todos os sistemas
busca "seo pruning"

# Só arquivos .py em local
busca "notificar_google" --tipo py --sistema local

# Só no Drive, últimos 7 dias
busca "orlando" --sistema drive --desde 7d

# Só em servidor específico
busca "util_indexing" --sistema ssh:tencent

# Retornar top 10 mais recentes
busca "manifesto" --top 10 --ordenar modificado_em

# Formato JSON pra pipe
busca "backup" --formato json | jq '.[].path'

# Somente arquivos maiores que 100MB
busca "" --min-tamanho 100M

# Fuzzy find via fzf integrado
busca --fzf                              # interactive fuzzy find em tudo
```

### 2.4 Integração com CLIs Claude/Codex/GLM

3 opções complementares (implementar todas):

**a) Comando shell disponível globalmente:**
- Alias `busca` em `~/.bashrc` — funciona em qualquer terminal, incluindo os que rodam Claude/Codex/GLM
- Todos os agentes podem chamar via `Bash("busca X")`

**b) MCP server dedicado:**
- `mcp_server_busca.py` expõe funções: `search_files`, `search_content`, `get_file_metadata`
- Configurar Claude Code (settings.json): adicionar buscador local MCP
- Codex e GLM (via wrapper Claude Code): herdam automaticamente

**c) Arquivo de índice consultável:**
- `indice/busca.sqlite` fica disponível pra qualquer script fazer query direta
- Doc de schema em `README.md` do buscador

### 2.5 Cadência de indexação

- **Local**: cron diário 04:00 BRT (workspace muda muito)
- **Drive**: cron semanal domingo 05:00 BRT (muda menos frequentemente)
- **B2**: cron mensal dia 1 06:00 BRT (raramente muda — só quando novo backup sobe)
- **R2**: cron semanal (mídia pode atualizar diariamente pelos agentes V3, mas volume é pequeno)
- **Servidores**: cron diário 04:30 BRT (código pode mudar)

Indexação incremental (só re-hash o que mudou desde última indexação).

### 2.6 Excludes padrão

```yaml
excludes:
  - "**/node_modules/**"
  - "**/__pycache__/**"
  - "**/venv/**"
  - "**/.git/**"
  - "**/*.pyc"
  - "**/.wwebjs_auth/**"
  - "**/.cache/**"
  - "**/.local/**"
  - "**/.nvm/**"
```

---

## 3. Escopo de sistemas a indexar

| Sistema | Como acessar | Tamanho estimado | Prioridade |
|---|---|---|---|
| Local workspace | `find` direto | 137 GB | **1 - máxima** |
| `~/legacy/` | `find` direto | 10 GB (crescente) | 1 |
| `drive:` | `rclone lsjson` | 420 GB usados | 2 |
| `b2:cafezinho-backups/` | `rclone lsjson` | 4.6 GB | 3 |
| `b2:failover-cafezinho1/` | `rclone lsjson` | 534 GB | 3 |
| `b2:Legacy-Cafezinho/` | `rclone lsjson` | 8.7 GB | 4 |
| `b2:Legacy-Miguel/` | `rclone lsjson` | 14 GB | 4 |
| `b2:Backup-GoogleDrive-Miguel/` | `rclone lsjson` | 37 GB | 4 |
| `b2:Orlando-Diniz-Dossie/` | `rclone lsjson` | 0.4 GB | 4 |
| `b2:*` demais | `rclone lsjson` | vários | 5 |
| `r2:` bucket V3 mídia | `rclone lsjson` | ? | 5 |
| Tencent `43.156.151.165:38422` | ssh + find `/root/` | ? | 2 |
| NYC failover `198.199.121.136` | ssh + find `/root/` | ? | 3 |
| GSN NYC `159.89.237.100` | ssh + find `/root/` `/var/www/` | ? | 3 |
| ServerDo.in `us65.serverdo.in:51439` | ssh + find `/var/www/ocafezinho/` | ? | 3 |
| cafezinho.news `159.65.177.60` | ssh + find `/root/` | ? | 4 |

---

## 4. Contratos entre agentes

### 4.1 Uso pelo Claude Code (esta sessão + futuras)

```python
# Via Bash tool
Bash("busca 'util_indexing' --tipo py")

# Via MCP tool (após config)
mcp__buscador__search_files(query="notificar_google", tipo="py", limit=10)
```

### 4.2 Uso pelo Codex

Mesma interface CLI. Codex já usa Bash via wrapper.

### 4.3 Uso pelo GLM (Ming)

Mesma interface CLI + acesso direto ao SQLite via `sqlite3` pra queries complexas.

### 4.4 Regras de convivência

- **Buscador é read-only** — nunca modifica arquivos indexados
- **Índice pode ser reconstruído a qualquer momento** — sem estado crítico próprio
- **Todos os agentes podem consultar simultaneamente** — SQLite suporta múltiplos readers
- **Só um indexador roda por vez** por sistema (lock via arquivo `.indexando_<sistema>`)

---

## 5. Implementação por fases

### Fase 1 — MVP (esta semana)
- [ ] Estrutura de dirs em `/home/migueldorosario/ferramentas/buscador/`
- [ ] SQLite + schema FTS5
- [ ] `indexar_local.py` rodando (só local workspace)
- [ ] CLI `busca` básico (query por nome + FTS por conteúdo em .md/.py/.txt)
- [ ] README + docs

### Fase 2 — Cloud
- [ ] `indexar_drive.py`
- [ ] `indexar_b2.py` (todos buckets)
- [ ] `indexar_r2.py`

### Fase 3 — Servidores
- [ ] `indexar_servidores.py` (SSH + find nos 5 servidores)

### Fase 4 — Integração agentes
- [ ] Alias global `busca` em `.bashrc`
- [ ] MCP server pra Claude Code
- [ ] Docs de uso pros 3 agentes (Claude, Codex, GLM)

### Fase 5 — Cadência automatizada
- [ ] Crons de indexação
- [ ] Cadência incremental (só re-index diff)
- [ ] Telemetria (quantos arquivos, tempo, erros)

### Fase 6 — Recursos avançados
- [ ] Busca semântica (embeddings via API OpenAI/Claude)
- [ ] Deduplicação inteligente (achar mesmos arquivos em sistemas diferentes)
- [ ] Interface web local opcional

---

## 6. Custo estimado

- **Storage extra**: SQLite ~500 MB pra índice completo (296k arquivos local + 200k Drive + etc)
- **Compute**: indexação local ~5 min, Drive ~30 min, servidores ~10 min cada
- **APIs (só se Fase 6)**: embeddings OpenAI ~$0.02 por 1M tokens; 296k arquivos ~$5-10 uma vez
- **Rede**: rclone lsjson é leve (metadata, não conteúdo) — ~1MB por bucket

Custo operacional: ~zero (infraestrutura já existe).

---

## 7. Perguntas em aberto (Miguel decide)

### 7.1 Onde instalar o buscador?

- **Opção A** — `/home/migueldorosario/ferramentas/buscador/` (fora do workspace, atende múltiplos projetos)
- **Opção B** — `<workspace>/06_Ferramentas/buscador/` (dentro do workspace, versionável)
- **Recomendado A**: buscador não deve ser tocado pelo workspace, é infraestrutura pessoal.

### 7.2 Índice: local ou compartilhado (Drive)?

- **Opção A** — SQLite local em `~/ferramentas/buscador/indice/busca.sqlite`. Rápido, offline.
- **Opção B** — SQLite espelhado no Drive. Backup automático.
- **Recomendado A + backup Drive semanal** (semelhante ao Cerebro).

### 7.3 Servidores: indexar via SSH ou não?

- **A favor**: encontrar código do NYC via `busca 'notificar_e_logar'` sem SSH manual
- **Contra**: mais complexo, requer manter chaves SSH válidas, potencial lentidão
- **Recomendado**: sim, mas cron diário só 04:30 BRT (fora de horário de pico)

### 7.4 Embeddings pra busca semântica?

- **A favor**: "quero achar coisa sobre X" retorna resultados relevantes mesmo sem match exato
- **Contra**: custo (US$5-10 uma vez + centavos por refresh) + complexidade
- **Recomendado**: Fase 6, opcional, só se depois de MVP mostrar valor

### 7.5 Interface web?

- **A favor**: mais confortável que CLI, permite thumbnails/preview
- **Contra**: overhead de manter servidor local
- **Recomendado**: Fase 6, só se demanda real aparecer

### 7.6 Nome do comando

Sugestão: `busca` (curto, PT-BR, intuitivo). Alternativas: `find2` (chato), `grepall` (limitado), `whereis-miguel` (bobo).

---

## 8. Comparação com alternativas prontas

| Ferramenta | Prós | Contras |
|---|---|---|
| `find`/`grep` | Nativo, poderoso | Só local, sintaxe difícil, sem índice |
| `fzf` | Fuzzy interativo | Só local, sem conteúdo |
| `ripgrep` (`rg`) | Rápido, conteúdo | Só local |
| `recoll` | GUI, plugins | Overkill, GUI-first |
| `Everything` (Win) | Rápido, moderno | Só Windows |
| `mdfind` (Mac) | Nativo, rápido | Só macOS |
| **Buscador Miguel (proposto)** | Multi-sistema, custom | Precisa implementar |

Nenhuma alternativa pronta cobre Drive+B2+R2+servidores. Vale implementar.

---

## 9. Referências cruzadas

- Mapa reorganização: `Cerebro/mapa_reorganizacao_20260717.md`
- Manifesto Miguel: `Projeto Cafezinho Agentes/Ponto de Retomada/manifesto_ativos_sites_e_agentes_v4_20260717.md`
- CLAUDE.md: `Projeto Cafezinho Agentes/CLAUDE.md`
- Backup Drive: `~/legacy/BACKUP_DRIVE_20260717/MANIFEST.md`
- Backup B2 Codex: `Projeto Cafezinho Agentes/Foruns/forum_backup_v4_tematicos_backblaze_20260717_004222.md`

---

## 10. Log de conversa

**2026-07-17 01:20 BRT — Claude Code:** fórum criado a pedido de Miguel após conclusão de FASE A do sprint de reorganização. Buscador é ferramenta paralela à reorganização estrutural, com valor imediato (encontrar arquivos entre múltiplos sistemas) e valor de longo prazo (retomada intuitiva por qualquer agente).

**Próximas ações (Claude autoriza-se via diretriz "autonomia com manifest"):**
1. Aguardar backup workspace Drive terminar
2. Consultar Miguel sobre §7.1 até §7.6 se ele quiser refinar
3. Implementar Fase 1 (MVP local)
4. Documentar uso no CLAUDE.md
5. Reportar

**Aberto pra Codex + GLM + Miguel comentarem/refinarem.**

---

*Documento vivo. Editar em patch/Edit — nunca full rewrite.*
