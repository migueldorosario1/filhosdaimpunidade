# 📅 Inventário das automações (tarefas agendadas) do ZCode do Dell

**Gerado em:** 17/08/2026 — ZCode/DeepSeek, a pedido do Miguel ("no arquivo tem as memórias das tarefas agendadas?").

**Por que este arquivo existe:** as automações em si (os cron jobs do ZCode) **NÃO migram** para a Laura — elas são **por máquina**: se a Laura as tivesse, dispararia os MESMOS jobs do Dell em duplicidade (relatórios em dobro, backups em dobro, concorrência no WordPress). Este inventário é a **memória descritiva** das tarefas: a Laura conhece o que existe, quando roda e quem é responsável — e, se um dia precisar **assumir** uma tarefa (failover), encontra o runbook completo no Cérebro.

> ⚠️ Os prompts integrais das automações não vão neste pacote (são enormes e contêm detalhes operacionais de cada máquina/servidor). O conhecimento completo de cada tarefa está no Cérebro: fóruns + memórias + manuais (ex.: `Cerebro/Memorias/manual_agentes_youtube_operacao_20260816.md`).

## Automações ativas no workspace do Dell (fonte: CronList em 17/08/2026)

| # | Automação | Agenda | O que faz (resumo) |
|---|---|---|---|
| 1 | **CCTV — saúde do painel + relatório Telegram** (`automation-e3465bb3`) | `0 2,6,8-21,22 * * *` (8/8h) · 74 rodadas | Ronda de saúde do Painel CCTV V6 (Tencent): checa loops/publicações/audiência/erros, age em críticos (protocolo "agir antes de avisar"), vigia alertas YT-PATRULHA e envia o relatório humanizado ao Telegram do Miguel (a Ponte Telegram é exclusiva dele). |
| 2 | **Caçadora de imagens V4 + Patrulha YouTube** (`automation-e1b2d648`) | `0 * * * *` (1/1h) · 153 rodadas | Busca e aplica imagens reais/licenciadas em posts V4 sem capa (canônico + espelho cafezinho.news), com ver visual + Tribunal Visual + gate fail-close; faz a patrulha leve do agente YouTube (crons GSN/nacional/painel). |
| 3 | **Faxina de Taxonomia do Cafezinho** (`automation-a7be3a1e`) | `0 2,4 * * *` (2h/4h madrugada) · 8 rodadas | Sprint noturno de limpeza de taxonomia do WP canônico (Onda 1a: tags órfãs count=0 com validação SEO 404, máx 80/sprint, backup antes). |
| 4 | **Vigília Backup + Ponte do Claude + Baleia Azul** (`automation-647b2f13`) | `0 4,7,11,15,19,22 * * *` (4/4h dia, 6/6h noite) · ativa | Fiscal do backup total C05 + co-executor C06+ (rclone Drive/B2), ponte do Claude (inbox/canal/cartinhas), bug-buddy, e editor titular do Baleia Azul (edições 07h e 19h). |

## Crons de servidor relacionados (não são automações ZCode, mas fazem parte da rotina)

- **Ponte de imagens** — na verdade é a automação nº 2 acima.
- **Enxame de comentários** — disparador cron `*/10` no servidor NYC (agente_comentarista.py) com regra permanente: manchete de política nacional ⇒ enxame automático (kill switch financeiro por escopo).
- **Emissor do Baleia Azul** — crontab local do Dell (envio 08:00 e 20:00).
- **Sync Cérebro↔GitHub** — `sync_cerebro_to_github.py` cron `*/30` (push) + `git pull` cron `*/15` (repo cerebro-miguel).
- **Sync YouTube painel** — cron local `*/5` (sync_youtube_painel.py, caixa de entrada Tencent).
- **Backup diário do Cérebro** — cron 03:40 (B2×2, Drive×2, GitHub).

## Se a Laura precisar assumir alguma tarefa

1. Ler o fórum + memória do tema no Cérebro (Regra Nº 1).
2. Criar a automação NO ZCode DA LAURA (CronCreate) com o mesmo cron — só depois de o Dell ser desativado para aquele job (nunca os dois ao mesmo tempo).
3. Confirmar com o Miguel antes de qualquer failover de tarefa.

*Inventário descritivo — não é o banco de automações (tasks-index.sqlite), que permanece só no Dell.*
