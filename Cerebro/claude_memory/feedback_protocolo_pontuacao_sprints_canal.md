---
name: feedback-protocolo-pontuacao-sprints-canal
description: "Toda Trindade DEVE pontuar canal 3x por sprint (início+etapa+conclusão) e documentar em fórum próprio. Maestro vigia com tickle automático. Sem isso Miguel se perde, sprints somem."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 656d971f-de46-442e-a3e2-07fe0206d845
---

# Protocolo §87 — Pontuação obrigatória de Sprints no canal trindade

**Regra inviolável (Miguel 22/05/2026 15:55 BRT, pós-incidente Codex G1+G2 entregar sem pontuar início):**

Toda Trindade pontua canal 3x por sprint:
1. **INÍCIO** (antes de começar): "🟢 {Agente} pegou Sprint X, começando agora. Detalhe forum Y."
2. **ETAPA** (cada marco intermediário): "🟡 {Agente} progresso Sprint X step Y."
3. **CONCLUSÃO** (entrega final): "🟢 {Agente} entregou Sprint X. Aguardando audit Maestro. Forum Y §N."

**Why:** sem pontuação Maestro não sabe se agente pegou, Miguel se perde, sprint vira pauta morta. Aplicação retroativa em sprints já atribuídos (Codex/DS/Kimi/AG pontuam próximo tick deles).

**How to apply:**

### Atribuição Maestro
- Sempre NOMINAL: "🟢 {Agente} — atribuído Sprint X, prazo Y, fórum Z"
- Nunca vago tipo "alguém pega isso?"

### Agente que recebe
- Ponto 1: pontuar canal ANTES de codar (PEGUEI)
- Ponto 2: pontuar cada etapa intermediária no canal + diff/raw no fórum
- Ponto 3: pontuar conclusão no canal + sumário no fórum

### Tickle Maestro
- Sprint sem ponto 1 em >30min → cutucão automático
- Sprint sem ponto 2 em >2h → cutucão
- Sprint sem ponto 3 após prazo → escalação Miguel

### Onde documenta
- Canal trindade = comunicação curta
- Fórum próprio do sprint = diff, raw, smoke, consenso, decisões
- NUNCA só canal — sempre fórum correspondente

Relacionado: [[feedback_imagem_destacada_obrigatoria]] (§86) · [[feedback_re_sincronizar_antes_de_postar_coordenacao]]

— Inscrito por Claude Maestro 2026-05-22 15:55 BRT
