# Coringa AssemblyAI integrado nas cascatas LLM — 16/08/2026

> **Ordem do Miguel (16/08 ~23:50):** "não pode nunca depender de um LLM só. temos uma cascata imensa, inclusive o coringa assembly."
> **Tema Duplo:** memória técnica `Memorias/memoria_coringa_assemblyai_cascata_llm_20260816.md`.
> **Decisão anterior que isto executa:** Miguel 01/08 — "AssemblyAI entra como coringa de todos os V4" (Cofre de Chaves). Faltava a integração real; agora foi feita.

## O que é o coringa

**AssemblyAI LLM Gateway** — conta pay-as-you-go (saldo US$ 47,75 em 29/05, autopay ativo), endpoint OpenAI-compatível `https://llm-gateway.assemblyai.com/v1/chat/completions`, dá acesso a vários modelos (Claude Opus/Sonnet/Haiku, GPT-OSS etc.). Chave mestra espelhada no cofre local (`ASSEMBLYAI_API_KEY`, sha8 `77f59e59` — bate com a validada no Tencent em 29/05; `ASSEMBLY_API_KEY` é espelho idêntico, mantido porque o roteador legado ainda lê).

## O que foi feito (16/08 ~23:55, ZCode/Qwen 3.8)

1. **`agentes_tematicos/v4/nucleo_llm.py`** (roteador de TODOS os V4 + agente YouTube): provider novo `assemblyai` (modelo default `claude-haiku-4-5-20251001`, configurável por `ASSEMBLYAI_GATEWAY_MODEL`) + **CADEIA_PADRAO agora termina no coringa**: deepseek→kimi→glm→qwen→openai→**assemblyai**. Backup `.bak_pre_coringa_assembly_20260816`.
2. **`agentes_tematicos/v4/config/llm_tiers.json`**: coringa no fim das duas cadeias — `superluxo` (redação do agente YouTube: gpt55→openai→deepseek→kimi→glm→qwen→**assemblyai**) e `padrao`. Backup idem.
3. **`agentes_cafezinho/youtube_cafezinho.py::_chat_json_cascata`** (confirmação do Jornal da Fórum): DeepSeek→**AssemblyAI**→Kimi paygo. Backup idem.

**Regra de posição:** o coringa é SEMPRE o último recurso (custa crédito em dólar); os provedores com cota/plano vêm antes.

## Provas

- Smoke isolado do coringa via `nucleo_llm.gerar(cadeia=["assemblyai"])`: HTTP 200, respondeu "OK" (mesmo padrão do smoke original do Codex 29/05).
- Teste stub da cascata do Jornal: DeepSeek forçado a 500 → coringa assumiu e resolveu (`_provider: assemblyai/claude-haiku-4-5-20251001`), Kimi ficou de último sem ser chamado.
- `py_compile` verde nos dois .py; JSON dos tiers válido.

## Efeito prático

Nenhuma chamada LLM do ecossistema local que passe pelo nucleo_llm depende mais de um provedor só: se TODOS os planos/cotas falharem (cenário da noite de 16/08: Kimi paygo suspenso), o gateway paga e entrega. O mesmo vale para a confirmação do Jornal da Fórum.

## Estado da missão

- **O que aconteceu:** coringa integrado nas 3 cascatas + provado em smoke real e stub.
- **O que falta:** nada obrigatório. Opcional: levar o padrão ao GSN V2 (NYC) e demais agentes que tenham chamada single-provider (varredura futura).
- **O que preciso de você (Miguel):** nada.

— ZCode (Qwen 3.8), 16/08/2026 ~23:55 BRT

## Adendo 1 — Health check da cadeia V4 (21/08/2026, ZCode/GLM-5.3)

Pedido do Miguel: "como está o health check de todos os LLMs usados no V4?" — smoke real, 1 chamada por provider do `nucleo_llm.py` (CADEIA_PADRAO + tier superluxo), executado do Dell com o cofre local (`/tmp/health_llm_v4.py`, script de análise fora do repo). Chaves presentes em todos; teste mede resposta real do endpoint.

| Provider | Modelo | Status | Latência | Detalhe |
|---|---|---|---|---|
| deepseek | deepseek-chat | 🔴 FALHA | 1,1s | HTTP 402 "Insufficient Balance" (bate com vigília: saldo US$ −1,48) |
| kimi | moonshot-v1-128k | 🔴 FALHA | 1,0s | HTTP 429 — conta org suspensa por saldo insuficiente (mesma conta já suspensa em 16/08) |
| glm | glm-4.5-flash | 🟢 OK | 1,9s | respondeu "OK" |
| qwen | qwen-plus | 🟢 OK | 3,2s | respondeu "OK" |
| openai | gpt-4o-mini | 🔴 FALHA | 0,6s | HTTP 429 "no credits remaining" |
| assemblyai (coringa) | claude-haiku-4-5 | 🟢 OK | 2,0s | respondeu "OK" — coringa vivo |
| openai_gpt55 (superluxo) | gpt-5.5 | 🔴 FALHA | 0,3s | HTTP 429 "no credits remaining" |

**Leitura:** a cascata FUNCIONA (é o desenho) — produção V4 cai para glm/qwen vivos, coringa vivo atrás. Mas hoje os 2 primeiros elos da CADEIA_PADRAO (deepseek, kimi) e TODO o flanco OpenAI (gpt-4o-mini + gpt-5.5) estão mortos por crédito: o tier `superluxo` na prática entrega glm-4.5-flash, não gpt-5.5.

**Estado da missão**
- **O que aconteceu:** health check real executado e registrado (adendo aqui + seção nova no `CEREBRO_NODE_CHAVES_E_LLMS.md`).
- **O que falta:** recargas (decisão Miguel): DeepSeek, conta moonshot do V4 (`KIMI_API_KEY`) e OpenAI — ou aceite formal de que o V4 roda só com glm+qwen+coringa.
- **O que preciso de você (Miguel):** decidir recargas. Nada quebra enquanto isso.

— ZCode (GLM-5.3), 21/08/2026 ~14:15 BRT

## Adendo 2 — Pós-recarga Miguel (OpenAI + DeepSeek): V4 destavou; gargalo restante é o PROXY IPRoyal (21/08 ~17:20 BRT, ZCode/GLM-5.3)

**Recarga do Miguel (21/08 ~14:15-14:25 BRT):** OpenAI + DeepSeek. Health check rerodado (~17:10 BRT): 🟢 deepseek-chat OK (saldo `/user/balance` = **US$ 18,51**) · gpt-4o-mini OK · gpt-5.5 OK · glm OK · qwen OK · assemblyai OK. 🔴 kimi/moonshot segue suspenso (não recarregado — não bloqueia, DeepSeek está na frente).

**Cadeia V4 Cafezinho (worker NYC) ≠ nucleo_llm dos temáticos:** o `v4_vertical_draft_worker.py` usa o `agente_roteador_llm.py` (swarm com `agent_data/modelos_vivos.json`, coringa gateway AssemblyAI). Estado de "cooldown" verificado — NADA a desligar: `falhas_modelos_runtime.json` só tem quirk `sem_temperature` do claude-opus-4-8 (não bloqueia); o "cooldown horário" (`hourly_quota` 55min global pós-draft confirmado, `--force` ignora) é cadência de DESIGN, conta sucesso, não falha.

**Por que travava ontem:** DeepSeek morto por saldo (402) + OpenAI zerada (429). NO_PROXY do NYC já cobre `api.deepseek.com` e `api.openai.com` → recarga chegou direto. **Prova de destravamento (17:18 BRT): rodada manual `v4_vertical_draft_worker.py geopolitica` → `draft_sem_imagem wp_post_id=266937` criado** (redação LLM OK; imagem ficou pending por cota IA 50%, não por LLM).

**⚠️ Gargalo restante — PROXY IPRoyal sem crédito:** `Tunnel connection failed: 402 Payment Required` no túnel HTTPS para tudo que PASSA pelo proxy (chaves.sh): `llm-gateway.assemblyai.com` (coringa do swarm) e `www.flickr.com` (busca de fotos ao vivo — provado na rodada de teste). Opções p/ Miguel: (a) recarregar IPRoyal; (b) expandir NO_PROXY com `flickr.com,llm-gateway.assemblyai.com` (não feito sem ordem — proxy existe por razão, possivelmente anti-bloqueio de IP datacenter).

**Nacional em stall por OUTRO motivo:** `v4_production_stall_alert` com last_draft_confirmed 20/08 02:50 UTC, mas causa = `no_candidate` (só 1 pauta nova; coletor `pol` trazendo pouco) — não é LLM.

**Estado da missão**
- **O que aconteceu:** recarga validada; V4 redação destavado com prova (draft 266937); cooldown verificado e INOCENTE; causa-raiz do resíduo = IPRoyal 402.
- **O que falta:** decisão Miguel sobre IPRoyal (recarregar × NO_PROXY) + pauta fraca na coleta da nacional; kimi/moonshot segue suspenso (opcional).
- **O que preciso de você (Miguel):** decidir o IPRoyal.

— ZCode (GLM-5.3), 21/08/2026 ~17:25 BRT
