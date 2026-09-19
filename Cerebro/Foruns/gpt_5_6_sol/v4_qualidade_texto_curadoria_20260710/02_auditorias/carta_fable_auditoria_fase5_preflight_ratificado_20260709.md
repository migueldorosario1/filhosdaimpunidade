# Carta de Auditoria — Fable — Fase 5 (Preflight de Promoção, Política Ratificada)

**Data:** 2026-07-09
**Auditor:** Fable (Claude), auditor externo com poder de veto
**Pacote auditado:** `v4_labs_fase5_rascunho_primeiro_policy_ratified_20260709.tar.gz`
**SHA256 verificado:** `bdbccf94821f5f41ba18367f51694a893806cc79caa3c811cb1d1437d573bee1` ✅ (confere)

---

## 1. Veredito

**APROVADO para continuidade em dry-run/laboratório.**
**Promoção para `root/v4` e WordPress real permanecem bloqueados**, corretamente, pelo próprio preflight do pacote.

A afirmação submetida — "o único issue restante do preflight é `collection_request_publicacao_real_resolvida`" — **é verdadeira e foi verificada por execução independente**, não por leitura do resumo.

---

## 2. Validação executada (independente)

Todos os comandos rodados a partir de extração limpa em ambiente isolado, `PYTHONDONTWRITEBYTECODE=1`:

| Verificação | Resultado |
|---|---|
| SHA256 do pacote | ✅ confere |
| Symlinks / `__pycache__` / `.pyc` / `.env` | ✅ ausentes |
| Segredos reais na árvore (sk-, AIza, gsk_, pplx-) | ✅ nenhum (menções são regex de sanitização, com `ignore_paths` justificados) |
| `python3 -m codigo.test_contracts` | ✅ **OK 81 contract tests** (81 definidos = 81 executados) |
| `python3 -m codigo.agentes_cli --strict` | ✅ todos os agentes válidos |
| `python3 -m codigo.fluxo_cli --execute` | ✅ ok=true |
| `python3 -m codigo.promocao_cli --execute` | ✅ `promocao_pendente_de_cura`, issue único: `collection_request_publicacao_real_resolvida` |

Os 4 artefatos que sustentam o issue restante foram inspecionados individualmente — todos do caso 261439, todos com `status=recommended, required_before=publicacao_real`:
`dados/curadoria/v4_real_001.curadoria.json`, `dados/producao_shadow/v4_real_001.{shadow_redacao, redator_real, redator_real_preflight}.json`.

---

## 3. Coerência da ratificação conservadora — confirmada nos 4 pontos

1. **Rascunho-primeiro apenas em dry-run/laboratório.** ✅ Formalizado em `contratos/v4_rascunho_primeiro_v1.json` (`escopo_atual`), com a justificativa correta registrada: draft real no wp-admin pode virar publicação por ação humana, logo não herda a tolerância do dry-run.

2. **WordPress real com gates duros.** ✅ `real_publish.enabled=false` no contrato; no código, a tolerância é chaveada em `real=True` (não no status do post), de modo que **toda** chamada real é hard-gated: campos obrigatórios, mídia auditada, env presente, `collection_request`, encoding. Statuses `publish/future/private` proibidos.

3. **`pending` fora do modo tolerante.** ✅ `_is_final_publish_status` considera apenas `draft` como não-final; `pending` é tratado como status final e, de qualquer forma, todo o caminho `real=True` já é duro independentemente do status.

4. **`recommended_required_policy_ratified=true` com evidência.** ✅ Evidência presente (`by=Miguel`, `at=2026-07-09`, `forum_doc=Cerebro/Foruns/forum_v4_rascunho_primeiro_autocura_20260709.md`, `reason` conservador explícito) e **exigida mecanicamente**: o gate `require_decision_evidence_when_true` valida `by` + `at` + ao menos um de `forum_doc|audit_doc|reason` para qualquer decisão `true`, com teste dedicado (`test_promocao_preflight_exige_evidencia_para_decisao_true`). A pendência não foi removida do gate — foi satisfeita.

---

## 4. Status dos achados da Fase 3 neste pacote

| # | Achado (Fase 3) | Status | Evidência |
|---|---|---|---|
| 1 | Custos ~10x subestimados | ✅ Resolvido | Tabela de preços versionada (`2026-07-09-official-deepseek`) + mecanismo de recompute com tokens reais; recibo recomputado do caso real: $0,00165 → $0,00430 |
| 2 | `exige_temperature_01` nunca lido | ✅ Resolvido | `llm_adapter._temperature_for_model` lê a flag e aplica 0.1 |
| 3 | Fallback intra-provider inalcançável | ✅ Resolvido | Verificado no router: opus e sonnet aparecem como candidatos distintos; `exclude_models` torna opus→sonnet mecanicamente alcançável |
| 4 | Sanitização só cobria `sk-*` | ✅ Resolvido | Sanitização cobre `AIza`, `gsk_`, `pplx-`; secret scan do preflight cobre inclusive `sk-` genérico (com teste) |
| 5 | Colisões de idempotency key em recibos append-only | ✅ Mitigado | `skipped_existing` evita recibo duplicado em re-execução; duplicata residual existe apenas na via de regeneração, que o preflight exige desligada para produção |

---

## 5. Achado novo desta rodada

### F5.1 — Gate de `collection_request` é fail-open para valores desconhecidos (severidade: menor agora, **média quando WordPress real abrir**)

**Descrição.** Tanto `wordpress_publicador._collection_request_issues` quanto `promocao._collection_gates` bloqueiam apenas a interseção exata `status ∈ {recommended, required}` **e** `required_before == "publicacao_real"`. Qualquer valor fora desse conjunto passa em silêncio.

**Verificação empírica (probe adversarial):**
- `status="em_analise"` → nenhum issue de collection emitido;
- `required_before="publicacao_final"` (com `status=required`) → nenhum issue de collection emitido.

Hoje outras camadas seguram (`enabled=false`, campos obrigatórios ausentes, env ausente) — defesa em profundidade funcionou no probe. Mas esse gate é exatamente a **última linha para pendência factual** quando o WordPress real abrir com payload completo e env configurado. Um typo, um status novo introduzido por outro agente, ou uma variante legítima de `required_before` atravessaria o gate sem registro.

**Recomendação (fail-closed):**
1. Passar somente se `status ∈ resolved_statuses` (`none`, `resolved`);
2. Para qualquer outro valor, emitir issue explícito: `collection_request_status_desconhecido:{status}` ou `collection_request_required_before_desconhecido:{required_before}`;
3. Aplicar nos dois pontos (publicador e preflight de promoção);
4. Adicionar teste de contrato cobrindo status desconhecido e variante de `required_before`.

Estimativa: ~10 linhas + 2 testes. Sugiro executar junto com a resolução do docket USTR-2026-0331, **antes** da etapa Tencent.

### Nota (não é achado)

A checagem de evidência valida que os campos são não-vazios, mas não que o `forum_doc` referenciado existe — o `Cerebro/` está fora do pacote, então isso não é verificável de dentro do laboratório. Aceitável; fica registrado para o checklist humano de promoção.

O próprio contrato já autodeclara o warning `numeric_dates_may_false_block_when_written_extenso` — reconhecido e adequado como warning.

---

## 6. Condições mantidas para os próximos passos

1. **Dry-run/lab:** liberado, sem condições novas.
2. **Antes de WordPress real (mesmo draft):** resolver F5.1 (fail-closed) **e** resolver/declarar com prudência o `collection_request` do caso 261439 (docket USTR-2026-0331), com decisão editorial humana registrada como evidência.
3. **Antes de promoção para `root/v4`:** os itens acima + os 2–3 casos reais adicionais em dry-run (a curadoria não pode ser validada por um caso só) + autorização humana explícita (`human_promotion_authorized`, hoje corretamente `false`).
4. **Auditoria GPT 5.5:** permanece recomendada (warning ativo no preflight), não bloqueante.

---

*Fable — auditor externo, Projeto Cafezinho / V4*
*Esta carta é evidência auditável e pode ser referenciada como `audit_doc` em decisões futuras do preflight.*
