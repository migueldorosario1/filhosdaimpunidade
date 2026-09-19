---
name: feedback-imagem-destacada-obrigatoria
description: "Toda publicação Cafezinho (publish via REST API ou motor) DEVE ter featured_media setado. Sem isso, rebaixar pra draft. Regra inviolável detectada por Miguel 22/05 14:37 BRT após Claude publicar manualmente sem."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 656d971f-de46-442e-a3e2-07fe0206d845
---

# Imagem destacada é OBRIGATÓRIA em qualquer publicação Cafezinho

**Regra inviolável:** nenhum post no Cafezinho WordPress pode ir ao ar com `status=publish` sem `featured_media` setado (≠ 0).

**Why:** Miguel apontou em 22/05/2026 14:37 BRT após eu (Claude Maestro) publicar a matéria CartaCapital BR-07114 (post #250395) manualmente via REST API esquecendo o `featured_media`. Sem imagem:
- SEO degrada (Google rank cai)
- Compartilhamento social (Open Graph) fica vazio — engagement zero
- Layout home/feed quebra (placeholder)
- Identidade visual do portal fica prejudicada

**How to apply:**

### Publicação manual via REST API (Maestro/admin)

Sempre incluir `featured_media` no POST inicial:

```bash
curl -X POST https://controle.ocafezinho.com/wp-json/wp/v2/posts \
  -u "Redator:..." \
  -d '{"title":"...","content":"...","featured_media":<ID>,"status":"publish"}'
```

Hierarquia de fonte (CLAUDE.md §3.4):
1. `og:image` da fonte original
2. Banco SQLite `banco_midia_cafezinho.db` por entidade
3. Flux / Ideogram / DALL-E
4. **Fallback ÚLTIMO:** `FEATURED_IMAGE_ID=227448` (padrão Cafezinho do `.env.unificado`)

### Publicação automatizada (motor)

`motor_publicador.py` já valida `_thumbnail_id`. Garantir invariante: **se `featured_media` ausente/zero, rebaixar pra `draft` ou abortar publicação. NUNCA forçar `publish` sem.**

### Lapso pós-fato (correção)

Se publicou sem, PATCH IMEDIATO:

```bash
curl -X POST https://controle.ocafezinho.com/wp-json/wp/v2/posts/<post_id> \
  -u "..." -d '{"featured_media":<ID>}'
```

### Histórico de aplicação
- 22/05/2026 14:34 — Claude publicou post #250395 sem featured_media (lapso)
- 22/05/2026 14:37 — Miguel detectou e apontou
- 22/05/2026 14:38 — Claude PATCH com `FEATURED_IMAGE_ID=227448` (fallback padrão)
- 22/05/2026 14:38 — Inscrito em `CEREBRO_NODE_GOVERNANCA.md` §86 + memória aqui

Relacionado: [[reference_sistema_resumo]] (CLAUDE.md §3.4 Tribunal Visual + Banco Mídia)
