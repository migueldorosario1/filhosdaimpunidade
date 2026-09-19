# Memória técnica — Vazamento de scaffolding LLM (269519/267466/268459) + cura em 3 camadas

> 08/09/2026, ZCode (Qwen3.8-Max). Fórum irmão: `Foruns/forum_vazamento_scaffolding_269519_20260908.md`. Log técnico completo (comandos, provas, arquivos, rollback).

## 1. Cronologia executada (BRT)

- 21:2x — ordem do Miguel (fix urgente + investigação + cura estrutural; depois: "tira os travessões, proibidos no manual; estranho esse post").
- 21:2x — `wp post list --name=enquanto-lula…` → ID 269519, publish 21:16:39, autor 5780. Download do content cru (`wp post get 269519 --field=content`): markdown puro, 4618 bytes, blocos `## Bloco "Leia Mais"` (linha 17) e `## Opções alternativas de título` (linha 20, 5 títulos), 13 travessões totais (11 corpo + 2 no bloco vazado).
- 21:2x — monitor lido (Regra Nº2): nenhuma sessão paralela em WP/mu-plugins. Backup `Cerebro/Backups/posts_editados/269519_pre_fix_20260908.md`.
- 21:2x — 1ª tentativa `wp post update 269519 --post_content=@/tmp/…` → **BLOQUEADO** pelo mu-plugin `cafezinho-protecao-editorial` (`post_publicado_por_humano`, canal wp_cli, user_id 0) — 5780 fora da lista de automáticos {5470,5786,5787}.
- 21:2x — override justificado (ordem explícita): `sudo -u www-data env CAFEZINHO_EDITORIAL_HUMAN_OVERRIDE=1 wp … post update 269519 --post_content=@/tmp/…` → "Success" MAS **@file não é interpretado**: gravou a string literal "@/tmp/269519_content_corrigido.txt" (35 bytes). 🔴 ARMADILHA: update de conteúdo via arquivo = **argumento POSICIONAL** (`wp post update <id> /tmp/arquivo`), nunca `--post_content=@`.
- 21:2x — reaplicado posicional → 3803 bytes, diff = só linha em branco final. Purge: `rocket_clean_post(269519)` + `rocket_clean_domain()` + `wp_cache_flush()` + `redis-cli FLUSHALL`.
- 21:3x — verificação pública: URL com traços do pedido do Miguel = **404** («Página não encontrada»); `option get permalink_structure` = `/%year%/%monthnum%/%day%/%postname%/`; URL canônica `/2026/09/08/slug/` = **200**, auditoria python do HTML: corpo íntegro, 0 travessões, 0 `##`, 0 `**`, 0 resquício dos 5 títulos alternativos em toda a página.
- 21:4x — varredura SQL (3 queries, arquivo scp'd + `wp db query "$(cat …)"`): (a) scaffolding em qualquer post → 268459 (draft, 5735) + **267466 (PUBLISH 24/08)**; (b) travessões publish ≥01/09 → 58 posts (tabela §4); (c) histórico autor 5780 → 40 posts desde 01/09.
- 21:4x — 267466: `_cafezinho_origem` = via admin, user 5735, **Windows/Chrome**, 24/08 11:56. Backup `267466_pre_fix_20260908.md`. Truncamento python a partir de `<strong>Leia Mais:</strong>` (offset 4081 de 4831). Fix override posicional + purge → página pública 200, 0 vazamento, corpo presente. 9 travessões do corpo preservados (escopo: só vazamento).
- 21:5x — mu-plugin `cafezinho-filtro-scaffolding.php` instalado (php -l OK, owner/mode espelhados do `cafezinho-legenda-limpa.php` = www-data:www-data 664) + testes `wp eval-file /tmp/teste_scaf.php` **7/7 PASS**.
- 21:53 — sweeper `/root/verificador_vazamento.py` (755, py_compile OK) 1ª corrida manual: 41 vistos, 3 flags (267466 travessoes:9 · 269523 travessoes:8 · 269516 draft travessoes:2), `ok 269519`. Cron `*/15` instalado (marker VAZAMENTO_SWEEPER_20260908, flock /tmp/vazamento.lock).
- 21:5x — Ronda ZM Vigia (automation-94fb93f2) atualizada: passo **P2.6** consome `vazamento_flags.jsonl` (severidade 🔴 bloco/metatexto/markdown_cru vs 🟡 travessoes) + instruções de investigação se bloco_interno aparecer pós-cura.
- 21:5x — fact-check do conteúdo (Bing News RSS): Quaest/SP REAL, números 1:1 (Flávio 31, Lula 30, Cury 8, Caiado 4, Renan 2, Zema 1 — 08/09 13:36 GMT). URL-traços do bloco Leia Mais vazado (`/2026-08-30/soma-de-17…`) = 404; barras = 200 → LLM do Gabriel fabrica formato de URL. `wptelegram` message_template = `{post_title}\n\n{post_excerpt}\n\n{full_url}` (canônico — inocente).

## 2. Culpado e mecanismo (provas)

- **User 5735 `gabrielbarbosa` (Gabriel)** — mapas de autoria: Gabriel = 5780 (redator2, autoria) + 5735 (+5799 gabriel_redacao individual desde 24/08). `_edit_last=5735`, `_edit_lock=…:5735`, `_cafezinho_origem` via=admin UA Android (269519, ts 21:12:27, publish 21:16:39 — 4 min) e Windows (267466).
- Mecanismo: cola a resposta BRUTA do LLM pessoal (prompt dele exige «Bloco "Leia Mais"» + 5 «Opções alternativas de título» — template inexistente no ecossistema, grep 0 hits no Dell) sem revisar; no celular o editor não converte markdown → `##`/`**` literais na página.
- Nenhum gate cobre: publicação humana direta (§130/§132); R1/R2 crons :05/:20 não pegam janela de 4 min; guardião/R1 tratam 5780/5735 como humano (correto).
- Mesma família: 268459 (metatexto «Sem sobreposição direta… Segue a matéria» antes do título), caso 269169 06/09 (parecer como matéria).

## 3. Cura (arquivos e rollback)

| Camada | Arquivo | Rollback |
|---|---|---|
| 1. Filtro no save | `/var/www/ocafezinho/wp-content/mu-plugins/cafezinho-filtro-scaffolding.php` (cópia /tmp) | `rm` do arquivo |
| 2. Sweeper alerta | `/root/verificador_vazamento.py` + cron marker `VAZAMENTO_SWEEPER_20260908` | remover linha crontab + `rm` |
| 3. Ronda P2.6 | automation-94fb93f2 (prompt atualizado 08/09 21:5x) | CronUpdate removendo o P2.6 |

- Filtro: regexes de bloco (md: `^#{0,6} (**)?Bloco "Leia Mais"` variantes aspas retas/curvas; `^#{0,6} (**)?Opções alternativas de título`; `^(**)Leia Mais:(**)$`; html: `<strong>…</strong>` ± `<p>`) → corte do MENOR offset até o fim + fecha `</p>` órfão; metatexto = 1º parágrafo (html `<p>…</p>` ou texto até `\n\n`) casando lista conservadora E ≤500 chars E havendo corpo depois; markdown_cru = aviso (≥2 de: heading `^#`, `**bold**`, `[x](http`). Log: option `cafezinho_scaf_log` (array, teto 200, ts/post/user/achado). Notice via `redirect_post_location` + `admin_notices` (`?cafezinho_scaf=1`). Só post_type=post. Nunca toca status/date/autor.
- Sweeper: espelho do `verificador_datasemana.py` (mesmas funções log/wp/vistos); janela post_modified ≤3h; statuses publish,future,draft; anti-loop sha1_8 do content; flags jsonl append-only; MAX_POSTS 40; vistos teto 500.
- Testes do filtro (eval-file, sem criar post — publicador */15 poderia catar draft): md_269519 limpou ✓, html_267466 limpou ✓, metatexto_268459 limpou ✓ (título+corpo preservados), 2 controles NÃO mexidos ✓ (menção a "Leia Mais" no meio de frase não dispara), resíduos zero ✓.

## 4. Travessões sistêmicos (publish ≥01/09, varredura SQL 21:4x) — AGUARDA "VAI"

58 posts. Top por contagem: **269173=30** (5780), **269144=27** (5470), **268553=18** (5801), 268993=17 (5780), 269155=16 (5470), 269085=15 (5795), 268537=15 (5780), 268841=14 (5470), 268824=14 (5780), 268826=13 (5780), 269341=13 (5780), 268576=13 (5795), 269426=12 (5780), 269420=12 (5780), 268999=12 (5780), 268806=12 (5780), 268664=12 (5470), 268534=12 (5780), 268879=11 (5470), 268509=11 (5780), 268640=10 (5780), 268634=10 (5780), 268584=10 (5780), 268706=10 (5780), 268816=10 (5780), 268537=15, 269387=10 (5780), 269369=10 (5780), 269338=12 (5780)… (lista completa no stdout da varredura; reprodução: query `varredura_travessao.sql` = `SELECT ID, post_author, … (LENGTH(post_content)-LENGTH(REPLACE(post_content,'—','')))/3 AS n FROM wp_posts WHERE post_type='post' AND post_status='publish' AND post_date>='2026-09-01' AND post_content LIKE '%—%'`). Por autor: 5780 (Gabriel) = maioria esmagadora; 5470/5786/5801/5795 (robôs/agentes) = minoria significativa → travessão NÃO é só problema humano; R2/juiz2 também não estão barrando.
- Manual v2.1.1 (03/09), linhas ~143 e ~213: "Dois-pontos e travessão: com parcimônia… a régua é preferência, não proibição". Ordem do Miguel 08/09 21:3x: "estão PROIBIDOS no manual de estilo" → conflito a resolver (atualizar manual + regex do apêndice do verificador? — item 3 do fórum).
- 269519 corrigido = referência de método: travessão → vírgula (aposto) ou ponto (frase nova), NUNCA substituição cega.

## 5. Pendências / próximos donos

- Itens 1-6 do fórum §5 (todos aguardam "vai" do Miguel): retroativo travessões · 269523 · manual · recado ao Gabriel · fact-check humano · travessão em R2/juiz2 (NYC, §112).
- Ronda Vigia P2.6 vigia o filtro (flag bloco_interno pós-cura = investigar).
- Draft 268459 (Gabriel): não tocado; mu-plugin limpa no próximo save; se publicar sem salvar de novo → sweeper alerta.
