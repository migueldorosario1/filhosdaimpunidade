---
name: auditoria-cega-exercitar-str-format-runtime
description: "Em auditoria cega de código Python que usa str.format() em templates, sempre exercitar .format() em runtime — não só validar string final isoladamente"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 831ab0d8-9f43-4146-9bf9-65f536fabdf7
---

Em auditoria cego de código Python que usa `str.format()` em templates (ex.: `prompt_template.format(**vars)`), sempre exercitar `.format()` em runtime com valores reais. Não basta validar a string final ou testar funções isoladas — é preciso chamar o `.format()` para detectar `KeyError` de chaves não-escapadas.

**Why:** Caso fundador em 21/06 01:00 BRT na auditoria PASSO 2B Política V2. Validei `_limpar_meta_discurso` empiricamente em 8 cenários exportando a função isolada — todos passaram. Mas o template do prompt em `v2_agente_tese.py:61` tinha `'{' e o último '}'` não-escapados. Quando chamado via `.format()` em runtime, gerava `KeyError: "' e o último '"`. Grok pegou (M10b); eu perdi. Admiti retratação no cruzamento duplo-cego-cruzado.

**How to apply:**
- Ao auditar arquivo `.py` que tenha template strings com `{variavel}` placeholders, grep por `'{` ou `{` literal dentro do template
- Verificar se chaves literais (não-placeholder) estão escapadas como `{{` e `}}`
- Em smoke tests, incluir cenário que force `.format()` em runtime mesmo quando mock path não o chama
- Smoke cenário 4 do PASSO 2B (mock sem `llm_client`) caía no mock interno que não invoca `.format()` — por isso M10b não foi detectado pelo smoke. Cenários que injetam `FakeLLMWithMeta` chamam `.format()` e teriam pego o bug.
- Lição geral cruzamento auditor duplo-cego-cruzado: 2 auditores olhando ângulos diferentes pegam bugs diferentes — função vs integração.

Ver [[feedback-auditoria-dupla-cega-cruzada]].
