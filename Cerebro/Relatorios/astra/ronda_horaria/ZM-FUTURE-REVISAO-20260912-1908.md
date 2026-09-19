# ZM-FUTURE-REVISAO-20260912-1908 — autorização de revisão em `future` VIABILIZADA (ordem Miguel ~19:03 via CM)

## O que mudou (com backup e testes)

1. **Coleta da ronda (probe_wordpress.py, backup .bak_pre_future_20260912):** queries `posts` e `recent_content` agora incluem `future` até 36h à frente (future listado primeiro; recent_content ampliada para 12 itens; campo `status` em cada linha). Rankings por views seguem intocados na lógica (future não tem views).
2. **Monitoring (monitoring.py, mesmo backup):** cada artigo da amostra expõe `metadata.status` (`publish`|`future`); escopo reescrito com a regra future (revisar antes do disparo; nunca alterar status/data; recibo indica status). Testes existentes: 15/15 OK; py_compile OK.
3. **Prova ao vivo (SELECT only, a mesma query do patch):** devolveu os 11 agendados da grade noturna no topo (270325 Peruca 10:00 … 270364 Datafolha 22:26, 270341 Tarso 23:00, 270324 Gilmar 00:20, 270342 BRICS 01:00, 270328 02:20, 270358 03:00, 270327 04:30, 270255 05:45, 270326 07:00, 270256 08:30) + publish recentes.
4. **Gates verificados para future (leitura do código):** proteção editorial só protege `publish` (future editável); gate2c consultivo (não bloqueia); gate-imagem age só na transição publish (metas aplicadas em future valem no disparo — provado às 19:00 pelo CM-009: isenção em future → publicou 19:00 em ponto); Emenda 7 v3 cobre capa em qualquer status relevante.
5. **Mandato do Astra atualizado** (`~/.codex/miguel/REVISAO_EDITORIAL.md`): regra future — nunca tocar post_status/post_date; --edit_date proibido em revisão; recibo com status; metas em future valem no disparo; coleta inclui future (Luna 30/30 varre publish+future).

## O que NÃO mudou
Gates do WP (nenhum editado — apenas verificados); crons/executor/fila (nenhum criado); o protocolo do dueto (handoff segue igual); o cron novo da Luna (prompt paralelo do CM/redesenho — eu só garanti que a coleta já traga future).

## Retomada (Luna/Astra)
A próxima ronda da Luna que rodar com este probe já enxerga os future na amostra (status visível). Nenhum comando extra necessário; a revisão segue o fluxo normal (AST pela porta CAFEZINHO_EDITORIAL_REVISOR=AST para posts humanos PUBLICADOS; future é editável direto).

— ZM · ZCode/GLM-5.3 · 12/09/2026 19:08 BRT
