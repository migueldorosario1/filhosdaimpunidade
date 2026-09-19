---
name: feedback-solucao-estrutural-nao-paliativo
description: "Quando bug recorrente de padrão estrutural aparece (capitalização, dedup, parsing), Miguel prefere refatoração que elimina classe inteira do bug em vez de crescer whitelist/regex caso a caso."
metadata: 
  node_type: memory
  type: feedback
  author: GLM/Ming
  written_at: 2026-07-17T19:30:00-03:00
  originSessionId: 513bf7fc-b567-4743-971a-e811d21ef5a9
---

> ⚠️ **Autoria:** Esta memória foi escrita por **GLM/Ming** (glm-5.2 via wrapper Claude Code CLI) em 17/07/2026 ~19:30 BRT. Se uma sessão futura do Claude Code puro ou outro agente ler isto, saiba que esta é perspectiva do GLM — confirmar com o Miguel antes de tratar como cânone seu.

# Solução estrutural > paliativo (whitelist crescente)

Quando um bug recorrente de padrão estrutural aparece (capitalização de topônimos, deduplicação fuzzy, parsing de wire estrangeiro, etc), **Miguel prefere refatoração que elimina a classe inteira do bug** em vez de crescer whitelist/regex caso a caso.

**Why:** Miguel 17/07 19:25 BRT, após eu reportar bug "Puerto Madero" lowerizado indevidamente: *"se precisar, corrige agora. e sim, construa solução estrutural para não ter esse problema de capitalização"*. O bug original vinha da estratégia do `_normalizar_title_case_ptbr`: lowerizar TUDO e depois recapturar via `_NOMES_PROPRIOS` whitelist finita. Topônimos estrangeiros não catalogados (Puerto Madero, México, Buenos Aires) viravam lowercase. Cada novo bug = adicionar entrada na whitelist = escalada infinita.

**How to apply:**
- Antes de adicionar entrada a `_NOMES_PROPRIOS` ou similar whitelist para corrigir bug específico, **perguntar**: este é um caso único (topônimo raro) ou sintoma de abordagem errada?
- Se sintoma: refatorar estratégia. Bug Puerto Madero → mudou de "loweriza tudo + whitelist inclusiva" para "preserva suspeitos + whitelist exclusiva" (`_VERBOS_SUBSTANTIVOS_COMUNS_PTBR` — só o que PRECISA ser lowercase).
- Whitelist inclusiva (cresce com cada novo caso) = red flag. Whitelist exclusiva (categoriza classes de palavras) = aceitável.
- Em pipeline de agentes, mesma lógica: auditor que precisa de prompt cada vez mais restritivo para barrar conteúdo = refatorar separação ranker/curador (ver [[feedback_auditor_nao_e_curador]]).
- Não fazer só o hotfix. Fazer hotfix + refatoração estrutural na mesma entrega.

**Sinal de alerta:** aparece o terceiro bug da mesma classe num prazo curto → parar e refatorar estratégia, não adicionar mais caso.

Irmã de [[feedback_auditor_nao_e_curador]] (definir o problema certo antes de afiar a solução).

**Assinatura:** GLM/Ming | 17/07/2026 ~19:30 BRT | sessão retomada 19:21 BRT | glm-5.2 via wrapper
