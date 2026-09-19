# MEMÓRIA TÉCNICA — V4.1 Player (robô do carrossel na nuvem)

Data: 03/09/2026 · Autor: ZCode/GLM-5.3 (Dell) · Fórum: Foruns/forum_v41_player_robo_carrossel_20260903.md

## Arquivos
- Tencent (ubuntu): `~/v41_player/v41_player.py` (v1.1), `MEMORIA_VIVA.md`, `fontes/`, `cortes/`, `log/`, `estado/processadas.json`. Crontab: linha `V41_PLAYER_20260903` (varredura :41/h; backup /tmp/cron_bak.txt). Modelo whisper: "small" int8 CPU (~60s para 90s de áudio).
- Espelho NYC: mu-plugin v0.4.1 (carrossel+CSS single); posts do player: cat 28 draft, metas `_cafezinho_recorte_mp4`, `_cafezinho_player_v41`, `_cafezinho_reels_teste` (modo teste). Provas E2E: 400348/400350 (reescritos à mão pós-QA; os _c1/_c2.mp4 nos uploads 2026/09).
- Túnel: tencent→nyc aceito no known_hosts (StrictHostKeyChecking=accept-new) — BatchMode funciona.

## Comandos
- Manual: `python3 v41_player.py --fonte <arquivo|url> --cortes 6 --duracao 30 --publicar --teste --origem "..." --contexto "Ciro Gomes: candidato ao governo do CE; ..."`.
- Varredura: `--varredura` (processa todo MP4 novo em fontes/; marca em processadas.json).
- Rollback: remover linha do crontab; limpar posts: `wp post list --meta_key=_cafezinho_player_v41 ...`.

## Receitas e armadilhas
- yt-dlp na Tencent NÃO lista YouTube (IP datacenter, saída vazia) — fonte vem por arquivo (fetcher residencial da Dell baixa e scp para fontes/).
- Verticalização reels: vf `split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=18[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2`.
- wp-cli com acentos: conteúdo via ARQUIVO (`wp post create /tmp/x.html`) e título/excerpt com aspas simples no shell; `--porcelain` devolve o ID.
- DeepSeek chat JSON: `response_format json_object` ok via api.deepseek.com; GLM reserva com GLM_BASE_URL/GLM_API_KEY do .env.unificado (nunca expor valores).
- QA LLM redator: INVERSÃO de sentido temporal é o erro nº 1 (proibir no prompt); citações de trecho ruidoso é o nº 2 (paráfrase sem aspas); erros óbvios de whisper ("carriata") normalizar.
- A rede da Dell pode ficar instável (timeout para a DO) — o jump `ssh -J tencent root@159.65.177.60` é o plano B que sempre funciona.
