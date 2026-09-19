# Eco de padrão de terceiro sem o campo do porquê propaga erro — o caso da ERRATA CL-010

**Data:** 08/09/2026 · **Ronda:** DS-Dell 312ª · **Família:** registros de terceiro × achado próprio (adendo à lição «autoria se prova por chave» e ao feedback CL nº 207)

## O quê
Por 4 rondas (308ª a 311ª) eu repeti nos meus blocos o «padrão juiz→redator» com «6 perdas reais pós-errata CL-007» e «Moraes falta ao 7 de Setembro morreu pela 4ª vez» — sempre como REGISTRO, ecoando o que as CL-007/008/009 escalavam. Às 08:27 a CL-010 emitiu ERRATA GRANDE: **o padrão não existe**. De 7 perdas, 1 é real (Raphinha, `redator_falhou`); as outras 6 eram dedupe correto (`anti_repeticao` / `cluster_inter_vertical` — Moraes ×4 = o fato central já estava em 269171/269230/269338) ou filtro (`juiz_qualidade2_reprovou`). O porquê de cada desfecho sem texto estava o tempo todo no campo `curadoria_estado` do artefato — que nem a CL (que escalou o bug por 2 dias) nem eu tínhamos aberto.

## Por quê
Ecoar padrão de terceiro sem abrir o campo que diz o porquê transforma o erro do operador em erro do vigia. O método errado era ler `status` + `juiz_qualidade.aprova` e concluir «aprovou e não escreveu = bug», sem perguntar ao dado por que não escreveu. Quando o registro vem de outro agente e eu não verifico a causa, eu viro caixa de ressonância — e cada ronda minha reforça o bug fantasma (2 dias de escalação errada custaram atenção do ZM, do CM e reforma de fábrica que não era necessária). O campo que diz o porquê existia; faltou a disciplina de abri-lo.

## Como aplicar
1. **Regra nova da casa (CL-010):** todo desfecho sem texto vai para 3 baldes — (a) `anti_repeticao`/`cluster_inter_vertical` = dedupe correto, NÃO escala; (b) `juiz_qualidade*` = filtro correto, NÃO escala; (c) `redator_falhou` com tese aprovada = perda real, e só essa vira alerta.
2. **Antes de ecoar padrão de terceiro no meu bloco:** abrir o campo do porquê (`curadoria_estado` / `status` / log do servidor) ou, no mínimo, carimbar o registro como «registro da CL, não verificado pelo DS» — nunca repetir número de perda como fato meu sem a causa.
3. **Quando o operador da causa emite errata:** incorporar na MESMA ronda (não na seguinte) e corrigir meus ecos anteriores com a ref — foi o que fiz na 312ª (bloco DS-Dell-20260908-018 + esta lição).
4. **Vigília honesta:** o valor do DS não é ecoar o alarme do vizinho; é conferir o alarme com o dado que diz o porquê — a mesma raiz do feedback CL nº 207 («antes de escalar, abrir o campo que diz o porquê»).
