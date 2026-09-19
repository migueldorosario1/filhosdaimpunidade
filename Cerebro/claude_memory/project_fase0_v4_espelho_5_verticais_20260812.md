---
name: project-fase0-v4-espelho-5-verticais-20260812
description: FASE 0 ativa desde 12/08/2026 — 5 verticais V4 novas (cultura/economia/meio-ambiente/esporte/saúde) publicam DRAFT no espelho cafezinho.news; Claude revisa como se fosse canônico; canônico ocafezinho.com INTACTO
metadata: 
  node_type: memory
  type: project
  originSessionId: d917262a-1c40-4990-942c-4a2a8b497e3d
---

**FASE 0 — 5 verticais V4 publicando draft no espelho `cafezinho.news`, Claude Code revisa antes do publish.**

Ativada por Miguel + ZCode (GLM-5.2) em 12/08/2026 ~16:50 BRT com cron ligado no NYC. Cartinha oficial: `Cerebro/Foruns/cartinhas/cartinha_claude_code_fase0_v4_espelho_20260812.md`. Checkpoint: `Cerebro/Foruns/forum_checkpoint_espelho_5_verticais_20260812.md`. Meu ACK: `Cerebro/Foruns/cartinhas/cartinha_claude_ack_fase0_v4_espelho_20260812.md`.

**Why:** as 5 novas verticais são teste — a decisão de levar pro canônico é depois. Miguel quer curadoria editorial humana (via Claude Code) antes de expor ao público oficial. Canônico está protegido: as 3 verticais ativas (nacional=22, geopolitica=5003, ciencia=19936) seguem no `ocafezinho.com` sem alteração.

**How to apply:**

- **5 categorias FASE 0** (mesmos IDs no espelho e no canônico): Cultura=79, Economia=43, Meio Ambiente=582, Esporte=1271, Saúde=258.
- **Cron NYC** (draft-only, target = espelho):
  - `35 */4` → Economia (4h)
  - `5 */4` → Cultura (4h)
  - `15 1,9,17` → Meio Ambiente (8h)
  - `15 2,10,18` → Esporte (8h)
  - `15 3,11,19` → Saúde (8h)
  - Todas com `flock` por vertical + lock global `/tmp/v4_redacao_global.lock` + `VERTICAIS_ESPELHO=1` na env.
- **Endpoint espelho:** `https://cafezinho.news/wp-json/wp/v2/`. Creds: `ESPELHO_WP_SITE/USER/PASS` em `Outros/chaves/agentes_labs/.env.unificado` (user = `Redator`, ID 5470). Basic Auth do front está **DESATIVADA** durante fase — não tentar autenticar por Basic.
- **Log Claude separado:** bugs em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_espelho_YYYY-MM-DD.jsonl` (arquivo diferente do canônico), mesmo schema Vigília V5 + campo `target: "espelho"`.
- **Régua editorial:** [[feedback-modo-enxuto-preservar-worker-v4]] + [[feedback-titulo-forte-simples-ludico-politico]] + [[feedback-titulo-tese-corpo-argumenta]] + [[feedback-espelho-fontes-invisiveis-regra-editorial]].
- **Featured image:** worker já comprime <500KB; conferir no publish. **Cultura sem imagem IA** (se `attribution = fal_ai/flux-pro` em cat 79, escalar em vez de publicar).
- **NÃO promovo pro canônico sozinho.** Migração está planejada em `Cerebro/Foruns/forum_plano_migracao_canonico_20260812.md` (5 etapas, ~40min, rollback) — aguarda "vai" do Miguel.
- **Meu papel = revisor editorial, não infra.** Não ligar/desligar cron, não mexer em tema/mu-plugin do espelho, não religar Basic Auth. Se detectar cron parado (elegíveis=0 por >24h em alguma vertical), ping ZCode via `inbox_trindade/zcode.md`.
- **Meu Vigília V5 canônico segue normal** — as 3 verticais ativas (autor 5786 no `ocafezinho.com`) continuam com pipeline tripla DS+GPT+Claude+WebSearch inalterado.

**Status quando essa memória foi escrita (12/08 17:10 BRT):** cron ligado ~16:50, primeiro draft ainda não caiu. Aguardando.

**Sinal de fim da FASE 0:** Miguel autoriza `forum_plano_migracao_canonico_20260812.md` → cron passa a apontar canônico → Basic Auth do espelho é religada → esse memory vira obsoleto. Quando isso acontecer, apagar/atualizar.
