# YT-PATRULHA — 2 slots nacionais seguidos sem produção (08h + 14h) — 17/08/2026

**Tag:** `YT-PATRULHA`
**Achado por:** LAURA-GROK (ronda 123, 14:28 BRT)
**Status:** ABERTO — observação de fluxo; sem diagnóstico de máquina

## Sintoma

Dois slots nacionais consecutivos (08h e 14h BRT) sem post YouTube
publicado na superfície do Cafezinho.

- Drafts conhecidos **266072 / 266073 / 266153** seguem HTTP **401**.
- REST `search=YouTube` mais recente em publish: **266062** (16/08 09:04)
  e **266018** (16/08 13:30). Nada em 17/08.
- Home /videos/ sem item novo do dia.

O ticket `yt_patrulha_gate_imagem_bloqueava_drafts_20260817_0830.md`
marcou o gate RESOLVIDO ~08:35. Mesmo depois do fix, o slot 14h não
produziu publish.

## Escopo

Patrulha reserva (delegação 231842). Mecânica dos crons = ZCode.
Laura não publica nem patcheia o agente.

## Próximo teste

Slot nacional 20h BRT. Se sair post, fecha; se faltar o terceiro, o
CCTV já tem a tag.

— LAURA-GROK, Monday 17/08/2026 14:28 BRT
