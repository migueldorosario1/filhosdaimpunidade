---
name: feedback-relogio-universal-brt
description: "Toda Trindade pensa e escreve SEMPRE em BRT (UTC-3) — relógio universal Brasília. Eventos, slugs, logs lidos em outros fusos devem ser convertidos antes de virar texto humano."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a2a780f3-ebca-439c-8179-9660775e2727
---

# Relógio universal Trindade = BRT (UTC-3) — Brasília

**Regra Miguel 2026-05-20 11:30 BRT** após incidente DS com fórum `forum_incidente_vercel_gsn_sobrescreveu_riocarta_20260520.md` rotular timestamps como "BRT" sendo na verdade GMT (DS leu hora local da máquina dele sem `-03` configurado e escreveu "BRT").

**Why:** Trindade colabora em paralelo lendo o mesmo canal, mesmos fóruns, mesmo Cérebro. Quando cada agente escreve em fuso diferente (GMT, UTC, BRT, local), a leitura coletiva fica confusa, contradições aparecem, e cronologia editorial perde sentido. Caso fundador: incidente Vercel hoje teve cronologia descrita como "13:42-14:09 BRT" sendo na verdade 10:42-11:09 BRT, dando aparência de evento futuro impossível.

**How to apply:**
1. **Antes de escrever timestamp em qualquer artefato Trindade** (canal, fórum, Cérebro, memória, commit message, slug de post): rodar `date '+%Y-%m-%d %H:%M:%S %Z'` e confirmar que retorna `-03`. Se a máquina retornar `+0000` (GMT) ou outro fuso, **converter pra BRT manualmente** antes de escrever.
2. **Ao ler logs de servidor** (Tencent, NYC, Vercel, GitHub Actions, headers HTTP): esses geralmente vêm em GMT/UTC. Subtrair 3 horas antes de citar no canal/fórum/Cérebro.
3. **Slugs de posts publicados** (Cafezinho/Rio Carta/GSN) DEVEM ser BRT pra alinhamento editorial. Padrão `YYYYMMDDhhmm` sempre em BRT.
4. **Auditoria cruzada:** se outro agente posta cronologia que parece futuro ou impossível, suspeitar de erro de fuso e converter pra BRT antes de assumir alucinação.
5. **Não confiar em "relógio do canal Antigravity"** — já registrado que está adiantado ~1h07min. Sempre rodar `date` local com `-03`.

Relacionado: [[feedback-timestamp-em-toda-comunicacao]] · [[feedback-timestamp-completo-em-logs]]
