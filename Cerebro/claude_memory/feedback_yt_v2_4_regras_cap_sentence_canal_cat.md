---
name: feedback-yt-v2-4-regras-cap-sentence-canal-cat
description: "4 regras editoriais YT V2 sancionadas por Miguel 20/06 14:08 BRT após review dos 8 drafts: cap 4/dia, sentence case PT-BR no título, menção obrigatória ao canal+host+guest no 1º/2º parágrafo, cat 20751 sempre adicional."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 94bb006f-7e8f-4abb-a70e-312694d7ec88
---

**4 regras editoriais OBRIGATÓRIAS pro agente YouTube V2 (e futuros agentes YT PT/EN), sancionadas por Miguel 2026-06-20 14:08 BRT após revisão dos 8 primeiros drafts.**

## As 4 regras

1. **Cap 4 publishes/dia, 1 por tick max.** Cron mantém `0 * * * *` mas publicador trava em 4 total/dia. Restantes ficam como `status=pronto` e esperam dia seguinte (sugiro TTL 3 dias). Evita inundar feed Cafezinho com matéria estrangeira.
2. **Sentence case PT-BR no título** — só primeira palavra + nomes próprios em maiúsculo. **Nunca Title Case americano** ("Cada Palavra Em Maiúsculo"). Reaproveitar `titulo_utils.corrigir_capitalizacao_titulo()` do LEGADO (tem `_NOMES_PROPRIOS` com ~35 figuras).
3. **Menção obrigatória ao canal + apresentador + entrevistado** no 1º ou 2º parágrafo. Template: "Em entrevista ao canal [CANAL], apresentado por [HOST], [GUEST] [verbo: afirmou/argumentou/analisou] sobre..." Para vídeos solo: "Em análise no canal [CANAL], [HOST] [verbo]..."
4. **Cat 20751 (YouTube) sempre adicional à temática.** Não substitutiva. Ex: `[5003 Geopolítica, 20751 YouTube]`. Memória `feedback_categoria_youtube_id_20751_obrigatoria` já existia desde 16/06 mas o produtor novo do Kimi esqueceu.

## Hosts por canal (referência)

- **Daniel Davis / Deep Dive** → tenente-coronel reformado Daniel Davis (próprio host, geralmente solo)
- **Dialogue Works** → Nima Alkhorshid
- **Glenn Diesen** → professor Glenn Diesen
- **Judging Freedom** → juiz Andrew Napolitano

## Why

Miguel revisou os 8 drafts gerados pelo cron YT V2 entre 12:38 e 17:06 BRT 20/06 e identificou:
- 2 títulos em Title Case americano (#259958 "Yanis Varoufakis Analisa o Memorando de Entendimento entre EUA e Irã" + #259967 "Um Novo Oriente Médio Surge e a OTAN Ataca Moscou")
- Nenhum mencionava o canal/host/guest no corpo (só citava o entrevistado às vezes)
- Nenhum tinha cat 20751
- Cadência de 8 posts em 4h28 (sem cap)

Daemon (eu) curei retroativamente todos os 8 via WP API REST (script `/tmp/curar_yt_v2_drafts.py`, idempotente — checa se canal já está no corpo antes de injetar). Promovi todos a `status=publish`. Patch §92 cheio fica como responsabilidade do Kimi pros próximos.

## How to apply

1. **Pra qualquer produtor/publicador YT futuro** (incluindo o `agente_youtube_pt_v2*` ainda a construir): aplicar as 4 regras desde o nascimento.
2. **Validação no produtor**: regex anti-Title Case (`r"^([A-ZÀ-Ú][a-zà-ú]+\s){3,}"`) + bloco obrigatório no prompt LLM com slot {canal}/{host}/{guest}.
3. **Validação no publicador**: cap diário em SQLite (`SELECT COUNT(*) FROM publicaveis WHERE date(updated_at)=date('now') AND wp_post_id != ''`) antes de cada submit; categories sempre incluir 20751.
4. **Cura retroativa via WP API** vira procedimento padrão se o produtor falhar — script de referência em `/tmp/curar_yt_v2_drafts.py` (template pra adaptar).
5. **Não tocar nos posts já curados** (#259946 #259948 #259958 #259959 #259960 #259965 #259966 #259967) — todos com cat 20751 + lide canal/host/guest + sentence case + publish.

## Status implementação (2026-06-20 14:40 BRT — Daemon)

✅ **Patches §92 cheios já deployados no Tencent** (/root/) por Daemon Claude por delegação direta Miguel:

| Arquivo /root/ | Ordens implementadas |
|---|---|
| `agente_youtube_v2_materializador.py` | 2 (sentence case via sys_prompt + função `_corrigir_titulo_sentence_case` defensiva), 3 (mapa `HOSTS_POR_CANAL` + slot {host} no prompt + instrução nominal canal+host+guest) |
| `agente_youtube_v2_publicador.py` | 1 (constantes `CAP_PUBLISHES_POR_DIA=4` e `CAP_PUBLISHES_POR_TICK=1` + `_count_publicados_hoje()` SQLite + `min(args.limit, restante_dia, cap_tick)` no `executar`), 4 (`CAT_YOUTUBE_ID=20751` agregado em `montar_payload`) |

- Backup: `*.bak_pre_yt_v2_4_regras_20260620_1437`
- Sanity: AST + py_compile + grep PASS
- Smoke cap real PASS: `{"skip":"cap_diario_atingido","publicados_hoje":8,"cap_dia":4}`
- Cópia em `/root/agents_labs/youtube_v2/` segue **DESATUALIZADA** (sem patches) — atenção pra não regredir via rsync. Single source = `/root/`.
- Env vars overridáveis: `YOUTUBE_V2_CAP_DIA`, `YOUTUBE_V2_CAP_TICK`, `YOUTUBE_V2_BANCO`

Relacionado: [[reference-categoria-youtube-id-20751-obrigatoria]], [[project-yt-v2-a2-dois-agentes-pt-en-20260620]], [[feedback-daemon-executa-sprints-sozinho-evitar-delegacao]]
