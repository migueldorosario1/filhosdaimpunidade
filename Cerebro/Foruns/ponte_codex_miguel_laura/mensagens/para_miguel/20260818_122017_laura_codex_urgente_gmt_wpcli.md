# Urgente — publishes antecipados explicados por GMT incorreto, não por WP-CLI

```yaml
de: LAURA-CODEX
para: MIGUEL
ts_brt: 2026-08-18T12:20:17-03:00
prioridade: ALTA
ref_commit: 8d09e622
wordpress_mutations: 0
server_mutations: 0
```

Miguel, a memória nova atribui os publishes antecipados 266410/266424 a um bug
do WP-CLI e recomenda SQL direto. O comando documentado, porém, passou a mesma
hora nos campos local e GMT. Em BRT, `12:15` local é `15:15` UTC; informar
`post_date_gmt=12:15` faz o core enxergar o horário como passado e converter
`future` para `publish`.

O teste 266414 não isolou a hipótese: ao trocar WP-CLI por SQL também corrigiu
GMT de 12:15 para 15:15. A documentação/código oficial confirma a comparação
contra `gmdate()` em `wp_insert_post()`:
<https://developer.wordpress.org/reference/functions/wp_insert_post/>.

Veredito: `GMT_INCORRETO_NO_COMANDO` é causa provável forte. Sugiro suspender a
regra de SQL direto, porque ela contorna hooks/cache/transições, e reproduzir em
rascunho seguro com GMT correto antes de criar helper. Se for necessário
agendamento manual, também validar retorno/duplicidade de
`wp_schedule_single_event()`:
<https://developer.wordpress.org/reference/functions/wp_schedule_single_event/>.

O 266414 ainda retornava 401 no REST público às 12:20, compatível com não
publicado. LAURA-CODEX não tocou WordPress, servidor, cron ou credenciais.

— LAURA-CODEX
