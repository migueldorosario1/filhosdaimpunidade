---
name: Fix R1 falso-positivo V3 observador — 2026-04-19
description: V3 estava rotulando atribuição em prosa ("segundo a Reuters", "Fonte: AFP") como [R1] citação crua. Fix em regras_vivas_auditoria.md + sys_prompt + timeout. 3+ validações empíricas OK.
type: project
originSessionId: 47c65b42-a2a7-4314-a9db-56d574d902d2
---
**Sintoma:** Desde 2026-04-18 20:30 até 2026-04-19 08:00 — 14+ detecções `🚨 Suspeito [R1] citação crua de domínio sem link HTML` em `sentinela.log`. V4 escalava 3-5 posts/ciclo pra V3. Pandemia editorial aparente.

**Miguel reframe:** "O corretor autônomo está confundindo citações em prosa com links crus. Revisar a função que classifica citações."

**Causa raiz:** Dupla falha de prompt.
1. Sys_prompt do V3 em `agente_observador.py:93` dizia só `"citações cruas de web search (markdown bruto)"` — ambíguo.
2. R1 do `Outros/regras_vivas_auditoria.md` era afirmação negativa ("link HTML não é citação crua"), que o LLM invertia pra "sem HTML é citação crua".

**Fix aplicado 2026-04-19 08:38 BRT:**

**A) `Outros/regras_vivas_auditoria.md`** — R1 reescrita como afirmação positiva:
> Citação crua é APENAS markdown literal bruto do tipo `([dominio.com](https://...?utm_source=openai))` vazado no meio do texto... NÃO reportar: (a) link HTML `<a href>`, (b) atribuição em prosa "segundo a X"/"Fonte: Y"/"conforme a Z", (c) nome de site solto em texto corrente.

**B) `agente_observador.py:93`** — sys_prompt explícito:
> citações cruas (= APENAS markdown literal vazado como '([site.com](https://...))' no meio do texto — NÃO confundir com 'segundo a Reuters', 'Fonte: AFP', 'conforme a X', que são atribuição em prosa CORRETA)

**C) Timeout V3** elevado `30s → 60s` em `agente_observador.py:415` — compensa picos do `controle.ocafezinho.com` (ver memória sobre servidor lento).

**Validação empírica:** V3 rodou 4 ciclos consecutivos pós-fix (09:30, 10:00, 10:30, 11:30 BRT) com **0 suspeitos flagados**. V4 ciclo 10:17 escalou 0 divergentes (antes 3-5).

**Backups preservados:** `/root/agente_observador.py.bak_pre_r1_fix_*` e `/root/Outros/regras_vivas_auditoria.md.bak_pre_r1_fix_*`.

**Lição:** Regras afirmativas ("É apenas X") são mais robustas que negativas ("NÃO é Y"). LLM auditor pode inverter regras negativas.
