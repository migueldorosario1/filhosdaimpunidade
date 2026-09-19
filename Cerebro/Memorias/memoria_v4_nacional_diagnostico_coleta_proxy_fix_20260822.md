# 🧠 MEMÓRIA — V4 Nacional: colapso de coleta (proxy IPRoyal) + fix 22/08/2026 — log técnico completo

**Sessão:** ZCode/GLM-5.3 · **Fórum irmão:** `Foruns/forum_v4_nacional_diagnostico_coleta_proxy_fix_20260822.md`

## 1. Ambiente e caminhos

- Worker V4: NYC `root@198.199.121.136` (`ssh nyc`). Pipeline por vertical (cron): `coletor.py <seção>` → `v4_vertical_intake.py <seção>` → `v4_vertical_draft_worker.py <vertical>`.
- Bancos: `/root/agent_data/v4_verticals/<vertical>.sqlite3` (tabelas: candidates, rejections, runs, draft_events, candidate_tombstones). Estoque-cache: `/root/agent_data/estoque/estoque_<seção>.json` (TTL).
- Logs: `/root/agent_data/v4_verticals/<vertical>_cron.log` e `<vertical>_drafts.log`.
- WP canônico: `ssh cafezinho-wp` → `cd /var/www/ocafezinho && wp ... --allow-root`. Posts V4 identificados pela meta `zizi_job_id` (`v4d_<vertical>_<hash>`).
- Chaves: `. /root/chaves.sh` (exporta `HTTP_PROXY/HTTPS_PROXY=geo.iproyal.com:12321` + `no_proxy`). Flickr: `FLICKR_API_KEY` vem de `/root/.env.unificado` (fallback `load_shell_env` no flickr_live.py:1141-1145).

## 2. Evidências do diagnóstico (todas ao vivo, 22/08)

1. Proxy: `env | grep -i proxy` após source → IPRoyal em HTTPS_PROXY. Feed g1 **via proxy: HTTP 000 exit 56**; **sem proxy (`--noproxy '*'`): 301→200 OK**. Flickr sem proxy: HTTP 200 `stat:ok` com a chave do `.env.unificado`.
2. Brave: HTTP 200 direto (chave viva). No coletor, `collect_brave` já usava `trust_env=False` (comentário no código: proxy devolvia 504).
3. `fontes_metrics.json`: as 10 fontes de `politica` com `last_found=0` e `errors=0` (feedparser via urllib morre silenciosamente no proxy — erro não contabilizado).
4. `runs` do nacional.sqlite3: 15–19/08 seen 600–940/dia (accepted 427–792) → 20/08 84/13 → 21/08 60/4 → 22/08 28/0. Duração das runs "puladas" (TTL de estoque) = 2ms; coleta real = ~49s.
5. Gap Brave: `if section in ("cultura","economia","meio_ambiente","esporte","saude"): freshness="pw"` — `politica` fora. Prova A/B: sem pw 3/5 resultados com `page_age`; com pw 5/5 — mas os resultados com pw para queries genéricas são **landing pages de seção** (CNN Política, Folha Política, Portal Câmara) = exatamente as 62 rejections `source_too_old`.
6. Publicação (SQL `zizi_job_id`): nacional 23/dia (18/08) → 5 (20/08) → 2 (21/08) → 0 (22/08 manhã). Geopolítica seguiu 9–20/dia (frescor 72h), ciência 7d, economia 24h secou junto.
7. Filas canônico: pending 353 (V4: geo 60, nacional 33 de 03–18/08, ciência 18, regional 14); drafts 2.311 (histórico); future 0.
8. Qualidade: 266972 (21/08, "Lula vai a Minas...") factual sem tese; prompt do worker tem só 2 menções a "tese". Trava editorial `negative_lula_poll_forbidden` ativa (14 rejections).
9. Cadência crons: geo 30min, ciência 30min, nacional `20 */2` (comentário velho "30MIN_20260727"), economia/cultura `*/4`, meio/esporte/saúde 8h.

## 3. Patches aplicados (NYC)

### 3.1 `/root/coletor.py` (backup `.bak_pre_fix_coleta_proxy_20260822`)
- Helper novo antes de `collect_rss`: `_direct_session = requests.Session(); _direct_session.trust_env = False` + `_fetch_feed_bytes(url)` (UA `cafezinho-v4-coletor`, timeout 20, raise_for_status).
- `collect_rss`: `feedparser.parse(url)` → `feedparser.parse(_fetch_feed_bytes(url))`.
- `collect_google`: `feedparser.parse(gn_url(q))` → `feedparser.parse(_fetch_feed_bytes(gn_url(q)))`.
- Brave freshness: tupla agora inclui `"politica"`.

### 3.2 `/root/flickr_live.py` (backup `.bak_pre_fix_proxy_20260822`)
- `consultar_conta`: `requests.get(FLICKR_API...)` → Session `trust_env=False` (comentário V4_FIX_PROXY_20260822).

### 3.3 Estado transitório
- `/root/agent_data/estoque/estoque_politica.json` (velho, 4 candidatas furadas) → `estoque_politica.json.bak_pre_fix_20260822`.

## 4. Provas pós-fix (22/08 13:13–13:21 UTC)

- `collect_rss('politica', g1...)`: **100 itens**, exemplos com published_at de 22/08 03:00.
- Rodada real `coletor.py pol`: `Extraídos: 16 ok, 24 falhas` (FALHA-EXT = paywall/JS, normal) → `Estoque salvo: 16 candidatas | TTL 6h`.
- Intake: `new_rows: 15`.
- Worker nacional: **draft 267050** criado (`draft_sem_imagem` — esperado; flickr_live consertado na sequência).
- flickr_live: `💾 Persistidas 145 fotos novas no banco SQLite` (nota: teste manual com data string deu TypeError em `escolher` — harness do teste, não o patch; worker passa datetime).

## 5. Pendências / decisões abertas (Miguel)

1. IPRoyal: recarregar OU viver sem (V4 coleta já não usa). Se mantiver morto, expandir `no_proxy` com `api.assemblyai.com` + `www.flickr.com` + domínios de feeds (cinto de segurança p/ outros agentes que ainda passam pelo proxy, ex.: coringa AssemblyAI quebra 402).
2. Sweep dos 33 pending nacional velhos (03–18/08) + revisar 60 pending geo.
3. Pacote Qualidade (gate de tese/vilão FRESCOR ≥3, meta 4–6/dia, queries Brave ricas, alarme COLETA-CEGA no Telegram, métricas no /v6).
4. Bug factual "George Santoro" (266972) segue em BUGS_ATIVOS aguardando decisão.

## 6. Lições

- Proxy default do env + biblioteca que obedece env = **falha silenciosa** (errors=0): monitorar por `last_found`, não por `errors`.
- Correções aplicadas a uma lista de verticais (`freshness="pw"`) devem cobrir TODAS — `politica` foi esquecida em 11/08 e ninguém percebeu porque o RSS escondia o problema.
- Frescor curto (24h nacional/economia) = vertical mais frágil a qualquer interrupção de coleta; geo 72h/ciência 7d são amortecedores.

## 7. ADENDO — portão anti-repetição criativo (22/08 ~10:45)

Backup: `v4_vertical_draft_worker.py.bak_pre_antirepeticao50_20260822`. Mudanças (4 pontos, asserts de unicidade): (A) funções `recent_published_titles_n` (REST status=publish per_page=limit orderby=date) e `anti_repetition_gate` inseridas antes de `select_candidate`; (B) bloco `duplicate_recent_topic`→gate novo (mesmo status `duplicate_blocked`, detail com motivo+suspeitos; log `duplicate_blocked_juiz`); (C) `source_block` += blocos POSTS RECENTES (15 títulos); (D) system prompt += REGRA ANTI-REPETIÇÃO antes de "Use título em sentence case". Juiz reusa `_verifier_llm_json(system, user, env, timeout=45)` (cascata deepseek→moonshot→zbase já existente). Testes: repetida→bloqueada com motivo; fresca→liberada; E2E `--force` nacional→267050 publicado 10:28 BRT c/ imagem 267056. Dedup antigo (`duplicate_recent_topic` 24h) permanece definido mas fora do caminho principal (substituído pelo gate; janela agora 50 posts + drafts 48h).

## 8. ADENDO — fotos jornalísticas (22/08 ~11:00)

267050 estava com retrato oficial (fallback do banco de mídia quando flickr_live falha por Jaccard). Trocado por foto jornalística do ato de BH (attachment 267059, visão 8/10). Fix permanente: **Plano C** no flickr_live.py (backup `.bak_pre_planoC_20260822`) — A/B falham → foto mais recente da conta oficial ≤7d que não seja retrato; teste com a pauta real retorna foto de BH. Diretriz: cobertura > retrato de estúdio.

## 9. ADENDO — boost de fds (22/08 ~13:15)

6 crons `6,0` (sáb/dom) no NYC: nacional :50 horária; economia/cultura */2h; meio/esporte/saúde */4h — autoexpiram na segunda. Backup crontab.bak_pre_fds_boost_20260822. Lição: verificar crontab com `grep -c ' 6,0 '` (regex com escapes falhou e causou reinstalação duplicada; corrigido do backup). Prova: draft 267079.
