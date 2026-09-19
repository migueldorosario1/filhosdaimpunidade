# Fórum — Moka: modelo da casa = DeepSeek V4 Flash (default do sistema) + UX 4.1

> Data: 2026-08-01 (noite) · Autor: ZCode · Status: ✅ EM PRODUÇÃO (commit `498c93d`, "Moka 4.1")

## 1. Decisão do Miguel (verbatim resumido)

- **"Vamos usar o DeepSeek V4 Flash como default de todo o sistema"** — mas **trocável**: o usuário troca nas configurações avançadas e o administrador troca o default (env).
- O V4 Flash é **por conta da casa** (pontos/assinatura) e **consome MENOS pontos** — o app deve **informar o custo** ("tokens por ponto") em cada opção.
- Arquitetura da chave (nota colada por Miguel, de consulta a LLM): a chave fica **só no backend** (env/cofre — nunca no navegador); uma chave atende muitos usuários simultâneos, mas o limite real = rate limits da conta + capacidade do servidor + custo + arquitetura. Arquitetura-alvo: **usuário → site → nosso servidor → fila → API do modelo**, com controle por usuário, limite de mensagens, cache, retry com backoff progressivo e teto financeiro. Em produção: chave por projeto, com orçamento e acompanhamento.

## 2. O que já era verdade / o que foi construído

- O gateway (`/ia/completar`, Tencent) **já rodava 100% server-side** com `DEEPSEEK_API_KEY` no `.env` (nunca no cliente) e **default já era `deepseek-v4-flash`** (`MOKA_DEEPSEEK_MODEL`) — a decisão formaliza e amplia.
- **Novo (4.1):**
  - `IaIn.modelo` opcional + **allowlist `MODELOS_CASA`** no gateway: `deepseek-v4-flash` (×1) e `deepseek-v4-pro` (×4 pontos). Modelo fora da lista → 400. Default custom do admin (env) passa com ×1.
  - `_debitar` aceita multiplicador; `llm_usada` registra o modelo real (auditoria).
  - App: **seletor "🚀 Modelo da IA da casa"** nas ⚙️ (bloco da conta de pontos) com **info de custo por opção** — "DeepSeek V4 Flash ☕ — ~90 mil tokens por ponto" vs "V4 Pro — ~8 mil tokens por ponto (custa 4× mais pontos)". Persiste em `localStorage("moka.modeloCasa")`; `iaCompletar` envia `modelo`; `gatewayProvider` aplica em TODAS as ações da casa (resumo/explicação/tradução de livro e vídeo).
  - 12 idiomas (set_model_*).

## 3. Tokens por ponto (a conta exibida)

1 ponto ≈ R$ 0,0909 (R$10/110) ≈ US$ 0,0164. Preço mesclado 75% in / 25% out (catálogo Cérebro):
- **v4-flash** ($0,14/$0,28 por 1M → mescla $0,175): **~90 mil tokens/ponto** — o econômico ☕
- **v4-pro** (regular $1,74/$3,48 → mescla $2,175): **~8 mil tokens/ponto** (promo até 31/05 melhora pra ~30 mil)

## 4. E2E ao vivo (conta de teste usuario_id=7)

| Teste | Resultado |
|---|---|
| sem `modelo` (default) | `debitado: 30` (resumo_video ×1), `llm_usada=deepseek-v4-flash` ✅ |
| `modelo: deepseek-v4-pro` | `debitado: 80` (transcricao_video_15min 20 ×4), `llm_usada=deepseek-v4-pro` ✅ |
| `modelo: gpt-99-ultra` | HTTP 400 ✅ |

Deploy gateway: backup `app.py.bak_pre_modelo_casa_20260801` + restart uvicorn (nohup/setsid — **pendente: systemd unit**).

## 5. UX 4.1 no mesmo deploy

- **FIX crônico do menu superior que sumia** (BUG-20260801-MOKA-MENU-SUPERIOR-SOME): botão de ocultar saiu do ☕ (marca — armadilha de clique) pro 👁/🙈; 🌐 sempre renderizado (sumia em PDF sem pdfSource).
- **Modal ANOTAR (📝) unificado**: um ícone só para **Resumir** e **Explicar** (antes dois 📝+🧠 — redundância cortada a pedido do Miguel) com **barra deslizante de tamanho**: resumo 5–50% das palavras da página (**máx. metade**), explicação 30–100%; escopo livro mantido no resumo; streaming + auto-save em anotações; 12 idiomas.
- **FIX 4.1.1 (02/08, `677e25b`) — popup flutuante:** o modal herdou overlay de tela cheia + fundo escuro do SummaryModal e "cortava quase metade inferior do livro" (report do Miguel: "a página do livro tem que continuar aparecendo inteira"). Virou **popup sem fundo escuro**: card na lateral direita no desktop (sobre a margem), folha inferior compacta (máx. 58vh) no celular, com **botão minimizar ➖** (pilula no canto — livro 100% livre durante processamento/leitura). Lição: overlay de tela cheia NUNCA mais para ferramentas de leitura — janela de IA convive com a página, não a substitui.

## 6. Pendências alinhadas à nota de arquitetura (Fase futura do gateway)

- **Fila** no gateway (absorver picos — hoje é chamada direta síncrona), controle de concorrência por usuário, limite de mensagens, cache de completions, retry com backoff, teto financeiro diário.
- Chave DeepSeek em "projeto" separado com orçamento (hoje usa a chave geral do cofre).
- Rate limits: monitorar 429 da DeepSeek em picos (mil usuários simultâneos não cabem no tier inicial).

## Registros

- Bugs do dia: `CEREBRO_NODE_BUGS_RESOLVIDOS.md` (menu-superior-some + msg técnica + botões "trecho")
- Moka 4.0 (transcrição da casa): `Foruns/forum_moka_video_transcricao_transkriptor_plano_v2_20260801.md` + memória homônima
- Catálogo de modelos: `CEREBRO_NODE_CATALOGO_MODELOS_LLM.md` (deepseek-v4-flash $0,14/$0,28, 1M ctx)
