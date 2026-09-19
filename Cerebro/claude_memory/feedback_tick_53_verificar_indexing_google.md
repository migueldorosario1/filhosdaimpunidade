---
name: feedback-tick-53-verificar-indexing-google
description: "A cada tick §53 do Loop Maestro Cafezinho, conferir se os posts da janela foram pingados pro Google Indexing via JSONL §93."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ad62e53a-7337-4799-84ba-ed7ccefc1122
---

🔗 **A cada tick §53, sempre verificar se os posts da janela foram pingados pro Google Indexing API.** Não é opcional — é parte integral do tick.

**Why:** Miguel pediu em 2026-06-07 ~12:30 BRT: "lembra de conferir no ticket se os posts estão indo indexados ao google". §93 (`feedback_google_indexing_api_inegociavel`) é regra inegociável — todo publish DEVE pingar Google. A verificação no tick fecha o ciclo: detecta gaps em tempo real, complementa o auditor cron e o verificador GSC.

**How to apply:**
- Toda vez que rodar um tick §53, na fase de auditoria conferir TAMBÉM o JSONL `/root/agent_data/indexing_calls.jsonl` pra cada publish da janela
- Reportar no chat (não só no relatório): X/N publishes pingados Google, Y gaps detectados
- Se gap → conferir se o agente está com `util_indexing.notificar_e_logar` no patch §93
- Se gap recorrente do mesmo agente → escalar pro Kimi/Codex

**Comando padrão no tick:**
```bash
sudo grep -E "256ABC|256DEF" /root/agent_data/indexing_calls.jsonl
# OU pegar todos os IDs da janela:
sudo tail -50 /root/agent_data/indexing_calls.jsonl | grep -E "ts_brt|status"
```

**Auditor §93 cron `*:07,37`** já faz isso retroativamente, mas o tick verifica em tempo real (detecta gap antes do auditor rodar).

Relacionado: [[feedback_google_indexing_api_inegociavel]] §93, [[feedback_tick_mostrar_correcoes_e_banco_midia]] (template anterior do tick).
