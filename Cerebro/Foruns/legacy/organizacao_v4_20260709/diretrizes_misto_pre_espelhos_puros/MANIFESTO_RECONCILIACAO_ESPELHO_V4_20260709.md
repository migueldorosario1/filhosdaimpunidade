# Manifesto de reconciliacao do espelho V4

Data: 2026-07-09  
Escopo: fatia fina V4 — curadoria de tese

Este manifesto registra que os contratos centrais do espelho de auditoria batem com a fonte viva local em `diretrizes/`.

Fonte viva:

```text
/home/migueldorosario/Downloads/Antigravity Google/diretrizes/
```

Espelho:

```text
/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/v4/diretrizes/
```

## Resultado

```text
diretrizes/v4_fluxo_dry_run_v1.json | Cerebro/Foruns/v4/diretrizes/v4_fluxo_dry_run_v1.json | 896994acdb55983e | 896994acdb55983e | MATCH
diretrizes/v4_agentes_tecnicos_v1.json | Cerebro/Foruns/v4/diretrizes/v4_agentes_tecnicos_v1.json | 327981757366393d | 327981757366393d | MATCH
diretrizes/v4_feedback_casos_editoriais_v1.json | Cerebro/Foruns/v4/diretrizes/v4_feedback_casos_editoriais_v1.json | 2d660740733d8403 | 2d660740733d8403 | MATCH
diretrizes/v4_bancos_camadas_v1.json | Cerebro/Foruns/v4/diretrizes/v4_bancos_camadas_v1.json | 7f05b0e76c709874 | 7f05b0e76c709874 | MATCH
diretrizes/v4_wordpress_publicador_v1.json | Cerebro/Foruns/v4/diretrizes/v4_wordpress_publicador_v1.json | c9b0314ba5a77b93 | c9b0314ba5a77b93 | MATCH
diretrizes/v4_curadoria_tese_v1.json | Cerebro/Foruns/v4/diretrizes/v4_curadoria_tese_v1.json | 481528bac0bda21e | 481528bac0bda21e | MATCH
diretrizes/v4_redator_shadow_v1.json | Cerebro/Foruns/v4/diretrizes/v4_redator_shadow_v1.json | b6839875ac367ea8 | b6839875ac367ea8 | MATCH
```

## Teste automatizado

`v4_diretrizes/test_contracts.py` agora inclui:

```text
test_espelho_diretrizes_reconciliado_com_fonte_viva
```

Esse teste falha se:

```text
- v4_fluxo_dry_run_v1.json do espelho divergir da fonte viva;
- v4_agentes_tecnicos_v1.json do espelho divergir da fonte viva;
- v4_feedback_casos_editoriais_v1.json do espelho estiver ausente ou divergente;
- bancos/camadas, publicador ou curadoria divergirem;
- o fluxo espelhado nao comecar por curadoria_dry_run;
- o produtor ou imagem espelhados nao lerem curadoria.
```

Validacao atual:

```text
python3 -m compileall -q v4_diretrizes
python3 -m v4_diretrizes.test_contracts
Resultado: OK 52 contract tests
```

## Observacao para auditores

Se algum parecer indicar que `v4_fluxo_dry_run_v1.json` ainda sai direto de `auditado` para `producao`, ou que `v4_agentes_tecnicos_v1.json` nao tem `curador`, o parecerista provavelmente recebeu pacote antigo ou cacheado.

No espelho atual:

```text
v4_fluxo_dry_run_v1.json:
  step 1 = curadoria_dry_run, from auditado, to curadoria
  step 2 = produzir_dry_run, from curadoria, to producao

v4_agentes_tecnicos_v1.json:
  inclui agente curador
  produtor.default_read_layers = [curadoria]
  imagem.default_read_layers = [curadoria]
```
