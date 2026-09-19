# 🧠 Memória técnica — Investigação social (IG/FB/X) + plano Top 1 + Conselheiro (19/08/2026)

> Sessão: ZCode/Kimi K3 · ~14:40→15:20 BRT · Fórum irmão: `Foruns/forum_plano_social_top1_conselheiro_audiencia_20260819.md`
> **Zero posts de teste** (compromisso com o Miguel) — só leitura e desenho.

## 1. Inventário técnico verificado (read-only)

- **Vault social real:** `/root/.env` no NYC (não o chaves.sh!) — contém FB_PAGE_ACCESS_TOKEN, FB_PAGE_ID, IG_USER_ID, X_API_KEY(+SECRET), X_ACCESS_TOKEN(+SECRET), X_BEARER_TOKEN, CREATOMATE_API_KEY (+templates), INSTAGRAM_MAKE_WEBHOOK, *_PREMIUM_MODE. Os 2 cofres Dell têm as mesmas chaves (conferido por hash md5, sem expor valores).
- **Verificações read-only (NYC, /root/venv):**
  - X: `tweepy.OAuth1UserHandler` + `verify_credentials()` → **@ocafezinho** OK.
  - FB: GET graph.facebook.com/v19.0/{FB_PAGE_ID} → 200 "O Cafezinho".
  - IG: GET /{IG_USER_ID}?fields=username → 200 **ocafezinhooficial** (id 17841400848520269).
- **Publicadores:** `postador_meta.py` (Graph v19: /photos com imagem, /feed com link; usado por FB e IG); `postador_twitter.py` (Tweepy v1 OAuth1 + v2 Client; TWITTER_DAILY_LIMIT env, default 2); `postador_twitter_fio.py` = contrato DRY-RUN de fios (não publica; valida 280 chars, prompt-vazado, vídeo ≤512MB); `agente_creatomate_bridge.py` (render Reels/cards).
- **Estado dos agentes:** FB ativo (foto, cooldown 4h, sem LLM — fórum /root/forum_agentefacebook.md descreve o modo texto 4-5 parágrafos); Twitter pausado 19/05 (manifesto em /root/forum_agente_twitter.md: fios 5-8 tweets, 270 chars, anti-bait); Instagram NYC pausado 20/07; Instagram noturno local (scratch/card_v2, 22h) desligado 17/08 (fórum diz como religar).
- **Aprovação humana existente:** fluxo Creatomate retém em `pendentes_social.json` até OK via Telegram — reaproveitar na Etapa 1.

## 2. Gotchas registrados

- `grep` por "twitter" no cofre NÃO acha as chaves: elas se chamam `X_API_KEY*` — buscar por `^X_`.
- Credencial do IG é o token DA PÁGINA do Facebook (Meta unificada) — IG_USER_ID + FB_PAGE_ACCESS_TOKEN.
- O "Antigravity publica fio" referencia esta mesma stack (Tweepy OAuth1 no NYC).

## 3. Peças do plano (fórum §2-§4)

- Motor de dados: `/root/top_tendencias_push.py` (NYC) — Top 1 das 24h alimenta IG/FB/X às 09:30 BRT.
- Histórico: `/root/agent_data/top10_historico/AAAA-MM-DD.json` + cópia em `Cerebro/Dados/top10_historico/` → base dos tops semana/15d/30d/3m/6m/1ano.
- Conselheiro de Audiência: análise diária 07:30 (janelas dia→1ano) → `diretriz_conselheiro.json` (fail-soft) lida pelos intakes V4 + análises arquivadas (auto-alimentação). Fundir com o Radar (fórum 11:30).

---

## 4. Regras visuais + simulações locais (19/08 ~16:15)

- Regras do Miguel: SEM fundo escuro; imagem inteira 4:5; logo topo; textos embaixo c/ sombra por glifo; visão rejeita imagem com texto; preferir foto de pessoa; selo "TOP 1 DO CAFEZINHO" + data/hora + URL na imagem.
- Gerador: `~/ZCodeProject/social_simulacoes/gerador_card_top1.py` (PIL 12.1.1; Liberation Sans; logos `logo_cafezinho_branca/preta.png` do card_v2; sombra = camada RGBA 8 offsets + GaussianBlur 6-7; chip vermelho #d40000 rounded; creme #f7f1e3 no card de texto).
- Caso real da visão: foto do Top 1 (Ciro, anexo 266482) = print BandNews coberto de texto → REJEITADA; foto Lula×Putin (266522, Stuckert) limpa → usada nos 2 cards de simulação.
- Cards: `cards/01_top1_capa_lula_putin.jpg`, `02_top1_texto_lula_putin.jpg`, `99_REJEITADA_visao_cheia_de_texto.jpg` + README.md na pasta.
- ⚠️ Espelho cafezinho.news fora do ar desde ~16:00 (ping/ssh/http falham; NYC e canônico OK) — pendente verificar.
