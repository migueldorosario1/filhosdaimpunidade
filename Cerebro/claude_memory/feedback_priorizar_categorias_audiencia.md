---
name: Pós-redução — priorizar editorias de alta audiência + qualidade dos que sobram
description: Critério editorial pós-redução 23:43 BRT 24/04 — Maestro 6→2 slots/h. Cada slot deve ir pra editoria com audiência GA4 comprovada; qualidade dos que ficam vira prioridade.
type: feedback
originSessionId: 372483cf-746c-41be-98b2-407f880fb471
---
Após a redução de 144→48 publish/dia (Maestro 6→2 slots/h, redução 24/04 23:43 BRT), Miguel deu a diretriz editorial:

> "temos que usar as categorias dos posts com mais audiência. e melhorar a qualidade dos que ficam."

**Why:** Com menos slots, cada publicação custa mais em proporção. Editorial precisa concentrar em categorias com tráfego comprovado pelo GA4 (Fantástico já roda nos top hits — NASA SR-1 42k views, Xiaomi 23k, arqueologia 18k) e elevar barra de qualidade pra quem sobreviver à fila reduzida.

**How to apply:**
- Ao avaliar score de matéria pra publicação: bônus pra categorias com histórico GA4 alto (deixar `agente_analytics_v9` informar).
- Ao escolher editoria do slot Maestro: já é GA4-driven via `maestro_editorial.py`; confirmar que pesos refletem audiência atual e não estão chumbados.
- Nas auditorias da Trindade Editorial: barra mais alta — descartar com nota mais facilmente o que era "borderline" antes.
- NÃO retomar `feedback_publicar_os_melhores.md` no sentido inverso: continua proibido guilhotinar na coleta. A diferença é que a fila final agora tem menos espaço — a guilhotina é o próprio cron reduzido.
- Não é regra rígida sobre quais editorias publicar: é vetor de priorização dentro do mecanismo do Maestro.
