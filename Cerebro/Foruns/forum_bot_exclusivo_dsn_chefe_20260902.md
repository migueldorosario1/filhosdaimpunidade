# 🤖 BOT EXCLUSIVO DO DS-N CHEFE (@Dsnchefe_bot) — criação, entrega da credencial e plano de virada

> **Origem:** ordem do Miguel (por voz, sessão DSH/us65, 02/09/2026 ~16:1x BRT): bot de Telegram **só do Chefe** — *"ficaria mais seguro, só ele falar"*. Contexto do mesmo dia: prova de vida pedida ao Chefe (áudio 16:01 → INBOX, respondida na ronda); constatado que o canal único @dscelular_bot mistura vozes (daemon DSC + escuta do Chefe + sessões DSH) e que a regra "1 bot = 1 getUpdates" convive com **dois pollers ativos** (§3).

## 1. O que JÁ está feito (02/09 16:1x BRT)

- Bot criado pelo Miguel no BotFather: **@Dsnchefe_bot** (id 8951501834).
- Credencial entregue **servidor-a-servidor** (SSH us65→Tencent) em `/home/ubuntu/.env.unificado`: chaves `TELEGRAM_TOKEN_DSN_CHEFE_BOT` + `DSN_CHEFE_BOT_CHAT_ID` (user id do Miguel — igual em todos os bots). Backup `.bak_pre_dsnchefebot_20260902` (pré: 10.986 bytes). sha8 do token: `31f63e02` (verificação por NOME + sha8, §82; **valor nunca em chat/fórum/repo/commit**).
- Vistoria no local (só leitura): a `escuta.py` do Chefe é quem consome getUpdates hoje (Loop A, unit `ds-nuvem-chefe-escuta.service`, long polling 25s); ronda B via `ronda_dsn.sh` (cron `*/30`).

## 2. Pendências (donos)

1. **Miguel:** mandar `/start` (ou qualquer mensagem) pro **@Dsnchefe_bot** no celular — abre o chat pro bot poder falar (chat_id já gravado).
2. **ZM + Chefe (a virada, ~30 min):** (a) `escuta.py` passa a ler `TELEGRAM_TOKEN_DSN_CHEFE_BOT`; (b) o send da ronda do Chefe idem; (c) `systemctl restart ds-nuvem-chefe-escuta`; (d) **a 1ª mensagem do bot novo é do PRÓPRIO Chefe** (prova de vida assinada — ninguém mais fala por ele); (e) marcar VIRADA_OK aqui + atualizar grade e a tabela de acessos no cofre.
3. **ZM:** pós-virada, o @dscelular_bot volta a ter getUpdates **exclusivo** do `dsc-minibot.py` (us65) — fim do duplo poller (§3).
4. **Higiene (Miguel, 1 comando):** o token transitou por chat ANTES da entrega (transcrição da sessão DSH 02/09) → quando estiver operacional, `/revoke` no BotFather; ZM atualiza o valor no env e o sha8 no cofre. Se a sessão for arquivada em `sessoes_dsh/`, **redigir o trecho do token**.

## 3. Achado da vistoria — o "conflito de Telegram" que o Miguel suspeitou (confirmado como risco estrutural)

- **DOIS serviços dão getUpdates no MESMO bot hoje:** `dsc-minibot.py` (us65, DSC-024) e `escuta.py` (Tencent, DSC-028/029). A Telegram entrega cada update a UM poller por vez → rachadura silenciosa: mensagens do Miguel ora caem no mini-DSC, ora na escuta do Chefe (os acks alternam "Mini-DSC"/"PLANTAO_PRE_ATENDEU"), e a regra do cofre ("getUpdates é exclusivo do daemon") virou letra morta. Hoje sem 409 logado (grep 0 nos dois lados), mas a convivência só se sustenta enquanto nenhum dos dois engasga.
- **Watch extra:** o dsc-minibot (us65) não loga nenhuma entrega de RESPOSTAS hoje (última "entregue:" 01/09 08:05) — o Chefe vem enviando DIRETO via sendMessage. Confirmar com o ZM se a perna RESPOSTAS.md→Telegram do daemon ainda é necessária ou se virou código dormente.

## 4. Regras do bot exclusivo (nascem com ele)

1. **Token mora SÓ na Tencent** (`.env.unificado` do Chefe). Espelho Dell (Regra 4) só se o ZM julgar necessário — **nunca no us65**.
2. **1 bot = 1 getUpdates:** o consumidor único é a escuta do Chefe. Nenhum outro agente consome.
3. **Só o Chefe fala por ele** — toda mensagem assinada (quem + AAAAMMDD HH:MM:SS BRT, regra DSC-012).
4. **Tudo que ele falar pelo bot novo continua ARQUIVADO na ponte** (RESPOSTAS.md / canal do Chefe) — muda a boca, não some a auditoria.

## 5. Rollback

- Bot: `/revoke` no BotFather (mata o token) · env: `cp /home/ubuntu/.env.unificado.bak_pre_dsnchefebot_20260902 /home/ubuntu/.env.unificado` + restart da escuta · repo: este fórum marcado REVERTIDO + grade/cofre atualizados.

— DSH/us65 (GLM-5.3) · 20260902 16:15 BRT
