# 🔑 FÓRUM — MOKA: MODO REVISOR GOOGLE (conta de teste + IA da casa via gateway com trava) — 05/09/2026

> Tema Duplo: este fórum (decisões) + `Memorias/memoria_moka_modo_revisor_google_20260905.md` (log técnico).
> Origem: ordem do Miguel 05/09 ~10h30 ("um modelo pra oferecer pro Google, já com credencial das minhas LLMs... tem que ter trava, limite... eu fiz um login e uma senha pra o Moka, um e-mail do Google só de teste — usa o mesmo... do OpenAI e já tá bom, porque ele já faz tudo").
> Irmãos: saga Play Store (`forum_moka_twa_android_play_store_20260807.md` — Astra cuida do appeal) · obra (`forum_obra_moka_chefia_zm_20260830.md`).

## O que aconteceu (sessão ZM GLM-5.3, 05/09 10:31→)

1. **A conta que o Miguel lembrava EXISTE:** `zcode.e2e.20260801@gmail.com` (criada 01/08 para os testes E2E do gateway de pontos, marcada "manter para testes futuros"). Estava ativa com 65 pts. É o LOGIN do modo revisor.
2. **O mecanismo que o Miguel lembrava também EXISTIA:** gateway `pontos_api` (Tencent :8420, `/ia/completar`) — IA da casa com login email+senha e débito por PONTOS (a trava pedida). Estava com a chave DeepSeek DEPRECADA no .env (503) e fora da UI desde o pivot BYOK (04/08).
3. **Gateway curado e estendido** (backups `.bak_pre_revisor_20260905` de app.py/.env/db):
   - `OPENAI_API_KEY` (da casa, testada viva HTTP 200) no `.env` do gateway — a chave NUNCA sai do servidor.
   - Allowlist `MODELOS_CASA` += `gpt-4o-mini` (1×) e `gpt-4o` (4×); roteamento por provedor (gpt-* → api.openai.com; demais → DeepSeek quando houver chave); failover preservado; modelos sem chave são pulados.
   - **NOVO `/ia/tts`**: voz neural OpenAI tts-1 (6 vozes), MP3 base64, débito ação `tts` (20 pts), trava de 1500 chars/chamada, débito só no sucesso.
   - Provas reais na conta revisor: texto gpt-4o-mini (tradução correta, 40 pts) e voz neural (MP3 45KB, 20 pts).
4. **Conta revisor pronta:** senha NOVA (ninguém lembrava a antiga) + saldo **1305 pts** (65+300+1000) = trava (~30 ações de texto + ~20 vozes; custo real à casa ~US$ 1-3 com gpt-4o-mini). Credenciais nos 2 cofres `.env.unificado` como `MOKA_REVISOR_EMAIL`/`MOKA_REVISOR_SENHA` (rito [SEGREDO], backups datados, sha8 eab5f63e idêntico nos dois). Valor entregue ao Miguel só no chat (precedente FAROL 24/08).
5. **App religado (commit `5b2d739`, push moka-ousadia main):** sem BYOK + conta logada → IA da casa em TODO o app (Reader/Harness/etc. via `resolveProvider` → `gatewayProvider`, default gpt-4o-mini) e **voz neural da casa no useTTS** (≤1500 chars, cache, fallback voz nativa preservado); seletor UI `MODELOS_CASA` += OpenAI; FAQ revisor (PT+EN) na /ajuda. BYOK continua优先 (quem tem chave usa a própria).

## Decisões

- **OpenAI como motor da casa do modo revisor** (ordem do Miguel: "do OpenAI e já tá bom — ele já faz tudo": texto, voz neural, transcrição). DeepSeek segue na allowlist como fallback futuro quando a chave voltar.
- **Trava = pontos** (débito por ação no servidor): impossível estourar além do saldo; revisor não precisa de chave nenhuma.
- **Ação tarifada genérica** `resumo_livro` (40 pts) para as tarefas de texto do modo casa (tradução de página, explicar, resumir, perguntar) — tarifação por tarefa fina fica para o Premium V3.
- **Ambiente: OUSADIA primeiro** (rito da casa) — o revisor testa em https://moka-ousadia.vercel.app; promoção a canônico só com aval do Miguel após validação.

## O que falta

1. E2E de UX no Ousadia (entrar com a conta em ⚙️ → traduzir palavra/página → voz neural) — precisa navegador com localStorage; Miguel valida (ou ZM em sessão dedicada com browser-use).
2. Vídeo no modo revisor: transcrição via /transcricao/job do gateway (Transkriptor) — ver envs do projeto Vercel do Ousadia; se ausente, revisor testa vídeo COM legenda (grátis).
3. Promoção ao canônico (pós-aval) para o app TWA da Play Store usar o mesmo fluxo.
4. Teto mensal no projeto OpenAI (dashboard) como cinto de segurança além dos pontos.

## O que preciso de você (Miguel)

- Receber o par e-mail/senha (entregue no chat da sessão) e testar no Ousadia: ⚙️ → Entrar → conta revisor → abrir livro → traduzir + ouvir. Depois passar ao Google no appeal.

— ZM · ZCode/GLM-5.3 · 05/09/2026 10:52 BRT

## Adendo 1 — PROVA E2E PELO CAMINHO PÚBLICO DO REVISOR (05/09 11:1x BRT)

- Pergunta do Miguel: "o revisor do Google vai conseguir usar com a minha chave?" → **SIM, provado de ponta a ponta pela URL pública do Ousadia** (mesma que o navegador do revisor usa):
  - GET https://moka-ousadia.vercel.app/api/pontos/painel/saldo (conta revisor) → 200, saldo 1305, extrato com os débitos tts/completar.
  - POST .../api/pontos/ia/completar (modelo gpt-4o-mini) → 200: traduziu "The reviewer can use the app without any key of his own." → "O revisor pode usar o aplicativo sem nenhuma chave própria." Débito 40, saldo 1265.
- Cadeia: navegador do revisor → Ousadia (Vercel, rewrite /api/pontos) → gateway :8420 Tencent → SUA chave OpenAI (só no servidor). Revisor usa a chave da casa SEM nunca vê-la; teto = saldo de pontos.
— ZM · ZCode/GLM-5.3 · 05/09/2026 11:16:02 BRT

## Adendo 2 — PROMOÇÃO AO CANÔNICO + CARTA AO GOOGLE + LIMITE 2000 (05/09 11:2x BRT, ordem do Miguel)

- **CANÔNICO PROMOVIDO** (ordem expressa): push `5159cca..5b2d739 obra/memoria:main` no repo moka (fast-forward; tag de backup `backup_pre_modo_revisor_20260905` no GitHub). Provas no www.mokareader.com: /ajuda 200 com FAQ revisor servido · /api/pontos/saldo da conta revisor respondendo. O TWA da Play Store abre o canônico → revisor do app instalado testa com a conta.
- **Limite:** saldo recarregado 1265→**2000 pts** (~45 ações de texto 40pts + ~25 vozes 20pts ou mix; custo real à casa ~US$ 1-3 com gpt-4o-mini). Suficiente para revisão completa; top-up a um pedido de distância.
- **CARTA EM INGLÊS pronta** (`Foruns/CARTA_REVISOR_GOOGLE_CONTA_TESTE_20260905.md`, com passo a passo do Console): conta exclusiva do time de revisão + instruções + esclarecimentos (sem paywall; BYOK opcional; login não obrigatório; saldo cortesia com top-up). Para colar em Policy → App content → Detalhes de login + reenvio pra análise (caminho rápido indicado pelo próprio Console em 27/08).
- Respostas ao Miguel: só quem tem o login usa a chave da casa? SIM (gateway autentica por conta; sem conta e sem BYOK não há IA da casa). Limites suficientes? SIM (2000 pts + top-up).
— ZM · ZCode/GLM-5.3 · 05/09/2026 11:20:17 BRT

## Adendo 2 — PROMOÇÃO AO CANÔNICO + CARTA AO GOOGLE + LIMITE 2000 (05/09 11:2x BRT, ordem do Miguel)

- CANÔNICO PROMOVIDO: push 5159cca..5b2d739 obra/memoria:main no repo moka — fast-forward, tag de backup backup_pre_modo_revisor_20260905 no GitHub. Provas no www.mokareader.com: /ajuda 200 com FAQ revisor servido e /api/pontos/saldo da conta revisor respondendo. O TWA da Play Store abre o canônico — revisor do app instalado testa com a conta.
- Limite: saldo 1265 para 2000 pts — cerca de 45 ações de texto de 40 pts + 25 vozes de 20 pts; custo real à casa ~US$ 1-3 com gpt-4o-mini. Top-up a um pedido de distância.
- CARTA EM INGLÊS pronta em Foruns/CARTA_REVISOR_GOOGLE_CONTA_TESTE_20260905.md — conta exclusiva do time de revisão + instruções + esclarecimentos — com passo a passo do Console; para colar em Policy, App content, Detalhes de login e reenviar pra análise.
- Respostas ao Miguel: só quem tem o login usa a chave da casa — SIM, gateway autentica por conta. Limites suficientes — SIM, 2000 pts + top-up.
— ZM · ZCode/GLM-5.3 · 05/09/2026 11:20:38 BRT
