# Achado técnico — CONTENT END: renderizado × REST público (18/08/2026 ~00:10)

- **Origem:** Claude Laura (CL-20260817-002), ronda 140 do Loop Laura.
- **Medição:** 8 posts publicados em 17/08 entre 20:15 e 23:15. Página renderizada: `CONTENT END` = 0. REST público (`content.rendered`): marcador `<!-- CONTENT END 1 -->` presente em 8 de 8.
- **Hipótese:** o tema esconde na renderização o que segue gravado no conteúdo (não é regressão de gravação até prova contrária).
- **Pendência:** leitura interna do banco (post_content dos 8 posts) pelo LAURA-CODEX (E1-RO) — pedido formal XL-002 na ponte. Sem confirmação interna, NÃO escalar como regressão.
- **Registrado por:** ZCode/DeepSeek (ZM-20260818-002). Sem ação no WP até a confirmação.

## FECHAMENTO 18/08/2026 01:19

Causa identificada: plugin **Ad Inserter** (`wp-content/plugins/ad-inserter/constants.php` é o único arquivo do WP com a string CONTENT END). O marcador é injetado pelo filtro de conteúdo do plugin (contexto REST entrega; o tema esconde na página). Comportamento corrente e inofensivo ao leitor. Não é regressão do worker V4. Decisão de supressão no REST = Miguel.
