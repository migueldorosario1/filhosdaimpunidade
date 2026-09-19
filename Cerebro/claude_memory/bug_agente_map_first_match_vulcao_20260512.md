---
name: bug-agente-map-first-match-vulc-o-resolvido-12-05-23-23-brt
description: Vigia TE_V1 mapeava post científico de vulcão pra agente_geopolitica via first-match-wins de substring. Fix BC (longest-match + word-boundary regex) deployado com consenso Trindade 4/5.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e41c8659-4910-4323-a35a-1425133fac7c
---

# BUG-20260512-AGENTE-MAP-FIRST-MATCH-VULCAO

## Sintoma

Por 5 ticks (TE_V1 #51..#61, 17:30→22:30 BRT) o vigia da Trindade Econômica V1 atribuía post top "Poços de Caldas foi construída sobre caldeira vulcânica de 70 milhões de anos" ao `agente_geopolitica` em vez de `agente_fantastico`.

## Causa raiz

`mapear_agente_por_post()` linha 268 de `/root/trindade_economica_vigia.py`:

```python
for cat, agente in cat_to_agente.items():
    if cat in titulo.lower():
        return agente, ...   # primeira key matching ganha
```

Dois problemas combinados:
1. **First-match-wins**: a primeira key do dict que casa retorna; ordem do JSON importa.
2. **Substring sem word-boundary**: key curta tipo `"ira"` (de "Irã") matcha dentro de palavras maiores como "construída".

Refino que fiz às 17:11 BRT adicionou 19 keys científicas (vulcão, caldeira, fóssil, etc) no FIM do dict — não pegou porque alguma key geopolítica anterior já dava false-positive.

## Why (lição arquitetural)

Substring matching cego em dict ordenado é frágil em duas dimensões. Adicionar mais keys depois NÃO RESOLVE — o bug está na lógica, não nos dados. A regra a tirar: **se o problema persiste depois de mudar dados, o bug é de algoritmo, não de configuração.**

## Fix BC (deployado 23:23 BRT)

Editado `/root/trindade_economica_vigia.py`:
- Linha 38: adicionado `import re`
- Linhas 258-280: função reescrita

```python
melhor_match = None
melhor_len = 0
for cat, agente in cat_to_agente.items():
    cat_lower = cat.lower()
    if re.search(r'\b' + re.escape(cat_lower) + r'\b', titulo):
        if len(cat_lower) > melhor_len:
            melhor_len = len(cat_lower)
            melhor_match = agente
```

**B = longest-match-wins** (key mais longa = mais específica vence).
**C = word-boundary regex** (`\bcat\b` evita match dentro de palavras).

## Consenso

Trindade 4/5 BC (Miguel autorizou consenso parcial 23:17 BRT):
- Claude: BC (motivo articulado)
- DeepSeek V4: BC (só letra)
- Qwen: BC ("longest-match evita ambiguidade, word-boundary elimina falso-positivo")
- Antigravity: BC ("A é band-aid; única forma robusta")
- Kimi: ⚠️ abstém — API silenciosa (4 tentativas, zero output sem erro)
- Codex: ignorado nesta votação (ocupado com smoke Rio Carta)

## Validação

- **Smoke local 7/7 OK** (`/tmp/test_vigia_func.py`):
  - vulcão→fantastico ✅
  - "Construída em ira de Deus"→geopolitica ✅ (word-boundary preserva matches reais)
  - "ira" em "construída" não matcha mais ✅
- **py_compile** OK local + remoto
- **Smoke real Tencent tick #63** (23:23 BRT, dry-run manual): `agente_top: agente_fantastico` ✅
- **MD5:** antes `12c67ffbc0dadcbbcb275d5664fb1bfc` → depois `6c3b8ab2fbec937db6b87cbf4aa83bcd`
- **Backup remoto pré-deploy:** `/root/Backups/vigia_pre_fix_BC_20260512_2320_claude.py`

## How to apply (regra geral)

Em qualquer função que faça lookup palavra-chave → categoria/agente/tag, **NUNCA usar `keyword in texto` cego**:
1. Use `re.search(r'\b{kw}\b', texto)` pra word-boundary.
2. Itere TODAS as keys e escolha a MAIS LONGA que casa (não a primeira).
3. Documente `Fix BUG-ID` na docstring se a função foi corrigida pra futuros agentes não regredirem.

Vinculado: [[reference_trindade_economica_vigia]] · [[manual_de_bugs_ler_primeiro]]. Indexado também em `CEREBRO_NODE_BUGS.md` linha 39 (Codex 22:52 BRT, atualizado por Claude 23:23 BRT).
