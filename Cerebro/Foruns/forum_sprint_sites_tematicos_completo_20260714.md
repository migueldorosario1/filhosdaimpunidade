# 🎨 Fórum — Sprint Completo dos Sites Temáticos (infra + editorial V4)

**Data de abertura:** 2026-07-14 (fim de tarde BRT)
**Autor:** Claude Code (agente), a pedido de Miguel
**Status:** aberto — execução programada pro fim de semana 19-20/jul
**Prioridade:** alta (Miguel quer executar essa sprint completa)
**Duração estimada:** fim de semana pro bloco A, próximas 2-4 semanas pro bloco B

---

## 1. Motivação

Miguel decidiu fazer uma **reforma completa dos sites temáticos** — não é só infraestrutura de indexação. É trabalho duplo:

- **Bloco A (infra):** finalizar separação de service accounts do Google Indexing API (7 sites + Cafezinho canônico isolados por SA própria — código pronto na sessão 14/jul, falta parte manual no GSC)
- **Bloco B (editorial):** reformar os AGENTES de cada site temático, incorporando as inovações do **sistema V4** (auditor, consenso 3/3, fact-check em cascata, dry-run, invariantes hard-coded, etc) que a Trindade (Codex + Fable + Claude) construiu para o Cafezinho canônico

Contexto por trás: Cafezinho canônico está em recovery pós-punição algorítmica com publicação humana + agentes reformados. Sites temáticos ficaram parados enquanto Cafezinho passa por essa transição. Miguel quer **ativar os temáticos com a mesma qualidade editorial** que Cafezinho está buscando — não repetir o erro dos agentes automatizados sem freio.

---

## 2. Sites em escopo (7 no total)

| Site | Domínio | Stack | Agentes atuais | GSC verificado |
|---|---|---|---|---|
| Global South News (EN) | globalsouth.news | WordPress | agente_curadoria_gsn (traduz do Cafezinho) | Sim (sc-domain) |
| Global South News BR | globalsouthnews.com.br | ? | ? | Sim |
| Rio Carta | riocarta.com | WordPress | agentes silo próprio `Rio Carta Agentes/rio_carta` | ⚠️ verificar |
| Mundo dos Trilhos | mundotrilhos.com | WordPress | agente_ferroviario_v2 (cross-post) | ⚠️ verificar |
| Discover Brazil | discoverbrazil.news | WordPress | (poucos posts, semi-parado) | ⚠️ verificar |
| Mapa Rio | mapario.com.br | WordPress | (dormente) | ⚠️ verificar |
| AIatolah | aiatolah.com | **Astro/GitHub/Vercel** (não WP) | agentes Python `aiatolah/agentes/` | ⚠️ verificar |
| ceara.digital ("Cicero") | ceara.digital | ? | agentes silo `Cicero Agentes/` | ⚠️ verificar |

**Fica claro:** heterogeneidade grande. Nem todos são WordPress. Nem todos têm mesmo tipo de agente. **A reforma não vai ser copy-paste** — cada site precisa de análise própria.

---

## 3. Bloco A — Infraestrutura de indexação (fim de semana 19-20/jul)

**Depende deste fórum companion:** [`forum_separacao_service_accounts_indexing_20260714.md`](forum_separacao_service_accounts_indexing_20260714.md) que tem detalhes técnicos completos.

### Estado hoje (14/jul) — o que já foi feito

- ✅ 7 projetos GCP criados: `indexing-gsn`, `indexing-riocarta`, `indexing-mundotrilhos`, `indexing-discoverbrazil`, `indexing-mapario`, `indexing-aiatolah`, `indexing-ceara`
- ✅ 7 service accounts criadas (`indexer@indexing-<site>.iam.gserviceaccount.com`)
- ✅ 7 keys JSON geradas e transferidas pro NYC em `/root/agent_data/indexing_keys/`
- ✅ Código refatorado: `util_indexing.py` com dict `INDEXING_SITES` mapeando domínio → keyfile, `indexador_google.py` com param `keyfile`. Backward compat 100% (12+ agentes editoriais continuam funcionando sem mudança)
- ✅ Smoke test da resolução de keyfile: 7 sites passam, denylist (cafezinho.news, controle.ocafezinho) bloqueia
- ✅ Cafezinho canônico continua indexando normal (ping real testado, 54/200 hoje)

### O que falta pro fim de semana (Miguel faz + Claude valida)

**Tarefa 1 — Adicionar Owner das SAs no GSC (Miguel, manual, ~30 min)**

Pra cada site abaixo, entrar no Search Console → Configurações → Usuários e permissões → Adicionar usuário → colar email da SA → permissão **Owner (Proprietário)** → salvar.

| Site | Email SA (copy-paste) | Link direto GSC |
|---|---|---|
| GSN | `indexer@indexing-gsn.iam.gserviceaccount.com` | https://search.google.com/search-console?resource_id=sc-domain%3Aglobalsouth.news |
| Rio Carta | `indexer@indexing-riocarta.iam.gserviceaccount.com` | https://search.google.com/search-console?resource_id=https%3A%2F%2Fwww.riocarta.com%2F |
| Mundo Trilhos | `indexer@indexing-mundotrilhos.iam.gserviceaccount.com` | https://search.google.com/search-console?resource_id=https%3A%2F%2Fmundotrilhos.com%2F |
| Discover Brazil | `indexer@indexing-discoverbrazil.iam.gserviceaccount.com` | https://search.google.com/search-console?resource_id=sc-domain%3Adiscoverbrazil.news |
| Mapa Rio | `indexer@indexing-mapario.iam.gserviceaccount.com` | https://search.google.com/search-console?resource_id=http%3A%2F%2Fmapario.com.br%2F |
| AIatolah | `indexer@indexing-aiatolah.iam.gserviceaccount.com` | (adicionar propriedade `https://aiatolah.com/` primeiro se não existe) |
| ceara.digital | `indexer@indexing-ceara.iam.gserviceaccount.com` | (adicionar propriedade `https://ceara.digital/` primeiro se não existe) |

**Tarefa 2 — Remover Owner da SA velha do Rio Carta e GSN (Miguel, manual, ~5 min)**

A SA velha `indexing-cafezinho@gen-lang-client-0200069757.iam.gserviceaccount.com` ainda é Owner de Rio Carta E GSN (herança histórica). Depois que as SAs novas estiverem como Owner nesses dois sites, remover a velha. Fica: Cafezinho canônico exclusivo dessa SA.

**Tarefa 3 — Smoke test por site (Claude executa após ownership pronto, ~15 min)**

Pra cada site que Miguel confirmar "Owner adicionado", Claude roda:

```python
r = util_indexing.notificar_e_logar_v2("https://<domínio>/qualquer-url-real/", agent_name="smoke_temativos")
assert r["status"] == "ok" and r["ping_count"] > 0
```

Se retornar OK, isolamento por SA está funcionando. Se retornar `skip_dominio` ou `erro`, alguma coisa está errada — investigar.

**Tarefa 4 — Deletar projetos GCP obsoletos (opcional, ~5 min)**

- `open-claw-gsn` (esqueleto abortado, sem API habilitada — nunca foi usado, agora tem `indexing-gsn` no lugar)
- `ZOMBIE - Cafezinho`, `ZOMBIE - Cafezinho novo`, `ZOMBIE - Cafezinho novo2` (só se Miguel quiser liberar quota — deleção é reversível por 30 dias)

---

## 4. Bloco B — Reforma editorial dos agentes temáticos (semanas 22/jul - 15/ago)

Aqui é o trabalho maior e mais complexo. **Não vai ser executado no fim de semana** — é sprint separada de 2-4 semanas.

### Inventário dos agentes temáticos atuais (pra reformar)

Do NYC (`/root/`) — agentes com ligação a temáticos:

| Agente | Site alvo | Estado atual | Precisa V4? |
|---|---|---|---|
| `agente_curadoria_gsn.py` | GSN | Traduz top do Cafezinho pra EN | ✅ Sim |
| `agente_turismo_embratur.py` | GSN (turismo) | Ativo, cross-post BR+EN | ✅ Sim |
| Silo `Rio Carta Agentes/rio_carta/` | Rio Carta | Autonomo, subCérebro próprio | ✅ Sim |
| `agente_ferroviario_v2.py` | Mundo Trilhos | Cross-post cafezinho + mundotrilhos | ✅ Sim |
| `aiatolah/agentes/aiatolah_agente_coletor_ia.py` | AIatolah | Pipeline próprio Astro/GitHub | ✅ Sim (adaptar V4 pra stack não-WP) |
| Silo `Cicero Agentes/` | ceara.digital | Autonomo | ✅ Sim |
| Sem agente | Discover Brazil | Semi-parado | 🆕 Criar agente novo com V4 |
| Sem agente | Mapa Rio | Dormente | 🆕 Criar agente novo com V4 |

### O que é V4 e por que incorporar

V4 é o **sistema editorial de nova geração** que a Trindade (Codex + Fable + Claude) construiu para o Cafezinho canônico ao longo de 2026. Está em Fase 7 de auditoria multi-item (fórum ativo: `forum_v4_fase6_multicase_dryrun_20260710.md`).

**Inovações-chave do V4 que valem incorporar em cada agente temático:**

1. **Auditor pré-publicação (consenso 3/3)**: antes de publicar, 3 juízes independentes (GPT + Claude + outro) avaliam o rascunho. Se algum reprovar, não publica.
2. **6 invariantes hard-coded** (validações estruturais impossíveis de burlar): título sem sigla técnica, foto obrigatória validada, fact-check obrigatório, ausência de meta-discurso de LLM (evitar "Não posso publicar este conteúdo"), atribuição obrigatória, formato editorial padrão.
3. **Dry-run antes de promoção**: pipeline testa em ambiente sombra (`v4_real_*` cases) antes de sair pra WordPress real. Previne desastres tipo "publiquei alucinação".
4. **Fact-check em cascata**: DeepSeek/Gemini → Perplexity sonar-reasoning-pro → Claude fallback (Regra §6 da hierarquia CLAUDE.md).
5. **Tribunal Visual** (`tribunal_visual.py`): valida foto/legenda antes do upload com Gemini 2.5 Flash. Cross-check título↔legenda.
6. **Autocura V4** (`agente_autocura_v4.py`): monitora publicação recente, rebaixa a rascunho quem passar direto por bug.
7. **Preparador → Publicador → Auditor** (separação de responsabilidades): mata bug de contrato entre blocos (lição B-049 22/06).
8. **Detecção de meta-discurso de LLM** (Adendo 7 CLAUDE.md): função `detectar_recusa_llm()` bloqueia publicação de "Rascunho apresenta eventos fictícios e não pode ser publicado" como título.
9. **Regra global de sigla no título** (Adendo 22/06): sem sigla técnica exceto lista fechada (ONU, STF, EUA, etc). Aplicável a TODOS os agentes.

### Trabalho por site (ordem sugerida)

**Fase B.1 — Piloto (Rio Carta, ~1 semana)**
- Rio Carta já tem silo próprio + fóruns próprios + estrutura semi-autônoma
- É o melhor candidato pra piloto porque: (a) tem menos dependência do Cafezinho, (b) já tem investimento editorial, (c) errar aqui não afeta veículo principal
- Aplicar V4 completo (auditor + tribunal visual + fact-check + invariantes)
- Rodar 1 semana em dry-run antes de promover ao WP

**Fase B.2 — GSN (~1 semana)**
- Repete padrão do Rio Carta, adaptando pra EN
- Fact-check em EN (Perplexity sonar suporta multilingue)
- Tribunal Visual em EN (Gemini suporta)
- Cross-post com Cafezinho continua (curadoria GSN)

**Fase B.3 — Mundo Trilhos + Discover Brazil + Mapa Rio (~1 semana)**
- Sites de nicho, volume baixo (~2-5 posts/dia)
- Aplicar V4 simplificado (sem tribunal visual se site é pouco visual)
- Provavelmente criar agentes novos (não tem agente ativo em Discover/Mapa Rio)

**Fase B.4 — AIatolah + ceara.digital (~1 semana)**
- Adaptar V4 pra stack Astro (aiatolah) — não é WordPress, precisa reescrever o publicador
- ceara.digital já tem silo próprio (`Cicero Agentes/`) — auditar arquitetura atual antes

### Métricas de sucesso do Bloco B

Pra cada site reformado, medir após 30 dias:
- **Zero recorrência do bug "publicou alucinação"** (histórico do CLAUDE.md Adendo 7)
- **Zero recorrência do bug "cota Indexing esgotada por spam"** (resolvido pela sep SAs)
- Impressões GSC ≥ baseline pré-reforma
- CTR ≥ 3% (padrão atingido pelo Cafezinho canônico pós-transição)
- Publicação estável ≥ 3 posts/dia (temáticos são menor volume)

---

## 5. Cronograma proposto

| Semana | Dias | Tarefa |
|---|---|---|
| Fim de semana | Sáb 19 - Dom 20/jul | Bloco A completo (infra GSC, ~1h) |
| Semana 30 | 22 - 28/jul | Fase B.1 (Rio Carta piloto V4) |
| Semana 31 | 29/jul - 04/ago | Fase B.2 (GSN V4) |
| Semana 32 | 05 - 11/ago | Fase B.3 (Mundo Trilhos + Discover + Mapa Rio) |
| Semana 33 | 12 - 18/ago | Fase B.4 (AIatolah + ceara.digital) |
| Semana 34 | 19 - 25/ago | Consolidação + métricas + snapshot |

**Duração do Bloco B especificamente** (Bloco A é ~1 hora no fim de semana):
- **Otimista**: 5 semanas (se cada fase respeitar 1 semana e nada bagunçar)
- **Realista com surpresas de código**: 6-8 semanas
- **Pessimista** (se algum site exigir refactor do V4 pra funcionar em stack não-WP): 10+ semanas

Ordem prática: começar Fase B.1 (Rio Carta) só depois do Bloco A ter fechado + as respostas de Miguel em §7 chegarem. Isso pode adicionar 1-2 semanas de espera antes do cronômetro começar.

---

## 6. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Quebrar Cafezinho canônico durante refactor V4 pra temáticos | Trabalhar em branches. Cafezinho canônico continua com V9 estável. V4 nos temáticos primeiro. |
| Duplicação de código (V4 em 7 lugares) | Extrair V4 pra biblioteca comum `/root/lib/v4_editorial.py`, cada agente importa. Não copiar. |
| Ativar indexação de site com conteúdo ruim = piorar reputação da SA nova | Ativar indexação por site SÓ APÓS o agente reformado estiver rodando com V4 completo. Não antes. |
| Sites com stack diferente (AIatolah Astro) | Fase B.4 fica pro final, tempo pra adaptar |
| Agentes automatizados voltando aos vícios antigos (volume>qualidade) | V4 tem 6 invariantes hard-coded que impedem. Se não passar por invariante, não publica. |
| Miguel + Gabriel ainda cuidando do Cafezinho canônico manualmente | Sprint B não sobrepõe carga humana — é 100% técnica |

---

## 7. Perguntas em aberto (Miguel decide)

### 7.1 Qual o volume-alvo por site temático?
- **Opção A**: 2-5 posts/dia (nicho autoral, alta qualidade)
- **Opção B**: 5-10 posts/dia (volume médio, curadoria pesada)
- **Opção C**: por site diferente (Rio Carta 10/dia, Discover 2/dia, etc)

### 7.2 Indexar Google via API é prioridade em quais sites?
- Todos os 7 têm SA pronta. Mas fazer sentido indexar via API só quem tem publicação suficiente.
- **Sugestão**: ativar API só quando o site publica ≥3/dia (não desperdiçar quota)

### 7.3 Cross-post entre sites deve continuar ou reformar também?
- Hoje: Cafezinho → Mundo Trilhos (agente_ferroviario_v2), Cafezinho → GSN (agente_curadoria_gsn)
- Se cada site tem sua identidade autoral V4, cross-post pode virar contradição
- Opções: manter cross-post apenas de matérias explicitamente marcadas, ou eliminar

### 7.4 Miguel + Gabriel também vão publicar humanamente nos temáticos?
- Ou temáticos ficam 100% agentes V4 com curadoria humana só em pauta?

### 7.5 Prioridade de qual site atacar primeiro?
- Piloto sugerido: **Rio Carta** (autonomia, investimento já feito). Miguel confirma ou prefere outro?

### 7.6 Sobre AIatolah especificamente
- Está no GoDaddy (não Enom/Namecheap), stack Astro/Vercel (não WordPress). Reforma V4 exige adaptação grande.
- Fica pra Fase B.4 (final) ou vira sprint separada?

---

## 8. Log de conversa neste fórum

**2026-07-14 — Miguel:** pediu abertura de fórum dedicado sprint sites temáticos, incluindo reforma dos agentes com inovações V4. Execução no fim de semana pra bloco A, semanas seguintes pra bloco B.

**2026-07-14 — Claude Code:** fórum aberto. Aguardando respostas de Miguel em §7 antes de iniciar Bloco B. Bloco A já está scheduling para 19/jul (lembrete registrado em `Cerebro/CEREBRO_NODE_AGENDA_LEMBRETES.md`).

**2026-07-16 01:15 BRT — Claude Code — BLOCO A 100% CONCLUÍDO ✅** (adiantado 3 dias em relação ao 19/jul planejado).

7 sites com service accounts isoladas + smoke tests OK + SA velha limpa dos GSCs de Rio Carta e GSN. Rotina executada ao vivo com Miguel na sessão que começou 15/07 22:00 BRT. Cafezinho canônico agora tem quota Google Indexing 100% exclusiva.

**Descobertas colaterais (registradas pra Bloco B):**
- **GSN** com apenas 5 páginas indexadas de 621 no GSC e zero cliques em 90d — reforça urgência da reforma editorial V4.
- **TODOS os 7 sites temáticos são servidos por Vercel** (GSN, Rio Carta, Mundo Trilhos, Discover Brazil, Mapa Rio, AIatolah, ceara.digital) — confirmado via `server: Vercel` header + IPs Vercel + `x-vercel-id`. Zero WordPress entre eles. Só o Cafezinho canônico continua WP. **Consequência pro Bloco B:** V4 atual usa WP REST API pra publicar — vai precisar ser reescrito por completo pro publicador de todos os 7 sites (git commit + push pra repo Astro/Vercel, ou API do CMS que cada site usa). Não existe piloto "V4 puro sem adaptar" — o piloto (Rio Carta ou GSN) já será piloto do **V4 adaptado pra Vercel**. CLAUDE.md sugere WP em vários dos sites — desatualizado, precisa auditar.
- **Miguel + Gabriel** publicando humano no Cafezinho (11-14 posts/dia). Cross-post automático dos temáticos com essa base pode virar contradição de identidade — merece decisão em §7.3.

Detalhamento técnico completo no fórum companion [`forum_separacao_service_accounts_indexing_20260714.md`](forum_separacao_service_accounts_indexing_20260714.md).

**Bloco A fechado. Bloco B segue pendente das 6 perguntas em §7 acima.**

---

**2026-07-16 01:40 BRT — Miguel — DIRETRIZ MACRO: Bloco B vira V4.1 (framework config-driven)**

Depois do fechamento do Bloco A, Miguel definiu escopo novo pro Bloco B:

- **TODOS os 7 sites terão agentes V4** (não só piloto — todos entram, mas Rio Carta continua sendo o primeiro)
- **Rio Carta NÃO pode ser apenas repetidor de notícia** — precisa **qualidade + novidade** (jornalismo original, não só cross-post do Cafezinho nem RSS reciclado)
- **Estilo V4.1**:
  - **Diretrizes EXTERNAS** — configs por site (YAML/JSON/MD) que definem identidade, fontes, categorias, tom, volume, threshold auditor
  - **ZERO hardcode** — framework único genérico, N configs
  - **Dinâmicos** — configs mutáveis sem redeploy
  - **Modernos** — incorpora práticas 2026 (structured output, config-driven pipelines, sem tomada-de-decisão embutida em código)

**Consequência arquitetural:** V4 atual (que é um agente hardcoded por site) precisa evoluir pra V4.1 (framework genérico + config layer). Piloto Rio Carta = piloto do framework V4.1 + config Rio Carta específica.

**Consequência editorial:** cross-post automático rígido provavelmente sai. Cada site precisa produzir conteúdo com **identidade própria** — Rio Carta pauta hiperlocal RJ, GSN pauta multipolar EN, Mundo Trilhos pauta ferroviária brasileira, etc.

**Próxima ação (retomada 16/07 pela manhã):**
1. Auditoria do estado atual do Rio Carta (silo `Rio Carta Agentes/`, publicações últimas 30d, agentes ativos, publicador Vercel)
2. Desenho preliminar do framework V4.1 (schema de config, componentes reutilizáveis, contratos entre camadas)
3. Fórum específico do piloto: `forum_piloto_v4_1_riocarta_20260716.md`
4. Miguel responde as 5 perguntas restantes do §7 com contexto do relatório
5. Só depois começar código (semana +1)

**Diretriz complementa a memória recente `feedback_auditor_nao_e_curador.md` (16/07)**: auditor V4.1 será veto-only (threshold 40, na dúvida aprova) — decisão de qualidade/relevância fica em outros componentes (ranker + curador) que devem entrar no framework V4.1 também.

---

## 9. Referências cruzadas

- **Fórum companion (infra service accounts):** [`forum_separacao_service_accounts_indexing_20260714.md`](forum_separacao_service_accounts_indexing_20260714.md)
- **Fórum V4 auditoria atual:** `forum_v4_fase6_multicase_dryrun_20260710.md`
- **Cartas V4 em curso (Codex + Fable):** `carta_fable_auditoria_fase*.md`, `carta_gpt55_fable_*.md`
- **Análise SEO Cafezinho canônico:** `forum_analise_gsc_completa_20260714.md`
- **CLAUDE.md** — arquitetura V9 vigente + adendos 6 (fórum obrigatório dúvida grande), 7 (bug meta-discurso), 8 (Lawfare Orlando Diniz), 11 (Rio Carta independência)
- **Silo Rio Carta:** `Rio Carta Agentes/rio_carta/`, fóruns em `Rio Carta Agentes/Foruns/`
- **Silo AIatolah:** `aiatolah/` (agentes, arquitetura, chaves)
- **Silo Cicero (ceara.digital):** `Cicero Agentes/`

---

*Documento vivo. Editar em patch/Edit — nunca full rewrite. Complementar em §8 quando decisões novas forem tomadas.*
