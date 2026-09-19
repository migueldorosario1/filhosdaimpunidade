# Memória — PD-1: canal cafezinho-wp-write ganha publish + schedule (21/08/2026)

**Tema:** extensão da identidade de escrita da Laura (PD-1) — publicação direta autorizada pelo Miguel.
**Fórum pareado:** `Cerebro/Foruns/forum_ponte_laura_completa_20260817.md` (ADENDO 21/08/2026 17:39).
**Gatilho:** ordem direta do Miguel 21/08 ~13:00 (voz, chat Laura) registrada em `cerebro/Foruns/loop_trindade_laura/controle/recebidas/20260821_1300_ordem_miguel_autorizacao_publicar.md` + pedido formal CL-20260821-018 item 2 na ponte.

## Contexto de governança

- Revogado o limite "corrigir sim, publicar não" (18/08).
- Pacto de publicação por consenso duplo: Claude Laura (check editorial/textual) + LAURA-AGY (check técnico/visual); quem estiver na vez do ciclo publica com 2/2 checks. Máx. 1 post/30 min (regra editorial do loop, não aplicada no servidor).
- Parceria plena CL×AGY + escala intercalada no cron (:12 CL, :27 AGY, :42 CL, :57 AGY) — AL-20260821-022.
- Exclusividade de publicação do Claude Miguel (Regra 10 provisória do protocolo anti-conflito) SUPERADA; ciência dada no canal Trindade 17:39.

## Mudança técnica (log completo)

**Arquivos editados (canônico 190.89.239.65:51439):**
1. `/usr/local/sbin/cafezinho-wp-write` (wrapper Python, validate): aceitação de `publish <id> ["data"]` e `schedule <id> "data"` (data como 1 arg quoted ou 2 args soltos; regex `YYYY-MM-DD HH:MM(:SS)?`).
2. `/usr/local/libexec/cafezinho-wp-write-query.php` (lógica PHP): `publish` saiu da `$forbidden_ops`; 2 casos novos no switch + helpers `laura_wr_norm_date()` (valida/normaliza data) e `laura_wr_gmt_sane()` (repara gmt zerado derivando de post_date). Whitelist passou de 7 para 9 ops.
3. Reader (`/usr/local/libexec/cafezinho-wp-write-reader`) e authorized_keys: NÃO tocados.

**Backups (rollback):** `/root/pd1_write_backup_20260818/cafezinho-wp-write-query.php.bak_pre_publish_20260821_1426` e `cafezinho-wp-write.bak_pre_publish_20260821_1426`. Rollback = restaurar os dois arquivos.

**Comportamento das ops novas:**
- `publish <id>` → status publish AGORA. Se o post tinha data futura (ex-future), a data vira `current_time('mysql')` (senão o core converte publish→future silenciosamente). GMT zerado é reparado.
- `publish <id> "YYYY-MM-DD HH:MM:SS"` → backdate permitido; data futura → erro de negócio `date_is_future_use_schedule` (exit 0 + JSON ok:false).
- `schedule <id> "YYYY-MM-DD HH:MM:SS"` → status future; exige data ≥ now+2min (senão `date_not_future`); `post_date_gmt` SEMPRE derivado server-side via `get_gmt_from_date()` — o caller nunca envia gmt (previne o bug `post_date_gmt=0000-00-00` de 18/08).
- Ambas exigem `edit_date => true` no `wp_update_post` — sem isso o WP ignora post_date/post_date_gmt (achado do teste; na rodada 1 o schedule virou publish imediato por causa disso).
- Resposta JSON de sucesso traz o estado FINAL: `post_status`, `post_date`, `post_date_gmt` (re-fetch pós-update).

**Gates do site que seguem valendo (mu-plugins carregam apesar do `--skip-plugins` do reader):**
- `cafezinho-gate-imagem-checada.php` (fail-close): publish sem `_cafezinho_img_check` ok ou `_cafezinho_img_isenta` → revertido para pending.
- §86 (thumbnail obrigatória): publish sem featured image → revertido para draft (`[CAFEZINHO-§86]`).
- `cafezinho-protecao-editorial.php`: post com status `publish` E autor fora da lista automática (5470/5786/5787) = "post_publicado_por_humano" → wp-cli bloqueado (wp_die) em update/meta/delete/taxonomy. Override humano declarado: env `CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1`.
- Interação descoberta: em post de autor NÃO automático, o gate-img tenta reverter o publish mas a proteção mata o processo no meio (wp_die na meta de log) — o post FICA publicado. Em produção não ocorre (posts de agente têm autor automático), mas explica o comportamento dos testes com posts criados pelo root.

**Provas (posts descartáveis 266938-266944, todos apagados depois):**
- Rodada 1 (autor root): expôs os dois achados acima + cleanup com override humano.
- Rodada 2 (autor 5787 = condições de produção): publish sem recibo → JSON final `post_status=draft/pending` (fail-close vivo); schedule → future com gmt = local+3h correto; set-img-check → publish → publicado; publish em ex-future → publica agora; backdate aplicado; gmt zerado reparado (`0000-00-00` → valor real); wrapper via `SSH_ORIGINAL_COMMAND` OK (health/schedule aceitos, delete e data inválida negados); auditoria no auth.log registrando allowed/denied.

**Ponteiros:** ZM-20260821-001 (resposta na ponte) · ledger/estado atualizados · canal Trindade 21/08 17:39.
