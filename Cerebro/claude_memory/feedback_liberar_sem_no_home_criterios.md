---
name: feedback-liberar-sem-no-home-criterios
description: Post pode ser publicado SEM cat 20699 (No home) se atender 3 critérios rígidos - checagem tripla DS+GPT+Claude + nota muito boa + imagem real. Miguel 11/08 03:37 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab72ecc4-9deb-4729-9735-80bcceefd907
---

Post V4 pode ser publicado **SEM cat 20699 (No home)** apenas se atender **todos** os 3 critérios:

1. **Checagem tripla completa** — DS + GPT + Claude+WebSearch, com pipeline opção 2 paralelo (regra 09/08 17:20)
2. **Nota muito boa** — `peso_editorial: alto` no DS OU GPT (não médio, não baixo)
3. **Imagem real** — featured_media é foto jornalística/arquivo/oficial, NÃO IA nem placeholder

**Se qualquer um dos 3 falhar:** mantém cat 20699 default. Todos os outros posts continuam recebendo cat 20699 como padrão (comportamento atual).

**Why:** Miguel 11/08 03:37 BRT: "se tiver post com nota muito boa e imagem real, pode liberar sem no-home. mas só posts checados triplamente por ds, gpt e voce". Confiança editorial em posts que passaram por 3 revisões independentes + têm imagem legítima — merecem menos gatekeeping.

**How to apply:** No fluxo de publish do loop Vigília (DIA/NOITE), após rodar DS+GPT+Claude+WebSearch, checar:
- Ambos DS e GPT retornaram (nenhum `dsgpt_timeout`)
- Ao menos um dos dois marcou `peso_editorial: alto`
- Featured media do post (`featured_media` != 0, checar `_wp_attachment_metadata` ou similar pra confirmar não é IA)

Se **todos** OK → publish sem incluir 20699 na lista de `categories`.
Se **qualquer** falhar → publish com 20699 (comportamento atual, home garantida).

**Registro obrigatório no JSONL bugs:** campo novo `liberado_sem_no_home: true|false` + `razao_no_home` se true (ex: "peso_alto_ambos_ds_gpt_imagem_real").

Regra irmã: [[feedback-reportar-vertical-v4-no-bloco-report]] (o report continua indicando vertical) · [[feedback-vigilia-v5-dsgpt-paralelo-websearch]] (pipeline paralelo obrigatório) · [[feedback-titulo-tese-corpo-argumenta]] (qualidade editorial base).
