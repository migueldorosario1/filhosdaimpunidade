# MEMÓRIA TÉCNICA — GSN embed duplicado (09/09/2026)

Par do fórum: `Foruns/forum_gsn_embed_duplicado_20260909.md`.

## Mapa do fluxo de briefs de vídeo do GSN (p/ próximas sessões)

- Pipeline YouTube V2 no NYC: `/root/agents_labs/youtube_v2/` — materializador →
  auditor (incorpora o embed no html) → publicador (`montar_payload`) que grava em
  `/root/agent_data/gsn_fila/<video_id>.json` com AMBOS: `conteudo_html` (html c/
  embed já dentro) e `embed_youtube` (div montado de novo).
- Consumidor roda no DELL: `Projeto Cafezinho Agentes/agentes_cafezinho/consumidor_gsn_fila.py`,
  cron `30 12 * * *` (BRT), scp da fila NYC → brief-*.md + hero no repo Dell
  `Projeto Cafezinho Agentes/sites-v4/globalsouth` → commit --author "GSN Agent
  <gsn@cafezinho.local>" + push → Vercel. Kill switch: `agent_data/gsn_consumidor_PAUSAR`.
  Logs: `agent_data/gsn_consumidor.log` e `gsn_consumidor_cron.log`.
- O clone V4 do NYC (`/root/tematicos/sites-v4/globalsouth`) FICA ATRASADO (não dá
  pull); o que publica é o clone do Dell. Não confundir ao investigar.
- Marcador no banco NYC: `marcar_nyc()` via ssh (auditados/publicaveis/videos =
  'publicado') e JSONs movidos p/ `/root/agent_data/gsn_fila_publicadas/`.
- Trava dedup do consumidor: grep `watch?v=<vid>"` no blog antes de processar.

## O bug e a cura

- Bug: consumidor escrevia `fm + d["embed_youtube"] + "\n\n" + corpo` com corpo já
  contendo o embed → 2 players. 21 briefs afetados (24/08→08/09).
- Cura gerador: `prefixo = "" if f"embed/{vid}" in corpo else embed + "\n\n"`;
  sanidade `ok` usa `prefixo + corpo`.
- Cura acervo: script de varredura (regex do div de embed, remove ocorrências
  repetidas do MESMO div, preserva embeds diferentes) → 21 arquivos, commit `c7e3195`.
- Prova ao vivo: `grep -c '<iframe'` = 1 nos posts 202609071530/202609081530/202608251530.

## Armadilhas

- JSON-LD com 2 VideoObject é POR DESIGN (solto + aninhado em BroadcastEvent,
  BlogPost.astro 33-59) — não "corrigir".
- Contar `youtube.com/embed` na página viva pega o JSON-LD junto; contar `<iframe`
  é o teste certo do player visível.
- Títulos EN em title case no GSN são convenção de manchete em inglês — NÃO aplicar
  o sentence case pt-BR lá (o `_sentence_case_ptbr` do produtor V4 só age em sites
  pt-BR; o GSN nem passa por esse produtor).
