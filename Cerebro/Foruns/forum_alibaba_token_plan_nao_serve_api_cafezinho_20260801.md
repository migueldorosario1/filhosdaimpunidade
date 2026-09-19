# FÓRUM — Alibaba Model Studio "Token Plan" NÃO serve para API do Cafezinho (01/08/2026)

**Data:** 2026-08-01 ~16:30 BRT
**Autor:** ZCode (GLM-5.2), a pedido do Miguel
**Veredito:** 🚫 **NÃO assinar o Token Plan (Lite/Standard/Pro) para uso no site Cafezinho.** O remédio é recarregar o pay-as-you-go.
**Memória irmã (fonte primária + análise técnica):** `Memorias/memoria_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md`
**Relacionado:** `Foruns/forum_qwen_alibaba_contas_20260801.md` (análise Qwen do mesmo dia, complementar) · `Foruns/forum_unificacao_cofre_chaves_20260801.md`

---

## 1. A dúvida do Miguel (transcrição resumida)

> "Vale a pena assinar o Alibaba Cloud Model Studio Standard/Pro Plan do Qwen? Quero saber se essa assinatura (tokenplanoverview.com) vai dar direito pra usar a API no site Cafezinho, porque já tô tendo uma trava lá. Em vez de pay-as-you-go eu usaria subscription token plan. O Alibaba é o site mais complicado pra usar... eu uso muito Qwen em visão, quero ver se consigo usar."

**Resposta curta:** Não. O Token Plan é para ferramentas de código/agente (Claude Code, Cursor, Cline) — **não para backend de site em produção**. A trava é saldo do pay-as-you-go; recarregue o pay-as-you-go.

---

## 2. Os 4 produtos do Alibaba que confundem (fonte: página oficial + docs)

| Produto | O que é | Serve pro widget/site Cafezinho? |
|---------|---------|----------------------------------|
| **Pay-as-you-go** (DashScope, ATUAL) | Cobra por token usado | ✅ É o que funciona hoje |
| **Token Plan — Pessoal** (Lite/Standard/Pro) | Assinatura mensal em **Credits** | 🚫 **NÃO** (motivos no §4) |
| **Token Plan — Equipe** (por assento) | Por colaborador/seat | 🚫 Não (feito pra times) |
| **Coding Plan** (Lite/Pro) | Só pra IDEs de código | 🚫 Não (endpoint próprio) |

A página que o Miguel colou é o **Token Plan 概述** (overview). Tiers Pessoais:

| Tier | Preço promo | Credits / 7 dias | Concorrência |
|------|------------|------------------|--------------|
| **Lite** | ¥39/mês (normal ¥60) | 2.500 | 1-2 agentes |
| **Standard** | ¥139/mês (normal ¥180) | 10.000 | 3-4 agentes |
| **Pro** | ¥499/mês (normal ¥600) | 40.000 | 6-8 agentes |

---

## 3. Por que NÃO serve para o Cafezinho — evidência da própria página oficial

A página é explícita (linha 146, 152 da fonte colada):

> "Token Plan 是阿里云百炼推出的 AI 大模型订阅服务...支持 Claude Code、Cursor、Qwen Code、Qoder、Qoder CN、OpenClaw 等主流 **AI 编程和智能体工具**"
> *(Token Plan é um serviço de assinatura... suporta Claude Code, Cursor, Qwen Code, Qoder, OpenClaw etc. — **ferramentas de programação AI e agentes**)*

**Tradução operacional:** o Token Plan foi desenhado para ferramentas de desenvolvedor/agente, não para um backend de site chamando a API de forma automatizada em produção.

A documentação de endpoint confirma:
> "Coding Plan / Token Plan **必须使用其专属 Base URL 和 API Key**，否则会按量计费"
> *(Token Plan **exige Base URL e API Key dedicados**; senão, cobra pay-as-you-go)*

O endpoint do Token Plan é diferente do DashScope (`dashscope-intl.aliyuncs.com`) que o Cafezinho usa hoje — algo como `token-plan.cn-beijing.maas.aliyuncs.com/apps/...`.

---

## 4. As 4 travas técnicas fatais (da página oficial, linhas 149-315)

| # | Trava | Citação da fonte | Impacto no Cafezinho |
|---|-------|------------------|----------------------|
| 1 | **Endpoint próprio obrigatório** | "必须使用其专属 Base URL" | Reescrever código do widget + trocar API key + mudar região |
| 2 | **Região Pequim obrigatória** | "Token Plan 目前仅支持华北2（北京）地域" (linha 149) | Servidor Tencent roteia diferente; latência muda |
| 3 | **Janela de 5h + 7 dias com PAUSA de serviço** | "累计消耗达到限额后暂停服务" (linhas 308-312) | Ao bater o limite, **derruba o Tribunal Visual do nada** |
| 4 | **Crédito não acumula + concorrência limitada** | "未用完的额度不结转"; Pro = 6-8 agentes (linhas 212-224) | Perde Credits não usados; cafezinho dispara chamadas paralelas → bate teto |

**Adicional:** uso é medido em Credits por **coeficiente de modelo** (linha 154: "按模型分档抵扣系数计费") — modelos mais caros (qwen-max) "comem" mais credits por chamada → menos chamadas que o esperado.

---

## 5. 🏷️ Padrão recorrente — mesmo erro já documentado no Cérebro p/ Zhipu/Kimi

O Cérebro já documenta (linhas 534-557 do `CEREBRO_NODE_CHAVES_E_LLMS.md`): **assinatura e pay-as-you-go são sistemas de cobrança separados, com endpoints diferentes**.

| Provider | Endpoint ASSINATURA | Endpoint PAY-AS-YOU-GO |
|----------|---------------------|------------------------|
| **Zhipu/GLM** | `open.bigmodel.cn/api/coding/paas/v4` | `open.bigmodel.cn/api/paas/v4` |
| **Kimi/Moonshot** | `api.kimi.com/coding/v1` | `api.moonshot.ai/v1` |
| **Alibaba/Qwen (Token Plan)** | `token-plan.cn-beijing.maas.aliyuncs.com/apps/...` | `dashscope-intl.aliyuncs.com/compatible-mode/v1` |

Regra viva do Cérebro (linha 556): *"chave de assinatura no endpoint pay-as-you-go dá erro enganoso — o erro mente a causa."* O Alibaba segue exatamente o mesmo padrão. **Esta é a terceira ocorrência** (Alibaba depois de Zhipu e Kimi) → padrão arquitetural consolidado de todas as clouds chinesas de IA.

---

## 6. O que resolve a trava de verdade (3 caminhos, do mais simples)

### ✅ Opção A — Recarregar pay-as-you-go (RECOMENDADO)
- Console Alibaba → **模型调用计费** → adicionar saldo ou comprar **resource package (资源包)**.
- **Não mexe em código, endpoint nem região.** Site continua idêntico.
- Resource package = pacote pré-pago de tokens com desconto, **sem compromisso mensal**, sem trava de janela.

### Opção B — Savings Plan (节省计划) — só se gasto alto e constante
- Compromisso de gasto mensal (3/6/12/24 meses) → desconto escalonado, **mantém endpoint pay-as-you-go**.
- Doc: `help.aliyun.com/en/model-studio/savings-plan-and-resource-package`.

### Opção C — Otimizar consumo de visão (raiz do gasto)
- O Miguel "usa muito Qwen em visão". Catálogo: `qwen-vl-plus` ~$0,26/1M (barato), mas se volume explodiu:
  - cache de imagens repetidas; rebaixar parte das chamadas; auditar `root/agent_data/precos_modelos.json`.

---

## 7. Recomendação final e próximo passo

**Recomendação:** Opção A (recarregar pay-as-you-go + avaliar resource package). Preserva tudo que funciona; zero risco de derrubar produção.

**Critério objetivo para decidir A vs B** (registrado para consulta futura):
- Gasto Qwen mensal observado < ¥139 → **só recarregar** (A).
- Gasto Qwen mensal alto e estável → **A + Savings Plan** (B).
- Antes de assinar QUALQUER plano: confirmar no console que ele libera **chamada API externa/produção** (não só uso no playground).

**Próximo passo:** ler `Memorias/memoria_despesas.md` + logs (`banco_custos`, `log_rotas_llm.jsonl`) para medir gasto real de Qwen do último mês → decidir A vs A+B. (Pendente execução.)

---

## 8. Decisões pendentes de Miguel

1. Recarregar pay-as-you-go do Qwen (quanto? qual conta?).
2. Avaliar resource package vs Savings Plan depois de medir gasto (próximo passo acima).
3. Confirmar: quer que eu meça o gasto real de Qwen agora?

— ZCode (GLM-5.2), 01/08/2026 ~16:30 BRT · Fonte primária: página `token-plan-overview` oficial colada pelo Miguel + docs Alibaba Cloud Help.
