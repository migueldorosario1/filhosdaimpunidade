# Fórum — Guarda estrutural §86: impossível aprovar/publicar sem imagem destacada

> [!CAUTION]
> **ROTA DE REDAÇÃO SUPERADA EM 09/08/2026.** As conclusões sobre o incidente de imagem permanecem históricas; a descrição do agente antigo como parte do V4 não é mais operacional. Ver `Memorias/memoria_arquitetura_v4_canonica_pos_cutover_20260810.md`.

**Data abertura:** 2026-07-30 ~16:20 BRT
**Autor:** Kimi K3 (ZCode)
**Ordem direta Miguel:** "duas matérias da categoria tecnologia sem imagem. O que houve? Conserta isso e conserta estruturalmente, para não poder aprovar isso"
**Status:** ✅ RESOLVIDO no mesmo dia (fix cirúrgico + 4 camadas estruturais deployadas e testadas)

---

## 1. O que aconteceu (sintoma)

Dois posts da vertical **Ciência/Tec V4** foram ao ar em 29/07 **sem imagem destacada**, visíveis na home de `/tecnologia/`:

| Post | Título | Publicado (BRT) | zizi_job_id |
|---|---|---|---|
| 263426 | Morte de criança em teste genético na China foi ocultada por meses… | 29/07 11:49 | `v4d_ciencia_432bb0f625144daf` |
| 263428 | Kabum! lança robô aspirador com base autolimpante e 90 dias… | 29/07 12:20 | `v4d_ciencia_3441e1536dc44264` |

Violação direta da **§86** (imagem destacada obrigatória, inscrita 22/05 após caso idêntico).

## 2. Cadeia causal completa (4 elos, todos verificados em log/DB)

1. **Redator cria rascunho sem imagem (por design).** O worker V4 (`/root/v4_vertical_draft_worker.py`, NYC) invoca `agente_controlado.py` com `skip_image=True` — a imagem (cartoon) só é anexada DEPOIS pelo worker, com readback. Log: `Imagem=None` no `ciencia_draft_agent.log`.
2. **Gate editorial bloqueia — mas o rascunho já existe.** `validate_title_clarity()` abortou ambos com `editorial_semantics_title_ellipsis_forbidden` (reticências no título). O worker registrou `editorial_blocked` com `wp_post_id: null` e **não escondeu nem descartou o rascunho órfão** — ficou como `draft` aprovável.
3. **Redator já tinha enviado os botões de aprovação.** `notify_telegram_draft_review()` mandou o Telegram com "✅ Publicar Agora" **sem nenhum aviso de que não havia imagem**.
4. **Aprovação cega sem guarda.** Miguel clicou "Publicar Agora" (11:49 e 12:20 BRT). O handler `wp_audit_publish` do `bot_zizi_linda.py` chamava `wp_update_post(post_id, status="publish")` **sem checar `featured_media`** → publish sem imagem.

## 3. Fix cirúrgico (29/07 → corrigido 30/07 ~16:40 BRT)

- **263428:** og:image da fonte (Canaltech — foto real do produto) → media **263609** → `featured_media` setado + crédito.
- **263426:** og:image da fonte (SCMP — foto laboratório/biotech) → media **263610** → `featured_media` setado + crédito.
- Hierarquia §86 Prioridade 1 (og:image da fonte original). Readback OK; página `/tecnologia/` verificada: ambos os cards renderizam imagem.
- **3 órfãos idênticos ainda na fila** (mesmo modo de falha, vertical Nacional: 263574, 263571, 263498 — todos `editorial_blocked` por reticências, rascunhos sem imagem) → movidos para `pending`.

## 4. Cura estrutural (defesa em profundidade, 4 camadas)

| # | Camada | Arquivo (produção) | O que faz |
|---|---|---|---|
| 1 | **WP servidor (a trava final)** | `mu-plugins/cafezinho-guard-featured-media.php` (ServerDo.in) | REST: `rest_pre_insert_post` → publish sem thumbnail efetivo = **HTTP 400** (`cafezinho_featured_media_obrigatorio`). Não-REST: `transition_post_status` reverte para draft. **Ninguém publica sem imagem, nem por engano.** |
| 2 | **Bot Telegram (a aprovação)** | `/root/bot_zizi_linda.py` (NYC) | `wp_audit_publish_*` checa `featured_media` ANTES: se 0 → ⛔ mensagem clara + teclado: "🖼️ Publicar com imagem padrão" (`wp_audit_pubfb_`, anexa `FEATURED_IMAGE_ID` e publica — escolha informada), "📝 Manter rascunho", "❌ Descartar". Serviço `zizilinda-cafezinho` reiniciado. |
| 3 | **Redator (a criação)** | `/root/agente_controlado.py` (NYC) | `status_final == publish` sem `image_id` → rebaixa para draft + log anomalia + alerta Telegram. E `notify_telegram_draft_review()` agora mostra "⛔ SEM IMAGEM DESTACADA" em destaque na auditoria. |
| 4 | **Worker V4 (o órfão)** | `/root/v4_vertical_draft_worker.py` (NYC) | No `except` que grava `editorial_blocked`/`failed`: se o rascunho já foi criado no WP (`match`), move para `pending` (some da fila de aprováveis) e registra `orphan_to_pending` no evento. |

**Backups §82:** `.bak_pre_guard_sec86_20260730` nos 3 arquivos NYC; espelhos locais canônicos (`Projeto Cafezinho Agentes/root/`) sincronizados (estavam stale desde o fallback Qwen-VL de 29/07; backup `.bak_stale_pre_sync_20260730`).

## 5. Validação (smoke tests executados)

- **Camada 1:** draft novo sem imagem → `POST status=publish` → **400** `cafezinho_featured_media_obrigatorio` (post segue draft) ✅ · draft sem imagem → publish "caminho do bot" (PATCH status-only) → **400** ✅ · attach imagem → publish status-only → **200 publish** ✅ · update comum em post publicado → **200** ✅.
- **Pegadinha encontrada no teste:** `transition_post_status` no REST revertia publish legítimo (controller anexa `featured_media` DEPOIS do `wp_update_post`). Fix: camada 2 ignora REST (`REST_REQUEST`), camada 1 decide com payload completo. Documentado no plugin.
- **Bot:** `py_compile` local+remoto OK; serviço ativo pós-restart (PID novo).
- **Worker/agente:** `py_compile` local+remoto OK.

## 6. Lições (padrão a vigiar)

- **Fail-open em aprovação humana é bug estrutural:** qualquer botão "Publicar" precisa validar invariantes §86 no ato, não confiar no pipeline.
- **Gate tardio precisa de cleanup:** todo gate que roda DEPOIS da criação do objeto no WP tem de esconder/descartar o órfão no caminho de bloqueio.
- **Notificação de auditoria deve mostrar o estado crítico** (sem imagem, sem fonte, etc.) — o aprovador não pode descobrir no site.
- Recorrência observada: `editorial_semantics_title_ellipsis_forbidden` bloqueou 5+ drafts em 2 dias (títulos com reticências do redator) — vale ajuste no PROMPT do redator (não no gate). Separado deste bug; anotar para próxima sprint V4.

## 7. Endereços

- Bug completo: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` → `BUG-20260730-SEC86-PUBLISH-SEM-IMAGEM`
- Memória técnica: `Cerebro/Memorias/memoria_sec86_guarda_imagem_obrigatoria_20260730.md`
- Regra mãe: `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md` §86
- Caso fundador §86 (22/05): `Foruns/carta_maestro_trindade_miguel_20260522.md`
