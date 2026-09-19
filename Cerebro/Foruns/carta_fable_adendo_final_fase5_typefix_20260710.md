# Carta de Auditoria — Fable — Adendo Final Fase 5 (F5.2 Fechado)

**Data:** 2026-07-10
**Auditor:** Fable (Claude), auditor externo com poder de veto
**Pacote auditado:** `v4_labs_fase5_collection_typefix_20260709.tar.gz`
**SHA256 verificado:** `9f7954dfe07ae148d2e3f6068372e5bc4b7c0769d65b0020d3415534b901db65` ✅ (confere)
**Referência:** fecha o achado F5.2 da `carta_fable_adendo_fase5_failclosed_20260709.md`

---

## 1. Veredito

**F5.2 RESOLVIDO E VERIFICADO.**
**A parte mecânica da Fase 5 está formalmente encerrada pela auditoria Fable.**
Pendência remanescente é exclusivamente editorial/factual: `collection_request_publicacao_real_resolvida` (caso 261439 / docket USTR-2026-0331), a resolver por decisão humana com evidência.

---

## 2. Validação executada (independente)

| Verificação | Resultado |
|---|---|
| SHA256 | ✅ confere com o declarado no fórum |
| Higiene (symlinks, `__pycache__`, `.pyc`, `.env`, segredos) | ✅ limpa |
| Diff vs. pacote `failclosed` auditado | ✅ cirúrgico: `wordpress_publicador.py`, `promocao.py`, `test_contracts.py`, contrato de preflight (min 83→85) + 4 metadados esperados (README, auditor note, `eventos.jsonl`, output do preflight) |
| `test_contracts` | ✅ **OK 85 contract tests** (85 definidos = 85 executados) |
| `agentes_cli --strict` | ✅ |
| `fluxo_cli --execute` | ✅ |
| `promocao_cli --execute` | ✅ `promocao_pendente_de_cura`; issue único `collection_request_publicacao_real_resolvida` |

## 3. Verificação adversarial do F5.2

Simulação de estado futuro no publicador (`enabled=true`, env presente, POST instrumentado):

| Caso | Resultado |
|---|---|
| `required_before=["publicacao_real"]` (lista) | ✅ issue `collection_request_invalido_para_publicacao_real`, tentativa `blocked` — antes crashava com TypeError |
| `status=["required"]`, `status=None`, `status=1`, `required_before={dict}` | ✅ todos produzem o mesmo issue auditável, sem exceção |
| Baselines F5.1 (`em_analise`, `publicacao_final`, `recommended/publicacao_real`) | ✅ sem regressão |
| POSTs disparados em todos os casos | **0** |

Preflight de promoção: artefato malformado (`status` não-string) injetado em `dados/` — o preflight **roda até o fim** e reporta `collection_request_valores_conhecidos → issue` com o caminho do arquivo ofensor. Antes, um único arquivo ruim derrubava o relatório inteiro com TypeError.

Os dois testes novos (`test_wordpress_publicador_collection_request_nao_string_vira_issue`, `test_promocao_preflight_collection_request_nao_string_vira_issue`) seguem o padrão forte dos anteriores, assertando inclusive que o POST nunca é atingido.

## 4. Observação registrada (não é achado)

No preflight, o type-check agora precede a tolerância de `none/resolved`: um artefato com `required_before` ausente (None) é marcado inválido mesmo com `status="none"`. Comportamento mais estrito que o anterior, na direção fail-closed, coerente com o vocabulário do projeto que exige `"none"` explícito. Toda a árvore atual usa a string; o check rodou com count 0. Registrado como intencional.

Permanece a nota de manutenção do adendo anterior: vocabulário de statuses/estágios hardcoded em `promocao.py` vs. lido do contrato no publicador — melhoria opcional futura (fonte única de vocabulário), sem urgência.

---

## 5. Estado consolidado — Fase 5 encerrada mecanicamente

Histórico de achados da Fase 5, todos fechados:

| Achado | Severidade | Status |
|---|---|---|
| Bypass no caminho real do WordPress (rascunho-primeiro) | bloqueante | ✅ corrigido e ratificado (política conservadora) |
| F5.1 — collection gate fail-open para valores desconhecidos | menor→média | ✅ corrigido (fail-closed) e verificado |
| F5.2 — tipos não-string causavam TypeError | menor | ✅ corrigido e verificado |

Condições vigentes:

1. **Dry-run/lab:** liberado, sem pendência mecânica.
2. **Antes de WordPress real (mesmo draft):** resolver/declarar com prudência o `collection_request` do caso 261439, com decisão editorial humana registrada como evidência de cura.
3. **Antes de promoção para `root/v4`:** item acima + 2–3 casos reais adicionais em dry-run + `human_promotion_authorized` explícito.
4. **Auditoria GPT 5.5:** recomendada, não bloqueante (warning ativo no preflight).

---

*Fable — auditor externo, Projeto Cafezinho / V4*
*Esta carta encerra a trilha de auditoria mecânica da Fase 5 e pode ser referenciada como `audit_doc` no preflight (ex.: `fable_fase5_mechanical_closed: true`).*
