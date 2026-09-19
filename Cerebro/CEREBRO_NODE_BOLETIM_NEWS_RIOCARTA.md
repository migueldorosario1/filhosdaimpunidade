# Boletim News Rio Carta

Gerado automaticamente em 2026-05-19 06:20 BRT.

Este boletim resume os fóruns recentes do Rio Carta para retomada rápida por Miguel, Codex, Claude, Antigravity e Trindade chinesa.

## Regras fixas

- Rio Carta e Astro/Markdown/Vercel/Git, nao WordPress.
- Qualquer proposta em linguagem WP/API REST precisa ser traduzida para Markdown/frontmatter/Git antes de virar codigo.
- Todo sprint Rio Carta deve deixar ponteiro no indice oficial do projeto.
- Imagem destacada/OG image e obrigatoria; IA de imagem fica como ultimo fallback.
- Rio Carta pode ser laboratorio para o Cafezinho, sem tocar no Cafezinho vivo.

## Endereços principais

- Índice oficial Rio Carta: `Rio Carta Agentes/CEREBRO_INDEX_RIOCARTA.md`
- Fóruns Rio Carta: `Rio Carta Agentes/Foruns`
- Fóruns Trindade/Cafezinho com assuntos Rio Carta: `Projeto Cafezinho Agentes/Foruns`
- Canal Trindade: `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`

## Fóruns recentes analisados (16 / últimos 3 dias)

### Rio Carta — Painel Admin 502 em `/admin`

- Arquivo: `Rio Carta Agentes/Foruns/forum_riocarta_admin_502_20260517.md`
- Atualizado: 2026-05-18 15:55 BRT
- Pontos principais:
  - Rio Carta — Painel Admin 502 em `/admin`
  - [2026-05-17 18:46 BRT] Diagnóstico
  - Próximo hardening recomendado: substituir o painel Flask legado por um painel administrado dentro da arquitetura nova, com autenticação e deploy sem segredos legados.

### Diagnóstico de Problema de Acesso - Rio Carta (Theo Rodrigues)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_acesso_theo_riocarta.md`
- Atualizado: 2026-05-18 13:38 BRT
- Pontos principais:
  - Diagnóstico de Problema de Acesso - Rio Carta (Theo Rodrigues)
  - Transcrição dos Áudios

### Relatório de Operação: Auditoria e População do Menu do Rio Carta

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_auditoria_menu_riocarta_20260518.md`
- Atualizado: 2026-05-18 02:16 BRT
- Pontos principais:
  - Relatório de Operação: Auditoria e População do Menu do Rio Carta
  - Resumo do que foi feito

### Fórum Reativação Global South News

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_reativacao_gsn.md`
- Atualizado: 2026-05-18 00:22 BRT
- Pontos principais:
  - Fórum Reativação Global South News
  - Objetivos

### Investigação Arquitetural: Links de Navegação do Rio Carta (Prefeituras, Vereadores, Bairros)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_arquitetura_links_riocarta_20260517.md`
- Atualizado: 2026-05-17 18:58 BRT
- Pontos principais:
  - Investigação Arquitetural: Links de Navegação do Rio Carta (Prefeituras, Vereadores, Bairros)
  - 1. Status Atual da Arquitetura de Links (Header.astro)

### Arquitetura e Expansão do Menu Rio Carta

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_menu_riocarta_20260515.md`
- Atualizado: 2026-05-17 01:55 BRT
- Pontos principais:
  - Arquitetura e Expansão do Menu Rio Carta
  - Contexto
  - Decisão de slug: usar **prefixo `turismo-`** pra não conflitar com tags geográficas editoriais (ex: `turismo-niteroi`, `turismo-paraty`)
  - Validação local:
  - Validação pública:

### Fórum: Arquitetura Conceitual - Global South News (GSN)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_arquitetura_gsn_satelite_20260516.md`
- Atualizado: 2026-05-16 23:42 BRT
- Pontos principais:
  - Fórum: Arquitetura Conceitual - Global South News (GSN)
  - Objetivo
  - Validação:
  - Validação pública: `https://gsnews.vercel.app`, `https://globalsouth.news` e `https://www.globalsouth.news` servem `Global South News`, `og:url=https://globalsouth.news/` e `robots=noindex,nofollow`.

### 🌐 Fórum de Arquitetura: Global South News (GSN) como Espelho do Cafezinho

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_gsn_arquitetura_espelho_cafezinho_20260516.md`
- Atualizado: 2026-05-16 16:47 BRT
- Pontos principais:
  - 🌐 Fórum de Arquitetura: Global South News (GSN) como Espelho do Cafezinho
  - 📌 Contexto

### Arquitetura de Agentes Autônomos — Global South News (GSN)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_arquitetura_agentes_gsn_20260516.md`
- Atualizado: 2026-05-16 15:49 BRT
- Pontos principais:
  - Arquitetura de Agentes Autônomos — Global South News (GSN)
  - 1. Visão Geral

### Editoria de Opinião do Rio Carta — Diretor + 12 colunistas autônomos

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_opiniao_riocarta_20260515.md`
- Atualizado: 2026-05-16 15:13 BRT
- Pontos principais:
  - Editoria de Opinião do Rio Carta — Diretor + 12 colunistas autônomos
  - 1. Estrutura no menu (já no ar — `Header.astro` commit pendente)

### 🧪 Fórum de Proposta: Página de Teste do Novo Header (Rio Carta)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_pagina_teste_header_20260516.md`
- Atualizado: 2026-05-16 13:51 BRT
- Pontos principais:
  - 🧪 Fórum de Proposta: Página de Teste do Novo Header (Rio Carta)
  - 📌 Contexto
  - Rollback simples: remover a página de teste e o componente de teste, ou `git revert` do commit.
  - Validação local: `npm run build` OK, 3543 páginas geradas, incluindo `/teste-header-novo/index.html`.
  - Validação pública: `curl -I -L https://www.riocarta.com/teste-header-novo/` retornou HTTP 200.

### 🎨 Fórum de Arquitetura: Evolução UX/UI do Rio Carta

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_ux_ui_20260516.md`
- Atualizado: 2026-05-16 13:39 BRT
- Pontos principais:
  - 🎨 Fórum de Arquitetura: Evolução UX/UI do Rio Carta
  - 📌 Contexto
  - Implementação em fases:
  - Regra: não codar a varredura retrospectiva junto com o teste visual do header. Primeiro validar visual, depois mexer em metadados de posts.

### Fórum: Plano Estratégico e Arquitetura 100% Autônoma - Global South News (GSN)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_arquitetura_gsn_100_autonoma_20260516.md`
- Atualizado: 2026-05-16 13:37 BRT
- Pontos principais:
  - Fórum: Plano Estratégico e Arquitetura 100% Autônoma - Global South News (GSN)
  - 1. Visão Geral e Objetivo

### 🏃 Sprint de Desenvolvimento: Rio Carta e GSN

- Arquivo: `Projeto Cafezinho Agentes/Foruns/tarefa_sprint_riocarta_gsn_20260516.md`
- Atualizado: 2026-05-16 11:54 BRT
- Pontos principais:
  - 🏃 Sprint de Desenvolvimento: Rio Carta e GSN
  - 📌 Missão

### 🗳️ Fórum de Arquitetura: UX de Votos e Seção de Mapas (Rio Carta)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_votos_mapas_20260516.md`
- Atualizado: 2026-05-16 11:51 BRT
- Pontos principais:
  - 🗳️ Fórum de Arquitetura: UX de Votos e Seção de Mapas (Rio Carta)
  - 📌 Contexto e Diretrizes

### Fórum: Arquitetura de Rastreamento e População de Links - Rio Carta

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_riocarta_arquitetura_rastreador_links_20260516.md`
- Atualizado: 2026-05-16 11:11 BRT
- Pontos principais:
  - Fórum: Arquitetura de Rastreamento e População de Links - Rio Carta
  - 1. Escopo e Visão Geral

## Pendências de retomada

- Manter este boletim diário atualizado automaticamente.
- Consolidar no índice oficial qualquer fórum novo do Rio Carta.
- Implementar macroeditorias Geral/Política/Lazer no Astro com frontmatter, não via WordPress.
- Continuar separando Rio Carta de Cafezinho em credenciais, agentes sociais e deploy.

<!-- GERADO_AUTOMATICAMENTE: BOLETIM_NEWS_RIOCARTA -->

- [FÓRUM Tribunal Visual Rio Carta + plano econômico 08/09](Foruns/forum_tribunal_visual_riocarta_20260908.md) — hero do Aécio Neves curada ao vivo; tribunal visual (gate de crédito custo zero + Gemini×Qwen-VL + desembargador, fail-close) opt-in no riocarta; titulação sentence case pt-BR; cron 3/dia → 1/dia (ECONOMIA_RIOCARTA_1DIA_20260908)
- [MEMÓRIA técnica Tribunal Visual 08/09](Memorias/memoria_tribunal_visual_riocarta_20260908.md) — mapa do pipeline V4 no NYC, cadeia de falha do caso Aécio, arquivos tocados, testes, armadilhas
