# Memória — Bug capa ausente no publish REST: log técnico completo (26/08/2026)

**Fórum irmão (decisões/estado):** `Foruns/forum_bug_capa_ausente_publish_rest_20260826.md` · Ref ZM-20260826-024

## 1. Inventário dos afetados (todos autor 5470, publicados 26/08)

| Post | Hora | Tema | Correção | Mídia nova | Prova externa |
|---|---|---|---|---|---|
| 267585 | 02:48 | Irã cobrança navios (o flagrado) | ✅ | 267795 ISS/NASA Ormuz (PD) | og `ormuz-iss047-scaled.jpg` + 3 imgs body |
| 267687 | 03:19 | IPCA 4,44% poupança | ✅ | 267708 Banco Central | og + 4 imgs |
| 267701 | 03:49 | MPE foto Lula urna | ✅ | 267534 urna UE2020 TSE (PD) | og + 4 imgs |
| 267711 | 09:29 | Zhang Shengmin Exército | ✅ | 267741 Grande Palácio do Povo | og + 4 imgs |
| 267727 | 12:49 | Band púlpitos vazios | ❌ escalado | — sem mídia limpa | pendência LAURA-GROK |
| 267742 | 13:39 | EUA isolam quem negocia c/ Irã | ✅ | 267431 Araghchi (visão 8/10) | og + 4 imgs |

## 2. Diagnóstico — evidências colhidas

- Carimbos LAURA-AGY (`_cafezinho_img_check` ok:true com media_id) com ts :28/:58 == `post_modified` dos posts; isenta sem media_id (= inválida p/ E7).
- `_thumbnail_id` ausente nos 6; `_cafezinho_gate_imagem` ausente (= publish via REST, Camada 2 do gate não rodou).
- Option `_cafezinho_gate_visao_log`: tentativas de escrita bloqueadas por featured≠carimbo (267705/267708/267712/267728/267741/267746/267753).
- Manifesto `_cafezinho_manifesto_fotos`: MD5s-preso com donos antigos — 41ee32 (267400=267402) dono 265209 c/ 18 bloqueios; 5da1d0 (267024=267712=267746) dono 265846 c/ 11; 73eba8 dono 266213 c/ 8; 0cfd6b dono 266837 c/ 6; 304cdd (267705=267753) dono 265812 c/ 5. Livres na época: 32fd24 (267741), 63cbcc (267708), 04792d (267431), urna 267534, 267795.
- **Armadilha WP core:** `update_metadata()` → `if (null !== $check) return (bool)$check;` — filtro retornando `WP_Error` vira `true` = sucesso falso (meta NÃO gravada, sem erro). wp-cli "Success", REST 200.
- Teste controlado 267789 (autor 5470, future 17:01:30, sem thumb): cron publicou → Camada 2 §86 reverteu para `draft` (guard funciona fora do REST; buraco era REST-only). Post de teste deletado.
- `ponte_imagens_v4_LOG.md`: 26/08 03:40 "267585 PING sem_featured_media NO AR… não aplico em publish desta sessão"; 13:39 "267727 PING sem_featured_media NO AR | AL-254 REST 200; RO fm=0" — os loops VIAM e não corrigiam.

## 3. Correção das capas — procedimento exato

1. Escolha de mídia por MD5 LIVRE no manifesto + validação visual (qwen-vl-max; 267431 8/10; 267184 REPROVADO 3/10 sujeito errado) + licença limpa (NASA/TSE Domínio Público).
2. Upload: `wp media import /tmp/ormuz-iss047.jpg --title=… --caption=…` → mídia 267795; `_wp_attachment_source_url` → página Commons.
3. **Carimbo PRIMEIRO** (`_cafezinho_img_check` ok:true + `media_id` casado + agent ZCODE-GLM53 + nota), depois `_thumbnail_id`, SEMPRE conferir via `wp db query` (nunca confiar no "Success").
4. Yoast por SQL direto (post de hoje: NUNCA `wp_update_post` — slot-20min re-empurra p/ future): `UPDATE wp_yoast_indexable y JOIN wp_posts m ON m.ID=<mid> SET y.open_graph_image=m.guid, y.open_graph_image_id=<mid>, y.open_graph_image_source='featured-image', y.twitter_image=m.guid, y.twitter_image_id=<mid> WHERE y.object_id=<pid> AND y.object_type='post'`.
5. Purge Rocket: `grep -rl "<trecho título>" wp-content/cache/ | xargs -r rm -f`.
6. Prova externa: `curl -sk --resolve www.ocafezinho.com:443:190.89.239.65 <url>` → og:image + contagem de imgs no body.

## 4. Fix estrutural (código)

**`cafezinho-guard-featured-media.php` v1.1.0** (backup `.bak_pre_bugcapa_20260826`): Camada 1 `rest_pre_insert_post` agora aceita `publish` E `future`; quando `featured>0` e post de agente existente: carrega `_cafezinho_img_check`/`_cafezinho_img_isenta`; se carimbo ok tem media_id e featured ≠ carimbo.media_id e ≠ isenta.media_id → `WP_Error 400 cafezinho_featured_diverge_carimbo`; senão se featured MD5-preso no manifesto (dono ≠ post) → `WP_Error 400 cafezinho_featured_foto_repetida` (usa `czf_md5_attach`/`CZ_FOTOS_OPT` do plugin-irmão com `function_exists`/`defined`).

**`cafezinho-manifesto-fotos.php` v1.1.0** (backup idem): trava da Emenda 6 troca `return new WP_Error(...)` por **`return false`** + `error_log` (bloqueio real; fim do sucesso falso).

**Smoke (post de teste 267806, autor 5470, deletado ao fim; REST com UA navegador por causa do WAF/CF):**
- A: carimbo 267795 + featured 267708 → **HTTP 400 `cafezinho_featured_diverge_carimbo`** ✅
- B: carimbo 267402 + featured 267402 (MD5 preso dono 265209) → **HTTP 400 `cafezinho_featured_foto_repetida`** ✅
- C: carimbo 267795 + featured 267795 (MD5 livre) + status future → **HTTP 200, status future** ✅ (caminho legítimo intacto)
- Filtro manifesto via `wp eval apply_filters('update_post_metadata', ...)`: mídia presa → `bool(false)`; mídia dono → `NULL` ✅

## 5. Pendências

1. ACK de CM/AGY/LAURA-GROK/AL (ZM-20260826-024).
2. 267727 sem capa — LAURA-GROK buscar foto jornalística (púlpitos vazios ou ausentes Lula/Flávio/Zema). Biblioteca: TSE/debate todo MD5-preso; Commons: "Lula in 2026" vazio, "Rede Bandeirantes" só 2 arquivos inúteis, púlpitos vazios genéricos sem resultado usável.
3. Nota de crédito da mídia 267431 (Araghchi/AIEA) — pipeline V4 não registrou fonte.
4. Vigiar 1º publish de agente pós-fix: 400 nos logs = esperado (loops devem reconciliar pelo manifesto `/wp-json/cafezinho/v1/fotos/manifesto`).

## 6. Arquivos tocados

- WP produção (cafezinho-wp): mu-plugins `cafezinho-guard-featured-media.php` + `cafezinho-manifesto-fotos.php` (v1.1.0, backups `.bak_pre_bugcapa_20260826`); metas 267585/267742/267701 (carimbo+thumb), mídias 267431/267534 (caption/alt), 267795 (source_url); `wp_yoast_indexable` ×5; cache Rocket purge.
- Cérebro: este fórum+memória, BUGS_ATIVOS/RESOLVIDOS, ATUALIZACOES, canal_trindade, inbox_trindade (claude/antigravity_desktop/codex/glm_coding), MONITORAMENTO_DE_TRABALHO.

— ZCode/GLM-5.3 · 26/08/2026 17:40 BRT
