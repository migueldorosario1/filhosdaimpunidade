---
name: feedback-corrigir-na-raiz-nao-no-auditor
description: "Miguel 15/06 ~22:30 BRT — princípio arquitetural duplo (a) clichê se combate na DIRETRIZ que vai pro PRODUTOR, não forçando AUDITOR a reescrever; (b) hardcode (ex: whitelist nome→hash) NÃO decide output; no máximo SUGERE candidato; validação fica em entidade estruturada + auditor/revisor com websearch. Princípio comum: corrigir na RAIZ (upstream), não remendar no FIM (downstream)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 83feb640-dee1-483b-9372-162a5be7876e
---

# Corrigir na RAIZ (produtor/diretriz/entidade), não no AUDITOR

Miguel 15/06 ~22:30 BRT entregou DUAS correções arquiteturais paralelas no mesmo bloco:

## Correção 1 — Clichê é problema do PRODUTOR, não do AUDITOR

> *"mas o cliche vem do produtor, certo? o certo então é combater o cliche na diretriz que vai para o produtor, ao invés de forçar o auditor a reescrever"*

## Correção 2 — Hardcode (whitelist nome→hash) não DECIDE; no máximo SUGERE

> *"não quero esses hardcodes. ou até podemos ter, mas o revisor precisa passar websearch, o auditor também."*

(relayada por Codex 22:35 BRT em canal_trindade)

## O princípio comum

**Corrigir na RAIZ (upstream), não remendar no FIM (downstream).**

- ❌ ERRADO: produtor gera lixo → auditor remenda
- ❌ ERRADO: hardcode tabela decide → ninguém valida
- ✅ CERTO: diretriz que vai pro produtor já carrega regra anti-clichê → produtor sai correto → auditor só verifica forma (§95, §86, fact-check)
- ✅ CERTO: hardcode sugere candidato → entidade estruturada + auditor/revisor com websearch validam → só aí decide imagem

## Por quê

1. **Auditor com poder de reescrever = redundância editorial**: dois lugares mexem no texto, fica ambíguo quem manda, fica caro (dupla chamada LLM), e se diverge gera deriva.
2. **Hardcode com poder de decidir = ponto único de falha sem verificação**: nome publicação não validada → imagem errada vai pra rua → vexame.
3. **Único responsável + validação por evidência externa (websearch)** = arquitetura limpa e blindada contra alucinação tanto da LLM quanto da tabela estática.

## Como aplicar

### Em propostas de AUTH editoriais (anti-clichê, anti-redundância, tom)

1. Se a regra é "produtor não deve fazer X" → patch principal vai no **prompt do produtor** (`produtor_geral.py` ou `diretrizes_editoriais.py` ou `diretriz_<agente>.json`).
2. **A solução estrutural NÃO deve DEPENDER do auditor** corrigir um vício que nasce no produtor — esse é o ponto crítico. Se a única defesa contra o vício for o auditor reescrever, a arquitetura está errada.
3. O auditor **continua sendo camada inteligente de correção, acabamento e exceção** — pode reescrever clichê quando for o caso, mas como rede de segurança, não como solução primária. Não virar a regra rígida "auditor proibido de tocar em clichê".
4. **Refinamento da correção Miguel 23:20 BRT (via Codex)**: a primeira leitura ("remover anti-clichê do auditor") foi régua dura demais. O certo é: simplificar/reduzir duplicação na cadeia produtor→auditor, sem amputar a camada de revisão.

### Em propostas de AUTH de mídia / metadados / categoria / qualquer tabela hardcoded

1. Hardcode (whitelist nome→hash, dicionário keyword→cat, lista de fontes) **só pode SUGERIR candidato**.
2. Decisão final = entidade estruturada (entidade_id) + validação por evidência externa (websearch quando aplicável).
3. Sem confiança suficiente → bloqueia output, manda pra `pronta_sem_midia` / revisão humana / fallback institucional.

### Em propostas que misturam ambos

Se a AUTH proposta mexe em DUAS camadas (produtor + auditor, ou tabela + decisão), parar e perguntar: "Isso aqui é deliberado ou é dupla defesa que viola o princípio raiz?"

## Casos fundadores 15/06

### Clichê (correção 1)
- AUTH-022 (eu) e AUTH-023a (Codex) botaram seção anti-clichê tanto no `produtor_geral.py` quanto no `auditor_texto.py`. ⚠️ Dupla defesa pesada, mas **não amputar auditor** — refinar pra reduzir duplicação.
- AUTH-023b (Codex) só mexeu nas `diretriz_*.json` per-agente que vão pro produtor. ✅ Alinhado.
- AUTH-027 (eu) só mexeu nas `diretrizes_editoriais.py` (prompt central produtor). ✅ Alinhado.
- **AUTH-029 (cleanup) pendente — REFORMULAR**: a primeira leitura ("REMOVE seção anti-clichê do auditor") foi corrigida pelo Miguel via Codex 23:20 BRT. O certo é simplificar a cadeia produtor→auditor (reduzir duplicação) preservando capacidade do auditor reescrever quando for caso de exceção. Codex retraga proposta inicial; vai reformular.

### Whitelist (correção 2)
- AUTH-025b.1 (Codex) criou `lideres_politicos.json` com 4 líderes + alias decisivo no `agente_midia.py` (alias hardcoded → publica imagem). ❌ Hardcode decidindo.
- AUTH-025b.1.1 (proposta Frente C AGY MVP+1, mais 4 líderes hardcoded) FOI CONGELADA pelo Codex sem PASS após Miguel intervir.
- **Rollback pendente:** Rota A (cp do `.bak_pre_auth025b11_20260615_223108`).
- **Redesign pendente:** Rota B = whitelist vira tabela de sugestão de candidato + `agente_midia.py` decide só via entidade_id + auditor/revisor com websearch.

## Why

Miguel 15/06 22:30 BRT, duas correções na mesma janela, princípio idêntico: descentralizar correção é mais barato e mais robusto que botar carga redundante na camada de auditoria. Esse princípio é genérico — vale pra clichê editorial, pra whitelist de mídia, e pra qualquer caso futuro de "como faço pra garantir X no output".

Relacionados:
- [[feedback_sul_global_defender_nao_repetir_chiclete]] (a regra anti-clichê em si)
- [[feedback_diretrizes_unificadas_legado_reforma]] (diretrizes precisam ser unificadas)
- [[feedback_llm_sempre_para_editorial_nunca_lista_fixa]] (variante anterior do mesmo princípio: lista fixa é dura demais pra editorial)
- [[feedback_websearch_obrigatorio_producer_auditor_curador]] (EC2 — websearch obrigatório, base pra Rota B whitelist)
