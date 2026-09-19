# 🎨 Teoria de Escolha de Imagem por Vertical (Cafezinho V4)

> **Tipo:** documento de referência editorial (não código). Define a "teoria" que o futuro motor de curadoria de imagem por tese vai respeitar.
> **Origem:** ordem Miguel (voz, 12/08/2026): "era bom que a gente formasse uma teoria, criasse uma teoria... como a imagem geopolítica, a gente pode escolher um mapa, um mapa do Irã, um mapa da China... essa aqui pode criar uma imagem artificial, uma tese tal. Vamos criar toda uma arquitetura teórica e prática para escolher imagem."
> **Pares:** `forum_curadoria_imagem_por_tese_arquitetura_20260812.md` + `memoria_curadoria_imagem_por_tese_arquitetura_20260812.md`.
> **Estado:** 📄 v1 — evolui conforme aprendemos com o loop humano.

---

## 0. Princípio fundamental

> **A imagem não ilustra o texto — ela COMUNICA a tese.** Não é "arrume uma foto do Lula". É "qual visual comunica a tese desta matéria?". Às vezes é o Lula; às vezes é um mapa; às vezes é um documento; às vezes é uma ilustração gerada. A escolha é editorial, não decorativa.

**Consequência prática:** o motor de curadoria lê a tese (`v4_curadoria_tese.frame_visual`) → decide o **tipo visual** → só então busca/gera.

---

## 1. Taxonomia de tipos visuais comunicativos

O campo futuro `tipo_entidade` (ver memória §4) e o `frame_visual.prioridade` usam esta taxonomia:

| Tipo | Quando comunica melhor a tese | Exemplo canônico |
|---|---|---|
| **pessoa** | a tese é sobre um ator político individual e seu rosto é a notícia | Lula sancionando lei; Bolsonaro em comício |
| **instituição** | a tese é sobre um órgão/coletivo, não uma pessoa | STF pleno, Senado, CPMI, Banco Central |
| **documento** | a tese vive num artefato (lei, decisão, relatório, planilha) | trecho da CF em destaque, AO do TSE, gráfico do PIB |
| **local/mapa** | a tese é geográfica/territorial | Estreito de Hormuz, fronteira, mapa eleitoral |
| **infraestrutura/setor** | a tese é sobre produção/indústria | navio petroleiro, painel solar, fábrica, porto |
| **evento/cena** | a tese é o acontecimento em si | protesto, desastre, cerimônia |
| **ilustração (IA)** | a tese é abstrata e não há foto real adequada | "concentração de renda", "inteligência artificial", metáfora |

**Regra de desambiguação:** quando 2 tipos servem, **pessoa > instituição > documento > cena > mapa > setor > ilustração** (prioriza o concreto e identificável). Exceção: se a tese explicitamente é "geográfica" (Hormuz), mapa vence.

---

## 2. Regras por vertical

### 🌍 Geopolítica
- **Tipos preferenciais:** mapa, local/cena, pessoa (líder), infraestrutura (petroleiro/porto).
- **Mapas:** priorizar **oficiais ou de processo determinístico** (gov, ONU, EIA, mapa SVG livre). **NUNCA IA generativa para mapa factual** (risco de fronteira/rotulo errado fabricado — `forum_mutirao §7`).
- **IA generativa permitida:** cota **20% por bloco de 4h** (policy viva), só pra tese abstrata (ex: "eixo China-Irã" como composição simbólica). Sempre legenda "ilustração".
- **Sensível:** guerra/morte/desastre → rubrica de alto risco do tribunal (Kimi Vision obrigatório); nunca IA de rosto de líder sensível.

### 🔬 Ciência / Tecnologia
- **Tipos preferenciais:** documento (gráfico/paper), infraestrutura (equipamento), ilustração (microscopia/telescópio/esquema).
- **IA generativa LIVRE** (policy), mas **proibido fabricar figura científica/dado/mapa factual** — só ilustração conceitual com legenda "ilustração".
- **Registrar sempre:** gerador/modelo/prompt/data nos metadados (`metadados_json`).
- **Pessoa:** só se for cientista identificado em evento (foto oficial/CC).

### 🇧🇷 Nacional (política institucional brasileira)
- **Tipos preferenciais:** pessoa, instituição (Congresso/STF/Palácio), documento (AO/lei).
- **IA generativa PROIBIDA** (policy: zero IA em Nacional). Sempre foto real.
- **Rosto político sensível:** nunca IA; foto oficial TSE é último recurso (`forum_mutirao §4`).
- **Identidade:** visão não prova identidade; exige metadado oficial/legenda.

### 🏘️ Regional / Temáticos
- **Tipos preferenciais:** cena local, pessoa, infraestrutura.
- **IA generativa PROIBIDA.** Sempre foto real (agente/parceiro/stringer).
- **Licença:** prioridade CC0/domínio público > CC BY > Commons > Flickr oficial > órgão público.

---

## 3. Quando buscar real vs gerar IA

```
tese → tipo visual decidido?
  ├─ pessoa/instituição/documento/local/cena → BUSCAR REAL no Banco Ouro
  │    └─ não achou com score≥limiar? → loop humano (Fase 2) OU busca externa (Wikimedia/Flickr oficial)
  │         └─ humano diz "não existe"? → registrar falta, publicar sem imagem destaque NÃO (§86 exige) → gerar ilustração só se vertical permite IA
  └─ tipo=ilustração (tese abstrata) → GERAR IA (só se vertical permite IA)
       └─ validar com tribunal (Qwen+Gemini); rejeita pseudotexto/logo/rosto deformado
       └─ legenda obrigatória "ilustração" + metadados do gerador
```

**Regra de ouro:** foto real sempre preferida quando existe e comunica a tese. IA é fallback pra tese abstrata, nunca atalho pra "não achei foto do sujeito".

---

## 4. Critérios de "comunicação editorial" (o score futuro)

O `score_comunicacao_tese` (0-100, a ser implementado na Fase 1) pondera:
1. **Pertinência semântica** (40%): a imagem bate com a tese? (Gemini cross-check tese↔imagem)
2. **Identificação correta** (25%): se a tese é sobre Lula, o rosto é do Lula? (Qwen Vision + prova documental)
3. **Frescor** (10%): data_foto recente (não reaproveitar foto de 2020 pra notícia de hoje)
4. **Diversidade** (10%): hash não usado recentemente (evita repetição)
5. **Qualidade técnica** (10%): composição, resolução, sem corte ruim
6. **Policy** (5%): licença ok, sem IA em vertical proibida, sem rosto sensível fabricado

**Limiar de auto-aprovação:** ≥75 (configurável). <75 → top-3 vai pro loop humano.

---

## 5. O loop de aprendizado (teoria → prática → teoria)

1. Motor propõe top-K com scores.
2. Se score alto → auto (com recibos, auditável).
3. Se score baixo → humano escolhe (Telegram/painel/e-mail).
4. Escolha humana vira **gold** (`gold_source:human_explicit`).
5. Replay no Corpus Ouro → detecta onde o motor errou → `RuleProposal`.
6. Gates L0–L3 → Miguel aprova L3 → motor promovido (versão bumpada).
7. **Teoria atualizada:** se um padrão recorrente emerge (ex: "toda matéria sobre PEC usa documento, não pessoa"), vira regra nesta taxonomia.

> **A teoria não é estática.** Cada escolha humana refinada é um voto na teoria. Este documento evolui.

---

## 6. Glossário

- **tese** — a afirmação editorial central da matéria (o "porquê"), produzida por `v4_curadoria_tese`.
- **frame_visual** — campo do contrato de curadoria que declara a prioridade visual (`pessoa|instituição|documento|setor_produtivo|infraestrutura`).
- **tipo_entidade** — coluna futura do Banco Ouro (`pessoa|instituição|local|tema|evento|documento`); chave pra o motor distinguir foto-pessoa de mapa.
- **score_comunicacao_tese** — score futuro 0-100 de "quão bem a imagem comunica a tese".
- **tier_prominencia** — conceito do classificador (pessoa única identificada + score≥450 → aprova direto).
- **gold_source** — origem do rótulo de treino (`human_explicit` quando humano escolheu).
- **tribunal visual** — Qwen Vision (composição) + Gemini Vision (pertinência) + Kimi Vision (editor top-3, desempate).
- **Corpus Ouro** — dataset canônico de replay p/ autoaprendizado governado.
- **§86** — regra viva: imagem destacada obrigatória em toda publicação Cafezinho.

---

## 7. Exemplos canônicos (casos de teste da teoria)

| Matéria (tese) | Vertical | tipo_entidade | Escolha ideal |
|---|---|---|---|
| "Lula sanciona marco das saneadoras" | Nacional | pessoa | foto oficial Lula sancionando |
| "STF forma maioria para..." | Nacional | instituição | plenário STF (não rosto individual) |
| "PEC da segurança pública avança" | Nacional | documento | trecho da PEC/artigo CF em destaque |
| "Iran bloqueia Estreito de Hormuz" | Geopolítica | local/mapa | mapa do estreito (oficial/determinístico) |
| "China supera EUA em patentes de IA" | Ciência | documento/ilustração | gráfico de patentes OU ilustração conceitual |
| "Concentração de renda bate recorde" | Nacional/Economia | ilustração | IA generativa (tese abstrata) — com legenda |
| "James Webb capta..." | Ciência | infraestrutura/documento | foto do telescópio ou imagem divulgada pela NASA |

---

## 📜 Autoria
ZCode (GLM-5.2). 2026-08-12 ~10:10 BRT. v1. Evolui com o loop humano. Pares: `forum_curadoria_imagem_por_tese_arquitetura_20260812.md` + `memoria_curadoria_imagem_por_tese_arquitetura_20260812.md`.
