# Cerebro: Índice Mestre — Ceará Digital

> Criado em 21/07/2026 por ZCode (Kimi). Gap identificado: o Ceará Digital não tinha índice próprio no Cérebro (só menções em fóruns). Este é o ponto único de retomada do site.

## 0. Ficha viva obrigatória

- **Site**: Ceará Digital — portal de política e notícias do Ceará.
- **Domínio**: `https://ceara.digital` (HTTP 200 validado em 20/07/2026).
- **Stack**: Astro/Markdown, content collection `src/content/blog/`, posts em `/blog/{slug}/`.
- **Repo GitHub**: `migueldorosario1/ceara-v4` (branch `main`).
- **Projeto Vercel**: **`cicero`** — pegadinha de nome: o domínio `ceara.digital` é servido pelo projeto `cicero`, não por um projeto "ceara".
- **Deploy**: push na `main` → GitOps Vercel automático.
- **Checkout local**: `/home/migueldorosario/Downloads/Antigravity Google/Projeto Cafezinho Agentes/sites-v4/ceara`.
- **Config**: `~/Downloads/Antigravity Google/agent_data/configs/ceara.json`.
- **Contrato editorial**: `~/Downloads/Antigravity Google/agent_data/contratos/ceara.md`.
- **Pipeline**: `~/Downloads/Antigravity Google/agentes_tematicos/v4/` — `orquestrador.py --site ceara` (coletor → produtor → youtube → publicador). Python 3.10.13 via pyenv.
- **Indexação Google**: chave `gcloud_indexing_keys/ceara.json` (indexing habilitado no config).
- **O que NÃO é**: não é WordPress; não usa o Droplet do Rio Carta legado.

## 1. Linha editorial (diretriz Miguel 21/07/2026)

Progressista assumida. Prioridade absoluta: **política cearense e eleições 2026**.
- Construtivo: Elmano de Freitas (PT), Camilo Santana (PT), Luizianne Lins (PT).
- Oposição com destaque: Ciro Gomes, André Fernandes (PL), PL/bolsonarismo CE — só fatos verificáveis.
- Pesquisas: só com instituto + registro TSE + data de campo + margem.
- Zero invenção; fonte nominal + link; sem ataque a vida privada.
- Fórum canônico da mudança: `../Projeto Cafezinho Agentes/Foruns/forum_diretriz_editorial_politica_ceara_riocarta_20260721.md` (caminho real: `cerebro-miguel/projeto_cafezinho_agentes/foruns/`).

## 2. Autonomia e ritmo

- Publicação **automática ao vivo** (sem draft), diretriz Miguel 21/07/2026.
- Cron dedicado: `0 */8 * * * orquestrador.py --site ceara` (00h/08h/16h) + rodadas `--all` às 03h/13h.
- `posts_por_rodada: 2`, `auditor_threshold: 40`.

## 3. Histórico

- **20/07/2026**: refatoração V4 — repo migrado de `ceara-digital-astro` para `ceara-v4`; Vercel `cicero` religada via API (DELETE/POST `/v9/projects/{proj}/link`); backup em `Backups/refatoracao_v4_tematicos_20260720_171637`. Log: `forum_refatoracao_sistema_sites_tematicos_20260720.md` + `MANIFESTO_REFATORACAO_V4_20260720.md`.
- **21/07/2026**: nova linha editorial político-eleitoral aplicada (contrato + config + cron 8h).

## 4. Pendências conhecidas

- Posts publicados antes de 20/07 podem ter URLs erradas indexadas no Google (bug `/{slug}/` vs `/blog/{slug}/` corrigido no publicador).
- Token `ghp_OKTA...` exposto em remotes antigos precisa ser rotacionado (pendência geral da refatoração).
- Propagar AdSense do riocarta para os demais sites (pendência geral).
