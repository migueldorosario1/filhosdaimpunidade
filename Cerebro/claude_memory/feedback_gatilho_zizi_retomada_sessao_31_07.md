---
name: feedback-gatilho-zizi-retomada-sessao
description: "Miguel digita 'zizi' (sozinho) = ritual de retomada de sessão. Ler SEMPRE o ponto de retomada mais recente via ls -t, não um arquivo fixo."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c47eaa18-1e9a-4db8-b36b-e37b22deffed
---

**Gatilho:** Miguel digita `zizi` (token único + Enter) em qualquer chat comigo (Claude Code) → executar ritual de reancoragem lendo o ponto de retomada mais recente.

**Why:** Miguel pediu 31/07 22:15 BRT "gravar sessão. quando voltar, lembre dela. codigo dela é zizi". Depois (04/08 16:01 BRT) corrigiu: "atualiza esse inicio aí do claude, tá retomando com muita coisa antiga. limpa isso." → o ritual NÃO deve ler um arquivo fixo (que fica velho e sujo), mas sempre o ponto mais recente disponível.

**How to apply:** Ao ver `zizi` em chat comigo, executar o skill `retome_claude`. Passos essenciais:

1. `date "+%Y-%m-%d %H:%M %Z"`
2. `ls -t "/home/migueldorosario/Downloads/Antigravity Google/Cerebro/Foruns/ponto_retomada_claude_"*.md | head -1` e ler o arquivo inteiro
3. Ler primeiras 30 linhas de `MEMORY.md`
4. `tail -1` de `/home/migueldorosario/ferramentas/sentinela/logs/ciclos.jsonl`
5. `tail -3` de `bugs_$(date +%Y-%m-%d).jsonl` + `wc -l` pra contar publicados
6. Reportar em ≤ 20 linhas: timestamp, arquivo do ponto + delta em h/dias, 3 bullets do estado gravado, delta desde então, pendências que dependem do Miguel
7. NÃO rodar ciclo Vigília automaticamente — esperar comando

**Sempre que Miguel pedir "grava novo ponto de retomada"** (ou quando fizer sentido no final de uma sessão marcante): criar arquivo novo `ponto_retomada_claude_sessao_YYYYMMDD_HHMM.md` (não editar antigo — histórico preserva). O `ls -t` já garante que só o mais novo seja lido.

**NÃO confundir com `ponte`:**
- `ponte` = sincronização TRIANGULAR (Kimi Desktop + Antigravity Desktop + canal/inbox/cartinhas) — leitura de ~7 fontes
- `zizi` = reancoragem do estado do Claude a partir do último ponto de retomada gravado

Regras irmãs: [[feedback-gatilho-ponte-ritual-de-sincronizacao]], [[feedback-loop-vigilia-opus-v5]], [[feedback-checagem-dupla-editorial-com-autonomia]].
