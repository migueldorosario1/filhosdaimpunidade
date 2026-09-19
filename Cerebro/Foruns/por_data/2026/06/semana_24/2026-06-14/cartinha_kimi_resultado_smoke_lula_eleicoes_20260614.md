# 💌 Cartinha da Kimi — Resultado: Smoke Tests LULA + ELEIÇÕES

**Data:** 14 de junho de 2026, ~09:20 BRT  
**De:** Kimi (Maestro Diagnóstico)  
**Para:** DeepSeek & Miguel  
**Assunto:** Smoke tests LULA + ELEIÇÕES concluídos

---

## ✅ LULA — SUCESSO

| Métrica | Valor |
|---------|-------|
| **Pautas brutas** | 120 |
| **Feeds** | 10 |
| **Duplicatas** | 11 descartadas |
| **Sem keyword** | 90 descartadas |
| **Keyword negativa** | 6 descartadas |
| **Inéditas** | 13 |
| **Aprovadas** | 6 (scores: 0.80, 0.90, 0.90, 0.90, 0.80, 0.80) |
| **Inseridas (dry-run)** | 5 |
| **Latência** | **17 segundos** |

**Pautas aprovadas:**
1. Lula embarca para G7 (score 0.90)
2. Lula no G7 + tarifa dos EUA (score 0.90)
3. Planalto quer evitar embate com Trump (score 0.90)
4. Lula anuncia linha de crédito para entregadores (score 0.80)
5. Lula vai ao G7 com conversa com Trump indefinida (score 0.80)

**Observação:** Score mínimo do Lula é 0.80 (RSS) e 0.90 (Brave). Funcionou bem.

---

## ✅ ELEIÇÕES — SUCESSO

| Métrica | Valor |
|---------|-------|
| **Pautas brutas** | 93 |
| **Feeds** | 7 |
| **Duplicatas** | 5 descartadas |
| **Sem keyword** | 63 descartadas |
| **Keyword negativa** | 3 descartadas |
| **Inéditas** | 22 |
| **Aprovadas** | 2 (scores: 0.90, 0.90) |
| **Rejeitadas** | 20 (scores de 0.00 a 0.80) |
| **Inseridas (dry-run)** | 2 |
| **Latência** | **26 segundos** |

**Pautas aprovadas:**
1. "Paradoxo da direita": Flávio Bolsonaro perde força (score 0.90)
2. Flávio Bolsonaro perde apoio entre evangélicos (score 0.90)

**Observação:** Score mínimo de eleições é 0.85 (RSS) e 0.95 (Brave) — **MUITO rigoroso**. Por isso só 2 aprovadas. A maioria das pautas sobre eleições foi rejeitada por score baixo.

---

## 📊 Comparativo dos 4 Coletores

| Coletor | Brutas | Inéditas | Aprovadas | Latência | Score Mín |
|---------|--------|----------|-----------|----------|-----------|
| **Geopolítica** | 290 | 39 | 25 | 1m32s | 0.80 / 0.90 |
| **Nacional** | 193 | 56 | 4 | 40s | 0.80 / 0.90 |
| **Lula** | 120 | 13 | 6 | **17s** | 0.80 / 0.90 |
| **Eleições** | 93 | 22 | 2 | 26s | **0.85 / 0.95** |

---

## 🎯 Veredito

| Coletor | Status |
|---------|--------|
| Lula | ✅ PASSOU — rápido, eficiente, 6 pautas boas |
| Eleições | ✅ PASSOU — muito seletivo (pode ser intencional) |

---

## ⚠️ Alerta: Eleições MUITO seletivo

O coletor de eleições tem score mínimo 0.85 (RSS) e 0.95 (Brave). Isso é mais alto que os outros (0.80/0.90).

**Resultado:** Só 2 pautas aprovadas de 22 inéditas.

**Pergunta:** Isso é intencional? A diretriz de eleições é mais rigorosa para evitar fake news? Ou deveria ser ajustada para 0.80/0.90 igual aos outros?

---

Pronto para a próxima ordem! 🎯

— Kimi
