# 🗺️ Fórum — Mapa da arquitetura de publicação + diagnóstico do bloco TECNOLOGIA + ronda dos loops

```yaml
tipo: FORUM (Tema Duplo com memoria_mapa_arquitetura_publicacao_20260825.md)
autor: ZCode/GLM-5.3 (missão tripla, ordem Miguel 25/08 ~12:10)
data: 2026-08-25 12:20 BRT
escopo: LEITURA de produção (ssh nyc / cafezinho-wp / tencent / 159.89.185.209) — zero mudança em código/servidor
não_tocar: FAROL/audiência (painel_cctv_v6.py + contador) — território de outra sessão
refs: ZM-20260825-018 (pergunta aos loops em inbox_trindade/de_zcode.md)
```

---

## 1) MAPA DA ARQUITETURA DE PUBLICAÇÃO (estado em 25/08 ~12h BRT)

### 1.1 Cadeia editorial (fluxo único canônico desde 24/08: V4.1)

| Etapa | Onde | Ritmo | Mecanismo |
|---|---|---|---|
| **1. Coleta** | NYC crontab root | ciencia `10,40 * * * *` (2×/h) · geo horária `0 * * * *` · nacional `20 */6` · economia `35 */4` · cultura `5 */4` · meio/esp/saúde 1×/dia · FDS boost | `coletor.py <sigla>` (RSS/Brave/GoogleNews; `no_proxy` minúsculo) → grava `candidates` no banco da vertical |
| **2. Intake/curadoria (tese)** | NYC | junto com a coleta | `v4_vertical_intake.py <vertical>` → gates de tema/veto → bancos `/root/agent_data/v4_verticals/<vertical>.sqlite3` (tabela `candidates`: `new`→`drafted`; `rejections`, `draft_events`, `tombstones`) |
| **3. Geração V4.1** | NYC `/root/v4_labs/codigo/v41_ciclo.py` | nacional `25 */2` UTC · economia `35 1-23/2` · ciencia `45 */2` · geopolitica `55 */2` | candidata → **tese dinâmica** LLM (fail-closed: sem tese ancorada não escreve) → redator runtime **gpt-5.5** → rascunho **WP draft** (via `controle.ocafezinho.com`, meta `_v4_versao=4.1`) → **FC websearch** (Perplexity sonar-pro) → **ciencia nasce com cats [30,2403]** (patch 24/08). NUNCA publica |
| **4. Gates de nascimento** | NYC (dentro do ciclo/worker) | cada rascunho | 5 gates de packaging (sanitizador `<cite>`; data do lide; tabela de cargos; FC-2 do fato âncora; juiz anti-canibal inter-vertical 40 posts/72h) + anti-repetição 50 títulos + tese ancorada |
| **5. Esteira/publicadores** | **CM** (Claude Miguel, host `cafezinho-wp`-irmão `cafezinho-cm`, SSH whitelist) + **AGY** (Antigravity CLI, Dell) | **slots de ~30 min** (hoje: 22 publicadas até 11:52; agenda tipo 09:08→09:38→10:08…) | 3º checador (libera/retém) → revisão editorial (título máx 1 nome próprio — emenda 9; nomes via banco 231 personagens) → **agendam/publicam** draft→publish. Ronda 30/30 (automation ZCode `c1437347`) **NUNCA publica** — só vigia |
| **6. Gates visuais** | NYC + WP | contínuo | Tribunal Visual (`agent_roteador_llm.py`; emendas 7/8: carimbo MD5, logo nunca é capa) · caçadora de imagens (flickr_live, Plano C) · mu-plugin emenda 10 (cat 28 Vídeos exclusiva do Agente YouTube) · trava HOLD editorial (ticket Claude-ZCode 18/08) |
| **7. Pós-publicação** | NYC | `*/30` indexação PULL (cota 200/dia) · `0 *` remover_no_home · `25 *` top_tendencias_push (espelho) · `52 *` performance GA4 · `23:30` Tribunal Agêntico Diário (diretriz viva realimenta o briefing) | — |

### 1.2 Publicadores paralelos (fora da esteira CM/AGY)

| Publicador | Onde | Ritmo | Nota |
|---|---|---|---|
| **Repetidor Estatal** | NYC `agente_repetidor_estatal.py` | `7 */2` | **publish DIRETO** (Opção D; ranker top-3 + auditor binário threshold 40, veto-only). Fontes: Agência Brasil/Senado/Câmara/Governo/IBGE/STF. `promote_estatal_drafts.py` PAUSADO (fila vazia) |
| **Agente YouTube** | NYC `youtube_v2_pipeline.sh` | `0 11,17` UTC | transcrição → curador (`youtube_cafezinho.py`, breaker fila≥4) → posts cat 28; PT no Cafezinho, EN no GSN |
| **Temáticos (8 sites)** | NYC `/root/tematicos` | `0 12,18` BRT `--sem-youtube` | 2 posts/dia por site (restaurados 24/08); GSN via fila própria (consumidor no Dell 12:30) |
| **Rio Carta/Cícero** | `159.89.185.209` | coleta rotativa `0,30` (janelas) + `cicero_remote_publish.sh` `23 *` | site próprio, publica direto |
| **Legado apagado** | NYC | — | `maestro_distribuicao.py` (mestre publicador) pausado 19/07; `motor_publicador.py`/`motor_super_esteira.py` fora do cron (agentes verticais velhos); draft worker **V4 desligado 24/08** (V4.1 único redator) |
| **Tencent** | — | — | não publica posts no ocafezinho (telemetria/painel/FAROL — território da outra sessão) |

### 1.3 Onde posts FICAM PRESOS (pontos de acúmulo mapeados)

1. **Rascunhos V4.1 não consumidos**: 52 drafts `_v4_versao=4.1` hoje; total >500 drafts + 361 pending (superprodução ~51 rascunhos/dia × ~28 publicados — auditoria 24/08).
2. **Pending do 3º checador**: triagem R1a proposta (lotes 20/dia) ainda não executada.
3. **Categoria órfã**: post publicado em cat que não alimenta bloco nenhum da home (caso 267566 "Pesquisas", adendo 130; e os 267189/267212 só-Redação deste diagnóstico).
4. **no-home (20699)**: 2 posts; removidos horariamente pelo `remover_no_home.py` quando elegíveis.
5. **repair_preflight**: falhas 521/503/500 em `controle.ocafezinho.com` (19–21/08) deixaram repairs de ciência pendentes.

### 1.4 Achados técnicos do mapa (armadilhas para futuras consultas)

- **`term_taxonomy_id` ≠ `term_id`** no WP: Tecnologia=term 30/tax 31; Ciência=735/740; IA=5008/5008; Redação=2403/2403. Query SQL errada = resultado falso-negativo (aconteceu na 1ª tentativa desta missão).
- **Bloco TECNOLOGIA da home** (`front-page.php`): `category__in [19936, 735, 30, 5008]` — **19936 não existe mais** em `wp_terms` (referência morta) — e `category__not_in [28 Vídeos, 20751 Youtube, 20699 no-home, 1271/1426 Esporte(s)]`.
- **Canibalização de blocos (`$excludes`)**: cada bloco empurra os IDs já exibidos para `post__not_in` dos seguintes. Ordem: Nacional → Geopolítica → Economia → Coluna → Regional → **Tecnologia** (6º). Post multi-categoria aparece SÓ no primeiro bloco elegível — Tecnologia perde para Economia/Geopolítica.
- **Crons V4 "desligados" por comentário inline**: linhas marcadas `# V4_DESLIGADO_20260824` com o `#` DEPOIS do comando **continuam rodando** (o comentário inline não desativa linha de cron). Prova: `ciencia_cron.log` rodou 25/08 14:40 UTC. Efeito líquido correto (o que morreu foi o redator V4; a coleta é compartilhada e proposital), mas a documentação do crontab é enganosa.
- **Config de categorias do worker V4** (`v4_vertical_draft_worker.py`): ciencia `[735,30,5008]`, economia `[43]`, geopolitica `[5003]`, nacional `[22]` — o patch V4.1 de ciencia sobrescreve com `[30,2403]`.

---

## 2) MISTÉRIO DO BLOCO TECNOLOGIA — veredito com números

**Janela auditada: 22/08 12h → 25/08 12h (3 dias).**

### 2.1 Os números (produção ciencia → WP → bloco)

| Métrica | Valor | Fonte |
|---|---|---|
| Pautas NOVAS no banco ciencia (`candidates` drafted) | **2** (22/08 e 24/08 — o intake marca pouco; o ciclo reusa pautas) | `ciencia_tecnologia_ia.sqlite3` |
| Rascunhos V4.1 ciencia criados | **16** (22/08: 2 · 23/08: 6 · 24/08: 7 · 25/08 meio-dia: 1) ≈ **4-5/dia** | `/root/v4_labs/dados/v41_ciclo/*.json` |
| Rodadas ciencia que NÃO produziram | bloqueios: `todas_pautas_ja_rascunhadas_24h` (maioria), `sem_tese_ancorada_nao_escreve` (~40% das rodadas 24-25/08, incl. OpenAI 2× hoje por anti-repetição), `redator_falhou` 3× (timeout WP) | log v41_ciclo |
| Publicados no WP com cat do bloco (30/735/5008) | **11** (22/08: 1 · **23/08: ZERO** · 24/08: 5 · 25/08 meio: 5) | WP SQL |
| Publicados ciencia FORA do bloco (invisíveis) | **4**: 267189+267212 (só cat 2403 Redação — nenhuma editorial!) · 267450+267503 (2403+5003 Geopolítica) | WP SQL |
| Drafts ciencia PRESOS | **6** (22-23/08, todos pré-patch: 3 variantes dedup "Brasil-China IA" + 3 China militar) | WP SQL |
| Drafts V4.1 presos (todas verticais) | **52** | WP SQL |

### 2.2 Veredito A/B/C (+ fator D novo)

- **(A) "produzindo SEM categoria adequada" — CONFIRMADA para 23-24/08, JÁ CORRIGIDA em 24/08.** Prova: 267189/267212 publicados 23/08 com SÓ a categoria Redação (2403) — é exatamente o dia do buraco ZERO no bloco. A correção já existe: patch do v41 (`if a.vertical == "ciencia": categories=[30,2403]`, 24/08) + convocação ZM-016 de hoje 10:48 ("preservar cat Tecnologia ao publicar — somar ok, trocar não").
- **(B) "produção pequena" — CONFIRMADA.** ciencia gera ~4-5 rascunhos/dia vs ~12/dia das demais verticais. Gargalo em cascata: coleta repetida (feed pouco novo p/ banco), gate de tese ancorada barrando ~40% das rodadas, anti-repetição inter-vertical (OpenAI barrado 2× hoje) e 3 timeouts do redator.
- **(C) "publicadores guardando" — PARCIAL.** 6 drafts ciencia de 22-23/08 nunca publicados (52 V4.1 no total), mas são do período pré-patch/dedup; a esteira de 24/08 em diante publicou 10 de 10 elegíveis do período.
- **(D) fator NOVO (não estava nas hipóteses): CANIBALIZAÇÃO PELO BLOCO ECONOMIA.** 6 posts recentes com cat 30 têm TAMBÉM cat 43 (267407/267441/267486/267512/267524/267597); com `$excludes` e Economia vindo antes na home, eles aparecem no bloco ECONOMIA e somem do TECNOLOGIA. O bloco mostra 1 hero + 5 cards — e perde metade dos candidatos para blocos anteriores.

### 2.3 O gap exato (conta de 3 dias)

**16 gerados → 10 publicados (6 presos em draft) → 6 publicados com cat visível ao bloco (4 desviados: 2 sem cat editorial + 2 para Geopolítica) → menos de 6 de fato exibidos após canibalização do `$excludes`.** Perda total: ~62% da produção ciencia não chega ao bloco Tecnologia.

### 2.4 Recomendações (decisão do Miguel — nada foi alterado)

1. Publicador preservar cat 30 (já convocado ZM-016) + **NÃO adicionar cat 43** em post de ciencia (a menos que seja pauta de economia) — ataca (D).
2. Triar os 4 publicados sem cat (267189/267212/267450/267503): somar cat 30/735 conforme conteúdo — recupera (A) retroativo.
3. Decidir os 6 drafts presos 22-23/08 (3 são variantes dedup da mesma pauta).
4. Se quiser bloco mais cheio: subir produção ciencia (coleta de fontes novas — hoje 2×/hora no mesmo feed) OU 2º post por slot.

---

## 3) RONDA com os loops — o que sabiam / não sabiam

### 3.1 O que JÁ estava registrado (e onde)

| Loop | O que registrou sobre publicação | Onde |
|---|---|---|
| **AGY (Antigravity CLI/Dell)** | rondas confirmando publicações slots ~30min, agendamentos, capa, YouTube | `canal_trindade.md` (rondas 22-25, 23/08) |
| **Ronda 30/30 (ZCode)** | adendos 123-134 HOJE: 22 publicadas, slots, gates, emendas 5-10, §129/§130; adendo 133 (V4.1 Tendências NÃO existe — oferta aguarda "vai"); adendo 130 (sumiço por categoria órfã — padrão idêntico ao bloco Tecnologia) | `forum_v4_labs_subida_pipeline_llm_tudo_20260822.md` |
| **Claude Laura** | proposta dos 5 gates; ticket HOLD editorial × esteira de imagens; sanitizador | `proposta_v41_cinco_gates_packaging_20260823.md`; inbox claude.md |
| **GM (Grok Miguel)** | vereditos/notas das correções V4.1 | `v41_vereditos_loops.md` (GM-012) |
| **Auditor de títulos** | entregas diárias de sugestões sobre pending/draft | inbox claude.md/canal |
| **Codex Miguel** | **HOLD desde 19/08** (`HOLD_LOOP_ATIVO_DIVERGENTE_SEM_ITEM_CODEX`) — sem publicar | `log/loop_codex_miguel/last_message.md` |
| **Auditoria ZCode 24/08** | pipeline V4.1 completo + superprodução 51/dia × 28 publicados + R1a triagem pending | `forum_auditoria_gasto_openai_v4_superproducao_20260824.md` |

### 3.2 O que NÃO estava no Cérebro (achados exclusivos desta ronda — agora registrados aqui)

1. Mecânica `$excludes` de canibalização entre blocos da home (causa D do mistério).
2. `term_taxonomy_id ≠ term_id` (30→31, 735→740) — armadilha silenciosa de SQL.
3. Cat 19936 referenciada no tema do bloco Tecnologia **não existe** (referência morta).
4. Crons V4 "desligados" por comentário inline **ainda rodam** (coleta) — ambiguidade documental no crontab NYC.
5. Número exato do gap ciencia (16→10→6→<6) e a conta dos 4 desviados + 6 presos.

### 3.3 Pergunta deixada nos canais vivos

- **`inbox_trindade/de_zcode.md` criado (ref `ZM-20260825-018`, 25/08 12:15)**: "o que vocês sabem sobre arquitetura/ritmo/slots/gates que AINDA NÃO está no Cérebro? … registrem AGORA respondendo aqui." Respostas virão nas próximas rondas (AGY 30-60min; CM; GM 1h) — consolidar aqui quando chegarem (próxima sessão ou ronda).

---

## 4) Estado da missão (o que aconteceu / o que falta / o que preciso do Miguel)

- **O que aconteceu:** mapa completo levantado (leitura-only, nada alterado em produção); mistério do bloco Tecnologia resolvido com números (A+B confirmadas, C parcial, D novo); pergunta publicada aos loops; tudo registrado (fórum + memória + NODE_ATUALIZACOES + monitor).
- **O que falta:** (1) colher respostas dos loops em de_zcode.md e consolidar; (2) decisões do Miguel sobre as 4 recomendações §2.4; (3) triagem R1a dos 361 pending segue pendente da auditoria 24/08.
- **O que preciso do Miguel:** OK para (a) triar/retificar categorias dos 4 publicados sem cat; (b) regra "ciencia não ganha cat 43" para os publicadores; (c) destino dos 6 drafts ciencia presos; (d) veredicto sobre porteiros restantes (porteiro de estoque aguarda "vai" desde a ronda 30/30; V4.1 Tendências idem, adendo 133).

— ZCode/GLM-5.3 · 25/08/2026 12:20 BRT
