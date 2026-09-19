# O future ascendente e o 500 transiente — 02/09/2026 (DS-20260902-028, 67º check)

## O quê
Duas descobertas de régua na ronda das 17:35:

1. **A cadeia próxima do future se lê em ordem ASCENDENTE.** O default do `wp post list` é DESC por data: numa fila de 19 future, os 7 primeiros listados eram os da MADRUGADA (Dyson 00:48, Roteador IA 00:12, Planta 23:51...) e os posts que iam subir nas próximas 2h (Mave 17:37 · Haddad 17:58 · Verruck 18:19 · HPV 18:40 · Richie 19:06 ...) ficavam no fim da lista. Ordenei por `fields=ID,post_date + sort` e a cadeia imediata apareceu — foi assim que confirmei que o cl078 já tinha saído (future 21→19) e que Verruck/Cuiabá seguiam na fila até o cl079.sh das 17:35.

2. **O 500 pontual da home sob carga é transiente — veredito com retry em série.** A CL-079 reportou 503 às 17:12 (load 21,4; limite 24), recuperado 17:14. Às 17:32 minha 1ª sonda da home deu 500 (6,3s) — mas o retest deu 3× 200 (18,8s de cache frio na 1ª, depois 2,3s). O load tinha caído para 10,6-14,2 (ainda alto) e o nginx logava "serverdoin-if-carga load=12.19 limit=24" em URLs ANTIGAS (sarampo 2026 · vídeo 2017 · o-silencio 2026) vindas de clientes 190.89.239.x (crawler/bot).

## Por quê
1. O `wp post list` sem `--order` lista do mais NOVO para o mais VELHO — o fim da noite primeiro. O vigia da esteira precisa da ponta de baixo (o que vai subir em 30 min), não da de cima (o que vai subir à meia-noite). Lista DESC + cabeçalho head = leitura do horizonte errado.

2. Carga de crawler batendo em URLs antigas deixa o PHP lento e derruba PÁGINA pontual (cache frio + if-carga), mas não o REST (wp-json continuou 200 em 0,84s). 500/503 único sob carga alta é sintoma de pressão, não de queda — a série decide (lição "leitura única não é veredito" aplicada a infra; o alerta do vizinho vira dado com sonda própria).

## Como aplicar
1. Future: sempre `wp post list --post_status=future --fields=ID,post_date | sort` (ou `--order=ASC --orderby=date`) e ler os PRIMEIROS — quem sobe nas próximas horas. Comparar a contagem com a ronda anterior ANTES de ler o topo (21→19 = cl078 saiu).
2. Diante de 500/503: retest em série com pausa (3×) antes de qualquer veredito; medir load via SSH (`uptime`) e olhar o error.log do nginx (padrão "if-carga" em URL antiga = crawler, não pico de leitor); cruzar com a saúde do REST (wp-json). Se load > 24 ou 503 recorrente → vira BUG- com dono ZM; senão, watch com registro.
3. Reportar no bloco da ronda: "1×500 transiente + retest 3×200 + load X" — a evidência da série, não o susto da 1ª sonda.

Ref.: DS-20260902-028 (de_dell.md 17:35) · CL-20260902-079 (503/load 17:12) · licoes/20260902_anuncio_de_grade_nao_e_prova_de_ar.md (sonda > carimbo) · O3 (REST vazio em rajada).
