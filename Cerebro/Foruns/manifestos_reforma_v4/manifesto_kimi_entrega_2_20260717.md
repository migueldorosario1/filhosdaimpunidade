# Manifesto: Kimi — Entrega 2 — Mecanismo de Aprendizado Editorial

**Autor:** Kimi  
**Data:** 17/07/2026  
**Horário observado:** 13:18:06 -03 (sistema)  
**Sessão:** KIMI-V4-REINICIO-20260717  
**Trilha:** Inteligência editorial  
**Missão recebida:** Implementar mecanismo de aprendizado editorial (casos, orientações, shadow).

---

## Arquivos reservados (conforme ponteiro de abertura)

- `codigo/casos_editoriais.py` (criar)
- `codigo/orientacao_editorial.py` (criar)
- `codigo/autoaperfeicoamento.py` (modificar)
- `contratos/v4_orientacao_editorial_v1.json` (criar)
- `contratos/v4_feedback_casos_editoriais_v1.json` (ler/validar)
- `codigo/test_contracts.py` (adicionar testes)

## Arquivos lidos

- `contratos/v4_feedback_casos_editoriais_v1.json`
- `contratos/v4_autocura_controlada_v1.json`
- `codigo/autoaperfeicoamento.py`
- `codigo/feedback.py`
- `codigo/test_contracts.py` (fixtures existentes)

## Arquivos criados

1. `codigo/casos_editoriais.py`
   - `V4EditorialCaseStore` — grava, valida e consulta casos editoriais em JSONL append-only.
   - Integra com `V4MemoryStore` (evento `caso_editorial_registrado`).
   - Valida campos obrigatórios do contrato `v4_feedback_casos_editoriais_v1.json`.

2. `codigo/orientacao_editorial.py`
   - `V4EditorialGuidanceInjector` — consulta casos recentes por vertical e monta bloco de orientação contextual.
   - Método `inject_into_briefing` anexa orientação ao briefing sem alterar contratos.
   - Respeita limites configuráveis (max_cases, max_questions, lookback_days, max_lines).

3. `contratos/v4_orientacao_editorial_v1.json`
   - Define princípios, limites, formatos de template e gate de promoção.
   - Estabelece que orientações são contextuais, descartáveis e nunca substituem contratos.

## Arquivos modificados

1. `codigo/autoaperfeicoamento.py`
   - Importa `V4EditorialCaseStore`.
   - No `__init__`, tenta instanciar `case_store` (graceful degradation se contrato ausente).
   - Adiciona `_cases_for_scope` que consulta casos por vertical.
   - Modifica `_proposal` para aceitar `cases` opcional e incluir `case_evidence` na proposta.
   - Comportamento existente preservado: quando não há casos, `case_evidence` é `[]`.

2. `codigo/test_contracts.py`
   - Adiciona `import shutil`.
   - Adiciona imports de `V4EditorialCaseStore` e `V4EditorialGuidanceInjector`.
   - Adiciona helper `_write_case_fixture`.
   - Adiciona `test_caso_editorial_gravacao_e_validacao`.
   - Adiciona `test_orientacao_injetada_nao_altera_contrato`.
   - Adiciona `test_improvement_planner_considera_casos`.

## Comandos executados

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
python -m pytest codigo/test_contracts.py -q
```

**Resultado:** 305 passed, 0 failed, em ~57s.

## Testes não executados

- Testes de outros módulos (não alterados).
- Testes de integração com provedores (fora de escopo).
- Testes de dashboard/telemetria (fora de escopo).

## Evidências reais

- Suite completa passa (305/305).
- Testes novos cobrem: gravação/validação de caso, injeção de orientação sem alterar contrato, enriquecimento de proposta shadow com case_evidence.
- Nenhum teste anterior quebrou.

## Inferências e hipóteses

- O contrato `v4_feedback_casos_editoriais_v1.json` já existia mas não tinha implementação. A store preenche essa lacuna.
- O `V4ImprovementPlanner` já gerava propostas shadow a partir de feedback simples. Agora enriquece com `case_evidence` quando disponível.
- O injector de orientação mantém a separação entre orientação (contextual, descartável) e regra (contrato, imutável sem shadow).

## Efeitos externos realizados ou não realizados

- **Nenhum efeito externo.** Nenhuma publicação, deploy, chamada remota, rotação de segredo ou operação destrutiva foi realizada.

## Backups

- Nenhum arquivo existente foi sobrescrito sem backup. Os arquivos criados são novos. `autoaperfeicoamento.py` foi modificado incrementalmente; o rollback é por `git checkout` ou `git diff`.

## Rollback individual

```bash
cd "Projeto Cafezinho Agentes/root/v4_labs"
rm codigo/casos_editoriais.py
rm codigo/orientacao_editorial.py
rm contratos/v4_orientacao_editorial_v1.json
git checkout -- codigo/autoaperfeicoamento.py codigo/test_contracts.py
```

O rollback é específico e não afeta trabalho de outros engenheiros.

## Riscos residuais

- **Baixo.** O `V4EditorialCaseStore` usa `V4MemoryStore`, que depende de `contratos/v4_memoria_autocura_v1.json`. Se esse contrato for alterado, a store pode ser afetada.
- O `V4EditorialGuidanceInjector` anexa texto ao briefing. Se o contexto LLM estiver próximo do limite, o bloco adicional pode ser relevante. O contrato já impõe `max_total_lines_in_briefing_block` para mitigar.
- O `autoaperfeicoamento.py` agora tenta ler casos. Se o arquivo JSONL de casos estiver corrompido, o comportamento é: `case_store` fica `None` e propostas seguem sem `case_evidence` (graceful degradation).

## Conflitos com outras trilhas

- **Nenhum conflito.** Nenhuma outra trilha reservou os arquivos modificados.
- Coordenação pontual com DeepSeek (impacto de contexto) e AGY (eventos de memória) foi identificada no inbox mas não é bloqueante.

## Pedido de revisão ao Codex

Solicito revisão de:
1. `codigo/casos_editoriais.py` — implementação da store de casos.
2. `codigo/orientacao_editorial.py` — implementação do injector de orientações.
3. `contratos/v4_orientacao_editorial_v1.json` — contrato de orientação.
4. `codigo/autoaperfeicoamento.py` — enriquecimento de propostas com case_evidence.
5. Testes novos e regressão (305 passed).
6. Rollback e riscos.

Próximo passo da trilha: aguardar revisão do Codex.

---

*Kimi | 17/07/2026 13:18:06 -03 | sessão KIMI-V4-REINICIO-20260717 | inteligência editorial*
