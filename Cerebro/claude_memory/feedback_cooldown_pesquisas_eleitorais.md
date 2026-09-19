---
name: feedback-cooldown-pesquisas-eleitorais
description: "Cooldown anti-repetição em pesquisas eleitorais — uma matéria por pesquisa+instituto, exceto se nova matéria trouxer ângulo/análise claramente diferente."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

📊 Quando sair uma pesquisa (Datafolha, Quaest, Ipec, AtlasIntel, Genial, PoderData, etc), publicar **1 matéria principal**. Próximas matérias sobre a MESMA pesquisa+instituto só passam se trouxerem **ângulo/análise claramente diferente** (recorte regional, série temporal, comparação entre institutos, recorte demográfico, leitura editorial específica). Sem ângulo novo → não publicar (rebaixar draft).

**Why:** Miguel 2026-06-21 ~16:30 BRT: "Você está repetindo muito. A gente já publicou várias sobre Datafolha. Toda pesquisa é a mesma coisa, você fica publicando várias matérias sobre a mesma pesquisa, fica demais." Caso fundador: 3 matérias sobre Datafolha 20/06 em 4h (#260078 12:40, #260109 16:09, #260114 16:12 draft). #260109 tem ângulo único (agregação 3 institutos), #260078 e #260114 são redundantes.

**How to apply:**
1. **Chave de dedup**: `(instituto, data_da_pesquisa)` — ex.: `(Datafolha, 2026-06-20)`.
2. **Cooldown**: se já existe publish recente com mesma chave nas últimas **24h**, bloquear nova publicação.
3. **Exceção — ângulo novo**: liberar se nova matéria tem **pelo menos uma** de:
   - Comparação entre múltiplos institutos (mesma janela)
   - Recorte demográfico/regional não coberto na primeira
   - Série temporal (evolução vs pesquisas anteriores)
   - Leitura editorial específica (ex.: impacto Sul Global)
4. **Implementação técnica sugerida** (sprint Codex/Kimi): SQLite `pesquisas_publicadas (instituto TEXT, data_pesquisa TEXT, post_id INT, angulo TEXT, ts TIMESTAMP, UNIQUE(instituto, data_pesquisa, angulo))`. Antes do publish, agente_publicador consulta — se chave já existe e novo `angulo` é vazio/repetido, rebaixar pra draft.
5. **Cura retroativa** quando detectar repetição já publicada: manter a 1ª, rebaixar repetições pra draft. Caso fundador: #260114 mantido draft pela cura 2026-06-21.

Aplica em conjunto com [[feedback-pesquisas-fonte-primaria-sem-repercutidor]].
