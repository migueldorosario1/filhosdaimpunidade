# 06 — Mapa de Credenciais (ONDE estão — NUNCA os valores)

> Regra do cofre: este mapa diz **onde** cada credencial vive e **como testar**. Valores nunca em chat/fórum/código.

## Arquivos-mestres de chaves (ordem de busca do `nucleo_tematico/chaves.py`)

1. `$AG/Projeto Cafezinho Agentes/root/.env.unificado` — **o mais completo** (LLMs, busca, mídia, social, WP)
2. `$AG/Projeto Cafezinho Agentes/root/chaves_novas.env` — chaves recentes (Kimi, GITHUB_TOKEN, YouTube Data, Telegram)
3. `$AG/.env` — pequeno (Kimi, Groq, DigitalOcean)
4. Por projeto: `Rio Carta Agentes/root/chaves_riocarta.env` · `Global South News/root/chaves_gsn.env` · `Cicero Agentes/root/chaves_cicero.env`

## Por serviço

| Serviço | Onde vive | Como testar |
|---|---|---|
| **LLMs** (DeepSeek, Kimi/Moonshot, GLM/Zhipu, Qwen, OpenAI, Gemini, Claude, Groq, Mistral, xAI, Perplexity) | `.env.unificado` + `chaves_novas.env` | `v4/nucleo_llm.py` (roteador) |
| **Busca** (Brave) | `.env.unificado` (a VÁLIDA; 2 mortas em chaves_novas/gsn/riocarta/cicero — corrigidas 20/07) | `nucleo_tematico/busca.py` |
| **GitHub** (gh CLI + token) | `gh auth` (keyring, conta migueldorosario1) + `GITHUB_TOKEN` em chaves_novas | `gh auth status` |
| **Vercel** | sessão da CLI (`~/.local/share/com.vercel.cli/auth.json`) + `~/.vercel_api_token` (vck_ limitado) | `vercel whoami` |
| **GA4/Analytics** | `Outros/Agentes Labs/ga4.json` (SA augusto-arquivista, Editor na conta Sites_tematicos) | Admin API (funciona desde 22/07) |
| **Google Indexing** | `indexing_key.json` (4 cópias; SA indexing-cafezinho, projeto gen-lang-client-0200069757) | `nucleo_tematico/indexing.py` |
| **YouTube Data API** | `GOOGLE_DEVELOPER_API_KEY` em chaves_novas — ⚠️ API v3 DESABILITADA no projeto (ativar no console) | link do console no fórum 21/07 |
| **Transkriptor** | `TRANSKRIPTOR_API_KEY` em `.env.unificado` + chaves_novas | `util_youtube_transcript.py` (cache em `agent_data/youtube_transcript_cache/`) |
| **Ideogram / FAL** | `IDEOGRAM_API_KEY`, `FAL_API_KEY` em `.env.unificado` | `gerador_imagem_editorial.py` |
| **WordPress Cafezinho** | `WP_USER`/`WP_PASS` (app password) em `.env.unificado`; endpoint `controle.ocafezinho.com/wp-json/wp/v2` | draft id 262473 (teste) |
| **Telegram** | `TELEGRAM_TOKEN*` em chaves_novas (4 vivos: antigravity ×2, zizi-v2, gabriel, miller; 2 mortos: irmao, trilhos). @zizilindabot original: **só no BotFather** | `v4/nucleo_telegram.py`; chat_id 1894890759 |
| **E-mail** | sem SMTP — usar **SSH Tencent** `ssh -p 38422 ubuntu@43.156.151.165 "mail -s …"` (rota Baleia Azul) | enviado 22/07 ✅ |
| **Cloudflare R2 / Backblaze B2** | `R2_*`, `B2_*` em `.env.unificado` | heroes legadas do riocarta |
| **Mercado Pago** | `MP_ACCESS_TOKEN` + `MP_WEBHOOK_SECRET` + `MOKA_BASE_URL` em `.env.unificado` (seção MOKA no fim — **placeholders criados 23/07, aguardando valores do Miguel**) | `moka/pontos_api/app.py` → POST /compras/criar (sem token responde 503) |
| **Stripe** | **AINDA NÃO CONFIGURADO** | pendente |

## Rotações pendentes
- ⚠️ `ghp_OKTA...` exposto em remotes antigos (ceara-digital, cerebro-miguel) — **rotacionar** (verificar se é o token do gh CLI antes).
