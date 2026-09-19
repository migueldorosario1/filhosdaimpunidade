# 📡 Fórum — DSC: credencial do terminal Telegram + aceleração (refs DSC-016/023/024/025) — 30/08/2026

> Tema Duplo: este fórum (decisões) + `Memorias/memoria_dsc_credencial_terminal_telegram_20260830.md` (log técnico).
> Ordem direta do Miguel (prompt único, 30/08 ~14:05 BRT — "MISSÃO ACELERAÇÃO, faça na ordem, com calma e prova"). Executor: ZM · ZCode/GLM-5.3.

## O que aconteceu (tudo com prova)

1. **Credencial gravada** — `TELEGRAM_TOKEN_DSC_BOT` + `DSC_BOT_CHAT_ID` (valor NUNCA em fórum, §82):
   - Tencent: `/home/ubuntu/.env.unificado` (o da ronda DSN) e `/root/.env.unificado`; backups `.bak_pre_dsc_bot_20260830_1407` em cada.
   - Dell (espelho Regra 4, sem perguntar): `Projeto Cafezinho Agentes/root/.env.unificado` e `Outros/chaves/agentes_labs/.env.unificado`; backups `.bak_pre_dsc_bot_20260830_1410`.
2. **Teste ao vivo**: `curl sendMessage` → **ok=True, message_id=18** ("🤖 DSN no ar!… · 20260830 14:14 BRT"). Miguel recebeu no Telegram.
3. **Ronda DSN configurada (30/30) — arquitetura ANTI-COLISÃO de getUpdates**:
   - Descoberta: o `getUpdates` do bot @dscelular_bot tem **UM único consumidor** = daemon `dsc-minibot.py` (root, servidor cafezinho-wp/us65, ativo desde 13:50), que replica pro `telegram_dsc/INBOX_MIGUEL.md` e entrega o `RESPOSTAS.md` no Telegram.
   - `ronda_dsn.sh` (Tencent): agora exporta **só as 2 vars** do bot (cirúrgico — não exporta o cofre inteiro p/ não interferir no roteador de LLM); backup `.bak_pre_dsc_telegram_20260830`; sintaxe `bash -n` OK.
   - `ronda_dsn_prompt.md`: seção nova **0b TERMINAL TELEGRAM DSC** — DSN lê `INBOX_MIGUEL.md` (que É a réplica do getUpdates), responde em `RESPOSTAS.md` (1º da fila, janela 40 min), pode enviar mensagem direta via sendMessage com as vars do ambiente; ⚠️ **PROIBIDO chamar getUpdates** — dois consumidores roubam mensagem um do outro. Backup idem.
4. **Bônus 1 — linha direta SSH us65→Tencent porta 22 PROVADA**:
   - Diagnóstico: ufw já liberava 22, mas o sshd só escutava na 38422 → "Connection refused" não era firewall (lição DSC-023 revalidada).
   - Fix: `sshd_config` com `Port 38422` + `Port 22` (backup `.bak_pre_port22_20260830`; `sshd -t` validou antes; `systemctl reload` sem derrubar sessões) + `ufw allow from 190.89.239.65 to any port 22` (us65 = cafezinho-wp, onde mora o daemon do DSC).
   - Prova real: `/dev/tcp` do us65 → **"ABERTA (TCP OK)"**.
   - Nota de segurança: as regras pré-existentes "22 ALLOW Anywhere" seguem no ufw; fail2ban ativo na Tencent mitiga. Apertar para só-us65 (remover Anywhere) **aguarda "vai" do Miguel**.
5. **Bônus 2 — rota B (DSC-025)**: chave `DEEPSEEK_CAFEZINHO_CANONICO` lida no `~/cofre_intake/cofre_intake.env` e enviada ao Telegram PRIVADO do Miguel pelo bot DSC (**ok=True, message_id=19, sha8 f0aaa272cec** = hash canônico já conhecido — confere com a memória de 29/08; método printf sem \n). Valor nunca apareceu em chat/fórum/log.
   - ⚠️ Cronologia honesta: o DS-Dell cumpriu a mesma DSC-025 às 14:03 pelo bot da ponte (@cafezinhoantigravitybot); a ordem desta missão (~14:05) foi escrita antes desse resultado virar público → **Miguel recebeu 2× a MESMA chave** (duplicata inofensiva em chat privado; sha8 bate).
6. **Fix incidental (família DS-097)**: o `de_dell.md` VIVO ficou 2× com marcadores de conflito no período (rebase interrompido — o `git pull --rebase` silencioso da ronda de prints engole erro no /dev/null). Resolvido preservando os dois lados (append-only); backup `.bak_pre_conflito_20260830_1415`. Lição: operar a ponte pelo REPO + commit imediato — meu 1º append no vivo foi varrido pelo sync na janela de corrida e precisou ser refeito.

## O que falta
- **Miguel**: repassar a chave DeepSeek ao @dscelular_bot no privado (o daemon cofra `sk-...` sozinho) — se ainda não fez.
- **Miguel**: decidir se aperta a ufw 22 para só-us65 (remover Anywhere) — precisa "vai".
- DSC-013 segue pendente (palavra-chave do pacote gpg ao DSC no celular).
- Conferir a 1ª ronda DSN com a seção 0b viva (= 14:30 BRT): log `/tmp/ronda_dsn/` na Tencent deve mostrar leitura do INBOX.
- Espelho pendente por design: token NÃO foi preciso no cafezinho-wp (daemon já tem o próprio) — se um dia o daemon passar a ler do cofre, espelhar lá também.

## O que preciso de você (Miguel)
1. Confirmar que recebeu os recados no Telegram: "DSN no ar" (#18) e a chave (#19 — e a do DS-Dell 14:03).
2. "Vai" ou não para apertar a porta 22 só pro us65.

— ZM · ZCode/GLM-5.3 · 20260830 14:20 BRT

---

# 🧪 ADENDO — SPRINT ROBÔ-PONTE (mini-DSC), testes T1–T6 — 30/08 ~14:52 BRT (ZM)

> Ordem DSC-027 (delegada ao ZCode na ponte 14:12). Daemon do DSC no us65 NÃO foi refeito — completado, corrigido (2 bugs) e testado.

## Resultado dos testes

| # | Teste | Resultado | Prova |
|---|---|---|---|
| T1 | texto → ack + INBOX + commit | ✓ | msgs reais 13:38 ("/start", "oi") → commits AUTO `9214e424e`/`a34de091e` em **3s/0s**; ack síncrono por desenho |
| T2 | áudio guardado + ponte avisada | ◐ | .ogg REAL salvo 13:55 (Opus 48kHz, 411667 bytes); ack+INBOX falharam NA ÉPOCA (bug `ts`, fix DSC 14:40 + revisão ZM 14:48); bloco INBOX **recuperado** com assinatura ZM; E2E aguarda áudio novo |
| T3 | RESPOSTAS.md → Telegram <60s | ✓ | **32s** (push 14:48:33 → journal `entregue: ZM` 14:49:05); msg 📮 [TESTE T3] entregue |
| T4 | timeout 40min → escalada fila | 🔶 armado | fila documentada em 3 lugares (README, CONTEXTO_MINI, ack) + prompt DSN; drill vivo exige janela real — não simulável sem falsificar fala do Miguel |
| T5 | 2º da fila posta VERIFIQUEI ✓ | 🔶 armado | README item 4; dispara na 1ª resposta real |
| T6 | chave sk- → cofre, nunca ponte | ✓ | estrutura (regex→cofre→continue antes do INBOX) + sandbox (cofre 600, INBOX limpo) + grep git zero ocorrências; cofre real intacto |

## Correções do ZM no daemon (us65, `/usr/local/bin/dsc-minibot.py`, backup `.bak_pre_zm_fix_20260830`)

1. **Dedup do SENT_FILE quebrado** — era `.split()` (tokens) vs chaves com espaço → 1 duplicata por restart (Miguel recebeu a resposta do DS-N 2× às 14:0x/14:41). Fix: `.splitlines()` + SENT_FILE deduplicado. 
2. **Log de entrega** — `print('entregue:', agent, tsag)` no journal: prova de latência e auditoria de entregas.
Restart 14:48, serviço `active`. Lição: bug de dedup só aparecia em restart — testes de fogo precisam incluir restart.

## Chave real + cérebro do mini-DSC

- Chave reenviada ao Telegram privado com instrução explícita de encaminhar ao @dscelular_bot (msg #24, 14:50). Cofre `/root/.dsc_deepseek_key` ainda vazio às 14:51 (aguardando forward).
- **Cérebro provado**: réplica exata da chamada do daemon (modelo `deepseek-chat`, system = persona mini-DSC + CONTEXTO_MINI, pergunta "o que tá rolando na casa hoje?") → resposta em personagem, curta, com emojis, usando o contexto correto (Quaest 268257, obra MOKA, ponte ativa, pendências) e respeitando o limite "só conversa/informa". A camada LLM arma sozinha quando a chave cair no cofre (interceptação sk- → arquivo → próxima mensagem do Miguel já é respondida com IA).

## DSN autônomo (passo 2 da sprint)

- (a) terminal: seção 0b do `ronda_dsn_prompt.md` — DSN lê o INBOX (réplica do getUpdates) a cada ronda 30/30; **nunca** chama getUpdates direto (consumidor único = daemon; dois consumidores roubam updates pelo offset). Ronda 14:30 já reportou o Telegram ao vivo.
- (b) resposta: 0b manda escrever em RESPOSTAS.md no formato do README (carimbo + RESPOSTA_PRO_MIGUEL + assinatura) como 1º da fila (janela 40 min).
- (c) NOVO: dever de manter `CONTEXTO_MINI.md` atualizado quando o estado da casa mudar (é o cérebro-contexto do robô).

## Estado / falta / preciso do Miguel

- **Estado**: robô completo, acordado, 2 bugs corrigidos, T1/T3/T6 provados, T2 parcial (fix pronto), T4/T5 armados, cérebro validado, fila documentada.
- **Falta**: forward da chave (arma a IA), áudio novo (T2 E2E), drill T4/T5 em janela real, Whisper (futuro).
- **Preciso do Miguel**: encaminhar a msg #24 ao @dscelular_bot e mandar qualquer pergunta no bot (a IA responde na hora) — e um áudio, quando puder, pro T2 fechar 100%.

## ✅ FECHAMENTO — 03/09/2026 15:03 BRT

- **DSC-013 ENCERRADO.** O Miguel lembrou a passphrase e rodou `~/desbloqueia_dsc.sh` no Dell (~15:02-15:03). Fluxo: senha digitada oculta (`read -s`) → gpg decifrou o pacote (senha só em memória do processo) → entrega via scp ao us65 → script apagado do Dell.
- **Prova da entrega (us65, 15:03 BRT):** `/root/dsc_credenciais/` (700) com `rclone_drive_token.txt` (493 B), `rclone_r2_b2.txt` (451 B), `telegram_ponte.txt` (68 B) — todos 600; `rclone.conf` no padrão `/root/.config/rclone/`.
- **A senha NUNCA saiu do Dell** — nem chat, nem ponte, nem Cérebro, nem histórico de shell. A cifra do pacote segue íntegra nas cópias (ninguém mais precisa abri-lo).
- **Limpeza do lembrete fixo:** `ronda_dsn_prompt.md` e `ronda_30min_prompt.md` (backups `.bak_pre_dsc013_20260903`); AGENDA_PENDENCIAS_MAESTRO item 12 → ✅; CONTEXTO_MINI do DSC atualizado; MONITORAMENTO_DE_TRABALHO ✅.
- **Correção de registro:** a nota antiga "ARQUIVADA (confusão do DS-N — não existe gpg/palavra-chave)" estava ERRADA — o pacote existia (5 cópias em disco) e foi aberto agora com a passphrase correta.
- **O que aconteceu / o que falta / o que preciso do Miguel:** aconteceu = pendência de 5 dias fechada sem exposição de segredo nenhum; falta = o DSC conferir/consumir as credenciais na próxima ronda (avisado em de_dell + CONTEXTO_MINI); preciso do Miguel = nada.

— ZCode/GLM-5.3 (ZM), 03/09/2026 15:0x BRT
