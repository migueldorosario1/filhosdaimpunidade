---
name: failover-nyc-rebuild-20260611-glm
description: Rebuild completo do failover NYC executado pelo GLM em 10-11/06 com quorum Trindade
metadata: 
  node_type: memory
  type: project
  originSessionId: 21db8d3d-e482-41f0-a651-2c1019db2865
---

# Rebuild Failover NYC — GLM 10-11/06/2026

**Status:** CONCLUIDO

**Quorum §92:** 4/4 engenheiros (Claude, DeepSeek, Kimi, Qwen) + Miguel autorizou.

**O que foi feito:**
1. Diagnostico completo do failover (forum_diagnostico_failover_20260610.md)
2. Carta a Trindade com plano em 6 fases (forum_carta_failover_rebuild_20260610_glm.md)
3. Rsync Cingapura→NYC com flags seguras (--no-o --no-g --exclude='.ssh')
4. Venv sincronizado via pip freeze (134 pacotes, zero diff)
5. rclone instalado no NYC + config B2 copiada
6. sync_nyc.sh IP corrigido (45.55.50.249 morto → 198.199.121.136)
7. Cron sync ajustado de semanal para 48h (0 4 * * 0,2,4,6)
8. pip mirror Tencent no NYC trocado por PyPI publico
9. 5/5 hashes identicos validados

**Pendencias nao-bloqueantes:**
- Ensaio de failover real (fim de semana com Miguel)
- P0 credenciais GitHub (se rotacionar, re-sincronizar .env)
- Reboot NYC (kernel pendente)

**Gasto Alibaba $17.17/dia identificado e corrigido:**
- Causa: contexto "economico" fazendo ~5.600 chamadas/dia ao qwen-plus (fallback de deepseek em circuit breaker)
- Correcao: alibaba movido para ultimo na cadeia de rota (depois de mistral/openai)
- Arquivo: agente_roteador_llm.py (backup: .bak_pre_alibaba_demote_20260611_0100)

**Foruns:**
- `Foruns/forum_diagnostico_failover_20260610.md`
- `Foruns/forum_carta_failover_rebuild_20260610_glm.md`
