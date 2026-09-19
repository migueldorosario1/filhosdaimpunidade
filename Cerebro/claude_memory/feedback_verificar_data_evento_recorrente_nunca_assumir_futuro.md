---
name: feedback-verificar-data-evento-recorrente-nunca-assumir-futuro
description: "Eventos temporais recorrentes (COP, G20, campeonatos mundiais, eleições, Olimpíadas) DEVEM ser verificados via WebSearch antes de qualquer publish. Meu cutoff de treinamento pode ser anterior ao evento — se eu tratar como \"futuro\" algo que já aconteceu, alucino no tempo. Nunca confiar na minha data mental para eventos recorrentes marcados no calendário mundial."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73eca14d-c13b-47ac-a05e-3285ca9a2dc6
---

**REGRA:** Antes de publicar qualquer matéria que mencione **evento internacional recorrente** (COP climática, G20, G7, BRICS, Olimpíadas, Copa do Mundo, WEF Davos, eleição presidencial americana, etc.), **fazer WebSearch obrigatório** confirmando se o evento **já aconteceu, está acontecendo, ou é futuro**. Nunca assumir "vai acontecer em [mês futuro]" baseado só na minha data mental — meu cutoff de treinamento pode ser anterior ao evento e eu confundir passado com futuro.

**Why:** Miguel 09/08/2026 ~06:15 BRT flagrou o post 264869 como alucinação: eu escrevi "**Brasil vai à COP30 em Belém sem instância central**" tratando a COP30 como evento futuro. WebSearch cético revelou que **a COP30 já aconteceu — encerrou em 22 de novembro de 2025** em Belém, com o Pacote de Belém aprovado por 195 países. Marina Silva foi ovacionada no encerramento antes de sair do MMA em 1º/4/2026 para candidatura ao Senado (SP). O núcleo factual do post (Autoridade Nacional Climática nunca criada, dorme na Câmara desde 2023) era verdadeiro; o enquadramento temporal ("Brasil vai à COP30", "COP30 começa em novembro") era 100% alucinação — um evento que já era passado tratado como futuro. Post deletado (status=draft, DELETE HTTP 403 + trash HTTP 400). Backup em `_DELETED_264869_76568a865d3fe7a6.json`.

**Como o erro se formou:** confiei na minha intuição de data ("COP30 é em novembro em Belém") sem verificar se o novembro já havia sido. Combinado com o fato de que o worker V4 (fonte do draft) também tratava como futuro, criei uma cascata onde nenhum dos dois questionou o calendário. WebSearch teria pego em 30 segundos: **"COP30 Belém 2025 encerrada"** já retornaria as 195 países + Pacote de Belém.

**How to apply:**

1. **Lista de eventos recorrentes a sempre verificar antes de publish:**
   - COP climática da ONU (COP30 = Belém, nov 2025; COP31 = Austrália, nov 2026)
   - G20 (Joanesburgo nov 2025; próximo?)
   - G7, BRICS, WEF Davos
   - Olimpíadas (Paris 2024; Los Angeles 2028)
   - Copa do Mundo (Qatar 2022; EUA/Canadá/México 2026)
   - Eleições nacionais estrangeiras marcadas em calendário (EUA nov de anos pares, meio-mandato etc.)
   - Aniversários redondos (centenário Fidel 13/8/2026 — data futura ou passada?)

2. **WebSearch obrigatório antes do publish**, mesmo que o worker V4 já cite o evento como futuro/passado. Termo simples: `[evento] [ano] resultados` ou `[evento] [ano] encerrada` — resultado direto se já foi.

3. **Se ficar em dúvida se meu cutoff cobre o evento, sempre tratar como POSSIVELMENTE PASSADO** e verificar. Assunção-padrão "é futuro" foi o que quebrou o 264869.

4. **Sinais de que estou alucinando data:** (a) worker V4 cita o evento sem data específica; (b) meu instinto diz "novembro" ou "próximo mês" sem base concreta; (c) uso frases como "vai acontecer", "em novembro em Belém", "na cúpula que se aproxima" sem citar reportagem que confirme a proximidade. Cada uma dessas frases exige verificação temporal antes de manter no texto.

5. **Regra irmã** [[feedback-ceticismo-nao-apagar-investigar-lingua-original]]: aquela regra fala em investigar antes de remover atribuição/nome; esta aqui fala em investigar antes de tratar evento como futuro. Duas caras da mesma disciplina: **verificar meu cutoff antes de confiar na minha memória de calendário**.

6. **Se descobrir mid-publish que meu enquadramento temporal está errado:** parar tudo, refazer o enquadramento com fatos corretos, aplicar título/tese à nova realidade (evento passado ≠ evento futuro implica narrativa diferente). Se já publicou e Miguel apontou, **deletar imediatamente** (status=draft se DELETE/trash falharem) — nunca deixar circulando um post com erro temporal que altera a leitura política.
