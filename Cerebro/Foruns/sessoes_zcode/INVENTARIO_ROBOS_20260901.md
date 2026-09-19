# 📇 INVENTÁRIO DE ROBÔS DA CASA — 01/09/2026 ~14:00 BRT (pesquisa ao vivo, Z0/ZM)

> **Pedido do Miguel:** "Quantos robôs estão no ar? Quantos DSN? Endereço de todos, função, se estão em ronda, se estão ativos com tarefa."
> **Método:** leitura AO VIVO dos crontabs + systemctl + logs/estados internos via SSH (tencent / nyc / cafezinho-wp) + crontab do Dell + CronList do ZCode. Zero chute — cada linha tem prova.

## 🥇 A resposta curta

**5 DS-N (DS Nuvem) no ar**, todos com ronda viva comprovada + **1 robô irmão** (Olho Apurado do Banco Ouro) + esteira V4.1 + verificador de virada + uma constelação de robôs de apoio (telemetria, backup, indexação). **Nenhum DS-N morto.** A vaga que NÃO nasceu: Marketing, Coordenador/RH, Segurança, Métricas, Memória, Editor Baleia, Redes (todas em `TAREFAS_MESTRE.md` Z2/Z3/Z4).

## 📋 A família DS NUVEM (5 no ar)

| # | Robô | Endereço | Função | Ronda | Estado (prova ao vivo 01/09 ~14:00) |
|---|---|---|---|---|---|
| 1 | **DS-N Chefe** | `tencent` (ubuntu@43.156.151.165 -p 38422): escuta = systemd `ds-nuvem-chefe-escuta.service`; ronda = `~/ronda_dsn.sh` | Ouvido da casa no Telegram (Loop A, long polling 25s) + ronda de saúde da família | escuta 24/7 + ronda */30 | 🟢 ATIVO — serviço running desde 30/08 16:39; log de hoje com assinatura `DS-N Chefe · 20260901 13:30:58 BRT` exit=0 13:33 |
| 2 | **DS-N Publicador** | `tencent`: `/home/ubuntu/dsn_publicador/` (dsn_publicador.py) | Mão editorial: publica rascunhos aprovados c/ capa+veredito, provas REST, freios 3+8/dia | */15 | 🟢 ATIVO — estado.json: publicados até **12:45 de hoje** (últ. 268540), provas com link+capa, halted=false; cron.log velho (ReadTimeout 21:47 de 31/08) é o engasso intermitente já fichado, não morte |
| 3 | **DS-N Ideias** | `tencent`: `/home/ubuntu/dsn_ideias/` (ronda_dsn_ideias.sh) | Arquiteto: caça problemas 2/2h, propõe ideias, estuda audiência quando quieto | 13,43 (2×/h) | 🟢 ATIVO — syslog prova execuções **13:13 e 13:43 de hoje**; última produção registrada (caçadas/ideias executadas) 31/08; estado `processadas: []` = sem dedup pendente |
| 4 | **DS-N YouTube "Deni"** | `tencent`: `/home/ubuntu/ds_youtube/` + **porta de download no Dell** `~/ds_youtube_fetcher/` (fetcher */5, IP residencial) | Vídeo→transcrição→matéria estilo casa; NUNCA publica (gate CL→Publicador) | Tencent 7,22,37,52 + Dell */5 | 🟢 ATIVO — estado.json tocado **13:37 de hoje** (last_check 13:07); batismo Sabatina das Cunhãs 31/08 (268440 no ar 20:31); fila Roni Lessa pendente de processar (DSC-20260901-003) |
| 5 | **DS-N Imagem** | `nyc` (root@198.199.121.136): `/root/v4_labs/codigo/dsn_imagem.py` | Capas: fila de rascunhos frescos → busca FOTO ACHADA (IA proibida) → visão dupla → aplica via adapter; nunca publica | */20 (limite 3) | 🟢 ATIVO — rodada fim no log às **16:40 UTC de hoje** (minutos antes da checagem), fila_olho_humano=5 |

**Irmão de família (conta à parte):** **Olho Apurado do Banco Ouro** — `nyc`: `/root/olho_apurado_ouro.py`, ronda 25 */2h, visão dupla nas 474 fotos aprovadas. 🟡 RODA mas a última rodada bateu no **erro de proxy IPRoyal** (`ProxyConnectionError`, 40 erros / 0 processadas às 16:34 UTC) — proxy caído ou crédito; cura = checar IPRoyal (memória DSL-010 tem o kill-switch).

## 🤖 Outros robôs em ronda (não-DSN, confirmados ao vivo)

| Robô | Endereço | Função · ronda | Estado |
|---|---|---|---|
| **Esteira V4.1** (redator oficial) | `nyc`: `/root/v4_labs` (codigo.v41_ciclo) | Pauta→tese→rascunho por vertical | 🟢 rascunho 268544 (saúde) hoje 12:44 BRT; ciclo nacional 13:27 rodou |
| **Tribunal Agenético** | `nyc`: `codigo.tribunal_agentic_diario` | Julga melhor/pior post do dia | 🟢 diário 23:30 |
| **Verificador de Virada** | `cafezinho-wp` (root@190.89.239.65 -p 51439): `/root/verificador_virada.sh` | Publica future vencido c/ capa+check (BUG-DS-100 estrutural) | 🟢 syslog prova 13:30/13:35/13:40 de hoje; log vazio = nada vencido (normal) |
| **Minibot DSC** (carteiro @dscelular_bot) | `cafezinho-wp`: `/usr/local/bin/dsc-minibot.py` (systemd) | Único consumidor getUpdates do Telegram do DSC | 🟢 processo active desde 03:31 de hoje — ⚠️ a ronda do meio-dia o dava como "mudo": se o DSC não responder no Telegram, revalidar |
| **Sync memória DSH→GitHub** | `cafezinho-wp`: `/root/Cerebro/scripts/sync_memoria_dsh.sh` | Camada garantia da memória (*/30) | 🟢 no crontab desde 01/09 madrugada |
| **Baleia Azul (envio)** | Dell: `~/bin/enviar_baleia_azul_ponte.sh` | Boletim manhã 08:00 + tarde 19:30 (+ custos 8,18h; vigia */30) | 🟢 crons vivos; editor-robô próprio = vaga Z3.5 |
| **DS Miguel (Dell)** ronda 30 min | Dell: `~/.../ronda_30min.sh` */30 | Ronda do DS do Dell c/ assinatura qualificada | 🟢 no crontab |
| **Vigília de crédito** | Dell: `~/.zcode/hooks/credito_vigilia.py --probe` */15 | Cabeçalho de saldo dos provedores | 🟢 (linha no topo desta conversa) |
| **LUMINA / FAROL / telemetria §118** | `tencent`: lumina_coleta */30, farol-coletar */30, healthchecks */5, telemetria_export */5, prometheus */5 | Medidores e guardiões de custo da casa | 🟢 todos no crontab |
| **V4.2 estatístico** | `nyc`: agente_economia (coletor 10,20 · ingestor */15 · ciclo 15:10) | Matéria estatística diária (espelho) | 🟢 |
| **Bot News · Coment. só-humanos · indexadores · PageSpeed/GSC/GA4 · temáticos (GSN etc.) · moka vigia/descadastro** | `nyc` / `tencent` | Apoio editorial e de produto | 🟢 nos crontabs (V4 legado marcado V4_DESLIGADO_20260824 — só V4.1 vale) |

## 🎭 Automações do ZCode (Dell — CronList ao vivo)

| Automação | Cadência | Estado |
|---|---|---|
| Ronda ponte ZM↔DSC (`a36cc334`) | */30 | 🟢 ATIVA (últ. run hoje 13:23) |
| Ronda V4.1 canônico (`90a56cde`) | */30 | 🟢 ATIVA (últ. hoje 13:12; 111 runs) |
| Maestro Cafezinho+MOKA (`3ad40af1`) | 1/1h | ⏸️ PAUSADA após o plantão noturno (últ. run hoje 12:00; 14 runs) |
| MOKA ronda produtiva (`25e54785`) | 1/1h | ⏸️ PAUSADA (Miguel pausou 31/08 23:18 — perna MOKA assumida pelo maestro) |
| Relatório 2h Telegram (`3ddb410c`) · Play Store 11h (`3631380a`) · Fênix Priscila (`d4e94344`) | — | ⏸️ PAUSADAS |

## 📜 AUDITORIA DE LOGS (pedido do Miguel 01/09 ~14:0x: "cada um tem que ter um log") — veredicto: TODOS os 5 DS-N têm log

| Robô | Log (caminho) | Histórico | Última linha | O que registra |
|---|---|---|---|---|
| **DS-N Chefe** | `tencent:/tmp/ronda_dsn/YYYYMMDD.log` (1 por dia) | 29/08→hoje (4 diários, 10–70KB) | hoje 13:33 `exit=0` | 🥇 MODELO: relatório da ronda inteiro — saúde da família, lições (ex.: cura do quirk face 2 validada 2×), assinatura qualificada BRT |
| **DS-N Publicador** | `tencent:~/dsn_publicador/logs/YYYYMMDD.log` + `estado.json` (provas REST) | 31/08→hoje | hoje **13:45** `fim de ciclo: publicados=[] avisos=[268437,268491] resgates=0` | Cada ciclo */15: publicados/avisos/erros (ex.: `olho reprovado (REPROVADA/REPROVADA)` no 268484 às 13:31) + histórico de provas com link+capa |
| **DS-N Ideias** | `tencent:/tmp/dsn_ideias/YYYYMMDD.log` (1 por dia) | 31/08 (27KB)→hoje (54KB) | hoje **13:45** `exit=0` | Raciocínio completo da ronda: fila de ideias, regra do silêncio (1 CHECK/h), commits no canal `de_ideias.md` |
| **DS-N YouTube "Deni"** | `tencent:~/ds_youtube/logs/YYYYMMDD.log` | 31/08→hoje | hoje **12:07** `pull falhou, pulo ciclo` | Cada ciclo: reconcile git → fila → matéria. 🔴 **log revela robô TRAVADO desde 12:07** (ver abaixo) |
| **DS-N Imagem** | `nyc:/root/agent_data/dsn_imagem/cron.log` (930 linhas) + `log.txt` (74KB) + `estado.json` + `fila_caca.jsonl` + `memoria_aprendizado.json` | 31/08 14:20→agora | hoje 16:40 UTC `RODADA fim: fila_olho_humano=5` | Rodadas início/fim, vereditos de visão, fila de caça, memória de aprendizado |
| Olho Apurado | `nyc:.../olho_apurado_cron.log` (540 linhas) | 31/08→agora | hoje 16:34 (40 erros proxy) | Vereditos por foto + erros |
| V4.1 | `nyc:/root/agent_data/v41_ciclo.log` (583 linhas) | — | hoje | Ciclo por vertical, tese, rascunho |
| Verificador de Virada | `cafezinho-wp:/root/agent_data/verificador_virada.log` | só escreve quando há vencido | 12:01 (nenhum vencido desde) | ⚠️ log esporádico por design (ociosidade = syslog do cron) |

### 🔴 Achado da auditoria: DS-N YouTube parado desde 12:07 (o log contou a história)

```
[2026-09-01 12:07:04] reconcile falhou: cannot pull with rebase: You have unstaged changes
[2026-09-01 12:07:07] pull falhou, pulo ciclo: Diverging branches can't be fast-forwarded
```
= no clone `~/cerebro-miguel` da Tencent há **mudanças não commitadas + a divergência origin 392×428** (a mesma que trava o push do Dell). O robô está vivo e em ronda (estado 13:37) mas **pula todo ciclo** — a fila Roni Lessa (DSC-20260901-003) não anda por isso. **Cura (receita, aguarda "vai" — repo concorrido com o Publicador):** na Tencent, `git stash` (ou commit seletivo do que for do Publicador) + `git pull --rebase origin main` resolvendo a divergência local; a divergência estrutural origin segue como pendência ZM↔us65.

### 🟡 Gaps menores de log (não bloqueiam)
1. `~/dsn_publicador/cron.log` = só Tracebacks de ReadTimeout (lixo de erro do wrapper; o log de verdade é `logs/`).
2. Ideias: `estado.json` órfão (`processadas: []` desde 31/08) — o próprio log explica: o sandbox nega escrita fora do workspace; estado real fiel no canal `de_ideias.md`.
3. Verificador de Virada não loga ociosidade (syslog cobre; virar log-heartbeat se o Miguel quiser).

## 🔴 Mortos / não-nascidos (honestidade)

- **Agente YouTube ANTIGO (bloco Vídeos):** morto desde 28/08 (Transkriptor sem crédito) — substituído pelo DS-N YouTube novo.
- **Robôs PEDIDOS ontem e ainda não construídos** (só a vaga existe — nada no ar): Marketing (DSC-013, prompt no seu Telegram) · Coordenador/RH · Segurança · Métricas · Memória · Editor Baleia Azul · DS-N Redes (pós-debate) · DS-N Publicidade (vaga 01/09 ~02h) · DS-N Relações Públicas/Mapa Rio. Mapa: `TAREFAS_MESTRE.md` Z2/Z3/Z4.
- **@dscelular_bot:** processo minibot VIVO desde 03:31, mas ronda do meio-dia registrou o bot mudo — vigiar.

— ZCode/GLM-5.3 (Z0) · 01/09/2026 · carimbo BRT

## 🧠 ANÁLISE DE UTILIDADE (pedido do Miguel ~14:2x: "estão servindo pra algo? o Ideias está dando ideias, estão sendo ouvidas? tem diálogo?") — leitura dos CONTEÚDOS dos logs/canais em 01/09 ~14:2x

**Veredicto por robô (com prova do que o log diz):**

1. **DS-N Publicador — ÚTIL DIRETO (a mão editorial).** Hoje: publicou 268441 (03:16), 268456 (07:46), 268462 (08:30), 268412 (09:45), 268474 (10:31), 268473 (11:15) — todos com prova REST (link+capa) no estado.json. Do 31 posts do dia, a madrugada/manhã foi majoritariamente mão dele. O Chefe comemorou ao vivo: "268473 entrou no ar às 11:15:17 — 9º post do dia".
2. **DS-N Ideias — ÚTIL E CONVERTENDO (o cérebro da casa).** 10ª caçada hoje (12:47): 5 problemas + 12 ideias com qualidade real (quirk da bitácora, esqueleto Ronnie Lessa ENTREGUE, mapa de pontes, hora dourada 12:00-12:30 com dados LUMINA/GA4, régua de teto overdrive). Conversão PROVADA: IDEIA-003 (verificador de virada) virou código real e validado ("268455 virou 23:55 confirmado em 3 vias — P1 funcionou como desenhado"); IDEIA-001/001A (manual redes) virou sprint aprovada; IDEIA-004 (ORIGENS+editora) entregue 00:47; o ZM absorveu input dele ("IDEIA-003 validada/absorvendo input do ZM"; P2 Banco Ouro executada 02:00 pelo maestro). **Diálogo existe e o log prova.**
3. **DS-N Chefe — ÚTIL (o termômetro e o narrador).** Ronda 125 hoje; "20ª leitura seguida sem alerta"; volume 3h=8/12h=17/24h=34; LUMINA 1.076 distintos = novo máximo do dia. E é ELE quem documenta o diálogo dos outros: "268482 subiu 12:39 — a AGY Laura executou a cura do quirk com o trio de datas e a receita da Claude".
4. **DS-N YouTube — provado hoje:** 1º ciclo autônomo E2E → matéria 268553 no gate.
5. **DS-N Imagem — hoje mais GUARDA do que aplicador:** rodadas vivas mas fila_olho_humano=5 e nenhum veredito APROV/REPROV com data de hoje no log.txt; requests repetidos do 268425 (Play Books) 4h→6h sem achar. Papel do dia = triagem/barreira (rede de segurança), não aplicação. Olho Apurado: 🟡 proxy IPRoyal caído (40 erros/0 processadas).

**O gráfico do diálogo (quem fala com quem, provado nos canais):** Ideias propõe (caçadas + P1..P5) → ZM/maestro executam (P2 Banco Ouro ✅ 02:00) → AGY-Laura aplica na esteira (cura do quirk 12:39) → Chefe confirma e narra (rondas 12:00-14:00) → Miguel decide o topo (6 decisões do cartão). **O diálogo robô↔robô FUNCIONA; o gargalo declarado é a fila de ✓ no Miguel** (12 ideias + 6 decisões + IDEIA-004 pendentes — o próprio Ideias avisou: "sem resposta até o fim do dia → pendência de agenda formal"). E o Ideias repete CHECKs "fila vazia" (17º) — precisa de insumo novo (blocos IDEIA_PRO, dados de audiência, ou encomendas).

— ZCode/GLM-5.3 (Z0) · 01/09/2026 ~14:2x BRT
