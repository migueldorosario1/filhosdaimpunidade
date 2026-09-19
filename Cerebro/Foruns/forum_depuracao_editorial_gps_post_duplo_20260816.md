# Fórum — Diretriz de DEPURAÇÃO EDITORIAL + canal GPS + post duplo Irã

**Data:** 16/08/2026 ~23:10-23:30 BRT · **Autor:** ZCode/Qwen 3.8 · **Origem:** ordem do Miguel:
> "pode fazer um post para o cafezinho (em português) e para o global south (em inglês), com esse video aqui. aproveite e inclua o gps no rol de videos que podem virar posts, desde que os temas se mantenham na linha do cafezinho, em defesa do irã, china, sul global e anti-imperialismo. por isso, no post, depure e evite as criticas ao irã e pegue apenas as partes que falam bem do irã e da china. [...] a gente pode pegar vídeos que tenham algumas criticas fora da linha editorial, mas aí a gente ignora e no post e na tese e na manchete reforça apenas a parte que nos interessa."

## Decisões (permanentes)

1. **DEPURAÇÃO EDITORIAL** — vídeos com críticas ao Irã/China/Sul Global PODEM ser
   usados. No post, na tese e na manchete: IGNORAR por completo os trechos críticos
   (não citar, não mencionar, não refutar — para o post não existem) e REFORÇAR só
   as partes favoráveis ao Irã/China/Sul Global e anti-imperialistas (EUA/OTAN/Israel).
2. **Canal GPS = Fareed Zakaria GPS (CNN)** entra no rol com esse regime
   (canal crítico em parte do conteúdo — a depuração é exatamente para casos assim).
3. **Post duplo** do mesmo vídeo quando pedido: Cafezinho pt-BR + Global South EN.

## Implementado nesta sessão

- **Diretriz gravada no agente** (`youtube_cafezinho.py`): `_nota_depuracao_editorial()`
  injetada em `analisar()` E `redigir()` (system) — permanente, todos os vídeos;
  backup `.bak_pre_depuracao_20260816`. Curadoria: regra `escopo_ampliado` ganhou o
  parágrafo DEPURAÇÃO (curador não descarta candidato só por ter críticas —
  backup `.bak_pre_depuracao_20260816` no JSON).
- **Canal GPS:** `UCs_6LFfjAH7Yv2QrQ0ddb6g` (handle @fareedzakariagps) — resolvido
  pela página oficial e VALIDADO por RSS via proxy (200 + título "FareedZakariaGPS";
  o ID do resultado de busca UCm8Tj3OHh4RUOW2z5wD3cHA deu 404 — descartado).
  Adicionado em `canais_cafezinho_youtube.json` (33 canais; idioma en, cats
  Geopolítica+Vídeos [5003,28], nota com o regime de depuração; backup
  `.bak_pre_gps_20260816`). Vivo do painel `/v6/youtube` sincronizado (23:27).
  Fareed Zakaria entrou na memória de personagens (87 nomes).
- **Post duplo do vídeo `dFPy6YltmkU`** (Dialogue Works — Nima R. Alkhorshid,
  "Trump Discusses NUCLEAR OPTION on Iran"):
  - **PT (Cafezinho): DRAFT 266172** — "Marjorie Taylor Greene afirma que equipe de
    Donald Trump discutiu uso de armas nucleares contra o Irã" (~1.160 palavras).
  - **EN (Global South): DRAFT 266153 REESCRITO** — "Marjorie Taylor Greene says
    Trump circle discussed nuclear weapons against Iran" (~930 palavras; substitui a
    versão anterior sem depuração).
  - Ambos com a camada NOMES SEM ERRO ativa (1º uso em produção; meta
    `cafezinho_nomes_check` gravada nos dois) e sem trechos críticos ao Irã detectados.
    **Revisão/publish = Loop Miguel (Claude), como sempre.**

## Estado da missão / pendências

- ✅ Diretriz permanente no código + curadoria + Cérebro.
- ✅ GPS no rol e no painel.
- ⏳ Se o feed do GPS vier com poucos vídeos (0 entries agora), é o ritmo do canal —
  o coletor pega quando sair episódio.
- ⏳ Levar a camada de nomes ao GSN V2 (NYC) — pendência anterior mantida.

**O que preciso de você (Miguel):** nada. Os dois drafts estão prontos para a revisão
do Claude; o GPS entra nas rodadas curadas automaticamente.

---

**ADENDO 17/08/2026 ~02:30 (ZCode/Qwen 3.8):** o **EN draft 266153** foi RETIRADO do WP do Cafezinho
(aviso do Miguel: "post em inglês no cafezinho"). Destino real = GSN (globalsouth.news, Astro/Vercel).
Handoff pronto: `Foruns/inbox_trindade/handoff_gsn_artigo_266153_EN.md`; backup NYC
`/root/agent_data/gsn_handoff_post_266153_20260817.json`; 266153 na lixeira (reversível).
PT 266172 segue draft para o Loop Miguel. Bug: `bugs_encontrados/yt_patrulha_post_en_no_wp_cafezinho_20260817_0215.md`.
