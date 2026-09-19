# Auditoria V4

Este diretorio existe apenas para materiais de auditoria externa.

Nao e fonte viva de execucao. As fontes canonicas ficam na raiz do workspace:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

Pacote atual para Fable/GPT 5.5/AGY:

```text
pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Depois de extrair:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

Nao usar materiais em `Cerebro/Foruns/legacy/` para auditoria corrente.
