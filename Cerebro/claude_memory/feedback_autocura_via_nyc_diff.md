---
name: Autocura por diff NYC — versão "pura" pra identificar regressão
description: NYC failover dormente (45.55.50.249) tem sync DELIBERADAMENTE atrasado (24-48h) pra servir de âncora pré-bug. Diff Tencent vs NYC é o jeito mais rápido de localizar regressão.
type: feedback
originSessionId: 44f2c389-881d-4335-a540-25075ea2110b
---
Quando Tencent (produção) dá erro estranho ou regressão, **diff vs NYC** é o caminho mais rápido pra identificar quando o bug entrou.

**Why:** o sync NYC `sync_nyc_leve.sh` roda 1x/dia (04:00 BRT) **DE PROPÓSITO**. Miguel atrasou pra 24-48h justamente pra que NYC sirva de **âncora "pura" pré-incidente**. Se Antigravity, Codex ou Claude introduz bug em produção, NYC ainda tem a versão estável de ontem/anteontem, e diff revela exatamente a regressão.

Funcionou em 2026-05-01: NYC tinha `motor_publicador.py:507` versão limpa de `normalizar_titulo` SEM chamada a `strip_html`. Tencent tinha versão com chamada inserida (sem definição = NameError). Diff revelou exatamente a regressão. Restaurar comportamento NYC (Opção A) foi mais seguro que adicionar band-aid (Opção B = `def strip_html`).

**How to apply:**
```bash
# Pegar arquivo NYC
ssh root@45.55.50.249 'cat /root/<arquivo>.py' > /tmp/nyc_<arquivo>.py

# Pegar Tencent
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo cat /root/<arquivo>.py' > /tmp/tencent_<arquivo>.py

# Diff focado em função problemática
diff <(grep -A10 "^def <funcao>" /tmp/nyc_<arquivo>.py) <(grep -A10 "^def <funcao>" /tmp/tencent_<arquivo>.py)

# MD5 cross-check
ssh root@45.55.50.249 'md5sum /root/<arquivo>.py'
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo md5sum /root/<arquivo>.py'
```

**Quando NÃO usar NYC como referência:**
- NYC tem >7 dias sem sync (dado fica obsoleto).
- A "regressão" é uma feature deliberada introduzida no Tencent (ex: novo agente que NYC ainda não recebeu).
- O bug é em arquivo que NYC nunca teve (ex: novo agente criado HOJE).

**Memórias relacionadas:**
- `arquitetura_nyc_backup_temporal.md` — NYC é backup temporal, não espelho.
- `sync_cingapura_nyc_correto.md` — comando rsync correto.
- `feedback_validacao_runtime_real.md` — antes de festejar fix, validar com agente real.

**Contexto histórico do atraso:**
Antes (até 2026-04-21), o sync rodava `*/5 * * * *` (5 em 5min) — gerou cobrança frenética no Tencent. Em 2026-04-21 Miguel reduziu pra 1x/dia 04:00 BRT pra:
1. Cortar custo (sync agressivo gerava transferência constante).
2. **Manter NYC como âncora pré-incidente** — versão "fresca demais" anularia o valor diagnóstico.

A janela de 24h é o sweet-spot: tempo suficiente pra um bug aparecer no Tencent + ser detectado, com NYC ainda mantendo a versão estável anterior.
