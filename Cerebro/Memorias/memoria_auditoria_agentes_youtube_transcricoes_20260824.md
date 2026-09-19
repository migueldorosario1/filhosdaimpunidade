# 🧠 MEMÓRIA — Auditoria agentes YouTube × transcrições (24/08/2026, ZCode GLM-5.3)

Complemento técnico do `Foruns/forum_auditoria_agentes_youtube_transcricoes_20260824.md`. Tudo em modo leitura (SQL/bancos/logs); nenhuma alteração em produção.

## Fontes consultadas (provas)

1. `agent_data/youtube_transcript_stats.jsonl` (Dell) — 234 eventos 21/07→24/08: transkriptor_url_direto 73 (US$ 28,34) · rejeitado_qualidade 71 (US$ 26,68) · transkriptor_falhou 68 (US$ 0) · cache_hit 12 (US$ 0) · transcricao_parcial 8 (US$ 2,88) · via_s3 2 (US$ 0,36). Total US$ 58,26.
2. `agent_data/v4_cafezinho_youtube/` — BANCO_DIR do agente: 4 transc_*.json em cache, historico.jsonl com 56 vídeos, pendentes_youtube.json VAZIO (recuperações concluídas), sem flag PAUSAR_TRANSCRICAO (transcrição liberada), cron.log com draft de hoje 267438 (vídeo gz6jEJMqcrs, redação deepseek).
3. WP canônico (ssh cafezinho-wp → /var/www/ocafezinho, wp db query --allow-root): `post_content LIKE '%youtube.com/embed%'` desde 21/07 → **53 publicados**; drafts/pending com embed → ~22 IDs, sendo ~12 entre 17-24/08 (267438, 267352, 267283, 266426, 266356, 266344, 266290, 266282, 266281, 265793, 265665, 265579, 265470…) + legados abr-jun.
4. `agentes_tematicos/v4/youtube.py` (287 linhas): máx 1 vídeo/rodada e 1/dia/site; transcrição via util compartilhado (cache `agent_data/youtube_transcript_cache`, 291 arquivos); falha de transcrição NÃO é fatal (post cai p/ título+descrição); anti-repost `youtube_vistos.json` (últimos 2000).
5. `agent_data/configs/*.json`: youtube.enabled=True em aiatolah(3 canais), ceara(4), globalsouth(7), mapario(4); False em discoverbrazil, mundotrilhos, railpost, riocarta.
6. Bancos auditados `agent_data/v4/<site>/auditado.jsonl` (origem_coleta=youtube): 12/4/2/4/26/1/1/1 = 51 produzidos, TODOS status=aprovado (publicador não marca "publicado" no banco — o status fica desatualizado; verdade de publicação = repo).
7. Repos `Projeto Cafezinho Agentes/sites-v4/<site>` (posts .md c/ embed): aiatolah 9 (EN; aiatolah PT 0) · ceara 4 · globalsouth 20 (18 brief-* do GSN V2 + 2 do agente) · mapario 27. Últimos: mapario 20/08, ceara 18/08, globalsouth brief 20/08.
8. NYC (ssh nyc): crontab `0 11,17 * * * /root/youtube_v2_pipeline.sh` (REATIVADO_20260823_ZM); `/root/agent_data/youtube_dialogos.sqlite` — videos: 56 publicado / 43 falha_transcricao / 27 texto_vencido / 18 falha_livestream / 1 novo; dialogos: 76 url_direto (US$ 145,58) + 6 via_s3 (US$ 2,58) = US$ 148,16 (custo médio US$ 1,81 — vídeos internacionais longos, diarização); publicaveis: 18 publicado / 30 draft / 34 descartado_vencido / 1 pronto; 18 diálogos sem produzido. `gsn_fila`: 9 JSONs (2 de 24/08 11:10: X3-ohm8fc7s, XLRpWFcFAaY; antigos de 18/08).
9. Log pipeline NYC 24/08 11:00: BRS8DkhtQ_c e 1CGQFX2L0oQ falharam (Transkriptor Failed + yt-dlp **"No supported JavaScript runtime could be found. Only deno is enabled by default"** → fallback morto). XLRpWFcFAaY processou (90s+ polling).
10. Gate de qualidade: `agents_labs/youtube_v2/util_youtube_transcript.py:165-185` — chars/min < 100 → `rejeitado_qualidade` com `custo_est` registrado (PAGO) e retorno vazio, sem gravar cache.
11. Crontab Dell (67 linhas ativas): YouTube Cafezinho 0 8,14,20 --rodada + 22:30/23:00 --jornal + 14:30 --forum11 (pyenv 3.10.13). Crons GSN locais TODOS comentados (migrados p/ NYC).
12. Duplicata provada: X3-ohm8fc7s (Dialogue Works) — Dell: transcrito 23/08 14:06 BRT p/ Cafezinho (histórico 267… post "Irã arma resposta ao D-Day"); NYC: gsn_fila 24/08 11:10 (transcrito de novo p/ GSN). Caches isolados por design (Dell json × NYC sqlite).

## Cálculo-chave do aproveitamento

- Dell total: US$ 58,26 → desperdício puro US$ 26,68 (rejeitados, 46%) + US$ 2,88 parcial; retorno: 53 posts Cafezinho (US$ ~0,55/post só de transcrição — barato) + 42 temáticos (compartilharam o mesmo pool).
- NYC GSN: US$ 148,16 → 18 publicados = **US$ 8,23/post**; perdidos por vencimento 34 publicáveis (~US$ 61 por sobreduração); 30 drafts parados; fila CM 9.
- KPI sugerido: US$ de transcrição / matéria publicada, por pipeline, no painel /v6/custos (telemetria §118).

## Riscos/limitações da leitura

- Status "aprovado" nos auditados não reflete publicação (verdade = repo/ar); gap aiatolah 12×9 pode conter 3 nunca publicados (checar uid no repo se for recuperar).
- Rascunhos WP legados (abr-jun) não são do pipeline V4 atual — não contar como desperdício novo.
- `falha_transcricao` 43 no NYC não gerou custo (Transkriptor falha antes de cobrar), mas desperdiça janela de frescor do vídeo (perde pauta).

## Próximos passos propostos (aguardam "vai" do Miguel)

1. Consumir gsn_fila (9) antes de vencerem — CM ou ZCode com autorização.
2. Fix yt-dlp NYC (instalar deno OU node + `--js-runtimes node`) e reverter as 43 falhas.
3. Pré-filtro duração no Dell (yt-dlp real vs estimativa 3600s) antes de pagar Transkriptor.
4. Cache compartilhado de transcrição Dell↔NYC por video_id (dupla pagamento morto).
5. TTL/vencimento GSN: alongar ou reduzir coleta (breaker "quem não publica não transcreve" no pipeline NYC).
6. Encaixe no R4 (migrar YouTube do Dell p/ servidor — produção-zero-no-Dell).

## Adendo EXECUÇÃO (24/08 11:25→13:32) — detalhes técnicos

- Configs temáticos: `agent_data/configs/{aiatolah,ceara,globalsouth,mapario}.json` → `youtube.enabled=false` + nota `_desligado`; backups `.bak_pre_youtube_off_20260824`. Crons Dell de temáticos YouTube: já não existiam (operação era da Laura).
- Publicação GSN: script `/tmp/gsn_publicar_fila_20260824.py` (tradução parágrafo-a-parágrafo via `nucleo_llm.gerar_json(cadeia=["glm","qwen"])` — SEM a cadeia explícita cada chamada leva ~14 min atravessando deepseek/kimi mortos; com cadeia ~30-60s). GOTCHA: 2 processos paralelos geraram briefs duplicados → dedup por video_id (heroImage no frontmatter como chave). Lição: `kill <pid do wrapper bash>` não mata o python filho — usar `pkill -f script.py`.
- Briefs: 9 arquivos `brief-20260824*.md` + heroes `public/hero/youtube-*.jpg`; frontmatter idêntico ao padrão GSN (lang en, author Global South News Desk, pubDate = data do VÍDEO, tags [canal, entrevistado]). Sanidade 9/9: embed ✓ hero ✓ corpo 3.4–6.2k chars ✓ EN>PT ✓.
- Git: push inicial rejeitado (loop tinha commitado `846080e` em paralelo — Larry Johnson qNqRj0RpVWY) → `pull --rebase` → push `2e90f5a`. Domínio: globalsouth.news (307 apex→www é normal; 200 no www).
- Banco NYC (base64 p/ evitar quoting ssh): updates em auditados/publicaveis/videos p/ os 10 vídeos; fila → `/root/agent_data/gsn_fila_publicadas/`.
- Materializador NYC: `agente_youtube_v2_materializador.py` — sys_prompt e instrução 1 parametrizados por `dialogo.idioma` (en→EN/Global South News); instrução 6 reforça idioma no HTML.
- Pré-filtro Dell: no `util_youtube_transcript.py`, logo antes de `custo_est` — `TRANSKRIPTOR_MIN_DURACAO_S` (default 300; 0=off), método stats `pre_filtro_curto` custo 0. Prova: jNQXAC9IVRw (19s) bloqueado sem custo. Import do util exige os paths do cafezinho (youtube_v2_config não está na pasta do Dell — vem de outro path do sys.path do agente).
- Consumidor: `Projeto Cafezinho Agentes/agentes_cafezinho/consumidor_gsn_fila.py`; crontab Dell `30 12 * * *` (pyenv 3.10.13); logs `agent_data/gsn_consumidor.log` + `gsn_consumidor_cron.log`; fail-soft (nunca apaga sem publicar; push falhou = banco não marcado); detecta PT e traduz (fallback).
- Deno NYC: binário direto do GitHub (`deno-x86_64-unknown-linux-gnu.zip`) → `/usr/local/bin/deno` 2.9.5 (install.sh falhou silenciosamente). Anti-bot YouTube persiste p/ IP do NYC; NO_PROXY do chaves.sh mantém youtube fora do proxy (IPRoyal 402).
