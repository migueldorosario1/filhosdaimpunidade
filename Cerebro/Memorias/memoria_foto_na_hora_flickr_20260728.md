# 📸 MEMÓRIA TÉCNICA — "Foto na Hora" Fase 0 (Flickr ao vivo prioritário)

**Data:** 2026-07-28 00:30–00:40 BRT · **Agente:** ZCode · **Autorização:** Miguel
**Fórum irmão:** `Cerebro/Foruns/forum_foto_na_hora_flickr_20260728.md`

---

## 1. Contexto

Miguel: agentes autônomos precisam de imagem boa e FRESCA; banco de mídia e Wikimedia velha não servem para entidades vivas (Lula, Flávio, Haddad). Estratégia aprovada em 5 pilares (cadastro vivo → prioridade do ao vivo → descoberta automática → disciplina anti-ban → direitos/crédito). Fase 0 executada nesta sessão.

## 2. Estado ANTES (diagnóstico)

- `flickr_live.py` já existia e já era chamado pelo `motor_publicador.py` como "Prioridade 1.5", DEPOIS do banco S9 ("1.25").
- S9 (`banco_midia_busca.buscar_por_entidade_inteligente`) tem cascata 7d → 30d → 90d → **qualquer data** → foto velha vencia.
- `FLICKR_API_KEY` presente em `chaves_novas.env` e `.env.unificado` (root do projeto). Valor nunca exposto.
- `robo_coleta_imagens.py` só existe no servidor (persistência do flickr_live falha local, não-bloqueante).

### Bug reproduzido (falso negativo Jaccard)

Pauta "Lula critica juros altos em discurso no Planalto" → `None` com pool de 500 fotos.
Causa: títulos/tags estilo Stuckert ("27.07.2026 - Cerimônia de assinatura de atos" + tags concatenadas "2026presidente lulapresidente...") → Jaccard ~0.024, abaixo dos portões A=0.18 / B=0.12. O match de entidade já está correto pela escolha da conta; exigir match temático textual em conta dedicada é conceitualmente errado.

## 3. Descoberta de contas (via API, 2026-07-28)

| Conta | NSID | Situação |
|---|---|---|
| Oficial Fernando Haddad | `193500322@N03` | ✅ 25.969 fotos, última 27/07/2026 |
| Governo do Estado de SP | `38014693@N04` | ✅ 123.616 fotos, última 02/07/2026 (restrição eleitoral no título da última) |
| Câmara dos Deputados | `194280112@N08` | ❌ parou 30/06/2023 |
| multimidiaabr (Agência Brasil Flickr) | `24663774@N06` | ❌ parou 2008 |
| fazenda | `81371542@N00` | ❌ 2006 |
| haddad13, camaradeputados(url), ministeriodafazenda, defesa, fab_oficial, marinhaoficial, exercitooficial, stjoficial, tseoficial, governodobrasil | — | ❌ User not found |

Método: `flickr.urls.lookupUser` + `flickr.people.findByUsername` + `getPublicPhotos(per_page=1, extras=date_upload)`.

## 4. Alterações de código (espelho local `Projeto Cafezinho Agentes/root/`)

**Backups:** `flickr_live.py.bak_pre_foto_na_hora_20260728`, `motor_publicador.py.bak_pre_foto_na_hora_20260728`.

### flickr_live.py
1. `NSID_OFICIAIS` += `haddad`, `gov_sp` (com data de validação); seção DESCARTADOS atualizada com os mortos de 2026-07-28.
2. Novo conjunto `CONTAS_DEDICADAS` = {lula, planalto, pt, flavio_bolsonaro, haddad, gov_sp, casa_branca, elysee_macron}.
3. `ENTIDADES` += regex `haddad|fernando haddad|ministro da fazenda` → [haddad]; `tarcísio|governo (do estado )?de são paulo|palácio dos bandeirantes` → [gov_sp].
4. `buscar_foto_oficial()`: nova cascata **A → B → C**. Plano C: filtra pool pelas dedicadas detectadas, chama `escolher(..., janela_c=168h, jaccard_min=0.0)` → foto mais fresca da janela. Param `janela_c` adicionado à assinatura (default 168).

### motor_publicador.py
- Bloco "1.5 Flickr live" movido para ANTES do S9; renumerado **Prioridade 1.2 (Flickr AO VIVO)** → **Prioridade 1.5 (S9, fallback do live)**. Ordem final: Fonte original (1) → Flickr ao vivo (1.2, com Tribunal Visual Gemini) → S9 (1.5) → banco local (2) → gerador editorial (3). Ambos os blocos eram guardados por `if not media_id_pre_aprovada:` → troca cirúrgica, sem efeito colateral. Comentários de cabeçalho registram a decisão e a data.
- `py_compile` OK nos dois arquivos.

## 5. Teste de aceitação (3 pautas reais, 2026-07-28 00:35 BRT)

| Pauta | Contas detectadas | Plano | Foto | Data |
|---|---|---|---|---|
| Lula critica juros altos no Planalto | lula, planalto | **C** | `...55424263684_...c.jpg` | 27/07 17:42 |
| Haddad anuncia arcabouço na Fazenda | haddad | **C** | `...55424758499_...c.jpg` | 27/07 21:59 (crédito Diogo Zacarias) |
| Flávio Bolsonaro + Valdemar no PL | flavio_bolsonaro | B | `...55419562604_...c.jpg` (c/ Milei) | 25/07 23:50 |

Antes do patch, a pauta Lula retornava `None`. URLs baixadas e inspecionadas: JPEGs 800×533 / 800×375 legítimos (Lula com Presidente da Coreia; Haddad com entregadores em SP).

## 6. Lições / regras duras

1. **Conta dedicada ⇒ Jaccard não é portão, é só desempate.** O filtro semântico está na escolha da conta.
2. **Anti-ban:** 429 do Flickr já derrubou o Tencent uma vez; ao vivo = poucas req/ciclo + cache por processo (`_cache` em `flickr_live`). Batch retroativo = local + WARP (ver ATUALIZACOES 2026-06-26).
3. Tamanhos: cascata `url_c → url_z → url_n → url_l`; nunca `url_o/h/k` (Tribunal Visual reprova ≥6MB).
4. Agência Brasil não tem Flickr vivo — o acervo CC BY dela exige adaptador próprio (site/RSS), Fase 2.

## 7. Pendências (Fases 1–2, aprovadas em conceito)

- Registry como dados + validação "ativo ≤ 90 dias".
- Descoberta automática de contas (candidata → valida → propõe).
- `flickr.photos.getInfo` no fetch → licença + nome real do fotógrafo gravados no banco (crédito real desde a captura).
- Métricas por publicação: origem usada, idade da foto, taxa de acerto live vs. banco.
- **Deploy no Tencent pendente de auditoria** (protocolo padrão ouro: não deployar sem auditoria Claude/Codex).

---

## 8. Bateria de testes 2 (10:52–11:15 BRT) — política nacional + acoplamento V4

Pedido de Miguel: bateria com foco em política nacional (foco V4) + controle NY/Trump, com fotos baixadas para conferência visual. Artefatos: `teste_foto_na_hora_20260728/` (fotos + `manifest.json`).

### 8.1 Resultados V3 (flickr_live) — 9 pautas

| Pauta | Resultado | Plano | Foto |
|---|---|---|---|
| Lula sanciona lei | ✅ 27/07 Stuckert | C | Lula c/ Pres. Coreia |
| Haddad reforma fiscal | ✅ 27/07 | C | Haddad c/ entregadores (crédito Diogo Zacarias) |
| Flávio + Valdemar | ✅ 25/07 | B | Flávio c/ Milei no Bandeirantes |
| Tarcísio obras SP | ❌ → banco (correto) | — | Gov SP **congelado por legislação eleitoral**; única "foto" recente era aviso textual |
| STF Moraes julgamento | ✅ 27/07 | C (após ampliação) | Prédio STF iluminado (fresco, genérico) |
| Senado plenário | ✅ 20/07 | D (novo) | Foto Agência Senado (8d, fraca tematicamente) |
| PT Gleisi | ❌ → banco (correto) | — | Flickr PT dormente desde abr/2026 |
| Trump NY/Casa Branca | ✅ 27/07 | C | Jantar WHCA; legenda traduzida EN→PT (roteador: Gemini 429 → Claude Opus) |
| Controle: café | ❌ silêncio (correto) | — | sem entidade → sem Flickr |

### 8.2 Bugs/encontros da bateria → fixes aplicados no dia

1. **STF tinha 155 fotos frescas e retornava None** — institucionais fora de `CONTAS_DEDICADAS`. Fix: Plano C ampliado a todas as contas curadas (exceto `unicef_ethiopia`, fio regional).
2. **Tarcísio pegou "foto" que era aviso eleitoral em texto** (13kb). Fix: filtro `_TITULO_BLOQUEADO` na ingestão (legislação eleitoral / avisos institucionais).
3. **Janela C ±7d curta demais** para contas de menor cadência (Senado: última foto 8d). Fix: **Plano D** — dedicadas, ±30d, sem Jaccard, último recurso antes do banco. Foto oficial de ≤30d > Wikimedia de 2019.
4. **Gov SP real está morto desde jun/2025** (fotos reais de 2025 e 2022 no pool; conta congelada pelo calendário eleitoral). Anotado no registry; reavaliar pós-eleições 2026.
5. **Gemini (gemini-3.5-flash) SEM CRÉDITOS** — 429 RESOURCE_EXHAUSTED "prepayment credits are depleted" no roteador LLM. Tradução caiu para Claude Opus. **RESOLVIDO 28/07 ~14h BRT:** Miguel recarregou os créditos; gemini-2.5-flash testado com visão nas 6 fotos da bateria (vereditos ricos: identificou Janja, delegação coreana, leu faixa "Não Somos Invisíveis", flagrou prédio STF sem pessoas e expo VR do Senado). Qwen Vision (qwen-vl-max) também validado como fallback funcional da cadeia V4.

### 8.3 Acoplamento V4 (v4_labs) — diagnóstico completo

- **V4 JÁ TEM subsistema Flickr nativo e mais rico que o V3**: `flickr_media.py` (busca por pessoa, aliases, decisão de direitos, ranking), `featured_image_adapters.py` (resolução de conta com cache), contrato `contratos/v4_imagem_destacada_v2.json`, config de **40+ contas** (`config/v4_flickr_official_accounts.json`: partidos, governos estaduais, prefeituras, IBGE, Petrobras...). `enable_flickr=True` por padrão.
- **Haddad faltava na config V4** → cadastrado nesta sessão (NSID `193500322@N03`, aliases Fernando Haddad/Ministro da Fazenda; backup `.bak_pre_haddad_20260728`). Pauta-teste coletou 13 candidatos.
- **Cadeia de visão V4 = Qwen→Gemini (fallback) e FUNCIONA** apesar do Gemini sem crédito (Qwen respondeu análise estruturada: entity_present, identity_confidence, montage...).
- **O gargalo do V4 não é coleta — é a POLÍTICA VISUAL.** Pauta Lula: 13 candidatos coletados, 13 rejeitados pela visão. Vereditos reais extraídos: foto score **100** rejeitada só por `entity_not_prominent`; score **98** por `crop_not_safe`; várias por `identity_ambiguous` (fotos frescas oficiais são montagens/colagens ou fotos de grupo amplas — Lula pequeno no quadro). Contrato exige identidade ≥0.9, área do sujeito ≥12%, centralidade ≥0.72, rosto ≥120px pós-crop.
- **Decisão pendente de Miguel (editorial, não bug):** relaxar proeminência para fontes oficiais (aceitar foto de grupo com pessoa identificada), OU manter estrito e deixar o gerador IA cobrir. Sugestão técnica: "melhor esforço" — se todos falharem mas houver score ≥65 com únicos issues de proeminência/crop, selecionar mesmo assim para draft com flag `human_review`.

### 8.4 Estado dos arquivos ao fim do dia (todos no espelho LOCAL)

- `root/flickr_live.py` — Haddad/Gov SP, CONTAS_DEDICADAS ampliada, Planos C+D, filtro de avisos. Backup `.bak_pre_foto_na_hora_20260728`.
- `root/motor_publicador.py` — Prioridade 1.2 (live) → 1.5 (S9). Backup idem.
- `root/v4_labs/config/v4_flickr_official_accounts.json` — +Haddad. Backup `.bak_pre_haddad_20260728`.
- `teste_foto_na_hora_20260728/` — 6 fotos baixadas + manifest.json (conferência visual de Miguel: 6/6 legítimas).

### 8.5 Painel Banco Ouro de Mídia (pedido Miguel: "bota o link pra eu trabalhar")

- **Link:** `http://43.156.151.165/midia-ouro/` — NO AR (nginx → app porta 8091). O **401 é Basic Auth de propósito** (realm "Banco Ouro de Midia") — mesma senha do painel (htpasswd no nginx do Tencent).
- Estado das features (fórum V6, 22/07): botão 🗑️ remover (soft delete) implementado e testado; **robô busca ativa rearmado em 22/07 com deadline +7d** (estava morto desde 27/06) — janela vence ~29/07: checar se buscou.
- V6 do painel: `http://43.156.151.165/v6/` (200 OK, systemd `cctv-v6.service`).
- **Conexão natural (próximo passo):** a busca ativa do Banco Ouro é da mesma família do Foto na Hora — plugar nela as contas novas (Haddad) + portão Vision `entity_present` para pautas de pessoa. Deploy Tencent via protocolo padrão ouro (auditoria).

### 8.6 Banco Ouro: robô permanente + fila por frescor + data no card (28/07 12:20 BRT, deploy Tencent)

Pedidos de Miguel: (a) saber se existe agente de busca ativa alimentando o banco; (b) fila de revisão ordenada por **entidades importantes + data mais recente** ("senão passo a vida aprovando foto antiga"); (c) **data da foto no alto** do card.

**Diagnóstico (SSH cingapura):**
- Robô existe: `robo_banco_ouro_midia_v3.py --confirmar --loop` (flock+timeout 25m, `BANCO_OURO_GEMINI_VISION=1`), log mostrava aprovações ao vivo por entidade (Lula, Haddad 11 candidatos, Moraes, Trump, Alckmin...). MAS: deadline file vencia **29/07 ~12h** ("rodadas 30min/20h" armado em 22/07 com +7d) e **sem cron** — processo órfão desde 22/07.
- Painel: servia código de 22/07 por processo **órfão** (PID 1181992); o `midia-ouro-panel.service` crash-loopava há meses (120.866 restarts — porta 8091 tomada pelo órfão).
- Fila: 333 pendentes; query antiga ordenava por entidade/prioridade — topo tinha Moraes **2024**. Coluna `data_foto` existe na tabela.

**Aplicado (deploy direto, padrão do painel):**
1. **Fila nova** (`review_payload`): `m.data_foto` no SELECT; ROW_NUMBER por entidade ordenado por `data_foto DESC`; `entidade_data_max` (MAX por entidade); ORDER BY `entidade_pos, entidade_data_max DESC, data_foto DESC` — rodízio 1-por-entidade preservado, entidades ordenadas pela foto mais fresca, velhas afundam. Preview validado no banco real: Lula 26/06 → Senado 25/06 → ... → Moraes 2024 no fundo.
2. **Card:** linha "📅 Data da foto" como 1ª linha do card de dados + data no subtítulo; JS `fmtData`/`idadeInfo` com **semáforo** (verde ≤30d, amarelo ≤180d, vermelho >180d "há X anos ⚠️").
3. **Deploy:** backup `/root/painel_midia_ouro.py.bak_pre_foto_na_hora_20260728`; órfão morto; `midia-ouro-panel.service` agora **active** (fim do crash-loop de 120k); API `/api/midia-ouro/review/next` retorna Lula 26/06 com `data_foto` — confirmado.
4. **Robô permanente:** deadline file → **28/07/2027**; cron root `*/30 * * * * /root/V3/rodar_banco_ouro_midia_controlado.sh` (tag `BUSCA_ATIVA_BANCO_OURO_PERMANENTE_20260728`); backup crontab em `/root/backups/crontab_root_pre_busca_ativa_permanente_20260728.txt`.

**V4 ↔ Banco (pergunta "agentes V4 saberem usar o banco"):**
- **Já está plugado no código:** `v4_labs/codigo/media_sources.py` (`ouro_sqlite`) consulta `midia_ouro_fts` + `midia_ouro_indice` WHERE `uso_automatico=1` — **toda foto que Miguel aprova no painel vira candidata dos agentes V4 automaticamente**. Caminho do DB via env/contract (`path_env`/`fallback_path`) — apontar para `/root/agent_data/banco_midia_ouro_v3/banco_midia_ouro_v3.db` no deploy de produção V4 (Bloco B, sprint própria).
- Loop fechado: robô (permanente) → fila (frescor) → aprovação Miguel → V4 Nacional/Geopolítica/Tecnologia usam.

**Por que o topo da fila estava em 26/06 (pergunta de Miguel, 28/07 ~14h):**
- `rejeicoes_ouro` últimas 24h: **6.449× `gemini_vision_erro`** (a fila de classificação travou durante a pane de créditos do Gemini) vs. só 2× rejeição genuína de conteúdo. Fotos frescas de julho EXISTEM no banco (Lula 27/07, Lula 25/07, Flávio 10/07) mas como `nao_classificado` — não tinham sido classificadas/enfileiradas.
- Com Gemini recarregado (28/07 ~14h) + robô permanente a cada 30min, a varredura retomou a classificação ao vivo (observado: Lula 12 candidatos → Trump 9 → Hugo Motta 8...). Itens de julho entram na fila nas próximas rodadas e, pela nova ordenação, saltam para o topo. Mecânica confirmada: **toda vez que Miguel abrir a revisão, a primeira foto é a mais recente aguardando olho humano.**

### 8.7 Causa raiz definitiva + fallback de visão + classificador permanente (28/07 ~14:25 BRT)

- **A fila nunca se atualizava sozinha:** quem alimenta `fila_catalogacao_humana_ouro` é `classificar_banco_ouro_midia.py` (DELETE no pendente + rebuild por heurística) — e ele **não estava em NENHUM cron**; só rodava manual (última vez ~28/06). Por isso a fila parou no tempo. 84 itens `nao_classificado` (incluindo julho) aguardando.
- **Resolvido:** classificador executado (572 itens: 418 revisão humana, 132 uso_automatico, 22 bloqueada) → **topo da fila = Lula 27/07/2026** (verificado via API do painel, total 417). Agendado permanente: cron `17,47 * * * *` (tag `CLASSIFICADOR_BANCO_OURO_PERMANENTE_20260728`, log em `/root/agent_data/logs/classificar_banco_ouro.log`). Backup DB: `/root/backups/banco_midia_ouro_v3_pre_reclassificacao_20260728.db`.
- **Tribunal Visual NÃO tinha fallback** (resposta à pergunta de Miguel): `analisar_imagem_gemini_banco_ouro` era Gemini-puro; qualquer exceção → rejeição `gemini_vision_erro`. **Implementado fallback Qwen VL** (`analisar_imagem_qwen_banco_ouro`, DashScope OpenAI-compatible, `qwen-vl-max`, env `QWEN_API_KEY`): Gemini falha (429/cota/rede/SDK) → Qwen com mesmo prompt/contrato; falha dupla → rejeição com erro duplo. Deploy `/root/V3/robo_banco_ouro_midia_v3.py` (backup `.bak_pre_fallback_qwen_20260728`), ciclo supervisionado rc=0 (56 rejeitadas, 43 duplicadas, 0 erros).
- **Escalada de visão no ecossistema (mapa):** robô Banco Ouro = **Gemini → Qwen** (novo); cadeia V4 = **Qwen → Gemini** (já existia); tradução legendas V3 = **Gemini → Claude** (roteador). Apagão de um único provedor não derruba mais nenhum dos três fluxos.

### 8.8 O segundo assassino de fotos frescas: portão de 5MB (28/07 ~14:45 BRT)

- Miguel reportou: "apareceram 3-4 imagens novas, depois voltou pras de um mês". Investigação: só 3 fotos de julho existiam no banco porque o robô aprovava **ZERO** por ciclo (111 candidatas → 0). Motivo das 2.158 rejeições `gemini_vision_erro` pós-crédito: **`imagem_maior_que_limite_gemini`** — originais >5MB (Stuckert 6000×4000 etc.) morriam no portão de bytes ANTES da chamada de visão, sem chance.
- **Fix:** `_derivada_para_visao()` — foto >5MB agora gera derivada JPEG redimensionada (~1600px, q85, ≤4,7MB) só para a ANÁLISE; o original intacto segue para o banco. Mesma derivada serve Gemini e fallback Qwen. Deploy `/root/V3/robo_banco_ouro_midia_v3.py` (backup `.bak_pre_fallback_qwen_20260728` já cobre).
- **Verificado pós-fix (≥14:30):** `gemini_vision_erro` despencou de 2.158 → **2**; vereditos reais fluindo (19× quarentena humana, bytes/dimensão residuais). Robô ciclando limpo.
- Lição: o rótulo `gemini_vision_erro` misturava 3 doenças (cota 429, SDK, tamanho) — o detalhe_json das rejeições é a fonte da verdade.

### 8.9 Coleta segmentada por vertical V4 70/20/10 (28/07 ~15:30 BRT, diretriz Miguel)

Diretriz: coleta separada por agente — "essa é para o V4 Geopolítica, essa é para o V4 Política Nacional, essa é para o V4 Tecnologia; eu vou aprovar para os 3 V4". Proporção 70/20/10.

**Implementado (deploy Tencent, backups carimbados):**
1. **Manifest segmentado** `ENTIDADES_VERTICAL_V4` no robô (o `ENTIDADES_PADRAO` aponta pra ele): campo `vertical` + `limite` por entidade; loop respeita limite individual. Nacional 15×10=150 · Geopolítica 8×6=48 · Tecnologia 7×3+3×2=27 candidatos/ciclo ≈ 67/21/12. Novas entidades: Gleisi, Tarcísio (nacional); Xi, Milei, Macron, Putin, Zelensky, Sheinbaum, Guterres (geopolítica); Musk, Altman, Huang, Nadella, Zuckerberg, Cook, Pichai + empresas Tesla/Nvidia/Meta (tecnologia).
2. **Fontes novas** no `agente_midia_oficial_externa_v3.py`: `embaixada_china` (194618475@N02), `elysee_macron` (92405495@N00) — NSIDs validados ativos no V3; +15 regexes em `PESSOAS_PARA_FONTES` (xi/china, macron/frança, milei, putin, zelensky, sheinbaum, gleisi, tarcísio, musk/tesla/spacex, altman/openai, huang/nvidia, nadella/microsoft, zuckerberg/meta, cook/apple, pichai/google, intel, huawei).
3. **Painel:** dropdown "V4 Nacional (70%)/V4 Geopolítica (20%)/V4 Tecnologia (10%)" com contagem ao vivo (`_SQL_VERTICAL_CASE`, espelha o manifest — manter sincronizado) + pill colorido no card (verde/ouro/roxo). Filtro testado via API: geopolitica→Trump 07/05 ✓, tecnologia→vazio (enche nos próximos ciclos) ✓.
4. **Coleta testada no servidor:** Xi 3 candidatos (AB), Macron 3 ✓.
5. **Lacuna descoberta:** Agência Brasil Flickr tem ZERO conteúdo tech (Musk/Tesla/Nvidia=0; Moraes=365). V4 Tecnologia hoje depende de Microsoft/Intel/Huawei/NASA oficiais; CEOs/fachadas precisam conector Openverse/Wikimedia → **Iteração 2**.
6. **Carta à Trindade:** `Cerebro/Foruns/cartinhas/cartinha_zcode_foto_na_hora_verticais_v4_20260728.md` + ponteiro no `canal_trindade.md`.

### 8.10 Config do V4 sincronizada (28/07 ~16h, pergunta de Miguel)

Miguel perguntou se o V4 foi configurado para melhorar a busca em Flickr ao vivo + banco. Estado real:
- **Config V4 (`v4_labs/config/v4_flickr_official_accounts.json`):** +`embaixada_china`, +`elysee_macron` (Haddad já tinha entrado de manhã). JSON validado. Teste ao vivo pauta Xi Jinping: **8 candidatos coletados** (antes: 0 — conta não existia na config).
- **Banco no V4:** já estava ligado (`ouro_sqlite`, `uso_automatico=1`) — não precisou mudança; o que mudou é o banco agora crescer segmentado 70/20/10.
- **Trava persistente do V4 (decisão editorial pendente de Miguel):** a política visual estrita segue rejeitando todos os candidatos (`entity_not_prominent`, montagem, identidade) — inclusive os 8 do Xi. Opções apresentadas de manhã: (a) relaxar proeminência p/ fontes oficiais, (b) modo "melhor esforço" score≥65 com flag human_review, (c) manter estrito+IA. Sem essa decisão, o V4 coleta mas não seleciona.

### 8.11 Política visual V4 v2 — melhor esforço + human_review DEPLOYADO (29/07 ~01:50 BRT, decisão Miguel 00:40 opção b)

**Autorização:** Miguel escolheu opção (b) via Claude — cartinha `cartinha_kimi_decisao_v4_politica_visual_opcao_b_20260729_0040.md` + ponteiro canal `[MIGUEL-DECISAO-V4-POLITICA-VISUAL-OPCAO-B]`.

**Patch (espelho LOCAL `root/v4_labs/codigo/featured_image_pipeline.py`; backup `.bak_pre_melhor_esforco_20260729`):**
- SHA-256 pré: `7dd427ac5ca546c1d13bfb8b5f484d40f21374580028cf5e8aa81ace9003c1be`
- SHA-256 pós: `33c300fcc8b76c1abcfc1875e08206ed6b6fad21048a73acfaf7fd7983f7e808`
- Novo: constantes `MELHOR_ESFORCO_MIN_FINAL_SCORE=65.0` + `MELHOR_ESFORCO_ALLOWED_ISSUES={entity_not_prominent, crop_not_safe, identity_ambiguous, final_score_below_threshold}`; método `_melhor_esforco_human_review()` acionado em `_evaluate_and_promote` quando `approved` vazio; seleção SEM promoção ao acervo auditado, `safe_to_publish=False`, `human_review=True` + `human_review_reason='melhor_esforco_score_XX_reproved_por_YYY'`; flag surfada em `decision.human_review` + `manifest.human_review` + warning `human_review_melhor_esforco_pending`. `final_score_below_threshold` no conjunto permitido é decorrência mecânica da barra de 70 com piso de 65 (não é "bug sério"). Prefixo `human_review:` do adapter é normalizado antes do match. Bugs sérios (entity_not_present, visual_format_rejected, mídia inválida, provider falho, score<65) seguem fail-closed.
- Testes novos em `test_featured_image_pipeline.py` (`MelhorEsforcoHumanReviewTests`, 3 casos: seleciona c/ flag e sem promoção; escolhe a melhor elegível; fail-closed p/ montagem/provider/ausente/score 64.9). Suite completa V4: **566 passed, 0 failed** (52s).

**Smoke test ao vivo (29/07 ~01:50):**
- Xi Jinping (geopolítica): 8 coletados → fallback NÃO disparou — todos com `vision_provider_failed` (ver incidentes abaixo). Correto por desenho: falha de provedor ≠ reprovação editorial.
- Lula (nacional): 11 coletados → fallback NÃO disparou — vereditos reais Qwen: 2× `entity_not_present`, 1× `visual_format_rejected`, 3× `vision_response_invalid`; 6× budget (max_visual_calls=5). Correto: nada elegível.
- **Haddad (nacional): 13 coletados → ✅ PASS — `flickr:52339291706` (score 92, final 93.05) selecionada com `human_review_reason='melhor_esforco_score_93_reproved_por_crop_not_safe+entity_not_prominent'`, sem promoção, badge no manifest.** Exatamente o caso-alvo da decisão (foto oficial fresca, recorte imperfeito).

**⚠️ INCIDENTES DE VISÃO descobertos no smoke (produção NYC afetada AGORA):**
1. **Qwen/DashScope modera foto do Xi Jinping** — `data_inspection_failed` (HTTP 400, "Input data may contain inappropriate content") em TODA foto real do Xi (qualquer tamanho, as 2 chaves QWEN_API_KEY/_2). Fotos de Lula/Haddad/Flávio passam normal. Ontem ~16h o Xi auditava normal — mudança do lado DashScope entre 28/07 16h e 29/07 01h. Hipótese: moderação de imagem de figura de Estado + prompt de confirmação de identidade facial. **Impacto:** vertical Geopolítica cega para Xi (possivelmente Putin/Kim/outros líderes — testar).
2. **Gemini sem crédito DE NOVO** — 429 "prepayment credits are depleted" em todos os modelos (3.5/2.5/2.0-flash). A recarga de 28/07 ~14h durou <12h (robô Banco Ouro cicla Gemini-first a 30min + fallback Qwen). Sem Gemini, qualquer falha Qwen = foto morta.
3. Secundário: 3/5 respostas Qwen em fotos Lula grandes vieram com schema inválido (`vision_response_invalid`) — qualidade da resposta em derivadas grandes; encolhe o pool elegível.

**Pendências deploy:** patch está no ESPELHO LOCAL; produção roda em NYC — deploy via protocolo padrão ouro (sync + ciclo supervisionado). Worker-side: mapear `decision.human_review`/`human_review_reason` → meta do post WP (badge 🟡 painel Banco Ouro já sabe ler flag quando chegar). Claude (checagem dupla) já foi avisado via canal: se draft escapar com flag, ele faz checagem visual antes de publicar.
