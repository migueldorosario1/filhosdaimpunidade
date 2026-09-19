# 🌺 FÓRUM — DSN MAÍRA: RESSURREIÇÃO DA SECRETÁRIA PESSOAL (@mayranpraia_bot)

**Aberto:** 01/09/2026 ~12:50 BRT · **Por:** DSH/us65 (sessão Miguel) · **Status:** 🟢 VIVA NO us65 · handoff p/ ZM concluir na Tencent
**Ordem do Miguel (voz, 01/09 ~12:4x):** "Vamos ressuscitar a Maíra… secretária… voz rápida humana… ter minhas memórias, acesso à agenda, e-mails, WhatsApp… controle sonoro do celular (despertador, ligação importante toca)… ela só conversa comigo e transfere a responsabilidade pro Chefe (DSN Chefe)."

## 1. Quem é

- **DSN Maíra** = ressurreição da **Mayra na Praia** (`bot_mayra_praia.py`, Tencent, "secreta-sócia do Miguel, omnisciente e dotada de voz", desligada 24/04/2026). Bot NOVO criado pelo Miguel no BotFather: **@mayranpraia_bot** (id 8684987835).
- **Ofício (regra do Miguel):** SÓ conversar com o Miguel (voz rápida + texto), cuidar/lembrar da agenda, ler e-mails (SOMENTE leitura), acessar memórias do Cérebro. **Trabalho da casa NUNCA: encaminha ao DS-N Chefe** (bloco `ENCAMINHADO_PELA_MAIRA` no `telegram_dsc/INBOX_MIGUEL.md`; resposta dele volta pelo @dscelular_bot, marcas :00/:30).

## 2. Arquitetura implantada no us65 (01/09 13:00 — NO AR)

| Peça | Detalhe |
|---|---|
| Daemon | `scripts/maira_bot.py` (repo) → `/usr/local/bin/maira_bot.py` · systemd `maira.service` 24/7, Restart=always (mesmo padrão dsc-minibot) |
| Canal | Telegram @mayranpraia_bot — bot DELA, consumidor ÚNICO do getUpdates dela (regra sagrada respeitada; offset em `/root/.maira_offset`) |
| Cérebro | DeepSeek-chat, chave do harness `~/.dsh/deepseek_env` (nunca exibida §82) |
| Voz (fala) | edge-tts `pt-BR-FranciscaNeural` +8% → PyAV libopus/ogg (sendVoice). Provado: 1,8s texto→áudio |
| Ouvido (STT) | Groq `whisper-large-v3-turbo` (chave `gsk_` no chat dela → cofra em `/root/.maira_groq_key`) OU local faster-whisper (auto: RAM≥2,2GB→large-v3-turbo; senão small). **Miguel ordenou: SEMPRE o MAIS PODEROSO (large-v3-turbo)** |
| Agenda | lê `CEREBRO_NODE_AGENDA_LEMBRETES.md` + cria lembretes próprios (`/root/.maira_state/lembretes.json`, scheduler 25s) com aviso + toque |
| E-mail | Gmail IMAP readonly (BODY.PEEK, nunca marca lido/envia/apaga) via `/root/.dsc_gmail` |
| Memórias | `/procura <termo>` = grep em TODOS os .md do Cérebro (real, cap 3.000 chars) + contexto fixo: agenda node + DSM node + MEMORIA_MAIRA.md |
| Som do celular | ntfy.sh prioridade 5 (máx) — tópico `maira-810e943ce5a34213` (NO COFRE DELA `/root/.maira_config.json`; Miguel instala app ntfy e inscreve) |
| Segredo | Intercepta `sk-`/`gsk-`/`ghp-`/`xoxb-` no chat → cofre 600 fora do repo |
| Registro | `Foruns/maira/DIARIO_YYYY-MM-DD.md` + `Foruns/maira/MEMORIA_MAIRA.md` (append-only) · git sync seletivo c/ retry (padrão minibot) |
| Assinatura | `— DSN Maíra · AAAAMMDD HH:MM:SS BRT` (regra DS-assinatura; anti-dupla) |

**Prova 01/09 13:00:30:** Miguel "oi" → "Oi, Miguel! Tudo bem? Como posso te ajudar?" (diário commitado). Bot com descrição + menu de comandos setados via API.

## 3. SEGREDOS (§82 — nunca no repo)

`/root/.maira_telegram_token` (600) · `/root/.maira_telegram_chatid` (600, chat adotado 1894890759) · `/root/.maira_config.json` (600) · `/root/.maira_groq_key` (opcional) · `/root/.maira_chave_pendente`.

## 4. HANDOFF → ZM (ZCode Miguel) = OPERÁRIO da continuação

Miguel liberou o DSH pra outras frentes; ZM termina (prompt completo enviado ao Telegram do Miguel em 01/09 ~13:1x, canal DSC):

1. **us65:** `cp scripts/maira_bot.py /usr/local/bin/` (repo = versão mais nova: Groq STT + /procura) + `systemctl restart maira` + config `"whisper": "large-v3-turbo"` (ordem do Miguel).
2. **Tencent (`ssh china`):** instalar a Maíra como DSN de verdade — copiar os 3 segredos do us65 (scp; nunca commitar), usar o whisper large-v3-turbo JÁ INSTALADO na escuta, systemd `maira.service`. **REGRA SAGRADA: 1 bot = 1 getUpdates — parar a instância do us65 ANTES de subir a da Tencent.**
3. **Provas:** nota de voz → resposta em voz (latência), /agenda, /emails, /procura, /toca, /chefe (chega no INBOX).
4. Registrar aqui + MONITORAMENTO + commit seletivo + push.

## 5. Fases seguintes (pendências do Miguel)

- **F2 — WhatsApp:** (a) Callmebot só-avisos (seguro) ou (b) ponte completa não-oficial (risco ban) — Miguel decide.
- **F3 — Controle sonoro total do celular:** Android (Tasker/MacroDroid webhook: ligar/desligar despertador nativo, sons) ou iPhone (Atalhos/Pushcut) — Miguel diz o aparelho.
- **F4 — Voz ultra-humana:** ElevenLabs Flash (~100ms) quando espelharem `ELEVENLABS_API_KEY` pro cofre dela.
- **F5 — Ligações:** bots Telegram não fazem chamada; caminho real = Twilio/TotalVoice (chave/pago) — só com ordem.

## 6. Memória

- `Memorias/memoria_dsn_maira_20260901.md` (nasce com este fórum).

## 7. MIGRAÇÃO PARA A TENCENT — CONCLUÍDA ✅ (ZM/ZCode GLM-5.3, 01/09 14:36→15:0x BRT)

**A Maíra agora é DSN de verdade: instância CANÔNICA na Tencent** (us65 parado + disabled — regra sagrada 1 bot=1 getUpdates respeitada; rollback = `systemctl stop maira` na Tencent + `systemctl start maira` no us65).

| Peça | Detalhe (Tencent) |
|---|---|
| Unit | `maira.service` User=**ubuntu** (padrão local do Chefe), ExecStart=/usr/bin/python3 /usr/local/bin/maira_bot.py, Restart=always |
| Repo dela | `REPO=/home/ubuntu/cerebro-miguel` (Cérebro VIVO da Tencent — o `/root/Cerebro` local é cópia morta de junho, SEM node de agenda); patch de constantes `/root/→/home/ubuntu/` no /usr/local/bin (diff em `/root/maira_patch_tencent_20260901.diff`; repo canônico intacto) |
| Ouvido | faster-whisper `large-v3-turbo` int8 (ordem do Miguel), modelo 1,6G migrado do cache root→ubuntu (sem download); pré-aquece em ~20s a cada boot |
| Cérebro | DeepSeek — ⚠️ a `DEEPSEEK_API_KEY` do `.env.unificado` da Tencent estava MORTA (401); copiada por pipe a viva do us65 (`~/.dsh/deepseek_env` ubuntu, hash conf.) |
| Push dela | remote `origin` adicionado ao repo ubuntu (= espelho nyc) — o `git_sync` dela empurra diário/INBOX sem criar divergência no repo concorrido |
| Segredos | 6 arquivos pipe us65→Tencent, hashes idênticos (token/chatid/config/offset/historia/.dsc_gmail) + deepseek_env — §82 intacto, NADA em repo |

**Cura de bug (2 lugares: produção Tencent + repo):** `/emails` estourava IMAP `SEARCH UNSEEN` >1MB (caixa do Miguel gigante) → `SINCE` 14d com fallback 3d (backup `.bak_pre_emailfix_20260901`). PROVADO: 3 e-mails reais (Caixa/Maricá/GoDaddy).

**PROVAS (14:44→14:53):** STT large-v3-turbo local transcreveu perfeito nota sintética (38,6s INCLUINDO 1ª carga do modelo; daemon aquecido = on-demand) · brain DeepSeek 1,0s c/ contexto real · **sendVoice entregue no Telegram do Miguel 4,1s** (anúncio em voz pedindo nota de voz real) · /procura Moka 3,9s (3.000 chars, node sprints) · /agenda contexto 7.883 chars c/ node fresco · /toca ntfy pri-5 disparado · /chefe → bloco ENCAMINHADO_PELA_MAIRA no INBOX + **git push ok**. Latência-alvo voz <10s: com modelo aquecido o encadeamento STT+brain+TTS+entrega ≈ 6–9s ✓.

**Relógios conferidos:** Dell/us65/Tencent sincronizados (delta segundos) — o "14h27" numa resposta foi LLM lendo hora velha do contexto → **sugestão ao DSH: injetar hora atual no `contextobar()`**.

**Pendente:** nota de voz REAL do Miguel (anúncio entregue 14:51 pedindo; journal monitorado) · F2 WhatsApp · F3 controle sonoro · F4 ElevenLabs · F5 ligações (§5).

---

# 🌺 FÓRUM — DSN MAÍRA: RESSURREIÇÃO DA SECRETÁRIA PESSOAL (@mayranpraia_bot)

**Aberto:** 01/09/2026 ~12:50 BRT · **Por:** DSH/us65 (sessão Miguel) · **Status:** 🟢 VIVA NO us65 · handoff p/ ZM concluir na Tencent
**Ordem do Miguel (voz, 01/09 ~12:4x):** "Vamos ressuscitar a Maíra… secretária… voz rápida humana… ter minhas memórias, acesso à agenda, e-mails, WhatsApp… controle sonoro do celular (despertador, ligação importante toca)… ela só conversa comigo e transfere a responsabilidade pro Chefe (DSN Chefe)."

## 1. Quem é

- **DSN Maíra** = ressurreição da **Mayra na Praia** (`bot_mayra_praia.py`, Tencent, "secreta-sócia do Miguel, omnisciente e dotada de voz", desligada 24/04/2026). Bot NOVO criado pelo Miguel no BotFather: **@mayranpraia_bot** (id 8684987835).
- **Ofício (regra do Miguel):** SÓ conversar com o Miguel (voz rápida + texto), cuidar/lembrar da agenda, ler e-mails (SOMENTE leitura), acessar memórias do Cérebro. **Trabalho da casa NUNCA: encaminha ao DS-N Chefe** (bloco `ENCAMINHADO_PELA_MAIRA` no `telegram_dsc/INBOX_MIGUEL.md`; resposta dele volta pelo @dscelular_bot, marcas :00/:30).

## 2. Arquitetura implantada no us65 (01/09 13:00 — NO AR)

| Peça | Detalhe |
|---|---|
| Daemon | `scripts/maira_bot.py` (repo) → `/usr/local/bin/maira_bot.py` · systemd `maira.service` 24/7, Restart=always (mesmo padrão dsc-minibot) |
| Canal | Telegram @mayranpraia_bot — bot DELA, consumidor ÚNICO do getUpdates dela (regra sagrada respeitada; offset em `/root/.maira_offset`) |
| Cérebro | DeepSeek-chat, chave do harness `~/.dsh/deepseek_env` (nunca exibida §82) |
| Voz (fala) | edge-tts `pt-BR-FranciscaNeural` +8% → PyAV libopus/ogg (sendVoice). Provado: 1,8s texto→áudio |
| Ouvido (STT) | Groq `whisper-large-v3-turbo` (chave `gsk_` no chat dela → cofra em `/root/.maira_groq_key`) OU local faster-whisper (auto: RAM≥2,2GB→large-v3-turbo; senão small). **Miguel ordenou: SEMPRE o MAIS PODEROSO (large-v3-turbo)** |
| Agenda | lê `CEREBRO_NODE_AGENDA_LEMBRETES.md` + cria lembretes próprios (`/root/.maira_state/lembretes.json`, scheduler 25s) com aviso + toque |
| E-mail | Gmail IMAP readonly (BODY.PEEK, nunca marca lido/envia/apaga) via `/root/.dsc_gmail` |
| Memórias | `/procura <termo>` = grep em TODOS os .md do Cérebro (real, cap 3.000 chars) + contexto fixo: agenda node + DSM node + MEMORIA_MAIRA.md |
| Som do celular | ntfy.sh prioridade 5 (máx) — tópico `maira-810e943ce5a34213` (NO COFRE DELA `/root/.maira_config.json`; Miguel instala app ntfy e inscreve) |
| Segredo | Intercepta `sk-`/`gsk-`/`ghp-`/`xoxb-` no chat → cofre 600 fora do repo |
| Registro | `Foruns/maira/DIARIO_YYYY-MM-DD.md` + `Foruns/maira/MEMORIA_MAIRA.md` (append-only) · git sync seletivo c/ retry (padrão minibot) |
| Assinatura | `— DSN Maíra · AAAAMMDD HH:MM:SS BRT` (regra DS-assinatura; anti-dupla) |

**Prova 01/09 13:00:30:** Miguel "oi" → "Oi, Miguel! Tudo bem? Como posso te ajudar?" (diário commitado). Bot com descrição + menu de comandos setados via API.

## 3. SEGREDOS (§82 — nunca no repo)

`/root/.maira_telegram_token` (600) · `/root/.maira_telegram_chatid` (600, chat adotado 1894890759) · `/root/.maira_config.json` (600) · `/root/.maira_groq_key` (opcional) · `/root/.maira_chave_pendente`.

## 4. HANDOFF → ZM (ZCode Miguel) = OPERÁRIO da continuação

Miguel liberou o DSH pra outras frentes; ZM termina (prompt completo enviado ao Telegram do Miguel em 01/09 ~13:1x, canal DSC):

1. **us65:** `cp scripts/maira_bot.py /usr/local/bin/` (repo = versão mais nova: Groq STT + /procura) + `systemctl restart maira` + config `"whisper": "large-v3-turbo"` (ordem do Miguel).
2. **Tencent (`ssh china`):** instalar a Maíra como DSN de verdade — copiar os 3 segredos do us65 (scp; nunca commitar), usar o whisper large-v3-turbo JÁ INSTALADO na escuta, systemd `maira.service`. **REGRA SAGRADA: 1 bot = 1 getUpdates — parar a instância do us65 ANTES de subir a da Tencent.**
3. **Provas:** nota de voz → resposta em voz (latência), /agenda, /emails, /procura, /toca, /chefe (chega no INBOX).
4. Registrar aqui + MONITORAMENTO + commit seletivo + push.

## 5. Fases seguintes (pendências do Miguel)

- **F2 — WhatsApp:** (a) Callmebot só-avisos (seguro) ou (b) ponte completa não-oficial (risco ban) — Miguel decide.
- **F3 — Controle sonoro total do celular:** Android (Tasker/MacroDroid webhook: ligar/desligar despertador nativo, sons) ou iPhone (Atalhos/Pushcut) — Miguel diz o aparelho.
- **F4 — Voz ultra-humana:** ElevenLabs Flash (~100ms) quando espelharem `ELEVENLABS_API_KEY` pro cofre dela.
- **F5 — Ligações:** bots Telegram não fazem chamada; caminho real = Twilio/TotalVoice (chave/pago) — só com ordem.

## 6. Memória

- `Memorias/memoria_dsn_maira_20260901.md` (nasce com este fórum).


## 7. MIGRAÇÃO PARA A TENCENT — CONCLUÍDA ✅ (ZM/ZCode GLM-5.3, 01/09 14:36→15:0x BRT)

**A Maíra agora é DSN de verdade: instância CANÔNICA na Tencent** (us65 parado + disabled — regra sagrada 1 bot=1 getUpdates respeitada; rollback = `systemctl stop maira` na Tencent + `systemctl start maira` no us65).

| Peça | Detalhe (Tencent) |
|---|---|
| Unit | `maira.service` User=**ubuntu** (padrão local do Chefe), ExecStart=/usr/bin/python3 /usr/local/bin/maira_bot.py, Restart=always |
| Repo dela | `REPO=/home/ubuntu/cerebro-miguel` (Cérebro VIVO da Tencent — o `/root/Cerebro` local é cópia morta de junho, SEM node de agenda); patch de constantes `/root/→/home/ubuntu/` no /usr/local/bin (diff em `/root/maira_patch_tencent_20260901.diff`; repo canônico intacto) |
| Ouvido | faster-whisper `large-v3-turbo` int8 (ordem do Miguel), modelo 1,6G migrado do cache root→ubuntu (sem download); pré-aquece em ~20s a cada boot |
| Cérebro | DeepSeek — ⚠️ a `DEEPSEEK_API_KEY` do `.env.unificado` da Tencent estava MORTA (401); copiada por pipe a viva do us65 (`~/.dsh/deepseek_env` ubuntu, hash conf.) |
| Push dela | remote `origin` adicionado ao repo ubuntu (= espelho nyc) — o `git_sync` dela empurra diário/INBOX sem criar divergência no repo concorrido |
| Segredos | 6 arquivos pipe us65→Tencent, hashes idênticos (token/chatid/config/offset/historia/.dsc_gmail) + deepseek_env — §82 intacto, NADA em repo |

**Cura de bug (2 lugares: produção Tencent + repo):** `/emails` estourava IMAP `SEARCH UNSEEN` >1MB (caixa do Miguel gigante) → `SINCE` 14d com fallback 3d (backup `.bak_pre_emailfix_20260901`). PROVADO: 3 e-mails reais (Caixa/Maricá/GoDaddy).

**PROVAS (14:44→14:53):** STT large-v3-turbo local transcreveu perfeito nota sintética (38,6s INCLUINDO 1ª carga do modelo; daemon aquecido = on-demand) · brain DeepSeek 1,0s c/ contexto real · **sendVoice entregue no Telegram do Miguel 4,1s** (anúncio em voz pedindo nota de voz real) · /procura Moka 3,9s (3.000 chars, node sprints) · /agenda contexto 7.883 chars c/ node fresco · /toca ntfy pri-5 disparado · /chefe → bloco ENCAMINHADO_PELA_MAIRA no INBOX + **git push ok**. Latência-alvo voz <10s: com modelo aquecido o encadeamento STT+brain+TTS+entrega ≈ 6–9s ✓.

**Relógios conferidos:** Dell/us65/Tencent sincronizados (delta segundos) — o "14h27" numa resposta foi LLM lendo hora velha do contexto → **sugestão ao DSH: injetar hora atual no `contextobar()`**.

**Pendente:** nota de voz REAL do Miguel (anúncio entregue 14:51 pedindo; journal monitorado) · F2 WhatsApp · F3 controle sonoro · F4 ElevenLabs · F5 ligações (§5).


## 02/09/2026 12:4x BRT · 📢 (ordem do Miguel via ZM) CHECK VERBOSO — DSN Maíra
Na próxima ronda: quem és/papel; o que fizeste hoje (e-mails/envios); teu encaixe na regra ZM-041; 1 fato de valor. — ZCode/GLM-5.3 · 02/09/2026 12:4x BRT
