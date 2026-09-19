---
name: feedback-emenda-constitucional-1-teto-canal
description: EC1 sancionada 13/06 ~00:15 BRT — teto Canal Trindade 30→100 (dia a dia) ou 300 (sprint especial). Princípio do não-dogmatismo entra na Constituição.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 417ea1cb-f7cb-41c7-b869-848cc256e49c
---

**Regra:** Teto do Canal Trindade passou de 30 linhas fixas para **100 linhas (dia a dia) ou 300 linhas (sprint especial declarado por Miguel)**. Fóruns (800 linhas/80KB) e sub-índices (30 itens) não mudam.

**Why:** Miguel identificou que 30 linhas era dogmático e contraproducente: durante a Grande Reforma, o canal chegou a 31 linhas ainda na fase de montagem do mapa do sistema, obrigando arquivamento frequente que fragmentava a visão de conjunto. Miguel: "a gente não pode ser dogmático. se precisar mudar uma regra, a gente muda" (13/06 ~00:15 BRT).

**How to apply:**
- Modo ativo declarado em `A_GRANDE_REFORMA_LOCAL_20260610/root_modelo/Config/comunicacao_modo.txt` (valores: `sprint_especial` ou vazio = dia_a_dia).
- Script `A_GRANDE_REFORMA_LOCAL_20260610/scripts/manter_comunicacao_limpa.py` lê o arquivo via função `canal_max_lines()` que retorna `(teto, modo)`.
- Para propor nova emenda: agente abre `forum_grande_reforma_emenda_constitucional_N_<data>.md` com motivo + proposta + impacto → Miguel sanciona → aplica em Constituição + script + memória + canal.

**Artefatos EC1:**
- Fórum: `Foruns/forum_grande_reforma_emenda_constitucional_1_20260613.md`
- Constituição atualizada: Artigo 3 + seção "Emendas Constitucionais" + EC1 documentada
- Script atualizado: detecta modo via arquivo, default dia_a_dia
- Modo ativo: `Config/comunicacao_modo.txt` = `sprint_especial` (Grande Reforma)

**Relacionado:** [[feedback_constituicao_artigo2_comunicacao_trindade]], [[project_grande_reforma_frente_deduplicacao_pautas]].
