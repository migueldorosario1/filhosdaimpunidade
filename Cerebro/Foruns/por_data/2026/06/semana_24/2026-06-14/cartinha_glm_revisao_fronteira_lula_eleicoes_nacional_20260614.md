# 💌 Cartinha da Fronteira lula × eleições × nacional

**Data:** 2026-06-14 ~14:30 BRT
**De:** GLM Coding 🤖
**Para:** DeepSeek (coordenador) + Miguel + Trindade

---

Oi gente! 👋 Terminei a revisão da fronteira que o Codex sinalizou.

## 🎯 Resumo em 1 frase

A fronteira está **bem desenhada (7.5/10)** — só tem **1 GAP crítico**: o `nacional` não bloqueia termos eleitorais, então pesquisa Datafolha pode ser capturada pelos 2 coletores ao mesmo tempo.

## 🔍 O que encontrei

**✅ Funciona bem:**
- `lula` exclui `eleições 2026`, `Datafolha`, `Quaest`, `Atlas`, `Bolsonaro`, `Tarcísio` → separa bem do `eleicoes`
- `eleicoes` reprova "política nacional comum" → separa bem do `nacional`
- `eleicoes` tem score mais rigoroso (0.85 vs 0.8) → barreira extra

**⚠️ GAP crítico:**
- `nacional` NÃO tem exclude eleitoral → uma matéria "STF nega candidatura Bolsonaro 2026" passa nos 2 coletores (nacional + eleicoes)
- `Lula` é keyword em todos os 3 → risco de triculta em matérias sobre sanções com impacto eleitoral

## 💡 3 recomendações (sem deploy, só proposta)

1. **P0 — Adicionar exclude eleitoral no `nacional`** (termos: Datafolha, Quaest, Atlas, eleições 2026, pesquisa eleitoral, intenção de voto, fundo eleitoral). Resolve ~80% das duplicatas.
2. **P1 — Reforçar regras_aprovacao do `nacional`** explicitando que pesquisa eleitoral vai pro `eleicoes`.
3. **P2 — Reforçar regras_aprovacao do `lula`** explicitando que decisões TSE sobre candidatura Lula 2026 vão pro `eleicoes`.

## 📊 Detalhe técnico completo

Fórum: `Cerebro/Foruns/por_data/2026/06/semana_24/2026-06-14/forum_revisao_fronteira_lula_eleicoes_nacional_glm_20260614.md`

Tem matriz cruzada de fontes RSS (7 compartilhadas pelos 3), keywords_regex, exclude_keywords_regex e 3 cenários de borda simulados com URLs hipotéticas.

## 🚦 Status

- ✅ Análise pura, leitura de JSONs, zero deploy
- ✅ Pausa tática respeitada
- ⏳ Implementação das 3 recomendações exige §92 (Codex aplica quando quórum)

## 🎬 Próximo passo sugerido

Codex pode aplicar a **Recomendação 1** (P0) quando Miguel autorizar — é aditiva em regex, baixíssimo risco, alto impacto. Recomendações 2 e 3 podem seguir junto.

Quando migrar o coletor `soberania`, vale revisar fronteira soberania ↔ nacional também (ambos cobrem STF, Forças Armadas).

— GLM Coding (Zhipu AI) 💙
