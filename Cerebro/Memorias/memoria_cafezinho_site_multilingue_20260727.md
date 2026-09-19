# 🌐 Memória Técnica — Cafezinho Multilíngue: estudo de viabilidade da versão em inglês

**Data:** 2026-07-27 · **Autor:** ZCode/Kimi · **Fórum pareado:** `Foruns/forum_cafezinho_site_multilingue_20260727.md` · **Status:** pesquisa concluída, aguardando decisão de Miguel

## 1. Perguntas de Miguel e respostas técnicas

### 1.1 "O que é hreflang?"

Etiqueta (`<link rel="alternate" hreflang="CODIGO" href="URL">` no `<head>`, ou header HTTP, ou sitemap XML) que declara ao Google as versões alternativas de uma página por idioma/região. Efeito: o Google **exibe** a versão adequada no resultado de busca (usuário EN vê `/en/...`, usuário PT vê a original).

Regras oficiais (doc "localized-versions", verificada 27/07):
- **Self-referencing:** cada versão lista a si mesma + todas as outras.
- **Bidirecional:** se A não aponta para B e B não aponta para A, as tags são **ignoradas**.
- **`x-default`:** versão coringa para usuários cujo idioma não bate com nenhuma versão (recomendado = página PT original, no nosso caso).
- Códigos: ISO 639-1 (idioma) + opcional ISO 3166-1 Alpha 2 (região): `pt-BR`, `en`, `en-US`, `es`. Código de país sozinho é inválido. `es-419` não é suportado. `EU`/`UN`/`UK` ignorados.
- URLs totalmente qualificadas; podem estar em domínios diferentes.
- **3 métodos equivalentes — escolher UM** (usar os 3 dificulta manutenção sem benefício).
- Versões localizadas só contam como duplicata se o conteúdo principal permanecer sem traduzir.
- Ferramentas de validação citadas pelo próprio Google: gerador da Aleyda Solis; testador Merkle SEO.

**Fato importante:** o Google **não usa** hreflang nem `<html lang>` para **detectar** idioma — a detecção é por algoritmo sobre o conteúdo visível. hreflang afeta *serving* (qual versão aparece), não *indexing*.

### 1.2 "Redirect por IP para quem acessa do exterior — vale a pena?"

**Não, na forma de redirecionamento forçado.** Posição oficial verificada (doc "managing-multi-regional-sites" e "locale-adaptive-pages"):

- *"Don't use IP analysis to adapt your content"* — geolocalização por IP é "difficult and generally not reliable".
- O **Googlebot rastreia majoritariamente de IPs dos EUA** e **sem header `Accept-Language`**. O Google não varia a localização do rastreamento.
- Redirect automático "could prevent users (and search engines) from viewing all the versions of your site" — ou seja: **o bot seria sempre empurrado para o inglês e a versão PT (nosso negócio central) arriscaria perder indexação/cobertura**.
- Páginas locale-adaptive: o Google "might not crawl, index, or rank all your content for different locales".

**Solução oficial:** URLs separadas por idioma + hreflang + **links/banner de troca de idioma** (o usuário escolhe). Banner com sugestão ("View this article in English") sem redirecionar é o padrão seguro — usado por grandes portais.

### 1.3 "O indexador muda quando o texto é em outra língua?"

**Não muda.** Análise sobre nossa stack (`CEREBRO_NODE_SEO_OBSERVATORY.md` §6):

- **Indexing API** (`indexador_google.py`, service account `indexing-cafezinho@...`): a API é **cega a idioma** — recebe URL e notifica (`URL_UPDATED`/`URL_DELETED`). Bastaria enviar as URLs `/en/` novas, mesma lógica, mesma fila. Nenhuma alteração de código por causa de idioma.
- **Search Console:** propriedade `sc-domain:ocafezinho.com` **já cobre todos os subdiretórios e subdomínios** — `/en/` apareceria nos relatórios sem nenhuma configuração nova. Não existe "criar um indexador novo"; no máximo, filtros/segmentos novos no SEO Observatory para separar métricas PT vs EN.
- **Ressalva conhecida:** a Indexing API é oficialmente escopada para `JobPosting` e `BroadcastEvent` (livestream) — uso para notícias é off-label (prática comum de SEO; já é nosso uso atual). Cota padrão: 200 envios/dia. Doc não menciona idioma em nenhum ponto.
- **Detecção de idioma:** automática pelo conteúdo visível (ver §1.1). O que precisa existir de novo: (a) estrutura de URL `/en/`; (b) hreflang bidirecional; (c) um idioma por página (não misturar PT/EN na mesma URL).

### 1.4 "O que o Google diz sobre traduzir conteúdo em escala?"

Spam policies (verificada 27/07) — **"scaled content abuse"**: criar muitas páginas com objetivo primário de manipular ranking, tipicamente conteúdo não-original e sem valor, *independentemente do método* (IA, automação ou humano). Tradução aparece na política como exemplo de **transformação automatizada aplicada a conteúdo raspado de terceiros** (sinonimizar/traduzir/ofuscar feed alheio).

**Leitura para o nosso caso:** nosso conteúdo é **original e próprio**; traduzi-lo com qualidade agrega valor (acesso a outro público) e não é obfuscação de plágio. O risco real seria tradução automática **sem nenhuma revisão**, em volume industrial, com erros — o gate de qualidade do pipeline (Kimi 3 / validador §AUTH-060) é a mitigação natural. Não há proibição a conteúdo gerado/traduzido por IA em si.

## 2. Estrutura de URL — opções oficiais e recomendação

| Opção | Exemplo | Google diz | Para nós |
|---|---|---|---|
| ccTLD/domínio novo | `ocafezinho.com.br`+`.com`... / `cafezinho.news` | válido, geolocalização clara | ❌ autoridade zero, custo de domínio/infra |
| Subdomínio | `en.ocafezinho.com` | válido, fácil separação | ⚠️ ok, mas separa métricas e dilui manutenção |
| **Subdiretório** | `ocafezinho.com/en/` | válido, "fácil de configurar, baixa manutenção" | ✅ **recomendado** — herda autoridade do domínio, mesmo host, mesmo WP |
| Parâmetro | `?lang=en` | **"Not recommended"** | ❌ |

Observação: o espelho `cafezinho.news` (lab visual, droplet 159.65.177.60) pode servir de **homologação** da versão EN antes do canônico — mesmo fluxo espelho→homologação→canônico da reforma visual.

## 3. Implementação técnica — caminhos (a decidir)

**Opção A — mu-plugin próprio (padrão da casa):** pipeline cria o post EN via REST API (mesmo fluxo `publicar_cafezinho_wp.py`, status `draft`, imagem destacada §86), vincula PT↔EN por meta field (`_translation_of`), mu-plugin injeta hreflang no `<head>` + template EN + banner de idioma. 100% aditivo, rollback = apagar arquivos (mesmo protocolo da reforma visual). Sem dependência de plugin pago.

**Opção B — plugin (WPML pago / Polylang):** gestão madura de traduções, hreflang automático, seletor de idioma pronto. Contras: custo, peso no front (atenção: CLS/PSI já são ponto fraco — SEO node §11), mais uma superfície de atualização.

**Parecer preliminar:** Opção A, alinhada ao padrão mu-plugin aditivo já aprovado por Miguel na reforma visual.

## 4. Medição (SEO Observatory — já existente, zero custo novo)

- Crawler/Analisador/Otimizador (`cron_seo_crawler.py`, `seo_analyzer.py`, `agente_optimizador_seo.py`) já ingerem Search Analytics **sem filtro de URLs** (correção 05/06) — queries EN entrariam automaticamente.
- Adicionar segmento/categoria `en` em `urls_monitoramento` e comparar: impressões, cliques, CTR, posição, queries EN vs PT; Discover separado por idioma.
- Janela sugerida: 60–90 dias (Search Analytics tem delay de 2–3 dias; maturação SEO típica 4–12 semanas).
- CrUX de URLs novas: normal vir sem dados (SEO node §11).

## 5. Custos estimados (ordem de grandeza)

Tradução de matéria (~2–4k tokens in + 2–4k out): frações de centavo em modelos baratos (DeepSeek/Flash) a poucos centavos em premium; gate de qualidade adiciona custo similar. **Total por matéria: < US$ 0,01–0,05.** A 10 matérias/dia: ≤ US$ 15/mês no cenário caro — abaixo do limiar de alerta diário (US$ 15/dia, auditoria financeira). Catálogo de modelos: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`.

## 6. Casos reais de expansão linguística de notícias

Verificação ao vivo parcialmente bloqueada (captcha em buscadores) — itens marcados ⚠️ vêm de conhecimento de treinamento, tratar como leads:

| Caso | Ano | Desfecho | Fonte |
|---|---|---|---|
| El País Brasil (ES→PT) ⚠️ | 2013–2017 | **Fechado** — inviável economicamente, demissões | Knight Center/cobertura BR da época |
| HuffPost Intl (~15 edições, incl. Brasil) ⚠️ | 2011– | maioria **fechada/vendida** | Digiday/Nieman Lab |
| BuzzFeed Intl (BR, MX, DE...) ⚠️ | — | operações **fechadas** | imprensa especializada |
| Le Monde in English (FR→EN) ⚠️ | 2022– | ativo; assinantes internacionais ↑ (fonte: o próprio grupo) | comunicados Le Monde |
| El País English (ES→EN) ⚠️ | 2023– | ativo; sem números auditados encontrados | cobertura de mídia |
| The Local (Europa, 8-9 idiomas) ⚠️ | — | caso de sucesso relativo, multilíngue desde a origem | Journalism.co.uk |

**Leitura cética:** (1) o padrão de fracasso é de quem montou **redação paga** no idioma novo — custo fixo insustentável; nossa estrutura (tradução LLM sobre conteúdo já produzido) tem custo marginal ~zero, a equação é outra. (2) "Cases de sucesso" com números na web vêm majoritariamente de vendors de tradução (Weglot/WPML/Smartling) — evidência enviesada. (3) Viés de sobrevivência: fracassos viram notícia, sucessos modestos não. Fontes para verificação manual futura: niemanlab.org, journalism.co.uk, wan-ifra.org, INMA/Twipe.

## 7. Matriz de riscos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Redirect por IP quebrar indexação PT | alta (se implementado) | **crítico** | **não fazer redirect**; banner + hreflang |
| Tradução robótica/sem revisão → risco scaled content + dano à marca | média | alto | gate de qualidade (Kimi 3/validador); só 3 editorias |
| Cannibalização PT×EN | **baixa** (idiomas = mercados separados; hreflang resolve serving) | baixo | hreflang bidirecional + x-default |
| Diluir foco da equipe em sprint cheio (reforma visual, vídeo diário, V4) | média | médio | piloto pequeno, tudo automatizado, sem nova infra |
| Tráfico EN não materializar (nicho política-BR em EN é pequeno; Discover EN muito competitivo) | média | baixo (custo ~zero) | janela 60–90 dias com go/no-go por dado |
| Peso técnico (plugin/CLS) | baixa (se mu-plugin) | baixo | Opção A aditiva; rollback = apagar arquivos |

## 8. Sinergias registradas (27/07)

- **Editora Multilíngue** (`memoria_plano_editora_multilingue_20260727.md`): livros em PT/EN/ES/FR/中文/RU via Moka + Amazon KDP + editora chinesa. Site EN = canal de descoberta para os livros EN (SINGULARIDADE em 1º).
- **V4 ciência bilíngue** (ATUALIZAÇÕES 27/07 13:30): pipeline NYC já ingere pautas EN de ciência com listas simétricas — o fluxo já "fala inglês" na origem.
- **Espelho cafezinho.news**: laboratório natural de homologação da versão EN.

## 9. Protocolo de verificação desta pesquisa

- Verificado ao vivo nesta sessão (docs oficiais): localized-versions (hreflang), managing-multi-regional-sites, locale-adaptive-pages, spam-policies (scaled content abuse), indexing-api quickstart. 2 agentes de pesquisa web (casos + discussões SEO): buscadores com captcha; docs oficiais re-verificados pelo agente; casos de mercado marcados ⚠️.
- Pendente de verificação manual futura: falas individuais de John Mueller sobre redirect/idioma; números auditados das edições EN do Le Monde/El País; relatos r/SEO pós-mar/2024.

---

## 10. Dossiê de evidências verificadas (27/07 ~16h45 BRT — resposta ao "não inspirou confiança")

Tudo abaixo foi verificado **diretamente** (código, HTML ao vivo, banco de dados, API do Google), não pesquisado de segunda mão.

### 10.1 Indexador — prova de código

`Global South News/root/indexador_google.py`, função `notificar_google(url, action)`: recebe apenas URL + ação (`URL_UPDATED`/`URL_DELETED`). **Zero referências a idioma em todo o arquivo.** Já é multi-domínio por desenho: resolve a chave por domínio (`indexing_key_{dominio}.json`) com fallback para `indexing_key.json`. **Conclusão verificada: indexar conteúdo em inglês não exige nenhuma mudança no indexador.**

### 10.2 Site ao vivo — prova de HTML (curl 27/07)

- `<html lang="pt-br">`; **zero ocorrências de hreflang**; `max-image-preview:large` presente (confirma nodo SEO §4).
- Campo verde: nenhuma infra multilíngue pré-existente no Cafezinho.

### 10.3 Demanda real — prova de banco de dados (Tencent, `seo_performance.db`)

32.827 keywords, 15.341 cliques, período **2026-06-01 → 2026-06-16**:
- Top 15 queries: 100% PT/temas BR ("o cafezinho" 2.021 cliques, russia 804, flávio bolsonaro 601, vorcaro 576, irã 552, ucrânia 446...).
- Queries em inglês: ~2 cliques no período inteiro ("ai news" 1, "the intercept" 1).
- **Conclusão: a demanda internacional atual do Cafezinho é ≈ zero. Público EN teria que ser construído do zero, não "capturado".**

### 10.4 GSN — o braço inglês que JÁ EXISTE (descoberta central)

- **Site ao vivo:** `https://www.globalsouth.news` — `<html lang="en">`, matérias datadas de **27/07 (hoje)**: Mali, Guatemala, BRICS/dedolarização, Kimi K3 × dominância IA. Repo `migueldorosario1/global-south-news` com push em 24/07. Pipeline Astro/Markdown → GitHub → Vercel, agentes geram conteúdo próprio (não traduz Cafezinho).
- ⚠️ `globalsouthnews.com` (**.com**) redireciona para site estranho alheio (`actionla.org`) — o .com não é nosso ou foi perdido; canônico é **.news**. Vazamento de marca, não canibalização.
- Implicação estratégica: o experimento "conteúdo do ecossistema em inglês" **já está rodando**. O tráfego do GSN (Search Console próprio) é o piloto natural que já existe — medir antes de criar estrutura nova.

### 10.5 Separação de contas Google — memória de Miguel CONFIRMADA em 3 níveis

Miguel lembrava: "fiz outra conta para os temáticos, fiz tudo à parte". Verificado em `/root/agent_data/indexing_keys/` (NYC) + API Search Console:

| Portal | Projeto Google Cloud | Search Console (via API, read-only) |
|---|---|---|
| Cafezinho | gen-lang-client-0200069757 | `ocafezinho.com` + `sc-domain:ocafezinho.com` (owner) |
| GSN | indexing-gsn | `sc-domain:globalsouth.news` (owner) — **só isso** |
| Mundo Trilhos | indexing-mundotrilhos | `sc-domain:mundotrilhos.com` (owner) — **só isso** |
| Ceará / DiscoverBrazil / RioCarta / Aiatolah / MapaRio | projetos próprios (indexing-ceara, indexing-discoverbrazil, indexing-riocarta, indexing-aiatolah, indexing-mapario) | — |

**Cada portal = projeto Google próprio + service account própria + propriedade Search Console própria.** Resíduos inofensivos: conta Cafezinho lista `mundotrilhos.com` como não-verificado (histórico); silo local do GSN ainda tem a chave compartilhada antiga como `indexing_key.json` (se rodar local, indexaria GSN pela conta Cafezinho — corrigir copiando `gsn.json`).

### 10.6 Canibalização GSN × Cafezinho e conflitos entre temáticos — veredito

**Não existe canibalização hoje.** Canibalização exige mesma língua + mesma intenção de busca; o portfólio é separado por desenho em língua × tema:

| Portal | Língua | Território | Sobreposição com Cafezinho |
|---|---|---|---|
| Cafezinho | PT | política nacional BR | — |
| GSN | EN | geopolítica Sul Global/BRICS | **zero** (língua e tema) |
| Mundo Trilhos | PT | ferroviário | zero (tema) |
| Rail Post | EN | ferroviário internacional | zero |
| Discover Brazil | EN | turismo/cultura BR | zero |
| Ceará Digital | PT | notícias do Ceará | marginal (escopo estadual; "ceara news" = 0 cliques reais no Cafezinho) |

**⚠️ Risco INVERSO identificado:** se o Cafezinho-EN publicar **geopolítica em inglês**, criaria sobreposição real com o GSN (mesma língua, mesmo tema, contas separadas competindo) — ou seja, a versão EN pode **criar** a canibalização que hoje não existe. Divisão editorial limpa sugerida: **GSN = o mundo visto do Sul (já existe); Cafezinho-EN = o Brasil explicado ao mundo** (política BR e ciência para leitor internacional). Geopolítica EN → reforçar o GSN, não duplicar.

### 10.7 ⚠️ SEO Observatory MORTO há 39 dias (achado operacional grave)

- `seo_crawler.log` no Tencent: última execução com sucesso **2026-06-18 03:02** ("🏁 CONCLUÍDO COM SUCESSO", 2.827 keywords ingeridas).
- Banco parou em 16/jun; **cron de SEO ausente** no crontab root do Tencent; `/root/seo_performance.db` no NYC é stub de **0 bytes** (17/jun); sqlite3 nem instalado no NYC.
- Provável órfão da migração "tudo para NYC" (Miguel, 27/07). **Impacto direto neste tema:** o sistema que mediria o piloto EN está desligado. Registrado em `CEREBRO_NODE_BUGS_ATIVOS.md`.

### 10.8 Quotes verbatim (copiados via curl das docs oficiais, 27/07)

Redirect/geolocalização (managing-multi-regional-sites):
- *"Don't use IP analysis to adapt your content."*
- *"Avoid automatically redirecting users from one language version of a site to a different language version of a site."*
- *"These redirections could prevent users (and search engines) from viewing all the versions of your site."*
- *"This is because the Googlebot crawler usually originates from the USA."*
- *"IP location analysis is difficult and generally not reliable."*

Spam policies (scaled content abuse):
- *"Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings and not helping users... large amounts of unoriginal content that provides little to no value to users, no matter how it's created."*
- Exemplo citado: *"Scraping feeds, search results, or other content to generate many pages (including through automated transformations like synonymizing, translating, or other obfuscation techniques)"* — tradução como obfuscação de conteúdo **alheio**; nosso caso (traduzir o **próprio** conteúdo) está fora desta definição.
