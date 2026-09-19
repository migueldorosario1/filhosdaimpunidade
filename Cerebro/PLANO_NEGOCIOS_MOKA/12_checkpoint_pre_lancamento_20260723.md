# 12 — CHECKPOINT PRÉ-LANÇAMENTO (23/07) — LEIA PRIMEIRO NA CONVERSA NOVA

> **🚀 O MOKA LANÇA NESTE FIM DE SEMANA (25–26/07/2026).** Tudo abaixo está pronto ou pendente para o lançamento.

## 1. Entregue e pronto para o lançamento

### Vídeo de marketing (pronto para postar)
Local: `Antigravity Google/moka/marketing/videos/`
- **`moka_anuncio_corte_silencios_bbc.mp4`** — VERSÃO PRINCIPAL: 4min07, sem silêncios, legenda BBC (branco negrito/caixa preta), sem marca d'água
- `moka_anuncio_60s_tiktok.mp4` — corte 55s (Reels/TikTok/Stories)
- `moka_anuncio_completo_legendado.mp4` — completo 5min41 (amarelo, YouTube/FB)
- SRTs em `moka/marketing/legendas/`
- Roteiro da fala: transcript polido na conversa + `transcricao_com_timecodes.txt`

### Features do Moka Video (código — mokareader.com)
Repo: `migueldorosario1/moka-video` (branch main). 3 commits prontos:
1. `cf0737c` — **idioma livre PT/EN** (seletor 🌐, cache por idioma), **assistir legendado** (player YouTube+legenda sincronizada), **baixar legenda .srt**, **baixar com legenda** (API yt-dlp+ffmpeg), footer do modal (❤️ apoiar + ✓ OK·Fechar)
2. `432189c` — **player de leitura TTS** em todos os painéis
3. `4f42e5b` — **voz neural × sintética** (OpenAI TTS via chave BYOK do usuário × voz grátis do navegador)

Build `next build` passa em todos. 

### Moka pontos (backend)
- Schema validado: `Foruns/moka_pontos_schema_v1.sql`
- API FastAPI 4/4 validada: `Antigravity Google/moka/pontos_api/app.py`

## 2. ⚠️ PENDÊNCIAS CRÍTICAS para o lançamento (ordem)

1. ~~DEPLOY do moka-video~~ ✅ **RESOLVIDO 23/07**: o projeto `moka-video` ESTÁ na team miguel-do-rosario-s-projects (`.vercel/project.json`), auto-deploy via push funcionou — cf0737c (02:14), 432189c (02:26), 4f42e5b (02:40) todos READY. Features confirmadas no chunk JS da página (app é client-rendered — grep no HTML cru não mostra; validar no navegador).
2. **Checkout R$5**: landing `/experimente` + Mercado Pago (Checkout Bricks Pix) + webhook → 100 pontos (doc 09 do plano).
3. **Painel de pontos do usuário** (HTML consumindo `/painel/saldo`).
4. **Gerador de convites** (lote de códigos MOKA-XXXXX para os primeiros usuários).

## 3. Pendências secundárias (pós-lançamento)
- ~15 heroes IA da varredura 22/07 (sites temáticos)
- Captions/hashtags do vídeo por plataforma
- Corte 60s a partir do bruto sem silêncios (mais fluido)
- Parecer jurídico CVM antes de vender títulos de capital

## 4. Estado do ecossistema (23/07)
- 7 portais ativos com GA4, cron 4×/dia, juiz visual, blur-fill
- YouTube Cafezinho: cron 6h/12h/18h/23h → drafts p/ Claude publicar
- Canais: e-mail via SSH Tencent, 2 bots Telegram (@cafezinhoantigravitybot, @zizilindav2bot; chat 1894890759)
- Diretórios: `Cerebro/PLANO_NEGOCIOS_MOKA/`, `Cerebro/ARQUITETURA_MOKA/`, `Antigravity Google/moka/`
EOF
## Atualização 23/07 (3) — Pendências críticas RESOLVIDAS
1. ✅ **Gerador de convites**: `moka/pontos_api/gerar_convites.py` (lotes MOKA-XXXXX, testado integrado com a API)
2. ✅ **Painel do usuário**: `moka/pontos_api/painel.html` (login email+senha → saldo, histórico, totais; pronto p/ servir junto da API)
3. ✅ **Landing /experimente**: `moka/marketing/experimente.html` (oferta R$5, resgate de convite FUNCIONANDO hoje contra a API, checkout Pix com ponto de encaixe pronto)
4. ⏳ **Falta só**: credenciais Mercado Pago (Miguel fornece) → ativar o botão R$5; deploy moka-video (outra conta Vercel).

Fluxo validado ponta a ponta: gerar código → resgatar na landing → painel com 200 pts.

## Atualização 23/07 (4) — Vídeos do anúncio no R2
- `.../moka/anuncio/moka_anuncio_bbc.mp4` (principal) e `.../moka_anuncio_60s.mp4` (corte) — URLs públicas verificadas (HTTP 200). Registradas no mapa de arquivos da arquitetura.

## Atualização 23/07 (5) — PASSAGEM DE BASTÃO para conversa nova
Conversa-mãe (20–23/07) encerrada com contexto quase cheio. Tudo persistido:
- Cérebro: PLANO_NEGOCIOS_MOKA/ (docs 01–12) + ARQUITETURA_MOKA/ (01–07)
- Drive: gdrive:Cerebro_Backups/ (tudo sincronizado)
- GitHub: 8 sites *-v4 + moka-video (4 commits: cf0737c, 432189c, 4f42e5b, deploys READY)
- R2: vídeos do anúncio com URL pública
- Pendências na conversa nova (ordem): 1) credencial Mercado Pago → ativar checkout R$5; 2) abrir no navegador e validar as features do moka-video; 3) lançamento no fim de semana 25–26/07.
ABERTURA SUGERIDA para a conversa nova: "lê Cerebro/PLANO_NEGOCIOS_MOKA/README.md + 12_checkpoint_pre_lancamento_20260723.md + Cerebro/ARQUITETURA_MOKA/README.md e segue do backlog".

## Atualização 23/07 (6) — Checkout R$5 IMPLEMENTADO (conversa nova, ZCode/Kimi)
- Código completo: `moka/pontos_api/app.py` (checkout Pix via API MP `/v1/payments`, webhook HMAC, polling com reconciliação, páginas `/` e `/painel` servidas pela API) + landing `experimente.html` com fluxo Pix real (QR copia-e-cola → polling → sucesso c/ senha).
- Testado: 12/12 E2E com MP mockado. Detalhes: `Foruns/forum_moka_checkout_mercadopago_20260723.md` + `Cerebro/Memorias/memoria_moka_checkout_mercadopago_20260723.md`.
- **Falta SÓ o Miguel colar o `MP_ACCESS_TOKEN`** (placeholders no fim de `.env.unificado`) → checkout fica vivo. Depois: `MOKA_BASE_URL` + webhook cadastrado no painel MP.

## Atualização 23/07 (7) — Checkout ATIVO em sandbox
Token de TESTE do MP integrado; ensaio real: Pix sandbox emitido ponta a ponta (criar→QR→status→painel). Pendente p/ lançamento: credencial de PRODUÇÃO (ativar no painel MP: indústria+website+termos), `MOKA_BASE_URL` e webhook (`MP_WEBHOOK_SECRET`). Detalhes: memória `memoria_moka_checkout_mercadopago_20260723.md`.

## Atualização 23/07 (8) — Checkout EM PRODUÇÃO 💰
Token de produção `APP_USR-` integrado (backup do cofre feito). Smoke test: Pix real gerado + status consultado ao vivo no MP. Restam: URL pública da API (MOKA_BASE_URL), webhook no painel MP (MP_WEBHOOK_SECRET) e 1ª compra real paga. Detalhes: memória `memoria_moka_checkout_mercadopago_20260723.md`.
