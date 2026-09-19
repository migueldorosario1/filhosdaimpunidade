# Memória técnica — Regra IDIOMA PT INTEGRAL no agente YouTube

**Data:** 2026-08-17 ~16:00 BRT · **Agente:** ZCode (DeepSeek)
**Fórum:** `Foruns/forum_regra_idioma_pt_integral_agente_youtube_20260817.md`

## Ordem do Miguel (literal)

"o agente youtube tem trechos em ingles, corrige lá e nunca mais faça isso.
tudo tem que ser em portugues! os trechos são as aspas"

## O que foi feito

1. **Prompt de redação** (`youtube_cafezinho.py`, função de redação ~linha 544):
   nova regra IDIOMA — "TODO o texto — título, corpo E ASPAS DIRETAS — deve estar em
   PORTUGUÊS... NUNCA deixe trecho em inglês no post, nem entre aspas".
2. **Guarda `_tem_aspas_ingles(corpo_html)`**: heurística — citação (aspas simples/duplas,
   ≥25 chars, ≥6 palavras) com ≥2 stopwords EN (`_EN_STOPWORDS` frozenset) → True.
   Em `publicar_draft()` e `atualizar_draft()`: True ⇒ status `pending` + log (fail-close:
   inglês nunca passa ao publish automático). Smoke test: EN→True, PT→False, vazio→False.
3. **Correção no ar (266172):** 6 aspas EN traduzidas via REST (context=edit, content update,
   HTTP 200), verificado zero aspas EN por varredura PHP no servidor.
4. **Varredura completa:** WP_Query cat 28 + "Transkriptor" + regex de aspas EN em todos os
   status (publish/future/pending/draft) — único caso: 266172. Os demais (266072/266073/
   266195/266284...) estão limpos.
5. **Manual §9** novo com a regra e as 2 camadas.

## Gotchas

- A heurística ignora citações curtas (<25 chars) e com <6 palavras — aceitável: frases de
  impacto em inglês são longas; para rigor total, a revisão humana (pending) cobre o resto.
- O vídeo-fonte pode ser EN (canais GSN) — a regra é sobre o TEXTO publicado, não sobre a
  transcrição interna.
- GSN V2 (NYC) grava EN no WP do Cafezinho por bug de roteamento — atribuído ao Claude
  (`yt_patrulha_post_en_no_wp_cafezinho_20260817_0215.md`); é a última porta de EN no site.

## Arquivos

- `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py` (prompt + guarda; backup `.bak_pre_gate_imagem_20260817`)
- `Cerebro/Memorias/manual_agentes_youtube_operacao_20260816.md` (§9)
