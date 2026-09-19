---
name: gerador_fios_x — 1 linha por parágrafo no Twitter (2026-04-17)
description: O agente Twitter agora garante uma única linha por parágrafo, separados só por linha vazia. Prompt reforçado + pós-processamento determinístico.
type: project
originSessionId: 82c307d7-bd07-4c7a-8ed2-9e86b6fa4e22
---
Em 2026-04-17 Miguel pediu que o `agente_twitter.py` sempre produza **uma única linha por parágrafo** (sem quebras internas), separando parágrafos apenas com linha vazia.

**Fix (deploy 08:40, `/root/gerador_fios_x.py`):**
1. **Prompt reforçado** (linha 119 do `coletar_wikimedia_commons`... digo, do `gerar_fio_grok`): *"Formatação OBRIGATÓRIA: cada parágrafo deve ocupar UMA ÚNICA LINHA (sem quebras internas). Separe parágrafos APENAS com uma linha vazia (dois \\n seguidos). Nunca quebre a linha no meio de um parágrafo."*
2. **Pós-processamento determinístico** após o parse do JSON do Grok: para cada `item["texto"]`, faz `split("\n\n")`, remove quebras internas de cada parágrafo com `" ".join(p.split())`, rejunta com `\n\n`. Garante conformidade mesmo se o LLM desobedecer o prompt.

**Backup no servidor:** `/root/gerador_fios_x.py.bak_20260417_0840`

**Why:** Formatação consistente no feed do X — parágrafos compactos, sem wrap estranho.

**How to apply:** esse pós-processamento é **determinístico**, não depende do modelo obedecer. Se precisar trocar o formato (ex: permitir multiline internamente), ajustar ambos: prompt + pós-processamento.
