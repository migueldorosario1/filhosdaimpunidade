# Memória — Série soja: liberação edição IA + caixa HTML embutida + reescopo controle→www (10/09/2026)

**Sessão:** ZCode Dell (GLM-5.3) · 10/09/2026 ~20:0x→20:3x BRT · fórum irmão: `Foruns/forum_serie_soja_liberacao_edicao_ia_caixa_20260910.md`

## Log técnico completo

### 1. Diagnóstico

- Posts: 269789 (Parte 1) / 269790 (Parte 2) / 269791 (Parte 3), autor **5486** (`ocafezinho_2`, display "Miguel do Rosario", subscriber, conta de 2019), publicados 10/09 20:01:42/48/54.
- Erro do redator: REST PUT → 423 `editorial_post_intocavel` motivo `post_publicado_por_humano`.
- Causa: `wp-content/mu-plugins/cafezinho-protecao-editorial.php` (v1.0.0) lista autores automáticos = apenas `array(5470, 5786, 5787)`; 5486 fora → post tratado como humano → agentes bloqueados (REST + WP-CLI + meta + taxonomia + delete/trash).
- Mapeamento de contas (7 dias, wp db query + origem-post): 5470 Redator (215 pub) · 5780 redator2 = **Gabriel HUMANO** (não incluir!) · 2018 James2017 = **Miguel HUMANO** (não incluir!) · 5786/5787 agentes · 5801 cafezinhodsn1 agente (5 pub) · 5486 byline IA (6 pub) · 5795 zcode_miguel incerto (2 pub) · 5800/1257/5749/5735 humanos.
- "Gêmea" da ronda 17:34: rascunhos 269630/269633/269636 na conta 2018 = cópias do próprio Miguel no editor. Não tocados.

### 2. Cura do gate (v1.1.0)

- `cafezinho_protecao_editorial_autores_automaticos()` → `array( 5470, 5786, 5787, 5486, 5801 )` + docblock explicando quem NÃO incluir.
- Backup servidor: `cafezinho-protecao-editorial.php.bak_pre_byline5486_20260910` (na pasta mu-plugins, junto dos .bak antigos).
- `php -l` ok. Prova wp eval:
  - `motivo(269789)` = `` (vazio → agente PODE editar) ✅
  - `motivo(269767)` (2018) = `post_publicado_por_humano` ✅ protegido
  - `motivo(269759)` (5780/Gabriel) = `post_publicado_por_humano` ✅ protegido
  - `contexto_agente()` em WP-CLI sem override = true (edições seguintes rodaram no caminho de agente de verdade).
- Efeito colateral aceito: quem autenticar via REST como 5486/5801 passa a ser tratado como agente (5486 é subscriber, sem poder de escrita REST; 5801 já era agente no gate-dois-checks).
- REST do Redator (5470): `rest_pre_dispatch` bloqueia só quando motivo não-vazio → com 5486 registrada, PUT/POST nos posts da byline passam. Não testado com app-password do Redator (segredo no cofre, não exposto); prova equivalente = update WP-CLI sem override abaixo.

### 3. Caixa da série (layout) + vazamento controle

- Conteúdo antigo: `<!-- wp:group serie-soja-nav ... -->` com `wp:buttons` layout flex — tema NÃO carrega CSS de layout do bloco no público → 3 botões empilhados.
- **Achado crítico:** botões apontavam `https://controle.ocafezinho.com/?p=269789|90|91` e as 4 imagens de gráficos da Parte 1 também vinham de `controle.ocafezinho.com/wp-content/uploads/...` (padrão do incidente Vorcaro 07/09). Partes 2/3 só tinham os botões errados; imagens já www.
- Substituição: grupo → bloco `<!-- wp:html -->` com div bege `#f4ebdd`, radius 14px, flex row **wrap** (adaptação minha ao design do redator: no desktop linha única, no celular quebra em vez de estourar; redator tinha proposto nowrap), botões `#c8102e` (parte atual, "Você está na Parte N") e `#3d2b1f` ("Partiu Parte X"), permalinks www corretos das 3 partes.
- Script gerador: `/tmp/soja_fix/build_boxes.py` (regex do group bege, asserts: 1 substituição, 0 controle pós-reescopo, 1 "Você está na Parte N", 3 permalinks, 0 `serie-soja-nav`). ⚠️ heredoc derrubou acentos na 1ª geração ("Voce esta") — restaurados antes do upload; LIÇÃO: asserts de texto com acento ANTES de gravar/subir.
- Reescopo: `https://controle.ocafezinho.com/` → `https://www.ocafezinho.com/` (só nestes 3 posts; 4 imagens testadas 200 no www antes).
- Aplicação: `wp post update <id> /tmp/<id>_new.html` **sem override** — Success ×3 (prova da liberação). Post update não tocou status/date/author (readback: publish, 5486, modified 20:17:17/22/27).
- Armadilha evitada: NÃO usar search-replace global (string existe em centenas de posts antigos — lição Vorcaro).

### 4. Provas

- Banco: controle=0, voceesta=1, wwwlinks=3, caixavelha=0 em cada um dos 3.
- Cache: `rocket_clean_post` ×3 + `rocket_clean_domain()` + `wp_cache_flush()`.
- Ao vivo (?nocache): 3× HTTP 200, `display:flex;flex-direction:row` presente, "Você está na Parte 1/2/3" correto, 2× "Partiu Parte" por página, 0 `controle.ocafezinho.com` no HTML servido.
- QA visual: screenshot headless full-page 1280×12000 (`google-chrome --headless --screenshot`), análise de imagem confirmou caixa bege com 3 botões LADO A LADO e vermelho na Parte 1. Print 1º (2400px) não alcançou o fim da página — caixa fica no rodapé da matéria; usar janela ≥12000px.

### 5. Backups / rollback

- Conteúdo original dos 3: `Cerebro/Backups/posts_editados/{269789,269790,269791}_pre_serie_soja_box_20260910.md` (restaurar = `wp post update <id> <arquivo>`, com override se autor voltar a ser não-agente).
- Gate: `.bak_pre_byline5486_20260910` no servidor (rollback = cp de volta).
- Novos conteúdos: `/tmp/soja_fix/*_new.html` (efêmero).

### 6. Pendências

1. 5795 `zcode_miguel`: classificar agente×humano (2 posts publicados; se agente, adicionar à lista do gate).
2. Tema não carrega CSS de layout de blocos Gutenberg no público → séries futuras: caixa = bloco HTML com estilo embutido desde o rascunho (passar a receita ao redator).
3. Posts antigos da byline 5486 (267462/267463/268390) agora editáveis por IA — ciência do Miguel (era o pedido).
4. Varredura site-wide de `controle.ocafezinho.com` em conteúdo público segue como débito antigo (centenas de posts, decisão Vorcaro: fora de escopo naquele dia).


### 7. Adendo ~20:4x — autoria James2017 + allowlist v1.2.0

- Ordem: 3 posts p/ conta 2018. Miguel fez no editor (saves 20:38:03/08/12; _edit_lock user 2018 desde ~20:20). Meu wp-cli `--post_author=2018` bloqueado em `meta_wp_cli` (autor já era humano) — estado final correto sem intervenção.
- Gate v1.1.0 → v1.2.0: `cafezinho_protecao_editorial_liberados()` (269789/90/91, expira 2026-12-31, checada antes do teste de humano; bloqueios `ordens` mantêm prioridade). Backup `.bak_pre_liberados_20260910` no servidor. Prova wp eval: 3 IDs motivo vazio; 269767 (outro post do 2018) = `post_publicado_por_humano`.
- Live pós-purga: byline "Miguel do Rosário" ×3, james2017 ×4/página, caixa flex=1, controle=0.
- Rollback autor: `wp post update <id> --post_author=5486` (com override se preciso). Rollback gate: cp .bak_pre_liberados.
