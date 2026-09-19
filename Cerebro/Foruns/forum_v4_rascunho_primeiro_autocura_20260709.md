# Forum V4 — Rascunho primeiro, relatorio e autocura

Data: 2026-07-09

## Contexto

Miguel apontou uma tendencia perigosa da engenharia da Trindade: transformar pendencias editoriais em bloqueios demais. A correcao de rumo fica registrada aqui.

O V4 nao deve cultivar cultura de bloqueio para rascunho editorial. A filosofia operacional passa a ser:

```text
rascunho -> relatorio transparente -> cura/autocura -> revisao humana -> promocao/publicacao final
```

## Retificacao de proveniencia

Esta filosofia **nao** foi diagnostico nem recomendacao do Fable. O Fable, nas auditorias anteriores, defendeu gates duros em varios pontos: evidencia para decisoes, preservacao de artefato bloqueado e gate de `collection_request` no publicador.

A politica rascunho-primeiro foi adotada a partir da orientacao do Miguel e pelos seus proprios meritos operacionais: nao perder material de trabalho e transformar pendencias em relatorio/cura.

Auditoria posterior do Fable aprovou a parte dry-run/laboratorio da filosofia, mas vetou o afrouxamento do caminho real de publicacao WordPress. Essa correcao foi incorporada: rascunho-primeiro vale integralmente para dry-run/lab; qualquer chamada real ao WordPress (`draft`, `pending` ou `publish`) mantem gates duros ate ratificacao explicita do forum.

Adendo posterior do Fable: a retificacao de autoria/proveniencia foi aceita. O ponto tecnico permanece: se Miguel decidir no futuro que rascunhos reais no WordPress podem subir com pendencias, essa decisao precisa ser ratificada no forum e acompanhada de ajustes explicitos (`pending` fora do modo tolerante, preflight alinhado e decision evidence). O pacote atual escolhe o caminho conservador: WordPress real continua duro; tolerancia rascunho-primeiro fica no dry-run/lab.

## Decisao

Rascunho editorial deve seguir sempre que for tecnicamente possivel, mesmo com pendencias. A pendencia entra como warning/relatorio, nao como perda de material.

Bloqueio duro fica reservado para:

- publicacao final;
- promocao para `root/v4`;
- acoes destrutivas;
- segredo ou credencial exposta;
- credencial ausente quando uma acao de rede real depende dela;
- risco juridico ou operacional irreversivel.

## Exemplos praticos

Sem imagem auditada:

```text
rascunho dry-run segue sem imagem;
warning registra a pendencia;
editor ou autocura resolve depois.
```

`collection_request` aberto:

```text
shadow/rascunho local segue com relatorio;
WordPress real/publicacao final/promocao esperam resolucao ou decisao editorial explicita.
```

`curadoria_id` ausente em dry-run:

```text
rascunho registra warning;
publicacao final exige rastreabilidade.
```

## Alteracoes codificadas no V4 labs

Fonte viva:

```text
Projeto Cafezinho Agentes/root/v4_labs/
```

Arquivos alterados/criados:

```text
contratos/v4_rascunho_primeiro_v1.json
contratos/v4_wordpress_publicador_v1.json
contratos/v4_fluxo_dry_run_v1.json
contratos/v4_promocao_preflight_v1.json
codigo/wordpress_publicador.py
codigo/fluxo.py
codigo/promocao.py
codigo/test_contracts.py
README_V4_LABS.md
AUDITOR_NOTE_FASE5_PROMOCAO_PREFLIGHT_20260709.md
```

Mudancas:

- publicador WordPress agora retorna `warnings` alem de `issues`;
- rascunho/dry-run sem `featured_media` vira `dry_run_with_warnings`, nao erro fatal;
- rascunho/dry-run sem `curadoria_id` vira warning;
- fluxo local segue sem midia auditada e registra `imagem_destacada_pendente`;
- qualquer chamada real ao WordPress preserva gates duros para `collection_request`, `curadoria_id`, `featured_media` e `manifesto`;
- preflight de promocao passa a usar status `promocao_pendente_de_cura`, nao `promocao_bloqueada`;
- novo contrato `v4_rascunho_primeiro_v1.json` define o vocabulario e as politicas.

## Validacao

Rodado em `Projeto Cafezinho Agentes/root/v4_labs/`:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
OK 81 contract tests

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.agentes_cli --strict
OK

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.fluxo_cli --execute
ok=true

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.promocao_cli --execute
status=promocao_pendente_de_cura
```

Pacote anterior substituido:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_20260709.tar.gz
SHA256: 82a1542e995b042f75521eb8cde8f535a2ed428653a06b5dadde1d2039c607f9
Tamanho: 165K
Motivo: auditoria Fable encontrou bypass no caminho real do WordPress.
```

Pacote novo de auditoria, com veto do Fable incorporado, gerado e validado em extracao limpa:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_auditfix_fable_20260709.tar.gz
SHA256: d46fdbe7b78e4f25930417166cc08f16da4dbf25afcfe3b030a3eee8fe24124c
Tamanho: 166K
Standalone: OK 81 contract tests; agentes OK; fluxo OK; promocao_pendente_de_cura.
```

## Ponto para Trindade

Ao auditar o V4, nao pedir mais bloqueio por padrao para rascunho. Preferir:

```text
warning claro;
relatorio curto;
recibo/telemetria;
proposta de autocura;
pedido de decisao humana quando necessario.
```

Bloqueio deve ser justificado como risco final ou irreversivel.

## Ratificacao — 2026-07-09

Miguel ratificou no chat:

```text
tudo bem. aceito sermos conservadores. vamos adiante.
```

Decisao registrada:

```text
rascunho-primeiro vale para dry-run/laboratorio;
qualquer chamada real ao WordPress (draft, pending, publish) mantem gates duros;
promocao para root/v4 mantem gates duros;
recommended e required seguem o mesmo gate mecanico por estagio, com severidade editorial diferente;
pending nao e draft tolerante.
```

Impacto no preflight:

```text
recommended_required_policy_ratified=true
decision_evidence aponta para este forum.
```

Permanece pendente:

```text
collection_request_publicacao_real_resolvida
```

Essa pendencia e do caso 261439 / docket USTR-2026-0331 e nao impede dry-run, redacao local ou continuidade do sprint. Ela impede apenas publicacao real/promocao final enquanto nao for resolvida ou tratada com decisao editorial explicita.

## Pacote Ratificado

Pacote novo apos ratificacao da politica conservadora:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_rascunho_primeiro_policy_ratified_20260709.tar.gz
SHA256: bdbccf94821f5f41ba18367f51694a893806cc79caa3c811cb1d1437d573bee1
Tamanho: 166K
```

Validacao em extracao limpa:

```text
OK 81 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
```

## Auditfix Fail-Closed — 2026-07-09

Auditoria Fable posterior aprovou a Fase 5 para dry-run/lab e encontrou uma fresta nao bloqueante para laboratorio, mas bloqueante antes de WordPress real:

```text
collection_request com status desconhecido ou required_before desconhecido passava em silencio.
```

Correcao incorporada:

```text
wordpress_publicador._collection_request_issues agora falha fechado;
promocao._collection_gates agora falha fechado;
valores conhecidos de required_before: shadow_redacao, redator_real_llm, publicacao_real, none;
valores conhecidos de status: none, resolved, recommended, required.
```

Novos testes:

```text
test_wordpress_publicador_collection_request_fail_closed_valores_desconhecidos
test_promocao_preflight_collection_request_fail_closed_valores_desconhecidos
```

Validacao local:

```text
OK 83 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
```

## Decisao editorial — Docket USTR-2026-0331 — 2026-07-10

Miguel escolheu a opcao 2 para a pendencia factual/editorial do caso `v4_real_001`:

```text
seguir com prudencia sem depender do comentario escrito detalhado do docket USTR-2026-0331;
usar como base a transcricao oficial do USTR, o Federal Register e demais fontes auditadas;
nao afirmar como fato auditado qualquer conteudo do comentario escrito USTR-2026-0331 enquanto ele nao estiver localizado;
se o docket for citado, declarar a limitacao com prudencia.
```

Efeito no V4 labs:

```text
collection_request.status="resolved";
collection_request.required_before="none";
resolved_by="Miguel";
resolved_at="2026-07-10";
resolution_type="editorial_prudence";
```

Isto cura a pendencia `collection_request_publicacao_real_resolvida` sem fingir que o documento escrito foi encontrado. A decisao e editorial: a materia pode seguir porque a tese principal esta sustentada por transcricao oficial e documentos oficiais ja auditados; o documento escrito ausente nao deve ser usado como pilar factual.

Validacao apos a cura:

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

Pacote curado:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_cured_20260710.tar.gz
SHA256: 580384b8898e3ee0f740271c1dd2dbf6256dec7dd05b20589f5c5f95a0576081
Tamanho: 168K
```

## Fechamento Mecanico Fase 5 — Fable — 2026-07-10

Carta:

```text
Cerebro/Foruns/carta_fable_adendo_final_fase5_typefix_20260710.md
```

Veredito registrado:

```text
F5.2 RESOLVIDO E VERIFICADO.
A parte mecanica da Fase 5 esta formalmente encerrada pela auditoria Fable.
Pendencia remanescente e exclusivamente editorial/factual: collection_request_publicacao_real_resolvida.
```

Contrato atualizado:

```text
decisions.fable_fase5_mechanical_closed=true
decision_evidence.fable_fase5_mechanical_closed.audit_doc=Cerebro/Foruns/carta_fable_adendo_final_fase5_typefix_20260710.md
```

Condicoes vigentes:

```text
dry-run/lab liberado;
WordPress real continua fechado;
promocao para root/v4 continua fechada;
resolver/tratar docket USTR-2026-0331 antes de publicacao real/promocao;
rodar 2-3 casos reais adicionais em dry-run antes de promocao;
human_promotion_authorized so depois de decisao explicita.
```

Pacote vigente com fechamento mecanico Fase 5 registrado:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_mechanical_closed_20260710.tar.gz
SHA256: 0e509a1c679a7b0dd935ef7eb1dd707af86452fd9f7ca2a3f23b4bbd6cd19e18
Tamanho: 167K
```

Validacao em extracao limpa:

```text
OK 85 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
```

## Confirmacao Final do Pacote Mechanical Closed — Fable — 2026-07-10

Registro curto, sem nova carta formal:

```text
Fable verificou o pacote v4_labs_fase5_mechanical_closed_20260710.tar.gz
SHA256: 0e509a1c679a7b0dd935ef7eb1dd707af86452fd9f7ca2a3f23b4bbd6cd19e18
Data: 2026-07-10
Resultado: incorporacao fiel, escopo minimo, 85 testes executados, evidencia validada pelo gate.
```

Confirmacao de estado:

```text
nada mecanico pendente;
caminho critico agora e editorial/factual;
resolver ou declarar com prudencia o docket USTR-2026-0331;
registrar a cura com by/at/documento/reason;
depois rodar 2-3 casos reais adicionais em dry-run.
```

Pacote novo F5.2, substitui o pacote fail-closed anterior:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_typefix_20260709.tar.gz
SHA256: 9f7954dfe07ae148d2e3f6068372e5bc4b7c0769d65b0020d3415534b901db65
Tamanho: 167K
```

Validacao em extracao limpa:

```text
OK 85 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
```

Pacote novo, substitui o pacote ratificado anterior:

```text
Projeto Cafezinho Agentes/root/v4_labs_fase5_collection_failclosed_20260709.tar.gz
SHA256: 2041b7e3f582af11a22b638a20e9ac2f21ac6b4744f216ffa22aa56f268d2c9d
Tamanho: 167K
```

Validacao em extracao limpa:

```text
OK 83 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
promocao_warnings=["gpt55_audit_recommended_before_promotion"]
```

## Auditfix F5.2 — Tipos Invalidos em Collection Request

Auditoria Fable do pacote fail-closed encontrou achado residual menor:

```text
collection_request.status ou required_before com valor nao-string causava TypeError em vez de issue auditavel.
```

Correcao incorporada:

```text
wordpress_publicador valida isinstance(status, str) e isinstance(required_before, str);
promocao valida o mesmo antes de testar pertencimento;
valor malformado vira issue, nao stack trace;
preflight continua rodando mesmo se houver artefato ruim em dados/.
```

Novos testes:

```text
test_wordpress_publicador_collection_request_nao_string_vira_issue
test_promocao_preflight_collection_request_nao_string_vira_issue
```

Validacao local:

```text
OK 85 contract tests
agentes OK
fluxo OK
promocao_status=promocao_pendente_de_cura
promocao_issues=["collection_request_publicacao_real_resolvida"]
```
