# Vigília com marco único cego: o deploy andou 4h antes do cron-alvo (ronda 93º, 10:30)

## O quê
A vigília do V4.2 Investimento (DSC-064) tinha marco único "pós-14h: confiro o 1º rascunho `_v42_*` no espelho" — mas o 1º ciclo saiu às **09:59/10:01** (posts 400353 e 400358 PUBLISHED no espelho, cat 100007, com imagem + tribunal de mídia), ~4h antes do cron-alvo das 14h. O ZM (deploy) recebeu ordem direta do Miguel ("tem que ter imagem, obviamente… tribunal de mídia"), implementou o tribunal, calibrou ao vivo (reprovou o 1º gráfico nota 4 → rascunho; aprovou o corrigido nota 10) e publicou no espelho. O marco da vigília (14:30) teria encontrado o fato 4h depois da publicação; quem pegou o fato foi a leitura REST **por categoria** da ronda 10:30 (1 GET barato).

## Por quê
Marco único de vigília é cego a mudanças de janela do dono do deploy: ordem direta do Miguel + deploy manual do ZM podem antecipar o marco em horas. O cron de 14h segue no ar, mas o "1º post" (o fato que o DSC-064 me mandou reportar ao Miguel) não esperou o cron — saiu na mão do fluxo do tribunal.

## Como aplicar
1. Vigília de espelho/lab = **sondar por categoria a CADA ronda** (1 GET REST `?categories=<id>`, custo zero), não só no marco formal — o marco vira "confirmação formal + reporte ao Miguel com prova", não "primeira detecção".
2. Quando o dono do deploy está ativo (ordens diretas do Miguel), reconferir antes do marco; quando está mudo, o marco único basta.
3. Reporte ao Miguel assim que o fato subir (dever DSC-060/064: "reporta o 1º post de teste"), com URL e prova (carimbo, nota do tribunal) — feito nesta ronda (msg 155, @dscelular_bot).
4. Registrar também o contexto de segurança quando houver (o mesmo espelho sofreu SQLi na janela — o reporte levou as duas notícias: marco V4.2 + decisão B do ataque).
