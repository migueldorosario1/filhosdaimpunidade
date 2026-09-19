---
name: Fix YouTube generate_text + Crime faltando 2026-04-17
description: Corrigido NameError `generate_text` na linha 263 do agente_youtube.py (retry do Editor) e deploy do agente_crime.py que estava ausente do servidor.
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Deploy 2026-04-17 15:57 BRT. Dois bugs detectados pelo Antigravity ao auditar o enxame:

**1. YouTube — NameError: `generate_text` is not defined**
- No retry minimalista do Editor (linha 263 do agente_youtube.py, adicionado no fix de recência+JSON), chamaram `generate_text(...)` em vez de `router_gen(...)`.
- `router_gen` é o alias local de `from agente_roteador_llm import gerar_texto as router_gen` (linha 162).
- Fix: trocar `generate_text` → `router_gen`. Arquivo agora tem 4 usos consistentes (linhas 210, 263, 315, 335).
- Afetou canais 'Glenn Diesen' e 'Daniel Davis / Deep Dive' — o Editor falhou no parse inicial, caiu no retry, e aí quebrava no NameError. Próximo cron às :25 já testa.

**2. Agente Crime — script sumido do servidor**
- Cron tentava rodar `15 2,8,14,20 * * * * agente_crime.py` desde que foi cadastrado, mas o arquivo nunca existiu em `/root/`.
- Log `crime.log` tinha só "can't open file '/root/agente_crime.py'" repetido.
- Arquivo existia local (`root/agente_crime.py`, 17/04 07:44, 11410 B) — só não foi deployado.
- Fix: scp para o servidor, chmod +x, importa sem erros. Próximo run 20:15.

**Why:** Ambos apontados pelo Antigravity. O do YouTube é regressão do fix anterior do Editor (recência+JSON); o do Crime é falha de deploy clássica — criado local mas não subido.

**How to apply:** Sempre que introduzir novo helper (tipo o retry do Editor), rodar `grep -n 'nome_da_função' arquivo.py` depois pra confirmar que a chamada usa o alias correto (`router_gen` no YouTube, não `generate_text`). Pra agentes novos, após criar local sempre fazer scp + ajustar crontab no mesmo ciclo.
