---
name: feedback-url-categoria-cafezinho-e-slug-direto-sem-prefixo
description: URLs de categoria no Cafezinho são /slug/ direto (não /category/ nem /categoria/) por Yoast stripcategorybase=true. Falso positivo 11/08 06:00 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

**URL correta de categoria no Cafezinho é o slug direto, sem prefixo.**

Ex:
- ✅ `ocafezinho.com/geopolitica/` — funciona (200)
- ✅ `cafezinho.news/economia/` — funciona (200)
- ❌ `ocafezinho.com/category/geopolitica/` — 404 (formato WordPress vanilla desligado)
- ❌ `ocafezinho.com/categoria/geopolitica/` — 301 redirect (formato português também desligado)

**Why:** Cafezinho usa plugin **Yoast SEO** com opção `stripcategorybase = true` + `category_base = "categoria"`. Isso desliga qualquer prefixo na URL de categoria — serve direto pelo slug raiz. Configuração intencional desde sempre. Não é bug.

**Erro que cometi (11/08 05:47 BRT):** ao auditar espelho, testei `/category/geopolitica/` (formato padrão WP vanilla) e reportei 404 como bug. Miguel pediu pra investigar. Descobri que URL correta é `/geopolitica/` direto e ambos os sites funcionam. Bug marcado como `NOT_A_BUG_ERRO_DE_DIAGNOSTICO_CLAUDE` em `lab_visual_bugs/bugs_2026-08-11.jsonl` (LV-20260811-001).

**How to apply:** ao testar URL de categoria/tag/arquivo/autor em Cafezinho:

1. **Verificar setting antes de assumir formato:** `get_option("category_base")` + `get_option("permalink_structure")` + `get_option("wpseo_titles")["stripcategorybase"]`
2. **Formato canônico Cafezinho:**
   - Categoria: `/slug/`
   - Post: `/YYYY/MM/DD/slug/` (permalink dia+nome)
   - Autor: verificar (não testei) — provável `/author/slug/`
   - Tag: verificar
   - Arquivo: `/YYYY/` ou `/YYYY/MM/`
3. **Nunca reportar bug de rewrite sem antes checar Yoast SEO settings** — Yoast tem toggles pra desligar praticamente qualquer URL do WP vanilla

**Padrão pra futuras auditorias de lab visual:** antes de rodar suite de HTTP status em URLs de categoria/tag/arquivo, pegar as URLs REAIS do WP via query dos options e testar essas — não assumir vanilla.

Regras irmãs: [[feedback-lab-visual-anotar-bugs-seguranca-port-canonico]] (protocolo bugs lab visual) · [[project-lab-visual-cafezinho-news-20260811]]
