# Auditor Note — Fase 3 DeepSeek/Fallback/Telemetria

Data: 2026-07-09

Escopo deste pacote:

- Fonte viva de laboratorio: `Projeto Cafezinho Agentes/root/v4_labs/`.
- Este pacote nao contem chaves, `.env`, `__pycache__` ou `.pyc`.
- WordPress real segue bloqueado; todos os artefatos continuam em laboratorio.

## Mudancas da rodada

1. A redacao V4 preserva frente superluxo/frontier habilitada e mantem DeepSeek V4 Pro como luxo/fallback por configuracao externa:
   - `config/llm_providers.json`: `deepseek_luxo -> deepseek-v4-pro`.
   - `config/llm_ratings.json`: `deepseek-v4-pro` liberado para `redacao`, `revisao`, `auditoria`, `fact_check`, `perifericos_editoriais` e `curadoria`.
   - `contratos/v4_rotas_llm_limpas_v1.json`: `openai_luxo`, `anthropic_luxo` e `gemini_luxo` ficam na frente; `deepseek_luxo` entra no fim como fallback. `xai_luxo` nao entra na rota ativa enquanto o provider estiver desabilitado.
   - O codigo operacional nao contem `deepseek-v4-pro` hardcoded.

2. O adapter real passou a respeitar a ordem editorial da rota externa:
   - No modo `real`, a selecao usa a ordem do contrato de rota.
   - Ranking/custo continuam disponiveis para dashboard e exploracao, mas a chamada real nao reordena contra a decisao editorial.
   - `deepseek-v4-pro` obedece `flags.exige_temperature_01=true`; a chamada real usa e registra `temperature=0.1`.

3. O redator real ganhou fallback auditavel:
   - Falha real de provider/model agora preserva provider/model via `V4LLMRealCallError`.
   - `V4RealRedator.call_real()` tenta o proximo modelo da rota quando houver erro ou saida incompleta, ate `fallback.max_attempts`.
   - Fallback intra-provider e preservado: se `claude-opus` falhar, `claude-sonnet` ainda e alcancavel.
   - Cada tentativa entra em `fallback_attempts`.

4. A chamada real agora grava recibo JSONL de telemetria:
   - Recibo em `agent_data/v4/receipts/`.
   - O recibo registra provider, modelo, tier, tokens reais quando a API retorna usage, custo estimado, status, tentativas, temperatura, max_tokens, thinking_budget e tamanho do texto.
   - O recibo nao grava prompt nem texto completo.

5. Correcao de custo:
   - `V4Pricing.estimate_by_tokens()` calcula custo por tokens reais.
   - `deepseek-v4-pro` atualizado para a pagina oficial DeepSeek de 2026-07-09: input `0.435`, output `0.87` por 1M tokens.
   - Recibos antigos com versao de pricing anterior sao reconciliados por `recompute_costs` em trilha append-only, sem editar recibo original.

6. Esteira V4 local expandida:
   - Novos contratos: `v4_revisao_v1.json`, `v4_fact_check_v1.json`, `v4_auditoria_final_v1.json`.
   - Novos agentes: `V4ReviewAgent`, `V4FactCheckAgent`, `V4FinalAuditAgent`.
   - O fluxo dry-run agora passa por `curadoria -> producao -> revisao -> fact_check -> auditado_final -> publicado_dry_run`.
   - Saida bloqueada ou required field ausente interrompe o fluxo; artefato invalido nao pode mais aparecer como sucesso.

## Validacao

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m codigo.test_contracts
OK 69 contract tests na Fase 3; o estado atual do pacote esta no README e na nota da Fase 4.
```

Smoke real controlado do fallback DeepSeek, sem WordPress:

```text
provider: deepseek
model: deepseek-v4-pro
status: redator_real_llm_pronto
texto_real: 5120 caracteres
tokens_in: 5206
tokens_out: 1967
cost_usd_estimated: 0.0039759
pricing_table_version: 2026-07-09-official-deepseek
temperature: 0.1
issues: []
telemetry_receipt.ok: true
```

## Gates ainda fechados

- `wordpress_real=false` em todos os artefatos.
- Publicacao real continua bloqueada pelo contrato do publicador.
- `collection_request` do caso 261439 continua bloqueando `publicacao_real` ate confirmar o comentario escrito no docket USTR-2026-0331 ou declarar a limitacao com prudencia editorial.
