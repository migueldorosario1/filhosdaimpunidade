# V4 Labs — laboratorio de testes

Data: 2026-07-09

Este diretorio e o laboratorio V4 dentro do ecossistema operacional do Cafezinho:

```text
Projeto Cafezinho Agentes/root/v4_labs/
```

Ele existe para testar o V4 antes de migrar arquivos auditados para o diretorio final:

```text
Projeto Cafezinho Agentes/root/v4/
```

## Regra

```text
v4_labs = testes, shadow, dry-run, auditoria tecnica local.
v4      = somente arquivos finais auditados e prontos para producao.
```

## Filosofia operacional: rascunho primeiro

O V4 deve evitar cultura de bloqueio em rascunho editorial. Quando uma pendencia nao destruir rastreabilidade nem criar risco irreversivel, o comportamento esperado e:

```text
registrar pendencia -> gerar relatorio -> seguir com rascunho -> permitir cura/autocura.
```

Exemplos:

```text
sem imagem auditada       -> rascunho segue sem imagem, com warning;
collection_request aberto -> rascunho/shadow segue, publicacao final e promocao aguardam cura;
curadoria_id ausente      -> rascunho dry-run registra warning, publicacao final exige rastreabilidade;
```

Bloqueio duro fica reservado para promocao ao diretorio final, qualquer chamada real ao WordPress ate ratificacao explicita do forum, publicacao final, credenciais/segredos, acoes destrutivas ou risco juridico/operacional irreversivel.

Observacao apos auditoria Fable: rascunho-primeiro vale integralmente para dry-run/laboratorio. Draft ou pending real no WordPress continuam com gates duros, porque podem ir ao ar por acao humana no wp-admin.

## Conteudo atual

```text
contratos/     copia de laboratorio dos contratos/diretrizes V4
codigo/        copia de laboratorio do codigo Python V4
dados/         copia de laboratorio dos dados em camadas V4
config/         copia de laboratorio da config LLM usada pelos testes
```

Status operacional apos limpeza de 2026-07-09:

```text
Este diretorio e a unica fonte ativa de laboratorio do V4.
```

As copias provisorias que estavam soltas na raiz do workspace foram movidas para:

```text
Backups/v4_root_provisorio_pre_labs_unico_20260709_021707/
```

Esse backup e somente recuperacao/rollback, nao fonte viva.

## Config LLM

O codigo usa caminhos locais do pacote:

```text
config/llm_providers.json
config/llm_ratings.json
config/llm_context_routes.json
```

Nao ha shim de compatibilidade para caminho externo antigo dentro do pacote. A copia local em `config/` torna o pacote exportado executavel de forma standalone.

Convencao de arquivos de curadoria:

```text
dados/curadoria/*.curadoria.json
```

A variante duplicada com underscore foi removida do laboratorio e arquivada fora do pacote.

## Validacao

Rodar dentro de `v4_labs`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
```

Resultado esperado:

```text
OK 88 contract tests
```

## Status atual

O caso `v4_real_001` ja possui coleta primaria USTR/Federal Register e transcricao oficial USTR Day 2 suficiente para liberar o preflight de redator real:

```text
dados/auditado/v4_real_001.coleta_primaria_ustr.json
dados/producao_shadow/v4_real_001.redator_real_preflight.json
```

Estado dos gates:

```text
collection_request do caso USTR foi curado por decisao editorial de prudencia;
preflight de promocao esta aprovado em shadow;
WordPress real continua desabilitado;
promocao real nao executada;
auditoria GPT 5.5 segue como warning recomendado, nao issue.
```

Observacao factual:

```text
A audiencia USTR ocorreu em 6 e 7 de julho de 2026. A transcricao oficial do Dia 2 registra Flavio Bolsonaro no Painel 8 em 7 de julho de 2026. Miguel decidiu seguir com prudencia sem depender do comentario escrito USTR-2026-0331: a materia deve usar a transcricao oficial, o Federal Register e fontes auditadas, declarando a limitacao se o docket for citado.
```

Resultado das chamadas reais em laboratorio:

```text
dados/producao_shadow/v4_real_001.redator_real_attempts.jsonl
dados/producao_shadow/v4_real_001.redator_real.json

Achados:
- o healthcheck local anterior nao detectava billing/credito;
- Gemini passou no smoke real depois da recarga;
- Gemini exigiu thinking_budget=0 para nao consumir o orcamento em raciocinio invisivel;
- o gate real_output_quality bloqueou saidas curtas/interrompidas;
- a chamada final com gemini/gemini-3.5-flash gerou texto real completo.
- A redacao V4 usa frente superluxo/frontier habilitada por rota externa (`openai_luxo`, `anthropic_luxo`, `gemini_luxo`); DeepSeek V4 Pro fica como luxo/fallback (`deepseek_luxo` -> `deepseek-v4-pro`), sem hardcode em Python. xAI/Grok segue fora da rota ativa enquanto o provider estiver desabilitado.
- O redator real agora faz fallback auditavel por modelo da rota externa, preservando fallback intra-provider.
- O fluxo local ganhou agentes V4 de revisao, fact-check e auditoria final: `curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run`.
- Artefato gerado com status bloqueado ou campo requerido ausente agora interrompe o fluxo; o pipeline nao mascara mais saida invalida como sucesso.
- A regeneracao automatica de artefato invalido e permitida apenas como conveniencia de laboratorio; o contrato de promocao para producao exige preservar bloqueios como evidencia append-only.
- O fact-check local agora declara `check_type=metadata_plus_text_presence_heuristic` e verifica presenca textual minima dos fatos obrigatorios no `texto_revisado`; isto nao substitui fact-check LLM/humano.
- A heuristica de fact-check preserva tokens numericos curtos (`25`, `91`, `301`) e exige que numeros do fato travado aparecam no texto, para reduzir falso positivo em percentual/docket/citacao.
- O publicador WordPress registra `collection_request` no rascunho dry-run e o trata como pendencia de cura; coleta pendente ou ausente segura qualquer chamada real ao WordPress ate ratificacao explicita, alem de publicacao final/promocao.
- O gate de `collection_request` agora falha fechado: status ou `required_before` desconhecido bloqueia publicador real e promocao, em vez de passar em silencio.
- Valores nao-string em `collection_request.status` ou `collection_request.required_before` viram issue auditavel, nao stack trace.
- Fase 5 adicionou preflight de promocao: `codigo/promocao.py` + `contratos/v4_promocao_preflight_v1.json`. O preflight nao promove arquivos; ele marca a promocao como pendente de cura enquanto houver pendencias editoriais reais.
- Estado atual do preflight: `promocao_shadow_aprovada`, `issues=[]`, warning `gpt55_audit_recommended_before_promotion`. Isto ainda nao promove para `root/v4`, porque promocao real exige autorizacao humana explicita.
- Auditfix da Fase 5: secret scan cobre `sk-` generico, e qualquer `decisions.*=true` precisa vir acompanhado de evidencia (`by`, `at` e `forum_doc`/`audit_doc`/`reason`). O check de testes foi renomeado para `contract_tests_defined_min`, deixando claro que ali e contagem estatica, nao execucao da suite.
- Toda execucao do redator real com `execute=True` grava recibo JSONL de telemetria sem incluir prompt nem texto completo, com tokens reais, custo, temperatura, max_tokens e thinking_budget.
- Smoke real controlado com DeepSeek V4 Pro validou o fallback: `deepseek/deepseek-v4-pro`, 5120 caracteres, `issues=[]`, `temperature=0.1`, `telemetry_receipt.ok=true`. A rota normal de redacao agora prioriza frontier/superluxo antes de acionar DeepSeek.
- Custo do recibo passou a usar tokens reais da API; recibos antigos com tabela anterior foram reconciliados via `agent_data/v4/receipts/recomputed/`.

external_call_executed=true nas tentativas;
wordpress_real=false em todas;
status final atual: redator_real_llm_pronto;
texto_real atual: 5120 caracteres;
issues: [].
```

## Status Fase 6 — multi-caso dry-run

Em 2026-07-10 o laboratorio rodou tres casos adicionais para testar generalizacao alem do caso `v4_real_001`:

```text
v4_real_002 — Jason Miller / documentos judiciais / politica internacional
v4_real_003 — IBGE PIM abril 2026 / industria mensal
v4_real_004 — IBGE PIA-Produto 2024 / estrutura produtiva
```

Resultado:

```text
3/3 ok=true
curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run
issues=[]
warnings apenas em publicar_dry_run por imagem auditada ausente
wordpress_real=false
external_publish=false
```

Achados corrigidos durante a rodada:

```text
curadoria nao deve confundir "industria" com "USTR";
tese de pauta economica nao deve herdar linguagem de pressao externa;
produtor mock precisa receber fatos travados para o fact-check validar presenca textual.
```

Relatorio:

```text
dados/promocao/v4_labs_multi_case_dry_run_20260710.json
```

## Limite

Nada aqui deve ser tratado como final auditado. A promocao para `../v4/` exige auditoria e decisao explicita.
