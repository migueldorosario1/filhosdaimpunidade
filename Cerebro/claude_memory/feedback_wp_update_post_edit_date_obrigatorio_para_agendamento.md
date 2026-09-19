---
name: feedback-wp-update-post-edit-date-obrigatorio-para-agendamento
description: "Ao agendar post WP via wp_update_post com post_status=future, é OBRIGATÓRIO passar edit_date=true além de post_date/post_date_gmt — sem essa flag, WP publica imediato mesmo com fuso correto"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d556bf3a-514a-43d5-a6d6-417905366fd5
---

**Bug reproduzido 13/08/2026 11:22 BRT com 12 posts do lote Kimi.**

## O que aconteceu

Rodei script `/tmp/schedule_12.php` no NYC via `wp eval-file`:
```php
wp_update_post([
  "ID"=>$id,
  "post_status"=>"future",
  "post_date"=>"2026-08-13 12:30:00",              // BRT desejado
  "post_date_gmt"=>get_gmt_from_date($when),        // "2026-08-13 15:30:00" UTC (correto)
], true);
```

**Esperado**: 12 posts agendados nos slots 12:30 → 01:20 (14/08).
**Real**: 12 posts publicaram imediatamente às 11:22 BRT, com `post_date` resetado pra 11:22 (não 12:30).

## Diagnóstico

Verifiquei:
- `timezone_string` = `America/Sao_Paulo` ✅
- `gmt_offset` = -3 ✅
- `get_gmt_from_date("2026-08-13 12:30:00")` = `"2026-08-13 15:30:00"` ✅ correto (BRT+3h)
- `strtotime($gmt) - time()` = 2233 segundos NO FUTURO ✅ deveria agendar
- Nenhum hook `transition_post_status` customizado interferindo
- `wp_get_schedule("publish_future_post")` = `false` — WP nem chegou a agendar cron pro futuro (evidência de que interpretou como "publish agora")
- Categorias intactas (`wp_update_post` não mexe em cats se não passar `post_category`)

## Causa raiz

**Falta a flag `"edit_date" => true` no array de `wp_update_post`.**

Sem essa flag, o WP usa o `post_date_gmt` **anterior** (`$post_before->post_date_gmt`) da criação original do post no seu processamento interno de `wp_insert_post`. Como o post original em `pending` foi criado antes (`post_date_gmt` no passado quando o worker o gerou), a lógica interna `if ('future' === $post_status && strtotime($post_date_gmt) <= time()) $post_status = 'publish'` disparou e o WP forçou publish imediato — resetando `post_date` pra `current_time("mysql")` (agora).

Meu novo `post_date`/`post_date_gmt` foram gravados NO BD (persistiram no array final), mas o **fluxo de decisão de status já tinha executado antes** usando o `post_date_gmt` anterior do post.

## Solução obrigatória

Sempre incluir `"edit_date" => true` quando o objetivo é **agendar** um post existente:

```php
wp_update_post([
  "ID"=>$id,
  "post_status"=>"future",
  "post_date"=>"2026-08-13 12:30:00",
  "post_date_gmt"=>get_gmt_from_date("2026-08-13 12:30:00"),
  "edit_date"=>true,   // ← ESSA FLAG É OBRIGATÓRIA
], true);
```

`edit_date=true` força o WP a usar `$postarr["post_date"]`/`$postarr["post_date_gmt"]` (meus valores) no fluxo de decisão de status, **antes** de comparar com `time()`. Aí a checagem de future funciona corretamente.

## Verificação pós-agendamento

Sempre confirmar após o `wp_update_post`:

```php
$p = get_post($id);
echo "$id | status=$p->post_status | post_date=$p->post_date | post_date_gmt=$p->post_date_gmt\n";
// Esperado: status=future, post_date=2026-08-13 12:30:00
```

Se `status=publish` ao invés de `future` → agendamento falhou, veja se faltou `edit_date=true` ou se `post_date_gmt` que passei já estava no passado.

## Aplicabilidade

- **Agendar post existente** (`draft`→`future` ou `pending`→`future`): `edit_date=true` obrigatório.
- **Publicar imediato** (`draft`→`publish` ou `pending`→`publish` sem post_date custom): NÃO precisa `edit_date`.
- **Atualizar título/content de post publish**: NÃO precisa `edit_date`.
- **Trocar categoria de post publish**: usar `wp_set_post_categories()`, não `post_category` em `wp_update_post` (mais confiável).

## Registro histórico

- 13/08/2026 11:22 BRT: **incidente** — 12 posts Kimi publicaram imediato em vez de agendar.
- 13/08/2026 ~12:00 BRT: **descoberta** via diagnóstico solicitado por Miguel ("primeira coisa é entender pra evitar novo erro no futuro. gravar erro e solução no cérebro").
- 13/08/2026 ~12:00 BRT: **decisão Miguel** aproveitar o publish e remover cat No home dos 15 (não vale reverter tudo pra agendar).
- Backup pré-mudança: `Cerebro/backups_pre_edit/2026-08-13_1200_15posts_remover_nohome_publicar_3pending.json` (43KB, todos os 15 posts com meta+cats+status originais).

Regras irmãs: [[feedback-vigilia-nunca-publicar-batch-agendar-madrugada]] (agendar sempre — daí a necessidade de FAZER O AGENDAMENTO FUNCIONAR) · [[feedback-backup-json-pre-batch-wp]] (snapshot JSON antes de batch ≥5).
