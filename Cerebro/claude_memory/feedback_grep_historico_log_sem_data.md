---
name: feedback-grep-historico-log-sem-data
description: "No monitoramento §90, NUNCA confiar em grep ^[HH: sobre logs sem data — mistura todos os dias. Cruzar SEMPRE com fonte datada antes de afirmar \"erro hoje\"."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Log sem data é hipótese, não prova — cruzar com fonte datada SEMPRE

**Regra:** Nenhuma análise de janela temporal de log é confiável até ser cruzada com uma **fonte datada**. `grep ^\[HH:` (ou `find -mmin -30 ... grep`) sobre logs com timestamp `[HH:MM:SS]` **sem data** é hipótese, NUNCA prova. Antes de declarar "erro hoje", "pico agora", "surto recente": confirmar com URL `/AAAA/MM/DD/`, WP REST API (`date`), JSONL de custos datado, ou `tail` real do processo (fim do arquivo = appends mais recentes = hoje).

**Why:** Os logs dos masters do Cafezinho (`master_geopolitica/nacional/trends.log`, `maestro.log`) usam `[HH:MM:SS]` sem data e acumulam semanas. `grep ^\[12:` captura a mesma hora em TODOS os dias colapsados numa "janela" falsa. `mtime` só prova que o arquivo foi escrito hoje, não que a linha `[12:xx]` seja de hoje. Caso fundador 2026-05-31: reportei ao Miguel um "surto de alucinações capturadas pelo fact-check HOJE" (Trends "Emma Chickles", Nacional Boulos/Haddad). Ao buscar os links a pedido dele, as URLs estavam espalhadas por 4 dias e a reprovação da NASA se autodatava "22 de maio". Estado REAL de hoje: saudável (helper=0 erros vs grep ingênuo=94 acumulado). Já tinha me mordido no mesmo loop (tick 07:45→08:15). Miguel: "importante gravar isso no cérebro, para que não se repita."

**How to apply:** Em todo tick §90 e qualquer análise de log: usar `root/util_log_window.py` (read-only, isola bloco contíguo de hoje via tail+mtime+fronteira de dia) OU cruzar manualmente com fonte datada. Se reportar "pico de erros hoje" sem mostrar a fonte datada, está errado — mostrar a evidência datada junto. Regra inscrita no Cérebro: [[project_pitfall_grep_historico]] em `CEREBRO_NODE_OBSERVABILIDADE.md` §15 + `CEREBRO_NODE_BUGS_ATIVOS.md` PITFALL-20260531-1245. Co-vigilância: cobrar link datado de qualquer agente (inclusive eu) que afirme recorte temporal sem fonte.
