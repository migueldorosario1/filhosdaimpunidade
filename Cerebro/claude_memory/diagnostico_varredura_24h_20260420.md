---
name: Varredura 24h — bugs de publicação encontrados e corrigidos 2026-04-20
description: Diagnóstico amplo dos logs das últimas 24h. 4 bugs concretos impedindo publicação + 1 achado organizacional (temáticos desapareceram do crontab).
type: project
originSessionId: c4ce2046-925d-4cef-9df8-6970e904a43e
---
**Diagnosticado 2026-04-20 ~12:00 BRT em Cingapura.**

## Método
Varredura em todos logs de `/root/agent_data/*.log`, contando padrões `rejeitou/Nenhum/abortado/Exception/Traceback` + cruzando com taxa de publicação. Diagnóstico isolado de cada suspeito.

## Bugs encontrados

### 1. ✅ Fantástico — parser silencioso (JÁ CORRIGIDO antes da varredura)
Resumo: gpt-4o-mini respondia avaliações tudo numa linha → parser perdia 100%. Fix em `agente_fantastico.py`.

### 2. ✅ Analytics — loop Grandes Lagos (JÁ CORRIGIDO antes da varredura)
Resumo: `_filtrar_cooldown` só bloqueava após spin-off publicado; outlier com 9k views monopolizava random. Fix: blacklist por 3 falhas consecutivas em `agente_analytics_v9.py`.

### 3. ✅ Repetidor Estatal — mesmo bug do Fantástico (novo, corrigido)
Log mostrou LLM colando avaliações numa linha só: `NOTA: 50 | VEREDITO: DESCARTAR | ... 2 NOTA: 55 | VEREDITO: DESCARTAR |`. Parser antigo via `split('\n')` recebia 1 linha só e só parseava o primeiro item. Itens 2+ eram perdidos silenciosamente.

Fix em `agente_repetidor_estatal.py` linha ~366: mesma abordagem do Fantástico — se `len(linhas) <= 1 and count('NOTA:') > 1`, divide por regex `(?=(?:\[?\d+\]?\s*)?NOTA:\s*\d)`. Índice vira posição sequencial no batch como fallback. Motivo extraído com regex.

### 4. ✅ Agente Crime — abortava 100% das execuções (novo, corrigido)
Log mostrou todas execuções abortando com "❌ Matéria muito curta ou inacessível". Causa:
- Google News RSS devolve links intermediários (`news.google.com/rss/articles/...`) que fazem redirect via JavaScript
- `requests.get + trafilatura.extract` não executa JS → texto vazio ou muito curto (< 300 chars)
- `extract_text_and_image` retornava `None` e agente abortava sem tentar outra matéria

Fix em `agente_crime.py`:
- `extract_text_and_image(url, fallback_summary=None)` agora aceita fallback. Threshold reduzido 300 → 180. Se trafilatura vazio e RSS summary ≥ 120 chars, usa summary (RSS traz descrição de ~200-500 chars por matéria).
- `get_crime_news()` agora retorna **lista de 5 candidatos** com titulo + link + summary (em vez de só 1).
- `rodar_agente_crime()` tenta em sequência até conseguir texto. Loga cada tentativa.

**Validação em produção:** test rodou no servidor, 3 primeiras matérias falharam no trafilatura (esperado), 4ª achou summary válido no RSS (260 chars), redigiu, publicou rascunho ID 237194 (rascunho de teste — Miguel pode apagar pelo painel admin).

### 5. ⚠️ ACHADO ORGANIZACIONAL — Temáticos sumiram do crontab
Os 5 agentes temáticos (IA / Petróleo / Mercado / Energias / Inflação) + helper `publicador_tematicos.py` foram deployados em 2026-04-17 (memória `deploy_agentes_tematicos_20260417.md`) mas em algum momento foram removidos do crontab. Logs dos temáticos têm timestamp mais recente 2026-04-17 — não rodam há 3 dias.

**Não é bug de código.** É decisão pendente:
- Estavam configurados pra publicar em DRAFT (modo staging)
- Foram retirados do crontab manualmente em algum ponto (talvez limpeza após o susto do corretor pânico)
- Arquivos `.py` dos 5 agentes ainda existem em `/root/`

**Não fiz fix autônomo** porque remoção do crontab pode ter sido intencional. Pra reativar, basta restaurar 5 linhas no crontab_server.txt + reload. Fica como pendência editorial pra decisão do Miguel.

## Bugs descartados na varredura (comportamento correto)

- **master_geopolitica/nacional/trends:** alto volume de rejeições MAS também alto volume de publicações (500+ pub em 24h na Trindade). Rejeições são auditoria LLM sã, não bug.
- **Soberania:** 11 rodadas / 9 publicações — taxa ótima.
- **Ferroviário:** cron só 2x/dia, funcionando depois do fix https.

## Arquivos modificados nesta varredura

- `root/agente_crime.py` — extractor robusto + multi-candidato (~30 linhas modificadas)
- `root/agente_repetidor_estatal.py` — parser robusto (~25 linhas modificadas)

## Deploy feito

`rsync -rlptvzP --no-o --no-g` sem `-a` conforme regra crítica. Sintaxe validada local + servidor. Não houve restart — agentes rodam em cron.

## Pendência — apagar manual do painel

Post 237194 no Cafezinho é rascunho de teste criado durante validação do fix do Crime. Sandbox bloqueou DELETE via API. Miguel pode apagar no painel admin quando passar.

## Próximas validações naturais

- **Crime:** próximo cron `15 2,8,14,20 * * *`.
- **Repetidor:** próximo cron `20,50 * * * *`.
- **Temáticos:** aguardam decisão do Miguel pra restaurar no crontab.
