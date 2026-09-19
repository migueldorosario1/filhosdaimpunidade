# Fórum — Adapter de busca na biblioteca de mídia do WordPress do Cafezinho

**Data:** 2026-08-09 ~05:20–06:10 BRT
**Sessão:** ZCode (GLM-5.2) — conversa "IMAGENS DUPLICADAS + adapter WP"
**Provador:** ordem do editor Miguel: *"os nomes que não tem foto no banco, você bota prioridade na fila para buscar, e você mesmo pode buscar no flickr. lembre que você pode publicar também no banco de midia do próprio wordpress do cafezinho. lá também tem imagens. de repente, essa é uma solução que pode resolver muita dor de cabeça nossa. desde que não seja imagem que a gente tenha usado já recentemente."*
**Estado:** ✅ ADAPTER CONSTRUÍDO, PLUGADO E TESTADO · 1 post resolvido (Mendonça) · ajuste fino de ranking pendente

---

## O que foi feito

### Novo adapter `_extract_wp_library_photo` no `v4_vertical_draft_worker.py`
Busca foto REAL na **biblioteca de mídia do WordPress** do Cafezinho (113.860 mídias, ~80% fotos reais com título descritivo) para personagens sem foto no banco ouro. É a fonte "da casa" — mais confiável que scrape externo.

**Fluxo do adapter:**
1. Extrai entidade do título (nome próprio capitalizado, filtra genéricos).
2. Busca `GET /wp-json/wp/v2/media?search=<entidade>&per_page=100` (per_page=100 para não perder fotos reais atrás das capas V4).
3. Filtra capas/IA (`v4-featured-*`, `cafezinho-*`, `trend-art-*`, `image-*`) — só fotos reais.
4. **Guarda anti-reuso (ordem Miguel):** exclui mídias usadas como featured nos últimos 50 posts (`_recent_featured_media_ids`) + as do ledger (`_load_used_media_urls`).
5. Ranking por tokens do nome (tolerante a nomes grudados: "MarinaSilvaTriste" casa com "Marina Silva").
6. Download → validação MIME/tamanho → **juiz visual Gemini** (`_audit_original_photo`).
7. Retorna dict no contrato dos 4 adapters (`content`, `content_type`, `source_url`, `image_url`, `caption`, `generator="wp_library"`, `visual_audits`) ou `None`.

### Ponto de inserção
**Logo após o banco ouro, antes de `_extract_original_photo`** (linha ~994). Justificativa:
- Mesmo tier editorial do banco ouro (acervo curado/próprio).
- **Resolve o buraco do "nacional"** — hoje nacional não tinha degrau de banco curado (banco ouro só roda para política/geopolítica/ciência/regional).
- Vem antes de scrape/flickr (fontes externas não-curadas).

### Provas
- `py_compile` OK.
- Busca WP confirmada: "Mendonça"→47, "Tarcísio"→102, "Marina Silva"→45 resultados. Com `per_page=100`: Tarcísio tem **70 fotos reais**, Mendonça **26**.
- **Post #264853 (Mendonça) resolvido ao vivo:** era foto do Lula, agora tem foto de evento judicial (caption: "Solenidade de posse..."). Aplicado via adapter + upload WP.

### Guarda anti-reuso (crítico)
- `_recent_featured_media_ids(site, auth)`: busca featured_media dos últimos 50 posts e bloqueia esses IDs.
- `_load_used_media_urls()`: ledger existente (URLs).
- Combinação garante que uma imagem não vira capa de 2 posts próximos (ordem Miguel atendida).

## O que falta / observações

- **Ajuste fino de ranking pendente:** quando várias candidatas empatam em score, a escolha pode pegar uma foto genérica ("Política V3 — oficial") em vez da melhor (#260153 `midia-v3-mendonca-...`). Melhoria: priorizar match da entidade no **nome do arquivo** (não só no título). Não-bloqueante — o juiz visual (Gemini) já filtra fotos ruins.
- **Resolver mais posts:** Marina (#264869, foto do Lula), Tarcísio (matéria Lula×Flávio em #264861). O adapter está pronto para rodar neles.
- **Mendonça/Marina/Tarcísio sem conta Flickr oficial** → biblioteca WP é a única fonte viável hoje; flickr_live não os cobre.

## Backups
- `v4_vertical_draft_worker.py.bak_pre_wp_library_20260809` no NYC.

## Reversão
Restaurar `.bak_pre_wp_library_20260809`. Mídias substituídas reversíveis via WP revisions.
