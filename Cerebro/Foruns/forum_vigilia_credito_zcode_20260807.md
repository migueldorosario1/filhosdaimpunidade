# Fórum — Vigília de Crédito ZCode: failover Kimi K3 → Qwen Token Plan (07/08/2026)

**Sessão:** ZCode (Qwen Code Token Plan / qwen3.8-max), workspace ZCodeProject, chat direto
**Pedido do Miguel (voz):** quando acabar o crédito do Kimi K3, o ZCode deve automaticamente mudar para o Qwen Code Token Plan e **continuar a tarefa sem parar**; além disso, monitorar a situação do crédito para **parar um pouquinho antes de esgotar** (janela de 5h) e **gravar no Cérebro** para não perder nada.

## Decisões resumidas

1. **ZCode NÃO tem failover nativo de modelo** (verificado no bundle `app.asar` — strings de fallback são só UI de plano de equipe). Solução construída com **hooks + script + protocolo**: a troca do modelo na sessão ativa é 1 clique do Miguel no seletor (limitação do app), mas tudo o mais é automático.
2. **Kimi Code NÃO tem API de quota** (`/usage`, `/dashboard/billing/subscription` → 404). Sinais usados: (a) **passivo** — banco do ZCode `~/.zcode/cli/db/db.sqlite` tabela `model_usage` (erros `auth_failed` + soma de tokens); (b) **ativo** — probe mínimo `POST /chat/completions`: 403 `access_terminated_error` = esgotado (não consome), 200 = voltou.
3. **Orçamento auto-calibrado:** medido o consumo real entre esgotamentos consecutivos no banco: ciclos de 5h recentes = **75M–221M tokens** (mediana ~123M). A vigília recalcula sozinha a cada ciclo (média móvel dos últimos 6).
4. **Níveis e protocolo** (injetados em todo prompt via hook `UserPromptSubmit` + `SessionStart`): 🟢 ok / 🟡 atenção (40%) / 🟠 **checkpoint no Cérebro AGORA** (60%) / 🔴 esgotado → frase única ao Miguel ("troque para Qwen Code (Token Plan) e digite continue") — **a sessão mantém todo o contexto após a troca, nada se perde**. Cadeia de failover: **Kimi K3 → Qwen Token Plan → GLM-5.2 (Z.ai)**.
5. **Cron `*/15`** só faz probe ativo enquanto um provedor está esgotado (custo zero — 403 não consome); ao detectar a renovação da janela, avisa no **Telegram** via Ponte Cafezinho.
6. **Regra 4 aplicada:** descobertas 2 chaves Kimi Code VIVAS (a do ZCode sha8 `92aed0f2` e a do cofre `kimi_code.env` sha8 `6dcfcad3` — ambas válidas, ambas esgotadas agora; possivelmente assinaturas/contas diferentes). A do ZCode foi espelhada nos 3 cofres como `KIMI_CODE_API_KEY_ZCODE`; `KIMI_VISION_API_KEY` (sha8 `320da64b`) estava só no espelho → espelhada ao cofre canônico. Backups `.bak_pre_vigilia_20260807_1221` em tudo.
7. **Hoje (07/08 ~11:52) o Kimi esgotou de novo** — foi o que motivou esta sessão no Qwen. Estado atual da vigília: 🔴 kimi-k3 esgotado / 🟡 qwen em consumo.

## Estado / arquivos

| Item | Caminho |
|---|---|
| Script da vigília | `~/.zcode/hooks/credito_vigilia.py` (`--status` / `--hook` / `--probe` / `--json`) |
| Estado + log | `~/.zcode/hooks/vigilia_estado.json`, `vigilia.log` |
| Hooks | `~/.zcode/cli/config.json` (`hooks.enabled: true`; backup `.bak_pre_vigilia_20260807`) |
| Protocolo p/ agentes | `~/.zcode/AGENTS.md` seção "🕵️ VIGÍLIA DE CRÉDITO" |
| Cron | `*/15 * * * *` → `--probe`, log `/tmp/vigilia_credito_cron.log` (backup do crontab em `scratch/crontab_backup_pre_vigilia_20260807.txt`) |

## O que falta / próximos passos

- ~~**Teste ao vivo do hook**~~ — ✅ **CONFIRMADO 07/08 (mensagem seguinte do Miguel):** os contextos de `SessionStart` e `UserPromptSubmit` chegaram injetados na conversa (schema `additionalContext` **funciona no 3.6.5**, sem precisar do 3.7.3). Sistema completo e validado ao vivo.
- Possível evolução: auto-troca do modelo padrão (`model` no cli/config.json) enquanto o Kimi está esgotado — não feito ainda por risco de formato de ID errado; decidir com calma.
- Se as duas chaves Kimi forem de contas diferentes, dá para fazer **rodízio de chave** no provider quando uma esgota (a vigília já conhece as duas; falta testar com crédito vivo).

**Log técnico completo:** `Memorias/memoria_vigilia_credito_zcode_20260807.md`

---

## ADENDO 16/08/2026 ~20:00 — FAILOVER AUTOMÁTICO DE LLMs NO AR (ordem do Miguel)

**Pedido do Miguel (16/08 ~19:40):** "sempre que algum chegar a 90% da cota semanal ou de 5 horas, ou perto de fechar, você muda para outro LLM. O importante é as missões nunca serem interrompidas."

**Decisões:**
1. Motor novo `~/.zcode/hooks/llm_fallback.py` (+ `fallback_config.json`, estado `fallback_estado.json`, log `fallback.log`).
2. **Gatilho:** ≥90% da janela 5h (Kimi/Qwen, estimativa do banco) OU ≥90% da cota semanal/5h oficial (GLM, telemetria Z.ai) OU esgotado (403) OU saldo DeepSeek < US$2.
3. **Cadeia (prioridade):** Kimi K3 → Qwen Token Plan → GLM-5.3 → DeepSeek (assinaturas antes de dinheiro; DeepSeek último). GLM fica auto-excluído enquanto semana=100% (renova 21/08 02:16).
4. **3 camadas de atuação:** (a) automações ativas no `tasks-index.sqlite` + tasks-alvo; (b) sessão viva (linha da sessão na tabela `tasks`, via hook — troca entre turnos, contexto intacto); (c) modelo default do `cli/config.json`.
5. **Reversão automática** ao modelo original quando o provedor volta <75% (hysteresis) + cooldown 30 min. Troca manual do Miguel é respeitada (override removido, sistema não briga).
6. **Integração:** hook `UserPromptSubmit`/`SessionStart` chama `hook_check` (só cache/local, nunca rede) + cron `8,23,38,53 * * * *` → `--check` (com rede). Backup diário do tasks-index antes da 1ª escrita.
7. **Sem Telegram** (regra 15/08): eventos em `Cerebro/Foruns/fallback_llm_eventos.md` + visibilidade via contexto do hook em toda conversa.

**Testado (provas):** simulação forçada Kimi→Qwen em dry-run (2 automações + default CLI); reversão qwen→kimi em cópia do banco; sessão viva em GLM morto → Kimi preservando sufixo `$max`; idempotência; hook integrado 2,6s (timeout 15s).

**Estado da missão:** ✅ PRONTO E NO AR. **O que falta:** nada bloqueante. Observar o 1º failover real (Kimi a 89% no momento da instalação). Backups: `credito_vigilia.py.bak_pre_fallback_20260816`, `tasks-index.sqlite.bak_fallback_YYYYMMDD`, crontab `/tmp/crontab_bak_*`.


**Update 16/08 20:05 — 1º failover REAL + autorização DeepSeek:**
- **20:01:34 — 1º failover em produção (validação completa):** Kimi cruzou 91% → o hook desta conversa trocou sozinho as automações IPRoyal (`42b81071`) e CCTV (`e3465bb3`) para Qwen + default CLI. Eventos em `fallback_llm_eventos.md`. Reversão automática quando a janela do Kimi renovar.
- **Miguel AUTORIZOU usar DeepSeek como fallback** ("é crédito, mas pode usar") — já está na cadeia como último recurso (saldo US$ 21,40, piso US$ 2). Como o GLM está auto-excluído até 21/08 (semana 100%), a cadeia efetiva HOJE é Kimi → Qwen → DeepSeek.
- **Aprendizado:** o app ZCode reescreve `cli/config.json` (chave `model` virou `null` após a troca) — camada default-CLI é melhor-esforço; as camadas fortes são automações + sessão viva (essa cobre sessões novas no 1º prompt).

**Log técnico completo:** `Memorias/memoria_vigilia_credito_zcode_20260807.md` (adendo 16/08).

---

## ADENDO 29/08/2026 ~00:25 — Grok prepaid no cabeçalho da vigília (ordem Miguel)

**Pedido:** "você consegue entrar botar no cabeçalho dos posts o credito do grok?" (depois de colar `MONITOR_GROK` no cofre intake e as instruções da Management API).

**Decisões:**
1. **Sim, no ar.** O cabeçalho de todo prompt (hook `UserPromptSubmit`/`SessionStart`) agora inclui `🟡/🟢/🟠/🔴 VIGÍLIA CRÉDITO — xAI Grok (prepaid cafezinho): saldo US$ X.XX`.
2. **Fonte oficial:** token `MONITOR_GROK` (`xai-token-…`, sha12 `303dd9daa4a3`, intake 29/08 00:04) contra `GET https://management-api.x.ai/v1/billing/teams/a154fa36-…/prepaid/balance`. Time **cafezinho**. Só leitura. Nunca `POST` (não cria chave, não faz top-up).
3. **Unidade:** `total.val` vem em **centavos com sinal contábil** (`"-799"` = **US$ 7,99** restantes). Cache 4 min no `vigilia_estado.json` (`grok_saldo`). Sem valor de token no estado/log.
4. **Níveis (espelho DeepSeek, tetos menores porque o saldo é baixo):** 🟢 > US$ 10 · 🟡 ≤ 10 · 🟠 ≤ 5 · 🔴 ≤ 1. Medição ao vivo no smoke: **US$ 7,99 → 🟡**.
5. **O que NÃO faz:** failover automático continua DESLIGADO; a chave de chat do ZCode (`grok-4.6`) continua sem saldo; o outro time "O Cafezinho's Team" dá 403 neste token (amarrado ao cafezinho).
6. **Identidade:** apelido `grok-4.6` no `_modelo_do_payload` para o hook §113 não assinar GLM nesta sessão.

**Prova:** `python3 credito_vigilia.py --hook` com model `…/grok-4.6` → `additionalContext` contém a linha xAI Grok US$ 7.99; hook 0,38s; `py_compile` OK; backup `.bak_pre_grok_header_20260829`.

**Estado:** ✅ NO AR. **O que falta:** recarga do prepaid se o Miguel quiser (saldo baixo). **O que preciso do Miguel:** nada bloqueante.

**Log técnico:** `Memorias/memoria_vigilia_credito_zcode_20260807.md` (adendo 29/08).

---

## ADENDO 29/08/2026 ~00:37 — OpenAI SAI do cabeçalho (ordem Miguel)

**Pedido:** "tira o open ai, já que não tem. a menos que voce encontre uma maneira de obter do open ai? será que tem"

**Decisão:** **tira.** Sondagem ao vivo nas duas chaves (`ZCODE_OPENAI` sha8 `cfd708ae` e `OPENAI_API_KEY` sha8 `67d2ff31`):

- `/v1/dashboard/billing/credit_grants` e `/subscription` → **403 session key** ("only from the browser")
- `/v1/organization/costs` e `/v1/organization/usage/completions` → **403 Missing scopes: api.usage.read**
- `/v1/usage?date=` → 200 mas lista vazia, **sem saldo restante**
- chave secreta `sk-proj-` serve para `/v1/models` (chat), não para billing

Não há saldo oficial com o que temos. Voltar a mostrar OpenAI só se o Miguel criar uma **Admin API key** com `api.usage.read` (ainda assim é custo/uso, não prepaid restante — a OpenAI não expõe crédito restante na API de chave secreta).

**Patch:** removida a linha placeholder do `mensagem_contexto`. Backup `.bak_pre_openai_out_20260829`. Smoke `--hook`: `has_openai=False`, Grok/Kimi/DeepSeek/GLM/Qwen intactos.

**Estado:** ✅ NO AR. Nada a pedir ao Miguel.
