# CEREBRO_NODE_CODIGO_MORTO_INDEXADO.md

**Indexado em:** 2026-06-23 00:55 BRT — Claude Code (Daemon)  
**Origem:** `/root/` Tencent → movido para `/root/Legacy_codigos_mortos_20260623/`  
**Backup tarball:** `/root/BACKUPS/codigos_mortos_tier_a_20260623.tar.gz` (150 KB)  
**Cópia individual:** 57 arquivos preservados em `/root/Legacy_codigos_mortos_20260623/`  

## 📜 Contexto

Miguel autorizou 22-23/06 limpeza de código morto do ambiente de produção.
Critério rigoroso aplicado: **(a)** não está no cron ATIVO,
**(b)** não é editoria no `maestro_distribuicao.py`,
**(c)** não importado por nenhum arquivo ativo,
**(d)** modificado há > 30 dias.

Esses arquivos contêm instruções, prompts e lógicas úteis que podem ser
reaproveitadas em futuras iterações. **Nada foi apagado** — apenas movido
para `/root/Legacy_codigos_mortos_20260623/` + tarball em `/root/BACKUPS/`.

## 🗂️ Como reativar um arquivo

```bash
# 1. Copiar de volta
sudo cp /root/Legacy_codigos_mortos_20260623/<arquivo>.py /root/
# 2. Validar imports e dependências (muitos podem estar quebrados)
sudo python3 -m py_compile /root/<arquivo>.py
# 3. Religar no cron OU no maestro_distribuicao.py conforme o caso
```

---

## 📋 Índice por categoria (57 arquivos · 522 KB total)


### Agentes de curadoria/observação (13 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_agitador.py` | 3.5KB | 2026-04-11 | Função Placeholder (MVP) que simulará a conexão via API Bluesky (atproto) Aqui entra a lógica da API: auth() -> get_post() -> like() -> post_reply() -> repost() |
| `agente_audio_monitor.py` | 14.5KB | 2026-04-26 | agente_audio_monitor.py — Daemon que transcreve áudios da pasta /root/audio_uploads/ via cascata STT de 4 níveis e atualiza o processing_log.jsonl. Cascata (Miguel pediu fallback redundante 26/04 11:04 + Transkriptor 11:09): 1. Groq — whisper-large-v3-turbo (rápido, free tier alt… |
| `agente_auditoria_sistema.py` | 10.6KB | 2026-05-14 | (sem docstring) Função principal: `now_iso()` |
| `agente_comentarista_china.py` | 3.1KB | 2026-05-07 | Gerador governado de debates China para revisao editorial. Nao posta comentarios publicos automaticamente. Gera rascunhos rotulados para revisao, evitando engajamento artificial invisivel. |
| `agente_comunicador.py` | 4.6KB | 2026-04-05 | (sem docstring) Função principal: `ler_arquivo()` |
| `agente_correcao.py` | 62.5KB | 2026-05-14 | Caetano — Agente de Correção do O Cafezinho @caetanoechicobot |
| `agente_curador_fontes.py` | 6.7KB | 2026-04-13 | Tenta pingar a URL para checar se está minimamente on-line e respondendo |
| `agente_curador_midia.py` | 7.4KB | 2026-05-03 | Retorna até 3 imagens do wikimedia |
| `agente_curadoria.py` | 15.4KB | 2026-04-12 | agente_curadoria.py — O Cafezinho Lê performance_weights.json (gerado pelo agente_performance.py), interpreta os dados via Gemini e atualiza: - curadoria_diaria.json (expira em 24h) - curadoria_geral.json (atualiza se tendência se mantiver 3+ dias) - config_editorial.py (GOOGLE_Q… |
| `agente_curadoria_gsn.py` | 8.0KB | 2026-05-04 | Agente Curadoria GSN — V1 Verifica os últimos posts aprovados e publicados no "O Cafezinho" nas editorias de Geopolítica, Política, Tecnologia, traduz para o inglês e posta no Global South News. |
| `agente_escalada_qualificacao.py` | 16.9KB | 2026-05-09 | agente_escalada_qualificacao.py — Escalada AUTOMÁTICA upgrade/downgrade de tier dos agentes. Sob diretivas Miguel 2026-05-08 13:13-13:22 BRT (forum_certificador_qualidade.md §"Promoção Temporal Automática + Autocura Escalada"). 5 camadas: Camada 1: Promoção Temporal (draft_only →… |
| `agente_monitor_eleicoes.py` | 9.5KB | 2026-05-19 | agente_monitor_eleicoes.py Observador do Agente Eleições. Não publica, não altera pautas e não chama LLM. Lê o banco intermediário, logs do roteador/produtor/coletor e grava alertas machine-readable para acompanhar mudanças de comportamento apos ajustes. |
| `agente_vigilante.py` | 3.7KB | 2026-04-11 | (sem docstring) Função principal: `carregar_historico()` |

### Agentes de mídia social/automação (6 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_bluesky.py` | 4.8KB | 2026-04-22 | (sem docstring) Função principal: `carregar_json()` |
| `agente_facebook.py` | 6.0KB | 2026-05-02 | Busca a URL da imagem destacada de um post via WP REST API com _embed. |
| `agente_heygen.py` | 8.4KB | 2026-04-21 | AGENTE HEYGEN - Integração com a API da HeyGen e Vozes ElevenLabs Suporta: - Opção 1: Texto Direto (Requer que a chave da ElevenLabs já esteja inserida no painel HeyGen) - Opção 2: Via URL de Áudio (Upload prévio para S3 ou servidor local e envio da URL) |
| `agente_newsletter_mailchimp.py` | 7.5KB | 2026-04-19 | Busca as últimas matérias no O Cafezinho via REST API |
| `agente_twitter_video.py` | 12.4KB | 2026-05-12 | Retorna {'text', 'uploader', 'has_video'} ou None. Cascata: yt-dlp (tem vídeo) -> Twitter API v2 (texto/metadata). Não levanta exception: falhas são logadas e classificadas. |
| `agente_videomaker_diario.py` | 5.6KB | 2026-04-21 | AGENTE VIDEOMAKER DIÁRIO (O Cafezinho) - Recupera a última manchete postada no site O Cafezinho - Roteiriza uma locução curta - Gera vídeo e áudio via FFMPEG/OpenAI - Publica no YouTube (Privado) - Publica no Twitter (X) |

### Agentes editoriais experimentais (12 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_diario_direita.py` | 9.6KB | 2026-05-03 | AGENTE DIÁRIO DA DIREITA (O Cafezinho) - Monitora portais conservadores (BR e Exterior) - Persona: Antropólogo Irônico (Desprezo Benevolente) - Compila a histeria ou pauta principal do dia da direita em um texto de resumo. |
| `agente_escritor_scifi.py` | 8.6KB | 2026-05-14 | (sem docstring) Função principal: `log()` |
| `agente_escritor_scifi_en.py` | 8.2KB | 2026-05-14 | (sem docstring) Função principal: `log()` |
| `agente_ficcao_noturna.py` | 15.6KB | 2026-04-30 | (sem docstring) Função principal: `log()` |
| `agente_grade_diaria.py` | 2.6KB | 2026-04-21 | (sem docstring) Função principal: `enviar_grade_diaria()` |
| `agente_historiador.py` | 16.0KB | 2026-05-03 | Envia notificacao via Telegram Bot API. |
| `agente_historiador_bkp.py` | 11.9KB | 2026-04-17 | Busca as palavras e assuntos mais procurados no momento no Google News para guiar a Aula de História |
| `agente_pet_v1.py` | 24.5KB | 2026-04-30 | Agente Pet Autônomo — V1 Focado em histórias de superação, proteção, resgates e fatos heroicos envolvendo cães e gatos. Baseado na arquitetura do Agente Ferroviário V2, com adaptações para carga emocional. |
| `agente_petroleo.py` | 2.6KB | 2026-04-17 | AGENTE TEMÁTICO: PETRÓLEO / GEO-ENERGIA FÓSSIL — V9. |
| `agente_planejador_bella_ciao.py` | 3.8KB | 2026-05-14 | (sem docstring) Função principal: `log()` |
| `agente_produtor_bella_ciao.py` | 5.8KB | 2026-05-14 | (sem docstring) Função principal: `log()` |
| `agente_riocarta.py` | 10.1KB | 2026-05-03 | Baixa a imagem remotamente e faz o sideload no WP Target |

### Agentes especializados (8 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_analise.py` | 9.9KB | 2026-05-14 | Agente Análise — orquestrador das 5 camadas. Ver `forum_agenteanalise.md` §1-§13 para especificação completa. Este arquivo apenas amarra as peças já testadas em `analise/`: Camada 1 — Escuta (analise/camada1_escuta.py) Camada 2 — Agrupamento (analise/camada2_agrupamento.py) Camad… |
| `agente_audio_consumer.py` | 6.0KB | 2026-04-26 | agente_audio_consumer.py — CLI utilitária pro Claude Code interagir com a fila de áudios/textos vindos do bot Telegram @cafezinho_claudebot. Roda no Tencent (/root/). Claude Code chama via SSH. Subcomandos: list-pending # imprime entradas pendentes em JSON reply --audio-file X --… |
| `agente_banco_midia.py` | 5.8KB | 2026-04-15 | (sem docstring) Função principal: `carregar_indice()` |
| `agente_china_health.py` | 7.2KB | 2026-05-09 | Read-only health report for the China agent pipeline. |
| `agente_energias.py` | 2.8KB | 2026-04-17 | AGENTE TEMÁTICO: ENERGIAS ALTERNATIVAS E TRANSIÇÃO VERDE — V9. |
| `agente_news_trend.py` | 11.6KB | 2026-05-03 | AGENTE NEWS TREND (O Cafezinho) - V2.1: Fotografia Real do Wikimedia via gerenciador_imagens.py - Tráfego Altíssimo, SEO Rigoroso e Rascunho WP Nativo |
| `agente_novo_trends.py` | 6.2KB | 2026-05-14 | AGENTE NOVO TRENDS E COMERCIAL (Fase 1) - Inspirado na arquitetura do Gabriel/Miller. - Sistema de 3 Camadas de Segurança (Redator -> Revisor -> Auditor). - Módulo para buscar assunto em alta (Mockup) e gerar a matéria. - Conecta diretamente ao WordPress como Rascunho. |
| `agente_reciclador.py` | 6.9KB | 2026-04-06 | agente_reciclador.py — Catador de sobras editoriais. Varre reservas, bancos primários e legado, pega o melhor artigo não-publicado e entrega ao motor_publicador (mesmos 10 estágios de qualidade). Roda 3x/dia em horários de baixa. |

### Backups datados (3 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_editorial_backup_20260405.py` | 19.3KB | 2026-04-05 | agente_editorial.py — Agente Editorial do O Cafezinho Autor: Miguel do Rosário Fluxo: 1. Recebe texto/áudio do editor via bot_mayrag_v2 (modo editorial) 2. GPT escreve o texto com diretrizes editoriais 3. GPT faz revisão leve (sem descaracterizar) 4. Envia para editor aprovar no … |
| `agente_ficcao_noturna_backup_20260405.py` | 12.1KB | 2026-04-05 | (sem docstring) Função principal: `log()` |
| `agente_historiador_backup_20260405.py` | 12.0KB | 2026-04-05 | Busca as palavras e assuntos mais procurados no momento no Google News para guiar o Diário do Historiador |

### Coletores legacy (8 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `robo_coleta_bruta.py` | 21.0KB | 2026-05-02 | Carrega títulos do banco jsonl de publicações do Cafezinho para evitar pautas velhas. |
| `robo_coleta_discursos.py` | 4.9KB | 2026-04-20 | robo_coleta_discursos.py — Coletor Especializado de Discursos Presidenciais Utiliza a Jina Reader API para realizar bypass do firewall do Planalto (gov.br). |
| `robo_coleta_geopolitica.py` | 5.1KB | 2026-04-15 | REGRAS_APROVACAO = |
| `robo_coleta_latam.py` | 6.1KB | 2026-04-20 | REGRAS_APROVACAO = |
| `robo_coleta_nacional.py` | 3.8KB | 2026-04-15 | REGRAS_APROVACAO = |
| `robo_coleta_riocarta.py` | 5.8KB | 2026-04-11 | Busca via Brave Search API para caçar pautas frescas. |
| `robo_coleta_sheinbaum.py` | 3.7KB | 2026-04-20 | REGRAS_APROVACAO = |
| `robo_coleta_trends.py` | 5.7KB | 2026-04-05 | REGRAS_APROVACAO = |

### Masters legacy (5 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_master_discursos.py` | 7.9KB | 2026-04-22 | agente_master_discursos.py — Orquestrador do Agente de Discursos do Lula Lê os discursos brutos processados, gera artigos para O Cafezinho (PT) e Global South News (EN), aciona o gerador de vídeos curtos, e insere na fila do X (Twitter). |
| `agente_master_geopolitica.py` | 0.7KB | 2026-04-04 | (sem docstring) Função principal: `master_geopolitica_run()` |
| `agente_master_lula_legacy.py` | 6.6KB | 2026-04-21 | agente_master_lula.py — Master Publicador do Agente Lula (Trindade Edition) Padrão canônico (igual master_nacional.py): delega ciclo completo ao motor_publicador.iniciar_publicacao_especializada com como_rascunho=True. Diferencial editorial — pré-processamento "Olhar do Stuckert"… |
| `agente_master_nacional.py` | 0.7KB | 2026-04-04 | (sem docstring) Função principal: `master_nacional_run()` |
| `agente_master_trends_legacy.py` | 1.6KB | 2026-04-04 | (sem docstring) Função principal: `acionar_agentes_reserva()` |

### Rascunhos abandonados (2 arquivos)

| Arquivo | Tamanho | Última mod | Propósito (do docstring/header) |
|---------|---------|------------|----------------------------------|
| `agente_eleicoes_produtor_rascunho_antigravity_20260424.py` | 11.8KB | 2026-04-24 | agente_eleicoes_produtor.py — Agente Eleições 2026 (Módulo Produtor) Responsável por puxar pautas do banco, auditar, enriquecer com TSE, redigir, inserir interlink e publicar. |
| `coletor_eleicoes_rascunho_antigravity_20260424.py` | 6.3KB | 2026-04-24 | coletor_eleicoes.py — Agente Eleições 2026 (Módulo de Coleta) Responsável por varrer fontes (Brave Search), fazer a raspagem e popular o banco intermediário. |

---

## 🆕 Aposentados posteriores à faxina 2026-06-23

### `motor_publicador.py` — LEGACY (12/08/2026)

**Destino:** `/root/legacy/motor_publicador_aposentado_20260812/` (NYC) + `Projeto Cafezinho Agentes/root/legacy/motor_publicador_aposentado_20260812/` (espelho local).

| Arquivo | Tamanho | Última mod | Propósito |
|---------|---------|------------|-----------|
| `motor_publicador.py` | 148885 B | 2026-08-09 | "Mestre único publicador" — orquestrador legado de publicação (10 estágios de qualidade). **Substituído pelo runtime V4** (`codigo.v4_vertical_redactor_runtime` chamado por `v4_vertical_draft_worker.py`) no cutover de 09/08. O cerco de títulos `gate_titulo.py` foi plugado nele (linhas 2499-2563) **mas estava órfão do cron** — nenhum agente que o invoca estava ativo. |
| `motor_publicador.py.bak_pre_cerco_titulos_20260809` | 146653 B | 2026-08-09 | Backup pré-cerco de títulos (Claude). |
| `motor_publicador.py.bak_pre_safety_net_95_20260609_2330_claude` | 148014 B | 2026-06-10 | Backup pré safety-net 95. |
| `motor_publicador.py.bak_sprint_cat_20260610` | 148750 B | 2026-06-10 | Backup sprint categorias. |

**Backup/rollback:** `/root/Backups/faxina_motor_publicador_20260812_135635.tar.gz` (sha256 `dddabe66...f5575d`). Rollback: `tar -xzf /root/Backups/faxina_motor_publicador_20260812_135635.tar.gz -C /root`.

**Critério aplicado (igual à faxina 06/23):** (a) não está no cron ATIVO; (b) não é editoria no `maestro_distribuicao.py`; (c) **não importado por nenhum arquivo da cadeia V4 ativa** (worker/intake/coletor/redactor_runtime); (d) substituído formalmente pelo V4 em 09/08.

**Mantido no `/root`:** `gate_titulo.py` (autossuficiente, não importa o motor — só era importado por ele). Fica órfão de caller, aguardando conselheiro de títulos / integração ao worker V4.

**Smoke pós-movimento (tudo verde):** `py_compile` 9/9 OK (motor no legacy + gate_titulo + worker/intake/coletor/repetidor_estatal/auditor/redactor_runtime); `gate_titulo` importável; `import motor_publicador`→`ModuleNotFoundError`; crontab 35 linhas ativas sem referência.

### ⚠️ Sinalizado — órfãos pendurados (`import motor_publicador` quebrado, NENHUM no cron)

Estes agentes-irmãos **legacy** permanecem no `/root` e em `/root/cafezinho/portal_cafezinho/` com `import motor_publicador` agora quebrado (ImportError se rodados). **Nenhum está no cron ativo** (confirmado), então não afetam o runtime automático — mas quebrariam se executados manualmente. Fora de escopo desta faxina; próxima faxina decide (mover pra legacy ou descartar):

`agente_crime`, `agente_lula`, `agente_master_geopolitica`, `agente_master_nacional`, `agente_reciclador`, `agente_latam`, `agente_matriz_energetica`, `agente_sheinbaum`, `agente_militar`, `agente_soberania`, `agente_ia`, `publish_caiado`, `agente_master_lula_legacy`, `agente_master_trends_legacy` + cópias em `cafezinho/portal_cafezinho/` (`publish_china_draft`, `update_china_draft`, `scratch/publica_artigo`).

## 🔗 Relacionados

- `MEMORIA_BUGS_ATUAL.md` — C-043, C-044 (pausa Reciclador + robo_nacional + auditoria órfãos)
- `CEREBRO_NODE_AGENTES.md` — agentes ATIVOS em produção
- `feedback_pending_so_miguel_promove.md` — regra atual de cura editorial
