---
name: feedback-gpt-revisor-camada-tripla
description: "3ª camada de revisão via GPT (após DeepSeek, antes de Claude). Cap 10/dia + preferência horário pico BRT 08-11+14-19. Rotação 3 modelos baratos. Miguel 2026-08-03 14:00 BRT."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9ff9d002-2c71-4670-87db-7c5f55616550
---

**Regra:** Depois do DeepSeek revisor rodar, se `should_call()==True`, chamar GPT como 2ª opinião. Claude tem a palavra final após WebSearch.

**Ordem oficial:** DeepSeek (sempre) → GPT (~10x/dia, pico prefer.) → Claude (WebSearch + decisão final).

**Script:** `/home/migueldorosario/ferramentas/sentinela/gpt_revisor.py`

**Chave:** `OPENAI_API_KEY_REVISOR` no `.env` — chave exclusiva pra esta função (Miguel criou 2026-08-03).

**Modelos em rotação (baratos):**
- `gpt-5-mini` — US$ 0.25/M in, 2.00/M out — mais novo, reasoning bom mas latência 30-40s
- `gpt-4.1-mini` — US$ 0.40/M in, 1.60/M out
- `gpt-4o-mini` — US$ 0.15/M in, 0.60/M out — mais barato e rápido

Rotação por índice: `MODELOS_ROTACAO[calls % 3]` — permite comparar performance ao longo do dia.

**Cap diário:** 999 (efetivamente sem cap — Miguel 03/08 14:15 BRT: "gpt é barato, pode usar em todos os loops"). Script `CAP_DIARIO=999`, `HORAS_PICO_BRT=set(range(24))`. Se voltar a querer restringir, editar essas 2 variáveis.

**Regra de horário:** todas as horas (chama em todo ciclo).

**Switch on/off:**
- `state/gpt_enabled.txt` = `on` (default) ou `off`.
- Comandos: `python3 gpt_revisor.py --on` / `--off` / `--status`.

**Contador diário:**
- Arquivo: `state/gpt_counter_YYYY-MM-DD.json` (persistente).
- Reset automático por dia (arquivo novo).
- Guarda: `calls`, `custo_usd_total`, `por_modelo`.

**Telemetria completa:**
- Log JSONL: `/home/migueldorosario/ferramentas/sentinela/logs/gpt_revisor_telemetria.jsonl`.
- Campos: `ts_utc, modelo, in_tok, out_tok, custo_usd, custo_brl, lat_ms, recomendacao, concordo_deepseek, vertical, titulo_ok, counter_dia`.

**Prompt do sistema:** revisor Cafezinho, é 2ª opinião do DeepSeek. Recebe também o JSON da revisão anterior no user_content. Retorna JSON com campo extra `concordo_deepseek: bool` + `divergencia_deepseek: str|null`.

**Custo estimado:** ~R$ 0.03/call (gpt-5-mini), ~R$ 0.02 (gpt-4.1-mini), ~R$ 0.01 (gpt-4o-mini). Média ~R$ 0.02. 10/dia = R$ 0.20/dia = R$ 6/mês. Barato.

**Caso-teste fundador (03/08 14:03 BRT):**
- Draft: "Milei ataca Lula de 'ladrão' de novo; Brasil convoca embaixador"
- DeepSeek pegou: regência, ;, fonte CAPS, gênero fem, caps pós-vírgula
- GPT pegou tudo isso + nuances: identificar "presidente argentino Javier Milei" na 1ª menção; trocar "de novo" por "novamente"; falta contexto/data; link sem href
- GPT concordou com DeepSeek (concordo_deepseek=true), sem divergências
- Latência: 34.6s (gpt-5-mini reasoning); custo: R$ 0.03

**Como aplicar no ciclo (a partir do próximo):**
1. Puxar draft
2. DeepSeek revisor (sempre)
3. `should_call()` decide GPT — se True, chama passando `revisao_deepseek=r_ds`
4. Combinar bugs (DeepSeek + GPT + minha própria)
5. WebSearch em bugs_factuais_potenciais
6. Aplicar fixes + publish + backup SHA-256
7. Log JSONL com o que cada camada pegou

**Fail-safe:** Se GPT falha (timeout/500), publish segue com DeepSeek + Claude — não bloqueia.

**Ajuste rápido pra desligar/reduzir:**
- Desligar temporariamente: `python3 gpt_revisor.py --off` (Claude vira 2-camadas: DeepSeek + Claude)
- Reduzir cap: editar `CAP_DIARIO` no script.
- Mudar janela pico: editar `HORAS_PICO_BRT`.
- Trocar modelos: editar lista `MODELOS_ROTACAO`.

Regras irmãs: [[feedback-deepseek-revisor-camada-extra]], [[feedback-checagem-titulo-semantica-e-genero-fonte]], [[feedback-smoke-de-api-precisa-chamada-real-de-centavos]], [[feedback-nunca-chave-literal-em-forum]], [[feedback-reportar-economia-em-real-ao-delegar-sub-agent]].
