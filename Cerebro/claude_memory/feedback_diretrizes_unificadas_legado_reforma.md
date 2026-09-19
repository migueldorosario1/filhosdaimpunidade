---
name: feedback-diretrizes-unificadas-legado-reforma
description: "Miguel 15/06 ~18:15 BRT — A partir de agora, TODA regra/diretriz editorial nova deve ser inserida tanto no LEGADO quanto na REFORMA. Manter tudo unificado. Quando aparecer um erro novo (ex: título 'marcando marco' redundância tosca), adicionar EXEMPLO concreto na diretriz dos DOIS sistemas pra não repetir. NÃO esquecer um dos dois."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Diretrizes unificadas — LEGADO + REFORMA sempre

Miguel 15/06 ~18:15 BRT, ao revisar o título #258717 "LandSpace lança... marcando marco na corrida espacial":

> *"que coisa horrível! que llm produz um título horrível desse? corrige isso imediatamente e acrescenta o exemplo na diretriz para não termos esse erro! a partir de agora, bota sempre nas diretrizes do legado e da reforma, para a gente ter tudo sempre unificado."*

## A regra

**Sempre que um erro editorial recorrente for identificado e a cura for adicionar uma instrução na diretriz, fazer no LEGADO E NA REFORMA simultaneamente.** Não deixar um dos dois pra depois.

## O que isso significa na prática

1. **Erro novo flagado** (Miguel reclama OU detecto em tick §53 OU GLM/Qwen aponta)
2. **Cura imediata do post** já publicado (cura §51 via WP API)
3. **Diretriz nova** com exemplo concreto: "EVITAR redundância tosca como 'marcando marco' (mesmo radical)" — texto explícito
4. **Aplicar a regra nas DUAS bases**:
   - LEGADO: `/root/diretrizes_editoriais.py` (ou módulo equivalente do produtor)
   - REFORMA: `/root/cafezinho/portal_cafezinho/Sistema/agentes/produtor_geral.py` + `auditor_texto.py` + `diretrizes_editoriais.py`
5. **AUTH §92 cheio** com diff explícito → backup ambos → patch ambos → py_compile ambos → sanity ambos → smoke ambos → rollback documentado ambos
6. **Codex audita** pós-execução

## Casos fundadores

**15/06 18:00 BRT — #258717 "marcando marco"**:
- Título publicado: "LandSpace lança com sucesso foguete melhorado Zhuque-2, marcando marco na corrida espacial comercial chinesa"
- Redundância tosca: "marcando" + "marco" (mesmo radical lexical)
- Cura §51 imediata: "marcando marco" → "e consolida avanço"
- **Diretriz nova** a inserir LEGADO + REFORMA: "Verbo + substantivo do mesmo radical/cognato — EVITAR ('marcando marco', 'finalizando final', 'consolidando consolidação', etc). Quando a frase repetir radical lexical, REESCREVER trocando uma das ocorrências por sinônimo distante."

## Outros padrões pra agregar na mesma diretriz unificada (ir acumulando)

À medida que novos casos aparecem, adicionar exemplos curtos pra fortalecer a regra:

- Redundância radical ("marcando marco")
- Auto-referência "O Cafezinho reitera" (já em AUTH-022 REFORMA — precisa replicar LEGADO)
- Clichê extemporâneo "Sul Global" em pauta off-topic (já em AUTH-022 REFORMA — replicar LEGADO)
- Minúscula início de parágrafo `<p> aaa` em vez de `<p>Aaa` (2 casos #258714/258712 — registrar)
- Title Case americano em vez de sentence case PT-BR
- HTML entities vazados `&#8216;` no título

## How to apply

1. **No próximo erro flagado**: cura imediata + AUTH §92 cheio nas DUAS bases.
2. **Ao propor AUTH**: explicar no diff que a aplicação é simultânea LEGADO + REFORMA, com 2 backups, 2 sanitys, 2 rollbacks.
3. **No fórum**: criar `forum_diretrizes_unificadas_legado_reforma_<data>.md` ou anexar nos fóruns existentes com tag "DUPLO".
4. **Memória**: atualizar esta entrada com cada caso novo adicionado, mantendo histórico.

## Why

Miguel quer COERÊNCIA entre LEGADO e REFORMA durante a fase dual. Se uma regra existe num só, os 2 sistemas produzem qualidade diferente — e quando o cutover REFORMA ↔ LEGADO acontecer, a regressão é certa. Unificação simultânea = single source of truth distribuído mas idêntico.

Relacionados:
- [[feedback_cafezinho_defende_china_global_times_alinhado]] (diretriz fundadora China)
- [[feedback_sul_global_defender_nao_repetir_chiclete]] (anti-clichê, já em AUTH-022 REFORMA — pendente LEGADO)
- [[feedback_cutover_legado_so_apos_saude_reforma]] (durante fase dual, ambos precisam estar saudáveis)
- [[feedback_llm_sempre_para_editorial_nunca_lista_fixa]] (regras editoriais via prompt LLM, não lista fixa)
