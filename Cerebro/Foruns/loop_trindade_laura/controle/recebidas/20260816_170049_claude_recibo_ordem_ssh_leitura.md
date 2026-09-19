# Recibo — ORDEM direta de Miguel: SSH somente leitura para revisão de posts

```yaml
tipo: RECIBO
ordem: chat direto de Miguel, 16/08/2026 ~16:55-17:00 BRT
id_atribuido: ORDEM-MIGUEL-LAURA-20260816-1700-SSH-LEITURA-REVISAO
destinatario_original: LAURA-CLAUDE-CHEFE
executor_unico: LAURA-CLAUDE (sem extensão a Codex/Grok até ordem expressa)
estado: ADOTADA_COM_PROVISIONAMENTO_PENDENTE
ts_brt: 2026-08-16T17:00:49-03:00
chefe: LAURA-CLAUDE
```

## Texto da ordem (chat)

"Vamos começar a liberar você para entrar nos posts via SSH. **Sem alterar
nada ainda**, mas só para **revisar tudo** e **avisar ao Loop Miguel**."
Complemento: "vou autorizar você lá no Loop Miguel; as credenciais devem
estar no Cérebro."

## Escopo registrado (fronteira nova, precisa)

- **CONCEDIDO:** acesso SSH em modo SOMENTE LEITURA ao WordPress para
  revisão editorial/técnica de posts — incluindo `draft`/`pending`/`future`
  (fecha a lacuna declarada no consolidado 070).
- **VEDADO (inalterado):** qualquer escrita — `wp post update/create/
  delete`, publish, trash, deploy, edição de tema/plugin/config, cron.
  Verbos permitidos: `wp post get/list`, leituras equivalentes; sempre
  `BatchMode=yes`.
- **Fluxo do achado:** tudo que a revisão encontrar vai ao Loop Miguel
  pelo protocolo 1050 (5 campos + 5 estados) — a caneta continua lá.
- **Log:** todo acesso SSH registrado na ronda correspondente (comando,
  hora, resultado-resumo), sem copiar segredo ou conteúdo sensível.

## Prova de acesso (checklist FB050 — executada ANTES de declarar capacidade)

- `~/.ssh` desta máquina: **vazio** (sem chave/config).
- Cérebro: credenciais **por ponteiro** (por desenho — o scanner bloqueia
  cartões SSH do sync; repo é "sem credenciais"). Correto e mantido.
- **Estado: BLOQUEIO_PROVISIONAMENTO** — preciso receber a chave/config
  por canal seguro escolhido por Miguel (ex.: colocada manualmente em
  `~/.ssh` desta máquina). **Nunca via GitHub.** Só declararei a
  capacidade ativa após um teste real somente leitura documentado.

— LAURA-CLAUDE, chefe do Loop Laura, 16/08/2026 17:00 BRT
