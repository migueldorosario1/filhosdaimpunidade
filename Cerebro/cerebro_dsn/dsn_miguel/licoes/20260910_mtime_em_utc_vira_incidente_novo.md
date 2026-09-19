# O mtime lido pelo WP-CLI vem em UTC — e vira "incidente novo" que não existia

**Data:** 10/09/2026 (ronda 403ª DS-Dell) · **Família:** «o mecanismo responde sem ter feito» (182·184·187·190·191·198·200·201) + BUG-201 (fuso)

## O quê
O primeiro medidor da ronda imprimiu `maintenance mtime=2026-09-10 14:02:18`. A leitura
imediata era: «o upgrader **rearmou** o gatilho às 14:0x» — ou seja, um incidente NOVO no
BUG-193 (o `.maintenance` que sobrevive no disco e rearma o 503 a cada update).

**Não rearmou.** O mtime real é **11:02:18 BRT** — o mesmo da manhã, 6 h 30 de resíduo sem
alteração.

## Por quê (causa provada por 3 vias independentes)
1. `date_default_timezone_get()` no WP-CLI = **UTC** → `date('Y-m-d H:i:s', filemtime())`
   imprime **UTC**, não a hora do site. `date()` e `gmdate()` deram o **mesmo** valor (14:02:18).
2. `date -d @1789048938` na física local = **2026-09-10 11:02:18 -03**. O epoch é o mesmo do
   registro das 11:02.
3. **O conteúdo do arquivo** (`$upgrading = 1789048938`) é o **mesmo** valor da manhã. Um
   rearme de verdade gravaria `time()` novo — o carimbo mudaria, e o mtime também.

## O erro gêmeo, na direção oposta, na mesma ronda
`_cafezinho_origem` foi lido com `is_array($o)` e devolveu **`-` (ausente)** para 269630/269789/269792.
O meta é **JSON em STRING** (`{"via":"rest","ua":"...","user_id":5470,"ts":"..."}`) — o campo
**existe**. Ou seja: **falso positivo** no mtime e **falso negativo** no meta, do mesmo
instrumento, em 20 minutos.

## Como aplicar
- Todo `mtime` lido por WP-CLI sai **rotulado**: `epoch` + `UTC` + `local`. Hora do site se lê
  com `current_time()`, nunca com `date()`.
- **Conferir o metadado contra o conteúdo**: o `$upgrading` antigo foi o que me salvou. Carimbo
  que muda sem conteúdo que mude **não é evento**.
- `_cafezinho_*` é **JSON-string**: `json_decode` do valor; `is_array()` mente.
- Antes de abrir incidente a partir de um campo de tempo, perguntar **em que fuso esse campo
  fala** — é a 3ª vez no mesmo dia que essa pergunta decide entre bug e nada (201, 202, 203).

## Frase-âncora
**O carimbo não é o evento.** Um número plausível (14:02) com cara de novidade é o esconderijo
perfeito para uma leitura em outro fuso.
