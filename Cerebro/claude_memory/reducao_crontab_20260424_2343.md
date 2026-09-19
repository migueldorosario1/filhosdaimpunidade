---
name: Crontab reduzido 2026-04-24 23:43 BRT — A/B test custos LLM
description: 7 reduções aplicadas no crontab Tencent baseadas em GA4 + custos. Baseline US$ 20.86/dia em 7003 calls. Gatilho de rollback documentado. Comparar custos amanhã/depois.
type: project
originSessionId: 3fe330c3-19fc-40ae-a8cb-5d6a13d594a3
---
## Mudanças aplicadas (Tencent + espelho local + REDUZIDO.txt)

| Job | Antes | Depois | Motivo |
|---|---|---|---|
| Maestro Editorial | `0,10,20,30,40,50` (6/h, 144 slots/dia) | `0,30` (2/h, 48 slots/dia) | maior consumidor — economia significativa |
| Coletor Trends | `20,50` (2/h) | `30` (1/h) | Maestro deu cota 0 pra trends |
| Repetidor Estatal | `20,50` (2/h) | `5` (1/h) | colidia com Maestro + corte 50% |
| Feminino | `0 8,20` (2/dia) | `0 14` (1/dia) | zero hits no top 30 GA4 |
| Analytics V9 | `45 *` (24/dia) | `45 8,12,16,20` (4/dia) | reciclagem com baixo retorno |
| China | `0 10,15` + `45 23` + `0 2,4` (5/dia) | `0 10,15` + `45 23` (3/dia) | cortou madrugada |
| Crime | `15 2,8,14,20` (4/dia) | `15 8,14,20` (3/dia) | cortou 02:15 |

## Não mexido (atenção GA4)

- **Fantástico hourly** — gera os TOP hits (NASA SR-1 42k, Xiaomi 23k, arqueologia 18k)
- **Premium 1/dia** (lula, ia, latam, sheinbaum, mercado, matriz, inflacao)
- **Sentinelas vitais** (observador, autocura, sync_nyc, sync_b2)
- **Coletores Trindade** (não publicam, alimentam banco)

## Baseline custos LLM 24/04 (pré-redução)

**Total:** US$ 20.8625 / 7003 chamadas / 11.95M tokens in / 1.05M out

**Por modelo (top):**
- gpt-5-chat-latest: US$ 9.22 (44%) / 5450 calls
- claude-sonnet-4-6: US$ 4.03 (19%) / 156 calls
- fal-ai (imagens): US$ 3.08 (15%) / 88 calls
- sonar-reasoning-pro: US$ 1.59 / 149 calls
- gpt-4o-mini: US$ 1.21 / 138 calls
- grok-4.20-reasoning: US$ 1.01 / 157 calls
- gemini-2.5-flash: US$ 0.54 / 717 calls (Tribunal Visual)

**Por tag (top):**
- master_trends_v9_auditor: US$ 4.04
- agente_comentarista: US$ 3.86 (4330 calls — verboso)
- gerador_imagem_editorial: US$ 3.08
- master_trends_v9: US$ 2.66
- sentinela_v3: US$ 1.49

Snapshot completo: `/root/agent_data/snapshot_custos_pre_reducao_20260424.json`

## 🔄 GATILHO DE ROLLBACK — voltar como estava antes

**Comando único:**
```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 \
  'sudo cat /root/crontab_backup_pre_reducao_20260424_2343.txt | sudo crontab -'
```

E também restaurar o espelho local:
```bash
cp "Projeto Cafezinho Agentes/root/crontab_server.txt.bkp-pre-reducao-20260424_2343" \
   "Projeto Cafezinho Agentes/root/crontab_server.txt"
```

**Backups preservados:**
- Tencent: `/root/crontab_backup_pre_reducao_20260424_2343.txt` (vivo de antes)
- Local: `Projeto Cafezinho Agentes/root/crontab_server.txt.bkp-pre-reducao-20260424_2343`
- Local: `Projeto Cafezinho Agentes/root/crontab_LIVE_20260424_2343.txt` (snapshot puxado pré-edit)

## Comparação prevista (amanhã 25/04 23:30+)

Re-rodar o snapshot com:
```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 'sudo /root/venv/bin/python3 /tmp/snapshot_custos.py'
```
(script já está no Tencent em `/tmp/snapshot_custos.py` — pode mover pra `/root/` se quiser persistir)

Comparar `total.usd` e `por_modelo` com `snapshot_custos_pre_reducao_20260424.json`. Esperado: queda 30-40% no custo total se a redução fizer sentido.

## Validação pós-deploy

- Crontab: 176 linhas (cresceu 13 vs 163 por comentários explicativos)
- SHELL=/bin/bash ✓
- agente_observador `*/30` ✓
- agente_autocura_v4 `:17` ✓
- sync_nyc_leve dom 04h ✓
- sync_b2 diário 05h ✓
- 8 temáticos premium ✓
