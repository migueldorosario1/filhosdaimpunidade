# Cerebro: Indice Mestre - Global South News (GSN)

> [!NOTE]
> **DIRETRIZ DE RESOLUÇÃO DE CAMINHOS (CÉREBRO UNIFICADO):**
> Este arquivo faz parte do **Cérebro Unificado** (Cerebro).
> - **Localização Local:** `/home/migueldorosario/Downloads/Antigravity Google/Cerebro/`
> - **Localização no Servidor (Tencent/Alibaba):** `/root/Cerebro/` (ou `../Cerebro/` relativo aos diretórios de agentes).
> - **Resolução de Atalhos:** Qualquer link relativo no formato `../Cerebro/` aponta para esta pasta unificada, funcionando de maneira idêntica tanto localmente quanto nos servidores.
> - **Histórico da Reforma:** Detalhes em `Foruns/forum_organizacao_unificacao_cerebro_20260613.md`.


Este é o índice principal do ecossistema autônomo, de hospedagem e do painel editorial do portal **Global South News (GSN)**, isolado de qualquer outro projeto do workspace.

---

## 0. Ficha Viva Obrigatória — Arquitetura Real do GSN

Esta seção deve ser consultada antes de qualquer diagnóstico, ajuste de acesso, deploy ou criação de novos agentes do GSN.

### Resumo Curto
Global South News (GSN) é um site de jornalismo geopolítico **Astro/Markdown publicado via GitHub -> Vercel**. Este é o caminho canônico de publicação pública.

**Regra operacional:** não tratar Droplet/SSH como deploy do site público do GSN. Qualquer script antigo de deploy direto para Droplet é legado e não deve ser usado sem nova autorização explícita do Miguel.


### ⚠️ ERRATA 2026-07-27 (Miguel, via ZCode/Kimi)

**Executor GSN não é mais Beijing.** Miguel: "GSN não está em Beijing, todo mundo está em NYC hoje." Confirmado em verificação direta: `/root/agente_curadoria_gsn.py` e `/root/gsn_remote/` presentes no NYC (198.199.121.136); Beijing (82.156.167.218) inacessível/timeout em 27/07. A seção "Executor Cloud" acima está DESATUALIZADA — executor vigente: **NYC**. Chaves de indexação por portal em `/root/agent_data/indexing_keys/` (NYC), cada portal com projeto Google Cloud próprio (verificado via API Search Console).

### Executor Cloud dos Agentes GSN

**Executor canônico dos agentes GSN:** Tencent Beijing `82.156.167.218`, usuário `ubuntu`, diretório `/home/ubuntu/gsn_agentes/`.

Este servidor é o lugar correto para rodar agentes automáticos do GSN em nuvem. Não confundir:

- **Publicação pública do site:** GitHub `migueldorosario1/global-south-news` -> Vercel.
- **Execução dos agentes:** Tencent Beijing `82.156.167.218` -> gera Markdown/assets -> `git push` -> Vercel publica.
- **NYC antigo:** legado/indisponível para esta frente.
- **Computador local `novo`:** pode servir para desenvolvimento/teste, mas não deve ser executor recorrente do GSN.
- **Alibaba Beijing:** casa do Cérebro/Kimi, não executor canônico do GSN.

**Confirmação Codex 2026-05-21 13:30 BRT:** SSH read-only em `ubuntu@82.156.167.218` confirmou o host `VM-0-16-ubuntu` e o diretório `/home/ubuntu/gsn_agentes/`, com agentes GSN e pipeline `gsn_smoke_pipeline.py` presentes. Os scripts específicos do YouTube (`gsn_agente_youtube.py`, `gsn_agente_youtube_publicador.py`, `gsn_youtube_inbox.py`) ainda não foram encontrados nesse diretório na checagem; antes de qualquer cron YouTube, eles precisam ser instalados/sincronizados e auditados no executor Beijing.

**Regra para agentes da Trindade:** antes de perguntar "onde roda o GSN" ou inferir por memória, consultar esta ficha. Se houver conflito entre lembrança, canal antigo e Cérebro, parar e pedir auditoria do Maestro.

### Stack Tecnológica & Fluxo de Publicação
1. **Frontend:** Astro (Headless estático, ultra-rápido, otimizado para SEO).
2. **Hospedagem:** Vercel (Hospeda o frontend estático compilado diretamente do repositório).
3. **Repositório GitHub:** `migueldorosario1/global-south-news`.
4. **"Banco de Dados" Vivo:** Arquivos Markdown (`.md`) salvos diretamente sob `src/content/blog/`.
5. **Publicação:** agentes geram Markdown/assets no repo e fazem `git push`; a Vercel publica pelo webhook do GitHub.
6. **Painéis/rotas antigas:** qualquer painel Flask/Droplet citado em registros antigos deve ser considerado legado até nova auditoria.

---

## 🔑 Infraestrutura

*   **Site público:** GitHub `migueldorosario1/global-south-news` -> Vercel.
*   **Repo local Astro:** `Global South News/gsn/`.
*   **Silo de agentes:** `Global South News/root/`.
*   **Segredos locais de agentes:** `Global South News/root/chaves_gsn.env`.
*   **Banco de mídia local do silo:** `Global South News/root/agent_data/banco_midia/banco_imagens_reais.db`.

---

## 🤖 Agentes Autônomos GSN (Silo Root)

Os scripts e agentes do GSN estão localizados no diretório `/home/migueldorosario/Downloads/Antigravity Google/Global South News/root/` e mantêm o prefixo `gsn_`.

*   **Painel Editorial Flask:** [gsn_admin.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_admin.py)
    *   *Função:* Interface visual premium (Visual Editor / Quill + Código HTML), traduzida em inglês com paleta "Dark Diplomat".
*   **Agente Master (Trends V9):** [gsn_agente_master.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_agente_master.py)
*   **Robô de Coleta Bruta:** [gsn_robo_coleta.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_robo_coleta.py)
*   **Agente Comentarista (Enxame):** [gsn_agente_comentarista.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_agente_comentarista.py)
    *   *10/08/2026 — Regra do AUTOR:* persona proibida de responder na 1ª pessoa do autor (bug: Chico/Francisco de Assis respondeu "eu não conheço o Ceará" a comentário dirigido ao Miguel). Fórum: `Foruns/forum_comentarista_regra_autor_primeira_pessoa_20260810.md`.
*   **Agente Injetor Premium:** [gsn_agente_injetor_premium.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_agente_injetor_premium.py)
*   **Gerador de Markdown (Vigias):** [gsn_smoke_markdown.py](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_smoke_markdown.py)

---

## ⚙️ Configurações & Dependências

*   **Arquivo de Chaves:** [chaves_gsn.env](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/chaves_gsn.env)
*   **Fila de Postagem Social:** [gsn_social_queue.json](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/agent_data/gsn_social_queue.json)
*   **Banco de Dados Local do Painel:** `root/admin_db.json` (Registra títulos, autores, timestamps e status de rascunho/publicado).
*   **Personas de Comentários:** [gsn_personas_comentarios.json](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/agent_data/gsn_personas_comentarios.json)
*   **Astro Config Schema:** [content.config.ts](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/gsn/src/content.config.ts)

---

## 📁 Custom GSN Taxonomy & Schema

Toda matéria gravada em `src/content/blog/` contém a seguinte estrutura canônica de frontmatter:
```yaml
---
title: "Title of the geopolitical brief"
description: "SEO summary sub-headline"
pubDate: "ISO timestamp format"
categoria_macro: "Geopolitics | BRICS | Development | Latin America etc."
tags: ["trade", "development", "multipolar-world"]
heroImage: "/hero/slug.jpg"
author: "Global South News Desk"
lang: "en"
draft: true | false
---
```

---

## 🚫 Conteúdo Proibido (Ban a Conteúdo Doméstico Brasileiro)

1. **Ban em Notícias de Polícia/Política Interna do Brasil:** É expressamente proibida a publicação de matérias referentes a operações policiais domésticas brasileiras (ex: operações da Polícia Federal, investigações da Polícia Civil, apreensões locais, como "Operação Sem Refino") e escândalos de corrupção ou disputas políticas internas brasileiras (envolvendo governadores, deputados, prefeitos, ex-presidentes, etc.) que não tenham impacto geopolítico ou macroeconômico diplomático internacional direto de nível global.
2. **Foco Internacional:** O portal **Global South News** é direcionado estritamente ao público internacional em língua inglesa. O conteúdo deve ser de geopolítica internacional, multilateralismo (BRICS, Sul-Sul, etc.), infraestrutura de integração regional global, e soberania do Sul Global.
3. **Filtro de Idioma e Localidade:** Toda coleta realizada pelos robôs (`gsn_robo_coleta.py`, `gsn_publicador_tematicos.py`) deve ter filtros rigorosos ativados para descartar qualquer conteúdo em língua portuguesa de notícias locais brasileiras.

---

## 🚀 Publicação Canônica

O publicador vivo do GSN deve terminar em commit/push no repositório Astro:

*   [gsn_remote_publish.sh](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/gsn_remote_publish.sh)
    *   *Função:* atualizar repo, rodar autocura/smoke, gerar Markdown/assets e publicar via GitHub -> Vercel.

### Legacy

O antigo `deploy_gsn.sh` de Droplet/DigitalOcean foi movido para:

*   [deploy_gsn_droplet_legacy.sh](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/legacy/deploy_gsn_droplet_legacy.sh)

Não usar esse script para publicação pública do GSN.

---

## 📰 Registros de Linha Editorial & Incidentes (Camada 3)

*Catálogo dos fóruns/memórias vivos do GSN (Regra do Tema Duplo — novos registros entram AQUI, nunca no Index Master).*

| Data | Registro | Tema |
|---|---|---|
| 2026-09-19 | `Foruns/forum_gsn_headless_corte_agentes_20260919.md` + `Memorias/memoria_gsn_headless_corte_agentes_20260919.md` | **Corte da via dos agentes pós-migração headless:** wp-json do NYC 401/404 (WP legado deprecado no `.env.unificado`; canônico = Astro/GitHub→Vercel). Missão do Antigravity (editorial BRICS Paulo Nogueira; Cafezinho ok mas EM TRIPLICATA 272237/272239/272244; GSN falhou) entregue ao ZM — prompt `Foruns/ponte_laura_completa/PROMPT_ZM_GSN_HEADLESS_BRICS_20260919.md`, ref ponte ZM-20260919-001. **AGUARDA execução de sessão ZM livre** |
| 2026-08-05 | `Foruns/forum_gsn_pt_campnou_publicador_gate_20260805.md` + `Memorias/memoria_gsn_pt_campnou_publicador_gate_20260805.md` | Recaída PT no ar (Camp Nou 02/08 + Níger 30/07): itens pré-gate dormiram na fila e o **publicador** publicou sem revalidar. Cura: gate `V4_PATCH_GSN_EN_PUBLICADOR_20260805` nas DUAS pontas + veto URL `/sports/` + purga fila (36→31); Níger republicado EN |
| 2026-07-29 | `Foruns/forum_gsn_colunistas_priscila_20260729.md` + `Memorias/memoria_gsn_colunistas_priscila_20260729.md` | Seção **Colunistas**: submenu Editorial→Columnists (flyout), páginas `/colunistas/[autor]`, `categoria_macro: "Priscila Miranda"` nos 3 posts dela (commit `f2edc9c`) |
| 2026-07-29 | `Foruns/forum_gsn_linha_editorial_diretriz_20260729.md` | **LINHA EDITORIAL CONSOLIDADA (canônica):** EN-only, geopolítica dura anti-imperialista pró-Irã/China/Rússia/Brasil/Sul Global + tech estratégica; veto pauta mole; legado mole antigo PERMANECE (já indexado) — decisão Miguel |
| 2026-07-29 | `Foruns/forum_gsn_pauta_mole_pt_20260729.md` + `Memorias/memoria_gsn_pauta_mole_pt_20260729.md` | Incidente: post PT + pauta mole no ar — quem escolheu (piloto automático), derrubada, gates `V4_PATCH_GSN_EN_LINHA_20260729` |
| 2026-08-05 | `CEREBRO_NODE_BUGS_RESOLVIDOS.md` → `BUG-20260802-1323-GSN-PT-PUBLICADOR-SEM-GATE` | Bug resolvido: gates agora nas DUAS pontas da esteira (produção + publicação); lição: fila intermediária é zona cega |
| 2026-07-29 | `CEREBRO_NODE_BUGS_RESOLVIDOS.md` → `BUG-20260729-0300-GSN-PT-PAUTA-MOLE` | Bug resolvido com cura estrutural (trava idioma + gate editorial) |
| 2026-07-23 | `Foruns/forum_gsn_post_sem_imagem_20260723.md` + `Memorias/memoria_gsn_post_sem_imagem_20260723.md` | Post sem imagem — cura em 4 camadas + guarda prebuild |

---

## 🔗 Redundância & Atalhos de Acesso Rápido

Para facilidade de localização e segurança contra perda de dados em outros agentes ou LLMs, este índice e suas referências estão espelhados em:
1.  **Índice de Produção:** [CEREBRO_INDEX_GSN.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/CEREBRO_INDEX_GSN.md)
2.  **Diretório de Scripts:** [CEREBRO_INDEX_GSN.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Global%20South%20News/root/CEREBRO_INDEX_GSN.md)
3.  **Workspace Geral de Agentes:** [CEREBRO_INDEX_GSN.md](file:///home/migueldorosario/Downloads/Antigravity%20Google/Projeto%20Cafezinho%20Agentes/CEREBRO_INDEX_GSN.md)

---

## 🛡️ Infrastructure Decommissioning & Sanitization Certificate

### 📜 Certificate of Completion
- **Project:** Global South News (GSN) Headless Migration & Decommissioning
- **Status:** **APPROVED & FULLY DECOMMISSIONED**
- **Date:** 2026-06-12 (Z)
- **Authorized Nodes:**
  - **Beijing Node (82.156.167.218):** Autonomous GitOps publishing node. Verified 100% clean of database files, PHP/WordPress runtimes, and local SQL exports. Disk usage is healthy (~52% capacity).
  - **NYC Droplet (198.199.121.136):** Deprecated WordPress host. Confirmed that the domain DNS of `globalsouth.news` points to Vercel (`76.76.21.21`), bypassing NYC completely. All legacy WordPress configurations, database parameters, and API keys are commented out/disabled on `nyc` and `beijing` nodes.
- **Verification of Pipeline Integrity:**
  - `gsn_zelador_destaques.py` has been verified as operating cleanly without residual JSON staging artifact dependencies.
  - No active WordPress-dependent crons run on the Beijing node.
  - Headless GitOps queue execution via `gsn_hourly_cron.sh` and continuous Vercel integration is fully operational.
