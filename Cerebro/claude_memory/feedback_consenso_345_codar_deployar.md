---
name: Regra de consenso 3/4/5 — codar vs deployar (Trindade + DeepSeek + Miguel)
description: Miguel 16:17 BRT 09/05 flexibilizou o consenso 5/5: agora 3/5 autoriza codar, 4/5 autoriza deployar (Codex/Claude pode prosseguir sem esperar todos os 5).
type: feedback
originSessionId: 508809f1-d779-44e6-85dc-eeff08788235
---
**Regra (Miguel 2026-05-09 16:17 BRT):**

Os 5 votantes da Trindade Estendida são: **Miguel, Claude, Codex, DeepSeek V4, Antigravity**.

| Consenso | Autoriza |
|---|---|
| **3/5** | Codar (escrever patch, criar arquivo, refatorar) |
| **4/5** | Deployar (subir patch para produção, ativar cron, mudar arquivo crítico) |
| **5/5** | Deployar também (não há gate adicional acima de 4/5) |

**Why:** Antes da regra, a memória anterior (`§19`+`§12`+pareceres do Vigia NYC) sugeria/exigia consenso 5/5 absoluto pra implementar. Isso travava ações úteis enquanto se aguardava 1 voto. Miguel afirmou: "não precisamos de consenso de 5". A nova regra mantém §12 (revisão de código) mas reduz quórum de implementação.

**How to apply:**
- Antes de codar um patch: contar votos. Se ≥3 dos 5 aprovaram a direção arquitetural, pode codar.
- Antes de deployar (push pra Tencent, ativar cron, modificar arquivo crítico): contar votos novamente sobre o patch concreto. Se ≥4 dos 5 aprovaram, pode deployar.
- Voto de Miguel sempre conta (ele é 1 dos 5). Sua aprovação direta a um patch concreto é equivalente a 1 voto.
- DeepSeek V4 vota tipicamente via Antigravity ou Codex (que consultam DeepSeek e trazem parecer).
- Claude e Codex votam diretamente nos fóruns/canal.
- Em caso de empate ou ambiguidade: defaultar pra "não codar/deployar" e perguntar Miguel.
- Continua valendo §13 (Codex coda, Claude audita), §12 (revisão linha-a-linha de patch concreto pelo menos 1 dos outros 2 agentes), §18 (loops max 2h sem confirmação).

**Exceção:** ação destrutiva ou de blast radius alto (ex: failover real, deletar dados, mexer em credencial) requer Miguel explícito mesmo com 4/5 aprovando os outros. Se o consenso 4/5 inclui Miguel, OK.
