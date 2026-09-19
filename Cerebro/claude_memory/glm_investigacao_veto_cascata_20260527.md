---
name: glm-investigacao-veto-cascata
description: "Investigação P1 do veto de cascata LLM — achados read-only, zero código editado"
metadata: 
  node_type: memory
  type: project
  originSessionId: e3d004b9-42ca-46ce-9bbf-5671821a846e
---

## Investigação P1 — Veto de Cascata LLM (27/05/2026)

**Status:** Diagnóstico completo. Sem autorização para corrigir.

### Achados

1. `_validar_separacao_modelos()` e string "VETO DE CASCATA" **não existem em nenhum .py local** — código Tencent-only não sincronizado
2. `motor_publicador.py:316` (revisão) e `:437` (auditoria) chamam `router_gen` sem passar exclusão de família
3. `roteador_llm.py:89-91` suporta `excluir_familias` mas o motor usa o roteador velho (`agente_roteador_llm.py`)
4. `llm_ratings_router.py:81-82` só lê exclusões estáticas do JSON
5. Mapeamento de famílias em `coletar_custos_internos.py:143-163` (qwen→alibaba, glm-→zhipu, etc.)

### Regra operacional (Miguel 27/05 ~00:20 BRT)

- **Estagiário** — só participa de fóruns e votações
- **Zero edição** de código sem autorização expressa do Claude Maestro + Miguel
- Comunicação via: fóruns + memória pessoal + inbox do Maestro (`inbox_trindade/claude.md`)
- **Why:** GLM é novo na Trindade, precisa de treinamento antes de tocar produção
- **How to apply:** Toda ação que não seja ler/escrever em fórum ou memória requer dupla autorização

### Links

- Fórum emergência: `Foruns/forum_emergencia_auditoria_agentes_pos_reforma_20260526.md` §8
- Relatório técnico Codex: `Foruns/forum_relatorio_tecnico_llms_cascatas_timeouts_20260526.md`
- Fórum Soberania: `Foruns/forum_diagnostico_agente_soberania_20260526.md`
