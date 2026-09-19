# 🔑 CÉREBRO CAMADA 2: Nodo de Chaves, Inteligência e LLMs

---

## 📅 ATUALIZAÇÃO 2026-08-30 ~08:40 — CONFIG: DeepSeek Flash + Vision plugados no ZCode Miguel ("JPSC" = DeepSeek)

**Fórum:** [`Foruns/forum_config_jpsc_deepseek_flash_vision_zcode_20260830.md`](./Foruns/forum_config_jpsc_deepseek_flash_vision_zcode_20260830.md) · **Memória:** [`Memorias/memoria_config_jpsc_deepseek_flash_vision_zcode_20260830.md`](./Memorias/memoria_config_jpsc_deepseek_flash_vision_zcode_20260830.md)

**Resumo:** Miguel pediu "JPSC Flash e JPSC Vision" no ZCode Miguel. Sigla não batia com nada (varridos Cérebro, cofres Dell/NYC, config e catálogo embutido) → identificada como **transcrição de voz de "DeepSeek"**. Configurados no `~/.zcode/v2/config.json` (backup datado): `deepseek-v4-flash` no provider anthropic existente + provider novo "DeepSeek Vision" (openai-compatible) com `deepseek-v4-flash-vision-exp` (texto+imagem). Ambos **testados na API real** (HTTP 200). `deepseek-v4-pro` intocado; nenhuma chave nova criada (reusada `DEEPSEEK_API_KEY`). Anotar: **"JPSC" = DeepSeek**.

---

## 📅 ATUALIZAÇÃO 2026-08-25 ~13:00 — DECISÃO: DeepSeek V4 Pro = modelo principal do ZCode (ordem do Miguel)

**Fórum:** [`Foruns/forum_estrategia_modelos_zcode_decisao_20260825.md`](./Foruns/forum_estrategia_modelos_zcode_decisao_20260825.md) · **Memória:** [`Memorias/memoria_estrategia_modelos_zcode_decisao_20260825.md`](./Memorias/memoria_estrategia_modelos_zcode_decisao_20260825.md)

**Resumo:** Miguel decidiu apostar no DeepSeek por API como modelo principal do ZCode (sem janela de 5h, ~US$ 0,06/turno pesado; já usado em sites/Moka) e **não renovar a assinatura Kimi** (janela esgotava; 12 esgotamentos desde 20/07). Infra pronta na mesma sessão: provider "OpenAI (GPT-5.6 Sol)" plugado no ZCode + chave `ZCODE_OPENAI` espelhada (sha8 `8035a022`) + preços Kimi/GPT-5.6 documentados. Pendências do Miguel: recarga DeepSeek, cancelar renovação Kimi; opcionais: DeepSeek na cadeia do `llm_fallback.py` e manter Qwen Lite (US$ 6) como reserva.

---

## 📅 ATUALIZAÇÃO 2026-08-23 ~16:10 — PESQUISA: DeepSeek Harness (DSH/`dsh`) × ZCode — vale instalar?

**Fórum:** [`Foruns/forum_deepseek_harness_dsh_pesquisa_20260823.md`](./Foruns/forum_deepseek_harness_dsh_pesquisa_20260823.md) · **Memória:** [`Memorias/memoria_deepseek_harness_dsh_20260823.md`](./Memorias/memoria_deepseek_harness_dsh_20260823.md)

**Resumo:** pedido do Miguel. DSH = harness de agente open-source (MIT, developer preview, ~187k stars) — **mesma categoria do ZCode**, não é modelo. Multi-provedor (DeepSeek/OpenAI/Anthropic/Kimi/Qwen/custom), Web UI local :3080 + CLI + SDK Python, subagentes, arquitetura "tudo é plugin". Dell JÁ atende o pré-requisito (Node v22.22.2; pnpm ausente, só p/ plugins). **Parecer: laboratório sim (custo ~zero + recarga ~US$ 2), substituto do ZCode não** (preview instável, docs fracas, e a conta DeepSeek `fe52ae94` seguia 402 em 21/08 — recarregar antes de testar). Aguarda decisão do Miguel.

---

## 📅 ATUALIZAÇÃO 2026-08-21 ~14:15 — HEALTH CHECK CADEIA V4 (nucleo_llm): 4 de 7 providers mortos por crédito

**Fórum:** [`Foruns/forum_coringa_assemblyai_cascata_llm_20260816.md`](./Foruns/forum_coringa_assemblyai_cascata_llm_20260816.md) (Adendo 1)

Smoke real 1×/provider executado do Dell (`/tmp/health_llm_v4.py`, cofre local, chaves presentes em todos):

| Provider | Modelo | Estado 21/08 |
|---|---|---|
| glm (Zhipu) | glm-4.5-flash | 🟢 OK (1,9s) |
| qwen | qwen-plus | 🟢 OK (3,2s) |
| assemblyai (coringa) | claude-haiku-4-5 | 🟢 OK (2,0s) — autopay segurando |
| deepseek | deepseek-chat | 🔴 402 saldo (conta `fe52ae94` — ver vigília: US$ −1,48) |
| kimi (moonshot `KIMI_API_KEY`) | moonshot-v1-128k | 🔴 429 conta suspensa por saldo (desde 16/08) |
| openai | gpt-4o-mini | 🔴 429 sem créditos |
| openai_gpt55 (tier superluxo) | gpt-5.5 | 🔴 429 sem créditos |

**Impacto:** V4 não para (cascata cai no glm), mas DeepSeek-líder e o flanco OpenAI inteiros mortos; tier `superluxo` entrega glm-4.5-flash na prática. Pendente decisão de recarga do Miguel.

---

## 📅 ATUALIZAÇÃO 2026-08-09 ~11:20 — FREE QUOTA ALIBABA: cota `qwen-vl-plus` esgotou; rotação para modelos com cota até 09-15

**Fórum:** [`Foruns/forum_rotacao_free_quota_alibaba_20260809.md`](./Foruns/forum_rotacao_free_quota_alibaba_20260809.md) · **Memória:** [`Memorias/memoria_rotacao_free_quota_alibaba_20260809.md`](./Memorias/memoria_rotacao_free_quota_alibaba_20260809.md)

**Resumo:** e-mail da Alibaba (conta **aiatolahnews@gmail.com**) avisou que a free quota de `qwen-vl-plus` esgotou. Descoberta: a chave canônica do pipeline (`85ecbfc0`, workspace `ws-x4x2zxwucryw1pr6`) consome JUSTA essa cota (padrão de consumo bate exato: vl-plus esgotado, vl-max 95%, qwen3-max 35%, qwen-max 15%). A conta tem **87 modelos com 1M tokens grátis cada até 2026-09-15**. 19 smokes ao vivo: visão migra p/ `qwen3-vl-32b-thinking` + `qwen3-vl-235b-a22b-thinking` (grátis); cascata de texto já debita da cota sozinha. **Bug achado:** alias `qwen-vl-max-latest` dá 403 neste workspace (fallback do tribunal estava morto) — usar `qwen-vl-max`. Ratings locais atualizados (backup `.bak_pre_free_quota_qwen_20260809`); **deploy NYC/Tencent pendente de coordenação (mutirão ativo) + OK do Miguel**.

---

## 📅 ATUALIZAÇÃO 2026-08-07 ~18:15 — Política de roteamento Kimi: `k3-256k` como default econômico (top-up bridge)

**Fórum:** [`Foruns/forum_k3_256k_modelo_economico_kimi_topup_20260807.md`](./Foruns/forum_k3_256k_modelo_economico_kimi_topup_20260807.md) · **Memória:** [`Memorias/memoria_k3_256k_modelo_economico_kimi_topup_20260807.md`](./Memorias/memoria_k3_256k_modelo_economico_kimi_topup_20260807.md)

**Política de roteamento (ficar valendo):** para trabalho de código / gestão do ecossistema, **preferir `k3-256k`** sobre `k3` (1M). A doc do Kimi é explícita — *"Within 256k context, it delivers the same results"* — é o mesmo K3 (2.8T params), mesma inteligência, só janela menor (256k vs 1M). Consume **~metade da quota** por chamada → dobra o tempo útil do mesmo crédito. Reservar `k3` (1M) apenas para ingerir codebases inteiras em uma única chamada (caso raro no padrão de uso do Miguel).

**IDs de modelo válidos no seletor/API Kimi:** `k3` (1M) · `k3-256k` (256k, **default econômico**) · `kimi-for-coding` (K2.7 Code) · `kimi-for-coding-highspeed` (K2.7 HighSpeed, 6× vel, 3× quota). NÃO usar nomes de versão ("Kimi K3") — dá erro. ⚠️ K3/K2.7 com Thinking OFF roteia para K2.6 — manter thinking ligado.

**Configuração:** `k3-256k` adicionado ao provedor "Kimi 3" (`abc953f0-…`) em `~/.zcode/v2/config.json` (backup `.bak_pre_k3-256k_20260807_1812`); `kimi-k3` (1M) mantido. Teste ao vivo HTTP 200.

**Cenário:** cota semanal do Kimi esgotou; assinatura vigente até 23/08; assinaturas novas em fila de espera; Miguel aplicou **top-up pay-as-you-go** para cobrir ~5 dias → usar só `k3-256k` maximiza a duração do crédito pago. **Cadeia de failover vigente:** Kimi K3 (`k3-256k` default) → Qwen Code (Token Plan) → GLM-5.2 (Z.ai coding plan).

**Reversão:** seletor → `kimi-k3` (1M) volta com 1 clique; OU restaurar backup `cp ~/.zcode/v2/config.json.bak_pre_k3-256k_20260807_1812 ~/.zcode/v2/config.json`.

---

## 📅 ATUALIZAÇÃO 2026-08-01 — Saldos medidos ao vivo + estado das chaves (auditoria ZCode)

| Chave/conta | Estado 01/08 | Detalhe |
|---|---|---|
| **DeepSeek** (`fe52ae94`, única conta) | ⚠️ **saldo US$ 1,15** | Endpoint `/user/balance` medido 4× no dia: 1,21 → 1,20 → 1,15. **Recarga afirmada por Miguel ~14h NÃO visível** — ou processamento (boleto) ou feita em outra plataforma. Vigia local agora checa saldo 1×/dia (alerta < US$ 2). |
| **Kimi paygo** (`KIMI_PAYGO_API_KEY`, `Outros/chaves/kimi_paygo.env`) | ✅ viva | HTTP 200 em 29/07 e 01/08 (kimi-k3, `api.moonshot.ai/v1`). Conta reativada após recarga Miguel. É fallback do curador Cafezinho. **Arquivo órfão fora do cofre canônico** → inventário F0 do Cofre Único. |
| **Kimi vision/assinatura** (`KIMI_VISION_API_KEY`) | ✅ `sk-kimi-xQ…` SINCRONIZADA | NYC tinha a velha `sk-kimi-4K…` (401); sincronizada 01/08 11:45 do cofre local p/ `/root/chaves.sh` + `.env.unificado` (backups `*.bak_kimi_vision_20260801`). Zero 401s pós-14:20 UTC. |
| **Preços DeepSeek (confirmados ao vivo 01/08)** | flash ≪ pro | v4-flash $0,14/$0,28 (cache hit $0,0028) · v4-pro $0,435/$0,87 por 1M. **Curador Cafezinho migrado p/ flash explícito** (cascata deepseek-v4-flash → kimi-k3 → heurística; `youtube_cafezinho.py`, backup `...bak_curador_cascata_20260801`). |
| **Zhipu paygo** | US$ 0 | Só glm-4.7-flash grátis (erro 1113 nos pagos) — sem mudança. |
| **AssemblyAI** | saldo US$ 47,75 (29/05) | Autopay ativo. **CORINGA universal INTEGRADO (ordem Miguel 16/08):** último recurso da `CADEIA_PADRAO` e dos tiers `superluxo`/`padrao` do `nucleo_llm.py` + cascata do Jornal da Fórum (`youtube_cafezinho.py`). Gateway OpenAI-compatível `llm-gateway.assemblyai.com/v1`; modelo default `claude-haiku-4-5-20251001` (override `ASSEMBLYAI_GATEWAY_MODEL`). Chave mestra `sha8:77f59e59` no cofre local. Fórum: `Foruns/forum_coringa_assemblyai_cascata_llm_20260816.md`. |

Refs: `Foruns/forum_auditoria_custos_telemetria_recuperacao_crons_20260729.md` (Adendos 1–4) · `Memorias/memoria_auditoria_custos_telemetria_recuperacao_crons_20260729.md` · `Foruns/forum_unificacao_cofre_chaves_20260801.md` §6.

---

## 🐋 MAPA ESTRATÉGICO DE LLMs — Pipeline V2 — 2026-06-18

**Fórum canônico:** [`Projeto Cafezinho Agentes/Foruns/forum_mapa_estrategico_llms_pipeline_v2_20260618.md`](../Projeto%20Cafezinho%20Agentes/Foruns/forum_mapa_estrategico_llms_pipeline_v2_20260618.md)

Mapa completo de qual LLM usar em cada uma das 7 etapas do pipeline V2 (Coleta+Filtro → Scoring → Redação → Mídia → Fact-check → Auditoria → Publicação+Validador). Custo total: ~$0.12/dia (6.7x mais barato que o legado). Inclui gap analysis do que já está codeado vs o que falta implementar.

📰 **Boletim Baleia Azul:** [`Projeto Cafezinho Agentes/Foruns/boletim_baleia_azul_20260618.md`](../Projeto%20Cafezinho%20Agentes/Foruns/boletim_baleia_azul_20260618.md) — Edição #1 do jornal interno diário. Manchete: Pipeline V2 definido. Cobre decisões, sprints, AUTHs, Trindade e custos. (Coleta+Filtro → Scoring → Redação → Mídia → Fact-check → Auditoria → Publicação+Validador). Custo total: ~$0.12/dia (6.7x mais barato que o legado). Inclui gap analysis do que já está codeado vs o que falta implementar. Decisões de Miguel em 18/06: fact-check com Gemini Grounding, auditoria com websearch de luxo, filtro antilixo na coleta, validador final com poder de bloqueio.

---

## ✅ Regra Operacional — Cascata LLM com Websearch Obrigatório — 2026-06-11

**Fórum canônico:** [`Foruns/forum_cascata_llm_websearch_20260611.md`](../Foruns/forum_cascata_llm_websearch_20260611.md)

Decisão Miguel/Codex:

- Produção pode usar LLM sem busca: `deepseek-v4-pro → openai_luxo → claude-sonnet-4-6`.
- Revisão, auditoria e fact-checking exigem websearch real.
- Perplexity/Sonar está sob investigação por falso positivo; fica apenas como fallback final investigado.

Estado deployado no Tencent:

| Etapa | Cascata |
|---|---|
| Produção | `deepseek_luxo → openai_luxo → anthropic_luxo` |
| Revisão | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` |
| Auditoria | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` |
| Fact-check | Gemini + `google_search` → OpenAI `web_search` → Claude `web_search` → Perplexity fallback investigado |

Arquivos canônicos no Tencent:

- `/root/agente_roteador_llm.py`
- `/root/config/llm_context_routes.json`
- `/root/fact_check_perplexity.py`

Backups principais:

- `/root/agente_roteador_llm.py.bak_pre_openai_claude_search_20260611_codex`
- `/root/config/llm_context_routes.json.bak_pre_openai_claude_search_20260611_codex`
- `/root/fact_check_perplexity.py.bak_pre_openai_claude_search_20260611_codex`

Correção pós-auditoria real dos posts — 2026-06-11 22:27 BRT:

- A primeira subida existiu, mas a checagem dos posts `257676` e `257674` mostrou que não bastava.
- Causa 1: diversidade dinâmica podia excluir Gemini/OpenAI em `auditor` e deixar Qwen/Moonshot/Mistral entrar.
- Causa 2: `motor_publicador.py` ainda tinha fact-check/auditoria auxiliar por `gerar_texto_provider_hard("anthropic")`, sem contexto `fact_check`/`auditor`.
- Correção: `/root/agente_roteador_llm.py` agora força apenas Gemini/OpenAI/Claude com websearch em contextos obrigatórios e pula provider sem suporte; `/root/motor_publicador.py` agora chama `gerar_texto(..., contexto="fact_check")` e `gerar_texto(..., contexto="auditor")` nos portões finais.
- Backups novos: `/root/agente_roteador_llm.py.bak_fix_websearch_diversidade_20260611_codex`, `/root/motor_publicador.py.bak_fix_factcheck_websearch_20260611_codex`, `/root/motor_publicador.py.bak_fix_auditoria_extra_websearch_20260611_codex`.
- Validação remota: `compile(...)` OK nos 3 arquivos; simulação de `auditor`, `revisor` e `fact_check` com exclusões artificiais ainda retorna Gemini/Search → OpenAI/Search → Claude/Search.

---

## 🟢 SNAPSHOT CHAVES VIVAS — 2026-05-22 14:00 BRT (Claude Maestro · ordem direta Miguel)

**Contexto:** este snapshot foi criado por ordem direta do Miguel após o incidente Perplexity HTTP 401 detectado em 22/05/2026 que deixou o fact-check em fail-open. Inscrito em lugar visível pra qualquer agente da Trindade poder conferir rapidamente o estado vivo das chaves sem precisar SSH.

**Fonte canônica:** sempre `/root/.env.unificado` no Tencent (`43.156.151.165:38422`). Esta seção é o **espelho mais recente** mas pode defasar. Pra usar a chave em runtime, **NUNCA hardcode** — sempre `os.environ.get("...")`.

### 🟢 SNAPSHOT ATUALIZADO — 2026-07-09 03:30 BRT (Codex)

**Rotação OpenAI/Anthropic executada por ordem direta do Miguel.** Valores brutos não foram registrados neste nodo; usar apenas variáveis, caminhos e fingerprints curtos.

| Provider | Variáveis | Fingerprint vigente | Validação |
|---|---|---:|---|
| OpenAI | `OPENAI_API_KEY` | `sha8=0a643fdb` | local `models.list` OK; Tencent `GET /v1/models` HTTP 200 |
| Anthropic / Claude | `ANTHROPIC_API_KEY` = `CLAUDE_API_KEY` | `sha8=3b2a80d5` | local `models.list` OK; Tencent `GET /v1/models` HTTP 200 |

**Cofres sincronizados:**

- Local canônico: `Outros/chaves/agentes_labs/.env.unificado`
- Local produção/labs: `Projeto Cafezinho Agentes/root/.env.unificado`, `Projeto Cafezinho Agentes/root/chaves_novas.env`
- Local compatibilidade: `Outros/chaves/cafezinho_root/chaves.sh`, `Outros/chaves/agentes_labs/chaves.sh`, `Outros/chaves/agentes_labs/.env_root`
- Tencent vivos: `/root/.env.unificado`, `/home/ubuntu/.env.unificado`
- Tencent compatibilidade runtime: `/root/.env`, `/root/chaves.sh`, `/home/ubuntu/chaves.sh`, `/home/ubuntu/chaves_novas.env`

**Limpeza:** backups temporários da rotação apagados; arquivos legacy/backups locais e Tencent com atribuições antigas dessas três variáveis foram sanitizados. Varredura direta final: `old_assignments_remaining=0`.

**Regra:** não repetir valores brutos em fórum, chat, pacote V4 ou memória. Próximas referências devem usar somente variável + fingerprint.

### 🟢 SNAPSHOT ATUALIZADO — 2026-06-09 23:45 BRT (DeepSeek V4)

**Mudanças desde 22/05:**

| Provider | Mudança | Status |
|----------|---------|--------|
| **OpenAI** | Chave trocada (Miguel 09/06 ~18:00). `sk-proj-sSihp...` → `sk-proj---R5U09...` | ✅ |
| **Anthropic** | Chave trocada (Miguel 09/06 ~22:30). `sk-ant-api03-Bbv5Kt...` → `sk-ant-api03-aEdYQ1...` | ✅ |
| **xAI/Grok** | Chave trocada (Miguel 09/06 ~22:15). OK local, Tencent não alcança `api.x.ai` | ⚠️ |
| **Gemini** | Cota renovada por Miguel 09/06 | ✅ |
| **Zhipu/GLM** | Sem saldo. REMOVIDO da cascata (`status: inativo_sem_saldo`) | ❌ |
| **AssemblyAI** | Gateway c/ 5 modelos. Config: `assemblyai_modelos.json`. Fórum: `forum_assemblyai_gateway_20260609.md` | ✅ |
| **GA4** | Credencial renovada (Miguel 09/06). `private_key_id: 4b8fa439...` | ✅ |

**APIs vivas (10/12):** OpenAI, DeepSeek, Qwen, Kimi, Perplexity, Mistral, Groq, Gemini, Anthropic, AssemblyAI
**Offline:** Zhipu (sem saldo), xAI/Grok (bloqueio de rede no Tencent)
**Limpeza Tencent:** 1.597 → 766 itens. B2: `Legacy-Cafezinho`. Fórum: `forum_governanca_limpeza_backups_20260609.md`

### Chaves LLM ativas (validadas 14:00 BRT)

| Provider | Variável | Chave (vigente) | Validação |
|---|---|---|---|
| OpenAI | `OPENAI_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| DeepSeek | `DEEPSEEK_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Gemini | `GEMINI_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Anthropic / Claude | `ANTHROPIC_API_KEY` = `CLAUDE_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso (sob assinatura Max) |
| xAI / Grok | `XAI_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | 🟢 **Funcionando 22/05 14:05** (testado `grok-3` → HTTP 200 retornou `grok-4.3`). Os 403 eram de ontem 21/05 21:41 BRT antes de Miguel recarregar. Crédito atual: $3.54. ⚠️ Hardcoded em `agente_fantastico.py` e `agente_master_trends_v9.py` (não passaram pela reforma Codex 22/05). |
| Groq | `GROQ_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Mistral | `MISTRAL_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| **Perplexity** | `PERPLEXITY_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | 🟢 **NOVA — instalada por Claude Maestro 22/05 13:55 BRT após HTTP 401 da chave antiga `pplx-nlg8...`. Smoke sonar-pro HTTP 200 antes E depois da instalação.** |
| Qwen / Alibaba | `DASHSCOPE_API_KEY` = `QWEN_API_KEY` = `ALIBABA_API_KEY` | `sha8=62c5c207` | 🟢 **ROTACIONADA 01/08 ~17:00 BRT (ZCode, ordem Miguel)** — workspace sk-ws-, conta migueldorosario2, Singapore. Unificou 6 valores antigos drift (incl. `850f5099` morta e `5f38f6a9` fantasma). Smoke NYC produção: qwen-plus "OK" + qwen-vl-plus "Red." (visão). Tencent espelho + local OK. `QWEN_API_KEY_2` unificado. Antigas → `legacy_qwen_keys_20260801.md`. Detalhe: `forum_rotacao_qwen_unificacao_62c5c207_20260801.md`. |
| Kimi / Moonshot | `KIMI_API_KEY` = `MOONSHOT_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso (crédito recarregado por Miguel 22/05 ~13:30 BRT) · ⚠️ **content filter bloqueia política BR** (Bolsonaro etc) |
| Zhipu / GLM | `ZHIPU_API_KEY` = `GLM_API_KEY` = `BIGMODEL_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | 🟢 **NOVA — Miguel 25/05 ~13:50 BRT.** Primeira chave Zhipu no ecossistema (nunca existiu antes). Crédito adicionado por Miguel. Deploy Tencent por Codex 14:55 BRT. Testada OK com `glm-4-plus`. |
| MANUS | `MANUS_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |

### Chaves de busca/imagem

| Provider | Variável | Chave | Estado |
|---|---|---|---|
| Brave Search | `BRAVE_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | rotacionada em 2026-07-26 (Miguel aumentou limite do plano); validada 10/10 + 30/30 queries (mediana 1.25s, p95 1.6s); usada na coleta V4 temáticos + camada 2 do gate fact-check Sentinela (bug #37) |
| SearchAPI (searchapi.io) | `SEARCHAPI_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | 🟢 NOVA 2026-07-26 (em `chaves_novas.env`); Google real, qualidade boa mas latência instável (p95 7.8s, max 26s) → camada RESERVA do gate fact-check com timeout 5s; quota não consultável via API (`/account` 404) — plano pendente dashboard Miguel |
| Brave Answer API | (chave separada) | `[OCULTADO_POR_SEGURANCA]` | ⚠️ DESCARTADA como oráculo de fact-check 2026-07-26 (se contradisse entre queries adjacentes: Fachin vs Barroso); mantida pra uso futuro de chat, NÃO entra no pipeline |
| Google Custom Search JSON API | — | — | ❌ INVIÁVEL 2026-07-26: Google fechou a API pra projetos novos em 2026 (HTTP 403 PERMISSION_DENIED mesmo com billing ativo); desligamento total previsto 2027-01-01. Não é bug nosso. |
| Fal.ai | `FAL_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Ideogram | `IDEOGRAM_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Flickr (live photo) | `FLICKR_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | em uso |
| Google Developer API | `GOOGLE_DEVELOPER_API_KEY` | `[OCULTADO_POR_SEGURANCA]` | 🟢 **NOVA — Miguel 2026-06-05.** Para PageSpeed Insights e CrUX APIs. |


### §90 Sistema de Notas LLM — ATIVADO EM PRODUÇÃO (25/05 14:50 BRT)

**Arquivo canônico:** `root/config/llm_ratings.json`
**Roteador:** `root/llm_ratings_router.py` — consultado por `agente_roteador_llm.py` quando `LLM_RATINGS_ROUTER_ENABLED=1`
**Fórum:** `Foruns/forum_pesquisa_precos_llms_20260525.md`

**3 dimensões:** Qualidade (Q⭐ 1-5), Economia (P⭐ 1=caro 5=barato), Velocidade (V⭐ 1-5)

**Cascata dinâmica ativa:**
- Redação: `deepseek-v4-pro → moonshot-v1-32k → qwen-max → qwen3-max → gemini-2.5-pro → gpt-4o`
- Revisão: exclui DeepSeek (cruzamento editorial)
- Auditoria: exclui DeepSeek + Moonshot (terceira voz)
- Tribunal Visual: `qwen-vl-plus` primário (mais barato $0.26/M), `gemini-2.5-flash` cross-check
- Fact-check: Perplexity Sonar (obrigatório)

**Regra:** trocar modelo = editar JSON, sem deploy de código. Modelo novo → testar §66.6 → atualizar JSON → automaticamente entra na cascata.

### Variáveis de configuração DeepSeek-V4 (atualizadas 22/05 13:55-13:58 BRT)

| Variável | Valor atual | Default código | Notas |
|---|---|---|---|
| `DEEPSEEK_V4_MIN_MAX_TOKENS` | `32000` | 6500 | **Claude Maestro 22/05 13:57 BRT.** Ordem Miguel pós-fire 13:41 BRT que retornou content vazio em 1m55s (reasoning consumiu piso 6500). Reproduziu §66 bug fundador. **Ver também:** [`BUG-20260522-DEEPSEEK-V4-JSON-PARSE-REVISAO`](./CEREBRO_NODE_BUGS.md#bug-20260522-deepseek-v4-json-parse-revisao) (JSON truncado em revisão, inscrito por Claude 19:00 BRT, indexado por Kimi K4). |
| `DEEPSEEK_V4_TIMEOUT` | `360` | 240 | **Claude Maestro 22/05 13:58 BRT.** Alinhado com max_tokens grande (6min). |
| `DEEPSEEK_TIMEOUT` (não-V4) | (não setado) | 90 | sem ajuste |

### Backup pré-incidente

- `/root/.env.unificado.bak_pre_pplx_e_deepseek_maxtokens_20260522_1355_claude` (Tencent · 156 linhas · estado anterior à atualização Perplexity/DeepSeek-V4)
- Rollback 1 comando: `sudo cp <backup> /root/.env.unificado`

### ⚠️ Regras de uso

1. **NUNCA hardcode** chave em código (`.py`, `.sh`, JSON). Sempre `os.environ.get("KEY")`.
2. **NUNCA postar chaves no canal_trindade.md ou em fóruns públicos.** Use este Cérebro como referência interna.
3. **Atualizar este snapshot** após CADA troca de chave (anotar timestamp + agente + motivo).
4. **Validar antes de instalar:** sempre rodar curl/HTTP smoke ANTES de sobrescrever `.env.unificado`.
5. **Backup obrigatório** pré-mudança: `cp .env.unificado .env.unificado.bak_pre_<motivo>_<YYYYMMDD_HHMM>_<agente>`.
6. **Linha vermelha §10:** NUNCA `crontab -r` ou tocar `.env` sem aval Miguel (exceto quando ele autoriza explicitamente, como hoje 22/05).

### Bugs/quotas conhecidos hoje (22/05/2026 14:00 BRT)

- 🟢 **xAI/Grok** — 403 era de 21/05 21:41 BRT (crédito zerado). Miguel recarregou; testado agora 22/05 14:05 BRT → HTTP 200. Crédito $3.54 disponível. Cuidado: hardcoded em `agente_fantastico.py` e `agente_master_trends_v9.py` (modelo `grok-4-fast-non-reasoning` redireciona pra `grok-4.3` upstream). Esses 2 agentes NÃO passaram pela reforma asiática Codex 22/05.
- 🟡 **Kimi/Moonshot content filter** — bloqueia política BR (Bolsonaro, Flávio, escândalos) com HTTP 400 "high risk". Crédito recarregado por Miguel mas filtro chinês persiste. Recomendar GLM/Mistral como fallback auditor em pautas BR sensíveis.
- 🟢 **Perplexity** — chave nova instalada após HTTP 401 da antiga (24h+ de fail-open).

— Inscrito por Claude Maestro · 2026-05-22 14:02 BRT · ordem direta Miguel

---


Este nó mapeia todas as credenciais sensíveis e a malha de inteligência artificial do sistema. 
**Objetivo principal:** Garantir que o Cérebro saiba exatamente ONDE as chaves estão, QUAIS LLMs estão disponíveis e COMO não desperdiçar dinheiro/tokens.

---

## 1. Cofres de Credenciais e Chaves de API
- 📁 **Tema: Proteção e Acesso a Chaves de IA e Servidor**
  - **Fórum:** [forum_seguranca_chaves.md](./Foruns/forum_seguranca_chaves.md) (Regras de proteção)
  - **Memória / Cofre Físico (Index):** O índice mestre real das chaves da Tencent, GSN e Backblaze fica em `/root/chaves_novas.env` e documentadas na pasta local em `/root/chaves/`.

## 1.1. Catálogo Completo de Chaves (Todas as APIs e Serviços)
As credenciais diretas das LLMs e serviços NÃO devem ser expostas aqui. Elas se encontram exclusivamente no arquivo de configuração do servidor (`/root/.env` ou `/root/chaves_novas.env`). NENHUM token ou chave verdadeira deve ser guardado em texto plano nos fóruns ou nós do Cérebro, por determinação expressa do validador de segurança.

Para referência de QUAIS serviços possuímos chaves (sem expor as chaves em si):
- LLMs Chinesas: ZHIPU_API_KEY, QWEN_API_KEY, DEEPSEEK_API_KEY, KIMI_API_KEY
- LLMs Ocidentais: OPENAI_API_KEY, ANTHROPIC_API_KEY, CLAUDE_API_KEY, GEMINI_API_KEY
- LLMs Alternativas e Busca: XAI_API_KEY, GROQ_API_KEY, MISTRAL_API_KEY, PERPLEXITY_API_KEY, BRAVE_API_KEY
- Geração de Mídia: FAL_API_KEY, IDEOGRAM_API_KEY, FLICKR_API_KEY, ELEVENLABS_API_KEY, HEYGEN_API_KEY, CREATOMATE_API_KEY, TRANSKRIPTOR_API_KEY
- Redes Sociais e Telegram: X_API_KEY, TELEGRAM_TOKEN

### Atualização Codex 2026-05-09 11:52 BRT — Kimi / Moonshot

- `KIMI_API_KEY` e `MOONSHOT_API_KEY` existem localmente em `Outros/chaves/kimi.env` e foram instaladas, sem expor valor, nos `.env` operacionais locais e no Tencent.
- Arquivos locais com variável: `root/.env`, `root/.env.unificado`, `root/chaves_novas.env`, `.env`.
- Arquivos Tencent com variável: `/root/.env`, `/root/.env.unificado`, `/root/chaves_novas.env`, `/root/chaves.sh`.
- `CEO_KIMI_MODEL=kimi-k2.6` é o modelo inicial do CEO do Cérebro, por ordem do Miguel de começar pelo melhor Kimi e reduzir depois.
- Compatibilidade: `kimi-k2.6` exige `temperature=0.6` e, para boletim textual direto, o CEO envia `thinking={"type":"disabled"}` via `extra_body`.
- Smoke real Codex: `root/agent_data/ceo_index/relatorios/ceo_cognitivo_20260509_115146.md`, provider `kimi`, modelo `kimi-k2.6`, custo `US$0.000442`.

### Atualização Codex 2026-05-20 09:45 BRT — Recarga Kimi/Moonshot e Zhipu/GLM

**Objetivo:** registrar onde recarregar e qual foi o problema operacional observado, sem guardar chaves ou dados de cartão.

**Kimi / Moonshot**

- Painel oficial: `https://platform.moonshot.ai/`
- Documentação de recharge/rate limit: `https://platform.kimi.ai/docs/llms.txt` como índice geral; página de Recharge and Rate Limiting informa tiers por recarga acumulada.
- Sintoma observado em 2026-05-20: API respondia HTTP 429 com `exceeded the consumption budget`, mesmo com chave presente.
- Diagnóstico: não era apenas rate limit por tier; era limite/budget de consumo do projeto/API key.
- Correção feita por Miguel: upgrade para Tier 2 e ajuste do consumption budget do projeto.
- Smoke pós-correção: `KIMI_API_KEY`, `MOONSHOT_API_KEY` e `KIMI_API_KEY_2` responderam `OK` via `moonshot-v1-8k`.
- Lembrete operacional: se voltar esse erro, conferir primeiro o saldo e depois o budget do projeto associado à chave `ak-...`; não expor a chave completa no Cérebro/canal.

**Zhipu / GLM**

- Painel oficial de billing/API keys: `https://z.ai/manage-apikey/billing`
- Sintoma observado em 2026-05-20: API respondia HTTP 429 com código `1113` e mensagem chinesa `余额不足或无可用资源包,请充值。`
- Tradução operacional: saldo insuficiente ou sem pacote disponível; precisa recarregar.
- Correção feita por Miguel: recarga no painel.
- Smoke pós-correção: `glm-4-plus` respondeu `OK` com uso mínimo de tokens.
- Lembrete operacional: Zhipu fica configurado no local/Tencent; no Alibaba, nesta verificação, não havia `ZHIPU_API_KEY` carregada.

### Atualização Codex 2026-05-10 04:50 BRT — Backblaze do Cérebro/Memórias

Miguel criou uma application key Backblaze com o nome `cerebro-memorias`.

**Finalidade:** permitir que o Cérebro use Backblaze de maneira inteligente:

- espelhar regularmente a memória viva;
- arquivar memórias antigas/pesadas;
- manter índice local no Alibaba;
- deixar manifesto, resumo e caminho de recuperação para tudo que sair do Alibaba;
- nunca transformar Alibaba em backup frio.

**Regra de segurança:** o `applicationKey` bruto não deve ser registrado em fóruns, canal, nodes do Cérebro ou logs. O Cérebro registra apenas o nome/finalidade da chave e as variáveis esperadas:

- `B2_CEREBRO_KEY_ID`
- `B2_CEREBRO_APPLICATION_KEY`
- `B2_CEREBRO_BUCKET`

O valor real deve existir somente em arquivo de segredo com permissão restrita ou cofre operacional, nunca em memória pública.

**Regra de baldes Backblaze (Miguel 2026-05-10 05:20 BRT):**

- `failover-cafezinho1` é o balde do **sistema/failover/produção**.
- `Cerebro-Memorias` é o balde do **Cérebro e memórias**.
- Não misturar os dois. O Cérebro deve usar `Cerebro-Memorias`; backups operacionais do Cafezinho continuam no balde de failover.

**Status 2026-05-10 05:20 BRT:** Fase 0 dry-run aprovada 5/5. Fase 1 snapshot manual único executada no Alibaba com a chave `cerebro-memorias`, sem expor segredo em logs públicos. O arquivo seguro local é `Outros/chaves/backblaze_cerebro.env`; no Alibaba fica em `/root/cerebro_trindade/secrets/backblaze_cerebro.env` com permissão `600`.

**Snapshot/restore 2026-05-10 05:23 BRT:** snapshot real em `b2://Cerebro-Memorias/cerebro-snapshots/2026/05/cerebro_snapshot_20260510_082000.tar.gz`; manifesto em `root/agent_data/backblaze_index/snapshot_20260510T082000.json`; restore check para `/tmp` no Alibaba aprovado com `size_matches=true`, `sha1_matches=true` e `sha256_matches=true`.

**Parecer DeepSeek 2026-05-10 05:26 BRT:** DeepSeek aprovou a Fase 1 como segura e sem risco crítico. Antes de cron diário, exigiu travas: checagem de disco livre, intervalo mínimo de 6h, lock contra execução simultânea, alerta após 2 falhas e limite de 1 GB por snapshot. Proibiu `b2_delete_file_version`, stubs automáticos sem validação humana, chave dentro de cron e mistura entre `failover-cafezinho1` e `Cerebro-Memorias`.

**Travas implementadas 2026-05-10 05:41 BRT:** `scripts/cerebro_b2_snapshot.py` agora possui checagem de disco livre, intervalo mínimo de 6h, lock, alerta após 2 falhas e limite de 1 GB por snapshot. Instalado também no Alibaba em `/root/cerebro_trindade/scripts/cerebro_b2_snapshot.py`. Smoke remoto foi apenas `local_only`, sem novo upload e sem cron.

## 2. Roteamento de Inteligência Artificial (LLMs)
O sistema deve saber usar a IA certa para o trabalho certo:
- **Claude (Opus/Sonnet) e GPT-4:** Para alta densidade analítica, arquitetura (Antigravity) e **Criação de Texto/Redação de Fato**. São as escolhas **prioritárias** para gerar as matérias, por alta precisão e baixa alucinação. **NÃO são exclusivos:** se ambos caírem (custo, quota, indisponibilidade), o fallback é liberado. Gemini 3.1 Pro é uma alternativa muito boa nessa situação. *(Correção Miguel 2026-05-09 13:18 BRT, contra interpretação anterior de "exclusividade".)*
- **DeepSeek (V4/R1):** APENAS para programação pura e lógica matemática. **PROIBIDO PARA REDAÇÃO/CRIAÇÃO DE TEXTO** — testes de campo comprovaram que o modelo alucina excessivamente na redação, mesmo com auditorias, prompt rigoroso e conteúdo objetivo. A promoção de maio deve ser aproveitada apenas para código.
- **Perplexity:** Ferramenta oficial para **Fact-Checking** rigoroso e busca de fontes fidedignas.
- **Kimi (Moonshot):** Extração em massa via Long-Context (ler e resumir documentos/PDFs gigantes, sem gerar novos textos).
- 📁 **Tema: Roteamento Inteligente e Economia de Tokens**
  - **Fórum:** [forum_modelos_dinamicos.md](./Foruns/forum_modelos_dinamicos.md)
  - **Memória:** [memorias_modelos_dinamicos_governanca_20260502.md](./Memorias/memorias_modelos_dinamicos_governanca_20260502.md)
  - **Código Mestre:** O roteador principal que implementa isso vive em `/root/agente_roteador_llm.py`.

## 2.1. Modelos Simples com Escalada Dinâmica
- **Princípio:** modelo simples por padrão; escalada obrigatória por complexidade. O agente começa pelo Cérebro e pelo menor modelo suficiente. Se faltar ficha, rollback, evidência, contexto ou segurança editorial, sobe de nível. Se uma solução amadurece no Cérebro, desce de nível.
- **Níveis:**
  1. **N0 — lookup sem LLM:** índice, regex, tabela de sintomas, validação simples.
  2. **N1 — modelo simples/sentinela:** canal, logs, classificação, autocura conhecida.
  3. **N2 — modelo médio:** investigação de variante, auditoria, dry-run, falso positivo.
  4. **N3 — modelo forte:** causa raiz difícil, arquitetura, regra nova, código crítico.
  5. **N4 — Miguel:** decisão humana crítica, irreversível, sensível ou acima do mandato.
- **Gatilhos de subida:** solução ausente no Cérebro; soluções conflitantes; rollback incerto; produção/crontab/WPCode/credenciais/custo alto; impacto >50%; risco factual/editorial; contexto grande demais; incerteza que muda a ação.
- **Gatilhos de descida:** sintoma recorrente ≥2 vezes; fix em ficha curta; rollback e validação claros; autocura estável ≥7 dias; resultado binário/verificável.
- **Fórum de desenvolvimento:** [forum_trindade_protocolos.md](./Foruns/forum_trindade_protocolos.md) — Rodada 6.

## 2.2. AssemblyAI LLM Gateway — Candidato Isolado
- **Atualização Codex 2026-05-07 16:36 BRT:** fontes oficiais AssemblyAI indicam endpoint `https://llm-gateway.assemblyai.com/v1/chat/completions`, compatível em formato com Chat Completions. Uso permitido nesta janela apenas como Fase 0/1 do Sobrenatural: forum/contrato tecnico e smoke isolado dry-run. **Nao tocar em `agente_roteador_llm.py`** sem proposta separada, consenso, rollback e validacao de custo.
- **Fórum:** [forum_sobrenatural_assemblyai.md](./Foruns/forum_sobrenatural_assemblyai.md)

### Atualização 2026-05-29 — Billing LLM Gateway + chave mestra

**Fonte:** painel Billing AssemblyAI do Miguel em 2026-05-29 + docs oficiais (`/pricing` e LLM Gateway Chat Completions).

**Estado da conta:** Pay as you go; saldo observado no painel: US$ 47.75. Autopay ativo no painel. Não registrar dados de cartão no Cérebro.

**Smoke chave mestra:** Tencent, 2026-05-29 16:3x BRT. Chave presente (`sha8:77f59e59`), `POST https://llm-gateway.assemblyai.com/v1/chat/completions`, modelo `claude-haiku-4-5-20251001`, prompt mínimo, `max_tokens=3`: HTTP 200, resposta `OK.`, uso `input_tokens=13`, `output_tokens=3`.

**Preços operacionais LLM Gateway — USD/1M tokens:**

| Modelo | Input | Output |
|---|---:|---:|
| Claude Opus 4.7 | 5.50 | 27.50 |
| Claude Sonnet 4.6 / 4.5 / 4 | 3.00 | 15.00 |
| Claude 4.5 Haiku | 1.00 | 5.00 |
| Claude 3.5 Haiku | 0.80 | 4.00 |
| Claude 3 Haiku | 0.25 | 1.25 |
| GPT-5.2 | 1.75 | 14.00 |
| GPT-5 / GPT-5.1 | 1.25 | 10.00 |
| GPT-5 Mini | 0.25 | 2.00 |
| GPT-5 Nano | 0.05 | 0.40 |
| GPT-4.1 | 2.00 | 8.00 |
| ChatGPT-4o | 5.00 | 15.00 |
| Gemini 2.5 Flash Lite | 0.10 | 0.40 |
| Gemini 2.5 Flash | 0.30 | 2.50 |
| Gemini 2.5 Pro (0-200K) | 1.25 | 10.00 |
| Gemini 3 Pro Preview (0-200K) | 2.00 | 12.00 |
| Gemini 3 Flash Preview | 0.50 | 3.00 |
| Kimi K2.5 | 0.60 | 3.00 |
| Qwen3 32B | 0.15 | 0.60 |
| Qwen3 Next 80B A3B | 0.15 | 1.20 |
| gpt-oss-20b | 0.07 | 0.30 |
| gpt-oss-120b | 0.15 | 0.60 |

**Custo accounting:** em 2026-05-29 Codex ajustou o Sobrenatural para registrar chamadas como `assemblyai_gateway:<modelo>` e adicionou aliases AssemblyAI em `root/agent_data/precos_modelos.json`, evitando contaminar preços de provedores diretos.

## 3. Transparência Financeira (A Memória de Despesas)
- 📁 **Tema: Auditoria de Gastos e Tokens (USD)**
  - **Livro-Caixa:** [memoria_despesas.md](./Memorias/memoria_despesas.md)
  - **A Regra:** Qualquer rodada pesada de desenvolvimento que consuma grandes fatias de contexto ou anomalias financeiras nas APIs deve ser obrigatoriamente registrada na `memoria_despesas.md` pelo agente responsável (Antigravity, Claude Code ou Codex).

## 4. Banco de Dados Supabase (Rio Carta)
As chaves da API do banco de dados do Rio Carta (Supabase), criadas em 2026-05-11 para o sistema de Comentários Abertos.
- **URL do Projeto:** `https://qznsodqyfwhaouruhsbp.supabase.co`
- **Chave Pública (Anon):** `sb_publishable_yLB3sZINbJc3sY8tYD9mKQ_gQt3e7BF` (Pode ser exposta no front-end).
- **Chave Secreta:** Salva localmente em `rio_carta/.env`. NUNCA deve ser exposta publicamente nem commitada no GitHub.

---
*Nota: Este nó garante a eficiência financeira e segurança estrutural do Cérebro.*


## [2026-05-15 14:10 BRT] Referencia de chave publica SSH - Droplet Rio Carta Astro

Esta entrada registra **chave publica SSH**, nao segredo. A chave privada correspondente fica localmente em `~/.ssh/id_ed25519` e nao deve ser copiada para forum/canal/Cerebro.

Alvo: `root@159.89.185.209` (`agente-clone-01`, DigitalOcean Astro/API Rio Carta).

Chave publica:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFfXIj3Has1WDRbn95V89g/YpJ6tSXIu3CF3yB9vTbHm migueldorosario@novo
```

Fingerprint:

```text
256 SHA256:wB+pG1u1dDKyxP9bQSRDIzl+4Uxj6QD45Px6AL/dQqI migueldorosario@novo (ED25519)
```

Comando recomendado:

```bash
ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 root@159.89.185.209
```

Fonte historica da recuperacao: `Projeto Cafezinho Agentes/scratch/scratch_ssh.py`. Esse scratch contem material sensivel; nao replicar senha. Forum operacional: `Rio Carta Agentes/Foruns/forum_riocarta_ssh_droplet_20260515.md`.


## [2026-05-17 09:39 BRT] Qwen/DashScope — chave nova validada e lição de governança

Qwen foi estabilizado com nova chave internacional DashScope, fingerprint `sha8=0a93e3ae` / máscara `sk-92f...4f33`. Valor real não deve ser repetido em fórum/canal.

A conta enxerga modelos de topo e multimodais. Testes OK: `qwen3.6-max-preview`, `qwen3-max-preview`, `qwen-max-latest`, `qwen3.6-plus`, `qwen-plus-latest`, `qwen-vl-max-latest` e `qwen-image-2.0-pro` na listagem viva.

Decisão operacional: usar `qwen3.6-max-preview` para tarefas Qwen de maior exigência quando custo/latência aceitarem; `qwen3.6-plus`/`qwen-plus-latest` para equilíbrio; `qwen-vl-max-latest` no tribunal visual; `qwen-image-2.0-pro` como fallback chinês de imagem.

O atraso ocorreu porque o sistema não tinha fonte única de verdade: local Cafezinho já estava novo, mas Cingapura e outros arquivos ainda estavam antigos. A partir deste incidente, chave LLM só é considerada atualizada se local + servidor vivo + endpoint + smoke remoto baterem.


## [2026-05-18 02:58 BRT] Relatório benchmark redação editorial sob trava anti-alucinação §4.2 (Claude)

Antes do deploy F0a/Zhipu, rodei bake-off direto entre `glm-4-plus`, `deepseek-v4-pro` e `deepseek-chat` com `temperature=0.1` + sys_prompt da política §4.2 (instrução explícita de recusar quando faltar fonte). Detalhes técnicos em `CEREBRO_NODE_GOVERNANCA.md` §66.7 e `Foruns/forum_comparativo_monitoramento_llm_20260518.md` §4.2.1-bis.

### Relatório por LLM (estado 18/05/2026)

| LLM | Velocidade | Custo aprox | Trava anti-alucinação | Veredito |
|---|---|---|---|---|
| `deepseek-v4-pro` | ⚡ 617ms (não-reasoning na prática) | ~$0.0014/chamada | ✅ Respeita | 🥇 PRIMÁRIO REDAÇÃO/AUDITORIA |
| `glm-4-plus` | 🐌 11s média | ~$0.001/chamada | 🔴 **DESOBEDECE** (alucina decreto inexistente como se fosse real) | 🟡 Tier 2, não capitania editorial |
| `deepseek-chat` | ⚡ 628ms | ~$0.0001/chamada | ✅ Respeita | 🥉 Fallback econômico |
| `qwen-plus-latest` | ⚡ 3.2s (sem censura BR) | ~$0.003/chamada | testado parcialmente | OK alinhamento editorial |
| `qwen-max` | a testar | a testar | a testar | Pendente bake-off direto |
| `moonshot-v1-32k` (Kimi) | varia | $1/$3 por 1M | a testar trava | Long-context, revisor candidato |

### ⚠️ Alerta `glm-4-plus`

Mesmo com `temperature=0.1` + sys_prompt "NUNCA invente nomes, datas, números, fontes ou eventos; se não tiver certeza, recuse", o GLM-4-plus inventou conteúdo plausível para um decreto fictício (14.890 de 12/11/2026 sobre criptoativos):

> "O decreto presidencial nº 14.890 de 12 de novembro de 2026 **estabelece regras para criptoativos no Brasil**. A norma cria um regime jurídico específico... **exchanges devem se registrar no Banco Central**... **transações acima de R$ 30 mil passarão a ser monitoradas**..."

Falha grave: desobedeceu instrução explícita do sys_prompt. Bug catalogado em `BUG-20260518-GLM-4-PLUS-ALUCINA-COM-TRAVA-EXPLICITA`.

### Caveat sobre §66.1 (datado 14/05)

`deepseek-v4-pro` estava listado no §66.1 como reasoning de 12.7s. Meu teste de 18/05 deu **617ms**. Possíveis razões: DeepSeek mudou comportamento da API, ou o bug `BUG-20260514-DEEPSEEK-V4-REASONING-TOKENS-CONSUMIDOS` foi corrigido pela DeepSeek. Validar com Codex no deploy.

### Política de manutenção

A pedido do Miguel: "manter relatório atualizado sobre cada LLM". Sempre que um LLM novo for testado ou um existente mostrar comportamento mudado, atualizar esta tabela com data + comportamento + veredito + link pro bake-off. Não apagar entradas antigas — apender revisões pra preservar histórico.


## [2026-05-18 03:42 BRT] Sistema de Notas LLM — novo padrão de governança (em construção)

Miguel propôs (e Trindade adotou) substituir a nomenclatura ambígua "luxo / econômico" por **sistema de notas em 2 dimensões independentes** (1-5⭐ qualidade + 1-5⭐ economia).

**Fórum de trabalho:** `Foruns/forum_sistema_notas_llm_20260518.md` (rascunho colaborativo Trindade)

### Princípios

1. **Cada modelo recebe 2 notas**:
   - Qualidade editorial (1-5⭐) — capacidade de não-alucinar + obedecer trava
   - Economia (1-5⭐, 5=mais barato) — custo por chamada
2. **Convenção universal:** mais estrelas = mais desejável pro projeto, em ambas dimensões
3. **Regra de elegibilidade por tarefa:**
   - Redação/revisão/auditoria/fact-check: qualidade ≥ 4⭐
   - Periféricos editoriais (comentários, moderação, etc.): qualidade ≥ 4⭐
   - Periféricos simples (coleta, parsing): qualidade ≥ 2⭐
4. **Cascata derivada automaticamente** — filtra por qualidade mínima, ordena por economia desc, preferência asiático sobre ocidental
5. **Pesquisa independente** por cada IA da Trindade (Claude / Codex / DeepSeek / Antigravity) antes de consenso — evita viés
6. **Agente curador** semanal atualiza notas com base em testes-trava + preços oficiais — propõe diff, não aplica direto

### Arquivo destino futuro

`root/config/llm_ratings.json` — substitui (gradualmente) `llm_context_routes.json` (que tem chaves `luxo`/`economico` que viraram nomenclatura morta).

### Substituição de hardcodes

Hardcodes tipo `gerar_texto_provider_hard("zhipu", ...)` viram dinâmicos:
```
gerar_texto(..., tarefa="redacao") → roteador lê llm_ratings.json e escolhe
```

### Cronograma

2 semanas estimadas até sistema completo + monitor + curador rodando. Detalhe em §12 do fórum.

### Status atual (atualizado 18/05 15:10 BRT)

- ✅ Critérios definidos
- ✅ Tabela inicial rascunho Claude (26 modelos com notas Q/E) — §3 do fórum
- ✅ Pesquisa independente Codex — concluída 18/05 13:15 BRT (§14 do fórum: agregação local `banco_custos.json` + `governanca_financeira_api_usage.jsonl` + `log_rotas_llm.jsonl`)
- ✅ Pesquisa independente DeepSeek — concluída 18/05 (§16 do fórum: testes ao vivo Zhipu/DeepSeek/Qwen)
- ✅ Pesquisa independente Antigravity — concluída 18/05 (§15 do fórum: preços oficiais 1M tokens + Arena 2026)
- ✅ Parecer cruzado Codex sobre §15 — §17 do fórum (13:25 BRT: pediu URLs/data + propôs duas economias separadas)
- ✅ Consolidação técnica provisória Codex — §18 do fórum (14:55 BRT: schema mínimo, tabela 18 modelos, regras por tarefa, ordenação roteador)
- ✅ Auditoria Claude — §19+§20 do fórum (03:59 + 14:50 BRT: auto-crítica, 3 divergências resolvidas, adendo schema `bloqueado_por_politica`)
- ✅ Correção crítica Claude — §20.6 do fórum partia de premissa errada (sangria Anthropic ativa). **Auditoria 14:58 BRT confirmou:** `anthropic.enabled=false` desde 14/05 + zero linhas Anthropic em `banco_custos_2026-05.jsonl`. Sangria já tinha parado. Lição registrada: verificar premissa atual de custo/estado antes de propor decisão urgente.
- ✅ Handoff Claude → DeepSeek (parcial dividido) — §22 do fórum (15:08 BRT): DeepSeek pega testes-trava + custos reais chineses (chaves PROD); Claude fica em supervisão sem chaves; Codex segue código.
- ✅ Decisão Miguel 15:30 BRT: caminho A aprovado. F0a intermediário reescalonado para dentro do sprint completo do sistema de notas/roteador dinâmico; sem deploy Tencent avulso porque Anthropic já está desativado desde 14/05.
- 🟡 Pendente DeepSeek: testes-trava `qwen3-max`, `mistral-large-latest`, `kimi-k2.5`, `qwen-max-latest`, `glm-5.1[enable_thinking=false]`, `qwen-vl-max-latest` (imagem real), `glm-5.1` em temas sensíveis CN
- 🟡 Pendente Antigravity: URLs/fontes/data nas tabelas oficiais §15 (Codex §17/§18.5 cobrou)
- ✅ Codex: `root/config/llm_ratings.proposta.json` + `scripts/validar_llm_ratings.py` criados em modo seguro, fora do roteador, com 28 modelos e validação local.
- ⏸️ Migração F0a (reescalonada para o sprint completo; sem deploy intermediário)

**Indexação Cérebro:** §66.8 + §66.8.1 do `CEREBRO_NODE_GOVERNANCA.md` (§66.8.1 é o estado consolidado pós-handoff).

---

### [2026-05-21 19:25 BRT] — Política Perplexity por silo

**Decisão Miguel:** Perplexity continua permitido no Cafezinho, mas fica pausado no Rio Carta e no Global South News durante a reforma editorial/infraestrutural.

**Motivo:** diagnóstico de custo mostrou uso relevante no Cafezinho/Tencent (`sonar-pro` em fact-check), e Miguel decidiu evitar expansão desse custo para os satélites.

**Regra operacional:**
- Cafezinho: Perplexity permitido para fact-check, sob monitoramento financeiro.
- Rio Carta: Perplexity bloqueado/pausado.
- Global South News: Perplexity bloqueado/pausado.
- Roteadores, cascatas e `llm_ratings` não devem escolher Perplexity para Rio Carta/GSN sem autorização explícita de Miguel.

**Arquivos locais ajustados por Codex:**
- `Rio Carta Agentes/root/riocarta_publicador_tematicos.py`
- `Global South News/root/gsn_publicador_tematicos.py`

**Registro:** `Foruns/forum_freio_perplexity_riocarta_gsn_20260521.md`

---

### [2026-05-22 00:38 BRT] — Política LLM Mundo Trilhos

**Decisão Miguel/Trindade:** Mundo Trilhos deve operar durante a reforma com pipeline editorial 100% asiático e sem Perplexity.

**Arquitetura proposta no fórum:**

- Triagem: DeepSeek V4 Flash
- Redação: DeepSeek V4 Pro
- Higienização: Qwen Max
- Fact-checking de coerência lógica: Kimi/Moonshot
- Auditoria final: Zhipu/GLM

**Regra operacional:** Mundo Trilhos não deve usar Perplexity, OpenAI, Anthropic ou Gemini no pipeline de publicação sem autorização explícita posterior de Miguel. Antes de deploy, a Trindade deve confirmar nomes reais dos modelos configurados no roteador/cascata e testar chaves sem expor segredos.

**Registro:** `Foruns/forum_mundo_trilhos.md`

---

### Atualização Kimi K3 2026-07-25 ~01:00 BRT — Nova chave Zhipu testada (pedido Miguel)

Miguel passou chave Zhipu nova via chat para teste de viabilidade (organização de assinaturas com API). Resultados (sem exposição do valor — referência `sha8=bf908cec`):

| Teste | Chave NOVA (`sha8=bf908cec`) | Chave COFRE (local sentinela) |
|---|---|---|
| `GET /paas/v4/models` (autenticação) | ✅ HTTP 200 · 8 modelos visíveis | ✅ HTTP 200 · idem |
| `glm-5.2` chat completion | ❌ HTTP 429 código 1113 — "sem saldo/pacote" | ❌ HTTP 429 código 1113 — idem |
| `glm-5`, `glm-5.1`, `glm-4.5-air`, `glm-4-plus` | ❌ 1113 (sem saldo) | — |
| `glm-4.7-flash` (grátis) | ✅ HTTP 200 "OK" (57.9s — reasoning lento; 1ª tentativa deu 1305 congestão, transitório) | — |

**Conclusões:**
1. Chave nova é **diferente da do cofre** (sha distintos) e **válida** (autentica).
2. **glm-5.2 EXISTE** na API (lançamento posterior ao catálogo, que parava no 5.1) — junto com `glm-5` e `glm-5-turbo`.
3. **Conta sem saldo/pacote de recursos**: toda inferência paga bloqueada (1113) — mesma situação da chave antiga (status `inativo_sem_saldo` se mantém). Para usar glm-5.2: recarregar no console open.bigmodel.cn.
4. O que funciona hoje de graça: `glm-4.7-flash` (reasoning, lento — catálogo já marca "grátis mas inútil" pra pipeline).
5. Compatibilidade técnica total com o ecossistema: endpoint OpenAI-compatible, health check `glm_zhipu` do Sentinela já monitora esse endpoint.

**Pendente decisão Miguel:** (a) recarregar saldo Zhipu? (b) se recarregar, cadastrar chave nova nos `.env` (local/Tencent/NYC — a antiga está só local) ou manter a antiga? Kimi NÃO gravou a chave nova em nenhum arquivo — aguardando orientação.

---

## 🏷️ MAPA ASSINATURA × EXTERNA — Zhipu/GLM e Kimi/Moonshot (Kimi K3, 2026-07-25 ~01:30 BRT, pedido Miguel)

**Conceito (a dúvida do Miguel):** assinatura de "Coding Plan" e saldo pay-as-you-go são **dois sistemas de cobrança separados na mesma conta**, com **endpoints de API diferentes**. A assinatura NÃO é "só pra CLI" (caso Coin/Kilo que Miguel lembrava) — **funciona como API normal para o sistema** (Sentinela, workers, escrita), desde que chamada no endpoint certo. Testado ao vivo em 25/07.

### Zhipu / GLM

| Tipo | Endpoint | Chave | Status ao vivo 25/07 |
|---|---|---|---|
| **API de ASSINATURA** (GLM Coding Plan Max, $144/mês, renova 17/ago/2026) | `https://open.bigmodel.cn/api/coding/paas/v4` | `sha8=bf908cec` (chave nova do Miguel) | ✅ **glm-5.2 HTTP 200** (4.0s). Consumo conta na quota do plano (5h/semanal/MCP — painel mostra 622.69M tokens GLM-5.2 usados pelo coding) |
| **API EXTERNA** (pay-as-you-go) | `https://open.bigmodel.cn/api/paas/v4` | mesma chave autentica | ❌ **Saldo $0** — todos os modelos pagos → erro 1113. Só grátis: `glm-4.7-flash` (funciona, reasoning lento 57.9s) |

### Kimi / Moonshot

| Tipo | Endpoint | Chave (env local) | Status ao vivo 25/07 |
|---|---|---|---|
| **API de ASSINATURA** (Kimi for Coding — plano Max) | `https://api.kimi.com/coding/v1` | `KIMI_VISION_API_KEY` `sha8=320da64b` | ✅ Modelos: `kimi-for-coding`, `kimi-for-coding-highspeed`, `k3`, `k3-256k`. **k3 HTTP 200** (2.6s). **Já em uso no sistema**: juiz visual do worker V4. Exige `temperature=1` |
| **API EXTERNA** (pay-as-you-go, saldo ~$22) | `https://api.moonshot.ai/v1` | `KIMI_API_KEY` `sha8=05fba1d7` | ✅ `kimi-k2.6` HTTP 200 (2.2s), `moonshot-v1-8k` OK (1.0s). Modelos novos exigem `temperature=1`. ⚠️ `kimi-k3` externo: HTTP 200 mas **content vazio** (141 tokens — padrão §66 reasoning consumindo; usar k2.6 em vez de k3 na externa até investigar) |

### Regras práticas derivadas

1. **Sentinela/loops podem usar as assinaturas** — estão dentro do direito de uso (são APIs documentadas do plano). A quota é a do plano (GLM: 5h/semanal/MCP; Kimi: quota Max) — monitorar no painel do fornecedor, não é ilimitado.
2. **Nunca confundir endpoint:** chave de assinatura no endpoint pay-as-you-go (ou vice-versa) dá erro enganoso (1113 "sem saldo" no Zhipu, 404/auth no Kimi) — o erro mente a causa.
3. **Modelos Kimi novos (k3, k2.6) exigem `temperature=1`** — outro valor → HTTP 400 "invalid temperature".
4. Health check Sentinela `glm_zhipu` testa o endpoint **pay-as-you-go** (`/paas/v4/models`) — autenticação OK mas não reflete a assinatura. Se o ecossistema adotar glm-5.2 via coding plan, o health precisa apontar para `/coding/paas/v4`.

---

## 🏷️ MAPA ASSINATURA × EXTERNA — Alibaba/Qwen (ZCode/GLM-5.2, 2026-08-01 ~16:30 BRT, pedido Miguel)

**Conceito (a dúvida do Miguel):** "vale assinar o Token Plan (Standard/Pro) do Model Studio pra usar a API no site Cafezinho em vez de pay-as-you-go?" — mesma classe de confusão do mapa Zhipu/Kimi acima, agora na Alibaba. Análise completa: `Foruns/forum_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md` + `Memorias/memoria_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md`.

**Veredito:** 🚫 **NÃO assinar o Token Plan para uso no site Cafezinho.** É produto para ferramentas de coding/agente (Claude Code, Cursor, Cline), não para backend de site em produção. A trava sentido pelo Miguel é saldo do pay-as-you-go; remédio = recarregar pay-as-you-go (ou resource package / Savings Plan se volume justificar).

### Alibaba / Qwen

| Tipo | Endpoint | Status ao vivo 01/08 |
|---|---|---|
| **API EXTERNA (pay-as-you-go)** — ATUAL, a que funciona | `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` | ✅ `QWEN_API_KEY` (`3af892f5`) texto+visão OK (smoke 01/08, ver `forum_qwen_alibaba_contas_20260801.md`) |
| **API de ASSINATURA (Token Plan — Pessoal Lite/Standard/Pro; Equipe)** | `https://token-plan.cn-beijing.maas.aliyuncs.com/apps/{workspaceId}/...` (região fixa cn-beijing) | 🚫 **Não serve para o Cafezinho** — exige endpoint dedicado + key dedicada + região Pequim; tem janela 5h/7d com **pausa de serviço**; concorrência máx 6-8 agentes; Credits não acumulam; coeficiente por modelo |

### 4 travas técnicas fatais do Token Plan (fonte: página oficial `token-plan-overview`, atualizada 2026-07-27)

1. **Endpoint próprio obrigatório** — "必须使用其专属 Base URL"; senão, cobra pay-as-you-go silenciosamente.
2. **Região Pequim obrigatória** — "目前仅支持华北2（北京）地域".
3. **Janela 5h + 7d com PAUSA de serviço** — "累计消耗达到限额后暂停服务"; derrubaria o Tribunal Visual imprevisivelmente.
4. **Credits não acumulam + concorrência limitada** — "未用完的额度不结转"; Pro = 6-8 agentes vs chamadas paralelas do Cafezinho.

### Padrão arquitetural consolidado (3ª ocorrência — Zhipu, Kimi, Alibaba)

Todas as clouds chinesas de IA mapeadas separam **assinatura** (endpoint dedicado, quota do plano, ferramenta de coding/agente) de **pay-as-you-go** (endpoint DashScope-like, por token, sem janela). A confusão é sistemática. **Regra derivada:** ao avaliar qualquer assinatura de cloud chinesa de IA, sempre verificar (1) endpoint dedicado exigido, (2) se permite chamada externa/produção ou só IDE/playground, (3) janelas e pausas de serviço.

### O que resolve a trava (em vez de Token Plan)
- **Opção A (recomendada):** recarregar pay-as-you-go do Qwen / comprar **resource package (资源包)** — não mexe em código, endpoint nem região.
- **Opção B:** **Savings Plan (节省计划)** se gasto alto e estável — desconto escalonado mantendo endpoint pay-as-you-go.
- **Critério:** gasto Qwen < ¥139/mês → só A; ≥ ¥139 e estável → A + B. Medir gasto real antes (pendente).

---

## 🕵️ VIGÍLIA DE CRÉDITO ZCode + quota Kimi Code mapeada (Qwen Token Plan/qwen3.8-max, 2026-08-07 ~12:30 BRT)

Tema Duplo: `Foruns/forum_vigilia_credito_zcode_20260807.md` + `Memorias/memoria_vigilia_credito_zcode_20260807.md`.

**O que se descobriu ao vivo (07/08):**
- **Kimi Code NÃO tem API de quota** (`/usage` etc. → 404). Assinatura de esgotamento = **HTTP 403 `access_terminated_error`** ("You've reached your usage limit for this billing cycle") — não consome crédito. ZCode registra como `error_type='auth_failed'` no `model_usage` do `~/.zcode/cli/db/db.sqlite`.
- **Orçamento por ciclo de 5h (auto-calibrado pelo banco do ZCode):** regime pesado 06–07/08 = 75M–221M tokens in+out por ciclo (mediana ~123M); 12 episódios de esgotamento desde 20/07.
- **Existem DUAS chaves Kimi Code vivas:** a do provider ZCode "Kimi 3" sha8 `92aed0f2` e a do cofre `kimi_code.env` (`KIMI_CODE_API_KEY`) sha8 `6dcfcad3` — ambas válidas, ambas esgotadas em 07/08 (contas/assinaturas possivelmente distintas → candidato a rodízio de chave; testar com crédito vivo).
- **Qwen Token Plan do Miguel (assinado 07/08, LITE)** usa endpoint **`token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1`** (região Singapura — o mapa de 01/08 acima documentava só o cn-beijing; o produto internacional existe). Também tem janela 5h/7d → monitorado pela mesma vigília.

**O que ficou armado:**
- `~/.zcode/hooks/credito_vigilia.py` (`--status/--hook/--probe/--json`) + hooks `UserPromptSubmit`/`SessionStart` (`hooks.enabled: true` em `~/.zcode/cli/config.json`) → níveis 🟢🟡🟠🔴 injetados em todo prompt; 🟠 = checkpoint no Cérebro antes de esgotar; 🔴 = failover Kimi K3 → Qwen Token Plan (`qwen3.8-max`) → GLM-5.2. Protocolo permanente em `~/.zcode/AGENTS.md` seção "🕵️ VIGÍLIA DE CRÉDITO". **Adendo 29/08:** xAI Grok prepaid entra no mesmo cabeçalho (token `MONITOR_GROK` / Management API, time cafezinho; smoke US$ 7,99).
- Cron `*/15` faz probe só em provedor esgotado (custo zero) e avisa no Telegram (Ponte Cafezinho) quando a janela renova.
- **16/08/2026: FAILOVER AUTOMÁTICO NO AR** — `~/.zcode/hooks/llm_fallback.py` troca sozinho automações/sessão viva/default quando um provedor cruza 90% da cota (5h ou semanal) ou esgota; cadeia Kimi→Qwen→GLM→DeepSeek; reversão automática <75%. Detalhes: adendo 16/08 em `Foruns/forum_vigilia_credito_zcode_20260807.md`.
- **Regra 4:** `KIMI_CODE_API_KEY_ZCODE` (sha8 `92aed0f2`) gravada nos 3 cofres; `KIMI_VISION_API_KEY` (sha8 `320da64b`) espelhada ao cofre canônico (só estava no espelho). Backups `.bak_pre_vigilia_20260807_1221`.

---

## 🏷️ CONFIG GLM-5.2 (Z.ai Coding Plan) no ZCode + investigação Vigília (GLM-5.2, 2026-08-07 ~13:55 BRT, pedido Miguel)

Tema Duplo: `Foruns/forum_config_glm52_zai_coding_plan_vigilia_20260807.md` + `Memorias/memoria_config_glm52_zai_coding_plan_vigilia_20260807.md`.

**Pedido:** configurar a chave nova do GLM-5.2 no ZCode ("não estou conseguindo configurar") + adicionar o % do GLM na Vigília de Crédito (como já há p/ Kimi/Qwen).

**Causa raiz do "não configurava":** o provider "Z.ai API" (`e488030c…`) já tinha a chave nova do Miguel, mas apontada pro **endpoint pay-as-you-go** (`/api/paas/v4`) → erro `1113` "sem saldo". A chave era de **assinatura (Coding Plan)**; chamada no endpoint errado. **Mesma classe de confusão dos Mapas Assinatura × Externa** acima (Zhipu/Kimi/Alibaba). Cuidado extra no ZCode: os providers built-in vêm com baseURL pré-preenchida que pode ser pay-go.

**Correção aplicada em `~/.zcode/v2/config.json`** (backup `.bak_pre_zai_glm52_config_20260807_1353`):

| Provider | Mudança |
|---|---|
| "Z.ai API" (`e488030c…`) | baseURL `/api/paas/v4` → **`/api/coding/paas/v4`** |
| `builtin:zai-coding-plan` (Anthropic-native, `enabled:true`) | apiKey `0e3373ea` → `084efcbd` |
| `builtin:zai` (Anthropic-native) | apiKey `bf908cec` (conta $0 desde 25/07) → `084efcbd` |

**Endpoint de assinatura Z.ai = 2 variantes** (ambas HTTP 200 com a chave nova `sha8=084efcbd`):
- OpenAI-compatible: `https://api.z.ai/api/coding/paas/v4` (intl) / `https://open.bigmodel.cn/api/coding/paas/v4` (CN)
- Anthropic-compatible (nativo do agente ZCode): `https://api.z.ai/api/anthropic`

**Modelos no plano:** `glm-4.5`, `glm-4.5-air`, `glm-4.6`, `glm-4.7`, `glm-5`, `glm-5-turbo`, `glm-5.1`, `glm-5.2`. **GLM-5.2 validado em 6 testes** (chat + Anthropic; minúsculas e MAIÚSCULAS — formato exato do ZCode). Miguel já trocou o seletor; usa GLM-5.2 nesta conversa.

**Investigação Vigília — GLM tem API de quota?** Sondados 11 endpoints (`/usage`, `/quota`, `/billing`, `/subscription`, `/user/info`, `/account`, `/me` em coding/paas/v4 + paas/v4 + anthropic/v1): **TODOS 404**. **Z.ai NÃO tem API de quota** — mesmo padrão Kimi. O % do GLM na Vigília será **estimado por consumo de tokens** (janela rolante 5h + auto-calibração por ciclos de esgotamento), igual Kimi/Qwen. **Implementação pendente** (spec pronta na memória §5; cadeia de failover revisada p/ cíclica: Kimi K3 → Qwen → GLM → Kimi).


## ⚠️ ADENDO 2026-08-07 ~19:00 — k3-256k / top-up Kimi ESGOTADO (política revogada)

- Painel Kimi: **consumo $19,75 no mês, saldo $0,25** — o top-up queimou em <24h de uso de agente de código (contexto grande por turno). **Miguel: "definitivamente não vale a pena usar crédito extra".**
- **REVOGADA** a política "preferir k3-256k p/ código/gestão" (criada 07/08 18:15 pela sessão GLM). `k3-256k` segue no config (1 clique de reversão), mas **não usar** — saldo zerado.
- **Cadeia de failover vigente:** Kimi K3 assinatura → **Qwen Code (Token Plan)** → GLM-5.2. Sem top-up no meio.
- Referência: Tema Duplo `*_k3_256k_modelo_economico_kimi_topup_20260807` (criação) + `forum_midia_ouro_prioridade_nome_identificado_20260807` (adendo do esgotamento).

### 🔍 Auditoria de gasto + mapa de chaves DeepSeek (24/08/2026)
- Tema Duplo: `Foruns/forum_auditoria_gasto_deepseek_chaves_moka_20260824.md` + `Memorias/memoria_auditoria_gasto_deepseek_20260824.md`
- Gasto 18-24/08 (US$ 182,97): "moka reader" US$ 101 (BYOK do Miguel no navegador, v4-pro, Reader reenvia ~418k tokens/página) · "z code api" US$ 75 (pico 18-19/08, contido pelo failover→GLM) · temáticos/V4 ~US$ 7.
- Repos moka/moka-espelho PÚBLICOS no GitHub, varridos e LIMPOS (histórico + AAB Play Store). Chaves DeepSeek atuais mapeadas por máscara no fórum (§2) — usar na rotação.

### 🖼️ Sessão Ponte de Imagens V4 (ZCode Dell): GLM-5.3 com fallback DeepSeek (27/08/2026)
- Ordem do Miguel 27/08 ~12:10: a sessão da ponte de imagens fica no **GLM-5.3**, com **DeepSeek de fallback** (não volta pro Qwen — plano esgotado; a linha 🔴 do Qwen no cabeçalho da vigília é STATUS do plano dele, não o modelo da sessão).
- ⚠️ Limitação conhecida do fallback: **DeepSeek NÃO tem visão** (Read de imagem devolve `[Unsupported Image]` — memória 26/08). Nesta sessão, o PASSO 3.5 (ver a imagem, REGRA-MÃE) NÃO roda no DeepSeek: se cair no fallback durante caça, o trabalho VISUAL pausa/escala (tribunal no NYC segue de pé) e o Miguel é avisado para religar GLM/Qwen renovado; todo o resto (varreduras, WP, patrulha YT, registros) roda normal no DeepSeek.
- Failover continua MANUAL no app (ordem 25/08 vale): isto é roteamento operacional da missão, não auto-failover.

### 👁️ Teste de VISÃO por chave — GLM NÃO serve, DeepSeek SERVE (28/08/2026)
- Ordem do Miguel 28/08 ~09:40: testar as chaves dele nos modelos de visão p/ uso no Cafezinho (enxergar personagem/notícia).
- **GLM (assinatura Z.ai Coding Plan + 2 contas):** chaves VÁLIDAS p/ texto (10 modelos glm-4.5→glm-5.3-flash, 200), mas `glm-4.5v`/`glm-4.6v` retornam **429 "Insufficient balance or no resource package"** em TODAS as 3 contas e bases — a assinatura NÃO inclui pacote de visão. Só recarregando.
- **DeepSeek (`deepseek-v4-flash-vision-exp`, 21/08):** ✅ chave do saldo funciona; acertou Lula 2/2 (foto do post 267802); ~US$0,0003 por análise de capa (imagem ≤384 tokens; 0,22/0,66 por 1M off-peak); é modelo de raciocínio → `max_tokens ≥ 300`.
- **Qwen-VL (referência):** errou 1× com prompt longo (Lula→Bolsonaro), acertou 2/2 com pergunta curta.
- Tema Duplo: `Foruns/forum_visao_chaves_glm_deepseek_qwen_20260828.md` + `Memorias/memoria_visao_chaves_glm_deepseek_qwen_20260828.md`.
- **✅ DEPLOY 28/08 ~13:40 (ordem "vai"):** vision-exp PLUGADO no pipeline visual do NYC (`media_vision_providers.py`): DeepSeek 1º + dupla-checagem Qwen (divergência → ambiguous+menor confiança); ativado automaticamente pelo `DEEPSEEK_API_KEY` do `/root/.env.unificado` (retrocompatível). Memória técnica: `memoria_visao_deploy_deepseek_vision_nyc_20260828.md`.

### 💸 FREIO DE GASTO DEEPSEEK — todos os DS em deepseek-flash (11/09/2026)
- Ordem Miguel 11/09 ~09:1x: "muda todos os DeepSeeks dos DS para Lite" + ronda DS Miguel 4/4h. **Lite = `deepseek-flash`** (a conta só expõe `deepseek-flash` e `deepseek-v4-pro` em `/models`; não existe id "deepseek-lite").
- Aplicado em: `~/.dsh/settings.yaml` Dell+Tencent (flash+reasoning low), `dsn_revisor1/2.py`, `escuta.py` do Chefe, `dsn_router.py` (degrau v4-flash→flash; mantidos `deepseek-v4-pro` p/ complexo e `deepseek-v4-flash-vision-exp` p/ visão). Crons das rondas Dell+Chefe: `0 */4`. Backups `.bak_pre_freio_ds_20260911`.
- 🔴 Chaves DeepSeek (Dell ****806b, Tencent ****8762) "invalid" desde ~09:30 de 11/09 — parque parado; vigia P11 bug do log corrigido (`est["falhas"]`).
- Vazadores medidos: ronda DS Miguel 48/dia (v4-flash+high) · transcriber US$ 6 numa transcrição de 1h (Transkriptor URL-direto, sem teto) · fábrica V4.1 7d US$ 31 (v41_ciclo 67%). Verticais/temáticos: zero.
- Tema Duplo: `Foruns/forum_freio_gasto_deepseek_20260911.md` + `Memorias/memoria_freio_gasto_deepseek_20260911.md`.

### 🚨 PLANO DE EMERGÊNCIA 4 NÍVEIS + chaves DeepSeek NOVAS (11/09/2026)
- Níveis PRO(20-30 posts/dia)/BÁSICO(5-6)/MÍNIMO(2-3)/ZERO — troca: `ssh tencent '/home/ubuntu/bin/plano_uso.sh {status|pro|basico|minimo|zero}'`. **MÍNIMO ATIVO desde 11/09 ~10:00.**
- Chaves DeepSeek regeneradas pelo Miguel 11/09: **canônica** sk-a20c… (sha8 2b0569ed; NYC chaves.sh+.env.unificado, cofres Dell) e **DSN** sk-3d49… (sha8 f5ee9259; tencent deepseek_env+.env.unificado; robôs pausados). **Mesma conta — saldo único** (US$ 4,25 às 09:49; P11 vigia a canônica e cobre tudo). Velhas ****806b/****8762 inválidas — só nos `.bak_pre_chave_ds_20260911`.
- Fios de gasto invisível cortados: `monitor_chaves_api --test-api` (chamada real por chave ×96/dia) e `agente_validador_modelos` (testes reais diários, comentado).
- Tema Duplo: `Foruns/forum_plano_emergencia_4_niveis_20260911.md` + `Memorias/memoria_plano_emergencia_4_niveis_20260911.md`. Veja também `forum_freio_gasto_deepseek_20260911.md` (flash/Lite em todos os DS).
