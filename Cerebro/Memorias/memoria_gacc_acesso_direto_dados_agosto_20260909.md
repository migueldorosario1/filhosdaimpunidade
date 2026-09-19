# Memória — GACC acesso direto: log técnico completo (testes, receita, dados ago/2026)

**Data:** 09/09/2026 ~07:5x–08:1x BRT · **Agente:** ZCode Dell (Qwen3.8-Max)
**Fórum irmão:** `Foruns/forum_gacc_alfandega_chinesa_acesso_direto_20260909.md`
**Contexto:** missão do Miguel — entrar na alfândega chinesa (GACC) p/ estatísticas de comércio exterior; testar SSH Beijing. Substitui a fonte morta `beijing_legacy_csv` do agente V4.2 Economia (série parada em fev/2026).

## 1. Testes de acesso (provas)

| Alvo | Origem | Resultado |
|---|---|---|
| SSH `beijing` (ubuntu@82.156.167.218:22, id_ed25519) | Dell | ❌ `Connection timed out` — servidor morto (offline desde ~07/2026, já registrado) |
| `http://www.customs.gov.cn/` (site zh) | Dell | ❌ HTTP 412 (WAF; IP 27.155.113.149) — mesmo c/ headers completos de navegador (UA Chrome, Accept, Accept-Language, Referer) |
| `http://stats.customs.gov.cn/` (consulta zh) | Dell | ❌ HTTP 412 |
| `http://english.customs.gov.cn/` | Dell | ✅ HTTP 200 (~3,7s) |
| `http://english.customs.gov.cn/Statistics/Statistics?ColumnId=1` | **NYC** (ssh nyc + curl) | ✅ HTTP 200 (~10,4s — lento mas funcional) |
| `http://www.customs.gov.cn/` | NYC | ❌ HTTP 412 (WAF não é bloqueio por IP estrangeiro — é desafio JS; versão inglesa não tem) |

Conclusão: **412 = WAF com desafio JS no site chinês** (curl/urllib não resolvem). **A versão inglesa serve os MESMOS dados e não tem desafio** → acesso direto viável do Dell e do NYC (onde roda o coletor V4.2).

## 2. Receita de coleta (GACC inglês)

Seções (`http://english.customs.gov.cn/Statistics/Statistics?ColumnId=N`):
- **ColumnId=1 — Preliminary Release**: tabelas-resumo do mês MAIS NOVO (release de ago/2026 saiu em 09/09/2026; cadência típica: dia 7-10 do mês seguinte). Itens (1)-(5)+(6): totais CNY/USD, por modo de comércio (mensal e acumulado), por país/região, principais exportações e importações (qtd+valor).
- **ColumnId=2 — Monthly Bulletin**: tabelas DETALHADAS com ~1 mês de defasagem (em 09/09 constava até 7.2026): Summary USD (anual/mensal), por país de origem/destino, por Seção/Divisão HS, por regime aduaneiro, por tipo de empresa, por localização dos importadores/exportadores e dos consumidores/produtores.
- ColumnId=3 — Quarterly Release (reviews trimestrais); ColumnId=4 — Release Calendar (calendário de divulgação, tem por ano); ColumnId=5 — Explanatory Notes (metodologia, por ano).

Mecânica:
1. Listar a coluna: `curl -A "Mozilla/5.0" ".../Statistics/Statistics?ColumnId=1"` → os artigos aparecem como `<a href="http://english.customs.gov.cn/Statics/<uuid>.html">(título)</a>`.
2. Baixar o artigo: URL `/Statics/<uuid>.html` → tabela HTML simples (`<table>/<tr>/<td>`), parse direto com regex + `html.unescape`.
3. Unidades: tabelas (1) em "USD 100 Million"; tabela (4) por país em "USD 1 Million" — ATENÇÃO à diferença (o coletor V4.2 já normaliza p/ US$ mi; ÷100 no caso "100 Million").
4. Data de publicação: aparece no HTML do artigo (release ago/2026 = `2026-09-09`).
5. `/newsroom/statistics` (link do menu da home) é 404 — NÃO usar; usar `/Statistics/Statistics?ColumnId=N`.

## 3. Release Agosto/2026 — dados baixados

Arquivados em `Cerebro/dados_gacc/release_agosto_2026/`:
- 10 CSVs parseados: `gacc_01_total_agosto2026_{usd,cny}.csv`, `gacc_02_modo_comercio_agosto2026_{usd,cny}.csv`, `gacc_03_modo_comercio_jan_ago2026_{usd,cny}.csv`, `gacc_04_paises_agosto2026_{usd,cny}.csv`, `gacc_05_principais_exportacoes_agosto2026_{usd,cny}.csv`
- `RESUMO_brasil_e_totais_agosto2026.csv` (série p/ uso jornalístico/V4.2)
- `html_bruto/` (10 HTML originais, proveniência)

UUIDs dos artigos USD de ago/2026 (âncoras; se mudarem, religar via ColumnId=1):
- (1) Total: `f8da41eb-f559-4b41-988e-16a0a1869f0e` · (2) Modo mês: `34bd3bbb-9de3-4ef2-a990-3d864fcdc64f` · (3) Modo acum: `614f33af-46c4-42bd-802b-9efb2825d40c` · (4) Países: `e10175fb-249b-4b8d-9fe5-b8eb0037f1ad` · (5) Principais exportações: `da19d841-89a8-40b8-9f91-9144fe8e884d`

### Números-chave (USD; mês ago/2026 | acumulado jan-ago | YoY)

- **Total China:** 683,80 bi | 5.042,17 bi | **+22,4%** (mês: +26,3% a/a, +0,1% m/m)
- **Exportações:** 401,44 bi | 2.923,84 bi | +19,3% (mês +25,0% a/a)
- **Importações:** 282,36 bi | 2.118,33 bi | +27,0% (mês +28,2% a/a)
- **Superávit:** 119,09 bi no mês | 805,51 bi acumulado
- **Brasil:** total 20,75 bi | **148,24 bi (+23,9%)**; export China→BR 8,09 bi | 57,35 bi (+22,4%); import China←BR 12,66 bi | 90,88 bi (+24,9%)
- EUA: 55,77 bi | 400,84 bi (+5,5%) · ASEAN: 118,61 bi | 862,75 bi (+25,6%) · UE: 78,09 bi | 608,10 bi (+12,4%) · Rússia: 25,60 bi | 185,05 bi (+28,4%) · Índia: 16,81 bi | 125,04 bi (+22,6%) · América Latina: 57,59 bi | 422,64 bi (+19,1%) · África: 34,29 bi | 273,95 bi (+23,3%) · RCEP: 224,04 bi | 1.628,96 bi (+30,2%) · Belt and Road: 350,19 bi | 2.572,45 bi (+20,7%)
- Leitura editorial (tese Sul-Sul/BRICS do V4.2): parceiros do Global South (ASEAN +25,6%, África +23,3%, AL +19,1%, Rússia +28,4%, Brasil +23,9%) crescem MUITO acima dos EUA (+5,5%) — desdolarização/reeixo comercial em curso.

## 4. Pendências p/ plugar no V4.2 (aguarda "vai")

1. No NYC, `coletor_comercio_exterior_v4.py`: trocar fonte GACC de `beijing_legacy_csv` (morto, 2022-01→2026-02) por `gacc_english_direct` — raspar ColumnId=1 mensalmente (cron já existe 07:00/17:00 p/ comércio exterior; adicionar verificação de release novo ~dia 7-10) e ColumnId=2 p/ detalhe.
2. Lacuna a cobrir: mar→ago/2026 (releases anteriores estão listados nas mesmas colunas — cada mês tem seus 10 artigos; backfill possível artigo a artigo).
3. Normalização: tabela (1) vem em "USD 100 Million" (×100 p/ chegar a US$ mi); tabela (4) já em US$ mi.
4. Beijing (82.156.167.218): SSH morto de Dell — confirmar no console Tencent se a instância foi desligada/expirou (só o Miguel tem acesso ao console). Enquanto isso, o GACC direto torna o Beijing dispensável p/ esta finalidade.

## 5. Comandos reutilizáveis

```bash
# teste de vida do Beijing
timeout 20 ssh -o ConnectTimeout=12 -o BatchMode=yes beijing 'echo OK'
# listar release mais novo (preliminar)
curl -sS -A "Mozilla/5.0" "http://english.customs.gov.cn/Statistics/Statistics?ColumnId=1" \
  | grep -o '<a href="http[^"]*Statics[^"]*"[^>]*>[^<]*</a>' | head -12
# baixar artigo e parsear tabela: ver script embutido no histórico desta sessão (regex <table>/<tr>/<td> + html.unescape)
```

---

## 6. ADENDO 09/09 ~08:3x — SOJA POR PAÍS: testes e receitas

### Tabela (6) Major Imports (soja total) — paginação
- A lista da ColumnId=1 é paginada: `?ColumnId=1&page=2` traz itens (6) Major Imports (CNY/USD) + início do release anterior (jul/2026). Itens (6) de ago/2026: CNY `5b03808d-858b-4d54-ae74-7ed61180e98d`, USD `1c29d265-76bf-4a44-9867-224c6ba7ec52`.
- Decodificação do cabeçalho 2 níveis: Commodity | QTY Unit | (8: Quantity|Value) | (1-8 Total: Q|V) | (1-8 Total 2025: Q|V) | (YoY%: Q|V). Linha soja: `Soya beans | 10,000 Tons | 1,214.1 | 5,848.3 | 7,410.7 | 35,244.7 | 7,333.2 | 32,567.8 | 1.1 | 8.2` — qty em 10 mil toneladas, value em US$ mi (tabela USD).

### Browser Use × WAF Ruishu (stats.customs.gov.cn/indexEn)
- IAB (Electron/Chrome 146): `goto` estoura timeout de 32s do playwright (page fica "complete" com body 0); desafio 1º estágio EXECUTA (cookies `SF_cookie_251=...` + cookie dinâmico `AV7KYchI7HHaT=...` aparecem), reload manual não ajuda; `fetch(location.href, credentials:include)` same-origin devolve **412 + desafio novo** (cookie dinâmico some) → 2º estágio reprova fingerprint (UA `ZCode/3.11.2 Electron/41.0.3`, webdriver=false). Veredito: automação de webview NÃO atravessa Ruishu; só navegador humano (ou farm de fingerprint residencial — fora de cogitação).
- A página de desafio curl: `<meta id="...">` + `$_ts` + script externo ofuscado `/Qy6JDI4LYvbD/....js` = assinatura Ruishu Botgate.

### UN Comtrade preview (sem key)
- `GET https://comtradeapi.un.org/public/v1/preview/C/M/HS?reporterCode=156&period=YYYYMM&cmdCode=1201&flowCode=M` — máx 1 período por request; China = count 0 em 2025-11..2026-07 (todos). API legado comtrade.un.org/api = 302 → comtradeplus (morto).

### ComexStat soja BR→China (FUNCIONOU — receita validada 09/09)
```
POST https://api-comexstat.mdic.gov.br/general   (sem chave; Content-Type: application/json)
{"flow":"export","monthDetail":true,
 "period":{"from":"2025-01","to":"2026-12"},
 "filters":[{"filter":"country","values":["160"]},
            {"filter":"ncm","values":["12011000","12019000"]}],
 "details":[],"metrics":["metricFOB"]}
```
- Resposta: `data.list[]` com `{year, monthNumber, metricFOB}` (US$ brutos → /1e6).
- Armadilhas: **429 frequente** (limite ~1 req/10s — backoff 20-25s, como no coletor V4.2); métricas de peso (`metricStatNetWeight`, `metricStatGrossWeight`) = **400 "Métrica inválida"** no flow export (só FOB/CIF); China=160 (código SISCOMEX confirmado).
- Série obtida: jan/2025→ago/2026 (20 meses); jan-ago/2026 = US$ 27.496 mi FOB; ago/2026 = US$ 3.140,0 mi.

### US Census (perna EUA) — BLOQUEADO sem key
- `https://api.census.gov/data/timeseries/intltrade/exports/hs?get=E_COMMODITY,E_ALL_VAL_MO&time=YYYY-MM&E_COMMODITY=12010000&E_COUNTRY=5700` → 302 → `/data/missing_key.html`. Key grátis em api.census.gov (exige e-mail). Variáveis p/ quando houver key: E_ALL_VAL_MO (mês), E_ALL_VAL_YR (acumulado), E_COUNTRY=5700 (China), E_COMMODITY=12010000 (soja HS6+).

### Derivados (shares espelho)
- Share BR no valor das import. chinesas de soja jan-ago/2026: 27.496/35.244,7 = **78,0%** (GACC CIF-like × ComexStat FOB → margem ±3-5 p.p.). Ago: 3.140,0/5.848,3 = **53,7%** (entressafra BR; resíduo de US$ 2,7 bi = EUA? Argentina/Uruguai/Rússia? — sem espelho EUA não confirma).
- Preço médio soja China jan-ago/2026: 35.244,7/74,107 = **US$ 475,6/t** (ago: 481,7/t; jan-ago/2025: 444,1/t → +7,1% a/a no preço).
