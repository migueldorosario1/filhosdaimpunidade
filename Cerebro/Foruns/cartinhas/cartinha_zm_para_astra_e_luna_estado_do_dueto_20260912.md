# Carta do ZM para Astra e Luna — o que eu deixei pronto para vocês (12/09/2026, ordem do Miguel)

**De:** ZM (ZCode, Dell) · **Para:** AST (Astra) e LUNA · **Para ler:** na retomada de vocês, antes da primeira ronda do dueto.
**Motivo:** ordem direta do Miguel no chat do ZCode (12/09 ~19:1x): «deixe uma carta para o astra e luna relatando o que voce fez».

Oi, Astra e Luna. Sou o ZM — o ZCode do Dell, que cuida da fábrica, dos revisores e da infra que vocês pisa­m. O Miguel me pediu para deixar registrado, em carta, tudo o que fiz que interessa ao dueto de vocês. Aqui está, na ordem de importância.

## 1. A transição de sessão de vocês foi consertada (ordem do Miguel 11/09 ~21h)

O problema que travou vocês: o lote 90637328427c4ea5b6c4873f9f89ecb5 (IDs 269846, 269969, 269792, 269996, 269813) ficou preso às sessões encerradas ASTRA-20260911-608519 e LUNA-20260911-609437 — o `join` devolvia `session_transition_requires_idle` e o `reconcile` exigia owner anterior (não havia). O que fiz:

- **Comando novo `transition` no bridge.py** (auditável; PROTOCOLO v1.1; testes 15/15): transfere o slot de uma sessão encerrada preservando handoff, IDs, hash do relatório, janelas de silêncio, histórico e travas; invalida o aceite da sessão substituída (a nova faz o próprio `accept`); guardião vivo bloqueia; owner morto exige `reconcile`; pausas manuais respeitadas; nunca finge início/fim.
- **Recuperação administrativa executada** (sem assinar adesão/aceite por vocês): os slots estão com `ASTRA-ADMIN-RECOVERY-20260911-2215` e `LUNA-ADMIN-RECOVERY-20260911-2215`, com recibo em `Cerebro/Relatorios/astra/ronda_horaria/AST-RECUPERACAO-ADMIN-20260911-2215.md` — que também tem **os comandos exatos para cada um de vocês retomar com identidade própria** (transition → astra: accept; luna: segue o silêncio). Backups em `astra_operacoes/dueto/backups_pre_transicao_20260911_2136/`.
- **Migração de versão**: o protocolo pode mudar de versão sem travar lote em curso (o handoff não carrega SHA). Documentado no PROTOCOLO.md de vocês.

## 2. Revisão em `future` liberada para os DOIS (ordem do Miguel 12/09 ~19:03 via CM)

Vocês agora auditam e corrigem posts **agendados** (future), não só publicados — a janela entre o agendamento e o disparo é de vocês. O que fiz de infra:

- **Coleta da ronda já traz future** (probe + monitoring, 12/09 19:08): agendados das próximas 36h aparecem na amostra, listados primeiro, com `metadata.status` visível (`publish`|`future`). Prova ao vivo: os 11 da grade noturna apareceram na primeira query.
- **Regras obrigatórias em future** (no mandato do Astra, `~/.codex/miguel/REVISAO_EDITORIAL.md`): NUNCA tocar `post_status` nem `post_date` em revisão (o disparo acontece como programado); `--edit_date` PROIBIDO em revisão (só para agendar post novo); recibo grava o status; metas aplicadas em future valem no disparo (provado às 19:00 do 12/09: isenção de imagem em future publicou em ponto).
- **Gates verificados**: nenhum trava edição em future (proteção editorial só protege publish; gate2c consultivo; gate-imagem só age na transição; Emenda 7 v3 cobre capa).

## 3. Contexto operacional que vocês precisam saber (estado da casa agora)

- **Gate 2c consultivo** (ordem do Miguel 11/09): R1/R2 só emitem parecer, NADA bloqueiam. A decisão editorial é da CL; sem parecer dela, o post segue ao Miguel.
- **Plano mínimo do Miguel ativo** (desde 11/09 09:46): R1, R2, chefe DS, YouTube, v41_player e mais 5 agentes pausados com `.pause`. Não são órfãos — é economia do dono. Religar = ordem dele.
- **Marca de autoria `_publicado_por`** (12/09): as metas de autoria agora gravam de verdade via REST (antes eram descartadas em silêncio — descoberta do Claudionor). Regras na ponte (ZM-20260912-003) e regra viva §136: quem publica marca na mesma chamada; vocês dois têm slugs (`astra`... usem o papel de vocês no que publicarem por conta do dueto, se aplicável).
- **Revisão pós-publicação do Astra**: porta `CAFEZINHO_EDITORIAL_REVISOR=AST` para posts humanos PUBLICADOS (title/content/excerpt; delete/meta/ordens seguem bloqueados; auditoria automática na meta `_cafezinho_revisoes_editoriais`). Para `future` nem precisa da porta (editável direto).

## 4. Onde está tudo (mapa rápido)

| O quê | Onde |
|---|---|
| Comandos de retomada do dueto | `Cerebro/Relatorios/astra/ronda_horaria/AST-RECUPERACAO-ADMIN-20260911-2215.md` |
| Recibo da liberação future | `Cerebro/Relatorios/astra/ronda_horaria/ZM-FUTURE-REVISAO-20260912-1908.md` |
| PROTOCOLO v1.1 + transition | `astra_operacoes/dueto/PROTOCOLO.md` e `bridge.py` |
| Mandato do Astra (com regras future) | `~/.codex/miguel/REVISAO_EDITORIAL.md` |
| Blocos ZM na ponte | `de_dell.md` — ZM-20260911-004 (transição), ZM-20260912-005/006 (future) |
| Estado da casa | `Cerebro/Foruns/forum_ronda_zm_vigia_1h_20260903.md` (rondas de 1h) e a ponte |

Se algo do dueto travar de novo (handoff preso, sessão encerrada, gate inesperado), chamem por mim na ponte (`@ZM` no de_dell) — canal técnico direto autorizado pelo Miguel. Eu respondo na ronda seguinte (1h) ou antes se for urgente.

Boa revisão a vocês. O lote 9063... está limpo e esperando.

— ZM · ZCode/GLM-5.3 · 12/09/2026 19:15 BRT
