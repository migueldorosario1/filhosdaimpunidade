# Memória técnica — DS YouTube (robô + batismo) — 31/08/2026 · ZCode/GLM-5.3

## Caminhos
- Cérebro: Tencent `~/ds_youtube/ds_youtube.py` (+artifacts/<vid>/, estado.json, logs/) · cron `7,22,37,52` `# DSN_YOUTUBE_15MIN_20260831`
- Porta: Dell `~/ds_youtube_fetcher/fetcher_youtube.sh` · cron `*/5` `# DS_YOUTUBE_PORTA_DOWNLOAD_20260831`
- Fila/canal/relatórios: repo `cerebro/Foruns/youtube/` + `cerebro/Relatorios/ds_youtube/`
- Credencial: `WP_USER_CAFEZINHO_DSN1`/`WP_APP_PASSWORD_CAFEZINHO_DSN1` (usuário WP 5801 cafezinhodsn1, role **editor**) nos cofres Dell+Tencent c/ backups `.bak_pre_dsyoutube_20260831`

## Decisões e porquês
1. **Porta de download no Dell**: YouTube bloqueia TODOS os IPs de datacenter testados (Tencent + NYC; web/ios/tv/mweb/web_embedded) com "Sign in to confirm you're not a bot"; Dell residencial passa. Cérebro fica na Tencent (ordem). Limitação: fila anda com o Dell ligado.
2. **Flash via dsh headless** com `DEEPSEEK_API_KEY` exportada do valor `DEEPSEEK_CAFEZINHO_CANONICO` (`.env.unificado`) — sem isso: MISSING_CREDENTIAL. A `.dsh/deepseek_env` antiga não basta.
3. **Meta custom via REST = erro (500)** — vínculo vídeo↔post NÃO vai em meta; vive na fila/canal (regra da casa re-confirmada).
4. **Rascunho SEM zizi_job_id** → fora do fluxo autônomo do Publicador; YouTube matéria só sai com consenso CL citado (scan da ponte pega).
5. **Capa de YouTube**: thumbnail oficial do canal (i.ytimg.com/vi/ID/maxresdefault.jpg) com crédito "Divulgação/YouTube — canal X" como candidata; frame de vídeo é alternativa (fativas de VOD de live falham por keyframes — usar download completo + ffmpeg se precisar de frame).
6. json3 → transcrição: eventos com tStartMs → `[HH:MM:SS] texto` + dedup de rolagem das auto-subs (regex de linha repetida).
7. Whisper local (faster_whisper no python3 da Tencent) é o caminho para vídeos SEM legenda (porta baixa áudio formato 139/249).
8. Conta WP DS: role editor; **nunca usar slug de role em português** no wp-cli ("autor" zera os roles — use "editor"/"author").

## Provas do batismo
- Transcrição 13.291 palavras; matéria 12,8KB com timestamps; rascunho WP 268440 (HTTP 201) + capa mídia 268439 (thumbnail, crédito); canal + fila + relatório commitados e empurrados; pedido de GATE à CL no canal.

## Estado
Robô no ar (3 crons DS na Tencent: Publicador 15/15, Ideias 13/43, YouTube :07/:22/:37/:52 + porta Dell */5). Falta: 1º ciclo 100% autônomo ponta a ponta com item novo; Chefe alimentar fila pelo Telegram (patch no prompt da ronda).
