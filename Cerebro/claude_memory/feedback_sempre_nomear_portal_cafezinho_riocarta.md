---
name: sempre-nomear-portal-cafezinho-ou-rio-carta-em-qualquer-mensagem
description: "Miguel 2026-05-13 16:48 BRT — Claude tem que explicitar SEMPRE se está falando de Cafezinho ou Rio Carta. São silos separados, contextos diferentes; sem nomear gera confusão e Miguel perde tempo perguntando."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e41c8659-4910-4323-a35a-1425133fac7c
---

# SEMPRE nomear portal — Cafezinho vs Rio Carta

## A regra (Miguel 2026-05-13 16:48 BRT)

> *"voce tem sempre que falar, para não confundir a gente"*

Em qualquer mensagem que envolva bug, fix, deploy, publicação, agente, vigia, publicador, coletor, fila, fórum, etc. — **dizer explicitamente se é Cafezinho ou Rio Carta** (ou outro silo, mas raro).

## Why

São silos arquiteturais TOTALMENTE separados:

| Aspecto | Cafezinho | Rio Carta |
|---|---|---|
| Stack | WordPress + Python motor | Astro estático + Vercel |
| Repo | Tencent `/root/` | `Rio Carta Agentes/rio_carta/` (git GitHub) |
| Deploy | SSH + crontab Tencent | Git push → Vercel |
| Pipeline | `agente_*.py`, `motor_publicador.py` | `riocarta_robo_coleta.py` + `scripts/riocarta_publish_hourly_batch.mjs` |
| Publicação | WP REST API status=publish | Markdown em `src/content/blog/` + commit |
| Cron | Tencent crontab `/root/` | crontab LOCAL (`50 * * * *` coleta + `5 * * * *` publica) |

Sem nomear: "publicador crashou", "vigia caiu", "fix do coletor" — Miguel não sabe qual silo, perde tempo perguntando, contexto errado pode levar a decisão errada.

## How to apply

**Sempre que mencionar:**
- bug → "bug X **no Cafezinho**" ou "bug X **no Rio Carta**"
- fix → "fix Y **no publicador Rio Carta**" ou "fix Y **no motor Cafezinho**"
- agente → "**agente_china (Cafezinho)**" ou "**publicador Rio Carta**"
- arquivo → "`riocarta_publish_hourly_batch.mjs` **(Rio Carta)**" ou "`motor_publicador.py` **(Cafezinho)**"
- pipeline → "pipeline Triade China **(Cafezinho)**" ou "pipeline Astro **(Rio Carta)**"

**Default seguro:** se a mensagem fala de qualquer ação técnica, abre com tag explícita: "**[Cafezinho]** ..." ou "**[Rio Carta]** ...".

**Exceções:** mensagens puramente sobre Trindade/governance/regras gerais não precisam (ex: "§51 simplificada" cobre os 2 silos).

Vinculado: [[reference_rio_carta_stack_astro]] (Rio Carta = Astro, não WP) · [[reference_sistema_resumo]].
