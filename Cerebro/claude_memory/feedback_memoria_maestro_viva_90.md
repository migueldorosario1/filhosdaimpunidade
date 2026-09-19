---
name: feedback-memoria-maestro-viva-90
description: §90 Cérebro — Memória Maestro Viva (janela 3h) + memórias provisórias por agente. Ordem direta Miguel 27/05 01:52 BRT.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a1ff8306-b098-4c3f-ab5e-8b9d269295bb
---

Claude Maestro mantém `memoria_maestro_viva.md` (raiz projeto Cafezinho) como índice central de TODAS as ações em tempo real. Janela de 3h, backup automático do que sai da janela em `Backups/memoria_maestro/`.

**Why:** Computador de Miguel travou 27/05 01:30 BRT e quase perdemos contexto de 6h de sprint. Sistema garante reconstrução em 30 segundos.

**How to apply:** A cada ação relevante (deploy, diagnóstico, voto, sprint, bug, decisão), registrar entrada na memória Maestro. Ao iniciar sessão, mover entradas >3h para backup. Ler as memórias provisórias dos outros agentes em `memorias_provisorias/` para coordenar. Regra inscrita como §90 em `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md`.

Relacionado: [[feedback_protocolo_backup_rollback_index_inegociavel]]
