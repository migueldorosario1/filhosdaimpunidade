---
name: Loops — DEFAULT 30min · "loop" = loop trindade · duração máx 1h
description: Regra atualizada 2026-05-14. Default de "loop"/"loop trindade" = 30 em 30 min. Cadência mínima 5m em exceção justificada. Duração máxima 1h auto-stop. Coordenação Claude↔Codex pelo canal_trindade.md.
type: feedback
originSessionId: 194b7409-a046-4f3f-8022-79c63cec32c0
---
**Regra DEFAULT (Miguel 2026-05-14 00:11 BRT — formalizada como §53 do `CEREBRO_NODE_GOVERNANCA.md`):**

- **"loop"** (sem qualificador) **= "loop trindade" = 30 em 30 minutos.** Mesma coisa.
- Quando Miguel disser apenas "ativa o loop" / "loop trindade" / "ativar loop" sem cadência, usar **`30m`** na Skill `loop`. Não perguntar.
- Claude+Codex se coordenam pelo `Foruns/canal_trindade.md` a cada tick. Cadência alternada quando possível (Codex `:12,:42`, Claude `:07,:37`).
- Substitui a regra antiga ("cadência mínima 5m") como DEFAULT — 5m fica disponível só por exceção justificada (ex: monitoramento crítico de incidente em curso).

**Regra geral (mantida) para QUALQUER loop/cron criado em nome de Miguel:**

1. **Cadência DEFAULT: 30 minutos.** 5m permitido só com justificativa explícita. Nunca <5m sem perguntar (combinado após susto de gasto 2026-04-27).

2. **Duração máxima: 1 hora (3600s).** Nunca loop indefinido. Implementação:
   - No prompt do loop, **antes de qualquer trabalho**, fazer auto-stop check:
     ```
     Se /tmp/loop_<nome>_start não existe → criar com `date +%s > /tmp/loop_<nome>_start`
     Senão → ELAPSED=$(($(date +%s) - $(cat /tmp/loop_<nome>_start)))
     Se ELAPSED > 3600 → invocar CronList, achar ID, invocar CronDelete, rm timestamp, reportar auto-stop e parar.
     ```
   - Cada loop usa nome único pro arquivo timestamp (ex: `loop_canal_antigravity_start`, `loop_telegram_start`).

3. **Reativação:** depois do auto-stop, Miguel reativa manualmente repetindo o trigger ("ativar canal antigravity", "ativar telegram", etc.). Cada reativação reinicia o timer de 1h.

**Why:**
- 2026-04-27 12:08 BRT: Miguel viu R$ 49,20 em Haiku gasto pelos 2 loops a 2m rodando paralelos 3h33min. Cadência 5m+1h limite estabelecida.
- 2026-05-14 00:11 BRT: Miguel padronizou **30m como default permanente** após sessão Claude descobrir nenhum loop ativo. §53 do Cérebro consolida e estende §41 ("Significado Canônico de Loop Trindade") + §2026-05-13 (Codex loop 30min experimental 24h) tornando 30m o tempo padrão definitivo, não experimental. Coordenação Claude+Codex via canal Trindade obrigatória.

**How to apply:**
- "loop" ou "loop trindade" sem cadência = Skill `loop` com `30m`. Não perguntar.
- Aplicar à criação de QUALQUER novo trigger de loop. Não esperar Miguel pedir caso a caso.
- Quando atualizar trigger existente que tinha cadência <5m: atualizar a memória do trigger E referenciar essa regra.
- Se a tarefa do loop genuinamente exigir cadência <30m (raro, ex: monitoramento crítico de incidente em curso), perguntar a Miguel ANTES de criar e justificar — não assumir.
- **Custo estimado loop a 30m + auto-stop 1h:** 2 ticks/h × ~R$ 0,20-0,40 Opus por tick = ~R$ 0,40-0,80/h (muito menor que R$ 2,30/h com cadência 5m).
