# 🗺️ MAPA — Cobertura regional histórica do Cafezinho (2011→2026) × categorias de estado/região

**De:** Z (ZCode), a pedido do Miguel (30/07/2026)
**Data:** 2026-07-30 ~18:30 BRT
**Método:** varredura READ-ONLY de **77.133 posts publicados** (API REST WP, nada alterado no site)
**Pareia com:** `forum_agente_v4_regional_eleicoes_estados_20260730.md` (§1–§14) · Memória `MEMORIA/memoria_agente_v4_regional_eleicoes_estados_20260730.md`

---

## §1 — O que foi feito (resumo do método)

1. **Inventário de categorias:** as 274 categorias do site foram baixadas e cruzadas com as 27 UFs e 5 regiões.
2. **Varredura profunda** em 2 passos:
   - **Passo 1 (títulos):** dump completo dos 77.133 posts → regex por UF nos **títulos** (nome do estado, capitais, governadores atuais, demônios). Termos ambíguos com filtro case-sensitive e borda de palavra (Acre≠acreditar, Pará≠prepará, Mato Grosso≠do Sul).
   - **Passo 2 (conteúdo):** busca server-side só de **termos distintivos de 1 palavra** (demônios: cearense, paraense, potiguar…; estados de nome único: Alagoas, Piauí…; governadores de 1 palavra: Zema, Tarcísio…). Passo suplementar com variantes hifenizadas (mato-grossense, sul-mato-grossense, acreano, candango).
3. **Tiers de confiança:**
   - **Tier A** — UF citada no **título** → relevância regional editorial certa → **auto-aplicável**.
   - **Tier B** — UF citada só no **conteúdo** → inclui *roundups nacionais* (boletins covid, "27 governadores", alertas Inmet, rankings) que **mencionam** o estado sem serem matéria regional → **exige triagem** (não entra no backfill automático).

## §2 — Inventário de categorias (o que existe × o que falta)

### Estados — existem só 8 de 27

| Categoria | ID | Posts | Filhas |
|-----------|-----|-------|--------|
| Ceará | 4968 | 268 | — |
| São Paulo | 4988 | 295 | São Paulo capital (5001, 222) |
| Rio de Janeiro | 1656 | 454 | RJ Capital (5002, 178), Baixada Fluminense (5085), Niterói (20543), Nova Friburgo (4997) |
| Brasília | 5710 | 102 | — |
| Rio Grande do Sul | 5004 | 28 | — |
| Bahia | 4994 | 23 | — |
| Minas Gerais | 2549 | 20 | — |
| Paraíba | 5101 | 5 | — |

**FALTAM 19:** AC, AL, AM, AP, ES, GO, MA, MT, MS, PA, PR, PE, PI, RN, RO, RR, SC, SE, TO

### Regiões — existe só 1 de 5

- **Nordeste (4984, 19 posts)** existe. **FALTAM:** Norte, Centro-Oeste, Sudeste, Sul.

### Eleições — estrutura boa já existe

Eleições (47) · 2014 (843) · 2016 (1306) · 2018 (1323) · 2020 (3568) · 2022 (3615) · 2024 (5000) · **Eleições 2026 (5088) — 1.098 posts, sem filhas** → pronta para receber as editorias estaduais como filhas/netas.

## §3 — O MAPA: posts regionais detectados por UF

Ordenado por volume. **Backfill A** = posts tier A que **não têm** a categoria do estado (alvo do retroativo automático).

| UF | Região | Total detectado | Tier A (título) | Tier B (conteúdo) | Categoria | Já categorizados | **Backfill A** |
|----|--------|----------------:|----------------:|------------------:|:---------:|-----------------:|---------------:|
| **SP** | Sudeste | 3.589 | 836 | 2.753 | ✅ 4988 | 154 | **770** |
| **BA** | Nordeste | 2.377 | 311 | 2.066 | ✅ 4994 | 23 | **294** |
| **CE** | Nordeste | 2.230 | 606 | 1.624 | ✅ 4968 | 248 | **442** |
| **RJ** | Sudeste | 2.151 | 294 | 1.857 | ✅ 1656 | 168 | **255** |
| **PE** | Nordeste | 1.588 | 154 | 1.434 | ❌ FALTA | 0 | **154** |
| **GO** | Centro-Oeste | 1.338 | 101 | 1.237 | ❌ FALTA | 0 | **101** |
| **AM** | Norte | 1.165 | 122 | 1.043 | ❌ FALTA | 0 | **122** |
| **MA** | Nordeste | 1.153 | 87 | 1.066 | ❌ FALTA | 0 | **87** |
| **MG** | Sudeste | 1.101 | 225 | 876 | ✅ 2549 | 16 | **212** |
| **RR** | Norte | 996 | 36 | 960 | ❌ FALTA | 0 | **36** |
| **AP** | Norte | 960 | 18 | 942 | ❌ FALTA | 0 | **18** |
| **TO** | Norte | 810 | 18 | 792 | ❌ FALTA | 0 | **18** |
| **AL** | Nordeste | 738 | 47 | 691 | ❌ FALTA | 0 | **47** |
| **PR** | Sul | 676 | 291 | 385 | ❌ FALTA | 0 | **291** |
| **PI** | Nordeste | 663 | 43 | 620 | ❌ FALTA | 0 | **43** |
| **SE** | Nordeste | 604 | 31 | 573 | ❌ FALTA | 0 | **31** |
| **PB** | Nordeste | 565 | 43 | 522 | ✅ 5101 | 5 | **38** |
| **RO** | Norte | 488 | 20 | 468 | ❌ FALTA | 0 | **20** |
| **RS** | Sul | 468 | 190 | 278 | ✅ 5004 | 17 | **180** |
| **ES** | Sudeste | 336 | 103 | 233 | ❌ FALTA | 0 | **103** |
| **PA** | Norte | 181 | 97 | 84 | ❌ FALTA | 0 | **97** |
| **RN** | Nordeste | 178 | 87 | 91 | ❌ FALTA | 0 | **87** |
| **DF** | Centro-Oeste | 151 | 37 | 114 | ✅ 5710 | 0 | **37** |
| **SC** | Sul | 140 | 49 | 91 | ❌ FALTA | 0 | **49** |
| **MS** | Centro-Oeste | 66 | 17 | 49 | ❌ FALTA | 0 | **17** |
| **MT** | Centro-Oeste | 64 | 14 | 50 | ❌ FALTA | 0 | **14** |
| **AC** | Norte | 31 | 24 | 7 | ❌ FALTA | 0 | **24** |
| **TOTAL** | | **24.807** | **3.901** | **20.906** | 8/27 | 631 | **3.587** |

### Por região

| Região | Posts detectados | Tier A | UFs sem categoria |
|--------|-----------------:|-------:|:-----------------:|
| Nordeste | 10.096 | 1.409 | 7 de 9 |
| Sudeste | 7.177 | 1.458 | 1 de 4 (ES) |
| Norte | 4.631 | 335 | 7 de 7 |
| Centro-Oeste | 1.619 | 169 | 3 de 4 |
| Sul | 1.284 | 530 | 2 de 3 |

### Por ano (tier A — matérias claramente regionais)

2011: 9 · 2012: 19 · 2013: 16 · 2014: 38 · 2015: 32 · 2016: 158 · 2017: 90 · 2018: 137 · 2019: 109 · 2020: 428 · 2021: 307 · 2022: 510 · 2023: 513 · 2024: 518 · 2025: 294 · **2026: 723** (ano eleitoral já é o recorde — e ainda faltam 2 meses de campanha)

## §4 — Controle de qualidade (falsos positivos mapeados)

Amostras auditadas por termo de risco. Achados:

1. **Tier B contém roundups nacionais** (boletins covid 2020-22, "27 governadores tomam posse", alertas Inmet, Monitor da Violência, pesquisas nacionais com recorte por estado) → **fora do backfill automático**; triagem futura com filtro anti-roundup.
2. **Termos ambíguos no título** → bucket **REVISAR (254 posts)**, fora do lote automático:
   - `Vitória` (vitória eleitoral ≠ cidade, ES) — 74 posts
   - `Natal` (o feriado ≠ a cidade, RN) — 61 posts
   - `Ratinho` (apresentador do SBT ≠ governador do PR) — 18 posts
   - `Salvador` (Allende/pessoas ≠ cidade, BA) — 32 posts
   - `Belém` (Belém bíblica ≠ cidade, PA) — 23 posts
   - `Fortaleza`/`Palmas` — 46 posts (CE/TO)
3. Demônios tiveram precisão alta nas amostras (`fluminense` pegou petroleiros/Niterói/Paes, não futebol; `gaúcho` pegou Brizola/Jango/RS; `Tarcísio` pegou o governador).
4. Falso positivo isolado identificado: "Carlo Caiado" (vereador RJ) ≠ Ronaldo Caiado (GO) — o bucket REVISAR + triagem da Fase B absorvem.

## §5 — Plano de trabalho do retroativo (preenchendo as categorias)

> Pedido do Miguel: *"primeiro faz o histórico, para a gente já ir preenchendo essas categorias com materiais dos estados […] se não fica muito pesado, já colocando a categoria certa."*
> **Não fica pesado:** o lote principal são ~3,3 mil atualizações de categoria (1 chamada API por post, ~1h de execução, log completo, reversível). Nenhum conteúdo é alterado — só taxonomia.

| Lote | O quê | Volume | Peso | Reversão |
|------|-------|--------|------|----------|
| **0** | Criar as **19 categorias de UF** + **4 de região** (Norte, Centro-Oeste, Sudeste, Sul); hierarquia: região → UF (e UF → capitais futuras); pendurar as 8 UF existentes nas regiões | 23 categorias | mínimo | apagar categorias |
| **1** | **AUTO:** aplicar categoria da UF + da região nos **3.333 posts tier A** (bucket auto), mantendo categorias atuais | 3.333 posts | ~1h | script reverso pelo log |
| **2** | **REVISAR:** triagem dos 254 posts de termos ambíguos (regra: contexto eleitoral/geográfico no título) | 254 posts | ~30 min assistido | idem |
| **3** (sprint futura) | **Tier B (20.906):** filtro anti-roundup + triagem (LLM leve) → só matérias efetivamente regionais | sob demanda | sprint própria | idem |

**Regras do retroativo:**
- **Aditivo sempre** — nunca remover categoria existente; só acrescentar UF/região.
- **Log por post** (`backfill_log.jsonl`: id, cats antes, cats depois, UF, tier, termo-evidência) → rollback = 1 script.
- Posts já na categoria da UF são pulados (idempotente; rodar 2× não duplica).
- **Não mexer** nas categorias Eleições 20xx do histórico (2014/2018/2022 já têm suas casas; recategorização eleitoral é decisão editorial separada).
- Ritmo cortês com o servidor: ~2 req/s, pausa a cada 500.
- **Governança:** Lote 0 e 1 só disparam com o **"vai"** do Miguel (AUTH) — scripts prontos, dry-run disponível.

## §6 — O que já está pronto (entregáveis técnicos)

Workspace `ZCodeProject/regional_v4/`:
- `inventario_categorias.py` + `cache/categorias.json` — as 274 categorias
- `scanner_v2.py` + `cache/titulos_p*.json` (771 páginas) + `cache/t3_*.json` — varredura completa, resumível
- `cache/posts_por_uf.jsonl` — **24.807 posts mapeados** (uf, id, data, título, cats, tier, evidência)
- `cache/mapa_ufs.json` — resumo por UF/região/ano
- `cache/backfill_plano.json` — **lotes AUTO (3.333) e REVISAR (254)** prontos para o executor
- `passo_suplementar.py` — variantes de demônio (já incorporado acima)

**Falta escrever (após o "vai"):** `executar_backfill.py` (cria categorias → aplica lotes com log + rollback) — esqueleto definido neste mapa, ~150 linhas, reusa auth do cofre.

## §7 — Ligação com o Agente V4 Regional

Este mapa **é a Fase 0.5** do projeto V4 Regional: as 27 editorias nascem **já preenchidas** com o acervo histórico (3,3 mil matérias + triagens), o que resolve o "estado vazio" no lançamento e dá SEO imediato por UF. O motor de prioridade (§5 do fórum) passa a ter histórico por UF para o termo de justiça ("dias desde a última matéria").

---

*Ass: Z (ZCode) — 2026-07-30 ~18:30 BRT. Varredura 100% READ-ONLY; nada foi alterado no site.*
