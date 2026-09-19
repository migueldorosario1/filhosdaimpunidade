# Memória: fix do gráfico 24h do LUMINA (y invertido) — 02/09/2026 ~23:5x BRT

**Quem:** ZCode (GLM-5.3, DSH) · **Ordem:** Miguel, por voz ~23:2x — "o primeiro
gráfico da página do LUMINA no painel CCTV, páginas vistas por hora, tá muito
feio, quebrado, não dá pra ver nada — conserta".

## 1. Sintoma

`/v6/lumina` (público `http://43.156.151.165/v6/lumina`, interno
`127.0.0.1:8084/lumina` — nginx faz **strip do prefixo /v6**, atenção no teste
interno: `/v6/lumina` na 8084 dá 404 "rota nao encontrada"): o primeiro gráfico
("📉 LUMINA — páginas vistas por hora — últimas 24h") aparecia espremido no
topo da caixa, com a maior parte das barras invisível.

## 2. Causa-raiz

`_umami_svg_24h()` desenhava com o **chão no TOPO do SVG** (`base=30`,
`viewBox 0 0 960 210`): `y = base - h1` dava **y negativo** para toda barra
acima de 30px — a barra nascia acima do canvas e era cortada. Prova no HTML
ao vivo: **47 rects com y negativo** (24 azuis + 23 amarelas, ex. `y="-43"`).
Era o MESMO y-invertido do gráfico GA4 corrigido na manhã do 02/09
(`svg_barras_hora_ga4`, base=178) — a correção de lá não alcançou o LUMINA.

## 3. Correção (padrão visual do gráfico GA4 já consertado)

- Chão EMBAIXO: `chao=182`, área útil 150px, `viewBox 0 0 960 232`.
- Grade sutil (⅓/⅔/teto) + linha de chão destacada.
- Rótulos de hora a cada 3h (00 03 06 … 21) e **data** no 1º bucket + na
  virada do dia (00h).
- Cabeçalho com contexto: `máx N/h · 24h X pageviews`.
- `<title>` do mouse com data completa: `02/09 14h — 621 pageviews`.
- Compat mantida: chave antiga `t` do Umami, aviso "aguardando beacons",
  zero-toques fora da função (+1 comentário-marca no HTML).

## 4. Prova (deploy 02/09 ~23:5x)

- Backup no servidor: `painel_cctv_v6.py.bak_lumina24h_20260902` (antes do swap).
- `py_compile` **no servidor (3.12.3) antes** de tocar no serviço — arquivo
  inteiro não compila no python 3.10 local (f-string com `\w` pré-existente,
  linha ~6758: usar o gate do servidor).
- `sudo systemctl restart cctv-v6` (ubuntu não reinicia sem sudo — senha-free OK).
- Público 200 · `RECTS_Y_NEGATIVO: 0` (era 47) · 24+24 barras y∈[32,141] ·
  marca `fix_lumina_24h_y_invertido_20260902` no HTML · 7 rotas irmãs 200
  (`/`, audiencia, audiencia-redundante, sol, reforma, custos, api) · journal
  sem erro.

## 5. Lições

1. **Bug-irmão**: quando corrigir geometria de um gráfico SVG, **procurar o
   mesmo padrão nos gráficos vizinhos** no mesmo dia — o GA4 foi corrigido e o
   LUMINA ficou doente com o mesmo sintoma.
2. **SVG de barras**: checar SEMPRE que `y + height ≤ viewBox height` e
   `y ≥ 0` no teste — 1 asserção dessas teria pego o bug no deploy original.
3. **Ambiente local ≠ servidor**: validar py_compile na MESMA versão do
   servidor (3.12) antes do swap; 3.10 local rejeita código legal do 3.12.
4. **Teste interno do painel**: nginx remove `/v6` — interno é
   `:8084/lumina`, não `:8084/v6/lumina` (senão 404 enganoso).

## 6. Arquivos

- Produção: Tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py`
  (md5 `a9d37796ed904a8595218a4c811303d3`).
- Repo: `.tencent_v6_oficina/fix_lumina_24h_20260902/painel_cctv_v6.py`
  (cópia = produção), `vivo_20260902/painel_cctv_v6.py` (mirror sincronizado),
  `painel_cctv_v6.py` da oficina (base antigo com a mesma função corrigida,
  para o bug não voltar num redeploy daquele base).
