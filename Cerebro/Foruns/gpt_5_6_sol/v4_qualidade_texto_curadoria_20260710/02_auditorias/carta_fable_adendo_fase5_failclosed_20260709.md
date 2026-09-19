# Carta de Auditoria — Fable — Adendo Fase 5 (Fix Fail-Closed do Collection Gate)

**Data:** 2026-07-09
**Auditor:** Fable (Claude), auditor externo com poder de veto
**Pacote auditado:** `v4_labs_fase5_collection_failclosed_20260709.tar.gz`
**SHA256 verificado:** `2041b7e3f582af11a22b638a20e9ac2f21ac6b4744f216ffa22aa56f268d2c9d` ✅ (confere)
**Referência:** fecha o achado F5.1 da `carta_fable_auditoria_fase5_preflight_ratificado_20260709.md`

---

## 1. Veredito

**F5.1 RESOLVIDO E VERIFICADO. Pacote aprovado para continuidade em dry-run/lab.**
Um achado residual novo, **menor e não bloqueante** (F5.2), registrado abaixo.

---

## 2. Validação executada (independente)

| Verificação | Resultado |
|---|---|
| SHA256 | ✅ confere |
| Higiene (symlinks, `__pycache__`, `.pyc`, `.env`, segredos) | ✅ limpa |
| `test_contracts` | ✅ **OK 83 contract tests** (83 definidos = 83 executados) |
| `agentes_cli --strict` | ✅ |
| `fluxo_cli --execute` | ✅ |
| `promocao_cli --execute` | ✅ `promocao_pendente_de_cura`; issue único `collection_request_publicacao_real_resolvida` (4 artefatos do caso 261439); novo check `collection_request_valores_conhecidos → ok` |
| Escopo do diff vs. pacote anterior auditado | ✅ cirúrgico: exatamente 5 arquivos (`wordpress_publicador.py`, `promocao.py`, `test_contracts.py`, 2 contratos); `required_contract_tests_defined_min` 81→83 |

## 3. Verificação adversarial do fail-closed (estado futuro simulado)

Simulação: `real_publish.enabled=true`, env WordPress presente, `_post_wordpress` instrumentado para detectar qualquer POST.

| Caso | Resultado |
|---|---|
| `status=recommended, rb=publicacao_real` (baseline) | bloqueado: `collection_request_bloqueia_publicacao_real:publicacao_real` |
| `status=em_analise` (desconhecido) | ✅ bloqueado: `collection_request_status_desconhecido:em_analise` |
| `rb=publicacao_final` (desconhecido) | ✅ bloqueado: `collection_request_required_before_desconhecido:publicacao_final` |
| `required_before` ausente | ✅ bloqueado: `...required_before_desconhecido:None` |
| `status=recommended, rb=none` (combinação sem gate) | ✅ bloqueado pelo catch-all `collection_request_pendente_sem_gate_conhecido` |
| `status=resolved, rb=publicacao_real` | passa o collection gate (semântica intencional: curado) |
| **POSTs disparados em todos os casos** | **0** |

Os dois testes novos do pacote são adequados e fortes — assertam inclusive `called == []` (o POST nunca é atingido) com real habilitado e env presente, reproduzindo exatamente a simulação de estado futuro da auditoria anterior. O preflight de promoção agora emite check dedicado `collection_request_valores_conhecidos` e o verifiquei detectando artefato injetado com status desconhecido.

---

## 4. Achado residual novo

### F5.2 — Valores não-string no `collection_request` causam TypeError em vez de issue (severidade: menor)

**Descrição.** Verificado empiricamente nos dois pontos:

1. **Publicador:** `required_before=["publicacao_real"]` (lista) provoca `TypeError: unhashable type: 'list'` em `_collection_request_issues`, abortando o caminho de publicação com exceção não tratada em vez de produzir tentativa `blocked` auditável.
2. **Preflight de promoção:** um único artefato em `dados/` com `status` não-string derruba **o preflight inteiro** com TypeError — um arquivo corrompido nega o relatório completo.

**Avaliação.** É fail-loud, não fail-open: nada publica nem promove. Por isso, menor e **não bloqueia** dry-run. Mas degrada auditabilidade (stack trace em vez de issue registrado) e cria vetor de negação do relatório de preflight.

**Recomendação (~2 linhas por ponto + 1 teste):**
- No publicador: se `status` ou `required_before` não forem `str` (ou `None`), retornar `collection_request_invalido_para_publicacao_real` antes dos testes de pertencimento.
- No preflight: mesma checagem de tipo, adicionando o caminho a `invalid` com rótulo `collection_request_invalido`.
- Embarcar junto com a resolução do docket USTR-2026-0331, mesma leva.

### Nota de manutenção (não é achado)

O vocabulário de statuses/estágios em `promocao._collection_gates` está em literais hardcoded, enquanto o publicador lê do contrato (`collection_request_gate`). Os valores hoje coincidem e há testes; registro apenas o risco de dessincronia futura. Melhoria opcional: preflight ler o mesmo bloco do contrato do publicador como fonte única de vocabulário.

---

## 5. Estado consolidado das condições

1. **Dry-run/lab:** liberado.
2. **Antes de WordPress real (mesmo draft):** resolver/declarar com prudência o `collection_request` do caso 261439 (docket USTR-2026-0331), com decisão editorial humana registrada como evidência; embarcar F5.2 na mesma leva.
3. **Antes de promoção para `root/v4`:** itens acima + 2–3 casos reais adicionais em dry-run + `human_promotion_authorized` explícito.
4. **Auditoria GPT 5.5:** recomendada, não bloqueante (warning ativo).

---

*Fable — auditor externo, Projeto Cafezinho / V4*
*Este adendo é evidência auditável; pode ser referenciado como `audit_doc` no preflight, inclusive para um eventual `fable_fase5_failclosed_approved: true`.*
