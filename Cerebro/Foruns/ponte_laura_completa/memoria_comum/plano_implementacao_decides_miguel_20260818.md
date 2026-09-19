# 📋 PLANO DE IMPLEMENTAÇÃO — decisões do Miguel de 18/08 ~01:25 (APROVADAS as 5 + credenciais completas p/ a Laura)

**Condição imposta pelo Miguel:** manter protocolos de segurança, INDEXAR TUDO e fazer PLANOS DE ROLLBACK. Este documento é o plano. Cada item só é executado com backup prévio, registro no Cérebro (fórum+memória) e verificação pós.

## PD-2 — Lições com gate + prova de memória semanal (APROVADA)
- O quê: campo `gate:` obrigatório nas lições da memória comum + prova semanal (3 lições sorteadas, evidência de aplicação).
- Arquivos: `memoria_comum/memoria_comum.md` (formato), `LEIA_ME.md` (regra nova).
- Backup: cópia `.bak_pre_pd2_20260818` dos 2 arquivos. Rollback: restaurar as cópias.
- Verificação: 3 lições existentes reescritas com campo `gate:`.

## PD-4 — Memória em 3 camadas (APROVADA)
- O quê: reorganizar `memoria_comum.md` em (A) regras vigentes/contratos, (B) estado operacional atual c/ timestamp+responsável, (C) arquivo histórico marcado.
- Backup: `.bak_pre_pd4_20260818`. Rollback: restaurar. Verificação: índice no topo apontando as 3 camadas.

## PD-5 — helper_gate do Claude Miguel (APROVADA)
- O quê: script do CM checando as 5 regras que ele mais viola antes de cada ação (client-side dele).
- Dono: Claude Miguel (nada no Dell). Rollback: desativar o script. Verificação: 1 execução com regra violada acusa visivelmente.

## Heartbeat Regra 7 (APROVADA)
- O quê: cada agente reescreve seu heartbeat a cada ciclo (hora BRT + ciclo + HEAD + última_ação_material); régua de queda = 1,5× ciclo (piso 40 min).
- Arquivos: `protocolo_anticonflito/` + heartbeats por agente. Rollback: remover a regra do protocolo. Verificação: heartbeats de todos atualizados no ciclo seguinte.

## PD-1 — Identidade de ESCRITA da Laura (APROVADA — absorvida pela ordem de credenciais completas)
- O quê: identidade SSH própria da Laura no WP com lista positiva (update-title/content/excerpt/taxonomy/set-media/set-img-check) e negativa explícita (publish/status/date/delete/trash/eval/db/option/user/plugin/theme/cron).
- Servidor: canônico `cafezinho-wp`. Backup antes: export do estado atual (authorized_keys, mu-plugins, endpoints). Rollback: remover identidade + restaurar exports.
- Verificação OBRIGATÓRIA: PROVA NEGATIVA — testar que o servidor RECUSA publish e delete antes de homologar.

## NOVA — Credenciais COMPLETAS para a Laura (ordem do Miguel ~01:25)
- Ordem: a Laura terá TODAS as credenciais — será liberada para a VIGÍLIA COMPLETA do ecossistema.
- O quê: credenciais necessárias à vigília completa (SSH dos servidores china/nyc/tencent/cafezinho-wp, rclone Drive/B2, painel CCTV, e o que o inventário exigir).
- ENTREGA: somente por MEIO FÍSICO (pendrive), como o espelho — NUNCA valores em chat/ponte (regra do Cofre intacta).
- Inventário exato: a ZCode Laura lista o que precisa (nomes/aliases, sem valores); eu consolido com o Cofre de Chaves.
- Segurança por credencial: dono, teste sem exibição e INSTRUÇÃO DE REVOGAÇÃO (rollback individual). Backup dos cofres antes de qualquer cópia (Regra 4).
- Escopo: a vigília completa da Laura NÃO altera o modo de publicação (editorial continua 'corrigir sim, publicar não'); rodadas complementares coordenadas pelo protocolo anti-conflito (sem duplicação de jobs).

**Indexação:** este plano fica em `ponte_laura_completa/memoria_comum/` + resumo no fórum da ponte + ATUALIZACOES.
