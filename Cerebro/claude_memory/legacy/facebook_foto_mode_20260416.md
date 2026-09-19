---
name: Facebook agora posta com imagem destacada (modo /photos)
description: Sistema de postagem no Facebook migrado de /feed (link preview feio) para /photos (imagem destacada como foto principal com caption).
type: project
originSessionId: d93140b1-8d95-4fdf-b122-0e1b195d583e
---
Em 2026-04-16 o fluxo de postagem no Facebook foi reformulado:

**Arquivos alterados:**
- `postador_meta.py` — `postar_facebook()` aceita `image_url`. Com imagem, usa `/{FB_PAGE_ID}/photos` (url + caption). Sem imagem, fallback pro `/feed` original.
- `gerador_meta_textos.py` — Prompt do Grok reescrito: emojis temáticos, tom combativo/Sul Global, zero hashtags, CTA "☕ Leia a matéria completa no link abaixo."
- `agente_facebook.py` — Nova função `buscar_imagem_destacada(post_id)` via WP REST API com `?_embed`. Fallback para og:image. Cooldown reduzido de 4h para 15min.

**Why:** Posts apareciam como link preview feio sem controle de imagem. O modo /photos gera posts visualmente muito melhores no feed.

**How to apply:** O `postar_instagram()` não foi alterado. Se precisar mudar o comportamento do Facebook, os 3 arquivos acima são os envolvidos.
