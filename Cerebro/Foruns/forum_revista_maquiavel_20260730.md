# 🏛️ Fórum — Revista Maquiavel (nascimento do tema) — 2026-07-30

**Data:** 2026-07-30 ~16:40 BRT
**Origem:** Ideia do Miguel em sessão ZCode (chat interativo)
**Registrado por:** ZCode/Kimi
**Memória técnica pareada:** `MEMORIA/memoria_revista_maquiavel_20260730.md`
**Nodo (Camada 2):** `CEREBRO_NODE_REVISTA_MAQUIAVEL.md`
**Status:** 🟢 NOME + REPO HOMOLOGADOS — Miguel criou `github.com/migueldorosario1/maquiavel` (público, vazio) em 30/07 16:51 BRT, durante a própria sessão. Demais pontos (§5) parcialmente abertos.

---

## 1. A ideia (palavras do Miguel, resumidas)

Criar uma **revista de ciência política jornalística** — uma revista de artigos sobre política, baseada em ciência política. Nome: **Maquiavel** (preferência expressa do próprio Miguel sobre a alternativa "Hobbes": *"não é melhor Maquiavel?"* — confirmada pela criação do repo).

**Expansão na mesma sessão (16:55 BRT):** a Maquiavel também será **podcast/programa de debates** — convidar cientistas políticos do **IESP-UERJ** (citado como "IPESP"), **UFRJ**, **UFF** e demais universidades para falar de ciência política. *"Vamos transformar nosso programa num debate sobre ciência política"* — com foco no **estado do Rio de Janeiro e no Brasil** (foco Brasil). O programa diário do Miguel (sprint Vídeo Diário Multirrede) passa a abrigar esse formato.

Escopo declarado:
- **Ciência política + jornalismo/comunicação + sociologia + ciência em geral**
- **Inteligência artificial** como pauta
- Política **brasileira e internacional**
- **Bilíngue PT + EN**
- Artigos bem escritos, pesquisa de qualidade
- Receber artigos de colaboradores e **cadastrar-se como revista científica**
- **Automação total:** "varrer o Brasil e o mundo de artigos inteligentes e publicar"
- **Divulgação cruzada:** Global South News (EN) + O Cafezinho (PT)
- Visão do Miguel: *"está na hora de fazer uma boa revista, vamos ressuscitar o conceito de revista"*

## 2. Verificação no Cérebro (feita antes de qualquer proposta)

- Menções prévias a "Maquiavel" no ecossistema = **o filósofo** (Biblioteca Livre do Moka, `PLANO_NEGOCIOS_MOKA/documentos/18_conceito_biblioteca_livre.md`; cards de citação do Cafezinho). **Nenhum projeto de revista existente** — marca livre no ecossistema.
- Sinergia já existente: **O Príncipe é livro-símbolo da campanha do Moka** — a revista fecha o círculo da marca Maquiavel no ecossistema.
- Lição obrigatória (incidente `BUG-20260729-0300-GSN-PT-PAUTA-MOLE`): automação editorial sem gate de linha editorial publica conteúdo fora da pauta → **gates rígidos desde o dia 1**.

## 3. Arquitetura proposta (ZCode — PROPOSTA, não homologada)

### Trilha A — Revista-magazine (lançar primeiro)
- **Stack comprovada do GSN:** Astro + Markdown + GitHub → Vercel; agentes geram `.md` e publicam via `git push`; custo marginal ~zero.
- **Conteúdo:**
  1. **Curadoria automatizada** — coletores varrem SciELO, think tanks (CEBRAP, FGV, IPEA), Foreign Affairs, The Conversation, blogs acadêmicos BR/mundo; LLM filtra, resume contextualiza e traduz PT↔EN.
  2. **Artigos originais** — escritos por agentes (padrão de qualidade Cafezinho/GSN) e por colaboradores humanos.
  3. **Submissões externas** — fluxo de recebimento de artigos desde o início (form/email editorial), preparando o terreno da Trilha B.
- **Gates editoriais:** linha editorial explícita + trava de escopo (ciência política/comunicação/sociologia/IA) + fact-check com websearch (regra já consolidada no ecossistema) antes de qualquer publicação.

### Trilha B — Revista científica (em paralelo, médio prazo)
1. **ISSN** via IBICT (gratuito, online) — primeiro passo formal.
2. Conselho/editorial board, normas de submissão, política de revisão por pares, periodicidade definida.
3. DOI via Crossref quando houver volume publicado.
4. Qualis/CAPES = horizonte longo (exige histórico) — a Trilha A constrói corpo e reputação.

### Distribuição cruzada (como pediu o Miguel)
- **GSN** empurra artigos EN (link/teaser) — respeitando a linha EN-only do GSN.
- **O Cafezinho** empurra artigos PT (padrão teaser + link, igual ao fluxo Revista Fórum).
- **Moka**: sinergia de marca (Maquiavel na Biblioteca Livre).

## 4. Posicionamento editorial proposto

Entre *Foreign Affairs*, *Le Monde Diplomatique* e *Piauí* — mas nascida no **Sul Global**: análise política rigorosa com base em ciência política, linguagem de revista (não de paper), bilíngue nativa. A revista cobre o espaço que o GSN não cobre (política doméstica brasileira é **proibida** no GSN por regra editorial) e que o Cafezinho cobre em ritmo diário — a Maquiavel entra com **profundidade e permanência** (artigos de ideias, não notícia quente).

## 5. Decisões pendentes do Miguel (homologação)

| # | Ponto | Proposta ZCode | Status |
|---|-------|----------------|--------|
| 1 | Nome oficial | **Maquiavel** (verificar conflitos de marca/ISSN/domínio antes) | ✅ **HOMOLOGADO** (repo criado pelo Miguel, 30/07 16:51 BRT) |
| 2 | Stack | Astro + GitHub + Vercel (padrão GSN) | ⏳ aguardando OK |
| 3 | Começo | Trilha A agora + Trilha B em paralelo | ⏳ aguardando OK |
| 4 | Domínio | Checar disponibilidade (maquiavel / revistamaquiavel, .com/.com.br/.news/.org) | ⏳ não pesquisado |
| 5 | Periodicidade/cadência | Sugestão: fluxo contínuo + "edição" temática quinzenal | ⏳ aguardando OK |
| 6 | Executor dos agentes | NYC (padrão atual do ecossistema) ou local | ⏳ aguardando OK |
| 7 | Formato podcast | Debates com cientistas políticos (IESP-UERJ, UFRJ, UFF…), foco RJ + Brasil; episódio → transcrição → artigo na revista | ⏳ formato sugerido, agenda de convidados com Miguel |

## 5b. Trilha C — Podcast/Programa (adicionada pelo Miguel na sessão)

- **Conceito:** o programa do Miguel vira também **debate de ciência política** — entrevistas/conversas com cientistas políticos de IESP-UERJ, UFRJ, UFF e outras UFs; recorte RJ + Brasil, foco Brasil.
- **Funil editorial:** episódio gravado → transcrição automática (stack Leitor de Vídeo/Moka já mapeada no ecossistema) → artigo na revista + cortes multirrede (sprint Vídeo Diário já prevê FB/IG/TikTok/YT/X).
- **Posição no site:** seção "Podcast/Entrevistas" na Maquiavel desde o esqueleto.

## 6. Próximos passos (após homologação)

1. Registrar domínio + criar repo `migueldorosario1/maquiavel` (ou nome homologado) no padrão Astro.
2. Sprint 1: esqueleto do site bilíngue (PT/EN) + identidade visual (pena/flâmula renascentista; paleta sóbria) + primeiras 5 matérias-manifesto.
3. Sprint 2: agente coletor-curador (`maquiavel_agente_curador.py`) com gates editoriais + tradução PT↔EN.
4. Sprint 3: página de submissões + normas; pedido de ISSN no IBICT.
5. Sprint 4: integração de divulgação GSN + Cafezinho (teasers automáticos).

---

*Regra do Tema Duplo cumprida: este fórum (decisões resumidas) + `MEMORIA/memoria_revista_maquiavel_20260730.md` (log técnico completo).*

---

## 7. ATUALIZAÇÃO DE CONCEITO — 30/07 ~18:20 BRT (Miguel, mesma sessão)

Decisões novas do Miguel, **substituindo/ajustando** o desenho anterior:

| # | Decisão | Detalhe |
|---|---------|---------|
| D1 | **TRILÍNGUE** | EN = base (`/`), PT = `/pt/`, ES = `/es/` — slugs/URLs separados por língua para indexação própria no Google. "Faz o básico em inglês." |
| D2 | **ESCOPO FECHADO** | **Somente ciência política** ("vamos fazer só de ciência política"). Comunicação/sociologia/IA entram apenas enquanto fenômenos políticos. |
| D3 | **POSICIONAMENTO** | **Revista internacional** desde o nascimento ("começar bem internacional"). |
| D4 | **GÊNERO** | **Ensaística, nunca hard news.** Artigos muito bem escritos, ideias, profundidade. |
| D5 | **PERIODICIDADE** | Revista **online contínua** (não mensal, sem data fixa); "muito visual". |
| D6 | **ACERVO (banco de dados)** | Menu com: teses e ensaios; links de universidades (UFRJ e ciência política no mundo); **todas as revistas de ciência política, história e comunicação do Brasil e do mundo**; links de Substacks; vídeos e entrevistas de ciência política. |
| D7 | **AUTOMAÇÃO (V4)** | Preparar a parte automática padrão V4: **RSS dos grandes sites de ciência política**, verificando **quais são abertos para copiar/traduzir** (licenças) nas 3 línguas. |
| D8 | **VISUAL** | Antigravity faz logo + direção visual elegante. ZCode prepara **todo o resto** (técnica, conteúdo, dados, esqueleto deployado) + **o prompt completo** para o Antigravity. |
| D9 | **PUBLICAÇÃO** | **Começar a publicar já.** |
| D10 | **BASE TÉCNICA** | Seguir o exemplo do GSN (GitHub + Vercel), mas com site **original**, mais ensaístico — não clone do tema GSN. |

**Plano de execução aprovado pelo Miguel ("prepara tudo, pode deixar até o esqueleto já pronto, até deployado"):**
1. Esqueleto Astro i18n próprio (EN/PT/ES) + ensaio fundador nas 3 línguas → push + deploy Vercel.
2. Banco de dados do Acervo (JSON) alimentando páginas de menu.
3. Fontes de curadoria com status de licença + esqueleto do agente curador V4.
4. Prompt visual completo para o Antigravity (`docs/PROMPT_ANTIGRAVITY_VISUAL.md` no repo).
