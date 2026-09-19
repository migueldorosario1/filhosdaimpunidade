---
name: reference-banco-midia-canonico-legado
description: "Banco mídia legado canônico Tencent é /root/agent_data/banco_midia/banco_imagens_reais.db (411MB, 345k imagens). Confusão histórica de paths resolvida 26/06/2026."
metadata: 
  node_type: memory
  type: reference
  originSessionId: ab544d32-d470-42b2-8246-7c83f1137bc1
---

## Banco mídia legado — referência canônica (pós-limpeza 26/06/2026)

### Path canônico ÚNICO

```
/root/agent_data/banco_midia/banco_imagens_reais.db
```

- 411MB · 345.382 imagens
- 100% com URL alta
- 70 entidades no gazetteer
- 125.764 imagens com vínculo de entidade (36%)
- 94,6% Wikimedia Commons + 5,4% Flickr oficiais BR (senado/planalto/lula/casa_branca/onu/stf/mre)
- Tabelas: `imagens` (não `imagens_reais`!) · `entidades` · `imagem_entidade` · `indexador_state`
- Robô que popula: `/root/robo_coleta_imagens.py` (cron 2h) + `/root/robo_coleta_flickr_rapido.py` (cron 13,43)
- Cresce ~6k imagens/dia

### Quem consome (validado 26/06 antes de mover órfãos)

- `/root/cafezinho/Sistema/midia/agente_midia.py` (`LEGACY_BANCO_MIDIA_DB`)
- `/root/scripts/auditar_banco_midia.py` (`DB_PADRAO`)
- `/root/banco_midia_busca.py` (`DEFAULT_DB`)
- `/root/util_joia_r2_v3.py` (`DB_MIDIA_LEGADO`)
- `/root/gerenciador_imagens.py` (`BANCO_MIDIA_DB`, env-overridable)
- `/root/.env.unificado` (`BANCO_MIDIA_DB`)

### Variável de ambiente

```
BANCO_MIDIA_DB=/root/agent_data/banco_midia/banco_imagens_reais.db
```

### NÃO confundir com (escopo separado, NÃO tocar pensando que é o mesmo)

- `/root/agent_data/banco_midia/banco_imagens_curadas_v3.db` (5MB) — curadoria V3
- `/root/V3/banco_midias_*` — workspace V3 política (publicadas/auditadas/candidatas)
- `/root/V3/banco_catalogo_midia_r2_v3.db` (2.6MB) — catálogo R2 V3
- `/root/agent_data/banco_imagens_curadas.db` se existir — outro escopo

### Paths órfãos arquivados em 26/06/2026

Estavam em produção causando confusão (4 paths com mesmo nome `banco_imagens_reais.db` em diretórios diferentes). Movidos pra `/root/legacy/banco_midia_20260626/` com README + backup tar.gz em `/root/backups/limpeza_bancos_midia_orfos_20260626_004335.tar.gz`:

- `agent_data_root_banco_imagens_reais.db` (4KB, era `/root/agent_data/`)
- `cafezinho_dados_agentes_banco_imagens_reais.db` (17MB, era `/root/cafezinho/dados_agentes/banco_midia/`)
- `gsn_Legacy_banco_imagens_reais.db` (215MB, era `/root/cafezinho/sites_tematicos/gsn/...`)
- `V3_tmp_banco_imagens_reais.db` (215MB, era `/root/V3/tmp/`)
- `V3_tmp_banco_imagens_trilhos.db` (444KB, era `/root/V3/tmp/`)

Plus 4 deletados (3 vazios 0 bytes + 1 symlink quebrado):
- `/root/banco_midia_cafezinho.db`
- `/root/banco_imagens_reais.db`
- `/root/agent_data/banco_midia/banco_midia_cafezinho.db`
- `/root/cafezinho/portal_cafezinho/Dados/bancos/banco_imagens_reais.db` (symlink)

### Query útil de busca por entidade

```python
import sqlite3
conn = sqlite3.connect("/root/agent_data/banco_midia/banco_imagens_reais.db")
res = conn.execute("""
    SELECT i.id, i.origem, i.url_alta, i.descricao
    FROM imagens i
    JOIN imagem_entidade ie ON ie.imagem_id = i.id
    JOIN entidades e ON e.id = ie.entidade_id
    WHERE e.nome LIKE ?
    LIMIT 10
""", ("%Lula%",)).fetchall()
```

Top entidades cobertas: Irã 39k (over-collected), Brasil 22k, Trump 8k, Lula 8k, Ucrânia 7k, Modi 4k, China 3.6k, Rússia 3.5k, EUA 3.3k.
