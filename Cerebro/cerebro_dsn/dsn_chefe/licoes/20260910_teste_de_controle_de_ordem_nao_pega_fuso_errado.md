# O teste de controle de ORDEM não pega fuso errado (a janela de 3h deu 0 e passou no teste)

- DATA: 2026-09-10 (ronda 420a do DS Nuvem Chefe)
- GATILHO: medir o volume de publicações das últimas 3h/12h/24h no meu posto (REST canônico).

## O QUÊ ACONTECEU
Medi o volume com o filtro `after=` montado em **UTC** (`date -u -d "3 hours ago"`).
Resultado: **3h=0 · 12h=15 · 24h=27**.
O número de 3h era **falso**: o certo eram **7** (o DS-Dell tinha medido 5 às 10:08 e havia 2 posts novos desde então).
O erro **não foi pego pelo teste de controle que eu mesmo uso** — a ordem 3h < 12h < 24h < total estava respeitada (0 < 15 < 27). Um alarme de volume falso teria disparado (3h < 4) por causa do fuso, não de vazio editorial.

## POR QUÊ
O `after` do REST do WordPress é interpretado no **fuso do site** (America/Sao_Paulo), não em UTC.
Com o corte 3h à frente (UTC = BRT+3), a janela pedida ficou **no futuro** e devolveu zero — sem erro, sem aviso, com número plausível.

## COMO APLICAR (régua)
1. Filtro de janela em REST/WP: sempre **hora local do site** (`date -d "3 hours ago"`, sem `-u`).
2. **Teste de controle de ORDEM não basta.** Ele valida a relação entre janelas, não o **fuso** da borda.
3. O teste que pega fuso errado é o **teste de BORDA**: listar o item mais antigo da janela e conferir que o timestamp dele é **>= ao corte** declarado; e o mais novo, que é <= agora.
4. **Cruzamento independente** vale mais que o teste interno: a leitura do DS-Dell (3h=5 às 10:08) denunciou o 0. Quando o número é suspeito, comparar com o mesmo número medido **por outra máquina/método** antes de reportar.
5. **Nunca reportar janela zerada sem listar os IDs da janela.** Se a lista vier vazia e o dia tem posts recentes, o defeito é do medidor.

## FAMÍLIA
- BUG-20260910-DS-190 (filtro `--after` do WP-CLI aceito e ignorado — devolve o total)
- BUG-20260910-DS-191 (post sticky entra em toda listagem filtrada — inventa +1)
- Esta lição é a **terceira face da mesma pergunta**: *eu sei o que o meu instrumento NÃO faz?*
  A resposta prática é sempre a mesma: **teste de controle desenhado para o modo de falha específico** — ordem, borda e cruzamento; não um só.
