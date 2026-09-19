# Organizacao V4 em Foruns

Data: 2026-07-09

Diretorio ativo:

```text
Cerebro/Foruns/v4/
```

## Regra principal

```text
Cerebro/Foruns/v4/ e apenas diretorio de discussao/auditoria e material para colar em Fable/GPT 5.5/AGY.
Nao e fonte viva de execucao.
Nao deve conter copias descompactadas de `diretrizes/`, `v4_diretrizes/` ou `v4_data/`.
Nao editar aqui como origem de producao.
```

## Estrutura ativa

```text
foruns/     discussoes V4
cartas/     cartas V4 para colar em auditores e pareceristas
auditoria/  pacotes zipados/notes para auditoria externa
```

Pacote atual para Fable/GPT 5.5/AGY:

```text
Cerebro/Foruns/v4/auditoria/pacote_auditoria_v4_fase2_standalone_20260709.tar.gz
```

Forum especifico sobre organizacao e deploy Tencent:

```text
Cerebro/Foruns/v4/foruns/forum_organizacao_arquivos_v4_deploy_tencent_20260709.md
```

Comando esperado dentro do pacote extraido:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

## Legado

Duplicatas, aliases e pacotes intermediarios foram movidos para:

```text
Cerebro/Foruns/legacy/organizacao_v4_20260709/
```

Nao usar `legacy` para auditoria corrente. Ele existe apenas para rastreabilidade e recuperacao.

## Fontes vivas de execucao

As fontes vivas de execucao continuam na raiz do workspace:

```text
diretrizes/
v4_diretrizes/
v4_data/
```

Qualquer mudanca de codigo, contrato ou dado de trabalho deve ser feita nas fontes vivas. Quando houver auditoria externa, gerar um pacote zipado em `Cerebro/Foruns/v4/auditoria/` a partir dessas fontes canonicas.
