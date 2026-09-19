# Memória técnica — Guarda estrutural §86 (publish sem imagem) — 2026-07-30

> [!CAUTION]
> **ROTA DE REDAÇÃO SUPERADA EM 09/08/2026.** O incidente e as proteções de imagem continuam como histórico válido, mas as passagens que colocam `agente_controlado.py` dentro da cadeia V4 descrevem apenas a arquitetura anterior ao corte. Ver `memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

**Tema:** BUG-20260730-SEC86-PUBLISH-SEM-IMAGEM
**Fórum par:** `Cerebro/Foruns/forum_sec86_guarda_imagem_obrigatoria_20260730.md`
**Executor:** Kimi K3 (ZCode) · ordem direta Miguel ~16:20 BRT
**Estado final:** ✅ fix cirúrgico + 4 camadas estruturais deployadas, testadas e registradas

---

## A. Cronologia da investigação (evidências)

1. **Confirmação do sintoma (API pública WP):** posts 263426 (29/07 11:49:35) e 263428 (29/07 12:20:01), `status=publish`, `featured_media=0`, `author=5786` (`redacao-nova`, identidade V4 desde 27/07), categorias `[735, 19936, 5008, 30]` (Ciência + Tec + IA).
2. **Meta dos posts:** `zizi_job_id` = `v4d_ciencia_432bb0f625144daf` / `v4d_ciencia_3441e1536dc44264`.
3. **Log redator (NYC `ciencia_draft_agent.log`):**
   - `[14:48:04] [TEC] Publicado/Rascunho! ID=263426 | Imagem=None`
   - `[15:11:38] [TEC] Publicado/Rascunho! ID=263428 | Imagem=None`
   (timestamps UTC; o worker roda o redator com `skip_image=True` — imagem é anexada depois pelo worker)
4. **DB worker (NYC `ciencia_tecnologia_ia.sqlite3`, `draft_events`):** ambos os eventos `outcome=editorial_blocked`, `wp_post_id=null`, `detail=RuntimeError:editorial_semantics_title_ellipsis_forbidden`. O gate `validate_title_clarity()` (worker linha ~391) abortou por reticências no título — DEPOIS do rascunho já existir no WP.
5. **Publicação:** `date_gmt` 14:49:35 / 15:20:01 (1–9 min após a criação do rascunho) = clique humano no botão "✅ Publicar Agora" do Telegram.
6. **Buraco de aprovação:** `bot_zizi_linda.py` handler `wp_audit_publish_{id}` → `wp_update_post(post_id, status="publish")` sem checar `featured_media`. `wp_update_post` (linha 965) também não checava.

## B. Arquitetura do fluxo (para quem mexer depois)

```
cron NYC (:10/:40 ciencia) → v4_vertical_draft_worker.py
   ├─ subprocess: agente_controlado.py (env NEWS_STATUS=draft, skip_image=True)
   │     └─ cria post WP status=draft featured_media=0 + meta.zizi_job_id
   │     └─ notify_telegram_draft_review() → botões no Telegram  ← enviava SEM aviso de imagem
   ├─ gates: validate_title_clarity → factual_late_gate           ← bloqueou; órfão ficava draft
   ├─ staging pending → generate_upload_attach_cartoon() → draft  ← nunca executado nos 2 casos
   └─ (bloqueio) candidates.status=editorial_blocked              ← sem cleanup do órfão (antes do patch)
Miguel clica botão → bot_zizi_linda.py wp_audit_publish → PATCH status=publish  ← sem guarda §86 (antes do patch)
```

## C. Mudanças aplicadas (arquivos + backups)

| Arquivo | Host | Backup pré-patch | Mudança |
|---|---|---|---|
| `wp-content/mu-plugins/cafezinho-guard-featured-media.php` | ServerDo.in (190.89.239.65:51439) `/var/www/ocafezinho/` | arquivo novo | REST `rest_pre_insert_post`: publish sem thumbnail efetivo → WP_Error 400 `cafezinho_featured_media_obrigatorio`. `transition_post_status`: publish não-REST sem thumbnail → reverte draft + error_log. Camada 2 **ignora REST** (controller anexa featured_media após wp_update_post — sem esse guard, publish legítimo seria revertido; achado no smoke test). |
| `/root/bot_zizi_linda.py` | NYC (198.199.121.136) | `.bak_pre_guard_sec86_20260730` | Novo helper `wp_get_featured_media_id()`. Handler `wp_audit_` aceita `publish` e `pubfb`: checa imagem antes; sem imagem → ⛔ + teclado [🖼️ publicar c/ imagem padrão (`FEATURED_IMAGE_ID` env, fallback 227658)] [📝 manter rascunho] [❌ descartar]. Serviço `zizilinda-cafezinho` reiniciado (PID novo 1077298). |
| `/root/agente_controlado.py` | NYC | `.bak_pre_guard_sec86_20260730` | Guarda §86: `status_final=="publish" and not image_id` → draft + log + `notify_telegram()`. `notify_telegram_draft_review(..., image_id=None)` novo parâmetro; banner "⛔ SEM IMAGEM DESTACADA" quando ausente; caller passa `image_id=image_id`. |
| `/root/v4_vertical_draft_worker.py` | NYC | `.bak_pre_guard_sec86_20260730` | `except` do loop principal: se `locals().get("match")` tem post criado → PATCH `status=pending` + `orphan_to_pending:{...}` no `detail` do evento (vale para `editorial_blocked` e `failed`). |
| Espelhos `Projeto Cafezinho Agentes/root/{v4_vertical_draft_worker,agente_controlado}.py` | local | `.bak_stale_pre_sync_20260730` | Estavam stale (sem o fallback `_qwen_visual` de 29/07). Sincronizados com NYC: md5 `509446cc…` (worker) e `4c4d5923…` (agente). |

Rollback de qualquer camada: restaurar o `.bak` correspondente (bot: + `systemctl restart zizilinda-cafezinho`; mu-plugin: `rm` do arquivo).

## D. Smoke tests (evidência de comportamento)

- Draft novo 263622/263624 sem imagem: `POST {status:publish}` → **400** `cafezinho_featured_media_obrigatorio`, post permanece draft ✅
- "Caminho do bot" (draft sem imagem + PATCH status-only) → **400** ✅
- Attach `featured_media=263609` + PATCH status-only → **200 publish** ✅
- Update de conteúdo em post publicado (sem tocar status/imagem) → **200** ✅
- `php -l` OK; `py_compile` local e remoto OK nos 3 Python.

## E. Itens corrigidos no mesmo ciclo

- Post 263428 ← media 263609 (foto real produto, Canaltech, webp→jpg) ✅ no ar
- Post 263426 ← media 263610 (foto laboratório, SCMP) ✅ no ar
- Órfãos `editorial_blocked` sem imagem → `pending`: 263574, 263571, 263498 (vertical nacional, mesma causa `title_ellipsis`) ✅
- Nota: meta Yoast `_yoast_wpseo_opengraph-image*` rejeita PATCH via REST pelo usuário redacao-nova (HTTP 400) — inócuo, Yoast cai no featured image por padrão.

## F. Pendências sugeridas (não bloqueantes)

1. Prompt do redator V4 gera títulos com reticências → `title_ellipsis` bloqueou ≥5 drafts em 48h. Ajustar prompt (proibir "…") em sprint V4 separada (exige OK Miguel — mudança de prompt editorial).
2. Nacional tem fila de `image_pending` por `cartoon_visual_rejected_after_4_attempts` (texto renderizado na imagem) — relacionado ao tribunal visual/BUG-20260729-KIMI-VISION-KEY-401 (aguarda chave nova do Miguel).
3. Considerar sweep diário: qualquer draft V4 com >2h e `featured_media=0` → pending automático (hoje coberto pelo patch do worker para órfãos novos).
