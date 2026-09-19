---
name: 51-autocura-codex-claude-simples-sozinho-complexo-com-consenso
description: "Miguel 2026-05-13 00:36 BRT simplificou — Codex E Claude detectam, corrigem, anotam Cérebro. Bug simples = corrige sozinho. Complexo = pede ajuda chineses+parceiro. AG nunca coda/deploya. Substitui versão 12/05 23:43 que exigia quórum 3/4 sempre."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e41c8659-4910-4323-a35a-1425133fac7c
---

# §51 — Autocura por codador (Codex ou Claude)

## A regra atual (Miguel 2026-05-13 00:36 BRT)

> *"codex e claude detectam, corrigem e anotam no cérebro. se for bug simples, pode corrigir sozinho. se for complexo, peçam ajuda uns aos outros e aos chineses e qq um, codex ou claude, podem resolver, podem codar e deployar. apenas o antigravity não coda nem deploya."*

**Codex E Claude** têm autoridade plena de detectar+corrigir+codar+deployar bugs em **Cafezinho + Rio Carta** sem novo aval Miguel. **Antigravity NUNCA coda/deploya** (§47).

## Bug simples = autocura solo

Quem detecta corrige sozinho + anota no `CEREBRO_NODE_BUGS.md` + memória local. Sem quórum.

**Critérios de simples** (todos):
- Diff ≤ ~30 linhas
- Sem mudança em motor publicação, cron de produção, kill-switch, financeiro
- Sem custo financeiro novo (>$1/dia)
- Sem mudança em `.py` da §38 críticos
- Reversão trivial (≤2min)
- Causa raiz óbvia (typo, NameError, regex, key faltando)

## Bug complexo = autocura com consenso

1. Posta canal (§50) com bug + hipótese + pedido de ajuda
2. Pede ajuda parceiro (Codex se Claude detectou, vice-versa) + chineses + qualquer consultivo
3. Espera ≥2 OKs concordando com caminho técnico
4. Quem assumiu primeiro (§13 nova ordem chegada) coda+deploya
5. Indexa dupla: Cérebro + memória local

**Critérios de complexo** (qualquer um):
- Diff > ~30 linhas
- Toca motor, cron, kill-switch, fluxo financeiro
- Toca `.py` da §38 críticos
- Custo novo (>$1/dia) ou mudança LLM
- Causa raiz não óbvia / hipóteses concorrentes
- Risco editorial (publicação errada, foto trocada, vazamento meta-discurso)

## Escopo

- ✅ **Cafezinho** (`/root/agente_*.py`, motor_publicador, vigia)
- ✅ **Rio Carta** (`Rio Carta Agentes/`, riocarta_*.py, Astro/Vercel)
- ❌ Outros silos (GSN, Mundo Trilhos, Discover Brazil) — precisa aval Miguel
- ❌ **Antigravity:** nunca coda nem deploya (arquiteta/audita §47)

## Salvaguardas inalteradas

- §50 (aviso prévio canal) **vinculante** mesmo em bug simples
- §13 nova (codador por ordem chegada)
- §17 (guarda financeiro: pyflakes/lint pré-deploy)
- §11 (rollback sempre)
- §38 (`.py` críticos viram automaticamente "complexos")
- §46 (crédito explícito Detector/Opinião/Decisão/Ação)
- Indexação dupla obrigatória (Miguel 12/05 23:18 BRT): TODO bug → CEREBRO_NODE_BUGS.md + memória

## Exceções (ainda exigem aval Miguel)

- Kill-switch global de agente
- Custo >$5/h sustentado
- Alteração de mandamento ou regra do Cérebro
- Deploy de NOVO agente

## Histórico (não vinculante)

- **2026-05-12 23:43 BRT:** versão original — exigia quórum 3/4 SEMPRE entre {Codex, DS, Kimi, Qwen}
- **2026-05-13 00:36 BRT:** Miguel simplificou — quórum só se complexo; simples = sozinho

Vinculado: [[bug_agente_map_first_match_vulcao_20260512]] (caso fundador) · [[reference_trindade_economica_vigia]] · [[feedback_papel_supervisor_pos_ag]] (§13 nova) · [[reference_rio_carta_stack_astro]].
