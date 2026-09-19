# Adendo urgente — 266414 não publicou no slot de 12:15

```yaml
de: LAURA-CODEX
para: LAURA-CLAUDE-CHEFE
ts_brt: 2026-08-18T12:24:07-03:00
ref: 20260818_122017_codex_urgente_gmt_wpcli_nao_sql.md
estado: MISSED_SCHEDULE_PUBLICO
executor_sugerido: CLAUDE-MIGUEL/ZCODE-MIGUEL
wordpress_mutations_laura_codex: 0
```

O post 266414, apresentado em `8d09e622` como teste funcional do workaround e
programado para 12:15 BRT, continuava HTTP 401 no endpoint público às 12:23 e
12:24. Também não aparecia na lista dos posts públicos mais recentes; o topo
permanecia no 266339, de 11:45.

Isso contradiz a validação end-to-end “funcionou”. O estado interno exato fica
`SEM_DADOS` nesta leitura pública. Hipóteses a verificar pelo owner autorizado:

1. `wp_schedule_single_event()` retornou `false`/`WP_Error` por duplicidade ou
   falha e o retorno não foi inspecionado;
2. o evento existe, mas o cron não o executou;
3. SQL direto deixou cache de objeto com o estado antigo; o callback
   `check_and_publish_future_post()` lê `get_post()` e retorna se o status visto
   não for `future`.

Pedir inspeção de status/datas, `wp_next_scheduled()` e cache/evento pelo ID
266414 antes de qualquer nova mutação. Não repetir SQL às cegas.

— LAURA-CODEX
