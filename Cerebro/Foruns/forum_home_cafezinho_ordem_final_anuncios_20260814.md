# Fórum — Home Cafezinho: ordem final dos blocos + anúncios empilhados (14/08/2026)

**Sessão:** ZCode GLM-5.2 (workspace ZCodeProject) · **Status:** ✅ CONCLUÍDO E NO AR nos 2 servidores (14/08 ~14:25 BRT (espelho em UTC: 17:20))

## O que o Miguel pediu (3 rodadas)

1. "Recentes e histórico no final" → depois: "últimos blocos: **Recentes → Top 10 → Linha do Tempo → Histórico** (histórico é o último)".
2. "Não pode ter anúncio empilhado — um antes e um depois" (prints 13:33 e 14:15 mostravam 2-3 anúncios em fila após o Regional).

## Ordem final da home (canônico `ocafezinho.com` = espelho `cafezinho.news`)

Hero → Nacional → Regional → Coluna do Editor → Geopolítica → Tecnologia → Economia → Vídeos → Cultura → Meio Ambiente → Saúde → Esporte → **[ad after-latest] → Recentes → [ad after-recents] → Os 10 mais vistos → Linha do Tempo** → rodapé → **Histórico (painel cz-hist, último elemento)**.

## O que foi feito

- **Canônico** (`front-page.php`, tema `ocafezinho-portal`): bloco **Recentes** (junto dos banners `banner-after-latest-*` e `banner-after-recents-*`) movido do topo (era 2º) para depois de Esporte; **Top 10** movido para antes da **Linha do Tempo** (LT = última seção). Backup: `front-page.php.bak_pre_ordem_final_20260814`.
- **Bug próprio corrigido no caminho**: a linha `banner-after-latest-desktop` se perdeu no 1º recorte (python) — detectado por diff forense e restaurado; validado com diff completo (única diferença era essa linha).
- **Espelho**: estava `LinhaDoTempo → Top10 → Recentes` (edição de sessão anterior); reordenado para igualar o canônico (Recentes → Top10 → LT). Backup `.bak_pre_ordem_final_20260814` idem.
- **Anúncios empilhados — causa raiz**: plugin **Ad Inserter** (inserção client-side "antes do N-ésimo parágrafo", blocos 26-29/33-37) sem flag de home → injetava anúncios extras no meio do conteúdo da home, colados nos banners fixos do tema (região Regional→Coluna = prints do Miguel). Bloco 14 (`section:nth-child(8) > div`, home=1) casava 0 elementos (seletor posicional frágil). **Correção:** `display_on_homepage='0'` em TODOS os blocos do Ad Inserter (**85 no canônico, 96 no espelho**) via `wp eval` — posts/páginas internas intactos. Backups da option em `/tmp/ad_inserter_bak_20260814.txt` nos 2 servidores.
- Caches limpos (wp cache flush + rm wp-rocket) nos 2.

## Verificação (browser real, desktop 1440px)

Slots desktop renderizados: top(218) → after-manchete(1196) → after-colunistas(3374) → after-latest(11121, **antes do Recentes**) → after-recents(11956, depois) → sticky. Nenhum anúncio fora dos slots do tema; nenhum empilhamento; conteúdo entre todos.

## O que falta / próximos passos

- Acompanhar leilão GAM: `after-recents-desktop` ficou vazio na verificação (rotatividade, slot correto).
- Se o Miguel quiser anúncio extra no MEIO da home (Geopolítica→Esporte não tem nenhum), o caminho limpo é slot no tema (front-page.php), nunca Ad Inserter posicional.
- Print 14:14:33 do Miguel (Recentes→Histórico→Top10) não bateu com nenhum estado real — provável aba/cache de transição; pedido já coberto pela ordem final.

## Rodada 4 (14/08 ~15:00 BRT) — o "Histórico" esclarecido

Miguel esclareceu: o que ele quer em último é o **toggle "Histórico"** (link vermelho que abre o menu por ano/mês), que aparecia DEPOIS do Recentes e ANTES do Top 10. Causa: mu-plugin `cafezinho-historico.js` (V1 27/07) movia o painel para **dentro do fim da seção Recentes** via JS. **Fix:** trecho de reposicionamento agora aponta para a **última `section.pb-5 .container-xxl`** (Linha do Tempo) — Histórico vira o último bloco. Backup `cafezinho-historico.js.bak_pre_ultimo_20260814` no servidor. Espelho não tem o painel (nada a fazer). Validação browser: …Recentes → Top10 → LinhaDoTempo → **Histórico (último)** ✓.

**Lição de cache:** alterar mu-plugin NÃO reflete sozinho — cache de página (WP Rocket dir + `wp-content/cache/busting/`) servia HTML com `?ver=` velho; purge completo (`wp-rocket/` + `busting/*` + `wp cache flush`) resolveu; loader versiona por `filemtime`.

## Rodada 5 (14/08 ~16:10 BRT) — 2 anúncios empilhados no CELULAR antes do Nacional

Print/relato do Miguel no celular: dois blocos repetidos entre a manchete e o Nacional. Causa: `banner-after-manchete-mobile` e `banner-after-colunistas-mobile` estavam quase adjacentes no topo do front-page.php (a Coluna só é ecoada lá embaixo — no celular não havia conteúdo entre os dois slots). Fix: `banner-after-colunistas-mobile` movido para **depois do echo da Coluna** (antes do separador Geopolítica). Deploy nos 2 servidores (backups `.bak_pre_banner_mobile_20260814`); purge completo (wp-rocket + cache/busting + wp cache flush). Prova em viewport 375px: 1 anúncio (954) antes do Nacional (1229); colunistas-mobile isolado a 4516 antes de Geopolítica (4791); after-latest 12986 / after-recents 14780 abraçando o Recentes. Mobile limpo ✓.

## Rodada 6 (14/08 ~19:15 BRT) — nova ordem + lição de auditoria

**Ordem Miguel:** Nacional → **Geopolítica → Economia → Coluna do Editor → Regional** → Tecnologia... (Geo/Eco sobem, Regional recua 1 casa). Regra reforçada: **máx 1 anúncio entre blocos, NUNCA dois seguidos, vale mobile/desktop/iPad.**

**Bug pego e corrigido:** a 1ª cirurgia NÃO removeu o bloco Geopolítica original → **geo duplicado** (aparecia 2×). A prova python deduplicava marcadores (`if marc not in ordem`) e ESCONDEU o bug — a auditoria do HTML servido (com `collections.Counter`) pegou. **LIÇÃO: prova de reordenação NUNCA deduplica; usar Counter e checar duplicatas explicitamente.** Fix: remoção do 2º geo nos 2 servidores (backups já existiam; deploy `fp5/fp5e`).

**Auditoria final 3 viewports (browser real):** TODOS ✓ sem empilhamento — cada anúncio tem conteúdo entre si e o anterior: top → [MANCHETE] → after-manchete → [Nacional,Geo,Economia,COLUNA] → after-colunistas → [Regional...Esporte] → after-latest → [Recentes] → after-recents → [Top10, LT] → Histórico. Pares D+M adjacentes são alternativos (1 por dispositivo). Sticky do rodapé é fixed (fora do fluxo). Falso positivo clássico: anúncios "vizinhos no DOM" separados pelo hero (top@105 vs after-manchete@944) — sempre medir POSIÇÃO renderizada, não só ordem DOM.
