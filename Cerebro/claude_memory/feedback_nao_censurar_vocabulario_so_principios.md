---
name: nao-censurar-vocabulario-so-principios
description: "Não se censura palavra/expressão de estilo no Cafezinho; só se barra o que viola princípios filosóficos, editoriais e políticos (linha anti-imperialista)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# Não censurar vocabulário — só barrar violação de princípios

**Regra:** No Cafezinho NÃO se proíbe palavra ou expressão por questão de estilo. Só se barra conteúdo que viola os três princípios **filosóficos, editoriais E políticos** (a linha anti-imperialista). Vocabulário "chamativo" — `revela`, `extraordinário`, `segredo`, `mistério` etc. — é permitido e até desejado.

**Why:** Miguel formalizou isso em 2026-06-02 ("siga o princípio filosófico que não precisamos censurar palavras ou expressões, desde que sigamos os princípios filosóficos, editoriais e políticos"). O caso fundador é "revela", marcada como veto absoluto na diretriz provisória `RD-40e909ffaf`, quando na verdade é escolha editorial DELIBERADA baseada nos 50 posts mais lidos de todos os tempos (ver [[feedback_revela_nao_e_proibido_e_desejado]]). Censura de estilo gera falso positivo e empobrece o texto — é o oposto da intenção editorial.

**How to apply:** Ao auditar/codar filtros de título ou corpo, distinga dois eixos:
- **Estilo/vocabulário** (Categoria A) → LIBERAR. Não criar listas de "termos proibidos" por gosto. Já aplicado: `sanitizador_vernacular.py` (`_TERMOS_PROIBIDOS_TITULO = []`), `diretrizes_permanentes_v1.md` (regra 5 do gerador de títulos diz explicitamente "não há vocabulário proibido"), `diretriz_ativa.json` recompilada.
- **Princípios** (Categoria B) → BARRAR de verdade, com check determinístico. Isso inclui a linha anti-imperialista INEGOCIÁVEL: nunca publicar contra Rússia, veto a "regime/aiatolás/ditadura" sobre Irã, ataques a Governo/STF/comparação pró-EUA (ver [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]]). Essa categoria NÃO se libera sem ordem explícita de Miguel.

O sanitizador mantém correções **não-estilísticas** legítimas: falsos cognatos de espanhol (buzos→mergulhadores), grafias canônicas (Kyiv→Kiev, Hezbolá→Hezbollah), caixa de meses, timestamps de agência. Isso é vernáculo/factual, não censura de vocabulário — continua valendo.

Casa com [[project_arquitetura_3_camadas_diretrizes]]: política em código (determinística, reusa REGRA_VETO), forma/estilo em prompt (probabilística, sem proibir palavra).
