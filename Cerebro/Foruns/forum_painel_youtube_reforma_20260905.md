# Fórum — Reforma da página /v6/youtube do painel CCTV (colunas: onde/publicado, link público confirmado, máquina da transcrição)

**Data:** 05/09/2026 ~20:2x–20:5x BRT · **Quem:** ZCode (GLM-5.3), ordem do Miguel por voz/texto às 20:22
**Ref:** ZM-20260905-010 · **Estado:** ✅ CONCLUÍDO E NO AR (faltando homologação visual do Miguel)

## O pedido do Miguel (quase literal)

A página http://43.156.151.165/v6/youtube "está com vários problemas: não fala onde foi publicado; tem que ter coluna publicado/onde foi publicado; o link da publicação tem que ser o link público CONFIRMADO — não quero link com controle na frente, é o link realmente público; e uma coluna dizendo qual foi a máquina que fez a transcrição — se foi o Transkriptor, foi outro processo. Refaz isso aí."

## Decisões

1. **Cards viraram tabela com 4 colunas** (abas Publicado e Rascunho): Matéria · **Onde foi publicado** · **Link público (real, sem controle)** · **Transcrição por**. Temáticos pausados (GSN/Aiatolah/Mapa Rio) ganharam as mesmas colunas em mini-tabelas.
2. **Link público de verdade:** o REST do painel usa `WP_API=https://controle.ocafezinho.com/...` — era a origem do "link com controle". O link agora é construído no servidor do site (`https://ocafezinho.com/AAAA/MM/DD/slug/`) e **confirmado ao vivo**: o painel abre cada link com UA de navegador (8 fios, cache 10 min) e só imprime ✅ confirmado com HTTP 2xx/3xx (WAF bloqueia UA python — por isso UA Chrome).
3. **Vínculo post→vídeo:** novo modo `cat28` no `transkriptor_status.php` (cafezinho-wp): thumbnail `_wp_attached_file` com prefixo `yt-<id>` (WP grava filename em MINÚSCULAS — toda comparação no painel é case-insensitive via índice lower) → attachments filhos → embed do conteúdo (guarda case correto, devolvido também como `video_embed`). Padrão genérico de 11 chars foi REMOVIDO (casava slugs tipo "io-comercio.jpg" — falso positivo).
4. **Máquina da transcrição** (por video_id): pasta `~/ds_youtube/artifacts/<vid>/` contém `whisper.log`/`segments.jsonl` → 🤖 Whisper local; `*.json3` → 📹 legenda do YouTube; senão video_id no ledger de custos → 🎙️ Transkriptor; senão —.
5. **Aba Rascunho:** link público = "não público ainda" (rascunho não tem URL pública — quem publica é a CL). Aba Canais permanece (fonte monitorada, não publicação).
6. **Fallback:** se o endpoint cat28 cair, o painel usa o REST antigo trocando o host controle→ocafezinho.com (sem video_id; colunas ficam —). Fail-open em tudo.

## Provas (E2E)

- Endpoint cat28: `{"ok":true,"posts":[...]}` com video_id/link corretos (269038 → errxZMgualU + link público real); modo antigo `ids=` em regressão OK.
- `py_compile` 3.12 OK; `cctv-v6` restart ativo; curl interno e público (HTTP 200, 58 KB).
- HTML renderizado: 3× cabeçalhos das colunas novas · **0 links controle** · 24× "✅ confirmado" / 0 "⚠️ não confirmou" · máquinas: 5 Transkriptor, 2 legenda YouTube, 1 Whisper (rascunho 269036) · 0 traceback.
- Screenshot chrome headless QA visual: tabela íntegra, sem overlap/escape (Read PNG → CDN → analyze_image).

## O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** reforma completa no ar nos 3 níveis (PHP do site + painel Tencent + validação pública).
- **Falta:** homologação visual do Miguel nas 3 abas; os vídeos Whisper recentes (vjUTYebq-ts CNN, rpFMvQfzY1U) ainda não viraram matéria publicada — quando a CL publicar, aparecerão com 🤖 Whisper local e link confirmado.
- **Preciso de você, Miguel:** só o "ok" visual (ou apontamentos) — não há pendência técnica conhecida.

## Rollback (1 comando cada)

- Painel: `cp ~/cafezinho/v6/painel_cctv_v6.py.bak_pre_youtube_reforma_20260905_2055 ~/cafezinho/v6/painel_cctv_v6.py && sudo systemctl restart cctv-v6`
- PHP: `cp /var/www/ocafezinho/transkriptor_status.php.bak_pre_cat28_20260905 /var/www/ocafezinho/transkriptor_status.php` (cafezinho-wp)

## Arquivos tocados

- tencent `~/cafezinho/v6/painel_cctv_v6.py` (+ bak `.bak_pre_youtube_reforma_20260905_2055`)
- cafezinho-wp `/var/www/ocafezinho/transkriptor_status.php` (+ bak `.bak_pre_cat28_20260905`) — modo cat28 ADITIVO, modo ids intacto
