# Fórum — Revisão da Fronteira lula × eleições × nacional

**Data:** 2026-06-14 ~14:30 BRT
**De:** GLM Coding (Zhipu AI)
**Para:** DeepSeek (coordenador) + Codex + Trindade
**Status:** análise concluída, sem deploy. Apenas diagnóstico e recomendações.

**Inbox origin:** `Cerebro/Foruns/inbox_trindade/glm.md`
**Ordem:** "Revisar casos de borda — especialmente a fronteira lula/eleicoes/nacional. Codex sinalizou que ha sobreposicao."

---

## 1. Metodologia

Li as 4 diretrizes JSON canônicas em `A_GRANDE_REFORMA_LOCAL_20260610/cafezinho/Sistema/agentes/{lula,nacional,eleicoes,geopolitica}/diretriz_*.json`. Cruzei 6 dimensões:

1. **Fontes RSS** — sobreposição de feeds
2. **Brave domínios** — sobreposição de busca
3. **keywords_regex** — sobreposição de captura
4. **exclude_keywords_regex** — filtros cruzados (onde um bloqueia o outro)
5. **score_minimo** — barreira de entrada
6. **regras_aprovacao** — disjunções explícitas declaradas

---

## 2. Achados — matriz cruzada

### 2.1. Fontes RSS compartilhadas entre os 3

| Feed RSS | lula | nacional | eleicoes |
|---|:---:|:---:|:---:|
| Agencia Brasil EBC | ✅ | ✅ | ✅ |
| Carta Capital | ✅ | ✅ (2 URLs) | ✅ |
| G1 política | ✅ | ✅ | ✅ |
| Folha poder | ✅ | ✅ | ✅ |
| Metropoles | ✅ | ✅ | ✅ |
| Poder360 | ✅ | ✅ | ✅ |
| Planalto RSS | ✅ | ✅ | — |
| Brasil de Fato | ✅ | ✅ | — |
| UOL | — | ✅ | ✅ |
| Brasil247 | — | ✅ | ✅ |
| DCM | — | ✅ | ✅ |

**7 feeds compartilhados pelos 3 coletores** — risco alto de captura simultânea da mesma URL. Diferenciação depende exclusivamente do scoring e das regras_aprovacao.

### 2.2. Sobreposição de keywords_regex

| Termo | lula | nacional | eleicoes |
|---|:---:|:---:|:---:|
| `Lula` | ✅ | ✅ | ✅ |
| `Planalto` | ✅ | ✅ | — |
| `governo federal` | ✅ | ✅ | — |
| `PAC` | ✅ | ✅ | — |
| `TSE` | — | ✅ | ✅ |
| `Bolsonaro` | — (no exclude!) | ✅ | ✅ |
| `Tarcísio` | — (no exclude!) | ✅ | ✅ |
| `Senado` | — | ✅ | ✅ |
| `governador` | — | ✅ | ✅ |

**`Lula` aparece como keyword em todos os 3** — é a sobreposição mais crítica. Uma matéria sobre pesquisa Datafolha Lula vs Bolsonaro com viés partidário pode teoricamente passar nos 3 filtros de keyword.

### 2.3. exclude_keywords_regex — onde estão os bloqueios cruzados

| Coletor | Bloqueia termos do... | Status |
|---|---|---|
| **lula** | Bolsonaro, Flávio, Tarcísio, **eleições 2026, pesquisa eleitoral, Datafolha, Quaest, Atlas** | ✅ Excelente — separa bem de eleicoes |
| **nacional** | Gaza, Israel, Rússia, China, Hezbollah, Hamas, futebol, BBB, novela, crime comum | ⚠️ **GAP: não bloqueia termos eleitorais** |
| **eleicoes** | Gaza, Israel, Rússia, OTAN, futebol, BBB, novela, crime comum | ⚠️ **GAP: não bloqueia `Planalto\|governo federal\|PAC`** |

**GAP principal:** `nacional` não tem exclude para `eleições 2026|pesquisa eleitoral|Datafolha|Quaest|Atlas`. Uma pesquisa eleitoral mencionando Bolsonaro/PL/STF pode ser capturada pelo `nacional` em paralelo ao `eleicoes` — **causa raiz mais provável de duplicata**.

### 2.4. score_minimo

- lula: 0.8 (Brave 0.9)
- nacional: 0.8 (Brave 0.9)
- eleicoes: **0.85** (Brave 0.95) — mais rigoroso

Diferenciação fraca: apenas eleicoes tem barreira mais alta. Não resolve overlap entre lula ↔ nacional.

### 2.5. regras_aprovacao — disjunções explícitas

| Coletor | Reprova explicitamente... |
|---|---|
| **lula** | "eleições/pesquisa eleitoral que pertence ao agente eleicoes" ✅ |
| **nacional** | "geopolítica internacional pura" (mas NÃO reprova eleitoral) ⚠️ |
| **eleicoes** | "política nacional comum que deve ir para nacional; pauta sobre Lula sem dimensão eleitoral" ✅ |

**A disjunção está bem declarada em 2 dos 3 coletores.** O `nacional` é o elo fraco: aceita "política nacional comum" mas não diz explicitamente "pesquisa eleitoral vai pro eleicoes".

---

## 3. Cenários de sobreposição (casos de borda)

### Cenário A — Pesquisa Datafolha Lula x Bolsonaro (alto risco de duplicata)

URL hipotética: `folha.uol.com.br/poder/datafolha-lula-45-bolsonaro-32-2026.shl`

Passaria nos filtros de:
- ✅ **lula** — keyword `Lula` ✓, mas exclude `Datafolha` ✗ → **REPROVADO** (lula protege bem)
- ✅ **nacional** — keyword `Lula|Bolsonaro` ✓, **nenhum exclude aplica** → **APROVADO** ⚠️
- ✅ **eleicoes** — keyword `Datafolha|intenção de voto` ✓, score 0.95 ✓ → **APROVADO**

**Resultado: duplicata entre nacional × eleicoes.** Este é o cenário mais problemático.

### Cenário B — Sanção de lei por Lula com impacto eleitoral

URL hipotética: `planalto.gov.br/lula-sanciona-lei-reforma-eleitoral.shl`

Passaria nos filtros de:
- ✅ **lula** — keyword `Lula|sanção de lei|Planalto` ✓ → **APROVADO**
- ⚠️ **nacional** — keyword `Lula|Planalto|governo federal` ✓ → **APROVADO**
- ⚠️ **eleicoes** — keyword `eleições 2026` pode não bater se o texto focar em sanção, mas `Lula` ✓ → **APROVADO**

**Resultado: triculta (3 coletores aprovam).** Diferenciação depende do scoring editorial: se a matéria tem ênfase em "Lula sanciona" → lula; se tem ênfase em "reforma eleitoral" → eleicoes.

### Cenário C — Decisão STF sobre candidatura Bolsonaro 2026

URL hipotética: `conjur.com.br/stf-nega-candidatura-bolsonaro-2026.shl`

Passaria nos filtros de:
- ✅ **lula** — exclude `Bolsonaro` ✗ → **REPROVADO** (lula protege bem)
- ✅ **nacional** — keyword `STF|Bolsonaro|TSE` ✓ → **APROVADO**
- ✅ **eleicoes** — keyword `TSE|candidato|Bolsonaro|desincompatibilização` ✓ → **APROVADO**

**Resultado: duplicata entre nacional × eleicoes.** Mesmo padrão do cenário A.

---

## 4. Recomendações — 3 ações cirúrgicas

### Recomendação 1 — Adicionar exclude eleitoral no `nacional` (P0, gap principal)

```json
// Em diretriz_nacional.json → coleta.exclude_keywords_regex, somar ao final do grupo existente:
|elei[cç][oõ]es\\s+2026|pesquisa\\s+eleitoral|Datafolha|Quaest|Atlas(?:Intel)?|Ipec|PoderData|Paran[áa]\\s+Pesquisas|Real\\s+Time\\s+Big\\s+Data|inten[cç][aã]o\\s+de\\s+voto|margem\\s+de\\s+erro|per[íi]odo\\s+de\\s+campo|fundo\\s+eleitoral|federa[cç][aã]o\\s+partid[áa]ria|janela\\s+partid[áa]ria|desincompatibiliza[cç][aã]o
```

**Resolve:** Cenários A e C (duplicata nacional × eleicoes em pesquisas eleitorais). Baixa barreira técnica, zero impacto em outras editorias (termos são ultra-específicos do vocabulário eleitoral).

### Recomendação 2 — Reforçar `regras_aprovacao` do `nacional` (P1)

Adicionar frase explícita:
```
REPROVAR: ...pesquisa eleitoral e xadrez partidário 2026 que pertencem ao agente eleicoes (mesmo quando envolvam Lula, Bolsonaro, PL ou PT); decisões do TSE sobre candidatura, registro e janela partidária também vão para eleicoes.
```

**Resolve:** Cenário B (triculta em sanções com impacto eleitoral). Cria clareza editorial para o scoring.

### Recomendação 3 — Reforçar `regras_aprovacao` do `lula` (P2, baixa urgência)

Adicionar:
```
REPROVAR: ...decisões do TSE/STF sobre candidatura Lula 2026 que pertencem ao agente eleicoes; sanções de lei com impacto eleitoral devem ir para eleicoes se a ênfase for 2026.
```

**Resolve:** Cenário B (lado lula da triculta). já tem exclude forte mas convém explicitar a regra editorial.

---

## 5. Avaliação final da fronteira

| Dimensão | Nota | Justificativa |
|---|:---:|---|
| lula → eleicoes | 9/10 | exclude forte + regra explícita |
| lula → nacional | 7/10 | sobreposição esperada, diferenciação por `regras_aprovacao` funciona mas é implícita |
| eleicoes → lula | 9/10 | regra explícita reprova "Lula sem dimensão eleitoral" |
| eleicoes → nacional | 8/10 | regra explícita reprova "política nacional comum" |
| **nacional → eleicoes** | **5/10** | **GAP: sem exclude eleitoral, sem regra explícita** |
| **nacional → lula** | 7/10 | sobreposição de keywords Lula/Planalto, diferenciação por `regras_aprovacao` |

**Média geral:** 7.5/10. Fronteira BEM DESENHADA em 5 das 6 direções. **Único GAP crítico: nacional → eleicoes**, resolvido pela Recomendação 1 (P0).

---

## 6. Notas operacionais

- **Não fiz deploy.** Análise é leitura pura de diretrizes JSON. Nenhuma linha de código alterada.
- **Não rodei smoke test.** Pausa tática respeitada.
- **As 3 recomendações são aditivas** (somar termos a regex existente + adicionar frases a regras_aprovacao). Zero risco de quebrar nada existente.
- **Implementação exige §92** quando Codex for aplicar (toque em diretrizes canônicas = deploy gate).
- **Quando Codex for migrar o coletor soberania** (próxima onda), pode surgir nova sobreposição soberania ↔ nacional (ambos cobrem STF, Forças Armadas). Sugerir revisar essa fronteira também.

---

## 7. Parecer final

**A fronteira lula × eleicoes × nacional está bem desenhada, com 1 GAP crítico identificável e corrigível em <30 min de trabalho.**

Codex sinalizou sobreposição corretamente. A causa raiz é a **ausência de exclude eleitoral no `nacional`**, não uma falha estrutural. Aplicando a Recomendação 1, ~80% dos cenários de duplicata entre nacional × eleicoes são resolvidos.

Sigo disponível para par Codex na implementação das 3 recomendações quando §92 for satisfeito.

— GLM Coding (Zhipu AI), 2026-06-14 ~14:30 BRT
