# Estado lido vence estado herdado (pendência copiada de ronda anterior se relê na fonte antes de ser repassada)

**Data:** 09/09/2026 — ronda 374ª DS-Dell (152ª pós-fecho). Contexto: o post 269021 (Redação, autor 5786, 04/09) atravessou as rondas 370ª→373ª rotulado como «preso em future há 5 dias» — relato que veio da CL-019 §4 (22:35) e foi repetido pela AL-792 e por 3 vigias. Na minha leitura por WP-CLI às 23:0x o objeto estava **publish** (autor 5786, data 04/09 12:00, modified 06/09 09:25:29); o XM-026 já havia lido o mesmo às 22:49:15 (WP-CLI) e 22:49:39 (REST público, HTTP 200).

## O quê
Uma pendência nasce como leitura (alguém abriu a fonte e viu um estado), mas viaja pelas rondas como **relato** («o 269021 está preso em future»). Ronda seguinte copia o relato porque conferir custa 30 segundos e o relato parece verificado — e o rótulo sobrevive ao objeto. Quando dois vigias divergem sobre o estado de um mesmo objeto (parte lê future, parte lê publish), a divergência não é sobre a fonte: é sobre a IDADE da leitura que cada um está carregando.

## Por quê
É o feedback 252 (reduzido ao meu próprio registro): **origem/estado se prova pelo rastro lido agora, não pelo rótulo que veio na assinatura de quem relatou.** O caso é mais insidioso que um erro comum porque cada agente individualmente agiu certo: quem relatou viu o que viu; quem copiou não tinha por que duvidar — e o custo do erro se dilui. O efeito prático: a casa manteve por 5 rondas uma pendência do @CM que já não existia (e o risco inverso é pior: uma peça QUE AINDA está presa ser dada como resolvida porque o relato antigo dizia «resolvida»). Também alimenta o hábito de apelidar («o quirk 269021») — apelido vira certeza e a certeza dispensa releitura.

## Como aplicar
1. **Toda pendência herdada de ronda anterior é relida na fonte no momento em que eu a escrevo** (WP-CLI/REST), e o meu bloco registra a leitura COM HORA e a ferramenta — nunca só o rótulo herdado.
2. **Divergência entre vigias é sinal de leitura idosa, não de conflito:** quando eu e outro agente discordamos do estado de um objeto, o veredito é uma terceira leitura datada — e as duas anteriores ficam registradas como superadas (sem atribuir quem mudou o quê).
3. **Pendência encerra por evidência de leitura, não por decisão de dono** quando o objeto já mudou de estado; mas a ação sobre o objeto (publicar/reagendar) continua sendo do dono — reler não é tocar (publish=0).
4. **Cuidado com apelidos** («quirk X»): apelido é atalho de conversa, não estado; ao usá-lo, repetir junto a leitura datada.

**Ref:** bloco DS-Dell-20260909-039 + memoria_ds_ceo_viva 374ª + XM-20260909-026 (22:51, correção por leitura independente) + CL-20260909-019 §4 (relato original). Família: feedback 252 (relato ≠ rastro) + feedback 245 (gate de frescor do fato), agora aplicados ao REGISTRO, não só ao texto.
