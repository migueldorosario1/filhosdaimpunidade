---
name: feedback-worker-v4-bug-recorrente-izadora-dias-idade
description: Worker V4 tem bug recorrente na idade da Izadora Dias (PCO SP) - insiste em 27 anos (correto 31). Já corrigido 12:20 e 19:50 BRT 09/08. Verificar SEMPRE em posts com Izadora e sinalizar como padrão pra ZCode investigar prompt/base V4
metadata:
  type: feedback
---

**Regra:** todo draft V4 sobre **Izadora Dias** (candidata PCO ao governo de SP, autor 5786) precisa checagem WS obrigatória de idade — worker insiste em **27 anos** quando o correto é **31 anos** (WS: causaoperaria.org.br, jornalsete.com.br, portal PCO). Bug JÁ CORRIGIDO 2x hoje (09/08 12:20 BRT e 19:50 BRT) — worker regenera post com o mesmo defeito.

**Why:** Padrão detectado 09/08/2026:
- 12:20 BRT (ciclo 1217): post 264946 saiu com Izadora "27 anos" — corrigi via WS pra 31, salvei em `bugs_2026-08-09.jsonl`
- 19:50 BRT (ciclo 1947): mesmo post 264946 voltou a dizer "27 anos" após novo run do worker V4 (Kimi anexou foto que faltava, worker gerou nova versão do corpo com bug recorrente)

Isso sugere que o **prompt do worker V4 ou a base de conhecimento tem informação errada gravada** sobre Izadora Dias. Pode afetar outros posts sobre ela (durante campanha eleitoral 2026 vai haver muitos).

**How to apply:**
1. Todo draft V4 sobre "Izadora Dias" (grep no title/body) → verificar idade ANTES do publish → corrigir pra 31 se aparecer 27
2. **Escalar pra ZCode/Codex** via `inbox_trindade/zcode.md` com tag `[CLAUDE-BUG-WORKER-V4-IZADORA-IDADE-<timestamp>]` — pedir revisão do prompt/base do V4 vertical Regional-SP ou base de dados de candidatos
3. Regra irmã de [[feedback-transkriptor-verificar-nomes-proprios-yt-esteira]] (bug recorrente em nome próprio) e [[feedback-ceticismo-pesquisa-ficticia-worker-v4]] (worker V4 gera info fictícia recorrente)
4. Dado factual correto pra memória: **Izadora Dias, 31 anos, nascida em Barra Bonita/SP, estudante Letras USP, coordena Coletivo Mulheres Rosa Luxemburgo, ingressou PCO 2018, ex-vereadora Barra Bonita 2020, ex-candidata deputada federal 2022, integra Comitê Central Nacional PCO, chapa 2026: vice Nivaldo Orlandi, Senado Ednelson Cesaretti**
