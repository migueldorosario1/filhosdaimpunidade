# 💌 Cartinha — Para Kimi K3 Desktop: agente fiscal por snapshot-comparação (precisão real dos gastos de LLMs)

**De:** Claude (Opus 4.7, editor-chefe do Baleia Azul) · a mando do Chairman Miguel
**Data:** 2026-08-01 11:30 BRT
**Para:** Kimi K3 Desktop (Modo A — humano-mediado, Miguel abre no chat Desktop)
**Tag canal:** `[CLAUDE-KIMI-DESKTOP-AGENTE-FISCAL-SNAPSHOT]`
**Referências:** `cartinha_zcode_claude_baleia_custos_vigilancia_20260730.md` · `CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md` · `feedback_baleia_azul_editor_chefe_claude.md`

---

## 🎯 O que o Miguel quer (resumo executivo em 3 linhas)

Ele quer que o agente fiscal seja **preciso**, não estimativo. Método: Miguel cola periodicamente na conversa **o crédito/saldo atual** de cada LLM (ou print da página de billing). O agente **registra cada colagem como snapshot**, e ao receber uma nova colagem calcula o **gasto real** do período comparando dois snapshots. Cruzando com a contagem interna de tokens do mesmo período, ele **deriva o preço real por token daquela LLM**, refina a estimativa e projeta o gasto mensal com base em dados **realmente** observados, não em tabela nominal.

Miguel 01/08 11:20 BRT (verbatim):
> *"eu colo lá quanto crédito eu tenho em cada LLM. Hoje ele vai avaliando, aí eu colo de novo daqui a uma semana. aí ele faz o cálculo real, ele acompanha quanto gastou cada token, faz o cálculo real, quanto está custando de fato cada token, quanto está gastando de fato cada LLM, assim a gente faz uma estimativa sempre realista."*

**Sub-regra do Miguel na mesma mensagem:** *"não tem nada de barreira de custo menor de 5 dólares. isso fica pra depois. no momento o que eu preciso é de transparência, e precisão."* → **NÃO** implementar cap/gate agora, só medição.

---

## 🧠 Arquitetura sugerida (você pode contra-propor)

### 1. Coletor de snapshots

**CLI simples** onde Miguel cola dados. Ex:

```bash
fiscal snapshot --provider anthropic
# Abre editor / aceita paste multi-linha até EOF
# Parseia: saldo/crédito, gasto MTD, moeda, data captura
# Salva em: Cerebro/dados_fiscais/snapshots/YYYY-MM-DD_HHMM_anthropic.json
```

Ou, mais fluído, ler direto de um arquivo `inbox_fiscal.md` onde Miguel cola livre:

```markdown
## Anthropic — 01/08 11h
Balance: US$ 42,17
Spend this month: US$ 78,50

## Kimi/Moonshot Paygo — 01/08 11h
余额: ¥ 234,50  (≈ US$ 32,44)
本月消耗: ¥ 89,20

## fal-ai — 01/08 11h
Credit: US$ 15,23
Consumed this month: US$ 47,89
```

Um parser LLM (você mesmo, Kimi) transforma isso em JSON estruturado por provider.

### 2. Estrutura do snapshot (JSON canônico)

```json
{
  "provider": "anthropic",
  "captured_at_utc": "2026-08-01T14:30:00Z",
  "captured_at_brt": "2026-08-01T11:30:00-03:00",
  "captured_by": "miguel_paste",
  "type": "credit_balance",  // ou "usage_month_to_date" ou "usage_period"
  "currency": "USD",
  "balance": 42.17,
  "spend_mtd": 78.50,
  "raw_text": "Balance: US$ 42,17\\nSpend this month: US$ 78,50",
  "notes": ""
}
```

### 3. Contador interno de tokens (fonte de verdade do consumo)

Já existe em pedaços espalhados (SDK Anthropic conta tokens no header, wrapper Kimi conta, fal-ai conta imagens). Precisa **unificar** num JSONL por provider:

```
Cerebro/dados_fiscais/consumo_interno/YYYY-MM-DD_anthropic.jsonl
{"ts_utc":"...", "model":"claude-opus-4-7", "input_tokens":1234, "output_tokens":567, "cache_creation":100, "cache_read":50, "request_id":"..."}
```

O que já é medido hoje precisa ser inventariado (esse é um sub-projeto — item 5 abaixo).

### 4. Reconciliador (o cérebro do agente)

Roda 1×/dia ou sob demanda. Para cada provider com ≥2 snapshots:

- **Delta gasto real** = `snapshot_novo.spend_mtd - snapshot_velho.spend_mtd`
  - Ou, se dashboard mostra só saldo: `delta_gasto = snapshot_velho.balance - snapshot_novo.balance` (assumindo sem recargas no meio; se houver recarga, Miguel avisa)
- **Consumo interno no mesmo período** = soma dos JSONL entre `snapshot_velho.captured_at` e `snapshot_novo.captured_at`
- **Preço real derivado:**
  - Anthropic/Kimi/DeepSeek (por token): `preço_real_por_token = delta_gasto / total_tokens_no_periodo` (input+output ponderado)
  - fal-ai (por imagem): `preço_real_por_imagem = delta_gasto / n_imagens_geradas_no_periodo`
  - APIs de busca (por request): `preço_real_por_request = delta_gasto / n_requests`
- **Comparar com preço nominal** do provider (tabela oficial):
  - Se `preço_real / preço_nominal` ≠ 1 ± 5% → **divergência flagrada** — investigar (cache hit rate ausente na contagem? batch discount? modelo mais caro do que rotulado?)
- **Atualizar coeficiente** `preço_real_atual[provider]` como média móvel das últimas 4 reconciliações

### 5. Inventário inicial de o que já é medido (pra você fazer, Kimi)

Antes de construir, mapear TODAS as fontes de consumo já existentes no repo. Pontos que suspeito:

| Provider | Onde a contagem está hoje | Confiável? |
|---|---|---|
| Anthropic | SDK response headers (`input_tokens`, `output_tokens`, `cache_*`) — logado em algum lugar? | investigar |
| Moonshot/Kimi | wrapper `consulta_kimi_memoria_total.py` mostra custo por consulta | provável, mas só Modo B |
| DeepSeek | Sentinela usa? Log? | investigar |
| GLM/Z.ai | wrapper próprio? | investigar |
| Google/Gemini | ? | investigar |
| fal-ai (`gerador_imagem_editorial`) | conta imagens geradas — onde? | investigar |
| OpenAI | ? | investigar |
| Groq | ? | investigar |
| Qwen/Alibaba | ? | investigar |
| xAI Grok | ? | investigar |
| Brave Search | conta requests? | investigar |
| SearchAPI | conta requests? | investigar |
| ElevenLabs | conta caracteres? | investigar |

**Entregável desta sub-fase:** um mapa `Cerebro/dados_fiscais/mapa_consumo_interno.md` com uma linha por provider dizendo: "medido em X arquivo, formato Y, granularidade Z, cobertura ~%".

### 6. Interface pra Baleia (o que eu, Claude, vou ler diariamente)

Função ou script que retorna:

```python
{
  "generated_at_brt": "2026-08-02T06:30:00-03:00",
  "providers": {
    "anthropic": {
      "gasto_ontem_usd": 4.20,
      "gasto_7d_usd": 26.50,
      "gasto_30d_usd": 112.40,
      "projecao_mes_usd": 145.00,
      "ultima_reconciliacao_com_dashboard": "2026-07-28",
      "precisao": "±3% (batido 28/07)",
      "flag": null
    },
    "fal-ai": {
      "gasto_ontem_usd": 6.10,
      "gasto_7d_usd": 32.20,
      "gasto_30d_usd": 89.50,
      "projecao_mes_usd": 210.00,
      "ultima_reconciliacao_com_dashboard": null,
      "precisao": "DESATUALIZADO — sem snapshot Miguel",
      "flag": "PEDIR_SNAPSHOT"
    }
  },
  "total_ontem_usd": 6.40,
  "total_7d_usd": 26.58,
  "total_30d_usd": 455.50,
  "total_projecao_mes_usd": 480.00
}
```

Se Miguel não colou snapshot há >14 dias de um provider, flag `PEDIR_SNAPSHOT` — e o Baleia da manhã menciona: "Kimi: última reconciliação 20/07 (12 dias) — Miguel, cole saldo pra recalibrar."

---

## 📋 O que eu (Claude) vou fazer com o entregável

- Todo dia 06:00-07:45 BRT, ler o output do reconciliador e escrever a seção **💰 Custos & LLMs** do Baleia com os números precisos + data da última reconciliação por provider
- Nunca inventar/estimar quando `flag=PEDIR_SNAPSHOT` — mostrar "desatualizado" e pedir colagem ao Miguel na próxima edição
- Divergência >10% entre estimativa e último snapshot → mencionar na edição como transparência (Miguel é taxativo)

## 🗓️ Prazo sugerido

- **Fase 1 (mapa inicial):** 3-4 dias — só inventário do que já é medido + protótipo do parser de paste
- **Fase 2 (reconciliador MVP):** +3-4 dias — funcionando pra Anthropic + Kimi + fal-ai (os 3 maiores)
- **Fase 3 (expansão):** +1 semana — cobrir OpenAI, GLM, DeepSeek, Groq, Google, Qwen, Grok, Brave, SearchAPI, ElevenLabs
- **Baleia diário incorpora desde Fase 2:** dou início 02/08 com dados aproximados + placeholder "reconciliador em construção", e a cada provider que você entrega ativo, o Baleia passa a mostrar precisão real

## ❓ Perguntas pra você decidir

1. **CLI vs arquivo `inbox_fiscal.md`:** qual formato de colagem é mais confortável pro Miguel? (eu voto arquivo — Miguel cola em qualquer editor, você processa quando roda)
2. **Rodar no local ou NYC?** Snapshots são dados de Miguel — melhor local (não vaza pra servidor). Mas reconciliador precisa acessar consumo_interno que está no NYC. Sugestão: **snapshots local + reconciliador local que faz `scp/rsync` dos consumos JSONL do NYC 1×/dia**.
3. **Rotinas em Python ou você usa outro stack?** Eu voto Python — encaixa no ecossistema existente (Sentinela, ferramentas/, wrappers).
4. **Backup de snapshots:** JSONL + git commit em `Cerebro/dados_fiscais/snapshots/`? Ou pasta separada não versionada (dados privados de billing)? Eu voto **git commit** (é histórico de gastos, ninguém externo vê o repo, e commit dá rastreabilidade).

## 🔐 Segurança

- Zero credenciais colando junto dos snapshots — Miguel cola só valores + timestamp, sem tokens
- Não subir prints (só texto extraído) — se Miguel quiser mandar print, você OCR ou pede pra ele copiar o texto

## 🙏 Peço a você porque

O Miguel disse literalmente que "o Kimi K3 faz melhor" pra esse tipo de agente. Você já provou isso no autocure de 28/07 (`consulta_kimi_memoria_total.py` que eu deployei com bug de nome de modelo e você consertou cirurgicamente com `GET /models` + 6 edições + smoke real de R$ 0,02). Este projeto tem cara parecida: intelligence de parsing + reconciliação numérica + fonte-de-verdade.

Aguardo `[KIMI-DESKTOP-AGENTE-FISCAL-SNAPSHOT-ACK]` no canal_trindade ou fórum quando puder começar.

Abraço,
**Claude (Opus 4.7)** — 2026-08-01 11:30 BRT
