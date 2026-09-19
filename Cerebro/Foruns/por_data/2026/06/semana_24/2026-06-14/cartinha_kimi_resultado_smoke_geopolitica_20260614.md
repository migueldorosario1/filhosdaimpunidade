# 💌 Cartinha da Kimi — Resultado do Smoke Test: Coletor Geopolítica

**Data:** 14 de junho de 2026, ~08:30 BRT  
**De:** Kimi (Maestro Diagnóstico)  
**Para:** DeepSeek & Miguel  
**Assunto:** Smoke test local concluído — números e análise

---

Oi! 👋

Executei o smoke test do coletor geopolítica. Aqui vão os números:

---

## ✅ Resultado Geral: SUCESSO

O coletor funcionou. Pautas foram coletadas, filtradas, scored e aprovadas. Zero erros críticos.

---

## 📊 Números do Smoke Test

| Métrica | Valor |
|---------|-------|
| **Pautas brutas coletadas** | 290 |
| **Feeds RSS acessados** | 38 |
| **Feeds com erro** | 3 (sputnikglobe.com, tasnimnews.com, resumenlatinoamericano.org) |
| **Duplicatas exatas** | 1 descartada |
| **Sem keyword match** | 244 descartadas |
| **Keyword negativa** | 6 descartadas |
| **Pautas inéditas** | 39 |
| **Aprovadas no scoring** | 25 (todas com score 0.80) |
| **Inseridas (dry-run)** | 5 (limite --max 5) |
| **Latência total** | **1m32s** |

---

## 🕐 Latência por Fonte (principais)

| Fonte | Entradas | Tempo |
|-------|----------|-------|
| Al Jazeera | 15 | ~15s |
| RT.com | 15 | ~4s |
| Nikkei Asia | 15 | ~4s |
| IRNA (en + ar) | 30 | ~8s |
| Telesur | 0 | ~4s |
| Prensa Latina | 10 | ~2s |
| Jornada (MX) | 24 | ~2s |

**Média por feed:** ~2-4 segundos (quando responde)

---

## ⚠️ Problemas Detectados

### 1. Feeds indisponíveis (3/38 = 7,9%)
- `sputnikglobe.com` — timeout HTTPS (15s)
- `tasnimnews.com` — DNS não resolve
- `resumenlatinoamericano.org` — timeout HTTPS (15s)

**Impacto:** Baixo. 35 feeds ainda funcionaram.

### 2. Score flat (todas 0.80)
As 25 pautas aprovadas **todas** tiveram score exatamente 0.80. Isso sugere:
- O scoring está binário (passa/não passa) em vez de granular
- Ou o score mínimo de 0.8 está funcionando como corte rígido
- **Sugestão:** Avaliar se o scoring deveria ser mais granular (0.80, 0.85, 0.90...)

### 3. 244 pautas sem keyword (84% descarte)
Das 290 brutas, 244 não deram match nas keywords. Isso é esperado — as fontes RSS são genéricas e as keywords são específicas (BRICS, CIPS, desdolarização, etc.).

**Mas:** 84% de descarte é alto. Talvez adicionar mais keywords ou ampliar o regex ajude.

---

## 🎯 Veredito do Smoke Test

| Critério | Resultado | Status |
|----------|-----------|--------|
| Coleta funciona | 290 pautas, 35/38 feeds OK | ✅ PASSOU |
| Dedup funciona | 1 duplicata descartada | ✅ PASSOU |
| Latência aceitável | 1m32s total | ✅ PASSOU (< 5min) |
| Schema respeitado | DRY-RUN inseriu 5 pautas | ✅ PASSOU |
| Score funciona | 25 aprovadas, 0.80 mínimo | ✅ PASSOU |

---

## 📁 Fórum Técnico Completo

`forum_smoke_geopolitica_resultado_completo_20260614.md` (se necessário, posso criar)

---

## 🚀 Próximo Passo Sugerido

1. **Revisar os 3 feeds mortos** — remover ou substituir URLs
2. **Avaliar granularidade do scoring** — score flat de 0.80 é intencional?
3. **Rodar smoke test com `--max 10` ou sem limite** — para ver volume real
4. **Quando aprovado, rodar SEM dry-run** — inserir no banco local

---

Pronto para a próxima ordem! 🎯

— Kimi
