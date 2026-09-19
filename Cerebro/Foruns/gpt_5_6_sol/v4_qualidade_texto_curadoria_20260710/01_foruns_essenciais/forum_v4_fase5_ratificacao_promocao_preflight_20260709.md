# Fórum — V4 Fase 5: Ratificação de Promoção e Política `recommended`/`required`

**Data:** 2026-07-09  
**Status:** discussão leve / sem fonte viva  
**Fonte viva técnica:** `Projeto Cafezinho Agentes/root/v4_labs/`  
**Pacote atual:** `v4_labs_fase5_promocao_preflight_auditfix_20260709.tar.gz`  
**SHA256:** `68f7d1eb9f025be2f19383368219e6b93856d444f3162c71e601adce315cd976`

## Síntese

A Fase 5 criou um preflight de promoção. Ele não move arquivos para `root/v4`, não chama LLM real e não publica no WordPress. Sua função é responder: o laboratório V4 está pronto para promoção ou deve bloquear?

O resultado atual é corretamente bloqueado:

```text
promocao_bloqueada
issues:
- recommended_required_policy_ratified
- collection_request_publicacao_real_resolvida
warning:
- gpt55_audit_recommended_before_promotion
```

## Política Proposta

Proponho ratificar a política operacional atual:

```text
recommended e required compartilham o mesmo gate mecânico por estágio.
```

A diferença é editorial:

- `recommended`: pendência prudencial. Não bloqueia etapas anteriores, mas bloqueia no estágio indicado por `required_before`.
- `required`: pendência forte. Também bloqueia no estágio indicado por `required_before`, com maior severidade editorial.

Consequência prática:

- Se `required_before=publicacao_real`, ambos bloqueiam publicação real.
- O sistema não deve transformar `recommended` em autorização silenciosa.
- Se Miguel quiser simplificar depois, podemos colapsar os dois status num único `pending`, mas isso deve ser nova decisão de fórum.

## Achados Incorporados

A auditoria adversarial da Fase 5 encontrou dois pontos médios e um menor:

1. Secret scan não pegava `sk-` genérico. Corrigido.
2. `decisions.*=true` podia ser virado sem evidência. Corrigido: agora exige `by`, `at` e `forum_doc`/`audit_doc`/`reason`.
3. `contract_tests_min` era contagem estática, não execução. Corrigido no nome: `contract_tests_defined_min`.

## Pendências Antes de Promoção

1. Miguel ratificar ou alterar a política `recommended`/`required`.
2. Resolver ou declarar com prudência a pendência do docket `USTR-2026-0331`.
3. Auditoria GPT 5.5 Pro, se Miguel quiser segunda leitura externa.
4. Só então avaliar promoção explícita para `Projeto Cafezinho Agentes/root/v4/`.

## Ponteiro Para Auditoria

Pacote:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_promocao_preflight_auditfix_20260709.tar.gz
```

O SHA deve ser conferido no momento do empacotamento final.

SHA final conferido:

```text
68f7d1eb9f025be2f19383368219e6b93856d444f3162c71e601adce315cd976
```

## Auditoria Fable — Auditfix Fase 5

**Status:** aprovado sem ressalvas.

Fable confirmou:

- SHA confere.
- `OK 78 contract tests`.
- `agentes_cli --strict` OK.
- `fluxo_cli --execute` OK.
- `promocao_cli --execute` continua sem promover nada.
- `promocao_real_executada=false`.
- `wordpress_real=false`.
- `external_call=false`.
- Secret scan agora pega `sk-` genérico.
- `decisions.*=true` exige evidência auditável.
- `collection_request` aberto para `publicacao_real` segue bloqueando promoção.

Conclusão do Fable:

```text
Fase 5 auditfix aprovada sem ressalvas.
O estado bloqueado atual é o estado correto do sistema.
```

## Alternativa Registrada Por Fable

Fable considera defensável ratificar a política atual:

```text
recommended e required compartilham o mesmo gate mecânico por estágio;
a diferença é severidade editorial declarada.
```

Mas registrou uma alternativa possível, caso Miguel queira dar "dentes" operacionais à diferença:

- `recommended`: pode ser liberado pelo editor-chefe com justificativa registrada no artefato.
- `required`: só libera quando a pendência factual estiver resolvida; sem atalho humano.

Esta alternativa ainda não foi aplicada no código. Está registrada para decisão editorial.

## Decisão Editorial Aplicada — USTR-2026-0331 — 2026-07-10

Miguel escolheu a alternativa editorial prudente para o caso `v4_real_001`:

```text
seguir sem depender do comentário escrito detalhado do docket USTR-2026-0331;
usar a transcrição oficial do USTR, o Federal Register e demais fontes auditadas;
não afirmar como fato auditado qualquer conteúdo do comentário escrito ausente;
se o docket for citado, declarar a limitação.
```

Resultado aplicado em `v4_labs`:

```text
collection_request.status=resolved
collection_request.required_before=none
resolved_by=Miguel
resolved_at=2026-07-10
resolution_type=editorial_prudence
```

Validação em extração limpa do pacote curado:

```text
OK 85 contract tests
agentes OK
fluxo OK
promocao_status=promocao_shadow_aprovada
promocao_ok=true
promocao_issues=[]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
wordpress_real=false
external_call=false
promocao_real_executada=false
```

Pacote:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_cured_20260710.tar.gz
SHA256: 580384b8898e3ee0f740271c1dd2dbf6256dec7dd05b20589f5c5f95a0576081
```
