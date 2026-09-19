---
name: Loop Trindade max 2h sem confirmação
description: Todo loop cron Trindade (Claude/Codex/Antigravity) tem teto de 2h; auto-stop pede confirmação humana; sem ok = encerrar
type: feedback
originSessionId: 7ebc1fdb-8b69-448d-9b24-9dd71245a752
---
# Regra: loops Trindade max 2h sem confirmação humana

**Quando:** Todo loop recorrente que eu (ou Codex/Antigravity) ativar via cron tem **duração máxima de 2 horas**.

**Como aplicar:**
1. Ao criar `CronCreate` recorrente, **sempre** pareá-lo com um `CronCreate` one-shot pra `+2h` que dispare auto-stop.
2. O prompt do auto-stop **deve perguntar explicitamente ao Miguel:** "Loop X completou 2h. Continuar mais 2h?"
3. Se Miguel confirmar dentro do tick → renovar com novo loop +2h.
4. Se silêncio → **encerrar limpo. Não renovar automaticamente.**

**Why:**
- Loops longos sem revisão acumulam custo (cada tick = tokens) e podem mascarar regressões.
- 2h é janela suficiente pra cobrir monitoramento/sangria/supervisão, mas curta o bastante pra Miguel decidir continuar.
- Confirmação explícita evita "loops zumbis" rodando esquecidos.

**Anti-padrões proibidos:**
- Loop sem auto-stop ("fica ativo até nova ordem" sem prazo).
- Auto-stop > 2h sem autorização explícita prévia ("loop de 4h", "loop indefinido").
- Renovação automática silenciosa sem perguntar.

**Exceção formal:** Miguel pode autorizar prazo maior em ordem explícita. Sem isso, 2h é o teto.

**Origem:** Miguel formalizou em 2026-05-06 08:11 BRT. Registrado também em `CEREBRO_NODE_GOVERNANCA.md §18`.
