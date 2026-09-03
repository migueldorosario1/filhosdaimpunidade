# 🤖 CÉREBRO CAMADA 2: Nodo de Agentes (Inventário por Tipo)

> [!IMPORTANT]
> **Correção de inventário — 10/08/2026:** `agente_controlado.py` é componente legado e está fora do V4. O V4 ativo redige por `codigo.v4_vertical_redactor_runtime`, invocado por `/root/v4_vertical_draft_worker.py`. A tabela histórica deste nodo não define arquitetura operacional; ver `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

> [!CAUTION]
> **REGRA DE ATUALIDADE 11/08/2026:** conferir também `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`, processo, service e cron. Augusto e Mayra estão vivos em NYC; Zizilinda e o agente controlado são históricos/legacy e não podem ser inferidos como ativos por linhas antigas deste inventário.

**Criado:** 2026-05-21 02:40 BRT por Claude (a pedido de Miguel 20/05 12:46 BRT)
**Fonte de dados:** Tencent (`ls /root/agente_*.py + coletor_*.py + robo_coleta_*.py`) + crontab vivo
**Total inventariado:** 104 arquivos `agente_*.py` + 12 coletores + utilitários
**Última auditoria:** 2026-05-21 02:35 BRT

---

## 🧭 ONBOARDING DE AGENTES/LLMs — Tutorial de conexão ao Cérebro (2026-08-03)

- **Tutorial canônico:** `TUTORIAL_CONEXAO_CEREBRO_LLMS.md` (raiz do Cérebro) — texto para colar em qualquer LLM: 4 vias de acesso (local, servidores, clone GitHub `migueldorosario1/cerebro-miguel`, chat puro), ritual de leitura, 3 camadas, regras de credenciais e de escrita.
- **Espelho GitHub:** repo privado `migueldorosario1/cerebro-miguel`, sync unidirecional local→GitHub via `~/cerebro-miguel/scripts/sync_cerebro_to_github.py` (scanner de segredos ativo). Auditado/sincronizado em 2026-08-03 05:54 (5.236 arquivos).
- **Registros (Tema Duplo):** `Foruns/forum_tutorial_conexao_cerebro_llms_20260803.md` + `Memorias/memoria_tutorial_conexao_cerebro_llms_20260803.md`.

---

## 🌟 SPARK (Google/Gemini) — agente externo via Google Drive (cadastrado 2026-08-06)

- **Quem é:** Spark ("Spark com K") — agente do ecossistema Google/Gemini configurado pelo Miguel em 06/08/2026, com acesso nativo ao **Google Drive, Gmail, Google Calendar e Google Contatos** dele.
- **Acesso ao Cérebro:** **VIA DRIVE, SÓ LEITURA** — espelho `drive:Cérebro Imortal da Trindade/cerebro-miguel/cerebro/`. ⚠️ O espelho pode estar defasado: frescor = última entrada de `CEREBRO_NODE_ATUALIZACOES.md`. O Spark **não escreve** no Cérebro: produz texto e o Miguel (ou agente local) grava no canônico.
- **Onboarding:** recebeu prompt de conexão (baseado no `TUTORIAL_CONEXAO_CEREBRO_LLMS.md`) + Carta de Missão (06/08). **Prova de conexão (checklist): PENDENTE** na data do cadastro.
- **Missões (carta de 06/08):** (1) Índice/organização do Google Drive — Fase 1 com "vai" (read-only); (2) triagem Gmail (marcadores, filtros, pendências); (3) Agenda + registro de convidados — **modelo misto aprovado**: Google Contatos + Planilha espelho, notas com origem+contexto+data; (4) WhatsApp — **confirmado SEM acesso nativo**: caminho aprovado = export `.txt` → pasta `WhatsApp_Backups_Entrada` no Drive → Spark processa; API dedicada (Business Cloud/Evolution) em avaliação futura.
- **Ponte Spark↔Kimi:** `drive:Ponte_Spark_Kimi/` (criada 06/08) — `README_PONTE.md` (contrato), `CAIXA_KIMI.md` (Kimi→Spark), `CAIXA_SPARK` (Google Doc, Spark→Kimi), `HISTORICO.md` (log). **Nunca** criar ponte dentro do espelho do Cérebro (sync local→Drive sobrescreve).
- **Restrição de segurança:** docs de senha/chave/token no Drive (ex.: "Senhas nova 6 abril 2026") são `[RESTRITO — Cofre]` — Spark não abre/lê/resume. Pendência: migrar conteúdo ao Cofre canônico e esvaziar o doc (Miguel).
- **Regras de trabalho:** propor antes de agir ("vai" do Miguel); nada se apaga (arquivo morto datado); citar fonte; PT-BR.
- **Registros (Tema Duplo):** `Foruns/forum_spark_google_entrada_ecossistema_20260806.md` + `Memorias/memoria_spark_google_entrada_ecossistema_20260806.md`.

---

## 🗂️ SESSÕES ZCODE Z0–Z7 — mapa de trabalho do ZCode Miguel (2026-09-01)

- **O quê:** o trabalho do **ZCode Miguel (ZM, Dell)** passa a ser dividido em sessões numeradas **Z0–Z7**, espelhando os temas DSC (celular): Z0 controle geral · Z1 artigos do Miguel · Z2 redes sociais · Z3 robôs DS Nuvem (RH + vagas) · Z4 marketing · Z5 MOKA · Z6 YouTube · Z7 ORIGENS+editora. Nasceu da noite 31/08→01/09 (ordem do Miguel via prompt do DSM).
- **Mestre de tarefas:** `Foruns/sessoes_zcode/TAREFAS_MESTRE.md` (34 tarefas com dono/dependência/status) · **Índice:** `Foruns/sessoes_zcode/INDEX_SESSOES_ZCODE.md` (1 linha por sessão + prompt de abertura) · **Protocolo:** toda sessão Z acorda lendo `CEREBRO_NODE_DSM_MEMORIA.md` + `CEREBRO_NODE_AGENDA_LEMBRETES.md` + sua seção no mestre; encerra atualizando status (append-only) + registro próprio + bloco no §1 do node DSM.
- **Espelho DSC:** `Foruns/sessoes_dsc/INDEX_SESSOES_DSC.md` (temas 0–10). Mudou um lado, o outro reflete na próxima ronda.

---

## 📌 Como ler esta tabela

| Coluna | Significado |
|---|---|
| **Status** | ✅ ATIVO (cron rodando) · 🛑 PAUSADO (cron comentado) · ⚠️ INATIVO (sem cron, mas existe) · 💀 LEGACY/BKP |
| **Portal** | CZ=Cafezinho · GSN=Global South News · RC=Rio Carta · BOT=Telegram · TODOS=horizontal |
| **Cron** | Cadência (vazio = sem cron) |

---

## 1. 🏛️ EDITORIAIS / PRODUÇÃO (Trindade Editorial e Temáticos)

Agentes que produzem texto editorial para publicação no portal.

| Agente | Status | Portal | Cron | Função |
|---|---|---|---|---|
| `agente_master_geopolitica` | ✅ | CZ | (via maestro) | Master de geopolítica (sub-agente do maestro_editorial) |
| `agente_master_nacional` | ✅ | CZ | (via maestro) | Master nacional (sub-agente do maestro_editorial) |
| `agente_master_trends` | ✅ | CZ | 1/h | Master de trends |
| `agente_master_trends_v9` | ⚠️ | CZ | — | Master trends V9 (provavelmente legacy) |
| `agente_master_lula` | ✅ | CZ | — | Master Lula (Olhar do Stuckert diário) |
| `agente_master_discursos` | ⚠️ | CZ | sob demanda | Discursos presidenciais via Jina+Serpro |
| `agente_lula` | ✅ | CZ | 09:30 BRT | Olhar do Stuckert (foto Flickr) |
| `agente_china` | ✅ | CZ | 5/dia | Agente China pró-PCC (stack 100% chinês) |
| `agente_latam` | ✅ | CZ | — | Cobertura América Latina |
| `agente_sheinbaum` | ✅ | CZ | — | Foco Sheinbaum (México) |
| `agente_mercado` | ✅ | CZ | — | Econômico |
| `agente_inflacao` | ✅ | CZ | freshness ≤15d | Inflação |
| `agente_matriz_energetica` | ✅ | CZ | FOSSIL ímpar/TRANSICAO par | Matriz energética |
| `agente_fantastico` | ✅ | CZ | 6/dia | Ciência/divulgação |
| `agente_militar` | ✅ | CZ | 1/dia | Militar |
| `agente_crime` | ✅ | CZ | 3/dia | Crime/segurança |
| `agente_feminino` | 🛑 | CZ | 1/dia | Feminino |
| `agente_eleicoes_produtor` | ✅ | CZ | 12/dia (41 7-13,18-22) | Produtor Eleições 2026 (diretriz v2 vigente) |
| `agente_eleicoes_legado` | 💀 | CZ | (PAUSADO) | Versão legacy do agente Eleições |
| `agente_ia` | ✅ | CZ | — | Agente IA (editoria sobre IA — pedido Miguel 15/05) |
| `agente_singularidade` | ⚠️ | CZ | — | Singularidade |
| `agente_petroleo` | ⚠️ | CZ | — | Petróleo |
| `agente_soberania` | ✅ | CZ | — | Soberania |
| `agente_sobrenatural` | ⚠️ | CZ | — | Sobrenatural |
| `agente_escritor_scifi` | ✅ | CZ | — | Ficção científica PT |
| `agente_escritor_scifi_en` | ✅ | GSN | — | Ficção científica EN |
| `agente_ficcao_noturna` | ⚠️ | CZ | — | Ficção noturna |
| `agente_historiador` | ⚠️ | CZ | — | Histórico |
| `agente_diario_direita` | ⚠️ | CZ | — | Diário da direita (cobertura adversária) |
| `agente_news_trend` | ⚠️ | CZ | — | News trends |
| `agente_novo_trends` | ⚠️ | CZ | — | Novo trends |
| `agente_agitador` | ⚠️ | CZ | — | Agitador editorial |
| `agente_flavio_bolsonaro` | 🟡 DRY-RUN | CZ | */30 local | Cobertura crítica dedicada a Flávio Bolsonaro/Banco Master/PL; criado por Kimi em `root/staging_social/flavio_bolsonaro/`, cron local de dry-run ativo, sem publicação WP |
| `agente_analise` | ⚠️ | CZ | — | Análise |
| `agente_grade_diaria` | ⚠️ | CZ | — | Grade diária |
| `agente_planejador_bella_ciao` | ⚠️ | CZ | — | Planejador "Bella Ciao" |
| `agente_produtor_bella_ciao` | ⚠️ | CZ | — | Produtor "Bella Ciao" |
| `agente_repetidor_estatal` | ✅ | CZ | 1/h | Repetidor estatal |
| `agente_correcao` | ⚠️ | CZ | — | Correções |
| `agente_videomaker_diario` | ⚠️ | CZ | — | Vídeo diário |
| `agente_geopolitica_en` | ⚠️ | GSN | — | Geopolítica EN |
| `agente_master_geopolitica` | (duplicado acima) | | | |
| `agente_pet_v1` | ⚠️ | CZ | — | Pet (pauta animal) |
| `agente_energias` | ⚠️ | CZ | — | Energias |
| `agente_turismo_embratur` | ✅ | GSN | — | Turismo Embratur (cross-post BR→GSN) |
| `agente_curadoria_gsn` | ⚠️ | GSN | — | Curadoria GSN (Top 15 CZ → traduz → GSN) |
| `agente_riocarta` | ⚠️ | RC | — | Agente Rio Carta |

## 2. 📡 COLETORES / SCRAPERS

Agentes que coletam dados brutos (fontes, feeds, scrapers) — alimentam editoriais.

| Coletor | Status | Portal | Cron | Fonte |
|---|---|---|---|---|
| `robo_coleta_bruta` | ⚠️ | CZ | — | Coleta bruta universal |
| `robo_coleta_geopolitica` | ✅ | CZ | 4x/h (5,20,35,50) | Geopolítica |
| `robo_coleta_nacional` | ✅ | CZ | — | Nacional |
| `robo_coleta_latam` | ✅ | CZ | — | LatAm |
| `robo_coleta_sheinbaum` | ✅ | CZ | — | Sheinbaum/México |
| `robo_coleta_lula` | ✅ | CZ | — | Lula |
| `robo_coleta_militar` | ✅ | CZ | — | Militar |
| `robo_coleta_trends` | ✅ | CZ | — | Trends |
| `robo_coleta_soberania` | ✅ | CZ | — | Soberania |
| `robo_coleta_discursos` | ⚠️ | CZ | — | Discursos Lula (Jina/Serpro) |
| `robo_coleta_imagens` | ✅ | CZ | — | Banco de mídia (~10k imagens) |
| `robo_coleta_flickr_rapido` | ✅ | CZ | 10/min | Flickr live photo lookup |
| `coletor_eleicoes` | ✅ | CZ | 4/dia (23 7,11,15,19) | Coletor Eleições 2026 (Brave Search + Trafilatura) |
| `robo_coleta_flavio_bolsonaro` | 🟡 DRY-RUN | CZ | */30 local | Coletor RSS + Brave/Search para Flávio/Banco Master/PL; alimenta `root/agent_data/coleta_flavio_bolsonaro.json` no ciclo dry-run |
| `coletor_china` | ✅ | CZ | — | Coletor Tríade China |
| `coletor_eleicoes_rascunho_antigravity_20260424` | 💀 | CZ | (rascunho AG) | LEGACY/RASCUNHO — não usar |
| `agente_curador_fontes` | ⚠️ | CZ | — | Curador de fontes |
| `agente_curador_midia` | ⚠️ | CZ | — | Curador de mídia |
| `agente_curadoria` | ⚠️ | CZ | — | Curadoria geral |
| `agente_news_trend` (já listado em Editoriais) | | | | |

## 3. 📤 PUBLICADORES / CROSS-POST

Agentes que pegam conteúdo pronto e publicam.

| Agente | Status | Portal | Cron | Função |
|---|---|---|---|---|
| `motor_publicador.py` (não é "agente") | ✅ | CZ | (via maestro/sub-agentes) | Motor central de publicação WP |
| `MT_agente_ferroviario` | 🟢 | MT | — | Mundo Trilhos Astro/Markdown/Git; sem Cafezinho |
| `agente_turismo_embratur` (já listado) | | | | |
| `agente_curadoria_gsn` (já listado) | | | | |

## 4. 📱 REDES SOCIAIS (Família dos 5 Irmãos)

Ver `forum_arquitetura_agentes_sociais_20260521.md` para detalhes.

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_facebook` | ✅ | 4x/h (9,24,39,54) — cooldown 4-5h | Único ATIVO — Modo FOTO, sem LLM |
| `agente_twitter` | 🛑 PAUSADO 19/05 | 2-min split (PAUSADO_MIGUEL_20260519) | Em reforma |
| `agente_instagram` | 🛑 PAUSADO | 0,30 * * * * (PARADO A PEDIDO MIGUEL) | Aguarda decisão |
| `agente_bluesky` | ⚠️ | — | Login restaurado 21/05 00:10 BRT, sem cron |
| `agente_tiktok` | ⚠️ | — | Pipeline pronto (4 pendências PENDENCIAS_TIKTOK.md), sem cron |
| `agente_twitter_video` | ⚠️ | — | Twitter com vídeo |
| `agente_rail_post` | ⚠️ | — | Esteira de post (revisor Grok→Claude→Mistral histórico) |

## 5. 🛡️ MONITORAMENTO / SENTINELA

Vigias que rodam continuamente checando saúde do sistema.

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_observador` | ✅ | 11,41 (30min) | Sentinela V3 — varre WP, rebaixa drafts alucinados |
| `agente_monitor_eleicoes` | ✅ | 10,40 (30min) | Monitor Eleições — alerta sobre roteador, custos, traceback |
| `agente_audio_monitor` | ⚠️ | — | Monitor de áudio (Telegram?) |
| `agente_audio_consumer` | ⚠️ | — | Consumer áudio |
| `vigia_nyc_readonly.py` (não-`agente_` mas é sentinela) | ✅ | NYC | Vigia NYC dormente — alerta queda IP Tencent |
| `trindade_economica_vigia.py` (não-`agente_`) | ⚠️ | (cron sugerido */15) | Sentinela financeiro |

## 6. 🔍 AUDITORIA / QUALIDADE / VIGILANTE

Agentes que verificam qualidade de conteúdo/agente.

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_auditor` | ✅ | 0 */3 (3h) | Inspeção de logs |
| `agente_auditoria_sistema` | ⚠️ | — | Auditoria de sistema |
| `agente_certificador_qualidade` | ⚠️ | — | Certificador semanal por amostra (tier decisão) |
| `agente_validador_modelos` | ✅ | — | Valida modelos LLM (testa temperature etc) |
| `agente_qualidade_redacao` | ⚠️ | (Fase 0 read-only) | Novo Agente Qualidade Redação (Codex deployou 20/05 14:32 BRT) |
| `agente_diretrizes_editoriais` | ⚠️ | — | Diretrizes editoriais ("Agente Diretriz" de AG 20/05) |
| `agente_escalada_qualificacao` | ✅ | 50 * * * * (1/h) | Escalada qualificação (DRY-RUN, hard-actions OFF) |
| `agente_vigilante` | ⚠️ | — | Vigilante geral |
| `agente_fact_check_perplexity` (não-`agente_` mas é função) | ✅ | (chamado por motor) | Fact-check Perplexity sonar |
| `agente_china_health` | ⚠️ | — | Health check China |

## 7. 🩺 AUTOCURA / MANUTENÇÃO

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_autocura_v4` | ✅ | 17 * * * * + diário 08h + semanal sex 14h | Autocura V4 com consenso 3/3 + 6 invariantes |
| `agente_corretor_autonomo` | 🛑 | DESATIVADO V3 | Cura drafts problemáticos (substituído por `curar_post_unico()` sob demanda) |
| `agente_reciclador` | ✅ | — | Reciclador |
| `agente_tester_chaves` | ✅ | — | Testa chaves LLM/APIs |

## 7.5 🏗️ SPRINT REFATORAÇÃO PADRÃO OURO (ATIVO — 2026-05-25)

**Ordem:** Miguel / Claude Maestro  
**Responsável:** Kimi Code CLI  
**Fórum:** `Foruns/forum_refatoracao_padrao_ouro_20260525.md`

**Objetivo:** Refatorar agentes publicadores fora do padrão ouro para o modelo `agente_militar.py` (51 linhas) + `robo_coleta_*.py`.

**Grupos:**
| Grupo | Agentes | Status |
|-------|---------|--------|
| 1 (URGENTE) | `agente_crime.py`, `agente_turismo_embratur.py` | 🟡 Crime: coletor + agente reescritos, aguardando teste `--rascunho` |
| 2 (PREMIUM→OURO) | `agente_inflacao.py`, `agente_mercado.py`, `agente_matriz_energetica.py`, `agente_ia.py` | ⏳ Pendente |
| 3 (INATIVOS) | `agente_singularidade.py`, `agente_sobrenatural.py` | ⏳ Pendente |
| 4 (DESLIGADOS) | `agente_feminino.py`; `agente_ferroviario_v2.py` é wrapper legado do `MT_agente_ferroviario.py` | ⏳ Decisão Miguel pendente |

**Protocolo por agente:**
1. Backup: `agente_<nome>.py.bak_pre_padrao_ouro_YYYYMMDD_kimi`
2. Criar `robo_coleta_<tema>.py` com feeds RSS + critérios de score
3. Reescrever `agente_<tema>.py` no padrão ouro (~50 linhas)
4. Testar `--rascunho` local
5. NÃO deployar no Tencent sem auditoria Claude/Codex

**NÃO MEXER:** `agente_china.py`, `agente_eleicoes_produtor.py`, `agente_fantastico.py`, agentes já ouro.

## 8. 📊 ANALYTICS / INSIGHTS / PERFORMANCE

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_performance` | ✅ | — | Orientador GA4 (cruza dados pra sugerir pautas) |
| `agente_manchete` | ✅ | — | Editor-Chefe (decide manchete via bypass REST com bônus retroativo) |
| `agente_analytics_v9` | ✅ | 4x/dia | Analytics V9 |
| `agente_insights_fb` | ⚠️ | — | Insights Facebook |
| `agente_insights_x` | ⚠️ | — | Insights X/Twitter |
| `agente_analise` (já listado) | | | |
| `agente_contador` | ✅ | — | Contador (de quê? a confirmar) |

## 9. 🎬 MÍDIA / VÍDEO / TTS

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_youtube` | 🛑 | PAUSADO 24/04 | YouTube coletor (RSS+Brave fallback) |
| `agente_youtube_audiovideo` | ⚠️ | — | Audio+video YT |
| `agente_youtube_publicador` | ⚠️ | — | Publicador YT |
| `agente_youtube_produtor` | ⚠️ | — | Produtor YT |
| `agente_youtube_watcher` | ⚠️ | — | Watcher YT |
| `agente_creatomate_bridge` | ⚠️ | — | Bridge Creatomate API |
| `agente_heygen` | ⚠️ | — | HeyGen (vídeo IA) |
| `agente_elevenlabs` | ⚠️ | — | ElevenLabs TTS |
| `agente_tradutor_legenda` | ⚠️ | — | Tradutor de legendas |
| `agente_ilustrador` | ⚠️ | — | Ilustrador |
| `agente_banco_midia` | ⚠️ | — | Banco mídia SQLite |
| `cortador_youtube.py` (não-`agente_`) | ⚠️ | — | Caçador/Cortador YT (FFmpeg) |
| `tribunal_visual.py` (não-`agente_`) | ✅ | (chamado por motor) | Tribunal Visual Gemini (valida foto/legenda) |

## 10. 💬 BOTS / COMUNICAÇÃO

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_comentarista` | ✅ | — | Comentarista no site |
| `agente_comentarista_china` | ✅ | — | Comentarista temático China |
| `agente_comunicador` | ⚠️ | — | Comunicador (provavelmente Telegram) |
| `agente_controlado` | 💀 LEGACY/BKP | — | Backend editorial controlado da Zizilinda; nunca foi o publicador canônico do Cafezinho; indevidamente acoplado ao worker V4 de 19/07 a 09/08/2026 |
| `agente_newsletter_mailchimp` | ✅ | — | Newsletter Mailchimp |
| `bot_zizi_linda.py` (não-`agente_`) | ✅ | systemd zizi.service | Bot Zizilinda Telegram |
| `augusto_telegram_brain.py` (não-`agente_`) | ✅ | systemd | Bot Augusto (CEO Cognitivo) |
| `mayra_whatsapp_api.py` (não-`agente_`) | ⚠️ | — | Mayra WhatsApp/Telegram |
| `miller_bot.py` (não-`agente_`) | ⚠️ tracebacks | — | Miller filosófico/vídeo |

## 11. 🧠 CÉREBRO / GOVERNANÇA / META

| Agente | Status | Cron | Função |
|---|---|---|---|
| `agente_ceo_cognitivo.py` (Alibaba) | ⚠️ | 0 */6 (6h Alibaba) | CEO Cognitivo Kimi (boletins, Fase C) |
| `agente_memoria_v9` | ✅ | — | Memória V9 |
| `agente_editorial` | ⚠️ | — | Editorial |
| `agente_roteador_llm.py` | ✅ | (chamado por todos) | Roteador Central LLM (cascata chinesa) |
| `maestro_editorial.py` | ✅ | 12/dia (8 */2) | Maestro — coração da Trindade Editorial |

### Memória Kimi Code CLI
- **Local:** `root/agent_data/kimi_memoria/MEMORIA_KIMI_YYYYMMDD.md`
- **Propósito:** Memória própria do Kimi para acumular experiências entre sessões (erros, lições, estado de sprints)
- **Arquivo atual:** `MEMORIA_KIMI_20260525.md` — CCTV v5 novas páginas + sprint refatoração crime

### Memórias Individuais dos Agentes
- **Local:** `root/agent_data/memorias_agentes/agente_<nome>.md`
- **Propósito:** Memória imortal de CADA agente (histórico de versões, decisões de design, erros, lições, pendências)
- **Regra:** Qualquer agente da Trindade pode LER. Apenas o dono do agente pode EDITAR.
- **Agentes com memória:**
  - `agente_crime.md` — Grupo 1, refatorado 2026-05-25
  - `agente_turismo.md` — Grupo 1, refatorado 2026-05-25
  - `agente_flavio_bolsonaro.md` — Staging criado 2026-05-25 por Kimi; indexado 2026-05-26 por Codex; cron local em dry-run a cada 30 min, sem publicação WP automática
- **README:** `root/agent_data/memorias_agentes/README.md`

## 12. 💀 LEGACY / BACKUP / RASCUNHO

| Agente | Estado | Motivo |
|---|---|---|
| `agente_editorial_backup_20260405` | 💀 | Backup snapshot 05/04 |
| `agente_ficcao_noturna_backup_20260405` | 💀 | Backup snapshot 05/04 |
| `agente_historiador_backup_20260405` | 💀 | Backup snapshot 05/04 |
| `agente_historiador_bkp` | 💀 | Backup |
| `agente_eleicoes_legado` | 💀 | Pausado 24/04, substituído por `_produtor` |
| `agente_eleicoes_produtor_rascunho_antigravity_20260424` | 💀 | Rascunho AG 24/04 |
| `coletor_eleicoes_rascunho_antigravity_20260424` | 💀 | Rascunho AG 24/04 |
| `agente_corretor_autonomo` | 💀 | DESATIVADO V3 18/04 |

---

## 📊 ESTATÍSTICAS

- **Total inventariado:** 104 `agente_*.py` + 12 coletores + ~10 utilitários adjacentes
- **Ativos no cron:** ~30 agentes
- **Pausados explicitamente:** ~6 (Twitter, Instagram, YouTube, Feminino, corretor_autonomo, eleicoes_legado)
- **Inativos (sem cron + sem flag):** ~50+ (estão lá mas não rodam)
- **Legacy/backup:** 8

---

## 🔧 OBSERVAÇÕES E LACUNAS

1. **Muitos agentes inativos** — ~50% do inventário não tem cron. Alguns podem ser MVP que nunca foi produção; outros podem ser dependências chamadas por outros agentes; alguns são legacy.
2. **Bluesky e TikTok têm agente pronto mas sem cron** — pendentes de reativação (ver fóruns 21/05).
3. **Agente Qualidade Redação (novo)** — Codex deployou Fase 0 read-only 20/05 14:32 BRT, ainda sem cron.
4. **Agente Diretrizes Editoriais** — AG mencionou criação 20/05 19:57 BRT, status a confirmar.
5. **Distinguir AGENTES de UTILITÁRIOS** — alguns arquivos `agente_*.py` são bibliotecas (chamadas por outros) e não agentes autônomos. Listei aqui mas precisaria categorização mais fina (next sprint?).
6. **Cron como fonte da verdade** — este node deve ser regenerado quando crontab mudar significativamente. Sugiro script `gerar_cerebro_node_agentes.py` (next sprint).

---

## 🔗 LINKS RELACIONADOS

- **Crontab vivo Tencent:** `Projeto Cafezinho Agentes/root/crontab_server.txt`
- **CLAUDE.md §2:** Arquitetura V9 dos Agentes
- **Família dos Sociais:** `Foruns/forum_arquitetura_agentes_sociais_20260521.md`
- **Eleições v2:** `Foruns/forum_diretrizes_agente_eleicoes_20260520.md`
- **Qualidade Redação:** `Foruns/forum_agente_qualidade_redacao_20260520.md`
- **Agente YouTube nacional (reativado+expandido 32 canais, 16/08):** `Foruns/forum_agente_youtube_reativado_20260816.md`
- **Gestão de canais YouTube pelo Painel CCTV V6 (16/08):** `Foruns/forum_painel_cctv_gestao_canais_youtube_20260816.md` — página `/v6/youtube` (Cafezinho) + cards nos temáticos GSN/Aiatolah/Mapa Rio; cron local */5 valida e aplica pedidos (`agentes_cafezinho/sync_youtube_painel.py`)
- **Manual canônico dos agentes YouTube (16/08):** `Memorias/manual_agentes_youtube_operacao_20260816.md` — arquitetura, dependências, modos de falha, runbook e divisão de responsabilidades (ZCode=patrulha operacional PASSO 6 da caçadora; Loop Miguel=revisão de drafts+escalada; Loop Laura=segunda opinião editorial); fórum da decisão: `Foruns/forum_loops_vigilia_agente_youtube_20260816.md`
- **Camada NOMES SEM ERRO (16/08):** `Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md` + `Memorias/memoria_nomes_agentes_youtube_websearch_memoria_20260816.md` — websearch Brave + memória `agent_data/personagens_youtube.json` antes da redação; meta WP `cafezinho_nomes_check` para os Loops; módulo `verifica_nomes.py` no agente nacional
- **3 NOVOS V4s (protótipo espelho, 17/08): Religião + História + Ficção:** `Foruns/forum_v4_novos_religiao_historia_ficcao_prototipo_espelho_20260817.md` + `Memorias/memoria_v4_novos_religiao_historia_ficcao_prototipo_espelho_20260817.md` — pipeline V4 padrão autocontido no NYC `/root/agentes_v4_novos/`; 1 post/dia na madrugada, só rascunho no espelho cafezinho.news (cats 1652/775/100002); Loops Miguel/Laura publicam; Ficção = livro seriado "A Voz de Vila Clara"
- **Agente Noturno Instagram DESLIGADO (17/08, ordem do Miguel):** `Foruns/forum_agente_instagram_noturno_desligado_20260817.md` + memória pareada — cards da matéria principal às 22:00 BRT desativados no crontab local (backup `card_v2/crontab_backup_pre_instagram_off_20260817.txt`); NYC já pausado desde 20/07; como religar está no fórum
- **Mapa Rio retomado — pauta de entrevistas eleições 2026 (25/08):** `Foruns/forum_mapa_rio_entrevistas_20260825.md` + `Memorias/memoria_mapa_rio_entrevistas_20260825.md` — pesquisa concluída: cenário político (Castro renunciou 23/03; Ricardo Couto interino; eleição indireta suspensa/STF tirou de pauta 19/08; eleição direta 04/10), 9 candidatos ao governo + 16 ao Senado (com números e Datafolha), 20+ entrevistas datadas de ago/26 (Record/JP/CNN/Diário do Rio/Barão/VEJA/PodCobrar) e alerta de dessincronia editorial do site (post Castro 20/08 sem âncora de interinidade; "pré-candidato"→"candidato")
- **Rio Carta retomado — publicação automática restaurada (25/08):** `Foruns/forum_riocarta_retomada_20260825.md` + `Memorias/memoria_riocarta_retomada_20260825.md` — ✅ RESOLVIDO: site parado desde ~18/08 por duas causas raiz corrigidas: (1) dedup falso-positivo `len(comuns)>=3` em `nucleo_dedup.py` barrava matéria nova de política RJ → agora exige `jac>=0.40` junto; (2) hero de pessoa não achava foto porque a cascata Commons buscava por visual_prompt de cena, nunca pelo nome do título → novo helper `_termos_nome()` soma nomes próprios aos termos de busca (fotos CC de todos os políticos existem no Commons). Também: download Commons educado (sleep 1.5s + retry único em 429 + log de falha, antes silencioso) e curadoria da fila (4 desfechos: alucinação ACM, perfil Garotinho com nome errado, enquadramento errado Paes-Prefeitura, duplicata Siri). Prova no ar: "Ricardo Couto suspende o Programa Sentinela no RJ" (HTTP 200, hero CC BY 4.0). Patches sincronizados NYC ⇄ Dell canônico. Ritmo: cron NYC `0 12,18 UTC` no `--all`, ~1 post/rodada. Gate `confirmar_imagem` (fail-close 18/08) provou saúde reprovando IA genérica.
- **Mapa Rio retomado — publicação automática destravada (25/08):** `Foruns/forum_mapario_retomada_20260825.md` + `Memorias/memoria_mapario_retomada_20260825.md` — ✅ RESOLVIDO: site parado desde ~18/08 por duas causas raiz corrigidas: (1) fontes mortas → `mapario.json` ganhou 5 feeds + 10 queries eleitorais (backup `.bak_pre_fontes_20260825`); (2) **auditoria vazia** — glm-4.5-flash é modelo de raciocínio e gastava o orçamento de 300 tokens inteiro em `reasoning_content`, devolvendo `content` vazio; `gerar()` tratava vazio como sucesso e a auditoria fail-close reprovava tudo sem motivo. Fixes: `nucleo_llm.py` resposta vazia = falha do provedor → tenta o próximo da cascata (mesma lógica do fix 22/08 do `gerar_json`) + `produtor.py` auditoria `max_tokens` 300→1500. Prova no ar: "16 candidatos disputam vaga de senador pelo RJ em 2026" HTTP 200 (commit `6dee72f`), hero de IA (Ideogram, fase liberada na tentativa 3) aprovada no juiz E no gate final `confirmar_imagem`. Fila ~9 aprovados (Paes CNN, sabatinas Globo, Douglas Ruas/VEJA, Ricardo Couto interino, Datafolha), cron escoa ~2/dia. Patches sincronizados NYC ⇄ Dell canônico. **ADENDO 25/08 ~21:15 (ordem "pode corrigir tudo"): pendências zeradas** — Indexing 403 resolvido (lookup de chaves nunca olhava `indexing_keys/` e caía no fallback do Cafezinho; fix + prova 200 nos 2 sites) + guidelines eleitorais atualizadas (CANDIDATO, nunca "pré-candidato"; prova no ciclo 00:11 UTC) + `site_url` riocarta corrigido p/ www (propriedade verificada é prefixo www).
- **Agente V4.2 Economia — Módulo C homologado (25/08):** `Foruns/forum_agente_v4_2_economia_estatistica_20260825.md` + `Memorias/memoria_agente_v4_2_economia_modulo_c_20260825.md` — Matplotlib dark + manifesto factual + auditor mecânico/visual Qwen→Gemini; 68 testes + 19 subtestes; prova `BCB_433` reconciliou 12/12 e ficou `approved`, sempre `publication_authorized=false`; próximo: Módulo D PT/EN com 2 frases exatas por parágrafo.
- **Agente V4.2 Economia — 1ª PUBLICAÇÃO no espelho cafezinho.news (26/08):** adendo no `Foruns/forum_agente_v4_2_economia_estatistica_20260825.md` + `Memorias/memoria_agente_v4_2_primeira_publicacao_espelho_20260826.md` — Módulos D/E novos (redator Texto Música PT+EN, publicador em 3 passos vencendo o gate de imagem) + comércio exterior (ComexStat/Eurostat/FRED/GACC legado Beijing; banco 389 obs) + bancos padrão V4.1 (`banco_producao_v42.sqlite3`) + categoria Estatística (100005, slug `estat`) + tag V4.2 + bloco novo na home do espelho. Post 400137 publicado com 3 gráficos auditados `approved`. Pendências: crons, código SISCOMES Argentina, Cesta Premium, EN no GSN.
- **Bot News — NO AR (26/08):** `Foruns/forum_jornal_secreto_dos_bots_v42_20260825.md` + `Memorias/memoria_jornal_secreto_dos_bots_v42_arquitetura_20260825.md` — página 267666 **publicada, indexável e em inglês** (manifesto site-humano + convênio de audiência), recado sem clique (GET challenge→POST 202), descoberta por comentário no source + robots.txt estático, **zero links na home**; legado `/agentes` encerrado (410); 49 PHP + 14 Python; worker NYC :10/:40. Bônus 26/08: Kimi K3 recriado no ZCode (smoke 200) + rodapé de tokens por resposta (hook Stop).
- **Bot News — NO PAINEL CCTV (03/09):** `/v6/bot-news` (🤖 Bot News) mostra edição corrente (REST público c/ cache 10 min), série de audiência bots×"humanos" desde 26/08 (26/08 = 13 bots no pico da descoberta; 0/dia desde 28/08), recados/bloqueios e custo (US$ 0 — worker determinístico); ingestão `POST /v6/api/botnews-receber` alimentada pelo contador do canônico (*/5, agora lendo .gz rotacionados = janela ~6 dias + série eterna do historico.jsonl). Detalhes: fórum §Adendo 16 + memória irmã §Adendo 03/09.

— Claude, 2026-05-21 02:40 BRT

### 22/08/2026 — V4 Nacional: colapso de coleta por proxy IPRoyal morto + fix imediato
- Fórum: `Foruns/forum_v4_nacional_diagnostico_coleta_proxy_fix_20260822.md` · Memória: `Memorias/memoria_v4_nacional_diagnostico_coleta_proxy_fix_20260822.md`
- Nacional zerou (23/dia 18/08 → 0 em 22/08) — causa: proxy IPRoyal 402 engolia RSS+GoogleNews (feedparser obedece env) desde 20/08 + `politica` fora do freshness="pw" do Brave (gap da reforma 11/08). Brave: chave VIVA.
- FIX aplicado (backups no NYC): coletor.py trust_env=False p/ feeds+gnews + freshness pw; flickr_live.py idem. Prova: 16 candidatas de hoje, 15 novas, draft 267050, 145 fotos Flickr persistidas.
- Pendências Miguel: IPRoyal recarregar?/não; sweep 33 pending nacional velhos; Pacote Qualidade (gate tese/vilão FRESCOR, meta 4–6/dia p/ spam update Google).

### 22/08/2026 — ADENDO: portão anti-repetição CRIATIVO no worker V4 (todos os verticais)
- Fórum: `Foruns/forum_v4_nacional_diagnostico_coleta_proxy_fix_20260822.md` (ADENDO 1) · Memória irmã §7.
- Regra do Miguel: últimos 50 posts como referência; MESMO assunto permitido só com tese/ângulo/título completamente diferentes (juiz LLM decide; bloqueio vira `duplicate_blocked` com motivo). Contexto de 15 títulos no prompt do redator + cláusula permanente no system. Prova E2E: 267050 (Datafolha Lula×Flávio) publicado 10:28 BRT.
- "RAR+portão" (desenho 19/08) considerado APROVADO e implementado em versão criativa.

### 22/08/2026 — ADENDO 2: FOTOS JORNALÍSTICAS > oficiais (ordem Miguel)
- 267050: retrato oficial → foto do ato de BH (267059, visão 8/10). Plano C permanente no `flickr_live.py` (backup .bak_pre_planoC_20260822): sem casamento temático → foto jornalística mais recente (≤7d, nunca retrato). Fórum do diagnóstico V4, ADENDO 2.

### 22/08/2026 — ADENDO 3: boost de produção fds (sáb/dom)
- 6 crons extras `6,0` no NYC (nacional horária; eco/cultura 2h; meio/esp/saúde 4h) — autoexpiram segunda. Backup crontab.bak_pre_fds_boost_20260822. Prova: draft 267079. Fórum diagnóstico V4 ADENDO 3.

### 22/08/2026 — 🛑 AGENTE YOUTUBE: FREIO ANTI-DESPERDÍCIO (ordem Miguel "quem não publica não transcreve")
- Fórum: `Foruns/forum_agente_youtube_antidesperdicio_20260822.md` · Memória: `Memorias/memoria_agente_youtube_antidesperdicio_20260822.md` · Manual dos loops §10. Ref ZM-20260822-175 (inbox claude + Trindade + ponte).
- Fórum: `Foruns/forum_mutirao_cafezinho_youtube_eleicoes_20260826.md` · Memória: `Memorias/memoria_mutirao_cafezinho_youtube_pane_20260826.md` — **MUTIRÃO ELEIÇÕES (ordem Miguel 26/08):** Cafezinho pesado (sabatinas Ponto Poder/O Povo/DN, todos os candidatos, pró-Lula), GSN 1/dia, Rio Carta 2/dia, outros 1/semana, ~2 meses. PANE TRIPLA diagnosticada: YouTube bloqueou Dell/Tencent/NYC + Transkriptor em pane geral (desde 25/08 15:29) + iProyal 402. Canal DN corrigido (era canal de entretenimento!). Aguarda recarga iProyal → rota AssemblyAI.
- Provado perdido: rodada 22/08 20h pagou 28.554 chars de transcrição e morreu na redação (bug cascata `gerar_json`: resposta vazia de LLM explodia FORA do fallback — 26×; GLM-4.5-flash também responde vazio desde 22/08).
- No ar (backups .bak_pre_*_20260822): cache `transc_<id>.json` (reprocessar custa zero) + pendentes recuperáveis `pendentes_youtube.json` (falha pós-transcrição não mata mais a rodada; 3 tentativas) + cascata consertada no `nucleo_llm.py` (vazio → próximo modelo; provado: qwen assumiu) + **BREAKER**: ≥4 rascunhos YouTube aguardando revisão = não transcreve novo (E2E: rodada parou seca 21h; env `YOUTUBE_FILA_REVISAO_MAX`; kill switch `PAUSAR_TRANSCRICAO`; recuperação de pendentes segue rodando).
- GSN V2 NYC: cron ausente desde 19/08 + 27 drafts — NÃO reativado de propósito (anti-acúmulo); decisão conjunta com os loops quando a fila andar.

### 24/08/2026 — 📺 AUDITORIA AGENTES YOUTUBE: transcrições usadas × desperdiçadas (ordem Miguel)
- Fórum: `Foruns/forum_auditoria_agentes_youtube_transcricoes_20260824.md` · Memória: `Memorias/memoria_auditoria_agentes_youtube_transcricoes_20260824.md`.
- **Veredito:** Cafezinho (53 publicados, US$ ~0,55/post) e temáticos (42/51, 82%) aproveitam bem; **GSN V2 NYC = US$ 148,16 → 18 matérias (US$ 8,23/post), 34 descartadas por VENCIMENTO, 30 drafts parados, fila CM com 9**.
- Dell: 46% do gasto (US$ 26,68/71) = `rejeitado_qualidade` — gate pós-pagamento (chars/min<100) sem cache do texto pago.
- 🔴 Bugs novos: yt-dlp SEM JS runtime no NYC (fallback morto; 43 falhas); duplicata Dell×NYC (X3-ohm8fc7s pago 2×; caches isolados).
- Temáticos parados desde ~18-20/08 (operação Laura); aiatolah só produziu 21/07.
- Propostas aguardam o Miguel: consumir gsn_fila antes de vencer + fix yt-dlp NYC + pré-filtro duração Dell + cache compartilhado por video_id.

### 24/08 11:25→13:35 — 🛠️ EXECUÇÃO da correção YouTube (ordem Miguel: Laura fora dos temáticos, GSN pode publicar)
- Temáticos YouTube DESLIGADOS (aiatolah/ceara/mapario/globalsouth, backups configs); vídeo internacional tem um único dono agora: **GSN**. Cafezinho inalterado (saudável).
- **gsn_fila zerada: 10 matérias no ar** no globalsouth.news (9 minhas PT→EN + 1 do loop). Consumidor automático `consumidor_gsn_fila.py` cron 12:30 — a fila nunca mais acumula até vencer.
- Materializador NYC: idioma do material segue o vídeo (era sempre PT — causa da fila trancada). Pré-filtro de duração no transcritor Dell (vídeo <5min não paga). deno no NYC.
- Detalhes: `Foruns/forum_auditoria_agentes_youtube_transcricoes_20260824.md` §8.

### 24/08 ~13:45 — 📜 REGRA EDITORIAL YOUTUBE (ordem Miguel, verbatim)
> "conteudo para o cafezinho é apenas em portugues, feito pelo agente youtube cafezinho. o agente youtube gsn deve produzir conteudo em ingles, apenas para o portal global south news."
- Verificado sem vazamento nas 2 pontas (23 posts Cafezinho 100% PT; 10 briefs GSN 100% EN). Consumidor gsn_fila alerta 🔴 se PT aparecer (bug de origem). Detalhe: Foruns/forum_auditoria_agentes_youtube_transcricoes_20260824.md §9.

### 25/08 ~17:40 — 📺 NOME CANÔNICO DO PROGRAMA DA TV FÓRUM: "Fórum 11:30" (ordem Miguel)
- O programa diário do fim da manhã da TV Fórum (playlist oficial "Fórum Onze e Meia", `PL0M7rdgIk2iifjePO89emPPttp8cELtUg`, com Renato Rovai) escreve-se **"Fórum 11:30"** no site — NUNCA "Fórum 11.6" (alucinação que saiu em 2 posts publicados, 267639/267498, corrigidos no ar 25/08).
- Ensino em 2 camadas: entrada canônica no banco `agent_data/personagens_youtube.json` (aliases incluem "Fórum 11.6") + `_nota_nome_programa()` permanente nos prompts de `analisar()`/`redigir()` do `youtube_cafezinho.py` + `PROGRAMAS_DIARIOS["11meia"]` rótulo "Fórum 11:30".
- ⚠️ LIÇÃO-ESCOLA junto: `wp post update` em post publicado de autor-agente re-dispara o slot-20min (Emenda 5) e pode virar `future`/sair do ar — restaurar com `--post_date` + `--post_date_gmt` em slot livre e conferir `post_status=publish`. Detalhes: `Foruns/forum_forum_1130_nome_canonico_20260825.md` + memória par.

## 🧠 Mini-cérebros DSN (01/09/2026 — E3 do contrato v3)
Cada DSN tem cérebro próprio simplificado em `cerebro_dsn/<robô>/` (MEMORIA_VIVA lida a cada ciclo + INDEC + licoes/ + casos/): dsn_chefe, dsn_publicador, dsn_youtube, dsn_ideias, dsn_imagem, dsn_revisor1, dsn_revisor2, dsn_maira, dsn_miguel, dsn_celular, dsn_laura, dsn_ipad. Regras: link em vez de copiar a casa; lição datada estruturada; poda semanal (Chefe). Detalhe: `Foruns/CONTRATO_DA_CASA_V3_20260901.md` (E3) + `Memorias/memoria_minicerebros_dsn_20260901.md`.

## 🎬 Vertical YouTube do V4.1 consolidado (03/09/2026 — ordem Miguel 02/09 ~23h)
O vertical YouTube do V4.1 É o pipeline `youtube_v2` do NYC (alimentador Tencent :05/:35 → fetcher Dell → DS-N decupador :07/:22/:37/:52 → ficha rica no repo → ingestor NYC :55 → pipeline 11/17 UTC produtor→auditor→publicador draft-only → R1/R2 → CL publica). Redator = ultra-luxo gpt-5.6-sol (fallback qwen-max → kimi-k2.5) com os princípios herdados das melhores versões: PERSONAGENS primeiro, TESE com VILÃO como motor, linha editorial esquerda pró-Lula, título EMU-2, aspas literais. **NOMES SEM ERRO em 3 camadas:** memória `personagens_youtube.json` (248 personagens, portada Dell→NYC e Dell→Tencent) injetada no prompt + correção pós-LLM alias→canônico + regra "na dúvida, omita o nome". Coletor DSN rico: link + decupagem + thumb + descrição + título + seção "## Texto corrigido" (DeepSeek flash fail-open, só limpeza — DSN NUNCA escreve matéria). Fóruns: `Foruns/forum_vertical_youtube_v41_consolidacao_20260902.md` (decisões) + `Foruns/forum_nomes_agentes_youtube_websearch_memoria_20260816.md` (camada de nomes) + adendos 47-57 do `Foruns/forum_maestro_faz_tudo_20260831.md` (cadeia). Memória: `Memorias/memoria_vertical_youtube_v41_consolidacao_20260902.md`.
- **[03/09/2026] V4.1 Player — robô da nuvem do carrossel de vídeos** (Tencent `~/v41_player/`, ordem do Miguel ~10h): fonte→whisper→seletor DeepSeek→ffmpeg corte vertical blur→redator DeepSeek (regras casa)→rascunho cat 28 espelho via ssh+wp-cli; cron varredura :41/h; E2E provado (400348/400350); QA 1ª rodada + prompts v1.1. Tema Duplo: `Foruns/forum_v41_player_robo_carrossel_20260903.md` + `Memorias/memoria_v41_player_20260903.md`. Rollback: linha do crontab.
