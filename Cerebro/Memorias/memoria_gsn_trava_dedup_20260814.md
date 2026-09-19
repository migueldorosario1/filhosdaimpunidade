# Memória — GSN: sprint dedup 14/08/2026 (sessão ZCode GLM-5.3)

## Log técnico
- **Gatilho:** print do Miguel (14/08 14:33) mostrando 2 matérias quase iguais na home www.globalsouth.news sobre visto da embaixadora Maria Luiza Ribeiro Viotti.
- **Rastreio da fonte de publicação:** GitHub `global-south-news` stale em 13/08 23:01 → site tinha posts de 14/08 → busca por `*us-revokes*` no disco → verdadeira fonte: `Projeto Cafezinho Agentes/sites-v4/globalsouth/` (remote `git@github.com:migueldorosario1/globalsouth-v4.git`, `.vercel/project.json` = projeto `global-south-news`, push = deploy automático).
- **Arquivos:**
  - Removidos: `src/content/blog/20260814-us-revokes-brazil-ambassador-s-visa-in-escalating-diplomatic.md` + `public/hero/...in-escalating-diplomatic.jpg` (commit `dcac330`).
  - Editado: `scripts/gsn_publish_hourly_batch.mjs` (+~100 linhas; commit `0ee3fa7`): `STOPWORDS`, `titleTokens`, `titleSimilarity`, `findDuplicateTitle`, `heroLegendaSpam`; chamadas com veto duro dentro de `auditAndFix` quando `publish=true`, com log JSONL de bloqueio.
- **Testes:** `node --check` OK; similaridade BBC×Guardian 0,60 (≥0,55 bloqueia), Cuba colapso×restauro 0,08, Cuba×Turquia 0,00. Verificação ao vivo pós-deploy: URL antiga 404, mantida 200.
- **Ilustrações (verificadas via visão):** mantida = bandeiras internacionais (Pexels, ok p/ crise diplomática); removida = casal andando de costas com filtro sépia (Pixabay) + hero_legenda keyword-spam.

## O que falta / observação
- Monitorar `logs/gsn_publication_audit.jsonl` nas próximas rodadas do hourly por falsos-positivos em séries de follow-up (threshold ajustável via `GSN_DEDUP_THRESHOLD`).

## De que preciso do Miguel
- Nada agora. Se a trava segurar cobertura legítima de seguimento, recalibramos o threshold.
