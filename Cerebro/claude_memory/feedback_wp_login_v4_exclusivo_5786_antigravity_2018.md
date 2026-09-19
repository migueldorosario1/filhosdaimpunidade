---
name: feedback-wp-login-v4-exclusivo-5786-antigravity-2018
description: "Separação de identidade WP consolidada 27/07/2026 19:58 BRT — 5786 (redacao-nova) EXCLUSIVO agentes V4, 2018 (james2017/Miguel do Rosário) EXCLUSIVO Antigravity Desktop humano; heurística antiga 'zizi_job_id vazio = humano' descontinuada"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Identidades WP na fase pós-27/07/2026 ~20h BRT:

| WP User ID | Slug | Nome | Papel |
|---|---|---|---|
| **5786** | `redacao-nova` | `redacao-nova` | **EXCLUSIVO agentes V4 automatizados** (worker Geo/Nacional/Ciência do Kimi) |
| **2018** | `james2017` | `Miguel do Rosário` | **EXCLUSIVO Antigravity Desktop** (posts manuais Miguel) |
| **5470** | (legado) | (legado) | Pipeline V4 legado antigo — em migração |
| **5749** | `rian` | `Rian` | Rian humano — fora do escopo V4 |
| **5735** | (legado) | (legado) | Legado |

**Why:** Miguel criou conta WP dedicada `James2017` (WP ID 2018) em 27/07/2026 ~19:58 BRT após teste de homologação (draft 263125 "teste" saiu com autor 2018 confirmado). Motivo: separar publicações manuais dele via Antigravity Desktop da identidade dos agentes V4. Item #2 do lembrete das 14h RESOLVIDO. Miguel textual: *"agora o v4 tem login exclusivo"*.

**Descontinua heurística antiga:** regra `feedback_diferenciar_llm_desktop_cli_mobile` mencionava distinguir humano×agente via `zizi_job_id`/`_agente_origem` preenchidos vs vazios com autor 5786. Isso era WORKAROUND. Agora é distinção nativa via user ID.

**How to apply:**
- **Loop Vigília Opus** (cron Claude): filtro drafts elegíveis fica `author=5786` puro (nenhuma exceção pra "5786+vazio=humano"). Todo 5786 = agente V4 = checagem dupla obrigatória.
- **Loop Vigília Haiku**: mesma coisa — todo autor 5786 vai pro pipeline de observação.
- **Antigravity Miguel** publica com autor 2018 → NÃO entra na fila de checagem dupla (é humano, edição manual dele).
- **Se aparecer post autor 5786 sem `zizi_job_id`/`_agente_origem`**: agora é BUG DE VERDADE (agente sem populate metadata) — reportar Kimi ao invés de assumir humano.
- **Consequência pra produtor V4:** deve popular `_agente_origem`/`_agente_versao`/`zizi_job_id` SEMPRE. Já sugerido na cartinha Kimi 16:55 (pergunta #5). Fica agora obrigatório.

**Casos borderline:**
- Draft 263125 "teste" autor 2018 — teste de homologação Miguel. Ignorar (não é editorial real).
- Posts antigos hoje autor 5786 sem meta (263032, 263036) — foram Miguel via ferramenta antiga (não Antigravity com nova conta). Ficam como estão (regra `feedback_kimi_stop_retroativo`).

**Regras irmãs:**
- [[feedback-diferenciar-llm-desktop-cli-mobile]] — parte sobre WP 5786 vazio=humano fica OBSOLETA
- [[feedback-checagem-dupla-editorial-com-autonomia]] — continua valendo, agora sem exceção 5786
- [[feedback-kimi-stop-retroativo]] — posts autor 5786 já existentes ficam intactos
