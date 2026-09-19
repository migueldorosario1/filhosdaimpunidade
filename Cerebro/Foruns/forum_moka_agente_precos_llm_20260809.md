# ☕ Fórum — Agente Atualizador de Preços de LLM (ecossistema inteiro, 09/08/2026)

> Tema Duplo da missão 14 do dia 09/08 (sessão ZCode GLM-5.2).
> Commit Moka: `e7e2d86`. Agente: `Projeto Cafezinho Agentes/agentes_cafezinho/atualizador_precos_llm.py`.

## O que o Miguel pediu (voz, quase literal)

> "Esses preços que você fez, esse ranking de preços, tem que ser dinâmico — botar atualizados a cada 24 horas. Cria um agente pra atualizar esse preço. Vai ser importante pra gente usar em todo o ecossistema do Cafezinho/Mídia Group. Um bom atualizador de preço, vamos usar ele e informar o público também."

## Decisões (confirmadas via AskUserQuestion)
- **Frequência:** DIÁRIA (Miguel mudou de semanal pra diário: "peraí, acho melhor diário mesmo").
- **Onde mora:** Agente Python na Tencent root@ (padrão do ecossistema) — JSON canônico consumido por todos os sites. Miguel não respondeu a 2ª pergunta, mas disse explicitamente "ecossistema inteiro" → fora do Moka.

## Pesquisa de fontes
- **[PricePerToken](https://pricepertoken.com/)** — 300+ modelos, atualização diária, mas só MCP (não REST).
- **[OpenRouter](https://openrouter.ai/api/v1/models)** — `/api/v1/models` com preços em JSON estruturado (200+ modelos). **Usado no agente.**
- Sites oficiais: DeepSeek, OpenAI, Anthropic, Mistral, x.ai, Google AI Studio — scraping individual (fase 2).

## O que foi entregue

### 1. Agente Python `atualizador_precos_llm.py` (~280 linhas)
**Onde:** `Projeto Cafezinho Agentes/agentes_cafezinho/atualizador_precos_llm.py`.
- **Tabela canônica** (`MODELOS_CANONICOS`): 18 modelos com preços verificados contra `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md`.
- **Scraping:** OpenRouter `/api/v1/models` (JSON) + DeepSeek (placeholder parse, fase 2).
- **Cotação USD→BRL:** AwesomeAPI (`economia.awesomeapi.com.br`).
- **Saída:** `/root/agent_data/precos_llm/ranking_llm.json` com `{updated_at, usd_brl, modelos[], fonte}`.
- **Diff:** detecta mudanças vs. versão anterior, loga `[NOVO]`/`[ALT]`.
- **Padrão ecossistema:** script `.py` solto, `source /root/.env.unificado`, `flock`, logs em `agent_data/`.
- `py_compile` verde.

### 2. LEIA-ME com instruções de deploy
**Onde:** `LEIA-ME_atualizador_precos_llm.md`. Cron sugerido: `0 9 * * *` (09:00 UTC / 06:00 BRT) na Tencent root@.

### 3. Moka consome JSON dinâmico (`llm-prices.ts`)
- `fetchLlmPrices()`: fetch com cache 24h (localStorage `moka.llmPricesCache`); fallback hardcoded (`LLM_PRICES`) se rede falhar.
- `LLM_PRICES_DYNAMIC_URL = ""` (vazio) — só fallback até o Miguel publicar o endpoint do agente.
- Conversão de formato: `{id, nome, preset_id, input_usd, output_usd}` → `{modelo, presetId, inUsd, outUsd}`.

### 4. LlmPriceRanking mostra "atualizado em"
- `useState` + `useEffect`: busca preços dinâmicos no mount.
- Mostra "↻ Preços atualizados em DD/MM/AAAA" quando os dados vêm do agente.
- Chave i18n `rank_updated` ×12 idiomas.

## Estado
- ✅ **ENTREGUE E NO AR:** commit `e7e2d86` (push `5503413..e7e2d86`), Moka deploy Vercel.
- ✅ Agente Python criado + LEIA-ME; `py_compile` verde.
- ✅ Moka consome dinâmico (fallback ativo até endpoint público).
- ⏳ **Pendências (fase 2):**
  1. **Deploy do agente na Tencent** (SSH root@) — Miguel ou sessão de servidor roda o `scp` + `crontab -e`.
  2. **Endpoint público do JSON** — Miguel escolhe: (A) commitar `ranking_llm.json` num repo → raw.githubusercontent; (B) nginx Tencent; (C) Vercel edge. Quando escolher, preencho `LLM_PRICES_DYNAMIC_URL` no Moka.
  3. Scraping individual de cada provedor (hoje só OpenRouter + tabela).

## Próximos passos (fase 2)
- Commit automático do agente nos repos consumidores (Aiatolah `ranking.json`).
- Notificação no Telegram quando o agente detectar mudança de preço.
- Alan (robô de ajuda) reusa os preços ao explicar custos.
