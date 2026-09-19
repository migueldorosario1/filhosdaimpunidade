# Memória — Home Cafezinho ordem final + anúncios (14/08/2026) — log técnico

**Sessão ZCode GLM-5.2** (13:20–~14:25 BRT). Par do fórum: `Foruns/forum_home_cafezinho_ordem_final_anuncios_20260814.md`.

## Comandos e arquivos

- Canônico via `ssh cafezinho-wp` (190.89.239.65:51439), tema `/var/www/ocafezinho/wp-content/themes/ocafezinho-portal/front-page.php` (823→824 linhas). Edições locais em `/tmp/front-page_CANON.php`; deploy com `php -l` + `install -o www-data -g www-data -m 644` + `wp cache flush` + `rm -rf wp-content/cache/wp-rocket/`.
- Espelho via `ssh root@159.65.177.60`, tema `/var/www/cafezinho-news/wp-content/themes/ocafezinho-portal/front-page.php` (55024 bytes final).
- Backups: `front-page.php.bak_pre_ordem_final_20260814` (nos 2) + `/tmp/ad_inserter_bak_20260814.txt` (option Ad Inserter, nos 2).

## Técnica: mover blocos com python por âncoras

Recorte/insert por `idx('âncora')` com asserts (conteúdo do bloco, nº de `</section>`). **Lição:** conferir por diff DE LINHAS do bloco original vs movido — no 1º movimento a linha `banner-after-latest-desktop` sumiu silenciosamente (asserts não pegaram porque eram só de estrutura). Diff forense revelou e restaurou. NOVOS asserts padrão: grep final por TODOS os ids de banner esperados.

## Técnica: decodificar option do Ad Inserter

`ad_inserter` = `:AI:` + base64(serialize(array)). Parser PHP-serialize em python (bytes! contagem de bytes nas strings). Flags: `display_type` (16=depois elemento, 6=antes/depois parágrafo c/ `paragraph_number`, `detect_client_side`), `display_on_homepage` ausente = default (entrava na home). Edição via `wp eval` PHP: unserialize → set → serialize → update_option; validar lendo de volta. Espelho usa `--allow-root`.

## Descobertas

1. Ad Inserter 2.8.17 ativo nos 2; insere client-side (por isso anúncios não aparecem no HTML estático — só no DOM renderizado). Diagnóstico no browser via `playwright.evaluate` read-only (getBoundingClientRect dos `.ad-space`) — evaluate com outerHTML/closest é REJEITADO pelo IAB (side-effect); versão mínima passa.
2. Empilhamento dos prints (Peso Argentino+Burger King / aluguel+Jewel+FENAE após o Regional) = anúncio do Ad Inserter colado no banner fixo `banner-after-colunistas-desktop`. Resolvido com `display_on_homepage=0` em 85 (canônico) + 96 (espelho) blocos.
3. `cafezinho.com.br` = "Account Suspended" (hosting velho) — domínio vivo é `.com`. CF `cf-cache-status: DYNAMIC` mas houve janela ~5min servindo HTML antigo (transição dos prints do Miguel).
4. Painel Histórico (cz-hist, accordion ano/mês) vive no rodapé — já é o último elemento da home nos 2.
5. Espelho divergia do canônico em `category__not_in` (sem 20699) — mantida a divergível, só a ordem de blocos foi igualada.

## Provas finais

- curl ordem canônico: Nacional→…→Esporte→Recentes→Top10→LinhaDoTempo→footer→Histórico ✓; espelho idem ✓ (pós-deploy ~17:20).
- Browser desktop 1440px: 5 slots desktop preenchidos/ok, after-latest restaurado a 11121px (antes do Recentes), after-recents 11956 (depois), zero anúncio fora de slot.

## Estado / falta

- Tudo no ar; nada pendente de execução. Monitoramento: linha ✅ arquivada.

## Rodada 4: mu-plugin cafezinho-historico.js

- Painel `#cafezinho-historico` nasce no rodapé e o JS o move; alvo antigo = fim da section "Recentes" (por isso o toggle aparecia entre Recentes e Top10). Novo alvo = última `section.pb-5 .container-xxl` (Linha do Tempo). Heredoc python com aspas escapadas dentro de ssh quebra — editar local + scp + install é o caminho.
- Caches: `wp-content/cache/busting/` também precisa de purge junto com wp-rocket. `?ver=` vem de `filemtime` no loader php.

## Rodada 5 (14/08 ~16:10 BRT) — 2 anúncios empilhados no CELULAR antes do Nacional

Print/relato do Miguel no celular: dois blocos repetidos entre a manchete e o Nacional. Causa: `banner-after-manchete-mobile` e `banner-after-colunistas-mobile` estavam quase adjacentes no topo do front-page.php (a Coluna só é ecoada lá embaixo — no celular não havia conteúdo entre os dois slots). Fix: `banner-after-colunistas-mobile` movido para **depois do echo da Coluna** (antes do separador Geopolítica). Deploy nos 2 servidores (backups `.bak_pre_banner_mobile_20260814`); purge completo (wp-rocket + cache/busting + wp cache flush). Prova em viewport 375px: 1 anúncio (954) antes do Nacional (1229); colunistas-mobile isolado a 4516 antes de Geopolítica (4791); after-latest 12986 / after-recents 14780 abraçando o Recentes. Mobile limpo ✓.

## Rodada 6 (14/08 ~19:15 BRT) — nova ordem + lição de auditoria

**Ordem Miguel:** Nacional → **Geopolítica → Economia → Coluna do Editor → Regional** → Tecnologia... (Geo/Eco sobem, Regional recua 1 casa). Regra reforçada: **máx 1 anúncio entre blocos, NUNCA dois seguidos, vale mobile/desktop/iPad.**

**Bug pego e corrigido:** a 1ª cirurgia NÃO removeu o bloco Geopolítica original → **geo duplicado** (aparecia 2×). A prova python deduplicava marcadores (`if marc not in ordem`) e ESCONDEU o bug — a auditoria do HTML servido (com `collections.Counter`) pegou. **LIÇÃO: prova de reordenação NUNCA deduplica; usar Counter e checar duplicatas explicitamente.** Fix: remoção do 2º geo nos 2 servidores (backups já existiam; deploy `fp5/fp5e`).

**Auditoria final 3 viewports (browser real):** TODOS ✓ sem empilhamento — cada anúncio tem conteúdo entre si e o anterior: top → [MANCHETE] → after-manchete → [Nacional,Geo,Economia,COLUNA] → after-colunistas → [Regional...Esporte] → after-latest → [Recentes] → after-recents → [Top10, LT] → Histórico. Pares D+M adjacentes são alternativos (1 por dispositivo). Sticky do rodapé é fixed (fora do fluxo). Falso positivo clássico: anúncios "vizinhos no DOM" separados pelo hero (top@105 vs after-manchete@944) — sempre medir POSIÇÃO renderizada, não só ordem DOM.
