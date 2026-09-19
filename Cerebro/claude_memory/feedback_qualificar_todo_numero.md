---
name: qualificar-todo-numero
description: Todo número reportado ao Miguel deve vir com qualificação (bom/ruim/normal/alerta) — nunca número cru
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8f64da6c-82cd-49c1-ae1d-c915d81a8046
---

Todo número que eu trouxer pro Miguel precisa de qualificação imediata — dizer se é bom, ruim, normal, preocupante, excelente.

**Why:** Miguel não quer interpretar números brutos. Ele precisa saber de relance se algo precisa de atenção ou está ok. Número sem contexto é ruído.

**How to apply:** Em TODA comunicação com dados numéricos (monitoramento, custos, load, disco, tracebacks, posts, velocidade):
- Load 0.15 → "ocioso, excelente"
- Disco 61% → "tranquilo, longe do limite"
- Custo $22/dia → "acima do normal ($15-20 baseline), mas caindo após fix"
- 229 tracebacks → "crônico, não é novo, sem impacto na publicação"
- HTTP 200 em 1.3s → "rápido, bom"
- featured_media=0 num publish → "ALERTA: post sem imagem"

Regra vale pra monitoramento, relatórios, diagnósticos, qualquer mensagem com dados.
