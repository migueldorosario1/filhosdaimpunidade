# MEMÓRIA — Temáticos: destaques por audiência GA4 + fix hero Ceará (05/08/2026)

**Data:** 2026-08-05 01:00→01:40 BRT · **Agente:** ZCode/Kimi K3
**Fórum irmão:** `Foruns/forum_tematicos_destaques_ga4_20260805.md`

## 1. Diagnóstico técnico completo

### 1.1 Imagem quebrada (card Ciro, ceara.digital)
- Home ao vivo referenciava `/hero/20260721-ciro-gomes-lanca-pre-candidatura-ao-governo-do-ceara-com-cri.jpg` → **404**; arquivo real: `/hero/ciro-gomes-…-cri.jpg` (sem prefixo de data) → 200.
- Origem da referência errada: `src/data/destaques.json` (seção estática da home), entrada escrita à mão.
- **Split-brain de repo (mesmo padrão do GSN):** site no ar = repo `migueldorosario1/ceara-v4` (checkout local `Projeto Cafezinho Agentes/sites-v4/ceara`, pipeline V4 local, cron `0 */8` orquestrador `--site ceara`). O NYC `/root/cicero_remote/ceara-digital` (cron 9:15) empurra o repo ANTIGO `ceara-digital` — fora do ar. O zelador de sticky (`ceara_zelador_destaques.py`) roda no repo morto e não afeta o site real.

### 1.2 Destaques congelados
- `src/pages/index.astro` dos temáticos importa `../data/destaques.json` (seção `fv-grid`; `li:first-child` = manchete grande). O feed usa a collection (automático). JSON manual com 2 commits na história → congelado desde 21-22/07.
- `onerror` fallback do feed existe (`/images/fallback_ceara.png`) mas a seção de destaques (`fv-img`) **não tem** onerror — por isso o card quebrado aparecia como alt-text.

## 2. Implementação — `agentes_tematicos/v4/ga4_destaques.py`

- **GA4 Data API** (`google-analytics-data`, já instalada no pyenv 3.10.13 local): `RunReportRequest` dimension `pagePath`, metric `screenPageViews`, filter CONTAINS `/blog/`, order desc, janela `7daysAgo`→`today` (fallback `28daysAgo`).
- **Credencial:** `GA4_KEYFILE` env ou default `/home/migueldorosario/Dados_Frios/Agentes Labs/keys/ga4.json` (SA `augusto-arquivista@gen-lang-client-0200069757…` — testada ao vivo contra a property do Ceará: lê tudo).
- **Properties (CEREBRO_NODE_TELEMETRIA §4):** mundotrilhos 546667776 · discoverbrazil 546669474 · riocarta 546673810 · ceara 546675232 · aiatolah 546675625 · globalsouth 546677232 · railpost 546679970 · mapario — sem property conhecida.
- **Montagem da entrada:** slug do path → `src/content/blog/<slug>.md` → frontmatter (title/description/heroImage/author/categoria_macro). Kicker = categoria_macro prettificado (mapa PT + title-case). Hero validada em `public/` (URL http externa passa direto — riocarta legacy usa r2.dev). Drafts fora.
- **Padding:** audiência primeiro; se <5 elegíveis, completa com recentes (`fonte` registrada como `…+recencia_padding`). Sem audiência alguma → 100% recentes (`recencia_sem_audiencia`).
- **Git:** pull --ff-only → escreve → commit `chore(destaques): por audiencia GA4 (fonte, N views)` → push; pula se JSON inalterado; falha de push só loga (não derruba rodada).
- **Cron local:** `45 3,13 * * *` (após o orquestrador V4 das 03:00/13:00) → log `agent_data/v4/ga4_destaques.log`.

## 3. Rodada de estreia (01:26 BRT) e verificação

6/6 repos com destaques.json atualizados e pushed (tabela no fórum). ceara.digital verificado ao vivo ~01:29: manchete "Quem é Elmano de Freitas…" (3 views, #1 do 28d), **5/5 heroes HTTP 200**, card quebrado extinto.

## 4. Fix avulso anterior

`destaques.json` do ceara: hero do card Ciro corrigida à mão (commit `36752cf`) ANTES do gerador entrar — resposta imediata ao "corrige".

## 5. Pendências / riscos

- aiatolah + mapario sem seção Destaques — criar? (decisão Miguel). mapario sem property GA4 conhecida.
- Feedback loop da manchete (mais vista se perpetua): janela 7d mitiga; decay futuro se necessário.
- Cron NYC `ceara_hourly_cron.sh` (repo morto) roda à toa — candidato a DESLIGADO_… (ordem Miguel pendente).
- Lição reutilizável: **toda seção editorial estática precisa de gerador automático ou vira "destaque parado"**; e sempre validar hero no disco antes de referenciar.
