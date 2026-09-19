---
name: Fecho natural — sem fórmula rígida "E daí?"
description: Miguel rejeitou 2026-04-20 o selo "E daí?" no último parágrafo. Cada matéria pede fecho próprio; proibido qualquer fórmula mecânica ("E daí?", "Em resumo", "Por fim", "Vale destacar").
type: feedback
originSessionId: ce520e95-41e3-4a15-9648-a544b965e78a
---
**Regra:** O último parágrafo deve fechar com sentido, mas SEM fórmula rígida. Pode amarrar impacto, apontar consequência, traçar cenário, fechar com ironia, deixar pergunta no ar — o que a matéria pedir. **Cada matéria tem seu fecho próprio.**

**Proibido:**
- Abrir o último parágrafo com "E daí?"
- Selos mecânicos: "Em resumo", "Por fim", "Vale destacar", "Em conclusão"
- Qualquer formato fixo que se repita entre matérias

**Why:** Em 2026-04-20 Miguel viu o draft 237312 (Inflação gás de botijão) fechando com "E daí? A combinação de estabilidade na Petrobras e desaceleração no gás doméstico sustenta a política de desindexação..." Reportou: "não precisa desse modelo rígido de e daí no final. cada matéria é de um jeito". O padrão "E daí?" era hardcoded como regra em múltiplos prompts e saía mecânico.

**Where the mandate was hardcoded pre-fix:**
- `publicador_tematicos.py:307` regra 5 do prompt V9 ("FECHO E DAÍ?")
- `agente_inflacao.py:194` ("Feche com um 'E Daí?'...")
- `agente_analytics_v9.py:527` e `:792` (auditor Claude + redator do spin-off)
- CLAUDE.md projeto seção 5.5

**Fixed 2026-04-20 ~17:00 BRT.** Prompts reescritos exigindo fecho natural, vetando as fórmulas explicitamente. Deploy Cingapura md5 confirmado.

**How to apply:**
- Em QUALQUER agente novo ou revisão de prompt, NÃO injetar "E daí?" nem qualquer selo mecânico.
- O princípio de "fecho com sentido/impacto" pode ser mantido como orientação, mas sempre deixando o LLM escolher a forma.
- Se ver qualquer matéria futura com selo robótico no último parágrafo, flag como bug editorial.
