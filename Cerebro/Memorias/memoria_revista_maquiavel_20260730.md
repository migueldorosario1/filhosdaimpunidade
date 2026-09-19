# 🧠 Memória Técnica — Nascimento da Revista Maquiavel — 2026-07-30

**Sessão:** ZCode (chat interativo), 2026-07-30 ~16:40–17:00 BRT
**Participantes:** Miguel (ideia e decisões) + ZCode/Kimi (consulta ao Cérebro, proposta, registro)
**Fórum pareado:** `Foruns/forum_revista_maquiavel_20260730.md`
**Nodo:** `CEREBRO_NODE_REVISTA_MAQUIAVEL.md`

---

## 1. Cronologia da sessão

| Hora BRT | Evento |
|---|---|
| ~16:40 | Miguel traz a ideia: revista de ciência política jornalística, nome Hobbes **ou Maquiavel** ("não é melhor Maquiavel?"), PT+EN, política BR e internacional, receber artigos, cadastrar como revista científica, **totalmente automatizada** ("varrer o Brasil e o mundo de artigos inteligentes"), divulgação via GSN + Cafezinho. Escopo: ciência política, jornalismo/comunicação, sociologia, ciência em geral, IA. |
| ~16:42 | ZCode executa Regra Nº 1: lê `00_CEREBRO_CANONICO.md`, `CEREBRO_INDEX_MASTER.md`, `CARTAO_BOLSO_WP_REVISTA_FORUM.md`, `CEREBRO_INDEX_GSN.md`, `CEREBRO_NODE_BOLETIM_NEWS.md`, índice de despertar leve e sprints ativos; busca "maquiavel"/"revista" em todo o Cérebro. |
| ~16:45 | Achados: "Maquiavel" só existia como **autor** (Biblioteca Livre do Moka — doc 18; cards de citação Cafezinho). Nenhum projeto de revista. Lição de gates editoriais do incidente GSN 29/07 incorporada à proposta. |
| ~16:47 | ZCode apresenta proposta (duas trilhas, stack GSN, gates) + 3 perguntas de decisão (nome/stack/trilha). Miguel não responde às perguntas; segue o fluxo. |
| 16:51 | **Miguel cria o repo `github.com/migueldorosario1/maquiavel`** (público, vazio, sem branch default — verificado via `gh repo view` e `git ls-remote`). Homologação **por ato** do nome "Maquiavel". |
| ~16:55 | Miguel expande: **podcast/programa de debates** com cientistas políticos do "IPESP" (lido como **IESP-UERJ**), "UF" (universidades federais), **UFRJ**; transformar o programa dele em debate de ciência política; foco **RJ + Brasil**. Diz "continua". |
| ~17:00 | ZCode registra o tema (Regra do Tema Duplo): fórum + esta memória + nodo Camada 2 + log em ATUALIZAÇÕES + linha no Index Master. |

## 2. Conteúdo da ideia (transcrição estruturada das falas do Miguel)

- **Produto:** revista de artigos sobre política, jornalística mas baseada em ciência política.
- **Nome:** Maquiavel (preferência do próprio Miguel; confirmada pelo repo).
- **Idiomas:** português e inglês.
- **Cobertura:** política brasileira e política internacional.
- **Áreas:** ciência política + jornalismo/comunicação + sociologia + ciência em geral + inteligência artificial.
- **Qualidade:** "artigos bem escritos, pesquisa".
- **Modelo científico:** "a gente trabalha, recebe os artigos, se cadastra para ser uma revista científica".
- **Automação:** "vai ser bem automática; ela vai reunir artigos inteligentes, varrer o Brasil e o mundo de artigos inteligentes e publicar".
- **Distribuição:** GSN + Cafezinho.
- **Visão:** "ressuscitar o conceito de revista".
- **Expansão podcast:** convidar cientistas políticos (IESP-UERJ, UFRJ, UFs) para debates; o programa do Miguel passa a incluir esse formato; foco RJ e Brasil.

## 3. Consulta ao Cérebro — evidências

1. `00_CEREBRO_CANONICO.md` — caminho canônico confirmado (local, não Legacy).
2. Busca `grep -rli maquiavel` no Cérebro: apenas 3 hits relevantes —
   - `PLANO_NEGOCIOS_MOKA/documentos/18_conceito_biblioteca_livre.md` (Maquiavel = autor de O Príncipe, livro-símbolo da campanha Moka);
   - `subcerebro_antigravity_desktop/...` (cards de citações de pensadores, jun/2026);
   - `CEREBRO_NODE_ATUALIZACOES.md` (log do doc 18).
   → **Conclusão: nenhum projeto de revista registrado; marca livre no ecossistema.**
3. `CEREBRO_INDEX_GSN.md` — stack de referência: Astro/Markdown → GitHub → Vercel; agentes geram `.md`; executor atual NYC (errata 27/07); linha editorial EN-only com veto a política doméstica BR (**a Maquiavel cobre exatamente esse espaço proibido no GSN — complementaridade estrutural**).
4. `CARTAO_BOLSO_WP_REVISTA_FORUM.md` — referência de publicação dupla teaser (Cafezinho ↔ Revista Fórum), padrão reutilizável para divulgação cruzada.
5. Incidente `BUG-20260729-0300-GSN-PT-PAUTA-MOLE` — automação sem gate editorial publicou conteúdo fora da linha → **requisito rígido de gates desde o dia 1** na Maquiavel.
6. `CEREBRO_NODE_SPRINTS_ATIVOS.md` — sprint Vídeo Diário Multirrede (Miguel grava 1 vídeo/dia; FB/IG/TikTok/YT/X) = infraestrutura pronta para o podcast/cortes.

## 4. Arquitetura proposta (ZCode — itens marcados ✅ homologados por ato do Miguel)

### 4.1 Trilha A — Revista-magazine (imediata)
- **Repo:** ✅ `github.com/migueldorosario1/maquiavel` (criado 30/07 16:51 BRT; público; vazio).
- **Stack proposta:** Astro + Markdown + GitHub → Vercel (padrão GSN; `GITHUB_TOKEN` ativo no ecossistema; `VERCEL_TOKEN` pendente historicamente — deploy via webhook do GitHub dispensa token).
- **Frontmatter bilíngue proposto** (extensão do schema GSN):
  ```yaml
  ---
  title: "..."
  description: "..."
  pubDate: "ISO"
  secao: "Analise | Entrevista | Curadoria | Dossie | Resenha"
  area: "ciencia-politica | comunicacao | sociologia | ia | ciencia"
  escopo: "brasil | internacional"
  tags: ["..."]
  heroImage: "/hero/slug.jpg"
  author: "..."
  lang: "pt | en"
  par_bilingue: "slug-do-par"   # artigo PT <-> EN
  origem: "original | submissao | curadoria"
  fonte_curadoria: "URL"         # quando curadoria
  revisao: "editorial | pares"   # trilha B usa 'pares'
  draft: true | false
  ---
  ```
- **Conteúdo:** (1) curadoria automatizada BR+mundo (SciELO, CEBRAP, FGV, IPEA, Foreign Affairs, The Conversation, blogs acadêmicos) com tradução PT↔EN; (2) artigos originais (agentes + humanos); (3) submissões externas com fluxo editorial.
- **Gates obrigatórios:** linha editorial explícita; trava de escopo; fact-check com websearch real (regra consolidada do ecossistema); dedup de hero (patches V4 de 29/07 reutilizáveis).

### 4.2 Trilha B — Revista científica (paralela)
ISSN via IBICT → conselho editorial + normas + revisão por pares + periodicidade → DOI/Crossref → Qualis/CAPES (longo prazo). A Trilha A constrói corpo, corpo editorial e reputação.

### 4.3 Trilha C — Podcast/Programa (expansão do Miguel)
- Debates com cientistas políticos (IESP-UERJ, UFRJ, UFF, UFs); recorte RJ + Brasil.
- Funil: gravação → transcrição automática (stack Leitor de Vídeo/Moka) → artigo na revista + cortes multirrede (sprint Vídeo Diário).
- Seção "Podcast/Entrevistas" no site desde o esqueleto.

### 4.4 Distribuição cruzada
- GSN (EN-only) empurra artigos EN; Cafezinho (PT) empurra PT (padrão teaser+link, cf. fluxo Revista Fórum); Moka = sinergia de marca (O Príncipe na Biblioteca Livre).

## 5. Decisões e pendências (foto 30/07 17:00 BRT)

| Item | Estado |
|---|---|
| Nome "Maquiavel" | ✅ homologado por ato (repo criado) |
| Repo GitHub | ✅ existe, vazio — precisa 1º commit |
| Stack Astro/Vercel | ⏳ proposta, sem veto |
| Domínio | ⏳ não pesquisado |
| Cadência | ⏳ sugestão: fluxo contínuo + edição quinzenal |
| Executor agentes | ⏳ NYC (padrão) ou local |
| Agenda de convidados podcast | ⏳ com Miguel |

## 6. Próximos passos técnicos (ordem proposta)

1. 1º commit no repo (README + manifesto editorial + estrutura Astro mínima bilíngue).
2. Sprint 1: esqueleto site PT/EN + identidade visual + 5 matérias-manifesto (uma delas explicando o projeto Maquiavel).
3. Sprint 2: `maquiavel_agente_curador.py` (coleta → filtro escopo → fact-check → tradução → markdown → push) com gates.
4. Sprint 3: página de submissões + normas; pedido ISSN no IBICT.
5. Sprint 4: divulgação cruzada GSN/Cafezinho + seção podcast com página por episódio (player + transcrição + artigo derivado).

## 7. Observações de governança

- Tema registrado conforme Regra do Tema Duplo (fórum + memória) e catalogado em nodo próprio (Camada 2) — `CEREBRO_NODE_REVISTA_MAQUIAVEL.md`.
- Nodo linkado no `CEREBRO_INDEX_MASTER.md` (seção 1) e log estrutural em `CEREBRO_NODE_ATUALIZACOES.md`.
- Nenhum segredo/credencial neste documento.

— ZCode/Kimi, 2026-07-30 17:00 BRT

---

## 8. ADITIVO 18:20 BRT — Pivô de conceito (Miguel, mesma sessão)

**Fala-chave do Miguel (estruturada):** pegar o exemplo técnico do GSN (GitHub+Vercel) mas fazer site **original e mais ensaístico**; Antigravity fará a parte visual (logo, elegância) — ZCode prepara **toda a parte técnica**; **banco de dados** de teses, ensaios, links de universidades (UFRJ, mundo); **menu com todas as revistas de ciência política, história e comunicação do Brasil e do mundo**; links de Substacks; links de vídeos/entrevistas; **revista internacional, só de ciência política**; **não é hard news**, é ensaística; **online contínua** (não mensal), muito visual; **trilíngue EN/PT/ES** com páginas/slugs separados por língua para indexação Google, base em inglês (`/pt/`, `/es/` como prefixos); **já começar a publicar**; **automação padrão V4** com RSS dos grandes sites de ciência política, **verificando licenças** para copiar/traduzir nas 3 línguas; guardar tudo no Cérebro; deixar esqueleto deployado + prompt pronto para o Antigravity.

### Interpretação operacional (ZCode)

- **i18n:** rotas `/` (EN, default), `/pt/*`, `/es/*`; cada artigo com 3 slugs próprios e chave de par (`par_trilingue`) no frontmatter; `hreflang` no `<head>` para o Google indexar as 3 versões corretamente.
- **Escopo:** só ciência política; comunicação/sociologia/IA só como fenômenos políticos (ajusta manifesto v0.1 → v0.2).
- **Acervo:** dados em `src/data/acervo/*.json` (revistas_br, revistas_mundo, repositorios, universidades, substacks, videos) → páginas geradas por build; campos: nome, país/idioma, instituição, URL, acesso (aberto/assinatura), licença para curadoria quando aplicável.
- **Curadoria legal:** fontes com licença aberta (CC) para tradução/republicação com crédito (ex.: The Conversation CC-BY-ND, SciELO CC, openDemocracy CC-BY-NC); demais fontes = só resenha/link, nunca cópia integral. `agentes/fontes_curadoria.json` carrega o status por fonte.
- **V4:** reutilizar padrões maduros do `agentes_tematicos/v4/` (coleta → gate escopo → fact-check websearch → tradução → markdown → git push); esqueleto `agentes/maquiavel_agente_curador.py` documentado, sem cron até AUTH.
- **Deploy:** Vercel CLI autenticada no ecossistema (precedente casadamoeda); webhook GitHub→Vercel depois de conectado.

### Estado de execução (fechado 19:05 BRT)

- [x] Aditivo registrado no Cérebro (fórum §7, memória §8, nodo)
- [x] Esqueleto Astro i18n + ensaio fundador 3 línguas → **18 páginas, build limpo**
- [x] Acervo v1 (6 JSON, 77 entradas) + páginas por língua
- [x] Build + push + **deploy Vercel — https://revistamaquiavel.vercel.app (17/17 URLs 200)**; webhook git→Vercel validado
- [x] Fontes curadoria (9, com licenças) + esqueleto agente (smoke OK, sem cron sem AUTH)
- [x] Prompt Antigravity (`docs/PROMPT_ANTIGRAVITY_VISUAL.md`) + manifesto v0.2

**Notas de infra:** (1) upload local ao Vercel aborta em massa pela rede desta máquina → deploys feitos via API com o token do CLI local e, daqui em diante, pelo webhook git→Vercel; (2) `maquiavel.vercel.app` já pertence a um projeto de terceiro → domínio provisório `revistamaquiavel.vercel.app`; (3) glibc 2.31 local exige rollup ≤ 4.22 (pin em `package.json` overrides) — inócuo no build cloud; (4) branch `main` (master renomeado; default GitHub = main).
