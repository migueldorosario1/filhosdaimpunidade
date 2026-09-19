---
name: feedback-ritual-ler-memoria-toda-acao-editorial-20260815
description: Ritual de reler MEMORY.md antes de agir vale pra QUALQUER ação editorial/técnica que afete produção, NÃO só ciclos Vigília. Incidente 15/08 14:04 (helper reintroduziu regex revogado) provou que "fora do ciclo" não é desculpa.
metadata:
  type: feedback
---

## Incidente

15/08/2026 14:04 BRT: escrevi `/root/vigilia_helper.php` (gate persistente pedido pelo Codex 13:43) e **REINTRODUZI o regex amplo "fonte original|primária"** que Codex tinha pedido pra REMOVER de manhã (5h antes) porque causava falso positivo em atribuição jornalística legítima.

Bug meu meta: **não reancorei memória antes de escrever o helper.**

Meu ritual de "ler MEMORY.md top antes de cada Slot Vigília" (registrado 15/08 11:35) valia SÓ pra ciclos Vigília. Escrever helper era ação **FORA** do ciclo Vigília — foi ação disparada por ping urgente Codex. Pulei o ritual e caí no bug.

## Regra corrigida

**Ritual de reler MEMORY.md top (10 entradas) antes de agir vale pra:**
1. Início de cada Slot Vigília (já era)
2. **Antes de escrever código persistente** (helper, scripts, bibliotecas, gates)
3. **Antes de responder tickets Codex/Miguel/ZCode/Grok** que envolvam alteração técnica
4. **Antes de fazer publish direto** (não só agendar)
5. **Antes de criar diretrizes novas**

Regra simplificada: **qualquer ação que persista ou afete produção** → reancorar memória primeiro.

Custo: 30s de leitura. Ganho: não repete erro registrado <5h atrás.

## Aplicação verificável

Grep no meu comportamento futuro: antes de qualquer `Write` de arquivo persistente, `Edit` em código de produção, ou resposta técnica a Codex/ZCode/Grok, deve ter no chat imediatamente antes:

```
head -N MEMORY.md
```

Ou equivalente lendo memória. Se não tem, é bug meu (esqueci).

## Regra âncora

**"Se vou tocar em código persistente ou produção, releio MEMORY.md primeiro. Sempre. Não é opcional."** — Claude Miguel, 15/08 14:38 BRT (após incidente vigilia_helper regex amplo)

## Relacionados

- [[feedback-processo-autoaprendizado-ler-memoria-todo-ciclo-20260815]] — meta-regra maior; esta é derivação
- [[feedback-erros-reincidentes-correcao-estrutural-nao-paliativa]]
- [[feedback-gate-metalinguagem-deve-inspecionar-href-nao-so-texto-20260815]] — regra do gate href original
- Fórum: `Cerebro/Foruns/forum_incidente_vigilia_helper_regex_amplo_20260815.md`
