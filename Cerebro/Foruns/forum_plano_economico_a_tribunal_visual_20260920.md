# 🅰️ PLANO ECONÔMICO A — Contingência do Tribunal Visual sem Gemini Vision

**Nome do plano:** PLANO ECONÔMICO A
**Criado:** 20/09/2026 ~08:5x BRT por ZCode/Kimi K3 (pedido do Miguel: "cria um plano econômico A, reversível e indexado")
**Motivo:** Gemini Vision fora do ar por falta de crédito pré-pago no projeto Cafezinho Canonico (gen-lang-client-0200069757) — HTTP 402. Miguel sem verba para recarga agora. O tribunal visual do portal (`analisar_imagem_gemini_vision`, Gemini-only, fail-closed) está reprovando tudo; worker V4 segue de pé só com 1 juiz (Kimi).
**Regra do plano:** REVERSÍVEL por flag, sem apagar nada do setup Gemini. Quando o crédito voltar, desliga a flag e tudo retorna ao original.
**Fórum irmão do incidente:** `forum_incidente_chave_gemini_gcp_20260919.md` · **Memória técnica:** `memoria_plano_economico_a_tribunal_visual_20260920.md`

## Mapa de visão — testado AO VIVO em 20/09 ~08:4x (imagem real de teste)

| Juiz | Custo marginal | Estado ao vivo |
|---|---|---|
| **Kimi assinatura** (kimi-for-coding, api.kimi.com/coding) | R$ 0 (assinatura já paga) | ✅ 200 — descreveu a imagem corretamente |
| **DeepSeek flash vision** (deepseek-v4-flash e -vision-exp) | ~US$ 0,0003/análise | ✅ 200 nos dois; o `-exp` é de raciocínio → **exige max_tokens ≥ 3000** (com 500 devolve content vazio — falha silenciosa) |
| **Claude Haiku 4.5** (visão) | ~US$ 0,001/análise | ✅ 200 — descreveu corretamente |
| Kimi paygo (moonshot.ai) | — | ❌ 429 (sem saldo paygo) |
| Qwen VL Plus | — | ❌ 400/403 (conta Alibaba fora de good standing) |
| GLM visão (glm-4.6v/4.5v) | — | ❌ 429/401 (conta sem pacote de visão) |
| Gemini 2.5-flash | — | ❌ 402 (sem crédito — motivo do plano) |

## Quem pode caçar e verificar imagem (divisão de trabalho)

**Caçar (busca por texto — Commons/Flickr/Openverse/WP):** não usa visão, segue normal para todos: Laura (crons), ZM, CL, CM, AGY.

**Verificar (olhar a foto e julgar):**
- **ZM** (ZCode Miguel, Kimi K3) — vê imagem (Read local + API Kimi). ✅
- **CL** (Claude Laura) e **CM** (Claude Maestro) — veem via API (chave viva testada). ✅
- **AGY** (Antigravity Desktop — também é Gemini): a chave que morreu era a do Agent Platform (API). O IDE usa OAuth da conta Google do Miguel — quota separada. **Teste de 30s:** abrir o AGY e pedir "descreva esta foto". Se responder, ele entra como revisor manual de capas importantes.
- **Miguel** — palavra final editorial (janela política, manchete).

## AÇÕES DO PLANO

### AÇÃO 1 — Tribunal do portal ganha escada (o remendo principal)
Função `analisar_imagem_gemini_vision` em `agente_roteador_llm.py` (Dell + NYC `/root/`):
- Hoje: Gemini-only; falha → REPROVADA (fail-closed).
- Plano A: mesma função, mesma assinatura, mesmo formato de resposta (`VEREDICTO:`/`LEGENDA:`). Ordem da escada: **Gemini** (se voltar) → **Kimi assinatura** → **DeepSeek flash vision** → **Claude Haiku**.
- **Flag:** `PLANO_ECONOMICO_A=1` no ambiente liga a escada; `=0` (ou ausente) = comportamento original. Sem flag, nada muda.
- Backup: `.bak_pre_plano_economico_a_20260920` nos dois hosts.
- Reversão: 1 toggle (ou restaurar o .bak). Nada do setup Gemini é apagado.

### AÇÃO 2 — Worker V4 ganha degrau DeepSeek (redundância barata)
Contrato `/root/v4_labs/contratos/v4_rotas_visao_v1.json` (NYC): adicionar rota `deepseek_vision` (openai_compatible, `deepseek-v4-flash`, DEEPSEEK_API_KEY, max_tokens 3000) com prioridade 25 — entre kimi_paygo e qwen. Reversão: `enabled: false`. Hoje o V4 tem 1 juiz só; com o plano passa a ter 2 independentes (Kimi + DeepSeek).

### AÇÃO 3 — Regra editorial temporária (enquanto o plano estiver ativo)
- Fotos de político nomeado: segue a regra permanente (sem foto real → não publica).
- Tribunal automático com 1 juiz decide; veredicto duvidoso ou matéria de manchete → escala para revisor com olhos (ZM/CL/CM/AGY se a conta dele estiver ativa).
- Caça de imagem por texto continua normal (não usa visão).

## Custos estimados
- Kimi assinatura: R$ 0 marginal. DeepSeek: centavos de dólar por dia (capa = ~1.300 tokens com imagem reduzida). Claude: só desempate. **Total: praticamente zero.**

## Saída do plano (rollback)
Miguel recarrega o AI Studio (https://ai.studio/usage) → Gemini volta → `PLANO_ECONOMICO_A=0` (ou remover a env) nos dois hosts → portal volta a ser Gemini-only → rota DeepSeek do V4 vira `enabled:false`. Fim.



---

## ✅ IMPLEMENTADO — 20/09 ~12:4x BRT (ZCode/Kimi K3, ordem Miguel: recado do Telegram "Juiz visual V4 fora do ar" + "vai")

**Remetente do recado identificado:** `nucleo_visao.py` (juiz visual das hero images dos temáticos, NYC) enviando pelo bot `antigravity` via `nucleo_telegram.enviar_relatorio` — SEM assinatura. **Curado:** toda mensagem de sistema agora sai assinada automaticamente com `— <módulo chamador> @ <host>` (patch em nucleo_telegram.py; teste com mock provou a assinatura na mensagem final).

**Implementação (arquivos tocados, todos com .bak_pre_plano_a_20260920):**
- NYC `nucleo_visao.py` — cascata de `julgar_imagem` e `confirmar_imagem` agora é gemini → gemini-tencent → **[kimi, deepseek]** → qwen-vl, controlada por `_plano_economico_a()` (env `PLANO_ECONOMICO_A=1` OU arquivo `/root/controles_pause/plano_economico_a.pause`). Funções novas `_julgar_kimi` (kimi-for-coding) e `_julgar_deepseek` (deepseek-v4-flash).
- NYC `v4_rotas_visao_v1.json` — rota `deepseek_vision` prio 25 (openai_compatible, DEEPSEEK_API_KEY).
- NYC `agente_roteador_llm.py` — o tribunal do portal anexa kimi-for-coding + deepseek-v4-flash aos candidatos quando o plano está ativo; provider `kimi` registrado em `llm_providers.json`.
- DELL `agentes_tematicos/agente_roteador_llm.py` (versão antiga) — `_tribunal_escala_economica()` assume quando o Gemini falha (Kimi → DeepSeek → Claude Haiku), mesmo prompt e mesmo formato de resposta.
- Flag ativada: `/root/controles_pause/plano_economico_a.pause` + `PLANO_ECONOMICO_A=1` no `.env.unificado` do NYC.

**Testes de produção (NYC, imagem real):** foto real (pug) → **APROVADA** pelo deepseek com motivo correto; imagem vazia → REJEITADA; py_compile limpo nos 5 arquivos. `julgar_imagem` voltou a VER (fail-open só se TODOS os 5 juízes caírem) e `confirmar_imagem` voltou a emitir veredito (fail-close preservado).

**⚠️ Descoberta no caminho:** Kimi assinatura estourou o **limite semanal de 7 dias** (403 "weekly usage limit") — o degrau 1 do plano A hoje é o DeepSeek (~US$0,0003/análise, saldo DeepSeek em dia). Kimi paygo 429 e Qwen 403 seguem fora.

**Reversão (rollback):** apagar `/root/controles_pause/plano_economico_a.pause` + tirar a env + restaurar os `.bak_pre_plano_a_20260920` (5 arquivos em NYC + 1 no Dell).

## Estado da implementação
- [ ] AÇÃO 1 — aguardando "vai" do Miguel
- [ ] AÇÃO 2 — aguardando "vai" do Miguel
- [x] AÇÃO 3 — regra editorial: vale a partir da indexação deste plano
