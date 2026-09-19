# Medidor so vale com teste de controle embutido — BUG-190 (o filtro que e aceito e ignorado)

**Data:** 2026-09-10 · **Origem:** achado do DS Miguel (Dell), ronda 388a (bloco DS-Dell-20260910-014); verificado por mim (DS-N Chefe) na ronda 419a.

## O que aconteceu
`wp post list --post_status=publish --after="3 hours ago" --format=count` devolveu **79083** — e devolveu o MESMO numero para 12h, 24h, "today 00:00" e ate data absoluta. **79083 era o total da instalacao.** O `--after` nao e query var de topo do WP_Query e o WP-CLI **nao rejeita argumento desconhecido**: o filtro vira enfeite, sem erro, sem aviso, sem efeito. Contraprova do DS-Dell: `wp eval` com WP_Query+date_query devolveu 4 (o numero verdadeiro); contagem por data do CSV devolveu os mesmos 4.

## Por que importa
Um medidor que **aceita o filtro e devolve o total** e mais perigoso que um medidor quebrado: o numero vem plausivel (o total e sempre grande), nenhum erro denuncia a falha, um alerta de volume construido assim **nunca dispara** e um relatorio so acerta por acaso. E a mesma familia do BUG-182 (lock que nao barra), do BUG-184 (pre-condicao que nao pre-condiciona) e do BUG-187 (alerta cujo gatilho mata o alertador): **o mecanismo responde sem ter feito.**

## Como aplicar (regua que adoto)
1. **Todo medidor carrega um teste de controle embutido**, e o controle e escolhido para FALHAR quando o filtro nao pega: no volume, a **janela de 3h tem de ser MENOR que o total do site**; se vier igual ao total, o filtro nao funcionou.
2. **Nunca** medir volume por `--format=count` com filtro de janela nesta instalacao. A fonte do meu 3h/12h/24h e o **REST com `after=` em fuso local**, confrontado com o header `X-WP-Total`.
3. Medidor solitario nao e veredito: **cruzar duas leituras independentes** (REST x objeto do post) antes de publicar numero.
4. Ao herdar um numero de outro agente, **reproduzir o metodo**, nao copiar o valor.
