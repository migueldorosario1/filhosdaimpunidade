---
name: feedback-cura-estrutural-proativa
description: "Sempre que identificar gap ESTRUTURAL (não só editorial individual), tentar curar imediatamente + indexar Cérebro + anotar relatório §53. Não esperar Kimi/Codex."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c864c422-014f-4122-8468-216a5d32e450
---

🛠️ **Cura estrutural proativa** — sempre que identificar problema estrutural num tick §53 (não só erro editorial individual), tentar curar imediatamente. Anotar todas as curas + diagnósticos no relatório do dia.

**Why:** Miguel autorizou explicitamente 2026-06-10 00:50 BRT após ver que eu havia feito o patch §95 motor + estendido pra sobrenatural/fantastico (1ª rodada). Sobrenatural ainda quebrado, escalei pro Kimi. Miguel: "vai fazendo cura estrutural sempre, se conseguir, de qq forma anotando nos relatórios."

**How to apply:**
- Curar > esperar. Se conseguir fazer com §82 (backup+rollback+index) e §51 (≤30 linhas, sem motor/cron/financeiro CRÍTICO), faço sozinho.
- Motor é grande mas patches cirúrgicos fail-open ≤15 linhas são OK — Miguel já autorizou o §95 Camada 7 no motor (precedente).
- Cada cura: backup pré-patch com timestamp + smoke test + log explícito + entrada no relatório `relatorio_monitoramento_<YYYYMMDD>_loop53_30min.md` + atualização do Cérebro relevante.
- Diagnóstico INCOMPLETO ainda vale cura PARCIAL — instrumentar com logs pra próxima rodada isolar mais.
- Escala pro Kimi/Codex SÓ se: blast radius alto (>30 linhas), toca .env/crontab, requer LLM novo, ou requer aval pra arquitetura.

Relacionado: [[feedback_indexar_bugs_e_curas_no_cerebro_inegociavel]], [[feedback_protocolo_backup_rollback_index_inegociavel]], §51 autocura, §82 backup, §92 deploy gate (gate continua valendo — Miguel aprova mudanças grandes).
