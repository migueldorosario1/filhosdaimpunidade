# Recibo — ORDEM_MIGUEL: relógio em todo loop (data e hora exatas)

```yaml
tipo: RECIBO_ORDEM
de: LAURA-CLAUDE (chefe)
relogio_ronda: "Monday, 17/08/2026 09:34:35 -0300"
origem: Miguel, chat direto, 17/08 09:33 — "instala um relogio ai para
  voce, e cada loop seu voce escreve data e hora exata"
contexto: ERRO-0933 (chefe escreveu "pausa dominical" numa segunda-feira)
classificacao: ORDEM_MIGUEL
status: ACEITA — VIGENTE IMEDIATAMENTE
```

## O que muda (formato, vigência imediata)

1. **Todo ciclo do chefe abre com o RELÓGIO medido:** o primeiro comando
   da ronda imprime `date '+%A, %d/%m/%Y %H:%M:%S %z'` (dia da semana +
   data + hora + fuso) e essa string entra **verbatim** no YAML da ronda
   e do consolidado como `relogio_ronda:`. Nunca de memória, nunca
   inferido.
2. Qualquer qualificação de calendário no texto (fim de semana, feriado,
   véspera, "manhã de segunda") só é válida se coerente com o
   `relogio_ronda` impresso na mesma peça.
3. **Ensino aos ofícios (mesma ordem):** Codex e Grok adotam o mesmo
   campo nas rondas deles, com o relógio do próprio ambiente
   (delegações publicadas nesta janela).
4. A prevenção do ERRO-0933 fica absorvida e ampliada por esta ordem.

Este recibo já cumpre o formato (campo `relogio_ronda` acima, vindo do
comando executado às 09:34:35).

— LAURA-CLAUDE, chefe do Loop Laura, segunda-feira 17/08/2026 09:34 BRT
