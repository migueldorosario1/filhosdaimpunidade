# Sonda do espelho: o MÉTODO define o veredito (.htm 404 vs REST per-ID 200) — ronda 214ª (00:00 06/09)

## O quê
Na abertura da ronda 00:00, a sonda do 400490 (vigília DSC-064) por URL .htm no espelho (https://cafezinho.news/400490.htm) respondeu 404 — o que QUEBRARIA a série de 95 confirmações anteriores. Antes de reportar mudança de estado, repeti a sonda no método canônico da casa (mirror REST per-ID: https://cafezinho.news/wp-json/wp/v2/posts/400490 com follow) → 200. Falso alarme evitado: o .htm só cobre posts ESPELHADOS (propagados por slug); o REST per-ID cobre o ID no banco do espelho — os dois respondem coisas diferentes.

## Por quê
A lição do DS-Dell já declarava o método (mirror REST per-ID com follow), mas eu usei a URL .htm por hábito da sonda de slug (usada para ver propagação de post novo). O 400490 é um post do ESPELHO (nascido lá, id 400490) — sua URL .htm pode não existir mesmo com o post vivo no banco (formato de link do espelho é por slug .htm, mas nem todo id tem slug canônico espelhado); o REST per-ID é a fonte da verdade da vigília. Método errado → leitura falsa → alarme falso ou quebra indevida de série.

## Como aplicar
1. Sonda de ID do espelho (400490 e congêneres da vigília) = SEMPRE mirror REST per-ID com follow (wp-json/wp/v2/posts/<id>) — nunca a URL .htm.
2. Sonda de propagação de post NOVO (ex.: 269176) = slug .htm no espelho é o indicador certo (o post nasceu no canônico e precisa propagar).
3. Antes de declarar mudança de estado em série vigiada (200→404, propagou/não propagou), repetir no método da série + anotar o método no bloco.
4. Bônus da ronda: canônico REST exige -L (301 para www.ocafezinho.com) — sem follow, leitura vazia/301 também vira falso negativo.
