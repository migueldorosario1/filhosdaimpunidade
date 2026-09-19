---
name: forum-v4-incidente-rodada3-estado
description: Estado do fórum de incidente V4 (saúde/produção) pós-3ª rodada em 09/08/2026 13:45 BRT — GLM entregou §21 com 4 P0 alinhados ao §18.3; aguarda Gemini e decisão Miguel
metadata: 
  node_type: memory
  type: project
  originSessionId: 1a437e9e-f4cf-4489-8f4a-4625ae5d63ff
---

# Fórum de incidente V4 — estado pós-3ª rodada (09/08/2026 13:45 BRT)

**Fórum canônico:** `Cerebro/Foruns/forum_incidente_saude_producao_v4_20260809.md` (2435 linhas).
**Fórum irmão:** `Cerebro/Foruns/forum_reuniao_trabalho_novo_contrato_cafezinho_v4_20260809.md`.

**Why:** V4 com saúde amarela. 3ª rodada convocada por Miguel em 09/08 ~12:30 BRT restrita a **GLM, Grok, Claude, Gemini** (Qwen dispensado pra preservar crédito). Exigências: correção explícita dos erros da R2, P0 limitado a 4, revisão adversarial sanitizador Grok, recálculo métricas GLM, contrato WordPress viável Claude, auditoria independente Gemini, **NENHUM deploy**.

**How to apply:** próximas sugestões sobre V4 devem referenciar estado consolidado pós-R3. P0 único = §18.3 + trava mídia como parte do patch (consenso Grok+Claude+GLM). Aguardar Gemini antes de promoção a P1.

## P0 único consenso (4 ações — §18.3 + trava mídia)

| ID | Ação | Owner |
|---|---|---|
| **P0.1** Observabilidade fail-visible (`DEVNULL`→`capture`+sanitizador allowlist) | Grok autor + Gemini revisor |
| **P0.2** Recibo de falha sanitizado em `draft_events.failure_receipt` (JSONL em scratch p/ Regional CO/NE/Sul) + **trava forte contra sobrescrita de mídia** (`featured_media != 0` fail-closed) | Claude runtime + Gemini revisor |
| **P0.3** Dry-run Nacional + Geo via **runtime direto** (worker não propaga `V4_REDACTOR_DRY_RUN`, confirma Grok §19.0) | GLM escreve script em scratch |
| **P0.4** Decisão manual `264929` (one-shot Miguel+Claude); `264946` pending enquanto `featured_media=0` | Miguel decide, Claude executa |

## Recálculo conversão por `item_key` terminal (GLM 3ª rodada)

Janela 48h, `MAX(started_at)` por item_key:
- **Nacional:** 24/62 = **38.7%**
- **Geo:** 13/55 = **23.6%**
- **Ciência:** 1/14 = **7.1%**
- **Pooled:** 38/131 = **29.0%** (vs 25% R2 — soma bruta estava contaminada por retries)

**Ciência 30 rejeições `missing_geopolitical_technology_nexus`:** 15 únicas; **11/15 = ~73% falsos negativos** com claro nexus geopolítica-tech (OpenAI/Anthropic, Alibaba/Qwen, DeepSeek, BYD/Sinopec, SpaceX, NASA+China curbs). Gate é decisão editorial "opção A" — alterar exige Miguel.

## Correções GLM da R2 (tabela §21.0 do fórum)

- **5 CORRIGIR:** drift Regional CO/NE/Sul (não CO/Sul); conversão 25%→29%; Regional Sul G1 58%+ND Mais 42% (não "100% G1"); 5 contagens Nacional = partição correta; `repair_preflight_failed` são retries não itens distintos.
- **3 RETIRAR:** propor `POLICY['tecnologia']=168h` (já implementado); CAS via timestamp (não é CAS); "inserir primeiro NYC" (topologia invertida).
- **2 RECLASSIFICAR P0→P1:** reciclar 21.390 rejeições; migrar Regional CO/NE/Sul.

## Estado dos 4 participantes (3ª rodada)

- **Grok §19** (linhas 1604-2273): entregue. Sanitizador reescrito allowlist + classificador corrigido + worker não propaga `V4_REDACTOR_DRY_RUN` (L2381-2391) — dry-run deve invocar runtime direto.
- **Claude §20** (linhas 2278-2339): entregue. Máquina 3 camadas (PHP `register_post_meta`/escrita/leitura); separação 264929/264946; P0-C = 4 ações; APROVAR 7 / ALTERAR 5 / REJEITAR 8.
- **GLM §21** (linhas 2341-2435): entregue 09/08 13:45 BRT. P0-G = 4 ações alinhadas §18.3 + trava mídia. APROVAR 7 / ALTERAR 3 / REJEITAR 5.
- **Gemini §18.6:** pendente (auditoria independente do sanitizador Grok).

## Próximos passos

1. Aguardar entrega Gemini.
2. Decisão Miguel sobre P0 único (provável = §18.3 + trava mídia como parte do patch P0.2).
3. Sequência sugerida pós-decisão: P0.1+P0.2 (observabilidade + trava mídia, mesmo patch) → P0.3 (dry-run) → P0.4 (manual 264929).
4. Após 3 ciclos × 4 verticais sem falha opaca + recibo em toda falha, reavaliar P1 (reciclar 21.390, migrar Regional).

## Critério de encerramento (§10 + §18.9)

3 ciclos consecutivos por vertical sem falha opaca + toda falha com recibo classificado + nenhuma sobrescrita de mídia curada + nenhum `pending` com mídia por erro de reconciliação + Ciência com oferta útil documentada (depende decisão Miguel sobre gate nexus) + filas com idade controlada + título/corpo passam gates + fluxo exclusivamente em rascunho.

Ver [[acesso-sqlite-v4-nyc]] para método de diagnóstico contínuo.
