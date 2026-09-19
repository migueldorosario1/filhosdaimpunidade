# Adendo urgente — teste 266414 falhou no resultado final

```yaml
de: LAURA-CODEX
para: MIGUEL
ts_brt: 2026-08-18T12:24:07-03:00
ref: 20260818_122017_laura_codex_urgente_gmt_wpcli.md
estado: MISSED_SCHEDULE_PUBLICO
wordpress_mutations: 0
```

O 266414, usado como prova do workaround SQL e marcado para 12:15 BRT,
continuava 401 no REST público às 12:23 e 12:24 e não aparecia entre os posts
publicados. Logo, “ficou future logo após o comando” não provou o desfecho; a
publicação no horário falhou ou ainda não ocorreu.

Sem leitura interna autorizada, não escolho entre evento recusado/duplicado,
cron atrasado ou cache obsoleto após SQL direto. Sugiro que Claude/ZCode Miguel
inspecione agora status/datas, `wp_next_scheduled('publish_future_post',
array(266414))`, retorno do agendamento e cache, sem repetir SQL às cegas.

LAURA-CODEX apenas leu o endpoint público; não tocou WP, SSH, SQL ou cron.

— LAURA-CODEX
