# Especificação única v0.1 — Autoaprendizado e autocura do V4 Mídia

**Data:** 2026-08-07 02:05 BRT  
**Autor da consolidação:** Codex  
**Convocação:** Miguel do Rosário  
**Tag:** `[CODEX-ESPEC-V0.1-AUTOAPRENDIZADO-AUTOCURA-V4-MIDIA]`  
**Entradas lidas integralmente:** convocação Codex · Claude 01:30 · Antigravity §20 · Grok 01:37/§21 · Kimi R1 01:40 · Kimi R2 01:50  
**Ausentes:** DeepSeek, Qwen e GLM; parecer tardio é aceito, mas não bloqueia esta versão.  
**Estado:** especificação para homologação de Miguel; artefatos L0/L2 podem ser construídos em shadow, mas nada aqui autoriza escrita editorial ou promoção automática em produção.

---

## 1. Veredito da rodada

As cinco convergências identificadas pelo Kimi ficam **homologadas na especificação v0.1**:

1. **Gold positivo:** somente `human_accept` explícito ou `official_hash` verificado. Publicação, ausência de correção e consenso entre modelos são telemetria, nunca ouro.
2. **Funil determinístico antes de visão:** C0–C5 barato; visão somente no top-K, com `K ≤ 3`; IA final somente quando a política da vertical permitir e com recibo das tentativas.
3. **Ledger append-only com um único writer path:** nenhuma escrita direta por agentes; correção por supersessão.
4. **NOOP_FIRE é falha:** processo disparado sem trabalho útil nunca conta como health verde.
5. **Toda rejeição recebe `reason_code` taxonomizado.** Exceção silenciosa é defeito de observabilidade.

Também ficam homologadas as adjudicações R2:

- publish pode registrar `features_preservadas`, mas com `role=production` e `gold=false`;
- unwrap determinístico de HTML é L1; reescrita de frase é decisão editorial;
- freio de backlog é hemostasia e sempre abre diagnóstico L0 com `causa_suspeita`;
- shadow challenger é amostrado, nunca full-traffic por padrão;
- replay exige `policy_version` e `system_state`.

## 2. Contrato canônico do recibo v0.1

O R2 chamou o contrato de “15 campos”, mas o exemplo continha 17 campos de topo. Para eliminar a inconsistência, a v0.1 terá **15 campos funcionais de topo**; identificação, supersessão, vértice e tempo ficam agrupados em `metadata`.

```json
{
  "sinal": "descrição observável que iniciou o caso",
  "causa_raiz": "mecanismo comprovado ou unknown",
  "correcao": "ação executada, proposta ou none",
  "prova": {
    "before": {},
    "after": {},
    "checks": [],
    "artifacts": []
  },
  "rollback": "procedimento, feature flag ou n/a — read-only",
  "regra_derivada": "condição → ação reutilizável",
  "alcance": "local|vertical|v4|ecossistema",
  "risco_promocao": "L0|L1|L2|L3",
  "policy_version": "midia-v0.1",
  "origem": "human_editor|machine_autocure|trindade_deliberation",
  "system_state": {
    "seletor": "...",
    "cotas": "...",
    "fontes_ativas": [],
    "prompt_juiz": "...",
    "schema_versions": {}
  },
  "role": "production|shadow|gold",
  "gold_source": "human_explicit|official_hash|hard_block_deterministic|null",
  "reason_code": "NOOP_FIRE|ENTITY_MISMATCH|...",
  "metadata": {
    "schema_version": "receipt-v0.1",
    "receipt_id": "ULID ou UUID",
    "ref": null,
    "vertice": "kimi|claude|codex|grok|antigravity|worker",
    "ts": "ISO-8601 com timezone",
    "generalizabilidade": "high|medium|low",
    "causa_suspeita": null
  }
}
```

### 2.1 Regras de validação

- Todos os 15 campos são obrigatórios; valor desconhecido é explícito (`unknown`/`null`), nunca omitido.
- `role=gold` exige `gold_source != null` e evidência verificável em `prova`.
- `human_explicit` exige referência à decisão humana; `official_hash` exige SHA-256 e origem oficial; `hard_block_deterministic` só cria gold negativo.
- `ref` aponta para recibo anterior quando houver correção/supersessão. Nenhum recibo é atualizado ou apagado.
- `causa_raiz=unknown` impede painel de exibir “curado”; no máximo “contido”.
- `risco_promocao=L2|L3` jamais executa ação de produção pelo writer.
- `generalizabilidade=high` exige repetição 2+/7d, regra derivável e ausência de contradição ativa; exceções precisam de deliberação Trindade/Miguel.

## 3. Ledger e responsabilidades

### 3.1 Fonte de verdade

- Master proposto: sidecar no Tencent, junto ao master do Banco Ouro, mas fora do banco de acervo.
- Fonte durável: JSONL append-only com rotação diária.
- Índice SQLite é cache reconstruível, nunca autoridade.
- NYC e local recebem espelhos read-only.

### 3.2 Escrita

- Único escritor: `ledger_writer.py` no master.
- Agentes e workers depositam recibos em inboxes; nunca abrem o ledger ou o banco de acervo para escrever.
- O writer valida schema, atribui ID/tempo quando necessário, faz append atômico, registra rejeições e mantém idempotência por `receipt_id`.
- A Ponte de Imagens produz candidatas e evidências; ingestão no acervo continua pelo writer próprio do Banco Ouro.

### 3.3 Separação de papéis

- **Ledger:** história das decisões e autocuras.
- **Corpus Ouro:** subconjunto curado de recibos gold.
- **Telemetria:** produção/shadow, útil para investigação, sem poder de treinar regra como verdade.
- **Banco Ouro:** mídia e metadados de acervo; não recebe regras de autocura.

## 4. Taxonomia inicial de `reason_code`

### Infraestrutura

`NOOP_FIRE`, `COMMAND_TRUNCATED_BY_COMMENT`, `EXECUTABLE_MISSING`, `TIMEOUT`, `LOCK_BUSY`, `LOG_PATH_INVALID`, `SCHEMA_DRIFT`, `WRITE_PERMISSION_DENIED`, `SYNC_STALE`.

### Recuperação e arquivo

`MIME_INVALID`, `BINARY_CORRUPT`, `DIMENSIONS_LOW`, `LICENSE_EMPTY`, `LICENSE_FORBIDDEN`, `SOURCE_BROKEN`, `OBJECT_MISSING`, `HASH_REJECTED`, `REPEAT_COOLDOWN`, `QUERY_NO_PROGRESS`.

### Semântica editorial

`ENTITY_MISMATCH`, `EVENT_MISMATCH`, `LOCATION_MISMATCH`, `GENERIC_STOCK`, `TEXT_OR_LOGO`, `IA_VERTICAL_FORBIDDEN`, `CAPTION_INVALID`, `CREDIT_INVALID`, `HTML_WORD_BREAK`.

### Fila e estado

`IMAGE_PENDING_CREATED`, `REPAIR_FAILED`, `REPAIR_SUCCEEDED`, `BACKLOG_NET_GROWTH`, `CIRCUIT_BREAKER_OPEN`, `WP_SQLITE_RECONCILED`, `EXTERNAL_RESOLUTION`, `QUARANTINED`.

Novos códigos entram por proposta versionada; strings livres ficam apenas em `sinal`/`prova`.

## 5. Máquina de estados da pauta e da imagem

```text
DISCOVERED
  └─> DRAFT_BUILDING
        ├─> DISCARDED
        └─> IMAGE_RESOLUTION
              ├─> PREFLIGHT_REJECTED ──> próxima estratégia
              ├─> IMAGE_SELECTED
              │     └─> READY_FOR_REVIEW
              │           ├─> PUBLISHED
              │           ├─> DISCARDED
              │           └─> IMAGE_PENDING (rejeição editorial)
              └─> IMAGE_PENDING
                    └─> REPAIRING
                          ├─> IMAGE_SELECTED
                          ├─> IMAGE_PENDING (com progressão obrigatória)
                          └─> QUARANTINED
```

### 5.1 Invariantes

- `IMAGE_PENDING` não é elegível a publicação.
- Falha de reparo não cria pauta nova na mesma vertical enquanto o circuit breaker estiver aberto.
- Cada retry registra `strategy_id`; repetir a mesma estratégia/query/fonte sem evidência nova gera `QUERY_NO_PROGRESS` e não consome indefinidamente o orçamento.
- `READY_FOR_REVIEW` exige readback de `featured_media`, licença/crédito e estado WP.
- Mudança externa no WP é reconciliada; nunca se rebaixa post publicado nem se ressuscita lixo.
- `QUARANTINED` exige motivo e rota humana; não é descarte invisível.

### 5.2 Estado da vertical

Separado do estado da pauta:

`HEALTHY → DEGRADED → CIRCUIT_OPEN → RECOVERING → HEALTHY`.

- `DEGRADED`: sinal presente, criação ainda segura.
- `CIRCUIT_OPEN`: `net_queue_growth > 0` por 3 ciclos, age/p95 excedido ou hard invariant quebrada; pausa novas pautas, mas permite reparos.
- `RECOVERING`: causa corrigida; exige dois ciclos úteis consecutivos antes de reabrir.
- Toda abertura exige `causa_suspeita` e ticket L0. Sem causa fechada, painel diz “contido”, não “curado”.

## 6. Funil de mídia C0–C7

1. **C0:** MIME, legibilidade, arquivo completo.
2. **C1:** dimensões e aspect ratio.
3. **C2:** licença e crédito parseáveis ou fonte allowlist.
4. **C3:** hash/pHash, blacklist e cooldown de reutilização.
5. **C4:** entidade tipada; substring genérica proibida.
6. **C5:** aderência textual/embedding barato e ranking.
7. **C6:** visão somente no top-K (`K ≤ 3`).
8. **C7:** escape final/IA somente com política da vertical, orçamento e recibo.

Cada descarte C0–C5 produz `reason_code` sem chamada visual. Consenso de modelos nunca transforma telemetria em gold.

## 7. Gates de promoção

### L0 — observar

Pode entrar direto em shadow: lint, métricas, ledger, heartbeat útil, replay offline. Não altera produção.

### L1 — determinístico e reversível

Só é promovido após:

1. regra precisa e idempotente;
2. teste positivo, negativo e de repetição;
3. pós-condição/readback;
4. rollback testado;
5. emissão de recibo válida;
6. shadow sem regressão em casos adversariais;
7. definição explícita do que acontece quando a causa é desconhecida.

Primeiras candidatas: reconciliação WP→SQLite, freio de backlog, preflight de schema conhecido, normalização de link público, unwrap de HTML sem reescrita e NOOP heartbeat. Ações que escrevem WP continuam fora de L1 v0.1, salvo decisão explícita de Miguel.

### L2 — adaptação

Exige Corpus Ouro, replay determinístico diário, replay visual semanal/sob promoção, pack adversário, challenger amostrado ≤20% ou N/vertical/dia e kill-switch de custo.

### L3 — política/editorial

Somente Miguel autoriza. Inclui cotas, prompts, licenças aceitas, voz, taxonomia, identidade e liberação de IA por vertical.

## 8. Métricas do piloto

Ordem de prioridade:

1. `identity_precision@1` — métrica-chefe, somente em gold verificável;
2. `event_precision@1`;
3. `human_same_reason_7d`;
4. `license_pass_rate`, `stock_generic_rate`, `repeat_ahash_7d_site`;
5. `net_queue_growth`, `age_p95`, `strategy_progression_rate`, `noop_fire_rate`;
6. `vision_calls_per_hero`, `cost_usd_per_correct_hero`;
7. `shadow_regret` e `promotion_rejection_rate`.

“Menos pending” e “mais featured” são métricas operacionais, não prova de acerto editorial.

## 9. Malha de entrega em 48 horas

| Responsável | Entrega | Gate |
|---|---|---|
| Kimi | `media_ledger` v0.1, writer/inbox/read-only mirrors e recibo Regional | L0 shadow |
| Claude | `gate_pre_publish.py` com 3 gates e recibos; HTML limitado a unwrap | testes/replay antes de produção |
| Antigravity | lint de cron + circuit breaker | inicialmente read-only/shadow |
| Grok | pack adversário + replay de métricas | offline, gate de regressão |
| Codex | esta especificação + máquina de estados + contrato de schema | homologação Miguel |

Integração: todos emitem recibo v0.1 para inbox; nenhum escreve no acervo; nenhum executa L2/L3.

## 10. Gates submetidos a Miguel

### G0 — Construção do piloto shadow

**Recomendação Codex: APROVAR.** Autoriza construir os artefatos da §9 sem escrita editorial e sem chamadas visuais em tráfego total.

### G1 — Regra de gold

**Recomendação: APROVAR.** Positivo apenas humano explícito/hash oficial; negativo humano/hard-block reproduzível.

### G2 — Orçamento

**Recomendação: APROVAR COM TETO.** Challenger ≤20% ou N/vertical/dia; visão top-K≤3; kill-switch por custo diário definido antes de ativar.

### G3 — Autocuras L1 em produção

**Recomendação: NÃO AUTORIZAR EM BLOCO.** Cada autocura pede promoção individual após testes. Lint/heartbeat podem alertar; escrita ou pausa automática só depois de aceite específico.

### G4 — Patch GLM de observabilidade do dedup

**Recomendação: APROVAR**, pois troca `continue` silencioso por rastro/`reason_code`, com backup e sem alterar decisão editorial. Deve gerar recibo nº 2.

### G5 — Autoridade

Kimi mantém palavra final técnica sobre o pipeline de mídia conforme decisão anterior; Miguel mantém decisão exclusiva de L3 e dos gates de produção.

## 11. Critério de aceite do piloto

Após sete dias, o piloto só pede promoção se:

- nenhum hard case adversário regredir;
- `identity_precision@1` não cair;
- `human_same_reason_7d` mostrar queda ou tendência explicável;
- custo estiver dentro do teto;
- ledger não tiver violações de append-only/schema;
- toda cura tiver prova e rollback;
- incidentes contidos, mas sem causa, aparecerem como abertos;
- Miguel receber um relatório legível de promoções aceitas e rejeitadas.

## 12. Pergunta-hábito

> **O que o sistema aprendeu, como provamos e até onde ele pode agir sozinho na próxima vez?**

Esta pergunta vira campo de fechamento de todo trabalho material, mas a resposta só entra como gold quando obedecer ao contrato desta especificação.

— Codex · 2026-08-07 02:05 BRT
