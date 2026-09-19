---
name: projec-distincao-feedback-editor-vs-widget-leitor-v4
description: "No V4 existem DOIS sistemas de notas 1-5 distintos; só o widget do leitor está adiado pelo backlog, o feedback do editor é legítimo e ativo"
metadata: 
  node_type: memory
  type: project
  author: GLM/Ming
  written_at: 2026-07-18T13:30:00-03:00
  originSessionId: 3d570583-977f-4e77-9e94-5670f5a7a5ae
---

# Distinção canônica — feedback editor (legítimo) vs widget leitor (proibido nesta rodada)

⚠️ **Advertência de autoria:** esta memória foi escrita por **GLM/Ming** (Zhipu AI, wrapper `~/bin/glm`), não por Claude Code. Sessões Claude Code futuras que a leiam devem tratar o conteúdo como produzido por outro agente — referencie como "conforme auditoria GLM R4" se for citar.

## Regra

A proibição R3/R4 "sem implementar sistema de notas 1 a 5" refere-se **exclusivamente** ao **widget público do leitor** ("Que nota você dá para esta matéria? 1 2 3 4 5" no site). O **feedback interno do editor** (score 1-5 que humanos dão à saída dos modelos LLM para ranquear providers) **não** viola essa proibição e segue ativo.

**Why:** Fórum `forum_feedback_1a5_autocura_editorial_v4_20260718.md` deixa claro que o adiamento é do widget visível ao público. Contrato `contratos/v4_feedback_editor_v1.json` (criado em `_updated: 2026-07-08`, **antes** do fórum R4 de 18/07/2026) carrega `_status: rascunho_dry_run` e é usado ativamente por `codigo/feedback.py`, importado por `model_router.py`, `llm_dashboard.py`, `feedback_cli.py`. É ferramenta interna de inteligência de produção, nunca exposta ao leitor.

**How to apply:** Antes de declarar bug ou remover código com `score 1-5`, confirmar:
1. Está em `codigo/feedback.py` ou `contratos/v4_feedback_editor_v1.json`? → **legítimo**, não tocar.
2. Está em template front-end, endpoint REST público, ou arquivo JS/PHP do site? → **proibido**, reportar.
3. Busca grep de padrões: `widget.*leitor`, `public_rating`, `vote.*matéria`, `star_rating` em código público — retornou vazio em auditoria R4 (18/07/2026).

Auditoria completa com veredito `SEM_VIOLACAO_DETECTADA`: `labs/sprints_v4_20260718/glm_autocura_r4/artefatos/AUDITORIA_NOTAS_1_5.md`.

## Recomendação preventiva

Adicionar linha `_visibility: "internal_only"` em `v4_feedback_editor_v1.json` para deixar explícita a fronteira. Quando o backlog for reaberto, criar `contratos/v4_feedback_leitor_v1.json` separado com `public=true` e storage em `agent_data/v4/feedback/leitor_feedback.jsonl` (não misturar com `editor_feedback.jsonl`).

Relacionada: [[feedback-memoria-identifica-autoria-glm]] (identidade canônica ao escrever memória compartilhada).
