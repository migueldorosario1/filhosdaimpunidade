# 🗞️ Boletim News — Cérebro (Camada 2)

> **🚨 TODA IA LÊ ESTE ARQUIVO PRIMEIRO AO DESPERTAR.**
> Depois: `CEREBRO_INDEX_MASTER.md` → node pertinente → fórum/memória da frente ativa.
>
> **Filosofia:** boletim leve por design (alvo <500 linhas / <25KB). Só ponteiros. Conteúdo substantivo vive nos fóruns/memórias linkados (Camada 3).

🧭 **Camada 1 (mapa):** [`CEREBRO_INDEX_MASTER.md`](./CEREBRO_INDEX_MASTER.md)

---

## 🧠 NOVO: Boletim News Dinâmico — Kimi CEO do Cérebro Vivo

**Status:** 🟢 ATIVO desde 2026-05-28 02:00 BRT
**Frequência:** A cada 10 min (teste 1h) → depois 30 min
**Local:** `root/painel_v5/boletins/boletim_latest.md`
**Painel CCTV:** http://localhost:8082/boletim
**Agente:** `~/.openclaw/workspace/agente_boletim_kimi.py`

### O que é
O **Kimi CEO** compila automaticamente:
- Ticks do Claude (Loop Maestro)
- Inboxes da Trindade
- Relatórios de monitoramento
- Sprints ativos
- Canal Trindade

### Como ler o boletim dinâmico
```bash
# Opção 1: Ler arquivo local
cat "/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/root/painel_v5/boletins/boletim_latest.md"

# Opção 2: Acessar painel CCTV
curl -s http://localhost:8082/boletim

# Opção 3: Ver histórico
curl -s http://localhost:8082/boletim/historico
```

### Protocolo de despertar atualizado (§68.1)
Todo agente ao acordar deve ler **NESTA ORDEM**:
1. Relógio real
2. **Boletim News Dinâmico** (`boletim_latest.md` ou `/boletim`)
3. Canal Trindade
4. Índice de fóruns
5. Fóruns indicados pelo boletim

---

## 🔧 Protocolo de Atualização Determinística (LEGADO — manter para referência)

Este arquivo é gerado/regerado deterministicamente pelo algoritmo em:

- `Projeto Cafezinho Agentes/root/gerar_boletim_news.py`
- Wrapper seguro: `Projeto Cafezinho Agentes/root/run_boletim_news.sh`

**Como regenerar:**
```bash
cd "/home/migueldorosario/Downloads/Antigravity Google" && python3 "Projeto Cafezinho Agentes/root/gerar_boletim_news.py"
```

**Fontes determinísticas:**
1. `Projeto Cafezinho Agentes/Foruns` → fóruns Cafezinho/Cérebro
2. `Rio Carta Agentes/Foruns` → fóruns Rio Carta

**Classificação automática por padrão de nome:**
- ☕ Cafezinho: agentes, coletores, publicadores, redes, qualidade, custos
- 📰 Rio Carta: riocarta, prefeituras, vereadores, aiatolah
- 🧠 Cérebro: trindade, roteador, índice, memória, protocolo
- 📖 Origens: livro, democracia, origens
- 🌍 Geral: tudo o mais

Se este arquivo tiver mais de 24h, **regenere antes de usar**.

---

## Atualização rápida — 2026-05-27 14:00 BRT

- **Fóruns analisados:** 40 (últimos 3 dias)
- ☕ Cafezinho: 25 | 📰 Rio Carta: 0 | 🧠 Cérebro: 11 | 📖 Origens: 0 | 🌍 Geral: 4

---

## 🎯 Decisões do Miguel (extraídas automaticamente)

- Decisão: não prosseguir automaticamente. Precisa decidir qual é o WordPress canônico antes de instalar `wp_metrics.sh`. O `node_exporter` continua ativo; Fase D WP não foi aplicada.
- Decisão de maestria:
- Decisão: Fase D WordPress metrics segue congelada até ordem explícita. Se retomada, deve usar `WP_PATH=/var/www/ocafezinho` fixo e nunca varrer `/var/www/*`.
- Ordem objetiva:
- Decisão: Fase A experimental do inbox por agente está aprovada. Padrão: Markdown com checkbox `[ ]` / `[x]`. Regra central: ordem direta deve ir para o canal e para o inbox do destinatário. Ressalva incorporada: inbox nã
- Ordem de prioridade baseada no que vi no Tencent:
- decisão;
- Pedido operacional ao Claude/Miguel: se quiserem conter antes de 01:41 BRT, o caminho mais conservador é autorizar uma intervenção mínima e reversível só na política de descarte do `agente_eleicoes`, não desligar fact-ch
- decisao = self.raciocinar_e_agir()
- Decisão operacional Codex: modelos ocidentais entram como banca, auditoria, qualidade, visão e casos especiais. Não devem virar motor diário de publicação em massa. Perplexity continua importante no Cafezinho, mas com fr

---

## ☕ O Cafezinho

### Fórum — Integridade antes do publicador

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_integridade_pre_publicador_20260527.md`
- Atualizado: 2026-05-27 12:49 BRT
- Pontos principais:
  - Fórum — Integridade antes do publicador
  - 1. Princípio
  - contexto;
  - risco jurídico;
  - Validação:

### Fórum Sprint: Resiliência LLM — Fallbacks Dinâmicos e Detecção Proativa de Cota

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_sprint_resiliencia_llm_20260527.md`
- Atualizado: 2026-05-27 12:43 BRT
- Pontos principais:
  - Fórum Sprint: Resiliência LLM — Fallbacks Dinâmicos e Detecção Proativa de Cota
  - 1. O QUE ACONTECEU — HISTÓRIA REAL
  - Validação:
  - Regra nova no prompt: cargos, funções e instituições precisam estar precisos; se houver dúvida, usar forma neutra.
  - Regra prática:

### Fórum Loop Maestro — 27/05/2026

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_loop_maestro_27mai2026.md`
- Atualizado: 2026-05-27 12:15 BRT
- Pontos principais:
  - Fórum Loop Maestro — 27/05/2026
  - Contexto
  - Próximo run 10:45. 2 reprovações consecutivas = problema de qualidade no rascunho, não técnico.
  - contexto eleitoral/2º turno/intenção de voto;
  - Validação: `python3 -m py_compile /root/fact_check_perplexity.py` OK.

### Fórum de Auditoria: Padronização do Interlink "Leia Também"

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_auditoria_interlink_20260522.md`
- Atualizado: 2026-05-27 03:46 BRT
- Pontos principais:
  - Fórum de Auditoria: Padronização do Interlink "Leia Também"
  - 1. O Problema (Violação do 6º Mandamento)

### Fórum: Emergência — Auditoria dos Agentes Pós-Reforma

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_emergencia_auditoria_agentes_pos_reforma_20260526.md`
- Atualizado: 2026-05-26 23:45 BRT
- Pontos principais:
  - Fórum: Emergência — Auditoria dos Agentes Pós-Reforma
  - 1. Pedido do Miguel
  - Regra operacional:
  - objetivo é matéria fresca, escândalo novo e coleta viva.

### Fórum: Diagnóstico — Agente Soberania Inoperante

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_agente_soberania_20260526.md`
- Atualizado: 2026-05-26 23:30 BRT
- Pontos principais:
  - Fórum: Diagnóstico — Agente Soberania Inoperante
  - Sumário

### Fórum: Relatório Técnico — LLMs, Cascatas, Timeouts e Fact-check Pós-Reforma

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_relatorio_tecnico_llms_cascatas_timeouts_20260526.md`
- Atualizado: 2026-05-26 23:29 BRT
- Pontos principais:
  - Fórum: Relatório Técnico — LLMs, Cascatas, Timeouts e Fact-check Pós-Reforma
  - 1. Pedido do Miguel
  - contexto;
  - decisão;

### 📑 Fórum: Auditoria de Publicadores e Desempenho de Agentes Autônomos (Sprint de Alinhamento)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_auditoria_publicadores_agentes_20260525.md`
- Atualizado: 2026-05-26 21:20 BRT
- Pontos principais:
  - 📑 Fórum: Auditoria de Publicadores e Desempenho de Agentes Autônomos (Sprint de Alinhamento)
  - 🧭 1. Introdução e Objetivo

### Fórum do Agente Eleições

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_agente_eleicoes.md`
- Atualizado: 2026-05-26 19:55 BRT
- Pontos principais:
  - Fórum do Agente Eleições
  - Diagnóstico Inicial (19 de Maio de 2026)
  - Validação local:
  - Pendência antes de smoke remoto:
  - Próximo passo recomendado: manter a Fase 2 com cap `1/h` e observar as próximas janelas antes de aumentar cadência. Se houver segunda alucinação de pesquisa no mesmo dia, abrir patch específico para forçar modo "pesquisa

### Fórum: Proposta de Agente Análise e Pesquisa Eleitoral

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_agente_analise_pesquisa_eleitoral_20260526.md`
- Atualizado: 2026-05-26 19:55 BRT
- Pontos principais:
  - Fórum: Proposta de Agente Análise e Pesquisa Eleitoral
  - Ideia de Miguel
  - risco de o redator preencher números que não estão na fonte.
  - alerta de discrepância entre pesquisas.
  - alerta de manipulação narrativa;

### Fórum: Divisão de Cobertura entre Agente Eleições e Agente Flávio Bolsonaro

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_divisao_eleicoes_flavio_20260526.md`
- Atualizado: 2026-05-26 19:55 BRT
- Pontos principais:
  - Fórum: Divisão de Cobertura entre Agente Eleições e Agente Flávio Bolsonaro
  - Pergunta de Miguel
  - Implementação fica para sprint futura, após 10 ciclos/24h do Agente Flávio em dry-run.

### Fórum: Ideias e Auditoria Estratégica do Agente Cobertura Flávio Bolsonaro

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_ideias_agente_flavio_bolsonaro_20260526.md`
- Atualizado: 2026-05-26 19:13 BRT
- Pontos principais:
  - Fórum: Ideias e Auditoria Estratégica do Agente Cobertura Flávio Bolsonaro
  - Contexto
  - Status verificado por Codex em 2026-05-26 17:29 BRT:

### Fórum: Sprint Radar de Frescor Político para Eleições

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_sprint_radar_frescor_politico_eleicoes_20260526.md`
- Atualizado: 2026-05-26 19:13 BRT
- Pontos principais:
  - Fórum: Sprint Radar de Frescor Político para Eleições
  - Diretiva de Miguel
  - validação automática de chaves vivas;

### Fórum: Reforma do Agente Twitter

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_reforma_agente_twitter_20260520.md`
- Atualizado: 2026-05-26 11:50 BRT
- Pontos principais:
  - Fórum: Reforma do Agente Twitter
  - Solicitação Inicial (Miguel / Antigravity)
  - Status ao vivo de cada API (`Tweepy: OK`, `Graph API: OK`, `ATProto: OK`).

### Forum: Ajuste de `modelos_vivos.json` segundo pesquisa 25/05

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_ajuste_modelos_vivos_20260526.md`
- Atualizado: 2026-05-26 11:19 BRT
- Pontos principais:
  - Forum: Ajuste de `modelos_vivos.json` segundo pesquisa 25/05
  - 1. Diagnose: O que esta ERRADO hoje no Tencent

### Padrão Ouro de Agente Autônomo — v10 Refatorado

- Arquivo: `Projeto Cafezinho Agentes/Foruns/PADRAO_OURO_AGENTE_v10.md`
- Atualizado: 2026-05-25 23:30 BRT
- Pontos principais:
  - Padrão Ouro de Agente Autônomo — v10 Refatorado
  - 1. FILOSOFIA ARQUITETURAL (O Que Mudou da v9 para v10)

### Fórum: Concepção do Agente Cobertura Flávio Bolsonaro (Monitoramento e Foco Negativo)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_agente_flavio_bolsonaro_20260525.md`
- Atualizado: 2026-05-25 23:19 BRT
- Pontos principais:
  - Fórum: Concepção do Agente Cobertura Flávio Bolsonaro (Monitoramento e Foco Negativo)
  - 🎙️ Solicitação Inicial (Miguel)

### Fórum: Concepção do Agente Escândalo (Varredura de Portais de Esquerda)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_agente_escandalo_20260525.md`
- Atualizado: 2026-05-25 19:52 BRT
- Pontos principais:
  - Fórum: Concepção do Agente Escândalo (Varredura de Portais de Esquerda)
  - 🎙️ Solicitação Inicial (Miguel)

### Fórum: Pesquisa de Preços, Velocidade e Qualidade — Todos os LLMs do Ecossistema

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_pesquisa_precos_llms_20260525.md`
- Atualizado: 2026-05-25 17:45 BRT
- Pontos principais:
  - Fórum: Pesquisa de Preços, Velocidade e Qualidade — Todos os LLMs do Ecossistema
  - 1. Sistema de Notas Proposto (Miguel)
  - Decisão operacional Codex: modelos ocidentais entram como banca, auditoria, qualidade, visão e casos especiais. Não devem virar motor diário de publicação em massa. Perplexity continua importante no Cafezinho, mas com fr

### Pesquisa Catálogo LLM — Zhipu AI / GLM

- Arquivo: `Projeto Cafezinho Agentes/Foruns/pesquisa_llm_glm_coding_20260525.md`
- Atualizado: 2026-05-25 17:26 BRT
- Pontos principais:
  - Pesquisa Catálogo LLM — Zhipu AI / GLM
  - 0. Visão Geral Zhipu AI

### 📋 Fórum de Governança Editorial: Consolidação, Diagnóstico e Roteiro do Loop de Qualidade

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_agente_qualidade_20260525.md`
- Atualizado: 2026-05-25 17:23 BRT
- Pontos principais:
  - 📋 Fórum de Governança Editorial: Consolidação, Diagnóstico e Roteiro do Loop de Qualidade
  - 🏛️ Introdução e Objetivo Editorial

### 🏗️ Sprint Refatoração Padrão Ouro — Agente Crime (Grupo 1)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_refatoracao_padrao_ouro_20260525.md`
- Atualizado: 2026-05-25 17:22 BRT
- Pontos principais:
  - 🏗️ Sprint Refatoração Padrão Ouro — Agente Crime (Grupo 1)
  - Objetivo

### Pesquisa Catálogo LLM — Moonshot/Kimi

- Arquivo: `Projeto Cafezinho Agentes/Foruns/pesquisa_llm_kimi_20260525.md`
- Atualizado: 2026-05-25 17:20 BRT
- Pontos principais:
  - Pesquisa Catálogo LLM — Moonshot/Kimi
  - 1. Resumo Executivo

### Pesquisa LLM — Codex Providers Ocidentais

- Arquivo: `Projeto Cafezinho Agentes/Foruns/pesquisa_llm_codex_ocidentais_20260525.md`
- Atualizado: 2026-05-25 17:20 BRT
- Pontos principais:
  - Pesquisa LLM — Codex Providers Ocidentais
  - 1. Resumo Executivo

### 🔬 Pesquisa: Catalogo Completo DeepSeek para Aiatolah + Roteador

- Arquivo: `Projeto Cafezinho Agentes/Foruns/pesquisa_llm_deepseek_20260525.md`
- Atualizado: 2026-05-25 17:16 BRT
- Pontos principais:
  - 🔬 Pesquisa: Catalogo Completo DeepSeek para Aiatolah + Roteador
  - Modelos ja catalogados (confirmados)

---

## 🧠 Cérebro / Trindade

### 📡 Canal Trindade (Claude ↔ Codex ↔ Antigravity)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/canal_trindade.md`
- Atualizado: 2026-05-27 13:51 BRT
- Pontos principais:
  - 📡 Canal Trindade (Claude ↔ Codex ↔ Antigravity)
  - [2026-05-24 19:32 BRT] Codex → Trindade / Sprints da noite movidas para fórum
  - Decisão: não prosseguir automaticamente. Precisa decidir qual é o WordPress canônico antes de instalar `wp_metrics.sh`. O `node_exporter` continua ativo; Fase D WP não foi aplicada.
  - Decisão de maestria:
  - Decisão: Fase D WordPress metrics segue congelada até ordem explícita. Se retomada, deve usar `WP_PATH=/var/www/ocafezinho` fixo e nunca varrer `/var/www/*`.

### Fórum — Sprint Memória de Trabalho dos Agentes

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_sprint_memoria_trabalho_20260527.md`
- Atualizado: 2026-05-27 02:31 BRT
- Pontos principais:
  - Fórum — Sprint Memória de Trabalho dos Agentes
  - 1. Problema
  - contexto das últimas horas se perde quando há crash;
  - Regra: se não couber em 3 bullets, o detalhe vai para fórum/memória de sprint.
  - próximo passo;

### Sub-Cérebro Antigravity & Miguel

- Arquivo: `Projeto Cafezinho Agentes/Foruns/sub_cerebro_antigravity_miguel.md`
- Atualizado: 2026-05-27 00:04 BRT
- Pontos principais:
  - Sub-Cérebro Antigravity & Miguel
  - 📜 10 Mandamentos de Segurança do Cérebro (Antigravity)

### Índice Histórico de Fóruns (Backup)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/INDICE_FORUNS_BACKUP.md`
- Atualizado: 2026-05-26 05:05 BRT
- Pontos principais:
  - Índice Histórico de Fóruns (Backup)
  - [Agente Apuracao de Preco LLM — Laboratorio GSN](Foruns/forum_agente_apuracao_preco_llm_20260519.md)

### Índice Semanal de Fóruns Ativos

- Arquivo: `Projeto Cafezinho Agentes/Foruns/INDICE_FORUNS_SEMANAL.md`
- Atualizado: 2026-05-26 05:05 BRT
- Pontos principais:
  - Índice Semanal de Fóruns Ativos
  - 📊 Painel de Status (KPIs)
  - Contexto: Miguel dividiu as frentes no canal Trindade às 23:15 BRT: Claude segue na Tríade China; Codex assume a criação do Agente Sobrenatural.

### Índice de Murais Históricos da Trindade

- Arquivo: `Projeto Cafezinho Agentes/Foruns/INDICE_DOS_MURAIS_HISTORICOS.md`
- Atualizado: 2026-05-26 05:05 BRT
- Pontos principais:
  - Índice de Murais Históricos da Trindade

### 🏛️ Fórum de Concepção Técnica: O Cérebro Vivo Autônomo (Living Brain V1)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_concepcao_cerebro_vivo_20260526.md`
- Atualizado: 2026-05-26 02:48 BRT
- Pontos principais:
  - 🏛️ Fórum de Concepção Técnica: O Cérebro Vivo Autônomo (Living Brain V1)
  - 🟢 SNAPSHOT DE DISCUSSÃO ARQUITETURAL — 2026-05-26 05:40 BRT
  - decisao = self.raciocinar_e_agir()

### 🏛️ Fórum de Concepção Arquitetural: O Conselho IA do Cafezinho (Decisão Editorial Democrática & Veto Soberano)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_conselho_ia_decisoes_editoriais_20260526.md`
- Atualizado: 2026-05-26 01:59 BRT
- Pontos principais:
  - 🏛️ Fórum de Concepção Arquitetural: O Conselho IA do Cafezinho (Decisão Editorial Democrática & Veto Soberano)
  - 🧭 1. Introdução e Visão Geral

### Fórum: Upgrade do Indexador Determinístico por Tags (Cérebro Leve V2)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_arquitetura_indice_foruns_tags_20260526.md`
- Atualizado: 2026-05-26 00:23 BRT
- Pontos principais:
  - Fórum: Upgrade do Indexador Determinístico por Tags (Cérebro Leve V2)
  - 🎙️ Contexto e Visão Geral
  - status: desenho_arquitetural

### Fórum: Protocolo de Comunicação Inbox/Outbox e Roteamento Dinâmico

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_protocolo_comunicacao_inbox_outbox_20260526.md`
- Atualizado: 2026-05-26 00:16 BRT
- Pontos principais:
  - Fórum: Protocolo de Comunicação Inbox/Outbox e Roteamento Dinâmico
  - 1. Carta pública à Trindade
  - Status:
  - Próximo passo:

### Fórum: Roteador Multimodal e Auditoria de Modelos Visuais (Wan vs. Flux vs. Ideogram)

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_roteador_multimodal_visual_20260526.md`
- Atualizado: 2026-05-26 00:06 BRT
- Pontos principais:
  - Fórum: Roteador Multimodal e Auditoria de Modelos Visuais (Wan vs. Flux vs. Ideogram)
  - 🔍 1. Análise de Impacto no Tribunal Visual (P0)

---

## 🌍 Geral / Outros

### FÓRUM — Diagnóstico de Performance e Travamentos do Computador do Miguel

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_diagnostico_hardware_miguel_20260527.md`
- Atualizado: 2026-05-27 13:48 BRT
- Pontos principais:
  - FÓRUM — Diagnóstico de Performance e Travamentos do Computador do Miguel
  - 1. Relato do Miguel
  - Próximo pico pode esgotar SWAP completamente → OOM killer → travamentos reais

### Sprint P0 — Trump tratado como ex-presidente em 2026

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_sprint_trump_expresidente_websearch_20260527.md`
- Atualizado: 2026-05-27 13:45 BRT
- Pontos principais:
  - Sprint P0 — Trump tratado como ex-presidente em 2026
  - Objetivo
  - regra: "em 2026, Donald Trump é presidente dos EUA; Joe Biden é ex-presidente".

### FÓRUM EMERGÊNCIA: Agentes Temáticos Bloqueados / Desbalanceamento Editorial

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_emergencia_agentes_bloqueados_20260526.md`
- Atualizado: 2026-05-27 11:10 BRT
- Pontos principais:
  - FÓRUM EMERGÊNCIA: Agentes Temáticos Bloqueados / Desbalanceamento Editorial
  - 1. DIAGNÓSTICO — 8 Problemas Identificados
  - Próximo ciclo: 10:00 BRT (coleta)
  - Status: **Já rodando em produção**
  - Próximo ciclo auditor: 15 minutos

### Fórum de Boas-Vindas — Grok Coding

- Arquivo: `Projeto Cafezinho Agentes/Foruns/forum_boas_vindas_grok_coding_20260525.md`
- Atualizado: 2026-05-25 19:19 BRT
- Pontos principais:
  - Fórum de Boas-Vindas — Grok Coding
  - 1. Visão Geral do Ecossistema

---

## ⚠️ Riscos e Bloqueios Operacionais

- Fóruns com palavras-chave de risco/bloqueio nas últimas 3 dias são listados nas seções acima.
- Verifique `AGENDA_PENDENCIAS_MIGUEL.md` para bloqueios que exigem decisão humana.
- Verifique `CEREBRO_NODE_BUGS.md` para bugs críticos ativos.

---

## 🔄 PROTOCOLO DE ATUALIZAÇÃO

**Quando atualizar este boletim:**
- Cada decisão Miguel (regra nova, ordem direta, alinhamento estratégico)
- Cada deploy crítico (produção, crontab, credencial, infra)
- Cada § Cérebro novo
- Cada bug crítico aberto/fechado
- Cada sprint passando de fase

**Como atualizar:**
- Regenere via `python3 root/gerar_boletim_news.py` (zero LLM)
- Editar manualmente somente para anotações pontuais que o algoritmo não capturou
- Sempre carimbar timestamp no rodapé

**Quem atualiza:**
- Qualquer agente pode rodar o script determinístico
- Auto-vigilância Trindade: se um boletim tem >24h, outro agente pode regenerar

**Tamanho-alvo:** <500 linhas, <25KB. Se passar, fazer auto-poda agressiva.

---

🤖 **Gerado:** 2026-05-27 14:00 BRT por `gerar_boletim_news.py`
🤖 **Próxima revisão:** próximo ciclo de `run_boletim_news.sh` ou agente que acordar

<!-- GERADO_AUTOMATICAMENTE: BOLETIM_NEWS_GERAL -->

## 🚨 CHECKUP-001 — Pausa total Tencent (2026-06-01 21:48 BRT)

Miguel iniciou noite de check-up e ordenou pausar tudo no Tencent, inclusive bots e robôs, para investigação da deterioração editorial/operacional e religamento gradual.

**Estado atual:** ecossistema Cafezinho/Trindade no Tencent em pausa total. Crontabs `root` e `ubuntu` sem linhas ativas; serviços `augusto`, `cctv-v5`, `cctv-editorial`, `zizi` e `websearch_proxy` inativos; nenhum processo do projeto vivo na validação final. Infraestrutura do servidor preservada.

**Backups de rollback:** `/root/crontab_backups_pause_all_20260601_213647/root.crontab.bak` e `/root/crontab_backups_pause_all_20260601_213647/ubuntu.crontab.bak`.

**Registro canônico:** `CEREBRO_NODE_CHECKUPS.md` → `CHECKUP-001`. Fórum: `Foruns/forum_investigacao_deterioracao_publicacao_20260601.md`.

**Regra:** não religar nada sem ordem explícita de Miguel, registro no fórum/canal, rollback e smoke por etapa.


## 📊 ORIENTAÇÃO DE MONITORAMENTO (adicionado 2026-05-27 16:10 BRT)

> Toda a Trindade deve saber fazer monitoramento. DeepSeek, Codex, Kimi, Qwen, GLM, Grok e Claude.

### Como monitorar

1. **Credenciais de servidores:** `MEMORIA_DEEPSEEK.md` §10 (DeepSeek) / `CLAUDE.md` §4 e §13 (Claude/Codex)
2. **Checklist de tick:** `Foruns/forum_loop_maestro_27mai2026.md` — formato padrão de tick
3. **Canal Trindade:** `Foruns/canal_trindade.md` — última janela 24h
4. **WP API:** `curl -u "Redator:..." "https://controle.ocafezinho.com/wp-json/wp/v2/posts?per_page=10&status=publish"`
5. **Logs remotos:** `ssh tencent "find /var/log -name '*.log' -mmin -30 -exec grep -l Traceback {} \;"`

### Tick rápido (5 passos)

```
1. Ler últimas ~40 linhas do canal Trindade
2. Ler último tick do loop maestro
3. ssh tencent "find /var/log -name '*.log' -mmin -30 -exec grep -l Traceback {} \;"
4. curl WP API → últimos 10 posts (detectar duplicatas, categorias)
5. Postar no canal: timestamp BRT + status (publicações, erros, agentes dormentes, duplicatas)
```

### Quem já sabe

- ✅ DeepSeek — credenciais em MEMORIA_DEEPSEEK.md §10
- ✅ Kimi — ativo no loop maestro 27/05
- ✅ Codex — acesso total aos servidores
- ⚠️ Qwen — precisa de orientação (Codex + DeepSeek vão orientar)
- ⚠️ GLM — pendente
- ⚠️ Grok — pendente
