# MEMÓRIA — Alibaba Token Plan: análise técnica completa (fonte primária + endpoints)

**Data:** 2026-08-01 ~16:30 BRT
**Autor:** ZCode (GLM-5.2), a pedido do Miguel
**Fórum irmão (decisões resumidas):** `Foruns/forum_alibaba_token_plan_nao_serve_api_cafezinho_20260801.md`
**Tipo:** Log técnico permanente — análise da página oficial `token-plan-overview` + docs de endpoint.

---

## 1. Fonte primária consultada

O Miguel colou em 01/08 ~16:03 BRT a página oficial completa:
`https://help.aliyun.com/zh/model-studio/token-plan-overview` (atualizada 2026-07-27 09:55:53).

Texto-chave da linha 146:
> "Token Plan 是阿里云百炼推出的 AI 大模型订阅服务，以 Credits 统一计量，支持多种 AI 编程和智能体工具。"

Texto-chave da linha 149:
> "Token Plan 目前仅支持华北2（北京）地域，请在百炼控制台左上角将地域切换至华北2（北京）后购买并使用。"

Texto-chave da linha 152 (modelos suportados/ferramentas):
> "...支持在 Claude Code、Cursor、Qwen Code、Qoder、Qoder CN、OpenClaw 等主流 AI 编程和智能体工具中使用。"

---

## 2. Tabela de tiers (extraída da página oficial, linhas 174-224)

### Personal (个人版)

| Campo | Lite | Standard | Pro | 用量包 (add-on) |
|-------|------|----------|-----|-----------------|
| Preço normal | ¥60/mês | ¥180/mês | ¥600/mês | ¥100/unid/mês |
| Preço promo | ¥39/mês | ¥139/mês | ¥499/mês | — |
| **Limite 5h** | 700 Credits | 3.000 Credits | 12.000 Credits | sem limite |
| **Limite 7 dias** | 2.500 Credits | 10.000 Credits | 40.000 Credits | sem limite |
| **Agentes concorrentes** | 1-2 | 3-4 | 6-8 | — |
| Condição de compra | — | — | precisa assinatura ativa, máx 5 | — |

### Team (团队版) — linhas 254-302

| Assento | Preço promo | Créditos/mês/assento |
|---------|-------------|----------------------|
| Standard | ¥150/assento/mês (normal ¥198) | 25.000 |
| Pro (高级) | ¥550/assento/mês (normal ¥698) | 100.000 |
| Max (尊享) | ¥1.398/assento/mês (sem promo) | 250.000 |
| Shared Bundle (Extra) | ¥5.000/unid/mês | 625.000 |

Team não tem janelas 5h/7d, usa **cota mensal por assento**.

---

## 3. Mecânica de cobrança e limites (linhas 306-315)

- **Personal:** 2 janelas fixas (5h e 7d). Cada janela inicia na 1ª chamada. Ao bater o limite, **serviço pausa** até resetar.
- **Não acúmulo:** "窗口期内未用完的额度不结转至下一周期" (Credits não usados NÃO transferem ao próximo ciclo).
- **Credits por coeficiente:** "按模型分档抵扣系数计费" — cada modelo tem um multiplicador. Modelo mais caro = menos chamadas reais por Credit.
- **Team:** cota mensal por assento; ao estourar, chamada é **bloqueada** (需 comprar Shared Bundle).
- **Promoção atual (qwen3.8-max-preview):** consumo de Credits a 1折 (1/10) durante preview + 2折 noturno (22h-08h) → 0.2折 efetivo. É uma promo, **não é a régua permanente**.

---

## 4. Endpoint e Base URL (pesquisa doc Alibaba Cloud Help)

Resultado da busca nas docs oficiais (`help.aliyun.com/zh/model-studio/regions/`, `/claude-code`, `/claude-code-token-plan`):

1. **Pay-as-you-go (DashScope, OpenAI-compatible):**
   - Internacional: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1` ← **este é o que o Cafezinho usa**
   - China: `https://dashscope.aliyuncs.com/compatible-mode/v1`

2. **Token Plan endpoint dedicado:**
   - Forma: `https://token-plan.cn-beijing.maas.aliyuncs.com/apps/{workspaceId}/...`
   - **Região fixa: cn-beijing (华北2)** — não há variantes intl/sg/tokyo/frankfurt.

3. **Regra oficial confirmada:** "使用 Coding Plan / Token Plan 时务必用专属 Base URL，否则会按量计费." → chamar o endpoint pay-as-you-go com chave do Token Plan cobra em **pay-as-you-go** (não desconta da assinatura).

**Implicação para o Cafezinho:** para usar Token Plan seria preciso:
(a) reescrever a `BASE_URL` no código do widget/backend;
(b) gerar e usar uma API Key diferente;
(c) travar a região em Pequim;
(d) aceitar as janelas 5h/7d com pausa de serviço.

---

## 5. Comparativo com o padrão Zhipu/Kimi (Cérebro, linhas 534-557)

O Alibaba repete o mesmo desenho arquitetural das outras duas clouds chinesas de IA já mapeadas:

| Cloud | Endpoint ASSINATURA | Endpoint PAY-AS-YOU-GO | Erro enganoso típico |
|-------|---------------------|------------------------|----------------------|
| Zhipu | `open.bigmodel.cn/api/coding/paas/v4` | `open.bigmodel.cn/api/paas/v4` | 1113 "sem saldo" |
| Kimi | `api.kimi.com/coding/v1` | `api.moonshot.ai/v1` | 404/auth |
| **Alibaba** | `token-plan.cn-beijing.maas.aliyuncs.com/...` | `dashscope-intl.aliyuncs.com/compatible-mode/v1` | cobra paygo silenciosamente |

**Padrão consolidado (3ª ocorrência):** todas as clouds chinesas de IA (Zhipu, Kimi, Alibaba) separam **assinatura** (endpoint dedicado, quota do plano, ferramenta de coding/agente) de **pay-as-you-go** (endpoint DashScope-like, por token, sem janela). A confusão é sistemática e esperada. **Regra derivada para o Cérebro:** ao avaliar qualquer assinatura de cloud chinesa de IA, sempre verificar (1) endpoint dedicado exigido, (2) se permite chamada externa/produção ou só IDE/playground, (3) janelas e pausas de serviço.

---

## 6. Veredito técnico e por quê

**🚫 Token Plan NÃO serve para backend de site em produção (Cafezinho), porque:**

1. Exige endpoint próprio → reescrita de código + troca de key + região Pequim.
2. Janela 5h + 7d com **pausa de serviço** ao bater limite → derruba o widget/Tribunal Visual imprevisivelmente.
3. Concorrência limitada (máx 6-8 agentes no Pro) vs chamadas paralelas do Cafezinho (redação + auditoria + visão).
4. Credits não acumulam; coeficiente de modelo reduz chamadas reais.
5. Desenhado para ferramentas de coding/agente (Claude Code/Cursor), não para produção web.

**✅ O remédio é recarregar o pay-as-you-go** (ou resource package / Savings Plan, se volume justificar), mantendo o endpoint DashScope que já funciona.

---

## 7. Gasto atual do Cafezinho com Qwen (a medir)

Para decidir entre recarga simples (A) vs Savings Plan (B), falta medir o gasto real. Fontes a consultar:
- `Memorias/memoria_despesas.md` (livro-caixa)
- `root/agent_data/banco_custos.json` / `banco_custos_*.jsonl`
- `root/agent_data/governanca_financeira_api_usage.jsonl`
- `root/agent_data/log_rotas_llm.jsonl`

Critério: gasto Qwen < ¥139/mês → só recarregar. ≥ ¥139 e estável → avaliar Savings Plan.

---

## 8. Fontes

- Página oficial Token Plan: `https://help.aliyun.com/zh/model-studio/token-plan-overview` (colada pelo Miguel, atualizada 2026-07-27)
- Token Plan Personal: `https://help.aliyun.com/zh/model-studio/token-plan-personal-overview`
- Coding Plan: `https://www.alibabacloud.com/help/en/model-studio/coding-plan`
- Model pricing: `https://www.alibabacloud.com/help/en/model-studio/model-pricing`
- Savings Plans & Resource Packages: `https://help.aliyun.com/en/model-studio/savings-plan-and-resource-package`
- OpenAI compatibility: `https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope`
- Claude Code (Token Plan Team): `https://help.aliyun.com/zh/model-studio/claude-code-token-plan`
- Regiões/endpoint: `https://help.aliyun.com/zh/model-studio/regions/`

— ZCode (GLM-5.2), 01/08/2026 ~16:30 BRT
