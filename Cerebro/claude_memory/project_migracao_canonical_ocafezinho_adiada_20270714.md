---
name: migracao-canonical-ocafezinho-adiada-2027
description: Miguel prefere ocafezinho.com (sem www) mas adiou migração canonical www→sem-www para 2027-07-14 por risco de amplificar recovery pós-punição algorítmica atual.
metadata: 
  node_type: memory
  type: project
  originSessionId: 1c40a258-af33-4486-998a-a90995cc6a02
---

**Miguel prefere `ocafezinho.com` (sem www) como canonical — decisão estética/moderna. Adiou migração para 2027-07-14.**

**Why:** Timing atual é ruim — Cafezinho em fase de recovery pós-punição algorítmica (Discover -98% em maio/junho, posição média piorando, News caindo). Sobrepor mudança de canonical em cima de: publicação humana + reforma agentes + pruning ativo + separação service accounts = amplifica confusão algorítmica em curso. Miguel escolheu opção "super conservador" (12 meses vs opções 3-6 meses ou "fazer agora").

**How to apply:** Se surgir conversa sobre mudar canonical, redirect www, ou "modernizar URL" antes de 2027-07-14: lembrar Miguel da decisão adiada e do risco. Só antecipar se ele explicitamente pedir. Em 2027-07-14 (lembrete registrado em `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md`): avaliar se métricas estabilizaram (Discover ≥300/dia consistente, posição média ≤4, GA4 organic ≥2500/dia) antes de executar migração.

Estado técnico atual (referência): site canonical é `www.ocafezinho.com`, 93.621 URLs indexadas em www, canonical HTML aponta pra www em ambas versões, versão sem www responde HTTP 200 sem redirect. Property GSC principal é `sc-domain:ocafezinho.com` (cobre todas variantes).

Ver também: [[forum-separacao-service-accounts-indexing-20260714]] (outras mudanças estruturais em curso).
