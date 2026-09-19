# Fórum — Core Web Vitals Mobile (O Cafezinho) — Diagnóstico

**Data:** 2026-08-11 ~09:15 BRT
**Agente:** ZCode (GLM-5.2 Z.ai)
**Fonte:** Relatório CWV do GSC (agregado 28 dias) + medições em tempo real + diagnóstico de servidor via SSH

## Estado atual (09/08/2026)
- Total URLs avaliadas: **9.032** (mobile)
- ✅ **Bom: 5.304 (58%)**
- 🟡 Melhorias necessárias: 3.318 (36%) — **CLS > 0,1**
- 🔴 Ruins: 410 (4%) — **LCP > 4s**

## Evolução importante (boa notícia histórica)
- **Evento 16/06:** "Bom" saltou de 351 → 13.878 URLs num dia (mudança de tema/otimização entrou — provável reforma visual do Cafezinho).
- **Pico "Bom":** 15.224 URLs em 21/06 (69%).
- "Ruins" (LCP>4s) só apareceu em 29/06 — **antes era zero**. Ou seja, a situação atual de LCP é piora recente, recuperável.

## Diagnóstico raiz (medido em produção)

### Problema nº 1: LCP > 4s (410 URLs ruins) — CAUSA: TTFB alto
- **Home (cacheada): TTFB 0,55s** ✅
- **Posts (não cacheados): TTFB 5,5s** 🔴 (10x mais lento)
- O LCP é puxado pelo servidor demorando pra responder.

### Causa raiz do TTFB alto: MySQL sobrecarregado
- **MySQL: 204% CPU** (2 núcleos inteiros!) + **1,8 GB RAM**
- Load average: **3,87** (servidor de 8 núcleos — não é crítico mas MySQL é o gargalo)
- RAM: 4,2/7,8 GB usados + **2,3 GB em swap** (pressão de memória)

### Banco de dados inchado
| Tabela | Tamanho | Linhas |
|--------|---------|--------|
| wp_wffilemods (Wordfence) | **855 MB** | 1,3M |
| wp_posts | 518 MB | 201k |
| wp_wfknownfilelist (Wordfence) | 393 MB | 1,3M |
| wp_postmeta | 274 MB | 1,3M |
| wp_comments | 259 MB | 625k |
| wp_evermonitor_event_queue | 194 MB | 159k |
| wp_commentmeta | 119 MB | 989k |

- **Posts publicados: 77.760**
- Revisões: 834 (ok, baixo)
- **Wordfence sozinho ocupa ~1,25 GB** (wffilemods + wfknownfilelist) — peso enorme no DB.

### Problema nº 2: CLS > 0,1 (3.318 URLs) — layout shift
- Provavelmente causado por: anúncios/ads sem dimensões reservadas, imagens sem width/height, fontes web carregando tarde.
- Não medi ainda (precisa PageSpeed Insights em URL específica).

## Plano de ação recomendado (por impacto, do maior pro menor)

### 🔴 PRIORIDADE 1 — Curar TTFB/LCP (ataca as 410 URLs ruins + previne piora)
1. **Otimizar MySQL:** indexação, query cache, buffer pool. Ajustar `innodb_buffer_pool_size` (tem 1,8GB em uso → reservar ~3GB dedicados).
2. **Aumentar cache WP Rocket:** pré-carregar (preload) os posts populares. Configurar cache de consultas de banco.
3. **Redis Cache:** confirmar que está cacheando queries (já ativo, mas o MySQL ainda bate 204% — verificar se Redis está efetivo).
4. **PHP-FPM tuning:** 69 processos é muito para 8 núcleos/7,8GB. Ajustar `pm.max_children`.

### 🟡 PRIORIDADE 2 — Limpar banco de dados (reduz carga do MySQL)
1. **Wordfence (1,25 GB):** limpar `wp_wffilemods` e `wp_wfknownfilelist` (tabelas de scan que incham). Reduzir frequência de scan.
2. **wp_comments/wp_commentmeta (378 MB):** limpar spam/antigos. 625k comentários é muito.
3. **wp_evermonitor_event_queue (194 MB):** verificar se pode ser limpa (fila de eventos).
4. **Otimizar tabelas:** `wp db optimize` (reclama espaço).

### 🟢 PRIORIDADE 3 — Resolver CLS (3.318 URLs)
1. Garantir `width`/`height` em todas as imagens (evita reflow).
2. Reservar espaço para anúncios (ad slots com dimensão fixa).
3. `font-display: swap` nas fontes web.

## Estado / O que falta / Próximos passos
- **Feito:** diagnóstico completo raiz (servidor + DB + CWV).
- **Decisão do Miguel necessária:** qual prioridade atacar primeiro? Recomendo **PRIORIDADE 1** (TTFB/LCP) — é a que tem 410 URLs "ruins" e afeta diretamente ranking + experiência.
- **Não fiz:** nenhuma mudança em produção (só diagnóstico leitura). Aguardando decisão do Miguel.
