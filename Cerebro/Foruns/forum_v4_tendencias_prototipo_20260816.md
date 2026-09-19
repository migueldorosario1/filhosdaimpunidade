# 📈 FÓRUM — PROJETO V4 "TENDÊNCIAS" (protótipo de pipeline focado em audiência)

**Origem:** ordem do Miguel, 16/08 ~08:58 — "um novo V4, um bloco novo no Cafezinho chamado Tendências; protótipo baseado em audiência/tendências, pipeline inteiramente focado em audiência, com relatórios diários ou de hora em hora do agente de performance; pode ser o carro-chefe; JÁ FIZEMOS ALGO PARECIDO ANTES E DESLIZOU PARA O SENSACIONALISTA — muito cuidado."
**Autor:** ZCode (GLM-5.3) · **Status:** 🟢 **GATE 0 APROVADO pelo Miguel (16/08 ~09:30 BRT)** — P0 em execução (radar; sem produção de posts)

**📌 NOTA DE FLUXO (ordem do Miguel, 16/08 ~09:30):** o vertical Tendências **não publica direto** — entra como **rascunho** e sobe para publish **pelos loops Miguel e Laura** (fluxo de revisão editorial dos loops; publish nunca pelo worker nem direto). Esta regra substitui/complementa o "publish só via Claude" onde os dois se sobrepuserem: o ponto final de publish é o loop.

**📌 NOTA PAINEL (ordem Miguel 16/08 ~09:30):** nada de dia parcial no painel — a série exibida termina no último dia FECHADO. Aplicado (patch 2, backup `.bak_pre_sem_dia_parcial_20260816_0931`).
**Contexto-base:** `forum_cafezinho_analise_posts_3semanas_20260815.md` (raio-X de audiência) · `forum_plano_diretrizes_v4_audiencia_20260815.md` (plano prudente geral)

---

## 1. O que já existia (garimpo — e por que sensacionalizou)

**Acervo encontrado:** `agente_fantastico.py` (NYC+Tencent), `agente_master_trends_v9_legacy.py`, `agente_analytics_v9.py`, `diretriz_trends.json` / `diretriz_news_trend.json`, `banco_artigos_brutos_trends.json`, `fantastico_semantic_history.jsonl` (Tencent `/root/` + NYC `/root/`).

**O DNA do erro:** a `diretriz_trends.json` pautava pelo **"Triângulo de Ouro"** escolhido a priori — (1) tecnologia com rivalidade oculta, (2) **"AMEAÇA E ESCATOLOGIA CLIMÁTICA/GEOLÓGICA"** ("oceanos evaporando, cidades que vão afundar"), (3) Brasil épico na nova ordem — com ordem explícita de **"criar senso de urgência focado em fatos extremos"**. O `ESTILO_FANTASTICO` pedia "tom instigante, misterioso". Ou seja: o interesse era **inventado** (aparato: medo/maravilha/extremo), nunca **medido**. Resultado conhecido: sensacionalismo → agentes desativados (fantastico sobrescreveu; sobrenatural desativado 18/06; trends zumbi removido do maestro 22/06).

**A diferença essencial do novo protótipo:** a pauta nasce do **interesse medido** (o que a audiência real está clicando/buscando AGORA no GA4, GSC web e Discover), nunca de aparato presumido. E a camada de guardiões é o coração do projeto, não um acessório.

**Achado operacional:** o `agente_performance.py` existe (gera `performance_weights.json`), mas **está sem cron desde antes de julho** (`performance_weights.json` parado em 01/07). O "relatório de hora em hora" precisa ser criado/reativado — é a peça central do radar.

## 2. Acesso confirmado às fontes (tudo já testado nesta sessão)

| Fonte | Acesso | Como |
|---|---|---|
| GA4 (audiência/páginas/tempo) | ✅ | API, property 374552425, `/root/keys/ga4.json` (Tencent) |
| Google Search Web (queries/páginas/posição) | ✅ | API GSC, `sc-domain:ocafezinho.com`, chave em `/root/cafezinho/dados_agentes/indexing_key.json` |
| Google Discover | ✅ | mesma API, `type=discover` (só dims page/date) |
| Painel CCTV V6 | ✅ | série GA4 com cache 30min (corrigido hoje) |
| Agente de performance | ⚠️ existe mas SEM cron | reativar + estender (ver P0) |

## 3. Arquitetura do protótipo (4 peças)

### 📡 Peça 1 — RADAR (`agente_radar_tendencias.py`, NYC, cron */30min)
Coleta leve e contínua, alimentando `radar_atual.json` + histórico `radar_YYYYMMDD_HH.json`:
- **GA4 intradiário:** top páginas/views 1h e 24h (o que está explodindo agora), tempo de leitura por post, canais.
- **GSC web:** queries com impressões subindo vs mediana (demanda emergente), páginas ganhando posição.
- **GSC Discover:** páginas entrando no feed (sinal precoce de viral).
- **Sinais próprios:** `performance_weights.json` reativado (pesos por tema), coorte de publicações (painel V6 já tem).
- **Anti-ruído:** só promove tema a "quente" com ≥2 sinais independentes ou pico ≥3× a mediana móvel — evita caçar variação aleatória.

### 🧭 Peça 2 — CURADORIA DINÂMICA (`diretriz_tendencias.json`, versionada no repo)
A diretriz é **regenerada do radar** (diário 06h + ajuste intradiário só para sinais fortes), traduzindo interesse medido → ângulos permitidos e vetados. É aqui que moram as **regras duras anti-sensacionalismo** (abaixo). Toda regeneração gera diff datado (auditoria: o que mudou e por quê — evidência anexada).

### ✍️ Peça 3 — PRODUÇÃO (`v4_vertical_tendencias`, runtime canônico)
Novo vertical herdando `v4_vertical_redactor_runtime` (mesmo worker, mesma disciplina draft-only; publish continua exclusivo do Claude). Prompt-template específico de tendência + gate de título (verbo + nome próprio, da análise) + **revisor anti-tabloide** antes de gravar o draft.

### 🏠 Peça 4 — DISTRIBUIÇÃO (bloco "Tendências" na home)
Categoria WP nova `Tendências` + bloco no `front-page.php` via `category__in` (mesmo padrão dos blocos existentes; histórico-toggle continua ÚLTIMO — regra de 14/08). **Só na P2**, depois do Miguel ver os posts.

## 4. 🛡️ Guardiões anti-sensacionalismo (a lição do passado — regras duras)

**PROIBIDO (rejeita o texto):** urgência fabricada; escatologia como isca ("cidade vai afundar" sem dado); número sem fonte no 1º parágrafo; adjetivos vazios ("chocante", "impressionante", "absurdo"); pergunta-gancho não respondida; capitalização de medo ("VOCÊ precisa saber"); entidade errada/contexto forçado.
**OBRIGATÓRIO:** título sustentado por fato do texto; superlativo só com número + fonte; tom de notícia com serviço ("o que muda para você").
**Gate técnico:** lista léxica de tabloide (auto-rejeita) + checagem de 1 número central do título contra o corpo + conformidade verbo+nome próprio.
**Veto humano inalterado:** draft/pending; publish só via Claude.

## 5. Cadência e métricas do piloto (congeladas)

- Radar: */30min · Diretriz: 06h diária (+intraday só picos) · Produção piloto: 2–3 posts/dia.
- **Sucesso (14 dias):** decolagem do vertical ≥ 2× baseline V4 (2%→4% posts >500 views) · v/post ≥ 2× mediana do site (25→50) · tempo de leitura ≥ mediana V4 (47s) · zero rollback editorial · zero flag do revisor passando batido.
- **Kill switch:** `diretriz_tendencias.json` com `enabled:false` desliga o vertical sem tocar em mais nada.

## 6. Fases com gates

| Fase | O quê | Duração | Gate |
|---|---|---|---|
| **P0** | Reativar `agente_performance` (cron) + subir o RADAR (só coleta, sem produção); painel já fornece série 30min | 2d | Miguel vê o `radar_atual.json` |
| **P1** | Vertical Tendências produzindo 2–3 posts/dia **draft-only** (sem bloco na home; aparecem na Linha do Tempo/categoria) | 7d | Miguel lê os posts e aprova qualidade |
| **P2** | Bloco "Tendências" na home + medição do bloco (CTR, coorte) | 14d | Miguel decide com números |
| **P3** | Promoção a carro-chefe OU ajuste OU encerramento documentado | — | Miguel |

**Anti-canhibalismo:** dedupe por entidade/título contra as verticais hard-news ativas (o V4 já tem dedupe interno — estender o cruzamento). Tendências cobre o que está emergindo; Nacional/Geopolítica seguem donas do ciclo duro.

## 7. Estado

- **O que aconteceu:** painel corrigido (cache 30min + MM7 sem dia parcial — o "-12% fixo" era o dia corrente parcial na média); protótipo antigo garimpado e lição extraída; projeto desenhado ancorado no runtime real.
- **O que falta:** Gate 0 do Miguel → P0 (radar ligando).
- **O que preciso do Miguel:** aprovar o projeto/fases e confirmar o nome ("Tendências" — categoria e vertical).

---

## 8. ADENDO 17/08 (~01:05–02:00) — ESCOPO NOVO (ordem Miguel ~01:20): produção e publicação 100% no ESPELHO

> O plano do §6/§7 foi substituído por ordem de voz do Miguel (~01:20): **terminar a vertical e produzir/publicar SÓ no espelho cafezinho.news** (não no canônico); criar bloco na home do espelho; basear a diretriz na **fórmula de sucesso da Baleia Extraordinária de 15/08** (trabalhar os mesmos assuntos dos 10 posts mais lidos); **autoaprendizado persistente** ("tem que guardar sempre, tem que manter"); depois será portada ao canônico (aí sim indexada). O espelho **tem que continuar fora do radar do Google** ("não pode dividir o SEO do canônico").

### 8.1 Segurança do espelho (verificada ANTES de produzir)

- Sync `sync_from_cafezinho.sh` (cron `17 * * * *`) é **unidirecional canônico→espelho** e nunca deleta posts locais → posts Tendências locais sobrevivem às sincronizações.
- **Noindex triplo reconfirmado na prática** (1º post publicado): `robots.txt` com `Disallow: /` + `<meta name="robots" content="noindex, nofollow">` na página + mu-plugins blindados. SEO do canônico intacto.
- Creds `ESPELHO_WP_SITE/USER/PASS` presentes no `/root/chaves.sh` do NYC (valores nunca expostos — Regra 4).

### 8.2 Peça 2 — Diretriz viva + autoaprendizado (ENTREGUE)

- `diretriz_tendencias.json` **v1** (`enabled: true`, `escopo: "espelho"`): fórmula de sucesso da Baleia embutida (9 itens: verbo+nome próprio 9×, ≤250 palavras=Discover/800+=fidelização, janelas 06h/09h/10h, sábado 2,5×, ângulo eleitoral até 25/10, geopolítica motor 58%, análise com tese, velocímetro KPI, mediana 25), regras duras anti-sensacionalismo, 10 temas com palavras-chave, kill switch. Backup da v0: `diretriz_tendencias.json.bak_v0_20260816`.
- **Regenerador diário** `/root/regenera_diretriz_tendencias.py` (Tencent, cron `5 6 * * *`): consolida snapshots 24h do radar → top-10 por views + temas persistentes; **nunca mexe em enabled/escopo**; versões em `diretriz_hist/` (30) + diff datado em `diretriz_HISTORICO.md`; modo `--intraday` só registra picos ≥4 fontes.
- **Endpoint novo no painel:** `GET /v6/api/tendencias/pautas` (função `api_tendencias_pautas` no `painel_cctv_v6.py`, backup `.bak_pre_api_tendencias_20260817`) — serve diretriz + top-10/temas quentes do radar p/ o intake no NYC. Testado: `top10=10 temas=7 formula=9` (nº1: lei-rouanet 1157 views).

### 8.3 Peça 3 — Produção publicando direto no espelho (ENTREGUE, no ar)

- **Intake** `/root/v4_tendencias_intake.py` (NYC, cron `*/30` com flock): lê o endpoint do radar (3 tentativas + cache local de fallback), dá match de candidatas **REAIS dos estoques V4** (varre todos os sqlite3 de `/root/agent_data/v4_verticals/`) pelos `temas_palavras` + tokens dos slugs do top-10; anti-canibalismo (pula item_key já draftado em qualquer vertical + idade mínima 2h); insere em `tendencias.sqlite3` com `raw_json.v4_tendencias` (tema/top_path que casou, db de origem). **Autoaprendizado:** `tendencias_aprendizado.json` (rolling 400 ciclos + agregados de presença por tema/path). 1ª rodada real: **fila 173 candidatas** (189 matched, 2 puladas por já draftadas, 13 jovens).
- **Worker** `/root/v4_vertical_draft_worker.py` — vertical nova `tendencias` (backup `.bak_pre_tendencias_espelho_20260817`): CONFIG com `apenas_espelho: True` e categoria **100003**; **fail-closed** (sem creds do espelho → aborta, nunca cai no canônico); kill switch da diretriz desliga sem publicar; briefing com a fórmula de sucesso + PROIBIDOS/OBRIGATÓRIOS + contexto de tendência injetado (uso interno — o texto nunca menciona radar/audiência); **gate léxico anti-tabloide** antes de publicar; **publish direto no espelho** (canônico segue exclusividade dos loops).
- **Política de imagem:** SÓ foto real (os 6 estágios herdados). IA continua vetada fora de geopolitica/ciencia (**Emenda 1 do Contrato v1.0**). Se nenhuma foto real for achada: **publica SEM imagem com isenção documentada** (precedente V4_DESTRAVA_20260813).
- **Descoberta importante:** o mu-plugin `cafezinho-gate-imagem-checada.php` (fail-close de 16/08, incidente 266029) reverte QUALQUER publish sem meta de checagem — inclusive via wp-cli e REST. Solução: o worker grava `_cafezinho_img_check` (foto auditada no pipeline) ou `_cafezinho_img_isenta` (sem imagem, motivo documentado) numa **1ª chamada REST e publica na 2ª** (o filtro `rest_pre_insert_post` lê a meta já gravada). Serve de alerta p/ os 3 V4s novos do espelho (sessão paralela 01:14–01:50) quando forem publicar.
- **Espelho:** categoria Tendências criada (**term_id 100003**, slug tendencias) + **bloco Tendências na home** (`front-page.php`, modelo do bloco Vídeos, `category__in => array(100003)`; backup `.bak_pre_bloco_tendencias_20260817`; `php -l` OK; renderiza 1 destaque + 4 itens). Nota de coordenação: a sessão paralela dos 3 V4s novos também editou o front-page.php na mesma janela (backup deles `/root/backup_front_page_pre_blocos_novos_20260817.php`) — os dois conjuntos de blocos coexistem, verificado no ar.
- **Crons NYC:** intake `*/30` + worker `40 7,13,19 * * *` (BRT) com flock (backup `/root/crontab.bak_pre_tendencias_20260817`).

### 8.4 Prova (1º post publicado)

- **400077** "Itamar Ben-Gvir defende matar até 40 pessoas por noite em Gaza" — `status=publish`, categoria 100003, exibido no bloco Tendências da home, página do post com meta `noindex, nofollow` confirmada. Fonte RT-ES; nenhuma foto real achada nos 6 estágios → publicado sem imagem com isenção documentada (fluxo novo).
- **400079** "Israel Katz promete novos ataques ao Hezbollah após mortes no Líbano" — **ciclo 100% autônomo validado (~02:00):** o worker selecionou a candidata, redigiu, achou foto REAL (`busca_ativa_foto_real`), gravou `_cafezinho_img_check {ok:true, image_kind:real}` na 1ª chamada REST, publicou na 2ª (passou no GATE-IMG), categoria 100003, no ar na home. `https://cafezinho.news/2026/08/17/israel-katz-promete-novos-ataques-ao-hezbollah-apos-mortes-no-libano/`

### 8.5 Estado (substitui o §7)

- **O que aconteceu:** vertical completa NO AR produzindo e publicando SOZINHA no espelho: radar → diretriz viva → intake → redação (fórmula Baleia) → publish, com bloco na home e autoaprendizado gravando em 2 camadas (NYC + Tencent).
- **O que falta:** Gate P1 = **Miguel testar o espelho** (https://cafezinho.news → bloco Tendências); ajustar tom/volume conforme feedback; portar ao canônico quando o Miguel mandar (aí com indexação + publish via loops).
- **O que preciso do Miguel:** olhar o espelho e dizer se o tom/volume está bom.
- **Kill switch:** `diretriz_tendencias.json` → `enabled:false` (intake e worker param na hora) OU remover os 2 crons do NYC. Nada é apagado.

---

## 9. ADENDO 17/08 ~18:30 BRT — ARQUITETURA V2 (ordem Miguel ~18:00): sem bloco próprio, distribui por editoria + abertura à novidade

> Ideia do Miguel ("tive uma ideia boa agora"): o Tendências não precisa de bloco
> próprio — ele produz as matérias com mais visibilidade, com foco em audiência, e
> **distribui para os blocos correspondentes** pela categoria (geopolítica→bloco
> Geopolítica, política nacional→bloco Nacional, cultura→Cultura, tecnologia→
> Tecnologia). E o papel dele ficou claro: **"um V4 que apure o que está estourando
> agora... no Brasil e no mundo"** — com sensibilidade ao momento presente. Também
> aprovou as ideias de abertura à novidade (cota de exploração + queries novas +
> medição por sinal).

### 9.1 O que mudou (peças entregues)

1. **Diretriz v2** (Tencent, backup `.bak_pre_v2_20260817`): `bloco_proprio: false` + `mapeamento_categorias` (15 entradas tema→categoria do ESPELHO: lula/flávio/eleições/stf→22 Política-Nacional; ceará→4986 Regional; economia→43; irã/china/eua/rússia→5003 Geopolítica; cultura→79; tecnologia→30; esporte→1271; saúde→258; meio ambiente→582; fallback 22) + `cota_exploracao` (1 exploração/rodada máx 3/dia) + `fonte_de_pauta` reescrita ("o que está estourando AGORA, BR e mundo").
2. **Radar v2** (Tencent, backup `.bak_pre_v2_20260817`): novo sinal `gsc_queries_novas` — queries do GSC que apareceram pela PRIMEIRA VEZ na semana (impressões ≥100, top 15) = demanda nova pura (novidade). Rodada manual OK: 15 queries novas, 0 erros.
3. **Painel v2**: o endpoint `/v6/api/tendencias/pautas` tinha sido PERDIDO por edição concorrente do painel (17/08, sessões paralelas — 404 desde ~02:00, intake em cache). Reaplicado em v2 (função + rota, backup `.bak_pre_api_tendencias_v2_20260817`, serviço reiniciado): agora serve mapeamento, cota e queries novas.
4. **Intake v2** (NYC): grava `categoria_sugerida` (tema→mapa; top10/exploração→heurística por palavras) + `sinal` de origem (tema/top10/gsc_emergente/exploracao) em cada candidata; **cota de exploração** (tema frio com query nova OU score ≥8); aprendizado conta `exploracoes_dia`. **Fix de falsos positivos:** palavras curtas (≤4 chars) agora casam por token exato — "ira" não casa mais dentro de "atira" (caso real: pauta policial classificada como Irã); "tse"/"candidato" na heurística de Política.
5. **Worker v2** (NYC, deployado): para a vertical tendencias, a categoria do post vem da candidata (`raw_json.v4_tendencias.categoria_sugerida`) — fallback 22 (Nacional). CONFIG `category_ids` = [22]. Mantém: apenas_espelho fail-closed, kill switch, gate anti-tabloide, guard de source_url, publish direto no espelho.
6. **Espelho**: bloco Tendências REMOVIDO da home (backup `.bak_pre_remove_bloco_tendencias_20260817`, php -l OK); posts 400077/400079 recategorizados para Geopolítica (5003) — já aparecem no bloco Geopolítica. Categoria 100003 fica existindo (histórico), sem bloco.

### 9.2 Estado

- **O que aconteceu:** reformulação completa aplicada — o Tendências agora é o caçador de audiência que distribui pelas editorias, com exploração de novidade e medição por sinal. Teste E2E do worker em curso no fechamento deste adendo.
- **O que falta:** validar o 1º post v2 (categoria temática + capa OK no bloco correspondente); observar ~2 dias; depois decidir cadência/portar ao canônico (aí com as categorias do canônico e indexação).
- **O que preciso do Miguel:** nada agora — olhar o espelho amanhã e ver as matérias caindo nos blocos certos.

### 9.3 Resultado do teste E2E + incidente da categoria fantasma (17/08 ~19:00 BRT)

- **Teste E2E v2 COMPLETO:** o worker pegou uma candidata da fila, redigiu e publicou o post **400108** ("Chanceler do Chile inicia viagem à China, ao Vietnã e ao Japão") no espelho. Sem foto real nos 6 estágios → publicou sem imagem (isenção documentada, como desenhado) e a caçada manual resolveu: retrato oficial de Alberto van Klaveren (Commons CC BY 2.0, Tribunal Visual APROVOU, media 400110, `_cafezinho_img_check` ok). **O post é o HERO do bloco Geopolítica com a capa renderizada** — distribuição por editoria funcionando de ponta a ponta.
- **Backfill:** 223 candidatas antigas da fila (v1, sem categoria) receberam `categoria_sugerida` via re-rodagem da lógica v2 — daqui em diante o worker publica na editoria certa sozinho.
- **⚡ INCIDENTE RESOLVIDO — categoria fantasma "5003" no espelho:** existia uma categoria corrompida (term_id 100004, name="5003", slug="5003", com os 3 posts Tendências dentro) — criada por engano por alguma automação; meus comandos `wp post term set ... 5003` resolveram pelo SLUG (caiam na fantasma) em vez da Geopolítica real (term_id 5003). Por isso os posts não apareciam no bloco Geopolítica. **Correção:** 3 posts movidos para a 5003 real via `wp eval` (IDs numéricos), categoria fantasma DELETADA (estava vazia). **Lição permanente:** em wp-cli, categoria com nome/slug numérico é armadilha — usar `wp eval` com IDs ou conferir `term list` depois do `term set`.
- **Anti-duplicata validado:** a primeira pauta processada no ciclo v2 (Ben-Gvir) foi bloqueada por duplicata contra o post já publicado — o guard funciona.
- **Guards de imagem validados:** `V4_MEDIA_SOURCE_URL_GUARD` (aborta capa fantasma) e o fluxo sem-imagem→isenção→caçadora completam o ciclo de imagem do espelho.

---

## 10. ADENDO 18/08 ~22:40 BRT — RAIO-X da produção no espelho (pergunta do Miguel) + BUG: cron do worker quebrado

**Publicados no espelho nas últimas 48h (produção local dos V4 novos, IDs 400xxx — 7 posts):**
- **Tendências:** 400077 (Ben-Gvir/Gaza, 17/08 01:48), 400079 (Israel Katz/Hezbollah, 17/08 02:01), 400108 (Chanceler do Chile → China/Vietnã/Japão, 17/08 18:28 — teste E2E v2, virou HERO do bloco Geopolítica).
- **Ficção:** 400075/400091 (Vila Clara caps 1-2, 17/08 09:20), 400111/400114 (Singularidade caps 1-2, 17/08 18:54).
- Restante do espelho no período (~59 posts IDs 266xxx) = espelho do canônico via sync unidirecional, não é produção dos V4 novos.

**Rascunhos de hoje (18/08, aguardam os loops publicarem):** 400117 Religião "Moisés e a Travessia do Mar Vermelho: A Física da Esperança" (1871p), 400119 História "O Rei que Inventou a Tolerância: Ciro..." (974p, **pauta por demanda** — query GSC "ira"), 400121 Ficção "Singularidade — Capítulo 3: O Mapa que Faltava" (985p, **sem capa** — Tribunal Visual reprovou a imagem IA; reparo: `python3 v4_ficcao.py --imagem 400121`).

**🐛 BUG DESCOBERTO (NÃO corrigido — aguardando sinal do Miguel):** a linha do cron do worker (`V4_TENDENCIAS_ESPELHO_20260817`) tem aspas corrompidas — literal `\x27` no lugar de `'` (bug de escape ao editar o crontab em 17/08). O cron DISPARA (prova syslog: 07:40/13:40/19:40 UTC) mas `/bin/bash -lc \x27cd` falha e a cadeia `&&` morre antes do Python → o worker **nunca executou via cron** (os 3 posts do Tendências saíram de runs manuais da sessão). Por isso ZERO posts do Tendências desde 17/08 18:28. Intake OK (*/30, fila ~589 candidatas crescendo; `stall_alert` só loga, não escala). Fix = 1 linha no crontab (restaurar aspas `'`). Backup: `/root/crontab.bak_pre_tendencias_20260817`.

---

## 11. ADENDO 18/08 ~23:30 BRT — ORDEM MIGUEL: V4 novos paralisados; Tendências restrito às 5 editorias do espelho (EXECUTADO)

**Ordem (~23:00):** (1) paralisar os V4 novos Religião/História/Ficção; (2) remover os blocos deles da home do espelho (e o de Tendências, já ausente desde a v2); (3) deixar o Tendências produzindo distribuído SÓ nos blocos de Geopolítica, Ciência, Inteligência Artificial, Cultura e Política (Nacional).

**Executado (tudo com backup .bak_pre_*):**
1. **NYC crontab** (`/root/crontab.bak_pre_paralisa_v4novos_20260818_20260819_0216`): 3 linhas `V4_NOVOS_*` REMOVIDAS; linha do worker Tendências CORRIGIDA (aspas literais `\x27` → `'` — o bug do §10; o cron nunca tinha executado de fato).
2. **Tencent — diretriz viva** (`/home/ubuntu/cafezinho/v6_data/radar_tendencias/diretriz_tendencias.json`, backup `.bak_pre_5editorias_20260818_2305`): `mapeamento_categorias` reescrito — 11 temas → só 5 cats: Geopolítica 5003, Política Nacional 22, Cultura 79, Ciência 735, IA 5008 (tema "tecnologia"→5008; tema novo "ciência"→735). Verificado no código: o regenerador diário NÃO sobrescreve o mapeamento. Histórico registrado (autor ZCode/DeepSeek).
3. **NYC intake** (`v4_tendencias_intake.py.bak_pre_5editorias_20260818`): constante `CATS_PERMITIDAS_TENDENCIAS = {22, 79, 735, 5003, 5008}` + gate que DESCarta candidata classificada fora das 5 (contador `skipped_categoria`); heurística: tecnologia 30→5008; novas palavras de Ciência→735.
4. **NYC worker** (`v4_vertical_draft_worker.py.bak_pre_5editorias_20260818`): guarda de defesa em profundidade — candidata fora das 5 → status `skip_categoria_fora`, não publica.
5. **NYC fila** (tendencias.sqlite3): 72 candidatas fora das 5 marcadas `skip_categoria_fora` (590→518). Restantes: 332 Política, 121 Geopolítica, 52 sem cat (fallback 22), 13 Cultura.
6. **Espelho home** (`front-page.php.bak_pre_remove_blocos_v4novos_20260818`): bloco `foreach` Religião/História/Ficção REMOVIDO (3019 chars, `php -l` OK). Bloco Tendências já não existia (removido na v2).
7. **Caçadora de imagens** (automação e1b2d648): PASSO 2.6 varre agora as 5 editorias (5003/22/79/735/5008) em vez de 100003/1652/775 — posts do Tendências publicados sem capa ganham foto real nas próximas rodadas e entram no bloco com capa.

**PROVA E2E (run manual do worker ~23:27 BRT):** post **400123** "Donald Trump declara Estreito de Ormuz como novo território dos EUA" — redigido e publicado pelo worker (redação DeepSeek), categoria **5003 Geopolítica**, **HERO do bloco Geopolítica na home do espelho** (ainda sem capa — a caçadora cobre). Link: https://cafezinho.news/2026/08/18/donald-trump-declara-estreito-de-ormuz-como-novo-territorio-dos-eua/

**Cron do worker:** mantido `40 7,13,19 * * *` (UTC no NYC = 04:40/10:40/16:40 BRT); agora CONSERTADO, próximo ciclo 07:40 UTC de 19/08. Intake segue */30.

---

## 12. ADENDO 19/08 ~10:15 BRT — RAIO-X do Tendências (pedido do Miguel: "já pode ir pro canônico?") + fix na caçadora

**Produção:** 5 posts no total — 400077/400079/400108 (era v1/v2) e 400123 (18/08 23:27, E2E) + **400125 (19/08 04:40 BRT, 1º post 100% autônomo via cron consertado** — prova no syslog 07:40 UTC com aspas corretas). Cadência: 1 post/ciclo × 3 ciclos/dia. Intake */30 saudável.

**Qualidade (li os 2 textos do regime novo):** 400123 (Trump/Ormuz) e 400125 (Israel/Cisjordânia) — sóbrios, fatos com fonte (Truth Social, reação de Gharibabadi, Qusra/ONU), sem léxico tabloide, sem número inventado, linha editorial correta. Gate anti-tabloide passando. Amostra ainda pequena (2 posts).

**Dinamismo — ponto de atenção:** o RADAR é diverso (9 temas quentes: bolsonaro, ceará, lula, eleições, stf...; queries novas: clima, Pablo Marçal, Carnaval 2027, Dostoievski, Cuba) e a FILA também (570 candidatas: 411 Política, 117 Geopolítica, 9 Cultura, 2 Ciência, 1 IA; sinais: top10 333, tema 168, gsc_emergente 37, exploração 2). PORÉM a SELEÇÃO está enviesada: 4 dos 5 posts publicados são Oriente Médio — o bônus de tema quente + top10 empurra geopolítica pro topo do score. O agente segue o interesse MEDIDO, e o interesse agora é Irã/Ormuz → risco real de "enxame" (o medo clássico). FALTA rotação de tema antes do canônico.

**Fix aplicado (caçadora e1b2d648):** o PASSO 2.6 atualizado ontem perdeu os escapes `\$` (o wp eval retornava vazio e a caçadora logava "espelho 5 editorias zerado" errado) — corrigido no prompt + `tail -15`→`head -15` (mais novos primeiro). 400123/400125 (sem capa, cat 5003) serão pegos na próxima rodada horária.

**VEREDITO (recomendação ZCode ao Miguel): NÃO portar ainda.** Aguardar ~48-72h (6-9 posts) e ANTES do port: (a) rotação de tema/editoria no worker (ex.: máx 2 posts seguidos do mesmo tema; alternar editorias quando o gap de score for pequeno); (b) confirmar fluxo de capas pela caçadora; (c) definir o fluxo de publicação no canônico (rascunho→loops, mapeamento para as categorias do canônico, indexação). O custo de erro no canônico é maior (indexado, publish pelos loops).

---

## 13. ADENDO 19/08 ~10:30 BRT — BLOCO "TOP TENDÊNCIAS" NA HOME DO ESPELHO (ordem Miguel)

**Ordem do Miguel (~10:15):** criar na home um bloco parecido com o "Os 10 mais vistos", chamado **Top 10 Tendências**, listando **SÓ posts do V4 Tendências**; embaixo, links **Top 20 | Top 50 | Top 100** (ele oscilou entre "anteriores/mostrar mais" e links — decidiu pelos links). SÓ no espelho hoje; amanhã vai pro canônico **se o Miguel aprovar**.

**Implementado (espelho, `front-page.php` do tema ocafezinho-portal; backup `.bak_pre_bloco_top_tendencias_20260819`; php -l OK):**
- Bloco inserido após "Os 10 mais vistos" e ANTES da Linha do Tempo (Linha do Tempo segue como última seção — regra 14/08 respeitada).
- Consulta: `WP_Query` com `meta_query zizi_job_id LIKE 'v4d_tendencias%'` — **marcador oficial** dos posts do V4 Tendências no espelho (400077/400079/400108/400123/400125 têm o marcador; o 400077 legado NÃO tinha — meta adicionada manualmente: `v4d_tendencias_legado_400077`).
- Ordenação: mais recentes primeiro (por data). Visual: badge numerado vermelho + título + data, igual ao bloco dos mais vistos.
- `?top_tendencias=10|20|50|100` (padrão 10; valor fora da lista cai no 10). O h4 muda ("Top 20 Tendências"), o número ativo vira badge vermelho e os demais são links.
- Verificado no ar: home com "Top 10 Tendências" + 5 posts; `?top_tendencias=100` com h4 "Top 100", badge ativo e links 10/20/50 funcionando.
- O sync horário canônico→espelho NÃO sobrescreve o front-page.php (só copia `uploads/2026`) — o bloco sobrevive aos syncs.

**Para o canônico (quando o Miguel aprovar):** mesmo bloco no front-page canônico + categorias/IDs do canônico (os posts Tendências vão nascer lá com as categorias correspondentes; a meta `zizi_job_id` prefixada `v4d_tendencias` deve ser mantida pelo worker na portabilidade) + avaliar ranking por views (top10 real) em vez de data.


### ⚠️ ADENDO DE SEGURANÇA 19/08 ~10:45 BRT — VAZAMENTO CORRIGIDO (ordem Miguel, regra nº 1)

**O que aconteceu:** o rodapé do bloco Top Tendências dizia "* Posts produzidos pelo agente V4 Tendências..." — texto RENDERIZADO revelando automação no site público (inaceitável mesmo no espelho). Na varredura pós-reprovação, descobri vazamento MAIOR: a REST pública expunha metas internas com VALORES — `zizi_job_id` (`v4d_tendencias_<hash>`) no espelho E no canônico (registro no functions.php do tema, sem auth_callback), e `_cafezinho_img_check` no canônico (valor cheio com `"checker":"claude_miguel"`; o registro divergente sem auth_callback NÃO foi localizado — mistério em aberto).

**Correções aplicadas (tudo com backup + php -l, sites 200):**
1. Texto do bloco → neutro ("* Mais recentes primeiro."; estado vazio sem "V4").
2. `auth_callback => current_user_can('edit_posts')` no registro de `zizi_job_id` (functions.php dos 2 sites; backups `.bak_pre_meta_privada_20260819`).
3. Mu-plugin novo `cafezinho-rest-meta-privada.php` nos 2 sites: filtro `rest_prepare_post` (prio 99) zera para NÃO-editores as metas internas (zizi_job_id, _cafezinho_img_*, cafezinho_image_kind/generator, cafezinho_nomes_check, _cafezinho_img_credit_pendente). Consumidores autenticados (painel .wp_creds, loops, workers REST auth) intactos.
4. Verificado de dentro E de fora (r.jina.ai): `zizi_job_id`="" e `_cafezinho_img_check`="" publicamente nos 2 sites; conteúdo dos 5 posts do Tendências sem termos internos; home do espelho sem referência a agente (só o "Worker" do script de emoji do WP core, benigno).

**Incidente de deploy (lição):** escrevi o PHP via heredoc dentro de aspas duplas do ssh sem escapar `$` → parse error no mu-plugin = site fora do ar em potencial; reescrito via pipe com heredoc quoted em minutos. Nunca mais: PHP no ssh vai por pipe com heredoc quoted ou arquivo via scp.

**Mistério em aberto (investigar depois):** com os DOIS registros de `_cafezinho_img_check` do canônico tendo auth_callback, a meta ainda expunha valor público — candidatos: opcache com arquivo velho, ou registro em código não varrido (variável como chave). O filtro do mu-plugin novo garante a privacidade independentemente da causa.

### ADENDO 19/08 ~11:45 — bloco "Top Tendências só-V4" DESMONTADO (superseded pelo carrossel)

O Miguel encomendou o box como CARROSSEL (ver `forum_top10_tendencias_espelho_arquiteturas_v4_20260819.md` — adendo 11:45). Meu bloco "só posts do V4" com links Top 20/50/100 (depois de "Os 10 mais vistos") foi REMOVIDO da home do espelho; o carrossel da 1ª posição (após a manchete) usa o ranking GA4. Reativar a versão só-V4 = WP_Query meta_query `zizi_job_id LIKE v4d_tendencias%` (a meta continua marcada nos posts).

### ADENDO 19/08 ~12:25 — KILL SWITCH: V4 Tendências DESLIGADO como publicador (ordem Miguel)

Ordem do Miguel (~12:00): "vamos desistir dele, ele não tem muito sentido" — o V4 Tendências deixa de publicar. `enabled=false` na diretriz viva (backup `.bak_pre_killswitch_20260819_1210`; endpoint já serve enabled=False). Intake/worker param sozinhos; **o radar (30/30min, Tencent) SEGUE** — vira o "agente silencioso" consultivo. O carrossel Top 10 Tendências (que usa GA4 do canônico, não o worker) segue vivo e foi pro canônico — detalhes no fórum do box. Religar = enabled=true.

---

### ADENDO 07/09 ~12:3x — Miguel RETOMA o fio: "COLETOR GA4 DOS MAIS LIDOS" (2 matérias/dia) — auditoria ZM + desenho, aguarda "vai"

**Pedido (Miguel, voz ~12:2x):** pesquisar se o "agente tendência" chegou a ser feito (foi — o protótipo deste fórum é a 2ª geração); proposta: **2 matérias/dia** derivadas dos posts mais lidos do site — **lista A** = top 30 dias FECHADOS, qualquer data de publicação (cauda longa/evergreen que segue sendo lida), **lista B** = top dos publicados nos últimos 7 dias (fresco/quente); matéria CORRELATA ("alguma coisa correlata"), não a mesma; ponderação: se a visitação estiver fraca, pesar a lista de 7 dias. Fonte: "Top 20 posts, 30 dias fechados" que o V6/GA4 já apura.

**Auditoria ZM (só leitura, provas):**
- GA4 **SAUDÁVEL** (incidente global de 03/09 backfillado — ver `forum_incidente_ga4_backlog_tendencias_20260903.md`): top 30d fechados AGORA = "China e Rússia cercam Japão em patrulha naval com rota inédita e tensa" **4.683 views** (o exemplo que o Miguel citou — transcrição de voz disse "Chile"), Lei Rouanet 2.812, Mendonça×Xandão 1.580, Casas Bahia×Mercado Livre 1.554, CV×condomínio 1.297. Filtro necessário: não-posts (home 47.768, página 404 3.728).
- **3 gerações do agente:** (1) fantastico/trends_v9/legacy (≤06/2026, "Triângulo de Ouro" = interesse inventado → sensacionalismo → desativados); (2) V4 Tendências (ESTE fórum, 16-19/08 — **morto pelo próprio Miguel 19/08 12:00**: "não tem muito sentido"; worker comentado 24/08 no desligão do V4; **intake `v4_tendencias_intake.py` */30 SEGUE no crontab da NYC** sem worker — limpeza pendente: confirmar se o kill-switch o fez parar de enfileirar); (3) camada de exibição **VIVA**: `top_tendencias_push.py` (horário :25, GA4 hoje+ontem, score gravidade, box Top 10 + página /top10 + categoria canônico/espelho — log ativo hoje 12:25 BRT) + radar /v6/tendencias (Tencent, sinais quentes GA4+GSC+ao vivo).
- **O que NUNCA existiu:** gerador diário mais-lidos-GA4 → pauta derivada → artigo no V4.1. É exatamente o buraco do pedido.

**Por que agora é diferente da versão morta em 19/08:** (a) a semente é a **métrica direta e determinística** (a lista top do GA4 que o Miguel vê no V6), não a cadeia indireta radar→diretriz→vertical que "não tinha sentido"; (b) **juiz 1 + juiz 2 + BOM GOSTO + rank-and-best estão NO AR** (nasceram 07/09) — os guardiões anti-sensacionalismo do §4 eram desenho de papel em 16/08; agora toda pauta derivada passa pelos 7 critérios ponderados + gate de texto + CL; (c) cadência fixa e pequena (2/dia) com tag de origem para medir de verdade (Astra: measure, don't assume).

**Desenho proposto (NADA implementado — aguarda "vai"):** adapter diário na NYC (padrão do coletor noturno IDEIA-012: fail-closed, INSERT OR IGNORE, idempotente) → lê GA4 (credencial/padrão já existem em NYC e Tencent) → 2 sementes (top A + top B, filtrando não-posts; piso: top A ≥ 500 views/30d; GA4 doente = colapso geral de views → NADA gerado, lição do 03/09) → **derivação**: LLM barato (cascata juiz) + busca web: "desdobramento/contexto atual/o que mudou desde então" do caso da semente — matéria correlata com gancho atual REAL e fontes atuais; **sem novidade, não escreve** (zero no dia é melhor que requentado — EMU/juiz 2 barrariam anyway) → insere a pauta no banco V4.1 com tag `tendencia_ga4_30d`/`_7d` + checagem "já publicou?" (RAR/dedupe) + **link interno da matéria nova para o post-semente** (SEO: autoridade para a página comprovadamente quente) → **slot de ciclo dedicado** (1×/dia, lote das 2 sementes no juiz 1; sugestão 13:05 BRT) → draft-only, publish segue exclusivo da CL. Herda: gate lexical tabloide (§4), métricas congeladas do piloto (§5, 14 dias) e kill-switch (enabled=false em config viva). Custo incremental estimado: ~US$ 0,20-0,30/dia (derivação barata; frontier só após juiz 1 aprovar).

**Abertos para o "vai":** (1) slot horário do ciclo; (2) desligar/limpar o intake órfão de 17/08; (3) se a matéria derivada pode ser de qualquer vertical (rota pelo assunto da semente) — sugestão: sim, roteamento normal com a tag de origem preservada.

— ZCode Dell (ZM) · Qwen3.8-Max · 07/09/2026 ~12:3x BRT
