# Carta de Auditoria — Fase 4 Agents/Pipeline (auditfix)

**De:** Fable (Claude, auditor externo com poder de veto)
**Para:** Miguel, Codex e fórum V4
**Data:** 2026-07-09
**Pacote auditado:** `v4_labs_fase4_agents_pipeline_auditfix_20260709.tar.gz`
**SHA256:** `334cc3865fcdcf75f74943574a977304ef88271f0c325c225e10a2fe96980071` (conferido)
**Substitui:** auditoria do pacote `v4_labs_fase4_agents_pipeline_20260709.tar.gz` (SHA `976f4136...`, 69 testes)

---

## Veredito

**Fase 4 auditfix APROVADA.** As três observações não bloqueantes da auditoria anterior foram incorporadas, cada uma com teste dedicado. `OK 73 contract tests` reproduzido de forma independente em extração limpa. O diff entre os pacotes é cirúrgico: 6 arquivos tocados, todos dentro do escopo das observações.

## Verificação das três correções

### Obs 1 — Regeneração automática vs. evidência de bloqueio

**Incorporada (declarativa).** O contrato `v4_fluxo_dry_run_v1.json` ganhou a cláusula `promocao_para_producao`:

- `regenera_artefato_fixture_invalido_deve_ser_false: true`
- `artefato_bloqueado_evidencia_append_only: true`
- `producao_nao_sobrescreve_bloqueio: true`
- Motivo registrado por extenso.

O teste `test_fluxo_producao_nao_regenera_artefato_bloqueado` trava a cláusula. **Ressalva:** a proteção é declarativa porque o contrato de produção ainda não existe. O checklist de promoção deve incluir a verificação efetiva de `regenera_artefato_fixture_invalido=false` quando esse contrato nascer. A cláusula é o lembrete contratual, não o enforcement.

### Obs 2 — Fact-checker que não lia o texto

**Incorporada, acima do mínimo pedido.** `V4FactCheckAgent` ganhou heurística de presença textual dirigida por contrato (`min_matched_tokens=3`, `min_overlap_ratio=0.35`, `min_token_len=4`, stopwords configuráveis), e o manifesto agora declara honestamente `check_type: metadata_plus_text_presence_heuristic`. Teste negativo (`test_fact_check_bloqueia_fato_obrigatorio_ausente_do_texto`) prova o bloqueio. Verificação empírica: a heurística falha fechada — fatos curtos são bloqueados mesmo quando presentes (atrito aceitável, não risco).

**Refinamentos sugeridos para próxima rodada (não bloqueantes):**

1. `min_token_len=4` descarta tokens numéricos curtos ("25", "301") — exatamente os números que um fact-check mais precisa conferir. Um fato com as palavras genéricas certas mas o percentual errado no texto passaria. Sugestão: preservar tokens numéricos independente do comprimento.
2. `matches` é lista e o denominador do ratio usa `set(fact_tokens)`: token duplicado no fato infla o ratio. Correção de uma linha: `set(matches)`.

### Obs 3 — Gate de collection_request na publicação real

**Incorporada, com decisão semântica embutida.** O publicador ganhou `_collection_request_issues`, dirigido pelo bloco `collection_request_gate` do contrato:

- `collection_request` ausente bloqueia publicação real.
- `recommended` e `required` com `required_before: publicacao_real` bloqueiam.
- `none`/`resolved` liberam.
- O payload WordPress carrega `v4_collection_request` na meta (rastreabilidade).

Dois testes novos cobrem ausência e bloqueio. O caso 261439 agora tem imposição mecânica com dono.

## Questão para ratificação do fórum

A correção da Obs 3 respondeu de facto uma questão que estava formalmente aberta: **`recommended` e `required` são hoje comportamentalmente idênticos em todos os pontos do pipeline** — ambos geram warning nos estágios intermediários e ambos bloqueiam duro na publicação real e nos estágios shadow/redator. A distinção entre os dois status é atualmente vocabulário decorativo.

Isso não é defeito — a postura "suave a montante, duro no último portão" é defensável. Mas é decisão editorial, e deve ser escolha registrada do Miguel/fórum, não acidente de implementação. Duas saídas possíveis:

1. **Diferenciar:** `recommended` passa a ser liberável por aprovação humana explícita no portão de publicação real; `required` permanece inegociável até `resolved`.
2. **Colapsar:** eliminar um dos termos do vocabulário do contrato e simplificar.

Recomendo levar ao fórum antes da abertura da rota `redator_real` em produção.

## Estado dos achados de auditorias anteriores

Todos os 5 achados da Fase 3 (custo/tokens reais, flag de temperatura, fallback por modelo, sanitização de chaves, idempotency key) permanecem resolvidos e testados neste pacote. Nenhuma regressão detectada.

## Gates confirmados fechados

- `wordpress_real=false` em todos os artefatos.
- Publicação real bloqueada por contrato do publicador.
- `collection_request` do caso 261439 bloqueando `publicacao_real` até confirmação do comentário no docket USTR-2026-0331 ou declaração da limitação com prudência editorial.

---

*Auditoria executada de forma independente a partir do pacote: extração limpa, SHA256 conferido, 73 testes reproduzidos, diffs entre pacotes verificados arquivo a arquivo, heurística de fact-check testada empiricamente com edge cases.*

— Fable
