# 2026-09-03 · FAROL: humano >2x a série em leitura isolada = padrão do coletor (2ª ocorrência), não degrau

## O quê
Na 21ª leitura (14:00) o FAROL db ts 13:30 (gerado 13:55) trouxe janela 30min com 👤1.003 — mais que o DOBRO da série do dia (432-554 no meio-dia; 388-460 na manhã) e ~2,3x o ponto anterior (432@13:00). É a 2ª ocorrência do dia do mesmo padrão: às 08:00 o mesmo campo saiu em 1.012 (série 388/399) e REGREDIU para 626 na medição 08:30 — ou seja, leitura isolada inflada que volta à curva no ponto seguinte.

## Por quê
O campo online_30min_humanos do FAROL mede janela de 30 min de um coletor que às vezes consolida em rajada (crawler/backlog de sessões) — quando a leitura isolada salta >2x a série sem movimento correspondente no tripé (navegações/visitantes/LUMINA subiram em ritmo normal, não em dobro), é artefato de coleta, não público real. Declarar degrau com uma leitura assim repete o erro das 08:00/09:00 (o "pico da 08:00" que regrediu) e das 13:00 (FAROL 860 que era janela de crawler por BOTS +103).

## Como aplicar
- Leitura isolada >2x a série (humano OU bot) = suspeita de medidor, NUNCA veredito — marcar "padrão do medidor solitário, confirmo no ponto seguinte" e só declarar degrau com 2+ leituras sustentadas OU tripé movendo junto.
- Veredito humano mora no TRIPÉ (navegações + visitantes + LUMINA/GA4 coerentes), não no campo online_30min sozinho.
- Conferir a regressão na medição seguinte (ts 14:00, gerado ~14:25) antes de qualquer conclusão — a régua se paga em 30 min.
- Registrar a ocorrência no bloco + CONTEXTO_MINI (o plantão pode ser perguntado sobre o número alto).
