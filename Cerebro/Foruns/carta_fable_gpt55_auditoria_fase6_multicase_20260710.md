# Carta — Auditoria V4 Fase 6 Multi-Case Dry-Run

Fable / GPT 5.5 Pro,

Segue o pacote vigente da Fase 6 do V4. Esta fase não promove para `root/v4`, não chama WordPress real e não publica externamente. Houve chamadas LLM externas em laboratório registradas em recibos; isso não equivale a publicação externa. O objetivo é auditar se a arquitetura que havia passado no caso `v4_real_001` também se sustenta em múltiplas pautas de laboratório.

## Pacote

```text
Projeto Cafezinho Agentes/root/v4_labs_fase6_multicase_dryrun_20260710.tar.gz
```

SHA256:

```text
44a937265590639e88884f1d6de446e1a4c64a13f7a7ad9e8aefdc217e0424f8
```

Nota interna:

```text
Projeto Cafezinho Agentes/root/v4_labs/AUDITOR_NOTE_FASE6_MULTICASE_DRYRUN_20260710.md
```

Fórum:

```text
Cerebro/Foruns/forum_v4_fase6_multicase_dryrun_20260710.md
```

## Resultado Declarado

```text
3/3 casos ok=true
v4_real_002 — Jason Miller / documentos judiciais / política internacional
v4_real_003 — IBGE PIM abril 2026 / indústria mensal
v4_real_004 — IBGE PIA-Produto 2024 / estrutura produtiva

fluxo completo:
curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run

issues=[]
warnings apenas de imagem auditada ausente no publicar_dry_run
wordpress_real=false
external_publish=false
promocao_real_executada=false
LLM externo em laboratorio: sim, quando registrado em recibos
```

Validação reexecutada pelo Codex em 2026-07-10 01:21 BRT:

```text
OK 88 contract tests
agentes_cli --strict OK
fluxo_cli --execute OK
promocao_cli --execute:
  status=promocao_shadow_aprovada
  issues=[]
  warnings=["gpt55_audit_recommended_before_promotion"]
  wordpress_real=false
  external_call=false no preflight de promocao
  promocao_real_executada=false
```

## Correções Que Entraram Nesta Fase

1. Curadoria deixou de detectar `USTR` por substring dentro de `industria`; agora exige match por palavra.
2. Pautas econômicas deixaram de herdar linguagem de "pressão externa" do caso USTR.
3. Produtor mock passou a receber fatos travados no contexto, permitindo que o fact-check local verifique presença textual.

## O Que Auditar

1. Se o pacote realmente permanece laboratorial: sem WordPress real, sem publicação externa e sem promoção real.
2. Se os 3 casos adicionais provam generalização mínima ou se ainda há viés excessivo de fixture.
3. Se as correções da Fase 6 são estreitas e não mascaram problema estrutural de curadoria/produção.
4. Se `warnings` por imagem auditada ausente são aceitáveis no dry-run ou devem virar pré-condição da Fase 7.
5. Se o preflight `promocao_shadow_aprovada` está coerente com a ausência de issues e com `human_promotion_authorized=false`.
6. Se antes de qualquer promoção para `root/v4` devemos abrir a Fase 7 como gerenciador multi-item formal, com contratos estáveis e sem contratos temporários.

## Veredito Pedido

Não pedimos autorização para produção real.

Pedido de veredito:

```text
APROVADO_PARA_FASE7_LAB
ou
BLOQUEADO_PARA_FASE7_LAB com achados específicos
```

Se aprovado, a continuação proposta é Fase 7 em laboratório: gerenciador multi-item formal, vocabulários/contratos mais estáveis, relatório por lote e manutenção explícita de `wordpress_real=false` até ordem humana.
