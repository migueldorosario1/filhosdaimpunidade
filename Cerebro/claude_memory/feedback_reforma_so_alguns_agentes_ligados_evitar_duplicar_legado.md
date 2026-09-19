---
name: feedback-reforma-so-alguns-agentes-ligados-evitar-duplicar-legado
description: "Miguel 15/06 ~22:20 BRT — REFORMA não liga TODOS os agentes do LEGADO. Decisão deliberada de Miguel: só liga ALGUNS agentes pra evitar duplicação cross-system com o LEGADO. Atualmente (15/06 noite): apenas china + sheinbaum produzindo na REFORMA. NÃO interpretar como gargalo/bug — é estratégia editorial."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# REFORMA: só alguns agentes ligados, propositalmente

Miguel 15/06 ~22:20 BRT, em resposta a observação Daemon de que "apenas 2 agentes REFORMA produzindo (china + sheinbaum)" no relatório de drafts:

> *"eu liguei apenas alguns agentes do reforma, para não repetir o legado"*

## A regra

**REFORMA não é cópia 1:1 do LEGADO.** Miguel ativa um subconjunto controlado de agentes na REFORMA durante a fase dual pra evitar:
- Duplicação cross-system (mesma pauta saindo de china LEGADO + china REFORMA gera double-publish)
- Sobrecarga de auditor / publicador / banco mídia
- Custo LLM dobrado sem ganho editorial

## Agentes REFORMA ativos confirmados (15/06 noite)

| Agente | Status REFORMA | Status LEGADO |
|---|---|---|
| china | ✅ ATIVO | ✅ ativo (AUTH-021 reativou) |
| sheinbaum | ✅ ATIVO | ✅ ativo |
| outros (lula/latam/militar/petroleo/geopolitica/soberania/eleicoes/flavio/ia/repetidor/...) | ⏸️ desligado | ✅ ativos |

## Implicação pra Daemon

1. **NÃO flagar como anomalia** matérias REFORMA sendo só `china_*` / `sheinbaum_*` no `auditada_<agente>_<hash>` do publicador.
2. **NÃO sugerir "investigar upstream gargalo"** — não há gargalo, é design.
3. **Quando avaliar drafts REFORMA**, contexto: a maior parte do volume editorial vem do LEGADO (cron `*/10` maestro_distribuicao); REFORMA está em modo experimental controlado.
4. **Cutover REFORMA↔LEGADO** ([[feedback_cutover_legado_so_apos_saude_reforma]]) só após saúde confirmada — incluindo expansão gradual dos agentes REFORMA conforme Miguel decidir.

## Como saber quais agentes estão ativos na REFORMA

Olhar no Tencent qual cron `*/30` do `maestro_grande_reforma.py` está configurado:

```bash
ssh ... 'sudo crontab -l | grep maestro_grande_reforma'
```

Atualmente passa flag `--agentes sheinbaum,flavio_bolsonaro,militar --processar-completo --validar-fase-d` (após AUTH-019). Mas o que efetivamente CHEGA até o publicador depende de:
- Quais agentes têm coletores REFORMA ligados
- Quais têm auditor configurado
- Se há matéria pronta pra publicar quando o slot rodar

Pra mapear o real, cruzar:
- `crontab -l | grep cafezinho/portal_cafezinho` — coletores REFORMA ativos
- Banco SQLite REFORMA: `SELECT DISTINCT noticia_pronta_id LIKE 'pronta_<agente>_%'` mostra quais agentes geraram pauta hoje

## Caso fundador

15/06 22:18 BRT — Daemon listou pra Miguel "9 ciclos AUTH-026, 100% PASS, mas apenas china + sheinbaum produzindo. ⚠️ Apenas 2 agentes REFORMA produzindo. Outros agentes não estão entregando — pode valer investigar". Miguel respondeu: "eu liguei apenas alguns agentes do reforma, para não repetir o legado". Daemon interpretou como gargalo/bug; era decisão estratégica.

## How to apply

1. **Em relatórios e ticks §53 daqui pra frente:** "Distribuição REFORMA: china + sheinbaum (agentes ativos por decisão editorial Miguel)" — NÃO escrever "só 2 agentes produzindo, investigar gargalo".
2. **Em propostas de AUTH:** se for sugerir expansão de agentes REFORMA, FALAR EXPLÍCITO "Miguel quer expandir?" — não pressupor que mais agentes = melhor.
3. **Em diagnóstico de saúde REFORMA:** comparar com Lista ATIVA de Miguel, não com todos os agentes que existem no código.

## Why

Miguel 15/06 22:20 BRT, literal. Fase dual REFORMA + LEGADO é transitória ([[feedback_cutover_legado_so_apos_saude_reforma]]). REFORMA é canário em modo experimental controlado — não é "LEGADO 2.0 com todos os agentes ligados". Cada agente novo na REFORMA é uma decisão deliberada de Miguel quando ele julga que a infra REFORMA aguenta + a redação está saudável.

Relacionados:
- [[feedback_cutover_legado_so_apos_saude_reforma]] (cutover por saúde, não calendário)
- [[feedback_monitoramento_dual_legado_reforma]] (monitoramento comparativo legado vs reforma)
- [[feedback_comparacao_legado_reforma_janela_2h]] (janela curta, não 24h)
- [[feedback_marcacao_obrigatoria_legado_reforma_todo_comentario]] (sempre dizer se é 🟦 LEGADO ou 🟪 REFORMA)
