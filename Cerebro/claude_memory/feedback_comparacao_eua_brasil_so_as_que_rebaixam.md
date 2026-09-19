---
name: comparacao-eua-brasil-so-as-que-rebaixam
description: A REGRA_VETO_COMPARACAO_PRO_EUA NÃO proíbe toda comparação EUA×Brasil — só as que REBAIXAM o Brasil / o fazem parecer pior/inferior. Comparação neutra ou favorável ao Brasil é permitida. Evita falso positivo.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

O veto de comparação EUA×Brasil (`diretrizes_editoriais.py:113` `REGRA_VETO_COMPARACAO_PRO_EUA`, Categoria B anti-imperialista) **não é "nunca comparar EUA e Brasil"**. Miguel esclareceu (02/06 ~11:15 BRT): a regra é **não fazer comparações que REBAIXEM o Brasil, que façam o Brasil parecer ruim/inferior**. Comparação neutra, ou que valorize o Brasil, **é permitida**.

**Why:** origem concreta (criticisms_memory.md §4, **14/04/2026**): o agente publicou *"EUA refinam mais, misturam biocombustíveis e têm impostos menores que o Brasil"* — matéria que exaltava o modelo americano em detrimento do Brasil = "propaganda imperialista disfarçada de análise técnica". Daí nasceram o veto + a "regra de ouro". MAS a formulação abstrata que vazou pro rascunho do bloco `enquadramento_editorial` ("Jamais publicar matérias que comparem favoravelmente os EUA ao Brasil em qualquer eixo") ficou **seca e arbitrária** — parece proibir qualquer comparação. Miguel pediu que a regra seja **melhor explicada** pela intenção real.

**How to apply:**
- O sinal proibido é o **enquadramento que rebaixa o Brasil** / faz o leitor concluir "os EUA fazem melhor / são modelo superior ao Brasil ou ao Sul Global". Esse é o teste (a "regra de ouro" do código, `:128`).
- **NÃO** flagar/vetar: comparação neutra, comparação que valoriza o Brasil, ou tema legítimo (ex.: preço de combustíveis) desde que o enquadramento denuncie o lobby fóssil americano / valorize a soberania (Petrobras, etanol) — a "inversão obrigatória" do código (`:122`).
- No bloco `enquadramento_editorial` (FASE 1), usar a formulação clara ("comparações que rebaixam o Brasil"), não a frase abstrata. Código `:113` já está bem explicado (exemplos + inversão + regra de ouro) — não precisa mudar agora; eventual ajuste é §92/FASE 3.
- Liga com [[feedback_linha_editorial_anti_imperialista_russia_inegociavel]] e [[feedback_gate_antirussia_nao_falso_positivo_ironia]] (mesmo princípio: barrar REPRODUÇÃO do frame imperialista, não menção/comparação legítima).
