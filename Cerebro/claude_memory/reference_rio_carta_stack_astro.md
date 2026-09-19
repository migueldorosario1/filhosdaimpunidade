---
name: rio-carta-n-o-wordpress-astro-est-tico-vercel
description: "Rio Carta usa Astro (build estático), markdown em src/content/blog/, deploy Git/Vercel. Credencial WP no CLAUDE.md §12 é legado da migração antiga, não vale."
metadata: 
  node_type: memory
  type: reference
  originSessionId: e41c8659-4910-4323-a35a-1425133fac7c
---

# Rio Carta — stack real (Miguel correção 2026-05-12 23:50 BRT)

**Rio Carta NÃO é WordPress.** Não usar WP REST API. Não usar credencial `migueladmin / Qs7zCNRfVYp86wO1C9ycxpfZ` do CLAUDE.md §12 — é legado da migração antiga e está desatualizado.

## Stack real

- **Framework:** Astro (build estático)
- **Repo local:** `Rio Carta Agentes/rio_carta/`
- **Conteúdo:** markdown em `src/content/blog/` com frontmatter padrão Astro:
  ```yaml
  ---
  title: ...
  draft: true|false
  heroImage: ...
  tags: [...]
  ---
  ```
- **Build:** `npm run build` no diretório `rio_carta/` → `dist/` com 2210 páginas estáticas
- **Deploy:** via Git push → Vercel (rebuild automático)
- **Inbox de matérias:** `riocarta_inbox.db` (SQLite, 255 matérias prontas em 12/05)
- **Diagnóstico de mídias legado:** `Rio Carta Agentes/Foruns/forum_descasamento_de_imagens.md` + `Rio Carta Agentes/root/riocarta_diagnostico_midias_wp.py` (read-only)

## Independência do silo

ADENDO 11 do CLAUDE.md (12/05): *"Rio Carta deve permanecer independente do Cafezinho. Agentes, scripts, configs, fóruns e índices vivos do Rio Carta devem usar namespace `riocarta_`, `rio_carta` ou `rio-carta` e residir no silo Rio Carta."*

## Publicação 3/h (decisão Miguel 12/05 23:40+23:53 BRT)

- 3 matérias por hora, com auditoria pré-publish
- Progressão geométrica controlada (3 → 6 → 12...) conforme auditoria aprova
- Auditoria ampliada: cruza modelos chineses; quórum >3 votos favoráveis pra deploy
- Status inicial dos posts: `draft: true` no frontmatter; humanos revisam no admin antes de publish manual

## Fix de imagens crítico

CLAUDE.md ADENDO 11 + diagnóstico Codex 12/05: *"Não rodar reparo massivo por `_thumbnail_id` sozinho. Qualquer script de correção deve usar grafo de candidatos e classificar `OK_FISICO`, `AUSENTE_TAR`, `MISMATCH_BINARIO`, `SEMANTICO_SUSPEITO`, `INLINE_FALLBACK`, preferindo placeholder/revisão a publicar foto errada."*

Vinculado: [[reference_trindade_economica_vigia]] · [[feedback_autocura_claude_3de4_quorum]] (autocura §51 vale Cafezinho + Rio Carta).
