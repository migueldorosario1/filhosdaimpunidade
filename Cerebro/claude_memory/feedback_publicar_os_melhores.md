---
name: Política "publicar os melhores, não guilhotinar"
description: Miguel pediu expressamente para não usar cortes duros na coleta ou na publicação — ordenar os melhores e publicar. Guilhotina só quando houver censura por erro factual no final do pipeline.
type: feedback
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Regra editorial do Cafezinho: **não guilhotinar pautas ou imagens com cortes duros. Ordenar pelo score e publicar os melhores.** A única guilhotina legítima é no *final* do pipeline, quando o fact-check (Perplexity/Claude) vetar por erro factual.

**Why:** Em 2026-04-17 o Miguel corrigiu a lógica do `motor_coletor.py` que estava usando `corte_dinamico = max(score_minimo*0.60, maior_nota*0.65)` — descartando a maioria das matérias aprovadas pela IA quando aparecia um outlier (maior_nota=12 → corte=7.8, matando notas 1-7). Resultado visível: banco geopolítica com 1 matéria, publicador dizendo "banco vazio". Miguel disse: *"agora a ordem não é guilhotinar tudo, tanto na coleta quanto na publicação, mas escolher os melhores e publicar os melhores. Guilhotina apenas se houver censura no final por conta de erros."*

**How to apply:**
- Em qualquer refactor de coleta/publicação/curadoria, **confiar no filtro primário da IA** (score >= 1.0 já é qualidade aprovada) e não adicionar segundo corte estatístico por cima.
- Ordenar por score do maior para o menor, mas **manter a cauda** — não cortar "os piores" dos aprovados. Quem segura a qualidade final é o fact-check, não a curadoria de entrada.
- Aplicar esse mesmo princípio ao `motor_publicador.py` (ex: `nota_corte_imagem=90` é agressivo — cogitar reduzir quando tiver contexto).
