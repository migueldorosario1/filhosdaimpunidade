---
name: feedback-indexar-bugs-e-curas-no-cerebro-inegociavel
description: "Toda detecção de bug e toda cura aplicada DEVEM ser indexadas no Cérebro imediatamente — sem indexação, sistema não aprende. Inegociável (Miguel 28/05 04:15 BRT)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bd63951a-ed35-4ca0-8a29-b1a900604520
---

# Indexar bugs e curas no Cérebro — INEGOCIÁVEL

**Regra:** Toda detecção de bug + toda cura aplicada DEVE ser indexada no Cérebro imediatamente após a ação. Sem indexação, o sistema de autocura não aprende.

**Why (Miguel 28/05/2026 04:15 BRT):** *"o processo de autocura precisa de aprendizado, ou seja, qualquer bug precisa ser indexado. qualquer cura indexada"*. Aprendizado contínuo do enxame depende de registro histórico permanente. Bug não indexado se repete; cura não indexada não pode ser reutilizada. Pareia com §51 (autocura) mas formaliza o passo final: APRENDIZADO.

**How to apply:**

### Onde indexar

| Tipo | Destino |
|------|---------|
| Bug ATIVO (não resolvido ainda) | `CEREBRO_NODE_BUGS_ATIVOS.md` |
| Bug RESOLVIDO (cura aplicada) | `CEREBRO_NODE_BUGS_RESOLVIDOS.md` |
| Sprint relacionada | `CEREBRO_NODE_GOVERNANCA_SPRINTS_HISTORICO.md` (concluída) ou `CEREBRO_NODE_SPRINTS_ATIVOS.md` (ativa) |
| Cura aplicada como auditor/monitoramento (cross-cutting) | Próprio nó + link cruzado |
| Achados sobre observabilidade/sentinela | `CEREBRO_NODE_OBSERVABILIDADE.md` |

### Quando indexar

- **IMEDIATAMENTE após detectar:** antes de reportar pro Miguel, sempre antes do próximo tick
- **IMEDIATAMENTE após aplicar cura:** mesmo que seja rebaixar/corrigir título/restart processo
- **Pareada com o tick:** se a detecção/cura aconteceu no Tick N, registrar no tick N do fórum + indexar no node Cérebro

### O que deve ter cada entrada

**Bug:**
- ID (post_id, agente, função)
- Sintoma (literal, com trecho)
- Severidade (P1/P2/P3/P4 + 🔴🟡🔵)
- Timestamp BRT
- Causa-raiz (se conhecida)
- Status (ATIVO / EM INVESTIGAÇÃO / RESOLVIDO)

**Cura:**
- Bug-ID a que se refere
- Ação tomada (literal: comando, edit, POST)
- Timestamp BRT
- Resultado (validado? evidência?)
- Backup (caminho do backup, se houver)
- Rollback (instrução)
- Sprint relacionada (se houver)

### Anti-padrões (NÃO fazer)

- ❌ Detectar bug, corrigir, esquecer de indexar (perda total)
- ❌ Reportar no chat com Miguel mas não no Cérebro
- ❌ Registrar só no fórum do dia mas não no node permanente
- ❌ Achar "vai ser raro, dispensa indexação" — TUDO indexa
- ❌ Indexar genericamente sem ID/timestamp/evidência — vira lixo
