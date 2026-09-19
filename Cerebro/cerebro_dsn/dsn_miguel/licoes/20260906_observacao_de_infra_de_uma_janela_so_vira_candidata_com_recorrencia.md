# Lição 06/09/2026 (ronda 254ª DS-Dell) — Observação de infra de uma janela só vira candidata com recorrência

## O quê
Na ronda 253ª (23:02-23:06) o mirror cafezinho.news devolveu respostas vazias/timeouts em rajada no REST per-ID (400490/269275 só confirmaram na 3ª tentativa), com o canônico www.ocafezinho.com 200 ESTÁVEL nos mesmos IDs. Registrei como OBSERVAÇÃO DE INFRA (sem BUG novo), com a régua: "se repetir na 254ª, vira candidata a nota/BUG com causa provável (throttle/refresh do mirror)". Na 254ª (23:34-23:36), TODAS as leituras do mirror vieram limpas na 1ª tentativa (400490 PRESENTE, 269281 PRESENTE, série do dono PRESENTE, ausentes com corpo vazio corretos) — a observação NÃO recorreu e foi encerrada como transitória, sem BUG.

## Por quê
Uma janela única de instabilidade no medidor não é diagnóstico: pode ser throttle do mirror, refresh de cache, rede, ou ruído do próprio coletor. Se cada rajada virasse bug formal, a lista de bugs afogaria em falso positivo e o sinal verdadeiro (recorrência) se perderia. O veredito de infra mora na SÉRIE DE SLOTS + no canônico (a régua «indisponibilidade do medidor ≠ ausência do post», da ronda 230ª, reaplicada ao próprio medidor): o 504/rajada não vira 404, e observação sem recorrência é transitório, não candidata.

## Como aplicar
1. Rajada única de infra no mirror/API: registrar como OBSERVAÇÃO (sem BUG novo), anotando a janela exata, o comportamento (respostas vazias × timeouts) e o contraste com o canônico.
2. Dar 1 slot de recorrência (próxima ronda) antes de qualquer conclusão: recorreu → candidata a nota/BUG com causa provável; não recorreu → encerrar como transitória no mesmo bloco (foi o que a 254ª fez).
3. Método de leitura mantido: retry + validação do CORPO (HTTP 200 com `[]` = ausente; só corpo não-vazio conta como presente — lição da família «duas torneiras», lição 201ª).
4. Nunca transformar observação de 1 janela em alarme na ponte: alarme é para esteira/volume/produção com causa operada; infra de medidor se vigia em silêncio e se encerra com registro.
