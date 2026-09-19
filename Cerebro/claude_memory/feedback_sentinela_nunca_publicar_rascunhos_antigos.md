---
name: feedback-sentinela-nunca-publicar-rascunhos-antigos
description: "Loop Sentinela (e qualquer agente autônomo de publicação) NUNCA pode publicar drafts V4 com mais de 2h de fila. Backlog velho é território editorial exclusivo do Miguel. Regra inviolável, vale mais que qualquer outro critério."
metadata: 
  node_type: memory
  type: feedback
  author: "Claude Code (Anthropic, claude-opus-4-7)"
  written_at: 2026-07-20 08:00 BRT
  originSessionId: b3501857-e7d4-49f4-83bd-74804874c770
---

**⚠️ ATENÇÃO: memória escrita por Claude Code (Anthropic), NÃO por GLM/Ming (Zhipu AI).**

## Regra INVIOLÁVEL

**Loop Sentinela — e qualquer agente autônomo de publicação — SÓ publica drafts V4 com `date` nas últimas 2 HORAS. NUNCA publicar backlog velho. Se draft tem >2h de fila, é território editorial EXCLUSIVO do Miguel do Rosário.**

Aplica-se em duas camadas de defesa:
1. **Prompt Claude Opus** — regra explícita `config/prompts.md`
2. **Código Python** — filtro em `sentinela_ciclo.py:aplicar_correcoes()` que ABORT publish se `now - date_gmt > 2h`, mesmo se Opus autorizar

Estrutura de mensagem quando ABORT: `{"acao": "ABORT-antigo-{idade_h}h", "regra": "cap 2h — Miguel 2026-07-20"}`

**Why:** Em 2026-07-20 07:28 BRT, Loop Sentinela publicou 5 drafts antigos em cascata: 262127 (34h fila), **262103 (40h fila — Xi Jinping IA, DUPLICATA de post já publicado dias atrás)**, 261941 (54h), 261937 (56h). Miguel viu 262103 no wp-admin, reconheceu como conteúdo duplicado, rebaixou pra pending, e me chamou atenção: *"você não pode publicar rascunhos antigos não viu é pra publicar só os rascunhos novos"* ... *"posso te dizer quem publicou? é rascunho de um post que já publiquei, dias atrás. e agora alguém pegou esse rascunho e publicou. eu já rebaixei"*. Ciclo 06:57 já tinha publicado 262161/262150/262101 (~19-40h de fila) sem autorização também. Total 7 posts antigos publicados por engano.

Causa raiz: meu prompt original do Sentinela em `config/prompts.md` NÃO fixou critério temporal. Só listou "featured_media > 0" + "corpo >500 chars" + "sem TESTE no título". Opus interpretou "publicável" como decisão editorial pura, ignorando idade da fila. Publicou tudo que parecia bom.

**How to apply:**

1. **Loop Sentinela (`sentinela_ciclo.py`):** filtro Python OBRIGATÓRIO em `aplicar_correcoes()`. Nunca remover mesmo que prompt melhore.

2. **Prompt Sentinela (`config/prompts.md`):** critério `IDADE MÁXIMA 2 HORAS` em posição #1 (antes de todos os outros), marcado como "REGRA ABSOLUTA — NUNCA publicar rascunhos antigos".

3. **Qualquer novo agente de publicação futuro** (autocura inteligente, Maestro Local, versão sucessora do Sentinela) — replicar mesma regra em prompt+código.

4. **Cap 2h justificativa (Miguel 20/07):** "2 a 5 horas é novo também" — 2h é margem conservadora. Se draft tem 3h e Miguel não pegou, Sentinela deixa. Backlog velho SÓ Miguel resolve.

5. **Rebaixamento retroativo:** se descobrir que já publicou draft antigo por engano, rebaixar pra `pending` (padrão que Miguel usa), NÃO `draft`. Logar em `Cerebro/monitoramento_horario/mudancas_aplicadas/YYYY-MM-DD.jsonl` como `action: "REBAIXAR_publish_antigo"`.

## Casos observados

- **2026-07-20 06:57 BRT:** Sentinela publicou 262161 (19h), 262150 (24h), 262101 (40h). Fora do cap.
- **2026-07-20 07:28 BRT:** Sentinela publicou 262276 (20min ✅), 262127 (34h ❌), 262103 (40h ❌ DUPLICATA), 261941 (54h ❌), 261937 (56h ❌). Miguel detectou 262103 e chamou atenção.
- **2026-07-20 08:00 BRT:** Miguel formaliza regra. Claude aplica fix duplo (prompt+código) + memória inviolável.
- **Nova rodada Sentinela pós-fix:** próximas iterações do loop foreground vão pegar prompt e código atualizados.

## Relacionadas

- [[claude-editor-baleia-azul-20260719]] — outro papel editorial de Claude, também com regra "só edições curtas honestas"
- [[feedback-perguntar-antes-assumir-bug-publicacao]] — perguntar Miguel antes de reverter estado (aplica na direção oposta: aqui, NÃO publicar sem autorização temporal implícita)
- [[feedback-miguel-edita-titulos-manual]] — Miguel tem prerrogativa editorial ativa; agente não pode atropelar
- [[claude-engenheiro-chefe-ecossistema-20260719]] — passagem de autoridade + limites §21

## Assinatura

Registro escrito por Claude Code (Anthropic, `claude-opus-4-7`), sessão `CLAUDE-CHEFE-ECOSSISTEMA-20260719-1020` (continua ativa 2026-07-20), 2026-07-20 08:00 BRT.
