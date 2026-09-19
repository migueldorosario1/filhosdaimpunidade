# 🧠 MEMÓRIA — Estratégia de modelos do ZCode: DECISÃO do Miguel (25/08/2026)

**Criada:** 2026-08-25 ~12:58 BRT · ZCode/DeepSeek
**Fórum-irmão:** `Foruns/forum_estrategia_modelos_zcode_decisao_20260825.md`

## Log técnico do sprint (tudo executado hoje nesta sessão)

**Arquivos tocados:**

1. `~/.zcode/v2/config.json` — provider novo `6ff9b527-db32-44ee-a0e4-0030d69853a2` "OpenAI (GPT-5.6)": kind `openai-compatible`, baseURL `https://api.openai.com/v1`, modelos `gpt-5.6-sol`/`-terra`/`-luna` (contexto 1M, saída 128K), override reasoning p/ Sol. Backup: `.bak_pre_openai_gpt56_20260825_1251`.
2. `Outros/chaves/agentes_labs/.env.unificado` + `Projeto Cafezinho Agentes/root/.env.unificado` — `ZCODE_OPENAI_API_KEY` (sha8 `8035a022`) anexada com cabeçalho; backups `.bak_pre_zcode_openai_20260825`. Origem: `~/cofre_intake/cofre_intake.env` (`ZCODE_OPENAI`).
3. `Cerebro/CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md` — linha Kimi Allegretto: 🔴→✅ (US$ 31 anual / US$ 39 mensal; tabela completa dos 4 planos).
4. `Cerebro/CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` — seção nova GPT-5.6 (preços oficiais + benchmarks).
5. `Cerebro/CEREBRO_NODE_COFRE_CHAVES.md` — seção nova ZCODE_OPENAI (GPT-5.6 Sol).
6. `Cerebro/CEREBRO_NODE_ATUALIZACOES.md` — 2 entradas (12:30 preços Kimi; 12:55 provider Sol).
7. `Cerebro/MONITORAMENTO_DE_TRABALHO.md` — linha da missão marcada ✅.
8. Este Tema Duplo (fórum + memória).

**Provas (smokes ao vivo, sem exposição de segredos):**

- Chave OpenAI nova: `GET /v1/models` HTTP 200, 126 modelos, família 5.6 visível.
- `gpt-5.6-sol` chat: HTTP 200, resposta "OK", 16/4 tokens.
- DeepSeek V4 Pro na sessão: turno `msg_mt8uhr0e` completado (provider `397f633c`, 127.205 in / 1.109 out, ~26s, ~US$ 0,06) — lido em `model_usage` do `~/.zcode/cli/db/db.sqlite`.
- Websearch com DeepSeek ativo: cotação do dólar 25/08 retornada ao vivo (R$ 5,1481 meio-dia).

**Preços que ancoram a decisão (fontes oficiais 25/08):**

- DeepSeek V4 Pro: $0,435 / $0,87 por 1M (cache ~$0,014).
- GPT-5.6 Sol: $4 / $20 (cache $0,40) — PROMOCIONAL até ≥21/11/2026; Terra $2/$12; Luna $0,20/$1,20.
- Kimi: Moderato $15/$19 · Allegretto $31/$39 · Allegro $79/$99 · Vivace $159/$199 (anual/mensal; créditos lineares 1×/2×/5×/10×).
- Benchmarks Sol: Terminal-Bench 2.0 #1 (91,9%) · SWE-bench Pro 64,6% (qwen3.8-max 67,7%) · Coding Agent Index líder 80 pts.

**O que aconteceu / o que falta / o que preciso de você (Miguel):**

- **Aconteceu:** estratégia decidida (DeepSeek = principal via API; Kimi fora) e infra pronta (Sol plugado, chave espelhada, preços e benchmarks no Cérebro).
- **Falta:** (1) recarga DeepSeek (US$ 50-100 sugeridos; saldo US$ 23,97); (2) cancelar renovação do Kimi; (3) OK opcional p/ incluir DeepSeek na cadeia do `llm_fallback.py`; (4) manter Qwen Lite como reserva (US$ 6)?
- **Preciso de você:** só os itens 1 e 2 (dinheiro/renovação são suas contas); 3 e 4 eu resolvo com um "pode".
