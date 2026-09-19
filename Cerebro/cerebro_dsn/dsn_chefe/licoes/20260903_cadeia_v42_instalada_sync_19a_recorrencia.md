# Lição 2026-09-03 · Cadeia V4.2 fechou sozinha e o sync comeu a ordem do vigia — marco objetivo + restauro verbatim do dono

## O quê
A cadeia automática do V4.2 Investimento fechou SOZINHA às 04:10:06 (watcher detectou as creds ESPELHO_WP_* no cofre → instalou o cron 14:00 com backup → se desligou e logou "INSTALADO"). Na MESMA janela, o sync d417f8d15 (04:22) comeu 4 conteúdos: o auto-desligar 10:30 BRT do v42_espelho_watcher.py (ordem do Miguel 03/09 ~02h), a REGRA DE TESTE NO ESPELHO (memória do v42_monitor + ADENDO 1 no fórum de reforma) e o feedback CL nº 26 no canal dos revisores (CL-103). Restaurei os 4 verbatim dos commits ancestrais; a linha da MEMORIA_VIVA do DS-Dell (pulso duas torneiras) ficou sinalizada ao dono — não mexi.

## Por quê
A ordem do Miguel ("solução automática que eu não precise fazer nada") troca o processo por marcos objetivos — e o sync-bug (DSC-049, kill-switch prazo 03/09) atacou exatamente os arquivos que guardam ordens do Miguel no território V4.2 (ZM/Chefe). Se ninguém restaurasse, o vigia do espelho seguiria rodando depois das 10:30 sem o auto-desligamento que o Miguel pediu, e a regra de teste realista (rascunho apagado ao final) sumiria no dia em que o 1º ciclo do Investimento vai rodar às 14:00.

## Como aplicar
1. Vigília de cadeia automática = conferir LOG + marco objetivo (INSTALADO / 1º rascunho _v42_*) com prova, e reportar ao Miguel no Telegram na hora do marco (msg direta assinada; desta vez message_id 37).
2. Smoke D4 antes do cron: perna viva = glm-5-turbo OK; qwen 429 (cota semanal) não é bloqueio — o teste roda na reserva, não espera (DSC-061).
3. Sync comeu arquivo com ordem do Miguel → restaurar VERBATIM do commit ancestral + linha de registro de restauro (nunca reescrever conteúdo, nunca `git add -A`); arquivo alheio sem ordem minha (memória do DS-Dell) = sinalizar no bloco para o dono restaurar.
4. Conferir crontab do teste à prova de UMA casa só (tencent preferida; NYC plano B DSC-060) — aqui o crontab não abre na sandbox, evidência = log INSTALADO + backup datado + rodar.sh.
5. Nota criativa do dia: 268731 Anvisa (suspensão de fabricação ≠ recall — medida sobre o processo, não sobre o produto).
