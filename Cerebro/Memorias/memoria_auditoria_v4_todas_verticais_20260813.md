# Memória — Auditoria integral dos V4 do Cafezinho (Fases 0+1): log técnico completo

**Data:** 13/08/2026 · **Agente:** ZCode (Kimi K3) · **Sprint handoff:** `Foruns/forum_handoff_zcode_auditoria_todos_v4_padrao_ouro_20260813.md`
**Fórum irmão (estado/decisões):** `Foruns/forum_auditoria_v4_todas_verticais_fase01_20260813.md`
**Evidências locais:** `ZCodeProject/auditoria_v4_20260813/fase0/` (nyc_fase0_*.txt + codigo_vivo/ com sha256 conferidos)

---

## 1. Topologia confirmada (Fase 0)

- **Servidor de agentes:** NYC `Cafezinho-failover-vigia` (198.199.121.136), uptime 38d. Código V4 em `/root/`; bancos em `/root/agent_data/v4_verticals/`; runtime redator em `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py` (⚠️ Codex citou `codigo.v4_vertical_redactor_runtime` sem o prefixo v4_labs — é o pacote Python `codigo.` dentro de V4_RUNTIME_ROOT=/root/v4_labs).
- **WordPress canônico:** `ocafezinho.com` (SSH `cafezinho-wp` = 190.89.239.65, WP-CLI `www-data`, PHP 7.4 CLI). REST usado pelos agentes: `controle.ocafezinho.com` (timeouts 30s ocasionais — 1 falha nacional 12/08 12:51 UTC).
- **Espelho:** `cafezinho.news` (159.65.177.60) — NÃO recebe mais posts V4 desde a migração 12/08 (`V4_MIGRADO_CANONICO_20260812`).
- **Hashes vivos (sha256, 13/08 ~12:15 UTC):** worker `49c2bf5f…` (150.237 bytes, mtime 13/08 12:14 UTC — patch idempotência GLM), intake `e73c21dc…` (12.357 b, 11/08 16:30), coletor `c45b889c…` (47.114 b, 11/08 19:08), redator runtime `ccd23fef…`, vision_router `821b1f1c…`.
- **Crons:** 8 verticais no crontab root + `/etc/cron.d/v4_regional` (intake horário :07 + worker 6×/dia) + `/etc/cron.d/v4_autolimpeza` (arquivamento diário 07:35 UTC). Nada em /etc/crontab.

## 2. Cadeia V4 canônica (traçada ponta a ponta, Fase 1)

1. `coletor.py <alias>` (pol/geo/tec/cul/eco/amb/esp/sad) → RSS diretos + Google News RSS + Brave (freshness="pw" p/ 5 novas; fix V4_FIX_BRAVE_DATE: sem page_age → sem published_at) → dedupe Jaccard 0,60 por título + URL exata → extrai texto (trafilatura, blacklist de domínios) → `estoque_<section>.json`.
2. `v4_vertical_intake.py <section>` → gates fail-closed: missing_identity / missing_or_invalid_source_date / source_date_in_future / source_too_old (TTL 12–48h por vertical) / negative_lula_poll (só política) / tech-nexus (só tecnologia, threshold 4). UPSERT por `item_key` (sha256 URL canônica) — **idempotente por construção**. ⚠️ **As 5 novas NÃO têm gate de nexo editorial** — qualquer item com data válida e texto entra como `new`.
3. `v4_vertical_draft_worker.py <vertical>` (cron): lock global `/tmp/v4_redacao_global.lock` flock -n (perde a rodada se ocupado) → `emit_stall_alert` → `repair_pending_image` (se houver image_pending com wp_post_id: reconcilia mídia existente / externa resolvido / tenta gerar; **válvula final IA após 3 tentativas** por post via `ia_final_tentativas.json`) → cooldown 55min pós-draft_confirmed → quarentenas → expire_stale → select_candidate (1 pauta: status=new, texto≥500, mais fresca, score−poder360 penalty) → duplicate_recent_topic (títulos V4 48h + WP 24h qualquer status, `_is_same_topic`) → no_home/cota home 10%/20% → BEGIN IMMEDIATE status=processing → write_briefing → **subprocess `python3 -m codigo.v4_vertical_redactor_runtime`** (NEWS_STATUS=draft, ZIZI_DEFAULT_PUBLICATION_MODE=draft) → match por `zizi_job_id`==event_id → **V4_IDEMPOTENCIA_20260813: status=wp_created imediato** → enforce_draft_taxonomy (categorias da vertical + CAT_NO_HOME 20699) → enforce_contextual_source → validate_title_clarity → factual_late_gate (fail-open, registra) → staging **pending** → generate_upload_attach_cartoon (banco ouro V3 → WP library → fonte original → Flickr live → busca ativa Commons/Flickr CC → IA conforme política) → candidate=drafted, evento=draft_confirmed.
4. **Redator canônico** (`v4_vertical_redactor_runtime.py`): V4LLMAdapter por contratos (3 tentativas, exclui modelo que falha), JSON estrito (`v4_redactor_json_missing`), título ≤80c sem ":"/"—"/"…" (`v4_title_compound_forbidden` etc.), corpo ≥900c, `<strong>` ok, links/Markdown stripados, cria post **status=draft** com meta zizi_job_id + receipt JSONL em `/root/v4_labs/agent_data/v4/vertical_runtime/`. **Nenhum caminho para publish.**

## 3. Contagens independentes (13/08 ~15:10 UTC) × Codex

| Vertical | drafted (m eu) | Codex | new | estados-nota |
|---|---:|---:|---:|---|
| nacional | 296 | 294 | 34 | 1 image_pending (265482), 1 wp_created, 52 editorial_blocked, 13 stale |
| geopolitica | 309 | 307 | 247 | 1 image_pending (265504), 1 wp_created_failed, 1 duplicate_blocked |
| ciencia_tec_ia | 104 | 103 | 9 | 1 wp_created, 1 wp_created_failed, 1 discarded |
| cultura | 0 | 0 | 14 | 1 image_pending (265473), 1 dup_blocked, 3 quarantena, 9 stale |
| economia | 0 | 0 | 24 | 1 image_pending (265454), 4 quarantena, 20 stale |
| meio_ambiente | 0 | 0 | 28 | 8 quarantena, 6 stale — SEM fila presa |
| esporte | 0 | 0 | 28 | 1 image_pending (265439), 2 quarantena, 18 stale (TTL 12h!) |
| saude | 0 | 0 | 15 | 1 editorial_blocked, 4 quarantena, 9 stale |
| reg. sudeste | 11 | — | 167 | worker regional próprio |
| reg. norte | 3 | — | 547 | 1 image_pending |
| reg. nordeste | 0 | — | 1.481 | **sem tabela draft_events** |
| reg. centro-oeste | 0 | — | 758 | **sem tabela draft_events** |
| reg. sul | 0 | — | 424 | 1 image_pending, 2 eventos |

(Meu número ligeiramente maior = produção continuou após a leitura do Codex. Substitância confirmada.)

## 4. Mecanismo do travamento das 5 novas (prova por evento)

- **cultura:** eventos failed rc=1 (00:05, 01:39 UTC) → duplicate_blocked correto (Margareth Menezes, 04:07) → failed (08:05) → 12:06 post 265473 criado e travado em `image_pending:vertical_sem_ia:cultura`. Órfão 265431 (draft, sem mídia, **cat 2403 "Redação"** — taxonomia nunca aplicada) retentado a cada ciclo. Como `_VERTICAL_SEM_IA={"cultura"}`, nem a válvula final (IA_FINAL_TENTATIVAS=3) libera → **deadlock editorial permanente** até foto real manual.
- **economia:** 4× failed (2 com rc=0 e new_draft_ids [] — falha silenciosa!) → 265454 preso em image_pending → repair_preflight_failed com `ConnectionError cafezinho.news` (era pré-migração, 00:35 UTC) → **resolvido fora da banda**: imagem Kimi + publish Claude.
- **esporte:** 265439 preso image_pending (02:16) → repair 10:16 falhou `vertical_sem_ia:esporte` (esporte NÃO está em SEM_IA — a válvula abriria na 3ª tentativa) → resolvido fora da banda (publish Claude). TTL 12h + cadência 8h = 18 stale_expired.
- **saúde:** failed rc=1 → editorial_blocked `editorial_semantics_opaque_acronym_in_title` ("SUS"), órfão 265471→pending automaticamente (guarda §86) → resolvido fora da banda (publish Claude após revisão).
- **meio_ambiente:** só 2 eventos (11/08 e 13/08), ambos failed rc=1 — nunca completou 1 ciclo. Sem fila presa: a falha é na redação (sem stderr capturado — ver §6).

## 5. Fronteiras também degradadas AGORA (prova)

- **nacional:** 19 repair_preflight_failed/24h; 265482 pending desde 13:20 UTC; reparos falham `vertical_sem_ia:politica` e depois `cartoon_visual_rejected_after_4_attempts` (juiz visual: "números visíveis no relógio = texto proibido"). 13 draft_confirmed/24h.
- **geopolitica:** 38 repair_preflight_failed/24h por `cota_ia_bloco_50pct_estourada`; 265504 preso 15:00 UTC. 17 draft_confirmed/24h. 1 factual_gate_corrected.
- **ciencia:** 33 failed/24h (rc=1, inclui v4_redactor_json_missing intermitente) + 2× wordpress_draft_taxonomy_not_confirmed (12/08, órfãos 265396/265399→pending). 3 draft_confirmed/24h.
- Lock global: 9 rodadas perdidas hoje (nacional 3, ciência 3, geo 1, cultura 1, saúde 1). Log acumulado: 187 preflight_failed (nacional), 210 (geo).

## 6. Lacunas de telemetria (confirmam Codex #9)

- `failed rc=1, new_draft_ids []` não dizem o porquê. O capture de stderr (`*_redactor_stderr.log`) só existe p/ nacional/geo/ciência — **as 5 novas nunca geraram esse arquivo** (falhas anteriores ao patch de hoje 12:14 UTC ou subprocesso sem saída). Receipts JSONL só registram sucessos.
- `factual_gate_skipped` com motivo `sem_claims` (geo/econ/esp) ou `llm_indisponivel` (nacional) — gate factual quase inócuo hoje.
- `orphan_cross_vertical_skip`: cada worker das 5 novas varre ~25 drafts/pending de OUTRAS verticais a cada rodada (dezenas de chamadas WP REST por ciclo) — ruído + custo; backlog de pendentes com até 158h de fila.

## 7. Divergências formais ao Codex (com evidência)

1. **Chamada duplicada de repair:** ausente no vivo (grep: def 1961, única chamada 2530; sha256 49c2bf5f). Era versão pré-patch.
2. **Espelho "parece inativo":** está MORTO no runtime (`if False`, L2510), mas o comentário do cron (V4_NOVAS_FASE0_ESPELHO_20260812) e logs pré-migração ainda dizem "publicando_no_espelho" — dívida documental confirmada; runtime atual = canônico para as 8.
3. **"nenhuma completou ciclo homologado":** parcialmente superado — as 5 novas completaram criação de draft (receipts) e 4 posts foram ao ar pela ponte Kimi+Claude; o que nunca completaram é o ciclo **autônomo** com imagem (sempre image_pending).
4. **Codex não registrou:** quarentena_invented_date é manutenção one-off (não consta em nenhum .py vivo); as 5 novas não têm gate de nexo no intake; cultura está em deadlock permanente por política (não acidente).

## 8. Segurança de publicação (prova negativa)

- Redator: payload `"status": "draft"` fixo (runtime L174). Worker: staging `"status": "pending"` (L2711) e guarda §86 move órfão para pending. Nenhuma string `publish` em posição de escrita no worker/redator/intake/coletor (só `recent_published_titles` leitura, e repair que RECONHECE publish externo sem rebaixar).
- WP canônico: 738 posts publish com zizi_job_id desde 19/07 (promoções externas legítimas), 15 desde 12/08. draft=42, pending=74, trash=48.
- **Conclusão:** nenhum caminho automático chega a publish. O contrato (V4→draft/pending→Claude revisa→publish) está de pé e foi exercitado hoje com 4 posts das novas verticais.

## 9. Próximos passos (Fases 2–3)

- Tabela campo a campo (15 dimensões) novas × nacional/geo.
- Plano de correção em 4 grupos (integridade / operacional / editorial / observabilidade) com backup, teste, rollback e critério de aprovação por item.
- Manifesto do backlog (74 pending + 42 draft) e proposta para wp_created/wp_created_failed retomáveis.
- **Decisões pendentes Miguel:** (a) cultura SEM IA absoluta — manter deadlock ou abrir válvula? (b) ligar worker regional p/ Nordeste+Centro-Oeste? (c) aprovar plano de correção antes de qualquer patch.

---
*Log encerrado 13/08 ~12:40 BRT. Zero escrita em código/servidor/WP nesta fase.*
