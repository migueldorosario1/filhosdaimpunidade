---
name: Fix ferroviário cross-post + fact-check + Tribunal Visual (2026-04-19)
description: agente_ferroviario_v2.py agora publica em 2 sites (mundotrilhos + cafezinho), com factcheck Claude corrigido e Tribunal Visual Gemini integrado.
type: project
originSessionId: bdb186bc-c504-409c-bc1f-aadf5fc5fe53
---
**Deployado 2026-04-19 16:47 BRT em Cingapura.**

## Mudanças aplicadas em `agente_ferroviario_v2.py`

**1. Cross-post duplo:**
- Adicionada lista `SITES_PUBLICACAO` com 2 configs: MundoTrilhos (primário) + OCafezinho (secundário).
- `upload_image_to_wp(filepath, title, site_cfg, legenda)` aceita config de site e legenda jornalística.
- `generate_featured_image` retorna `(media_id, img_path, legenda)` — a imagem local é reutilizada em cada site.
- `publish_post` POSTa no primário (com Yoast + indexador Google), depois replica nos sites extras via `_publicar_em_site`.
- Flag `CAFEZINHO_CROSS_POST_FERROVIARIO=0` desliga o cross-post se precisar.
- Categorias no Cafezinho: 14004 (infraestrutura) + 1650 (mobilidade urbana).

**2. Fact-check Claude corrigido:**
- Antes: `if "REPROVADO" in resposta.upper(): return False` — substring match rejeitava se a palavra aparecesse em qualquer lugar da resposta.
- Agora: prefixo `startswith("APROVADO")` ou `startswith("REPROVADO")`; em ambiguidade, quem aparece primeiro vence.
- Prompt amenizado: removi "precisão cirúrgica", reforcei que dados 2020-{ano} são normais. `max_tokens=20` (antes 10).
- Todo veredito agora é logado — facilita diagnose.

**3. Tribunal Visual Gemini integrado:**
- Helper `_tribunal_visual_aprovou(url, title, body, notes) → (bool, legenda)` chama `analisar_imagem_gemini_vision`.
- Aplicado ANTES do download em og:image e Wikimedia. Se reprovar, pula pra próxima fonte.
- Se aprovar, usa a legenda do Tribunal como caption/description do upload (tanto no primário quanto no cross-post).

## Validação DRY_RUN

- MundoTrilhos: DRAFT criado
- OCafezinho: DRAFT ID=236847 (https://www.ocafezinho.com/?p=236847)
- Tribunal reprovou foto da metro.sp.gov.br como esperado (genérica demais pro título)
- Fact-check retornou APROVADO na primeira tentativa (antes reprovava 100%)

## Histórico da crise pré-fix

- 10/04: agente ainda postava no Cafezinho
- 15-16/04: migrou pro MundoTrilhos — só 2 posts (wp_id 10 "Tram-train" e 12 "Linha 17-Ouro")
- 17-19/04: rodava 02h+04h (cron) mas `factcheck_claude_ferroviario` reprovava 100% das fontes → zero posts
- Por isso o site mundotrilhos.com estava praticamente vazio

## Pendências conhecidas

- Bug pré-existente em `gerador_imagem_editorial.py`: `list indices must be integers or slices, not str` (cai no fallback de segurança).
- Drafts de teste deixados pra deletar manual: 236842, 236847 (Sandbox bloqueou DELETE).
- Sentinela V3/V4 Autocura olha só o Cafezinho — posts replicados no Cafezinho entram no radar; posts primários no MundoTrilhos passam sem auditoria.
- `agente_rail_post.py` (60880 bytes, 15/04) existe no servidor mas não está no crontab — dormente.

## Backup

`/root/agente_ferroviario_v2.py.bak_pre_dual_pub_20260419` (60676 bytes, abr 19 16:38 BRT).
