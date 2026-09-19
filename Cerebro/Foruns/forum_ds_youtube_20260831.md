# Fórum — DS Nuvem YouTube: robô no ar + batismo de fogo (ordem Miguel, ref DSC-20260831-012)

**Data:** 31/08/2026 · **Operador:** ZCode/GLM-5.3 (Dell) · **GATE:** Claude Laura (Consenso Duplo antes de publicar)

## O que existe (arquitetura)
| Peça | Onde | Papel |
|---|---|---|
| Cérebro `~/ds_youtube/ds_youtube.py` | Tencent, cron :07/:22/:37/:52 (flock) | fila → transcrição → flash matéria → rascunho WP → canal + PEDIDO DE GATE |
| Porta `~/ds_youtube_fetcher/fetcher_youtube.sh` | Dell, cron */5 (flock) | yt-dlp (legendas pt manuais+automáticas, info.json, thumbnail) → entrega na Tencent → marca BAIXADO; live ativa → AGUARDANDO_VOD; sem legenda → baixa áudio p/ Whisper |
| Fila `Foruns/youtube/queue_youtube.md` | repo ponte | entrada única (Telegram via DS-N Chefe, DSC, bloco VIDEO_PRO_DSYOUTUBE) |
| Canal `Foruns/youtube/canal_ds_youtube.md` | repo ponte | provas, pedidos de gate, CHECK 1/h |
| Relatórios `Relatorios/ds_youtube/` | repo ponte | diário + INDEX (regra DSC-006) |
| Conta WP `cafezinhodsn1` (ID 5801, editor) | cofre Dell+Tencent (`WP_USER/WP_APP_PASSWORD_CAFEZINHO_DSN1`, backup datado, sha8 c78617c2/2271fea3) | rascunhos com autoria DS própria |

## Por que a porta mora no Dell (achado estrutural)
O YouTube bloqueia extração por IP de datacenter: Tencent e NYC testados em 31/08 com todos os player_clients (web/ios/tv/mweb/web_embedded) → "Sign in to confirm you're not a bot". O IP residencial do Dell passa limpo. A porta é burra (só baixa), o cérebro é na Tencent (como o Miguel mandou). Limitação honesta: fila anda quando o Dell estiver ligado.

## Lei da casa (item 4 do prompt, preservada)
DS YouTube NÃO publica. A matéria entra na esteira NORMAL: capa (thumbnail/frame COM CRÉDITO do canal, ou acervo/PD — decisão tribunal/CL) → **Consenso Duplo com Claude Laura** (o rascunho NÃO leva zizi_job_id: fica fora do fluxo autônomo do Publicador; só sai com consenso CL citado na ponte, que o Publicador pega pelo scan) → Publicador publica com prova REST.

## Batismo de fogo (KLjB9eQ5d9o — "Sabatinas das Cunhãs 2026")
- Live ENCERRADA (VOD 68min) — não precisou de AGUARDANDO_VOD.
- Legendas automáticas pt (1,19MB json3) → transcrição 13.291 palavras com timestamps.
- Flash DeepSeek (dsh headless, chave canônica; 1ª tentativa falhou: dsh sem DEEPSEEK_API_KEY no ambiente — curido) escreveu matéria 12,8KB: furo = Elmano (PT-CE) chama de "absolutamente mentiroso" dado de feminicídio atribuído a Ciro; embates de segurança, concursos, meio ambiente; citações com [HH:MM]; FONTE + PAUTA-CHEQUE.
- Rascunho WP **268440** (conta DS 5801; role editor — slip meu p/ "autor" corrigido em <1min) + capa candidata **268439** (thumbnail oficial, crédito "Divulgação/YouTube — canal As Cunhãs").
- **PEDIDO DE GATE postado no canal** → Claude Laura decide; Publicador executa ao ver consenso citado.
- Curas no caminho: meta custom via REST = erro (vínculo vídeo↔post vive na fila/canal); json3→txt com dedup de rolagem.

## O que falta
1. DS-N Chefe passar a por links de YouTube do Telegram na fila (patch do prompt da ronda feito — ver memória).
2. Primeiro ciclo autônomo ponta a ponta (item novo PENDENTE → ... → publicado) — a estrutura foi validada por peça, o encadeamento completo roda no próximo vídeo real.
3. Whitelist de canais (se o Miguel quiser restringir origem).

## O que preciso de você (Miguel)
- Nada bloqueante. Se quiser, mande o próximo link por Telegram (o Chefe agora poe na fila) e o robô faz sozinho.

## [Adendo 01/09 14:20 BRT — ZM] 🧪 CURA DO ROBÔ EM MODO TESTE + 1º CICLO AUTÔNOMO E2E COMPLETO (Roni Lessa)

**Ordem do Miguel (~14:00):** "conserta o DS YouTube, mas está em teste — não deixa ele publicar nada no Cafezinho antes da gente ter certeza que ele funciona."

**3 bugs achados e curados (tudo com backup + prova + rollback):**
1. **Porta Dell morta por auto-deadlock de flock** — o crontab chamava `flock -n /tmp/ds_youtube_fetcher.lock fetcher_youtube.sh` e o script tentava pegar O MESMO lock internamente (`flock -n 9 || exit 0`): toda execução via cron saía muda. O batismo passou porque foi manual. Cura: flock externo removido do crontab (backup `crontab.bak_pre_fix_20260901`); o interno fica.
2. **Porta presa ao git do Dell** — `git pull --ff-only origin` falha pela divergência estrutural 397×465. Cura: fila lida/gravada VIA SSH no clone da Tencent (que sincroniza bem). Backup `fetcher_youtube.sh.bak_pre_fix_20260901`.
3. **`rodar_flash` com bug de parse bash desde o nascimento** — o `export DEEPSEEK_API_KEY="$(... tr -d '"''''")"` tinha um `)` dentro de aspas duplas → o `$(` nunca fechava → `bash -c: unexpected EOF while looking for matching ')'` → flash NUNCA rodou sozinho (batismo foi semi-manual; reproduzido e provado com echo). Cura: linha reescrita com aspas balanceadas (`tr -d '"')`), py_compile OK, teste `chave=35_FLASH_OK`. Backup `ds_youtube.py.bak_pre_flashfix_20260901`.

**1º CICLO AUTÔNOMO E2E COMPLETO (14:05→14:15):** porta baixou legendas pt (6.702 palavras) + thumbnail oficial → item BAIXADO → robô transcreveu → flash escreveu a matéria «Ronnie Lessa quebra o silêncio: primeira entrevista do assassino confesso de Marielle Franco» → **rascunho WP 268553** (autor cafezinhodsn1, capa mídia 268552 = thumbnail c/ crédito Divulgação/Record) → **ENTREGUE_GATE** com pedido de Consenso Duplo no canal.

**🧪 MODO TESTE (a pedido do Miguel):** (a) robô não tem caminho de publicar — código cria apenas `status: draft` (0 ocorrências de "publish" auditadas); (b) trava de processo gravada no canal `canal_ds_youtube.md`: **Claude Laura NÃO aprova matérias YouTube até avaliação do Miguel**; (c) prova viva: 268553 = `post_status draft`, 0 ocorrências em publish (wp-cli cafezinho-wp 14:1x).

**O que falta / preciso do Miguel:** ler o rascunho 268553 (está no gate) e dizer: aprovou o robô? Aí a CL faz o Consenso Duplo e o Publicador publica. Rollback total: restaurar os 2 `.bak_*` + linha do crontab (backup guardado).

— ZCode/GLM-5.3 (ZM) · 01/09/2026 14:20 BRT
