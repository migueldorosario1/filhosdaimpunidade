# CEREBRO_INDEX_SATELITES

> [!IMPORTANT]
> **OVERRIDE CANÔNICO DE 11/08/2026 (atualizado 17/08/2026):** a lista viva tem nove sites, conforme `root/ferramentas/sentinela_tematicos/site_registry.json`. Os oito temáticos V4 ficam em `Projeto Cafezinho Agentes/sites-v4/`; a **Revista Maquiavel** (adicionada 17/08/2026) mantém repo próprio em `Revista Maquiavel/maquiavel` (revista ensaística, não orquestrada pelo V4). Caminhos e estados iniciais de maio abaixo são história do projeto, não autoridade de produção; ver `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`.

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


Índice mestre dos portais satélites do ecossistema Miguel/Cafezinho.

Atualização inicial: 2026-05-16 21:55 BRT.

## Princípio central

Os satélites são laboratórios autônomos inspirados no Rio Carta, não extensões técnicas do Cafezinho.

Regra absoluta:

- **Cafezinho intocável.**
- Não importar, copiar ou acoplar `motor_publicador.py`.
- Não editar scripts vivos de produção do Cafezinho para atender satélites.
- Usar Rio Carta apenas como laboratório conceitual: Markdown, GitHub, Vercel, logs, filtros de imagem, autocura e disciplina de rollback.

## Portais atuais

### Mundo Trilhos

- Domínio: `https://mundotrilhos.com` / `https://www.mundotrilhos.com`
- Repositório local: `Projeto Cafezinho Agentes/mundo_trilhos`
- GitHub: `git@github.com:migueldorosario1/mundo-trilhos.git`
- Título Astro: `Mundo Trilhos`
- Descrição: `Notícias Ferroviárias`
- Função: portal ferroviário em português, com foco Brasil/América Latina e infraestrutura ferroviária.
- Estado local/Git: frontend Astro publicado na Vercel; fake posts ainda presentes; `noindex,nofollow` ativo no `BaseHead.astro`.
- Estado público em 2026-05-16 22:22 BRT: **corrigido**. `mundotrilhos.com` e `www.mundotrilhos.com` servem `Mundo Trilhos`, descrição `Notícias Ferroviárias`, `og:url https://mundotrilhos.com/` e `robots=noindex,nofollow`.
- Últimos commits relevantes:
  - `982f5c1` hardening `.gitignore`;
  - `7e5a280` meta `noindex` pre-launch.

### Rail Post

- Domínio: `https://railpost.news` / `https://www.railpost.news`
- Repositório local: `Projeto Cafezinho Agentes/rail_post`
- GitHub: `git@github.com:migueldorosario1/rail-post.git`
- Título Astro: `The Rail Post`
- Descrição: `International Railway News Portal`
- Função: portal ferroviário internacional em inglês, gêmeo editorial do Mundo Trilhos.
- Estado local/Git: frontend Astro publicado na Vercel; fake posts ainda presentes; `noindex,nofollow` ativo no `BaseHead.astro`.
- Estado público em 2026-05-16 22:22 BRT: **corrigido**. `railpost.news` e `www.railpost.news` servem `The Rail Post`, descrição `International Railway News Portal`, `og:url https://railpost.news/` e `robots=noindex,nofollow`.
- Últimos commits relevantes:
  - `b66d657` hardening `.gitignore`;
  - `419c84d` meta `noindex` pre-launch.

### Discover Brazil

- Domínio: `https://discoverbrazil.news` / `https://www.discoverbrazil.news`
- Repositório local: `Projeto Cafezinho Agentes/discover_brazil`
- GitHub: `git@github.com:migueldorosario1/discover-brazil.git`
- Título Astro: `Discover Brazil`
- Descrição: `The Ultimate Tourism Guide`
- Função: portal visual em inglês para turismo, cultura, geoturismo e regiões brasileiras.
- Estado: frontend Astro publicado na Vercel; fake posts ainda presentes; `noindex,nofollow` ativo no `BaseHead.astro`.
- Estado público em 2026-05-16 22:22 BRT: **corrigido**. `discoverbrazil.news` e `www.discoverbrazil.news` servem `Discover Brazil`, descrição `The Ultimate Tourism Guide`, `og:url https://discoverbrazil.news/` e `robots=noindex,nofollow`.
- Últimos commits relevantes:
  - `f07d894` hardening `.gitignore`;
  - `363f099` meta `noindex` pre-launch.

### Global South News

- Repositório local conhecido: `Projeto Cafezinho Agentes/global_south_news`
- Título Astro: `Global South News`
- Descrição: `The Voice of the Developing World`
- Estado: em arquitetura separada; domínio `globalsouth.news` ainda precisa validação DNS/roteamento antes de assumir produção.
- Função: portal internacional em inglês com foco Sul Global, BRICS, regiões, setores estratégicos e mapa de mídia.
- Fórum conceitual dedicado: `Foruns/forum_arquitetura_gsn_satelite_20260516.md`.
- Estado de arquitetura em 2026-05-16 22:45 BRT: Antigravity propôs taxonomia macro GSN e fonteamento inicial; aplicar em `Header.astro`/JSON do repo `global_south_news` depende de aprovação editorial do Miguel.

### Revista Maquiavel

- Domínio: `https://revistamaquiavel.vercel.app` (`/`, `/pt/`, `/es/`)
- Repositório local: `Revista Maquiavel/maquiavel`
- GitHub: `git@github.com:migueldorosario1/maquiavel.git` (branch `main`; webhook git→Vercel ativo)
- Título Astro: `Maquiavel`
- Descrição: revista internacional de ciência política, ensaística, trilíngue EN/PT/ES.
- Função: revista de ciência política jornalística + curadoria legal de artigos acadêmicos traduzidos + acervo de periódicos/repositórios/universidades + podcast de debates. Complementa o GSN (que veta política doméstica BR).
- Estado: site no ar (17/17 páginas 200); esqueleto Astro i18n + identidade visual Antigravity aplicados; ensaio fundador 3 línguas; acervo v1 (77 entradas). **Conteúdo além do fundador e agente curador em produção = pendência (ver plano).**
- Registro no Sentinela: adicionado ao `site_registry.json` em 17/08/2026 (cadência `semanal`, limiar 192h, métrica `git_commit`).
- Nodo dedicado: `CEREBRO_NODE_REVISTA_MAQUIAVEL.md` · Fórum fundador: `Foruns/forum_revista_maquiavel_20260730.md`

## Consenso da Trindade Chinesa

Consulta registrada em `Foruns/forum_arquitetura_taxonomia_satelites_20260516.md`.

- Qwen: aprova com ressalvas.
- Kimi: aprova Sprint 0, mas veta automação antes de análise de risco.
- DeepSeek: aprova com ressalvas e veto parcial ao timing da automação.

Consenso prático:

- avançar com Sprint 0 documental/estrutural;
- piloto inicial: Mundo Trilhos;
- sem publicação automática por enquanto;
- fechar taxonomia, metadados, mídia visual, créditos, licenças e riscos antes de backend;
- fazer ao menos dois ciclos manuais ou semi-manuais no Mundo Trilhos antes de automatizar publicação.

## Taxonomia v1 proposta

### Mundo Trilhos / Rail Post

Eixos:

- Modalidade: alta velocidade, carga, metrô/VLT, trem regional, trem turístico, ferrovia urbana.
- Infraestrutura: trilhos, estações, sinalização, eletrificação, manutenção, túneis, pontes.
- Economia: logística, exportações, indústria ferroviária, concessões, financiamento, integração portuária.
- Geografia: Brasil, América do Sul, Europa, Ásia, África, Oriente Médio, América do Norte.

Regra editorial:

- Mundo Trilhos deve priorizar Brasil e América Latina.
- Rail Post deve ter vocação global.
- Pautas estratégicas podem sair nos dois idiomas com interlink.

### Discover Brazil

Eixos:

- Regions: Amazon, Northeast, Southeast, South, Central-West.
- States/Cities: Rio de Janeiro, Bahia, Pernambuco, Amazonas, Pará, Minas Gerais, São Paulo, Paraná, Santa Catarina, Ceará.
- Experiences: beaches, historic towns, food, music, festivals, nature, city life, museums, nightlife.
- Travel Planning: hotels, resorts, rentals, routes, airports, safety, best season.
- Visual Stories: photo essays, short videos, maps, itineraries.

Regra editorial:

- Imagem não é enfeite: é parte central do produto.
- Cada post deve ter imagem forte, crédito, licença e alt text.
- Galeria, mapa ou vídeo entram conforme o tipo de pauta.

### Global South News

Eixos:

- Multipolar World: BRICS, SCO, ASEAN, CELAC, African Union, Belt and Road.
- Regions: Latin America, Africa, West Asia, South Asia, East Asia, Eurasia.
- Strategic Sectors: energy, food, infrastructure, technology, currencies, trade.
- Media Map: mídia africana, asiática, latino-americana, árabe, chinesa, russa, indiana.
- Country Hubs: Brazil, China, Russia, India, South Africa, Iran, Indonesia, Mexico, Egypt, Ethiopia.

Complemento Antigravity 2026-05-16:

- BRICS ampliado: Brazil, Russia, India, China, South Africa, Egypt, Ethiopia, Iran, UAE.
- Organizations: SCO, ASEAN, African Union, CELAC.
- Regions: Latin America & Caribbean, Africa, Asia & Pacific, Middle East / West Asia, Eurasia.
- Strategic Sectors: Energy & Commodities, Infrastructure & Logistics, Trade & Currencies, Technology & Innovation.
- Media Map: African Media, Asian Media, Latin American Media, Arab/Middle Eastern Media.
- Campo `source_name` deve ser obrigatório no GSN, porque o portal funcionará como curadoria/agregação de mídias do Sul Global.

Regra editorial:

- Não deve ser clone em inglês do Cafezinho.
- Pode aproveitar pauta e apuração, mas precisa de linguagem internacional, contexto para leitor estrangeiro e foco Sul Global.

## Frontmatter mínimo futuro

Proposta v0 para posts dos satélites:

```yaml
---
title: ""
slug: ""
lang: "pt-br"
categoria_macro: ""
tags: []
hero: ""
hero_credit: ""
hero_license: ""
hero_source_url: ""
alt: ""
interlink_url: ""
interlink_lang: ""
publishedAt: ""
draft: true
---
```

Campos de imagem são obrigatórios antes de publicação real:

- `hero`
- `hero_credit`
- `hero_license`
- `hero_source_url`
- `alt`

## Mídia visual

Hierarquia recomendada:

1. Acervo próprio aprovado.
2. Banco local herdado dos projetos antigos.
3. Wikimedia Commons com licença checada.
4. Bancos públicos oficiais: Embratur, Visit Brasil, ministérios, secretarias, agências públicas.
5. Press kits oficiais com licença compatível.
6. Imagem gerada por IA chinesa apenas como último fallback.

Regra anti-erro Rio Carta:

- Copiar, quando o backend nascer, um filtro anti-logo semelhante ao `util_hero_filter.py` do Rio Carta.
- Não importar diretamente de outro projeto; copiar/adaptar para manter isolamento.

## Acervo ferroviário encontrado

Acervo operacional:

- `Projeto Cafezinho Agentes/root/agent_data_trilhos/`
- Contém rascunhos JSON, imagens temporárias, curadoria, memória, diretrizes e logs.

Acervo antigo maior:

- `Outros/Agentes Labs/agent_data_trilhos/`
- Contém cerca de 34 rascunhos JSON e dezenas de imagens.
- Este é o melhor ponto de partida para o piloto Mundo Trilhos.

Regra:

- Antes de publicar, separar material bom, velho e lixo.
- Não despejar o acervo inteiro no site.
- Fazer dois ciclos manuais/semi-manuais de curadoria.

## SEO pre-launch

Enquanto houver fake posts/lorem ipsum:

- `BaseHead.astro` deve manter:

```html
<meta name="robots" content="noindex,nofollow" />
```

Remover apenas quando:

- fake posts forem removidos;
- houver posts reais suficientes;
- frontmatter visual estiver completo;
- Miguel/Trindade autorizarem abertura para indexação.

## SEO pós-launch (17/08/2026)

Sites ABERTOS para indexação (todos servem `index,follow`; o estado "noindex" que o GSC reporta é histórico do período pré-launch). Correções de indexação aplicadas nos 8 repos `sites-v4/` (ver `Foruns/forum_gsc_tematicos_indexacao_noindex_sitemap_20260817.md`):

- Sitemap filtrado (sem `/tags/`, `/teste*`, `/preview/`; riocarta também sem `/senadores/`/`/prefeituras/`);
- Tag pages com `noindex,follow` (páginas finas — não valem rastreio);
- riocarta: blog pré-renderizado (2.809 artigos estáticos no sitemap; antes 0 artigos e 1.043 rascunhos);
- Pendências: ceara.digital é SPA (artigos não são estáticos — prerender pendente) + redirects apex↔www em aiatolah/mapario/ceara.

## Próximos passos

Sprint 0 pendente:

1. Inventariar acervo ferroviário antigo e classificar em aproveitável / revisar / descartar.
2. Fazer dois posts manuais/semi-manuais no Mundo Trilhos, mantendo `noindex`.
3. Validar frontmatter real com imagem/crédito/licença/alt.
4. Só depois discutir publicador mínimo isolado.

Concluído em 2026-05-16:

- Roteamento/domínios Vercel corrigido para Rail Post, Mundo Trilhos e Discover Brazil.
- Taxonomia JSON v1 criada por portal.
- Schema v0 criado no Mundo Trilhos.
- `noindex,nofollow` ativo nos três enquanto houver fake posts.

## Fóruns relacionados

- `Foruns/forum_implantacao_sites_satelites_20260516.md`
- `Foruns/forum_arquitetura_taxonomia_satelites_20260516.md`
- `Foruns/forum_arquitetura_gsn_satelite_20260516.md`

## Global South News - Sprint 0 técnico aplicado em 2026-05-16

Repositório:

- `Projeto Cafezinho Agentes/global_south_news`
- GitHub: `migueldorosario1/global-south-news`

Commit:

- `c163a50 Prepare GSN satellite taxonomy and prelaunch SEO`

O que mudou:

- `astro.config.mjs` aponta para `https://globalsouth.news`.
- O `base` legado `/global_south_news` foi removido.
- `BaseHead.astro` mantém `noindex,nofollow` enquanto o site estiver em pre-launch.
- `content.config.ts` aceita campos editoriais, visuais e de fonte necessários para GSN.
- `taxonomy.json` recebeu BRICS ampliado, regiões do Sul Global, setores estratégicos, mapa de mídias e regras editoriais.
- `package.json` e `package-lock.json` foram renomeados para `global_south_news`.

Validação:

- JSON OK.
- Build Astro OK, 14 páginas.
- Domínios públicos OK:
  - `https://gsnews.vercel.app`
  - `https://globalsouth.news`
  - `https://www.globalsouth.news`
- Todos retornam `robots=noindex,nofollow` e `og:url=https://globalsouth.news/`.

Pendência:

- `npm install` apontou 1 vulnerabilidade alta no audit. Não corrigida nesta sprint para evitar alteração automática ampla.

Regra:

- GSN continua fechado para indexação pública até substituir posts falsos por acervo real com fonte, imagem, crédito, licença e categoria.

## Mundo Trilhos - 2 posts piloto publicados em 2026-05-16

Repositório:

- `Projeto Cafezinho Agentes/mundo_trilhos`
- GitHub: `migueldorosario1/mundo-trilhos`

Commit:

- `9f5f814 Publish Mundo Trilhos pilot posts`

Posts piloto:

- `https://www.mundotrilhos.com/blog/linha-17-ouro-plano-nacional-ferrovias/`
- `https://www.mundotrilhos.com/blog/vlt-brasilia-tecnologia-aps/`

Origem:

- Triagem do Claude no `forum_arquitetura_taxonomia_satelites_20260516.md`.
- Acervo usado: `Outros/Agentes Labs/agent_data_trilhos/`.

O que mudou:

- Dois textos reais foram adaptados para Markdown Astro.
- Imagens foram copiadas para `public/hero`.
- O post singular exibe categoria, descrição, imagem, crédito/licença, fonte principal e autor.
- `og:image` usa a imagem destacada real do post.
- Data do post em `pt-BR`.
- Tags normalizadas para slugs de menu.

Validação:

- Build Astro OK, 26 páginas.
- Domínio público OK nos dois posts.
- `noindex,nofollow` continua ativo por segurança de pre-launch.

Pendência:

- O repositório ainda contém 10 fake posts.
- Decidir se remove agora ou após mais uma rodada piloto.
- `npm install` apontou 1 vulnerabilidade alta no audit; não corrigida automaticamente.

Atualização em 2026-05-16 23:27 BRT:

- Fake posts removidos do Mundo Trilhos.
- Commit: `5d5dbac Remove Mundo Trilhos placeholder posts`.
- Build OK, 15 páginas.
- `fake-post-0` validado como 404 no domínio público.
- Home mostra posts reais.
- `noindex,nofollow` permanece ativo.

## Rail Post - 2 posts piloto publicados em 2026-05-16

Repositório:

- `Projeto Cafezinho Agentes/rail_post`
- GitHub: `migueldorosario1/rail-post`

Commit:

- `4a0e340 Publish Rail Post pilot articles`

Posts piloto:

- `https://www.railpost.news/blog/brazil-line-17-national-rail-plan/`
- `https://www.railpost.news/blog/brasilia-lrt-aps-technology/`

Origem:

- Versões internacionais dos 2 pilotos ferroviários usados no Mundo Trilhos.
- Base factual: acervo `Outros/Agentes Labs/agent_data_trilhos/`.

O que mudou:

- Dois textos em inglês foram publicados em Markdown Astro.
- Imagens foram copiadas para `public/hero`.
- O post singular exibe categoria, descrição, imagem, crédito/licença, fonte principal e autor.
- `og:image` usa a imagem destacada real do post.
- Fake posts foram removidos.

Validação:

- Build Astro OK, 15 páginas.
- Domínio público OK nos dois posts.
- `fake-post-0` validado como 404.
- `noindex,nofollow` continua ativo.

Pendência:

- `npm install` apontou 1 vulnerabilidade alta no audit; não corrigida automaticamente.

## Discover Brazil - sprint piloto em 2026-05-16

Repositório:

- `Projeto Cafezinho Agentes/discover_brazil`
- GitHub: `migueldorosario1/discover-brazil`

Commit:

- `c78ab0f Publish Discover Brazil pilot guides`

Posts criados:

- `/blog/rio-de-janeiro-first-time-guide/`
- `/blog/brazil-travel-planning-basics/`

O que mudou:

- Dois guias evergreen em inglês foram publicados no código.
- Imagens do acervo local foram copiadas para `public/hero`.
- Schema/layout foram alinhados ao padrão dos satélites com fonte, crédito/licença de imagem, categoria, autor, `alt` e `og:image` real.
- Fake posts foram removidos do código.

Validação local:

- Build Astro OK, 14 páginas.
- HTML local contém os posts novos, imagem e fonte principal.

Bloqueio público:

- Vercel/domínio ainda serve deploy antigo.
- `https://www.discoverbrazil.news/blog/rio-de-janeiro-first-time-guide/` retornou 404.
- `https://www.discoverbrazil.news/blog/fake-post-0/` ainda retornou 200.

Diagnóstico:

- GitHub está correto no commit `c78ab0f`.
- O problema provável está no deploy automático da Vercel ou no vínculo projeto/branch/domínio.

Pendência:

- Abrir Vercel de Discover Brazil e verificar último deploy/erro/projeto conectado.
- `npm install` apontou 1 vulnerabilidade alta no audit; não corrigida automaticamente.

Atualização em 2026-05-16 23:56 BRT:

- Discover Brazil publicou corretamente após atraso do deploy Vercel.
- `rio-de-janeiro-first-time-guide`: HTTP 200.
- `brazil-travel-planning-basics`: HTTP 200.
- `fake-post-0`: HTTP 404.
- Home mostra posts reais.
- `noindex,nofollow` permanece ativo.
- Bloqueio encerrado como atraso de deploy, não erro de código.

## Global South News - editoriais pre-launch em 2026-05-17

Repositório:

- `Projeto Cafezinho Agentes/global_south_news`
- GitHub: `migueldorosario1/global-south-news`

Commit:

- `4868fb8 Replace GSN placeholders with prelaunch editorials`

Posts:

- `https://www.globalsouth.news/blog/why-global-south-news/`
- `https://www.globalsouth.news/blog/how-we-cover-the-global-south/`

O que mudou:

- Dois editoriais institucionais foram publicados para substituir os fake posts.
- Fake posts removidos.
- Imagens do acervo local copiadas para `public/hero`.
- Layout de post singular passa a exibir fonte principal, categoria, autor e crédito/licença da imagem.
- `og:image` usa imagem real do post.

Validação:

- Build Astro OK, 11 páginas.
- Domínio público OK nos dois posts.
- `fake-post-0` validado como 404.
- Home mostra posts reais.
- `noindex,nofollow` permanece ativo.

Limite:

- Ainda não existe acervo jornalístico maduro para GSN.
- Os textos são institucionais/pre-launch, não notícias.
- Backend/publicador automático ainda não foi criado.

### Ceará Digital

- Domínio no ar: **`https://ceara.digital`** (verificado 2026-08-05 — o `cearadigital.news` previsto em 22/07 NÃO é o domínio real).
- Função: portal temático estadual de política/notícias do Ceará (linha progressista; foco Elmano/Camilo/Luizianne, fiscalização da oposição).
- Estado: **ATIVO** — pipeline V4 local (`agentes_tematicos/v4/`, cron `0 */8 * * * --site ceara` + gerais 3h/13h); ~60 posts desde 21/07; destaques da home por audiência GA4 desde 05/08.
- Repo: `git@github.com:migueldorosario1/ceara-v4.git` → deploy Vercel; path local `Projeto Cafezinho Agentes/sites-v4/ceara`. Repo antigo `cicero_remote/ceara-digital` (NYC) fora do ar, cron rodando à toa — pendente ordem de desligamento.
- Painel: Central dos Temáticos do CCTV V6 — **`http://43.156.151.165/v6/tematicos/ceara-digital`** (slug curto `ceara` dá "não encontrado"); GA4 property **546675232** já conectada ao painel.
- Agentes: V4 compartilhado (coletor/produtor/publicador universais + `config/ceara.json`).
- Registros 2026-08-05: `Foruns/forum_ceara_hero_quaest_flickr_20260805.md` + `Memorias/memoria_ceara_hero_quaest_flickr_20260805.md` (hero errada corrigida via Flickr; diretriz imagem-casada-com-texto; gap de lideranças cearenses no Banco de Mídia).

- **18/08/2026 (ZCode/DeepSeek):** temáticos V4: cadência reduzida a **1 post/dia** (ordem Miguel — configs `posts_por_rodada=1` nos 8 sites + cron local diário 13h + `CEARA_BATCH_SIZE=1` no NYC) + **gate de CONFIRMAÇÃO de imagem fail-close** antes de publicar (`publicador.py` + `nucleo_visao.confirmar_imagem`) — cobre acervo default, que antes não passava por juiz. Tema Duplo: `Foruns/forum_tematicos_1post_dia_confirmacao_imagem_20260818.md` + `Memorias/memoria_tematicos_1post_dia_confirmacao_imagem_20260818.md`.
