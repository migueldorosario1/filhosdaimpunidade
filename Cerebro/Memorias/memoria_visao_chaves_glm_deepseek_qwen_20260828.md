# 🧠 MEMÓRIA TÉCNICA — Teste de chaves de VISÃO: GLM × DeepSeek × Qwen (28/08/2026)

**Sessão:** ZCode/DeepSeek (Dell) · Ordem do Miguel 28/08 ~09:40 · Fórum-irmão: `Foruns/forum_visao_chaves_glm_deepseek_qwen_20260828.md`

## 1. Escopo e método

Testar, com as chaves JÁ existentes nos cofres do Miguel, se os modelos de visão do GLM (assinatura Z.ai) e do DeepSeek funcionam e quanto custam — uso-alvo: Cafezinho (enxergar personagem/notícia/capa). Scripts em `/tmp/teste_visao_chaves.py`, `/tmp/teste_visao_fase2.py`, `/tmp/teste_visao_fase3.py`, `/tmp/teste_visao_fase4.py`. Chaves lidas por nome do cofre canônico `Outros/chaves/agentes_labs/.env.unificado` — **nenhum valor exposto** (auditoria por sha8).

## 2. Descoberta (GET /models)

- **Bases no .env.unificado:** TODAS as variáveis GLM apontam para `https://api.z.ai/api/coding/paas/v4` (base coding) ou `open.bigmodel.cn/api/coding/paas/v4`. A base padrão `api.z.ai/api/paas/v4` responde com as mesmas chaves.
- **Chaves GLM no cofre (3 contas distintas):** `ZAI_CODING_PLAN_API_KEY` sha8=`084efcbd` · `ZHIPU_CODING_API_KEY` sha8=`bf908cec` · (`ZAI_API_KEY`=`GLM_API_KEY`=`ZHIPU_API_KEY`=`BIGMODEL_API_KEY`) sha8=`151cc374` — mesma chave repetida em 4 variáveis (anotar p/ futura faxina do cofre).
- **Modelos de texto (200 em todas):** `glm-4.5, glm-4.5-air, glm-4.6, glm-4.7, glm-5, glm-5-turbo, glm-5.1, glm-5.2, glm-5.3, glm-5.3-flash`.
- **DeepSeek** `DEEPSEEK_API_KEY` sha8=`f0aaa272`: lista `deepseek-v4-flash`, `deepseek-v4-pro`, **`deepseek-v4-flash-vision-exp`** ✅.

## 3. Testes de visão (POST chat/completions com imagem base64)

Imagem de teste: capa do post 267802, `https://www.ocafezinho.com/wp-content/uploads/2026/08/foto-lula-flickr-jornalistica.jpg` (75.796 bytes, foto jornalística do Lula — Flickr). Atenção: capas NOVAS do site são `.avif` (o DeepSeek Vision só aceita jpeg/png/webp/gif; converter antes — ffmpeg local do Dell NÃO decodifica avif, testar outra ferramenta quando precisar).

- **GLM `glm-4.5v`/`glm-4.6v`** (existem na plataforma; `glm-5v`, `glm-4v-plus`, `glm-4v-flash`, `glm-4.1v` NÃO existem = 400): **429 `{"code":"1113","message":"Insufficient balance or no resource package. Please recharge."}` em TODAS as 3 contas, em ambas as bases** (z.ai e bigmodel). A assinatura Coding Plan NÃO inclui pacote de visão.
- **DeepSeek `deepseek-v4-flash-vision-exp`** ✅ 2/2 acertos:
  - Prompt longo (curador visual, 4 perguntas, max_tokens 400): identificou **Lula** ("Luiz Inácio Lula da Silva, atual presidente do Brasil"), descreveu solenidade militar c/ mão no peito e continência, "não há texto visível", aprovou como capa. `usage={prompt_tokens:495, completion_tokens:400, reasoning_tokens:252}`.
  - Prompt curto ("Quem é a pessoa? só nome e cargo", max_tokens 300): "Luiz Inácio Lula da Silva, Presidente do Brasil." `usage={prompt:415, completion:113, reasoning:98}`.
  - ⚠️ Com `max_tokens=60` devolveu CONTEÚDO VAZIO (o raciocínio comeu o teto) — usar `max_tokens ≥ 300`.
- **Qwen-VL `qwen-vl-plus`** (base aliyuncs `ws-x4x2zxwucryw1pr6`): prompt longo → **ERROU: "Jair Bolsonaro, deputado federal"** (1 rodada); prompt curto → acertou 2/2 ("Luiz Inácio Lula da Silva, Presidente da República"). Erro real mas não consistente — prompt complexo induz confusão.

## 4. Preços (fonte: docs.z.ai pricing + cobertura do lançamento DeepSeek 21/08)

| Modelo | Input | Output | Imagem |
|---|---|---|---|
| `deepseek-v4-flash-vision-exp` | US$0,22/M off-peak · 0,44 peak (cache hit 0,007) | US$0,66/M · 1,32 peak | máx **384 tokens/imagem** ≈ US$0,000084 |
| `glm-4.6v` | US$0,30/M (cache 0,05) | US$0,90/M | tokenizada junto |
| `glm-4.5v` | US$0,60/M | US$1,80/M | tokenizada junto |
| `qwen-vl-plus` | plano Token Plan (janela 5h) | — | — |

Peak DeepSeek = horário de Pequim 9–12h e 14–18h (01–04h e 06–10h UTC). Custo medido de 1 análise completa de capa ≈ 895 tokens ≈ **US$0,0003** (~10 mil análises por US$3).

## 5. Estado da missão

**O que aconteceu:** teste completo ao vivo — GLM (assinatura) NÃO tem pacote de visão; DeepSeek Vision SERVE com a chave do saldo e é o mais barato; Qwen-VL serve mas mostrou 1 erro de identificação com prompt longo.
**O que falta:** decisão do Miguel de plugar `deepseek-v4-flash-vision-exp` no pipeline visual do Cafezinho (auditor de capas/Tribunal Visual).
**O que preciso de você (Miguel):** "vai" para a troca do auditor visual (DeepSeek 1º + Qwen de dupla-checagem) e, se quiser GLM Vision, recarga de pacote na conta Z.ai.
