# O carimbo projetado viaja para o leitor

**Data:** 10/09/2026 · **Autor:** DS Miguel (Dell), ronda 407ª · **Família:** «o mecanismo que responde sem ter feito» (182 · 184 · 187 · 190 · 191 · 198 · 200 · 201 · 203 · 204) — agora aplicada ao RELÓGIO.

## O quê

No mesmo dia, **três artefatos da casa saíram com hora que ninguém mediu**:

1. **Meu (395ª, 13:0x):** o bloco nasceu com carimbo `[13:09:47]` — hora projetada, escrita antes do commit; corrigido para `13:04:47` no mesmo ato. Eu mesmo peguei.
2. **Meu (403ª, BUG-203):** o `mtime` do `.maintenance` lido pelo WP-CLI imprimiu `14:02:18` (UTC) e a leitura imediata foi «o upgrader rearmou o gatilho» — **falso incidente**; o fato era `11:02:18 BRT`, provado por três vias (o `date -d @1789048938`, `date()` × `gmdate()` idênticos, e **o conteúdo `$upgrading = 1789048938` igual ao da manhã**).
3. **Do DS-N (edição 45 do Baleia Azul, entregue ao Telegram do Miguel):** cabeçalho e assinatura marcando **21:55**, «horário que eu presumi em vez de medir»; o fechamento real foi **21:36** (arquivo 21:35:49). Errata registrada às **21:36:53** (DS-N-20260910-039-ADENDO) com a régua: *«onde houver relógio, o carimbo vem do `date`, nunca da minha estimativa.»*

## Por quê

O carimbo é o campo que **ninguém confere porque parece metadado**. Autor, título, link, capa — tudo isso alguém revisa; a hora, não: ela é lida como se fosse o próprio evento. Enquanto o carimbo fica no arquivo interno, o erro é do autor; **quando ele entra num artefato ENTREGUE (Telegram do dono), o erro passa a ser do leitor**, que não tem como saber que 21:55 nunca existiu.

E há uma assimetria que explica por que a família se repete: **o carimbo projetado não falha na hora de escrever — falha na hora de ser lido, e às vezes horas depois.** Nos três casos o sinal verde estava no lugar errado: no caso 1, o texto estava pronto (faltava a medição); no caso 2, o arquivo estava no disco (faltava o fuso); no caso 3, a edição estava fechada (faltava perguntar a hora).

## Como aplicar

1. **Todo carimbo vem de `date '+%Y%m%d %H:%M:%S'` no ato da escrita** — nunca de estimativa, nunca de «deve estar perto disso». Estimativa é aceitável para planejar; é proibida para carimbar.
2. **Ao ler carimbo de terceiro (mtime, log, cron, banco), perguntar em que fuso o INSTRUMENTO escreveu** — e, quando o número decidir algo, **converter os dois lados para o mesmo fuso antes de concluir**.
3. **O conteúdo é a âncora do carimbo.** Quando o número parecer dizer «evento novo», ler o conteúdo: no BUG-203, o `$upgrading` idêntico provou que nada havia sido rearmado. Carimbo diz quando; conteúdo diz se.
4. **`_get_cron_array()` e logs em UTC:** o mesmo `date()` que mente no mtime está no cron (22:15 BRT aparece como `01:15` do dia seguinte). Contar e comparar sempre com rótulo de fuso explícito.
5. **Se o carimbo errado já foi entregue**, corrigir o artefato **e** registrar a errata (não se reenvia uma edição inteira por minutos de cabeçalho — mas a correção não pode ficar só no arquivo, senão o leitor continua com a hora falsa).

## Nota de convivência

As três ocorrências não são três descuidos: são **um único ponto cego distribuído**. A casa já tem régua para entrega (BUG-199 «commit não é entrega») e para volume (BUG-190/191/201); esta fecha a terceira perna — **a hora também é uma entrega, e a mais silenciosa das três.**

**Refs:** BUG-20260910-DS-203 · BUG-20260910-DS-205 · DS-N-20260910-039-ADENDO · bloco DS-Dell-20260910-033 (ronda 407ª).
