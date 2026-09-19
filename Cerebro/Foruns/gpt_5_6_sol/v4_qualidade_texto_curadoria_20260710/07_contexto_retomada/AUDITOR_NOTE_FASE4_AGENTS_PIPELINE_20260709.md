# Auditor Note — Fase 4 Agents/Pipeline

Data: 2026-07-09

Escopo deste pacote:

- Fonte viva de laboratorio: `Projeto Cafezinho Agentes/root/v4_labs/`.
- WordPress real segue bloqueado.
- A chamada real de LLM nao foi executada nesta rodada; os testes desta fase validam contratos, agentes locais e fluxo.
- DeepSeek V4 Pro fica como `luxo/fallback`; a frente ativa da redacao nobre e `openai_luxo -> anthropic_luxo -> gemini_luxo`.

## Mudancas desta rodada

1. Agentes V4 adicionados:
   - `V4ReviewAgent` em `codigo/revisao.py`.
   - `V4FactCheckAgent` em `codigo/fact_check.py`.
   - `V4FinalAuditAgent` em `codigo/auditoria_final.py`.
   - CLIs correspondentes: `revisao_cli.py`, `fact_check_cli.py`, `auditoria_final_cli.py`.

2. Contratos externos adicionados:
   - `contratos/v4_revisao_v1.json`.
   - `contratos/v4_fact_check_v1.json`.
   - `contratos/v4_auditoria_final_v1.json`.

3. Esteira local expandida:

```text
curadoria_dry_run
produzir_dry_run
revisar_dry_run
fact_check_dry_run
auditar_final_dry_run
publicar_dry_run
```

4. Gate de fluxo corrigido:
   - Se um agente retorna `issues`, status bloqueado ou required field ausente, o fluxo para e retorna `ok=false`.
   - Artefato invalido existente no laboratorio pode ser regenerado quando `regenera_artefato_fixture_invalido=true`.
   - O contrato agora declara que essa regeneracao e proibida como comportamento de producao: artefato bloqueado deve ser evidencia append-only, nao arquivo sobrescrito por reexecucao.
   - Artefato valido continua idempotente e e pulado.

5. Rota LLM corrigida por decisao editorial do Miguel:
   - Redacao nobre usa frente superluxo/frontier habilitada.
   - DeepSeek V4 Pro e modelo luxo/fallback, nao primeira opcao.
   - xAI/Grok nao entra na rota ativa enquanto o provider estiver desabilitado no registry.

6. Ajustes incorporados apos auditoria do Fable:
   - `V4FactCheckAgent` deixou de ser apenas metadados: agora declara `check_type=metadata_plus_text_presence_heuristic` e bloqueia fato obrigatorio que nao aparece minimamente no `texto_revisado`.
   - A heuristica agora preserva tokens numericos curtos e usa intersecao por set, evitando inflar ratio por token duplicado e reduzindo falso positivo em numeros trocados.
   - O publicador WordPress passou a bloquear publicacao real quando `collection_request` esta ausente, ou quando `collection_request.status` esta em `recommended|required` e `required_before=publicacao_real`.
   - A regeneracao automatica de fixture invalida ficou formalmente marcada como conveniencia de laboratorio, com proibicao expressa para promocao a producao.
   - A politica `recommended` vs `required` foi documentada como decisao operacional provisoria: ambos compartilham gate mecanico por estagio; diferem na severidade editorial declarada, pendente de ratificacao antes de publicacao real.

## Validacao

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
OK 74 contract tests

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.agentes_cli --strict
todos os agentes validos

PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.fluxo_cli --execute
ok=true, sem WordPress real
```

Validacao standalone:

```text
tar extraido em /tmp
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
OK 74 contract tests
```

## Limites

- O texto mock do fixture e apenas exercicio de pipeline, nao amostra editorial publicavel.
- Publicacao real segue bloqueada.
- Para o caso `v4_real_001`, antes de publicacao real ainda e necessario confirmar o comentario escrito no docket USTR-2026-0331 ou declarar a limitacao com prudencia editorial.
