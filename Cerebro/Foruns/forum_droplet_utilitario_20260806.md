# 🏭 Fórum — Droplet utilitário (Central + agentes migrados + YouTube renascido)

> **Criado:** 2026-08-06 ~18:30 BRT por ZCode (Kimi K3), ordem do Miguel ("faz as três coisas + novo agente YouTube Aiatolah juntos").
> **Droplet:** `142.93.48.252` — renomeado conceitualmente de `gsn-youtube-nyc-01` para **Droplet Utilitário / Central de Operações**.
> **Memória técnica:** `Memorias/memoria_droplet_utilitario_20260806.md`.

## O que aconteceu

O droplet ocioso (US$6/mês parados) foi promovido a **3 papéis** numa só sessão:

| Papel | Status | Detalhe |
|---|---|---|
| **Central de Alertas** | ✅ no ar (sessão anterior) | Uptime Kuma + vigia de discos → Telegram |
| **Casa de agentes leves** | ✅ migrados | Ferroviário (Mundo Trilhos/Rail Post) + Turismo (Discover Brazil) — saíram do Rio-Carta-Agentes lotado |
| **Hub de YouTube** | ✅ renascido | YouTube GSN (revivido) + YouTube Aiatolah (novo na central) |

## Migração ferroviário + turismo (rio-ag → central)

- **Código + dados + chaves** copiados via stream SSH (não via rede pública).
- **Clones git novos** (limpos): `mundo-trilhos`, `rail-post`, `discover-brazil` — chave GitHub do Cícero instalada (`id_ed25519_cicero_github`, 600).
- **Crons NOVOS na central** (backup automático do estado anterior):
  - Ferroviário: `15 */2 * * *` + retry `15 4 * * *` (mesma cadência do rio-ag).
  - Turismo: `42 9,13,17,21 * * *` (mesma cadência).
- **Crons VELHOS desligados no rio-ag** (backup em `/root/crontab_backup_pre_migracao_central_20260806.txt`).
- **Depêndencias:** swap 2G criado; instalados `feedparser beautifulsoup4 pillow youtube-transcript-api trafilatura python-dotenv`.
- **Bugs corrigidos durante a migração:**
  1. **Turismo `search_brave` sem fallback** → patchado com `search_perplexity` (mesmo padrão do ferroviário). Prova: busca retornou 5 fontes (antes: 0 — estava falhando silenciosamente há dias no rio-ag).
  2. **Chaves LLM mortas nos envs de servidor** (DeepSeek e Qwen davam 401) → substituídas pelas vivas do cofre canônico. Backups `.bak_pre_ds_viva_20260806` / `.bak_qwen_20260806`.

## YouTube GSN — revivido

- Código intacto desde 05/06 (último publish: Jeffrey Sachs). Crons reativados:
  - Coletor: `0 6,14,22 * * *` (3×/dia).
  - Publicador: `35 6,14,22 * * *` (após coletor).
- **Qwen consertada** (401→OK) — era o motivo do sumiço.
- Publicador usa roteador LLM (ED zhipu/glm → RE deepseek → RV qwen) + yt-dlp + Transkriptor.

## YouTube Aiatolah — novo na central (e bug crítico corrigido)

- **Repo vivo confirmado:** `migueldorosario1/aiatolah.git` (commit `e8958d6` no ar em aiatolah.com; o `aiatolah-v4` é Espelho/Cópia, não publicador). Clonado em `/root/aiatolah`.
- **🐛 BUG GRAVE corrigido: 5 de 6 channel IDs estavam ERRADOS** no `CANAIS_AI`. Validação via `feeds/videos.xml`: todos retornavam **0 vídeos**. IDs reais extraídos das páginas `@handle`:

| Canal | ID antigo (errado) | ID corrigido |
|---|---|---|
| Lex Fridman | UC_QhL74e… | `UCJIfeSCssxSC_Dhc5s7woww` |
| Dwarkesh Patel | UCxS9K_iT… | `UCZa18YV7qayTh-MRIrBhDpA` |
| Andrej Karpathy | UC7G0B3yO… | `UCe4jUOmQPKMDvOkzJpDfMRQ` |
| DeepLearning.AI | UCcIXc5m… | `UCcIXc5mJsHVYTZR1maL5l9w` (único certo) |
| Google DeepMind | UCxCO1M9… | `UCP7jMXSY2xbc3KCAE0MHQ-A` |
| OpenAI | UC78o7sX… | `UCXZCJLdBC09xxGZ6gcdrc6A` |

  **Prova pós-fix:** todos os 6 retornam **15 vídeos** cada (antes, 5 de 6 = zero). O agente do Aiatolah não tinha com o que trabalhar há semanas.
- `.env.local` criado com chaves vivas (DeepSeek, Qwen, Perplexity, FAL) — 600.
- Cron: `0 */6 * * *` (4×/dia, como era no Miguel local antes da reforma V4).

## Pendências

- Validação do 1º artigo publicado por cada agente a partir da central (cronNoturno/amanhã).
- Repositório `aiatolah-v4` — confirmar se é lixo (não publicador) e arquivar.
- **LEMBRETE Miguel:** reconstruir failover NYC↔Tencent (separado; não tocado aqui).
