# FÓRUM — GSN: vídeo incorporado duplicado nos posts (09/09/2026)

> Report do Miguel (09/09 ~05:5x): "Global South News está com um bug. Os vídeos
> incorporados estão vindo duplicados dentro dos posts" + URL do brief
> 202609071530 (Era Of Proportional Response Is Over).
> Sessão: ZCode/Qwen 3.8 (Dell).

## 1. Diagnóstico (cadeia fechada)

1. Página viva com 2 iframes idênticos (`youtube.com/embed/bobO9Iv3U8A`).
2. A duplicação está NA FONTE md (origin/main do `globalsouth-v4`): o corpo começa
   com o div do embed e, duas linhas acima, o consumidor tinha prefixado o MESMO div.
3. Causa: o payload da fila `/root/agent_data/gsn_fila` (NYC, publicador
   `agente_youtube_v2_publicador.py`) traz DOIS campos com o player:
   `conteudo_html` (html do material, que "já vem com embed incorporado do auditor")
   e `embed_youtube` (embed montado de novo na linha ~156).
4. O consumidor (`Projeto Cafezinho Agentes/agentes_cafezinho/consumidor_gsn_fila.py`,
   cron Dell `30 12 * * *`, commita como "GSN Agent <gsn@cafezinho.local>") escrevia
   `fm + d["embed_youtube"] + "\n\n" + corpo` → player duas vezes.
5. Alcance: TODOS os 21 briefs publicados pelo consumidor desde 24/08.

## 2. Correções

1. Gerador (consumidor, linha ~189): só prefixa `embed_youtube` se `embed/{vid}` NÃO
   estiver no corpo; checagem de sanidade passa a usar `prefixo + corpo`.
2. Varredura no repo Dell `sites-v4/globalsouth`: dedup de divs de embed idênticos
   (mantém o 1º, remove repetidos; embeds DIFERENTES no mesmo post são legítimos e
   não são tocados) → 21 arquivos corrigidos, commit `c7e3195`, push → Vercel.
3. Verificação ao vivo: posts 202609071530, 202609081530 e 202608251530 com 1 iframe
   cada; corpo intacto.

## 3. Não-bug verificado (não mexer)

O JSON-LD da página tem 2 `"@type":"VideoObject"` POR DESIGN: um solto + um aninhado
no `BroadcastEvent` (BlogPost.astro linhas 33-59). É structured data válida; não é a
duplicação visível.

## 4. Estado

- PRONTO: gerador curado + 21 posts deduplicados no ar + provas ao vivo.
- FALTA: nada. (Se um dia um post precisar de 2 vídeos DIFERENTES, o dedup do
  consumidor não interfere — ele só evita prefixar o que já está no corpo.)
- PRECISO DE VOCÊ (MIGUEL): nada bloqueante.
