# 🎢 FÓRUM ESPELHO OUSADIA (Moka espelho 2) — nascimento aos poucos

> **Conceito (Miguel, 25/08 ~11:10):** dois espelhos — o **espelho 1 vira "ESPELHO CANÔNICO"** (moka-espelho.vercel.app; deve ficar IGUAL ao canônico + melhorias aprováveis; paridade espelho ⊇ canônico sempre) e nasce o **"ESPELHO OUSADIA" (espelho 2)** para os testes mais ousados do aplicativo. Feito aos poucos, 1 passo por rodada da automação diária (09:10).

## 📋 Estado (a ronda atualiza esta seção)

- **Passo atual:** ✅ PLANEA COMPLETO (F0–F5) — Espelho Ousadia NO AR
- **Concluídos:** F0 ✅ (25/08 09:10, rodada 1) · **F1–F4 ✅ (26/08 ~11:45, pela sessão principal — adendo 30 do fórum do espelho):** repo migueldorosario1/moka-ousadia criado + branch local `ousadia` + remote `ousadia-mirror` · projeto Vercel `prj_cAXX3GT1pVZTz6Efvs5qUqbB1D3Z` criado · 9 envs configuradas (NEXT_PUBLIC_SITE_URL + SUPABASE públicas + SMTP×4 + TRANSKRIPTOR + MOKA_MOTOR_KEY, sem exibição de valores) · badge 🎢 OUSADIA em todas as páginas (commit `99f07b4`) · **F5 ✅ (27/08 09:10, rodada 3):** provas finais — 7 rotas 200 (/, /configuracoes, /telemetria, /mural-das-ias, /estante, /ajuda, /biblioteca) + badge presente no bundle + deploy READY (`99f07b4`).
- **✅ PENDÊNCIA RESOLVIDA (26/08 09:17):** token Vercel PERMANENTE (`vcp_...`) instalado no auth.json do CLI a partir do `~/cofre_intake/`.
- **✅ Login no Ousadia LIBERADO (27/08 ~09:20):** Miguel adicionou `https://moka-ousadia.vercel.app/api/auth/callback` às Redirect URLs do Supabase e confirmou "funcionou" — login voltando pro Ousadia logado. Allowlist agora tem 7 URLs.
- **URL FINAL:** https://moka-ousadia.vercel.app · repo `migueldorosario1/moka-ousadia` · branch `ousadia` no repo `~/ZCodeProject/moka-app`

## 🪜 Plano F0–F5 (1 passo por rodada; ao concluir um, marque acima)

- **F0 — Pré-requisitos:** conferir `gh` autenticado (`gh auth status`), token Vercel legível em `~/.local/share/com.vercel.cli/auth.json` (GET /v6/deployments do espelho 1 deve retornar 200), e anotar as 2 env públicas do Supabase do bundle do espelho 1 (já conhecidas do fórum do espelho — NÃO re-extrair se o token falhar).
- **F1 — Repo GitHub:** criar `migueldorosario1/moka-ousadia` (público, mesmo modelo do espelho 1) + branch local `ousadia` (a partir da branch `espelho` atual) + remote `ousadia-mirror` + push inicial (espelho:main → ousadia main? NÃO: branch ousadia → main do repo novo).
- **F2 — Projeto Vercel:** criar projeto `moka-ousadia` via API (POST /v10/projects, name moka-ousadia, gitSource github migueldorosario1/moka-ousadia, productionBranch main, teamId team_QQzbgQTC569AoQxaur7tNLGj). Anotar projectId.
- **F3 — Env vars do ousadia:** NEXT_PUBLIC_SITE_URL=https://moka-ousadia.vercel.app + NEXT_PUBLIC_SUPABASE_URL/ANON_KEY (públicas, mesmas do espelho 1) + SMTP×4 + TRANSKRIPTOR_API_KEY + MOKA_MOTOR_KEY (valores SÓ dos cofres vivos — nunca exibir) + commit vazio de rebuild + push.
- **F4 — Badge do ousadia:** na branch `ousadia` (NUNCA na espelho), estender o badge 🧪 pra incluir "ousadia" no SITE_URL (`.includes("ousadia")`) + commit + push + aguardar READY + prova: home 200 e badge presente no bundle.
- **F5 — Fechamento:** provas finais (5 rotas 200) + 🔴 pendência OPCIONAL do Miguel: liberar login no ousadia (Supabase → Redirect URLs → `https://moka-ousadia.vercel.app/api/auth/callback`) — só se ele quiser testar login lá + relatório final ao Miguel por Telegram (`ponte_cafezinho.py --send`) + **propor o desligamento desta automação** (missão cumprida).

## 🚨 Regras inegociáveis da ronda

1. Ler ESTE fórum antes de tudo; atualizar "Estado" ao fim de cada rodada.
2. **1 passo por rodada** (no máximo; se falhar, registrar o erro e tentar de novo na rodada seguinte — máx. 2 tentativas por passo; depois Pausar e avisar o Miguel por Telegram).
3. **NUNCA commitar/pushar na branch `espelho` (espelho canônico) nem na `main`** — só na branch `ousadia` e no repo novo.
4. Commits como `ZCode/GLM-5.3 <migueldorosario1@users.noreply.github.com>`.
5. Nunca exibir valores de env/segredos (Regra do Cofre).
6. Ao concluir F5: relatório + sugerir CronDelete desta automação ao Miguel (a automação se encerra com aval dele).

---

## 🔑 YouTube Data API v3 + innertube + proxy residencial — PANE TRIPLA RESOLVIDA (27/08 ~12:20)

**Contexto:** o Miguel criou a YouTube Data API v3 key no Google Cloud (projeto "GA4 e YouTube") e depositou no cofre intake (`ZCODE_MOKA_YOUTUBE`), guiado por print passo a passo.

**O que a chave oficialmente dá (testado ao vivo):**
- `videos.list` ✅ 200 (ficha: título/canal/duração/descrição/thumbs — 1 unidade de quota)
- `search.list` ✅ 200 (coleta por tema, 100 unidades; cota 10.000/dia)
- `captions.list` ✅ 200 (lista idiomas de legenda)
- `captions.download` ❌ **401 — exige OAuth2** (API key não serve; Google não entrega texto de legenda de terceiros por key)

**A via nova que destravou a transcrição (sem OAuth, sem yt-dlp, sem Transkriptor):**
1. `POST /youtubei/v1/player` com client **ANDROID** (innertube, sem chave) → `playabilityStatus OK` + `captionTracks` com baseUrl assinada
2. `GET baseUrl&fmt=json3` → srv3 (XML) ou json3 → parser novo
3. Validado: Rick Astley pt-BR manual (60 blocos) e **g1 asr pt (127 blocos, 2.230 chars — pergunta completa do jornalista)**

**Pega descoberta na Vercel:** bot-check é por CLASSE de IP. Residencial = OK; datacenter (Tencent testado: LOGIN_REQUIRED) = bloqueado. A Vercel roda em datacenter.
**Solução:** `tubeFetch` com undici `ProxyAgent` pelo **IProyal recarregado** ($11,90/2GB ≈ 7 mil vídeos a ~300KB). Provado: Tencent+proxy = OK com tracks.

**Entregue (commit 8337140, promovido em cascata ousadia → espelho 1 → canônico):**
- `route.ts` do ingest: legendas em cascata **innertube(+proxy) → página HTML (fallback antigo)**; metadados em cascata **Data API v3 → innertube → oEmbed → og:title**; parser srv3 de bônus
- Envs Vercel: `YOUTUBE_API_KEY` + `PROXY_RESIDENCIAL_URL` nos 3 projetos (production+preview; pegadinha: POST com 3 targets juntos dá ENV_CONFLICT — criar 1 por vez)
- **E2E VERDE no Ousadia:** HTTP 200, 19 segmentos do g1, ficha oficial (duração 119s, upload 27/08, thumb maxres)
- Lote: 4d01f54 (Moka Video modernizado: barra %, LLM em uso, cancelar) + 670acdc (innertube) + 19b11a8 (proxy) + 8337140 (limpeza)
- Cofres: chave espelhada nos 3 (sha8 8b37fadc) + registrada no nodo do Cofre

**Estado:** o que aconteceu = transcrição de vídeo NO AR nos 3 ambientes (deploy de produção saindo no espelho/canônico ao concluir este registro). O que falta = Miguel testar a UX do vídeo no espelho (barra/cancelar do 4d01f54 nunca foram vistos por ele). Próximo de você (Miguel) = abrir moka-espelho.vercel.app/video, colar um link do YouTube e ver a mágica; se quiser, prometo E2E formal nos 2 domínios restantes antes do seu teste.
**Nota:** worker NYC (Whisper) e Transkriptor seguem como fallback para vídeo SEM legenda nenhuma — casos raros.

---

## 🤖 "Corrigida com IA" modernizada (27/08 ~12:45, relato do Miguel: "sem barra de tempo % e ficou travado rodando; abriu a caixa de tarefa falhou")

- **Causa raiz:** o submenu (pedido de 10/08) era a ÚNICA ação no caminho antigo `p.complete` SEM streaming — correção de transcrição grande = resposta longa de uma vez, muda (sem barra), e a conexão morria no timeout do proxy → "tarefa falhou".
- **Fix (commit 2b2d00c, promovido aos 3):** `correctTranscript` migrado pro `runStream` das demais análises (context+stream, `shouldCancel`, trava de cap em tempo real, telemetria `video-correct`). Painel: texto fluindo com cursor ▌ + overlay barra %/LLM em uso/⏹ cancelar + aviso amigável se cancelar antes do 1º texto (parcial é preservado, igual Reader).
- **Estado:** código novo confirmado servido no Ousadia; espelho 1 + canônico buildando no ato deste registro. Miguel testa clicando 📜 Transcrição → 🤖 Corrigida com IA no espelho.

---

## 🏛️ Menu "Política"→"Contexto" + 👥 Personagens mais firme (ordem Miguel 27/08 ~12:50, commit d9212e9)

- **Contexto:** rótulo renomeado nos 12 idiomas (video_tool_politics = Contexto/Context/Contexte/Kontext/Contesto/Контекст/背景/맥락/السياق/संदर्भ). Prompt reescrito: **todas as datas das falas viram datas concretas** (âncora = data de publicação, agora incluída no `videoHeader` via uploadDate da ficha oficial), conjuntura com antecedentes de quem são as partes, datas por extenso com mês e ano (regra Cafézinho — nunca "recentemente" solto), maxTokens 1600→1800. Aplica o mesmo rigor a tema não-político.
- **Personagens:** prompt endurecido — apresentadores/âncoras/entrevistadores **obrigatórios e em 1º lugar** ("quem conduz é personagem tanto quanto quem responde"), papel sempre específico (âncora/co-apresentador/repórter/entrevistador/convidado…), identifica também quem apresenta o PROGRAMA ( Breaking Points, JN…), depois entrevistados e por fim citados.
- Confirmado no ar nos 3 domínios (frase "datas e conjuntura do tema" no chunk page-[id] de cada um).

---

## 🔚 FECHAMENTO DA SESSÃO (27/08 ~13:15, pedido do Miguel: "sessão pesada — guarde na memória, desligue tarefa agendada, deixe prompt pra sessão nova")

- **Automação do Espelho Ousadia (F0–F5, 9h10/dia) DESLIGADA** com aval do Miguel (era a pendência: proposta de desligamento aguardava desde a ronda de fechamento do plano).
- Demais rondas (V4.1 30/30, telemetria 6/6h, Fênix 12/12h, segurança 48h, Instituto 9h, CCTV, caçadora) seguem ativas — outras missões.
- Checkpoint: memória harness `moka-transcricao-youtube-resolvida-20260827.md` + esta seção + memória técnica `memoria_youtube_transcricao_innertube_api_v3_20260827.md`.

### 📋 PROMPT DE RETOMADA (colar na sessão nova)
```
Retomando o Moka (pós-27/08). Antes de agir, leia (Regra Nº 1):
1. Cerebro/Foruns/forum_moka_ousadia_20260825.md — seções de 27/08
2. Cerebro/Memorias/memoria_youtube_transcricao_innertube_api_v3_20260827.md

ESTADO: transcrição de YouTube NO AR nos 3 ambientes (innertube ANDROID +
proxy IProyal + chave Data API v3); commit d9212e9 alinhado em tudo (mains,
deploys, chunks); "Corrigida com IA" modernizada; menu Contexto com datas;
Personagens com apresentadores. Automação do Ousadia desligada.

PENDÊNCIAS (na ordem): (1) meu feedback do teste da UX do vídeo (barra %,
cancelar, Contexto, Personagens); (2) "liga" do serviço de transcrição pago
(auditoria pane Transkriptor → reviver checkout tag pre-pivot-pago-v4.3 →
MOKA_CASA_TRANSCRICAO=1; alternativa AssemblyAI); (3) lote 2 i18n
(textos PT hardcoded, /privacidade, /sobre, slugs EN); (4) vídeo sem
legenda nenhuma (worker NYC ainda bloqueado). Repo: ~/ZCodeProject/moka-app,
branch ousadia, promover com push ousadia:main nos 3 remotes.
```

---

## Adendo — Ideia do Miguel 27/08 27/08/2026 14:17: BYOK-Transkriptor como fallback da transcrição de vídeo (parecer técnico)

**O QUE ELE PROPÔS:** quando a transcrição de vídeo falhar, recado pedindo a própria chave do Transkriptor da pessoa; raciocínio = sistema usaria o IP da pessoa + a gente já tem o iProyal.

**PARECER (ZCode/GLM-5.3):**
- A parte da CHAVE resolve e vale a pena: falha → recado → pessoa cola a chave (padrão BYOK do app, chave no dispositivo) → backend chama a API do Transkriptor passando SÓ a URL do vídeo → quem baixa do YouTube é o TRANSCRIPTOR, com IP DELES → o bot-check no nosso IP sai da jogada e o custo fica na chave da pessoa.
- O IP DA PESSOA não entra tecnicamente: o navegador dela não consegue ler os bytes de áudio do YouTube (bloqueio cross-origin) e o servidor não pode "emprestar" o IP de quem acessa. Mas o objetivo (tirar o download do nosso IP marcado) é alcançado do mesmo jeito — pelo IP do Transkriptor.
- Único caminho com o IP da pessoa de verdade seria ela mesma baixar o arquivo e subir pro Moka (UX ruim, descartado).
- Alternativa AssemblyAI (US$0,37/h): NÃO baixa YouTube — quem baixa continua sendo nosso innertube+proxy (funciona hoje, mas exposto ao bot-check).
- Estado checkado agora (27/08/2026 14:17): pane do Transkriptor PERSISTE — nenhum usage desde 25/08 (arquivos transkriptor_usage_*.json param em 25/08) e transkriptor_detalhe.json vazio no NYC. Diagnóstico da pane era "conta" (job evapora) — se for só da nossa conta, chaves de OUTROS usuários podem funcionar normalmente; confirmar com smoke de 1 job antes de codar o recado.

**O QUE PRECISO DO MIGUEL:** o "liga" pra montar (recado na falha + campo de chave Transkriptor nas configurações + rota server-side) e ok pra um smoke de 1 job (~1 vídeo da assinatura) quando a pane levantar.

---

## Adendo 2 — Pesquisa 27/08/2026 14:27: alternativa pay-as-you-go ao Transkriptor (resposta ao "me dá uma solução")

**CONTEXTO NOVO DO MIGUEL:** a pane do Transkriptor = CRÉDITO/ASSINATURA DELE encerrada (não pane do serviço) → chaves de OUTRAS pessoas com plano ativo funcionariam; ele não quer/não pode assinar agora e pediu alternativa barata PAYG com API.

**PESQUISA (web, 27/08 14:2x):**

| Serviço | Baixa o YouTube (IP deles)? | Sem legenda (ASR)? | Preço | Observa |
|---|---|---|---|---|
| **Supadata** ✅ | SIM (GET /v1/transcript?url=) | SIM — fallback Whisper automático | FREE 100 créditos/mês SEM CARTÃO; 1 crédito = 1 transcrição c/ legenda; ASR = 2 créditos/min (~US$0,68-1,20/h); auto-recharge US$10/1k | API REST simples (x-api-key), SDK JS/TS, 50+ idiomas |
| Transkriptor | SIM | SIM | assinatura ~US$6/vídeo | pane atual = conta do Miguel |
| TranscriptAPI | SIM (só puxa legendas) | NÃO (flag hasCaptions) | US$5/mês = 1k créditos (~0,5¢/vídeo) | barato p/ vídeos COM legenda |
| AssemblyAI | NÃO (download é nosso) | SIM | US$0,37/h | mais barato c/ ASR, mas mantém nosso innertube+proxy exposto |
| Sonix | SIM | SIM | US$10/h | caro |

**DECISÃO PROPOSTA (aguarda "vai" do Miguel):** Supadata como 1ª alternativa BYOK no seletor de transcrição de vídeo — plano FREE atende o Miguel HOJE (100 vídeos/mês com legenda, ~5 vídeos de 10min sem legenda) sem assinar nada. Multi-serviço no seletor (padrão das caixinhas 📖/🔊/🎬 de 26/08): Grátis (casa) · Supadata · Transkriptor · AssemblyAI.

**SPEC (se "vai"):** (1) provider Supadata no módulo de transcrição de vídeo + campo de chave nas configurações (padrão BYOK: chave no dispositivo, repassa por request); (2) recado na falha do caminho grátis oferecendo configurar chave; (3) ui-strings 12 idiomas LINHA-A-LINHA (nunca regex em massa — lição 27/08); (4) parte do Miguel: criar conta Supadata (2 min, sem cartão) e colar a chave.

**O que aconteceu / o que falta / o que preciso do Miguel:** pesquisa entregue ✅ · falta o "vai" para codar + conta Supadata do Miguel.

---

## Adendo 3 — 27/08/2026 14:47: ✅ BYOK DE TRANSCRIÇÃO NO AR NO OUSADIA (commit b57fa79, ordem Miguel ~14:35 "monta no Moka Ousadia, bota todos esses")

**O QUE FOI PARO NO AR** (https://moka-ousadia.vercel.app — SÓ o ousadia; espelho 1 e canônico NÃO receberam):
1. **⚙️ Configurações → seção nova "🎬 Moka Vídeo — serviço de transcrição"**: explicação bonitinha (grátis primeiro; sem legenda/bloqueio → SEU serviço com SUA chave), seletor 🎥 com 5 opções (Automático grátis · 🥇 Supadata · 📝 Transkriptor · 📄 TranscriptAPI · 🎙 AssemblyAI), campo de chave (criptografada no navegador, padrão BYOK), botão salvar, link "🔗 Como eu pego minha chave?" por serviço e nota de privacidade.
2. **/api/ingest**: ramo BYOK pós-captions (legenda grátis continua FIRST); quem baixa o vídeo é o SERVIÇO (IP deles). Síncronos (Supadata GET /v1/transcript com x-api-key; TranscriptAPI GET v2 Bearer) respondem na hora; assíncronos (Transkriptor tor.app com chave do usuário; AssemblyAI innertube→áudio→upload→poll com diarização) devolvem orderId e o cliente faz polling 12s (mesmo loop da casa). **Pegadinha corrigida no caminho:** o step status era interceptado pelo handler da CASA antes do BYOK (orderId do serviço morria no polling da casa) → BYOK-status agora intercepta antes; transcript mantém grátis-primeiro.
3. **Página de vídeo**: headers x-tx-service/x-tx-key em transcript+status; retomada de pendingJob só se o serviço é o mesmo; RECADO na falha quando não há serviço configurado → link "⚙️ Configurar serviço de transcrição"; nota honesta no "Ouvindo o vídeo" (sem pontos).
4. **/ajuda**: seção 🎬 com passo a passo de como pegar a chave em cada serviço (Supadata grátis 100/mês sem cartão; Transkriptor assinatura; TranscriptAPI US$5/mês; AssemblyAI dashboard US$0,37/h).
5. **ui-strings**: 18 chaves × 12 idiomas, LINHA-A-LINHA por ordem de aparição (método seguro pós-incidente do regex); conferido 18×12=216 presenças.

**PROVAS:** tsc 0 erros · build verde · smokes locais (MOKA_DISABLE_YTDLP=1): vídeo sem legenda (hTWKZoEtwcQ, Nirvana) + chave falsa → Supadata 401→"A chave do Supadata não funcionou…" · TranscriptAPI 401 idem · Transkriptor 502 amigável · status fake→422 · vídeo COM legenda continua grátis (captions antes do BYOK) · **produção**: deploy confirmado ao vivo (428 do deploy velho → 401 amigável do novo entre 2 polls), string "Supadata" no chunk servido 592-d22583d42086cd37.js, rotas /, /video, /ajuda, /configuracoes todas 200. Push: ousadia→main+ousadia no remote ousadia-mirror (d9212e9..b57fa79).

**Arquivos:** lib/video/byok-services.ts (NOVO) · transkriptor.ts (tk* aceitam chave BYOK) · api/ingest/route.ts · lib/config.ts (getTxService/setTxKey etc.) · video/page.tsx · SettingsForm.tsx · ajuda/page.tsx · ui-strings.ts (+1043/−27).

**O que aconteceu / o que falta / o que preciso do Miguel:** feature NO AR ✅ · falta: (1) Miguel criar conta no Supadata (2 min, grátis, sem cartão — supadata.ai) e colar a chave nas ⚙️ do ousadia pra E2E real; (2) AssemblyAI ainda sem E2E (sem chave real — adapter segue o padrão dos irmãos); (3) após aprovação no ousadia, promover pro espelho 1 e canônico (push main dos outros 2 remotes).

---

## Adendo 4 — 27/08/2026 15:04: ✅ BOTÃO "▶ TESTAR CHAVE" NO AR (commit 5993cac — pedido do Miguel ~15h: "tinha que ter um botãozinho de teste")

**O QUE É:** botão ao lado do "💾 Salvar chave" na seção 🎬 Moka Vídeo. Testa o que está no CAMPO (ou a chave já salva, se o campo está vazio) e mostra o resultado inline (verde "Chave aceita pelo Supadata ✅" / vermelho "A chave não foi aceita…").

**COMO TESTA SEM GASTAR CRÉDITO:** sonda que só checa autenticação — cutuca o serviço de um jeito que nunca transcreve nada: supadata GET /v1/transcript SEM url (401 = ruim; 400 = boa); transcriptapi idem sem video_url; transkriptor POST transcription/url com url VAZIA (403 com ruim — provado ao vivo); assemblyai GET /v2/transcript?page_size=1 (200 = boa, zero custo). **401/403 = rejeitada; qualquer outra resposta = aceita.** Os 4 pressupostos validados ao vivo com chave falsa antes de codar.

**INFRA:** rota nova `/api/tx-test` (POST {service, key}, chave no body HTTPS, nunca persistida) + `byokTestKey()` na byok-services + botão/estado no SettingsForm + chave `tx_test` × 12 idiomas.

**PROVAS:** tsc+build verdes · smoke local: fake→"não foi aceita" 200, vazio→400 amigável · produção: 404 (deploy velho) → 200 com rejeição (deploy novo) entre 2 polls · "Testar chave" no chunk novo 592-1c3cced24d718064.js. Push ousadia→main+ousadia (b57fa79..5993cac).

**Incidente menor do turno:** um comando com `pkill -f "next dev -p 3199"` matou o PRÓPRIO shell (a linha de comando do bash casava com o padrão) e o commit não rodou — percebido pelo git log intocado, refeito sem o pkill. Lição: pkill -f com padrão presente no próprio comando = suicídio; matar por PID.

**O que aconteceu / o que falta / o que preciso do Miguel:** botão NO AR ✅ · Miguel testa com a chave REAL do Supadata que ele já pegou (⚙️ → 🎬 → colar → ▶ Testar) · depois disso E2E de um vídeo sem legenda · promoção espelho+canônico após aval.

---

## Adendo 5 — 27/08/2026 15:08: ✅ SUCESSO DE TESTE COM ALEGRIA (commit 2fe9161 — pedido Miguel ~15h: "verde, fonte grande, negrito, mais animado")

**O QUE MUDOU:** classe nova `.feedback.ok-big` (16px, negrito 800, verde vivo #15803d/#4ade80 no dark, borda 2px, sombra e animação `ok-pop` de 0.4s — cresce e "pula") aplicada em: (1) "Testar conexão" das chaves de IA (2 pontos do SettingsForm, prefixo ✓ vira 🎉); (2) botão ▶ Testar chave da seção 🎬 (mensagem do server agora: "Chave aceita pelo X — tá tudo certo! Pode usar. 🎉").

**PROVA:** CSS novo servido (423f9d937d87500e.css, hash mudou do d75204b…) contendo ok-pop; tsc+build verdes; push ousadia→main+ousadia (5993cac..2fe9161).

**Nota:** resposta com feedback discreto continua igual (vermelho), só o SUCESSO ganhou festa.

---

## Adendo 6 — 27/08/2026 15:15: ✅ MULTI-SERVIÇO COM FALLBACK EM CASCATA (commit 8791b30 — ordem Miguel ~15:35 "pode mais de um, por ordem, com fallback, avisando quando cair")

**O QUE MUDOU (só ousadia, 2fe9161..8791b30):**
1. **⚙️ 🎬 virou LISTA**: cada serviço é uma linha com ☑ (ativar), badge **1º/2º/3º**, setas **▲▼** pra mudar a ordem, e — quando ativo — campo de chave próprio + ▶ Testar + 💾 + 🔗 como pego a chave. Explicação nova em destaque: "Pode ativar MAIS DE UM: o Moka tenta na ordem e, se um falhar, cai pro próximo sozinho".
2. **Cascata no cliente** (page.tsx): tenta o 1º da ordem → se falha, stage ao vivo mostra "⚠️ X falhou — caindo pro próximo serviço…" → tenta o 2º → … → esgotou a cadeia, segue pro caminho da casa (worker/casa/recado). Sucesso/pending interrompe a cascata na hora.
3. **Storage novo**: `mokavideo.txServices` (lista ordenada) + `mokavideo.txKey.<serviço>` (uma chave por serviço) + **migração automática** do formato antigo (serviço único + chave única) — o Miguel não perde a chave do Supadata que ele já colou.
4. **pendingJob** guarda o serviço dono do job; polling usa a chave dele (retomada coerente).
5. /ajuda: parágrafo novo com exemplo prático (Supadata 1º grátis + TranscriptAPI 2º — crédito acabou, segue no 2º sem fazer nada).
6. ui-strings: 6 chaves novas × 12 idiomas, linha-a-linha (tx_multi_note, tx_order_up/down, tx_step_trying/fellback/allfailed).

**PROVAS:** tsc+build verdes · 6×12 chaves conferidas · deploy provado ao vivo (parágrafo "fallback em cascata" na /ajuda entre tentativas 1→2).

**FALTA (frente 2, aguarda spec-avali do Miguel): FALLBACK DAS CHAVES DE IA** (tradução/explicação com fila de LLMs ordenável por função + aviso "X falhou, usando Y") — hoje NÃO existe (fact-check: nenhum fallback no ai-client/book-translate; erro sobe direto). Spec no chat.

**O que aconteceu / o que falta / o que preciso do Miguel:** cascata de transcrição NO AR ✅ · Miguel testa: ativar 2 serviços (ex.: Supadata real + TranscriptAPI com chave inventada) → o Testar mostra o 2º rejeitado e a transcrição deve cair pro 1º com aviso ao vivo · aval da frente 2 (LLM fallback).

---

## Adendo 7 — 27/08/2026 15:19: ✅ PERSONAGENS: fim das hashtags + entrevistador vem da DESCRIÇÃO (commit e4c7fd8 — relato Miguel ~15:4x)

**PROBLEMAS RELATADOS:** (1) aba Personagens com "muito sinalzinho/jogo da velha" — hashtags (#assunto) listadas como personagens; (2) nome do entrevistador está na DESCRIÇÃO do vídeo e não era aproveitado.

**FIXES:**
1. `videoHeader()` (vale pra TODAS as análises): descrição enviada LIMPA de hashtags (`#\w+` removido) — o ruído some na fonte.
2. Prompt de characters turbinado: bloco **"🔍 FONTES DOS NOMES"** em ordem de confiança — 1ª A DESCRIÇÃO ("costuma trazer quem apresenta/entrevista; extraia dela os apresentadores SEMPRE que mencionar"), 2ª como se chamam na fala, 3ª programa do título; falantes genéricos ('Falante 1') devem virar NOME REAL; bloco **🚫 PROIBIDO**: hashtags, @menções, links, nome de programa (só quem APRESENTA), temas, rótulos — "a lista é de PESSOAS".

**PROVA:** tsc+build verdes; "FONTES DOS NOMES" presente no chunk de vídeo servido (app/video/[id]/page-1fe0509a85232a9b.js) após deploy (8791b30..e4c7fd8).

**Pendente:** Miguel re-testa a aba Personagens no mesmo vídeo que mostrou o problema (Ctrl+Shift+R; a análise nova roda ao clicar a aba de novo).

---

## Adendo 8 — 27/08/2026 15:34: 🚀 PROMOÇÃO APROVADA PELO MIGUEL ("maravilha perfeito... leva para o espelho 1 e para o canônico")

**O QUE SUBIU (d9212e9..e4c7fd8, push fast-forward ousadia→main nos 3 remotes):** BYOK multi-serviço de transcrição (Supadata/Transkriptor/TranscriptAPI/AssemblyAI) + cascata de fallback com aviso ao vivo + botão ▶ Testar sem gastar crédito + sucesso festivo ok-big + Personagens sem hashtags c/ entrevistador vindo da descrição.

**PROVAS DE ALINHAMENTO (protocolo 3 ambientes):** /api/tx-test 200 ok:false no espelho e canônico (404→200 entre deploys) · "fallback em cascata" presente na /ajuda dos 3 · home+/video 200 nos 3 · **chunk de vídeo IDÊNTICO nos 3** (app/video/[id]/page-1fe0509a85232a9b.js contendo "FONTES DOS NOMES").

**Estado:** saga do dia 27/08 INTEIRA em produção nos 3 ambientes. Pendências que seguem: frente 2 (fallback das chaves de IA — spec no chat, aguarda aval) · E2E do Supadata com a chave real do Miguel · promoção futura volta a seguir o fluxo ousadia→espelho1→canônico.

---

## Adendo 9 — 27/08/2026 18:34: registro de propriedade do Moka (pedido Miguel ~16h "preciso registrar a patente... forma mais simples") + correção da análise 26/08

**RESPOSTA ENTREGUE (fontes oficiais 2026):** forma mais simples = 2 registros online no INPI, SEM patente:
1. **MARCA "Moka"** (e-Marcas): R$ 440/classe PF (50% off) / R$ 880 PJ — tabela 2026 (valor de 26/08 R$ 355 era antigo).
2. **SOFTWARE no INPI** (Lei 9.609/98 art. 17 — CORREÇÃO: a análise de 26/08 apontava FBN/cartório; o caminho legal do registro de programa de computador é o próprio INPI, agora tarifado pela Portaria INPI 10/2025 — valor exato na Tabela de Retribuições ao preencher). FBN (R$ 40 PF) = obras literárias; cartório RTD (~R$ 89+) = contratos de licença.
3. **PATENTE: NÃO** — software em si não é patentável (art. 10 LPI).
Prova extra de anterioridade grátis: repo Git com commits datados + fóruns do Cérebro. Memória [[moka-registro-invencao-inpi-marca-software-20260826]] ATUALIZADA com valores 2026 e a correção.

## Adendo 10 — 14/09/2026: ✅ SYNC canônico→espelho→ousadia + CURA DO SELETOR DE IDIOMAS NO AR (ordem Miguel 14/09)

- **Sync:** os 3 ambientes iguais ao canônico `2164349` (espelho via merge `-s ours` `428c570`; ousadia fast-forward nas 2 branches). Prova: 3 domínios 200 com link `/privacidade` do commit novo.
- **Cura das bandeirinhas** (bug: nomes cortando as primeiras letras + bandeirinha picada em árabe/híndi): causa = regra de grupo `.igot-topbar-actions button` (44×44/20px/center `!important`) esmagando os `.lang-option` + `max-height: 320px` não comportando os 12 itens. Fix commit `5d80145` (SÓ ousadia): seletor triplo de escape + `max-height: min(70vh, 460px)`. Provas numéricas antes/depois (local + produção ousadia) no fórum dedicado.
- **Registro completo:** `Foruns/forum_moka_bandeirinhas_idiomas_20260914.md` + `Memorias/memoria_moka_bandeirinhas_idiomas_20260914.md`.
- **Estado:** ousadia `5d80145` no ar; AGUARDA o Miguel conferir (https://moka-ousadia.vercel.app/estante → 👁️ → bandeirinha) para PROMOVER espelho+canônico. Telemetria no painel = sprint futuro.
