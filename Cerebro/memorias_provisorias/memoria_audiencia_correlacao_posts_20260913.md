# Memória — GA4 /v6/audiencia: correlação posts×audiência — 13/09/2026 (ZCode/GLM-5.3)

Log técnico completo do sprint. Decisões resumidas: `Foruns/forum_audiencia_correlacao_posts_20260913.md`.

## Arquivos tocados

| Arquivo | Ação |
|---|---|
| tencent `/home/ubuntu/cafezinho/v6/painel_cctv_v6.py` | 3 edições (função nova, SVG reformulado, seção da página) |
| tencent idem `.bak_pre_correlacao_posts_20260913` | backup pré-mudança (rollback 1 comando) |
| tencent `.../agent_data/cctv/v6/pubs_dia_correlacao.json` | cache novo da contagem (apagado 1× p/ corrigir versão incompleta) |
| local `ZCodeProject/tencent_v6_audiencia/` | `painel_cctv_v6.py` (edição, md5 = servidor), `testa_rest.py`, `audiencia_correlacao.png` + `recorte_correlacao.png` (screenshot) |

## Mudanças de código

1. **`pub_contagem_diaria(ndias=45) -> dict`** (inserida antes de `pub_serie_horaria`): REST `WP_API/posts?status=publish&per_page=100&page=N&orderby=date&order=desc&after=<47d>&_fields=id,date`, auth Basic (`.wp_creds`), loop `range(1,31)` com break em página vazia/curta; conta por dia BRT (`_pub_dia_hora_brt`), só `d < hoje`; cache `_cache_get/_cache_set("pubs_dia_correlacao.json", 3600)`; fail-open (exception → stale cache ou `{}`).
2. **`svg_linha_dupla(serie, posts_dia=None, janela=7)`** reformulada:
   - escala esquerda ÚNICA `vmax = max(max(vals), max(mm)) * 1.12` (era: dois máximos independentes);
   - `np_ = posts_dia.get(data, 0)` por ponto; `escala_p = max(pmax*2, 4)` (coluna máx = 50% da área);
   - colunas `<rect>` `#39d98a` fill-opacity 0,16 rx=2, largura = passo×0,55 (mín 4px), desenhadas ANTES das linhas (por baixo);
   - rótulo `<text>` font-size 10,5 verde em `y = topo - 3` para cada q > 0;
   - rótulos eixo esquerdo agora cinza `#6a8aaf` (antes dourado) — eixo tem 2 séries; eixo direito verde com `{pmax, max(1,round(pmax/2))}` em `Yp(v)`;
   - legenda nova: "views diárias + MM7 (ambas no eixo esquerdo)" + "▮ posts publicados no dia (nº em cima da coluna · eixo direito)".
3. **Seção da página** (`pagina_audiencia`/GA4): título reescrito + `<p>` explicativo + `{svg_linha_dupla(fechada[-40:], posts_dia=pub_contagem_diaria())}`.

## Comandos/provas (executados)

- `python3 -m py_compile` LOCAL FALHOU (Python local 3.10 × servidor 3.12; f-string com backslash pré-existente na linha ~4343 é PEP 701). Aprovado com `ast.parse` no 3.12 do servidor + teste isolado da função extraída por regex em 3.10 local (33 colunas/33 rótulos/max=7 OK; sem posts → só linhas OK).
- Deploy: scp → `/tmp/painel_cctv_v6_novo.py` → `ast.parse` OK → `cp` → `systemctl restart cctv-v6` (active) → md5 servidor = local.
- Rota interna é `/audiencia` (nginx faz strip do `/v6/`; primeiro curl em `/v6/audiencia` na 8084 deu 404 esperado).
- Cache incompleto detectado: v1 com `range(1,9)` parou em 21 dias (711 posts ≈ 8 páginas cheias). Corrigido para 30 páginas, cache apagado, regerado: 47 dias, 2.205 posts.
- Diagnóstico REST: 2.214 posts/23 páginas/**22,2s** (~1,1s/página) — a lentidão de ~2min do primeiro load era a página GA4 INTEIRA fria (GA4 realtime/séries), não o gráfico novo; quente = 0-3s.
- Provas HTTP: interno 200 (40 colunas, rótulos 15→70, eixo direito 35/70); público 200 UA Chrome (64.093 bytes, 40 colunas); coluna de 70 tem topo em f=0,5 exato (`y=164,7` com área útil 260px).
- Screenshot headless Chrome 1400×3400 + recorte PIL; visão 5/5 aprovada.

## Lições

- **Paginação REST precisa de limite GENEROSO ou esgotamento real**: 8×100 parecia muito e cortou agosto (~50 posts/dia). Nesta casa, janela de posts = sempre calcular pelo pior caso histórico (~70/dia), não pelo plano atual (2-3/dia).
- py_compile local (3.10) não valida código do servidor (3.12/PEP 701): usar `ast.parse` remoto como gate.
- Cache de arquivo da casa envelopa `{_ts, data}` e `_cache_get` desembrulha — funções novas podem cachear valor puro sem se preocupar.

## Estado

- **O que aconteceu:** no ar, provado, auditado visualmente.
- **O que falta:** homologação do Miguel; nada técnico.
- **O que preciso do Miguel:** nada além do "ok visual" (ou ajustes de cor/altura/janela se quiser).

## Adendo v1.1 (13/09 ~15:5x)

- `svg_linha_dupla` ganhou bloco MM7 de posts: para cada data da série, média de `posts_dia` das 7 datas consecutivas TERMINANDO nela (`date.fromisoformat` + `timedelta`); polyline `stroke="#7fe0a8" stroke-width="2.2" stroke-opacity="0.55"` em `Yp(v)` (escala de posts); legenda nova.
- Ajuste de rótulo: i=0 da MM7 de views com `(dx,dy)=(16,-22)`; meio `(0,-9)`.
- Lição: MM7 por data real > `_media_movel` sobre a janela visível quando existe histórico anterior no insumo (linha entra cheia, sem artefato de rampa).
- Testes: extração por regex + exec isolada 3.10 (40 pontos; 1º ponto = média cheia 5,29 no fake; sem posts_dia → sem linha); deploy AST OK 3.12; provas interno/público 200; screenshots v11 + final auditados.
- Arquivos novos: `audiencia_correlacao_v11.png`, `recorte_correlacao_v11.png`, `recorte_v11_final.png` (ZCodeProject/tencent_v6_audiencia/).


## Adendo v1.2 (13/09 ~18:1x) — análise estatística 6 meses

- Extração no Tencent: script importável (`if __name__` guard confirma) reusou `ga4_serie_diaria(184)` (cache próprio `ga4_serie_374552425_184d.json`, não interfere nas janelas do painel) + varredura REST 171 páginas (`after=190d`, X-WP-Total=17055 conferido). 1ª tentativa cortou em 13k por teto de 130 págs — de novo a lição do pior caso (~90 posts/dia médio em 6 meses!).
- Estatística local (numpy/scipy): Pearson/Spearman níveis, lags 0-14 e reverso, ΔMM7 (sem tendência), correlação mensal, regressão. Gráfico matplotlib 2 painéis (índice base 100 + dispersão), auditado por visão 3/3.
- Números-chave ver análise no fórum §Adendo v1.2 (fórum é a referência). Artefatos: analise_6meses.json/png/nums.json + extrai_6meses.py + analisa_6meses.py no ZCodeProject/tencent_v6_audiencia/.
- Lição: correlação de NÍVEIS em séries com tendência comum superestima relação — sempre reportar ΔMM7 junto; melhor lag da resposta de audiência = 2-3 dias.


## Adendo v1.3 (13/09 ~18:2x)

- Base semanal defasada (audiência semana N × produção média diária N-1): script inline gerou `correlacao_semanal.csv` (24 semanas, 23/03→31/08) + `correlacao_semanal.png`. r=+0,721/r²=52%/ρ=+0,742.
- Lições: (1) REST WP não retorna dias sem publicação — em agregações por período, usar `get(dia,0)`, nunca descartar; (2) semana corrente só entra quando os 7 dias fecharem; (3) correlação semanal defasada (0,72) >> ΔMM7 diário (0,34) — a granularidade semanal é a melhor lente para esse par de indicadores.


## Adendo v1.4 (13/09 ~18:4x)

- `svg_semanal_defasada(serie, posts_dia)` nova (semanas seg→dom fechadas em `all(x in views)`; posts `get(x,0)`; Pearson manual cov/σ; rótulos X a cada `max(1,n//11)`); seção nova na página; `pubs_dia_190d()` leitor de cache longo; `sync_pubs_190d.py` + cron 23 */6 (backup crontab ~/crontab.bak_pre_pubs190_20260913).
- Testes: extração-por-regex do SVG com dados reais → 24-25 semanas, r manual +0.720 vs scipy +0.721 (diff 0,0012); deploy AST OK; provas interno/público; screenshot auditado.
- Lições: (1) varredura de minutos NUNCA no request — cron + cache + TTL generoso + fail-open; (2) GA4 pode omitir dias com 0 views → `all(x in views)` protege semanas furadas e backfill do Google pode adicionar semanas antigas depois (25ª semana apareceu sozinha).


## Adendo v1.5 (13/09 ~18:5x)
- m_v = sum(7 dias) sem /7; rótulo 'views/semana'; r invariante (+0,72). Deploy + provas + screenshot 5/5.


## Adendo v1.6 (13/09 ~19:0x)
- Versão final: janela móvel 7d, 56 dias, dourada = média diária (v7/7), verde = posts/dia janela anterior. r visível +0,18 (8 semanas misturam jul+/ago−/set+ — coerente com análise mensal). Screenshot 5/5.


## Adendo v1.7 (13/09 ~19:1x)
- Defasagem 1 dia (posts D-7..D-1), n=30; conferência manual exata (10.358 × 29,0). r 30d = −0,60 (agosto negativo domina o recorte — coerente com análise mensal). Screenshot auditado.


## Adendo v1.8 (14/09 ~23h BRT)
- 4 páginas c/ gráfico defasado (unidade por fonte); serie_diaria_farol/lumina novas (cache 1h, dia BRT); guard 12d; _exemplo_janela dinâmico. r estreia: FAROL −0,69/LUMINA −0,27/SOL +0,90/GA4 −0,52. Fusos ancorados (sv=BRT; lumina coletado_em=BRT). Lição: f-string com chamada de função em template inserido por script — chaves simples avaliam, duplas viram literal; testar grep do resultado ANTES do deploy pegou o bug.


## Adendo v1.9 (15/09 ~11:4x)
- Auditoria DOW FAROL: não acumulava; artefato = dia de nascimento parcial (24/08 14:30) como dia cheio. Fix `_descartar_nascimento_parcial` (1º registro ≥02:00 = parcial) nas 3 séries do jsonl. Lição: série de medidor jovem sempre checar o PRIMEIRO dia — nascimento no meio do dia vira barra fantasma. GA4 das mesmas datas como contra-prova.


## Adendo v2.0 (15/09 ~12h)
- Auditoria defasado FAROL: aritmética ok; `hoje_navegacoes` com QUEBRA de série 09/09 (3,9→6,7 nav/visitante; cadência do pusher mudou 09:05) → gráfico migrou p/ hoje_humanos_distintos (16.814/dia, r=−0,61). Inversão posts×audiência de setembro é REAL (r −0,71 em humanos). Bug registrado em BUGS_ATIVOS.


## Adendo v2.1 (15/09 ~12:1x)
- Lumina auditado: série limpa (razão v/d estável, padrão semanal), r=−0,73, visitas +31% × posts −23% — fenômeno REAL, sem fix. Consolidação curto-prazo: GA4 −0,52 · FAROL humanos −0,61 · Lumina −0,73 (vs +0,72 no longo). Lição de auditoria: razão métrica-derivada (nav/visitante, visitas/visitante) + padrão de fim de semana = os 2 testes rápidos para separar artefato de crescimento real.


## Adendo v2.2 (15/09 ~12:2x)
-views-GA4 por humano caiu 1,01→0,59 em set (gente nova rasa/adblock) + stall GA4 10/09 = GA4 flat vs FAROL/Lumina subindo. Métrica explica o paradoxo assimétrico. Régua rápida: cruzar GA4×FAROL humanos pela razão views/humano para detectar mudança de MIX de tráfego.


## Adendo v2.3 (15/09 ~12:3x)
- svg_barras + MM7 branca (#f2f6fa) sobre as barras; offset = len(serie)-len(dados), ini=max(0,6-offset) (linha cheia quando há histórico); rótulo final/dia. Cor: MM7 dourada é padrão da casa, MAS aqui as barras dos últimos 7d já são douradas → branca para contraste. Sol herdou de graça.


## Adendo v2.4 (16/09 ~16h)
- 72h: headroom 18% + rótulo de pico abaixo da linha (y<34→XY+20). Página: gráficos→Top20→coortes 7d/30d no fim. Auditoria 40d: posts EXATOS vs WP (10/10 dias). WP REST: HTTP 500 intermitente em varreduras longas → retry 3×/backoff 20s no pub_contagem_diaria. Obs: página tinha sido refeita por outra sessão (72h linha, fechado=72h atrás) — baixar código do servidor ANTES de editar (md5 confere).


## Adendo v2.5 (16/09 ~16:1x)
- Rótulos do 72h: azul claro #8fc4ff + '/h' (associação de cor à linha), offset 17/23px. Mesma função = GA4+LUMINA corrigidos juntos.


## Adendo v2.6 (16/09 ~16:3x)
- Padrão rótulo 17px/fill-opacity 0.55/início-meio-fim em 6 funções (semanal_defasada, linha_dupla+colunas 13/0.55, linha, barras, 72h, mesmo_dow +2px/0.6 c/ halo). Sufixo /dia só no fim; verde 'p/d'.


## Adendo v2.7 (16/09 ~18:2x)
- MANUAL_DE_GRAFICOS_V1 no Cerebro/Estilo (7 regras). Regra 1 implementada por ponto com clamp; teste anti-colisão (pares ≥17px); linha_dupla idem quando MM < linha azul.


## Adendo v2.8 (16/09 ~18:3x)
- svg_barras: média do período (linha verde tracejada + rótulo com desvio de colisão automático). Padrão MM7-branca-ondulada (tendência) × média-verde-tracejada (referência fixa).


## Adendo v2.10 (17/09 ~09:5x)
- totalUsers paramétrico nas séries GA4 (cache com sufixo); gráfico 72h usuários + 7 cards de usuários nos comparativos. Sanidade: MM7×7 ≈ total7d.
