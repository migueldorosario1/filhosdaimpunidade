---
name: feedback-no-home-fim-semana
description: "Fim de semana (sábado 00:00 → domingo 23:59 BRT): remover cat 20699 (no-home) de TODOS os posts V4 publicados. Volta ao normal automaticamente na segunda. Aplicar a todas as verticais (Geo + Ciência-Tec + Nacional)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b2a244d9-f9b6-46dc-8edb-3f4744e84e11
---

**Regra:** Sáb/dom BRT, remover cat `20699` (no-home) de todos os posts publicados pelo loop V5 antes do `wp_post`. Segunda-feira volta ao comportamento V4 padrão (Geo/Ciência com `force_no_home: True` hard-coded + Nacional por score).

**Why:** Miguel 01/08 13:19 BRT autorizou: *"pode remover no-home de tudo no final de semana. na segunda volta ao que era antes"*. Motivação: volume noticioso natural é menor no fim de semana → home fica com mais movimento se posts que iriam pra no-home vão pra home. Escolha por "de tudo" (não parcial) elimina risco de conflito com escolha de manchete — não há mecanismo automatizado de manchete no pipeline V4 (verificado via grep 01/08), então empurrar tudo pra home dá controle manual total ao Miguel.

**How to apply:**

**No wrap `backup_and_publish` de cada ciclo Vigília V5:**
```python
from datetime import datetime, timezone, timedelta
weekday = datetime.now(timezone(timedelta(hours=-3))).weekday()  # 5=sab, 6=dom
if weekday in (5, 6):
    cats = [c for c in cur.get('categories', []) if c != 20699]
    payload['categories'] = cats
```

**Aplicar a TODAS as verticais** — Geo + Ciência-Tec + Nacional. Zero exceções no fim de semana. Segunda-feira `weekday()==0` faz a condição pular sozinho — sem código de rollback.

**Se detectar retroativamente que posts publicados no fim de semana ainda estão com cat 20699** (ex: publicado por outro agente antes desta regra entrar em vigor), aplicar `POST /wp/v2/posts/{pid}` com `{"categories": [...sem 20699]}` + backup pré-edit + SHA-256 no JSONL do dia.

**No log JSONL de bugs, registrar como:**
```json
{"acao_final": "no_home_removido_fim_semana", "categories_antes": [...], "categories_depois": [...], "obs": "sábado/domingo BRT — cat 20699 removida automaticamente"}
```

**Rastreabilidade:**
- Caso fundador 01/08/2026 (sábado): **11 posts** publicados com no-home receberam remoção retroativa entre 13:20-13:30 BRT (IDs 263638, 263847, 263653, 263634, 263838, 263857, 263654, 263844, 263851, 263852, 263854)
- Backups em `Cerebro/Backups/vigilia_v5/2026-08-01/` com prefix `_pre_remove_nohome_`
- Todos em `Cerebro/monitoramento_horario/bugs_encontrados/bugs_2026-08-01.jsonl`

**Não confundir com Nacional score:** regra `feedback_nacional_tem_no_home_por_score` diz que Nacional recebe cat 20699 por score baixo do próprio worker V4. Isso é comportamento normal dias úteis. No fim de semana, minha regra **sobrescreve** — remove no-home mesmo de Nacional com score baixo. Volta ao normal segunda-feira automaticamente.

**Anti-pattern:** NÃO aplicar em posts autor 2018 (james2017 = Miguel via Antigravity Desktop) — só posts autor 5786 (agente V4 puro). Regra de escopo do loop Vigília se mantém.

Regras irmãs: [[feedback-loop-vigilia-opus-v5]], [[feedback-nacional-tem-no-home-por-score]], [[feedback-baleia-azul-editor-chefe-claude]].
