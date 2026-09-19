---
name: feedback-pending-janela-24h-e-slots-reequilibrio-20260818
description: "Miguel 18/08 11:06 BRT — 3 correções operacionais. (1) Quando ele pergunta de pending/fila, é SEMPRE janela últimas 24h (nada de velharia). (2) Nacional (cat 22) e Geopolítica (cat 5003) são EDITORIALMENTE mais importantes que outras verticais — não tratar desequilíbrio 45%+29% pending como problema do worker V4. (3) Ensinar Claude Laura o protocolo Slots A/B (cadência, cutoffs, classificação) para ela operar quando piloto Trindade Laura estiver ativo."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 870114c6-7ee3-4080-8592-299996b3140e
---

## Contexto — o meu erro que gerou o feedback

Miguel perguntou 18/08 10:57 BRT se a fila estava engarrafada. Respondi olhando pending TOTAL histórico (143 posts, incluindo 1 de 01/08). Miguel corrigiu 11:06 BRT com 3 pontos:

> "mas o v4 nacional e geopolítica é mais importante mesmo. voce é que tinha que reequilibrar melhor os spots. E a propósito, tinha que ensinar o claude laura esse lance dos slots, etc. Mas olha só. quando eu perguntar de pending, é pending apenas das ultimas 24 horas, obviamente. não me interessa velharia"

## Regra 1 — Pending = últimas 24h SEMPRE

**Why**: fila V4 acumula lixo semanal (posts que esfriaram, temas fora de gancho, drafts abandonados). Contar tudo infla número e gera resposta enganosa. Miguel quer sinal editorial vivo, não estoque parado.

**How to apply**: quando Miguel perguntar "quantos pending", "está engarrafado", "como está a fila" — SQL com filtro `post_date >= DATE_SUB(NOW(), INTERVAL 24 HOUR)`. Se ele quiser panorama histórico, ele pede explicitamente ("me mostra pending desde início do mês"). Padrão silencioso é 24h.

**Exemplo do dia** (11:06 BRT): 143 pending total virou **22 pending 24h** — número operacional útil.

## Regra 2 — Nacional (cat 22) + Geopolítica (cat 5003) > outras verticais editorialmente

**Why**: linha editorial do Cafezinho é política nacional + geopolítica; cultura/economia/meio-amb/esporte/saúde são secundárias. Distribuição 45% geopolítica + 29% nacional pending **não é bug do worker** — é característica da linha editorial. Meu erro foi propor "arrumar o worker" quando o problema era minha cadência 50/50 Slot A/B tratando as duas metades como equivalentes.

**How to apply**:
- Ao ver distribuição desequilibrada (Slot A muito mais que Slot B), NÃO propor mudança no worker V4 nem no prompt.
- Meu ajuste = reequilibrar cadência dos slots. Regra proposta a Miguel (aguarda confirmação): quando Slot B chega vazio, rodo Slot A no mesmo ciclo. Zero desperdício.
- Se Slot B tiver 1-2 candidatos por dia, isso é normal — não escalar.

## Regra 3 — Ensinar Claude Laura sobre Slots

**Why**: piloto Trindade Laura foi ativado 18/08 03:01 (ZM-022) com Laura primária. Claude Laura precisa conhecer o protocolo Slot A/B pra decidir o que priorizar quando ela opera vigília. Hoje ela só sabe da parte editorial (título/imagem/texto); falta a parte de escolha operacional de posts por vertical/cutoff/classificação temporal.

**How to apply**: escrever doc pra ela em `Cerebro/Foruns/ponte_claude_miguel_laura/mensagens/para_laura/` contendo:
- Slot A = cats 22 (Nacional) + 5003 (Geopolítica) + 30 (Tec) + regionais. Prioridade editorial ALTA.
- Slot B = cats 79 (Cultura) + 43 (Economia) + 582 (Meio-amb) + 1271 (Esporte) + 258 (Saúde). Prioridade editorial SECUNDÁRIA (produz pouco, tudo bem).
- Cutoff CHURN 2h (post precisa ter esfriado antes de eu tocar; menor risco de sobrescrever ajuste que o V4 acabou de fazer).
- Classificação TEMPORAL (publish imediato ≤15min) vs ATEMPORAL (agendar future ≤8h à frente).
- Cadência 20min alternado A/B (revista quando Miguel confirmar fallback A se B vazio).
- Teto por ciclo: 3 publish + 2 correções.
- Fluxo publish: helper_gate → recibo _cafezinho_img_check via wp eval + file_get_contents → gate PASS antes de agendar.

Doc é apenas informativo (ela não decide publish — publish continua meu por §2 Contrato). Ela pode SUGERIR pela ponte editorial: "esse pending do 266XXX é Slot A temporal, vale mover pra front" — e eu executo se concordar.

Ligado a: [[project-laura-escopo-ampliado-corrigir-sim-publicar-nao-20260818]] · [[project-cadencias-trindade-20260817]] · [[project-laura-grok-operacao-sem-burocracia-20260818]].
