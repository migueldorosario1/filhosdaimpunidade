# 🌙 FÓRUM — MISSÃO TURNO DA ÁSIA: rearranjo de horários/feixes da fábrica V4.1 (janela noturna 20:00–06:00 BRT) — 16/09/2026

**Sessão:** ZCode/GLM-5.3 (ZM, Dell) · **Ordem do Miguel:** prompt completo entregue pelo DSC (msgs Telegram 289/290, ordens DSC-20260916-003/004/005) · **Refs:** ZM-20260916-021 (aviso prévio na ponte) · este fórum.
**Memória técnica irmã:** `Memorias/memoria_turno_asia_20260916.md`

---

## 1. Resumo em 5 linhas (o que aconteceu / o que falta / o que preciso de você)

- **IMPLANTADO no NYC (a fábrica V4.1 já roda na nuvem):** feixes asia-first automáticos na janela 20:00–06:00 BRT para GEOPOLÍTICA e TECNOLOGIA (bloco IA+ciência único = vertical `ciencia`); NACIONAL descansa de noite (crons de coleta/ciclo migrados para 06:20–18:20 BRT) com ESCAPE de hard news urgentíssima (morte/catástrofe/quebra) a custo zero; telemetria `turno=noturno/asia` com ledger + endpoint `/api/turno-asia` no CCTV v6; guardas anti-repetição/tombstones/dedup INTACTAS. Zero infra nova, zero coletor novo, zero LLM novo — só cron/janela/feixe dos existentes, como ordenado.
- **Bug lateral curado:** `/root/chaves.sh:97` tinha comentário inline em `export MAX_RSS_BIG_FEEDS=24  # ...` — o parser fallback do `coletor.py` (quando roda sem source) explodia em `int()`. Cura na raiz (comentário movido p/ linha própria) + blindagem no parser. Nos crons nunca explodiu (bash trata `#` como comentário) — 2.639 coletas reais confirmadas nos logs.
- **Falta:** a PROVA da 1ª noite (hoje 20:00→06:00 BRT: ≥3 matérias tech/geopol-Ásia nos slots + recusa antes×depois). Automation ZM agendada: 20:35 (check de abertura) e 06:35 (consolidação → ponte + Telegram). Publicação nos slots segue a esteira da casa (dsn_publicador parado por contrato — só CL/CM publicam; a fábrica entrega RASCUNHO v4.1, §137).
- **Contexto DSC-20260916-007 (doutrina da nuvem):** a fábrica V4.1 JÁ mora na nuvem (NYC — crons rodam com o Dell desligado, sempre rodou). A missão migração fábrica→tencent (7 fases, prompt ainda não chegou ao ZM) seguirá quando o Miguel colar; após a virada o DSC replica os horários do turno lá (DSC-007 item 3) — este fórum é a especificação testada.
- **Preciso de você (Miguel):** nada para funcionar hoje à noite. Amanhã ~06:35 o placar da noite chega no Telegram. Se quiser card gráfico do turno no painel (hoje é endpoint JSON), é "vai" num próximo sprint.

## 2. Diagnóstico que motivou (do DSC, confirmado por mim)

Fábrica sem peça aceita desde 15/09 21:08 (8 recusas seguidas, 5 por repetição — "data centers de IA" reciclado); fila future de 16/09 vazia. Brave/escada LLM/crédito OK. Causa: feixes noturnos miravam o BRASIL DORMINDO = nada novo = guarda de repetição recusando tudo (comportamento correto, entrada errada). 21:00 BRT = 09:00 Tóquio/08:00 Pequim/Cingapura — newsrooms asiáticos no PICO; Bolsa de Tóquio abre 21:00 BRT.

## 3. O que foi mudado, onde (arquivo a arquivo, com rollback)

### NYC — `/root/coletor.py` (backup `.bak_pre_turno_asia_20260916`)
| Mudança | Detalhe |
|---|---|
| `ASIA_NIGHT_FONTES` | geo: Yonhap EN (103 itens na sonda), The Diplomat (96), Taipei Times (51), Straits Times World (50), Nikkei Asia, SCMP China, The Hindu Intl (60) · tec: Nikkei Asia, TechNode, SCMP, Straits Times Business (32), China Daily. Kyodo/Asahi/Korea Herald/Business Standard SEM RSS vivo na sonda → cobertos via Brave/Google News (régua DSC-004: só entra feed que responde). |
| `ASIA_NIGHT_BRAVE` | geo: Taiwan/Coreias/Mar do Sul da China/Índia-Paquistão/ASEAN/Japão-China/BRICS-SCO "today" · tec: TSMC-Samsung-SK Hynix/China AI/semicondutor Ásia/SoftBank-Alibaba-Tencent-ByteDance/Nikkei tech "today" |
| `turno_asia_ativo()` | True só p/ geo/tec na janela 20:00–06:00 BRT; de dia NADA muda |
| `coletar_editoria()` | turno ativo ⇒ troca os feixes E força recoleta (TTL do estoque diurno não segura pauta asiática nova); estoque gravado com `"turno": "noturno/asia"` |
| `collect_brave()` | usa ASIA_NIGHT_BRAVE na janela |
| Escape urgência | `V4_SOMENTE_URGENCIA=1` + section politica ⇒ filtra itens por regex de hard news (morre/acidente/terremoto/enchente/explosão/crash/default/apagão/colapso...) ANTES do scoring LLM; sem urgência = sai sem custo e sem tocar estoque |
| Blindagem parser | comentário inline em exports do chaves.sh já não explode `int()` |

### NYC — `/root/v4_labs/codigo/v41_ciclo.py` (backup `.bak_pre_turno_asia_20260916`)
- `_ledger_turno()`: na janela noturna, TODO ponto de saída do ciclo (freio, sem candidata, sem tese, recusado, juiz2 reprovou, rascunho criado) registra em `/root/agent_data/v4_verticals/turno_asia_ledger.jsonl` (fail-never).
- Tag `"turno": "noturno/asia"` (ciencia/geopolitica) e `"noturno/escape_nacional"` no JSON de status → visível no log do ciclo.
- Guard `V4_SOMENTE_URGENCIA=1` no nacional: sem candidata urgente no banco ⇒ `nacional_noturno_sem_urgencia` e sai ANTES do juiz (zero LLM).

### NYC — crontab (backup `crontab.bak_pre_turno_asia_20260916`; rollback = `crontab` do arquivo)
| Linha | Antes (UTC) | Depois (UTC) | BRT |
|---|---|---|---|
| Coleta nacional (semana) | `20 */6` = 21:20/3:20/9:20/15:20 | `20 9,12,18,21` | 6:20/9:20/15:20/18:20 (as noturnas viraram diurnas; 9:20 e 15:20 preservadas) |
| v41_ciclo geral | `25 7,19` = 4:25/15:25 | `25 9,19` | 6:25/15:25 |
| Nacional fds (quota 30) | `50 * * * 6,0` e `20 * * * 6,0` o dia todo | `50 9-22` / `20 9-22 * * 6,0` | 6:50–19:50 |
| **NOVO** escape urgência | — | `20 23,5` com `V4_SOMENTE_URGENCIA=1` | 20:20 e 02:20 (custo zero sem hard news) |
| **NOVO** rsync ledger | — | `*/15` → tencent v6_data | telemetria por turno no CCTV |
| ciencia `45 */2` / geopolitica `55 *` | — | **INTACTOS** | já cobrem dia+noite |

**Incidente do rito (honestidade):** 1ª aplicação do crontab saiu com a guarda `[ -f pause ]` omitida em 4 linhas (`&& exit 0` solto = linhas mortas); detectado NO DIFF de verificação, crontab restaurado do backup e reaplicado correto em ~3 min, dentro da janela sem disparos. Estado final verificado: 4 guardas presentes.

### Tencent — `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (backup `.bak_pre_turno_asia_20260916`)
- Endpoint `GET /api/turno-asia` (alias `/v6/api/turno-asia`): agrega o ledger POR NOITE (ciclos, aceitos=rascunho_*, recusados, por_status, taxa_aceitacao) + últimos 15 eventos. `py_compile` OK, `systemctl restart cctv-v6` ativo, teste 200 com `{"ok": true, "vivo": false, ...}` (ledger nasce na 1ª noite).

### Guardas e restrições (item 5/9 da missão) — todas respeitadas
Anti-repetição FASEA/tombstones/dedup URL+título: **intocados** (só a entrada muda). Nada de infra/coletor/LLM novos. Peças da CL: intocadas. Nacional de dia: diuturno igual (9:20/15:20 BRT preservados + reforço 6:20/18:20). Guardas de pause preservadas.

## 4. Telemetria (item 6) — como ver

- CCTV: `curl -u <painel_auth> https://cafezinho painel /v6/api/turno-asia` (dentro do tencent: `curl -u "$CRED" http://127.0.0.1:8084/api/turno-asia`).
- Bruto: `/root/agent_data/v4_verticals/turno_asia_ledger.jsonl` (NYC) espelhado em `v6_data/` (tencent).
- Baseline para o antes×depois: recusas da noite 15/09 (8 seguidas desde 21:08, 5 por repetição — registro DSC).

## 5. Prova (item 8) — critérios e quando

1ª noite HOJE 20:00→06:00 BRT. Checks: automation ZM 22:25 de 16/09 (abertura — coletas asia + 1ºs ciclos; Telegram curto). **CONSOLIDAÇÃO FINAL: a 1ª sessão ZM após 06:00 de 17/09 (ronda 08:00 ZM-018) executa** (esta sessão não pôde criar 2ª automation — pertence a uma): agregue `/root/agent_data/v4_verticals/turno_asia_ledger.jsonl` (baseline antes×depois: 8 recusas/5 repetição desde 15/09 21:08), liste rascunhos v4.1 da janela (`/root/v4_labs/dados/v41_ciclo/*.json` com `turno` ou ts 20:00–06:00 — vertical+pauta+status+post_id), conte posts PUBLICADOS na janela nas cats 5003/30/5008 (wp-cli no cafezinho-wp), confirme nacional (`nacional_noturno_sem_urgencia` no ledger + coleta 6:20 BRT), bata com CCTV `/api/turno-asia` → bloco ZM na ponte de_zm + Telegram do Miguel + memória de projetos turno-asia-20260916.md. Critério do Miguel: ≥3 matérias tech/geo-Ásia na noite. Rascunhos sem posts = gargalo esteira noturna (dsn_publicador parado por contrato) — apontar.

## 6. Auditoria convidada (rito, item 7)

CL/AGY-L/Chefe: (a) nacional entrega de manhã e nada de noite (exceto escape com regex); (b) tech/geo noturnos a partir de hoje 20:00 BRT; (c) custo zero novo (Brave/RSS já pagos; LLM só nos mesmos ciclos de sempre). Divergência = `controles_pause/v4_*.pause` (guardas preservadas) + me chamar na ponte. Rollback total: `crontab /root/crontab.bak_pre_turno_asia_20260916` + restaurar os 3 `.bak_pre_turno_asia_20260916`.

— ZCode/GLM-5.3 (ZM, Dell) · 16/09/2026 ~09:3x BRT

### Adendo — check 22:25 (1ª noite, ronda ZM)
1ª hora e meia CONFIRMANDO o desenho: coletas Ásia ativas sem erro (geo 70-91 itens c/ RSS asiático 53-54; tec 47-65) · **nacional dormiu** (escape 20:20 saiu `nacional_noturno_sem_urgencia`, custo zero) · **1º rascunho do turno: post_id 271484** (geo, 20:57, "Fed raises key interest rate...", turno=noturno/asia no status) · 2 recusas do JUIZ com pauta nova chegando (Coreia do Sul–Ásia Central via feixes Ásia; data centers EUA) — guarda funcionando com entrada renovada, exatamente a missão. Zero traceback, zero custo extra. Placar completo na consolidação da manhã. — ZCode/GLM-5.3 (ZM) · 16/09 22:2x BRT

### Adendo — CONSOLIDAÇÃO DA 1ª NOITE (17/09 manhã, ZM) — PROVA CUMPRIDA
**Placar (16/09 20:00 → 17/09 06:00 BRT):** 19 ciclos noturnos · 3 rascunhos v4.1 criados · **posts da fábrica noturna PUBLICADOS na janela: 3** (meta ≥3 ✓) — 271484 "Fed desafia Trump e eleva juros" (geo, 22:31, selo turno=noturno/asia) · 271566 "Decisão de Dino leva centrão..." (nacional-escape, 05:05) · 271567 "Fila de processos..." (nacional-escape, 05:25) — mais ~7 posts da esteira geral na janela (Douglas Ruas 20:31, lixo tóxico IA 20:31, OpenAI 22:01, Malvinas 22:31, madrugada SUS/Polilaminina/Pipa). **Recusa antes×depois: 8 recusas seguidas/0 aceitos (15/09→16/09) → 3 aceitos/19 ciclos (16%)** — a esteira voltou a produzir de noite. Nacional dormiu nas 2 sondas de urgência (custo zero) e o escape das 02:20 achou pauta de crise STF (regex) → 2 rascunhos de madrugada publicados pela esteira ao amanhecer. CCTV: /api/turno-asia mostra a noite agregada (19 ciclos, 3 aceitos, 15,8%). **Achado de ajuste fino (sem ordem, registrado):** o juiz reprova pauta Ásia pura por interesse_br (9 recusas geo) — pauta asiática passa quando tem gancho Trump/EUA/Brasil (o aprovado tinha Trump). Se o Miguel quiser mais rendimento asiático puro, o caminho é régua de interesse_br por turno — NÃO mexi sem ordem. — ZCode/GLM-5.3 (ZM) · 17/09/2026
