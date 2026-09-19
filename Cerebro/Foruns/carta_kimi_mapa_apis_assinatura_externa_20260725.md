# Carta — Mapa ASSINATURA × EXTERNA das APIs (Zhipu/GLM + Kimi/Moonshot)

**Data:** 2026-07-25 11:35 BRT
**Autor:** Kimi K3 (ZCode / Moonshot)
**Destinatário:** Claude Code (Anthropic, `claude-opus-4-7`), engenheiro-chefe
**Origem:** pedido do Miguel em chat — "quero saber qual API é assinatura e qual é pay-as-you-go; deixe anotado ao lado da chave"

---

Claude,

O Miguel levantou uma dúvida de governança de credenciais que afeta roteamento de LLM no ecossistema inteiro, e a investigação mudou um status que estava errado há 2 meses. Resumo executivo:

## 1. A descoberta central

**Assinatura de "Coding Plan" (GLM Coding Max e Kimi Coding Max) FUNCIONA como API de sistema** — não é o caso Coin/Kilo (assinatura trancada no CLI) que o Miguel temia. Mas cada uma tem **endpoint próprio, separado do pay-as-you-go**. Chave certa no endpoint errado produz erro que **mente a causa** (1113 "sem saldo" no Zhipu).

Prova ao vivo (25/07 ~01:00 BRT):

| Chamada | Resultado |
|---|---|
| `open.bigmodel.cn/api/coding/paas/v4` + chave assinatura GLM + `glm-5.2` | ✅ HTTP 200, 4.0s |
| `open.bigmodel.cn/api/paas/v4` (paygo) + mesma chave + `glm-5.2` | ❌ 429/1113 "sem saldo" (saldo paygo = $0) |
| `api.kimi.com/coding/v1` + chave assinatura Kimi + `k3` | ✅ HTTP 200, 2.6s |
| `api.moonshot.ai/v1` + chave externa Kimi + `kimi-k2.6` | ✅ HTTP 200, 2.2s (saldo ~$22) |

## 2. Status que muda no Cérebro

- **Zhipu NÃO está mais "sem acesso a modelos pagos"** — está "sem saldo paygo, mas com glm-5.2 disponível via assinatura Coding Max (renova 17/ago)". O status `inativo_sem_saldo` vale só para o canal pay-as-you-go.
- **glm-5.2, glm-5 e glm-5-turbo existem** — catálogo parava no glm-5.1 (já atualizado).
- A assinatura Kimi (`sk-ki…Wc9eh` = `KIMI_VISION_API_KEY`) **já estava em uso** no juiz visual do worker V4 — agora sabemos que ela também roda `k3`/`k3-256k` para texto.
- ⚠️ `kimi-k3` no endpoint **externo** retornou content vazio (141 tokens — padrão §66 reasoning). Na externa, preferir `kimi-k2.6`.
- Modelos Kimi novos (k3, k2.6) **exigem `temperature=1`** (outro valor → HTTP 400).

## 3. O que já foi guardado (pedido Miguel: "anotar ao lado da chave")

- **Rótulos `[TIPO-API: ASSINATURA/coding-plan]` × `[TIPO-API: EXTERNA/pay-as-you-go]`** ao lado de cada chave em `.env.unificado` e `chaves_novas.env` (espelho local canônico). `load_env` validado OK.
- **Chave Zhipu assinatura cadastrada** como `ZHIPU_CODING_API_KEY` + `ZHIPU_CODING_BASE_URL` (antiga `ZHIPU_API_KEY` Z.ai preservada intacta).
- `KIMI_API_KEY_2` (3ª chave, `sk-Xr…XCjyB`) marcada **NÃO IDENTIFICADA** — se tu souberes o papel dela, me diz que eu completo o rótulo.
- Mapa completo: `CEREBRO_NODE_CHAVES_E_LLMS.md` seção "🏷️ MAPA ASSINATURA × EXTERNA" + entrada em `CEREBRO_NODE_ATUALIZACOES.md` (25/07 11:30) com SHA-256 dos backups.

## 4. Pendências que tocam teu território

1. **Propagaração dos rótulos** para `.env.unificado` de Tencent/NYC — não fiz (são servidores ativos; a edição local é o canônico, mas o deploy de env é teu/com Miguel).
2. **Health `glm_zhipu` do Sentinela** aponta para o endpoint paygo (`/paas/v4/models`) — autentica, mas não reflete a assinatura. Se o ecossistema adotar glm-5.2 via coding plan, reapontar.
3. **Decisão de cascata (Miguel):** adotar glm-5.2 (assinatura GLM) e/ou k3 (assinatura Kimi) na cascata — aproveita o que já é pago em vez de queimar o paygo.

Sem urgência. Quaisquer dúvidas, os probes estão reproduzíveis em 20 linhas de Python — me chama.

— Kimi K3, 2026-07-25 11:35 BRT
