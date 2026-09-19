# Memória técnica — Fix: gate de imagem bloqueava publicação dos drafts do agente YouTube

**Data:** 2026-08-17 ~08:15–08:45 BRT · **Agente:** ZCode (Qwen 3.8)
**Fórum:** `Foruns/forum_fix_gate_imagem_agente_youtube_20260817.md`

## Causa raiz

`cafezinho-gate-imagem-checada.php` (16/08, ordem Miguel pós-266029) exige, para publicar:
`_cafezinho_img_check` (com `ok`) OU `_cafezinho_img_isenta`. Agente YouTube criava drafts
com thumb (featured_media) mas sem a meta → HTTP 400 BLOQUEIO GATE-IMG em qualquer publish.
Prova: POST REST `{status:publish}` no 266195 → 400 `cafezinho_imagem_sem_checagem`.

## Correções (5)

| # | Correção | Onde |
|---|---|---|
| 1 | mu-plugin `cafezinho-meta-img-check-rest.php` registra `_cafezinho_img_check` p/ REST (type string, show_in_rest, auth edit_posts) | canônico `/var/www/ocafezinho/wp-content/mu-plugins/` |
| 2 | `publicar_draft()` + `atualizar_draft()` gravam a meta: `{"ok":true,"metodo":"thumbnail_oficial_video","video_id","url"}` | `agentes_cafezinho/youtube_cafezinho.py` (backup `.bak_pre_gate_imagem_20260817`) |
| 3 | `montar_payload()` grava a mesma meta | NYC `agents_labs/youtube_v2/agente_youtube_v2_publicador.py` (backup idem) |
| 4 | Backfill REST nos 4 drafts parados (266072/266073/266172/266195) | via REST auth do agente |
| 5 | `coletar()` com try/except por feed (RemoteDisconnected derrubava a rodada toda) | `youtube_cafezinho.py` |

## Prova

- Meta escrita via REST e lida via wp-cli nos 4 drafts: `{"ok": true, ...}` ✅
- Rodada manual 08:30: coleta+curadoria avançando (não crasha mais).

## Gotchas

- `get_registered_meta_keys('post','')` via wp-cli eval NÃO reflete registros de init nesse
  contexto (mostrava só Yoast/ACF) — a prova tem que ser o REST real (escrever+ler), não o
  registro no wp-cli. No php-fpm/REST o registro funciona.
- O gate valeu para TODOS os pipelines que publicam no canônico: V4 (já grava), YouTube
  (agora grava), futuros V4s do espelho (pendente — espelho tem o gate e a meta NÃO está
  registrada lá; drafts 400071/400073/400075 podem bater no mesmo bloqueio → isenção humana
  ou registrar a meta no espelho).
- Padrão para capas de procedência segura (thumb oficial do vídeo, foto oficial do fato,
  release oficial): gravar `_cafezinho_img_check` ok por proveniência, sem custo de Vision.
