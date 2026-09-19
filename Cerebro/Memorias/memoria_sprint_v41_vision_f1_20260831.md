---
name: sprint-v41-vision-f1-poc-20260831
description: Sprint V4.1 Vision (ZM, GLM-5.3) — F1 POC provada E2E + adapter WP dry-run + curas (chave DeepSeek morta no .env do ciclo, espelho NYC divergido); aguarda "vai" p/ --execute no 268380
metadata:
  type: project
---

# Sprint V4.1 Vision — F1 (31/08/2026, ZCode/GLM-5.3 Dell)

Dono: ZM. Fórum operacional: [[forum-sprint-v41-vision-zm-20260831]] (`cerebro/Foruns/forum_sprint_v41_vision_zm_20260831.md`, blocos -001 abertura / -002 relatório F1). Carta do CM: `carta_para_zcode_miguel_sprint_v41_vision_20260831.md`.

## O que foi provado (31/08 10:09→10:48 BRT)

1. **POC E2E no draft real 268380** (Chen Ye/Nature Index): cascata completa `draft_image_selected_mapping_pending` — banco vazio → Flickr/OpenCatalog coletam → visão dupla DeepSeek×Qwen rejeita os impertinentes → IA flux-pro gera → 1ª rejeitada → **autocura 2ª APROVADA** (conf 0.9, centralidade 0.82, crop_safe) → promovida ao banco auditado. 2m36s, ≲US$0.25 no dia (4 gerações + ~8 visões).
2. **Tema BR 268393** (Ituverava): Flickr allowlist RENDERIZOU foto real local (CC BY 2.0, conf 1.0, score 95) rejeitada por gate editorial JUSTO (`subject_not_prominent`: inauguração ≠ seca). Fail-closed funcionando nas 2 direções.
3. **Adapter `codigo/wp_apply_featured_image.py`** escrito + dry-run OK: fail-closed, sha256 casado, MD5 anti-canibal, 100% REST (metas registradas pelo mu-plugin), carimbo `_cafezinho_img_check` no formato exato do gate `cafezinho-gate-visao-capa.php` (ok:true + media_id = thumbnail), readback de prova. Default dry-run; --execute só com "vai" CM+Miguel.

## Decisão de arquitetura (F1-a)

Caminho A `media_vision_providers.py` (doublecheck + gates + contrato v2) = canônico. Router B `v4_vision_router.py` órfão vira fonte declarativa das rotas extras (Kimi assinatura/paygo; KIMI_VISION_API_KEY AUSENTE no env) a integrar como providers A na F2, junto com Google/Psic Vision. Não reescrever o provado.

## Curas de infra (feitas no caminho)

- `/root/.env` NYC tinha DEEPSEEK_API_KEY MORTA (sha8 b6c4d4de; a cura 29/08 não chegou no .env do ciclo) → trocada pela viva f0aaa272, backup `.env.bak_pre_dskey_viva_20260831`. Regra 4 aplicada sem perguntar.
- Espelho NYC divergiu (cron mirror falhando non-ff desde 30/08): patch-id provou 14/14 commits só-no-espelho com equivalente no GitHub → realinhado c/ backup ref `backup_divergencia_20260831` (23749c513). Cron OK de novo.

## Pegadinhas (L-lessons do sprint)

- Editoria do pipeline ≠ categoria WP: mapa de 4 (`ciencia_tecnologia_ia`/`politica_economia`/`geopolitica_internacional`/`cultura`); "tecnologia" explode `generated_image_editoria_invalid`. F2 mapeia.
- Tese já suportada: `frame_visual.tese_principal` (gerador lê; `curadoria_tese.py` produz) — F2 liga.
- Wikimedia 429 no download (recorrente).
- Collector espera o OBJETO request (não `request.subject()` dict); evaluator máx 5 visões/cascata; geração IA tem autocura 2×.
- 1ª POC "sem seleção" era SÓ editoria errada — o pipeline estava certo o tempo todo.

## Estado / o que falta / preciso do Miguel

- ✅ Feito: F1-a/b/c(dry-run) + curas + fórum -001/-002 + monitor + commit.
- ⏳ F1 final: **"vai" CM+Miguel** p/ `--execute` no 268380 → checagem dupla CM/CL (olho humano na imagem, regra sagrada) → publish HTTP 200.
- 🔶 Miguel: Psic Vision (o que é/onde está a credencial?) e se Google Vision vale vs Gemini ativo.
- F2: integração `v41_ciclo.py` (adapter pós-redator + flag `_cafezinho_capa_pendente_v4` + mapeamento categoria→editoria + tese automática); F3: banco/Scout (derruba custo IA); F4: aprovação anual.

— ZCode/GLM-5.3 · 2026-08-31 10:49 BRT
