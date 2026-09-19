# 🏛️ CEREBRO NODE — REVISTA MAQUIAVEL (Camada 2)

**Tema:** Revista de ciência política jornalística + podcast de debates — bilíngue PT/EN, automatizada, com trilha de credenciamento científico.
**Criado em:** 2026-07-30 por ZCode/Kimi, a pedido do Miguel (nascimento do tema na mesma sessão).
**Status:** 🟢 ATIVO E NO PORTFÓLIO — site no ar c/ identidade visual completa (01–03/08); registrada no portfólio Cafezinho Media Group em 17/08/2026 (registry sentinela 9º site + index satélites + nodo ecossistema); plano de trabalho de conteúdo (artigos científicos BR & mundo) aprovado-pendente em `Foruns/forum_revista_maquiavel_plano_trabalho_20260817.md`; entrada no painel CCTV preparada (adiada por colisão de sessão — ver fórum §6).

## O projeto (1 parágrafo) — ATUALIZADO 30/07 18:20 (pivô Miguel)

A **Maquiavel** é uma **revista internacional de ciência política**, ensaística (nunca hard news), **trilíngue EN/PT/ES** (base em inglês; `/pt/` e `/es/` com slugs próprios para indexação Google), **online contínua** e muito visual. Três trilhas: **(A)** revista automatizada — ensaios originais, curadoria legal (só licenças abertas) dos grandes sites de ciência política traduzida nas 3 línguas, submissões; **(B)** credenciamento científico (ISSN/IBICT → peer review → DOI → Qualis); **(C)** podcast de debates com cientistas políticos (IESP-UERJ, UFRJ, UFF, UFs), episódio → artigo. **Acervo:** banco de dados de revistas de CP/história/comunicação do Brasil e do mundo, repositórios de teses, universidades, Substacks e vídeos — no menu do site. Stack padrão GSN (Astro → GitHub → Vercel), site **original** (não clone); **visual/logo pelo Antigravity** a partir de prompt completo preparado pelo ZCode. Divulgação cruzada: GSN (EN/ES), Cafezinho (PT).

## Infraestrutura

| Item | Valor | Estado |
|---|---|---|
| **Site no ar** | **https://revistamaquiavel.vercel.app** (+ `/pt/`, `/es/`) | ✅ 17/17 páginas 200 (30/07 18:55) |
| **Repo GitHub** | `github.com/migueldorosario1/maquiavel` (branch `main`) | ✅ ativo; **webhook git→Vercel funcionando** (push = deploy) |
| **Clone local** | `Antigravity Google/Revista Maquiavel/maquiavel/` | ✅ ativo |
| **Projeto Vercel** | `revistamaquiavel` (id `prj_Drd9wlZp…`, conta miguel-do-rosario-s-projects) | ✅ framework astro, prod branch main, SSO off |
| **Stack** | Astro 5 + Markdown + GitHub → Vercel; rollup pin 4.22.0 (compat glibc 2.31 local) | ✅ build 18 páginas |
| **Domínio** | `maquiavel.vercel.app` tomado por terceiro (portfólio dev) → usamos revistamaquiavel; domínio próprio a pesquisar | ⏳ pendente |
| **Automação** | `agentes/fontes_curadoria.json` (9 fontes c/ licenças) + `maquiavel_agente_curador.py` (esqueleto documentado) | ✅ pronto; **sem cron sem AUTH** |
| **Visual** | `docs/PROMPT_ANTIGRAVITY_VISUAL.md` (brief completo: logo, paleta, tipografia, restrições) | ✅ pronto p/ enviar ao Antigravity |
| **Executor agentes** | NYC (padrão ecossistema) ou local | ⏳ a definir |
| **Credenciais** | `GITHUB_TOKEN` ✅; Vercel via CLI/API token local (`~/.local/share/com.vercel.cli/auth.json`) | ✅ disponível |

**Páginas (×3 línguas):** home, ensaio (slug próprio por língua + hreflang), sobre, acervo, podcast, colabore. **Conteúdo fundador:** ensaio "Why a Journal Named Machiavelli?" EN/PT/ES. **Acervo v1:** 77 entradas — 13 revistas BR, 20 mundo, 16 repositórios, 24 universidades, 8 substacks, 10 vídeos (JSON data-driven).

## Ponteiros (Camada 3)

- **Fórum fundador:** `Foruns/forum_revista_maquiavel_20260730.md` — ideia, decisões, pendências de homologação, roadmap de sprints
- **Memória fundadora:** `Memorias/memoria_revista_maquiavel_20260730.md` — cronologia da sessão, evidências da consulta ao Cérebro, schema de frontmatter proposto, detalhe técnico das 3 trilhas
- **Fórum da rodada Trindade:** `Foruns/forum_maquiavel_rodada_trindade_20260801.md` — convocada 01/08, sem respostas registradas (encerramento sugerido no plano 17/08)
- **📋 Plano de trabalho 17/08/2026:** `Foruns/forum_revista_maquiavel_plano_trabalho_20260817.md` — portfólio + 4 fases (fontes científicas BR/mundo → piloto curador → regime contínuo → trilha científica) + decisões pendentes do Miguel (§4) + entrada CCTV pronta (§6)
- **Memória do plano:** `Memorias/memoria_revista_maquiavel_portifolio_plano_20260817.md` — auditoria com provas, arquivos tocados, decisões técnicas

## Relações com o ecossistema

| Projeto | Relação |
|---|---|
| **GSN** | Stack-fonte (Astro/Vercel/agentes); canal de divulgação EN; linha editorial complementar (GSN veta política doméstica BR → Maquiavel cobre) |
| **O Cafezinho** | Canal de divulgação PT (teaser+link, padrão Revista Fórum); fonte de padrões editoriais |
| **Moka** | Sinergia de marca: O Príncipe/Maquiavel é livro-símbolo da Biblioteca Livre; transcrição de episódios |
| **Leitor de Vídeo** | Stack de transcrição reutilizada no funil podcast → artigo |
| **Vídeo Diário Multirrede (sprint)** | Infra de distribuição de cortes (FB/IG/TikTok/YT/X) para o podcast |

## Regras vivas específicas

1. **Gates editoriais desde o dia 1** (lição do BUG-20260729-GSN-PT-PAUTA-MOLE): linha editorial explícita + trava de escopo + fact-check com websearch real antes de publicar.
2. **Bilíngue nativo:** todo artigo tem par PT↔EN (`par_bilingue` no frontmatter); curadoria sempre credita a fonte original (`fonte_curadoria`).
3. **Trilha científica honesta:** ISSN/peer review/periodicidade documentados; nunca anunciar credenciamento não obtido.
4. Regra do Tema Duplo: novos fóruns/memórias do tema catalogam-se **neste nodo**, nunca direto no Index Master.

## Log do tema

| Data | Evento | Registro |
|---|---|---|
| 2026-07-30 16:40–17:00 | Nascimento da ideia (Miguel, sessão ZCode); repo criado pelo Miguel às 16:51; expansão podcast ~16:55; registro Cérebro | fórum + memória (links acima) |
| 2026-07-30 ~18:15 | 1º commit no repo (`c0579a1`, master): README bilíngue + manifesto editorial v0.1 (gates, 5 seções, trilha científica) por ZCode | este nodo |
| 2026-07-30 18:20 | Pivô de conceito (Miguel): só ciência política, internacional, trilíngue EN/PT/ES, ensaística, online contínua, acervo no menu, automação V4, visual pelo Antigravity | fórum §7, memória §8 |
| 2026-07-30 18:55–19:05 | **SITE NO AR:** esqueleto Astro i18n (18 páginas), ensaio fundador 3 línguas, acervo v1 (77 entradas), deploy Vercel (API — upload local bloqueado pela rede), webhook git→Vercel validado; domínio `revistamaquiavel.vercel.app` (maquiavel.vercel.app tomado); branch main; SSO off; automação + prompt Antigravity commitados; manifesto v0.2 | este nodo |
| 2026-08-01 10:50 | **Rodada Trindade convocada pelo Miguel:** chamada no canal + 11 pings em inboxes; fórum consolidador `Foruns/forum_maquiavel_rodada_trindade_20260801.md`; carta de missão visual para o Antigravity entregue ao Miguel (chat ZCode) | fórum da rodada |
| 2026-08-01→03 | **Identidade visual aplicada** (4 commits: direção Renascença, emblema, painel multi-coluna, logo lockup + About) — repo no `4c513f4` | git log do repo |
| 2026-08-17 ~01:00 | **Retomada (Miguel): portfólio + plano.** Auditoria (site 200 nas 3 línguas, repo limpo, só ensaio fundador publicado, rodada Trindade sem respostas); registro no portfólio Cafezinho Media Group: registry sentinela (9º site, cadência semanal/192h/git_commit, backup `.bak_pre_maquiavel_20260817`) + `CEREBRO_INDEX_SATELITES.md` + `CEREBRO_NODE_ECOSSISTEMA_CANONICO.md`; plano de trabalho 4 fases (fontes científicas BR/mundo → piloto curador → regime → trilha ISSN); entrada CCTV preparada e adiada por colisão de sessão | fórum + memória de 17/08 (ponteiros acima) |
