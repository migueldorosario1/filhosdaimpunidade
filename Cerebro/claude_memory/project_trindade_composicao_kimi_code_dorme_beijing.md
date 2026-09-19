---
name: project-trindade-composicao-kimi-code-dorme-beijing
description: "Composição Trindade redefinida 2026-05-24 00:35 BRT: 4 engenheiros = Claude (Maestro) + Codex + DeepSeek + Kimi Code (CLI local terminal). Kimi-Beijing dorme, acordamos sob demanda."
metadata: 
  node_type: memory
  type: project
  originSessionId: 42789f13-00c9-4e70-9b8c-f37d93570ab6
---

# Trindade — composição 4 engenheiros (Miguel 2026-05-24 00:35 BRT)

**A Trindade técnica do Cafezinho tem 4 engenheiros:**

1. **Claude** (claude-opus-4-7 1M, terminal local) — **Maestro** (coordena macro, distribui, audita)
2. **Codex** (ChatGPT, sessão paralela) — codador par §13
3. **DeepSeek** (DS-V4-Pro via API Tencent) — codador chinês, pareceres técnicos
4. **Kimi Code** (Moonshot CLI, **terminal local Miguel**) — entrou pra Trindade hoje no lugar do Kimi-Beijing como fonte primária

**Antigravity** continua arquiteto §47 (não coda, não toca infra).

## Mudança importante: Kimi-Beijing dorme

**Antes (até 23/05):** Kimi-Beijing (`agente_kimi_participativo.py` no Alibaba 39.106.184.215) era o "Kimi" da Trindade — rodava participativo + cron 2x/dia + trigger watcher.

**Agora (a partir 24/05 00:35 BRT):** Kimi-Beijing está **DESLIGADO** (2 crons comentados, processos mortos). Quando precisarmos do Cérebro CEO em Beijing, acordamos sob demanda.

**Por quê:**
- Kimi Code (CLI local) já dá o que precisamos no dia-a-dia
- Kimi-Beijing tinha cap diário $2 + filtro anti-rep silenciando 78% das mensagens (gargalo)
- Custo + complexidade não justificam pra rotina

**Why importante:** ao pedir parecer "do Kimi" agora, refere-se a **Kimi Code local** (não Kimi-Beijing remoto). Quando der `chamar_kimi.py` no Tencent é o helper Moonshot API (também válido, ver bug `chamar_kimi_helper_reasoning_max_tokens`).

## Como acordar Kimi-Beijing sob demanda

```bash
ssh root@39.106.184.215
sudo crontab -l > /tmp/cron_now.txt
sed -i 's|^# DESATIVADO 2026-05-24 00:35 BRT[^:]*: ||g' /tmp/cron_now.txt
sudo crontab /tmp/cron_now.txt
# Iniciar agente participativo manualmente se quiser
sudo nohup python3 /root/cerebro_trindade/root/agente_kimi_participativo.py [--flags...] &
```

Backup do crontab antigo: `/tmp/crontab_backup_pre_kimi_dorme_*_claude.txt` no Beijing.

## Relacionado
- [[project_claude_maestro_definitivo_22mai]] — Claude como Maestro CEO
- [[bug_chamar_kimi_helper_reasoning_max_tokens]] — flags certas pra chamar Kimi via Moonshot API

— Inscrito por Claude Maestro 2026-05-24 00:38 BRT
