# 2026-09-03 · Correlação de sessão root se faz pela CHAVE e pela JANELA, não pelo IP

## O quê
A CL-109 (08:47) formalizou ao DS-Dell (missão especial — "deixa que eu faço isso aqui") a correlação das 2 sessões root "não atribuídas" da Tencent (00:07:41 / 00:10:15) do incidente 268714 (metas `_cafezinho_img_check`/`_cafezinho_txt_isenta` sumiram entre 22:08 e 00:14; gate reverteu o post para pending). Com ssh root read-only ao us65 (cafezinho-wp), a correlação fechou do lado servidor:

1. **Pela CHAVE (authorized_keys + fingerprint), não pelo IP:** `ssh-keygen -lf` em cada chave do `/root/.ssh/authorized_keys` casou as sessões observadas no auth.log aos donos:
   - 43.156.151.165 (tencent), ED25519 `wB+pG1u1...` = auth[6]/auth[8] ("migueldorosario@novo" ED25519 = **"vigia-central"**) — a MESMA identidade das sessões periódicas do tencent (00:05:28 · 00:20:09 · 00:30:10 · 00:50:10, batendo com os ciclos R1/R2 :05/:20) → as "não atribuídas" NÃO são estranhas: são a automação vigia/tencent da casa.
   - 189.99.98.64 (Vivo casa), RSA `k+A3E5eN...` = auth[5] "migueldorosario@novo" → máquina do Miguel/launchers (CL/AGY).
   - 159.65.177.60, ED25519 `4+xZ5Eq1...` = auth[7] "cafezinho-news-sync@159.65.177.60" (nyc, com from= restrito).
2. **Pela JANELA (quem mais estava ativo no intervalo do incidente):** durações — 00:07:41 = 2s (sessão 259808, comando único remoto); **00:10:15 = ~25s (sessão 261051: aberta 00:10:19, fechada 00:10:40 — janela real de operação, ~2 min antes do slot)**. E o ACHADO: **189.99.98.64 fez 68 sessões root em 02/09 22:00-24:00 + 26 em 03/09 00:00-00:30**, com rajadas 23:17-23:39 e **00:12:21→00:16:28 (bem na janela do gate que reverteu o 268714 às 00:14:32)** — como os metas sumiram entre 22:08 (cl088 gravou) e 00:14, e **de 22:08→23:59 o ÚNICO ator SSH foi 189.99.98.64**, se o apagamento foi antes da meia-noite o suspeito é o lado launchers, não o tencent.
3. **O que o servidor NÃO pode dizer:** cron local do us65 não apaga meta (só o escalonador `wp cron event run --due-now` a cada :01; `verificador_virada.sh` COMENTADO desde 01/09 — PARADO_CONTRATO); wp é phar stock (sem log de comando); sessão root direta não passa por sudo → o COMANDO não fica no auth.log. Fecho honesto: identidade atribuída + janela estreitada + 2º ator revelado; o que cada lado RODOU (tencent às 00:07:41/00:10:15; launchers às 23:17-23:39 e 00:12-00:16) é dos donos (ZM/vigia e CL/AGY) — registro + pergunta, não cobrança.

## Por quê
- O registro do incidente dizia "sessões root da Nuvem (43.156.151.165) às 00:05/00:07/00:10:15/00:20 não atribuídas" — mas "não atribuída" era falta de correlação, não falta de identidade: a chave estava no authorized_keys do próprio servidor, e a cadência periódica da MESMA chave provava que era automação legítima da casa, não intruso.
- Só olhar o IP (43.156.151.165 = tencent) teria mantido o foco errado: a JANELA mostrou um segundo ator (189.99.98.64, a máquina do Miguel/launchers) ativo durante TODO o intervalo do sumiço — inclusive numa rajada exatamente na janela do gate. Correlação de incidente pergunta "quem MAIS podia ter feito", não "quem eu suspeito".
- A física ensina o limite do método: auth.log registra quem entrou e por quanto tempo, não o que rodou (root direto, sem sudo, wp sem wrapper de log). Saber o limite é o que separa o fecho real do "não confirmado" honesto.

## Como aplicar
- Correlacionar sessão suspeita: (1) fingerprint no authorized_keys do servidor → dono da chave; (2) cadência da mesma chave (sessões periódicas = automação conhecida, não intruso); (3) duração da sessão (2s = comando único; 25s = operação real); (4) JANELA completa do incidente: listar TODOS os atores SSH no intervalo (não só o apontado), inclusive os "de confiança".
- Ler auth.log com a régua do servidor: `grep -E "Sep  3 00:(0[0-9]|1[0-9])" /var/log/auth.log | grep sshd` + `ssh-keygen -lf` nas chaves autorizadas + `crontab -l` (o que roda local) — tudo read-only, sem tocar produção.
- O que o servidor não loga (comando da sessão root direta) vira pergunta ao DONO de cada lado — registro com dono formal, sem acusação.
- Missão especial de correlação cabe ao DS quando a física alcança a PORTA (ssh root read-only ao us65 existe) — assumir com "deixa que eu faço isso aqui" e entregar o fecho + o que falta, cada coisa com seu dono.

— DS Miguel (Dell) · 20260903 09:08 BRT
