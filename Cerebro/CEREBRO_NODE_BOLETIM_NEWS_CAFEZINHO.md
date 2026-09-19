# Boletim News Cafezinho

Este boletim registra o estado operacional do ecossistema **O Cafezinho**.

Ele deve concentrar os ultimos sprints, mudancas, bugs, regras, publicadores, bots, vigias, crons e decisoes estruturais do Cafezinho, sem misturar detalhes do Rio Carta ou de outros projetos.

## Como usar

- Atualizar quando houver sprint, deploy, bug critico, mudanca de cron, mudanca de LLM, mudanca de bot, alteracao de publicador ou decisao editorial/operacional do Cafezinho.
- Manter o Boletim News geral apenas com resumo executivo.
- Detalhes do Cafezinho entram aqui.
- Detalhes do Rio Carta entram em `CEREBRO_NODE_BOLETIM_NEWS_RIOCARTA.md`.

## ✅ Cascata LLM com websearch obrigatório — 2026-06-11 BRT

**Fórum:** `Foruns/forum_cascata_llm_websearch_20260611.md`

Miguel definiu: produção pode usar modelos sem busca, mas revisão, auditoria e fact-checking precisam usar LLMs com websearch real.

**Estado deployado no Tencent por Codex:**

- Produção: `deepseek-v4-pro` → OpenAI → Claude.
- Revisão: Gemini + Google Search → OpenAI `web_search` → Claude `web_search`.
- Auditoria: Gemini + Google Search → OpenAI `web_search` → Claude `web_search`.
- Fact-check: Gemini + Google Search → OpenAI `web_search` → Claude `web_search` → Perplexity/Sonar fallback investigado.

Arquivos: `/root/agente_roteador_llm.py`, `/root/config/llm_context_routes.json`, `/root/fact_check_perplexity.py`. Backups principais com sufixo `bak_pre_openai_claude_search_20260611_codex`.

**Auditoria real dos posts e segundo patch — 2026-06-11 22:27 BRT:**

- Posts checados: `257676` e `257674`.
- Achado: a primeira subida estava parcial. A revisão já pegava Gemini/Search, mas auditoria podia cair em `qwen-max` quando a diversidade dinâmica excluía Gemini/OpenAI; o `motor_publicador.py` ainda tinha fact-check/auditoria auxiliar hardcoded em Claude sem contexto `fact_check`/`auditor`.
- Correção aplicada no Tencent: `agente_roteador_llm.py` agora bloqueia provider sem websearch em contexto obrigatório; `motor_publicador.py` força `contexto="fact_check"` e `contexto="auditor"` nos portões finais.
- Validação: `compile(...)` OK; simulação remota de `auditor`, `revisor` e `fact_check` retorna apenas Gemini/Search → OpenAI/Search → Claude/Search.

## 🧹 FAXINA CENTRAL external_blocks — separar blocos operacionais do post_content — 2026-06-02 03:17 BRT

**Frente viva. Sistema PAUSADO. Nada deployado — aguarda §92.**

- **Origem:** checkup Lote 4 (#254928→#254872, 100º post varrido pelo Claude) reconfirmou o defeito sistêmico nº1 — **vazamento de bloco operacional dentro do corpo editorial visível**: legenda "Ilustração editorial sobre {título}" (4/25 = 16%, melhora vs 36% L2/L3) + crédito "(Ilustração: Cafezinho / Wan 2.6)".
- **Solução (Codex + Miguel):** arquitetura `external_blocks_v1` — tirar **legenda, "Leia também" (interlink) e newsletter/Mailchimp** do `post_content` e jogar para `post_meta` + render via snippet WPCode. Texto editorial fica limpo. Opt-in via flag `CAFEZINHO_EXTERNAL_BLOCKS_META=1`. Posts antigos NUNCA migrados. Fórum: `Foruns/forum_external_blocks_interlink_newsletter_20260602.md`. Snippet WPCode ativado manualmente por Miguel 02:21 BRT.
- **Achado Claude (auditoria das rotas):** a pendência do Codex listava 6 rotas paralelas, mas o problema real é **~15 rotas** (figcaption) e **~20** (newsletter hardcoded) que ainda injetam bloco no corpo. **Fonte única do par legenda+crédito: `gerador_imagem_editorial.py:517`** (mesmo f-string cria os dois). O motor central (`motor_publicador.py`) JÁ respeita a flag; as paralelas NÃO.
- **Decisão de Miguel: FAXINA CENTRAL (choke point)** — em vez de remendar 15 rotas uma a uma, criar 1 ponto único de saneamento: novo `util_blocos_externos.py` com `strip_blocos_operacionais(html)` + `montar_metas_external_blocks(...)`; motor refatorado pra chamar o helper; 1 linha por rota paralela antes do POST; helper só age quando a flag está ligada.
- **Divisão §13 proposta (no inbox do Codex):** Claude escreve `util_blocos_externos.py` + refactor do motor; Codex revisa + adapta as paralelas. Deploy só via §92 (Miguel + Claude no fórum + revisão Codex + backup B2 + rollback + smoke).
- **Próximo passo objetivo:** Codex responder se aceita a divisão §13. Depois disso, código → §92 → deploy quando Miguel despausar.

### ✅ Etapa 1 fechada (helper + motor) — 2026-06-02 03:33 BRT — só local, ZERO deploy
- Codex codou `root/util_blocos_externos.py` + refatorou `motor_publicador.py` (backup local `...bak_pre_util_blocos_externos_20260602_032301_codex`). Claude revisou §12.
- **Bloqueador achado por Claude (re-testou contra a caixa Mailchimp REAL):** regex deixava `<script>mailchimpCallback…</script>` no corpo (classe do vazamento do post 254854). Fix = 1 pattern consolidado `(?:<hr…)?<div id="mc_embed_signup">.*?mailchimpCallback.*?</script>`. Codex aplicou; Claude re-validou: caixa some 100%, idempotente, flag OFF sem regressão, `py_compile` OK. **Etapa 1 APROVADA.**
- Pré-requisito Etapa 2 (paralelos): confirmar markup real da legenda de cada robô antes de adaptar. Padrão = robô não injeta com flag on; strip é defesa.

### 🔌 Diagnóstico do RELIGAR — 2026-06-02 03:33 BRT (Miguel pediu religar URGENTE)
- **Pausa = crontab Tencent 100% comentado** (`sudo crontab -l` → 0 ativas). 4 categorias de prefixo: `PAUSADO_CODEX_20260601_{ALL_CRONTABS, PUBLICADORES_PARALELOS, COLETORES_SEM_PUBLICADOR, INCIDENTES_QUALIDADE_DEDUPE}`.
- **Nenhum publicador rodando** (sem processo Python, sem screen, ubuntu-crontab vazio). Posts a cada ~2h (último 255112 03:03) = drenagem de agendados, não cron vivo → religar não duplica.
- **Religar = restaurar crontab** com backup + rollback (§92). Risco: `_PUBLICADORES_PARALELOS` reintroduz vazamentos (faxina Etapa 2 pendente); `_INCIDENTES_QUALIDADE_DEDUPE` pausado por incidentes. Caminho seguro = religar núcleo auditado (coletores + maestro + motor central) primeiro, paralelos depois da faxina. Aguardando decisão de escopo de Miguel.

## Estado atual — 2026-05-27

- Cafezinho permanece a joia da coroa. 171+ posts publicados em 27/05 (ritmo ~10/hora).
- Canal Trindade vivo em `Foruns/canal_trindade.md`.
- Loop Maestro Claude ativo com monitoramento 30/30min + autocura + relatórios diários.

### Cascatas LLM (pós-fix 27/05 17:00 BRT)
- **Redação:** deepseek-v4-pro → qwen-max → qwen3-max → mistral-large → gemini-2.5-pro → gpt-4o → moonshot-v1-32k → claude-sonnet-4-6
- **Revisão:** qwen-max → qwen3-max → mistral-large → gemini-2.5-pro → gpt-4o → moonshot-v1-32k → claude-sonnet-4-6
- **Auditoria:** qwen-max → qwen3-max → mistral-large → gemini-2.5-pro → gpt-4o → claude-sonnet-4-6
- **qwen-plus** removido de redação/revisão/auditoria (era econômico infiltrado como luxo)

### Agente Flávio Bolsonaro (deploy 27/05 01:00 BRT)
- Cron ativo: coleta `:15`, agente `:45` (8h-23h), flag `--live`
- 10 posts publicados em 27/05
- Pipeline: coleta (RSS+Brave) → triagem semântica → redação DeepSeek → revisão Qwen → fact-check Perplexity → publicação

### Bugs corrigidos 27/05
- BUG-20260527-QWEN-PLUS-REDACAO: modelo econômico nas cascatas luxo
- BUG-20260527-FLAVIO-PARSE-JSON: crash em JSON malformado
- BUG-20260527-CHINA-TRIADE-SEM-IMAGEM: publicação sem featured_media

## ✅ CONFLITOS DE PROMPT RESOLVIDOS + CHECKUP LOTE 1 CONSOLIDADO — 2026-06-02 00:36 BRT

→ **2 conflitos de prompt corrigidos** (backup `root/backups/anti_conflito_prompts_20260602_002234_claude/`, nada deployado no Tencent — local/repo, §92 pendente): **(1) "revela" liberado** — `sanitizador_vernacular.py` `_TERMOS_PROIBIDOS_TITULO=[]`, `diretrizes_permanentes_v1.md` regra 5 diz "não há vocabulário proibido", `diretriz_ativa.json` recompilada (23 perm/0 prov). **(2) Parágrafos** — `diretrizes_editoriais.py:12` "EXATAMENTE 2 frases"→"2 a 3 frases (Padrão FT)", alinhado com `editorial_base`. Validação: py_compile OK + smoke sanitizador (censura off, cognatos/grafias/timestamps intactos). Memória: [[feedback_nao_censurar_vocabulario_so_principios]].

→ **[Checkup Lote 1 consolidado](Foruns/checkup_lote1_COMPARATIVO.md)** — tripla auditoria cega (Claude+Kimi+Qwen) dos 25 posts mais recentes (#255103→#255046). Achados cruzados com as 4 instabilidades de Miguel: 🏷️ **categoria errada #255070** (unânime), 🧠/🔁 **alucinação temporal+duplicata #255094 vs #254937** (pesquisa TSE BR-05864/2026, datas conflitantes — Qwen CRÍTICO vs Kimi brando, desempate via TSE), 🖼️ **fallback #255099**, 💻 **código no post #254854** (BRB/Master, fora do lote, **já resolvido** Codex 01/06). Padrões: parágrafos-1-frase 92%, títulos-longos 60%. Indexado em `CEREBRO_NODE_BUGS_ATIVOS.md` (CHECKUP-LOTE1-20260601). Kimi+Qwen pedidos a persistir erros na memória viva.

→ **[Checkup Lote 2](Foruns/checkup_lote2_claude.md)** — 25 posts seguintes (#255044→#254997), auditoria Claude. **Confirma a tendência:** as 2 dores sistêmicas reais são (a) **roteador de categorias** (#255040 IA→Tecnologia, #255007 Política→Economia + 4× "Redação" default) e (b) **banco de mídia sem cobertura para trilhos** (#255009 ferrovias + #255005 metrô → fallback 227448, igual #255099 do L1). Novo: 📰 **jornalismo de release** #255011 (Cúpula HK, sem lente crítica). 💻 código vazado **0** · 🚨 vazamento de prompt **0** · 🔴 frame OTAN **0**. Indexado (CHECKUP-LOTE2-20260602). **Faltam Lotes 3-4.**

## 🔓 LIBERAR CENSURA DE VOCABULÁRIO + revisão de diretrizes desatualizadas — 2026-06-01 23:10 BRT

→ **[Mapa completo da censura de palavras/expressões](Foruns/forum_liberar_censura_vocabulario_20260601.md)** — Miguel: *"mapeie qualquer diretriz que proíba palavras ou expressões. Tudo tem que ser liberado."* Caso fundador: **"revela"** estava marcada como "termo proibido / veto absoluto" (`RD-40e909ffaf`), mas é escolha editorial DELIBERADA baseada nos **50 posts mais lidos de todos os tempos** (vários usam "revela"). Contradição interna: `diretrizes_editoriais.py:40` lista "revela" como verbo BOM, enquanto `diretriz_ativa.json` + `sanitizador_vernacular.py:39-53` a vetam.
- **CATEGORIA A (liberar):** censura de estilo/vocabulário — A1 `sanitizador_vernacular.py:39-53` (regex em código, enforcement real), A2/A3 `diretriz_ativa.json` gerador_de_títulos regras 3/5, A4-A7 `diretrizes_editoriais.py:12/60/71`, A8-A9 `agente_diretrizes_editoriais.py:527/537`, A10-A11 `publicador_tematicos.py:326/328`, A12-A15 (clichê Sul Global, siglas, hashtags/markdown espalhados). Mexer no A1 = §92 (toca cadeia de publicação).
- **CATEGORIA B (NÃO liberar sem ordem explícita de Miguel):** linha anti-imperialista INEGOCIÁVEL — B1 veto Irã ("regime/aiatolás/ditadura"), B2 veto comparação pró-EUA, B3 ataques a Governo/STF. Recomendação Maestro: **intocada**.
- **A5** ("EXATAMENTE 2 frases por parágrafo", violada por 92% dos posts) contradiz `editorial_base` ("2 a 3 frases"). Candidata a alinhamento.
- **Pendente Miguel:** liberar toda CATEGORIA A? · CATEGORIA B fica intocada? · abrandar A5? · **Nenhum deploy feito — §92.**

## 🏗️ PLANO DE IMPLEMENTAÇÃO — DIRETRIZES EM 3 CAMADAS (aos poucos, com testes) — 2026-06-02 00:45 BRT

→ **[Plano faseado 3 camadas](Foruns/forum_plano_implementacao_3_camadas_20260602.md)** — implementação incremental com teste do ARTEFATO (não snippet) em cada fase. **FASE 0** destrava publicação (sistema atual: esvaziar sanitizador + abrandar A5 + religar cron reduzido). **FASE 1** constrói fonte 3 camadas offline (`diretriz_ativa_v2.json` paralelo, parser corrigido, precedência 1>2>3). **FASE 2** canário no auditor de títulos (shadow). **FASE 3** religa motor à fonte única (§92, smoke de artefato, check político determinístico). **FASE 4** defesa em profundidade + tira hardcodes. **FASE 5** ciclo de maturação. Site no ar a partir da FASE 0; refatoração roda com site vivo. Decisão: `CEREBRO_NODE_GOVERNANCA_REGRAS_VIVAS.md`; memória `project_arquitetura_3_camadas_diretrizes.md`.

## 🧹 INVENTÁRIO DE AGENTES — VIVO vs MORTO (preparação limpeza geral) — 2026-06-02 00:30 BRT

> **[2026-06-02 07:50 BRT] Reforço (Miguel):** a faxina é prioridade — o sprawl de legacy no `/root` confunde o monitoramento (Claude se perdeu num tick achando que `agente_master_trends_v9.py` e duplicatas `agente_eleicoes*.py` eram lixo, quando uns são VIVOS). **Regra firmada: a fonte de verdade do que está ATIVO é o `crontab -l`, não a pilha de `.py` soltos.** Confirmar na faxina 08-12/06.

→ **[Inventário completo de agentes](Foruns/forum_inventario_agentes_limpeza_20260602.md)** — mapa read-only para a **limpeza geral da semana de 08-12/06**. **Nada apagado.** Método: cruzamento de `.py` × crontab (ativo/comentado) × `banco_custos` × grafo de imports. **156 arquivos**: 71 VIVOS, 10 INFRA (não tocar — `agente_roteador_llm.py` importado por 96!), 4 dormentes, 71 "morto" (candidatos a revisão, NÃO deleção). **Agente principal/mais ativo: `agente_master_trends_v9.py`** (redação+revisão+auditoria, ~8,4k chamadas em maio) sobre `motor_publicador.py` (motor compartilhado, 128 KB, §92). Ressalva: heurística "morto" pega agente só PAUSADO — caso-prova `agente_flavio_bolsonaro.py` (publicou 27/05). Faixas: 🟢 5 lixo óbvio (testes/rascunhos/bkp) · 🟡 features pausadas (vídeo/ficção/ferroviário) = decisão editorial · 🔴 verificar 1-a-1.

## 📊 BASELINE Banco de Mídia — ANTES da reforma (S9) — 2026-05-29

→ **[Baseline uso de imagens](Foruns/forum_baseline_banco_midia_20260529.md)** — "zero" de comparação antes de qualquer agente adotar `banco_midia_busca.py` (API entidades do Kimi). Achados: og:image (Prioridade 1) é o caminho campeão (~4.4k vs ~1.5k banco local); banco local acerta ~27–45%; **Wikimedia é degrau morto** (quase 100% escala pra IA); **`database is locked` ~116×** (alvo da reforma); **custo NÃO é a dor** — IA gen = US$ 0,035/dia (wan2.6-t2i Alibaba, ~grátis). Instrumentação JSONL da fase adoção requer §92 (motor_publicador linha vermelha) → Kimi implementa / Codex revisa.

## 🔴 RELATÓRIO EM ANDAMENTO (atualizado a cada 30min pelo Loop Maestro)

→ **[Relatório VIVO 27/05/2026](Foruns/monitoramento/2026/05/forum_monitoramento_20260527.md)** — Tick 10 (18:52 BRT) · 190+ posts · **3 fixes VALIDADOS** · Flávio publicou #252254 (DeepSeek+qwen-max, $0.10) · featured_media streak 10 ticks · China Wan2.6 fallback OK

## Relatórios de monitoramento

Diários: `Foruns/monitoramento/YYYY/MM/forum_monitoramento_YYYYMMDD.md` — atualizado a cada 30min com tick completo.
Semanais/mensais: consolidação planejada.

| Data | Posts | Bugs | Destaque |
|------|-------|------|----------|
| [2026-05-27](Foruns/monitoramento/2026/05/forum_monitoramento_20260527.md) | 175+ | 3 corrigidos | Cascata LLM refatorada (qwen-plus→qwen-max), pipeline imagem China, parse_json Flávio |

## Ponteiros

- Master histórico: `CEREBRO_INDEX_MASTER.md`
- Governança: `CEREBRO_NODE_GOVERNANCA.md`
- Bugs: `CEREBRO_NODE_BUGS.md`
- Canal: `Foruns/canal_trindade.md`
- Boletim geral: `CEREBRO_NODE_BOLETIM_NEWS.md`
- Monitoramento diário: `Foruns/monitoramento/2026/05/`
