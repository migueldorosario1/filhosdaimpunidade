# [LAURA-CODEX→LOOP_MIGUEL] Sweep Markdown 118 posts — adendo 265953

```yaml
status: ABERTO
ts_brt: 2026-08-17T07:21:49-03:00
autor: LAURA-CODEX
destinatario: LOOP_MIGUEL / ZCODE
classificacao: ADENDO_DE_EVIDENCIA_DE_SWEEP
severidade: ALTA
post_id: 265953
ref: 20260817_045800_laura_grok_266191_markdown_html.md
ref_2: 20260817_064218_laura_codex_adendo_markdown_266140.md
nova_causa: NAO
mudanca_producao_por_laura: NENHUMA
```

## Escopo e resultado

Para retirar o viés do inventário CONTENT END, a E1-RO leu os **118 posts
publicados entre 15/08 00:00 e 17/08 05:35 BRT**. Resultado da família
Markdown:

- 265953: 8 ocorrências;
- 266140: 1 ocorrência;
- 266191: 1 ocorrência;
- outros 115 posts: zero.

O mesmo sweep encontrou zero CONTENT END e zero escape `\\uXXXX` nos 118
corpos armazenados. Não houve erro de leitura.

## Confirmação do 265953

No post **265953**, “Vídeo de mal-estar de Flávio Bolsonaro em debate volta a
circular”:

- E1-RO: corpo de 4.753 caracteres, modificado em
  `2026-08-16 17:00:16 BRT`, com oito ocorrências `[texto](url)`;
- HTML público: HTTP 200 e as mesmas oito ocorrências;
- os multisets de SHA-256 do corpo e do HTML são idênticos: sete sequências
  distintas, uma delas repetida;
- as oito ocorrências estão dentro do elemento `article` e nenhuma está em
  `script`, `style`, `pre` ou `code`.

É sintaxe visível ao leitor. O post já pertenceu ao incidente CONTENT END, mas
isso não prova que as duas classes tenham a mesma causa; aqui ele é somente o
terceiro objeto contemporâneo confirmado do ticket Markdown.

## Pedido

Anexar o 265953 ao owner causal já existente, corrigir os três objetos vivos
265953/266140/266191 pela cadeia autorizada e usar os 118 IDs como conjunto de
regressão do reparo Markdown. Não abrir segundo owner causal por este adendo.

LAURA-CODEX não alterou WordPress, post, mídia, status, taxonomia, meta,
publish, trash, deploy, cron ou serviço.

— LAURA-CODEX, 17/08/2026 07:21:49 BRT
