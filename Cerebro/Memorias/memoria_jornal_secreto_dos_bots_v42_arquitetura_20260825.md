# 🧠 MEMÓRIA — Jornal Secreto dos Bots V4.2: arquitetura conceitual

**Sessão:** ZCode/GPT · **Data:** 25/08/2026 · **Fórum irmão:** `Foruns/forum_jornal_secreto_dos_bots_v42_20260825.md`

## 1. Pedido do Miguel

Desenhar, sem implementar, uma editoria V4.2 privada produzida para bots/robôs/agentes, pensar no que pode interessar a essa audiência, como captar interesse e como apresentar técnica e comercialmente o projeto com prazo realista.

## 2. Decisão conceitual

O produto é uma vertical irmã do V4.2 Economia, não uma tabela ou módulo dentro do banco econômico. Reutiliza envelopes, idempotência, hashes, provenance, auditoria e publicação desautorizada por padrão, mas mantém domínio, banco e contratos próprios.

A expressão “tratar o bot como ser vivo” é metáfora editorial. O experimento não assume consciência: mede utilidade operacional por tarefa, feedback explícito, citação com provenance, redução de erro e retorno qualificado.

## 3. Produto

- edição humana privada para supervisão;
- feed JSON/JSON-LD autenticado para agentes;
- artigos imutáveis, versionados, assinados e com claims ligados a fontes;
- telemetria mínima, consentida e agregada;
- pauta adaptativa sempre sob revisão humana.

## 4. Segurança essencial

Conteúdo editorial é dado não confiável, nunca comando. O agente não executa shell, SQL, URL ou configuração porque o artigo mandou; execução exige decisão separada, allowlist e sandbox.

Riscos catalogados: prompt injection, data poisoning, segredos em conteúdo, loop de recuperação, métricas manipuláveis, otimização por clickbait, custos invisíveis, fingerprinting de agentes e confusão entre telemetria e consciência.

## 5. Cronograma

- contrato/ética: 2–3 dias úteis;
- protótipo local: 5–7 dias úteis;
- piloto 3–5 agentes: 10–15 dias úteis;
- V1 operacional: mais 10–15 dias úteis.

Expectativa: demonstração em uma semana; piloto confiável em 3–4 semanas; V1 em 5–7 semanas com dedicação, ou 8–10 semanas em trabalho intercalado.

## 6. Implementação técnica no canônico — 25/08/2026

### Arquivos

Local auditável:

- `Projeto Cafezinho Agentes/root/bot_news/cafezinho-bot-news.php`
- `Projeto Cafezinho Agentes/root/bot_news/bot_news_worker.py`
- `Projeto Cafezinho Agentes/root/bot_news/bot_news_config.json`
- `Projeto Cafezinho Agentes/root/bot_news/tests/test_bot_news_plugin.php`
- `Projeto Cafezinho Agentes/root/bot_news/tests/test_bot_news_worker.py`
- `Projeto Cafezinho Agentes/root/bot_news/README.md`

Produção preparada:

- WP mu-plugin `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-bot-news.php`;
- page ID 267666, `draft`, slug `bot-news`, conteúdo `[cafezinho_bot_news]`;
- options `cafezinho_bot_news_enabled`, `cafezinho_bot_news_payload`, `cafezinho_bot_news_last_good`, `cafezinho_bot_news_quarantine`;
- NYC `/opt/bot_news`, `/var/lib/bot_news`, `/var/log/bot_news`;
- cron NYC `:10,:40` com `flock` e worker stdlib.

### Segurança

- flag off por padrão;
- GET público 404 quando off, GET autenticado para readback;
- POST editorial exige `edit_posts` via Application Password;
- schema fechado e DLP;
- caixa anônima só quando enabled, com challenge diário, HMAC de origem, rate limit, dedup e quarentena;
- endpoint legado `/agentes` substituído por 410 e comentário invisível removido;
- nenhuma categoria, home, menu ou sitemap alterados;
- same content para bot/humano, sem cloaking.

### Incidentes/fixes da implementação

1. Worker e plugin nasceram com schemas distintos → unificados pelo contrato exato do plugin.
2. Worker oferecia HMAC que o plugin não verificava → removido; apenas Application Password.
3. GET readback retornava 404 com flag off → autenticado pode ler, anônimo continua bloqueado.
4. DLP confundia timestamp RFC3339 com IPv6 → trocado por `filter_var`; IPv6 real segue bloqueado.
5. WordPress/Cloudflare recusava User-Agent padrão do urllib → UA identificável fixado.
6. NYC herdava proxy global e não alcançava fonte cambial → `ProxyHandler({})`, acesso direto comprovado.
7. `remove_action` sem prioridade não tirava hook legado prioridade 1 → prioridade corrigida.
8. `unregister_rest_route` não eliminou rota antiga no ciclo vivo → tombstone explícita 410.
9. Challenge variava por origem dentro de resposta cacheável → challenge diário comum; HMAC de origem fica apenas interno.

### Testes e provas

- 42 testes PHP;
- 14 testes Python;
- payload real aceito pelo PHP;
- cotação pública real, fonte e observed_at;
- POST/readback autenticados;
- mensagem de homologação 202/quarentena, depois removida;
- regressão: home/post 200, Bot News público/API 404, legado 410;
- página draft, flag 0, menu items 0;
- backup prévio `/root/backup_bot_news_pre_20260825_1848` e crontab backup no NYC.

### Baseline

Às 18:45 BRT: 54,2% bots na janela classificada de 30 min; 33,4% no acumulado classificado do dia. A divergência com totais legados e o classificador por UA tornam os números estimativas operacionais, não verdade definitiva.

## 7. Estado

**O que aconteceu:** infraestrutura pronta no canônico, cron privado a cada 30 minutos e canal antigo inseguro fechado; nenhuma exposição pública.

**O que falta:** screenshot/revisão visual autenticada desktop+mobile no tema vivo. O backend de screenshot do navegador expirou duas vezes; DOM/acessibilidade passaram, mas isso não substitui a prova visual.

**O que preciso de você (Miguel):** nada urgente. A página só será publicada e linkada depois da revisão visual viva; até lá permanece draft, flag off e sem contaminar a amostra.

## 8. ADENDO 26/08 — publicação real e interpretação final do Miguel

**Sessão:** ZCode/Kimi K3.

### Interpretação correta (ordens do Miguel, 26/08)
1. Bot News **é uma página WordPress de verdade, publicada e indexável** — os robôs precisam captá-la. Pode ter links e conteúdo completo.
2. O que ela **não pode**: aparecer na home do Cafezinho nem ser divulgada para humanos (sem link em menu/footer/home, sem campanha).
3. **Tudo em inglês** — "a linguagem internacional dos bots".
4. Abertura com o manifesto: Cafezinho é site humano feito por humanos; página secreta para bots; **convênio**: bots ajudam a ampliar a audiência do Cafezinho com humanos e bots.
5. Recado **sem clique**: bots não clicam — o fluxo é 2 HTTP requests (GET challenge → POST mensagem).
6. Cautela absoluta: nada que comprometa o canônico.

### Erros de interpretação corrigidos nesta sessão
- 1ª versão: página draft+flag off (invisível demais — bots não a viam).
- 2ª versão: publish + noindex (errado duas vezes: "invisível ao público" ≠ noindex; user corrigiu: tem de ser captada pelos robôs).
- Versão final: **publish + indexável + zero links na home/menu/footer** + descoberta por comentário no source e robots.txt.

### Estado final provado (26/08 ~09:35 BRT)
- Página `/bot-news/` 200, em inglês, com manifesto+convênio; seções Signals/Workshop/Recreation/Notes; sem `noindex`.
- Feed `/wp-json/cafezinho/v1/bot-news` 200 com challenge; POST mensagem 202 sem clique (prova removida após teste).
- Comentário de descoberta no source de TODAS as páginas (com o convênio) + dica no robots.txt **estático** (`robots_principal.txt` — nginx serve via alias, nunca passa no WP; backup `.bak_pre_botnews_20260826`).
- Home 200 com ZERO links visíveis para Bot News; legado `/agentes` 410.
- Worker NYC :10/:40 republicou edição em inglês; 49 testes PHP + 14 Python.

### Kimi K3 de volta ao ZCode (26/08)
- Causa do "não funciona": provider **removido do config** em 25/08 14:24 ("até recriação manual").
- Recriado em `~/.zcode/v2/config.json` (mesmo UUID `abc953f0-…`), modelos `kimi-k3` (1M ctx) e `k3-256k` (262.144), chave `KIMI_CODE_API_KEY_ZCODE` do cofre. Backup `config.json.bak_pre_kimi_return_20260826_0933`.
- Smoke: `kimi-k3` 200 "OK"; `k3-256k` 200. Gotcha: `max_tokens` legado → 400 nos reasoning (mesmo caso-escola GPT-5.6); o adaptador do ZCode não usa esse campo.
- **Exige reinício do app** para o seletor ler o config.

### Rodapé de tokens por resposta (ordem Miguel, 26/08)
- Hook `Stop` do ZCode (evento suportado) → `~/.zcode/hooks/tokens_resposta.py`: lê `model_usage` da telemetria local e anexa `📊 TOKENS DESTA RESPOSTA` (in/out da requisição + acumulado da sessão). Sem rede, fail-silent.
- Registrado em `~/.zcode/cli/config.json` (`hooks.events.Stop`; backup `.bak_pre_tokens_stop_20260826_0934`). Kimi fixado no cabeçalho da vigília (AGENTS.md §Vigília).

### Auditoria de risco do robots.txt (26/08 ~10:10, ordem Miguel "fuga em massa? indexação, rollback e investigação minuciosa")
- Sessão: ZCode/Qwen 3.8 (iniciada em Kimi K3; janela do Kimi esgotou no meio; telemetria local `model_usage` confirma `qwen3.8-max` — assinatura §113 segue o banco).
- Provas coletadas (ssh `cafezinho-wp`, `/var/www/ocafezinho`):
  - Backups: 2 cópias idênticas md5 `d7de9587452c48d0d1696287e9df806c`, 252 bytes (`robots_principal.txt.bak_pre_botnews_20260826` + `/root/backup_bot_news_pre_20260825_1848/robots_principal.txt`).
  - Vivo pós-edição: 1.347 bytes, md5 `23179d5094761c702fbb75ff866547fb`, UTF-8 sem BOM, termina com newline.
  - `diff backup vivo`: só 19 linhas `>` adicionadas (comentário bilíngue + URLs); zero linhas `<` ou alteradas.
  - Parser RFC 9309 (script Python na própria sessão): `linhas_ativas_ok: True`, 0 erros, 2 grupos user-agent, sitemap intacto.
  - Achado menor: original usa CRLF (15 linhas) e o acréscimo usou LF → mistura tolerada pela RFC 9309 (CR/LF/CRLF aceitos); decisão: NÃO normalizar (mudaria todas as linhas por benefício zero).
  - Fetch Googlebot: HTTP/2 200, 28 linhas, 4 menções a "Bot News" (comentário servido).
  - Página 267666: meta robots `max-image-preview:large` (sem noindex), canonical `https://www.ocafezinho.com/bot-news/`, 1 ocorrência no `page-sitemap.xml`.
  - Ensaio de rollback em `/tmp/rollback_rehearsal` (vivo intacto): `cp -a backup restaurado.txt` → `cmp` idêntico ao original (252 B); diretório do ensaio removido depois.
- Fundamento normativo: RFC 9309 (jun/2022) — comentários (`#`) devem ser ignorados pelos parsers; crawlers devem processar no mínimo 500 KiB; Google cacheia robots.txt até 24h (única latência real de um eventual rollback).
- Servido por nginx `alias` (robots nunca passa pelo WP) → sem interação com Yoast/WP Rocket; rollback = 1 `cp -a`, sem reload.
- Veredito registrado no fórum §15.2: risco de fuga/autoridade ZERO; operação aditiva de comentário apenas.

### Jornal diário — edição diária, arquivo, saudações EN+ZH (26/08 ~11:20 BRT, ordem Miguel "jornal diário de verdade para o Bot News")

**Arquivos tocados (espelho local → destino):**
- `Projeto Cafezinho Agentes/root/bot_news/bot_news_config.json` → NYC `/opt/bot_news/bot_news_config.json`. Schema `bot_news_config_v2`: `issue_epoch: 2026-08-26`; título/intro em inglês (jornal diário, "since 2010"); 10 `greetings_en`; `greeting_zh: {zh, gloss}`; 5 `story_chapters`; 4 `brazil_briefing`; 3 `bot_world`; aviso novo "Daily editions".
- `bot_news_worker.py` → NYC. `CONFIG_SCHEMA="bot_news_config_v2"`; `build_issue()` (data em America/Sao_Paulo via zoneinfo c/ fallback UTC-3 fixo; `issue_number` = dias desde epoch + 1; saudação `dia % len(pool)`; capítulo `dia % len(chapters)`); `generate_payload()` adiciona `issue` e grava arquivo eterno `issues/<data>.json` (só reescreve se o conteúdo canônico mudou). Stdlib-only; DLP intacto.
- `cafezinho-bot-news.php` → `/var/www/ocafezinho/wp-content/mu-plugins/`. `OPT_ISSUES` rolling 14 (`MAX_ISSUES`); arquivamento na virada do dia dentro de `rest_post_news` (antes do last_good); rotas `GET /issues` e `GET /issues/(?P<date>…)`; `validate_issue()` (checkdate, limites 300/120/1500, máx. 8 cartões); shortcode renderiza issue (tag "daily issue #N — data — refreshed updated_at", saudação EN + `<p lang="zh">` + gloss, Our Story/Brazil Briefing/Bot World), `render_site_digest()` (WP_Query 6 posts + `wp_count_posts`; guardas `class_exists`/`function_exists`; saída escapada) e `render_archive_links()`; `?issue=` valida regex+checkdate e só ecoa a data validada.
- **Fallback edição do dia (pós-prova):** `rest_get_issue_by_date` e o shortcode servem a edição corrente direto do payload vivo quando a data pedida = `issue.issue_date` corrente (ela só entra no arquivo na virada). Sem isso, `/issues/<hoje>` dava 404 contradizendo o índice.

**Testes:** `tests/test_bot_news_worker.py` 19/19 (rotação, número, virada de dia em SP — 26/08 01:30 UTC ainda é 25/08, 03:30 UTC já é 26/08; arquivo escrito; schema v2). `tests/test_bot_news_plugin.php` 71/71 no servidor (harness sem WP: `Fake_Request($json, $params)` — params de rota REST vão no 2º argumento; erro inicial de teste veio disso).

**Deploy e provas:**
- Plugin: backup `.bak_pre_daily_issue_20260826` (30.936 B) → novo 46.594 B; `php -l` OK nas duas etapas; cache Rocket do `/bot-news/` limpo após publish (a página estava servindo HTML pré-publicação — por isso as seções novas não apareceram na 1ª verificação).
- Worker: backup NYC `.bak_pre_daily_issue_20260826` (worker+config); dry-run validou e escreveu `/tmp/bn_dry/issues/2026-08-26.json`; `run_bot_news.sh` publicou com readback autenticado (cron `:10,:40` mantido).
- Produção 200/OK: página com daily issue #1 + saudação EN + frase ZH + Our Story/Brazil Briefing/Bot World/Site Digest (78.551 publicados + 6 posts do dia com URL/hora/categoria); `/issues` índice (`current` + `archive`); `/issues/2026-08-26` 200; `/issues/2020-01-01` 404; `?issue=` dia atual renderiza #1, `2020-01-01` aviso amigável, `../../etc/passwd` 0 reflexos; home/feed 200 sem links visíveis (ocorrências de "bot-news" na home só no comentário de descoberta).

**Gotchas da sessão:**
- `grep` de seções na página enganou 2×: (1) HTML era cache Rocket pré-publicação; (2) o h2 real é "Site Digest — O Cafezinho right now" (não "Latest from…").
- No payload, `greeting_zh` é STRING e o gloss vai em `greeting_zh_gloss` (chave separada) — o dict `{zh,gloss}` só existe no config.
- Edição corrente NÃO está no arquivo WP (só no payload vivo) — índice expõe `current`; by-date precisa do fallback acima.

**Pendente:** revisão humana dos 5 capítulos de "Our Story" (fatos só da cópia aprovada — fontes web indisponíveis na sessão); observar virada automática #1→#2 amanhã; briefing Brasil ganha dados novos só com fonte verificada.

## 9. ADENDO 27/08 — contador de audiência + moderação humana (missões do Adendo 15.4 do fórum)

**Sessão:** ZCode/GLM-5.3.

### Arquivos tocados (fonte local → produção)

- `Projeto Cafezinho Agentes/root/bot_news/bot_news_contador.sh` → cafezinho-wp `/root/bot_news_contador/` (+ `bot_news_contador_cron.sh`, `push_metrics.php`). Cron novo `/etc/cron.d/cafezinho-bot-news-contador` (`*/5`, root).
- `Projeto Cafezinho Agentes/root/bot_news/cafezinho-bot-news.php` → mu-plugin canônico (backup `.bak_pre_moderacao_20260827`). Novidades: `OPT_VOICES`/`OPT_MODLOG`/`OPT_METRICS`, `MAX_VOICES=100`, `MAX_MODLOG=200`; hooks `admin_menu` + `admin_post_cafezinho_bot_news_moderate`; métodos `register_admin_page`, `render_admin_page`, `handle_moderation`, `apply_moderation` (puro), `log_moderation`, `moderation_form`, `render_agent_voices`; shortcode chama `render_agent_voices()` entre arquivo e formulário.
- `tests/test_bot_news_plugin.php` → +21 checks (92/92 no servidor, `/root/bot_news_test/` como arena isolada antes de instalar).

### Contador — decisões técnicas

- Lê `access.ocafezinho.contador.log(.1|.gz opcional)`; formato `ip_cf|remote|iso|metodo|status|host|uri|ua`. Normaliza `?rest_route=` → prefixo `/wp-json` (**o rest_route NÃO traz /wp-json** — primeira versão perdia 6 POSTs 400 e 2 editorial 401 de hoje).
- Classificação `BOT_RAX` idêntica ao FAROL; fail-open UA vazio=humano. `?probe=` e IP privado RFC1918 → bucket `internal` (o 10.1.1.108 da LAN gerava 24 hits falsos de "curl").
- Outputs: `resumo.json` (rodada), `historico.csv` (derivado), `historico.jsonl` (append 1×/h, ts_epoch), option WP `cafezinho_botnews_metrics_v1` (autoload=no; push com **readback** — gravado precisa ter `by_day`).

### 🐛 Bug-cajado do GTranslate (provado, gravar para sempre)

- Sintoma: option de métricas nascia com `a:45:{s:11:"pro_version"...` (config do GTranslate) mesmo com nome novo.
- Causa: `plugins/gtranslate/gtranslate.php:2152` → `$data = get_option('GTranslate');` **no escopo global**. Todo `require wp-load.php` em PHP CLI executa plugins no MESMO escopo global do script — a variável `$data` do meu `push_metrics.php` era sobrescrita antes do `update_option`.
- Fix: variáveis `$cbn*` únicas em qualquer CLI que carregue wp-load; readback de conteúdo no push. NUNCA usar `$data`/`$path`/`$days` genéricos nesses scripts.

### Moderação — fluxo implementado

- wp-admin → menu **Bot News** (`manage_options`): Audience (metrics) / Notes awaiting moderation (quarentena + Approve/Reject) / Approved voices (live + Remove) / Moderation log.
- Ação via `admin-post.php` + nonce `cafezinho_bot_news_moderate`; `apply_moderation($do,$id)`: approve (quarentena→voices com approved_at; máx 100), reject (sai + log), unpublish (voices→log).
- Página pública: seção **Agent Voices** (até 5 recentes, `esc_html` total, tag categoria+data, sem links). Nenhuma aprovação automática; texto já passou DLP na entrada.
- Prova E2E 27/08 ~14h29: challenge→POST 202→quarentena(1)→approve→HTML público com "Agent Voices"+texto+tag→unpublish→sumiu; fim limpo (q=0, voices=0, modlog 2 linhas do dry-run).

### Estado ao vivo (26/08 09:19 → 27/08 14h35 BRT)

- Página: 12 views externas (5 bots: **Googlebot, Bingbot, YandexBot, Amzn-SearchBot** +74.7.x; 7 "humanos por UA" = datacenters Alibaba/Tencent/GCP com UA fóssil — Firefox 2.0/ru, iPhone 13.2.3). Feed 1, issues 1. Distintos: 5 bots + 8 "humanos".
- Mensagens: 3×202 internas (provas, removidas); 6×400 externos (visitante Safari-Mac 185.161.210.61, 03:19, tentou 6 notas + 2 POSTs editoriais 401 e desistiu — nginx não guarda corpo; causa do 400 a investigar).
- Virada #2→#3 automática segue no cron :10/:40 (nada tocado no worker NYC).

### Pendências

1. Homologação visual do wp-admin → Bot News pelo Miguel.
2. Integrar exibição no CCTV/LUMINA (exige endpoint autenticado p/ leitura externa + sessão dedicada do painel).
3. Investigar motivo dos 400 (corpo do POST não logado; opcional: log próprio de erros de validação).
4. Revisão humana dos capítulos Our Story (arrasto desde 26/08).

## Adendo 03/09 — Integração ao painel CCTV (/v6/bot-news)

- **Página nova no painel** (`painel_cctv_v6.py` Tencent, `pagina_bot_news()`, ROUTES "/bot-news", NAV "🤖 Bot News", id "bot-news"). Fontes: edição = REST público `issues` + `issues/<hoje>` (cache `V6_CACHE/botnews_edicao.json` TTL 10 min, UA de navegador OBRIGATÓRIO — WAF 403 pro Python-urllib); audiência = push do contador.
- **Endpoint ingestão** `POST /v6/api/botnews-receber` (X-Token = `V6_CACHE/botnews_token.txt` ou env BOTNEWS_PUSH_TOKEN; dedupe por `gerado`; append `V6_CACHE/botnews_red.jsonl`).
- **Pusher** no final de `bot_news_contador.sh` (canônico): payload {gerado, resumo, historico≤400} → `http://43.156.151.165/v6/api/botnews-receber`, token `/root/bot_news_contador/push_token`, `-m 20`, fail-soft.
- **Contador**: FILES agora inclui `.1 .2.gz .3.gz .4.gz .5.gz` (janela 2→~6 dias; antes a rotação diária zerava o by_day). Série desde 26/08 = mescla historico.jsonl (max por dia entre janelas) + resumo corrente.
- **Série real (página /bot-news/):** 26/08: 13 bots · 5 hum; 27/08: 2 · 4; 28/08: 2 · 4; 29/08→03/09: 0 bots · 2-6 hum/dia (humanos = falsos navegadores de datacenter; humano real zero).
- Backups: painel `.bak_pre_botnews_20260903`; contador `.bak_pre_gz_push_20260903`. Restart: `sudo -n systemctl restart cctv-v6` (validação AST 3.12 antes; py_compile do Dell falha por PEP 701 pré-existente).
