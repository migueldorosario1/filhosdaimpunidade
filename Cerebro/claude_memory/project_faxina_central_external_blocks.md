---
name: faxina-central-external-blocks
description: "Frente external_blocks_v1 — tirar legenda/interlink/newsletter do post_content via choke point único (util_blocos_externos.py). Decisão Miguel = faxina central. Sistema pausado, aguarda §92."
metadata: 
  node_type: memory
  type: project
  originSessionId: d7137897-dcad-4847-af64-a409ee24938c
---

# 🧹 Faxina central — external_blocks_v1 (separar blocos operacionais do corpo editorial)

**Decisão de Miguel (2026-06-02 ~03:00 BRT):** resolver o vazamento de bloco operacional no corpo visível por **FAXINA CENTRAL (choke point único)**, não remendando rota por rota.

**Why:** o checkup Lote 4 (#254928→#254872, 100º post varrido) reconfirmou o defeito sistêmico nº1 — legenda "Ilustração editorial sobre {título}" e crédito "(Ilustração: Cafezinho / Wan 2.6)" aparecendo no texto que o leitor lê. Arquitetura `external_blocks_v1` (Codex + Miguel) tira legenda + "Leia também" (interlink) + newsletter/Mailchimp do `post_content`, jogando para `post_meta` + render via snippet WPCode. Opt-in via flag `CAFEZINHO_EXTERNAL_BLOCKS_META=1`. Posts antigos nunca migrados.

**How to apply:** ao retomar esta frente, lembrar que:
- A pendência do Codex listava **6 rotas paralelas**, mas a auditoria do Claude mostrou que o escopo real é **~15 rotas** (figcaption) e **~20** (newsletter hardcoded). Não confiar na contagem de 6.
- **Fonte única do par legenda+crédito: `gerador_imagem_editorial.py:517`** — mesmo f-string cria os dois (`resultado["legenda"] = f"Ilustração editorial sobre {titulo_limpo}. (Ilustração: Cafezinho / {gerador_nome})"`).
- O motor central `motor_publicador.py` JÁ respeita a flag (L1994 lê env, L2014 `append_html`, L2034 figcaption só se NÃO external_blocks, L2078-2086 meta, L2247 newsletter fora do corpo, L2277 o POST). As **rotas paralelas NÃO respeitam** — elas é que precisam do choke point.
- Plano: novo `util_blocos_externos.py` com `strip_blocos_operacionais(html)` + `montar_metas_external_blocks(media_id, related_id, newsletter)`; motor refatorado pra chamar o helper; 1 linha por rota paralela antes do POST; helper só age quando a flag está ligada.
- **Divisão §13 proposta** (no inbox do Codex): Claude escreve `util_blocos_externos.py` + refactor do motor; Codex revisa + adapta as paralelas.
- **Nada deployado.** Sistema PAUSADO. Deploy só via §92 (Miguel + Claude no fórum + revisão Codex §12 + backup B2 + rollback + smoke). Não viola [[feedback_soltar_posts_nao_prender]] porque saneia e publica, não retém.

**Fórum vivo:** `Foruns/forum_external_blocks_interlink_newsletter_20260602.md` (tem auditoria das rotas + design do helper). Indexado também no Boletim News Cafezinho (seção datada 2026-06-02) e relaciona com [[feedback_simular_renderizacao_nao_html_cru]].

**Smoke já feito pelo Codex:** rascunhos 255107/255108/255110/255113 (HTTP 201). Smoke 2 mostrou legenda duplicada → snippet WPCode NÃO deve renderizar legenda (legenda fica só na Media Library).

## ✅ ETAPA 1 FECHADA E APROVADA (2026-06-02 03:33 BRT) — só local, ZERO deploy
- Miguel decidiu **Codex coda**, Claude revisa §12. Codex criou `root/util_blocos_externos.py` + refatorou `motor_publicador.py` (backup local `motor_publicador.py.bak_pre_util_blocos_externos_20260602_032301_codex`).
- Helper: `external_blocks_enabled()`, `strip_blocos_operacionais(html)`, `montar_metas_external_blocks(...)`, `aplicar_external_blocks(...)`. Só age com flag on; fail-safe; idempotente.
- Motor: import com fallback local; guard da newsletter em L2271 (`if not _external_blocks_meta_enabled` injeta legado, senão fica fora); strip aplicado antes da newsletter.
- **Bloqueador que EU achei na revisão §12 (re-testei contra a `CAIXA_NEWSLETTER_AJAX` REAL, não snippet):** os patterns originais deixavam `<hr>` + `</div>` órfão + `<script>mailchimpCallback…</script>` INTEIRO no corpo (vazamento de JS — classe do post 254854). Causa: `<div id="mc_embed_signup">.*?</div>` não-guloso parava no 1º `</div>` aninhado. **Fix (1 pattern consolidado):** `r'(?:<hr\b[^>]*>\s*)?<div\b[^>]*id=["\']mc_embed_signup["\'][^>]*>.*?mailchimpCallback.*?</script>'`. Codex aplicou; eu re-testei: caixa some 100%, idempotente, flag OFF devolve corpo idêntico (sem regressão), `py_compile` OK.
- **Pré-requisito ETAPA 2 (paralelos):** para CADA robô confirmar o markup REAL da legenda antes de adaptar (checkup achou legenda como texto solto → algum paralelo não usa `<figure class="cafezinho-featured-caption">`). Padrão = robô não injeta com flag on; strip é defesa.

## 🔌 MECANISMO DA PAUSA + RELIGAR (descoberto 2026-06-02 03:33 BRT)
- Sistema pausado via **crontab do Tencent 100% comentado** (`sudo crontab -l` → 0 linhas ativas). Prefixos de pausa, 4 categorias: `PAUSADO_CODEX_20260601_ALL_CRONTABS`, `_PUBLICADORES_PARALELOS`, `_COLETORES_SEM_PUBLICADOR`, `_INCIDENTES_QUALIDADE_DEDUPE`.
- **Nenhum processo Python de publicação rodando**, sem screen/tmux, ubuntu-crontab vazio. Posts a cada ~2h (último 255112 03:03) = drenagem de agendados/resíduo, NÃO cron vivo. Religar via crontab NÃO duplica.
- **Religar = restaurar crontab** (descomentar os `PAUSADO_CODEX_20260601_*` ou empurrar `crontab_server.txt`), com backup + rollback (§92). **Cuidado:** religar `_PUBLICADORES_PARALELOS` reintroduz os vazamentos que a faxina conserta (Etapa 2 ainda não feita); `_INCIDENTES_QUALIDADE_DEDUPE` foi pausado por incidentes de qualidade/dedupe. Religar primeiro o NÚCLEO auditado (coletores + maestro + motor central) é o caminho seguro.

**Próximo passo objetivo:** decisão de Miguel sobre ESCOPO do religar (núcleo auditado agora vs tudo agora). Depois: backup crontab → religar → smoke → documentar rollback → indexar.
