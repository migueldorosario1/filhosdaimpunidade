---
name: feedback-contar-publish-por-autor-5786
description: "Métrica única de produção editorial diária é contar publish pelo autor 5786 (V4) via WP REST, não pelos ciclos do meu loop Vigília — dado que V4 é o único agente V4 hoje e é o dono do número"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7a8b86e8-615f-48dd-924d-5e86f182a869
---

**Ao reportar "quantos posts foram publicados hoje", contar SEMPRE via WP REST filtrando `author=5786` (V4 sozinho), não via meu log JSONL de ciclos.**

**Why:** Miguel corrigiu 06/08 ~22:50 BRT após eu reportar "3 publish" no fechamento do DIA (na verdade dia todo teve 47 publish no WP, 33 do V4). Motivo do meu erro: contei só os publish do meu turno da sessão (ambíguo — dá impressão que o site publicou pouco quando na verdade só a MINHA sessão foi baixa). Miguel: **"agora o v4 está sozinho com o número dele, é mais fácil monitorar"** — ou seja, o autor 5786 virou métrica única e limpa desde que não há mais múltiplos workers V4 (Sentinela publish desligado 27/07, único loop editorial V4 é Opus 4.7 sozinho + o worker V4 do lado ZCode que produz drafts).

**How to apply:**

**Comando canônico** (usar sempre no fechamento do DIA e do NOITE, e quando Miguel perguntar volume):
```python
posts = wp_get(env, '/wp-json/wp/v2/posts?status=publish&per_page=100&after=YYYY-MM-DDT03:00:00&orderby=date&order=asc')
v4 = [p for p in posts if p['author']==5786]
```
(`03:00:00` UTC = 00:00 BRT; filtro `author=` na querystring dá 404 no endpoint atual do WP, filtrar client-side)

**No relatório de fechamento incluir sempre:**
- Total publish V4 (autor 5786) do dia
- Breakdown por hora BRT (identifica gargalos: minha sessão travou? V4 caiu?)
- Cadência esperada: **2/hora estável** (comportamento medido 06/08 03-15h)
- Quando cadência cai abaixo disso, investigar: (a) V4 parou de produzir drafts? (b) meu pipeline segurou por pending de cota IA? (c) Kimi sem responder acumulou fila?

**Diagnóstico de gargalo por hora:**
- Se autor 5786 = 0 publish/h por >1h: V4 parou de produzir OU meu loop está segurando tudo em pending. Confirmar via `wp_get status=draft author=5786 <2h` (drafts elegíveis).
- Se autor 5786 = 2/h regular mas eu reporto poucos publish: o "pouco" é só do meu turno, os outros vieram de outros ciclos anteriores (madrugada NOITE ou DIA da manhã antes da retomada).

**Distinção crucial:**
- **"3 publish" do meu turno** ≠ **"33 publish" do V4 hoje**
- Sempre reportar OS DOIS quando fizer fechamento: (a) publish V4 dia todo (métrica oficial), (b) meu turno (métrica operacional pra medir eficiência do meu pipeline).

**Autores conhecidos (referência):**
- **5786 = V4** (o número que importa)
- 5470, 5787, 5780 = outros workers (não contar como V4)
- **2018 = Miguel humano via Antigravity — IGNORAR sempre no loop Vigília** (regra vigente)

**Regras irmãs:** [[feedback-loop-vigilia-opus-v5]] (loop DIA/NOITE), [[feedback-gravacao-datada-por-ciclo-e-ponte-kimi-regular]] (log datado).
