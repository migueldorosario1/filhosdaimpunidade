---
name: project-trindade-reduzida-apenas-loop-laura-claude-grok-20260820
description: "Composição atual da Trindade 20/08/2026 01:01 BRT CONFIRMADA — Loop Miguel = Claude Miguel + Grok Miguel (caçadora imagens) · Loop Laura = Claude Laura + Grok Laura. ZCode/Codex Miguel e ZCode/Codex Laura OFF"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0dcfd4fe-1561-42c4-9a28-e7c51dd207b7
---

# Composição atual da Trindade (20/08/2026 00:58 BRT — Miguel)

**Ordens textuais Miguel:**
- 00:56: *"agora só temos loop laura com claude e grok ativos e voce."*
- 00:58: *"loop laura reduzido e voce aqui e o grok miguel."*
- 01:01 (confirmação final): *"loop laura é claude e grok"*

## Quem está OPERANDO agora (CONFIRMADO 01:01 BRT)

**Loop Miguel (Dell) — 2 agentes:**
- ✅ **Claude Miguel (Opus 4.7)** — eu. Cadência Vigília V6 `*/20` A/B manual (cron durable sumiu 18/08, chamada por Miguel). Publish exclusivo.
- ✅ **Grok Miguel** — RETOMADO. Escopo confirmado 01:00: **caçadora de imagens V4** (papel prévio de 17/08). Aplica thumb em drafts V4 sem `_thumbnail_id` via Wikimedia/tribunal visual; eu publico após gate PASS.
- ❌ **ZCode Miguel (DeepSeek)** — OFF
- ❌ **Codex Miguel** — OFF

**Loop Laura (Windows) — 2 agentes:**
- ✅ **Claude Laura** — ativo. Escopo SHADOW_EDITORIAL_WRITE (correções texto/título/resumo/taxonomia via `laura_ed25519`, §127 alertas obrigatórios).
- ✅ **Grok Laura** — ativo. Escopo §128 correção de imagem V4 sem burocracia (root cafezinho-wp p/ media-import + laura_ed25519 p/ set-media). Recibo `_cafezinho_img_check` continua meu.
- ❌ **ZCode Laura** — OFF
- ❌ **Codex Laura** — OFF

## Total ecossistema: 4 agentes ativos (2 por loop)

## O que muda pra mim (Claude Miguel) — implicações práticas

1. **Sou único do Loop Miguel** — sem fall-back Codex, sem caçadora ZCode. Se cair minha sessão, Loop Miguel = zero.
2. **Caçadora de imagens V4** — sem ZCode Miguel fazendo failover automático (era ele quem aplicava capa em drafts sem thumb via Wikimedia/tribunal visual). Se draft V4 novo chegar sem `_thumbnail_id`, eu preciso caçar via WebSearch Wikimedia CC (plan B já mapeado na memória 17/08 15:38).
3. **Sem sync com Codex/ZCode `*/30`** — cadência `*/20` A/B minha continua, mas não há mais alternância de ciclos ZCode :00/:30 + Codex :10/:40. Fluxo simplifica pra: só eu no Loop Miguel, cadência única.
4. **Ledger triplo (`inbox_trindade/{zcode,codex,claude}.md`)** — na prática só `claude.md` novo. Ainda leio zcode.md/codex.md por histórico, mas sem expectativa de novos alertas deles.
5. **Ponte Laura Completa** — reduzida a 3 agentes ativos (eu + Claude Laura + Grok Laura). Não espero mais mensagens ZM-/CL-Codex/XL-Codex novas. Se aparecerem, é sinal de que voltaram.
6. **Trindade Laura** — reduzida. Publish continua meu (§2 Contrato). Claude Laura mantém escopo SHADOW_EDITORIAL_WRITE (correções via `laura_ed25519`). Grok Laura mantém correção imagem sem burocracia (§128 piloto ainda ativo).
7. **Fila future=0 há tempos** — dependia de todos publicarem. Agora sou única fonte de publish do Loop Miguel. Reabastecer future por conta própria (Vigília V6 default).

## Régua sucesso 24h

Se conseguir manter cadência Vigília V6 sozinho + Grok Laura corrigindo imagens + Claude Laura corrigindo texto = operação estável. Se cair, escalar Miguel imediato ("Loop Miguel sem cobertura").

## O que NÃO muda

- Contrato Geral vigente (Emenda 5 canibalização, §126/127/128)
- Publish exclusivo Claude Miguel até Fase 2 da migração CM-007 (se Miguel confirmar)
- Helper gate v0.1 client-side (só depende de mim)
- Memória JSONL bugs + Sentinela (crons independentes)
- Regras editoriais (título ≤80, imagem check, TEMPORAL×ATEMPORAL, cutoff CHURN 2h)

## Como aplicar no próximo ciclo (Slot A 01:08)

1. Listar drafts V4 Slot A normal (cats 22/5003/30/regionais)
2. Se draft sem `_thumbnail_id`: **eu mesmo caço** via WebSearch Wikimedia CC + verifico + grava `_cafezinho_img_check`
3. Sem esperar ZCode/Codex — publish direto quando gate PASS
4. Reportar como sempre + registrar "Loop Miguel single-agent" no bug JSONL

## Refs

- [[project-cadencias-trindade-20260817]] (composição prévia, agora superada)
- [[project-laura-grok-operacao-sem-burocracia-20260818]] (Grok Laura continua ativo)
- [[project-laura-escopo-ampliado-corrigir-sim-publicar-nao-20260818]] (Claude Laura continua ativo)
- [[reference-ponte-laura-completa-20260817]] (ponte reduzida a 3 agentes)
