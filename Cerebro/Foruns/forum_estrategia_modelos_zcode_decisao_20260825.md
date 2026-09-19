# 🎯 FÓRUM — Estratégia de modelos do ZCode: DECISÃO do Miguel (25/08/2026)

**Criado:** 2026-08-25 ~12:57 BRT · ZCode/DeepSeek · Ordem do Miguel: "vou apostar no deepseek, por API. achei o kimi k3 muito caro... a gente usa também fora daqui, no sistema, nos sites, no moka"
**Memória-irmã:** `Memorias/memoria_estrategia_modelos_zcode_decisao_20260825.md`

## A decisão (texto do Miguel, resumido)

- **DeepSeek V4 Pro via API = modelo principal do ZCode** (pay-as-you-go, sem janela de 5h).
- **Kimi K3 (assinatura Allegretto) = caro demais e a janela de 5h prejudicava** — não renovar.
- Motivo extra: o DeepSeek **já é usado no resto do ecossistema** (sites V4/V4.1, Moka, temáticos) — um provedor só pra tudo.

## Por que faz sentido (números medidos hoje)

| | DeepSeek V4 Pro | Kimi K3 (assinatura) | GPT-5.6 Sol (promo) |
|---|---|---|---|
| Preço | $0,435 / $0,87 por 1M | US$ 31–39/mês + janela 5h | $4 / $20 por 1M |
| Turno pesado (127k in + 1,1k out) | **~US$ 0,06** | conta quota → esgota (12× desde 20/07) | ~US$ 0,53 |
| Janela de 5h | **não tem** (só saldo) | tem, esgota | não tem (só crédito) |
| Websearch no ZCode | ✅ via ferramenta do harness (provado ao vivo 25/08) | ✅ idem | ✅ idem |

## Estado da configuração (tudo pronto hoje)

1. ✅ Preços dos planos Kimi documentados (`CEREBRO_NODE_CUSTOS_REAIS_MENSAL.md` — lacuna 🔴 fechada).
2. ✅ Família GPT-5.6 (Sol/Terra/Luna) no catálogo com preços e benchmarks.
3. ✅ Provider "OpenAI (GPT-5.6)" criado no ZCode + smoke do Sol 200 (backup `.bak_pre_openai_gpt56_20260825_1251`).
4. ✅ Chave `ZCODE_OPENAI` (sha8 `8035a022`) espelhada nos 2 cofres (Regra 4).
5. ✅ DeepSeek validado na sessão: turno real completado (127.205 in / 1.109 out, ~US$ 0,06) + websearch ao vivo.

## O que falta / preciso de você (Miguel)

1. **Recarregar o DeepSeek** (saldo hoje US$ 23,97 🟢) com a parte dos R$ ~1.000 que decidir — sugestão: US$ 50-100 agora.
2. **Kimi:** cancelar a renovação automática da assinatura (deixar expirar; o ZCode segue sem ele — é o que está acontecendo nesta sessão).
3. **Opcional (precisa OK):** incluir o DeepSeek na cadeia de failover automático do hook (`~/.zcode/hooks/llm_fallback.py` — hoje: Kimi→Qwen→GLM). Com Kimi fora, a cadeia pode virar DeepSeek→GLM→Qwen.
4. **Qwen Lite (US$ 6/mês):** manter como reserva barata? (recomendação do Cérebro: sim — é o 2º elo da cadeia e inclui glm-5.2/ds-v4-pro no endpoint.)

## Vigência

Revisar em **21/11/2026** (fim garantido da promoção do Sol) e quando o saldo DeepSeek cruzar US$ 10 (vigília 🟠).

## ADENDO 1 — 2026-08-25 ~13:20 — FIX: GPT-5.6 dava 400 `max_tokens` no ZCode (kind errado)

**Sintoma:** ao tentar usar gpt-5.6-luna/sol no seletor, erro 400 da OpenAI: "Unsupported parameter: 'max_tokens' is not supported with this model. Use 'max_completion_tokens' instead."

**Causa raiz (achada no código do ZCode, `/opt/ZCode/resources/glm/zcode.cjs`):** provider com `kind: "openai-compatible"` usa o adaptador genérico, que SEMPRE envia `max_tokens` (sem detecção de modelo reasoning). A família gpt-5.6 só aceita `max_completion_tokens`. Já o `kind: "openai"` usa o adaptador oficial (Responses API), que trata reasoning nativamente.

**Fix aplicado:** provider `6ff9b527-db32-44ee-a0e4-0030d69853a2` trocado de `openai-compatible` → `openai` no `~/.zcode/v2/config.json` (backup `.bak_pre_openai_kind_fix_20260825_1315`).

**Prova (chave real, Responses API `/v1/responses`):** luna HTTP 200 "OK" · sol HTTP 200 "OK" (12 in/5 out tokens).

**Requer reinício do ZCode** (config lido na inicialização). Lição: para provedor OpenAI nativo, kind `"openai"` — `openai-compatible` é só para terceiros (DeepSeek/Qwen/Kimi etc.).

## ADENDO 2 — 2026-08-25 ~14:25 — Kimi removido integralmente; OpenAI Sol padrão; failover desligado

Por ordem explícita do Miguel, Kimi não é apenas “não renovar”: foi removido dos providers vivos `~/.zcode/v2/config.json` e `~/.zcode/cli/config.json`, da `PROVEDORES` da vigília e das instruções ativas em `~/.zcode/AGENTS.md`. O default CLI agora é `OpenAI GPT-5.6 Sol`. O failover automático antigo foi desativado (`fallback_config.json: habilitado=false`), cron `llm_fallback.py --check` comentado e overrides vivos zerados; backups datados preservam histórico.

Prova do hook real: OpenAI presente; Kimi ausente; nenhuma instrução “troque para Qwen”; nenhum resumo de failover antigo. OpenAI é pay-as-you-go e a vigília não inventa quota: informa provider ativo + telemetria local. O probe de quota permanece apenas para Qwen.

**O que aconteceu:** retirada definitiva concluída.

**O que falta:** reiniciar o ZCode para o seletor recarregar sem Kimi.

**O que preciso do Miguel:** reiniciar o aplicativo quando conveniente; a conversa atual continua no OpenAI GPT-5.6.
