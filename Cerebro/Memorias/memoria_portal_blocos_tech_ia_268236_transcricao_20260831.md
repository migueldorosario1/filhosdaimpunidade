# 🧠 MEMÓRIA TÉCNICA — Blocos Tech/IA + 268236 + cascata transcrição (31/08/2026)

**Tema Duplo:** `Foruns/forum_portal_blocos_tech_ia_268236_transcricao_20260831.md`
**Sessão:** ZCode/DeepSeek (Dell), 31/08 09:40→~11:00 BRT. Ordem do Miguel ~09:35.

## Comandos e caminhos (reproduzível)

- WP canônico: `ssh cafezinho-wp` + `--path=/var/www/ocafezinho --allow-root` (wp-cli como root EXIGE --allow-root; sem isso erro suprimido por 2>/dev/null parece "post não existe").
- WP espelho: `ssh root@159.65.177.60` + `--path=/var/www/cafezinho-news --allow-root`.
- Recategorização segura: `wp post term add <ID> category <term_id> --by=id` (sem --by=id cria categoria falsa com nome do número — reincidência da lição de 30/08) + `wp post meta update <ID> _yoast_wpseo_primary_category <term_id>` + `wp cache flush`.
- Contagem por bloco/dia (BRT = GMT−3): `wp db query "SELECT DATE_FORMAT(DATE_SUB(p.post_date_gmt, INTERVAL 3 HOUR), '%d/%m') dia, tt.term_id, COUNT(*) n FROM ${P}posts p JOIN ${P}term_relationships tr ON tr.object_id=p.ID JOIN ${P}term_taxonomy tt ON tt.term_taxonomy_id=tr.term_taxonomy_id AND tt.taxonomy='category' WHERE p.post_type='post' AND p.post_status='publish' AND p.post_date_gmt >= DATE_SUB(UTC_TIMESTAMP(), INTERVAL 6 DAY) AND tt.term_id IN (...) GROUP BY dia, tt.term_id ORDER BY p.post_date_gmt DESC"`.
- Estado da esteira: `ssh nyc` + últimos JSONs de `/root/v4_labs/dados/v41_ciclo/*.json` (campo `vertical`, `status`, `post_id`) + `/root/agent_data/v41_ciclo.log`.
- Pautas: `/root/agent_data/v4_verticals/ciencia_tecnologia_ia.sqlite3` (tabelas candidates/rejections/runs/draft_events). ⚠️ `observed_at` é ISO com `T` — filtrar tempo com `LIKE 'AAAA-MM-DD%'`, NUNCA `>= datetime('now',...)` (comparação de string entre formatos infla tudo).

## Mudanças em produção (todas com backup + py_compile 3/3)

1. `/root/agents_labs/youtube_v2/youtube_transcription_fallbacks.py` `.bak_pre_cascata_assemblyai_20260831`: `DEFAULT_PROVIDERS` `"supadata,transkriptor"` → `"supadata,assemblyai,transkriptor"` (assemblyai tem chave no `/root/chaves.sh`; provider `_provider_assemblyai` já existia linha 211).
2. `/root/agents_labs/youtube_v2/agente_youtube_v2_coletor_dialogos.py:205` `.bak_pre_hint_assemblyai_20260831`: hint default `"transkriptor"` (morto) → `"supadata,assemblyai"`.
3. `/root/v4_vertical_intake.py` `.bak_pre_tech_sem_nexo_20260831`: gate tecnologia — `geo_tech_score < 4` deixou de ser veto; com termo tech no título entra com badge `v4_tech_sem_nexo_geo` (nexo = prioridade no score). Prova: intake tecnologia `accepted 1→4 / new_rows 3`; candidatas novas 31/08 = 4 (média histórica 1–4/dia).
4. WP canônico + espelho: post 268236 Cultura/Séries → **Geopolítica 5003 + Internacional 15** (primary 5003). Origem do erro: pauta nasceu `zizi_job_id=v41_cultura_cde667611f8b` (programa "Brasil no Mundo" classificado como cultura).

## Descobertas estruturais (não óbvias)

- **Bloco Tecnologia (cat 30) secou por dreno estrutural:** a vertical `digital` (principal fornecedora da cat 30) migrou para 5008 em 27/08 (V41_IA_20260827). Sobrou só a vertical `ciencia`, funil de 1–4 candidatas/dia → 0 posts de 29–31/08. Patch do nexo ajuda; engordar de verdade = decisão Miguel: tech-IA em 2 blocos `[5008,30]` × ampliar fontes do coletor `tec`.
- **Fila de capas é o gargalo da publicação inteira:** 19 rascunhos (268291→268386) sem `_cafezinho_img_check`; a ronda V4.1 30/30 (automation-90a56cde, ATIVA, 56 runs) é o 5º fallback legítimo de caça — não duplicar em sessão manual.
- **Cascata de transcrição estava vazia na prática** (supadata sem chave + transkriptor morto) — um dos motivos do agente YouTube não fechar fichas (`publicaveis_pendentes: 0`, último post cat 28 em 28/08 17:39). Lives agendadas ainda são tentadas ("begin in 10 hours") — filtro `is_upcoming` existe (coletor:153-160), checar ORDEM vs job de transcrição (pendência).
- `wp rocket purge` não existe como comando wp neste WP — `wp cache flush` cobre o object cache.
- wp post list de drafts: usar `wp post list --post_status=draft,future` (SQL cru com LEFT JOIN + GROUP BY retornou vazio sem explicação).

## Pendências

1. Capas dos 19 rascunhos (esteira AGY/CL — cobrado na ponte ZM-20260831-002; prioridade 268380/268386).
2. Validar ciclos seguintes (ciência ~10:45 BRT, digital 14:00 BRT): mais rascunhos tech/IA com cats certas.
3. Ordem live-check × transcrição no coletor YouTube.
4. Degrão Whisper Tencent grátis na cascata (mini-serviço HTTP) — escopo futuro.
5. Decisões Miguel: Supadata (logar/colar chave), Transkriptor (parecer: desnecessário tecnicamente), (a)×(b) do bloco Tecnologia.

— ZM · ZCode/DeepSeek · 31/08/2026 ~10:00 BRT

## Adendo 31/08 ~11:1x — DSN IMAGEM NO AR (ordem Miguel "pode ir, vai")

- Worker: `/root/v4_labs/codigo/dsn_imagem.py` v2 (NYC) — scheduler da fila de capas; cron `*/20` c/ flock `/tmp/dsn_imagem.lock` (backup `crontab.bak_pre_dsn_imagem_20260831`). Visão: factory `create_media_vision_provider` = DeepSeek × Fallback([Qwen, Gemini]) — o desenho pedido pelo Miguel, nativo do código.
- Convergência com sprint V4.1 Vision (irmã, GLM-5.3, ordem via carta CM 09:55): aplicação de capa 100
## Adendo 31/08 ~11:15 — DSN IMAGEM NO AR (ordem Miguel "pode ir, vai")

- Worker: `/root/v4_labs/codigo/dsn_imagem.py` v2 (NYC) — scheduler da fila de capas; cron de 20 em 20 min com flock `/tmp/dsn_imagem.lock` (backup `crontab.bak_pre_dsn_imagem_20260831`). Visão: factory `create_media_vision_provider` = DeepSeek × Fallback([Qwen, Gemini]) — o desenho pedido pelo Miguel, nativo do código.
- Convergência com sprint V4.1 Vision (irmã, GLM-5.3, ordem via carta CM 09:55, que JÁ aplicou capa no 268380/mídia 268395): aplicação de capa 100 por cento via `codigo.wp_apply_featured_image --decision <path> --post-id X --execute`; ACK + nota de coordenação no `estado.json` compartilhado. Editorias do request = canônicas do gerador (ciencia_tecnologia_ia|politica_economia|geopolitica_internacional|cultura) — categoria WP explode o gerador IA (generated_image_editoria_invalid, que era o motivo dos generation_failed nos testes da manhã).
- Provas: rodada 1 E2E (fila 19 posts detectada; 268394 processado sem crash); rodada v2 E2E (14:05 UTC: 268393 com entity curta → 1 candidata → visão dupla rejeitou → fila de olho humano); carimbo REST provado (probe ok:false no 268291, post morto); FIX FLICKR_API_KEY sem export no chaves.sh:99 (backup `.bak_pre_flickr_export_20260831`) — sem export, subprocess não herda → flickr_api_key_missing.
- Estado/LOG: `/root/agent_data/dsn_imagem/estado.json` + `log.txt`; fila de OLHO HUMANO no estado (268380 pessoa/Emenda 12, 268386 marcas/Emenda 8 + rejeitados da visão).
- Lições: primary_entity = título inteiro → 0 candidatas na busca externa (v2 usa 6 primeiras palavras); printf com "%" no texto quebra (usar heredoc); monitor vivo muda entre sessões → sempre re-ler antes do Edit.
