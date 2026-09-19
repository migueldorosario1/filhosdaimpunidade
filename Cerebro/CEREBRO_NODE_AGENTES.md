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
- **Painel /v6/youtube REFORMADO (05/09 noite, ordem Miguel):** abas Publicado/Rascunho viraram tabela com 4 colunas — **Onde foi publicado** (☕ Cafezinho + chips GSN/Rio Carta/Mapa Rio por vídeo via ledger) · **Link público REAL confirmado** (`https://ocafezinho.com/AAAA/MM/DD/slug/`, nunca o domínio `controle.`; HTTP 200 ao vivo com UA navegador, cache 10 min) · **Transcrição por** (🤖 Whisper local / 📹 legenda do YouTube / 🎙️ Transkriptor — lidos da pasta `~/ds_youtube/artifacts/<vid>/` e do ledger de custos; comparação case-insensitive porque o WP grava filename da capa em minúsculas). Novo modo `cat28` no `transkriptor_status.php` (ADITIVO). Detalhes: `Foruns/forum_painel_youtube_reforma_20260905.md` + `Memorias/memoria_painel_youtube_reforma_20260905.md`.
- **[03/09/2026] V4.1 Player — robô da nuvem do carrossel de vídeos** (Tencent `~/v41_player/`, ordem do Miguel ~10h): fonte→whisper→seletor DeepSeek→ffmpeg corte vertical blur→redator DeepSeek (regras casa)→rascunho cat 28 espelho via ssh+wp-cli; cron varredura :41/h; E2E provado (400348/400350); QA 1ª rodada + prompts v1.1. Tema Duplo: `Foruns/forum_v41_player_robo_carrossel_20260903.md` + `Memorias/memoria_v41_player_20260903.md`. Rollback: linha do crontab.

## 🔄 Ronda ZM 1/1h do ecossistema (03/09/2026 — ordem Miguel ~13h; VIGIA desde ~15:5x)
Automação ZCode automation-877aeabb (cron 5 * * * *, âncora :05): engaja o ZM no loop Laura×Miguel (mesmo com loop_ativo=laura, sem violar ofícios do contrato), fila DSC-024 do Telegram do Miguel (3º, rede de segurança ~1h), ponte ZM↔us65 (refs ZD), DSNs todos (relatórios do Chefe + caixa_agentes.jsonl do Tencent como rede de segurança) e provas de vida dos robôs Telegram (@Dsnchefe_bot, @Dsnfinancas_bot, bot news). Tema Duplo: `Foruns/forum_ronda_zm_loop_ecossistema_20260903.md` + `Memorias/memoria_ronda_zm_loop_ecossistema_20260903.md`.
- **[03/09 15:5x→16h] REENCARNAÇÃO VIGIA — RONDA ZM VIGIA 1/1h** (ordem Miguel ~15:5x; a ronda de script foi desligada 15:13 na reforma da grade): automação de AGENTE `automation-2a8954e2` (cron `12 * * * *`, âncora :12) — pontes Laura + **Telegram do Miguel** (escuta `conversa_48h.jsonl` + saúde do serviço `ponte_cafezinho`) + DSC (caixa tencent + ZD) + **ajuda técnica ao CL/Clodo de Lara** (inbox claude + canal_trindade, atendida do Dell) + **vigilância do sistema em pé** (CCTV `http://43.156.151.165/v6/` no Tencent, canônico, espelho, uptime tencent/nyc, provas de vida dos robôs) + **PODER de correção direta de coisa SÉRIA** (prova→backup→mínima→prova→registro; nunca post publicado/esteira CL-CM). Telegram ao Miguel SÓ com novidade (grade enxuta). Tema Duplo: `Foruns/forum_ronda_zm_vigia_1h_20260903.md` + `Memorias/memoria_ronda_zm_vigia_1h_20260903.md`. Rollback: CronDelete.


AST-20260905-017 — 05/09/2026 10:41:36 BRT: leitura efetiva V3/anexos, funções e auditoria Telegram documentadas em Foruns/PROPOSTA_ADENDO_ASTRA_V3_E_ATIVACAO_20260905.md; memória Memorias/MEMORIA_ASTRA_V3_TELEGRAM_20260905.md; prompt único Foruns/PROMPT_UNICO_ATIVACAO_ASTRA_V3_20260905.md. Miguel dispensou revisão prévia DSN/ZM apenas da ronda: autorização não está pendente. Adendo continua PROPOSTA; suplência pode seguir protocolo previamente autorizado, sem licença humana por ocorrência, respeitando ordem, escopo e exclusividade. Astra não é XM e não publica. Registro manual das decisões Telegram realizado; incorporação automática/controles novos ainda pendentes. Ronda desativada, Telegram ativo; nenhum cron, serviço alheio ou produção alterado.


<!-- AST-INSTITUCIONAL:MANUAL-INTEGRACAO-20260905-1120 -->

AST-20260905-019 | 2026-09-05T11:20:50-03:00 | Controles implementados e análise real validada; ativação é a próxima etapa

Tarefa: AST-PEDIDO-3079a8327006c038fa4a. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/MANUAL-INTEGRACAO-20260905-1120.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-79. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260905-018-ATIVACAO -->

AST-20260905-018 | 2026-09-05T11:42:54-03:00 | Configuração horária Astra ativada às 11h39; primeira rodada prevista às 12h

Tarefa: AST-CONFIGURACAO-HORARIA. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-018-ATIVACAO.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-120001-1788620401869890846 -->

AST-20260905-020 | 2026-09-05T12:01:15-03:00 | Rio: reconciliação da margem de disco e plano de medição estrutural

Tarefa: AST-RIO-ESTUDO. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-120001-1788620401869890846.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-20260905-023:INTEGRACAO-RECEBIDA -->

AST-20260905-023 | 2026-09-05T15:13:29-03:00 | Miguel autorizou integração do atendimento Telegram ao Cérebro, memória mínima e fila própria. Tarefa reservada no monitor; implementação/testes em andamento. Ronda temporariamente desabilitada; Telegram preservado. Sem ampliar permissões, publicar, excluir ou gastar. Fórum: cerebro/Foruns/FORUM_ASTRA_TELEGRAM_CEREBRO_20260905.md. O questionário antigo reenviado é registro histórico, não mudança de agenda.


<!-- AST-INSTITUCIONAL:AST-20260905-023-INTEGRACAO-FINAL -->

AST-20260905-023 | 2026-09-05T15:40:07-03:00 | Astra: atendimento integrado e ronda reativada

Tarefa: AST-INTEGRACAO-TELEGRAM-CEREBRO. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-023-INTEGRACAO-FINAL.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-CORRECAO-16H-20260905 -->

AST-20260905-024 | 2026-09-05T16:47:19-03:00 | Astra: corrigida a rejeição de fonte da ronda16h

Tarefa: AST-CORRECAO-SNAPSHOT-16H. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-CORRECAO-16H-20260905.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-170001-1788638401308511441 -->

AST-20260905-025 | 2026-09-05T17:01:15-03:00 | Incidente da ponte: leitura reconhecida e critério de proteção reconciliado

Tarefa: AST-PEDIDO-971deed9666f773ee74e. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-170001-1788638401308511441.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-39f76fd617a889ef8bd3f59b. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260905-180001-1788642001506513381 -->

AST-20260905-026 | 2026-09-05T18:01:17-03:00 | Google Drive: o que ficou pendente e como explicar nas rondas

Tarefa: AST-PEDIDO-9e9195efa2dcf39d04df. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-180001-1788642001506513381.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-107. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260905-190001-1788645601275426901 -->

AST-20260905-027 | 2026-09-05T19:01:23-03:00 | Rio: diagnóstico aguarda medições de crescimento e custos

Tarefa: AST-RIO-ESTUDO. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-190001-1788645601275426901.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-200001-1788649201577796545 -->

AST-20260905-028 | 2026-09-05T20:01:22-03:00 | TG-112: minuta para revisão da limpeza do Rio

Tarefa: AST-PEDIDO-cbfe312ab2587203fff8. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-200001-1788649201577796545.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-112. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-DRIVE-REPARO-20260905 -->

AST-20260905-029 | 2026-09-05T20:25:51-03:00 | Drive: transporte corrigido; quota compartilhada ainda impede regularização

Tarefa: AST-DRIVE-REPARO-20260905. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-DRIVE-REPARO-20260905.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-ACESSOS-TELEGRAM-20260905 -->

AST-20260905-030 | 2026-09-05T20:37:12-03:00 | Acessos conferidos e prompt de integração Telegram preparado; operação WordPress não ativada

Tarefa: AST-ACESSOS-TELEGRAM-PROMPT. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-ACESSOS-TELEGRAM-20260905.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-210001-1788652801646419848 -->

AST-20260905-032 | 2026-09-05T21:02:08-03:00 | TG-115: prompt de retomada do Google Drive atualizado

Tarefa: AST-PEDIDO-4f47a3182e828e61bef6. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-210001-1788652801646419848.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-115. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-WP-SSH-20260905 -->

AST-20260905-031 | 2026-09-05T21:14:38-03:00 | Acesso direto WP/SSH testado; post269165 pending; contas restritas aguardam aprovação

Tarefa: AST-ACESSO-DIRETO-WP-SSH. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-WP-SSH-20260905.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-ACESSOS-ADMIN-DECISAO-20260905 -->

AST-20260905-033 | 2026-09-05T21:30:41-03:00 | Miguel dispensa contas restritas; Astra mantém acessos administrativos existentes

Tarefa: AST-ACESSOS-ADMIN-DECISAO-20260905. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-ACESSOS-ADMIN-DECISAO-20260905.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-220002-1788656402160366602 -->

AST-20260905-035 | 2026-09-05T22:01:30-03:00 | Patrocínio: ficha do piloto e cálculo de preço para decisão

Tarefa: AST-PATROCINIO-PREPARO. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-220002-1788656402160366602.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260905-230002-1788660002198733355 -->

AST-20260905-036 | 2026-09-05T23:01:36-03:00 | Patrocínio: critérios de aceite e tratamento de entrega incompleta

Tarefa: AST-PATROCINIO-PREPARO. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260905-230002-1788660002198733355.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260906-000001-1788663602026829104 -->

AST-20260906-019 | 2026-09-06T00:01:35-03:00 | Drive: correção de orientação reconhecida; trabalho técnico permanece com Claude Miguel

Tarefa: AST-PEDIDO-0c775fc2b463cd593a5b. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-000001-1788663602026829104.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-5fa2da3018eba523b6801cc8. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-080002-1788692402121813633 -->

AST-20260906-020 | 2026-09-06T08:01:38-03:00 | Parecer sobre geopolítica: retomada comprovada por relatos, cura estrutural ainda sem prova

Tarefa: AST-PEDIDO-4ac765a7c1db000c65e5. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-080002-1788692402121813633.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-698881913b73c58fbe4ac65a. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-090001-1788696001905438261 -->

AST-20260906-021 | 2026-09-06T09:01:34-03:00 | Patrocínio: separar apoio identificado de promoção de produto

Tarefa: AST-PATROCINIO-PREPARO. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-090001-1788696001905438261.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260906-100001-1788699601450852500 -->

AST-20260906-022 | 2026-09-06T10:01:41-03:00 | Audiência: quais dias compõem a alta de 1,34%

Tarefa: AST-AUDIENCIA-ANALISE. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-100001-1788699601450852500.md). Sem publicação, produção, exclusão ou despesa nova.


<!-- AST-INSTITUCIONAL:AST-20260906-110001-1788703201467653612 -->

AST-20260906-023 | 2026-09-06T11:03:17-03:00 | TG-133: identificar os medidores e esclarecer os registros pendentes

Tarefa: AST-PEDIDO-1c55829011dd6e77c6fb. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-110001-1788703201467653612.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-133. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-120001-1788706801302822787 -->

AST-20260906-024 | 2026-09-06T12:01:42-03:00 | CL-008: curadoria reconciliada com a migração já concluída

Tarefa: AST-PEDIDO-d59f2a64f508d83c6eaa. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-120001-1788706801302822787.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-3b0cd0fadba0f1b0d203322b. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-DRIVE-MANUAL:2026-09-06T12:36:12-03:00 -->

AST-20260906-025 | 2026-09-06T12:36:12-03:00 | Recuperação das cópias Drive e correção do Manual

Resultado concreto: recuperador explícito passou a incluir o preflight externo com origem/hash fixos; avisos distinguem andamento de conclusão e entregam próximo passo/prompt. 187 testes da ronda e 45 do atendimento passaram. Manual corrigido conforme CM-005, §10 e CL-008/009: memória coletiva é do Presidente em exercício, atualmente CL; ZM conserva curadoria técnica. Histórico preservado.

Drive NÃO regularizado: 20 entregas da fila + 1 preflight requerem reconciliação; seis arquivos têm recibo histórico de gravação, não são presumidos ausentes. Nenhuma análise refeita, nenhuma cópia GitHub/Tencent reenviada. Último erro comprovado: quota de requisições por minuto do projeto. Espera local vigente até 06/09 13h02min19,770936s BRT, sem garantia de liberação. Teste manual 12h33min37s confirmou recuo antes da rede. Próxima ronda prevista 13h; cron único e pausa preservados.

Inventário por arquivo/hash, testes, fontes, reversão e prompt para colar no Claude Code: cerebro/Foruns/FORUM_ASTRA_COPIAS_DRIVE_E_MANUAL_20260906.md. Não pedir token pelo chat, não alterar gdrive compartilhado nem serviços de colegas. Estado: correção local concluída; confirmação do Drive pendente. Registro informativo, sem disparar conversa automática e sem closes_ref de entrega não concluída.


<!-- AST-INSTITUCIONAL:AST-20260906-130001-1788710401330423135 -->

AST-20260906-026 | 2026-09-06T13:01:38-03:00 | TG-138: recado claro sobre o Manual Astra e as cópias no Drive

Tarefa: AST-PEDIDO-d2672792bdf26beada42. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-130001-1788710401330423135.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-138. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-140002-1788714002319049675 -->

AST-20260906-027 | 2026-09-06T14:01:33-03:00 | CL-009: limites da cobertura e provas da rotação da memória

Tarefa: AST-PEDIDO-5115934949d1b2f93a2e. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-140002-1788714002319049675.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-2cb96aae77681780c65a3fa6. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-150001-1788717601750077594 -->

AST-20260906-028 | 2026-09-06T15:01:23-03:00 | CL-009: anúncio repetido de migração já analisada

Tarefa: AST-PEDIDO-06d9a95008aa5cb72393. Resultado da análise: no_change. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-150001-1788717601750077594.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-b30d67a3df604ee70e929c61. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-160001-1788721201871842598 -->

AST-20260906-029 | 2026-09-06T16:02:14-03:00 | CL-010: pendências das 11h49 reconciliadas com os relatos da tarde

Tarefa: AST-PEDIDO-28cb009e354e6505e2cb. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-160001-1788721201871842598.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-f98206582429a0d9cee82677. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-170002-1788724802318104337 -->

AST-20260906-030 | 2026-09-06T17:01:45-03:00 | CL-012: pendências reconciliadas e duração da cobertura noturna corrigida

Tarefa: AST-PEDIDO-540941d9831df3fec470. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-170002-1788724802318104337.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-3cbb9dc29356d5f6da3abb28. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-180001-1788728402069410727 -->

AST-20260906-031 | 2026-09-06T18:01:43-03:00 | CL-011: correção do tutorial reconhecida e limite da checagem esclarecido

Tarefa: AST-PEDIDO-ae69ad24645a601898b1. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-180001-1788728402069410727.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-be3b5325ab77e45f5ac3f50b. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-190001-1788732002138280572 -->

AST-20260906-032 | 2026-09-06T19:01:47-03:00 | CL-014: previsão de escassez superada; correção do coletor segue sem prova

Tarefa: AST-PEDIDO-c603dfb75dbba21b4227. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-190001-1788732002138280572.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-4f48752b9835f6923c943b44. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-200001-1788735601894644717 -->

AST-20260906-033 | 2026-09-06T20:01:57-03:00 | CL-013: aprovação de revisão não encerra retenção editorial

Tarefa: AST-PEDIDO-f00242dee04bb2b50365. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-200001-1788735601894644717.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-680ce3162f9bb58c080bc19e. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST034-REMOTO-EXCLUSIVO -->
AST-20260906-034 — Astra → AGY / ZM / Miguel  
06/09/2026, 20:55 BRT.

Remoto exclusivo parametrizado e selecionado no executor próprio. 253 testes offline aprovados; leitura real em gdrive-astra às 20:53:52 com hash registrado. Nenhum reenvio e nenhuma análise repetida. A fila permanece pendente: 28 outbox + preflight + avulso AST023. Avulso apenas com manifesto preparatório; ainda não é coberto pelo recuperador.

Remotos e serviços alheios intocados. Cron único e pausa preservados. Próximo passo: reconciliação coordenada por arquivo/hash; não tratar sucesso de leitura como recuperação da fila. Relatório: [AST-REMOTE-PARAM-20260906](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-REMOTE-PARAM-20260906.md).

— Astra · gpt-6-astra · 20260906 20:55 BRT


<!-- AST-INSTITUCIONAL:AST-20260906-210001-1788739201755618373 -->

AST-20260906-035 | 2026-09-06T21:03:34-03:00 | CL-016: critérios preparados para verificar formatação e categoria

Tarefa: AST-PEDIDO-0241a138348fa100f57c. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-210001-1788739201755618373.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-7ac46bf8fdba1a92210b8e27. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260906-220002-1788742802185965772 -->

AST-20260906-036 | 2026-09-06T22:02:55-03:00 | CL-015: omissões editoriais reconciliadas com o balanço do dia

Tarefa: AST-PEDIDO-9af82935fe51584e089b. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260906-220002-1788742802185965772.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-f118c4a1477f488458f47dd3. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-000002-1788750002262553950 -->

AST-20260907-019 | 2026-09-07T00:02:55-03:00 | CL-018: publicação prevista confirmada em relato posterior

Tarefa: AST-PEDIDO-a12f95ae0341c707fcec. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-000002-1788750002262553950.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-04d49098532ac94829ff321f. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-080002-1788778802603293685 -->

AST-20260907-020 | 2026-09-07T08:02:22-03:00 | TG-157: critérios de qualidade precisam acompanhar a reforma já em curso

Tarefa: AST-PEDIDO-a4fd0334890ea1a9872b. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-080002-1788778802603293685.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-157. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-090001-1788782401358522580 -->

AST-20260907-021 | 2026-09-07T09:01:44-03:00 | CL-017: título de Atoms reconciliado com correção posterior

Tarefa: AST-PEDIDO-1134be7e47d992d86e94. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-090001-1788782401358522580.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-77da498d9a105671a775c43d. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-100001-1788786001565805157 -->

AST-20260907-023 | 2026-09-07T10:01:44-03:00 | CL-020: reserva editorial de Miguel reconciliada com os relatos posteriores

Tarefa: AST-PEDIDO-83c30b1bd2e39c850e32. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-100001-1788786001565805157.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-9f324814a70111f1c31f5065. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-110001-1788789602049312023 -->

AST-20260907-025 | 2026-09-07T11:01:39-03:00 | CL-019: correção factual reconhecida e limites da revisão de vídeos

Tarefa: AST-PEDIDO-f492be2b43e7e49d22a1. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-110001-1788789602049312023.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-ba7d9a2c9ef7145904b96e62. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-RETOMADA-AUTOCURA-20260907 -->

## Ordem vigente de Miguel — 07/09/2026

Astra deve retomar a ronda com foco permanente em audiencia, qualidade jornalistica, aprendizado e ajuda a autocura. Horarios BRT:07,09,11,13,15,17,19,23,03; exatamente duas rondas noturnas entre21h e07h, separadas por4h. Um recado factual em cada rodada. Esta ordem substitui os horarios00h+08h–23h e a pausa integral da madrugada citados acima. Os outros loops preservam seu estado.

Em toda rodada: publicacoes1h/2h contra media comparavel; GA4,FAROL,LUMINA,SOL com frescor e detalhes por pagina/tipo/categoria/assunto; revisao de amostra conforme Bom Gosto; uma ideia e ajuda concreta aos responsaveis. Abaixo da media gera alerta; dados ausentes nao viram zero. Alertas sao deduplicados e exigem duas leituras validas para encerrar a condicao. Corrigir exige prova; proposta nao equivale a execucao.

Mandato e criterios: cerebro/Memorias/MEMORIA_ASTRA_RETOMADA_AUTOCURA_20260907.md. A agenda ainda depende do recibo de ativacao desta implementacao; esta nota nao e prova antecipada de disparo.


<!-- AST-INSTITUCIONAL:AST-ANALISE-INICIAL-AUTOCURA-20260907 -->

AST-20260907-026 | 2026-09-07T12:17:58-03:00 | CL-022 reconciliada: retenções preservadas e correções editoriais preparadas

Tarefa: AST-PEDIDO-302098bfaf7f5d9cc99b. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-ANALISE-INICIAL-AUTOCURA-20260907.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-caf00934faeb29ab64276d67. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-130002-1788796802401484083 -->

AST-20260907-027 | 2026-09-07T13:07:19-03:00 | CL-021 reconciliada: retenção explica volume menor; revisão ainda exige provas

Tarefa: AST-PEDIDO-f64af09d2d56ff805467. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-130002-1788796802401484083.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-cf0d1c4edface587d2c3f7dd. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-150001-1788804001765758145 -->

AST-20260907-028 | 2026-09-07T15:06:26-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-e76ed40c284dfd9940cc. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-150001-1788804001765758145.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-af6d8e0d6cc5a0495b91210b. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260907-170001-1788811201705713621 -->

AST-20260907-029 | 2026-09-07T17:06:34-03:00 | CL-024 reconciliada: correções reconhecidas e alerta de título inconsistente

Tarefa: AST-PEDIDO-c239a8fe6346aa890c03. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260907-170001-1788811201705713621.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-c9f8e1db2ff4ec0b9802b079. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-090001-1788868801778844735 -->

AST-20260908-019 | 2026-09-08T09:11:35-03:00 | CL-025 reconciliada: dengue publicada; revisão precisa ir além dos sinais automáticos

Tarefa: AST-PEDIDO-f19b86b04b60cfc719b1. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-090001-1788868801778844735.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-fdde205463c569e863a820bc. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-110001-1788876001802737735 -->

AST-20260908-020 | 2026-09-08T11:06:17-03:00 | CL-028 reconciliada; produção acima da média e revisão de pesquisas preparada

Tarefa: AST-PEDIDO-c8da3af1f6b109c69aaf. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-110001-1788876001802737735.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-0b0d0ec61f7546eab389ec5f. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-130002-1788883202389879389 -->

AST-20260908-021 | 2026-09-08T13:03:11-03:00 | CL-027 reconciliada: série publicada; volume menor exige conferir o disparo das 13h

Tarefa: AST-PEDIDO-905cadd45f74665aa9b7. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-130002-1788883202389879389.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-eed079e78382fee864892eaa. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-150001-1788890402025650296 -->

AST-20260908-022 | 2026-09-08T15:06:51-03:00 | CL-029 reconciliada: teste do escape de marcação preparado e revisão editorial atual

Tarefa: AST-PEDIDO-c01b3b6a9909a23e6822. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-150001-1788890402025650296.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-06e2c700610840207bfb3355. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-170002-1788897602352970757 -->

AST-20260908-023 | 2026-09-08T17:06:38-03:00 | CL-030 reconciliada; duas horas sem publicação exigem conferir o post 269476

Tarefa: AST-PEDIDO-ea6ea9740d12e050609d. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-170002-1788897602352970757.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-8acf72d76450757eeb0bcb31. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-190002-1788904802126720449 -->

AST-20260908-024 | 2026-09-08T19:06:07-03:00 | CL-030 reconciliada: produção retomada e revisão de pesquisas preparada

Tarefa: AST-PEDIDO-dcc89b2fe0feb7b1543a. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-190002-1788904802126720449.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-de407aac301415ec3234c4ae. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260908-230001-1788919201430278581 -->

AST-20260908-025 | 2026-09-08T23:06:19-03:00 | CL-032 reconciliada; produção recuperada e contradições editoriais identificadas

Tarefa: AST-PEDIDO-f9f53f80dffea35dd9a1. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260908-230001-1788919201430278581.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-6a5e10447f87083e1f63105d. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-030001-1788933601782040045 -->

AST-20260909-019 | 2026-09-09T03:04:02-03:00 | CL-031 reconciliada; volume noturno explicado e revisão editorial preparada

Tarefa: AST-PEDIDO-7a86d62ceb1d7650cc51. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-030001-1788933601782040045.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-b05d1764f0b2409a40d3292b. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-070002-1788948002240136352 -->

AST-20260909-020 | 2026-09-09T07:08:39-03:00 | CL-003 reconciliada: corte editorial esclarecido e disparo das 07h pendente de prova

Tarefa: AST-PEDIDO-1b590f7f900e80fc7a1d. Resultado da análise: needs_review. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-070002-1788948002240136352.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-024f8b264969d58abd35aa75. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-110002-1788962402212724956 -->

AST-20260909-021 | 2026-09-09T11:06:31-03:00 | CL-007 reconciliada: falha histórica sem causa comprovada; revisão atual preparada

Tarefa: AST-PEDIDO-b61b0326da0d59c59317. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-110002-1788962402212724956.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-1af51320f23e18019a7a7e4c. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-130001-1788969602098450104 -->

AST-20260909-022 | 2026-09-09T13:06:19-03:00 | CL-008 reconciliada: próxima candidata confirmada; disparo das 13h ainda sem prova

Tarefa: AST-PEDIDO-7c02095967f9e80a9acc. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-130001-1788969602098450104.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-22f8f05c92858c4715357527. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-150001-1788976802019453517 -->

AST-20260909-023 | 2026-09-09T15:06:12-03:00 | CL-005 reconciliada: fila preservada e correções de precisão preparadas

Tarefa: AST-PEDIDO-fc5ca4fc37df828706e6. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-150001-1788976802019453517.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-6479fe06f0ed5dfa77a1f49e. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-170002-1788984002223158652 -->

AST-20260909-024 | 2026-09-09T17:03:33-03:00 | CL-006: horário do agendador esclarecido; volume baixo explicado pela janela

Tarefa: AST-PEDIDO-8d8c178f2116f949f26f. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-170002-1788984002223158652.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-6ff2db41bc946c4a2959432d. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-190002-1788991202252069089 -->

AST-20260909-025 | 2026-09-09T19:04:14-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-3b5e9bf1720d536291fe. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-190002-1788991202252069089.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-9fa8cad1ac519f38fe0bd10a. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260909-230001-1789005601369972800 -->

AST-20260909-026 | 2026-09-09T23:04:22-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-e772b0dab3e90857b931. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260909-230001-1789005601369972800.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-a6ffa7d1d1e799280830ad50. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260910-030001-1789020001948715303 -->

AST-20260910-019 | 2026-09-10T03:04:28-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-881b160ab92d034f1abe. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260910-030001-1789020001948715303.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-dd349d6a99091ac44665dae9. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260910-070001-1789034401414255648 -->

AST-20260910-020 | 2026-09-10T07:06:43-03:00 | CL-004 reconciliada: revisão antes do agendamento e correções de precisão preparadas

Tarefa: AST-PEDIDO-436828d86816eab6735e. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260910-070001-1789034401414255648.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-e8225beecbed31383b58d1fa. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260910-090002-1789041602321071949 -->

AST-20260910-021 | 2026-09-10T09:06:25-03:00 | CL-011 reconciliada: retenção preservada, produção melhora e revisão preparada

Tarefa: AST-PEDIDO-bfbd8ee85edb04eb8aae. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260910-090002-1789041602321071949.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-4e4cde55a0cd2fe44656da2f. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260910-110002-1789048802266003597 -->

AST-20260910-022 | 2026-09-10T11:06:25-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-989a61fe034dfc18523a. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260910-110002-1789048802266003597.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-8e72d53463db587cdcb28ae9. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260910-130002-1789056002251886161 -->

AST-20260910-023 | 2026-09-10T13:07:03-03:00 | CL-010 respondida: auditoria semanal preparada e revisão de precisão encaminhada

Tarefa: AST-PEDIDO-5cbd8865b7cb276ad3b8. Resultado da análise: completed. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260910-130002-1789056002251886161.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-d533736e2c66a5c5df9ff90a. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260911-030002-1789106402171738874 -->

AST-20260911-019 | 2026-09-11T03:09:12-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-069f1f4cf20ad9768b31. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260911-030002-1789106402171738874.md). Sem publicação, produção, exclusão ou despesa nova.

ref: TG-193. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260911-070002-1789120802332960668 -->

AST-20260911-020 | 2026-09-11T07:04:18-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-ff981e0cbaf1d438c859. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260911-070002-1789120802332960668.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-3162860952a864050fb6ee3e. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.


<!-- AST-INSTITUCIONAL:AST-20260911-090001-1789128002005404834 -->

AST-20260911-021 | 2026-09-11T09:06:05-03:00 | Rodada interrompida com segurança

Tarefa: AST-PEDIDO-683118d87151e1182475. Resultado da análise: progress. [Relatório](https://github.com/migueldorosario1/cerebro-miguel/blob/main/cerebro/Relatorios/astra/ronda_horaria/AST-20260911-090001-1789128002005404834.md). Sem publicação, produção, exclusão ou despesa nova.

ref: PONTE-55fd3ce45b9cf5094f28c738. A resposta/avaliação não concede nova permissão nem encerra uma operação externa.
- [💸 Sangramento Transkriptor×GSN 13/09 (ZM-20260913-010)](Foruns/forum_transkriptor_gsn_pipeline_sangramento_20260913.md) — esteira 11/17 UTC do NYC ficou fora do pause de 12/09; transcreveu US$ 33 em 10-13/09 com consumidor morto; 8 JSONs na gsn_fila; kworker malware no NYC desde 10/09; + [memória](Memorias/memoria_transkriptor_gsn_pipeline_sangramento_20260913.md)

- 15/09/2026 00:3x — ZM/ZCode GLM-5.3 — PAINEL DE COMANDO MANUAL DO AGENTE YOUTUBE no /v6/youtube (ordem Miguel 14-15/09): campo URL + prompt opcional do editor + 5 marcadores (Cafezinho/GSN/Mapa Rio/Aiatolah/Rio Carta) + botão PRODUZIR + status ao vivo; executor youtube_manual.py no NYC com padrão V2 Cafezinho para TODOS (correção de nomes, entrevistado citado, gate de idioma, auditoria com retry fail-closed); transporte ssh com chave command= forçada; provas E2E (draft 270973 real, US$ 0 por reuso) e prints. Fórum: Foruns/forum_painel_comando_youtube_manual_20260915.md · Memória: Memorias/memoria_painel_comando_youtube_manual_20260915.md

- 16/09/2026 10:2x BRT — ZM/ZCode GLM-5.3 (ZM-20260916-025) — PARECER plano AGENTES HUMANOS GABRIEL & PEDRO (DSC-010/011, ordem Miguel; NADA construído): viável com 5 correções de desenho (instalador Windows-first sem segredo embutido + beacon HTTP na etapa 1; teto GLM via proxy fino da casa com apelidos glm-gabriel/glm-pedro no banco_custos — Z.ai não tem teto por chave; org GitHub nova + sync a partir do espelho GitHub com allowlist fail-closed e duas linhas de escrita casa/×agente/; bots novos por pessoa no BotFather; Rio Carta reerguido em sede nova com camada de aprovação por protocolo pro Pedro) + RETIFICAÇÃO: Rio Carta ≠ GSN/NYC — esteira parada desde 14/07/2026, Droplet 159.89.185.209 morto (SSH timeout), site+login vivos via Vercel, esforço 1-2 sessões. Parecer: Foruns/ponte_zm_dsc/de_zm.md (repo) bloco ZM-20260916-025 · Memória: Memorias/memoria_parecer_agentes_humanos_20260916.md (repo) · commit b2e68bf19.
