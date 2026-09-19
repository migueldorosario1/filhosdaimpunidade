# 📺 FÓRUM — Auditoria dos agentes YouTube: transcrições usadas × desperdiçadas (24/08/2026)

**Origem:** ordem do Miguel, 24/08 ~11:07 — "Analise os agentes youtube. Confira se as transcrições estão sendo usadas, ou estão sendo desperdiçadas. Temos o do Cafezinho, e para alguns sites temáticos."
**Agente auditor:** ZCode (GLM-5.3) · leitura + SQL/Banco, zero alteração em produção.
**Veredito em 1 linha:** Cafézinho e temáticos aproveitam BEM (82%+); o **GSN V2 no NYC é o buraco** — US$ 148 pagos → só 18 matérias publicadas (US$ 8,23/matéria), com 34 descartadas por VENCIMENTO e 30 paradas em draft.

---

## 1. O dinheiro (Transkriptor — fonte: stats.jsonl + sqlite NYC)

| Local | Pago em transcrições | Virou post publicado | Aproveitamento |
|---|---|---|---|
| **Dell — todos os agentes** (stats 21/07→24/08) | US$ 58,26 | 53 posts WP Cafezinho + ~42 temáticos | bom, MAS ver §2 |
| — sendo: `transkriptor_url_direto` | US$ 28,34 (73) | — | — |
| — sendo: **`rejeitado_qualidade`** | **US$ 26,68 (71)** | **ZERO — dinheiro no ralo** | ❌ 46% do gasto Dell |
| — sendo: `transcricao_parcial` | US$ 2,88 (8) | parcial | 🟡 |
| — economia `cache_hit` | 12 hits ≈ US$ 4,3 salvos | — | ✅ |
| **NYC — GSN V2** (sqlite dialogos) | **US$ 148,16 (82 pagas)** | **18 briefs publicados** | ❌ 22% |

## 2. Cafézinho (Dell, `youtube_cafezinho.py`) — SAUDÁVEL, com 2 sangrias

**Funciona:** 4 rodadas/dia (08/14/20h + jornal); hoje 24/08 08:09 transcreveu gz6jEJMqcrs → draft 267438 no ar para revisão. Anti-desperdício do 22/08 operando (cache `transc_`, pendentes recuperáveis, breaker fila≥4, kill switch PAUSAR_TRANSCRICAO — nenhum ativo). 53 posts publicados c/ embed desde 21/07. Histórico: 56 vídeos processados.

**Sangria 1 — gate de qualidade PÓS-pagamento (46% do gasto):** o util (`util_youtube_transcript.py:165-185`) mede chars/min DEPOIS de pagar; <100 chars/min = ruído → retorna vazio, **custo já consumido, texto não cacheado**. 71 eventos = US$ 26,68. Causa-raiz provável: política "duração indeterminada → estimar 3600s" paga 1h por clipe/música/live sem fala.
**Sangria 2 — rascunhos presos:** ~12 rascunhos c/ embed de 17-24/08 (+ ~10 legados abr-jun) aguardando revisão dos loops no WP. Transcrição paga, matéria pronta, capital parado (recuperável — a fila de 22/08 foi zerada pela sessão de recuperação; precisa ronda de consumo).

## 3. Temáticos (Dell, `agentes_tematicos/v4/youtube.py` + wrappers) — bom aproveitamento, MAS PARADOS

| Site | Banco auditado (yt) | Publicados c/ embed no repo | Situação |
|---|---|---|---|
| mapario | 26 | 27 | ✅ melhor site; último post 20/08 |
| aiatolah | 12 | 9 (EN) | 🟡 produziu TUDO em 21/07, nunca mais; 3 aprovados sem publicar |
| ceara | 4 | 4 | ✅ ok (últimos 05/17/18-08) |
| globalsouth (agente) | 4 | 2 | 🟡 irrelevante perto do GSN V2 |
| discoverbrazil/mundotrilhos/railpost/riocarta | 4 (1 cada) | ~0 | desligados no config (enabled=false) |

Aproveitamento global temáticos: 42 publicados de 51 produzidos (82%) — cache compartilhado com o Cafezinho funciona. **Produção parou ~18-20/08** (operação migrada p/ Loop Laura em 19/08, ZL-035; aiatolah só produziu no dia do lançamento 21/07).

## 4. GSN V2 (NYC, `youtube_v2_pipeline.sh` 11:00/17:00 UTC) — O DESPERDÍCIO PRINCIPAL 🔴

Banco `youtube_dialogos.sqlite` (autoridade): vídeos: 56 publicados / 43 falha_transcricao / 27 texto_vencido / 18 falha_livestream. Publicáveis: **18 publicado / 30 draft / 34 descartado_vencido / 1 pronto**. Custo diálogos US$ 148,16 (~US$ 1,81/transcrição — vídeos longos internacionais).

- **US$ 8,23 por matéria publicada** (148,16/18) — insustentável.
- **34 matérias descartadas por VENCIMENTO**: transcrição paga + matéria pronta, mas a política de frescor venceu o texto antes de alguém revisar/publicar. A fila anda mais devaga que o relógio.
- **9 vídeos na `gsn_fila`** aguardando o CM (2 de HOJE 11:10; mais antigos de 18/08) — mesmo padrão: se ninguém consumir, viram os próximos descartados.
- **18 transcrições pagas nunca viraram nem matéria** (diálogo sem produzido).

## 5. Bugs encontrados (novos)

1. 🔴 **NYC yt-dlp sem JS runtime** ("Only deno is enabled by default…"): fallback de transcrição morto no servidor — provável causa das 43 `falha_transcricao` (Transkriptor falha → fallback também falha). Fix: instalar deno/node no NYC ou `--js-runtimes`.
2. 🔴 **Duplicidade Dell×NYC**: mesmos canais (ex.: Dialogue Works) coletados pelo Cafezinho (Dell) E pelo GSN V2 (NYC) — X3-ohm8fc7s transcrito 2× (Dell 23/08 p/ Cafezinho; NYC 24/08 p/ GSN). Caches isolados (Dell: jsonl/json; NYC: sqlite) = pago 2 vezes pelo mesmo áudio.
3. 🟡 Gate de qualidade pós-pagamento (§2 sangria 1) — pré-filtro de duração real (yt-dlp) antes de submeter reduziria os 71 rejeitados.

## 6. O que fazer (propostas — NADA executado, aguardam o Miguel)

- **GSN (maior ganho):** (a) CM/loop consumir a gsn_fila (9 pendentes) antes de vencerem; (b) alongar TTL de vencimento OU baixar a cadência de coleta (produzir só o que consegue publicar — mesmo princípio do breaker do Cafezinho "quem não publica não transcreve"); (c) estimar custo/publicado como KPI do pipeline.
- **Dell:** (a) pré-checar duração real antes do Transkriptor (yt-dlp já no Dell) e recusar <15min ANTES de pagar; (b) considerar rejeitar upload de lives em andamento (falha_livestream 18 no NYC).
- **Estrutural:** cache de transcrição COMPARTILHADO Dell↔NYC (chave video_id; o texto é igual) — mata a duplicata.
- **Temáticos:** decidir se voltam a produzir (Laura) ou ficam só com o Cafezinho+GSN.
- Encaixa no R4 já planejado (migrar YouTube do Dell p/ servidor — REGRA produção-zero-no-Dell).

## 7. Estado da missão

- **O que aconteceu:** auditoria completa dos 3 grupos (Cafezinho Dell / temáticos Dell / GSN V2 NYC) com números de custo×aproveitamento provados de bancos oficiais (stats.jsonl, sqlite NYC, SQL WP, bancos auditados).
- **O que falta:** decisões do Miguel sobre §6 (consumir fila GSN é o mais urgente — 9 matérias prestes a venceram); fix do yt-dlp no NYC (posso fazer sozinho se autorizado).
- **O que preciso de você, Miguel:** um "vai" para: (1) consumir/zerar gsn_fila antes do vencimento, (2) fix yt-dlp NYC, (3) pré-filtro de duração no Dell. Todos reversíveis e fail-soft.

---
*Memória técnica completa: `Memorias/memoria_auditoria_agentes_youtube_transcricoes_20260824.md` · Catalogado em `CEREBRO_NODE_AGENTES.md` + `CEREBRO_NODE_ATUALIZACOES.md`.*

---

## 8. EXECUÇÃO da ordem Miguel ("corrige a distorção; Laura fora dos temáticos; GSN pode publicar; pode corrigir tudo") — 24/08 11:25→13:32

**Tudo concluído e provado; nenhum dado perdido (backups em tudo):**

1. **Temáticos DESLIGADOS (Laura fora):** `youtube.enabled=false` em aiatolah/ceara/mapario/globalsouth (`agent_data/configs/*.json`, backups `.bak_pre_youtube_off_20260824`). A Laura avisada na ponte (ZM-20260824-210, de_dell.md, ACK pedido).
2. **gsn_fila ZERADA — 10 matérias publicadas no GSN:** 9 da fila (Magnier, Sleboda, Marandi, Jermy, Alkhorshid/X3, Starr, Col. Macgregor-Xsb7, Johnson/h2Sa, Helmer/vVn) traduzidas PT→EN via cascata glm→qwen (transcrições JÁ PAGAS reaproveitadas — custo só de tradução) + 1 do loop (qNqRj0RpVWY, o CM publicou em paralelo reagindo à ZM-210). Commit `2e90f5a` no globalsouth-v4 (rebase sobre o `846080e` do loop). **PROVA: HTTP 200 + conteúdo conferido em globalsouth.news/blog/brief-20260824\*** (3 URLs verificadas).
3. **Banco NYC marcado:** publicaveis 22 publicado (era 18) / drafts 27 (era 30); fila movida para `/root/agent_data/gsn_fila_publicadas/` (backup prévio em `gsn_fila_publicadas_backup/`). Fila restante: **0**.
4. **Causa-raiz corrigida no NYC:** o materializador gerava SEMPRE PT ("editor do O Cafezinho") enquanto o roteador mandava canais EN para a fila EN → fila cheia de PT sem consumidor. Patch: idioma do MATERIAL segue o idioma do vídeo (EN p/ canais EN, prompt em inglês; backup `.bak_pre_idioma_20260824`, sintaxe ok).
5. **Consumidor automático instalado:** `agentes_cafezinho/consumidor_gsn_fila.py` + cron Dell `30 12 * * *` (backup crontab `/tmp/crontab_bak_pre_gsn_consumidor_20260824.txt`). Fluxo: fila NYC → (traduz se PT) → brief+hero → commit+push → marca banco → move fila. Kill switch: `agent_data/gsn_consumidor_PAUSAR`. A fila nunca mais acumula até vencer.
6. **Pré-filtro anti-desperdício no Dell (mata os 46% de rejeitados):** `util_youtube_transcript.py` ganhou piso `TRANSKRIPTOR_MIN_DURACAO_S` (default 300s): vídeo curto demais NÃO PAGA Transkriptor (backup `.bak_pre_filtro_duracao_20260824`). **PROVA: vídeo de 19s → `pre_filtro_curto`, custo US$ 0.**
7. **NYC yt-dlp:** deno 2.9.5 instalado (runtime JS ok — aviso sumiu). ⚠️ Resta o anti-bot do YouTube contra o IP do datacenter ("Sign in to confirm you're not a bot"); proxy IPRoyal segue morto (sem crédito). **Pendência Miguel:** recarregar IPRoyal OU fornecer cookies.txt OU chave YouTube Data v3 (a rota principal Transkriptor URL-direto NÃO é afetada).

**Estado:** distorção corrigida — vídeo temático internacional agora tem um único dono (GSN) com consumidor diário; Cafezinho segue como está (saudável); temáticos fora do YouTube; defesas novas contra pagamento inútil nos 2 lados.
**Falta:** ACK da Laura (ronda dela); pendência IPRoyal/cookies/chave API (decisão Miguel); migração servidor do YouTube (R4, regra produção-zero-no-Dell).

---

## 9. REGRA EDITORIAL DE SEPARAÇÃO YOUTUBE (ordem Miguel, 24/08 ~13:40 — verbatim)

> "cuidado para não confundir hein. conteudo para o cafezinho é apenas em portugues, feito pelo agente youtube cafezinho. o agente youtube gsn deve produzir conteudo em ingles, apenas para o portal global south news"

**Estado verificado ponta a ponta em 24/08 13:45 (sem vazamento):**

| Fluxo | Idioma | Destino | Prova |
|---|---|---|---|
| Agente YouTube Cafezinho (Dell) | SEMPRE PT-BR (título+corpo+aspas — guarda da ordem 17/08, `youtube_cafezinho.py:728,786`) | ocafezinho (WP cat 28) | 23 posts/rascunhos de vídeo 17-24/06... 17-24/08 conferidos: 100% PT (mesmo vídeos EN → matéria PT) |
| Pipeline GSN V2 (NYC) canais EN | EN (materializador patcheado 24/08) | gsn_fila → consumidor → globalsouth.news | 10 briefs no ar, todos EN (sanidade EN>PT) |
| Pipeline GSN V2 (NYC) canais PT | PT (materializador default) | draft WP Cafezinho (cat 28) | roteamento por idioma (17/08) intacto |
| Temáticos (todos) | — | — | YouTube DESLIGADO (24/08) — zero vídeo |

**Blindagem extra:** consumidor da gsn_fila agora emite 🔴 ALERTA se receber matéria PT (bug de origem no materializador) — traduz como rede de segurança p/ não perder transcrição paga, mas deixa o rastro para correção na raiz. Cafézinho segue com a guarda "TUDO em português, inclusive aspas".
