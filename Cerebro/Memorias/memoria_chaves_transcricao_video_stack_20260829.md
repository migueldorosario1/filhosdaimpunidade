# Memória técnica — Consolidação das chaves de transcrição/download de vídeo (29/08/2026)

> **Sessão:** ZCode/Qwen 3.8 (Dell), 2026-08-29 ~00:41→01:00 BRT
> **Fórum correspondente:** `Foruns/forum_chaves_transcricao_video_stack_consolidado_20260829.md`
> **Gatilho:** ordem do Miguel ("vamos conseguir as chaves agora desses programas... ter tudo no cérebro para quando precisar baixar vídeo baixar a transcrição"), retomando a conversa do Moka Vídeo de 27-28/08.

## 1. Recuperação do contexto (Regras 1 e 2)

- `MONITORAMENTO_DE_TRABALHO.md` lido (linha da troca Transkriptor→Supadata de 28/08 ainda 🔄, pendência = chave Supadata).
- Memórias do ZCode consultadas: `supadata-byok-transcricao-video-20260827`, `moka-video-byok-transcricao-arquitetura-20260827`, `youtube-transcricao-innertube-api-v3-proxy-20260827`.
- Fórum-fonte: `forum_moka_ousadia_20260825.md` — adendo 2 (27/08 14:27) contém a pesquisa comparativa que originou "a lista": Supadata / Transkriptor / TranscriptAPI / AssemblyAI / Sonix (Sonix descartado por preço, US$ 10/h).

## 2. Varredura dos cofres (só NOMES, nenhum valor exposto)

- `~/cofre_intake/cofre_intake.env`: tem `ZCODE_MOKA_YOUTUBE` (entre outras). Sem Supadata.
- `.env.unificado` (os 2 espelhos: `Projeto Cafezinho Agentes/root/` e `Outros/chaves/agentes_labs/`): nomes encontrados = `TRANSKRIPTOR_API_KEY`, `ASSEMBLY_API_KEY`, `ASSEMBLYAI_API_KEY`, `IPROYAL_PROXY`, `ZCODE_MOKA_YOUTUBE` (+ variáveis de configuração `YOUTUBE_V2_*`, `YOUTUBE_PROXY_MODE`, `YOUTUBE_PREMIUM_MODE`).
- NYC (ssh `nyc` = root@198.199.121.136, BatchMode ok): `/root/chaves.sh` existe, **0 menções a SUPADATA** (instalar quando a chave chegar).

## 3. AssemblyAI — validação para transcrição (NOVIDADE)

- A chave `ASSEMBLYAI_API_KEY` (sha256-8 `77f59e59`, bate com o registro do fórum coringa de 16/08) é a chave mestra da conta pay-as-you-go usada no LLM Gateway (`llm-gateway.assemblyai.com`).
- Teste 29/08 ~00:47: `GET https://api.assemblyai.com/v2/transcript?page_size=1` com `Authorization: <chave>` → **HTTP 200**, `result_count=1` (há 1 transcrição antiga na conta). Sonda de listagem = custo zero.
- Conclusão: a MESMA chave serve para a API de transcrição (api.assemblyai.com/v2) e para o LLM Gateway. Encerra a pendência "AssemblyAI sem E2E (sem chave real)" do adendo 3 do fórum Moka Ousadia: o adapter BYOK do Moka pode receber essa chave.
- `ASSEMBLY_API_KEY` segue como espelho idêntico (roteador legado lê).

## 4. Supadata — caçada à chave

Linha do tempo verificada:
- Histórico do Chrome (perfil Default, via python3/sqlite com cópia do banco): **27/08 14:57** — signup `dash.supadata.ai/auth/sign-up?plan=free` → OAuth Google → callback → **14:58** página `dash.supadata.ai/organizations/532670f6-3d4e-4c9c-8aa6-f92afec8ca48/api-key-test`. Ou seja: conta existe e a chave foi exibida uma vez.
- 29/08 varredura completa nesta máquina:
  - localStorage de TODOS os perfis (UTF-8 e UTF-16, `.ldb`+`.log`): zero menções a `mokavideo`, `txKey`, `supadata` → a hipótese de 28/08 ("a chave mora no navegador dele, storage mokavideo.txKey") era FALSA: ele nunca colou a chave no Moka.
  - Cookies (`Default/Cookies` antigo e `*/Network/Cookies` de todos os perfis): zero cookies do Supadata → sessão descartada (cookie de sessão).
  - Não há `secret-tool` no Dell; decriptação de cookies seria via keyring (indisponível) — rota abandonada por inútil: não HÁ cookie para decriptar.
- Ação: navegador interno do ZCode (IAB; única backend anunciada) → `dash.supadata.ai/organizations` → redirect ao sign-in → botão "Google" (clique normal expirou; `locator.evaluate(el => el.click())` resolveu — widget de chat/overlay interceptava) → Google OAuth → **preenchi o e-mail `migueldorosario@gmail.com`** (achado em `~/.config/google-chrome/*/Preferences` → `account_info` do perfil Default; era o 1º da lista) → Google ACEITOU (avançou para `challenge/pwd` = conta correta).
- **Estado ao final:** aba aberta na tela de SENHA do Google. Só o Miguel digita. Depois do login, a chave aparece no dashboard (org `532670f6-3d4e-4c9c-8aa6-f92afec8ca48`, seção API Keys).

## 5. Transkriptor e TranscriptAPI

- `TRANSKRIPTOR_API_KEY` segue nos cofres, mas a assinatura do Miguel está encerrada (diagnóstico dele mesmo, 27/08) → credencial morta. Decisão: manter a variável no lugar (a cascata NYC `youtube_transcription_fallbacks.py` a lê como 2º provider; renomear quebraria sem ganho) e marcar o estado de morta no nodo do Cofre + fórum. Se re-assinar: colar chave nova por cima (Regra 4).
- TranscriptAPI (US$ 5/mês, só legendas existentes): não contratada — redundante com o free do Supadata (100 créditos/mês sem cartão).

## 6. Registros feitos

- `CEREBRO_NODE_COFRE_CHAVES.md`: seção nova "🎬 Stack de transcrição/download de vídeo — mapa de chaves (29/08/2026)" com a tabela do stack e a receita de instalação da Supadata.
- Este fórum + esta memória (Tema Duplo).
- `CEREBRO_NODE_ATUALIZACOES.md`: linha do tempo (a seguir).
- Monitor de trabalho: linha da sessão registrada ao começar, atualizada ao final.

## 7. Receita de instalação da SUPADATA_API_KEY (quando chegar)

1. Sonda sem custo: `GET https://api.supadata.ai/v1/transcript` SEM `url`, header `x-api-key` → **400 = válida / 401 = inválida** (pressuposto validado ao vivo em 27/08 no botão "▶ Testar" do Moka).
2. Backup dos cofres: `.bak_pre_supadata_<AAAAMMDD>` no intake e nos 2 `.env.unificado`.
3. Gravar `SUPADATA_API_KEY=<valor>` em: `~/cofre_intake/cofre_intake.env` · `.env.unificado` ×2 · NYC `/root/chaves.sh` (ssh `nyc`; o `youtube_transcription_fallbacks.py` lê do ambiente/chaves.sh).
4. sha256-8 nos 4 pontos → iguais; registrar o sha8 no fórum e no nodo.
5. E2E barato: 1 vídeo CURTO com legenda no pipeline NYC (1 crédito do free) — log `youtube_v2_pipeline` deve mostrar `provider=supadata` OK.
6. Opcional: colar nas ⚙️ do Moka (🎬 → Supadata) para o BYOK do app.

## 8. Como baixar vídeo/transcrição (estado da arte 29/08)

- **Com legenda (maioria):** innertube ANDROID + iProyal (Moka `/api/ingest` nos 3 ambientes; pipeline NYC). Zero chave.
- **Ficha/metadados:** `ZCODE_MOKA_YOUTUBE` (10k unidades/dia).
- **Sem legenda:** Supadata (chave pendente; baixa no IP deles) > AssemblyAI (chave pronta, US$ 0,37/h, download nosso) > Whisper NYC.
- **Bot-check:** datacenter precisa do proxy residencial; residencial direto passa.
- Preços Supadata (verificados 27/08): free 100 cr/mês sem cartão; 1 cr = 1 vídeo com legenda; sem legenda = 2 cr/min no Whisper (~US$ 0,68–1,20/h); recarga US$ 10/1k créditos; créditos não acumulam; NÃO usar a tradução deles (a LLM do Moka traduz).

## 9. O que aconteceu / o que falta / o que preciso do Miguel

- **Aconteceu:** auditoria e consolidação completas do stack; AssemblyAI provada para transcrição; mapa gravado no Cérebro; login do Supadata preparado até a tela de senha com a conta certa.
- **Falta:** senha do Google no painel (só o Miguel) → capturar a chave → receita da seção 7.
- **Preciso do Miguel:** 30 segundos no painel do ZCode (ou me passar a chave por chat/Telegram se preferir logar no Chrome dele).
