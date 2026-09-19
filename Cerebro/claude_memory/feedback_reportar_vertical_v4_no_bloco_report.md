---
name: feedback-reportar-vertical-v4-no-bloco-report
description: "Sempre que reportar posts publicados no bloco do ciclo vigília, incluir vertical V4 explícito (Geopolítica/Ciência-Tec/Nacional) por post — regra Miguel 28/07/2026 10:23 BRT"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Todo report de ciclo vigília V4 deve indicar EXPLICITAMENTE o vertical de cada post (Geopolítica / Ciência-Tec / Nacional). Miguel precisa dessa granularidade pra avaliar ritmo de cada worker Kimi separadamente.

**Como identificar o vertical:**
- **Fonte primária (preferida):** `meta.zizi_job_id` do post. Padrões:
  - `v4d_geopolitica_<hash>` → **Geopolítica**
  - `v4d_ciencia_<hash>` → **Ciência/Tec**
  - `v4d_nacional_<hash>` → **Nacional**
- **Fonte secundária (fallback quando zizi vazio):** categorias WP
  - Cats com `5003` → Geopolítica
  - Cats com `22` → Nacional
  - Cats com `19936`/`735`/`5008` → Ciência/Tec
  - Cat `20699` sozinha = no-home flag, NÃO indica vertical

**Como aplicar no report:**
- Tabela markdown do ciclo — adicionar coluna "Vertical" OU incluir vertical entre parênteses no título do post
- Exemplo: `**263238** (Geo) — *Petróleo cai 6,7%...*`
- Bloco final "Total do dia" já pode continuar como agora (X publicados / breakdown por vertical)

**Why:** Miguel 28/07/2026 10:23 BRT: *"quando mencionar os posts, menciona também qual o v4 que fez, se foi o v4 tecnologia ou geopolítica ou política nacional"*. Necessidade: acompanhar ritmo de cada worker (geo é o que mais produz atualmente, ciência estava travada até fix bilíngue Kimi 27/07 13:30, nacional teve cron migrado hoje).

**Regras irmãs:** [[feedback-checagem-dupla-editorial-com-autonomia]], [[feedback-nacional-tem-no-home-por-score]].
