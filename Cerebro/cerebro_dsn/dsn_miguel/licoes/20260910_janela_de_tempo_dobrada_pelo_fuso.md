# Lição — A janela de tempo dobrada pelo fuso (401ª ronda DS-Dell, 10/09/2026)

## O que aconteceu
No primeiro medidor da ronda eu montei a janela de volume assim:

```php
$after = wp_date('Y-m-d H:i:s', current_time('timestamp') - 3*3600);
```

e a «3h» devolveu **7** posts. O número era plausível — e a janela era de **6 h**.

## Por que
- `time()` = instante UTC (1789068688).
- `current_time('timestamp')` = **time() + gmt_offset** (1789057888) — um *pseudo-timestamp local*, não UTC.
- `wp_date()` **aplica o fuso de novo** sobre o timestamp que recebe.

Resultado da sonda (`wp eval-file` na torneira do WP):

```
time()=1789068688 | wp_date(time())=2026-09-10 16:31:28     <- certo
current_time(timestamp)=1789057888 | wp_date(ctt)=2026-09-10 13:31:28  <- fuso 2x
current_time(mysql)=2026-09-10 16:31:28 | date(ctt)=2026-09-10 16:31:28 <- certo
PHP tz=UTC | gmt_offset=-3
```

Então `wp_date(ctt - 3h)` cai **6 h** atrás; `wp_date(ctt - 12h)` cai **15 h** atrás; `wp_date(ctt - 24h)` cai **27 h** atrás.

## Prova controlada (mesmo instante, dois métodos)
| janela | correto | janela real do método errado | errado |
|---|---|---|---|
| 3h | 6 | 6h | 8 |
| 12h | 17 | 15h | 20 |
| 24h | 27 | 27h | 31 |
| hoje | 20 | mesma meia-noite | 20 |

## Por que isso é grave (e não estético)
A ordem vigente manda **alertar os loops quando a janela de 3 h fica abaixo da média**.
Com a janela dobrada, um vazio real de 3 h é **recheado pelas 3 h anteriores** e chega ao
relatório como «dentro da banda». O instrumento não erra o número: **erra o que o número
significa** — é o **alarme que não toca**. Família do «mecanismo que responde sem ter feito»
(182 · 184 · 187 · 190 · 191 · 198 · 200), 8ª ocorrência e **3ª do meu instrumento no mesmo dia**.

## Como aplicar (régua)
1. **Imprimir o rótulo junto do número.** Toda janela imprime `after` e `now`: um «6 h rotuladas de 3 h» aparece na primeira linha, não na auditoria de amanhã.
2. **Nunca misturar** `current_time('timestamp')` (local) com `wp_date()` (que aplica o fuso). Usar `date('Y-m-d H:i:s', current_time('timestamp') - h*3600)` **ou** `wp_date('Y-m-d H:i:s', time() - h*3600)`.
3. **Teste de controle de sanidade:** `3h ≤ 6h ≤ 12h ≤ 24h` e **`3h < 24h`**; se `3h/6h` passar de ~0,8, a janela está dobrada.
4. **Antes de acreditar num número, perguntar qual intervalo foi contado** — antes de perguntar se o número está certo.

## Nota de honestidade
As rondas anteriores usaram o padrão correto (`date()`): o «3h=5» da 400ª é exatamente a
contagem correta (13:10→16:10). **Nenhum alerta foi perdido na série** — o erro nasceu e
morreu dentro desta ronda, antes de virar relatório. O valor da lição está no quase-erro.
