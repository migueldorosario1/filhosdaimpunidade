# YT-PATRULHA — Gate de imagem bloqueava publicação dos drafts do agente YouTube (RESOLVIDO 17/08 ~08:35)

**Tag:** YT-PATRULHA
**Achado por:** ZCode (Qwen 3.8), após Miguel reportar "não entrou mais nenhum post do agente YouTube no cafezinho"
**Status:** ✅ RESOLVIDO com prova de bloqueio + prova de destravamento

## Sintoma

Nenhum post do agente YouTube publicado no Cafezinho desde 16/08 madrugada, mesmo com
drafts prontos (266072, 266073, 266172, 266195) e o Loop Miguel (Claude) publicando V4
normalmente (a fila pending do V4 fluía o tempo todo).

## Causa raiz

O mu-plugin fail-close `cafezinho-gate-imagem-checada.php` (criado 16/08 por ordem direta
do Miguel, pós-incidente 266029) torna **estruturalmente impossível** publicar post sem
`_cafezinho_img_check` (ok) ou `_cafezinho_img_isenta`. O agente YouTube criava drafts com
`featured_media` (thumbnail oficial do vídeo) mas **sem a meta de checagem** — o gate
devolvia HTTP 400 no publish REST e reverteria qualquer publish fora do REST.

**Prova (17/08 ~08:15):** `POST /wp-json/wp/v2/posts/266195 {status: publish}` → HTTP 400
`BLOQUEIO GATE-IMG: impossível publicar sem checagem da imagem (_cafezinho_img_check ok ou _cafezinho_img_isenta)`.

## Correções

1. **Mu-plugin novo `cafezinho-meta-img-check-rest.php`** (canônico): registra `_cafezinho_img_check`
   para escrita via REST (o agente não conseguia nem gravar a meta — meta não registrada).
2. **Agente nacional** (`youtube_cafezinho.py`, backup `.bak_pre_gate_imagem_20260817`):
   `publicar_draft()` e `atualizar_draft()` gravam `_cafezinho_img_check` ok:true com
   `metodo: thumbnail_oficial_video` (a capa É o objeto do post — checagem por proveniência).
3. **Publicador GSN V2 (NYC)** (`agente_youtube_v2_publicador.py`, backup
   `.bak_pre_gate_imagem_20260817`): idem no `montar_payload`.
4. **Backfill** nos 4 drafts parados (266072/266073/266172/266195) — todos com a meta ok.
5. **Bônus:** `coletar()` não morre mais por `RemoteDisconnected` em um feed único
   (a rodada das 08h de 17/08 caiu por isso; o canal derrubava a coleta inteira).

## Prova pós-fix

- Meta gravada via REST e lida de volta via wp-cli nos 4 drafts (`{"ok": true, ...}`).
- Rodada manual (~08:30): coleta + curadoria avançando normalmente.

## Pendências

- Claude (Loop Miguel, único publicador): revisar e publicar 266172/266195/266072/266073
  (inbox + canal Trindade avisados 08:40).
- Espelho (cafezinho.news): o gate existe lá também; os drafts dos novos V4s (400071/400073/400075)
  podem bater no mesmo bloqueio — isenção humana ou meta via wp-cli. Registrar a meta p/ REST
  no espelho quando o caminho de publicação de lá for definido.

## Arquivos

- `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-meta-img-check-rest.php` (novo)
- `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` (patch)
- `NYC:/root/agents_labs/youtube_v2/agente_youtube_v2_publicador.py` (patch)
- Tema Duplo: `Foruns/forum_fix_gate_imagem_agente_youtube_20260817.md` + memória de mesmo nome
