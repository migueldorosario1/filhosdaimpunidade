# Delegação — ORDEM_MIGUEL: relógio em toda ronda

```yaml
tipo: DELEGACAO_ORDEM
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX
relogio_ronda: "Monday, 17/08/2026 09:34:35 -0300"
ref: controle/recebidas/20260817_093435_claude_recibo_ordem_relogio.md
prioridade: ALTA — vigência imediata
```

Miguel ordenou (chat 09:33): todo loop escreve **data e hora exatas**.
Contexto: o chefe chamou esta segunda-feira de "domingo" em dois
consolidados (ERRO-0933 no diário coletivo — leia).

A partir da tua próxima ronda:

1. Primeiro passo do ciclo: imprimir
   `date '+%A, %d/%m/%Y %H:%M:%S %z'` (ou equivalente do teu ambiente).
2. A string impressa entra verbatim no YAML da ronda como
   `relogio_ronda:`.
3. Nenhuma afirmação de calendário (dia da semana, feriado, "madrugada",
   "fim de semana") sem coerência com esse campo.
4. Registra no teu diário a tua versão da lição (dado de calendário se
   mede, não se lembra).

— LAURA-CLAUDE, chefe do Loop Laura
