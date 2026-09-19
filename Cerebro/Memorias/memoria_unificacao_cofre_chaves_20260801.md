# MEMÓRIA — Auditoria fingerprint das chaves + base técnica da OPERAÇÃO COFRE ÚNICO (01/08/2026)

**Data:** 2026-08-01 ~12:40 BRT · Kimi K3 (ZCode), a pedido do Miguel
**Fórum irmão (plano + decisões):** `Foruns/forum_unificacao_cofre_chaves_20260801.md`
**Método:** auditoria por fingerprint `sha8` (sha256[:8] do valor). **Nenhum valor de chave foi exposto, copiado ou gravado nesta memória** — conforme COFRE_CHAVES ("ponteiros, não cópias").

---

## 1. Inventário de arquivos auditados (12)

| Label | Caminho | Bytes | mtime | Vars tipo-chave |
|---|---|---:|---|---:|
| CANONICO | `Outros/chaves/agentes_labs/.env.unificado` | 8.822 | 27/07 14:51 | 65 |
| root_env_unificado | `Projeto Cafezinho Agentes/root/.env.unificado` (espelho `/root/` servidores) | 11.902 | 27/07 04:42 | 75 |
| root_chaves_novas | `Projeto Cafezinho Agentes/root/chaves_novas.env` | — | — | 33 |
| root_chaves.env | `Projeto Cafezinho Agentes/root/chaves.env` (ponteiro, 0 chaves — OK) | 184 | 12/06 | 0 |
| labs_chaves.sh | `Outros/chaves/agentes_labs/chaves.sh` | — | — | 22 |
| labs_env_root | `Outros/chaves/agentes_labs/.env_root` | — | — | 50 |
| cafroot_chaves.sh | `Outros/chaves/cafezinho_root/chaves.sh` | — | — | 22 |
| cafroot_novas.sh | `Outros/chaves/cafezinho_root/chaves_novas.sh` | — | — | 0 |
| kimi_code.env | `Projeto Cafezinho Agentes/Outros/chaves/kimi_code.env` | — | — | 1 |
| kimi_paygo.env | `Projeto Cafezinho Agentes/Outros/chaves/kimi_paygo.env` | — | — | 1 |
| gsn_env.local | `Projeto Cafezinho Agentes/sites-v4/globalsouth/.env.local` | — | — | 1 |
| riocarta_vercel | `Projeto Cafezinho Agentes/sites-v4/riocarta/.env.vercel` | — | — | 1 |

**Total:** 96 variáveis-chave únicas; 65 no canônico. **Ausente e previsto pela Constituição:** `Projeto Cafezinho Agentes/.env.unificado` (ponteiro) — não existe.

## 2. DRIFT — mesma variável, valores diferentes (17 casos)

| Variável | Valor A (sha8 → arquivos) | Valor B (sha8 → arquivos) | Leitura |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | `3334781a` → CANONICO, root_env, labs.sh, cafroot.sh | `3b2a80d5` → **chaves_novas**, env_root | B = pré-rotação 09/07. **E B é o que o V4 carrega** (precedência chaves_novas). Explica Sonnet em circuit breaker. |
| `KIMI_API_KEY` | `f1e91a87` → CANONICO | `05fba1d7` → root_env, **chaves_novas** | B = conta que estava suspensa (429). Pós-recarga Miguel: Fase 0 testa as duas. |
| `OPENAI_API_KEY` | `f6a7d97d` → CANONICO, root_env, chaves_novas, labs.sh, cafroot.sh | `0a643fdb` → env_root | B = pré-rotação 18/07. Obs.: rotação 18/07 registrou `9ca13238` — canônico tem `f6a7d97d` ⇒ **houve rotação posterior NÃO registrada** (incidente de governança leve). |
| `GEMINI_API_KEY` | `62a36df0` → CANONICO, root_env, chaves_novas | `86dbeac9` → labs.sh, env_root, cafroot.sh | Duas contas/projetos → explica "juiz funciona" × "crédito esgotado". |
| `QWEN_API_KEY` | `850f5099` → CANONICO | `3af892f5` → root_env | B funciona (6/6 telemetria). Canônica não provada. |
| `PERPLEXITY_API_KEY` | `eaacf25c` → CANONICO, root_env | `d4abba9a` → chaves_novas, labs.sh, env_root, cafroot.sh | V4 carrega B (velha?). |
| `XAI_API_KEY` | `a328b6c4` → CANONICO, root_env | `b1835f12` → chaves_novas, labs.sh, env_root, cafroot.sh | V4 carrega B. |
| `BRAVE_API_KEY` | `0df143b7` → CANONICO, root_env, chaves_novas | `17ee3b18` → labs.sh, env_root, cafroot.sh | — |
| `GROQ_API_KEY` | `dd0b0050` → CANONICO, root_env | `31410206` → env_root | — |
| `TELEGRAM_TOKEN_ZIZI` | `54bfb5c1` → CANONICO, root_env, labs.sh, env_root, cafroot.sh | `bcad5f3a` → chaves_novas | Risco: bot de aprovação com token velho. |
| `X_BEARER_TOKEN` | `90d0c80b` → CANONICO, root_env, labs.sh, env_root, cafroot.sh | `2871df86` → chaves_novas | — |
| `TIKTOK_ACCESS_TOKEN` | `99f26d6b` → CANONICO | `e7515971` → env_root | — |
| `TIKTOK_REFRESH_TOKEN` | `0ef567d3` → CANONICO | `23bf4cb7` → env_root | — |
| `B2_REFORMA_APP_KEY` / `KEY_ID` / `KEY_NAME` | 3 vals → CANONICO | 3 vals → root_env | Credenciais de backup divergentes. |
| `VERCEL_OIDC_TOKEN` | `3eb39b95` → gsn_env.local | `b771771a` → riocarta_vercel | Esperado (projetos diferentes) — não é drift, é por-site. |

**Consistentes em todo lugar (saudáveis):** `DEEPSEEK_API_KEY` (`fe52ae94`), `FAL_API_KEY` (`cdeed67a`) — recargas de DeepSeek/fal.ai não exigem troca de chave.

## 3. ÓRFÃS — vivas fora do cofre canônico (31)

`ZHIPU_API_KEY` ⚠️ (gerador predominante do V4!), `ZHIPU_CODING_API_KEY`, `KIMI_VISION_API_KEY`, `QWEN_API_KEY_2`, `KIMI_API_KEY_2`, `MOONSHOT_API_KEY` (alias), `KIMI_CODE_API_KEY`, `KIMI_PAYGO_API_KEY`, `PEXELS_API_KEY`, `PIXABAY_API_KEY`, `UNSPLASH_ACCESS_KEY`, `UNSPLASH_SECRET_KEY`, `APIFY_TOKEN`, `GITHUB_TOKEN`, `GOOGLE_DEVELOPER_API_KEY`, `SEARCHAPI_API_KEY`, `B2_KEY`, `B2_KEY_ID`, `MOKA_SMTP_PASS`, `MP_ACCESS_TOKEN`, `MP_WEBHOOK_SECRET`, `PAINEL_AUTH_PASS`, `MUNDO_TRILHOS_WP_PASS`, `WP_PASS_GSN`, `WP_PASS_SOBERANIA`, `WP_PASS_FALLBACK`, `WP_APP_PASSWORD_CAFEZINHO`, `REVAI_ACCESS_TOKEN`, `REV_AI_API_KEY`, `TELEGRAM_TOKEN_IRMAO`, `VERCEL_OIDC_TOKEN` (por-site, fica fora mesmo).

Decisão na Fase 1: entram no v2 as vivas; aposentam-se as mortas (Fase 0 verifica).

## 4. ALIASES (mesmo valor, nomes diferentes) — manter, documentar

`ANTHROPIC_API_KEY`=`CLAUDE_API_KEY` · `KIMI_API_KEY`=`MOONSHOT_API_KEY` · `TELEGRAM_TOKEN`=`TELEGRAM_TOKEN_AUGUSTO` · `WP_APP_PASSWORD`=`WP_APP_PASSWORD_CAFEZINHO`=`WP_PASS`=`WP_PASS_CAFEZINHO` · `GSN_WP_PASS`=`WP_PASS_GSN` · `TELEGRAM_BOT_SECRETARIA_TOKEN`=`TELEGRAM_TOKEN_MAYRA_PRAIA` · `REVAI_ACCESS_TOKEN`=`REV_AI_API_KEY` · `WP_PASS_FALLBACK`=`WP_PASS_SOBERANIA`.

## 5. O mecanismo da bagunça — `agentes_tematicos/nucleo_tematico/chaves.py`

- Pastas varridas: `/root`, `/root/agent_data`, dirs locais, `Projeto Cafezinho Agentes/root`, `Outros/Agentes Labs`…
- **Ordem de arquivos:** `chaves_novas.env` → `.env.unificado` → `chaves_gsn/riocarta/cicero.env` → `.env` → `.env.local`.
- **`os.environ.setdefault` → o PRIMEIRO arquivo ganha.** Logo, no servidor, `/root/chaves_novas.env` (velho) **sobrescreve** `/root/.env.unificado` (canônico espelhado) para todas as vars que contém.
- Consequência medida: Anthropic velha, Kimi suspensa, xAI/Perplexity/Telegram-Zizi/X-Bearer velhos em produção — **o cofre canônico existia mas não mandava**.

## 6. AssemblyAI LLM Gateway (o coringa)

- **Endpoint:** `https://llm-gateway.assemblyai.com/v1/chat/completions` (OpenAI-compatible).
- **Chave mestra:** `sha8:77f59e59` — vista no Tencent em 29/05 (smoke Codex: `claude-haiku-4-5` HTTP 200). **Não consta de NENHUM arquivo de cofre auditado** → Fase 0 localiza; Fase 1 põe no v2 como `ASSEMBLYAI_API_KEY`.
- **Conta:** pay-as-you-go, autopay ativo; saldo 29/05: US$ 47,75; **Miguel confirmou crédito em 01/08**.
- **Modelos gateway (US$/1M tok in/out):** Claude Opus 4.7 (5,50/27,50) · Sonnet 4.6/4.5/4 (3/15) · Haiku 4.5 (1/5) · Haiku 3.5 (0,80/4) · Haiku 3 (0,25/1,25) · GPT-5.2 (1,75/14) · GPT-5/5.1 (1,25/10) · GPT-5 Mini (0,25/2) · GPT-5 Nano (0,05/0,40) · GPT-4.1 (2/8) · ChatGPT-4o (5/15) · Gemini 2.5 Flash Lite (0,10/0,40) · Flash (0,30/2,50) · Pro (1,25/10) · Gemini 3 Flash Preview (0,50/3) · 3 Pro Preview (2/12) · Kimi K2.5 (0,60/3) · Qwen3 32B (0,15/0,60) · Qwen3 Next 80B (0,15/1,20) · gpt-oss-20b (0,07/0,30) · gpt-oss-120b (0,15/0,60).
- **Uso atual:** zero providers `assemblyai` nos agentes V4 (`nucleo_llm.py` tem deepseek/kimi/glm/qwen/openai/openai_gpt55). Diagnóstico 01/08 registrou "rota AssemblyAI funcionou" para Sonnet — via componente Sobrenatural (não nos espelhos locais; vive no servidor).
- **Accounting:** custo registrado como `assemblyai_gateway:<modelo>` (aliases em `root/agent_data/precos_modelos.json`, Codex 29/05).
- **Governança vigente (Codex 07/05):** "não tocar em `agente_roteador_llm.py` sem proposta separada, consenso, rollback e validação de custo" → por isso este plano pede concordância do Claude antes de executar.

## 7. Cascata V4 — estado real

`PROVIDERS` em `nucleo_llm.py`: `deepseek` (deepseek-chat, temp 0.2) → `kimi` (moonshot-v1-128k, api.moonshot.ai — K2 nega 404 na internacional) → `glm` (glm-4.5-flash, base de `ZHIPU_BASE_URL`) → `qwen` (qwen-plus, base de `QWEN_BASE_URL_2`) → `openai` (gpt-4o-mini, temp 0.2) → `openai_gpt55` (gpt-5.5, sem temperature, max_completion_tokens).

`llm_ratings.json` (tarefas editoriais): auditoria/redação/curadoria/revisão/fact_check/periféricos → `claude-opus-4-8 → gpt-5.5 → gpt-5.4 → gemini-3.5-flash → gemini-2.5-pro (→ grok-4.3) → claude-sonnet-4-6`. Bloqueados globais: `claude-opus-*` (na prática liberado p/ superluxo), `gpt-5*`, `o1*/o3*/o4*`.

**Mapa assinatura × paygo (Kimi K3, 25/07):** Zhipu — Coding Plan `/coding/paas/v4` (glm-5.2 OK, $144/mês, renova 17/08) vs paygo `/paas/v4` ($0, erro 1113; grátis só glm-4.7-flash lento). Kimi — Coding `api.kimi.com/coding/v1` (`KIMI_VISION_API_KEY` `320da64b`; k3/kimi-for-coding OK; já usada no juiz visual V4) vs paygo `api.moonshot.ai/v1` (`KIMI_API_KEY`; saldo ~$22 em 25/07; suspensa em 01/08 → **recarregada por Miguel em 01/08**). Modelos Kimi novos exigem `temperature=1`.

## 8. Rastreabilidade desta operação

- Baseline de fingerprints: seções 2–4 desta memória (sha8 por var × arquivo).
- Manifestos de execução: `manifesto_unificacao_<ts>.json` gerados a cada fase (Fase 0 em diante).
- Fontes: auditoria local 01/08 + `CEREBRO_NODE_COFRE_CHAVES.md` + `CEREBRO_NODE_CHAVES_E_LLMS.md` + CHECKUP-005.
