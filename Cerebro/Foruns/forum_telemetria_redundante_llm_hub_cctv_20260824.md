# 📊 Fórum — Telemetria LLM redundante em todo o sistema + hub na página de custos do CCTV (24/08/2026)

**Sessão:** ZCode/GLM-5.3 (sess_c3b1edeb) · **Gatilho:** ordem do Miguel 24/08 ~10:00 — "qualquer iniciativa que use LLM precisa ter telemetria robusta, redundante… regra de pedra… varredura do sistema… acompanhável online na página de custos do CCTV". Regra gravada como **regra viva §118** (GOVERNANCA).

## 1. O que JÁ existe (espinha dorsal — 4 pilares maduros)

| Pilar | Onde | O que faz |
|---|---|---|
| **`telemetria_api.py`** | NYC `/root/` (espelho no Dell `agentes_tematicos/`) | Instrumentação universal: `registrar_chamada_api(provider, modelo, tokens, agente, contexto)` + wrapper `instrumentar(agente=...)` que intercepta `requests.post`/openai em scripts legados; fail-open, anti-double-count, corr_id |
| **`gerenciador_tokens.py` + `banco_custos_YYYY-MM.jsonl`** | NYC `/root/agent_data/` + droplet 159.89 | Ledger canônico append-only com fcntl, rotação mensal, preços em `/root/agent_data/precos_modelos.json`; `registrar_gasto()` |
| **`governanca_financeira_api_usage.jsonl`** | NYC (cron `coletar_custos_internos.py` às :07) | 2ª camada (redundância) consolidando por agente/modelo |
| **Painel CCTV v6 — página de custos** | `tencent:/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (serviço `cctv-v6` :8084, `pagina_custos()` L2021, lê `/home/ubuntu/cafezinho/v6_data/custos/`, sync horário do NYC, warm-cache */25) | **Já renderiza custos consolidados em R$ com ranking de LLMs — é a página online pedida** |

Complementos vivos: `vigia_custos_baleia.sh` (cap US$ 5/dia + anomalia 1,5×, alerta Telegram), `enviar_boletim_custos.sh` (boletim 8h/18h só Miguel), `credito_vigilia.py` (saldos), ZCode `model_usage` (db.sqlite), Tencent `consumo.custo_usd` (pontos_api), Moka `/telemetria` (feito 24/08), droplet 159.89 já registra via roteador Cícero ("zero gap").

## 2. GAPS — quem chama LLM SEM registrar (raiz dos furos de 24/08)

1. 🔴 **`v4_vertical_draft_worker.py`** (NYC; usado também por `v41_ciclo.py`) — o redator V4/V4.1, **maior gastador vivo (OpenAI gpt-5.5, US$ 39/5d)**: chamadas diretas a z.ai/deepseek/moonshot **sem `registrar_gasto`**.
2. `agentes_tematicos/v4/nucleo_llm.py` + `nucleo_visao*.py` + `gerador_imagem_editorial.py` (Dell/réplicas)
3. `.codex_work/agente_auditor_titulos_gpt.py`
4. ZCode `model_usage` não exporta pro hub; Tencent `consumo` não alimenta o hub; Moka ledger é local do navegador (BYOK).

## 3. Arquitetura alvo (regra §118: local durável + push redundante + online)

```
chamador LLM ──► telemetria_api.instrumentar() ──► banco_custos_YYYY-MM.jsonl (local, append-only)
                                                    └► governanca_financeira_api_usage.jsonl (2ª via, :07)
sync horário NYC──► tencent:/cafezinho/v6_data/custos/*.json ──► painel /v6/custos (online, R$)
vigia 30min ──► alerta cap/anomalia (Telegram)   |   reconciliação semanal ──► CSV oficial das plataformas
```

## 4. Etapas (executor + prazo)

- **E1 (URGENTE, próxima sessão/ronda): instrumentar o redator V4/V4.1** — `instrumentar()` do telemetria_api.py no `v4_vertical_draft_worker.py` (e conferir `v41_ciclo.py`); idem nucleo_llm/visao/gerador_imagem/auditor_titulos. É o gap que deixou US$ 39 invisíveis.
- **E2: fontes novas no hub** — exportador ZCode (db.sqlite→jsonl formato banco_custos, agente="zcode") + Tencent consumo + droplet 159.89 no sync do `v6_data/custos/`.
- **E3: página de custos** — blocos por sistema (V4.1/ZCode/Moka/Tencent/temáticos) + linha de reconciliação (custo medido × faturado pelas plataformas).
- **E4: reconciliação semanal automatizada** — robô baixa/consome os CSVs oficiais (como os zips de 24/08), compara com banco_custos, flag de divergência >10% no boletim.
- **E5: auditoria de conformidade §118 na ronda CCTV** — checklist "todo chamador registrado?" (varredura grep periódica por chamadas HTTP a provedores sem instrumentar).

## 5. Estado / falta / preciso do Miguel

- **Feito:** regra §118 gravada; varredura completa; desenho; fórum+memória.
- **Falta:** E1–E5 (E1 na próxima sessão com contexto fresco — cirurgia em produção NYC).
- **Preciso do Miguel:** nada por agora — aprovação implícita já dada ("faça"); E1 executa na sequência e reporta no Telegram.

---

## 🔬 ADENDO 6 — FURO 2 §118 (25/08 ~18:05): redator V4.1 invisível por DUAS camadas (subprocesso + SDK OpenAI) — FIXADO E PROVADO

**Gatilho:** queixa do Miguel 25/08 ~17:56 — "a página de custos ao vivo continua a só aparecer Repetidor Estatal. é o único que aparece. não faz sentido".

**O painel estava são:** ranking 24h por agente com barras + tabela com rajadas ×N agrupadas + cotação — ele mostrava a realidade do ledger. No ledger o Repetidor dominava (72 dos últimos 100 eventos: 38 `Repetidor_Estatal` + 17 `Repetidor Auditor` + 17 `repetidor_estatal` minúsculo) porque é o único fluxo volumoso instrumentado. O V4.1 (joia da coroa) tinha **ZERO registros em agosto** (`grep -c v4_1_ciclo = 0`) apesar de redigir o dia inteiro — prova: ciclo 17:26 BRT → rascunho 267658, gpt-5.5, FC websearch com claims confirmadas. Gastou sem registrar.

**Causa raiz em 2 camadas (o fix da manhã de 25/08 era necessário mas insuficiente):**
1. **Subprocesso:** o redator do V4.1 NÃO é o `v4_vertical_draft_worker.py` (aquele era o V4, aposentado) — é `codigo.v4_vertical_redactor_runtime.py`, disparado por `v41_ciclo.py` via `subprocess.run`. Monkey-patch não atravessa fronteira de processo: instrumentar o arquivo errado nunca alcançaria o runtime real.
2. **SDK OpenAI:** `instrumentar()` prometia no docstring envelopar o SDK OpenAI (`_INSTRUMENTADO` tem a chave "openai"), mas **o envelopamento nunca foi implementado** — só existiam wrappers de `requests`. E o `llm_adapter` chama gpt-5.5 por `client.chat.completions.create` (SDK → httpx), invisível para qualquer wrapper de requests.

**Fix (3 peças, backup antes, fail-open em tudo, ast.parse antes de gravar — patcher `/tmp/patch_v41_telemetria_furo2.py` no padrão local+scp+validar):**
- `/root/telemetria_api.py` (`.bak_openai_sdk_20260825`): NOVA `_instrumentar_openai()` — envelopa `openai.resources.chat.completions.Completions.create` e `responses.Responses.create`; extrai usage (chat: prompt/completion; responses: input/output), provider via base_url do client; disparada de dentro de `instrumentar()`.
- `/root/v4_labs/codigo/v41_ciclo.py` (pai, `.bak_telemetria_subproc_20260825`): `instrumentar(agente="v4_1_ciclo")` no topo — pega o FC websearch (Perplexity via requests) do próprio ciclo.
- `/root/v4_labs/codigo/v4_vertical_redactor_runtime.py` (filho, `.bak_telemetria_20260825`): `instrumentar(agente="v4_redator")` após os imports — o subprocesso se instrumenta sozinho.
- Higiene: cópia velha `/root/tematicos/agentes_tematicos/telemetria_api.py` (sem wrapper Session nem `chave_apelido`; superset confirmado por diff = 0 linhas exclusivas) sincronizada da canônica (`.bak_pre_sync_20260825`, md5 iguais `2229b21a`).

**Provas (ponta a ponta):** chamada real pelo SDK → registro no ledger `selftest_openai_sdk · gpt-4o-mini · 13/2 tok · US$ 5,2e-05 · chave_apelido "v4 cafezinho (openai)" · corr_id` → flusher */1min levou ao tencent (ao_vivo_nyc.jsonl mtime 18:03:58) → endpoint interno :8084 E público `http://43.156.151.165/v6/telemetria/v1/ultimos` com `ok:true` e o evento visível (usd_brl 5,17). O traceback da 1ª tentativa (401 DeepSeek) já mostrava `_create_telemetrado` na pilha — o wrapper intercepta o caminho do SDK.

**Próximo marco:** 1º ciclo real pós-fix (nacional ~19:25 BRT, ciência ~19:45, geo ~19:55, eco ~21:35) deve gravar `v4_redator`/`v4_1_ciclo` com custo real — a ronda §118 (automation-1874aaf5, */1h :30) segue plantada pra telegramar o MARCO ao Miguel.

**Achado extra (pendência de credencial):** `DEEPSEEK_API_KEY` do `.env.unificado` do NYC responde **401** (sufixo mascarado 96ba) — mesma família da pendência M (401 no tencent). A cascata do V4.1 pula o DeepSeek por isso. Quando o Miguel girar a chave, espelhar nos cofres (Regra 4).

**Estado:** ✅ furo fechado no código e provado ponta a ponta · 🔄 aguardando 1º registro real do `v4_redator` (ronda confere) · pendência: chave DeepSeek NYC 401.

**Adendo 6.1 (25/08 ~18:55, após print do Miguel às 18:46):** o fix JÁ aparecia no painel (ranking com 12 sistemas, `v4 redator` US$ 0,19 às 15:38 em gpt-5.5; 1º registro real do V4.1 pós-fix ✔). A sensação de "só repetidor" vinha de 2 defeitos visuais, corrigidos no `painel_cctv_v6.py` (`.bak_casing_20260825`): (a) ranking agora agrega `por_agente` por `casefold` — `Repetidor_Estatal` e `repetidor_estatal` minúsculo eram O MESMO agente contado em 2 linhas (agora $3,02 numa linha); tabela agrupa rajadas independente de casing; (b) intervalo das rajadas não sai mais invertido (`Math.min/max` em ini/fim). Provas: AST 3.12 OK no servidor (falso negativo 3.10 local confirmado de novo), restart cctv-v6, 8084 e público 200 em `/custos`, `/custos/ao-vivo`, `/v6/custos`, `/v6/custos/ao-vivo`. Nota de leitura: o Transkriptor (`youtube_transcriber_autonomo`, US$ 24/24h) é o maior custo da janela — gastão conhecido e auditado.

---

## 🔬 ADENDO 7 — POLUIÇÃO no ao-vivo (25/08 ~23h): wrapper Session registrava chamadas NÃO-LLM — FIXADO, FILTRADO E PROVADO

**Gatilho:** queixa do Miguel ~23h — "página custos ao vivo tem muito V4, um ciclo, com tokens in/out zero, custo zero... vê se é poluição". Era poluição, sim: **42 dos últimos 100 eventos** eram linhas `v4_1_ciclo`/`v4_redator` com `modelo=desconhecido`, tokens 0/0, US$ 0 (199 dessas no mês inteiro). Nota: "zoom" não existe em nenhum ledger/página — leitura provável do Miguel da coluna "chamadas ×N" ou do valor "desconhecido" na coluna modelo.

**Causa raiz (o próprio fix do Adendo 6 veio com furo):** `_instrumentar_session` (criado 25/08 p/ furo §118) envelopa `Session.request` = **qualquer HTTP** do processo. Sem filtro, GETs de feeds/health e POSTs sem usage viravam registro zerado. O irmão `requests.post` de módulo TEM o filtro `if pt or ct` ("evita ruído de chamadas não-LLM") — o Session não tinha. Como o `v4_1_ciclo` (instrumentado 25/08 ~18h) é o fluxo mais HTTP-intenso, a tabela encheu de linhas V4 zeradas. **2º defeito na mesma função:** body via `data=` (string JSON) não era inspecionado → LLM REAL registrada como "desconhecido" (prova no ledger: POST 1040/949 tok, US$ 0,001989, chave "glm nyc", modelo desconhecido).

**Fix (2 pontas, ledger canônico INTACTO — append-only preservado):**
1. `/root/telemetria_api.py` (NYC, `.bak_filtro_session_20260825`): `_req_telemetrado` agora só registra com `pt/ct>0` (idêntico ao irmão) + corpo também via `kw.get("data")`; `_modelo_de_body` aceita str/bytes JSON (json.loads) → modelo volta a sair com nome certo.
2. `/root/flusher_ao_vivo.py` (NOVO, cron */1min substituiu o rsync cru; backup `backup_crontab_pre_filtro_aovivo_20260825`): manda pro tencent só eventos `custo>0 OU tokens>0` (cauda 5000) — GETs/POSTs não-LLM ficam fora do feed ao-vivo; 2º rsync (autoria_views_snapshots) preservado. Escolha deliberada filtrar NA FONTE (NYC) para não tocar `painel_cctv_v6.py` no tencent (sessão-irmã trabalhando no Mural Geral).

**Provas:** unit com servidor HTTP local no NYC — GET `{"ok":true}` NÃO gerou registro; POST com usage gerou 1 registro com `modelo=modelo-teste-x` extraído de `data=` string (custo calculado). Endpoint público `/v6/telemetria/v1/ultimos`: zerados **42→0**, janela 24h preservada (US$ 28,29, só saíram linhas $0), página `/v6/custos/ao-vivo` 200. Cron rodou (2 execuções no log); arquivo ao-vivo 5000 eventos / 0 zerados. Log do flusher honesto: lidos 12185, mantidos 11986 (**199 não-LLM fora**).

**Leitura correta do painel agora:** `v4_1_ciclo` que continua na tabela = LLM REAL (FC websearch/redação com tokens e custo >0). Transkriptor (custo 6.0, tokens 0) e fal-ai (0.035) permanecem — têm custo real.

**Estado:** ✅ poluição zerada na fonte e no feed · aguardando a "outra coisa" que o Miguel ia lembrar.
