# Auditor Note — Fase 6 Multi-Case Dry-Run

Data: 2026-07-10

Escopo: validar se a arquitetura V4 sai do caso único `v4_real_001` e roda pautas adicionais em dry-run, sem WordPress real e sem promoção para `root/v4`.

## Casos Rodados

```text
v4_real_002 — Jason Miller / documentos judiciais / política internacional
v4_real_003 — IBGE PIM abril 2026 / indústria mensal
v4_real_004 — IBGE PIA-Produto 2024 / estrutura produtiva
```

## Resultado

```text
3/3 ok=true
issues=[]
warnings=["imagem_destacada_pendente:*"] apenas no passo publicar_dry_run
wordpress_real=false
external_publish=false
```

Relatório materializado:

```text
dados/promocao/v4_labs_multi_case_dry_run_20260710.json
```

## Correções Feitas Durante a Rodada

1. A curadoria deixou de detectar `USTR` por substring dentro de `industria`.
2. Teses de pauta econômica deixaram de herdar linguagem de pressão externa.
3. O produtor mock passou a receber os fatos travados no contexto, permitindo que o fact-check local verifique presença textual.

## Validação

```text
OK 88 contract tests
agentes_cli --strict OK
fluxo_cli --execute OK
promocao_cli --execute:
  status=promocao_shadow_aprovada
  issues=[]
  warnings=["gpt55_audit_recommended_before_promotion"]
  wordpress_real=false
  external_call=false
  promocao_real_executada=false
```

## Limite

Esta fase não abre publicação real, não promove para `root/v4` e não substitui revisão editorial humana. O objetivo foi provar que curadoria, produção mock, revisão, fact-check, auditoria final e publicação dry-run funcionam em mais de uma pauta.
