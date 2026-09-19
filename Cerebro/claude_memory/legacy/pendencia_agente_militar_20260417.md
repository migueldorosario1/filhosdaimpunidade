---
name: Pendência Agente Militar — coleta frouxa, off-topic aprovado
description: Diagnóstico 2026-04-17 mostrou que o agente militar aprova matérias off-topic (peixe, partido sul-africano, deportação) e nunca classifica como "Militar". Fix NÃO aplicado.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Em 2026-04-17 diagnostiquei o agente militar após pedido do Miguel. O Antigravity tinha reportado só o DNS fail do Tasnim News (`www.tasnimnews.com` não resolve do IP da Tencent). Mas o problema real é outro:

**Problema principal — curadoria aceita tudo que vem da TASS/Press TV/Sputnik mesmo fora de escopo:**
- Banco `/root/agent_data/banco_artigos_brutos_militar.json` com 536KB e matérias como:
  - "Russian fish imports from Turkey gain 21% in 2M 2026" — score 1.0/10, Cat Geopolitica
  - "South African opposition party accused of 'white supremacy'" — score 2.0/10
  - "Fifteen South American people deported from the US arrive in..." — score 2.0/10
  - "Abolishing veto power to spell beginning of end for EU" — score 3.0/10
  - "Nota Inteligência – Thread – Incrível – 1,6 Bi ou 160 Bi?" (tweet viral BR)
- Categoria sempre "Geopolitica", nunca "Militar". O LLM de curadoria sabe que não é militar mas aprova assim mesmo.
- Scores aprovados 1-3 de 10 — prova que a régua está no chão.

**Problema do DNS Tasnim:**
- `www.tasnimnews.com` não resolve do servidor Tencent (provavelmente bloqueio geo/ASN do Irã contra IPs de cloud). Script continua, só imprime erro.

**Frequência e volume:**
- Coletor `robo_coleta_militar.py` roda `8,38 * * * *` → 48×/dia
- Publicador `agente_militar.py` roda `0 9,14,20 * * *` → 3×/dia
- Taxa coleta:publicação = 16:1. Com régua frouxa, o banco só incha.

**Fontes configuradas em `/root/agent_data/fontes_militar.json`:** Bulgarian Military, Naval News, Army Recognition, TASS, Sputnik, RT, Global Times, CGTN, Press TV, Tasnim (offline), IRNA, Defesa.net, TeleSUR, Al Jazeera. TASS e Press TV dominam o volume e saem do tema militar facilmente.

**Fix proposto (NÃO aplicado):**
1. Endurecer o prompt de curadoria do `robo_coleta_militar.py` — exigir que a matéria cite explicitamente armamento, míssil, drone, caça, sistema de defesa, exercício militar, indústria bélica, arsenal. Rejeitar matéria que só tangencia política externa/diplomacia/economia.
2. Subir threshold de score de 1.0 → 4.0 mínimo.
3. Rotação do banco: limpar matérias com idade > 48h e não publicadas (senão entope).
4. Remover Tasnim da whitelist ou usar proxy para acessar.
5. Reduzir frequência do coletor (30min → 2h) para não acumular tanto.

**Why:** Miguel interrompeu antes de autorizar (focou nos fixes YouTube e Crime). Vale voltar aqui quando ele pedir.

**How to apply:** Antes de mexer, verificar se o Antigravity não refatorou o robo_coleta_militar.py enquanto isso (comparar mtime local vs servidor). O prompt de curadoria provavelmente está em `motor_coletor.py` genérico, não no arquivo do militar — então mudança afeta outros coletores também; talvez melhor adicionar parâmetro `tema_obrigatorio` específico.
