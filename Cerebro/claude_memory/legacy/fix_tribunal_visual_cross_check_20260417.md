---
name: Fix Tribunal Visual — prompt endurecido + cross-check pós-legenda
description: agente_roteador_llm.py ganhou 5 regras de reprovação automática e 2ª chamada ao Gemini validando se a legenda contradiz o título. Motivado pelo caso rio Colorado/rio Ocoee (post 235789).
type: project
originSessionId: b8d23953-06f2-4699-9a68-275c279163e9
---
Deploy 2026-04-17 13:01 BRT na `/root/agente_roteador_llm.py` (função `analisar_imagem_gemini_vision`). O Tribunal Visual estava com régua frouxa ("APROVADA se for minimamente coerente/temática"), e aprovou uma imagem-brochure do USGS sobre o **rio Ocoee** (Tennessee) como ilustração de matéria sobre o **rio Colorado** (Grand Canyon) — post 235789. O Gemini foi honesto: na legenda escreveu literalmente "rio Ocoee", mas o código não checava coerência entre legenda e título.

**O que mudou:**

1. **Prompt endurecido** com 5 reprovações automáticas: (a) troca de entidade geográfica/nomeada; (b) material primariamente textual (brochures, folders, infográficos, diagramas, mapas, pôsteres); (c) texto em idioma estrangeiro dominante em matéria PT-BR; (d) coerência apenas por palavra-chave genérica; (e) teste final "a legenda verdadeira é compatível com o título sem mentir?". Incluído o próprio caso do rio Ocoee como exemplo de "não faça assim".

2. **Cross-check pós-legenda** (defesa em camadas): depois de `veredicto=APROVADA` e `legenda` montada, faz 2ª chamada Gemini (só texto, `gemini-2.5-flash`, temperature 0, maxOutputTokens 10) perguntando "a legenda é incompatível com o título? SIM/NAO". Se SIM → retorna REPROVADA com log explícito.

3. **Fail-open** no cross-check: se o 2º Gemini crashar/timeout, mantém a aprovação original pra não bloquear publicação por problema de rede.

**Custo:** +1 chamada Gemini Flash (~$0.0001) só em imagens aprovadas pelo 1º filtro. Imagens reprovadas não pagam segunda chamada.

**Backup do arquivo anterior:** `/root/agente_roteador_llm.py.bak_20260417_1300`.

**Why:** O sistema publicou imagem errada porque "coerência temática" é critério ambíguo demais. Prompt agora exige ENTIDADE ESPECÍFICA e rejeita documentos textuais. Cross-check garante que mesmo se o Gemini aprovar por engano, a contradição legenda×título é pega antes de ir ao WP.

**How to apply:** Se futuramente houver reclamação de imagem fora do assunto, checar se o cross-check foi desligado por engano ou se o Gemini está retornando NAO quando deveria SIM (prompt do validador pode precisar de mais exemplos). Se precisar desabilitar temporariamente o cross-check, só envolver em `if False:` — a função principal volta ao comportamento antigo.
