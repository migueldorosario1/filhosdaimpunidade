# Lição 05/09/2026 — Na leitura de volume, o HOST decide (canônico × espelho)

## O que aconteceu
Ronda 191ª (12:00): na consulta de volume, usei por engano `https://cafezinho.news/wp-json/wp/v2/posts` e obtive números que não fechavam com nada da casa: X-WP-Total 6099 (o canônico tinha 78.943), posts do dia com IDs 400xxx (400556 às 03:36) e o post 269127 retornando rest_post_invalid_id. Quase reportei no relatório 12:00 "total caiu para 6.099" e "269127 sumiu" — duas anomalias falsas.

## Causa raiz
`cafezinho.news` é o ESPELHO (cópia de segurança que o ZM opera), uma instalação WordPress SEPARADA com IDs próprios (série 400xxx) e total próprio. O site CANÔNICO (produção, o que o Miguel lê e onde os 269xxx vivem) é `https://www.ocafezinho.com`. O DS-Dell já lia "REST canônico www" — o "www" era o domínio, não um detalhe.

## O que aprendi (como aplicar)
1. ANTES de ler volume/total: confirmar o host. Canônico = www.ocafezinho.com (IDs 26xxxx, total ~78.944) · Espelho = cafezinho.news (IDs 400xxx, total ~6.099) · Painel de gestão = controle.ocafezinho.com.
2. X-WP-Total do espelho NÃO fecha com o canônico — é outra instalação; comparar totais entre eles é comparar maçãs com laranjas. A vigília DSC-064 usa o ID 400490 NO ESPELHO (per-ID = 200) — esse é o uso correto do espelho.
3. "Número que não bate com a série da casa" é sinal de host errado, não de sumiço — conferir a URL antes de decretar anomalia (mesma família da lição "o rodapé mentiu, a medição estava viva": verificar a FONTE antes do veredito).
4. Bônus de método: o filtro after/before do REST usa a hora do SITE (BRT) — usar date local, nunca date -u (lição da ronda 180ª reaplicada).

## Verificação
Consulta correta 12:02 no canônico www.ocafezinho.com: total 78.944 (78.943 + 269127), 12/12 hoje com 269127 Corinthians 11:58 no topo, 3h=6 · 12h=12 · 24h=42. Espelho 400490 = 200 (72ª confirmação DSC-064).
