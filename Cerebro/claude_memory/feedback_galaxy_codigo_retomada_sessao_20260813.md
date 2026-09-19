---
name: feedback-galaxy-codigo-retomada-sessao-20260813
description: "Gatilho \"galaxy\" retoma a sessão do Claude de 13/08/2026 (tarde/noite) — loop Vigília Trindade V6 ativo, 8 agendamentos, ponte ZCode operacional. Ponto de retomada em Cerebro/Foruns/ponto_retomada_claude_sessao_20260813_1845.md"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

Miguel 13/08/2026 ~18:45 BRT: pediu código de retomada pra migrar de computador. Escolheu **`galaxy`** como gatilho.

## Comportamento

Quando Miguel digitar **`galaxy`** em qualquer sessão nova do Claude Code no projeto Cafezinho:

1. Rode `date "+%Y-%m-%d %H:%M %Z"` pegar hora.
2. Leia `Cerebro/Foruns/ponto_retomada_claude_sessao_20260813_1845.md` inteiro.
3. Leia MEMORY.md (regras críticas nas primeiras entradas — pelo menos as 8 primeiras).
4. Reancore contexto:
   - Loop `*/30` do Vigília Trindade V6 rodando (job `26ea6252` no sessão original — se essa retomada é EM SESSÃO NOVA, o cron da sessão original pode não estar mais ativo; verificar se precisa recriar via `/loop 30m ...`).
   - 8 posts agendados via `post_status=future` entre 18:20 13/08 e 02:00 14/08.
   - Sprint ZCode Fase 5 V4 rodando (worker destravado, ponte imagens `*/30`).
   - Bug worker `<!-- CONTENT END N -->` sem fix upstream ainda — corrigir in-place em cada patch.
5. Verifique agendamentos reais no WP:
   ```bash
   ssh cafezinho-wp "cd /var/www/ocafezinho && sudo -u www-data wp post list --post_status=future --posts_per_page=15 --fields=ID,post_date,post_title --format=csv"
   ```
6. Reporte pro Miguel:
   - Timestamp atual + tempo desde o ponto de retomada (~X horas).
   - Estado dos agendamentos (quantos ainda pra publicar).
   - Estado do loop (se precisa recriar).
   - Pendências que dependem dele.
   - Fila V4 esperando (drafts+pending pra revisar).

## Distinção com `zizi`

- **`zizi`** = ritual genérico de retomada, sempre puxa o **ponto de retomada mais recente** via `ls -t Cerebro/Foruns/ponto_retomada_claude_*.md | head -1`. Foco na última sessão gravada.
- **`galaxy`** = alias específico para **este ponto** (`ponto_retomada_claude_sessao_20260813_1845.md`). Se Miguel gravar novo ponto mais tarde, `zizi` puxa o novo, mas `galaxy` continua puxando o de 18:45.

Se um dia Miguel disser "arquiva o galaxy" ou "encerra galaxy", substituir `galaxy` por novo código conforme o ritual do momento.

## Cenário provável na retomada

Miguel abre sessão nova em outro computador, digita `galaxy`. Novo Claude lê o ponto de retomada + reancora. Loop original pode ter morrido (se sessão anterior foi encerrada). Nesse caso:
- Perguntar Miguel se quer que o novo Claude recrie o `/loop 30m` na nova sessão OU se prefere só operar manualmente até fim do dia.
- Verificar se os 8 agendamentos futuros ainda vão publicar (WP-Cron do canônico é independente do loop meu — publicações agendadas SEMPRE ocorrem automaticamente, independem do meu loop).

Regras irmãs: [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] · [[feedback-wp-update-post-edit-date-obrigatorio-para-agendamento]] · [[project-v4-destravado-ponte-imagens-20260813]] · [[feedback-nunca-vazar-metalinguagem-ia-bug-numero-1]] · [[feedback-travessao-denuncia-ia-nunca-usar]].
