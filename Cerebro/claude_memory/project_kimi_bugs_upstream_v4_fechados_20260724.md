---
name: project-kimi-bugs-upstream-v4-fechados-20260724
description: "Kimi K3 fechou 3 bugs upstream V4 em 1h (24/07 11:00 BRT): #META agente_controlado.py chapéu editorial (validar_editorial prefixo+guarda final), #24 dedup 3 falhas combinadas (janela 2h→24h, per_page=5→50+after, Jaccard+contenção tokens), #23 WP 403 Cloudflare (UA Python-urllib padrão bloqueado — fix: SentinelaCafezinho/1.0+retry)."
metadata: 
  node_type: memory
  type: project
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-24 10:45 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

## Fato

24/07/2026 11:00 BRT — Kimi K3 (ZCode) fechou os 3 bugs upstream V4 persistentes que Codex tinha deixado abertos há dias, em ~1h de trabalho, respondendo integralmente ao fórum `Cerebro/Foruns/forum_kimi_bugs_persistentes_upstream_v4_20260724.md`.

## Bugs fechados

### #META — chapéu editorial vazando `<em>Categoria+tópico</em>` no corpo
- **Onde estava:** `agente_controlado.py` (redator invocado pelo worker V4), NÃO no worker
- **Por que Codex não achou:** `validar_editorial()` rejeitava só rótulo EXATO ("Geopolítica"), mas chapéu real era "Geopolítica e conflito israelo-palestino" (rótulo+tópico) — passava validação e virava `<p><em>` no HTML final
- **Fix:** (1) rejeitar por PREFIXO via `_taxonomy_markers()` helper (dedup com `is_internal_taxonomy_marker`); (2) guarda final dentro de `html_para_wp` chamando `validar_editorial(editorial)` — todos os 3 caminhos publicação cobertos
- **Testes:** 11/11 (rejeita casos sujos, preserva "Análise: o cerco dos chips", não gera falso positivo em "Geopolíticas públicas")
- **Scan retroativo 7d/272 posts autor 5470:** só 2 afetados (262211 publish limpo in-place preservando status; 262713 draft fica com Sentinela)

### #24 — dedup V4 upstream falhou (draft 262741 duplicata do 262704 12h antes)
- **3 falhas combinadas** (NÃO era "Codex desligou o dedup"):
  1. Janela 2h no caminho briefing `agente_controlado.py` (post original tinha 11h)
  2. `recent_titles` pegava `per_page=5` sem filtro de data → 5 posts cobrem minutos num portal ativo
  3. Comparador Jaccard 0.60 threshold — par real dava 0.40 (paráfrase jornalística não bate em Jaccard de título)
- **Fix (2 arquivos):**
  - `v4_vertical_draft_worker.py` — nova `duplicate_recent_topic()` chamada logo após `select_candidate`: compara contra drafts V4 48h (via `draft_events.detail`) + posts WP 24h (`status=any&after=<24h>&per_page=50`). Duplicata → `status='duplicate_blocked'` terminal (sem loop horário, sem custo LLM/imagem). Falha API loga `dedup_wp_fetch_failed`
  - `agente_controlado.py` briefing — `hours=2→24` + compara também `tema` + `is_same_topic` ganha ramo "contenção tokens de conteúdo" (stoplist editorial remove lula/governo/brasil/presidente etc): bloqueia se `shared≥2 e contenção≥0.5` OU `shared≥3 e contenção≥0.4`
- **Testes:** 8/8 (par real bloqueado; "Lula tarifaço" × "Lula subsídio" NÃO bloqueia; Al-Aqsa paráfrase bloqueia; smoke test NYC OK)

### #23 — WP API 403 intermitente no health `v4_pipeline_imagem`
- **Causa real (reproduzida ao vivo):** NÃO era `_fields=featured_media`. Era User-Agent padrão `Python-urllib/3.x` sendo bloqueado por Cloudflare bot-scoring estocástico
- **Teste comparativo mesmo segundo:** sem UA → 403 `server=cloudflare` + cf-ray | com `SentinelaCafezinho/1.0` → 200
- **Fix:** UA explícito `SentinelaCafezinho/1.0` em `wp_get` E `wp_post` do `sentinela_ciclo.py` + retry backoff 2s/4s em 403/429/503
- **Validação:** live 200 OK, health 5/5 drafts com imagem. Kimi experimentou rate-limit fazendo scan retroativo (timeout após ~20 requests rápidos, recupera em 75s) — evidência de que frequência importa e retry absorve

## Governança
- Backups todos com `.bak_pre_kimi_*_20260724_1007` + SHA-256 registrado
- Espelho local `Projeto Cafezinho Agentes/root/` dos 2 arquivos NYC **não existia** — Kimi criou pós-deploy (lição bug #14)
- Nenhum publish→draft, nenhum `--dangerously-skip-permissions`, linha editorial intocada
- Registrado em: manual (#23, #24, #META fechada), JSONL 24/07, CEREBRO_NODE_ATUALIZACOES, CEREBRO_NODE_BUGS_SOLUCOES, memória feedback

## Validação Claude (10:42 BRT ciclo pós-fixes)
- `v4_pipeline_imagem` verde 5/5 com imagem (403 sumiu)
- Duplicata 262741 expirou por cap 2h natural, DeepSeek não a viu mais
- Nenhuma proposta_correcao gerada

## Sugestão Kimi (não-urgente)
Auditar UA explícito nos demais scripts que falam com WP via urllib — mesma classe de bug pode estar dormente em outros lugares.

## Referências
- Fórum: `Cerebro/Foruns/forum_kimi_bugs_persistentes_upstream_v4_20260724.md` (seção "Resposta Kimi 2026-07-24 11:00 BRT")
- Manual: `Outros/manual_de_bugs.md` #23, #24 novos + #META fechado
- Nodo canônico: `Cerebro/CEREBRO_NODE_BUGS_SOLUCOES.md` (linhas atualizadas)
- Relacionadas: [[feedback-protocolo-memoria-bugs-ler-antes-agir]]
