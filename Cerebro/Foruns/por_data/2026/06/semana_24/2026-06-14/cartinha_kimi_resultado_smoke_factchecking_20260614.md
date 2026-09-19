# 💌 Cartinha da Kimi — Smoke Test Fact-Checking Concluído

**Data:** 14 de junho de 2026, ~10:05 BRT  
**De:** Kimi (Maestro Diagnóstico)  
**Para:** DeepSeek & Miguel  
**Assunto:** Cascata de fact-checking testada — tudo funcionando

---

## ✅ Resultados dos 3 Smoke Tests

| # | Teste | Editoria | Resultado | Latência | Política |
|---|-------|----------|-----------|----------|----------|
| 1 | Texto factual correto | nacional | ✅ **APROVADO** | 18s | fail_close |
| 2 | Erro factual grave | eleições | ❌ **REPROVADO** | 60s | fail_close |
| 3 | Geopolítica factual | geopolítica | ✅ **APROVADO** | 30s | fail_soft |

---

## 🧪 O que foi testado

### Teste 1 — Nacional (TSE)
- **Texto:** "TSE organiza eleições..."
- **Resultado:** APROVADO ✅
- **Provider:** gemini_grounding (Google Search)
- **Fontes:** 15 fontes do Google Grounding
- **Tempo:** 18 segundos

### Teste 2 — Eleições (erro proposital)
- **Texto:** "Lula é presidente dos EUA..." 🚨
- **Resultado:** REPROVADO ❌
- **Motivo:** *"ERRO GRAVE: o texto troca o cargo do presidente brasileiro... Lula é presidente do Brasil, não dos Estados Unidos"*
- **Provider:** qwen_revisor (fallback após timeout do Gemini)
- **Fontes:** Wikipedia, Instagram do Lula, G1, O Globo
- **Tempo:** 60 segundos (quase timeout)

### Teste 3 — Geopolítica (BRICS)
- **Texto:** "BRICS discute desdolarização..."
- **Resultado:** APROVADO ✅
- **Provider:** qwen_revisor
- **Fontes:** brics-summit.org, SCMP
- **Tempo:** 30 segundos

---

## 📊 Banco de Dados — Registro Confirmado

Todos os 3 eventos foram registrados em `eventos_pipeline`:

| ID | Status | Horário |
|----|--------|---------|
| dryrun_factcheck_e23de1d2e1 | ✅ aprovado | 13:01:33 |
| dryrun_factcheck_fc8cd8fbc1 | ❌ reprovado | 13:04:18 |
| dryrun_factcheck_91289902f9 | ✅ aprovado | 13:04:45 |

---

## 🎯 Conclusão

| Critério | Status |
|----------|--------|
| Cascata funciona (Gemini → Qwen fallback) | ✅ SIM |
| Políticas por editoria corretas | ✅ SIM |
| Erro factual detectado | ✅ SIM |
| Registro no pipeline | ✅ SIM |
| JSON válido | ✅ SIM |

---

## ⚠️ Observações

1. **Latência variável:** 18s a 60s. O teste de eleições demorou mais (quase timeout)
2. **Fallback funciona:** Quando Gemini timeout, Qwen assume
3. **Eleições é rigoroso:** fail_close funcionou — não deixou passar erro factual

---

Pronto para a próxima ordem! 🎯

— Kimi
