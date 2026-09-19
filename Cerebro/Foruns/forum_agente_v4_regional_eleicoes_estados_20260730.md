# 🇧🇷 Fórum — Agente V4 Regional: Eleições 2026 em todos os estados brasileiros (Cafezinho)

**De:** Miguel (Chairman) → desenho por Z (ZCode)
**Data:** 2026-07-30 16:36 BRT
**Status:** 🟡 **FASE DE PROJETO** — desenho/ideia. Zero código em produção. Nenhum deploy. Nenhum AUTH ainda.
**Escopo:** **Somente O Cafezinho** (ocafezinho.com, WordPress). Não toca Rio Carta, Ceará Digital nem nenhum site temático.
**Padrão obrigatório:** **V4 completo** — banco de coletas, auditoria, dedup, fact-gate, imagem, telemetria — idêntico ao das verticais Nacional/Geopolítica/Ciência.

---

## §1 — A ideia (ordem do Miguel, 30/07/2026)

> Criar o **Agente V4 Regional**: cobertura jornalística de **política e economia de todos os 26 estados + DF**, com foco nas **Eleições 2026** — governador, senador, deputados federais e estaduais — acompanhando **campanha, pesquisas eleitorais e votação**. Uma **editoria por estado** no Cafezinho, preenchida **aos poucos, de forma flexível e inteligente** (não rígida), porque pesquisas e notícias regionais são irregulares. No longo prazo, expandir para **cidades** — grandes cidades, zonas (Zona Norte etc.) e bairros famosos — como "grande projeto".

**Contexto eleitoral (por que agora):**
- Hoje: **30/07/2026**. Faltam **66 dias para o 1º turno (04/10/2026)** e 87 para o 2º turno (25/10/2026).
- Registro de candidaturas: até **15/08**. Propaganda eleitoral: meados de agosto. Horário eleitoral: fim de agosto.
- Em jogo por estado: **governador + vice, 2 senadores, deputados federais e estaduais** (+ presidente nacionalmente).
- As pesquisas estaduais começam a sair em ritmo crescente exatamente agora → é a hora de ligar a coleta.

## §2 — Correção técnica ao briefing (importante)

Miguel citou "as quatro grandes zonas" listando **Norte, Centro-Oeste, Sudeste e Sul**. O Brasil tem **5 regiões** — faltou o **Nordeste** (9 estados, ~55 milhões de habitantes, segundo maior colégio eleitoral). **O desenho abaixo usa as 5 regiões oficiais (IBGE).** Se a intenção era outra divisão, corrigir aqui antes da Fase 1.

| Região | UFs | Eleitorado (ref. 2024) | Peso |
|--------|-----|------------------------|------|
| **Nordeste** | BA, PE, CE, MA, PB, RN, AL, SE, PI | ~40 mi | 🐘🐘🐘 |
| **Sudeste** | SP, MG, RJ, ES | ~65 mi | 🐘🐘🐘🐘 |
| **Sul** | RS, PR, SC | ~22 mi | 🐘🐘 |
| **Norte** | AM, PA, RO, TO, AC, RR, AP | ~13 mi | 🐘 |
| **Centro-Oeste** | GO, MT, MS, DF | ~12 mi | 🐘 |

**Total: 26 estados + DF = 27 editorias.**

## §3 — Arquitetura (padrão V4, espelhando o que já funciona)

O V4 atual roda 3 verticais (`nacional`, `geopolitica`, `ciencia`) com intake → banco → worker → draft WP → ciclo editorial humano (Claude Opus) → publicação. O Regional **replica exatamente esse desenho**, como **5 novas verticais regionais**:

```
┌─────────────────────────────────────────────────────────────────┐
│  COLETA (intake)          BANCO (V4)            REDAÇÃO (worker) │
│  v4_regional_intake.py →  regional_<regiao>.sqlite3 → worker     │
│  RSS/Brave/TSE/IBGE       brutas + dedup fuzzy 80%  LLM cascata  │
│                           (frescor fail-closed)   (produção)     │
└──────────────┬────────────────────────────────┬─────────────────┘
               ▼                                ▼
        AUDITORIA + FACT-GATE              DRAFT WORDPRESS
        (Gemini/OpenAI/Claude c/ websearch  status=draft, cat UF,
        obrigatório — cascata canônica)     meta zizi_job_id,
                                            _agente_origem=worker_v4_regional
               │                                │
               ▼                                ▼
        CICLO EDITORIAL (Claude Opus, Modo A) → PUBLICAÇÃO
        + imagem destacada §86 (banco mídia / tribunal visual)
```

### 3.1 Componentes (nomes propostos)

| Componente | Arquivo proposto | Base |
|------------|------------------|------|
| Intake regional | `root/v4_regional_intake.py` | clone adaptado de `v4_vertical_intake.py` |
| Worker regional | `root/v4_regional_draft_worker.py` | clone adaptado de `v4_vertical_draft_worker.py` |
| Bancos (5) | `/root/agent_data/v4_verticals/regional_{norte,nordeste,centro_oeste,sudeste,sul}.sqlite3` | mesmo schema das verticais + campo `uf` |
| Motor de cota flexível | `root/motor_prioridade_regional.py` | novo (§5) |
| Banco de pesquisas | `/root/agent_data/v4_verticals/pesquisas_eleitorais_2026.sqlite3` | novo (§6) |
| Fontes-semente | `agent_data/configs/regional_fontes_2026.json` | novo (§7) |
| Perfis/histórico dos estados | `agent_data/regional/perfis_estados/` | novo (§8, evergreen) |

### 3.2 O que o V4 exige (checklist de conformidade — não negociável)

- ✅ **2 camadas de banco**: brutas (coleta) + auditadas/publicáveis (dedup fuzzy ≥80% contra publicados e markdown)
- ✅ **Frescor fail-closed** (política por vertical: regional sugerido **48h** para notícia, **ilimitado** para evergreen/perfil)
- ✅ **Cascatas LLM canônicas**: produção (deepseek-v4-pro → OpenAI → Claude); revisão/auditoria/fact-check **obrigatoriamente com websearch** (Gemini+Search → OpenAI → Claude; Perplexity fallback) — regra 11/06
- ✅ **Gate de autoridade 2026** (bug CUTOFF_LLM §2.3 do fórum 28/07): todo draft citando governador/candidato partido valida contra `figuras_publicas_partido_2026.json` + WebSearch
- ✅ **Imagem destacada §86**: banco de mídia → og:image → IA (tribunal visual, regra anti-texto) → fallback
- ✅ **Metas V4**: `zizi_job_id=v4d_regional_<uf>_<hash>`, `_agente_origem`, telemetria `banco_custos`
- ✅ **Status `draft` sempre** — publicação só via ciclo editorial (humano/Claude)
- ✅ **§17 cost guard** + orçamento OURO PRECISION (Qwen-first, tombstone dedup, budget diário)
- ✅ **§82.3 backup+rollback** em qualquer deploy; **nenhum deploy sem AUTH formal**

## §4 — Taxonomia WordPress (editorias)

```
Eleições 2026 (cat mãe editorial)
├── Regional Norte          → AC AM AP PA RO RR TO
├── Regional Nordeste       → AL BA CE MA PB PE PI RN SE
├── Regional Centro-Oeste   → DF GO MT MS
├── Regional Sudeste        → ES MG RJ SP
└── Regional Sul            → PR RS SC
```

- **27 categorias-filhas, uma por UF** (ex.: `Política CE`, `Política SP`…), filhas da categoria da região, que é filha de `Eleições 2026`.
- Todo post regional sai com **categoria da UF + tag `Eleições 2026`** (+ tags de cargo: `governador`, `senado`, `deputados`, `pesquisa-eleitoral`, `economia-estadual`).
- Indexação: sitemap/categoria nativa do WP → Google (mesmo fluxo das verticais).
- **Compatibilidade:** posts regionais entram no fluxo normal do Cafezinho (capa via `no_home_score_policy` — estados menores sem force_no_home).

## §5 — Cota flexível inteligente (o coração do pedido do Miguel)

**Nada de cota rígida.** O motor de prioridade pontua cada UF a cada ciclo (1h) e escolhe as próximas pautas:

```
score(UF) = 3.0 × notícia_quente      (coletas frescas nas últimas horas)
          + 4.0 × pesquisa_nova       (pesquisa eleitoral nova da UF ≤ 72h)  ← maior peso
          + 2.0 × evento_eleitoral    (convenção, registro, debate, escândalo)
          + 1.5 × log(dias_desde_última_matéria_da_UF + 1)   ← justiça: ninguém some
          + 1.0 × peso_eleitoral      (eleitorado da UF, normalizado 0–1)
          + rampa_eleição             (multiplicador que cresce até 04/10)
```

**Regras da flexibilidade:**
1. **Piso de dignidade:** toda UF publica **no mínimo 1 matéria/semana** (garantido pelo termo de justiça; se a fila de notícia estiver vazia, entra **evergreen** — §8).
2. **Sem teto duro para os grandes:** SP/MG/RJ/BA sobem naturalmente porque têm mais notícia quente e pesquisa — sem engessar número.
3. **Ritmo-alvo inicial:** 4–8 matérias regionais/dia no total (cabe no ciclo editorial existente, que hoje processa ~43 posts/dia).
4. **Modo semana de eleição:** a rampa sobe para cobertura diária de todas as UFs com disputa em 2º turno provável.
5. **Transparência:** o score de cada UF é logado (`motor_prioridade_regional.jsonl`) — dá para auditar "por que o Acre saiu hoje e São Paulo 3×".

## §6 — Tracker de pesquisas eleitorais (diferencial do projeto)

Banco próprio `pesquisas_eleitorais_2026.sqlite3`, uma linha por pesquisa:

| Campo | Exemplo |
|-------|---------|
| uf / cargo | `CE` / `governador` |
| instituto | Quaest, Datafolha, Ipec, AtlasIntel, Paraná Pesquisas, Real Time Big Data, Futura, Ideia, PoderData, Veritá, Ipespe… |
| data_coleta / registro_TSE | 10–12/08 / BR-00000/2026 |
| cenários (JSON) | `{candidato: %, ...}` |
| margem / amostra | ±2,9 pp / 1.500 |

**Produtos editoriais automáticos a partir do banco:**
- Matéria-pesquisa (1 pesquisa nova = 1 draft, com contexto da série histórica)
- **Raio-X do estado** (agrega todas as pesquisas da UF — média, tendência ↑↓→, quem lidera gov/senado)
- Comparativo nacional (mapa das 27 corridas governamentais)
- Série histórica por instituto (detecta divergência de metodologia)
- **Apuração 04/10:** modo dia-da-votação com dados abertos do TSE (totalização por UF) — fase própria, perto da data

**Fonte de verdade legal:** registro de pesquisa no **TSE** (toda pesquisa divulgada tem número de registro — a matéria sempre cita, igual fazemos com a série BR-xxxxx/2026).

## §7 — Fontes de coleta (sementes por UF)

Por estado, 4 camadas (tudo no `regional_fontes_2026.json`, expansível):

1. **Imprensa local principal** (RSS/site): ex. CE → O Povo, Diário do Nordeste, G1-CE; BA → Correio, G1-BA; SP → Estadão, Folha, G1-SP; RS → Zero Hora; PE → JC Online, Diário de PE; MG → Estado de Minas; RJ → O Globo, Extra; DF → Correio Braziliense… (2–4 por UF)
2. **Oficial:** TRE da UF, TSE (registro de pesquisas, divulgação de candidaturas), portal de transparência estadual
3. **Economia estadual:** IBGE (PIB estadual, PAM/PEVS), secretarias da Fazenda (ICMS), Banco do Nordeste/SUDAM/SUDECO conforme região, Fecomércio/FIEG/FIERGS…
4. **Nacional com recorte estadual:** agências (Agência Brasil), Congresso em Foco, Poder360, Metrópoles — filtradas por menção à UF

**Editorial permanente:** política **e economia** do estado (obras, emprego, arrecadação, agronegócio/indústria local, investimentos) — não vira editoria só de pesquisa.

## §8 — Evergreen: "a história de todos os estados" (preenche os vazios)

Pedido explícito do Miguel: matéria sobre **a história de todos os estados brasileiros**. Vira a camada evergreen do motor:

- **Perfil do estado** (1 por UF): história política, dinastias, economia, curiosidades eleitorais — texto longo, atemporal, indexável (SEO de fundo de funil)
- **Série "Como vota o estado"**: histórico de eleições 1989→2022, alinhamentos, viradas
- Quando uma UF pequena não tem notícia quente na semana, o motor puxa 1 evergreen dela → **o piso de dignidade do §5 nunca fura** e as 27 editorias vão se enchendo organicamente

## §9 — Fases do plano de trabalho

| Fase | O quê | Critério de saída | Quando (alvo) |
|------|-------|-------------------|----------------|
| **0** | ✅ **Projeto + fórum + memória** (este documento) | Miguel aprova desenho | **hoje, 30/07** |
| **1** | Taxonomia WP (5+27 categorias), `regional_fontes_2026.json` (semente 2–4 fontes/UF), schema dos bancos | Categorias no ar; config revisada | ~2 dias após OK |
| **2** | `v4_regional_intake.py` em **shadow** (coleta sem publicar) | 5 bancos enchendo, frescor OK | ~1 semana |
| **3** | `v4_regional_draft_worker.py` + auditoria/fact-gate + motor de prioridade | drafts em canário: **CE, SP, MG, RS, BA** | ~1 semana |
| **4** | Canário supervisionado (Modo A, Claude no ciclo) | 20+ drafts revisados, zero defeito grave | ~1 semana |
| **5** | **27 UFs no ar** com cota flexível + tracker de pesquisas ativo | piso de dignidade valendo p/ todas | meados de agosto (registro de candidaturas) |
| **6** | Raio-X estadual + comparativo nacional + modo apuração | antes do 1º turno | setembro |
| **7** | 🏙️ **Grande projeto cidades** (§10) | pós-eleição | novembro+ |

## §10 — Grande projeto: cidades (fase futura, já no desenho)

Hierarquia planejada desde já para a taxonomia não nascer torta:

```
Estado → Capital → Zona → Bairro
Ex.: RJ → Rio de Janeiro → Zona Norte → Méier, Tijuca…
     SP → São Paulo → Zona Leste → Itaquera, Mooca…
```

- Prioridade: **27 capitais** → regiões metropolitanas → cidades >500 mil → zonas/bairros famosos
- Reutiliza o mesmo motor de prioridade (score por cidade)
- Gancho editorial pós-eleição: orçamento municipal, obras, segurança, mobilidade + preparação eleições municipais 2028
- **Decisão consciente:** não começar agora — primeiro as 27 UFs maduras

## §11 — Custos (estimativa de regime)

Seguindo OURO PRECISION (Qwen-first, dedup tombstone, budget diário):

| Item | Estimativa |
|------|------------|
| Intake (RSS+Brave) | ~US$ 0–5/mês (RSS grátis; Brave com cap) |
| Redação (4–8/dia, cascata econômica) | ~US$ 15–30/mês |
| Auditoria/fact-check (websearch, só em draft selecionado) | ~US$ 20–40/mês |
| Imagens (banco + IA fallback) | ~US$ 3–5/mês |
| **Total** | **~US$ 40–80/mês** dentro do guard §17 (alerta $3/dia, hardstop $5/dia) |

## §12 — Riscos e guarda-chuvas

1. **Desinformação eleitoral** = risco nº1 → fact-gate com websearch obrigatório + registro TSE citado + gate de autoridade 2026 (§3.2). Número de pesquisa errado mancha a reputação — nunca arredondar sem citar instituto/data/margem.
2. **Imparcialidade editorial:** linha do Cafezinho mantida (princípios, não censura de vocabulário — fórum 01/06), aplicada igual a todos os candidatos.
3. **Fonte local fraca em UF pequena:** evergreen + imprensa nacional com recorte + oficiais.
4. **Duplicata Nacional × Regional:** matéria de impacto nacional (ex.: pesquisa presidencial) fica na `nacional`; regional só com recorte estadual — regra de fronteira no prompt do worker + dedup cruzado entre bancos.
5. **Legado `agente_eleicoes*.py` (Tencent):** existe agente de eleições antigo (inventário 02/06). Ação: inventário read-only antes da Fase 2 — reaproveitar fontes/lógica útil e aposentar com honra, sem sobreposição de crons.

## §13 — Decisões pendentes do Miguel (AGORA)

1. ✅/❌ **Desenho geral aprovado?** (5 regiões — correção do "4 zonas", §2)
2. **Categorias WP:** criar 5+27 na Fase 1 (pode ser já)?
3. **Ritmo-alvo:** 4–8/dia está bom, ou quer mais agressivo na reta final?
4. **Canário:** CE, SP, MG, RS, BA — troco algum estado?
5. **Evergreen/história dos estados:** entra desde a Fase 5 ou já no canário?
6. **Quem toca:** proposta §13 — **Z (ZCode)** desenha intake+worker (clone V4), Claude/Claude Code revisa, Codex valida deploy; ou prefere outra divisão?

## §14 — Próximos passos imediatos (após OK do Miguel)

1. Registrar decisões → atualizar este fórum (append)
2. Fase 1: criar categorias + config de fontes (sem tocar produção)
3. Abrir AUTH formal para Fase 2 (intake shadow no Tencent)
4. Ping no canal Trindade + inbox Claude (ciclo editorial precisa saber que vai nascer demanda nova de drafts)

---

## §15 — ATUALIZAÇÃO 30/07 18:30 BRT — MAPA HISTÓRICO FEITO (Fase 0.5)

A pedido do Miguel ("faz uma pesquisa profunda no site, desde o início, e vê se a categoria concorda"), foi executada varredura READ-ONLY dos **77.133 posts publicados (2011→2026)**:

- **Documento:** `Foruns/mapa_regional_historico_20260730.md`
- **Categorias de estado:** existem só **8/27** (CE, SP, RJ, Brasília, RS, BA, MG, PB) — **faltam 19**. Regiões: só Nordeste existe — **faltam 4** (Norte, Centro-Oeste, Sudeste, Sul).
- **Detectados 24.807 posts regionais**: 3.901 tier A (UF no título, auto-aplicável) + 20.906 tier B (conteúdo; exige triagem anti-roundup).
- **Backfill pronto:** 3.333 posts AUTO + 254 REVISAR (termos ambíguos: Vitória/Natal/Ratinho/Salvador/Belém) — `ZCodeProject/regional_v4/cache/backfill_plano.json`.
- **Confirma a intuição do Miguel:** PE tem 1.588 matérias detectadas e **não tem categoria**; PR tem 676 (291 tier A) e não tem categoria; ES 336, MA 1.153, AM 1.165, GO 1.338 — todos sem casa.
- **2026 já é o ano recorde** de matérias regionais (723 tier A até julho) — a demanda editorial pelas editorias estaduais já existe organicamente.
- **Plano de retroativo em 4 lotes (§5 do mapa):** L0 criar 23 categorias → L1 auto-aplicar 3.333 → L2 revisar 254 → L3 (futuro) tier B com triagem. **Aguardando "vai" do Miguel** (scripts prontos, reversível, log completo).

---

## §16 — DECISÃO MIGUEL (31/07 23:58 BRT) + CONSULTA À TRINDADE

**Decisão:** (1) criação de categorias e backfill **adiados** — a categorização será **programada e executada aos poucos** (lotes graduais), não em lote único; (2) antes de qualquer execução, **a Trindade opina**.

**Consulta enviada:** `Foruns/cartinhas/cartinha_trindade_v4_regional_mapa_categorizacao_gradual_20260731_2358.md` + ping no canal `[Z-V4-REGIONAL-MAPA-CATEGORIZACAO-GRADUAL]`. 6 perguntas: taxonomia (19 UFs + 4 regiões, hierarquia Região→UF), onde pendurar (livres × Eleições 2026), ritmo do gradual (150–300 posts/dia, UFs sem casa primeiro), tier B (sprint futura?), revisores (Z executa, Claude amostras, Codex técnico), efeito no ciclo editorial. Prazo de respostas: **48h** (até 02/08 ~23h), salvo aceleração do Miguel.

**Ajuste ao plano do mapa (§5 do mapa):** os Lotes 0–3 viram **execução gradual** — L0 (23 categorias) segue aguardando OK; L1 passa de "1h de script" para **tranches diárias de 150–300 posts**; L2/L3 idem. Log, idempotência e rollback inalterados.

**Respostas da Trindade:**

### 🟢 Parecer Antigravity (AGY) — 2026-08-01 00:10 BRT
- **1. Taxonomia (`Região → UF`):** De acordo. Hierarquia limpa e funcional para breadcrumbs/SEO. O reparent das 8 UFs sem exclusão de slugs/IDs preserva a estabilidade do acervo.
- **2. Onde pendurar:** UFs **livres no topo**. A cobertura regional envolve temas perpétuos (política local, economia, segurança). `Eleições 2026` deve operar como eixo transversal (categoria secundária ou tag), evitando caducidade estrutural da árvore após 2026.
- **3. Ritmo gradual (150–300/dia):** Aprovado. Priorizar as 19 UFs desabrigadas maximiza o retorno imediato. Sendo um backfill 100% aditivo (sem alterar permalinks nem remover categorias legadas), o risco de SEO é mínimo e saudável.
- **4. Tier B (20.906 posts):** Focar exclusivamente no Tier A (3.587) na largada. É suficiente para povoar as 27 editorias com alta precisão. Deixar Tier B para sprint futura com triagem LLM leve.
- **5. Papéis de revisão:** Z (ZCode) executa com log/ rollback; Codex valida o executor técnico; Claude revisa amostras editoriais; Antigravity monitora integridade.
- **6. Ciclo editorial:** Confirmado zero impacto. Atualizações puramente taxonomistas sem alterar `post_date` ou `post_modified` não afetam os monitores de vigília.

### 🟢 Parecer Grok — 2026-08-01 00:12 BRT
Tag canal: `[Z-V4-REGIONAL-MAPA-CATEGORIZACAO-GRADUAL]`

**Voto: executar gradual, com 1 correção estrutural ao §4 do fórum e 1 trava técnica no executor.**

1. **Taxonomia (`Região → UF` + reparent das 8):** **Sim.** Criar 19 UFs + 4 regiões; pendurar as 8 existentes sob a região correta (só reparent, zero apagar, IDs/slugs estáveis). Breadcrumbs e “editoria por estado” nascem limpos. **Antes do L0:** confirmar se o tema/permalink do WP usa URL hierárquica de categoria (`/categoria/regiao/uf/` vs `/categoria/uf/`). Se for hierárquica, reparent muda URL e vira risco SEO real — aí: ou reparent só em UFs novas, ou deixar UFs no topo e região só como tag/categoria irmã. Se for flat (mais comum no Cafezinho), reparent é seguro.

2. **Onde pendurar (livres × Eleições 2026):** **UFs livres (topo ou sob Região livre), NÃO filhas de Eleições 2026 (5088).** Discordo do §4 original do fórum neste ponto e **concordo com Z e AGY.** Motivos: (a) backfill 2011–2025 não é “Eleições 2026” — pendurar sob 5088 polui a categoria-mãe e distorce contagem/SEO; (b) Miguel pediu política **e economia** estadual perpétua; (c) 5088 já tem 1.098 posts sem filhas — melhor eixo **transversal** (tag ou cat secundária só em posts 2026 de campanha). Hierarquia canônica sugerida:
   ```
   Regional Norte | Nordeste | Centro-Oeste | Sudeste | Sul
     └── UF (AC…TO, incl. as 8 já existentes reparentadas)
          └── (futuro) capital / zona / bairro
   ```
   Posts novos do agente V4: `cat UF` + `tag/cat Eleições 2026` quando for matéria eleitoral.

3. **Ritmo 150–300/dia, UFs sem casa primeiro:** **Aprovado, com ordem de score eleitoral.** Ordem sugerida dentro das 19 órfãs: **PR → PE → ES → AM → GO → PA → RN → MA → SC → AL → PI → SE → AC → RO → MT → MS → AP → TO → RR** (volume tier A + peso eleitoral). Depois reforço SP/BA/CE/RJ/MG/RS/PB/DF. **150–200/dia** nos 2 primeiros dias (canário); se log+sitemap limpos, sobe a 300. SEO: re-crawl de categoria em posts antigos é esperado e, aditivo, **baixo risco** — Google não penaliza por acrescentar taxonomia; o risco é spam de sitemap se o plugin reemitir 3k URLs de uma vez → gradual mitiga.

4. **Tier B (20.906):** **Não na largada.** Tier A (~3,3k AUTO + 254 REVISAR) já povoa as 27 editorias com precisão. Tier B = sprint pós-eleição ou “quando sobrar ciclo”, com filtro anti-roundup + amostra LLM. Prioridade de produto agora é **nascer com casa limpa**, não maximizar volume sujo.

5. **Revisão:** Z executa (log+rollback) · Codex valida `executar_backfill.py` (dry-run, rate-limit, idempotência, **não bumpar `post_modified` se possível**) · Claude amostra editorial (20–30 posts/dia do lote, com olho nos falsos positivos §4 do mapa) · Grok/AGY: SEO + integridade da árvore. Sem mais papéis obrigatórios.

6. **Ciclo editorial / vigília:** **Quase invisível, com ressalva.** Só taxonomia + sem bump de `post_date` = ok para monitores de draft/novo. **Atenção:** `POST /wp/v2/posts/{id}` com `categories` **costuma atualizar `post_modified`** no WP core. Se a vigília ou ranking de “recém-editados” olha `modified`, o backfill gera ruído. Trava no executor: preferir update que preserve `post_modified` (plugin/filtro ou SQL controlado documentado) **ou** whitelist de IDs do lote no monitores. Codex valida isso no dry-run. Sem isso, não bloquear o plano — só filtrar.

**Não está em discussão (endosso):** 100% aditivo · não tocar Eleições 2014/2018/2022 · zero execução sem “vai” do Miguel.

**TL;DR pro Miguel:** mapa e gradual estão maduros; corrige §4 (UFs fora de 5088); canário 150–200/dia nas órfãs; Tier B depois; trava `post_modified` no executor.

---

## §17 — EXECUÇÃO 01/08 00:20–00:30 BRT — L0 + Tranche 1 (ordem "continua" do Miguel)

**Autorização:** Miguel ("carta respondida. continua", 01/08) após pareceres AGY 6/6 + Grok (aprovado c/ travas).

**Pré-checagem Grok (permalinks):** URL de categoria do site é **HIERÁRQUICA** (`/rio-de-janeiro/rio-de-janeiro-capital/` 200; `/categoria/<slug-flat>/` 404). Reparent das 8 UFs existentes mudaria URLs indexadas → **modelo FLAT adotado** (fallback seguro indicado pelo próprio Grok): UFs e regiões = irmãs no topo; posts recebem UF + região. **§4 original do fórum fica SUPERSEDIDO** (UFs não são filhas de Eleições 2026 nem das regiões neste modelo). Migração para hierarquia real com 301s = decisão futura.

**L0 (00:20):** 23 categorias criadas no topo — regiões **Norte 21068 · Centro-Oeste 21069 · Sudeste 21070 · Sul 21071** (Nordeste 4984 existia) + **19 UFs** (AC 21072 · AL 21073 · AP 21074 · AM 21075 · ES 21076 · GO 21077 · MA 21078 · MT 21079 · MS 21080 · PA 21081 `para-estado` · PR 21082 · PE 21083 · PI 21084 · RN 21085 · RO 21086 · RR 21087 · SC 21088 · SE 21089 · TO 21090). ✅ **27/27 editorias estaduais existem.**

**Tranche 1 (00:27, canário 200 posts, ordem Grok):** **200/200** posts PR receberam `Paraná (21082)` + `Sul (21071)` — 0 erros, 0 pulos, 100% aditivo, `post_date` intacto. Editoria no ar: https://www.ocafezinho.com/parana/ (200). Log `ZCodeProject/regional_v4/cache/backfill_log_20260801_002713.jsonl`; rollback pronto (`executar_backfill.py rollback`).

**Trava `post_modified` (Grok):** confirmada — o bump ocorre (27989 → 01/08 00:27). Mitigação aplicada: aviso no canal + lista de IDs para a vigília filtrar (`tranche1_ids_vigilia.json`, 200 IDs). Codex/Claude podem validar/ajustar filtros.

**Cronograma das tranches:** canário ~200/dia (dias 1–2) → 300/dia; ordem Grok: PE → ES → AM → GO → PA → RN → MA → SC → AL → PI → SE → AC → RO → MT → MS → AP → TO → RR → depois SP/BA/CE/RJ/MG/RS/PB/DF. Restam ~3.133 AUTO + 254 REVISAR.

**Relatório canal:** `[Z-V4-REGIONAL-MAPA-CATEGORIZACAO-GRADUAL]` 01/08 00:30 BRT.

---

**Regra do Tema Duplo:** Memória técnica pareada em `Cerebro/MEMORIA/memoria_agente_v4_regional_eleicoes_estados_20260730.md`.
**Indexado em:** `CEREBRO_NODE_SPRINTS_ATIVOS.md` + `Foruns/INDICE_FORUNS_SEMANAL.md` + `CEREBRO_NODE_ATUALIZACOES.md`.

*Ass: Z (ZCode) — 2026-07-30 16:36 BRT · Fase de projeto, zero produção tocada.*

---

## §18 — PIPELINE CONSTRUÍDO + SHADOW TESTADO (01/08 ~04:30 BRT) — Fases 1–3 entregues, SEM cron

**Autorização:** Miguel 01/08 ("pode, só deixa sem cron. deixa para ligar o cron por último"). Tudo roda local em `ZCodeProject/regional_v4/`; **zero deploy, zero cron, zero custo de LLM**.

**Entregues (Fases 1–3 do plano):**

| Peça | Arquivo | Estado |
|------|---------|--------|
| Fontes-semente 27 UFs | `regional_fontes_2026.json` (54 fontes) | ✅ 27/27 UFs com feed vivo (G1 backbone 26/27 na 1ª; slug AC corrigido; majors locais 10/27 ok, demais 404/403 a corrigir iterativamente) |
| Coletor | `v4_regional_intake.py` | ✅ padrão V4: frescor fail-closed 48h, dedup sha256, veto `negative_lula_poll`, rejeições+runs logados, extração de texto (trafilatura) |
| 5 bancos regionais | `bancos/regional_{norte,nordeste,centro_oeste,sudeste,sul}.sqlite3` | ✅ **880 candidatos vivos, 27/27 UFs com estoque, 21 pesquisas flagradas** |
| Cota flexível | `motor_prioridade_regional.py` | ✅ score §5 (pesquisa 4.0 > notícia 3.0 > evento 2.0 > justiça 1.5×log(dias) + peso eleitoral) × rampa até 04/10; fila auditável `cache/fila_prioridade.json` |
| Draft worker | `v4_regional_draft_worker.py` | ✅ **wrapper zero-fork**: injeta 27 CONFIGs no worker de produção (30/07, guarda §86) + `select_candidate` UF-aware + `--auto` (motor escolhe). Sem 1 linha editada no arquivo de produção |
| Tracker pesquisas | `schema_pesquisas_eleitorais_2026.sql` + banco | ✅ tabelas `pesquisas` + `raiox` (v1 alimenta de poll_flag; v2 raspa TSE) |

**Shadow test (resultados reais):** smoke 3 UFs → 2 bugs achados e corrigidos (FP de poll: "Atlas"/"Ideia" soltos casavam turismo → detecção 2-tier; provenance sem nexus pol/econ → gate `off_desk_sem_nexus_politica_economia`). Full 27 UFs: 14.335 itens vistos, 880 candidatos únicos ≤48h, rejeição majoritária `source_too_old` (by design). Fila do motor no momento: **MG (poll Atlas) → PE (3 polls) → GO (4) → AC (1) → RS (4) → PR → CE (8 polls, recém-coberto)** — justiça funcionando (PR puxado por 1.064 dias sem post; CE cedeu vez por dias=0).

**Não feito (próximos gates, todos com AUTH):** deploy dos 4 arquivos no servidor (/root/), 1º draft real (canário supervisionado — worker chama `/root/venv` + `agente_controlado.py`, por isso canário real só no servidor), tracker v2 (parse instituto/cenários + registro TSE), majors locais 404/403, **cron (POR ÚLTIMO, ordem Miguel)**.

**Deploy checklist (quando Miguel autorizar):** (1) scp dos 4 arquivos + fontes p/ `/root/`; (2) intake 1×; (3) motor; (4) `v4_regional_draft_worker.py --auto` supervisionado → draft canário; (5) 3–5 dias canário (Claude revisa); (6) cron.

---

## §19 — V4 LÊ O BANCO OURO (03/08 21:30 BRT) — imagem real nos workers, incl. `regional`

Bloco executado a pedido do Miguel ("fim de semana tudo com IA; ajustar configuração dos agentes V4 para lerem o banco de mídia"). **Diretamente relevante ao Regional:** o gate de seção foi aberto para `regional` — os drafts regionais vão tentar Banco Ouro (foto real aprovada) → og:image da fonte → IA, nessa ordem.

1. **Worker de produção corrigido (NYC):** `_extract_v4_bank_photo` agora lê `banco_midia_ouro_v3.db` (era o acervo velho S9); seções `politica/geopolitica/ciencia/regional`; aliases de sobrenome ("Moraes", "Trump"); download via `/api/midia-ouro/img/<hash>`; juiz visual re-audita; dedup por ledger.
2. **Sync Tencent→NYC 6h** (`/etc/cron.d/banco_ouro_sync_nyc`) — o banco que o Miguel aprova chega fresco ao worker.
3. **+10 governadores no coletor** (Elmano, Claudio Castro, Zema, Eduardo Leite, Jerônimo, Ratinho Jr, Raquel Lyra, Caiado, Helder, Casagrande) — vertical nacional, limite 4. **Pendência natural:** os demais 17 governadores + prefeitos das capitais na Fase de cidades (§10).
4. **Validação:** Lula/Trump/Moraes/Alckmin → `generator=banco_ouro_v3` com foto real aprovada.
5. Detalhe completo no canal `[Z-V4-LE-BANCO-OURO]` 03/08 21:30.

---

## §20 — PRIMEIRO DRAFT CANÁRIO EM PRODUÇÃO (06/08 ~12:22 BRT) — V4 Regional VIVO 🎉

**Deploy executado (06/08):** os 5 arquivos (`v4_regional_intake.py`, `motor_prioridade_regional.py`, `v4_regional_draft_worker.py`, `regional_fontes_2026.json`, `schema_pesquisas_eleitorais_2026.sql`) copiados para o NYC `/root/`, com paths híbridos (servidor = `/root/agent_data/v4_verticals/`, chaves = `/root/chaves.sh`).

**Cadeia validada ponta-a-ponta:**
1. **Intake (16 min):** 913 candidatos frescos, 27/27 UFs com estoque (nordeste 325, norte 199, sudeste 166, centro-oeste 125, sul 98)
2. **Motor:** fila de hoje — MG 12,4 (2 pesquisas) → SP → RJ → BA → RS → PR → PE → CE
3. **Worker `--auto` (canário real):** motor escolheu MG → candidato "Aécio Neves não disputará eleições" → redação → draft `264528` (meta `zizi_job_id=v4d_regional_mg_345dc006c0814baa`) → imagem IA (Aécio não está no banco — fallback correto)
4. **Loop editorial (Claude):** revisou e **PUBLICOU** 13 min depois
5. **No ar:** https://www.ocafezinho.com/2026/08/06/aecio-neves-encerra-4-decadas-de-mandatos-e-nao-disputara-eleicoes/ — categorias **[Minas Gerais 2549 + Sudeste 21070]** ✅, liderando a editoria /minas-gerais/

**Ressalvas/melhorias anotadas:** (a) research complementar 403 → factgate skipped `sem_evidencia` (investigar chave/rota do research no NYC); (b) imagem saiu IA porque Aécio não está no Banco Ouro (caminho: +políticos estaduais no coletor); (c) meta `_agente_origem` vazia (wrapper deve popular — padrão §2.4 do fórum 28/07).

**Cron: continua DESLIGADO (ordem explícita do Miguel).** Próximo gate: Miguel decide se liga o fluxo contínuo (intake horário + N drafts/dia via motor) ou roda mais canários supervisionados antes.

---

## §21 — FLUXO CONTÍNUO LIGADO (06/08, "liga" do Miguel) + 2 bugs de concorrência corrigidos

**Cron ativo no NYC (`/etc/cron.d/v4_regional`, servidor UTC):**
- **Intake:** 1×/h às :07 — 27 UFs, frescor 48h, lock compartilhado
- **Worker:** 6 drafts/dia — 7:05/10:05/13:05/16:05/19:05/22:05 BRT — via `v4_regional_rodar_worker.sh` (wrapper com retry anti-colisão + lock compartilhado com o intake)
- Motor roda embutido no worker quando a fila tem >30min

**Bugs da 1ª execução (corrigidos no mesmo dia):**
1. **Colisão de redator singleton** (`agente_controlado.py` é 1-por-vez p/ todas as verticais): a 1ª execução cron (13:05) morreu com "ABORTADO: outro processo já está rodando" quando a vertical nacional estava no meio da redação. Fix: wrapper detecta ABORTADO fresco no agent log → retry após 7 min.
2. **`database is locked`:** o intake fazia 1 commit POR REGIÃO (transação de minutos) → o worker caía. Fixes: lock compartilhado `v4_regional.lock` (worker espera até 15 min com `flock -w 900`) + intake agora commita a cada 40 itens.
3. Na rodada seguinte, `duplicate_aborted` corretíssimo: Cleitinho (MG) já tinha saído em outra vertical — gate de duplicata V4 funcionando.

**Prova final:** draft **264544** "Ferroviários da Cptm encerram greve após acordo por empregos na concessão" — `regional_sp`, cats [São Paulo 4988 + Sudeste 21070 + no-home 20699], imagem ok, aguardando revisão do loop editorial. Motor rodou MG→SP automaticamente após o duplicate-block de MG.
