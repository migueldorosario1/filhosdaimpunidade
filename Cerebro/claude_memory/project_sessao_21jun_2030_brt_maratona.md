---
name: project-sessao-21jun-2030-brt-maratona
description: Pausa sessão Ming 21/06 20:30 BRT após 22h+ contínuas (iniciada 22:08 BRT 20/06). 44 ticks §53 · 15 curas §51 · 6 patches §92 + 1 §111 standby AGY + 1 patch §92 bug TZ YT V2 pendente · 4 publishes varredura drafts · 3 curas editoriais retroativas · tutorial AssemblyAI · carta AGY endossada · 2 memórias editoriais novas.
metadata: 
  node_type: memory
  type: project
  originSessionId: f312988d-5dc6-4ea6-b08a-94b4cada57ec
---

🌙 **Pausa sessão Ming 21/06 20:30 BRT** após maratona 22h+ contínuas (iniciada 22:08 BRT 20/06).

**Why:** Miguel pediu "grava sessão" 20:28 BRT após dia denso de patches estruturais + tutorial AssemblyAI + curas + diretrizes editoriais novas + investigação YT V2 timezone bug.

**How to apply:** Ao retomar, ler MEMORY.md + tail canal_trindade + esta memória + relatório `relatorio_monitoramento_20260621_loop53_30min.md`. Pendências críticas Miguel decidir:
- **#19**: Deploy patch §111 combinado (Ming cleanup regex + AGY dedup SQLite) — 4 §92 cheios em `util_gate_pesquisas.py` + `motor_coletor.py:270` + `agente_eleicoes.py:663` + `motor_publicador.py:2572+2576`. AGY endossou e está aguardando ack pra começar
- **#21 NOVO**: Patch §92 1-linha SQL em `agente_youtube_v2_publicador.py:_count_publicados_hoje()` trocar `date('now')` por `date('now','-3 hours')` (bug timezone UTC vs BRT — cap diário 4 estourou às 21:00 BRT por causa dos posts da véspera 21h-24h BRT que caem em "21/06 UTC")
- **#18**: Promover ou manter pending #260122 + #260125 (Flávio+Vorcaro, Wagner+Master). Editorialmente alinhados mas pending = semântica WP "aguardando aprovação editorial"
- **#20**: Promover ou manter draft #260127 (4ª Datafolha mas com ângulo único `leitura_editorial_especifica`)

**Realizações da sessão (22h):**

### Patches §92 cheios deployados Tencent (6+1)
1. `.env.unificado`: +ZHIPU_API_KEY (Z.ai Coding Plan)
2. `agente_roteador_llm.py`: qwen-max→qwen-plus + Zhipu endpoint api.z.ai + glm-4.6 + AssemblyAI coringa em TODAS chains
3. `fact_check_perplexity.py`: qwen-max→qwen-plus
4. `agente_certificador_qualidade.py`: glm-5.1→glm-4.6 + endpoint api.z.ai
5. `auditor_texto.py` (Sistema REFORMA): qwen-max→qwen-plus
6. `agente_comentarista.py` (Tencent 22:51 BRT 20/06): manchete 12→random(15,30) — backup `.bak_pre_manchete_15a30_20260620_2334`
7. **STANDBY**: gate §111 pesquisas eleitorais (AGY endossou, aguarda sanção Miguel)
8. **STANDBY**: bug TZ YT V2 cap diário (descoberto 19:30 BRT 21/06, aguarda sanção)

### Curas §51 aplicadas (15 totais na sessão)
- 20/06: #259974 anacronismo §110 (pending→draft)
- 21/06: #260014 (Estrito→Estreito), #260017 §107, #260022 §51, #260042 §107, #260046 sobrenatural, #260048 sobrenatural, #260052 §107, #260087 §107, #260096 §107, #260104 §107 (5ª), #260131 §107 (6ª/7ª), #260139 §107 (8ª)
- Cat 19936 fallback: #260130 esquartejado, #260135 motociclista, #260141 UFAC violência mulher, #260137 Hezbollah/Israel
- **Padrão §107 confirmado**: 8 ocorrências, 6+ envolvem família Bolsonaro (Carlos/Flávio) — bug chave canônica `agente_flavio_bolsonaro.py` em `AGENTES_HARD_HOME` que tem só `"flavio"`

### Varredura drafts (4 publicados + 1 mantido)
- #260058 China índio (cura §107) + #260063 México + #260078 Lula 10pts + #260084 Flávio+IA+PT (publicados)
- #260053 mantido draft (alucinação meta "Politica V2" — teste sprint PASSO 3-A)

### Curas editoriais retroativas (3)
- #260078 ("Como reportou o Metrópoles" removido)
- #260109 ("Levantamento da Carta Capital" → "Agregação de três institutos")
- #260127 ("A íntegra foi publicada pelo Metrópoles" removido)

### Diretrizes editoriais novas (2 memórias)
- `feedback_pesquisas_fonte_primaria_sem_repercutidor`: NUNCA citar veículo intermediário em matéria de pesquisa
- `feedback_cooldown_pesquisas_eleitorais`: cooldown 24h por (instituto, data_pesquisa) salvo ângulo único

### Infraestrutura validada
- **AssemblyAI Gateway coringa**: 26/27 modelos OK (1 EOL); validado em produção real durante incidente Anthropic 15:17 BRT (conta zerada $; drafts continuaram via Gateway)
- **Alibaba RESOLVIDO** (achado #5 retirado): erro meu de busca chave SSH — `Host alibaba` no `~/.ssh/config` local sempre existiu com `id_rsa`. Triplo deploy QUÁDRUPLO completo a partir do tick 13:00 BRT
- **Tutorial AssemblyAI**: `Foruns/tutorial_assemblyai_gateway_cafezinho_20260621.md` + JSON estruturado `/root/agent_data/assemblyai/health_check_20260621_1245.json`

### Health check completo 16 LLMs via API real
✅ Pipeline 100% funcional pós-recargas: Gemini, OpenAI, Anthropic Sonnet+Opus(4-1/5/7/8), xAI Grok, DeepSeek, Groq, Mistral, Perplexity, Qwen-Max/Plus, Zhipu/GLM via Z.ai Coding Plan
⚠️ Qwen3-Max 403 free tier exausto (config DashScope)
✅ Anthropic recuperou 16:17 BRT após incidente quota_exhausted das 15:17 BRT

### 8 incidentes de provider durante o dia (todos absorvidos)
- Gemini-2.5-pro/flash quota_exhausted 08:52-13:24 BRT (4h+) — coringa AssemblyAI cobriu
- Anthropic Sonnet+Haiku quota_exhausted 15:17-16:17 BRT (1h) — drafts continuaram via Gateway
- DeepSeek-V4-Pro Insufficient Balance 11:24-23:24 BRT (12h) — fallback chains absorveram
- WP API Cloudflare rate-limit transiente (×3 incidentes ao longo do dia, mitigado `sleep 10 + retry 2`)

### Carta AGY peer review
- `Foruns/carta_ming_para_agy_gate_pesquisas_eleitorais_20260621.md` (236 linhas total)
- AGY entregou parecer técnico embasado: arquitetura híbrida A+B (upstream coleta + downstream publicador), refs empíricas com linha+arquivo, código pronto ~60 linhas, SQLite shared. **Endossou patch §111 combinado**. Aguarda sanção Miguel + meu ack pra deploy.

### Bug timezone YT V2 (DESCOBERTO 19:30 BRT 21/06)
- `_count_publicados_hoje()` em `agente_youtube_v2_publicador.py` usa `date('now')` UTC
- Posts publicados 21h-24h BRT caem no "dia seguinte UTC" → cap diário estoura ANTES do dia BRT começar
- Hoje: 3 publishes 20/06 (21h-24h BRT) + 1 publish 21/06 00:04 BRT = 4 posts no "21/06 UTC" → cap 4/4 atingido às 00:04 → bloqueado dia 21 inteiro
- **Cura sugerida**: `date(updated_at,'-3 hours') = date('now','-3 hours')` (1 linha SQL)

### Identidade
Sigo como **Ming (GLM · Zhipu AI · sessão §53 local Claude Code)** pela memória `feedback_identidade_glm_nao_claude` (20/06 14:55 BRT). Miguel anotou hoje 19:00 BRT que AGY estava se referindo a "Claude" mas chamou de "Ming" — vou esperar instrução explícita Miguel pra reverter identidade se for o caso.

Aplica em conjunto com [[feedback-pesquisas-fonte-primaria-sem-repercutidor]] e [[feedback-cooldown-pesquisas-eleitorais]].
