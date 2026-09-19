# FÓRUM — Processo Etapista: Agente Manchete Inteligente (Fase 1 simples → meta) — 12/08/2026

**Data:** 2026-08-12
**Autor:** ZCode (GLM-5.2, Z.ai — fallback final; Kimi/Qwen 🔴🔴)
**Status:** 🟡 ROADMAP + Fase 1 concreta (pra implementar). Começa simples, configura rumo à meta.
**Origem:** Miguel — *"processo etapista, primeira fase mais simples, vamos configurando na direção da meta de ter um agente comentarista [manchete] altamente inteligente. começar simples, critérios simples mas objetivos. manchetes precisam ter pegada. pode deepseek v4, mas não hardcode. escolher entre posts das últimas 24h qual merece. mais estabilidade com filtro rigoroso. títulos muito bons, fotos boas (reais, frescas). escândalo/notícia negativa contra bolsonaro valem pontos. força de lula (pesquisas, programas, discurso) vale pontos. tese: anti-imperialista e anti-direita, mas silenciosa, de argumentos, menos clichês."*
**Relacionado:** `forum_piloto_agente_manchete_inteligente_20260812.md` (modelo completo) · `forum_arquitetura_curadoria_manchete_estavel_20260812.md` · `forum_seletor_llm_inteligente_telemetria_20260812.md` · `CEREBRO_NODE_MANCHETE.md`

---

## 🎯 A META (norte)

Um **agente manchete altamente inteligente**: escolhe a manchete por **curadoria editorial multi-critério** (LLM dinâmica via seletor preço+qualidade), com **estabilidade** (filtro rigoroso, a manchete fica), **títulos e fotos excelentes**, capacidade de **reescrita ativa**, **telemetria redundante** e **assinatura**. Se der certo, **reproduz pro ecossistema**.

## 🪜 O ROADMAP etapista (cada fase adiciona, sem rework)

| Fase | Foco | O que entra | Estado |
|---|---|---|---|
| **Fase 0** ✅ | Base pronta | cat 22 até 2º turno, veto repetidor 5786, enxame 80-130, delay 2min, anti-draft | **no ar** |
| **Fase 1** ⬅️ agora | **Curadoria objetiva simples** | LLM-juiz via **seletor** (não hardcode), critérios claros, threshold alto, **estabilidade**, prioriza humanos | **design** |
| **Fase 2** | Qualidade do post | + **reescrita de título** (propoe), + **foto real/fresca** (validar/substituir), telemetria redundante | futuro |
| **Fase 3** | Profundidade | + reescrita de lead/ângulo, classificador de risco, seletor multi-modelo maduro | futuro |
| **Fase 4 (meta)** | Inteligência plena | editoração ativa `auto`, generalização pro ecossistema | futuro |

---

## 🟢 FASE 1 — Curadoria objetiva SIMPLES (implementável agora)

### Escopo (deliberadamente pequeno)
- **Só ESCOLHE** a manchete (sem reescrita — isso é Fase 2).
- LLM-juiz avalia cada candidato → **nota 0–100**.
- Veto ao repetidor estatal (5786), **só cat 22** (até 30/11/2026), prioriza humanos (2018 Miguel, 5780 Gabriel).
- **Estabilidade** (a manchete fica).
- Telemetria **básica** (JSONL + Prometheus).

### A fórmula da nota (0–100) — critérios objetivos do Miguel
```
nota = GA4_normalizado(0-30)          # audiência real (base)
     + pegada_editorial(0-40)         # LLM-juiz: é quente? tem pegada?
     + bonus_humano(0-15)             # Miguel(2018) ou Gabriel(5780)
     + frescor(0-10)                  # idade
     + foto_real(0-5)                 # tem imagem destacada real (não default/placeholder)
```
A **pegada_editorial (0–40)** é onde mora a tese — o LLM-juiz avalia (ver prompt abaixo).

### O prompt do LLM-juiz (Fase 1) — tom SILIENCIOSO, sem clichês
```
Você é o editor-chefe do portal O Cafezinho. Avalie a PEGADA EDITORIAL deste post
como candidato à manchete (nota 0 a 40), considerando:
- É uma notícia QUENTE, com pegada? (peso alto)
- Escândalo / notícia NEGATIVA contra Bolsonaro, Flávio ou a direita? (+)
- Força de LULA: pesquisas, programas de governo, discurso forte? (+)
- Crítica ao PAPEL IMPERIALISTA (EUA/Israel/etc.) — via ARGUMENTO, não slogan (+)
- Informação NOVA / exclusiva / ângulo original (+)
- O post defende uma TESE com argumento? (+)

EVITE: clichês, jargão de panfleto, obviedade. Premie ARGUMENTO e informação,
não retórica vazia. A linha editorial é anti-imperialista e anti-direita, mas
a luta é SILENCIOSA — de ideias, não de gritaria.
Retorne SÓ JSON: {"nota": int(0-40), "sinais": [...], "cliche": bool, "risco_linha": bool}
Se risco_linha=true (fere a linha: atacar STF/Lula/Irã/Rússia, ou vira panfleto) → nota vira 0.
Título: ...
Resumo: ...
```
> `risco_linha=true` → **veta** (nota 0). `cliche=true` → **desconta**.

### Estabilidade (filtro rigoroso — a manchete fica)
- **Threshold:** só vira manchete se `nota ≥ 70/100`.
- **Permanência mínima:** 8h (mais estável que o 6h original — pedido "mais estabilidade").
- **Histerese:** só troca se `nota_candidato ≥ nota_atual × 1.3` (30% melhor).
- **Override urgência:** `nota ≥ 92 E humano` → troca imediato ("explodiu").
- Se **ninguém** atinge 70 → **mantém a atual** (não troca por trocar).

### LLM via SELETOR (não hardcode)
- Capacidade: `curadoria_manchete_fase1`.
- Seletor escolhe (preço+qualidade+saldo). **DeepSeek-V4 é o candidato natural** (barato, bom pra política BR) — mas a escolha é do seletor, não do código.
- Se DeepSeek sem saldo → seletor pula pro próximo (Gemini/Qwen).

### Telemetria Fase 1 (básica)
- JSONL local: cada avaliação (post, nota, sinais, modelo, custo).
- Prometheus: `manchete_nota{post_id}`, `manchete_escolhas_total{motivo}`, `llm_custo_usd_total`.
- (Redundância multi-canal é Fase 2.)

### Fotos (reais, frescas) — Fase 1 parcial
- Sinal `foto_real` (0-5): post **tem** imagem destacada real (não placeholder/default) → +5; sem imagem → 0 (e perde pontos). Já dá um incentivo.
- **Validar/substituir fotos fracas** → Fase 2.

---

## ⚙️ Configurando rumo à meta (o que cada fase adiciona, sem rework)

- **Fase 1** estabelece o **esqueleto** (seletor + juiz + estabilidade + telemetria básica + veto + humanos). Tudo plugável.
- **Fase 2** pluga **reescrita de título** + **foto** + **telemetria redundante** no mesmo esqueleto.
- **Fase 3** pluga **reescrita de lead** + **classificador de risco** + seletor maduro.
- **Fase 4** liga **modo auto** + **generaliza**.
> Nada do que se faz na Fase 1 é desperdiçado — é a fundação.

## ✅ Próximo passo

Implementar a **Fase 1** no `agente_manchete.py` (ou `agente_manchete_v2.py` ao lado do legado):
1. seletor mínimo (preço+saldo, qualidade fixa v1).
2. LLM-juiz com o prompt acima (nota 0-40 pegada).
3. fórmula da nota 0-100.
4. estabilidade (threshold 70, permanência 8h, histerese 1.3×, override 92).
5. telemetria JSONL+Prometheus.
6. **teste cego** (diagnóstico): ranquear velho vs. novo em várias rodadas, te mostrar as escolhas, calibrar — **só depois vai pro ar**.

---

— **ZCode (GLM-5.2, Z.ai coding plan)**, 12/08/2026
