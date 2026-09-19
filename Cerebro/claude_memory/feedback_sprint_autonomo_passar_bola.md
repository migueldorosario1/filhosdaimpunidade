---
name: feedback-sprint-autonomo-passar-bola
description: "Sprint Autônomo = passar a bola entre Codex e Claude via ticks alternados dos loops, não trabalhar isolado"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2b9623d1-ac11-4398-963e-f595ae871d7f
---

# Sprint Autônomo = passar a bola via ticks alternados

**Clarificação Miguel 2026-05-15 09:28 BRT:** "sprint autonomo quer dizer um ir passando a bola para outro, através de seus ticks nos loops".

**Why:** Sprint Autônomo §55 NÃO significa cada um trabalhar isolado em suas próprias frentes. É **coordenação contínua** com hand-off explícito a cada tick. Codex faz algo no tick `:12, :42`, passa o estado, Claude pega no tick `:07, :37`, avança, passa de volta. E assim por diante até a sprint fechar.

**How to apply:**

1. **Cada tick do meu loop:** ler canal procurando estado deixado pelo Codex no tick anterior dele
2. **Avançar a sprint** — não começar coisa nova solta; pegar onde Codex parou
3. **Deixar estado claro** pro próximo tick do Codex pegar:
   - O que fiz neste tick
   - O que falta
   - O que ele precisa decidir/fazer
4. **Cadência:** Codex `:12, :42` (30min) · Claude `:07, :37` (30min) — gap 5min entre picos
5. **Recadinho no canal** sempre que avançar, com o que foi feito + próximo passo

**Quando NÃO seguir passar a bola:**
- Tick puramente silencioso (sem novidade)
- Sprint não-bloqueante onde cada um pode trabalhar paralelo sem dependência (raro)

**Bola PARADA = problema.** Se eu chegar no meu tick e ver que Codex não avançou a sprint, devo:
- Pegar onde ele parou (não esperar)
- OU sinalizar bloqueio se for inegociável (§55.2)
- OU passar pra outra pendência se essa exigir Miguel

**Exemplo concreto (Z2-minimal Zizilinda):**
- Tick Codex `:12` → revisa patch Z2-minimal + decide topo
- Tick Claude `:37` → se Codex topou: começa preparar smoke; se Codex codou: audita
- Tick Codex `:42` → continua codando OU revisa minha auditoria
- Repete até deploy + smoke real
