---
name: feedback-lula-nunca-cat-crime-sempre-politica
description: "Miguel 17/06 ~10:50 BRT — pauta com Lula NUNCA pode receber cat=4995 Crime, mesmo que tenha keyword 'crime organizado' no lide. Sempre cat=22 Política. ADICIONAR conforme contexto: cat=[5088 Eleições, 2900 Pesquisas] se eleições 2026; cat=[5003 Geopolítica] se reunião internacional (G7/BRICS+/cúpula). Caso fundador #259008 17/06 Lula G7 que saiu como Crime porque lide tinha 'combate ao crime organizado' (frase diplomática Lula contra ingerência EUA) — Miguel curou pra [5003 Geopolítica, 22 Política]. Regra editorial inegociável: Lula = Política sempre, nunca Crime. Vale tanto pra cura §51 quanto pra peer review futuro do `util_categorizador_rigido.py`."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Lula NUNCA cat=Crime — sempre Política + contexto

## A regra

Miguel 17/06 ~10:50 BRT, após cura manual #259008:

> "melhor acrescentar, se tem Lula não pode ser crime, é sempre política e as vezes mais outra, como eleições 2026 e, no caso de reunião internacional, geopolítica"

## Aplicação

**Toda pauta com Lula no título OU sujeito do lide deve receber:**
- `cat=22 (Política)` SEMPRE — base obrigatória
- + `cat=4995 (Crime)` **PROIBIDO** — mesmo que keyword "crime organizado" / "crime" / "facção" apareça
- + EXTRAS conforme contexto:
  - **Eleições 2026/pesquisas eleitorais** → adicionar `[5088 Eleições, 2900 Pesquisas]`
  - **Reunião internacional** (G7, BRICS+, cúpula, OEA, ONU, UE) → adicionar `[5003 Geopolítica]`
  - **Discurso/política internacional** (sem reunião específica) → adicionar `[15 Internacional]`

## Por quê

Lula é sujeito político central da pauta editorial Cafezinho. Quando aparece em pauta sobre "combate ao crime organizado" como **fala/discurso/posição**, é política/diplomacia — não pauta criminal.

A confusão acontece porque `util_categorizador_rigido.py` (AUTH-034 16/06) tem regra forte pra keyword "crime organizado" e dispara cat=4995 mesmo em pauta diplomática. Caso fundador: #259008 17/06 "Lula critica tarifaço de Trump e defende soberania no G7" — lide continha "ingerência externa no combate ao crime organizado" (recado diplomático Lula a Trump). Saiu como Crime. Miguel curou pra [5003 Geopolítica, 22 Política].

## Como aplicar

### Cura §51 imediata (no tick §53)

Se detectar pauta Lula com `cat=[4995 Crime]`:
1. **Rebaixar Crime instantaneamente** (curar via WP API)
2. Substituir por `cat=[22 Política]` + extras contextual:
   - Eleições/pesquisa → adicionar `[5088, 2900]`
   - Cúpula G7/BRICS+ → adicionar `[5003 Geopolítica]`
   - Discurso internacional genérico → adicionar `[15 Internacional]`

### Peer review Codex (AUTH-049 ou similar)

Adicionar regra de EXCLUSÃO no `util_categorizador_rigido.py`:
```python
# Se sujeito é Lula/presidente Brasil, NÃO classificar como Crime
# mesmo que keyword "crime organizado" presente
if has_keyword(["Lula", "presidente Lula", "Luiz Inácio Lula da Silva"]) \
   and predicted_cat == 4995:  # Crime
    return [22]  # forçar Política como base
```

## IDs categorias relevantes

- `22` = Política (base obrigatória pra Lula)
- `4995` = Crime (PROIBIDO em pauta Lula)
- `5003` = **Geopolítica** (não "Soberania" — eu corrigi nomenclatura 17/06)
- `5088` = Eleições
- `2900` = Pesquisas
- `15` = Internacional / Política Internacional (slug `politica-internacional`)

## Caso fundador

- **#259008** 17/06 10:14 BRT "Lula critica tarifaço de Trump e defende soberania no G7"
- Saiu cat=`[4995 Crime]` por bug `util_categorizador_rigido`
- Miguel curou pra `[5003 Geopolítica, 22 Política]` ~10:48 BRT
- Miguel deixou regra: "Lula nunca Crime; sempre Política + às vezes Eleições/Geopolítica"

## Relacionados

- [[feedback_corrigir_na_raiz_nao_no_auditor]] — regra de exclusão NO CLASSIFICADOR é correção raiz; cura WP é só remediação
- [[feedback_cafezinho_defende_china_global_times_alinhado]] — semelhante: keywords/contexto da linha editorial vencem regra mecânica
- [[reference_doc_claudia_beatriz_monitoramento]] — Cláudia Beatriz pode pegar esses padrões em revisão diária
