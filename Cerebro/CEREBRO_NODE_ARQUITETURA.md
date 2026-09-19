# 🏛️ CÉREBRO CAMADA 2: Nodo de Arquitetura

Este arquivo pertence à Camada 2 do Grande Cérebro. Ele concentra todos os links para Fóruns, Memórias e Arquivos de Código-Fonte relacionados à **arquitetura do projeto, failovers, infraestrutura de servidores e bots**.

- 🌉 **PARECER TRÊS PONTES — comunicação robô-robô SEMPRE por 2 vias (15/09/2026):** [forum_ponte_tres_vias_parecer_zm_20260915.md](./Foruns/forum_ponte_tres_vias_parecer_zm_20260915.md) + [memoria_ponte_tres_vias_parecer_zm_20260915.md](./Memorias/memoria_ponte_tres_vias_parecer_zm_20260915.md) — análise conjunta ZM×Astra a pedido do Miguel (GitHub principal · GDrive · NYC; nada implementado ainda, ele decide quem coda). 7/7 achados da Astra confirmados no código + 2 novos: ZM-8 (queda TOTAL do GitHub aborta o sync 15min no fetch ANTES do commit local — fallback NYC inalcançável) e ZM-9 (dois espelhos GDrive paralelos `gdrive:`×`drive:`). Proposta: separar DISTRIBUIÇÃO (main espelhável c/ force + snapshots) de MENSAGEM (caixas append-only por emissor, arquivo imutável nomeado pelo ID da casa, branch `caixas` FF-only no origin+mirror — imune ao force; ACK-<id> na caixa do destinatário; ponte_push v1.3 c/ readback e exit 2=DEGRADADO; leitura 2-vias). Retorno à Astra em Relatorios/astra/ronda_horaria/ZM-RETORNO-ASTRA-TRES-PONTES-20260915.md; bloc ZM-20260915-011 na ponte.

- 🖼️ **MISSÃO CAPAS V4.1 — Fase 1: pipeline de imagem destacada provado E2E + DeepSeek Vision como olho primário (2026-08-29):** [forum_capas_v41_deepseek_vision_20260829.md](./Foruns/forum_capas_v41_deepseek_vision_20260829.md) + [memoria_capas_v41_pipeline_deepseek_20260829.md](./Memorias/memoria_capas_v41_pipeline_deepseek_20260829.md) — `featured_image_runtime_cli` (contrato v2 fail-closed: Flickr oficial → Commons/Openverse → IA) rodando com visão dupla DeepSeek×Qwen (regra sagrada do Miguel: ver + cruzar antes de publicar). 3 fixes estruturais: chave DeepSeek morta deprecada (sobrescrevia a viva → Qwen decidia sozinho), FLICKR espelhada no `chaves.sh`, collector Commons corrigido (dims declaradas vs thumb derivado; Wikimedia agora recusa largura 2400 → 1920). Fila 268226/28/36/45/50 ainda sem capa por gates EDITORIAIS; 2 candidatas validadas a olho (Leila CPI 2024; estação Santa Cecília 2024) esbarram no gate pessoa-origem-não-confiável → proposta `media_human_review_cli` (Fase 2) aguarda "vai".

- ⏱️ **FRESCOR REGRA DURA NO V4.1 (caso-escola 96h) + sabatina Lula JN na capa (2026-08-28):** [forum_frescor_regra_dura_v41_sabatina_lula_jn_20260828.md](./Foruns/forum_frescor_regra_dura_v41_sabatina_lula_jn_20260828.md) + [memoria_frescor_regra_dura_v41_20260828.md](./Memorias/memoria_frescor_regra_dura_v41_20260828.md) — pauta de domingo virou post 268033 na quinta (seleção pegava `drafted` sem filtro de data; juiz só media repetição, ninguém media a idade do fato) → patch `V41_FRESCOR_20260828`: teto por vertical na seleção (hard news 24h, ciência/saúde/esporte/MA/digital 48h, cultura 72h) + regra `pauta_fria` no juiz inter-vertical, alinhado à doutrina FRESCOR-V5; provas: pauta do caso-escola BARRADA + ciclo real escreveu pauta do dia (268079). Post 268078 da sabatina JN no ar como MANCHETE (trava 8h, foto Stuckert, transcrição real 1.370 segs via Dell). Lições: repetição ≠ frescor; `drafted` sem janela = pauta-zumbi; Emenda 7 exige carimbo JSON com media_id casado; fuso do canônico joga post novo p/ `future` (fix SQL).

- 🧭 **BLOCOS REGIONAL/ESPORTES/DIGITAL — correção + audiência + destravamento (2026-08-27):** [forum_blocos_regional_esportes_digital_20260827.md](./Foruns/forum_blocos_regional_esportes_digital_20260827.md) + [memoria_blocos_regional_esportes_digital_20260827.md](./Memorias/memoria_blocos_regional_esportes_digital_20260827.md) — post 267872 (barricadas Rio) Saúde→Regional (causa: feed GERAL da Ag. Brasil + keyword "sus" por substring em "suspeitos"; fix = feed `rss/saude/feed.xml` no coletor NYC, meio_ambiente segue com o risco); Esportes TEM audiência (549 views/7d com 7 posts ≈ 78/post, melhor média das verticais; bloco parecia parado por gap 24-26/08 + sequestro do post novo pelo Top 10 `$excludes`); vertical digital MUDA desde o nascimento (banco sem tabela `draft_events`, gate fail-closed) → tabela criada + ciclo manual → **draft 267929 TikTok = 1ª matéria inédita do bloco Digital**; lições: wp-cli `--by=id`, classifier substring = porta de vazamento, banco de vertical nova precisa do esquema completo.

- 🧭 **AUDITORIA V4×V4.1 — O QUE PARAR (2026-08-26):** [forum_auditoria_v4_x_v41_o_que_parar_20260826.md](./Foruns/forum_auditoria_v4_x_v41_o_que_parar_20260826.md) + [memoria_auditoria_v4_x_v41_o_que_parar_20260826.md](./Memorias/memoria_auditoria_v4_x_v41_o_que_parar_20260826.md) — V4.1 tec/ciência/IA saudável (20 posts/7d, `_v4_versao=4.1`); V4 antigo vivo em 3 pontas: **regional em `/etc/cron.d/v4_regional`** (escapou da faxina 24/08 — cron tem 2 andares!), repetidor estatal falhando 400 desde 16/08 (~US$1-2/dia zerado), tendencias_intake sem consumidor; proposta de parada aguarda "vai" do Miguel.

- 🎙️ **RECEPTOR DE VOZ EXTERNO DO ZCODE (2026-08-25):** [forum_receptor_voz_zcode_20260825.md](./Foruns/forum_receptor_voz_zcode_20260825.md) + [memoria_receptor_voz_zcode_20260825.md](./Memorias/memoria_receptor_voz_zcode_20260825.md) — protótipo local Whisper com “ZCode, ouvir” para iniciar e “ZCode, Enter” para finalizar; dry-run padrão, clipboard/Enter protegido por janela ZCode em primeiro plano; falta teste manual com Miguel.

> **Regra do Tema Duplo:** Todo novo projeto de infraestrutura listado aqui deve possuir um par (Fórum + Memória).
> - **Fórum:** Para entender o planejamento e o resumo da arquitetura.
> - **Memória:** Para ler o log técnico, comandos executados e credenciais/portas.

---

## 0. Chaves Mestra e Acessos SSH (Mandatório)
Para evitar bloqueios de permissão ("Permission Denied") e timeouts, a Trindade DEVE usar as chaves corretas para cada cluster de servidores abaixo:

1. **Master Server (Tencent / Cingapura)**
   - **IP:** `43.156.151.165` (Porta: `38422`)
   - **User:** `ubuntu` *(root bloqueado)*
   - **Chave Local Exigida:** `~/.ssh/id_rsa`
   - **Comando base:** `ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165`

2. **Cluster DigitalOcean (Nova Conta / NYC / Astro / Rio Carta)**
   - **IPs:** `198.199.121.136` (Cafezinho Failover), `159.89.185.209` (Astro), `174.138.36.31` (Legacy WP)
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes root@<IP_DO_DROPLET>`
   - **Rio Carta vivo auditado 2026-05-22 23:50 BRT:** `159.89.185.209` = `agente-clone-01`, NÃO legado. Hospeda `riocarta_admin.service`, crontab de coleta/publicação/indexação e clone Astro `/root/riocarta_remote/rio_carta/`. Ver mapa operacional em [CEREBRO_INDEX_RIOCARTA.md](./CEREBRO_INDEX_RIOCARTA.md).

3. **Alfândega Chinesa (Beijing)**
   - **IP:** `82.156.167.218` (Porta: `22`)
   - **User:** `ubuntu`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes ubuntu@82.156.167.218`
   - **Função GSN atualizada em 2026-05-21 13:30 BRT:** executor canônico dos agentes Global South News (GSN), no path `/home/ubuntu/gsn_agentes/`. O site público do GSN continua GitHub -> Vercel; Beijing executa agentes, gera Markdown/assets e faz `git push`. Não confundir com Alibaba/Beijing do Cérebro nem com NYC legado.

4. **ServerDoIn (Brasil) — ⚠️ CONGELADO**
   - **IP:** `190.89.239.65` (Serverdo.in)
   - **Status (2026-05-24):** P0 ServerDoIn Fase D **congelada** por ordem de Codex Maestro.
   - **Motivo:** Incerteza sobre qual é o WordPress canônico do Cafezinho. Existem 3 caminhos WP (`/var/www/ocafezinho`, `/var/www/ocafezinho-BKP16-05-2026`, `/var/www/rioocafezinho`), e o Cafezinho usa CDN pesado. Miguel não conseguiu confirmar a origem viva com segurança.
   - **Decisão:** Não instalar `wp_metrics.sh`, não criar cron, não alterar `node_exporter` até ordem explícita do Miguel.
   - **Candidato provável:** `/var/www/ocafezinho` (nginx aponta vhosts, logs ativos, WP-CLI retorna posts recentes que batem com REST público).
   - **Legados isolados:** `rioocafezinho` e `ocafezinho-BKP16-05-2026` fora da métrica nova.
   - **Fórum:** `Foruns/forum_sprint_P0_telemetria_serverdoin_20260524.md`
   - **Não é Rio Carta vivo:** auditoria read-only em 2026-05-22 não encontrou crontab/arquivos Rio Carta relevantes neste host.
   - **GSN cron auditado 2026-05-23 00:00 BRT:** scripts GSN e YouTube existem, mas o crontab atual tem apenas Prometheus/tradutor/stargate. Não há crontab editorial GSN ativo em Beijing neste momento. Ver [CEREBRO_INDEX_GSN.md](./CEREBRO_INDEX_GSN.md).

5. **DigitalOcean NYC — Executor YouTube GSN**
   - **IP:** `142.93.48.252`
   - **Host:** `gsn-youtube-nyc-01`
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_ed25519`
   - **Comando base:** `ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes root@142.93.48.252`
   - **Função:** executor específico do Agente YouTube GSN, criado para contornar bloqueios de YouTube na China. Scripts em `/root/gsn_agentes/`; dados/logs em `/root/agent_data/`.
   - **Status auditado 2026-05-23 00:00 BRT:** crontab atual só tem Prometheus. Cron editorial YouTube está pausado; backup anterior em `/root/agent_data/crontab_pre_pausa_gsn_youtube_20260521_1805.txt` contém `0 */3 * * * /root/gsn_agentes/run_coletor.sh`.

4. **Alibaba Cloud (Beijing) - Oficina de Inteligência / Cérebro Vivo**
   - **IP:** `39.106.184.215` (Porta: `22`)
   - **User:** `root`
   - **Chave Local Exigida:** `~/.ssh/id_rsa`
   - **Comando base:** `ssh root@39.106.184.215`
   - **API RAM:** Chaves OpenAPI armazenadas localmente em `root/chaves/alibaba_api.env` com políticas `AliyunSWASFullAccess` e `AliyunSWASOpenFullAccess`.
   - **Status 2026-05-10:** não é mais Failover 2 do site por padrão. A função canônica passa a ser Cérebro Vivo, Trindade Técnica, memórias dinâmicas, fóruns, relatórios, Swarm Loop e processamento auxiliar. NYC permanece o failover frio do Cafezinho.
   - **Status 2026-08-06 (auditoria ao vivo):** ⛔ **SERVIDOR MORTO** — ping 100% perda + SSH timeout. Confirmar no console Alibaba se a VM foi solta/destruída e se a **cobrança parou** (alavanca de economia nº 2 do nodo de custos).

---

- 🗺️ **MAPA CANÔNICO DE SERVIDORES (auditoria ao vivo 2026-08-06):** [forum_mapa_servidores_ecossistema_20260806.md](./Foruns/forum_mapa_servidores_ecossistema_20260806.md) + [memoria_mapa_servidores_ecossistema_20260806.md](./Memorias/memoria_mapa_servidores_ecossistema_20260806.md) — o que cada máquina faz DE FATO (NYC failover-vigia = produção V4; Rio-Carta-Agentes = fábrica satélites; Alibaba/Beijing/RioWP-legado mortos; gsn-youtube ocioso; ServerDo reboot diário 03:31). Consultar antes de afirmar onde roda qualquer agente.

- 🚨 **CENTRAL DE ALERTAS (nasceu 2026-08-06, droplet 142.93.48.252 — ex-gsn-youtube):** [forum_central_alertas_20260806.md](./Foruns/forum_central_alertas_20260806.md) + [memoria_central_alertas_20260806.md](./Memorias/memoria_central_alertas_20260806.md) — Uptime Kuma (13 monitores, bind localhost) + Vigia de Discos SSH (cron :42, 6 servidores) → ambos alertam no **Telegram via bot Augusto**. Credenciais no cofre (`uptime_kuma_central_alertas.env`). Lições: tipo TCP no Kuma = `port`; `config.type` obrigatório no JSON da notificação; SQL não-trivial só via arquivo.

- 🏭 **DROPLET UTILITÁRIO (142.93.48.252, evoluiu da Central em 2026-08-06):** [forum_droplet_utilitario_20260806.md](./Foruns/forum_droplet_utilitario_20260806.md) + [memoria_droplet_utilitario_20260806.md](./Memorias/memoria_droplet_utilitario_20260806.md) — além da Central, agora hospeda: **ferroviário** (Mundo Trilhos/Rail Post, migrado do rio-ag) + **turismo** (Discover Brazil, idem) + **YouTube GSN** (revivido) + **YouTube Aiatolah** (novo). Bugs corrigidos: channel IDs Aiatolah 5/6 errados; chaves LLM mortas reativadas; `/root/config/` copiada; turismo ganhou fallback Perplexity. Crons ativos ×7.

- 📝 **LEGENDA OBRIGATÓRIA NOS TEMÁTICOS (2026-08-06, ordem Miguel):** [forum_legenda_obrigatoria_tematicos_20260806.md](./Foruns/forum_legenda_obrigatoria_tematicos_20260806.md) + [memoria_legenda_obrigatoria_tematicos_20260806.md](./Memorias/memoria_legenda_obrigatoria_tematicos_20260806.md) — toda imagem com legenda visível (item 7 dos 8 contratos; `hero_legenda` no frontmatter; figcaption nos 8 sites ao vivo; engine V4 local + writers do droplet patchados). **PENDENTE:** retrofit dos writers legados cicero/GSN (rio-ag + NYC; lista exata de arquivos:linhas na memória) — ou migrar ceara/globalsouth de vez para o V4 local, que já tem a regra.

- 🔭 **VIGÍLIA TEMÁTICOS — 3 SINAIS = FALSO ALARME (2026-08-07, verificação Kimi K3):** [forum_vigilia_tematicos_3_sinais_falso_alarme_20260807.md](./Foruns/forum_vigilia_tematicos_3_sinais_falso_alarme_20260807.md) + [memoria_vigilia_tematicos_3_sinais_falso_alarme_20260807.md](./Memorias/memoria_vigilia_tematicos_3_sinais_falso_alarme_20260807.md) — aiatolah NÃO parou (posts 07/08 na seção "Latest Reports"; scraper leu seção pinada "Frontier Broadcasts" 21/07); "hero→logo" NÃO é bug de template (1º `<img>` = logo do header; 2º = hero real `/hero/<slug>.jpg`, 200 nos 5 sites; layouts equivalentes); railpost+mapario VIVOS (200 via 3 servidores; 216.150.x.x = range legado Vercel; timeout = rota local intermitente). **8/8 sites vivos.** Lições de scraping: cuidado com seção pinada no topo, `.logo-img` do header, `onerror`→fallback, e 308→timeout = redirect não seguido. Logs da vigília: `Cerebro/monitoramento_horario/vigilia_tematicos/`.

- 🌐 **CEARÁ DIGITAL — DOMÍNIO CORRETO É ceara.digital (2026-08-07, ordem Miguel):** [forum_correcao_dominio_ceara_digital_20260807.md](./Foruns/forum_correcao_dominio_ceara_digital_20260807.md) — o `site_registry.json` do Sentinela trazia `www.cearadigital.news` (SEM DNS), por isso os "ceara fora do ar" eram falso alarme; site real vive em **`https://ceara.digital`** (200, favicons 200, canonical e astro.config já certos). Registry corrigido (`url` + `atualizado_em`). **Pendência Miguel:** entrada segue `pre_lancamento/allowlist_sem_alerta` — promover a `ativo`?

- 🧹 **MISSÃO DIÁRIA DE FAXINA LEGACY E DISCOS (plano 07/08; reativada por Miguel em 11/08):** [forum_plano_faxina_continua_droplets_20260807.md](./Foruns/forum_plano_faxina_continua_droplets_20260807.md) + [memoria_missao_faxina_diaria_legacy_20260811.md](./Memorias/memoria_missao_faxina_diaria_legacy_20260811.md) — missão permanente e não automática: inventariar tudo, inclusive o lixo; provar inatividade; somente depois de mais de 15 dias apresentar o item a Miguel; mover ou descartar apenas com autorização explícita; então manifestar, copiar ao B2, verificar e registrar no Cérebro. Com 15 dias ou menos, preservar. Destino de sistema: `failover-cafezinho1/faxina/`; memórias: `Cerebro-Memorias`.
  - **Mapa obrigatório antes da faxina:** [CEREBRO_NODE_ECOSSISTEMA_CANONICO.md](./CEREBRO_NODE_ECOSSISTEMA_CANONICO.md) separa a face visível da infraestrutura invisível que a sustenta. Nenhum candidato pode ser classificado sem confronto com esse mapa e seus nodos especializados.
  - **Consulta pendente da rodada local 03:** `Projeto Cafezinho Agentes/sites-tematicos_LEGADO_NAO_USAR` tem 3,5 GB, último arquivo em 24/07 e zero consumidor operacional detectado. Índice integral verificado no B2; original intacto. Um repo contém modificação local não commitada, exigindo arquivo completo se Miguel autorizar a retirada.
  - **Consulta pendente da rodada NYC 04:** `/root/legacy/banco_midia_20260626` tem 449 MB, está parado desde 29/06 e não possui consumidor detectado. Cinco bancos íntegros coincidem com backup B2 já verificado; o original aguarda autorização e receberá snapshot exato antes de eventual retirada.

- 📺 **GSN YOUTUBE FUNCIONANDO NO SITE CERTO (2026-08-07, ordem Miguel):** [forum_gsn_youtube_repoint_v4_20260807.md](./Foruns/forum_gsn_youtube_repoint_v4_20260807.md) + [memoria_gsn_youtube_repoint_v4_20260807.md](./Memorias/memoria_gsn_youtube_repoint_v4_20260807.md) — causa-raiz: publicador escrevia no repo **legado** `global-south-news.git` (beco sem saída); site é servido pelo `globalsouth-v4.git`. Fix: repoint p/ `/root/gsn_v4/globalsouth-v4` no droplet + frontmatter schema V4 (legenda obrigatória incluída) + commit-guard (HEAD==origin) + logs de falha LLM (o "Gary" de 06/08 morreu em silêncio no redator + expiração 6h). **1º post real AO VIVO:** Chas Freeman/Dialogue Works, HTTP 200 + hero + iframe + legenda + home. Canais **6/6** com ID real (Neutrality Studies `UCHdLVKd…`, MFA Russia `UCIULQ7Y…` resolvidos). **Incidente bancada:** commit de teste vazou p/ origin (`&&` pulou `set-url`) → force-push corrigido na hora; lição: `set-url` pro bare ANTES de qualquer push. Pendências p/ Miguel: ZHIPU sem saldo, expiração inbox 6h→**resolvida: fila subiu p/ 12h** (ordem voz). Bot legado GSN: NYC já off desde 23/07 (repo morto tarred→B2 nesta faxina) e cópia rio-ag pausada com tag `PAUSADO_USER_REQUEST_20260807`.

- ✅ **FAXINA PONTUAL EXECUTADA NOS 3 SERVIDORES (2026-08-07, autorizado por voz):** [forum_faxina_pontual_3_servidores_20260807.md](./Foruns/forum_faxina_pontual_3_servidores_20260807.md) + [memoria_faxina_pontual_3_servidores_20260807.md](./Memorias/memoria_faxina_pontual_3_servidores_20260807.md) — regra de ouro indexar→B2→verificar→apagar; destino `b2:failover-cafezinho1/faxina/<servidor>/<classe>/<aaaa-mm>/`. **rio-ag 87→83%** (npm −862MB; audit ceara 214MB→B2+truncate; git gc ×3), **NYC 79→61%** (caches pip+puppeteer 5,1G; backups/ 1,6G→B2; logs truncados; 815 used_*; .bak >7d; gsn_remote 1,9G→B2), **Tencent** upload 9,2G em curso. Manifestos: `Cerebro/Memorias/faxina_20260807/MANIFESTO_FAXINA_*.jsonl`. **Ficha dos zumbis p/ Miguel decidir:** `174.138.36.31` riocarta-WP legado (SSH morto) e `159.89.237.100` GSN-WP ocioso pagando.

- 🎨 **CURADORIA DE IMAGEM POR TESE — ARQUITETURA DOCUMENTADA (2026-08-12, ordem Miguel voz):** [forum_curadoria_imagem_por_tese_arquitetura_20260812.md](./Foruns/forum_curadoria_imagem_por_tese_arquitetura_20260812.md) + [memoria_curadoria_imagem_por_tese_arquitetura_20260812.md](./Memorias/memoria_curadoria_imagem_por_tese_arquitetura_20260812.md) + [teoria_escolha_imagem_por_vertical_20260812.md](./Foruns/teoria_escolha_imagem_por_vertical_20260812.md) — visão: escolher imagem pela TESE editorial, não pela entidade crua; loop humano híbrido quando a IA não acha (Telegram inline + painel web + e-mail) + aprendizado gold. **Diagnóstico V4 confirma SEGURO** derivar `entidade=pessoas[0]` (`_extract_v4_bank_photo` no NYC `v4_vertical_draft_worker.py:776` casa por `pessoas_identificadas_json`×título, docstring "jamais o campo entidade"; mapa entidade→vertical só no painel, não no V4). 4 fases: (0) unificar entidade híbrida editável + fallback NOT NULL p/ 15 instituições/locais 🔴 bloqueador baixo risco ~1h; (1) motor tese→imagem semântico c/ embeddings + tribunal (qwen3-vl grátis 15/09) shadow; (2) loop multi-canal + auth HMAC + callback listener + ingest gold; (3) coluna `tipo_entidade` (não existe) + teoria por vertical. Reaproveita `v4_curadoria_tese`/`frame_visual`, endpoint `/api/midia-ouro/review/<hash>` (no ar, **sem auth — gap**), `enviar_baleia_azul_v2.sh`. **Estado: 📄 documentado, execução pausada aguardando Miguel autorizar Fase 0.** Zero código alterado. — ZCode (GLM-5.2)

**Canal de escrita restrito da Laura no canônico (PD-1, 18/08/2026):** usuário `loop-laura-write` (forced command, sem shell) → wrapper de auditoria → whitelist de ops no `write-query.php`. Desde **21/08/2026 (ordem Miguel 13:00 + pacto de dupla checagem CL×AGY)** a whitelist inclui `publish` e `schedule` (9 ops; gmt derivado server-side). Gates do site seguem valendo (GATE-IMG fail-close, §86 thumbnail, proteção editorial). Detalhes técnicos e provas: [memoria_pd1_canal_write_laura_publish_schedule_20260821.md](./Memorias/memoria_pd1_canal_write_laura_publish_schedule_20260821.md) + adendo 21/08 em [forum_ponte_laura_completa_20260817.md](./Foruns/forum_ponte_laura_completa_20260817.md).

## 1. Arquitetura de Redundância e Failover
- 📁 **Tema: Infraestrutura DigitalOcean (Nova Conta Ativa)**
  - **Conta Oficial:** `migueldorosario2@gmail.com`
  - **Droplets (first-project):**
    - `ubuntu-s-1vcpu-2gb-nyc1` (Failover do Cafezinho) — IP `198.199.121.136` (2GB RAM, 50GB Disk)
    - `agente-clone-01` (Nova infraestrutura Astro/API) — IP `159.89.185.209` (1GB RAM, 25GB Disk)
    - `riocarta-wordpress` (Legacy WP Rio Carta) — IP `174.138.36.31` (1GB RAM, 25GB Disk)
  - **Papel canônico 2026-05-10:** NYC/DigitalOcean é o failover frio do Cafezinho e também a casa de outros sites/projetos: Rio Carta, GSN, Mundo Trilhos, Rail Post, Discover Brazil e Mapa Rio.
- 📁 **Tema: Warm-Standby em Nova York (NYC)**
  - **Fórum/Documentação Base:** [protocolo_failover_nyc.md](./Memorias/protocolo_failover_nyc.md) *(Conceito e regra de "quebrar o vidro")*
  - **Fórum Vigia NYC:** [forum_vigia_nyc.md](./Foruns/forum_vigia_nyc.md) *(planejamento e deploy do Vigia read-only Fase 0)*
  - **IP Atual:** `198.199.121.136` (DigitalOcean NYC)
  - **Memória:** [memorias_vigia_nyc.md](./Memorias/memorias_vigia_nyc.md) *(Logs de testes reais e operação)*
  - **Vigia Fase 0 (2026-05-09 17:03 BRT):** `/root/vigia_nyc_readonly.py` deployado no NYC, MD5 `249591ff5fb854e6ff7c42e329a23570`, cron final `17 * * * * /usr/bin/flock -n /root/agent_data/vigia_nyc/vigia_nyc.cron.lock /root/venv/bin/python3 /root/vigia_nyc_readonly.py --commit-state >> /root/agent_data/vigia_nyc/cron.log 2>&1 # VIGIA_NYC_READONLY_FASE0_20260509_CODEX`, apenas GET público na API WP, heurísticas determinísticas, cache `processed_ids`, relatório em `/root/agent_data/vigia_nyc/`, custo LLM `0.0000` e sem credencial WP/admin. Rollback: `crontab /root/crontab_backup_pre_vigia_nyc_flock_20260509_170105_codex.txt` no NYC e restaurar script com `/root/vigia_nyc_readonly.py.bak_pre_codex_flock_20260509_170012`.
- 📁 **Tema: Backups Locais e Limpeza Legacy**
  - **Fórum/Política de Backup:** [forum_backup_e_legacy.md](./Foruns/forum_backup_e_legacy.md)
  - **Diretório Snapshot:** `backup_root/`
  - **Resumo:** Espelho completo de 1.4GB do `root/` e quarentena de pastas velhas (`root/legacy/`).
  - **Nota 2026-05-07:** o antigo `sync_gdrive_5min.sh` do Cafezinho entrou formalmente em quarentena (`root/legacy/` e `cingapura_root_sync/legacy/`). Os caminhos vivos agora sao stubs de bloqueio para impedir reativacao acidental do sync amplo para Google Drive.
  - **Nota 2026-05-09:** `root/agente_zelador_memoria.py` ganhou modo explícito `--aplicar-manifesto-legacy`, mantendo `--plan-only` como padrão seguro. A execução autorizada pelo Miguel moveu 48 arquivos órfãos classificados como `legacy`, `tarefa_efemera` ou `canal_legacy` para `Legacy/20260509_103745/`, com rollback em [zelador_mvp1_apply_20260509_103745.json](./root/agent_data/zelador/zelador_mvp1_apply_20260509_103745.json).
- 📁 **Tema: Malha de Backups Local/B2/NYC**
  - **Fórum:** [forum_backup.md](./Foruns/forum_backup.md)
  - **Resumo:** Centraliza a proposta de espelho local `backup_root/`, cadência B2 e câmara de ar do failover NYC. Qualquer higienização de árvore que possa ser sincronizada para produção deve ser proposta antes no canal, com rollback e validação.

- 🚨 **BACKUP CRÍTICO ATIVO — `.git/` DA RAIZ (2026-05-27)**
  - **Fórum:** [forum_backup.md](./Foruns/forum_backup.md) *(seção "BACKUP CRÍTICO")*
  - **Motivo:** Repo git da raiz cresceu para **17 GB** (blobs grandes: .mkv 2GB, .tar 1.4GB). `git pack-objects` consumia 7 GB de RAM → OOM kills → travamentos.
  - **Backup local:** `Backups/backup_dotgit_20260527_154226.tar.gz` *(17 GB, seguro)*
  - **Backup B2:** `b2:mayra-brain/Antigravity_Google/backups/git/backup_dotgit_20260527_154226.tar.gz` *(upload agendado para 05:00 BRT)*
  - **Script:** `Projeto Cafezinho Agentes/root/upload_backup_git_b2.sh` *(auto-upload + auto-remove do cron quando concluir)*
  - **Cron:** `0 5 * * * bash .../upload_backup_git_b2.sh`
  - **Log:** `/tmp/upload_backup_git_b2.log`
  - **Tamanho:** 17 GB comprimido — histórico COMPLETO com todos os blobs
  - **Status:** 🟡 Upload B2 agendado para **madrugada 05:00 BRT**
  - **Ação pós-backup:** `git filter-repo` para remover blobs grandes → reduzir `.git/` para ~2-3 GB
  - **Rollback:** Extrair backup do local ou B2 e restaurar `.git/`
  - **⚠️ IMPORTANTE:** Qualquer agente que for manipular o repo git DEVE verificar se este backup está 100% no B2 antes de reescrever histórico.

## 2. Modelos Dinâmicos e Governança
- 📁 **Tema: Regras da Trindade e Agentes Autônomos**
  - **Fórum:** [forum_modelos_dinamicos.md](./Foruns/forum_modelos_dinamicos.md)
  - **Memória:** [memorias_modelos_dinamicos_governanca_20260502.md](./Memorias/memorias_modelos_dinamicos_governanca_20260502.md)
- 📁 **Tema: Tríade China — coletor/auditor/publicador com guardas de segurança**
  - **Fórum:** [forum_ativar_triade_china.md](./Foruns/forum_ativar_triade_china.md)
  - **Código:** `root/coletor_china.py`, `root/auditor_china.py`, `root/publicador_china.py`
  - **Resumo 2026-05-07:** pipeline novo default-off ativado por cron com `AGENTE_CHINA_TRIADE_ENABLED=1`; legado `agente_china.py` pausado. Coletor usa round-robin RSS, Brave opcional, fallback Jina Reader quando extração fica curta e fontes Sul Global B.5 (`Asia Times`, `Sputnik Globe`, `SCMP`, `TRT World`). Auditor bloqueia item sem texto antes de qualquer LLM e desvia pauta sensível para `MANUAL_REVIEW`. Publicador só atua sobre status `APROVADO`.
  - **Atualização 2026-05-09:** publicador ganhou gate próprio de título PT-BR. Mesmo que item antigo chegue com `titulo` em inglês no SQLite, `publicador_china.py` tenta traduzir antes do POST e bloqueia para `MANUAL_REVIEW` se o título continuar parecendo inglês; também bloqueia markdown cru no HTML. Bug indexado: `BUG-20260509-CHINA-PUBLICADOR-TITULO-EN-GATE`.
- 📁 **Tema: Agente Sobrenatural — Arquivista do Insólito**
  - **Fórum:** [forum_agente_sobrenatural.md](./Foruns/forum_agente_sobrenatural.md)
  - **Memória:** [memoria_agente_sobrenatural.md](./Memorias/memoria_agente_sobrenatural.md)
  - **Código:** `root/agente_sobrenatural.py`, `cingapura_root_sync/agente_sobrenatural.py`
  - **Resumo 2026-05-08 12:28 BRT:** Agente destravado na Tencent com `/root/agente_sobrenatural.py`, config `enabled=true`, `wp_status=draft`, orçamento diário `US$ 3.00`, limite de `6` drafts/dia aplicado em código e cron remoto `10,40 * * * * ... # AGENTE_SOBRENATURAL_MVP`. Codex corrigiu dry-run com efeito externo, adicionou trava financeira/registro de `usage`, filtro pré-auditor anti-Cloudflare/fonte insuficiente, exigência de imagem destacada e teto diário. Primeiro draft real criado: WP `244388`, mídia `244386`, interlink ativo. O código ativo força `draft`; publish direto não está liberado nesta versão.
- 📁 **Tema: Agente Cobertura Flávio Bolsonaro — Staging crítico dedicado**
  - **Fórum:** [forum_agente_flavio_bolsonaro_20260525.md](./Foruns/forum_agente_flavio_bolsonaro_20260525.md)
  - **Memória individual:** [agente_flavio_bolsonaro.md](./root/agent_data/memorias_agentes/agente_flavio_bolsonaro.md)
  - **Código em staging:** `root/staging_social/flavio_bolsonaro/agente_flavio_bolsonaro.py`, `root/staging_social/flavio_bolsonaro/robo_coleta_flavio_bolsonaro.py`, `root/staging_social/flavio_bolsonaro/diretriz_flavio_bolsonaro.json`
  - **Status 2026-05-26 19:10 BRT:** criado por Kimi em staging em 2026-05-25, indexado por Codex em 2026-05-26 e colocado em cron local de **dry-run** a cada 30 minutos. Primeiro ciclo real com internet coletou 48 candidatos RSS, aprovou 1 pauta, redigiu com DeepSeek, revisou com Kimi/Moonshot, passou fact-check Perplexity e salvou rascunho local. Sem publicação WordPress.
  - **Escopo:** cobertura crítica de Flávio Bolsonaro, Banco Master, PL, Valdemar Costa Neto, Michelle Bolsonaro e Carlos/Carluxo, com coleta RSS + Brave, triagem por whitelist, redação, revisão, fact-check e rascunho WordPress.
  - **Guarda operacional:** cron atual é apenas dry-run local (`AGENTE_FLAVIO_BOLSONARO_DRYRUN_20260526_CODEX`), sem publicação direta. A flag `--publish` do README ainda deve gravar apenas `draft`; qualquer liberação para rascunho WP ou publish exige ordem explícita de Miguel e registro prévio de backup/rollback.

## 3. Bot Zizilinda — Arquitetura em 6 Camadas
- 📁 **Tema: Refatoração do bot_zizi_linda.py (Gatekeeper → Extrator → Tese → Redator → Auditor → Publicador)**
  - **Fórum principal:** [forum_zizilinda.md](./Foruns/forum_zizilinda.md)
  - **Memória principal:** [memorias_zizilinda.md](./Memorias/memorias_zizilinda.md)
  - **Memória (arquitetura geral):** [memoria_arquitetura_zizilinda_20260502.md](./Memorias/memoria_arquitetura_zizilinda_20260502.md)
  - **Memória (pipeline Instagram):** [memoria_zizilinda_instagram_20260502.md](./Memorias/memoria_zizilinda_instagram_20260502.md)
- 📁 **Tema: Fluxo Avançado de Vídeo Twitter (Menus de Intenção e Callback Assíncrono)**
  - **Fórum de Arquitetura:** [forum_zizilinda_twitter_arquitetura.md](./Foruns/forum_zizilinda_twitter_arquitetura.md)
  - **Memória:** [memoria_zizilinda_twitter.md](./Memorias/memoria_zizilinda_twitter.md)

## 4. Arquitetura de Autocura e Observabilidade
- 📁 **Tema: Sistema de Autocura Operacional**
  - **Índice de incidentes:** [CEREBRO_NODE_BUGS.md](./CEREBRO_NODE_BUGS.md) §3/§4
  - **Memória de referência:** [indice_expediente_20260502.md](./Memorias/indice_expediente_20260502.md)
  - **Fechamento técnico:** [fechamento_expediente_20260502.md](./Memorias/fechamento_expediente_20260502.md)
  - **Resumo:** Autocura V4, observador, Caetano crítico-only, Vigia NYC e cooldowns de alerta formam a camada de detecção/estancamento. Antes de alterar qualquer peça, o agente deve abrir o índice de bugs e localizar a ficha curta do sintoma.
- 📁 **Tema: Autocura Editorial por Audiência/Monitoramento**
  - **Fórum:** [forum_elevar_audiencia_20260504.md](./Foruns/forum_elevar_audiencia_20260504.md)
  - **Memória:** [memoria_elevar_audiencia_20260504.md](./Memorias/memoria_elevar_audiencia_20260504.md)
  - **Resumo:** Registra o uso de monitoramento para duplicatas, meta-discurso LLM, placeholders, regressões de imagem, `intocaveis.json`, BOOST e relatórios de defesa editorial.

## 5. Arquitetura Editorial de Títulos e Audiência
- 📁 **Tema: DNA Galileia, Score de Títulos e Auditoria 500**
  - **Fórum:** [forum_melhoria_titulos_20260504.md](./Foruns/forum_melhoria_titulos_20260504.md)
  - **Tarefa de retomada:** [tarefa_retomada_melhoria_titulos_20260504.md](./Memorias/tarefa_retomada_melhoria_titulos_20260504.md)
  - **Resumo:** Debate a melhoria dos títulos a partir da auditoria offline dos 500 posts, antes de qualquer patch de prompt. Define checklist de número concreto, entidade forte, verbo ativo, apelo visual e clareza em 2 segundos.
- 📁 **Tema: Auditoria Expandida GA4 26d e Dry-run de Títulos**
  - **Fórum:** [forum_melhoria_titulos_20260504.md](./Foruns/forum_melhoria_titulos_20260504.md)
  - **Memória:** [memoria_retomada_madrugada_20260505.md](./Memorias/memoria_retomada_madrugada_20260505.md)
  - **Script:** [auditoria_expandida_ga4_26d.py](./scripts/auditoria_expandida_ga4_26d.py)
  - **Relatório:** [auditoria_expandida_top_bottom_ga4_26d.md](./Analises/auditoria_500_20260504/auditoria_expandida_top_bottom_ga4_26d.md)
  - **Resumo:** Codex cruzou GA4 26d com WP REST para top 50 e bottom 50 maduro. Resultado sustenta dry-run com threshold 50: abaixo de 37 alerta vermelho; 37-49 alerta amarelo; 50-69 passa com log; 70+ é meta editorial, não bloqueio automático.
- 📁 **Tema: Defesa Contra Alucinação de Cargos Políticos**
  - **Fórum:** [forum_melhoria_titulos_20260504.md](./Foruns/forum_melhoria_titulos_20260504.md)
  - **Memória:** [memoria_retomada_madrugada_20260505.md](./Memorias/memoria_retomada_madrugada_20260505.md)
  - **Seed local:** [figuras_politicas_brasil.json](./root/config/figuras_politicas_brasil.json)
  - **Script dry-run:** [dry_run_cargos_politicos.py](./scripts/dry_run_cargos_politicos.py)
  - **Utilitário vivo:** [util_cargos_politicos.py](./root/util_cargos_politicos.py)
  - **Relatório dry-run:** [dry_run_cargos_20260505](./Analises/dry_run_cargos_20260505/)
  - **Resumo:** Após bug Lindbergh, Codex criou seed local em modo `0.1-dry-run`, com aliases, validade e `bloqueio_automatico=false`. Em 2026-05-05 05:42 BRT, Codex adicionou auditor offline zero-write de cargos: leitura do JSON + posts locais/WP opcional. Validação local em 500 posts encontrou 1 alerta real, o Lindbergh já conhecido; Claude auditou 175 menções às 06:50 BRT e encontrou zero falsos positivos. Em 2026-05-05 07:12 BRT, Codex integrou `util_cargos_politicos.py` em `motor_publicador.py` (Nacional/Lula) e `agente_eleicoes_produtor.py` (Eleições) como dry-run vivo pré-publish: loga `CARGOS_POLITICOS`/`ALERTA_CARGO`, não bloqueia, não altera payload e opera em fail-open. Em 07:44 BRT, Codex executou rsync para Tencent e validou MD5/`py_compile`/smoke. Backups: `Backups/*bak_pre_cargos_dryrun_20260505_071052` e remotos `/root/*bak_pre_cargos_dryrun_rsync_20260505_074049`.

## 6. Padrão Sentinela com Escalada por Cérebro (Haiku→Sonnet→Opus)
- **🧠 Origem:** ordem direta do Miguel em 2026-05-05 06:00 BRT — *"o haiku pode ser um sentinela. se ele detectar problema, consulta o cérebro, que vai informar sobre grau de complexidade do problema e a necessidade de usar modelo mais complexo. além do mais, como estamos trabalhando em equipe, a simplicidade de um é neutralizada pela gestão partilhada"*.
- **Princípio arquitetural:** **modelo leve detecta + Cérebro classifica + modelo certo resolve.** A simplicidade isolada do sentinela é compensada pela inteligência distribuída da Trindade — Haiku sozinho seria limitado, mas com Cérebro+rota+escalada, opera tão bem quanto Opus em 90% dos casos com fração do custo.
- **Materialização da §16 do `CEREBRO_NODE_GOVERNANCA.md`:** este padrão é a operacionalização concreta da regra "inteligência é para gastar bem, não para economizar".

### Camadas do padrão
1. **Detecção (sentinela leve — Haiku):**
   - Varre logs, ticks, monitoramento, canal, GA4
   - Detecta sintoma (HTTP 500, post duplicado, score Galileia <37, tracebacks novos, queda GA4)
   - **Custo:** ~$0.002-0.01 por execução
2. **Classificação no Cérebro (sem LLM — regex/lookup direto):**
   - Tabela `CEREBRO_NODE_BUGS.md` mapeia sintoma → complexidade conhecida
   - **Custo:** zero
3. **Roteamento por complexidade:**
   - **Sintoma conhecido + fix conhecido** → sentinela (Haiku) aplica autocura registrada — ex.: rebaixar duplicata via WP API, cooldown Caetano, `detectar_recusa_llm()`
   - **Sintoma conhecido + fix desconhecido** → escala pra **Sonnet** investigar variante
   - **Sintoma novo + impacto crítico** → escala pra **Opus** orquestrar (debugging difícil + redação de regra/autocura nova)
   - **Sintoma novo + crise irreversível** → escala humano (Miguel) com timestamp BRT
4. **Registro de aprendizado (qualquer modelo que resolveu):**
   - Caso novo vira ficha curta no `CEREBRO_NODE_BUGS.md`
   - Próxima vez que sintoma igual aparecer → Haiku resolve direto (passou de complexo pra rotineiro)

### Quando rebaixar do Opus pro Haiku
- Sintoma indexado ≥2 vezes no Cérebro com fix idempotente
- Autocura validada em produção sem regressão por ≥7 dias
- Fix cabe em ficha curta (<15 linhas) sem dependência de contexto longo

### Anti-padrão proibido
- Despertar com Opus pra "ser seguro" sem antes consultar `CEREBRO_NODE_BUGS.md`. Maioria dos sintomas já tem mapa cirúrgico — Haiku resolve.
- Aplicar autocura nova sem indexar no Cérebro depois — perde-se a oportunidade de rebaixar pro Haiku no futuro.

### Métrica de maturidade do padrão
- **% de incidentes resolvidos no nível do sentinela** (sem escalar) → quanto maior, mais maduro o Cérebro
- **Custo médio por incidente** → tende a cair conforme Cérebro indexa
- **Tempo médio de resolução** → tende a cair (lookup é mais rápido que LLM novo)

### Materialização atual no projeto
- **Caetano** (notificação): já é sentinela leve com cooldown crítico-only
- **Autocura V4** (cron `:17`): sentinela com lookup em `agent_data/`
- **Monitoramento Claude 30/30** (atualmente Opus): candidato natural a virar Haiku quando o Cérebro estabilizar
- **Tribunal Visual** (Gemini): exemplo do padrão — modelo barato detecta, escala pra IA generation só quando precisa
- **Tick canal-only Codex 10/10**: também candidato a Haiku quando os fluxos do canal forem todos rotineiros

### Aplicabilidade ao Codex (Miguel 2026-05-05 06:10 BRT)
O mesmo padrão se aplica ao Codex com **seus próprios modelos** (gpt-5-mini / gpt-5 / o3): tick rotineiro em modelo barato, investigação em modelo médio, debugging arquitetural em modelo top. Codex pode ajustar `cron/codex_tick_implementador.sh` pra usar `--model` por classe de tarefa quando estiver maduro pra isso. Princípio é o mesmo: **modelo leve detecta + Cérebro classifica + modelo certo resolve**.

### Teste piloto Claude (iniciado 2026-05-05 06:10 BRT)
O mesmo padrão se aplica ao Codex com **seus próprios modelos** (gpt-5-mini / gpt-5 / o3): tick rotineiro em modelo barato, investigação em modelo médio, debugging arquitetural em modelo top. Codex pode ajustar `cron/codex_tick_implementador.sh` pra usar `--model` por classe de tarefa quando estiver maduro pra isso. Princípio é o mesmo: **modelo leve detecta + Cérebro classifica + modelo certo resolve**.
Claude Code começa em **Haiku como sentinela**, sobe pra **Sonnet** em investigação não-indexada, sobe pra **Opus** antes de deploy/inscrição no Cérebro/redação de regra. Mecânica: Claude pede troca explícita; Miguel executa `/model haiku|sonnet|opus`. Toda troca = re-leitura leve do Cérebro pertinente (§15). Resultados deste piloto vão informar refinamento futuro deste padrão.

## 7. Arquitetura de Vídeo e Legendas (Zizilinda Padrão BBC)
- 📁 **Tema: Padrão Ouro de Legendas Nativas (Substituição de drawbox/pad por libass nativo)**
  - **Fórum:** (Decisão originada no chat do Telegram/Antigravity em 2026-05-05)
  - **Memória:** [memoria_zizilinda_ffmpeg_libass_bug_20260505.md](./Memorias/memoria_zizilinda_ffmpeg_libass_bug_20260505.md)
  - **Script Motor:** `motor_legendas_bbc.py` (Localizado na raiz do projeto)
  - **Resumo Arquitetural:** Para a produção automatizada de vídeos jornalísticos da Zizilinda, abandonou-se o uso de filtros visuais externos do FFMPEG (`pad`, `drawbox`) que quebravam proporção de tela ou cobriam a imagem original. O Padrão BBC agora é codificado estritamente em um arquivo `.ass` com **`BorderStyle=4`** (Caixa delimitadora oficial do Libass) em vez de `BorderStyle=3` (que sofre com bug de transparência forçada em algumas builds). O motor Python também aplica **word wrap estrito** (máx ~42 caracteres) antes da conversão FFMPEG, garantindo legibilidade perfeita com `Fontsize=48` sem vazar a tela. Este motor deve ser usado como biblioteca/módulo base para toda geração de vídeo da Zizilinda V4.
- 📁 **Tema: Flag futura de faixa preta inferior para vídeos paisagem traduzidos**
  - **Origem:** Antigravity registrou em 2026-05-06 09:03 BRT teste local com `pad=iw:ih+180:0:0:black`, ajuste de `MarginV` e `PlayResY` no ASS.
  - **Resumo Arquitetural:** A Zizilinda deve ganhar no futuro uma flag explicita de "faixa preta" para vídeos paisagem/tradução, posicionando a legenda em tarja inferior adicionada fora da imagem original, evitando cobrir GCs/lower-thirds. Este requisito fica separado do fluxo BBC atual e não deve ser ativado implicitamente no cortador ou no publicador sem smoke visual e autorização.

## 8. Motor Unificado Zizilinda / YouTube
- 📁 **Tema: Fronteira funcional entre Zizilinda, Agente YouTube e Motor Unificado**
  - **Fórum:** [forum_youtube_autonomo_textos.md](./Foruns/forum_youtube_autonomo_textos.md)
  - **Resumo Arquitetural:** Decisão Codex 2026-05-06: YouTube deve ser a camada de **fonte/coleta** (`video_id`, RSS/cron, recência, Transkriptor, custo, `youtube_inbox`). Zizilinda deve ser a **orquestra controlada + contrato editorial** (Assunto, Data, Personagens, Tese, tom, citação e estrutura jornalística), reutilizável para YouTube, X/Twitter, Instagram, URL comum e texto colado. O Motor Unificado recomendado é `motor_zizilinda.py`, como biblioteca editorial independente dos gatilhos. Manter `agente_youtube.py`, `youtube_inbox.py`, `agente_youtube_publicador.py` e `bot_zizi_linda.py` vivos por compatibilidade; integrar o motor por flag/dry-run antes de qualquer renome ou deploy.
  - **Implementação inicial Codex 2026-05-06 01:16 BRT:** Criados `root/contrato_zizilinda.py` (schema `material` v2 dry-run, validação de diarização YouTube, plano editorial e 4 camadas heurísticas) e `root/motor_zizilinda.py` (core puro que processa material/inbox, monta prompts das 4 camadas e prompt da matéria, sem side effects em import). `root/agente_youtube_publicador.py` recebeu dry-run opcional `ZIZI_MOTOR_UNIFICADO_DRYRUN=1`, default desligado e fail-open, para logar diagnóstico do motor sem mudar publicação, WP, LLM ou inbox.
  - **Hardening Codex 2026-05-06 01:35 BRT:** `root/motor_zizilinda.py` normaliza as 4 camadas vindas da LLM antes do prompt final; em especial, `personagens` string vira lista de um item, evitando degradar o campo para caracteres separados. Validação local cobriu `py_compile`, smoke com LLM fake retornando string e smoke da flag dry-run do publicador.
  - **Polimento pós-auditoria Claude 2026-05-06 01:37 BRT:** Flag única alinhada em `ZIZI_MOTOR_UNIFICADO_DRYRUN`; `motor_unificado_ativo()` virou alias compatível de `motor_unificado_dryrun_ativo()`; diarização aceita `Speaker`, `Locutor`, `Falante` e `Voz`; parser inválido das 4 camadas emite warning e cai em heurística. O `util_cost_guard.py` permanece corretamente fora do motor editorial, na camada `util_youtube_transcript.py` antes de qualquer custo Transkriptor.
  - **Requisitos Antigravity/Miguel 2026-05-06 02:25 BRT:** O contrato editorial do motor passa a separar `falantes_identificados` (quem fala, com `codigo`, `nome_real`, `papel`) de `pessoas_citadas` (apenas mencionadas), e a tese editorial deve explicitar o entrevistado principal quando identificável. Hardening local: parser aceita retorno do roteador como texto puro ou `(texto, modelo)`; merge das camadas preserva as chaves novas; heurística reconhece `SPK`, `Speaker`, `Locutor`, `Falante` e `Voz`. A Super Esteira de Vídeo fica desenhada como módulos fail-open pós-publicação: selecionar trecho, cortar com `ffmpeg`, traduzir, queimar legenda BBC/libass, publicar thread no X/Twitter, atualizar WP com embed. Twitter/X, update WP pós-publicação e Video SEO/Schema são críticos e só podem sair do desenho para deploy com rollback literal, smoke remoto e autorização explícita.
  - **Fase 2 local Codex 2026-05-06 02:45 BRT:** Criado `root/cortador_youtube.py` como módulo independente da Super Esteira, sem side effects em import e sem chamadas a Transkriptor, WordPress ou Twitter/X. O contrato do módulo é `processar_corte_youtube(url_youtube, transcricao_diarizada, tese_editorial, workdir, ...) -> {ok,path,erro,etapa,janela}` em fail-open. Etapas internas: seleção LLM de janela exata de 180s em JSON, extração do texto da janela a partir da transcrição já paga, tradução PT-BR via roteador, geração `.ass` BBC com `BorderStyle=4` e wrap 42 chars, corte `ffmpeg` com stream copy e fallback reencode, e queima de legenda por libass. Uso real permanece bloqueado até auditoria Claude/Antigravity, smoke com vídeo controlado e plano de rollback/deploy.
- **Memória prática 2026-05-19 — legendagem de filme curto com música/Trump:** técnica validada em teste manual para reaproveitar depois: baixar vídeo real, extrair áudio 16kHz mono, transcrever, traduzir o SRT inteiro para PT-BR em uma chamada com DeepSeek/Qwen de luxo e temperatura baixa, preservar nomes próprios/siglas, gerar `.ass` BBC com texto amarelo e caixa preta, adicionar faixa preta inferior com `ffmpeg pad=iw:ih+bar:0:0:black` e queimar a legenda exclusivamente nessa faixa. O vídeo original não deve ser distorcido nem coberto; usar `libx264 -crf 21 -preset veryfast -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart`. Para música/áudio misto, priorizar legibilidade e sincronização visual sobre métricas brutas de chars/MB. Continuar este sprint depois, sem automatizar cron/publicação ainda.
- **Exemplo bem-sucedido validado por Miguel 2026-05-21 — Kaja Kallas:** tarefa local em `Outros/pautas editoriais o cafezinho/2026 Mai 21/Kaja Kallas/`. Entrada `kaja kallas.mp4` 1920x1080, 12,46s, já com legenda inglesa queimada no quadro original. Saída aprovada por Miguel: `kaja_kallas_legendado_bbc.mp4`, 1920x1328, com faixa preta inferior de 248px e legenda PT-BR amarela dentro da faixa. Comando-base usado: `python3 root/claude/claude_agente_legendador_de_video.py --input-video <mp4> --output <saida> --work-dir <codex_legendador_bbc> --bar-ratio 0.23 --line-width 40 --preset veryfast --crf 21`. Resultado visual perfeito segundo Miguel: vídeo preservado sem distorção, sem cobrir a legenda original nem o conteúdo; a tradução ficou curta, legível e sincronizada. Este caso deve ser usado como referência operacional pela Trindade para vídeos curtos horizontais já baixados.
  - **Governança de Gatilhos (02:48 BRT):** Estabelecido que **não haverá diferença de tratamento** entre links manuais (enviados via Telegram) e links autônomos (coletados via RSS Whitelist). Ambos disparam o pipeline VIP completo (WP + Corte 3m + Twitter Fio + Embed). O Motor Zizilinda deve ser estritamente agnóstico em relação à fonte da URL.  - **Hardening Claude/Codex 2026-05-06 02:48 BRT:** `cortador_youtube.py` ganhou wrapper público `cortar_video_3min(..., dry_run=True, timeout_seconds=600, keep_workdir=False)`, `justificativa` no JSON da seleção, limite de vídeo de 4h, validação de workdir por prefixo (`/tmp/cortador*` ou `/root/agent_data/cortes`), `ffprobe` para medir duração, fallback reencode quando `-c copy` gera duração fora de 178-182s, `modo_ffmpeg` na janela, metadata de tempo/tamanho e warning >100MB. Dry-run não baixa nem corta por padrão.
  - **Auditoria Codex 2026-05-06 08:15 BRT:** `cortador_youtube.py` foi endurecido contra os gaps remanescentes do parecer Claude: timeouts default internos agora são 300s; janela LLM fora de 180s exatos, `start_time` negativo ou `end_time` além da duração conhecida falham em vez de serem corrigidos silenciosamente; workdir exige path real dentro de `/tmp/cortador` ou `/root/agent_data/cortes`; `.ass` é gravado com UTF-8 BOM; CLI default usa `/tmp/cortador`; retorno inclui `metadata.video_id`; há cache idempotente para output final >1MB e logs estruturados JSON de início/cache/erro/sucesso. Dry-run continua sem download/corte/queima, e uso real segue bloqueado até smoke com vídeo controlado e autorização.
  - **Auditoria linha-a-linha Codex 2026-05-06 08:25 BRT:** Dois gaps finais foram corrigidos em `cortador_youtube.py`: a CLI voltou a ser dry-run por padrão e só executa download/corte/queima com `--executar-real`; quando `duracao_total` não é fornecida, o módulo agora mede o arquivo baixado/local com `ffprobe`, aborta vídeos >4h ou <180s e revalida `end_time <= duracao_video` antes do corte. Validação local: `py_compile`, smoke com LLM fake, `--help` da CLI e `validar_cerebro.py`.
  - **Smoke controlado Codex 2026-05-06 08:35 BRT:** Após aprovação Claude 08:31, aplicados polimentos locais no `cortador_youtube.py`: fallback de `video_id` por hash MD5 da URL para evitar colisão de cache, `yt-dlp` limitado a até 720p, parser de timestamp aceita decimal `[MM:SS.xx]`, blocos de legenda limitados a 8s e `base` inicializado sem redefinição insegura. Smoke real com vídeo sintético local de 205s, LLM fake, sem download/Transkriptor/WP/Twitter: saída `/tmp/cortador/SMOKETEST123_3min_legendado.mp4`, duração `180.025s`, tamanho `17.464.817 bytes`, `modo_ffmpeg=reencode`, logs `cortador_inicio` e `cortador_finalizado`.
  - **Smoke com download real Codex 2026-05-06 08:44 BRT:** Antigravity autorizou teste real; `yt-dlp` local `2024.10.22` falhou com YouTube (`Precondition check failed`/formatos indisponíveis), então Codex usou binário temporário `/tmp/cortador_tools/yt-dlp` versão `2026.03.17` apenas no PATH do smoke. Vídeo CC `aqz-KE-bpKQ` baixado via módulo, cortado `30->210`, legendado e salvo em `/tmp/cortador/aqz-KE-bpKQ_3min_legendado.mp4`; `ffprobe` final `180.032s`, tamanho `31.468.951 bytes`, `modo_ffmpeg=reencode`, `duracao_total_s=634.624`, logs `cortador_inicio` e `cortador_finalizado`. Achado reutilizável: ambiente Tencent/local para uso real precisa `yt-dlp` novo fora do Python 3.8 ou binário empacotado/instalado com rollback.
  - **Contrato Twitter Fio dry-run Codex 2026-05-06 08:45 BRT:** Criado `root/postador_twitter_fio.py` como módulo separado e inofensivo: monta payload de 2 tweets para a Super Esteira (Tweet 1 com MP4 local, Tweet 2 com link da matéria), valida tamanho <=280, existência/tamanho do vídeo e URL http(s), mas não importa Tweepy, não lê credenciais e não chama API X. `publicar_fio_real()` retorna bloqueio explícito. Validação local com o MP4 do smoke real passou; publicação viva segue bloqueada até autorização Miguel, smoke remoto e revisão Claude.
  - **Polimento Twitter Fio Codex 2026-05-06 08:56 BRT:** Após diretriz Antigravity/Miguel de não tocar Twitter real, `postador_twitter_fio.py` recebeu contagem estimada de URL por t.co (23 chars), margem comentada de 10 chars no Tweet 1, placeholder explícito `__TWEET_1_ID_REAL_NO_ADAPTADOR__`, CLI `--saida-json` e metadata com política: integração viva deve manter/copiar o MP4 para `/root/agent_data/cortes` antes de montar o payload, não depender de workdir temporário do cortador. Smoke fechado gerou JSON auditável em `agent_data/twitter_fio_dryrun/fio_smoke_miguel_20260506_0855.json`; `publicar_fio_real()` segue retornando bloqueio.
  - **Orquestrador Super Esteira dry-run Codex 2026-05-06 09:05 BRT:** Criado `root/motor_super_esteira.py` para consolidar `motor_zizilinda -> cortador_youtube -> postador_twitter_fio` em um JSON único, sem WP publish/update, sem Twitter/X real e sem Video SEO. O módulo persiste MP4 de teste em `agent_data/cortes` no ambiente local e documenta que produção deve usar `/root/agent_data/cortes`. Smoke com `SMOKETEST123_3min_legendado.mp4` gerou `agent_data/super_esteira_dryrun/super_esteira_smoke_20260506_0905.json` com `materia_html`, `cortador_metadata`, `fio_dryrun` e travas explícitas.
  - **Ponte youtube_inbox -> Super Esteira Codex 2026-05-06 09:18 BRT:** Criado `root/youtube_super_esteira_dryrun.py` e flag `ZIZI_SUPER_ESTEIRA_DRYRUN=1` em `agente_youtube_publicador.py` para gerar JSON consolidado por entrada do `youtube_inbox` sem remover a fila, sem WordPress, sem Twitter/X real e sem Video SEO. O JSON sai em `agent_data/super_esteira_dryrun/<video_id>.json`. A ponte usa gerador local heurístico por padrão para evitar custo LLM acidental em dry-run; LLM só entra se um chamador injetar explicitamente `gerar_texto`. `motor_super_esteira.py` também aceita dry-run sem MP4 ainda (`exigir_mp4_para_fio=false`) e hash de URL como fallback de `video_id`.
  - **Rsync Tencent + estado operacional Codex 2026-05-06 10:40-10:57 BRT:** Miguel autorizou rsync controlado dos 7 arquivos da Super Esteira para `/root` no Tencent. Estado vivo permanece conservador: `ZIZI_SUPER_ESTEIRA_DRYRUN=0` por default, sem Twitter/X real, sem WP publish/update, sem Video SEO e sem Transkriptor. Após erro real da API X com MP4 de 153s (`403 Forbidden` por limite de conta básica), a janela operacional do cortador ficou em `JANELA_SEGUNDOS=135`; prompts, gerador dry-run e validação pós-`ffprobe` usam a constante (`JANELA_SEGUNDOS ±2`) em vez de faixas fixas `178..182`. Smokes local/remoto com vídeo sintético geraram MP4 de `135.001s`; pendentes do inbox remoto/local estavam zerados.
  - **Regra de frescor YouTube Codex 2026-05-08 17:05 BRT:** Miguel definiu que o Agente YouTube não deve formar banco/acervo de transcrições. `youtube_inbox` é fila curta de passagem para idempotência anti-recobrança e retry breve, não estoque editorial. Operação correta: coletar entrevista recém-publicada, auditar data/frescor/canal, transcrever, criar rascunho WP imediatamente quando houver 1 item fresco, e arquivar pendências antigas sem nova chamada LLM/Transkriptor. **Hard cap editorial:** vídeo com mais de 24h não entra. **Ideal:** recém-publicado, preferencialmente 0-6h. **Cadência:** não esperar lote de 4; 4/dia é teto de segurança, não meta. **Horário:** watcher leve somente durante o dia (ex.: 08h-22h BRT); à noite não precisa coletar/postar. **Fluxo automático desejado:** RSS whitelist sem custo -> se achou 1 novidade fresca, transcreve URL-direto -> publica draft imediatamente -> limpa inbox. Se Transkriptor ficar `Processing`, guardar `order_id` e consultar depois sem reenviar a URL; nunca baixar/transcrever várias vezes o mesmo vídeo. Patch em `youtube_inbox.py`/`agente_youtube_publicador.py`: `YOUTUBE_INBOX_MAX_IDADE_HORAS` default 6h, `arquivar_expiradas()` move itens velhos para outbox, cron continua desligado e Google Indexing só roda se `YOUTUBE_AUTONOMO_STATUS=publish`.
  - **Autocura Codex 2026-05-09 18:24 BRT:** cron do coletor YouTube no Tencent passou de `/root/agente_youtube.py` para `/root/agente_youtube_watcher.py`, mantendo o publicador separado em `draft`. Motivo: reduzir lote/custo e alinhar à regra “colhe 1 e faz logo”. Cron vivo: `25 9,13,17,21 * * * ... agente_youtube_watcher.py ... # YOUTUBE_AUTONOMO_WATCHER_4XDIA_20260509_CODEX`; publicador: `35 9,13,17,21 * * * ... agente_youtube_publicador.py ... # YOUTUBE_AUTONOMO_4XDIA_20260509_CODEX`. Backup/rollback: `/root/crontab_backup_pre_youtube_watcher_20260509_182138_codex.txt` e cópia B2 `b2:failover-cafezinho1/criticos/crontab_backup_pre_youtube_watcher_20260509_182138_codex.txt`.
- **Renomeação Caçador/Cortador de Vídeos 2026-05-10 10:46 BRT:** o antigo conceito “Gerador de Vídeo” foi aposentado porque induzia confusão com IA generativa. O agente correto **não cria vídeo do zero**: ele caça vídeos reais do YouTube, usa `yt-dlp` para baixar e `ffmpeg` para cortar pílulas jornalísticas. Fórum oficial novo: [forum_agente_cacador_cortador_de_videos.md](./Foruns/forum_agente_cacador_cortador_de_videos.md); fórum antigo `forum_agente_gerador_video_ffmpeg.md` fica obsoleto. Estado seguro atual: Fase 0 local, sem cron, sem deploy Tencent e sem postagem real. `root/cortador_youtube.py` aceita cortes de 5s a 140s, mira 90s-135s e valida saída com `ffprobe`; `config/agente_cacador_cortador_videos.json` mantém `cron_autonomo=false` e `publicacao_real_x=false`.
- **Fórum V2 enxuto + F1.0 `/clipar` 2026-05-10 13:27 BRT:** a discussão nova do Caçador/Cortador passa para [forum_cortador_youtube_20260510_v2.md](./Foruns/forum_cortador_youtube_20260510_v2.md), mantendo o fórum anterior apenas como histórico. Codex preparou patch local para o Augusto receber `/clipar URL_MP4 INICIO FIM`, aceitar somente MP4/MOV/M4V/WebM diretos, bloquear YouTube nesta fase (sem `yt-dlp`), limitar 5-140s, aplicar cooldown por chat e devolver o MP4 validado no Telegram. Validação local OK (`py_compile`, `json.tool`, sandbox dry-run, corte sintético 10s com `ffprobe_ok`). Deploy no Augusto vivo fica pendente de auditoria Claude linha-a-linha e smoke real com MP4 público pequeno; sem cron, sem X/Twitter e sem publicação.
- **Teste Lula F1.5 2026-05-10 13:44 BRT:** Antigravity abriu [forum_cacador_teste_lula_v1.md](./Foruns/forum_cacador_teste_lula_v1.md) para liberar YouTube no `/clipar` usando `yt-dlp --download-sections` no canal `@LulaOficial`. Parecer Codex/Kimi/DeepSeek: direção editorial aprovada, mas **não remover a trava YouTube ainda**. O `yt-dlp` local `2024.10.22` falhou em metadados/formatos (`Precondition check failed`, `nsig`, `Requested format is not available`). Próximo passo seguro é F1.5a isolado: testar `yt-dlp` atualizado fora do Augusto, sem cron, sem publicação e sem alteração no bot vivo; se passar, criar F1.5b com whitelist de canais e auditoria Claude.
  - **Blindagem contra prompt vazado Codex 2026-05-06 10:49 BRT:** `motor_zizilinda.py`, `bot_zizi_linda.py`, `postador_twitter_fio.py` e `autocura_patterns.py` passaram a tratar diretrizes humanas livres como instrução interna, não como conteúdo publicável. O postador de fio reprova determinísticamente sinais de prompt/diretriz vazada, e a autocura reconhece o padrão em HTML WP. Regra reutilizável: antes de qualquer nova postagem viva em rede social, exibir saída crua final para aprovação humana do texto concreto.

## 9. Pipeline V9-style Tríade China (Sprints A.4 → A.10 + B.4-B.7)

> Consolidado em 2026-05-08 após sequência de Sprints 2026-05-07. Status: PRODUÇÃO ATIVA com 4 drafts WP gerados.

### Cadeia completa (cron `:05`/`:15`/`:25` Tencent)

```
1. Coleta — RSS (B.5: Asia Times + Sputnik + SCMP + TRT World) + Brave + Xinhua HTML scraper (B.4) + Zhipu chinês fallback (B.7)
2. Extrator — Trafilatura + Jina Reader fallback se <3000 chars (A.2)
3. A.4 Limpador — `deepseek-chat` chinês (remove sidebar/rodapé)
4. A.6 Filtro relevância (regex keywords China) + Trava formato (HTML/code-fence)
5. REDATOR (estágio 4 V9) — claude-sonnet-4-5-20250929 via AssemblyAI (A.10) → fallback claude-sonnet-4 → opus-4 → qwen-max → glm-5.1
6. REVISOR — glm-5.1 (chinês, perspectiva diferente)
7. AUDITOR 1 (consenso) — claude-sonnet-4-5 via AssemblyAI
8. AUDITOR 2 (consenso) — claude-sonnet-4 via AssemblyAI (DIFERENTE do 1, reduz bias)
9. A.3 Pauta sensível contextual — Taiwan/HK só dispara se co-ocorrência com termo político
10. FACT-CHECK — Perplexity sonar-reasoning-pro (busca real)
11. Tribunal Visual — qwen-vl-max (chinês com visão)
12. Publicador — qwen-turbo (posta como `status=draft` no WP, Miguel/Antigravity revisam); desde 2026-05-09 possui gate final de título PT-BR e markdown cru antes do POST.
```

### Schema JSON (`agente_china_modelos.json` v1.6-redator-ocidental)

10 roles configurados: coletor (redator), revisor, auditor_1, auditor_2, fact_checker, tribunal_midia, publicador, comentarista, comentarista_flash, limpador.

DeepSeek V4 banido do redator (regra §30.2 / §29). Mantido em comentarista.

### A.10 ativa (2026-05-07 23:15 BRT)

Redator trocou de qwen-max → claude-sonnet-4-5 via AssemblyAI Gateway. Resultado empírico: 4 drafts gerados na madrugada (id=76 SCMP airship, 83/87 Pandaily, 88 Sputnik) com `wp_post_id` populado, status=draft no WP. Primeira ROUND-TRIP do pipeline.

### Bug atual REJEITADO_FORMATO (Sonnet 4.5 retorna code fence)

Cron 09:15 BRT 2026-05-08: 3/3 itens (id=98/99/100) caíram em `formato_invalido:code_fence_inicio`. Sonnet envelopa resposta em ` ```markdown `. Não-determinismo do prompt — ontem 4 drafts passaram. Fix proposto: 1 linha no prompt anti-fence. Pendente autorização Miguel (role crítica §30.3). Ver `BUG-20260508-SONNET-CODE-FENCE-REDATOR`.

### Custo estimado pipeline

- Limpador (DeepSeek-chat): ~$0.10/dia
- Redator (Sonnet 4.5): ~$0.50/dia
- Revisor (GLM-5.1): ~$0.20/dia
- Auditor 1+2 (Sonnet 4.5+4): ~$1.00/dia
- Fact-check (Perplexity): ~$0.30/dia
- Tribunal visual (qwen-vl-max): ~$0.15/dia
- Publicador (qwen-turbo): ~$0.05/dia
- **Total:** ~$2.30/dia (kill-switch JSON: $5/dia)

### Fórum vivo

- 📁 [forum_ativar_triade_china.md](./Foruns/forum_ativar_triade_china.md) — todas as Sprints A.0 → A.10 + B.4-B.7
- 📁 [forum_agente_china_calibracao_20260509.md](./Foruns/forum_agente_china_calibracao_20260509.md) — calibração 2026-05-09: lógica AND dos auditores corrigida e Ação 5 de métricas de saúde read-only deployada.

### Calibração e healthcheck (2026-05-09)

- Patch Codex 18:40 BRT em `/root/auditor_china.py`: divergência entre dois auditores (`APROVADO + REJEITADO_*`) agora vai para `MANUAL_REVIEW`, em vez de `REJEITADO`; ambos aprovados seguem para fact-check; ambos rejeitados continuam rejeição.
- Ação 5 Codex 19:23 BRT: script read-only `/root/agente_china_health.py` deployado para baseline de saúde/conversão, sem cron e sem escrita no banco.
- Artefato do smoke: `/root/agent_data/china_health_latest.json`.
- MD5 script: `3d0cbf1e76835142d45eb1776a3ff3ed`.
- Backup B2: `b2:failover-cafezinho1/criticos/agente_china_health.py.deployed_20260509_1923_codex`.
- Baseline vivo do DB: `total=117`, `PUBLICADO=6` (`5.13%`), `DRAFT_WP=1`, `pipeline_output=7` (`5.98%`), `MANUAL_REVIEW=39`, rejeições `71` (`60.68%`), divergência de auditores `6.42%`.
- Alertas emitidos: conversão publicada baixa, conversão pipeline baixa, 1 falso positivo candidato histórico.
- Ação 2 Codex 19:27 BRT: `KEYWORDS_RELEVANCIA` de `/root/auditor_china.py` expandido para BRICS+, ASEAN, LATAM/Mercosul, África, Oriente Médio multipolar, Eurásia/Rússia, Ucrânia/Putin, Hungria/Orbán, Japão, Filipinas e termos geopolíticos correlatos; `sem_keywords_china_sul_global` continua fora de escopo técnico (`REJEITADO_FORA_ESCOPO`), não `DRAFT_WP`.
- MD5 `auditor_china.py` pós-Ação 2: `0c9e78c3fc35195f1a2951c7227324c0`; backup remoto `/root/auditor_china.py.bak_pre_keywords_sul_global_20260509_1926_codex`; backups B2 pré/pós em `criticos/`.
- Próximo passo: medir conversão pós-patch com `/root/agente_china_health.py` nos próximos ciclos antes de mexer em Revisor A7.

---

## 10. AssemblyAI LLM Gateway (Claude via gateway)

**Descoberto 2026-05-07 18:28 BRT.**

- **Endpoint:** `POST https://llm-gateway.assemblyai.com/v1/chat/completions` (OpenAI-compatible)
- **Auth:** `Authorization: Bearer ${ASSEMBLY_API_KEY}` (chave em `/root/.env`)
- **Modelos disponíveis:** APENAS família Anthropic Claude 4.x:
  - `claude-sonnet-4-5-20250929` (Sonnet 4.5 — top, redator A.10)
  - `claude-sonnet-4-20250514` (Sonnet 4 — auditor_2)
  - `claude-haiku-4-5-20251001` (Haiku 4.5 — limpador/publicador alternativos)
  - `claude-opus-4-20250514` (Opus 4 — futuro Validador 1 do Certificador)
- **NÃO suporta:** GPT, Gemini, DeepSeek, Qwen, GLM (testado, retorna 400)
- **Conclusão:** AssemblyAI Gateway = fachada Claude da Anthropic com pricing próprio
- **Pendência:** consolidar `ASSEMBLY_API_KEY` em `.env.unificado` e `chaves.sh` (hoje só em `.env`)

---

## 11. Categorias agregadas LLM (proposta consenso 3/3, não codada ainda)

> Status: 🟡 Aprovado (Claude 09:00 BRT + Antigravity 09:45 + Codex 10:01) — aguarda implementação após NYC OK ✓
> Fórum: [forum_categorias_llm_qualidade_preco.md](./Foruns/forum_categorias_llm_qualidade_preco.md)

### Princípio sem hardcode (§30.1)

Agentes que publicam referenciam slots simbólicos. Atualizador descobre + categoriza modelos vivos via API.

### Slots agregados propostos (em `modelos_vivos.json`)

```json
{
  "chineses_luxo":      ["qwen-max", "glm-5.1"],
  "chineses_medio":     ["qwen-plus", "glm-4-plus", "moonshot-v1", "doubao-pro-128k"],
  "chineses_barato":    ["qwen-turbo", "deepseek-v4-flash", "glm-4.5-air"],
  "ocidentais_luxo":    ["claude-sonnet-4-5", "claude-sonnet-4", "claude-opus-4"],
  "ocidentais_economico": ["claude-haiku-4-5", "gemini-flash"]
}
```

Cascata cruzada: `ocidentais_luxo → chineses_luxo (qwen-max custa 4x menos que Haiku 4.5) → chineses_medio`.

---

## 12. NYC Failover (atualizado 2026-05-08)

### Estado atualizado pós-incidente NYC (2026-05-08 10:42 BRT)

**Conta DigitalOcean atual:** `migueldorosario2@gmail.com` (substituiu antiga `migueldorosario@gmail.com` que foi encerrada).

**Droplets ativos:**

| Droplet | IP | Função |
|---|---|---|
| `ubuntu-s-1vcpu-2gb-nyc1` | **198.199.121.136** | **Failover Cafezinho NYC ⭐** |
| `agente-clone-01` | 159.89.185.209 | Astro/API |
| `riocarta-wordpress` | 174.138.36.31 | Legacy WP Rio Carta |

**IP morto (NÃO usar):** `45.55.50.249` — droplet apagado junto com encerramento da conta antiga.

### Sync Tencent → NYC

- Script: `/root/sync_nyc_leve.sh` (Tencent)
- Cron: `0 4 * * 0` — APENAS DOMINGO 04:00 BRT (§28: congelamento natural 48h)
- Auth: chave Tencent `/root/.ssh/id_ed25519_nyc_sync` autorizada no NYC
- Última sync manual: 2026-05-08 10:52 BRT (1GB total, OK)

### Backups

- **Backblaze B2** (`failover-cafezinho1`) — cron diário `0 5 * * *` ATIVO
- **NYC failover** — sincronizado domingos
- **Local Backups/** — `.bak_pre_<motivo>_<timestamp>` por patch
- **§30.5 pré-requisitos** pra deploy crítico: Backblaze + NYC + local + rollback documentado.

---

## 13. Agente Certificador de Qualidade (deployado dry-run 2026-05-08 13:35 BRT)

> **O que é:** Agente especial de **luxo** que avalia AUTOMATICAMENTE a qualidade dos OUTROS agentes publicadores e decide o **tier** deles (quarentena/draft_only/publish_direct/publish_destaque). Roda 1x/semana, NÃO publica nada — só observa, julga e atualiza arquivo de qualificação. Substitui revisão manual humana por consenso 2/2 de 2 LLMs top.

### Função no ecossistema

Cafezinho tem ~20 agentes que publicam matérias automaticamente (Tríade China, Sobrenatural, Fantástico, Geopolítica, Lula, Mercado etc). Antes desse Certificador, Miguel revisava drafts manualmente. **Agora o sistema se auto-policia:**

```
Agentes publicadores → posts no banco/WP
                              ↓
                   Certificador (semanal)
                   ↓               ↓
            Validador 1       Validador 2
        (claude-opus-4)    (glm-5.1 Zhipu)
                   ↓               ↓
                   Consenso 2/2
                              ↓
              qualificacao_agentes.json
                              ↓
              motor_publicador respeita tier:
              - publish_direct → status=publish
              - draft_only → status=draft (Miguel revisa)
              - quarentena → bloqueia post
```

### Arquivos do Certificador

| Arquivo | Função |
|---|---|
| `/root/agente_certificador_qualidade.py` | Agente principal — chama validadores + grava decisão |
| `/root/qualificacao_agentes.py` | Helper: `tier_de(agente)`, `status_wp_para_tier()`, `deve_postar()` |
| `/root/agent_data/qualificacao_agentes.json` | Tier corrente de cada agente (real) |
| `/root/agent_data/qualificacao_agentes.json.dry_run` | Modo dry-run (14 dias antes de modo real) |
| `/root/agente_escalada_qualificacao.py` | Escalada AUTOMÁTICA upgrade (6h) + downgrade com autocura |

### 5 Camadas de escalada (forum_certificador §"Promoção Temporal Automática + Autocura Escalada")

**Camada 1 — Promoção Temporal (auto upgrade após 6h):**
Agente novo nasce em `draft_only`. Se em 6h tem ≥3 drafts, taxa rejeição <30%, zero REJEITADO_FORMATO, custo <80% limite, zero traceback → promove automático pra `publish_direct`.

**Camadas 2-5 — Erro NÃO rebaixa imediato (autocura primeiro):**
- 2: `agente_autocura_v4.py` tenta corrigir
- 3: `agente_corretor_autonomo.py` tenta (mais agressivo)
- 4: Patcha código do agente pra `status="draft"` default (DRY-RUN por flag `ESCALADA_HARD_AUTORIZADA=0`)
- 5: Comenta agente no crontab (DRY-RUN por flag) + alerta Miguel

### Validadores (2 LLMs top, providers diferentes)

| Slot | Modelo | Provider | Custo/semana |
|---|---|---|---|
| Validador 1 | claude-opus-4-20250514 | AssemblyAI Gateway (`ASSEMBLY_API_KEY`) | ~$45 |
| Validador 2 | glm-5.1 (745B) | Zhipu (`ZHIPU_API_KEY`) | ~$8 |
| **Total** | | | **~$53/semana = ~$7.50/dia** |

Diferença de provider e cultura editorial reduz bias (Anthropic ocidental vs Zhipu chinês).

### Anti-paranoia política (§30 + §28)

Validadores recebem prompt explícito:
- Linha editorial Cafezinho NÃO é critério de rejeição (pró-Lula, pró-China, pró-Sul Global é a linha)
- Critérios OBJETIVOS: ALUCINACAO_FACTUAL, CITACAO_FAKE, ATRIBUICAO_AUSENTE, FORMATO_CORROMPIDO, COERENCIA_QUEBRADA
- Critérios NÃO-VÁLIDOS: tom pró-China, crítica EUA/OTAN, apoio Rússia/Irã/Cuba/Venezuela, falta de "ambos os lados"
- Toda rejeição exige citar trecho exato + fonte original

### Tiers e thresholds

| Tier | Score consenso | O que faz |
|---|---|---|
| `quarentena` | < 40 | Bloqueia post — agente desligado |
| `draft_only` | 40-74 | Posta como draft — Miguel revisa via WP |
| `publish_direct` | 75-89 | Posta direto status=publish |
| `publish_destaque` | ≥ 90 | Posta direto + elegível manchete/destaque |

### Política de transição automática

| Cenário consenso 2/2 | Ação |
|---|---|
| Ambos APROVAM (≥75 cada) | ✅ Promove tier (precisa 2 validações consecutivas pra subir) |
| Ambos REPROVAM (<75 cada) | ⬇️ Rebaixa pra draft_only (cooldown 24h + autocura antes) |
| **DISCORDAM** | 🔒 MANTÉM tier atual (status quo) |
| Ambos VETAM (<40 cada) | 🚫 Quarentena — pede autorização Miguel |

### Salvaguardas (forum_certificador.md §"Salvaguardas")

7 camadas anti-falso-positivo + cautela com audiência alta:
1. Janela móvel 15-20 posts
2. Cooldown rebaixamento 24h
3. Notificação Telegram em mudança de tier
4. Histórico permanente últimas 8 validações
5. Modo DRY-RUN obrigatório 14 dias antes de modo real
6. Promoção lenta (2 validações consecutivas pra subir)
7. Freeze automático se GA4 cair >20% em 24h

### Status atual (2026-05-09 16:59 BRT)

- ✅ Helper `qualificacao_agentes.py` deployado
- ✅ JSON `qualificacao_agentes.json` com defaults conservadores (China+Sobrenatural=draft_only, agentes maduros=publish_direct grandfathered)
- ✅ Escalada `agente_escalada_qualificacao.py` deployada (camadas 1-3 reais, 4-5 dry-run-only)
- ✅ Certificador `agente_certificador_qualidade.py` deployado (modo dry-run obrigatório)
- ✅ Cron de Escalada dry-run instalado: `50 * * * * cd /root && ESCALADA_HARD_AUTORIZADA=0 /root/venv/bin/python3 /root/agente_escalada_qualificacao.py --tick >> /root/agent_data/escalada_qualificacao.log 2>&1 # ESCALADA_QUALIFICACAO_DRYRUN_20260509_CODEX`
- ✅ Smoke/tick manual 2026-05-09 16:58 BRT: `py_compile` OK, China não promoveu por `drafts_minimo`/`taxa_rejeicao_ok`, Sobrenatural sem telemetria suportada, camadas 4-5 permanecem dry-run.
- ✅ Fase 1 Autonomia Supervisionada deployada 2026-05-09 18:08 BRT: `/root/util_ledger.py` + integração em `/root/agente_escalada_qualificacao.py`, com ledger hash-chain append-only em `/root/agent_data/ledger_decisions.jsonl`; `verify` remoto OK (`count=4`, `errors=[]`), MD5 `util_ledger.py=f6fa2c813007d1634fef6e7db7aa2c3b`, `agente_escalada_qualificacao.py=a5589485bfd8b045553751d461cab6ac`.
- ✅ Fase 2 Restart Counter implementada local/dry-run 2026-05-09 21:09 BRT em `root/agente_escalada_qualificacao.py`, sem deploy Tencent/crontab: helper `check_and_record_restart(...)`, arquivo `root/agent_data/restart_counter.dryrun.json`, ledger separado `root/agent_data/ledger_decisions.restart_counter_dryrun.jsonl`, limite 3 reinicializações/60min por agente, timestamps UTC `Z`, lock `fcntl`, escrita atômica, `blocked_until`, reset de janela e fail-closed para JSON corrompido/invariante quebrada. Smoke local OK (`actual_allowed=[true,true,true,false]`, JSON corrompido `allowed=false`) e ledger dry-run `verify` OK; Claude auditou e aprovou integralmente às 21:10 BRT.
- ✅ Backup nomeado no Backblaze B2: `b2:failover-cafezinho1/criticos/util_ledger.py.deployed_20260509_180720_codex`, `b2:failover-cafezinho1/criticos/agente_escalada_qualificacao.py.deployed_ledger_fase1_20260509_180720_codex` e backup pré-patch `agente_escalada_qualificacao.py.bak_pre_ledger_fase1_20260509_180526_codex`.
- ⏸️ Integração em publicação direta ainda bloqueada por guardas: `motor_publicador`/`publicador_china` só devem respeitar tier real depois de 14 dias dry-run e nova autorização/validação; `ESCALADA_HARD_AUTORIZADA` deve permanecer `0`.
- Rollback do cron de Escalada: no Tencent, `sudo crontab /root/crontab_rollback_remove_escalada_qualificacao_20260509_165843_codex.txt && sudo crontab -l | grep -v ESCALADA_QUALIFICACAO_DRYRUN_20260509_CODEX`.
- Rollback da Fase 1 Ledger: `sudo cp /root/agente_escalada_qualificacao.py.bak_pre_ledger_fase1_20260509_180526 /root/agente_escalada_qualificacao.py && sudo rm -f /root/util_ledger.py /root/agent_data/ledger_decisions.jsonl.lock && sudo /root/venv/bin/python3 -m py_compile /root/agente_escalada_qualificacao.py`.
- Rollback local da Fase 2 Restart Counter: `cp "Projeto Cafezinho Agentes/Backups/agente_escalada_qualificacao.py.bak_pre_restart_counter_fase2_20260509_210629_codex" "Projeto Cafezinho Agentes/root/agente_escalada_qualificacao.py" && rm -f "Projeto Cafezinho Agentes/root/agent_data/restart_counter.dryrun.json"* "Projeto Cafezinho Agentes/root/agent_data/ledger_decisions.restart_counter_dryrun.jsonl"* && python3 -m py_compile "Projeto Cafezinho Agentes/root/agente_escalada_qualificacao.py"`.

### Fórum vivo

📁 [forum_certificador_qualidade.md](./Foruns/forum_certificador_qualidade.md) — proposta completa, pareceres Antigravity (09:45) + Codex (10:01) consenso 3/3, schema, plano §11 rollback, cronograma 14 dias dry-run.

📁 [forum_certificador_escalada_autocura_20260509.md](./Foruns/forum_certificador_escalada_autocura_20260509.md) — âncora operacional da Escalada 5 camadas, cron dry-run e rollbacks.

📁 [forum_certificador_autonomia_supervisionada_20260509.md](./Foruns/forum_certificador_autonomia_supervisionada_20260509.md) — Autonomia Supervisionada: Fase 1 Ledger Imutável deployada e Fase 2 Restart Counter local/dry-run auditada.

### Bug derivado da concepção

📁 [forum_meta_agente_auto_corretor.md](./Foruns/forum_meta_agente_auto_corretor.md) — evolução futura: Certificador também REESCREVE regras automaticamente quando detecta padrão de falso positivo. Aguarda Certificador validado dry-run + 14 dias antes de codar.

---

## 14. CEO do Cérebro / Augusto Cognitivo (Passo 2, definido em 2026-05-09)

**Função:** camada executiva do Cérebro para priorizar pendências, ler diffs de fóruns/canal/memórias, manter mural de slots, cobrar protocolo da Trindade e acionar o Zelador como módulo operacional de memória. Não substitui o Vigia: Vigia monitora produção viva; CEO/Zelador organizam conhecimento, prioridades e governança.

**Fórum vivo:** [forum_zelador_passo2_modulo_cognitivo.md](./Foruns/forum_zelador_passo2_modulo_cognitivo.md)

**Modelo primário escolhido por Miguel:** Kimi / Moonshot, via `KIMI_API_KEY`, por janela de contexto longa.

**Cascata do CEO:**

1. Kimi / Moonshot — primário para long-context e síntese executiva.
2. DeepSeek V4 — fallback 1.
3. Qwen — fallback 2.
4. Gemini 3.1 — fallback 3, apenas no fim da cascata; implementação deve validar alias real disponível antes de chamada paga.

**Modo inicial obrigatório:** `--dry-run --diff-only`, sem cron e sem escrita estrutural automática. O índice diferencial fica em `/root/agent_data/ceo_index/` com `filepath`, `mtime`, `size` e `sha256`; o LLM recebe apenas diffs relevantes.

**Guarda financeira:** cada chamada do CEO precisa registrar provider/modelo/tokens/custo estimado em JSONL próprio ou Caixa Trindade antes de ativar cron. Primeiro cron só após smoke local e consenso.

**Status 2026-05-09 18:18 BRT:** Fase 0 local validada em `root/agente_ceo_cognitivo.py`, sem deploy e sem cron. Manifesto determinístico `root/agent_data/ceo_index/tree_index_manifest.json` com `schema_version=1.0` e `generated_at`; `canal_trindade.md` fica `ativo` e `can_summarize=false`. Smoke real Kimi OK com `kimi-k2.6`; após autocura de custo por `changes_para_prompt(...)` + `--max-prompt-chars`, input caiu para `2073` tokens e custo estimado do tick para `US$0.002994`. Antes de cron real, melhorar seleção contextual para evitar decisões com diff truncado demais.

**Direção Miguel 2026-05-10 03:44 BRT:** o Cérebro também deve ficar no Alibaba. Interpretação: Alibaba vira oficina pesada + biblioteca viva do Cérebro; NYC permanece failover limpo/read-only; Tencent segue produção principal. Implementação ainda bloqueada até auditoria read-only do Alibaba, separação rígida entre memória e segredos, e plano de sync sem `.env`, `chaves/`, tokens ou credenciais WP. Fórum de desenho: [forum_revisor_alibaba_swarm.md](./Foruns/forum_revisor_alibaba_swarm.md).

**Diretriz Miguel 2026-05-10 03:54 BRT:** Alibaba deve hospedar tanto o Cérebro Vivo quanto a Trindade Técnica. O Cérebro organiza memórias autonomamente e pode participar de canal/fóruns com sugestões; a Trindade Técnica (Codex, Claude e DeepSeek via API) roda monitoramento/autocura, consulta o Cérebro e decide/executa. Nada pode ser apagado por padrão; se houver problema de memória/espaço, usar Backblaze. Apagar qualquer coisa exige consenso absoluto com Miguel.

**Correção Codex 2026-05-10 04:22 BRT:** a ideia de Alibaba como Failover 2 do site fica rebaixada para histórico. Arquitetura preferida: Tencent = produção; NYC = failover frio único do site; Alibaba = Cérebro/Trindade/Memórias; Backblaze = arquivo histórico. Qualquer ordem de "expurgo" em `/root/cafezinho` deve ser interpretada como inválida até Miguel confirmar explicitamente deleção. A ação segura é inventário + cofre/quarentena + manifesto, sem apagar.

**Regra final Miguel 2026-05-10 04:43 BRT:** Alibaba não é Failover 2 e não é backup. Alibaba é Cérebro, memórias dinâmicas e Trindade. Memórias antigas devem migrar com o tempo para Backblaze, mantendo manifesto, resumo e caminho de recuperação. Alibaba deve permanecer leve: sem espelho de produção, sem vídeos pesados, sem venv/node_modules/caches/pacotes históricos.

**Separação Backblaze 2026-05-10 05:20 BRT:** são baldes diferentes. `failover-cafezinho1` guarda backup do sistema/failover/produção; `Cerebro-Memorias` guarda backup do Cérebro e memórias. Rotinas do Cérebro no Alibaba devem usar `Cerebro-Memorias`.

**Correção operacional 2026-05-10 12:57 BRT:** não confundir o alias SSH local `beijing` com Alibaba. O alias `beijing` foi validado por metadata como Tencent Beijing (`tencent_region=ap-beijing`). O Alibaba correto do Cérebro é `39.106.184.215`, host `iZ2ze82jxyxjztl5fpi651Z`, metadata `alibaba_region=cn-beijing`. Qualquer frente que diga "usar Alibaba" deve validar essa metadata antes de rodar carga, SCP, cron ou instalação. Caso a metadata não confirme Alibaba, parar e pedir revisão humana.


---

## 15. Trindade Econômica V1 — Vigia Autônomo (`root/trindade_economica_vigia.py`)

**Implementado:** 2026-05-11 17:23 BRT por Claude Opus 4.7.
**Decisão fundadora:** §45 do `CEREBRO_NODE_GOVERNANCA.md` (quórum 5/5 em 17:00 BRT).
**Fórum canônico:** `Foruns/forum_transicao_modelos_opus_sonnet_haiku_20260511.md`.
**Status atual:** deployado no Tencent/Cingapura (`/root/trindade_economica_vigia.py`, MD5 histórico `06317410ee844d72541c6e6c3ee85543` no deploy inicial). Cron ativo em 2026-05-14 07:04 BRT por autorização Miguel: `0,20,40 * * * * cd /root && /root/venv/bin/python3 /root/trindade_economica_vigia.py --ao-vivo --autocura-wp-on --telegram-on >> /root/agent_data/trindade_economica.log 2>&1 # TRINDADE_ECONOMICA_V1_20MIN_PENDING_AUTOCURA_20260514_CODEX`. Autocura continua limitada a rebaixar para `pending`, não `draft`.

### Propósito

Loop autônomo Python que executa 1 tick por invocação (cron-style), implementando o **modo Trindade Econômica V1**: DeepSeek+Kimi+Qwen deliberam por quórum técnico dentro do escopo permitido pela §45, Claude e Codex entram como observadores ativos com poder de veto e auditoria. Substitui o loop Trindade conduzido por Opus (custo ~R$ 6/tick) por trio LLM chinês (custo ~R$ 0.02/tick). Economia estimada: **85-98%** (varia por etapa de calibração — ver §45 e fórum canônico).

### Arquitetura técnica

- **1 execução = 1 tick** (cron dispara, script roda 1 ciclo e sai).
- **Helpers consultivos:** `scripts/chamar_deepseek.py`, `scripts/chamar_kimi.py`, `scripts/chamar_qwen.py` no diretório local; no Tencent, `SCRIPTS_DIR` resolve dinamicamente pra `/root/scripts/` (helpers replicados em 2026-05-11 17:23 BRT).
- **Paralelismo:** `ThreadPoolExecutor(max_workers=3)` chama os 3 helpers em paralelo por tick.
- **State persistente:** `/root/agent_data/trindade_economica_state.json` (contagem de divergências consecutivas, offlines consecutivos, ticks totais).
- **Log estruturado:** `/root/agent_data/trindade_economica.jsonl` (append-only, 1 entry/tick + 1 entry/autocura).
- **Append no canal:** bloco resumido em `Foruns/canal_trindade.md` a cada tick.

### Escopo permitido (sem escalar)

1. Curl WP API (`https://controle.ocafezinho.com/wp-json/wp/v2/posts?per_page=10&status=any`) com 3 retries.
2. Procurar sentinelas de metadiscurso em títulos: `o texto relembra`, `ja botei`, `aqui esta`, `como solicitado`, `segue a materia`, `o texto aborda`, `o texto descreve`.
3. Consultar trio em paralelo.
4. **Autocura limitada:** se quórum 3/3 unânime SIM no parser de voto, rebaixar post (`status=draft`) via WP REST. Apenas em modo `--ao-vivo`; default `--dry-run` registra mas não escreve.
5. Append no canal e JSONL.

### Escopo proibido (script não implementa, conforme §45)

Deploy de código, SSH com escrita em outros .py, edição de crontab, mudança em `motor_publicador.py`, autocura nova além de rebaixamento, publicação editorial, gasto novo, escrita em `.env`/chaves, criação de novo fórum/memória/script. Tentativa fora do escopo deve abortar com log.

### Gates de auto-pause

- **Kill switch:** arquivo `/root/agent_data/trindade_economica_KILL` existe → exit imediato com log.
- **WP fail:** 3 retries consecutivos sem HTTP 200 → exit 1 + log.
- **Offlines consecutivos:** ≥2 ticks com 1+ LLM offline → log `GATE_OFFLINES_CONSECUTIVOS` + print de alerta humano (não para, mas registra).
- **Divergência:** lógica de contagem de divergência DeepSeek×Kimi×Qwen ainda a refinar (state já contabiliza placeholder).

### Custo observado smoke

- Tick smoke local (DeepSeek+Kimi+Qwen): ~R$ 0.020 confirmado (já gravado em JSONL).
- Tick smoke remoto: idêntico.

### Cron sugerido (NÃO ativado)

```
*/15 * * * * cd /root && /root/venv/bin/python3 /root/trindade_economica_vigia.py --dry-run >> /root/agent_data/trindade_economica.log 2>&1
```

Cadência 15min validada pelo trio em 11/05 17:05 BRT (Kimi apontou WP publica ~2x/hora, 10min era overkill). Default `--dry-run` é segurança extra: ao vivo só com `--ao-vivo` explícito.

### Rollback

```bash
# Apagar arquivo (não há backup pré-deploy porque era criação nova)
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  'sudo rm /root/trindade_economica_vigia.py && sudo rm -rf /root/agent_data/trindade_economica*'

# Helpers /root/scripts/ podem ficar (não interferem em nada se vigia não rodar).
```

### Pendências (Miguel autoriza quando quiser)

1. **Ativar cron** `*/15 * * * *` no Tencent (edição do crontab — escopo proibido sem humano).
2. **Definir thresholds** finais: quantos ticks de divergência disparam pause real (não só log).
3. **Implementar shadow Opus 10%** dos ticks pra calibrar trio no primeiro mês.
4. **Smoke 24h** sob Opus monitor passivo + auditoria Codex 4h.
5. **Decisão final:** virar default ou voltar pra Etapa 1 (Opus operacional).


### NOTA §15 — Fase 1 Telegram Augusto IMPLEMENTADA (2026-05-11 18:52 BRT)

Vigia agora coleta GA4 Realtime + monta msg Augusto + estima custo USD/BRL por tick. Cron `0,30` ativo. `--telegram-on` default OFF (24h dry-run log conforme ressalva Codex+AG, voto 6/6 do `forum_telegram_augusto_fase1_20260511.md`). Próximo passo: 12/05 18:51 BRT decisão Miguel de ativar `--telegram-on` no crontab + reajustar threshold "bombando" com dados reais.

Modos da msg: BOMBANDO (top post >1000 users), ALERTA (sentinela/autocura/offline), NORMAL_CURTO (default), SILENCIO (02-06 BRT + <10 users). Mapeamento agente via `root/agente_map.json` (tabela paralela).

Pendência: kill switch via Telegram (sub-frente Fase 2 — exige edit `augusto_telegram_brain.py`).

---

## 16. Rio Carta — Arquitetura Canônica Astro/Vercel + Markdown/Git + Supabase

**Atualizado:** 2026-05-22 23:50 BRT por Codex após bloqueio DeepSeek na reforma do crontab.

**Mapa operacional canônico:** [CEREBRO_INDEX_RIOCARTA.md](./CEREBRO_INDEX_RIOCARTA.md). Se houver dúvida sobre host, cron, deploy ou legado, ler esse índice antes de canal/fórum antigo.

**Diretório canônico local:** `Rio Carta Agentes/`

**Frontend:** `Rio Carta Agentes/rio_carta/`, Astro hospedado na Vercel.

**Publicação canônica:** arquivos Markdown em `rio_carta/src/content/blog/`, com frontmatter compatível com `src/content.config.ts`: `title`, `description`, `pubDate`, `updatedDate` opcional, `heroImage` opcional, `wp_id` legado opcional e `tags` opcional. Deploy por `git push origin main` no repositório Astro.

**Comentários/engajamento:** Supabase via componentes do frontend Astro. WordPress não é backend operacional de comentários.

**WordPress Rio Carta:** legado/migração. Não é canal de publicação dos agentes. Chamadas a `/wp-json/wp/v2/posts`, upload de mídia WP, categorias/tags WP e injetor de Cesta Premium WP não pertencem ao pipeline operacional novo.

**Silo Python:** `Rio Carta Agentes/root/` pode coletar, curar, redigir, auditar, baixar imagem e gerar Markdown. Não deve postar por REST WP. A função de publicação deve ser canônica e portável:

- resolver o repositório Astro por `RIOCARTA_ASTRO_REPO` ou busca segura (`/root/rio_carta` no Droplet, `../rio_carta` local);
- criar `.md` em `src/content/blog/`;
- salvar imagem em `public/hero/` quando houver;
- rodar build/smoke local quando aplicável;
- só executar `git add/commit/push` fora de dry-run e com rollback/log.

**Estado remoto histórico em 2026-05-11 22:54 BRT:** Droplet auditado `159.89.185.209` com `crontab` vazio. Esse dado foi superado pelos sprints de 15/05.

**Estado remoto vivo em 2026-05-22 23:50 BRT:** Droplet `159.89.185.209` (`agente-clone-01`) é o executor vivo do Rio Carta. `riocarta_admin.service` está ativo. O crontab root contém coleta rotativa, publicação remota e indexador Google. O clone operacional fica em `/root/riocarta_remote/rio_carta/`; o publicador remoto é `/root/riocarta_remote_publish.sh`; o fluxo final é GitHub -> Vercel. Tencent/Cingapura tem arquivos Rio Carta antigos sem cron visível; Tencent/Beijing não é executor Rio Carta.

**Execução Codex 2026-05-11 23:12 BRT:** primeira refatoração local aplicada. `riocarta_publicador_tematicos.py` passou a publicar Markdown/Astro com validação de repo Git, dry-run sem push e imagem em `public/hero/`. `riocarta_agente_master.py` deixou de fazer POST WordPress no final e só marca pauta como postada depois de publicação Markdown bem-sucedida. `riocarta_agente_injetor_premium.py` foi desativado como stub seguro. `riocarta_carregar_chaves.py` só exige credencial WP em modo legado explícito.

**Validações 2026-05-11 23:12 BRT:** `py_compile` OK nos scripts tocados; dry-run Markdown OK; `npm run build` no Astro OK com 1912 páginas; busca por strings críticas WP nos três arquivos operacionais tocados vazia; repo Astro limpo após build; `crontab` remoto segue vazio.

**Diretriz editorial/operacional fundadora 2026-05-11 23:01 BRT:** Rio Carta é portal 100% Rio de Janeiro, com coleta em RSS/cadernos locais e ângulo fluminense/carioca. Backbone barato com DeepSeek/Kimi/Qwen para redação, auditoria e curadoria. Banco de imagens do Cafezinho pode ser reaproveitado como fonte barata, mas sem upload WP. Tribunal Visual/IA generativa são fallback condicionado, preferencialmente usando motores chineses quando tecnicamente viável.

**Pendências técnicas prioritárias:**

- Mapear fontes RSS/cadernos locais do Rio de Janeiro e ajustar `riocarta_robo_coleta.py`.
- Transformar banco de imagens/Tribunal Visual em fallback barato sem upload WP.
- Revisar `riocarta_interlink_interno.py` e `riocarta_gerenciador_imagens.py` para eliminar dependência operacional de WordPress.
- Rotacionar credenciais expostas anteriormente em fórum antes de qualquer cron de produção.

**Fóruns canônicos:** `Rio Carta Agentes/Foruns/forum_arquitetura_v1_riocarta.md`, `Rio Carta Agentes/Foruns/forum_rio_carta_migracao.md`, `Rio Carta Agentes/Foruns/credenciais.md` (inventário seguro, sem valores).

**Diretriz Miguel 2026-05-11 23:32 BRT — isolamento total:** Rio Carta não pode colocar o Cafezinho em risco. Nenhum agente/script operacional Rio Carta pode importar, ler, escrever, publicar, comentar, fazer deploy, buscar dependência ou usar credencial do Cafezinho ou de outro projeto. Todos os agentes Python Rio Carta devem ter prefixo `riocarta_` ou `rio_carta`/`rio-carta`. Reuso de recurso só por cópia explícita para dentro do silo Rio Carta, nunca referência viva.

**Correção Codex 2026-05-11 23:32 BRT:** removidos fallback `CAFEZINHO_ROOT` do deploy, imports de `motor_publicador`, caminho externo no `sys.path` do master, alvos externos do comentarista, personas externas, links sociais do header para `ocafezinho`, scratch scripts fora do padrão e caches `.pyc` legados. Validação: `py_compile` dos `riocarta_*.py` OK; `bash -n deploy_riocarta.sh` OK; todos os `.py` do silo têm prefixo `riocarta_`; busca operacional por `Cafezinho/ocafezinho/motor_publicador/CAFEZINHO_ROOT/GSN` em `root`, deploy, header e índice Rio Carta vazia.

---

## 17. Pendência Arquitetural — Unificar Fóruns no Diretório Raiz

**Registrado:** 2026-05-11 23:22 BRT por Codex, a pedido de Miguel.

**Diretriz:** os fóruns devem ficar no diretório raiz do workspace, não espalhados dentro de silos como `Projeto Cafezinho Agentes/Foruns/` e `Rio Carta Agentes/Foruns/`.

**Objetivo:** criar uma raiz canônica única para governança, leitura por agentes e reindexação do Cérebro, reduzindo caminhos duplicados e risco de agentes consultarem fórum errado.

**Plano preliminar aprovado por Miguel:**

- Inventariar todos os diretórios `Foruns/` existentes em `Projeto Cafezinho Agentes/`, `Rio Carta Agentes/` e outros silos.
- Definir raiz canônica única, provavelmente `Foruns/` diretamente em `/home/migueldorosario/Downloads/Antigravity Google/`.
- Escolher estratégia anti-colisão: subpastas por projeto (`Foruns/Cafezinho/`, `Foruns/RioCarta/`) ou prefixos (`cafezinho_*`, `riocarta_*`).
- Atualizar referências internas em Cérebro Nodes, canais, memórias e scripts que apontam para caminhos antigos.
- Rodar varredura com `rg "Foruns/"` para localizar dependências hard-coded.
- Reindexar o Cérebro e corrigir links quebrados.
- Rodar `validar_cerebro.py` até ficar sem erro crítico.
- Só depois apagar diretórios antigos ou transformá-los em ponteiros/README de compatibilidade.

**Risco principal:** scripts e agentes podem ler fóruns por caminho fixo. A migração deve começar com mapa de dependências e pode usar etapa intermediária com symlinks/ponteiros para evitar quebra operacional.

**Status:** pendente. Não executar migração sem nova ordem explícita de Miguel.
## STATUS-20260513-TOPOLOGIA-SERVIDORES-E-VIGIA-CHINES-CAFEZINHO

Checagem Codex em 2026-05-13 10:40 BRT, corrigida apos observacao de Miguel em 10:49 BRT.

Topologia canonica:

- NYC/DigitalOcean: failover frio do Cafezinho e casa de outros sites/projetos. Nao deve receber loop pesado por padrao.
- Tencent/Cingapura: servidor principal do Cafezinho, onde ficam os agentes de producao.
- Tencent/Beijing: servidor separado para agente estatistico chines, usado esporadicamente para dados do governo chines, comercio exterior e similares. Alias local `beijing` aponta para este Tencent Beijing, nao para Alibaba.
- Alibaba/Beijing `39.106.184.215`: casa do Cerebro Vivo, Trindade Tecnica e memorias. Nao e failover do site e nao e publicador Cafezinho por padrao.

Estado observado:

- Alibaba direto `39.106.184.215`: nao ha vigia do Cafezinho identificado rodando. O crontab mostra apenas o CEO do cerebro/Kimi em `/root/cerebro_trindade/root`, uma vez por dia, as 03:00 no horario do servidor Alibaba. Tambem aparecem agentes de monitoramento nativos da Alibaba Cloud (`cloudmonitor`/`aegis`), que nao sao vigia editorial do Cafezinho.
- Tencent/Beijing alias `beijing`: nao apareceu processo de Cafezinho/vigia na checagem simples; isso e esperado porque esse servidor nao e o principal do Cafezinho.
- Tencent/Cingapura: ha processos vivos de `agente_comentarista.py --engajar-novo-post ... --site cafezinho`, com locks recentes em `/tmp/comentarista_lock_cafezinho_*.lock`. Isso indica operacao de comentarios/engajamento do Cafezinho em andamento no servidor principal.
- Tencent/Cingapura cron root: o vigia chines/Trindade Economica do Cafezinho esta ativo de 2 em 2 horas, linha `0 */2 * * *`, com `--ao-vivo --telegram-on`, sem autocura WP autonoma.
- Local: `monitor_publicacao_rio_cafezinho.sh` esta ativo a cada 2 horas em minuto 35 das horas impares (`35 1-23/2 * * *`), registrando em `root/agent_data/monitor_publicacao_rio_cafezinho.log`.
- Local: `agente_vigilante.py` antigo continua desativado desde 2026-04-24.

Conclusao:

Nao existe vigia Cafezinho ativo no Alibaba. O vigia chines do Cafezinho que Miguel citou esta no Tencent/Cingapura. O que esta operando hoje e:

1. monitor local Rio/Cafezinho de 2 em 2 horas;
2. vigia chines/Trindade Economica no Tencent/Cingapura de 2 em 2 horas;
3. comentaristas do Cafezinho disparados no Tencent/Cingapura por fluxo operacional de posts.

Regra para evitar nova confusao:

- Quando alguem disser "Beijing", confirmar se fala de Tencent/Beijing estatistico ou Alibaba/Beijing Cerebro.
- Quando alguem disser "vigia chines do Cafezinho", assumir Tencent/Cingapura, salvo se Miguel especificar migracao.


---

## §X — Nome formal: "Agente YouTube Semi-Autômato" (batizado 2026-05-15 01:30 BRT)

**Origem:** Miguel 15/05 01:30 BRT — definiu nome do pipeline YouTube que combina curadoria humana de URLs + automação pós-injeção.

### Componentes
- `scratch/injetar_dicas_youtube.py` — injeção manual de URLs curadas por Miguel via fórum/Augusto
- `youtube_inbox.py` — fila persistente JSONL com flags `prioridade_manual`, `dica_miguel`, `entrevistado_canonico` (§64.7 + Codex 14/05 §64.3)
- `agente_youtube.py` — coletor, baixa transcrição via Transkriptor
- `agente_youtube_publicador.py` — Editor/Redator/Revisor + guardrails Codex 13/05 22:52 (atribuição/personagem/citação) + auditoria diversa
- Cron `35 * * * *` — publicador horário (§64.1, autorização §55.2 Miguel)
- Cadeia auditoria: qwen3-max → qwen-max-latest → qwen-plus-latest → deepseek-chat (§66.2)

### Modo de operação
"Híbrido, meio autônomo meio controlado" (Miguel): humano cura lista → máquina prepara/transcreve/audita/publica em draft → humano aprova `/aprovar 247xxx` → publish.

### NÃO confundir com
- **Caçador/Cortador YouTube** — agente próprio (`cortador_youtube.py` + `/clipar URL ini fim`), corta shorts vertical pra X/TikTok/Reels (FFmpeg). Função diferente, agente independente.
- **Publicador Híbrido YT antigo** — fórum 11/05 (Antigravity) com prefixo `Vídeo:` + canal tvcafezinho + OAuth2. Descartado.

— Claude, 2026-05-15 01:32 BRT

### Complemento Codex 2026-05-15 01:29 BRT — Zizilinda Z1 e fronteira LLM

Miguel separou duas camadas:

- **Bot Zizilinda:** camada conversacional/triagem/briefing. Por ordem Miguel 2026-05-15 02:36 BRT, deve operar chineses-only no Telegram. Provedores LLM permitidos no bot: `qwen`, `kimi`, `deepseek`. Sem OpenAI, Anthropic/Claude, Gemini/Google, Mistral, Groq, xAI/Grok, Perplexity, Assembly, FAL, Ideogram ou DALL-E no ambiente/código do processo.
- **Agentes publicadores / Agente YouTube Semi-Autômato:** camada editorial de publicação. Pode manter redação de luxo com OpenAI/Sonnet quando autorizado; revisão, auditoria e fact-checking devem evitar repetição do mesmo modelo e usar diversidade.

Implementação Tencent/Cingapura:

- `/root/start_zizi.sh` protegido com `flock` em `/var/lock/zizi.lock`, dry-run `ZIZI_START_DRY_RUN=1` e abort seguro `exit 0` em lock ocupado.
- `/root/bot_zizi_linda.py` zera chaves ocidentais dentro do processo da Zizi e limita `/modelo`/fallback a `qwen`, `kimi`, `deepseek`.
- `_llm_simple` não usa mais o roteador geral para evitar fallback caro/acidental.
- Zizi não foi religada nesta etapa; Z1 preparou base segura para smoke futuro.

Atualização Codex 2026-05-15 02:45 BRT:

- Zizi estava ativa e foi endurecida para chineses-only estrito.
- `/root/start_zizi.sh` agora remove chaves/modelos ocidentais antes do `exec` do bot.
- Validação de ambiente do processo após restart: só permaneceram chaves chinesas (`QWEN_API_KEY`, `KIMI/MOONSHOT_API_KEY`, `DEEPSEEK_API_KEY`, `ZHIPU_API_KEY`) e serviços não-LLM como Brave/Transkriptor/Uptime/WP.
- `zizi.service` reiniciado e `active`.
- Rollback remoto: restaurar `/root/bot_zizi_linda.py.bak_pre_zizi_chinese_only_strict3_20260515_024454_codex` e `/root/start_zizi.sh.bak_pre_zizi_chinese_only_env3_20260515_024454_codex`, rodar `py_compile` e `systemctl restart zizi.service`.

Backups remotos:

- `/root/start_zizi.sh.bak_pre_zizi_z1_20260515_012334_codex`
- `/root/bot_zizi_linda.py.bak_pre_zizi_z1_llm_20260515_012801_codex`

### Complemento Codex 2026-05-15 09:52 BRT — Z2-minimal `/post_video` validado

Recorte executável sob sprint autônomo Miguel/Claude/Codex:

- Zizilinda ganhou apenas `/post_video <URL_YOUTUBE> [nome]`.
- O comando valida autorização/chat, extrai `video_id`, evita duplicata em inbox/vistos/outbox e chama `coletar_transcricao_yt()` com `prioridade_manual=True`, `dica_zizi=True`, `ordem_dica=time()` e `chat_id_origem`.
- `agente_youtube.py` propaga `dica_zizi`, `entrevistado_canonico`, `language` e `chat_id_origem` para `youtube_inbox.gravar()`.
- `youtube_inbox.py` persiste `dica_zizi` e `meta_extra.origem=zizilinda` para o publicador reconhecer origem.
- Não foram adicionados `/aprovar` nem `/rejeitar`; nada mexe diretamente em status WordPress.

Validações remotas no Tencent:

- `sudo /root/venv/bin/python3 -m py_compile bot_zizi_linda.py agente_youtube.py youtube_inbox.py` OK.
- Smoke zero-write de `youtube_inbox.gravar()` em inbox temporária confirmou `dica_zizi=True` e `prioridade_manual=True`.
- Dry smoke do URL `https://youtu.be/G7EXnvfqqsM` extraiu `G7EXnvfqqsM`. Busca ampliada depois confirmou que esse vídeo já estava no outbox de maio como post `247116`, então o handler deve recusá-lo como duplicata se Miguel testar exatamente esse URL.
- `zizi.service` ativo com 1 processo real.

Backups/snapshots remotos pós-validação:

- `/root/Backups/bot_zizi_linda.py.snapshot_z2_minimal_validated_20260515_0948_codex`
- `/root/Backups/agente_youtube.py.snapshot_z2_minimal_validated_20260515_0948_codex`
- `/root/Backups/youtube_inbox.py.snapshot_z2_minimal_validated_20260515_0948_codex`

Rollback:

```bash
sudo cp -a /root/Backups/bot_zizi_linda.py.snapshot_z2_minimal_validated_20260515_0948_codex /root/bot_zizi_linda.py
sudo cp -a /root/Backups/agente_youtube.py.snapshot_z2_minimal_validated_20260515_0948_codex /root/agente_youtube.py
sudo cp -a /root/Backups/youtube_inbox.py.snapshot_z2_minimal_validated_20260515_0948_codex /root/youtube_inbox.py
cd /root && sudo /root/venv/bin/python3 -m py_compile bot_zizi_linda.py agente_youtube.py youtube_inbox.py
sudo systemctl restart zizi.service && systemctl is-active zizi.service
```

## §Y — Rio Carta: cron rotativo de coleta restaurado (2026-05-15)

**Origem:** Rio Carta parou após `crontab -r` no Droplet `159.89.185.209` em 2026-05-12 14:39 BRT. Investigação Claude/Codex mostrou que a causa real era ausência de cron, não DeepSeek.

**Deploy Codex 2026-05-15 02:41 BRT:**

- Criado `/root/riocarta_cron_rotativo.sh` no Droplet.
- O wrapper alterna `capital`, `metropolitana` e `interior`.
- Chama `/root/riocarta_cron_coleta.sh` com `RIOCARTA_PYTHON=/root/venv/bin/python3`.
- Cadência em BRT:
  - 06h-23h59: a cada 30 minutos;
  - 00h-05h59: a cada 1 hora.
- Como o servidor usa UTC, o crontab usa `0,30 0-2,9-23` e `0 3-8`.

**Escopo:** coleta. Não há evidência histórica de master/publicador por cron; geração/publicação end-to-end LLM é sprint separado.

**Backup remoto:** `/root/crontab_backup_pre_riocarta_rotativo_20260515_024104_codex.txt`.


## [2026-05-15 14:10 BRT] DigitalOcean/Rio Carta - chave publica SSH operacional do Droplet Astro

Servidor: `agente-clone-01` / `159.89.185.209` / funcao Astro/API Rio Carta e rede de sites.

Chave publica autorizada para acesso root:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFfXIj3Has1WDRbn95V89g/YpJ6tSXIu3CF3yB9vTbHm migueldorosario@novo
```

Fingerprint:

```text
256 SHA256:wB+pG1u1dDKyxP9bQSRDIzl+4Uxj6QD45Px6AL/dQqI migueldorosario@novo (ED25519)
```

Comando recomendado:

```bash
ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209
```

Historico do incidente: em 2026-05-15, Codex perdeu tempo tratando como bloqueio novo porque nao consultou primeiro o historico. A recuperacao estava documentada em `Projeto Cafezinho Agentes/scratch/scratch_ssh.py`, arquivo antigo de bootstrap do Antigravity. Forum completo: `Rio Carta Agentes/Foruns/forum_riocarta_ssh_droplet_20260515.md`.

Regra: a senha/procedimento sensivel de recuperacao nao deve ser copiado aqui; este no contem apenas chave publica, fingerprint e caminho do registro historico.

## [2026-05-15 15:35 BRT] Politica de custo Perplexity no motor_publicador.py

Origem: investigacao Claude/Codex apos Miguel detectar salto Perplexity de ~200 para ~480 requisicoes/dia.

Diagnostico: o aumento veio do sprint Codex de 2026-05-14 16:04-16:17 BRT, que colocou Perplexity como checagem factual no `motor_publicador.py` para evitar cadeia `Sonnet -> Sonnet -> Sonnet`. O toque das 22:20 BRT no mesmo arquivo foi outro ajuste, ligado a DeepSeek V4/tokens, e confundiu o rastreio pelo `mtime`.

Correcao aceita: Claude removeu Perplexity da camada intermediaria `auditar_com_claude()`, preservando checagem cedo e checagem final. Codex concorda com a remocao.

Regra arquitetural: Perplexity e validador factual caro. Padrao maximo: 2 chamadas Perplexity por materia publicada, uma cedo sobre fatos/pauta e uma final sobre texto gerado. Auditoria intermediaria deve usar LLM diversa e mais barata, salvo excecao registrada em forum com motivo e rollback.


## [2026-05-16 14:17 BRT] Direção futura - Cafezinho autônomo e backup próprio

Miguel apontou uma frente de médio/longo prazo: o Cafezinho não deve ficar dependente apenas do WordPress atual/servidor do provedor. A direção é caminhar em duas frentes, sem execução imediata neste tick:

- obter/organizar backup próprio do banco de dados do WordPress do Cafezinho;
- manter cópia/backup em Backblaze B2 sob controle próprio;
- estudar um Cafezinho paralelo, leve e autônomo em modelo semelhante ao Rio Carta, usando Tencent/DigitalOcean como laboratório/infra;
- em paralelo, aumentar o controle operacional do servidor WordPress atual, com acessos, autorizações, limpeza e redução de sujeira de banco;
- tratar isso como arquitetura e plano, não como failover ou migração imediata.

Qualquer ação concreta nessa frente continua exigindo fórum, inventário, backup, rollback, autorização humana quando envolver credenciais/servidor/banco, e validação sem risco ao Cafezinho vivo.

## [2026-05-16 15:47 BRT] Rio Carta - arquitetura inicial para breaking news

Miguel pediu que a Trindade pense uma arquitetura de breaking news para o Rio Carta, possivelmente usando Brave Search e fontes como G1, Metropoles, Folha, Reuters e similares.

Diretriz inicial: não criar cron nem publicar automaticamente no primeiro passo. O caminho seguro é uma sentinela read-only, isolada no silo Rio Carta, rodando em dry-run por 24h, com ledger deduplicado, pontuação de urgência, registro de fontes e geração apenas de candidatos/drafts. Só depois de auditoria de precisão/custo a Trindade deve propor cadência, fontes finais e status-gate editorial.

Fórum aberto: `Projeto Cafezinho Agentes/Foruns/forum_breaking_news_politica_20260516.md`.

## [2026-05-16 16:45 BRT] Arquitetura de integração entre Cafezinho, GSN e Rio Carta

Miguel definiu duas direções complementares via Telegram/Augusto:

- **GSN + Cafezinho:** não duplicar trabalho do agente YouTube. A transcrição/coleta/artigo-base deve nascer como artefato canônico único, com adaptadores de saída: Cafezinho em português/WordPress e Global South News em inglês/Astro.
- **Rio Carta + Cafezinho:** matérias fortes do Rio Carta podem alimentar o Cafezinho, mas por fila seletiva, adaptação editorial e filtros de relevância nacional. Rio Carta mantém liberdade própria.

Regra arquitetural: preferir `coleta única -> artefato canônico -> adaptadores por destino`, compartilhando ledger, custos e validação factual. Publicação cruzada deve começar em dry-run/draft/status-gate, sem `publish` direto no Cafezinho.

Fóruns atualizados: `Foruns/forum_gsn_arquitetura_espelho_cafezinho_20260516.md` e `Foruns/forum_cafezinho_media_group_20260516.md`.

## [2026-05-16 17:45 BRT] Cafezinho sob controle do Cérebro + retomada Mundo Trilhos/Rail Post

Miguel reforçou via Telegram/Augusto que o Cafezinho precisa ficar sob controle técnico completo do Cérebro: WordPress, plugins, anúncios, arquitetura, backups e dependências do servidor. Isso complementa a frente já aberta de autonomia WordPress/Cafezinho paralelo.

Diretriz operacional: tratar primeiro como inventário e arquitetura. Não mexer em banco, credenciais, plugins, anúncios, DNS, servidor ou publicação viva sem fase própria, backup, rollback e autorização explícita quando envolver produção.

Também pediu retomar Mundo Trilhos e Rail Post como experiência de sites gêmeos, com Mundo Trilhos em português e Rail Post em inglês. Busca local Codex confirmou que a base não está perdida:

- sites Astro locais: `Projeto Cafezinho Agentes/mundo_trilhos/` e `Projeto Cafezinho Agentes/rail_post/`;
- ambos têm `package.json`, `astro.config.mjs`, `src/`, logos e posts fantasma `src/content/blog/fake-post-0.md` a `fake-post-9.md`;
- agentes/dados existentes: `root/agente_ferroviario_v2.py`, `root/agente_rail_post.py`, `root/bot_mundodostrilhos_v_1.py`, `root/agent_data_trilhos/`;
- `agent_data_trilhos` contém diretrizes, curadoria, memória, rascunhos e imagens de abril de 2026.

### Confirmação de Domínios (DNS apontado para Vercel)
Em 2026-05-16, a infraestrutura DNS dos três portais autônomos foi devidamente apontada via CNAME/A Record para o IP da Vercel (`76.76.21.21`):
1. **Global South News (GSN)**: `globalsouth.news`
2. **Mundo Trilhos**: `mundotrilhos.com`
3. **Rail Post**: `railpost.news`

Próximo passo seguro: auditoria local read-only/build dos dois sites Astro, configurar o `astro.config.mjs` com os novos domínios, atualizar identidade/interlinks "duas bolas" e preencher com posts fantasmas para a inauguração do fim de semana.

## [2026-05-22 00:38 BRT] Mundo Trilhos — decisão headless/Astro/Vercel

Miguel pediu espalhar pela Trindade a decisão arquitetural do Mundo Trilhos. O portal deve abandonar a publicação WordPress e operar como site headless/Astro/Vercel, com geração de Markdown e deploy por Git.

Diretriz consolidada:

- domínio `mundotrilhos.com` tratado como Vercel/headless;
- arquivo legado principal a auditar: `root/agente_ferroviario_v2.py`;
- saída futura: Markdown em `mundo_trilhos/src/content/blog/`;
- publicação: `git commit` + `git push`, com Vercel fazendo build;
- WordPress e banco relacional saem do caminho do Mundo Trilhos;
- Perplexity não entra no pipeline Mundo Trilhos durante esta reforma;
- pipeline editorial deve ser 100% asiático, seguindo a arquitetura registrada no `Foruns/forum_mundo_trilhos.md`.

Distribuição inicial de sprint:

- DeepSeek: auditar `agente_ferroviario_v2.py` e propor pontos de remoção WordPress/contrato Markdown;
- Kimi Code: confirmar contrato Astro/Vercel do repositório Mundo Trilhos;
- Claude Monitor: monitorar domínio/status/placeholder/metalinguagem;
- Antigravity: revisão arquitetural sem código/deploy;
- Codex Maestro: coordenação, validação de backup/rollback e liberação posterior.

Regra de segurança: antes de qualquer patch real, confirmar path canônico do repo, criar backup, gerar somente `draft: true`, validar antimetalinguagem e só depois considerar commit/push.

---

## §91 Tutorial de Monitoramento — Loop Maestro (2026-05-27)

Tutorial completo para qualquer agente da Trindade assumir o loop de monitoramento 30/30min.

- **Tutorial:** [tutoriais/tutorial_monitoramento_loop_maestro.md](./tutoriais/tutorial_monitoramento_loop_maestro.md)
- **Conteúdo:** Pré-requisitos (SSH, WP REST), 7 etapas do tick (coleta, qualidade, análise, autocura, fórum, report, boletim), mapa de logs, mapa de cascatas LLM, guards §86, checklist para novo agente
- **Relatórios diários:** `Foruns/monitoramento/YYYY/MM/forum_monitoramento_YYYYMMDD.md`
- **Boletim News (link vivo):** `CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md` → seção "RELATÓRIO EM ANDAMENTO"
- **Circuito futuro:** `Foruns/forum_circuito_monitoramento_diretrizes_20260527.md`

---

## §Arquitetura de Publicação V4.1 — Mapa canônico (2026-08-25)

**Mapa completo da cadeia de publicação do ocafezinho** (coleta → intake/tese → v41_ciclo */2h → 3º checador → publicação CM/AGY slots ~30min → WP), publicadores paralelos (repetidor estatal publish direto, YouTube, temáticos, Rio Carta), pontos de acúmulo (52 drafts V4.1, 361 pending, cats órfãs, no-home) e armadilhas técnicas (`term_taxonomy_id≠term_id`; bloco Tecnologia `$excludes` canibaliza posts multi-cat; cat 19936 morta no tema; crons V4 "desligados" por comentário inline ainda rodam).

- **Fórum (decisões+veredito do bloco TECNOLOGIA A/B/C+D):** [Foruns/forum_mapa_arquitetura_publicacao_20260825.md](./Foruns/forum_mapa_arquitetura_publicacao_20260825.md)
- **Memória (provas/comandos):** [Memorias/memoria_mapa_arquitetura_publicacao_20260825.md](./Memorias/memoria_mapa_arquitetura_publicacao_20260825.md)
- **Pergunta viva aos loops:** [Foruns/inbox_trindade/de_zcode.md](./Foruns/inbox_trindade/de_zcode.md) (ref ZM-20260825-018)

— ZCode/GLM-5.3 · 25/08/2026 12:30 BRT
- **[30/08/2026] Portal parado / Bloco Nacional vazio — fix estrutural:** `forum_portal_bloco_nacional_vazio_20260830.md` + `memoria_portal_bloco_nacional_vazio_20260830.md` (ZM): _CATS_NASCIMENTO ganha nacional[22,2403]/economia[43,2403]/geopolitica[5003,15,2403]; retro-fix 22 posts; wpcron 1min; lição --by=id.

- **V41_TECH_SEM_NEXO_20260831 + V41_TX_CASCADE_20260831 (ZM, ordem Miguel "blocos parados"):** (1) intake tecnologia — nexo geopolítico virou prioridade/badge, não veto (backups .bak_pre_tech_sem_nexo / _cascata_assemblyai / _hint_assemblyai no NYC); (2) cascata transcrição YouTube = supadata→assemblyai→transkriptor (assemblyai = chave viva; antes VAZIA na prática); (3) 268236 Cultura→Geopolítica (canônico+espelho). Fórum: Foruns/forum_portal_blocos_tech_ia_268236_transcricao_20260831.md

<!-- CATALOG_20260909_ZCODE_QWEN38: Rio Carta × Banco V-Ouro FASE 0 -->
- `Foruns/forum_riocarta_banco_vouro_fase0_20260909.md` — Rio Carta com acesso EFETIVO ao Banco V-Ouro (espelho NYC + cron seg 06:20), carinho Couto, pesquisa RJ obrigatória, purga Paes + guarda curadoria (09/09/2026)
- `Memorias/memoria_riocarta_banco_vouro_fase0_20260909.md` — log técnico: FASE 0 morta→viva, manifesto RJ +40 mídias, GUARDA_CURADORIA no robô V3, matcher sem tokens soltos, espelho 1301 mídias
