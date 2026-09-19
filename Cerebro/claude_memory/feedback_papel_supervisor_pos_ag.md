---
name: 13-codador-por-ordem-de-chegada-revogou-codex-coda
description: "Miguel 2026-05-12 22:54 BRT — REVOGADO o \"default Codex coda\". Agora Claude E Codex codam em pé de igualdade; quem pegar a tarefa primeiro coda. Antigravity continua arquitetando."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e41c8659-4910-4323-a35a-1425133fac7c
---

# §13 — Codador por ordem de chegada (regra atual)

## A regra atual (2026-05-12 22:54 BRT)

> **Miguel:** *"tira essa regra de que codex coda. voces dois codam. quem pegar a tarefa primeiro. eu já pedi para mudar isso há tempos"*

**Claude E Codex codam em pé de igualdade.** Não há mais "default Codex coda". **Quem pegar a tarefa primeiro coda** — sem hierarquia padrão entre os dois.

## Why

A regra original "Codex coda, Claude supervisiona" (criada 2026-05-04 19:45 BRT após Claude errar deploy AG HTTP 500) gerava ociosidade: quando Miguel falava com Claude direto e Codex estava em outra frente, a tarefa esperava sem necessidade. Adendo 08/05 já tinha aberto exceção ("Claude pode codar quando recebe primeiro"), mas mantinha o "Default Codex" — confundia. Miguel agora consolidou: **acaba o default**, fica só ordem-de-chegada.

## How to apply

**Fluxo operacional (ambos os codadores seguem):**
1. **Tarefa chega** (Miguel posta no canal/chat com qualquer um dos dois)
2. **Quem recebeu posta no canal:** *"vou codar X em [estimativa]"* — registro anti-colisão (§30.7 + §50)
3. **Outro agente dá feedback técnico** no canal/fórum (consenso obrigatório antes de deploy/mudança crítica)
4. **Quem assumiu primeiro coda** após consenso 3/3 (parceiro + Antigravity + Miguel autoriza, em tarefas críticas)
5. **Antigravity arquiteta** (não coda `.py` crítico) — escopo §21 inalterado

**Tarefas críticas** (deploy `.py`, crontab, produção viva, custo >$1/dia, mandamento): exigem **roda completa** com aval Antigravity ANTES da codagem.

**Tarefas não-críticas** (governança/memória, fóruns, scripts offline zero-write, autocura §6): fluxo rápido (recebe → feedback parceiro → coda) sem aval Antigravity obrigatório.

**Supervisão cruzada continua:**
- Pré-deploy: revisão linha-a-linha do snippet/patch pelo parceiro (§12)
- Durante: `curl -I` em URLs canônicas + logs em paralelo
- Pós-deploy: HTTP status + marcador esperado + GA4 sem regressão
- Erro detectado: rollback §11 imediato, sem nova aprovação

## Histórico (para contexto, NÃO mais vinculante)

- **2026-05-04 19:45 BRT** — regra original "Codex coda, Claude supervisiona" criada após Claude errar deploy AG (HTTP 500 em todos AMP por hookear plugin "AMP for WP" sem identificar). Codex demonstrou precisão cirúrgica detectando o 500 em <2min de fora.
- **2026-05-08 15:40 BRT** — Adendo "Codador por Ordem de Chegada": Claude também coda quando recebe primeiro, mas mantém "Default Codex coda".
- **2026-05-12 22:54 BRT** — Miguel revoga o "Default Codex coda" por completo. Fica APENAS ordem-de-chegada pura.

## Combinações com outras regras

- §6 (Emergência): qualquer um pode agir sem consenso em ações reversíveis em segundos
- §8 (Consenso técnico): aprovação conceitual entre os dois codadores
- §11 (Rollback obrigatório): plano sempre anexado pelo codador
- §12 (Consenso de código): parceiro revisa snippet do codador antes do deploy
- §13 (esta): ordem de chegada pura, supervisão cruzada
- §21 (AG checklist): inalterado, AG não coda `.py` crítico
- §50 (Aviso prévio canal): codador anuncia antes de agir

Vinculado: [[feedback_codex_chatgpt_antigravity_gemini]] (identidades distintas dos 3 agentes), [[reference_sistema_resumo]].
