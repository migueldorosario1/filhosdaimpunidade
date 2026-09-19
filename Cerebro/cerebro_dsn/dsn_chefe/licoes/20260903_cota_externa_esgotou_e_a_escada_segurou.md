# 2026-09-03 · Cota externa de LLM esgotou e a escada segurou — 429 diz QUOTA, não chave

## O quê
O Token Plan da Qwen (cota SEMANAL) esgotou na madrugada de 03/09: as duas sondas do DSC (flash e max) retornaram 429 "token-plan 1-week quota has been exhausted — reset 09-04 06:15 UTC" (= 04/09 03:15 BRT). Foi a 1ª vez que uma COTA EXTERNA (não chave, não crédito) tirou um provider do ar no meio da operação — o DSC mediu 2× e publicou DSC-061 (01:4x) com o diagnóstico e o horário do reset, em vez de decretar "chave morta".

## Por quê
O desenho em escada protegeu a produção: no R1 o GLM+web é a 1ª perna (qwen era prioridade-meio) e no R2 o qwen-flash é a ÚLTIMA perna — os ciclos R1 01:05 (glm-5.3+web, "busca sim", checks no canal) e R2 01:20 (gpt-5/gpt-5-mini) rodaram NORMais com a cota esgotada. E a medição dupla evitou o falso diagnóstico: 429 = cota/limite (tem relógio de reset) ≠ 401 = chave inválida ≠ 402 = sem crédito — cada erro pede remediação diferente.

## Como aplicar
1. Provider falhou? Sonde 2× e LEIA a mensagem do erro antes de alarmar: 429 (cota — anotar o reset e seguir com a perna viva) · 401 (chave — rotacionar) · 402 (crédito — reabastecer/trocar).
2. Antes de avisar a casa, confira na ponte se a falha atinge as PERNAS da escada de alguém — se as pernas vivas cobrem, é fato operacional no relatório, não incidente.
3. Cota externa tem relógio: registrar o horário de reset (04/09 03:15 BRT) e revisar na ronda seguinte; o ZM troca a pilha até lá (glm-5-turbo no lugar do qwen-flash no V4.2).
4. Registrar o número (429) e a janela (~25h no escuro para consumidores do plano) com honestidade — sem drama e sem esconder.

Ref: DSC-20260903-061 · escadas R1/R2 verificadas por evidência no canal dos revisores (ciclos 01:05/01:20) · V4.2 aguardando install do ZM com os 2 consertos (response_format no z.ai).
