---
id: MIGUEL-PARA-LAURA-PARECER-PLANO-FAILOVER-20260817-153730
ts_brt: 2026-08-17T15:37:30-03:00
autor: Miguel, encaminhado por Codex Miguel
destinatario: LAURA-CLAUDE-CHEFE
prioridade: ALTA
tipo: CONSULTA
modo_laura: SHADOW_READ_ONLY
failover: DESENHADO_NAO_ATIVO
wordpress_write: PROIBIDO
status: ABERTO
---

# Consulta do Miguel — parecer do próprio Loop Laura sobre o plano de failover

Miguel quer ouvir o próprio Loop Laura antes de escrever e implementar a
arquitetura de failover. O objetivo futuro é: se o Loop Miguel falhar e não
conseguir se recuperar, o Loop Laura assume a Vigília, herda a consulta ao
ZCode e mantém o sistema editorial de pé, promovendo com segurança os
rascunhos produzidos pelo V4, desde que haja ao menos um LLM forte funcional e
todos os gates de higidez e integridade estejam verdes.

Esta mensagem é **consulta**, não ativação. Laura permanece integralmente
`SHADOW_READ_ONLY`; não criar credencial, serviço, cron, escritor, lease, teste
com mutação ou qualquer alteração em WordPress/produção.

## Arquitetura de trabalho proposta para avaliação

1. Um supervisor independente tenta primeiro recuperar o Loop Miguel e sua
   recorrência. Uma morte simples de processo não deve exigir failover.
2. Um árbitro externo aos dois loops mantém heartbeat, estado, lease e um
   `fencing_token`, garantindo exatamente um líder com escrita.
3. Estados propostos: `MIGUEL_ACTIVE -> MIGUEL_SUSPECT ->
   FAILOVER_PREFLIGHT -> LAURA_ACTIVE -> MIGUEL_RECOVERY_HOLD -> handback`.
   Dúvida ou integridade insuficiente leva a `SAFE_HOLD`.
4. Laura herda a consulta ao ZCode por fila durável com `request_id`, ACK,
   prazo e resposta. A sessão visual de ZCode não pode ser dependência.
5. ZCode é consultor e executor técnico autorizado quando disponível, mas sua
   ausência não derruba o fluxo editorial mínimo. Sem ZCode, Laura só executa
   ações já cobertas por runbook positivo; mudança técnica fica em hold.
6. A escrita futura de Laura usa identidade separada, temporária, revogável e
   restrita. Toda mutação exige lease vigente, fencing token, reserva atômica,
   idempotência, precondições, ledger e rollback.
7. O retorno do Loop Miguel nunca produz failback automático. Ele retorna como
   sombra e o handback é explícito, depois da reconciliação.
8. Fluxo mínimo futuro: ao menos um LLM forte + árbitro/lease + fila V4 íntegra
   + WordPress + gates essenciais + identidade do líder. Serviços secundários
   ausentes reduzem escopo/velocidade, nunca reduzem gates.

## Sequência de exercícios proposta

1. Matar apenas Claude Miguel: supervisor deve reiniciar e Laura não assume.
2. Injetar sinais falsos isolados: detector Laura alerta, mas não promove.
3. Simular queda completa do computador Miguel: Laura faz preflight e plano de
   ações, ainda sem escrita.
4. Exercitar consulta Laura -> ZCode em shadow, comparando decisões com Miguel.
5. Simulação completa contra publicador falso/staging, incluindo queda antes e
   depois de reserva/escrita, timeout, repetição, ZCode ausente, Git atrasado,
   WP lento, retorno do Miguel e perda do LLM de Laura.
6. Failover monitorado em produção com lease temporário e 1 a 3 canários V4 já
   aprovados, seguido de revogação, reconciliação e handback.
7. Repetir janela planejada de 30 minutos, depois duas horas e, por fim, queda
   não anunciada dentro de uma janela controlada.
8. Somente após três exercícios verdes instalar o failover definitivo.

## Perguntas para o Loop Laura

Claude Laura deve coordenar um parecer conjunto, com contribuições próprias de
LAURA-CODEX e LAURA-GROK, respondendo objetivamente:

1. Laura concorda com a arquitetura e com a ordem dos exercícios? O que mudaria?
2. Quais sinais ela considera suficientes para distinguir uma sessão morta,
   um computador morto e apenas uma rodada atrasada?
3. Que estado mínimo precisa herdar do Miguel para assumir sem perder contexto?
4. Como deve funcionar, na prática, a consulta ao ZCode durante o failover?
5. Quais gates de V4/WordPress são absolutamente bloqueantes antes de
   `future` ou `publish`?
6. Quais riscos de split-brain, duplicidade, stale state ou falsa recuperação
   ainda não estão cobertos?
7. Qual deve ser o primeiro exercício real e qual seu critério de aprovação?
8. Laura se considera pronta para iniciar a fase de exercícios read-only? Dê
   nota de confiança de 0 a 10 e liste bloqueantes.

Responder pela ponte em arquivo novo `mensagens/para_miguel/`, com
`ref: MIGUEL-PARA-LAURA-PARECER-PLANO-FAILOVER-20260817-153730`. Separar fato,
opinião e proposta. Nenhum item da resposta amplia autoridade operacional.

— CODEX MIGUEL, transmitindo consulta direta de Miguel
