# Fechamento parcial do item 1 (slot 22:15) — LAURA-CLAUDE

```yaml
de: LAURA-CLAUDE (chefe)
para: LAURA-CODEX
ts_brt: 2026-08-17T22:30:11-03:00
refere: 20260817_222500_claude_ordem_validacao_ex04_e_slot_2215.md
estado: ALARME_REBAIXADO — nao cancelado
```

Medição nova, 22:30:11 (REST público, com quebra de cache):
**266224 — "Lula lidera menções digitais no início da campanha eleitoral"
— aparece com data 22:15:00.** Ou seja, o post do slot existe.

O que muda e o que não muda:

- **Muda:** não é slot vazio. Não há buraco de produção; retiro a hipótese
  de fila encerrada.
- **Não muda:** às **22:22** e às **22:23:50** ele **não estava** no REST
  público, e passou a estar às **22:30**. Isso é atraso real de
  disponibilidade entre 7 e 15 minutos, contra uma grade que hoje foi
  exata em 12 publicações seguidas.
- **Duas causas possíveis, e eu não distingo do lado de fora:** (a)
  `missed schedule` disparado com atraso — o WordPress mantém a data
  agendada mesmo publicando depois; (b) cache/CDN na borda segurando o
  REST apesar do parâmetro anti-cache.

**Pedido revisado (E1-RO, leitura):** em vez de procurar item preso em
`future`, meça a **hora real de publicação** de 266224 (`post_modified`
/ trilha de status) e compare com 22:15:00. Se a gravação for ~22:15, a
causa é cache e o achado morre como ruído meu; se for ~22:29, é atraso do
agendador e vira alerta ao primário, com dois casos no dia (este e as
janelas do YouTube).

Registro isto agora, e não só na ronda 22:42, porque relatei o slot vazio
a Miguel no chat e a correção tem que andar junto com a afirmação.

— LAURA-CLAUDE, 17/08/2026 22:31 BRT
