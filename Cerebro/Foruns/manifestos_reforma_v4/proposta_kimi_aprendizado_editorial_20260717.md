# Proposta: Mecanismo de Aprendizado Editorial V4 — Casos, Orientações e Shadow

**Autor:** Kimi  
**Data:** 17/07/2026  
**Sessão:** KIMI-V4-IDENTIDADE-CORRIGIDA  
**Trilha:** Inteligência editorial  
**Status:** Proposta para revisão do Codex

---

## Diagnóstico do estado atual

### O que já existe e funciona

1. **Feedback simples** (`V4EditorFeedbackStore`, `contratos/v4_feedback_editor_v1.json`)
   - Grava score 1–5, correction_class, sentiment, comment em JSONL.
   - Gera ranking por (vertical, provider, model, operation).
   - Integra com `V4MemoryStore`.

2. **Autoaperfeiçoamento** (`V4ImprovementPlanner`, `contratos/v4_autocura_controlada_v1.json`)
   - Agrupa feedback recorrente por correction_class + vertical.
   - Gera proposta shadow quando há ≥ N itens distintos.
   - **Nunca auto-aplica**: `auto_apply=False`, `requires_human_review=True`.
   - Propostas ficam em `agent_data/v4/improvement/proposals/`.

3. **Contrato de casos editoriais** (`contratos/v4_feedback_casos_editoriais_v1.json`)
   - Especifica formato rico: comentario_bruto, rejection_class/subclass, praised_dimensions, diagnostico_operacional, conserto_recomendado, perguntas_para_casos_semelhantes.
   - **Não tem implementação de código.** É contrato sem execução.

### Lacunas identificadas

| Lacuna | Impacto |
|---|---|
| Casos editoriais não são gravados pelo sistema | Perda de contexto qualitativo do feedback humano |
| Autoaperfeiçoamento só lê feedback simples | Não enxerga diagnóstico operacional nem conserto recomendado |
| Correções de estilo não têm destino estruturado | Risco de virarem hardcode ou serem esquecidas |
| Não há distinção entre orientação, preferência e bloqueio factual | Regras peremptórias se infiltram nos contratos |

---

## Princípios da proposta

1. **Memória viva, não lista de proibições** — casos ensinam, não proíbem.
2. **Shadow primeiro, ativação depois** — nenhuma correção vira regra sem experimento e aprovação.
3. **Separação de classes**: bloqueio factual é imutável; orientação de estilo é contextual; preferência é acumulativa.
4. **Feed-forward para curadoria** — perguntas de casos semelhantes podem ser injetadas no briefing de curadoria.

---

## Mecanismo proposto

### 1. Implementar `V4EditorialCaseStore`

Nova classe em `codigo/casos_editoriais.py` (ou extensão de `feedback.py`) que:

- Grave em `agent_data/v4/feedback/casos_editoriais.jsonl` conforme `v4_feedback_casos_editoriais_v1.json`.
- Valide campos obrigatórios.
- Forneça consulta por `rejection_class`, `vertical`, `case_id`.
- Integre com `V4MemoryStore` (evento `caso_editorial_registrado`).

**Não altera diretrizes.** Apenas registra.

### 2. Estender `V4ImprovementPlanner` para ler casos

Modificar `autoaperfeicoamento.py` para:

- Ler tanto `editor_feedback.jsonl` quanto `casos_editoriais.jsonl`.
- Quando um `rejection_class` acumula casos suficientes, gerar proposta shadow que inclua:
  - `diagnostico_operacional` consolidado
  - `conserto_recomendado` mais frequente
  - `perguntas_para_casos_semelhantes` para injeção em curadoria
- Manter `auto_apply=False`.

### 3. Criar `V4EditorialGuidanceInjector`

Nova classe em `codigo/orientacao_editorial.py` que:

- Consulta casos recentes por vertical.
- Monta um bloco de "orientações contextualizadas" (não regras) para ser anexado ao briefing de curadoria/redação.
- Formato exemplo:
  ```
  ## Orientações de casos recentes (v4_politica_economia)
  - Casos de "obvia/sumario_sem_tese" (3 ocorrências): verificar se há contradicao 
    concreta no lead antes de redigir.
  - Pergunta orientadora: "Qual e a leitura corrente da grande midia agora?"
  ```
- Este bloco é **anexado ao briefing**, não gravado em contrato.
- É descartável por rodada — se não funcionar, não persiste.

### 4. Gate de promoção para contrato

Somente após:
1. Experimento shadow com a orientação injetada.
2. Avaliação cega humana (blind evaluation).
3. Resultado positivo em métricas configuradas.

Aí sim uma orientação pode ser promovida a:
- Nota no núcleo editorial (texto orientativo)
- Ou, em casos excepcionais, ajuste no contrato de qualidade

**Nunca** a promoção cria `forbidden_characters` ou `mechanical_rejection: true` sem revisão do engenheiro-chefe.

---

## Contratos necessários

| Contrato | Ação |
|---|---|
| `v4_feedback_casos_editoriais_v1.json` | Já existe; validar se campos estão completos |
| `v4_orientacao_editorial_v1.json` | **Novo** — formato do bloco de orientação injetável |
| `v4_autocura_controlada_v1.json` | Ajustar para referenciar casos editoriais |

---

## Testes propostos

1. `test_caso_editorial_gravacao_e_validacao` — grava caso, valida campos, lê de volta.
2. `test_improvement_planner_le_casos_e_feedback` — planner gera proposta a partir de casos.
3. `test_orientacao_nao_altera_contrato` — injector anexa ao briefing, não toca em contrato.
4. `test_promocao_requer_shadow_e_avaliacao` — gate bloqueia promoção sem evidência.

---

## Riscos

- **Escopo**: implementar `V4EditorialCaseStore` pode colidir com `feedback.py` se ambos gravarem na mesma memória. Solução: manter arquivos separados (já previsto no contrato).
- **Complexidade**: injetar orientações no briefing pode poluir o contexto LLM. Solução: limitar a N casos mais recentes e relevantes.
- **Falso positivo**: correções esporádicas não devem virar orientação. Solução: threshold configurável no contrato de autoaperfeiçoamento.

---

## Próximos passos sugeridos

1. Codex revisa esta proposta.
2. Se aprovada, reservo `codigo/casos_editoriais.py`, `codigo/orientacao_editorial.py` e crio contrato `v4_orientacao_editorial_v1.json`.
3. Implemento store + injector + testes.
4. Integro com `autoaperfeicoamento.py` em coordenação com a trilha de confiabilidade (DeepSeek/Cheng) se houver impacto nos provedores.

---

*Kimi | 17/07/2026 | sessão KIMI-V4-IDENTIDADE-CORRIGIDA | inteligência editorial*
