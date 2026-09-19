# 📊 MANUAL DE GRÁFICOS DO PAINEL — v1 (16/09/2026, ordem do Miguel)

> "O Cérebro tem que ter uma questão de qualidade, manual de gráficos."
> Regras de desenho dos SVGs do painel CCTV V6 (e qualquer gráfico futuro da casa).
> Origem: aprendizados com o Miguel ao longo de 13-16/09/2026 (fórum da correlação posts×audiência).

## Regra 1 — O rótulo segue o lado da linha (§ordem 16/09 ~18h, a mais importante)

- Quando a linha está em cima, o rótulo fica em CIMA dela; quando a linha está embaixo, o rótulo fica em EMBAIXO.
- Em gráfico com DUAS linhas rotuladas: cada linha rotula para FORA do espaço entre elas — a que está mais alta naquele ponto rotula acima; a mais baixa rotula abaixo. Assim os rótulos nunca "trepam" um no outro.
- Decisão por PONTO (as linhas podem cruzar): comparar os Y dos dois pontos no índice rotulado e mandar cada rótulo para o lado oposto ao da outra linha.

## Regra 2 — Rótulos: grandes, transparentes, 3 posições

- Letra grande (17px nos de linha) e TRANSPARENTE (fill-opacity ≈ 0.55) — legível sem ofuscar o que está por trás (linhas, grade, colunas).
- Mínimo 3 rótulos por série: início, meio e fim. Sufixo de unidade ("/dia", "/h", "p/d") só no rótulo final, quando couber.

## Regra 3 — Cor do rótulo = cor da linha

- Rótulo da linha azul é azul; da dourada é dourado; da verde é verde. Numca branco genérico em gráfico multicolor — o leitor não sabe a qual linha pertence.

## Regra 4 — Headroom: pico não encosta no topo

- Escala com ~15-18% de folga acima do máximo. Rótulo nunca corta no topo nem colide com o cabeçalho; se ainda assim subir demais, rotula abaixo da linha.

## Regra 5 — Padrões de cor da casa

- MM7 = dourada (#e0c040), grossa; série diária = azul fina (#5b9bd5); posts = verde (#39d98a); MM de posts = verde clarinho (#7fe0a8).
- Exceção: em gráfico de BARRAS cujos últimos 7 dias já são dourados, a MM7 vira BRANCA (#f2f6fa) para não sumir.

## Regra 6 — Dados honestos

- Dia parcial NÃO entra (regra 16/08): hoje fora; dia de NASCIMENTO do medidor fora (primeiro registro ≥ 02h = dia pela metade).
- Série com QUEBRA de coleta não se compara antes×depois (caso hoje_navegacoes 09/09) — trocar a métrica ou anotar a quebra no gráfico.
- MM7 de janela móvel usa histórico anterior à janela visível (linha entra "cheia"); sem histórico, começa no 7º ponto — nunca média parcial disfarçada.

## Regra 7 — Eixos

- Duas métricas = dois eixos, rótulos de eixo na cor da série correspondente, valores alinhados às marcas reais da escala.
- Pearson exibido com r², nº de pontos e janela — sempre o da janela VISÍVEL.

---

Aplicação de referência: `svg_semanal_defasada`, `svg_linha_dupla`, `svg_linha`, `svg_barras`, `_ga4_svg_linha_72h`, `svg_mesmo_dow` no `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` (Tencent).
Catalogado em: `CEREBRO_NODE_OBSERVABILIDADE.md` · Histórico de decisões: `Foruns/forum_audiencia_correlacao_posts_20260913.md`.

## Adendo v1.1 (17/09)
- Rótulo de LINHA DE REFERÊNCIA FIXA (média do período): canto OPOSTO ao rótulo final da série (início do gráfico), com desvio automático de colisão. Evita trepar quando média e MM7 convergem (caso Sol 1.8k×1.8k).
