# Memória técnica — /v6/tendencias: entidade no título + score rotulado (ZM-20260910-024)

**Fórum par:** `Foruns/forum_tendencias_entidade_titulo_score_rotulo_20260910.md`

## Caminho da investigação

1. Card suspeito: post 269603 (`?p=269603`), título com `&#8220;` visível no /v6/tendencias (bloco "Top 10 Tendências — Algoritmo de Velocidade V2").
2. HTML do CCTV: entidade vinha ESCAPADA (`&amp;#8220;`) — escape duplo.
3. Post público: H1 com `&#8220;` crua (browser decodifica → leitor vê “ ”), `<title>`/og com `&quot;`; corpo com 17 ocorrências (todas renderizam bem).
4. Banco (cafezinho-wp): `wp post get 269603 --field=title` = aspas RETAS; varredura `post_title LIKE '%&#8%'` últimos 600 = 0 rows.
5. Cadeia: banco (retas) → REST `cafezinho/v1/top-tendencias` devolve `get_the_title()` com filtros (curvas como `&#8220;`) → painel `_card()` aplica `html.escape` → dupla → visível.

## Mudanças (tencent painel_cctv_v6.py, backup .bak_pre_tend_score_20260910)

- `title = html.unescape(str(item.get("title", "")))` no loop do Top 10.
- Rótulos: "Score Gravidade V2" → **"Score Tendência V2"**; "Velocidade: X views/h" → **"Ritmo agora: X views/h (últimas 6h)"**.
- Parágrafo do algoritmo + fórmula: agora exibe `Score = views/h nas últimas 6h + 0,15 × [Views_48h / (Idade_h + 1,5)^1,2]` com explicação (ritmo recente manda, volume pesa 15%).
- py_compile OK · restart cctv-v6 active · prova pública: 0 `&amp;#8220;`, título com “ ”, rótulos novos presentes.

## Fórmula validada (produtor `nyc:/root/top_tendencias_push.py`)

- `ga4_views_recentes_por_slug(6)` = velocidade atual; `grav_v2 = v_total/((age+1.5)**1.2)`; `v_score = vel_atual + grav_v2*0.15`; `v_h = v_per_hour` (ritmo 6h); `views = v_total` (hoje+ontem ≈ 48h).
- Checks: 269603 = 0,84+0,094 → 0,93 ✓; 269641 = 9,84+0,433 → 10,27 ✓.
- v3 "velocidade ATUAL manda" = ordem Miguel 24/08 (bak `.bak_pre_vel_atual_20260824` no NYC).

## Lições

- Título exibido por painel que consome REST WP: SEMPRE `html.unescape` antes do próprio escape (WP entrega texto filtrado com entidades).
- Rótulo de métrica que não explica a janela ("views/h" sem "últimas 6h") gera falsa suspeita de bug — a pergunta do Miguel nasceu disso.
- Rollback: `ssh tencent "cd /home/ubuntu/cafezinho/v6 && cp painel_cctv_v6.py.bak_pre_tend_score_20260910 painel_cctv_v6.py && sudo systemctl restart cctv-v6"`.
