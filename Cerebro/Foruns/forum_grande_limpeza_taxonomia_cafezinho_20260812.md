# 🧹 GRANDE LIMPEZA DE TAXONOMIA — O Cafezinho (categorias + tags)

> **Fórum de PLANEJAMENTO** (Regra Nº 3 — missão em curso para continuar em outra conversa).
> **Data:** 12/08/2026 19:30 BRT · **Autor:** ZCode (GLM-5.2, fallback — Kimi/Qwen 🔴🔴)
> **Alvo:** WordPress **O Cafezinho canônico** (`ocafezinho.com`, SSH `cafezinho-wp`, `/var/www/ocafezinho`)
> **Ordem do Miguel (12/08 ~19:25):** *"Prepara aí uma grande limpeza de tags e categorias… deixa só as principais… tira categorias que são nomes de autores… espalha para as grandes categorias (política, regional, geografia, Rio, região sudeste)… cidade deixa como tag… categoria tem limite, faz as principais que têm mais assuntos… poucas categorias. **SÓ um plano agora**, pra executar ao longo da semana. Um rastreamento bem leve agora e prepara o plano."*
> **FASE ATUAL:** 📋 **PLANO PRONTO, AGUARDA MIGUEL VALIDAR O MODELO antes de executar.** Zero escrita no banco até aprovação.

> ## 🔄 MUDANÇA DE DIRETRIZ (12/08 23:07 — ordem Miguel)
> **NOVA ABORDAGEM:** *"não vamos apagar nenhuma categoria agora. Vamos organizar e, a partir de agora, apenas publicar em categorias específicas, poucas, organizadas. Estabelecer uma política para categorias."*
> - **Faxina do passado (Ondas 1–5 deste fórum) → PAUSADA.** A automação `automation-a7be3a1e-...` está com `STATUS: PAUSADO` em `faxina_taxonomia_PROGRESSO.md`. Reativável.
> - **Foco novo → POLÍTICA DE CATEGORIAS** (disciplinar publicação futura via whitelist + mu-plugin). Documento: **`Foruns/forum_politica_categorias_cafezinho_20260812.md`**.
> - Este fórum permanece válido como **diagnóstico + análise SEO + plano de referência** para o dia em que o Miguel quiser retomar a faxina do histórico (com redirects). Por ora, só a política de publicação nova avança.

---

## 1. Diagnóstico (rastreamento leve, só-leitura, 12/08 19:25–19:30)

### 1.1 Números gerais

| Métrica | Valor |
|---|---|
| Categorias (com ≥1 post) | **296** |
| Tags totais | **19.460** |
| Tags órfãs (count=0) — lixo puro | 969 |
| Tags com só 1 post (singletons) | **12.845** ⚠️ |
| Tags com 2–5 posts | 4.140 |
| Tags com 6–50 posts | 1.346 |
| Tags com >50 posts (as "úteis") | 193 |
| Tags com `#` no nome | 59 (ex.: `#ChinaEUA` = 289 posts) |

**Leitura:** a dispersão de tags é extrema — **66% das tags (12.845) têm um único post**. É o problema clássico de tag virando "palavra-quebra-no-título". Categorias sofrem do oposto: 296 é demais, com muita redundância e ~45 categorias que na verdade são **nomes de colunistas**.

### 1.2 As 4 famílias de problema nas CATEGORIAS

**Família A — Nomes de autores/colunistas como categoria (~45 categorias):** o Miguel quer tirar. As maiores:

| Categoria (term_id) | Posts | Categoria (term_id) | Posts |
|---|---|---|---|
| Rhyan de Meira (4949) | 4.211 | Wellington Calasans (1713) | 164 |
| Clarice Candido (4959) | 640 | Miguel do Rosário (1618) | 145 |
| Ruann de Lima (4950) | 538 | Raphael Lacerda (4965) | 143 |
| Letícia Souza (4958) | 464 | Augusto Werneck (4966) | 58 |
| Cleber Lourenço Original (4944) | 453 | Eder Casagrande (1653) | 57 |
| Gabriel Barbosa (4942) | 445 | Jeferson Miola (2886) | 52 |
| Pedro Breier (1697) | 392 | Theo Rodrigues (1342) | 50 |
| Maria Clara (4952) | 333 | Mariana T Noviello (1619) | 48 |
| Ana Prestes (2978) | 256 | Denise Assis (2398) | 40 |
| Patrick Chaie (4951) | 231 | Bruno Falci (2834) | 39 |
| Tadeu Porto (1434) | 197 | (+ ~25 outras, 1–23 posts cada) | — |
| Charles Nisz (4946) | 190 | **TOTAL autores** | **~13.500 posts** |
| Bajonas Teixeira (1620) | 185 | | |
| Luis Edmundo Araujo (1555) | 169 | | |
| Tulio Ribeiro (2469) | 168 | | |

**Família B — Geografia bagunçada:** mistura região/estado/cidade/país como categoria, sem hierarquia clara.
- **Regiões:** Sul (21071)=200, Nordeste (4984)=19, Sudeste (21070)=9, Norte (21068)=2, Centro-Oeste (21069)=0 — **5 regiões existem mas quase vazias**
- **Estados "vivos":** Ceará 274, São Paulo 302, Rio de Janeiro (1656) 455, Paraná 200, Rio Grande do Sul 28, Minas Gerais 23, Bahia 23, Paraíba 5
- **Estados recém-criados com 0 posts** (do plano do menu hambúrguer): Acre, Alagoas, Amapá, Amazonas, Espírito Santo, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Pará, Pernambuco, Piauí, Rio Grande do Norte, Rondônia, Roraima, Santa Catarina, Sergipe, Tocantins — **falta DF**
- **Cidades como categoria (devem virar TAG):** Niterói (4969) 27, São Paulo capital (5001) 222, Rio de Janeiro Capital (5002) 178, Brasília (5710) 102, Belo Horizonte 2, Nova Friburgo 1, Baixada Fluminense 2
- **Países/regiões como categoria** (devem virar tag — já existem as tags): China 1.839, EUA 1.722, Oriente Médio 780, Rússia 309, Argentina 171, Europa 158, Brics 156, África 34

**Família C — Redundância/duplicação temática (consolidar):**
- Guerra (5062) 2.032 → Geopolítica
- Golpe (1308) 1.795 + Metagolpe + Fascismo (1422) 126 + Ditadura 28 → Política
- STF (1100) 886 + Senado 317 + Congresso 316 + Câmara 54 + Governo Temer 343 + Governo Lula 330 + Governo Federal 54 → Política / subdividir por tag
- Corrupção 644 + Lava-Jato 268 → Justiça (ou Política)
- Petrobrás 451 + Petróleo 316 + BNDES 60 + Agro 123 + Indústria 127 + Mercado 30 → Economia (tag específica)
- "Eleições 2014/2016/2018/2020/2022/2024/2026" (8 categorias, ~2.500 posts) → tag única "Eleições" + categoria Política
- Ciência, Tecnologia & Soberania Digital + Ciência & Tecnologia (duplicadas) → Tecnologia
- Esporte (1271) 210 + Esportes (1426) 51 + Futebol 1 + Libertadores 1 → Esporte (singular)

**Família D — "Lixo" / catch-all / formato / obsoleto (redistribuir):**
- **Redação (2403) = 37.385 posts** ⚠️ — categoria-catcher (quase tudo cai aqui). **Decisão estratégica do Miguel:** manter como "geral/não-classificado" ou redistribuir massivamente?
- Conteúdo Livre (3) 1.956, Uncategized (1) 47, Assinante (4) 552, Comunicados 212, Destaques 53, No home 3, Atualidades 1
- English (1336) 74, Espanol (1343) 31 — versões em outro idioma (talvez manter separado?)
- Formato: Entrevista 255, Exclusivo! 189, Humor 148, Análise de Conjuntura 406, Notas Urgentes 609, Notas Internacionais 258, Notas da política 14, Clipping 1, Boatos 8, Séries 2, Spoiler 1, Ao vivo 5
- Séries/colunas: Duplo Expresso 47, Cafezinho no Almoço 42, Cafezinho Econômico 14, Bom Dia Cafezinho 5, Cafezinho Espresso 4, etc.
- Obsoletos: Governo Temer, Eleições 2014, Temergate, Fenae, INSS, ELETROBRAS, etc.

---

## 2. MODELO DE TAXONOMIA-ALVO (proposta para o Miguel validar)

Princípio do Miguel: **poucas categorias, 2 eixos (geografia + temas), geografia até estado, cidade = tag.**

### 2.1 Eixo TEMAS (editoriais) — ~15 categorias

As que têm mais posts + cobrem o essencial de um portal político:

| # | Categoria | ID atual | Posts | Observação |
|---|---|---|---|---|
| 1 | Política | 22 | 12.866 | Absorve Golpe/Fascismo/Ditadura/Congresso/STF/Eleições |
| 2 | Internacional | 15 | 8.361 | Mantém |
| 3 | Economia | 43 | 6.293 | Absorve Petrobrás/Agro/Indústria/BNDES/Mercado |
| 4 | Geopolítica | 5003 | 5.913 | Absorve Guerra/Países (China/EUA viram tag) |
| 5 | Tecnologia | 30 | 4.897 | Absorve IA/Computação Quântica/Guerra dos chips |
| 6 | Justiça | 1335 | 1.547 | Absorve STF/Lava-Jato/Corrupção/Lawfare |
| 7 | Ciência | 735 | 1.150 | Mantém |
| 8 | Direitos Humanos | 358 | 888 | Mantém |
| 9 | Energia | 98 | 703 | Mantém (petróleo + elétrica) |
| 10 | Meio Ambiente | 582 | 696 | Mantém |
| 11 | Saúde | 258 | 663 | Mantém |
| 12 | Mídia | 23 | 1.234 | Crítica de mídia — editoria forte do portal |
| 13 | Educação | 1479 | 343 | Mantém |
| 14 | Segurança | 36 | 370 | Mantém |
| 15 | Cultura | 79 | 353 | Absorve Cinema/Música/Literatura |
| 16 | Esporte | 1271 | 210 | Singular (consolida Esportes/Futebol) |

> **+1 a decidir:** "Redação" (37.385) vira a categoria **"Geral"** ou some? (ver §4.4)

### 2.2 Eixo GEOGRAFIA — hierárquica Regional ▸ região ▸ estado

```
Regional (4986)
├── Sudeste (21070)
│   ├── Rio de Janeiro (1656)
│   ├── São Paulo (4988)
│   ├── Minas Gerais (2549)
│   ├── Espírito Santo (21076)
├── Sul (21071)
│   ├── Paraná (21082)
│   ├── Rio Grande do Sul (5004)
│   ├── Santa Catarina (21088)
├── Nordeste (4984)
│   ├── Ceará (4968) · Bahia (4994) · Pernambuco (21083) · Paraíba (5101)
│   ├── + Alagoas, Maranhão, Piauí, RN, Sergipe, (criar)
├── Norte (21068)
│   ├── + Amazonas, Pará, Amapá, Roraima, Rondônia, Acre, Tocantins
├── Centro-Oeste (21069)
│   ├── + Distrito Federal (CRIAR — faltante) · Goiás · Mato Grosso · Mato Grosso do Sul
```

**Cidade = TAG** (sai de categoria): Rio de Janeiro Capital (5002) → tag, São Paulo capital (5001) → tag, Brasília (5710) → tag, Niterói, Belo Horizonte, Nova Friburgo, Baixada Fluminense.

> **Atenção SEO:** a página `/categoria/sao-paulo-capital/` (222 posts) vai mudar de URL. **Redirect 301 obrigatório** (ver §5).

### 2.3 O que VIRA TAG (deixa de ser categoria)

- **~45 colunistas/autores** → tag de autor (ex.: `tag/rhyan-de-meira/`) **OU** abandonar categoria e classificar via `post_author` + perfil de autor. (Decisão Miguel §4.3)
- **Países/regiões estrangeiras** → tag (China, EUA, Rússia, Argentina, Europa, Brics, África, Oriente Médio) — tags equivalentes já existem e têm mais posts que as categorias
- **Cidades brasileiras** → tag
- **Eleições por ano** → uma tag `eleicoes` + tag anual
- **Séries/colunas nomeadas** (Duplo Expresso, Cafezinho no Almoço, Cafeína, etc.) → tag

---

## 3. PLANO DE TAGS (limpeza)

### 3.1 Eliminar
- **969 tags órfãs (count=0)** — lixo puro, excluir direto.
- **Revisar 12.845 singletons (count=1)** — a grande maioria é lixo (título-quebrado, erro de digitação). **Política proposta:** excluir as que casam com blacklist (numerosas, typos, só-diacrítico) + revisar manualmente as de alto valor SEO. Em lotes.

### 3.2 Converter (59 tags com `#`)
- Cada tag `#Xxx` → redistribuir para a tag equivalente sem `#`. Ex.: `#ChinaEUA` (289) → somar em `china` + `eua`. `#GeopolíticaGlobal` (27) → `geopolitica`. `#DonaldTrump` (3) → `donald-trump`.
- Casos multi-tag numa string (`#ColiseuCarioca #JustiçaDoPolegar ...`) → quebrar e redistribuir.

### 3.3 Preservar
- **193 tags com >50 posts** — o núcleo saudável (eua, lula, china, stf, trump, etc.). Manter todas.

---

## 4. ETAPAS DE EXECUÇÃO (uma por dia, ao longo da semana — não pesar)

> Cada etapa = sessão isolada de ~1h, com **backup antes**, **teste no espelho** `cafezinho.news` antes do canônico, e **redirects 301** quando uma URL de categoria some.

| Etapa | O quê | Risco | Pré-requisito |
|---|---|---|---|
| **0 ✅ FEITA** | Rastreamento leve + este plano | zero | — |
| **1** | **Backup DB completo** (mysqldump wp_terms + wp_term_taxonomy + wp_term_relationships + redirects-table) no canônico + snapshot espelho | zero | — |
| **2** | **Geografia:** criar DF + hierarquizar Regional▸5regiões▸27estados; converter 7 cidades em tag | 🟡 médio (muda URLs de categoria) | Etapa 1 |
| **3** | **Autores:** converter ~45 categorias de colunistas → tag de autor (ou post_author) | 🟡 médio | Etapa 1 + decisão §4.3 |
| **4** | **Temas:** consolidar redundâncias (Guerra→Geopolítica, Golpe→Política, STF→Justiça, 8 Eleições→1, etc.) | 🟡 médio | Etapa 1 |
| **5** | **Lixo/catch-all:** redistribuir Redação/Conteúdo Livre/Uncategized/Assinante/Comunicados | 🟠 alto (37.385 posts da Redação!) | Decisão §4.4 |
| **6** | **Tags:** excluir 969 órfãs + converter 59 com `#` + 1º lote de singletons | 🟢 baixo | Etapa 1 |
| **7** | **SEO/Menu:** refletir nova taxonomia no menu hambúrguer + redirects 301 em massa + purgar cache + reenviar sitemap ao Google | 🟠 alto (indexação) | Etapas 2–6 |

### 4.1 Decisão pendente do Miguel — Geografia
- Confirmar **5 regiões** (Sudeste/Sul/Nordeste/Norte/Centro-Oeste) vs 4? (mesma pendência do menu hambúrguer, já no monitor)
- DF: criar como estado?

### 4.2 Decisão pendente — Temas
- Confirmar as ~15 editoriais da §2.1? Tirar/adcional alguma? (ex.: manter "Mídia" como editoria? "Energia" própria ou dentro de Economia?)

### 4.3 Decisão pendente — Autores (CRÍTICA)
Como classificar colunistas depois que a categoria some?
- **Opção A:** virar **tag de autor** (`/tag/rhyan-de-meira/`) — simples, mantém URL indexável.
- **Opção B:** abandonar categoria e classificar só via **`post_author`** (perfil WP) — mais "correto" estruturalmente, mas muda tudo.
- **Recomendação:** Opção A (tag de autor) — preserva SEO, é reversível, baixo risco.

### 4.4 Decisão pendente — "Redação" (37.385 posts) é o elefante
- **Opção A:** renomear para **"Geral"** e manter como categoria-catcher (zero redistribuição, baixo risco). ⭐ recomendado
- **Opção B:** redistribuir os 37.385 por tema/geografia (alto risco, alto esforço, pode demorar dias).
- **Recomendação:** Opção A — "Redação/Geral" fica como categoria explícita de "não classificado".

---

## 5. ⚠️ PONTOS CRÍTICOS (não podem ser esquecidos)

1. **Backup ANTES de cada etapa de escrita** — `mysqldump` das tabelas `wp_terms`, `wp_term_taxonomy`, `wp_term_relationships`. Sem backup, não executa.
2. **Redirects 301** — toda categoria que some vira 404 na URL `/categoria/slug/`. Mapear antes (slug antigo → destino: tag ou nova categoria) e configurar no Nginx **antes** de excluir. Crítico para SEO — o site tem milhares de leitores diários e URLs indexadas no Google.
3. **Espelho primeiro** (`cafezinho.news`) — toda mudança testada lá (sincronizado de hora em hora, não copia tema) antes de ir ao canônico `ocafezinho.com`.
4. **Cache WP Rocket** — purge após cada etapa.
5. **Posts órfãos de categoria** — ao excluir categoria, o WP move posts para a categoria default (config `default_category`). Confirmar qual é antes de excluir em massa.
6. **Menu canônico 21062** — refazer o submenu Editorias ao final (Etapa 7) para refletir as ~15 editoriais + dropdown Regional▸região▸estado.
7. **Autores como tag vs `post_author`** — se colunista já existe como usuário WP, a tag de autor pode duplicar; alinhar com perfis existentes.

---

## 6. Estado da missão (Regra Nº 3)

- **O que aconteceu (12/08 19:25–19:30):** rastreamento leve só-leitura no canônico (categorias + tags + perfis de contagem) + redação deste plano.
- **O que está PRONTO:** diagnóstico completo (§1) + modelo de taxonomia-alvo (§2) + plano de tags (§3) + 7 etapas (§4) + pontos críticos (§5).
- **O que FALTA:** validação do Miguel sobre 4 decisões (§4.1 geografia, §4.2 temas, §4.3 autores, §4.4 Redação) → só então começar Etapa 1 (backup).
- **O que preciso do Miguel:**
  1. Validar as ~15 editoriais (§2.1) — tirar/adcional alguma?
  2. Geografia: 4 ou 5 regiões? Criar DF?
  3. Autores: Opção A (tag) ou B (post_author)?
  4. "Redação" (37.385): Opção A (virar "Geral") ou B (redistribuir)?
  5. Confirma execução em etapas ao longo da semana, uma por sessão, espelho-antes-canônico?
- **Próximo passo:** Miguel responde as 5 perguntas → Etapa 1 (backup) pode começar.

---

## 7. Catalogação

- Fórum (este): `Foruns/forum_grande_limpeza_taxonomia_cafezinho_20260812.md`
- A executar (Tema Duplo na 1ª etapa de escrita): `Memorias/memoria_grande_limpeza_taxonomia_cafezinho_*.md`
- Nodos: `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` (nova seção TAXONOMIA) + `CEREBRO_NODE_SEO_OBSERVATORY.md` (redirects) + `CEREBRO_NODE_ATUALIZACOES.md` (linha do tempo).

---

# 📐 ADENDO (12/08 ~19:40) — Análise de Risco + Plano de Longo Prazo

> **Origem:** Miguel — *"primeiro faça uma análise de risco. E faça um plano de longo prazo, distribuindo a mudança ao longo de semanas ou mesmo meses, começando pelo mais importante. A gente usa o loop vigília + backup + ponte aqui do ZCode pra ir fazendo isso com calma. Prepara o plano."*
> **Isto SUBSTITUI a cadência "7 etapas em 7 dias" do §4** pelo modelo de **ondas mensais com autonomia gradual**. O §1–§3 (diagnóstico + modelo-alvo) continuam válidos.

## 8. Análise de Risco (matriz)

Site-alvo: **WordPress O Cafezinho canônico** (`ocafezinho.com`) — produção, **milhares de leitores/dia**, URLs indexadas no Google, MySQL já sob pressão (MyISAM + swap 2,5 GB + Wordfence 1,2 GB — ver diagnóstico `forum_diagnostico_peso_painel_cafezinho_canonico_20260811.md`).

| # | Risco | Severidade | Prob. | Mitigação |
|---|---|---|---|---|
| 1 | **SEO — 404 em massa** ao remover categoria (`/categoria/slug/` indexada) | 🔴 CRÍTICA | Alta | Mapear redirects 301 **antes** de excluir; reenviar sitemap ao Google; monitorar Search Console 7 dias pós-onda |
| 2 | **Perda de link juice / tráfego orgânico** | 🔴 CRÍTICA | Média | Redirect 301 1:1 preserva ~100% do juice; `rel=canonical` temporário se dupla durante a transição |
| 3 | **Quebra de blocos do tema** — `front-page.php` usa `category__in=array(ID)` | 🟠 ALTA | Média | Lista de **IDs intocáveis** (§10.3); ao fundir, atualizar PHP no mesmo commit; testar no espelho |
| 4 | **Quebra de agentes** — `CAT_*_ID` hardcoded (cat 22 Política, 28 Vídeos, 43 Economia, 79 Cultura, 258 Saúde, 582 Meio Ambiente, 1271 Esporte, 5003 Geopolítica, 5087 Headline, 2403 Redação...) | 🟠 ALTA | Alta | Fundir **sempre mantendo o ID-alvo** (mover posts de Esportes 1426 → Esporte 1271, nunca o inverso); atualizar `.env`/CONFIG dos agentes na mesma onda |
| 5 | **Menu canônico 21062** — referências por db_id/term_id | 🟡 MÉDIA | Alta | Reconfigurar menu na mesma onda; `auto_add` OFF sempre; backup do menu antes |
| 6 | **Performance** — INSERT/DELETE em massa em `wp_term_relationships` trava MyISAM (lock de tabela) | 🟡 MÉDIA | Alta | Lotes de **≤500 posts**; janela de madrugada (01h–05h BRT); observar `slow_query_log`; pausar se swap > 3 GB |
| 7 | **Posts órfãos** — ficam sem categoria ao excluir a deles | 🟡 MÉDIA | Média | Confirmar `default_category` antes; reatribuir a categoria-alvo **antes** de excluir a origem |
| 8 | **Count fantasma** — `count` dessincronizado (já vimos "655" na cat Vídeos) | 🟢 BAIXA | Alta | `wp term recalculate-count` ou UPDATE manual pós-lote; validar HTML renderizado |
| 9 | **Espelho divergente** — sync `:17`/h copia posts mas termos podem divergir | 🟢 BAIXA | Média | Validar espelho antes de cada onda canônica; termos criados no canônico primeiro |
| 10 | **AMP** — páginas de categoria AMP com cache próprio | 🟢 BAIXA | Média | Purge cache AMP pós-onda (WP Rocket + AMP plugin) |
| 11 | **RSS externo** — feeds `/categoria/slug/feed/` quebram | 🟢 BAIXA | Baixa | Redirects 301 cobrem feeds (HTTP redirect vale p/ tudo) |
| 12 | **Tags duplicadas** — slug em conflito (`niteroi` vs `niteroi-rio-de-janeiro`, `baixada-fluminense` x2) | 🟢 BAIXA | Alta | Deduplicar tags no mesmo lote (merge por slug canônico) |

**Veredito de risco:** 🔴 itens 1–2 exigem **redirects 301 impecáveis** (não-bargável). 🟠 itens 3–4 exigem **lista de IDs intocáveis** (§10.3). O resto é **baixo risco com mitigação simples**. **Nenhuma onda começa sem backup + dry-run + teste no espelho.**

---

## 9. Plano de Longo Prazo — 5 ondas mensais (começando pelo mais seguro + importante)

Princípio: **maior valor de higiene primeiro, com o menor risco**. Cada onda = 1 ciclo de **dry-run → espelho → observar 48h → canônico → redirects → Search Console 7 dias**. Dilui o trabalho em **semanas/meses**, sem sessões longas, sem pesar o servidor.

### 🟢 Onda 1 — Mês 1: Higiene segura (autonomia TOTAL da automação)
A automação (§10) roda sozinha, micro-lotes, checkpoint no Cérebro. Gate humano só no fim de cada sub-fase.
- **1a.** Excluir **969 tags órfãs** (count=0) — não afeta URLs de posts, baixíssimo impacto SEO.
- **1b.** Converter **59 tags com `#`** → redistribuir para a tag sem `#` (ex.: `#ChinaEUA`→`china`+`eua`).
- **1c.** Deduplicar tags com slug conflitante (`niteroi`/`niteroi-rio-de-janeiro`, etc.).
- **1d.** Consolidar redundâncias temáticas pequenas e **seguras**: `Esportes` (1426, 51) → `Esporte` (1271, mantém ID); `Ciência & Tecnologia` + `Ciência, Tecnologia & Soberania Digital` → `Tecnologia` (30); unificar `Eleições 2014/16/18/20/22` → tag `eleicoes` + `Política` (22).

### 🟡 Onda 2 — Mês 2: Geografia (gate humano por lote)
- **2a.** Criar **DF** (faltante) + confirmar 4 vs 5 regiões (decisão §4.1).
- **2b.** Hierarquizar `Regional` (4986) ▸ 5 regiões ▸ 27 estados (definir `parent` nos termos).
- **2c.** Converter **7 categorias-cidade em TAG** (São Paulo capital, RJ capital, Brasília, Niterói, BH, Nova Friburgo, Baixada Fluminense) — com **redirect 301** `/categoria/X/` → `/tag/X/`.
- **2d.** Migrar posts das categorias-país (China, EUA, Rússia...) → já têm tag equivalente com mais posts; redirect 301.

### 🟡 Onda 3 — Mês 3: Autores → tag (gate humano por lote, ~45 categorias / ~13.500 posts)
- Decisão §4.3: **Opção A (tag de autor)** recomendada — redirect 1:1 `/categoria/rhyan-de-meira/` → `/tag/rhyan-de-meira/`.
- Lotes de ≤500 posts por sessão de automação (Rhyan sozinho = 4.211 = ~9 lotes).
- Alinhar com `post_author` existente (se colunista já é usuário WP, a tag complementa o perfil).

### 🟠 Onda 4 — Mês 4: Consolidar temas grandes + "Redação" (gate humano por onda)
- Fundir Guerra→Geopolítica, Golpe/Metagolpe/Fascismo/Ditadura→Política, STF/Lava-Jato/Corrupção→Justiça, Petrobrás/Agro/BNDES→Economia, etc.
- **Decisão "Redação" (37.385)** §4.4 — se Opção A (virar "Geral"), risco baixo; se redistribuir, quebra em sub-lotes temáticos ao longo do mês.

### 🟠 Onda 5 — Mês 5+: Tags singletons (12.845 — revisão assistida, longo prazo)
- A maioria é lixo (título-quebrado, typo, palavra única). Automação propõe exclusão em lotes de 100; **revisão humana amostral** antes de aplicar.
- Critério de preservação: tag com valor SEO, entidade nomeada, ou ligada a post "quente".
- Pode durar **2–3 meses** — tudo bem, é o item de menor urgência.

---

## 10. Mecanismo de execução — via Vigília + Backup + Ponte do ZCode

### 10.1 Desenho (reaproveitando o loop existente)
O ecossistema já tem 3 peças contínuas: (a) **Vigília `*/30`** (`automation-647b2f13`, motor GLM-5.2) — cadência base; (b) **Backup Total** (C01–C07 + B2) — segurança; (c) **Ponte Cafezinho** — resumo no Telegram do Miguel.

**Proposta:** criar uma automação dedicada **"🧹 Faxina Taxonomia Cafezinho"** (cron próprio, ex.: `*/2h`), com o MESMO padrão da vigília (checkpoint Cérebro + resumo Ponte), independente da Vigília `*/30` (pra ter kill switch próprio e não sobrecarregar a vigília). Alternativa B: estender a Vigília `*/30` com um "gancho faxina" a cada N disparos — menos recomendado (mistura responsabilidades).

### 10.2 O que cada disparo da automação faz (~3 min de trabalho)
1. Lê o **estado da faxina** em `Cerebro/Foruns/faxina_taxonomia_PROGRESSO.md` (onda/sub-fase/lote/contador).
2. Executa **UM micro-lote** (ex.: excluir 50 tags órfãs, ou migrar 200 posts) — sempre via SSH `cafezinho-wp` + wp-cli, com **dry-run** que conta antes de escrever.
3. Atualiza o PROGRESSO + anexa 1 linha no `Memorias/memoria_grande_limpeza_taxonomia_*.md` (log auditável).
4. Envia resumo curto via Ponte (`ponte_cafezinho.py --send "🧹 Faxina: lote X — 50 tags órfãs removidas (919/969)"`).
5. **Kill switch:** se erro (403, timeout, swap > 3 GB, count divergente), **PÁRA** e avisa o Miguel no Telegram — não insiste.

### 10.3 Lista de IDs INTOCÁVEIS (automação nunca mexe sem gate humano)
Categorias amarradas a agentes/menu/blocos do tema — fundir SEMPRE mantendo estes como destino:
- **Agentes V4/verticais:** 22 (Política), 43 (Economia), 79 (Cultura), 258 (Saúde), 582 (Meio Ambiente), 1271 (Esporte), 5003 (Geopolítica), 30 (Tecnologia), 15 (Internacional), 735 (Ciência).
- **Agentes especiais:** 28 (Vídeos/cat YouTube unificada), 5087 (Headline/manchete), 2403 (Redação → possível "Geral").
- **Menu/estrutura:** 4986 (Regional), 21062 (menu canônico), 21068–21090 (regiões + estados do menu hambúrguer).
- **Regra:** ao fundir A→B, **B é sempre o intocável** (ex.: Esportes 1426 → Esporte 1271).

### 10.4 Autonomia por onda (gatilho humano)
| Onda | Automação sozinha? | Gate humano |
|---|---|---|
| 1 (tags órfãs/#, duplicatas, redundâncias pequenas) | ✅ **Sim** | Só revisar o relatório diário da Ponte |
| 2 (geografia) | 🟡 Prepara + dry-run | Validação Miguel antes de "aplica no canônico" |
| 3 (autores) | 🟡 Executa em lote | Miguel aprova o lote (autor por autor) |
| 4 (temas grandes + Redação) | 🟠 Prepara | Miguel decide onda por onda |
| 5 (singletons) | 🟡 Propõe exclusão | Revisão humana amostral antes de aplicar |

### 10.5 Salvaguardas obrigatórias
1. **Backup antes de cada onda** (mysqldump `wp_terms`+`wp_term_taxonomy`+`wp_term_relationships`) — a automação **recusa** rodar se não houver backup < 24h.
2. **Dry-run sempre** — contar o que mudaria antes de escrever.
3. **Espelho antes do canônico** — toda mudança testada em `cafezinho.news`, observada 48h.
4. **Janela de madrugada** (01h–05h BRT) para lotes > 100 posts.
5. **Redirects 301 no Nginx configurados ANTES** de excluir categoria (script que gera o bloco de redirects a partir da tabela antigo→novo).
6. **Search Console** — após cada onda no canônico, observar 7 dias por 404s/indexação.
7. **Kill switch diário** — limite de operações/dia (ex.: 500 posts migrados ou 200 tags excluídas); excedeu, espera o dia seguinte.

---

## 11. Estado da missão (atualizado 12/08 19:40)

- **O que aconteceu:** adendo de análise de risco (§8) + replanejamento em ondas mensais (§9) + desenho do mecanismo de automação (§10) — **sem criar cron, sem mexer no banco**.
- **O que está PRONTO:** diagnóstico + modelo-alvo + análise de risco + plano de longo prazo + mecanismo desenhado.
- **O que FALTA (decisões Miguel):**
  1. As **4 decisões originais** (§4): ~15 editoriais ok? · 4 vs 5 regiões + DF? · autores→tag? · "Redação"→"Geral"?
  2. **Mecanismo:** criar automação dedicada "🧹 Faxina Taxonomia" (recomendado) vs estender a Vigília `*/30`?
  3. **Cadência inicial:** `*/2h` (10–12 lotes/dia, Onda 1 em ~1 semana) ou mais lento `*/6h` (Onda 1 em ~3 semanas)?
  4. **Confirma gate humano** por onda conforme §10.4?
- **Próximo passo:** Miguel responde → (a) se aprovar o mecanismo, **crio a automação** via CronCreate + o arquivo `faxina_taxonomia_PROGRESSO.md` inicial; (b) começo a **Onda 1** (tags órfãs) que é segura e não depende das 4 decisões editoriais.

---

## 12. Análise de Impacto SEO aprofundada (12/08 19:45 — read-only no canônico)

> **Origem:** Miguel — *"vou precisar de mais análise sobre impacto SEO."*
> Investigação empírica via SSH + curl no domínio real `ocafezinho.com` (não localhost).

### 12.1 Descobertas factuais (comprovadas)

1. **URL de categoria é servida na RAIZ** — o Nginx faz redirect 301 de `/categoria/X/` → `/X/`:
   - `ocafezinho.com/categoria/redacao/` → **301 → `www.ocafezinho.com/redacao/`** → **200** ✅
   - `ocafezinho.com/categoria/rhyan-de-meira/` → **301 → `/rhyan-de-meira/`** → **200** ✅
   - Logo: cada categoria tem uma URL pública curta (`/redacao/`, `/politica-2/`, `/rhyan-de-meira/`, `/videos/`, `/economia/`...) **indexável pelo Google**.
2. **URL de tag** = `/tag/X/` → **200** (indexável) para tags com posts. Confirmado: `/tag/lula/` 200, `/tag/china/` 200.
3. **robots.txt** (público) só bloqueia `/wp-admin/` e `/wp-includes/` — **NÃO bloqueia categoria nem tag** → Google livre pra indexar archives.
4. **Sitemap ativo** — `sitemap_index.xml` (200) referencia `category-sitemap.xml` (200) + `news-sitemap.xml` (200). **Categorias são alimentadas ao Google via sitemap.**
5. **Tags órfãs (count=0) retornam 404** — testadas 6 (`/tag/ford/`, `/tag/gaza-2/`, `/tag/reajuste-dos-servidores/`, `/tag/forcasarmadaschinesas/`, etc.) — **todas 404**. Ou seja: **tags sem posts já não têm URL pública indexável**.

### 12.2 Matriz de impacto SEO por operação

| Operação | URL pública afetada | Estado hoje | Impacto SEO | Ação obrigatória |
|---|---|---|---|---|
| Excluir 969 tags órfãs (count=0) | `/tag/X/` | **já 404** | 🟢 **NENHUM** (SEO-neutro) | Nenhuma — seguro excluir direto |
| Converter 59 tags com `#` | `/tag/chinaeua/` etc. | 200 (indexada) | 🟡 Médio (URL some) | **Redirect 301** → `/tag/china/` (ou destino) |
| Cidade → tag (Onda 2) | `/sao-paulo-capital/`, `/rio-de-janeiro-capital/`, `/brasilia/` | 200 | 🟡 Médio | **Redirect 301** → `/tag/X/` |
| Autor → tag (Onda 3) | `/rhyan-de-meira/`, `/clarice-candido/`... (~45 URLs) | 200 (forte tráfego colunista) | 🟠 Médio-alto | **Redirect 301** 1:1 → `/tag/X/` |
| Fundir categorias (Onda 4) | URL da origem | 200 | 🟡 Médio | **Redirect 301** origem→destino |
| Renomear slug de categoria | URL antiga | 200 | 🟡 Médio | **Redirect 301** antigo→novo |

### 12.3 Conclusões da análise SEO

1. **A Onda 1a (969 tags órfãs) é 100% SEO-neutra** — comprovado que count=0 = 404 = não indexada. **A automação pode excluir sem redirect e sem risco de indexação.** ✅
2. **Tags com `#` (59) e tudo que envolve categoria/tag-com-posts NÃO é SEO-neutro** — exigem redirect 301 mapeado. Por isso essas operações têm **gate humano** (§10.4) e não rodam sozinhas na automação noturna.
3. **Estratégia SEO padrão para cada onda (2 em diante):** (a) gerar tabela `slug_antigo → slug_novo` ANTES; (b) configurar redirects 301 no Nginx ANTES de excluir; (c) purge WP Rocket + AMP cache; (d) reenviar sitemap ao Google via Search Console; (e) observar 7 dias por 404s e perda de impressões.
4. **Risco residual controlado:** redirects 301 preservam ~100% do link juice (Google). O perigo real seria excluir SEM redirect — por isso a regra de ouro: **nenhuma categoria/tag-com-posts é excluída sem o redirect já no ar**.
5. **Recomendação de monitoramento:** antes da 1ª onda com redirect (Onda 1b tags #), tirar um **snapshot do Google Search Console** (impressões/cliques por página) como baseline — pedir ao Miguel acesso, ou ele exporta. Permite medir se alguma onda causou queda.

### 12.4 O que MUDA no plano com essa análise
- **Onda 1 reordenada:** `1a` (969 órfãs, autonomia total) → **só depois** `1b` (59 tags `#`, com redirect + gate humano). A automação noturna faz **só 1a** até zerar; 1b fica para sessão assistida.
- **Onda 2/3/4:** toda mudança de URL vem precedida de "fase redirect" (configurar 301 no Nginx 24h antes de excluir a categoria) + baseline Search Console.

---

## 13. PLANO DE LIMPEZA DE TAGS (fase futura, em etapas) — ordem Miguel 12/08 ~23:15

> **Origem:** Miguel — *"bota no plano também para a gente limpar as tags no momento certo, em etapas."*
>
> ⚠️ **ATUALIZAÇÃO 13/08 14:10 — PAUSA + DESCOBERTA SEO + CRITÉRIO REVISADO:** (1) **Pausa total** até o Miguel acabar a reforma do **MENU** — o menu vira a **fonte de verdade** da taxonomia. (2) **Descoberta:** tags `count=0` servem HTTP **200** com `index,follow` no domínio público → **NÃO são SEO-neutras** como se supunha (a validação de segurança da automação pegou e abortou; **0 tags apagadas**, backup intacto). (3) **Critério revisado:** **NUNCA apagar por `count=0`** — pode ser categoria-âncora de menu (ex.: "Região Norte" tem 0 posts mas abre os estados). Candidata a apagar = **não está no menu E não é submenu**. (4) Tudo consolidado no **§9 do `forum_politica_categorias_cafezinho_20260812.md`**.
>
> ✅ **ATUALIZAÇÃO 14/08 ~08:20 — ONDA 1a/T1 EXECUTADA E CONCLUÍDA:** ordem Miguel *"já terminei a reforma do menu; pode continuar faxina; não mexer nos itens do menu (mesmo vazios — regiões, estados)"*. Menu 21062 mapeado e protegido (43 itens: regiões, 27 UF, editoriais, Eleições▸2026). Execução manual assistida: backup fresco `/root/backup_taxonomia_20260814_0800.sql` → lotes de 50 c/ re-confirmação count=0 → **tags órfãs 969→0** (968 excluídas; total 19.460→18.492). Zero categorias/menu/posts tocados. Site HTTP 200. Log completo: `Memorias/memoria_grande_limpeza_taxonomia_20260812.md`. **Próximo: T2/1b (59 tags `#` c/ redirect 301) — gate humano.**
> **Estado:** ⏸️ **AGUARDANDO O "MOMENTO CERTO"** — só começa **depois da Política de Categorias estabilizada** (mu-plugin Fase 1 LOG rodando ~2–4 semanas, sem violações novas). As tags são o item de **menor urgência** (não travam a política nem a publicação nova).
> **Política de Categorias (canônica):** `CARTAO_BOLSO_POLITICA_CATEGORIAS.md` + `Foruns/forum_politica_categorias_cafezinho_20260812.md`.

### Gatilho ("momento certo")
Política de Categorias com mu-plugin **ENFORCE ativo** + 2 semanas sem violações novas → aí começa a limpeza de tags por **T1**.

### Etapas (cada uma: gate humano + dry-run + backup)

| Etapa | O quê | Volume | Impacto SEO | Autonomia |
|---|---|---|---|---|
| **T1** | Excluir tags órfãs (count=0) | 969 | 🟢 **neutro** (já dão 404, não indexadas) | ✅ automação (já criada, pausada) |
| **T2** | Converter tags com `#` → tag sem `#` (`#ChinaEUA`→`china`+`eua`) | 59 | 🟡 médio (redirect 301) | gate humano |
| **T3** | Deduplicar tags de slug conflitante (`niteroi`/`niteroi-rio-de-janeiro`, etc.) | ~dezenas | 🟡 médio (merge + redirect) | gate humano |
| **T4** | Revisar/excluir singletons (count=1) — maioria é lixo (título-quebrado, typo, palavra única) | 12.845 | 🟡 variável | revisão humana amostral, lotes de 100 |
| **T5** | Padronizar nomenclatura + **mu-plugin validador de tag** (sem `#`, sem duplicar slug, sem palavra-de-título) | — | 🟢 preventivo | preventivo (contínuo) |

### Regras para T2–T4 (toda tag com posts/URL indexada)
1. Antes de excluir/fundir: mapear `slug_antigo → slug_novo`.
2. Configurar **redirect 301** no Nginx (`/tag/antigo/` → `/tag/novo/`) **24h antes** de excluir.
3. Purge WP Rocket + reenviar sitemap ao Google.
4. Observar Search Console 7 dias por 404s.

### Cadência (quando reativada)
Mesma pegada da automação de faxina: 2 sprints noturnos (2h/4h BRT), lotes pequenos (≤80/sprint ou ≤100 singletons), checkpoint no Cérebro, resumo na Ponte. **T1 roda sozinho** (seguro); **T2–T5 com gate humano** por lote.

> **Para ativar:** quando o Miguel disser *"é o momento certo das tags"*, reativar T1 mudando `STATUS: ATIVO` em `Foruns/faxina_taxonomia_PROGRESSO.md` e seguir T2–T5 com gates.
