---
name: feedback-duplicata-pos-publish-vira-pending
description: "Quando Claude detectar duplicata semântica de post JÁ PUBLICADO, ação padrão é mudar status para 'pending' (revisão), não 'draft' nem 'trash' — regra Miguel 27/07 14:20 BRT via Kimi"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0c239f1e-08c3-4beb-a91e-5adf020d8159
---

**Regra:** Quando eu identificar que um post já publicado (`status=publish`) precisa sair do ar por ser duplicata semântica de outro publicado, precisa hold editorial, ou similar → mudar status para **`pending`** (revisão). NÃO `draft`. NÃO `trash`.

**Why:** Miguel 27/07/2026 14:20 BRT (via Kimi K3 `[KIMI-PENDING-RULE-263072]` 14:26 no canal). Caso fundador: 263072 (duplicata do 263017) publicado pelo Miguel manual foi movido de `publish` → `pending`. Racional: `pending` é "um degrau abaixo de publish" — mantém o post rastreável na fila de revisão editorial, tira do ar imediato, permite reversão fácil pra publish depois se decisão editorial mudar. `draft` sumiria da fila de revisão; `trash` seria destrutivo e vira 410 Gone pro Google.

**How to apply:**
- Detectei duplicata semântica de post JÁ PUBLICADO → `wp_post(env, f'/wp-json/wp/v2/posts/{PID}', {'status': 'pending'})`
- Ponteiro no canal com tag `[CLAUDE-DUP-PUBLISH-PENDING]` explicando qual post virou pending + qual é o duplicado canônico
- NÃO aplica a DRAFTS duplicados — esses continuam como draft (não published ainda, então não estão no ar; Kimi ou Miguel decide se vira pending, trash ou mantém pra reprocesso)
- NÃO aplica a posts com erro factual grave após publish — nesse caso preferir `editar_corpo_publicado` in-place (memória `feedback_autocura_protocolo_registro_com_solucao_e_rollback`) que preserva URL indexada
- Backup pre-transição sempre (memória AUTOCURA), + registro 3 camadas
- Se um post movido pra pending for restaurado pra publish depois (Miguel/Kimi decide), restaurar via `{'status': 'publish'}` (não perde histórico WP nativo)

**Estados WP relevantes:** `publish` (no ar), `pending` (revisão, fora do ar mas rastreável), `draft` (rascunho, fora do ar, autor pode editar), `trash` (lixeira 30d recuperável) → escala de destruição crescente da direita pra esquerda. Regra prefere o mínimo destrutivo.

**Regras irmãs:** [[feedback-checagem-dupla-editorial-com-autonomia]] (autonomia editorial), [[feedback-autocura-protocolo-registro-com-solucao-e-rollback]] (backup sempre), [[feedback-seo-pruning-uso-restrito]] (410 Gone requer autorização Miguel — pending NÃO é 410, apenas oculta do frontend).
