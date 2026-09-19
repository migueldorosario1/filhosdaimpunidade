---
name: Investigação 2026-04-25 — alegação de textos truncados sem caso real
description: Miguel reportou textos publicados incompletos. Varredura em 100 publish + 30 drafts: zero truncamento confirmado. Pontos de risco teóricos anotados sem patch (Regra #2 CLAUDE.md).
type: project
originSessionId: 372483cf-746c-41be-98b2-407f880fb471
---
**Reporte do Miguel 2026-04-25 ~07:30 BRT:** "Múltiplos textos estão sendo publicados incompletos, com a leitura interrompida no meio da última frase."

**Investigação Claude Code:**
- 100 posts publicados (mais recentes) + 30 drafts (incluindo agente Análise) examinados.
- Detector regex inicial deu 3 candidatos: `239431` (Butantan vacina), `239398` (Congresso dosimetria), `237727` (Petróleo Ormuz).
- **Inspeção do `raw` content de cada um:**
  - 239431: lista de hospitais por região completa (Sul tinha só 2 — PUC-RS e Moinhos). Não truncado.
  - 239398: `<ul>` com 10 itens de progressão de pena fechada após cabeçalho `<strong>`. Não truncado.
  - 237727 (de 21/04): citação IA crua `([habtoorresearch.com](URL))` não removida no fim — bug real mas anterior ao reforço do `_limpar_citacoes_ia` em `publicador_tematicos.py:649`.
- **Falsos positivos vinham de:** detector procurava `[.!?…]$` no fim do texto puro, mas posts terminam em "Fonte: <a>...</a>" (formato editorial) ou em itens de lista que o regex `<p>` não captura.

**Decisão Miguel:** "se não tem caso nenhum, pode acabar gerando mais problema" — sem patch.

**Pontos de risco anotados pra futuro (NÃO patchados):**
1. `motor_publicador.py:998` — fallback de JSON parse usa regex lazy `*?` em `"html"\s*:\s*"([\s\S]*?)",\s*"palavras_chave"`. Se LLM truncar JSON antes de fechar `"palavras_chave"`, esse fallback ainda assim captura `html` parcial.
2. `motor_publicador.py:205,225,237` — Trindade Editorial usa `max_tokens=5000` consistente. Folgado pra 1000 palavras, mas em JSON com escapes (`\"`, `\n`) e múltiplos campos (titulo+html+yoast×3+focus+palavras_chave+categoria) pode apertar se LLM gerar 1500+ palavras.
3. `analise/camada4_redacao.py:299` — rewrite de parágrafo longo com `max_tokens=400`. Suficiente pra 2 frases curtas, MAS se o parágrafo original era denso, rewrite pode cortar.
4. `publicador_tematicos.py:649 _limpar_citacoes_ia` — pode ter brecha pra formatos exóticos de citação (multiline, com markdown image, etc).

**Como confirmar truncamento real (se voltar):**
- Pegar `raw` do post via `?context=edit&_fields=content` com WP_USER+WP_APP_PASSWORD
- Olhar último PARÁGRAFO DE CONTEÚDO (excluindo `Fonte:` e `Leia também:`)
- Se termina em palavra minúscula ou cabeçalho `<strong>` solitário sem corpo depois → truncado.

**Como aplicar:** se Miguel reportar de novo com IDs concretos, ir direto pro `raw` desses IDs antes de qualquer hipótese.
