---
name: gerador_meta_textos com fallback Grok→gpt-4o (2026-04-17)
description: Adicionado fallback automático para gpt-4o quando Grok falha (429, timeout, etc). Antes Facebook/Instagram paravam inteiro quando créditos xAI acabavam.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 o `gerador_meta_textos.py` (usado por `agente_facebook.py` e `agente_instagram.py`) usava apenas `chamar_grok()`. Quando os créditos xAI esgotaram (`429 Client Error: Too Many Requests — Your team has either used all available credits or reached its monthly spending limit`), o Facebook ficou 100% parado: não gerava post nenhum.

**Fix aplicado (deploy 08:30):**
- Nova função `chamar_openai(prompt)` com modelo `gpt-4o` — reusa o mesmo `SYSTEM_PROMPT`/`LINHA_MESTRE_EDITORIAL` que o Grok usa.
- Nova função `chamar_llm(prompt)` — tenta `chamar_grok` primeiro; se retornar `None`, pula pra `chamar_openai`.
- Trocados 3 call sites (`gerar_texto_facebook`, `gerar_caption_instagram`, `gerar_badge_instagram`) para usar `chamar_llm` em vez de `chamar_grok` direto.
- `chamar_grok` mantida — é o caminho primário.

**Backup no servidor:** `/root/gerador_meta_textos.py.bak_20260417_0830`

**Why:** resiliência. Miguel precisa comprar mais créditos xAI ou o Grok fica "morto" por dias. Enquanto isso, gpt-4o atende.

**How to apply:** se for criar novo agente que usa LLM para gerar texto social, chamar `chamar_llm(prompt)` (com fallback) em vez de `chamar_grok` direto. Se precisar expandir o fallback (Claude, Gemini, DeepSeek), adicionar etapas em `chamar_llm`.
