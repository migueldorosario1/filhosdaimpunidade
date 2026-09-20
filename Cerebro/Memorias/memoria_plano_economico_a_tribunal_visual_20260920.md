# Memória — PLANO ECONÔMICO A: implementação do tribunal visual substituto (2026-09-20)

**Sessão:** ZCode/Kimi K3 · **Ordem:** Miguel ("vai" após recado do Telegram "Juiz visual V4 fora do ar" sem assinatura) · **Fórum:** `Foruns/forum_plano_economico_a_tribunal_visual_20260920.md`

## Remetente do recado sem assinatura (resolvido)

O recado "Juiz visual V4 fora do ar / Gemini e Qwen-VL falharam / Heroes estão passando sem julgamento (fail-open)" veio de:
- Arquivo: `/root/tematicos/agentes_tematicos/v4/nucleo_visao.py` (funções `julgar_imagem` e `confirmar_imagem`), via `nucleo_telegram.enviar_relatorio(..., so="antigravity")`.
- Bot: `@cafezinhoantigravitybot` (TELEGRAM_TOKEN). Throttle 1x/24h em `agent_data/visao_alerta_throttle.json`.
- Cura (ordem "toda mensagem tem que ser assinada"): `nucleo_telegram.py` ganhou `_assinatura_origem()` (inspect: 2 frames acima = módulo chamador + hostname). `enviar_relatorio` agora anexa `\n\n— {módulo} @ {host}` em TODA mensagem. Testado com mock de requests.post: mensagem saiu assinada.

## Patches (todos com backup .bak_pre_plano_a_20260920)

| Host | Arquivo | Mudança |
|---|---|---|
| NYC | `tematicos/agentes_tematicos/v4/nucleo_visao.py` | cascata julgar/confirmar: gemini → tencent → **[kimi, deepseek]** → qwen; `_julgar_openai_compat/_julgar_kimi/_julgar_deepseek`; `_plano_economico_a()` = env `PLANO_ECONOMICO_A=1` OU `/root/controles_pause/plano_economico_a.pause` |
| NYC | `tematicos/agentes_tematicos/v4/nucleo_telegram.py` | assinatura obrigatória em enviar_relatorio |
| NYC | `v4_labs/contratos/v4_rotas_visao_v1.json` | rota `deepseek_vision` prio 25 (openai_compatible, DEEPSEEK_API_KEY, deepseek-v4-flash, max_tokens 1600) |
| NYC | `agente_roteador_llm.py` | `_plano_economico_a()` + anexo de kimi-for-coding/deepseek-v4-flash aos candidatos do tribunal do portal quando ativo |
| NYC | `v4_labs/config/llm_providers.json` | provider `kimi` (api.kimi.com/coding/v1, KIMI_VISION_API_KEY) |
| NYC | `.env.unificado` | `PLANO_ECONOMICO_A=1` (persistente — o arquivo .ativo sumiu 2x de controles_pause, algo varre a pasta; .pause + env sobrevivem) |
| DELL | `agentes_tematicos/agente_roteador_llm.py` | `_tribunal_escala_economica()` (Kimi→DeepSeek→Claude Haiku) chamada nos 2 pontos de falha do Gemini (HTTP error e exception) — mesma assinatura/prompt/parse da função original |

## Testes de produção (NYC, python do venv)

1. `py_compile` limpo nos 5 arquivos patcheados.
2. `julgar_imagem('/tmp/foto_real.jpg', 'Crescimento do mercado pet no Brasil')` → `deepseek: ✓ APROVADA: Cachorro ilustra mercado pet nacional.` (foto real do pug via picsum.photos).
3. Imagem vazia 64x64 → REJEITADA/NAO_CONFIRMADA (fail-close preservado no gate final).
4. Assinatura: mock de post capturou `— assinatura_test3.py @ Cafezinho-failover-vigia` no fim da mensagem (em produção sairá nucleo_visao.py).

## Descobertas colaterais

- **Kimi assinatura esgotou o limite semanal** (403 "weekly (7-day) usage limit" — a janela de 5h/7d da vigília é real e chegou ao fim). O degrau 1 do plano A hoje é o DeepSeek (saldo US$ 12,40 🟢; ~US$0,0003/análise).
- A pasta `/root/controles_pause/` teve o arquivo `.ativo` apagado 2x em minutos — usar `.pause` (padrão da casa) + env var.
- Wikimedia bloqueou curl sem UA completo; para testes de imagem usar picsum.photos ou UA de navegador.
- Tokens dos bots Telegram apareceram no stdout de teste (nunca registrar em fórum/memória — segredo).

## Rollback

`rm /root/controles_pause/plano_economico_a.pause` + remover `PLANO_ECONOMICO_A=1` do `.env.unificado` NYC + restaurar os 6 `.bak_pre_plano_a_20260920` (5 NYC + 1 Dell). Sem nada disso, o plano desliga sozinho quando o Gemini voltar a ter crédito (a cascata tenta gemini primeiro).
