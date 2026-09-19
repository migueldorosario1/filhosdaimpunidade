# 11 — Estado da madrugada 23/07 (checkpoint para retomar)

## Entregue nesta madrugada
1. **Roteiro final do anúncio Moka** (voz do Miguel, sem metalinguagem) — em `Foruns/` e na conversa.
2. **Vídeo bruto transcrito** (Gemini, 66 timecodes) — `moka/marketing/legendas/transcricao_com_timecodes.txt`.
3. **Vídeo legendado completo** (5min41, amarelo bold): `Antigravity Google/moka/marketing/videos/moka_anuncio_completo_legendado.mp4`.
4. **Corte 55s para TikTok/Reels**: `moka/marketing/videos/moka_anuncio_60s_tiktok.mp4` (intro→dor→app→mágica→R$5→fecho).
5. **Diretório Moka movido para a raiz** `Antigravity Google/moka/` (Cafezinho fica SÓ com agentes — regra do Miguel). `pontos_api/` junto; app.py testado no novo caminho.
6. Transkriptor: busca por arquivo do Miguel ensinou que `/files` retorna `file_name` no campo — o vídeo era `20260722_233828.mkv`.

## ⚠️ PENDENTE — bugs do Moka Video (mokareader.com)
Código: `Outros/Aplicativos/MokaVideo/` (Next.js). **Nenhuma alteração feita ainda.**
1. **Aba Política não rola a página** — investigar: `.panel` tem min-height 220px e `padding 80px` no `.video-page`; suspeita de `overflow` na `.panel`/`body` quando o conteúdo da análise é longo. Começar por `src/app/globals.css` (regras `.panel`, `.video-page`, `.moka-shell`) e `src/app/video/[id]/page.tsx` (seção `.panel`).
2. **Ícones duplicados leitura/vídeo inconsistentes** — o toggle (📖/🎬) aparece nas páginas do MokaVideo mas falta em partes do MokaReader (`Outros/Aplicativos/Moka/`). Verificar o header compartilhado e padronizar.

## Retomar também
- ~15 heroes IA pendentes da varredura 22/07 (sites temáticos).
- Caption/hashtags por plataforma para o vídeo de 55s.
- Limpeza do tropeço "sem, sem, sem arriscar" na legenda (opcional).

## Atualização 23/07 — Features do Moka Video IMPLEMENTADAS (commit cf0737c no moka-video)
1. **Idioma livre das análises (PT/EN)**: `ai-client.ts` com `OutputLang` + `systemBase(lang)`, seletor 🌐 na página do vídeo, cache por idioma (`kind:lang` — PT e EN não colidem).
2. **Assistir legendado**: `components/SubtitledPlayer.tsx` — embed YouTube + legenda sincronizada por polling (iframe API), overlay amarelo no estilo do anúncio.
3. **Baixar legenda (.srt)**: botão no painel de transcrição (gera SRT client-side).
4. **Baixar com legenda**: API route `/api/download-legendado` (yt-dlp + ffmpeg no servidor; em serverless sem ffmpeg retorna 501 com orientação).
5. **SettingsModal**: footer com "❤️ Apoiar o projeto" (esq) + "✓ OK · Fechar" (dir).
6. Build `next build` passa. Push em `migueldorosario1/moka-video` main (cf0737c).

### ⚠️ DEPLOY PENDENTE
mokareader.com é Vercel, mas o projeto NÃO está na team `miguel-do-rosario-s-projects` (está em outra conta/team — provavelmente a do Cafezinho, gerenciada pela outra conversa). O push está no GitHub; o deploy depende do auto-deploy daquele projeto ou de disparo manual de quem gerencia. Se em 1h não subir, verificar com o fork/Claude (que administra essa Vercel).

## Atualização 23/07 (2) — Player de leitura TTS (commit 432189c)
`components/ReadAloud.tsx`: botão 🔊 (play/pausa/stop) no alto de TODOS os painéis — resumo, análises e transcrição. Usa SpeechSynthesis do navegador (sem custo de API), voz segue o idioma selecionado (pt-BR/en-US), divide o texto em frases para textos longos. Build passa.
