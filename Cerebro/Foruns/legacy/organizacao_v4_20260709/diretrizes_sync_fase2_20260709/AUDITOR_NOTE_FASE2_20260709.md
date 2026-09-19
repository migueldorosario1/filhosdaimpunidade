# Nota ao auditor — Fase 2 V4

Este diretorio e o pacote leve de leitura/auditoria de contratos e artefatos. Ele permite verificar os JSONs, os scripts espelhados e os artefatos do caso 261439, mas nao contem o package Python completo com todos os modulos auxiliares.

Para executar os 52 testes de contrato de ponta a ponta, use o pacote standalone:

```text
Cerebro/Foruns/pacote_auditoria_v4_fase2_standalone_20260709/
```

Comando esperado dentro da raiz do pacote standalone:

```bash
python3 -m v4_diretrizes.test_contracts
```

Resultado esperado:

```text
OK 52 contract tests
```

Escopo: a Fase 2 segue em `shadow_redacao`. Nao ha chamada LLM externa, nao ha WordPress real e nao ha publicacao real. No caso 261439, `collection_request.status=recommended` libera `shadow_redacao`, mas bloqueia `redator_real_llm` e `publicacao_real` ate coleta USTR/Federal Register.

O campo `texto_shadow` e placeholder de pipeline. Ele serve para validar consumo de curadoria, fatos travados, consequencia material e ausencia de chamada externa. Nao deve ser usado como benchmark final de prosa.
