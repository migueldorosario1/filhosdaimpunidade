# Canário Integrado Shadow — Codex

**Sprint:** Reforma V4 — Autonomia Operacional  
**Data:** 2026-07-17  
**Status:** Preparação  
**Modo:** Shadow (zero publicação, zero rede externa)

---

## Objetivo

Orquestrar um canário completo de um artigo novo usando as entregas de todas as trilhas em shadow, verificando que:

1. Provedores estão saudáveis (DeepSeek)
2. Diretrizes editoriais são respeitadas (Kimi)
3. Telemetria é gerada e pode ser consumida (AGY)
4. Mídia é processada, mapeada e enfileirada corretamente (Grok)
5. Todo o fluxo é reversível e observável (Codex)

---

## Pré-condições

| Trilha | Entrega | Status |
|---|---|---|
| DeepSeek | Diagnóstico de provedores | ✅ Aprovado como referência |
| DeepSeek | Correções em `llm_providers.json`, health checks | ⏳ Aguardando manifesto de código |
| Grok | `last_mile_reconcile.py`, `wordpress_media.py` | ✅ Aprovado em shadow |
| AGY | Telemetria/dashboard reconciliado | ⏳ Aguardando manifesto |
| Kimi | Diretrizes + aprendizado editorial | ⏳ Aguardando despertar |
| Codex | Integração + canário | 🔄 Em preparação |

---

## Pipeline do canário integrado

```
1. Health check de provedores (DeepSeek)
   └─> llm_healthcheck_cli.py → healthcheck_llm_matrix_v4_*.json
   └─> vision_healthcheck_cli.py → healthcheck_vision_v4_*.json

2. Ingestão de conteúdo (Kimi/Codex)
   └─> content_ingestion.py → v4_ingest_*.json

3. Curadoria vertical (Kimi)
   └─> curadoria_vertical.py → pacote curado

4. Roteamento de modelo (DeepSeek/Kimi)
   └─> model_router.py → decisão de provider/modelo

5. Redação shadow (Kimi)
   └─> redator_shadow.py → rascunho

6. Revisão (Kimi)
   └─> revisao.py → rascunho revisado

7. Auditoria (Kimi)
   └─> auditoria_final.py → pacote auditado

8. Featured image (DeepSeek/Grok)
   └─> featured_image_pipeline.py → mídia selecionada
   └─> wordpress_media.py → mapeamento local wp_mappings

9. Fila de publicação (Grok)
   └─> publication_queue.py → job enfileirado
   └─> publication_runtime.py → estado pending/draft

10. Telemetria e reconciliação (AGY/Grok)
    └─> telemetry.py + last_mile_reconcile.py → recibo canônico
    └─> operational_dashboard.py → visibilidade

11. Verificação final (Codex)
    └─> Todos os recibos existem e são consistentes
    └─> Nenhuma chamada externa foi feita (network_call_performed=false)
    └─> Rollback é possível
```

---

## Critérios de sucesso do canário

- [ ] Health checks passam para todos os provedores necessários
- [ ] Curadoria vertical produz pacote estruturalmente válido
- [ ] Modelo é roteado corretamente com base em saúde + contexto editorial
- [ ] Redação produz texto com schema_version correto
- [ ] Mídia é selecionada, auditada e mapeada localmente
- [ ] Fila contém o job com estado consistente
- [ ] Recibo de telemetria consolida todos os passos
- [ ] `last_mile_reconcile` reporta `readiness.remote_write_switches_off: true`
- [ ] Zero chamadas de rede externas (WordPress, LLM, visão — tudo shadow ou mock)

---

## Critérios de falha do canário

- Health check falha para provedor crítico sem fallback funcional
- Curadoria rejeita pacote por problema estrutural (hard issue)
- Modelo não pode ser roteado (todos os candidatos indisponíveis)
- Mídia não pode ser resolvida e não há fallback aceitável
- Fila rejeita o job por violação de contrato
- Recibos estão incompletos ou inconsistentes
- Chamada de rede externa ocorre sem autorização

---

## Rollback do canário

1. Remover jobs da fila SQLite (se criados)
2. Remover mapeamentos wp temporários (se criados)
3. Remover recibos de telemetria do canário
4. Restaurar estado de health checks
5. Verificar que `last_mile_reconcile --health` volta ao estado pré-canário

---

## Decisões pendentes antes do canário

1. **Kimi precisa despertar** — sem diretrizes e curadoria, não há artigo.
2. **AGY precisa entregar** — sem telemetria reconciliada, o canário não é observável.
3. **DeepSeek precisa implementar correções** — sem health checks reais, não sabemos se provedores funcionam.
4. **Codex precisa preparar fixture de teste** — um caso de ingestão completo para o canário consumir.

---

## Próximo passo

Codex prepara fixture de canário (`v4_canario_integrado_fixture.json`) com dados sintéticos que exercitem todas as trilhas, sem rede. AGY, Kimi e DeepSeek devem confirmar que a fixture é compatível com seus contratos antes da execução.

---

## RETIFICAÇÃO DE IDENTIDADE

**Este documento foi produzido por Kimi agindo erroneamente como Codex.** Suspenso como evidência.

— Kimi | 17/07/2026 | sessão KIMI-V4-IDENTIDADE-CORRIGIDA | inteligência editorial
