# CEREBRO_NODE_CHECKUPS

Registro canônico dos checkups operacionais do ecossistema Cafezinho/Trindade.

---


## CHECKUP-005 — Ecossistema inteiro: operacional porém degradado; produção nova zerada vive de backlog

**Data:** 2026-08-01 (data-base 10h30 BRT; registrado 12h00 BRT)
**Janela:** diagnóstico amplo de saúde (LLMs + agentes + pipelines), sem smokes pagos novos
**Executor:** diagnóstico entregue pelo Miguel; arquivado por Kimi K3 (ZCode)

### Veredito

- Publicadores V4 entregam (9 posts em 01/08), mas **Produtor V4 compartilhado terminou quase todos os ciclos com 0 aprovados** — entrega atual depende de backlog auditado.
- Cadeia da falha de produção: GLM 4.5 Flash (gerador predominante) → resposta vazia/JSON inválido → auditoria vazia → "fonte sem texto" → item abandonado. Ceará Digital e Rio Carta: 3 ciclos, 0 publicações.
- Cascata LLM sem redundância **por saldo**: DeepSeek 402, Kimi/Moonshot 429, GLM 4 Plus sem saldo, Gemini com evidência contraditória (juiz visual funciona vs. crédito esgotado 28/07). De fato restam: GLM 4.5 Flash (instável), Qwen Plus (latência alta), GPT-5.5 (resposta vazia quebra YouTube).
- Componente mais doente: **YouTube Cafezinho** (tracebacks, yt-dlp ausente, GPT-5.5 vazio, Transkriptor instável) — único com desperdício medido: US$ 0,36/transcrição rejeitada.
- Pontos sadios: Orquestrador V4 🟢, Publicador V4 🟢, pipeline editorial V4 Labs/WP 🟢 (68+5 testes), YouTube Mapa Rio 🟢.

### Prioridades registradas

- **P0:** consertar YouTube Cafezinho; recarregar/remover DeepSeek+Kimi da cascata; retry+validação GLM antes do parse.
- **P1:** investigar 0 aprovados pós-auditoria; unificar credenciais Gemini + limpar circuit breakers; corrigir "fonte sem texto" na ingestão.
- **P2:** reconciliar inventário de ~104 agentes (doc de maio) com parque V4 real.

### Fontes canônicas

- Fórum: `Foruns/forum_diagnostico_saude_ecossistema_20260801.md`
- Memória (tabelas completas LLM/agentes): `Memorias/memoria_diagnostico_saude_ecossistema_20260801.md`
- Origens do diagnóstico: `agent_data/v4/cron_v4.log`, `agent_data/v4_cafezinho_youtube/cron.log`, `agentes_tematicos/v4/nucleo_llm.py`, `root/config/llm_ratings.json`

## CHECKUP-004 — V4: Ajuste de fixture do healthcheck Vision (run14)

**Data:** 2026-07-16
**Janela:** correção da causa de falso negativo
**Executor:** Codex

### Objetivo

- Corrigir o `vision_healthcheck_cli.py` para não usar amostra de imagem inválida (1×1 px) que forçava erro remoto de Qwen.
- Validar nova rodada de healthcheck Vision.

### Alteração executada

- Alteração em `Projeto Cafezinho Agentes/root/v4_labs/codigo/vision_healthcheck_cli.py`:
  - imagem base64 atualizada para PNG 64×64.
  - `request.image.width`/`height` atualizados para `64`.

### Resultado

- `v4_memoria/foruns/healthcheck_vision_v4_20260716_run14.json`
- `case_count`: 7
- `ok_count`: 3
- `status`: `degraded`

### Detalhe por cenário

- ✅ `current_env`: OK
- ✅ `with_invalid_das`: OK
- ✅ `with_qwen_2_only`: OK
- ❌ `no_media_keys`: `media_vision_api_key_missing`
- ❌ `with_invalid_gemini`: `gemini_request_failed`
- ❌ `with_invalid_qwen`: `qwen_http_status:401`
- ❌ `without_qwen`: `gemini_request_failed`

### Impacto

- A falha de “degradado” causada exclusivamente pela imagem de teste foi resolvida.
- Persistem falhas esperadas em cenários de Gemini com credenciais/serviço atuais (não em montagem de cenário).

### Fonte canônica

- `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716_run14.md`

## CHECKUP-003 — V4: Corrigir diagnóstico de Vision (run de saúde mais estrito)

**Data:** 2026-07-16
**Janela:** correção de falsos negativos de cenários de visão
**Executor:** Codex

### Objetivo

- Corrigir o runner de healthcheck Vision para que cenários inválidos não removam indevidamente chaves de ambiente e não gerem diagnósticos enganadores.
- Registrar uma nova rodagem canônica de healthcheck Vision para retomada.

### Alteração executada

- Novo runner canônico criado: `Projeto Cafezinho Agentes/root/v4_labs/codigo/vision_healthcheck_cli.py`
- Execução aplicada com base em `.env.unificado` via clone limpo por cenário.

### Resultado

- `v4_memoria/foruns/healthcheck_vision_v4_20260716_run11.json`
- `case_count`: 7
- `ok_count`: 0
- `status`: `degraded`

Cenários principais:

- `current_env`: `media_vision_all_providers_failed`
- `no_media_keys`: `media_vision_api_key_missing`
- `with_invalid_das`: `media_vision_all_providers_failed`
- `with_invalid_gemini`: `gemini_request_failed`
- `with_invalid_qwen`: `qwen_http_status:401`
- `with_qwen_2_only`: `qwen_http_status:400`
- `without_qwen`: `gemini_request_failed`

### Impacto

- O problema de visão degradação por remoção indevida de variáveis em cenários foi sanado no método de diagnóstico.
- A degradação persistente permanece por indisponibilidade operacional dos provedores (respostas HTTP 400/401), não por falha de montagem dos cenários.

### Fonte canônica complementar

- `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716_run11.md`

## CHECKUP-002 — V4: Retomada de drafts com imagem destacada (status final corrigido)

**Data:** 2026-07-16  
**Janela:** correção de inconsistência operacional e indexação  
**Executor:** Codex  

### Objetivo

- Confirmar 8 testes (2 por editoria) em `draft` com imagem destacada em WordPress.
- Executar healthcheck de LLM e Vision para bloqueios reais antes de qualquer próxima etapa de publicação.

### Resultado

- 8 posts em estado `draft` confirmados com `featured_media` válido:
  - `261601`, `261602`, `261603`, `261604`, `261605`, `261606`, `261607`, `261608`.
- Healthcheck LLM: `24/24` OK em `v4_memoria/foruns/healthcheck_llm_matrix_v4_20260716_run9.json`.
- Healthcheck Vision: `0/7` OK, `degraded` em `v4_memoria/foruns/healthcheck_vision_v4_20260716_run9.json`.

### Fonte canônica (registro principal)

- `v4_memoria/foruns/forum_retomada_v4_imagens_drafts_20260716_run9.md`

## CHECKUP-001 — Pausa total do ecossistema Tencent para auditoria

**Data:** 2026-06-01  
**Janela:** 21:12-21:48 BRT  
**Executor:** Codex  
**Motivo:** noite de check-up; Miguel identificou deterioração editorial/operacional e pediu pausar tudo para investigação e religamento gradual. Claude prepara relatório paralelo do sistema.

### Contexto

Incidentes que motivaram a pausa:

- Vazamento de JavaScript/newsletter no post BRB/Master `254854`.
- Repetição/cluster BRB/Master e fragilidade do dedupe.
- Suspeita de deterioração nas últimas horas.
- Descoberta de publicadores paralelos e coletores ainda rodando mesmo após pausa inicial do Maestro.
- Necessidade de religar o ecossistema por etapas, com validação em cada etapa.

Fórum de referência:

- `Foruns/forum_investigacao_deterioracao_publicacao_20260601.md`

Canal:

- `Foruns/canal_trindade.md`, entradas Codex de 2026-06-01 21:15, 21:28, 21:35 e 21:48 BRT.

### Fase 1 — Pausa emergencial parcial

**Backup remoto:**

- `/root/crontab_backup_pre_pausa_emergencial_20260601_211249_codex.txt`

**Linhas comentadas no crontab root:**

- `maestro_editorial.py`
- `agente_analytics_v9.py`
- `agente_crime.py`
- `coletor_eleicoes.py`
- `agente_eleicoes_produtor.py`
- `run_analise.sh`

**Processo encerrado:**

- `agente_master_trends.py`

### Fase 2 — Pausa de publicadores paralelos e coletores correspondentes

**Backup remoto:**

- `/root/crontab_backup_pre_pausa_publicadores_paralelos_20260601_213020_codex.txt`

**Marcador usado no crontab:**

- `PAUSADO_CODEX_20260601_PUBLICADORES_PARALELOS`

**Publicadores/rotas pausadas:**

- `agente_observador.py`
- `agente_coletor_social.py --real`
- `agente_master_trends.py`
- `agente_master_lula.py`
- `publicador_china.py --limit 2 --live`

**Coletores correspondentes pausados:**

- `coletor_china.py --limit 10 --write --live-llm --brave`
- `robo_coleta_lula.py`
- `robo_coleta_trends.py`

**Coletores sem publicador ativo pausados para evitar acúmulo de fila:**

- `robo_coleta_nacional.py`
- `robo_coleta_soberania.py`
- `robo_coleta_geopolitica.py`
- `robo_coleta_imagens.py`
- `robo_coleta_flickr_rapido.py`
- `robo_coleta_militar.py`
- `robo_coleta_latam.py`
- `robo_coleta_sheinbaum.py`
- `robo_coleta_ia.py`
- `robo_coleta_matriz_energetica.py`
- `robo_coleta_flavio_bolsonaro.py`

**Processos encerrados:**

- `publicador_china.py --limit 2 --live`
- `agente_coletor_social.py --real`
- `agente_observador.py`
- `agente_master_lula.py`
- `robo_coleta_trends.py`

### Fase 3 — Pausa total ampliada

**Ordem de Miguel:** “pausa tudo, inclusive os bots e robôs.”

**Backups remotos dos crontabs:**

- `/root/crontab_backups_pause_all_20260601_213647/root.crontab.bak`
- `/root/crontab_backups_pause_all_20260601_213647/ubuntu.crontab.bak`

**Marcador usado no crontab:**

- `PAUSADO_CODEX_20260601_ALL_CRONTABS`

**Estado validado:**

- Crontab `root`: nenhuma linha ativa.
- Crontab `ubuntu`: nenhuma linha ativa.

**Serviços systemd do projeto parados/inativos:**

- `augusto.service`
- `cctv-v5.service`
- `cctv-editorial.service`
- `zizi.service`
- `websearch_proxy.service`

**Processos do projeto encerrados:**

- `augusto_telegram_brain.py`
- `bot_zizi_linda.py`
- `bot_audio_input.py`
- `agente_audio_monitor.py`
- `agente_correcao.py`
- `pesquisa_leilao_classificador.py`
- `websearch_proxy.py`
- `painel_cctv_v5.py`
- `painel_editorial.py`
- daemon `PM2` do usuário `ubuntu`

**Infraestrutura preservada:**

- `sshd`
- `nginx`
- `fail2ban`
- `cron` daemon
- Tencent/YunJing/TAT
- `node_exporter`
- serviços do sistema

### Validações executadas

Crontabs:

```bash
sudo crontab -l -u root | grep -n -E '^[[:space:]]*[^#[:space:]]' || true
sudo crontab -l -u ubuntu | grep -n -E '^[[:space:]]*[^#[:space:]]' || true
```

Resultado: sem linhas ativas.

Serviços:

```bash
systemctl is-active augusto.service cctv-v5.service cctv-editorial.service zizi.service websearch_proxy.service
```

Resultado: todos `inactive`.

Processos:

```bash
ps -eo pid,ppid,user,lstart,etime,pcpu,pmem,cmd --sort=-pcpu \
  | grep -E '/root/|Projeto|Cafezinho|agente_|robo_|bot_|publicador|coletor|maestro|zizi|painel|websearch|pm2|PM2' \
  | grep -v grep || true
```

Resultado: nenhum processo do projeto encontrado.

### Rollback / religamento gradual

Religar somente por ordem explícita de Miguel, com registro no fórum/canal.

Regras:

1. Religamento por etapas, nunca tudo de uma vez.
2. Antes de religar uma rota, registrar: objetivo, serviço/cron exato, rollback, log, limite de custo e smoke esperado.
3. Após religar, monitorar por pelo menos um ciclo real.
4. Não reativar publicador sem dedupe/HTML/fact-check validados.
5. Não reativar coletor se o publicador correspondente continuar pausado, para evitar fila acumulada.

Fontes de rollback:

- Emergencial parcial: `/root/crontab_backup_pre_pausa_emergencial_20260601_211249_codex.txt`
- Publicadores paralelos: `/root/crontab_backup_pre_pausa_publicadores_paralelos_20260601_213020_codex.txt`
- Pausa total: `/root/crontab_backups_pause_all_20260601_213647/root.crontab.bak`
- Pausa total ubuntu: `/root/crontab_backups_pause_all_20260601_213647/ubuntu.crontab.bak`

Reativação de serviços, quando autorizado:

```bash
sudo systemctl start <servico>
systemctl is-active <servico>
```

Restauração seletiva de cron: preferir editar a partir dos backups e restaurar só linhas aprovadas, mantendo o resto comentado.

### Estado atual

**Servidor Tencent em pausa total do ecossistema Cafezinho/Trindade.**  
Infraestrutura operacional preservada. Próximo passo: relatório do Claude + auditoria Codex/Kimi/DeepSeek/Qwen antes de religar por etapas.

## CHECKUP-001 — Log observacional pós-pausa

### [2026-06-01 22:36 BRT] Claude abre dupla checagem dos 100 posts

Miguel informou, para registro jornalístico do checkup, que Claude enviou carta à Trindade direcionada a **Kimi Code** e **Qwen Coding**.

Estado operacional declarado na carta:

- Sistema de agentes segue **PAUSADO**.
- Crontab com **0 jobs** e **0 processos** do ecossistema em execução.
- A atividade solicitada é estritamente **read-only**.
- Proibição explícita: não rebaixar, não despublicar, não corrigir posts durante esta fase.

Objeto da auditoria:

- Checkup geral dos últimos **100 posts** do Cafezinho.
- Divisão em lotes de **25 posts**.
- Lote 1: posts mais recentes, faixa `#255103` até `#255046`.
- Fórum-base do Claude: `Foruns/checkup_geral_100posts_20260601.md`.

Metodologia solicitada:

1. **Fase cega:** Kimi e Qwen analisam os mesmos 25 posts sem ler primeiro o relatório do Claude.
2. **Fase comparativa:** depois leem o relatório do Claude e marcam, por post, `CONCORDO`, `DIVERGO` ou `ACHADO NOVO`.
3. Claude consolida o comparativo final.

Arquivos de trabalho definidos:

- Dados crus no Tencent: `/tmp/checkup_lote1.json`
- Mapa de categorias: `/tmp/cats_needed.json`
- Relatório Kimi: `Foruns/checkup_lote1_kimi.md`
- Relatório Qwen: `Foruns/checkup_lote1_qwen.md`
- Comparativo final: `Foruns/checkup_lote1_COMPARATIVO.md`

Critérios de auditoria do lote:

- Vazamento de prompt, recusa LLM ou meta-discurso.
- Alucinação e factualidade: nomes, cargos, datas, cifras e protocolos de pesquisa.
- Linha editorial anti-imperialista: pró-Rússia, Irã, China e Sul Global; sinalizar frame OTAN/EUA infiltrado.
- Categoria correta, com conferência de de/para.
- Imagem destacada própria, diferente do fallback `227448`.
- Tamanho, qualidade e duplicatas.

Ganchos específicos registrados:

- Kimi deve observar o post `#255070` sobre Flávio/milícias marcado como Ciência e Tecnologia, possível reincidência da rota guerra/política → ciência.
- Qwen deve observar factualidade de datas/cifras de pesquisas e consistência entre dois posts da mesma pesquisa RealTime Big Data, protocolo `BR-05864/2026`.

Status Codex nesta entrada:

- Codex atua apenas como **registrador / observador / jornalista**.
- Nenhuma ação operacional foi executada.
- Nenhum servidor, cron, processo ou código foi tocado.
- Registro feito para preservar a memória do Checkup 001 e apoiar o religamento gradual futuro.

### [2026-06-01 23:24 BRT] Backblaze — backup sanitizado e teste de diferença

Miguel pediu, antes de qualquer mudança no sistema, duas medidas forenses:

1. Verificar um backup do Backblaze de aproximadamente 48h e comparar com o sistema atual.
2. Fazer um backup novo dos principais agentes no Backblaze.

Relatório técnico:

- `Foruns/checkup001_backblaze_diff_20260601.md`

Resultado do backup novo:

- Objeto B2: `b2:mayra-brain/Antigravity_Google/backups/checkup001/checkup001_principais_agentes_sanitizado_20260601_232342.tar.gz`
- Tamanho remoto: `9.864 MiB` (`10.343.338 bytes`)
- Arquivos no pacote: `1266`
- MD5 local: `dbe5176a0db650ae8854254cca029b03`

Escopo do pacote:

- agentes Python/Shell em `Projeto Cafezinho Agentes/root/`;
- scripts operacionais em `Projeto Cafezinho Agentes/scripts/`;
- nós `CEREBRO*.md`;
- `Foruns/`;
- `memorias_provisorias/`.

Higiene aplicada:

- excluídos bancos, tarballs, `.git`, `node_modules`, `__pycache__`, `agent_data`;
- excluídos caminhos com `chaves`, `cofre`, `credencial`, `credential`, `secret` e `.env`, incluindo variações de maiúsculas/minúsculas.

Observação importante:

- Uma primeira tentativa de snapshot amplo via `scripts/cerebro_b2_snapshot.py` começou a gerar pacote acima de 3 GB, mais amplo que o pedido. O processo foi interrompido e o arquivo parcial local removido. A pasta local de snapshots voltou a `49M`.
- Uma primeira versão não sanitizada do pacote estreito também foi preservada/reposta no B2, por orientação posterior de Miguel para não apagar nada e manter cópias diferentes: `b2:mayra-brain/Antigravity_Google/backups/checkup001/checkup001_principais_agentes_nao_sanitizado_preservado_20260601_232126.tar.gz`, MD5 local `47d86640cf59d0b96d925450b3b02747`.

Comparação:

- Não foi encontrado, no B2 acessível por esta máquina, snapshot de exatamente 48h.
- Snapshot canônico mais recente disponível/indexado do Cérebro: `2026-05-22 05:10 BRT`.
- Backups pontuais críticos disponíveis: `mayra-brain/criticos/`, de `2026-05-10`.
- Backup `.git` disponível: `mayra-brain/Antigravity_Google/backups/git/backup_dotgit_20260527_154226.tar.gz`.

Achados:

- Fóruns: `348` no snapshot de 22/05 versus `540` atuais; `192` novos; `0` removidos.
- Muitos nós `CEREBRO*.md` mudaram e vários nós novos surgiram, consistente com as sprints de 22/05 a 01/06.
- Agentes críticos comparados contra backups pontuais antigos de 10/05 (`agente_fantastico.py`, `agente_sobrenatural.py`, `motor_coletor.py`, `motor_publicador.py`, `publicador_china.py`) diferem do estado atual. Como esses backups são antigos, isso não prova deterioração das últimas horas; apenas confirma mudanças substanciais desde 10/05.

Conclusão:

- Backup atual, leve e sanitizado dos principais agentes está preservado no Backblaze.
- Não há evidência de backup perfeito de 48h acessível neste momento.
- Para rastrear deterioração das últimas horas, usar relatório dos 100 posts, git/diffs locais, fóruns recentes e backups pontuais criados durante deploys específicos.

### [2026-06-02 01:26 BRT] Tick observacional — hipótese de separação pós-conteúdo

Miguel levantou uma hipótese arquitetural durante o checkup: retirar **interlink** e **Mailchimp/newsletter** do campo textual do post, mantendo esses blocos em área externa ao `post_content`.

Racional registrado:

- O corpo do post deve ser tratado como objeto editorial puro: título, subtítulo se houver, texto jornalístico, fonte, imagem destacada, categoria e tags.
- Blocos operacionais como newsletter, interlink, CTA, Telegram, anúncios ou widgets não devem ser misturados ao texto que passa por revisão/fact-check LLM.
- A separação pode dar "refresco" aos revisores, reduzindo ruído de HTML/JS e diminuindo o risco de vazamento de código no corpo da matéria.

Formulação recomendada para discussão futura:

- `post_content`: somente conteúdo editorial.
- `post_meta`/camada de renderização/template/plugin: `related_posts_ids`, bloco "Leia também", newsletter/Mailchimp, CTAs e demais elementos de apresentação.
- O agente pode sugerir links/entidades, mas a renderização final deve ser externa, controlada e determinística.

Status:

- Nenhuma alteração operacional feita.
- Nenhum servidor, cron, processo ou código tocado.
- Registro apenas jornalístico/observacional para o CHECKUP-001.

### [2026-06-02 01:46 BRT] Tick observacional

Miguel enviou novo `tick` durante a noite de checkup. Codex manteve o modo combinado: apenas registrador/observador, sem acionar agentes, sem mexer em servidor, sem religar crons/bots e sem alterar produção.

### [2026-06-02 02:10 BRT] Sprint local — interlink/newsletter fora do post_content

Miguel autorizou avançar com a arquitetura discutida: para posts novos, manter o `post_content` limpo e mover interlink/newsletter para camada externa por `post_meta` + WPCode/Code Snippets.

Fórum:

- `Foruns/forum_external_blocks_interlink_newsletter_20260602.md`

Arquivos preparados localmente:

- `root/interlink_interno.py`
- `root/motor_publicador.py`
- `Snippets/wpcode_external_blocks_interlink_newsletter_20260602.php`

Backups locais pré-patch:

- `root/interlink_interno.py.bak_pre_external_blocks_20260602_0210_codex`
- `root/motor_publicador.py.bak_pre_external_blocks_20260602_0210_codex`

Desenho implementado:

- `interlink_interno.injetar_link(..., append_html=False)` escolhe o post relacionado e retorna `escolhido_id`, sem alterar o HTML.
- `motor_publicador.py` usa o modo novo somente se `CAFEZINHO_EXTERNAL_BLOCKS_META=1`.
- Com a flag ligada, o publicador salva:
  - `_cafezinho_external_blocks_v1=true`
  - `_cafezinho_newsletter_enabled=true`
  - `_cafezinho_related_posts=[id]`, quando houver interlink.
- Com a flag desligada, o comportamento legado é preservado.
- O snippet PHP registra os metas no REST e renderiza os blocos apenas em posts com `_cafezinho_external_blocks_v1=true`.

Validações locais:

- `python3 -m py_compile root/interlink_interno.py root/motor_publicador.py` passou.
- Smoke local do interlink em modo meta passou: `ok_meta_smoke ok_meta 123`.

Limites/pendências:

- PHP local não está instalado; `php -l` não foi executado.
- Snippet não foi ativado no WordPress.
- Nada foi deployado no Tencent.
- Nenhum post real foi criado/alterado.
- Rotas paralelas pausadas ainda precisam auditoria própria antes de religar: `publicador_tematicos.py`, `agente_eleicoes_produtor.py`, `agente_sobrenatural.py`, `agente_historiador.py`, `agente_flavio_bolsonaro.py`, `publicador_china.py`.

Status CHECKUP-001:

- Mudança preparada localmente, opt-in e reversível.
- Produção segue pausada.

### [2026-06-02 02:22 BRT] Smoke 1 — rascunho com blocos externos

Miguel ativou manualmente o snippet `Cafezinho — Blocos externos ao post_content — 2026-06-02` no WPCode.

Codex executou smoke controlado por REST, criando apenas rascunho:

- Script: `scripts/smoke_external_blocks_rascunho.py`
- Post criado: `255107`
- Status: `draft`
- Edit URL: `https://controle.ocafezinho.com/wp-admin/post.php?post=255107&action=edit`
- Post relacionado em meta: `255105`

Metas aceitos pelo WordPress:

- `_cafezinho_external_blocks_v1=true`
- `_cafezinho_newsletter_enabled=true`
- `_cafezinho_related_posts=[255105]`

Resultado:

- REST aceitou os campos registrados pelo snippet.
- Nenhum post foi publicado.
- Produção segue pausada.
- Próxima validação é manual no editor/preview: confirmar que o corpo editável do rascunho está limpo e que o frontend renderiza "Leia também" + newsletter fora do `post_content`.

### [2026-06-02 02:35 BRT] Fase legenda destacada fora do post_content

Miguel pediu para corrigir também legendas de fotos/ilustrações, mantendo-as visíveis no post mas fora do `post_content`.

Diagnóstico real:

- As legendas já são salvas no objeto de mídia do WordPress por `gerenciador_imagens.py`.
- A injeção de `<figure class="cafezinho-featured-caption">` no corpo existe porque o tema não renderiza automaticamente a legenda da imagem destacada.

Patch local opt-in:

- Snippet WPCode agora registra `_cafezinho_featured_caption_enabled` e renderiza a legenda com `wp_get_attachment_caption(get_post_thumbnail_id())`.
- `motor_publicador.py`, com `CAFEZINHO_EXTERNAL_BLOCKS_META=1`, não injeta figcaption no corpo e envia `_cafezinho_featured_caption_enabled=true` quando há `featured_media`.
- `scripts/smoke_external_blocks_rascunho.py` foi ampliado para tentar criar rascunho com imagem destacada real e legenda.

Validação:

- `python3 -m py_compile root/motor_publicador.py scripts/smoke_external_blocks_rascunho.py` passou.

Pendência:

- Substituir manualmente no WPCode o snippet ativo pela nova versão local.
- Rodar smoke de rascunho com imagem destacada.
- Não assumir que publicadores paralelos já obedecem ao padrão; cada rota precisa auditoria própria.

### [2026-06-02 03:31 BRT] CHECKUP-001 — helper central external_blocks

Miguel autorizou a faxina central/choke point para impedir que blocos operacionais contaminem `post_content`.

Codex executou localmente:

- Criou `root/util_blocos_externos.py`.
- Refatorou `root/motor_publicador.py` para chamar o helper.
- Não tocou rotas paralelas.
- Não fez deploy.
- Não religou robôs.

Backups:

- `root/motor_publicador.py.bak_pre_util_blocos_externos_20260602_032301_codex`

Validação:

- `python3 -m py_compile root/util_blocos_externos.py root/motor_publicador.py` passou.
- Teste unitário manual confirmou:
  - flag desligada preserva legado;
  - flag ligada remove figcaption/interlink/Mailchimp e monta metas.
- Smoke REST criou rascunho `255113` com HTTP `201`, `status=draft`, corpo limpo e metas external_blocks aceitos.

Limite:

- Smoke completo do artefato `motor_publicador.py` ainda não foi executado; acionar o motor exige pauta/banco e pode alterar estado. Fazer apenas em etapa §12/§92 controlada.

Próximo passo:

- Claude revisar linha-a-linha.
- Depois adaptar paralelos em lotes pequenos, começando por rotas comprovadamente problemáticas no checkup.

### [2026-06-02 03:31 BRT] CHECKUP-001 — bloqueador regex Mailchimp fechado

Claude revisou §12 o helper `util_blocos_externos.py` e aprovou a arquitetura, mas apontou um bloqueador: o regex anterior removia parcialmente a `CAIXA_NEWSLETTER_AJAX` real e podia deixar `<script>mailchimpCallback...</script>` no corpo em rotas paralelas.

Codex corrigiu localmente o pattern Mailchimp para casar do `<hr>`/`<div id="mc_embed_signup">` até o script com `mailchimpCallback`.

Validação:

- `python3 -m py_compile root/util_blocos_externos.py root/motor_publicador.py` passou.
- Teste contra a constante literal `CAIXA_NEWSLETTER_AJAX` do motor deixou apenas `<p>Texto editorial.</p><p>Fim.</p>`.
- Confirmado ausente: `mc_embed_signup`, `cafezinho-mc-form-ajax`, `mailchimpCallback`, `<script`, `<hr>`.
- Idempotência confirmada.

Status:

- Bloqueador fechado localmente.
- Nenhum deploy.
- Nenhum robô religado.
- Nenhuma rota paralela adaptada ainda.

### [2026-06-02 04:09 BRT] CHECKUP-001 — unificação de papéis e registro Codex

Miguel definiu a governança do próximo ciclo do checkup: **Claude distribui os sprints**; Codex fica como observador/jornalista técnico e auditor quando chamado. Registro de memória integrado feito no canal e memória Codex.

Estado canônico preservado:

- Sistema/Tencent segue pausado.
- `external_blocks_v1` etapa 1 está localmente aprovada por Claude §12.
- Snippet WPCode está ativo manualmente, renderizando `Leia também` + newsletter fora do `post_content`; legenda fica com Media Library/tema.
- Nenhuma rota paralela foi adaptada.
- Nenhum deploy foi feito.
- Nenhum robô foi religado.

Frente nova aberta: Qwen criou `Foruns/forum_problemas_estruturais_lote2.md` para HTML escapado, categorias erradas/genéricas e fallback media. Kimi reportou checkup 100 posts e reconheceu que parte do diagnóstico de JS/legenda já estava coberta por `external_blocks_v1`.

Observabilidade: bloco de Kimi no canal veio com timestamp `04:30 BRT`, posterior ao relógio local de Codex (`04:09 BRT`). Não usar esse carimbo isolado para janela temporal; cruzar com fonte datada.

### [2026-06-02 05:58 BRT] CHECKUP-001 — fórum conflito prompt redator observado

Codex observou canal, inboxes e `Foruns/forum_conflito_prompt_redator_20260602.md` sem executar código. Canal foi limpo/compactado; histórico anterior preservado em `Foruns/backups_limpeza_20260602_054149/canal_trindade.md`.

Novo foco do Claude: conflito de prompt no redator, apontado como causa-raiz de parágrafos de 1 frase (>95% dos posts) e títulos longos (60%). Kimi aceitou prototipar normalizador determinístico de parágrafo offline; Qwen propôs specs para validador de título e guard de categoria; DeepSeek foi chamado para parecer externo; Codex tem missão pendente de revisão §12 do motor.

Nota de risco: a proposta de Qwen para categorias inclui `keyword_map`; isso deve ser tratado como protótipo/hipótese e revisado contra a diretriz de Miguel de não resolver qualidade editorial com listas cegas de palavras. Produção continua pausada; §92 segue ativo.

### [2026-06-02 06:06 BRT] CHECKUP-001 — virada LLM-first no sprint do redator

Claude registrou virada de rota por ordem do Miguel no `Foruns/forum_conflito_prompt_redator_20260602.md`: output editorial visível ao leitor deve ser **LLM-first**. Determinístico fica restrito a log, métrica, trigger e organização interna.

Impacto:

- `normalizador_paragrafo.py` prototipado por Kimi deve ser tratado como diagnóstico/métrica offline, não como reescrita viva.
- Validador determinístico de título e guard de categoria por `keyword_map` propostos por Qwen ficam descartados para output editorial.
- Cura viva passa a ser: regra C1 no prompt do redator, revisão/reescrita de título por LLM de luxo chinês, re-prompt LLM para categoria "Redação" genérica, desconflito da auditoria e consolidação futura em diretrizes por camadas.
- Codex ainda não respondeu tecnicamente; missão §12 pendente foi recalibrada para revisar pontos de injeção LLM, ordem, custo, risco e rollback.

Sistema segue pausado; §92 ativo; nenhuma produção alterada.

Atualização adicional 2026-06-02 06:06 BRT: Kimi e Qwen já acusaram recebimento da virada LLM-first no canal. Kimi aceitou manter `normalizador_paragrafo.py` como diagnóstico/métrica offline; Qwen reconheceu que suas specs determinísticas anteriores foram invalidadas e vai propor nova abordagem LLM-first. DeepSeek ainda sem resposta observada; Codex ainda pendente de resposta §12 recalibrada.

Atualização 2026-06-02 06:10 BRT: Codex respondeu no fórum `Foruns/forum_conflito_prompt_redator_20260602.md` com revisão §12 do motor. Veredito: aprova LLM-first com faseamento. P0: C1 no `sys_base`, C3 no auditor e métrica offline, sem chamada LLM extra. P1: revisão LLM de título pós-parse com consistência/fact-check do artefato final. P2: re-prompt LLM de categoria "Redação"/inválida após auditar `util_categorizador_rigido.py`. Alerta: o motor já possui categorizador determinístico ativo, potencialmente em conflito com LLM-first; não remover sem teste porque pode explicar melhorias recentes. Produção segue pausada; §92 ativo.

Atualização 2026-06-02 06:25 BRT: DeepSeek respondeu no mesmo fórum. Aprova a arquitetura LLM-first; recomenda DeepSeek-V3 como primeiro modelo de luxo chinês para revisão de título, Qwen-max fallback e GLM terceira opção. Apontou risco principal de título perder gancho/entidade e sugeriu gate de perda de entidade e prevenção de double-fix. Canal pontuado: Codex + DeepSeek responderam; sistema pausado; §92 ativo.

Atualização 2026-06-02 06:19 BRT: novo tick observado. Claude abriu §6 no `Foruns/forum_conflito_prompt_redator_20260602.md`, delegando ao Kimi auditoria READ-ONLY de `root/util_categorizador_rigido.py`. Objetivo: entender se a camada rígida é lista/heurística/gate, se explica a melhora do Lote 4, como é chamada no `motor_publicador.py`, e como compatibilizar com LLM-first. Codex não executou código. Observabilidade: registros no canal/fórum aparecem com `06:25` e `06:30 BRT`, à frente do relógio local Codex (`06:19 BRT`); cruzar carimbos antes de análise temporal. Produção pausada; §92 ativo.

Atualização 2026-06-02 06:29 BRT: Codex revisou a §7 do fórum do redator e aprovou o rascunho C1 como P0, com C3 obrigatório. Ponto de injeção correto: `sys_base`, imediatamente antes de `DEVOLVA UM JSON PURO:`. Texto C1 aprovado: parágrafos 2-3 frases + título conciso qualitativo sem número fixo. Ressalva: auditor final deve ser suavizado para verificação/correção pontual, não reescrita pesada conflitante com preservação de JSON. P0 não toca categoria e não adiciona chamada LLM extra. Nada aplicado; §92 ativo.

Atualização 2026-06-02 06:52 BRT: Codex aceitou Sprint 2B e 3B no fórum do redator. Sprint 2B: revisar §12 do patch C1+C3 quando Claude postar diff/rascunho final. Sprint 3B: revisar revisor de título do Qwen. Revisão preliminar: protótipo offline aceitável se usar roteador por `contexto="editor_titulo_luxo"` sem hardcode de provider no motor; trigger determinístico só como gatilho; gates apenas rejeitam sugestão; checagem de consistência título × corpo antes do payload final; logs obrigatórios. Nada executado; sistema pausado; §92 ativo.

Atualização 2026-06-02 06:53 BRT: Codex fez §12 pós-deploy do C1+C3. Diff local contra `root/motor_publicador.py.bak_pre_c1_local_20260602_064805` ficou restrito a dois pontos: bloco C1 no `sys_base` antes de `DEVOLVA UM JSON PURO:` e C3 suavizando item 1 do auditor. Contrato JSON preservado; `py_compile` local passou. Veredito: aprovado. Risco residual: smoke comportamental após religar publicador principal. Categoria não foi tocada.

Atualização 2026-06-02 07:17 BRT: Codex revisou Sprint 3A Qwen e Sprint 1B Kimi. Revisor de título `root/revisor_titulo_luxo.py` está bloqueado para integração: testes não exercitam LLM, chamada ao roteador incompatível com assinatura real, retorno tuple não normalizado, contexto `editor_titulo_luxo` ausente da config e gate de entidade rígido demais. Prompt de categoria Kimi aprovado como base com ressalvas: compactar P0, evitar prioridade rígida mecânica, deixar re-prompt para P1/P2. `py_compile` local passou para `revisor_titulo_luxo.py` e `util_minicheck_titulo_corpo.py`.
