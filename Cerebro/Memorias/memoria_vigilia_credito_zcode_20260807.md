# Memória — Vigília de Crédito ZCode (failover Kimi K3 → Qwen Token Plan) — 07/08/2026

**Sessão:** ZCode desktop 3.6.5, modelo qwen3.8-max via provider "Qwen Code (Token Plan)" (id `2d084035-94d4-46dc-9068-bc5829b65375`), workspace ZCodeProject.
**Fórum par:** `Foruns/forum_vigilia_credito_zcode_20260807.md`

## 1. Contexto

~11:52 de 07/08 o crédito do Kimi K3 esgotou no meio do trabalho (6 erros `auth_failed` em cascata entre 11:52:49 e 11:54:40 na tabela `model_usage`). Miguel migrou esta sessão para o Qwen Code Token Plan (assinado por ele no mesmo dia, plano LITE) e pediu: failover automático + continuação da tarefa + monitoramento preventivo com checkpoint no Cérebro antes de esgotar.

## 2. Descobertas técnicas (verificadas ao vivo)

### 2.1 ZCode — onde mora cada coisa
- `~/.zcode/v2/config.json` — registro de providers do app desktop: top-level `provider` (dict por id) → `options.{apiKey,baseURL}`. Backup pré-existentes: `.bak_pre_qwen38_fix_20260807`, `.bak_pre_token_plan_20260807`.
- `~/.zcode/cli/config.json` — config do runtime (plugins, provider-ponte, `model` default, **hooks**). Backup feito: `.bak_pre_vigilia_20260807`.
- `~/.zcode/cli/db/db.sqlite` — tabelas: `session, message, part, model_usage, turn_usage, ...`. `model_usage` (19,8k linhas) tem: `provider_id, model_id, status ('completed'|'error'), error_type, error_code, error_message, input_tokens, output_tokens, reasoning_tokens, cache_read_input_tokens, started_at (epoch ms), session_id, ...` — telemetria perfeita p/ monitoria.
- `~/.zcode/v2/setting.json` — preferências do desktop (não guarda modelo default por provedor custom).
- Providers relevantes: `abc953f0-69af-46c9-bd91-6cb53f7edc2c` "Kimi 3" (`api.kimi.com/coding/v1`, modelo `kimi-k3`, contexto 1M); `2d084035...` "Qwen Code (Token Plan)" (`token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1`, modelo `qwen3.8-max`); `1b950583...` "Qwen 3.8 Max" (pay-as-you-go, emergência); `builtin:zai-coding-plan` GLM-5.2 (ativo).

### 2.2 Failover nativo: não existe
Grep do `app.asar`: nenhuma lógica de fallback de modelo em runtime (strings "fallback*" são da UI de plano de equipe). Runtime de hooks: eventos exatamente `SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PostToolUseFailure, Stop`; config-file hooks exigem `hooks.enabled: true`; saída stdout = JSON estrito; `additionalContext` injeta na conversa; `Stop` pode pedir continuação (até 3×); exit 2 bloqueia. Fonte: skill `diagnosing-hooks` (obs.: a string `additionalContext` não aparece no bundle da 3.6.5 — pode ser feature do runtime 3.7.x; teste ao vivo pendente, update 3.7.3 já baixado/pendente no app).
- O runtime de hooks NÃO está no `out/host/index.js` nem no `out/main/*` (só a UI de config de hooks); o parser deve estar no processo `zcode-cli`/`zcode-host-local-1` (mesmo binário `/opt/ZCode/zcode`, argv reescrito). Não foi possível extrair o schema exato → abordagem empírica adotada.

### 2.3 Kimi Code — quota
- **Não existe endpoint de quota:** `GET /v1/usage` 404, `GET /v1/dashboard/billing/subscription` 404, `GET /coding/usage` 404. `GET /v1/models` 200 (lista `k3`, `kimi-for-coding`, `kimi-for-coding-highspeed`, ...).
- **Assinatura de esgotamento:** `POST /v1/chat/completions` → **HTTP 403** `{"error":{"message":"You've reached your usage limit for this billing cycle. Your quota will be refreshed in the next cycle...","type":"access_terminated_error"}}` — não consome crédito. O ZCode registra isso como `error_type='auth_failed'`, mensagem "Provider authentication failed."
- **Calibração do orçamento** (soma de tokens de chamadas completadas ENTRE esgotamentos consecutivos, `model_usage`): 12 episódios desde 20/07; regime pesado 06–07/08: **221,1M** (06/08 12:31→14:58), **139,6M** (→21:07), **75,8M** (→03:17), **106,9M** (→11:52). Mediana ≈ 123M; mínimo 75,8M. Janela = 5h (plano). Hipótese: limite combinado 5h + 7 dias (orçamento por ciclo varia conforme consumo acumulado da semana).
- Headers do 403: só `X-Trace-Id` — sem informação de reset.

### 2.4 Chaves Kimi (Regra 4 — NENHUM valor exposto, só sha8)
| Variável/local | sha8 | Status ao vivo (07/08 ~12:15) |
|---|---|---|
| ZCode provider "Kimi 3" (`options.apiKey`) | `92aed0f2` | válida, ESGOTADA |
| `kimi_code.env` → `KIMI_CODE_API_KEY` | `6dcfcad3` | válida, ESGOTADA |
| `KIMI_VISION_API_KEY` (espelho → agora canônico tb) | `320da64b` | (não testada; era a do coding plan em 25/07) |
As duas primeiras são chaves distintas, ambas vivas — possivelmente contas/assinaturas diferentes (a testar: se janelas independentes, cabe rodízio de chave no provider quando uma esgota).

## 3. O que foi construído

### 3.1 `~/.zcode/hooks/credito_vigilia.py` (novo, chmod +x)
- Lê `model_usage` (sqlite read-only): última falha vs último sucesso por provider → estado; soma tokens janela rolante 5h; recalibra orçamento (mediana dos últimos 6 ciclos com >1M tokens).
- Níveis: 🟢 <40% / 🟡 ≥40% / 🟠 ≥60% ("checkpoint AGORA") / 🔴 esgotado (falha após último sucesso, ou probe 403 válido por 30 min).
- Modos: `--hook` (JSON `{"additionalContext": ...}`, sempre exit 0), `--status`, `--probe` (ativo, só em provedor esgotado; transição → Telegram via `ponte_cafezinho.py --send`), `--json`.
- Estado: `vigilia_estado.json`; log: `vigilia.log` (mesma pasta). Chaves lidas do config v2, nunca impressas.
- Providers configurados: `kimi` (fallback → Qwen Token Plan/qwen3.8-max) e `qwen_token_plan` (fallback → GLM-5.2). Probe kimi usa modelo `k3` + `thinking.disabled`; probe qwen usa `enable_thinking:false`.

### 3.2 Hooks em `~/.zcode/cli/config.json`
`hooks.enabled: true`; eventos `UserPromptSubmit` e `SessionStart` → `python3 /home/migueldorosario/.zcode/hooks/credito_vigilia.py --hook` (timeout 15s). Backup: `config.json.bak_pre_vigilia_20260807`.

### 3.3 `~/.zcode/AGENTS.md` — seção permanente "🕵️ VIGÍLIA DE CRÉDITO"
Protocolo por nível p/ qualquer sessão: 🟠 = commit + Cérebro + monitor antes de continuar; 🔴 = resumo no Cérebro + frase única ao Miguel ("troque no seletor p/ fallback e digite continue") + não insistir no provedor morto. Cadeia: Kimi K3 → Qwen Token Plan → GLM-5.2.

### 3.4 Cron
```
*/15 * * * * /usr/bin/python3 /home/migueldorosario/.zcode/hooks/credito_vigilia.py --probe >> /tmp/vigilia_credito_cron.log 2>&1
```
Backup prévio do crontab: `scratch/crontab_backup_pre_vigilia_20260807.txt`. Só consome crédito quando probe retorna 200 (recuperação) — ~2 tokens.

### 3.5 Cofres (Regra 4, backups `.bak_pre_vigilia_20260807_1221`)
- `KIMI_CODE_API_KEY_ZCODE` (= chave do ZCode sha8 `92aed0f2`) gravada em: `Outros/chaves/agentes_labs/.env.unificado` (canônico), `Projeto Cafezinho Agentes/root/.env.unificado` (espelho) e `Projeto Cafezinho Agentes/Outros/chaves/kimi_code.env`.
- `KIMI_VISION_API_KEY` (sha8 `320da64b`): estava só no espelho → copiada ao canônico.
- Verificação final por sha8: todos os espelhos conferem.

## 4. Testes executados
- `--status` e `--hook`: ok (saída correta, exit 0; 🔴 kimi / 🟢🟡 qwen conforme esperado).
- `--probe`: 1ª tentativa falhou silenciosamente (`chave_config_path` sem o nível `options` → `ler_chave` retornava None) → corrigido; 2ª tentativa ok: `probe kimi: http=403 esgotado=True` registrado em `vigilia.log` e `vigilia_estado.json`.
- Calibração histórica: query de episódios reproduzida 2× (rolling 5h e entre-esgotamentos) — a 2ª é a usada pelo script.
- **Pendente:** hook disparando ao vivo numa sessão real (só dispara no próximo prompt; validar `vigilia.log` + eventual erro de schema no log do ZCode `~/.zcode/v2/logs/`).

## 5. Comandos úteis (reuso)
```bash
python3 ~/.zcode/hooks/credito_vigilia.py --status    # panorama rápido
python3 ~/.zcode/hooks/credito_vigilia.py --probe kimi  # força probe
python3 ~/.zcode/hooks/credito_vigilia.py --json      # estado completo
tail -f ~/.zcode/hooks/vigilia.log                    # auditoria dos disparos
```

## 6. Pendências / riscos conhecidos
1. Schema `additionalContext` não confirmado no bundle 3.6.5 (ver §2.2) — se o log do ZCode mostrar "failed", adaptar (talvez precise do update 3.7.3 ou de formato alternativo).
2. Auto-troca do `model` default no cli/config.json: adiada (formato de ID de modelo de provider v2 não confirmado).
3. Rodízio das duas chaves Kimi quando uma esgota: ideia registrada, testar com crédito vivo.
4. Qwen Token Plan também tem janela 5h/7d — já monitorado pela mesma vigília (fallback GLM-5.2).

---

## ADENDO 16/08/2026 ~20:00 — Failover automático de LLMs (log técnico)

**Arquivos novos/alterados:**
- `~/.zcode/hooks/llm_fallback.py` (novo, ~430 linhas) — motor do failover. Modos: `--check` (cron, rede), `--rapido`, `--status`, `--json`, `--dry-run`, `--forcar <prov>` (teste), `--trocar <task_id> <prov>` (manual).
- `~/.zcode/hooks/fallback_config.json` — `frac_failover: 0.90`, `frac_retorno: 0.75`, `ds_min_usd: 2.0`, `cooldown_min: 30`, `cadeia: [kimi, qwen, glm, deepseek]`, `trocar_sessao_viva: true`, `mexer_config_cli: true`.
- `~/.zcode/hooks/credito_vigilia.py` — patch no `--hook`: chama `llm_fallback.hook_check(session_id)` e anexa linhas ao contexto; `salvar_estado` após `mensagem_contexto` (persiste cache de cotas). Backup: `.bak_pre_fallback_20260816`.
- Cron: `8,23,38,53 * * * * /usr/bin/python3 ~/.zcode/hooks/llm_fallback.py --check >> /tmp/llm_fallback_cron.log 2>&1 # FAILOVER_LLM_20260816` (8 min após o probe da vigília). Backup do crontab: `/tmp/crontab_bak_20260816_*.txt`.

**Formatos-chave descobertos (não documentados antes):**
- `tasks-index.sqlite`: colunas `model` de `tasks`/`automations` usam `<provider-uuid>/<model-id>[$variante]` (ex.: `abc953f0-…/kimi-k3$max`, `builtin:zai-coding-plan/GLM-5.3$enabled`). A coluna `provider` é sempre `glm` (= backend agent CLI, não o vendor — não mexer).
- A linha da task na tabela `tasks` espelha o modelo REAL em uso pela sessão (validado: sessão atual qwen3.8-max ↔ model_usage). Trocar a linha troca o modelo da sessão (base do failover de sessão viva).
- UUIDs: Kimi `abc953f0-69af-46c9-bd91-6cb53f7edc2c` (kimi-k3), Qwen Token Plan `2d084035-94d4-46dc-9068-bc5829b65375` (qwen3.8-max), GLM `builtin:zai-coding-plan` (GLM-5.3), DeepSeek `397f633c-73af-424a-a8fa-552e7818e123` (deepseek-v4-pro).
- `cli/config.json` usa formato `nome/modelo` (ex.: `kimi/kimi-k3`) na chave raiz `model`.
- `setting.json` NÃO guarda modelo default (só providers habilitados); novo default de sessão vem do seletor da UI.

**Saúde por provedor:** Kimi/Qwen = `consultar_db`+`avaliar` do credito_vigilia (doente em ≥90% da janela ou `esgotado`); GLM = `glm_quota` oficial (j5h/semana ≥90%); DeepSeek = `deepseek_saldo` (<US$2 ou indisponível). Cache local de telemetria em `fallback_estado.json:quota_cache` (TTL 10 min; hook nunca faz rede).

**Mecânica anti-flapping:** override por item guarda `original/atual/desde/motivo`; reversão só com original <75% E cooldown 30 min; modelo trocado na mão limpa o override; emergência (todos doentes) = menos doente.

**Testes executados (16/08 19:50-20:00):**
1. `--status` e `--check --dry-run` com telemetria real: GLM 🔴 semana 100%, DS $21,41, Kimi 89%, Qwen 34%.
2. `--forcar kimi --dry-run`: 2 automações Kimi (IPRoyal `42b81071`, CCTV `e3465bb3`) → qwen + default CLI → `qwen/qwen3.8-max`.
3. Bug achado e corrigido: dry-run contaminava `fallback_estado.json` (deepcopy do estado no dry-run).
4. Em cópia do banco (`/tmp/test_tasks.sqlite`): reversão CCTV qwen→kimi OK; sessão viva GLM→Kimi preservando `$max`; 2ª chamada idempotente.
5. Hook integrado ponta a ponta: exit 0, 2,6s, JSON válido.

**Como reverter tudo:** remover linha do crontab (`FAILOVER_LLM_20260816`), restaurar `credito_vigilia.py.bak_pre_fallback_20260816` e apagar `llm_fallback.py`/`fallback_*` — ou só `"habilitado": false` no `fallback_config.json` (mata o sistema sem tocar em nada).

---

## ADENDO 29/08/2026 ~00:25 — Grok prepaid no cabeçalho

**Arquivo alterado:** `~/.zcode/hooks/credito_vigilia.py` (backup `.bak_pre_grok_header_20260829`).

**Funções novas:** `_grok_monitor_chave()` lê `MONITOR_GROK=` de `~/cofre_intake/cofre_intake.env` (fallback nos `.env.unificado`); `grok_saldo(cache, ttl=240)` faz GET só-leitura em `management-api.x.ai/v1/billing/teams/a154fa36-8ed5-4f4f-857b-4d7ba204dbdb/prepaid/balance`, timeout 5s, fallback DoH/SNI só se não houver cache. Persistido em `vigilia_estado.json` → `grok_saldo: {ts, dados:{saldo, team}}`. Token nunca vai pro estado (prova: `xai-token-` ausente no JSON).

**Unidade:** `total.val` = centavos com sinal (`-799` → `abs/100` = 7.99 USD). Preview do ciclo 08/2026 confirmou o mesmo número em `prepaidCredits.val`.

**Cabeçalho:** inserido em `mensagem_contexto` logo após DeepSeek. Limiares: >10 🟢 / ≤10 🟡 / ≤5 🟠 / ≤1 🔴.

**Identidade §113:** `APELIDOS_MODELO` ganhou `grok-4.6` / `grok-4` / `grok` (o payload do hook desta sessão é `d9b87475-…/grok-4.6`; sem isso o texto antigo ainda dizia GLM).

**Provas:**
- `py_compile` OK
- `--status` intacto (kimi/qwen)
- `--hook` 0,38s exit 0; contexto contém `🟡 VIGÍLIA CRÉDITO — xAI Grok (prepaid cafezinho): saldo US$ 7.99`
- GET no time irmão `6adec541-…` = 403 (token amarrado ao cafezinho) — não monitorar esse time com esta chave

**Reversão:** `cp ~/.zcode/hooks/credito_vigilia.py.bak_pre_grok_header_20260829 ~/.zcode/hooks/credito_vigilia.py`

---

## ADENDO 29/08/2026 ~00:37 — OpenAI fora do cabeçalho

**Pedido Miguel:** tirar OpenAI do cabeçalho, salvo se existir jeito de obter crédito.

**Sondagem (sem expor chave):**
| Endpoint | ZCODE_OPENAI | OPENAI_API_KEY de produção |
|---|---|---|
| GET `/v1/models` | 200 | (não precisou) |
| GET `/v1/dashboard/billing/credit_grants` | 403 session key (browser) | — |
| GET `/v1/organization/costs` | 403 `api.usage.read` | 403 `api.usage.read` |
| GET `/v1/usage?date=2026-08-28` | 200 lista vazia | 200 lista vazia |

Conclusão: **não há saldo restante via chave secreta.** Usage Costs API exigiria Admin key com scope; mesmo aí é gasto, não prepaid.

**Patch:** apagada a linha hardcoded `OpenAI GPT-5.6 (pay-as-you-go): provider ativo…` em `mensagem_contexto`. Backup `.bak_pre_openai_out_20260829`. `--hook` 0,1s, `OpenAI` ausente do `additionalContext`.


