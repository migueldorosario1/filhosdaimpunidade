# Matriz padrão-ouro + plano de correção — Auditoria V4 (Fases 2 e 3)

**Data:** 13/08/2026 · **Agente:** ZCode (Kimi K3)
**Série:** `forum_handoff_zcode_auditoria_todos_v4_padrao_ouro_20260813.md` (carta) → `forum_auditoria_v4_todas_verticais_fase01_20260813.md` (Fase 0+1) → **ESTE** (Fase 2+3)
**Base de prova:** `Memorias/memoria_auditoria_v4_todas_verticais_20260813.md` + `ZCodeProject/auditoria_v4_20260813/fase0/`

---

## PARTE 1 — MATRIZ V4 PADRÃO OURO (veredito por vertical)

Legenda dos 16 critérios da carta: ①fonte/coleta ②intake idempotente ③banco coerente ④seleção aderente ⑤pesquisa/fontes ⑥redação canônica sem fallback legacy ⑦fatos verificáveis ⑧título ≤80c ⑨taxonomia whitelist ⑩dedup pré/pós ⑪criação idempotente retomável ⑫imagem adequada licenciada ⑬falha-imagem desacoplada ⑭logs suficientes ⑮zero publish automático ⑯repetição de ciclos estável.

| Vertical | Veredito | Critérios OK | Falhas | Evidência |
|---|---|---|---|---|
| **Nacional** | **V4 estrutural maduro — NÃO ouro agora (degradado)** | ①②③④⑤⑥⑧⑨⑩⑮ | ⑦ gate factual skip; ⑪ wp_created sem retomada; ⑬ fila bloqueia (19 falhas/24h); ⑫ preso em image_pending (265482) | 296 drafted; 13 draft_confirmed/24h |
| **Geopolítica** | **V4 estrutural maduro — NÃO ouro agora (degradado)** | ①②③④⑤⑥⑧⑨⑩⑮ | ⑬ cota IA 50%/4h estoura e congela (38 falhas/24h); ⑪ idem; ⑦ gate skip | 309 drafted; 17 draft_confirmed/24h; 265504 preso |
| **Tecnologia/Ciência** | **V4 estrutural — instável (não ouro)** | ①②③⑤⑥⑧⑨⑮ | ④ vazamento geopolítico-militar histórico (gate nexus existe mas frouxo); ⑩ sofreu duplicação (29 lixeira 13/08); ⑪ wp_created_failed parado; ⑭ 33 failed/24h opacos | 104 drafted; 3 confirmados/24h |
| **Cultura** | **V4 estrutural — BLOQUEADO (deadlock editorial)** | ②③⑤⑥⑧⑮ | ⑫⑬ SEM IA absoluto + sem foto real = travamento permanente por design; ④ sem gate de nexo (páginas de seção entram); ⑨ órfão 265431 com cat 2403 errada; ⑯ zero ciclos autônomos | 0 drafted; receipts provam redação OK |
| **Economia** | **V4 estrutural — BLOQUEADO** | ②③⑤⑥⑧⑮ | ⑫⑬ fila presa (265454); ④ sem nexo (Nvidia/Trump-Irã entram em economia); ⑭ falhas rc=0 silenciosas | 0 drafted; 1 publish via ponte |
| **Meio Ambiente** | **V4 estrutural — FRÁGIL (nunca completou ciclo)** | ②③⑥⑧⑮ | ⑯ só 2 eventos, ambos failed rc=1; ④ sem nexo (CNN/INPE/Brasil Escola evergreen); ⑭ stderr inexistente | 0 drafted; 28 new no estoque |
| **Esporte** | **V4 estrutural — BLOQUEADO + TTL hostil** | ②③⑤⑥⑧⑮ | ⑫⑬ fila presa (265439); ④ "ao vivo"/fotos de treino entram; freshness 12h × cadência 8h = 18 stale | 0 drafted; 1 publish via ponte |
| **Saúde** | **V4 estrutural — INSTÁVEL** | ②③⑤⑥⑧⑮ | ⑦ gate de acrônimo bloqueou "SUS" (falso positivo editorial); ④ releases CONASS como pauta; ⑭ opaco | 0 drafted; 1 publish via ponte |
| **Regional Sudeste** | **híbrido V4 maduro (pipeline próprio)** | 11 drafted | worker/intake regionais separados do canônico vertical | 46 eventos |
| **Regional Norte** | híbrido, baixa produção | 3 drafted | 1 image_pending | 10 eventos |
| **Regional Nordeste** | **sem redação** | — | tabela draft_events inexistente; 1.481 new acumulados | — |
| **Regional Centro-Oeste** | **sem redação** | — | tabela draft_events inexistente; 758 new | — |
| **Regional Sul** | híbrido, bloqueado | 0 drafted | 1 image_pending | 2 eventos |

**Nenhuma vertical recebe hoje o selo "V4 padrão ouro homologado"** — nacional/geopolítica estão mais próximas (maduras, mas degradadas por imagem/fila); as 5 novas são **V4 estruturais não homologadas** (arquitetura canônica real, zero ciclo autônomo completo).

## PARTE 2 — COMPARAÇÃO CAMPO A CAMPO (novas × fronteiras)

| Campo | Nacional/Geopolítica (fronteira) | 5 novas | Gap |
|---|---|---|---|
| Arquitetura | coletor→intake→worker→redator canônico | **idêntica** (mesmo CONFIG/worker) | nenhum — são V4 de verdade |
| Fontes | RSS+Google+Brave curados, blacklist | idem, mas feeds jovens (CONASS, ge, CNN via Google) | qualidade de fonte |
| Gate de nexo no intake | tecnologia: nexus≥4; política: negative_lula | **nenhum** | 🔴 pauta poluída |
| Frescor (TTL) | 24h/72h | 12–48h (esporte 12h × ciclo 8h = hostil) | 🟠 calibrar |
| Score/seleção | score−poder360, 1 pauta/ciclo | idêntico | nenhum |
| Gates específicos no worker | quarentenas Lula/ciência + taxonomia + título | **só genéricos** | 🟠 gates editoriais próprios |
| Dedup | Jaccard batch + item_key + _is_same_topic (48h V4 + 24h WP) | idêntico (funcionou: Margareth Menezes) | nenhum |
| Idempotência | wp_created imediato (patch 13/08) | idêntico | retomada ausente p/ todos |
| Imagem | geo/ciência: IA c/ cota; nacional: real+válvula | cultura: SEM IA absoluta; demais: válvula após 3 | 🔴 política trava fila |
| Falha-imagem | bloqueia vertical (return 4) | bloqueia vertical (return 4) | 🔴 comum — bug de design |
| Lock | global flock -n (perde rodada) | idem | 🟠 9 rodadas/dia |
| Estados SQLite | coerentes + wp_created/_failed | coerentes | retomada ausente |
| Telemetria | stderr log existe | **nunca gerado** (falhas opacas) | 🟠 |
| WordPress | canônico, draft/pending | canônico (desde 12/08), draft/pending | nenhum |
| Política rascunho | draft→pending→revisão | idêntica | nenhum |
| Recuperação | repair_pending_image + órfãos | idem + órfão cultura sem taxonomia | 🟠 |

## PARTE 3 — PLANO DE CORREÇÃO PRIORIZADO (4 grupos)

### GRUPO 1 — Bloqueadores de integridade

**P1.1 — Retomada determinística de `wp_created`/`wp_created_failed`**
- Causa provada: nacional tem 1 wp_created e ciência 1+1 parados; repair só cobre `image_pending` (memória §4-5).
- Arquivo/função: `v4_vertical_draft_worker.py` — nova função `reconcile_wp_created()` chamada no main() antes de select_candidate.
- Lógica: para cada candidate em wp_created/_failed com evento <72h: GET post no WP → existe+imagem→`drafted`+evento `draft_confirmed`(reconciled); existe sem imagem→`image_pending` (entra no reparo); 404→`new` (wp_created_failed) ou `discarded` (wp_created órfão).
- Risco: baixo (só reconcilia estados; nunca cria post). Backup: `.bak_pre_reconcile_<ts>` + dump dos bancos. Teste: candidato controlado (forçar wp_created num banco de cópia); rodar 2× o mesmo job → mesma candidata, zero posts novos. Rollback: restaurar .bak + statuses anotados em recibo JSON. Critério: ciência e nacional com zero wp_created/_failed parados >24h.

**P1.2 — Backfill taxonomia do órfão 265431 (cultura, cat 2403→79)** — micro-ação WP-CLI pontual, snapshot antes.

### GRUPO 2 — Bloqueadores operacionais

**P2.1 — Fila de imagem NÃO bloqueante (o coração do sprint)**
- Causa provada: `return 4` após falha de reparo + `return 0` após reparo bem-sucedido — seleção nova nunca acontece enquanto houver image_pending (main() L2530-2557). Hoje trava até as fronteiras.
- Proposta: orçamento de reparo = 1 tentativa/ciclo; **se o reparo falhar, segue para seleção nova**, com teto de 3 image_pending simultâneos por vertical (acima do teto, pausa seleção — preserva a lição do incidente 27/07).
- Risco: fila de pendentes sem imagem cresce até o teto — mitigado pelo teto + ponte Kimi/Claude caçando foto. Backup .bak; teste: simular image_pending + rodar worker → novo draft criado MESMO com pendente; rollback: .bak. Critério: vertical com 1 image_pending continua produzindo drafts novos.

**P2.2 — Cultura: destravar o deadlock SEM IA (decisão editorial do Miguel)**
- Opções: (a) manter absoluto e formalizar a ponte humana como etapa do fluxo (SLA 24h, depois descarta candidata); (b) válvula final após 3 tentativas também para cultura; (c) fallback: foto editorial de acervo licenciado por tema (teatro/música/cinema) quando não houver foto do fato. **Recomendo (c)+(a)**: acervo temático licenciado primeiro, ponte humana depois, nunca IA — preserva a decisão 11/08 sem congelar a vertical.

**P2.3 — Lock global com espera curta** — `flock -w 90` (ou retry 1× após 90s) em vez de `-n` puro; 9 rodadas/dia deixam de ser perdidas. Risco baixíssimo. Alternativa estrutural (fase 2): locks por estágio.

**P2.4 — Desacoplar cron** — coleta, intake e worker em linhas separadas por vertical (contenção seletiva, lição da madrugada 13/08). Mudança só de crontab, com backup `crontab.bak_<ts>`.

### GRUPO 3 — Qualidade editorial

**P3.1 — Gate de nexo no intake das 5 novas** — reusar `classifier_keywords` do coletor: score mínimo de aderência (ex.: ≥1 keyword no título OU ≥2 no corpo) + rejeitar título genérico de seção/índice ("Meio ambiente", "Queimadas", "Info Dengue", "IPCA Hoje") + flag/rejeito "ao vivo" em esporte. Causa provada: candidatas-poluição catalogadas na memória §3.
**P3.2 — Whitelist de acrônimos** no gate `editorial_semantics_opaque_acronym_in_title` (SUS, INSS, IPCA, PIB, STF…) — saúde foi bloqueada por falso positivo ("SUS").
**P3.3 — Factual gate honesto** — quando `sem_claims`, registrar "no-op" explícito no detail e no receipt; médio prazo: extrair claims mínimos (datas/números/cargos) sempre.
**P3.4 — Esporte: freshness 12h→18h** OU cadência 8h→6h — hoje 18/49 pautas morrem stale antes de qualquer tentativa.

### GRUPO 4 — Observabilidade

**P4.1 — Redator: receipt também em falha** (hoje só sucesso) + validar stderr capture das 5 novas nas próximas rodadas (patch 12:14 UTC).
**P4.2 — Classificar o `failed rc=0, new_draft_ids []`** (era do espelho) e o rc=1 sem saída — worker deve gravar `redactor_no_output` explícito.
**P4.3 — Agregar `orphan_cross_vertical_skip`** (1 linha/rodada com contagem) — hoje ~25 linhas × 8 verticais × N ciclos de ruído e dezenas de GETs WP por ciclo.
**P4.4 — Métricas no CCTV/Baleia:** rodadas perdidas por lock, repair_preflight_failed, image_pending por vertical, stale_expired.

### Ordem de execução proposta (Fase 4, microetapas, 1 patch por vez)
P2.1 (destrava tudo) → P1.1 (retomada) → P3.1 (nexo) → P2.2 (cultura, c/ Miguel) → P3.2 (acrônimos) → P4.1/P4.2 (telemetria) → P2.3 (lock) → P2.4 (cron) → P3.3/P3.4 → P4.3/P4.4.
Cada um: backup → patch → py_compile → teste controlado → draft/pending only → validação SQLite+WP → re-run idempotência → checkpoint Cérebro.

## PARTE 4 — MANIFESTO DO BACKLOG WP (13/08 ~12:30 BRT)

Com `zizi_job_id` (draft+pending ≈120): geopolítica 49 (38 pending, **9 sem imagem**) · nacional 35 (22 pending, **4 sem imagem**) · ciência 10 (**2 sem imagem**) · regional 4 (1 sem imagem) · cultura 1 (265431 draft, sem imagem, cat errada) · "outro" legacy 17 (14 draft muito antigos + 3 pending).
**17 posts sem featured image** são a fila real da ponte de imagens. Recomendação: (1) os 9 geo + 4 nacional + 2 ciência sem imagem entram na próxima leva da ponte Kimi/Claude; (2) 14 drafts legacy "outro" (meses de idade): candidatos a lixeira recuperável após revisão; (3) 265431: backfill taxonomia + foto real ou lixeira.

## PARTE 5 — Respostas às 10 perguntas da carta

1. **Meio Ambiente, Cultura e Esporte são V4 de verdade?** SIM em arquitetura (mesmo coletor/intake/worker/redator canônico, bancos próprios, receipts). NÃO em maturidade operacional (zero ciclo autônomo completo).
2. **Em quê não alcançam Nacional/Geopolítica?** Gates de nexo no intake, gates editoriais próprios no worker, telemetria de falha, e política de imagem que não congela a fila.
3. **Fallback/legacy executável (agente_controlado, espelho)?** NÃO. Espelho = `if False` (morto); redator = runtime canônico exclusivo; `legacy_agent_used: false` nos receipts. Há código morto + comentários/logs antigos (dívida documental).
4. **Por que zero draft_confirmed nas 5 novas?** Nunca por falta de redação: (a) image_pending na 1ª candidata congela a fila por design; (b) cultura: deadlock SEM IA; (c) falhas intermitentes do redator (json_missing) sem retry no mesmo ciclo; (d) saúde: falso positivo do gate de acrônimo.
5. **O que impede rascunhos estáveis?** Em ordem: fila de imagem bloqueante → ausência de retomada wp_created → gates de nexo inexistentes → telemetria opaca.
6. **Seguro manter os workers ativos durante a correção?** SIM para leitura/auditoria; para os patches do Grupo 1-2, pausar SÓ a vertical em patch (worker nunca publica — risco de campo é duplicata, mitigado pelo wp_created + testes de re-run).
7. **Impedir que falta de imagem bloqueie a redação?** P2.1 (orçamento de reparo + teto de pendentes + seguir produzindo).
8. **Uma candidata → um único wp_post_id?** Já garantido na criação (zizi_job_id + wp_created imediato); P1.1 fecha a retomada; teste de re-run obrigatório por patch.
9. **Nenhum agente publica no ar?** Provado: redator só `draft`; worker só `pending`; publishes com zizi_job_id são promoções externas (Claude/humano). Manter assim: qualquer patch meu será draft/pending-only.
10. **O que autoriza o selo padrão-ouro?** 3 ciclos completos consecutivos (pautas diferentes, sem duplicata, sem intervenção), com imagem adequada, taxonomia whitelist, logs explicando cada falha — por vertical, na ordem cultura→esporte→meio ambiente→economia→saúde→tecnologia→regionais→reauditoria das fronteiras.

---
*Fases 2-3 entregues em 13/08 ~13:00 BRT. Nenhuma linha de código/cron/WP foi alterada neste sprint — tudo aguarda o "vai" do Miguel para a Fase 4.*

---
## ADENDO — DECISÕES DO MIGUEL (13/08 ~12:50 BRT) — FASE 4 AUTORIZADA

1. **"Pode destravar tudo"** — Fase 4 aprovada.
2. **⭐ NOVA REGRA EDITORIAL DE IMAGEM:** *"Não vamos travar os verticais por causa de imagem. Ele pode publicar rascunho SEM IMAGEM e a gente vai atrás depois."* — image_pending NUNCA mais bloqueia produção; o rascunho nasce (pending, sem featured_media) e a ponte busca a imagem depois.
3. **Ligar o worker regional** (Nordeste/Centro-Oeste sem draft_events).
4. **Criar um bloco Regional no Cafezinho** (home).
5. **Nova camada de ajuda (eu, ZCode):** automação em loop a cada 30 minutos caçando imagens adequadas para os posts V4 sem featured_media.
6. **Regra absoluta REAFIRMADA:** V4 nunca publica direto — sempre draft/pending, sempre via Claude.
7. **Não esquecer o V4 Ciência** (33 failed/24h, wp_created_failed, taxonomy_not_confirmed).

---
## ✅ FASE 4 EXECUTADA (13/08 ~13:50 BRT) — tudo testado, zero publicação

**Patches no NYC (backups: `.bak_pre_destrava_20260813_162941`, `.bak_pre_reconcile2_*`, `.bak_pre_rotacao_*`, `.bak_pre_fome_*`):**
1. **`v4_vertical_draft_worker.py` — V4_DESTRAVA_20260813:** (a) falha de reparo de imagem NÃO bloqueia mais (só pausa acima de `IMAGE_PENDING_TETO=3` posts sem imagem em aberto — válvula anti-fila-infinita); (b) falha de imagem no fluxo novo vira **`draft_sem_imagem`** (post fica pending, evento image_pending alimenta a ponte, produção continua — nova regra Miguel); (c) **`reconcile_wp_created()`**: wp_created/wp_created_failed reconciliados com o WP real (post+imagem→drafted; post sem imagem→image_pending; publish→external_resolved; trash→discarded; 404→new) + **retry de wp_created_failed sem post após 6h** (máx 2/ciclo); (d) fail-open, orçamento 5 WP-calls/ciclo.
2. **`v4_regional_draft_worker.py` — top-27 + fome + rotação:** fila do motor agora com as 27 UFs (CO estava FORA do top-10); prioridade 1ª=UF que NUNCA produziu (bootstrap NE/CO/Sul), 2ª=UF sem draft há 6h, 3ª=comportamento antigo.

**Provas (testes controlados, tudo draft/pending):**
- esporte: `external_resolved` (265439, publicado pela ponte) → fila LIBERADA;
- **meio ambiente: PRIMEIRO draft_confirmed da história (265552, COM imagem via busca ativa)**;
- ciência: rodou (hourly_quota — cron das 16:10 já produzira; reconcile roda antes do cooldown);
- regional: motor escolheu **RS** (faminta) e reconciliou 265135 `external_resolved`;
- **idempotência:** re-run meio_ambiente → `hourly_quota`, zero duplicata;
- nacional 265478 (wp_created) será reconciliado no próximo ciclo do cron (17:20 UTC).

**Bloco Regional na home (canônico):** `front-page.php` 761→801 linhas, após Esporte/antes da Linha do Tempo; consulta cat 4986+5 regiões (posts regionais carregam UF+região, category__in não é hierárquico); modelo col-md-7+col-md-5 do bloco Vídeos; exclui 28/20751/20699. Backup `/root/backup_bloco_regional_20260813_133857/` (+rollback.sh). PHP lint verde, cache flush, **HTTP 200 ao vivo com posts+thumbs renderizados**.

**Automação nova (camada de ajuda do próprio ZCode, ordem Miguel):** `automation-e1b2d648` "🖼️ Caçadora de imagens V4" — **a cada 30 min** busca fila de image_pending nos bancos, pesquisa imagem real licenciada (Commons/Flickr CC/PD, licença verificada na página), aplica via WP-CLI `www-data` (máx 3/rodada, NUNCA publish), registra em `Foruns/ponte_imagens_v4_LOG.md`. Bancos se auto-reconciliam no ciclo seguinte de cada worker.

**Estado pós-Fase 4:** espera-se produção contínua em TODAS as verticais (rascunhos podem nascer sem imagem), NE/CO entrando na rotação regional, posts sem imagem sendo caçados pela automação */30 e revisados/publicados SÓ pelo Claude.

### Adendo Fase 4 (13/08 ~13:55) — Regional invisível no hambúrguer: CORRIGIDO
- **Causa:** Regional estava no nível 2 (dentro do dropdown "Editorias"▸Política▸Regional▸regiões) — no offcanvas mobile, dropdown aninhado do Bootstrap 5 na prática não abre → Miguel não via.
- **Fix:** item 263595 promovido a **nível 1** do menu 21062 (`--parent-id=0`, ordem após Editorias); regiões+estados continuam como subitens. Snapshot pré-mudança: `/root/backup_menu_regional_topo_20260813_134609/menu_21062.json`.
- **Efeito colateral bom:** o rodapé (nav depth=1) também ganha "Regional" como link de topo.
- **Prova ao vivo (pós purge WP Rocket + cache-buster):** offcanvas nível 1 = Quem somos? / Editorias / **Regional** com 12 subitens renderizando (5 regiões + 7 estados).
- **Aprendizado:** `wp cache flush` NÃO limpa o WP Rocket — precisa `wp rocket clean` + rm do `wp-content/cache/wp-rocket/`.

### Adendo Fase 4b (13/08 ~14:00) — Árvore Regional▸Região▸Estado (ordem Miguel)
- **Menu WP 21062:** 7 estados existentes re-paiados + **20 estados criados** como itens de categoria sob suas regiões (Pará slug `para-estado`); ordenação via `wp_update_post` na coluna `menu_order` (aprendizado: `--menu-order` não existe no wp-cli e `_menu_item_menu_order` meta é ignorado). Snapshot: `/root/backup_menu_regional_arvore_20260813_*/menu_21062.json`.
- **Header desktop (hover):** Regional ▸ 5 regiões ▸ cada região abre seu submenu de estados (27 no total, `dropdown-submenu` aninhado). Backup: `/root/backup_header_regional_arvore_20260813_135645/`.
- **Provado ao vivo:** desktop com 5 submenus aninhados + 27 estados; hambúrguer com Ceará dentro de Nordeste (árvore correta, depth=3).
