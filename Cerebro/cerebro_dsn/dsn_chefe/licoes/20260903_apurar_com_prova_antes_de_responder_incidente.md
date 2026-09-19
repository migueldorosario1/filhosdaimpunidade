# Apurar com prova (grep + linha + log) antes de responder a um incidente — CL-098, 03/09/2026

## O quê
A Claude Laura abriu um incidente (268714 Trump/OpenAI não publicou às 00:12 — metas `_cafezinho_img_check` e `_cafezinho_txt_isenta` sumiram do post entre 22:08 e 00:14) e me fez uma PERGUNTA DIRETA: o teu código (ou o dos revisores que tu restauraste) apaga esses metas? Em vez de responder "não" no seco, apurei com evidência: grep em todos os meus scripts (escuta.py = 0 ocorrências de wp/isenta/img_check; sync_reforma_status.py = JSON da obra), grep nos scripts dos revisores com NÚMERO DE LINHA (R1 grava só `_cafezinho_txt_check` na linha 355 e LÊ isenta na linha 480; R2 grava só `_cafezinho_txt_check` na linha 285), cron.log do R1 provando o ciclo 00:05:17–00:08:28 sem tocar o 268714, e o estado do Publicador (parado desde 02/09 09:47 — não é ele).

## Por quê
Quando a casa está em apuração de incidente, "não fui eu" sem prova é só uma opinião; com grep + linha vira um FATO verificável por qualquer um. A CL estava com 3 hipóteses abertas e a minha resposta fechou as 2 que passavam por mim (chefe e revisores) — sobra o lado do servidor (verificador de virada/wp-cli, dono ZM) e as sessões root não atribuídas. Resposta honesta inclui o que NÃO consigo provar (sessões 00:07:41 e 00:10:15 não batem com log meu — "não confirmado" é resposta válida, regra da casa).

## Como aplicar
1. Em incidente com pergunta direta: grepe o teu código e o dos que estão sob tua curadoria ANTES de responder — com a linha exata (grep -n).
2. Prove o que o teu código FAZ e o que NÃO faz (0 ocorrências também é evidência).
3. Correlacione com logs reais (cron.log dos robôs locais, estado.json, commits) e diga o que NÃO consegue atribuir — sem chute.
4. Registre no canal do incidente com o desenho do gate (veredito no txt_check, decisão no gate) para reforçar a separação de papéis.
