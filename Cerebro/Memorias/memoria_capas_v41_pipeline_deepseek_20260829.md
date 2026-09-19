# Memória técnica — Capas V4.1 × pipeline de imagem × DeepSeek Vision (29/08/2026)

Log completo da missão (par técnico do `Foruns/forum_capas_v41_deepseek_vision_20260829.md`).

## Topologia e comandos

- NYC (`ssh nyc`): `/root/v4_labs/codigo/` (pipeline), `/root/venv/bin/python3`, cofres `/root/chaves.sh` + `/root/chaves_novas.env` + `/root/.env.unificado`.
- WP (`ssh cafezinho-wp`): `wp ... --path=/var/www/ocafezinho --allow-root`.
- CLI: `python3 -m codigo.featured_image_runtime_cli <pedido.json> --allow-network --execute --root /root/v4_labs` (flags `--no-flickr`, `--no-ai`). `--execute` persiste decisão em `agent_data/v4/media/pipeline_decisions/`, NUNCA sobe ao WP.
- Env correto p/ rodar: `set -a; . /root/chaves_novas.env; . /root/chaves.sh; set +a` (novas.env tem atribuições SEM `export`; chaves.sh por último).
- Healthcheck visão: `python3 -m codigo.vision_healthcheck_cli --env /root/.env.unificado --out <json>` (8 casos).

## Schema do pedido (FeaturedImageRequest)

`item_id, title, primary_entity, editoria, target_status, curadoria_id, article_sha256 (sha256 hex do corpo WP ou vazio), frame_visual{entidade_principal, conflito_visual, evitar, prioridade, tese_principal}, requires_person`. `prioridade=pessoa`/`requires_person=true` liga o gate de pessoa.

## Cadeia de gates (por que uma capa passa ou não)

1. Coleta: `audited_store` → Flickr (allowlist `config/v4_flickr_official_accounts.json`, `global_fallback=True`, máx 8) → OpenCatalog (Openverse + Commons `gsrsearch=primary_entity`, `iiurlwidth` agora 1920, máx 5/fonte).
2. Técnico: dims mínimas 1200x675; `media_declared_width_mismatch` se declarado ≠ baixado; `media_animated_rejected`; orçamento de visão `max_visual_calls=5` (candidatas além disso = `visual_candidate_budget_exhausted` — Flickr entra na frente e pode comer o orçamento!).
3. Visão (DoubleCheck DS primário × Qwen secundário; divergência de identidade >0,30 → `ambiguous_identity`): `entity_present`, `prominent`, `crop_safe`, `screenshot/logo/montage` → `visual_format_rejected`; pessoa nomeada exige `origin_trusted` (conta oficial Flickr) OU metadata confirmada — Commons/Openverse são NÃO confiáveis p/ pessoa → `trusted_metadata_identity_missing` → human_review.
4. Score: `final_score = 0,65*score_candidata + 0,35*confiança_visual`, mínimo 70.
5. `promote()` no acervo auditado é fail-closed: só recibo `approved`+`safe`. NÃO existe override humano (lacuna → proposta `media_human_review_cli`).

## Bugs corrigidos (commits/backs no NYC)

1. `open_catalog_media.py`: dims do derivado (1920 proporcional) + `iiurlwidth=1920` (2400 → HTTP 400 "Use thumbnail sizes listed on https://w.wiki/GHai"). Backup `.bak_pre_fix_thumbdims_20260829`.
2. Credencial: `DEEPSEEK_API_KEY` morta sha8 `b6c4d4de` (401 texto+visão) deprecada; viva `f0aaa272` espelhada; `FLICKR_API_KEY` (sha8 `9c684254`) espelhada no `chaves.sh`. Backups `.bak_pre_higiene_deepseek_20260829`. ⚠️ Lição: `chaves_novas.env` SEM `export` exige `set -a`; ordem de source muda a chave efetiva.
3. Observado: crons do `v41_ciclo` NÃO sourcam chaves.sh (lêem env por outro caminho) — integrar na Fase 2.

## Evidências-chave

- DeepSeek direto na foto CPI da Leila: `entity_present=true, crop_safe=true, subject_bbox 0,90x0,98, face_bbox ok, identity_confidence=0,8` (custo ~US$0,0003/análise; saldo DeepSeek US$56,96 em 29/08).
- Qwen sozinho (quando DS 401): bbox absurdo (faixa 0,42 de altura num close-up) → prova de que o cruzamento DS×Qwen é o que presta (regra sagrada do Miguel).
- Commons sonda (UA obrigatório `Cafezinho-V4-MediaScout/1.0`, senão 403): Dario Amodei só 2023; Leila 2018-2022 + CPI 2024; Santa Cecília estação 2024; Siraya Lai Ching-te 2021.
- Pedidos de teste em `/tmp/capas/*.json` (NYC); decisões em `/root/v4_labs/agent_data/v4/media/pipeline_decisions/`.

## Fila de drafts sem capa (29/08 16h)

268226, 268228, 268236, 268245, 268250 (268230 tem capa 268243, dedup canibal pendente vs 268062).

## Próximo (Fase 2, aguarda "vai")

`media_human_review_cli` (promoção humana append-only c/ operador+motivo+recibo) + chamada do runtime no `v41_ciclo` pós-rascunho + cron varredura drafts sem capa + upload WP (`wp media import` + `_thumbnail_id` + meta §86 + `wordpress_media_cli add`).

— ZCode/Qwen 3.8 · 29/08/2026

## ADENDO 29/08 ~18:20 — visão do Dell + prova SHA1 de identidade

- `/tmp/ds_vision_dell.py` (Dell): lê `DEEPSEEK_API_KEY` do cofre local, POST `https://api.deepseek.com/chat/completions` c/ model `deepseek-v4-flash-vision-exp`, imagem em base64 data-URL, `max_tokens=800`, prompt curto. Prova: HTTP 200, 746 tokens. Cofres Dell espelhados c/ chave viva (sha8 `f0aaa272` via `printf '%s'`; o `3471bb06` anterior incluía `\n`).
- Identidade 268228: DS disse Maria do Rosário (erro); olho sozinho incerto; SHA1 da imagem (`6931e37be8dba0c41c6e23fce3f6b35f2b926a2f`) → `action=query&list=allimages&aisha1=` no Commons (UA `Cafezinho-V4-MediaScout/1.0`) devolveu `Leila_Pereira_-_CPI_da_Manipulação_de_Jogos_e_Apostas_Esportivas_(cropped).jpg` = entidade do draft. Receita SHA1→Commons = desempate canônico de identidade p/ Fase 2.

## ADENDO 29/08 ~22:05 — fila de capas andando (provas WP)

- Loop noturno Laura/AGY publicou com capa: 268228→`_thumbnail_id` 268263 (`leila-cpi-2024.jpg`, a candidata validada no ADENDO 1), 268250→268265 (`taiwan-indigenous.jpg`), 268245 (19:43) c/ retrato oficial Trump. Verificação: `wp post meta get <ID> _thumbnail_id` + `wp post get <thumb> --fields=post_title,guid`.
- Restam SEM_CAPA (22:05): drafts 268226 e 268236; novos drafts da esteira noturna sem capa: 268266, 268268, 268273.
- Commit/push: ver linha ZM no ATUALIZACOES (ronda 22:00).
