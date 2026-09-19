---
name: feedback-cutover-legado-so-apos-saude-reforma
description: "Miguel 15/06 ~01:15 BRT — a fase dual 🟦 LEGADO + 🟪 REFORMA é TRANSITÓRIA. Após confirmar saúde do REFORMA, LEGADO é DESLIGADO (cutover); só REFORMA fica ativo. O cutover NÃO é por calendário (21/06 não é deadline rígido) — é por SAÚDE CONFIRMADA. Toda migração de agente de suporte deve ser pensada com o cutover como destino final."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Cutover 🟦 LEGADO → 🟪 REFORMA — só após saúde confirmada

Miguel 15/06 ~01:15 BRT, em 2 mensagens consecutivas:

> "lembrando que é transitória. porque apos o periodo de transição, apenas a reforma ficará ativa"

> "quer dizer, a transição só vai acontecer depois de confirmada a saude da reforma"

## A regra

A convivência 🟦 [LEGADO] + 🟪 [REFORMA] é **TRANSITÓRIA**, não estado final.

Estado final = **só REFORMA**. LEGADO é DESLIGADO no cutover.

O cutover acontece **SÓ DEPOIS de saúde do REFORMA confirmada** — NÃO por calendário rígido.

## Implicações práticas

### Para migração de agentes de suporte

Cada agente migrado pra 🟪 REFORMA tem que ser **portável independente do LEGADO**:
- ❌ Não pode depender de tabelas/scripts/locks do LEGADO
- ❌ Não pode ler dados que só existem no LEGADO
- ✅ Deve ler do SQLite canário (REFORMA tem fonte própria)
- ✅ Deve escrever logs/métricas próprios
- ✅ Cutover futuro = simplesmente desligar cron LEGADO; REFORMA continua sozinho

A duplicação durante a transição é PREÇO temporário, não bagunça permanente.

### Para o que conta como "saúde do REFORMA"

Já está em [[feedback_transicao_7_dias_reforma_canonica]] (7 critérios), mas reforçar:

1. Drafts gerados consistentemente sem bloqueio
2. Auditor §53C operando (após migração)
3. Autocura V4 operando (após migração)
4. Fact-check cascata operando (AUTH-004)
5. Trib Visual com taxa aprovação razoável (≥50% após AUTH-008b + AUTH-012)
6. Zero crashes recorrentes
7. Métrica de vazão equivalente ou superior ao LEGADO em janela 2h consecutivas por ≥3 dias

Não está em "21/06" hardcoded — é **por critério**.

### Para AUTH-013 (migração agentes suporte) e similares

- Precisa de segregação clara durante transição (LEGADO vs REFORMA não duplicam decisões)
- MAS migração é **prioritária** porque sem agentes de suporte no REFORMA, cutover é impossível
- Não é "atrasar a migração", é "fazer com cuidado e portabilidade"

## Why

Miguel 15/06 ~01:15 BRT — momento de reposicionamento. No tick anterior eu havia escrito "NÃO AUTORIZADO AINDA" focando no risco da duplicação. Miguel esclareceu que sem migração, REFORMA nunca tem paridade pra cutover. Saúde antes de cutover (não calendário) também muda como avalio quando "REFORMA está pronta".

## How to apply

1. **Em ticks §53**: medir saúde REFORMA por critérios objetivos. Não falar "estamos no dia X da transição" — falar "REFORMA passou em N de 7 critérios".
2. **Em AUTHs de migração de agente**: exigir segregação durante transição + portabilidade pós-cutover (dependência zero do LEGADO).
3. **Em recomendações de prazo**: não citar 21/06 como deadline rígido — usar "quando saúde confirmada".
4. **Quando atingir saúde**: propor cutover formal pro Miguel (AUTH separada com plano de desligamento gradual do LEGADO).
5. **Logs separados sempre** — facilita cutover (deletar logs LEGADO depois sem perder REFORMA).

Relacionados: [[feedback_transicao_7_dias_reforma_canonica]] (7 critérios saúde), [[feedback_hierarquia_trindade_claude_daemon_vivo]] (autoridade técnica), [[feedback_marcacao_obrigatoria_legado_reforma_todo_comentario]] (marcação durante transição).
