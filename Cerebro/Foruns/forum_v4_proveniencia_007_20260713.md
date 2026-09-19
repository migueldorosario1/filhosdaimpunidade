# V4 — proveniência V2 do 007 e novo gate humano

Data: 2026-07-13 13:21 BRT  
Agente: Codex  
Escopo: laboratório local `Projeto Cafezinho Agentes/root/v4_labs/`

## Resultado

A proveniência cultural do `v4_real_007` foi normalizada de forma append-only. Dos 14 claims canônicos, os oito usados pelo template shadow e pelo Fact-check V2 agora possuem snapshot local, SHA-256, locator exato e metadados explícitos. A coleta anterior permaneceu imutável.

```text
coleta anterior: dados/auditado/v4_real_007.coleta_publica_20260711.json
sha256: b603e5680b47afb6ec5fec08acd84ee6892cdc47f7c8a981e02d0b5d7c7db411

coleta normalizada: dados/auditado/v4_real_007.coleta_publica_v2_20260713.json
sha256: 97afdacc89ae7a3268a93e23236937f72326b87d21807dd2ed03432fd540e91a
semantic_review_performed: false
```

O contrato append-only `contratos/v4_fluxo_dry_run_v3.json` materializou a nova curadoria:

```text
run_id: run_ea5eb32931ca37e4efef
curadoria: dados/curadoria/runs/run_ea5eb32931ca37e4efef/v4_real_007.curadoria.json
curadoria sha256: 38cf164a09529e235f76981104c77f86bdf308d55b8fa072c01c80e4b2e605c2
estado sha256: 96b17b24b50b0971ad3102233da92a279ba38cc747700c2a18ad47d01433f742
estado_editorial: rascunho_revisao_humana
semantic_evaluation_complete: false
```

## Gate preservado

A produção parou em `gate_shadow_selection_ausente`, com warning `avaliacao_semantica_humana_pendente`. A última seleção do 007 aponta para a canônica `run_f34...`; o shadow `run_ac46010ba6a46394778b` é histórico e não foi reaproveitado.

O binding 8/8 e o Fact-check V2 foram exercitados somente como prova contratada: `issues=[]`, parecer inconclusivo apenas pelos oito segmentos interpretativos. Nenhum novo input bound, shadow, revisão ou fact-check foi persistido para `run_ea5...`.

## Validação

```text
suite: OK 272 contract tests
agentes strict: 11/11 válidos
recibo: dados/testes/suite_receipt_ad870d471b1e5f166e02ba9c45a3defd62000fd2644d852fbac1f615f67e0d85.json
tree_sha256: ad870d471b1e5f166e02ba9c45a3defd62000fd2644d852fbac1f615f67e0d85
manifest_count: 599
no_pycache: ok
no_pyc: ok
```

O preflight V3 atual permaneceu corretamente em `promocao_pendente_de_cura`. Bloqueios: ausência de autorização humana de promoção, pendências de coleta por estágio, semântica não concluída, etapas obrigatórias ausentes e linhagem shadow atual incompleta. `wordpress_real=false` e `promocao_real_executada=false`.

## Próximo passo

É necessário um novo ateste humano ligado ao caminho e ao SHA-256 da curadoria `run_ea5eb32931ca37e4efef`. Só depois devem ser gerados, de forma append-only, o input bound, o shadow, a revisão e o fact-check.

Não houve publicação, promoção para `root/v4`, email, contato com fonte, chamada real ao WordPress, aprovação semântica ou ativação de autoaperfeiçoamento.

