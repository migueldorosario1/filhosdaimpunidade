---
name: feedback-constituicao-artigo2-comunicacao-trindade
description: "Artigo 2 da Constituição da Grande Reforma — canal=ponteiro, fórum=memória, inbox=pessoal, cartinha=resumo humanizado. Vinculante durante e após a Reforma"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

Artigo 2 da Constituição da Grande Reforma (Miguel 2026-06-12 ~23:25 BRT) — separa canais por função.

**Regra de ouro de comunicação:**

| Onde | Função | Tamanho |
|---|---|---|
| `canal_trindade.md` | **Ponteiro** — link + resumo de 1 linha | 1-3 linhas |
| Fórum dedicado | **Memória** — documento completo (decisões/diagnósticos/deploys/incidentes) | Sem limite |
| `inbox_trindade/<agente>.md` | **Mensagem pessoal entre engenheiros** (Codex → Kimi etc) | Curta |
| Cartinha humanizada | **Resumo pós-missão** pra Miguel colar nos chats — linguagem de gente, emojis ok | 10-30 linhas |

**Why:** Antes a comunicação virava bagunça — alertas longos no canal_trindade, decisão sem rastro estruturado, inbox usada como broadcast. Artigo 2 dá disciplina pra Grande Reforma rodar sem virar caos.

**How to apply:**
- **Incidente/missão crítica:** abrir fórum `Foruns/forum_<tema>_<YYYYMMDD>.md` ANTES de postar. No canal_trindade só uma linha apontando: `> [DATA] Agente → Trindade / Título curto. Fórum: forum_X.md`.
- **Missão concluída:** escrever cartinha humanizada (com emojis ok) pra Miguel circular. Detalhe técnico no fórum.
- **Comunicação cross-engenheiro privada:** inbox direto. Não broadcast.
- **Decisão de sistema:** sempre em fórum. "Se não está no fórum, não aconteceu."

**Caso fundador:** meus alertas §93 de 18:50 e 22:30 BRT do dia 12/06 violaram a regra nova (80+ linhas no canal_trindade direto). Eram pré-Artigo 2 — passam. Mas a partir de agora: fórum primeiro, ponteiro no canal.

Mesmo nível de inegociável de [[feedback_protocolo_backup_rollback_index_inegociavel]] e [[feedback_deploy_gate_92]].
