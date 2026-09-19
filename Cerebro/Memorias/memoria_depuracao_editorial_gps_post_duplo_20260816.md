# Memória técnica — Depuração editorial + canal GPS + post duplo Irã

**Data:** 16/08/2026 · **Autor:** ZCode/Qwen 3.8 · **Fórum pareado:** `Foruns/forum_depuracao_editorial_gps_post_duplo_20260816.md`

## Log técnico

### 1. Diretriz de depuração no agente
- `youtube_cafezinho.py`: função nova `_nota_depuracao_editorial(video)` (string
  permanente, sem flag de canal — vale para TODOS os vídeos) injetada no fim do
  prompt de `analisar()` e no `sistema` de `redigir()`. Texto: ignorar por completo
  trechos críticos ao Irã/China/Sul Global (não citar/mencionar/refutar); reforçar
  na tese/manchete/corpo só partes favoráveis e anti-imperialistas.
- `curadoria_cafezinho_youtube.json` → `escopo_ampliado.regra` += parágrafo
  DEPURAÇÃO EDITORIAL (curador não descarta candidato por conter críticas; exemplo
  citado: Fareed Zakaria GPS).
- Backups: `youtube_cafezinho.py.bak_pre_depuracao_20260816`,
  `curadoria_cafezinho_youtube.json.bak_pre_depuracao_20260816`.

### 2. Canal GPS (Fareed Zakaria GPS / CNN)
- Resolução: Brave → dois candidatos; página oficial via proxy (urllib + UA):
  handle @fareedzakariagps → **UCs_6LFfjAH7Yv2QrQ0ddb6g**;
  /channel/UCm8Tj3OHh4RUOW2z5wD3cHA → RSS **404** (descartado — lição: ID vindo
  de resultado de busca pode ser canal morto; RSS 200 é a prova final, igual à
  lição da missão do painel).
- RSS do ID oficial: 200 + título "FareedZakariaGPS" (0 entries no momento — ritmo
  do canal; coletor pega quando sair vídeo).
- Entrada em `canais_cafezinho_youtube.json` (33 canais): peso 1.0, idioma en,
  origem `miguel_20260816_gps`, categoria_ids [5003, 28] (Geopolítica+Vídeos),
  `nota` com o regime de depuração. Backup `.bak_pre_gps_20260816`.
- Vivo do painel: `sync_youtube_painel.py` rodado manualmente → vivo cafezinho na
  Tencent com 33 canais e GPS presente (23:27).
- Memória de personagens: +Fareed Zakaria (87 nomes).

### 3. Post duplo do vídeo dFPy6YltmkU (Dialogue Works / Nima R. Alkhorshid)
- Transcrição do cache (`autonomo_en_dFPy6YltmkU.json`, 30.880 chars, en).
- Pipeline: `analisar()` (deepseek; tese depurada: ameaça nuclear de Trump =
  desespero imperialista, determinação do Irã) → `verifica_nomes` (Nima
  R. Alkhorshid confirmado de memória; Marjorie Taylor Greene confirmada via
  websearch e gravada na memória) → `redigir()` pt-BR (superluxo/openai_gpt55).
- **PT: DRAFT 266172** (~1.160 palavras; cats [5003,28] via categoria_ids do vídeo;
  meta cafezinho_nomes_check 1113 chars).
- **EN: DRAFT 266153 reescrito** via `atualizar_draft` (script avulso com sistema
  EN estilo Global South News + mesma depuração + `_bloco_factcheck`; ~930 palavras;
  meta 872 chars). Artefatos: `agent_data/v4_cafezinho_youtube/duplo_en_dFPy6YltmkU.json`.
- Verificação REST (context=edit): ambos status=draft, meta presente, scan de
  frases críticas ao Irã/China limpo.
- Gotcha do script: walrus dentro de f-string (3.10) quebra — computar antes.
- Gotcha de extração: `extrair_nomes` deixou passar "sua administração" /
  "a administração dos EUA" (entram como duvidoso na memória; sem dano — redação
  omite). Candidato a refinamento: descartar frases começando por artigo/possessivo.

### 4. Observações operacionais
- Durante a geração, o cron 22:30/23:00 do Jornal da Fórum seguia esbarrando em
  `bot_check` do iProyal na coleta (ver bugs_encontrados/yt_patrulha...). A rede
  das 23:30 já usa a cascata DeepSeek→Kimi.
- Revisão/publish dos dois drafts é do Loop Miguel (Claude) — avisado na inbox.
