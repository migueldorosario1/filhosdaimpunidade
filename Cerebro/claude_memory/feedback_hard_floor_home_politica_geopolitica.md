---
name: feedback-hard-floor-home-politica-geopolitica
description: "Política (lula, eleições, flavio, crime, repetidor) + Geopolítica (soberania, militar, latam, sheinbaum, china) JAMAIS vão pra no_home — hard-floor visível na home. Ciência/IA/Fantástico SEMPRE no_home. §107 aplicado 2026-06-20 ~10:55 BRT após caso #259920 (matéria sobre ex-chefe Carlos Bolsonaro réu por peculato saiu no_home errado, Miguel reverteu)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7b054038-ee9d-4869-bac1-f58e75f914b3
---

# Hard-floor HOME/NO_HOME por tema editorial

**Política e Geopolítica NUNCA podem sair como no_home. Ciência/IA/Fantástico SEMPRE no_home. Independente de teto diário ou contador.**

**Why:** Caso fundador 20/06 ~10:50 BRT — post #259920 "Justiça torna ex-chefe de gabinete de Carlos Bolsonaro réu por organização criminosa e peculato" (cat=22 Política) saiu no_home. Miguel reverteu manualmente e cravou a regra: "política, eleições, flavio, lula, nunca é no-home" + "no home é mais ciência, ia, fantástico". A lógica antiga em `maestro_distribuicao.py` aplicava teto rígido `META_VISIVEIS=50` que, após atingido, empurrava qualquer agente (mesmo SÉRIO) pra no_home — bug operacional que invisibilizava matérias politicamente fortes só porque "deu o teto do dia".

**How to apply:**

Listas vinculantes em `/root/maestro_distribuicao.py` (LEGADO):

| Conjunto | Agentes | Comportamento |
|---|---|---|
| `AGENTES_HARD_HOME` | lula, eleicoes, flavio, crime, repetidor (política) + soberania, militar, latam, sheinbaum, china (geopolítica) | `decidir_no_home()` retorna `False` SEMPRE |
| `AGENTES_HARD_NO_HOME` | ia, fantastico | `decidir_no_home()` retorna `True` SEMPRE |
| Demais | matriz, mercado, inflacao, turismo, ferroviario, reciclador, analytics | Seguem `AGENTES_SERIOS`/`AGENTES_LEVES` com teto 50/100 |

Em qualquer patch futuro que toque `decidir_no_home()` ou as listas de agentes:
1. Não remover `AGENTES_HARD_HOME`/`AGENTES_HARD_NO_HOME` sem nova diretiva Miguel
2. Verificar antes do teto/contador (linha 230-235 do maestro)
3. Ao adicionar agente novo, classificar como hard-home, hard-no_home, ou neutro conforme tema editorial
4. REFORMA: aplicar mesma lógica quando agentes da Reforma entrarem em produção

Vinculada a [[project-cafezinho-media-group-diretriz-18jun]] (foco editorial: IA + Política/Geopolítica + Comércio Exterior + Ciência séria).
