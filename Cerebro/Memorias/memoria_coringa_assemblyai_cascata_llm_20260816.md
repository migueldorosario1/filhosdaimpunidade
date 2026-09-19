# Memória técnica — Coringa AssemblyAI nas cascatas LLM (16/08/2026)

> Fórum: `Foruns/forum_coringa_assemblyai_cascata_llm_20260816.md`. Ordem Miguel 16/08 ~23:50 ("não pode nunca depender de um LLM só… inclusive o coringa assembly"). Execução: ZCode/Qwen 3.8.

## Contexto/porquê

Na noite de 16/08 a conta Kimi paygo amanheceu SUSPENSA (HTTP 429). A confirmação do Jornal da Fórum era Kimi-só e quase quebrou; foi criada a cascata DeepSeek→Kimi. O Miguel então generalizou a regra: **nenhuma chamada LLM pode depender de um só provedor**, e lembrou do coringa disponível — o gateway AssemblyAI (decisão já tomada em 01/08: "AssemblyAI entra como coringa de todos os V4", mas nunca integrada de fato).

## O coringa (dados operacionais)

- **Endpoint:** `https://llm-gateway.assemblyai.com/v1/chat/completions` (formato OpenAI Chat Completions).
- **Conta:** pay-as-you-go; saldo US$ 47,75 em 29/05; autopay ativo. Preços por 1M tokens (docs 29/05): Claude Opus 4.7 $5,50/$27,50 · Sonnet 4.x $3/$15 · **Haiku 4.5 $1/$5** (default escolhido) · gpt-oss-120b $0,15/$0,60.
- **Chave:** variável canônica `ASSEMBLYAI_API_KEY` no cofre local `Projeto Cafezinho Agentes/root/.env.unificado`; sha8 `77f59e59` = chave mestra validada no Tencent em 29/05. `ASSEMBLY_API_KEY` = espelho de mesmo valor (mantida: `scratch/.../agente_roteador_llm.py` ainda lê o nome antigo). Conta no painel AssemblyAI; custo contabilizado como `assemblyai_gateway:<modelo>` (acerto Codex 29/05, `root/agent_data/precos_modelos.json`).
- **Default do modelo:** `claude-haiku-4-5-20251001` (o mais barato da família validada no smoke original); override por env `ASSEMBLYAI_GATEWAY_MODEL`.

## Mudanças (com backups `.bak_pre_coringa_assembly_20260816`)

### 1. `agentes_tematicos/v4/nucleo_llm.py`
- `PROVIDERS["assemblyai"]`: base `https://llm-gateway.assemblyai.com/v1`, modelo via env-default acima, `key_env: ASSEMBLYAI_API_KEY`, `key_env_alt: ASSEMBLY_API_KEY`.
- `CADEIA_PADRAO = ["deepseek", "kimi", "glm", "qwen", "openai", "assemblyai"]`.
- Comportamento herdado por todos os consumidores do roteador: `gerar`/`gerar_json` tentam a cadeia em ordem e só chegam no coringa se tudo antes falhar (fallback silencioso com log de erros interno).

### 2. `agentes_tematicos/v4/config/llm_tiers.json`
- `superluxo` (usado pela redação do agente YouTube): `["openai_gpt55","openai","deepseek","kimi","glm","qwen","assemblyai"]`.
- `padrao`: `["deepseek","kimi","glm","qwen","openai","assemblyai"]`.

### 3. `Projeto Cafezinho Agentes/agentes_cafezinho/youtube_cafezinho.py`
- `_chat_json_cascata()` (confirmação do Jornal da Fórum, `_jornal_confirmar_llm`): ordem agora **DeepSeek → AssemblyAI → Kimi paygo**. Chave do coringa resolvida por `get_key("ASSEMBLYAI_API_KEY") or get_key("ASSEMBLY_API_KEY")`. Modelo default do gateway idem, com override por env.
- `_kimi_chat_json()` ficou sem chamadores (código morto; manter por ora para referência do payload com `thinking: disabled`).

## Provas (16/08 ~23:55)

1. **Smoke real isolado:** `nucleo_llm.gerar("Responda apenas: OK", cadeia=["assemblyai"])` → `texto='OK'`, `provider='assemblyai'` (HTTP 200; custo ~16 tokens).
2. **Stub da cascata do Jornal:** `requests.post` fake — deepseek 500 → assemblyai 200 com JSON → resultado `_provider='assemblyai/claude-haiku-4-5-20251001'`; ordem de tentativas registrada: `api.deepseek.com` → `llm-gateway.assemblyai.com`. Kimi não chegou a ser chamado.
3. `python3 -m py_compile` verde em `nucleo_llm.py` e `youtube_cafezinho.py`; `llm_tiers.json` parseia.

## Decisões registradas

- **Posição do coringa = sempre último** (é o único elo que queima dólar por chamada; tudo antes é plano/cota).
- Modelo default = Haiku 4.5 (custo/qualidade para fallback de classificação/JSON); nada impede override pontual por env.
- Não se mexe em `scratch/reuniao_trindade_v4_20260809/agente_roteador_llm.py` (legado; diretriz Codex 07/05 segue valendo para aquele arquivo).

## Pendências/futuro

- Levar o mesmo padrão ao GSN V2 no NYC (varrer chamadas single-provider lá) — opcional, próxima sessão.
- Se a conta Kimi paygo for declarada morta em definitivo: remover `_kimi_chat_json`/passo Kimi e a chave do cofre (Regra 4).
- Fórum do gateway original: `Foruns/forum_assemblyai_gateway_20260609.md`; Sobrenatural: `Foruns/forum_sobrenatural_assemblyai.md`.

— ZCode (Qwen 3.8), 16/08/2026 ~23:55 BRT
