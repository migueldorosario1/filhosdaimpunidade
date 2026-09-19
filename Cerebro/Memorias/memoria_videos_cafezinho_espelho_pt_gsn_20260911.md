# 🧠 Memória — Vídeos de volta ao Cafezinho: espelho PT GSN→Cafezinho + alimentador religado (11/09/2026)

Companion do fórum `Foruns/forum_videos_cafezinho_espelho_pt_gsn_20260911.md`. Log técnico completo.

## Cadeia vertical YouTube (estado real encontrado em 11/09 ~01h BRT)

- **Banco de verdade:** `nyc:/root/agent_data/youtube_dialogos.sqlite` (NÃO o `agent_data/youtube_dialogos.sqlite` dentro de `agents_labs/youtube_v2/` — esse é vazio/legado, 1 vídeo de junho).
- **Pipeline EN (o "gasto diário"):** `nyc:/root/youtube_v2_pipeline.sh` (cron 0 11,17 UTC) = coletor → produtor (materializador clássico restaurado 03/09 + enxertos EMU/nomes) → auditor → publicador. Publicador roteia por idioma (ordem Miguel 17/08): EN → `gsn_fila` JSON; PT → WP Cafezinho draft.
- **Consumidor da gsn_fila:** Dell `agentes_cafezinho/consumidor_gsn_fila.py` → repo Astro globalsouth → Vercel. Posts de vídeo no ar até 10/09 (Dialogue Works, Glenn Diesen, Deep Dive...).
- **Status EN últimos 12 dias:** 2-4 "publicado en"/dia, 4-8 "falha_transcricao en"/dia ( Judging Freedom/Dialogue Works/kremlin etc.).
- **PT morreu 03/09:** materializador V4.1-espelho desativado (Miguel: "está horrível") + alimentador Tencent DESATIVADO (linha de cron 5,35) → fila DSN seca em 06/09 (último artefato 23:52) → último vídeo Cafezinho #269033 (06/09 16:50).
- **Jornal da Fórum:** ZERO posts desde 25/08. Causa: feed RSS da TV Fórum (UC3sMBA3BdnsKSVI0WB9yVWQ) 404 persistente (5/5 do Dell + 500/404 da Tencent, mesmo minuto; outros canais alternam OK — TRT respondeu na mesma rodada) + IPRoyal 402 (sem saldo, assinatura ~03/09 venceu) + yt-dlp lento/timeout ao IP do Dell de madrugada. Página do canal abre 200 (canonical = mesmo UC).

## Mudanças executadas

### NYC — espelho PT (novo arquivo, aditivo)
`/root/agents_labs/youtube_v2/agente_youtube_v2_espelho_pt.py`
- Lê `gsn_fila/*.json` frescos ≤48h (campo `criado_em_utc`; fallback mtime), ordena por idade, **teto 2/dia** (`ESPELHO_PT_TETO_DIA`), ledger `/root/agent_data/gsn_fila_espelho_pt/ledger.json` (idempotente).
- Tradução: extrai `<p>` do `conteudo_html` EN (descarta div de embed), sys-prompt TRADUÇÃO EDITORIAL FIEL (proibido inventar fato; título PT 1 frase sem Title Case; aspas só se original; sem clichê distópico EMU-11; sem repetição EMU-12), bloco de grafias canônicas do `personagens_youtube.json` (importa `_bloco_personagens_prompt` + `corrigir_nomes_personagens` + `_limpar_json` do materializador).
- Escada: openai gpt-5.6-sol **temperature=1.0** (400 com 0.3!) → alibaba qwen-plus 0.3 → fallback `gerar_texto`.
- Draft WP: cat 28, featured_media = `media_wp_id` do JSON, embed no topo, excerpt, meta `_video_id_youtube`, tag "Espelho GSN" (timeout 25s, fail-open).
- Cron: `40 12,18 * * *` com `source /root/chaves.sh`; log `/root/agent_data/espelho_pt.log`.
- Provas: drafts 269875/269876 (11/09 ~04:32 UTC) — cat Vídeos ✓, _thumbnail_id 269754/269751 ✓, embed ✓, tag espelho-gsn aplicada via wp-cli (rest da tag deu timeout na 1ª vez).

### Tencent — alimentador religado
- Crontab: linha `5,35 * * * * ... alimentador_fila.py` reativada (comentário datado RELIGADO_20260911).
- `canais_youtube.txt`: Judging Freedom + Dialogue Works comentados (evita transcrição duplicada — coletor NYC cobre); ficam Record News, Al Jazeera, DW, BBC, CNN, TRT.
- Backups: `alimentador_fila.py.bak_pre_religa_20260911`, `canais_youtube.txt.bak_pre_religa_20260911`.
- Prova: rodada manual 01:37 BRT → ADICIONADO Vb5Qi7sFxCg (TRT World, Houthis/Mocha) → fluxo retoma no decupador :07/:22/:37/:52 → ingestor NYC :55 → pipeline 11/17 UTC.
- Armadilha: reinstalar crontab com linha de comentário SEM `#` → "bad minute" e o crontab inteiro NÃO instala (vixie valida linha a linha).

### Dell — fallback 3 de feed no agente nacional
- `agentes_cafezinho/youtube_cafezinho.py` (+`.bak_pre_scrape_feed_20260911`): classe `_EntryScrape` (compat feedparser: yt_videoid/title/published_parsed/summary) + `_feed_scrape_canal()` = **yt-dlp --flat-playlist -J /videos, timeout 90s, 6 itens**; degrau 3 inserido entre proxy e desistência; log `[FEED:...] RECUPERADO_VIA_SCRAPE_VIDEOS`.
- Flat não traz published → published=agora; filtros existentes seguram (padrao_titulo + data do dia do --jornal, janela duração, juiz LLM, _ja_visto, _estreia_futura).
- Testes: yt-dlp flat listou o canal 1× (FLÁVIO BOLSONARO... 1518s) mas nas tentativas seguintes voltou 0/timeout (YouTube hostil ao IP do Dell de madrugada) — fail-soft, rodada seguinte tenta de novo. Scraping regex de ytInitialData DESCARTADO (UI nova: 0× videoRenderer; shell + JS).

## Pendências / decisões
1. CL parada desde 09/09 17:12 → religar (ninguém publica os rascunhos).
2. IPRoyal 402 → renovar (pagamento do Miguel) = degrau 2 do feed + caminho yt-dlp anti-bloqueio.
3. Conferir corridas 12:40/18:40 UTC de 11/09 (espelho) e 1ª matéria Record News da cadeia religada.
4. Opcional: streamlar espelho p/ fila da CL com selo (decisão Miguel).

## Comandos úteis
- Rodar espelho agora: `ssh nyc 'source /root/chaves.sh; cd /root/agents_labs/youtube_v2 && PYTHONPATH=/root:/root/agents_labs/youtube_v2 /root/venv/bin/python3 agente_youtube_v2_espelho_pt.py --apply'`
- Log: `ssh nyc 'tail -20 /root/agent_data/espelho_pt.log'`
- Fila DSN: `ssh tencent 'tail -5 ~/ds_youtube/alimentador.log'`

— ZCode/GLM-5.3 · 11/09/2026 ~02h BRT
