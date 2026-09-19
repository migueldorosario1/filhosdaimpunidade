# Memória técnica — Painel de comando manual do agente YouTube — 15/09/2026

Log técnico completo da construção. Fórum gêmeo: Foruns/forum_painel_comando_youtube_manual_20260915.md.

## Arquivos criados/alterados (com backups)

NYC:
- /root/tematicos/agentes_tematicos/v4/youtube_manual.py (NOVO, ~420 linhas) — executor: argparse (--url --destinos --pedido --prompt-base64); Status scp incremental; oembed gate; reuso dialogos; produzir_com_auditoria (gera→corrige nomes→audita→retry); publicar_tematico (fila livre=publicador oficial; ocupada=render+commit direto); subir_media_cafezinho + draft_cafezinho (REST cat 28, metas, capa). Ambiente: source /root/chaves.sh; PYTHONPATH=/root:/root/agents_labs/youtube_v2:/root/tematicos/agentes_tematicos/v4:/root/tematicos/agentes_tematicos; /root/venv/bin/python3; YOUTUBE_DIALOGOS_DB=/root/agent_data/youtube_dialogos.sqlite.
- /root/youtube_manual_dispatch.sh (NOVO) — command= forçado da chave; valida URL/destinos/pedido/b64; pgrep anti-duplicado; setsid nohup.
- /root/.ssh/authorized_keys (+1 linha restrict) — chave yt_manual_painel_v6_tencent (ed25519 gerada no tencent ubuntu /home/ubuntu/.ssh/yt_manual_dispatch).
- /root/agent_data/youtube_manual/{pedidos,logs}/ + crontab.bak_pre_pause_manual_yt_20260914 (do pause anterior).

Tencent:
- /home/ubuntu/cafezinho/v6/painel_cctv_v6.py — patch 20260915: _YM_BLOCO_HTML (form+JS+tabela), cartão MODO MANUAL refeito, parágrafo 2 atualizado, rotas GET/POST /youtube/manual[/status], métodos _youtube_manual_disparar/_youtube_manual_status/_ym_json. BAK: .bak_pre_ym_painel_20260915. py_compile OK; restart cctv-v6.
- /home/ubuntu/cafezinho/v6_data/youtube_manual/ (dir de status scp).

Dell:
- scratch/print_painel_youtube_comando_form_20260915.png + print_painel_youtube_status_pedidos_20260915.png.

## Reuso de componentes da casa (chaves da manutenção futura)

- Transcrição: util_youtube_transcript.YouTubeTranscriber(modo="zizi", language=hint) — diarização; cache próprio; TRANSKRIPTOR_UNKNOWN_DURATION_POLICY=estimate.
- Correção de nomes: agente_youtube_v2_materializador.corrigir_nomes_personagens (retorna tupla).
- Entrevistado: agente_youtube_v2_auditor.identificar_entrevistado(material{titulo,descricao,html,meta}) — lista-ouro/meta/regex.
- Gate idioma: publicador._versao_no_idioma({title, body_markdown}, "pt"|"en").
- LLM: nucleo_llm.gerar_json(tarefa="youtube") — tiers do config llm_tiers.json.
- Draft WP: payload espelho PT (cat 28, meta _video_id_youtube) + featured_media via POST /media (controle.ocafezinho.com, WP_USER/WP_PASS da chaves.sh, UA navegador).
- Astro: nucleo_frontmatter.render(artigo, cfg) → blog_dir; publicador.rodar(site, limite=1).

## Armadilhas registradas (para quem mexer depois)

1. bash 5.2: regex ERE com quantificador de intervalo GRANDE ({0,8192}) = OOM kill silencioso — usar * + [[ ${#v} -gt N ]].
2. ${#VAR:-0} é bad substitution — materializar default antes.
3. scp do status é fail-open (capture_output): diretório de destino precisa existir ANTES (mkdir no tencent).
4. Sessões paralelas no painel_cctv_v6.py se sobrescrevem — conferir texto pós-restart (caso 14/09 23:50).
5. oembed 401/403/404 = vídeo privado/removido → abortar antes de custo (implementado no metadados()).
6. O venv (/root/venv) é obrigatório (PIL etc.); python3 do sistema quebra nos imports do publicador.
7. A chave yt_manual_dispatch NÃO serve para shell — só o command= (testar mudanças no dispatcher rodando SSH_ORIGINAL_COMMAND="youtube_manual ..." bash -x /root/youtube_manual_dispatch.sh).

## Testes executados

- Auditoria offline 6/6 (idiomas, entrevistado, tamanhos).
- Chave forçada: evil.com rc=65; "yum install" → uso rc=64; args válidos → DISPATCH_OK.
- E2E pelo painel: 20260915_002223_6a027d → draft 270973 completo (autor 5470, cat Vídeos, capa 270972, embed, meta) em ~70s, custo US$ 0 (reuso). Prompt do editor refletiu no título.
- Segurança: 401 público sem creds (X-Real-IP); POST/GET fora do nginx = 404 externo; porta 8084 fechada.

— ZCode Miguel (ZM) · GLM-5.3 · 15/09/2026 00:3x BRT

## ➕ Adendo — restauração 15/09 ~15:1x BRT (3º caso de sobrescrita)

- Bloco perdido às 12:52 (sessão MMN/MM7 sobrescreveu o painel a partir de versão anterior à obra); NYC nunca foi afetado.
- Restaurado com: cp -p → .bak_pre_ym_restore_20260915_1510 (462.612 bytes, estado de hoje COM MM7); `python3 /tmp/patch_ym_painel.py` (âncoras 6/6 presentes — inclui cartão velho 11/09 e par2 velho 19/08, confirmando a regressão) + `python3 /tmp/patch_get_ym.py`; py_compile OK (SyntaxWarning linha ~8033 é do _AOVIVO_HTML pré-existente, não do patch); `sudo systemctl restart cctv-v6`.
- Provas: /youtube 200 «Comando manual» ×1 + «MODO MANUAL desde 14/09 22:40» + PRODUZIR + riocarta ×2; POST evil.com → 400; POST sem destinos → 400; GET /youtube/manual/status → 200 JSON (pedido 20260915_002223_6a027d legível); público /v6/youtube 401 sem creds / 200 com creds c/ bloco; ssh dispatcher: `youtube_manual` sem args → rc=64 uso (chave viva, nada produzido).
- ⚠️ Efeito colateral: o patch original tem BAK fixo (.bak_pre_ym_painel_20260915) e o shutil.copy2 sobrescreveu o histórico de 14/09 23:32 com o estado de hoje — sem perda de conhecimento (conteúdo vivo está no arquivo atual; pré-obra de hoje no .bak_pre_ym_restore), mas BAK FIXO em patch reaplicável é armadilha: nunca repetir.
- Artefatos: /tmp/patch_ym_painel.py + /tmp/patch_get_ym.py (tencent) = fonte canônica de reaplicação enquanto /tmp viver; bug recorrente registrado em CEREBRO_NODE_BUGS_ATIVOS (BUG-20260915-PAINEL-V6-SOBRESCRITA-SESSOES).

— ZCode/GLM-5.3 · 15/09/2026 15:2x BRT · adendo restauração

## ➕ Adendo 2 — fail-open exposto pelo 1º pedido real + curas (15/09 ~19:2x BRT)

- Pedido 151528 (Poll FLIP): Transkriptor Failed em 60s + yt-dlp «Sign in to confirm you're not a bot» (IP NYC) ⇒ 0 chars ⇒ executor seguiu (bloco_transcricao retorna "" e o prompt segue sem base) ⇒ LLM ALUCINOU aspas de Krystal Ball/Saagar Enjeti em 271151 (PT) e no post EN do GSN; auditoria (título/idioma/tamanho/entrevistado) NÃO pega aspas alucinadas.
- Push GSN com check=False + remote à frente (09b1ca1) ⇒ rejeitado silenciosamente; log «publicado» falso.
- Patch fail-closed (bak .bak_pre_failclosed_20260915 no NYC; /tmp/patch_failclosed_20260915.py na Dell): guarda `len(transcricao) < 500` ⇒ aborta com resultado 🔴 por destino + fase=erro; push capturado e RuntimeError se rc!=0.
- Limpeza: commit 3fca6e7 (GSN) descartado via fetch+reset --hard origin/main (backup .md+hero em /root/agent_data/youtube_manual/descartados/); 271151 backupado (/root/descartados_yt_20260915/ no cafezinho-wp) e trashed.
- Reexecução 192035_f7d739: transkriptor_url_direto OK 21.551 chars/US$ 3; draft 271200 (428 palavras, SEM aspas diretas — paráfrase); GSN 974feca pushado e 200 em www.globalsouth.news/blog/20260915-poll-reveals-shift-republicans-viewed-as-corrupt-and-extreme (apex 307→www é o padrão do site).
- Lições: (1) Transkriptor intermitente no MESMO vídeo (Failed 15:15 → Completed 19:24) — «tente de novo» é primeira resposta; (2) auditoria de aspas (grep na transcrição) ainda é MANUAL — gate automático proposto no fórum v1.2 aguarda «vai»; (3) tutor de bend: redirect apex→www do GSN confunde verificação — sempre -L ou www direto.

— ZCode/GLM-5.3 · 15/09/2026 19:2x BRT · adendo 2
