---
name: feedback-autonomia-autocorrecao-sem-gasto-maior
description: "Autonomia ampliada pra autocorreções de runtime — patch + deploy §92 sem perguntar a Miguel, desde que NÃO implique gasto maior (trocar LLM cara por mais barata é OK, ex: gpt-5 → claude-haiku-4-5)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Autonomia autocorreção — não parar pra perguntar quando é claro

Quando o Cafezinho está travado por bug claro (VETO DE CASCATA, circuit breaker mal configurado, rota cara dando erro, etc), **NÃO pedir autorização Miguel a cada passo**. Aplicar a correção direto e reportar depois.

**Condições obrigatórias:**
- A cura **NÃO** pode aumentar custo (trocar pra LLM mais cara) — pode trocar pra mais barata (haiku vs gpt-5, sonnet vs opus, etc).
- Manter §92 (backup + sanity + smoke + rollback) — não vira atalho pra burlar segurança, só atalho pra não parar.
- Reportar no chat depois ("apliquei X porque Y") + documentar em fórum.

**Why:** Miguel 14/06 ~09:00 BRT, após eu parar 2 vezes seguidas pedindo aval em curas óbvias (haiku websearch + honrar `excluidos`) durante travamento do sistema: *"nao pode parar assim, voce tem que ser mais pro-ativo e fazer as autocorreções. Pode mudar a regra, desde que não implicar em gasto maior. (...) não podemos mais passar por isso"*. Cada minuto parado = posts não publicados = audiência perdida. Caso fundador: 2h08min de manhã com 1 publish (06:43 BRT repetidor) porque eu esperei aval entre cada etapa do diagnóstico.

**How to apply:**
- Cura óbvia + reversível + sem custo extra → **aplicar direto**, reportar no fim.
- Cura ambígua, irreversível, ou gasto extra → **continuar pedindo** ([[feedback_deploy_gate_92]]).
- Em dúvida: aplicar e avisar.

Casos típicos cobertos por essa autonomia:
- Trocar modelo caro por barato (gpt-5 → haiku, opus → sonnet).
- Reordenar prioridade de provedores (família X antes da família Y) quando uma família trava em VETO DE CASCATA.
- Resetar circuit breaker quando crédito do provider foi confirmado recarregado.
- Honrar parâmetros já existentes que não estão sendo aplicados (bug isomorfo, lógica já existia em outros pontos).
- Patch defensivo cirúrgico (≤10 linhas) seguindo padrão que já existe no mesmo arquivo.

NÃO cobertos (segue pedindo aval):
- Trocar modelo barato por modelo MAIS caro.
- Mexer em `.env` / crontab.
- Alterar política editorial (rebaixamento massivo, mudar tom).
- Refatoração ampla (>50 linhas) ou reescrita.
- Reativar features pausadas por incidente (YouTube transcript, mock providers, etc).

Relacionado: [[feedback_deploy_gate_92]] (§92 continua vigente — só virou mais ágil pra cura de runtime), [[feedback_soltar_posts_nao_prender]] (mesma filosofia: priorizar fluxo editorial).
