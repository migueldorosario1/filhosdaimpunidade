# MEMÓRIA TÉCNICA — /v6/diretrizes-ceo vira casa do Manual de Estilo + GA4 da /v6/audiencia (11/09/2026)

> Log técnico completo do sprint ZCode/Kimi K3 11/09 ~12:5x→13:1x.
> Fórum irmão (decisões/estado): `Foruns/forum_diretrizes_ceo_casa_manual_estilo_20260911.md`.

## A. Diagnóstico GA4 da /v6/audiencia (pergunta do Miguel: "gráfico parado no dia 10?")

**Cadeia da página:** `pagina_audiencia()` (tencent `~/cafezinho/v6/painel_cctv_v6.py:3130`) → `ga4_serie_diaria(dias=92)` (:248) e `ga4_serie_horaria(horas=40)` (:278) → GA4 Data API v1beta, propriedade `374552425` (env `GA4_PROPERTY_ID`), credencial `~/cafezinho/Projeto Cafezinho Agentes/root/ga4.json`. Cache 30 min (`_cache_get`, V6_CACHE = `~/cafezinho/Projeto Cafezinho Agentes/root/agent_data/cctv/v6`); em falha de fetch serve `_cache_get_stale`. Cron `*/25` (WARM_CACHE_V6_20260816) mantém a série quente via curl localhost:8084.

**Provas colhidas:**
1. Página gerada 11/09 12:57 mas eixo diário terminava em 10/09 ("mais recente (10/09): 3.583") e o horário de 40h só tinha rótulos 09/09-09/10 → dado velho, renderizador vivo.
2. API GA4 ao vivo (mesma credencial/caminho do painel) responde OK — diário: 08/09=12.480 · 09/09=11.748 · 10/09=3.655→3.668 (cresceu entre consultas = backfill parcial) · 11/09=1.
3. Horário GA4 (dateHour): 09/09 normal (300-630/h); 10/09: 09h=245, 10h=251, **11h=149 (início do penhasco)**, 12h=78, 13h=41 … 22h=8, 23h=5; 11/09 00h=1.
4. Sem filtro `platform=web` e com dimensão platform: idêntico (tudo web) → filtro inocentado.
5. Totais 10/09: sessions 3.034 / users 2.751 / views 3.668 (~25-30% do normal) → parcial, não zero absoluto.
6. **Tempo real GA4: 68 activeUsers** (11/09 ~15h) — compatível com a razão histórica GA4/contador próprio (~12-13%).
7. **Contador próprio** (`agent_data/cctv/v6/audiencia_red.jsonl`, push do site */5min): 10/09 completo e normal (~96,6 mil navegações/dia); 11/09 às 13h: 66.551 navegações, 8.304 visitantes, horas 3.076-12.817. Lumina (Umami) também viva.
8. Tag no site: home e post de hoje (269969) HTTP 200 com `<script async src=".../gtag/js?id=G-4E5DKNTYET">` + `gtag('config','G-4E5DKNTYET')` — embed normal, **sem** `rocketlazyloadscript`/delay.

**Veredito:** stall de processamento dos relatórios padrão do GA4 no lado Google desde 10/09 ~11h BRT (tempo real imune; tag, site, credenciais e tráfego sãos). Backfill esperado em 24-72h. **Nenhuma ação corretiva nossa.** Melhoria futura proposta (aguarda "vai"): faixa de honestidade GA4×FAROL na /v6/audiencia.

## B. Reforma da /v6/diretrizes-ceo (build)

**Antes:** matriz ETAPA × ESCOPO de ~25 slots de prompt do V4 (`pagina_diretrizes_ceo()` em `painel_cctv_v6.py:4901`, módulo `v6/ceo/` — engine 27 KB, registry.yaml, fila de patches, shadow_v4).

**Depois (NO AR):** hub do Manual de Estilo. Módulo novo **`tencent:~/cafezinho/v6/painel_cctv_v6_diretrizes_estilo.py`** (padrão modular da casa, como `painel_cctv_v6_controle.py`):
- `MANUAIS`: registro slug→arquivo (7 manuais em `~/cerebro-miguel/cerebro/Estilo/`);
- `_md_para_html()`: conversor md→HTML stdlib (h1-h4→h3-h5, bold/em/code, ul c/ sub-item, blockquote, hr, tabelas pipe, fence ```; escapa HTML antes do inline);
- `_extrair_sintese()`: recorta `## ⚡ SÍNTESE OPERACIONAL` do unificado via regex `re.S`;
- `render_estilo_home()` / `render_manual(slug)`: retornam HTML interno (o `chrome()` do painel embrulha; `active="ceo"` preserva o menu);
- `handle_post_estilo()` / `handle_post_estilo_remover()`: fila em `~/cafezinho/v6/ceo/ceo_data/estilo_propostas.jsonl` (append; remoção = soft delete `status:"removida"` + `removida_em` — nada se apaga). ID `EST-AAAAMMDD-NNN` sequencial por dia (BRT). Validações: tipo ∈ {incluir,remover,alterar}, manual ∈ slugs, texto ≥ 8 chars (teto 2.000), autor ≤ 60.

**4 edições ancoradas em `painel_cctv_v6.py`** (assert count==1 cada, aplicadas por script):
1. ROUTES: `"/diretrizes-ceo"` → lambda chrome+`render_estilo_home()`; `"/diretrizes-ceo-v4"` → `pagina_diretrizes_ceo` (matriz antiga preservada);
2. do_GET: `elif path.startswith("/diretrizes-ceo/manual/")` antes de `/audiencia-redundante`;
3. do_POST: `/api/estilo/propor` e `/api/estilo/remover` (aceita também prefixo `/v6` — ver armadilha abaixo);
4. cartão da home: descrição → "Casa do Manual de Estilo — ler o unificado e os específicos, propor itens".

**Armadilha resolvida (nginx):** o server da porta 80 (`/etc/nginx/conf.d/painel.conf`) só tem `location /v6/ → 8084` (strip) — **não existe** `location /api/` para o painel (as APIs antigas do CEO, `/api/ceo/*`, nunca funcionaram pela URL pública). Solução sem tocar o nginx: JS chama `/v6/api/estilo/*`; o strip entrega `/api/estilo/*` ao painel; do_POST aceita as duas formas (padrão "2o alias" já usado em `/v6/custos/ao-vivo`).

**Backups (tencent `~/cafezinho/v6/`):** `painel_cctv_v6.py.bak_pre_diretrizes_estilo_20260911` (estado anterior íntegro) + `.bak_fix_api_estilo_20260911` (após as 4 edições, antes do fix do /v6/api). Cópia de trabalho do módulo: `/tmp/painel_cctv_v6_diretrizes_estilo.py` no Dell (reenviada por scp).

**Rollback total:** `cd ~/cafezinho/v6 && cp painel_cctv_v6.py.bak_pre_diretrizes_estilo_20260911 painel_cctv_v6.py && rm painel_cctv_v6_diretrizes_estilo.py && sudo systemctl restart cctv-v6` (a rota volta à matriz V4).

**Provas de aceite (curl externo, UA navegador):**
- `/v6/diretrizes-ceo` 200 (19.137b) — marcadores: Síntese operacional ✓ Manuais específicos ✓ Interagir — propor item ✓ link -v4 ✓ "Ler o Manual Unificado inteiro" ✓;
- manuais 200: unificado (47.851b, c/ EMU-13 e Núcleo A) · escrita (24.459b) · portal (27.526b) · titulo (10.577b) · bom-gosto (13.597b) · publicador (17.398b) · comunicacao (16.685b); slug inválido → página amigável 200;
- fumaça da fila: POST propor → `{"ok":true,"id":"EST-20260911-001"}` → hub exibe → POST remover → `{"ok":true}` → hub sem a proposta → jsonl com 1 registro "removida"; tipo inválido → `{"ok":false,"erro":"tipo inválido…"}`;
- regressões: `/v6/diretrizes-ceo-v4` 200 (matriz viva) · `/v6/audiencia` 200 · home `/v6/` com cartão novo ✓;
- `py_compile` módulo + painel OK; `systemctl is-active cctv-v6` = active (restart via `sudo -n`).

**Pendências (aguardam "vai" do Miguel):** (1) faixa GA4×FAROL na /v6/audiencia; (2) sync das propostas de estilo → Cérebro (hoje curadoria manual no jsonl do Tencent); (3) cópia do módulo para o repo `.tencent_v6_oficina/` (padrão dos módulos do painel).
