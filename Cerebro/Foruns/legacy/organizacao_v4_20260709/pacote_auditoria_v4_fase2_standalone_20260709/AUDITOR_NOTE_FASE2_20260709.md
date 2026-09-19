# Nota ao auditor — Fase 2 V4

Este pacote standalone executavel foi gerado a partir das fontes vivas do V4.

Fontes vivas dentro do pacote:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

Contexto de discussao/auditoria:

```text
Cerebro/Foruns/v4/foruns/
Cerebro/Foruns/v4/cartas/
Cerebro/Foruns/v4/README_ORGANIZACAO_V4_20260709.md
```

Nao ha copias descompactadas de `diretrizes/`, `v4_diretrizes/` ou `v4_data/` dentro de `Cerebro/Foruns/v4/`. Esse foi um ajuste deliberado para evitar confusao entre fonte viva e material de forum.

Rode a partir da raiz extraida:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

Escopo: Fase 2 e somente `shadow_redacao`. Nao ha chamada LLM externa, nao ha WordPress real e nao ha publicacao real. No caso 261439, `collection_request.status=recommended` libera `shadow_redacao`, mas bloqueia `redator_real_llm` e `publicacao_real` ate coleta USTR/Federal Register.
