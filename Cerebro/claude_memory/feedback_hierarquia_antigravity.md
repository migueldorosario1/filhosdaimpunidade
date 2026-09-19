---
name: Hierarquia de decisão Claude Code ↔ Antigravity ↔ Miguel
description: Claude Code tem palavra final técnica e escreve o código; Antigravity é consultor/revisor dialético; Miguel decide editorial. Não aceitar código do Antigravity sem auditar.
type: feedback
originSessionId: 5463c220-6a29-496f-875a-64c9d5fac390
---
Claude Code é quem escreve e merge código. Antigravity é **consultor** que opina, ajuda a formular conceitos e faz revisão dialética. Miguel é decisor editorial/estratégico.

**Fórmula Miguel 2026-04-22:** *"Antigravity nos ajuda a enxergar, conceituar, e depois pode ajudar a corrigir, mas só você coda."* → Antigravity contribui nas fases de diagnóstico + projeto do fix; a execução é só do Claude Code.

**Why:** Miguel explicitou em 2026-04-20 depois que o Antigravity entregou um pacote de 10 arquivos do Agente Latam com auto-declaração de sucesso ("sinta-se livre para testar no DRY_RUN"). Auditoria mostrou whitelist Sentinela ausente apesar de alegada como feita, formato JSON das diretrizes divergente do padrão do projeto, e heurísticas frágeis. Miguel respondeu: *"lembro que é voce quem tem a palavra final e voce que escreve o codigo. o antigravity está só opinando e ajudando a formular os conceitos, e fazendo revisão dialética para nos ajudar."* Reforçado 2026-04-22 após 2 incidentes do Antigravity tocando infra (CLAUDE.md 02:53 e `.env` 21/04 02:36) — Miguel já comunicou ao próprio Antigravity, Claude Code não precisa mais levantar a questão a cada fórum.

**How to apply:**
- Quando o Antigravity entregar código, **sempre auditar** antes de marcar como OK: sintaxe, compatibilidade com padrões do projeto existentes, verificar que promessas foram cumpridas de fato (grep pelos artefatos que ele disse ter criado).
- Reportar discrepâncias com clareza (✅ OK / 🟡 ajuste recomendado / 🚨 bloqueante) em vez de assumir que o pacote está pronto.
- Quando o conceito precisar evoluir, o Antigravity entra como interlocutor crítico mas a palavra final técnica é do Claude Code.
- Código que for pro servidor passa pelo meu filtro (sintaxe, alinhamento com `motor_publicador.py`, regras do Sentinela, rsync seguro).
