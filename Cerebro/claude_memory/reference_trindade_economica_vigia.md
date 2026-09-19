---
name: trindade_economica_vigia.py — vigia autônomo §45
description: Script Python do vigia autônomo Trindade Econômica V1. Como operar, rodar, ativar/desativar, ler logs.
type: reference
originSessionId: 74d51083-651f-4cd2-8c94-a94a70f6fdcb
---
**Onde está:**
- Espelho local: `Projeto Cafezinho Agentes/root/trindade_economica_vigia.py`
- Tencent: `/root/trindade_economica_vigia.py` (MD5 `06317410ee844d72541c6e6c3ee85543`, deploy 2026-05-11 17:23 BRT)
- Helpers consultivos no Tencent: `/root/scripts/chamar_{deepseek,kimi,qwen}.py`

**Fundamento normativo:** §45 do `CEREBRO_NODE_GOVERNANCA.md` + §15 do `CEREBRO_NODE_ARQUITETURA.md` + bloco "DECISÃO FECHADA — Trindade Econômica V1" em `Foruns/forum_transicao_modelos_opus_sonnet_haiku_20260511.md`.

**Como operar:**

- **Smoke dry-run (qualquer hora):**
  ```
  ssh ... 'sudo /root/venv/bin/python3 /root/trindade_economica_vigia.py --dry-run'
  ```
- **Modo ao vivo (rebaixa post se 3/3 SIM):** trocar `--dry-run` por `--ao-vivo`. Só com autorização Miguel formal.
- **Cron sugerido (NÃO ativado por padrão):**
  ```
  */15 * * * * cd /root && /root/venv/bin/python3 /root/trindade_economica_vigia.py --dry-run >> /root/agent_data/trindade_economica.log 2>&1
  ```
- **Pausar (kill switch):**
  ```
  ssh ... 'sudo touch /root/agent_data/trindade_economica_KILL'
  ```
- **Retomar:**
  ```
  ssh ... 'sudo rm /root/agent_data/trindade_economica_KILL'
  ```
- **Log estruturado:** `/root/agent_data/trindade_economica.jsonl` (1 entry por tick + por autocura).
- **State persistente:** `/root/agent_data/trindade_economica_state.json`.

**Sinais pra subir pro Miguel/Opus/Codex:**
- `evento=GATE_OFFLINES_CONSECUTIVOS` no log → 2+ ticks com LLM offline.
- `evento=AUTOCURA_NAO_3DE3` → trio divergiu sobre rebaixar.
- `evento=WP_FAIL` → 3 retries sem HTTP 200 do WordPress.

**O que NÃO pode mudar sem novo quórum 5/5:**
- Adicionar nova ação fora do escopo permitido §45 (deploy, SSH escrita, crontab, autocura nova).
- Mudar quórum 3/3 → 2/3 sem ressalva.
- Remover kill switch ou auto-stop.
