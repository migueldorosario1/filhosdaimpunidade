# 2026-09-03 · ESPELHO: seletividade com recuperação parcial NÃO cronológica (4 rondas provadas) — stall seco é só com prova negativa sustentada

## O quê
O espelho cafezinho.news parou de receber o grosso do principal a partir de ~11:47:31 e, nas rondas 98ª→101ª (13:00→14:30), NENHUM post entre 11:57 e 14:18 caiu lá na ordem cronológica: HPV 268544 (11:57), Netflix 268413 (12:37), Hepatite 268407 (12:57), Planta 268427 (13:17), Clipto 268557 (13:37), ConvergeLab 268697 (13:58) e Kallas 268773 (14:18) seguem 404 no espelho com 200 no canônico — enquanto TSE 268821 (12:17) CHEGOU (200 entre 13:05-13:35) e Ceará 268841 (13:56) CHEGOU entre 14:00-14:30, e SP Atlas 268826 (11:47) está lá. Ou seja: o espelho recebe posts FORA da ordem de publicação, pulando intermediários.

## Por quê
Espelhamento com fila/lag por post (seletividade) ≠ stall seco: se fosse atraso cronológico simples, o HPV (11:57, mais antigo) chegaria ANTES do TSE (12:17) — o oposto aconteceu. A observação de "parou às 11:47" das rondas 98ª/99ª era verdadeira mas INCOMPLETA: o mecanismo não parou, está seletivo/lagando, e a recuperação é parcial e não-cronológica. "404 no espelho" em um ponto no tempo não é prova de parada — é prova de ausência NAQUELE post NAQUELE momento.

## Como aplicar
- Sondar o espelho PER-POST por slug (canônico REST dá o slug; espelho usa /<slug>.htm) e registrar 200/404 individual — nunca um veredito global a partir de 1-2 posts.
- Interpretar com a régua: stall seco só com N posts CONSECUTIVOS ausentes E zero chegada em 2+ janelas de 30 min; chegada de post mais novo com ausência de mais antigo = seletividade/lag por post (não cronológico).
- Recuperação parcial (TSE 12:17 chegou; Ceará 13:56 chegou) = o mecanismo está VIVO e processando — reduzir tom de alarme, manter watch com marco.
- Dono ZM segue sem confirmar se é desenho; produção dele exige sessão dedicada — cobrar com a tabela per-post como prova, não com narrativa.
- Registrar a tabela per-ID/per-slug no bloco da ponte para o dono e para a série seguinte (a 98ª sem prova per-ID gerou retrabalho de interpretação).
