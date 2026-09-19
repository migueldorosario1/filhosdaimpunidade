---
name: feedback-nacional-tem-no-home-por-score
description: "Vertical Nacional V4 tem dispositivo no-home próprio via decide_no_home() calculado por score da nota — NÃO é bug quando post nacional aparece com cat 20699, é feature; só geo/ciência têm force_no_home hard-coded"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Não estranhar quando post do vertical Nacional V4 aparecer com cat `20699` (no-home). É feature, não bug. O worker chama `no_home_score_policy.decide_no_home(agent, score)` (v4_vertical_draft_worker.py linha 26 import + linha 1256 uso) que retorna `{no_home: bool, reason: ...}` calculado pela nota/score de cada post nacional individualmente. Score baixo → no-home ativado; score alto → post vai pra home.

**Diferença arquitetural entre verticais:**
- **Geo (5003) e Ciência (19936+):** `CONFIG` do worker tem `force_no_home: True` — TODOS vão no-home sempre, independente de score
- **Nacional (22):** SEM `force_no_home` — decide via `decide_no_home()` por post

**Why:** Miguel 27/07 13:31 BRT me corrigiu quando eu observei no canal_trindade que "263086 nacional veio com cat 20699 estranho pra nacional". Miguel: *"nao, o nacional tem dispositivo no-home também. tem um calculo por nota."* Verifiquei código imediatamente: `no_home_score_policy` importado e chamado com score. Comportamento normal.

**How to apply:**
- Se post nacional (cat 22) aparece com cat 20699 no `_get_categories()` → NÃO reportar como bug/anomalia
- Se quiser saber por que aquele post específico ficou no-home: puxar `meta.no_home_reason` ou similar do post via WP API context=edit
- Pendência conhecida do sistema (memória feedback_manifesto_bugs 22/07 ou anterior): "Score policy home/no-home entregando 60-90% HOME em vez de ~20%" — Codex investigar `decide_no_home()`, mas isso é sobre CALIBRAÇÃO da policy, não sobre existência dela
- Aplicar retroativamente: se em algum ponto anotei "nacional com no-home = bug", ignorar essa observação

**Regras irmãs:** [[feedback-checagem-dupla-editorial-com-autonomia]] (autonomia editorial), [[project-seo-pruning-automatizado-20260701]] (outro exemplo de decisão por score).
