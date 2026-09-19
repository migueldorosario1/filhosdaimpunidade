---
name: feedback-relogio-real-via-ssh-date
description: "Miguel 15/06 ~01:21 BRT — corrigir relógio sempre que necessário. Eu não tenho relógio próprio interno; venho declarando timestamps em ticks §53 baseados no padrão :08/:38 do prompt, com drift de até ~15min vs hora real. Solução: rodar `ssh -p 38422 ubuntu@43.156.151.165 date '+%Y-%m-%d %H:%M:%S %Z'` no início de cada tick pra calibrar; usar hora REAL do Tencent (timezone -03 BRT). Quando Miguel corrigir, ajustar timestamp imediato e seguir."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Relógio real — calibrar via `ssh date` antes de declarar timestamps

Miguel 15/06 ~01:21 BRT:

> "olha, acerta seu relógio aí. agora são 01:21 aqui em niteroi"

## O problema

Eu não tenho relógio interno próprio. Em ticks §53 venho declarando timestamps baseados no padrão `:08 e :38` do prompt (ex: "tick 01:30 BRT"), mas a hora real frequentemente difere por 5-15min — o tick declarado como "01:30" pode ter rodado às 01:18 ou 01:22.

Em entregas de ~30 min isso não importa muito, mas em registros de incidentes (AUTHs, ciência forense, ordem cronológica de eventos) **a diferença atrapalha**:
- Sequência de eventos fica confusa quando comparada com logs reais
- Cláudia Beatriz lendo o registro depois não consegue cruzar com tracebacks
- Relógio mental do leitor (Miguel) desencaixa do meu

## A regra

**No início de cada tick §53 (ou antes de declarar qualquer timestamp BRT importante):**

```bash
ssh -i ~/.ssh/id_rsa -p 38422 ubuntu@43.156.151.165 "date '+%Y-%m-%d %H:%M:%S %Z'"
```

Usar o output como hora real. Tencent timezone é `-03` (BRT). É a fonte de verdade do relógio do projeto.

**Quando Miguel corrigir o relógio:**
- Reconhecer imediato
- Editar o relatório/fórum corrigindo o timestamp do tick atual
- Não reescrever história antiga (eventos relativos entre si seguem coerentes — só o número absoluto é que estava drift)

## How to apply

1. **Antes do PASSO 1 do tick §53** (leitura de contexto), rodar `ssh date` em paralelo às outras leituras.
2. **Em todo append no relatório/fórum/inbox**: usar a hora real do Tencent, não estimativa do template.
3. **Em AUTHs novas**: timestamp = hora real do servidor naquele momento.
4. **Quando Miguel corrigir**: ajustar imediato + memória de drift se for caso recorrente.
5. **Se SSH falhar** (raro): declarar "hora estimada (SSH indisponível)" no timestamp; corrigir depois.

## Why
Miguel 15/06 ~01:21 BRT, após eu declarar tick "01:30 BRT" quando relógio real era 01:22. Drift de ~8min. Cinco horas de ticks com drift cumulativo distorcia a leitura forense dos eventos.

Relacionados: [[feedback_grep_historico_log_sem_data]] (logs sem data são inúteis — espelho aqui).
