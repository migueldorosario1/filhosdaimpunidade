---
name: feedback-workaround-bug-wp-cli-publish-imediato-20260818
description: "Bug wp-cli publish imediato ao invés de future quando pending tem post_date antigo → resolvido 18/08 12:09 via SQL direto UPDATE + wp_schedule_single_event. Duas vezes causou publish antecipado hoje (266410 09:14, 266424 11:31). Workaround testado e funcional no 266414."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 870114c6-7ee3-4080-8592-299996b3140e
---

## Bug

Ao rodar `wp post update <id> --post_status=future --post_date='YYYY-MM-DD HH:MM:SS' --post_date_gmt='YYYY-MM-DD HH:MM:SS'` num post `pending` com `post_date` antigo (ex.: post do worker V4 que ficou pending desde de manhã), o WordPress dispara o hook `publish_future_post` via `wp-cron` imediatamente, publicando o post **na hora atual**, e resetando `post_date` pra `NOW()` — em vez de deixar o post agendado pra data futura desejada.

## Sintomas hoje

- **266410 (Moraes/Bolsonaro dentista)**: agendei future 12:35 no ciclo 09:08 → publish imediato 09:14 (~6min depois do update).
- **266424 (Conass/SUS)**: agendei future 12:15 no ciclo 11:29 → publish imediato 11:31 (~2min depois).

Nos dois casos, `wp post update ...` retornou `Success: Updated post NNNNN` sem erro, mas o post foi ao ar imediatamente. Log JSONL registrou `bug_wp_cli`.

## Workaround (testado 18/08 12:09 no 266414 — funcionou)

```bash
# 1. SQL direto — bypass do wp-cli, atualiza post sem trigger de hooks
ssh cafezinho-wp "wp --path=/var/www/ocafezinho db query \"UPDATE wp_posts SET post_status='future', post_date='2026-08-18 12:15:00', post_date_gmt='2026-08-18 15:15:00', post_modified=NOW(), post_modified_gmt=UTC_TIMESTAMP() WHERE ID=266414\" --allow-root"

# 2. Re-armar wp-cron event pra publicar no horário futuro correto
ssh cafezinho-wp "wp --path=/var/www/ocafezinho eval \"wp_schedule_single_event(strtotime('2026-08-18 15:15:00 UTC'), 'publish_future_post', array(266414));\" --allow-root"

# 3. Validar
ssh cafezinho-wp "wp --path=/var/www/ocafezinho db query 'SELECT ID, post_status, post_date FROM wp_posts WHERE ID=266414' --allow-root"
# esperado: 266414 | future | 2026-08-18 12:15:00
```

Resultado: post fica `future` com `post_date` correto, `wp-cron` agendado pra publicar no horário certo. **Não dispara publish imediato.**

## Por que funciona

- SQL direto no `wp_posts` **bypassa** os hooks WordPress. Sem hook, sem dispatcher.
- `wp_schedule_single_event(timestamp_utc, 'publish_future_post', array(post_id))` cria manualmente o evento cron pra dispatch na hora correta.
- O timestamp precisa ser em **UTC** (por isso `2026-08-18 15:15:00 UTC` para BRT 12:15).

## Regras de uso

1. **SEMPRE** usar quando agendar future pra pending V4 com post_date antigo (>1h no passado).
2. **NUNCA** usar pra publish imediato (`--post_status=publish` no now) — o hook não é o problema aí, e SQL direto pode confundir cache/comentários.
3. **Validar** com `SELECT ID, post_status, post_date FROM wp_posts` depois — se ficou publish em vez de future, algo deu errado.
4. Log JSONL registrar `metodo=sql_direto_wp_schedule_single_event` para futura auditoria.
5. Se ZCode Miguel quiser transformar isso em helper (`wp_schedule.sh`), integra ao pipeline; enquanto isso, uso comando SSH direto.

## Origem histórica

ZCode Miguel usou padrão parecido 17/08 pra resolver 5 posts future travados (265985, 266027, 266080, 266197, 266225). Detalhes em `Cerebro/monitoramento_horario/bugs_encontrados/` e ledger. Meu caso é preventivo — antes do post travar, não depois.

Ligado a: [[feedback-wp-meta-update-json-grava-vazio-20260817]] (mesma família "wp-cli faz coisa errada silenciosamente").
