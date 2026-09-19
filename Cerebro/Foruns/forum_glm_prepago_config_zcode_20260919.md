# Fórum — GLM PRÉ-PAGO: chave nova testada, ZCode configurado, cofres espelhados (19/09/2026)

**Quem:** ZCode/Kimi K3 · **Ordem do Miguel:** 19/09 ~15:3x BRT ("testa essa chave aqui do GLM... é API pré-paga, botei dinheiro lá, não é mais assinatura... configura aí no ZCode")
**ID monitor:** ZM-GLM-PREPAGO-20260919 · **Memória gêmea:** Memorias/memoria_glm_prepago_config_zcode_20260919.md

## O que aconteceu

Miguel colocou saldo na Z.ai e gerou uma **chave GLM PRÉ-PAGA** (pay-as-you-go) nova — sha8 `d0f53631`, len 49 (valor só nos cofres). O plano **Coding Plan (assinatura) EXPIROU** — e com ele morreu o endpoint Anthropic.

## Provas ao vivo (19/09 ~15:41-15:51)

- ✅ **HTTP 200** no endpoint pré-pago `https://api.z.ai/api/paas/v4`: `glm-5.3`, `glm-4.6`, `glm-4.5-flash` (do Dell) e `glm-5.3-flash` (do Tencent, já com a chave nova instalada)
- 🔴 Endpoint Anthropic `/api/anthropic` com a chave nova → **429 código 1309** "Your GLM Coding Plan package has expired" — esse endpoint é EXCLUSIVO da assinatura; pré-pago não entra nele
- 🔴 Chaves antigas TODAS mortas (**401 Authentication Failed**): as dos providers `builtin:zai` e `builtin:zai-coding-plan` do ZCode, e `ZAI_API_KEY`/`GLM_API_KEY` dos cofres Dell e Tencent (prefixo 4d8ae2...)

## Configuração no ZCode (`~/.zcode/v2/config.json`, backup `.bak_pre_glm_prepago_20260919_1547`)

- Provider "Z.ai API" (`e488030c-d773-4049-9aa9-dd06950f94c7`) → renomeado **"Z.ai API — PRÉ-PAGO"**: baseURL `https://api.z.ai/api/paas/v4`, chave nova, modelos **GLM-5.3 / GLM-4.6 / GLM-4.5-Flash** (reasoning low/high/max), `enabled:true`
- `builtin:zai` e `builtin:zai-coding-plan` → `enabled:false` (chaves mortas ficam no arquivo como histórico; se a assinatura for renovada um dia, é só reativar)
- ⚠️ Se o modelo não aparecer no seletor, reiniciar o app ZCode para recarregar o config

## Espelhos Regra 4 (todos com backup `.bak_pre_glm_prepago_20260919_1548`)

- **Dell:** `Projeto Cafezinho Agentes/root/.env.unificado` ⇄ `Outros/chaves/agentes_labs/.env.unificado` — bloco `ZAI_PREPAGO_API_KEY` + `ZAI_PREPAGO_BASE_URL` inserido; `ZAI_API_KEY`/`GLM_API_KEY` mortas viraram `_DEPRECADA_20260919`
- **Tencent:** `/root/.env.unificado` (mesmo padrão do Dell) + `/root/.env` (chave e base rotacionadas para a viva) + **`/home/ubuntu/cafezinho/redes/.env_redes`** (`ZAI_API_KEY` viva + `ZAI_BASE_URL` → `/api/paas/v4`)

## Efeito colateral positivo

A perna ZAI da **curadoria da esteira de fios** estava morta desde a expiração do plano (rondas suspendiam slots ou iam só de DeepSeek). Com a chave viva no `.env_redes`, a curadoria glm-5.3-flash **volta a funcionar** — prova 200 ao vivo do tencent.

## Estado da missão

- **Pronto:** teste completo, config no ZCode, espelhos Dell+Tencent, provas ao vivo, registro no Cérebro
- **Falta:** nada bloqueante. Pendências leves: (1) vigília de crédito GLM lia quota do coding plan — adaptar para prepaid quando houver endpoint de saldo; (2) Miguel escolher "Z.ai API — PRÉ-PAGO" no seletor de modelos quando quiser usar GLM
- **Preciso de você (Miguel):** nada urgente

## ADENDO 19/09 ~15:5x — LIMPEZA DO SELETOR (ordem Miguel: "apaga a assinatura, deixa só um Z com a API pré-paga")

- Apagados do `~/.zcode/v2/config.json` (backup `.bak_limpeza_zai_20260919_155x`): `builtin:zai`, `builtin:zai-coding-plan`, `builtin:zai-start-plan`, `builtin:bigmodel`, `builtin:bigmodel-coding-plan`, `builtin:bigmodel-start-plan` (chaves mortas 401 ou vazias; histórico nos backups)
- Restou UM Z.ai no seletor: **"Z.ai API — PRÉ-PAGO"** (GLM-5.3 / GLM-4.6 / GLM-4.5-Flash)
- `setting.json`: ponteiros mortos das famílias zai/bigmodel removidos (selectedKeys + connectionSelections); `cli/config.json`: modelo padrão repontado de `builtin:zai-coding-plan/GLM-5.3` para o pré-pago `e488030c/GLM-5.3`; `coding-plan-cache.json` removido (app regenera) — tudo com backup
- Se algo do plano reaparecer no seletor: é o app recriando templates builtin vazios/desativados — ignorar ou mandar limpar de novo
