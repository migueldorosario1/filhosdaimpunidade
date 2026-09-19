# 📋 POLÍTICA DE CATEGORIAS — O Cafezinho (publicação futura disciplinada)

> **Fórum CANÔNICO — whitelist APROVADA pelo Miguel (12/08 23:10).**
> **Princípio-chave (ordem Miguel):** *"a whitelist está ótima. O resto pode ser tag."* → **tudo que não está na whitelist vira TAG, nunca categoria nova.** As categorias antigas (autores, redundâncias, obsoletas) são **arquivo morto** — não recebem posts novos nem são apagadas.
> **Data:** 12/08/2026 23:07 BRT · **Autor:** ZCode (GLM-5.2, fallback — Kimi/Qwen 🔴🔴)
> **Origem:** Miguel — *"não vamos apagar nenhuma categoria agora. Vamos organizar e, a partir de agora, apenas publicar em categorias específicas, poucas, organizadas. Vamos estabelecer uma política para categorias."*
> **Abordagem:** 🎯 **não mexer no histórico** (zero risco SEO/redirect) — as categorias antigas viram **arquivo morto** naturalmente. Disciplinar **só a publicação nova** via whitelist + aplicação em agentes/mu-plugin.
> **Relacionado:** `forum_grande_limpeza_taxonomia_cafezinho_20260812.md` (diagnóstico + análise SEO — a "faxina" do passado fica pausada).

---

## 1. Princípios da política

1. **Poucas categorias oficiais** (whitelist) para toda publicação nova.
2. **2 eixos only:** Tema (editorial) + Geografia (até estado).
3. **Cidade / país / pessoa / evento / série = TAG** (nunca categoria nova).
4. **Categorias antigas (autores, redundâncias, obsoletas) = ARQUIVO** — não recebem posts novos, mas **não são apagadas** (sem redirect, sem risco SEO).
5. Todo post novo **deve ter ≥1 categoria da whitelist** (ideal: 1 editorial + 1 geografia se aplicável).
6. **Safety net:** se nada encaixar, cai em "Redação/Geral" (2403) + tag específica.

---

## 2. WHITELIST — categorias OFICIAIS para publicação nova

### Eixo A — EDITORIAIS (temas)  · ~17 categorias

| Categoria | ID | Posts (12/08) | Observação |
|---|---|---|---|
| Política | 22 | 12.866 | Absorve implicitamente Golpe/Fascismo/Congresso/STF/Eleições (via tag) |
| Internacional | 15 | 8.361 | |
| Economia | 43 | 6.293 | Absorve Petrobrás/Agro/BNDES/Mercado (via tag) |
| Geopolítica | 5003 | 5.913 | Absorve Guerra/países (via tag) |
| Tecnologia | 30 | 1.282* | *cresceu: concentrou Ciência+IA (decisão 22:56) |
| ↳ Ciência | 735 | 1.150 | subcategoria de Tecnologia |
| ↳ Inteligência Artificial | 5008 | 623 | subcategoria de Tecnologia |
| Saúde | 258 | 663 | |
| Meio Ambiente | 582 | 696 | |
| Energia | 98 | 703 | petróleo + elétrica |
| Justiça | 1335 | 1.547 | STF/Lava-Jato/Corrupção (via tag) |
| Direitos Humanos | 358 | 888 | |
| Mídia | 23 | 1.234 | crítica de mídia |
| Educação | 1479 | 343 | |
| Segurança | 36 | 370 | |
| Cultura | 79 | 353 | Cinema/Música/Literatura (via tag) |
| Esporte | 1271 | 210 | |

> ✅ **Bate com o que os agentes V4 já usam** (22/15/43/5003/30/735/79/258/582/1271) — a maior parte da política já é seguida na prática.

### Eixo B — GEOGRAFIA (até estado; cidade = tag)

| Categoria | ID | Observação |
|---|---|---|
| Regional | 4986 | raiz (guarda-chuva) |
| ↳ Sudeste / Sul / Nordeste / Norte / Centro-Oeste | 21070 / 21071 / 4984 / 21068 / 21069 | 5 regiões |
| ↳↳ 27 unidades federativas | vários | 26 estados + **DF (Centro-Oeste)** — cat DF = **21139** (slug `distrito-federal`, criada 12/08) |

**Cidade = TAG** (não categoria): **Brasília**, Rio de Janeiro, São Paulo, Niterói, BH, etc. *A categoria "Brasília" (5710) já existente = arquivo morto.*

### Eixo C — TRANSVERSAIS (operacionais)

| Categoria | ID | Uso |
|---|---|---|
| Redação | 2403 | "Geral" / safety-net (37.385 posts — catch-all histórico; considerar renomear para "Geral") |
| Vídeos | 28 | formato (agente YouTube) |
| Headline / Manchete | 5087 | operacional do agente manchete |

---

## 3. CATEGORIAS FECHADAS (arquivo — NÃO publicar mais, NÃO apagar)

Estas **continuam existindo** (posts antigos permanecem, URLs indexadas preservadas), mas a **política proíbe publicar novo nelas**:

- **~45 nomes de autores/colunistas** (Rhyan de Meira, Clarice, Ruann, Letícia, Cleber, Gabriel, Pedro Breier, etc.) → classificação de autor passa a ser via `post_author` + tag.
- **Redundâncias temáticas** (Guerra, Golpe, Metagolpe, Fascismo, Ditadura, STF, Senado, Congresso, Câmara, Lava-Jato, Corrupção, Petrobrás, Petróleo, BNDES, Agro, Mercado, Esportes, Eleições 2014/16/18/20/22/24, "Ciência e Tecnologia" 19936, Youtube 20751, etc.).
- **Formato obsoleto** (Notas Urgentes, Duplo Expresso, Cafezinho no Almoço, Clipping, Boatos, etc.).

> Estes posts ficam acessíveis; novos posts do mesmo tema vão para a **editorial da whitelist** + **tag específica** (ex.: post sobre STF → categoria **Justiça** + tag **stf**).

---

## 4. REGRA DE PUBLICAÇÃO (aplicável a agentes LLM e humanos)

1. **≥1 editorial** da whitelist (Eixo A) em todo post novo.
2. Se o post tem ângulo **geográfico relevante** (não só menção), adicionar **Regional ▸ região ▸ estado** (Eixo B) — opcional, não obrigatório.
3. **Cidade / país / pessoa / evento** → **TAG** (nunca criar categoria nova).
4. **NUNCA** usar categoria de autor (Eixo "fechadas").
5. **Safety net:** se nenhum editorial encaixar → **Redação (2403)** + tag específica + revisão editorial.
6. **Tags:** livres, mas **sem `#`**, **sem duplicação de slug**, **sem título-quebrado** (palavras do título não viram tag).

---

## 5. APLICAÇÃO (como impor a política)

### 5.1 mu-plugin `cafezinho-politica-categorias.php` (hook `save_post`)
Faseado, do mais brando ao mais forte:
- **Fase 1 — LOG (2 semanas):** registra em `/root/log_politica_categorias.log` todo post novo cuja categoria está fora da whitelist; **não bloqueia**. Gera relatório semanal.
- **Fase 2 — WARN:** adiciona meta `_politica_violacao` (visível no wp-admin / REST) para posts fora da whitelist.
- **Fase 3 — ENFORCE:** reatribui automaticamente ao safety-net (Redação/Geral) + notifica editor.
- Anti-recursão, só em `publish`/`draft`, nunca em `trash`.

### 5.2 Guia editorial canônico
`Cerebro/cartoes_bolso/CARTAO_BOLSO_POLITICA_CATEGORIAS.md` — 1 página com a whitelist + regras, para qualquer agente LLM (Grok/Claude/ChatGPT/Codex/Kimi/Qwen/GLM) saber **exatamente onde publicar**. Integrar ao `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md`.

### 5.3 Config dos agentes
Revisar `CAT_*_ID` de todos os agentes contra a whitelist:
- V4 verticais (nacional→22, geopolítica→5003, economia→43, cultura→79, ciência→735, meio_ambiente→582, esporte→1271, saúde→258) ✅ já batem.
- `agente_youtube` → 28 (Vídeos) ✅; `agente_manchete` → 2403+5087 ✅.
- Verificar agentes-irmãos (repetidor_estatal, etc.) — alinhar.

### 5.4 Monitoramento semanal
Relatório "posts publicados fora da whitelist na semana X" → detecta agente desalinhado ou LLM criando categoria nova.

---

## 6. Decisões pendentes do Miguel (para eu implementar)

1. **Whitelist de editoriais (Eixo A, ~17)** está OK? Quer **tirar** ou **adicionar** alguma?
2. **Geografia:** confirmar **4 ou 5 regiões**? Crio o **DF**? (mesma pendência do menu hambúrguer)
3. **"Redação" (2403)** — renomeio para **"Geral"** (mais claro como safety-net)? Ou mantém "Redação"?
4. **Aplicação:** começo pela **Fase 1 LOG** (2 semanas só observando, sem bloquear)? — recomendado.
5. **Guia editorial** vira `CARTAO_BOLSO_POLITICA_CATEGORIAS.md` + integra ao nodo de publicação? — recomendado.

---

## 7. Estado da missão

- **O que aconteceu (12/08 23:07):** Miguel mudou a diretriz — não apagar categorias, focar em política de publicação. Pausei a automação de faxina (STATUS:PAUSADO). Esbocei esta política.
- **O que está PRONTO:** princípios + whitelist proposta + regras + plano de aplicação faseado.
- **O que FALTA:** Miguel validar a whitelist (§6.1) + confirmar aplicação Fase 1 LOG (§6.4) → então eu crio o mu-plugin (log-only) + o cartão-bolso + reviso config dos agentes.
- **O que preciso do Miguel:** as 5 respostas do §6 (ou só "aprova, vai na Fase 1 LOG" que eu começo pelo mais seguro).
- **Próximo passo (se Miguel aprovar):** (a) criar `CARTAO_BOLSO_POLITICA_CATEGORIAS.md`; (b) mu-plugin Fase 1 LOG no espelho primeiro; (c) revisar `CAT_*_ID` dos agentes; (d) relatório semanal baseline.

---

## 8. Catalogação
- Fórum (este): `Foruns/forum_politica_categorias_cafezinho_20260812.md`
- A derivar: `CARTAO_BOLSO_POLITICA_CATEGORIAS.md` + mu-plugin `cafezinho-politica-categorias.php`
- Nodos: `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` + `CEREBRO_NODE_ATUALIZACOES.md`

---

## 9. EVOLUÇÃO (13/08 ~14:10) — Menu como fonte de verdade + categoria-âncora + submenus

> **Origem:** Miguel — *"Deixa eu acabar a reforma do cafezinho (o menu). Tem categorias órfãs que só servem pra orientar, tipo Região Norte — não tem post mas tem os estados. Não vamos apagar as categorias regionais. O que não tiver no menu a gente pode apagar. Categoria-base como Eleições vai ter submenu (2026, 2024...). Mesma lógica pra tudo. Não com pressa — só anota."*

### 9.1 Princípios revistos (superam os anteriores em caso de conflito)
1. 🧭 **O MENU é a fonte de verdade da taxonomia** — não o `count`. O que estrutura o menu, fica.
2. 🏷️ **Categoria-âncora de menu:** uma categoria pode ter **0 posts** e ser **essencial** — é só um **cabeçalho de navegação** que abre submenu. Ex.: "Região Norte" (0 posts diretos, mas abre Amazonas/Pará/...). **Essas NUNCA se apagam**, mesmo com count=0.
3. 🧹 **Critério de limpeza REVISTO:** **NÃO** usar `count=0` como critério (é ambíguo — vira tanto tag órfã quanto categoria-âncora de menu). Candidata a apagar = o que **não está no menu E não é submenu** (e mesmo assim, com gate humano + paciência).
4. ⏸️ **Faxina PAUSADA** até o Miguel acabar a reforma do menu. O menu final define o que fica.

### 9.2 Estrutura de SUBMENUS proposta (idéias do Miguel — a confirmar conforme a reforma avança; não executar agora)
| Categoria (cabeçalho) | Submenus sugeridos |
|---|---|
| **Eleições** | 2026 · 2024 · 2022 · 2018 · 2016 · 2014 (as que existirem) |
| **Cultura** | Cinema · Teatro · Literatura · Televisão · Streaming · Artes Plásticas |
| **Geopolítica** | Irã · Guerras · (+ países/conflitos conforme surgirem) |
| **Tecnologia** | Inteligência Artificial |
| **Economia** | Agricultura · Pecuária · Indústria · Comércio · Serviços · Emprego |
| **Vídeos** | Nacional · Internacional *(a confirmar — Miguel pediu pra não fazer tudo de uma vez)* |
| **Regional** | N/S/NE/SE/CO ▸ Estados (já existe; estrutura pronta) |

### 9.3 Descoberta SEO crítica (13/08, da tentativa de limpeza de tags)
- **Tags `count=0` NÃO são SEO-neutras** como se supunha: no domínio público servem página **200** com `<meta name='robots' content='index, follow'>` → **indexáveis** pelo Google. (A **validação de segurança** da automação pegou isso e **abortou antes de apagar** — **0 tags apagadas**, backup intacto.)
- **MAS** não estão no sitemap (Yoast só lista tags com posts) → provável impacto real baixo.
- **Implicação:** a limpeza de tags precisa de **estratégia** (noindex primeiro OU redirect fallback OU checagem no Search Console), **não apagar direto**. E **categoricamente**, `count=0` não autoriza apagar — pode ser categoria-âncora de menu.

### 9.4 Estado
- ⏸️ **Faxina de tags/categorias PAUSADA** até a reforma do menu do Miguel terminar.
- 📋 Estas notas registradas; a política será **finalizada/refinada com base no menu final** do Miguel.
- ✅ Backup das tabelas de termos intacto: `/root/backup_taxonomia_20260813_1400.sql`.
- ✅ **Categoria Distrito Federal (21139)** já criada (atende o submenu Regional▸Centro-Oeste▸DF).
