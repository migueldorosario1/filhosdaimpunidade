---
name: feedback-tick-53-qualidade-20-posts-e-claudia
description: Mudança de foco do tick §53 (Miguel 07/06/2026 19:24 BRT) — cada tick examina qualidade profunda de 20 posts + lê 1 dia do doc da Cláudia Beatriz. Substitui o foco anterior de auditoria rápida.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🔍 **Novo formato do tick §53 (Miguel 07/06/2026 ~19:24 BRT):**
A cada tick, fazer:
1. **Auditoria profunda de 20 posts** (os 20 mais recentes ou janela equivalente)
2. **Relatório consolidado** com tabela + indicadores agregados + casos críticos
3. **Ler 1 dia** do doc da Cláudia Beatriz por tick (tracker em `Foruns/estado_leitura_doc_claudia_beatriz.md`)
4. **Cruzar padrões** entre auditoria do dia e padrões da Cláudia

**Why:** Miguel decidiu (07/06 19:24 BRT) que o foco do monitoramento muda — não é mais só "n posts novos auditados rapidamente", e sim qualidade profunda recorrente, integrando o trabalho manual da Cláudia. Objetivo: melhorar a redação ao longo do tempo, fechar gaps estruturais (§95 hiperlink, target= vazado, subtítulos errados, temas repetidos).

**How to apply (passo a passo):**

1. **Pegar 20 posts:** `curl WP API per_page=20 orderby=date order=desc status=any`
2. **Para cada post, conferir:**
   - Hiperlink fonte presente (regex `<a\s[^>]*href=[^>]+target=`)
   - "Via @handle" ou "Com informações de" (alternativa válida)
   - "target=" vazado como texto literal no corpo (strip HTML primeiro)
   - Title Case americano suspeito (≥5 palavras com maiúscula em título de 6+ palavras)
   - Siglas erradas (Nasa→NASA, Otan→OTAN, Eua→EUA, Onu→ONU, Stf→STF, etc.)
   - Editorial anti-Rússia/China/Irã reproduzido (regime de Putin, ditadura russa, agressão russa, anexação ilegal, regime chinês, etc.)
   - Inglês não traduzido (called, said, When X, United States, because, Chinese — ≥2 ocorrências)
   - FM=227448 (fallback genérico ferroviário)
   - Texto muito curto (<800 chars)
   - Subtítulo formato errado (Cláudia 06/06 #5: Título 2 onde devia ser Título 3) — **CHECK ADICIONAR**
   - Tema repetido nos últimos 40 posts (Jaccard título ≥0.70)
3. **Doc Cláudia:** ler próximo dia da fila no tracker `Foruns/estado_leitura_doc_claudia_beatriz.md` (15 dias, 1/tick, ciclo de ~7 dias)
4. **Relatório:** `Foruns/relatorio_qualidade_<YYYYMMDD>_<HHhMM>.md` com:
   - Tabela 20 posts
   - Indicadores agregados vs meta vs Cláudia
   - Casos críticos detalhados
   - Cruzamento Cláudia
   - Ações propostas (imediato / Kimi / Codex)
5. **Cadência:** mantém §53 (30min pico, 1h fora pico, 3h madrugada).

**Relação com formato antigo:**
O formato antigo (rápido N posts auditados nos últimos 30min) **SUBSTITUÍDO** por este. Antigos `relatorio_monitoramento_<data>_loop53_30min.md` viram histórico — novo nome `relatorio_qualidade_<data>_<hora>.md`.

**Inegociáveis preservados:**
- §52 soltar posts não prender
- §92 deploy gate
- §53 indexing check no auditor JSONL (em background)
- Não rebaixar draft humano (author≠5470) como captura

**Tracker doc Cláudia:** [[reference_doc_claudia_beatriz_monitoramento]] — file ID `1yZe_bG8hl1_sqxMfuXAiNrMvFczpQu59HrVjK7tI4EY`, 15 dias, char inicial mapeados em `estado_leitura_doc_claudia_beatriz.md`.

**Primeiro tick deste formato:** 07/06/2026 19:45 BRT — relatório `Foruns/relatorio_qualidade_20260607_19h45.md`. Dia da Cláudia lido: 06/06/2026.
