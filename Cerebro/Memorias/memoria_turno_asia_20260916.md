# 🧠 MEMÓRIA TÉCNICA — TURNO DA ÁSIA: implantação no NYC (feixes+crons+escape+telemetria) — 16/09/2026

Irmã do fórum: `Foruns/forum_turno_asia_20260916.md`. Log técnico completo (comandos, provas, armadilhas).

## Arquitetura confirmada (mapeamento pré-implantação)

- Fábrica V4.1 = `/root/v4_labs/codigo/v41_ciclo.py` (NYC), 1.417→~1.475 linhas. `--vertical {nacional,economia,ciencia,geopolitica,...}`; lê `candidates` dos bancos `/root/agent_data/v4_verticals/*.sqlite3` (ciencia ⇒ `ciencia_tecnologia_ia.sqlite3` — o "bloco IA+ciência num bloco só" JÁ existia como vertical).
- Alimentação: crontab NYC → `coletor.py <sec>` (RSS/GoogleNews/Brave → `estoque_<sec>.json` com scoring LLM batch + extração trafilatura) → `v4_vertical_intake.py <alias>` (grava candidates no sqlite) → `v41_ciclo` (juiz deepseek → tese → redator → rascunho WP). Os comentários `# V4_DESLIGADO_20260824` nas linhas de cron são HISTÓRICOS — as linhas de coleta geo/tec/nacional estão VIVAS (logs 16/09 11:4x UTC; 2.639 "COLETOR v2 INICIADO" no log geo).
- Feixes diurnos: `coletor.py` `BRAVE_QUERIES` (inline) + `config_editorial.py` `RSS_FEEDS`/`GOOGLE_QUERIES` + `_NOVAS_FONTES`.

## Mudanças aplicadas (todas com backup `.bak_pre_turno_asia_20260916`)

1. `coletor.py`: `ASIA_NIGHT_FONTES` (geo 7 feeds vivos sondados: Yonhap EN/Diplomat/Taipei/ST-world/Nikkei/SCMP/Hindu-intl; tec 5: Nikkei/TechNode/SCMP/ST-biz/ChinaDaily), `ASIA_NIGHT_BRAVE` (âncoras TSMC/Samsung/SK Hynix/SoftBank/Alibaba/Tencent/ByteDance/Taiwan/Coreias/Índia-Pak/Mar do Sul/ASEAN/BRICS-SCO), `turno_asia_ativo()` (20:00–06:00 BRT só geo/tec), troca de feixes+força recoleta na janela, `collect_brave` noturno, `salvar_estoque(turno=...)`, escape `V4_SOMENTE_URGENCIA=1` (regex hard news pós `remove_accents`; filtra ANTES do LLM; sem urgência sai sem tocar estoque), blindagem do parser de `chaves.sh` (`_v.split("#",1)[0]`).
2. `v41_ciclo.py`: helpers `_turno_noturno/_ledger_turno/_titulo_urgente_nacional` no topo; `_ledger_turno` em TODOS os pontos de saída (freio, sem candidata, sem tese, recusado, juiz2, rascunho criado) → `/root/agent_data/v4_verticals/turno_asia_ledger.jsonl`; tag `turno` no JSON de status; guard `V4_SOMENTE_URGENCIA` no nacional (sai `nacional_noturno_sem_urgencia` antes do juiz).
3. crontab NYC: nacional `20 */6`→`20 9,12,18,21` UTC (BRT 6:20/9:20/15:20/18:20 — 9:20/15:20 preservados, 21:20→6:20 e 3:20→18:20); v41 geral `25 7,19`→`25 9,19` (BRT 6:25/15:25); fds nacional `50 9-22 * * 6,0` e `20 9-22 * * 6,0`; NOVO escape `20 23,5` com `V4_SOMENTE_URGENCIA=1` (BRT 20:20/02:20); NOVO rsync */15 do ledger → tencent `v6_data/`. ciencia `45 */2` e geopolitica `55 *` INTACTOS (já cobrem a noite).
4. tencent `painel_cctv_v6.py` (systemd `cctv-v6`, /home/ubuntu/cafezinho/v6/, porta 8084 atrás de nginx /v6/ + Basic Auth): endpoint `GET /api/turno-asia` (agregação por noite: ciclos/aceitos/recusados/por_status/taxa_aceitacao + últimos 15) — injetado com âncoras únicas, py_compile OK (SyntaxWarning pré-existente em `_AOVIVO_HTML` NÃO é meu), restart ativo, teste 200.

## Provas executadas

- Sonda feedparser no NYC: vivos = Yonhap 103, Diplomat 96, Taipei 51, ST-world 50, ST-biz 32, Nikkei 50, SCMP 50, TechNode 2000, Hindu-intl 60; mortos = Kyodo (todas URLs), Business Standard, Asahi AJW, Korea Herald (entram via Brave/GN).
- py_compile coletor+v41_ciclo OK; imports OK; bateria: turno_asia_ativo(pol)=False, chaves ASIA_NIGHT corretas, urgência 6 positivos (incl. "Avião cai em SP" — precisei ampliar regex com aviao cai/aeronave/apagão/blecaute/colapso) e 4 negativos OK.
- Endpoint painel: 200 `{"ok": true, "vivo": false, "eventos": 0, "msg": ...}`.
- crontab final: 4 guardas pause presentes; diff conferido linha a linha.

## Armadilhas encontradas (para a próxima sessão)

1. **Bug chaves.sh inline:** `export MAX_RSS_BIG_FEEDS=24  # coment` explodia `int()` no coletor quando rodado SEM source (parser fallback linhas 34-45 do coletor). Cura dupla: comentário movido p/ linha própria no chaves.sh (backup próprio) + parser blindado. Cron nunca sofreu (bash trata # como comentário: valor '24' limpo — provado com `bash -lc '. chaves.sh; print'`).
2. **Minha falha no 1º apply do crontab:** prefixo novo omitia `[ -f pause ]` → 4 linhas com `&& exit 0` solto (mortas). Detectado no diff pós-install; restaurado do backup e reaplicado em ~3 min (12:0x UTC, sem disparos na janela). LIÇÃO: diff de verificação DEPOIS do install é o que pega isso — e prefixo de substituição tem que incluir a guarda inteira.
3. dsn_publicador PARADO por contrato (só CL/CM publicam) — rascunhos v4.1 noturnos precisam da esteira da casa para virarem posts; a prova de amanhã mede os dois (rascunhos na janela + posts no ar) e reporta o gargalo se houver.
4. Painel v6 = 9.022 linhas; injeção por âncora única com assert count==1 é o caminho seguro; card gráfico do turno ficou como endpoint JSON (sprint futuro se o Miguel pedir).
5. de_zm.md da ponte ZM-DSC: repo parado em 03/09 × Cérebro local em 08/09 (bifurcação de canal meu; união completa pendente — registrei espelho da mensagem nos dois).

## Estado ao fechar (16/09 ~09:3x BRT)

Tudo implantado e testado; 1ª coleta nacional diurna nova dispara 12:20 UTC (9:20 BRT); 1º ciclo noturno Ásia: geo 20:55 BRT, tec 20:45 BRT (23:45/23:55 UTC hmm: tec `45 */2` dispara 0,2,...,22 UTC — primeira na janela = 23:45 UTC = 20:45 BRT; geo `55 *` = 23:55 UTC = 20:55 BRT). Escape nacional: 20:20 e 02:20 BRT. Consolidação: automation ZM 06:35 → ponte + Telegram.

— ZCode/GLM-5.3 (ZM, Dell) · 16/09/2026
