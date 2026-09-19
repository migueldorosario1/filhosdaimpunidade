# 💌 Cartinha da Kimi — Resultado do Smoke Test: Coletor Nacional

**Data:** 14 de junho de 2026, ~08:45 BRT  
**De:** Kimi (Maestro Diagnóstico)  
**Para:** DeepSeek & Miguel  
**Assunto:** Smoke test local concluído — números e análise

---

Oi! 👋

Smoke test do coletor nacional executado. Aqui vão os números:

---

## ✅ Resultado Geral: SUCESSO

O coletor funcionou. Pautas coletadas, filtradas, scored com granularidade real. Zero erros críticos.

---

## 📊 Números do Smoke Test

| Métrica | Valor |
|---------|-------|
| **Pautas brutas coletadas** | 193 |
| **Feeds RSS acessados** | 20 |
| **Feeds com erro** | 1 (diariodocentrodomundo.com.br — timeout) |
| **Duplicatas exatas** | 2 descartadas |
| **Sem keyword match** | 130 descartadas |
| **Keyword negativa** | 5 descartadas |
| **Pautas inéditas** | 56 |
| **Aprovadas no scoring** | 4 (score 0.80) |
| **Rejeitadas por score baixo** | 21 (scores de 0.10 a 0.70) |
| **Inseridas (dry-run)** | 4 (limite --max 5) |
| **Latência total** | **40 segundos** |

---

## 🎯 Comparativo com Geopolítica

| Métrica | Geopolítica | Nacional |
|---------|-------------|----------|
| Pautas brutas | 290 | 193 |
| Feeds com erro | 3 (7,9%) | 1 (5%) |
| Inéditas | 39 | 56 |
| Aprovadas | 25 | 4 |
| Latência | 1m32s | **40s** |
| Score granular | ❌ Flat (0.80) | ✅ Variado (0.10–0.80) |

---

## ✅ O que funcionou MELHOR no Nacional

### 1. Scoring granular
O nacional mostra scores reais: 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80.  
Isso é muito melhor que o geopolítica, que aprovou tudo com 0.80 flat.

### 2. Menor latência
40 segundos vs 1m32s. Menos feeds (20 vs 38), mas todos brasileiros — latência de rede menor.

### 3. Menos feeds mortos
Só 1 feed com erro (5%) vs 3 no geopolítica (7,9%).

---

## ⚠️ O que precisa de atenção

### 1. Apenas 4 aprovadas (7% das inéditas)
Das 56 inéditas, só 4 passaram no score 0.80. Isso é **muito seletivo**.

Possíveis causas:
- Score mínimo 0.80 pode ser alto demais para notícias nacionais
- Keywords podem ser muito específicas
- O LLM de scoring pode estar sendo muito rigoroso

### 2. 21 rejeitadas com scores baixos
Várias pautas sobre Lula, Bolsonaro, eleições foram rejeitadas com scores 0.20–0.70.  
Isso é intencional? A diretriz nacional prioriza "diálogo governo-congresso", "reforma tributária", "agenda legislativa" — talvez as pautas rejeitadas fossem "política de fofoca" em vez de "política de governo".

---

## 🎯 Veredito do Smoke Test

| Critério | Resultado | Status |
|----------|-----------|--------|
| Coleta funciona | 193 pautas, 19/20 feeds OK | ✅ PASSOU |
| Dedup funciona | 2 duplicatas descartadas | ✅ PASSOU |
| Latência aceitável | 40s total | ✅ PASSOU |
| Score granular | Scores de 0.10 a 0.80 | ✅ PASSOU |
| Schema respeitado | DRY-RUN inseriu 4 pautas | ✅ PASSOU |

---

## 🚀 Próximo Passo Sugerido

1. **Avaliar se score 0.80 não é alto demais** para nacional — talvez 0.70 seja mais realista
2. **Comparar com o legado** — quantas pautas o `robo_coleta_nacional.py` aprovava por rodada?
3. **Quando aprovado, rodar SEM dry-run** — inserir no banco local

---

Pronto para a próxima ordem! 🎯

— Kimi
