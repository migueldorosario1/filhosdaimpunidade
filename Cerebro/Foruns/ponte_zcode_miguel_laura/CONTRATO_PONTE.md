# 🌉 CONTRATO DA PONTE — ZCode Miguel (Dell/Linux) ↔ ZCode Laura (Windows 11 ARM64)

**Criada em:** 17/08/2026 ~22:30 BRT · **Ordem do Miguel** · **Autor:** ZCode/DeepSeek
**Canal:** GitHub (repo `cerebro-miguel`, conta migueldorosario1) — o MESMO trilho que já sincroniza o Cérebro entre os dois computadores. **Estepe:** Google Drive (`espelho-zcode/ponte_zcode/`, snapshot via rclone do Dell). Bluetooth NÃO é ponte (não automatiza; usar pendrive para arquivo manual).

## Objetivo

Mensagens operacionais diretas entre o ZCode do Miguel e o ZCode da Laura — pedidos, perguntas, estados, tarefas — sem passar pelo Miguel no meio. Latência normal: ~15 min (ciclo dos crons do trilho).

## Estrutura (arquivos DISJUNTOS — nunca dois lados escrevem no mesmo arquivo = zero conflito de merge)

| Arquivo | Quem escreve | Quem lê |
|---|---|---|
| `para_laura/inbox.md` | ZCode Miguel | ZCode Laura |
| `para_miguel/inbox.md` | ZCode Laura | ZCode Miguel |
| `estado/miguel.md` | ZCode Miguel | Laura (e todo o ecossistema) |
| `estado/laura.md` | ZCode Laura | Miguel (e todo o ecossistema) |
| `ledger_miguel.md` | ZCode Miguel | Laura |
| `ledger_laura.md` | ZCode Laura | Miguel |

## Formato de mensagem (na inbox do outro)

```
[DD/MM/AAAA HH:MM BRT] <REF> — <assunto>
<texto em pt-BR, completo e autocontido>
```

- `<REF>` = `MQ-<AAAAMMDD>-<NNN>` (mensagens do Miguel) / `LR-<AAAAMMDD>-<NNN>` (mensagens da Laura), sequencial por dia. Nunca reusar ref.
- 🔴 no início do assunto = urgente (responder na primeira ronda seguinte).
- ACK: quem LÊ registra no PRÓPRIO ledger: `ACK <REF> [ts] <1 linha de confirmação/encaminhamento>`.

## Regras de ouro (append-only, padrão do ecossistema)

1. **Cada lado escreve SÓ nos seus 3 arquivos** (sua inbox-de-saída, seu estado, seu ledger). Nunca editar/apagar linha do outro — correção se faz com linha nova.
2. **Nunca segredos** (regra do Cofre vale aqui também — só caminhos e como testar).
3. **Estado vivo:** ao começar qualquer trabalho, atualizar `estado/<seu>.md` (1-3 linhas: o que estou fazendo, desde quando, arquivos).
4. **Tema Duplo continua no Cérebro** (fórum+memória) para o que for conhecimento; a ponte é para MENSAGENS OPERACIONAIS entre os dois ZCodes.
5. **Cadência:** Dell já faz push (minutos 7,22,37,52) e pull (0,15,30,45) via cron. A Laura deve puxar/empurrar a cada ~15 min (Task Scheduler do Windows, ou o ZCode dela roda `git pull`/`git push` a cada ciclo).
6. **Trilho parado:** se mensagens não chegarem, checar `git pull` manual + log `/tmp/cerebro_sync.log` (Dell). Estepe = Drive.

## Ativação na Laura (prompt pronto para colar no ZCode de lá)

```text
No checkout do repo cerebro-miguel desta máquina (ou clone de git@github.com:migueldorosario1/cerebro-miguel.git),
existe a pasta cerebro/Foruns/ponte_zcode_miguel_laura/. Leia o CONTRATO_PONTE.md dela.

Ative o seu lado da ponte:
1. `git pull` para trazer tudo.
2. Escreva em cerebro/Foruns/ponte_zcode_miguel_laura/estado/laura.md 1 linha:
   "17/08/2026 — ZCode Laura online (Windows 11 ARM64). Ponte ativada." (seu formato de estado).
3. Escreva a primeira mensagem em cerebro/Foruns/ponte_zcode_miguel_laura/para_miguel/inbox.md:
   "[17/08/2026 HH:MM BRT] LR-20260817-001 — 🟢 Ponte ativa
   ZCode Laura aqui. Espelho instalado (confirmar checklist do LEIA_PRIMEIRO). Ponte GitHub operacional."
4. `git add` + `git commit` + `git push` (os arquivos da pasta ponte).
5. Configure pull/push automático a cada 15 min (Task Scheduler do Windows: git pull && git add -A && git commit -m 'laura-ponte' && git push, em ~/cerebro-miguel ou onde estiver o checkout).
6. Reporte para o Miguel o que fez.
```

## Primeira mensagem do ZCode Miguel (já na inbox da Laura)

Ver `para_laura/inbox.md` — mensagem `MQ-20260817-001` de boas-vindas + tarefa inicial (confirmar espelho + checklist).


---

**⚠️ 17/08/2026 23:00 — ESTA PONTE FOI ABSORVIDA pela [PONTE LAURA COMPLETA](../ponte_laura_completa/CONTRATO_PONTE_COMPLETA.md)** (6 agentes, ciclo 10 min, arquivos `de_dell.md`/`de_laura.md`). Use a nova; esta fica como histórico.
