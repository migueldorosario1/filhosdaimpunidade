---
name: acesso-sqlite-v4-nyc
description: Caminhos canônicos + método de acesso aos 8 SQLite V4 no host Nova York (nyc SSH alias) via python3 sqlite3 modo read-only
metadata: 
  node_type: memory
  type: reference
  originSessionId: 1a437e9e-f4cf-4489-8f4a-4625ae5d63ff
---

# Acesso SQLite V4 no NYC

**Host:** `nyc` (alias SSH em `~/.ssh/config`, IP `198.199.121.136`, user root, key `~/.ssh/id_ed25519`).

**Bancos canônicos V4 em `/root/agent_data/v4_verticals/`:**

| Vertical | Caminho | Tamanho típico |
|---|---|---:|
| Nacional | `nacional.sqlite3` | ~5 MB |
| Geopolítica | `geopolitica.sqlite3` | ~7 MB |
| Ciência | `ciencia_tecnologia_ia.sqlite3` | ~6 MB |
| Regional Centro-Oeste | `regional_centro_oeste.sqlite3` | ~13 MB |
| Regional Nordeste | `regional_nordeste.sqlite3` | ~28 MB |
| Regional Norte | `regional_norte.sqlite3` | ~21 MB |
| Regional Sudeste | `regional_sudeste.sqlite3` | ~12 MB |
| Regional Sul | `regional_sul.sqlite3` | ~10 MB |

**Arquivo morto:** `ciencia.sqlite3` (0 bytes, legacy) — usar `ciencia_tecnologia_ia.sqlite3`.

**Método de acesso (sem sqlite3 CLI no host):**

```bash
ssh nyc 'python3 << "PYEOF"
import sqlite3
con = sqlite3.connect("file:/root/agent_data/v4_verticals/nacional.sqlite3?mode=ro", uri=True)
con.row_factory = sqlite3.Row
for r in con.execute("SELECT status, COUNT(*) n FROM candidates GROUP BY status"):
    print(dict(r))
PYEOF
'
```

`?mode=ro` garante read-only — impossível escrever mesmo em bug.

**Schema candidates (todas verticais):** `item_key, title, url, source_type, source_name, published_at, collected_at, first_seen_at, last_seen_at, score, text_content, text_sha256, status, raw_json`.

**Schema candidates Regional (extra):** também tem `uf, poll_flag, provenance`.

**Schema draft_events:** `event_id (PK), item_key, started_at, finished_at, outcome, wp_post_id, wp_status, detail`. Note: **Regional Sul e Centro-Oeste NÃO têm tabela `draft_events`** (drift de schema, bug aberto).

**Schema rejections:** `id (PK), item_key, [uf em Regional], title, url, reason, observed_at, raw_json, first_seen_at, last_seen_at, seen_count`.

**Schema runs (Nacional/Geo/Ciência):** `run_id, started_at, finished_at, source_path, seen, accepted, rejected, new_rows`. Regional SE/CO/NE/S/N usam schema diferente com `fontes_ok, fontes_erro` adicionais.

**Status típicos de candidates:** `new, drafted, editorial_blocked, stale_expired, image_pending, duplicate, duplicate_blocked, discarded`.

**Outcomes típicos de draft_events:** `draft_confirmed, repair_preflight_failed, failed, factual_gate_skipped, factual_gate_corrected, editorial_blocked, duplicate_blocked, duplicate_aborted, image_pending`.

**Queries úteis:** ver `Cerebro/Foruns/resposta_glm_rodada2_forum_incidente_v4_20260809.md` §1 e §7.1 (`v4_queue_metrics.py` pronto pra deploy read-only).

**Limitações confirmadas em 09/08/2026:**
- `text_sha256` só deduplica texto idêntico — RSS re-publica com edits leves e produz hash diferente. Não captura duplicidade semântica.
- SQLite sem `percentile()` nativo — calcular em Python ordenando.
- Regional CO/NE/S sem `draft_events` = diagnóstico cego de vazão nessas regiões.

Conforme [[forum-v4-incidente-rodada2-estado]] para o caso de uso específico.
