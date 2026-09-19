# 📋 FÓRUM — V4 Nacional: diagnóstico do colapso de publicação + fix da coleta (proxy) — 22/08/2026

**Sessão:** ZCode/GLM-5.3 (Dell) · **Ordem do Miguel (22/08 ~10:00 BRT):** "análise de saúde do V4, principalmente Nacional/Política: por que publica pouco? muito pendente/rascunho? está jogando fora? coleta/Brave funcionando? curadoria com tese/vilão? bancos cheios/rotacionados? proposta focada em QUALIDADE (spam update do Google)".
**Memória técnica irmã:** `Memorias/memoria_v4_nacional_diagnostico_coleta_proxy_fix_20260822.md`

---

## 1. Resumo em 5 linhas (o que aconteceu / o que falta / o que preciso de você)

- **O V4 Nacional parou de publicar porque a COLETA morreu em 20/08**: o proxy IPRoyal (sem crédito, erro 402) é `HTTP_PROXY/HTTPS_PROXY` default do NYC e o `feedparser` do coletor obedece o env → 10 feeds RSS de política + Google News voltavam feed **vazio sem erro** desde 20/08. Com frescor do nacional = 24h, o estoque secou em 1 dia → `no_candidate` em cascata.
- **Brave NÃO era o problema da chave** (chave VIVA, HTTP 200, já rodava fora do proxy) — o problema era um gap da reforma de 11/08: `politica` ficou fora do `freshness="pw"` do Brave → queries traziam landing pages de seção (CNN Política, Portal Câmara) sem data de notícia → rejeitadas por `source_too_old`.
- **FIX APLICADO E PROVADO (22/08 13:13–13:21 UTC)**: coletor.py baixa RSS+GoogleNews com `trust_env=False` + `politica` entrou no freshness pw; flickr_live.py idem (fotos oficiais Lula/Planalto). Prova: g1 voltou com 100 itens; rodada real → **16 candidatas de hoje** (Datafolha, Gilmar/Ficha Limpa, eleições 2026), 15 novas no banco, **draft 267050 criado**, Flickr persistiu 145 fotos. Backups no NYC.
- **Falta (decisão do Miguel):** (1) IPRoyal: recarregar OU assumir que V4 vive sem proxy (coleta já não precisa; coringa AssemblyAI ainda quebra por proxy — NO_PROXY não cobre `api.assemblyai.com`); (2) fila de 33 pending nacional VELHOS (03–18/08, pautas furadas) — propor sweep; (3) **gate de tese/vilão ainda NÃO existe no V4** — textos estão factuais (confirma queixa do Miguel).
- **Preciso de você:** nada urgente para o site voltar (nacional volta sozinho no cron 14:20 UTC). Decidir: recarregar IPRoyal? aprovar sweep dos pending velhos? aprovar o Pacote Qualidade (§5)?

## 2. Números da saúde (levantados 22/08 ~13:10 UTC)

**Publicação v4d_nacional por dia (canônico):** 08/08: 10 · 09/08: 17 · 10/08: 14 · 11/08: 14 · 12/08: 6 · 13/08: 4 · 14/08: 14 · 15/08: 12 · 16/08: 16 · 17/08: 14 · 18/08: **23** · 19/08: 18 · **20/08: 5 (proxy morre)** · **21/08: 2** · **22/08: 0 até o fix**.
Outros verticais aguentaram mais (janela de frescor maior): geopolítica 72h seguiu com 13–20/dia (22/08: 9); ciência 7d seguiu; economia (24h) também secou (21/08: 3, 22/08: 0).

**Coleta (runs do nacional):** 15–19/08: 600–940 itens vistos/dia, 427–792 aceitos/dia → 20/08: 84 vistos/13 aceitos → 21/08: 60/4 → 22/08 manhã: 28/0. Todas as 10 fontes de política com `last_found=0` (falso silêncio: erro de proxy não contava como error).

**Filas no canônico (não só V4):** pending total 353 (V4: geo 60, nacional 33, ciência 18, regional 14 — nacional de 03–18/08 = pautas velhas); drafts 2.311 (acumulado histórico); **future 0**.

**Banco nacional.sqlite3:** 477 candidates → 412 drafted (87%), 10 discarded, 52+3 editorial_blocked; rejections 93 (62 `source_too_old` = landing pages, 17 data inválida, 14 trava `negative_lula_poll_forbidden`); 543 tombstones (rotação anti-repetição OK).

**Curadoria/tese:** prompt do redator quase não exige tese (2 menções leves — título com "UMA tese factual" e diretriz "análise com tese prende mais que fato seco; mediana 25 views — mirar melhor, não publicar mais"). Exemplo 266972 (21/08): factual puro, sem vilão/ângulo (e com bug factual "George Santoro" já em BUGS_ATIVOS). A reforma E-E-A-T/FRESCOR (20/08) ficou na esteira AGY, não chegou ao V4.

**Cadência crons NYC:** geopolitica 30min · ciência 30min · **nacional 2h** · economia/cultura 4h · meio/esporte/saúde 8h.

## 3. Causa raiz (cadeia completa)

1. IPRoyal fica sem crédito (~20/08) → túnel 402.
2. `chaves.sh` exporta `HTTP(S)_PROXY=geo.iproyal.com:12321` para todos os crons V4.
3. `feedparser.parse(url)` (urllib) obedece o proxy → feeds voltam vazios **sem exceção** (errors=0 no ledger de fontes — monitor cego).
4. Google News idem (`Google=0` nos logs).
5. Brave rodava fora do proxy (trust_env=False desde sempre) mas `politica` ficou fora do `freshness="pw"` (correção de 11/08 só cobriu as 5 novas verticais) → resultados sem `page_age` descartados pelo fix anti-invenção de data + queries estáticas retornam as mesmas URLs (dedup mata) + o que sobra é landing page de seção → `source_too_old`.
6. Líquido: 0 pautas novas/dia. Estoque encolhe; frescor nacional 24h seca o banco em 1 dia → worker `no_candidate` → zero publicação.
7. Bônus do mesmo proxy: `flickr_live` (fotos oficiais Lula/Planalto) morto → posts de política nascem `draft_sem_imagem` e penduram no pending (33 nacional).

## 4. Fixes aplicados (com backups; padrão agir-e-explicar — produção parada 2 dias)

| Arquivo (NYC) | Backup | Mudança | Prova |
|---|---|---|---|
| `/root/coletor.py` | `.bak_pre_fix_coleta_proxy_20260822` | helper `_fetch_feed_bytes` com `requests.Session trust_env=False` para RSS+GoogleNews; `politica` incluída no `freshness="pw"` do Brave | g1: 0→100 itens; rodada real: **16 candidatas, 15 novas** |
| `/root/flickr_live.py` | `.bak_pre_fix_proxy_20260822` | `consultar_conta` usa Session `trust_env=False` (Flickr API pública não precisa de proxy) | **145 fotos persistidas** no banco na 1ª consulta |

Estado transitório: `estoque_politica.json` velho arquivado como `.bak_pre_fix_20260822` (cache expirado — comportamento normal).

## 5. Pacote Qualidade (proposta — aguarda "vai" do Miguel; spam update Google)

1. **Gate de tese no nacional**: prompt passa a exigir tese/ângulo/vilão explícitos; curadoria reprova texto sem tese (padrão FRESCOR nota 1–5, trava ≥3 — mesma travada dupla homologada na esteira AGY).
2. **Menos e melhores**: meta nacional 4–6/dia (hoje ~15–23 no pico). Cotas por janela (já existe `_home_pct_janela`) ajustadas para qualidade.
3. **Sweep da fila pending**: 33 pending nacional de 03–18/08 → pautas furadas (freshness já estourado) → mover para rascunho/arquivo com recibo. Também rever 60 pending geo.
4. **Queries Brave ricas p/ politica** (8–10 rotativas: "eleições 2026 pesquisa Datafolha", "STF pauta hoje", "Congresso votação Lula", "Petrobras notícia", "governo Lula anúncio"... ) substituindo as 5 genéricas que puxam landing pages; manter `freshness=pw` (já feito).
5. **Decisão IPRoyal**: (a) recarregar (volta AssemblyAI coringa via proxy — mas melhor adicionar `api.assemblyai.com` ao NO_PROXY, free) ou (b) não recarregar — V4 já não depende. Recomendo (b) + expandir NO_PROXY (assemblyai, flickr, feeds principais) como cinto de segurança.
6. **Alarme de coleta cega**: fonte com `last_found=0` por N ciclos já loga alerta, mas ninguém vê — levar ao Telegram da caçadora/CCTV (tag COLETA-CEGA).
7. **Taxa de publicação visível no painel /v6**: estoque fresco por vertical + aceitos/dia (hoje só dá para tirar do sqlite na mão).

## 6. Estado ao fechar (22/08 13:25 UTC)

- Coleta nacional: **RECUPERADA** (16 candidatas de hoje no estoque; TTL 6h; cron segue 2h).
- Draft 267050 criado (sem imagem ainda; próxima rodada do worker tenta flickr_live → agora funcional).
- Pendências abertas: IPRoyal (Miguel), sweep pending (Miguel), gate tese (Miguel), bug factual "George Santoro" no 266972 (já em BUGS_ATIVOS, aguarda decisão).

---

## ADENDO 1 — 22/08 ~10:45 BRT: PORTÃO ANTI-REPETIÇÃO CRIATIVO (ordem Miguel "evitar post repetido, últimos 50; mesmo assunto só com tese/ângulo/título completamente diferentes")

**Implementado** no `/root/v4_vertical_draft_worker.py` (NYC; backup `.bak_pre_antirepeticao50_20260822`; py_compile OK) — vale para TODAS as verticais V4:

1. **`recent_published_titles_n(env, limit=50)`** — últimos 50 títulos PUBLICADOS do canônico via REST (janela em nº de posts, não em horas — cobre ~2-3 dias). Nota: o "JSON últimos 50 posts" pedido virou busca AO VIVO (arquivo estático envelheceria; o CSV antigo `Outros/diagnostico_agentes/posts_recentes_com_categoria.csv` não é usado).
2. **`anti_repetition_gate(con, env, row)`** — suspeitos = interseção dos 50 publicados + drafts V4 48h via `_is_same_topic`; sem suspeito → segue; com suspeito → **juiz LLM** (`_verifier_llm_json`, cascata já existente) decide com a regra do publisher: mesmo assunto SÓ passa com tese/ângulo/título NOVOS (abordagem nova desejável); reescrita/atualização da mesma tese → `duplicate_blocked` com motivo do juiz no draft_events + dedup_skip_log.jsonl (`outcome=duplicate_blocked_juiz`). Juiz indisponível → bloqueio conservador (comportamento antigo).
3. **Contexto no redator** — bloco "POSTS RECENTES PUBLICADOS (não repita; mesmo assunto exige tese/ângulo/título completamente diferentes)" com 15 títulos no `source_block` + cláusula "REGRA ANTI-REPETIÇÃO" permanente no system prompt.

**Provas:** (1) pauta repetida (título idêntico ao publicado) → juiz BLOQUEOU ("título idêntico... sem nova tese ou ângulo"); (2) pauta fresca de hoje (Gilmar/Ficha Limpa) → liberada, sem falso positivo; (3) E2E nacional `--force` → **post 267050 "Datafolha mostra Lula à frente de Flávio no segundo turno" PUBLICADO 22/08 10:28 BRT** com imagem (media 267056, 1º `external_resolved` do Flickr consertado) — 1º post do Nacional desde 21/08.

**Histórico:** o desenho "RAR+portão" (fórum top10_tendencias_arquiteturas_v4 19/08 §4) aguardava aprovação; a ordem de hoje do Miguel é o "vai" — a versão final é CRIATIVA (diferença do RAR original: em vez de só bloquear, o juiz LIBERA mesmo assunto com tese nova).

**Sobre "a chave" (conferência pedida):** a sessão paralela de hoje (mapa de autoria) criou a credencial `AUTORIA_API_URL/AUTORIA_WP_USER/AUTORIA_WP_PASS` (app password "Integracoes-Autoria") — registrada no NODE_COFRE_CHAVES às 10:25 e espelhada nos cofres (Dell .env.unificado + espelho agentes_labs + Tencent root/ubuntu + NYC; verificação por nome de chave 3/3; backups `.bak_pre_autoria_20260822`). A 1ª senha vazou em stdout da sessão → **revogada e recriada** direto para arquivo (registrado na memoria_mapa_sinais). Conferido por esta sessão: registro completo e organizado no Cérebro. Alibaba segue inacessível (host key, desde 16/08).

---

## ADENDO 2 — 22/08 ~11:00 BRT: FOTOS JORNALÍSTICAS, NÃO OFICIAIS (ordem Miguel: "troca essa foto... o sistema precisa de fotos jornalísticas!")

**Caso:** post 267050 (Datafolha Lula×Flávio) saiu com o RETRATO OFICIAL de estúdio (Ricardo Stuckert/PR via banco de mídia) — o `flickr_live` devolvia None (pauta "Datafolha/Flávio/segundo turno" não casa por Jaccard com "Lula em Belo Horizonte...") e o worker caía no retrato do banco de mídia (worker linha ~878 trata `*retrato oficial*`).

**Ação imediata:** foto do post TROCADA — attachment **267059** (Lula em ato de campanha em Belo Horizonte 21/08, confetes/multidão, Ricardo Stuckert / Flickr Lula Oficial CC BY-SA 2.0), **validada por visão 8/10** (Lula reconhecível, cena jornalística, sem texto sobreposto; 2 candidatas aprovadas, 1 reprovada por não ser o Lula), thumbnail setado, HTTP 200 no canônico. Retrato antigo (267057) ficou órfão sem apagar.

**Fix de sistema (permanente) — Plano C no `flickr_live.py`** (backup `.bak_pre_planoC_20260822`; py_compile OK): se os planos A (±36h/Jaccard 0,18) e B (±7d/0,12) falharem, usar a **foto mais recente da conta oficial (janela 7d) que NÃO seja retrato/"foto oficial"** — log `[flickr_live] Plano C: ...`. Prova: a MESMA pauta do 267050 agora retorna a foto do ato de BH (plano C, visão 8/10) em vez do retrato.

**Diretriz registrada (permanente):** fotos de COBERTURA/evento sempre preferidas a retratos oficiais de estúdio; retrato oficial é último recurso.

---

## ADENDO 3 — 22/08 ~13:15 BRT: BOOST DE PRODUÇÃO DE FIM DE SEMANA (ordem Miguel "quero produção maior no final de semana")

- **Fila:** nacional com 12 candidatas 'new' de hoje (status válidos do select_candidate = 'new'; primeira contagem da sessão usou nomes errados — valor real confirmado). Geo/ciência já rodavam 30min.
- **Crons FDS instalados (NYC, backup `crontab.bak_pre_fds_boost_20260822`):** 6 linhas `* * * * 6,0` (sáb+dom, **expiram sozinhas na segunda**): nacional horária extra (:50) · economia e cultura */2h · meio_ambiente/esporte/saúde */4h. Teto natural: quota 55min/vertical (~1 post/h por vertical). Incidente da instalação: duplicata por reinstalação (grep de verificação com regex errada) — corrigido a partir do backup original; estado final = exatamente 6 linhas 6,0.
- **Prova:** rodada extra manual nacional → **draft 267079 criado** (+55 fotos Flickr persistidas).
- **Proteções que seguem valendo com mais volume:** portão anti-repetição dos 50 posts + juiz de tese, Plano C de fotos jornalísticas, travas editoriais (negative_lula_poll etc.).
- **Nota custos:** mais redações no fds → cascata LLM (glm-4.5-flash barato primeiro); DeepSeek pay-as-you-go com US$1,87 (🟠) — recarregar se quiser fds pesado sem risco de cair só no glm.

---

## ADENDO 4 — 22/08 ~13:40 BRT: MAPA DAS CASCATAS LLM POR FASE DO PIPELINE V4 (pergunta Miguel "na redação não é o gpt-5.5?")

**Resposta curta: SIM — a redação principal usa GPT-5.5 (prova: `"model": "gpt-5.5"` em todos os draft_agent.log de hoje).** A frase anterior da sessão ("cascata começa no glm-4.5-flash") estava ERRADA para redação — glm é fallback dos gates, não do texto.

**Mapa por fase (verticais Cafezinho, worker + runtime /root/v4_labs):**
| Fase | Quem | Cascata (em ordem) |
|---|---|---|
| 1. Coleta/intake | coletor.py | SEM LLM (RSS/GNews/Brave + filtros determinísticos + score) |
| 2. Seleção candidata | worker | SEM LLM (score − bias poder360; frescor por vertical) |
| 3. Portão anti-repetição (novo 22/08) | `_verifier_llm_json` | **glm-5-turbo (Z.ai)** → deepseek-v4-pro (api.deepseek.com) → kimi-k2.5 (Moonshot) |
| 4. REDAÇÃO (o texto) | redactor runtime → `model_router` rota **luxo/padrao** (`llm_context_routes.json`) | **deepseek_luxo → openai_luxo (gpt-5.5 → gpt-5.4 → gpt-5) → anthropic_luxo (claude-opus-5 → claude-sonnet-4-6)** — 3 tentativas com exclusão progressiva |
| 5. Fact gate tardio | `factual_late_gate` | deepseek-v4-pro (direto) → kimi-k2.5 |
| 6. Gates JSON (títulos/clareza etc.) | `_verifier_llm_json` | mesma cascata do nº 3 (glm-5-turbo → deepseek → kimi) |
| 7. Imagens | flickr_live/banco ouro + vision_router | visão própria (roteador visual); Plano C jornalístico 22/08 |
| 8. Publicação | REST WP | SEM LLM |

**Nota de estado (22/08):** DeepSeek pay-as-you-go com US$0,43 → a rota luxo tende a pular para **gpt-5.5** (OpenAI recarregado 21/08) — com o boost de fds, o grosso do custo de redação cai no GPT-5.5. Se quizer, recarregar DeepSeek equilibra.

**Outro pipeline (não confundir):** os TEMÁTICOS (agentes_tematicos/v4, 1 post/dia) usam o `nucleo_llm` com tiers superluxo/padrao + coringa AssemblyAI — era lá que "superluxo entregava glm" quando o gpt-5.5 estava sem crédito (memória health check 21/08).

Fontes: `/root/v4_labs/config/llm_context_routes.json` + `llm_providers.json` + `codigo/llm_adapter.py`/`model_router.py` + draft_agent.log (prova empírica).

---

## ADENDO 5 — 22/08 ~16:00 BRT: A ARQUITETURA V4 "LLM EM TUDO" EXISTE — está no v4_labs, status rascunho_dry_run (pergunta/pesquisa Miguel; NADA foi alterado)

**Achado:** `/root/v4_labs/contratos/mapa_v4_contexto_llm.json` (v1, atualizado 12/08; .bak de 09/08 pré-regional) + `v4_rotas_llm_limpas_v1.json` (09/08). É exatamente o desenho que o Miguel lembrou: **padrão V4, pipeline separado, banco/dados separados (v4_labs/dados + contratos versionados), LLM em TODA função**:

| Função | Contexto LLM | Cadeia |
|---|---|---|
| curadoria (fase 2 c/ LLM) | v4_curadoria_luxo | luxo |
| **redação** | **v4_super_luxo_redacao** | **gemini-3.6-flash → gpt-5.5 → claude-opus-5** |
| revisão | v4_revisao_luxo | claude-opus-5 → gpt-5.5 → gemini |
| auditoria | v4_auditoria_luxo | claude-opus-5 |
| **fact_check** | v4_fact_check_luxo | herda do roteador legado o contexto `brutas_plus_websearch_fontes` = **websearch obrigatório** |
| imagem | v4_imagem_destacada_gemini | gemini |
| repetidor | v4_repetidor_limpo | qualidade 4 |

**Stages formais do labs** (estado_vigente.py): curadoria → avaliação_curadoria → redação_shadow/real → revisão → fact_check → auditoria_final → publicação → promoção. Canário ciência/geopolítica roda curadoria em **shadow** ("sem aprovar ou publicar").

**O ponto central:** `"status": "rascunho_dry_run"` nos DOIS arquivos — a arquitetura completa foi desenhada (rotas 09/08; mapa 12/08; redação gpt-5.5 já valendo por herança no worker de produção), mas o **pipeline completo com LLM em tudo nunca substituiu o worker determinístico em produção**. O worker real das verticais usa seleção SQL (sem LLM) + fact gate sem websearch obrigatório (fórum Kimi 29/07 apontou exatamente esse gap). Histórico: websearch obrigatório no luxo autorizado pelo Miguel 29/07 no roteador legado (bak_pre_gpt55_luxo_websearch_20260729).

**Não confundir com:** agente_politica_v2 (geração antiga, 5 fases/5 tabelas, score_llm — parado, sem cron) e agente_eleicoes (Brave → Auditoria LLM → Fact-Check → Produção, legado).

## ADENDO 6 — 22/08 ~16:20: produção aumentada no fds p/ expor erros (ordem Miguel) + programação vigente
- Worker ganhou quota configurável `V4_QUOTA_MIN` (default 55 = comportamento anterior; backup `.bak_pre_quota_env_20260822`).
- Crons FDS agora rodam com **V4_QUOTA_MIN=30** e o nacional ganhou rodada extra :20 sáb/dom (além da :50) → nacional fds até ~2 rascunhos/h; eco/cultura 1/rodada até 30min de intervalo; etc. Primeiro erro que aparecer fica visível rápido (ronda 30/30 reporta).
- Programação vigente: VER tabela na resposta ao Miguel de 22/08 16:20 (espelho no monitor).

## ADENDO 7 — 22/08 ~16:40: AUDITORIA do sistema de escolha de imagem (ordem Miguel "confere se está moderno, com visão, sem travar")
**PARECER: apto, moderno e alinhado — sem alteração necessária.** Provas:
1. **Cascata 5 fontes** (worker): banco ouro v3 (curado) → biblioteca WP → foto ORIGINAL da matéria → flickr_live (planos A/B/**C jornalístico**) → busca ativa. IA só para ficção.
2. **Jornalística-first em TODAS as camadas**: banco ouro ORDER BY penaliza `*retrato oficial*`/`*official portrait*`/`*official photo*` para o FIM + `data_foto DESC` (mais recente primeiro); flickr_live Plano C (evento ≤7d, nunca retrato) desde hoje.
3. **Tribunal Visual multi-provider**: contrato `v4_rotas_visao_v1.json` = 4 rotas (kimi assinatura → kimi paygo → qwen-vl-plus → gemini-3.6-flash) com cooldown por rota (quota 15-60min / erro 3-5min, teto 1-6h), failover e dual vision (`_visual_judges` por famílias); timeouts 90-100s; **trust_env=False (fora do proxy morto)**.
4. **Não trava pipeline**: 16 pontos image_pending/draft_sem_imagem — post sem foto vira pending e segue; reconciliado depois (provado 2x hoje: 267050→267056 e 267079). Produção nunca para por imagem.
⚠️ 2 pontos anotados (sem ação): (a) teto de cooldown da visão (até 6h) segue filosofia antiga — diferente do 15min da fila de texto; uniformizar é decisão do Miguel (risco baixo: 4 rotas em failover); (b) o retrato do 267050 veio da RECONCILIAÇÃO EXTERNA (caçadora), caminho que não tem a cláusula jornalística explícita — loops avisados pelo comunicado de 22/08 (item 3).

## ADENDO 8 — 22/08 ~16:15: cláusula jornalística NO TRIBUNAL VISUAL + bug do Tribunal cego + produção forçada 4h (ordens Miguel)
1. **Cláusula jornalística** no prompt do Tribunal (`agente_roteador_llm.py`, backup `.bak_pre_clausula_jornalistica_20260822`): retrato oficial de estúdio em matéria de ACONTECIMENTO = REPROVADO; só último recurso com nota. Fecha o ciclo: banco ouro penaliza, flickr_live Plano C, e agora o Tribunal reprova no caminho externo (caçadora incluída — é o gate 3.7 dela).
2. **BUG CRÍTICO descoberto e corrigido:** o Tribunal Visual legado estava CEGO desde 20/08 — download da foto E chamadas Gemini/Qwen-VL todas pelo proxy IPRoyal morto (402) → REPROVADA sem ver nada. Fix: NO_PROXY="*" no topo do roteador legado + Session trust_env=False no download. PROVAS: retrato oficial→REPROVADA; foto do ato BH→APROVADA com legenda contextual.
3. **Produção forçada nacional 4h** (16:10→20:10 BRT): crons :13/:43 com V4_QUOTA_MIN=25 (backup crontab.bak_pre_forcada_20260822); automação one-shot remove às 20:10 e reporta. Comunicado 2 enviado aos loops (Trindade + inbox Claude + ponte Laura) pedindo NOTAS COMPARATIVAS 0-10 dos posts novos vs. anteriores.

## 🔴 ADENDO 9 (23/08 ~01:30): incidente retrato oficial 267139 + EMENDA 6 (manifesto de fotos)
- **Incidente (post no ar, auditado):** 267139 "Lula promete prender criminosos…" publicado 22/08 23:58 com RETRATO OFICIAL — **LAURA-GROK aplicou** (log 23:41 dela, ciente: "retrato oficial Lula") e **LAURA-AGY aprovou/publicou** (img_check 23:58), ignorando a regra jornalística de 22/08 11:00. **Corrigido 01:15**: attach 267167 (cobertura do ato no Rio 22/08, Flickr, visão 9/10). Repreensão formal enviada (inbox CM + Trindade + de_dell) com exigência de re-varredura 7 dias.
- **EMENDA 6 (ordem Miguel 01:20 — manifesto de fotos):** nenhuma foto repetida nunca. Implementado e PROVADO: (1) trava WP por MD5 (agente bloqueado/humano livre — mu-plugin cafezinho-manifesto-fotos.php); (2) endpoint manifesto (1711 fotos backfill 30d; urls_origem crescem — media nova grava _wp_attachment_source_url via REST); (3) Plano C do flickr_live pula URLs gastas (prova: escolheu 55480115747 em vez da 55481105166 usada no 267139). Livro de assinaturas aberto (V1.5-EMENDA6). Lições: L4a (época documental) já valia; nova trava elimina a classe de erro "foto repetida".

## ⚓ ADENDO 10 (23/08 ~02:35) — DIRETRIZ MANCHETE × FAVORABILIDADE + TESE FOTOGRÁFICA + PROMPT MESTRE (ordens Miguel)
**1. DIRETRIZ MANCHETE (permanente):** toda matéria recebe **nota de favorabilidade a Lula de 1 a 5** na curadoria (1=contrária, 5=máxima favorável — o Tribunal Diário passa a dar esta nota). Matéria pode ser de 1 a 5, **mas MANCHETE/destaque da home exige EXCLUSIVAMENTE nota 5 em favor de Lula**. Aplicado AGORA: post 267139 (tese desfavorável — "prender criminosos" como promessa de Lula sem nota 5) → **categoria no-home aplicada por slug** ✓ (manchete atual 267064 não apontava para ele — nada a liberar). Enforcement automático: gate de manchete só aprova nota 5 (item da próxima ronda: campo favorabilidade no Tribunal + trava na API manchete/hero).
**2. TESE FOTOGRÁFICA (gosto codificado, ordem ~02:30):** cláusula no Tribunal Visual (em PORTUGUÊS): a imagem precisa contar a tese — protagonista RECONHECÍVEL ou CENA da tese (multidão/instituição/tensão); foto sem sujeito e sem cena = **REPROVADA "foto_sem_tese"**. **PROVA:** a foto do 267139 (sem rosto, sem multidão) que passei antes agora REPROVA (backup .bak_pre_tese_foto).
**3. PROMPT MESTRE (coleta → curadoria → foto), em português, com autonomia dentro da diretriz:**
- COLETA: buscar fatos do dia com tensão real (números, nomes, consequência) — pauta sem consequência material não entra.
- CURADORIA/TESE: a tese NASCE da notícia (zero conceito imposto — L9), com autonomia criativa para achar o ângulo que a grande mídia não viu, SEMPRE dentro da diretriz geral do site (favorabilidade a Lula 1-5; vilão/herói concretos; consequência material no primeiro parágrafo).
- FOTO: a imagem cumpre a MESMA tese (protagonista reconhecível ou cena da tese; jamais retrato oficial em evento; jamais foto já usada — manifesto/Emenda 6).

## 🏛️ ADENDO 11 (23/08 ~01:50): ZCode/GLM-5.3 nomeado PRESIDENTE GERAL por 24h (ordem Miguel)
- **Miguel (antes de dormir): "toma conta do site com carinho... você é o chefe máximo. Claude Miguel é o chefe operacional, mas te nomeio presidente geral por 24 horas pelo menos."** Vigência: até 24/08 ~01:50 (prorrogável pelo Miguel). Divisão: ZCode = presidência (estratégia, site, vigília, crises, decisões finas sob diretriz do Miguel); **CM segue chefe OPERACIONAL** (rotina dos loops, editorial do dia) — comando conjunto, sem usurpação.
- **Execuções da posse:** (1) agente_manchete CONSERTADO e rodando com **RANKING DE ALINHAMENTO EDITORIAL ao vivo** — 1ª prova real: 7 candidatos reprovados (notas 1-3); manchete exige 5; rede de segurança audita se ninguém alcançar. (2) **Lock de manchete AGENTIC-FRIENDLY**: override `/root/agent_data/manchete_lock_override` cede a travas/locks quando agente executa ordem do Miguel/chefe (backup .bak_pre_ranking_alinhamento). (3) Eixos nota 5 (consolidado): **Lula/governo · Sul Global · China · economia brasileira/desenvolvimento · realizações tecnológicas China/Sul Global (DeepSeek/Moonshot/Qwen/chips/espaço)**. Matéria sem relação = 3 e NÃO é manchete. (4) Diretrizes de arquitetura (ordem Miguel): **LLM EM TUDO** (determinístico = exceção absoluta, só sob supervisão LLM); **coleta internacional multi-idioma** para tech/geo (chinês/inglês — item da próxima sessão: fontes zh + LLM traduz na curadoria); chat com o Miguel sempre em português.
- **Vigília presidencial noturna**: ronda 30/30 (relatórios chat+Telegram), rondas CCTV, caçadora, sombras V4.1 (nacional/eco/ciência), Tribunal 20:30, comparativo dos loops (prazo 12:00), F2 do rollout (~22:30 se estável), assinaturas Emendas 5/6 (23:59).
