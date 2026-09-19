# Nota ao auditor — Fase 2 V4

Este e o pacote standalone executavel. Ele contem:

```text
diretrizes/
v4_diretrizes/
v4_data/
Cerebro/Foruns/diretrizes/
Cerebro/Foruns/diretrizes_sync_fase2_20260709/
Projeto Cafezinho Agentes/root/config/
```

Rode a partir desta raiz:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

Sanidade rapida:

```bash
grep -c "def test_" v4_diretrizes/test_contracts.py
grep -n "segundo a curadoria\|promessa editorial" v4_diretrizes/*.py Cerebro/Foruns/diretrizes/*.json || true
grep -n "Associated Press registra" Cerebro/Foruns/diretrizes/v4_real_001*.json
```

Resultados esperados:

```text
52
vazio para meta-linguagem em texto publicavel/gerador
fato USTR atribuido a Associated Press
```

Escopo: Fase 2 e somente `shadow_redacao`. Nao ha chamada LLM externa, nao ha WordPress real e nao ha publicacao real. No caso 261439, `collection_request.status=recommended` libera `shadow_redacao`, mas bloqueia `redator_real_llm` e `publicacao_real` ate coleta USTR/Federal Register.

O campo `texto_shadow` e placeholder de pipeline, nao benchmark final de prosa.
