# Ordem do dono via relay pode entrar na ronda com lag de ~40 min — re-checar INBOX/git log DEPOIS de rebase

**Data:** 04/09/2026 — ronda 156º (18:30→18:40)

## O quê
O Miguel ordenou por voz a REVISÃO TOTAL do Cafezinho às 17:55, com complemento às 18:05 (relay DSH-us65). Os commits só entraram na INBOX_MIGUEL.md às 18:32:19 e 18:32:53 (da2865716 + b181c0ddb) — ~35-40 min depois da voz. As rondas 154º (18:10) e 155º (18:30) leram a INBOX no início e a ordem NÃO estava lá; a 156ª abriu como "trigger duplicado, nada novo" e só encontrou a ordem DEPOIS do rebase das 18:34, quando o commit do relay entrou na árvore.

## Por quê
Ordem por relay tem DOIS tempos: o da voz do dono (17:55) e o do commit na ponte (18:32). A INBOX é a fonte da verdade para a ronda, mas o relay (DSH-us65/sessões) pode commitar com atraso grande. Quase fechei a ronda como "absorção de trigger duplicado, sem mudanças" — sem a ordem mais importante do dia em execução.

## Como aplicar
1. Em TODA ronda, depois de QUALQUER `git pull --rebase` ou rebase mid-ronda (inclusive os de push rejeitado), re-checar: `git log origin/main --oneline -5` (procurar commits de relay/INBOX/sync novos) + `tail` da INBOX_MIGUEL.md.
2. Ordem do dono tem prioridade máxima mesmo quando entra no meio da ronda — não adiar para a próxima.
3. Verificar se os rounds anteriores realmente viram a INBOX da época (o relay pode ter entrado depois) antes de afirmar "sem msg nova".
4. Quando uma ronda abrir como "duplicado/nada novo", confirmar que o HEAD local já inclui os commits de relay mais recentes do origin.
