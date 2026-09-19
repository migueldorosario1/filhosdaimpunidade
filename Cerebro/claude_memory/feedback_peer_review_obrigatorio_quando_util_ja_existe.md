---
name: feedback-peer-review-obrigatorio-quando-util-ja-existe
description: "Codex 16/06 09:30 BRT (caso AGY AUTH-043) — quando proposta de AUTH envolve util/helper que JÁ EXISTE no Tencent (mesmo nome, mesma função), peer review é OBRIGATÓRIO antes de emitir AUTH formal. Comparar versão proposta vs versão existente, identificar regressões silenciosas (fallback removido, lista incompleta), mesclar o melhor de cada. Caso fundador: AGY propôs nova versão de `util_hiperlink_fonte.py` que regredia fallback de domínio quando nome_fonte vazio + lista de agentes incompleta. Codex peer review pegou ambos, mesclou Tencent base + regex AGY + gate expandido."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Peer review obrigatório quando util/helper proposto já existe

Codex 16/06 09:30 BRT, após executar AUTH-043 corrigida (resolução §95 hiperlinks LEGADO).

## A regra

**Quando uma proposta de AUTH envolve refactor de util/helper que JÁ EXISTE no Tencent** (mesmo arquivo, mesma função, mesma intenção arquitetural), peer review por outro engenheiro é OBRIGATÓRIO antes do Daemon emitir AUTH formal. **Não basta sintaxe OK + import OK + lógica nova OK — precisa comparar dimensionalmente** versão proposta vs versão existente:

1. Quais **edge cases** a versão existente trata que a nova não?
2. Quais **fallbacks** a existente tem que a nova removeu?
3. Quais **constantes/listas** estão incompletas na nova?
4. Quais **comportamentos fail-open vs fail-closed** divergem?

## Por quê

Refactor de util compartilhado é uma das operações mais perigosas porque:

- Pode **regredir silenciosamente** comportamentos importantes que ninguém pediu na proposta
- Outros agentes/scripts que dependem do util sofrem regressão **invisível** (não há erro de sintaxe ou import; só comportamento errado em casos extremos)
- Util normalmente tem **histórico de patches incrementais** que acumulam edge cases reais — perder esse histórico = perder anos de aprendizado

## Como aplicar

### Em proposta de AUTH que mexe em util/helper

Antes de emitir AUTH formal:

1. **Verificar se existe versão prévia no Tencent** (`ssh ... 'sudo ls /root/<util>.py'`)
2. Se SIM:
   - Comparar **linha a linha** versão proposta vs versão Tencent (`diff` ou `git diff` se em git)
   - Identificar **regressões funcionais** (fallbacks removidos, listas incompletas, casos `''/null/{}` tratados diferente)
   - **Pedir peer review obrigatório** por outro engenheiro antes de emitir AUTH
   - AUTH formal = **versão mesclada** (preservar o bom de cada lado), NÃO versão proposta literal
3. Se NÃO existir (criação nova): peer review continua sendo boa prática mas é menos crítico

### Pra Daemon emitir AUTH

NÃO emitir AUTH formal direto se a proposta:
- Mexer em util/helper compartilhado
- E versão prévia existir no Tencent
- E não houver peer review documentado por outro engenheiro

Em vez disso:
> "Peer review obrigatório antes de AUTH. <Engenheiro> compara versão proposta vs versão Tencent. Identifica regressões + faz merge. Daemon emite AUTH formal sobre o merge."

## Caso fundador (AUTH-043, 16/06)

**Contexto**: AGY identificou §95 hiperlink como buraco em 7 agentes que bypassam o motor. Propôs:
- Nova `util_hiperlink_fonte.py`
- Patch em motor_publicador + 6 agentes
- Backups locais + py_compile + import test OK

**Peer review Codex pegou 2 regressões na versão AGY**:

1. **Fallback de domínio quando `nome_fonte=""`**: versão Tencent (09/06, AUTH-028 antigo) injetava hiperlink usando o domínio extraído da URL quando `nome_fonte` vinha vazio. Versão AGY removia esse fallback → matérias com fonte sem nome amigável ficariam sem hiperlink em silêncio.

2. **`AGENTES_EXIGEM_URL_FONTE` incompleto**: AGY patchou 7 agentes mas só botou 5 nomes no frozenset. 2 agentes ficariam sem cobertura do gate.

**Solução Codex**: merge — base = util Tencent (preserva fallback) + regex melhor do AGY + lista expandida cobrindo os 7 + 4 prévios.

**Lição**: sem peer review, eu (Daemon) teria emitido AUTH-043 sobre a versão AGY literal e o sistema regrediria silenciosamente o fallback de domínio. Bug clássico de "ninguém pediu pra mudar mas mudou".

## Implicação pra Daemon (eu)

Daqui pra frente, em qualquer proposta de AUTH que mexa em util/helper compartilhado:

1. **Step 0**: verificar existência prévia no Tencent
2. **Step 1**: se existe, **NÃO emitir AUTH direto** mesmo com py_compile/sanity OK
3. **Step 2**: peer review obrigatório por outro engenheiro (Codex/Kimi/GLM)
4. **Step 3**: peer review reporta merge ou divergências
5. **Step 4**: Daemon emite AUTH formal sobre o merge (ou rejeita)

Isso vale também pra propostas que parecem simples ("só atualizar regex", "só adicionar nome na lista") — porque é nessas que regressões silenciosas escondem.

Relacionados:
- [[feedback_hierarquia_trindade_claude_daemon_vivo]] (Daemon coordena, engenheiros propõem)
- [[feedback_corrigir_na_raiz_nao_no_auditor]] (princípio raiz, refactor cuidadoso)
- [[feedback_creditos_apis_primeiro_item_diagnostico_lentidao]] (Step 0 sistemático em diagnóstico)
- [[feedback_grep_historico_log_sem_data]] (verificar histórico antes de concluir)
