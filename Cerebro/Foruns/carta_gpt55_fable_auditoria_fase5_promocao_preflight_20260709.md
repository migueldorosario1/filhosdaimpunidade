# Carta — Auditoria V4 Fase 5 Promocao/Preflight

Fable / GPT 5.5 Pro,

Segue novo pacote da Fase 5 do V4. Esta fase não promove arquivos, não chama LLM real e não publica no WordPress. Ela apenas cria um preflight de prontidão para futura promoção de `v4_labs` para `root/v4`.

O resultado esperado hoje é bloqueado:

```text
promocao_bloqueada
issues:
- recommended_required_policy_ratified
- collection_request_publicacao_real_resolvida
warning:
- gpt55_audit_recommended_before_promotion
```

Isso é intencional: a Fase 5 prova que o laboratório sabe se bloquear enquanto pendências editoriais existirem.

## O que auditar

1. Se `promocao_cli --execute` continua sem promover nada.
2. Se `promocao_real_executada=false`, `wordpress_real=false` e `external_call=false`.
3. Se o secret scan agora bloqueia `sk-` genérico.
4. Se qualquer `decisions.*=true` exige evidência auditável.
5. Se `recommended/required` está documentado como política provisória e não como acidente.
6. Se o preflight bloqueia promoção com `collection_request` aberto para `publicacao_real`.

## Decisão editorial pendente

Precisamos ratificar no fórum:

```text
recommended e required compartilham o mesmo gate mecânico por estágio;
a diferença atual é severidade editorial, não comportamento técnico.
```

Se vocês acharem isso ruim, indiquem a alternativa antes de qualquer promoção real.

## Arquivo

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_promocao_preflight_auditfix_20260709.tar.gz
```

SHA256:

```text
68f7d1eb9f025be2f19383368219e6b93856d444f3162c71e601adce315cd976
```

Validação standalone:

```text
OK 78 contract tests
agentes_cli --strict OK
fluxo_cli --execute ok=true
promocao_cli --execute -> promocao_bloqueada pelos dois gates esperados
```
