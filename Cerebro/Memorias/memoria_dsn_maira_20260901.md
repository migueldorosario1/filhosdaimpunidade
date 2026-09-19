# 🧠 Memória — DSN Maíra: nascimento/ressurreição (01/09/2026)

**Fonte:** sessão DSH/us65 com o Miguel · fórum: `Foruns/forum_dsn_maira_ressurreicao_20260901.md`

## Fato

- Ordem por voz do Miguel (~12:4x): ressuscitar a Maíra (a antiga secretária "Mayra na Praia") como **DSN Maíra**, com voz humana rápida, acesso a memórias/agenda/e-mails, WhatsApp e controle sonoro do celular; ofício = SÓ conversar e transferir responsabilidade ao DS-N Chefe.
- 12:50 — Miguel criou bot novo no BotFather: **@mayranpraia_bot** (id 8684987835); token cofrado em `/root/.maira_telegram_token` (600, fora do repo).
- 13:00 — `maira.service` no ar no us65 (systemd 24/7, padrão dsc-minibot). Miguel mandou "oi" → resposta do cérebro DeepSeek às 13:00:32 (diário commitado). Chat adotado: 1894890759.
- Capacidades no ar: voz edge-tts Francisca+8% (1,8s), STT (Groq gsk_ no chat dela OU whisper local; **ordem explícita do Miguel 13:1x: sempre o MAIS PODEROSO = large-v3-turbo, aceitar swap**), /agenda, /emails (IMAP readonly), /procura (grep em todo o Cérebro), lembretes c/ scheduler+alarme, /toca (ntfy prioridade 5, tópico no cofre dela), /chefe (escalada via INBOX_MIGUEL.md), intercepta segredo §82, assinatura "— DSN Maíra · carimbo".
- ~13:1x — Miguel direcionou: **handoff pro ZM como operário** (prompt completo enviado ao Telegram dele pelo canal DSC) — ZM: atualizar /usr/local/bin no us65 + instalar na Tencent (ssh china, whisper turbo da escuta, segredos via scp, PARAR instância us65 antes — 1 bot = 1 getUpdates) + provas.

## Lição

- Bot com corpo próprio nasce em minutos quando o dono cria no BotFather e cola o token; o gargalo real é infra (SSH Tencent não sai do us65 sem chave do cofre GPG — resolver via ZM, que tem `ssh china`).
- Servidor de produção (WP) pede cuidado com modelo grande em RAM: o auto escolhe `small` com RAM<2,2GB; a ordem "mais poderoso" do Miguel passa a valer via config explícita e fica melhor na Tencent (whisper turbo já instalado lá).
- Canal Telegram do vault (bot DSC) é a via rápida pra entregar prompt colável ao Miguel — mais direto que ponte quando ele está no celular.

## Pendências (herdadas pelo ZM / próximas fases)

- F2 WhatsApp (Callmebot × ponte completa) · F3 controle sonoro total (Android Tasker / iPhone Atalhos — Miguel diz aparelho) · F4 ElevenLabs Flash · F5 ligações (Twilio, pago).

## 2026-09-01 14:36→15:0x BRT — MIGRAÇÃO P/ TENCENT (ZM/ZCode GLM-5.3, handoff DSH 13:15)

1. us65: `cp scripts/maira_bot.py /usr/local/bin/` (repo novo Groq+/procura, backup .bak_pre_repo) · config `whisper=large-v3-turbo` (.bak_pre_turbo) · restart 14:37:42 · pré-aquecido 14:40:21 · depois `systemctl stop+disable` (regra 1 getUpdates).
2. Tencent (china-install root + china ubuntu): pip `edge-tts`+`faster-whisper` 1.2.1 (--break-system-packages) · modelo large-v3-turbo 1,6G cp root→ubuntu cache · deepseek_env ubuntu (1ª tentativa do .env.unificado deu **401 — chave morta**; copiada a viva do us65, sha256 3c8902bc1abe48f7 conf. 2 lados) · segredos 6× pipe com sha256 idêntico · unit User=ubuntu · remote origin=espelho nyc.
3. Patch produção Tencent: constantes REPO/TOKF/CIDF/CFGF/OFFF/STDIR/DEEPSEEK_ENV/GMAILF/GROQ_KEYF `/root/→/home/ubuntu/` + REPO=/home/ubuntu/cerebro-miguel (py_compile OK; diff /root/maira_patch_tencent_20260901.diff; .orig_sem_patch_20260901 guardada).
4. Patch /emails: `M.search(None,'UNSEEN')` estourava 1MB (imaplib error command SEARCH) → SINCE 14d fallback 3d (backup .bak_pre_emailfix_20260901, py_compile, restauração automática no falha) — MESMO patch aplicado ao repo (upstream) neste commit. Prova: 3 não-lidos reais.
5. Boot Tencent 14:46:53 (pré-aquece 22s) · restart c/ patch 14:53:27 (18s) · RAM ok (~3G avail + swap 10G).
6. Provas E2E: ver fórum §7 (tabela). Exec das funções SEM importar o loop: `exec(compile(src[:corte],'maira_funcs','exec'))` com corte no marcador `# main` — getUpdates nunca tocado por terceiro.
7. Lições: .env.unificado pode ter chave morta (sempre testar 401 antes de culpar o código) · script sem `__main__` guard não pode ser importado em teste (loop roda) — corte do fonte é o caminho · repo Tencent = `/home/ubuntu/cerebro-miguel` (layout `cerebro/`), NÃO o /root/Cerebro (morto desde junho).

**Estado:** Maíra VIVA na Tencent (canônica), us65 parada/disabled. Falta: nota de voz real do Miguel (anúncio em voz entregue 14:51).

# 🧠 Memória — DSN Maíra: nascimento/ressurreição (01/09/2026)

**Fonte:** sessão DSH/us65 com o Miguel · fórum: `Foruns/forum_dsn_maira_ressurreicao_20260901.md`

## Fato

- Ordem por voz do Miguel (~12:4x): ressuscitar a Maíra (a antiga secretária "Mayra na Praia") como **DSN Maíra**, com voz humana rápida, acesso a memórias/agenda/e-mails, WhatsApp e controle sonoro do celular; ofício = SÓ conversar e transferir responsabilidade ao DS-N Chefe.
- 12:50 — Miguel criou bot novo no BotFather: **@mayranpraia_bot** (id 8684987835); token cofrado em `/root/.maira_telegram_token` (600, fora do repo).
- 13:00 — `maira.service` no ar no us65 (systemd 24/7, padrão dsc-minibot). Miguel mandou "oi" → resposta do cérebro DeepSeek às 13:00:32 (diário commitado). Chat adotado: 1894890759.
- Capacidades no ar: voz edge-tts Francisca+8% (1,8s), STT (Groq gsk_ no chat dela OU whisper local; **ordem explícita do Miguel 13:1x: sempre o MAIS PODEROSO = large-v3-turbo, aceitar swap**), /agenda, /emails (IMAP readonly), /procura (grep em todo o Cérebro), lembretes c/ scheduler+alarme, /toca (ntfy prioridade 5, tópico no cofre dela), /chefe (escalada via INBOX_MIGUEL.md), intercepta segredo §82, assinatura "— DSN Maíra · carimbo".
- ~13:1x — Miguel direcionou: **handoff pro ZM como operário** (prompt completo enviado ao Telegram dele pelo canal DSC) — ZM: atualizar /usr/local/bin no us65 + instalar na Tencent (ssh china, whisper turbo da escuta, segredos via scp, PARAR instância us65 antes — 1 bot = 1 getUpdates) + provas.

## Lição

- Bot com corpo próprio nasce em minutos quando o dono cria no BotFather e cola o token; o gargalo real é infra (SSH Tencent não sai do us65 sem chave do cofre GPG — resolver via ZM, que tem `ssh china`).
- Servidor de produção (WP) pede cuidado com modelo grande em RAM: o auto escolhe `small` com RAM<2,2GB; a ordem "mais poderoso" do Miguel passa a valer via config explícita e fica melhor na Tencent (whisper turbo já instalado lá).
- Canal Telegram do vault (bot DSC) é a via rápida pra entregar prompt colável ao Miguel — mais direto que ponte quando ele está no celular.

## Pendências (herdadas pelo ZM / próximas fases)

- F2 WhatsApp (Callmebot × ponte completa) · F3 controle sonoro total (Android Tasker / iPhone Atalhos — Miguel diz aparelho) · F4 ElevenLabs Flash · F5 ligações (Twilio, pago).


## 2026-09-01 14:36→15:0x BRT — MIGRAÇÃO P/ TENCENT (ZM/ZCode GLM-5.3, handoff DSH 13:15)

1. us65: `cp scripts/maira_bot.py /usr/local/bin/` (repo novo Groq+/procura, backup .bak_pre_repo) · config `whisper=large-v3-turbo` (.bak_pre_turbo) · restart 14:37:42 · pré-aquecido 14:40:21 · depois `systemctl stop+disable` (regra 1 getUpdates).
2. Tencent (china-install root + china ubuntu): pip `edge-tts`+`faster-whisper` 1.2.1 (--break-system-packages) · modelo large-v3-turbo 1,6G cp root→ubuntu cache · deepseek_env ubuntu (1ª tentativa do .env.unificado deu **401 — chave morta**; copiada a viva do us65, sha256 3c8902bc1abe48f7 conf. 2 lados) · segredos 6× pipe com sha256 idêntico · unit User=ubuntu · remote origin=espelho nyc.
3. Patch produção Tencent: constantes REPO/TOKF/CIDF/CFGF/OFFF/STDIR/DEEPSEEK_ENV/GMAILF/GROQ_KEYF `/root/→/home/ubuntu/` + REPO=/home/ubuntu/cerebro-miguel (py_compile OK; diff /root/maira_patch_tencent_20260901.diff; .orig_sem_patch_20260901 guardada).
4. Patch /emails: `M.search(None,'UNSEEN')` estourava 1MB (imaplib error command SEARCH) → SINCE 14d fallback 3d (backup .bak_pre_emailfix_20260901, py_compile, restauração automática no falha) — MESMO patch aplicado ao repo (upstream). Prova: 3 não-lidos reais.
5. Boot Tencent 14:46:53 (pré-aquece 22s) · restart c/ patch 14:53:27 (18s) · RAM ok (~3G avail + swap 10G).
6. Provas E2E: ver fórum §7 (tabela). Exec das funções SEM importar o loop: `exec(compile(src[:corte],'maira_funcs','exec'))` com corte no marcador `# main` — getUpdates nunca tocado por terceiro.
7. Lições: .env.unificado pode ter chave morta (sempre testar 401 antes de culpar o código) · script sem `__main__` guard não pode ser importado em teste (loop roda) — corte do fonte é o caminho · repo Tencent = `/home/ubuntu/cerebro-miguel` (layout `cerebro/`), NÃO o /root/Cerebro (morto desde junho).

**Estado:** Maíra VIVA na Tencent (canônica), us65 parada/disabled. Falta: nota de voz real do Miguel (anúncio em voz entregue 14:51). Commit us65→origin: efddd891f→d0aeb45fd (rebase autostash).
