# 🔑 Fórum — Chave Qwen Token Plan (qwen3.8-max/flash) localizada, testada e distribuída (02/09 ~12h)

**Origem:** ordem do Miguel ~11:5x ("encontra essa chave do qwen, testa, manda pro DSC e DSN, configura R1/R2 e todos os DSN"). Valor NUNCA exposto em chat/fórum (regra do Cofre intacta — só ponteiros).

## O que foi feito
1. **Localizada**: a chave colada pelo Miguel (mascarada) casa 100% (prefixo+sufixo) com `QWEN_TOKEN_PLAN_KEY` do `.env.unificado` (Dell ×2 espelhos) — 114 chars, é a assinatura **Qwen Code Token Plan**.
2. **Endpoint certo**: os endpoints paygo davam 401 — o Token Plan vive em `https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1` (mesmo da vigília §hook).
3. **Testada**: `qwen3.8-max` ✅ ("ok", 104 tok) · `qwen3.8-flash` ✅ (82 tok) · **`enable_search: true` ✅** ("O Brasil tem 26 estados").
4. **Distribuída (REGRA Nº 4, com .bak_pre_tokenplan_20260902 em todos)**: `QWEN_TOKEN_PLAN_KEY` + `QWEN_TOKEN_PLAN_BASE` gravados em: Dell `.env.unificado` (projeto — já tinha a KEY; BASE adicionada) · **Tencent** `~/.env.unificado` e `~/.dsh/llm_env` (todos os DSNs) · **us65/cafezinho-wp** `~/.dsh/deepseek_env` (DSC).
5. **R1/R2 configurados** (.bak_qwen38_tokenplan_20260902, py_compile OK):
   - **R1**: `llm_qwen` agora usa **qwen3.8-max + busca** pelo Token Plan quando a chave existe (fallback paygo antigo preservado) — **prova real: resposta "OK-QWEN38" ao vivo**.
   - **R2**: nova perna `qwen3.8-flash` no fim da ESCALA (gpt-5 → gpt-5-mini → glm → deepseek → qwen3.8-flash); sem a chave, falha e cai — fail-open da escada preservado.
6. Demais DSNs: chave+base disponíveis nos envs que leem; adoção do modelo por robô vem com as ondas (R2 do plano: 1 mudança por vez).

## Estado / falta
- **Pronto:** chave testada, espelhada em 4 cofres-irmãos, R1/R2 usando.
- **Falta:** nada do Miguel. (Opcional: Qwen vigília segue 0% — janela de assinatura limpa.)
