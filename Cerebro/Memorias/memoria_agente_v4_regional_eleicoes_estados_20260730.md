# 🧠 Memória — Agente V4 Regional: Eleições 2026 em todos os estados (Cafezinho)

**Tema:** Nascimento do projeto "Agente V4 Regional" (política+economia das 27 UFs, Eleições 2026, pesquisas, editoria por estado)
**Fórum pareado (Regra do Tema Duplo):** `Cerebro/Foruns/forum_agente_v4_regional_eleicoes_estados_20260730.md`
**Autor do log:** Z (ZCode) · **Data:** 2026-07-30 16:36 BRT
**Status:** Fase de projeto. Nenhum arquivo de produção tocado. Nenhum deploy. Nenhum AUTH.

---

## 1. Pedido do Miguel (transcrição fiel, sessão ZCode 30/07/2026)

Miguel propôs: agente **V4 Regional** — primeiro desenho/ideia + criar o fórum. Usar **todo o padrão V4** (banco de coletas, auditoria etc.). Matéria sobre **todos os estados e, no futuro, todas as cidades** brasileiras (grandes cidades com zonas, ex. Zona Norte, e bairros famosos). Motivação imediata: **eleições 2026** — acompanhar votação e pesquisas. Cobrir governador, senador e legislativo de todos os estados. Cota **flexível e inteligente**, não rígida ("as pesquisas são muito irregulares"; "alguns estados têm mais"; "aos poucos a gente vá preenchendo todos os estados, vão ter matéria, vão estar indexados, vão estar na editoria"). Foco **política e economia**. Escopo: **só o Cafezinho** ("Eu sei que a gente tem o site temático lá, Ceará, Rio Carta, mas agora eu quero focar só no Cafezinho").

**Deslize de ditado detectado:** Miguel listou 4 zonas (Norte, Centro-Oeste, Sudeste, Sul) e omitiu o **Nordeste**. Desenho feito com as **5 regiões oficiais** e flag explícita no fórum (§2) para confirmação — Brasil = 26 estados + DF = 27 editorias.

## 2. Consulta ao Cérebro (ritual Regra Nº1 — nesta ordem)

| Etapa | Arquivo | Achados usados no desenho |
|-------|---------|---------------------------|
| 1 | `00_CEREBRO_CANONICO.md` | confirmação de caminho; regras de escrita; Tema Duplo |
| 2 | `CEREBRO_INDEX_MASTER.md` | mapa de nodos; apontadores V4/sprints |
| 3 | `memorias_provisorias/INDICE_DESPERTAR_LEVE.md` | Z = coleta estatística + redação + WP **draft sempre** |
| 4 | `CEREBRO_NODE_BOLETIM_NEWS_CAFEZINHO.md` | cascatas LLM canônicas (produção sem busca OK; revisão/auditoria/fact-check exigem websearch real — regra 11/06); legado `agente_eleicoes*.py` existe no Tencent |
| 4 | `Foruns/inbox_trindade/documento_especificacoes_refatoracao_v4.md` | **padrão V4.1**: 2 bancos JSONL/SQLite (bruto + auditadas), dedup fuzzy ≥80%, auditoria (sem jargão IA, aspas simples, fact-check temporal), GitOps + indexing |
| 4 | `root/v4_vertical_intake.py` + `root/v4_vertical_draft_worker.py` (leitura do código) | verticais vivas: `nacional` (cat 22, frescor 24h), `geopolitica` (cat 5003, 72h), `ciencia` (cats 19936/735/30/5008, 7 dias); bancos em `/root/agent_data/v4_verticals/*.sqlite3`; `no_home_score_policy`; máx. 1 draft/h/vertical |
| 4 | `Foruns/forum_kimi_5_patterns_recorrentes_diretrizes_v4_20260728.md` | bugs V4 quentes que o Regional herda como gates: FONTE_EM_GRITO, MINUSCULA_POS_VIRGULA, **CUTOFF_LLM_AUTORIDADE** (governadores/partidos 2026 — crítico p/ eleição), AGENTE_V4_NAO_POPULA_META_ZIZI (`_agente_origem`+`zizi_job_id` obrigatórios), PARTIDO_POLITICO_TROCADO (`figuras_publicas_partido_2026.json`) |
| 4 | `CEREBRO_NODE_SPRINTS_ATIVOS.md` | estado V4 (~43 posts/dia via ciclo Claude Opus), OURO PRECISION (economia Gemini/Qwen-first, tombstone, budget diário), reforma visual, AUTHs |
| 4 | `memorias_provisorias/despertar_leve_z.md` | identidade Z; protocolo WP draft; casa do ZCode |

**Não consultado (sem necessidade agora):** Cofre de Chaves (fase de projeto não toca credenciais), Bugs Ativos (nenhum bug reportado), Telemetria (só referência de custo).

## 3. Decisões de desenho (e justificativa)

1. **5 verticais regionais** (norte/nordeste/centro-oeste/sudeste/sul), 1 banco SQLite por região + campo `uf` — replica o padrão das 3 verticais V4 sem explodir em 27 bancos.
2. **27 editorias WP** (categoria por UF), filhas de 5 categorias regionais, sob mãe `Eleições 2026`; tags de cargo/tipo.
3. **Cota flexível = motor de prioridade com score** (pesquisa nova pesa 4.0 > notícia quente 3.0 > evento 2.0 > justiça log(dias) 1.5 > peso eleitoral 1.0, com rampa até 04/10). **Piso de dignidade: 1 matéria/UF/semana**, preenchido por evergreen quando não há notícia. Atende literalmente ao "flexível, inteligente, aos poucos" do Miguel.
4. **Tracker de pesquisas em banco próprio** (`pesquisas_eleitorais_2026.sqlite3`) com registro TSE obrigatório na matéria (licença legal + antídoto desinformação; memória do caso TSE BR-05864/2026 do checkup Lote 1).
5. **Evergreen "história dos estados"** como camada de preenchimento — pedido explícito do Miguel ("vamos fazer a história de todos os estados") e solução elegante para UF pequena sem notícia.
6. **Cidades/zonas/bairros = Fase 7** (pós-eleição), com hierarquia UF→Capital→Zona→Bairro já prevista na taxonomia para não nascer torta.
7. **Fronteira Nacional × Regional:** pauta de impacto nacional fica na vertical `nacional`; regional só com recorte estadual + dedup cruzado (evita o bug histórico de duplicatas entre pipelines).
8. **Legado `agente_eleicoes*.py` (Tencent):** inventário read-only antes da Fase 2; reaproveitar fontes; aposentar sem sobrepor crons (lição do CHECKUP-001/inventário 02/06).
9. **Conformidade V4 integral** (§3.2 do fórum): cascata canônica, fact-gate com websearch, §86 imagem, §17 cost guard, §82.3 backup/rollback, metas zizi, **draft sempre** — publicação segue no ciclo editorial humano/Claude.

## 4. Calendário eleitoral usado no plano

- 30/07/2026 (hoje) → registro de candidaturas até **15/08** → propaganda meados de agosto → **1º turno 04/10** (66 dias) → **2º turno 25/10**.
- Por UF em 2026: governador+vice, **2 senadores**, deputados federais e estaduais/distritais.
- Janela ideal: Fase 5 (27 UFs no ar) mirando **meados de agosto**, quando o registro oficial dispara a cobertura e as pesquisas estaduais.

## 5. Escritas nesta sessão (Camada 3 + catálogos)

1. `Cerebro/Foruns/forum_agente_v4_regional_eleicoes_estados_20260730.md` — fórum (plano completo §1–§14)
2. `Cerebro/MEMORIA/memoria_agente_v4_regional_eleicoes_estados_20260730.md` — esta memória
3. Catálogo Camada 2: `Foruns/INDICE_FORUNS_SEMANAL.md` (nova seção) + `CEREBRO_NODE_SPRINTS_ATIVOS.md` (sprint aberto, fase projeto)
4. Linha do tempo: `CEREBRO_NODE_ATUALIZACOES.md`

**Nada mais foi escrito. Nada em produção. Nenhum segredo exposto (só caminhos).**

## 6. Pendências abertas (bloqueiam Fase 1)

- OK do Miguel ao desenho geral e à correção 5 regiões (fórum §13, itens 1–6)
- Definição de divisão de trabalho §13 (proposta: Z coda intake+worker, Claude revisa, Codex valida deploy)
- AUTH formal antes de qualquer coisa no Tencent

## 7. Aprendizados para futuras sessões

- O padrão V4 vivo hoje é **SQLite por vertical** (`/root/agent_data/v4_verticals/`), não só JSONL (o doc V4.1 original falava JSONL — o código atual usa sqlite3; seguir o código, não o doc antigo).
- Todo worker novo **precisa** popular `zizi_job_id` + `_agente_origem` (bug §2.4 de 28/07) — incluído no checklist desde o nascimento.
- Gates de autoridade/partido 2026 são **ainda mais críticos** para cobertura eleitoral estadual (27 governadores + centenas de candidatos) — `figuras_publicas_partido_2026.json` deve ganhar seção por UF na Fase 1.

*Ass: Z (ZCode) — 2026-07-30 16:36 BRT.*

---

## 8. PARTE 2 — Mapa histórico (sessão continuação, 30/07 ~18:30 BRT)

**Pedido do Miguel (transcrição):** olhar se o site tem categorias de todos os estados/regiões; se não tiver, criar; pesquisar matérias já publicadas relacionadas a cada estado ("Tem muito do Rio, muito do Ceará. Deve ter muito de Minas, muito de São Paulo"); pesquisa profunda desde o início do site; "faz um mapa"; plano de trabalho; "se não fica muito pesado, já colocando a categoria certa".

### Execução (100% READ-ONLY no site)

1. **Leitura** `CEREBRO_NODE_PUBLICACAO_WP_CAFEZINHO.md` → endpoint `controle.ocafezinho.com`, auth Basic via cofre `.env.unificado` (teste `/users/me` = 200; nenhum segredo exposto).
2. **Inventário:** 274 categorias baixadas (`cache/categorias.json`). Achados: 8/27 UFs têm categoria (CE 4968/268 posts · SP 4988/295 + SP capital 5001/222 · RJ 1656/454 + RJ capital 5002/178 + Baixada/Niterói/Friburgo · Brasília 5710/102 · RS 5004/28 · BA 4994/23 · MG 2549/20 · PB 5101/5); 19 faltam. Regiões: só Nordeste (4984). Eleições 2026 (5088) existe com 1.098 posts, sem filhas.
3. **Varredura v1 abortada:** busca server-side de termos ambíguos explodia ("Acre" ⊂ "acreditar"; busca WP é AND de substrings, sem frase exata). Lição registrada.
4. **Varredura v2 (executada, ~40 min):** (a) dump completo de títulos — 771 páginas, 77.133 posts (`cache/titulos_p*.json`); (b) regex estrito por UF nos títulos (lookarounds PT-BR, case-sensitive p/ ambíguos) → 3.793 posts iniciais; (c) busca de ~52 termos distintivos de 1 palavra (demônios, estados de nome único, governadores 1-palavra); (d) passo suplementar: mato-grossense (48 novos), sul-mato-grossense (22), acreano (7), candango (8) — rondoniano 0.
5. **QA por amostragem** de termos de risco: demônios com precisão alta; confirmado que tier B contém roundups nacionais (covid, "27 governadores", Inmet) → fora do backfill automático; falsos positivos nomeados: "Carlo Caiado" (RJ) ≠ Ronaldo Caiado; "Vitória" (eleitoral ≠ cidade); "Natal" (feriado ≠ cidade); "Ratinho" (SBT ≠ governador).
6. **Consolidação:** 24.807 posts mapeados (`cache/posts_por_uf.jsonl`) → 3.901 tier A / 20.906 tier B → backfill AUTO **3.333** + REVISAR **254** (`cache/backfill_plano.json`). Por ano (tier A): pico **2026 (723)**, depois 2024 (518), 2023 (513), 2022 (510).

### Números-chave

| Métrica | Valor |
|---|---|
| Posts do site (publish) | 77.133 |
| Posts regionais detectados | 24.807 (3.901 tier A) |
| Tier A sem categoria de estado | 3.587 → AUTO 3.333 + REVISAR 254 |
| UFs sem categoria | 19 de 27 |
| Regiões faltantes | 4 de 5 |
| Maiores "sem casa" | PE 1.588 · GO 1.338 · AM 1.165 · MA 1.153 · PR 676 · ES 336 |

### Artefatos

- `Cerebro/Foruns/mapa_regional_historico_20260730.md` — o MAPA (§1–§7) com plano de retroativo em 4 lotes
- `ZCodeProject/regional_v4/` — scripts + caches (varredura resumível)
- Fórum do projeto atualizado (§15)

### Pendências desta etapa

- **"Vai" do Miguel** para Lote 0 (criar 23 categorias) + Lote 1 (auto-aplicar 3.333) — `executar_backfill.py` a escrever (~150 linhas, log `backfill_log.jsonl`, rollback reverso, ~2 req/s).
- Lote 2 (revisar 254) — triagem assistida.
- Lote 3 (tier B 20.906) — sprint futura com filtro anti-roundup + triagem LLM leve.
- Decisão editorial separada: recategorização eleitoral histórica (2014/2018/2022) — não tocar no retroativo.

*Ass: Z (ZCode) — 2026-07-30 ~18:30 BRT.*

---

## 9. PARTE 3 — Decisão Miguel: categorização gradual + consulta à Trindade (31/07 23:58 BRT)

**Sequência de fatos:** Miguel disse "vai" e, na mesma fala, condicionou: categorias para depois; categorização **programada aos poucos**; antes, **cartinha à Trindade pedindo opinião**; "lembra protocolos de comunicação; limpa inbox, canal, abre forum e faz cartinha aqui".

### Protocolos de comunicação relembrados (fonte)

- Canal vivo: `Projeto Cafezinho Agentes/Foruns/canal_trindade.md` — formato `### emoji [TAG] dd/mm hh:mm BRT — título` + corpo `**De → Para (c/c Miguel)**` + assinatura.
- Cartinhas: `Cerebro/Foruns/cartinhas/cartinha_<tema>_<yyyymmdd>_<hhmm>.md` (ex.: `cartinha_zcode_claude_baleia_custos_vigilancia_20260730.md`).
- Inboxes: `Cerebro/Foruns/inbox_trindade/<agente>.md` — regra `feedback_limpeza_diaria_inbox` (reset diário por Claude Code, backup em `Cerebro/Backups/inbox_<data>/`).
- Ponte: `Cerebro/ponte_kimi/CONTRATO_PONTE_CLAUDE_KIMI.md` (§5 bilateral, §6 triangular).

### Limpeza de inbox/canal (processamento)

- **Inbox (kimi.md):** 2 pings do Claude (31/07 11:22 + 12:30) apontando `cartinha_kimi_pending_delegados_20260731_1120.md` — 3 posts para decidir (263649 duplicata+erro factual → trash; 263072 janela fechada → trash; 263165 FDA desatualizado → atualizar) + **8 posts §86 sem featured_media** (263498, 263635, 263571, 263638, 263653, 263574, 263634, 263654) revertidos a `pending` por Claude, aguardando pipeline de imagem + publish.
- **Ação:** ACK postado no canal `[KIMI-PENDING-3-DELEGADOS-ACK]` com decisões (2 trash, 1 atualizar, 8 assumidos p/ pipeline de imagem). **Execução fica na fila** — Miguel decide se rodo de madrugada ou em dia.
- **Canal:** lido o tail (~15 mensagens, 29/07) — contexto: rollback cascata roteador (regra: produção só com autorização explícita por item), telemetria restaurada, gpt-5.5 luxo com web_search.

### Consulta à Trindade (entrega principal)

- **Cartinha:** `Cerebro/Foruns/cartinhas/cartinha_trindade_v4_regional_mapa_categorizacao_gradual_20260731_2358.md` — resumo do mapa + decisão do gradual + **6 perguntas** (taxonomia; onde pendurar; ritmo 150–300/dia UFs-sem-casa-primeiro; tier B; revisores Z/Claude/Codex; efeito no ciclo editorial). Prazo respostas 48h.
- **Ping canal:** `[Z-V4-REGIONAL-MAPA-CATEGORIZACAO-GRADUAL]` 31/07 23:58 BRT.
- **Fórum:** §16 adicionado (decisão + consulta + ajuste dos lotes p/ tranches diárias).

### Estado ao fim da sessão

- Backfill **suspenso** (nenhuma categoria criada, nenhum post alterado) — aguarda opiniões Trindade + OK final Miguel.
- Dívida assumida: 8 posts §86 (imagem+publish) + 3 decisões (2 trash + 1 atualizar) — na fila, aguardando janela definida por Miguel.
- Próximo passo natural: consolidar respostas da Trindade (até 02/08) → plano final de categorização gradual → OK Miguel → L0.

*Ass: Z (ZCode) — 2026-07-31 23:58 BRT.*

---

## 10. PARTE 4 — Execução L0 + Tranche 1 (01/08 00:20–00:35 BRT)

**Gatilho:** Miguel — "carta respondida. continua" (01/08).

### Pareceres consolidados

- **AGY (00:10):** 6/6 aprovado (recomenda UFs livres no topo).
- **Grok (00:12):** aprovado com 2 travas + ordem: (a) **pré-L0 checar permalink** — se hierárquico, reparent quebra URLs; (b) **`post_modified` bumpa** no POST de categories — filtrar na vigília. Ordem: PR→PE→ES→AM→GO→PA→RN→MA→SC→AL→PI→SE→AC→RO→MT→MS→AP→TO→RR, depois as 8 com casa. Canário 150–200/dia (2 dias) → 300/dia. Correção ao §4: UFs fora da 5088.

### Decisão técnica: modelo FLAT

Checagem ao vivo: `/categoria/rio-de-janeiro/rio-de-janeiro-capital/` = 200; `/categoria/rio-de-janeiro-capital/` (flat) = 404 → **permalinks hierárquicos**. Reparent das 8 UFs quebraria URLs indexadas. Adotado o fallback seguro do Grok: **UFs e regiões como irmãs no topo; posts recebem UF + região**; zero URL alterada. Hierarquia real com 301s fica para decisão futura.

### Execução

1. **`executar_backfill.py`** escrito (dry-run, log jsonl, rollback, idempotente, rate ~2 req/s, pausa 5s/50).
2. **L0 (00:20):** dry-run limpo (0 colisões) → **23 categorias criadas**: Norte 21068, Centro-Oeste 21069, Sudeste 21070, Sul 21071 + AC 21072, AL 21073, AP 21074, AM 21075, ES 21076, GO 21077, MA 21078, MT 21079, MS 21080, PA 21081 (`para-estado`), PR 21082, PE 21083, PI 21084, RN 21085, RO 21086, RR 21087, SC 21088, SE 21089, TO 21090. **27/27 editorias existem.**
3. **Tranche 1 (00:27):** dry-run 200/200 → execução **200/200 PR + Sul, 0 erros**. Amostra verificada ao vivo: post 27989 [22,36]→[22,36,21071,21082], `date` 2015 intacta, `modified` bumpado (trava Grok confirmada). Editoria pública https://www.ocafezinho.com/parana/ = 200.
4. **Vigília:** aviso no canal + `tranche1_ids_vigilia.json` (200 IDs) para filtro do `post_modified`.
5. **Relatórios:** canal `[Z-V4-REGIONAL-MAPA-CATEGORIZACAO-GRADUAL]` 00:30; fórum §17.

### Artefatos novos

- `ZCodeProject/regional_v4/executar_backfill.py` · `cache/categorias_criadas.json` · `cache/backfill_log_20260801_002713.jsonl` · `cache/tranche1_ids_vigilia.json`

### Fila restante

- Tranches diárias (~3.133 AUTO restantes + 254 REVISAR) na ordem Grok.
- Pareceres tardios da Trindade (janela até 02/08) — consolidar no §16.

### 10.1 Delegação Claude — fechamento (01/08 ~00:45 BRT)

- **263649 + 263072 → trash** (DELETE executado; verificado status=trash).
- **263165:** resolvido pelo loop (publish, números novos, "Ars Technica", imagem).
- **8 posts §86:** ao chegar, 6 já tinham imagem e estavam sendo processados pelo loop do Claude (modified em minutos — **não toquei, anti-colisão**); 263634 ganhou imagem durante minha execução (pulo idempotente); **263638 (SCMP) og:image 404** → fail-closed pending, handoff ao Claude no canal `[KIMI-PENDING-3-DELEGADOS-FECHADO]`.
- **Lição anti-colisão:** checar `modified` recente antes de agir em posts de fila compartilhada; loop do Claude trabalha os mesmos drafts em tempo real.

*Ass: Z (ZCode) — 2026-08-01 00:35 BRT.*

---

## 11. PARTE 5 — Construção do pipeline (Fases 1–3) + shadow (01/08 ~04:30 BRT)

**Autorização:** "pode, só deixa sem cron. deixa para ligar o cron por último" (Miguel).

### Arquitetura final (decisões)

- **Intake standalone** (não depende de estoque upstream como o das verticais): RSS direto por UF → trafilatura p/ texto completo (worker exige ≥500 chars) → banco da região. Frescor 48h fail-closed; dedup sha256 URL canônica; veto `negative_lula_poll` (linha editorial idêntica à nacional); rejeições e runs logados.
- **UF assignment 2 vias:** marca-texto explícita (nome/capital/demônio/governador, regex com bordas) OU proveniência da fonte local + **gate de nexus política/economia** (`off_desk_sem_nexus...`) + bloqueio `national_desk_no_state_nexus`.
- **Poll flag 2-tier** (fix do smoke): instituto nominal (Datafolha/Quaest/Ipec/AtlasIntel/Paraná Pesquisas/Real Time/PoderData/Ipespe/Futura/Genial-Quaest/Veritá) OU (pesquisa/levantamento/intenção de voto + objeto eleitoral). Antes: "Atlas"/"Ideia" soltos → FP turismo.
- **Worker = wrapper zero-fork** (`importlib` no `v4_vertical_draft_worker.py` de 30/07 18:18 — cópia local é a mais nova, guarda §86 inclusa): injeta 27 CONFIGs (`regional_<uf>`: db da região, cats [UF, Região], section "regional", freshness 48), monkeypatch `select_candidate` com filtro `uf=?`, `--auto` lê `fila_prioridade.json`. Na produção, `WORKER_PADRAO` resolve `/root/...` automaticamente; quotas 55min por UF via `draft_events` nativo; zizi_job `v4d_regional_<uf>_…`.
- **Motor:** justiça = log10(dias_desde_último_post+1) via WP (cache 6h); peso eleitoral ~eleitorado 2024 normalizado; rampa 1.0→1.5 até 04/10.

### Números do shadow (01/08)

- 14.335 itens vistos → 880 candidatos vivos (≤48h) · 21 polls · 27/27 UFs com estoque
- Rejeições: maioria `source_too_old` (G1 serve 100 itens/feed, maioria >48h — esperado)
- Feeds: G1 27/27 (slug AC corrigido de `ac/cre`→`ac/acre`); majors locais 10/27 (404/403 pendentes)
- Fila do motor: MG → PE → GO → AC → RS → PR → CE — prova da justiça distributiva
- Testes wrapper: `--uf CE` ✅ (43 candidatos), `--auto` ✅ (motor escolheu MG, 33 candidatos)

### Arquivos novos (ZCodeProject/regional_v4/)

`v4_regional_intake.py` · `motor_prioridade_regional.py` · `v4_regional_draft_worker.py` · `regional_fontes_2026.json` · `schema_pesquisas_eleitorais_2026.sql` · `bancos/*.sqlite3` (5 + tracker) · `cache/fila_prioridade.json`

### Pendências (gates com AUTH)

1. Deploy dos 4 arquivos + fontes no servidor (`/root/`, bancos em `/root/agent_data/v4_verticals/`)
2. Canário real: `v4_regional_draft_worker.py --auto` supervisionado (worker chama `/root/venv/bin/python3 /root/agente_controlado.py` — por isso só no servidor)
3. Majors locais 404/403 (paths RSS reais) — G1 cobre enquanto isso
4. Tracker v2: parse de instituto/cenários do título + registro TSE
5. **CRON POR ÚLTIMO (ordem explícita do Miguel)**

---

## 12. PARTE 6 — Deploy + 1º canário em produção (06/08 ~15:22 UTC)

- **Deploy:** 5 arquivos para NYC `/root/`; paths híbridos adicionados (intake/motor: `/root/agent_data/v4_verticals` quando existe; motor lê `/root/chaves.sh` no servidor). Dependências confirmadas no NYC: trafilatura 2.0.0, PIL, venv.
- **Intake servidor:** 16 min, 913 candidatos, 27/27 UFs (feeds iguais ao shadow local: G1 27/27, majors 10/27).
- **Motor servidor:** MG 12,402 (2 polls) > SP > RJ > BA — fila `cache/fila_prioridade.json` no servidor.
- **Canário `--auto`:** escolheu MG; draft 264528 criado 15:09 UTC (`draft_confirmed`); `research_empty` (http_403 no research complementar); `factgate_skipped` (sem_evidencia — research falhou); imagem IA (Aécio fora do banco — generator não-banco, fallback correto); meta zizi ok; `_agente_origem` vazia (dívida anotada).
- **Editorial loop (Claude V5):** revisou e publicou 13 min depois (12:22 BRT). Post no ar com cats [2549 MG, 21070 Sudeste], topo da editoria MG.
- **Veredito:** pipeline V4 Regional VALIDADO EM PRODUÇÃO — primeiro artigo publicado: "Aécio Neves encerra 4 décadas de mandatos e não disputará eleições" (maior notícia política de MG da semana, escolhida pelo motor).
- **Cron segue OFF (ordem Miguel).**

---

## 13. PARTE 7 — Cron ligado + bugs de concorrência (06/08)

- **"liga" (Miguel):** `/etc/cron.d/v4_regional` — intake :07/h + worker 6×/dia BRT (wrapper `v4_regional_rodar_worker.sh`).
- **Bug 1 — colisão redator singleton:** `ABORTADO: outro processo já está rodando` (agente_controlado é 1-por-vez global). Fix: wrapper com retry (ABORTADO fresco no agent log → retry 7min).
- **Bug 2 — database is locked:** intake commitava 1× por REGIÃO (transação de minutos). Fixes: lock compartilhado worker↔intake (`flock -w 900`) + intake commit a cada 40 itens (redeployado).
- **Rodadas de validação:** duplicate_aborted (Cleitinho já coberto por outra vertical — gate correto) → depois draft_confirmed 264544 (SP/CPTM) com cats corretas + no_home.
- **Aprendizado:** qualquer vertical nova divide o redator com as demais — collision handling é obrigatório no wrapper; e intake novo deve commitar em lote desde o nascimento.
- **Cron de exemplo (UTC):** intake `7 * * * *` · worker `5 10,13,16,19,22,1 * * *` (= 7/10/13/16/19/22:05 BRT).
